# -*- coding: utf-8 -*-
"""Affiche un ou plusieurs dossiers « Autour d'une notion » pour s'en servir
comme matière de départ (contenus déjà vérifiés sur les cours)."""
import json, sys
D = json.load(open('autour_payload.json', encoding='utf-8'))
X = {d['cle']: d for d in D['dossiers']}
if len(sys.argv) > 1 and sys.argv[1] == '-l':
    q = [a.lower() for a in sys.argv[2:]]
    for d in D['dossiers']:
        b = (d['cle'] + ' ' + d['titre']).lower()
        if all(w in b for w in q):
            print('%-34s ens%-3s %s' % (d['cle'], d['ens'], d['titre']))
    sys.exit()
for c in sys.argv[1:]:
    d = X.get(c)
    if not d:
        print('?? ' + c); continue
    print('=' * 78); print(d['cle'], '·', d['titre'], '· ens', d['ens'])
    print('DEFI:', d['defi'])
    print('EXPL:', d['expl'])
    for m in d.get('mec') or []:
        print('  MEC', m.get('t'), '::', m.get('e'))
    for a in d.get('args') or []:
        print('  ARG', a.get('a'), '|| LIM', a.get('lim'))
    for a in d.get('crit') or []:
        print('  CRIT', a.get('t'), '::', a.get('rep'))
    for a in d.get('aut') or []:
        print('  AUT', a.get('n'), '::', a.get('i'))
    for a in d.get('faits') or []:
        print('  FAIT', a.get('f'), '::', a.get('p'))
    for a in d.get('comp') or []:
        print('  COMP', a)
