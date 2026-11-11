import os, re, json, glob, collections, sys
# usage: python3 -I extract.py <repo_root> <out.json> [service ...]
# Scans every service folder under <repo_root> (or only the named ones) and records, with file#line:
# routes, hosted services/timers, stored procedures, parameter keys, config sections, service URLs,
# logger message templates (with level, multi-line calls and interpolated strings) and thrown exceptions.
# Never records configuration values.
ROOT = sys.argv[1]
ONLY = set(sys.argv[3:])

def lines(p):
    try:
        return open(p, encoding='utf-8-sig', errors='replace').read().split('\n')
    except Exception:
        return []

pat = {
    'route': re.compile(r'\[(Route|Http(Get|Post|Put|Delete))\s*\(\s*"([^"]*)"'),
    'class': re.compile(r'\bclass\s+(\w+)'),
    'hosted': re.compile(r'AddHostedService<(\w+)>|:\s*BackgroundService|Task\.Delay\(([^)]*)\)|PeriodicTimer|Timer\('),
    'sp': re.compile(r'"((?:\[?(?:REP|Rep|rep|dbo|Common|COMMON|PR|iRep|IREP)\]?\.)\[?[A-Za-z_0-9]+\]?)"|"((?:PR|REP|rep|Rep|USP|usp|SP|sp|R2)_[A-Za-z0-9_]{3,})"'),
    'param': re.compile(r'"(REP_[A-Z0-9_]{3,}|IREP_[A-Z0-9_]{3,}|PR_[A-Z0-9_]{3,})"'),
    'cfg': re.compile(r'(?:Configuration|_configuration|config|configuration)\s*(?:\[|\.GetSection\(|\.GetValue<[^>]+>\()\s*"([^"]+)"'),
    'apiurl': re.compile(r'"((?:api/)?[A-Za-z]+/[A-Za-z0-9_/\-]+)"'),
    'svcname': re.compile(r'"(\w+Service)"'),
    'enum': re.compile(r'\benum\s+(\w+)'),
}
LOGSTART = re.compile(r'(?:_logger|logger|_log|Logger)\s*\.\s*Log(Error|Warning|Critical|Information|Debug|Trace)\s*\(|'
                      r'\bLog\s*\.\s*(Error|Warning|Fatal|Information|Debug|Verbose)\s*\(|'
                      r'throw\s+new\s+(\w*Exception)\s*\(')

def first_string(s):
    """First C# string literal in s (handles $"...{x ? "a" : "b"}..."), joining simple '+' concatenations."""
    parts = []
    i = 0
    n = len(s)
    for _ in range(6):
        j = s.find('"', i)
        if j < 0:
            break
        interp = (j > 0 and s[j - 1] == '$') or (j > 1 and s[j - 2:j] in ('$@', '@$'))
        k = j + 1
        depth = 0
        buf = []
        while k < n:
            c = s[k]
            if interp and c == '{':
                if k + 1 < n and s[k + 1] == '{':
                    buf.append('{'); k += 2; continue
                depth += 1
            elif interp and c == '}' and depth:
                depth -= 1
            elif c == '\\' and k + 1 < n:
                buf.append(s[k:k + 2]); k += 2; continue
            elif c == '"' and depth == 0:
                break
            buf.append(c); k += 1
        parts.append(''.join(buf))
        rest = s[k + 1:]
        m = re.match(r'\s*\+\s*(\$?")', rest)
        if m:
            i = k + 1 + m.start(1) + (1 if m.group(1) == '$"' else 0)
            continue
        m = re.match(r'\s*\+\s*([A-Za-z_][\w\.]*(?:\(\))?)(\s*\+\s*(\$?"))?', rest)
        if m:
            parts.append('{' + m.group(1) + '}')
            if m.group(3):
                i = k + 1 + m.start(3) + (1 if m.group(3) == '$"' else 0)
                continue
        break
    return ''.join(parts) if parts else None

out = {}
for svc in sorted(os.listdir(ROOT)):
    if ONLY and svc not in ONLY:
        continue
    if not os.path.isdir(os.path.join(ROOT, svc)):
        continue
    d = collections.defaultdict(list)
    for p in sorted(glob.glob(f'{ROOT}/{svc}/**/*.cs', recursive=True)):
        if '.Tests' in p:
            continue
        rel = os.path.relpath(p, ROOT)
        L = lines(p)
        cls = ''
        meth = ''
        for i, l in enumerate(L, 1):
            st = l.strip()
            mc = re.search(r'\bclass\s+(\w+)', l)
            if mc:
                cls = mc.group(1)
            mm = re.match(r'\s*(?:public|private|protected|internal)[\w\s<>\[\],\.\?]*\s(\w+)\s*\(', l)
            if mm and not st.endswith(';'):
                meth = mm.group(1)
            if st.startswith('//'):
                continue
            for k, r in pat.items():
                for m in r.finditer(l):
                    g = [x for x in m.groups() if x]
                    v = g[-1] if g else m.group(0)
                    d[k].append((v, f'{rel}#L{i}'))
            for m in LOGSTART.finditer(l):
                level = m.group(1) or m.group(2) or ('Throw:' + m.group(3))
                chunk = l[m.end():]
                j = i
                while chunk.count('(') + 1 > chunk.count(')') and j < len(L) and j < i + 8:
                    chunk += ' ' + L[j].strip(); j += 1
                tmpl = first_string(chunk)
                if not tmpl:
                    tmpl = '<' + re.sub(r'\s+', ' ', chunk.split(';')[0])[:80] + '>'
                d['log'].append((tmpl, f'{rel}#L{i}'))
                d['logl'].append((level, tmpl, f'{rel}#L{i}', cls, meth))
    out[svc] = d
json.dump(out, open(sys.argv[2], 'w'))
for svc, d in out.items():
    print(f'\n######## {svc}  logs={len(d.get("logl", []))}')
    for k in ['hosted', 'route', 'svcname', 'apiurl', 'sp', 'param', 'cfg']:
        c = collections.OrderedDict()
        for v, loc in d.get(k, []):
            c.setdefault(v, loc)
        if c:
            print(f' {k}({len(c)}):', '; '.join(f'{v}' for v in list(c)[:40]))
