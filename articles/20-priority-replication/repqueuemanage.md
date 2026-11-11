---
doc_id: CMP-REPQUEUEMANAGE
type: component
mechanism: [priority-replication]
group: pr-send
runs_on: [office, vessel]
components: [RepQueueManage]
log_files: [QueueManagerLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepQueueManage — queue counts and limits

RepQueueManage keeps queue counts and enforces total and per-channel queue limits (`GetQueueCount`, `AddOrUpdateQueueCount`). When limits are reached, new work waits.

## Role in replication

RepQueueManage is a Priority Replication send-side step with no timer of its own: it runs only when called over HTTP (no hosted background service found in the project). Keywords: RepQueueManage, queuemanage, priority replication, send side, queue counts and limits.

- Limits: `[REP].[PR_REP_GET_TOTAL_QUEUE_LIMIT]`, `[REP].[PR_REP_GET_CHANNEL_QUEUE_LIMIT]`.

## API routes

Controller routes and their source lines. Keywords: RepQueueManage routes, API, TestService.

| Route | Source |
|---|---|
| `QueueManage` | `RepQueueManage/MariApps.PAL.Rep.QueueManage.Service/Controllers/QueueManageController.cs#L16` |
| `GetQueueCount` | `RepQueueManage/MariApps.PAL.Rep.QueueManage.Service/Controllers/QueueManageController.cs#L30` |
| `AddOrUpdateQueueCount` | `RepQueueManage/MariApps.PAL.Rep.QueueManage.Service/Controllers/QueueManageController.cs#L87` |
| `TestService` | `RepQueueManage/MariApps.PAL.Rep.QueueManage.Service/Controllers/QueueManageController.cs#L149` |
| `GetVersion` | `RepQueueManage/MariApps.PAL.Rep.QueueManage.Service/Controllers/QueueManageController.cs#L157` |

## Database and parameters

Stored procedures and CO_Parameters keys this service uses (names only). Keywords: RepQueueManage stored procedure, CO_Parameters, REP schema.

- `[REP].[PR_REP_GET_CHANNEL_QUEUE_LIMIT]` — `RepQueueManage/MariApps.PAL.Rep.QueueManage.DAL/QueueManageRepository.cs#L41`
- `[REP].[PR_REP_GET_TOTAL_QUEUE_LIMIT]` — `RepQueueManage/MariApps.PAL.Rep.QueueManage.DAL/QueueManageRepository.cs#L23`

Parameters: none found.

## Logs and what to look for

Log: `Logs/QueueManagerLog_.txt`. Error-type messages found in code (first 10; full list in `inventory/ms-rep-logs.md` → RepQueueManage). Keywords: QueueManagerLog_.txt, RepQueueManage error, failed.

| Message (template) | Source |
|---|---|
| none found | |

What each message means in practice: Not determined from code beyond the text itself — to be filled from incident history.

## Related

- PLT-MSREP-OVERVIEW, CMP-REPINTEGRATION, FLW-PR-EXPORT
