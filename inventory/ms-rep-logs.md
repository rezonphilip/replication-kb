---
doc_id: INV-MSREP-LOGS
type: inventory
components: [ms-rep]
status: draft
author: claude
last_verified: 2026-11-11
---

# MS-REP log message catalogue

Every logger message template found in MS-REP code, per service, with its source line. Used to write error signatures. Keywords: log, error message, signature, Serilog.

## RepAckn

Logger templates in RepAckn. Keywords: RepAckn log, error.

| Message template | Source |
|---|---|
| {MethodName}\| Starting Acknowledgement process for TableSettings Id {TableSetttingsId} for Packet Counter {PacketCounter} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L48` |
| {MethodName}\| Processing for {FileLocation} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L63` |
| {MethodName}\| Base URL or API URL is empty for Table Settings Id {TableSetttingsId} for Packet Counter {PacketCounter} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L104` |
| {MethodName}\| Invoking external service for {FileLocation} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L151` |
| {MethodName}\| Acknowledgement process completed successfully for {FileLocation} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L158` |
| {MethodName}\| Acknowledgement process failed for {FileLocation} with error {ErrorMessage} - {HttpStatusCode} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L183` |
| {MethodName}\| All files failed for TableSettings Id {TableSetttingsId} for Packet Counter {PacketCounter} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L216` |
| {MethodName}\| {Message} for TableSettings Id {TableSetttingsId} for Packet Counter {PacketCounter} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L237` |
| {MethodName}\| Acknowledgement process completed successfully for TableSettings Id {TableSetttingsId} for Packet Counter {PacketCounter} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L250` |
| {MethodName}\| Exception occurred while processing Acknowledgement for TableSettings Id {TableSetttingsId} for Packet Counter {PacketCounter} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L259` |
| {MethodName}\| Input is null | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L123` |
| {MethodName}\| ImportQId is 0 | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L133` |
| {MethodName}\| VesselObjectId is 0 | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L143` |
| {MethodName}\| TableSettingsId is 0 | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L153` |
| {MethodName}\| TableSettingsId is not valid | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L163` |
| {MethodName}\| PacketCounter is 0 | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L173` |
| {MethodName}\| SplitFiles is null or empty | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L183` |
| {MethodName}\| FileLocation is null or file does not exist | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L193` |
| {MethodName}\| Validation successful | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L203` |
| {MethodName}\| Invalid Request | `RepAckn/MariApps.PAL.Rep.Ackn.Service/Controllers/AcknController.cs#L84` |
| AcknController\|TestService\|Vessel | `RepAckn/MariApps.PAL.Rep.Ackn.Service/Controllers/AcknController.cs#L138` |
| {MethodName}\| ID {Id} is not available in registered table settings | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L53` |
| {MethodName}\| External invoke parameters cannot be null | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L77` |
| {MethodName}\| Table settings ID {Id} is not available | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L83` |
| {MethodName}\| POST request successful. Status: {StatusCode}, Response time: {ResponseTime}ms | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L117` |
| {MethodName}\| POST request failed. Status: {StatusCode}, Response: {Response} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L127` |
| {MethodName}\| HTTP request exception occurred | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L141` |
| {MethodName}\| Request timeout occurred | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L154` |
| {MethodName}\| Unexpected error occurred | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L168` |
| {MethodName}\| BaseUrl cannot be null or empty | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L205` |
| {MethodName}\| ExternalInvokeParam cannot be null | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L316` |
| {MethodName}\| TableSettingsId {Id} is available, using ClientFactoryDestinationHandler | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L323` |
| {MethodName}\| TableSettingsId {Id} is not available, using CommonDestinationHandler | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L328` |
| {MethodName}\|Posting data to {ApiAddress} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/ExternalSL.cs#L30` |
| {MethodName}\|Data post to Api {ApiAddress} completed with status Code {ResponseStatus} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/ExternalSL.cs#L51` |
| {MethodName}\|Response from Api {ApiAddress} completed with status Code {ResponseStatus} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/ExternalSL.cs#L70` |
| {MethodName}\|Exception | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/ExternalSL.cs#L74` |
| {MethodName}\| Error in SaveAcknowledgementStatus | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L89` |
| {MethodName}\| {ErrorMessage} | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L192` |
| {MethodName}\| Error in Error method | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L211` |
| {MethodName}\| {InfoMessage} | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L220` |
| {MethodName}\| Error in Information method | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L239` |
| {MethodName}\| Error while reading table settings | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L271` |
| {MethodName} - Error in reading Common CO Parameters values | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L332` |
| {MethodName}\| Error in SaveAcknDataBulkd | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L537` |

## RepAcquisition

Logger templates in RepAcquisition. Keywords: RepAcquisition log, error.

| Message template | Source |
|---|---|
| Data did not save Successfully | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L632` |
| {MethodName} - Error in reading Common CO Parameters values | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L57` |
| {MethodName} Exception while reading last in packet counter | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L95` |
| {MethodName}\|Exception occured while reading missing packet data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L140` |
| {MethodName}\|Exception occured while reading error missing packet data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L175` |
| {MethodName}\|Exception occured while reading vessel rep code | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L210` |
| {MethodName}\|Error occured while reading transfer data for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L242` |
| {MethodName}\|Error occured while reading transfer location for {TransferID} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L273` |
| {MethodName}\|Exception occured while reading vessels | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L322` |
| {MethodName}\| Exception while reading Table Settings Id from Downloads for {FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L357` |
| {MethodName}\| Saving Import Packet Data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L367` |
| {MethodName}\| Import Packet Data saved with InPacketHdId {InPacketHdId} and MissingPacketId {MissingPacketId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L392` |
| {MethodName}\| Exception while saving Import Packet Data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L397` |
| {MethodName}\| Import bulk Packet Data saved | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L428` |
| {MethodName}\| Updating Vessel {VesselId} In Packet Counter {PacketCounter} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L444` |
| {MethodName}\| Exception while updating Vessel In Packet Counter | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L462` |
| {MethodName}\| Reading all Table Settings | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L470` |
| {MethodName}\| Saving V2V Import Packet Data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L532` |
| {MethodName}\| Import V2V Packet Data saved with InPacketHdId {InPacketHdId} and MissingPacketId {MissingPacketId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L566` |
| {MethodName}\| Exception while reading V2V Packet Counter Settings for Channel {ChannelId}, for source {SourceId} to Destination {DestinatinId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L612` |
| {MethodName}\| Exception while updating V2V Packet Counter with new Counter {Counter} for Channel {ChannelId}, for source {SourceId} to Destination {DestinatinId | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L654` |
| Exception while saving packet data {MethodName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L757` |
| {MethodName}\| Import Queue Data saved | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L791` |
| {MethodName}\| Error while saving Import Queue Data\| Message:{Message} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L801` |
| Exception occured while saving data in {MethodName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L812` |
| {MethodName}\| Import Queue sub details Data updated successfully | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L851` |
| {MethodName}\| Error while saving updating import Queue sub details  Data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L861` |
| {MethodName}\| Error in updating Import Queue sub details  data Items | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L872` |
| {MethodName}\| Import Queue Data updated successfully | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L915` |
| {MethodName}\| Error while saving updating import Queue Data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L925` |
| {MethodName}\| Error in updating Import Queue data Items | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L936` |
| {MethodName}\| Starting Process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L60` |
| {MethodName}\| ImportVesselIds contains 0\|Import will not proceed | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L71` |
| {MethodName}\| Inbox Directory not found | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L89` |
| {MethodName}\| isVessel value could not be found | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L95` |
| {MethodName}\| Missing Packet Table Info not found\| Intitialising it to 0 | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L101` |
| {MethodName}\| No active vessel found, exiting | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L108` |
| {MethodName}\| Started processing for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L122` |
| {MethodName}\| Inbox Location {InboxDirectory} or Replication Code {RepCode} not found for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L132` |
| {MethodName} \| Step 1: generalChannelId is null. ChannelKey: {ChannelKey}, VesselId: {VesselId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L139` |
| {MethodName}\| Process Completed | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L185` |
| An exception occured in {MethodName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L189` |
| {MethodName}\| Starting worker for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L199` |
| {MethodName}\|No Pending Files available for vessel | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L220` |
| {MethodName}\| No valid files found for {Vessel} at location {SourceLocation} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L234` |
| {MethodName}\| Worker Completed for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L256` |
| A critical Exception occured while processing import data in {MethodName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L260` |
| {MethodName}\| File {FileName} is locked, skipping now | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L385` |
| {MethodName}\| Error while validating files for {Vessel}\| Error: {ErrorMessage} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L397` |
| {MethodName}\| Last Packet Counter for {Vessel} is not found | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L420` |
| {MethodName}\| Packet Name {FileName} is not of a valid naming format for {Vessel}\| Moving to errorn folder | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L454` |
| {MethodName}\| Error while moving failed packet to error folder {FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L459` |
| {MethodName}\| Packet {FileName} is waiting for previous packet to be processed for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L489` |
| {MethodName}\| File {FileName} gotten is valid for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L525` |
| {MethodName}\| Saved Import item for {Count} files | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L611` |
| {MethodName}\| An exception occured while saving Import Queue Items for {Vessel}\| Stopping the processing for this vessel | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L617` |
| {MethodName}\| Packet {FileName} is already processed and being skipped for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L625` |
| {MethodName}\| Packet {FileName} is not valid for {Vessel}\| Moving to error folder | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L679` |
| {MethodName}\| Not all split file is available for file {FileName} for {Vessel}\| Skipping this file | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L699` |
| {MethodName}\| Process Completed for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L725` |
| {MethodName}\| Error while saving Import Packet Data, result gotten is empty or null | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L746` |
| Error while saving Import Packet Data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L747` |
| {MethodName}\| Saving Last Vessle {Vessel} Received In packet counter with {LastInPacketCounter} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L749` |
| {MethodName}\| Exception while saving Import Queue Data\| Message : {ExMessage} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L817` |
| Exception occured in {MethodName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L830` |
| {MethodName}\| Starting file acquisition process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L840` |
| {MethodName}\| Import Vessel Ids contains -1, skipping all vessels for acquistion | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L854` |
| {MethodName}\| Work base directory not found | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L868` |
| {MethodName}\| not Vessel Object Id data found | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L902` |
| {MethodName}\| Transfer type value could not be gotten for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L926` |
| {MethodName}\| Inbox folder location could not be gotten for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L937` |
| {MethodName}\| No files found to import for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L987` |
| {MethodName}\| Error while moving error/pending file from all zip to inbox\|File name: {FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1116` |
| {MethodName}\| Zip file does not exist in Allzip location or all splits might not be available for file {FileName} for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1123` |
| Exception occured in {MethodName}\| while reading/processing error/missing packets | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1128` |
| {MethodName}\| Missing packets have not been replicated for vessel {Vessel} so skipping its import as it is sequence import | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1180` |
| {MethodName}\| {Count} priority packets processed for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1191` |
| {MethodName}\| No valid packets found to import | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1196` |
| {MethodName}\| Removing {Count} files from Acquisition Queue for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1199` |
| {MethodName}\|{Message} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1208` |
| {MethodName}\| {Message} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1219` |
| {MethodName}\| Import process completed for all vessels | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1226` |
| {MethodName}\| General occured while processing import file | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1239` |
| {MethodName}\| Processing priority packets for vessel {Vessel} with count {AcqCount} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1251` |
| {MethodName}\| Read and Processing file -{FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1270` |
| {MethodName}\|Error while moving split packets to allzip\|FileName: {FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1435` |
| {MethodName}\| Packet {PacketCounter} -  {FileName} skipped for vessel {Vessel} as it's already processed | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1475` |
| {MethodName}\| Validation failed for file {File} Vessel {VesselObjectId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1481` |
| {MethodName}\| Error while moving file {FileName} to error folder {Folder} for vessel {VesselObjectId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1487` |
| {MethodName}\| Validation Successfull - {File}\| all split faile available and validated | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1493` |
| {MethodName}\| Not all split files are available for file {FileName} for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1557` |
| {MethodName}\| Finished processing file {FileName} for vessel {VesselObjectId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1560` |
| {MethodName}\| Processing import packet data for vessel {VesselObjectId} with count {ImportPacketCount} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1573` |
| {MethodName}\| No record found in outputPacketList for packet with counter {PacketCounter} for vessel {VesselObjectId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1627` |
| {MethodName}\| Updating Vessel Packet Counter for Vessel {VesselObjectId} with value {MaxPacketCounter} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1636` |
| {MethodName}\| After saving import data in packet hd id and missing packet is not saved due to Update: {UpdatePacketCounter} packet counter gotten is {MaxPacketC | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1644` |
| {MethodName}\| While importing after saving packet InpakcetHdId, missingPacketId {ImportData},  is null or empty | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1650` |
| {MethodName}\| No import packet data found to save for vessel {VesselObjectId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1657` |
| Exception in {MethodName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1668` |
| {MethodName}\|Validating Packet Name | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1677` |
| {MethodName}\|{File} has {Message} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1705` |
| {MethodName}\| Validating Packet Counter for {FileName} with LastInPacketCounter {LastInPacketCounter} and VesselData {VesselData} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1715` |
| {MethodName}\| Packet is missing another packet before it needs to be processed | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1730` |
| {MethodName}\| Packet Counter is correct | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1740` |
| {MethodName}\| packet counter {PacketCounter}, gotten is old | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1745` |
| {MethodName}\| No missing packet info could be found against the packet\| Proceeding | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1751` |
| {MethodName}\| {FileName} is having status {Status} so reprocessing | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1759` |
| {MethodName}\| {FileName} is already processed | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1764` |
| {MethodName}\| {FileName} status gotten is invalid or not available so reprocessing | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1769` |
| {MethodName}\| Packet counter validation for file {FileName} completed with output {PacketType} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1775` |
| {MethodName}\|Exception occured while validating File {FileName} with LastInPacketCounter {LastInPacketCounter} and VesselData {VesselData} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1781` |
| {MethodName}\| Validating File {FileName} with params RepCode {RepCode}, Is Split {IsSplit}, Is Vessel {IsVessel}, LastInPktCTR {LastInPktCTR}, VesselData {Vesse | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1791` |
| {MethodName} \|Process  START | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1932` |
| {MethodName}\| Started Missing packet process for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1984` |
| {MethodName}\| Processing missing packet {PacketCounter} for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2020` |
| {MethodName}\| Packet file {FileName} with Counter {PacketCounter} not found in AllZipDirectory or TempDirectory for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2066` |
| {MethodName}\| Moved packet file {FileName} to {InboxDirectory} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2078` |
| {MethodName}\| Failed to move packet file {FileName} to {InboxDirectory} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2082` |
| {MethodName}\| Exception while moving packet file {FileName} to inbox | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2087` |
| {MethodName} \|Exception processing Error and Missing Files | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2094` |
| {MethodName}\| Configuration error: BasicSettings:ImportVesselIds is null or empty. Example: [-1] or [1001,1002]. | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2102` |
| {MethodName}\| Starting to process Vessel to Vessel Priority Packets {Count} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L45` |
| {MethodName}\| Packet related header data is not proper for File {File} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L108` |
| {MethodName}\| Packet Destination Information does not match current environment moving for File {FileName}, moving to error directory | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L116` |
| {MethodName}\| No validlast in packet counter could be gotten for Source Vessel {Souce} and Destination Vessel {Destination}\| skipping this file | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L145` |
| {MethodName}\| Packet counter {Counter} is latest for File {PacketName} with Source Unique Id {Source} and Destination Unique Id {Destination} for channel | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L237` |
| {MethodName}\| {PacketName} Updating Vessel to Vessel Last In Packet Counter {Counter} failed for Channel {ChannelId} where souce is {Source} and destination is  | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L261` |
| {MethodName}\| Vessel to Vessel Packet {PacketName} with Packet Counter {Counter} is successfully processed for Channel {ChannelId} where souce is {Source} and d | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L367` |
| {MethodName}\| Packet counter {Counter} is already processed for File {PacketName} with Source Unique Id {Source} and Destination Unique Id {Destination} for cha | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L373` |
| {MethodName}\| Packet {FileName}\| validation failed got invalid status {Status}, moving to error fodler | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L423` |
| {MethodName}\| Finsihed processsing File {FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L440` |
| {MethodName}\| File {FileName} is not complete and is waiting for other splits, where Source {Source} And Destination {Destination} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L444` |
| {MethodName}\| Finished processing {FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L447` |
| {MethodName}\| Finished processing Vessel to Vessel Priority Packets {Count} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L450` |
| {MethodName}\| Error in processing Vessel to Vessel Priority Packets | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L454` |
| Transfer Type gotten is null for current location from GetCurrentVesselTransferType method | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L496` |
| {MethodName}\| Validating {FileName} packet counter {Counter} for source vessel {SourceVessel} and destination vessel {DestinationVessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1118` |
| {MethodName}\| Packet {FileName} {PacketCounter} gotten is not correct for Source Vessel {SourceVessek} and Destination Vessel {DestinationVessel} for Channel {C | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1146` |
| {MethodName}\|Exception occured while validating File {PacketName} with packet counter {Counter} for Source Vessel {Source} and destination Vessel {Destination} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1186` |
| {MethodName}\| Validating packet counter {Counter} for source vessel {SourceVessel} and destination vessel {DestinationVessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1197` |
| Packet related header data is not proper | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1366` |
| Base address is null or empty | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/ValidateConfigBL.cs#L16` |
| End point address is null or empty | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/ValidateConfigBL.cs#L18` |
| {MethodName}\|File:{FileName} is being used waiting for {WaitTime} milliseconds\| CHECK Count {CheckCount} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L91` |
| {MethodName}\| Search path does not exist: {SearchPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L211` |
| {MethodName}\| Multiple files with name {FileName} found in {SearchPath}. Found {FileCount} instances: {FilePaths} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L237` |
| {MethodName}\| Selected most recently modified file: {SelectedFile} (Modified: {ModifiedTime}) | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L247` |
| {MethodName}\| Access denied while searching in {SearchPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L257` |
| {MethodName}\| Directory not found while searching in {SearchPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L262` |
| {MethodName}\| Error searching for file {FileName} in {SearchPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L267` |
| {MethodName}\| Exception occurred while searching for file {FileName} in {SearchPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L285` |
| {MethodName}\| Exception occurred while searching for {BaseName} in {SearchPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L357` |
| {MethodName}\| Starting Batch Acquisition Process for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L43` |
| {MethodName}\| Invalid batch input: {ValidationMessage} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L49` |
| {MethodName}\| Replication Code not found for {Vessel}, exiting | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L86` |
| {MethodName}\| Batch Acquisition Process Completed for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L115` |
| {MethodName}\| Exception occured while processing Batch Acquisition for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L120` |
| {MethodName}\| Starting Batch Priority Process for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L202` |
| {MethodName}\| Packet Name {FileName} is not of a valid naming format for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L243` |
| An exception occured while saving Import Queue Items | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L388` |
| {MethodName}\| Exception occured while processing Batch Priority for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L491` |
| {MethodName}\| Exception while saving General Notification Import Queue Data\| Message : {ExMessage} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L609` |
| {MethodName}\| Exception while updating Import Queue Data\| Message : {ExMessage} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L619` |
| {MethodName}\| Exception while saving Import Queue Dt Data\| Message : {ExMessage} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L629` |
| {MethodName}\| Starting Acquisition Import process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L45` |
| {MethodName}\| Old Import is disabled | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L49` |
| {MethodName}\| Acquisition Old Import process completed with data {Count} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L66` |
| {MethodName}\| Setting Initial Data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L93` |
| {MethodName}\| Acquisition Import Service config is not accessible | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L100` |
| {MethodName}\| Acquisition Import Process has exceeded the time limit | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L116` |
| {MethodName}\| Acquisition Import Process is already running\| Another pass has been requested | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L125` |
| {MethodName}\|Initating Acquisition Import Process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L153` |
| {MethodName}\| Acquisition Import Process Completed | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L158` |
| {MethodName}\| Acquisition Import was triggered during the run, starting another pass | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L166` |
| {MethodName}\| Exception in background task | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L174` |
| {MethodName}\| {ParamName} is not configured, import queue is not started | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L229` |
| {MethodName}\| Starting Integration import queue | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L236` |
| {MethodName}\| Exception while starting Integration import queue | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L245` |
| {MethodName}\| Starting Acquisition error handler process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L255` |
| {MethodName}\| Acquisition Error Hanlder Process is already running | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L288` |
| {MethodName}\|Initating Acquisition Error Handler Process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L321` |
| {MethodName}\| Acquisition Error Handler Process Completed | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L326` |
| {MethodName}\| Batch acquisition request received for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionGeneralController.cs#L31` |
| {MethodName}\|Initiating Acquisition Import Process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L96` |
| {MethodName}\|Initiating Error File Handler Process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L108` |

## RepAzure

Logger templates in RepAzure. Keywords: RepAzure log, error.

| Message template | Source |
|---|---|
| WorkerService:StartAsync | `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L33` |
| WorkerService:StopAsync | `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L41` |
| Starting {MethodName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L50` |
| {MethodName}\|Process cycle Start | `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L60` |
| {MethodName}\|Process cycle Ends | `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L83` |
| ServiceConfigData is null or empty | `RepAzure/MariApps.PAL.Rep.Azure.Service/AzureServiceDependency.cs#L63` |
| Error encrypting:  | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/EncryptionBL.cs#L55` |
| inputStream | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/XXHash.cs#L507` |
| Specified argument must be a non-negative integer. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/XXHash.cs#L988` |
| Multi dimension array is not supported on this operation. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/XXHash.cs#L992` |
| The lower bound of target array must be zero. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/XXHash.cs#L996` |
| Offset was out of bounds for the array. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/XXHash.cs#L1006` |
| {MethodName}\|Started Process | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L63` |
| {MethodName}\| Azure Data Conduit Init Data completed with status {AzureInitStatus} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L72` |
| Error in {MethodName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L87` |
| {MethodName}\| Startning download process | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L104` |
| {MethodName}\| Setting Initial Data | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L107` |
| {MethodName}\| Azure init settings message = {AzureInitMessage} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L116` |
| {MethodName}\| Network Status = {NetworkMessage} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L128` |
| {MethodName}\|Download process initiated successfully. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L160` |
| Exception in {MethodName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L175` |
| {MethodName}\|Download process time exceeded. Removing status. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L199` |
| {MethodName}\|Download process is already running. Exiting. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L205` |
| {MethodName}\|Download process status updated. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L210` |
| Exception in background download process in {MethodName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L224` |
| {MethodName}\|Removing download process status in finally block. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L228` |
| {MethodName}\|Move process time exceeded. Removing status. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L255` |
| {MethodName}\|Move process is already running. Exiting. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L261` |
| {MethodName}\|Move process status updated. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L271` |
| Exception in background move process in {MethodName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L284` |
| {MethodName}\|Removing move process status in finally block. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L288` |
| {MethodName}\|Move operation process initiated successfully. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L296` |
| {MethodName}\| Startning file blob deletion process | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L326` |
| {MethodName}\|Delete process time exceeded. Removing status. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L369` |
| {MethodName}\|Delete process is already running. Exiting. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L375` |
| {MethodName}\|Delete process status updated. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L385` |
| Exception in background delete process in {MethodName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L399` |
| {MethodName}\|Removing delete process status in finally block. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L403` |
| {MethodName}\|Delete operation process initiated successfully. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L409` |
| {MethodName}\|Move to History process time exceeded. Removing status. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L497` |
| {MethodName}\|Move to History process is already running. Exiting. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L503` |
| {MethodName}\|Move to History process status updated. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L513` |
| Exception in background move-to-history process in {MethodName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L527` |
| {MethodName}\|Removing move-to-history process status in finally block. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L531` |
| {MethodName}\|Move to History operation process initiated successfully. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L537` |
| Excetion in {MethodName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L617` |
| Started AzureController.TestService | `RepAzure/MariApps.PAL.Rep.Azure.Service/Controllers/AzureController.cs#L102` |
| Start of AzureVerifyAccess | `RepAzure/MariApps.PAL.Rep.Azure.Service/Controllers/AzureController.cs#L110` |
| EndpointKey '{destinationRequest.TableSettingsId}' is not a REP_PRIORITY_TABLE_SETTINGS ID | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/BulkTransferDestinationSL.cs#L38` |
| {(isVessel ?  | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/BulkTransferDestinationSL.cs#L47` |
| Destination API {requestUri} returned {(int)result.StatusCode}: {output} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/BulkTransferDestinationSL.cs#L65` |
| {MethodName}\| Error RepIntegration Service API details missing | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/IntegrationSL.cs#L34` |
| {MethodName}\| {ServiceName} not in services.json; status {Event} of transfer {TransferId} not reported | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/BulkTransferAckSL.cs#L51` |
| {MethodName}\| {Event} of transfer {TransferId} reported, HTTP {StatusCode} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/BulkTransferAckSL.cs#L66` |
| {MethodName}\| Could not report {Event} for file {FileName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/BulkTransferAckSL.cs#L70` |

## RepAzureRes

Logger templates in RepAzureRes. Keywords: RepAzureRes log, error.

| Message template | Source |
|---|---|
| WorkerService:StartAsync | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/WorkerService.cs#L33` |
| WorkerService:StopAsync | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/WorkerService.cs#L41` |
| {MethodName}\| process started with worker service Initiate status {InitiateStatus} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/WorkerService.cs#L49` |
| {MethodName}\| Process cycle started | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/WorkerService.cs#L67` |
| {MethodName}\| Process cycle completed | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/WorkerService.cs#L82` |
| ServiceConfigData is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/ServiceDependency.cs#L50` |
| CommonOperationBL.CreateDirectory | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L73` |
| CommonOperationBL.RewriteContent | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L144` |
| {MethodName}\|Error in deleting file {File} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L176` |
| {MethodName}\| Generating file for {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L188` |
| {MethodName}\|Error in generating json file | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L229` |
| {MethodName}\| File does not exist {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L246` |
| {MethodName}\| File is locked {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L253` |
| Json file not created | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L294` |
| Exception while generating blob chunk json file | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L298` |
| {MethodName}\| checking network status | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L318` |
| {MethodName}\|Network status: {NetworkStatus} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L335` |
| {MethodName}\|Error in checking network status | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L340` |
| CommonOperationBL.GetAzureBlobPrimaryConnectionString | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L363` |
| CommonOperationBL.CheckFile | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L388` |
| {MethodName}\|Error in deleting old files | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L468` |
| Azure Upload Pending Count has not been updated in 6 hours, resetting | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L477` |
| Integration Pending Count has not been updated in 3 hours, resetting | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L484` |
| Emptying static variables | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L493` |
| {MethodName}\|Started Process | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L56` |
| {MethodName}\| Azure Data Conduit Init Data completed with status {AzureInitStatus} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L65` |
| Error in {MethodName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L76` |
| {MethodName}\| Started saving file for Upload | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L96` |
| {MethodName}\| Source file does not exist. Skipping {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L133` |
| {MethodName}\| Failed to prepare file {FileName} for upload. Skipping file. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L190` |
| {MethodName}\| No valid files available for upload after validation | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L198` |
| {MethodName}\| Packet(s) already queued for upload, treating as awaiting | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L217` |
| {MethodName}\|Error in saving data to AzureResUploadEntities due to {ErrorMessage} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L226` |
| Exception in {MethodName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L240` |
| {MethodName}\|Intiating Upload process | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L252` |
| {MethodName}\|Service basic config is not available. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L258` |
| {MethodName}\|Upload process time exceeded. Removing status. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L282` |
| {MethodName}\|Upload process is already running. Exiting. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L288` |
| {MethodName}\| Upload process stopped, application is stopping | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L308` |
| {MethodName}\| Error occurred during upload process | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L312` |
| {MethodName}\| Initiating Azure Upload Call back process | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L327` |
| {MethodName}\| Azure config status is not success. Exiting callback. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L332` |
| {MethodName}\|Callback process time exceeded. Removing status. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L344` |
| {MethodName}\| Call back process stopped, application is stopping | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L369` |
| {MethodName}\| Error occurred during callback process | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L373` |
| {MethodName}\| Attempting to clear old JSON files | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L387` |
| {MethodName}\| Old JSON files cleared. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L397` |
| {MethodName}\| Archival already run today, skipping clear. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L405` |
| {MethodName}\|Started Uploading Pending Data | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L82` |
| {MethodName}\| No pending data found for upload | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L90` |
| {MethodName}\| Azure settings verification failed, cannot proceed with upload | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L98` |
| Azure Account Key is empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L127` |
| {MethodName}\| AzurePrimaryConnectionString is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L133` |
| {MethodName}\| NO network connection | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L140` |
| {MethodName}\| Chunk size {ChunkSize} exceeds MaxChunkSizeInKB, using {MaxChunkSize} bytes | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L152` |
| {MethodName}\| Chunk size is zero, network speed is low cannot proceed with upload | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L158` |
| {MethodName}\| Uploading files with chunk size {ChunkSize} bytes | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L162` |
| {MethodName}\| Application is stopping, no new upload batch is started | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L171` |
| {MethodName}\|No network | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L184` |
| {MethodName}\| No valid Azure resume upload data found for processing | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L201` |
| {MethodName}\| Uploading {Count} number of files | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L212` |
| {MethodName}\| Folder structure {FolderStructure} is in invalid format for file {FileName}, updating to default format | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L236` |
| {MethodName}\|Upload pending process END | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L263` |
| {MethodName}\|FileName or file location is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L285` |
| {MethodName}\|File {FileName} does not exist in source location and Json file also does not exist | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L305` |
| {MethodName}\|updating failed status to Db completed with {Status} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L346` |
| {MethodName}\| Json file content is null or empty for file {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L435` |
| {MethodName}\| Json file is corrupted for file {FileName} — deleting and regenerating | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L462` |
| {MethodName}\| Failed to regenerate Json file for {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L473` |
| {MethodName}\| Invalid block metadata for file {FileName}. Reason: {Reason}. Regenerating json. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L484` |
| {MethodName}\| Failed to regenerate Json file for {FileName} after invalid block metadata | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L497` |
| Invalid block metadata and regeneration failed for {uploadWorkerParamsEntity.UploadEntity.FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L498` |
| {MethodName}\| Regenerated block metadata is still invalid for file {FileName}. Reason: {Reason} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L508` |
| Invalid regenerated block metadata for {uploadWorkerParamsEntity.UploadEntity.FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L510` |
| {MethodName}\| Starting upload for file {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L514` |
| {MethodName}\| upload Process completed for file {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L573` |
| {MethodName}\|Upload worker crashed for {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L578` |
| {MethodName}\| Upload failed status update completed with status code {UpdateStatusCode} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L591` |
| {MethodName}\| Calculating MD5 for {FileName} ({FileSize} bytes) | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L599` |
| MD5 checksum could not be calculated for {uploadEntity.FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L618` |
| MD5 checksum could not be saved for {uploadEntity.FileName}: {saveStatus?.ErrorMessage} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L623` |
| {MethodName}\| MD5 saved for {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L626` |
| {MethodName}\| Heartbeat update failed for {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L661` |
| Azure Blob Connection string is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L679` |
| {MethodName}\| Uploading to blob {BlobName} number of chunks uploaded {BlockSubListCount} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L695` |
| {MethodName}\| Found {StagedCount} already staged chunks for blob {BlobName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L724` |
| {MethodName}\| Pending chunks to upload {PendingId} for file {BlobName} and max count{MaxId} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L731` |
| Expected {blockSub.Buffer} bytes at offset {blockSub.Offset} but file ended after {totalRead} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L745` |
| {MethodName}\| Blob {BlobName} uploaded successfully | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L774` |
| {MethodName}\| Exception | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L780` |
| {MethodName}\| Upload is failed for file {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L831` |
| {MethodName}\| Old json files cleared | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L889` |
| AzurePrimaryConnectionString is empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1028` |
| Azure connecitons string is empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1029` |
| Verified Access to container  | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1033` |
| {MethodName}\| File {FileName} of {FileSize} bytes needs chunk size {MinChunkSize} to stay within {MaxBlockCount} blocks, configured {ChunkSize} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1126` |
| Exception in {MethodName} for {FileLocation} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1133` |
| {MethodName}\| Calculating chunk size for speed: {Speed} KB/s | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1140` |
| {MethodName}\| Using 4MB chunks for very fast connection | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1145` |
| {MethodName}\| Using 2MB chunks for fast connection | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1150` |
| {MethodName}\| Using 1MB chunks for medium connection | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1155` |
| {MethodName}\| Using 256KB chunks for slow connection | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1160` |
| {MethodName}\| Using 64KB chunks for very slow connection | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1165` |
| {MethodName}\| Connection too slow for upload, speed: {Speed} KB/s | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1170` |
| {MethodName}\| Starting upload speed test | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1180` |
| {MethodName}\| Upload test: {DataSize} bytes in {Time} seconds | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1205` |
| {MethodName}\| Calculated upload speed: {Speed} KB/s | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1210` |
| {MethodName}\| Speed test failed, assuming very slow connection | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1215` |
| {MethodName}\| Starting V2V Azure Resend Data | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1232` |
| {MethodName}\| {Packet} exists status {AzureFileStatus} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1246` |
| {MethodName}\| V2V Azure Resend Data Completed | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1269` |
| {MethodName}\| Checking if file {FileName} exists in container {ContainerName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1293` |
| {MethodName}\| file size mismatch for {FileName} blob Size: {BlobFileSize} ,Actual Size: {FileSize} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1312` |
| {MethodName}\| file checksum mismatch for {FileName} blob checkSum: {BlobCheckSum} ,Actual CheckSum: {CheckSum} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1324` |
| {MethodName}\| file {FileName} exists in container {ContainerName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1337` |
| {MethodName}\| file {FileName} does not exist in container {ContainerName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1349` |
| Error encrypting:  | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/EncryptionBL.cs#L52` |
| {MethodName} Started | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L39` |
| {MethodName}\| No finished Azure resume call back data found for processing | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L46` |
| {MethodName}\| Application is stopping, no new call back batch is started | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L58` |
| {MethodName}\| No valid Azure resume call back data found for processing | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L69` |
| {ApiError} \| Error while calling integration API | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L115` |
| {MethodName} Ended | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L142` |
| {ErrorMethod} \| Error while processing finished data | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L151` |
| AzureResUploadController.TestService | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/Controllers/AzureResUploadController.cs#L36` |
| AzureResUploadController.ResumeUpload | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/Controllers/AzureResUploadController.cs#L44` |
| {MethodName}\| Error RepDblogW Service API details missing | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L27` |
| Api address is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L46` |
| {MethodName}\| DB service returned {StatusCode} with output {Output} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L112` |
| {MethodName}\| save failed for input {ReqJson} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L124` |
| Api URL is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L143` |
| {MethodName}\| update failed for input {ReqJson} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L165` |
| Base URL is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L189` |
| {MethodName}\| update and move to Hisotry failed for input {ReqJson} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L406` |
| API URL is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/IntegrationSL.cs#L40` |

## RepCompression

Logger templates in RepCompression. Keywords: RepCompression log, error.

| Message template | Source |
|---|---|
| Data did not save Successfully | `RepCompression/MariApps.PAL.Rep.Compress.DAL/CompressRepository.cs#L109` |
| {MethodName} - Validation failed: {Error} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBatchBL.cs#L36` |
| {MethodName} - Processing GroupId {GroupId}, output: {OutputPath} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBatchBL.cs#L49` |
| {MethodName} - GroupId {GroupId} compressed successfully | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBatchBL.cs#L89` |
| {MethodName} - Compression failed for GroupId {GroupId} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBatchBL.cs#L93` |
| {MethodName} - Could not delete partial file: {Path} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBatchBL.cs#L196` |
| The FileName Generated  | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L106` |

## RepDBLogW

Logger templates in RepDBLogW. Keywords: RepDBLogW log, error.

| Message template | Source |
|---|---|
| Data did not save Successfully | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L80` |
| Error in {MethodName} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/Rep2IDbRepository.cs#L64` |
| {MethodName}\| Transient error (attempt {RetryAttempt}/{MaxAttempts}), retrying in {DelayMs}ms | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L960` |
| Error in {MethodName} after {RetryCount} retries | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L967` |
| Exception in {MethodName} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1030` |
| {MethodName}\| Duplicate submission, record already queued: {Message} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2432` |
| Data did not save Successfully\|{outputData?[1]?.Value} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2436` |
| SbusNotificationRepository.UpdateAzureResUploadData - Transient error (attempt {RetryAttempt}/{MaxAttempts}), retrying in {DelayMs}ms | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2475` |
| SbusNotificationRepository.UpdateAzureResUploadData - Permanent error after {RetryCount} retries | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2483` |
| Exception in Db call for {MethodName} with input Type:{Type}, Read Status {Status}, RecordCount {RecordCount}, NewUpdateStatus {UpdateStatus} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2700` |
| Exception in {MethodName} after {RetryCount} retries | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2745` |
| {MethodName}\| Row with NAME 'REP_MANUAL_OP_PATH' not found | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/Rep2XDbRepository.cs#L92` |
| {MethodName}\| Error checking if Azure resource data exists for status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L63` |
| {MethodName}\| Error checking if Azure download data exists for status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L100` |
| {MethodName}\| Azure downloads saved successfully | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L132` |
| {MethodName}\| Error while saving Azure downloads | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L142` |
| Exception occurred while saving Azure downloads in {MethodName} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L153` |
| {MethodName}\| Export type updated successfully for vesselObjectId: {VesselObjectId} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L177` |
| Exception occurred while updating export type in {MethodName} for vesselObjectId: {VesselObjectId} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L181` |
| {MethodName}\| Import Queue Data saved | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L212` |
| {MethodName}\| Error while saving Import Queue Data | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L222` |
| Exception occured while saving data in {MethodName} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L233` |
| {MethodName}\| Error checking Azure resource data exists for status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/AzureDblogBL.cs#L58` |
| {MethodName}\| Error checking Azure download data exists for status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/AzureDblogBL.cs#L84` |
| {MethodName}\| Error updating export type for vesselObjectId: {VesselObjectId} with exportType: {ExportType} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/AzureDblogBL.cs#L104` |
| {MethodName}\| Error occurred while saving Azure downloads bulk data. | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/AzureDblogBL.cs#L159` |
| {MethodName}\| error in save to import validate queue | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/DBlogWBL.cs#L46` |
| START: AzureDblog\|CheckAzureResDataExists\|Status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L37` |
| END: AzureDblog\|CheckAzureResDataExists\|Status: {Status}\|Result: {DataExists} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L41` |
| START: AzureDblog\|CheckAzureDownloadDataExists\|Status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L56` |
| END: AzureDblog\|CheckAzureDownloadDataExists\|Status: {Status}\|Result: {DataExists} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L60` |
| START: AzureDblog\|ProcessNgV4SyncHd\|ID: {ID} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L75` |
| END: AzureDblog\|ProcessNgV4SyncHd\|ID: {ID} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L80` |
| START: AzureDblog\|SaveAzureDownloadsBulk\|Count: {Count} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L104` |
| END: AzureDblog\|SaveAzureDownloadsBulk\|Status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L108` |
| START: AzureDblog\|UpdateExportType\|VesselObjectId: {VesselObjectId}\|ExportType: {ExportType} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L124` |
| END: AzureDblog\|UpdateExportType\|VesselObjectId: {VesselObjectId} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L128` |

## RepDecompress

Logger templates in RepDecompress. Keywords: RepDecompress log, error.

| Message template | Source |
|---|---|
| {MethodName}\| Input is null | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/ValidateBL.cs#L84` |
| {MethodName}\| ImportQId is 0 | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/ValidateBL.cs#L94` |
| {MethodName}\| VesselObjectId is 0 | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/ValidateBL.cs#L104` |
| {MethodName}\| SplitFiles is null or empty | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/ValidateBL.cs#L114` |
| {MethodName}\| FileLocation is null or file does not exist | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/ValidateBL.cs#L124` |
| {MethodName}\| Unzipping the file: {InFile} to {OutFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L76` |
| Invalid LZMA header: too short | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L90` |
| Unexpected end of file while reading size. | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L100` |
| {MethodName}\| Successfully decompressed: {InFile} to {OutFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L109` |
| {MethodName}\| File I/O error during decompression: {InFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L116` |
| {MethodName}\| Invalid data error during decompression: {InFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L120` |
| {MethodName}\| Unexpected Exception during decompression: {InFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L124` |
| {MethodName}\| Unzipping the file: {InputFile} to {OutputDirectory} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L194` |
| {MethodName}\| Skipping suspicious entry outside output directory: {EntryKey} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L222` |
| {MethodName}\| Extraction attempt {Attempt}/{MaxAttempts} failed with I/O error, retrying in {DelayMs}ms: {Message} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L261` |
| {MethodName}\| All {MaxAttempts} extraction retry attempts failed for file {InputFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L270` |
| {MethodName}\| File is locked or not accessible: {FilePath} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L304` |
| File is locked or not accessible: {filePath} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L305` |
| {MethodName}\| I/O error during TAR extraction: {InputFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L317` |
| {MethodName}\| Permission error while extracting: {InputFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L322` |
| {MethodName}\| Unexpected error during TAR extraction: {InputFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L327` |
| {MethodName}\| Extracted tar.zst archive to {OutputFolder} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L419` |
| {MethodName} Files extracted error, extractPath: {ExtractPath}, Message:{Message} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L433` |
| {MethodName}\| Converting MessagePack files to JSON format in folder: {FolderPath} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L443` |
| {MethodName}\| Converted {MsgPackFile} to {JsonFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L466` |
| {MethodName}\|  Error converting MessagePack file to JSON: {MsgPackFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L472` |
| {MethodName}\| Error during MessagePack to JSON conversion in folder: {FolderPath} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L480` |
| {MethodName}\|File:{FileName} is being used waiting for {WaitTime} milliseconds\| CHECK Count {CheckCount} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L506` |
| Exception in {MethodName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L520` |
| {MethodName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L537` |
| {MethodName}\| Failed to delete existing destination file {File}, will attempt overwrite: {Message} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L619` |
| {MethodName}\| Failed to copy file {Source} after {Attempts} attempts | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L642` |
| {MethodName}\| Copy attempt {Attempt}/{MaxAttempts} failed for {Source}, retrying in {DelayMs}ms: {Message} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L647` |
| {MethodName}\| Failed to delete source file {Source} after {Attempts} attempts | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L671` |
| {MethodName}\| Delete attempt {Attempt}/{MaxAttempts} failed for {Source}, retrying in {DelayMs}ms | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L676` |
| {MethodName}\| Creating original copy of extraction files failed for count {Count} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L694` |
| {MethodName}\| Error while copying files from {Source} to {Destination} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L706` |
| {MethodName}\| Failed to delete file: {FilePath} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L736` |
| {MethodName}\| Failed to delete subdirectory: {SubDirPath} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L749` |
| {MethodName}\| Failed to delete directory and its contents: {DirectoryPath} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L758` |
| {MethodName}\| Starting to process for Vessel {VesselObjectId} and Packet Counter {PacketCounter} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L41` |
| {MethodName}\| Base folder could not be found, exiting the process | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L51` |
| Base folder is not set. | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L52` |
| {MethodName}\| Could not create working copy of split files | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L77` |
| {MethodName}\| Extracting {FileName} contents | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L101` |
| {MethodName}\| Extraction failed for {FileName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L118` |
| {MethodName}\| Extraction aborted for {FileName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L125` |
| {MethodName}\| File content for {FileName} was extracted successfully | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L176` |
| {MethodName}\| Extracted files to be processed further: {Count} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L180` |
| {MethodName}\| Some files in the manifest are missing in the extracted files: {MissingFiles} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L222` |
| {MethodName}\| Table Settings ID fetched for Packet Header file {FileName} is {TableSettingsId} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L243` |
| {MethodName}\| Table Settings ID fetched for Packet Info file {FileName} is {TableSettingsId} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L265` |
| {MethodName}\| Extraction completed successfully for {VesselObjectId} and packet counter {PacketCounter} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L286` |
| {MethodName}\| No files were extracted for {VesselObjectId} and packet Counter {PacketCounter} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L292` |
| {MethodName}\| Extracting packet from {FileName} to {UnzipDirectory} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L334` |
| {MethodName}\| Skipping non-archive file with extension {Extension}: {FileName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L341` |
| The extension  | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L365` |
| {MethodName}\| No files extracted from {FileName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L370` |
| {MethodName}\| Files extracted successfully from {FileName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L377` |
| {MethodName}\| Invalid Request | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/Controllers/DecompressController.cs#L90` |

## RepFileMerge

Logger templates in RepFileMerge. Keywords: RepFileMerge log, error.

| Message template | Source |
|---|---|
| {MethodName}\| Starting to process for Vessel {VesselObjectId} and Packet Counter {PacketCounter} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L275` |
| {MethodName}\| Base folder could not be found, exiting the process | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L290` |
| Base folder is not set. | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L291` |
| {MethodName}\| File is being used by another process, exiting the process | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L324` |
| {MethodName}\| File {FileName} could not be merged | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L345` |
| {MethodName}\| All Split files available for file {FileName}, not merging | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L373` |
| {MethodName}\| Not all split files are available for file {FileName} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L378` |
| {MethodName} File {FileName} has been merged with status {MergedStatus} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L389` |
| {MethodName} File {FileName} could not be moved to destination location as merged file is missing | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L393` |
| {MethodName} Merge operation has been completed and File {FileName} has been moved to destination location {DestinationLocation} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L404` |
| {MethodName}\| File {FileName} is no longer accessible while fetching metadata | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L411` |
| {MethodName}\| Critical exception while merging file | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L437` |
| {MethodName}\| Input is null | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L90` |
| {MethodName}\| ImportQId is mandatory | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L100` |
| {MethodName}\| Packet counter is mandatory | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L110` |
| {MethodName}\| Split count is mandatory | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L120` |
| {MethodName}\| VesselObjectId is mandatory | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L130` |
| {MethodName}\| SplitFiles is mandatory | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L140` |
| {MethodName}\| One or more SplitFiles have empty FileLocation | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L150` |
| {MethodName}\| One or more SplitFiles are missing. Sample files: {MissingFiles} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L165` |
| {MethodName}\| Merging file {FileName} at location {MergeLocation} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L29` |
| {MethodName}\| Finished combining all split files into {MergeFileName} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L55` |
| {MethodName}\| IO Exception while combining files | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L63` |
| {MethodName}\| Unauthorized access while combining files | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L67` |
| {MethodName}\| General Exception in combining files | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L71` |
| {MethodName}\|File:{FileName} is being used waiting for {WaitTime} milliseconds\| CHECK Count {CheckCount} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L116` |
| Exception in {MethodName} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L130` |
| {MethodName} File {FileName} is locked or not accessible | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L167` |
| {MethodName} Split File {FileName} is locked or not accessible | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L192` |
| {MethodName} File {FileName} moved to destination location {DestinationFolder} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L195` |
| {MethodName} Exception while moving file {FileName} to destination location {DestinationFolder} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L201` |

## RepIntegration

Logger templates in RepIntegration. Keywords: RepIntegration log, error.

| Message template | Source |
|---|---|
| WorkerService StartAsync | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L31` |
| WorkerService StopAsync | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L38` |
| {MethodName}\|WorkerService:ExecuteAsync\|Start | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L45` |
| {MethodName}\| Process Cycle begings | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L59` |
| {MethodName} \| invoking common init data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L64` |
| {MethodName} \| Initiating Integration export processes | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L70` |
| {MethodName}\| Calling auto resend process for Priority Resend | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L74` |
| {MethodName}\| Invoking General Notification sending method | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L77` |
| {MethodName}\| Integration main processes not started due to InitiateOnInterval is false | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L93` |
| {MethodName}\| Process Cycle ends | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L95` |
| {MethodName}\| Host stopping, process cycle cancelled | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L100` |
| {MethodName} \| Work service failed  | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L105` |
| {MethodName}\|Ended | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L110` |
| WorkerService Dispose | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L117` |
| {MethodName}\|Sending missing packet and updating missing packt status via notification for input | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L930` |
| {MethodName}\| Starting Process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L992` |
| {MethodName}\| Process started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L79` |
| {MethodName}\| Process completed with message: {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L95` |
| {MethodName}\| Track save is completed with message {Message}\| Invoking export based on Condition {InvokeExportAfterSave} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L128` |
| {MethodName}\| Process completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L132` |
| {MethodName}\| Track save is being processed with Message {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L160` |
| {MethodName}\| Track record save is completed with message {Message}\| Invoking export based on Condition {InvokeExportAfterSave} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L163` |
| {MethodName}\| Process completed with message {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L168` |
| {MethodName}\| Transfer Process Initiate is disabled | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L486` |
| {MethodName}\| Call back gotten for {Id} and file name {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L565` |
| {MethodName}\| Process started for Vessel {VesselObjectid} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L629` |
| {MethodName}\| {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L673` |
| {MethodName}\| Started for file {FileName} ({FileSizeInKB} KB) with endpoint key {EndpointKey} to vessels {VesselList} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L690` |
| {MethodName}\| Table settings {TableSettingsId} not found or has no {UrlColumns} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L732` |
| {MethodName}\| Transfer request failed for vessel {VesselObjectId} with message {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L777` |
| {MethodName}\| Transfer {TransferId} queued for vessel {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L781` |
| {MethodName}\| Error while requesting transfer for vessel {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L799` |
| {MethodName}\| Ended with {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L821` |
| {MethodName} \| Should the common initialization process be invoked? Process Init Status: {ProcessInitStatus} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L868` |
| {MethodName}\| Process started invoke status -{Invoke} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L879` |
| {MethodName}\| Transfer Resend process is already running, skipping initiation | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L907` |
| {MethodName}\| Initiating File Resend Process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L918` |
| {MethodName}\| Transfer resend process has not been started, Service Data Status:{ServiceStatus}\| Is resend Process running {ResendStatus}\| next resend time reac | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L923` |
| {MethodName} \| Exception occured while invoking priority resend. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L954` |
| {MethodName}\| Initiating General Notification Sending | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L1005` |
| {MethodName}\| General notification send process has not been started, Service Data Status:{ServiceStatus}\| Is notif process running {GeneralNotifStatus} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L1033` |
| {MethodName}\| Transfer Queue Save data status : {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L500` |
| Invalid Data gotten from Transfer Service\| Message:  | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L2028` |
| Transfer Channel data gotten is invalid exiting | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L2033` |
| {MethodName}\| no transfer information found to resend to vessel {Vessel} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L2110` |
| {MethodName}\| Export Process started with param IsVessel {Param1} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L118` |
| {MethodName}\| Channel Flow is empty | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L127` |
| {MethodName}\| No PR enabled vessels found. Exiting. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L135` |
| {MethodName}\| New Export invocation is enabled. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L142` |
| {MethodName}\| New Export invocation is disabled. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L147` |
| {MethodName}\| Reading pending records information for channel : {InputChannelFlow} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L156` |
| {MethodName}\| No pending records found for channel : {InputChannelFlow} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L170` |
| {MethodName}\| Processing pending records for vessel object id : {VesselObjectId} with record count : {RecordCount} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L185` |
| {MethodName}\| Channel Flow is empty for specific channel {ItemChannel} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L234` |
| {MethodName}\| calling main export call methods | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L238` |
| {MethodName}\| Remaining pending records count for vessel object id : {VesselObjectId} is {RemainingCount} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L256` |
| {MethodName}\| Queued processing for vessel object id : {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L259` |
| {MethodName}\| Completed processing all pending records for all vessels count {Count} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L273` |
| {MethodName}\| Export Process completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L277` |
| {MethodName}\| Exception while processing pending data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L295` |
| File content is null  | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L629` |
| {MethodName}\| No pending transfer data found for processing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L959` |
| {MethodName}\| No valid transfer data was found for processing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L989` |
| {MethodName}\| Processing trasnfer queue for  {Count} number of files | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L997` |
| {MethodName}\| Processing file {FileName} with retry Count {RetryCount} from service {CurrentProcessedServiceId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1001` |
| {MethodName}\| Invalid transfer item gotten with Id {Id} for file {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1049` |
| {MethodName}\| Invalid transfer channel gotten {TransferChanneId} for file {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1055` |
| {MethodName}\| Updated transfer queue error status to Failed for file {FileName}, with update Status {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1061` |
| {MethodName}\| Invalid file name or file location gotten for file {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1067` |
| {MethodName}\| Validated transfer item for file {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1076` |
| {MethodName}\| Starting worker for file {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1090` |
| {MethodName}\| Completed worker for file {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1140` |
| {MethodName}\| Updated transfer queue error status to Failed for file {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1162` |
| {MethodName}\| Transfer Queue process has been completed for all service for {FileName} after service Id {ServiceId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1212` |
| {MethodName}\| File {FileName} not found at location {FileLocation} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1277` |
| {MethodName}\| Error while moving file {FileName} to sent folder {SentFolder} with status {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1286` |
| {MethodName}\|Bulk transfer file {FileName} sent to vessel {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1358` |
| {MethodName}\|Export path not found for replica type {ReplicaTypeId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1368` |
| {MethodName}\| Transfer Queue process has been completed for {FileName} with service Id {ServiceId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1385` |
| {MethodName}\| Transfer Queue process awaiting response for {FileName} for service {ServiceName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1405` |
| {MethodName}\| Transfer Queue process failed as gotten invalid response for {FileName} for service Id {Service} with return code {StatusCode} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1424` |
| {MethodName}\| Transfer Queue process has reached maximum retry limit for {FileName} for service Id {Service} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1450` |
| {MethodName}\| Initiating Priority Resend\| Vessel input-{VesselId} or all vessels | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1542` |
| {MethodName}\| Transfer channel not found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1550` |
| Transfer channel not found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1551` |
| {MethodName}\| No priority resend packets found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1560` |
| {MethodName}\| Priority Resend process completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1584` |
| {MethodName}\| Starting to send missing packet notification | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1597` |
| {MethodName}\| General Notification sending is not enabled | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1611` |
| {MethodName}\| No pending notification queue data found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1625` |
| {MethodName}\| Processing notification for record {RecordId} for notif {NotificationType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1633` |
| {MethodName}\| Completed sending missing packet notification | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1647` |
| {MethodName}\| Processing missing packet notification for item {RecordId}\| Type : {NotificationType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1658` |
| {MethodName}\| Data gotten is invalid for {Id}, aborting it | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1677` |
| {MethodName}\| No missing packet data found for RecordId {RecordId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1688` |
| {MethodName}\| Communication type {CommunicationType} is not supported for missing packet notification | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1695` |
| {MethodName}\| Missing packet notification queue name: {QueueName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1729` |
| {MethodName}\| no queue name found for missing packet notification for record {RecordId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1732` |
| {MethodName}\| Sbus notification failed for RecordId {RecordId} with error {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1756` |
| {MethodName}\| Completed processing missing packet notification for item {RecordId} \| Type : {NotificationType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1768` |
| {methodName} : Script Execution was cancelled by caller. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/SqlScriptExecutor.cs#L69` |
| {methodName} : concurrency gate exhausted max {opts.MaxConcurrentExecutions}, rejecting request | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/SqlScriptExecutor.cs#L80` |
| {methodName} : failed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/SqlScriptExecutor.cs#L129` |
| {MethodName} : PowerShell execution is disabled (ScriptExecutionOptions:PowerShell:Enabled). CorrelationId={CorrelationId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L78` |
| {MethodName} : cancelled while waiting for an execution slot. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L100` |
| {MethodName} : concurrency gate exhausted max {Max}, rejecting request | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L106` |
| {MethodName} : could not parse the wrapper result. CorrelationId={CorrelationId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L161` |
| {MethodName} : failed. CorrelationId={CorrelationId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L191` |
| {MethodName} : could not stop the PowerShell process. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L314` |
| {MethodName} : could not delete {Dir} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L359` |
| Embedded resource '{WrapperResourceName}' is missing from {assembly.GetName().Name}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L367` |
| {MethodName}\| Initiating process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L49` |
| {MethodName}\| Process status added to memory store witht status {AddStatus} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L78` |
| {MethodName} - Error in initiating process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L82` |
| {MethodName}\| Required keys not found in fetched data {Keys} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L111` |
| {MethodName} - Error in reading Common CO Parameters values | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L119` |
| {MethodName}\| Vessel Data not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L144` |
| {MethodName} - Error in reading Vessel Data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L154` |
| {MethodName}\| Table Settings Id not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L178` |
| {MethodName} - Error in reading Priority Table Settings | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L187` |
| {MethodName}\| Channel details not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L213` |
| {MethodName} - Error in reading Priority Channel Details | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L222` |
| {MethodName}\| Channel flow information could not be found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L270` |
| {MethodName}\| Import Channel details not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L282` |
| {MethodName} - Error in reading Priority Import Channel Details | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L291` |
| {MethodName}\| Export Channel flow information could not be found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L339` |
| {MethodName}\| Export Channel details not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L351` |
| {MethodName} - Error in reading Priority Export Channel Details | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L360` |
| {MethodName}\| Setting Transfer Resend Run time | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L369` |
| Error in {MethodName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L378` |
| {MethodName}\| Setting Vessel Settings Update Time | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L388` |
| {MethodName}\| Setting Common Init Time | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L406` |
| {MethodName}\| Service Status not found in cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L433` |
| {MethodName}\| Vessel Data not found in cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L451` |
| Exception in {MethodName} while reading vessel data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L478` |
| {MethodName}\| Common Param Data not found in cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L495` |
| {MethodName}\| Common Param Data not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L505` |
| Exception in {MethodName} while reading common param data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L514` |
| {MethodName}\| Channel Data not found in cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L531` |
| {MethodName}\| Channel Data not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L542` |
| Exception in {MethodName} while reading channel data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L551` |
| {MethodName}\| Table Settings not found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L566` |
| {MethodName}\| Table Settings not found for TableSettingsId:{TableSettingsId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L573` |
| {MethodName}\| Table settings Data not found in cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L592` |
| {MethodName}\| Table settings Data not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L603` |
| {MethodName}\| Exception while reading tbale settings | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L613` |
| {MethodName}\| Channel Flow Settings Data not found in cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L631` |
| {MethodName}\| Channel Flow settings Data not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L642` |
| {MethodName}\| Exception while reading channel flow settings | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L652` |
| {MethodName}\| Channel Details not found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L671` |
| {MethodName}\| Value not found for key {KeyName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L690` |
| {MethodName}\| Channel Flow settings not found for ChannelId:{ChannelId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L709` |
| {MethodName}\| Vessel data not found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L724` |
| {MethodName}\| Vessel data not found for VesselObjectId:{VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L731` |
| {MethodName}\| MissingAt value is null or empty | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L759` |
| {MethodName}\| Vessel data not found in memory or database | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L765` |
| Exception in {MethodName} when checking resend data for {Vessel} or all | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L820` |
| Exception in {MethodName} when checking general resend data for {Vessel} or all | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L845` |
| {MethodName}\| Saving Transfer Queue Data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L854` |
| {MethodName}\| Checking if Transfer Queue data exists for status {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L865` |
| {MethodName}\| Moving Transfer Queue data to history | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L874` |
| {MethodName}\| Last Common Init Time not found, continuing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L924` |
| {MethodName}\| Current Time is less than {RetryThresholdinMin} minutes, waiting | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L929` |
| {MethodName}\| Last resend time not found, continuing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L951` |
| {MethodName}\| Last resend time is older than {Time} hour | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L956` |
| {MethodName}\| Last vessel settings update time not found, continuing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L980` |
| {MethodName}\| Last vessel settings update time is older than 7 days | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L985` |
| {MethodName}\| Error reading V2V Office Queue Name | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L1027` |
| {MethodName}\| Error sending Generic Notification | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L1049` |
| {MethodName}\| Error occurred while reading pending items from import Q | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L85` |
| {MethodName}\| Insert/upsert completed for table {TableName}. Status: {Status}, Message: {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L319` |
| {MethodName}\| Exception during insert/upsert for table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L324` |
| {MethodName}\| Failed to save packet details with status: {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L362` |
| {MethodName} \| Started reading track records (slim) for {ChannelCount} channels | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L59` |
| {MethodName} \| No track records found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L66` |
| {MethodName} \| Successfully processed {PendingRecordsCount} pending records (slim) | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L123` |
| {MethodName} \| Error occurred while reading track records (slim) | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L128` |
| {MethodName}\| Reading pending priority packets for channel flow data mapper : {ChannelFlowDataMapper} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L137` |
| {MethodName}\| Checking for priority track exceed conditions | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L146` |
| {MethodName}\| Reading priority track records for channel IDs : {ChannelIds} and vessel IDs : {VesselIds} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L157` |
| {MethodName}\| Updating priority track status for operation type : {OperationType} and data : {DataToUpdate} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L171` |
| {MethodName}\| Updating PR track record status for HD records count: {HdCount} and DT records count: {DtCount} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L180` |
| {MethodName} \| Error occurred while updating records status | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L210` |
| {MethodName} \| Error occurred while reading pending packet info for VesselObjectId: {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L232` |
| {MethodName}\| Error occurred while generating packet | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L257` |
| {MethodName}\| Error occurred while zipping batch | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L276` |
| {MethodName}\| Error in ReadCompressionType | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L335` |
| {MethodName}\| Error occurred while handling priority transfer | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L369` |
| Get-ScheduledTask failed:  | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ConfigEvaluation/MachineProbe.cs#L119` |
| {fileName} did not start | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ConfigEvaluation/MachineProbe.cs#L226` |
| {fileName} did not finish in {ProcessTimeout.TotalSeconds:0} s | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ConfigEvaluation/MachineProbe.cs#L239` |
| {MethodName}\| Started, deep:{Deep}, categories:{Categories} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ConfigEvaluation/ConfigEvaluationService.cs#L129` |
| {MethodName}\| Completed in {Duration} ms, pass:{Pass} warning:{Warning} fail:{Fail} skipped:{Skipped} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ConfigEvaluation/ConfigEvaluationService.cs#L177` |
| {MethodName}\| Database not reachable | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ConfigEvaluation/ConfigEvaluationService.cs#L218` |
| {MethodName}\| {Category} check {Code} could not run | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ConfigEvaluation/ConfigEvaluationService.cs#L566` |
| Invalid configuration for PR_REP_MAX_ATTACHMENT_SIZE | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L219` |
| generalTransferEntity.ChannelId | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L342` |
| generalTransferEntity.VesselObjectId | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L345` |
| generalTransferEntity.SourceClient | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L348` |
| generalTransferEntity.CommunicationType | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L351` |
| generalTransferEntity.SplitFiles | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L354` |
| bulkTransferEntity | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L374` |
| bulkTransferEntity.VesselList | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L378` |
| bulkTransferEntity.EndpointKey | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L381` |
| bulkTransferEntity.FilePath | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L388` |
| FilePath does not exist:  | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L392` |
| File is empty:  | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L395` |
| chatNotifMessage | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L428` |
| chatNotifMessage.MessageJson is null or empty | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L430` |
| chatNotifMessage.TableSettingsId is null, empty or 0 | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L434` |
| chatNotifMessage.DestinationDetails.UniqueId list is null, empty or 0 | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L436` |
| {MethodName}\| Process Started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L52` |
| {MethodName}\| Process Completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L60` |
| {MethodName}\| Export process is disabled by configuration | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L86` |
| {MethodName}\| Export process is already running | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L109` |
| {MethodName}\| Export queue process has been started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L130` |
| {MethodName}\| Export Queue process has been Completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L134` |
| {MethodName}\| Critical exception occurred during export queue processing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L138` |
| {MethodName}\| PR Transfer process is already running | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L200` |
| {MethodName}\| PR Transfer queue process has been started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L221` |
| {MethodName}\| PR Transfer queue process has been Completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L225` |
| {MethodName}\| Critical exception occurred during PR Transfer queue processing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L229` |
| {MethodName}\| General Packet Resend process is already running | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L289` |
| {MethodName}\| General Packet Resend process has been started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L309` |
| {MethodName}\| General Packet Resend process has been Completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L313` |
| {MethodName}\| Critical exception occurred during General Packet Resend processing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L317` |
| {MethodName}\|  Validating if general Export is enabled for Vessels | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L347` |
| {MethodName}\| Export process is disabled by configuration. Skipping general Export validation. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L354` |
| {MethodName}\| Not the right time to validate general Export for Vessels. Skipping. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L364` |
| {MethodName}\| This is not a vessel. Skipping general Export validation. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L375` |
| {MethodName}\| General Packet channel not found. Please check configuration. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L383` |
| {MethodName}\| General export is already enabled for this Vessel so Skipping. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L393` |
| {MethodName}\| Failed to enable general Export for Vessel {VesselObjectId}. Status: {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L405` |
| {MethodName}\| General Export validation completed for Vessel {VesselObjectId}. Save status: {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L442` |
| {MethodName}\| Exception occurred while validating general Export for Vessels | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L452` |
| {MethodName}\| Import process is disabled by configuration | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L471` |
| {MethodName}\| Import process is already running\| Another pass has been requested | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L496` |
| {MethodName}\| Import queue process has been started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L522` |
| {MethodName}\| Import Queue process has been Completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L526` |
| {MethodName}\| Import queue was triggered during the run, starting another pass | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L546` |
| {MethodName}\| Critical exception occurred during import queue processing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L552` |
| {MethodName}\| Starting acquisition process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L589` |
| {MethodName}\| Acquisition process completed with status: {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L605` |
| {MethodName}\| Starting dynamic table insert/upsert for table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L635` |
| {MethodName}\| Dynamic table insert/upsert completed for table {TableName}. Status: {Status}, Message: {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L641` |
| {MethodName}\| Retrieving service status | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L665` |
| {MethodName}\| Service status retrieved successfully | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L673` |
| {MethodName}\| Exception occurred while retrieving service status | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L701` |
| {MethodName}\| Invoking file Merge service for Packet {Counter} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportServiceHandler.cs#L41` |
| {MethodName}\| Process failed for {Counter} while handling file merge service, marking as failed\| Due to :{ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportServiceHandler.cs#L47` |
| {MethodName}\| Processing for {Counter} was aborted by merge service, due to Error :{Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportServiceHandler.cs#L57` |
| {MethodName}\| Merge process completed for {Counter} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportServiceHandler.cs#L78` |
| {MethodName}\| Database update failed while updating DT data for {Counter}, aborting and retrying later | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportServiceHandler.cs#L89` |
| {MethodName}\| Exception while handling file merge | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportServiceHandler.cs#L101` |
| {MethodName}\| Invoking Decompress service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportServiceHandler.cs#L134` |
| {MethodName}\| Process failed while handling Decompress service, marking as failed\| Due to :{ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportServiceHandler.cs#L140` |
| {MethodName}\| Processing was aborted by decompress service, due to Error :{Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportServiceHandler.cs#L150` |
| {MethodName}\| Process failed while decompressing {FileName}, aborting | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportServiceHandler.cs#L155` |
| {MethodName}\| Process completed successfully | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportServiceHandler.cs#L180` |
| {MethodName}\| Exception while handling decompress service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportServiceHandler.cs#L203` |
| {MethodName}\| Base URL or API URL is empty for priority Settings Id {SettingsId} for Packet Counter {Counter} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportServiceHandler.cs#L239` |
| {MethodName}\| Invoking Acknowledgement service for packet {Counter} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportServiceHandler.cs#L283` |
| {MethodName}\| Process failed while handling Ackn service, marking as failed\| Due to :{ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportServiceHandler.cs#L289` |
| {MethodName}\| Exception while handling ackn service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportServiceHandler.cs#L310` |
| {MethodName}\| Starting to build queue from Track Change Records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L50` |
| {MethodName}\| General Packet channel information not found. Exiting. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L58` |
| {MethodName}\| Working directory is not configured. Exiting. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L65` |
| {MethodName}\| No channel flow settings found for export. Exiting. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L75` |
| {MethodName}\| Retrieved {Count} channel flow settings | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L79` |
| {MethodName}\| No vessels found with General Export enabled. Exiting. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L93` |
| {MethodName}\| No pending track records found for export. Exiting. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L106` |
| {MethodName}\| Retrieved {Count} pending track records for export | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L111` |
| {MethodName}\| Completed building queue from Track Change Records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L126` |
| {MethodName}\| Exception occurred in InitiateTrackExport | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L130` |
| {MethodName}\| Processing TableSettingsId: {TableSettingsId} with {RecordCount} records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L153` |
| {MethodName}\| Exception occurred while processing TableSettingsId: {TableSettingsId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L165` |
| {MethodName}\| Exception occurred in ExportNextHandler | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L185` |
| {MethodName}\| Starting processing for TableSettingsId: {TableSettingsId} with {RecordCount} records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L192` |
| {MethodName}\| Compression failed for TableSettingsId: {TableSettingsId}. Marking records as failed. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L245` |
| {MethodName}\| Source file not found: {SourceFilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L301` |
| {MethodName}\| Failed to copy file to {DestFilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L309` |
| {MethodName}\| Error copying file from {SourceFilePath} to {DestFilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L318` |
| {MethodName}\| No files were copied for vessel folder: {VesselFolderPath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L326` |
| No files were copied for vessel folder:  | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L327` |
| {MethodName}\| Error processing vessel folder operations for VesselObjectId: {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L338` |
| {MethodName}\| Completed processing for TableSettingsId: {TableSettingsId}and packets are ready for Transfer | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L391` |
| {MethodName}\| Handling packet generation response | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L405` |
| {MethodName}\| Packet generation failed with message: {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L411` |
| {MethodName}\| Failed to update track record status | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L463` |
| {MethodName}\| Starting failure process for track records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L483` |
| {MethodName}\| No failed records to process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L496` |
| {MethodName}\| Failed to update status for failed track records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L506` |
| {MethodName}\| Exception occurred while processing failed track records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L511` |
| {MethodName}\| Starting packet transfer handler | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L519` |
| {MethodName}\| Transfer channel information not found. Exiting. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L535` |
| {MethodName}\| No active vessels available to process. Exiting. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L558` |
| {MethodName}\| Completed single pass through all vessels for packet transfer. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L585` |
| {MethodName}\| Exception occurred in PacketTransferHandler | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L589` |
| {MethodName}\| Vessel {VesselObjectId} has no pending packets. Skipping transfer. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L608` |
| {MethodName}\| Retrieved {PendingCount} pending packets for vessel {VesselObjectId}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L612` |
| {MethodName}\| {FailedCount} packets failed validation for vessel {VesselObjectId}. Updating them with error status. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L620` |
| {MethodName}\| Failed to update error status for {FailedCount} packets in vessel {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L634` |
| {MethodName}\| No valid packets remaining after validation for vessel {VesselObjectId}. Exiting transfer handler. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L641` |
| {MethodName}\| Proceeding with {ValidCount} valid packets for vessel {VesselObjectId} (from original {TotalCount}). | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L645` |
| Invalid or null transfer response received for vessel {vesselObjectId}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L667` |
| {MethodName}\| Transfer failed for vessel {VesselObjectId} with message: {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L672` |
| {MethodName}\| Failed to save transfer queue data for vessel {VesselObjectId} for count {TransferDataToSaveCount}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L746` |
| {methodName}\| Failed to update packet status for vessel {vessel.VesselObjectId} for count {successUpdateList.Count}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L752` |
| {MethodName}\| Exception occurred while processing packets for vessel {VesselObjectId}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L757` |
| {MethodName}\| Packet ID {PacketId} failed validation: {Errors} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L814` |
| {MethodName}\| Validation summary - Total packets: {TotalCount}, Valid: {ValidCount}, Failed: {FailedCount} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L825` |
| {MethodName}\| File not found at original location for Packet ID {PacketId}: {FilePath}. Attempting recovery. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L856` |
| {MethodName}\| File found at recovered location for Packet ID {PacketId}. Attempting to copy from {RecoveredPath} to {OriginalPath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L881` |
| {MethodName}\| Successfully copied file for Packet ID {PacketId} from {RecoveredPath} to {OriginalPath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L906` |
| {MethodName}\| Exception occurred during file validation and recovery for Packet ID {PacketId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L931` |
| {MethodName}\| Completed single pass through all vessels for packet transfer resend. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L1039` |
| {MethodName}\| Retrieved {PendingCount} pending resend packets for vessel {VesselObjectId}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L1061` |
| {methodName}\| Failed to save transfer queue data for vessel {vessel.VesselObjectId} for count {transferDataToSave.Count}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L1208` |
| {methodName}\| Exception occurred while processing packets for vessel {vesselObjectId}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L1219` |
| {MethodName}\| Starting Import Process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L46` |
| {MethodName}\|No Pending Communication type in import data to process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L82` |
| {MethodName}\| Starting import process for CommunicationType: {CommunicationType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L103` |
| {MethodName}\| Added ImportVesselWorker task for CommunicationType: {CommunicationType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L109` |
| {MethodName}\| Exception occured which crashed the process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L128` |
| {MethodName}\| Cleared all running comm types | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L134` |
| {MethodName}\| Starting import for Vessels -{Count} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L151` |
| {MethodName}\| Current Client details not found, cannot proceed with import | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L159` |
| {MethodName}\| General Notification Channel not found, cannot proceed with import | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L166` |
| {MethodName}\| Skipping Vessel {VesselId} for CommunicationType {CommType} as vessel is missing a packet | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L216` |
| {MethodName}\| Completed import for Vessels -{Count} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L247` |
| {MethodName}\| Exception occured while processing Import Queue Item | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L251` |
| {MethodName}\| Cleared running comm types for CommunicationType: {CommunicationType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L258` |
| {MethodName}\| No Pending Import Items found for Vessel {VesselId} and CommunicationType {CommType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L285` |
| {MethodName}\| Import Queue Item {Id} for Vessel {VesselId} and CommunicationType {CommType} is not valid, skipping | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L296` |
| {MethodName}\| Import Queue Item {Id} for Vessel {VesselId} and CommunicationType {CommType} has invalid files, skipping | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L318` |
| {MethodName}\| Processing Import Queue Item {Id} for Vessel {VesselId} and CommunicationType {CommType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L334` |
| {MethodName}\| Awaiting response received for Import Queue Item {Id}. Stopping current batch and re-reading latest queue data. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L373` |
| {MethodName}\| Completed Import Worker for Vessel {VesselId} and CommunicationType {CommType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L381` |
| {MethodName}\| Exception occured while processing Import Queue Item for Vessel {VesselId} and CommunicationType {CommType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L385` |
| {MethodName}\|Import Queue Item is null or not proper | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L400` |
| {MethodName}\|Channel for Import Queue Item {Id} is not valid | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L406` |
| {MethodName}\|Channel-{Channel} for Import Queue Item {Id} is not valid | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L412` |
| {MethodName}\|Channel Flow not found for channel-{Channel} for Import Queue Item {Id} is not valid | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L420` |
| {MethodName}\|Exception occured while validating Import Queue Item | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L428` |
| {MethodName}\|ImportQSubDtEntities is null or empty for ImportQueueItem {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L444` |
| {MethodName}\|AllZipDirectory does not exist or is not configured: {AllZipDirectory} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L451` |
| {MethodName}\|Failed to create AllZipDirectory: {AllZipDirectory} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L460` |
| {MethodName}\|FileLocation is empty or FileSize <= 0 for SubItem {SubItemId} in ImportQueueItem {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L468` |
| {MethodName}\|Error copying file from {ZipFilePath} to {FileLocation} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L492` |
| {MethodName}\|File {FileLocation} still does not exist after copy from {ZipFilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L498` |
| {MethodName}\|File {FileLocation} successfully copied from zip directory | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L503` |
| {MethodName}\|File {FileLocation} not found. Primary location missing. AllZipDirectory: {AllZipDirectory}, DirectoryExists: {DirExists}, FilePath: {ZipFilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L508` |
| {MethodName}\|All files validated for ImportQueueItem {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L520` |
| {MethodName}\| Matched with Acquisition File Service Id | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L535` |
| {MethodName}\| Matched with File Merge Service Id | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L540` |
| {MethodName}\| Matched with File Decompress Service Id | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L545` |
| {MethodName}\| Matched with Acknowledgement Service Id | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L550` |
| {MethodName}\| Matched with Sbus Send Update Service Id | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L555` |
| {MethodName}\| Service {ServiceId} is not implemented for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L569` |
| {MethodName}\| Import Item {Id} processing aborted or failed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L576` |
| {MethodName}Finished processing for all service for item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L583` |
| {MethodName}\| Import Item {Id} is awaiting response for next service {NextServiceId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L603` |
| {MethodName}\| Exception occured while processing Import Item for Service {ServiceId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L628` |
| {MethodName}\| Packet is waiting {PacketCounter} for another packet before this to proceeed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L699` |
| {MethodName}\| Exception occured while processing Import Item for Acquisition Batch Service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L708` |
| {MethodName}\| File Merge Service failed for Import Item {Id} with error {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L746` |
| {MethodName}\|Import item has been aborted due to error {ErrorMessage} for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L762` |
| {MethodName}\| Failed to update Import Queue Sub Data Items for Import Item {Id} with error {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L789` |
| {MethodName}\| Completed processing Import Item for File Merge Service for Import Queue Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L812` |
| {MethodName}\| Merge Process failed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L817` |
| {MethodName}\| Failed to save decompressed files to database for Import Item {Id} with error {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L925` |
| {MethodName}\| Failed to save decompressed succes info to In Packet H for Import Item {Id} with error {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L953` |
| {MethodName}\| Failed to update missing packet info for Import Item {Id}  | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L979` |
| {MethodName}\| Process failed while handling ackn service, marking as failed\| Due to :{ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1107` |
| {MethodName}\| Ackn service returned no saved ack ids for Import Item {Id}; no general notification queued | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1235` |
| {MethodName}Import queue process for Ackn Completed successfully for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1238` |
| {MethodName}\| Queue name is null or empty for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1279` |
| {MethodName}\| Sending notification to queue {QueueName} for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1285` |
| {MethodName}\| Exception while handling service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1292` |
| {MethodName}\| Notification operation type is not provided for Import Item {Id} aborting | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1312` |
| {MethodName}\| No IDs provided for General Notification for Import Item {Id} aborting | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1349` |
| {MethodName}\| No Missing Packet details found for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1375` |
| {MethodName}\| No table details found for Import Item {Id} for table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1423` |
| {MethodName}\| Unsupported notification operation type {OperationType} for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1470` |
| {MethodName}\| Sending General Notification for Import Item {Id} to queue {QueueName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1579` |
| {MethodName}\| Process failed while sending General Notification for Import Item {Id}, marking as failed\| Due to :{ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1585` |
| {MethodName}\| General Notification sent successfully for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1612` |
| {MethodName}\| Handling exception for Import Queue Item {Id} with status: {Status} and message: {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1622` |
| {MethodName}\| Import item has been aborted for Import Queue Item {Id}. Moving to history with ABORTED status | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1628` |
| {MethodName}\| Processing error for Import Queue Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1689` |
| {MethodName}\| Retry limit {RetryLimit} exceeded for Import Queue Item {Id}. Moving to history with ABORTED status | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1700` |
| {MethodName}\| Marking Import Queue Item {Id} as FAILED. Retry count: {RetryCount}/{RetryLimit} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1773` |
| {MethodName}\| Exception occurred while handling Import Queue Item exception for Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1786` |
| {MethodName}\| Start | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L209` |
| {MethodName}\| End with status {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L213` |
| ExecuteScriptAndGetResult : initiating, CorrelationId={CorrelationId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/ScriptExecutionController.cs#L34` |
| ExecuteScriptAndGetResult : finished, Status={Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/ScriptExecutionController.cs#L36` |
| ExecuteScriptAndGetResult : failed while attempting to execute script | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/ScriptExecutionController.cs#L61` |
| {MethodName}\| failed for transfer {TransferId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/BulkTransferStatusController.cs#L44` |
| {MethodName}\| failed while evaluating configuration | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/ConfigEvaluationController.cs#L74` |
| {MethodName}\| failed while building log summary | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/LogSummaryController.cs#L68` |
| {MethodName} - Start | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationQueueController.cs#L32` |
| {MethodName} - End | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationQueueController.cs#L48` |
| {MethodName}\| TransferService returned non-success status code {StatusCode} for request: {RequestJson} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/TransferSL.cs#L46` |
| {MethodName}\| Error occurred while processing priority transfer | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/TransferSL.cs#L65` |
| {MethodName}\| PacketCreationService returned non-success status code {StatusCode} for request: {RequestJson} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/PacketCreationSL.cs#L107` |
| {MethodName}\| Error occurred while calling PacketCreationService\| Request: {RequestJson} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/PacketCreationSL.cs#L124` |
| {MethodName}\| Compression service returned {StatusCode}: {Body} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/CompressionSL.cs#L46` |
| {MethodName}\| Successfully updated export type for vesselObjectId: {VesselObjectId} to exportType: {ExportType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/DBlogWSL.cs#L59` |
| {MethodName}\| Failed to update export type for vesselObjectId: {VesselObjectId}. Status code: {StatusCode}, Response: {Response} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/DBlogWSL.cs#L64` |
| {_methodNamePrefix} : DI Constructor -> DefaultConnection is not configured / loaded properly | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L30` |
| {methodName} : the script supplied is empty or null, nothing to proceed with | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L46` |
| Script supplied is empty or null, nothing to proceed with | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L47` |
| {methodName} : DefaultConnection is not configured, cannot proceed | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L52` |
| DefaultConnection is not found in configuration | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L53` |
| maxRowCount is set to 0; which will let the row count to unlimited; | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L68` |
| ScriptExection.MaxRecordInSingleExecutionFilter is set to 0; | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L79` |
| {methodName} : Executing SQL Script, length {script.Length}, maxRowCount = {maxRowCount}, maxResultSet = {maxResultSets} and maxExecutionTimeSecond = {maxExecut | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L108` |
| {methodName} : MaxResultSets {maxResultSets} reached, remaining results will be capped | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L118` |
| {methodName} : MaxRowCount {maxRowCount} reached on result set {resultSetIndex}, remaining rows discarded | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L135` |
| {methodName} : Script executed successfully, {resultSets.Count} result set(s) | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L173` |
| {methodName} : Execution exceeded the {maxExecutionTimeSeconds}s limit and was cancelled | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L184` |
| Script execution exceeded the configured limit of {maxExecutionTimeSeconds} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L185` |
| {methodName} : Script execution cancelled by cancellation request | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L188` |
| Script execution cancelled by cancellation request | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L189` |
| {methodName} : Error occurred while executing script. | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L192` |
| {methodName} : No batches supplied, nothing to execute | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L208` |
| No script batches supplied, nothing to execute | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L209` |
| {methodName} : executing batch {i + 1} of {batches.Count} against [{connection.Database}] | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L242` |
| {methodName} : execution exceeded the {maxExecutionTimeSeconds}s limit and was cancelled | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L250` |
| {methodName} : execution cancelled by cancellation request | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L255` |
| {methodName} : error occurred while executing script batches. | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L260` |
| Exception in {MethodName} for type {IsExport} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L84` |
| {MethodName}\|Exception occured while reading vessels | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L120` |
| {MethodName}\|Exception while reading resend Packet | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L144` |
| {MethodName}\| Transfer Queue Data saved successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L172` |
| {MethodName}\| Error while saving transfer Queue Data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L182` |
| {MethodName}\| Error in saving trasnfer Queue data Items | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L193` |
| {MethodName}\| Error checking if Transfer Queue data exists | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L226` |
| {MethodName}\| Transfer Queue data moved to history successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L253` |
| {MethodName}\| Error while moving Transfer Queue data to history | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L263` |
| {MethodName}\| Error in moving Transfer Queue data to history | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L274` |
| {MethodName}\| Error in reading Pending Import Queue Common Type | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L304` |
| {MethodName}\| Error in updating Import Queue Exceed Items | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L326` |
| {MethodName}\| Error in reading Pending Import Queue | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L353` |
| Exception occured in {MethodName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L382` |
| {MethodName}\| Import Queue Data saved | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L411` |
| {MethodName}\| Error while saving Import Queue Data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L421` |
| Exception occured while saving data in {MethodName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L432` |
| {MethodName}\| Import Queue Data updated successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L467` |
| {MethodName}\| Error while saving updating import Queue Data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L477` |
| {MethodName}\| Error in updating Import Queue data Items | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L488` |
| {MethodName}\| Import Queue sub details Data updated successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L523` |
| {MethodName}\| Error while saving updating import Queue sub details  Data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L533` |
| {MethodName}\| Error in updating Import Queue sub details  data Items | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L544` |
| {MethodName}\| Import Queue Data moved to history successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L579` |
| {MethodName}\| Error while  moving import Queue Data to history | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L589` |
| {MethodName}\| Error in moving Import Queue data Items to history | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L600` |
| {MethodName}\| Table name cannot be null or empty | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L620` |
| {MethodName}\| No IDs provided for table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L626` |
| {MethodName}\| Error fetching data from table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L700` |
| {MethodName}\| Target table name cannot be null or empty | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L714` |
| {MethodName}\| No data provided for insertion to table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L725` |
| {MethodName}\| Inserted: {Inserted}, Updated: {Updated} rows to table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L884` |
| {MethodName}\| Error inserting/updating data to table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L895` |
| {MethodName}\| Exception while validating Import Queue for Vessel {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L929` |
| {MethodName}\| Pr Rep In Packet dt data saved successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1017` |
| {MethodName}\| Error while  saving Pr rep in packet dt data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1027` |
| {MethodName}\| Error in saving Pr rep in packet dt data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1038` |
| {MethodName}\| Exception in updating Pr Rep In Packet data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1081` |
| {MethodName}\| Error updating missing packet info | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1113` |
| {MethodName}\| Error reading Track Records | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1140` |
| {MethodName}\| Records status updated successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1161` |
| {MethodName}\| Error updating records status | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1166` |
| {MethodName}\| Error while fetching pending priority packets | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1193` |
| {MethodName}\| Error while checking priority track exceed | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1211` |
| {MethodName}\| Error while fetching priority track records | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1236` |
| {MethodName}\| Error while updating priority track status | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1259` |
| {MethodName}\| Error while updating PR track record status | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1283` |
| {MethodName}\| PR Packet Status updated successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1310` |
| {MethodName}\| Error while updating PR Packet Status: {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1315` |
| {MethodName}\| Error updating PR Packet Status | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1322` |
| {MethodName}\| Error reading Pending Packet Info | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1349` |
| {MethodName} \| Started | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L153` |
| {MethodName} \| Pending Records fetched with Count: {PendingRecordsCount} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L201` |
| {MethodName}\| TableSettingsList fetched with Count: {TableSettingsListCount} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L221` |
| {MethodName}\| RecordList fetched with Count: {RecordListCount} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L244` |
| {MethodName}\| VesselObjectId and DestinationList fetched | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L273` |
| {MethodName} Fetching Transfer Channel Id for Transfer Name: {TransferName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L525` |
| Error in {MethodName} with param {TransferChannelName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L552` |
| Data did not save Successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L576` |

## RepPacketCreation

Logger templates in RepPacketCreation. Keywords: RepPacketCreation log, error.

| Message template | Source |
|---|---|
| {MethodName} \| Request is null | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L205` |
| {MethodName} \| BasePath is null or empty | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L211` |
| {MethodName} \| ChannelId or TableSettingsId is zero | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L217` |
| {MethodName} \| VesselGroups is null or empty | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L223` |
| {MethodName} \| One or more VesselGroups have invalid VesselObjectId or VesselPacketDirectory | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L229` |
| {MethodName} \| One or more VesselGroups have non-existent VesselPacketDirectory | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L235` |
| {MethodName} \| One or more VesselGroups have null or empty TrackRecordDetails | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L241` |
| {MethodName} \| Error validating packet generation request | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L249` |
| Invalid path | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/FileChunkWriterStream.cs#L14` |
| Rep code value gotten is null  or empty | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L325` |
| Packet Name value gotten is null or empty | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L343` |
| {MethodName} - Error occurred while extracting zip file from {ZipPath} to {ExtractPath}. Message: {Message} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L52` |
| {MethodName} - Error occurred while generating packet for TableSettingsId: {TableSettingsId}, ChannelId: {ChannelId} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L118` |
| {MethodName} - Failed to rename packet file from {OldFileName} to {NewFileName} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L213` |
| Failed to rename packet file from {packetName} to {correctPacketName} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L214` |
| {MethodName} - Error occurred while generating packet for VesselObjectId: {VesselObjectId}, PacketNameBase: {PacketNameBase} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L233` |
| {MethodName} - Failed to save packet header for VesselObjectId: {VesselObjectId}, PacketName: {PacketName} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L292` |
| Failed to save packet header for VesselObjectId: {metaInfo.VesselObjectId}, PacketName: {correctPacketName} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L293` |
| {MethodName} - Error occurred while saving packet header for VesselObjectId: {VesselObjectId}, PacketName: {PacketName}, PacketLocation: {PacketLocation} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L304` |
| GetPacketName - Error occurred while generating packet name for RepCode: {RepCode}, ChannelId: {ChannelId} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L330` |
| {MethodName} - Creating Zstd packet for PacketName: {PacketName} from file list | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L340` |
| {MethodName} - Appending packet header for VesselObjectId: {VesselObjectId}, PacketCounter: {PacketCounter} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L357` |
| RenameFile \| New file already exists: {NewFilePath}. Deleting it before renaming. | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L403` |
| RenameFile \| Old file does not exist: {OldFileName} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L411` |
| RenameFile \| Error renaming file from {OldFileName} to {NewFileName} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L417` |
| [MESSAGEPACK COMPRESSION] Extracted tar.zst archive to {OutputFolder} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L450` |
| {MethodName} Files extracted error, extractPath: {ExtractPath}, Message:{Message} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L462` |
| Data did not save Successfully | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L462` |
| {MethodName} \| Error saving out packet HD \| PacketNo: {PacketNo}, PacketName: {PacketName}, FileSize: {FileSize} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketDapperRepository.cs#L53` |
| {MethodName} \| Error retrieving last out packet counter for VesselObjectId: {VesselObjectId} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketDapperRepository.cs#L76` |
| {MethodName} \| Error updating packet counter for VesselObjectId: {VesselObjectId} to NewCounter: {NewCounter} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketDapperRepository.cs#L98` |
| {MethodName} \| Error reading RepCode for VesselObjectId: {VesselObjectId} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketDapperRepository.cs#L120` |

## RepSbus

Logger templates in RepSbus. Keywords: RepSbus log, error.

| Message template | Source |
|---|---|
| WorkerService:StartAsync | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L35` |
| {MethodName}\| Stopping service | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L43` |
| {MethodName}\| stopped notification was not sent due to Office Queue name not being valid  | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L66` |
| {MethodName}\| stopped notification not sent this is already office XD | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L71` |
| {MethodName}\| Exception occured while stopping the service | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L77` |
| {MethodName}\| Starting Executioner | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L87` |
| {MethodName}\| Executioner cycle has been started | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L91` |
| {MethodName}\| Service bus listener is not running due to {ErrorMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L109` |
| {MethodName}\|Receiver is not processing, restarting | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L117` |
| {MethodName}\| Service bus listener is running, with status : {ReceiverStartMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L126` |
| {MethodName}\| Service is stopping, executioner cycle cancelled | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L136` |
| Exception in {MethodName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L141` |
| SbusService\|ExecuteAsync execution Ended | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L143` |
| ServiceConfigData is null or empty | `RepSbus/MariApps.PAL.Rep.Sbus.Service/ServiceBusDependencyInjection.cs#L38` |
| {MethodName}\| Initiating process | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L35` |
| {MethodName}\| Process status added to memory store witht status {AddStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L50` |
| {MethodName} - Error in initiating process | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L58` |
| {MethodName}\| service bus connection string and basic info is not found | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L76` |
| {MethodName}\| ServiceBus settings added to memory store | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L84` |
| Error in {MethodName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L94` |
| {MethodName}\| Queue name is not found | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L111` |
| {MethodName}\| Current Environment Queue V2V added to memory store | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L119` |
| {MethodName}\| Getting Local IP Address | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L138` |
| {MethodName}\| Local IP Address: {IpAddress} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L169` |
| {MethodName}\| Local IP Address not found | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L174` |
| {MethodName}\| Setting Current Machine Name: {MachineName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L185` |
| {MethodName}\| Reading ServiceBus Credential | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L216` |
| {MethodName}\| Service bus credentials not found for {KeyName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L227` |
| {MethodName}\| Service bus credentials found for {KeyName} and returning | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L232` |
| Error in {MethodName}\| credentials not fetched | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L242` |
| {MethodName}\| Reading Current Queue Name | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L251` |
| {MethodName}\| Queue name not found found in config | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L261` |
| {MethodName}\| Queue name not found in memory store for V2V data for Key {KeyName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L266` |
| {MethodName}\| Queue name found for {KeyName} and returning | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L271` |
| {MethodName}\| Queue name {QueueName} found and returning | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L275` |
| Error in {MethodName}\| Queue name not fetched | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L284` |
| {MethodName}\| Reading CommonSettingsSbus | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L293` |
| {MethodName}\| CommonSettingsSbus not found for {KeyName}, retrying | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L300` |
| {MethodName}\| CommonSettingsSbus not found for {KeyName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L306` |
| {MethodName}\| CommonSettingsSbus found for {KeyName} and returning | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L315` |
| Error in {MethodName}\| CommonSettingsSbus not fetched | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L325` |
| {MethodName}\| Machine Name not found in memory | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L342` |
| {MethodName}\| Machine Name read from memory with name {MachineName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L346` |
| {MethodName}\| Local IP Address not found in memory | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L368` |
| {MethodName}\| Local IP Address read from memory with IP {IpAddress} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L372` |
| {MethodName}\|Starting listener | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L67` |
| {MethodName}\| Internet not available | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L73` |
| {MethodName}\| Service is not ready to start listener due Service Intital Status being {ServiceStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L86` |
| {MethodName}\| Service Bus Access failed with error {Error} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L101` |
| {MethodName}\|Listener is already running | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L114` |
| {MethodName}\| Receiver was not running, restarted it with status {ReceiverStartStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L131` |
| {MethodName}\| Receiver started notification has been sent with status {NotificationStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L144` |
| {MethodName}\| Receiver start failed with status {ReceiverStartStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L155` |
| {MethodName}\|Exception while starting listener | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L171` |
| {MethodName}\|Starting receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L185` |
| Queue name is empty | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L193` |
| Service bus credential is empty | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L196` |
| {MethodName}\| Going to listen to queue {QueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L198` |
| {MethodName}\| Queue {QueueName} is not active or created, creating it | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L202` |
| {MethodName}\| Queue creation failed for {QueueName} with error {Error} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L208` |
| {MethodName}\| Queue {QueueName} created successfully | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L218` |
| {MethodName}\|Service Bus client intitialised | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L225` |
| {MethodName}\|Exception while starting receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L240` |
| {MethodName}\|Receiver started with status {ReceiverStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L245` |
| {MethodName}\| Queue does not exists : {QueueName}, creating it | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L265` |
| {MethodName}\|Queue {QueueName} was successfully Created with status {Status} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L275` |
| {MethodName}\| Queue creation failed : {QueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L293` |
| {MethodName}\| Stopping receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L310` |
| {MethodName}\| Stopping Receiver Queue Name: {QueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L315` |
| {MethodName}\| Stopped receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L321` |
| {MethodName} exception while stopping | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L325` |
| {MethodName}\|Restarting receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L343` |
| {MethodName}\|Receiver stopped successfully | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L348` |
| {MethodName}\|Receiver starterd successfully | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L352` |
| {MethodName}\|Receiver start failed {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L355` |
| {MethodName}\|Receiver stop failed, {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L365` |
| {MethodName}\|Restarted receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L373` |
| {MethodName}\| Error while restarting | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L387` |
| {MethodName}\|Getting receiver status | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L400` |
| {MethodName}\|Processor status: {IsProcessing}, closed status: {IsClosed} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L416` |
| {MethodName}\|Receiver status: {ReceiverStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L455` |
| {MethodName}\| Verifying Service Bus Access | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L462` |
| {MethodName}\| Queue {QueueName} is already active | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L476` |
| {MethodName}\| Error while verifying Service Bus Access | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L489` |
| {MethodName}\|Stopping receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L497` |
| {MethodName}\|Processor is null | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L502` |
| {MethodName}\| messageHandlerCount- {MessgaeHandler}\| errorHandler - {ErrorHandler} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L520` |
| {MethodName}\|Processor is not processing | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L526` |
| {MethodName}\|Stopped receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L529` |
| {MethodName}\|Error stopping receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L533` |
| {MethodName} Error while setting ErrorHandler event. | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L555` |
| Failed to initialize ErrorHandler. | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L556` |
| {MethodName} Error while setting MessageHandler event. | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L570` |
| Failed to initialize MessageHandler. | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L571` |
| One or more handlers could not be initialized. | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L576` |
| {MethodName}\| ServiceBus Listener is already running for Queue {QueueName}, listener not initalised again | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L588` |
| {MethodName}Initialising receiver \|queueName:{QueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L593` |
| {MethodName}\| Listener has been started for Queue {QueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L610` |
| {MethodName}\|Service bus message process exception, removing message and error handler | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L615` |
| {MethodName}\|Exception | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L624` |
| {MethodName}\| Received a  message: SequenceNumber:{SequenceNumber}, Reply To Address:{ReplyTo}, Subject {Subject}, Delivery Count {DeliveryCount} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L655` |
| {MethodName}\| Common Settings are not set, Config that were checked Location:{Location}, send Queeu Name:{SendQueueName}, Vessel Object ID : {VesselId} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L663` |
| Common settings are not set | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L665` |
| {MethodName}\| Invalid Json gotten as Message {Body} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L672` |
| {MethodName}\| Invalid Json gotten as Message {Body}\| Removing from queue | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L692` |
| {MethodName}\| Packet transfer data gotten sending acknowledgement File:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L712` |
| {MethodName}\| Processing Packet Transfer data for File:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L729` |
| {MethodName}\| Packet Transfer data saved for File:{FileName} with Message: {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L736` |
| {MethodName}\| Packet Transfer data save failed for File:{FileName} with Message: {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L759` |
| {MethodName}\| Acknowledgment Data gotten for VesselObjectId:{VesselObjectId} \| File:{FileName} \| Status:{Status} \| Message:{StatusMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L785` |
| {MethodName}\| Service info gotten as notificaiton {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L798` |
| {MethodName}\| General Notification gotten {Messgae} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L806` |
| {MethodName}\| {NotificationType} v2v packet transfer data gotten sending acknowledgement File:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L812` |
| {MethodName}\| Notification ackowledgement sent for File:{FileName} \| with status {Status} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L831` |
| {MethodName}\|Notification sent to office with Status:{Status} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L837` |
| {MethodName}\| Processing  V2V Packet Transfer data for File:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L840` |
| {MethodName}\| V2V Packet Transfer data saved for File:{FileName} with Message: {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L846` |
| {MethodName}\| V2V Packet Transfer data save failed for File:{FileName} with Message: {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L879` |
| {MethodName}\| Acnknowledgement got for Type {NotificationType}\| with statusMessage :{Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L899` |
| {MethodName}\| Acknowledgement saved status {Saved} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L902` |
| {MethodName}\| V2V Send Acknowledgement got for Type {NotificationType}\| with statusMessage :{Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L907` |
| {MethodName}\|MISSING_PACKET_STATUS save completed  | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L920` |
| {MethodName}\|MISSING_PACKET_STATUS save failed with input {Input} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L928` |
| {MethodName}\| {NotificationType} data gotten | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L936` |
| {MethodName}\| Chat data saved, invoking queue | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L941` |
| {MethodName}\| Chat data saved, invoking api completed with status {RequestStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L968` |
| {MethodName}Saving to chat Queue Failed | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L972` |
| {MethodName}\| General data saved successfully | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L984` |
| {MethodName}\| General data save failed with error: {ErrorMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L989` |
| {MethodName}\| Failed to deserialize ScriptExecutionRequestEnvelope from message body | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1005` |
| {MethodName}\| JSON deserialization error for ScriptExecutionRequestEnvelope: {ErrorMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1011` |
| {MethodName}\| Initiating Script execution | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1015` |
| {MethodName}\| Script execution returned null result for RequestId: {RequestId} \| CorrelationID: {CorrelationID} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1019` |
| {MethodName}\| Script execution reply sent failed for RequestId: {RequestId} \| CorrelationID: {CorrelationID} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1028` |
| {MethodName}\| Script execution reply sent successfully for RequestId: {RequestId} \| CorrelationID: {CorrelationID} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1032` |
| {MethodName}\| Failed to deserialize TroubleshootRunRequestEnvelope from message body | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1045` |
| {MethodName}\| JSON deserialization error for TroubleshootRunRequestEnvelope: {ErrorMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1051` |
| {MethodName}\| Troubleshoot run request expired at {ExpiresAtUtc} \| CorrelationID: {CorrelationID} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1058` |
| {MethodName}\| Triggering troubleshoot run \| CorrelationID: {CorrelationID} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1064` |
| {MethodName}\| Troubleshoot run reply sent failed ({Status}) for RequestId: {RequestId} \| CorrelationID: {CorrelationID} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1073` |
| {MethodName}\| Troubleshoot run reply ({Status}) sent successfully for RequestId: {RequestId} \| CorrelationID: {CorrelationID} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1077` |
| {MethodName}\| {NotificationType} gotten is invalid | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1082` |
| {MethodName}\| Invoking process after receiving message | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1087` |
| {MethodName}\| Operation timeout occurred - message processing took too long | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1098` |
| {MethodName}\| Transient service bus error occurred - message will be retried | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1105` |
| {MethodName}\| Exception in message processing | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1112` |
| {MethodName}\| Failed to abandon message after error | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1122` |
| {MethodName}\| Message completion failed - lock already lost (message likely processed by another receiver or lock expired) | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1202` |
| {MethodName}\| Message completion failed - message not found (already removed from queue) | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1207` |
| {MethodName}\| Message completion failed due to transient error - will retry | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1212` |
| {MethodName}\| Message completion failed with unexpected error | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1217` |
| {MethodName}\| Message abandon failed - lock already lost (message likely processed by another receiver or lock expired) | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1232` |
| {MethodName}\| Message abandon failed - message not found (already removed from queue) | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1237` |
| {MethodName}\| Message abandon failed due to transient error - will not retry | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1242` |
| {MethodName}\| Message abandon failed with unexpected error | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1247` |
| Failed Message Handler | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1262` |
| {MethodName}\| Transient error occurred - retrying ({Attempt}/{MaxRetries}) after {DelayMs}ms | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1284` |
| {MethodName}\| Operation {OperationName} failed after {Attempts} attempts | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1290` |
| {MethodName}\| Transient Service Bus error, processor will retry\| Reason:{Reason}\| Source:{ErrorSource}\| Entity:{EntityPath}\| Message:{Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1344` |
| {MethodName}\|Number of Error Notification has exceeded daily limit. Skipping Notification | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1356` |
| {MethodName}\| Error Notification sent to {QueueName} with message {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1379` |
| Notification ErrorHandler | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1383` |
| {MethodName}\| Invoking download api, Download current status:{Count}, time:{LastCallTime}  | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1391` |
| {MethodName}\|Calling Download API, current count:{Count} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1396` |
| {MethodName}\|Download has been called successfully | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1403` |
| {MethodName}\|Download has been failed with error message {ErrorMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1407` |
| {MethodName}\|Download has been queued | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1414` |
| {MethodName}\| Handling Packet Transfer Message | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1425` |
| {MethodName}\| Packet transfer file download data saved successfully with message:{Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1477` |
| {MethodName}\| Packet transfer download failed with message: {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1486` |
| {MethodName}\| API Exception Packet Transfer download failed DblogW save api not being available | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1489` |
| {MethodName}\| Error in handling packet transfer message | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1502` |
| {MethodName}\| Handling V2V Packet Transfer Message | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1519` |
| {MethodName}\| V2V Packet transfer file download data saved successfully with message:{Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1575` |
| {MethodName}\| V2V Packet transfer download failed with message: {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1584` |
| {MethodName}\| API Exception Packet Transfer V2V download failed to DblogW save api not being available | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1588` |
| {MethodName}\| {Operation} {Status} for File:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1637` |
| {MethodName}\| Status {Event} for transfer {TransferId} not saved: {Error} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1693` |
| {MethodName}\| Could not save bulk transfer status for File:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1697` |
| {MethodName}\| Sending Notification to Queue:{QueueName} \| FileName:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1705` |
| {MethodName}\| Notification has been sent with Status : {ResponseStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1718` |
| {MethodName}\| Notification has been saved in DB with status {Status} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1723` |
| {MethodName}\| {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1730` |
| {MethodName}\| Failed to send Notification to Queue:{QueueName} \| FileName:{FileName} \| Error:{Error} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1737` |
| {MethodName}\| Sending message to queue:{QueueName} \| FileName:{FileName}\| for process {ProcessName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1773` |
| {MethodName} Notification has been sent Successfully with Status  {ResponseStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1796` |
| {MethodName} sending to {Queue} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1803` |
| {MethodName} sending to troubleshoot queue | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1820` |
| {MethodName}\| Sending Notification to Queue:{QueueName}  | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1834` |
| {MethodName}\| Sending Notification to Queue:{QueueName} \| FileName:{FileName} \| Notification Type :{NotificationType}\| Packet Counter {PcktCounter} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1869` |
| {MethodName}\| Failed to send Notification to Queue:{QueueName} \| FileName:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1882` |
| {MethodName}\| Start | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1894` |
| {MethodName}\| Acquisition service API url are not available | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1901` |
| {MethodName}\| Acquisition REP_INTERGRATION_BASE_URL parameter value is empty | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1906` |
| {MethodName}\| Acquisition REP_INTERGRATION_API_URL parameter value is empty | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1912` |
| {MethodName}\| Invoking Integration Service Call with Status : {Status} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1926` |
| {MethodName}\| Exception | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1930` |
| {MethodName}\| Starting to sending a notfication | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1937` |
| {MethodName}\| ServiceBusClient is not initialized, initializing again | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1949` |
| {MethodName}\| The message body size is too large {Length} to fit in the message batch | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1971` |
| {MethodName}\| Failed to send message to the queue {DestinationQueue} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1983` |
| {MethodName}\| Notification has been sent successfully | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1997` |
| {MethodName}\| Processor has been restarted for Queue | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L2056` |
| {MethodName}\| Error while restarting processor. | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L2060` |
| {MethodName}\|checking network | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonOperation.cs#L24` |
| {MethodName}\|network status: {NetworkStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonOperation.cs#L41` |
| {MethodName}\| Validating directory {Dir} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonOperation.cs#L69` |
| {MethodName}\| Directory path is null or empty | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonOperation.cs#L75` |
| {MethodName}\| Directory does not exists creating it {Dir} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonOperation.cs#L81` |
| {MethodName}\| Unauthorized access to directory {Dir}\| Service does not have permission | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonOperation.cs#L90` |
| {MethodName}\| Error occured while validating directory {Dir} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonOperation.cs#L95` |
| {MethodName}\| Starting to Process | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L42` |
| {MethodName}\| Service configuration status is false, retrying initialization | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L59` |
| {MethodName}\| Service Configuration is not proper | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L65` |
| {MethodName}\| Service Configuration value is not proper | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L77` |
| {MethodName}\| ServiceBus ConnectionString is not proper | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L88` |
| {MethodName}\| Queue names could not be found for destination and source | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L123` |
| {MethodName}\| Source Queue name could not be found | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L132` |
| {MethodName}\| Destination Queue name could not be found | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L141` |
| {MethodName}\| Office Queue name could not be found | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L150` |
| {MethodName}\| Processing V2V data | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L193` |
| {MethodName}\| Finished | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L201` |
| {MethodName}\| Out packet source Id :{SourceId} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L259` |
| {MethodName}\| Message sending failed :{ErrorMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L269` |
| {MethodName}\| Notification sent successfully | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L346` |
| {MethodName}\| Exception Occured | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L359` |
| {MethodName}\| Finished Processing | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L361` |
| {MethodName}\| Sending message to queue :{QueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L446` |
| {MethodName}\| Finished sending all messages | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L461` |
| {MethodName}\| Moving file to SENT folder :{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L537` |
| {MethodName}\| File moved to SENT folder :{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L560` |
| {MethodName}\| Remote troubleshoot runs are disabled (TroubleshootRunSettings:Enabled=false) | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/TroubleshootLauncher.cs#L44` |
| {MethodName}\| Troubleshoot executable not found at '{Path}' | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/TroubleshootLauncher.cs#L52` |
| {MethodName}\| Starting {Path} --remote-run{StopSwitch} RunId={RunId} CorrelationId={CorrelationId} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/TroubleshootLauncher.cs#L81` |
| {MethodName}\| No acknowledgement within {Seconds}s | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/TroubleshootLauncher.cs#L163` |
| {MethodName}\| Acknowledged {Status} RunId={RunId} Pid={Pid} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/TroubleshootLauncher.cs#L169` |
| {MethodName}\| Troubleshoot exited with code {ExitCode} before acknowledging | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/TroubleshootLauncher.cs#L180` |
| {MethodName}\| No acknowledgement within {Seconds}s; leaving process {Pid} running | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/TroubleshootLauncher.cs#L188` |
| {MethodName}\| Failed to start the troubleshoot process | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/TroubleshootLauncher.cs#L197` |
| {MethodName}\|Sending Notification to {QueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/Controllers/SbusSendController.cs#L36` |
| {MethodName}\| Started | `RepSbus/MariApps.PAL.Rep.Sbus.Service/Controllers/SbusSendController.cs#L45` |
| {MethodName}\| Started for File:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/Controllers/SbusSendController.cs#L58` |
| TestService:Started | `RepSbus/MariApps.PAL.Rep.Sbus.Service/Controllers/SbusSendController.cs#L133` |
| SbuSendController\|ReadStaticVariable\|Current Download Count {0}, Last Download time:{1} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/Controllers/SbusSendController.cs#L149` |
| Exception in ServiceBusSL.IntiateDownloadQueue | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/AzureSl.cs#L55` |
| Exception in {MethodName} with input {Json} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/DblogWSL.cs#L97` |
| Exception in {MethodName} for transfer {TransferId} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/DblogWSL.cs#L126` |
| {MethodName}\| Started saving with input {Json} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/DblogWSL.cs#L134` |
| Exception in {MethodName}\| Message: {Body} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/IntegrationSL.cs#L61` |
| {methodName} : The request jsonBody is invalid or empty hence skipping the remaining processing | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/IntegrationSL.cs#L107` |
| Exception in {MethodName}\| ScriptExecutionResult : {CorrelationId} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/IntegrationSL.cs#L162` |
| {MethodName}\|Posting data to {ApiAddress} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ExternalInvokerClient.cs#L30` |
| {MethodName}\|Data post to Api {ApiAddress} completed with status Code {ResponseStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ExternalInvokerClient.cs#L49` |

## RepSplit

Logger templates in RepSplit. Keywords: RepSplit log, error.

| Message template | Source |
|---|---|
| The Directory  value of OutzipVslPathMain gotten is null or empty | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L42` |

## RepTransfer

Logger templates in RepTransfer. Keywords: RepTransfer log, error.

| Message template | Source |
|---|---|
| Exception in {MethodName} when finding file {FileName} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/CommonMethodBL.cs#L253` |
| Source Client is mandatory | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/ValidateInputBL.cs#L244` |
| Vessel Object Id is mandatory | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/ValidateInputBL.cs#L247` |
| Split Files is mandatory | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/ValidateInputBL.cs#L250` |
| File Location or File Name is mandatory | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/ValidateInputBL.cs#L253` |
| One or more split files do not exist at the specified location | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/ValidateInputBL.cs#L256` |
| {MethodName}\| Validation successful  | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/ValidateInputBL.cs#L326` |
| {MethodName}\| Error occurred while validating priority transfer | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/ValidateInputBL.cs#L337` |
| Transfer Medium folder details gotten is Null or Empty | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferPacketExtBL.cs#L110` |
| Error while moving split file to OUTBOX Folder | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferPacketExtBL.cs#L153` |
| Transfer Medium folder details gotten is Null or Empty OR does not exists | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferPacketExtBL.cs#L467` |
| Transfer Type not found for VesselObjectId:  | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferPacketExtBL.cs#L704` |
| Error in Split Files count | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferPacketExtBL.cs#L732` |
| {MethodName}\| Transfer directory is empty for transferType {TransferType}, vessel {VesselObjectId} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferHandler.cs#L58` |
| {MethodName}\| Unknown transfer type {TransferType} for vessel {VesselObjectId} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferHandler.cs#L116` |
| {MethodName}\| Error occurred while handling priority transfer | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferHandler.cs#L149` |
| {MethodName}\| Error occurred while fetching vessel transfer type | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferHandler.cs#L190` |
| {MethodName}\| Error occurred while fetching vessel transfer location | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferHandler.cs#L224` |
| {MethodName}\| Process started | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L35` |
| {MethodName}\| transferMediumBaseFolder is null or empty for transfer type: {TransferType} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L76` |
| {MethodName}\| Transfer Move failed for some records. Setting status to FAILED for table Settings Id - {TableIdList} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L217` |
| {MethodName}\| Process completed successfully {Message} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L224` |
| Exception occured while transferring {MethodName} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L235` |
| {MethodName}\|Processing VesselObjectId: {VesselObjectId} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L262` |
| {MethodName}\|Transfer Type: {TransferType} for vessel {VesselObjectId} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L266` |
| {MethodName}\| File is not a directory: {FileNameLocation} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L287` |
| {MethodName}\|Processing transfer type: {TransferType} for vessel {VesselObjectId} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L387` |
| {MethodName}\| Process completed successfully with status: {Status} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L408` |
| {MethodName}\| Exception occurred while moving file folder | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L419` |
| {MethodName}\| File not found in any folder \| FileName: {FileName} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L573` |
| {MethodName}\| Preparing TransferBO with resend data | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L627` |
| {MethodName}\| No resend data found | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L636` |
| {MethodName}\| Processing complete | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L642` |
| Exception in {MethodName} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L651` |
| {MethodName}\| Error occurred while reading transfer information | `RepTransfer/MariApps.PAL.Rep.Transfer.DAL/TransferDapperRepository.cs#L43` |
| {MethodName}\| Error occurred while reading transfer type | `RepTransfer/MariApps.PAL.Rep.Transfer.DAL/TransferDapperRepository.cs#L68` |

