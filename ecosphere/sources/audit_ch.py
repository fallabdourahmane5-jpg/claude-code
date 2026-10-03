#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pour chaque auteur de l'Atlas, compare les chapitres où il a une entrée avec
les chapitres où son patronyme figure réellement dans le texte des cours."""
import io, json, re, unicodedata, collections, sys

cours = json.load(io.open('cours.json', encoding='utf-8'))
atlas = json.load(io.open('atlas.json', encoding='utf-8'))
ORDRE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 22]


def nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    return ''.join(c for c in s if not unicodedata.combining(c))


# patronyme = dernier mot significatif du nom
PARTICULES = {'de', 'du', 'des', 'van', 'von', 'der', 'le', 'la'}
def patro(nom):
    mots = [m for m in re.split(r'[\s]+', nom) if m and m.lower() not in PARTICULES]
    return mots[-1] if mots else nom

# patronymes trop courants pour être cherchés seuls -> on exige le nom complet
AMBIGUS = {nz(x) for x in ('Say', 'Mill', 'Clark', 'Ford', 'List', 'Law', 'Watt', 'Monnet',
                           'Cohen', 'Simon', 'Sen', 'Rey', 'Means', 'Jenny', 'Allen', 'March',
                           'Bell', 'Hall', 'Hart', 'Moore', 'White', 'Chen', 'Wolf', 'Miller',
                           'Porter', 'Bain', 'Robinson', 'Evans', 'Johnson', 'Wade', 'Douglas',
                           'Carré', 'Dubois', 'Cobb', 'Berger', 'Durant', 'Frey', 'Perot')}

# chapitres où chaque auteur a déjà une entrée
ecrits = collections.defaultdict(set)
noms = {}
for ch in atlas['chapitres']:
    for e in ch['e']:
        k = nz(e['n'])
        ecrits[k].add(ch['k'])
        noms[k] = e['n']

lignes = []
for k, nom in sorted(noms.items(), key=lambda x: x[1]):
    p = patro(nom)
    if nz(p) in AMBIGUS or len(p) < 4:
        pat = re.compile(r'\b' + re.escape(nom), re.I)      # nom complet
    else:
        pat = re.compile(r'\b' + re.escape(p) + r'\b', re.I)  # patronyme
    occ = {}
    for c in ORDRE:
        n = len(pat.findall(cours[str(c)]))
        if n:
            occ[c] = n
    manque = {c: n for c, n in occ.items() if c not in ecrits[k]}
    if manque:
        lignes.append((max(manque.values()), nom, ecrits[k], occ, manque))

lignes.sort(reverse=True)
print('%d auteurs présents dans des chapitres où ils n\'ont pas d\'entrée Atlas\n' % len(lignes))
print('%-28s %-22s %s' % ('AUTEUR', 'ATLAS', 'COURS (manquants en gras)'))
print('-' * 100)
for mx, nom, ec, occ, manque in lignes:
    o = ' '.join(('**ch%s:%d**' % (c, n)) if c in manque else ('ch%s:%d' % (c, n))
                 for c, n in sorted(occ.items()))
    print('%-28s %-22s %s' % (nom[:28], ' '.join('ch%s' % c for c in sorted(ec)), o))
