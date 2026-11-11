---
doc_id: CMP-REPAZURERES
type: component
mechanism: [smartsync]
group: smartsync-transport
runs_on: [office, vessel]
components: [RepAzureRes]
log_files: [AzureResumeLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepAzureRes — SmartSync resumable blob upload

RepAzureRes uploads packet files to Azure Blob in chunks so an interrupted upload can resume, then calls back so the rest of the chain can notify the other side. It adapts chunk size to measured network speed. If uploads stop, the sending side shows packets as transferred to outbox but the receiver never sees them.

> **V2V (vessel-to-vessel) is a dropped feature.** The V2V routes, procedures and message types mentioned in this article still exist in the code and database but are not in use; do not troubleshoot them. See DATA-MSREP-OFFVSL.

## Role in replication

RepAzureRes is the upload half of SmartSync's file channel. Keywords: azure upload, resumable upload, chunk, block, resume, callback, V2V resend.

- RepIntegration calls `AzureResUpload/ResumeUpload` and `AzureResUpload/V2VAzureResendData` (see `inventory/ms-rep.md` → RepIntegration).
- After uploads, `InitiateAzureCallBack` calls the integration side; failures log `{ApiError} | Error while calling integration API` (`RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L115`).
- Database writes go through RepDBLogW (`SL/DbConfigSL.cs`); a missing RepDBLogW address logs `Error RepDblogW Service API details missing` (`SL/DbConfigSL.cs#L27`).

## How it runs

Every `WorkerServiceSettings:SchedulerIntervalInMinutes` the worker loads settings, then (if `InitiateUpload`) checks Azure settings, uploads pending files and runs the callback; it always tries to clear old chunk JSON files. Keywords: worker, upload pending, CheckAzureSettings, callback, chunk json.

Order: `SetAllInitData` → `CheckAzureSettings` → `UploadPendingData` → `InitiateAzureCallBack` → `TryClearOldJsonFiles` (`RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/WorkerService.cs#L63-L80`).

How resumable upload works (from `BL/UploadProcessBL.cs` and `BL/CommonOperationBL.cs`):

- For each file a JSON file records the block list; if it is missing or invalid it is regenerated (`Invalid block metadata for file {FileName}. Reason: {Reason}. Regenerating json.`, `BL/UploadProcessBL.cs#L484`).
- Chunk size is computed from a speed test; `Chunk size is zero, network speed is low cannot proceed with upload` (`#L158`) and `Speed test failed, assuming very slow connection` (`#L1215`) show bandwidth problems. `AzureSettings:MaxChunkSizeInKB` and `MinUploadSpeedInKBps` bound this.
- A heartbeat is updated while uploading (`Heartbeat update failed for {FileName}`, `#L661`); a checksum is stored (`CheckSumCalcType`).
- Safety resets: if the upload pending count has not changed for 6 hours, or the integration pending count for 3 hours, in-memory counters are reset (`BL/CommonOperationBL.cs#L477`, `#L484`).

## API routes

Routes are under `AzureResUpload` (`RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/Controllers/AzureResUploadController.cs`). Keywords: ResumeUpload, UploadPendingData, V2VAzureResendData, CheckAzureSettings.

| Route | Purpose | Line |
|---|---|---|
| `ResumeUpload` | Queue/resume upload of given files | L41 |
| `UploadPendingData` | Run upload now | L53 |
| `V2VAzureResendData` | Resend for vessel-to-vessel (dropped feature) | L61 |
| `CheckAzureSettings` | Verify storage settings | L68 |
| `InitiateAzureCallback` | Run callback now | L91 |
| `ReadingStaticCount`, `ChronoStaticCleansing` | Show / clear in-memory counters | L82, L99 |
| `TestService`, `Version` | Health | L33, L75 |

## Configuration

Keywords: upload settings, chunk size, upload speed, Kestrel URL, connection string.

| Key | Where | Effect |
|---|---|---|
| Azure connection string / account key **(secret)** | Loaded at runtime (via RepDBLogW) | Missing → `Azure Account Key is empty` (`BL/UploadProcessBL.cs#L127`), `AzurePrimaryConnectionString is null or empty` (`#L133`), `Azure Blob Connection string is null or empty` (`#L679`). |
| `PR_REP_ROOT` | CO_Parameters | Root folder for packet files. |
| `WorkerServiceSettings:SchedulerIntervalInMinutes`, `InitiateOnInterval`, `InitiateUpload` | appsettings | Timer and switches. |
| `AzureSettings:MaxChunkSizeInKB`, `MinUploadSpeedInKBps`, `ConnectionRetryLimit`, `ConnectionRetryDelayInSec`, `ConnectionMaxRetryDelayInSec`, `NetworkTimeoutInSec` | appsettings | Chunking and retry. |
| `BasicSettings:CheckInterval`, `CallIntegrationMethod`, `NoOfRecordsRead`, `CheckSumCalcType`, `ServiceId` | appsettings | Cadence, batch size, checksum type, service identity. |
| `LargeFileLaneSettings:*` | appsettings | Separate lane for large files. |
| `Kestrel:Endpoints:Http:Url` | appsettings | Listens on localhost only by default in repo appsettings (port 5058). |

## Logs and what to look for

Log: `Logs/AzureResumeLog_.txt`. Keywords: AzureResumeLog, upload failed, chunk size zero, json file, block metadata.

| Message (template) | Meaning | Source |
|---|---|---|
| `Azure settings verification failed, cannot proceed with upload` | Settings/credentials bad; nothing uploads. | `BL/UploadProcessBL.cs#L98` |
| `Chunk size is zero, network speed is low cannot proceed with upload` | Link too slow / speed test failed. | `#L158` |
| `File {FileName} does not exist in source location and Json file also does not exist` | Source file gone before upload. | `#L305` |
| `Upload is failed for file {FileName}` | Upload of a file failed. | `#L831` |
| `Invalid block metadata ... Regenerating json.` / `Regenerated block metadata is still invalid` | Resume state corrupt. | `#L484`, `#L508` |
| `Azure Upload Pending Count has not been updated in 6 hours, resetting` | Counter stuck; auto-reset. | `BL/CommonOperationBL.cs#L477` |
| `Error while calling integration API` | Callback to RepIntegration failed. | `BL/IntegrationCallBL.cs#L115` |

## Common failure points

Keywords: upload stuck, slow network, vessel bandwidth, resume failed.

- Slow or no network → chunk size zero → ISS-AZURERES-001.
- Credentials/container wrong → ISS-AZURE-002 (shared with RepAzure).
- Source file missing (moved/deleted by another step) → check RepTransfer and RepIntegration file validation (ExportQueueProcess recovery logic).

## Related

- PLT-MSREP-OVERVIEW, CMP-REPAZURE, CMP-REPSBUS, CMP-REPTRANSFER, FLW-PR-EXPORT
- ISS-AZURERES-001, ISS-AZURE-002
