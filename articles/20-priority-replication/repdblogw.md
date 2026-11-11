---
doc_id: CMP-REPDBLOGW
type: component
mechanism: [priority-replication, smartsync, irep]
group: pr-core
runs_on: [office, vessel]
components: [RepDBLogW]
log_files: [DbLogServiceLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepDBLogW — database gateway for replication

RepDBLogW is an HTTP front door to the replication database. Priority Replication services write logs and packet state through it, and the SmartSync transport services (RepSbus, RepAzure, RepAzureRes) load their settings, credentials, queue names and download/upload queues through it. It has no timer. If RepDBLogW is down or cannot reach SQL Server, the transport cannot even load its configuration, so the failure shows up first in *other* services' logs.

## Role in replication

RepDBLogW is part of the Priority Replication core and, in the code, also the settings source for SmartSync. Keywords: DBlogW, database gateway, log write, packet log, settings, credentials, Rep2i, Rep2x.

- Priority Replication: packet logs and state (`DbPckLog/*`, `DBlogWrite/*`), import queue saves (`AzureDblog/Packet-ImportQ-Save`).
- SmartSync: 55 routes under `DbServiceSbus` serve RepSbus (`SbusWin*`), RepAzure (`Azure*`, `ReadAzureFileDownloadQ`, `MovInsertAzureDownHistory`) and RepAzureRes (`SaveAzureResUploadData`, `PendingAzurResData`, `Move-Azure-Res-History`, …) — `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs`.
- iRep: has DB contexts for the iRep databases (`Rep2IDbRepository`, `Rep2XDbRepository` in `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/`) and routes such as `SaveIRepValidateFile`. iRep may call RepDBLogW to read data (platform team).

> Review note: the platform team describes RepDBLogW as Priority Replication core. The code also shows it is the configuration source for all three SmartSync services. Recorded in `reviews/open-questions.md` (Q3).

## API routes by area

Four controllers, 82 routes (full list with lines: `inventory/ms-rep.md` → RepDBLogW). Keywords: LogWrite, UpdateOutPacketHd, ReadCompressionType, SbusWinReadConfiguration, GetFilesToDownload.

| Controller | Used by | Examples |
|---|---|---|
| `DBlogWrite` | all PR services | `LogWrite`, `LogWriteV2V`, `LogWriteService`, `LogWriteServiceBulk`, `LogWriteApiCallData`, `ReadApiCallLog` |
| `DbPckLog` | RepIntegration, RepTransfer, RepPacketCreation | `UpdateOutPacketSource`, `GetExportParams`, `SaveExtPacketDetails`, `ReadCompressionType`, `ReadPriorityPacketStatus`, `ReadAcknStatusList`, `UpdateOutPacketHd`, `SaveMissingPackets`, `ReadMissingPacketById` |
| `AzureDblog` | RepIntegration, RepAzure/RepAzureRes | `CheckAzureResDataExists/{status}`, `CheckAzureDownloadDataExists/{status}`, `Packet-ImportQ-Save`, `Downloads-Save-Bulk`, `UpdateExportType/{vesselObjectId}/{exportType}` |
| `DbServiceSbus` | RepSbus, RepAzure, RepAzureRes | `SbusWinReadConfiguration`, `SbusWinGetSbusSettings`, `SbusWinReadCoParam`, `SbusWinGetFilesToDownload`, `SbusWinUpdateDownload`, `GetCredentialsSettingsV2V`, `GetQueueNameV2V`, `AzureGetAzureSettings`, `AzureGetTransferType`, `SaveAzureResUploadData`, `ReadManualOpPath` |

## Database objects

Stored procedures are in the `REP` schema. Keywords: stored procedure, REP schema, PR_REP_SAVE_LOG_DB, REP_GET_SBUS_SETTINGS, REP_GETFILESTODOWNLOAD.

Most-used groups (complete list: `inventory/ms-rep.md` → RepDBLogW):

- Logging: `[REP].[PR_REP_SAVE_LOG_DB]`, `[REP].[PR_REP_SAVE_LOG_DB_BULK]`, `[REP].[PR_REP_LOG_SAVE]`, `[REP].[REP_READ_PR_REP_LOG]`, `[Rep].[SAVE_SERVICE_STATUS]`.
- Service Bus: `[REP].[REP_GET_SBUS_SETTINGS]`, `[REP].[REP_GET_QUEUE_NAME]`, `[REP].[REP_PR_READ_QUEUE_NAME]`, `[REP].[REP_GET_AZURE_SBUS_CREDENTIALS_V2V]`, `[Rep].[REP_SBUS_NOTIFICATION_INSERT]`, `[REP].[REP_SAVE_NOTIFICATION_ERROR_LOG]`.
- Azure download/upload: `[REP].[REP_GETFILESTODOWNLOAD]`, `[REP].[REP_UpdateDownloads]`, `[REP].[REP_INSERT_DOWNLOADS_BULK]`, `[REP].[PR_REP_READ_AZURE_FILE_Q]`, `[REP].[REP_UPDATE_AZURE_DOWNLOAD_Q]`, `[REP].[REP_INSERT_AZURE_RES_UPLOAD]`, `[REP].[REP_READ_AZURE_RES_UPLOAD]`, `[REP].[REP_UPDATE_AZURE_RES_UPLOAD]`, `[REP].[REP_GET_AZURE_SETTINGS]`.
- Packets: `[REP].[GET_PR_COMRESSION_TYPE]`, `[REP].[GET_PRIORITY_FILE_STATUS]`, `[REP].[GET_PRIORITY_FILE_ACKN]`, `[REP].[SAVE_EXT_PACKET_DETAILS]`, `[REP].[UPDATE_EXT_PACKET_DATA]`, `[REP].[REP_MISSING_PACKET_BULK_SAVE]`, `[REP].[SAVE_PR_REP_IMPORT_QUEUE]`.
- V2V: `[REP].[GET_V2V_MASTER_LOG_DATA]`, `[REP].[GET_V2V_RESEND_PACKET]`, `[REP].[V2V_RESEND_LOG_OPERATIONS]`, `[REP].[REP_SAVE_MASTER_LOG]`.

## Configuration

Keywords: connection string, CO_Parameters, REP_RETRY_COUNT, REP_IN_INBOX, REP_MANUAL_OP_PATH.

| Key | Where | Effect |
|---|---|---|
| Database connection strings **(secret)** | appsettings `ConnectionStrings` | Main replication DB and iRep DBs. |
| `REP_SERVICEBUS_CONNECTION_STRING`, `REP_AZURE_STORAGE_ACCOUNT_KEY` **(secret)** | `REP.REP_SERVICEBUS_CREDENTIALS` (CO_Parameters rows may be empty) | Read here and handed to the transport services. |
| `REP_AZURE_STORAGE_ACCOUNT_NAME`, `REP_STORAGE_CONTAINER_NAME`, `REP_CLIENT_CODE`, `REP_CLIENT_ENVIROMENT_UNICID`, `REP_LOCATION` | CO_Parameters | Transport identity. |
| `REP_CHUNK_SIZE`, `REP_PARALLEL_PROCESS_COUNT`, `REP_RETRY_COUNT` | CO_Parameters | Transfer tuning. |
| `REP_IN_INBOX`, `REP_MANUAL_OP_PATH` | CO_Parameters | Inbox and manual-operation folders. |
| `REP_INTERGRATION_BASE_URL`, `REP_INTERGRATION_API_URL` | CO_Parameters | Where RepIntegration is reached. |

## Logs and what to look for

Log: `Logs/DbLogServiceLog_.txt` (51 logger templates — `inventory/ms-rep-logs.md` → RepDBLogW). Keywords: DbLogServiceLog, SQL timeout, connection failed, settings not found.

Because callers depend on it, check RepDBLogW whenever another service logs that settings, credentials or queue names are missing, for example RepSbus `service bus connection string and basic info is not found` or RepAzureRes `Error RepDblogW Service API details missing`. First checks: `DBlogWrite/TestService` answers; the SQL Server is reachable from the service account; then the specific procedure behind the failing route.

## Related

- PLT-MSREP-OVERVIEW, CMP-REPSBUS, CMP-REPAZURE, CMP-REPAZURERES, CMP-REPINTEGRATION
