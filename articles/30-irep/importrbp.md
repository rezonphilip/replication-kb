---
doc_id: CMP-IMPORTRBP
type: component
mechanism: [irep]
group: irep-import
runs_on: [office, vessel]
components: [ImportRBP]
log_files: [RbpServiceLog_.txt]
error_types: [dataapply, http, db, stuck]
applies_to_versions: ["Not determined from code"]
sources: ["iRep snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# ImportRBP — applying staged rows to PAL

ImportRBP is the last step of the sync+ import. It takes the REP2I read queue entries for inserts/updates and for deletes. For each table it posts the staged rows to the application endpoint configured for that table. When a batch succeeds, it deletes the processed rows from the `_REP` / `_REP_DEL` table. Rows that "arrived on the vessel but are not visible in the application" are usually still waiting here.

## How it runs

ImportRBP is driven by its own timer and by calls from ImportDES. An in-memory run token guards each replica type, and a reprocess job runs on a long interval. Keywords: RBP worker, RepImportSync, run token, reprocess, RepreocessIntervalInHours.

**Timer.** The worker calls `RepImportPacketAsyn` each cycle (`ImportRBP/Mariapps.PAL.RepImportRBP/WorkerService.cs#L44-L79`). The interval is `CheckIntervalInMin`; if that is 0 it uses `SchedulerIntervalInMinutes`. Errors are logged as "WorkerService ExecuteAsync, ErrorMessage", and the loop continues.

**Reprocess.** When `ReprocessEnabled` is on, `ReplicaRecordsReprocess` runs every `RepreocessIntervalInHours` hours, or every 12 hours if that is 0 (`ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L104-L135`). Note the misspelled key name `RepreocessIntervalInHours`. The last-run time is held in memory, so a restart resets it.

**Per replica type** (L150-L260):

1. Read the connection list from ComINT on every cycle (L47). The cache code after the return is unreachable.
2. Check that RBP is enabled for the replica type. If not: "RBP not enabled for ReplicaTypeId" (L149).
3. Validate the connection string fields. If they are invalid: "Invalid connectionString settings …". This line logs connection fields, so treat it as sensitive (L184).
4. Claim the run token with `TryStartProcess` (L159), and release it when the run completes (L233-L257). As in ExportCDT, the token has no expiry; the clear route is `RepImportClearProcessStatusList`.

## Applying data

`RepImportPacket` works in fixed order: endpoint details first, then deletes, then inserts/updates, then deletes again. Keywords: GetEndPointDetails, INS_OR_UPD, DEL, application API, _REP table, _REP_DEL table, batch.

1. **Read the endpoint details.** Each table has a base URL and a destination API (`USP_GetEndPointDetails`; `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L360`).
2. **Process the read queue.** It reads the queue for `DEL`, then `INS_OR_UPD`, then `DEL` again, marking each entry in-progress as it reads it (L363-L402).
3. **Apply each table** (`RepImportPacketSubUpdate` / `ProcessInsertUpdateData`, L482-L590):
   1. Resolve the table name from the table id. If it cannot: "Table name not found for TableId".
   2. Read the rows from `<table>_REP` (insert/update) or `<table>_REP_DEL` (delete) in batches.
   3. Post each batch as JSON to `BASEURL/DESTINATIONAPI` (L546). The method is called `SimulateApiCall`, but it makes a **real HTTP POST** (L677-L692).
   4. If the call succeeds, delete the processed rows (L550). If some rows cannot be deleted, it logs "{n} of {m} processed rows c…" (L734). A batch delete that fails is retried row by row (`ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L814`).
   5. If the call fails, it logs "API call failed for table …, batch …" and the rows **stay** in the `_REP` table for reprocessing (L566-L570).
4. **Clean up.** It deletes the processed DES proc-live-data rows (L418-L428), marks the queue completed (L437), updates the job-queue percentage (L452), and writes failures to the REP2I error log (L468).

`RepImportUsingInqueue` is a separate path. It reprocesses entries from the reprocess in-queue into the replica tables and the proc-live-data import queue (L287-L319).

## Routes

All routes are under `RepImportRBP/` (`ImportRBP/Mariapps.PAL.RepImportRBP/Controllers/RepImportRBPController.cs`). Keywords: RepImportSync route, RepImportUsingInqueue, clear process status.

| Route | Purpose | Line |
|---|---|---|
| `RepImportSync` | Apply now (called by ImportDES) | L30 |
| `RepImportUsingInqueue` | Reprocess in-queue entries | L37 |
| `ClearAllCache`, `ClearAllCacheByKey` | Clear the caches | L47, L54 |
| `RepImportClearProcessStatusList`, `RepImportClearResponseList` | Clear run tokens and responses | L61, L75 |
| `Version`; `EvaluateConfig` | Version and configuration check | L89 |

## Failure-point coverage

The specific cards are ISS-IREP-RBP-001, ISS-IREP-CFG-001 and ISS-IREP-STUCK-001. All other templates fall under ISS-IRIMP-*. Security: the failure line logs the application response body (L691). Keywords: RBP errors.

## Related

PLT-IREP, CMP-IMPORTDES, FLW-IREP-IMPORT, DATA-IREP, ISS-IREP-RBP-001
