import re,os,glob,yaml,json,sys
# usage: python3 -I validate.py <kb_root> <repo_root>
K=sys.argv[1].rstrip('/'); R=sys.argv[2]
bad=[]
cite=re.compile(r'((?:Rep[A-Za-z]+|ComINT|ComPBR|ExportCDT|ExportDCS|ImportDES|ImportDSC|ImportRBP|iRepScript|IntialDeployment)/[A-Za-z0-9_./\[\],-]+\.(?:cs|json|sql|txt))(?:#L(\d+)(?:-L(\d+))?)?')
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
    s=re.sub(r'\{[^}]+\}','12345',l); s=re.sub(r'"\s*\+\s*"','',s); s=s.replace('" + ','').replace(' + "','')
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

# failure-point catalogue: every failure point must point to an existing card
cat=os.path.join(K,'catalog','failure-points.yaml')
if os.path.exists(cat):
  fps=yaml.safe_load(open(cat))['failure_points']
  ids={yaml.safe_load(open(f))['id'] for f in glob.glob(K+'/issues/*.yaml')}
  for e in fps:
    if e['card'] not in ids: bad.append(('fp-card-missing',e['id'],e['card']))
    if e['regex']:
      try: re.compile(e['regex'])
      except re.error: bad.append(('fp-bad-regex',e['id']))
  print('failure points:',len(fps),'cards referenced:',len({e['card'] for e in fps}))

# related_docs on cards must resolve to an article doc_id
docids=set()
for f in glob.glob(K+'/articles/**/*.md',recursive=True)+glob.glob(K+'/inventory/*.md'):
  m=re.search(r'^doc_id:\s*(\S+)',open(f,errors='ignore').read(),re.M)
  if m: docids.add(m.group(1))
docids|={yaml.safe_load(open(f))['id'] for f in glob.glob(K+'/issues/*.yaml')}
for f in sorted(glob.glob(K+'/issues/*.yaml')):
  c=yaml.safe_load(open(f))
  for d in c.get('related_docs',[]) or []:
    if d not in docids: bad.append(('related-doc-missing',c['id'],d))
for b in bad: print(*b)
print('issues:',len(bad))
