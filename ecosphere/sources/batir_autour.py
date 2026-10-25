# -*- coding: utf-8 -*-
"""Assemble la charge de la section « Autour d'une notion ».

Pour chacun des dossiers prévus, on produit :
  - son identité (clé, ensemble, titre) ;
  - son état : rédigé, à venir, ou hors du champ couvert par les cours ;
  - ses liens, calculés à partir des contenus réellement présents dans
    l'application (chapitres, fiches, idées de l'Atlas, sujets) ;
  - son contenu lorsqu'il est rédigé.

Aucun lien ni aucune attribution n'est inventé : les liens proviennent de
liens.py, le contenu des modules doss*.py, eux-mêmes adossés aux cours.
"""
import json
import re
import unicodedata

import notions_liste
import liens
import doss_base
import glob as _glob
import importlib as _il

for _f in sorted(_glob.glob('doss[0-9][0-9]*.py')):
    _il.import_module(_f[:-3])

# correspondance entre le libellé de la liste et la clé du dossier rédigé
CLES = {
 "Libre-échange": "le28-libre-echange",
 "Arguments en faveur du libre-échange et conditions de validité": "le28-arguments-le",
 "Gains du commerce et répartition de ces gains": "le28-gains-repartition",
 "Coûts de l’ouverture et ajustements économiques et sociaux": "le28-couts-ouverture",
 "Ouverture commerciale progressive et maîtrisée": "le28-ouverture-progressive",
 "Protectionnisme": "le28-protectionnisme",
 "Protectionnisme éducateur et industries naissantes": "le28-educateur",
 "Protectionnisme défensif": "le28-defensif",
 "Protectionnisme offensif": "le28-offensif",
 "Protection des industries vieillissantes ou en déclin": "le28-vieillissantes",
 "Protectionnisme temporaire et protectionnisme permanent": "le28-temporaire-permanent",
 "Protectionnisme sélectif et protectionnisme généralisé": "le28-selectif-generalise",
 "Protectionnisme tarifaire : droits de douane": "le28-droits-douane",
 "Protectionnisme non tarifaire : quotas, licences, normes et procédures administratives":
     "le28-non-tarifaire",
 "Subventions à la production et aux exportations": "le28-subventions",
 "Politique commerciale stratégique": "le28-politique-strategique",
 "Protectionnisme agricole": "le28-agricole",
 "Protectionnisme environnemental": "le28-environnemental",
 "Protectionnisme social": "le28-social",
 "Marchés publics et préférence nationale": "le28-marches-publics",
 "Exigences de contenu local": "le28-contenu-local",
 "Dumping et mesures antidumping": "le28-dumping",
 "Mesures de sauvegarde": "le28-sauvegarde",
 "Réciprocité commerciale": "le28-reciprocite",
 "Représailles et guerres commerciales": "le28-representailles",
 "Détournement des échanges": "le28-detournement",
 "Coûts du protectionnisme pour les consommateurs et les entreprises utilisatrices de produits importés":
     "le28-couts-protectionnisme",
 "Recherche de rente et maintien artificiel d’activités inefficaces": "le28-rente",
 "Protection commerciale, sécurité économique et souveraineté": "le28-securite-souverainete",
}

# un même libellé peut figurer dans deux ensembles (« Libre-échange » en 16
# et en 28, « Rente » en 22 et en 27…). On indexe donc par (ensemble, libellé) ;
# les correspondances écrites à la main ci-dessus portent toutes sur l'ens. 28.
CLES = {(28, lib): cle for lib, cle in CLES.items()}

# Libellés dont le terme apparaît dans les cours, mais dans un sens étranger
# à la notion visée : le comptage automatique les classerait « à venir », ce
# qui laisserait croire qu'un dossier est possible. On les déclare hors-cours.
HORS_COURS = {
 (21, "Convergence européenne"):
     "la convergence des cours est celle de Solow, du rattrapage asiatique "
     "et de la « grande convergence » de Baldwin ; ni la convergence "
     "européenne ni les critères de Maastricht n'y figurent",
 (22, "Méritocratie"):
     "seul le terme « mérite » apparaît, dans l'analyse du mythe de "
     "l'entrepreneur par Galluzzo, et non une discussion de la méritocratie",
 (22, "Assurance et assistance"):
     "les cours ne construisent pas cette typologie de la protection "
     "sociale : « minima sociaux » et Beveridge en sont absents",
 (22, "Universalité et ciblage"):
     "le « ciblage » des cours est celui de la politique industrielle, non "
     "le ciblage des prestations sociales",
}

REDIGES = {x['cle']: x for x in doss_base.DOSSIERS}
assert len(REDIGES) == len(doss_base.DOSSIERS), 'clés de dossier en double'


def _nz(s):
    s = unicodedata.normalize('NFD', str(s or '')).lower()
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9 ]+', ' ', s.replace('\u2019', ' ')).strip()


def _rattacher():
    """Associe chaque dossier rédigé au libellé de la liste qu'il traite.

    Le rattachement se fait à l'intérieur d'un même ensemble, par similarité
    de titre. Les correspondances écrites à la main dans CLES l'emportent.
    """
    from difflib import SequenceMatcher
    pris = set(CLES.values())
    for x in doss_base.DOSSIERS:
        if x['cle'] in pris:
            continue
        cands = []
        for e in notions_liste.ENSEMBLES:
            if e['num'] != x['ens']:
                continue
            for lib in e['dossiers']:
                if (e['num'], lib) in CLES:
                    continue
                r = SequenceMatcher(None, _nz(x['titre']), _nz(lib)).ratio()
                cands.append((r, (e['num'], lib)))
        cands.sort(reverse=True)
        if cands and cands[0][0] >= 0.70:
            CLES[cands[0][1]] = x['cle']
            pris.add(x['cle'])
        else:
            raise SystemExit('dossier non rattaché : %s (%s)'
                             % (x['cle'], x['titre']))


_rattacher()


def slug(ens, titre):
    s = unicodedata.normalize('NFD', titre.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.replace('’', ' ').replace("'", ' ')
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return 'n%d-%s' % (ens, s[:48].rstrip('-'))


def batir():
    sortie = {'ensembles': [], 'dossiers': []}
    vus = set()
    for e in notions_liste.ENSEMBLES:
        sortie['ensembles'].append({'num': e['num'], 'titre': e['titre'],
                                    'questions': e['questions']})
        for titre in e['dossiers']:
            cle = CLES.get((e['num'], titre))
            redige = REDIGES.get(cle) if cle else None
            if cle is None or redige is None:
                cle = slug(e['num'], titre)
            # un même dossier peut servir plusieurs ensembles : on le rattache
            # au second sous forme de renvoi plutôt que de le dupliquer
            if cle in vus:
                sortie['dossiers'].append(
                    {'cle': '%s@%d' % (cle, e['num']), 'ens': e['num'],
                     'titre': titre, 'etat': 'renvoi', 'vers': cle,
                     'liens': {'ch': [], 'fi': [], 'at': [], 'su': [], 'au': []},
                     'poids': 0})
                continue
            vus.add(cle)

            L = liens.liens_de(titre)
            total = sum(c['n'] for c in L['ch'])
            if redige:
                etat = 'redige'
            elif total == 0 or (e['num'], titre) in HORS_COURS:
                etat = 'hors-cours'
            else:
                etat = 'a-venir'

            x = {'cle': cle, 'ens': e['num'], 'titre': titre, 'etat': etat,
                 'liens': L, 'poids': total}
            if redige:
                x.update({k: redige[k] for k in
                          ('court', 'defi', 'expl', 'mec', 'args', 'crit',
                           'aut', 'faits', 'diss', 'comp')})
                x['voisins'] = [CLE_PAR_DOSSIER[v] for v in redige['voisins']
                                if v in CLE_PAR_DOSSIER]
            sortie['dossiers'].append(x)
    return sortie


# les voisins sont écrits avec les clés des modules : on les garde telles quelles
CLE_PAR_DOSSIER = {c: c for c in REDIGES}

if __name__ == '__main__':
    data = batir()
    json.dump(data, open('autour_payload.json', 'w'), ensure_ascii=False)
    n = len(data['dossiers'])
    par_etat = {}
    for x in data['dossiers']:
        par_etat[x['etat']] = par_etat.get(x['etat'], 0) + 1
    print('dossiers        :', n)
    for k in ('redige', 'a-venir', 'hors-cours', 'renvoi'):
        print('  %-11s : %3d' % (k, par_etat.get(k, 0)))
    print('ensembles       :', len(data['ensembles']))
    print('questions       :', sum(len(e['questions']) for e in data['ensembles']))
    print('liens chapitres :', sum(len(x['liens']['ch']) for x in data['dossiers']))
    print('liens fiches    :', sum(len(x['liens']['fi']) for x in data['dossiers']))
    print('liens Atlas     :', sum(len(x['liens']['at']) for x in data['dossiers']))
    print('liens sujets    :', sum(len(x['liens']['su']) for x in data['dossiers']))
    print('taille charge   : %.2f Mo'
          % (len(json.dumps(data, ensure_ascii=False)) / 1048576))
