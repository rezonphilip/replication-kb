---
doc_id: PLT-IREP
type: overview
mechanism: [irep, smartsync]
group: irep-config
runs_on: [office, vessel]
components: [ComINT, ExportCDT, ExportDCS, ImportDES, ImportDSC, ImportRBP, ComPBR]
log_files: [ComINTServiceLog_.txt, CDTServiceLog_.txt, DcsServicePalLog_.txt, DesServiceLog_.txt, DscServiceLog_.txt, RbpServiceLog_.txt, PbrServiceLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["iRep snapshot staged 2026-11-11 (no git commit available)", "MS-REP snapshot staged 2026-11-11"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# iRep (SmartSync+, "sync+") — overview

iRep — internally SmartSync+ or sync+ — replicates table changes between office and vessel databases using SQL Server change tracking on the export side and staged replica tables on the import side. It is made of seven .NET services, and it uses SmartSync (the MS-REP transport services) to move its packets. This article maps the services, databases, logs and troubleshooting entry points; read it before any component article.

> The platform has three mechanisms: **Priority Replication (PR)** — MS-REP services (PLT-MSREP-OVERVIEW); **iRep / sync+** — this section; **SmartSync (sync)** — the transport layer used by both (RepAzure, RepSbus, RepAzureRes, RepTransfer, with RepIntegration as the entry point for iRep transfers).

## The services

Seven services make up sync+: two export, three import, one configuration gateway and one inspection service. Keywords: sync+, smartsync+, irep services, CDT, DCS, DES, DSC, RBP, PBR, ComINT.

| Service | Role | Runs by itself? | Log file | Article |
|---|---|---|---|---|
| ComINT | Configuration gateway: returns database connection settings per replica type | No (worker does nothing, see CMP-COMINT) | ComINTServiceLog_.txt | CMP-COMINT |
| ExportCDT | Reads SQL change tracking, writes changed row ids into REP2X record-sync tables, routes them per vessel | Yes, timer | CDTServiceLog_.txt | CMP-EXPORTCDT |
| ExportDCS | Builds `.tzst` packets per vessel from REP2X, records them and hands them to RepIntegration for transfer; resends | Yes, timer; also called by ExportCDT | DcsServicePalLog_.txt | CMP-EXPORTDCS |
| ImportDES | Validates received packets (name, counter, splits) and reads them into REP2I staging tables | Yes, timer | DesServiceLog_.txt | CMP-IMPORTDES |
| ImportDSC | Compares packet schema with replica tables and creates/alters REP2I tables | No, called by ImportDES | DscServiceLog_.txt | CMP-IMPORTDSC |
| ImportRBP | Applies REP2I staged rows to PAL (directly or through application endpoints), reprocesses failures | Yes, timer; also called by ImportDES | RbpServiceLog_.txt | CMP-IMPORTRBP |
| ComPBR | Reads packet headers/zip contents and writes consolidated packet information | Yes, timer | PbrServiceLog_.txt | CMP-COMPBR |

The acronym expansions (CDT = change data tracking is clear from code; DCS, DES, DSC, RBP, PBR are not spelled out) are an open question.

## Databases and replica types

sync+ works with four database roles, and every service picks its connections by **replica type id**. Keywords: PAL, PAL_REP, REP2X, REP2I, replica type, ReplicaTypeId, AzureDB.

- **PAL** — application database (primary and read-only secondary). Change tracking is read here; RBP applies rows here.
- **REP2X** — export staging: record-sync tables, vessel export queues, packet counters, outgoing packet headers (OutPacketHd), resend logs, export configuration.
- **REP2I** — import staging: DES validate/process queues, replica (`_REP`, `_REP_DEL`) tables, skip/error data, RBP queries and endpoints.
- **PAL_REP** — replica type with its own PAL-side settings.

In code and logs, **"Azure DB"/"AzureDB" means the REP2X/REP2I staging SQL database**, not Azure Blob storage. Log text such as "SaveCdtLastExtractedVersion to Azure DB Failed" is a database failure, not a transport failure.

Replica types configured in ComINT (`ComINT/Mariapps.PAL.ComINT/appsettings.json#L43-L60`): 1 NORMAL, 2 ATTACHMENTS, 3 PAL_REP, 4 REP2X, 5 REP2I, each with `IsEnabled`. ExportCDT skips disabled replica types (`ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L122`). See DATA-IREP for tables and procedures.

## End-to-end path

A change in PAL reaches the other side through CDT → DCS → RepIntegration/RepTransfer → SmartSync → RepAzure → RepDBLogW → DES → DSC → RBP. Keywords: end to end, irep flow, export import path, where is my data.

1. **ExportCDT** reads change tracking per table in the export order and writes REP2X record sync, then routes rows per vessel (record vessel sync). See FLW-IREP-EXPORT.
2. ExportCDT calls **ExportDCS** `ExportDcs/InitateExportProcess` when `DcsCallEnabled` is on (`ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L272-L276`). DCS builds a packet per vessel, moves it to the outbox, increases the packet counter and saves OutPacketHd.
3. DCS calls **RepIntegration** `Integration/TransferGeneral` (`ExportDCS/Mariapps.PAL.RepExportDCS/services.json`), which passes the packet to **RepTransfer** / SmartSync for upload (CMP-REPINTEGRATION, CMP-REPTRANSFER, CMP-REPAZURE).
4. On the receiving side **RepAzure** downloads it. RepAzure has an iRep step `ReadIRepFolderFile` (`RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L434`), and RepDBLogW `SaveIRepValidateFile` (`RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L717`) inserts the packet into the REP2I DES validate queue through `REP_INS_DES_VALIDATE_Q_ITEM` (`RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/Rep2IDbRepository.cs#L79`). The class that connects the two (`MoveOperationBL`) is not in the staged source — open question.
5. **ImportDES** validates the packet, moves it to the process queue, reads it into REP2I, and calls **ImportDSC** for schema comparison when needed. See FLW-IREP-IMPORT.
6. ImportDES calls **ImportRBP** `RepImportRBP/RepImportSync` (`ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L276-L278`), which applies the rows to PAL.

## Common behaviour of all sync+ services

All sync+ services share in-memory "running" state, settings from appsettings plus ComINT, cache-clear routes, an EvaluateConfig route, and Serilog at Error level. Keywords: running flag, cache, EvaluateConfig, log level, restart.

- **In-memory run flags.** ExportCDT and ImportRBP claim a per-replica-type run token (`TryStartProcess`) before working; a second cycle is skipped while it is set. The flag has **no expiry** — a hung run blocks that replica type until the service restarts or the clear route is called (`ExportCDT/Mariapps.PAL.RepExportCDT.Model/Common/ProcesStatusEntity.cs#L60-L80`; route `RepImportClearProcessStatusList`, `ExportCDT/Mariapps.PAL.RepExportCDT/Controllers/RepExportCDTController.cs#L74`). ExportDCS and ImportDES keep queue-running flags and process state in their cache instead.
- **Connection settings come from ComINT on every cycle.** ExportCDT and ImportRBP return the ComINT answer directly; the caching code after the return is unreachable (`ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L62-L63`, `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L47`). If ComINT is down, these services stop. ComINT serves its own appsettings loaded once at startup (`ComINT/Mariapps.PAL.ComINT/Startup.cs#L39`), so a configuration change needs a ComINT restart.
- **EvaluateConfig.** Every service except ComINT exposes `EvaluateConfig`, which checks settings, database objects and paths; the dashboard can call these routes as safe health probes (CFG-IREP).
- **Logging hides most warnings.** Every appsettings sets Serilog minimum level Error (`ExportCDT/Mariapps.PAL.RepExportCDT/appsettings.json#L3-L4`). Skip/retry messages, "CheckCdtVersion validation failed … retry", "Export process start skipped" and "Incorrect packet counter" never reach the log. Conversely some normal status lines ("Process started", "CACHE_CHEKING") are logged at Error — see ISS-PLATFORM-BENIGN and ISS-IREP-LOG-001.

## Troubleshooting entry points

Start from the symptom, then open the card; every log template in the code is mapped to a card in `catalog/failure-points.yaml`. Keywords: troubleshooting, where to start, irep not working, sync+ issue.

| Symptom | First card |
|---|---|
| Nothing exported for a table | ISS-IREP-CDT-001, ISS-IREP-CDT-002 |
| CDT stops right after version change / upgrade | ISS-IREP-CDT-003 |
| All sync+ services fail at once | ISS-IREP-CFG-001 (ComINT) |
| CDT runs but no packets are created | ISS-IREP-DCS-001 |
| One vessel never gets packets / never validated | ISS-IREP-DCS-002 |
| Packets created but not delivered | ISS-IREP-DCS-003 |
| Packets in inbox but not imported | ISS-IREP-DES-001, ISS-IREP-DES-002 |
| Some rows missing after import | ISS-IREP-DES-003 |
| Rows in REP2I but not in PAL | ISS-IREP-RBP-001 |
| Service silent or stuck | ISS-IREP-STUCK-001, ISS-IREP-LOG-001 |

Group cards (ISS-IREXP-*, ISS-IRIMP-*, ISS-IRCFG-*, ISS-IRPBR-*) cover every other failure point by failure class; INV-FAILURE-POINTS shows the coverage.

## Security notes

The staged iRep code contains sensitive settings; locations only, never values. Keywords: security, secret, connection string in log.

- ComINT returns full connection strings over HTTP to any caller (`ComINT/Mariapps.PAL.ComINT/Controllers/ComINTController.cs#L28-L31`).
- ExportCDT and ImportRBP write connection string fields into Error logs when settings are invalid ("Invalid connectionString settings … PrimaryDB: …") (`ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L163`). Treat CDT/RBP logs as sensitive.
- ImportRBP logs the HTTP response body of application endpoints (`ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L691`).
- Monitoring keys and alert e-mail settings are present in appsettings/code — listed by file and key name in the review file.

## Related

CMP-COMINT, CMP-EXPORTCDT, CMP-EXPORTDCS, CMP-IMPORTDES, CMP-IMPORTDSC, CMP-IMPORTRBP, CMP-COMPBR, FLW-IREP-EXPORT, FLW-IREP-IMPORT, DATA-IREP, CFG-IREP, INV-IREP, INV-IREP-DB, INV-FAILURE-POINTS, PLT-MSREP-OVERVIEW
