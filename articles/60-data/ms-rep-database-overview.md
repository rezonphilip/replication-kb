---
doc_id: DATA-MSREP-OVERVIEW
type: reference
mechanism: [priority-replication, smartsync]
group: data
runs_on: [office, vessel]
components: [RepIntegration, RepTransfer, RepDBLogW]
sources: ["MS-REP database scripts snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# MS-REP database — how the scripts are organised and what lives where

The MS-REP database objects are deployed from two script projects: `RepIntegration/PAL.DatabaseScripts.{Office,Vessel}` (Priority Replication, queues, logs, V2V) and `RepTransfer/PAL.DatabaseScripts.{Office,Vessel}` (transfer/SmartSync settings, upload/download records). Almost everything lives in the `REP` schema; parameters live in `Common.CO_Parameters`. Full object list: `inventory/ms-rep-db.md`.

## Script layout and deployment order

Each project has numbered folders that run in order; every script is written to be re-runnable. Keywords: deployment, database scripts, InitialDeployment, Scripts, StoredProcedures, re-run, idempotent.

| Folder | What it contains | Example |
|---|---|---|
| `InitialDeployment` | Schemas `REP` and `COMMON`, the `Common.CO_Parameters` sequence/table and default parameter rows (secret values are deployment placeholders such as `$__…__$`) | `RepIntegration/PAL.DatabaseScripts.Office/InitialDeployment/001_default_keys.sql` |
| `Scripts` | Tables, table types, sequences, `ALTER TABLE … ADD` column upgrades, seed data | `RepIntegration/PAL.DatabaseScripts.Office/Scripts/017_TABLE_REP_PRIORITY_TABLE_SETTINGS.sql` |
| `StoredProcedures` | `DROP` + `CREATE PROCEDURE` per file | `RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/112_PRIORITY_RESEND_DATA.sql` |
| `Utilities` | Tools shipped alongside (script executor console, SSRS uploader, release-note uploader). Not replication logic. | `RepTransfer/PAL.DatabaseScripts.Office/Utilities/` |

- Table scripts use `IF NOT EXISTS (… INFORMATION_SCHEMA.TABLES …)` then `CREATE TABLE`, and later columns are added with `IF NOT EXISTS (… COLUMNS …) ALTER TABLE … ADD` (for example `RepIntegration/PAL.DatabaseScripts.Office/Scripts/044_TABLE_PR_REP_Vessel_Settings.sql#L30-L44`). A database that missed an upgrade script will lack those columns — procedures that use them then fail.
- Most settings tables have **SQL Server change tracking** enabled (for example `RepIntegration/PAL.DatabaseScripts.Office/Scripts/017_TABLE_REP_PRIORITY_TABLE_SETTINGS.sql#L28-L31`, `RepIntegration/PAL.DatabaseScripts.Office/Scripts/027_TABLE_PR_CHANNEL_SETTINGS.sql#L25-L28`). Why it is enabled is Not determined from code (likely so the tables themselves can be replicated — open question Q12).
- IDs come from sequences bound as column defaults (for example `NV_PR_TABLE_SETTINGS_SEQ` in `RepIntegration/PAL.DatabaseScripts.Office/Scripts/017_TABLE_REP_PRIORITY_TABLE_SETTINGS.sql#L34-L38`).

## Office and vessel scripts differ

The Office and Vessel projects create mostly the same objects, but some tables and procedures differ, so do not assume a vessel database looks like the office one. Keywords: office vs vessel, schema difference, vessel database.

Files that differ in size between Office and Vessel (RepIntegration) include `014_TABLE_PR_LOG_DB`, `017_TABLE_REP_PRIORITY_TABLE_SETTINGS`, `027_TABLE_PR_CHANNEL_SETTINGS`, `039_VALUES_PR_CO_PARAMETERS`, `041_VALUE_PR_CHANNEL_SETTINGS`, `072_TABLE_REP_PR_STORAGE_CREDENTIALS`, and procedures `GET_V2V_PACKET_COUNTER`, `REP_MOV_TRANSFER_QUEUE_HIST`, `SAVE_REP_TRANSFER_QUEUE`. Vessel-only procedures include `REP_GETDOWNLOADS_TABLEID` (`RepIntegration/PAL.DatabaseScripts.Vessel/StoredProcedures/037_REP_GETDOWNLOADS_TABLEID.sql`). A line-by-line comparison has not been done yet (open question Q13).

One concrete difference: `REP.PR_GET_TRANSFER_DATA` on the vessel reads the vessel's delivery method from `[PAL].[REP].[REP_VESSEL_INFRA]` unless `IS_PRODUCT` = `N`, while the office version always uses the `$__PALREP__$` database placeholder (`RepTransfer/PAL.DatabaseScripts.Vessel/StoredProcedures/002_SP_[Rep].[PR_GET_TRANSFER_DATA].sql#L11-L23` vs `RepTransfer/PAL.DatabaseScripts.Office/StoredProcedures/002_SP_[Rep].[PR_GET_TRANSFER_DATA].sql#L11-L19`).

## Main table groups

The tables fall into settings, export state, import state, transport queues, and logs. Keywords: tables, packet header, track change, import queue, transfer queue, downloads, logs.

| Group | Tables (REP schema unless noted) | Article |
|---|---|---|
| Settings | `REP_PRIORITY_TABLE_SETTINGS`, `PR_CHANNEL_SETTINGS`, `PR_PRIORITY_CHANNEL_FLOW_SETTINGS`, `PR_PRIORITY_QUEUE_SETTINGS`, `Common.PR_REP_Vessel_Settings`, `PR_PACKET_COUNTER_SETTINGS`, `PR_SERVICE_DETAILS`, `COMMUNICATION_TYPE`, `REP_TYPE_TRANSFER_MEDIUM`, `PR_REP_TRANSFER_MASTER`, `PR_CO_PARAMETERS` | DATA-MSREP-SETTINGS |
| Export state | `PR_TRACKCHANGE_RECORDS`, `PR_TRACKCHANGE_VESSELS`, `PR_REP_OUT_Packet_HD`, `PR_REP_OUT_PACKET_DT`, `PR_REP_OUT_FILE_HD/DT`, `PR_Zip_Splits`, `REP_PR_PACKET_SOURCE(_DETAILS)` | DATA-MSREP-STATUS |
| Import state | `PR_REP_IN_Packet_HD`, `PR_REP_IN_Packet_DT`, `PR_REP_IMPORT_QUEUE(_DT, _HISTORY)`, `PR_REP_Missing_Packets`, `PR_SAVE_DATA_RECORDS`, `REP_ACKN` | DATA-MSREP-STATUS |
| Resend | `PR_RESEND_LOG`, `PR_RESEND_QUEUE` (RepTransfer scripts), `V2V_RESEND_LOG` | DATA-MSREP-RESEND |
| Transport queues | `REP_TRANSFER_QUEUE(_HISTORY)`, `REP_AZURE_RES_UPLOAD(_HISTORY)`, `REP_Downloads`, `REP_DOWNLOADS_HISTORY`, `REP_UPLOAD_FILE`, `REP_BULK_TRANSFER_STATUS` | DATA-MSREP-STATUS |
| Service Bus / notifications | `REP_SERVICEBUS_CREDENTIALS`, `REP_SERVICE_BUS_MASTER_SETTINGS`, `REP_SERVICE_BUS_TRANSACTION_SETTINGS`, `REP_SBUS_NOTIFICATION`, `REP_TABLE_NOTIF_QUEUE`, `PR_REP_MESSAGE_NOTIF_QUEUE`, `PR_REPLICATED_CHAT_QUEUE` | DATA-MSREP-SETTINGS |
| V2V | `REP_PR_SUBSCRIBER_LIST(_DT)`, `REP_V2V_MASTER_LOG(_DETAILS)`, `V2V_STATUS_HIS`, `REP_PR_STORAGE_CREDENTIALS` | — (not yet written) |
| Logs | `PR_LOG_DB`, `PR_REP_LOG`, `REP_NOTIFICATION_LOG`, `REP_SERVICE_OPERATION_STATUS` | — |

## Where secrets are stored

Two different places hold secrets; neither may be copied into the KB, tickets or chat. Keywords: credentials, connection string, storage key, client secret, REP_SERVICEBUS_CREDENTIALS.

- `REP.REP_SERVICEBUS_CREDENTIALS` (`NAME`, `VALUE`) holds `REP_SERVICEBUS_CONNECTION_STRING` and `REP_AZURE_STORAGE_ACCOUNT_KEY`. `REP_GET_SBUS_SETTINGS` and `REP_GET_AZURE_SETTINGS` read the secret from this table and the non-secret settings from `Common.CO_Parameters` (`RepTransfer/PAL.DatabaseScripts.Office/StoredProcedures/010_SP_[REP].[REP_GET_SBUS_SETTINGS].sql#L7-L9`, `RepTransfer/PAL.DatabaseScripts.Office/StoredProcedures/009_SP_[REP].[REP_GET_AZURE_SETTINGS].sql#L7-L9`). `PR_GET_PARAM_DATA` with `CO_PARAM_SBUS` excludes those two names from CO_Parameters and takes them from the credentials table instead (`RepTransfer/PAL.DatabaseScripts.Office/StoredProcedures/001_SP_[REP].[PR_GET_PARAM_DATA].sql#L17-L21`).
- `REP.REP_SERVICE_BUS_MASTER_SETTINGS` has a `CLIENT_SECRET` column (`RepTransfer/PAL.DatabaseScripts.Office/Scripts/026_REP_SERVICE_BUS_MASTER_SETTINGS.sql`).
- The deployment scripts seed these names with placeholders or empty values, not real secrets (checked 2026-11-11).

**Consequence for troubleshooting:** a `CO_Parameters` row for `REP_SERVICEBUS_CONNECTION_STRING` may be empty while the service works, because the value is taken from `REP_SERVICEBUS_CREDENTIALS`. Check the credentials table (presence only) — see `catalog/scripts/sbus-settings-presence.sql`.

## Objects referenced in code but not in these scripts

Some procedures and tables the services use are created elsewhere. Keywords: external database, PAL_REP, REP_VESSEL_INFRA, missing object.

- `REP.REP_VESSEL_INFRA` (per-vessel `DELIVERY_METHOD`) and `REP.PR_REP_TRANSFER_LOCATIONS` are read by `PR_GET_TRANSFER_DATA` but not created by these scripts; the vessel infra table is read from another database (`$__PALREP__$` / `[PAL]`).
- 17 procedures called from C# are not created by these scripts (for example `REP.READ_COMMON_PARAMS_VALUE`, `REP.REP_PR_READ_QUEUE_NAME`, `REP.UPDATE_PR_COUNTER_SETTINGS`) — list in `inventory/ms-rep-db.md`. Their source: Not determined from code (open question Q14).

## Related

- INV-MSREP-DB, DATA-MSREP-STATUS, DATA-MSREP-SETTINGS, DATA-MSREP-RESEND, CMP-REPDBLOGW
