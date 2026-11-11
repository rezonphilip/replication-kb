import os,re,json,glob,collections,sys
# usage: python3 -I extract.py <repo_root> <out.json>
ROOT=sys.argv[1]
def lines(p):
    try: return open(p,encoding='utf-8-sig',errors='replace').read().split('\n')
    except: return []
pat={
 'route':re.compile(r'\[(Route|Http(Get|Post|Put|Delete))\s*\(\s*"([^"]*)"'),
 'class':re.compile(r'\bclass\s+(\w+)'),
 'hosted':re.compile(r'AddHostedService<(\w+)>|:\s*BackgroundService|Task\.Delay\(([^)]*)\)|PeriodicTimer|Timer\('),
 'sp':re.compile(r'"((?:\[?(?:REP|Rep|rep|dbo|Common|PR|iRep|IREP)\]?\.)\[?[A-Za-z_0-9]+\]?)"|"((?:PR|REP|rep|Rep|USP|usp|SP|sp)_[A-Za-z0-9_]{3,})"'),
 'param':re.compile(r'"(REP_[A-Z0-9_]{3,}|IREP_[A-Z0-9_]{3,}|PR_[A-Z0-9_]{3,})"'),
 'cfg':re.compile(r'(?:Configuration|_configuration|config)\s*(?:\[|\.GetSection\(|\.GetValue<[^>]+>\()\s*"([^"]+)"'),
 'apiurl':re.compile(r'"((?:api/)?[A-Za-z]+/[A-Za-z0-9_/]+)"'),
 'svcname':re.compile(r'"(\w+Service)"'),
 'log':re.compile(r'(?:Log(?:Error|Warning|Critical|Information)|throw new \w*Exception)\s*\(\s*(?:\w+\s*,\s*)?\$?"([^"]{8,160})'),
 'enum':re.compile(r'\benum\s+(\w+)'),
}
out={}
for svc in sorted(os.listdir(ROOT)):
    d=collections.defaultdict(list)
    for p in glob.glob(f'{ROOT}/{svc}/**/*.cs',recursive=True):
        rel=os.path.relpath(p,ROOT)
        for i,l in enumerate(lines(p),1):
            for k,r in pat.items():
                for m in r.finditer(l):
                    g=[x for x in m.groups() if x]
                    v=g[-1] if g else m.group(0)
                    d[k].append((v,f'{rel}#L{i}'))
    out[svc]=d
json.dump(out,open(sys.argv[2],'w'))
for svc,d in out.items():
    print(f'\n######## {svc}')
    for k in ['hosted','route','svcname','apiurl','sp','param','cfg']:
        c=collections.OrderedDict()
        for v,loc in d.get(k,[]): c.setdefault(v,loc)
        if c: print(f' {k}({len(c)}):', '; '.join(f'{v}' for v in list(c)[:40]))
