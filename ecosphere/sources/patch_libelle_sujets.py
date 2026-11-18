# -*- coding: utf-8 -*-
"""Libellé du chapitre sur les cartes de sujets.

La carte d'un sujet affichait « Chapitre 25 » ou « Chapitre 26 », alors que le
reste de l'application nomme ces chapitres « 2ᵉ année — Chapitre 5 » et
« 2ᵉ année — Chapitre 6 ». Le gabarit de la carte calcule désormais le libellé,
pour les quatre premiers chapitres de deuxième année comme pour les deux
nouveaux.
"""
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v221_fid.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v221_lib.html'

ANC = '<div class="subj-meta">Chapitre ${s.chapter}</div>'
NEUF = ('<div class="subj-meta">${escapeHTML((function(c){var m={'
        "'21':'2ᵉ année — Chapitre 1','22':'2ᵉ année — Chapitre 2',"
        "'23':'2ᵉ année — Chapitre 3','24':'2ᵉ année — Chapitre 4',"
        "'25':'2ᵉ année — Chapitre 5','26':'2ᵉ année — Chapitre 6'};"
        "return m[String(c)]||('Chapitre '+c);})(s.chapter))}</div>")

s = open(SRC, encoding='utf-8').read()
n = s.count(ANC)
assert n == 1, ('gabarit de carte introuvable ou multiple', n)
s = s.replace(ANC, NEUF)
open(DST, 'w', encoding='utf-8').write(s)
print('libellé des cartes de sujets corrigé')
print('%s → %s (%.2f Mo)' % (SRC, DST, len(s.encode()) / 1048576))
