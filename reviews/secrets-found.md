# Secret-like content found in source snapshots

Each entry gives a path and a key name only. Values were never copied. Give this list to the platform team so they can rotate and move the values to secure configuration.

## iRep snapshot (2026-11-11)

| File (relative to the iRep root) | What | Severity |
|---|---|---|
| `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/LogDataAnalytics.cs` L29-L30 | Hard-coded Log Analytics workspace id and shared key | High: a key in source code |
| `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/LogDataAnalytics.cs` L29-L30 | Same pattern (copied class; ExportDCS has no such class) | High |
| `ImportDSC/Mariapps.PAL.RepImportDSC.DAL/Repository/LogDataAnalytics.cs` L30-L31 | Same pattern | High |
| `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/LogDataAnalytics.cs` L29-L30 | Same pattern | High |
| `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/LogDataAnalytics.cs` L29-L30 | Same pattern | High |
| `ImportDSC`, `ImportRBP`, `ComPBR` → `appsettings.json` `ApplicationInsights:ConnectionString` | Application Insights connection string or instrumentation key | Medium |
| `ExportCDT/Mariapps.PAL.RepExportCDT/appsettings.json` `AlertMailConfiguration` (To, Cc, Bcc) | Personal e-mail addresses | Low (personal data) |
| `ComINT/Mariapps.PAL.ComINT/CacheSettings.json` | Internal cache host and port | Low |
| `ComINT/Mariapps.PAL.ComINT/appsettings.json` `ConnectionStringSettings[]`, `ConnectionStrings` | Connection strings, if filled; the staged copy should be checked | High if filled |

## Runtime exposure (code behaviour, not stored values)

- `ComINT/GetDbConfigurationDetails` returns all connection strings over HTTP (CMP-COMINT, Q34).
- ExportCDT (`RepExportCDTBL.cs` L163; `DBConnectionAggregator.cs` L49) and ImportRBP (`RepImportRBPBL.cs` L184) write connection-string fields into Error log lines when the settings are invalid. Log files from these services must be handled as sensitive.
- ImportRBP writes application API response bodies into the log (`RepImportRBPBL.cs` L691).

## MS-REP snapshot

The MS-REP code has no `LogDataAnalytics` class with hard-coded keys. MS-REP secrets live in `CO_Parameters` and credential tables; see DATA-MSREP-SETTINGS. Presence checks only.
