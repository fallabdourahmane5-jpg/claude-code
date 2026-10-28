# -*- coding: utf-8 -*-
"""Schéma des « Visualisations stratégiques ».

Une visualisation = un thème transversal, décomposé en nœuds explorables et
en liens explicités. Le placement n'est pas calculé ici : chaque nœud reçoit
un groupe (`grp`) et un rang (`ord`), et le moteur de rendu positionne les
nœuds après avoir mesuré leur taille réelle. Cela évite tout chevauchement,
quelle que soit la longueur des textes, et garde le texte net à tout zoom
puisqu'il reste du HTML et non une image.

Champs d'un nœud
  id      identifiant court, unique dans la visualisation
  t       titre affiché sur le nœud
  role    coeur | pilier | detail | limite | debat | fait | sortie
  r       résumé affiché sur le nœud (une à deux lignes)
  defi    définition développée, lue dans le panneau
  mec     mécanisme étape par étape : [(titre, explication)]
  args    arguments : [{a, lim}]
  opp     oppositions et débats : [{t, qui, rep}]
  aut     auteurs : [{n, i}] — n doit exister dans la base auteurs de l'app
  faits   faits, exemples et chiffres : [{f, p}]
  termes  expressions servant à calculer les liens réels vers les contenus
  dos     clés de dossiers « Autour d'une notion » (vérifiées au montage)
  grp     groupe de placement (colonne, niveau, bande… selon le type)
  par     nœud parent, pour les types radiaux

Champs d'un lien
  de, vers  identifiants de nœuds
  lab       étiquette courte affichée sur le lien
  expl      explication du lien, lue au clic
  t         cause | oppose | limite | renforce | mesure | conditionne
"""

VISUS = []

TYPES = {'hub', 'flux', 'duel', 'cycle', 'arbre', 'strates', 'courants'}
ROLES = {'coeur', 'pilier', 'detail', 'limite', 'debat', 'fait', 'sortie'}
TLIENS = {'cause', 'oppose', 'limite', 'renforce', 'mesure', 'conditionne'}


def nd(id, t, role, r, grp=0, par=None, defi=None, mec=None, args=None,
       opp=None, aut=None, faits=None, termes=None, dos=None):
    return {'id': id, 't': t, 'role': role, 'r': r, 'grp': grp, 'par': par,
            'defi': defi or '', 'mec': [{'t': a, 'e': b} for (a, b) in (mec or [])],
            'args': args or [], 'opp': opp or [], 'aut': aut or [],
            'faits': faits or [], 'termes': termes or [], 'dos': dos or []}


def ln(de, vers, lab, expl, t='cause'):
    return {'de': de, 'vers': vers, 'lab': lab, 'expl': expl, 't': t}


def v(cle, titre, kicker, type, resume, lecture, noeuds, liens, bandes=None,
      fam=None):
    x = {'cle': cle, 'titre': titre, 'kicker': kicker, 'type': type,
         'fam': fam or '', 'resume': resume, 'lecture': lecture,
         'noeuds': noeuds, 'liens': liens, 'bandes': bandes or []}
    VISUS.append(x)
    return x


# --------------------------------------------------------------- contrôles
MINI = {'resume': 150, 'r': 60, 'defi': 150}


def controler(liste, cles_dossiers=None, auteur_ok=None):
    """Vérifie la cohérence interne et le niveau de détail attendu."""
    pb = []
    vus = set()
    for x in liste:
        c = x['cle']
        if c in vus:
            pb.append('%s : clé de visualisation en double' % c)
        vus.add(c)
        if x['type'] not in TYPES:
            pb.append('%s : type inconnu « %s »' % (c, x['type']))
        if not x.get('fam'):
            pb.append('%s : famille manquante' % c)
        if len(x['resume']) < MINI['resume']:
            pb.append('%s : résumé trop court (%d)' % (c, len(x['resume'])))
        if len(x['lecture']) < 2:
            pb.append('%s : il faut au moins deux clés de lecture' % c)
        for a, b in x['lecture']:
            if len(b) < 70:
                pb.append('%s : clé de lecture « %s » trop courte' % (c, a[:30]))
        if len(x['noeuds']) < 8:
            pb.append('%s : seulement %d nœuds' % (c, len(x['noeuds'])))
        if len(x['liens']) < 6:
            pb.append('%s : seulement %d liens' % (c, len(x['liens'])))

        ids = [n['id'] for n in x['noeuds']]
        if len(set(ids)) != len(ids):
            pb.append('%s : identifiant de nœud en double' % c)
        coeurs = [n for n in x['noeuds'] if n['role'] == 'coeur']
        if x['type'] in ('hub', 'cycle', 'duel') and len(coeurs) != 1:
            pb.append('%s : %d nœud(s) cœur pour un type %s'
                      % (c, len(coeurs), x['type']))

        for n in x['noeuds']:
            q = '%s/%s' % (c, n['id'])
            if n['role'] not in ROLES:
                pb.append('%s : rôle inconnu « %s »' % (q, n['role']))
            if len(n['r']) < MINI['r']:
                pb.append('%s : résumé de nœud trop court (%d)' % (q, len(n['r'])))
            if len(n['r']) > 230:
                pb.append('%s : résumé de nœud trop long (%d)' % (q, len(n['r'])))
            if len(n['defi']) < MINI['defi']:
                pb.append('%s : définition trop courte (%d)' % (q, len(n['defi'])))
            fonds = len(n['mec']) + len(n['args']) + len(n['opp']) + len(n['faits'])
            if fonds < 3:
                pb.append('%s : contenu trop maigre (%d blocs)' % (q, fonds))
            for m in n['mec']:
                if len(m['e']) < 90:
                    pb.append('%s : étape « %s » trop courte' % (q, m['t'][:28]))
            for a in n['args']:
                if len(a.get('a', '')) < 90 or len(a.get('lim', '')) < 70:
                    pb.append('%s : argument ou limite trop court' % q)
            for o in n['opp']:
                if len(o.get('t', '')) < 70 or len(o.get('rep', '')) < 80:
                    pb.append('%s : opposition trop courte' % q)
            for a in n['aut']:
                if len(a.get('i', '')) < 60:
                    pb.append('%s : idée de %s trop courte' % (q, a.get('n')))
                if auteur_ok and not auteur_ok(a.get('n', '')):
                    pb.append('%s : auteur hors base « %s »' % (q, a.get('n')))
            for f in n['faits']:
                if len(f.get('f', '')) < 45 or len(f.get('p', '')) < 70:
                    pb.append('%s : fait trop court' % q)
            if not n['termes']:
                pb.append('%s : aucun terme pour calculer les liens' % q)
            if cles_dossiers is not None:
                for d in n['dos']:
                    if d not in cles_dossiers:
                        pb.append('%s : dossier inconnu « %s »' % (q, d))

        for l in x['liens']:
            q = '%s/%s→%s' % (c, l['de'], l['vers'])
            if l['de'] not in ids or l['vers'] not in ids:
                pb.append('%s : lien vers un nœud inexistant' % q)
            if l['t'] not in TLIENS:
                pb.append('%s : type de lien inconnu « %s »' % (q, l['t']))
            if len(l['lab']) < 3 or len(l['lab']) > 46:
                pb.append('%s : étiquette de lien inadaptée « %s »' % (q, l['lab']))
            if len(l['expl']) < 110:
                pb.append('%s : explication de lien trop courte (%d)'
                          % (q, len(l['expl'])))
        # tout nœud doit être relié, sauf le cœur d'un hub isolé
        relies = set()
        for l in x['liens']:
            relies.add(l['de'])
            relies.add(l['vers'])
        for n in x['noeuds']:
            if n['id'] not in relies:
                pb.append('%s/%s : nœud sans aucun lien' % (c, n['id']))
            if n['par'] and n['par'] not in ids:
                pb.append('%s/%s : parent inexistant' % (c, n['id']))
    return pb


def signes(x):
    n = len(x['resume']) + sum(len(a) + len(b) for a, b in x['lecture'])
    for d in x['noeuds']:
        n += len(d['t']) + len(d['r']) + len(d['defi'])
        n += sum(len(m['t']) + len(m['e']) for m in d['mec'])
        n += sum(len(a.get('a', '')) + len(a.get('lim', '')) for a in d['args'])
        n += sum(len(o.get('t', '')) + len(o.get('qui', '')) + len(o.get('rep', ''))
                 for o in d['opp'])
        n += sum(len(a.get('n', '')) + len(a.get('i', '')) for a in d['aut'])
        n += sum(len(f.get('f', '')) + len(f.get('p', '')) for f in d['faits'])
    n += sum(len(l['lab']) + len(l['expl']) for l in x['liens'])
    return n
