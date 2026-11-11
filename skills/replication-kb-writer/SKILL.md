---
name: replication-kb-writer
description: Write or update the Replication Troubleshooting KB (articles, issue cards, scripts, dictionaries) from a replication source repository such as MS-REP, iRep or Task Scheduler.
---

# Replication KB writer

Use this when asked to document a replication repository, add or improve KB articles or issue cards, or turn an incident into KB content for the ReplicationDashboard knowledge base.

## Before anything

1. Read `BRIEF.md` in the KB repo. Its rules win over anything here.
2. Read `dictionaries/labels.yaml` and `dictionaries/identifiers.yaml`. Use names exactly as listed.
3. Read `reviews/open-questions.md` so you do not re-ask answered questions or guess unanswered ones.

## Processing a repository (or a new version of one)

1. **Extract, don't read everything.** Run
   `python3 -I tools/extract.py <repo_root> <work>/extract.json`
   then write or update `tools/groups-<repo>.yaml` (service → group, as confirmed by the platform team) and run
   `python3 -I tools/gen_inventory.py <work>/extract.json <repo> tools/groups-<repo>.yaml .`
   This produces `inventory/<repo>.md` and `inventory/<repo>-logs.md`. Never hand-edit these.
   If the repo has SQL deployment scripts (folders like `PAL.DatabaseScripts.Office/Vessel`), also run
   `python3 -I tools/extract_sql.py <work>/sql.json <script_root> [...]` and
   `python3 -I tools/gen_db_inventory.py <work>/sql.json <work>/extract.json <repo> .` → `inventory/<repo>-db.md`.
   Stage Office scripts fully; for Vessel stage only files that differ in size or exist only there. Skip binaries and production data dumps.
2. **Find the moving parts.** Grep for `BackgroundService`/`WorkerService`, `Task.Delay`, and orchestration classes. Services without a hosted service run only when called — say so.
3. **Read the code paths that matter** (worker loops, queue handlers, controllers, the BL methods they call) and note exact line numbers as you go.
4. **Write in this order:** platform/group overview → hand-written component articles for orchestrators, transport and gateways → generated-plus-summary articles for simple step services → flow articles with a "where is it stuck" table → config index → issue cards.
5. **Issue cards:** build signatures only from logger templates in `inventory/<repo>-logs.md`; use .NET regex syntax (`(?<name>...)`). Write 20–50 phrasings in support-engineer language (typos, ship/office wording). Every solution step states who, whether it needs approval, and how to verify.
6. **Scripts:** read-only only; never select secret values — report `PRESENT/EMPTY/MISSING` instead. Each `.sql` gets a `.yaml` with `result_rules`.
7. **Unknowns** go to `reviews/open-questions.md` as numbered questions and are written as `Not determined from code.` in the article.

## Checks before handing over

Run `python3 -I tools/validate.py . <repo_root>` and fix everything it reports:
cited files/lines exist, every signature regex matches the cited source line, no secret-like strings, YAML parses, ≥ 20 phrasings per card.

Also check by eye: every `##` section opens with one summary sentence and a `Keywords:` line; nothing claims more than the cited code shows; general knowledge that is not from the code is labelled as such.

Write `reviews/<date>-<repo>.md` listing what was produced, what to review first, and gaps. Leave every file `status: draft`.

## Lessons from the MS-REP pilot

- In-memory "already running" flags with expiry times are a recurring failure pattern (RepIntegration, RepAzure). Document the flag, the expiry, and that a restart clears it.
- Many services load their settings through another service (MS-REP transport → RepDBLogW). Put "check the gateway first" in distinguishing checks.
- YAML: quote any value that starts with a backtick or quote, or contains `: `.
- Line numbers drift; cite the line of the logger call itself and let the validator confirm it.
- User-provided architecture can differ from what the code shows — record the difference as an open question rather than silently choosing one.
- SQL scripts can be UTF-16 or Latin-1: always decode before grepping, and cite the raw file line, not a filtered line number.
- Queue procedures hold the operational truth: look for `DATEADD(... -N ...)` resets and `STATUS` transitions, and document each timer in the status-codes article.
- Secrets may sit outside CO_Parameters (e.g. a credentials table read by a settings procedure). Read the settings procedures before writing "where is this key stored", and make presence scripts check every source.
- Code that is commented out (e.g. a validation call) changes behaviour: check the call site, not only the procedure.
