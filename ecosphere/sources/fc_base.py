# -*- coding: utf-8 -*-
"""Socle de la banque de flashcards (v227).

Une carte est ancrée sur un bloc identifiable du cours : l'index du bloc
donne à la fois l'année, le chapitre, la sous-partie et le renvoi vers le
passage. L'auteur n'écrit donc que la question, la réponse et, si elle
aide, une courte explication.

    c('Qu’est-ce que la monnaie fiduciaire ?',
      'Les billets et les pièces, dont la valeur repose sur la confiance.',
      x='Leur valeur faciale est sans rapport avec la valeur du support.',
      t='def', b=118)

Le validateur refuse : un recto qui ne tient pas tout seul, un recto qui
laisse voir la réponse, une réponse trop longue pour une seule carte, un
doublon de fond, un bloc inexistant.
"""

import json
import os
import re
import sys
import unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))

TYPES = {
    'def':  'Définition',
    'aut':  'Auteur',
    'mec':  'Mécanisme',
    'dist': 'Distinction',
    'fait': 'Chiffre ou fait',
    'form': 'Formule',
}

ANNEE = {}
for _n in range(1, 11):
    ANNEE[str(_n)] = 1
for _n in range(21, 27):
    ANNEE[str(_n)] = 2

# libellé court d'un chapitre tel qu'il doit s'afficher partout
def etiquette(ch):
    ch = str(ch)
    return ('1re année · ch. %s' % ch) if ANNEE[ch] == 1 \
        else ('2e année · ch. %d' % (int(ch) - 20))


# --------------------------------------------------------------- blocs

_BLOCS = None


def blocs(ch=None):
    global _BLOCS
    if _BLOCS is None:
        p = os.path.join(ICI, 'blocs_bruts.json')
        _BLOCS = json.load(open(p, encoding='utf-8'))
    return _BLOCS if ch is None else _BLOCS[str(ch)]


def texte_bloc(ch, b):
    o = blocs(ch)[b]
    return o.get('x') or ' '.join(x for x in (o.get('dt'), o.get('dd')) if x)


def chemin(ch, b):
    """Fil d'Ariane du bloc : [partie, sous-partie, sous-sous-partie]."""
    return [t for t in (blocs(ch)[b].get('p') or []) if t]


def sous_partie(ch, b):
    """Libellé de sous-partie retenu pour le classement d'une carte."""
    p = chemin(ch, b)
    if not p:
        return 'Chapitre'
    return p[1] if len(p) > 1 else p[0]


def partie(ch, b):
    p = chemin(ch, b)
    return p[0] if p else 'Chapitre'


# -------------------------------------------------------------- écriture

_LOT = []


def lot(ch):
    """Ouvre un chapitre : toutes les cartes suivantes lui sont rattachées."""
    global _LOT
    _LOT = []
    _LOT_CH[0] = str(ch)
    return _LOT


_LOT_CH = ['1']


def c(q, r, x=None, t='def', b=None, aussi=None):
    if b is None:
        raise ValueError('bloc manquant pour : ' + q[:60])
    d = {'q': q.strip(), 'r': r.strip(), 't': t, 'ch': _LOT_CH[0], 'b': int(b)}
    if x:
        d['x'] = x.strip()
    if aussi:
        d['aussi'] = [str(a) for a in aussi]
    _LOT.append(d)
    return d


# ------------------------------------------------------------ contrôles

_VIDES = re.compile(
    r'^\s*(d[ée]finition|auteur|notion|formule|tableau|sch[ée]ma|graphique|'
    r'[ée]tape\s*\d+|exemple|id[ée]e|citation|chiffre|fait|rappel|point\s*\d+|'
    r'partie\s*[ivx\d]+|[a-z]\.|\d+[.)]?)\s*[:.]?\s*$', re.I)

_MOTS_VIDES = set("""
a au aux avec ce ces dans de des du elle en et eux il ils je la le les leur
lui ma mais me meme mes moi mon ne nos notre nous on ou par pas pour qu que
qui sa se ses son sur ta te tes toi ton tu un une vos votre vous c d j l m n
s t y est sont ete etre avoir quel quelle quels quelles quoi comment pourquoi
dans entre selon chez sans sous plus moins tres bien aussi donc or ni car
lorsque quand si alors ainsi cette cet leurs
""".split())


def nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    s = ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn')
    s = s.replace('’', "'").replace('œ', 'oe')
    s = re.sub(r"[^a-z0-9]+", ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def mots(s):
    return [m for m in nz(s).split() if m not in _MOTS_VIDES and len(m) > 2]


def _plus_long_commun(a, b):
    """Longueur du plus long segment de mots commun à a et b."""
    A, B = nz(a).split(), nz(b).split()
    if not A or not B:
        return 0
    prec = [0] * (len(B) + 1)
    best = 0
    for i in range(1, len(A) + 1):
        cur = [0] * (len(B) + 1)
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                cur[j] = prec[j - 1] + 1
                if cur[j] > best:
                    best = cur[j]
        prec = cur
    return best


def verifier(cartes, strict=True):
    """Retourne la liste des reproches. Vide = banque livrable."""
    e = []
    vus_q = {}
    vus_fond = {}
    for i, k in enumerate(cartes):
        ref = '%s#%d' % (k['ch'], i + 1)
        q, r, t = k['q'], k['r'], k.get('t')
        x = k.get('x', '')

        if t not in TYPES:
            e.append('%s : type inconnu « %s »' % (ref, t))

        # --- le recto tient-il tout seul ?
        if _VIDES.match(q):
            e.append('%s : recto creux « %s »' % (ref, q))
        if len(q) < 18:
            e.append('%s : recto trop court « %s »' % (ref, q))
        if not mots(q):
            e.append('%s : recto sans contenu « %s »' % (ref, q))
        if not q.endswith(('?', '.', ' :')) and '?' not in q:
            e.append('%s : recto qui n’est pas une question « %s »' % (ref, q))
        if re.search(r'\b(ci-dessus|ci-dessous|ce passage|cette ligne|'
                     r'le tableau \d|ligne \d)\b', q, re.I):
            e.append('%s : recto qui renvoie à un contexte absent « %s »'
                     % (ref, q))

        # --- le recto laisse-t-il voir la réponse ?
        n = _plus_long_commun(q, r)
        if n >= 5:
            e.append('%s : le recto reprend %d mots de suite de la réponse — '
                     '« %s »' % (ref, n, q))

        # la réponse ne redit pas la question : elle commence par l'essentiel
        tete = mots(r)[:3]
        if len(tete) == 3 and all(m in mots(q) for m in tete):
            e.append('%s : la réponse redit la question avant de répondre — '
                     '« %s »' % (ref, r[:70]))

        # --- le verso
        if len(r) < 4:
            e.append('%s : réponse absente ou trop courte' % ref)
        if len(r) > 330:
            e.append('%s : réponse de %d signes — à découper en plusieurs '
                     'cartes (« %s »)' % (ref, len(r), q[:60]))
        if x and len(x) > 460:
            e.append('%s : explication de %d signes, trop longue' % (ref, len(x)))
        if x and len(x) < 30:
            e.append('%s : explication trop courte pour être utile' % ref)
        if x and _plus_long_commun(r, x) >= 8:
            e.append('%s : l’explication répète la réponse' % ref)

        # --- ancrage
        try:
            txt = texte_bloc(k['ch'], k['b'])
        except (KeyError, IndexError):
            e.append('%s : bloc %s absent du chapitre %s'
                     % (ref, k['b'], k['ch']))
            txt = ''
        if txt is not None and len(nz(txt)) < 12:
            e.append('%s : bloc %d sans texte exploitable' % (ref, k['b']))

        # --- doublons
        cq = nz(q)
        if cq in vus_q:
            e.append('%s : recto identique à %s' % (ref, vus_q[cq]))
        vus_q[cq] = ref
        fond = (k['ch'], t, ' '.join(sorted(set(mots(r)))[:9]))
        if fond[2] and fond in vus_fond:
            e.append('%s : même fond que %s (« %s » / même réponse)'
                     % (ref, vus_fond[fond], q[:52]))
        vus_fond[fond] = ref

    return e


def couverture(cartes, ch):
    """Sous-parties du chapitre, et nombre de cartes pour chacune.

    Une sous-partie qui ne contient que des titres n'entre pas dans le
    décompte : il n'y a rien à y mémoriser.
    """
    ch = str(ch)
    ordre, vus, utile = [], set(), set()
    B = blocs(ch)
    for b in range(len(B)):
        s = sous_partie(ch, b)
        if s not in vus:
            vus.add(s)
            ordre.append(s)
        if B[b].get('g') not in ('h2', 'h3', 'h4', 'h5', 'table') \
                and len(nz(texte_bloc(ch, b))) >= 25:
            utile.add(s)
    ordre = [s for s in ordre if s in utile]
    n = dict((s, 0) for s in ordre)
    for k in cartes:
        if k['ch'] != ch:
            continue
        n[sous_partie(ch, k['b'])] = n.get(sous_partie(ch, k['b']), 0) + 1
    return [(s, n.get(s, 0)) for s in ordre]


def parties(cartes, ch):
    """Couverture des grandes parties (premier niveau du fil d'Ariane)."""
    ch = str(ch)
    ordre, vus = [], set()
    B = blocs(ch)
    for b in range(len(B)):
        p = partie(ch, b)
        if p not in vus and B[b].get('g') not in ('h2', 'h3', 'h4', 'table') \
                and len(nz(texte_bloc(ch, b))) >= 25:
            vus.add(p)
            ordre.append(p)
    pris = set(partie(ch, k['b']) for k in cartes if k['ch'] == ch)
    return [(p, p in pris) for p in ordre]


def etalement(cartes, ch, rayon=20):
    """Part des blocs utiles du chapitre situés près d'une carte.

    Mesure si la banque balaie tout le chapitre ou se concentre sur
    quelques thèmes — ce qu'un simple décompte de cartes ne dit pas.
    """
    ch = str(ch)
    B = blocs(ch)
    utiles = [b for b in range(len(B))
              if B[b].get('g') not in ('h2', 'h3', 'h4', 'table')
              and len(nz(texte_bloc(ch, b))) >= 40]
    if not utiles:
        return 1.0
    ancres = sorted(k['b'] for k in cartes if k['ch'] == ch)
    if not ancres:
        return 0.0
    import bisect
    n = 0
    for b in utiles:
        i = bisect.bisect_left(ancres, b)
        for j in (i - 1, i):
            if 0 <= j < len(ancres) and abs(ancres[j] - b) <= rayon:
                n += 1
                break
    return n / len(utiles)


def bilan(cartes, ch, taire=False):
    cov = couverture(cartes, ch)
    pleines = [s for s, k in cov if k]
    par = parties(cartes, ch)
    pp = [p for p, ok in par if ok]
    et = etalement(cartes, ch)
    n = len([k for k in cartes if k['ch'] == str(ch)])
    if not taire:
        print('ch %s : %3d cartes · %d/%d parties · %d/%d sous-parties · '
              'étalement %d%%'
              % (ch, n, len(pp), len(par), len(pleines), len(cov), et * 100))
        vides = [p for p, ok in par if not ok]
        if vides:
            print('   parties non couvertes : '
                  + ' | '.join(v[:52] for v in vides))
    return {'ch': str(ch), 'n': n, 'sp': len(pleines), 'spTot': len(cov),
            'pa': len(pp), 'paTot': len(par), 'et': round(et * 100),
            'vides': [p for p, ok in par if not ok]}


def monter(cartes, sortie='flashcards.json', bilans=None):
    pb = verifier(cartes)
    for p in pb[:60]:
        print(' ', p)
    if len(pb) > 60:
        print('  … et %d autres' % (len(pb) - 60))
    out = []
    for i, k in enumerate(cartes):
        ch = k['ch']
        d = {'i': 'f%d' % (i + 1), 'q': k['q'], 'r': k['r'], 't': k['t'],
             'ch': ch, 'an': ANNEE[ch], 'b': k['b'],
             'sp': sous_partie(ch, k['b']), 'pa': partie(ch, k['b'])}
        if k.get('x'):
            d['x'] = k['x']
        if k.get('aussi'):
            d['aussi'] = k['aussi']
        out.append(d)
    d = {'v': 227, 'cartes': out, 'bilans': bilans or []}
    json.dump(d, open(os.path.join(ICI, sortie), 'w', encoding='utf-8'),
              ensure_ascii=False)
    par = {}
    for k in out:
        par[k['ch']] = par.get(k['ch'], 0) + 1
    print('\n%d cartes · %d chapitres · %d points à reprendre'
          % (len(out), len(par), len(pb)))
    return len(pb)
