---
doc_id: DATA-IREP
type: reference
mechanism: [irep]
group: data
runs_on: [office, vessel]
components: [ExportCDT, ExportDCS, ImportDES, ImportDSC, ImportRBP, ComPBR]
log_files: []
error_types: [db, dataapply, sequence]
applies_to_versions: ["Not determined from code"]
sources: ["iRep database scripts (iRepScript, IntialDeployment) staged 2026-11-11"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# sync+ databases — tables that hold the operational truth

This article lists the sync+ tables that support staff check when data is late or missing, grouped by database. The full object list (231 objects, with the services that call each procedure) is in INV-IREP-DB. Use these tables read-only; any change goes through the platform team.

## Script layout

The deployment scripts live in `iRepScript` (per database) and `IntialDeployment` (seed data). Keywords: iRepScript, IntialDeployment, deployment order, BSM, TaskTrack.

- `iRepScript/COMMON`, `PAL`, `REP2X`, `REP2I` and `REP2X,REP2I`: each has `001_Scripts` (tables, sequences, types) and `003_StoredProcedures`.
- `iRepScript/iRep/001_MISSING_DATABASE_CREATION.sql` creates missing databases.
- `IntialDeployment/BSM` and the TaskTrack variants seed `EXPORT_TABLE_ORDER`, `REP_EXPORT_VESSEL_QUERY`, `REP_ATTACHMENT_QUERY` and `REP_APPLICATION_HD_MAPPING` (for example `IntialDeployment/BSM/001_EXPORT_TABLE_ORDER_INSERTION.sql#L6`). Several seed tables are created in the `DBO` schema there, but in `REP` by iRepScript (`iRepScript/REP2X/001_Scripts/002_Export_Tables_Sequence.sql#L111`). Which one the services read depends on the procedure. This is an open question.
- Three procedures called by code are in no staged script: `REP.REP_AZ_CROSS_VERIFY_CDT_VERSION` (ExportDCS), `REP.REP_CDT_QUERIES_PAL_READ_ONLY` (ExportCDT) and `REP.REP_READ_CONNECTION_STRING` (ExportCDT, ImportDSC, ImportRBP). An environment without them fails with "Could not find stored procedure" (ISS-IREXP-DB, ISS-IRIMP-DB).

## Export side (REP2X)

These are the tables ExportCDT and ExportDCS write in order (FLW-IREP-EXPORT). Keywords: REP_RECORD_SYNC, REP_RECORD_VESSEL_SYNC, REP_OUT_PACKET_HD, REP_EXPORT_OUT_PACKET_NUMBER, spam, resend log.

| Table | Holds | Defined |
|---|---|---|
| `REP.EXPORT_TABLE_ORDER` | Tables to export, with order, CDT query (office/vessel), DCS export query, attachment flag, transfer applicability, replica type | `iRepScript/REP2I/001_Scripts/030_EXPORT_TABLE_ORDER.sql#L13` |
| `REP.REP_EXPORT_VESSEL_QUERY` | Vessel routing queries (office/vessel, insert/delete) per table | `iRepScript/REP2X/001_Scripts/002_Export_Tables_Sequence.sql#L111` |
| `REP.REP_RECORD_SYNC` (+ `_HISTORY`) | Changed ids captured by CDT, waiting for routing | `iRepScript/REP2X/001_Scripts/002_Export_Tables_Sequence.sql#L273` |
| `REP.REP_RECORD_VESSEL_SYNC` (+ attachment variant, history) | Ids routed per vessel, waiting for DCS | `iRepScript/REP2X/001_Scripts/002_Export_Tables_Sequence.sql#L360` |
| `REP.REP_RECORD_VESSEL_SPAM`, `REP.REP_SPAM_TABLE_VESSEL`, `REP.RECORD_SPAM_SETTINGS` | Rows held back as spam, and the spam rules | `iRepScript/REP2X/001_Scripts/002_Export_Tables_Sequence.sql#L301` |
| `REP.REP_CDT_VERSION`, `REP.REP_LAST_EXT_CDT_VERSION` | Change tracking versions extracted | `iRepScript/REP2X/001_Scripts/002_Export_Tables_Sequence.sql#L244`, `iRepScript/COMMON/001_Scripts/002_REP.REP_LAST_EXT_CDT_VERSION.sql#L6` |
| `REP.REP_EXPORT_OUT_PACKET_NUMBER` | Last packet counter per vessel (sender side) | `iRepScript/REP2X/001_Scripts/008_REP.REP_EXPORT_OUT_PACKET_NUMBER.sql#L6` |
| `REP.REP_OUT_PACKET_HD`, `REP.REP_OUT_QUEUE` | Packets created and their outgoing queue | `iRepScript/REP2X/001_Scripts/016_REP.REP_OUT_PACKET_HD.sql#L6` |
| `REP.REP_REPLICA_RESEND_LOG` | Auto-resend attempts | `iRepScript/REP2X/001_Scripts/022_REP_REPLICA_RESEND_LOG.sql#L6` |
| `REP.REP_EXPORT_CONFIG_PATH_MAP` | Export paths per vessel | `iRepScript/REP2X/001_Scripts/007_REP.REP_EXPORT_CONFIG_PATH_MAP.sql#L6` |
| `REP.REP_CONNECTION_STRINGS` | Connection strings (**secret**: presence checks only) | `iRepScript/REP2X/001_Scripts/002_Export_Tables_Sequence.sql#L181` |
| `REP.REP_PARAMETERS` | Parameters (see CFG-IREP) | `iRepScript/REP2X/001_Scripts/012_REP.REP_PARAMETERS.sql#L7` |
| `REP.R2_REP_ERROR_LOG` | Routing failures written when `LogErrorToDB` is enabled | `iRepScript/REP2X/001_Scripts/018_R2_REP_ERROR_LOG.sql#L6` |

## Import side (REP2I)

These are the tables ImportDES, ImportDSC and ImportRBP move through in order (FLW-IREP-IMPORT). Keywords: REP_DES_VALIDATE_QUEUE, REP_DES_PROCESS_QUEUE, REP_IMPORT_IN_PACKET_NUMBER, REP_ERROR_DES_SKIP_LIST, REP_REPLICA_PACKET_STATUS.

| Table | Holds | Defined |
|---|---|---|
| `REP.REP_DES_VALIDATE_QUEUE` | Received packets waiting for validation | `iRepScript/REP2I/001_Scripts/009_REP_DES_VALIDATE_QUEUE.sql#L6` |
| `REP.REP_DES_PROCESS_QUEUE` | Validated packets waiting to be read | `iRepScript/REP2I/001_Scripts/006_REP_DES_PROCESS_QUEUE.sql#L7` |
| `REP.REP_DES_PROC_LIVE_DATA` | Rows read and waiting for RBP | `iRepScript/REP2I/001_Scripts/003_REP_DES_PROC_LIVE_DATA.sql#L6` |
| `REP.REP_IMPORT_IN_PACKET_NUMBER` | Last applied packet counter per vessel (receiver side) | `iRepScript/REP2I/001_Scripts/002_REP_IMPORT_IN_PACKET_NUMBER.sql#L6` |
| `REP.REP_REPLICA_PACKET_STATUS` | Missing or incorrect packet status rows | `iRepScript/REP2I/001_Scripts/033_REP_REPLICA_PACKET_STATUS.sql#L6` |
| `REP.REP_ERROR_DES_SKIP_LIST`, `REP.REP_ERROR_DES_PROCESS_LIST` | Packets and rows skipped during validation or reading | `iRepScript/REP2I/001_Scripts/037_REP_ERROR_DES_SKIP_LIST.sql#L6` |
| `REP.REP_IMPORT_CONFIG_PATH_MAP`, `REP.REP_IMP_JSON_PATH` | Inbox, error and in-temp paths per vessel; DSC JSON directory | `iRepScript/REP2I/001_Scripts/014_REP_IMPORT_CONFIG_PATH_MAP.sql#L6` |
| `REP.REP_IMPORT_TABLE_ORDER`, `REP.REP_IMPORT_BLOB_ORDER` | Import order of tables and attachments | `iRepScript/REP2I/001_Scripts/018_[REP].[REP_IMPORT_TABLE_ORDER].sql#L7` |
| `REP.REP_REPLICA_IMPORT_QUEUE` | RBP read queue (INS_OR_UPD / DEL) | `iRepScript/REP2I/001_Scripts/022_[REP].[REP_REPLICA_IMPORT_QUEUE].sql#L6` |
| `REP.REP_REPLICA_ERROR_LOG`, `REP.REPLICA_REPROCESS_LOG` | RBP failures and reprocess runs | `iRepScript/REP2I/001_Scripts/021_[REP].[REP_REPLICA_ERROR_LOG].sql#L7` |
| `REP.PROCESS_Q_WAIT_TIMER` | Awaiter rows written after a vessel error (DCS) | `iRepScript/REP2I/001_Scripts/024_PROCESS_Q_WAIT_TIMER.sql#L6` |
| `REP.REP_PACKET_REGENERATE*` | Requests to regenerate packets | `iRepScript/REP2I/001_Scripts/035_[REP].[REP_PACKET_REGENERATE].sql#L5` |
| `REP.REP_REPLICA_TYPE_MASTER` | Replica types | `iRepScript/REP2I/001_Scripts/029_REP_REPLICA_TYPE_MASTER.sql#L13` |

`PROCESS_Q_WAIT_TIMER` and `EXPORT_TABLE_ORDER` are defined in REP2I scripts but used by the export side. The code reaches them through the connection it calls "AzureDB". Not determined from code: whether REP2X and REP2I are one database in some installations (the `REP2X,REP2I` script folder suggests shared objects).

## PAL side

PAL holds change tracking, application endpoint tables and the status-report tables used by alerts. Keywords: IREP_ENDPOINTMANAGER, status report, smrtSyn alert.

- `REP.IREP_ENDPOINTBASEADDRESS`, `REP.IREP_ENDPOINTMANAGER` and `REP.IREP_TABLE_IP_CALL` hold the application endpoints that RBP posts to (`iRepScript/PAL/001_Scripts/002_CONFLICT_TABLES_SEQUENCES.sql#L6`).
- `REP.REP_SMRTSYN_PLUS_STATUS_REPORT`, `REP.REP_SMRTSYN_STATUS_REPORT`, `REP.REP_TILE_ALERT_STATUS_TABLE` and `REP.REP_TILE_MISSING_STATUS_TABLE` hold the status reports and dashboard tiles (`iRepScript/PAL/001_Scripts/004_Replication_Status_Report_Tables.sql#L3`). They are a ready-made source for the ReplicationDashboard's sync+ health view (open question: who fills them and how often).

## Read-only checks the dashboard should run

These checks answer "where is it stuck" without logs. They are not written as scripts yet: they need the column names confirmed per version. Keywords: dashboard checks, silent failure, queue age.

| Check | Shows |
|---|---|
| Oldest `REP_RECORD_SYNC` row per table id | CDT routing stuck (ISS-IREP-CDT-002/003) |
| Count of `REP_RECORD_VESSEL_SYNC` rows per vessel, plus the age of the oldest | DCS not exporting that vessel (ISS-IREP-DCS-001/002) |
| `REP_EXPORT_OUT_PACKET_NUMBER` compared with the last OutPacketHd per vessel | Counter increased without a packet record |
| Oldest `REP_DES_VALIDATE_QUEUE` and `REP_DES_PROCESS_QUEUE` row per vessel | DES stuck (ISS-IREP-DES-*) |
| `REP_IMPORT_IN_PACKET_NUMBER` compared with the lowest counter waiting in the validate queue | Counter gap (ISS-IREP-DES-002) |
| Row count of `<table>_REP` and `_REP_DEL` | RBP not applying (ISS-IREP-RBP-001) |
| Rows in the skip, error and packet-status tables added in the last 24 h | Silent data skips |

## Related

INV-IREP-DB, FLW-IREP-EXPORT, FLW-IREP-IMPORT, CFG-IREP
