---
doc_id: CMP-REPINTEGRATION
type: component
mechanism: [priority-replication, irep]
group: orchestrator
runs_on: [office, vessel]
components: [RepIntegration]
log_files: [IntegrationServiceLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepIntegration — the orchestrator

RepIntegration is the service that makes Priority Replication happen: its background loop starts export, import, resend, notification and transfer work, and it calls every other MS-REP service in the right order. For iRep it handles only the transfer step. It also hosts diagnostics used by the dashboard (service status, config evaluation, log summary, read-only script execution). If RepIntegration is stopped or its loop is disabled, nothing new replicates even though all other services answer.

## Role in replication

RepIntegration is the conductor; the other services are instruments it calls over HTTP. Keywords: orchestrator, integration, export, import, resend, queue, iRep transfer, worker.

- Priority Replication: drives the full send chain (ProData → PacketCreation → Compression → Split → Transfer) and receive chain (Acquisition → FileMerge → Decompress → SaveData/Ackn). See FLW-PR-EXPORT and FLW-PR-IMPORT.
- iRep: only transfer — routes such as `IntegrateTrackRecord`, `IntegrateTrackFile`, `IntegrateTrackExport`, `TransferPacketFolder`; iRep data preparation, ingestion and packet creation happen elsewhere (confirmed by platform team, 2026-11-11).
- Health and diagnostics for all services: `CheckAllServiceStatus` calls `TestService` on every service; `CheckOperationByFile` checks Windows services and Service Bus/Azure access (RepSbus `ReceiverStatus`, `SbusVerifyAccess`; RepAzure `AzureVerifyAccess`).

## How it runs — the main loop

Every `SchedulerIntervalInMinutes × SchedulerMultiplier` milliseconds, if `EnableWorkerService` and `InitiateOnInterval` are on, the loop runs eight steps in order (`RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L42-L111`). Keywords: worker loop, InitiateOnInterval, EnableWorkerService, scheduler, main processes not started.

| # | Step | What it does | Line |
|---|---|---|---|
| 1 | `InitiateExport` | Legacy export chain (ProData → … → Transfer) | L71 |
| 2 | `InvokePriorityResend` | Resend priority packets that were not acknowledged in time | L75 |
| 3 | `InvokeGeneralNotification` | Send queued general notifications through RepSbus | L79 |
| 4 | `InitiateAcquisitionProcess` | Pick up incoming files, then start the import queue | L81 |
| 5 | `VerifyGenExportValidity` | Vessel side: make sure general export is enabled for the vessel | L83 |
| 6 | `InitiateExportQueue` | Queue-based export: build packets from track change records | L85 |
| 7 | `InitiatePrTransferQueue` | Queue-based transfer of ready packets per vessel | L87 |
| 8 | `GeneralPacketResend` | Queue-based resend | L89 |

- If `InitiateOnInterval` is false: `Integration main processes not started due to InitiateOnInterval is false` (L93).
- If any step throws: `Work service failed` and **all in-memory process flags are cleared** (`ProcessDictionary.ClearProcessStatus()`, L105-L106).

## "Already running" guards

Queue steps run in the background and are protected by in-memory flags that expire. Keywords: already running, process time exceeded, stuck, AwaitingResponse, lock.

- `InitiateExportQueue` returns `Export Process is already running. Last updated Time: ...` while a run is active; a flag older than **2 hours** is removed automatically (`BL/QueueHandler/IntegrationQueueProcessBL.cs#L75-L160`). Transfer and resend queues use the same pattern (L165-L343).
- `InvokeNewExport` = false → `Export process is disabled by configuration` (L82-L90). `InvokeNewImport` = false → `Import process is disabled by configuration` (L586-L600).
- Restarting the service clears all flags (they are in memory only).

## Queue-based export and transfer

`TrackExportQueueBuilder` turns pending track-change records into packets; `PacketTransferHandler` sends ready packets per vessel. Keywords: track change records, channel flow, PR enabled vessels, packets ready for transfer, validation failed, recover file.

Export (`BL/QueueHandler/ExportQueueProcess.cs#L47-L512`):
1. Needs the General Packet channel (`General Packet channel information not found. Exiting.`, L58), a working directory (L65), channel flow settings (L75), PR-enabled vessels (L85) and vessels with General Export enabled (L93).
2. Reads pending track records; groups by `TableSettingsId`; generates packets, compresses (`Compression failed for TableSettingsId ...`, L245), copies files to per-vessel folders (L301-L338).
3. Ends with `Completed processing for TableSettingsId: {TableSettingsId}and packets are ready for Transfer` (L391). Failures mark the track records failed (L483-L511).

Transfer (`ExportQueueProcess.cs#L515-L963`):
1. For each active PR vessel, reads pending packets; skips vessels with none (L608).
2. Validates each packet file; if missing at the original path it tries to recover it from the *sent* path (`File not found at original location ... Attempting recovery.`, L856; `ReplaceOutPathWithSentPath`, L940). Invalid packets are set to error status (L620-L634).
3. Calls RepTransfer; `Transfer failed for vessel {VesselObjectId} with message: {ErrorMessage}` (L672). Saves transfer queue data and updates packet status (L746-L752).

## Queue-based import

`InitiateAcquisitionProcess` runs acquisition, then starts the import queue; `ImportProcessor` takes each queue item through merge, decompress and acknowledgement. Keywords: import queue, acquisition, file merge, decompress, ackn, AllZipDirectory, general notification.

- Acquisition → `InitiateImportQueue` (`BL/QueueHandler/IntegrationQueueProcessBL.cs#L586-L610`). RepAcquisition can also start the import queue itself (`RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L161`, `#L218`).
- `ImportProcessor` (`BL/QueueHandler/ImportQueueProcess.cs#L40`) needs current client details (L159) and the General Notification channel (L166). Items with invalid channel/flow/files are skipped with warnings (L296-L420).
- Files must exist in `AllZipDirectory` or their recorded location (L444-L508).
- Steps: FileMerge (`File Merge Service failed for Import Item {Id}`, L746) → Decompress (`Process failed while handling Decompress service`, L868) → save results / in-packet header / missing-packet info (L925-L979) → Ackn (`Process failed while handling ackn service`, L1107) → general notification via RepSbus (queue name resolved at L1523; `Queue name is null or empty`, L1279).

## API routes (main)

Controllers: `Integration` and `IntegrationQueue` (full list with lines in `inventory/ms-rep.md` → RepIntegration). Keywords: Initiate-Export-Queue, Initiate-Import-Queue, CheckAllServiceStatus, EvaluateConfiguration, ExecuteScript-And-GetResult.

| Area | Routes |
|---|---|
| Run a step now | `Initiate-Export-Queue`, `Initiate-PR-Transfer-Queue`, `General-Packet-Resend`, `Initiate-Import-Queue`, `Initiate-Acquisition-Process`, `Verify-Gen-Export-Validity`, `General-Notification`, `Initiallise-Basic-Data` |
| iRep transfer | `IntegrateTrackRecord`, `IntegrateTrackFile`, `IntegrateTrackExport`, `TransferPacketFolder`, `IntegrateResendV2V`, `IntegrateDownloadV2vPacket` |
| Priority | `GetPriorityAciveVessel`, `GetPriorityPacketStatus`, `Priority-All-Resend`, `TransferResendPacket`, `SendPendingTransferData`, `ReadTransferQueueData` |
| Diagnostics | `CheckAllServiceStatus`, `StartSbuSReciever`, `ReadApiCallLog`, `EvaluateConfiguration`, `Get-Summary` (log summary), `ExecuteScript-And-GetResult`, `BulkTransferStatus` |

`ExecuteScript-And-GetResult` runs SQL/PowerShell under `ScriptExecutionOptions` limits — any use from the dashboard must stay behind per-invocation approval.

## Configuration

All keys from `appsettings.json` unless marked CO_Parameters. Values are defaults in the repo, shown only for tuning keys. Keywords: BasicSettings, InvokeNewExport, InvokeNewImport, RetryLimit, ResendTimeInH, ConfigEvaluationOptions.

| Key | Effect |
|---|---|
| `WorkerServiceSettings:EnableWorkerService`, `InitiateOnInterval`, `SchedulerIntervalInMinutes` (1), `SchedulerMultiplier` (60000), `CommonInitScheduleInMinutes` (5) | Loop on/off and timing. |
| `BasicSettings:InvokeNewExport`, `InvokeNewImport` | Turn queue-based export/import on or off. |
| `BasicSettings:InvokeExportAfterSave`, `InvokeTransferAfterSave` | Chain export/transfer after save. Exact trigger point: Not determined from code. |
| `BasicSettings:ParallelLimit` (1), `QueueReadLimit` (10), `RetryLimit` (20), `ExportQRetryInMin` (30), `CheckIntervalInMin` (5) | Throughput and retry. |
| `BasicSettings:ResendTimeInH` (1), `ResendExceedTimeInH` (2) | When unacknowledged packets are resent. |
| `BasicSettings:EnableGeneralNotification`, `GenralNotificationRetryCount` (15) | General notifications. |
| `RequestSettings:MaximumFilePerRequest` (15) | Files per transfer request. |
| `ConfigEvaluationOptions:*` (`DiskFailBelowGB`, `DiskWarnBelowGB`, `NtpServer`, `MaxClockDriftSeconds`, `ServiceBusPort`, `LongRunningQueryWarnMinutes`, `LongRunningQueryFailHours`, `ScheduledTaskMaxRunHours`) | Thresholds used by `EvaluateConfiguration` health rules. |
| CO_Parameters: `PR_REP_ROOT`, `PR_REP_SPLIT_SIZE`, `REP_CHUNK_SIZE`, `REP_PARALLEL_PROCESS_COUNT`, `REP_PR_AZURE_IN`, `REP_CODE`, `REP_PR_KEY_MASTER_ID`, `REP_SOURCE_UNIQUE_ID`, `REP_SOURCE_UNIQUE_OBJECT_TYPE`, `PR_PACKET_COUNTER` | Paths, sizes, identity and counters. |

## Logs and what to look for

Log: `Logs/IntegrationServiceLog_.txt`; every queue run has its own `CorrelationId`. Keywords: IntegrationServiceLog, work service failed, already running, transfer failed, no PR enabled vessels.

| Message (template) | Meaning |
|---|---|
| `Integration main processes not started due to InitiateOnInterval is false` | Loop disabled by config. |
| `{MethodName} | Work service failed` | A step threw; all flags were cleared. |
| `Export Process is already running. Last updated Time:` | Previous export still running (auto-cleared after 2 h). |
| `Export process is disabled by configuration` / `Import process is disabled by configuration` | `InvokeNewExport` / `InvokeNewImport` off. |
| `General Packet channel information not found. Exiting.` | Channel configuration missing in DB. |
| `No PR enabled vessels found. Exiting.` | No vessel has Priority Replication enabled. |
| `Transfer failed for vessel {VesselObjectId} with message: {ErrorMessage}` | RepTransfer returned an error. |
| `File not found at original location for Packet ID {PacketId}` | Packet file missing; recovery attempted. |
| `File Merge Service failed` / `Process failed while handling Decompress service` / `... ackn service` | Import step failed in that service. |

Sources: lines cited in the sections above. Full list: `inventory/ms-rep-logs.md` → RepIntegration.

## Related

- PLT-MSREP-OVERVIEW, FLW-PR-EXPORT, FLW-PR-IMPORT, CMP-REPTRANSFER, CMP-REPDBLOGW
- ISS-INTEG-001, ISS-INTEG-002, ISS-INTEG-003
