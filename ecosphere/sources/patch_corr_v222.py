# -*- coding: utf-8 -*-
"""Trois corrections demandées après la livraison v221.

0. Graphie de Jacques Généreux, uniformisée (le document du chapitre 5 porte
   « Jean » ; l'intitulé de section était corrigé, trois mentions non).

1. Renvois non cliquables de l'Atlas.
   - « Frank Galluzzo » : le cours du chapitre 8 ne donne que le patronyme,
     et l'auteur du « Mythe de l'entrepreneur » (2023) est Anthony Galluzzo.
     Le prénom erroné figurait dans la base d'auteurs, dans l'Atlas et dans
     les dossiers ; quatre renvois pointaient vers « Anthony Galluzzo » et
     restaient donc en texte simple.
   - « Orain » : l'entrée de l'Atlas a été renommée « Arnaud Orain », mais le
     renvoi du chapitre 6 et l'index de la base d'auteurs portaient encore le
     seul patronyme.

2. Attribution non justifiée dans l'Atlas du chapitre 2.
   Aucun des seize cours ne traite des zones monétaires optimales : le cours
   du chapitre 2 ne présente de Mundell que le triangle d'incompatibilité,
   « Robert Mundell, 1960s ». L'entrée « Zones monétaires optimales » est donc
   retirée, et l'entrée conservée ne renvoie plus à un ouvrage que les cours
   ne citent pas.
"""

import json
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'ecosphere_v221.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v222_corr.html'

s = open(SRC, encoding='utf-8').read()

# ------------------------------------------------- 1. renvois non cliquables
NOMS = [
 ('Frank Galluzzo', 'Anthony Galluzzo', 9),
 # Le document du chapitre 5 écrit « Jean Généreux » ; l'auteur cité est
 # Jacques Généreux. L'intitulé de section avait été corrigé, trois mentions
 # ne l'étaient pas, ce qui donnait deux graphies dans le même passage.
 ('Jean Généreux', 'Jacques Généreux', 3),
 ('{"a":"Orain"', '{"a":"Arnaud Orain"', 1),
 ('"Orain":[1]', '"Arnaud Orain":[1]', 1),
]
for anc, neuf, n in NOMS:
    vu = s.count(anc)
    assert vu == n, ('occurrences inattendues', anc, vu, n)
    s = s.replace(anc, neuf)
    print('%-22s → %-22s : %d mention(s)' % (anc, neuf, vu))
assert 'Frank Galluzzo' not in s

# ------------------------------- 2. Atlas du chapitre 2 : Mundell et les ZMO
i = s.find('id="eco-atlas-idees"')
assert i > 0
j = s.find('var DATA = ', i)
k = s.find('\n', j)
brut = s[j + len('var DATA = '):k].rstrip()
assert brut.endswith(';')
A = json.loads(brut[:-1])
assert json.dumps(A, ensure_ascii=False, separators=(',', ':')) == brut[:-1]

ch2 = [c for c in A['chapitres'] if c['k'] == 2][0]
avant = len(ch2['e'])
zmo = [x for x in ch2['e']
       if x['n'] == 'Robert Mundell' and x['ti'] == 'Zones monétaires optimales']
assert len(zmo) == 1, 'entrée « Zones monétaires optimales » introuvable'
ch2['e'] = [x for x in ch2['e'] if x is not zmo[0]]
assert len(ch2['e']) == avant - 1

tri = [x for x in ch2['e']
       if x['n'] == 'Robert Mundell' and x['ti'] == "Triangle d'incompatibilité"]
assert len(tri) == 1, 'entrée « Triangle d’incompatibilité » introuvable'
tri = tri[0]
assert tri['ou'] == 'International Economics (1968)', tri['ou']
tri['ou'] = "Travaux sur le triangle d'incompatibilité (années 1960)"
assert 'zone monétaire optimale' in tri['no']
tri['no'] = [x for x in tri['no'] if x != 'zone monétaire optimale']

# Robert Mundell reste présent dans l'Atlas : les renvois vers lui restent
# cliquables.
noms = {x['n'] for c in A['chapitres'] for x in c['e']}
assert 'Robert Mundell' in noms
manquants = sorted({(c['k'], l['a']) for c in A['chapitres'] for x in c['e']
                    for l in (x.get('li') or []) if l['a'] not in noms})
print('idées de l’Atlas : %d' % sum(len(c['e']) for c in A['chapitres']))
print('renvois non cliquables : %d' % len(manquants))
for m in manquants:
    print('   ch%-3s %s' % m)

neuf = 'var DATA = ' + json.dumps(A, ensure_ascii=False,
                                  separators=(',', ':')) + ';'
s = s[:j] + neuf + s[k:]

# Plus aucune trace dans la charge de l'Atlas. La charge indexée de la
# recherche est reconstruite ensuite à partir de l'Atlas : elle est contrôlée
# à ce moment-là.
for interdit in ('zone monétaire optimale', 'zones monétaires optimales',
                 'International Economics (1968)'):
    assert interdit not in neuf, ('formulation non justifiée encore présente '
                                  'dans l’Atlas', interdit)
assert 'Jean Généreux' not in s, 'la graphie corrigée Jacques Généreux a été perdue'

open(DST, 'w', encoding='utf-8').write(s)
print('%s → %s (%.2f Mo)' % (SRC, DST, len(s.encode()) / 1048576))
