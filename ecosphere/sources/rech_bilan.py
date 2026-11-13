# -*- coding: utf-8 -*-
"""Bilan chapitre par chapitre de ce que la nouvelle recherche atteint."""
import json
from collections import Counter

import rech_base as R

D = json.load(open('recherche_payload.json'))
B = R.blocs()
C = R.corpus()
I = json.load(open('inventaire.json'))

print('%-17s %7s %7s %7s %7s %7s %7s %7s %7s %7s'
      % ('chapitre', 'signes', 'blocs', 'sectio', 'défini', 'notion',
         'formul', 'chiffr', 'faits', 'idées'))
tot = Counter()
sec = Counter(x['c'] for x in D['sec'])
fml = Counter(x['c'] for x in D['fml'])
fai = Counter(x['c'] for x in D['fai'])
chf = Counter(x['c'] for x in D['chf'])
atl = Counter(x['c'] for x in D['atl'])
dfc = Counter()
for v in D['def'].values():
    for k, _ in v['ou']:
        dfc[k] += 1
for k in R.ORDRE:
    n = {'signes': I[k]['signes'], 'blocs': len(B[k]), 'sec': sec[k],
         'def': dfc[k], 'not': len(C['chapitres'][k]['notions']),
         'fml': fml[k], 'chf': chf[k], 'fai': fai[k], 'atl': atl[k]}
    for a, b in n.items():
        tot[a] += b
    print('%-17s %7d %7d %7d %7d %7d %7d %7d %7d %7d'
          % (R.lib(k), n['signes'], n['blocs'], n['sec'], n['def'], n['not'],
             n['fml'], n['chf'], n['fai'], n['atl']))
print('%-17s %7d %7d %7d %7d %7d %7d %7d %7d %7d'
      % ('TOTAL', tot['signes'], tot['blocs'], tot['sec'], tot['def'],
         tot['not'], tot['fml'], tot['chf'], tot['fai'], tot['atl']))
print()
print('définitions embarquées : %d' % len(D['def']))
print('  issues des cours     : %d'
      % sum(1 for v in D['def'].values() if 'redigee' not in v['o']))
print('  rédigées             : %d'
      % sum(1 for v in D['def'].values() if 'redigee' in v['o']))
print('dossiers               : %d' % len(D['dos']))
print('sigles reliés          : %d' % len(D['syn']))
