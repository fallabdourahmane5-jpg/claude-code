# -*- coding: utf-8 -*-
"""Relève les notions que les cours traitent sans qu'ÉcoSphère les définisse.

Une notion est « traitée » lorsqu'elle nomme un bloc de définition du cours,
une notion de la fiche du chapitre, un intitulé de section, ou un libellé de
la liste des 28 ensembles d'« Autour d'une notion ». Elle est « définie »
lorsqu'une définition autonome existe quelque part dans l'application.
"""
import json
import re
from collections import Counter

import notions_liste
import rech_base as R


def definitions_existantes():
    """cle -> (origine, terme, définition) pour tout ce qui définit déjà."""
    d = {}

    def ajoute(t, de, o, ch=None):
        c = R.cle(t)
        if not c or len(c) < 3:
            return
        d.setdefault(c, {'t': t, 'd': de, 'o': set(), 'ch': set()})
        d[c]['o'].add(o)
        if ch:
            d[c]['ch'].add(str(ch))
        if len(de) > len(d[c]['d']):
            d[c]['d'] = de

    B = R.blocs()
    for k in R.ORDRE:
        for x in B[k]:
            if x['g'] == 'db' and x['dt'] and x['dd']:
                ajoute(x['dt'].strip(' :·—-'), x['dd'], 'cours', k)
    C = R.corpus()
    for k in R.ORDRE:
        for n in C['chapitres'][k]['notions']:
            if n['t'] and n['d']:
                ajoute(n['t'], n['d'], 'fiche-chapitre', k)
    for x in R.autour()['dossiers']:
        if x['etat'] == 'redige':
            ajoute(x['titre'], x.get('defi') or '', 'dossier')
    for f in R.fiches():
        if f.get('term') and f.get('def') and f.get('type') in (
                'definition', 'définition', 'notion-clé', 'notion'):
            ajoute(f['term'], f['def'], 'fiche', f.get('ch'))
    return d


def notions_traitees():
    """cle -> ce que les cours en disent, et où."""
    t = {}

    def ajoute(terme, o, ch=None, extra=''):
        c = R.cle(terme)
        if not c or len(c) < 3:
            return
        t.setdefault(c, {'t': terme, 'o': set(), 'ch': set(), 'ex': []})
        t[c]['o'].add(o)
        if ch:
            t[c]['ch'].add(str(ch))
        if extra:
            t[c]['ex'].append(extra)
        if len(terme) < len(t[c]['t']):
            t[c]['t'] = terme

    B = R.blocs()
    for k in R.ORDRE:
        for x in B[k]:
            if x['g'] == 'db' and x['dt']:
                ajoute(x['dt'].strip(' :·—-'), 'cours-db', k)
            elif x['g'] in ('h2', 'h3', 'h4'):
                nom = R.titre_propre(x['x'])
                if R.est_notion(nom):
                    ajoute(nom, 'intitule', k)
    C = R.corpus()
    for k in R.ORDRE:
        for n in C['chapitres'][k]['notions']:
            if n['t']:
                ajoute(n['t'], 'fiche-chapitre', k)
    for e in notions_liste.ENSEMBLES:
        for lb in e['dossiers']:
            ajoute(lb, 'programme')
    return t


def ou_dans_les_cours(c, index_texte):
    """Chapitres dont le texte contient l'expression, avec le nombre d'occurrences."""
    return {k: n for k, n in index_texte.get(c, {}).items() if n}


if __name__ == '__main__':
    DEF = definitions_existantes()
    TRA = notions_traitees()
    print('définitions autonomes déjà présentes : %d' % len(DEF))
    print('  par origine :', Counter(o for v in DEF.values()
                                     for o in v['o']).most_common())
    print('notions traitées par les cours        : %d' % len(TRA))
    print('  par origine :', Counter(o for v in TRA.values()
                                     for o in v['o']).most_common())

    # présence réelle dans le texte des cours
    import socle
    TXT = {k: R.nz(socle.TXT[k]) for k in R.ORDRE}
    manque = {}
    for c, v in TRA.items():
        if c in DEF:
            continue
        # on ne retient que ce que le texte des cours porte vraiment
        occ = {}
        expr = R.nz(v['t'])
        for k in R.ORDRE:
            n = TXT[k].count(expr)
            if n:
                occ[k] = n
        if not occ:
            continue
        manque[c] = {'t': v['t'], 'o': sorted(v['o']), 'occ': occ,
                     'total': sum(occ.values())}
    print()
    print('notions traitées mais non définies    : %d' % len(manque))
    json.dump(manque, open('manques.json', 'w'), ensure_ascii=False)

    print()
    print('les 70 plus présentes dans les cours :')
    for c, v in sorted(manque.items(), key=lambda t: -t[1]['total'])[:70]:
        print('  %-50s %3d occ.  ch %s  [%s]'
              % (v['t'][:50], v['total'],
                 ','.join(sorted(v['occ'], key=R.ORDRE.index)),
                 ','.join(v['o'])))
