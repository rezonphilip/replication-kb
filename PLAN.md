# Replication Troubleshooting KB — plan (revised 2026-11-11 after iRep)

This plan replaces the pilot plan. It reflects what processing MS-REP and iRep showed: there are three mechanisms, there are thousands of failure points, most warnings are invisible at the default log level, and many failures are silent. The aim is unchanged. Support staff identify a replication problem and its fix from the ReplicationDashboard with **no AI at runtime**, and the knowledge behind that is generated and reviewed in local Claude sessions.

## 1. What changed and why

Processing iRep showed that "a card per known incident" leaves most failures uncovered. Every failure point in the code now needs a home.

| Finding | Consequence for the plan |
|---|---|
| Three mechanisms (PR, sync+, sync) share services and logs | Every item carries a `mechanism` label. Articles say which mechanism a log line belongs to. Transport cards are shared. |
| 2438 distinct failure points (1569 MS-REP, 871 iRep) | A **failure-point catalogue** is the identification layer. Cards are the explanation layer. |
| Serilog minimum level is Error in every service | Each failure point records `visible_by_default`. Hidden ones need state checks or a temporary level change (ISS-IREP-LOG-001). |
| Normal status lines are logged at Error level | A **benign list** (ISS-PLATFORM-BENIGN) suppresses them, so they do not raise alarms. |
| Many failures leave no error at all: in-memory run flags without expiry, a transfer failure that still returns success, skipped rows, counter gaps | **State probes** (read-only DB checks and EvaluateConfig routes) are first-class. Logs alone are not enough. |
| Configuration is spread over appsettings, services.json, CO_Parameters/REP parameters and ComINT | One config index per mechanism (CFG-*). Presence-only checks. |

## 2. Identification layers (how the dashboard decides)

The dashboard checks four layers in order and shows every card that matches, ranked. Keywords: identification, matching, ranking.

1. **Log signatures.**
   - New log lines go through `catalog/failure-points.yaml`, in the order hand cards, then the benign list, then the class cards. A match gives the card, the confidence and the code location.
   - Ranking prefers the hand card, then the higher log level, then the longer regex.
   - Lines that match nothing are counted and listed as "unrecognised". That list is the main input for the next KB pass.
2. **State probes.**
   - Read-only checks on a schedule:
     - queue ages (REP_RECORD_SYNC, REP_RECORD_VESSEL_SYNC, DES queues, `_REP` tables);
     - sender versus receiver counter gaps;
     - skip and error tables;
     - the EvaluateConfig and ReadAllCacheKeyValues routes.
   - Each probe result maps to a card (DATA-IREP § read-only checks; the MS-REP status-code articles).
   - This is how silent failures are found.
3. **Absence rules.** "No new log line from service X for more than 2 cycle intervals" → ISS-IREP-STUCK-001 or ISS-INTEG-001. "Queue moving but no errors" → nothing. "Queue not moving and no errors" → ISS-IREP-LOG-001 and the stuck cards.
4. **Text search.** For the support engineer's own words, the dashboard combines:
   - keyword and synonym search (dictionaries, `Keywords:` lines, phrasings);
   - the local ONNX semantic model over sections and phrasings.

## 3. Content model

Each layer has an owner and a generator. Keywords: content model, generated, hand-written.

| Item | Produced by | Edited by hand? |
|---|---|---|
| `inventory/*.md` (routes, SPs, settings, log templates, DB objects) | `tools/extract.py`, `gen_inventory.py`, `extract_sql.py`, `gen_db_inventory.py` | No |
| `catalog/failure-points.yaml`, `inventory/failure-points.md` | `tools/gen_failure_points.py` + `tools/failure_rules.yaml` | No (edit the rules) |
| Class cards `ISS-<GROUP>-<CLASS>` | `tools/gen_class_cards.py` | No (edit the generator) |
| Hand cards `ISS-<AREA>-NNN`, `ISS-PLATFORM-BENIGN` | Claude session + review | Yes |
| Articles (platform, component, flow, data, config) | Claude session + review | Yes |
| `catalog/scripts/*.sql` + rules | Claude session + review | Yes (read-only SQL only) |
| Dictionaries | Claude session + review | Yes |

## 4. Coverage targets ("everything is marked")

Coverage is measured, not estimated. `tools/validate.py` and `inventory/failure-points.md` report it. Keywords: coverage, CI, exhaustive.

- 100% of failure points have a card. This is now met: 2438 of 2438.
- Every failure point classed GENERIC is reviewed and either reclassified or given a hand card. Open: 205 remain across the groups.
- Hand cards exist for each group's top failure points by expected frequency. Today: 14 iRep hand cards plus the benign card, and 11 MS-REP hand cards. Next: MS-REP receive and send groups.
- Every hand card has at least 20 phrasings, at least one signature or an explicit absence rule, distinguishing checks, and solutions with who, approval and verification.
- Every state probe in DATA-* has a read-only script in `catalog/scripts/`, with PRESENT/EMPTY/MISSING rules where values are secret.
- CI check: on every KB change, run `validate.py` (citations, regex against the source line, secrets, phrasings, failure point → card, related docs). When a new code snapshot arrives, rerun the extract → catalogue → class-card chain and review the diff. New failure points show up as new FP ids.

## 5. Next passes

The order follows the value to support. Each pass ends with `validate.py` showing 0 issues and a review log. Keywords: roadmap, next steps.

1. **Review the iRep content** with the platform team, starting with the open questions Q-IREP-*: acronyms, the RepAzure → DES hand-off, `ImportDes/ValidatePacket`, DBO versus REP seed tables, and whether the PAL table creation in DSC is intended.
2. **Write the state-probe scripts** for sync+ (queue ages, counter gaps, `_REP` growth, skip tables) and MS-REP (status-code ages), with result rules that point to cards.
3. **Hand cards for the large class buckets**: SYNC-TRANSPORT, INTEG-DB, PRRECV-FILE, IRIMP-DATAAPPLY, PRRECV-PACKET, IRIMP-DB. Split each bucket into specific problems where the code shows distinct causes.
4. **Collect real logs** from 2-3 sites (sanitised), then run the catalogue over them. This measures the unrecognised rate and the real frequency, and adds sample-log signatures.
5. **Task Scheduler** repository (the next mechanism), using the same pipeline.
6. **Dashboard integration contract**: the JSON export of the catalogue, cards and probes. Ranking rules as in § 2.

## 6. Rules that do not change

- No runtime AI.
- No secrets or configuration values in the KB; key names only.
- Read-only scripts.
- Remote or data-changing actions need explicit approval.
- Everything stays `status: draft` until a human reviews it.
- The ticketing system stays separate.
