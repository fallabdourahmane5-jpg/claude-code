# -*- coding: utf-8 -*-
"""Confronte l'inventaire des cours à ce que l'ancienne recherche trouvait.

Le résultat est la liste, chapitre par chapitre, des expressions que les cours
définissent ou traitent explicitement et que l'ancien index ne permettait pas
d'atteindre.
"""
import json
import re
import unicodedata
from collections import Counter

ORDRE = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
         '21', '22', '23', '24']
LIB = {'21': '2ᵉ année — ch.1', '22': '2ᵉ année — ch.2',
       '23': '2ᵉ année — ch.3', '24': '2ᵉ année — ch.4'}


def nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.replace('’', "'").replace('‘', "'")
    return re.sub(r'\s+', ' ', re.sub(r"[^a-z0-9' ]+", ' ', s)).strip()


def sing(w):
    """Forme sans marque de pluriel usuelle."""
    if len(w) > 4 and w.endswith('aux'):
        return w[:-3] + 'al'
    if len(w) > 3 and w.endswith(('s', 'x')) and not w.endswith('ss'):
        return w[:-1]
    return w


def cle(s):
    return ' '.join(sing(w) for w in nz(s).split())


MARQUE = re.compile(r'^\s*(?:[IVXLC]{1,6}\.|[A-Z]{1,2}\.|\d{1,2}[-.)])\s*')
BRUIT = re.compile(
    r'^(idee|idee cle|idee generale|idee centrale|exemple|schema|formule|'
    r'document|lecture|remarque|attention|conclusion|definition|resume|'
    r'mot cle a retenir|a retenir|synthese|rappel|cl|source|reference|'
    r'点|graphique)$')


def candidats():
    """Expressions que les cours traitent explicitement, par chapitre."""
    B = json.load(open('blocs_bruts.json'))
    C = json.load(open('corpus.json'))
    out = {}
    for k in ORDRE:
        d = {}
        # 1. les blocs de définition du cours : terme -> définition
        for x in B[k]:
            if x['g'] == 'db' and x['dt'] and x['dd']:
                t = x['dt'].strip(' :·—-')
                if 3 <= len(t) <= 80 and not BRUIT.match(nz(t)):
                    d.setdefault(cle(t), {'t': t, 'd': x['dd'], 'o': set()})
                    d[cle(t)]['o'].add('cours-db')
        # 2. les intitulés de section : ce que le chapitre traite
        for x in B[k]:
            if x['g'] in ('h2', 'h3'):
                t = MARQUE.sub('', x['x']).strip(' :·—-')
                if not (4 <= len(t) <= 90) or BRUIT.match(nz(t)):
                    continue
                if t.endswith('?') or len(nz(t).split()) > 9:
                    continue
                d.setdefault(cle(t), {'t': t, 'd': '', 'o': set()})
                d[cle(t)]['o'].add('intitule')
        # 3. les notions de la fiche du chapitre
        for n in C['chapitres'][k]['notions']:
            t = (n['t'] or '').strip()
            if 3 <= len(t) <= 80:
                d.setdefault(cle(t), {'t': t, 'd': n['d'], 'o': set()})
                d[cle(t)]['o'].add('fiche-notion')
        out[k] = d
    return out


def trouvables():
    """Clés que l'ancien index permettait d'atteindre par le terme."""
    A = json.load(open('search_index_ancien.json'))
    s = set()
    for x in A:
        t = x['n'] or ''
        # l'index contenait des libellés de quiz : on ne garde que le noyau
        t = re.sub(r'^(?:Définis|Que faut-il retenir de|Quel concept correspond '
                   r'à cette (?:définition|idée)|Quel auteur associer à l\'idée '
                   r'suivante)\s*:?\s*', '', t).strip(' ?:')
        if t:
            s.add(cle(t))
    return s


if __name__ == '__main__':
    CAND = candidats()
    TROUV = trouvables()
    print('expressions traitées par les cours : %d (dont %d distinctes)'
          % (sum(len(v) for v in CAND.values()),
             len({c for v in CAND.values() for c in v})))
    print('clés atteignables dans l’ancien index : %d' % len(TROUV))
    print()
    manque = {}
    print('%-16s %7s %7s %7s  %s' % ('chapitre', 'traité', 'trouvé', 'manque',
                                     'taux'))
    for k in ORDRE:
        d = CAND[k]
        mq = {c: v for c, v in d.items() if c not in TROUV}
        manque[k] = mq
        print('%-16s %7d %7d %7d  %4.0f %%'
              % (LIB.get(k, 'chapitre ' + k), len(d), len(d) - len(mq), len(mq),
                 100.0 * (len(d) - len(mq)) / max(1, len(d))))
    tot = sum(len(v) for v in CAND.values())
    tm = sum(len(v) for v in manque.values())
    print('%-16s %7d %7d %7d  %4.0f %%'
          % ('TOTAL', tot, tot - tm, tm, 100.0 * (tot - tm) / tot))
    print()
    print('origine des expressions introuvables :',
          Counter(o for v in manque.values() for x in v.values()
                  for o in x['o']).most_common())
    json.dump({k: {c: {'t': v['t'], 'd': v['d'], 'o': sorted(v['o'])}
                   for c, v in manque[k].items()} for k in ORDRE},
              open('ecart.json', 'w'), ensure_ascii=False)
    print()
    for k in ORDRE:
        mq = manque[k]
        avec_def = [v for v in mq.values() if v['d']]
        print('--- %s : %d introuvables, dont %d que le cours définit'
              % (LIB.get(k, 'chapitre ' + k), len(mq), len(avec_def)))
        for v in sorted(mq.values(), key=lambda z: -len(z['d']))[:8]:
            print('      %-52s %s' % (v['t'][:52], (v['d'] or '')[:70]))
