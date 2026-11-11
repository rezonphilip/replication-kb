# usage: python3 -I gen_failure_points.py <kb_root> <src_root> <extract.json> [<extract.json> ...]
# Builds the exhaustive failure-point catalogue:
#   catalog/failure-points.yaml  - one entry per Error/Critical/Warning log template and thrown exception,
#                                  with a matching regex, level, default visibility, class and issue card.
#   inventory/failure-points.md  - coverage tables (card x count, service x class) for review.
# Assignment order: hand-written issue card whose signature matches the source line > benign rule > class rule.
import json, re, sys, os, glob, collections, yaml

KB, SRC = sys.argv[1].rstrip('/'), sys.argv[2]
EXTRACTS = sys.argv[3:]
R = yaml.safe_load(open(f'{KB}/tools/failure_rules.yaml'))
SVC2GRP = {s: g for g, v in R['groups'].items() for s in v['services']}
BENIGN = [re.compile(x, re.I) for x in R['benign']]
CLASSES = [(c['id'], re.compile(c['rx'], re.I)) for c in R['classes']]

def src_line(src):
    p, _, ln = src.partition('#L')
    try:
        lines = open(os.path.join(SRC, p), encoding='utf-8-sig', errors='ignore').read().split('\n')
        return lines[int(ln) - 1]
    except Exception:
        return ''

def sample(line):
    s = re.sub(r'\{[^}]+\}', '12345', line)
    return s.replace('" + ', '').replace(' + "', '')

def tmpl_regex(t):
    if t.startswith('<') and t.endswith('>'):
        return None
    parts = [p for p in re.split(r'\{[^}]*\}', t)]
    lits = [re.escape(p.strip()) for p in parts if len(p.strip()) >= 3]
    if not lits:
        return None
    return '.*?'.join(lits)

# hand-written cards (specific signatures win)
hand = []
for f in sorted(glob.glob(f'{KB}/issues/*.yaml')):
    c = yaml.safe_load(open(f))
    if c.get('generated'):
        continue
    for s in c.get('signatures', []):
        try:
            hand.append((c['id'], re.compile(s['regex'].replace('(?<', '(?P<'))))
        except re.error:
            pass

entries = []
for ex in EXTRACTS:
    d = json.load(open(ex))
    for svc, v in d.items():
        if svc not in SVC2GRP:
            continue
        grp = SVC2GRP[svc]
        seen = set()
        for lv, t, src, cls, meth in v.get('logl', []):
            if not (lv in ('Error', 'Critical', 'Warning', 'Fatal') or lv.startswith('Throw')):
                continue
            key = (lv, t, src)
            if key in seen:
                continue
            seen.add(key)
            norm = re.sub(r'\s+', ' ', re.sub(r'\{[^}]*\}', '{X}', t)).strip()
            line = src_line(src)
            card = None
            for cid, rx in hand:
                if rx.search(sample(line)) or rx.search(norm):
                    card = cid; break
            klass = None
            if not card and any(b.search(norm) for b in BENIGN):
                card, klass = 'ISS-PLATFORM-BENIGN', 'BENIGN'
            if not card:
                cnorm = norm
                if R['groups'][grp]['mechanism'] == 'irep':
                    # in sync+ code "Azure DB"/"in Azure" means the REP2X/REP2I staging SQL database, not transport
                    cnorm = re.sub(r'(?i)azure ?db|tables? ?in ?azure|in azure|azure', 'staging DB execution', norm)
                for cid, rx in CLASSES:
                    if rx.search(cnorm):
                        klass = cid; break
                if klass == 'GENERIC':
                    # generic text ("Error in {MethodName}"): classify by where it is raised
                    where = f'{cls} {meth} ' + re.sub(r'\{[^}]*\}', ' ', line)
                    where = re.sub(r'([a-z])([A-Z])', r'\1 \2', where)
                    if R['groups'][grp]['mechanism'] == 'irep':
                        where = re.sub(r'(?i)azure ?db|in azure|azure', 'staging DB execution', where)
                    for cid, rx in CLASSES[:-1]:
                        if rx.search(where):
                            klass = cid; break
                card = f'ISS-{grp}-{klass}'
            rx = tmpl_regex(t)
            check = 'ok'
            if rx:
                try:
                    if not re.search(rx, sample(line)):
                        check = 'multi-line'
                except re.error:
                    rx, check = None, 'bad-regex'
            level = 'Throw' if lv.startswith('Throw') else lv
            entries.append({
                'service': svc, 'group': grp, 'mechanism': R['groups'][grp]['mechanism'],
                'level': level, 'exception': lv.split(':', 1)[1] if lv.startswith('Throw') else None,
                'visible_by_default': level in ('Error', 'Critical', 'Fatal'),
                'template': t, 'regex': rx, 'source': src, 'source_check': check,
                'class': klass or 'HAND', 'card': card, 'benign': card == 'ISS-PLATFORM-BENIGN',
                'log_file': R['log_files'].get(svc), 'code_location': f'{cls}.{meth}'.strip('.'),
            })

# stable ids
cnt = collections.Counter()
for e in entries:
    cnt[e['service']] += 1
    e['id'] = f"FP-{e['service'].upper()}-{cnt[e['service']]:04d}"

os.makedirs(f'{KB}/catalog', exist_ok=True)
hdr = ('# Generated by tools/gen_failure_points.py - do not edit by hand.\n'
       '# Every Error/Critical/Warning logger template and thrown exception in the MS-REP and iRep code, mapped to an issue card.\n'
       '# Used by the dashboard identifier: match a log line against `regex` (case-sensitive, .NET/Python compatible),\n'
       '# then open `card`. `visible_by_default: false` lines only appear when the service log level is lowered below Error.\n')
open(f'{KB}/catalog/failure-points.yaml', 'w').write(hdr + yaml.safe_dump({'failure_points': entries}, sort_keys=False, allow_unicode=True, width=200))

# markdown coverage
by_card = collections.Counter(e['card'] for e in entries)
mat = collections.defaultdict(collections.Counter)
for e in entries:
    mat[e['service']][e['class']] += 1
cols = ['HAND', 'BENIGN'] + [c for c, _ in CLASSES]
L = ['---\ndoc_id: INV-FAILURE-POINTS\ntype: inventory\nmechanism: [priority-replication, smartsync, irep]\ncomponents: [ms-rep, irep]\nstatus: draft\nauthor: claude\nlast_verified: 2026-11-11\n---\n\n',
     '# Failure-point coverage\n\n',
     f'Every Error, Critical and Warning log template and every thrown exception in the code ({len(entries)} failure points) is mapped to an issue card. The machine-readable list is `catalog/failure-points.yaml`. Keywords: failure point, coverage, error catalogue, log level.\n\n',
     '## Visibility\n\nWhich failure points reach the log file with the shipped log level (Serilog minimum level Error). Keywords: log level, hidden warnings.\n\n',
     '| Level | Failure points | Visible by default |\n|---|---|---|\n']
lvl = collections.Counter(e['level'] for e in entries)
for k in sorted(lvl):
    L.append(f"| {k} | {lvl[k]} | {'yes' if k in ('Error','Critical','Fatal') else ('only if caught and logged' if k=='Throw' else 'no')} |\n")
L.append('\n## Cards\n\nNumber of failure points each card covers. Keywords: issue card, coverage.\n\n| Card | Failure points |\n|---|---|\n')
for c, n in sorted(by_card.items()):
    L.append(f'| {c} | {n} |\n')
L.append('\n## Service by class\n\nHow the failure points of each service split across failure classes (HAND = matched a hand-written card). Keywords: service, failure class.\n\n')
L.append('| Service | ' + ' | '.join(cols) + ' |\n|' + '---|' * (len(cols) + 1) + '\n')
for s in sorted(mat):
    L.append(f'| {s} | ' + ' | '.join(str(mat[s].get(c, '')) for c in cols) + ' |\n')
bad = [e for e in entries if e['source_check'] != 'ok']
L.append(f'\n## Regex check\n\n{len(entries)-len(bad)} regexes match their source line; {len(bad)} are multi-line calls or have no literal text (they match by exception text or code location only). Keywords: regex, signature check.\n')
open(f'{KB}/inventory/failure-points.md', 'w').write(''.join(L))
print(len(entries), 'failure points;', len(by_card), 'cards;', len(bad), 'without direct regex match')
print(sorted(by_card.items(), key=lambda x: -x[1])[:60])
