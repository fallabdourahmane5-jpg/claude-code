# -*- coding: utf-8 -*-
"""Page « Mon Progrès » : le compteur de chapitres visités était figé sur six.

Le dénominateur datait d'une version où l'application ne comptait que six
chapitres ; elle en porte seize. Il est désormais calculé.
"""
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'ecosphere_v221.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'ecosphere_v221b.html'

ANC = '<div class="pn">${visited}/6</div><div class="pl">Chapitres visités</div>'
NEUF = ('<div class="pn">${visited}/${Object.keys(CH_CONTENT).length}</div>'
        '<div class="pl">Chapitres visités</div>')

s = open(SRC, encoding='utf-8').read()
n = s.count(ANC)
assert n == 1, ('compteur introuvable ou multiple', n)
open(DST, 'w', encoding='utf-8').write(s.replace(ANC, NEUF))
print('compteur de chapitres visités : dénominateur calculé')
