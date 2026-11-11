---
doc_id: CMP-REPPACKETCREATION
type: component
mechanism: [priority-replication]
group: pr-send
runs_on: [office, vessel]
components: [RepPacketCreation]
log_files: [PacketCreatLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepPacketCreation — builds packet files with counters

RepPacketCreation turns prepared data into packet files and assigns the packet counter that the receiver uses to detect gaps. RepIntegration calls `Packet/Create` (and `GeneratePacketExt` / `PacketGen` for extended and queue-based exports). Counter problems here cause 'missing packet' symptoms on the other side.

## Role in replication

RepPacketCreation is a Priority Replication send-side step with no timer of its own: it runs only when called over HTTP (no hosted background service found in the project). Keywords: RepPacketCreation, packetcreation, priority replication, send side, builds packet files with counters.

- Packet counters come from `[REP].[PR_REP_GET_PACKET_COUNTER]` and the counter settings procedures (`GET_PR_COUNTER_SETTINGS` / `UPDATE_PR_COUNTER_SETTINGS`).
- `PR_REP_MAX_ATTACHMENT_SIZE` limits attachment size per packet.
- Before compressing, RepIntegration asks RepDBLogW `ReadCompressionType` for the compression type.

## API routes

Controller routes and their source lines. Keywords: RepPacketCreation routes, API, TestService.

| Route | Source |
|---|---|
| `Packet` | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L15` |
| `Create` | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L55` |
| `GeneratePacketExt` | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L103` |
| `PacketGen` | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L142` |
| `TestExtraction` | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L163` |
| `TestService` | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L173` |
| `GetVersion` | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L181` |

## Database and parameters

Stored procedures and CO_Parameters keys this service uses (names only). Keywords: RepPacketCreation stored procedure, CO_Parameters, REP schema.

- `PR_PACKET_INFO_` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L115`
- `PR_PARAM` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L57`
- `PR_PCK_` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L108`
- `PR_REP_MAX_ATTACHMENT_SIZE` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L57`
- `PR_REP_ROOT` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L47`
- `REP.PR_GET_PACKET_DATA` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L218`
- `REP.PR_GET_TRANSFER_DATA` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L302`
- `REP.PR_GET_VESSEL_CODE` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L66`
- `REP.PR_REP_GET_PACKET_COUNTER` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/SqlNamedQueries.cs#L12`
- `REP.PR_REP_OUT_FILE_DT` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/SqlNamedQueries.cs#L7`
- `REP.PR_REP_SAVE_PACKET_DATA` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/SqlNamedQueries.cs#L11`
- `REP.PR_UPDATE_VESSEL_SETTINGS` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/SqlNamedQueries.cs#L13`
- `REP_CODE` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L69`
- `[REP].[GET_PR_COUNTER_SETTINGS]` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L402`
- `[REP].[PR_GET_PARAM_DATA]` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L33`
- `[REP].[PR_REP_GET_PACKET_COUNTER]` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L109`
- `[REP].[PR_REP_OUT_FILE_DT]` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L195`
- `[REP].[PR_REP_SAVE_PACKET_DATA]` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L190`
- `[REP].[PR_UPDATE_VESSEL_SETTINGS]` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L155`
- `[REP].[SAVE_EXT_PACKET_DETAILS]` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L452`
- `[REP].[SAVE_SOURCE_SUB_DETAILS]` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L477`
- `[REP].[UPDATE_PR_COUNTER_SETTINGS]` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L428`
- `[Rep].[REP_PR_EXT_PACKET_TYP]` — `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L456`

Parameters: `PR_PACKET_INFO_`, `PR_PARAM`, `PR_PCK_`, `PR_REP_MAX_ATTACHMENT_SIZE`, `PR_REP_ROOT`, `REP_CODE`.

## Logs and what to look for

Log: `Logs/PacketCreatLog_.txt`. Error-type messages found in code (first 10; full list in `inventory/ms-rep-logs.md` → RepPacketCreation). Keywords: PacketCreatLog_.txt, RepPacketCreation error, failed.

| Message (template) | Source |
|---|---|
| {MethodName} \| Request is null | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L205` |
| {MethodName} \| BasePath is null or empty | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L211` |
| {MethodName} \| VesselGroups is null or empty | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L223` |
| {MethodName} \| One or more VesselGroups have invalid VesselObjectId or VesselPacketDirectory | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L229` |
| {MethodName} \| One or more VesselGroups have null or empty TrackRecordDetails | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L241` |
| {MethodName} \| Error validating packet generation request | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L249` |
| Invalid path | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/FileChunkWriterStream.cs#L14` |
| Rep code value gotten is null  or empty | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L325` |
| Packet Name value gotten is null or empty | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L343` |
| {MethodName} - Error occurred while extracting zip file from {ZipPath} to {ExtractPath}. Message: {Message} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L52` |

What each message means in practice: Not determined from code beyond the text itself — to be filled from incident history.

## Related

- PLT-MSREP-OVERVIEW, CMP-REPINTEGRATION, FLW-PR-EXPORT
