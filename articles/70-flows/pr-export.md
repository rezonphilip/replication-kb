---
doc_id: FLW-PR-EXPORT
type: flow
mechanism: [priority-replication, smartsync]
direction: both
runs_on: [office, vessel]
components: [RepIntegration, RepTrack, RepProData, RepPacketCreation, RepCompression, RepSplit, RepMedium, RepPacketInterim, RepTransfer, RepAzureRes, RepSbus, RepDBLogW]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# Priority Replication — sending a packet (export → transfer → upload)

This flow takes changed records on one side (office or vessel), packs them into numbered packets, moves them to the vessel's delivery location and — for Azure delivery — uploads them and notifies the other side. RepIntegration drives every step. "Done" for the sender means the packet was acknowledged by the receiver; until then it is eligible for resend.

> **V2V (vessel-to-vessel) is a dropped feature.** The V2V routes, procedures and message types mentioned in this article still exist in the code and database but are not in use; do not troubleshoot them. See DATA-MSREP-OFFVSL.

## Steps at a glance

There are two export paths in the code — the older chained export and the newer queue-based export — and both end in RepTransfer. Keywords: export steps, packet, transfer, upload, notification, chain, queue.

Queue-based (worker steps 6–8 in RepIntegration):
1. Track records are saved by RepTrack (`SaveTrackChangeRecord` / `SaveTrackChangeFile`).
2. RepIntegration `TrackExportQueueBuilder` reads pending track records, builds packets per table setting, compresses and copies them to per-vessel folders → packets "ready for Transfer" (`RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L47-L512`).
3. `PacketTransferHandler` validates packet files per vessel and calls RepTransfer (`ExportQueueProcess.cs#L515-L963`).
4. RepTransfer moves files to the delivery location for the vessel's `DELIVERY_METHOD` and marks the packet `PCK` (CMP-REPTRANSFER).
5. For Azure delivery, RepAzureRes uploads from the outbox and calls back (CMP-REPAZURERES).
6. RepSbus sends a `PACKET_TRANSFER` notification; the receiver answers `ACKNOWLEDGMENT_NOTIFICATION` (`RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L328-L344`).

Chained export (worker step 1, `InitiateExport`), as built by `IntegrationSetInputBL` / `IntegrationExportApiCallBL` in RepIntegration:
ProData `ProData/ProcessData` → PacketCreation `Packet/Create` (compression type from RepDBLogW `ReadCompressionType`) → Compression `Compress/ZIP` → Split `Split/Zip` → Transfer `Transfer/TransferPacket` (with Medium `GetSizeRestriction`, Split `SplitExt`, PacketInterim `ReadPckCounter` / `CreateJsonFile` / `UpdatePacketStatus`, PacketCreation `GeneratePacketExt`, Track `UpdateTrackStatus`, Transfer `TransferPacketExt`, DBLogW `UpdateOutPacketSource` / `GetExportParams` / `SaveExtPacketDetails`).

## Preconditions that silently stop export

If any of these is missing, the export step logs a message and exits without error popups. Keywords: export not running, nothing exported, no PR enabled vessels, channel not found, disabled by configuration.

| Condition | Message in IntegrationServiceLog | Source |
|---|---|---|
| RepIntegration loop disabled | `Integration main processes not started due to InitiateOnInterval is false` | `WorkerService.cs#L93` |
| Queue export disabled | `Export process is disabled by configuration` | `BL/QueueHandler/IntegrationQueueProcessBL.cs#L82-L90` |
| General Packet channel missing | `General Packet channel information not found. Exiting.` | `ExportQueueProcess.cs#L58` |
| Working directory not set | `Working directory is not configured. Exiting.` | `ExportQueueProcess.cs#L65` |
| No channel flow settings | `No channel flow settings found for export. Exiting.` | `ExportQueueProcess.cs#L75` |
| No PR-enabled vessel | `No PR enabled vessels found. Exiting.` | `ExportQueueProcess.cs#L85` |
| No vessel with General Export | `No vessels found with General Export enabled. Exiting.` | `ExportQueueProcess.cs#L93` |
| Nothing to send | `No pending track records found for export. Exiting.` | `ExportQueueProcess.cs#L106` |
| Previous run still active | `Export Process is already running. Last updated Time:` | `IntegrationQueueProcessBL.cs#L105-L115` |

On the vessel, `VerifyGenExportValidity` tries to enable General Export for the vessel automatically (`IntegrationQueueProcessBL.cs#L344-L458`).

## Transfer step and packet file validation

Before calling RepTransfer, every pending packet's file is checked and, if missing, recovered from the sent folder. Keywords: packet file missing, recovery, validation failed, error status, transfer failed for vessel.

- `File not found at original location for Packet ID {PacketId}: {FilePath}. Attempting recovery.` → looks in the path with OUT replaced by SENT (`ExportQueueProcess.cs#L845-L940`).
- Packets that still fail validation are set to error status: `{FailedCount} packets failed validation for vessel {VesselObjectId}. Updating them with error status.` (L620).
- RepTransfer errors: `Transfer failed for vessel {VesselObjectId} with message: {ErrorMessage}` (L672).

## Resend

Packets not acknowledged in time are resent. Keywords: resend, no acknowledgement, priority resend, ResendTimeInH.

- Worker step 2 `InvokePriorityResend` and step 8 `GeneralPacketResend` → `PacketTransferResendHandler` (`ExportQueueProcess.cs#L966-L1223`) → RepTransfer `TransferResendPacket` / `Priority-Resend`.
- Timing: `BasicSettings:ResendTimeInH`, `ResendExceedTimeInH` in RepIntegration.
- Selection rule (`REP.PRIORITY_RESEND_DATA`): packets the other side reports missing or in error, packets in `ERR`, and unacknowledged `PCK`/`PND` packets from the last 60 days, plus manual `PR_RESEND_QUEUE` requests; at most 5 resends per packet, at least 30 minutes apart. Details: DATA-MSREP-RESEND.
- V2V resend goes through RepAzureRes `V2VAzureResendData` (V2V is a dropped feature).

## How to tell where a packet is stuck

Use the last thing you can see to locate the stuck step. Keywords: where is my packet, stuck packet, not received, not uploaded.

| Last thing you see | Stuck between | Check |
|---|---|---|
| Track records pending, no packet | RepIntegration export step | Preconditions table above; `IntegrationServiceLog_` |
| Packet created, not in outbox | RepTransfer | `TransferServiceLog_`; vessel `DELIVERY_METHOD` (ISS-TRANSFER-001) |
| File in `OUT/PR/OUTBOX/<vessel>`, never uploaded | RepAzureRes | `AzureResumeLog_` (ISS-AZURERES-001) |
| Uploaded, receiver never downloads | RepSbus (either side) / RepAzure (receiver) | `SbusLog_` listener (ISS-SBUS-001); receiver `AzureService_` (ISS-AZURE-001) |
| Received, no acknowledgement back | Receiver import / RepAckn | FLW-PR-IMPORT |

For a database view of every stage at once run `catalog/scripts/queue-status-summary.sql` (statuses explained in DATA-MSREP-STATUS).

## Related

- FLW-PR-IMPORT, CMP-REPINTEGRATION, CMP-REPTRANSFER, CMP-REPAZURERES, CMP-REPSBUS
