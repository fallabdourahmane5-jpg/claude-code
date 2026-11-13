# -*- coding: utf-8 -*-
"""Trie l'audit des familles pour obtenir une liste de manques relisible.

Une expression relevée dans les cours n'est un vrai manque que si :
  — elle n'est pas une troncature d'une notion déjà définie
    (« concurrence pure » dans « concurrence pure et parfaite ») ;
  — elle n'est pas une suite de mots du discours ;
  — elle est attestée ailleurs que dans une simple phrase du cours.
"""
import json
import re
from collections import defaultdict

import rech_base as R
from audit_familles import defs_existantes, mots_nz

FAIBLE = set("""augmente augmentent baisse baissent diminue diminuent devient
deviennent reste restent produire produit produisent cherche cherchent
permet permettent conduit conduisent entraine entrainent suppose supposent
davantage moins plus comme ainsi donc alors ensuite enfin aujourd hui
hui n est n ont c est il y a cela elles ils autre autres meme memes
general generale grand grande grands grandes petit petite certain certains
certaines nombreux premier premiere deuxieme troisieme dernier derniere
montee comportement capacite niveau partie ensemble exemple cas type forme
point element condition resultat situation question rapport sens role
fonction structure analyse approche theorie""".split())

# têtes qui ne portent pas de famille de notions
TETE_HORS = set("""union guerre monde annee annees siecle jour jours mois
pays etat etats entreprise entreprises travailleur travailleurs menage
menages banque banques personne personnes individu individus groupe groupes
auteur auteurs chapitre chapitres partie parties exemple exemples document
documents idee idees question questions reponse reponses montee baisse
hausse evolution variation augmentation diminution ensemble element elements
point points cas type types forme formes niveau niveaux fois nombre part
parts taille ordre suite serie liste total somme moyenne""".split())


def troncature(c, cles):
    """L'expression est-elle le début d'une notion déjà définie ?"""
    for k in cles:
        if k == c:
            return k
        if k.startswith(c + ' '):
            return k
        if (' ' + k + ' ').find(' ' + c + ' ') >= 0 and len(k.split()) > len(c.split()):
            return k
    return None


if __name__ == '__main__':
    FAM = json.load(open('audit_familles.json'))
    D = defs_existantes()
    CLES = set(D)
    # index par mot-tête pour ne pas balayer 2 465 clés à chaque fois
    par_tete = defaultdict(list)
    for k in CLES:
        m = k.split(' ')
        if m:
            par_tete[m[0]].append(k)

    garde, rejet = defaultdict(list), 0
    for tete, membres in FAM.items():
        if tete in TETE_HORS:
            continue
        for m in membres:
            if m['def']:
                continue
            c = m['cle']
            jet = c.split(' ')[1:]
            if not jet or all(w in FAIBLE for w in jet):
                rejet += 1
                continue
            if len(jet) == 1 and jet[0] in FAIBLE:
                rejet += 1
                continue
            t = troncature(c, par_tete.get(jet and c.split(' ')[0] or '', []))
            if t:
                m['tronque'] = D[t]['t'] if t in D else t
                rejet += 1
                continue
            # attestation : un intitulé ou un encadré, pas seulement une phrase
            if not ({'intitule', 'encadre', 'libelle'} & set(m['att'])):
                rejet += 1
                continue
            garde[tete].append(m)

    n = sum(len(v) for v in garde.values())
    print('manques retenus : %d (écartés : %d)' % (n, rejet))
    print('familles        : %d' % len(garde))
    print()
    ordre = sorted(garde.items(), key=lambda z: -sum(m['n'] for m in z[1]))
    for tete, membres in ordre:
        membres.sort(key=lambda z: -z['n'])
        print('### %s (%d)' % (tete, len(membres)))
        for m in membres[:14]:
            print('    %-42s %4d  ch %-24s [%s]'
                  % (m['e'][:42], m['n'], ','.join(m['ch'])[:24],
                     ','.join(m['att'])))
    json.dump({k: v for k, v in garde.items()},
              open('audit_manques.json', 'w'), ensure_ascii=False)
