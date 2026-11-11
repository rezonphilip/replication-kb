---
doc_id: CMP-REPCOMPRESSION
type: component
mechanism: [priority-replication]
group: pr-send
runs_on: [office, vessel]
components: [RepCompression]
log_files: [Compression_Log_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepCompression — zips packets

RepCompression zips packet files (`Compress/ZIP`, batch variant `CompressBatch/ZipBatch`) using the utility named in `REP_ZIP_UTILITY`. It is a short step; failures are almost always path, disk or utility problems.

## Role in replication

RepCompression is a Priority Replication send-side step with no timer of its own: it runs only when called over HTTP (no hosted background service found in the project). Keywords: RepCompression, compression, priority replication, send side, zips packets.

- Zip utility path comes from `REP_ZIP_UTILITY`; working root from `PR_REP_ROOT`.
- Queue-based export logs `Compression failed for TableSettingsId ...` in RepIntegration when this step fails (`RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L245`).

## API routes

Controller routes and their source lines. Keywords: RepCompression routes, API, TestService.

| Route | Source |
|---|---|
| `CompressBatch` | `RepCompression/MariApps.PAL.Rep.Compress.Service/Controllers/CompressBatchController.cs#L11` |
| `ZipBatch` | `RepCompression/MariApps.PAL.Rep.Compress.Service/Controllers/CompressBatchController.cs#L26` |
| `Compress` | `RepCompression/MariApps.PAL.Rep.Compress.Service/Controllers/CompressController.cs#L11` |
| `ZIP` | `RepCompression/MariApps.PAL.Rep.Compress.Service/Controllers/CompressController.cs#L26` |
| `TestService` | `RepCompression/MariApps.PAL.Rep.Compress.Service/Controllers/CompressController.cs#L57` |
| `Version` | `RepCompression/MariApps.PAL.Rep.Compress.Service/Controllers/CompressController.cs#L65` |

## Database and parameters

Stored procedures and CO_Parameters keys this service uses (names only). Keywords: RepCompression stored procedure, CO_Parameters, REP schema.

- `PR_PARAM` — `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L42`
- `PR_REP_ROOT` — `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L42`
- `REP.PR_REP_UPDATE_PACKET_DATA` — `RepCompression/MariApps.PAL.Rep.Compress.DAL/CompressRepository.cs#L50`
- `REP_ZIP_UTILITY` — `RepCompression/MariApps.PAL.Rep.Compress.Service/Controllers/CompressController.cs#L35`
- `[REP].[PR_GET_PARAM_DATA]` — `RepCompression/MariApps.PAL.Rep.Compress.DAL/CompressRepository.cs#L24`
- `[REP].[UPDATE_EXT_PACKET_DATA]` — `RepCompression/MariApps.PAL.Rep.Compress.DAL/CompressRepository.cs#L98`

Parameters: `PR_PARAM`, `PR_REP_ROOT`, `REP_ZIP_UTILITY`.

## Logs and what to look for

Log: `Logs/Compression_Log_.txt`. Error-type messages found in code (first 10; full list in `inventory/ms-rep-logs.md` → RepCompression). Keywords: Compression_Log_.txt, RepCompression error, failed.

| Message (template) | Source |
|---|---|
| {MethodName} - Validation failed: {Error} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBatchBL.cs#L36` |
| {MethodName} - Compression failed for GroupId {GroupId} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBatchBL.cs#L93` |

What each message means in practice: Not determined from code beyond the text itself — to be filled from incident history.

## Related

- PLT-MSREP-OVERVIEW, CMP-REPINTEGRATION, FLW-PR-EXPORT
