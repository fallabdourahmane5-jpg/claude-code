#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Affiche le contexte complet des mentions d'un patronyme dans les cours."""
import io, json, re, sys
cours = json.load(io.open('cours.json', encoding='utf-8'))
noms = sys.argv[1:]
W = int(noms.pop(0)) if noms and noms[0].isdigit() else 900
for nom in noms:
    pat = re.compile(r'\b' + re.escape(nom), re.I)
    print('\n' + '#' * 76)
    print('### ' + nom)
    print('#' * 76)
    for ch, txt in cours.items():
        pos = [m.start() for m in pat.finditer(txt)]
        if not pos:
            continue
        # fusionner les positions proches
        blocs = []
        for p in pos:
            if blocs and p - blocs[-1][1] < W:
                blocs[-1][1] = p
            else:
                blocs.append([p, p])
        print('\n--- ch%s (%d mentions, %d blocs)' % (ch, len(pos), len(blocs)))
        for a, b in blocs:
            s = re.sub(r'[ \t]+', ' ', txt[max(0, a - 400):b + W])
            print('   …' + s.replace('\n', ' ⏎ ') + '…\n')
