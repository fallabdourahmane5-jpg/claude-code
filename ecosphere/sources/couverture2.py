# -*- coding: utf-8 -*-
import json, re, unicodedata, collections
import notions_liste, alias24

C = json.load(open('corpus.json'))
A = json.load(open('corpus_atlas.json'))

def nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'"))

CH = {k: nz(v['texte']) for k, v in C['chapitres'].items()}
NOTIONS = {k: [n['t'] for n in v['notions']] for k, v in C['chapitres'].items()}
ORDRE = ['1','2','3','4','5','6','7','8','9','10','21','22','23','24']

def expressions(lib):
    if lib in alias24.ALIAS:
        return [nz(x) for x in alias24.ALIAS[lib]]
    l = re.sub(r'\s*:\s*', ' | ', lib)
    out = []
    for p in re.split(r'\s+\|\s+|,\s*', l):
        p = p.strip(' .')
        if not p:
            continue
        m = re.match(r'^(.{4,45}?) et (.{4,60})$', p)
        if m:
            out += [m.group(1), m.group(2)]
        else:
            out.append(p)
    fin = []
    for o in out:
        o = re.sub(r"^(les|le|la|l'|des|du|de la|de l')\s+", '', o.strip(' .'), flags=re.I)
        if len(o) >= 5:
            fin.append(nz(o))
    return fin or [nz(lib)]

res = []
for e in notions_liste.ENSEMBLES:
    for d in e['dossiers']:
        ex = expressions(d)
        chaps = []
        for k in ORDRE:
            n = sum(CH[k].count(x) for x in ex)
            if n:
                chaps.append([k, n])
        fiches = [[k, t] for k in ORDRE for t in NOTIONS[k]
                  if any(x in nz(t) for x in ex)]
        idees = [[c['k'], x['n'], x['ti']] for c in A['atlas'] for x in c['e']
                 if any(e2 in nz(x['ti'] + ' ' + ' '.join(x['no'])) for e2 in ex)]
        res.append({'ens': e['num'], 'dossier': d, 'ex': ex, 'chapitres': chaps,
                    'total': sum(n for _, n in chaps),
                    'nfiches': len(fiches), 'fiches': fiches[:10],
                    'nidees': len(idees), 'idees': idees[:10]})

json.dump(res, open('couverture.json', 'w'), ensure_ascii=False)
c = collections.Counter()
for x in res:
    t = x['total']
    c['absent' if t == 0 else 'faible' if t < 5 else 'correct' if t < 25 else 'riche'] += 1
print('dossiers :', len(res))
for k in ['riche', 'correct', 'faible', 'absent']:
    print('%-8s : %3d' % (k, c[k]))
print()
print('--- toujours absents des cours :')
for x in res:
    if x['total'] == 0:
        print('  ens %-2d | %-55s | %s' % (x['ens'], x['dossier'][:55], x['ex'][:3]))
