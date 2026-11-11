---
doc_id: PLT-MSREP-OVERVIEW
type: overview
mechanism: [smartsync, priority-replication, irep]
runs_on: [office, vessel]
components: [RepSbus, RepAzure, RepAzureRes, RepTransfer, RepIntegration, RepDBLogW, RepProData, RepPacketCreation, RepCompression, RepSplit, RepPacketInterim, RepTrack, RepMedium, RepQueueManage, RepAcquisition, RepFileMerge, RepDecompress, RepSaveData, RepAckn]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# MS-REP — what the 19 services are and how they fit together

MS-REP is the replication service suite installed on both the office and every vessel. Its transport part is called **SmartSync** (Service Bus + Azure Blob); the rest of the suite implements **Priority Replication**, and RepIntegration also drives the transfer step for **iRep**. The iRep (SmartSync+, sync+) services are a separate suite documented in PLT-IREP; they use SmartSync for transport through RepIntegration `TransferGeneral`. When something "is not replicating", the first question is always *which group* has stopped: transport, adapter, orchestrator, or one of the Priority Replication steps.

## Same code on office and vessel

Every MS-REP service is the same binary at both ends; the role (office or vessel) comes from configuration and database parameters. Keywords: office, vessel, location, REP_LOCATION, OFF, same service both ends.

- The location is read from the `REP_LOCATION` parameter (for example in RepAzure, see `inventory/ms-rep.md` → RepAzure) and from `Location` in the Service Bus common settings. RepSbus treats the value `OFF` as office: on stop, only a non-office instance sends a "stopped" notification to the office queue (`RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L59-L72`).
- Database objects live in the `REP` schema; parameters are rows in `Common.CO_Parameters` read through procedures such as `[REP].[READ_COMMON_PARAMS_VALUE]` (`RepAckn/MariApps.PAL.Rep.Ackn.DAL/SqlNamedQueries.cs#L14`).
- Service addresses are not hard-coded: each service's `microservices.json` lists the other services with deployment placeholders (for example `$__TRANSFER_URL__$`, `$__DBLOG_URL__$`) that the installer replaces (`RepIntegration/MariApps.PAL.Rep.Integration.Service/microservices.json`).

## The six groups

The services split into six groups by responsibility. Keywords: SmartSync, Priority Replication, iRep, transport, adapter, orchestrator, DB gateway, send side, receive side.

| Group | Services | One-line role |
|---|---|---|
| SmartSync transport | RepSbus, RepAzure, RepAzureRes | Messages over Azure Service Bus; downloads (RepAzure) and resumable uploads (RepAzureRes) of packet files in Azure Blob. |
| Transfer adapter | RepTransfer | Puts packets into the right outbox/medium for a vessel and handles resend; sits between the orchestrator and the transport. |
| Orchestrator | RepIntegration | Background loop that starts export, import, resend, notification, acquisition and transfer queues. For iRep it handles transfer only. |
| PR core / DB gateway | RepDBLogW | HTTP gateway to the replication database (packet logs, Service Bus settings, download records). |
| PR send side | RepProData, RepPacketCreation, RepCompression, RepSplit, RepPacketInterim, RepTrack, RepMedium, RepQueueManage | Read pending changes, build packets, zip, split to size, record counters and track status. |
| PR receive side | RepAcquisition, RepFileMerge, RepDecompress, RepSaveData, RepAckn | Pick up incoming files, re-join splits, unzip, apply data, send acknowledgements. |

## Which services run on their own

Only four services have a background worker loop; the rest act only when called over HTTP. Keywords: worker service, background, interval, scheduler, not running, idle.

| Service | Loop interval key | Main steps each cycle | Source |
|---|---|---|---|
| RepIntegration | `WorkerServiceSettings:SchedulerIntervalInMinutes` × `SchedulerMultiplier` | export, priority resend, general notification, acquisition, export validity, export queue, PR transfer queue, general packet resend | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L42-L111` |
| RepSbus | `ReceiverCheckIntervalInMinutes` | make sure the Service Bus listener is running; restart it if not | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L83-L145` |
| RepAzure | `WorkerServiceSettings:SchedulerIntervalInMinutes` | download queue, move pending files, delete worker, move to history | `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L47-L88` |
| RepAzureRes | `WorkerServiceSettings:SchedulerIntervalInMinutes` | check Azure settings, upload pending data, Azure callback, clear old JSON | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/WorkerService.cs#L46-L86` |

Practical consequence: if RepIntegration is stopped, nothing new is exported or imported even though every other service answers `TestService`.

## Logs

Each service writes its own rolling Serilog file under its `Logs` folder; RepSbus's path is a deployment placeholder. Keywords: log file, Logs folder, Serilog, where are the logs.

| Service | Log file name | Service | Log file name |
|---|---|---|---|
| RepIntegration | `IntegrationServiceLog_.txt` | RepAcquisition | `AcquisitionLog_.txt` |
| RepSbus | `SbusLog_.txt` (folder from `$__LOG__$`) | RepFileMerge | `FileMergeLog_.txt` |
| RepAzure | `AzureService_.txt` | RepDecompress | `DecompressLog_.txt` |
| RepAzureRes | `AzureResumeLog_.txt` | RepSaveData | `SaveDataLog_.txt` |
| RepTransfer | `TransferServiceLog_.txt` | RepAckn | `AcknLog_.txt` |
| RepDBLogW | `DbLogServiceLog_.txt` | RepProData | `ProDataLog_.txt` |
| RepPacketCreation | `PacketCreatLog_.txt` | RepCompression | `Compression_Log_.txt` |
| RepSplit | `SplitServiceLog_.txt` | RepPacketInterim | `PacketInterimLog_.txt` |
| RepTrack | `TrackServiceLog_.txt` | RepQueueManage | `QueueManagerLog_.txt` |
| RepMedium | `Log_.txt` | | |

Source: the `Serilog` section of each service's `appsettings.json`. Most messages start with `{MethodName}|`, which makes the method name the best search term.

## Related

- INV-MSREP, INV-MSREP-LOGS
- CMP-REPINTEGRATION, CMP-REPSBUS, CMP-REPAZURE, CMP-REPAZURERES, CMP-REPTRANSFER, CMP-REPDBLOGW
- FLW-PR-EXPORT, FLW-PR-IMPORT
