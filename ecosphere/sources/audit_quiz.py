# -*- coding: utf-8 -*-
"""Rattache chaque question existante au passage du cours qui la justifie, puis
mesure la couverture des sous-parties.

Le rattachement se fait par recouvrement de vocabulaire entre l'énoncé (avec sa
bonne réponse) et chaque bloc du chapitre, les mots rares pesant davantage que
les mots courants. Le bloc retenu est celui qui obtient le meilleur score ; en
dessous d'un seuil, la question est signalée comme non localisée, ce qui est
le symptôme d'un énoncé flou ou d'un contenu absent du cours.
"""

import json
import math
import re
import unicodedata
from collections import Counter, defaultdict

VIDE = set("""le la les un une des du de d a à au aux et ou en dans sur pour par
avec sans sous entre vers chez est sont etre être avoir ont a ete été cette ce
ces cet son sa ses leur leurs il elle ils elles on nous vous que qui quoi dont
ou où quand comment pourquoi quel quelle quels quelles plus moins tres très
peut peuvent doit doivent fait font selon lors ainsi donc mais car si ne pas
non oui tout tous toute toutes meme même autre autres entre lorsque quelle
quels entre afin alors apres après avant deja déjà encore aussi bien y
laquelle lequel lesquels celui celle ceux celles cela ca ça leur leurs
notamment entre dune dun lun lune cest nest sest quil quelle""".split())


def nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = re.sub(r"[^a-z0-9' ]", ' ', s.replace('’', "'"))
    return re.sub(r'\s+', ' ', s).strip()


def mots(s):
    out = []
    for w in nz(s).replace("'", ' ').split():
        if len(w) < 4 or w in VIDE:
            continue
        if len(w) > 5 and w.endswith('s') and not w.endswith('ss'):
            w = w[:-1]
        out.append(w)
    return out


def index(blocs):
    """Sacs de mots des blocs, et poids inverse de fréquence."""
    sacs = [Counter(mots(x['x'])) for x in blocs]
    df = Counter()
    for s in sacs:
        df.update(s.keys())
    n = max(1, len(sacs))
    idf = {w: math.log(1 + n / (1 + c)) for w, c in df.items()}
    return sacs, idf


def localiser(sacs, idf, texte, mini=3.0):
    """Bloc du chapitre qui recouvre le mieux le texte, et son score."""
    q = Counter(mots(texte))
    if not q:
        return -1, 0.0
    best, bs = -1, 0.0
    for i, s in enumerate(sacs):
        if not s:
            continue
        sc = 0.0
        for w, c in q.items():
            if w in s:
                sc += idf.get(w, 1.0) * min(c, 2)
        # on privilégie les blocs substantiels : un titre de trois mots qui
        # recouvre deux mots n'est pas une justification
        sc *= 1.0 + min(len(s), 60) / 300.0
        if sc > bs:
            best, bs = i, sc
    return (best, bs) if bs >= mini else (-1, bs)


def texte_question(q):
    t = [q.get('q') or '']
    opts = q.get('opts') or []
    a = q.get('ans')
    if opts and isinstance(a, int) and 0 <= a < len(opts):
        t.append(opts[a])
    t.append((q.get('exp') or '')[:400])
    return ' '.join(t)


def main():
    B = json.load(open('blocs_bruts.json', encoding='utf-8'))
    SP = json.load(open('sousparties.json', encoding='utf-8'))
    QA = json.load(open('quiz_actuel.json', encoding='utf-8'))['bank']

    res = {}
    print('%-5s %5s %8s %9s %9s %9s' % ('ch', 'n', 'localis.', 'sp vides',
                                        'sp<3', 'médiane/sp'))
    for k in sorted(QA, key=lambda x: int(x)):
        blocs = B[k]
        sacs, idf = index(blocs)
        parsp = defaultdict(list)
        hors = []
        detail = []
        for q in QA[k]:
            b, sc = localiser(sacs, idf, texte_question(q))
            cle = ''
            if b >= 0:
                for s in SP[k]:
                    if s['a'] <= b < s['b']:
                        cle = s['cle']
                        break
                parsp[cle].append(q['id'])
            else:
                hors.append(q['id'])
            detail.append({'id': q['id'], 'b': b, 'sc': round(sc, 1), 'sp': cle})
        vides = [s['cle'] for s in SP[k] if not parsp.get(s['cle'])]
        maigres = [s['cle'] for s in SP[k] if 0 < len(parsp.get(s['cle'], [])) < 3]
        tailles = sorted(len(parsp.get(s['cle'], [])) for s in SP[k])
        med = tailles[len(tailles) // 2] if tailles else 0
        print('%-5s %5d %8d %9d %9d %9d'
              % (k, len(QA[k]), len(QA[k]) - len(hors), len(vides), len(maigres), med))
        res[k] = {'detail': detail, 'hors': hors, 'vides': vides,
                  'maigres': maigres,
                  'parsp': {c: v for c, v in parsp.items()}}
    json.dump(res, open('audit_quiz.json', 'w', encoding='utf-8'),
              ensure_ascii=False)
    tot = sum(len(v['hors']) for v in res.values())
    print('questions non localisées : %d' % tot)
    print('sous-parties sans question : %d'
          % sum(len(v['vides']) for v in res.values()))


if __name__ == '__main__':
    main()
