# Replication Troubleshooting Knowledge Base

Source content for the ReplicationDashboard KB portal (`/kb`) and its non-AI issue identification. Written in local Claude sessions, reviewed by humans, pulled by the dashboard.

**Start here:** `BRIEF.md` (rules every writer follows).

| Folder | Contents |
|---|---|
| `inventory/` | Script-extracted facts per repository (routes, SPs, parameters, log templates, database objects). Articles cite these. |
| `articles/00-platform` | How the platform fits together. |
| `articles/10-smartsync-transport` | SmartSync transport (RepSbus, RepAzure, RepAzureRes) and the RepTransfer adapter. |
| `articles/20-priority-replication` | RepIntegration (orchestrator), RepDBLogW, and the Priority Replication step services. |
| `articles/30-irep` | iRep (not yet written). |
| `articles/60-data` | Database: script layout, settings tables, status codes and automatic resets, resend and missing-packet rules. |
| `articles/70-flows` | End-to-end flows with "where is it stuck" tables. |
| `articles/90-config` | Configuration and parameter references. |
| `issues/` | Issue cards: phrasings, regex signatures, distinguishing checks, solution checklists. |
| `catalog/scripts/` | Read-only diagnostic SQL + rules for reading results. |
| `dictionaries/` | Allowed labels, synonyms, canonical identifiers. |
| `templates/` | Templates for articles, flows and issue cards. |
| `reviews/` | Review logs and open questions. |
| `skills/replication-kb-writer/` | The skill Claude sessions load to write here (copy into `.claude/skills/` locally to use it in Claude Code). |

Pilot status (2026-11-11): MS-REP code and MS-REP database scripts, all content `draft`.
