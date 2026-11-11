---
doc_id: CMP-REPPRODATA
type: component
mechanism: [priority-replication]
group: pr-send
runs_on: [office, vessel]
components: [RepProData]
log_files: [ProDataLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepProData — reads pending changed records for export

RepProData is the first step of a Priority Replication export: it reads the records that changed since the last packet and produces the data set for a packet. RepIntegration calls `ProData/ProcessData`. If it fails or returns nothing, no packet is created and the export simply looks idle.

## Role in replication

RepProData is a Priority Replication send-side step with no timer of its own: it runs only when called over HTTP (no hosted background service found in the project). Keywords: RepProData, prodata, priority replication, send side, reads pending changed records for export.

- Uses `[REP].[PR_REP_GETPENDING_RECORDS]`, `[REP].[PR_REP_GET_EXPORT_QUERY]`, `[REP].[PR_REP_SAVE_PROCESS_DATA]` and `[REP].[PR_REP_OUT_FILE_DT]` (see table below for sources).
- Which tables are exported, and with what query, is configured per table setting in the database (export query procedure). Exact table list: Not determined from code.

## API routes

Controller routes and their source lines. Keywords: RepProData routes, API, TestService.

| Route | Source |
|---|---|
| `ProData` | `RepProData/MariApps.PAL.Rep.ProData.Service/Controllers/ProDataController.cs#L18` |
| `ProcessData` | `RepProData/MariApps.PAL.Rep.ProData.Service/Controllers/ProDataController.cs#L38` |
| `TestService` | `RepProData/MariApps.PAL.Rep.ProData.Service/Controllers/ProDataController.cs#L76` |
| `GetVersion` | `RepProData/MariApps.PAL.Rep.ProData.Service/Controllers/ProDataController.cs#L84` |

## Database and parameters

Stored procedures and CO_Parameters keys this service uses (names only). Keywords: RepProData stored procedure, CO_Parameters, REP schema.

- `PR_REP_ROOT` — `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ProDataBL.cs#L105`
- `[REP].[PR_REP_GETPENDING_RECORDS]` — `RepProData/MariApps.PAL.Rep.ProData.DAL/ProDataRepository.cs#L88`
- `[REP].[PR_REP_GET_EXPORT_QUERY]` — `RepProData/MariApps.PAL.Rep.ProData.DAL/ProDataRepository.cs#L298`
- `[REP].[PR_REP_GET_FILE_COUNTER]` — `RepProData/MariApps.PAL.Rep.ProData.DAL/ProDataRepository.cs#L54`
- `[REP].[PR_REP_GET_SETTINGS]` — `RepProData/MariApps.PAL.Rep.ProData.DAL/ProDataRepository.cs#L27`
- `[REP].[PR_REP_OUT_FILE_DT]` — `RepProData/MariApps.PAL.Rep.ProData.DAL/ProDataRepository.cs#L344`
- `[REP].[PR_REP_SAVE_PROCESS_DATA]` — `RepProData/MariApps.PAL.Rep.ProData.DAL/ProDataRepository.cs#L340`
- `[REP].[PR_REP_UPDATE_RECORDS_STATUS]` — `RepProData/MariApps.PAL.Rep.ProData.DAL/ProDataRepository.cs#L267`
- `[REP].[PR_TRACKCHANGE_VESSEL_TYP]` — `RepProData/MariApps.PAL.Rep.ProData.DAL/ProDataRepository.cs#L92`

Parameters: `PR_REP_ROOT`.

## Logs and what to look for

Log: `Logs/ProDataLog_.txt`. Error-type messages found in code (first 10; full list in `inventory/ms-rep-logs.md` → RepProData). Keywords: ProDataLog_.txt, RepProData error, failed.

| Message (template) | Source |
|---|---|
| none found | |

What each message means in practice: Not determined from code beyond the text itself — to be filled from incident history.

## Related

- PLT-MSREP-OVERVIEW, CMP-REPINTEGRATION, FLW-PR-EXPORT
