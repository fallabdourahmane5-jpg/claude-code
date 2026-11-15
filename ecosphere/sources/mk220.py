#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fabrique patch_v220.py à partir de patch_v219.py.

Seule la présentation des résultats change : la feuille de style de la
section et les fonctions de rendu. Le moteur, les définitions, les liens et
les textes affichés sont repris tels quels.
"""
import io

src = io.open('patch_v219.py', encoding='utf-8').read()
css = io.open('style220.css', encoding='utf-8').read().strip()
js = io.open('rendu220.js', encoding='utf-8').read().strip()

# ------------------------------------------------------------------ style
a = src.index('STYLE = r"""') + len('STYLE = r"""')
b = src.index('"""\nMOTEUR = r"""')
assert 'eco-recherche-style-v219' in src[a:b]
src = src[:a] + '\n' + css + '\n' + src[b:]

# ------------------------------------------------------------------- rendu
DEB = '/* --------------------------------------------------- puces « où le retrouver » */'
FIN = 'function comptesRequete(R){'
a = src.index(DEB)
b = src.index(FIN, a)
anc = src[a:b]
for nom in ('function puces(', 'function rendreReponse(', 'function rendreFamille(',
            'function rendreLigne(', 'function ouLib(', 'function rendre(',
            'function barreOutils('):
    assert nom in anc, nom
src = src[:a] + js + '\n\n' + src[b:]

# ------------------------------------------------------- marques de version
src = src.replace("DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v218.html'",
                  "DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v220.html'")
src = src.replace('"""Remplace entièrement la section « Recherche » d\'ÉcoSphère.',
                  '"""Remplace entièrement la section « Recherche » d\'ÉcoSphère.\n\n'
                  'v220 : la présentation des résultats est refaite (hiérarchie de la\n'
                  'réponse, mise en évidence discrète, « à ne pas confondre » lisible,\n'
                  '« où le retrouver » groupé par section, cadres allégés). Le moteur,\n'
                  'les définitions et les destinations sont ceux de la v219.')

io.open('patch_v220.py', 'w', encoding='utf-8').write(src)
print('patch_v220.py écrit —', len(src), 'octets')
