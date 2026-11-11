---
doc_id: DATA-MSREP-STATUS
type: reference
mechanism: [priority-replication, smartsync]
group: data
runs_on: [office, vessel]
components: [RepIntegration, RepTransfer, RepAzure, RepAzureRes, RepAcquisition]
sources: ["MS-REP code and database scripts snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# MS-REP status codes and automatic resets

Every MS-REP queue table has a `STATUS` column, and most have a procedure that quietly puts "stuck" rows back to pending after a fixed time. Knowing the codes and the timers tells you whether a row is genuinely stuck or just waiting for its next automatic retry. Numeric codes whose names are defined in model classes that were not in the snapshot are described by behaviour only.

## Packet and record status letters (text codes)

Text status codes are shared by packet headers, track-change records and missing-packet rows; RepIntegration maps them to names. Keywords: PND, PCK, PSD, ERR, RCD, MSG, RND, RED, WTG, SNT, status meaning.

| Code | Name in code | Where it appears |
|---|---|---|
| `PND` | PENDING | track records, packet headers, missing packets |
| `WTG` | (waiting — picked by an export run) | `PR_TRACKCHANGE_RECORDS`, `PR_TRACKCHANGE_VESSELS` |
| `RED` | (being read for transfer) | `PR_REP_OUT_Packet_HD` |
| `PCK` | PACKED | `PR_REP_OUT_Packet_HD` after RepTransfer moved the files |
| `SNT` / `SNS` / `SND` | SENT | packet headers |
| `RND` | (resend requested) | `PR_RESEND_LOG`, `PR_REP_OUT_Packet_HD` |
| `RCD` | RECEIVED | `PR_REP_Missing_Packets` (receiver side) |
| `MSG` | MISSING | `PR_REP_Missing_Packets` |
| `PSD` | PROCESSED | track records, missing packets |
| `ERR` | ERROR | all of the above |
| `WTR` | Not determined from code | used by RepSaveData (`PR_REP_SAVE_DATA_OPERATION`) and RepAcquisition |

Names: `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/CommonOperationBL.cs#L65-L98`. Codes without a name there are described from the procedures that set them.

## Export: track-change records

Changes waiting to be exported move PND → WTG when an export run picks them, and are put back to PND automatically if they stay WTG or ERR too long. Keywords: track change records, PR_TRACKCHANGE_RECORDS, WTG stuck, export pending.

- `REP.PR_REP_READ_PENDING_EXPORT` takes up to 500 `PND` records for the requested channels and vessels and marks them `WTG` (`RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/138_PR_REP_READ_PENDING_EXPORT.sql#L44-L93`).
- `REP.PR_REP_TRACK_EXCEED_CHECK` resets `WTG` older than **1 hour** and `ERR` older than **15 minutes** back to `PND`, for both records and per-vessel rows (`RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/137_PR_REP_TRACK_EXCEED_CHECK.sql#L25-L62`).
- So an `ERR` track record is retried roughly every 15 minutes indefinitely; no retry limit was found in this procedure.

## Export: outgoing packet headers

`REP.PR_REP_OUT_Packet_HD` tracks each outgoing packet; the transfer step marks rows `RED` while working and resets them if it does not finish. Keywords: PR_REP_OUT_Packet_HD, RED stuck, ERR retry, RETRY_COUNT, packet header.

- `REP.PR_PACKET_TRANSFER_INFO` resets `RED` rows older than **20 minutes**, and `ERR` rows older than **30 minutes** with `RETRY_COUNT` below **5** (incrementing `RETRY_COUNT`), back to `PND`; it then picks up to 1000 `PND` rows for the vessel **with `COMM_TYPE = 5`** and marks them `RED` (`RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/140_PR_PACKET_TRANSFER_INFO.sql#L8-L61`).
- After 5 failed retries an `ERR` packet is no longer reset by this procedure; it then depends on the resend rules (DATA-MSREP-RESEND).
- RepTransfer sets `PCK` after moving the files to the delivery folder (CMP-REPTRANSFER).
- `COMM_TYPE = 5` is not one of the values seeded in `REP.COMMUNICATION_TYPE` (0–4); what 5 means is Not determined from code (open question Q15).

## Import: import queue (numeric codes with names)

`REP.PR_REP_IMPORT_QUEUE` uses named numeric statuses from the RepIntegration model; RepIntegration resets stuck items itself on each import run. Keywords: import queue, PR_REP_IMPORT_QUEUE, AWAITING, PROCESSING, FAILED, ABORTED, SEQ_WAITING.

Statuses used in code: `PENDING`, `READ`, `PROCESSING`, `AWAITING`, `COMPLETED`, `FAILED`, `ABORTED` (`RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs`). Their numeric values are in a model class that was not in the snapshot.

| Reset at the start of each import run | After | Source |
|---|---|---|
| `READ` → `PENDING` | 10 minutes | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L52-L58` |
| `FAILED` → `PENDING` | 5 minutes | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L59-L64` |
| `PROCESSING` → `PENDING` | 45 minutes | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L65-L70` |

- A packet that must wait for an earlier packet returns `SEQ_WAITING` from acquisition and the item is set to `AWAITING`; the log line is `Packet is waiting {PacketCounter} for another packet before this to proceeed` (`RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L696-L700`).
- Finished items are copied to `REP.PR_REP_IMPORT_QUEUE_HISTORY` by `REP.PR_REP_IMPORT_MOVE_HISTQ`, which moves whatever items RepIntegration passes in and records a `STATUS_MESSAGE` and `END_DATE` (`RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/120_SP_PR_REP_IMPORT_MOVE_HISTQ.sql#L4-L44`). Which statuses RepIntegration sends there: Not determined from code beyond the call site (`RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L571`). The history table is the place to look for an item's final error text.
- `REP.COMMUNICATION_TYPE` values: 0 PriorityReplication, 1 VesselToVesselReplication, 2 NormalPackets, 3 iRep, 4 GeneralNotificationQueue (`RepIntegration/PAL.DatabaseScripts.Office/Scripts/130_DATA_PR_QUEUE_OPERATION_TYPE.sql`).

## Import: missing packets

`REP.PR_REP_Missing_Packets` records gaps in packet counters on the receiving side (`MISSING_AT` = `V` on a vessel, `O` at office, from `IS_VESSEL`). Keywords: missing packet, MSG, RCD, ERR, PSD, MISSING_AT, gap.

- Lifecycle: `MSG` (gap detected) → `RCD` (packet arrived) → `PSD` (processed). Updates never touch rows already `PSD` (`RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/004_PR_REP_MISSING_PACKETS_OPERATIONS.sql#L14-L33`).
- Operation `ERR`: a `RCD` row older than **15 minutes** with no matching import-queue item becomes `ERR`; the procedure then returns `ERR`/`MSG` rows received in the last **90 days** (`RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/004_PR_REP_MISSING_PACKETS_OPERATIONS.sql#L37-L64`). These are what the receiver asks the sender to resend.

## Transport: transfer queue

`REP.REP_TRANSFER_QUEUE` holds files to hand to the transport; its read procedure resets in-flight rows after per-status timeouts. Keywords: REP_TRANSFER_QUEUE, transfer queue stuck, status 7, retry exceeded.

| Status | Reset to | After | Condition |
|---|---|---|---|
| 1 | 0 | 30 min | `RETRY_COUNT` ≤ limit |
| 2 | 0 | 60 min | `RETRY_COUNT` ≤ limit |
| 3 | 0 | 120 min | `RETRY_COUNT` ≤ limit |
| 5 | 0 | 5 min | `RETRY_COUNT` ≤ limit |
| 5 | **7** | 5 min | `RETRY_COUNT` ≥ limit (gives up) |

Source: `REP.REP_READ_TRANSFER_QUEUE_DATA`, operation `PENDING` (`RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/086_REP_READ_TRANSFER_QUEUE_DATA.sql#L17-L45`). Rows in status **4** or **7** are moved to `REP_TRANSFER_QUEUE_HISTORY` (`RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/125_REP_MOV_TRANSFER_QUEUE_HIST.sql#L27-L32`). Reading of the table: 0 = pending, 4 = finished, 7 = failed after retries; names of 1/2/3/5 Not determined from code.

## Transport: Azure upload and download records

RepAzureRes upload rows and RepAzure download rows have their own numeric statuses and 10/15/30-minute resets. Keywords: REP_AZURE_RES_UPLOAD, REP_Downloads, upload status, download status.

Upload (`REP.REP_AZURE_RES_UPLOAD`, procedure `REP.REP_READ_AZURE_RES_UPLOAD`, `RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/083_REP_READ_AZURE_RES_UPLOAD.sql#L17-L51`):
- Operation `PENDING`: rows idle > **10 min** not in (0,3,5,7,8) and under the retry limit → 0; rows in 4 at/over the retry limit → 5.
- Operation `CALLINT` (callback to integration): rows in 7 idle > 10 min under the limit → 3; rows in 4 at/over the limit → 5.

Download (`REP.REP_Downloads`, procedure `REP.PR_REP_READ_AZURE_FILE_Q`, `RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/104_PR_REP_READ_AZURE_FILE_Q.sql#L20-L135`):
- `GET_PND_DOWNLOAD`: rows in 1/2 idle > **30 min**, or 5 idle > **15 min**, under the limit → 0; picked rows are set to 1.
- `PENDING_MOVE`: rows in 10/7 idle > 30 min → 3; picked rows set to 10.
- `GET_DEL`: rows in 13/12 idle > 30 min → 14; picked rows set to 13.

Names of these numeric codes: Not determined from code (enum classes not in snapshot; open question Q15).

## Related

- DATA-MSREP-OVERVIEW, DATA-MSREP-RESEND, FLW-PR-EXPORT, FLW-PR-IMPORT, CMP-REPAZURE, CMP-REPAZURERES
