# Replication KB — writing brief

Read this before writing or changing anything in this repository. It is the contract every Claude session (and every human editor) follows. The `replication-kb-writer` skill in `skills/` points here.

## 1. What this KB is for

The KB is read by the ReplicationDashboard **without any AI at runtime**. The dashboard finds content by:

1. regex error signatures (`issues/*.yaml` → `signatures`),
2. keyword / synonym search (front-matter labels, section keyword lines, `dictionaries/`),
3. local semantic search over sections (small ONNX embedding model).

So every piece of text must be *findable by words a support engineer will actually type or paste*, and every section must make sense when shown on its own.

## 2. The platform in one paragraph (pilot scope)

MS-REP is a set of 19 .NET services installed on **both office and vessel**; behaviour differs by configuration and `Common.CO_Parameters` rows (for example `REP_LOCATION`). Inside MS-REP:

| Group | Services | Role |
|---|---|---|
| SmartSync transport | RepSbus, RepAzure, RepAzureRes | Azure Service Bus messaging + Azure Blob download / upload. Shared by every replication mechanism. |
| Transfer adapter | RepTransfer | Adapter over the transport: moves packets to the right outbox / medium, handles resend. Serves Priority Replication; may serve iRep transfer flows. |
| Orchestrator | RepIntegration | Drives Priority Replication end to end. For iRep it handles **only transfer** (not data preparation, ingestion or packet creation). |
| PR core / DB gateway | RepDBLogW | Database gateway of Priority Replication. iRep may call it occasionally to read data. |
| PR send side | RepProData, RepPacketCreation, RepCompression, RepSplit, RepPacketInterim, RepTrack, RepMedium, RepQueueManage | Prepare and package outgoing data. |
| PR receive side | RepAcquisition, RepFileMerge, RepDecompress, RepSaveData, RepAckn | Pick up, rebuild, apply and acknowledge incoming packets. |

## 3. Hard rules

1. **Cite everything.** Every factual statement about behaviour carries a source: `Service/Project/File.cs#L10-L40`. Paths are relative to the repository root. Put the repository and snapshot/commit once in front-matter `sources`.
2. **Never guess.** If the code does not show it, write `Not determined from code.` and add the question to `reviews/open-questions.md`.
3. **Never copy configuration values.** Name keys (`REP_SERVICEBUS_CONNECTION_STRING`, `AzureSettings:ConnectionRetryLimit`) — never their values. Defaults from `appsettings.json` may be quoted only for non-secret numeric/boolean tuning keys and must be labelled "default in repo appsettings".
4. **No secrets, ever.** Connection strings, keys, passwords, tokens, SAS URLs, hostnames of customer environments, vessel names of customers. If you see one, do not reproduce it, and flag the file in `reviews/secrets-found.md` by path only.
5. **Read-only scripts only** in `catalog/scripts/`. Anything that changes data is an *action* and goes in a solution checklist as an instruction for a human, marked `requires approval`.
6. **Status is honest.** Everything Claude writes is `status: draft`. Only a human reviewer moves it to `approved` and fills `reviewed_by`.
7. **Use the dictionaries.** Use names from `dictionaries/identifiers.yaml` exactly (service names, SP names, log file names). Add new terms there rather than inventing spellings.

## 4. Article shape

- Front-matter as in `templates/article.md`. Labels must come from `dictionaries/labels.yaml`.
- Title, then a 2–3 sentence summary a support engineer can act on.
- Every `##` section starts with **one summary sentence**, then a line `Keywords: ...` (5–12 words people would type: error text fragments, service names, synonyms).
- Sections should be 80–400 words. Split anything longer. One idea per section.
- Prefer tables for: settings, routes, log locations, status codes.
- End with `## Related` linking doc_ids.

## 5. Issue cards (`issues/*.yaml`)

Follow `templates/issue.yaml`. Each card needs:

- `symptoms` written the way users report them,
- `phrasings`: **20–50** different ways a person might describe the issue (short, long, misspelt, ship-side vs office-side wording),
- `signatures`: regexes built **only** from real log templates in `inventory/ms-rep-logs.md` (cite the source line),
- `distinguishing_checks`: how to tell this issue from look-alikes,
- `solutions`: ordered checklists; each step says who does it, whether it needs approval, and how to verify.

## 6. Process for one repository

1. Extract structure → `inventory/<repo>.md` and `inventory/<repo>-logs.md` (script, not prose). If the repo has SQL deployment scripts, also run `tools/extract_sql.py` + `tools/gen_db_inventory.py` → `inventory/<repo>-db.md`.
2. Write `00-platform` overview and per-group overview first.
3. Component article per service (template `component.md`).
4. Flow articles (template `flow.md`) for each end-to-end path.
5. Config reference (`90-config`) — keys, where read, effect. Database reference (`60-data`) — settings tables, status codes and the procedures that reset them.
6. Issue cards seeded from log error templates and known incidents.
7. Self-check (section 7) and write `reviews/<date>-<repo>.md`.

## 7. Self-check before handing over

- [ ] Every `sources` path exists in the snapshot.
- [ ] `grep` for secret-like patterns (`AccountKey=`, `Password=`, `SharedAccessKey`, `sig=`) returns nothing.
- [ ] Every label value exists in `dictionaries/labels.yaml`.
- [ ] Every `##` section has a summary sentence and a `Keywords:` line.
- [ ] Every signature regex matches at least one template in `inventory/*-logs.md`.
- [ ] Open questions are recorded, not answered by guess.
