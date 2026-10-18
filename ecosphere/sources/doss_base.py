# -*- coding: utf-8 -*-
"""Schéma commun des dossiers de la section « Autour d'une notion ».

Un dossier réunit, pour une notion du programme :
  defi   définition claire
  expl   explication détaillée du raisonnement
  mec    mécanismes, étape par étape : (titre, explication)
  args   arguments en faveur : {a : l'argument, cond : conditions de validité,
         lim : limites}
  crit   critiques, oppositions, débats : {t : la thèse adverse, qui : qui la
         porte lorsque le cours le précise, rep : ce qu'on peut répondre}
  aut    auteurs : {n : nom, i : l'idée précise, p : la précision ou l'apport}
         — un même auteur peut revenir plusieurs fois
  faits  faits, exemples et chiffres : {f : le fait, p : ce qu'il démontre}
  comp   comparaison éventuelle : {titre, lignes : [(critère, A, B)], a, b}
  diss   mobilisations en dissertation : {q : le type de sujet, f : la
         formulation rédigée, r : le raisonnement, ex : l'exemple qui l'appuie}
  voisins clés des dossiers liés (vérifiées au montage)

Les liens vers les chapitres, fiches, idées de l'Atlas et sujets ne sont pas
écrits à la main : ils sont calculés par liens.py à partir des contenus
réellement présents dans l'application.
"""

DOSSIERS = []


def d(cle, ens, titre, court, defi, expl, mec, args, crit, aut, faits, diss,
      voisins=None, comp=None):
    DOSSIERS.append({
        'cle': cle, 'ens': ens, 'titre': titre, 'court': court,
        'defi': defi, 'expl': expl,
        'mec': [{'t': t, 'e': e} for (t, e) in mec],
        'args': args, 'crit': crit, 'aut': aut, 'faits': faits,
        'diss': diss, 'voisins': voisins or [], 'comp': comp,
    })
    return DOSSIERS[-1]


MINIMA = {'defi': 180, 'expl': 900}
MINI_LISTES = {'mec': 3, 'args': 3, 'crit': 2, 'aut': 2, 'faits': 2, 'diss': 2}


def controler(liste):
    """Vérifie que chaque dossier atteint le niveau de détail attendu."""
    pb = []
    vus = set()
    for x in liste:
        if x['cle'] in vus:
            pb.append('%s : clé en double' % x['cle'])
        vus.add(x['cle'])
        for champ, n in MINIMA.items():
            if len(x[champ]) < n:
                pb.append('%s : %s trop court (%d < %d)'
                          % (x['cle'], champ, len(x[champ]), n))
        for champ, n in MINI_LISTES.items():
            if len(x[champ]) < n:
                pb.append('%s : %s insuffisant (%d < %d)'
                          % (x['cle'], champ, len(x[champ]), n))
        for m in x['mec']:
            if len(m['e']) < 120:
                pb.append('%s : mécanisme trop court « %s »' % (x['cle'], m['t'][:40]))
        for a in x['args']:
            for c in ('a', 'cond', 'lim'):
                if len(a.get(c, '')) < 90:
                    pb.append('%s : argument %s trop court' % (x['cle'], c))
        for c in x['crit']:
            for k in ('t', 'rep'):
                if len(c.get(k, '')) < 85:
                    pb.append('%s : critique %s trop courte' % (x['cle'], k))
        for a in x['aut']:
            if len(a.get('i', '')) < 60 or len(a.get('p', '')) < 120:
                pb.append('%s : auteur %s trop court' % (x['cle'], a.get('n')))
        for f in x['faits']:
            if len(f.get('f', '')) < 60 or len(f.get('p', '')) < 90:
                pb.append('%s : fait trop court' % x['cle'])
        for s in x['diss']:
            for k, n in (('q', 20), ('f', 200), ('r', 120), ('ex', 60)):
                if len(s.get(k, '')) < n:
                    pb.append('%s : formulation %s trop courte' % (x['cle'], k))
    return pb


def signes(x):
    n = len(x['defi']) + len(x['expl'])
    n += sum(len(m['t']) + len(m['e']) for m in x['mec'])
    n += sum(len(a['a']) + len(a['cond']) + len(a['lim']) for a in x['args'])
    n += sum(len(c['t']) + len(c['rep']) for c in x['crit'])
    n += sum(len(a['i']) + len(a['p']) for a in x['aut'])
    n += sum(len(f['f']) + len(f['p']) for f in x['faits'])
    n += sum(len(s['f']) + len(s['r']) + len(s['ex']) for s in x['diss'])
    if x['comp']:
        n += sum(len(a) + len(b) + len(c) for (a, b, c) in x['comp']['lignes'])
    return n
