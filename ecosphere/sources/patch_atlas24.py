# -*- coding: utf-8 -*-
"""Atlas des idées : ajout du chapitre 4 de deuxième année (clé 24).

Le contenu de l'Atlas est une charge JSON compacte (`var DATA = {...};`) placée
dans le bloc <script id="eco-atlas-idees">. On la relit, on y insère le
chapitre 24, on applique la correction de l'entrée « Orain » du chapitre 1, puis
on réécrit la charge au format d'origine (JSON compact, accents littéraux).
"""

import json
import sys

import atlas24

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v204.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v205_atlas.html'

TITRE = 'Régionalisation, gouvernance et régulations internationales'
SOUS = ('Doux commerce et interdépendances asymétriques · biens publics mondiaux '
        'et stabilité hégémonique · GATT, OMC et cycles de négociation · création '
        'et détournement de trafic · intégration profonde et bol de spaghettis · '
        'trilemme de Rodrik, capitalisme de la finitude et mondialisation fragmentée.')

s = open(SRC, encoding='utf-8').read()

i = s.find('id="eco-atlas-idees"')
assert i > 0, 'bloc Atlas introuvable'
j = s.find('var DATA = ', i)
assert j > 0, 'charge DATA introuvable'
k = s.find('\n', j)
ligne = s[j:k]
brut = ligne[len('var DATA = '):].rstrip()
assert brut.endswith(';')
D = json.loads(brut[:-1])
assert json.dumps(D, ensure_ascii=False, separators=(',', ':')) == brut[:-1], \
    'la charge Atlas ne se réécrit pas à l’identique'

cles = [c['k'] for c in D['chapitres']]
assert 24 not in cles, 'le chapitre 24 est déjà présent dans l’Atlas'
print('Atlas lu : %d chapitres, %d idées'
      % (len(D['chapitres']), sum(len(c['e']) for c in D['chapitres'])))

# ------------------------------------------------------------------ corrections
for cor in atlas24.CORRECTIONS:
    vus = 0
    for c in D['chapitres']:
        if c['k'] != cor['ch']:
            continue
        for x in c['e']:
            if x['ti'] != cor['cible'] or x['n'] != cor['n_ancien']:
                continue
            x['n'] = cor['n']
            x['ou'] = cor['ou']
            deja = {l['a'] for l in x['li']}
            for l in cor.get('li_ajout', []):
                if l['a'] not in deja:
                    x['li'].append(dict(l))
            vus += 1
    assert vus == 1, 'correction « %s » : %d cible(s)' % (cor['cible'], vus)
    print('corrigé : chapitre %d · %s → %s' % (cor['ch'], cor['n_ancien'], cor['n']))

# ------------------------------------------------------------- nouveau chapitre
entrees = []
for x in atlas24.ENTREES:
    y = {'n': x['n'], 'd': x['d'], 'c': x['c'], 'ti': x['ti'], 'af': x['af'],
         'me': x['me'], 'ex': x['ex'], 'po': x['po'], 'di': x['di'],
         'co': x['co'], 'ou': x['ou'], 'no': list(x['no']),
         'li': [dict(l) for l in x['li']], 'ch': 24}
    entrees.append(y)

D['chapitres'].append({'k': 24, 'annee': 2, 'lib': '2ᵉ année — Chapitre 4',
                       'titre': TITRE, 'sous': SOUS, 'e': entrees})

# les liens vers un auteur absent de l'Atlas ne seraient pas cliquables
noms = set()
for c in D['chapitres']:
    for x in c['e']:
        noms.add(x['n'])
for c in D['chapitres']:
    if c['k'] != 24:
        continue
    for x in c['e']:
        for l in x['li']:
            assert l['a'] in noms, 'lien mort vers « %s »' % l['a']
            assert l['r'] in ('complement', 'opposition', 'prolonge'), l['r']

neuf = 'var DATA = ' + json.dumps(D, ensure_ascii=False, separators=(',', ':')) + ';'
s = s[:j] + neuf + s[k:]

open(DST, 'w', encoding='utf-8').write(s)
print('Atlas écrit : %d chapitres, %d idées (dont %d pour le chapitre 24)'
      % (len(D['chapitres']), sum(len(c['e']) for c in D['chapitres']), len(entrees)))
print('%s → %s (%.2f Mo)' % (SRC, DST, len(s) / 1048576))
