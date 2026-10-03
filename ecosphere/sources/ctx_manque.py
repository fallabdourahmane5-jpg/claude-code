#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extrait le contexte de chaque couple (auteur, chapitre manquant)."""
import io, json, re, unicodedata, collections, sys

cours = json.load(io.open('cours.json', encoding='utf-8'))
atlas = json.load(io.open('atlas.json', encoding='utf-8'))
ORDRE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 22]
MINI = int(sys.argv[1]) if len(sys.argv) > 1 else 2
W = int(sys.argv[2]) if len(sys.argv) > 2 else 650


def nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    return ''.join(c for c in s if not unicodedata.combining(c))


PARTICULES = {'de', 'du', 'des', 'van', 'von', 'der', 'le', 'la'}
def patro(nom):
    m = [x for x in nom.split() if x.lower() not in PARTICULES]
    return m[-1] if m else nom

AMBIGUS = {nz(x) for x in ('Say','Mill','Clark','Ford','List','Law','Watt','Monnet','Cohen','Simon',
                           'Sen','Rey','Means','Jenny','Allen','March','Bell','Hall','Hart','Moore',
                           'White','Chen','Wolf','Miller','Porter','Bain','Robinson','Evans',
                           'Johnson','Wade','Douglas','Carré','Dubois','Cobb','Berger','Durant',
                           'Frey','Perot','Colbert')}

ecrits = collections.defaultdict(set); noms = {}
for ch in atlas['chapitres']:
    for e in ch['e']:
        ecrits[nz(e['n'])].add(ch['k']); noms[nz(e['n'])] = e['n']

res = []
for k, nom in noms.items():
    p = patro(nom)
    pat = re.compile(r'\b' + re.escape(nom if (nz(p) in AMBIGUS or len(p) < 4) else p) + r'\b', re.I)
    for c in ORDRE:
        if c in ecrits[k]:
            continue
        pos = [m.start() for m in pat.finditer(cours[str(c)])]
        if len(pos) < MINI:
            continue
        res.append((len(pos), nom, c, pos))

res.sort(reverse=True)
print('%d couples (auteur, chapitre) à examiner — seuil %d occurrences\n' % (len(res), MINI))
for n, nom, c, pos in res:
    t = cours[str(c)]
    blocs = []
    for q in pos:
        if blocs and q - blocs[-1][1] < W:
            blocs[-1][1] = q
        else:
            blocs.append([q, q])
    print('\n' + '=' * 92)
    print('### %s — CHAPITRE %s (%d occurrences, %d blocs)' % (nom, c, n, len(blocs)))
    print('=' * 92)
    for a, b in blocs[:3]:
        print('  …%s…\n' % re.sub(r'\s+', ' ', t[max(0, a - 260):b + W]))
