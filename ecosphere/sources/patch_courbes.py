# -*- coding: utf-8 -*-
"""Pose la nouvelle section « Courbes » (v225) dans l'application.

Couche additive : la charge, la feuille de style et le moteur sont ajoutés à
la fin du document. Le moteur réécrit le contenu de la page #pg-graphs et
prend la main sur showPg ; l'ancien catalogue d'images n'est plus affiché.
L'ancienne couche reste en place mais devient inerte.
"""

import json
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v224.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v225.html'
CHARGE = sys.argv[3] if len(sys.argv) > 3 else 'courbes.json'

s = open(SRC, encoding='utf-8').read()
assert 'id="eco-courbes-v225"' not in s, 'la couche est déjà posée'
assert 'id="pg-graphs"' in s, 'page des courbes introuvable'

B = json.load(open(CHARGE, encoding='utf-8'))
charge = 'var CB = ' + json.dumps(B, ensure_ascii=False,
                                  separators=(',', ':')) + ';'
assert json.loads(charge[len('var CB = '):-1]) == B

js = open('courbes.js', encoding='utf-8').read()
assert '/* __PAYLOAD__ */' in js
js = js.replace('/* __PAYLOAD__ */', charge, 1)
css = open('courbes.css', encoding='utf-8').read()

for interdit in ('</script>', '<script'):
    assert interdit not in charge, 'la charge contient une balise de script'

bloc = ('\n<style id="eco-courbes-v225-style">\n' + css + '\n</style>\n'
        '<script id="eco-courbes-v225">\n' + js + '\n</script>\n')

i = s.rfind('</body>')
assert i > 0, 'fin de document introuvable'
s = s[:i] + bloc + s[i:]
open(DST, 'w', encoding='utf-8').write(s)

print('courbes posées : %d fiches, %d thèmes' % (len(B['f']), len(B['cat'])))
print('couche : %.0f Ko de moteur, %.0f Ko de style, %.0f Ko de charge'
      % (len(js.encode()) / 1024 - len(charge.encode()) / 1024,
         len(css.encode()) / 1024, len(charge.encode()) / 1024))
print('%s → %s (%.2f Mo)' % (SRC, DST, len(s.encode()) / 1048576))
