# -*- coding: utf-8 -*-
"""Contrôle des attributions d'auteurs des six dossiers ajoutés à l'ensemble 28.

Chaque idée prêtée à un auteur doit recouper, par ses mots pleins, soit la
fiche de cet auteur dans la base d'ÉcoSphère, soit le voisinage de son nom
dans le texte des cours. Une idée qui ne recoupe ni l'une ni l'autre est
signalée : c'est le symptôme d'une attribution non justifiée.
"""
import json
import re

import doss28i  # noqa: F401  (enregistre les dossiers)
import doss_base
import socle

VIDE = set("""de du des la le les l un une et ou a au aux en dans par pour
sur ce cette ces son sa ses leur leurs il elle on qui que quoi dont est sont
etre avoir plus moins tres tout tous toute toutes non pas ne n d s c qu y
comme donc alors meme autre autres entre vers chez sans sous apres avant
lorsque puisque parce ainsi aussi mais car si selon peut peuvent doit
doivent fait faire cours notion cela elles ils leurs tant plutot""".split())


def mots(s):
    t = socle.nz(s)
    t = re.sub(r"[^a-z0-9àâçéèêëîïôûùüÿñæœ' ]", ' ', t)
    return {w for w in t.replace("'", ' ').split() if len(w) > 3 and w not in VIDE}


C = json.load(open('corpus.json'))
FICHE = {}
for a in C['auteurs']:
    FICHE.setdefault(socle.nz(a['name']), []).append(
        ' '.join(str(a.get(k) or '') for k in ('idea', 'detail', 'phrase')) +
        ' ' + ' '.join(a.get('oeuvres') or []))

TXT = {k: socle.nz(v) for k, v in socle.TXT.items()}


def voisinage(nom):
    """Tout ce que les cours écrivent autour du nom de l'auteur."""
    cle = socle.nz(nom.split()[-1])
    bouts = []
    for t in TXT.values():
        for m in re.finditer(re.escape(cle), t):
            bouts.append(t[max(0, m.start() - 900):m.start() + 1800])
    return ' '.join(bouts)


CIBLES = {'le28-tentation-protectionnisme', 'le28-tentation-libre-echange',
          'le28-efficacite-protectionnisme', 'le28-mercantilisme',
          'le28-taille-pouvoir', 'le28-nouveaux-objectifs'}

pb = 0
for x in doss_base.DOSSIERS:
    if x['cle'] not in CIBLES:
        continue
    for a in x['aut']:
        n = socle.nz(a['n'])
        ref = mots(' '.join(FICHE.get(n, [])))
        voi = mots(voisinage(a['n']))
        idee = mots(a['i'])
        rf = len(idee & ref) / max(1, len(idee))
        rv = len(idee & voi) / max(1, len(idee))
        etat = 'ok' if max(rf, rv) >= 0.55 else ('a verifier' if max(rf, rv) >= 0.40 else 'SUSPECT')
        if etat != 'ok':
            pb += 1
        print('%-34s %-26s fiche %.2f  cours %.2f  %s'
              % (x['cle'], a['n'], rf, rv, etat))
        if etat != 'ok':
            print('      mots non retrouvés :', sorted(idee - ref - voi)[:14])
print()
print('attributions à revoir :', pb)
