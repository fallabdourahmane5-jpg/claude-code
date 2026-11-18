# -*- coding: utf-8 -*-
"""Section « Chiffres à retenir » : ajout des chapitres 5 et 6 de deuxième année.

La section porte sa charge dans `var D = {...};` au sein du bloc
<script id="eco-chiffres">. On la relit, on y ajoute les deux chapitres avec
leurs chiffres prioritaires et complémentaires, puis on la réécrit au format
d'origine.
"""

import json
import sys

import chif_e
import titres_ch2526

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v221_visu.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v221_chif.html'

LIB = {'25': '2ᵉ année — Chapitre 5', '26': '2ᵉ année — Chapitre 6'}
TITRES = {'25': 'Équilibre macroéconomique et politiques conjoncturelles',
          '26': 'Taux de change et systèmes de change'}

s = open(SRC, encoding='utf-8').read()

i = s.find('id="eco-chiffres"')
assert i > 0, 'section « Chiffres à retenir » introuvable'
j = s.find('var D = ', i)
assert j > 0, 'charge D introuvable'
k = s.find('\n', j)
brut = s[j:k][len('var D = '):].rstrip()
assert brut.endswith(';')
D = json.loads(brut[:-1])
assert json.dumps(D, ensure_ascii=False, separators=(',', ':')) == brut[:-1], \
    'la charge ne se réécrit pas à l’identique'

assert '25' not in D['ch'] and '26' not in D['ch'], 'chapitre déjà présent'
avant = sum(len(v['p']) + len(v['c']) for v in D['ch'].values())
print('chiffres lus : %d sur %d chapitres' % (avant, len(D['ch'])))

T = titres_ch2526.T
ajoutes = 0
for c in ('25', '26'):
    src = chif_e.CH[c]
    bloc = {'p': [], 'c': []}
    for imp, liste in (('p', src['prio']), ('c', src['comp'])):
        for rang, x in enumerate(liste, 1):
            cle = '%s%s%d' % (c, imp, rang)
            titre = T.get(cle)
            assert titre, ('titre manquant', cle)
            assert ' : ' in titre, ('titre sans valeur annoncée', cle)
            y = {'v': x['v'], 'u': x['u'], 'nat': x['nat'], 'z': x['z'],
                 'p': x['p'], 's': x['s'], 'd': x['d'], 'q': x['q'],
                 'k': list(x['k']), 't': titre}
            bloc[imp].append(y)
            ajoutes += 1
    D['ch'][c] = bloc
    D['lib'][c] = LIB[c]
    D['titres'][c] = TITRES[c]
    assert c not in D['ordre']
    D['ordre'].append(c)

# tous les titres fournis doivent avoir servi : aucun chiffre oublié
attendus = set()
for c in ('25', '26'):
    for imp, liste in (('p', chif_e.CH[c]['prio']), ('c', chif_e.CH[c]['comp'])):
        for rang in range(1, len(liste) + 1):
            attendus.add('%s%s%d' % (c, imp, rang))
inutiles = sorted(set(T) - attendus)
assert not inutiles, 'titres sans chiffre correspondant : %s' % inutiles

neuf = 'var D = ' + json.dumps(D, ensure_ascii=False, separators=(',', ':')) + ';'
s = s[:j] + neuf + s[k:]

open(DST, 'w', encoding='utf-8').write(s)
total = sum(len(v['p']) + len(v['c']) for v in D['ch'].values())
print('chiffres écrits : %d sur %d chapitres (%d ajoutés)'
      % (total, len(D['ch']), ajoutes))
print('  ch.25 : %d prioritaires, %d complémentaires'
      % (len(D['ch']['25']['p']), len(D['ch']['25']['c'])))
print('  ch.26 : %d prioritaires, %d complémentaires'
      % (len(D['ch']['26']['p']), len(D['ch']['26']['c'])))
print('%s → %s (%.2f Mo)' % (SRC, DST, len(s) / 1048576))
