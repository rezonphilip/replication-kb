---
doc_id: CMP-REPSAVEDATA
type: component
mechanism: [priority-replication]
group: pr-receive
runs_on: [office, vessel]
components: [RepSaveData]
log_files: [SaveDataLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepSaveData — applies replicated data

RepSaveData applies the replicated records to the local database (`SaveData/ProcessData`), and also saves acknowledgements and subscriber lists. Data errors (constraint violations, schema differences) surface here.

## Role in replication

RepSaveData is a Priority Replication receive-side step with no timer of its own: it runs only when called over HTTP (no hosted background service found in the project). Keywords: RepSaveData, savedata, priority replication, receive side, applies replicated data.

- Procedures: `PR_REP_SAVE_DATA_OPERATION`, `PR_REP_GET_IMPORT_QUERY`, `PR_REP_REPLICATIONDATA`, `PR_REP_UPDATE_STATUS`.

## API routes

Controller routes and their source lines. Keywords: RepSaveData routes, API, TestService.

| Route | Source |
|---|---|
| `SaveData` | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/Controllers/SaveDataController.cs#L19` |
| `ProcessData` | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/Controllers/SaveDataController.cs#L35` |
| `SaveAckn` | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/Controllers/SaveDataController.cs#L62` |
| `SaveSubscriberList` | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/Controllers/SaveDataController.cs#L78` |
| `TestService` | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/Controllers/SaveDataController.cs#L155` |
| `GetVersion` | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/Controllers/SaveDataController.cs#L163` |

## Database and parameters

Stored procedures and CO_Parameters keys this service uses (names only). Keywords: RepSaveData stored procedure, CO_Parameters, REP schema.

- `[REP].[PR_REP_GET_IMPORT_QUERY]` — `RepSaveData/MariApps.PAL.Rep.SaveData.DAL/SaveDataRepository.cs#L148`
- `[REP].[PR_REP_IMPORT_SUBSCRIBER_LIST]` — `RepSaveData/MariApps.PAL.Rep.SaveData.DAL/SaveDataRepository.cs#L261`
- `[REP].[PR_REP_IMPORT_SUBSCRIBER_LIST_DT_TYP]` — `RepSaveData/MariApps.PAL.Rep.SaveData.DAL/SaveDataRepository.cs#L267`
- `[REP].[PR_REP_IMPORT_SUBSCRIBER_LIST_TYP]` — `RepSaveData/MariApps.PAL.Rep.SaveData.DAL/SaveDataRepository.cs#L265`
- `[REP].[PR_REP_REPLICATIONDATA]` — `RepSaveData/MariApps.PAL.Rep.SaveData.DAL/SaveDataRepository.cs#L159`
- `[REP].[PR_REP_SAVE_DATA_OPERATION]` — `RepSaveData/MariApps.PAL.Rep.SaveData.DAL/SaveDataRepository.cs#L24`
- `[REP].[PR_REP_UPDATE_STATUS]` — `RepSaveData/MariApps.PAL.Rep.SaveData.DAL/SaveDataRepository.cs#L163`
- `[REP].[REP_SAVE_NOTIFICATION_LOG]` — `RepSaveData/MariApps.PAL.Rep.SaveData.DAL/SaveDataRepository.cs#L183`

Parameters: none found.

## Logs and what to look for

Log: `Logs/SaveDataLog_.txt`. Error-type messages found in code (first 10; full list in `inventory/ms-rep-logs.md` → RepSaveData). Keywords: SaveDataLog_.txt, RepSaveData error, failed.

| Message (template) | Source |
|---|---|
| none found | |

What each message means in practice: Not determined from code beyond the text itself — to be filled from incident history.

## Related

- PLT-MSREP-OVERVIEW, CMP-REPINTEGRATION, FLW-PR-IMPORT
