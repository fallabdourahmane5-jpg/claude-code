# -*- coding: utf-8 -*-
"""Relit dans l'application bâtie les charges des sections « Autour d'une
notion » et « Visualisations stratégiques », afin que la moisson de la section
Recherche indexe bien l'état courant (chapitres 5 et 6 compris).

Ces deux fichiers étaient jusqu'ici produits par batir_autour.py / batir_visu.py ;
comme les chapitres 25 et 26 ont été ajoutés directement dans la charge de
l'application, c'est l'application qui fait désormais foi.
"""
import json
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v221_res.html'
s = open(SRC, encoding='utf-8').read()


def charge(ancre, nom):
    i = s.find('id="%s"' % ancre)
    assert i > 0, 'bloc %s introuvable' % ancre
    j = s.find('var %s = ' % nom, i)
    assert j > 0, 'charge %s introuvable' % nom
    k = s.find('\n', j)
    brut = s[j:k][len('var %s = ' % nom):].rstrip()
    assert brut.endswith(';')
    o = json.loads(brut[:-1])
    assert json.dumps(o, ensure_ascii=False, separators=(',', ':')) == brut[:-1]
    return o


D = charge('eco-autour-notion', 'D')
VZ = charge('v215-visu-engine', 'VZ')

json.dump(D, open('autour_payload.json', 'w', encoding='utf-8'),
          ensure_ascii=False, separators=(',', ':'))
json.dump(VZ, open('visu_payload.json', 'w', encoding='utf-8'),
          ensure_ascii=False, separators=(',', ':'))

ch25 = sum(1 for x in D['dossiers']
           if any(str(c.get('k')) in ('25', '26')
                  for c in ((x.get('liens') or {}).get('ch') or [])))
print('autour_payload.json : %d dossiers (%d ensembles), dont %d liés aux '
      'chapitres 5 ou 6' % (len(D['dossiers']), len(D['ensembles']), ch25))
v25 = sum(1 for v in VZ
          if any(str(c.get('k')) in ('25', '26') for c in (v.get('chapitres') or [])))
print('visu_payload.json : %d visualisations, dont %d liées aux chapitres 5 ou 6'
      % (len(VZ), v25))
