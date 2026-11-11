# Review log — MS-REP pilot, 2026-11-11

**Author:** Claude (local session). **Status of everything produced:** draft.

## What was produced

| Area | Files |
|---|---|
| Inventory (script-generated) | `inventory/ms-rep.md`, `inventory/ms-rep-logs.md` |
| Platform overview | `articles/00-platform/ms-rep-overview.md` |
| SmartSync transport + adapter | `articles/10-smartsync-transport/` — RepSbus, RepAzure, RepAzureRes, RepTransfer (hand-written) |
| Priority Replication | `articles/20-priority-replication/` — RepIntegration, RepDBLogW (hand-written); 13 step services (generated skeleton + hand-written summary) |
| Flows | `articles/70-flows/pr-export.md`, `pr-import.md` |
| Config | `articles/90-config/ms-rep-co-parameters.md` |
| Issue cards | 9 cards in `issues/` (20–34 phrasings, 4–6 signatures each) |
| Scripts | 3 read-only scripts in `catalog/scripts/` (no values returned) |
| Dictionaries | `labels.yaml`, `synonyms.yaml`, `identifiers.yaml` |

## Automatic checks run

- All cited `Service/…/File.cs#Lx` paths exist and line numbers are within the file.
- Every issue signature regex matches a real logger line in the cited file, at the cited line.
- No secret-like patterns (`AccountKey=`, `Password=`, `SharedAccessKey=`, `sig=`) in articles, issues or scripts.
- All issue YAML parses.

## What a reviewer should check first

1. The six hand-written component articles and the two flows — they carry the most interpretation.
2. Open questions Q1, Q3, Q6, Q7 (`reviews/open-questions.md`).
3. Issue card solutions: are the steps what support actually does? Add real incident phrasings.

## Gaps

- The 13 generated PR step articles list routes/SPs/errors but say little about *meaning*; they need incident knowledge.
- SQL scripts (`PAL.DatabaseScripts.*`) were not staged, so table/SP bodies are not documented.
- iRep and Task Scheduler repositories not yet processed.
