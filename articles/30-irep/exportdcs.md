---
doc_id: CMP-EXPORTDCS
type: component
mechanism: [irep, smartsync]
group: irep-export
runs_on: [office, vessel]
components: [ExportDCS]
log_files: [DcsServicePalLog_.txt]
error_types: [config, sequence, http, file, stuck]
applies_to_versions: ["Not determined from code"]
sources: ["iRep snapshot staged 2026-11-11 (no git commit available)"]
status: draft
author: claude
reviewed_by: ""
last_verified: 2026-11-11
---

# ExportDCS — packet creation, transfer hand-off and resend

ExportDCS turns REP2X record-vessel-sync rows into `.tzst` packets, one vessel at a time. For each packet it moves the files to the outbox, increases the vessel packet counter, and asks RepIntegration to transfer it. It then records the packet in OutPacketHd. It also runs the automatic resend and the hourly directory resend. Most "data changed but nothing arrived" cases with a healthy CDT end here.

## How it runs

ExportDCS starts from its own timer or from a call by ExportCDT, and only when three conditions hold. Keywords: DCS worker, InvokeAllReplicaTypeWorker, InitateExportProcess, CheckDcsStatus, config status, export start skipped.

- **Timer.** The worker calls `InvokeAllReplicaTypeWorker` every `CheckIntervalInMin` minutes when `InitiateOnInterval` is true. The directory resend runs every `DirectoryAutoResentIntervalInH` hours (`ExportDCS/Mariapps.PAL.RepExportDCS/WorkerService.cs#L44-L80`).
  - **The loop has no generic catch**; it only catches cancellation (L83). One unhandled exception ends the worker until the service restarts.
  - With `CheckIntervalInMin` = 0 the delay is 0 and the loop spins.
- **Per replica type** (`ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L316-L377`):
  - The init data (vessel lists, configuration, table order) is re-read into the cache only when neither the export queue nor the resend queue is running. Otherwise it warns "Export Queue or resend Queue already running so not changing cache data" (L316-L328).
  - It then starts the export (L333-L335) and the auto resend (L349-L351).
- **Start gate** (`InitateExportProcess`, `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L397-L434`). The export starts only when all three checks pass:
  1. **DCS status:** no process meta information is left in memory.
  2. **Config status:** the startup configuration cache flag is true. If it is false, "Config Status is false, ReInitialize the Service startup config" is logged (`ExportDCS/Mariapps.PAL.RepExportDCS/BL/DataConduitMethods/ExportDataConduitBL.cs#L738`).
  3. **Export queue:** the export queue is free.

  Otherwise it logs the **Warning** "Export process start skipped. {DcsMessage} | {ConfigMessage} | {ExportMessage}". At the default Error level this warning is invisible (ISS-IREP-DCS-001).
- The export itself runs in a background task tied to the host, not to the HTTP request (L408-L418). A call from ExportCDT therefore returns at once.

## Export per vessel

`RepExportProcessQ` builds packets vessel by vessel (`ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ExportBL.cs#L65-L217`). Keywords: unique code, awaiter, invalid config vessel, packet counter, OutPacketHd, packet creation crashed.

1. Read the error awaiter timer (`REP_PROCESS_AWAIT_TIME`) and the client details (L78-L80).
2. Check the client details. If Unique Code or Unique Id is empty or 0, a **Critical** line is logged and the process exits (L95-L101, ISS-IREP-DCS-004).
3. Check the awaiter. If an earlier vessel error is still within its wait time, "Awaiter status is failed, exiting process" is logged (L111-L115).
4. Build the vessel meta list. Vessels on the invalid-config skip list are left out (L120-L138).
5. For each vessel:
   - Verify the export path configuration. On failure: "Error while path configuration for Vessel" (L153-L157, ISS-IREP-DCS-002).
   - Read the packet counter (L243).
   - Read the vessel config path (L263-L267).
   - Read the pending table ids (L276).
   - Generate the packet (attachment tables first, then data tables) (L464-L478).
6. Handle the packet (`HandlePacketTransport`, L482-L549):
   1. Move the files to the outbox. On failure: "Packet Move Status … FAILED", and the step throws.
   2. Update the vessel packet counter. On failure: "Error updating packet counter", and the step throws.
   3. Call `StartPacketTransfer` → RepIntegration `Integration/TransferGeneral`. On failure: "Packet Transfer Failed for Vessel", **but processing continues**.
   4. Save OutPacketHd. On failure: "Error saving to OutPacketHd".
   5. **Return SUCCESS whatever the transfer result was.** A transfer failure is repaired only by auto resend or directory resend (ISS-IREP-DCS-003).
7. If a vessel loop fails, ExportDCS logs "Error in … in loop for vessel". It deletes the vessel from the cache, which logs "Cache Delete status …" at Error level although it is a status line. It inserts an awaiter row, which logs "Awaiter Insert status …", also at Error level and also a status line (L413-L437). The next cycle then waits `REP_PROCESS_AWAIT_TIME` before exporting again.
8. Delete the processed record-vessel-sync rows (L189-L194), then call the "next service" (L207). services.json points the next service back at `ExportDcs/InitateExportProcess`, so DCS re-triggers itself to pick up remaining work (`ExportDCS/Mariapps.PAL.RepExportDCS/services.json`).

**Packet counter order matters.** The counter is updated **before** the transfer. If the transfer fails and resend later gives up (`REP_RESENT_LIMIT`), the receiver sees a gap and stops that vessel at the missing counter (ISS-IREP-DES-002).

## Resend

ExportDCS resends packets that were not acknowledged in time, plus any files left in transfer directories. Keywords: auto resend, InitiateAutoResent, directory resend, REP_RESENT_LIMIT, REP_RESENT_AWAIT_TIME_IN_MIN, transfer service not reachable.

- **Auto resend.** It runs per replica type when it is requested or when `AutoResentIntiateOnInterval` is set (`ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L349-L351`).
  - It reads the candidates from REP2X (resend log, OutPacketHd) using `REP_RESENT_LIMIT` and `REP_RESENT_AWAIT_TIME_IN_MIN`; see CFG-IREP.
  - After a configured number of consecutive transfer failures it stops the run: "Transfer service not reachable for {FailureCount} consecutive attempts, stopping resend" (`ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L141`).
- **Directory resend.** It scans the transfer directories every `DirectoryAutoResentIntervalInH` hours. If it is not enabled it logs "Directory resent is not enabled" (Warning, `ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/Common/CommonProcessBL.cs#L232`).
  - It checks that the number of files matches the packet's split count: "File count does not match split count" (`ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/DcsTransportHandler.cs#L226`).
  - On failure it moves files to the error folder (`ExportDCS/Mariapps.PAL.RepExportDCS/BL/Main/ResendBL.cs#L281`).

## Routes

All routes are under `ExportDcs/` (`ExportDCS/Mariapps.PAL.RepExportDCS/Controllers/RepExportDCSController.cs`). Keywords: InitateExportProcess route, DeleteAllCacheKeys, InitiateAutoResent, Initiate-Directory-Resend.

| Route | Purpose | Line |
|---|---|---|
| `SetAllInitData` | Reload the startup configuration into the cache (fixes "Config Status is false") | L29 |
| `InitateExportProcess` | Start the export (called by ExportCDT) | L36 |
| `DeleteCacheKey`, `DeleteAllCacheKeys` | Clear stale cache or running flags | L43, L50 |
| `InitiateAutoResent`, `Initiate-Directory-Resend` | Run the resends now | L57, L64 |
| `GetVersion`; `EvaluateConfig` (ConfigEvaluationController) | Version and configuration check | L71 |

## Failure-point coverage

The specific cards are ISS-IREP-DCS-001 to -004, ISS-IREP-STUCK-001 and ISS-IREP-DES-002 (receiver effect). All other templates fall under ISS-IREXP-*. Keywords: DCS errors.

## Related

PLT-IREP, CMP-EXPORTCDT, CMP-REPINTEGRATION, CMP-REPTRANSFER, FLW-IREP-EXPORT, CFG-IREP, ISS-IREP-DCS-001, ISS-IREP-DCS-002, ISS-IREP-DCS-003, ISS-IREP-DCS-004
