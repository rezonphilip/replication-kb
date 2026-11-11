---
doc_id: CMP-REPSPLIT
type: component
mechanism: [priority-replication]
group: pr-send
runs_on: [office, vessel]
components: [RepSplit]
log_files: [SplitServiceLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepSplit — splits zips to medium size

RepSplit cuts a zipped packet into parts no larger than the allowed size so it fits the transfer medium (`Split/Zip`, `SplitExt`). RepFileMerge joins the parts on the receiving side. Wrong size settings cause either oversized transfers or very many small parts.

## Role in replication

RepSplit is a Priority Replication send-side step with no timer of its own: it runs only when called over HTTP (no hosted background service found in the project). Keywords: RepSplit, split, priority replication, send side, splits zips to medium size.

- Split size: `PR_REP_SPLIT_SIZE`; part details saved with `[REP].[PR_REP_SAVE_SPLIT_DATA]`.
- For transfer, RepIntegration also asks RepMedium `GetSizeRestriction` for the medium's size limit.

## API routes

Controller routes and their source lines. Keywords: RepSplit routes, API, TestService.

| Route | Source |
|---|---|
| `Split` | `RepSplit/MariApps.PAL.Rep.Split.Service/Controllers/SplitController.cs#L16` |
| `Zip` | `RepSplit/MariApps.PAL.Rep.Split.Service/Controllers/SplitController.cs#L34` |
| `SplitExt` | `RepSplit/MariApps.PAL.Rep.Split.Service/Controllers/SplitController.cs#L68` |
| `TestService` | `RepSplit/MariApps.PAL.Rep.Split.Service/Controllers/SplitController.cs#L96` |
| `GetVersion` | `RepSplit/MariApps.PAL.Rep.Split.Service/Controllers/SplitController.cs#L104` |

## Database and parameters

Stored procedures and CO_Parameters keys this service uses (names only). Keywords: RepSplit stored procedure, CO_Parameters, REP schema.

- `PR_PARAM` — `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L36`
- `PR_REP_ROOT` — `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L36`
- `PR_REP_SPLIT_SIZE` — `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L54`
- `REP.PR_GET_PARAM_DATA` — `RepSplit/MariApps.PAL.Rep.Split.DAL/SplitRepository.cs#L24`
- `REP.PR_REP_SAVE_SPLIT_DATA` — `RepSplit/MariApps.PAL.Rep.Split.DAL/SplitRepository.cs#L102`
- `REP.PR_REP_UPDATE_PACKET_DATA` — `RepSplit/MariApps.PAL.Rep.Split.DAL/SplitRepository.cs#L52`

Parameters: `PR_PARAM`, `PR_REP_ROOT`, `PR_REP_SPLIT_SIZE`.

## Logs and what to look for

Log: `Logs/SplitServiceLog_.txt`. Error-type messages found in code (first 10; full list in `inventory/ms-rep-logs.md` → RepSplit). Keywords: SplitServiceLog_.txt, RepSplit error, failed.

| Message (template) | Source |
|---|---|
| The Directory  value of OutzipVslPathMain gotten is null or empty | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L42` |

What each message means in practice: Not determined from code beyond the text itself — to be filled from incident history.

## Related

- PLT-MSREP-OVERVIEW, CMP-REPINTEGRATION, FLW-PR-EXPORT
