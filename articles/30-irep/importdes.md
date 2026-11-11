---
doc_id: CMP-IMPORTDES
type: component
mechanism: [irep]
group: irep-import
runs_on: [office, vessel]
components: [ImportDES]
log_files: [DesServiceLog_.txt]
error_types: [packet, sequence, config, file, dataapply]
applies_to_versions: ["Not determined from code"]
sources: ["iRep snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# ImportDES — packet validation and reading

ImportDES takes received sync+ packets from the REP2I validate queue. It checks each packet against this environment and against the vessel's expected packet counter, then moves it to the process queue. The read queue unpacks the packet into REP2I replica tables, asks ImportDSC to compare schemas, and finally triggers ImportRBP. Packets that "arrived but never appeared in PAL" usually stop here.

## How it runs

One timer drives two queues per replica type, validate and read/process, and each queue has its own running flag. Keywords: DES worker, validate queue, process queue, read queue, InvokeAllReplicaTypeWorker, config status.

- **Timer.** The worker calls `InvokeAllReplicaTypeWorker` every `CheckIntervalInMin` minutes (minimum 1) when `InitiateOnInterval` is true. Unhandled errors are logged as "Unhandled error in process cycle" and the loop continues (`ImportDES/Mariapps.PAL.RepImportDES/WorkerService.cs#L27-L80`).
- **Replica list.** It reads the replica list from ComINT on every cycle. If the list is empty it logs "No replica configuration loaded from common integration service" (`ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L272-L280`).
- **Cache reload.** The init data is reloaded only when neither queue is running. Otherwise it logs "Process already running so not changing cache data" (L348-L361).
- **Validate queue** (L407-L446). It starts only if the config status is SUCCESS and `TryStartValidateQueueProcess` gets the flag.
- **Read queue** (L481-L530). It starts under the same two conditions, using its own flag. If the config status is FAILED, it logs a **Warning** with the reason (L528-L530).

## Validate queue

`ImportValidateBL` reads the first pending row of `REP_DES_VALIDATE_QUEUE` and checks it (`ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L100-L216`). Keywords: packet name validation, unique code, destination, tzst, split, old packet, incorrect packet counter, skip list, error folder.

1. **Row sanity.** A row with no file name or location, a packet counter of 0, or a file that is not on disk is deleted from the queue and recorded as skipped data (L584-L658). Several of these "Deleted entry … successfully" lines are logged at Error level although they are status lines.
2. **Vessel configuration** (L168-L172). If the vessel has no basic configuration, it logs "Vessel {id} basic configuration does not exist skipping". Invalid-config vessels go to a skip list (L330-L333, ISS-IREP-DCS-002).
3. **Packet counter** (`HandlePacketCounter`, L237-L345). The counter has one of three states:
   - **Valid:** continue.
   - **Old** (already applied): the queue row is deleted and the file moves to the error path. This is logged at Information only (L261-L271).
   - **Incorrect** (a gap): the vessel goes on the counter-mismatch list, a missing-packet status is written, and the **Warning** "Incorrect packet counter … received for vessel" is logged. The vessel is skipped "untill next cycle" (L293-L328, ISS-IREP-DES-002).
4. **Packet name** (L356-L369). Unique code, destination (vessel id), type (replica type), packet number and the `tzst` extension must all match. Otherwise an exception is thrown and the packet is moved to the error folder (ISS-IREP-DES-001).
5. **Split files** (L371-L411). The packet must have all its split files. Otherwise it logs "Incomplete packet split … Expected splits …, found …" (Warning) and waits.
6. **Success** (L416-L420, L488). The files move to the in-temp folder, the row is added to the process queue, and the counter is updated. If that update fails: "Packet counter updation failed" (L542).

## Read / process queue

`ProcessQBL` reads packets in parallel (`maxDegreeofParallelisation`) and writes rows into REP2I through `DesReaderBL` (`ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L255-L282`). Keywords: DES reader, bulk write, data skipped, schema compare, next service, RBP call.

- **Table lookup.** For each table in the packet it looks up the table name and the attachment path. Missing entries log "Table name not found for table …" or "Attachment base path not found" (`ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L261-L276`).
- **Schema compare.** It calls ImportDSC `RepImportDSC/RepImportSchemaCompare` (`ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L358`). An empty result logs "schema comparison failed" (L197, ISS-IREP-DES-003).
- **Bulk writes.** Bulk writes that reject rows log "Bulk write rejected row data … Retrying in smaller parts to skip only the bad rows" (Warning). The rows that are finally dropped are logged "[DATA_SKIPPED] Skipping row ID …" (`ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L128-L229`).
- **After the read loop** (`ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L269-L282`):
  - If `InvokeNextService` is on, it calls the "next service". **services.json points it at `ImportDes/ValidatePacket`, a route the DES controller does not have** (`ImportDES/Mariapps.PAL.RepImportDES/services.json`), so this call fails whenever the flag is on (open question).
  - If `InvokeRbpService` is on, it calls ImportRBP `RepImportRBP/RepImportSync`. An RBP failure is logged at Debug only, plus the Warning "RBP service call returned an HTTP error".

## Routes

All routes are under `ImportDes/` (`ImportDES/Mariapps.PAL.RepImportDES/Controllers/RepImportDesController.cs`). Keywords: SetAllInitData, ReadAllCacheKeyValues, DeleteAllCacheKeys.

| Route | Purpose | Line |
|---|---|---|
| `SetAllInitData` | Reload the startup configuration (fixes "Config Status is false") | L37 |
| `InvokeAllReplicaTypeWorker` | Run both queues now | L44 |
| `DeleteAllCacheKeys` | Clear stale flags, skip lists and counter lists | L51 |
| `ReadAllCacheKeyValues` | Read-only view of the cache (skip lists, processing vessels, error counters). Good dashboard probe | L58 |
| `GetVersion`; `EvaluateConfig` (ConfigEvaluationController) | Version and configuration check | L65 |

## Failure-point coverage

The specific cards are ISS-IREP-DES-001 to -003, ISS-IREP-DCS-001 (config status), ISS-IREP-DCS-002 (invalid config vessel) and ISS-IREP-STUCK-001. All other templates fall under ISS-IRIMP-*. Keywords: DES errors.

## Related

PLT-IREP, CMP-IMPORTDSC, CMP-IMPORTRBP, FLW-IREP-IMPORT, DATA-IREP, ISS-IREP-DES-001, ISS-IREP-DES-002, ISS-IREP-DES-003
