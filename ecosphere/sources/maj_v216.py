#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Met à jour, dans l'application déjà construite, les deux charges de données
rédigées : celle de « Autour d'une notion » (var D) et celle des
« Visualisations stratégiques » (var VZ).

Les couches de style et de moteur sont inchangées : seules les données sont
remplacées, ce qui évite de rejouer toute la chaîne de patchs.
"""
import io
import json
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'app_v215.html'
DST = sys.argv[2] if len(sys.argv) > 2 else 'app_v216.html'

s = io.open(SRC, encoding='utf-8').read()
dec = json.JSONDecoder()


def remplacer(texte, marqueur, charge, nom):
    i = texte.index(marqueur)
    j = texte.index('=', i) + 1
    ancien, fin = dec.raw_decode(texte, j + 1)
    neuf = json.dumps(charge, ensure_ascii=False, separators=(',', ':'))
    print('  %-28s %d -> %d octets' % (nom, fin - j - 1, len(neuf)))
    return texte[:j] + ' ' + neuf + texte[fin:], ancien


AUT = json.load(open('autour_payload.json'))
VZ = json.load(open('visu_payload.json'))

s, aut_av = remplacer(s, 'var D = {"ensembles"', AUT, 'Autour d’une notion')
s, vz_av = remplacer(s, 'var VZ = [', VZ, 'Visualisations')

# contrôles : rien ne doit avoir disparu
assert len(AUT['dossiers']) >= len(aut_av['dossiers'])
assert len(AUT['ensembles']) == len(aut_av['ensembles']) == 28
assert len(VZ) == len(vz_av) == 20

io.open(DST, 'w', encoding='utf-8').write(s)

red = sum(1 for x in AUT['dossiers'] if x['etat'] == 'redige')
print('  dossiers : %d dont %d rédigés (avant : %d dont %d)'
      % (len(AUT['dossiers']), red, len(aut_av['dossiers']),
         sum(1 for x in aut_av['dossiers'] if x['etat'] == 'redige')))
print('OK %s -> %s (%.2f Mo)' % (SRC, DST, len(s.encode('utf-8')) / 1048576.0))
