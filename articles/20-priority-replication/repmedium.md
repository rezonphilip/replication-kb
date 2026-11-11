---
doc_id: CMP-REPMEDIUM
type: component
mechanism: [priority-replication]
group: pr-send
runs_on: [office, vessel]
components: [RepMedium]
log_files: [Log_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepMedium — returns size limits per medium

RepMedium answers one question: how large may a transfer be for this vessel and medium (`GetSizeRestriction`). RepIntegration calls it before splitting for transfer.

> **V2V (vessel-to-vessel) is a dropped feature.** The V2V routes, procedures and message types mentioned in this article still exist in the code and database but are not in use; do not troubleshoot them. See DATA-MSREP-OFFVSL.

## Role in replication

RepMedium is a Priority Replication send-side step with no timer of its own: it runs only when called over HTTP (no hosted background service found in the project). Keywords: RepMedium, medium, priority replication, send side, returns size limits per medium.

- Uses `GET_V2V_TRANSFER_MED_SIZE_RESTRICTION` for vessel-to-vessel.

## API routes

Controller routes and their source lines. Keywords: RepMedium routes, API, TestService.

| Route | Source |
|---|---|
| `Medium` | `RepMedium/MariApps.PAL.Rep.Medium.Service/Controllers/MediumController.cs#L16` |
| `GetSizeRestriction` | `RepMedium/MariApps.PAL.Rep.Medium.Service/Controllers/MediumController.cs#L30` |
| `TestService` | `RepMedium/MariApps.PAL.Rep.Medium.Service/Controllers/MediumController.cs#L40` |
| `GetVersion` | `RepMedium/MariApps.PAL.Rep.Medium.Service/Controllers/MediumController.cs#L48` |

## Database and parameters

Stored procedures and CO_Parameters keys this service uses (names only). Keywords: RepMedium stored procedure, CO_Parameters, REP schema.

- `PR_REP_MAX_ATTACHMENT_SIZE` — `RepMedium/MariApps.PAL.Rep.Medium.DAL/MediumRepository.cs#L106`
- `[REP].[GET_V2V_TRANSFER_MED_SIZE_RESTRICTION]` — `RepMedium/MariApps.PAL.Rep.Medium.DAL/MediumRepository.cs#L70`
- `[REP].[PR_GET_PARAM_DATA]` — `RepMedium/MariApps.PAL.Rep.Medium.DAL/MediumRepository.cs#L29`
- `[REP].[PR_TRACKCHANGE_TYP]` — `RepMedium/MariApps.PAL.Rep.Medium.DAL/MediumRepository.cs#L74`

Parameters: `PR_REP_MAX_ATTACHMENT_SIZE`.

## Logs and what to look for

Log: `Logs/Log_.txt`. Error-type messages found in code (first 10; full list in `inventory/ms-rep-logs.md` → RepMedium). Keywords: Log_.txt, RepMedium error, failed.

| Message (template) | Source |
|---|---|
| none found | |

What each message means in practice: Not determined from code beyond the text itself — to be filled from incident history.

## Related

- PLT-MSREP-OVERVIEW, CMP-REPINTEGRATION, FLW-PR-EXPORT
