#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Relève, chapitre par chapitre et auteur par auteur, tout ce que les documents
disent réellement : titres de section, notions, phrases du cours. Sert à décider
quelles idées distinctes méritent une entrée propre dans l'Atlas."""
import io, json, re, sys, unicodedata

data = json.load(io.open('data.json', encoding='utf-8'))
atlas = json.load(io.open('atlas.json', encoding='utf-8'))


def nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    return ''.join(c for c in s if not unicodedata.combining(c))


def strip(h):
    h = re.sub(r'<[^>]+>', ' ', str(h or ''))
    h = (h.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&lt;', '<')
          .replace('&gt;', '>').replace('&#39;', "'").replace('&apos;', "'")
          .replace('&quot;', '"').replace('&eacute;', 'é'))
    return re.sub(r'\s+', ' ', h).strip()


cible = sys.argv[1:] or [str(c['k']) for c in atlas['chapitres']]

for ch in atlas['chapitres']:
    if str(ch['k']) not in cible:
        continue
    src = data['chapitres'][str(ch['k'])]
    cours = ''
    # le texte du cours n'est pas dans data.json : on reconstitue depuis le plan et les notions
    plan = [(n, strip(t)) for n, t in src['plan']]
    notions = [(strip(t), strip(d)) for t, d, _ in src['notions']]
    print('\n' + '=' * 78)
    print('CHAPITRE %s — %s' % (ch['lib'], src['title']))
    print('=' * 78)
    for e in ch['e']:
        nom = e['n']
        # motifs : nom complet, nom de famille
        parts = [p for p in re.split(r'\s+', nom) if len(p) > 3]
        pats = {nz(nom)} | {nz(p) for p in parts[-1:]}
        titres = [t for _, t in plan if any(p in nz(t) for p in pats)]
        nots = [(t, d) for t, d in notions if any(p in nz(t + ' ' + d) for p in pats)]
        if not titres and not nots:
            continue
        print('\n--- %s   [entrée actuelle : %s]' % (nom, e['ti']))
        for t in titres[:14]:
            print('    §  ' + t[:150])
        for t, d in nots[:10]:
            print('    N  %s : %s' % (t[:60], d[:170]))
