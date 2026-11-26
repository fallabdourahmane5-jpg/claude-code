# -*- coding: utf-8 -*-
"""Socle commun des fiches « Courbes ».

Une fiche décrit un graphique par des séries placées dans un repère
normalisé (x et y de 0 à 1, origine en bas à gauche) et par des étapes qui
déplacent ces séries. Les fonctions ci-dessous servent à écrire ces séries
sans calculer les intersections à la main : le moteur de rendu n'a plus qu'à
tracer ce qui est décrit.
"""

import json
import re
import unicodedata

# ----------------------------------------------------------------- séries


def lin(i, lib, x1, y1, x2, y2, c='ac', **kw):
    s = {'id': i, 'lib': lib, 'type': 'lin', 'p': [x1, y1, x2, y2], 'c': c}
    s.update(kw)
    return s


def pol(i, lib, pts, c='ac', **kw):
    p = []
    for a, b in pts:
        p += [a, b]
    s = {'id': i, 'lib': lib, 'type': 'pol', 'p': p, 'c': c}
    s.update(kw)
    return s


def pt(i, lib, x, y, c='ac2', **kw):
    s = {'id': i, 'lib': lib, 'type': 'pt', 'p': [x, y], 'c': c}
    s.update(kw)
    return s


def fl(i, lib, x1, y1, x2, y2, c='gr', **kw):
    s = {'id': i, 'lib': lib, 'type': 'fl', 'p': [x1, y1, x2, y2], 'c': c}
    s.update(kw)
    return s


def txt(i, lib, x, y, c=None, taille=15, gras=False, **kw):
    s = {'id': i, 'lib': lib, 'type': 'txt', 'p': [x, y], 'pt': taille}
    if c:
        s['c'] = c
    if gras:
        s['gras'] = 1
    s.update(kw)
    return s


def rep(i, x, y, lx=None, ly=None, c='gr', **kw):
    """Repères en pointillés vers les deux axes, avec leurs étiquettes."""
    s = {'id': i, 'type': 'rep', 'p': [x, y], 'c': c, 'lib': ''}
    if lx:
        s['lx'] = lx
    if ly:
        s['ly'] = ly
    s.update(kw)
    return s


def zone(i, lib, pts, c='ac', **kw):
    p = []
    for a, b in pts:
        p += [a, b]
    s = {'id': i, 'lib': lib, 'type': 'zone', 'p': p, 'c': c}
    s.update(kw)
    return s


# ------------------------------------------------------------- géométrie


def y_de(d, x):
    """Ordonnée d'une droite décrite par [x1, y1, x2, y2] à l'abscisse x."""
    x1, y1, x2, y2 = d['p'] if isinstance(d, dict) else d
    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)


def x_de(d, y):
    x1, y1, x2, y2 = d['p'] if isinstance(d, dict) else d
    return x1 + (x2 - x1) * (y - y1) / (y2 - y1)


def inter(a, b):
    """Intersection de deux droites, chacune donnée par sa série ou [x1…y2]."""
    ax1, ay1, ax2, ay2 = a['p'] if isinstance(a, dict) else a
    bx1, by1, bx2, by2 = b['p'] if isinstance(b, dict) else b
    d1x, d1y = ax2 - ax1, ay2 - ay1
    d2x, d2y = bx2 - bx1, by2 - by1
    den = d1x * d2y - d1y * d2x
    if abs(den) < 1e-9:
        raise ValueError('droites parallèles')
    t = ((bx1 - ax1) * d2y - (by1 - ay1) * d2x) / den
    return (round(ax1 + t * d1x, 4), round(ay1 + t * d1y, 4))


def bouge(d, dx=0.0, dy=0.0):
    """Nouvelle droite translatée — pratique pour calculer un équilibre."""
    x1, y1, x2, y2 = d['p'] if isinstance(d, dict) else d
    return [x1 + dx, y1 + dy, x2 + dx, y2 + dy]


def courbe_dec(x1, y1, x2, y2, n=9, creux=0.55):
    """Courbe décroissante convexe entre deux points (type demande)."""
    out = []
    for k in range(n):
        u = k / (n - 1.0)
        x = x1 + (x2 - x1) * u
        y = y1 + (y2 - y1) * (u ** (1.0 / creux) if creux else u)
        out.append((round(x, 4), round(y, 4)))
    return out


def courbe_cro(x1, y1, x2, y2, n=9, creux=0.55):
    """Courbe croissante concave entre deux points (type offre)."""
    out = []
    for k in range(n):
        u = k / (n - 1.0)
        x = x1 + (x2 - x1) * u
        y = y1 + (y2 - y1) * (u ** creux)
        out.append((round(x, 4), round(y, 4)))
    return out


def cloche(x1, x2, ybas, yhaut, n=13, pic=0.5):
    """Courbe en cloche (Laffer, Kuznets, utilité marginale décroissante…)."""
    out = []
    for k in range(n):
        u = k / (n - 1.0)
        x = x1 + (x2 - x1) * u
        y = ybas + (yhaut - ybas) * (1 - ((u - pic) / max(pic, 1 - pic)) ** 2)
        out.append((round(x, 4), round(max(ybas, y), 4)))
    return out


def en_u(x1, x2, yhaut, ybas, n=13, creux=0.45):
    """Courbe en U (coût moyen, coût marginal)."""
    out = []
    for k in range(n):
        u = k / (n - 1.0)
        x = x1 + (x2 - x1) * u
        y = ybas + (yhaut - ybas) * ((u - creux) / max(creux, 1 - creux)) ** 2
        out.append((round(x, 4), round(min(yhaut, y), 4)))
    return out


def logistique(x1, x2, ybas, yhaut, n=15, pente=9.0, milieu=0.5):
    out = []
    for k in range(n):
        u = k / (n - 1.0)
        x = x1 + (x2 - x1) * u
        import math
        y = ybas + (yhaut - ybas) / (1 + math.exp(-pente * (u - milieu)))
        out.append((round(x, 4), round(y, 4)))
    return out


def hyper(k, x1, x2, n=15, dx=0.0, dy=0.0):
    """Branche d'hyperbole (x−dx)(y−dy) = k : courbe d'indifférence, isoquante."""
    out = []
    for j in range(n):
        u = j / (n - 1.0)
        x = x1 + (x2 - x1) * u
        out.append((round(x, 4), round(dy + k / (x - dx), 4)))
    return out


def barre(i, lib, x, y, larg=0.07, c='ac', base=0.0, **kw):
    """Barre verticale — pour les graphiques de données."""
    return zone(i, lib, [(x - larg / 2, base), (x + larg / 2, base),
                         (x + larg / 2, y), (x - larg / 2, y)], c, **kw)


def concave(x1, y1, x2, y2, n=11, force=0.5):
    """Croissance concave (Solow : production par tête)."""
    out = []
    for k in range(n):
        u = k / (n - 1.0)
        x = x1 + (x2 - x1) * u
        y = y1 + (y2 - y1) * (u ** force)
        out.append((round(x, 4), round(y, 4)))
    return out


# ----------------------------------------------------------------- fiche


CHAMPS = ('id', 't', 'st', 'cat', 'an', 'ch', 'liens', 'type', 'q', 'axes',
          'depart', 'hyp', 'pente', 'fig', 'etapes', 'pieges', 'main',
          'phrase', 'src', 'mots', 'variantes')


def fiche(**kw):
    for c in ('id', 't', 'st', 'cat', 'an', 'ch', 'q', 'axes', 'fig',
              'main', 'phrase', 'liens'):
        if c not in kw:
            raise ValueError('champ manquant : %s dans %s' % (c, kw.get('id')))
    for c in kw:
        if c not in CHAMPS:
            raise ValueError('champ inconnu : %s' % c)
    return kw


def etape(t, d, **kw):
    e = {'t': t, 'd': d}
    e.update(kw)
    return e


def nzz(s):
    s = unicodedata.normalize('NFD', str(s or '').lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


# ------------------------------------------------------------ contrôles


def verifier(f):
    """Contrôles de forme : repère, étapes, séries citées, longueurs."""
    e = []
    ids = set()

    def cadre(s, ou):
        for k in range(0, len(s['p']), 2):
            x, y = s['p'][k], s['p'][k + 1]
            if not (-0.12 <= x <= 1.14) or not (-0.12 <= y <= 1.14):
                e.append('point hors du repère : %s (%.2f, %.2f) — %s'
                         % (s['id'], x, y, ou))

    for s in f['fig']['series']:
        if s['id'] in ids:
            e.append('série en double : ' + s['id'])
        ids.add(s['id'])
        cadre(s, 'figure de départ')
    for nom, ets in ([('principale', f.get('etapes') or [])] +
                     [(v['lib'], v['etapes']) for v in (f.get('variantes') or [])]):
        for i, et in enumerate(ets):
            for s in (et.get('add') or []):
                cadre(s, '%s, étape %d' % (nom, i + 1))
    jeux = []
    if f.get('etapes') or not f.get('variantes'):
        jeux.append(('principale', f.get('etapes') or []))
    for v in (f.get('variantes') or []):
        jeux.append((v['lib'], v['etapes']))
    if not f.get('etapes') and not f.get('variantes'):
        e.append('aucune étape de lecture')
    for nom, ets in jeux:
        if len(ets) < 2:
            e.append('%s : moins de deux étapes' % nom)
        connus = set(ids)
        for i, et in enumerate(ets):
            for s in (et.get('add') or []):
                connus.add(s['id'])
            for cle in ('on', 'off', 'vif', 'seul'):
                for sid in (et.get(cle) or []):
                    if sid not in connus:
                        e.append('%s, étape %d : série inconnue « %s »' % (nom, i + 1, sid))
            for sid in (et.get('move') or {}):
                if sid not in connus:
                    e.append('%s, étape %d : déplacement d’une série inconnue « %s »'
                             % (nom, i + 1, sid))
            if len(et.get('d') or '') < 60:
                e.append('%s, étape %d : explication trop courte' % (nom, i + 1))
    if len(f.get('main') or []) < 3:
        e.append('tracé à la main : moins de trois étapes')
    if len(f.get('phrase') or '') < 90:
        e.append('phrase de dissertation trop courte')
    if len(f.get('q') or '') < 40:
        e.append('question trop courte')
    if not f.get('liens'):
        e.append('aucun renvoi au cours')
    if f.get('type') == 'donnees':
        s = f.get('src')
        if not s:
            e.append('graphique de données sans source')
        elif isinstance(s, dict):
            for cle, nom in (('so', 'source'), ('pe', 'période'), ('un', 'unités')):
                if not s.get(cle):
                    e.append('graphique de données : %s manquante' % nom)
    return e


def monter(fiches, cats, sortie='courbes.json'):
    vus, pb = set(), 0
    for f in fiches:
        if f['id'] in vus:
            print('IDENTIFIANT EN DOUBLE :', f['id'])
            pb += 1
        vus.add(f['id'])
        for x in verifier(f):
            print('%-26s %s' % (f['id'], x))
            pb += 1
        if f['cat'] not in cats:
            print('%-26s thème inconnu : %s' % (f['id'], f['cat']))
            pb += 1
    d = {'v': 225, 'cat': cats, 'f': fiches}
    json.dump(d, open(sortie, 'w', encoding='utf-8'), ensure_ascii=False)
    print('\n%d fiches, %d points à reprendre' % (len(fiches), pb))
    par = {}
    for f in fiches:
        for k in f['ch']:
            par[k] = par.get(k, 0) + 1
    ordre = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
             '21', '22', '23', '24', '25', '26']
    print('par chapitre :', ' '.join('%s:%d' % (k, par.get(k, 0)) for k in ordre))
    return pb
