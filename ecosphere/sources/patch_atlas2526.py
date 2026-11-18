# -*- coding: utf-8 -*-
"""Atlas des idées : ajout des chapitres 5 et 6 de deuxième année (25 et 26).

Le contenu de l'Atlas est une charge JSON compacte (`var DATA = {...};`) placée
dans le bloc <script id="eco-atlas-idees">. On la relit, on y insère les deux
chapitres, on complète quelques entrées existantes par des liens vers les
nouveaux chapitres, puis on réécrit la charge au format d'origine.
"""

import json
import sys

import atlas2526

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v221.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v221_atlas.html'

CHAP = {
    25: {'lib': '2ᵉ année — Chapitre 5',
         'titre': 'L’équilibre macroéconomique : IS-LM, IS-LM-BP et OG-DG',
         'sous': ('Demande effective et équilibre de sous-emploi · multiplicateur '
                  'et fuites · préférence pour la liquidité et courbe LM · effet '
                  'd’éviction et trappe à liquidité · critiques monétaristes et '
                  'modèle OG-DG · policy mix · courbe BP, Mundell-Fleming et '
                  'triangle des incompatibilités.')},
    26: {'lib': '2ᵉ année — Chapitre 6',
         'titre': 'Taux de change et systèmes de change',
         'sous': ('Monnaie, devise et mesure du change · marché des changes et '
                  'financiarisation · parité des pouvoirs d’achat et effet '
                  'Balassa-Samuelson · régimes de change et peur du flottement · '
                  'triangle de Mundell et histoire du SMI · dévaluation '
                  'compétitive, Marshall-Lerner et courbe en J · désinflation '
                  'compétitive et théorème de Schmidt.')},
}

s = open(SRC, encoding='utf-8').read()

i = s.find('id="eco-atlas-idees"')
assert i > 0, 'bloc Atlas introuvable'
j = s.find('var DATA = ', i)
assert j > 0, 'charge DATA introuvable'
k = s.find('\n', j)
brut = s[j:k][len('var DATA = '):].rstrip()
assert brut.endswith(';')
D = json.loads(brut[:-1])
assert json.dumps(D, ensure_ascii=False, separators=(',', ':')) == brut[:-1], \
    'la charge Atlas ne se réécrit pas à l’identique'

cles = [int(c['k']) for c in D['chapitres']]
assert 25 not in cles and 26 not in cles, 'chapitre déjà présent dans l’Atlas'
print('Atlas lu : %d chapitres, %d idées'
      % (len(D['chapitres']), sum(len(c['e']) for c in D['chapitres'])))

# ------------------------------------------------------------- corrections
for cor in atlas2526.CORRECTIONS:
    vus = 0
    for c in D['chapitres']:
        if int(c['k']) != cor['ch']:
            continue
        for x in c['e']:
            if x['n'] != cor['n']:
                continue
            deja = {l['a'] for l in x['li']}
            for l in cor.get('li_ajout', []):
                if l['a'] not in deja:
                    x['li'].append(dict(l))
            vus += 1
    assert vus >= 1, 'entrée introuvable : chapitre %d · %s' % (cor['ch'], cor['n'])
    print('complété : chapitre %-3d · %-26s (%d entrée(s))' % (cor['ch'], cor['n'], vus))

# ---------------------------------------------------------- nouveaux chapitres
ajout = {}
for N in (25, 26):
    entrees = []
    for x in atlas2526.ENTREES:
        if x['ch'] != N:
            continue
        entrees.append({'n': x['n'], 'd': x['d'], 'c': x['c'], 'ti': x['ti'],
                        'af': x['af'], 'me': x['me'], 'ex': x['ex'],
                        'po': x['po'], 'di': x['di'], 'co': x['co'],
                        'ou': x['ou'], 'no': list(x['no']),
                        'li': [dict(l) for l in x['li']], 'ch': N})
    assert entrees, N
    ajout[N] = entrees
    D['chapitres'].append({'k': N, 'annee': 2, 'lib': CHAP[N]['lib'],
                           'titre': CHAP[N]['titre'], 'sous': CHAP[N]['sous'],
                           'e': entrees})

# ------------------------------------------------------------- contrôles
noms = set()
for c in D['chapitres']:
    for x in c['e']:
        noms.add(x['n'])
orphelins = {}
for N in (25, 26):
    for x in ajout[N]:
        for l in x['li']:
            assert l['r'] in ('complement', 'opposition', 'prolonge'), l['r']
            if l['a'] not in noms:
                orphelins.setdefault(l['a'], 0)
                orphelins[l['a']] += 1
if orphelins:
    # le rendu affiche alors le nom sans lien cliquable : c'est admis, mais on
    # le signale pour que le choix reste explicite.
    print('liens non cliquables (auteur absent de l’Atlas) : '
          + ', '.join('%s ×%d' % (a, n) for a, n in sorted(orphelins.items())))

neuf = 'var DATA = ' + json.dumps(D, ensure_ascii=False, separators=(',', ':')) + ';'
s = s[:j] + neuf + s[k:]

open(DST, 'w', encoding='utf-8').write(s)
print('Atlas écrit : %d chapitres, %d idées (dont %d pour le ch.25 et %d pour le ch.26)'
      % (len(D['chapitres']), sum(len(c['e']) for c in D['chapitres']),
         len(ajout[25]), len(ajout[26])))
print('%s → %s (%.2f Mo)' % (SRC, DST, len(s) / 1048576))
