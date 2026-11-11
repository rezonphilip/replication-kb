---
doc_id: CMP-REPFILEMERGE
type: component
mechanism: [priority-replication]
group: pr-receive
runs_on: [office, vessel]
components: [RepFileMerge]
log_files: [FileMergeLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepFileMerge — joins split parts

RepFileMerge joins the split parts of a packet back into one zip (`Merge/FILE`, `Splits`). If a part is missing the merge cannot complete and the import item stays pending or fails.

## Role in replication

RepFileMerge is a Priority Replication receive-side step with no timer of its own: it runs only when called over HTTP (no hosted background service found in the project). Keywords: RepFileMerge, filemerge, priority replication, receive side, joins split parts.

- Works under `REP_OFF_ROOT`. RepIntegration logs `File Merge Service failed for Import Item {Id}` when this step fails (`RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L746`).

## API routes

Controller routes and their source lines. Keywords: RepFileMerge routes, API, TestService.

| Route | Source |
|---|---|
| `Merge` | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/Controllers/FileMergeController.cs#L16` |
| `FILE` | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/Controllers/FileMergeController.cs#L34` |
| `Splits` | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/Controllers/FileMergeController.cs#L60` |
| `TestService` | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/Controllers/FileMergeController.cs#L88` |
| `GetVersion` | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/Controllers/FileMergeController.cs#L96` |

## Database and parameters

Stored procedures and CO_Parameters keys this service uses (names only). Keywords: RepFileMerge stored procedure, CO_Parameters, REP schema.

- `REP.PR_GET_PARAM_DATA` — `RepFileMerge/MariApps.PAL.Rep.FileMerge.DAL/FileMergeRepository.cs#L26`
- `REP.PR_GET_TRANSFER_DATA` — `RepFileMerge/MariApps.PAL.Rep.FileMerge.DAL/FileMergeRepository.cs#L101`
- `REP.PR_REP_MISSING_PACKETS_OPERATIONS` — `RepFileMerge/MariApps.PAL.Rep.FileMerge.DAL/FileMergeRepository.cs#L59`
- `REP_OFF_ROOT` — `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L34`

Parameters: `REP_OFF_ROOT`.

## Logs and what to look for

Log: `Logs/FileMergeLog_.txt`. Error-type messages found in code (first 10; full list in `inventory/ms-rep-logs.md` → RepFileMerge). Keywords: FileMergeLog_.txt, RepFileMerge error, failed.

| Message (template) | Source |
|---|---|
| {MethodName} File {FileName} could not be moved to destination location as merged file is missing | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L393` |
| {MethodName}\| Critical exception while merging file | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L437` |
| {MethodName}\| Input is null | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L90` |
| {MethodName}\| One or more SplitFiles have empty FileLocation | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L150` |
| {MethodName}\| One or more SplitFiles are missing. Sample files: {MissingFiles} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L165` |
| {MethodName}\| IO Exception while combining files | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L63` |
| {MethodName}\| General Exception in combining files | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L71` |
| Exception in {MethodName} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L130` |
| {MethodName} Exception while moving file {FileName} to destination location {DestinationFolder} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L201` |

What each message means in practice: Not determined from code beyond the text itself — to be filled from incident history.

## Related

- PLT-MSREP-OVERVIEW, CMP-REPINTEGRATION, FLW-PR-IMPORT
