# -*- coding: utf-8 -*-
"""Socle commun de la nouvelle recherche : normalisation et sources.

Toutes les étapes de la reconstruction (relevé des manques, rédaction des
définitions absentes, montage de l'index) partagent ces fonctions pour que la
clé d'une expression soit la même partout.
"""
import json
import re
import unicodedata

ORDRE = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
         '21', '22', '23', '24']
LIB = {'21': '2ᵉ année — ch.1', '22': '2ᵉ année — ch.2',
       '23': '2ᵉ année — ch.3', '24': '2ᵉ année — ch.4'}


def lib(k):
    return LIB.get(str(k), 'Chapitre ' + str(k))


def nz(s):
    """Minuscules, sans accents, apostrophes et ponctuation unifiées."""
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.replace('’', "'").replace('‘', "'").replace('œ', 'oe')
    s = s.replace('æ', 'ae')
    return re.sub(r'\s+', ' ', s).strip()


def mots(s):
    """Jetons d'une expression, pluriels ramenés au singulier."""
    t = re.sub(r"[^a-z0-9àâçéèêëîïôûùüÿ' ]+", ' ', nz(s))
    t = t.replace("'", ' ')
    return [sing(w) for w in t.split() if len(w) > 1]


def sing(w):
    """Forme singulier approchée. On ne touche pas au « x » final : « taux »,
    « prix » et « flux » ne sont pas des pluriels."""
    if len(w) > 5 and w.endswith('eaux'):      # réseaux -> réseau
        return w[:-1]
    if len(w) > 5 and w.endswith('aux'):       # travaux, chevaux
        return w[:-3] + 'al'
    if len(w) > 5 and w.endswith('ail'):       # travail -> même radical
        return w[:-3] + 'al'
    if len(w) > 3 and w.endswith('s') and not w.endswith('ss'):
        return w[:-1]
    return w


ARTICLE = re.compile(r'^(?:le|la|les|l|un|une|des|du|de|d|au|aux|ce|cet|'
                     r'cette|ces|son|sa|ses|leur|leurs|mon|notre)\b\s*')


def cle(s):
    """Clé de regroupement : jetons au singulier, articles de tête retirés."""
    t = ' '.join(mots(s))
    avant = None
    while t and t != avant:
        avant = t
        t = ARTICLE.sub('', t)
    return t or ' '.join(mots(s))


# intitulés décoratifs : ce ne sont pas des notions
BRUIT = re.compile(
    r'^(introduction|conclusion|idee|idee cle|idee generale|idee centrale|'
    r'exemple|exemples|schema|formule|formules|document|lecture|remarque|'
    r'attention|definition|definitions|resume|synthese|rappel|cl|source|'
    r'reference|references|graphique|tableau|plan|sommaire|transition|'
    r'mot cle a retenir|a retenir|mots cles|point|points|bilan|'
    r'consequence graphique|cas general|cas particulier|le principe|'
    r'principe|le mecanisme|mecanisme|la logique|logique|objectif|objectifs|'
    r'constat|probleme|enjeu|enjeux|limite|limites|critique|critiques|'
    r'pourquoi|comment|en resume|au total|donc|ainsi|mais|or)$')

MARQUE = re.compile(r'^\s*(?:[IVXLC]{1,6}\.|[A-Z]{1,2}\.|\d{1,2}\s*[-.)])\s*')


def titre_propre(s):
    """Intitulé débarrassé de sa marque de numérotation."""
    return MARQUE.sub('', str(s or '')).strip(' :·—–-’\'"')


def est_notion(t):
    """Un intitulé qui nomme une notion, et non une étape du raisonnement."""
    n = nz(t)
    if not (3 <= len(t) <= 80):
        return False
    if BRUIT.match(n) or t.endswith('?'):
        return False
    m = mots(t)
    if not m or len(m) > 8:
        return False
    # une phrase conjuguée décrit un raisonnement, pas une notion
    if re.search(r'\b(est|sont|peut|peuvent|doit|doivent|permet|permettent|'
                 r'montre|montrent|explique|expliquent|conduit|conduisent|'
                 r'depend|dependent|implique|impliquent|suppose|supposent|'
                 r'devient|deviennent|reste|restent|faut|il y a|on peut|'
                 r'illustre|illustrent|constitue|constituent|repose|reposent|'
                 r'traduit|traduisent|revient|reviennent|donne|donnent|'
                 r'apparait|apparaissent|se definit|cherche|cherchent)\b', n):
        return False
    return True


# ------------------------------------------------------------------- sources

def blocs():
    return json.load(open('blocs_bruts.json'))


def corpus():
    return json.load(open('corpus.json'))


def atlas():
    return json.load(open('corpus_atlas.json'))


def autour():
    return json.load(open('autour_payload.json'))


def visu():
    return json.load(open('visu_payload.json'))


def fiches():
    return json.load(open('fc_data.json'))


def chiffres():
    import importlib
    out = {}
    for m in ('chif_a', 'chif_b', 'chif_c', 'chif_d'):
        for k, v in importlib.import_module(m).CH.items():
            d = out.setdefault(str(k), [])
            for rang in ('prio', 'comp'):
                for x in (v.get(rang) or []):
                    y = dict(x)
                    y['rang'] = rang
                    d.append(y)
    return out


def resumes():
    import glob
    import importlib
    out = {}
    for f in sorted(glob.glob('res_[abc].py')) + sorted(glob.glob('res2_*.py')):
        for k, v in importlib.import_module(f[:-3]).R.items():
            out[str(k)] = v
    return out
