# -*- coding: utf-8 -*-
"""Corrections de fidélité sur les livrables des chapitres 5 et 6 de deuxième
année.

Trois défauts relevés à la relecture, tous des attributions que les documents
de cours ne justifient pas :

  1. les dates de Mundell et de Fleming. Les documents écrivent « Fleming
     (1962) et Mundell (1963) » ; plusieurs passages portaient « Mundell
     (1962, 1963) », « Mundell (1961, 1963) » ou « Mundell (1961, 1962,
     1963) », ce qui attribue à Mundell des travaux absents des cours ;
  2. la théorie des zones monétaires optimales et sa date de 1961, qui
     n'apparaissent dans aucun des seize cours de l'application ;
  3. les émissions communes de dette de 2020, absentes des documents.

Le script applique les mêmes corrections au fichier de l'application et aux
modules de contenu, afin qu'un remontage ultérieur reste correct.
"""

import re
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v221_rech.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v221_fid.html'

# (ancien, neuf, nombre minimal attendu dans l'application, modules concernés)
# Un même texte peut figurer deux fois : les résumés sont portés par la section
# « Résumés » et repris dans la charge indexée de la recherche.
C = [
 # --------------------------- 1. ordre des deux auteurs dans le texte suivi
 ("Mundell (1963) et Fleming (1962) ont établi cette symétrie inversée",
  "Fleming (1962) et Mundell (1963) ont établi cette symétrie inversée",
  1, ['don25_suj1.py']),

 ("Mundell (1963) et Fleming (1962) établissent une symétrie inversée",
  "Fleming (1962) et Mundell (1963) établissent une symétrie inversée",
  1, ['res2_25.py']),

 # ------------------------------- 2. zones monétaires optimales et 1961
 ("2ᵉ année ch. 6 (zone monétaire optimale, dévaluation interne)",
  "2ᵉ année ch. 6 (régimes de change, triangle de Mundell, ajustement par "
  "les prix et les salaires)", 1, ['don25_suj3.py']),

 ("3) Une capacité budgétaire centrale rapprocherait la zone des conditions "
  "d’une zone monétaire optimale au sens de Mundell (1963).",
  "3) Une capacité budgétaire centrale rapprocherait la zone d’une "
  "stabilisation comparable à celle d’un État fédéral, que le cours signale "
  "précisément comme hors de portée du budget actuel.", 1, ['don25_suj3.py']),

 ("C’est ce que la théorie des zones monétaires optimales énonçait dès 1961, "
  "et que l’architecture initiale a largement laissé de côté.",
  "Ce sont ces trois chantiers que l’architecture initiale a laissés de côté.",
  1, ['don25_suj3.py']),

 # --------------------------------- 3. émissions communes de dette de 2020
 ("2) Les émissions communes de dette engagées à partir de 2020 constituent "
  "une inflexion, sans transformer l’architecture.",
  "2) À défaut d’un tel instrument, la stabilisation repose sur les seules "
  "politiques budgétaires nationales, elles-mêmes encadrées par les règles "
  "communes.", 1, ['don25_suj3.py']),
]

s = open(SRC, encoding='utf-8').read()
total = 0

# Les documents n'attribuent à Robert Mundell qu'un seul travail daté, celui
# de 1963 ; Fleming porte celui de 1962. Toute liste de dates mentionnant 1961
# ou 1962 derrière le nom de Mundell est donc ramenée à 1963. Les mentions non
# datées héritées des autres chapitres (« 1960s », « trilemme ») sont laissées
# telles quelles.
DATES = re.compile(r'Mundell \((?:1961|1962)(?:, ?(?:1961|1962|1963))*\)')
MODULES_DATES = ['don25_suj1.py', 'don25_suj2.py', 'don25_suj3.py', 'res2_25.py']
n_dates = len(DATES.findall(s))
s = DATES.sub('Mundell (1963)', s)
for m in MODULES_DATES:
    t = open(m, encoding='utf-8').read()
    u = DATES.sub('Mundell (1963)', t)
    if u != t:
        open(m, 'w', encoding='utf-8').write(u)
print('dates de Mundell corrigées : %d mentions' % n_dates)
for anc, neuf, n, mods in C:
    vu = s.count(anc)
    assert vu >= n, ('passage introuvable dans l’application', vu, n, anc[:70])
    s = s.replace(anc, neuf)
    total += vu
    for m in mods:
        t = open(m, encoding='utf-8').read()
        if anc in t:
            open(m, 'w', encoding='utf-8').write(t.replace(anc, neuf))
        else:
            assert neuf in t, ('passage introuvable dans le module', m, anc[:70])

# plus aucune trace des formulations fautives
assert not DATES.search(s), 'une date non justifiée subsiste derrière Mundell'
for interdit in ('zone monétaire optimale au sens de Mundell',
                 'zones monétaires optimales énonçait',
                 'émissions communes de dette engagées'):
    assert interdit not in s, ('formulation fautive encore présente', interdit)

open(DST, 'w', encoding='utf-8').write(s)
print('corrections appliquées : %d passages sur %d règles' % (total, len(C)))
print('%s → %s (%.2f Mo)' % (SRC, DST, len(s.encode()) / 1048576))
