# -*- coding: utf-8 -*-
"""« Visualisations stratégiques » : mise à jour des thèmes existants par les
chapitres 5 et 6 de deuxième année.

Aucune visualisation n'est créée et la structure graphique reste inchangée :
on ajoute les chapitres dans la liste des sources, une clé de lecture, et des
mécanismes, auteurs ou faits sur des nœuds déjà présents.
"""

import json
import sys

import don2526_visu

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v221_autour.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v221_visu.html'

LIB = {25: '2ᵉ année — ch.5', 26: '2ᵉ année — ch.6'}
TITRE = {25: 'L’équilibre macroéconomique : IS-LM, IS-LM-BP et OG-DG',
         26: 'Taux de change et systèmes de change'}

s = open(SRC, encoding='utf-8').read()

i = s.find('id="v215-visu-engine"')
assert i > 0, 'bloc des visualisations introuvable'
j = s.find('var VZ = ', i)
assert j > 0, 'charge VZ introuvable'
k = s.find('\n', j)
brut = s[j:k][len('var VZ = '):].rstrip()
assert brut.endswith(';')
VZ = json.loads(brut[:-1])
assert json.dumps(VZ, ensure_ascii=False, separators=(',', ':')) == brut[:-1], \
    'la charge ne se réécrit pas à l’identique'

par_cle = {v['cle']: v for v in VZ}
print('visualisations lues : %d' % len(VZ))

bilan = {'visu': 0, 'ch': 0, 'lecture': 0, 'noeuds': 0,
         'mec': 0, 'aut': 0, 'faits': 0, 'dos': 0}


def nz(t):
    return ' '.join(str(t).lower().split())[:90]


for cle, up in don2526_visu.MAJ.items():
    v = par_cle.get(cle)
    assert v is not None, 'visualisation inconnue : ' + cle
    bilan['visu'] += 1

    # --- chapitres sources
    chs = v.setdefault('chapitres', [])
    poids = sum(len(a['mec']) + len(a['aut']) + len(a['faits'])
                for a in up['noeuds'].values()) + len(up['lecture'])
    for N in up['ch']:
        if any(str(c.get('k')) == str(N) for c in chs):
            continue
        chs.append({'k': str(N), 'n': max(1, poids), 'lib': LIB[N]})
        bilan['ch'] += 1
    chs.sort(key=lambda c: -int(c.get('n') or 0))

    # --- clés de lecture
    lect = v.setdefault('lecture', [])
    vus = {nz(x[0]) for x in lect if isinstance(x, list) and x}
    for t, e in up['lecture']:
        if nz(t) in vus:
            continue
        lect.append([t, e])
        vus.add(nz(t))
        bilan['lecture'] += 1

    # --- contenus des nœuds existants
    noeuds = {n['id']: n for n in v['noeuds']}
    for nid, add in up['noeuds'].items():
        n = noeuds.get(nid)
        assert n is not None, 'nœud inconnu : %s / %s' % (cle, nid)
        bilan['noeuds'] += 1
        for champ, cle_texte in (('mec', 't'), ('aut', 'n'), ('faits', 'f')):
            ajouts = add[champ]
            if not ajouts:
                continue
            courant = n.get(champ)
            if not isinstance(courant, list):
                courant = []
                n[champ] = courant
            deja = {nz(it.get(cle_texte, '')) for it in courant
                    if isinstance(it, dict)}
            for it in ajouts:
                if nz(it[cle_texte]) in deja:
                    continue
                courant.append(dict(it))
                deja.add(nz(it[cle_texte]))
                bilan[champ] += 1
        if add['dos']:
            d = n.get('dos')
            if not isinstance(d, list):
                d = []
                n['dos'] = d
            for cd in add['dos']:
                if cd not in d:
                    d.append(cd)
                    bilan['dos'] += 1
        # les liens du nœud mentionnent aussi les chapitres sources
        lk = n.get('lk')
        if isinstance(lk, dict):
            lch = lk.setdefault('ch', [])
            p = len(add['mec']) + len(add['aut']) + len(add['faits'])
            for N in up['ch']:
                if any(str(c.get('k')) == str(N) for c in lch):
                    continue
                lch.append({'k': str(N), 'n': max(1, p), 'lib': LIB[N],
                            'titre': TITRE[N]})
            lch.sort(key=lambda c: -int(c.get('n') or 0))

neuf = 'var VZ = ' + json.dumps(VZ, ensure_ascii=False, separators=(',', ':')) + ';'
s = s[:j] + neuf + s[k:]

open(DST, 'w', encoding='utf-8').write(s)
print('visualisations mises à jour : %d (%d nœuds)' % (bilan['visu'], bilan['noeuds']))
print('  chapitres sources ajoutés : %d · clés de lecture : %d'
      % (bilan['ch'], bilan['lecture']))
print('  mécanismes %d · auteurs %d · faits %d · dossiers liés %d'
      % (bilan['mec'], bilan['aut'], bilan['faits'], bilan['dos']))
print('%s → %s (%.2f Mo)' % (SRC, DST, len(s) / 1048576))
