# -*- coding: utf-8 -*-
"""« Autour d'une notion » : mise à jour des dossiers par les chapitres 5 et 6
de deuxième année.

Aucun dossier n'est créé. Pour chaque dossier concerné on ajoute le ou les
chapitres dans ses liens, puis les mécanismes, auteurs, arguments, faits et
pistes de dissertation que le document de cours justifie.
"""

import json
import sys

import don2526_dossiers

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v221_atlas.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v221_autour.html'

LIB = {25: '2ᵉ année — ch.5', 26: '2ᵉ année — ch.6'}
TITRE = {25: 'L’équilibre macroéconomique : IS-LM, IS-LM-BP et OG-DG',
         26: 'Taux de change et systèmes de change'}

s = open(SRC, encoding='utf-8').read()

i = s.find('id="eco-autour-notion"')
assert i > 0, 'bloc « Autour d’une notion » introuvable'
j = s.find('var D = ', i)
assert j > 0, 'charge D introuvable'
k = s.find('\n', j)
brut = s[j:k][len('var D = '):].rstrip()
assert brut.endswith(';')
D = json.loads(brut[:-1])
assert json.dumps(D, ensure_ascii=False, separators=(',', ':')) == brut[:-1], \
    'la charge ne se réécrit pas à l’identique'

dos = {x['cle']: x for x in D['dossiers']}
print('dossiers lus : %d (%d ensembles)' % (len(dos), len(D['ensembles'])))

bilan = {'dossiers': 0, 'ch': 0, 'mec': 0, 'aut': 0, 'args': 0,
         'faits': 0, 'diss': 0}


def nz(t):
    return ' '.join(str(t).lower().split())[:90]


for cle, up in don2526_dossiers.MAJ.items():
    x = dos.get(cle)
    assert x is not None, 'dossier inconnu : ' + cle
    bilan['dossiers'] += 1

    # --- liens vers les chapitres
    liens = x.setdefault('liens', {})
    chs = liens.setdefault('ch', [])
    for N in up['ch']:
        if any(str(c.get('k')) == str(N) for c in chs):
            continue
        # le compteur reprend le nombre d'éléments réellement ajoutés
        n = (len(up['mec']) + len(up['aut']) + len(up['args'])
             + len(up['faits']) + len(up['diss']))
        chs.append({'k': str(N), 'n': max(1, n), 'lib': LIB[N],
                    'titre': TITRE[N]})
        bilan['ch'] += 1

    # --- contenus, sans jamais dupliquer un item déjà présent
    for champ, cle_texte in (('mec', 't'), ('aut', 'n'), ('args', 'a'),
                             ('faits', 'f'), ('diss', 'q')):
        ajouts = up[champ]
        if not ajouts:
            continue
        courant = x.get(champ)
        if not isinstance(courant, list):
            courant = []
            x[champ] = courant
        vus = {nz(it.get(cle_texte, '')) for it in courant if isinstance(it, dict)}
        for it in ajouts:
            if nz(it[cle_texte]) in vus:
                continue
            courant.append(dict(it))
            vus.add(nz(it[cle_texte]))
            bilan[champ] += 1

# les chapitres sont classés par poids décroissant, comme dans le reste du bloc
for x in D['dossiers']:
    ch = (x.get('liens') or {}).get('ch')
    if isinstance(ch, list):
        ch.sort(key=lambda c: -int(c.get('n') or 0))

neuf = 'var D = ' + json.dumps(D, ensure_ascii=False, separators=(',', ':')) + ';'
s = s[:j] + neuf + s[k:]

open(DST, 'w', encoding='utf-8').write(s)
print('dossiers mis à jour : %d' % bilan['dossiers'])
print('  liens de chapitre ajoutés : %d' % bilan['ch'])
print('  mécanismes %d · auteurs %d · arguments %d · faits %d · pistes %d'
      % (bilan['mec'], bilan['aut'], bilan['args'], bilan['faits'], bilan['diss']))
print('%s → %s (%.2f Mo)' % (SRC, DST, len(s) / 1048576))
