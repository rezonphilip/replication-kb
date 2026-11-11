---
doc_id: DATA-MSREP-RESEND
type: reference
mechanism: [priority-replication]
group: data
direction: both
runs_on: [office, vessel]
components: [RepIntegration, RepTransfer, RepAcquisition]
sources: ["MS-REP code and database scripts snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# Resend and missing packets — the exact rules

The receiver records gaps in packet counters as missing packets; the sender resends packets that the other side reports missing, packets in error, and packets never acknowledged. Each packet is resent at most 5 times, at least 30 minutes apart. Once those limits are hit, nothing resends that packet automatically any more.

## How the receiver records a gap

When a packet counter jumps, the receiver writes a `MSG` row per missing counter in `REP.PR_REP_Missing_Packets`, marked with which side detected it. Keywords: missing packet, MSG, MISSING_AT, gap detection, RCD, PSD.

- `MISSING_AT` is `V` when `Common.CO_Parameters` `IS_VESSEL` = `Y`, otherwise `O` (`RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/004_PR_REP_MISSING_PACKETS_OPERATIONS.sql#L14-L17`).
- When the missing packet arrives the row becomes `RCD`, and `PSD` once processed; rows already `PSD` are never updated again (`RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/004_PR_REP_MISSING_PACKETS_OPERATIONS.sql#L18-L33`).
- A `RCD` row with no import-queue item after 15 minutes is turned into `ERR` (`#L37-L55`), so it is requested again.
- RepIntegration sends the missing list to the sender as a notification (`Starting to send missing packet notification`, `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1597`; failures such as `no queue name found for missing packet notification for record {RecordId}`, `#L1732`).

## Does a gap block later packets?

Yes for a packet that depends on an earlier one: acquisition returns `SEQ_WAITING` and the import item waits. Keywords: sequence waiting, AWAITING, packet waiting, import blocked, out of order.

- Log: `Packet is waiting {PacketCounter} for another packet before this to proceeed` (`RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L696-L700`); the item is set to `AWAITING`.
- A stronger per-vessel check exists in the database — `REP.PR_VALIDATE_VSL_IMPORTQ` puts **all** pending import items of a communication type into a wait status while any `MSG`/`ERR` missing packet exists (`RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/123_PR_VALIDATE_VSL_IMPORTQ.sql#L13-L45`) — but its call in `ImportProcessor` is **commented out** in this snapshot (`RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L203-L219`). Note the procedure as written does not filter the queue by vessel. Recorded as open question Q18 in case it is re-enabled.
- Practical consequence: a single missing packet can hold up the packets after it until the resend arrives. Check missing packets first when imports for one vessel stop (ISS-PR-001).

## Which packets the sender resends

The current resend procedure is `REP.PRIORITY_RESEND_DATA`, run for a list of vessels. Keywords: resend rules, PRIORITY_RESEND_DATA, resend limit, 5 resends, 30 minutes, 60 days.

It picks, per call (`RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/112_PRIORITY_RESEND_DATA.sql`):

| Group | Rule | Max per call | Lines |
|---|---|---|---|
| Reported missing / in error | Packet whose counter is `MSG`/`ERR` in the other side's missing list, **or** packet header `ERR` with no missing-packet row | 100 | L25-L46 |
| Not yet acknowledged | Packet header `PCK` or `PND` | 10 | L50-L59 |
| Manual requests | `REP.PR_RESEND_QUEUE` rows with `STATUS = 0` | 50 | L63-L69 |

Limits applied to the first two groups (L14-L15, L45, L58):
- only packets modified in the **last 60 days**;
- skipped if already resent **5 times** (`PR_RESEND_LOG.COUNT >= 5`);
- skipped if last resent **less than 30 minutes ago**.

Every resend increments `PR_RESEND_LOG.COUNT` (or inserts a row with `RND`), and manual queue rows are set to `STATUS = 1`. The older `REP.PR_GET_RESEND_PACKET` uses similar rules (top 5 missing/error, top 5 `PCK` from the last 7 days, more than 5 resends excluded, 30-minute gap; `RepIntegration/PAL.DatabaseScripts.Office/StoredProcedures/028_PR_GET_RESEND_PACKET.sql#L10-L47`). Which procedure each resend path uses is in CMP-REPINTEGRATION (priority resend in the worker loop, `GeneralPacketResend` in the queue code).

## When resend has given up

After 5 resends a packet is never picked automatically again, even if the other side still reports it missing. Keywords: resend exhausted, resend limit reached, manual resend, PR_RESEND_QUEUE, still missing.

Signs: the receiver still has a `MSG`/`ERR` row for the counter, and the sender's `PR_RESEND_LOG` shows `COUNT` ≥ 5 for that packet. The only automatic path left is a manual request row in `REP.PR_RESEND_QUEUE` (`STATUS = 0`), which bypasses the count check in `PRIORITY_RESEND_DATA`. Adding such a row is a data change — approval required (ISS-PR-002).

## Related

- DATA-MSREP-STATUS, FLW-PR-EXPORT, FLW-PR-IMPORT, ISS-PR-001, ISS-PR-002
