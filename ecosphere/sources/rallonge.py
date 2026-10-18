# -*- coding: utf-8 -*-
"""Remplace un texte logique dans un module de dossiers, quelle que soit la
façon dont la chaîne est coupée sur plusieurs lignes."""
import io, re, sys


def remplacer(chemin, paires):
    s = io.open(chemin, encoding='utf-8').read()
    for vieux, neuf in paires:
        motif = re.compile(r'(?:\s|"|\n)+'.join(re.escape(w) for w in vieux.split()))
        m = motif.search(s)
        if not m:
            raise SystemExit('introuvable : ' + vieux[:70])
        debut = s.rfind('\n', 0, m.start()) + 1
        indent = len(s[debut:]) - len(s[debut:].lstrip())
        # colonne de continuation : après « 'champ': " »
        tete = s[debut:m.start()]
        col = indent + max(0, len(tete.strip()) - 1)
        pref = ' ' * (debut + col - debut)
        lignes, cur = [], ''
        for mot in neuf.split():
            if len(cur) + len(mot) + 1 > 66:
                lignes.append(cur + ' ')
                cur = mot
            else:
                cur = (cur + ' ' + mot).strip()
        lignes.append(cur)
        bloc = ('"\n' + ' ' * col + '"').join(lignes)
        s = s[:m.start()] + bloc + s[m.end():]
    io.open(chemin, 'w', encoding='utf-8').write(s)
