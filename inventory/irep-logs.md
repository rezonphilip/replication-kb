---
doc_id: INV-IREP-LOGS
type: inventory
components: [irep]
status: draft
author: claude
last_verified: 2026-11-11
---

# iRep (SmartSync+) log message catalogue

Every logger call and thrown exception found in iRep (SmartSync+) code, per service, with level and source line. Services are configured with Serilog minimum level Error, so only Error/Critical lines (and unhandled exceptions) reach the log file by default; Information, Debug and Warning lines appear only if the level is lowered. Keywords: log, error message, signature, Serilog, log level.

## ComINT

Logger templates in ComINT. Keywords: ComINT log, error.

| Level | Message template | Source |
|---|---|---|
| Information | WorkerService StartAsync | `ComINT/Mariapps.PAL.ComINT/WorkerService.cs#L34` |
| Information | WorkerService StopAsync | `ComINT/Mariapps.PAL.ComINT/WorkerService.cs#L40` |
| Error | Process started | `ComINT/Mariapps.PAL.ComINT/WorkerService.cs#L46` |
| Error | default delay of 15 mins interval set for worker service | `ComINT/Mariapps.PAL.ComINT/WorkerService.cs#L61` |
| Information | {MethodName}\|Cancellation requested, stopping | `ComINT/Mariapps.PAL.ComINT/WorkerService.cs#L67` |
| Information | WorkerService Dispose | `ComINT/Mariapps.PAL.ComINT/WorkerService.cs#L75` |

## ComPBR

Logger templates in ComPBR. Keywords: ComPBR log, error.

| Level | Message template | Source |
|---|---|---|
| Information | {_className} {_methodName} DB execution started | `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/AzureDbRepository.cs#L36` |
| Information | {_className} {_methodName} DB execution completed | `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/AzureDbRepository.cs#L67` |
| Error | {_className} {_methodName} DB execution failed, ErrorMessage: {ex.Message} | `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/AzureDbRepository.cs#L74` |
| Debug | {0}\| ReadingExportTableOrder Data | `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/AzureDbRepository.cs#L89` |
| Debug | {0}\|Ended, Table Order list read | `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/AzureDbRepository.cs#L108` |
| Error | Error in {0}, while reading data with parameter transferApplicable Type: {1} and isAttachment:{2} | `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/AzureDbRepository.cs#L113` |
| Debug | {0}\| Import Config Path against each vessel  Data | `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/AzureDbRepository.cs#L125` |
| Debug | {0}\|Ended, Read import config path | `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/AzureDbRepository.cs#L146` |
| Error | Error in {0} | `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/AzureDbRepository.cs#L151` |
| Debug | {0}\|Ended, ReadAttachmentFileNameColumn | `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/AzureDbRepository.cs#L214` |
| Debug | {0}\|Ended, GetInPackets | `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/AzureDbRepository.cs#L240` |
| Debug | {0}\|Ended, GetOutPackets | `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/AzureDbRepository.cs#L266` |
| Debug | {0}\| Read Db Size | `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/AzureDbRepository.cs#L311` |
| Debug | {0}\|Read Db Size complete {1},Config value {2} | `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/AzureDbRepository.cs#L319` |
| Debug | {0}\|Ended, UpdatePacketId | `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/AzureDbRepository.cs#L378` |
| Error | {_className} ProbeConnection failed, Server: {result.Server}, Database: {result.Database}, ErrorMessage: {ex.Message} | `ComPBR/Mariapps.PAL.RepComPBR.DAL/Repository/ConfigProbeRepository.cs#L71` |
| Throw:ArgumentException | Filename is not in the correct format. | `ComPBR/Mariapps.PAL.RepComPBR.Model/Common/FilePackageInfo.cs#L46` |
| Information | {_className} {_methodName} started | `ComPBR/Mariapps.PAL.RepComPBR/BL/ConfigEvaluationBL.cs#L98` |
| Information | {_className} {_methodName} completed, Overall: {result.Overall}, Fail: {result.FailCount}, Warn: {result.WarnCount} | `ComPBR/Mariapps.PAL.RepComPBR/BL/ConfigEvaluationBL.cs#L126` |
| Error | {_className} {area} {check} failed, ErrorMessage: {ex.Message} | `ComPBR/Mariapps.PAL.RepComPBR/BL/ConfigEvaluationBL.cs#L844` |
| Error | error in IntCacheBL.SetData | `ComPBR/Mariapps.PAL.RepComPBR/BL/DataConduitMethods/RepComPBRCacheBL.cs#L63` |
| Error | <ex, methodName)> | `ComPBR/Mariapps.PAL.RepComPBR/BL/DataConduitMethods/RepComPBRCacheBL.cs#L156` |
| Debug | {0}\|Update result: {1} | `ComPBR/Mariapps.PAL.RepComPBR/BL/DataConduitMethods/RepComPBRCacheBL.cs#L199` |
| Debug | {0}\|Index of data: {1} | `ComPBR/Mariapps.PAL.RepComPBR/BL/DataConduitMethods/RepComPBRCacheBL.cs#L222` |
| Information | {MethodName}\| Started RepImportSync | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L69` |
| Error | {MethodName}\|{Message} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L93` |
| Error | Database Size exceed : {_basicSettingsBO.MaximumDatabaseSpaceGB}  | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L110` |
| Information | StartRepImportSync\|Cancellation requested, stopping | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L137` |
| Error | StartRepImportSync | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L142` |
| Error | GetAllPackets | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L189` |
| Error | ImportProcess \| Invalid VesselObjectId \| File Name  {FileName} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L208` |
| Debug | ImportProcess \| Invalid PacketHdId \| File Name  {FileName} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L216` |
| Error | ImportProcess \| Already Ready \| File Name  {FileName} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L222` |
| Error | GetFileInfo \| Invalid Format \| File Name  {FileName} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L246` |
| Error | FileMoveDirectory \| File Name {fileName} \| Error: {ex.Message} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L290` |
| Debug | ImportProcessWriteToDb\|Table ID {sqlTableJsonFormat.TableId.ToString()}\|{sqlTableJsonFormat.TableName} Count :{records.Count.ToString()} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L478` |
| Error | ImportProcessWriteToDb\|Table ID {sqlTableJsonFormat.TableId.ToString()} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L561` |
| Throw:Exception | <ex.Message)> | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L562` |
| Debug | {methodName} \| FileName: {fileName}, IsExport: {isExport} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L612` |
| Error | {methodName} \| FileName is null or empty | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L616` |
| Error | {methodName} \| File does not exist: {fileName} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L622` |
| Error | {methodName} \| Failed to parse file info from FileName: {fileName} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L630` |
| Debug | {methodName} \| Completed - TotalEntries: {response.Statistics.TotalEntries}, TotalRecords: {response.Statistics.TotalRecordCount}, Schemas: {response.TableSchemas.Count}, ConsolidatedTables: {response.ConsolidatedData.C | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L826` |
| Error | {methodName} \| Error reading zip file data: {fileName} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L840` |
| Debug | {methodName} \| FileName: {fileName}, TargetDirectory: {targetDirectory} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L850` |
| Error | {methodName} \| Failed to parse file info | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L870` |
| Debug | {methodName} \| Created directory: {moveDirectory} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L883` |
| Debug | {methodName} \| Deleted existing file: {destinationFilePath} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L899` |
| Debug | {methodName} \| Moved file: {fileToMove} -> {destinationFilePath} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L903` |
| Debug | {methodName} \| Moved file: {fileName} -> {destinationFilePath} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L917` |
| Debug | {methodName} \| Successfully marked file as processed | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L920` |
| Error | {methodName} \| Error marking zip file as processed: {fileName} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L925` |
| Debug | {methodName} \| OutputDirectory: {outputDirectory} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L935` |
| Error | {methodName} \| No consolidated data available | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L939` |
| Debug | {methodName} \| Created output directory: {outputDir} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L955` |
| Debug | {methodName} \| Created JSON data directory: {jsonDataDir} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L963` |
| Debug | {methodName} \| Written summary file: {summaryPath} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L982` |
| Debug | {methodName} \| Written table data: {fileName} ({tableData.TotalRecords} records) | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L1007` |
| Debug | {methodName} \| Written schemas file: {schemasPath} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L1018` |
| Debug | {methodName} \| Written zip entries manifest: {entriesPath} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L1029` |
| Debug | {methodName} \| Written index HTML: {indexPath} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L1037` |
| Debug | {methodName} \| Successfully wrote all consolidated data to: {outputDir} | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L1039` |
| Error | {methodName} \| Error writing consolidated data to files | `ComPBR/Mariapps.PAL.RepComPBR/BL/RepComPBRBL.cs#L1048` |
| Debug | {0}\|for API Address:{1}{2} | `ComPBR/Mariapps.PAL.RepComPBR/BL/ValidateConfigBL.cs#L14` |
| Throw:ArgumentNullException | Base address is null or empty | `ComPBR/Mariapps.PAL.RepComPBR/BL/ValidateConfigBL.cs#L16` |
| Throw:ArgumentNullException | End point address is null or empty | `ComPBR/Mariapps.PAL.RepComPBR/BL/ValidateConfigBL.cs#L18` |
| Debug | {0}\|for All serviceConfig data for key {1} | `ComPBR/Mariapps.PAL.RepComPBR/BL/ValidateConfigBL.cs#L24` |
| Throw:ArgumentNullException | All serviceConfig data is null or empty | `ComPBR/Mariapps.PAL.RepComPBR/BL/ValidateConfigBL.cs#L27` |
| Information | GetAndWriteZipFileData \| FileName: {FileName}, IsExport: {IsExport}, OutputDirectory: {OutputDirectory} | `ComPBR/Mariapps.PAL.RepComPBR/Controllers/RepComPBRController.cs#L45` |
| Error | GetAndWriteZipFileData \| Error | `ComPBR/Mariapps.PAL.RepComPBR/Controllers/RepComPBRController.cs#L82` |
| Error | \|{_configError} DCS calls will fail until it is configured. | `ComPBR/Mariapps.PAL.RepComPBR/ServiceClient/DCSServiceClient.cs#L42` |
| Error | \|{_configError} | `ComPBR/Mariapps.PAL.RepComPBR/ServiceClient/DCSServiceClient.cs#L50` |
| Throw:InvalidOperationException | {methodName}: {_configError} | `ComPBR/Mariapps.PAL.RepComPBR/ServiceClient/DCSServiceClient.cs#L51` |
| Debug | \|Input Data:{input} | `ComPBR/Mariapps.PAL.RepComPBR/ServiceClient/DCSServiceClient.cs#L57` |
| Debug | \|RESPONSE\|{output} | `ComPBR/Mariapps.PAL.RepComPBR/ServiceClient/DCSServiceClient.cs#L63` |
| Debug | \|Executing Post Request:{0}{1}, with input {2}  | `ComPBR/Mariapps.PAL.RepComPBR/ServiceClient/ExternalRequestServiceClient.cs#L19` |
| Debug | \|API RESULE:{contents.Result} | `ComPBR/Mariapps.PAL.RepComPBR/ServiceClient/ExternalRequestServiceClient.cs#L31` |
| Error | \|Exception | `ComPBR/Mariapps.PAL.RepComPBR/ServiceClient/ExternalRequestServiceClient.cs#L42` |
| Debug | Executing Method:{0}\|for  Get API:{1} | `ComPBR/Mariapps.PAL.RepComPBR/ServiceClient/ExternalRequestServiceClient.cs#L50` |
| Debug | {0} Result is {1} | `ComPBR/Mariapps.PAL.RepComPBR/ServiceClient/ExternalRequestServiceClient.cs#L61` |
| Throw:FileNotFoundException | File not found | `ComPBR/Mariapps.PAL.RepComPBR/StreamUtils/FileChunkReaderStream.cs#L75` |
| Throw:InvalidDataException | File is too small to be a valid chunk: {iteratingFileName} | `ComPBR/Mariapps.PAL.RepComPBR/StreamUtils/FileChunkReaderStream.cs#L94` |
| Throw:NotSupportedException | <)> | `ComPBR/Mariapps.PAL.RepComPBR/StreamUtils/FileChunkReaderStream.cs#L151` |
| Throw:InvalidOperationException | Stream is not initialized | `ComPBR/Mariapps.PAL.RepComPBR/StreamUtils/FileChunkReaderStream.cs#L196` |
| Throw:ArgumentOutOfRangeException | Offset cannot be negative | `ComPBR/Mariapps.PAL.RepComPBR/StreamUtils/FileChunkReaderStream.cs#L216` |
| Throw:ArgumentOutOfRangeException | Offset cannot be greater than file length | `ComPBR/Mariapps.PAL.RepComPBR/StreamUtils/FileChunkReaderStream.cs#L221` |
| Throw:InvalidOperationException | Could not find chunk for the given offset | `ComPBR/Mariapps.PAL.RepComPBR/StreamUtils/FileChunkReaderStream.cs#L228` |
| Throw:ArgumentOutOfRangeException | Invalid origin | `ComPBR/Mariapps.PAL.RepComPBR/StreamUtils/FileChunkReaderStream.cs#L247` |
| Throw:InvalidDataException | CRC validation failed for file: {waitStatus.Result.Item1.FileName} | `ComPBR/Mariapps.PAL.RepComPBR/StreamUtils/FileChunkReaderStream.cs#L298` |
| Throw:InvalidDataException | CRC validation failed for file: {result.Item1.FileName} | `ComPBR/Mariapps.PAL.RepComPBR/StreamUtils/FileChunkReaderStream.cs#L309` |
| Throw:ArgumentException | Stream must be seekable | `ComPBR/Mariapps.PAL.RepComPBR/StreamUtils/SegmentStream.cs#L43` |
| Throw:ArgumentException | Stream must be readable | `ComPBR/Mariapps.PAL.RepComPBR/StreamUtils/SegmentStream.cs#L48` |
| Throw:ArgumentException | Buffer is too small | `ComPBR/Mariapps.PAL.RepComPBR/StreamUtils/SegmentStream.cs#L96` |
| Throw:ArgumentOutOfRangeException | <nameof(offset))> | `ComPBR/Mariapps.PAL.RepComPBR/StreamUtils/SegmentStream.cs#L100` |
| Throw:ArgumentOutOfRangeException | <nameof(count))> | `ComPBR/Mariapps.PAL.RepComPBR/StreamUtils/SegmentStream.cs#L104` |
| Throw:ArgumentException | Invalid origin | `ComPBR/Mariapps.PAL.RepComPBR/StreamUtils/SegmentStream.cs#L151` |
| Information | WorkerService StartAsync | `ComPBR/Mariapps.PAL.RepComPBR/WorkerService.cs#L34` |
| Information | WorkerService StopAsync | `ComPBR/Mariapps.PAL.RepComPBR/WorkerService.cs#L40` |
| Information | {MethodName}\|WorkerService:ExecuteAsync\|Start | `ComPBR/Mariapps.PAL.RepComPBR/WorkerService.cs#L47` |
| Information | {MethodName}\|Process cycle Start | `ComPBR/Mariapps.PAL.RepComPBR/WorkerService.cs#L56` |
| Information | {0}\|Process cycle Ends | `ComPBR/Mariapps.PAL.RepComPBR/WorkerService.cs#L62` |
| Information | {MethodName}\|Process Cycle Ended | `ComPBR/Mariapps.PAL.RepComPBR/WorkerService.cs#L64` |
| Information | {MethodName}\|Cancellation requested, stopping | `ComPBR/Mariapps.PAL.RepComPBR/WorkerService.cs#L69` |
| Information | WorkerService Dispose | `ComPBR/Mariapps.PAL.RepComPBR/WorkerService.cs#L77` |

## ExportCDT

Logger templates in ExportCDT. Keywords: ExportCDT log, error.

| Level | Message template | Source |
|---|---|---|
| Information | {_className} {_methodName} DB execution started, isOffice:{isOffice} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L32` |
| Information | {_className} {_methodName} DB execution completed, isOffice:{isOffice}, rows fetched: {value.Count} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L84` |
| Error | {_className} {_methodName} DB execution failed, isOffice:{isOffice}, ErrorMessage: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L96` |
| Information | {_className} {_methodName} DB execution started, ColumnName: {columnName.ToString()} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L104` |
| Information | {_className} {_methodName} DB execution completed, ColumnName: {columnName.ToString()}, rows fetched: {value.Count} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L178` |
| Error | {_className} {_methodName} DB execution failed, ColumnName: {columnName.ToString()}, ErrorMessage: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L191` |
| Information | {_className} {_methodName} DB execution started, CDTVersion: {cdtVersion} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L292` |
| Information | {_className} {_methodName} DB execution completed, CDTVersion: {cdtVersion}, rows affected: {val} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L312` |
| Error | {_className} {_methodName} DB execution failed, CDTVersion: {cdtVersion}, ErrorMessage: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L325` |
| Information | {_className} {_methodName} DB execution started | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L335` |
| Information | {_className} {_methodName} DB execution completed, rows affected: {val} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L356` |
| Error | {_className} {_methodName} DB execution failed, ErrorMessage: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L369` |
| Information | {_className} {_methodName} DB execution completed, Result: {value} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L398` |
| Error | {_className} {_methodName} DB execution failed : {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L412` |
| Information | {_className} {_methodName} DB execution completed, Result count:{response.Count} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L453` |
| Information | {_className} {_methodName} DB execution started, TableId: {tableId}, CDTVersion: {cdtVersion} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L474` |
| Information | {_className} {_methodName} DB execution completed, TableId: {tableId}, CDTVersion: {cdtVersion}, rows affected: {val} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L495` |
| Error | {_className} {_methodName} {response.ErrorMessage} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L505` |
| Warning | {_className} {_methodName} rows affected not reported ({val}), treating update as successful, TableId: {tableId}, CDTVersion: {cdtVersion} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L510` |
| Error | {_className} {_methodName} DB execution failed, TableId: {tableId}, CDTVersion: {cdtVersion}, ErrorMessage: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L523` |
| Information | {_className} {_methodName} DB execution started, DataTable row count: {dataTable?.Rows?.Count ?? 0} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L535` |
| Information | {_className} {_methodName} DB execution completed, DataTable row count: {dataTable?.Rows?.Count ?? 0} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L559` |
| Error | {_className} {_methodName} DB execution failed ErrorMessage: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L569` |
| Information | {_className} {_methodName} DB execution started, MaxId: {maxId}, isDelete: {isDelete} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L584` |
| Information | {_className} {_methodName} DB execution completed, MaxId: {maxId}, isDelete: {isDelete}, rows affected {value} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L617` |
| Error | {_className} {_methodName} DB execution failed, MaxId: {maxId}, isDelete: {isDelete}, ErrorMessage: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L630` |
| Information | {_className} {_methodName} DB execution completed | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L676` |
| Information | {_className} {_methodName} DB execution completed, Result value: {response.Id} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/AzureDbRepository.cs#L774` |
| Error | {_className} ProbeConnection failed, Server: {result.Server}, Database: {result.Database}, ErrorMessage: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/ConfigProbeRepository.cs#L77` |
| Information | {_className} {_methodName} DB execution started, TableId: {tableId}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/PrimaryRepository.cs#L33` |
| Information | {_className} {_methodName} DB execution completed, TableId: {tableId}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, rows affected: {val} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/PrimaryRepository.cs#L56` |
| Error | {_className} {_methodName} DB execution failed, TableId: {tableId}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/PrimaryRepository.cs#L68` |
| Information | {_className} {_methodName} DB execution started, CDTVersion: {cdtVersion}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/PrimaryRepository.cs#L78` |
| Information | {_className} {_methodName} DB execution completed, CDTVersion: {cdtVersion}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, rows affected: {val} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/PrimaryRepository.cs#L99` |
| Error | {_className} {_methodName} DB execution failed, CDTVersion: {cdtVersion}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/PrimaryRepository.cs#L113` |
| Information | {_className} {_methodName} DB execution started, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/PrimaryRepository.cs#L123` |
| Information | {_className} {_methodName} DB execution completed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, Result: {val} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/PrimaryRepository.cs#L142` |
| Error | {_className} {_methodName} DB execution failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/PrimaryRepository.cs#L155` |
| Information | {_className} {_methodName} DB execution started, tableId: {tableId}, CDTVersion: {cdtVersion}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/PrimaryRepository.cs#L165` |
| Error | {_className} {_methodName} DB execution failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {item.ErrorMessage} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/PrimaryRepository.cs#L216` |
| Information | {_className} {_methodName} DB execution completed, tableId: {tableId}, CDTVersion: {cdtVersion}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/PrimaryRepository.cs#L224` |
| Error | {_className} {_methodName} DB execution failed, tableId: {tableId}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/PrimaryRepository.cs#L235` |
| Information | {_className} {_methodName} DB execution completed, SyncLagSecs(inSec): {response.SyncLagSecs}, SecondaryReplica: {response.SecondaryReplica}, PrimaryReplica: {response.PrimaryReplica}, ReplicaServerName: {response.Replic | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/PrimaryRepository.cs#L271` |
| Information | {_className} {_methodName} DB execution completed, SyncLagSecs(inMilliSec): {response.SyncLagSecs}, SecondaryReplica: {response.SecondaryReplica}, PrimaryReplica: {response.PrimaryReplica}, ReplicaServerName: {response.R | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/PrimaryRepository.cs#L281` |
| Information | {_className} {_methodName} DB execution started, TableId: {tableId}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, MaxId: {maxId} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/ReadOnlyRepository.cs#L28` |
| Information | {_className} {_methodName} DB execution completed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, TableId: {tableId}, MaxId: {maxId}, rows affected: {val} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/ReadOnlyRepository.cs#L52` |
| Error | {_className} {_methodName} DB execution failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, TableId: {tableId}, MaxId: {maxId}, ErrorMessage: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT.DAL/Repository/ReadOnlyRepository.cs#L66` |
| Information | {_className} {_methodName} started | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/ConfigEvaluationBL.cs#L105` |
| Information | {_className} {_methodName} completed, Overall: {result.Overall}, Fail: {result.FailCount}, Warn: {result.WarnCount} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/ConfigEvaluationBL.cs#L138` |
| Error | {_className} {area} {check} failed, ErrorMessage: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/ConfigEvaluationBL.cs#L700` |
| Information | {_className} {_methodName} ReplicaTypeId: {replicaTypeId} Started | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L44` |
| Error | Connection not feteched properly, ReplicaTypeId: {replicaTypeId} PrimaryDB: {connectionStringbo?.PrimaryDB} ReadOnlyDB: {connectionStringbo?.ReadOnlyDB} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L49` |
| Information | {_className} {_methodName} SaveCdtLastExtractedVersion to PAL Primary Successfull, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L62` |
| Error | {_className} {_methodName} SaveCdtLastExtractedVersion to PAL Primary DB Failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {cdtVersionResponsePalPrimary.ErrorMessage} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L65` |
| Information | {_className} {_methodName} SaveCdtLastExtractedVersion to Azure DB Successfull, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L74` |
| Error | {_className} {_methodName} SaveCdtLastExtractedVersion to Azure DB Failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {cdtVersionResponseAzureDB.ErrorMessage} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L77` |
| Error | {_className} {_methodName} GetMaxId failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {maxIdResponse.ErrorMessage} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L85` |
| Information | {_className} {_methodName} GetMaxId successfull, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, MaxId: {maxIdResponse.ResultValue} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L89` |
| Error | {_className} {_methodName} ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, MaxId 0 found, not continuing execution, ErrorMessage: {maxIdResponse.ErrorMessage} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L93` |
| Information | {_className} {_methodName} CheckCdtVersion validation failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, latencyValue:{latencyValue}, retry: {counter} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L110` |
| Information | {_className} {_methodName} ClearSpam successfull, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L133` |
| Error | {_className} {_methodName} ClearSpam failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {spamClearingResponse.ErrorMessage} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L135` |
| Information | {_className} {_methodName} SaveCdtLastExtractedVersion Azure DB Successfull, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L140` |
| Error | {_className} {_methodName} SaveCdtLastExtractedVersion Azure DB Failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {cdtVersionResponseAzure.ErrorMessage} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L142` |
| Information | {_className} {_methodName} DeleteDataFromRecordSync Azure DB Successfull, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L150` |
| Error | {_className} {_methodName} DeleteDataFromRecordSync Azure DB Failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {deleteFromRecordSyncResponse.ErrorMessage} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L152` |
| Error | {_className} {_methodName} DeleteDataFromRecordSync Azure DB Failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {deleteFromRecordSyncDeleteResponse.ErrorMessage} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L159` |
| Error | ReplicaTypeId: {connectionStringbo.ReplicaTypeId} faliure1Json: {faliure1Json} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L192` |
| Error | ReplicaTypeId: {connectionStringbo.ReplicaTypeId} faliure2Json: {faliure2Json} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L195` |
| Error | ReplicaTypeId: {connectionStringbo.ReplicaTypeId} faliureListToErrorLogSync: {faliureListToErrorLog1} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L202` |
| Error | ReplicaTypeId: {connectionStringbo.ReplicaTypeId} faliureListToErrorLogDelete: {faliureListToErrorLog2} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L208` |
| Error | {_className} {_methodName} CheckCdtVersion validation failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L220` |
| Error | {_className} {_methodName} CheckCdtVersion failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {checkCdtVesrionResponse.ErrorMessage} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L225` |
| Information | {_className} {_methodName} ReplicaTypeId: {connectionStringbo.ReplicaTypeId} Ended | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L228` |
| Error | {_className} {_methodName} ReplicaTypeId: {replicaTypeId} Ended Exception: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L236` |
| Error | {_className} {_methodName} connection settings null | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L248` |
| Information | {_className} {_methodName} Store cdtQueryDataset to cache success, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L266` |
| Error | {_className} {_methodName} Store cdtQueryDataset to cache failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMEaasge: {setGetCDTQueryCacheResponse} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L268` |
| Error | {_className} {_methodName} failed dataset cdtQueryDataset null value returned, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L272` |
| Error | {_className} {_methodName} failed to fetch currentcdtversion, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, response is null | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L285` |
| Error | {_className} {_methodName} failed to fetch currentcdtversion, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {currentCdtVersionResponse.ErrorMessage} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L291` |
| Error | {_className} {_methodName} UpdateCdtVersion failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, TableId: {item.Key}, CDTVersion: {cdtVersionItem.CdtVersion}, ErrorMessage: {updateCdtVersionResponse?.ErrorMessage}. | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L309` |
| Information | {_className} {_methodName} error while executing cdt query, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, TableId: {item.Key} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L314` |
| Error | {_className} {_methodName} TableId: {currentExecutingTableId}, ReplicaTypeId: {replicaTypeId}, Error: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L324` |
| Information | {_className} {_methodName} ReplicaTypeId: {replicaTypeId}, Ended | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L327` |
| Information | {_className} {_methodName} Store insRecordVslSyncDataset to cache success, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L358` |
| Error | {_className} {_methodName} ReplicaTypeId: {connectionStringbo.ReplicaTypeId} Store insRecordVslSyncDataset to cache failed: {GetQueryToInsertRecordVslSyncResponse} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L360` |
| Error | {_className} {_methodName} dataset insRecordVslSyncDataset null, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L364` |
| Error | {_className} {_methodName} ReplicaTypeId: {connectionStringbo.ReplicaTypeId} query missing in dataset {tbl.TableId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L383` |
| Information | {_className} {_methodName} dataset insRecordVslSyncTableIds null, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L394` |
| Error | {_className} {_methodName} ReplicaTypeId: {replicaTypeId}, Error in GetQueryToInsertRecordVslSync: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L403` |
| Information | {_className} {_methodName} ReplicaTypeId: {replicaTypeId} Ended | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L405` |
| Information | {_className} {_methodName} ReplicaTypeId: {connectionStringbo.ReplicaTypeId} Started | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L414` |
| Error | {_className} {MethodName} Query not found, skipping [REP].[REP_EXPORT_VESSEL_QUERY]  ID: {tbl.Id}, TableId: {tableId}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L436` |
| Error | {_className} {MethodName} TableId 0, skipping [REP].[REP_EXPORT_VESSEL_QUERY] Id: {tbl.Id}, TableId: {tableId}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L442` |
| Error | {_className} {MethodName} MaxId 0, skipping [REP].[REP_EXPORT_VESSEL_QUERY] Id: {tbl.Id}, TableId: {tableId}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L448` |
| Information | {_className} {MethodName} [REP].[REP_EXPORT_VESSEL_QUERY] {(_basicSettingsBO.IsOffice ? "OFF_EXPORT_QUERY" : "VSL_EXPORT_QUERY")} Id: {tableId} Response: {(response.StatusCode == 0 ? "FAILED" : "SUCCESS")}, ReplicaTypeId | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L462` |
| Error | {_className} {MethodName} [REP].[REP_EXPORT_VESSEL_QUERY] {(_basicSettingsBO.IsOffice ? "OFF_EXPORT_QUERY" : "VSL_EXPORT_QUERY")} Id: {tableId} Response: {(response.StatusCode == 0 ? "FAILED" : "SUCCESS")} {response.Erro | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L464` |
| Error | {_className} {MethodName} ReplicaTypeId: {connectionStringbo.ReplicaTypeId} Error: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L472` |
| Information | {_className} {_methodName} Store GetQueryToInsertRecordVslSync_DELETE to cache success, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L515` |
| Error | {_className} {_methodName} ReplicaTypeId: {connectionStringbo.ReplicaTypeId} Store GetQueryToInsertRecordVslSync_DELETE to cache failed: {GetQueryToInsertRecordVslSync_DELETEResponse} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L517` |
| Information | {_className} {_methodName} dataset insRecordVslSyncDatasetDelete null, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L521` |
| Error | {_className} {_methodName} ReplicaTypeId: {connectionStringbo.ReplicaTypeId} delete query missing in dataset {tbl.TableId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L542` |
| Error | {_className} {_methodName} ReplicaTypeId: {replicaTypeId} Error: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L562` |
| Debug | {_className} {_methodName} ReplicaTypeId: {connectionStringbo.ReplicaTypeId} Started | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L575` |
| Error | {_className} {MethodName} Query not found, skipping [REP].[REP_EXPORT_VESSEL_QUERY], Id: {tbl.Id}, TableId: {tableId}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L598` |
| Error | {_className} {MethodName} TableId 0, skipping [REP].[REP_EXPORT_VESSEL_QUERY], Id: {tbl.Id}, TableId: {tableId}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L604` |
| Error | {_className} {MethodName} MaxId 0, skipping [REP].[REP_EXPORT_VESSEL_QUERY], Id: {tbl.Id}, TableId: {tableId}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L610` |
| Information | {_className} {MethodName} [REP].[REP_EXPORT_VESSEL_QUERY] OFF_DEL_QUERY Table Id: {tableId} Response: {(response.StatusCode == 0 ? "FAILED" : "SUCCESS")}, ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L624` |
| Error | {_className} {MethodName} [REP].[REP_EXPORT_VESSEL_QUERY] OFF_DEL_QUERY Table Id: {tableId} Response: {(response.StatusCode == 0 ? "FAILED" : "SUCCESS")} {response.ErrorMessage}, ReplicaTypeId: {connectionStringbo.Replic | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L626` |
| Debug | {_className} {_methodName} ReplicaTypeId: {connectionStringbo.ReplicaTypeId} Ended | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DBConnectionAggregator.cs#L642` |
| Error | error in IntCacheBL.SetData | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DataConduitMethods/RepExportCDTCacheBL.cs#L70` |
| Error | <ex, methodName)> | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DataConduitMethods/RepExportCDTCacheBL.cs#L183` |
| Error | error in IntCacheBL.SetData, Id: {Id}, ReplicaTypeId: {ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DataConduitMethods/RepExportCDTCacheBL.cs#L201` |
| Debug | {0}\|Update result: {1} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DataConduitMethods/RepExportCDTCacheBL.cs#L234` |
| Debug | {0}\|Index of data: {1} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/DataConduitMethods/RepExportCDTCacheBL.cs#L261` |
| Information | {_className} {_methodName} Store connectionStringSettingsBOs to cache success | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L74` |
| Error | {_className} {_methodName} Store connectionStringSettingsBOs to cache failed, ErrorMessage: {setgetConnectionStringsListCacheResponse} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L76` |
| Error | {_className} {_methodName} failed dataset connectionStringSettingsBOs null value returned | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L82` |
| Error | Processing failed, not able to fetch database connectionString configurations for ReplicaTypeId: {input.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L98` |
| Error | CDT not enabled for ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L124` |
| Error | Invalid connectionString settings, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, PrimaryDB: {connectionStringbo.PrimaryDB}, ReadOnlyDB: {connectionStringbo.ReadOnlyDB} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L163` |
| Information | Processing started, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, Process started: {ProcesStatusEntity.GetProcessStatus(connectionStringbo.ReplicaTypeId)} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L179` |
| Error | CACHE_CHEKING ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ClearCacheEnabled: {_workerServiceSettingsBO.ClearCacheEnabled}, ClearCacheIntervalInMin: {_workerServiceSettingsBO.ClearCacheIntervalInMin}, GetCacheStatu | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L186` |
| Error | CACHE_CHEKING entered cache clearing | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L187` |
| Error | Processing failed, ReplicaTypeId: {claimedReplicaTypeId}, ErrorMessage: {taskEx.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L200` |
| Warning | Process status not released by this run, ReplicaTypeId: {claimedReplicaTypeId}: the flag was force-cleared while it ran and may now belong to a newer run. | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L214` |
| Information | Process already running, Process started: {ProcesStatusEntity.GetProcessStatus(connectionStringbo.ReplicaTypeId)} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L221` |
| Error | ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L233` |
| Error | Processing failed, not able to fetch database connectionString configurations | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L253` |
| Information | DcsServiceCallAsync {_databaseSettingsBO.DcsCallEnabled} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L271` |
| Information | DcsServiceCallAsync Start | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L275` |
| Error | DcsServiceCallAsync End | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L277` |
| Error | {_className} {_methodName} Processing failed, not able to fetch database connectionString configurations for ReplicaTypeId: {ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L290` |
| Information | {_className} {_methodName} successfully cleared cache | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L321` |
| Error | {_className} {_methodName} {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L330` |
| Error | No data found in spam tables | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L382` |
| Error | To, CC and Bcc configuration not found | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L402` |
| Error | easBaseUrl configuration not found | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L408` |
| Error | easSendUrl configuration not found | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L414` |
| Error | easConfigKey configuration not found | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/RepExportCDTBL.cs#L420` |
| Debug | {0}\|for API Address:{1}{2} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/ValidateConfigBL.cs#L14` |
| Throw:ArgumentNullException | Base address is null or empty | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/ValidateConfigBL.cs#L16` |
| Throw:ArgumentNullException | End point address is null or empty | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/ValidateConfigBL.cs#L18` |
| Debug | {0}\|for All serviceConfig data for key {1} | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/ValidateConfigBL.cs#L24` |
| Throw:ArgumentNullException | All serviceConfig data is null or empty | `ExportCDT/Mariapps.PAL.RepExportCDT/BL/ValidateConfigBL.cs#L27` |
| Error | Service RepExportCDT_Utility not found on services.json | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/ComINTServiceClient.cs#L51` |
| Information | {_className} {_methodName} Api Url: {_dbServiceData.ServiceUrl}{apiAddress} | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/ComINTServiceClient.cs#L62` |
| Information | {_className} {_methodName} Response: {output} | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/ComINTServiceClient.cs#L65` |
| Information | {_className} {_methodName} completed | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/ComINTServiceClient.cs#L66` |
| Error | {_className} {_methodName} | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/ComINTServiceClient.cs#L77` |
| Information | {_className} {_methodName} ReplicaTypeId: {ReplicaTypeId} started | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/DCSServiceClient.cs#L42` |
| Error | ReplicaTypeId: {ReplicaTypeId} Service RepExportDCS_Utility not found on services.json | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/DCSServiceClient.cs#L48` |
| Information | {_className} {_methodName} ReplicaTypeId: {ReplicaTypeId} Api Url: {_dbServiceData.ServiceUrl}{apiAddress} | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/DCSServiceClient.cs#L64` |
| Information | {_className} {_methodName} ReplicaTypeId: {ReplicaTypeId} Response: {output} | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/DCSServiceClient.cs#L67` |
| Information | {_className} {_methodName} ReplicaTypeId: {ReplicaTypeId} completed | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/DCSServiceClient.cs#L68` |
| Error | {_className} {_methodName} ReplicaTypeId: {ReplicaTypeId} | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/DCSServiceClient.cs#L76` |
| Debug | \|Executing Post Request:{0}{1}, with input {2}  | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/ExternalRequestServiceClient.cs#L25` |
| Debug | \|API RESULE:{contents} | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/ExternalRequestServiceClient.cs#L39` |
| Information | {methodName} serviceBaseAddress: {serviceBaseAddress}, serviceApiAddress: {serviceApiAddress} Success | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/ExternalRequestServiceClient.cs#L41` |
| Error | \|HttpClient null returned | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/ExternalRequestServiceClient.cs#L47` |
| Error | \|Exception | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/ExternalRequestServiceClient.cs#L57` |
| Debug | Executing Method:{0}\|for  Get API:{1} | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/ExternalRequestServiceClient.cs#L65` |
| Debug | {0} Result is {1} | `ExportCDT/Mariapps.PAL.RepExportCDT/ServiceClient/ExternalRequestServiceClient.cs#L76` |
| Information | WorkerService StartAsync | `ExportCDT/Mariapps.PAL.RepExportCDT/WorkerService.cs#L34` |
| Information | WorkerService StopAsync | `ExportCDT/Mariapps.PAL.RepExportCDT/WorkerService.cs#L40` |
| Information | Process started | `ExportCDT/Mariapps.PAL.RepExportCDT/WorkerService.cs#L46` |
| Information | WorkerService ExecuteAsync\|Process Reinitiated | `ExportCDT/Mariapps.PAL.RepExportCDT/WorkerService.cs#L51` |
| Information | WorkerService ExecuteAsync\|Cancellation requested, stopping | `ExportCDT/Mariapps.PAL.RepExportCDT/WorkerService.cs#L62` |
| Error | WorkerService ExecuteAsync, ErrorMessage: {ex.Message} | `ExportCDT/Mariapps.PAL.RepExportCDT/WorkerService.cs#L67` |
| Information | WorkerService Dispose | `ExportCDT/Mariapps.PAL.RepExportCDT/WorkerService.cs#L94` |

## ExportDCS

Logger templates in ExportDCS. Keywords: ExportDCS log, error.

| Level | Message template | Source |
|---|---|---|
| Error | {ClassName} ProbeConnection failed, Server: {Server}, Database: {Database}, ErrorMessage: {ErrorMessage} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/ConfigProbeRepository.cs#L76` |
| Information | {MethodName}\|Reading Delete Data from table: {TableName} ID:{TableId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/DcsProcDelRepository.cs#L33` |
| Warning | {MethodName}\|Column {ColumnIndex} contains SQL spatial type - skipping. Ensure Microsoft.SqlServer.Types assembly is available. | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/DcsProcDelRepository.cs#L93` |
| Warning | {MethodName}\|Error reading column {ColumnIndex} - setting to null | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/DcsProcDelRepository.cs#L98` |
| Information | {MethodName}\|Finished reading data for tableName:{TableName} with tableId:{TableId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/DcsProcDelRepository.cs#L111` |
| Information | {MethodName}\|Reading Delete table structure for {TableName} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/DcsProcDelRepository.cs#L118` |
| Information | {MethodName}\|Reading Data from table: {TableName} ID:{TableId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/DcsProcRepository.cs#L35` |
| Information | {MethodName}\| Read Data for Table {TableId}-{TableName} with batch length {BatchCount} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/DcsProcRepository.cs#L111` |
| Error | {MethodName}\|Invalid SQL configured for table Id {TableId} and table name {Name}. Query: {Query} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/DcsProcRepository.cs#L123` |
| Error | Error in {MethodName} while processing table Id {TableId} and table name {Name} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/DcsProcRepository.cs#L132` |
| Information | {MethodName}\|Reading Data from Attachment table: {TableName} ID:{TableId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/DcsProcRepository.cs#L143` |
| Error | {MethodName}\| Column name {ColumnName} not found in table {TableName} for physical files | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/DcsProcRepository.cs#L176` |
| Debug | {MethodName}\| Appending basePath {Path} with value from key {Key} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/DcsProcRepository.cs#L231` |
| Debug | {MethodName}\| Appended basePath {Path} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/DcsProcRepository.cs#L244` |
| Error | {MethodName}\|Invalid SQL configured for table Id {TableId} and table name {TableName}. Query: {Query} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/DcsProcRepository.cs#L262` |
| Error | Error in {MethodName} while processing tableName {TableName} tableId {TableId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/DcsProcRepository.cs#L270` |
| Information | {MethodName}\|Reading table structure for {TableName} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/DcsProcRepository.cs#L278` |
| Error | Error in {MethodName} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/PalExportDcsRepository.cs#L50` |
| Debug | {MethodName}\| Reading Export Order Data for replication Type Id {RepTypeId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L68` |
| Debug | {MethodName}\|Ended,Table Order list readfor replication Type Id {RepTypeId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L111` |
| Error | Error in {MethodName}, while reading attachment data with parameter operationType TransferApplicable Type:{TransferAppType} and ReplicatoinType Id {RepTypeId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L120` |
| Debug | {MethodName}\| Reading Attachment Export Blob Query Data | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L132` |
| Debug | {MethodName}\|Ended,Attachment Table Order list read | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L163` |
| Error | Error in {MethodName}, while reading blob query details | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L172` |
| Debug | {MethodName}\| Export Config Path against each vessel | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L182` |
| Debug | {MethodName}\|Ended, Read export config path mapped against vessel | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L222` |
| Debug | {MethodName}\| Reading Syncing Active Vessels | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L242` |
| Error | {MethodName}\|Error whie reading Sync Active Vessels | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L278` |
| Debug | {MethodName}\|Reading environment unique details | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L288` |
| Debug | {MethodName}\|Reading config paths | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L336` |
| Debug | {MethodName}\|Ended, Read config paths | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L366` |
| Debug | {MethodName}\|Reading Rep Type Master Data | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L386` |
| Debug | {MethodName}\|Ended, Read Rep Type Master Data | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L424` |
| Debug | {MethodName}\| reading packet counter for VesselObjectId: {VesselObjectId}, replicationDataType: {ReplicationDataType} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L432` |
| Throw:InvalidOperationException | PacketCounter is not found | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L459` |
| Error | {MethodName}\|Error while reading packetCounter | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L467` |
| Debug | {MethodName}\|Reading Record Vessel Sync Table Meta Information for replicationData Type:{ReplicaTypeId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L480` |
| Warning | {MethodName}\| No Meta Information found for record Vessel Sync | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L507` |
| Error | {MethodName}\|Error while reading MetaData Info from Record Vessel Sync Information for parameter {ReplicaTypeId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L525` |
| Debug | {MethodName}\| Reading Vessels list to export between Ids {MinId} and {MaxId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L535` |
| Error | Error while reading {MethodName} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L575` |
| Debug | {MethodName}\| Updating vessel packet counter for VesselObjectId: {VesselObjectId}, packetCounter: {PacketCounter}, replicaTypeId: {ReplicaTypeId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L584` |
| Error | {MethodName}\| Sql Exception gotten, while updating Packet Counter {PacketCounter} for vessel {VesselObjectId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L613` |
| Error | {MethodName}\| Awaiter Insert status for vessel {VesselObjectId} is {AwaitInsertStatus} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L619` |
| Debug | {MethodName}\| Reading pending table list for vessel {Vessel}, within range {MinId} -> {MaxId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L702` |
| Error | {MethodName}\|No record data type found against TableId {TableId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L760` |
| Debug | {MethodName}\|Finished reading tableMeta Data\|record count {Count} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L777` |
| Information | {MethodName}\| Delete table list record for VesselObject {VesselId}, within range {MinimumId} -> {MaximumId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L795` |
| Information | {MethodName}\| Ended, Delete table list record for VesselObject {VesselId}, within range {MinimumId} -> {MaximumId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L819` |
| Error | {MethodName}\| Sql Exception gotten, while deleting records for vessel  {VesselObjectId}, within VesselSync range {MinId} - {MaxId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L827` |
| Debug | {MethodName}\| Deleting records {RecordJson} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L854` |
| Error | {MethodName}\| Sql Exception gotten, while deleting records for vessel  {VesselObjectId}, within VesselSync range {MinId} - {MaxId} and record List count {RecordListCount} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L887` |
| Error | Error in {MethodName}, while deleting records for vessel  {VesselObjectId}, within VesselSync range {MinId} - {MaxId} and record List count {RecordListCount} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L903` |
| Debug | {MethodName}\|Saving packet details to OutPacketHd for packetCOunter {Counter} and vessel {VesselObjectId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L913` |
| Error | {MethodName}\| Sql Exception gotten, while inserting to OutPacketHd | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L947` |
| Error | {MethodName}\| Awaiter Insert status for is {AwaitInsertStatus} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L952` |
| Error | Error in {MethodName} with param  packetCOunter {Counter} and vessel {VesselObjectId} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L962` |
| Debug | {MethodName}\|Start | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L971` |
| Debug | {MethodName}\|Reading Resend Data | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L1056` |
| Debug | {MethodName}\|Ended, Resend Data read | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L1096` |
| Error | {MethodName}\| Error while reading data for Vessel {VesselObjectId}, ReplicaType {ReplicaTypeId} with constrains isOffice {IsOffice}, resentLimit {ResentLimit}, waitInMin {WaitInMin} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L1105` |
| Debug | {MethodName}\|Started for outPacketID {Id} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L1114` |
| Error | {MethodName}\| Sql Exception gotten, for auto resend log entry for PacketHdId {OutPacketId}  | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L1143` |
| Error | Error in {MethodName} for outPacketId {Id} | `ExportDCS/Mariapps.PAL.RepExportDCS.DAL/Repository/RepExportDCSRepository.cs#L1158` |
| Debug | {MethodName}\| Setting Key data for replica type {TypeName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L64` |
| Information | {MethodName}\|Setting cache data | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L69` |
| Information | {MethodName}\|Config read status to cache result: {Result} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L84` |
| Debug | {MethodName}\|Deleting all vessel in skip vessel list {Key} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L87` |
| Error | {MethodName}\|Error while settign Initial Data | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L98` |
| Debug | {MethodName}\|Started | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L134` |
| Debug | {MethodName}\|Export Table Order Data exists and saving to cache \| Record count:{Count}\| with key {KeyName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L164` |
| Debug | {MethodName}\|Saving Export Table Order Data  to cache result: {StatusResult} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L167` |
| Error | {MethodName}\|No Attachment Export Table order data found | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L172` |
| Error | {MethodName}\|Error while reading and setting  Export Table Order data to cache | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L182` |
| Debug | {MethodName}\|Environment default config path found, saving to cache key {Key}  | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L200` |
| Debug | {MethodName}\|Saving Environment Details to cache result: {Result} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L203` |
| Error | {MethodName}\|Environment default config paths not found | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L207` |
| Debug | {MethodName}\|Ended | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L210` |
| Debug | {MethodName}\|Saving Vessel Export Config Path\| Record count:{ConfigPathCount} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L234` |
| Debug | {MethodName}\|Saving Export Table Order Data  to cache result: {Result} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L237` |
| Error | {MethodName}\|No Vessel Config Path data found | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L242` |
| Error | {MethodName}\|Error while setting Export vessel config path to cache | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L252` |
| Debug | {MethodName}\|Reading Active Vessels | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L262` |
| Error | {MethodName}\|No active Vessels found | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L267` |
| Debug | {MethodName}\|Pushing Active Vessel List to Key {1} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L272` |
| Debug | {MethodName}\|Saving Active Vessel List to cache result: {1} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L274` |
| Error | {MethodName}\|Error while reading Active VesselSync | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L284` |
| Debug | {MethodName}\|Reading Client Details | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L294` |
| Debug | {MethodName}\|Pushing client unique data to key {KeyName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L298` |
| Debug | {MethodName}\|Saving Client Details to cache result: {Result} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L300` |
| Error | {MethodName}\|No Client Details found | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L304` |
| Error | {MethodName}\|Error while reading Client Details | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L315` |
| Debug | {MethodName}\|Reading Export Record Vessel Sync Table meta Info with param - record limit:{RecordLimit}, replica Type Id: {ReplicaTypeId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L325` |
| Warning | {MethodName}\|Could not read Record VesselSync table Meta Info | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L330` |
| Debug | {MethodName}\|Pushing Export Record Vessel Sync Table meta Info to Dictionary | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L335` |
| Debug | {MethodName}\|Saving Export Record Vessel Sync Table meta Infoto cache result: {Result} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L339` |
| Error | Error while setting {MethodName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L349` |
| Debug | {MethodName}\|Updating Pending Active Vessels to cache | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L369` |
| Debug | {MethodName}\|Saving Active Vessel List to cache result: {Result} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L372` |
| Debug | {MethodName}\|Update result: {Result} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L402` |
| Debug | {MethodName}\|Append result: {Result} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L408` |
| Debug | {MethodName}\|Adding Vessel to Active Queue | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L424` |
| Debug | {MethodName}\|Vessel added to Active Queue | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L428` |
| Error | {MethodName}\|Vessel already exists in Active Queue | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L432` |
| Debug | {MethodName}\|Appending List Data in cache | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L442` |
| Debug | {MethodName}\| Setting Vessel {VesselId} to queue | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L460` |
| Debug | {MethodName}\| setting for Replication data TYpe {Name} and ID {Id} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L500` |
| Throw:ArgumentNullException | <nameof(replicaInfo))> | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L502` |
| Debug | {MethodName}\|Active Keys Entity: {ActiveKeysEntity} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L516` |
| Debug | {MethodName}\|Reading Export Table Order List | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L551` |
| Error | {MethodName}\| Export Table Data not found in cache, reading from DB | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L557` |
| Debug | {MethodName}\|Export Table Data Found in cache | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L562` |
| Error | {MethodNAme}\| Error while reading export Table Order Data | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L573` |
| Debug | {MethodName}\|Reading Active Vessel Sync List | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L583` |
| Error | {MethodName}\|Active VesselSync Data not found in cache, reading from DB | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L589` |
| Debug | {MethodName}\|Active VesselSync Data Data Found in cache | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L594` |
| Error | Error whille reading {MethodName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L604` |
| Debug | {MethodName}\|Reading Config Path List | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L614` |
| Debug | {MethodName}\| Started reading client unique data | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L644` |
| Error | {MethodName}\|Client Details not found in cache, reading from DB | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L649` |
| Debug | {MethodName}\|Client Details Found in cache | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L654` |
| Error | {MethodName}\| Error while reading Client Details | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L664` |
| Warning | {MethodName}\|No Process Meta Info found in cache | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L680` |
| Debug | {MethodName}\|Process Meta Info found in cache | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L685` |
| Error | {MethodName}\|Error while checking Dcs Status | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L691` |
| Information | {MethodName}\|Started reading Export Record Vessel meta info for Replication Type:{ReplicaTypeId} with record limit {RecordLimit} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L699` |
| Error | {MethodName}\|Error while reading Export Record Vessel Table meta info | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L719` |
| Debug | {MethodName}\|Started reading Config Status from {KeyName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L732` |
| Error | {MethodName}\|Config Status is false, ReInitialize the Service startup config | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L738` |
| Debug | {MethodName}\|Current Environment Deats Found in cache | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L743` |
| Error | {MethodName}\|Error while reading Config Status | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L754` |
| Debug | {MethodName}\|Started reading Current Environment default path configs for key {KeyName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L762` |
| Error | {MethodName}\|Current Environment default config paths not found in cache, reading from DB | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L770` |
| Debug | {MethodName}\|Current Environment Deatsa Found in cache | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L775` |
| Debug | {MethodName}\|Started reading retry limit | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L783` |
| Debug | {MethodName}\|Started reading key value for key {KeyName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L794` |
| Error | Error in {MethodName} while fetching default connfig with Param {ExportDbConnection}, SearchKey {SearchKeyName}, KeyName {KeyName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L820` |
| Debug | {MethodName}\|Started readingVessel list for {KeyName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L828` |
| Debug | {MethodName}\|No Vessel found against {KeyName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L834` |
| Debug | {MethodName}\|Read {Count} of vessel from  {KeyName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L839` |
| Error | Error while {MethodName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L883` |
| Error | Error while reading {0} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L903` |
| Debug | {MethodName}\| Setting Key data for replica type {ReplicaTypeId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L919` |
| Warning | {MethodName}\|Export Config Status is false for Vessel {VesselObjectId} \| adding it to failed Vessel List | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L928` |
| Debug | {MethodName}\|Import Config Status is true for Vessel {VesselObjectId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L937` |
| Error | Error in {MethodName} while validating for Vessel {VesselId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L947` |
| Debug | {MethodName}\|Vessel not found in the list | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L967` |
| Error | {MethodName}\|Error while deleting Vessel to Queue | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L987` |
| Debug | {MethodName}\|Deleting Vessel from Active Queue | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L997` |
| Debug | {MethodName}\|Vessel deleted from Active Queue | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L1001` |
| Error | {MethodName}\|Vessel not found in Active Queue | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L1003` |
| Error | Error while deleting {MethodName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L1027` |
| Error | error in {methodName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExternalDataConduitBL.cs#L67` |
| Error | <ex, methodName)> | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExternalDataConduitBL.cs#L136` |
| Information | {MethodName}\|started for input {ReplicaTypeId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L57` |
| Error | {MethodName}\|ReplicaTypeId {ReplicaTypeId} not found in the configuration | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L88` |
| Error | Exception in {MethodName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L100` |
| Information | {MethodName}\|Started | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L108` |
| Information | {MethodName}\|Starting | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L165` |
| Warning | {MethodName}\| Directory resent is not enabled | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L232` |
| Information | Started processing {ReplicaMethodName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L309` |
| Information | {ReplicaMethodName}\| Export Queue Status is  {ExportQStatus}\| Resend Queue STatus is {ResendQStatus} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L315` |
| Information | {MethodName}\| Updating Initial/Cache data\| Export Queue running status {ExportQStatus}\| Resend Queue running Status : {ResendQStatus} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L318` |
| Warning | {MethodName}\| Export Queue or resend Queue already running so not changing cache data | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L328` |
| Information | Completed processing {ReplicaMethodName} with status {Status} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L375` |
| Error | Error in {ErrorMethodName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L387` |
| Warning | {MethodName}\|Export process start skipped. {DcsMessage} \| {ConfigMessage} \| {ExportMessage} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L434` |
| Information | {MethodName}\| Started Processs | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L463` |
| Error | {ErrorMethod}\|Error in InitiateResend | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L519` |
| Debug | {MethodName}\|Deleting key {Key} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L625` |
| Error | {MethodName}\|Error while deleting key {Key} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L629` |
| Information | {MethodName}\|Creating Packet for Tables for Vessel {Vessel} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L49` |
| Debug | {MethodName}\|Started Processing Normal Table:{TableName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L74` |
| Debug | {MethodName}\|Finished Processing Normal Table:{TableName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L140` |
| Information | {MethodName}\|Finished Creating packet for Vessel-{VesselObjectId} at folder Location {Location} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L160` |
| Information | {MethodName}\|Creating Attachment Packet for Tables for Vessel {VesselId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L183` |
| Debug | {MethodName}\| Attachment Base Path:{BasePath} for table {TableId}:{TableName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L276` |
| Debug | {MethodName}\|Finished Processing Attachment Table:{TableName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L347` |
| Information | {MethodName}\|Finihsed Creating attachment packet for Vessel-{Vessel} at file Location {Location} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L366` |
| Debug | {MethodName}\|Writting content to outputFile for tableId {TableId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L384` |
| Debug | {MethodName}\|Finished writting table details to file for tableId:{TableID} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L435` |
| Information | {MethodName}\|Writting physical attachment to zip file | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L441` |
| Debug | {MethodName}\|Checking for file {PhysicalFile} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L448` |
| Debug | {MethodName}\|Reading and zipping file {PhysicalFile} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L451` |
| Debug | {MethodName}\|Physical file json written to zip file with name {FileName}.{Ext} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L468` |
| Debug | {MethodName}\|Physical file written to zip file with name {NewName}.{Ext} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L474` |
| Information | {MethodName}\|Finished writting {Count} of physical attachment to zip file | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L477` |
| Debug | {MethodName}\|Writting Meta Info to zip file | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L483` |
| Debug | {MethodName}\|Packet meta information has been written to packet with file name {FileName}.{Ext} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L497` |
| Debug | {MethodName}\|New Packet Name Generated: {PacketName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsGenerator.cs#L519` |
| Debug | {MethodName}\|Started moving file | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsTransportHandler.cs#L44` |
| Error | Error while processing {MethodName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsTransportHandler.cs#L62` |
| Information | {MethodName}\|Started setting export Model | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsTransportHandler.cs#L145` |
| Error | {MethodName}\|Error in transfering file with error message {Msg} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsTransportHandler.cs#L173` |
| Debug | {MethodName}\| Checking if packet {PacketName} exist in folder Location {LocationList} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsTransportHandler.cs#L201` |
| Warning | {MethodName}\|Directory does not exist {DirectoryName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsTransportHandler.cs#L210` |
| Debug | {MethodName}\|File does not exist in directory {DirectoryName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsTransportHandler.cs#L220` |
| Warning | {MethodName}\|File count does not match split count for packet {PacketName} in directory {DirectoryName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsTransportHandler.cs#L226` |
| Warning | {MethodName}\|No valid resend files found for PacketName {PacketName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsTransportHandler.cs#L237` |
| Error | Error in {MethodName} when checking for PacketName {PacketName} in directories {DirecotryList} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsTransportHandler.cs#L246` |
| Information | {MethodName}\|Started Export Process Cycle | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L70` |
| Critical | {MethodName}\|Unique Code is empty or 0, exiting process | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L95` |
| Critical | {MethodName}\|Unique Id is empty or 0, exiting process | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L101` |
| Debug | {MethodName}\|Reading Record Vessel Sync Table Meta Data for export Data Type :{ReplicaTypeName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L109` |
| Error | {MethodName}Awaiter status is failed, exiting process | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L115` |
| Information | {MethodName}Export Record Vessel Sync Meta Table data gotten is null or empty | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L126` |
| Debug | {MethodName}\|-1 detected pushing data to recordVslMetaInfo | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L135` |
| Error | {MethodName}\|Error while path configuration for Vessel {Vessel} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L157` |
| Debug | {MethodName}\|Delete Status for Vessel {AllVessel} is {AllVesselStatus} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L190` |
| Debug | {MethodName}\|Delete Export Record Vessel Sync Meta Info for export data type:{ReplicaType} -{Name} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L193` |
| Debug | {MethodName}\|Delete Status for Export Record Vessel Sync Meta Info is {DeleteStatus} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L195` |
| Information | {MethodName}\|Finished Export Process Cycle | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L197` |
| Information | {MethodName}\|Invoking next service | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L202` |
| Information | {MethodName}\|Started Processing export data for vessel {VesselId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L226` |
| Error | {MethodName}\| Error packetCounter not gotten against Vessel {VesselId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L243` |
| Throw:InvalidOperationException | {0}\| Error packetCounter not gotten against Vessel {1} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L244` |
| Error | {MethodName}\|Error pushing Vessel {VesselId} to Active Vessel Dictionary | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L259` |
| Throw:InvalidOperationException | {0}\|Error pushing Vessel {1} to Active Vessel Dictionary | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L260` |
| Error | {MethodName}\|Error getting Vessel Config Info for Vessel {Vessel}} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L267` |
| Throw:InvalidOperationException | {0}\|Error getting Vessel Config Info for Vessel {1} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L268` |
| Throw:InvalidOperationException | {0}\|NO Pending Table Id found aginst vessel: {1} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L279` |
| Error | {MethodName}\|Packet Creation crashed for {Vessel} so aborting | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L298` |
| Throw:InvalidOperationException | {0}\|Packet Creation crashed for {1} so aborting | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L299` |
| Throw:InvalidProgramException | {0}\|Error while moving packet {1} or updating packetCOunter {2} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L311` |
| Error | {MethodName}\| Error packetCounter not gotten against Vessel {VesselObjectId} when processign -1 vessel | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L330` |
| Error | {MethodName}\|Error while deleting generatedPackets | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L366` |
| Debug | {MethodName}\|Deleted Generated packets | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L368` |
| Debug | {MethodName}\|cache Delete status for vessel {Vessel} is {CacheDeleteStatus} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L372` |
| Information | {MethodName}\|Delete Status for Vessel {Vessel} with record Id and Table Id is {DeleteStatus} for batch {BatchCount} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L390` |
| Information | {MethodName}\|Delete Status for Vessel {Vessel} with record Id and Table Id is {DeleteStatus} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L398` |
| Information | {MethodName}\| Finished Processing for Vessel {Vessel} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L404` |
| Error | Error in {MethodName} in loop for vessel {Vessel} input {Input} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L413` |
| Error | {MethodName}\|Cache Delete status for vessel {VesselObjectId} is {CacheDeleteStatus} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L431` |
| Debug | {MethodName}\|Packet Move Status for Vessel {VesselId} is {FileMoveStatus} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L486` |
| Error | {MethodName}\|Packet Move Status for Vessel {VesselObjectId} is {FileMoveStatus} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L489` |
| Throw:InvalidOperationException | {0}\|Packet Move Status for Vessel {1} is {2} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L490` |
| Error | {MethodName}\|Error updating packet counter for Vessel {VesselId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L497` |
| Throw:InvalidOperationException | {0}\|Error updating packet counter for Vessel {1} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L498` |
| Debug | {MethodName}\|Packet Counter updated successfully for vessel {VesselId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L501` |
| Debug | {MethodName}\|Packet Transfer Success for Vessel {VesselId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L508` |
| Error | {MethodName}\|Packet Transfer Failed for Vessel {VesselId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L512` |
| Error | {MethodName}\|Error saving to OutPacketHd for Vessel {VesselId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L542` |
| Debug | {MethodName}\|Saved to OutPacketHd for Vessel {VesselId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L545` |
| Information | {MethodName}\| Packet process completed for file {FileName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L547` |
| Debug | {MethodName}\|Updating packet counter for {PacketCounter}, vesselObjectId:{Vessel}, for Replication Export Type:{ReplicationExportType} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L556` |
| Debug | {MethodName}\|Checking if data exist to resent for VesselObjectId {VesselObjectId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L86` |
| Error | {MethodName}\| Error in VerifyExportConfigStatus for VesselObjectId {VesselObjectId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L92` |
| Information | {MethodName}\|No data found for VesselObjectId {VesselObjectId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L103` |
| Information | {MethodName}\|Resending data for VesselObjectId {VesselObjectId} and PacketNumber {PacketNumber} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L110` |
| Information | {MethodName}\|Resend data success for VesselObjectId {VesselObjectId} and PacketNumber {PacketNumber} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L116` |
| Error | {MethodName}\|Error in InsertAutoResendLog for VesselObjectId {VesselObjectId}, PacketNumber {PacketNumber}, ReplicaType {ReplicaTypeId} and Out Packet Id {Id} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L122` |
| Error | {MethodName}\|Resend data failed ({Reason}) for VesselObjectId {VesselObjectId}, PacketNumber {PacketNumber}, ReplicaType {ReplicaTypeId} and Out Packet Id {Id} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L127` |
| Warning | {MethodName}\|Transfer service not reachable for {FailureCount} consecutive attempts, stopping resend run at VesselObjectId {VesselObjectId}. Remaining packets are retried on the next run | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L141` |
| Error | {MethodName}\|Error in ResendData | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L154` |
| Debug | {MethodName}\| Started | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L164` |
| Error | {MethodName}\|Error in ResendFileData , no file could be found for PacketName {PacketName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L172` |
| Information | {MethodName}\|Resend process success for PacketName {PacketName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L181` |
| Error | {MethodName}\|Resend process failed ({Reason}) for PacketName {PacketName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L185` |
| Information | {MethodName}\| Starting resend processs from directory | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L210` |
| Warning | {MethodName}\|Outbox directory does not exist for VesselObjectId {VesselObjectId}. Path {OutboxPath} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L246` |
| Debug | {MethodName}\| For Vessel {VesselObject} found {FileCount} files in outbox {DirectoryName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L251` |
| Information | {MethodName}\|Resending data for VesselObjectId {VesselObjectId} and PacketName {PacketName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L257` |
| Error | {MethodName}\|Error in reading IRep file {FileName} as it does not match name pattern | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L264` |
| Information | {MethodName}\| Moving Error file to error folder {FolderName} for PacketName {PacketName} with status {Status} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L277` |
| Error | {MethodName}\|Error in moving file to error folder for PacketName {PacketName} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L281` |
| Debug | {MethodName}\|File delete for packet Name {PacketName} completed with status {Status} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L287` |
| Warning | {MethodName}\| Error folder not found for replica {Replica} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L291` |
| Debug | {MethodName}\| completed resend process for vesselobjectid {VesselobjectId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L319` |
| Warning | {MethodName}\|Transfer service not reachable for {FailureCount} consecutive attempts, stopping directory resend run at VesselObjectId {VesselObjectId}. Remaining files are retried on the next run | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L323` |
| Error | Error in {MethodName}, while processing for replica Type {Replica} and DB Connection {ExportDBConnection} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L334` |
| Debug | {MethodName}\| Started process | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L344` |
| Throw:NotSupportedException | <)> | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/StreamUtil/FileChunkWriterStream.cs#L25` |
| Information | {ClassName} {MethodName} started | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Validation/ConfigEvaluationBL.cs#L113` |
| Information | {ClassName} {MethodName} completed, Overall: {Overall}, Fail: {FailCount}, Warn: {WarnCount} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Validation/ConfigEvaluationBL.cs#L138` |
| Error | {ClassName} {Area} {Check} failed, ErrorMessage: {ErrorMessage} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Validation/ConfigEvaluationBL.cs#L1036` |
| Debug | {MethodName}\|for API Address:{1}{2} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Validation/ValidateConfig.cs#L26` |
| Throw:ArgumentNullException | Base address is null or empty | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Validation/ValidateConfig.cs#L28` |
| Throw:ArgumentNullException | End point address is null or empty | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Validation/ValidateConfig.cs#L30` |
| Error | {MethodName}\| ConfigPathEntity not found for vesse ObjectId {VesselId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Validation/ValidateConfig.cs#L39` |
| Error | {MethodName}\| ConfigPath gotten is null or empty for import Vessel {VesselId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Validation/ValidateConfig.cs#L45` |
| Error | {MethodName}\| ConfigPath gotten is null or empty for import config Vessel {VesselId} | `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Validation/ValidateConfig.cs#L51` |
| Throw:ArgumentNullException | <nameof(serviceConfig))> | `ExportDCS/Mariapps.PAL.RepExportDCS/ServiceClient/CommonIntServiceClient.cs#L34` |
| Debug | {MethodName}\| Calling method with no input | `ExportDCS/Mariapps.PAL.RepExportDCS/ServiceClient/CommonIntServiceClient.cs#L55` |
| Debug | {MethodName}\|RESPONSE\|{Output} | `ExportDCS/Mariapps.PAL.RepExportDCS/ServiceClient/CommonIntServiceClient.cs#L62` |
| Error | {MethodName}\|Exception | `ExportDCS/Mariapps.PAL.RepExportDCS/ServiceClient/CommonIntServiceClient.cs#L72` |
| Debug | {MethodName}\|Executing Post Request:{ServiceBaseAddress}{ServiceApiAddress}, with input {InputBo}  | `ExportDCS/Mariapps.PAL.RepExportDCS/ServiceClient/CommonIntServiceClient.cs#L80` |
| Debug | {MethodName}\|API RESULE: {Result} | `ExportDCS/Mariapps.PAL.RepExportDCS/ServiceClient/CommonIntServiceClient.cs#L87` |
| Debug | {MethodName}\|Executing Post Request:{ServiceBaseAddress}{ServiceApiAddress}, with input {Input}  | `ExportDCS/Mariapps.PAL.RepExportDCS/ServiceClient/NextServiceCallerServiceClient.cs#L85` |
| Debug | {MethodName}\| Calling method with input {InputJson} | `ExportDCS/Mariapps.PAL.RepExportDCS/ServiceClient/TransferServiceClient.cs#L59` |
| Debug | {MethodName}\|Executing Post Request:{ServiceBaseAddress}{ServiceApi}, with input {InputJson}  | `ExportDCS/Mariapps.PAL.RepExportDCS/ServiceClient/TransferServiceClient.cs#L104` |
| Throw:HttpRequestException | Transfer service unavailable, HTTP {(int)response.StatusCode} {response.StatusCode} | `ExportDCS/Mariapps.PAL.RepExportDCS/ServiceClient/TransferServiceClient.cs#L112` |
| Information | {MethodName}\|Process cycle Start | `ExportDCS/Mariapps.PAL.RepExportDCS/WorkerService.cs#L60` |
| Information | {MethodName}\|Ended export process for all replica type with end status {StatusCode} and message {Message} | `ExportDCS/Mariapps.PAL.RepExportDCS/WorkerService.cs#L64` |
| Information | {MethodName}\|Ended directory resend process with end status {StatusCode} and message {Message} | `ExportDCS/Mariapps.PAL.RepExportDCS/WorkerService.cs#L72` |
| Information | {MethodName}\|Process cycle Ends | `ExportDCS/Mariapps.PAL.RepExportDCS/WorkerService.cs#L76` |
| Information | {MethodName}\|Cancellation requested, stopping | `ExportDCS/Mariapps.PAL.RepExportDCS/WorkerService.cs#L85` |

## ImportDES

Logger templates in ImportDES. Keywords: ImportDES log, error.

| Level | Message template | Source |
|---|---|---|
| Error | {MethodName}\|Connection failed, Server: {Server}, Database: {Database}, ErrorMessage: {ErrorMessage} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ConfigProbeRepository.cs#L73` |
| Throw:ArgumentNullException | {0}\| DB Connection string gotten is null | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L28` |
| Debug | {MethodName}\|Started processing tableId {TableId} name {TableName}, record count {Count} with extension {Extension} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L35` |
| Throw:ArgumentException | Invalid extension | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L42` |
| Debug | {MethodName}\|Ended processing tableId {TableId} name {TableName}, record count {Count} with extension {Extension} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L58` |
| Information | {MethodName}\|Started processing tableId {TableId}, record count {Count} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L67` |
| Throw:InvalidOperationException | Destination column '{columnOrderList[i].ColumnName}' was not found in bulk-copy data table for {tableName}. | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L106` |
| Error | {MethodName}_[DATA_SKIPPED]\|Skipping row ID {RowId} for table {TableId} packet {PacketCounter} vessel {VesselObjectId}, column {ColumnName} value could not be stored | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L128` |
| Warning | {MethodName}\|Skipped {SkippedCount} of {Count} rows for table {TableId} due to data type mismatch | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L136` |
| Warning | {MethodName}\|No valid rows left to write for table {TableId} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L141` |
| Warning | {MethodName}\|Bulk write rejected row data for table {TableId}, record Count {Count}. {ColumnDiagnostics} Retrying in smaller parts to skip only the bad rows | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L172` |
| Warning | {MethodName}\|Bulk write finished for table {TableId}, skipped {SkippedCount} of {Count} rows rejected by the office table | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L177` |
| Error | {MethodName}\|Bulk write failed for table {TableId}, record Count {Count} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L186` |
| Information | {MethodName}\|Ended processing table {TableId}, record Count {Count} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L190` |
| Error | {MethodName}_[DATA_SKIPPED]\|Skipping row ID {RowId} for table {TableId} packet {PacketCounter} vessel {VesselObjectId}, rejected by the office table. {ColumnDiagnostics} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L229` |
| Error | {MethodName}\|Delete bulk write failed for table {TableId}, record Count {Count} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L338` |
| Debug | {MethodName}\|Started Clearing Replica Tables for packetNumber : {PacketNumber}\| VesselObjectId :{VesselId} for table Id : {TableId} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L350` |
| Error | Error in {MethodName} when deleting table {TableId} packet Number {PacketNumber} for Vessel {VesselObjectId}  with query {Query}  | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/DesInsertRepository.cs#L368` |
| Debug | {MethodName}\|Reading config paths | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ExportDbRepository.cs#L34` |
| Debug | {MethodName}\|reading config path ended, data count {Count} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ExportDbRepository.cs#L61` |
| Error | Error in {MethodName} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ExportDbRepository.cs#L70` |
| Debug | {MethodName}\|Saving packet details to InPacketHd | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ExportDbRepository.cs#L81` |
| Information | {MethodName}\| Output parameter value for saving Packet {Number}, vessel {VesselId} is {OutputParamValue} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ExportDbRepository.cs#L105` |
| Debug | {MethodName}\|Reading Rep Type Master Data | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ExportDbRepository.cs#L135` |
| Debug | {MethodName}\|Reading environment unique details | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ExportDbRepository.cs#L184` |
| Debug | {MethodName}\| ReadingExportTableOrder Data | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L83` |
| Debug | {MethodName}\|Ended, Table Order list read | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L121` |
| Error | Error in {MethodName}, while reading data with parameter transferApplicable Type: {TransferAppType} and replicationType:{ReplicaTypeId} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L130` |
| Debug | {MethodName}\| ReadingPacketCounter Data | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L143` |
| Error | Error in {MethodName}, while reading last in packet counter data  | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L183` |
| Debug | {MethodName}\|Reading Import Config Path against each vessel  Data | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L196` |
| Debug | {MethodName}\|Ended, Read import config path | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L233` |
| Debug | {MethodName}\| Reading Pending Data from Des valid Q for type :{Type} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L256` |
| Debug | {MethodName}\|Ended,Read all pending data from Des Valid Q got vessel {Vessel} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L291` |
| Error | Error in {MethodName} whil reading data against for type {Type} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L300` |
| Debug | {MethodName}\|Deleting DES VAlid Q data by Ids | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L310` |
| Debug | {MethodName}\|Deleting DES VAlid Q data by dataset | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L350` |
| Debug | {MethodName}\|Adding new item to Des Process Q | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L396` |
| Error | Error in {MethodName} using connection string {ConnString} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L431` |
| Debug | {MethodName}\| Reading Pending Data from Process Q for type :{Type} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L447` |
| Debug | {MethodName}\|Ended,Read first process Q data, got packetName {PacketName} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L480` |
| Error | Error in {MethodName} whil reading Process Q data against for type {ReplicaTypeId} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L489` |
| Debug | {MethodName}\|Adding live table {TableId} to Des Process Q live data for  {VesselObjectId} with packetCounter {PacketCounter} and Type {Type}  | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L499` |
| Error | Error in {MethodName} for processing  table {TableId} for {VesselObjectId} with packetCounter {PacketCounter}  | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L540` |
| Debug | {MethodName}\|Clearing des process q data against {VesselObjectId} with packetCounter {PacketCounter} and Type {Type}  | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L551` |
| Error | Error in {MethodName} while clearing for {VesselObjectId} with packetCounter {PacketCounter} and type {Type}  | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L588` |
| Debug | {MethodName}\|Deleting DES Process Q data by Ids | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L598` |
| Information | {MethodName}\|saving import queue data with parameters {VesselObjectId},   packetCounter {PacketCounter} and replication dataType: {ReplicaTypeId}  | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L645` |
| Information | {MethodName}\| Output parameter value for saving with parameters {VesselObjectId},   packetCounter {PacketCounter} and replication dataType: {ReplicationDataType} is {Output}  | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L668` |
| Error | Error in {MethodName} while saving to import queue for {VesselObjectId} and packetCounter {PacketCounter} for Replica Type {TypeId} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L682` |
| Information | {MethodName}\|Saving missing table entry for Table {TableId}:{TableName} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L692` |
| Error | {MethodName}\|Saving missing table entry for Table {TableId}:{TableName} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L728` |
| Debug | {MethodName}\|Start | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L740` |
| Debug | {MethodName}\|Updating process q item with id: {Id} with retry count {Count} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L783` |
| Error | Error in {MethodName} for Updating process q item with id: {Id} with retry count {Count} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L817` |
| Debug | {MethodName}\|Insert Process Q stop time {TimeName} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L827` |
| Debug | {MethodName}\|Handling Des Process Q error files for {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L873` |
| Error | Error in {MethodName} for processing {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L907` |
| Debug | {MethodName}\|clearing Des Process Q list for {VesselObjectId} with packetCounter {PacketCounter}  | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L917` |
| Error | Error in {MethodName} for processing {VesselObjectId} with packetCounter {PacketCounter}  | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L952` |
| Debug | {MethodName}\|Inserting packet {PacketName} for vessel {VesselObjectId}  with packetNumber {PacketCounter} before skipping | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L962` |
| Warning | {MethodName}\|Skipped packet already exists. Treating as success for PacketName {PacketName}, Vessel {VesselObjectId}, PacketCounter {PacketCounter} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L997` |
| Error | Error in {MethodName} when processing PacketName {PacketName} for {VesselObjectId} with packetCounter {PacketCounter}  | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L1006` |
| Debug | {MethodName}\|Reading Des Process Live Table for  {VesselObjectId} with packetCounter {PacketCounter} and Type {Type}  | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L1020` |
| Debug | {MethodName}\|Ended,Read all active tableId from Des Live Data Table | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L1050` |
| Error | Error in {MethodName} for {VesselObjectId} with packetCounter {PacketCounter}  | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L1059` |
| Debug | {MethodName}\|Clearing live data against {VesselObjectId} with packetCounter {PacketCounter} and Type {Type}  | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L1068` |
| Debug | {MethodName}\| Reading Replica removing query Data | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L1113` |
| Debug | {MethodName}\|Ended, read Replica remove query | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L1148` |
| Error | Error in {MethodName}, while reading data with parameter transferApplicable Type: {TransferAppType} and replicationDataType:{ReplicationDataTyp} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L1157` |
| Debug | {MethodName}\|Saving packet status | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L1170` |
| Error | Error in {MethodName} when saving for Vessel {Vessel} with packetr counter {Counter} | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L1208` |
| Debug | {MethodName}\|Saving packet status bulk | `ImportDES/Mariapps.PAL.RepImportDES.DAL/Repository/ImportRepository.cs#L1219` |
| Debug | {MethodName}\|Reading all cache keys | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L64` |
| Error | {MethodName}\|ReplicaTypeId {ReplicaTypeId} not found in the configuration | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L99` |
| Error | {MethodName}\|Error in reading all cache keys | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L109` |
| Information | {MethodName}\|started for input {ReplicaTypeId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L119` |
| Error | Exception in {MethodName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L160` |
| Debug | {MethodName}\|Deleting key {Key} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L182` |
| Error | {MethodName}\|Error while deleting key {Key} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L186` |
| Information | {MethodName}\|Started | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L204` |
| Information | {MethodName}\|Starting | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L260` |
| Error | {MethodName}\|No replica configuration loaded from common integration service | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L280` |
| Information | Started processing {ReplicaMethodName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L342` |
| Information | {ReplicaMethodName}\| ValidateQStatus {ValidateQStatus}\|ReadQStatus {ReadQStatus} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L347` |
| Information | {MethodName}\| Updating Initial/Cache data\| Process Q running status {ProcesssQStatus}\| Validate Q running status {ValidateQStatus} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L350` |
| Error | {MethodName}\| Process already running so not changing cache data | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L361` |
| Information | Completed processing {ReplicaMethodName} with status {Status} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L383` |
| Error | Error in {ReplicaMethodName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L394` |
| Information | {MethodName}\| Started Validate Import | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L405` |
| Error | {MethodName}\|Validate import run failed | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L436` |
| Error | {MethodName}\|{Message} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L462` |
| Information | {MethodName}\| Started Reading process | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L479` |
| Error | {MethodName}\|Packet read run failed | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L505` |
| Warning | {MethodName}\|{Message} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L530` |
| Information | {MethodName}\|{Message} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/CommonProcessBL.cs#L534` |
| Information | {MethodName}\|Completed, Overall: {Overall}, Fail: {FailCount}, Warn: {WarnCount} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/ConfigEvaluationBL.cs#L144` |
| Error | {MethodName}\|{Area} {Check} failed | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/ConfigEvaluationBL.cs#L1070` |
| Debug | {MethodName}\|Started moving file | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/FileOperationBL.cs#L43` |
| Debug | {MethodName}\|File {FileName} already exists in destination | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/FileOperationBL.cs#L55` |
| Error | {MethodName}\|IO error moving for file List: {FileLocation} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/FileOperationBL.cs#L78` |
| Error | {MethodName}\|IO error moving for file List: {FileList} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/FileOperationBL.cs#L84` |
| Error | {MethodName}\|Access error moving for file List: {FileList} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/FileOperationBL.cs#L89` |
| Error | Error while processing {MethodNAme} fileList :{FileList} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/FileOperationBL.cs#L94` |
| Throw:ArgumentException | Filename is not in the correct format. | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/FileOperationBL.cs#L111` |
| Debug | {MethodName}\|Attachment {Name} moving to full path {AttachmentFullPath} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/FileOperationBL.cs#L153` |
| Throw:InvalidOperationException | Attachment full path not found for table {tableName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/FileOperationBL.cs#L156` |
| Throw:InvalidOperationException | Attachment relative path {physAttachmentMetaInfo.RelativePath} resolves outside base path for table {tableName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/FileOperationBL.cs#L162` |
| Error | Error in {MethodName}\|Packet stream corrupt while writing attachment {Name} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/FileOperationBL.cs#L189` |
| Warning | {MethodName}\|Unable to delete partial attachment {Path} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/FileOperationBL.cs#L207` |
| Debug | {MethodName}\|Checking file: {FileName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/FileOperationBL.cs#L215` |
| Error | {MethodName}\|Error in checking file lock | `ImportDES/Mariapps.PAL.RepImportDES/BL/Common/FileOperationBL.cs#L252` |
| Error | error in {methodName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ExternalDataConduitBL.cs#L74` |
| Error | <ex, methodName)> | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ExternalDataConduitBL.cs#L143` |
| Debug | {MethodName}\| Setting Key data for replica type {TypeName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L54` |
| Information | {MethodName}\|Setting cache data on Init | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L58` |
| Debug | {MethodName}\|Config read status to cache result: {Result} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L92` |
| Debug | {MethodName}\|Deleting all vessel in skip vessel list {Key} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L94` |
| Information | {MethodName}\|Settings to cache ended\|Config Status {Result} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L97` |
| Error | {MethodName}\|Error while settign Initial Data | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L110` |
| Debug | {MethodName}\|Started | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L120` |
| Debug | {MethodName}\|Replica Type Master data gotten and saving it to Key {KeyName}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L127` |
| Debug | {MethodName}\|Replica Type Master data  cache save result: {ResultSTatus} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L130` |
| Error | {MethodName}\|Replica Type Master data  not found | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L134` |
| Debug | {MethodName}\|Ended | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L137` |
| Warning | {MethodName}\|No table order for TransferAppType {TransferAppType}, retrying with BOTH | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L154` |
| Debug | {MethodName}\|Import Table Order Data exists Record count:{Count}\| saving to cache key {KeyName}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L160` |
| Debug | {MethodName}\|Saving Import Table Order Data  to cache result: {Result} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L163` |
| Warning | {MethodName}\|No Import Table order data found | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L167` |
| Debug | {MethodName}\|Replica Import Queries exists Record count:{Count}\| saving to cache key {KeyName}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L194` |
| Debug | {MethodName}\|Saving Replica Import Queries Data  to cache result: {Result} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L197` |
| Warning | {MethodName}\|No replica remove query data found | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L201` |
| Debug | {MethodName}\|Setting import packet counter for Vessel {VesselId} with key {PacketCounterKey} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L237` |
| Debug | {MethodName}\|Saving Import Packet Counter data to cache result: {Result} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L240` |
| Error | {MethodName}\|No Import Packet Counter data found | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L247` |
| Debug | {MethodName}\| Setting ActiveVessels to cache | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L269` |
| Debug | {MethodName}\| Setting ActiveVessels to cache result {Status} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L271` |
| Debug | {MethodName}\|Environment Details exists with VesslObjectId :{VesselId}\| saving to cache key {KeyName}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L299` |
| Debug | {MethodName}\|Saving Environment Details to cache result: {StatusResult} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L302` |
| Error | {MethodName}\|No Environment Details data found | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L306` |
| Information | {MethodName}\|Started pushing Error Packet Counter data count {Count} to vessel {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L329` |
| Debug | {MethodName}\|Setting Active Skip Vessels to cache with count before {Count} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L333` |
| Debug | {MethodName}\|Setting Active Skip Vessels to cache with count after {Count} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L337` |
| Information | {MethodName}\|Ended pushing Error Packet Counter Data count {Count} to vessel {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L339` |
| Error | Error in {MethodName} while pushing error packet counter data count {Count} to Vessel {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L344` |
| Debug | {MethodName}\| Setting Vessel {VesselId} to memory | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L354` |
| Debug | {MethodName}\| Setting Vessel {VesselId} to queue | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L371` |
| Debug | {MethodName}\|Append result: {Result} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L382` |
| Debug | {MethodName}\|Environment default config path found, saving to cache key {Key}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L417` |
| Debug | {MethodName}\|Saving Environment Details to cache result: {Result} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L420` |
| Error | {MethodName}\|Environment default config paths not found | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L424` |
| Debug | {MethodName}\|Saving Vessel import Config Path\| Record count:{Count} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L451` |
| Debug | {MethodName}\|Saving import config path Data  to cache result: {Result} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L454` |
| Error | {MethodName}\|No Vessel Config Path data found | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L459` |
| Error | {MethodName}\|Error while setting import vessel config path to cache | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L469` |
| Information | {MethodName}\| updatin cache packetnumer for VesselObjectId {VesselId} with PacketNumber {PacketNumber} for key {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L480` |
| Information | {MethodName}\| updatin cache packetnumer for VesselObjectId {VesselId} with PacketNumber {PacketNumber}, index found \| key Name {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L485` |
| Information | {MethodName}\|cache Update status for VesseObjectId {VesselId} with PacketNumer {PacketCounter} is {Status}, last in packet number {LastInPacketId}\|KeyName {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L491` |
| Debug | {MethodName}\| Saving packet Status for vessel {VesselObjectId} for number {PacketCtr} with status {Status} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L516` |
| Error | {MethodName}\|Error while saving to packet status | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L521` |
| Debug | {MethodName}\|Saved to packet status | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L524` |
| Error | Error in {MethodName} for processing Packet Counter {Number} and Vessel {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L532` |
| Debug | {MethodName}\|Started Creating Missing table Id for Table Id {TableId} and Name {TableName}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L539` |
| Error | {MethodName}\|Error while saving Missing Table Id for Table Id {TableId} and Name {TableName}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L544` |
| Debug | {MethodName}\|Saved Missing Table Id for Table Id {TableId} and Name {TableName}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L549` |
| Debug | {MethodName}\|Reading Replica Type Master Data List | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L581` |
| Error | {MethdName}\|Replica Type Master Data not found in cache, reading from DB | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L586` |
| Debug | {MethodName}\|Replica Type Master Data Found in cache | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L591` |
| Error | Error while reading {MethodName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L601` |
| Debug | {MethodName}\|Started reading Config Status from {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L654` |
| Debug | {MethodName}\|Config status is true | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L660` |
| Error | {MethodName}\|Config Status is false, ReInitialize the Service startup config | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L665` |
| Error | {MethodName}\|Error while reading Config Status | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L675` |
| Debug | {MethodName}\|Read Started | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L685` |
| Error | {MethodName}\|Import Table Data not found in cache, reading from DB | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L693` |
| Debug | {MethodName}\|Import Table Order Data Found in cache | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L698` |
| Error | {MethodName}\|Error while reading Import Table order Data | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L709` |
| Debug | {MethodName}\|Started reading all vessel packetCounter for key {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L718` |
| Error | {MethodName}\|No active vessel was foudn with {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L727` |
| Error | {MethodName}\|Vessel Packet Counter not found for Vessel {VesselId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L738` |
| Error | {MethodName}\|Error while reading Vessel Packet Counter Data | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L747` |
| Error | {MethodName}\|No Vessel Packet Counter Data found | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L751` |
| Debug | {MethodName}\|Vessel Packet Counter Data found | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L753` |
| Debug | {MethodName}\|Started reading vessel packetCounter for key {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L760` |
| Information | {MethodName}\|Vessel packet counter data not found in cache, reading from DB | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L768` |
| Throw:InvalidOperationException | Vessel Packet Counter not found in DB | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L777` |
| Debug | {MethodName}\|Vessel Packet counter data gotten for Vessel {VesselObjectId} and Packet Counter {PacletCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L780` |
| Debug | {MethodName}\|Started reading Current Environment Deats for key {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L799` |
| Error | {MethodName}\|Current Environment Deats not found in cache, reading from DB | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L809` |
| Debug | {MethodName}\|Current Environment Deatsa Found in cache | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L814` |
| Error | {MethodName}\|Error while reading Current Environment Deats | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L825` |
| Debug | {MethodName}\|Started reading Error packet list for {ReplicaTypeId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L840` |
| Error | {MethodName}\|Error while reading all Error Packet data from Dictionary | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L848` |
| Debug | {MethodName}\|Started reading currently processing Vessel list for {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L856` |
| Information | {MethodName}\|No Vessel is being processed now  for key {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L862` |
| Debug | {MethodName}\|Read currently Proecssing List for {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L867` |
| Information | {MethodName}\|No active vessel was found with {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L882` |
| Debug | {MethodName}\|Started reading Current Environment default path configs for key {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L899` |
| Information | {MethodName}\|Current environment default config paths not found in cache, reading from DB | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L907` |
| Debug | {MethodName}\|Started reading import config path for key {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L920` |
| Information | {MethodName}\|Import config path not found in cache, reading from DB | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L928` |
| Debug | {MethodName}\|Started reading replica remove queries for key {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L941` |
| Information | {MethodName}\|Replica remove queries not found in cache, reading from DB | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L949` |
| Information | {MethodName}\|Validating vessel : {VesselId}, packet counter {PacketCounter} from packetCounterKey {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L966` |
| Information | {MethodName}\| Invalid packet counter found for vessel {VesselObjectId} and type {ReplicaTypeId}, last cache packet Number {LastPacketNumber} in cache key {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L975` |
| Information | {MethodName}\|Missing packet counter found in error list for vessel {VesselObjectId} and type {ReplicaTypeId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L980` |
| Warning | {MethodName}\|Missing packet status persistence failed for vessel {VesselObjectId} and type {ReplicaTypeId} in range {StartCounter}-{EndCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1018` |
| Warning | {MethodName}\|Packet counter is not the latest and is missing {MissingCounterCount} counters for vessel {VesselObjectId} and type {ReplicaTypeId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1021` |
| Debug | {MethodName}\| Packet Counter is the latest and is correct for vessel {VesselId} and type {RepliaTypeId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1026` |
| Information | {MethodName}\|Packet counter is old and skipping for Vessel {VesselId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1031` |
| Error | Error in {MethodName}\|while validating vessel : {VesselId}, packet counter {PacketCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1041` |
| Information | {MethodName}\|Checking Missing Packet in Error for Vessel {VesselId} packet counter list for packetCounter Between the range {MinPacketCounter} and {MaxPacketCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1049` |
| Error | {MethodName}\|Error while checking for Vessel {Vessel} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1095` |
| Debug | {MethodName}\|Bulk missing packet status insert failed for vessel {VesselObjectId} and type {ReplicaTypeId} in range {StartCounter}-{EndCounter}; trying single-row fallback | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1112` |
| Warning | {MethodName}\|Bulk missing packet status insert failed, but single-row fallback succeeded for vessel {VesselObjectId} and type {ReplicaTypeId} in range {StartCounter}-{EndCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1127` |
| Debug | {MethodName}\|Single-row fallback also failed for {FailedCount} missing packet counters for vessel {VesselObjectId} and type {ReplicaTypeId} in range {StartCounter}-{EndCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1131` |
| Debug | {MethodName}\|Started reading error path for type: {ExportType} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1141` |
| Debug | {MethodName}\|Started reading retry limit | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1153` |
| Debug | {MethodName}\|Error Await Timer is {RetryLimit} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1170` |
| Throw:InvalidOperationException | Replica Type Master Data not found for Id {replicaTypeId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1179` |
| Debug | {MethodName}\|Started reading Table Order Data for table Id {TableId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1205` |
| Error | {MethodName}\|Table Order Entity not found for TableId {TableId}, creating it | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1213` |
| Error | {MethodName}\|Missing Table Order Entity not found after creating for TableId {TableId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1221` |
| Throw:InvalidOperationException | Missing Table Order Entity not found after creating for TableId {tableId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1222` |
| Information | {MethodName}\|Table Order Entity found for TableId {TableId}\|{TableData} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1230` |
| Debug | {MethodName}\| verifying configuration for vessel {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1238` |
| Error | {MethodName}\|Import Config Status is false for Vessel {VesselObjectId} \| adding it to failed Vessel List | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1249` |
| Debug | {MethodName}\|Import Config Status is true for Vessel {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1256` |
| Error | Error in {MethodName} while validating for Vessel {VesselId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1266` |
| Debug | {MethodName}\|Reading last packet counter for vessel : {VesselId} from packetCounterKey {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1274` |
| Error | Error in {MethodName}\|readind last packet number for vessel : {VesselId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1286` |
| Debug | {MethodName}\|started error packet counter validation for vessel {VesselObjectId} and PacketCounter {PacketCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1295` |
| Debug | {MethodName}\|Error Packet Counter Deleted for vessel {VesselObjectId} and PacketCounter {PacketCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1322` |
| Warning | {MethodName}\|Retained {RetainedCount} future error packet counters for vessel {VesselObjectId}. Current packet {PacketCounter}, retained range {FirstPacketCounter} to {LastPacketCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1334` |
| Debug | {MethodName}\|Deleted {DeletedCount} stale error packet counters for vessel {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1339` |
| Error | {MethodName}\| error packet validation failed | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1345` |
| Debug | {MethodName}\| Finished | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1347` |
| Information | {MtehodName}\|Vessel {Vessel} not found in the list | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1367` |
| Information | {MethodName}\|Vessel {Vessel} removed from the memeory list | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1375` |
| Information | {MethodName}\| No Vessel found in the cache list when trying to remove vesseln {Vessel} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1382` |
| Error | {MethodName}\|Error while deleting Vessel to Queue | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1392` |
| Debug | {MethodName}\|Correct packet counter gotten for vessel {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1406` |
| Information | {MethodName}\|Error Packet Counter Count for vessel {VesselObjectId} is {ErrorCounterCount}\| Removing it all | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1409` |
| Information | {MethodName}\|Error Packet Counter Count for vessel {VesselObjectId} After removal is {ErrorCounterCount} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1412` |
| Error | Error in {MethodName} while deleting error Vessels {VesselId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1417` |
| Information | {MethodName}\|Delete started | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1426` |
| Information | {MethodName}\|Delete Ended with Status {Status} | `ImportDES/Mariapps.PAL.RepImportDES/BL/DataConduitMethods/ImportDesDataConduitBL.cs#L1430` |
| Information | {MethodName}\|Started processing packet {PacketName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L64` |
| Information | {MethodName}\|Ended Processing packet {PacketName} with status {PacketReaderStatus} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L75` |
| Error | {MethodName}\|End of stream exception | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L84` |
| Error | {MethodName}\|Invalid packet data while reading compressed stream | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L92` |
| Debug | {MethodName}\| starting reader process | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L115` |
| Debug | {MethodName}\|Starting to read packet meta info for table with extenstion {Ext}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L146` |
| Debug | {MethodName}\|Packet created date found for table with extenstion {Ext}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L153` |
| Warning | {MethodName}\|Packet created date not found for table with extenstion {Ext}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L158` |
| Debug | {MethodName}\|Finished reading packet meta info for table with extenstion {Ext}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L161` |
| Throw:InvalidOperationException | Table name read from Json is null or empty for tableId {tableId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L185` |
| Error | {MethodName}\| In packet {PacketCounter} Table {TableName} schema comparison failed when checking with {Json} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L197` |
| Throw:InvalidOperationException | Table name structure not gotten for table {currentTableName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L198` |
| Information | {MethodName}\|In Packet {PacketCounter} Table {TableName} for data type {Extension} schema comparison completed with column count {Count} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L201` |
| Throw:InvalidOperationException | Live data table entry failed for table {currentTableId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L207` |
| Debug | {MethodName}\|Starting to read data for table {TableName}:{TableId} with extension {Extension} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L212` |
| Debug | {MethodName}\|Finished reading data for table {TableName}:{TableId} with extension {Extension}, the data was pushed to Save method | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L240` |
| Debug | {MethodName}\|Starting to read attachment meta info for table {TableName}:{TableId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L244` |
| Error | {MethodName}\|Attachment meta info not found for table {TableId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L251` |
| Throw:InvalidOperationException | Attachment meta info not found for table {currentTableName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L252` |
| Error | {MethodName}\| Table name not found for table {TableId} in {Extension} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L261` |
| Error | {MethodName}\| Attachment base path not found for table {TableId} in {Extension} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L267` |
| Information | {MethodName}\| Physical Attachment info gotten for file {PhysFile} with relative path {RelateivePath} for table {TableName}:{TableId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L270` |
| Error | {MethodName}\| Attachment base path not found for table {TableId} in {Extension} for {FileName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L276` |
| Information | {MethodName}\| writting attachment file {FileName} for table {TableName}:{TableId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L282` |
| Information | {MethodName}\| finished writting attachment file {FileName} for table {TableName}:{TableId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L285` |
| Error |  Error in {MethodName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/DesReaderBL.cs#L310` |
| Information | {MethodName}\|Started importing process for {TypeMaster} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L77` |
| Throw:InvalidOperationException | Retry Count gotten is 0, exiting | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L96` |
| Error | {MethodName}\|Import table order data was not gotten for replica type {ReplicaTypeId}, stopping process queue execution | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L108` |
| Error | {MethodName}\|[WAITING]\|Process queue waiting time, exiting | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L119` |
| Information | {MethodName}\| excluding vessel list {Vessel} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L131` |
| Information | {MethodName}\|Packet data gotten for with excluded vessel list {List},is file Name {PacketName} and PacketCounter {PacketCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L137` |
| Error | {MethodName}\|No valid data found in Process Queue, waiting for it to complete and retrying again | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L145` |
| Warning | {MethodName}\| No valid data found for processing | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L149` |
| Information | {MethodName}\|Concurrent Task Object is still running for Process queue, waiting for it to complete and retrying again | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L161` |
| Information | {MethodName}\| No valid data found in Process Queue nor any task process found as runningg, stopping the process | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L166` |
| Error | {MethodName} no proper type gotten after CheckDesValidStatus | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L179` |
| Error | {MethodName}\|Packet Counter is not valid or no data found, skipping this vessel {VesselObjectId} and PacketCounter {PacketCtr} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L190` |
| Error | {MethodName}\| Live data table clear failed for packet number {PacketCounter} and vesselObjectId {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L197` |
| Error | {MethodName}\|packet error hadling process status {Status}\| Skipping vessel process | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L233` |
| Information | {MethodName}\|calling next api service | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L272` |
| Debug | {MethodName}\|Rbp service call returned failure status: {Message} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L281` |
| Error | Error in {MethodNamne} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L301` |
| Debug | {MethodName}\|Checking basic data for file | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L309` |
| Information | {MethodName}\|No valid Id or VesselObjectId found for packet | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L313` |
| Error | {MethodName}\|No valid PacketName or FileLocation found for packet | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L319` |
| Error | {MethodName}\|Deleted entry with missing File Name or location successfully from Validate Q | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L325` |
| Error | {MethodName}\|Error while deleting packet with missing File Name or location from Validate Q | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L327` |
| Error | {MethodName}\|No valid PacketCounter found for packet | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L334` |
| Error | {MethodName}\|Deleted entry with packetCounter 0 successfully from Validate Q | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L340` |
| Error | {MethodName}\|Error while deleting entry with packet Counter that is 0 from Validate Q | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L342` |
| Error | {MethodName}\|Error while saving skipped data for vessel {VesselObjectId} and PacketName {PacketName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L359` |
| Error | {MethodName}\|No valid File found for packet in locatoin | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L366` |
| Error | {MethodName}\|Deleted entry with packet {PacketName} not being available in file locaiton {Location} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L373` |
| Error | {MethodName}\|Error while deleting packet {PacketName} when file not available in {Location} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L375` |
| Debug | {MethodName}\| Verify and Handle packetCounter start for counter:{PacketCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L404` |
| Error | {MethodName}\|OldPacketCounter Gotten deleting and moving for vessel {VesselObjectId} and PacketName {PacketName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L421` |
| Error | {MethodName}\| Des Process q data removed for packet number {PacketCounter} and Vessel {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L443` |
| Error | {MethodName}\| Moving all packets {FileList} with invalid packet counter {PacketCounter} to Error Folder | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L445` |
| Information | {MethodName}\| File moved to error Directory with status:{MoveStatus} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L448` |
| Error | {MethodName}\| Des Process q data remove failedv for pacektCounter {PacketCounter} and Vessel {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L453` |
| Error | {MethodName}\|Incorrect packet counter Gotten, not expected, for vessel {VesselObjectId} and PacketName {PacketName}, moving all pending packets to errorList for this vessel | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L459` |
| Error | {MethodName}\|Incorrect Packet counter gotte, not expected, Moved it to error list table status {Status} and skipping | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L473` |
| Error | {MethodName}\| Error while reading validating packetCounter\|Skipping | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L480` |
| Error | {MethodName}\| No valid packet status gotten\|skipping | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L483` |
| Information | {MethodName}\|Started reading packet {PacketName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L494` |
| Error | {MethodName} file not found for processing | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L500` |
| Information | {MethodName}\| packet is locked current so vessel is being removed from active memory | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L517` |
| Error | {MethodName}\|Handling packet read success status {Status} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L545` |
| Throw:InvalidOperationException | Error in handling success packet for read packet | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L546` |
| Error | {MethodName}\|End of stream exception while reading packet {PacketName}; increasing retry count and continuing | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L552` |
| Error | {MethodName}\|Handling packet read retry status {Status} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L568` |
| Error | {MethodName}\|Handling packet read error status {Status} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L586` |
| Error | {MethodName}\| Packet reader status is not proper for file {PacketName} reading | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L603` |
| Information | {MethodName}\| Packet Data read process finished for Vessel {VesselObjectId} with status {PacketStatus} and vessel removed from active queue memory | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L609` |
| Debug | {MethodName}\| started | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L641` |
| Error | {MethodName}\|Clearing Error process list data after success failed for Vessel {VesselObjectId} and packet number {PckCtr} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L647` |
| Information | {MethodName}\| Updating Import Q status and packet number for Vessel {VesselObjectId}, with packet Number {PacketNumber}\| cache last in Packet Number {LastInPacketCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L652` |
| Error | {MethodName}\| Saving to import q and packet counter updation data failed for pacektCounter {PacketCounter} and Vessel {VesselObjectId}\|increasing retry count and waiting | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L658` |
| Information | {MethodName}\|Replica Import Queue item added and packet counter updated to DB for vessel {VesselObjectId} with packetCounter {PacketCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L662` |
| Information | {MethodName}\|Last in packet counter updated for vessel {VesselObjectId} with packetCounter {PacketCounter} \| last in packet cache counter {LastInPacketCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L673` |
| Error | {MethodName}\|packet counter cache update failed for vessel {VesselObjectId} and packetCounter {PacketCounter} against key {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L677` |
| Debug | {MethodName}\|packet counter cache update status for vessel {VesselObjectId} is {Status} against key {KeyName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L681` |
| Information | {MethodName}\|Clearing Error packet counter for vessel {VesselObjectId}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L684` |
| Error | {MethodName}\|Error packet counter clear failed for vessel {VesselObjectId}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L690` |
| Information | {MethodName}\| ValidateQ Error packet counter has been cleared for vessel {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L694` |
| Error | {MethodName}\|packet counter cache update failed for vessel {VesselObjectId} and packetCounter {PacketCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L699` |
| Debug | {MethodName}\|packet counter cache update status for vessel {VesselObjectId} is {Status} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L701` |
| Debug | {MethodName}\| Des Process q data removed for pacektCounter {PacketCounter} and Vessel {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L724` |
| Information | {MethodName}\| File moved to completed Directory with status:{MoveStatus} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L728` |
| Debug | {MethodName}\|Checking if any live Des Process data exist for vessel {VesselObjectId} and packetCounter {PacketCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L746` |
| Warning | {MethodName}\|Replica remove query not found for tableId {TableId}, packet number {PacketCounter} and vesselObjectId {VesselObjectId}; skipping this live table | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L759` |
| Error | {MethodName}\|{ErrorMessage} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L775` |
| Throw:InvalidOperationException | <erMsg)> | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L776` |
| Debug | {MethodName}\|Live data table {TableId} cleared for packet number {PacketCounter} and vesselObjectId {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L790` |
| Debug | {MethodName}\|Live data table cleared for packet number {PacketCounter} and vesselObjectId {VesselObjectId} withs status {Status} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L795` |
| Error | {MethodName}\|Error while clearing live table | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L805` |
| Error | {MethodName}\|Retry limit reached for packet name {Name} number {PacketCounter} and vesselObjectId {VesselObjectId}, deleting and moving it to Error Q | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L819` |
| Information | {MethodName}\| Retry count updated for packet number {PacketCounter} and vesselObjectId {VesselObjectId} with count {RetryCount} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L831` |
| Error | {MethodName}\| Retry count update failed for packet number {PacketCounter} and vesselObjectId {VesselObjectId} with count {RetryCount} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L835` |
| Error | {MethodName}\|Error while setting await timer exiting process abruptly | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L846` |
| Information | {MethodName}\|Packet error handled and removing from active Vessel memory | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L852` |
| Debug | {MethodName}\|Started save to In_packet_hd | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L862` |
| Error | {MethodName}\|Error while saving to In_packet_hd | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L888` |
| Debug | {MethodName}\|Saved to In_packet_hd | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L891` |
| Debug | {MethodName}\|Started handling corrupted file | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L918` |
| Information | {MethodName}\| Packet moved to Error Q for all packet number in vesselObjectId {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L952` |
| Error | {MethodName}\| Packet move to Error Q failed for all vesselObjectId {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/ProcessQBL.cs#L956` |
| Throw:FileNotFoundException | File not found | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/StreamUtil/FileChunkReaderStream.cs#L77` |
| Throw:InvalidDataException | File is too small to be a valid chunk: {iteratingFileName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/StreamUtil/FileChunkReaderStream.cs#L97` |
| Throw:InvalidDataException | Chunk sequence is incomplete. Missing chunk: {nextExpectedChunk} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/StreamUtil/FileChunkReaderStream.cs#L142` |
| Throw:NotSupportedException | <)> | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/StreamUtil/FileChunkReaderStream.cs#L176` |
| Throw:InvalidOperationException | Stream is not initialized | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/StreamUtil/FileChunkReaderStream.cs#L222` |
| Throw:ArgumentOutOfRangeException | Offset cannot be negative | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/StreamUtil/FileChunkReaderStream.cs#L242` |
| Throw:ArgumentOutOfRangeException | Offset cannot be greater than file length | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/StreamUtil/FileChunkReaderStream.cs#L247` |
| Throw:InvalidOperationException | Could not find chunk for the given offset | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/StreamUtil/FileChunkReaderStream.cs#L263` |
| Throw:ArgumentOutOfRangeException | Invalid origin | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/StreamUtil/FileChunkReaderStream.cs#L282` |
| Throw:InvalidDataException | CRC validation failed for file: {result.Item1.FileName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/StreamUtil/FileChunkReaderStream.cs#L356` |
| Throw:ArgumentException | Stream must be seekable | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/StreamUtil/SegmentStream.cs#L44` |
| Throw:ArgumentException | Stream must be readable | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/StreamUtil/SegmentStream.cs#L49` |
| Throw:ArgumentException | Buffer is too small | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/StreamUtil/SegmentStream.cs#L97` |
| Throw:ArgumentOutOfRangeException | <nameof(offset))> | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/StreamUtil/SegmentStream.cs#L101` |
| Throw:ArgumentOutOfRangeException | <nameof(count))> | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/StreamUtil/SegmentStream.cs#L105` |
| Throw:ArgumentException | Invalid origin | `ImportDES/Mariapps.PAL.RepImportDES/BL/Process/StreamUtil/SegmentStream.cs#L154` |
| Information | {MethodName}\|Started reset validate Queue Process | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L59` |
| Information | {MethodName}\|Import Validation Process Started for {TypeMaster} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L79` |
| Information | {MethodName}\| excluding vessel list {Vessel} and packetCounter data {Data} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L113` |
| Information | {MethodName}\|Packet data gotten for with excluded vessel list {List} and skip counter list {SkipPacketCounter},is file Name {PacketName} and PacketCounter {PacketCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L117` |
| Information | {MethodName}\|File not found for packet, skipping | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L126` |
| Information | {MethodName}\|Concurrent Task Object is still running wait for it to complete and retrying again | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L143` |
| Information | {MethodName}\| No valid data found in Validate Queeu nor any task process found as runningg, stopping the process | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L148` |
| Error | {MethodName}\| Vessel {VesselId} basic configuration does not exist skipping | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L172` |
| Information | {MethodName}\|Started validating packet {PacketName} for vessel - {VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L175` |
| Debug | {MethodName}\| adding vessel {VesselId} to memory | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L186` |
| Throw:InvalidOperationException | Adding Vessel {0} to memory failed exception | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L190` |
| Information | {MethodName}\|Old packet counter received. Deleting queue item and moving packet for vessel {VesselObjectId} and packet {PacketName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L257` |
| Debug | {MethodName}\|Old packet queue delete status: {QueueDeleteStatus} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L263` |
| Error | {MethodName}\|Old packet queue delete status: {QueueDeleteStatus} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L265` |
| Debug | {MethodName}\|Old packet move status: {FileMoveStatus} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L269` |
| Error | {MethodName}\|Old packet move status: {FileMoveStatus} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L271` |
| Warning | {MethodName}\|Incorrect packet counter {PacketCounter} received for vessel {VesselObjectId} and packet {PacketName}\|Last cache packet number {LasInCacheNUmber} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L295` |
| Error | {MethodName}\| Error in pushing error packet counter to cache list for vessel {VesselObjectId} and PacketName {PacketName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L313` |
| Warning | {MethodName}\|Incorrect packet counter {PacketCounter} for vessel {VesselObjectId}, cache list push status: {ErrorPckCtrStatus} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L326` |
| Warning | {MethodName}\| Skipping the vessel ObjectID {VesselId} from processing untill next cycle | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L328` |
| Error | {MethodName}\|Error while setting invalid config vessel {VesselId} to skip list | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L333` |
| Throw:InvalidOperationException | Unique Code read from packet name does not matching with current Env Uniq Code {validatePacketParam.UniqueCode} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L357` |
| Throw:InvalidOperationException | Destination read from packet name  does not match current Environment Vessel Id {validatePacketParam.CurrentVesselId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L360` |
| Throw:InvalidOperationException | Type read from packet name does not match with Util ReplicationType {validatePacketParam.ReplicaTypeId.ToString()} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L363` |
| Throw:InvalidOperationException | Packet counter read from packet name deos not match with valid packetCounter {validatePacketParam.DesQPacketData.PacketCounter} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L366` |
| Throw:InvalidOperationException | Extension gotten from packet name does not match with valid extension .tzst | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L369` |
| Warning | {MethodName}\|Incomplete packet split for vessel {VesselObjectId}, packet {PacketCounter}, file {PacketName}. Expected splits {ExpectedSplitCount}, found {FoundSplitCount}, last cache packet {LastInCacheNUmber}, cache pu | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L406` |
| Debug | {MethodName}\|Removing the vesssel {VesselId} from memory | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L409` |
| Information | {MethodName}\| Packet Counter gotten is latest for {PacketName} for Vesssel {VesselId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L414` |
| Error | {MethodName}\|File move failed skipping this vessel{VesselId} and PacektName {PacketName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L424` |
| Error | Error in {MethodName} while processing PacketName: {PacketName} for Vessel:{VesselObjectId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L432` |
| Error | {MethodName}\|Moving the packet {PacketName} from inbox folder status :{ErrorMoveStatus} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L435` |
| Debug | {MethodName}\|file {PacketName} moved successfully to work folder {WorkFolder} and now saving to Process Q | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L475` |
| Debug | {MethodName}\| adding data to Process Q Item {SaveStatus} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L492` |
| Debug | {MethodName}\| Error packet counter cleared for vessel {VesselId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L497` |
| Error | {MethodName}\| Error packet counter clear failed for vessel {VesselId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L499` |
| Debug | {MethodName}\|Deleted packet {PacketName} successfully from Validate Q | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L515` |
| Error | {MethodName}\|Error while deleting {PacketName} from Validate Q | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L517` |
| Information | {MethodName}\|File validated successfully for vessel{VesselId} and PacektName {PacketName} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L530` |
| Debug | {MethodName}\| Packet counter updated in cache list only | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L540` |
| Error | {MethodNae}\| Packet counter updation failed for vessel {VesselId} and PacketCounter {PacketCounter} for key {Counterkey} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L542` |
| Information | {MethodName}\|Removing the vesssel {VesselId} from memory | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L547` |
| Error | {MethodName}\|Error while saving {PacketName} to process Q | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L552` |
| Error | {MethodName}\|Move back process {PacketName} successfully to folder {InboxFolder} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L562` |
| Error | {MethodName}\|Error while move back {PacketName} to folder {InboxFolder} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L564` |
| Information | {MethodName}\|No valid Id or VesselObjectId found for packet\| InputData {Json}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L578` |
| Error | {MethodName}\|Deleted entry with missing File Name or location successfully from Validate Q\| InputData {Json}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L590` |
| Error | {MethodName}\|Error while deleting packet with missing File Name or location from Validate Q\| InputData {Json}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L592` |
| Error | {MethodName}\|Deleted entry with packetCounter 0 successfully from Validate Q\| InputData {Json}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L623` |
| Error | {MethodName}\|Error while deleting entry with packet Counter that is 0 from Validate Q\| InputData {Json}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L625` |
| Error | {MethodName}\|No valid File found for packet in location\| InputData {Json}  | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ImportValidateBL.cs#L633` |
| Debug | {0}\|for API Address:{1}{2} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ValidateConfig.cs#L26` |
| Throw:ArgumentNullException | Base address is null or empty | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ValidateConfig.cs#L28` |
| Throw:ArgumentNullException | End point address is null or empty | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ValidateConfig.cs#L30` |
| Debug | {0}\|for All serviceConfig data for key {1} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ValidateConfig.cs#L36` |
| Throw:ArgumentNullException | All serviceConfig data is null or empty | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ValidateConfig.cs#L39` |
| Error | {MethodName}\| ConfigPathEntity not found for vesse ObjectId {VesselId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ValidateConfig.cs#L48` |
| Error | {MethodName}\| ConfigPath gotten is null or empty for import Vessel {VesselId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ValidateConfig.cs#L54` |
| Error | {MethodName}\| ConfigPath gotten is null or empty for import config Vessel {VesselId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ValidateConfig.cs#L60` |
| Error | {MethodName}\| VesselPacketCounterEntity not found for vesse ObjectId {VesselId} | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ValidateConfig.cs#L73` |
| Error | {MethodName}\| ReplicaSettings is null or empty | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ValidateConfig.cs#L85` |
| Throw:ArgumentNullException | ReplicaSettings is null or empty | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ValidateConfig.cs#L86` |
| Error | {MethodName}\| PrimaryDB or ReadOnlyDB is null or empty | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ValidateConfig.cs#L91` |
| Throw:ArgumentNullException | ReplicaName or ReplicaTypeId gotten has null or 0 value | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ValidateConfig.cs#L92` |
| Error | {MethodName}\| IsEnabled is false for all replica settings | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ValidateConfig.cs#L97` |
| Throw:InvalidOperationException | IsEnabled is false for all replica settings | `ImportDES/Mariapps.PAL.RepImportDES/BL/Validate/ValidateConfig.cs#L98` |
| Throw:ArgumentNullException | <nameof(serviceConfig))> | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/CommonIntServiceClient.cs#L34` |
| Debug | {MethodName}\| Calling method with no input | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/CommonIntServiceClient.cs#L54` |
| Throw:InvalidOperationException | API endpoint not configured for {ServiceCallTypeName.CommonIntegrationApiKey}. | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/CommonIntServiceClient.cs#L58` |
| Debug | {MethodName}\|RESPONSE\|{Output} | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/CommonIntServiceClient.cs#L65` |
| Error | {MethodName}\|Exception | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/CommonIntServiceClient.cs#L75` |
| Debug | {MethodName}\|Executing Post Request:{ServiceBaseAddress}{ServiceApiAddress}, with input {InputBo}  | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/CommonIntServiceClient.cs#L83` |
| Debug | {MethodName}\|API RESULE: {Result} | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/CommonIntServiceClient.cs#L91` |
| Debug | {MethodName}\| Calling method with input {JsonData} | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/DscServiceClient.cs#L47` |
| Throw:InvalidOperationException | API endpoint not configured for {ServiceCallTypeName.DscSchemaComparerKey}. | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/DscServiceClient.cs#L51` |
| Debug | {MethodName}\|Executing Post Request:{0}{1}, with input {2}  | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/ExternalRequestServiceClient.cs#L49` |
| Debug | Executing Method:{0}\|for  Get API:{1} | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/ExternalRequestServiceClient.cs#L81` |
| Debug | {0} Result is {1} | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/ExternalRequestServiceClient.cs#L93` |
| Throw:InvalidOperationException | API endpoint not configured for {ServiceCallTypeName.NextServiceCallApiKey}. | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/NextServiceCallerServiceClient.cs#L60` |
| Throw:InvalidOperationException | API endpoint not configured for {ServiceCallTypeName.RepRbpApiKey}. | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/RbpServiceClient.cs#L65` |
| Warning | {MethodName}\|Output is null or empty when calling {Api} | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/RbpServiceClient.cs#L75` |
| Warning | {MethodName}\|RBP service call returned an HTTP error | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/RbpServiceClient.cs#L83` |
| Error | {MethodName}\|Error Occured | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/RbpServiceClient.cs#L92` |
| Debug | {MethodName}\|Executing Post Request:{ServiceBaseAddress}{ApiAdresss}, with input {InputJson}  | `ImportDES/Mariapps.PAL.RepImportDES/ServiceClient/RbpServiceClient.cs#L100` |
| Throw:ArgumentNullException | <nameof(workerServiceSettingsEntity))> | `ImportDES/Mariapps.PAL.RepImportDES/WorkerService.cs#L25` |
| Information | WorkerService StartAsync | `ImportDES/Mariapps.PAL.RepImportDES/WorkerService.cs#L33` |
| Information | WorkerService StopAsync | `ImportDES/Mariapps.PAL.RepImportDES/WorkerService.cs#L39` |
| Information | {MethodName}\|WorkerService:ExecuteAsync\|Start | `ImportDES/Mariapps.PAL.RepImportDES/WorkerService.cs#L46` |
| Information | {MethodName}\|Process cycle Start | `ImportDES/Mariapps.PAL.RepImportDES/WorkerService.cs#L57` |
| Information | {MethodName}\|Started export process for all replica type | `ImportDES/Mariapps.PAL.RepImportDES/WorkerService.cs#L60` |
| Information | {MethodName}\|Ended export process for all replica type with end status {StatusCode} and message {Message} | `ImportDES/Mariapps.PAL.RepImportDES/WorkerService.cs#L62` |
| Information | {MethodName}\|Process cycle Ends | `ImportDES/Mariapps.PAL.RepImportDES/WorkerService.cs#L64` |
| Information | {MethodName}\|Cancellation requested, stopping | `ImportDES/Mariapps.PAL.RepImportDES/WorkerService.cs#L70` |
| Error | {MethodName}\|Unhandled error in process cycle | `ImportDES/Mariapps.PAL.RepImportDES/WorkerService.cs#L75` |
| Information | WorkerService Dispose | `ImportDES/Mariapps.PAL.RepImportDES/WorkerService.cs#L92` |

## ImportDSC

Logger templates in ImportDSC. Keywords: ImportDSC log, error.

| Level | Message template | Source |
|---|---|---|
| Information | {_className} {_methodName} DB execution started | `ImportDSC/Mariapps.PAL.RepImportDSC.DAL/Repository/AzureDbRepository.cs#L38` |
| Information | {_className} {_methodName} DB execution completed | `ImportDSC/Mariapps.PAL.RepImportDSC.DAL/Repository/AzureDbRepository.cs#L76` |
| Error | {_className} {_methodName} DB execution failed, ErrorMessage:{ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC.DAL/Repository/AzureDbRepository.cs#L88` |
| Error | {_className} {_methodName} DB execution failed, TableName: {tableName}, ErrorMessage: {ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC.DAL/Repository/AzureDbRepository.cs#L161` |
| Error | {_className} {_methodName} DB execution failed, Query: {query}, ErrorMessage:{ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC.DAL/Repository/AzureDbRepository.cs#L194` |
| Error | {_className} ProbeConnection failed, Server: {result.Server}, Database: {result.Database}, ErrorMessage: {ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC.DAL/Repository/ConfigProbeRepository.cs#L70` |
| Information | {_className} {_methodName} DB execution started, TableId: {tableId}, TableName: {tableName} | `ImportDSC/Mariapps.PAL.RepImportDSC.DAL/Repository/PrimaryRepository.cs#L35` |
| Information | {_className} {_methodName} DB execution completed, TableId: {tableId}, TableName: {tableName}, affected rows: {value} | `ImportDSC/Mariapps.PAL.RepImportDSC.DAL/Repository/PrimaryRepository.cs#L66` |
| Error | {_className} {_methodName} DB execution failed : {ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC.DAL/Repository/PrimaryRepository.cs#L80` |
| Information | {_className} {_methodName} DB execution completed, TableId: {tableId}, TableName: {tableName}, Result: {value} | `ImportDSC/Mariapps.PAL.RepImportDSC.DAL/Repository/PrimaryRepository.cs#L112` |
| Error | {_className} {_methodName} DB execution failed, TableId: {tableId}, TableName: {tableName}, ErrorMessage: {ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC.DAL/Repository/PrimaryRepository.cs#L126` |
| Error | {_className} {_methodName} DB execution failed, TableId:{tableId}, ErrorMessage:{ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC.DAL/Repository/ReadOnlyRepository.cs#L61` |
| Error | {_className} {_methodName} DB execution failed, TableName: {tableName}, ErrorMessage:{ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC.DAL/Repository/ReadOnlyRepository.cs#L99` |
| Error | {_className} {_methodName} DB execution failed, ErrorMessage: {ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC.DAL/Repository/Rep2iRepository.cs#L93` |
| Information | {_className} CreateTablesInAzure DB execution started, TableName: {tableSchema?.TableName} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/AzureTableCreatorBL.cs#L44` |
| Throw:ArgumentException | Table name is empty | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/AzureTableCreatorBL.cs#L49` |
| Throw:ArgumentException | No columns received for table {tableSchema.TableName} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/AzureTableCreatorBL.cs#L52` |
| Information | {_className} CreateTablesInAzure DB execution completed, TableName: {tableSchema.TableName} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/AzureTableCreatorBL.cs#L85` |
| Error | {_className} CreateTablesInAzure DB execution failed, TableName: {tableSchema.TableName}, ErrorMessage:{response.ErrorMessage} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/AzureTableCreatorBL.cs#L87` |
| Error | {_className} CreateTablesInAzure DB execution failed, TableName: {tableSchema?.TableName}, ErrorMessage:{ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/AzureTableCreatorBL.cs#L95` |
| Throw:ArgumentException | No data columns received for table {tableSchema.TableName} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/AzureTableCreatorBL.cs#L145` |
| Throw:ArgumentException | Data type not available for column {column.ColumnName} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/AzureTableCreatorBL.cs#L168` |
| Throw:ArgumentException | Invalid table name {fullTableName} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/AzureTableCreatorBL.cs#L237` |
| Information | {_className} {_methodName} started | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/ConfigEvaluationBL.cs#L83` |
| Information | {_className} {_methodName} completed, Overall: {result.Overall}, Fail: {result.FailCount}, Warn: {result.WarnCount} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/ConfigEvaluationBL.cs#L117` |
| Error | {_className} {area} {check} failed, ErrorMessage: {ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/ConfigEvaluationBL.cs#L673` |
| Error | {_className} {_methodName} {ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/DBConnectionAggregator.cs#L58` |
| Information | {_className} {_methodName} Store tablesList to cache success | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/DBConnectionAggregator.cs#L70` |
| Error | {_className} {_methodName} Store tablesList to cache failed, ErrorMeaasge: {setGetCDTQueryCacheResponse} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/DBConnectionAggregator.cs#L72` |
| Error | {_className} {_methodName} failed dataset tablesList null value returned | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/DBConnectionAggregator.cs#L76` |
| Error | {_className} {_methodName} Store tablesList to cache failed, ErrorMessage: {setJsonPathCacheResponse} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/DBConnectionAggregator.cs#L218` |
| Error | error in IntCacheBL.SetData | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/DataConduitMethods/RepImportDSCCacheBL.cs#L69` |
| Error | {_className} {_methodName} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/DataConduitMethods/RepImportDSCCacheBL.cs#L182` |
| Error | <ex, methodName)> | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/DataConduitMethods/RepImportDSCCacheBL.cs#L219` |
| Debug | {0}\|Update result: {1} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/DataConduitMethods/RepImportDSCCacheBL.cs#L233` |
| Debug | {0}\|Index of data: {1} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/DataConduitMethods/RepImportDSCCacheBL.cs#L260` |
| Information | {_className} {_methodName} Store connectionStringSettingsBOs to cache success | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L100` |
| Error | {_className} {_methodName} Store connectionStringSettingsBOs to cache failed, ErrorMessage: {setgetConnectionStringsListCacheResponse} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L102` |
| Error | {_className} {_methodName} failed dataset connectionStringSettingsBOs null value returned | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L108` |
| Error | Connectionstring settings not found | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L137` |
| Error | Connectionstring settings not found for ReplicaTypeId: {inputEntity.TypeId} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L147` |
| Information | {_className} {_methodName} completed | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L206` |
| Error | {_className} {_methodName} TableName: {inputEntity.TableName}, TableId: {inputEntity.TableId}, VesselObjectId: {inputEntity.VesselObjectId}, TypeId: {inputEntity.TypeId}, jsonDirectoryItem null | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L213` |
| Error | {_className} {_methodName} TableName: {inputEntity.TableName}, TableId: {inputEntity.TableId}, VesselObjectId: {inputEntity.VesselObjectId}, TypeId: {inputEntity.TypeId}, SrcJsonFolder empty | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L220` |
| Error | {_className} {_methodName} TableName: {inputEntity.TableName}, TableId: {inputEntity.TableId}, VesselObjectId: {inputEntity.VesselObjectId}, TypeId: {inputEntity.TypeId}, ErrorMessage: {ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L232` |
| Error | {_className} {_methodName} TableId: {inputEntity.TableId}, VesselObjectId: {inputEntity.VesselObjectId}, tableList empty | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L252` |
| Error | {_className} {_methodName} TableId: {inputEntity.TableId}, VesselObjectId: {inputEntity.VesselObjectId}, sourceTableId not found | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L264` |
| Error | {_className} {_methodName} TableId: {inputEntity.TableId}, VesselObjectId: {inputEntity.VesselObjectId}, sourceTableId.TableName empty | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L273` |
| Information | {_className} {_methodName} TableId: {inputEntity.TableId}, VesselObjectId: {inputEntity.VesselObjectId}, file not found saving input to stored json folder | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L284` |
| Error | {_className} {_methodName} TableName: {inputEntity.TableName}, TableId: {inputEntity.TableId}, VesselObjectId: {inputEntity.VesselObjectId}, ErrorMessage: {ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L333` |
| Information | {_className} RemoveOldFile: Deleting empty file {storedTableJsonPath} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L355` |
| Information | {_className} RemoveOldFile: Deleting file with empty content {storedTableJsonPath} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L366` |
| Information | {_className} RemoveOldFile: Deleting file with invalid JSON {storedTableJsonPath} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L375` |
| Error | {_className} RemoveOldFile: Error reading file content: {readEx.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L382` |
| Error | {_className} RemoveOldFile failed, ErrorMessage: {ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L402` |
| Error | {_className} {_methodName} VesselObjectId: {inputEntity.VesselObjectId}, Destination path not configured {destinationTableJsonPath} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L428` |
| Information | {_className} {_methodName} VesselObjectId: {inputEntity.VesselObjectId}, File not found {destinationTableJsonPath} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L438` |
| Error | {_className} {_methodName} VesselObjectId: {inputEntity.VesselObjectId}, GeneratePalTableSchema result empty | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L445` |
| Error | {_className} {_methodName} azureTableCreationResponse failed, TableId: {inputEntity.TableId}, TableName: {inputEntity.TableName}, VesselObjectId: {inputEntity.VesselObjectId} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L497` |
| Error | {_className} {_methodName} Table doesnot exist on PAL, TableId: {inputEntity.TableId}, TableName: {inputEntity.TableName}, VesselObjectId: {inputEntity.VesselObjectId} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L520` |
| Error | {_className} {_methodName} Create table in azure failed, TableId: {inputEntity.TableId}, TableName: {inputEntity.TableName}, VesselObjectId: {inputEntity.VesselObjectId}, ErrorMessage: {createTableResponse?.ErrorMessage} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L525` |
| Information | {_className} {_methodName} Created table in azure, TableId: {inputEntity.TableId}, TableName: {inputEntity.TableName}, VesselObjectId: {inputEntity.VesselObjectId} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L532` |
| Error | {_className} {_methodName} TableId: {inputEntity.TableId}, TableName: {inputEntity.TableName}, VesselObjectId: {inputEntity.VesselObjectId}, ErrorMessage: {ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L557` |
| Error | {_className} {_methodName} VesselObjectId: {inputEntity.VesselObjectId}, AzureTableAlteration failed, ErrorMessage: {azureTableAlterResponse.ErrorMessage} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L574` |
| Error | {_className} {_methodName} VesselObjectId: {inputEntity.VesselObjectId}, AzureTableCreation StatusCode: {azureTableAlterResponse.StatusCode}, ErrorMessage: {azureTableAlterResponse.ErrorMessage} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L576` |
| Error | {_className} {_methodName} CreateStandardClassFromCommonColumns failed, TableId:  {inputEntity.TableId} , TableName:  {inputEntity.TableName} , VesselObjectId:  {inputEntity.VesselObjectId} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L682` |
| Error | {_className} {_methodName} AzureTableAlteration failed, TableId: {inputEntity.TableId}, TableName:{inputEntity.TableName}, VesselObjectId: {inputEntity.VesselObjectId}, ErrorMessage: {azureTableAlterResponse.ErrorMessage | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L691` |
| Error | {_className} {_methodName} CreateStandardClassFromCommonColumns failed, TableId: {inputEntity.TableId}, TableName: {inputEntity.TableName}, VesselObjectId: {inputEntity.VesselObjectId},  | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L711` |
| Error | {_className} {_methodName} destinationTableSchema Replica table properties fetching failed, TableId: {inputEntity.TableId}, TableName: {inputEntity.TableName}, VesselObjectId: {inputEntity.VesselObjectId} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L721` |
| Error | GeneratePalTableSchema result empty | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L750` |
| Error | {_className} {_methodName} Error while generating schema, TableName: {tableName} TableId: {tableId} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L806` |
| Error | Error while generating schema, TableName: {item.TableName} TableId: {item.Id} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L851` |
| Error | {_className} {_methodName}Error while generating schema, TableName: {currentExecutingTableName}, TableId: {currentExecutingTabId}, ErrorMessage: {ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/RepImportDSCBL.cs#L867` |
| Debug | {0}\|for API Address:{1}{2} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/ValidateConfigBL.cs#L14` |
| Throw:ArgumentNullException | Base address is null or empty | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/ValidateConfigBL.cs#L16` |
| Throw:ArgumentNullException | End point address is null or empty | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/ValidateConfigBL.cs#L18` |
| Debug | {0}\|for All serviceConfig data for key {1} | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/ValidateConfigBL.cs#L24` |
| Throw:ArgumentNullException | All serviceConfig data is null or empty | `ImportDSC/Mariapps.PAL.RepImportDSC/BL/ValidateConfigBL.cs#L27` |
| Information | RepImportSchemaCompare Start | `ImportDSC/Mariapps.PAL.RepImportDSC/Controllers/RepImportDSCController.cs#L60` |
| Information | RepImportSchemaCompare completed | `ImportDSC/Mariapps.PAL.RepImportDSC/Controllers/RepImportDSCController.cs#L67` |
| Error | Service ComINT_Utility not found on services.json | `ImportDSC/Mariapps.PAL.RepImportDSC/ServiceClient/ComINTServiceClient.cs#L41` |
| Information | {_className} {_methodName} Api Url: {_dbServiceData.ServiceUrl}{apiAddress} | `ImportDSC/Mariapps.PAL.RepImportDSC/ServiceClient/ComINTServiceClient.cs#L52` |
| Information | {_className} {_methodName} Response: {output} | `ImportDSC/Mariapps.PAL.RepImportDSC/ServiceClient/ComINTServiceClient.cs#L55` |
| Information | {_className} {_methodName} Executing Post Request:{serviceBaseAddress}{serviceApiAddress}, with input {_inputbo} | `ImportDSC/Mariapps.PAL.RepImportDSC/ServiceClient/ExternalRequestServiceClient.cs#L25` |
| Information | {_className} {_methodName} API Result: {contents.Result}{contents.Result} | `ImportDSC/Mariapps.PAL.RepImportDSC/ServiceClient/ExternalRequestServiceClient.cs#L37` |
| Error | {_className} {_methodName} Exception | `ImportDSC/Mariapps.PAL.RepImportDSC/ServiceClient/ExternalRequestServiceClient.cs#L48` |
| Information | {_className} {_methodName} Executing | `ImportDSC/Mariapps.PAL.RepImportDSC/ServiceClient/ExternalRequestServiceClient.cs#L56` |
| Debug | {_className} {_methodName} Result is {contents} | `ImportDSC/Mariapps.PAL.RepImportDSC/ServiceClient/ExternalRequestServiceClient.cs#L67` |
| Error | {_className} {_methodName} Exception: {ex.Message} | `ImportDSC/Mariapps.PAL.RepImportDSC/ServiceClient/ExternalRequestServiceClient.cs#L78` |
| Information | WorkerService StartAsync | `ImportDSC/Mariapps.PAL.RepImportDSC/WorkerService.cs#L25` |
| Information | WorkerService StopAsync | `ImportDSC/Mariapps.PAL.RepImportDSC/WorkerService.cs#L31` |
| Information | WorkerService:ExecuteAsync\|Start | `ImportDSC/Mariapps.PAL.RepImportDSC/WorkerService.cs#L37` |
| Information | WorkerService Dispose | `ImportDSC/Mariapps.PAL.RepImportDSC/WorkerService.cs#L48` |

## ImportRBP

Logger templates in ImportRBP. Keywords: ImportRBP log, error.

| Level | Message template | Source |
|---|---|---|
| Information | {_className} {_methodName} DB execution started | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/AzureDbRepository.cs#L34` |
| Information | {_className} {_methodName} DB execution completed | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/AzureDbRepository.cs#L78` |
| Error | {_className} {_methodName} DB execution failed, ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/AzureDbRepository.cs#L90` |
| Error | {_className} ProbeConnection failed, Server: {result.Server}, Database: {result.Database}, ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/ConfigProbeRepository.cs#L70` |
| Information | {_className} {_methodName} DB execution started, ProcessType: {processType.ToString()}, TableId: {tableId} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/PrimaryRepository.cs#L33` |
| Information | {_className} {_methodName} DB execution completed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ProcessType: {processType.ToString()}, TableId: {tableId}, rows affected: {val} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/PrimaryRepository.cs#L52` |
| Error | {_className} {_methodName} DB execution failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ProcessType: {processType.ToString()}, TableId: {tableId}, ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/PrimaryRepository.cs#L67` |
| Information | {_className} {_methodName} DB execution started, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, JobQueueId: {jobQueueEntity.JobQueueId}, Percentage: {jobQueueEntity.PercentageValue}, Type: {jobQueueEntity.Type} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/PrimaryRepository.cs#L78` |
| Information | {_className} {_methodName} DB execution completed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, JobQueueId: {jobQueueEntity.JobQueueId}, Percentage: {jobQueueEntity.PercentageValue}, Type: {jobQueueEntity.Type}, ro | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/PrimaryRepository.cs#L100` |
| Error | {_className} {_methodName} DB execution failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, JobQueueId: {jobQueueEntity.JobQueueId}, Percentage: {jobQueueEntity.PercentageValue}, Type: {jobQueueEntity.Type}, Error | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/PrimaryRepository.cs#L113` |
| Information | {_className} {_methodName} DB execution completed. Retrieved {endPointDetailsList.Count} endpoint details. | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/PrimaryRepository.cs#L159` |
| Error | GetConnectionStrings failed | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/ReadConnectionStringFromDB.cs#L46` |
| Information | {_className} {_methodName} DB execution started, TableId: {tableId} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L109` |
| Information | {_className} {_methodName} DB execution completed, TableId: {tableId} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L151` |
| Error | {_className} {_methodName} DB execution failed, TableId: {tableId}, ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L163` |
| Information | {_className} {_methodName} DB execution completed, ReplicaTypeId: {connectionStringSettingsbo.ReplicaTypeId} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L218` |
| Error | {_className} {_methodName} DB execution failed, ReplicaTypeId: {connectionStringSettingsbo.ReplicaTypeId}, ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L229` |
| Information | {_className} {_methodName} DB execution completed, ReplicaTypeId: {connectionStringSettingsbo.ReplicaTypeId}, rows affected {val} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L283` |
| Information | {_className} {_methodName} DB execution completed, ReplicaTypeId: {connectionStringSettingsbo.ReplicaTypeId}, TableId: {tableId}, rows affected: {val} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L324` |
| Error | {_className} {_methodName} DB execution failed, ReplicaTypeId: {connectionStringSettingsbo.ReplicaTypeId}, ProcessType: {processType}, TableId: {tableId}, ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L339` |
| Information | {_className} {_methodName} DB execution started, tableId:{tableId}, status: {status} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L352` |
| Error | {_className} {_methodName} DB execution failed, tableId:{tableId}, status: {status}, ReplicaTypeId: {connectionStringSettingsbo.ReplicaTypeId}, ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L388` |
| Information | {_className} {_methodName} - Reprocess operation initiated at {startTime} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L399` |
| Information | {_className} {_methodName} - Using connection timeout: {_connectionTimeOut} seconds | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L400` |
| Information | {_className} {_methodName} - Executing stored procedure: {SqlQueryValues.REPLICA_RECORDS_REPROCESS} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L401` |
| Debug | {_className} {_methodName} - Opening database connection | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L409` |
| Debug | {_className} {_methodName} - Database connection opened successfully | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L411` |
| Information | {_className} {_methodName} - Starting stored procedure execution | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L419` |
| Information | {_className} {_methodName} - Stored procedure executed successfully | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L427` |
| Information | {_className} {_methodName} - Execution duration: {executionDuration.TotalSeconds:F2} seconds | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L428` |
| Information | {_className} {_methodName} - Rows affected: {rowsAffected} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L429` |
| Information | {_className} {_methodName} - Reprocess operation completed successfully at {DateTime.Now} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L434` |
| Information | {_className} {_methodName} - Total operation duration: {totalDuration.TotalSeconds:F2} seconds | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L435` |
| Error | {_className} {_methodName} - SQL error during reprocess operation | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L440` |
| Error | {_className} {_methodName} - SQL Error Number: {sqlEx.Number}, Severity: {sqlEx.Class}, State: {sqlEx.State} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L441` |
| Error | {_className} {_methodName} - Procedure: {sqlEx.Procedure}, Line: {sqlEx.LineNumber} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L442` |
| Error | {_className} {_methodName} - Operation failed after {totalDuration.TotalSeconds:F2} seconds | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L443` |
| Error | {_className} {_methodName} - Unexpected error during reprocess operation | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L453` |
| Error | {_className} {_methodName} - Error Type: {ex.GetType().Name} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L454` |
| Error | {_className} {_methodName} DB execution failed, ErrorMessage:{ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L585` |
| Error | {_className} {_methodName} DB execution failed, TableName: {tableName}, ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L624` |
| Information | {_className} {_methodName} DB execution completed, TableId: {tableId}, TableName: {tableName} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L709` |
| Information | {_className} {_methodName} DB execution started, TableName: {tableName}, TableId: {tableId}, TopRecords: {topRecords} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L728` |
| Information | {_className} {_methodName} DB execution completed, TableName: {tableName}, RecordsRetrieved: {tableData.Rows.Count} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L752` |
| Error | {_className} {_methodName} DB execution failed, TableName: {tableName}, TableId: {tableId}, ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L761` |
| Information | {_className} {_methodName} DB execution started, TableName: {tableName}, RecordCount: {repIds.Count} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L769` |
| Error | {_className} {_methodName} DB connection failed, TableName: {tableName}, RecordCount: {ids.Count}, ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L791` |
| Error | {_className} {_methodName} Batch delete failed, retrying row by row, TableName: {tableName}, REP_ID_UNIC: {IdRange(chunk)}, ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L814` |
| Error | {_className} {_methodName} DB connection lost during single delete, TableName: {tableName}, RemainingCount: {remaining.Count}, ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L838` |
| Error | {_className} {_methodName} Single delete failed, TableName: {tableName}, REP_ID_UNIC: {id}, ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L856` |
| Information | {_className} {_methodName} DB execution completed, TableName: {tableName}, RowsDeleted: {result.DeletedCount}, FailedCount: {result.FailedIds.Count} | `ImportRBP/Mariapps.PAL.RepImportRBP.DAL/Repository/Rep2iRepository.cs#L865` |
| Error | GetProcessStatus key not found replicaTypeId: {replicaTypeId} | `ImportRBP/Mariapps.PAL.RepImportRBP.Model/Common/ProcesStatusEntity.cs#L154` |
| Error | ClearProcessStatus key not found replicaTypeId: {replicaTypeId} | `ImportRBP/Mariapps.PAL.RepImportRBP.Model/Common/ProcesStatusEntity.cs#L190` |
| Error | GetCacheStatus key not found replicaTypeId: {replicaTypeId} | `ImportRBP/Mariapps.PAL.RepImportRBP.Model/Common/ProcesStatusEntity.cs#L261` |
| Information | {_className} {_methodName} started | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/ConfigEvaluationBL.cs#L86` |
| Information | {_className} {_methodName} completed, Overall: {result.Overall}, Fail: {result.FailCount}, Warn: {result.WarnCount} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/ConfigEvaluationBL.cs#L117` |
| Error | {_className} {area} {check} failed, ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/ConfigEvaluationBL.cs#L532` |
| Error | error in IntCacheBL.SetData | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/DataConduitMethods/RepImportRBPCacheBL.cs#L67` |
| Error | <ex, methodName)> | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/DataConduitMethods/RepImportRBPCacheBL.cs#L180` |
| Debug | {0}\|Update result: {1} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/DataConduitMethods/RepImportRBPCacheBL.cs#L231` |
| Debug | {0}\|Index of data: {1} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/DataConduitMethods/RepImportRBPCacheBL.cs#L258` |
| Information | {_className} {_methodName} Store connectionStringSettingsBOs to cache success | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L60` |
| Error | {_className} {_methodName} Store connectionStringSettingsBOs to cache failed, ErrorMessage: {setgetConnectionStringsListCacheResponse} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L62` |
| Error | {_className} {_methodName} failed dataset connectionStringSettingsBOs null value returned | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L68` |
| Error | Processing failed, not able to fetch database connectionString configurations for ReplicaTypeId: {input.ReplicaTypeId} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L84` |
| Information | Reprocess check - Enabled: {_workerServiceSettingsBO.ReprocessEnabled}, Interval: {interval} hours, LastRunTime: {ProcesStatusEntity.ReprocessLastRunTime}, NextRunTime: {nextRunTime}, CurrentTime: {currentTime} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L110` |
| Information | Starting reprocess operation - LastRunTime: {ProcesStatusEntity.ReprocessLastRunTime}, Interval: {interval} hours | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L114` |
| Information | Reprocess operation completed successfully at {DateTime.Now} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L120` |
| Error | Error during reprocess operation: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L128` |
| Information | Reprocess not due yet. Time until next reprocess: {timeToNextReprocess.TotalMinutes:F2} minutes | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L135` |
| Debug | Reprocess is disabled in worker service settings | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L140` |
| Error | RBP not enabled for ReplicaTypeId: {connectionStringbo.ReplicaTypeId} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L149` |
| Error | Invalid connectionString settings, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, PrimaryDB: {connectionStringbo.PrimaryDB}, ReadOnlyDB: {connectionStringbo.ReadOnlyDB} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L184` |
| Information | Processing started, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, Process started: {ProcesStatusEntity.GetProcessStatus(connectionStringbo.ReplicaTypeId)} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L200` |
| Error | CACHE_CHEKING ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ClearCacheEnabled: {_workerServiceSettingsBO.ClearCacheEnabled}, ClearCacheIntervalInMin: {_workerServiceSettingsBO.ClearCacheIntervalInMin}, GetCacheStatu | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L204` |
| Error | CACHE_CHEKING entered cache clearing | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L208` |
| Error | Processing failed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {taskEx.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L220` |
| Information | Processing completed, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, Released: {released}, Process running: {ProcesStatusEntity.GetProcessStatus(connectionStringbo.ReplicaTypeId)} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L234` |
| Information | Process already running, ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, Process started: {ProcesStatusEntity.GetProcessStatus(connectionStringbo.ReplicaTypeId)} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L240` |
| Error | ReplicaTypeId: {connectionStringbo.ReplicaTypeId}, ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L252` |
| Error | Processing failed, not able to fetch database connectionString configurations | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L273` |
| Error | {_className} {_methodName} ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L478` |
| Error | {_className} {_methodName} Table name not found for TableId: {endPointDetails.TABLE_ID} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L491` |
| Information | {_className} {_methodName} Processing endpoint: {endPointDetails.EndPointName}, TableId: {endPointDetails.TABLE_ID} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L495` |
| Information | {_className} {_methodName} Processing insert/update data for table: {tableName} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L517` |
| Information | {_className} {_methodName} Processing batch {batchNumber} for table: {tableName} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L526` |
| Information | {_className} {_methodName} No more data found in table: {tableName}. Processing completed. | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L532` |
| Information | {_className} {_methodName} Retrieved and converted {tableName} data to JSON for batch {batchNumber} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L544` |
| Error | {_className} {_methodName} {errorMessage} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L558` |
| Information | {_className} {_methodName} Successfully processed and cleaned up batch {batchNumber} for table: {tableName} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L562` |
| Information | {_className} {_methodName} Completed processing all batches for table: {tableName}. Total batches processed: {batchNumber - 1} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L575` |
| Error | {_className} {_methodName} Error processing insert/update data for table {tableName}: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L584` |
| Information | {_className} {_methodName} Retrieving top 10,000 records from table: {tableName} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L596` |
| Error | {_className} {_methodName} Error retrieving data from table {tableName}: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L609` |
| Information | {_className} {_methodName} Preparing API call for {operationType} data for table: {tableName} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L619` |
| Information | {_className} {_methodName} API payload prepared for table: {tableName} with {apiPayload.records.Count} records | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L642` |
| Information | {_className} {_methodName} Calling API: {fullApiUrl} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L647` |
| Information | {_className} {_methodName} API call successful for table: {tableName}, operation: {operationType} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L654` |
| Error | {_className} {_methodName} API call failed for table: {tableName}, operation: {operationType} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L658` |
| Error | {_className} {_methodName} Error calling API for table {tableName}: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L671` |
| Information | ✅ Simulated API call SUCCESS to: {apiUrl}, Response: {result} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L686` |
| Error | ❌ Simulated API call FAILED to: {apiUrl}, Status: {response.StatusCode}, Response: {result} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L691` |
| Information | {_className} {_methodName} Deleting {repIds.Count} processed rows for table: {tableName}, operation: {operationType} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L704` |
| Error | {_className} {_methodName} Error deleting processed rows for table {tableName}: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L714` |
| Error | {_className} {_methodName} {deleteResult.FailedIds.Count} of {repIds.Count} processed rows could not be deleted for table: {tableName} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L734` |
| Information | {_className} {_methodName} Successfully deleted {deleteResult.DeletedCount} processed rows for table: {tableName} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L738` |
| Error | {_className} {_methodName} failed dataset importQueryList null value returned | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L753` |
| Error | {_className} {_methodName} Processing failed, not able to fetch database connectionString configurations for ReplicaTypeId: {ReplicaTypeId} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L882` |
| Error | {_className} {_methodName} {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L907` |
| Information | {_className} {_methodName} successfully cleared cache | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/RepImportRBPBL.cs#L924` |
| Debug | {0}\|for API Address:{1}{2} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/ValidateConfigBL.cs#L14` |
| Throw:ArgumentNullException | Base address is null or empty | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/ValidateConfigBL.cs#L16` |
| Throw:ArgumentNullException | End point address is null or empty | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/ValidateConfigBL.cs#L18` |
| Debug | {0}\|for All serviceConfig data for key {1} | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/ValidateConfigBL.cs#L24` |
| Throw:ArgumentNullException | All serviceConfig data is null or empty | `ImportRBP/Mariapps.PAL.RepImportRBP/BL/ValidateConfigBL.cs#L27` |
| Error | Service ComINT_Utility not found on services.json | `ImportRBP/Mariapps.PAL.RepImportRBP/ServiceClient/ComINTServiceClient.cs#L46` |
| Information | {_className} {_methodName} Api Url: {_dbServiceData.ServiceUrl}{apiAddress} | `ImportRBP/Mariapps.PAL.RepImportRBP/ServiceClient/ComINTServiceClient.cs#L57` |
| Information | {_className} {_methodName} Response: {output} | `ImportRBP/Mariapps.PAL.RepImportRBP/ServiceClient/ComINTServiceClient.cs#L60` |
| Information | {_className} {_methodName} completed | `ImportRBP/Mariapps.PAL.RepImportRBP/ServiceClient/ComINTServiceClient.cs#L61` |
| Error | {_className} {_methodName} | `ImportRBP/Mariapps.PAL.RepImportRBP/ServiceClient/ComINTServiceClient.cs#L72` |
| Debug | \|Executing Post Request:{0}{1}, with input {2}  | `ImportRBP/Mariapps.PAL.RepImportRBP/ServiceClient/ExternalRequestServiceClient.cs#L24` |
| Debug | \|API RESULE:{contents} | `ImportRBP/Mariapps.PAL.RepImportRBP/ServiceClient/ExternalRequestServiceClient.cs#L38` |
| Error | \|HttpClient null returned | `ImportRBP/Mariapps.PAL.RepImportRBP/ServiceClient/ExternalRequestServiceClient.cs#L44` |
| Error | \|Exception | `ImportRBP/Mariapps.PAL.RepImportRBP/ServiceClient/ExternalRequestServiceClient.cs#L54` |
| Debug | Executing Method:{0}\|for  Get API:{1} | `ImportRBP/Mariapps.PAL.RepImportRBP/ServiceClient/ExternalRequestServiceClient.cs#L62` |
| Debug | {0} Result is {1} | `ImportRBP/Mariapps.PAL.RepImportRBP/ServiceClient/ExternalRequestServiceClient.cs#L73` |
| Information | WorkerService StartAsync | `ImportRBP/Mariapps.PAL.RepImportRBP/WorkerService.cs#L31` |
| Information | WorkerService StopAsync | `ImportRBP/Mariapps.PAL.RepImportRBP/WorkerService.cs#L37` |
| Error | WorkerService ExecuteAsync \| Process started | `ImportRBP/Mariapps.PAL.RepImportRBP/WorkerService.cs#L43` |
| Error | WorkerService ExecuteAsync \| Process Reinitiated | `ImportRBP/Mariapps.PAL.RepImportRBP/WorkerService.cs#L48` |
| Information | WorkerService ExecuteAsync\|Cancellation requested, stopping | `ImportRBP/Mariapps.PAL.RepImportRBP/WorkerService.cs#L60` |
| Error | WorkerService ExecuteAsync, ErrorMessage: {ex.Message} | `ImportRBP/Mariapps.PAL.RepImportRBP/WorkerService.cs#L65` |
| Information | WorkerService Dispose | `ImportRBP/Mariapps.PAL.RepImportRBP/WorkerService.cs#L91` |

