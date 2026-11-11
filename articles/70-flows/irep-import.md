---
doc_id: FLW-IREP-IMPORT
type: flow
mechanism: [irep, smartsync]
group: irep-import
runs_on: [office, vessel]
direction: both
components: [RepAzure, RepDBLogW, ImportDES, ImportDSC, ImportRBP, ComINT]
log_files: [AzureService_.txt, DbLogServiceLog_.txt, DesServiceLog_.txt, DscServiceLog_.txt, RbpServiceLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["iRep snapshot staged 2026-11-11", "MS-REP snapshot staged 2026-11-11"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# sync+ import flow — from a downloaded packet to a row in PAL

This flow follows one received sync+ packet: SmartSync download, the DES validate queue, the process queue and REP2I replica tables, and finally RBP applying the rows to PAL through the application endpoint. Every stage leaves a database or folder trace, and the "where is it stuck" table maps the last trace to a card.

## Stages

There are nine stages. Every stage after the download has a trace you can check read-only. Keywords: import stages, validate queue, process queue, replica table, _REP, proc live data, RBP.

| # | Stage | Service | Trace (read-only check) | Code |
|---|---|---|---|---|
| 1 | The packet is downloaded from Azure | RepAzure | A download row and the file in the iRep inbox (import config path) | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L434-L469` |
| 2 | The packet is queued for validation | RepDBLogW `SaveIRepValidateFile` | A row in REP2I `REP.REP_DES_VALIDATE_QUEUE` | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/DBlogWBL.cs#L42` |
| 3 | Validation: vessel config, packet counter, name, splits | ImportDES validate | The row leaves the validate queue; files move to in-temp | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L100-L420` |
| 4 | The packet is queued for processing; the in-packet counter is updated | ImportDES | A row in `REP.REP_DES_PROCESS_QUEUE`; the vessel counter moves in `REP.REP_IMPORT_IN_PACKET_NUMBER` | L488-L542 |
| 5 | Schema compare and replica table create/alter | ImportDSC | REP2I table exists; JSON schema file exists | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L358` |
| 6 | Rows are read into the replica tables | ImportDES read | Rows in `<table>_REP` / `<table>_REP_DEL`; `REP.REP_DES_PROC_LIVE_DATA` entries | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L128-L229` |
| 7 | RBP is triggered | ImportDES → ImportRBP `RepImportSync` | RbpServiceLog shows a cycle | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L276-L278` |
| 8 | Rows are posted to the application endpoint | ImportRBP | Application data visible in PAL | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L546` |
| 9 | The processed replica rows are deleted; the queue is completed | ImportRBP | `_REP` rows gone; queue status completed | L550, L437 |

ComPBR reads the same packet folders and tables for reporting only (CMP-COMPBR).

## Where is it stuck

Find the last stage that has a trace. The next stage is where it stopped. Keywords: where is it stuck, import stuck, sync+ data not received, data not in PAL.

| Last trace found | Most likely cause | Card |
|---|---|---|
| Packet not downloaded | Transport side (Azure, Service Bus, network) | ISS-SYNC-TRANSPORT, ISS-AZURE-001 |
| File in the inbox, no validate-queue row | The RepAzure → RepDBLogW hand-off (the class is not in the staged source), or RepDBLogW is down | ISS-DBLOGW-DB, open question |
| Validate-queue row stays | Config status false, validate flag stuck, vessel on the skip list, a counter gap, or split files missing | ISS-IREP-DCS-001, ISS-IREP-DCS-002, ISS-IREP-DES-002, ISS-IREP-DES-001 |
| Validate-queue row gone, packet in the error folder | Name or identity mismatch, or an old (already applied) counter | ISS-IREP-DES-001 |
| Process-queue row stays | Read flag stuck, read exception, DSC failure | ISS-IREP-STUCK-001, ISS-IREP-DES-003 |
| Some rows missing from `_REP` | Bulk rows rejected or skipped (schema drift) | ISS-IREP-DES-003 |
| Rows stay in `_REP` / `_REP_DEL` | RBP not called (`InvokeRbpService` off), RBP disabled, no endpoint, application API failing, RBP token stuck | ISS-IREP-RBP-001, ISS-IREP-STUCK-001 |
| Rows were applied but reappear | Processed-row delete failed; reprocess picks them up again | ISS-IREP-RBP-001 |

## Ordering facts that matter

Four ordering facts explain most gap and data reports. Keywords: order, counter gap, skip until next cycle, reprocess.

1. **Packets are applied strictly in counter order per vessel.** A gap stops that vessel. The other vessels continue (`ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L293-L328`).
2. **Old packets are removed quietly.** A packet whose counter is already applied is deleted from the queue and moved to the error path, logged at Information only.
3. **Rejected rows are skipped, not retried, within the packet.** Bulk writes retry in smaller parts and then skip only the bad rows. The skipped rows are logged with `[DATA_SKIPPED]` and need a reprocess after the fix.
4. **RBP keeps rows until the application accepts them.** A failing endpoint makes `_REP` tables grow. Reprocess runs every `RepreocessIntervalInHours` hours (default 12).

## Related

PLT-IREP, CMP-IMPORTDES, CMP-IMPORTDSC, CMP-IMPORTRBP, CMP-REPAZURE, CMP-REPDBLOGW, DATA-IREP, FLW-IREP-EXPORT
