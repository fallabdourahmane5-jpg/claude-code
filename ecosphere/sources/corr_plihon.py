#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corrige le prénom de Plihon dans la base d'auteurs et partout où il est repris.

Les cours écrivent « D. Plihon » et « Plihon » : l'économiste est Dominique
Plihon, auteur des Capitalismes contemporains (2025). L'application était
incohérente avec elle-même — les résumés de chapitre, les « à retenir » et la
banque de quiz écrivaient déjà « Dominique Plihon », tandis que la base
d'auteurs, l'Atlas, deux dossiers et une visualisation écrivaient « David
Plihon ». Ce script aligne tout sur la forme correcte.

Le texte des cours n'est pas touché : il n'écrit jamais le prénom.
"""
import io
import os
import sys

FAUX = 'David Plihon'
VRAI = 'Dominique Plihon'

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v216.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v217.html'

FICHIERS = ['atlas.json', 'atlas_a.py', 'atlas_c.py', 'audit1.json',
            'auteurs_par_chapitre.txt', 'chapitres_auteurs.json',
            'doss02b.py', 'doss02d.py', 'enr_ch8.py', 'enr_v196a.py']

# ------------------------------------------------------------- l'application
s = io.open(SRC, encoding='utf-8').read()
n = s.count(FAUX)
assert n, 'rien à corriger dans %s' % SRC
avant_cours = s.count('D. Plihon')
t = s.replace(FAUX, VRAI)
assert t.count(FAUX) == 0
assert t.count('D. Plihon') == avant_cours, 'le texte des cours a bougé'
assert len(t) == len(s) + n * (len(VRAI) - len(FAUX))
io.open(DST, 'w', encoding='utf-8').write(t)
print('%s : %d occurrences corrigées -> %s (%.2f Mo)'
      % (SRC, n, DST, len(t.encode('utf-8')) / 1048576.0))

# ------------------------------------------------------------------- sources
for f in FICHIERS:
    if not os.path.exists(f):
        print('  absent :', f)
        continue
    u = io.open(f, encoding='utf-8').read()
    k = u.count(FAUX)
    if not k:
        continue
    io.open(f, 'w', encoding='utf-8').write(u.replace(FAUX, VRAI))
    print('  %-28s %d occurrence(s)' % (f, k))
