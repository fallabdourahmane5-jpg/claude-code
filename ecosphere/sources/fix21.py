#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deux libellés « 21 » encore visibles, contraires à la règle « jamais
Chapitre 21/22 » :
  1. Sujets — « Ch. 21 — 2ᵉ année ch. 1 (…) » : le préfixe « Ch. 21 — » est
     redondant, le libellé correct suit juste après. 52 occurrences, toutes
     identiques, corrigées à la source.
  2. Auteurs — badge « Chapitre 21 » : #pg-authors ne figurait pas dans les
     listes de la couche de relibellage du chapitre 21 (contrairement à celle
     du chapitre 22). On l'ajoute, avec #pg-frise et #pg-visualisations."""
import io

SRC = 'app_v190.html'
DST = 'app_v191.html'

s = io.open(SRC, encoding='utf-8').read()

# ---- 1. préfixe redondant dans les « chapitres à mobiliser » des sujets
MOTIF = 'Ch. 21 — 2ᵉ année ch. 1 ('
assert s.count(MOTIF) == 52, s.count(MOTIF)
s = s.replace(MOTIF, '2ᵉ année ch. 1 (')
assert 'Ch. 21 —' not in s

# ---- 2. #pg-authors absent des listes de relibellage du chapitre 21
A = "['#pg-chapter','#pg-quiz','#pg-maps','#pg-subjects','#pg-search','#pg-home','#pg-fc','#pg-prog','#pg-graphs']"
B = "['#pg-quiz','#pg-chapter','#pg-search','#pg-maps','#pg-subjects','#pg-home','#pg-prog','#pg-fc']"
assert s.count(A) == 1 and s.count(B) == 1
s = s.replace(A, A[:-1] + ",'#pg-authors','#pg-frise','#pg-visualisations']", 1)
s = s.replace(B, B[:-1] + ",'#pg-authors','#pg-frise','#pg-visualisations']", 1)

io.open(DST, 'w', encoding='utf-8').write(s)
print('OK %s -> %s (%.2f Mo)' % (SRC, DST, len(s.encode('utf-8')) / 1048576.0))
