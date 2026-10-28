# -*- coding: utf-8 -*-
"""Contrôle des attributions d'auteurs des visualisations.

Chaque idée attribuée à un auteur doit se retrouver, au moins par ses mots
pleins, soit dans la fiche de cet auteur dans la base d'ÉcoSphère, soit dans
l'une des idées que les dossiers « Autour d'une notion » lui prêtent déjà —
elles-mêmes vérifiées sur les cours. Une idée qui ne recoupe aucune des deux
sources est signalée : c'est le symptôme d'une attribution inventée.
"""
import glob
import importlib
import json
import re
import unicodedata

import socle
import vz_base

for f in sorted(glob.glob('vz_[0-9][0-9]*.py')):
    importlib.import_module(f[:-3])

VIDE = set("""de du des la le les l un une et ou a au aux en dans par pour
sur ce cette ces son sa ses leur leurs il elle on qui que quoi dont est sont
etre avoir plus moins tres tout tous toute toutes non pas ne n d s c qu y
comme donc alors meme autre autres entre vers chez sans sous apres avant
lorsque puisque parce ainsi aussi mais car si selon peut peuvent doit
doivent fait faire cours notion""".split())


def mots(s):
    t = socle.nz(s)
    t = re.sub(r"[^a-z0-9àâçéèêëîïôûùüÿñæœ' ]", ' ', t)
    return {w for w in t.replace("'", ' ').split() if len(w) > 3 and w not in VIDE}


# ------------------------------------------------- sources de référence
C = json.load(open('corpus.json'))
FICHE = {}
for a in C['auteurs']:
    FICHE.setdefault(socle.nz(a['name']), []).append(
        ' '.join(str(a.get(k) or '') for k in ('idea', 'detail', 'phrase')) +
        ' ' + ' '.join(a.get('oeuvres') or []))

D = json.load(open('autour_payload.json'))
DOSS = {}
for d in D['dossiers']:
    for a in (d.get('aut') or []):
        DOSS.setdefault(socle.nz(a.get('n', '')), []).append(a.get('i', ''))


def patro(nom):
    b = socle.nz(nom).split()
    return b[-1] if b else ''


pb = []
tot = 0
for x in vz_base.VISUS:
    for n in x['noeuds']:
        for a in n['aut']:
            tot += 1
            nom, idee = a['n'], a['i']
            n0 = socle.nz(nom)
            ref = ' '.join(FICHE.get(n0, []) + DOSS.get(n0, []))
            if not ref:
                # un patronyme seul : on rassemble toutes les homonymies
                p = patro(nom)
                for k, v in list(FICHE.items()) + list(DOSS.items()):
                    if patro(k) == p:
                        ref += ' ' + ' '.join(v if isinstance(v, list) else [v])
            mi, mr = mots(idee), mots(ref)
            if not mi:
                continue
            part = len(mi & mr) / len(mi)
            if part < 0.26:
                # second recours : le texte des cours lui-même, autour des
                # occurrences du patronyme
                p = patro(nom)
                env = []
                for k in socle.ORDRE:
                    t = socle.NTXT[k]
                    i = t.find(p)
                    while i >= 0 and len(env) < 60:
                        env.append(t[max(0, i - 900):i + 900])
                        i = t.find(p, i + 1)
                mc = mots(' '.join(env))
                part = max(part, len(mi & mc) / len(mi))
            if part < 0.26:
                pb.append((x['cle'], n['id'], nom, round(part, 2), idee[:110]))

print('attributions contrôlées : %d' % tot)
if not pb:
    print('aucune attribution suspecte')
for p in pb:
    print('  %-22s %-14s %-24s %.2f  %s' % p)
