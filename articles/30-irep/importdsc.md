---
doc_id: CMP-IMPORTDSC
type: component
mechanism: [irep]
group: irep-import
runs_on: [office, vessel]
components: [ImportDSC]
log_files: [DscServiceLog_.txt]
error_types: [dataapply, db, file, config]
applies_to_versions: ["Not determined from code"]
sources: ["iRep snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# ImportDSC — schema compare and replica table create/alter

ImportDSC keeps the REP2I replica tables in step with the table structure that arrives in packets. ImportDES calls it for each table it reads. DSC compares the incoming column list with a stored JSON schema and with the PAL table, then creates or alters the REP2I table. A table whose schema step fails will not import rows correctly.

## How it runs

ImportDSC has no worker. It works only when ImportDES calls `RepImportDSC/RepImportSchemaCompare`. Keywords: DSC, schema compare, RepImportSchemaCompare, no worker.

The hosted worker only logs a start line; its loop is commented out (`ImportDSC/Mariapps.PAL.RepImportDSC/WorkerService.cs#L35-L42`). Each comparison does the following (`ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L118-L170`):

1. Read the connection list from ComINT. If it is missing: "Connectionstring settings not found" (ISS-IREP-CFG-001).
2. Check that the replica type is in the list.
3. Lock per table entity, so two packets do not alter the same table at once (L167-L169).
4. Run the comparison.

## Comparison logic

DSC keeps one JSON schema file per table in a configured JSON directory. It compares in two directions: source (packet) against the stored JSON, and stored JSON against PAL. Keywords: JSON schema file, GetJsonPath, PalDestinationSchemaCompare, AzureTableCreation, AzureTableAlteration, difference log.

- `SchemaCompare` reads the JSON directory and the REP2I table list from the database (`ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L173-L196`).
- `PalDestinationSchemaCompare` creates the REP2I table if it does not exist (L406-L439). If the table already exists, it reads the stored JSON (L452-L476).
- `JsonExistsAndDifferenceFound` alters the REP2I table. If the alter fails, it recreates the table, then writes a difference log file (L565-L588).
- `JsonFileNotFoundButTableExistInAzure` writes a new JSON file and alters the table when it finds differences (L626-L664).
- `CreateAzureTableIfNotExistsInPAL` creates the table in PAL when the table is missing there. This logs "Table doesnot exist on PAL" (L520-L525). **This step changes the PAL schema.** Ask the platform team when it is intended (open question).

"Azure" in these names means the REP2I staging SQL database (see PLT-IREP).

## Routes

All routes are under `RepImportDSC/` (`ImportDSC/Mariapps.PAL.RepImportDSC/Controllers/RepImportDSCController.cs`). Keywords: GenerateTableSchema, CreateAzureTable, GeneratePalTableSchema, TestMethod.

| Route | Purpose | Line |
|---|---|---|
| `RepImportSchemaCompare` | Called by ImportDES | L53 |
| `GenerateTableSchema`, `GeneratePalTableSchema` | Regenerate the JSON schema files from PAL | L95, L137 |
| `CreateAzureTable` | Create a REP2I replica table | L126 |
| `TestMethod` | Lists REP2I tables (diagnostic) | L78 |
| `ClearAllCache`, `Version`; `EvaluateConfig` | Maintenance | L154, L184 |

## Typical failures

A typical failure is schema drift, a missing JSON directory, or no rights to alter the staging tables. Keywords: schema drift, column type, json path, create table failed.

| What you see | Card |
|---|---|
| "CreateTablesInAzure DB execution failed, TableName …" or "Create table in azure failed" | ISS-IREP-DES-003 |
| "GeneratePalTableSchema result empty" | ISS-IREP-DES-003 |
| "Destination path not configured" or errors reading or writing the JSON files | ISS-IRIMP-CONFIG, ISS-IRIMP-FILE |
| "Data type not available for column", "Invalid table name" (thrown) | ISS-IRIMP-DATAAPPLY |

## Related

PLT-IREP, CMP-IMPORTDES, FLW-IREP-IMPORT, ISS-IREP-DES-003
