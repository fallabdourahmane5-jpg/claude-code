# -*- coding: utf-8 -*-
"""Pose la nouvelle section Flashcards (v227).

La banque automatique est vidée et scellée par la couche elle-même ; ce
script n'ajoute que le style, le moteur et la banque écrite à la main.
"""

import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v226.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v227.html'
BANQUE = sys.argv[3] if len(sys.argv) > 3 else 'flashcards.json'

TITRES = {
    "1": "Pauvreté Monétaire, Circuit Économique & Consommation",
    "2": "Le Financement de l'Économie",
    "3": "Grands Courants de l'Analyse Économique",
    "4": "Analyse Microéconomique (I) : Le Consommateur",
    "5": "Analyse Microéconomique (II) : Défaillances du Marché",
    "6": "La Croissance Économique",
    "7": "Développement : stratégies, inégalités et soutenabilité",
    "8": "Révolutions industrielles, entreprise, travail et IA",
    "9": "Taille et stratégies des entreprises en concurrence imparfaite",
    "10": "Éléments de sociologie des organisations et du travail",
    "21": "Mondialisation, ouverture internationale et déséquilibres extérieurs",
    "22": "Les acteurs de la mondialisation économique : FMN et États",
    "23": "L’analyse économique du commerce international",
    "24": "Régionalisation, gouvernance et régulations internationales",
    "25": "L’équilibre macroéconomique : IS-LM, IS-LM-BP et OG-DG",
    "26": "Taux de change et systèmes de change",
}


def main():
    s = open(os.path.join(ICI, SRC), encoding='utf-8').read()
    assert 'id="eco-flashcards-v227"' not in s, 'la couche est déjà posée'
    assert 'id="pg-fc"' in s, 'section Flashcards introuvable'

    B = json.load(open(os.path.join(ICI, BANQUE), encoding='utf-8'))
    an = {}
    for k in B['cartes']:
        an[k['ch']] = k['an']
    charge = {'cartes': B['cartes'], 'an': an, 'titres': TITRES,
              'bilans': B.get('bilans') or []}
    payload = 'var FX = ' + json.dumps(charge, ensure_ascii=False,
                                       separators=(',', ':')) + ';'
    assert json.loads(payload[len('var FX = '):-1]) == charge

    js = open(os.path.join(ICI, 'flashcards.js'), encoding='utf-8').read()
    assert '/* __PAYLOAD__ */' in js
    js = js.replace('/* __PAYLOAD__ */', payload, 1)
    css = open(os.path.join(ICI, 'flashcards.css'), encoding='utf-8').read()

    for mot in ('</script>', '<script'):
        assert mot not in payload, 'la banque contient une balise de script'

    bloc = ('\n<style id="eco-flashcards-v227-style">\n' + css + '\n</style>\n'
            '<script id="eco-flashcards-v227">\n' + js + '\n</script>\n')
    i = s.rfind('</body>')
    assert i > 0, 'fin de document introuvable'
    s = s[:i] + bloc + s[i:]
    open(os.path.join(ICI, DST), 'w', encoding='utf-8').write(s)

    par = {}
    for k in B['cartes']:
        par[k['ch']] = par.get(k['ch'], 0) + 1
    print('flashcards posées : %d cartes sur %d chapitres'
          % (len(B['cartes']), len(par)))
    print('couche : %.0f Ko de moteur, %.0f Ko de style, %.0f Ko de banque'
          % ((len(js.encode()) - len(payload.encode())) / 1024,
             len(css.encode()) / 1024, len(payload.encode()) / 1024))
    print('%s → %s (%.2f Mo)' % (SRC, DST, len(s.encode()) / 1048576))


main()
