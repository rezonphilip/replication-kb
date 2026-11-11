---
doc_id: DATA-MSREP-SETTINGS
type: reference
mechanism: [priority-replication, smartsync]
group: data
runs_on: [office, vessel]
components: [RepIntegration, RepTransfer, RepAckn, RepQueueManage]
sources: ["MS-REP code and database scripts snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# MS-REP settings tables — what controls what

Priority Replication is driven by a handful of settings tables: which tables replicate (table settings), how work is grouped (channels and flows), which vessels take part (vessel settings), and how packets leave (delivery method and transfer master). Most "export exits early" and "transfer type not found" problems are a missing or wrong row in one of these.

> **V2V (vessel-to-vessel) is a dropped feature.** The V2V routes, procedures and message types mentioned in this article still exist in the code and database but are not in use; do not troubleshoot them. See DATA-MSREP-OFFVSL.

## Table settings — what replicates

`REP.REP_PRIORITY_TABLE_SETTINGS` has one row per replicated table or file type, with separate export/import queries for office and vessel and the destination URLs. Keywords: table settings, TableSettingsId, export query, import query, OFF_BASE_URL, VSL_API_URL.

- Columns include `MASTER_TABLE`, `OFFICE_EXPORT_QUERY`, `OFFICE_IMPORT_QUERY`, `VESSEL_EXPORT_QUERY`, `VESSEL_IMPORT_QUERY`, `CHANNEL_ID`, `PRIORITY`, `IS_FILE`, and `OFF_BASE_URL` / `VSL_BASE_URL` / `OFF_API_URL` / `VSL_API_URL` (`RepIntegration/PAL.DatabaseScripts.Office/Scripts/017_TABLE_REP_PRIORITY_TABLE_SETTINGS.sql#L4-L21`).
- The `TableSettingsId` in RepIntegration and RepAckn log lines is this table's `ID`.
- RepAckn's `Base URL or API URL is empty for Table Settings Id {TableSetttingsId}` (`RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L104`) points at the base/API URL columns of this table being empty for that ID. Which of the office/vessel pair is used on which side: Not determined from code.

## Channels, flows and queue settings — how work is grouped

Channels group table settings; flow rows define the service-to-service order per channel; queue settings cap how many items a channel exports. Keywords: channel, PR_CHANNEL_SETTINGS, channel flow, PR_PRIORITY_CHANNEL_FLOW_SETTINGS, queue count, GENERAL_PACKET.

- `REP.PR_CHANNEL_SETTINGS`: `CHANNEL_NAME`, `START_INTERVAL`, `QUEUE_COUNT`, `RETRY_LIMIT`, `IS_SINGLE`, `IS_PARALLEL`, `PRIORITY`, `CHANNEL_TYPE`, `LAST_EXPORT_TIME`, `LAST_IMPORT_TIME` (`RepIntegration/PAL.DatabaseScripts.Office/Scripts/027_TABLE_PR_CHANNEL_SETTINGS.sql#L4-L19`).
- Seeded channel names: `CHANNEL_RECORD`, `CHANNEL_FILE`, `TRANSFER_CHANNEL_FILE`, `TRANSFER_CHANNEL_FILE_V2V`, `CHAT_MESSAGE_CHANNEL`, `GENERAL_NOTIFICATION`, `GENERAL_PACKET` (`RepIntegration/PAL.DatabaseScripts.Office/Scripts/041_VALUE_PR_CHANNEL_SETTINGS.sql`). IDs come from a sequence, so they can differ between databases — always look channels up by name. In the Vessel copy of this script **all** channel inserts are commented out; the vessel's `001_default_keys.sql` creates only `CHANNEL_RECORD`, `CHANNEL_FILE`, `TRANSFER_CHANNEL_FILE` and `TRANSFER_CHANNEL_FILE_V2V` (V2V, dropped) (`RepIntegration/PAL.DatabaseScripts.Vessel/Scripts/041_VALUE_PR_CHANNEL_SETTINGS.sql`, DATA-MSREP-OFFVSL).
- RepIntegration's export stops with `General Packet channel information not found. Exiting.` when the `GENERAL_PACKET` channel is missing, and the import with `General Notification Channel not found` when `GENERAL_NOTIFICATION` is missing (ISS-INTEG-002, FLW-PR-IMPORT).
- `REP.PR_PRIORITY_CHANNEL_FLOW_SETTINGS`: per channel, `FROM_SUB_ID` → `TO_SUB_ID` with `IS_EXPORT` and `ORDER`; read by `REP.PR_REP_GET_CHANNEL_FLOW_SETTINGS @IS_EXPORT` (`RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/015_PR_REP_GET_CHANNEL_FLOW_SETTINGS.sql#L4-L11`). No rows → `No channel flow settings found for export. Exiting.`
- `REP.PR_PRIORITY_QUEUE_SETTINGS`: `PR_CHANNEL_SETTINGS_ID`, `IS_SINGLE`, `QUEUE_COUNT`; seeded only for channel IDs 1 and 2 with `QUEUE_COUNT` 500 on the Office (`RepIntegration/PAL.DatabaseScripts.Office/Scripts/043_VALUES_PR_PRIORITY_QUEUE_SETTINGS.sql#L1-L8`); not seeded at all on the Vessel (script commented out).
- Total queue limit: CO_Parameters `PR_QUEUE_TOTAL_LIMIT` (`RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/022_PR_REP_GET_TOTAL_QUEUE_LIMIT.sql#L6`); per-channel limit: `PR_CHANNEL_SETTINGS.QUEUE_COUNT` (`RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/023_PR_REP_GET_CHANNEL_QUEUE_LIMIT.sql#L6-L8`). Both are read by RepQueueManage.

> Observation for review (Q16): `REP.PR_REP_READ_PENDING_EXPORT` joins pending records to `PR_PRIORITY_QUEUE_SETTINGS` on the channel ID (`RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/138_PR_REP_READ_PENDING_EXPORT.sql#L81`). A channel without a queue-settings row would have its records marked `WTG` but never returned, and they would be reset to `PND` every hour by `PR_REP_TRACK_EXCEED_CHECK`. It also takes only the first 500 pending records ordered by channel ID (`#L44-L58`). Whether either matters in practice needs confirming against a live database.

## Vessel settings — which vessels take part

`Common.PR_REP_Vessel_Settings` has one row per vessel with the Priority Replication switches and last packet counters. Keywords: vessel settings, IS_PRIORITY_ENABLED, EXPORT_TYPE, general export, IS_PARALLEL, LAST_OUT_PKT_CTR.

| Column | Meaning (from the script) |
|---|---|
| `IS_PRIORITY_ENABLED` | Vessel takes part in Priority Replication ("No PR enabled vessels found" when none) |
| `EXPORT_TYPE` | `0` = normal Priority, `1` = General Export (comment in the script) |
| `IS_PARALLEL` | Process this vessel's imports in parallel |
| `LAST_OUT_PKT_CTR`, `LAST_IN_PKT_CTR` | Last packet counters sent / received |
| `IS_AUTO_EXPORT`, `STATUS`, `REP_ENABLED_ON`, `LAST_PACKET_SENT_DATE` | Other per-vessel state |

Source: `RepIntegration/PAL.DatabaseScripts.Office/Scripts/044_TABLE_PR_REP_Vessel_Settings.sql#L4-L44`. RepDBLogW exposes `AzureDblog/UpdateExportType/{vesselObjectId}/{exportType}` to change `EXPORT_TYPE`; RepIntegration's `VerifyGenExportValidity` enables General Export on a vessel automatically (CMP-REPINTEGRATION). An older `REP.PR_REP_Vessel_Settings` table with extract/import timestamps also exists (`RepIntegration/PAL.DatabaseScripts.Office/Scripts/005_TABLE_PR_REP_Vessel_Settings.sql`); which one current code uses for what: the new queue code reads the `Common` table — the older table's use is Not determined from code.

Per-sender/receiver packet counters for extended (multi-client) communication live in `REP.PR_PACKET_COUNTER_SETTINGS` (`SOURCE_UNIQUE_ID`, `DESTINATION_UNIQUE_ID`, `LAST_OUT_PKT_CTR`, `LAST_IN_PKT_CTR`, `CHANNEL_ID`).

## Delivery method and transfer locations — how packets leave

The vessel's delivery method picks a root-folder parameter through `REP.PR_REP_TRANSFER_MASTER`. Keywords: delivery method, transfer type, PR_REP_TRANSFER_MASTER, REP_AZURE_ROOT, REP_OFF_ROOT, REP_REALM_ROOT, TRANSFER_LOCATION_CODE.

| `DELIVERY_ID` | Office root parameter (`REP_CODE`) | Vessel root parameter | Seed scripts |
|---|---|---|---|
| 0 | `REP_OFF_ROOT` | `PR_REP_ROOT` | `RepTransfer/PAL.DatabaseScripts.Office/Scripts/020_DATA_[REP].[PR_REP_TRANSFER_MASTER]_1.sql`, `RepTransfer/PAL.DatabaseScripts.Vessel/Scripts/005_DATA_[REP].[PR_REP_TRANSFER_MASTER]_1.sql` |
| 1 | `REP_OFF_ROOT` | `PR_REP_ROOT` | `RepTransfer/PAL.DatabaseScripts.Office/Scripts/021_DATA_[REP].[PR_REP_TRANSFER_MASTER]_2.sql`, `RepTransfer/PAL.DatabaseScripts.Vessel/Scripts/006_DATA_[REP].[PR_REP_TRANSFER_MASTER]_2.sql` |
| 2 | `REP_AZURE_ROOT` (SmartSync) | `REP_AZURE_ROOT` | `RepTransfer/PAL.DatabaseScripts.Office/Scripts/022_DATA_[REP].[PR_REP_TRANSFER_MASTER]_3.sql` |
| 3 | `REP_REALM_ROOT` — **not in use** (confirmed by the team) | same | `RepTransfer/PAL.DatabaseScripts.Office/Scripts/023_DATA_[REP].[PR_REP_TRANSFER_MASTER]_4.sql` |

- `REP.PR_GET_TRANSFER_DATA` operation `TRANSFER_LOCATION_CODE` looks up `REP_CODE` for the delivery ID and returns `Common.CO_Parameters.VALUE` where `NAME LIKE '%' + REP_CODE + '%'` (`RepTransfer/PAL.DatabaseScripts.Office/StoredProcedures/002_SP_[Rep].[PR_GET_TRANSFER_DATA].sql#L24-L28`). RepTransfer keeps the last row returned (`RepTransfer/MariApps.PAL.Rep.Transfer.DAL/TransferRepository.cs`, `GetTransferLocation`). The name match is loose on purpose; only one parameter carries each name, so this is not a troubleshooting concern (confirmed by the team, Q17 closed). What matters is that the parameter exists and holds the right folder — on the office `REP_OFF_ROOT`, on the vessel `PR_REP_ROOT` for methods 0/1 (DATA-MSREP-OFFVSL).
- Operation `TRANSFER_TYPE` returns the vessel's `DELIVERY_METHOD` from `REP.REP_VESSEL_INFRA`; vessel ID `-999` always returns `2` (`RepTransfer/PAL.DatabaseScripts.Office/StoredProcedures/002_SP_[Rep].[PR_GET_TRANSFER_DATA].sql#L11-L19`).
- RepTransfer's `MoveFile` handles delivery methods 0, 1 and 2 (`RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L71-L140`). Method 3 (`REP_REALM_ROOT`) has no branch because it is not in use (Q19 closed).
- `REP.REP_TYPE_TRANSFER_MEDIUM` also stores a `DELIVERY_METHOD` and `COMPRESSION_TYPE` per vessel and replication type (`RepIntegration/PAL.DatabaseScripts.Office/Scripts/096_rep_type_transfer_medium.sql`); how it relates to `REP_VESSEL_INFRA`: Not determined from code.

## Service IDs used in queue rows

`CURR_SERVICE_ID` / `NEXT_SERVICE_ID` in queue tables refer to `REP.PR_SERVICE_DETAILS`. Keywords: service id, CURR_SERVICE_ID, NEXT_SERVICE_ID, PR_SERVICE_DETAILS.

| IDs | Services |
|---|---|
| 101–113, 116–119 | Send side: 101 TRACK_SAVETRACKCHANGERECORD, 102 TRACK_SAVETRACKCHANGEFILE, 103 PRODATA_PROCESSDATA, 104 PACKET_CREATE, 105 COMPRESS_ZIP, 106 SPLIT_ZIP, 107 TRANSFER_CREATE, 108 SPLIT_EXT, 109 MEDIUM_SIZE_RES, 110 PACKET_CREATE_EXT, 111 TRANSFER_PACKET_EXT, 112 PCKT_COUNTER_EXT, 113 JSON_CREATE_EXT, 116 ACKN_SERVICE, 117 TRANSFER_QUEUE, 118 AES_CIPHER, 119 TRANSFER_PACKET_FOLDER |
| 201–205 | Receive side: 201 ACQUISITION_FILE, 202 MERGE_FILE, 203 DECOMPRESS_EXTRACT, 204 SAVEDATA_PROCESSDATA, 205 CHECK_OPERATION |
| 301–313 | Integration/transport: 301 INTEGRATION_TRACKQUEUE, 302/303 QUEUEMANAGE, 304/305 DBLOGWRITE, 306 MAIL_SENT, 307 AZURE_AZUREUPLOAD, 309 SBUS_SBUSUPDATE, 310 AZURE_RES_UPLOAD, 311–313 Sbus send update / V2V update / general notification |

Source: `RepIntegration/PAL.DatabaseScripts.Office/Scripts/040_VALUES_PR_SERVICE_DETAILS.sql`. RepAzureRes's `BasicSettings:ServiceId` (310) matches `AZURE_RES_UPLOAD`.

## Related

- DATA-MSREP-OVERVIEW, DATA-MSREP-STATUS, CMP-REPTRANSFER, CMP-REPINTEGRATION, ISS-INTEG-002, ISS-TRANSFER-001
