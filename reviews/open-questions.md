# Open questions — MS-REP pilot (2026-11-11)

Questions the code could not answer. A reviewer answers here, then the linked articles are updated and moved to `needs-review`/`approved`.

| # | Question | Affects | Answer |
|---|---|---|---|
| Q1 | What do delivery methods `0` and `1` (`REP.REP_VESSEL_INFRA.DELIVERY_METHOD`) mean? Only `2` is clearly Azure/SmartSync (`OUT/PR/OUTBOX`). | CMP-REPTRANSFER, ISS-TRANSFER-001 || Partly answered from DB scripts (2026-11-11): 0 and 1 both map to `REP_OFF_ROOT`, 2 to `REP_AZURE_ROOT`, 3 to `REP_REALM_ROOT` (`REP.PR_REP_TRANSFER_MASTER`). Still open: what distinguishes 0 from 1. |
| Q2 | Which `TRANSFER_LOCATION_CODE` table/parameter holds the base folder per delivery method? | CMP-REPTRANSFER || Answered: `REP.PR_GET_TRANSFER_DATA` `TRANSFER_LOCATION_CODE` → `PR_REP_TRANSFER_MASTER.REP_CODE` → CO_Parameters value with that name (DATA-MSREP-SETTINGS). |
| Q3 | RepDBLogW is described as Priority Replication core, but in code it is also the settings/credentials source for RepSbus, RepAzure and RepAzureRes (55 routes in `DbServiceSbus`). Should it be documented as a shared component (transport + PR)? | CMP-REPDBLOGW, overview grouping | |
| Q4 | Column layout of `REP_SERVICE_BUS_MASTER` / `REP_SERVICE_BUS_TRANSACTION_SETTINGS` (SQL scripts were not in the staged snapshot). Needed for a queue-name presence script. | ISS-SBUS-002, catalog || Answered: queue names are in `REP.REP_PR_SUBSCRIBER_LIST`; the connection string is in `REP.REP_SERVICEBUS_CREDENTIALS`; `REP_SERVICE_BUS_TRANSACTION_SETTINGS` has `SERVICE_BUS_URL`, `LOCATION`, `VESSEL_OBJECT_ID`. Presence script updated. |
| Q5 | Does a missing packet (counter gap) block later packets from being applied on the receiver, or are later packets applied and the gap re-requested? | FLW-PR-IMPORT || Answered: a dependent packet waits (`SEQ_WAITING` → `AWAITING`); the vessel-wide check is commented out (DATA-MSREP-RESEND). See Q18. |
| Q6 | Which tables hold the General Packet channel, channel flow settings, working directory, PR-enabled and General-Export flags per vessel? | ISS-INTEG-002, FLW-PR-EXPORT || Mostly answered: channels `REP.PR_CHANNEL_SETTINGS`, flows `REP.PR_PRIORITY_CHANNEL_FLOW_SETTINGS`, vessel flags `Common.PR_REP_Vessel_Settings` (`IS_PRIORITY_ENABLED`, `EXPORT_TYPE`). Working directory source still open. |
| Q7 | Are both export paths live — chained `InitiateExport` and queue-based `InitiateExportQueue` — or is one legacy? Which one does a given site use? | FLW-PR-EXPORT, CMP-REPINTEGRATION | |
| Q8 | Which iRep flows call RepTransfer and RepDBLogW, and with which routes? (Needed for `30-irep` once the iRep repos are processed.) | 30-irep | |
| Q9 | Known incident: `JsonReaderException` with `<` in RepAzure `IntiateDownloadQueue`. What returned HTML (proxy, storage error page, service URL)? | ISS-AZURE-001 | |
| Q10 | Version labels: how do we map an installed MS-REP build to `applies_to_versions` (assembly version from `GetVersion`/`Version` routes?) | all articles | |
| Q11 | Two vessel-settings tables exist: `REP.PR_REP_Vessel_Settings` (older, extract/import timestamps) and `Common.PR_REP_Vessel_Settings` (new flags). Which code paths still use the older one? | DATA-MSREP-SETTINGS | |
| Q12 | Why is SQL Server change tracking enabled on the settings tables (so they replicate themselves?) | DATA-MSREP-OVERVIEW | |
| Q13 | Full Office vs Vessel script diff — several tables/procedures differ in size; which differences matter for troubleshooting? | DATA-MSREP-OVERVIEW | |
| Q14 | 17 procedures called from C# are not created by these scripts (e.g. `REP.READ_COMMON_PARAMS_VALUE`, `REP.REP_PR_READ_QUEUE_NAME`, `REP.UPDATE_PR_COUNTER_SETTINGS`). Where are they deployed? | INV-MSREP-DB | |
| Q15 | Names of numeric status codes for `REP_TRANSFER_QUEUE` (1,2,3,5), `REP_AZURE_RES_UPLOAD`, `REP_Downloads` (1,2,3,5,7,10,12,13,14), the numeric values of `ImportQueueStatus`, and what `COMM_TYPE = 5` means (not in `REP.COMMUNICATION_TYPE`). The enum classes were not in the snapshot. | DATA-MSREP-STATUS | |
| Q16 | `PR_REP_READ_PENDING_EXPORT` inner-joins `PR_PRIORITY_QUEUE_SETTINGS` (seeded only for channels 1 and 2) and takes the first 500 records ordered by channel. Can a channel without a queue-settings row, or a large backlog in a low-ID channel, starve exports? | DATA-MSREP-SETTINGS | |
| Q17 | `TRANSFER_LOCATION_CODE` uses `NAME LIKE '%' + REP_CODE + '%'` and RepTransfer keeps the last row. Can several parameters match (e.g. other names containing `REP_OFF_ROOT`)? | DATA-MSREP-SETTINGS, ISS-TRANSFER-001 | |
| Q18 | `REP.PR_VALIDATE_VSL_IMPORTQ` (vessel-wide wait while any packet is missing) is commented out in `ImportProcessor`, and as written it does not filter the queue by vessel. Is it intended to be re-enabled? | DATA-MSREP-RESEND | |
| Q19 | Delivery method 3 (`REP_REALM_ROOT`) exists in the database but RepTransfer `MoveFile` handles only 0, 1, 2. Where is method 3 handled? | CMP-REPTRANSFER | |
