---
doc_id: CMP-COMINT
type: component
mechanism: [irep]
group: irep-config
runs_on: [office, vessel]
components: [ComINT]
log_files: [ComINTServiceLog_.txt]
error_types: [config, http]
applies_to_versions: ["Not determined from code"]
sources: ["iRep snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# ComINT — configuration gateway for sync+

ComINT answers one question for every other sync+ service: "which databases belong to each replica type?". It returns the `ConnectionStringSettings` list from its own appsettings (replica type id, name, primary and read-only connection strings, enabled flag). If ComINT is down or its list is wrong, ExportCDT, ExportDCS, ImportDES, ImportDSC and ImportRBP all fail at the configuration step.

## What it does

ComINT has a single route and no database access of its own. Keywords: GetDbConfigurationDetails, ComINT_Utility, CommonIntegration, connection settings, replica type list.

- Route: `POST ComINT/GetDbConfigurationDetails` (`ComINT/Mariapps.PAL.ComINT/Controllers/ComINTController.cs#L27-L31`).
- The route returns the in-memory list as it is (`ComINT/Mariapps.PAL.ComINT/BL/ComINTBL.cs#L20-L22`).
- The list is loaded once at startup from the `ConnectionStringSettings` section (`ComINT/Mariapps.PAL.ComINT/Startup.cs#L39`). **A change to that section only takes effect after a ComINT restart.**
- Callers name ComINT differently in their services.json:
  - `ComINT_Utility` in ExportCDT, ImportDSC and ImportRBP;
  - `CommonIntegration` in ExportDCS and ImportDES.

  The route itself is the same everywhere.

## Worker service

ComINT has a hosted worker, but it does no replication work. Keywords: ComINT worker, default delay 15 mins, Process started.

The worker logs "Process started" at Error level. It then waits once (`SchedulerIntervalInMinutes`, or 30 minutes if that is 0) and returns (`ComINT/Mariapps.PAL.ComINT/WorkerService.cs#L44-L62`). The text "default delay of 15 mins interval set for worker service" is also logged at Error level, but the code waits 30 minutes. Both lines are benign (ISS-PLATFORM-BENIGN).

## Configuration keys

These are the key names only; values are environment-specific and some are secret. Keywords: ConnectionStringSettings, ReplicaTypeId, IsEnabled, CacheSettings.

- `ConnectionStringSettings[]`, with fields `ReplicaTypeId`, `ReplicaName`, `PrimaryDB`, `ReadOnlyDB`, `IsEnabled` (`ComINT/Mariapps.PAL.ComINT/appsettings.json#L43-L60`).
- `ConnectionStrings` (`PrimaryDB`, `ReadOnlyDB`, `AzureDB`), `BasicSettings`, `WorkerServiceSettings` (`ComINT/Mariapps.PAL.ComINT/Startup.cs#L32-L34`).
- `CacheSettings.json` holds a cache host address. Security: it is an internal address, so do not copy it into tickets.

## Failure modes

If ComINT fails, every sync+ service stops in the same cycle with configuration errors. Keywords: ComINT down, connection string not fetched, services.json.

| What you see | Where | Card |
|---|---|---|
| "Processing failed, not able to fetch database connectionString configurations" | CDT, RBP | ISS-IREP-CFG-001 |
| "Service ComINT_Utility not found on services.json" | CDT, DSC, RBP | ISS-IREP-CFG-001 |
| "No replica configuration loaded from common integration service" | DES | ISS-IRIMP-CONFIG |
| "ReplicaTypeId {id} not found in the configuration" | DCS, DES | ISS-IREXP-CONFIG, ISS-IRIMP-CONFIG |
| A replica type silently skipped | CDT (`IsEnabled` false) | ISS-IREP-CFG-001 |

Security: the route returns full connection strings over plain HTTP with no authentication visible in the controller. Restrict it to the server (open question).

## Related

PLT-IREP, CFG-IREP, ISS-IREP-CFG-001
