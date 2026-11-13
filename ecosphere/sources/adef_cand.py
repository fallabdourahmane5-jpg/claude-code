# -*- coding: utf-8 -*-
"""Liste les notions à définir et rassemble le passage du cours qui les traite.

Une notion entre dans la liste lorsqu'elle nomme une section du cours, que le
texte du chapitre l'emploie plusieurs fois, et qu'aucune définition autonome
n'existe encore dans ÉcoSphère — fiches, notions de chapitre, blocs de
définition du cours ou dossiers d'« Autour d'une notion » compris.
"""
import json
import re

import rech_base as R
import socle
from manques import definitions_existantes

GEN = set("""demande offre production structure role fonction rapport question
relation sens flux stock solution mesure mesures difference differences
paradoxe probleme enjeu enjeux consequence consequences caractere
caracteristiques explication idee essentielle auteur auteurs exemple
exemples travail travailleur travailleurs revenu revenus service services
bien biens marche concurrence pays etat etats entreprise entreprises
population principe logique objectif constat limite limites critique
premier deuxieme troisieme quatrieme horizontal vertical court long terme
moyen nature type types forme formes niveau niveaux cas effet effets
politique politiques analyse analyses approche approches point points
element elements condition conditions resultat resultats situation
situations commun communs resume introduction generale problematique
siecle amelioration reduction engagement engagements""".split())

REJET = re.compile(
    r'^(points? communs?|resume de (ces|cette) parties?|introduction generale|'
    r'problematique generale|au xxe siecle|logique economique|le revenu|'
    r'les engagements|amelioration de l efficacite|reduction des inegalites|'
    r'une economie de marches financiers|deng xiaoping|'
    r'la western electric company|sous investissement|'
    r'nombre d heures travaillees|le nombre d heures travaillees|'
    r'main d oeuvre abondante|dependance de sentier)$')


def candidats(seuil=3):
    DEF = definitions_existantes()
    B = R.blocs()
    TXT = {k: R.nz(socle.TXT[k]) for k in R.ORDRE}
    out = {}
    for k in R.ORDRE:
        for i, x in enumerate(B[k]):
            if x['g'] not in ('h2', 'h3'):
                continue
            t = R.titre_propre(x['x'])
            if not R.est_notion(t):
                continue
            m = R.mots(t)
            if not (2 <= len(m) <= 6) or not any(len(w) >= 6 for w in m):
                continue
            if all(w in GEN for w in m):
                continue
            c = R.cle(t)
            if c in DEF or c in out or REJET.match(c):
                continue
            if TXT[k].count(R.nz(t)) < seuil:
                continue
            # le passage du cours : la section qui porte cet intitulé
            suite = []
            for y in B[k][i + 1:i + 14]:
                if y['g'] in ('h2', 'h3'):
                    break
                if len(y['x']) > 12:
                    suite.append(y['x'])
            out[c] = {'t': t, 'ch': k, 'n': TXT[k].count(R.nz(t)),
                      'pos': i, 'contexte': ' / '.join(suite)[:1500],
                      'chemin': x['p']}
    return out


if __name__ == '__main__':
    C = candidats()
    print('notions à définir : %d' % len(C))
    json.dump(C, open('adef_cand.json', 'w'), ensure_ascii=False)
    for c, v in sorted(C.items(), key=lambda z: (R.ORDRE.index(z[1]['ch']),
                                                 -z[1]['n'])):
        print('\n### [ch %s · %d occ.] %s' % (v['ch'], v['n'], v['t']))
        print('    %s' % v['contexte'][:900])
