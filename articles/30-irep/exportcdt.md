---
doc_id: CMP-EXPORTCDT
type: component
mechanism: [irep]
group: irep-export
runs_on: [office, vessel]
components: [ExportCDT]
log_files: [CDTServiceLog_.txt]
error_types: [dataapply, db, config, stuck]
applies_to_versions: ["Not determined from code"]
sources: ["iRep snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# ExportCDT — change tracking extraction

ExportCDT is the first step of the sync+ export. For every enabled replica type it reads SQL Server change tracking in PAL, writes the changed row ids into REP2X record-sync tables, and splits them per vessel. It then calls ExportDCS to build packets. If ExportCDT fails, nothing new is packed, but already-built packets still flow.

## How it runs

A timer drives one run per enabled replica type, and an in-memory run token guards each run. Keywords: CDT worker, CheckIntervalInMin, RepChangeTrackAsync, TryStartProcess, run token.

**Timer.** The worker calls `RepChangeTrackAsync` when `EnableWorkerService` is true (`ExportCDT/Mariapps.PAL.RepExportCDT/WorkerService.cs#L44-L67`). The interval is `CheckIntervalInMin`. If that is 0, it falls back to `SchedulerIntervalInMinutes`, and then to 30 minutes (`ExportCDT/Mariapps.PAL.RepExportCDT/WorkerService.cs#L72-L82`). Exceptions are caught and logged as "WorkerService ExecuteAsync, ErrorMessage", and the loop continues.

**Per replica type** (`ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L92-L249`):

1. Get the connection list from ComINT on every run (L94). The cache code after the early return at L63 is unreachable.
2. Skip replica types with `IsEnabled` false (L122). The skip is logged as "CDT not enabled for ReplicaTypeId …".
3. Claim the run token with `TryStartProcess` (L135). If the token is taken, the replica type is skipped silently for this cycle.
4. Run `RepChangeTrack` in a background task (L151-L181). If `ClearCacheEnabled` is on, clear the CDT caches (L184-L189).
5. Release the token in `finally` (L211-L213). If an administrator force-cleared the token meanwhile, the warning "Process status not released by this run … force-cleared" is logged (L214).

The token has no expiry (`ExportCDT/Mariapps.PAL.RepExportCDT.Model/Common/ProcesStatusEntity.cs#L60-L80`). A run that hangs blocks the replica type until a restart or `RepImportClearProcessStatusList` (`ExportCDT/Mariapps.PAL.RepExportCDT/Controllers/RepExportCDTController.cs#L74`).

## The CDT sequence

`CDTChangesInsert` performs these steps in order. Most steps return early on failure, which leaves REP_RECORD_SYNC rows for the next cycle (`ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L40-L228`). Keywords: InsertIntoRecordSync, SaveCdtLastExtractedVersion, GetMaxId, CheckCdtVersion, latency, InsertIntoRecordVslSync, ClearSpam, DeleteDataFromRecordSync.

| # | Step | Database | On failure | Line |
|---|---|---|---|---|
| 0 | Validate the connection settings | — | "Connection not feteched properly … PrimaryDB: …" (logs connection fields), stop | L46-L50 |
| 1 | `InsertIntoRecordSync`: for each table in `[REP].[EXPORT_TABLE_ORDER]`, run the CDT query (`CHANGETABLE`) and insert changed ids | PAL → REP2X | Per table: "TableId … Error"; the other tables continue | L56 |
| 2 | `SaveCdtLastExtractedVersion` on the PAL primary (returns the current version) | PAL | "…to PAL Primary DB Failed", stop | L59-L66 |
| 3 | Save the same version in REP2X | REP2X | "…to Azure DB Failed", stop | L71-L78 |
| 4 | `GetMaxId` of record sync | REP2X | "GetMaxId failed", stop. A result of 0 logs "MaxId 0 found, not continuing" (Error level, but normal when nothing changed) | L81-L94 |
| 5 | Measure primary-to-secondary latency, then `CheckCdtVersion` on the read-only replica; retry 3 times, 2 s apart | PAL secondary | Retries are logged at Information only; afterwards "CheckCdtVersion validation failed" or "failed" | L98-L113, L220-L225 |
| 6 | `InsertIntoRecordVslSync` and its delete counterpart: per table, run the vessel routing query from `[REP].[REP_EXPORT_VESSEL_QUERY]` (office or vessel variant) | PAL secondary → REP2X | Per table: "Query not found, skipping", "TableId 0, skipping", "MaxId 0, skipping", SQL errors | L122-L125 |
| 7 | `ClearSpam` between the min and max record-vessel-sync ids | REP2X | "ClearSpam failed" (continues) | L130-L135 |
| 8 | Save the extracted version in REP2X again | REP2X | "SaveCdtLastExtractedVersion Azure DB Failed" (continues) | L137-L142 |
| 9 | `DeleteDataFromRecordSync` for rows routed successfully (insert, then delete) | REP2X | "DeleteDataFromRecordSync Azure DB Failed" (continues) | L147-L159 |
| 10 | If `LogErrorToDB` is ENABLED, write the routing failures to the REP2X error log | REP2X | failure JSON lines at Error level | L161-L215 |

After `CDTChangesInsert`, if `DcsCallEnabled` is on, ExportCDT calls ExportDCS `ExportDcs/InitateExportProcess` (`ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L267-L277`). "DcsServiceCallAsync End" is logged at Error level, but it is a status line.

Important behaviours:

- **The version is saved before routing succeeds** (steps 2-3 run before step 6). Rows that fail routing stay in REP_RECORD_SYNC and are retried on the next run. If REP_RECORD_SYNC is cleaned up by hand, those changes are lost. Not determined from code: whether a later run can recover them.
- **Change tracking must be enabled on every table in the export order.** The 2024 sample log shows "Change tracking is not enabled on table …" repeating every cycle for the same tables (`ExportCDT/Mariapps.PAL.RepExportCDT/Logs/Export_CDT_20240415.txt#L3`). See ISS-IREP-CDT-001.
- **A wrong routing query fails every cycle.** The sample log shows "The multi-part identifier … could not be bound" from a routing query (`ExportCDT/Mariapps.PAL.RepExportCDT/Logs/Export_CDT_20240415.txt#L78`). See ISS-IREP-CDT-002.
- **A procedure that does not match the service version fails every cycle.** The sample log shows "Must declare the scalar variable "@STATUS"" from CheckCdtVersion (`ExportCDT/Mariapps.PAL.RepExportCDT/Logs/Export_CDT_20240415.txt#L42`). See ISS-IREP-CDT-003.

## Routes

Every route works per replica type, or for all types when the id is 0. Keywords: RepExportCdt route, ClearAllCache, ReleaseSpamEntries, EvaluateConfig.

| Route | Purpose | Line |
|---|---|---|
| `RepExportCDT/RepExportCdt` | Run CDT now | `ExportCDT/Mariapps.PAL.RepExportCDT/Controllers/RepExportCDTController.cs#L39` |
| `ReleaseSpamEntries`, `SendSpamEntriesList` | Release rows held as "spam"; e-mail the list through EAS | L46, L53 |
| `ClearAllCache`, `ClearAllCacheByKey` | Drop the cached CDT and routing queries (needed after changing a query row) | L60, L67 |
| `RepImportClearProcessStatusList`, `RepImportClearResponseList` | Clear the run tokens and responses | L74, L88 |
| `Version`, `EvaluateConfig` | Version and configuration check | L102, L109 |

## Spam entries

Spam handling holds back record-vessel-sync rows that look abnormal and can send an alert mail. Keywords: spam, ClearSpam, ReleaseSpamEntries, EAS mail, alert.

`SendSpamEntriesList` reads the spam rows and builds an HTML table. It posts the table to EAS using `easBaseUrl`, `easSendUrl` and `easConfigKey` from REP2X, plus To/CC/BCC from `AlertMailConfiguration` (`ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L368-L442`). If any of these is missing, it logs "… configuration not found". The rule that makes a row "spam" sits in the database procedure; see DATA-IREP. Not determined from code: the business meaning of spam.

## Failure-point coverage

Every log template of ExportCDT is mapped to a card. Keywords: CDT errors, failure points.

The main hand-written cards are ISS-IREP-CDT-001/002/003, ISS-IREP-CFG-001 and ISS-IREP-STUCK-001. The remaining templates are covered by ISS-IREXP-DB, -DATAAPPLY, -CACHE, -CONFIG and -HTTP. See `catalog/failure-points.yaml`, filtered by service ExportCDT.

## Related

PLT-IREP, CMP-EXPORTDCS, FLW-IREP-EXPORT, DATA-IREP, CFG-IREP, ISS-IREP-CDT-001, ISS-IREP-CDT-002, ISS-IREP-CDT-003
