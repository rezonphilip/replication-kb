# usage: python3 -I gen_class_cards.py <kb_root>
# Generates one issue card per (service group, failure class) from catalog/failure-points.yaml, so that every
# failure point in the code lands on a card with symptoms, phrasings, checks and solutions. Hand-written cards
# (issues/ISS-*.yaml without `generated: true`) are never touched; they take precedence in the catalogue.
import yaml, sys, collections, re, os, glob

KB = sys.argv[1].rstrip('/')
R = yaml.safe_load(open(f'{KB}/tools/failure_rules.yaml'))
FP = yaml.safe_load(open(f'{KB}/catalog/failure-points.yaml'))['failure_points']
CLS = {c['id']: c['title'] for c in R['classes']}

MECH_WORDS = {
    'priority-replication': ['PR', 'priority replication', 'priority rep', 'PR replication'],
    'smartsync': ['smartsync', 'smart sync', 'sync transport', 'azure transfer'],
    'irep': ['sync+', 'smartsync+', 'irep', 'i-rep'],
}
RELATED = {
    'SYNC': ['CMP-REPSBUS', 'CMP-REPAZURE', 'CMP-REPAZURERES'],
    'XFER': ['CMP-REPTRANSFER'],
    'INTEG': ['CMP-REPINTEGRATION', 'FLW-PR-EXPORT', 'FLW-PR-IMPORT'],
    'DBLOGW': ['CMP-REPDBLOGW', 'DATA-MSREP-OVERVIEW'],
    'PRSEND': ['FLW-PR-EXPORT', 'DATA-MSREP-STATUS'],
    'PRRECV': ['FLW-PR-IMPORT', 'DATA-MSREP-STATUS'],
    'IRCFG': ['CMP-COMINT', 'PLT-IREP'],
    'IREXP': ['CMP-EXPORTCDT', 'CMP-EXPORTDCS', 'FLW-IREP-EXPORT'],
    'IRIMP': ['CMP-IMPORTDES', 'CMP-IMPORTDSC', 'CMP-IMPORTRBP', 'FLW-IREP-IMPORT'],
    'IRPBR': ['CMP-COMPBR', 'PLT-IREP'],
}

# Class guidance. {svcs} = services of the group, {logs} = their log files, {mech} = mechanism name.
TEXT = {
 'SEQUENCE': dict(
  symptoms=['Packets stop being applied for one vessel while other vessels continue.', 'Logs report an old, duplicate, missing or out-of-order packet counter.', 'Dashboard shows a growing gap between the last sent and the last applied packet number.'],
  seeds=['packet counter mismatch', 'missing packet', 'packets out of order', 'old packet received', 'duplicate packet', 'packet number gap', 'vessel stuck waiting for packet', 'later packets not applied', 'sequence error', 'counter not latest', 'packet already processed', 'resend missing packet', 'packet skipped'],
  checks=[('Compare the last packet number sent by the sender with the last packet number applied by the receiver for the vessel (read-only queries in the data articles).', 'gap exists -> a packet is missing or failed; find it in the error/skip lists', 'no gap -> look at the receiver queue status instead'),
          ('Search the receiver error folder and the skipped/error packet tables for the missing counter.', 'packet is there -> fix its cause (see PACKET/DATAAPPLY cards) and reprocess', 'packet never arrived -> request a resend from the sender')],
  solutions=[('Get the missing packet re-sent', 'One or more counters are missing on the receiving side.', [('Identify vessel, replica/channel and the first missing counter from the log line.', 'support', False, 'Counter and vessel known.'), ('Trigger the resend for that counter through the documented resend route or table (never edit counters by hand).', 'dev', True, 'Packet arrives and the counter advances.')]),
             ('Release an old or duplicate packet', 'The packet number is lower than or equal to the last applied one.', [('Confirm the packet really was applied before (status tables).', 'support', False, 'Applied status found.'), ('Let the service move it to the error/old folder; no data action needed.', 'support', False, 'No repeat of the message for that counter.')])]),
 'PACKET': dict(
  symptoms=['Packet files are moved to an error folder or skipped.', 'Logs report invalid packet names, missing split parts, checksum or decompression errors.', 'A packet is received but never reaches the import queue.'],
  seeds=['packet corrupt', 'invalid packet name', 'split file missing', 'checksum mismatch', 'crc failed', 'cannot extract packet', 'decompress error', 'zip error', 'packet moved to error folder', 'packet incomplete', 'chunk missing', 'tzst invalid', 'file size mismatch'],
  checks=[('Open the error/incoming folder and check whether all split parts of the packet exist with the expected size.', 'parts missing or zero size -> transfer incomplete; wait or request resend', 'all parts present -> file is damaged or not meant for this site'),
          ('Read the packet name: unique code, destination, type and counter must match the receiving environment.', 'mismatch -> packet was routed to the wrong site; do not import', 'match -> treat as corrupt and request resend')],
  solutions=[('Request a clean resend of the packet', 'The packet is incomplete or corrupt.', [('Note vessel, packet name and counter from the log.', 'support', False, 'Details recorded.'), ('Request a resend from the sending side and move the bad copy out of the inbox.', 'dev', True, 'New copy validates and imports.')]),
             ('Correct routing configuration', 'The packet belongs to another site or replica type.', [('Compare the destination and unique code in the name with the receiver configuration.', 'dev', False, 'Mismatch identified.'), ('Fix the sender/receiver configuration (vessel object id, unique code).', 'dev', True, 'New packets carry the right destination.')])]),
 'TRANSPORT': dict(
  symptoms=['Files wait in the outbox or download queue and are not delivered.', 'Logs mention Azure storage, Service Bus, network or upload/download failures.', 'Transfers resume after network recovers or a service restart.'],
  seeds=['azure upload failed', 'blob download error', 'no network on ship', 'service bus not connecting', 'smartsync not sending', 'files stuck in outbox', 'upload slow', 'storage key invalid', 'container not found', 'chunk upload error', 'download stuck', 'satellite link down', 'transfer paused'],
  checks=[('Check network reachability from the server to Azure (storage and Service Bus endpoints) and whether other vessels transfer.', 'only this site fails -> local network/firewall/proxy', 'all sites fail -> Azure account, key or service side'),
          ('Run the read-only settings presence scripts (Azure/Service Bus) for the site.', 'setting missing or empty -> restore configuration', 'settings present -> look at storage/Service Bus access and quotas')],
  solutions=[('Restore connectivity or credentials', 'Network down or credentials invalid.', [('Confirm network path and proxy rules with infrastructure.', 'support', False, 'Endpoint reachable.'), ('Restore/rotate the storage or Service Bus credential in the configured source (never paste secrets in tickets).', 'dev', True, 'Next cycle uploads/downloads succeed.')]),
             ('Let the queue drain', 'Transient failure that has cleared.', [('Watch the next cycles; failed items are retried by the service.', 'support', False, 'Queue count decreases.')])]),
 'STUCK': dict(
  symptoms=['A service stops processing without new errors.', 'Logs say a process is already running, a time limit was exceeded or a run was skipped.', 'Processing resumes after the reset interval or a service restart.'],
  seeds=['process already running', 'service stuck', 'nothing happening', 'queue not moving', 'export skipped', 'import skipped', 'time limit exceeded', 'worker crashed', 'needs restart to work', 'hangs', 'process flag stuck', 'waiting timer', 'retry limit reached'],
  checks=[('Look for the last successful cycle line and any "already running", "time exceeded" or crash line in {logs}.', 'flag/time line found -> in-memory running flag or wait timer is blocking', 'nothing logged -> check that the worker is enabled and the interval setting is not zero'),
          ('Check whether a long database call or HTTP call is still running (SQL activity, service response).', 'still running -> wait for timeout before restarting', 'nothing running -> the flag is stale')],
  solutions=[('Clear a stale running flag', 'The run ended abnormally and the in-memory flag was not cleared.', [('Use the service clear/reset route if available, otherwise restart the service in a quiet period.', 'support', True, 'Next cycle logs a start and progress.')]),
             ('Fix scheduler settings', 'Worker disabled or interval misconfigured.', [('Check the WorkerServiceSettings/BasicSettings interval and enable flags (names only).', 'dev', True, 'Worker runs on schedule.')])]),
 'CACHE': dict(
  symptoms=['Logs report cache read/write/delete failures or data "not found in cache, reading from DB".', 'Behaviour changes after cache clear or service restart.', 'Stale configuration is used after a configuration change.'],
  seeds=['cache error', 'redis not reachable', 'stale config', 'cache not updated', 'clear cache', 'old settings still used', 'cache key missing', 'memory cache issue', 'after change nothing happens', 'need to reset cache', 'cache set failed', 'dictionary error', 'active vessel list wrong'],
  checks=[('Check DataConduitSettings:ConduitType (StaticData or RedisCache) and, for Redis, that the cache server is reachable.', 'Redis unreachable -> infrastructure', 'static/in-memory -> data is rebuilt from DB; check the DB step'),
          ('After a configuration change, check whether the cache was cleared (ClearAllCache/DeleteAllCacheKeys routes).', 'not cleared -> clear and observe', 'cleared -> the DB value itself is wrong')],
  solutions=[('Clear the service cache', 'Cached data is stale or corrupt.', [('Call the documented cache-clear route for the service and replica type.', 'support', True, 'Next cycle reads fresh data.')]),
             ('Restore cache server', 'Redis is not reachable.', [('Escalate to infrastructure with the cache host name from configuration (do not paste credentials).', 'support', False, 'Cache reachable.')])]),
 'DATAAPPLY': dict(
  symptoms=['Rows are skipped, rejected or not applied to the target tables.', 'Logs report bulk-copy, column, schema, data type, change tracking or replica-table errors.', 'Some tables replicate while others stay behind.'],
  seeds=['rows not replicated', 'bulk insert failed', 'column missing', 'schema mismatch', 'data type error', 'table not updating on vessel', 'table not updating in office', 'change tracking not enabled', 'replica table error', 'data skipped', 'insert failed', 'update not applied', 'delete not applied'],
  checks=[('Identify table id/name from the log and compare the column list on both sides (sender query vs receiver table).', 'column/type differs -> schema drift; align schema', 'same -> check the query configuration for the table'),
          ('For change tracking errors, check that change tracking is enabled on the source database and table.', 'not enabled -> enable it (DBA) and re-run', 'enabled -> check the configured query text')],
  solutions=[('Align schema or configuration', 'Table structure or configured query does not match.', [('Record table id/name and the exact SQL message.', 'support', False, 'Details recorded.'), ('DBA/dev aligns the table or the configured query; rerun the cycle.', 'dev', True, 'No new errors for the table; rows applied.')]),
             ('Reprocess skipped rows', 'Rows were skipped after the fix.', [('Use the documented reprocess route/table for the replica type.', 'dev', True, 'Skipped rows applied.')])]),
 'CONFIG': dict(
  symptoms=['A service stops at start of a cycle with a "not configured", "not found" or "null or empty" message.', 'Problems start after install, upgrade, database restore or a move to a new server.', 'Only one site or one replica/channel is affected.'],
  seeds=['config missing', 'setting not found', 'base url empty', 'api url not configured', 'services.json wrong', 'connection string missing', 'co parameters missing', 'after upgrade not working', 'new vessel setup fails', 'after db restore stopped', 'endpoint not configured', 'table settings missing', 'wrong path configured'],
  checks=[('Use the service EvaluateConfig/ConfigEvaluation route (if present) or the read-only presence scripts to list missing settings (names only).', 'missing -> restore from the deployment template/source', 'all present -> check values point to the right server/folder'),
          ('Compare with a working site of the same version.', 'differs -> configuration drift', 'same -> look at the DB/HTTP card for the step')],
  solutions=[('Restore missing configuration', 'A setting, parameter or settings row is missing or empty.', [('Name the missing key from the log.', 'support', False, 'Key named.'), ('Dev/ops restores it from the deployment source; never paste secret values.', 'dev', True, 'EvaluateConfig/presence script shows it present.'), ('Restart or clear cache if the service caches configuration.', 'support', True, 'Next cycle passes the configuration step.')])]),
 'HTTP': dict(
  symptoms=['A service logs failed, timed-out or rejected calls to another service.', 'The calling side retries or leaves items pending.', 'The called service may be stopped, overloaded or listening on another address.'],
  seeds=['service not reachable', 'api call failed', 'timeout calling service', 'http 500', 'http 404', 'bad gateway', 'next service not called', 'integration api error', 'transfer service down', 'connection refused', 'service unavailable', 'request timed out', 'endpoint wrong'],
  checks=[('Call the target service health/version route from the calling server.', 'unreachable -> service stopped or address wrong', 'reachable -> look at the target service log for the same time'),
          ('Compare the configured endpoint (services.json / microservices.json / settings table) with the actual route.', 'mismatch -> fix the endpoint', 'match -> target-side failure')],
  solutions=[('Restore the target service', 'Target stopped, crashed or overloaded.', [('Start/restart the target service (IIS/Windows service) and check its log.', 'support', True, 'Health/version route answers.')]),
             ('Correct the endpoint configuration', 'Wrong base address or route.', [('Fix the endpoint in the configuration source.', 'dev', True, 'Next call succeeds.')])]),
 'FILE': dict(
  symptoms=['Logs report missing files or folders, locked files, access denied or failed move/copy/delete.', 'Packets stay in inbox/outbox/work folders.', 'Problems after disk cleanup, antivirus scan, permission change or path change.'],
  seeds=['file not found', 'folder missing', 'access denied', 'file locked', 'cannot move file', 'disk full', 'antivirus locking files', 'path wrong', 'inbox folder empty', 'outbox not cleared', 'permission issue', 'file in use', 'work folder error'],
  checks=[('Check the folder from the log exists and the service account has modify rights.', 'missing/no rights -> create folder or grant rights', 'exists with rights -> check locks and disk space'),
          ('Check free disk space and whether antivirus/backup software locks the folder.', 'full/locked -> free space or exclude folder', 'ok -> configuration path may be wrong')],
  solutions=[('Fix folder, permissions or disk space', 'Folder missing, no rights or disk full.', [('Infrastructure creates the folder/grants rights/frees space.', 'support', True, 'Next cycle moves files.')]),
             ('Release locked files', 'Another process holds the file.', [('Identify the locking process and stop it or exclude the folder from scanning.', 'support', True, 'Lock cleared.')])]),
 'INPUT': dict(
  symptoms=['A route rejects a request as invalid (null, zero or missing values).', 'Usually follows another failure that produced empty data, or a manual/API call with wrong input.'],
  seeds=['invalid request', 'input is null', 'vessel id is 0', 'mandatory field missing', 'bad request', 'empty input', 'request rejected', 'manual call failed', 'invalid parameters', 'null value error', 'packet counter is 0', 'table settings id invalid', 'file location missing'],
  checks=[('Find the calling service and step just before the rejection in its log.', 'caller produced empty data -> follow that failure', 'manual/API call -> correct the input')],
  solutions=[('Fix the caller or the manual input', 'Bad input reached the route.', [('Correct the request (or the upstream failure) and retry.', 'dev', True, 'Route accepts the request.')])]),
 'DB': dict(
  symptoms=['Logs report stored procedure or database errors, timeouts, deadlocks or failed saves/reads.', 'Queues stop moving or items stay in an intermediate status.', 'Often after a database restore, upgrade without scripts, or heavy load.'],
  seeds=['database error', 'sql timeout', 'stored procedure not found', 'deadlock', 'save failed', 'could not read data', 'db connection failed', 'after db restore', 'missing column error', 'cannot insert null', 'sql exception', 'db slow', 'login failed'],
  checks=[('Read the SQL message after the log text (procedure not found, invalid column, timeout, login failed, NULL into ID).', 'object/column missing -> deployment scripts not applied (see data articles)', 'timeout/deadlock -> load or blocking'),
          ('Check the service connection string target is the right database and reachable (names only).', 'wrong/unreachable -> fix connection', 'correct -> DBA checks blocking and object state')],
  solutions=[('Apply missing database scripts', 'Procedure/column/default missing on this database.', [('Compare deployed objects with the inventory for the version.', 'dev', False, 'Missing object identified.'), ('Run the deployment script set for the site (office or vessel copy).', 'dev', True, 'Error no longer occurs.')]),
             ('Relieve load or blocking', 'Timeouts or deadlocks.', [('DBA identifies blocking sessions and long queries.', 'dev', True, 'Calls complete within timeout.')])]),
 'GENERIC': dict(
  symptoms=['An unexpected exception is logged with the method name and stack trace.', 'The step may be retried on the next cycle.'],
  seeds=['unexpected error', 'exception in service', 'object reference not set', 'null reference', 'error in method', 'unhandled exception', 'crash', 'stack trace in log', 'service error', 'something failed', 'general error', 'error occurred', 'unknown error'],
  checks=[('Read the exception type and message in the line after the log text.', 'matches a known class (DB, file, HTTP) -> use that card', 'NullReference or similar -> report to dev with the stack trace')],
  solutions=[('Escalate with evidence', 'Unknown or code-level failure.', [('Collect the log lines around the time (service, method, exception).', 'support', False, 'Evidence attached.'), ('Dev analyses and fixes; data correction only with approval.', 'dev', True, 'No recurrence.')])]),
}

TYPOS = {'packet': 'pakcet', 'vessel': 'vesel', 'replication': 'replciation', 'service': 'servise', 'error': 'eror', 'office': 'ofice', 'missing': 'mising', 'failed': 'faild'}

def phrasings(cls, grp, svcs, mech):
    seeds = TEXT[cls]['seeds']
    words = MECH_WORDS[mech]
    out = []
    for i, s in enumerate(seeds):
        out.append(f'{words[i % len(words)]} {s}')
    for i, s in enumerate(seeds[:6]):
        out.append(f'{s} on ship' if i % 2 == 0 else f'{s} in office')
    for i, sv in enumerate(svcs):
        out.append(f'{sv} {seeds[i % len(seeds)]}')
    for i, s in enumerate(seeds[:5]):
        t = s
        for a, b in TYPOS.items():
            if a in t:
                t = t.replace(a, b, 1); break
        out.append(t)
    seen, res = set(), []
    for p in out:
        if p.lower() not in seen:
            seen.add(p.lower()); res.append(p)
    return res[:45]

def q(s):
    return s

by = collections.defaultdict(list)
for e in FP:
    if e['card'].startswith('ISS-') and e['class'] not in ('HAND', 'BENIGN'):
        by[e['card']].append(e)

for f in glob.glob(f'{KB}/issues/*.yaml'):
    c = yaml.safe_load(open(f))
    if c.get('generated'):
        os.remove(f)

for card, items in sorted(by.items()):
    grp = items[0]['group']; cls = items[0]['class']
    g = R['groups'][grp]; svcs = sorted({e['service'] for e in items})
    logs = sorted({e['log_file'] for e in items if e['log_file']})
    mech = g['mechanism']
    # signatures: visible, direct regex, most specific first, distinct
    cand = [e for e in items if e['regex'] and e['source_check'] == 'ok' and len(e['regex']) >= 12]
    cand.sort(key=lambda e: (not e['visible_by_default'], -len(e['regex'])))
    sigs, seen = [], set()
    for e in cand:
        if e['regex'] in seen:
            continue
        seen.add(e['regex'])
        sigs.append({'log_file': e['log_file'], 'regex': e['regex'], 'source': e['source'], 'level': e['level'],
                     'visible_by_default': e['visible_by_default'],
                     'confidence': 'high' if len(e['regex']) >= 40 else 'medium'})
        if len(sigs) >= 12:
            break
    T = TEXT[cls]
    fmt = lambda s: s.replace('{logs}', ', '.join(logs) or 'the service log').replace('{svcs}', ', '.join(svcs))
    doc = {
        'id': card,
        'generated': True,
        'title': f"{g['title']}: {CLS[cls]}",
        'status': 'draft', 'author': 'claude', 'reviewed_by': '', 'last_verified': '2026-11-11',
        'mechanism': [mech], 'runs_on': ['office', 'vessel'], 'components': svcs,
        'error_types': [cls.lower()], 'related_docs': RELATED.get(grp, []),
        'coverage': {'failure_points': len(items), 'visible_by_default': sum(e['visible_by_default'] for e in items),
                     'catalogue': 'catalog/failure-points.yaml (filter by card)'},
        'symptoms': [fmt(s) for s in T['symptoms']],
        'phrasings': phrasings(cls, grp, svcs, mech),
        'signatures': sigs,
        'distinguishing_checks': [{'check': fmt(a), 'if_true': fmt(b), 'if_false': fmt(c)} for a, b, c in T['checks']],
        'solutions': [{'id': f'SOL-{card[4:]}-{chr(65+i)}', 'title': t, 'when': w,
                       'steps': [{'do': fmt(d), 'who': who, 'requires_approval': ap, 'verify': v} for d, who, ap, v in steps],
                       'escalate_if': 'The failure repeats after the fix, or the cause is not covered by the checks above.'}
                      for i, (t, w, steps) in enumerate(T['solutions'])],
    }
    if not sigs:
        doc['signatures'] = []
    open(f'{KB}/issues/{card}.yaml', 'w').write(
        f'# Generated by tools/gen_class_cards.py from catalog/failure-points.yaml - edit the generator or write a hand card instead.\n'
        + yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=200))
print(len(by), 'class cards written')
