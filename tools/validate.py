import re,os,glob,yaml,json,sys
# usage: python3 -I validate.py <kb_root> <repo_root>
K=sys.argv[1].rstrip('/'); R=sys.argv[2]
bad=[]
cite=re.compile(r'(Rep[A-Za-z]+/[A-Za-z0-9_./\[\]-]+\.(?:cs|json|sql))(?:#L(\d+)(?:-L(\d+))?)?')
SKIP=('/inventory','/tools','/templates','/reviews','/BRIEF.md','/.claude')
files=[f for f in glob.glob(K+'/**/*',recursive=True) if os.path.isfile(f) and not f[len(K):].startswith(SKIP)]
for f in files:
  t=open(f).read()
  for m in cite.finditer(t):
    p,a,b=m.group(1),m.group(2),m.group(3)
    fp=os.path.join(R,p)
    if not os.path.exists(fp): bad.append(('missing-file',f.replace(K,''),p)); continue
    raw=open(fp,'rb').read()
    txt=raw.decode('utf-16') if raw[:2] in (b'\xff\xfe',b'\xfe\xff') else raw.decode('utf-8','ignore')
    n=txt.count('\n')+1
    for x in (a,b):
      if x and int(x)>n: bad.append(('line-out-of-range',f.replace(K,''),p,x,n))
  for pat in ['AccountKey=','SharedAccessKey=','Password=','sig=','DefaultEndpointsProtocol']:
    if pat in t: bad.append(('secret-pattern',f.replace(K,''),pat))
# templates from code: scan real source lines
def tmpl_ok(rx,src):
  p,_,ln=src.partition('#L'); ln=int(ln.split('-')[0]) if ln else 0
  fp=os.path.join(R,p); lines=open(fp,errors='ignore').read().split('\n')
  # build sample line by replacing {X} with sample values
  hits=[]
  for i,l in enumerate(lines,1):
    s=re.sub(r'\{[^}]+\}','12345',l); s=s.replace('" + ','').replace(' + "','')
    if re.search(rx,s): hits.append(i)
  return hits
for f in sorted(glob.glob(K+'/issues/*.yaml')):
  c=yaml.safe_load(open(f)); n=len(c.get('phrasings',[]))
  if n<20: bad.append(('few-phrasings',c['id'],n))
  for s in c['signatures']:
    hits=tmpl_ok(s['regex'].replace('(?<','(?P<'),s['source'])
    want=int(s['source'].split('#L')[1]) if '#L' in s['source'] else None
    if not hits: bad.append(('regex-no-match',c['id'],s['regex'],s['source']))
    elif want not in hits: bad.append(('regex-line',c['id'],s['regex'][:50],s['source'].split('/')[-1],'actual',hits[:4]))
for b in bad: print(*b)
print('issues:',len(bad))
