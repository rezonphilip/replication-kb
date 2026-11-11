# iRep — placeholder

iRep articles will be written when the iRep repositories are processed. What is already known from MS-REP:

- RepIntegration handles only the **transfer** part of iRep (routes `IntegrateTrackRecord`, `IntegrateTrackFile`, `IntegrateTrackExport`, `TransferPacketFolder`; see CMP-REPINTEGRATION).
- RepTransfer may serve iRep transfer flows (CMP-REPTRANSFER).
- RepDBLogW has iRep database contexts (`Rep2IDbRepository`, `Rep2XDbRepository`) and may be called by iRep to read data (CMP-REPDBLOGW).
- RepAzure has `ReadIRepFolderFile` (CMP-REPAZURE).

Open question Q8 tracks which iRep flows use which routes.
