# -*- coding: utf-8 -*-
"""Monte la charge des « Visualisations stratégiques ».

Pour chaque nœud, les liens vers les contenus de l'application (chapitres,
fiches, idées de l'Atlas, sujets, auteurs) ne sont pas écrits à la main :
ils sont calculés par liens.py à partir des expressions déclarées dans
`termes`, donc à partir de contenus réellement présents. Les clés de
dossiers « Autour d'une notion » et les noms d'auteurs sont vérifiés.
"""
import glob
import importlib
import json
import sys

import liens
import socle
import vz_base

for f in sorted(glob.glob('vz_[0-9][0-9]*.py')):
    importlib.import_module(f[:-3])

VISUS = vz_base.VISUS

# ----------------------------------------------------------- bases de contrôle
D = json.load(open('autour_payload.json', encoding='utf-8'))
CLES_DOS = {x['cle']: x for x in D['dossiers'] if x['etat'] == 'redige'}
TITRE_DOS = {k: v['titre'] for k, v in CLES_DOS.items()}
ENS_DOS = {k: v['ens'] for k, v in CLES_DOS.items()}

# quelques attributions sont écrites comme le cours les écrit, alors que la
# base auteurs de l'application porte une autre graphie ; on les autorise
# explicitement en gardant la trace de la citation qui les justifie.
EXCEPTIONS_AUTEURS = {
    "D. Plihon": "ch1 : « D. Plihon parle de Polycrise dans son livre "
                 "(les capitalismes contemporains) »",
}


def auteur_ok(nom):
    return bool(nom) and (socle.auteur_connu(nom) or nom in EXCEPTIONS_AUTEURS)


pb = vz_base.controler(VISUS, set(CLES_DOS), auteur_ok)
if pb:
    print('PROBLÈMES (%d) :' % len(pb))
    for p in pb[:60]:
        print('   ', p)
    sys.exit(1)

# --------------------------------------------------------------- liens réels
LIBCH = {'21': '2ᵉ année — ch.1', '22': '2ᵉ année — ch.2',
         '23': '2ᵉ année — ch.3', '24': '2ᵉ année — ch.4'}


def libch(k):
    return LIBCH.get(str(k), 'Chapitre ' + str(k))


tot = {'ch': 0, 'fi': 0, 'at': 0, 'su': 0, 'au': 0, 'dos': 0}
charge = []
for x in VISUS:
    chs_visu = {}
    noeuds = []
    for n in x['noeuds']:
        L = liens.liens_de(None, ex=[liens.nz(t) for t in n['termes']])
        ch = [{'k': c['k'], 'n': c['n'], 'lib': libch(c['k']), 'titre': c['titre']}
              for c in L['ch']][:6]
        for c in ch:
            chs_visu[c['k']] = chs_visu.get(c['k'], 0) + c['n']
        dos = [{'cle': d, 't': TITRE_DOS[d], 'ens': ENS_DOS[d]} for d in n['dos']]
        tot['ch'] += len(ch)
        tot['fi'] += len(L['fi'][:8])
        tot['at'] += len(L['at'][:8])
        tot['su'] += len(L['su'][:6])
        tot['au'] += len(L['au'][:10])
        tot['dos'] += len(dos)
        m = dict(n)
        m.pop('termes', None)
        m['lk'] = {'ch': ch, 'fi': L['fi'][:8], 'at': L['at'][:8],
                   'su': L['su'][:6], 'au': L['au'][:10], 'dos': dos}
        noeuds.append(m)
    ordre = sorted(chs_visu.items(), key=lambda t: -t[1])
    y = dict(x)
    y['noeuds'] = noeuds
    y['chapitres'] = [{'k': k, 'n': v, 'lib': libch(k)} for k, v in ordre[:6]]
    charge.append(y)

json.dump(charge, open('visu_payload.json', 'w', encoding='utf-8'),
          ensure_ascii=False, separators=(',', ':'))

sg = sum(vz_base.signes(x) for x in VISUS)
nn = sum(len(x['noeuds']) for x in VISUS)
nl = sum(len(x['liens']) for x in VISUS)
print('visualisations  : %d' % len(VISUS))
print('nœuds           : %d' % nn)
print('liens expliqués : %d' % nl)
print('signes rédigés  : %d' % sg)
print('liens calculés  : chapitres %d · fiches %d · Atlas %d · sujets %d · '
      'auteurs %d · dossiers %d'
      % (tot['ch'], tot['fi'], tot['at'], tot['su'], tot['au'], tot['dos']))
print('charge          : %.2f Mo'
      % (len(json.dumps(charge, ensure_ascii=False)) / 1048576))
for x in charge:
    print('   %-14s %-44s %-9s %2d nœuds %2d liens  ch: %s'
          % (x['type'], x['titre'][:44], '', len(x['noeuds']), len(x['liens']),
             ','.join(c['k'] for c in x['chapitres'])))
