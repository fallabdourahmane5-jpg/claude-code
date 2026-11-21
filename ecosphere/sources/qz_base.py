# -*- coding: utf-8 -*-
"""Socle de la banque de questions du quiz.

Modèle d'une question :

  id    identifiant stable, par exemple « q25-014 »
  ch    chapitre (1 à 10, 21 à 26)
  sp    clé de sous-partie, par exemple « c25-07 »
  niv   niveau de travail demandé :
          connaitre  — définir, identifier un auteur, situer un fait
          comprendre — expliquer un effet, distinguer deux notions, poser
                       les hypothèses d'un modèle
          appliquer  — partir d'un cas et retrouver le mécanisme
          raisonner  — enchaîner les causes, confronter deux analyses,
                       repérer une limite, choisir ce qu'on mobilise
  type  qcm (une réponse), qcmm (plusieurs réponses), vf (vrai/faux à
        justifier), assoc (auteur ↔ idée), ordre (remise en ordre),
        courte (réponse rédigée brève)
  q     énoncé
  opts  propositions (qcm, qcmm)
  ans   réponse : indice (qcm), liste d'indices (qcmm), booléen (vf),
        liste ordonnée (ordre), appariements (assoc), modèle (courte)
  exp   pourquoi la réponse est juste
  why   pour un QCM, pourquoi chacune des autres propositions est fausse
  diss  « Comment l'utiliser en dissertation » (facultatif)
  b     bloc du cours qui justifie la question (renvoi cliquable)
  src   intitulé du passage visé
"""

import re
import unicodedata

NIVEAUX = ('connaitre', 'comprendre', 'appliquer', 'raisonner')
TYPES = ('qcm', 'qcmm', 'vf', 'assoc', 'ordre', 'courte')

LIB_NIV = {'connaitre': 'Connaître', 'comprendre': 'Comprendre',
           'appliquer': 'Appliquer', 'raisonner': 'Raisonner'}
LIB_TYPE = {'qcm': 'QCM', 'qcmm': 'QCM à plusieurs réponses',
            'vf': 'Vrai ou faux', 'assoc': 'Association',
            'ordre': 'Remise en ordre', 'courte': 'Réponse rédigée'}


def nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = re.sub(r"[^a-z0-9 ]", ' ', s.replace('’', "'"))
    return re.sub(r'\s+', ' ', s).strip()


# ---------------------------------------------------------------- niveaux
# Le niveau d'une question héritée est déduit de sa forme, puis corrigé à la
# main dans les modules de chapitre lorsque la déduction est trop grossière.

RE_CONNAITRE = re.compile(
    r"(?i)^(qui |quel auteur|quelle ann[ée]e|en quelle|quelle est la d[ée]finition"
    r"|que d[ée]signe|qu['’]est-ce que|comment (?:appelle|nomme)|dans quel ouvrage"
    r"|quel ouvrage|combien|quel est le nom|lequel de ces auteurs"
    r"|quelle est la formule|quel est le sigle)")
RE_APPLIQUER = re.compile(
    r"(?i)(un pays qui|une entreprise qui|si (?:un|une|le|la|les)\b|dans le cas"
    r"|supposons|on observe|soit une|lorsqu['’]un|lorsqu['’]une|imaginons"
    r"|dans l['’]exemple|application num|avec c = |que se passe-t-il)")
RE_RAISONNER = re.compile(
    r"(?i)(pourquoi .*(?:alors|malgr[ée]|bien que)|en quoi|dans quelle mesure"
    r"|peut-on (?:dire|conclure|affirmer)|quelle limite|quelles limites"
    r"|quel argument|opposer|confronter|comment articuler|faut-il"
    r"|quelle cons[ée]quence pour|enchaînement|cha[îi]ne causale"
    r"|comment mobiliser|dissertation)")
RE_COMPRENDRE = re.compile(
    r"(?i)(pourquoi|comment|expliquer|quelle diff[ée]rence|distinguer"
    r"|quelle hypoth[èe]se|[àa] quelle condition|quel m[ée]canisme"
    r"|qu['’]implique|que signifie)")


def niveau(q, type_):
    t = ' '.join(str(q or '').split())
    if type_ in ('ordre',):
        return 'raisonner'
    if type_ == 'assoc':
        return 'connaitre'
    if RE_RAISONNER.search(t):
        return 'raisonner'
    if RE_APPLIQUER.search(t):
        return 'appliquer'
    if RE_CONNAITRE.search(t):
        return 'connaitre'
    if RE_COMPRENDRE.search(t):
        return 'comprendre'
    return 'comprendre'


# ------------------------------------------------------------- contrôles

def verifier(q):
    """Contrôles de forme appliqués à toute question de la banque."""
    e = []
    for champ in ('id', 'ch', 'sp', 'niv', 'type', 'q', 'exp'):
        if not q.get(champ) and q.get(champ) != 0:
            e.append('champ manquant : ' + champ)
    if q.get('niv') not in NIVEAUX:
        e.append('niveau inconnu : %r' % q.get('niv'))
    if q.get('type') not in TYPES:
        e.append('type inconnu : %r' % q.get('type'))
    t, a, o = q.get('type'), q.get('ans'), q.get('opts') or []
    if t == 'qcm':
        if not (3 <= len(o) <= 5):
            e.append('un QCM demande de trois à cinq propositions (%d)' % len(o))
        if not isinstance(a, int) or not (0 <= a < len(o)):
            e.append('réponse hors bornes : %r' % (a,))
        if len(q.get('why') or []) != len(o) - 1:
            e.append('il manque la réfutation des autres propositions')
    elif t == 'qcmm':
        if not (4 <= len(o) <= 6):
            e.append('un QCM multiple demande de quatre à six propositions')
        if not isinstance(a, list) or not (2 <= len(a) <= len(o) - 1):
            e.append('réponses multiples attendues : %r' % (a,))
        if any(not isinstance(x, int) or not (0 <= x < len(o)) for x in a):
            e.append('réponse hors bornes : %r' % (a,))
        if len(q.get('why') or []) != len(o):
            e.append('chaque proposition doit être commentée')
    elif t == 'vf':
        if a not in (True, False):
            e.append('vrai/faux : réponse booléenne attendue')
    elif t == 'assoc':
        if not isinstance(a, list) or len(a) < 3:
            e.append('une association demande au moins trois couples')
        for c in (a or []):
            if not (isinstance(c, (list, tuple)) and len(c) == 2):
                e.append('couple mal formé : %r' % (c,))
    elif t == 'ordre':
        if not isinstance(a, list) or len(a) < 3:
            e.append('une remise en ordre demande au moins trois étapes')
    elif t == 'courte':
        if not isinstance(a, dict) or not a.get('cles'):
            e.append('réponse rédigée : il faut les éléments attendus')
    if len((q.get('exp') or '')) < 110:
        e.append('corrigé trop court (%d signes)' % len(q.get('exp') or ''))
    if q.get('b') is None or q['b'] < 0:
        e.append('aucun renvoi au cours')
    return e
