# -*- coding: utf-8 -*-
"""Extrait d'un chapitre le texte compris entre deux intitulés."""
import re, sys, socle

def bloc(ch, debut, fin=None):
    t = socle.TXT[str(ch)]
    i = t.find(debut)
    if i < 0:
        return '!! introuvable : ' + debut
    j = t.find(fin, i + len(debut)) if fin else -1
    return t[i:j if j > 0 else i + 4000]

if __name__ == '__main__':
    print(bloc(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None))
