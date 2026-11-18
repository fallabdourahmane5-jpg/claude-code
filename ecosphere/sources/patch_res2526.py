# -*- coding: utf-8 -*-
"""Section « Résumés des chapitres » : ajout des chapitres 5 et 6 de deuxième
année.

La section porte sa charge dans `var D = {...};` au sein du bloc
<script id="eco-resumes">. On la relit, on y ajoute les deux résumés
approfondis, puis on la réécrit au format d'origine.
"""

import json
import sys

import res2_25
import res2_26

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v221_chif.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v221_res.html'

LIB = {'25': '2ᵉ année — Chapitre 5', '26': '2ᵉ année — Chapitre 6'}
TITRES = {'25': 'L’équilibre macroéconomique : IS-LM, IS-LM-BP et OG-DG',
          '26': 'Taux de change et systèmes de change'}
CHAMPS = ('q', 'ess', 'parties', 'ae', 'arg', 'deb', 'lien', 'min')

s = open(SRC, encoding='utf-8').read()

i = s.find('id="eco-resumes"')
assert i > 0, 'section « Résumés » introuvable'
j = s.find('var D = ', i)
assert j > 0, 'charge D introuvable'
k = s.find('\n', j)
brut = s[j:k][len('var D = '):].rstrip()
assert brut.endswith(';')
D = json.loads(brut[:-1])
assert json.dumps(D, ensure_ascii=False, separators=(',', ':')) == brut[:-1], \
    'la charge ne se réécrit pas à l’identique'

assert '25' not in D['ch'] and '26' not in D['ch'], 'chapitre déjà présent'
modele = D['ch']['24']
print('résumés lus : %d chapitres' % len(D['ch']))

for c, mod in (('25', res2_25.R), ('26', res2_26.R)):
    src = mod[c]
    assert set(src) == set(CHAMPS), set(src) ^ set(CHAMPS)
    assert set(src) == set(modele), 'champs différents de ceux du chapitre 24'
    assert len(src['ess']) > 3000, (c, len(src['ess']))
    assert len(src['parties']) >= 10, (c, len(src['parties']))
    assert len(src['min']) >= 20, (c, len(src['min']))
    for p in src['parties']:
        assert p['t'] and p['sp'], c
        for sp in p['sp']:
            assert sp['t'] and sp['d'], (c, p['t'])
    for x in src['ae']:
        assert set(x) == {'n', 'k', 'i'}, set(x)
        assert x['k'] in ('a', 'e'), x['k']
    for x in src['lien']:
        assert set(x) == {'c', 'p'}, set(x)
    D['ch'][c] = {ch: src[ch] for ch in CHAMPS}
    D['lib'][c] = LIB[c]
    D['titres'][c] = TITRES[c]
    assert c not in D['ordre']
    D['ordre'].append(c)

neuf = 'var D = ' + json.dumps(D, ensure_ascii=False, separators=(',', ':')) + ';'
s = s[:j] + neuf + s[k:]

open(DST, 'w', encoding='utf-8').write(s)
for c in ('25', '26'):
    x = D['ch'][c]
    print('  ch.%s : %d car. d’essentiel, %d parties, %d repères, %d auteurs et '
          'exemples, %d arguments, %d débats, %d liens'
          % (c, len(x['ess']), len(x['parties']), len(x['min']), len(x['ae']),
             len(x['arg']), len(x['deb']), len(x['lien'])))
print('résumés écrits : %d chapitres' % len(D['ch']))
print('%s → %s (%.2f Mo)' % (SRC, DST, len(s) / 1048576))
