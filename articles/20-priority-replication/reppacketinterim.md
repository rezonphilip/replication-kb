---
doc_id: CMP-REPPACKETINTERIM
type: component
mechanism: [priority-replication]
group: pr-send
runs_on: [office, vessel]
components: [RepPacketInterim]
log_files: [PacketInterimLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepPacketInterim — records packet counters and JSON

RepPacketInterim keeps interim packet bookkeeping during transfer: it reads the packet counter, writes the packet's JSON description and updates packet status (`ReadPckCounter`, `CreateJsonFile`, `UpdatePacketStatus`, `UpdateExtPacketDataBulk`). It is called by RepIntegration inside the transfer step.

## Role in replication

RepPacketInterim is a Priority Replication send-side step with no timer of its own: it runs only when called over HTTP (no hosted background service found in the project). Keywords: RepPacketInterim, packetinterim, priority replication, send side, records packet counters and JSON.


## API routes

Controller routes and their source lines. Keywords: RepPacketInterim routes, API, TestService.

| Route | Source |
|---|---|
| `PacketInterim` | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.Service/Controllers/PacketInterimController.cs#L17` |
| `ReadPckCounter` | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.Service/Controllers/PacketInterimController.cs#L33` |
| `CreateJsonFile` | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.Service/Controllers/PacketInterimController.cs#L52` |
| `UpdatePacketStatus` | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.Service/Controllers/PacketInterimController.cs#L71` |
| `UpdateExtPacketDataBulk` | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.Service/Controllers/PacketInterimController.cs#L90` |
| `TestService` | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.Service/Controllers/PacketInterimController.cs#L99` |
| `GetVersion` | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.Service/Controllers/PacketInterimController.cs#L107` |

## Database and parameters

Stored procedures and CO_Parameters keys this service uses (names only). Keywords: RepPacketInterim stored procedure, CO_Parameters, REP schema.

- `REP.PR_GET_PARAM_DATA` — `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.DAL/PacketInterimRepository.cs#L28`
- `[REP].[GET_V2V_PACKET_COUNTER]` — `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.DAL/PacketInterimRepository.cs#L57`
- `[REP].[PR_REP_UPDATE_PACKET_DATA_BULK]` — `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.DAL/PacketInterimRepository.cs#L118`
- `[REP].[SAVE_V2V_OUT_PACKET_HD]` — `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.DAL/PacketInterimRepository.cs#L89`
- `[REP].[UPDATE_EXT_PACKET_DATA_BULK]` — `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.DAL/PacketInterimRepository.cs#L142`

Parameters: none found.

## Logs and what to look for

Log: `Logs/PacketInterimLog_.txt`. Error-type messages found in code (first 10; full list in `inventory/ms-rep-logs.md` → RepPacketInterim). Keywords: PacketInterimLog_.txt, RepPacketInterim error, failed.

| Message (template) | Source |
|---|---|
| none found | |

What each message means in practice: Not determined from code beyond the text itself — to be filled from incident history.

## Related

- PLT-MSREP-OVERVIEW, CMP-REPINTEGRATION, FLW-PR-EXPORT
