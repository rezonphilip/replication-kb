---
doc_id: FLW-PR-IMPORT
type: flow
mechanism: [priority-replication, smartsync]
direction: both
runs_on: [office, vessel]
components: [RepSbus, RepAzure, RepAcquisition, RepIntegration, RepFileMerge, RepDecompress, RepSaveData, RepAckn, RepDBLogW]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# Priority Replication — receiving a packet (download → import → acknowledge)

This flow takes a packet that the other side has sent, downloads it (Azure delivery), rebuilds it, applies the data and sends an acknowledgement back. RepAzure and RepIntegration run on timers; RepAcquisition starts the import queue. "Done" means the data is saved and an acknowledgement has been sent.

## Steps at a glance

Keywords: import steps, download, acquisition, merge, decompress, save data, acknowledgement.

1. RepSbus receives `PACKET_TRANSFER` and replies with `ACKNOWLEDGMENT_NOTIFICATION` (receipt of the notice, not of the data) (`RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L328-L344`).
2. RepAzure's download lane fetches files listed for download (records read through RepDBLogW, e.g. `[REP].[REP_GETFILESTODOWNLOAD]`, `[REP].[PR_REP_READ_AZURE_FILE_Q]`) and moves them to the local inbox (`RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L65-L77`).
3. RepIntegration worker step 4 runs acquisition; RepAcquisition registers files, detects missing packets and starts the import queue (`RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L586-L610`; `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L161`).
4. `ImportProcessor` takes each queue item: FileMerge → Decompress → save results → Ackn → general notification through RepSbus (`BL/QueueHandler/ImportQueueProcess.cs#L40-L1300`).
5. SaveData applies the records (`SaveData/ProcessData`).

## Preconditions that silently stop import

Keywords: import not running, files not processed, disabled by configuration, client details not found.

| Condition | Message | Source |
|---|---|---|
| Queue import disabled | `Import process is disabled by configuration` | `IntegrationQueueProcessBL.cs#L586-L600` |
| Client details missing | `Current Client details not found, cannot proceed with import` | `ImportQueueProcess.cs#L159` |
| General Notification channel missing | `General Notification Channel not found, cannot proceed with import` | `ImportQueueProcess.cs#L166` |
| Invalid channel / flow for item | `Channel Flow not found for channel-{Channel} ...` | `ImportQueueProcess.cs#L400-L420` |
| Zip folder missing | `AllZipDirectory does not exist or is not configured` | `ImportQueueProcess.cs#L451` |

## Failures per step

Each import step logs a specific message in `IntegrationServiceLog_` and its own service log. Keywords: merge failed, decompress failed, ackn failed, file not found, import item aborted.

| Step | Message in IntegrationServiceLog | Then look in |
|---|---|---|
| File present | `File {FileLocation} not found. Primary location missing.` (L508) | RepAzure / RepAcquisition logs |
| Merge | `File Merge Service failed for Import Item {Id} with error {ErrorMessage}` (L746) | `FileMergeLog_` — usually a missing split part |
| Decompress | `Process failed while handling Decompress service, marking as failed` (L868) | `DecompressLog_` — corrupt/incomplete zip |
| Save results | `Failed to save decompressed files to database for Import Item {Id}` (L925) | `DbLogServiceLog_` |
| Ackn | `Process failed while handling ackn service, marking as failed` (L1107) | `AcknLog_` |
| Notification | `Queue name is null or empty for Import Item {Id}` (L1279) | Service Bus settings (ISS-SBUS-002) |
| Any | `Import item has been aborted due to error {ErrorMessage} for Import Item {Id}` (L762, L1167) | the step named in the error |

All line numbers refer to `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs`.

## Missing packets

The receiver tracks packet counters and records gaps. Keywords: missing packet, gap, packet counter, out of sequence.

- RepAcquisition: `PR_REP_MISSING_PACKETS_OPERATIONS`, `GET_MISSING_PRIORITY_PACKETS`; RepDBLogW: `SaveMissingPackets`, `ReadMissingPacketById`.
- The import step updates missing-packet info after decompress (`ImportQueueProcess.cs#L979`).
- A later packet that depends on a missing one waits: acquisition returns `SEQ_WAITING`, the item goes to `AWAITING`, and the log says `Packet is waiting {PacketCounter} for another packet before this to proceeed` (`RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L696-L700`). Full rules and the (currently disabled) vessel-wide check: DATA-MSREP-RESEND; issue card ISS-PR-001.

## Related

- FLW-PR-EXPORT, CMP-REPAZURE, CMP-REPACQUISITION, CMP-REPFILEMERGE, CMP-REPDECOMPRESS, CMP-REPSAVEDATA, CMP-REPACKN
