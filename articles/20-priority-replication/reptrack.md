---
doc_id: CMP-REPTRACK
type: component
mechanism: [priority-replication]
group: pr-send
runs_on: [office, vessel]
components: [RepTrack]
log_files: [TrackServiceLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepTrack — tracks change records and status

RepTrack stores and updates track-change records — the list of changes waiting to be exported — and their status per vessel (`SaveTrackChangeRecord`, `SaveTrackChangeFile`, `UpdateTrackStatus`, `UpdateTrackVesselStatus`, `UpdateTrackUniqueIdStatus`). The queue-based export in RepIntegration starts from these records.

> **V2V (vessel-to-vessel) is a dropped feature.** The V2V routes, procedures and message types mentioned in this article still exist in the code and database but are not in use; do not troubleshoot them. See DATA-MSREP-OFFVSL.

## Role in replication

RepTrack is a Priority Replication send-side step with no timer of its own: it runs only when called over HTTP (no hosted background service found in the project). Keywords: RepTrack, track, priority replication, send side, tracks change records and status.

- Procedures: `SAVE_TRACK_CHANGE_RECORD`, `SAVE_TRACK_CHANGE_FILE` (and `_V2V` variants), `UPDATE_TRACK_CHANGE_STATUS`.
- iRep transfer routes in RepIntegration (`IntegrateTrackRecord`, `IntegrateTrackFile`) also feed track records.

## API routes

Controller routes and their source lines. Keywords: RepTrack routes, API, TestService.

| Route | Source |
|---|---|
| `Track` | `RepTrack/MariApps.PAL.Rep.Track.Service/Controllers/TrackController.cs#L13` |
| `SaveTrackChangeRecord` | `RepTrack/MariApps.PAL.Rep.Track.Service/Controllers/TrackController.cs#L40` |
| `SaveTrackChangeFile` | `RepTrack/MariApps.PAL.Rep.Track.Service/Controllers/TrackController.cs#L70` |
| `UpdateTrackStatus` | `RepTrack/MariApps.PAL.Rep.Track.Service/Controllers/TrackController.cs#L98` |
| `UpdateTrackVesselStatus` | `RepTrack/MariApps.PAL.Rep.Track.Service/Controllers/TrackController.cs#L106` |
| `UpdateTrackUniqueIdStatus` | `RepTrack/MariApps.PAL.Rep.Track.Service/Controllers/TrackController.cs#L114` |
| `TestService` | `RepTrack/MariApps.PAL.Rep.Track.Service/Controllers/TrackController.cs#L122` |
| `GetVersion` | `RepTrack/MariApps.PAL.Rep.Track.Service/Controllers/TrackController.cs#L130` |

## Database and parameters

Stored procedures and CO_Parameters keys this service uses (names only). Keywords: RepTrack stored procedure, CO_Parameters, REP schema.

- `PR_TRACKCHANGE_RECORDS_ID` — `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L177`
- `REP.PR_GET_VESSEL_CODE` — `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L103`
- `[REP].[PR_GET_PARAM_DATA]` — `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L30`
- `[REP].[PR_TRACKCHANGE_NEW_TYP]` — `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L152`
- `[REP].[PR_TRACKCHANGE_TYP]` — `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L295`
- `[REP].[REP_V2V_GET_ACTIVE_VESSELS]` — `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L417`
- `[REP].[SAVE_TRACK_CHANGE_FILE]` — `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L148`
- `[REP].[SAVE_TRACK_CHANGE_RECORD]` — `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L291`
- `[REP].[SAVE_TRACK_CHANGE_RECORD_V2V]` — `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L614`
- `[REP].[UPDATE_TRACK_CHANGE_STATUS]` — `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L705`
- `[Rep].[PR_TRACKCHANGE_NEW_TYP_V2V]` — `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L462`
- `[Rep].[SAVE_TRACK_CHANGE_FILE_V2V]` — `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L458`

Parameters: `PR_TRACKCHANGE_RECORDS_ID`.

## Logs and what to look for

Log: `Logs/TrackServiceLog_.txt`. Error-type messages found in code (first 10; full list in `inventory/ms-rep-logs.md` → RepTrack). Keywords: TrackServiceLog_.txt, RepTrack error, failed.

| Message (template) | Source |
|---|---|
| none found | |

What each message means in practice: Not determined from code beyond the text itself — to be filled from incident history.

## Related

- PLT-MSREP-OVERVIEW, CMP-REPINTEGRATION, FLW-PR-EXPORT
