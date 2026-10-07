# -*- coding: utf-8 -*-
"""Extrait les phrases contenant des donnees chiffrees, chapitre par chapitre.

Separe les statistiques (pourcentages, montants, volumes, ratios) des simples
mentions d'annees, afin de pouvoir privilegier les premieres.
"""
import io, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
CHAPS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '21', '22', '23']

# un chiffre « statistique » : pourcentage, montant, volume, multiple, ratio
RE_STAT = re.compile(
    r'(\d[\d   ]*[,.]?\d*\s*(?:%|points?\s+de\s+(?:PIB|pourcentage)|'
    r'milliards?|millions?|milliers?|Md|M€|€|dollars?|\$|tonnes?|MtCO|habitants?|'
    r'fois|heures?|ans\b|années\b|emplois?|personnes?))'
    r'|(?:taux|part|ratio|indice|écart|PIB|dette|déficit|solde|chômage|inflation|'
    r'croissance|productivité|salaire|revenu|population|export|import|balance)'
    r'[^.;:]{0,80}?\d[\d   ]*[,.]?\d*\s*%',
    re.I)
RE_ANNEE_SEULE = re.compile(r'^\D*\b(1[5-9]\d\d|20\d\d)\b\D*$')
RE_NUM = re.compile(r'\d')


def phrases(txt):
    # le cours est fortement segmente : on travaille ligne a ligne puis phrase a phrase
    out = []
    for ligne in txt.split('\n'):
        ligne = ligne.strip()
        if not ligne:
            continue
        for ph in re.split(r'(?<=[.;])\s+', ligne):
            ph = ph.strip('  ')
            if 8 < len(ph) < 400:
                out.append(ph)
    return out


def classer(ch):
    txt = io.open(os.path.join(ICI, 'ch_txt_%s.txt' % ch), encoding='utf-8').read()
    corps, _, notions = txt.partition('=== NOTIONS ===')
    stats, autres = [], []
    vus = set()
    for ph in phrases(corps) + phrases(notions):
        if not RE_NUM.search(ph):
            continue
        cle = re.sub(r'\s+', ' ', ph.lower())[:90]
        if cle in vus:
            continue
        vus.add(cle)
        if RE_STAT.search(ph):
            stats.append(ph)
        elif not RE_ANNEE_SEULE.match(ph):
            autres.append(ph)
    return stats, autres


if __name__ == '__main__':
    total = 0
    for ch in CHAPS:
        stats, autres = classer(ch)
        total += len(stats)
        io.open(os.path.join(ICI, 'cand_%s.txt' % ch), 'w', encoding='utf-8').write(
            '### STATISTIQUES (%d)\n' % len(stats) + '\n'.join(stats)
            + '\n\n### AUTRES MENTIONS CHIFFRÉES (%d)\n' % len(autres) + '\n'.join(autres))
        print('ch%-3s %4d statistiques · %4d autres' % (ch, len(stats), len(autres)))
    print('total statistiques :', total)
