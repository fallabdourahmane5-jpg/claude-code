# -*- coding: utf-8 -*-
"""Pose la nouvelle section « Quiz » (v223) dans l'application.

Couche additive : la banque de questions, la feuille de style et le moteur
sont ajoutés à la fin du document. Le moteur réécrit le contenu de la page
#pg-quiz et prend la main sur showPg ; l'ancien écran n'est plus affiché.
"""

import json
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'ecosphere_v222.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v223.html'
BANQUE = sys.argv[3] if len(sys.argv) > 3 else 'banque.json'

s = open(SRC, encoding='utf-8').read()
assert 'id="eco-quiz-v223"' not in s, 'la couche est déjà posée'
assert 'id="pg-quiz"' in s, 'page du quiz introuvable'

B = json.load(open(BANQUE, encoding='utf-8'))
charge = 'var BQ = ' + json.dumps(B, ensure_ascii=False,
                                  separators=(',', ':')) + ';'
assert json.loads(charge[len('var BQ = '):-1]) == B

js = open('quiz223.js', encoding='utf-8').read()
assert '/* __PAYLOAD__ */' in js
js = js.replace('/* __PAYLOAD__ */', charge, 1)
css = open('quiz223.css', encoding='utf-8').read()

for interdit in ('</script>', '<script'):
    assert interdit not in charge, 'la charge contient une balise de script'

bloc = ('\n<style id="eco-quiz-v223-style">\n' + css + '\n</style>\n'
        '<script id="eco-quiz-v223">\n' + js + '\n</script>\n')

i = s.rfind('</body>')
assert i > 0, 'fin de document introuvable'
s = s[:i] + bloc + s[i:]
open(DST, 'w', encoding='utf-8').write(s)

q = B['q']
print('banque posée : %d questions, %d sous-parties sur %d chapitres'
      % (len(q), sum(len(v) for v in B['sp'].values()), len(B['sp'])))
print('couche : %.0f Ko de moteur, %.0f Ko de style, %.1f Mo de banque'
      % (len(js.encode()) / 1024 - len(charge.encode()) / 1024,
         len(css.encode()) / 1024, len(charge.encode()) / 1048576))
print('%s → %s (%.2f Mo)' % (SRC, DST, len(s.encode()) / 1048576))
