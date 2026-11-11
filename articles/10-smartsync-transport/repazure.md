---
doc_id: CMP-REPAZURE
type: component
mechanism: [smartsync]
group: smartsync-transport
runs_on: [office, vessel]
components: [RepAzure]
log_files: [AzureService_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepAzure — SmartSync blob download and file housekeeping

RepAzure downloads packet files from Azure Blob storage, moves downloaded files to where the receiving side expects them, deletes processed blobs, and moves finished records to history. It runs on its own timer and also answers on-demand download requests. If it stops, uploads from the other end pile up in the container and nothing arrives locally.

## Role in replication

RepAzure is the download half of SmartSync's file channel; RepAzureRes is the upload half and RepSbus carries the notices. Keywords: azure download, blob, container, download queue, move pending files, delete, history.

- RepIntegration calls `Azure/AzureDownloadByReference` for on-demand downloads and `Azure/AzureVerifyAccess` for health checks (see `inventory/ms-rep.md` → RepIntegration).
- RepAzure calls RepSbus `SbusSend/SendAcknowledgement` to acknowledge downloads (`inventory/ms-rep.md` → RepAzure).
- `ReadIRepFolderFile` (`RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L434`) is called after the move step (L239-L320), so RepAzure also serves iRep file pickup. What exactly it reads for iRep: Not determined from code.

## How it runs

Every `WorkerServiceSettings:SchedulerIntervalInMinutes` the worker runs four steps in order, each guarded by an in-memory "already running" flag. Keywords: worker, scheduler, download process already running, process time exceeded, lane.

1. Load settings (`SetAllInitData`) — `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L54-L65`.
2. If `InitiateDownload` is true: `IntiateDownloadQueue` (L67). It stops early if Azure settings are not loaded or the network check fails (`BL/AzureOperationBL.cs#L99-L140`). Downloads run in two lanes: **Normal** and, when `LargeFileLaneSettings:Enabled`, **Large** (files above `ThresholdInMB`).
3. `MovePendingFiles` (L70), then `InitiateDeleteWorker` (L73), then `MoveToHistoryProcess` (L76).

Each step sets a flag in a process dictionary before starting and clears it in `finally`. If a run is still going, the next cycle logs `Download process is already running. Exiting.` and skips. If the flag is older than the allowed time, it logs `Download process time exceeded. Removing status.` and starts again (`BL/AzureOperationBL.cs`, `StartDownloadLane`). The same pattern applies to move, delete and history.

## API routes

Routes are under `Azure` (`RepAzure/MariApps.PAL.Rep.Azure.Service/Controllers/AzureController.cs`). Keywords: AzureDownloadByReference, IntiateDownloadQueue, AzureVerifyAccess, ReadBlobDownloadStaticData.

| Route | Purpose | Line |
|---|---|---|
| `AzureDownloadByReference` | Download a specific file by reference (called by RepIntegration) | L35 |
| `IntiateDownloadQueue` | Run the download step now | L56 |
| `MovePendingFiles` | Run the move step now | L63 |
| `InitiateDeleteWorker` | Run the delete step now | L70 |
| `ReadIRepFolderFile` | iRep folder pickup | L78 |
| `MoveToHistoryProcess` | Run the history step now | L85 |
| `ReadBlobDownloadStaticData`, `ReadingStaticProcess` | Show in-memory queue/flags (diagnostics) | L92, L122 |
| `AzureVerifyAccess` | Test storage access | L107 |
| `ChronoStaticCleansing` | Clear in-memory state | L129 |
| `TestService`, `Version` | Health | L99, L115 |

## Configuration

Storage identity comes from CO_Parameters; tuning from `appsettings.json`. Keywords: storage account, container, client code, AzureSettings, retry, timeout.

| Key | Where | Effect |
|---|---|---|
| `REP_AZURE_STORAGE_ACCOUNT_NAME` / `REP_AZURE_STORAGE_ACCOUNT_KEY` **(secret)** | Name in CO_Parameters; key in `REP.REP_SERVICEBUS_CREDENTIALS` (read by `REP.REP_GET_AZURE_SETTINGS`) | Storage account access. |
| `REP_STORAGE_CONTAINER_NAME` | CO_Parameters | Container used. |
| `REP_CLIENT_CODE`, `REP_CLIENT_ENVIROMENT_UNICID`, `REP_LOCATION` | CO_Parameters | Identify client, environment and side; used to build paths/filters. Exact path format: Not determined from code. |
| `WorkerServiceSettings:SchedulerIntervalInMinutes`, `InitiateOnInterval`, `InitiateDownload` | appsettings | Timer and on/off switches. |
| `AzureSettings:ConnectionRetryLimit`, `ConnectionRetryDelayInSec`, `ConnectionMaxRetryDelayInSec`, `NetworkTimeoutInSec`, `AzureConnectionTimeoutInMin`, `BlobDeletionFlag` | appsettings | Retry/timeout behaviour; whether blobs are deleted after processing. |
| `BasicSettings:DeleteIntervalInHours`, `AzureReadDateRangeInDays`, `NoOfRecordsRead`, `CallIntegrationApi`, `ResetStaticVariableInHour` | appsettings | Housekeeping cadence, read window and batch size. |
| `LargeFileLaneSettings:Enabled`, `ThresholdInMB`, `ParallelCount` | appsettings | Separate lane for large files. |
| `BasicSettings:EncryptionKey` **(secret)** | appsettings | Never copy. |

Stored procedures used include `[REP].[REP_GET_AZURE_SETTINGS]`, `[REP].[PR_PENDING_UPLOAD_FILE]`, `[REP].[REP_INSERT_UPLOAD_FILE]`, `[REP].[READ_VESSEL_LIST]` (full list: `inventory/ms-rep.md` → RepAzure).

## Logs and what to look for

Log: `Logs/AzureService_.txt`. Keywords: AzureService log, download failed, exception in background download, already running.

| Message (template) | Meaning | Source |
|---|---|---|
| `Azure init settings message = {AzureInitMessage}` | Settings did not load; download skipped. | `BL/AzureOperationBL.cs` (IntiateDownloadQueue) |
| `Network Status = {NetworkMessage}` | Network check failed; download skipped. | same |
| `Download process is already running. Exiting.` (repeating for hours) | A previous run is stuck; waits for the exceed time. | same, `StartDownloadLane` |
| `Download process time exceeded. Removing status.` | Stuck flag was cleared automatically. | same |
| `Exception in background download process in {MethodName}` | Download run crashed. | `BL/AzureOperationBL.cs#L224` |
| `Exception in background move process in {MethodName}` / `delete` / `move-to-history` | Housekeeping crashed. | `#L284`, `#L399`, `#L527` |
| `{MethodName}| Error RepIntegration Service API details missing` | Cannot call back RepIntegration. | `SL/IntegrationSL.cs#L34` |
| `ServiceConfigData is null or empty` | `microservices.json`/service config not loaded at startup. | `AzureServiceDependency.cs#L63` |

## Common failure points

Keywords: azure download stuck, files not arriving, JsonReaderException, restart RepAzure.

- Download lane stuck "already running" → ISS-AZURE-001.
- Storage credentials/container wrong or network blocked → ISS-AZURE-002.
- Known incident (2026): `JsonReaderException` with an unexpected `<` during `IntiateDownloadQueue`; resolved by restarting the service. Root cause: Not determined from code (an HTML response where JSON was expected suggests a proxy or error page — to be confirmed). Recorded in ISS-AZURE-001 as a variant.

## Related

- PLT-MSREP-OVERVIEW, CMP-REPAZURERES, CMP-REPSBUS, CMP-REPTRANSFER, FLW-PR-IMPORT
- ISS-AZURE-001, ISS-AZURE-002
