# -*- coding: utf-8 -*-
"""Découpage de chaque chapitre en sous-parties exploitables par le quiz.

Les cours n'ont pas tous la même granularité : certains chapitres comptent
quatre grandes parties et beaucoup de sous-titres, d'autres soixante parties
courtes. On construit donc un découpage homogène : les grandes parties (h2)
forment des frontières infranchissables, et une partie trop longue est
redécoupée sur ses sous-titres (h3) en tranches de taille comparable.

Chaque sous-partie porte une clé stable, un libellé, la partie dont elle
relève et l'intervalle de blocs du cours qu'elle couvre.
"""

import json
import re
import unicodedata

CIBLE = 200      # taille visée d'une sous-partie, en blocs
SEUIL = 270      # au-delà, une partie est redécoupée sur ses sous-titres
MINI = 45        # en deçà, une sous-partie est absorbée par sa voisine
MAX_SP = 18      # nombre maximal de sous-parties par chapitre

MARQUE = re.compile(r'^\s*(?:[IVXLC]{1,6}\.|[A-Z]{1,2}\.|\d{1,3}\s*[-.)])\s*')


def propre(t):
    return MARQUE.sub('', ' '.join(str(t or '').split())).strip(' :·—–-’\'"')


def nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = re.sub(r"[^a-z0-9 ]", ' ', s.replace('’', "'"))
    return re.sub(r'\s+', ' ', s).strip()


BRUIT = re.compile(r"^(idee|idees|pourquoi|comment|exemple|exemples|lecture|cl|bilan|"
                   r"remarque|attention|synthese|conclusion|rappel|transition|"
                   r"definition|mecanisme|schema|graphique|tableau|resume|"
                   r"precision|nuance|application|illustration|cas|questions?|"
                   r"probleme|idee cle|idee essentielle|a retenir|point|plan|"
                   r"premier|deuxieme|troisieme|quatrieme|enfin|donc|mais|or)\b")


def intitule(blocs, a, b):
    """Le sous-titre le plus informatif d'un intervalle : celui qui nomme une
    notion, et non une étape du discours (« Idée », « Pourquoi ? », « Lecture »)."""
    cand = []
    for i in range(a, b):
        x = blocs[i]
        if x['g'] not in ('h3', 'h4'):
            continue
        t = propre(x['x'])
        n = nz(t)
        if len(t) < 18 or len(t) > 110 or BRUIT.match(n) or t.endswith('?'):
            continue
        # les premiers sous-titres de l'intervalle sont les plus représentatifs
        cand.append((abs(i - a), -min(len(t), 70), t))
    if not cand:
        return ''
    cand.sort()
    return cand[0][2]


def decouper(blocs):
    """Retourne la liste des sous-parties d'un chapitre."""
    n = len(blocs)
    h2 = [i for i, x in enumerate(blocs) if x['g'] == 'h2']
    if not h2 or h2[0] != 0:
        h2 = [0] + h2
    bornes = h2 + [n]
    parties = []
    for a, b in zip(bornes[:-1], bornes[1:]):
        titre = propre(blocs[a]['x']) if blocs[a]['g'] == 'h2' else 'Ouverture'
        parties.append((a, b, titre))

    sp = []
    for a, b, titre in parties:
        taille = b - a
        if taille <= SEUIL:
            sp.append((a, b, titre, ''))
            continue
        # redécoupage sur les sous-titres
        h3 = [i for i in range(a, b) if blocs[i]['g'] in ('h3', 'h4')]
        morceaux = max(2, round(taille / CIBLE))
        pas = taille / morceaux
        coupes = [a]
        for m in range(1, morceaux):
            vise = a + pas * m
            cand = [i for i in h3 if i > coupes[-1] + 40]
            if not cand:
                break
            coupes.append(min(cand, key=lambda i: abs(i - vise)))
        coupes.append(b)
        for x, y in zip(coupes[:-1], coupes[1:]):
            if y - x < 30 and sp and sp[-1][2] == titre:
                sp[-1] = (sp[-1][0], y, titre, sp[-1][3])
                continue
            sous = propre(blocs[x]['x']) if blocs[x]['g'] in ('h2', 'h3', 'h4') else ''
            sp.append((x, y, titre, sous))
    return sp


def fusionner(sp, maxi=MAX_SP):
    """Un chapitre taillé en cinquante petites parties ne donne pas un filtre
    utilisable : on fusionne les segments voisins les plus courts jusqu'à
    obtenir un nombre de sous-parties lisible."""
    seg = [{'a': a, 'b': b, 'deb': (titre if not sous else titre), 'fin': sous or titre}
           for a, b, titre, sous in sp]
    while len(seg) > 1 and (len(seg) > maxi or
                            min(x['b'] - x['a'] for x in seg) < MINI):
        i = min(range(len(seg) - 1),
                key=lambda j: (seg[j]['b'] - seg[j]['a']) + (seg[j + 1]['b'] - seg[j + 1]['a']))
        g, d = seg[i], seg[i + 1]
        seg[i:i + 2] = [{'a': g['a'], 'b': d['b'], 'deb': g['deb'], 'fin': d['fin']}]
    return seg


def construire(chemin='blocs_bruts.json'):
    B = json.load(open(chemin, encoding='utf-8'))
    out = {}
    for k in sorted(B, key=lambda x: int(x)):
        liste = fusionner(decouper(B[k]))
        blocs = B[k]
        assert len(liste) <= MAX_SP, (k, len(liste))
        out[k] = []
        for rang, s in enumerate(liste, 1):
            titre = intitule(blocs, s['a'], s['b']) or s['deb']
            out[k].append({
                'cle': 'c%s-%02d' % (k, rang),
                'lib': titre[:110],
                'partie': s['deb'][:80],
                'a': s['a'], 'b': s['b'],
            })
    return out


if __name__ == '__main__':
    SP = construire()
    json.dump(SP, open('sousparties.json', 'w', encoding='utf-8'),
              ensure_ascii=False)
    for k, v in SP.items():
        print('ch%-3s %2d sous-parties, de %4d à %4d blocs'
              % (k, len(v), min(x['b'] - x['a'] for x in v),
                 max(x['b'] - x['a'] for x in v)))
    print('total', sum(len(v) for v in SP.values()), 'sous-parties')
