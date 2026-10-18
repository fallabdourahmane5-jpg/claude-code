# -*- coding: utf-8 -*-
"""Outils de cadrage : matière disponible et contrôle des attributions.

Un dossier ne peut citer que des auteurs présents dans la base d'ÉcoSphère,
elle-même issue des cours. Toute autre mention est refusée au montage.
"""
import json, re, unicodedata

C = json.load(open('corpus.json'))

def nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'"))

ORDRE = ['1','2','3','4','5','6','7','8','9','10','21','22','23','24']
TXT = {k: C['chapitres'][k]['texte'] for k in ORDRE}
NTXT = {k: nz(v) for k, v in TXT.items()}
AUTEURS = {a['name'] for a in C['auteurs']}
NAUT = {nz(a['name']): a['name'] for a in C['auteurs']}
# un patronyme seul suffit lorsqu'il est sans ambiguïté
PATRO = {}
for a in C['auteurs']:
    bouts = a['name'].split()
    if len(bouts) > 1:
        PATRO.setdefault(nz(bouts[-1]), set()).add(a['name'])

def auteur_connu(nom):
    n = nz(nom)
    if n in NAUT:
        return True
    return n in PATRO

def ou(terme, n=3, w=340):
    """Occurrences d'un terme dans les cours, avec leur contexte."""
    out = []
    for k in ORDRE:
        for m in list(re.finditer(re.escape(terme), TXT[k], re.I))[:n]:
            a = max(0, m.start() - w // 2)
            out.append((k, TXT[k][a:m.start() + w].replace('\n', ' ')))
    return out

def compte(terme):
    t = nz(terme)
    return {k: NTXT[k].count(t) for k in ORDRE if NTXT[k].count(t)}

def auteurs_de(*termes):
    """Auteurs dont l'idée ou le détail évoque l'un des termes."""
    cibles = [nz(t) for t in termes]
    out = []
    for a in C['auteurs']:
        blob = nz((a.get('idea') or '') + ' ' + (a.get('detail') or '') + ' ' +
                  (a.get('phrase') or '') + ' ' + ' '.join(a.get('oeuvres') or []))
        if any(c in blob for c in cibles):
            out.append((a['name'], a.get('dates'), a.get('courant'),
                        (a.get('idea') or '')[:120]))
    return out
