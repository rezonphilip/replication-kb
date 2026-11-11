# usage: python3 -I extract_sql.py <out.json> <root_dir> [<root_dir> ...]
# Extracts database objects from SQL deployment scripts: tables (+columns), types, sequences,
# procedures (+parameters), functions, objects each procedure reads/writes, error messages,
# and parameter NAMES seeded into CO_Parameters. Never records literal values of parameters.
import os, re, sys, json, glob

def read(p):
    b = open(p, 'rb').read()
    if b[:2] in (b'\xff\xfe', b'\xfe\xff'):
        t = b.decode('utf-16')
    else:
        try:
            t = b.decode('utf-8-sig')
        except UnicodeDecodeError:
            t = b.decode('latin-1')
    return t.replace('\r\n', '\n').replace('\r', '\n')

NAME = r'((?:\[?\w+\]?\.)?\[?\w+\]?)'
def norm(n):
    n = n.replace('[', '').replace(']', '')
    if '.' not in n:
        n = 'REP.' + n if not n.upper().startswith(('#', '@')) else n
    s, o = n.split('.', 1)
    return f'{s.upper()}.{o.upper()}'

R = {
    'table': re.compile(r'\bCREATE\s+TABLE\s+' + NAME + r'\s*\(', re.I),
    'type': re.compile(r'\bCREATE\s+TYPE\s+' + NAME + r'\s+AS\s+TABLE', re.I),
    'sequence': re.compile(r'\bCREATE\s+SEQUENCE\s+' + NAME, re.I),
    'procedure': re.compile(r'\b(?:CREATE|ALTER|CREATE\s+OR\s+ALTER)\s+PROC(?:EDURE)?\s+' + NAME, re.I),
    'function': re.compile(r'\b(?:CREATE|ALTER|CREATE\s+OR\s+ALTER)\s+FUNCTION\s+' + NAME, re.I),
    'view': re.compile(r'\b(?:CREATE|ALTER|CREATE\s+OR\s+ALTER)\s+VIEW\s+' + NAME, re.I),
}
ADDCOL = re.compile(r'ALTER\s+TABLE\s+' + NAME + r'\s+ADD\s+\[?(\w+)\]?\s+\[?(\w+)', re.I)
WRITES = re.compile(r'\b(?:INSERT\s+INTO|UPDATE|DELETE\s+FROM|MERGE\s+INTO|MERGE)\s+' + NAME, re.I)
READS = re.compile(r'\b(?:FROM|JOIN)\s+' + NAME, re.I)
EXEC = re.compile(r'\bEXEC(?:UTE)?\s+' + NAME, re.I)
ERR = re.compile(r"\b(?:RAISERROR|THROW)\s*\(?\s*(?:\d+\s*,\s*)?N?'([^']{4,200})'", re.I)
PARAMNAME = re.compile(r"'((?:REP|PR|IREP|IS)_[A-Z0-9_]{2,})'")
SKIP_READ = {'INSERTED', 'DELETED', 'SYS', 'INFORMATION_SCHEMA'}

def cols_of(text, start):
    # text from the '(' after CREATE TABLE/TYPE name to its matching ')'
    i = text.index('(', start); depth = 0
    for j in range(i, len(text)):
        if text[j] == '(': depth += 1
        elif text[j] == ')':
            depth -= 1
            if depth == 0: break
    body = text[i + 1:j]
    cols = []
    for line in body.split('\n'):
        m = re.match(r'\s*\[?(\w+)\]?\s+\[?(\w+)\]?(\s*\(\s*[\w,\s]+\))?', line)
        if m and m.group(1).upper() not in ('CONSTRAINT', 'PRIMARY', 'UNIQUE', 'INDEX', 'FOREIGN', 'CHECK', 'WITH'):
            cols.append(f"{m.group(1)} {m.group(2)}{(m.group(3) or '').replace(' ', '')}")
    return cols

def params_of(text, start):
    seg = text[start:start + 4000]
    m = re.search(r'\bAS\b\s*(?:\n|BEGIN|SET|DECLARE|--)', seg, re.I)
    head = seg[:m.start()] if m else seg[:1500]
    return sorted(set(re.findall(r'(@\w+)\s+(?:\[?\w+\]?\.)?\[?(\w+)', head)), key=lambda x: head.index(x[0]))

out = {}
roots = sys.argv[2:]
for root in roots:
    for p in sorted(glob.glob(os.path.join(root, '**', '*.sql'), recursive=True)):
        rel = os.path.relpath(p, os.path.dirname(root.rstrip('/')))
        t = read(p)
        lines = t.split('\n')
        def ln(pos): return t.count('\n', 0, pos) + 1
        rec = {'objects': [], 'writes': [], 'reads': [], 'execs': [], 'errors': [], 'param_names': []}
        for kind, rx in R.items():
            for m in rx.finditer(t):
                o = {'kind': kind, 'name': norm(m.group(1)), 'line': ln(m.start())}
                if kind in ('table', 'type'):
                    try: o['columns'] = cols_of(t, m.end() - 1)
                    except ValueError: o['columns'] = []
                if kind in ('procedure', 'function'):
                    o['params'] = [f'{a} {b}' for a, b in params_of(t, m.end())]
                rec['objects'].append(o)
        for m in ADDCOL.finditer(t):
            rec['objects'].append({'kind': 'add_column', 'name': norm(m.group(1)), 'column': f'{m.group(2)} {m.group(3)}', 'line': ln(m.start())})
        body_start = 0
        for k, rx in (('writes', WRITES), ('reads', READS), ('execs', EXEC)):
            seen = set()
            for m in rx.finditer(t):
                n = norm(m.group(1))
                if n.split('.')[0] in SKIP_READ or n.split('.')[1].startswith('@') or n.split('.')[1] in ('SET', 'WHERE', 'SELECT'): continue
                if n not in seen:
                    seen.add(n); rec[k].append([n, ln(m.start())])
        for m in ERR.finditer(t):
            rec['errors'].append([m.group(1), ln(m.start())])
        if re.search(r'CO_PARAMETERS', t, re.I) and re.search(r'\bINSERT\b|\bUPDATE\b|\bMERGE\b', t, re.I):
            rec['param_names'] = sorted(set(PARAMNAME.findall(t)))
        out[rel] = rec
json.dump(out, open(sys.argv[1], 'w'), indent=1)
print(len(out), 'files')
