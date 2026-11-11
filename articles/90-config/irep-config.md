---
doc_id: CFG-IREP
type: config
mechanism: [irep]
group: irep-config
runs_on: [office, vessel]
components: [ComINT, ExportCDT, ExportDCS, ImportDES, ImportDSC, ImportRBP, ComPBR]
log_files: []
error_types: [config]
applies_to_versions: ["Not determined from code"]
sources: ["iRep snapshot staged 2026-11-11 (appsettings.json, services.json, deployment scripts)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# sync+ configuration index (key names only)

This index lists every configuration source that sync+ reads. It covers the appsettings sections, the services.json endpoints, the parameters in the REP databases and the replica types. Values are never recorded here: they are environment-specific and some are secret. To check a site, use the EvaluateConfig routes or the presence scripts. They report PRESENT, EMPTY or MISSING and never show a value.

## appsettings.json sections

Every service has the same Serilog block (minimum level Error) plus the sections below. Placeholders such as `$__DCS_PORT__$` are filled in at deployment. Keywords: appsettings, BasicSettings, WorkerServiceSettings, DatabaseSettings, DataConduitSettings, CheckIntervalInMin.

### ComINT

- `ConnectionStringSettings[]`: `ReplicaTypeId`, `ReplicaName`, `PrimaryDB`, `ReadOnlyDB`, `IsEnabled`.
- `ConnectionStrings`, `BasicSettings`, `WorkerServiceSettings`.

### ExportCDT

- `ConnectionStrings`: `PrimaryDB`, `ReadOnlyDB`, `AzureDB`.
- `BasicSettings`: `IsOffice`, `ReplicaTypeId`, `LogErrorToDB`.
- `DatabaseSettings`:
  - linked server key and value;
  - command timeouts;
  - `MaxConcurrentTask`, `BatchSize`, `BulkCopyTimeout`;
  - **`DcsCallEnabled`**, `CdtCallEnabled`.
- `WorkerServiceSettings`: `EnableWorkerService`, `SchedulerIntervalInMinutes`, `InitiateOnInterval`, `CheckIntervalInMin`, `ClearCacheEnabled`, `ClearCacheIntervalInMin`.
- `AlertMailConfiguration`: To, CC, BCC.
- `DataConduitSettings`.

### ExportDCS

- `ConnectionStrings`: `AzureDBConnection`, `PALConnection`.
- `BasicSettings`: `IsOffice`, `InvokeNextService`, `CommandTimeOut`.
- `WorkerServiceSettings`:
  - `InitiateOnInterval`;
  - **`CheckIntervalInMin`** — 0 makes the loop spin;
  - `ResetStaticVariableInHour`;
  - `AutoResentIntiateOnInterval`, `AutoResentCheckIntervalInMin`;
  - `DirectoryAutoResentOnInterval`, `DirectoryAutoResentIntervalInH`.
- `ExportSettings`: `RecordLimit`, `BatchSize`, `AttachmentBatchSize`, `ChunkSizeInMb`, `ParallelCountLimit`.
- `DataConduitSettings`: `ConduitType`, `KeyBaseName`, `IsSliding`, `ExpireTime`.

### ImportDES

- `ConnectionStrings`: `PALConnection`, `Rep2xConnection`, `ImportDbConnection`.
- `BasicSettings`: `IsOffice`, **`InvokeNextService`** (see the services.json note), **`InvokeRbpService`**, `CommandTimeOut`.
- `WorkerServiceSettings`: `InitiateOnInterval`, `CheckIntervalInMin`, `ResetStaticVariableInHour`, validate and read on-interval flags and intervals.
- `ImportSettings`: `RecordLimit`, `AttachmentBatchSize`, `ParallelCountLimit`, `PacketReaderParallelLimit`, `InsRecordBatchCount`.
- `DataConduitSettings`.

### ImportDSC

- `ConnectionStrings`: `PrimaryDB`, `ReadOnlyDB`, `AzureDB`, `Rep2i`.
- `BasicSettings`, `DatabaseSettings` (timeouts), `DataConduitSettings`.
- `ApplicationInsights:ConnectionString` (secret).

### ImportRBP

- `ConnectionStrings`: `PrimaryDB`, `ReadOnlyDB`, `AzureDB`, `Rep2i`.
- `BasicSettings`, including `ResetStaticVariableInHour`, `MaxConcurrentTask`, `LogErrorToDB`.
- `DatabaseSettings`, including **`RbpCallEnabled`**.
- `WorkerServiceSettings`, including `ReprocessEnabled` and `RepreocessIntervalInHours` (key name misspelled in code; default 12).
- `DataConduitSettings`.
- `ApplicationInsights:ConnectionString` (secret).

### ComPBR

- `ConnectionStrings`: `AzureDB`, `Rep2i`.
- `BasicSettings`:
  - `SchedulerIntervalInMinutes`, timeouts;
  - `MaxConcurrentTask`, `PacketReaderParallelLimit`;
  - `TypeId`, `MaximumDatabaseSpaceGB`;
  - `IsMsgDataLog`, `IsCompressEnabled`, `LogErrorToDB`.
- `DataConduitSettings`.
- `ApplicationInsights:ConnectionString` (secret).

`DataConduitSettings:ConduitType` selects the cache: in-memory or Redis. With Redis, the cache server must be reachable; otherwise the CACHE cards apply. Flags in `IsOffice` and the replica type must match the site. A vessel server configured as office runs the office queries and paths.

## services.json endpoints

Each service calls the others through endpoints in its services.json. The table lists service and endpoint names only; base addresses are placeholders or hosts. Keywords: services.json, endpoint, next service, TransferGeneral, ValidatePacket.

| Caller | Name | Endpoint | Note |
|---|---|---|---|
| ExportCDT | RepExportDCS_Utility | `ExportDcs/InitateExportProcess` | Used when `DcsCallEnabled` is on |
| ExportCDT, ImportDSC, ImportRBP | ComINT_Utility | `ComINT/GetDbConfigurationDetails` | |
| ExportDCS, ImportDES | CommonIntegration | `ComINT/GetDbConfigurationDetails` | |
| ExportDCS | RepTransferService | `Integration/TransferGeneral` | Goes to **RepIntegration** (`$__PR_BASE_URL__$`) |
| ExportDCS | RepNextService | `ExportDcs/InitateExportProcess` | Self-call after each export |
| ImportDES | RepImportDsc | `RepImportDSC/RepImportSchemaCompare` | |
| ImportDES | RepRbpService | `RepImportRBP/RepImportSync` | Used when `InvokeRbpService` is on |
| ImportDES | RepNextService | `ImportDes/ValidatePacket` | **Route does not exist** in the DES controller (open question) |
| ComPBR | RepExportDCSU_tility | `RepDcs/Value` | Name looks mistyped; no such route in ExportDCS |

## Database parameters

The parameter names below are seeded by the deployment scripts (INV-IREP-DB § CO_Parameters). The services read them through cached default-config lists. Keywords: REP_RESENT_LIMIT, REP_RESENT_AWAIT_TIME_IN_MIN, REP_PROCESS_AWAIT_TIME, REP_NEW_ERROR_PATH, REP_CLIENT_ENVIRONMENT_UNICID.

| Name | Used for |
|---|---|
| `REP_RESENT_LIMIT` | Maximum automatic resend attempts per packet (`ExportDCS/Mariapps.PAL.RepExportDCS.Model/CacheKeys/ExpConfigKeys.cs#L27`) |
| `REP_RESENT_AWAIT_TIME_IN_MIN` | Wait before a packet is resent (L29) |
| `REP_NEW_ERROR_PATH` | Folder where the directory resend moves badly named packets (L30) |
| `REP_PROCESS_AWAIT_TIME` | Pause after a vessel export error (`ExportDCS/Mariapps.PAL.RepExportDCS/BL/Validation/ConfigEvaluationBL.cs#L42`) |
| `REP_PROCESS_RETRY` | Retry count. Not determined from code: which step uses it |
| `REP_CLIENT_CODE`, `REP_CLIENT_ENVIRONMENT_UNICID`, `REP_SOURCE_UNIQUE_ID`, `REP_SOURCE_UNIQUE_OBJECT_TYPE` | Environment identity used in packet names; empty values trigger ISS-IREP-DCS-004 |
| `REP_OUT_OUTBOX`, `REP_MANUAL_OP_PATH` | Outbox and manual-operation folders |
| `REP_EAS_*` | EAS alert mail settings (spam mails) |
| `REP_CDT_STAGING_QUEUE`, `REP_VSL_PENDING_RECORDS` | PAL-side CDT staging and pending counts |
| `IS_VESSEL` | Site type flag |

## Probes for the dashboard

These routes are read-only and safe to call on a schedule. Keywords: EvaluateConfig, health probe, ReadAllCacheKeyValues, Version.

- `EvaluateConfig` on ExportCDT, ExportDCS, ImportDES, ImportDSC, ImportRBP and ComPBR. It checks settings, database objects, paths and identity.
- `ImportDes/ReadAllCacheKeyValues`: skip lists, processing vessels and counter mismatch lists.
- `Version` / `GetVersion` on each service: shows which build is deployed. Compare with the database scripts (ISS-IREP-CDT-003).

Do not call these on a schedule: `ComINT/GetDbConfigurationDetails` returns connection strings, and the trigger routes (InitateExportProcess, RepImportSync and similar) start work.

## Related

PLT-IREP, DATA-IREP, INV-IREP, INV-IREP-DB
