# -*- coding: utf-8 -*-
"""Pose la grille d'autoévaluation et l'exemple fil rouge (v226).

Couche additive : la section « Méthode Dissertation » existante n'est pas
touchée ; deux cartes lui sont ajoutées à la fin.
"""

import json
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v225.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v226.html'
CHARGE = sys.argv[3] if len(sys.argv) > 3 else 'methode.json'

s = open(SRC, encoding='utf-8').read()
assert 'id="eco-methode-v226"' not in s, 'la couche est déjà posée'
assert 'id="methodGrid"' in s, 'section Méthode introuvable'

B = json.load(open(CHARGE, encoding='utf-8'))
charge = 'var MT = ' + json.dumps(B, ensure_ascii=False,
                                  separators=(',', ':')) + ';'
assert json.loads(charge[len('var MT = '):-1]) == B

js = open('methode.js', encoding='utf-8').read()
assert '/* __PAYLOAD__ */' in js
js = js.replace('/* __PAYLOAD__ */', charge, 1)
css = open('methode.css', encoding='utf-8').read()

for interdit in ('</script>', '<script'):
    assert interdit not in charge, 'la charge contient une balise de script'

bloc = ('\n<style id="eco-methode-v226-style">\n' + css + '\n</style>\n'
        '<script id="eco-methode-v226">\n' + js + '\n</script>\n')

i = s.rfind('</body>')
assert i > 0, 'fin de document introuvable'
s = s[:i] + bloc + s[i:]
open(DST, 'w', encoding='utf-8').write(s)

n = sum(len(g['items']) for g in B['grille'])
notes = sum(len(pa.get('n') or []) for p in B['pieces'] for pa in p['paras'])
notes += sum(len(p.get('globaux') or []) for p in B['pieces'])
notes += len(B['plan'].get('notes') or [])
print('méthode posée : %d critères, %d pièces rédigées, %d annotations'
      % (n, len(B['pieces']) + 1, notes))
print('couche : %.0f Ko de moteur, %.0f Ko de style, %.0f Ko de charge'
      % (len(js.encode()) / 1024 - len(charge.encode()) / 1024,
         len(css.encode()) / 1024, len(charge.encode()) / 1024))
print('%s → %s (%.2f Mo)' % (SRC, DST, len(s.encode()) / 1048576))
