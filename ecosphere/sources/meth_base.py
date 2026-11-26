# -*- coding: utf-8 -*-
"""Socle de la grille d'autoévaluation et de l'exemple fil rouge.

Un critère porte un identifiant stable (« i2 », « d14 »…) qui sert à la fois
de clé dans la grille et de clé d'annotation dans les pièces rédigées. Une
annotation relie donc un critère à l'extrait exact qui le respecte.
"""

import json
import re
import sys

# ------------------------------------------------------------------ grille


def crit(i, t, ex=None, aide=None, na=False):
    """Un critère de la grille. ex = pièce de l'exemple où le voir."""
    c = {'id': i, 't': t}
    if ex:
        c['ex'] = ex
    if aide:
        c['aide'] = aide
    if na:
        c['na'] = 1
    return c


def groupe(t, items, intro=None):
    g = {'t': t, 'items': items}
    if intro:
        g['intro'] = intro
    return g


# ------------------------------------------------------- pièces rédigées


def para(txt, role=None, notes=None, isole=False):
    p = {'txt': txt}
    if role:
        p['r'] = role
    if notes:
        p['n'] = notes
    if isole:
        p['iso'] = 1
    return p


def note(k, e, x):
    """k = identifiant du critère, e = extrait exact, x = explication."""
    return {'k': k, 'e': e, 'x': x}


def glob(k, x):
    """Critère qui se juge sur la copie entière, pas sur un extrait."""
    return {'k': k, 'x': x}


def piece(**kw):
    for c in ('id', 't', 'st', 'paras'):
        if c not in kw:
            raise ValueError('champ manquant : %s dans %s' % (c, kw.get('id')))
    return kw


# ------------------------------------------------------------- contrôles


def nettoyer(txt):
    """Texte tel qu'il s'affiche : on retire le balisage de mise en forme."""
    return re.sub(r'\[\[[a-z]:(.*?)\]\]', r'\1', txt)


def verifier(grille, pieces, plan=None):
    e = []
    cles = {}
    for g in grille:
        for c in g['items']:
            if c['id'] in cles:
                e.append('critère en double : ' + c['id'])
            cles[c['id']] = c
    vus = set()
    for p in pieces:
        for i, pa in enumerate(p['paras']):
            t = pa['txt']
            if '[[' in t and not re.search(r'\[\[[a-z]:.*?\]\]', t):
                e.append('%s §%d : balisage mal formé' % (p['id'], i + 1))
            for n in (pa.get('n') or []):
                if n['k'] not in cles:
                    e.append('%s §%d : critère inconnu « %s »' % (p['id'], i + 1, n['k']))
                vus.add(n['k'])
                if t.count(n['e']) != 1:
                    e.append('%s §%d : extrait absent ou en double (%d) — « %s »'
                             % (p['id'], i + 1, t.count(n['e']), n['e'][:46]))
                # un extrait ne doit pas couper un balisage
                for m in re.finditer(r'\[\[[a-z]:.*?\]\]', t):
                    a, b = m.span()
                    j = t.find(n['e'])
                    k = j + len(n['e'])
                    if (a < j < b) or (a < k < b):
                        e.append('%s §%d : l’extrait coupe un balisage — « %s »'
                                 % (p['id'], i + 1, n['e'][:40]))
                if len(n['x']) < 50:
                    e.append('%s §%d : explication trop courte pour %s'
                             % (p['id'], i + 1, n['k']))
        for n in (p.get('globaux') or []):
            if n['k'] not in cles:
                e.append('%s : critère global inconnu « %s »' % (p['id'], n['k']))
            vus.add(n['k'])
            if len(n['x']) < 70:
                e.append('%s : explication globale trop courte pour %s'
                         % (p['id'], n['k']))
    # le plan détaillé porte les critères qui se jugent sur la copie entière
    for n in ((plan or {}).get('notes') or []):
        if n['k'] not in cles:
            e.append('plan : critère inconnu « %s »' % n['k'])
        vus.add(n['k'])
        if len(n['x']) < 70:
            e.append('plan : explication trop courte pour %s' % n['k'])
    manquants = [c for c in cles if c not in vus]
    if manquants:
        e.append('critères jamais illustrés : ' + ', '.join(sorted(manquants)))
    # chaque critère renvoyant à une pièce doit viser une pièce existante
    ids = {p['id'] for p in pieces} | {'plan'}
    for c in cles.values():
        if c.get('ex') and c['ex'][0] not in ids:
            e.append('%s : pièce inconnue « %s »' % (c['id'], c['ex'][0]))
    return e


def monter(grille, pieces, plan, sortie='methode.json'):
    pb = verifier(grille, pieces, plan)
    for x in pb:
        print(' ', x)
    d = {'v': 226, 'grille': grille, 'pieces': pieces, 'plan': plan}
    json.dump(d, open(sortie, 'w', encoding='utf-8'), ensure_ascii=False)
    n = sum(len(g['items']) for g in grille)
    notes = sum(len(pa.get('n') or []) for p in pieces for pa in p['paras'])
    notes += sum(len(p.get('globaux') or []) for p in pieces)
    mots = sum(len(nettoyer(pa['txt']).split()) for p in pieces for pa in p['paras'])
    print('\n%d critères · %d pièces · %d annotations · %d mots rédigés · '
          '%d points à reprendre' % (n, len(pieces), notes, mots, len(pb)))
    return len(pb)
