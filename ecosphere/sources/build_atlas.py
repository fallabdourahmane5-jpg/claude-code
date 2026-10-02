#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble l'Atlas des idées : vérifie la couverture, fusionne avec les
métadonnées d'AUTHORS (dates, courant) et produit atlas.json."""
import io, json, unicodedata, sys

from atlas_a import A
from atlas_b import B
from atlas_c import C
from atlas_d import D
from atlas_e import E

ATLAS = {}
for src in (A, B, C, D, E):
    ATLAS.update(src)

ORDRE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 22]

# fusions documentées : un même auteur apparaît sous deux graphies dans AUTHORS
ALIAS = {
    'walt rostow': 'Walt Whitman Rostow',
    'james robinson': 'James A. Robinson',
    'frank galluzzo': 'Anthony Galluzzo',
}

# entrées ajoutées à partir du texte du cours (et non d'AUTHORS)
HORS_AUTHORS = {
    22: ['Ronald Coase', 'Richard Baldwin', 'Charles-Albert Michalet', 'Paul Krugman'],
}


def norm(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return ' '.join(s.replace('.', ' ').split())


def cle(nom):
    n = norm(nom)
    return norm(ALIAS.get(n, nom))


data = json.load(io.open('data.json', encoding='utf-8'))
AUT = data['AUTHORS']
CHAP = data['chapitres']


def chapitres_de(a):
    src = a.get('chapters') or ([a.get('ch')] if a.get('ch') is not None else [])
    return sorted({c for c in src if c is not None})


# ---- index des métadonnées par (clé auteur) : on garde la fiche la plus riche
meta = {}
for a in AUT:
    k = cle(a['name'])
    cur = meta.setdefault(k, {'name': a['name'], 'dates': '', 'courant': '', 'oeuvres': [], 'poids': -1})
    poids = len(a.get('detail') or '') + len(a.get('idea') or '')
    if a.get('dates') and len(a['dates']) > len(cur['dates']):
        cur['dates'] = a['dates']
    if a.get('courant') and len(a['courant']) > len(cur['courant']):
        cur['courant'] = a['courant']
    for o in (a.get('oeuvres') or []):
        if o not in cur['oeuvres']:
            cur['oeuvres'].append(o)
    if poids > cur['poids']:
        cur['poids'] = poids
        cur['name'] = a['name']

# ---- couples (chapitre, auteur) attendus
attendu = {}
for c in ORDRE:
    attendu[c] = set()
for a in AUT:
    for c in chapitres_de(a):
        if c in attendu:
            attendu[c].add(cle(a['name']))
for c, noms in HORS_AUTHORS.items():
    for n in noms:
        attendu[c].add(cle(n))

# ---- couples effectivement rédigés
ecrit = {c: {cle(e[0]) for e in ATLAS.get(c, [])} for c in ORDRE}

erreurs = []
for c in ORDRE:
    manquants = attendu[c] - ecrit[c]
    surplus = ecrit[c] - attendu[c]
    if manquants:
        erreurs.append('ch%s MANQUE : %s' % (c, ', '.join(sorted(manquants))))
    if surplus:
        erreurs.append('ch%s EN TROP : %s' % (c, ', '.join(sorted(surplus))))
    doublons = [e[0] for e in ATLAS.get(c, [])]
    vus = set()
    for n in doublons:
        if cle(n) in vus:
            erreurs.append('ch%s DOUBLON : %s' % (c, n))
        vus.add(cle(n))

if erreurs:
    print('\n'.join(erreurs))
    sys.exit('COUVERTURE INCOMPLÈTE')

# ---- titre et libellé des chapitres
def libelle(c):
    if c == 21:
        return '2ᵉ année — Chapitre 1'
    if c == 22:
        return '2ᵉ année — Chapitre 2'
    return 'Chapitre %d' % c


CHAMPS = ('affirme', 'mecanisme', 'exemple', 'diss')

out = {'chapitres': [], 'genere': True}
total = 0
liens_total = 0
noms_connus = set()
for c in ORDRE:
    noms_connus |= ecrit[c]

for c in ORDRE:
    info = CHAP[str(c)]
    entrees = []
    for nom, titre, d in ATLAS[c]:
        k = cle(nom)
        m = meta.get(k, {})
        for ch in CHAMPS:
            v = (d.get(ch) or '').strip()
            if len(v) < 60:
                sys.exit('ch%s / %s : champ %s trop court (%d)' % (c, nom, ch, len(v)))
        liens = []
        for ln in d.get('liens') or []:
            if len(ln) != 3:
                sys.exit('ch%s / %s : lien mal formé' % (c, nom))
            cible, rel, txt = ln
            if rel not in ('complement', 'opposition', 'prolonge'):
                sys.exit('ch%s / %s : relation inconnue %r' % (c, nom, rel))
            if cle(cible) not in noms_connus:
                sys.exit('ch%s / %s : lien vers un auteur absent de l\'Atlas : %s' % (c, nom, cible))
            liens.append({'a': cible, 'r': rel, 't': txt})
        liens_total += len(liens)
        entrees.append({
            'n': m.get('name') or nom,
            'd': m.get('dates') or '',
            'c': m.get('courant') or '',
            'ti': titre,
            'af': d['affirme'], 'me': d['mecanisme'], 'ex': d['exemple'], 'di': d['diss'],
            'ou': (d.get('ouvrage') or '').strip(),
            'no': d.get('notions') or [],
            'li': liens,
            'ch': c,
        })
        total += 1
    out['chapitres'].append({
        'k': c,
        'annee': 2 if c >= 21 else 1,
        'lib': libelle(c),
        'titre': info.get('title') or '',
        'sous': info.get('sub') or '',
        'e': entrees,
    })

io.open('atlas.json', 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, separators=(',', ':')))

notions = set()
for ch in out['chapitres']:
    for e in ch['e']:
        notions |= {n for n in e['no']}
auteurs = {e['n'] for ch in out['chapitres'] for e in ch['e']}
sans_ouvrage = sum(1 for ch in out['chapitres'] for e in ch['e'] if not e['ou'])

print('OK atlas.json')
print('  %d idées (couples auteur x chapitre) sur %d chapitres' % (total, len(ORDRE)))
print('  %d auteurs distincts, %d notions distinctes, %d liens' % (len(auteurs), len(notions), liens_total))
print('  %d entrées sans ouvrage cité (aucune référence inventée)' % sans_ouvrage)
for ch in out['chapitres']:
    print('   %-26s %2d idées' % (ch['lib'], len(ch['e'])))
car = sum(len(e['af']) + len(e['me']) + len(e['ex']) + len(e['di']) for ch in out['chapitres'] for e in ch['e'])
print('  %d caractères d\'explication rédigée (%d en moyenne par idée)' % (car, car // total))
