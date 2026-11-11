---
doc_id: CFG-MSREP-COPARAMS
type: config
mechanism: [smartsync, priority-replication]
runs_on: [office, vessel]
components: [ms-rep]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# MS-REP CO_Parameters keys — who reads what

Index of `Common.CO_Parameters` keys referenced in MS-REP code and which services read them. Values are never recorded here.

## Key index

One row per parameter name, with the services that read it. Keywords: CO_Parameters, parameter, config key, REP_, PR_.

| Key | Read by | Secret |
|---|---|---|
| `PR_PACKET_COUNTER` | RepAckn, RepIntegration |  |
| `PR_PARAM` | RepCompression, RepDecompress, RepIntegration, RepPacketCreation, RepSplit, RepTransfer |  |
| `PR_REP_IN_PACKET_HD_ID` | RepDBLogW |  |
| `PR_REP_MAX_ATTACHMENT_SIZE` | RepMedium, RepPacketCreation |  |
| `PR_REP_ROOT` | RepAcquisition, RepAzureRes, RepCompression, RepDecompress, RepIntegration, RepPacketCreation, RepProData, RepSplit, RepTransfer |  |
| `PR_REP_SPLIT_SIZE` | RepIntegration, RepSplit |  |
| `PR_TRACKCHANGE_RECORDS_ID` | RepTrack |  |
| `REP_AZURE_STORAGE_ACCOUNT_KEY` | RepAzure, RepDBLogW | yes — never copy |
| `REP_AZURE_STORAGE_ACCOUNT_NAME` | RepAzure, RepDBLogW |  |
| `REP_CHUNK_SIZE` | RepDBLogW, RepIntegration |  |
| `REP_CLIENT_CODE` | RepAzure, RepDBLogW |  |
| `REP_CLIENT_ENVIROMENT_UNICID` | RepAzure, RepDBLogW |  |
| `REP_CODE` | RepAcquisition, RepIntegration, RepPacketCreation |  |
| `REP_INTERGRATION_API_URL` | RepDBLogW, RepSbus |  |
| `REP_INTERGRATION_BASE_URL` | RepDBLogW, RepSbus |  |
| `REP_IN_INBOX` | RepDBLogW |  |
| `REP_LOCATION` | RepAzure, RepDBLogW |  |
| `REP_LOG` | RepAckn, RepTransfer |  |
| `REP_MANUAL_OP_PATH` | RepDBLogW |  |
| `REP_OFF_ROOT` | RepAcquisition, RepDecompress, RepFileMerge |  |
| `REP_PARALLEL_PROCESS_COUNT` | RepDBLogW, RepIntegration |  |
| `REP_PR_AZURE_IN` | RepIntegration, RepTransfer |  |
| `REP_PR_AZURE_SENT` | RepTransfer |  |
| `REP_PR_KEY_MASTER_ID` | RepAcquisition, RepIntegration | yes — never copy |
| `REP_RETRY_COUNT` | RepDBLogW |  |
| `REP_SERVICEBUS_CONNECTION_STRING` | RepDBLogW | yes — never copy |
| `REP_SOURCE_UNIQUE_ID` | RepAcquisition, RepIntegration |  |
| `REP_SOURCE_UNIQUE_OBJECT_TYPE` | RepAcquisition, RepIntegration |  |
| `REP_STORAGE_CONTAINER_NAME` | RepAzure, RepDBLogW |  |
| `REP_WINDOWS_SERVICE` | RepSbus |  |
| `REP_ZIP_UTILITY` | RepCompression, RepDecompress |  |

Where each key is read (file and line): `inventory/ms-rep.md`, per service.

## Related

- PLT-MSREP-OVERVIEW, INV-MSREP
