---
doc_id: INV-FAILURE-POINTS
type: inventory
mechanism: [priority-replication, smartsync, irep]
components: [ms-rep, irep]
status: draft
author: claude
last_verified: 2026-11-11
---

# Failure-point coverage

Every Error, Critical and Warning log template and every thrown exception in the code (2438 failure points) is mapped to an issue card. The machine-readable list is `catalog/failure-points.yaml`. Keywords: failure point, coverage, error catalogue, log level.

## Visibility

Which failure points reach the log file with the shipped log level (Serilog minimum level Error). Keywords: log level, hidden warnings.

| Level | Failure points | Visible by default |
|---|---|---|
| Critical | 79 | yes |
| Error | 1784 | yes |
| Throw | 370 | only if caught and logged |
| Warning | 205 | no |

## Cards

Number of failure points each card covers. Keywords: issue card, coverage.

| Card | Failure points |
|---|---|
| ISS-AZURE-001 | 3 |
| ISS-AZURE-002 | 5 |
| ISS-AZURERES-001 | 4 |
| ISS-DBLOGW-CONFIG | 4 |
| ISS-DBLOGW-DATAAPPLY | 4 |
| ISS-DBLOGW-DB | 34 |
| ISS-DBLOGW-FILE | 2 |
| ISS-DBLOGW-INPUT | 1 |
| ISS-DBLOGW-PACKET | 1 |
| ISS-DBLOGW-SEQUENCE | 2 |
| ISS-DBLOGW-STUCK | 1 |
| ISS-DBLOGW-TRANSPORT | 33 |
| ISS-INTEG-001 | 2 |
| ISS-INTEG-002 | 12 |
| ISS-INTEG-003 | 6 |
| ISS-INTEG-CACHE | 7 |
| ISS-INTEG-CONFIG | 38 |
| ISS-INTEG-DATAAPPLY | 35 |
| ISS-INTEG-DB | 113 |
| ISS-INTEG-FILE | 50 |
| ISS-INTEG-GENERIC | 80 |
| ISS-INTEG-HTTP | 21 |
| ISS-INTEG-INPUT | 23 |
| ISS-INTEG-PACKET | 10 |
| ISS-INTEG-SEQUENCE | 7 |
| ISS-INTEG-STUCK | 11 |
| ISS-INTEG-TRANSPORT | 11 |
| ISS-IREP-CDT-001 | 1 |
| ISS-IREP-CDT-002 | 9 |
| ISS-IREP-CDT-003 | 4 |
| ISS-IREP-CFG-001 | 15 |
| ISS-IREP-DCS-001 | 6 |
| ISS-IREP-DCS-002 | 14 |
| ISS-IREP-DCS-003 | 11 |
| ISS-IREP-DCS-004 | 2 |
| ISS-IREP-DES-001 | 6 |
| ISS-IREP-DES-002 | 10 |
| ISS-IREP-DES-003 | 9 |
| ISS-IREP-RBP-001 | 9 |
| ISS-IREP-STUCK-001 | 4 |
| ISS-IREXP-CACHE | 32 |
| ISS-IREXP-CONFIG | 32 |
| ISS-IREXP-DATAAPPLY | 66 |
| ISS-IREXP-DB | 35 |
| ISS-IREXP-FILE | 17 |
| ISS-IREXP-GENERIC | 14 |
| ISS-IREXP-HTTP | 20 |
| ISS-IREXP-INPUT | 1 |
| ISS-IREXP-PACKET | 9 |
| ISS-IREXP-SEQUENCE | 13 |
| ISS-IREXP-STUCK | 3 |
| ISS-IREXP-TRANSPORT | 1 |
| ISS-IRIMP-CACHE | 39 |
| ISS-IRIMP-CONFIG | 42 |
| ISS-IRIMP-DATAAPPLY | 79 |
| ISS-IRIMP-DB | 77 |
| ISS-IRIMP-FILE | 46 |
| ISS-IRIMP-GENERIC | 29 |
| ISS-IRIMP-HTTP | 17 |
| ISS-IRIMP-INPUT | 4 |
| ISS-IRIMP-PACKET | 31 |
| ISS-IRIMP-SEQUENCE | 35 |
| ISS-IRIMP-STUCK | 15 |
| ISS-IRIMP-TRANSPORT | 2 |
| ISS-IRPBR-CACHE | 10 |
| ISS-IRPBR-CONFIG | 7 |
| ISS-IRPBR-DATAAPPLY | 3 |
| ISS-IRPBR-DB | 11 |
| ISS-IRPBR-FILE | 13 |
| ISS-IRPBR-GENERIC | 3 |
| ISS-IRPBR-HTTP | 2 |
| ISS-IRPBR-INPUT | 2 |
| ISS-IRPBR-PACKET | 34 |
| ISS-PLATFORM-BENIGN | 30 |
| ISS-PR-001 | 1 |
| ISS-PRRECV-CONFIG | 28 |
| ISS-PRRECV-DATAAPPLY | 12 |
| ISS-PRRECV-DB | 67 |
| ISS-PRRECV-FILE | 87 |
| ISS-PRRECV-GENERIC | 27 |
| ISS-PRRECV-HTTP | 19 |
| ISS-PRRECV-INPUT | 15 |
| ISS-PRRECV-PACKET | 75 |
| ISS-PRRECV-SEQUENCE | 40 |
| ISS-PRRECV-STUCK | 10 |
| ISS-PRRECV-TRANSPORT | 2 |
| ISS-PRSEND-CONFIG | 4 |
| ISS-PRSEND-DATAAPPLY | 1 |
| ISS-PRSEND-DB | 31 |
| ISS-PRSEND-FILE | 52 |
| ISS-PRSEND-GENERIC | 32 |
| ISS-PRSEND-HTTP | 7 |
| ISS-PRSEND-INPUT | 50 |
| ISS-PRSEND-PACKET | 36 |
| ISS-PRSEND-SEQUENCE | 9 |
| ISS-SBUS-001 | 7 |
| ISS-SBUS-002 | 13 |
| ISS-SYNC-CACHE | 2 |
| ISS-SYNC-CONFIG | 46 |
| ISS-SYNC-DATAAPPLY | 19 |
| ISS-SYNC-DB | 24 |
| ISS-SYNC-FILE | 36 |
| ISS-SYNC-GENERIC | 18 |
| ISS-SYNC-HTTP | 9 |
| ISS-SYNC-INPUT | 20 |
| ISS-SYNC-PACKET | 20 |
| ISS-SYNC-SEQUENCE | 2 |
| ISS-SYNC-STUCK | 8 |
| ISS-SYNC-TRANSPORT | 170 |
| ISS-TRANSFER-001 | 6 |
| ISS-XFER-CACHE | 3 |
| ISS-XFER-CONFIG | 5 |
| ISS-XFER-DB | 7 |
| ISS-XFER-FILE | 11 |
| ISS-XFER-GENERIC | 2 |
| ISS-XFER-INPUT | 4 |
| ISS-XFER-PACKET | 7 |

## Service by class

How the failure points of each service split across failure classes (HAND = matched a hand-written card). Keywords: service, failure class.

| Service | HAND | BENIGN | SEQUENCE | PACKET | TRANSPORT | STUCK | CACHE | DATAAPPLY | CONFIG | HTTP | FILE | INPUT | DB | GENERIC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ComINT | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ComPBR | 1 |  |  | 34 |  |  | 10 | 3 | 7 | 2 | 13 | 2 | 11 | 3 |
| ExportCDT | 25 |  |  | 3 |  |  | 16 | 38 | 14 | 2 | 1 |  | 13 |  |
| ExportDCS | 33 |  | 13 | 6 | 1 | 3 | 16 | 28 | 18 | 18 | 16 | 1 | 22 | 14 |
| ImportDES | 36 |  | 35 | 31 |  | 15 | 11 | 40 | 29 | 12 | 34 | 4 | 37 | 26 |
| ImportDSC | 9 |  |  |  | 2 |  | 14 | 22 | 6 | 3 | 7 |  | 19 |  |
| ImportRBP | 19 |  |  |  |  |  | 14 | 17 | 7 | 2 | 5 |  | 21 | 3 |
| RepAckn |  | 1 | 4 | 1 |  |  |  | 9 | 9 | 16 | 1 | 4 | 13 | 2 |
| RepAcquisition |  |  | 31 | 14 | 2 | 10 |  | 3 | 17 | 3 | 44 | 4 | 33 | 25 |
| RepAzure | 3 |  |  | 4 | 14 | 3 |  | 17 | 9 | 4 | 4 | 10 | 1 | 2 |
| RepAzureRes | 9 |  |  | 16 | 43 | 1 |  |  | 22 | 2 | 19 | 5 | 1 | 3 |
| RepCompression |  |  |  | 14 |  |  |  |  |  |  | 2 | 9 | 1 | 2 |
| RepDBLogW | 3 |  | 2 | 1 | 33 | 1 |  | 4 | 4 |  | 2 | 1 | 34 |  |
| RepDecompress |  |  | 2 | 47 |  |  |  |  | 1 |  | 20 | 4 | 1 |  |
| RepFileMerge | 1 |  | 3 | 13 |  |  |  |  | 1 |  | 22 | 3 |  |  |
| RepIntegration | 24 |  | 7 | 10 | 11 | 11 | 7 | 35 | 38 | 21 | 50 | 23 | 113 | 80 |
| RepMedium |  |  |  |  |  |  |  |  |  |  |  |  | 3 |  |
| RepPacketCreation |  |  | 7 | 9 |  |  |  |  | 3 | 3 | 35 | 23 | 12 | 14 |
| RepPacketInterim |  |  | 1 |  |  |  |  | 1 |  |  |  |  | 4 |  |
| RepProData |  |  | 1 |  |  |  |  |  | 1 | 2 |  | 3 | 4 | 7 |
| RepQueueManage |  |  |  |  |  |  |  |  |  |  |  | 3 | 4 | 1 |
| RepSaveData |  |  |  |  |  |  |  |  |  |  |  |  | 20 |  |
| RepSbus | 19 |  | 2 |  | 113 | 4 | 2 | 2 | 15 | 3 | 13 | 5 | 22 | 13 |
| RepSplit |  |  |  | 13 |  |  |  |  |  |  | 1 | 12 | 1 |  |
| RepTrack |  |  |  |  |  |  |  |  |  | 2 | 14 |  | 2 | 8 |
| RepTransfer | 4 |  |  | 7 |  |  | 3 |  | 5 |  | 11 | 4 | 7 | 2 |

## Regex check

2430 regexes match their source line; 8 are multi-line calls or have no literal text (they match by exception text or code location only). Keywords: regex, signature check.
