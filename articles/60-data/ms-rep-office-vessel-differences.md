---
doc_id: DATA-MSREP-OFFVSL
type: reference
mechanism: [priority-replication, smartsync]
group: data
runs_on: [office, vessel]
components: [RepIntegration, RepTransfer]
sources: ["MS-REP database scripts snapshot staged 2026-11-11 (no git commit available): RepIntegration and RepTransfer PAL.DatabaseScripts.Office / PAL.DatabaseScripts.Vessel, every file compared"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# MS-REP Office vs Vessel database scripts — every difference

The Office and Vessel script projects build mostly the same database, but not quite. This article lists **every** difference found by comparing each Office file with its Vessel counterpart, however small, and says which ones matter when troubleshooting. Keywords: office vs vessel, schema difference, vessel database, default constraint, sequence, NEXT VALUE FOR, change tracking, replication_id, IS_PRODUCT, PR_REP_ROOT, REP_OFF_ROOT.

> **V2V (vessel-to-vessel) is a dropped feature.** V2V objects still exist in both script sets (tables, types, procedures, the `TRANSFER_CHANNEL_FILE_V2V` channel, the `REP_INT_V2V_*` parameters). Their differences are listed below for completeness only; do not troubleshoot V2V.

## How the comparison was done

Files were paired by folder and by name with the number prefix removed (case and spaces ignored), so renumbered files are still compared. Keywords: diff method, renumbered, paired files.

| Project | Identical | Whitespace/line-ending only | Different | Office only | Vessel only |
|---|---|---|---|---|---|
| RepIntegration | 221 | 2 | 44 | 1 | 2 |
| RepTransfer | 27 + 4 shared utility files | 1 | 8 | 20 | 1 |

Whitespace-only pairs (no effect): `RepIntegration/PAL.DatabaseScripts.Office/Scripts/007_TABLE_PR_REP_IN_Packet_HD.sql`, `RepIntegration/PAL.DatabaseScripts.Office/Scripts/076_TYPE_[Rep].[REP_V2V_UNIQUE_OBJECT_ID].sql` (V2V, dropped), and `RepTransfer/PAL.DatabaseScripts.Office/StoredProcedures/011_SP_[REP].[REP_GETFILESTODOWNLOAD].sql` (also named `rep_GetFilesToDownload` in lower case on the vessel side — SQL Server object names are not case sensitive by default, so this does not matter).

## The differences that matter most

These change behaviour and are the ones to check first on a vessel. Keywords: cannot insert NULL into column ID, sequence default missing, transfer type, delivery folder, PAL database name.

1. **IDs: Office uses column defaults, Vessel passes the ID explicitly.** Office table scripts bind each sequence as a default constraint (`NV_..._SEQ`) so inserts can leave `ID` out. The Vessel table scripts do not create those defaults, and the Vessel procedures write `NEXT VALUE FOR <sequence>` into `ID` themselves. Affected tables and the matching Vessel procedures are listed in [Sequences and default constraints](#sequences-and-default-constraints). Consequence: an Office-version procedure run against a vessel database (or any insert that omits `ID` on a vessel) fails with SQL error 515 "Cannot insert the value NULL into column 'ID'". If that error appears on a vessel, compare the deployed procedure with the Vessel script.
2. **Vessel sequences start at the vessel's replication ID.** On the vessel, `PR_REP_Missing_Packets_SEQ`, the acknowledgement sequence and the service-operation-status sequence start at `replication_id` followed by seven zeros, so each vessel's IDs fall in their own range (`RepIntegration/PAL.DatabaseScripts.Vessel/Scripts/025_SEQ_PR_REP_Missing_Packets.sql#L6-L13`, `RepIntegration/PAL.DatabaseScripts.Vessel/Scripts/056_SEQ_REP_ACKN.sql#L12`). On the Office they start at 1 (`RepIntegration/PAL.DatabaseScripts.Office/Scripts/025_SEQ_PR_REP_Missing_Packets.sql#L6`, `RepIntegration/PAL.DatabaseScripts.Office/Scripts/056_SEQ_REP_ACKN.sql#L8`). The Vessel versions also skip the `CO_Vessel_Particulars` row with `ID = -1` (`RepIntegration/PAL.DatabaseScripts.Vessel/Scripts/097_REP_SERVICE_OPERATION_STATUS_SEQ.sql#L8-L9`); the Office version of 097 does not. If `CO_Vessel_Particulars` was empty or wrong when the scripts ran, the vessel's ID range is wrong too.
3. **Delivery folder for methods 0 and 1.** `REP.PR_REP_TRANSFER_MASTER` maps delivery IDs 0 and 1 to `REP_OFF_ROOT` on the Office (`RepTransfer/PAL.DatabaseScripts.Office/Scripts/020_DATA_[REP].[PR_REP_TRANSFER_MASTER]_1.sql#L3`, `RepTransfer/PAL.DatabaseScripts.Office/Scripts/021_DATA_[REP].[PR_REP_TRANSFER_MASTER]_2.sql#L3`) but to `PR_REP_ROOT` on the Vessel (`RepTransfer/PAL.DatabaseScripts.Vessel/Scripts/005_DATA_[REP].[PR_REP_TRANSFER_MASTER]_1.sql#L3`, `RepTransfer/PAL.DatabaseScripts.Vessel/Scripts/006_DATA_[REP].[PR_REP_TRANSFER_MASTER]_2.sql#L3`). Delivery ID 2 maps to `REP_AZURE_ROOT` on both. So a "folder not found" for method 0/1 points at a different parameter on each side. `REP_OFF_ROOT` is seeded only by the Vessel `001_default_keys.sql` (`RepIntegration/PAL.DatabaseScripts.Vessel/InitialDeployment/001_default_keys.sql#L234-L236`); no Office script creates it, although Office scripts read it — where it comes from on the Office: Not determined from code (open question Q20). Delivery method 3 (`REP_REALM_ROOT`) is not in use (confirmed by the team).
4. **Transfer type lookup on the vessel reads a hard-coded `PAL` database.** The Vessel `REP.PR_GET_TRANSFER_DATA` reads `DELIVERY_METHOD` from `$__PALREP__$[REP].[REP_VESSEL_INFRA]` only when CO_Parameters `IS_PRODUCT` = `N`; otherwise it reads `[PAL].[REP].[REP_VESSEL_INFRA]` (`RepTransfer/PAL.DatabaseScripts.Vessel/StoredProcedures/002_SP_[Rep].[PR_GET_TRANSFER_DATA].sql#L13-L22`). No script seeds `IS_PRODUCT`, so when the parameter is missing the hard-coded `PAL` branch is used. On a vessel whose main database is not named `PAL`, the transfer type lookup fails or returns nothing. The Office version always uses the placeholder (`RepTransfer/PAL.DatabaseScripts.Office/StoredProcedures/002_SP_[Rep].[PR_GET_TRANSFER_DATA].sql#L13-L18`). Vessel `-999` (the office) always gets transfer type 2 on both sides.
5. **The vessel does not seed channels, queue settings or most parameters through the numbered scripts.** On the Vessel, `041_VALUE_PR_CHANNEL_SETTINGS.sql` keeps only the sequence-restart block; all seven channel inserts are commented out (`RepIntegration/PAL.DatabaseScripts.Vessel/Scripts/041_VALUE_PR_CHANNEL_SETTINGS.sql`). `043_VALUES_PR_PRIORITY_QUEUE_SETTINGS.sql` is entirely commented out, as are `051_DATA_[Common].[CO_Parameters].sql` and RepTransfer's `018_DATA_CO_PARAM_VALUE.sql`. Instead the Vessel `001_default_keys.sql` inserts four channels — `CHANNEL_RECORD`, `CHANNEL_FILE`, `TRANSFER_CHANNEL_FILE`, `TRANSFER_CHANNEL_FILE_V2V` (`RepIntegration/PAL.DatabaseScripts.Vessel/InitialDeployment/001_default_keys.sql#L300-L343`). No Vessel script creates `GENERAL_PACKET`, `GENERAL_NOTIFICATION` or `CHAT_MESSAGE_CHANNEL`, and none creates `PR_PRIORITY_QUEUE_SETTINGS` rows. RepIntegration stops with `General Packet channel information not found. Exiting.` without `GENERAL_PACKET` (ISS-INTEG-002). These rows probably reach the vessel through replication of the change-tracked Office settings tables, but that is Not determined from code (open question Q21). If a new vessel shows that message, check whether the settings tables have replicated yet.
6. **Vessel `REP_SOURCE_UNIQUE_ID` is the vessel's own ID.** The Office sets CO_Parameters `REP_SOURCE_UNIQUE_ID` to `-999` (`RepIntegration/PAL.DatabaseScripts.Office/InitialDeployment/001_default_keys.sql#L92-L97`). The Vessel reads `VESSEL_OBJECT_ID` from `REP_VESSEL_INFRA` and writes that instead, falling back to `-999` only if the table is missing (`RepIntegration/PAL.DatabaseScripts.Vessel/InitialDeployment/001_default_keys.sql#L93-L104`). The script runs `UPDATE` when the row exists, so re-running it resets the value. A vessel whose `REP_SOURCE_UNIQUE_ID` is `-999` identifies itself as the office.
7. **Vessel subscriber list includes the vessel itself.** The Vessel `142_DATA_REP_PR_SUBSCRIBER_LIST.sql` adds a `REP_PR_SUBSCRIBER_LIST` row for the vessel (queue name built from the client and environment placeholders plus the vessel ID) and two `REP_PR_SUBSCRIBER_LIST_DT` rows linking `-999` ↔ vessel (`RepIntegration/PAL.DatabaseScripts.Vessel/Scripts/142_DATA_REP_PR_SUBSCRIBER_LIST.sql#L7-L34`). The Office version inserts only the office row (`RepIntegration/PAL.DatabaseScripts.Office/Scripts/142_DATA_REP_PR_SUBSCRIBER_LIST.sql#L3`). The queue name comes from this table (`REP_GET_QUEUE_NAME`), so a vessel without its own row has no queue name (ISS-SBUS-002). The vessel lookup also needs an active, current (`RECORD_STATUS='CU'`, `ACTIVE='Y'`) `CO_Vessel_Register` row for the code and name.
8. **Chunk size differs.** `REP_CHUNK_SIZE` is forced to `5242880` (5 MB) on the Office (`RepIntegration/PAL.DatabaseScripts.Office/InitialDeployment/001_default_keys.sql#L172-L179`) and `1048576` (1 MB) on the Vessel (`RepIntegration/PAL.DatabaseScripts.Vessel/InitialDeployment/001_default_keys.sql#L179-L186`). The script updates an existing value, so a manual change is overwritten on every deployment. RepTransfer's Office scripts also seed `51200` if the row does not exist yet (`RepTransfer/PAL.DatabaseScripts.Office/Scripts/008_DATA_[Common].[CO_Parameters]_REP_CHUNK_SIZE.sql`) — whichever runs first creates it, and `001_default_keys.sql` then overwrites it.
9. **Vessel table-settings columns.** The Vessel `017_TABLE_REP_PRIORITY_TABLE_SETTINGS.sql` adds `FILE_SIZE`, `CATEGORY`, `SUB_CATEGORY` and `TRANSFER_MEDIUM_ID` (`RepIntegration/PAL.DatabaseScripts.Vessel/Scripts/017_TABLE_REP_PRIORITY_TABLE_SETTINGS.sql#L39-L60`). No Office script adds them, and no C# in the snapshot uses them. If the table is replicated office → vessel, the column sets differ (open question Q22).
10. **No change tracking on the vessel's settings tables.** Office enables SQL Server change tracking on `REP_PRIORITY_TABLE_SETTINGS`, `PR_CHANNEL_SETTINGS`, `PR_PRIORITY_CHANNEL_FLOW_SETTINGS` (`RepIntegration/PAL.DatabaseScripts.Office/Scripts/017_TABLE_REP_PRIORITY_TABLE_SETTINGS.sql#L28-L31`) and on `REP_SERVICEBUS_CREDENTIALS`. Office also registers `REP_SERVICEBUS_CREDENTIALS` in `Common.REP_Table_Settings` with `VSL_ACTIVE = 'N'` (`RepTransfer/PAL.DatabaseScripts.Office/Scripts/032_REP_SERVICEBUS_CREDENTIALS.sql#L16-L41`). The Vessel scripts do neither. This supports the reading that these tables flow office → vessel only (Q12).

## Sequences and default constraints

The Office creates the default constraint; the Vessel creates none, and the matching Vessel procedure supplies the ID. Keywords: NV_ default constraint, NEXT VALUE FOR, explicit ID.

| Table | Office default (Vessel: none) | Vessel procedure that supplies `ID` |
|---|---|---|
| `Common.CO_Parameters` | `NV_Co_Parameters_SEQ` (`RepIntegration/PAL.DatabaseScripts.Office/InitialDeployment/001_default_keys.sql#L48-L50`) | inserts use `NEXT VALUE FOR` on both sides |
| `REP.PR_PACKET_COUNTER_SETTINGS` | `NV_PR_PACKET_COUNTER_SETTINGS_SEQ` (`063_PR_PACKET_COUNTER_SETTINGS.sql`) | `GET_V2V_PACKET_COUNTER_IMPORT`, `GET_V2V_PACKET_COUNTER` (V2V, dropped) |
| `REP.REP_PR_PACKET_SOURCE` | `NV_REP_PR_PACKET_SOURCE_SEQ` (`065_REP_PR_PACKET_SOURCE.sql`) | `SAVE_EXT_PACKET_DETAILS` (`RepIntegration/PAL.DatabaseScripts.Vessel/StoredProcedures/046_SAVE_EXT_PACKET_DETAILS.sql`) |
| `REP.REP_PR_PACKET_SOURCE_DETAILS` | `NV_REP_PR_PACKET_SOURCE_DETAILS_SEQ` (`067_REP_PR_PACKET_SOURCE_DETAILS.sql`) | `SAVE_SOURCE_SUB_DETAILS` (`RepIntegration/PAL.DatabaseScripts.Vessel/StoredProcedures/047_SAVE_SOURCE_SUB_DETAILS.sql`) |
| `REP.REP_PR_SUBSCRIBER_LIST` | `NV_REP_PR_SUBSCRIBER_LIST_SEQ` (`082_REP_PR_SUBSCRIBER_LIST.sql`) | data script 142 uses `NEXT VALUE FOR` |
| `REP.PR_CHANNEL_SETTINGS` | `NV_PR_CHANNEL_SETTINGS_SEQ` (`027_TABLE_PR_CHANNEL_SETTINGS.sql`) | Vessel `001_default_keys.sql` channel inserts |
| `REP.PR_CO_PARAMETERS` | `NV_PR_CO_PARAMETERS_SEQ` (`038_TABLE_PR_CO_PARAMETERS.sql`) | Vessel `039_VALUES_PR_CO_PARAMETERS.sql` inserts |
| `REP.PR_PRIORITY_QUEUE_SETTINGS` | `NV_PR_PRIORITY_QUEUE_SETTINGS_SEQ` (Office `029_TABLE_…`, Vessel `028_TABLE_…`) | none — Vessel seed script is commented out |
| `REP.REP_PRIORITY_TABLE_SETTINGS` | `NV_PR_TABLE_SETTINGS_SEQ` (`RepIntegration/PAL.DatabaseScripts.Office/Scripts/017_TABLE_REP_PRIORITY_TABLE_SETTINGS.sql#L34-L37`) | none in scripts |
| `REP.REP_NOTIFICATION_LOG` | `DF_REP_NOTIFICATION_LOG_ID` (`050_TABLE_[Rep].[REP_NOTIFICATION_LOG].sql`) | `REP_SAVE_NOTIFICATION_ERROR_LOG`, `REP_SAVE_NOTIFICATION_LOG` (`RepIntegration/PAL.DatabaseScripts.Vessel/StoredProcedures/030_SP_[REP].[REP_SAVE_NOTIFICATION_ERROR_LOG].sql`, `RepIntegration/PAL.DatabaseScripts.Vessel/StoredProcedures/033_SP_[REP].[REP_SAVE_NOTIFICATION_LOG].sql`) |
| `REP.PR_SAVE_DATA_RECORDS` | `NV_PR_SAVE_DATA_RECORDS_SEQ` (`RepIntegration/PAL.DatabaseScripts.Office/Scripts/053_TABL_PR_SAVE_DATA_RECORDS.sql#L13-L17`) | `PR_REP_SAVE_DATA_OPERATION` (`RepIntegration/PAL.DatabaseScripts.Vessel/StoredProcedures/034_PR_REP_SAVE_DATA_OPERATION.sql`) |
| `REP.REP_PR_STORAGE_CREDENTIALS` | `NV_REP_PR_STORAGE_CREDENTIALS_SEQ` (`072_TABLE_…`) | none in scripts |
| `REP.REP_PR_SUBSCRIBER_LIST_DT` | `NV_REP_PR_SUBSCRIBER_LIST_DT_SEQ` (`075_TABLE_…`) | data script 142 uses `NEXT VALUE FOR` |
| `REP.REP_V2V_MASTER_LOG` (V2V, dropped) | `NV_REP_V2V_MASTER_LOG_SEQ` (Vessel: same block commented out) | — |
| `REP.REP_SERVICE_BUS_MASTER_SETTINGS` | `NV_SERVICE_BUS_MASTER_SEQ` (RepTransfer Office `026`, Vessel `012`) | none in scripts |
| `REP.REP_SERVICE_BUS_TRANSACTION_SETTINGS` | `NV_REP_SERVICE_BUS_TRANSACTION_SETTINGS_SEQ` (RepTransfer Office `028`, Vessel `014`) | none in scripts |
| `REP.PR_RESEND_QUEUE` | `NV_PR_RESEND_QUEUE_SEQ` (RepTransfer Office `030`, Vessel `017`) | none in scripts |

The `Common.CO_Parameters` sequence itself is created in `001_default_keys.sql` on both sides. The Office checks for a row in `CO_Vessel_Particulars` (`RepIntegration/PAL.DatabaseScripts.Office/InitialDeployment/001_default_keys.sql#L15`). The Vessel checks that the table exists and otherwise starts from replication code `1` (`RepIntegration/PAL.DatabaseScripts.Vessel/InitialDeployment/001_default_keys.sql#L16-L19`). The Vessel version also restarts `PR_CHANNEL_SETTINGS_SEQ` above the highest existing ID before inserting channels (`#L300-L314`).

## Table definitions

Small schema differences in RepIntegration table scripts. Keywords: primary key, column order, comments.

- `REP.PR_SAVE_DATA_RECORDS`: the Office makes `ID` the primary key (`RepIntegration/PAL.DatabaseScripts.Office/Scripts/053_TABL_PR_SAVE_DATA_RECORDS.sql#L4`); the Vessel table has **no primary key** (`RepIntegration/PAL.DatabaseScripts.Vessel/Scripts/053_TABL_PR_SAVE_DATA_RECORDS.sql#L4`), so duplicate IDs are not rejected on a vessel.
- `REP.PR_LOG_DB`: the Office `CREATE TABLE` includes `STACK_TRACE` and `IS_REQUEST_LOG` (`RepIntegration/PAL.DatabaseScripts.Office/Scripts/014_TABLE_PR_LOG_DB.sql#L16-L17`); the Vessel creates the table without them and adds them later with `ALTER TABLE` (`RepIntegration/PAL.DatabaseScripts.Vessel/Scripts/014_TABLE_PR_LOG_DB.sql#L26-L35`, and again in `059_ALT_TABLE_Rep.PR_LOG_DB.sql`). The end result is the same; only the column order differs.
- `REP.PR_REP_Missing_Packets`: the Office has no comma between `[CHANNEL_ID] [BIGINT]` and the `CONSTRAINT … PRIMARY KEY` clause (`RepIntegration/PAL.DatabaseScripts.Office/Scripts/006_TABLE_PR_REP_Missing_Packets.sql#L21`); the Vessel has one (`RepIntegration/PAL.DatabaseScripts.Vessel/Scripts/006_TABLE_PR_REP_Missing_Packets.sql#L21`). SQL Server accepts both, and both create the same primary key on `ID`.
- `REP.REP_AZURE_RES_UPLOAD_HISTORY` (`119_…`): the Vessel adds comments only.
- `REP_AZURE_RES_UPLOAD_TYP` (`102_…`): the Office first drops the four procedures that use the type (`REP_UPDATE_AZURE_RES_UPLOAD`, `REP_INSERT_AZURE_RES_UPLOAD`, `PR_REP_MOV_AZURE_RES_HIST`, `REP_UPDATE_AZURE_RES_INFO`) and the type, so a changed type is rebuilt. The Vessel lacks that block, so on a vessel an existing type is never rebuilt.
- `REP_PR_PACKET_STATUS_DATA_TYP` (`079_…`): the reverse — the Vessel drops `PR_REP_UPDATE_PACKET_DATA_BULK` and the type before recreating it; the Office does not.
- `036_PR_SERVICE_DETAILS.sql` (Vessel adds a `GO`) and `101_REP_AZURE_RES_UPLOAD.sql` (Office has an extra `GO`): batch separators only, no effect.

## Seed data

Differences in rows the scripts insert. Keywords: seed data, CO_Parameters, PR_CO_PARAMETERS, LOCATION, queue total limit.

- `REP.PR_CO_PARAMETERS` (`039_VALUES_PR_CO_PARAMETERS.sql`): the Vessel inserts `ID` explicitly, and two values differ — `LOCATION` is `OFF` on the Office and `VSL` on the Vessel, and `PR_QUEUE_TOTAL_LIMIT` is `1000` on the Office and `10000` on the Vessel. All other rows are the same.
- `Common.CO_Parameters` (`051_DATA_[Common].[CO_Parameters].sql`): active on the Office, where it seeds `REP_PR_AZURE_IN`, `REP_INTERGRATION_BASE_URL`, `REP_INTERGRATION_API_URL` (`Integration/Initiate-Import`), `REP_PR_KEY_MASTER_ID`, `REP_SOURCE_UNIQUE_ID` (`-999`), `REP_SOURCE_UNIQUE_OBJECT_TYPE`, `REP_INT_V2V_Download_API` and `REP_INTERGRATION_V2V_RESEND_API` (V2V, dropped), `REP_ZIP_UTILITY` (`SevenZip`) and `REP_RETRY_COUNT` (`21`) (`RepIntegration/PAL.DatabaseScripts.Office/Scripts/051_DATA_[Common].[CO_Parameters].sql#L12-L53`). Fully commented out on the Vessel; the commented copy names a different API URL (`Integration/IntegrateTrackImport`) and an EAS log endpoint. On the Vessel the non-V2V parameters come from `001_default_keys.sql` instead, which seeds the same parameter list on Office and Vessel except `REP_OFF_ROOT` (Vessel only).
- `001_default_keys.sql` other differences: the Vessel moves the `IS_VESSEL` insert later in the file (same row, value from the `$__IS_VESSEL__$` placeholder) and adds the `REP_OFF_ROOT` and channel inserts described above.
- RepTransfer `CO_Parameters` (Office `031_DATA_CO_PARAM_VALUE.sql`, Vessel `018_DATA_CO_PARAM_VALUE.sql`): active on the Office, fully commented out on the Vessel. On the Office it builds folder parameters from `REP_OFF_ROOT` (`RepTransfer/PAL.DatabaseScripts.Office/Scripts/031_DATA_CO_PARAM_VALUE.sql#L12`) — if `REP_OFF_ROOT` is missing the folder values become NULL. It also builds a sequence-restart statement but never executes it (no `EXEC`, `#L9`). Every insert is `IF NOT EXISTS`, and the single-parameter scripts 005–019 run first, so they win (see below).
- `REP.PR_PRIORITY_QUEUE_SETTINGS` (`043_…`): two rows (channels 1 and 2, `QUEUE_COUNT` 500) on the Office; commented out on the Vessel.
- `REP.PR_CHANNEL_SETTINGS` (`041_…`): seven channels on the Office; inserts commented out on the Vessel (see point 5).
- RepTransfer Vessel-only `020_DATA_PR_VESSEL_VALUE.sql`: copies rows from `Common.REP_Vessel_Settings` into `Common.PR_REP_Vessel_Settings` with `IS_PARALLEL = 1`, `IS_PRIORITY_ENABLED = 1` and packet counters 0, but only if none of those vessels is already there (`RepTransfer/PAL.DatabaseScripts.Vessel/Scripts/020_DATA_PR_VESSEL_VALUE.sql#L1-L19`). On a vessel, Priority Replication is therefore switched on for the vessel by deployment.

## Office-only files

Files that exist only in the Office projects. Keywords: office only, single parameter scripts, utilities, release notes, intro script.

- RepIntegration `Scripts/070_SEQ_REP_PR_SUBSCRIBER_LIST_SEQ.sql` and Vessel-only `Scripts/070_REP_PR_SUBSCRIBER_LIST_SEQ.sql` are the same script under two names (same `REP_PR_SUBSCRIBER_LIST_SEQ` sequence, identical content).
- RepTransfer Office `005`–`019` single-parameter scripts, one `Common.CO_Parameters` row each, inserted only if missing: `REP_AZURE_ROOT` (folder under the base path), `REP_AZURE_STORAGE_ACCOUNT_KEY` **(secret — seeded empty)**, `REP_AZURE_STORAGE_ACCOUNT_NAME` (empty), `REP_CHUNK_SIZE` (`51200`), `REP_CLIENT_CODE` (empty), `REP_CLIENT_ENVIROMENT_UNICID` (empty), `REP_EXPORT_TRANSFER_API_URL`, `REP_EXPORT_TRANSFER_BASE_URL` (empty), `REP_PARALLEL_PROCESS_COUNT` (`2`), `REP_PR_FILECABINET_IN` and `REP_PR_NORMAL_IN` (folders under the base path), `REP_REALM_ROOT` (method 3, not in use), `REP_SERVICE_NAME` (empty), `REP_SERVICEBUS_CONNECTION_STRING` **(secret — seeded empty)**, `REP_STORAGE_CONTAINER_NAME` (empty) (`RepTransfer/PAL.DatabaseScripts.Office/Scripts/011_DATA_[Common].[CO_Parameters]_REP_EXPORT_TRANSFER_API_URL.sql` and siblings). Note the API URL: script `011` seeds `Integration/TransferPacketFolder`, while `031` would seed `Transfer/TransferPacketFolder`; `011` runs first, so the Office gets `Integration/TransferPacketFolder` unless the row already existed. RepIntegration's `001_default_keys.sql` also seeds this parameter on both sides. Which value a site actually has depends on run order: check it when RepIntegration cannot call RepTransfer.
- RepTransfer Office `Utilities/` (deployment tooling, not replication runtime):
  - `ReleaseNoteUploader/StoredProcedure/InsertScriptReleaseNote-001.sql` creates `[Admin].[Insert_ReleaseNotes]`, which writes to `ADMIN.AD_DA_APPLICATION_RELEASE_NOTES` (`RepTransfer/PAL.DatabaseScripts.Office/Utilities/ReleaseNoteUploader/StoredProcedure/InsertScriptReleaseNote-001.sql#L11`). `ReleaseNoteUploader/Utility/ReleaseNoteInterface.exe.config` holds only assembly bindings.
  - `ScriptExecutorConsole/UpdateScriptVersion.vbs`: a VBScript that reads and writes registry DWORD values for the script version (`RepTransfer/PAL.DatabaseScripts.Office/Utilities/ScriptExecutorConsole/UpdateScriptVersion.vbs#L48-L82`).
  - `Scripts/001_Dashboard_IntroScript.sql` and `Scripts/002_IntroScript _Prod.sql`: UI guided-tour content for `Training.Intro_Contents`; nothing replication-related.
- Shared by both sides and identical: `Utilities/RDLUploader/ReadMe.txt` and `SSRS.Upload.exe.config` (SSRS report uploader; config keys `SSRS_ServerUrl`, `SSRS_DataSource`, `SSRS_Folder_Name`, `SSRS_IsFormAuth`, `RDL_File_Path`), `Utilities/ScriptExecutorConsole/RunScriptExecuter.bat` (runs `ScriptExecutorConsole.exe` with a source path and a DB connection passed as arguments) and `ScriptExecutorConsole.exe.config` (`ExitOnError`, a `Connect` connection string — value not copied).

## Vessel-only files

Keywords: vessel only, REP_GETDOWNLOADS_TABLEID.

- `REP.REP_GETDOWNLOADS_TABLEID @PACKET_NAME`: returns the `TABLE_SETTINGS_ID` of the newest `REP.REP_Downloads` row whose file name contains the packet name (`RepIntegration/PAL.DatabaseScripts.Vessel/StoredProcedures/037_REP_GETDOWNLOADS_TABLEID.sql#L4-L10`). Called by RepAcquisition. It does not exist in an Office database, so an Office call fails with "Could not find stored procedure".
- `070_REP_PR_SUBSCRIBER_LIST_SEQ.sql` (same as Office `070_SEQ_…`) and RepTransfer `020_DATA_PR_VESSEL_VALUE.sql` (above).

## Renumbered files

Same object, different number (and therefore different run order). Keywords: renumbered, run order.

- RepIntegration: `PR_PRIORITY_QUEUE_SETTINGS` sequence and table swap places (Office `028_SEQ`/`029_TABLE`, Vessel `029_SEQ`/`028_TABLE`). On the Vessel the table script runs before its sequence exists, which is harmless only because the Vessel table has no default constraint. `REP_UPDATE_AZURE_RES_UPLOAD` 084 → 130, `REP_UPDATE_TRANSFER_QUEUE` 087 → 131, `REP_UPDATE_AZURE_RES_INFO` 110 → 132 and `PR_REP_MOV_AZURE_RES_HIST` 111 → 133 (Office → Vessel). Their content differs only in comments; `REP_UPDATE_TRANSFER_QUEUE` on the Vessel also drops two blocks that were already commented out on the Office (old history move for status 4/7).
- RepTransfer: Office `020`–`032` are Vessel `005`–`019` (the Vessel has no single-parameter scripts, so numbering shifts). Contents identical except `PR_REP_TRANSFER_MASTER` rows 1–2, `CO_PARAM_VALUE`, `REP_SERVICEBUS_CREDENTIALS`, the two Service Bus settings tables and `PR_RESEND_QUEUE`, all covered above.

## Procedure differences with no behaviour change

Keywords: comment only, return message.

- Comment-only changes: `REP_MOV_TRANSFER_QUEUE_HIST` (`125_…`), `SAVE_REP_TRANSFER_QUEUE` (`128_…`), and the four renumbered procedures above.
- `SAVE_EXT_PACKET_DETAILS`: besides the explicit ID, the Vessel removes a commented-out insert into `REP_PR_PACKET_DESTINATION`.
- `GET_V2V_MASTER_LOG_DATA` (V2V, dropped): `ISNULL(FILE_CHECK_SUM, 'EMPTY')` on the Office vs `''` on the Vessel.

## Related

- INV-MSREP-DB-FILES — every script file with its Office/Vessel status (generated).
- DATA-MSREP-OVERVIEW — where the scripts live and how they are deployed.
- DATA-MSREP-SETTINGS — channels, table settings, delivery methods.
- ISS-TRANSFER-001, ISS-INTEG-002, ISS-SBUS-002 — issues that the differences above can explain.
