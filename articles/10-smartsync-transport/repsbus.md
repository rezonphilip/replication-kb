---
doc_id: CMP-REPSBUS
type: component
mechanism: [smartsync]
group: smartsync-transport
runs_on: [office, vessel]
components: [RepSbus]
log_files: [SbusLog_.txt]
error_types: []
applies_to_versions: ["Not determined from code"]
sources: ["MS-REP snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# RepSbus — SmartSync Service Bus messaging

RepSbus sends and receives SmartSync messages over Azure Service Bus: packet-transfer notices, acknowledgements, service-info and general notifications, for both office↔vessel and vessel↔vessel (V2V). It keeps a queue listener running in the background. If the listener is down, the other side never learns that a packet is waiting, so downloads and acknowledgements stop even though uploads may still succeed.

## Role in replication

RepSbus is the signalling half of SmartSync: files travel through Azure Blob (RepAzure / RepAzureRes), and RepSbus tells the other end about them. Keywords: service bus, SmartSync, notification, queue, listener, receiver, acknowledgement, V2V.

- Other services call RepSbus to send: RepIntegration (notifications, updates, receiver status), RepAzure (`SbusSend/SendAcknowledgement`), and others listed in `inventory/ms-rep.md`.
- Incoming messages are dispatched by `NotificationType` in `MessageHandler` (`RepSbus/MariApps.PAL.Rep.Sbus.Service/BL/ServiceBusBL.cs#L313-L633`). Types handled: `PACKET_TRANSFER`, `ACKNOWLEDGMENT_NOTIFICATION`, `SERVICE_INFO`, `GENERAL_NOTIFICATION`, `PACKET_TRANSFER_V2V`, `ACKNOWLEDGMENT_NOTIFICATION_V2V`, `PACKET_TRANSFER_V2V_SEND_ACKN`, `PACKET_TRANSFER_V2V_RECEIVE_ACKN`, `PACKET_TRANSFER_V2V_DOWNLOAD_ACKN` (same file, L328-L425).
- On receiving `PACKET_TRANSFER` (or the V2V variant) it replies with an `ACKNOWLEDGMENT_NOTIFICATION` (or `_V2V`) (L328-L331, L366-L369).
- A message whose vessel data does not match is logged as `MessageHandler | Wrong vessel data | Data:` (L447).

## How it runs

A background worker checks the listener every `ReceiverCheckIntervalInMinutes` and restarts it when needed. Keywords: worker, listener not running, restart receiver, interval, StartListener.

1. Each cycle loads common data and calls `StartListener` (`RepSbus/MariApps.PAL.Rep.Sbus.Service/WorkerService.cs#L105`).
2. `StartListener` refuses to start if there is no internet (`{MethodName}| Internet not available`, `BL/ServiceBusOperation.cs#L73`), if the service's initial status is not ready (L86), or if access verification fails (`Service Bus Access failed with error {Error}`, L101). If the receiver was stopped it restarts it (L131).
3. If start fails the worker logs `Service bus listener is not running due to {ErrorMessage}` (`WorkerService.cs#L109`) and, when at least `RestartReciverIntervalInDays` days have passed since the last forced restart, restarts the receiver (L111-L121).
4. A health check counts handled messages and errors; `{MethodName}|Processor is not processing` (`BL/ServiceBusOperation.cs#L526`) means the processor exists but is not consuming.
5. On service stop, a vessel instance sends a stop notification to the office queue (`SendQueueName`); an office instance (`Location` = `OFF`) does not (`WorkerService.cs#L59-L72`).

Hosting: `Urls` in `appsettings.json` binds the HTTP API (port 5055 by default in repo appsettings).

## API routes

All routes are under `SbusSend` (`RepSbus/MariApps.PAL.Rep.Sbus.Service/Controllers/SbusSendController.cs`). Keywords: SbusSend, SendNotification, ReceiverStatus, RestartReceiver, SbusVerifyAccess.

| Route | Purpose | Line |
|---|---|---|
| `SendNotification` | Send a packet/transfer notification | L31 |
| `SendNotificationGeneric` | Generic notification | L41 |
| `SendAcknowledgement` | Send an acknowledgement (used by RepAzure) | L54 |
| `SendNotificationV2V` | V2V notification | L63 |
| `SendUpdate` / `SendUpdateV2V` | Update messages | L72 / L82 |
| `StartReceive` | Start the listener on demand | L93 |
| `ReceiverStatus` | Report listener status (used by RepIntegration health checks) | L102 |
| `RestartReceiver` | Force a listener restart | L111 |
| `SbusVerifyAccess` | Test Service Bus credentials/connectivity | L120 |
| `TestService`, `GetVersion`, `ReadStaticVariable` | Health/diagnostics | L130-L146 |

`AdminController` adds `api/Admin/Message/Meta` (`Controllers/AdminController.cs#L24`). A `TroubleshootLauncher` exists, gated by `TroubleshootRunSettings:Enabled` (off by default in repo appsettings).

## Configuration

RepSbus reads its Service Bus credentials and queue names from the database through RepDBLogW, and its tuning from `appsettings.json`. Keywords: connection string, queue name, credentials, ServiceBusSettings, appsettings.

| Key | Where | Effect |
|---|---|---|
| `REP_SERVICEBUS_CONNECTION_STRING` **(secret)** | `REP.REP_SERVICEBUS_CREDENTIALS` (read by `REP.REP_GET_SBUS_SETTINGS`; the CO_Parameters row may be empty — DATA-MSREP-OVERVIEW) | Service Bus connection. Missing → `service bus connection string and basic info is not found` (`BL/CommonDataConduit.cs#L76`). |
| Queue names / `SendQueueName` / `Location` | Queue names from `REP.REP_PR_SUBSCRIBER_LIST` (`REP.REP_GET_QUEUE_NAME`); location from CO_Parameters `REP_LOCATION`; all read via RepDBLogW `DbServiceSbus` routes | Missing → `Queue name is not found` (`BL/CommonDataConduit.cs#L111`), `Queue name not found found in config` (L261). |
| `REP_INTERGRATION_BASE_URL`, `REP_INTERGRATION_API_URL` | CO_Parameters | Where RepSbus calls RepIntegration. |
| `REP_WINDOWS_SERVICE` | CO_Parameters | Name used for Windows-service checks. Exact use: Not determined from code. |
| `ReceiverCheckIntervalInMinutes`, `RestartReciverIntervalInDays` | appsettings `BasicSettings` | Worker interval and forced-restart spacing. |
| `ServiceBusSettings:*` (`MaxConcurrentCalls`, `PrefetchCount`, `MaxRetryCount`, `LockDurationInMinutes`, `UseWebSockets`, `UseWebProxy`) | appsettings | Processor behaviour; `UseWebSockets` matters on networks that block AMQP port 5671 (general Azure Service Bus behaviour, not shown in this code; RepIntegration's config check probes `ConfigEvaluationOptions:ServiceBusPort`). |
| `IsQueueCreate` / `EnableQueueCreation` | appsettings | Whether a missing queue is created automatically (`BL/ServiceBusOperation.cs#L202-L208`, L265-L293). |
| `MessageReceiveTimeoutInH`, `ErrorNotificationLimit`, `Encryption` | appsettings | Receive timeout, error notification cap, payload encryption mode. |

## Logs and what to look for

Log: `SbusLog_.txt` in the folder set at deployment (`$__LOG__$`). Keywords: SbusLog, listener, receiver, credentials, queue not found.

| Message (template) | Meaning | Source |
|---|---|---|
| `Service bus listener is not running due to {ErrorMessage}` | Listener could not start this cycle; the reason follows. | `WorkerService.cs#L109` |
| `Internet not available` | Machine has no internet; nothing else will work. | `BL/ServiceBusOperation.cs#L73` |
| `Service Bus Access failed with error {Error}` | Credential/firewall/namespace problem. | `BL/ServiceBusOperation.cs#L101` |
| `Service bus credentials not found for {KeyName}` | DB has no credential row for this key. | `BL/CommonDataConduit.cs#L227` |
| `Queue {QueueName} is not active or created, creating it` / `Queue creation failed for {QueueName} with error {Error}` | Queue missing; auto-create attempted. | `BL/ServiceBusOperation.cs#L202`, `#L208` |
| `Processor is not processing` | Listener registered but not consuming. | `BL/ServiceBusOperation.cs#L526` |
| `Receiver start failed with status {ReceiverStartStatus}` | Restart attempt failed. | `BL/ServiceBusOperation.cs#L155` |
| `FAILED:ServiceBusSend: Message:` | Sending a message failed. | `BL/ServiceBusBL.cs#L1201` |
| `MessageHandler | Wrong vessel data` | Received message for another vessel/config mismatch. | `BL/ServiceBusBL.cs#L447` |
| `ErrorHandler:` | Exception raised by the Service Bus processor. | `BL/ServiceBusBL.cs#L638` |

## Common failure points

Keywords: service bus down, no acknowledgement, listener stopped, port 5671 blocked, credentials missing.

- Listener not running (no internet, AMQP blocked, bad credentials) → ISS-SBUS-001.
- Credentials or queue name missing in DB → ISS-SBUS-002.
- Queue missing and auto-create disabled or failing → ISS-SBUS-002.
- RepDBLogW unreachable: RepSbus cannot load its settings at all (it reads them through RepDBLogW) → check CMP-REPDBLOGW.

## Related

- PLT-MSREP-OVERVIEW, CMP-REPAZURE, CMP-REPAZURERES, CMP-REPDBLOGW, FLW-PR-EXPORT
- ISS-SBUS-001, ISS-SBUS-002
