#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Table d'audit : pour une liste de patronymes, occurrences par chapitre dans les
cours + présence dans AUTHORS et dans l'Atlas."""
import io, json, re, sys, unicodedata

cours = json.load(io.open('cours.json', encoding='utf-8'))
data = json.load(io.open('data.json', encoding='utf-8'))
atlas = json.load(io.open('atlas.json', encoding='utf-8'))


def nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    return ''.join(c for c in s if not unicodedata.combining(c))


NOMS = sys.stdin.read().split()
for n in NOMS:
    tot = {}
    for ch, t in cours.items():
        k = len(re.findall(r'\b' + n + r'\b', t, re.I))
        if k:
            tot[ch] = k
    q = nz(n)
    aut = sorted({a['name'] for a in data['AUTHORS'] if q in nz(a['name'])})
    atl = sorted({ch['k'] for ch in atlas['chapitres'] for e in ch['e'] if q in nz(e['n'])})
    etat = 'OK' if aut else ('—' if tot else 'absent des cours')
    print('%-16s cours: %-34s app: %-26s atlas: %s'
          % (n, ' '.join('ch%s:%d' % (a, b) for a, b in sorted(tot.items(), key=lambda x: -x[1]))[:34] or '0',
             (', '.join(aut))[:26] or '>>> MANQUE', atl or '—'))
