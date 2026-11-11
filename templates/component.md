---
doc_id: CMP-<SERVICE>            # e.g. CMP-REPSBUS
type: component
mechanism: [smartsync]           # smartsync | priority-replication | irep (from labels.yaml)
group: smartsync-transport       # from labels.yaml groups
runs_on: [office, vessel]
components: [RepSbus]
log_files: [SbusLog_.txt]
error_types: []                  # ErrorTypeCatalog codes, if known
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP @ <commit or snapshot date>"]
status: draft
author: claude
reviewed_by: ""
last_verified: YYYY-MM-DD
---

# <Service> — <what it does in five words>

<2–3 sentences: what it does, who calls it, what breaks if it is down.>

## Role in replication

<One summary sentence.>
Keywords: ...

## How it runs

<Hosting, background worker loop (interval key, steps in order), or "API only — runs only when called".>
Keywords: ...

## API routes

<Table: route | called by | purpose | source>
Keywords: ...

## Calls to other services and the database

<Table: target | route or SP | when | source>
Keywords: ...

## Configuration

<Table: key (appsettings or CO_Parameters) | effect | source. Names only, no values.>
Keywords: ...

## Logs and what to look for

<Log file, important messages (exact template), what each means.>
Keywords: ...

## Common failure points

<Bullets, each pointing to an issue card id if one exists.>
Keywords: ...

## Related

- ...
