# -*- coding: utf-8 -*-
"""Assemble la banque de flashcards à partir des modules par chapitre."""
import importlib
import sys
import fc_base as F

MODULES = [m for m in sys.argv[1:]] or ['fc_ch01']

CARTES, BILANS = [], []
for m in MODULES:
    mod = importlib.import_module(m)
    lot = list(mod.L)
    CARTES.extend(lot)

for ch in sorted({k['ch'] for k in CARTES}, key=int):
    BILANS.append(F.bilan(CARTES, ch))

print()
F.monter(CARTES, 'flashcards.json', BILANS)
