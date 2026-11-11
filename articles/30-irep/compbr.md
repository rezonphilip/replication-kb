---
doc_id: CMP-COMPBR
type: component
mechanism: [irep]
group: irep-inspection
runs_on: [office, vessel]
components: [ComPBR]
log_files: [PbrServiceLog_.txt]
error_types: [packet, file, db]
applies_to_versions: ["Not determined from code"]
sources: ["iRep snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# ComPBR — packet inspection and reporting

ComPBR reads sync+ packet folders and the REP2I/REP2X packet tables to produce consolidated packet information: which vessel, which counter, which tables and files. It also records packet ids against packet headers. It does not move data between office and vessel, so a ComPBR failure does not stop replication. It does remove a source of packet visibility.

## How it runs

A timer calls `RepImportSync` every `SchedulerIntervalInMinutes` (`ComPBR/Mariapps.PAL.RepComPBR/WorkerService.cs#L48-L65`). Keywords: PBR worker, packet browser, zip file data, GetAndWriteZipFileData.

- **The worker loop catches only cancellation** (L67). An unhandled exception ends the worker until the service restarts (ISS-IREP-STUCK-001).
- **Each run** (`ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L64-L234`):
  1. Read the database size, the replica type master, the import and export config paths, the attachment file-name columns, and the in and out packets (L107-L123).
  2. Open each packet zip and read its header and contents.
  3. Resolve the packet header id (L212) and mark it (L234).
- **Route `GetAndWriteZipFileData`** (`ComPBR/Mariapps.PAL.RepComPBR/Controllers/RepComPBRController.cs#L42`). It reads one zip and writes its consolidated data to files (`ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L607`, L930). Processed zips are marked (L845).
- **services.json** names a service `RepExportDCSU_tility` with endpoint `RepDcs/Value` (`ComPBR/Mariapps.PAL.RepComPBR/services.json`). The name looks mistyped and no matching route exists in ExportDCS. Not determined from code: whether ComPBR uses it.
- **EvaluateConfig** checks the queue table columns, the database-size and replica-type procedures, the client identity, and the config paths (`ComPBR/Mariapps.PAL.RepComPBR/BL/ConfigEvaluationBL.cs#L95-L582`). This is a useful read-only probe of REP2I health.

## Failures

All ComPBR templates map to ISS-IRPBR-* cards; the PACKET and FILE classes are the largest. Keywords: PBR errors, zip read error.

Typical causes:

- an unreadable or partial zip — the transfer is still in progress or the file is corrupt;
- a missing config path;
- a REP2I query failure.

None of them block replication. Treat them as reporting gaps unless the same packet also fails in ImportDES.

## Related

PLT-IREP, CFG-IREP, FLW-IREP-IMPORT
