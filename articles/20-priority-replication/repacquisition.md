---
doc_id: CMP-REPACQUISITION
type: component
mechanism: [priority-replication]
group: pr-receive
runs_on: [office, vessel]
components: [RepAcquisition]
log_files: [AcquisitionLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepAcquisition — picks up incoming packet files

RepAcquisition is the first receive step: it picks up incoming packet files from the inbox folders, registers them, detects missing packets, handles error files and queues them for import (`Acquisition/FILE`, `AcquireExtFiles`, `Initiate-Acquisition`, `Initiate-Error-File-Handler`, `Batch-Acquisition-Process`). It can start RepIntegration's import queue itself.

## Role in replication

RepAcquisition is a Priority Replication receive-side step with no timer of its own: it runs only when called over HTTP (no hosted background service found in the project). Keywords: RepAcquisition, acquisition, priority replication, receive side, picks up incoming packet files.

- Folders: `REP_OFF_ROOT`, `PR_REP_ROOT`.
- Missing packets: `PR_REP_MISSING_PACKETS_OPERATIONS`, `GET_MISSING_PRIORITY_PACKETS`; import registration: `PR_REP_SAVE_IMPORT_PACKET_DATA` (and `_BULK`).
- Starts the import queue after acquisition (`RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L161`, `#L218`).

## API routes

Controller routes and their source lines. Keywords: RepAcquisition routes, API, TestService.

| Route | Source |
|---|---|
| `Acquisition-General` | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionGeneralController.cs#L10` |
| `Batch-Acquisition-Process` | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionGeneralController.cs#L26` |
| `Acquisition` | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L15` |
| `FILE` | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L39` |
| `AcquireExtFiles` | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L66` |
| `Initiate-Acquisition` | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L92` |
| `Initiate-Error-File-Handler` | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L104` |
| `TestService` | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L116` |
| `AddToQueue` | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L123` |
| `ReadQueue` | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L129` |
| `DeleteAllFromQueue` | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L135` |
| `Version` | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L142` |
| `Init` | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L149` |

## Database and parameters

Stored procedures and CO_Parameters keys this service uses (names only). Keywords: RepAcquisition stored procedure, CO_Parameters, REP schema.

- `PR_REP_ROOT` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1267`
- `REP.GET_MISSING_PRIORITY_PACKETS` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L28`
- `REP.GET_V2V_MISSING_PACKET_STATUS` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L27`
- `REP.GET_V2V_PACKET_COUNTER_IMPORT` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L26`
- `REP.PR_GET_PARAM_DATA` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L30`
- `REP.PR_GET_TRANSFER_DATA` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L199`
- `REP.PR_GET_VESSEL_CODE` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L165`
- `REP.PR_REP_GET_ALL_SETTINGS` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L20`
- `REP.PR_REP_GET_PACKET_COUNTER` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L12`
- `REP.PR_REP_IMPORT_QUEUE_DT_TYP` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L8`
- `REP.PR_REP_IMPORT_QUEUE_TYP` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L7`
- `REP.PR_REP_MISSING_PACKETS` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L888`
- `REP.PR_REP_MISSING_PACKETS_EXT` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L469`
- `REP.PR_REP_MISSING_PACKETS_OPERATIONS` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L95`
- `REP.PR_REP_READ_ALL_CHANNELS` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L24`
- `REP.PR_REP_SAVE_IMPORT_PACKET_DATA` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L17`
- `REP.PR_REP_SAVE_IMPORT_PACKET_DATA_BULK` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L18`
- `REP.PR_REP_V2V_SAVE_PACKET_DETAILS` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L25`
- `REP.PR_UPDATE_VESSEL_SETTINGS` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L19`
- `REP.REP_GETDOWNLOADS_TABLEID` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L16`
- `REP.REP_GET_CURRENT_VESSEL_TRANSFER` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L22`
- `REP.REP_GET_DOWNLOAD_PACKET_DETAILS` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L521`
- `REP.REP_GET_PR_CHANNEL_DETAILS` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L23`
- `REP.SAVE_IMPORT_PACKET_TYP` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L6`
- `REP.SAVE_PR_REP_IMPORT_QUEUE` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L29`
- `REP.UPDATE_PR_REP_IMPORT_Q` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L30`
- `REP.UPDATE_PR_REP_IMPORT_QUEUE_DT` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/SqlNamedQueries.cs#L31`
- `REP.rep_GetDOWNLOADS_TABLEID` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L307`
- `REP_CODE` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L168`
- `REP_OFF_ROOT` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L861`
- `REP_PR_KEY_MASTER_ID` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L494`
- `REP_SOURCE_UNIQUE_ID` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L495`
- `REP_SOURCE_UNIQUE_OBJECT_TYPE` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L496`
- `[REP].[GET_MISSING_PRIORITY_PACKETS]` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L802`
- `[REP].[GET_V2V_MISSING_PACKET_STATUS]` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L708`
- `[REP].[GET_V2V_PACKET_COUNTER_IMPORT]` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L651`
- `[REP].[PR_REP_GET_ALL_SETTINGS]` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L401`
- `[REP].[PR_REP_GET_PACKET_COUNTER]` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L57`
- `[REP].[PR_REP_SAVE_IMPORT_PACKET_DATA]` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L343`
- `[REP].[PR_REP_SAVE_IMPORT_PACKET_DATA_BULK]` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L826`
- `[REP].[PR_TRACKCHANGE_NEW_TYP_V2V]` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L777`
- `[REP].[PR_TRACKCHANGE_TYP]` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L473`
- `[REP].[PR_UPDATE_VESSEL_SETTINGS]` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L371`
- `[REP].[REP_GET_CURRENT_VESSEL_TRANSFER]` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L560`
- `[REP].[REP_GET_PR_CHANNEL_DETAILS]` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L584`
- `[REP].[SAVE_TRACK_CHANGE_RECORD]` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L469`
- `[REP].[SAVE_TRACK_CHANGE_RECORD_V2V]` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L773`
- `[Rep].[PR_REP_V2V_SAVE_PACKET_DETAILS]` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L610`
- `[Rep].[REP_GET_DOWNLOAD_PACKET_DETAILS]` — `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L516`

Parameters: `PR_REP_ROOT`, `REP_CODE`, `REP_OFF_ROOT`, `REP_PR_KEY_MASTER_ID`, `REP_SOURCE_UNIQUE_ID`, `REP_SOURCE_UNIQUE_OBJECT_TYPE`.

## Logs and what to look for

Log: `Logs/AcquisitionLog_.txt`. Error-type messages found in code (first 10; full list in `inventory/ms-rep-logs.md` → RepAcquisition). Keywords: AcquisitionLog_.txt, RepAcquisition error, failed.

| Message (template) | Source |
|---|---|
| {MethodName} - Error in reading Common CO Parameters values | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L57` |
| {MethodName} Exception while reading last in packet counter | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L95` |
| {MethodName}\|Exception occured while reading missing packet data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L140` |
| {MethodName}\|Exception occured while reading error missing packet data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L175` |
| {MethodName}\|Exception occured while reading vessel rep code | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L210` |
| {MethodName}\|Error occured while reading transfer data for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L242` |
| {MethodName}\|Error occured while reading transfer location for {TransferID} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L273` |
| {MethodName}\|Exception occured while reading vessels | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L322` |
| {MethodName}\| Exception while reading Table Settings Id from Downloads for {FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L357` |
| {MethodName}\| Import Packet Data saved with InPacketHdId {InPacketHdId} and MissingPacketId {MissingPacketId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L392` |

What each message means in practice: Not determined from code beyond the text itself — to be filled from incident history.

## Related

- PLT-MSREP-OVERVIEW, CMP-REPINTEGRATION, FLW-PR-IMPORT
