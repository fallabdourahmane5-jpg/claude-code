# -*- coding: utf-8 -*-
"""Contrôle d'un lot de dossiers : forme, intégrité du texte, attributions."""
import importlib, re, sys
import doss_base, socle

for m in sys.argv[1:]:
    importlib.import_module(m)

D = doss_base.DOSSIERS
pb = doss_base.controler(D)

def champs(x):
    yield x['defi']; yield x['expl']
    for m in x['mec']: yield m['t']; yield m['e']
    for a in x['args']: yield a['a']; yield a['cond']; yield a['lim']
    for c in x['crit']: yield c['t']; yield c.get('qui', ''); yield c['rep']
    for a in x['aut']: yield a['i']; yield a['p']
    for f in x['faits']: yield f['f']; yield f['p']
    for s in x['diss']: yield s['q']; yield s['f']; yield s['r']; yield s['ex']
    if x['comp']:
        for t in x['comp']['lignes']:
            for u in t: yield u

anom = []
for x in D:
    for t in champs(x):
        if '  ' in t or re.search(r'[a-zà-ÿ]{3}[A-ZÀ-Ý]', t):
            anom.append('%s : %r' % (x['cle'], t[:70]))
    for a in x['aut']:
        if not socle.auteur_connu(a['n']):
            anom.append('%s : auteur hors base « %s »' % (x['cle'], a['n']))

print('dossiers : %d | signes : %d' % (len(D), sum(doss_base.signes(x) for x in D)))
print('forme    : %d' % len(pb))
for p in pb[:12]:
    print('   ', p)
print('intégrité: %d' % len(anom))
for a in anom[:12]:
    print('   ', a)
