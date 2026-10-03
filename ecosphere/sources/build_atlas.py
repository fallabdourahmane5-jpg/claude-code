#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble l'Atlas des idées : base rédigée + couche d'approfondissement,
vérifie la couverture et produit atlas.json."""
import io, json, unicodedata, sys

from atlas_a import A
from atlas_b import B
from atlas_c import C
from atlas_d import D
from atlas_e import E

import enr_ch1, enr_ch2, enr_ch3, enr_ch45, enr_ch6, enr_ch7, enr_ch8, enr_ch910, enr_ch2122, enr_meca, enr_meca2, enr_v194, enr_meca2
import enr_v195a, enr_v195b, enr_v195c, enr_v195d
import enr_v196a, enr_v196b, enr_v196c

ATLAS = {}
for src in (A, B, C, D, E):
    ATLAS.update(src)

# les modules sont appliqués dans l'ordre : une surcharge peut viser un titre
# produit par un module antérieur, ou une entrée ajoutée par lui
MODULES = (enr_meca, enr_meca2, enr_ch1, enr_ch2, enr_ch3, enr_ch45, enr_ch6,
           enr_ch7, enr_ch8, enr_ch910, enr_ch2122, enr_v194,
           enr_v195a, enr_v195b, enr_v195c, enr_v195d,
           enr_v196a, enr_v196b, enr_v196c)
# modules de l'audit des auteurs : leurs auteurs ne sont pas dans data.json
# (ils sont ajoutés à la base AUTHORS de l'application par patch_v195.py)
AUDIT = (enr_v195a, enr_v195b, enr_v195c, enr_v195d, enr_v196a, enr_v196b, enr_v196c)
SPLIT = {}
for m in MODULES:
    for k, v in getattr(m, 'SPLIT', {}).items():
        SPLIT.setdefault(k, []).extend(v)

ORDRE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 22]

ALIAS = {
    'walt rostow': 'Walt Whitman Rostow',
    'james robinson': 'James A. Robinson',
    'frank galluzzo': 'Anthony Galluzzo',
}
HORS_AUTHORS = {22: ['Ronald Coase', 'Richard Baldwin', 'Charles-Albert Michalet', 'Paul Krugman'],
                3: ['John Maynard Keynes']}
for _m in AUDIT:
    for _c, _lst in getattr(_m, 'SPLIT', {}).items():
        HORS_AUTHORS.setdefault(_c, []).extend(n for (n, _t, _d) in _lst)


def norm(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return ' '.join(s.replace('.', ' ').split())


def cle(nom):
    return norm(ALIAS.get(norm(nom), nom))


data = json.load(io.open('data.json', encoding='utf-8'))
AUT = data['AUTHORS']
CHAP = data['chapitres']


def chapitres_de(a):
    src = a.get('chapters') or ([a.get('ch')] if a.get('ch') is not None else [])
    return sorted({c for c in src if c is not None})


meta = {}
for a in AUT:
    k = cle(a['name'])
    cur = meta.setdefault(k, {'name': a['name'], 'dates': '', 'courant': '', 'poids': -1})
    if a.get('dates') and len(a['dates']) > len(cur['dates']):
        cur['dates'] = a['dates']
    if a.get('courant') and len(a['courant']) > len(cur['courant']):
        cur['courant'] = a['courant']
    poids = len(a.get('detail') or '') + len(a.get('idea') or '')
    if poids > cur['poids']:
        cur['poids'] = poids
        cur['name'] = a['name']

# ---------------------------------------------------------------- couverture
attendu = {c: set() for c in ORDRE}
for a in AUT:
    for c in chapitres_de(a):
        if c in attendu:
            attendu[c].add(cle(a['name']))
for c, noms in HORS_AUTHORS.items():
    for n in noms:
        attendu[c].add(cle(n))

ecrit = {c: ({cle(e[0]) for e in ATLAS.get(c, [])} | {cle(e[0]) for e in SPLIT.get(c, [])}) for c in ORDRE}
erreurs = []
for c in ORDRE:
    if attendu[c] - ecrit[c]:
        erreurs.append('ch%s MANQUE : %s' % (c, ', '.join(sorted(attendu[c] - ecrit[c]))))
    if ecrit[c] - attendu[c]:
        erreurs.append('ch%s EN TROP : %s' % (c, ', '.join(sorted(ecrit[c] - attendu[c]))))
if erreurs:
    sys.exit('\n'.join(erreurs))

# ---------------------------------------------------------------- fusion
CHAMPS = {'ti': 'ti', 'af': 'affirme', 'me': 'mecanisme', 'ex': 'exemple',
          'di': 'diss', 'po': 'portee', 'co': 'copie', 'no': 'notions'}

enrichies = 0
for m in MODULES:
    for c, ajouts in getattr(m, 'SPLIT', {}).items():
        ATLAS[c] = list(ATLAS.get(c, [])) + list(ajouts)
    for c, surcharges in getattr(m, 'ENR', {}).items():
        base = ATLAS[c]
        titres = {t for (_, t, _) in base}
        inconnus = set(surcharges) - titres
        if inconnus:
            sys.exit('%s / ch%s : surcharge sans cible : %s'
                     % (m.__name__, c, ', '.join(sorted(inconnus))))
        neuf = []
        for nom, titre, d in base:
            sur = surcharges.get(titre)
            if sur:
                enrichies += 1
                d = dict(d)
                titre = sur.get('ti', titre)
                for k, champ in CHAMPS.items():
                    if k == 'ti':
                        continue
                    if k in sur:
                        d[champ] = sur[k]
            neuf.append((nom, titre, d))
        ATLAS[c] = neuf

# ---------------------------------------------------------------- contrôles
MINI = {'affirme': 600, 'mecanisme': 400, 'exemple': 110, 'diss': 140, 'portee': 250, 'copie': 150}

noms_connus = set()
for c in ORDRE:
    noms_connus |= {cle(e[0]) for e in ATLAS[c]}

for c in ORDRE:
    vus = set()
    for nom, titre, d in ATLAS[c]:
        if titre in vus:
            sys.exit('ch%s : titre en double : %s' % (c, titre))
        vus.add(titre)
        for champ, mini in MINI.items():
            v = (d.get(champ) or '').strip()
            if not v:
                sys.exit('ch%s / %s : champ %s absent' % (c, nom, champ))
            if len(v) < mini:
                sys.exit('ch%s / %s : champ %s trop court (%d < %d)' % (c, nom, champ, len(v), mini))
        for ln in d.get('liens') or []:
            if cle(ln[0]) not in noms_connus:
                sys.exit('ch%s / %s : lien vers un auteur absent : %s' % (c, nom, ln[0]))
            if ln[1] not in ('complement', 'opposition', 'prolonge'):
                sys.exit('ch%s / %s : relation inconnue %r' % (c, nom, ln[1]))


def libelle(c):
    if c == 21:
        return '2ᵉ année — Chapitre 1'
    if c == 22:
        return '2ᵉ année — Chapitre 2'
    return 'Chapitre %d' % c


out = {'chapitres': []}
total = liens_total = 0
for c in ORDRE:
    info = CHAP[str(c)]
    entrees = []
    for nom, titre, d in ATLAS[c]:
        m = meta.get(cle(nom), {})
        liens = [{'a': a, 'r': r, 't': t} for (a, r, t) in (d.get('liens') or [])]
        liens_total += len(liens)
        entrees.append({
            'n': m.get('name') or nom, 'd': m.get('dates') or '', 'c': m.get('courant') or '',
            'ti': titre, 'af': d['affirme'], 'me': d['mecanisme'], 'ex': d['exemple'],
            'po': d['portee'], 'di': d['diss'], 'co': d['copie'],
            'ou': (d.get('ouvrage') or '').strip(), 'no': d.get('notions') or [],
            'li': liens, 'ch': c,
        })
        total += 1
    out['chapitres'].append({'k': c, 'annee': 2 if c >= 21 else 1, 'lib': libelle(c),
                             'titre': info.get('title') or '', 'sous': info.get('sub') or '',
                             'e': entrees})

io.open('atlas.json', 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, separators=(',', ':')))

auteurs = {e['n'] for ch in out['chapitres'] for e in ch['e']}
multi = sum(1 for ch in out['chapitres'] for e in ch['e']
            if sum(1 for ch2 in out['chapitres'] for e2 in ch2['e']
                   if e2['ch'] == e['ch'] and cle(e2['n']) == cle(e['n'])) > 1)
sans_ouvrage = sum(1 for ch in out['chapitres'] for e in ch['e'] if not e['ou'])
car = sum(len(e['af']) + len(e['me']) + len(e['ex']) + len(e['po']) + len(e['di']) + len(e['co'])
          for ch in out['chapitres'] for e in ch['e'])
caf = sum(len(e['af']) for ch in out['chapitres'] for e in ch['e'])

print('OK atlas.json')
print('  %d idées · %d auteurs distincts · %d liens' % (total, len(auteurs), liens_total))
print('  %d entrées enrichies, %d idées supplémentaires issues de séparations' % (enrichies, sum(len(v) for v in SPLIT.values())))
print('  %d idées appartiennent à un auteur traité plusieurs fois dans le même chapitre' % multi)
print('  %d entrées sans ouvrage cité (aucune référence inventée)' % sans_ouvrage)
print('  %d caractères rédigés (%d par idée), dont %d pour « la thèse » (%d par idée)'
      % (car, car // total, caf, caf // total))
for ch in out['chapitres']:
    print('   %-26s %2d idées' % (ch['lib'], len(ch['e'])))
