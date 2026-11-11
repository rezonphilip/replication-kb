---
doc_id: CMP-REPDECOMPRESS
type: component
mechanism: [priority-replication]
group: pr-receive
runs_on: [office, vessel]
components: [RepDecompress]
log_files: [DecompressLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepDecompress — unzips packets

RepDecompress unzips a merged packet (`EXTRACT`, `Extract-Packet`) and records the packet's details (`PR_REP_SAVE_PACKET_DT_DATA`). Corrupt or incomplete zips fail here.

> **V2V (vessel-to-vessel) is a dropped feature.** The V2V routes, procedures and message types mentioned in this article still exist in the code and database but are not in use; do not troubleshoot them. See DATA-MSREP-OFFVSL.

## Role in replication

RepDecompress is a Priority Replication receive-side step with no timer of its own: it runs only when called over HTTP (no hosted background service found in the project). Keywords: RepDecompress, decompress, priority replication, receive side, unzips packets.

- Uses `REP_ZIP_UTILITY`, `PR_REP_ROOT`, `REP_OFF_ROOT`. RepIntegration logs `Process failed while handling Decompress service` (`.../ImportQueueProcess.cs#L868`).

## API routes

Controller routes and their source lines. Keywords: RepDecompress routes, API, TestService.

| Route | Source |
|---|---|
| `Decompress` | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/Controllers/DecompressController.cs#L18` |
| `EXTRACT` | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/Controllers/DecompressController.cs#L39` |
| `Extract-Packet` | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/Controllers/DecompressController.cs#L79` |
| `TestService` | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/Controllers/DecompressController.cs#L106` |
| `GetVersion` | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/Controllers/DecompressController.cs#L114` |

## Database and parameters

Stored procedures and CO_Parameters keys this service uses (names only). Keywords: RepDecompress stored procedure, CO_Parameters, REP schema.

- `PR_PACKET_INFO_` — `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L582`
- `PR_PARAM` — `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L718`
- `PR_REP_ROOT` — `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L718`
- `REP.PR_GET_PARAM_DATA` — `RepDecompress/MariApps.PAL.Rep.Decompress.DAL/DecompressRepository.cs#L28`
- `REP.PR_GET_TRANSFER_DATA` — `RepDecompress/MariApps.PAL.Rep.Decompress.DAL/DecompressRepository.cs#L184`
- `REP.PR_REP_MISSING_PACKETS_OPERATIONS` — `RepDecompress/MariApps.PAL.Rep.Decompress.DAL/DecompressRepository.cs#L55`
- `REP.PR_REP_SAVE_PACKET_DT_DATA` — `RepDecompress/MariApps.PAL.Rep.Decompress.DAL/DecompressRepository.cs#L84`
- `REP.PR_REP_UPDATE_PACKET_DATA` — `RepDecompress/MariApps.PAL.Rep.Decompress.DAL/DecompressRepository.cs#L107`
- `REP_OFF_ROOT` — `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L406`
- `REP_ZIP_UTILITY` — `RepDecompress/MariApps.PAL.Rep.Decompress.Service/Controllers/DecompressController.cs#L51`
- `[REP].[PR_TRACKCHANGE_NEW_TYP_V2V]` — `RepDecompress/MariApps.PAL.Rep.Decompress.DAL/DecompressRepository.cs#L373`
- `[REP].[PR_TRACKCHANGE_TYP]` — `RepDecompress/MariApps.PAL.Rep.Decompress.DAL/DecompressRepository.cs#L357`
- `[REP].[SAVE_TRACK_CHANGE_RECORD]` — `RepDecompress/MariApps.PAL.Rep.Decompress.DAL/DecompressRepository.cs#L353`
- `[REP].[SAVE_TRACK_CHANGE_RECORD_V2V]` — `RepDecompress/MariApps.PAL.Rep.Decompress.DAL/DecompressRepository.cs#L369`

Parameters: `PR_PACKET_INFO_`, `PR_PARAM`, `PR_REP_ROOT`, `REP_OFF_ROOT`, `REP_ZIP_UTILITY`.

## Logs and what to look for

Log: `Logs/DecompressLog_.txt`. Error-type messages found in code (first 10; full list in `inventory/ms-rep-logs.md` → RepDecompress). Keywords: DecompressLog_.txt, RepDecompress error, failed.

| Message (template) | Source |
|---|---|
| {MethodName}\| Input is null | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/ValidateBL.cs#L84` |
| {MethodName}\| SplitFiles is null or empty | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/ValidateBL.cs#L114` |
| {MethodName}\| FileLocation is null or file does not exist | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/ValidateBL.cs#L124` |
| Invalid LZMA header: too short | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L90` |
| {MethodName}\| File I/O error during decompression: {InFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L116` |
| {MethodName}\| Invalid data error during decompression: {InFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L120` |
| {MethodName}\| Unexpected Exception during decompression: {InFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L124` |
| {MethodName}\| Extraction attempt {Attempt}/{MaxAttempts} failed with I/O error, retrying in {DelayMs}ms: {Message} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L261` |
| {MethodName}\| All {MaxAttempts} extraction retry attempts failed for file {InputFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L270` |
| {MethodName}\| I/O error during TAR extraction: {InputFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L317` |

What each message means in practice: Not determined from code beyond the text itself — to be filled from incident history.

## Related

- PLT-MSREP-OVERVIEW, CMP-REPINTEGRATION, FLW-PR-IMPORT
