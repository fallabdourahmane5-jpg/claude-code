# -*- coding: utf-8 -*-
"""Section « Recherche » : remplacement de la charge indexée par celle qui
couvre les seize chapitres, chapitres 5 et 6 de deuxième année compris.

La charge est portée par `var D = {...};` au sein du bloc
<script id="eco-recherche-v218">. On contrôle que l'ancienne charge se relit,
puis on écrit la nouvelle au même format.
"""

import json
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v221_res.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v221_rech.html'
CHARGE = sys.argv[3] if len(sys.argv) > 3 else 'recherche_payload.json'

s = open(SRC, encoding='utf-8').read()

i = s.find('id="eco-recherche-v218"')
assert i > 0, 'bloc « Recherche » introuvable'
j = s.find('var D = ', i)
assert j > 0, 'charge D introuvable'
k = s.find('\n', j)
brut = s[j:k][len('var D = '):].rstrip()
assert brut.endswith(';')
ancien = json.loads(brut[:-1])
assert json.dumps(ancien, ensure_ascii=False, separators=(',', ':')) == brut[:-1], \
    'la charge ne se réécrit pas à l’identique'


def bilan(d):
    return {'v': d['v'], 'ch': len(d['ch']), 'def': len(d['def']),
            'sec': len(d['sec']), 'fml': len(d['fml']), 'fai': len(d['fai']),
            'dos': len(d['dos']), 'atl': len(d['atl']), 'chf': len(d['chf']),
            'res': len(d['res']), 'syn': len(d['syn'])}


neuf_d = json.load(open(CHARGE, encoding='utf-8'))
assert set(neuf_d) == set(ancien), set(neuf_d) ^ set(ancien)
av, ap = bilan(ancien), bilan(neuf_d)
print('ancienne charge :', av)
print('nouvelle charge :', ap)
for c in ('ch', 'def', 'sec', 'fml', 'fai', 'atl', 'chf', 'res'):
    assert ap[c] >= av[c], ('rubrique appauvrie', c, av[c], ap[c])
assert ap['ch'] == 16, ap['ch']
for c in ('25', '26'):
    assert c in neuf_d['ch'], c
    assert neuf_d['ch'][c]['a'] == 2, c

# aucun renvoi ne doit pointer sur un bloc inexistant
for c, v in neuf_d['def'].items():
    for ou in v['ou']:
        assert ou[0] in neuf_d['ch'], (c, ou)
        assert 0 <= ou[1] < neuf_d['ch'][ou[0]]['n'], ('renvoi hors bornes', c, ou)
for nom in ('sec', 'fml', 'fai'):
    for x in neuf_d[nom]:
        assert x['c'] in neuf_d['ch'], (nom, x)
        assert 0 <= x['b'] < neuf_d['ch'][x['c']]['n'], ('renvoi hors bornes', nom, x)

neuf = 'var D = ' + json.dumps(neuf_d, ensure_ascii=False,
                               separators=(',', ':')) + ';'
s = s[:j] + neuf + s[k:]
open(DST, 'w', encoding='utf-8').write(s)

n25 = sum(1 for v in neuf_d['def'].values() if any(o[0] == '25' for o in v['ou']))
n26 = sum(1 for v in neuf_d['def'].values() if any(o[0] == '26' for o in v['ou']))
print('définitions renvoyant au chapitre 5 : %d · au chapitre 6 : %d' % (n25, n26))
for nom, lib in (('sec', 'sections'), ('fml', 'formules'), ('fai', 'faits')):
    a = sum(1 for x in neuf_d[nom] if x['c'] == '25')
    b = sum(1 for x in neuf_d[nom] if x['c'] == '26')
    print('%-9s : %d au chapitre 5, %d au chapitre 6' % (lib, a, b))
print('%s → %s (%.2f Mo)' % (SRC, DST, len(s) / 1048576))
