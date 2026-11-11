---
doc_id: FLW-IREP-EXPORT
type: flow
mechanism: [irep, smartsync]
group: irep-export
runs_on: [office, vessel]
direction: both
components: [ExportCDT, ExportDCS, RepIntegration, RepTransfer, RepAzure, ComINT]
log_files: [CDTServiceLog_.txt, DcsServicePalLog_.txt, IntegrationServiceLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["iRep snapshot staged 2026-11-11", "MS-REP snapshot staged 2026-11-11"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# sync+ export flow — from a changed row to a packet in transit

This flow follows one changed PAL row through ExportCDT and ExportDCS until SmartSync takes the packet. Each stage leaves a trace in a REP2X table or a folder. The "where is it stuck" table tells you which stage holds the row and which card applies. Office-to-vessel and vessel-to-office use the same steps; only the office or vessel query variants and the paths differ.

## Stages

There are eight stages. Every stage after the first has a database or folder trace you can check read-only. Keywords: export stages, record sync, record vessel sync, packet counter, outbox, OutPacketHd, transfer.

| # | Stage | Service | Trace (read-only check) | Code |
|---|---|---|---|---|
| 1 | The row changes in PAL; change tracking records it | SQL Server | `CHANGETABLE` for the table; the table appears in `sys.change_tracking_tables` | — |
| 2 | CDT inserts the changed ids into record sync | ExportCDT | Rows in REP2X `REP.REP_RECORD_SYNC` for the table id | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L56` |
| 3 | The last extracted version is saved | ExportCDT | `REP.REP_LAST_EXT_CDT_VERSION` / `REP.REP_CDT_VERSION` moves forward | L59-L78 |
| 4 | The row is routed per vessel | ExportCDT | Rows in `REP.REP_RECORD_VESSEL_SYNC` (or the attachment variant); the record-sync rows are deleted | L122-L159 |
| 5 | DCS builds the vessel packet | ExportDCS | A packet file in the temporary or generated folder | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L243-L298` |
| 6 | The packet moves to the outbox and the counter increases | ExportDCS | Files in the vessel outbox path; the vessel counter in `REP.REP_EXPORT_OUT_PACKET_NUMBER` increases | L485-L497 |
| 7 | Hand-off to transfer | ExportDCS → RepIntegration `Integration/TransferGeneral` → RepTransfer | IntegrationServiceLog and TransferServiceLog lines for the packet name | L504-L512 |
| 8 | The packet is recorded | ExportDCS | A row in `REP.REP_OUT_PACKET_HD` | L538-L542 |

SmartSync uploads the packet afterwards (FLW-PR-EXPORT describes the shared transport steps, CMP-REPAZURE the upload).

## Where is it stuck

Find the last stage that has a trace. The next stage is where it stopped. Keywords: where is it stuck, export stuck, sync+ data not sent.

| Last trace found | Most likely cause | Card |
|---|---|---|
| No row in REP_RECORD_SYNC for a changed table | Change tracking is off for the table, the CDT query failed, the table is not in EXPORT_TABLE_ORDER, the replica type is disabled, or CDT is not running | ISS-IREP-CDT-001, ISS-IREP-CFG-001, ISS-IREP-STUCK-001 |
| Rows stay in REP_RECORD_SYNC across cycles | The routing query is missing or invalid, CheckCdtVersion failed, the read-only replica lags, or GetMaxId failed | ISS-IREP-CDT-002, ISS-IREP-CDT-003 |
| Rows in REP_RECORD_VESSEL_SYNC, no new packet | The DCS start gate is closed (config status, DCS busy, export queue), the awaiter is waiting, the vessel is invalid or skipped, or unique code/id is missing | ISS-IREP-DCS-001, ISS-IREP-DCS-002, ISS-IREP-DCS-004 |
| Rows held in the spam tables | Spam rule (record spam settings) | CMP-EXPORTCDT § Spam entries |
| A packet was generated but is not in the outbox | File move failed (folder, rights, disk) | ISS-IREXP-FILE |
| A packet is in the outbox but the counter did not increase | Counter update failed (the vessel loop aborts; the packet is regenerated later) | ISS-IREXP-SEQUENCE |
| Packet in the outbox, OutPacketHd row present, nothing in the Integration log | Transfer hand-off failed; waiting for resend | ISS-IREP-DCS-003 |
| Integration or Transfer log shows the packet | Transport side | ISS-INTEG-*, ISS-TRANSFER-001, ISS-SYNC-TRANSPORT |

## Ordering facts that matter

Three ordering facts explain most data-loss and gap reports. Keywords: order, version saved, counter before transfer, resend.

1. **CDT saves the extracted version before routing** (stages 3-4). Rows that fail routing are not lost while REP_RECORD_SYNC keeps them. Do not delete REP_RECORD_SYNC rows by hand.
2. **DCS increases the vessel packet counter before transfer** (stage 6 before 7). A packet whose transfer fails is still counted. If resend later gives up, the receiver stops at that counter (ISS-IREP-DES-002).
3. **A transfer failure does not fail the export.** DCS returns success after logging "Packet Transfer Failed" (`ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L549`). Delivery relies on auto resend (`REP_RESENT_LIMIT`, `REP_RESENT_AWAIT_TIME_IN_MIN`) and the directory resend.

## Related

PLT-IREP, CMP-EXPORTCDT, CMP-EXPORTDCS, CMP-REPINTEGRATION, DATA-IREP, FLW-IREP-IMPORT
