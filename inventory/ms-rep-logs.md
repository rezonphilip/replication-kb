---
doc_id: INV-MSREP-LOGS
type: inventory
components: [ms-rep]
status: draft
author: claude
last_verified: 2026-11-11
---

# MS-REP log message catalogue

Every logger call and thrown exception found in MS-REP code, per service, with level and source line. Services are configured with Serilog minimum level Error, so only Error/Critical lines (and unhandled exceptions) reach the log file by default; Information, Debug and Warning lines appear only if the level is lowered. Keywords: log, error message, signature, Serilog, log level.

## RepAckn

Logger templates in RepAckn. Keywords: RepAckn log, error.

| Level | Message template | Source |
|---|---|---|
| Error | Error while executing method AcknRepository.GetAcknowledgementSettings | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/AcknRepository.cs#L78` |
| Information | SaveAcknowledgementStatus\| Saving data\|Status:{0},{1}  | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/AcknRepository.cs#L86` |
| Error | Error While executing SaveAcknowledgementStatus SP single\|ERROR MESSAGE: {ex.Message} | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/AcknRepository.cs#L144` |
| Error | Error While executing SaveAcknowledgementStatus SP bulk\|ERROR MESSAGE: {ex.Message} | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/AcknRepository.cs#L189` |
| Information | Save Response\| Saving data\|Status:{0},{1}  | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/AcknRepository.cs#L198` |
| Error | <msg)> | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/AcknRepository.cs#L262` |
| Error | <ex.Message)> | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/AcknRepository.cs#L281` |
| Information | <msg)> | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/AcknRepository.cs#L287` |
| Information | <ex.Message)> | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/AcknRepository.cs#L316` |
| Information | SaveV2VMIssingPacketTrackRecords, Could not find the table settings details REP.REP_ACKN_EXT_RECORD | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/AcknRepository.cs#L416` |
| Error | Error in AcquisitionRepository.SaveV2VMIssingPacketRecords | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/AcknRepository.cs#L470` |
| Throw:NotImplementedException | <)> | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/AcknRepository.cs#L520` |
| Debug | {MethodName}\| Saving acknowledgement status for VesselObjectId: {VesselObjectId}, TableSettingsId: {TableSettingsId} | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L44` |
| Debug | {MethodName}\| Successfully saved {Count} acknowledgement records | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L84` |
| Error | {MethodName}\| Error in SaveAcknowledgementStatus | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L89` |
| Error | Error in SaveAcknowledgementStatus: {ex.Message} | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L90` |
| Error | Error in SaveAcknowledgementStatusBulk: {ex.Message} | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L132` |
| Information | Save Response\| Saving data\|Status:{ackn.StatusCode},{ackn.FileName} | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L140` |
| Error | Error in SaveResponseStatus: {ex.Message} | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L183` |
| Error | {MethodName}\| {ErrorMessage} | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L192` |
| Error | {MethodName}\| Error in Error method | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L211` |
| Error | Error in Error method: {ex.Message} | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L212` |
| Information | {MethodName}\| {InfoMessage} | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L220` |
| Error | {MethodName}\| Error in Information method | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L239` |
| Information | Error in Information method: {ex.Message} | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L240` |
| Debug | {MethodName}\| Reading all Table Settings | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L250` |
| Debug | {MethodName}\| Found {Count} table settings | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L262` |
| Error | {MethodName}\| Error while reading table settings | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L271` |
| Debug | {MethodName}\| Reading Common CO Parameters values | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L311` |
| Debug | {MethodName}\| Read Common CO Parameters values | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L323` |
| Error | {MethodName} - Error in reading Common CO Parameters values | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L332` |
| Debug | {MethodName}\| Saving bulk acknowledgement data, Count: {Count} | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L485` |
| Warning | {MethodName}\| Truncated RESPONSE_MESSAGE for {Count} records to max length {MaxLength} before TVP save | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L514` |
| Debug | {MethodName}\| Successfully saved {Count} bulk acknowledgement records | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L532` |
| Error | {MethodName}\| Error in SaveAcknDataBulkd | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L537` |
| Error | Error in SaveAcknDataBulkd: {ex.Message} | `RepAckn/MariApps.PAL.Rep.Ackn.DAL/DapperAcknRepository.cs#L538` |
| Information | {MethodName}\| Starting Acknowledgement process for TableSettings Id {TableSetttingsId} for Packet Counter {PacketCounter} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L48` |
| Information | {MethodName}\| Processing for {FileLocation} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L63` |
| Debug | {MethodName}\| TableSettingsInfo is null for {FileLocation} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L67` |
| Error | {MethodName}\| Base URL or API URL is empty for Table Settings Id {TableSetttingsId} for Packet Counter {PacketCounter} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L104` |
| Information | {MethodName}\| Invoking external service for {FileLocation} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L151` |
| Debug | {MethodName}\| Response received for {FileLocation} with status code {StatusCode} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L154` |
| Information | {MethodName}\| Acknowledgement process completed successfully for {FileLocation} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L158` |
| Error | {MethodName}\| Acknowledgement process failed for {FileLocation} with error {ErrorMessage} - {HttpStatusCode} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L183` |
| Warning | {MethodName}\| All files failed for TableSettings Id {TableSetttingsId} for Packet Counter {PacketCounter} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L216` |
| Information | {MethodName}\| {Message} for TableSettings Id {TableSetttingsId} for Packet Counter {PacketCounter} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L237` |
| Information | {MethodName}\| Acknowledgement process completed successfully for TableSettings Id {TableSetttingsId} for Packet Counter {PacketCounter} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L250` |
| Critical | {MethodName}\| Exception occurred while processing Acknowledgement for TableSettings Id {TableSetttingsId} for Packet Counter {PacketCounter} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L259` |
| Information | INFO: ACKN_BL method, File \|FILE NAME:{item.FileLocation}FILE STATUS :{fileStatus} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L327` |
| Information | SUCCESS:File: {filename} \| Not used by any process | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L423` |
| Information | FAILED:The file is being used by another process\|File: {filename}\| ERROR MESSAGE: {ex.Message} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L427` |
| Information | PushToService, postbody: {0} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/AcknBL.cs#L485` |
| Error | {MethodName}\| Input is null | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L123` |
| Critical | {MethodName}\| ImportQId is 0 | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L133` |
| Critical | {MethodName}\| VesselObjectId is 0 | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L143` |
| Critical | {MethodName}\| TableSettingsId is 0 | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L153` |
| Critical | {MethodName}\| TableSettingsId is not valid | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L163` |
| Critical | {MethodName}\| PacketCounter is 0 | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L173` |
| Critical | {MethodName}\| SplitFiles is null or empty | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L183` |
| Error | {MethodName}\| FileLocation is null or file does not exist | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L193` |
| Information | {MethodName}\| Validation successful | `RepAckn/MariApps.PAL.Rep.Ackn.Service/BL/ValidateBL.cs#L203` |
| Debug | {MethodName}\| Process Started | `RepAckn/MariApps.PAL.Rep.Ackn.Service/Controllers/AcknController.cs#L78` |
| Error | {MethodName}\| Invalid Request | `RepAckn/MariApps.PAL.Rep.Ackn.Service/Controllers/AcknController.cs#L84` |
| Debug | {MethodName}\| Request completed with status :{Status} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/Controllers/AcknController.cs#L94` |
| Information | AcknController\|TestService\|Vessel | `RepAckn/MariApps.PAL.Rep.Ackn.Service/Controllers/AcknController.cs#L138` |
| Throw:ArgumentNullException | <nameof(httpClientFactory))> | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L29` |
| Throw:ArgumentNullException | <nameof(logger))> | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L30` |
| Throw:ArgumentNullException | <nameof(availableIds))> | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L31` |
| Debug | {MethodName}\| Checking if ID is available | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L43` |
| Debug | {MethodName}\| ID {Id} is available | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L49` |
| Warning | {MethodName}\| ID {Id} is not available in registered table settings | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L53` |
| Debug | {MethodName}\| Processing external invoke parameters | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L68` |
| Error | {MethodName}\| External invoke parameters cannot be null | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L77` |
| Throw:ArgumentNullException | <nameof(invokeParam))> | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L78` |
| Error | {MethodName}\| Table settings ID {Id} is not available | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L83` |
| Debug | {MethodName}\| Creating HTTP client for table settings ID {Id} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L90` |
| Debug | {MethodName}\| Sending POST request to {ApiAddress} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L103` |
| Information | {MethodName}\| POST request successful. Status: {StatusCode}, Response time: {ResponseTime}ms | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L117` |
| Warning | {MethodName}\| POST request failed. Status: {StatusCode}, Response: {Response} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L127` |
| Error | {MethodName}\| HTTP request exception occurred | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L141` |
| Error | {MethodName}\| Request timeout occurred | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L154` |
| Error | {MethodName}\| Unexpected error occurred | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L168` |
| Debug | {MethodName}\| Processing external invoke parameters for common destination | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L190` |
| Error | {MethodName}\| BaseUrl cannot be null or empty | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L205` |
| Debug | {MethodName}\| Creating common HTTP client | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L213` |
| Debug | {MethodName}\| Sending POST request to {BaseUrl}{ApiAddress} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L229` |
| Debug | {MethodName}\| Invoking external handler for TableSettingsId {Id} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L312` |
| Error | {MethodName}\| ExternalInvokeParam cannot be null | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L316` |
| Information | {MethodName}\| TableSettingsId {Id} is available, using ClientFactoryDestinationHandler | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L323` |
| Information | {MethodName}\| TableSettingsId {Id} is not available, using CommonDestinationHandler | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L328` |
| Debug | {MethodName}\| ExternalInvoker completed for TableSettingsId {Id} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/AcknPushHandlerSL.cs#L332` |
| Information | {MethodName}\|Posting data to {ApiAddress} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/ExternalSL.cs#L30` |
| Information | {MethodName}\|Data post to Api {ApiAddress} completed with status Code {ResponseStatus} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/ExternalSL.cs#L51` |
| Information | {MethodName}\|Response from Api {ApiAddress} completed with status Code {ResponseStatus} | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/ExternalSL.cs#L70` |
| Error | {MethodName}\|Exception | `RepAckn/MariApps.PAL.Rep.Ackn.Service/SL/ExternalSL.cs#L74` |

## RepAcquisition

Logger templates in RepAcquisition. Keywords: RepAcquisition log, error.

| Level | Message template | Source |
|---|---|---|
| Debug | {MethodName}\| Reading Common CO Parameters values | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L37` |
| Debug | {MethodName}\| Read Common CO Parameters values | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L48` |
| Error | {MethodName} - Error in reading Common CO Parameters values | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L57` |
| Debug | {MethodName}\| Reading Last in Packet Counter | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L68` |
| Debug | {MethodName}\| Read Last In Packet Counter {Value} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L89` |
| Error | {MethodName} Exception while reading last in packet counter | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L95` |
| Debug | {MethodName}\| Missing packet information could not be found for packet counter {PacketCounter} and vessel object id {VesselObjectId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L128` |
| Debug | {MethodName}\| Missing packet information found for packet counter {PacketCounter} and vessel object id {VesselObjectId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L132` |
| Error | {MethodName}\|Exception occured while reading missing packet data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L140` |
| Debug | {MethodName}\| Reading Error Missing Packets | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L150` |
| Error | {MethodName}\|Exception occured while reading error missing packet data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L175` |
| Debug | {MethodName}\| Reading Vessel rep Code | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L185` |
| Error | {MethodName}\|Exception occured while reading vessel rep code | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L210` |
| Debug | {MethodName}\| Reading trasnfer data for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L221` |
| Debug | {MethodName}\| Transfer data found for {Vessel} with transfer type {TransferType} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L236` |
| Error | {MethodName}\|Error occured while reading transfer data for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L242` |
| Debug | {MethodName}\| Reading trasnfer lcoation for {TransferID} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L255` |
| Debug | {MethodName}\| Transfer location found for {TransferID} with location {TransferLocation} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L267` |
| Error | {MethodName}\|Error occured while reading transfer location for {TransferID} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L273` |
| Debug | {MethodName}\| Reading V2V Current Vessel Transfer Type | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L282` |
| Debug | {MethodName}\| Read V2V Current Vessel Transfer Type {TransferType} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L292` |
| Debug | {MethodName}\| Reading all Vessels data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L301` |
| Error | {MethodName}\|Exception occured while reading vessels | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L322` |
| Debug | {MethodName}\| Reading Table Settings Id from Downloads for {FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L332` |
| Debug | {MethodName}\| Read Table Settings Id {TableSettingsId} for {FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L351` |
| Error | {MethodName}\| Exception while reading Table Settings Id from Downloads for {FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L357` |
| Information | {MethodName}\| Saving Import Packet Data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L367` |
| Information | {MethodName}\| Import Packet Data saved with InPacketHdId {InPacketHdId} and MissingPacketId {MissingPacketId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L392` |
| Error | {MethodName}\| Exception while saving Import Packet Data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L397` |
| Information | {MethodName}\| Import bulk Packet Data saved | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L428` |
| Information | {MethodName}\| Updating Vessel {VesselId} In Packet Counter {PacketCounter} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L444` |
| Debug | {MethodName}\| Updated Vessel {Vessel} with In Packet Counter {PacketCounter} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L458` |
| Error | {MethodName}\| Exception while updating Vessel In Packet Counter | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L462` |
| Information | {MethodName}\| Reading all Table Settings | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L470` |
| Debug | {MethodName} Reading packet download information  | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L493` |
| Debug | {MethodName}\| Reading Channel Details | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L513` |
| Information | {MethodName}\| Saving V2V Import Packet Data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L532` |
| Information | {MethodName}\| Import V2V Packet Data saved with InPacketHdId {InPacketHdId} and MissingPacketId {MissingPacketId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L566` |
| Debug | {MethodName}\| Reading V2V Packet Counter Settings for Channel {ChannelId}, for source {SourceId} to Destination {DestinatinId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L580` |
| Debug | {MethodName}\| Read V2V Packet Counter {PacketCounter} for Channel {ChannelId}, for source {SourceId} to Destination {DestinatinId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L606` |
| Error | {MethodName}\| Exception while reading V2V Packet Counter Settings for Channel {ChannelId}, for source {SourceId} to Destination {DestinatinId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L612` |
| Debug | {MethodName}\| Update V2V Packet Counter with new Counter {Counter} for Channel {ChannelId}, for source {SourceId} to Destination {DestinatinId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L621` |
| Debug | {MethodName}\| Updated V2V Packet Counter with new Counter {Counter} for Channel {ChannelId}, for source {SourceId} to Destination {DestinatinId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L648` |
| Critical | {MethodName}\| Exception while updating V2V Packet Counter with new Counter {Counter} for Channel {ChannelId}, for source {SourceId} to Destination {DestinatinId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L654` |
| Debug | {MethodName}\| Reading Missing Packet Status for Source {SourceId} to Destination {DestinatinId} with Packet Counter {PacketCounter} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L665` |
| Debug | {MethodName}\| Read Missing Packet Status for Source {SourceId} to Destination {DestinatinId} with Packet Counter {PacketCounter} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L685` |
| Debug | {MethodName}\| Reading Missing Packet Details for Vessel {VesselId} at location {MissingAt} for communication Type {CommType} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L695` |
| Debug | {MethodName}\| Saving Import Packet Data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L719` |
| Debug | {MethodName}\| Import Packet Data saved | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L751` |
| Error | Exception while saving packet data {MethodName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L757` |
| Debug | {MethodName}\| Saving Import Queue Data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L766` |
| Information | {MethodName}\| Import Queue Data saved | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L791` |
| Error | {MethodName}\| Error while saving Import Queue Data\| Message:{Message} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L801` |
| Error | Exception occured while saving data in {MethodName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L812` |
| Debug | {MethodName}\| Updating Import Queue sub items | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L827` |
| Information | {MethodName}\| Import Queue sub details Data updated successfully | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L851` |
| Error | {MethodName}\| Error while saving updating import Queue sub details  Data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L861` |
| Error | {MethodName}\| Error in updating Import Queue sub details  data Items | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L872` |
| Debug | {MethodName}\| Updating Import Queue data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L888` |
| Information | {MethodName}\| Import Queue Data updated successfully | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L915` |
| Error | {MethodName}\| Error while saving updating import Queue Data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L925` |
| Error | {MethodName}\| Error in updating Import Queue data Items | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionNewRepository.cs#L936` |
| Error | Error in AcquisitionRepository.GetVesselCode | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L297` |
| Error | Error in AcquisitionRepository.GetCurrentEnvironmentDetails | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L505` |
| Error | Error in AcquisitionRepository.GetDownloadPacketDetails | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L550` |
| Error | Error in AcquisitionRepository.GetCurrentVesselId | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L574` |
| Error | Error in AcquisitionRepository.ReadChannelDetails | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L599` |
| Throw:DataException | Data did not save Successfully | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L632` |
| Error | Error in AcquisitionRepository.SaveV2VPacketDetails | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L642` |
| Error | Error in AcquisitionRepository.ReadPacketCounterSettings | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L670` |
| Error | Error in AcquisitionRepository.UpdatePacketCounterSettings | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L698` |
| Error | Error in AcquisitionRepository.ReadMissingPacketStatus | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L727` |
| Error | Error in AcquisitionRepository.SaveV2VMIssingPacketRecords | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L791` |
| Error | Error in AcquisitionRepository.GetMissingPacketList | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L816` |
| Error | Error in AcquisitionRepository.PacketSavedDatas | `RepAcquisition/MariApps.PAL.Rep.Acquisition.DAL/AcquisitionRepository.cs#L857` |
| Information | {MethodName}\| Starting Process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L60` |
| Warning | {MethodName}\| ImportVesselIds contains 0\|Import will not proceed | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L71` |
| Error | {MethodName}\| Inbox Directory not found | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L89` |
| Error | {MethodName}\| isVessel value could not be found | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L95` |
| Error | {MethodName}\| Missing Packet Table Info not found\| Intitialising it to 0 | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L101` |
| Critical | {MethodName}\| No active vessel found, exiting | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L108` |
| Information | {MethodName}\| Started processing for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L122` |
| Critical | {MethodName}\| Inbox Location {InboxDirectory} or Replication Code {RepCode} not found for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L132` |
| Debug | {MethodName} \| Step 1: Initialized parameters for vessel {VesselId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L135` |
| Error | {MethodName} \| Step 1: generalChannelId is null. ChannelKey: {ChannelKey}, VesselId: {VesselId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L139` |
| Debug | {MethodName} \| Step 2: Parameter object created for vessel {VesselId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L155` |
| Debug | {MethodName} \| Step 3: Directories created for vessel {VesselId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L163` |
| Debug | {MethodName} \| Step 4: Starting AcquisitionWorker for vessel {VesselId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L167` |
| Debug | {MethodName} \| Step 5: Parallelism control applied. Active Tasks: {TaskCount} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L173` |
| Debug | {MethodName} \| Step 5: Task added. Current parallel count: {TaskCount} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L178` |
| Information | {MethodName}\| Process Completed | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L185` |
| Critical | An exception occured in {MethodName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L189` |
| Information | {MethodName}\| Starting worker for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L199` |
| Information | {MethodName}\|No Pending Files available for vessel | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L220` |
| Information | {MethodName}\| No valid files found for {Vessel} at location {SourceLocation} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L234` |
| Information | {MethodName}\| Worker Completed for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L256` |
| Critical | A critical Exception occured while processing import data in {MethodName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L260` |
| Debug | {MethodName}\| Validating files for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L281` |
| Debug | {MethodName}\| Validating file {FileName} for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L295` |
| Debug | {MethodName}\| File {FileNameWithoutExtension} Already exists adding it as split | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L321` |
| Error | {MethodName}\| File {FileName} is locked, skipping now | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L385` |
| Error | {MethodName}\| Error while validating files for {Vessel}\| Error: {ErrorMessage} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L397` |
| Debug | {MethodName}\| Processing file {FileName} for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L414` |
| Critical | {MethodName}\| Last Packet Counter for {Vessel} is not found | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L420` |
| Debug | {MethodName}\| Last Packet Counter for {Vessel} is {LastInPacketCounter} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L424` |
| Error | {MethodName}\| Packet Name {FileName} is not of a valid naming format for {Vessel}\| Moving to errorn folder | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L454` |
| Error | {MethodName}\| Error while moving failed packet to error folder {FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L459` |
| Information | {MethodName}\| Packet {FileName} is waiting for previous packet to be processed for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L489` |
| Information | {MethodName}\| File {FileName} gotten is valid for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L525` |
| Information | {MethodName}\| Saved Import item for {Count} files | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L611` |
| Error | {MethodName}\| An exception occured while saving Import Queue Items for {Vessel}\| Stopping the processing for this vessel | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L617` |
| Information | {MethodName}\| Packet {FileName} is already processed and being skipped for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L625` |
| Debug | {MethodName}\| Skipped file has been moved to All Zip Folder | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L629` |
| Error | {MethodName}\| Packet {FileName} is not valid for {Vessel}\| Moving to error folder | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L679` |
| Debug | {MethodName}\| Error file has been moved to Error Folder with Status {ErrorMoveStatus} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L683` |
| Warning | {MethodName}\| Not all split file is available for file {FileName} for {Vessel}\| Skipping this file | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L699` |
| Debug | {MethodName}\| Saving Remainning items to Database for Import Process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L708` |
| Information | {MethodName}\| Process Completed for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L725` |
| Debug | {MethodName}\| Saving Priority Import packet Items count {Count} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L740` |
| Error | {MethodName}\| Error while saving Import Packet Data, result gotten is empty or null | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L746` |
| Throw:InvalidOperationException | Error while saving Import Packet Data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L747` |
| Information | {MethodName}\| Saving Last Vessle {Vessel} Received In packet counter with {LastInPacketCounter} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L749` |
| Debug | {MethodName}\| Moving ile {FileName} to Work Folder | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L793` |
| Debug | {MethodName}\| Saving Priority Import Queue Items count {Count} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L812` |
| Error | {MethodName}\| Exception while saving Import Queue Data\| Message : {ExMessage} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L817` |
| Debug | {MethodName}\| Priority Import Queue Data saved successfully | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L819` |
| Error | Exception occured in {MethodName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L830` |
| Information | {MethodName}\| Starting file acquisition process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L840` |
| Information | {MethodName}\| Import Vessel Ids contains -1, skipping all vessels for acquistion | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L854` |
| Warning | {MethodName}\| Work base directory not found | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L868` |
| Warning | {MethodName}\| isVessel value could not be found | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L880` |
| Warning | {MethodName}\| not Vessel Object Id data found | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L902` |
| Error | {MethodName}\| Transfer type value could not be gotten for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L926` |
| Error | {MethodName}\| Inbox folder location could not be gotten for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L937` |
| Error | {MethodName}\| No files found to import for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L987` |
| Debug | {MethodName}\| Processing error file {FileName} for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1052` |
| Debug | {MethodName}\| Moving file {FileName} from AllZip to Inbox for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1075` |
| Error | {MethodName}\| Error while moving error/pending file from all zip to inbox\|File name: {FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1116` |
| Error | {MethodName}\| Zip file does not exist in Allzip location or all splits might not be available for file {FileName} for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1123` |
| Error | Exception occured in {MethodName}\| while reading/processing error/missing packets | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1128` |
| Information | All available files status is not 0 | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1135` |
| Information | {MethodName}\| Missing packets have not been replicated for vessel {Vessel} so skipping its import as it is sequence import | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1180` |
| Information | {MethodName}\| {Count} priority packets processed for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1191` |
| Error | {MethodName}\| No valid packets found to import | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1196` |
| Information | {MethodName}\| Removing {Count} files from Acquisition Queue for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1199` |
| Information | {MethodName}\|{Message} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1208` |
| Warning | {MethodName}\| {Message} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1219` |
| Debug | {MethodName}\| File acquisition process completed with status {Status} and outPut: {Json} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1223` |
| Information | {MethodName}\| Import process completed for all vessels | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1226` |
| Error | {MethodName}\| General occured while processing import file | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1239` |
| Information | {MethodName}\| Processing priority packets for vessel {Vessel} with count {AcqCount} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1251` |
| Information | {MethodName}\| Read and Processing file -{FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1270` |
| Debug | {MethodName}\| File {FileName} is a split file | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1284` |
| Debug | {MethodName}\| File {FileName} is not a split file | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1293` |
| Error | {MethodName}\|Error while moving split packets to allzip\|FileName: {FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1435` |
| Information | {MethodName}\| Packet {PacketCounter} -  {FileName} skipped for vessel {Vessel} as it's already processed | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1475` |
| Error | {MethodName}\| Validation failed for file {File} Vessel {VesselObjectId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1481` |
| Error | {MethodName}\| Error while moving file {FileName} to error folder {Folder} for vessel {VesselObjectId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1487` |
| Information | {MethodName}\| Validation Successfull - {File}\| all split faile available and validated | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1493` |
| Debug | {MethodName}\| File {FileName} is valid and will be processed for channel {ChannelId} and table settings id {TableSettingsId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1521` |
| Warning | {MethodName}\| Not all split files are available for file {FileName} for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1557` |
| Information | {MethodName}\| Finished processing file {FileName} for vessel {VesselObjectId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1560` |
| Information | {MethodName}\| Processing import packet data for vessel {VesselObjectId} with count {ImportPacketCount} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1573` |
| Error | {MethodName}\| No record found in outputPacketList for packet with counter {PacketCounter} for vessel {VesselObjectId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1627` |
| Information | {MethodName}\| Updating Vessel Packet Counter for Vessel {VesselObjectId} with value {MaxPacketCounter} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1636` |
| Error | {MethodName}\| After saving import data in packet hd id and missing packet is not saved due to Update: {UpdatePacketCounter} packet counter gotten is {MaxPacketCounter} \| last in packet counter {UpdatedPktCtr} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1644` |
| Error | {MethodName}\| While importing after saving packet InpakcetHdId, missingPacketId {ImportData},  is null or empty | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1650` |
| Information | {MethodName}\| No import packet data found to save for vessel {VesselObjectId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1657` |
| Error | Exception in {MethodName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1668` |
| Information | {MethodName}\|Validating Packet Name | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1677` |
| Information | {MethodName}\|{File} has {Message} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1705` |
| Information | {MethodName}\| Validating Packet Counter for {FileName} with LastInPacketCounter {LastInPacketCounter} and VesselData {VesselData} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1715` |
| Debug | {MethodName}\| Packet Counter is {PacketCounter} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1721` |
| Error | {MethodName}\| Packet is missing another packet before it needs to be processed | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1730` |
| Information | {MethodName}\| Packet Counter is correct | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1740` |
| Error | {MethodName}\| packet counter {PacketCounter}, gotten is old | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1745` |
| Information | {MethodName}\| No missing packet info could be found against the packet\| Proceeding | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1751` |
| Information | {MethodName}\| {FileName} is having status {Status} so reprocessing | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1759` |
| Information | {MethodName}\| {FileName} is already processed | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1764` |
| Information | {MethodName}\| {FileName} status gotten is invalid or not available so reprocessing | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1769` |
| Information | {MethodName}\| Packet counter validation for file {FileName} completed with output {PacketType} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1775` |
| Error | {MethodName}\|Exception occured while validating File {FileName} with LastInPacketCounter {LastInPacketCounter} and VesselData {VesselData} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1781` |
| Information | {MethodName}\| Validating File {FileName} with params RepCode {RepCode}, Is Split {IsSplit}, Is Vessel {IsVessel}, LastInPktCTR {LastInPktCTR}, VesselData {VesselData} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1791` |
| Error | AcquisitionBl.VaidateZipFile \|MESSAGE: PACKET IS MISSING ANOTHER PACKET BEFORE IT NEEDS TO BE PROCESSED | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1840` |
| Information | AcquisitionBl.VaidateZipFile \|MESSAGE: PACKET COUNTER IS CORRECT | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1852` |
| Error | AcquisitionBl.VaidateZipFile MESSAGE: PACKET COUNTER IS NOT LATEST | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1858` |
| Error | AcquisitionBl.VaidateZipFile {PacketCounter}\| Vessel {vesselData.VesselObjectId} \|MESSAGE: PACKET ALREADY REACHED AND Reprocessing | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1865` |
| Error | EAcquisitionBl.VaidateZipFile{PacketCounter}\| Vessel {vesselData.VesselObjectId} \|MESSAGE: PACKET ALREADY REACHED AND PROCESSED | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1872` |
| Error | AcquisitionBl.VaidateZipFile {PacketCounter}\| Vessel {vesselData.VesselObjectId} \|MESSAGE: PACKET IS MISSING ANOTHER PACKET BEFORE IT NEEDS TO BE PROCESSED | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1883` |
| Information | AcquisitionBl.VaidateZipFile {PacketCounter}\| Vessel {vesselData.VesselObjectId} \|MESSAGE: PACKET IS PENDING TO BE PROCESSED.Processing now | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1893` |
| Information | AcquisitionBl.VaidateZipFile{PacketCounter}\| Vessel {vesselData.VesselObjectId} \|MESSAGE: PACKET IS PENDING TO BE PROCESSED. Processing  | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1900` |
| Error | AcquisitionBl.VaidateZipFile {PacketCounter}\| Vessel {vesselData.VesselObjectId} \|MESSAGE:No Packet counter packet need to be processed | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1908` |
| Information | END AcquisitionBl.VaidateZipFile  | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1914` |
| Error | AcquisitionBl.VaidateZipFile \|MESSAGE: ERROR WHILE VALIDATING FILE {ex.Message} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1923` |
| Information | {MethodName} \|Process  START | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1932` |
| Information | {MethodName}\| Started Missing packet process for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L1984` |
| Information | {MethodName}\| Processing missing packet {PacketCounter} for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2020` |
| Debug | {MethodName}\| Missing-packet placeholder {FileName} detected; skipping search | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2050` |
| Debug | {MethodName}\| Searching for base name {BaseName} in AllZipDirectory | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2055` |
| Debug | {MethodName}\| Not found in AllZipDirectory. Searching TempDirectory for {BaseName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2060` |
| Warning | {MethodName}\| Packet file {FileName} with Counter {PacketCounter} not found in AllZipDirectory or TempDirectory for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2066` |
| Debug | {MethodName}\| Found packet file {FileName} at {PacketLocation} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2071` |
| Information | {MethodName}\| Moved packet file {FileName} to {InboxDirectory} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2078` |
| Error | {MethodName}\| Failed to move packet file {FileName} to {InboxDirectory} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2082` |
| Error | {MethodName}\| Exception while moving packet file {FileName} to inbox | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2087` |
| Error | {MethodName} \|Exception processing Error and Missing Files | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2094` |
| Error | {MethodName}\| Configuration error: BasicSettings:ImportVesselIds is null or empty. Example: [-1] or [1001,1002]. | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionBL.cs#L2102` |
| Information | {MethodName}\| Starting to process Vessel to Vessel Priority Packets {Count} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L45` |
| Debug | {MethodName}\| Processing Vessel to Vessel packet  | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L56` |
| Debug | {MethodName}\| Reading vessel 2 vessel packet info from json for file {File}  | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L88` |
| Error | {MethodName}\| Packet related header data is not proper for File {File} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L108` |
| Warning | {MethodName}\| Packet Destination Information does not match current environment moving for File {FileName}, moving to error directory | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L116` |
| Critical | {MethodName}\| No validlast in packet counter could be gotten for Source Vessel {Souce} and Destination Vessel {Destination}\| skipping this file | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L145` |
| Debug | {MethodName}\| Packet {FileName} gotten is not latest and is missing some packet counter in between {LastInPacketCounter} and {CurrentCounter} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L173` |
| Debug | {MethodName}\| Missing Packet {FileName} data pushed to import queue with status : {SaveStatus} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L210` |
| Debug | {MethodName}\| Missing packet notification info save completed with status {Status} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L233` |
| Information | {MethodName}\| Packet counter {Counter} is latest for File {PacketName} with Source Unique Id {Source} and Destination Unique Id {Destination} for channel | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L237` |
| Error | {MethodName}\| {PacketName} Updating Vessel to Vessel Last In Packet Counter {Counter} failed for Channel {ChannelId} where souce is {Source} and destination is {Destination} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L261` |
| Debug | {MethodName}\| Updated Vessel to Vessel Last In Packet Counter {Counter} for Channel {ChannelId} where souce is {Source} and destination is {Destination} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L266` |
| Debug | {MethodName}\|Move status for file {FileName} is {Status} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L294` |
| Debug | {MethodName}\| Packet {FileName} data pushed to import queue with status : {SaveStatus} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L362` |
| Information | {MethodName}\| Vessel to Vessel Packet {PacketName} with Packet Counter {Counter} is successfully processed for Channel {ChannelId} where souce is {Source} and destination is {Destination} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L367` |
| Information | {MethodName}\| Packet counter {Counter} is already processed for File {PacketName} with Source Unique Id {Source} and Destination Unique Id {Destination} for channel {ChannelId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L373` |
| Debug | {MethodName}\| Skipped file has been moved to All Zip Folder with Status {MoveStatys} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L379` |
| Debug | {MethodName}\| Skipped Packet {FileName} data pushed to import queue with status : {SaveStatus} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L417` |
| Error | {MethodName}\| Packet {FileName}\| validation failed got invalid status {Status}, moving to error fodler | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L423` |
| Debug | {MethodName}\| Skipped file has been moved to All Zip Folder with status {Status} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L427` |
| Information | {MethodName}\| Finsihed processsing File {FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L440` |
| Warning | {MethodName}\| File {FileName} is not complete and is waiting for other splits, where Source {Source} And Destination {Destination} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L444` |
| Information | {MethodName}\| Finished processing {FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L447` |
| Information | {MethodName}\| Finished processing Vessel to Vessel Priority Packets {Count} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L450` |
| Critical | {MethodName}\| Error in processing Vessel to Vessel Priority Packets | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L454` |
| Information | Processing Vessel to Vessel Priority Packets\|Count : {V2VFiles.Count} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L465` |
| Throw:ArgumentNullException | Transfer Type gotten is null for current location from GetCurrentVesselTransferType method | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L496` |
| Information | Reading from file | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L508` |
| Error | Packet related header data is not proper | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L532` |
| Information | Packet destination details does not match current vessel exiting for the file {readFile.FileName} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L539` |
| Information | One of the split is locked skipping this packet | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L619` |
| Error | Error in AcquisitionExtBL.ProcessV2VPackets.Packet coutner latest | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L664` |
| Error | Error in AcquisitionExtBl.ProcessV2VPackets.Parallel processing | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L893` |
| Error | Packet basic validation failed for {readFile.FileName} moving to Error file | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1038` |
| Error | All split file not available right now waiting for split | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1073` |
| Error | Error in AcquistionExt method ProcessV2VPackets | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1108` |
| Information | {MethodName}\| Validating {FileName} packet counter {Counter} for source vessel {SourceVessel} and destination vessel {DestinationVessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1118` |
| Debug | {MethodName}\| Packet {FileName} is being parallely {ParallelFlag} processed for Channel {ChannelId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1125` |
| Debug | {MethodName}\| Packet {FileName} {PacketCounter} is correct for Channel {ChannelId} with source vessel {SourceVessel} and destination vessel {DestinationVessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1131` |
| Debug | {MethodName}\| Packet {FileName} {PacketCounter} is not correct for Channel {ChannelId} with source vessel {SourceVessel} and destination vessel {DestinationVessel}continuing process as channel is parallely processed | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1138` |
| Error | {MethodName}\| Packet {FileName} {PacketCounter} gotten is not correct for Source Vessel {SourceVessek} and Destination Vessel {DestinationVessel} for Channel {ChannelId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1146` |
| Debug | {MethodName}\| Packet {FileName} {PacketCounter} is already processed for Channel {ChannelId} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1153` |
| Debug | {MethodName}\| Packet {FileName} info could not be found in Missing Packet table for packet Counter  {Counter}, continuing | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1160` |
| Error | {MethodName}\|Exception occured while validating File {PacketName} with packet counter {Counter} for Source Vessel {Source} and destination Vessel {Destination} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1186` |
| Information | {MethodName}\| Validating packet counter {Counter} for source vessel {SourceVessel} and destination vessel {DestinationVessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1197` |
| Information | Channel is parallely processed Channel Id:{packetData.ChannelId}\| Updating counter to table | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1204` |
| Information | Channel is parallely processed Channel Id:{packetData.ChannelId}\| Latest Counter already came | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1217` |
| Information | Packet status{missingPacketStatus.STATUS} {missingPacketStatus.PacketCtr} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1220` |
| Information | Channel is sequentially processed Channel Id:{packetData.ChannelId}\| Updating counter to table | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1232` |
| Information | Channel is sequentially processed Channel Id:{packetData.ChannelId}\| Latest Counter already came | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1245` |
| Error | Error in AcquisitionExtBL.ValidateV2VPackets | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1257` |
| Error | <acquisitionExtEntity.ErrorMessage)> | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1273` |
| Error | ERROR:AcquisitionController\|Acquire\|AcquireFiles\|Message:{acquisitionExtEntity.ErrorMessage} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1298` |
| Throw:ArgumentException | Packet related header data is not proper | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1366` |
| Error | Error while executing AcquisitionExtBL.AcquireExtFiles | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionExtBL.cs#L1435` |
| Information | {MethodName}\| Starting Batch Acquisition Process for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L43` |
| Error | {MethodName}\| Invalid batch input: {ValidationMessage} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L49` |
| Critical | {MethodName}\| Replication Code not found for {Vessel}, exiting | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L86` |
| Information | {MethodName}\| Batch Acquisition Process Completed for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L115` |
| Error | {MethodName}\| Exception occured while processing Batch Acquisition for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L120` |
| Information | {MethodName}\| Starting Batch Priority Process for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L202` |
| Error | {MethodName}\| Packet Name {FileName} is not of a valid naming format for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L243` |
| Throw:InvalidOperationException | An exception occured while saving Import Queue Items | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L388` |
| Error | {MethodName}\| Exception occured while processing Batch Priority for {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L491` |
| Error | {MethodName}\| Exception while saving General Notification Import Queue Data\| Message : {ExMessage} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L609` |
| Debug | {MethodName}\| General Notification Import Queue Data saved successfully | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L611` |
| Error | {MethodName}\| Exception while updating Import Queue Data\| Message : {ExMessage} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L619` |
| Debug | {MethodName}\| Import Queue Data updated successfully | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L621` |
| Error | {MethodName}\| Exception while saving Import Queue Dt Data\| Message : {ExMessage} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L629` |
| Debug | {MethodName}\| Import Queue Dt Data saved successfully | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionGenB.cs#L631` |
| Information | {MethodName}\| Starting Acquisition Import process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L45` |
| Information | {MethodName}\| Old Import is disabled | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L49` |
| Information | {MethodName}\| Acquisition Old Import process completed with data {Count} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L66` |
| Information | {MethodName}\| Setting Initial Data | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L93` |
| Warning | {MethodName}\| Acquisition Import Service config is not accessible | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L100` |
| Warning | {MethodName}\| Acquisition Import Process has exceeded the time limit | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L116` |
| Information | {MethodName}\| Acquisition Import Process is already running\| Another pass has been requested | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L125` |
| Information | {MethodName}\|Initating Acquisition Import Process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L153` |
| Information | {MethodName}\| Acquisition Import Process Completed | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L158` |
| Information | {MethodName}\| Acquisition Import was triggered during the run, starting another pass | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L166` |
| Error | {MethodName}\| Exception in background task | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L174` |
| Error | {MethodName}\| Unobserved task exception in background acquisition process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L188` |
| Warning | {MethodName}\| {ParamName} is not configured, import queue is not started | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L229` |
| Information | {MethodName}\| Starting Integration import queue | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L236` |
| Debug | {MethodName}\| Integration import queue response {Output} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L241` |
| Error | {MethodName}\| Exception while starting Integration import queue | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L245` |
| Information | {MethodName}\| Starting Acquisition error handler process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L255` |
| Information | {MethodName}\| Acquisition Error Hanlder Process is already running | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L288` |
| Information | {MethodName}\|Initating Acquisition Error Handler Process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L321` |
| Information | {MethodName}\| Acquisition Error Handler Process Completed | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L326` |
| Error | {MethodName}\| Unobserved task exception in background error handler process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/AcquisitionMainOperation.cs#L344` |
| Debug | INFO:PacketCreationController\|GeneratePackets\|DirectoryCreated\| {_Dir} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L28` |
| Error | ERROR:CommonOperationsBL\|CreateDirectory | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L33` |
| Information | INFO: CommonOperationsBL \| ClearOldFiles\| CHECKING DIRECTORY {file} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L43` |
| Warning | CommonOperationsBL.ClearOldFiles\| Failed to delete old file: {FilePath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L59` |
| Error | ERROR:CommonOperationsBL \| ClearOldFiles\|MESSAGE: ERROR WHILE CLEARING OLD FILES  | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L67` |
| Debug | {MethodName}\|CHECKING IF FILE IS BEING USED\| CHECK Count {CheckCount} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L87` |
| Information | {MethodName}\|File:{FileName} is being used waiting for {WaitTime} milliseconds\| CHECK Count {CheckCount} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L91` |
| Error | <ex, methodName)> | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L126` |
| Error | CommonOperationBL.MoveFiles\| Source file and destination file are same Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L147` |
| Information | CommonOperationBL.MoveFiles\| Checking {fi.Name} status:{status} is copy? {copy} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L152` |
| Information | File exists in destination folder {Path.Combine} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L173` |
| Error | CommonOperationBL.MoveFiles\| file exists in {Destination}\| error while deleting it | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L179` |
| Debug | Moving file {Source} \| to destination: {Path.Combine} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L183` |
| Error | Not able to move file{fi.Name} as it is being used by another process\| Copying file instead | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L191` |
| Error | CommonOperationBL.MoveFiles {Source} while moving to {Destination} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L198` |
| Warning | {MethodName}\| Search path does not exist: {SearchPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L211` |
| Debug | {MethodName}\| File {FileName} found directly in path: {SearchPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L219` |
| Warning | {MethodName}\| Multiple files with name {FileName} found in {SearchPath}. Found {FileCount} instances: {FilePaths} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L237` |
| Information | {MethodName}\| Selected most recently modified file: {SelectedFile} (Modified: {ModifiedTime}) | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L247` |
| Warning | {MethodName}\| Access denied while searching in {SearchPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L257` |
| Warning | {MethodName}\| Directory not found while searching in {SearchPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L262` |
| Error | {MethodName}\| Error searching for file {FileName} in {SearchPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L267` |
| Debug | {MethodName}\| File {FileName} found in subdirectory: {FoundPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L276` |
| Debug | {MethodName}\| File {FileName} not found in {SearchPath} or its subdirectories | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L280` |
| Error | {MethodName}\| Exception occurred while searching for file {FileName} in {SearchPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L285` |
| Debug | {MethodName}\| Exact base-name match found: {FoundPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L326` |
| Debug | {MethodName}\| Pattern match found: {FoundPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L347` |
| Debug | {MethodName}\| File {BaseName} not found in {SearchPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L352` |
| Error | {MethodName}\| Exception occurred while searching for {BaseName} in {SearchPath} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/CommonOperationsBL.cs#L357` |
| Debug | {0}\|for API Address:{1}{2} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/ValidateConfigBL.cs#L14` |
| Throw:ArgumentNullException | Base address is null or empty | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/ValidateConfigBL.cs#L16` |
| Throw:ArgumentNullException | End point address is null or empty | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/BL/ValidateConfigBL.cs#L18` |
| Information | START:AcquisitionController\|Acquire | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L46` |
| Information | END:AcquisitionController\|Acquire | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L49` |
| Error | ERROR:AcquisitionController\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L61` |
| Error | <ex, errorEntity.ErrorMessage)> | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L86` |
| Information | {MethodName}\|Initiating Acquisition Import Process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L96` |
| Information | {MethodName}\|Initiating Error File Handler Process | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L108` |
| Information | textname-Acquisition-TestService-Vessel | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionController.cs#L119` |
| Information | {MethodName}\| Batch acquisition request received for vessel {Vessel} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/Controllers/AcquisitionGeneralController.cs#L31` |
| Throw:ArgumentNullException | <nameof(serviceConfig))> | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/ServiceClient/DBlogWServiceClient.cs#L28` |
| Debug | \|Input Data:{input} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/ServiceClient/DBlogWServiceClient.cs#L46` |
| Debug | \|RESPONSE\|{output} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/ServiceClient/DBlogWServiceClient.cs#L52` |
| Throw:ArgumentNullException | <nameof(httpClient))> | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/ServiceClient/ExternalRequestServiceClient.cs#L22` |
| Debug | \|Executing Post Request:{0}{1}, with input {2}  | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/ServiceClient/ExternalRequestServiceClient.cs#L28` |
| Debug | \|API RESULT:{contents} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/ServiceClient/ExternalRequestServiceClient.cs#L44` |
| Error | \|Exception | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/ServiceClient/ExternalRequestServiceClient.cs#L54` |
| Debug | Executing Method:{0}\|for Get API:{1} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/ServiceClient/ExternalRequestServiceClient.cs#L62` |
| Debug | {0} Result is {1} | `RepAcquisition/MariApps.PAL.Rep.Acquisition.Service/ServiceClient/ExternalRequestServiceClient.cs#L75` |

## RepAzure

Logger templates in RepAzure. Keywords: RepAzure log, error.

| Level | Message template | Source |
|---|---|---|
| Throw:InvalidOperationException | ServiceConfigData is null or empty | `RepAzure/MariApps.PAL.Rep.Azure.Service/AzureServiceDependency.cs#L63` |
| Information | {MethodName}\|Started Process | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L63` |
| Information | {MethodName}\| Azure Data Conduit Init Data completed with status {AzureInitStatus} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L72` |
| Error | Error in {MethodName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L87` |
| Information | {MethodName}\| Startning download process | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L104` |
| Information | {MethodName}\| Setting Initial Data | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L107` |
| Information | {MethodName}\| Azure init settings message = {AzureInitMessage} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L116` |
| Information | {MethodName}\| Network Status = {NetworkMessage} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L128` |
| Information | {MethodName}\|Download process initiated successfully. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L160` |
| Error | Exception in {MethodName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L175` |
| Error | {MethodName}\|Download process time exceeded. Removing status. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L199` |
| Information | {MethodName}\|Download process is already running. Exiting. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L205` |
| Information | {MethodName}\|Download process status updated. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L210` |
| Error | Exception in background download process in {MethodName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L224` |
| Information | {MethodName}\|Removing download process status in finally block. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L228` |
| Debug | {MethodName}\|Started move operation | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L244` |
| Error | {MethodName}\|Move process time exceeded. Removing status. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L255` |
| Information | {MethodName}\|Move process is already running. Exiting. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L261` |
| Information | {MethodName}\|Move process status updated. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L271` |
| Error | Exception in background move process in {MethodName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L284` |
| Information | {MethodName}\|Removing move process status in finally block. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L288` |
| Information | {MethodName}\|Move operation process initiated successfully. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L296` |
| Information | {MethodName}\| Startning file blob deletion process | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L326` |
| Error | {MethodName}\|Delete process time exceeded. Removing status. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L369` |
| Information | {MethodName}\|Delete process is already running. Exiting. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L375` |
| Information | {MethodName}\|Delete process status updated. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L385` |
| Error | Exception in background delete process in {MethodName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L399` |
| Information | {MethodName}\|Removing delete process status in finally block. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L403` |
| Information | {MethodName}\|Delete operation process initiated successfully. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L409` |
| Debug | {MethodName}\|Started reading IRep folder file | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L440` |
| Debug | {MethodName}\|IRep folder file reading is already in progress | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L445` |
| Debug | {MethodName}\|Completed reading IRep folder file | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L469` |
| Debug | {MethodName}\|Started Process | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L486` |
| Error | {MethodName}\|Move to History process time exceeded. Removing status. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L497` |
| Information | {MethodName}\|Move to History process is already running. Exiting. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L503` |
| Information | {MethodName}\|Move to History process status updated. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L513` |
| Error | Exception in background move-to-history process in {MethodName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L527` |
| Information | {MethodName}\|Removing move-to-history process status in finally block. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L531` |
| Information | {MethodName}\|Move to History operation process initiated successfully. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L537` |
| Debug | {MethodName}\|Started process | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L584` |
| Error | Excetion in {MethodName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L617` |
| Debug | {MethodName}\|starting for {PacketName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/AzureOperationBL.cs#L633` |
| Error | Error encrypting: {e.Message} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/EncryptionBL.cs#L54` |
| Error | Error decrypting: {e.Message} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/EncryptionBL.cs#L92` |
| Debug | Executing Method:{0}\|for  Get API:{1} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/ExternalCallBL.cs#L30` |
| Debug | {0} Result is {1} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/ExternalCallBL.cs#L41` |
| Error | DataImport\|DataImport\|PushToServiceGet\|Error:{ex.StackTrace} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/ExternalCallBL.cs#L48` |
| Debug | DataImport\|DataImport\|PushToServicePost:Start | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/ExternalCallBL.cs#L56` |
| Debug | DataImport\|DataImport\|PushToServicePost\|Info:{contents.Result} | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/ExternalCallBL.cs#L69` |
| Error | DataImport\|DataImport\|PushToServicePost | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/ExternalCallBL.cs#L76` |
| Throw:ArgumentNullException | input | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/XXHash.cs#L69` |
| Throw:ArgumentNullException | state | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/XXHash.cs#L464` |
| Throw:ArgumentNullException | inputStream | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/XXHash.cs#L507` |
| Throw:InvalidOperationException | <)> | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/XXHash.cs#L938` |
| Throw:ArgumentException | <)> | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/XXHash.cs#L968` |
| Throw:ArgumentOutOfRangeException | Specified argument must be a non-negative integer. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/XXHash.cs#L988` |
| Throw:ArgumentException | Multi dimension array is not supported on this operation. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/XXHash.cs#L992` |
| Throw:ArgumentException | The lower bound of target array must be zero. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/XXHash.cs#L996` |
| Throw:ArgumentException | Offset and length wereout of bounds for the array or count is greater than the number of elements from offset to the end of the array. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/XXHash.cs#L1000` |
| Throw:ArgumentOutOfRangeException | Offset was out of bounds for the array. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/XXHash.cs#L1006` |
| Throw:ArgumentException | Specified state is uninitialized. States must then be initialized using ResetStateXX() before first use. | `RepAzure/MariApps.PAL.Rep.Azure.Service/BL/XXHash.cs#L1010` |
| Debug | AzureController.AzureDownloadByReference\|Input: {InputString} | `RepAzure/MariApps.PAL.Rep.Azure.Service/Controllers/AzureController.cs#L40` |
| Information | Started AzureController.TestService | `RepAzure/MariApps.PAL.Rep.Azure.Service/Controllers/AzureController.cs#L102` |
| Information | Start of AzureVerifyAccess | `RepAzure/MariApps.PAL.Rep.Azure.Service/Controllers/AzureController.cs#L110` |
| Warning | {MethodName}\| {ServiceName} not in services.json; status {Event} of transfer {TransferId} not reported | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/BulkTransferAckSL.cs#L51` |
| Information | {MethodName}\| {Event} of transfer {TransferId} reported, HTTP {StatusCode} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/BulkTransferAckSL.cs#L66` |
| Warning | {MethodName}\| Could not report {Event} for file {FileName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/BulkTransferAckSL.cs#L70` |
| Throw:InvalidOperationException | EndpointKey '{destinationRequest.TableSettingsId}' is not a REP_PRIORITY_TABLE_SETTINGS ID | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/BulkTransferDestinationSL.cs#L38` |
| Throw:InvalidOperationException | {(isVessel ? "VSL" : "OFF")}_BASE_URL / {(isVessel ? "VSL" : "OFF")}_API_URL not configured in REP_PRIORITY_TABLE_SETTINGS for ID {tableSettingsId} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/BulkTransferDestinationSL.cs#L47` |
| Debug | {MethodName}\| Calling {RequestUri} with input {InputJson} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/BulkTransferDestinationSL.cs#L51` |
| Debug | {MethodName}\|RESPONSE\|{StatusCode}\|{Output} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/BulkTransferDestinationSL.cs#L62` |
| Throw:HttpRequestException | Destination API {requestUri} returned {(int)result.StatusCode}: {output} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/BulkTransferDestinationSL.cs#L65` |
| Throw:ArgumentNullException | <nameof(serviceConfig))> | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L44` |
| Debug | {MethodName}\| Started with input {Input} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L57` |
| Debug | {MethodName}\| Ended with output {Output} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L74` |
| Debug | {MethodName}\| Reading Data | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L82` |
| Debug | {MethodName}\|API INPUT DATA: {Input} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L105` |
| Debug | {MethodName}\|RESPONSE\|{Output} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L121` |
| Debug | {MethodName}\|API READING DATA | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L131` |
| Debug | {MethodName}\|API READING DATA with input {Input} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L203` |
| Debug | {MethodName}\|API READING DATA with opType {Type} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L229` |
| Debug | {MethodName}\|API INPUT DATA: {QueryString} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L319` |
| Debug | {MethodName}\| Response: {Output} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L328` |
| Error | Exception in {0} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L401` |
| Debug | {MethodName}\| Started post request with input {InputJson} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L418` |
| Debug | {MethodName}\| Response json data is {OutputJson} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L433` |
| Debug | {0}\|API INPUT DATA | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L481` |
| Debug | {MethodName}\|API READING DATA with input Replica Type Id {ReplicaTypeId} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L482` |
| Debug | {MethodName}\| API INPUT DATA: {InputJson} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L516` |
| Debug | {MethodName}\|Start | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L548` |
| Debug | {MethodName}\|REsponse {Output} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L558` |
| Debug | {MethodName}\|Start with status {Status} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L573` |
| Debug | {MethodName}\|API REQUEST: {QueryString} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L580` |
| Debug | {MethodName}\|RESPONSE: {Output} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/DblogwSL.cs#L588` |
| Error | {MethodName}\| Error RepIntegration Service API details missing | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/IntegrationSL.cs#L34` |
| Debug | {MethodName}\| Calling method with no input | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/IntegrationSL.cs#L51` |
| Debug | {0}\|API INPUT DATA: {1} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/SbusSL.cs#L50` |
| Debug | {MethodName}\|Start API INPUT DATA: {InputJson} | `RepAzure/MariApps.PAL.Rep.Azure.Service/SL/SbusSL.cs#L52` |
| Information | WorkerService:StartAsync | `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L33` |
| Information | WorkerService:StopAsync | `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L41` |
| Information | Starting {MethodName} | `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L50` |
| Information | {MethodName}\|Process cycle Start | `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L60` |
| Debug | {MethodName}\|Ended Azure download process with message {DownlaodMessage} and status {DownloadStatus} | `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L68` |
| Debug | {MethodName}\|Ended Move pending files process with message {MoveMessage} and status {MoveStatus} | `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L71` |
| Debug | {MethodName}\|Ended Delete pending files process with message {DeleteMessage} and status {DeleteStatus} | `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L74` |
| Debug | {MethodName}\|Ended Move to history table process with message {MoveToHistoryMessage} and status {MoveToHistoryStatus} | `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L77` |
| Information | {MethodName}\|Process cycle Ends | `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L83` |
| Information | WorkerService:Dispose | `RepAzure/MariApps.PAL.Rep.Azure.Service/WorkerService.cs#L94` |

## RepAzureRes

Logger templates in RepAzureRes. Keywords: RepAzureRes log, error.

| Level | Message template | Source |
|---|---|---|
| Information | {MethodName}\|Started Process | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L56` |
| Information | {MethodName}\| Azure Data Conduit Init Data completed with status {AzureInitStatus} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L65` |
| Error | Error in {MethodName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L76` |
| Information | {MethodName}\| Started saving file for Upload | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L96` |
| Debug | {MethodName}\| Input Model: {AzureBO} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L97` |
| Warning | {MethodName}\| Source file does not exist. Skipping {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L133` |
| Warning | {MethodName}\| Failed to prepare file {FileName} for upload. Skipping file. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L190` |
| Warning | {MethodName}\| No valid files available for upload after validation | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L198` |
| Debug | {MethodName}\| Saving Azure Res Data {Count} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L208` |
| Warning | {MethodName}\| Packet(s) already queued for upload, treating as awaiting | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L217` |
| Debug | {MethodName}\| Azure Res Data saved successfully | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L219` |
| Error | {MethodName}\|Error in saving data to AzureResUploadEntities due to {ErrorMessage} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L226` |
| Error | Exception in {MethodName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L240` |
| Information | {MethodName}\|Intiating Upload process | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L252` |
| Warning | {MethodName}\|Service basic config is not available. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L258` |
| Error | {MethodName}\|Upload process time exceeded. Removing status. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L282` |
| Information | {MethodName}\|Upload process is already running. Exiting. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L288` |
| Debug | {MethodName}\| Upload process has been started | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L302` |
| Information | {MethodName}\| Upload process stopped, application is stopping | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L308` |
| Error | {MethodName}\| Error occurred during upload process | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L312` |
| Debug | {MethodName}\| Upload process status removed | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L317` |
| Information | {MethodName}\| Initiating Azure Upload Call back process | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L327` |
| Warning | {MethodName}\| Azure config status is not success. Exiting callback. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L332` |
| Error | {MethodName}\|Callback process time exceeded. Removing status. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L344` |
| Debug | {MethodName}\| Callback process is already running. Exiting. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L350` |
| Debug | {MethodName}\| Call back process has been started | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L364` |
| Information | {MethodName}\| Call back process stopped, application is stopping | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L369` |
| Error | {MethodName}\| Error occurred during callback process | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L373` |
| Debug | {MethodName}\| Callback process status removed | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L378` |
| Information | {MethodName}\| Attempting to clear old JSON files | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L387` |
| Information | {MethodName}\| Old JSON files cleared. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L397` |
| Information | {MethodName}\| Archival already run today, skipping clear. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/AzureResUploadBL.cs#L405` |
| Information | RepAzureResumeService\|{methodName}\|{Message} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L35` |
| Debug | RepAzureResumeService\|{methodName}\|{Message} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L50` |
| Error | Error in {methodName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L63` |
| Debug | {MethodName}\| Generating MD5 Checksum for file {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L97` |
| Debug | {MethodName}\| MD5 Checksum reused for file {FileName} is {CheckSum} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L107` |
| Debug | {MethodName}\| MD5 Checksum generated for file {FileName} is {CheckSum} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L127` |
| Throw:FileNotFoundException | <filePath)> | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L151` |
| Debug | {MethodName}\| Deleting file {File} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L168` |
| Error | {MethodName}\|Error in deleting file {File} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L176` |
| Information | {MethodName}\| Generating file for {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L188` |
| Throw:FileNotFoundException | <fileLocation)> | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L192` |
| Throw:FileNotFoundException | <jsonFileName)> | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L225` |
| Error | {MethodName}\|Error in generating json file | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L229` |
| Debug | {MethodName}\| Generatign json file {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L240` |
| Warning | {MethodName}\| File does not exist {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L246` |
| Error | {MethodName}\| File is locked {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L253` |
| Debug | {MethodName}\| Json file created successfully with {ChunkCount} chunks | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L290` |
| Throw:FileNotFoundException | Json file not created | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L294` |
| Error | Exception while generating blob chunk json file | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L298` |
| Information | {MethodName}\| checking network status | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L318` |
| Information | {MethodName}\|Network status: {NetworkStatus} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L335` |
| Error | {MethodName}\|Error in checking network status | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L340` |
| Throw:ArgumentNullException | Storage account name is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L355` |
| Throw:ArgumentNullException | Storage account key is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L360` |
| Debug | {MethodName}\| File is currently locked or inaccessible: {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L434` |
| Debug | {MethodName} clearing files older than 30 days | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L452` |
| Error | {MethodName}\|Error in deleting old files | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/CommonOperationBL.cs#L468` |
| Error | Error encrypting: {e.Message} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/EncryptionBL.cs#L51` |
| Error | Error decrypting: {e.Message} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/EncryptionBL.cs#L89` |
| Information | {MethodName} Started | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L39` |
| Information | {MethodName}\| No finished Azure resume call back data found for processing | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L46` |
| Information | {MethodName}\| Application is stopping, no new call back batch is started | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L58` |
| Information | {MethodName}\| No valid Azure resume call back data found for processing | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L69` |
| Debug | {MethodName}\| Starting call back process for {Count} files | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L102` |
| Error | {ApiError} \| Error while calling integration API | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L115` |
| Debug | {MethodName}\| Call back process completed for {Count} files with status {Status} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L119` |
| Information | {MethodName} Ended | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L142` |
| Error | {ErrorMethod} \| Error while processing finished data | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/IntegrationCallBL.cs#L151` |
| Debug | {MethodName}\| Large file lane is disabled | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L75` |
| Information | {MethodName}\|Started Uploading Pending Data | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L82` |
| Information | {MethodName}\| No pending data found for upload | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L90` |
| Error | {MethodName}\| Azure settings verification failed, cannot proceed with upload | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L98` |
| Throw:InvalidOperationException | Azure Account Key is empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L127` |
| Critical | {MethodName}\| AzurePrimaryConnectionString is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L133` |
| Error | {MethodName}\| NO network connection | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L140` |
| Warning | {MethodName}\| Chunk size {ChunkSize} exceeds MaxChunkSizeInKB, using {MaxChunkSize} bytes | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L152` |
| Warning | {MethodName}\| Chunk size is zero, network speed is low cannot proceed with upload | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L158` |
| Information | {MethodName}\| Uploading files with chunk size {ChunkSize} bytes | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L162` |
| Information | {MethodName}\| Application is stopping, no new upload batch is started | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L171` |
| Error | {MethodName}\|No network | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L184` |
| Information | {MethodName}\| No valid Azure resume upload data found for processing | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L201` |
| Information | {MethodName}\| Uploading {Count} number of files | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L212` |
| Warning | {MethodName}\| Folder structure {FolderStructure} is in invalid format for file {FileName}, updating to default format | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L236` |
| Information | {MethodName}\|Upload pending process END | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L263` |
| Debug | {MethodName}\| Validating upload data for {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L281` |
| Error | {MethodName}\|FileName or file location is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L285` |
| Debug | {MethodName}\|Update status for {FileName} is {Status} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L299` |
| Error | {MethodName}\|File {FileName} does not exist in source location and Json file also does not exist | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L305` |
| Debug | {MethodName}\| Validated upload data for {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L324` |
| Error | {MethodName}\|updating failed status to Db completed with {Status} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L346` |
| Debug | {MethodName}\| Starting Azure Upload Abort Handler for file {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L354` |
| Debug | {MethodName}\| Upload abort status update completed with status code {UpdateStatusCode} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L381` |
| Debug | {MethodName}\| Started azure worker process for file {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L392` |
| Debug | {MethodName}\|Json location is null or empty for file {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L403` |
| Debug | {MethodName}\|Json Update status for {FileName} is {Status} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L421` |
| Error | {MethodName}\| Json file content is null or empty for file {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L435` |
| Warning | {MethodName}\| Json file is corrupted for file {FileName} — deleting and regenerating | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L462` |
| Error | {MethodName}\| Failed to regenerate Json file for {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L473` |
| Warning | {MethodName}\| Invalid block metadata for file {FileName}. Reason: {Reason}. Regenerating json. | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L484` |
| Error | {MethodName}\| Failed to regenerate Json file for {FileName} after invalid block metadata | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L497` |
| Throw:InvalidDataException | Invalid block metadata and regeneration failed for {uploadWorkerParamsEntity.UploadEntity.FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L498` |
| Debug | {MethodName}\| Regenerated JSON content for {FileName}: {JsonContent} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L504` |
| Error | {MethodName}\| Regenerated block metadata is still invalid for file {FileName}. Reason: {Reason} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L508` |
| Throw:InvalidDataException | Invalid regenerated block metadata for {uploadWorkerParamsEntity.UploadEntity.FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L510` |
| Information | {MethodName}\| Starting upload for file {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L514` |
| Information | {MethodName}\| upload Process completed for file {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L573` |
| Error | {MethodName}\|Upload worker crashed for {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L578` |
| Error | {MethodName}\| Upload failed status update completed with status code {UpdateStatusCode} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L591` |
| Information | {MethodName}\| Calculating MD5 for {FileName} ({FileSize} bytes) | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L599` |
| Throw:InvalidDataException | MD5 checksum could not be calculated for {uploadEntity.FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L618` |
| Throw:InvalidOperationException | MD5 checksum could not be saved for {uploadEntity.FileName}: {saveStatus?.ErrorMessage} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L623` |
| Information | {MethodName}\| MD5 saved for {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L626` |
| Debug | {MethodName}\| Upload still in progress for {FileName}, heartbeat status {StatusCode} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L657` |
| Warning | {MethodName}\| Heartbeat update failed for {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L661` |
| Debug | {MethodName}\| Uploading blob {BlobName} to container {ContainerName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L669` |
| Throw:InvalidOperationException | Azure Blob Connection string is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L679` |
| Information | {MethodName}\| Uploading to blob {BlobName} number of chunks uploaded {BlockSubListCount} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L695` |
| Information | {MethodName}\| Found {StagedCount} already staged chunks for blob {BlobName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L724` |
| Information | {MethodName}\| Pending chunks to upload {PendingId} for file {BlobName} and max count{MaxId} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L731` |
| Throw:EndOfStreamException | Expected {blockSub.Buffer} bytes at offset {blockSub.Offset} but file ended after {totalRead} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L745` |
| Debug | {MethodName}\| Upload completed for chunk {Offset}, for file {BlobName} chunkNumber:{ChunkId} and chunk {Id}/{MaxId} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L755` |
| Information | {MethodName}\| Blob {BlobName} uploaded successfully | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L774` |
| Error | {MethodName}\| Exception | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L780` |
| Debug | {MethodName}\| Starting Azure Upload Complete Handler for file {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L807` |
| Debug | {MethodName}\| Upload is successful for file {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L812` |
| Debug | {MethodName}\| Upload complete status update completed with status code {UpdateStatusCode} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L824` |
| Error | {MethodName}\| Upload is failed for file {FileName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L831` |
| Debug | {MethodName}\| Json file content rewrite status {FileContentWriteStatus} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L835` |
| Debug | {MethodName}\| Upload failed status update completed with status code {UpdateStatusCode} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L847` |
| Debug | {MethodName}\| Clearing old json files | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L880` |
| Information | {MethodName}\| Old json files cleared | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L889` |
| Error | <ex, methodName)> | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L894` |
| Warning | AzurePrimaryConnectionString is empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1028` |
| Throw:ArgumentNullException | Azure connecitons string is empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1029` |
| Information | Verified Access to container {azureCommon.StorageContainerName} and basic  settings is accessible | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1033` |
| Throw:ArgumentNullException | Azure primary connection string is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1074` |
| Throw:ArgumentNullException | Container name is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1079` |
| Warning | {MethodName}\| File {FileName} of {FileSize} bytes needs chunk size {MinChunkSize} to stay within {MaxBlockCount} blocks, configured {ChunkSize} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1126` |
| Error | Exception in {MethodName} for {FileLocation} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1133` |
| Information | {MethodName}\| Calculating chunk size for speed: {Speed} KB/s | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1140` |
| Information | {MethodName}\| Using 4MB chunks for very fast connection | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1145` |
| Information | {MethodName}\| Using 2MB chunks for fast connection | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1150` |
| Information | {MethodName}\| Using 1MB chunks for medium connection | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1155` |
| Information | {MethodName}\| Using 256KB chunks for slow connection | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1160` |
| Information | {MethodName}\| Using 64KB chunks for very slow connection | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1165` |
| Warning | {MethodName}\| Connection too slow for upload, speed: {Speed} KB/s | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1170` |
| Information | {MethodName}\| Starting upload speed test | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1180` |
| Information | {MethodName}\| Upload test: {DataSize} bytes in {Time} seconds | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1205` |
| Information | {MethodName}\| Calculated upload speed: {Speed} KB/s | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1210` |
| Error | {MethodName}\| Speed test failed, assuming very slow connection | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1215` |
| Information | {MethodName}\| Starting V2V Azure Resend Data | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1232` |
| Information | {MethodName}\| {Packet} exists status {AzureFileStatus} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1246` |
| Information | {MethodName}\| V2V Azure Resend Data Completed | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1269` |
| Information | {MethodName}\| Checking if file {FileName} exists in container {ContainerName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1293` |
| Error | {MethodName}\| file size mismatch for {FileName} blob Size: {BlobFileSize} ,Actual Size: {FileSize} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1312` |
| Error | {MethodName}\| file checksum mismatch for {FileName} blob checkSum: {BlobCheckSum} ,Actual CheckSum: {CheckSum} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1324` |
| Information | {MethodName}\| file {FileName} exists in container {ContainerName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1337` |
| Error | {MethodName}\| file {FileName} does not exist in container {ContainerName} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/UploadProcessBL.cs#L1349` |
| Throw:ArgumentNullException | input is null | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/ValidationBL.cs#L23` |
| Throw:ArgumentNullException | <azureBO.CoParameterName, nameof(azureBO.CoParameterName))> | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/ValidationBL.cs#L24` |
| Throw:ArgumentNullException | Channel Details is empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/ValidationBL.cs#L25` |
| Throw:ArgumentNullException | Invalid File Details | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/ValidationBL.cs#L27` |
| Throw:ArgumentNullException | IS_VESSEL does not exist or value is num or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/ValidationBL.cs#L49` |
| Throw:ArgumentNullException | PR_REP_ROOT does not exist or value is num or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/ValidationBL.cs#L51` |
| Throw:ArgumentNullException | Storage Account name is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/ValidationBL.cs#L66` |
| Throw:ArgumentNullException | Storage Account key is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/ValidationBL.cs#L70` |
| Throw:ArgumentNullException | Storage Container name is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/ValidationBL.cs#L75` |
| Throw:ArgumentNullException | Client Code is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/ValidationBL.cs#L80` |
| Throw:ArgumentNullException | Client Environment Unique Id is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/ValidationBL.cs#L85` |
| Throw:ArgumentNullException | Locationis null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/BL/ValidationBL.cs#L90` |
| Error | {MethodName}\| Error RepDblogW Service API details missing | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L27` |
| Throw:ArgumentNullException | <nameof(serviceConfig))> | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L28` |
| Debug | {MethodName}\| Reading azure settings | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L41` |
| Throw:ArgumentNullException | Api address is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L46` |
| Debug | {MethodName}\| Ended with output {Output} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L55` |
| Debug | {MethodName}\| Get Azure Basic Settings | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L63` |
| Debug | {MethodName}\| Save azure resume data with input {InputJson} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L87` |
| Error | {MethodName}\| DB service returned {StatusCode} with output {Output} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L112` |
| Error | {MethodName}\| save failed for input {ReqJson} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L124` |
| Debug | {MethodName}\| Update azure resume info with input {InputJson} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L135` |
| Throw:ArgumentNullException | Api URL is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L143` |
| Error | {MethodName}\| update failed for input {ReqJson} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L165` |
| Debug | {MethodName}\| Update azure resume data with input {InputJson} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L181` |
| Throw:ArgumentNullException | Base URL is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L189` |
| Debug | {MethodName}\| GET azure Pending Data | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L220` |
| Debug | {MethodName}\|API INPUT DATA: {QueryString} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L234` |
| Debug | {MethodName}\| Reading all data based on status | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L262` |
| Debug | {MethodName}\| Read-Update azure res Pending Data | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L330` |
| Debug | {MethodName}\| Moving azure resume data to history table with input {InputJson} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L376` |
| Error | {MethodName}\| update and move to Hisotry failed for input {ReqJson} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L406` |
| Debug | {MethodName}\| Checking if azure res data exists for status {Status} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L415` |
| Debug | {MethodName}\| API INPUT DATA: {FullUrl} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/DbConfigSL.cs#L426` |
| Debug | {MethodName}\| Request: {Request} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/IntegrationSL.cs#L35` |
| Throw:ArgumentNullException | API URL is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/IntegrationSL.cs#L40` |
| Debug | {MethodName}\| Response: {Response} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/SL/IntegrationSL.cs#L57` |
| Throw:InvalidOperationException | ServiceConfigData is null or empty | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/ServiceDependency.cs#L50` |
| Information | WorkerService:StartAsync | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/WorkerService.cs#L33` |
| Information | WorkerService:StopAsync | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/WorkerService.cs#L41` |
| Information | {MethodName}\| process started with worker service Initiate status {InitiateStatus} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/WorkerService.cs#L49` |
| Debug | {MethodName}\| SetAllInitData Status:{Status} Message: {ErrorMessage} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/WorkerService.cs#L65` |
| Information | {MethodName}\| Process cycle started | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/WorkerService.cs#L67` |
| Debug | {MethodName}\| CheckAzureSettings Status:{Status} Message: {ErrorMessage} | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/WorkerService.cs#L73` |
| Information | {MethodName}\| Process cycle completed | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/WorkerService.cs#L82` |
| Information | WorkerService:Dispose | `RepAzureRes/MariApps.PAL.Rep.Azure.Res.Service/WorkerService.cs#L93` |

## RepCompression

Logger templates in RepCompression. Keywords: RepCompression log, error.

| Level | Message template | Source |
|---|---|---|
| Throw:DataException | Data did not save Successfully | `RepCompression/MariApps.PAL.Rep.Compress.DAL/CompressRepository.cs#L109` |
| Information | START:CompressController\|CreateZipFile\|CreateZipFile | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L30` |
| Information | INFO: Compression INPUT JSON DATA: {compressionInputJson} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L33` |
| Error | ERROR:PacketCreationController\|GeneratePackets\|GeneratePackets\|Message:{compressInput.ErrorMessage} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L50` |
| Throw:ArgumentException | The FileName Generated {tempTarFileName} already exists\| FileName passed should be unique | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L106` |
| Information | If multiple files creating tar file first then applying SevenZip Compression | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L108` |
| Error | tempTar file deletion error | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L128` |
| Error | ERROR:CompressController\|CreateZipFile\|CreateZipFile\|Message:{compressInput.ErrorMessage}Stack trace:{ex.Message} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L173` |
| Error | ERROR:CompressController\|CreateZipFile\|Error while Deleting files Message:  | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L187` |
| Information | SUCCESS:CompressController\|CreateZipFile\|CreateZipFile\|FileName:{CompZipPath} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L207` |
| Error | ERROR:CompressController\|CreateZipFile\|CreateZipFile\|Message:{compressInput.ErrorMessage} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L215` |
| Information | END:CompressController\|CreateZipFile\|CreateZipFile\|FileName:{CompZipPathErr} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L224` |
| Information | INFO: CompressionOUTPUT JSON DATA: {compressionOutputJson} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L227` |
| Error | ERROR:CompressController\|CreateZipFile\|CreateZipFile\|Message:{ex.Message}\|StackTrace:{ex.StackTrace}\|FileName:{CompZipPathErr} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L234` |
| Information | INFO:CompressController\|CreateZipFile\|CreateZipFile\|CreateDirectory\|DirectoryCreated\| {_Dir} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L427` |
| Error | ERROR:CompressController\|CreateZipFile\|CreateZipFile\|CreateDirectory\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L432` |
| Information | File:{fi.Name} CHECKING IF FILE IS BEING USED\| CHECK Count{checkCount} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L450` |
| Information | File:{fi.Name} is being used waiting for 20 seconds\| CHECK Count{checkCount} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L453` |
| Information | The file is being used by another process\|File: {fi.Name}\|Error messasge: {ex.Message} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L476` |
| Information | The file is being used by another process\|File: {file.Name}\| ERROR MESSAGE: {ex.Message} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBL.cs#L491` |
| Warning | {MethodName} - Validation failed: {Error} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBatchBL.cs#L36` |
| Information | {MethodName} - Processing GroupId {GroupId}, output: {OutputPath} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBatchBL.cs#L49` |
| Information | {MethodName} - GroupId {GroupId} compressed successfully | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBatchBL.cs#L89` |
| Error | {MethodName} - Compression failed for GroupId {GroupId} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBatchBL.cs#L93` |
| Warning | {MethodName} - Could not delete partial file: {Path} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/CompressBatchBL.cs#L196` |
| Error | ERROR:CompressController\|ValidateData\|Message:{inputBO.ErrorMessage} | `RepCompression/MariApps.PAL.Rep.Compress.Service/BL/ValidateInputBL.cs#L31` |
| Error | ERROR:CompressBatchController\|ZipBatch\|Message:{ex.Message} | `RepCompression/MariApps.PAL.Rep.Compress.Service/Controllers/CompressBatchController.cs#L40` |
| Error | ERROR:CompressController\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepCompression/MariApps.PAL.Rep.Compress.Service/Controllers/CompressController.cs#L50` |
| Information | Test Service Compression Service is working | `RepCompression/MariApps.PAL.Rep.Compress.Service/Controllers/CompressController.cs#L60` |

## RepDBLogW

Logger templates in RepDBLogW. Keywords: RepDBLogW log, error.

| Level | Message template | Source |
|---|---|---|
| Throw:ArgumentNullException | <nameof(connectionString))> | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Context/DapperContext.cs#L23` |
| Throw:ArgumentNullException | <nameof(dapperContext))> | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L27` |
| Throw:ArgumentNullException | <nameof(logger))> | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L28` |
| Debug | {MethodName}\| Checking if Azure resource data exists for status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L42` |
| Debug | {MethodName}\| Azure resource data exists: {DataExists} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L56` |
| Error | {MethodName}\| Error checking if Azure resource data exists for status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L63` |
| Debug | {MethodName}\| Checking if Azure download data exists for status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L79` |
| Debug | {MethodName}\| Azure download data exists: {DataExists} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L93` |
| Error | {MethodName}\| Error checking if Azure download data exists for status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L100` |
| Debug | {MethodName}\| Saving Azure downloads in bulk | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L114` |
| Information | {MethodName}\| Azure downloads saved successfully | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L132` |
| Error | {MethodName}\| Error while saving Azure downloads | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L142` |
| Error | Exception occurred while saving Azure downloads in {MethodName} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L153` |
| Debug | {MethodName}\| Updating export type for vesselObjectId: {VesselObjectId} to exportType: {ExportType} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L166` |
| Information | {MethodName}\| Export type updated successfully for vesselObjectId: {VesselObjectId} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L177` |
| Error | Exception occurred while updating export type in {MethodName} for vesselObjectId: {VesselObjectId} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L181` |
| Debug | {MethodName}\| Saving Import Queue Data | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L191` |
| Information | {MethodName}\| Import Queue Data saved | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L212` |
| Error | {MethodName}\| Error while saving Import Queue Data | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L222` |
| Error | Exception occured while saving data in {MethodName} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/AzureDblogRepository.cs#L233` |
| Error | ERROR:DBlogWrite\|LogWriteApiCallData\|SaveApiCallLogEntry\|Message:{ex.Message} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DBlogWRepository.cs#L39` |
| Error | ERROR:DBlogWrite\|LogWrite\|SaveLogEntry\|Message:{ex.Message} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DBlogWRepository.cs#L106` |
| Error | Error in DBlogWRepository.ReadApiCallLog | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DBlogWRepository.cs#L264` |
| Error | IntegrationRepository.ReadChannelFromTableSettingsId | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DBlogWRepository.cs#L299` |
| Warning | DbPckLogRepository.{OperationName} - Transient error (attempt {RetryAttempt}/{MaxAttempts}), retrying in {DelayMs}ms | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L43` |
| Throw:DataException | Data did not save Successfully | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L80` |
| Error | Error in DbPckLogRepository.UpdateOutPacketSource service method | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L86` |
| Error | Error in DbPckLogRepository.SaveExtPacketDetails service method | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L172` |
| Error | Error in DbPckLogRepository.SaveSourcePacketDetails service method | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L198` |
| Error | Error in DbPckLogRepository.GetExportParams\|Message: {ex.Message} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L228` |
| Information | <resendInput.UniqueId + resendInput.MissingAt)> | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L239` |
| Error | Error in DbPckLogRepository.GetV2VResendData | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L281` |
| Error | Error in DbPckLogRepository.V2VResendUpdatePacket | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L302` |
| Error | GetV2VSourcePacketData | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L352` |
| Error | Error in SaveCheckOperationStatus | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L378` |
| Error | DbPckLogRepositoy.ReadCompressionType | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L414` |
| Error | DbPckLogRepositoy.ReadPriorityPacketStatus | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L457` |
| Error | DbPckLogRepositoy.ReadAcknStatusList | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L498` |
| Warning | DbPckLogRepository.SaveMissingPacketStatusBulk - Duplicate key detected and ignored | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L530` |
| Warning | DbPckLogRepository.SaveMissingPacketStatusBulk - Transient error (attempt {RetryAttempt}/{MaxAttempts}), retrying in {DelayMs}ms | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L536` |
| Error | DbPckLogRepository.SaveMissingPacketStatusBulk - Permanent error after {RetryCount} attempts | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L543` |
| Error | DbPckLogRepositoy.ReadMissingPacketDataById | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/DbPckLogRepository.cs#L594` |
| Debug | {MethodName}\| Export Complete Config Path against each vessel Data | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/Rep2IDbRepository.cs#L34` |
| Debug | {MethodName}\|Ended, Read export complete config path mapped against vessel | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/Rep2IDbRepository.cs#L58` |
| Error | Error in {MethodName} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/Rep2IDbRepository.cs#L64` |
| Debug | {MethodName}\|Saving to Validte Q for Vessel {VesselId} with packetNumber {PacketNumber} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/Rep2IDbRepository.cs#L75` |
| Debug | {MethodName}\| Read Manual Operation Path | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/Rep2XDbRepository.cs#L77` |
| Warning | {MethodName}\| Row with NAME 'REP_MANUAL_OP_PATH' not found | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/Rep2XDbRepository.cs#L92` |
| Debug | {MethodName}\|Ended, Read Manual Operation Path | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/Rep2XDbRepository.cs#L97` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|SbusWinReadConfiguration | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L83` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|SbusWinGetPacketCounter | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L332` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|SbusWinReadVesselList | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L376` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|SbusWinReadCoParam | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L415` |
| Information | Getting CoParam value | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L419` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|SbusWinReadLocation | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L458` |
| Information | Transfer Type:{response.transferType} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L490` |
| Information | ReadLocation:File location:{response.transferLocation} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L518` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|SbusWinGetFilesToDownload | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L537` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|SbusWinUpdateDownload | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L594` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|SbusWinReadServiceUrl | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L661` |
| Information | Reading Intergration Service URL | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L680` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|SbusWinInsertSbusNotification | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L705` |
| Information | InsertSbusNotification\|VesselObjectId:{0}, FileName:{1}, Status:{2}, Message:{3} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L715` |
| Warning | SbusWinInsertSbusNotification - Transient error (attempt {RetryAttempt}/{MaxAttempts}), retrying in {DelayMs}ms | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L736` |
| Error | SbusWinInsertSbusNotification - Permanent error after {RetryCount} retries | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L743` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|SbusWinInsertErrorLog | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L792` |
| Error | ERROR_MSG:{error.ERROR_MSG} \| StackTrace:{error.STACK_TRACE} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L798` |
| Error | SbusNotificationRepository.ReadAzureFileDownloadQ | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L890` |
| Debug | {MethodName}\| Started with Type: {Type}, Status: {Status}, NoOfRecords: {NoOfRecords}, UpdateStatus: {UpdateStatus} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L898` |
| Debug | {MethodName}\| Successfully retrieved {RecordCount} records | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L954` |
| Warning | {MethodName}\| Transient error (attempt {RetryAttempt}/{MaxAttempts}), retrying in {DelayMs}ms | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L960` |
| Error | Error in {MethodName} after {RetryCount} retries | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L967` |
| Throw:DataException | <outputData[1].Value.ToString())> | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L991` |
| Debug | {MethodName}\| Inserting download history data for params {OperationType}, {UpdateStatus} and Type Table | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1006` |
| Debug | {MethodName}\| Update process ended | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1025` |
| Error | Exception in {MethodName} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1030` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|AzureGetExportParams | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1102` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|AzureReadVesselList | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1143` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|AzureUpdateUploadFile | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1178` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|AzureGetPendingUploadFile | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1212` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|AzureGetTransferType | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1251` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|AzureGetTransferLocation | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1299` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|AzureUpdateUploadFileBulk | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1346` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|AzureGetAzureSettings | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1428` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|AzureGetSettings | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1496` |
| Information | ERROR_MSG:{error.ERROR_MSG} \| StackTrace:{error.STACK_TRACE} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1570` |
| Error | ERROR_MSG:{msg} \| StackTrace:{stacktrace} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1604` |
| Error | ErrorSaveMethod:{ex.Message} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1627` |
| Information | ERROR_MSG:{msg} \| StackTrace:{stacktrace} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1632` |
| Error | InformationSaveMethod:{ex.Message} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1655` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|AzureGetSettingsV2V | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1849` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|GetQueueNameV2V | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L1909` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|SbusWinUpdateDownloadV2V | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2003` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|SaveMasterLogV2V | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2070` |
| Information | START:DbServiceSbusController\|SbusNotificationRepository\|GetTrackChangeDetailsV2V | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2139` |
| Debug | {MethodName}\| Saving data | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2417` |
| Warning | {MethodName}\| Duplicate submission, record already queued: {Message} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2432` |
| Throw:DataException | Data did not save Successfully\|{outputData?[1]?.Value} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2436` |
| Debug | {MethodName}\| Data save completed with status {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2438` |
| Warning | SbusNotificationRepository.UpdateAzureResUploadData - Transient error (attempt {RetryAttempt}/{MaxAttempts}), retrying in {DelayMs}ms | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2475` |
| Error | SbusNotificationRepository.UpdateAzureResUploadData - Permanent error after {RetryCount} retries | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2483` |
| Debug | {MethodName}\| updating data | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2496` |
| Error | Exception in Db call for {MethodName} with input Type:{Type}, Read Status {Status}, RecordCount {RecordCount}, NewUpdateStatus {UpdateStatus} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2700` |
| Debug | {MethodName}\| Started | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2709` |
| Debug | {MethodName}\| Db save completed with status {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2732` |
| Error | Exception in {MethodName} after {RetryCount} retries | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2745` |
| Error | SbusNotificationRepository.SaveChatMessageToQueue | `RepDBLogW/MariApps.PAL.Rep.DBlogW.DAL/Repositories/SbusNotificationRepository.cs#L2821` |
| Throw:ArgumentNullException | <nameof(azureDblogRepository))> | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/AzureDblogBL.cs#L33` |
| Debug | {MethodName}\| Started with status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/AzureDblogBL.cs#L48` |
| Debug | {MethodName}\| Completed. Data exists: {DataExists} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/AzureDblogBL.cs#L52` |
| Error | {MethodName}\| Error checking Azure resource data exists for status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/AzureDblogBL.cs#L58` |
| Error | {MethodName}\| Error checking Azure download data exists for status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/AzureDblogBL.cs#L84` |
| Debug | {MethodName}\| Started updating export type for vesselObjectId: {VesselObjectId} with exportType: {ExportType} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/AzureDblogBL.cs#L95` |
| Debug | {MethodName}\| Completed updating export type for vesselObjectId: {VesselObjectId} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/AzureDblogBL.cs#L99` |
| Error | {MethodName}\| Error updating export type for vesselObjectId: {VesselObjectId} with exportType: {ExportType} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/AzureDblogBL.cs#L104` |
| Debug | {MethodName}\| Started saving Azure downloads bulk data. Count: {Count} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/AzureDblogBL.cs#L113` |
| Error | {MethodName}\| Error occurred while saving Azure downloads bulk data. | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/AzureDblogBL.cs#L159` |
| Debug | {MethodName}\| PacketNumber is 0 fetching from DB | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/DBlogWBL.cs#L36` |
| Error | {MethodName}\| error in save to import validate queue | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/DBlogWBL.cs#L46` |
| Debug | {MethodName}\|Validate queue saved successfully | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/BL/DBlogWBL.cs#L51` |
| Throw:ArgumentNullException | <nameof(azureDblogBL))> | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L23` |
| Information | START: AzureDblog\|CheckAzureResDataExists\|Status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L37` |
| Information | END: AzureDblog\|CheckAzureResDataExists\|Status: {Status}\|Result: {DataExists} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L41` |
| Information | START: AzureDblog\|CheckAzureDownloadDataExists\|Status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L56` |
| Information | END: AzureDblog\|CheckAzureDownloadDataExists\|Status: {Status}\|Result: {DataExists} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L60` |
| Information | START: AzureDblog\|ProcessNgV4SyncHd\|ID: {ID} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L75` |
| Error | END: AzureDblog\|ProcessNgV4SyncHd\|ID: {ID} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L80` |
| Information | START: AzureDblog\|SaveAzureDownloadsBulk\|Count: {Count} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L104` |
| Information | END: AzureDblog\|SaveAzureDownloadsBulk\|Status: {Status} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L108` |
| Information | START: AzureDblog\|UpdateExportType\|VesselObjectId: {VesselObjectId}\|ExportType: {ExportType} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L124` |
| Information | END: AzureDblog\|UpdateExportType\|VesselObjectId: {VesselObjectId} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/AzureDblogController.cs#L128` |
| Information | START:DBlogWrite\|LogWrite | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DBlogWController.cs#L33` |
| Information | END:DBlogWrite\|LogWrite | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DBlogWController.cs#L37` |
| Information | START:DBlogWrite\|LogWriteApiCallData | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DBlogWController.cs#L79` |
| Information | END:DBlogWrite\|LogWriteApiCallData | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DBlogWController.cs#L83` |
| Information | START:DBlogWrite\|ReadApiCallLog | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DBlogWController.cs#L90` |
| Information | START:DBlogWrite\|TestService | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DBlogWController.cs#L102` |
| Information | START:DBlogWrite\|Version | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DBlogWController.cs#L111` |
| Information | START:DbServiceSbusController\|UpdateOutPacketSource | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbPckLogController.cs#L30` |
| Information | START:DbPckLogController\|GetExportParams | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbPckLogController.cs#L39` |
| Information | START:DbPckLogController\|SaveExtPacketDetails | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbPckLogController.cs#L47` |
| Information | START:DbPckLogController\|GetV2VResendPacketData | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbPckLogController.cs#L95` |
| Information | START:DbServiceSbusController\|SaveCheckOperationStatus | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbPckLogController.cs#L104` |
| Information | START:DbServiceSbusController\|ReadCompressionType | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbPckLogController.cs#L118` |
| Information | START:DbServiceSbusController\|ReadPriorityPacketStatus | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbPckLogController.cs#L133` |
| Information | START:DbServiceSbusController\|ReadAcknStatusList | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbPckLogController.cs#L147` |
| Information | START:DbServiceSbusController\|UpdateOutPacketHd | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbPckLogController.cs#L162` |
| Information | START:DbServiceSbusController\|UpdateMissingPacketEnity | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbPckLogController.cs#L194` |
| Warning | DbPckLogController.UpdateMissingPacketEnity - Empty missing packet payload received | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbPckLogController.cs#L198` |
| Warning | DbPckLogController.UpdateMissingPacketEnity - Duplicate rows in request: {DuplicateGroupCount} groups, {TotalRows} rows | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbPckLogController.cs#L217` |
| Warning | Duplicate missing packet key in request \| VesselObjectId:{VesselObjectId} PacketCounter:{PacketCounter} MissingAt:{MissingAt} ChannelId:{ChannelId} Count:{Count} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbPckLogController.cs#L222` |
| Information | START:DbServiceSbusController\|ReadMissingPacketById | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbPckLogController.cs#L234` |
| Information | START:DbServiceSbus\|TestService | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L79` |
| Information | START:DbServiceSbusController\|SbusWinReadConfiguration | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L90` |
| Information | START:DbServiceSbusController\|SbusWinGetPacketCounter | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L99` |
| Information | START:DbServiceSbusController\|SbusWinReadVesselList | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L108` |
| Information | START:DbServiceSbusController\|SbusWinReadCoParam | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L117` |
| Information | START:DbServiceSbusController\|SbusWinReadLocation | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L126` |
| Information | START:DbServiceSbusController\|SbusWinGetFilesToDownload | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L135` |
| Information | START:DbServiceSbusController\|SbusWinUpdateDownload | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L144` |
| Information | START:DbServiceSbusController\|SbusWinReadServiceUrl | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L165` |
| Information | START:DbServiceSbusController\|SbusWinInsertSbusNotification | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L174` |
| Information | START:DbServiceSbusController\|SbusWinGetSbusSettings | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L183` |
| Information | START:DbServiceSbusController\|SbusWinInsertErrorLog\| | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L192` |
| Information | START:DbServiceSbusController\|SbusWinFunctionalities | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L201` |
| Information | START:DbServiceSbusController\|AzureGetExportParams | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L231` |
| Information | START:DbServiceSbusController\|AzureReadVesselList | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L264` |
| Information | START:DbServiceSbusController\|AzureUpdateUploadFile | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L272` |
| Information | START:DbServiceSbusController\|AzureGetPendingUploadFile | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L280` |
| Information | START:DbServiceSbusController\|AzureGetTransferType | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L288` |
| Information | START:DbServiceSbusController\|AzureGetTransferLocation | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L296` |
| Information | START:DbServiceSbusController\|AzureUpdateUploadFileBulk | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L304` |
| Information | START:DbServiceSbusController\|AzureGetAzureSettings | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L312` |
| Information | START:DbServiceSbusController\|AzureGetSettings | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L320` |
| Information | START:DbServiceSbusController\|AzureErrorLog | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L328` |
| Information | DbServiceSbuscontroller.ReadAzureFileDownloadQ | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L344` |
| Debug | DbServiceSbuscontroller.ReadUpdateAzureDownloadQ | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L352` |
| Information | DbServiceSbuscontroller.UpdateAzureFileDownloadQ | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L360` |
| Debug | {MethodName}\|Started  | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L369` |
| Information | START:DbServiceSbusController\|GetCredentialsSettingsV2V | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L379` |
| Information | START:DbServiceSbusController\|AzureGetSettingsV2V | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L387` |
| Information | START:DbServiceSbusController\|SbusWinInsertSbusNotificationV2V | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L395` |
| Information | START:DbServiceSbusController\|GetReceiverQueueNameForVesselV2V | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L404` |
| Information | START:DbServiceSbusController\|SaveMasterLogV2V\|Input:{JsonConvert.SerializeObject} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L412` |
| Information | START:DbServiceSbusController\|GetTrackChangeDetailsV2V\|Input:{JsonConvert.SerializeObject} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L481` |
| Information | START:DbServiceSbusController\|GetV2VMasterLogData\|Input:{JsonConvert.SerializeObject} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L489` |
| Information | START:DbServiceSbusController\|GetV2VAutoResendData | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L500` |
| Information | START:DbServiceSbusController\|UpdateV2VResendLog\|Input : {JsonConvert.SerializeObject} | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L508` |
| Information | START:DbServiceSbusController\|SaveAzureResUploadData | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L562` |
| Information | START:DbServiceSbusController\|SaveChatMessageToQueue | `RepDBLogW/MariApps.PAL.Rep.DBlogW.Service/Controllers/DbServiceSbusController.cs#L674` |

## RepDecompress

Logger templates in RepDecompress. Keywords: RepDecompress log, error.

| Level | Message template | Source |
|---|---|---|
| Information | Executing UpdateMissingPacketById + {missingId} {status} | `RepDecompress/MariApps.PAL.Rep.Decompress.DAL/DecompressRepository.cs#L254` |
| Error | Error while executing Update Missing Packet Status\|MESSAGE: {ex.Message}\|StackTrace: {ex.StackTrace} | `RepDecompress/MariApps.PAL.Rep.Decompress.DAL/DecompressRepository.cs#L270` |
| Error | Error in AcquisitionRepository.SaveV2VMIssingPacketRecords | `RepDecompress/MariApps.PAL.Rep.Decompress.DAL/DecompressRepository.cs#L389` |
| Error | Error in CommonDecompressOpsBL\|DecompressFileLZMA | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L67` |
| Information | {MethodName}\| Unzipping the file: {InFile} to {OutFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L76` |
| Throw:InvalidDataException | Invalid LZMA header: too short | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L90` |
| Throw:EndOfStreamException | Unexpected end of file while reading size. | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L100` |
| Information | {MethodName}\| Successfully decompressed: {InFile} to {OutFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L109` |
| Error | {MethodName}\| File I/O error during decompression: {InFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L116` |
| Error | {MethodName}\| Invalid data error during decompression: {InFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L120` |
| Error | {MethodName}\| Unexpected Exception during decompression: {InFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L124` |
| Error | Error in CommonDecompressOpsBL.TarDecompression | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L184` |
| Information | {MethodName}\| Unzipping the file: {InputFile} to {OutputDirectory} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L194` |
| Warning | {MethodName}\| Skipping suspicious entry outside output directory: {EntryKey} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L222` |
| Warning | {MethodName}\| Extraction attempt {Attempt}/{MaxAttempts} failed with I/O error, retrying in {DelayMs}ms: {Message} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L261` |
| Error | {MethodName}\| All {MaxAttempts} extraction retry attempts failed for file {InputFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L270` |
| Debug | {MethodName}\| Files read from TAR: {FileCount} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L281` |
| Critical | {MethodName}\| I/O error during TAR extraction: {InputFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L317` |
| Critical | {MethodName}\| Permission error while extracting: {InputFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L322` |
| Critical | {MethodName}\| Unexpected error during TAR extraction: {InputFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L327` |
| Error | Error in CommonDecompressOpsBL.DecompressNormalZip | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L385` |
| Debug | {MethodName} initiated | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L394` |
| Information | {MethodName}\| Extracted tar.zst archive to {OutputFolder} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L419` |
| Debug | {MethodName} Files extracted to {ExtractPath} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L427` |
| Error | {MethodName} Files extracted error, extractPath: {ExtractPath}, Message:{Message} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L433` |
| Information | {MethodName}\| Converting MessagePack files to JSON format in folder: {FolderPath} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L443` |
| Information | {MethodName}\| Converted {MsgPackFile} to {JsonFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L466` |
| Error | {MethodName}\|  Error converting MessagePack file to JSON: {MsgPackFile} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L472` |
| Error | {MethodName}\| Error during MessagePack to JSON conversion in folder: {FolderPath} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L480` |
| Debug | {MethodName}\|CHECKING IF FILE IS BEING USED\| CHECK Count {CheckCount} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L502` |
| Information | {MethodName}\|File:{FileName} is being used waiting for {WaitTime} milliseconds\| CHECK Count {CheckCount} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L506` |
| Error | Exception in {MethodName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L520` |
| Error | {MethodName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L537` |
| Error | Error in CommonDecompressOpsBL.DeleteDirectory | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L558` |
| Debug | {MethodName}\| Directory created: {Directory} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L567` |
| Information | INFO: AcquisitionController \| Acquire \| AcquireFiles \| ClearOldFiles\| CHECKING DIRECTORY {file} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L574` |
| Error | Error in CommonDecompressOpsBL.ClearOldFiles | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L593` |
| Warning | {MethodName}\| Failed to delete existing destination file {File}, will attempt overwrite: {Message} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L619` |
| Error | {MethodName}\| Failed to copy file {Source} after {Attempts} attempts | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L642` |
| Warning | {MethodName}\| Copy attempt {Attempt}/{MaxAttempts} failed for {Source}, retrying in {DelayMs}ms: {Message} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L647` |
| Error | {MethodName}\| Failed to delete source file {Source} after {Attempts} attempts | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L671` |
| Warning | {MethodName}\| Delete attempt {Attempt}/{MaxAttempts} failed for {Source}, retrying in {DelayMs}ms | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L676` |
| Error | {MethodName}\| Creating original copy of extraction files failed for count {Count} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L694` |
| Debug | {MethodName}\| Created copy of orignal files to extract | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L700` |
| Error | {MethodName}\| Error while copying files from {Source} to {Destination} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L706` |
| Debug | {MethodName}\| Directory path is null or empty, nothing to delete | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L717` |
| Error | {MethodName}\| Failed to delete file: {FilePath} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L736` |
| Error | {MethodName}\| Failed to delete subdirectory: {SubDirPath} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L749` |
| Error | {MethodName}\| Failed to delete directory and its contents: {DirectoryPath} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/CommonDecompressOpsBL.cs#L758` |
| Information | {MethodName}\| Starting to process for Vessel {VesselObjectId} and Packet Counter {PacketCounter} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L41` |
| Critical | {MethodName}\| Base folder could not be found, exiting the process | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L51` |
| Throw:InvalidOperationException | Base folder is not set. | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L52` |
| Critical | {MethodName}\| Could not create working copy of split files | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L77` |
| Information | {MethodName}\| Extracting {FileName} contents | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L101` |
| Critical | {MethodName}\| Extraction failed for {FileName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L118` |
| Critical | {MethodName}\| Extraction aborted for {FileName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L125` |
| Information | {MethodName}\| File content for {FileName} was extracted successfully | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L176` |
| Information | {MethodName}\| Extracted files to be processed further: {Count} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L180` |
| Warning | {MethodName}\| Some files in the manifest are missing in the extracted files: {MissingFiles} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L222` |
| Information | {MethodName}\| Table Settings ID fetched for Packet Header file {FileName} is {TableSettingsId} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L243` |
| Information | {MethodName}\| Table Settings ID fetched for Packet Info file {FileName} is {TableSettingsId} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L265` |
| Debug | {MethodName}\| Deleted original file {FileName} after extraction | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L282` |
| Information | {MethodName}\| Extraction completed successfully for {VesselObjectId} and packet counter {PacketCounter} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L286` |
| Error | {MethodName}\| No files were extracted for {VesselObjectId} and packet Counter {PacketCounter} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L292` |
| Critical | Exception in {MethodName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L309` |
| Information | {MethodName}\| Extracting packet from {FileName} to {UnzipDirectory} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L334` |
| Warning | {MethodName}\| Skipping non-archive file with extension {Extension}: {FileName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L341` |
| Throw:InvalidDataException | The extension {param.FileExtension} is not valid for extraction | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L365` |
| Error | {MethodName}\| No files extracted from {FileName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L370` |
| Information | {MethodName}\| Files extracted successfully from {FileName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L377` |
| Information | START:DecompressController\|PacketExtract\|DecompressFile | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L397` |
| Error | ERROR:PacketCreationController\|GeneratePackets\|GeneratePackets\|Message:{decompressInput.ErrorMessage} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L414` |
| Information | Decompressing file: {item.FileName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L429` |
| Information | Extracting File Path: {item.FileNameLocation} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L446` |
| Information | File Extracted Successfully: {item.FileName} for communication type {channelRecord.CommunicationType} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L466` |
| Information | INFO: Moving Error file back to INBOX\|File: {item.FileName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L509` |
| Information | Moving error file back to inbox {Path.Combine} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L527` |
| Information | MOving error file to inbox{fileInfo.FullName} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L540` |
| Information | ERROR:DecompressController\|PacketExtract\|DecompressFile\|Extracting Zipfile error | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L546` |
| Error | ERROR:DecompressController\|PacketExtract\|DecompressFile\|Message:{decompressInput.ErrorMessage} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L550` |
| Information | INFO:DecompressController\|PacketExtract\|DecompressFile\|MESSAGE: FILE EXTRACTED | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L558` |
| Information | Extracted file status \|File Name: {check.Name}\|Status = {status} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L620` |
| Error | ERROR: ERROR WHILE INSETING TO DT TABLE{item.InPacketHdId} {item.FileName}\|Error Message: {ex.Message} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L637` |
| Information | FINISHED:DecompressController\|PacketExtract\|DecompressFile\|MESSAGE: FILE EXTRACTED | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L695` |
| Error | ERROR:DecompressController\|PacketExtract\|DecompressFile\| Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L706` |
| Information | INFO:DecompressController\|PacketExtract\|DecompressFile\|DirectoryCreated\| {path} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L755` |
| Error | ERROR:TransferController\|TransferPacket\|MoveFile\|Message{decompressInput.ErrorMessage} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L821` |
| Error | ERROR:TransferController\|TransferPacket\|MoveFile\|Message:{decompressInput.ErrorMessage} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L838` |
| Information | SUCCESS:DecompressController\|PacketExtract\|DecompressFile\|MESSAGE: FILE EXTRACTED | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L858` |
| Information | ERROR:DecompressController\|PacketExtract\|DecompressFile\| Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L870` |
| Information | Extracting file: {fi.Name} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L882` |
| Throw:ArgumentNullException | File list is null or empty | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L897` |
| Error | Error in 7z file  | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L902` |
| Error | Error in tar file  | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L923` |
| Throw:InvalidDataException | The extension {fi.Extension} is not valid for extraction | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L941` |
| Error | ERROR:DecompressController\|PacketExtract\|DecompressFile\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L951` |
| Error | ERROR:DecompressController\|PacketExtract\|DecompressFileLZMA\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/DecompressBL.cs#L989` |
| Error | ERROR:DecompressController\|ValidateData\|Message:{inputBO.ErrorMessage} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/ValidateBL.cs#L29` |
| Debug | {MethodName}\| Starting validation for input {Json} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/ValidateBL.cs#L80` |
| Error | {MethodName}\| Input is null | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/ValidateBL.cs#L84` |
| Critical | {MethodName}\| ImportQId is 0 | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/ValidateBL.cs#L94` |
| Critical | {MethodName}\| VesselObjectId is 0 | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/ValidateBL.cs#L104` |
| Critical | {MethodName}\| SplitFiles is null or empty | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/ValidateBL.cs#L114` |
| Error | {MethodName}\| FileLocation is null or file does not exist | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/ValidateBL.cs#L124` |
| Debug | {MethodName}\| Validation successful | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/BL/ValidateBL.cs#L134` |
| Information | START:DecompressController\|PacketExtract\| input json: {JsonConvert.SerializeObject} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/Controllers/DecompressController.cs#L46` |
| Information | END:DecompressController\|PacketExtract\|output Json: {JsonConvert.SerializeObject} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/Controllers/DecompressController.cs#L60` |
| Information | ERROR:DecompressController\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/Controllers/DecompressController.cs#L73` |
| Debug | {MethodName}\| Process Started | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/Controllers/DecompressController.cs#L84` |
| Error | {MethodName}\| Invalid Request | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/Controllers/DecompressController.cs#L90` |
| Debug | {MethodName}\| Request completed with status :{Status} | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/Controllers/DecompressController.cs#L100` |
| Information | START:DecompressController\|TestService | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/Controllers/DecompressController.cs#L109` |
| Information | START:DecompressController\|GetVersion | `RepDecompress/MariApps.PAL.Rep.Decompress.Service/Controllers/DecompressController.cs#L117` |

## RepFileMerge

Logger templates in RepFileMerge. Keywords: RepFileMerge log, error.

| Level | Message template | Source |
|---|---|---|
| Error | Error while executing Update Missing Packet Status\|MESSAGE: {ex.Message}\|StackTrace: {ex.StackTrace} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.DAL/FileMergeRepository.cs#L71` |
| Information | {MethodName}\| Merging file {FileName} at location {MergeLocation} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L29` |
| Debug | {MethodName}\| Merging file {FileName} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L39` |
| Information | {MethodName}\| Finished combining all split files into {MergeFileName} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L55` |
| Error | {MethodName}\| IO Exception while combining files | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L63` |
| Error | {MethodName}\| Unauthorized access while combining files | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L67` |
| Error | {MethodName}\| General Exception in combining files | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L71` |
| Debug | {MethodName}\|CHECKING IF FILE IS BEING USED\| CHECK Count {CheckCount} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L112` |
| Information | {MethodName}\|File:{FileName} is being used waiting for {WaitTime} milliseconds\| CHECK Count {CheckCount} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L116` |
| Error | Exception in {MethodName} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L130` |
| Error | <ex, methodName)> | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L147` |
| Debug | {MethodName} Moving file {MergedFile} to destination Location {DestinationFolder} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L158` |
| Critical | {MethodName} File {FileName} is locked or not accessible | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L167` |
| Critical | {MethodName} Split File {FileName} is locked or not accessible | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L192` |
| Information | {MethodName} File {FileName} moved to destination location {DestinationFolder} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L195` |
| Error | {MethodName} Exception while moving file {FileName} to destination location {DestinationFolder} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/CommonOperation.cs#L201` |
| Information | START:FileMergeController\|MergeFile\|MergeZipFIle | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L30` |
| Information | File Exist with a merge name:{mergeExist.Name} at :{mergeExist.FullName}Deleting | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L73` |
| Information | File Exist with a merge name:{mergeExist.Name} at :{mergeExist.FullName} file is locked | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L78` |
| Information | SUCCESS:FileMergeController\|MergeFile\|MergeZipFIleFileMerged | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L87` |
| Information | ERROR:FileMergeController\|MergeFile\|MergeZipFIleFileMerged\|Extracting Zipfile error | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L109` |
| Error | ERROR:FileMergeController\|MergeFile\|MergeZipFIle\|Message: Error while moving to error folder\| Message:{ex.Message} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L124` |
| Error | ERROR:FileMergeController\|MergeFile\|MergeZipFIle\|Message:{mergeInput.ErrorMessage} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L134` |
| Error | ERROR:FileMergeController\|MergeFile\|MergeZipFIle\|Message:{mergeInput.ErrorMessage}\| STACKTRACE :{ex.StackTrace} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L156` |
| Information | Marking Pending file as Pending and moving it to Inbox | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L169` |
| Information | INFO: FILE MERGE SERVICE\| MOVING PENDING FILES TO Inbox Location\|File: {failedRecords.FileName} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L176` |
| Error | ERROR:FILE MERGE SERVICE\| ERROR WHILE MOVING PENDING FILES TO Inbox Folder Location\|Error Message: {ex.Message} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L236` |
| Information | END:FileMergeController\|MergeFile\|MergeZipFIle | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L257` |
| Error | ERROR:FileMergeController\|MergeFile\|MergeZipFIle\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L264` |
| Information | {MethodName}\| Starting to process for Vessel {VesselObjectId} and Packet Counter {PacketCounter} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L275` |
| Debug | {MethodName}\| Base folder gotten as input is null or empty | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L282` |
| Critical | {MethodName}\| Base folder could not be found, exiting the process | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L290` |
| Throw:InvalidOperationException | Base folder is not set. | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L291` |
| Debug | {MethodName}\| File Already exists in destination folder deleting it {FileName} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L316` |
| Critical | {MethodName}\| File is being used by another process, exiting the process | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L324` |
| Debug | {MethodName}\| File {FileName} has been merged with status {MergedStatus} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L341` |
| Critical | {MethodName}\| File {FileName} could not be merged | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L345` |
| Information | {MethodName}\| All Split files available for file {FileName}, not merging | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L373` |
| Error | {MethodName}\| Not all split files are available for file {FileName} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L378` |
| Information | {MethodName} File {FileName} has been merged with status {MergedStatus} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L389` |
| Critical | {MethodName} File {FileName} could not be moved to destination location as merged file is missing | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L393` |
| Information | {MethodName} Merge operation has been completed and File {FileName} has been moved to destination location {DestinationLocation} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L404` |
| Warning | {MethodName}\| File {FileName} is no longer accessible while fetching metadata | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L411` |
| Critical | {MethodName}\| Critical exception while merging file | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L437` |
| Information | INFO:FileMergeController\|MergeFile\|MergeZipFIle\|CreateDirectory\| {_Dir} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L479` |
| Error | ERROR:FileMergeController\|MergeFile\|MergeZipFIle\|CreateDirectory\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L485` |
| Information | File Status\| File {fiPart.Name}\| STATUS: {exist} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L502` |
| Information | INFO:FileMergeController\|MergeFile\|MergeZipFIle\|Combinefile\|MESSAGE:File Merge Incomplete FileSize is 0 for {file.FileLocation} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L514` |
| Error | ERROR:FileMergeController\|MergeFile\|MergeZipFIle\|Combinefile\|MESSAGE:FIle is being used by another process {file.FileLocation} or file is not available | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L520` |
| Information | FILE HAS BEEN MERGED\| NEW FILE {mergeLoc} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L528` |
| Information | Deleting file that has been merged: {moveFile.Name} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L537` |
| Information | Moving MERGED FILE FROM MERGE FOLDER TO TEMP FOLDER | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L550` |
| Error | INFO:FileMergeController\|MergeFile\|MergeZipFIle\|Combinefile\|MESSAGE:ERROR WHILE MOVING FILE TO DIRECTORY AFTER COMPRESSION | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L557` |
| Information | INFO:FileMergeController\|MergeFile\|MergeZipFIle\|Combinefile\|MESSAGE:File Merge is Complete | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L563` |
| Information | INFO:FileMergeController\|MergeFile\|MergeZipFIle\|Combinefile\|MESSAGE:File Merge is Incompelete | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L569` |
| Error | ERROR:FileMergeController\|MergeFile\|MergeZipFIle\|Combinefile\|MESSAGE: {ex.Message}\|Stack Trace:{ex.StackTrace} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L578` |
| Information | INFO: AcquisitionController \| Acquire \| AcquireFiles \| ClearOldFiles\| CHECKING DIRECTORY {file} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L586` |
| Error | ERROR:AcquisitionController\|Acquire\|AcquireFiles\|ClearOldFiles\|MESSAGE: ERROR WHILE CLEARING OLD FILES {ex.Message} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L605` |
| Information | Checking file is available:{fi.Name} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L612` |
| Information | File:{fi.Name} CHECKING IF FILE IS BEING USED\| CHECK Count{checkCount} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L621` |
| Information | File:{fi.Name} is being used waiting for couple of seconds\| CHECK Count{checkCount} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L624` |
| Information | The file is being used by another process\|File: {fi.Name}\|Error messasge: {ex.Message} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L647` |
| Information | The file is being used by another process\|File: {file.Name}\| ERROR MESSAGE: {ex.Message} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/FileMergeBL.cs#L662` |
| Error | ERROR:FileMergeController\|ValidateData\|Message:{inputBO.ErrorMessage} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L29` |
| Debug | {MethodName}\| Validating Input {Json} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L86` |
| Critical | {MethodName}\| Input is null | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L90` |
| Critical | {MethodName}\| ImportQId is mandatory | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L100` |
| Error | {MethodName}\| Packet counter is mandatory | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L110` |
| Error | {MethodName}\| Split count is mandatory | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L120` |
| Error | {MethodName}\| VesselObjectId is mandatory | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L130` |
| Error | {MethodName}\| SplitFiles is mandatory | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L140` |
| Warning | {MethodName}\| One or more SplitFiles have empty FileLocation | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L150` |
| Warning | {MethodName}\| One or more SplitFiles are missing. Sample files: {MissingFiles} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L165` |
| Debug | {MethodName}\| Validation Success | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/BL/ValidateBL.cs#L175` |
| Information | START:FileMergeController\|MergeFile \| Input JSON : {JsonConvert.SerializeObject} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/Controllers/FileMergeController.cs#L39` |
| Information | END:FileMergeController\|MergeFile \| Output JSON : {JsonConvert.SerializeObject} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/Controllers/FileMergeController.cs#L44` |
| Error | ERROR:FileMergeController\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/Controllers/FileMergeController.cs#L54` |
| Information | START:FileMergeController\|TestService | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/Controllers/FileMergeController.cs#L91` |
| Information | START:FileMergeController\|GetVersion | `RepFileMerge/MariApps.PAL.Rep.FileMerge.Service/Controllers/FileMergeController.cs#L99` |

## RepIntegration

Logger templates in RepIntegration. Keywords: RepIntegration log, error.

| Level | Message template | Source |
|---|---|---|
| Debug | {MethodName}\| Reading Common CO Parameters values | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L38` |
| Debug | {MethodName}\| Read Common CO Parameters values | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L44` |
| Error | {MethodName} - Error in reading Common CO Parameters values | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L49` |
| Debug | {MethodName}\| Reading all Table Settings | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L58` |
| Debug | {MethodName}\| Reading Channel Flow Details | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L74` |
| Debug | {MethodName}\| Read Channel Flow data count-{Count} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L80` |
| Error | Exception in {MethodName} for type {IsExport} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L84` |
| Debug | {MethodName}\| Reading Channel Details | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L95` |
| Debug | {MethodName}\| Reading all Vessels data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L109` |
| Error | {MethodName}\|Exception occured while reading vessels | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L120` |
| Debug | {MethodName}\| Reading Priority Resend Info | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L129` |
| Error | {MethodName}\|Exception while reading resend Packet | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L144` |
| Debug | {MethodName}\| Saving Transfer Queue Data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L153` |
| Information | {MethodName}\| Transfer Queue Data saved successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L172` |
| Error | {MethodName}\| Error while saving transfer Queue Data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L182` |
| Error | {MethodName}\| Error in saving trasnfer Queue data Items | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L193` |
| Debug | {MethodName}\| Checking if Transfer Queue data exists for status {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L207` |
| Debug | {MethodName}\| Transfer Queue data exists: {DataExists} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L221` |
| Error | {MethodName}\| Error checking if Transfer Queue data exists | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L226` |
| Debug | {MethodName}\| Moving Transfer Queue data to history | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L235` |
| Information | {MethodName}\| Transfer Queue data moved to history successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L253` |
| Error | {MethodName}\| Error while moving Transfer Queue data to history | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L263` |
| Error | {MethodName}\| Error in moving Transfer Queue data to history | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L274` |
| Debug | {MethodName}\| Reading Pending Import Queue Common Type | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L291` |
| Debug | {MethodName}\| Read Pending Import Queue Common Type data count-{Count} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L299` |
| Error | {MethodName}\| Error in reading Pending Import Queue Common Type | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L304` |
| Debug | {MethodName}\| Updating Import Queue Exceed Items | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L313` |
| Error | {MethodName}\| Error in updating Import Queue Exceed Items | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L326` |
| Debug | {MethodName}\| Reading Pending Import Queue | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L334` |
| Debug | {MethodName}\| Read Pending Import Queue data count-{Count} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L347` |
| Error | {MethodName}\| Error in reading Pending Import Queue | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L353` |
| Debug | {MethodName}\| Reading Import Queue Dt table items | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L362` |
| Debug | {MethodName}\| Read Import Queue Dt table items count-{Count} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L376` |
| Error | Exception occured in {MethodName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L382` |
| Debug | {MethodName}\| Saving Import Queue Data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L391` |
| Information | {MethodName}\| Import Queue Data saved | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L411` |
| Error | {MethodName}\| Error while saving Import Queue Data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L421` |
| Error | Exception occured while saving data in {MethodName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L432` |
| Debug | {MethodName}\| Updating Import Queue data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L447` |
| Information | {MethodName}\| Import Queue Data updated successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L467` |
| Error | {MethodName}\| Error while saving updating import Queue Data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L477` |
| Error | {MethodName}\| Error in updating Import Queue data Items | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L488` |
| Debug | {MethodName}\| Updating Import Queue sub items | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L504` |
| Information | {MethodName}\| Import Queue sub details Data updated successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L523` |
| Error | {MethodName}\| Error while saving updating import Queue sub details  Data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L533` |
| Error | {MethodName}\| Error in updating Import Queue sub details  data Items | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L544` |
| Debug | {MethodName}\| Moving Import Queue data to history | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L560` |
| Information | {MethodName}\| Import Queue Data moved to history successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L579` |
| Error | {MethodName}\| Error while  moving import Queue Data to history | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L589` |
| Error | {MethodName}\| Error in moving Import Queue data Items to history | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L600` |
| Debug | {MethodName}\| Fetching data from table {TableName} for {Count} IDs | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L614` |
| Error | {MethodName}\| Table name cannot be null or empty | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L620` |
| Warning | {MethodName}\| No IDs provided for table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L626` |
| Debug | {MethodName}\| Executing query: {Query} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L659` |
| Debug | {MethodName}\| Fetched {RowCount} rows from table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L694` |
| Error | {MethodName}\| Error fetching data from table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L700` |
| Debug | {MethodName}\| Inserting {RowCount} rows to table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L708` |
| Error | {MethodName}\| Target table name cannot be null or empty | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L714` |
| Warning | {MethodName}\| No data provided for insertion to table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L725` |
| Information | {MethodName}\| Inserted: {Inserted}, Updated: {Updated} rows to table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L884` |
| Error | {MethodName}\| Error inserting/updating data to table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L895` |
| Debug | {MethodName}\| Validating Import Queue for Vessel {Vsl} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L909` |
| Debug | {MethodName}\| Validated Import Queue for Vessel {Vsl} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L924` |
| Error | {MethodName}\| Exception while validating Import Queue for Vessel {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L929` |
| Debug | {MethodName}\| Saving pr rep in packet dt data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L998` |
| Information | {MethodName}\| Pr Rep In Packet dt data saved successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1017` |
| Error | {MethodName}\| Error while  saving Pr rep in packet dt data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1027` |
| Error | {MethodName}\| Error in saving Pr rep in packet dt data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1038` |
| Debug | {MethodName}\| Updatin Pr Rep In Packet data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1053` |
| Error | {MethodName}\| Exception in updating Pr Rep In Packet data | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1081` |
| Debug | {MethodName}\| Updating missing packet info | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1090` |
| Debug | {MethodName}\| Missing packet info update successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1108` |
| Error | {MethodName}\| Error updating missing packet info | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1113` |
| Debug | {MethodName}\| Reading Track Records for {Count} channels | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1121` |
| Debug | {MethodName}\| Read {ResultCount} Track Records | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1135` |
| Error | {MethodName}\| Error reading Track Records | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1140` |
| Debug | {MethodName}\| Updating records status to {Status} for {Count} records | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1149` |
| Information | {MethodName}\| Records status updated successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1161` |
| Error | {MethodName}\| Error updating records status | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1166` |
| Debug | {MethodName}\| Fetching pending priority packets for channel flow data: {ChannelFlowData} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1175` |
| Debug | {MethodName}\| Fetched {Count} pending priority packets | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1186` |
| Error | {MethodName}\| Error while fetching pending priority packets | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1193` |
| Debug | {MethodName}\| Checking for priority track exceed | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1202` |
| Debug | {MethodName}\| Priority track exceed check completed successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1207` |
| Error | {MethodName}\| Error while checking priority track exceed | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1211` |
| Debug | {MethodName}\| Fetching priority track records for channel IDs: {ChannelIds} and vessel IDs: {VesselIds} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1218` |
| Debug | {MethodName}\| Fetched {Count} priority track records | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1230` |
| Error | {MethodName}\| Error while fetching priority track records | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1236` |
| Debug | {MethodName}\| Updating priority track status for operation type: {OperationType} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1244` |
| Debug | {MethodName}\| Priority track status updated successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1255` |
| Error | {MethodName}\| Error while updating priority track status | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1259` |
| Debug | {MethodName}\| Updating PR track record status for {HdCount} header records and {DtCount} detail records | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1266` |
| Debug | {MethodName}\| PR track record status updated successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1278` |
| Error | {MethodName}\| Error while updating PR track record status | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1283` |
| Debug | {MethodName}\| Updating PR Packet Status for {Count} records | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1291` |
| Information | {MethodName}\| PR Packet Status updated successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1310` |
| Error | {MethodName}\| Error while updating PR Packet Status: {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1315` |
| Error | {MethodName}\| Error updating PR Packet Status | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1322` |
| Debug | {MethodName}\| Reading Pending Packet Info for VesselObjectId: {VesselObjectId} with fetch count: {FetchCount} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1330` |
| Debug | {MethodName}\| Read {ResultCount} Pending Packet Info records | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1344` |
| Error | {MethodName}\| Error reading Pending Packet Info | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationNewRepository.cs#L1349` |
| Error | DL GetExportParams \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L54` |
| Error | DL GetRecordDetails \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L77` |
| Error | DL GetIsVessel \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L108` |
| Error | DL GetAllTableSettings \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L142` |
| Information | {MethodName} \| Started | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L153` |
| Information | {MethodName} \| Pending Records fetched with Count: {PendingRecordsCount} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L201` |
| Information | {MethodName}\| TableSettingsList fetched with Count: {TableSettingsListCount} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L221` |
| Information | {MethodName}\| RecordList fetched with Count: {RecordListCount} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L244` |
| Information | {MethodName}\| VesselObjectId and DestinationList fetched | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L273` |
| Error | Error in {MethodName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L282` |
| Error | DL GetChannelFlowSettings \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L354` |
| Error | DL UpdateLastExportDate \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L376` |
| Error | Error in AcquisitionRepository.GetCurrentEnvironmentDetails | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L484` |
| Error | Error in GetActiveVesselForCurrentEnvironment | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L513` |
| Information | {MethodName} Fetching Transfer Channel Id for Transfer Name: {TransferName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L525` |
| Error | Error in {MethodName} with param {TransferChannelName} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L552` |
| Throw:DataException | Data did not save Successfully | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L576` |
| Error | IntegrationRepository.SaveTransferQueueData | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L582` |
| Throw:DataException | <outputData[1].Value.ToString())> | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L607` |
| Error | IntegrationRepository.UpdateTransferQueueData | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L613` |
| Error | IntegrationRepository.ReadAzureResData | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L677` |
| Error | IntegrationRepository.SaveTableNotifQueeu | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L706` |
| Error | IntegrationRepository.UpdateTableNotifQueue | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L737` |
| Error | IntegrationRepository.ReadTableNotifQueueData | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L789` |
| Error | IntegrationRepository.ReadChannelFromTableSettingsId | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L824` |
| Error | IntegrationRepository.ValidateandReadQueueData | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L867` |
| Error | IntegrationRepository.ReadMessageNotifQueueData | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L972` |
| Error | IntegrationRepository.UpdateMessageNotifQueueData | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/IntegrationRepository.cs#L1003` |
| Error | {_methodNamePrefix} : DI Constructor -> DefaultConnection is not configured / loaded properly | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L30` |
| Error | {methodName} : the script supplied is empty or null, nothing to proceed with | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L46` |
| Throw:InvalidOperationException | Script supplied is empty or null, nothing to proceed with | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L47` |
| Error | {methodName} : DefaultConnection is not configured, cannot proceed | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L52` |
| Throw:InvalidOperationException | DefaultConnection is not found in configuration | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L53` |
| Throw:InvalidOperationException | maxRowCount is set to 0; which will let the row count to unlimited; | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L68` |
| Information | {methodName} : Executing SQL Script, length {script.Length}, maxRowCount = {maxRowCount}, maxResultSet = {maxResultSets} and maxExecutionTimeSecond = {maxExecutionTimeSeconds} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L108` |
| Warning | {methodName} : MaxResultSets {maxResultSets} reached, remaining results will be capped | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L118` |
| Warning | {methodName} : MaxRowCount {maxRowCount} reached on result set {resultSetIndex}, remaining rows discarded | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L135` |
| Information | {methodName} : Script executed successfully, {resultSets.Count} result set(s) | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L173` |
| Warning | {methodName} : Execution exceeded the {maxExecutionTimeSeconds}s limit and was cancelled | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L184` |
| Throw:TimeoutException | Script execution exceeded the configured limit of {maxExecutionTimeSeconds} | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L185` |
| Warning | {methodName} : Script execution cancelled by cancellation request | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L188` |
| Throw:TaskCanceledException | Script execution cancelled by cancellation request | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L189` |
| Error | {methodName} : Error occurred while executing script. | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L192` |
| Error | {methodName} : No batches supplied, nothing to execute | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L208` |
| Throw:InvalidOperationException | No script batches supplied, nothing to execute | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L209` |
| Information | {methodName} : executing batch {i + 1} of {batches.Count} against [{connection.Database}] | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L242` |
| Warning | {methodName} : execution exceeded the {maxExecutionTimeSeconds}s limit and was cancelled | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L250` |
| Warning | {methodName} : execution cancelled by cancellation request | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L255` |
| Error | {methodName} : error occurred while executing script batches. | `RepIntegration/MariApps.PAL.Rep.Integration.DAL/ScriptExecutionRepository.cs#L260` |
| Information | {MethodName}\|File deleted successfully: {FilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/CommonOperationBL.cs#L25` |
| Warning | {MethodName}\|Directory not found: {DirectoryPath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/CommonOperationBL.cs#L30` |
| Error | {MethodName}\|Error occurred while cleaning directories | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/CommonOperationBL.cs#L36` |
| Warning | {MethodName}\|File not found: {FilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/CommonOperationBL.cs#L54` |
| Error | {MethodName}\|Error occurred while deleting files | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/CommonOperationBL.cs#L60` |
| Information | {MethodName}\| Started, deep:{Deep}, categories:{Categories} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ConfigEvaluation/ConfigEvaluationService.cs#L129` |
| Information | {MethodName}\| Completed in {Duration} ms, pass:{Pass} warning:{Warning} fail:{Fail} skipped:{Skipped} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ConfigEvaluation/ConfigEvaluationService.cs#L177` |
| Error | {MethodName}\| Database not reachable | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ConfigEvaluation/ConfigEvaluationService.cs#L218` |
| Warning | {MethodName}\| {Category} check {Code} could not run | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ConfigEvaluation/ConfigEvaluationService.cs#L566` |
| Throw:InvalidOperationException | Get-ScheduledTask failed: {ConfigEvaluationRules.Trim} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ConfigEvaluation/MachineProbe.cs#L119` |
| Throw:InvalidOperationException | {fileName} did not start | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ConfigEvaluation/MachineProbe.cs#L226` |
| Throw:TimeoutException | {fileName} did not finish in {ProcessTimeout.TotalSeconds:0} s | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ConfigEvaluation/MachineProbe.cs#L239` |
| Information | {MethodName}\| Initiating process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L49` |
| Debug | {MethodName}\| Initiating Common data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L53` |
| Debug | {MethodName}\| CommonInitTime set with status {InitStatus} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L76` |
| Information | {MethodName}\| Process status added to memory store witht status {AddStatus} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L78` |
| Error | {MethodName} - Error in initiating process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L82` |
| Debug | {MethodName}\| Setting data in cache for key {Key} with result {Result} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L107` |
| Warning | {MethodName}\| Required keys not found in fetched data {Keys} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L111` |
| Debug | {MethodName}\| Reading Vessel Data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L129` |
| Debug | {MethodName}\| Vessel Data found in DB, adding same to cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L138` |
| Debug | {MethodName}\| Vessel Data added to cache with status {Result} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L140` |
| Critical | {MethodName}\| Vessel Data not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L144` |
| Debug | {MethodName}\| Reading Vessel Data completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L148` |
| Error | {MethodName} - Error in reading Vessel Data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L154` |
| Debug | {MethodName}\| Reading Priority Table Settings | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L164` |
| Debug | {MethodName}\| Table Settings Id found in DB, adding same to cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L172` |
| Debug | {MethodName}\| Table Settings Id added to cache with status {Result} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L174` |
| Critical | {MethodName}\| Table Settings Id not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L178` |
| Debug | {MethodName}\| Reading Priority Table Settings completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L182` |
| Error | {MethodName} - Error in reading Priority Table Settings | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L187` |
| Debug | {MethodName}\| Channel Details found in DB, adding same to cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L207` |
| Debug | {MethodName}\| Channel details added to cache with status {Result} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L209` |
| Critical | {MethodName}\| Channel details not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L213` |
| Debug | {MethodName}\| Reading Priority channel details completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L217` |
| Error | {MethodName} - Error in reading Priority Channel Details | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L222` |
| Debug | {MethodName}\| Reading Import Channel flow Details | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L231` |
| Critical | {MethodName}\| Channel flow information could not be found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L270` |
| Debug | {MethodName}\| Import Channel Flow Details found in DB, adding same to cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L276` |
| Debug | {MethodName}\| Import Channel Flow details added to cache with status {Result} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L278` |
| Critical | {MethodName}\| Import Channel details not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L282` |
| Debug | {MethodName}\| Reading Priority import channel flow details completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L286` |
| Error | {MethodName} - Error in reading Priority Import Channel Details | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L291` |
| Debug | {MethodName}\| Reading Export Channel flow Details | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L300` |
| Critical | {MethodName}\| Export Channel flow information could not be found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L339` |
| Debug | {MethodName}\| Export Channel Flow Details found in DB, adding same to cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L345` |
| Debug | {MethodName}\| Export Channel Flow details added to cache with status {Result} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L347` |
| Critical | {MethodName}\| Export Channel details not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L351` |
| Debug | {MethodName}\| Reading Priority Export channel flow details completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L355` |
| Error | {MethodName} - Error in reading Priority Export Channel Details | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L360` |
| Information | {MethodName}\| Setting Transfer Resend Run time | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L369` |
| Information | {MethodName}\| Setting Vessel Settings Update Time | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L388` |
| Information | {MethodName}\| Setting Common Init Time | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L406` |
| Debug | {MethodName}\| Reading Service Status | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L427` |
| Critical | {MethodName}\| Service Status not found in cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L433` |
| Debug | {MethodName}\| Reading All Vessels | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L443` |
| Error | {MethodName}\| Vessel Data not found in cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L451` |
| Debug | {MethodName}\| Reading updated data from memory store | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L457` |
| Error | Exception in {MethodName} while reading vessel data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L478` |
| Debug | {MethodName}\| Reading Common Param Values | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L487` |
| Error | {MethodName}\| Common Param Data not found in cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L495` |
| Debug | {MethodName}\| Reading updated data from memory database | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L501` |
| Critical | {MethodName}\| Common Param Data not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L505` |
| Error | Exception in {MethodName} while reading common param data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L514` |
| Error | {MethodName}\| Channel Data not found in cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L531` |
| Critical | {MethodName}\| Channel Data not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L542` |
| Error | Exception in {MethodName} while reading channel data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L551` |
| Debug | {MethodName}\| Filtering Table Settings | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L560` |
| Critical | {MethodName}\| Table Settings not found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L566` |
| Critical | {MethodName}\| Table Settings not found for TableSettingsId:{TableSettingsId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L573` |
| Debug | {MethodName}\| Reading Table Settings | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L584` |
| Error | {MethodName}\| Table settings Data not found in cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L592` |
| Critical | {MethodName}\| Table settings Data not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L603` |
| Debug | {MethodName}\| Reading Table Settings completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L608` |
| Error | {MethodName}\| Exception while reading tbale settings | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L613` |
| Debug | {MethodName}\| Reading Channel Flow Settings | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L622` |
| Error | {MethodName}\| Channel Flow Settings Data not found in cache | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L631` |
| Debug | {MethodName}\| Reading updated data from database | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L637` |
| Critical | {MethodName}\| Channel Flow settings Data not found in DB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L642` |
| Debug | {MethodName}\| Reading Channel Flow Settings completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L647` |
| Error | {MethodName}\| Exception while reading channel flow settings | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L652` |
| Debug | {MethodName}\| Filtering Channel by Name | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L665` |
| Critical | {MethodName}\| Channel Details not found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L671` |
| Debug | {MethodName}\| Filtering Param Value | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L682` |
| Critical | {MethodName}\| Value not found for key {KeyName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L690` |
| Debug | {MethodName}\| Filtering Channel Flow | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L700` |
| Critical | {MethodName}\| Channel Flow settings not found for ChannelId:{ChannelId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L709` |
| Debug | {MethodName}\| Reading vessel settings | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L718` |
| Critical | {MethodName}\| Vessel data not found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L724` |
| Critical | {MethodName}\| Vessel data not found for VesselObjectId:{VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L731` |
| Debug | {MethodName}\| Reading Vessel Resend Data for all vessel or specific Vessel - {Vessel} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L746` |
| Error | {MethodName}\| MissingAt value is null or empty | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L759` |
| Error | {MethodName}\| Vessel data not found in memory or database | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L765` |
| Debug | {MethodName}\| Vessel Resend Data read completed with {Count} items | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L803` |
| Error | Exception in {MethodName} when checking resend data for {Vessel} or all | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L820` |
| Debug | {MethodName}\| Reading General Packet Resend Data for all vessel or specific Vessel - {Vessel} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L829` |
| Debug | {MethodName}\| General Packet Resend Data read completed with {Count} items | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L840` |
| Error | Exception in {MethodName} when checking general resend data for {Vessel} or all | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L845` |
| Information | {MethodName}\| Saving Transfer Queue Data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L854` |
| Information | {MethodName}\| Checking if Transfer Queue data exists for status {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L865` |
| Information | {MethodName}\| Moving Transfer Queue data to history | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L874` |
| Debug | {MethodName}\| Reading Last Common Init Ready time | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L916` |
| Debug | {MethodName}\| Last Common Init Time read from memory with time {LastInitTime} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L920` |
| Information | {MethodName}\| Last Common Init Time not found, continuing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L924` |
| Information | {MethodName}\| Current Time is less than {RetryThresholdinMin} minutes, waiting | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L929` |
| Debug | {MethodName}\|Current Time is greater than {RetryThresholdinMin} minutes, continuing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L934` |
| Debug | {MethodName}\| Reading Last resend time | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L943` |
| Debug | {MethodName}\| Last packet resend time from memory with time {LastInitTime} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L947` |
| Information | {MethodName}\| Last resend time not found, continuing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L951` |
| Information | {MethodName}\| Last resend time is older than {Time} hour | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L956` |
| Debug | {MethodName}\|Last resend already run at {Time} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L961` |
| Debug | {MethodName}\| Reading Last vessel settings update time | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L972` |
| Debug | {MethodName}\| Last vessel settings update time read from memory with time {LastInitTime} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L976` |
| Information | {MethodName}\| Last vessel settings update time not found, continuing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L980` |
| Information | {MethodName}\| Last vessel settings update time is older than 7 days | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L985` |
| Debug | {MethodName}\|Vessel settings were already updated today | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L990` |
| Debug | {MethodName}\| Reading Current Client Details | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L999` |
| Debug | {MethodName}\| Reading Current Client Details completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L1010` |
| Debug | {MethodName}\| Reading V2V Office Queue Name | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L1017` |
| Debug | {MethodName}\| V2V Office Queue Name read successfully | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L1022` |
| Error | {MethodName}\| Error reading V2V Office Queue Name | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L1027` |
| Debug | {MethodName}\| Sending Generic Notification | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L1039` |
| Debug | {MethodName}\| Generic Notification sent successfully | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L1044` |
| Error | {MethodName}\| Error sending Generic Notification | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L1049` |
| Debug | {MethodName}\| Updating Export Type for Vessel {VesselObjectId} to {ExportType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/CommonDataConduit.cs#L1061` |
| Information | {MethodName} \| Started reading track records (slim) for {ChannelCount} channels | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L59` |
| Information | {MethodName} \| No track records found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L66` |
| Debug | {MethodName} \| Retrieved {RecordCount} track records from database | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L70` |
| Information | {MethodName} \| Successfully processed {PendingRecordsCount} pending records (slim) | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L123` |
| Error | {MethodName} \| Error occurred while reading track records (slim) | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L128` |
| Information | {MethodName}\| Reading pending priority packets for channel flow data mapper : {ChannelFlowDataMapper} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L137` |
| Information | {MethodName}\| Checking for priority track exceed conditions | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L146` |
| Information | {MethodName}\| Reading priority track records for channel IDs : {ChannelIds} and vessel IDs : {VesselIds} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L157` |
| Information | {MethodName}\| Updating priority track status for operation type : {OperationType} and data : {DataToUpdate} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L171` |
| Information | {MethodName}\| Updating PR track record status for HD records count: {HdCount} and DT records count: {DtCount} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L180` |
| Debug | {MethodName} \| Updating status to {Status} for {Count} records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L197` |
| Error | {MethodName} \| Error occurred while updating records status | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L210` |
| Debug | {MethodName} \| Reading pending packet info for VesselObjectId: {VesselObjectId} with fetch count: {FetchCount} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L222` |
| Debug | {MethodName} \| Retrieved {Count} pending packets for VesselObjectId: {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L226` |
| Error | {MethodName} \| Error occurred while reading pending packet info for VesselObjectId: {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L232` |
| Debug | {MethodName} \| Updating packet status for {Count} records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L241` |
| Debug | {MethodName}\| Starting GeneratePacket with input {InputJson} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L250` |
| Error | {MethodName}\| Error occurred while generating packet | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L257` |
| Debug | {MethodName}\| Starting ZipBatch with input {InputJson} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L269` |
| Error | {MethodName}\| Error occurred while zipping batch | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L276` |
| Debug | {MethodName}\| Starting ReadCompressionType with vesselList | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L290` |
| Debug | {MethodName}\| Processing VesselObjectId: {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L296` |
| Debug | {MethodName}\| Cache hit for VesselObjectId: {VesselObjectId} with CompressionType: {CompressionType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L304` |
| Debug | {MethodName}\| Cached CompressionType for VesselObjectId: {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L326` |
| Debug | {MethodName}\| Completed ReadCompressionType with {Count} records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L330` |
| Error | {MethodName}\| Error in ReadCompressionType | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L335` |
| Debug | {MethodName}\| Starting GeneratePacketAsync with input {InputJson} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L343` |
| Debug | {MethodName}\| Starting HandlePriorityTransfer with input {InputJson} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L362` |
| Error | {MethodName}\| Error occurred while handling priority transfer | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ExportDataConduit.cs#L369` |
| Debug | {MethodName}\| Reading Pending items from import Q | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L57` |
| Debug | {MethodName}\| Read {Count} items from import Q | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L80` |
| Error | {MethodName}\| Error occurred while reading pending items from import Q | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L85` |
| Debug | {MethodName}\| Starting insert/upsert for table {TableName} with {RowCount} rows | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L292` |
| Information | {MethodName}\| Insert/upsert completed for table {TableName}. Status: {Status}, Message: {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L319` |
| Error | {MethodName}\| Exception during insert/upsert for table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L324` |
| Debug | {MethodName}\| Saving Packet Details | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L344` |
| Debug | {MethodName}\| Successfully saved {Count} packet details | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L358` |
| Error | {MethodName}\| Failed to save packet details with status: {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L362` |
| Debug | {MethodName}\| Invoking File Merge Process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L396` |
| Debug | {MethodName}\| Invoking Decompress Process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L407` |
| Debug | {MethodName}\| Invoking Acknowledgement Handler | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L417` |
| Debug | {MethodName}\| Initiating Acquisition Process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L426` |
| Debug | {MethodName}\| Invoking Batch Acquisition Process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/DataConduitMethods/ImportDataConduit.cs#L435` |
| Information | {MethodName}\| Process started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L79` |
| Information | {MethodName}\| Process completed with message: {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L95` |
| Information | END:IntegrationController\|ManageServicesExport | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L97` |
| Debug | {MethodName}\| Message:{Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L125` |
| Information | {MethodName}\| Track save is completed with message {Message}\| Invoking export based on Condition {InvokeExportAfterSave} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L128` |
| Information | {MethodName}\| Process completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L132` |
| Information | {MethodName}\| Track save is being processed with Message {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L160` |
| Information | {MethodName}\| Track record save is completed with message {Message}\| Invoking export based on Condition {InvokeExportAfterSave} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L163` |
| Information | {MethodName}\| Process completed with message {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L168` |
| Debug | {MethodName}\| Export process has been started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L207` |
| Debug | {MethodName}\| Export process has been Completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L213` |
| Error | Error in IntegrationBL.GetActiveVessels | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L347` |
| Error | Error in IntegrationBL.GetPriorityAciveVessel | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L372` |
| Error | Error in IntegrationBL.GetPriorityPacketStatus | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L471` |
| Information | {MethodName}\| Transfer Process Initiate is disabled | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L486` |
| Debug | {MethodName}\| Upload process has been started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L517` |
| Information | {MethodName}\| Call back gotten for {Id} and file name {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L565` |
| Error | errror in IntegrationBL.CallTransferQueueAftProcess | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L592` |
| Error | Error in IntegrationBL.TransferPacketFolder | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L620` |
| Information | {MethodName}\| Process started for Vessel {VesselObjectid} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L629` |
| Debug | {0}\| Process started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L663` |
| Error | {MethodName}\| {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L673` |
| Information | {MethodName}\| Started for file {FileName} ({FileSizeInKB} KB) with endpoint key {EndpointKey} to vessels {VesselList} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L690` |
| Error | {MethodName}\| Table settings {TableSettingsId} not found or has no {UrlColumns} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L732` |
| Error | {MethodName}\| Transfer request failed for vessel {VesselObjectId} with message {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L777` |
| Information | {MethodName}\| Transfer {TransferId} queued for vessel {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L781` |
| Error | {MethodName}\| Error while requesting transfer for vessel {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L799` |
| Information | {MethodName}\| Ended with {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L821` |
| Information | {MethodName} \| Should the common initialization process be invoked? Process Init Status: {ProcessInitStatus} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L868` |
| Information | {MethodName}\| Process started invoke status -{Invoke} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L879` |
| Information | {MethodName}\| Transfer Resend process is already running, skipping initiation | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L907` |
| Information | {MethodName}\| Initiating File Resend Process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L918` |
| Information | {MethodName}\| Transfer resend process has not been started, Service Data Status:{ServiceStatus}\| Is resend Process running {ResendStatus}\| next resend time reached: {NextResend} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L923` |
| Debug | {MethodName}\| Transfer Resend has been started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L948` |
| Error | {MethodName} \| Exception occured while invoking priority resend. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L954` |
| Information | {MethodName}\| Initiating General Notification Sending | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L1005` |
| Debug | {MethodName}\| General notificaiton has been started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L1016` |
| Information | {MethodName}\| General notification send process has not been started, Service Data Status:{ServiceStatus}\| Is notif process running {GeneralNotifStatus} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationBL.cs#L1033` |
| Error | Exception in Service_GetQueueCount | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationCommonApiCallBL.cs#L40` |
| Error | Exception in {MethodName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationCommonApiCallBL.cs#L61` |
| Error | Exception in Service_AddOrUpdateQueueCount_Single | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationCommonApiCallBL.cs#L82` |
| Error | Error in IntegrationCommonAPiCallBL.Service_Sbus_Master_Log | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationCommonApiCallBL.cs#L119` |
| Error | Error in IntegrationImportApiCallBL.TestServiceMethod for {Method.ToString()} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationCommonApiCallBL.cs#L188` |
| Debug | START:IntegrationController\|ManageServicesExport\|Service_SaveTrackChange_Record | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L140` |
| Debug | END:IntegrationController\|ManageServicesExport\|Service_SaveTrackChange_Record\|Message:{outputstring} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L148` |
| Debug | START:IntegrationController\|ManageServicesExport\|Service_SaveTrackChange_File | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L155` |
| Debug | END:IntegrationController\|ManageServicesExport\|Service_SaveTrackChange_File\|Message:{outputstring} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L177` |
| Debug | Set_Packet_Create_Input : packetCreationBO:{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L245` |
| Debug | Set_Packet_Create_Input : packetCreationBO:result.Result:{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L246` |
| Debug | Set_Packet_Create_Input_File : packetCreationBO:{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L311` |
| Debug | Set_Packet_Create_Input_File : packetCreationBO:result.Result:{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L312` |
| Debug | Set_Compress_ZIP_Input : compressBO:{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L355` |
| Debug | Set_Compress_ZIP_Input : compressBO:result.Result:{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L356` |
| Debug | Set_Split_Zip_Input : splitBO:{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L390` |
| Debug | Set_Split_Zip_Input : splitBO:result.Result:{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L391` |
| Debug | callling transfer service with input: {JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L448` |
| Debug | Set_Transfer_Create_Input : transferBO:{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L454` |
| Debug | Set_Transfer_Create_Input : transferBO:result.Result:{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L455` |
| Debug | {MethodName}\| Saving pending transfer queue data {JsonToSave} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L463` |
| Information | {MethodName}\| Transfer Queue Save data status : {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L500` |
| Debug | Set_Transfer_Create_Input_Compress : transferBO:{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L537` |
| Debug | Set_Transfer_Create_Input_Compress : transferBO:result.Result:{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L538` |
| Debug | Medium result {result} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L692` |
| Debug | split test{result} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L801` |
| Debug | PAcket count service output{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L842` |
| Debug | packet counter test{result} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L862` |
| Debug | Compression type{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L939` |
| Debug | Pro Data input settings to PacketCreation EXT: {JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L1025` |
| Error | Error while updating Track change with PSD Status \| continuing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L1104` |
| Error | Error while updating Track change with Error Status\| continuing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L1130` |
| Error | Error in IntegrationExportApiCallBL.TestServiceMethod for {Method.ToString()} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L1601` |
| Debug | cypher input: {JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L1658` |
| Debug | Azure Res input: {JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L1844` |
| Debug | Calling Trasnfer withdata{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L2011` |
| Debug | Resend Transfer Data: {JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L2013` |
| Throw:InvalidOperationException | Invalid Data gotten from Transfer Service\| Message: {result.ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L2028` |
| Throw:InvalidOperationException | Transfer Channel data gotten is invalid exiting | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L2033` |
| Error | Error in IntegrationExportApiCallBL.SendGenericMessageNotif | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L2068` |
| Debug | {MethodName}\| Process started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L2103` |
| Information | {MethodName}\| no transfer information found to resend to vessel {Vessel} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L2110` |
| Debug | {MethodName}\| Transfer resend data {Json} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L2114` |
| Debug | {MethodName}\| Process completed successfully | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationExportApiCallBL.cs#L2117` |
| Error | GetExportParams Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L106` |
| Information | {MethodName}\| Export Process started with param IsVessel {Param1} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L118` |
| Error | {MethodName}\| Channel Flow is empty | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L127` |
| Warning | {MethodName}\| No PR enabled vessels found. Exiting. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L135` |
| Information | {MethodName}\| New Export invocation is enabled. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L142` |
| Information | {MethodName}\| New Export invocation is disabled. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L147` |
| Information | {MethodName}\| Reading pending records information for channel : {InputChannelFlow} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L156` |
| Information | {MethodName}\| No pending records found for channel : {InputChannelFlow} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L170` |
| Information | {MethodName}\| Processing pending records for vessel object id : {VesselObjectId} with record count : {RecordCount} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L185` |
| Error | {MethodName}\| Channel Flow is empty for specific channel {ItemChannel} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L234` |
| Information | {MethodName}\| calling main export call methods | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L238` |
| Information | {MethodName}\| Remaining pending records count for vessel object id : {VesselObjectId} is {RemainingCount} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L256` |
| Information | {MethodName}\| Queued processing for vessel object id : {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L259` |
| Information | {MethodName}\| Completed processing all pending records for all vessels count {Count} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L273` |
| Information | {MethodName}\| Export Process completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L277` |
| Error | {MethodName}\| Exception while processing pending data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L295` |
| Information | START:IntegrationController\|ManageServicesExport\|IntegrationMainExport\|MainMethodExport | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L302` |
| Error | ERROR:IntegrationController\|MainMethodExport\|Message: serviceId 0 | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L316` |
| Information | END:IntegrationController\|ManageServicesExport\|IntegrationMainExport\|MainMethodExport | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L353` |
| Error | ValidateDataFile:Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L369` |
| Information | Intiating Resend calling Transfer Service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L391` |
| Information | <JsonConvert.SerializeObject(resendStatusUpdList))> | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L497` |
| Information | <JsonConvert.SerializeObject(result))> | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L501` |
| Error | IntegrationMainBL.MainMethodResend | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L507` |
| Information | Intiated packet download Process  | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L515` |
| Warning | Chunk size value is not set or invalid in filter param, defaulting to 1MB | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L522` |
| Debug | Some files data not found intiating download | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L542` |
| Throw:ArgumentNullException | Input is null or empty | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L592` |
| Error | Error in IntegrationMainBL.MainMethodDownloadPacket | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L601` |
| Throw:ArgumentNullException | File content is null {rec.FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L629` |
| Error | Error in IntegrationMainBL.CheckOperationByFile | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L744` |
| Error | Error in IntegrationMainBL.CheckAllServiceStatus | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L941` |
| Information | {MethodName}\| No pending transfer data found for processing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L959` |
| Information | {MethodName}\| No valid transfer data was found for processing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L989` |
| Information | {MethodName}\| Processing trasnfer queue for  {Count} number of files | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L997` |
| Information | {MethodName}\| Processing file {FileName} with retry Count {RetryCount} from service {CurrentProcessedServiceId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1001` |
| Warning | {MethodName}\| Invalid transfer item gotten with Id {Id} for file {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1049` |
| Error | {MethodName}\| Invalid transfer channel gotten {TransferChanneId} for file {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1055` |
| Error | {MethodName}\| Updated transfer queue error status to Failed for file {FileName}, with update Status {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1061` |
| Error | {MethodName}\| Invalid file name or file location gotten for file {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1067` |
| Information | {MethodName}\| Validated transfer item for file {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1076` |
| Information | {MethodName}\| Starting worker for file {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1090` |
| Debug | {MethodName}\| Updated transfer queue status to InProgress for file {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1106` |
| Information | {MethodName}\| Completed worker for file {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1140` |
| Debug | {MethodName}\| Moved transfer queue data to history for file {FileName} with move status {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1154` |
| Error | {MethodName}\| Updated transfer queue error status to Failed for file {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1162` |
| Debug | {MethodName}\| Starting Complete handler for file {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1172` |
| Debug | {MethodName}\| Transfer Queue status update process completed for {FileName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1187` |
| Debug | {MethodName}\| Transfer Queue success has been updated with {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1207` |
| Information | {MethodName}\| Transfer Queue process has been completed for all service for {FileName} after service Id {ServiceId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1212` |
| Debug | {MethodName}\|Updating packet status as sent in priority table with input Json {InputJson} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1250` |
| Debug | {MethodName}\| Update status response {Response} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1252` |
| Error | {MethodName}\| File {FileName} not found at location {FileLocation} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1277` |
| Error | {MethodName}\| Error while moving file {FileName} to sent folder {SentFolder} with status {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1286` |
| Debug | {MethodName}\|Update Vessel to vessel data as SENT for transfer item file {FileName}, Response status: {Status}\| Message:{ResponseMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1343` |
| Information | {MethodName}\|Bulk transfer file {FileName} sent to vessel {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1358` |
| Error | {MethodName}\|Export path not found for replica type {ReplicaTypeId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1368` |
| Debug | {MethodName}\|File moved to location {DestinationPath} status {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1379` |
| Information | {MethodName}\| Transfer Queue process has been completed for {FileName} with service Id {ServiceId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1385` |
| Information | {MethodName}\| Transfer Queue process awaiting response for {FileName} for service {ServiceName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1405` |
| Debug | {MethodName}\| Transfer Queue status has been updated with {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1413` |
| Warning | {MethodName}\| Transfer Queue process failed as gotten invalid response for {FileName} for service Id {Service} with return code {StatusCode} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1424` |
| Warning | {MethodName}\| Transfer Queue process has reached maximum retry limit for {FileName} for service Id {Service} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1450` |
| Debug | {MethodName}\| Transfer Queue item moved to history for {FileName} with status {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1455` |
| Error | Error in IntegrationMainBL.TransferPacketFolder | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1485` |
| Error | Error in IntegrationMainBL.TransferResendPacket | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1506` |
| Debug | {0}\|Moving file {1} to destionation Folder {2} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1518` |
| Error | Error in {0}\| while processing file {1} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1532` |
| Information | {MethodName}\| Initiating Priority Resend\| Vessel input-{VesselId} or all vessels | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1542` |
| Error | {MethodName}\| Transfer channel not found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1550` |
| Throw:InvalidOperationException | Transfer channel not found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1551` |
| Information | {MethodName}\| No priority resend packets found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1560` |
| Debug | {MethodName}\| Waiting for remaining tasks to complete | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1580` |
| Information | {MethodName}\| Priority Resend process completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1584` |
| Information | {MethodName}\| Starting to send missing packet notification | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1597` |
| Warning | {MethodName}\| General Notification sending is not enabled | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1611` |
| Information | {MethodName}\| No pending notification queue data found | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1625` |
| Information | {MethodName}\| Processing notification for record {RecordId} for notif {NotificationType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1633` |
| Information | {MethodName}\| Completed sending missing packet notification | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1647` |
| Information | {MethodName}\| Processing missing packet notification for item {RecordId}\| Type : {NotificationType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1658` |
| Error | {MethodName}\| Data gotten is invalid for {Id}, aborting it | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1677` |
| Error | {MethodName}\| No missing packet data found for RecordId {RecordId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1688` |
| Error | {MethodName}\| Communication type {CommunicationType} is not supported for missing packet notification | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1695` |
| Information | {MethodName}\| Missing packet notification queue name: {QueueName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1729` |
| Error | {MethodName}\| no queue name found for missing packet notification for record {RecordId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1732` |
| Debug | {MethodName}\| Sending missing packet with input {Json} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1744` |
| Debug | {MethodName}\|Missing packet notif call output status: {Json} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1747` |
| Debug | {MethodName}\| Sbus notification sent successfully for RecordId {RecordId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1751` |
| Error | {MethodName}\| Sbus notification failed for RecordId {RecordId} with error {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1756` |
| Information | {MethodName}\| Completed processing missing packet notification for item {RecordId} \| Type : {NotificationType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationMainBL.cs#L1768` |
| Information | SetInputExportBO:servic input for {serviceId}: {JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L70` |
| Information | Previous Service: {prevService} Input:{outputbo} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L169` |
| Information | Calling prodata service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L781` |
| Information | TransferBO: {proDataInputjson} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L826` |
| Debug | {0}\|Started with channel {1} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L840` |
| Error | Error in {0} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L846` |
| Error | Error in IntegrationSetInputBL.ResendSetInput | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L859` |
| Error | Error in IntegrationSetInputBL.DownloadPacketList | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L872` |
| Debug | IntegrationSetInputBL.MissingPacktSaveTrackRecord\|updating mising packet status via record due to notification error input: {JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L882` |
| Error | IntegrationSetInputBL.MissingPacktSaveTrackRecord | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L921` |
| Information | {MethodName}\|Sending missing packet and updating missing packt status via notification for input | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L930` |
| Debug | {MethodName}\| Setting missing packet for Acquisition data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L937` |
| Debug | {MethodName}\| Setting missing packet for Decompress data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L955` |
| Debug | {MethodName}\| No missing packet data found to update via notification | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L979` |
| Information | {MethodName}\| Starting Process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L992` |
| Debug | {MethodName}\| Input: {Input} \| Service: {Service} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L995` |
| Information | Set_V2V_Master_Log_Notification_Input :{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L997` |
| Debug | {MethodName}\| Sending notification for V2V Master Log: {NotificationInput} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L1048` |
| Debug | Beofre API call: {JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L1133` |
| Information | Beofre SendNotificationOffice API call: {JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L1260` |
| Error | Error in IntegrationSetInputBL.SendNotificationOffice | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L1267` |
| Error | Error in IntegrationSetInputBL.WindowsServiceStatus | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L1333` |
| Error | Error in IntegrationSetInputBL.CheckSbusReceiverStatus | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L1349` |
| Information | IntegrationSetInputBL.StartSbuSReciever\| Service is stopped, restarting | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L1387` |
| Information | Receiver Started Successfully | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L1406` |
| Information | Access check is a successs | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L1413` |
| Error | Error in IntegrationSetInputBL.StartSbuSReciever | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L1445` |
| Information | IntegrationSetInputBL.CheckAzureServiceStatus\| Service is stopped, restarting | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L1472` |
| Error | Error in CheckAzureServiceStatus | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/IntegrationSetInputBL.cs#L1497` |
| Debug | Adding new data to notif queue{JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/NotificationBL.cs#L104` |
| Information | Current notification Queue Status:{0}, Message:{1}  | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/NotificationBL.cs#L120` |
| Error | NotificationBL.ChatNotificationMessage | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/NotificationBL.cs#L130` |
| Error | NotificationBL.ReadChatNotificationMessage | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/NotificationBL.cs#L169` |
| Throw:ArgumentNullException | Pending message Data to sent is null  | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/NotificationBL.cs#L230` |
| Error | Error in IntegrationMainBL.ProcessTransferQueuedata | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/NotificationBL.cs#L256` |
| Error | Notification failed for messsage with Id{0}, with error{1}  | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/NotificationBL.cs#L262` |
| Information | Notificaiton sent successfully | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/NotificationBL.cs#L283` |
| Information | {MethodName}\| Starting to build queue from Track Change Records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L50` |
| Error | {MethodName}\| General Packet channel information not found. Exiting. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L58` |
| Error | {MethodName}\| Working directory is not configured. Exiting. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L65` |
| Warning | {MethodName}\| No channel flow settings found for export. Exiting. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L75` |
| Information | {MethodName}\| Retrieved {Count} channel flow settings | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L79` |
| Warning | {MethodName}\| No vessels found with General Export enabled. Exiting. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L93` |
| Information | {MethodName}\| No pending track records found for export. Exiting. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L106` |
| Information | {MethodName}\| Retrieved {Count} pending track records for export | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L111` |
| Information | {MethodName}\| Completed building queue from Track Change Records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L126` |
| Error | {MethodName}\| Exception occurred in InitiateTrackExport | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L130` |
| Information | {MethodName}\| Processing TableSettingsId: {TableSettingsId} with {RecordCount} records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L153` |
| Error | {MethodName}\| Exception occurred while processing TableSettingsId: {TableSettingsId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L165` |
| Error | {MethodName}\| Exception occurred in ExportNextHandler | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L185` |
| Information | {MethodName}\| Starting processing for TableSettingsId: {TableSettingsId} with {RecordCount} records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L192` |
| Error | {MethodName}\| Compression failed for TableSettingsId: {TableSettingsId}. Marking records as failed. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L245` |
| Debug | {MethodName}\| CompressionOutput: {JsonOutput} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L250` |
| Debug | {MethodName}\| Copying file from {SourceFilePath} to {DestFilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L298` |
| Error | {MethodName}\| Source file not found: {SourceFilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L301` |
| Error | {MethodName}\| Failed to copy file to {DestFilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L309` |
| Debug | {MethodName}\| Successfully copied file from {SourceFilePath} to {DestFilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L314` |
| Error | {MethodName}\| Error copying file from {SourceFilePath} to {DestFilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L318` |
| Error | {MethodName}\| No files were copied for vessel folder: {VesselFolderPath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L326` |
| Throw:IOException | No files were copied for vessel folder: {vesselFolderPath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L327` |
| Debug | {MethodName}\| Deleting temporary files: {FilesToDelete} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L332` |
| Error | {MethodName}\| Error processing vessel folder operations for VesselObjectId: {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L338` |
| Information | {MethodName}\| Completed processing for TableSettingsId: {TableSettingsId}and packets are ready for Transfer | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L391` |
| Information | {MethodName}\| Handling packet generation response | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L405` |
| Error | {MethodName}\| Packet generation failed with message: {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L411` |
| Error | {MethodName}\| Failed to update track record status | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L463` |
| Error | {MethodName}\| Exception occurred while handling packet generation response | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L471` |
| Information | {MethodName}\| Starting failure process for track records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L483` |
| Information | {MethodName}\| No failed records to process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L496` |
| Error | {MethodName}\| Failed to update status for failed track records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L506` |
| Error | {MethodName}\| Exception occurred while processing failed track records | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L511` |
| Information | {MethodName}\| Starting packet transfer handler | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L519` |
| Error | {MethodName}\| Transfer channel information not found. Exiting. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L535` |
| Information | {MethodName}\| No active vessels available to process. Exiting. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L558` |
| Information | {MethodName}\| Completed single pass through all vessels for packet transfer. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L585` |
| Error | {MethodName}\| Exception occurred in PacketTransferHandler | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L589` |
| Information | {MethodName}\| Vessel {VesselObjectId} has no pending packets. Skipping transfer. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L608` |
| Information | {MethodName}\| Retrieved {PendingCount} pending packets for vessel {VesselObjectId}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L612` |
| Warning | {MethodName}\| {FailedCount} packets failed validation for vessel {VesselObjectId}. Updating them with error status. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L620` |
| Error | {MethodName}\| Failed to update error status for {FailedCount} packets in vessel {VesselObjectId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L634` |
| Information | {MethodName}\| No valid packets remaining after validation for vessel {VesselObjectId}. Exiting transfer handler. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L641` |
| Information | {MethodName}\| Proceeding with {ValidCount} valid packets for vessel {VesselObjectId} (from original {TotalCount}). | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L645` |
| Throw:InvalidOperationException | Invalid or null transfer response received for vessel {vesselObjectId}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L667` |
| Error | {MethodName}\| Transfer failed for vessel {VesselObjectId} with message: {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L672` |
| Throw:InvalidOperationException | Unknown TransferStatus: {x.TransferStatus} for OutPacketHdId: {x.OutPacketHdId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L735` |
| Error | {MethodName}\| Failed to save transfer queue data for vessel {VesselObjectId} for count {TransferDataToSaveCount}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L746` |
| Error | {methodName}\| Failed to update packet status for vessel {vessel.VesselObjectId} for count {successUpdateList.Count}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L752` |
| Error | {MethodName}\| Exception occurred while processing packets for vessel {VesselObjectId}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L757` |
| Warning | {MethodName}\| Packet ID {PacketId} failed validation: {Errors} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L814` |
| Debug | {MethodName}\| Packet ID {PacketId} passed validation successfully. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L819` |
| Warning | {MethodName}\| Validation summary - Total packets: {TotalCount}, Valid: {ValidCount}, Failed: {FailedCount} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L825` |
| Debug | {MethodName}\| All pending packets validated successfully. Total packets: {PacketCount} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L835` |
| Debug | {MethodName}\| File found at original location for Packet ID {PacketId}: {FilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L852` |
| Warning | {MethodName}\| File not found at original location for Packet ID {PacketId}: {FilePath}. Attempting recovery. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L856` |
| Information | {MethodName}\| File found at recovered location for Packet ID {PacketId}. Attempting to copy from {RecoveredPath} to {OriginalPath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L881` |
| Debug | {MethodName}\| Created destination directory: {DestinationDirectory} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L890` |
| Information | {MethodName}\| Successfully copied file for Packet ID {PacketId} from {RecoveredPath} to {OriginalPath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L906` |
| Error | {MethodName}\| Exception occurred during file validation and recovery for Packet ID {PacketId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L931` |
| Information | {MethodName}\| Completed single pass through all vessels for packet transfer resend. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L1039` |
| Information | {MethodName}\| Retrieved {PendingCount} pending resend packets for vessel {VesselObjectId}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L1061` |
| Error | {methodName}\| Failed to save transfer queue data for vessel {vessel.VesselObjectId} for count {transferDataToSave.Count}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L1208` |
| Error | {methodName}\| Exception occurred while processing packets for vessel {vesselObjectId}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ExportQueueProcess.cs#L1219` |
| Information | {MethodName}\| Starting Import Process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L46` |
| Information | {MethodName}\|No Pending Communication type in import data to process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L82` |
| Debug | {MethodName}\| Skipping commType {CommType} because it is already being processed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L98` |
| Information | {MethodName}\| Starting import process for CommunicationType: {CommunicationType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L103` |
| Information | {MethodName}\| Added ImportVesselWorker task for CommunicationType: {CommunicationType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L109` |
| Critical | {MethodName}\| Exception occured which crashed the process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L128` |
| Information | {MethodName}\| Cleared all running comm types | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L134` |
| Information | {MethodName}\| Starting import for Vessels -{Count} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L151` |
| Warning | {MethodName}\| Current Client details not found, cannot proceed with import | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L159` |
| Warning | {MethodName}\| General Notification Channel not found, cannot proceed with import | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L166` |
| Debug | {MethodName}\| Waiting for tasks to complete before adding more | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L235` |
| Information | {MethodName}\| Completed import for Vessels -{Count} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L247` |
| Error | {MethodName}\| Exception occured while processing Import Queue Item | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L251` |
| Information | {MethodName}\| Cleared running comm types for CommunicationType: {CommunicationType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L258` |
| Information | {MethodName}\| No Pending Import Items found for Vessel {VesselId} and CommunicationType {CommType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L285` |
| Warning | {MethodName}\| Import Queue Item {Id} for Vessel {VesselId} and CommunicationType {CommType} is not valid, skipping | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L296` |
| Debug | {MethodName}\| Import Queue Item {Id} moved to history with status {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L307` |
| Warning | {MethodName}\| Import Queue Item {Id} for Vessel {VesselId} and CommunicationType {CommType} has invalid files, skipping | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L318` |
| Information | {MethodName}\| Processing Import Queue Item {Id} for Vessel {VesselId} and CommunicationType {CommType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L334` |
| Information | {MethodName}\| Awaiting response received for Import Queue Item {Id}. Stopping current batch and re-reading latest queue data. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L373` |
| Debug | {MethodName}\| Completed processing Import Queue Item {Id} for Vessel {VesselId} and CommunicationType {CommType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L377` |
| Information | {MethodName}\| Completed Import Worker for Vessel {VesselId} and CommunicationType {CommType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L381` |
| Error | {MethodName}\| Exception occured while processing Import Queue Item for Vessel {VesselId} and CommunicationType {CommType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L385` |
| Warning | {MethodName}\|Import Queue Item is null or not proper | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L400` |
| Warning | {MethodName}\|Channel for Import Queue Item {Id} is not valid | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L406` |
| Warning | {MethodName}\|Channel-{Channel} for Import Queue Item {Id} is not valid | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L412` |
| Warning | {MethodName}\|Channel Flow not found for channel-{Channel} for Import Queue Item {Id} is not valid | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L420` |
| Error | {MethodName}\|Exception occured while validating Import Queue Item | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L428` |
| Warning | {MethodName}\|ImportQSubDtEntities is null or empty for ImportQueueItem {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L444` |
| Error | {MethodName}\|AllZipDirectory does not exist or is not configured: {AllZipDirectory} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L451` |
| Error | {MethodName}\|Failed to create AllZipDirectory: {AllZipDirectory} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L460` |
| Warning | {MethodName}\|FileLocation is empty or FileSize <= 0 for SubItem {SubItemId} in ImportQueueItem {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L468` |
| Debug | {MethodName}\|File {FileLocation} not found, checking AllZipDirectory {ZipFilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L476` |
| Debug | {MethodName}\|Copying file from {ZipFilePath} to {FileLocation} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L482` |
| Error | {MethodName}\|Error copying file from {ZipFilePath} to {FileLocation} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L492` |
| Error | {MethodName}\|File {FileLocation} still does not exist after copy from {ZipFilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L498` |
| Information | {MethodName}\|File {FileLocation} successfully copied from zip directory | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L503` |
| Error | {MethodName}\|File {FileLocation} not found. Primary location missing. AllZipDirectory: {AllZipDirectory}, DirectoryExists: {DirExists}, FilePath: {ZipFilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L508` |
| Debug | {MethodName}\|File {FileLocation} exists for SubItem {SubItemId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L517` |
| Information | {MethodName}\|All files validated for ImportQueueItem {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L520` |
| Debug | {MethodName}\| Import Item | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L528` |
| Information | {MethodName}\| Matched with Acquisition File Service Id | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L535` |
| Debug | {MethodName}\| Acquisition File Service completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L537` |
| Information | {MethodName}\| Matched with File Merge Service Id | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L540` |
| Debug | {MethodName}\| File Merge Service completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L542` |
| Information | {MethodName}\| Matched with File Decompress Service Id | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L545` |
| Debug | {MethodName}\| File Decompress Service completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L547` |
| Information | {MethodName}\| Matched with Acknowledgement Service Id | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L550` |
| Debug | {MethodName}\| Acknowledgement Service completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L552` |
| Information | {MethodName}\| Matched with Sbus Send Update Service Id | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L555` |
| Debug | {MethodName}\| Sbus Send Update Service completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L557` |
| Critical | {MethodName}\| Service {ServiceId} is not implemented for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L569` |
| Information | {MethodName}\| Import Item {Id} processing aborted or failed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L576` |
| Information | {MethodName}Finished processing for all service for item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L583` |
| Information | {MethodName}\| Import Item {Id} is awaiting response for next service {NextServiceId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L603` |
| Debug | {MethodName}\| Import Queue Item {Id} status updated to AWAITING with message {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L609` |
| Debug | {MethodName}\| Import Queue Item {Id} status updated to PENDING with message {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L620` |
| Debug | {MethodName}\| Completed processing Import Item for Service {ServiceId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L623` |
| Error | {MethodName}\| Exception occured while processing Import Item for Service {ServiceId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L628` |
| Debug | {MethodName}\| Failed status update completed with message {Message} for service {ServiceId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L634` |
| Debug | {MethodName}\| Processing Import Item for Acquisition Batch Service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L642` |
| Information | {MethodName}\| Packet is waiting {PacketCounter} for another packet before this to proceeed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L699` |
| Debug | {MethodName}\| Acquisition Batch Service completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L703` |
| Error | {MethodName}\| Exception occured while processing Import Item for Acquisition Batch Service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L708` |
| Debug | {MethodName}\| Processing Import Item for File Merge Service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L717` |
| Error | {MethodName}\| File Merge Service failed for Import Item {Id} with error {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L746` |
| Error | {MethodName}\|Import item has been aborted due to error {ErrorMessage} for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L762` |
| Debug | {MethodName}\| Data merged successfully | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L775` |
| Debug | {MethodName}\| Import Queue Sub Data Items updated with status {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L785` |
| Error | {MethodName}\| Failed to update Import Queue Sub Data Items for Import Item {Id} with error {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L789` |
| Information | {MethodName}\| Completed processing Import Item for File Merge Service for Import Queue Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L812` |
| Error | {MethodName}\| Merge Process failed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L817` |
| Debug | {MethodName}\| Processing Import Item for Decompress Service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L836` |
| Information | {MethodName}\| Invoking Decompress service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L862` |
| Error | {MethodName}\| Process failed while handling Decompress service, marking as failed\| Due to :{ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L868` |
| Critical | {MethodName}\| Process failed while decompressing {FileName}, aborting | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L899` |
| Debug | {MethodName}\| Decompress service completed successfully | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L919` |
| Error | {MethodName}\| Failed to save decompressed files to database for Import Item {Id} with error {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L925` |
| Error | {MethodName}\| Failed to save decompressed succes info to In Packet H for Import Item {Id} with error {ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L953` |
| Error | {MethodName}\| Failed to update missing packet info for Import Item {Id}  | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L979` |
| Debug | {MethodName}\| Import Queue Items saved with status {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1021` |
| Critical | {MethodName}\| Exception while handling decompress service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1056` |
| Debug | {MethodName}\| Processing Import Item for Ackn Service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1075` |
| Debug | {MethodName}\| Invoking Ackn service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1101` |
| Error | {MethodName}\| Process failed while handling ackn service, marking as failed\| Due to :{ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1107` |
| Debug | {MethodName}\| Ackn service completed successfully | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1185` |
| Debug | {MethodName}\| Import Queue acknowledgement data saved with status {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1231` |
| Warning | {MethodName}\| Ackn service returned no saved ack ids for Import Item {Id}; no general notification queued | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1235` |
| Information | {MethodName}Import queue process for Ackn Completed successfully for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1238` |
| Critical | {MethodName}\| Exception while handling ackn service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1245` |
| Debug | {MethodName}\| Processing Import Item for General Notification Service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1262` |
| Error | {MethodName}\| Queue name is null or empty for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1279` |
| Information | {MethodName}\| Sending notification to queue {QueueName} for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1285` |
| Critical | {MethodName}\| Exception while handling service | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1292` |
| Error | {MethodName}\| Notification operation type is not provided for Import Item {Id} aborting | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1312` |
| Error | {MethodName}\| No IDs provided for General Notification for Import Item {Id} aborting | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1349` |
| Debug | {MethodName}\| Processing Missing Packet Status for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1370` |
| Error | {MethodName}\| No Missing Packet details found for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1375` |
| Debug | {MethodName}\| Processing Acknowledgement for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1418` |
| Error | {MethodName}\| No table details found for Import Item {Id} for table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1423` |
| Debug | {MethodName}\| Processing for common.PR_REP_VESSEL_SETTINGS Table for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1443` |
| Error | {MethodName}\| Unsupported notification operation type {OperationType} for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1470` |
| Debug | {MethodName}\| Resolving queue name for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1525` |
| Debug | {MethodName}\| Queue name resolved as {QueueName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1573` |
| Information | {MethodName}\| Sending General Notification for Import Item {Id} to queue {QueueName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1579` |
| Error | {MethodName}\| Process failed while sending General Notification for Import Item {Id}, marking as failed\| Due to :{ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1585` |
| Information | {MethodName}\| General Notification sent successfully for Import Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1612` |
| Error | {MethodName}\| Handling exception for Import Queue Item {Id} with status: {Status} and message: {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1622` |
| Error | {MethodName}\| Import item has been aborted for Import Queue Item {Id}. Moving to history with ABORTED status | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1628` |
| Error | {MethodName}\| Processing error for Import Queue Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1689` |
| Error | {MethodName}\| Retry limit {RetryLimit} exceeded for Import Queue Item {Id}. Moving to history with ABORTED status | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1700` |
| Debug | {MethodName}\| Updating missing packet status to Error for Import Queue Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1706` |
| Information | {MethodName}\| Marking Import Queue Item {Id} as FAILED. Retry count: {RetryCount}/{RetryLimit} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1773` |
| Debug | {MethodName}\| Import Queue Item {Id} status updated to FAILED with message {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1779` |
| Critical | {MethodName}\| Exception occurred while handling Import Queue Item exception for Item {Id} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/ImportQueueProcess.cs#L1786` |
| Information | {MethodName}\| Process Started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L52` |
| Information | {MethodName}\| Process Completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L60` |
| Information | {MethodName}\| Export process is disabled by configuration | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L86` |
| Information | {MethodName}\| Export process is already running | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L109` |
| Information | {MethodName}\| Export queue process has been started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L130` |
| Information | {MethodName}\| Export Queue process has been Completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L134` |
| Critical | {MethodName}\| Critical exception occurred during export queue processing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L138` |
| Debug | {MethodName}\| Export Queue process status removed from dictionary | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L143` |
| Information | {MethodName}\| PR Transfer process is already running | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L200` |
| Information | {MethodName}\| PR Transfer queue process has been started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L221` |
| Information | {MethodName}\| PR Transfer queue process has been Completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L225` |
| Critical | {MethodName}\| Critical exception occurred during PR Transfer queue processing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L229` |
| Debug | {MethodName}\| PR Transfer queue process status removed from dictionary | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L234` |
| Information | {MethodName}\| General Packet Resend process is already running | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L289` |
| Information | {MethodName}\| General Packet Resend process has been started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L309` |
| Information | {MethodName}\| General Packet Resend process has been Completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L313` |
| Critical | {MethodName}\| Critical exception occurred during General Packet Resend processing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L317` |
| Debug | {MethodName}\| General Packet Resend process status removed from dictionary | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L322` |
| Information | {MethodName}\|  Validating if general Export is enabled for Vessels | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L347` |
| Information | {MethodName}\| Export process is disabled by configuration. Skipping general Export validation. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L354` |
| Information | {MethodName}\| Not the right time to validate general Export for Vessels. Skipping. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L364` |
| Information | {MethodName}\| This is not a vessel. Skipping general Export validation. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L375` |
| Warning | {MethodName}\| General Packet channel not found. Please check configuration. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L383` |
| Warning | {MethodName}\| General export is already enabled for this Vessel so Skipping. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L393` |
| Error | {MethodName}\| Failed to enable general Export for Vessel {VesselObjectId}. Status: {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L405` |
| Information | {MethodName}\| General Export validation completed for Vessel {VesselObjectId}. Save status: {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L442` |
| Error | {MethodName}\| Exception occurred while validating general Export for Vessels | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L452` |
| Information | {MethodName}\| Import process is disabled by configuration | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L471` |
| Information | {MethodName}\| Import process is already running\| Another pass has been requested | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L496` |
| Information | {MethodName}\| Import queue process has been started | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L522` |
| Information | {MethodName}\| Import Queue process has been Completed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L526` |
| Information | {MethodName}\| Import queue was triggered during the run, starting another pass | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L546` |
| Critical | {MethodName}\| Critical exception occurred during import queue processing | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L552` |
| Debug | {MethodName}\| Import Queue process status removed from dictionary | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L564` |
| Information | {MethodName}\| Starting acquisition process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L589` |
| Information | {MethodName}\| Acquisition process completed with status: {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L605` |
| Information | {MethodName}\| Starting dynamic table insert/upsert for table {TableName} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L635` |
| Information | {MethodName}\| Dynamic table insert/upsert completed for table {TableName}. Status: {Status}, Message: {Message} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L641` |
| Information | {MethodName}\| Retrieving service status | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L665` |
| Information | {MethodName}\| Service status retrieved successfully | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L673` |
| Error | {MethodName}\| Exception occurred while retrieving service status | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/QueueHandler/IntegrationQueueProcessBL.cs#L701` |
| Warning | {MethodName} : PowerShell execution is disabled (ScriptExecutionOptions:PowerShell:Enabled). CorrelationId={CorrelationId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L78` |
| Warning | {MethodName} : cancelled while waiting for an execution slot. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L100` |
| Warning | {MethodName} : concurrency gate exhausted max {Max}, rejecting request | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L106` |
| Information | {MethodName} : starting. CorrelationId={CorrelationId} Source={Source} ScriptSha256={Hash} Budget={Budget}s MaxObjects={MaxObjects} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L125` |
| Error | {MethodName} : could not parse the wrapper result. CorrelationId={CorrelationId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L161` |
| Error | {MethodName} : failed. CorrelationId={CorrelationId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L191` |
| Warning | {MethodName} : could not stop the PowerShell process. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L314` |
| Warning | {MethodName} : could not delete {Dir} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L359` |
| Throw:InvalidOperationException | Embedded resource '{WrapperResourceName}' is missing from {assembly.GetName().Name}. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L367` |
| Information | {MethodName} : finished. Status={Status} Objects={Objects} Errors={Errors} Warnings={Warnings} ExitCode={ExitCode} Truncated={Truncated} Bytes={Bytes} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/PowerShellScriptExecutor.cs#L516` |
| Warning | {methodName} : Script Execution was cancelled by caller. | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/SqlScriptExecutor.cs#L69` |
| Warning | {methodName} : concurrency gate exhausted max {opts.MaxConcurrentExecutions}, rejecting request | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/SqlScriptExecutor.cs#L80` |
| Error | {methodName} : failed | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/ScriptExecution/ScriptExecutors/SqlScriptExecutor.cs#L129` |
| Error | ERROR:IntegrationController\|ValidateDataRecord\|Message:{outBO.ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L45` |
| Error | ERROR:IntegrationController\|ValidateDataFile\|Message:{outBO.ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L112` |
| Throw:ArgumentException | Invalid configuration for PR_REP_MAX_ATTACHMENT_SIZE | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L219` |
| Throw:ArgumentNullException | input | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L307` |
| Throw:ArgumentNullException | Input coparam name is mandatory | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L310` |
| Throw:ArgumentNullException | Input channel record gotten is null | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L314` |
| Throw:ArgumentNullException | Input record details gotten is null | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L317` |
| Throw:ArgumentNullException | Vesselobject Id gotten is null | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L321` |
| Throw:ArgumentNullException | Filename location gotten does not exists or the directory might not exists | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L325` |
| Error | error in  ValidationBL.ValidateTransferPacketFolder | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L331` |
| Throw:ArgumentNullException | generalTransferEntity.VesselObjectId | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L345` |
| Throw:ArgumentNullException | generalTransferEntity.SourceClient | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L348` |
| Throw:ArgumentOutOfRangeException | generalTransferEntity.CommunicationType | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L351` |
| Throw:ArgumentNullException | generalTransferEntity.SplitFiles | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L354` |
| Throw:ArgumentNullException | bulkTransferEntity | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L374` |
| Throw:ArgumentOutOfRangeException | bulkTransferEntity.VesselList | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L378` |
| Throw:ArgumentNullException | bulkTransferEntity.EndpointKey | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L381` |
| Throw:ArgumentOutOfRangeException | bulkTransferEntity.EndpointKey | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L385` |
| Throw:ArgumentNullException | bulkTransferEntity.FilePath | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L388` |
| Throw:FileNotFoundException | FilePath does not exist: {bulkTransferEntity.FilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L392` |
| Throw:InvalidDataException | File is empty: {bulkTransferEntity.FilePath} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L395` |
| Error | error in  ValidationBL.ValidateTransferResendPacketInput | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L418` |
| Throw:ArgumentNullException | chatNotifMessage | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L428` |
| Throw:ArgumentException | chatNotifMessage.MessageJson is null or empty | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L430` |
| Throw:ArgumentOutOfRangeException | chatNotifMessage.MessageJson only allows upto 10000 characters | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L432` |
| Throw:ArgumentException | chatNotifMessage.TableSettingsId is null, empty or 0 | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L434` |
| Throw:ArgumentException | chatNotifMessage.DestinationDetails.UniqueId list is null, empty or 0 | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L436` |
| Error | error in  ValidationBL.ValidateChatMessageNotif | `RepIntegration/MariApps.PAL.Rep.Integration.Service/BL/Validation/ValidationBL.cs#L444` |
| Error | {MethodName}\| failed for transfer {TransferId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/BulkTransferStatusController.cs#L44` |
| Error | {MethodName}\| failed while evaluating configuration | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/ConfigEvaluationController.cs#L74` |
| Information | --------------------------------------------------BATCH_START---------------------------------------------------------------- | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L64` |
| Information | START:IntegrationController\|IntegrateTrackRecord | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L65` |
| Error | ERROR:IntegrationController\|IntegrateTrackRecord\|Message:{outBO.ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L84` |
| Information | END:IntegrationController\|IntegrateTrackRecord | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L95` |
| Information | --------------------------------------------------BATCH_END------------------------------------------------------------------- | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L96` |
| Information | {0}\|Start | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L108` |
| Error | ERROR:IntegrationController\|IntegrateTrackFile\|Message:{outBO.ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L125` |
| Error | IntegrateTrackFile:Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L142` |
| Information | END:IntegrationController\|IntegrateTrackFile | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L154` |
| Information | START:IntegrationController\|IntegrateTrackExport | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L166` |
| Error | IntegrateTrackExport : Message : {ex.Message} \| StackTrace : {ex.StackTrace} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L188` |
| Error | ERROR:IntegrationController\|IntegrateTrackExport\|Message:{outBO.ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L193` |
| Information | END:IntegrationController\|IntegrateTrackExport | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L196` |
| Information | {MethodName}\| Start | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L209` |
| Information | {MethodName}\| End with status {Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L213` |
| Information | --------------------------------------------------RESEND_START---------------------------------------------------------------- | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L222` |
| Information | START:IntegrationController\|IntegrateResendV2V | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L223` |
| Information | --------------------------------------------------RESEND_END---------------------------------------------------------------- | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L233` |
| Information | End:IntegrationController\|IntegrateResendV2V | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L234` |
| Information | --------------------------------------------------DOWNLOAD_START---------------------------------------------------------------- | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L255` |
| Information | START:IntegrationController\|IntegrateDownloadV2VPacket | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L256` |
| Information | --------------------------------------------------DOWNLOAD_END---------------------------------------------------------------- | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L263` |
| Information | End:IntegrationController\|IntegrateDownloadV2VPacket | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L264` |
| Information | START:IntegrationController\|GetActiveVessels | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L284` |
| Information | End:IntegrationController\|GetActiveVessels | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L288` |
| Debug | {MethodName}\| Call back starterd with input {Josn} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L348` |
| Information | Called IntegrationController.TransferPacketFolder\|Input= {JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L357` |
| Debug | {MethodName}\| Resend packet invoked with input:{Json} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L383` |
| Debug | {0}\| Started, Input : {1} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L434` |
| Debug | {0}\| Validation failed, Error : {1} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L441` |
| Debug | START:IntegrationController.ChatNotificationMessage\|with input: {JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L489` |
| Debug | IntegrationController.ChatNotificationMessage\|Validation status: {validateStatus.Status}\|Message: {validateStatus.ErrorMessage} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationController.cs#L492` |
| Information | {MethodName} - Start | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationQueueController.cs#L32` |
| Information | {MethodName} - End | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/IntegrationQueueController.cs#L48` |
| Information | ExecuteScriptAndGetResult : initiating, CorrelationId={CorrelationId} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/ScriptExecutionController.cs#L34` |
| Information | ExecuteScriptAndGetResult : finished, Status={Status} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/ScriptExecutionController.cs#L36` |
| Error | ExecuteScriptAndGetResult : failed while attempting to execute script | `RepIntegration/MariApps.PAL.Rep.Integration.Service/Controllers/ScriptExecutionController.cs#L61` |
| Debug | {MethodName}\| Starting process with input {InputJson} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/AcknSL.cs#L27` |
| Debug | {MethodName}\| Response: {Response} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/AcknSL.cs#L44` |
| Debug | {MethodName}\| Starting process | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/AcquisitionSL.cs#L28` |
| Debug | {MethodName}\| Starting process with request: {Request} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/AcquisitionSL.cs#L47` |
| Error | {MethodName}\| Compression service returned {StatusCode}: {Body} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/CompressionSL.cs#L46` |
| Debug | {MethodName}\| Response status code {StatusCode},  message: {Response} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/CompressionSL.cs#L56` |
| Debug | {MethodName}\| Starting process with input vesselObjectId: {VesselObjectId}, exportType: {ExportType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/DBlogWSL.cs#L51` |
| Information | {MethodName}\| Successfully updated export type for vesselObjectId: {VesselObjectId} to exportType: {ExportType} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/DBlogWSL.cs#L59` |
| Error | {MethodName}\| Failed to update export type for vesselObjectId: {VesselObjectId}. Status code: {StatusCode}, Response: {Response} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/DBlogWSL.cs#L64` |
| Debug | {MethodName}\| Calling PacketCreationService | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/PacketCreationSL.cs#L92` |
| Error | {MethodName}\| PacketCreationService returned non-success status code {StatusCode} for request: {RequestJson} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/PacketCreationSL.cs#L107` |
| Error | {MethodName}\| Error occurred while calling PacketCreationService\| Request: {RequestJson} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/PacketCreationSL.cs#L124` |
| Debug | {MethodName}\| Processing priority transfer | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/TransferSL.cs#L31` |
| Error | {MethodName}\| TransferService returned non-success status code {StatusCode} for request: {RequestJson} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/TransferSL.cs#L46` |
| Error | {MethodName}\| Error occurred while processing priority transfer | `RepIntegration/MariApps.PAL.Rep.Integration.Service/SL/TransferSL.cs#L65` |
| Debug | \|Executing Post Request:{0}{1}, with input {2}  | `RepIntegration/MariApps.PAL.Rep.Integration.Service/ServiceClient/AcquisitionServiceClient.cs#L52` |
| Debug | \|API RESULE:{contents.Result} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/ServiceClient/AcquisitionServiceClient.cs#L65` |
| Error | \|Exception | `RepIntegration/MariApps.PAL.Rep.Integration.Service/ServiceClient/AcquisitionServiceClient.cs#L72` |
| Error | CheckServiceClient.CheckAllWinService | `RepIntegration/MariApps.PAL.Rep.Integration.Service/ServiceClient/CheckServiceClient.cs#L39` |
| Information | <Newtonsoft.Json.JsonConvert.SerializeObject(services))> | `RepIntegration/MariApps.PAL.Rep.Integration.Service/ServiceClient/CheckServiceClient.cs#L48` |
| Error | CheckServiceClient.CheckWinServiceStatus | `RepIntegration/MariApps.PAL.Rep.Integration.Service/ServiceClient/CheckServiceClient.cs#L58` |
| Error | CheckServiceClient.RestartWinService | `RepIntegration/MariApps.PAL.Rep.Integration.Service/ServiceClient/CheckServiceClient.cs#L76` |
| Error | CheckServiceClient.StopWinService | `RepIntegration/MariApps.PAL.Rep.Integration.Service/ServiceClient/CheckServiceClient.cs#L90` |
| Error | CheckServiceClient.StartWinService | `RepIntegration/MariApps.PAL.Rep.Integration.Service/ServiceClient/CheckServiceClient.cs#L104` |
| Error | LogWriteService:Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/ServiceClient/DBlogWServiceClient.cs#L87` |
| Error | Error in DblogWServiceClient.SaveCheckOperationStatus | `RepIntegration/MariApps.PAL.Rep.Integration.Service/ServiceClient/DBlogWServiceClient.cs#L159` |
| Information | Calling SendNotificaionV2V with Input : {JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/ServiceClient/SbusNotificationServiceClient.cs#L38` |
| Information | SendNotificationV2V output: {JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/ServiceClient/SbusNotificationServiceClient.cs#L42` |
| Error | SbusNotificationServiceClient.SendNotificationV2V | `RepIntegration/MariApps.PAL.Rep.Integration.Service/ServiceClient/SbusNotificationServiceClient.cs#L46` |
| Information | Calling SendNotification with input : {JsonConvert.SerializeObject} | `RepIntegration/MariApps.PAL.Rep.Integration.Service/ServiceClient/SbusNotificationServiceClient.cs#L54` |
| Error | error in SbusNotificationServiceClient.SendGenericNotification | `RepIntegration/MariApps.PAL.Rep.Integration.Service/ServiceClient/SbusNotificationServiceClient.cs#L96` |
| Information | WorkerService StartAsync | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L31` |
| Information | WorkerService StopAsync | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L38` |
| Information | {MethodName}\|WorkerService:ExecuteAsync\|Start | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L45` |
| Information | {MethodName}\| Process Cycle begings | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L59` |
| Information | {MethodName} \| invoking common init data | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L64` |
| Information | {MethodName} \| Initiating Integration export processes | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L70` |
| Information | {MethodName}\| Calling auto resend process for Priority Resend | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L74` |
| Information | {MethodName}\| Invoking General Notification sending method | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L77` |
| Warning | {MethodName}\| Integration main processes not started due to InitiateOnInterval is false | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L93` |
| Information | {MethodName}\| Process Cycle ends | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L95` |
| Information | {MethodName}\| Host stopping, process cycle cancelled | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L100` |
| Error | {MethodName} \| Work service failed  | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L105` |
| Information | {MethodName}\|Ended | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L110` |
| Information | WorkerService Dispose | `RepIntegration/MariApps.PAL.Rep.Integration.Service/WorkerService.cs#L117` |

## RepMedium

Logger templates in RepMedium. Keywords: RepMedium log, error.

| Level | Message template | Source |
|---|---|---|
| Error | Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepMedium/MariApps.PAL.Rep.Medium.DAL/MediumRepository.cs#L45` |
| Information | Medium:GetSizeRestriction:GetSizeRestrictions:Start | `RepMedium/MariApps.PAL.Rep.Medium.DAL/MediumRepository.cs#L52` |
| Information | Medium:GetSizeRestriction:GetSizeRestrictions:END | `RepMedium/MariApps.PAL.Rep.Medium.DAL/MediumRepository.cs#L86` |
| Error | Medium:GetSizeRestriction:GetSizeRestrictions:ERROR:Message{ex.Message}\|StackTrace:{ex.StackTrace} | `RepMedium/MariApps.PAL.Rep.Medium.DAL/MediumRepository.cs#L94` |
| Information | Medium:GetSizeRestriction:Start | `RepMedium/MariApps.PAL.Rep.Medium.Service/Controllers/MediumController.cs#L33` |
| Information | Medium:GetSizeRestriction:End | `RepMedium/MariApps.PAL.Rep.Medium.Service/Controllers/MediumController.cs#L35` |
| Information | Medium-TestService | `RepMedium/MariApps.PAL.Rep.Medium.Service/Controllers/MediumController.cs#L43` |
| Information | Medium-GetVersion | `RepMedium/MariApps.PAL.Rep.Medium.Service/Controllers/MediumController.cs#L51` |

## RepPacketCreation

Logger templates in RepPacketCreation. Keywords: RepPacketCreation log, error.

| Level | Message template | Source |
|---|---|---|
| Error | DL GetExportParams \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L55` |
| Error | DL GetRepCode \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L97` |
| Error | DL ReadPcktCount \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L128` |
| Error | DL GetPcktCounter \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L166` |
| Warning | DL InsertOutPacketHd \| No record details found for packet {PacketName} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L177` |
| Error | DL InsertOutPacketHd \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L207` |
| Error | DL GetErrorMissingPackets \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L248` |
| Error | DL GetMissingFile \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L292` |
| Error | DL GetTransferType \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L353` |
| Error | DL GetTransferLocation \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L392` |
| Error | ERROR in PacketCreationRepository.GetExtPacketCounter | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L418` |
| Error | ERROR in PacketCreationRepository.UpdatePacketCounter | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L441` |
| Throw:DataException | Data did not save Successfully | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L462` |
| Error | Error in PacketCreationRepository.SaveExtPacketDetails | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L467` |
| Error | Error in PacketCreationRepository.SaveSourcePacketDetails | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketCreationRepository.cs#L490` |
| Debug | {MethodName} \| Saving out packet HD \| PacketNo: {PacketNo}, PacketName: {PacketName}, FileSize: {FileSize} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketDapperRepository.cs#L27` |
| Error | {MethodName} \| Error saving out packet HD \| PacketNo: {PacketNo}, PacketName: {PacketName}, FileSize: {FileSize} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketDapperRepository.cs#L53` |
| Debug | {MethodName} \| Retrieving last out packet counter for VesselObjectId: {VesselObjectId} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketDapperRepository.cs#L62` |
| Error | {MethodName} \| Error retrieving last out packet counter for VesselObjectId: {VesselObjectId} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketDapperRepository.cs#L76` |
| Debug | {MethodName} \| Updating packet counter for VesselObjectId: {VesselObjectId} to NewCounter: {NewCounter} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketDapperRepository.cs#L85` |
| Error | {MethodName} \| Error updating packet counter for VesselObjectId: {VesselObjectId} to NewCounter: {NewCounter} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketDapperRepository.cs#L98` |
| Debug | {MethodName} \| Reading RepCode for VesselObjectId: {VesselObjectId} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketDapperRepository.cs#L106` |
| Error | {MethodName} \| Error reading RepCode for VesselObjectId: {VesselObjectId} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.DAL/PacketDapperRepository.cs#L120` |
| Error | Error in CommonOperationsBL\| Method : FolderStructureExt | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L78` |
| Information | INFO:PacketCreationController\|GeneratePackets\|DirectoryCreated\| {_Dir} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L90` |
| Error | ERROR:PacketCreationController\|CreateDirectory\|CreateDirectory\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L95` |
| Error | DL GetPacketName \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L118` |
| Error | Error in CommonOperationBl.TarZipCreateCompressPacket | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L141` |
| Error | Error in CommonOperationBl.CreateNormalCompressPacket.Delete | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L154` |
| Information | CommonOperationBl.CreateNormalCompressPacket\|adding file :{f} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L166` |
| Error | Error in CommonOperationBl.CreateNormalCompressPacket | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L174` |
| Debug | {0}\|Started | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L185` |
| Debug | {0}\|Moved file to temp directory {1} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L189` |
| Debug | {0}\|Creating Tar zip file | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L193` |
| Debug | {0}\|Creating normal dotnet zip file | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L197` |
| Debug | {0}\|File created successfully | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L204` |
| Throw:FileNotFoundException | \|File not found | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L209` |
| Error | <ex, methodName)> | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L214` |
| Error | {0}\|Error while deleting temp directory {1} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L227` |
| Throw:ArgumentException | \|Source file list is empty | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L237` |
| Error | {0}\|Missing source file(s): {1} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L250` |
| Throw:FileNotFoundException | \|Missing source file(s): {string.Join} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L251` |
| Debug | {0}\|Tar zip file created | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L265` |
| Error | {0}\| Error while creating zipfile {1} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L269` |
| Debug | {0}\|Normal dotnet zip file created | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L285` |
| Debug | {0}\|copying files to temp folder {1} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L300` |
| Debug | {0}\|Copying file {1} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L304` |
| Error | CommonOperationBL.DeleteFile\|Exception | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L331` |
| Debug | CommonOperationBL.CheckFile \|CHECKING IF FILE IS BEING USED\| CHECK Count {0} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L347` |
| Information | CommonOperationBL.CheckFile\|File:{fi.Name} is being used waiting for 20 seconds\| CHECK Count{checkCount} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L350` |
| Error | Exception in CommonOperationBL.CheckFile | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L372` |
| Error | CommonOperationBL.IsFileLocked | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L387` |
| Warning | RenameFile \| New file already exists: {NewFilePath}. Deleting it before renaming. | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L403` |
| Warning | RenameFile \| Old file does not exist: {OldFileName} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L411` |
| Error | RenameFile \| Error renaming file from {OldFileName} to {NewFileName} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L417` |
| Debug | {_methodName} initiated | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L425` |
| Information | [MESSAGEPACK COMPRESSION] Extracted tar.zst archive to {OutputFolder} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L450` |
| Debug | {_methodName} Files extracted to {ExtractPath} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L455` |
| Error | {MethodName} Files extracted error, extractPath: {ExtractPath}, Message:{Message} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/CommonOperationsBL.cs#L462` |
| Error | Error in ExternalCallBL.ServiceCall | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ExternalCallBL.cs#L47` |
| Information | DataImport\|DataImport\|PushToServiceGet:START | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ExternalCallBL.cs#L54` |
| Information | DataImport\|DataImport\|PushToServiceGet\|Info:{contents.Result} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ExternalCallBL.cs#L67` |
| Error | DataImport\|DataImport\|PushToServiceGet\|Error:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ExternalCallBL.cs#L74` |
| Information | DataImport\|DataImport\|PushToServicePost:Start | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ExternalCallBL.cs#L81` |
| Information | DataImport\|DataImport\|PushToServicePost\|Info:{contents.Result} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ExternalCallBL.cs#L93` |
| Error | DataImport\|DataImport\|PushToServicePost\|Error:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ExternalCallBL.cs#L100` |
| Throw:ArgumentException | Invalid path | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/FileChunkWriterStream.cs#L14` |
| Throw:NotSupportedException | <)> | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/FileChunkWriterStream.cs#L33` |
| Error | ERROR:PacketCreationExtBL\|GeneratePacketExt Service\|Message: | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/GeneratePacketExtBL.cs#L51` |
| Warning | WARN:PacketCreationExtBL\|GeneratePacketExt\|MissingSourceFiles\|Count:{0}\|Files:{1} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/GeneratePacketExtBL.cs#L90` |
| Error | ERROR:PacketCreationExtBL\|GeneratePacketExt\|Message:{0} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/GeneratePacketExtBL.cs#L104` |
| Error | <ex, ch.ErrorMessage)> | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/GeneratePacketExtBL.cs#L116` |
| Error | Error in GeneratePacketExt in service | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/GeneratePacketExtBL.cs#L148` |
| Information | START:PacketCreationController\|GeneratePackets\|GeneratePackets | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L42` |
| Error | ERROR:PacketCreationController\|GeneratePackets\|GeneratePackets\|Message:{packetInput.ErrorMessage} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L55` |
| Information | INFO:PacketCreationController\|GeneratePackets\|GeneratePackets{PacketName}\|FileName:{OutzipVslPath} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L109` |
| Debug | Deleting files from location:{item.FileNameLocation} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L133` |
| Error | ERROR:PacketCreationController\|GeneratePackets\|GeneratePackets\|Message:{packetInput.ErrorMessage}Stack trace:{ex.Message} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L143` |
| Information | INFO:GeneratePackets\|Deleting ZIPFILE without packet counter if it exists\|FileName: {zipFIle.Name} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L200` |
| Information | INFO:PacketCreationController\|GeneratePackets\|GeneratePackets{_PcktName}\|FileName:{newZipfilefullpath} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L204` |
| Error | ERROR:PacketCreationController\| ERROR WHILE GENERATING PACKET WITH LATEST PACKET COUNTER\| ERROR MESSAGE: {ex.Message} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L212` |
| Information | END:PacketCreationController\|GeneratePackets\|GeneratePackets | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L262` |
| Error | ERROR:PacketCreationController\|GeneratePackets\|GeneratePackets\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L275` |
| Throw:ArgumentNullException | Rep code value gotten is null  or empty | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L325` |
| Throw:ArgumentNullException | Packet Name value gotten is null or empty | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L343` |
| Warning | WARN:PacketCreationController\|GeneratePackets\|GeneratePackets\|MissingSourceFiles\|Count:{0}\|Files:{1} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L373` |
| Information | Lock list length: {packetLock.Count} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L441` |
| Information | Packet Lock Created for {PacketName} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L447` |
| Information | Packet Lock Removed for {PacketName} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L463` |
| Error | Error while reading packet counter and creating packet\|ERROR Message:{ex.Message} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L469` |
| Error | ERROR:PacketCreationController\|CheckforErrorPackets\|Recreate Packet\|Message: Error while recreating packet\| Error Message: {ex.Message} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L595` |
| Information | INFO:Missing file does not exist\|Creating Empty packet | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L604` |
| Error | ERROR: PacketCreationController\|CheckforErrorPackets\|Recreate Packet\|Message: {ex.Message} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L651` |
| Information | INFO: PacketCreation Controller \| PacketCreationBL \| ClearOldFiles\| CHECKING DIRECTORY {file} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L660` |
| Error | ERROR:PacketCreation Controller \| PacketCreationBL \| ClearOldFiles\|MESSAGE: ERROR WHILE CLEARING OLD FILES {ex.Message} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketCreationBL.cs#L679` |
| Debug | {MethodName} - Start extracting zip file from {ZipPath} to {ExtractPath} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L42` |
| Debug | {MethodName} - Successfully extracted zip file. Extracted files count: {ExtractedFilesCount} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L47` |
| Error | {MethodName} - Error occurred while extracting zip file from {ZipPath} to {ExtractPath}. Message: {Message} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L52` |
| Debug | {MethodName} - Start generating packet for TableSettingsId: {TableSettingsId}, ChannelId: {ChannelId} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L61` |
| Debug | {MethodName} - Generating packet for VesselObjectId: {VesselObjectId} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L74` |
| Error | {MethodName} - Error occurred while generating packet for TableSettingsId: {TableSettingsId}, ChannelId: {ChannelId} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L118` |
| Debug | {MethodName} - Generating packet for VesselObjectId: {VesselObjectId}, PacketNameBase: {PacketNameBase} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L135` |
| Error | {MethodName} - Failed to rename packet file from {OldFileName} to {NewFileName} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L213` |
| Throw:Exception | Failed to rename packet file from {packetName} to {correctPacketName} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L214` |
| Error | {MethodName} - Error occurred while generating packet for VesselObjectId: {VesselObjectId}, PacketNameBase: {PacketNameBase} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L233` |
| Debug | {MethodName} - Saving packet header for VesselObjectId: {VesselObjectId}, PacketName: {PacketName}, PacketLocation: {PacketLocation} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L250` |
| Error | {MethodName} - Failed to save packet header for VesselObjectId: {VesselObjectId}, PacketName: {PacketName} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L292` |
| Throw:Exception | Failed to save packet header for VesselObjectId: {metaInfo.VesselObjectId}, PacketName: {correctPacketName} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L293` |
| Error | {MethodName} - Error occurred while saving packet header for VesselObjectId: {VesselObjectId}, PacketName: {PacketName}, PacketLocation: {PacketLocation} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L304` |
| Error | GetPacketName - Error occurred while generating packet name for RepCode: {RepCode}, ChannelId: {ChannelId} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L330` |
| Information | {MethodName} - Creating Zstd packet for PacketName: {PacketName} from file list | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L340` |
| Information | {MethodName} - Appending packet header for VesselObjectId: {VesselObjectId}, PacketCounter: {PacketCounter} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/PacketGenBL.cs#L357` |
| Error | Error while checking file size\|Message: {ex.Message} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L81` |
| Error | ERROR:PacketCreationController\|ValidateData\|Message:{inputBO.ErrorMessage} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L96` |
| Error | Error in ValidatePrNormalData method | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L193` |
| Error | {MethodName} \| Request is null | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L205` |
| Error | {MethodName} \| BasePath is null or empty | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L211` |
| Error | {MethodName} \| ChannelId or TableSettingsId is zero | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L217` |
| Error | {MethodName} \| VesselGroups is null or empty | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L223` |
| Error | {MethodName} \| One or more VesselGroups have invalid VesselObjectId or VesselPacketDirectory | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L229` |
| Error | {MethodName} \| One or more VesselGroups have non-existent VesselPacketDirectory | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L235` |
| Error | {MethodName} \| One or more VesselGroups have null or empty TrackRecordDetails | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L241` |
| Error | {MethodName} \| Error validating packet generation request | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/BL/ValidateInputBL.cs#L249` |
| Error | GetExportParams Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L49` |
| Information | START:PacketCreationController\|PacketCreation | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L60` |
| Information | INFO:INPUT\| PacketCreationInput JSON DATA: {packetCreationInputJson} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L63` |
| Information | END:PacketCreationController\|PacketCreation | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L82` |
| Information | INFO:OUTPUT\|PacketCreationOutputJson JSON DATA: {packetCreationOutputJson} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L85` |
| Error | ERROR:PacketCreationController\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L97` |
| Information | INFO:GeneratePacketExt\|Input JSON DATA: {requestData} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L109` |
| Error | ERROR:GeneratePacketExt\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L136` |
| Information | END:PacketCreationController\|TestService | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L176` |
| Information | END:PacketCreationController\|GetVersion | `RepPacketCreation/MariApps.PAL.Rep.PacketCreation.Service/Controllers/PacketCreationController.cs#L184` |

## RepPacketInterim

Logger templates in RepPacketInterim. Keywords: RepPacketInterim log, error.

| Level | Message template | Source |
|---|---|---|
| Error | Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.DAL/PacketInterimRepository.cs#L46` |
| Error | Error in PacketInterimRepository.UpdatePacketStatus | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.DAL/PacketInterimRepository.cs#L132` |
| Error | Error in PacketInterimRepository.UpdateExtPacketDataBulk | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.DAL/PacketInterimRepository.cs#L157` |
| Information | <JsonConvert.SerializeObject(input))> | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.Service/Controllers/PacketInterimController.cs#L39` |
| Information | <JsonConvert.SerializeObject(packetStatusBOs))> | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.Service/Controllers/PacketInterimController.cs#L77` |
| Information | <JsonConvert.SerializeObject(response))> | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.Service/Controllers/PacketInterimController.cs#L79` |
| Error | Error in PacketInterimController.UpdatePacketStatus | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.Service/Controllers/PacketInterimController.cs#L84` |
| Information | Input for PackerInterimController.UpdateExtPacketDataBulk\|json: {0} | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.Service/Controllers/PacketInterimController.cs#L93` |
| Information | PacketInterim-TestService | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.Service/Controllers/PacketInterimController.cs#L102` |
| Information | PacketInterim-GetVersion | `RepPacketInterim/MariApps.PAL.Rep.PacketInterim.Service/Controllers/PacketInterimController.cs#L110` |

## RepProData

Logger templates in RepProData. Keywords: RepProData log, error.

| Level | Message template | Source |
|---|---|---|
| Error | DL GetSettings \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepProData/MariApps.PAL.Rep.ProData.DAL/ProDataRepository.cs#L41` |
| Error | DL GetPacketCounter \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepProData/MariApps.PAL.Rep.ProData.DAL/ProDataRepository.cs#L68` |
| Error | DL GetPendingRecord \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepProData/MariApps.PAL.Rep.ProData.DAL/ProDataRepository.cs#L241` |
| Error | DL UpdateRecordStatus \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepProData/MariApps.PAL.Rep.ProData.DAL/ProDataRepository.cs#L278` |
| Error | DL GetPendingRecordData \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepProData/MariApps.PAL.Rep.ProData.DAL/ProDataRepository.cs#L321` |
| Error | DL SaveProcessingData \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepProData/MariApps.PAL.Rep.ProData.DAL/ProDataRepository.cs#L355` |
| Information | DataImport\|DataImport\|PushToServiceGet:START | `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ExternalCallBL.cs#L44` |
| Information | DataImport\|DataImport\|PushToServiceGet\|Info:{contents.Result} | `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ExternalCallBL.cs#L57` |
| Error | DataImport\|DataImport\|PushToServiceGet\|Error:{ex.StackTrace} | `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ExternalCallBL.cs#L64` |
| Information | DataImport\|DataImport\|PushToServicePost:Start | `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ExternalCallBL.cs#L71` |
| Information | DataImport\|DataImport\|PushToServicePost\|Info:{contents.Result} | `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ExternalCallBL.cs#L83` |
| Error | DataImport\|DataImport\|PushToServicePost\|Error:Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ExternalCallBL.cs#L90` |
| Error | ERROR:ProDataController\|ValidateData\|Message:{inputBO.ErrorMessage} | `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ProDataBL.cs#L39` |
| Information | START:ProDataController\|ProcessData\|ProcessData | `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ProDataBL.cs#L92` |
| Error | ERROR:ProDataController\|ProcessData\|ProcessData\|Message: | `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ProDataBL.cs#L114` |
| Error | SUCCESS:ProDataController\|ProcessData\|ProcessData\| Message:{item.ErrorMessage} | `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ProDataBL.cs#L151` |
| Error | ERROR:ProDataController\|ProcessData\|ProcessData\| Message:{item.ErrorMessage} | `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ProDataBL.cs#L158` |
| Error | ERROR:ProDataController\|ProcessData\|ProcessData\| Message:{msg} | `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ProDataBL.cs#L199` |
| Error | ERROR:ProDataController\|ProcessData\|ProcessData\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ProDataBL.cs#L219` |
| Information | END:ProDataController\|ProcessData\|ProcessData | `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ProDataBL.cs#L224` |
| Information | START:ProDataController\|ProcessData\|CreateJsonFile | `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ProDataBL.cs#L229` |
| Information | END:ProDataController\|ProcessData\|CreateJsonFile \| FileName:{fullpath} | `RepProData/MariApps.PAL.Rep.ProData.Service/BL/ProDataBL.cs#L267` |
| Information | START:ProDataController\|ProcessData | `RepProData/MariApps.PAL.Rep.ProData.Service/Controllers/ProDataController.cs#L43` |
| Information | START:ProDataController\|ProcessData\|Input Json Data: {JsonConvert.SerializeObject} | `RepProData/MariApps.PAL.Rep.ProData.Service/Controllers/ProDataController.cs#L45` |
| Information | END:ProDataController\|ProcessData | `RepProData/MariApps.PAL.Rep.ProData.Service/Controllers/ProDataController.cs#L54` |
| Information | END:ProDataController\|ProcessData\|Output Json Data: {JsonConvert.SerializeObject} | `RepProData/MariApps.PAL.Rep.ProData.Service/Controllers/ProDataController.cs#L55` |
| Error | ERROR:ProDataController\|ProcessData\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepProData/MariApps.PAL.Rep.ProData.Service/Controllers/ProDataController.cs#L70` |
| Information | INFO:ProDataController\|GetProcessData\|Message:ApiHit | `RepProData/MariApps.PAL.Rep.ProData.Service/Controllers/ProDataController.cs#L79` |
| Information | INFO:ProDataController\|GetVersion\|Message:ApiHit | `RepProData/MariApps.PAL.Rep.ProData.Service/Controllers/ProDataController.cs#L87` |

## RepQueueManage

Logger templates in RepQueueManage. Keywords: RepQueueManage log, error.

| Level | Message template | Source |
|---|---|---|
| Information | START:QueueManage\|GetQueueCount | `RepQueueManage/MariApps.PAL.Rep.QueueManage.Service/Controllers/QueueManageController.cs#L33` |
| Error | ERROR:QueueManage\|GetQueueCount\|Message:{queueInput.ErrorMessage} | `RepQueueManage/MariApps.PAL.Rep.QueueManage.Service/Controllers/QueueManageController.cs#L45` |
| Information | SUCCESS:QueueManage\|GetQueueCount\|Message:{queueInput.ErrorMessage} | `RepQueueManage/MariApps.PAL.Rep.QueueManage.Service/Controllers/QueueManageController.cs#L72` |
| Error | ERROR:QueueManage\|GetQueueCount\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepQueueManage/MariApps.PAL.Rep.QueueManage.Service/Controllers/QueueManageController.cs#L80` |
| Information | END:QueueManage\|GetQueueCount | `RepQueueManage/MariApps.PAL.Rep.QueueManage.Service/Controllers/QueueManageController.cs#L83` |
| Error | ERROR:QueueManage\|AddOrUpdateQueueCount\|Message:{queueInput.ErrorMessage} | `RepQueueManage/MariApps.PAL.Rep.QueueManage.Service/Controllers/QueueManageController.cs#L99` |
| Information | textname-QueueManage-TestService-Office | `RepQueueManage/MariApps.PAL.Rep.QueueManage.Service/Controllers/QueueManageController.cs#L152` |
| Information | textname-QueueManage-GetVersion-Office | `RepQueueManage/MariApps.PAL.Rep.QueueManage.Service/Controllers/QueueManageController.cs#L160` |

## RepSaveData

Logger templates in RepSaveData. Keywords: RepSaveData log, error.

| Level | Message template | Source |
|---|---|---|
| Error | Error in SaveDataRepository.ImportData | `RepSaveData/MariApps.PAL.Rep.SaveData.DAL/SaveDataRepository.cs#L172` |
| Error | ERROR_MSG:{error.ERROR_MSG} \| StackTrace:{error.STACK_TRACE} | `RepSaveData/MariApps.PAL.Rep.SaveData.DAL/SaveDataRepository.cs#L179` |
| Error | ERROR WHILE SAVING TO NOTIFICATION LOG TABLE\|MESSAGE: {ex.Message} | `RepSaveData/MariApps.PAL.Rep.SaveData.DAL/SaveDataRepository.cs#L208` |
| Error | Error in SaveDataRepository.SaveSubscriberList | `RepSaveData/MariApps.PAL.Rep.SaveData.DAL/SaveDataRepository.cs#L273` |
| Error | ERROR:SaveDataController\|ValidateData\|Message:{inputBO.ErrorMessage} | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/BL/SaveDataBL.cs#L32` |
| Information | START:SaveDataController\|ProcessData\|SaveData | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/BL/SaveDataBL.cs#L78` |
| Error | ERROR:SaveDataController\|SaveData\|Message:{saveDataInput.ErrorMessage} | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/BL/SaveDataBL.cs#L103` |
| Error | ERROR:SaveDataController\|ProcessData\|SaveData\|ErrorMessage:{saveDataInput.ErrorMessage} | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/BL/SaveDataBL.cs#L130` |
| Information | END:SaveDataController\|ProcessData\|SaveData | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/BL/SaveDataBL.cs#L136` |
| Error | ERROR:SaveDataController\|ProcessData\|SaveData\|ErrorMessage:{ex.Message}\|StackTrace{ex.StackTrace} | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/BL/SaveDataBL.cs#L143` |
| Information | ERROR:SaveDataController\|SaveData\|Message:{saveDataInput.ErrorMessage} | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/BL/SaveDataBL.cs#L188` |
| Information | START:SaveDataController\|ProcessData\|ReadFromJsonFile\|FileName:{FileNameLocation} | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/BL/SaveDataBL.cs#L349` |
| Information | END:SaveDataController\|ProcessData\|ReadFromJsonFile:{FileNameLocation} | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/BL/SaveDataBL.cs#L354` |
| Information | START:SaveDataController\|ProcessData | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/Controllers/SaveDataController.cs#L40` |
| Information | START:SaveDataController\|TrackQueue | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/Controllers/SaveDataController.cs#L48` |
| Error | ERROR:SaveDataController\|ProcessData\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/Controllers/SaveDataController.cs#L56` |
| Information | Save Data: FileLocation: {filePath}\| PacketCounter: {PacketCounter}\|Table Settings ID :  {TableSettingsId} | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/Controllers/SaveDataController.cs#L67` |
| Error | ERror in SaveAckn | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/Controllers/SaveDataController.cs#L72` |
| Information | Save Data\|SaveSubscriberList\|fileName: {acknBO.filePath}\|fileNameLocation: {acknBO.filePath} | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/Controllers/SaveDataController.cs#L135` |
| Error | Error in SaveAckn | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/Controllers/SaveDataController.cs#L146` |
| Information | START:SaveDataController\|TestService | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/Controllers/SaveDataController.cs#L158` |
| Information | START:SaveDataController\|GetVersion | `RepSaveData/MariApps.PAL.Rep.SaveData.Service/Controllers/SaveDataController.cs#L166` |

## RepSbus

Logger templates in RepSbus. Keywords: RepSbus log, error.

| Level | Message template | Source |
|---|---|---|
| Information | {MethodName}\| Initiating process | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L35` |
| Debug | {MethodName}\| Initiating AdminStructureHd | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L39` |
| Information | {MethodName}\| Process status added to memory store witht status {AddStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L50` |
| Error | {MethodName} - Error in initiating process | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L58` |
| Debug | {MethodName}\| Setting ServiceBus settings | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L67` |
| Critical | {MethodName}\| service bus connection string and basic info is not found | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L76` |
| Debug | {MethodName}\| ServiceBus settings added to memory store with status {AddStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L82` |
| Information | {MethodName}\| ServiceBus settings added to memory store | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L84` |
| Error | Error in {MethodName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L94` |
| Debug | {MethodName}\| Setting Current Environment Queue V2V | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L103` |
| Error | {MethodName}\| Queue name is not found | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L111` |
| Debug | {MethodName}\| Current Environment Queue V2V added to memory store with status {AddStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L117` |
| Information | {MethodName}\| Current Environment Queue V2V added to memory store | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L119` |
| Information | {MethodName}\| Getting Local IP Address | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L138` |
| Information | {MethodName}\| Local IP Address: {IpAddress} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L169` |
| Warning | {MethodName}\| Local IP Address not found | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L174` |
| Information | {MethodName}\| Setting Current Machine Name: {MachineName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L185` |
| Debug | {MethodName}\| Reading Service Status from memory | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L200` |
| Debug | {MethodName}\| Service Status read from memory with status {Status} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L202` |
| Information | {MethodName}\| Reading ServiceBus Credential | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L216` |
| Warning | {MethodName}\| Service bus credentials not found for {KeyName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L227` |
| Information | {MethodName}\| Service bus credentials found for {KeyName} and returning | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L232` |
| Error | Error in {MethodName}\| credentials not fetched | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L242` |
| Information | {MethodName}\| Reading Current Queue Name | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L251` |
| Warning | {MethodName}\| Queue name not found found in config | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L261` |
| Warning | {MethodName}\| Queue name not found in memory store for V2V data for Key {KeyName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L266` |
| Information | {MethodName}\| Queue name found for {KeyName} and returning | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L271` |
| Information | {MethodName}\| Queue name {QueueName} found and returning | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L275` |
| Error | Error in {MethodName}\| Queue name not fetched | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L284` |
| Information | {MethodName}\| Reading CommonSettingsSbus | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L293` |
| Warning | {MethodName}\| CommonSettingsSbus not found for {KeyName}, retrying | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L300` |
| Warning | {MethodName}\| CommonSettingsSbus not found for {KeyName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L306` |
| Information | {MethodName}\| CommonSettingsSbus found for {KeyName} and returning | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L315` |
| Error | Error in {MethodName}\| CommonSettingsSbus not fetched | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L325` |
| Debug | {MethodName}\| Reading Current Machine Name | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L334` |
| Warning | {MethodName}\| Machine Name not found in memory | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L342` |
| Information | {MethodName}\| Machine Name read from memory with name {MachineName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L346` |
| Debug | {MethodName}\| Reading Local IP Address | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L360` |
| Warning | {MethodName}\| Local IP Address not found in memory | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L368` |
| Information | {MethodName}\| Local IP Address read from memory with IP {IpAddress} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonDataConduit.cs#L372` |
| Information | {MethodName}\|checking network | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonOperation.cs#L24` |
| Information | {MethodName}\|network status: {NetworkStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonOperation.cs#L41` |
| Error | {MethodName}\|Exception | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonOperation.cs#L46` |
| Information | {MethodName}\| Validating directory {Dir} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonOperation.cs#L69` |
| Error | {MethodName}\| Directory path is null or empty | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonOperation.cs#L75` |
| Information | {MethodName}\| Directory does not exists creating it {Dir} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonOperation.cs#L81` |
| Critical | {MethodName}\| Unauthorized access to directory {Dir}\| Service does not have permission | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonOperation.cs#L90` |
| Error | {MethodName}\| Error occured while validating directory {Dir} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/CommonOperation.cs#L95` |
| Information | DataImport\|DataImport\|PushToServiceGet:START | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ExternalCallBL.cs#L24` |
| Information | DataImport\|DataImport\|PushToServiceGet\|Info:{contents.Result} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ExternalCallBL.cs#L37` |
| Error | DataImport\|DataImport\|PushToServiceGet\|Error:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ExternalCallBL.cs#L44` |
| Information | DataImport\|DataImport\|PushToServicePost:Start | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ExternalCallBL.cs#L51` |
| Information | DataImport\|DataImport\|PushToServicePost\|Info:{contents.Result} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ExternalCallBL.cs#L64` |
| Error | DataImport\|DataImport\|PushToServicePost\|Error:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ExternalCallBL.cs#L71` |
| Error | PACKET_TRANSFER\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ReceiverFuncBL.cs#L39` |
| Information | REP_ACKNOWLEDGEMENT:VesselObjectId:{_transferBO.VesselObjectId} \| File:{_transferBO.FileName} \| Status:{_transferBO.Status} \| Message:{_transferBO.StatusMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ReceiverFuncBL.cs#L45` |
| Information | SERVICE_INFO:VesselObjectId:{_transferBO.VesselObjectId} \| File:{_transferBO.FileName} \| Status:{_transferBO.Status} \| Message:{_transferBO.StatusMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ReceiverFuncBL.cs#L51` |
| Information | GENERAL_NOTIFICATION:VesselObjectId:{_transferBO.VesselObjectId} \| File:{_transferBO.FileName} \| Status:{_transferBO.Status} \| Message:{_transferBO.StatusMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ReceiverFuncBL.cs#L57` |
| Information | GENERAL_NOTIFICATION:JsonData:{_transferBO.JsonData} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ReceiverFuncBL.cs#L58` |
| Information | Decryption success | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L91` |
| Error | Decryption connection string \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L95` |
| Information | START:ServiceBusClient:Initialized\|_commonSettings.ServiceBusConnectionString exists:{_commonSettings.ServiceBusConnectionString.Length} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L122` |
| Information | END:ServiceBusClient:Initialized\|_commonSettings.ServiceBusConnectionString exists:{_commonSettings.ServiceBusConnectionString.Length} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L127` |
| Information | ReceiveService\|Message: {ex.Message}\|StackTrace: {ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L144` |
| Information | START:serviceBusClient.CreateProcessor:Initialized\|queueName:{queueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L292` |
| Information | END:serviceBusClient.CreateProcessor:Initialized\|queueName:{queueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L305` |
| Information | MessageReceived:{body} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L318` |
| Information | _transferBO null completing notification:{body} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L323` |
| Information | Notification Messages:{sendNotificationResponseJson} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L342` |
| Information | ACKNOWLEDGMENT_NOTIFICATION_V2V:VesselObjectId:{_transferBO.VesselObjectId} \| File:{_transferBO.FileName} \| Status:{_transferBO.Status} \| Message:{_transferBO.StatusMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L400` |
| Information | PACKET_TRANSFER_V2V_SEND_ACKN:VesselObjectId:{_transferBO.VesselObjectId} \| File:{_transferBO.FileName} \| Status:{_transferBO.Status} \| Message:{_transferBO.StatusMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L411` |
| Information | REP_WINDOWS_SERVICE: {DateTime.Now} VesselObjectId:{_transferBO.VesselObjectId} \| File:{_transferBO.FileName} \| Status:{_transferBO.Status} \| Message:{_transferBO.StatusMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L436` |
| Error | MessageHandler \| Wrong vessel data \| Data:{body} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L447` |
| Information | PACKET_TRANSFER_V2V Notification Messages:{sendNotificationResponseJson} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L495` |
| Information | PACKET_TRANSFER_V2V Notification Messages:{sendNotificationResponseJsonOffice} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L548` |
| Error | FAILED:MessageAfterReceiveDbUpdateFailed\|Data:{body} \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L575` |
| Error | SUCCESS:MessageAfterReceiveDbUpdateFailed\|Data:{body} \| Message:{fileWriteResponse.Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L625` |
| Error | ServiceBusBL\|MessageHandler\|Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L633` |
| Error | ErrorHandler:{args.Exception} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L638` |
| Information | ErrorHandler\|Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L656` |
| Information | Notification Messages:{sendNotificationResponseJson1} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L699` |
| Information | PACKET_TRANSFER_V2V Notification Messages:srcQueueName:{fileBO_PACKET_TRANSFER_V2V.srcQueueName}\|desQueueName:{fileBO_PACKET_TRANSFER_V2V.desQueueName}\|officeQueueName:{fileBO_PACKET_TRANSFER_V2V.officeQueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L758` |
| Information | PACKET_TRANSFER_V2V Notification Messages:{sendNotificationResponseJson1} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L761` |
| Information | PACKET_TRANSFER_V2V Notification Messages:{sendNotificationResponseJson2} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L767` |
| Error | ServiceBusBL\|MessageProcessing\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L821` |
| Information | ReceivedData:{receivedData} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L841` |
| Error | Exception: {ex.Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L875` |
| Error | ServiceBusBL\|MessageAfterReceive\|Message:{exjson.Message}\|StackTrace:{exjson.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L940` |
| Error | AzureTransferBO null | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L953` |
| Error | AzureTransferBO.FileName null | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L956` |
| Error | ServiceBusBL\|MessageAfterReceiveDbUpdateFailes\|Message:{exjson.Message}\|StackTrace:{exjson.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L978` |
| Error | GetTempFilesNotification\|FileName:{file.FullName}\|Locked | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L997` |
| Error | FAILED:DeleteTempFilesNotification:FileLocked:{item.azureTransferBo.FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1031` |
| Information | SUCCESS:DeleteTempFilesNotification:{item.azureTransferBo.FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1040` |
| Information | The file is being used by another process\|File: {fileLocation} \| ERROR MESSAGE: {ex.Message} \| StackTrace:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1072` |
| Information | <JsonConvert.SerializeObject(passedValue))> | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1086` |
| Information | ServiceBusSendNew:Message:{message} \| QueueName:{ClientEnviromentUnicID} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1102` |
| Information | PacketSentLog:{methodName}\|{queueName}\|{fileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1155` |
| Information | END:ServiceBusSend:NotificationType:{tBo.NotificationType} \| FileName: {tBo.FileName} \| QueueName:{queueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1175` |
| Error | The message {message} is too large to fit in the batch. | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1183` |
| Error | FAILED:ServiceBusSend: Message:{ex.Message} \| StackTrace:{ex.StackTrace} \| NotificationType:{tBo.NotificationType} \| FileName: {tBo.FileName} \| QueueName:{queueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1201` |
| Information | END:ServiceBusSend:NotificationType:{tBo.NotificationType} \| FileName: {tBo.packetName} \| QueueName:{desQueueNameBO.QueueName}\|packetCounter:{tBo.packetCounter} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1239` |
| Error | The message {input.Message} is too large to fit in the batch. | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1250` |
| Error | FAILED:ServiceBusSend: Message:{ex.Message} \| StackTrace:{ex.StackTrace} \| NotificationType:{tBo.NotificationType} \| FileName: {tBo.packetName} \| QueueName:{desQueueNameBO.QueueName}\|packetCounter:{tBo.packetCounter | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1275` |
| Error | GetListOfQueuesFromJsonFile failed : {logFolderPath} \| Message:{ex.Message} \| StackTrace{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1304` |
| Error | AddQueuesToJsonFile failed : {logFolderPath} \| Message:{ex.Message} \| StackTrace{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1327` |
| Error | Queue creation failed : {QueueName} \| Message:{ex.Message} \| StackTrace{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1350` |
| Information | IntegerationServiceCall\|Start | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1360` |
| Information | IntegerationServiceCall\|Start:{JsonConvert.SerializeObject} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1365` |
| Information | IntegerationServiceCall\|Acquisition service API url are not available | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1369` |
| Information | IntegerationServiceCall\|Acquisition REP_INTERGRATION_BASE_URL parameter value is empty | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1376` |
| Information | IntegerationServiceCall\|Acquisition REP_INTERGRATION_API_URL parameter value is empty | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1384` |
| Information | IntegerationServiceCall\|Start:REP_INTERGRATION_BASE_URL:{BaseUrl} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1392` |
| Information | IntegerationServiceCall\|Start:REP_INTERGRATION_API_URL:{ApiUrl} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1393` |
| Information | IntegerationServiceCall\|END | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1397` |
| Error |  Exception: {ex.Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1401` |
| Information | IntegerationServiceCallV2V\|Start | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1411` |
| Information | IntegerationServiceCallV2V\|Start:{JsonConvert.SerializeObject} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1416` |
| Information | IntegerationServiceCallV2V\|Acquisition service API url are not available | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1420` |
| Information | IntegerationServiceCallV2V\|Acquisition REP_INTERGRATION_BASE_URL parameter value is empty | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1425` |
| Information | IntegerationServiceCallV2V\|Acquisition REP_INTERGRATION_API_URL parameter value is empty | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1432` |
| Information | IntegerationServiceCallV2V\|Start:REP_INTERGRATION_BASE_URL:{BaseUrl} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1439` |
| Information | IntegerationServiceCallV2V\|Start:REP_INTERGRATION_API_URL:{ApiUrl} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1440` |
| Information | IntegerationServiceCallV2V\|END | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1444` |
| Error | IntegerationServiceCallV2V Exception: {ex.Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L1448` |
| Information | {MethodName}\|Starting listener | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L67` |
| Error | {MethodName}\| Internet not available | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L73` |
| Critical | {MethodName}\| Service is not ready to start listener due Service Intital Status being {ServiceStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L86` |
| Error | {MethodName}\| Service Bus Access failed with error {Error} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L101` |
| Information | {MethodName}\|Listener is already running | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L114` |
| Information | {MethodName}\| Receiver was not running, restarted it with status {ReceiverStartStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L131` |
| Information | {MethodName}\| Receiver started notification has been sent with status {NotificationStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L144` |
| Error | {MethodName}\| Receiver start failed with status {ReceiverStartStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L155` |
| Error | {MethodName}\|Exception while starting listener | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L171` |
| Information | {MethodName}\|Starting receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L185` |
| Throw:InvalidOperationException | Queue name is empty | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L193` |
| Throw:InvalidOperationException | Service bus credential is empty | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L196` |
| Information | {MethodName}\| Going to listen to queue {QueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L198` |
| Information | {MethodName}\| Queue {QueueName} is not active or created, creating it | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L202` |
| Error | {MethodName}\| Queue creation failed for {QueueName} with error {Error} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L208` |
| Information | {MethodName}\| Queue {QueueName} created successfully | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L218` |
| Information | {MethodName}\|Service Bus client intitialised | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L225` |
| Error | {MethodName}\|Exception while starting receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L240` |
| Information | {MethodName}\|Receiver started with status {ReceiverStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L245` |
| Debug | {MethodName}\| Creating Queue : {QueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L255` |
| Information | {MethodName}\| Queue does not exists : {QueueName}, creating it | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L265` |
| Information | {MethodName}\|Queue {QueueName} was successfully Created with status {Status} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L275` |
| Error | {MethodName}\| Queue creation failed : {QueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L293` |
| Information | {MethodName}\| Stopping receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L310` |
| Information | {MethodName}\| Stopping Receiver Queue Name: {QueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L315` |
| Information | {MethodName}\| Stopped receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L321` |
| Error | {MethodName} exception while stopping | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L325` |
| Information | {MethodName}\|Restarting receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L343` |
| Information | {MethodName}\|Receiver stopped successfully | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L348` |
| Information | {MethodName}\|Receiver starterd successfully | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L352` |
| Error | {MethodName}\|Receiver start failed {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L355` |
| Error | {MethodName}\|Receiver stop failed, {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L365` |
| Information | {MethodName}\|Restarted receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L373` |
| Error | {MethodName}\| Error while restarting | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L387` |
| Information | {MethodName}\|Getting receiver status | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L400` |
| Information | {MethodName}\|Processor status: {IsProcessing}, closed status: {IsClosed} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L416` |
| Error | {MethodName}\|Processor status: {IsProcessing}, closed status: {IsClosed} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L423` |
| Information | {MethodName}\|Receiver status: {ReceiverStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L455` |
| Information | {MethodName}\| Verifying Service Bus Access | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L462` |
| Information | {MethodName}\| Queue {QueueName} is already active | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L476` |
| Error | {MethodName}\| Error while verifying Service Bus Access | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L489` |
| Information | {MethodName}\|Stopping receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L497` |
| Information | {MethodName}\|Processor is null | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L502` |
| Information | {MethodName}\| messageHandlerCount- {MessgaeHandler}\| errorHandler - {ErrorHandler} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L520` |
| Information | {MethodName}\|Processor is not processing | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L526` |
| Information | {MethodName}\|Stopped receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L529` |
| Error | {MethodName}\|Error stopping receiver | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L533` |
| Error | {MethodName} Error while setting ErrorHandler event. | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L555` |
| Throw:InvalidOperationException | Failed to initialize ErrorHandler. | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L556` |
| Error | {MethodName} Error while setting MessageHandler event. | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L570` |
| Throw:InvalidOperationException | Failed to initialize MessageHandler. | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L571` |
| Throw:InvalidOperationException | One or more handlers could not be initialized. | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L576` |
| Warning | {MethodName}\| ServiceBus Listener is already running for Queue {QueueName}, listener not initalised again | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L588` |
| Information | {MethodName}Initialising receiver \|queueName:{QueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L593` |
| Information | {MethodName}\| Listener has been started for Queue {QueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L610` |
| Error | {MethodName}\|Service bus message process exception, removing message and error handler | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L615` |
| Information | {MethodName}\| Received a  message: SequenceNumber:{SequenceNumber}, Reply To Address:{ReplyTo}, Subject {Subject}, Delivery Count {DeliveryCount} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L655` |
| Debug | {MethodName}\| Message Body: {MessageBody} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L657` |
| Critical | {MethodName}\| Common Settings are not set, Config that were checked Location:{Location}, send Queeu Name:{SendQueueName}, Vessel Object ID : {VesselId} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L663` |
| Throw:InvalidOperationException | Common settings are not set | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L665` |
| Error | {MethodName}\| Invalid Json gotten as Message {Body} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L672` |
| Error | {MethodName}\| Invalid Json gotten as Message {Body}\| Removing from queue | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L692` |
| Information | {MethodName}\| Packet transfer data gotten sending acknowledgement File:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L712` |
| Debug | {MethodName}\| Sending acknowledgement for File:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L725` |
| Debug | {MethodName} Notification Messages: {Json} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L727` |
| Information | {MethodName}\| Processing Packet Transfer data for File:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L729` |
| Information | {MethodName}\| Packet Transfer data saved for File:{FileName} with Message: {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L736` |
| Debug | {MethodName} Notification Messages send status: {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L755` |
| Error | {MethodName}\| Packet Transfer data save failed for File:{FileName} with Message: {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L759` |
| Information | {MethodName}\| Acknowledgment Data gotten for VesselObjectId:{VesselObjectId} \| File:{FileName} \| Status:{Status} \| Message:{StatusMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L785` |
| Debug | {MethodName}\| Acknowledgement saved status {Saved} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L788` |
| Information | {MethodName}\| Service info gotten as notificaiton {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L798` |
| Debug | {MethodName}\| Service Info saved status {Saved} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L800` |
| Information | {MethodName}\| General Notification gotten {Messgae} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L806` |
| Information | {MethodName}\| {NotificationType} v2v packet transfer data gotten sending acknowledgement File:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L812` |
| Information | {MethodName}\| Notification ackowledgement sent for File:{FileName} \| with status {Status} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L831` |
| Information | {MethodName}\|Notification sent to office with Status:{Status} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L837` |
| Information | {MethodName}\| Processing  V2V Packet Transfer data for File:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L840` |
| Information | {MethodName}\| V2V Packet Transfer data saved for File:{FileName} with Message: {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L846` |
| Debug | {MethodName}\| Sending saved status for V2V Packet trasnfer for File:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L863` |
| Debug | {MethodName}\| Notification ackowledgement sent for File:{FileName} to source \| with status {Status} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L867` |
| Debug | {MethodName}\| Notification V2V ackowledgement sent for File:{FileName} to office \| with status {Status} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L873` |
| Error | {MethodName}\| V2V Packet Transfer data save failed for File:{FileName} with Message: {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L879` |
| Debug | {MethodName} Notification V2V failed Messages send status: {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L894` |
| Information | {MethodName}\| Acnknowledgement got for Type {NotificationType}\| with statusMessage :{Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L899` |
| Information | {MethodName}\| Acknowledgement saved status {Saved} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L902` |
| Information | {MethodName}\| V2V Send Acknowledgement got for Type {NotificationType}\| with statusMessage :{Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L907` |
| Information | {MethodName}\|MISSING_PACKET_STATUS save completed  | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L920` |
| Error | {MethodName}\|MISSING_PACKET_STATUS save failed with input {Input} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L928` |
| Information | {MethodName}\| {NotificationType} data gotten | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L936` |
| Information | {MethodName}\| Chat data saved, invoking queue | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L941` |
| Information | {MethodName}\| Chat data saved, invoking api completed with status {RequestStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L968` |
| Error | {MethodName}Saving to chat Queue Failed | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L972` |
| Information | {MethodName}\| General data saved successfully | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L984` |
| Error | {MethodName}\| General data save failed with error: {ErrorMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L989` |
| Error | {MethodName}\| Failed to deserialize ScriptExecutionRequestEnvelope from message body | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1005` |
| Error | {MethodName}\| JSON deserialization error for ScriptExecutionRequestEnvelope: {ErrorMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1011` |
| Information | {MethodName}\| Initiating Script execution | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1015` |
| Error | {MethodName}\| Script execution returned null result for RequestId: {RequestId} \| CorrelationID: {CorrelationID} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1019` |
| Information | {MethodName}\| Script execution reply sent failed for RequestId: {RequestId} \| CorrelationID: {CorrelationID} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1028` |
| Information | {MethodName}\| Script execution reply sent successfully for RequestId: {RequestId} \| CorrelationID: {CorrelationID} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1032` |
| Error | {MethodName}\| Failed to deserialize TroubleshootRunRequestEnvelope from message body | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1045` |
| Error | {MethodName}\| JSON deserialization error for TroubleshootRunRequestEnvelope: {ErrorMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1051` |
| Warning | {MethodName}\| Troubleshoot run request expired at {ExpiresAtUtc} \| CorrelationID: {CorrelationID} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1058` |
| Information | {MethodName}\| Triggering troubleshoot run \| CorrelationID: {CorrelationID} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1064` |
| Information | {MethodName}\| Troubleshoot run reply sent failed ({Status}) for RequestId: {RequestId} \| CorrelationID: {CorrelationID} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1073` |
| Information | {MethodName}\| Troubleshoot run reply ({Status}) sent successfully for RequestId: {RequestId} \| CorrelationID: {CorrelationID} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1077` |
| Information | {MethodName}\| {NotificationType} gotten is invalid | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1082` |
| Information | {MethodName}\| Invoking process after receiving message | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1087` |
| Error | {MethodName}\| Operation timeout occurred - message processing took too long | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1098` |
| Warning | {MethodName}\| Transient service bus error occurred - message will be retried | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1105` |
| Error | {MethodName}\| Exception in message processing | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1112` |
| Error | {MethodName}\| Failed to abandon message after error | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1122` |
| Debug | {MethodName}\| Message completed successfully | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1197` |
| Warning | {MethodName}\| Message completion failed - lock already lost (message likely processed by another receiver or lock expired) | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1202` |
| Warning | {MethodName}\| Message completion failed - message not found (already removed from queue) | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1207` |
| Warning | {MethodName}\| Message completion failed due to transient error - will retry | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1212` |
| Error | {MethodName}\| Message completion failed with unexpected error | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1217` |
| Debug | {MethodName}\| Message abandoned for retry | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1227` |
| Warning | {MethodName}\| Message abandon failed - lock already lost (message likely processed by another receiver or lock expired) | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1232` |
| Warning | {MethodName}\| Message abandon failed - message not found (already removed from queue) | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1237` |
| Warning | {MethodName}\| Message abandon failed due to transient error - will not retry | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1242` |
| Error | {MethodName}\| Message abandon failed with unexpected error | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1247` |
| Debug | {MethodName}\| Adding Failed Message Count | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1257` |
| Error | Failed Message Handler | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1262` |
| Debug | {MethodName}\| Executing operation: {OperationName} (Attempt {Attempt}/{MaxRetries}) | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1278` |
| Warning | {MethodName}\| Transient error occurred - retrying ({Attempt}/{MaxRetries}) after {DelayMs}ms | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1284` |
| Error | {MethodName}\| Operation {OperationName} failed after {Attempts} attempts | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1290` |
| Warning | {MethodName}\| Transient Service Bus error, processor will retry\| Reason:{Reason}\| Source:{ErrorSource}\| Entity:{EntityPath}\| Message:{Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1344` |
| Error | {MethodName}\| Exception Occured in Service Bus Message Processing | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1349` |
| Information | {MethodName}\|Number of Error Notification has exceeded daily limit. Skipping Notification | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1356` |
| Information | {MethodName}\| Error Notification sent to {QueueName} with message {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1379` |
| Error | Notification ErrorHandler | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1383` |
| Information | {MethodName}\| Invoking download api, Download current status:{Count}, time:{LastCallTime}  | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1391` |
| Information | {MethodName}\|Calling Download API, current count:{Count} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1396` |
| Information | {MethodName}\|Download has been called successfully | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1403` |
| Error | {MethodName}\|Download has been failed with error message {ErrorMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1407` |
| Information | {MethodName}\|Download has been queued | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1414` |
| Information | {MethodName}\| Handling Packet Transfer Message | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1425` |
| Debug | {MethodName}\| Packet Transfer Data gotten is {Json} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1427` |
| Debug | {MethodName}\| Saving file data :{Json} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1469` |
| Information | {MethodName}\| Packet transfer file download data saved successfully with message:{Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1477` |
| Error | {MethodName}\| Packet transfer download failed with message: {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1486` |
| Error | {MethodName}\| API Exception Packet Transfer download failed DblogW save api not being available | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1489` |
| Error | {MethodName}\| Error in handling packet transfer message | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1502` |
| Information | {MethodName}\| Handling V2V Packet Transfer Message | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1519` |
| Debug | {MethodName}\| V2V Packet Transfer Data gotten is {Json} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1521` |
| Information | {MethodName}\| V2V Packet transfer file download data saved successfully with message:{Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1575` |
| Error | {MethodName}\| V2V Packet transfer download failed with message: {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1584` |
| Error | {MethodName}\| API Exception Packet Transfer V2V download failed to DblogW save api not being available | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1588` |
| Information | {MethodName}\| {Operation} {Status} for File:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1637` |
| Warning | {MethodName}\| Status {Event} for transfer {TransferId} not saved: {Error} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1693` |
| Warning | {MethodName}\| Could not save bulk transfer status for File:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1697` |
| Information | {MethodName}\| Sending Notification to Queue:{QueueName} \| FileName:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1705` |
| Information | {MethodName}\| Notification has been sent with Status : {ResponseStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1718` |
| Information | {MethodName}\| Notification has been saved in DB with status {Status} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1723` |
| Error | {MethodName}\| {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1730` |
| Error | {MethodName}\| Failed to send Notification to Queue:{QueueName} \| FileName:{FileName} \| Error:{Error} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1737` |
| Information | {MethodName}\| Sending message to queue:{QueueName} \| FileName:{FileName}\| for process {ProcessName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1773` |
| Information | {MethodName} Notification has been sent Successfully with Status  {ResponseStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1796` |
| Information | {MethodName} sending to {Queue} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1803` |
| Information | {MethodName} sending to troubleshoot queue | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1820` |
| Information | {MethodName}\| Sending Notification to Queue:{QueueName}  | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1834` |
| Information | {MethodName}\| Sending Notification to Queue:{QueueName} \| FileName:{FileName} \| Notification Type :{NotificationType}\| Packet Counter {PcktCounter} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1869` |
| Error | {MethodName}\| Failed to send Notification to Queue:{QueueName} \| FileName:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1882` |
| Information | {MethodName}\| Start | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1894` |
| Error | {MethodName}\| Acquisition service API url are not available | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1901` |
| Error | {MethodName}\| Acquisition REP_INTERGRATION_BASE_URL parameter value is empty | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1906` |
| Error | {MethodName}\| Acquisition REP_INTERGRATION_API_URL parameter value is empty | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1912` |
| Information | {MethodName}\| Invoking Integration Service Call with Status : {Status} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1926` |
| Error | {MethodName}\| Exception | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1930` |
| Information | {MethodName}\| Starting to sending a notfication | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1937` |
| Debug | {MethodName}\| Sending Notification to Destination Queue: {DestinationQueue} \| Message: {Message} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1940` |
| Warning | {MethodName}\| ServiceBusClient is not initialized, initializing again | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1949` |
| Error | {MethodName}\| The message body size is too large {Length} to fit in the message batch | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1971` |
| Error | {MethodName}\| Failed to send message to the queue {DestinationQueue} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1983` |
| Information | {MethodName}\| Notification has been sent successfully | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L1997` |
| Error | Exception in {MethodName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L2002` |
| Error | FAILED:ValidateServiceBusClient | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L2020` |
| Error | Error in ServiceBusBL.ValidateServiceBusClient | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L2035` |
| Information | {MethodName}\| Processor has been restarted for Queue | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L2056` |
| Error | {MethodName}\| Error while restarting processor. | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L2060` |
| Information | ServiceBusBl.SetServiceBusOptions\| Setting the Following Options:UseWebSockets: {0}, Use WebProxy:{1} and WebProxyAddress:{2}  | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L2077` |
| Error | Error in setting ServiceBusBl.SetServiceBusOptions | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusOperation.cs#L2088` |
| Information | {MethodName}\| Starting to Process | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L42` |
| Debug | {MethodName}\| Input :{Input} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L44` |
| Warning | {MethodName}\| Service configuration status is false, retrying initialization | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L59` |
| Error | {MethodName}\| Service Configuration is not proper | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L65` |
| Error | {MethodName}\| Service Configuration value is not proper | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L77` |
| Error | {MethodName}\| ServiceBus ConnectionString is not proper | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L88` |
| Error | {MethodName}\| Queue names could not be found for destination and source | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L123` |
| Error | {MethodName}\| Source Queue name could not be found | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L132` |
| Error | {MethodName}\| Destination Queue name could not be found | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L141` |
| Error | {MethodName}\| Office Queue name could not be found | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L150` |
| Information | {MethodName}\| Processing V2V data | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L193` |
| Information | {MethodName}\| Finished | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L201` |
| Debug | {MethodName}\| Sending notification to queue :{QueueName} with Input {Json} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L241` |
| Information | {MethodName}\| Out packet source Id :{SourceId} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L259` |
| Error | {MethodName}\| Message sending failed :{ErrorMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L269` |
| Debug | {MethodName}\|Saving V2V Notification data to Master Log table\| with input :{Json} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L329` |
| Debug | {MethodName}\|Saved V2V Notification data to Master Log table\| with response :{Status} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L334` |
| Debug | {MethodName}\|Sending V2V Notification data to Office Queue\| with input :{Json} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L339` |
| Debug | {MethodName}\|Sent V2V Notification data to Office Queue\| with response :{Status} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L343` |
| Information | {MethodName}\| Notification sent successfully | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L346` |
| Error | {MethodName}\| Exception Occured | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L359` |
| Information | {MethodName}\| Finished Processing | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L361` |
| Information | {MethodName}\| Sending message to queue :{QueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L446` |
| Information | {MethodName}\| Finished sending all messages | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L461` |
| Debug | {MethodName}\| FileBO prepared :{FileBO} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L498` |
| Information | {MethodName}\| Moving file to SENT folder :{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L537` |
| Debug | {MethodName}\| Moving file {FileName} To Send Folder :{SendFolder} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L549` |
| Debug | {MethodName}\| New file location :{NewPath} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L558` |
| Information | {MethodName}\| File moved to SENT folder :{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceSbusBL.cs#L560` |
| Warning | {MethodName}\| Remote troubleshoot runs are disabled (TroubleshootRunSettings:Enabled=false) | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/TroubleshootLauncher.cs#L44` |
| Warning | {MethodName}\| Troubleshoot executable not found at '{Path}' | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/TroubleshootLauncher.cs#L52` |
| Information | {MethodName}\| Starting {Path} --remote-run{StopSwitch} RunId={RunId} CorrelationId={CorrelationId} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/TroubleshootLauncher.cs#L81` |
| Warning | {MethodName}\| No acknowledgement within {Seconds}s | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/TroubleshootLauncher.cs#L163` |
| Information | {MethodName}\| Acknowledged {Status} RunId={RunId} Pid={Pid} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/TroubleshootLauncher.cs#L169` |
| Warning | {MethodName}\| Troubleshoot exited with code {ExitCode} before acknowledging | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/TroubleshootLauncher.cs#L180` |
| Warning | {MethodName}\| No acknowledgement within {Seconds}s; leaving process {Pid} running | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/TroubleshootLauncher.cs#L188` |
| Error | {MethodName}\| Failed to start the troubleshoot process | `RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/TroubleshootLauncher.cs#L197` |
| Information | {MethodName}\|Sending Notification to {QueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/Controllers/SbusSendController.cs#L36` |
| Information | {MethodName}\| Started | `RepSbus/MariApps.PAL.Rep.Sbus.Service/Controllers/SbusSendController.cs#L45` |
| Information | {MethodName}\| Started for File:{FileName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/Controllers/SbusSendController.cs#L58` |
| Information | TestService:Started | `RepSbus/MariApps.PAL.Rep.Sbus.Service/Controllers/SbusSendController.cs#L133` |
| Information | SbuSendController\|ReadStaticVariable\|Current Download Count {0}, Last Download time:{1} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/Controllers/SbusSendController.cs#L149` |
| Throw:ArgumentNullException | <nameof(serviceConfig))> | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/AzureSl.cs#L26` |
| Debug | {MethodName}\| Process started | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/AzureSl.cs#L39` |
| Debug | {MethodName}\| Download api called got \|Response: {Output} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/AzureSl.cs#L50` |
| Error | Exception in ServiceBusSL.IntiateDownloadQueue | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/AzureSl.cs#L55` |
| Debug | {MethodName}\| Started  | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/DblogWSL.cs#L45` |
| Error | Exception in {MethodName} with input {Json} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/DblogWSL.cs#L97` |
| Error | Exception in {MethodName} for transfer {TransferId} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/DblogWSL.cs#L126` |
| Information | {MethodName}\| Started saving with input {Json} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/DblogWSL.cs#L134` |
| Debug | END: {MethodName} - Output: {Output} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/DblogWSL.cs#L206` |
| Debug | END: {MethodName} - RESPONSE: {Response} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/DblogWSL.cs#L235` |
| Information | {MethodName}\|Posting data to {ApiAddress} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ExternalInvokerClient.cs#L30` |
| Information | {MethodName}\|Data post to Api {ApiAddress} completed with status Code {ResponseStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ExternalInvokerClient.cs#L49` |
| Error | Exception in {MethodName}\| Message: {Body} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/IntegrationSL.cs#L61` |
| Information | {methodName} : The request jsonBody is invalid or empty hence skipping the remaining processing | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/IntegrationSL.cs#L107` |
| Error | Exception in {MethodName}\| ScriptExecutionResult : {CorrelationId} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/IntegrationSL.cs#L162` |
| Information | START:ServiceBusSL\|SbusWinReadConfiguration | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L25` |
| Error | ServiceBusSL\|SbusWinReadConfiguration\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L36` |
| Information | START:ServiceBusSL\|SbusWinInsertSbusNotification | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L44` |
| Error | ServiceBusSL\|SbusWinInsertSbusNotification\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L56` |
| Error | START:ServiceBusSL\|SbusWinUpdateDownload | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L64` |
| Error | ServiceBusSL\|SbusWinUpdateDownload\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L76` |
| Error | START:ServiceBusSL\|SbusWinReadServiceUrl | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L84` |
| Error | ServiceBusSL\|SbusWinReadServiceUrl\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L95` |
| Information | START:ServiceBusSL\|AzureServiceDownload | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L103` |
| Information | ServiceBusSL\|AzureServiceDownload\|Message:MethordStarted | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L107` |
| Information | ServiceBusSL\|AzureServiceDownload\|Message:MethordStarted\|Data{output} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L111` |
| Error | ServiceBusSL\|AzureServiceDownload\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L117` |
| Error | START:ServiceBusSL\|IntegrationServiceCall | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L125` |
| Error | ServiceBusSL\|IntegrationServiceCall\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L135` |
| Information | START:ServiceBusSL\|AzureGetSettings | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L144` |
| Information | END:ServiceBusSL\|AzureGetSettings{output} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L148` |
| Information | END:ServiceBusSL\|SbusWinGetSbusSettings\|RESPONSE\|{output} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L178` |
| Information | START:ServiceBusSL\|AzureGetSettingsV2V | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L186` |
| Information | END:ServiceBusSL\|GetCredentialsSettingsV2V{output} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L190` |
| Information | START:ServiceBusSL\|GetQueueNameV2V | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L196` |
| Information | END:ServiceBusSL\|GetQueueNameV2V{output} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L200` |
| Error | START:ServiceBusSL\|SbusWinInsertSbusNotification | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L205` |
| Error | START:ServiceBusSL\|SaveMasterLogV2V | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L253` |
| Error | ServiceBusSL\|SaveMasterLogV2V\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L274` |
| Error | START:ServiceBusSL\|SaveMasterLogV2VReceive | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L313` |
| Error | START:ServiceBusSL\|GetReceiverQueueNameForVesselV2V | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L341` |
| Error | ServiceBusSL\|GetReceiverQueueNameForVesselV2V\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L352` |
| Error | START:ServiceBusSL\|GetTrackChangeDetailsV2V | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L361` |
| Error | ServiceBusSL\|GetTrackChangeDetailsV2V\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/SL/ServiceBusSL.cs#L373` |
| Throw:InvalidOperationException | ServiceConfigData is null or empty | `RepSbus/MariApps.PAL.Rep.Sbus.Service/ServiceBusDependencyInjection.cs#L38` |
| Information | WorkerService:StartAsync | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L35` |
| Information | {MethodName}\| Stopping service | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L43` |
| Debug | {MethodName}\| Sending stop notification to queue name {QueueName} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L61` |
| Warning | {MethodName}\| stopped notification was not sent due to Office Queue name not being valid  | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L66` |
| Warning | {MethodName}\| stopped notification not sent this is already office XD | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L71` |
| Error | {MethodName}\| Exception occured while stopping the service | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L77` |
| Information | {MethodName}\| Starting Executioner | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L87` |
| Information | {MethodName}\| Executioner cycle has been started | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L91` |
| Debug | {MethodName}\| Initiating memory items | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L98` |
| Error | {MethodName}\| Service bus listener is not running due to {ErrorMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L109` |
| Information | {MethodName}\|Receiver is not processing, restarting | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L117` |
| Information | {MethodName}\|Receiver restarted after time {PeriodInDay} with restart Status {RestartStatus} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L119` |
| Information | {MethodName}\| Service bus listener is running, with status : {ReceiverStartMessage} | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L126` |
| Information | {MethodName}\| Service is stopping, executioner cycle cancelled | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L136` |
| Information | SbusService\|ExecuteAsync execution Ended | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L143` |
| Information | WorkerService:Dispose | `RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L151` |

## RepSplit

Logger templates in RepSplit. Keywords: RepSplit log, error.

| Level | Message template | Source |
|---|---|---|
| Information | START:SplitController\|CommonSplitMethodBL\|Splitting file File | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/CommonSplitMethodBL.cs#L20` |
| Information | END:CommonSplitMethodBL\|SplitFile\|COMPLETE | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/CommonSplitMethodBL.cs#L67` |
| Error | ERROR:CommonSplitMethodBL\|SplitFile\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/CommonSplitMethodBL.cs#L71` |
| Information | INFO:SplitController\|PacketSplit\|CreatePacketSplit\|CreateDirectory\|DirectoryCreated\| {_Dir} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/CommonSplitMethodBL.cs#L83` |
| Error | ERROR:SplitController\|PacketSplit\|CreatePacketSplit\|CreateDirectory\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/CommonSplitMethodBL.cs#L88` |
| Information | START:SplitController\|PacketSplit\|CreatePacketSplit | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L28` |
| Throw:ArgumentNullException | The Directory  value of OutzipVslPathMain gotten is null or empty | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L42` |
| Error | ERROR:PacketCreationController\|GeneratePackets\|GeneratePackets\|Message:{splitInput.ErrorMessage} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L61` |
| Information | INFO:SplitController\|PacketSplit\|CreatePacketSplit\|Checking file: {item.FileNameLocation} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L67` |
| Error | ERROR:SplitController\|PacketSplit\|CreatePacketSplit\|SplitCreated\|Message:{splitInput.ErrorMessage} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L79` |
| Information | INFO:SplitController\|PacketSplit\|CreatePacketSplit\|File found using absolute path: {fullFilePath} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L86` |
| Information | INFO:SplitController\|PacketSplit\|CreatePacketSplit\|Original file deleted: {originalFileLoc} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L119` |
| Warning | WARNING:SplitController\|PacketSplit\|CreatePacketSplit\|Failed to delete original file: {originalFileLoc} \| Error: {delEx.Message} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L123` |
| Information | SUCCESS:SplitController\|PacketSplit\|CreatePacketSplit\|SplitCreated\|FileName:{CompZipPath} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L128` |
| Error | ERROR:SplitController\|PacketSplit\|CreatePacketSplit\|Message:{ex.Message}\|StackTrace:{ex.StackTrace}\|FileName:{CompZipPathErr} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L159` |
| Information | END:SplitController\|PacketSplit\|CreatePacketSplit\|FileName:{CompZipPathErr} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L161` |
| Information | START:SplitController\|PacketSplit\|CreatePacketSplit\|SplitFile | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L166` |
| Information | END:SplitController\|PacketSplit\|CreatePacketSplit\|SplitFile | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitBL.cs#L211` |
| Information | START:SplitExtBL\|Method BEGINNING | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitExtBL.cs#L27` |
| Error | ERROR:SplitController\|PacketSplit\|CreatePacketSplit\|SplitCreated\|Message:{input.ErrorMessage} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitExtBL.cs#L39` |
| Information | DELETING ALL FILES AFTER CREATING INDIVIDUAL SPLITS | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitExtBL.cs#L80` |
| Information | DELETING FILE\| {Path.GetFileName} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitExtBL.cs#L85` |
| Error | Error while deleting original File\| {Path.GetFileName} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitExtBL.cs#L90` |
| Information | END:SplitExtBL\|Method ENDING | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitExtBL.cs#L95` |
| Error | Error in SplitExt method | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/SplitExtBL.cs#L100` |
| Error | ERROR:ValidateInputBL\|ValidateData\|Message:{inputBO.ErrorMessage} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/ValidateInputBL.cs#L45` |
| Information | INFO:ValidateInputBL\|ValidateData\|Updated file path to absolute: {absolutePath} | `RepSplit/MariApps.PAL.Rep.Split.Service/BL/ValidateInputBL.cs#L135` |
| Information | START:SplitController\|PacketSplit | `RepSplit/MariApps.PAL.Rep.Split.Service/Controllers/SplitController.cs#L39` |
| Information | INFO:INPUT\| split packt Input JSON DATA: {splitInputJson} | `RepSplit/MariApps.PAL.Rep.Split.Service/Controllers/SplitController.cs#L42` |
| Information | END:SplitController\|PacketSplit | `RepSplit/MariApps.PAL.Rep.Split.Service/Controllers/SplitController.cs#L51` |
| Information | INFO:INPUT\| split packt Output JSON DATA: {splitOutputJson} | `RepSplit/MariApps.PAL.Rep.Split.Service/Controllers/SplitController.cs#L54` |
| Error | ERROR:SaveDataController\|ProcessData\|Message:{ex.Message}\|StackTrace:{ex.StackTrace} | `RepSplit/MariApps.PAL.Rep.Split.Service/Controllers/SplitController.cs#L62` |
| Information | INFO:INPUT\| split packt output JSON DATA: {Newtonsoft.Json.JsonConvert.SerializeObject} | `RepSplit/MariApps.PAL.Rep.Split.Service/Controllers/SplitController.cs#L82` |
| Error | <ex,request.ErrorMessage)> | `RepSplit/MariApps.PAL.Rep.Split.Service/Controllers/SplitController.cs#L90` |
| Information | START:SplitController\|TestService | `RepSplit/MariApps.PAL.Rep.Split.Service/Controllers/SplitController.cs#L99` |
| Information | START:SplitController\|GetVersion | `RepSplit/MariApps.PAL.Rep.Split.Service/Controllers/SplitController.cs#L107` |

## RepTrack

Logger templates in RepTrack. Keywords: RepTrack log, error.

| Level | Message template | Source |
|---|---|---|
| Error | DL GetExportParams \| Message:{ex.Message} \| StackTrace:{ex.StackTrace} | `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L48` |
| Information | SUCCESS:TrackController\|SaveTrackChangeFile\|SaveTrackChangeFile\|Message:{trackMainOutputBO.ErrorMessage} | `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L203` |
| Error | ERROR:TrackController\|SaveTrackChangeFile\|SaveTrackChangeFile\|Message:{trackMainOutputBO.ErrorMessage} | `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L213` |
| Information | SUCCESS:TrackController\|SaveTrackChangeRecord\|SaveTrackChangeFile\|Message:{trackMainOutputBO.ErrorMessage} | `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L346` |
| Error | ERROR:TrackController\|SaveTrackChangeRecord\|SaveTrackChangeFile\|Message:{trackMainOutputBO.ErrorMessage} | `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L356` |
| Information | SUCCESS:TrackController\|SaveTrackChangeFileV2V\|SaveTrackChangeFileV2V\|Message:{trackMainOutputBO.ErrorMessage} | `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L514` |
| Information | SUCCESS:TrackController\|SaveTrackChangeFile\|SaveTrackChangeFile\|Message:{output.Message} | `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L715` |
| Error | ERROR:TrackController\|SaveTrackChangeFile\|SaveTrackChangeFile\|Message:{output.Message} | `RepTrack/MariApps.PAL.Rep.Track.DAL/TrackRepository.cs#L723` |
| Information | DataImport\|DataImport\|PushToServiceGet:START | `RepTrack/MariApps.PAL.Rep.Track.Service/BL/ExternalCallBL.cs#L44` |
| Information | DataImport\|DataImport\|PushToServiceGet\|Info:{contents.Result} | `RepTrack/MariApps.PAL.Rep.Track.Service/BL/ExternalCallBL.cs#L57` |
| Error | DataImport\|DataImport\|PushToServiceGet\|Error:{ex.StackTrace} | `RepTrack/MariApps.PAL.Rep.Track.Service/BL/ExternalCallBL.cs#L64` |
| Information | DataImport\|DataImport\|PushToServicePost:Start | `RepTrack/MariApps.PAL.Rep.Track.Service/BL/ExternalCallBL.cs#L71` |
| Information | DataImport\|DataImport\|PushToServicePost\|Info:{contents.Result} | `RepTrack/MariApps.PAL.Rep.Track.Service/BL/ExternalCallBL.cs#L83` |
| Error | DataImport\|DataImport\|PushToServicePost\|Error:{ex.StackTrace} | `RepTrack/MariApps.PAL.Rep.Track.Service/BL/ExternalCallBL.cs#L90` |
| Error | ERROR:TrackController\|ValidateRecordData\|Message:{output.ErrorMessage} | `RepTrack/MariApps.PAL.Rep.Track.Service/BL/TrackBL.cs#L25` |
| Error | ERROR:TrackController\|ValidateFileData\|Message:{output.ErrorMessage} | `RepTrack/MariApps.PAL.Rep.Track.Service/BL/TrackBL.cs#L194` |
| Information | INFO:TrackController\|SaveTrackChangeRecord\|Message:ApiHit | `RepTrack/MariApps.PAL.Rep.Track.Service/Controllers/TrackController.cs#L43` |
| Information | SUCCESS:TrackController\|SaveTrackChangeRecord\|Message:ApiHit | `RepTrack/MariApps.PAL.Rep.Track.Service/Controllers/TrackController.cs#L55` |
| Error | ERROR:TrackController\|SaveTrackChangeRecord\|Message:{output.ErrorMessage} | `RepTrack/MariApps.PAL.Rep.Track.Service/Controllers/TrackController.cs#L64` |
| Information | INFO:TrackController\|SaveTrackChangeFile\|Message:ApiHit | `RepTrack/MariApps.PAL.Rep.Track.Service/Controllers/TrackController.cs#L73` |
| Information | SUCCESS:TrackController\|SaveTrackChangeFile\|Message:ApiHit | `RepTrack/MariApps.PAL.Rep.Track.Service/Controllers/TrackController.cs#L86` |
| Error | ERROR:TrackController\|SaveTrackChangeFile\|Message:{output.ErrorMessage} | `RepTrack/MariApps.PAL.Rep.Track.Service/Controllers/TrackController.cs#L92` |
| Information | INFO:TrackController\|TestService\|Message:ApiHit | `RepTrack/MariApps.PAL.Rep.Track.Service/Controllers/TrackController.cs#L125` |
| Information | INFO:TrackController\|GetVersion\|Message:ApiHit | `RepTrack/MariApps.PAL.Rep.Track.Service/Controllers/TrackController.cs#L133` |

## RepTransfer

Logger templates in RepTransfer. Keywords: RepTransfer log, error.

| Level | Message template | Source |
|---|---|---|
| Debug | {MethodName}\| Process Started | `RepTransfer/MariApps.PAL.Rep.Transfer.DAL/TransferDapperRepository.cs#L25` |
| Error | {MethodName}\| Error occurred while reading transfer information | `RepTransfer/MariApps.PAL.Rep.Transfer.DAL/TransferDapperRepository.cs#L43` |
| Error | {MethodName}\| Error occurred while reading transfer type | `RepTransfer/MariApps.PAL.Rep.Transfer.DAL/TransferDapperRepository.cs#L68` |
| Warning | Using stale transfer type cache for VesselObjectId:{VesselObjectId} due to transient SQL error:{SqlErrorNumber} | `RepTransfer/MariApps.PAL.Rep.Transfer.DAL/TransferRepository.cs#L85` |
| Warning | Transient SQL error in GetTransferType for VesselObjectId:{VesselObjectId}, attempt:{Attempt}/{MaxAttempt}, sqlError:{SqlErrorNumber} | `RepTransfer/MariApps.PAL.Rep.Transfer.DAL/TransferRepository.cs#L132` |
| Error | Error in TransferRepository.ErrorPacketDetails | `RepTransfer/MariApps.PAL.Rep.Transfer.DAL/TransferRepository.cs#L311` |
| Information | <msg)> | `RepTransfer/MariApps.PAL.Rep.Transfer.DAL/TransferRepository.cs#L322` |
| Error | <msg)> | `RepTransfer/MariApps.PAL.Rep.Transfer.DAL/TransferRepository.cs#L326` |
| Error | Error in TransferRepository.SaveErroLog | `RepTransfer/MariApps.PAL.Rep.Transfer.DAL/TransferRepository.cs#L340` |
| Error | TransferRepository.Error Error while writting to Error Log | `RepTransfer/MariApps.PAL.Rep.Transfer.DAL/TransferRepository.cs#L376` |
| Error | TransferRepository.Information Error while writting to Error Log | `RepTransfer/MariApps.PAL.Rep.Transfer.DAL/TransferRepository.cs#L412` |
| Error | Exception in {MethodName} when finding file {FileName} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/CommonMethodBL.cs#L253` |
| Information | {MethodName}\| Process started | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L35` |
| Debug | {MethodName}\| Vessel List to check resend: {VesselList} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L42` |
| Error | {MethodName}\| transferMediumBaseFolder is null or empty for transfer type: {TransferType} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L76` |
| Error | {MethodName}\| Transfer Move failed for some records. Setting status to FAILED for table Settings Id - {TableIdList} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L217` |
| Information | {MethodName}\| Process completed successfully {Message} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L224` |
| Error | Exception occured while transferring {MethodName} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L235` |
| Information | {MethodName}\|Processing VesselObjectId: {VesselObjectId} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L262` |
| Information | {MethodName}\|Transfer Type: {TransferType} for vessel {VesselObjectId} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L266` |
| Error | {MethodName}\| File is not a directory: {FileNameLocation} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L287` |
| Information | {MethodName}\|Processing transfer type: {TransferType} for vessel {VesselObjectId} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L387` |
| Information | {MethodName}\| Process completed successfully with status: {Status} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L408` |
| Error | {MethodName}\| Exception occurred while moving file folder | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L419` |
| Information | recordsMainBO data: {JsonConvert.SerializeObject} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L498` |
| Information | chanelId data: {JsonConvert.SerializeObject} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L500` |
| Information | Resend data: {JsonConvert.SerializeObject} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L503` |
| Debug | {MethodName}\| Processing item \| VesselObjectId: {VesselObjectId}, FileName: {FileName} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L556` |
| Information | {MethodName}\| File not found in any folder \| FileName: {FileName} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L573` |
| Debug | {MethodName}\| File exists. Moving to work folder \| FileName: {FileName} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L577` |
| Debug | {MethodName}\| Record added to channel \| FileName: {FileName} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L622` |
| Information | {MethodName}\| Preparing TransferBO with resend data | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L627` |
| Information | {MethodName}\| No resend data found | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L636` |
| Information | {MethodName}\| Processing complete | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L642` |
| Error | Exception in {MethodName} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferBL.cs#L651` |
| Error | {MethodName}\| Transfer directory is empty for transferType {TransferType}, vessel {VesselObjectId} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferHandler.cs#L58` |
| Warning | {MethodName}\| Unknown transfer type {TransferType} for vessel {VesselObjectId} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferHandler.cs#L116` |
| Error | {MethodName}\| Error occurred while handling priority transfer | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferHandler.cs#L149` |
| Error | {MethodName}\| Error occurred while fetching vessel transfer type | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferHandler.cs#L190` |
| Error | {MethodName}\| Error occurred while fetching vessel transfer location | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferHandler.cs#L224` |
| Throw:ArgumentNullException | Transfer Medium folder details gotten is Null or Empty | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferPacketExtBL.cs#L110` |
| Throw:FileLoadException | Error while moving split file to OUTBOX Folder | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferPacketExtBL.cs#L153` |
| Throw:ArgumentNullException | Transfer Medium folder details gotten is Null or Empty OR does not exists | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferPacketExtBL.cs#L467` |
| Information | {0}\|Started for ChannelId:{1}\|VesselObjectId:{2} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferPacketExtBL.cs#L699` |
| Throw:InvalidOperationException | Transfer Type not found for VesselObjectId: {generalTransferEntity.VesselObjectId} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferPacketExtBL.cs#L704` |
| Debug | {0}\|Transfer Type found: {1} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferPacketExtBL.cs#L706` |
| Error | {0}\|Error in Split Files count | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferPacketExtBL.cs#L731` |
| Throw:InvalidOperationException | Error in Split Files count | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferPacketExtBL.cs#L732` |
| Error | Error in {0} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/TransferPacketExtBL.cs#L761` |
| Throw:InvalidOperationException | Source Client is mandatory | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/ValidateInputBL.cs#L244` |
| Throw:InvalidOperationException | Vessel Object Id is mandatory | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/ValidateInputBL.cs#L247` |
| Throw:InvalidOperationException | Split Files is mandatory | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/ValidateInputBL.cs#L250` |
| Throw:InvalidOperationException | File Location or File Name is mandatory | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/ValidateInputBL.cs#L253` |
| Throw:InvalidOperationException | One or more split files do not exist at the specified location | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/ValidateInputBL.cs#L256` |
| Warning | Validation failed in {0} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/ValidateInputBL.cs#L262` |
| Information | {MethodName}\| Validation successful  | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/ValidateInputBL.cs#L326` |
| Error | {MethodName}\| Error occurred while validating priority transfer | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/BL/ValidateInputBL.cs#L337` |
| Debug | Start: TransferResendUploadV2V \| Input Json: {JsonConvert.SerializeObject} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/Controllers/TransferController.cs#L200` |
| Information | {MethodName}\|Input:{Input} | `RepTransfer/MariApps.PAL.Rep.Transfer.Service/Controllers/TransferController.cs#L265` |

