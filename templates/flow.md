---
doc_id: FLW-<NAME>               # e.g. FLW-PR-EXPORT
type: flow
mechanism: [priority-replication]
direction: office-to-vessel      # office-to-vessel | vessel-to-office | vessel-to-vessel | both
runs_on: [office, vessel]
components: []
sources: ["MS-REP @ <commit or snapshot date>"]
status: draft
author: claude
reviewed_by: ""
last_verified: YYYY-MM-DD
---

# <Flow name>

<2–3 sentences: what moves, from where to where, what "done" looks like.>

## Steps at a glance

<Numbered list: step → service → route/SP → where state is recorded. One line each.>
Keywords: ...

## Step N — <name>

<One summary sentence. What happens, which status/table changes, which log shows it, how it fails.>
Keywords: ...

## How to tell where a packet is stuck

<Table: last thing you see → stuck between → check.>
Keywords: ...

## Related
