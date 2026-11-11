---
doc_id: CMP-REPACKN
type: component
mechanism: [priority-replication]
group: pr-receive
runs_on: [office, vessel]
components: [RepAckn]
log_files: [AcknLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepAckn — sends acknowledgements

RepAckn builds and sends acknowledgements for received packets (`SendAckn`, `Destination-Handler`, `Response`) so the sender can stop resending. Missing acknowledgements make the sender resend after `ResendTimeInH`.

> **V2V (vessel-to-vessel) is a dropped feature.** The V2V routes, procedures and message types mentioned in this article still exist in the code and database but are not in use; do not troubleshoot them. See DATA-MSREP-OFFVSL.

## Role in replication

RepAckn is a Priority Replication receive-side step with no timer of its own: it runs only when called over HTTP (no hosted background service found in the project). Keywords: RepAckn, ackn, priority replication, receive side, sends acknowledgements.

- Bulk insert of acks: `REP_ACKN_INSERT_BULK`; counter: `PR_PACKET_COUNTER`.
- Logs `Base URL or API URL is empty for Table Settings Id ...` when the destination address is not configured (`RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L104`).

## API routes

Controller routes and their source lines. Keywords: RepAckn routes, API, TestService.

| Route | Source |
|---|---|
| `Ackn` | `RepAckn/MariApps.PAL.Rep.Ackn.Service/Controllers/AcknController.cs#L16` |
| `SendAckn` | `RepAckn/MariApps.PAL.Rep.Ackn.Service/Controllers/AcknController.cs#L34` |
| `Destination-Handler` | `RepAckn/MariApps.PAL.Rep.Ackn.Service/Controllers/AcknController.cs#L73` |
| `Response` | `RepAckn/MariApps.PAL.Rep.Ackn.Service/Controllers/AcknController.cs#L100` |
| `TestService` | `RepAckn/MariApps.PAL.Rep.Ackn.Service/Controllers/AcknController.cs#L135` |
| `Version` | `RepAckn/MariApps.PAL.Rep.Ackn.Service/Controllers/AcknController.cs#L144` |

## Database and parameters

Stored procedures and CO_Parameters keys this service uses (names only). Keywords: RepAckn stored procedure, CO_Parameters, REP schema.

- `PR_PACKET_COUNTER` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/AcknRepository.cs#L92`
- `REP.REP_ACKN` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/AcknRepository.cs#L347`
- `REP.REP_ACKN_EXT_RECORD` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/AcknRepository.cs#L409`
- `REP_LOG` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/AcknRepository.cs#L268`
- `[REP].[PR_GET_PARAM_DATA]` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/SqlNamedQueries.cs#L27`
- `[REP].[PR_REP_GET_ALL_SETTINGS]` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/SqlNamedQueries.cs#L11`
- `[REP].[PR_REP_GET_ALL_TABLESETTINGS]` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/SqlNamedQueries.cs#L10`
- `[REP].[PR_SAVE_ERROR_LOG]` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/SqlNamedQueries.cs#L21`
- `[REP].[PR_TRACKCHANGE_NEW_TYP_V2V]` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/SqlNamedQueries.cs#L33`
- `[REP].[PR_TRACKCHANGE_TYP]` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/SqlNamedQueries.cs#L32`
- `[REP].[READ_COMMON_PARAMS_VALUE]` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/SqlNamedQueries.cs#L14`
- `[REP].[REP_ACKN_INSERT_BULK]` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/SqlNamedQueries.cs#L18`
- `[REP].[SAVE_TRACK_CHANGE_RECORD]` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/SqlNamedQueries.cs#L24`
- `[REP].[SAVE_TRACK_CHANGE_RECORD_V2V]` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/SqlNamedQueries.cs#L25`
- `[Rep].[PR_GET_ACKN_SETTINGS]` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/SqlNamedQueries.cs#L17`
- `[Rep].[PR_GET_ACKN_SETTINGS_TYP]` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/SqlNamedQueries.cs#L30`
- `[Rep].[PR_SAVE_ACKN_DATA_TYP]` — `RepAckn/MariApps.PAL.Rep.Ackn.DAL/SqlNamedQueries.cs#L31`

Parameters: `PR_PACKET_COUNTER`, `REP_LOG`.

## Logs and what to look for

Log: `Logs/AcknLog_.txt`. Error-type messages found in code (first 10; full list in `inventory/ms-rep-logs.md` → RepAckn). Keywords: AcknLog_.txt, RepAckn error, failed.

| Message (template) | Source |
|---|---|
| {MethodName}\| Base URL or API URL is empty for Table Settings Id {TableSetttingsId} for Packet Counter {PacketCounter} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L104` |
| {MethodName}\| Acknowledgement process failed for {FileLocation} with error {ErrorMessage} - {HttpStatusCode} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L183` |
| {MethodName}\| All files failed for TableSettings Id {TableSetttingsId} for Packet Counter {PacketCounter} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L216` |
| {MethodName}\| Exception occurred while processing Acknowledgement for TableSettings Id {TableSetttingsId} for Packet Counter {PacketCounter} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L259` |
| {MethodName}\| Input is null | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L123` |
| {MethodName}\| SplitFiles is null or empty | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L183` |
| {MethodName}\| FileLocation is null or file does not exist | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L193` |
| {MethodName}\| Invalid Request | `RepAckn/MariApps.PAL.Rep.Ackn.Service/Controllers/AcknController.cs#L84` |
| {MethodName}\| External invoke parameters cannot be null | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L77` |
| {MethodName}\| POST request failed. Status: {StatusCode}, Response: {Response} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L127` |

What each message means in practice: Not determined from code beyond the text itself — to be filled from incident history.

## Related

- PLT-MSREP-OVERVIEW, CMP-REPINTEGRATION, FLW-PR-IMPORT
