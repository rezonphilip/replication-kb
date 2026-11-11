---
doc_id: CMP-REPTRANSFER
type: component
mechanism: [smartsync, priority-replication, irep]
group: transfer-adapter
runs_on: [office, vessel]
components: [RepTransfer]
log_files: [TransferServiceLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepTransfer — adapter between replication and the SmartSync transport

RepTransfer decides *how* a packet leaves for a given vessel and puts the packet files where that delivery method picks them up: an outbox folder for Azure (SmartSync), or a medium folder for the other delivery methods. It also prepares resends and V2V downloads. It has no timer: it only acts when RepIntegration (or another caller) asks.

## Role in replication

RepTransfer is a thin adapter over the transport, used for transfer-related requirements of Priority Replication and possibly iRep. Keywords: transfer, outbox, delivery method, transfer type, resend, sent folder, medium.

- Called by RepIntegration: `Transfer/TransferPacket`, `TransferPacketExt`, `TransferPacketFolder`, `TransferResendPacket`, `Priority-Resend`, `TransferGeneral` (see `inventory/ms-rep.md` → RepIntegration).
- Calls RepAzure for V2V downloads (`TransferDownloadAzureFile`, `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferPacketExtBL.cs#L618`).
- Updates packet state in the database (`REP.PR_REP_UPDATE_PACKET_DATA`, `UpdateOutPacketHd` with status `PCK` after a successful move — `BL/TransferBL.cs#L125-L175`).

## How the delivery method is chosen

For every vessel, RepTransfer reads the vessel's delivery method and branches on it. Keywords: TRANSFER_TYPE, DELIVERY_METHOD, REP_VESSEL_INFRA, transfer type could not be found, IS_PRODUCT.

- Transfer type = `DELIVERY_METHOD` from `[REP].[REP_VESSEL_INFRA]` for the vessel (also exposed as `REP.PR_GET_TRANSFER_DATA` operation `TRANSFER_TYPE`; vessel ID `-999` always gives `2`); when `Common.CO_Parameters` `IS_PRODUCT` = `N` the table is read from the `[PAL_REP]` database (`RepTransfer/MariApps.PAL.Rep.Transfer.DAL/TransferRepository.cs#L94-L125`). The read is retried 3 times, 500 ms apart (L19-L20).
- Empty result → packet fails with `FAILED: Transfer Type could not be found` (`BL/TransferBL.cs#L50-L62`).
- Types `0` and `1`: files are moved to `<TRANSFER_LOCATION_CODE folder>/<generated folder>/<VesselObjectId>` (`BL/TransferBL.cs#L71-L124`). Both use the `REP_OFF_ROOT` folder (`REP.PR_REP_TRANSFER_MASTER`, DATA-MSREP-SETTINGS); what distinguishes 0 from 1 (e.g. e-mail vs manual medium): Not determined from code.
- Type `3` maps to `REP_REALM_ROOT` in the database, but `MoveFile` has no branch for it; behaviour for type 3: Not determined from code (open question Q19).
- Type `2` (Azure / SmartSync): files are moved to `<location>/OUT/PR/OUTBOX/<VesselObjectId>`; a `SENT/<VesselObjectId>` folder is created alongside (`BL/TransferBL.cs#L125-L140`). RepAzureRes uploads from there.
- If the base folder for the type is not configured: `transferMediumBaseFolder is null or empty for transfer type: {TransferType}` (types 0/1) or `Out box folder is not gotten for transfer type` (type 2).

## API routes

Routes are under `Transfer` (`RepTransfer/MariApps.PAL.Rep.Transfer.Service/Controllers/TransferController.cs`). Keywords: TransferPacket, TransferResendPacket, Priority-Resend, TransferDownloadAzureFile.

| Route | Purpose | Line |
|---|---|---|
| `TransferPacket` | Move new packets to the delivery location | L40 |
| `TransferPacketFolder` | Same, folder-based input | L73 |
| `Transfer-Priority-Handler` | Batch priority transfer (`BL/TransferHandler.cs#L31`) | L118 |
| `TransferResendPacket` / `Priority-Resend` | Resend previously sent packets | L134 / L161 |
| `TransferPacketExt` | Extended packet transfer (Azure folder structure per client) | L168 |
| `TransferResendUploadV2V`, `TransferDownloadAzureFile` | Vessel-to-vessel resend/download | L197 / L219 |
| `TransferGeneral` | General (non-priority) transfer | L260 |
| `TestService`, `GetVersion` | Health | L283 / L292 |

## Configuration

Keywords: REP_PR_AZURE_IN, REP_PR_AZURE_SENT, PR_REP_ROOT, TRANSFER_LOCATION_CODE.

| Key | Where | Effect |
|---|---|---|
| `DELIVERY_METHOD` | `[REP].[REP_VESSEL_INFRA]` per vessel | Chooses the branch above. |
| `TRANSFER_LOCATION_CODE` (operation type) | `REP.PR_GET_TRANSFER_DATA` → `REP.PR_REP_TRANSFER_MASTER.REP_CODE` → `Common.CO_Parameters` value whose name contains that code (`RepTransfer/PAL.DatabaseScripts.Office/StoredProcedures/002_SP_[Rep].[PR_GET_TRANSFER_DATA].sql#L24-L28`) | Base folder per delivery method: 0/1 → `REP_OFF_ROOT`, 2 → `REP_AZURE_ROOT`, 3 → `REP_REALM_ROOT`. |
| `IS_PRODUCT` | CO_Parameters | Selects `[PAL_REP]` database prefix. |
| `PR_REP_ROOT`, `REP_PR_AZURE_IN`, `REP_PR_AZURE_SENT`, `REP_LOG` | CO_Parameters | Root, Azure in/sent folders, log path. |
| Service address of RepAzure | `microservices.json` | For V2V download calls. |

RepTransfer's own DB scripts also seed many SmartSync parameters (for example `REP_SERVICEBUS_CONNECTION_STRING` **(secret)**, `REP_CHUNK_SIZE`, `REP_PARALLEL_PROCESS_COUNT`, `REP_PR_FILECABINET_IN`, `REP_PR_NORMAL_IN`, `REP_REALM_ROOT`, `REP_EXPORT_TRANSFER_API_URL`/`_BASE_URL`) and Service Bus tables (`REP_SERVICE_BUS_MASTER`, `REP_SERVICE_BUS_TRANSACTION_SETTINGS`) — see `inventory/ms-rep.md` → RepTransfer.

## Logs and what to look for

Log: `Logs/TransferServiceLog_.txt`. Errors are also written to the database through `[Rep].[PR_SAVE_ERROR_LOG]`. Keywords: TransferServiceLog, transfer type, move failed, out box folder.

| Message (fragment) | Meaning | Source |
|---|---|---|
| `FAILED: Transfer Type could not be found` | Vessel has no `DELIVERY_METHOD`. | `BL/TransferBL.cs#L50-L62` |
| `transferMediumBaseFolder is null or empty for transfer type` | No base folder for type 0/1. | `BL/TransferBL.cs#L72-L80` |
| `Out box folder is not gotten for transfer type` | No base folder for type 2. | `BL/TransferBL.cs#L128-L132` |
| `Error while moving '{file}' for transfer type` | File move failed (permissions, file locked, missing). | `BL/TransferBL.cs` (MoveFile) |
| `Error while getting packet id for packet` | File name did not give a packet id; status not updated. | same |
| `Transfer directory is empty for transferType {TransferType}, vessel {VesselObjectId}` | Priority batch: no folder for that type. | `BL/TransferHandler.cs#L31-L80` |

## Common failure points

Keywords: packets not leaving, outbox empty, transfer type missing, wrong delivery method.

- Vessel has no or wrong delivery method → ISS-TRANSFER-001.
- Folder missing / permission denied when moving files → ISS-TRANSFER-002 (to be written).

## Related

- PLT-MSREP-OVERVIEW, CMP-REPINTEGRATION, CMP-REPAZURERES, FLW-PR-EXPORT
- ISS-TRANSFER-001
