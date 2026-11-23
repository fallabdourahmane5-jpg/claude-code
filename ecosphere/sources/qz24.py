# -*- coding: utf-8 -*-
"""Chapitre 24 — La gouvernance mondiale du commerce et ses recompositions.

Audit : 142 questions héritées, 16 sous-parties. Les corrigés étaient
développés mais aucune des 98 questions à choix multiple ne réfutait ses
distracteurs, aucune des 22 réponses rédigées n'avait de grille d'évaluation,
et 138 questions sur 142 étaient étiquetées « comprendre ». Quatorze questions
vrai/faux reformulant à l'identique un QCM de la même sous-partie sont
écartées, 128 questions sont corrigées et une banque nouvelle est ajoutée,
concentrée sur la sous-partie consacrée au bilan des rounds, qui ne comptait
que deux questions.
"""

SP = {
 'c24-01': "Acteurs de la mondialisation, doux commerce et géoéconomie",
 'c24-02': "Biens publics mondiaux et nécessité d'une gouvernance",
 'c24-03': "Stabilité hégémonique et naissance de l'ordre commercial de 1945",
 'c24-04': "Les trois principes du GATT et leurs exceptions",
 'c24-05': "Sauvegardes, subventions et règlement des différends",
 'c24-06': "L'exception agricole et ses effets sur les pays en développement",
 'c24-07': "Les cycles de négociation, de Genève à l'enlisement de Doha",
 'c24-08': "Le bilan des rounds : ce que la libéralisation explique vraiment",
 'c24-09': "Accords régionaux et typologie de Balassa",
 'c24-10': "Viner : création et détournement de trafic",
 'c24-11': "Accords profonds, bol de spaghettis et effet domino",
 'c24-12': "Une gouvernance hybride : États, firmes, G20, société civile",
 'c24-13': "Le trilemme de Rodrik et la base sociale du rejet",
 'c24-14': "Le coût mesuré de la fragmentation géoéconomique",
 'c24-15': "Climat, simulations de l'OMC et puissance normative européenne",
 'c24-16': "Crise d'hégémonie et avenirs possibles de la gouvernance",
}

# Questions supprimées : chacune reformulait en vrai/faux un QCM de la même
# sous-partie, sans apporter de contenu nouveau.
DROP = [
 'ch24-vraifa-99',    # doublon de ch24-qcm-26 (le GATT n'est pas une organisation)
 'ch24-vraifa-102',   # doublon de ch24-qcm-36 (catégorie verte de l'Accord SMC)
 'ch24-vraifa-103',   # doublon de ch24-qcm-34 (conditions d'une sauvegarde)
 'ch24-vraifa-104',   # doublon de ch24-qcm-54 (zone de libre-échange / union douanière)
 'ch24-vraifa-105',   # doublon de ch24-qcm-59 (hausse du commerce intra-zone)
 'ch24-vraifa-107',   # doublon de ch24-qcm-51 (décomposition Findlay et O'Rourke)
 'ch24-vraifa-108',   # doublon de ch24-qcm-33 (statut chinois à l'OMC)
 'ch24-vraifa-111',   # doublon de ch24-qcm-10 (mécanisme du doux commerce)
 'ch24-vraifa-112',   # doublon de ch24-qcm-76 (trilemme de Rodrik)
 'ch24-vraifa-113',   # doublon de ch24-qcm-38 (protection agricole comparée)
 'ch24-vraifa-114',   # doublon de ch24-qcm-41 (groupe de Cairns)
 'ch24-vraifa-118',   # doublon de ch24-qcm-64 (intégration profonde)
 'ch24-vraifa-119',   # doublon de ch24-qcm-18 (propriétés d'un bien public mondial)
 'ch24-vraifa-120',   # doublon de ch24-qcm-84 (simulations de l'OMC)
]

from qz24f1 import FIX as _F1
from qz24f2 import FIX as _F2
from qz24f3 import FIX as _F3
from qz24f4 import FIX as _F4

FIX = dict(_F1)
for _d in (_F2, _F3, _F4):
    FIX.update(_d)


# Éléments attendus pour les réponses rédigées héritées.
def k(f, l):
    return {'f': f, 'l': l}


CLES = {
 'ch24-questi-121': [
   k(['consensus', 'annees 1990', 'prosperite', 'pacification'],
     "un consensus initial associant ouverture, prospérité et pacification"),
   k(['montesquieu', 'doux commerce', 'interdependance', 'ceca'],
     "la lecture de Montesquieu et la CECA de 1951"),
   k(['inegalite', 'perdant', 'distributif', 'territoire'],
     "la visibilité croissante des coûts distributifs"),
   k(['dependance', 'vulnerabilite', 'penurie', 'crise'],
     "la révélation des dépendances et des vulnérabilités"),
   k(['geopolitique', 'rivalite', 'puissance', 'luttwak'],
     "le retour des rivalités de puissance")],
 'ch24-questi-122': [
   k(['non rival', 'non-rival', 'rivalite'],
     "un bien public mondial est non rival"),
   k(['exclu', 'excluable', 'exclusion'],
     "et non excluable"),
   k(['climat', 'biodiversite', 'stabilite financiere', 'regle'],
     "exemples : climat, stabilité financière, règles commerciales"),
   k(['passager clandestin', 'free rider', 'laisser les autres'],
     "d'où un comportement de passager clandestin"),
   k(['nash', 'sous-optimal', 'sous produit', 'coordination'],
     "un équilibre sous-optimal, d'où la nécessité d'une coordination")],
 'ch24-questi-123': [
   k(['kindleberger', '1973', '1981', 'grande depression'],
     "la théorie de Kindleberger"),
   k(['puissance dominante', 'hegemon', 'responsabilite'],
     "une puissance dominante assumant des responsabilités collectives"),
   k(['monetaire', 'commercial', 'liquidite', 'cooperation'],
     "système monétaire, cadre commercial ouvert, liquidités, coopération"),
   k(['passager clandestin', 'tente', 'financer'],
     "chacun est tenté de laisser les autres financer ces biens"),
   k(['60', '70', 'or', 'production mondiale'],
     "la position américaine de 1945 : environ 60 % de la production, 70 % de l'or"),
   k(['bretton woods', 'gatt', 'marshall', 'reconstruction'],
     "Bretton Woods, le GATT et la reconstruction")],
 'ch24-questi-124': [
   k(['importation', 'gain', 'ricardo', 'hos'],
     "dans la théorie, l'importation est le gain de l'échange"),
   k(['exportation', 'concession', 'politiquement', 'inverse'],
     "dans la négociation, les exportations sont un gain et les importations une concession"),
   k(['krugman', 'mercantilisme eclaire'],
     "Krugman nomme cette logique mercantilisme éclairé"),
   k(['reciprocite', 'donnant-donnant', 'contrepartie'],
     "la réciprocité transforme ce raisonnement en moteur de libéralisation"),
   k(['paradoxe', 'abaisse', 'resultat', 'liberalisation'],
     "le paradoxe : un raisonnement erroné produit la libéralisation")],
 'ch24-questi-125': [
   k(['nation la plus favorisee', 'npf', 'article i'],
     "la clause de la nation la plus favorisée (article I)"),
   k(['traitement national', 'article iii'],
     "le traitement national (article III)"),
   k(['reciprocite', 'contrepartie', 'acceptable'],
     "la réciprocité"),
   k(['transparence', 'mesurable', 'negociable', 'tarif'],
     "la transparence, qui privilégie les instruments mesurables"),
   k(['exception', 'sauvegarde', 'article xxiv', 'sgp', 'encadr'],
     "les exceptions sont encadrées et temporaires, donc non contradictoires")],
 'ch24-questi-126': [
   k(['15,9', '3 %', 'droit de douane moyen'],
     "15,9 % dans l'agriculture contre environ 3 % dans l'industrie"),
   k(['securite alimentaire', 'revenu agricole', 'rural', 'souverainete'],
     "sécurité alimentaire, revenus agricoles, territoires ruraux, souveraineté"),
   k(['volatilite', 'prix mondiaux', 'instabilite'],
     "la protection contre la volatilité des prix mondiaux"),
   k(['1933', 'adjustment act', 'new deal', 'pac', '1962'],
     "une protection ancienne : 1933 aux États-Unis, 1962 avec la PAC"),
   k(['cairns', 'doha', 'subvention', 'coton'],
     "les contestations : groupe de Cairns, Doha, coton américain")],
 'ch24-questi-127': [
   k(['arachide', '40', 'terre cultivee'],
     "l'arachide jusqu'à 40 % des terres cultivées"),
   k(['exportation', 'vivriere', 'diversification'],
     "au détriment des cultures vivrières et de la diversification"),
   k(['securite alimentaire', 'sol', 'appauvri'],
     "des effets sur la sécurité alimentaire et les sols"),
   k(['emeute', '2007', '2008', 'tournant'],
     "les émeutes de la faim de 2007-2008 comme tournant"),
   k(['riz', 'riziculture', 'mil', 'diversifier'],
     "la riziculture puis la diversification vers le mil, les fruits et légumes")],
 'ch24-questi-128': [
   k(['geneve', '1947', '23'],
     "Genève 1947, 23 participants"),
   k(['annecy', 'torquay', '1949', '1951'],
     "Annecy 1949 et Torquay 1951"),
   k(['kennedy', '1964', '1967', '48', 'antidumping'],
     "le Kennedy Round (1964-1967), 48 participants, premier code antidumping"),
   k(['tokyo', '1973', '1979', '99', 'non tarifaire'],
     "le Tokyo Round (1973-1979), 99 participants, obstacles non tarifaires"),
   k(['uruguay', '1986', '1994', '123', 'omc'],
     "l'Uruguay Round, 123 participants à la conclusion, création de l'OMC"),
   k(['doha', '2001', 'enlis', 'echec'],
     "le cycle de Doha et son enlisement")],
 'ch24-questi-129': [
   k(['developpement', 'ped', 'acces au marche'],
     "un cycle présenté comme un cycle pour le développement"),
   k(['21', 'tres large', 'nombreux sujet', 'agriculture'],
     "un programme très large, souvent présenté comme 21 thèmes"),
   k(['engagement unique', 'rien n est convenu', 'tout'],
     "le principe de l'engagement unique"),
   k(['blocage', 'consensus', 'nombre de membre', 'divergence'],
     "la multiplication des possibilités de blocage"),
   k(['2015', '2016', 'impasse', 'sectoriel'],
     "l'impasse confirmée en 2015-2016, malgré des accords plus limités")],
 'ch24-questi-130': [
   k(['40', '3', '4', 'droit de douane'],
     "une réduction spectaculaire des droits de douane"),
   k(['23', '123', '166', 'elargissement', 'chine'],
     "un élargissement considérable, de 23 pays à 166 membres"),
   k(['dumping', 'subvention', 'service', 'propriete intellectuelle',
      'domaine'],
     "une extension des domaines régulés"),
   k(['doha', 'enlisement', 'blocage'],
     "limite : l'enlisement des négociations globales"),
   k(['organe de reglement', 'differend', 'affaibli', 'unilateral'],
     "limite : l'affaiblissement du règlement des différends"),
   k(['agriculture', 'exception', 'ped', 'asymetrie'],
     "limite : exceptions sectorielles et asymétries persistantes")],
 'ch24-questi-131': [
   k(['zone de libre-echange', 'libre echange', 'droit interne'],
     "la zone de libre-échange supprime les droits internes"),
   k(['regle d origine', 'origine'],
     "d'où l'importance des règles d'origine"),
   k(['union douaniere', 'tarif exterieur commun'],
     "l'union douanière ajoute un tarif extérieur commun"),
   k(['marche commun', 'facteur', 'circulation'],
     "le marché commun libère la circulation des facteurs"),
   k(['union economique', 'monetaire', 'politique'],
     "l'union économique et monétaire coordonne les politiques"),
   k(['integration totale', 'supranational'],
     "l'intégration totale unifie les politiques sous une autorité supranationale")],
 'ch24-questi-132': [
   k(['viner', '1950'],
     "l'analyse de Viner (1950)"),
   k(['creation de trafic', 'production domestique', 'moins chere'],
     "la création de trafic améliore le bien-être"),
   k(['detournement', 'fournisseur', 'moins efficace', 'preference tarifaire'],
     "le détournement de trafic le dégrade"),
   k(['comparer', 'emporte', 'solde', 'bilan'],
     "il faut comparer les deux effets"),
   k(['intra-zone', 'ne prouve', 'insuffisant'],
     "la hausse du commerce intra-zone ne prouve rien")],
 'ch24-questi-133': [
   k(['eloigne', 'geographique', 'canada', 'vietnam', 'mercosur'],
     "des accords reliant des économies géographiquement éloignées"),
   k(['lawrence', 'superficielle', 'profonde'],
     "la distinction de Lawrence entre intégration superficielle et profonde"),
   k(['norme', 'social', 'environnement', 'travail', 'concurrence'],
     "des domaines qui dépassent le commerce : normes, travail, concurrence"),
   k(['investissement', 'propriete intellectuelle', 'marche public'],
     "investissements, propriété intellectuelle, marchés publics"),
   k(['diffusion', 'normatif', 'instrument', 'puissance'],
     "les accords deviennent des instruments de diffusion normative")],
 'ch24-questi-134': [
   k(['bhagwati', '1995'],
     "l'image de Bhagwati (1995)"),
   k(['propre regle', 'droit', 'regle d origine', 'exception',
      'superpos'],
     "chaque accord fixe ses propres règles, qui se superposent"),
   k(['baldwin', '2008', 'amerique latine'],
     "l'illustration de Baldwin (2008) sur l'Amérique latine"),
   k(['cout', 'complexite', 'administratif', 'entreprise'],
     "un coût de complexité pour les entreprises"),
   k(['discrimination', 'efficacite', 'transparence', 'npf'],
     "une perte de transparence et de non-discrimination")],
 'ch24-questi-135': [
   k(['aucune institution unique', 'plusieurs acteur', 'multiple'],
     "aucune institution unique ne produit plus les règles"),
   k(['omc', 'etat', 'acr', 'firme', 'g20'],
     "OMC, États, accords régionaux, firmes, G7 et G20"),
   k(['doha', 'echec', 'blocage'],
     "l'échec de Doha prive l'OMC de sa capacité normative"),
   k(['acr', 'multiplication', 'preferentiel'],
     "la multiplication des accords préférentiels"),
   k(['contradictoire', 'incoherence', 'concurrence des regles'],
     "des règles potentiellement contradictoires")],
 'ch24-questi-136': [
   k(['hypermondialisation', 'democratie', 'souverainete'],
     "les trois termes du trilemme"),
   k(['deux', 'jamais les trois', 'impossible'],
     "on peut en conserver deux, jamais les trois"),
   k(['bretton woods', 'compromis', 'limiter'],
     "souveraineté et démocratie : le compromis de Bretton Woods"),
   k(['camisole', 'doree', 'marche', 'contrainte'],
     "hypermondialisation et souveraineté : la camisole dorée"),
   k(['supranational', 'gouvernance', 'federal'],
     "démocratie et hypermondialisation : une gouvernance supranationale")],
 'ch24-questi-137': [
   k(['pib par habitant', 'revenu median', 'diverg'],
     "la divergence entre PIB par habitant et revenu médian"),
   k(['etats-unis', '1984', '1980'],
     "le cas américain depuis les années 1980"),
   k(['haut de la distribution', 'concentr', 'inegalite'],
     "une concentration des gains vers le haut de la distribution"),
   k(['france', '10 %', 'median', 'modere'],
     "le cas français : progression inégale des niveaux de vie"),
   k(['rejet', 'politique', 'vote', 'protection'],
     "d'où une base sociale au rejet de l'hypermondialisation")],
 'ch24-questi-138': [
   k(['continuite', 'tension', 'exception', 'omc reste'],
     "premier scénario : la continuité sous tensions"),
   k(['guerre froide', 'decouplage', 'friend', 'bloc'],
     "deuxième scénario : la guerre froide économique"),
   k(['recomposition', 'reforme', 'plurilateral', 'nouvelle'],
     "troisième scénario : une recomposition du multilatéralisme"),
   k(['strategique', 'chaine de valeur', 'reorganis'],
     "des degrés différents de réorganisation des chaînes de valeur"),
   k(['pays tiers', 'choisir', 'pression', 'camp'],
     "des pressions croissantes sur les pays tiers")],
 'ch24-questi-139': [
   k(['bolhuis', 'chen', 'kett', 'fmi', '2023'],
     "les estimations de Bolhuis, Chen et Kett (FMI, 2023)"),
   k(['0,3', 'decouplage', 'limite', 'strategique'],
     "un découplage stratégique limité : environ 0,3 % du PIB mondial"),
   k(['2,3', 'deux bloc', 'complete'],
     "une fragmentation complète en deux blocs : environ 2,3 %"),
   k(['7', 'brutale', 'transition'],
     "jusqu'à 7 % en cas de transition très brutale"),
   k(['faible revenu', 'pauvre', 'inegal', 'vulnerable'],
     "des pertes concentrées sur les pays à faible revenu")],
 'ch24-questi-140': [
   k(['non rival', 'excluable', 'bien public'],
     "la stabilité climatique est un bien public mondial"),
   k(['passager clandestin', 'laisser les autres', 'incitation'],
     "exposé au comportement de passager clandestin"),
   k(['cout national', 'benefice mondial', 'asymetrie'],
     "coût national, bénéfice mondial"),
   k(['macf', 'carbone', 'frontiere', 'seqe'],
     "le MACF comme réponse européenne"),
   k(['normative', 'marche', '450', 'norme'],
     "la puissance normative européenne et la taille de son marché")],
 'ch24-questi-141': [
   k(['kindleberger', 'puissance', 'legitimite'],
     "les deux conditions de Kindleberger : puissance et légitimité"),
   k(['1945', 'etats-unis', 'reunissaient', 'debouche'],
     "après 1945, les États-Unis réunissaient les deux"),
   k(['recul', 'relative', 'remettent en cause', 'unilateral'],
     "aujourd'hui leur puissance relative recule et ils contestent les règles"),
   k(['chine', 'contestee', 'legitimite', 'bienveillant'],
     "la Chine a la puissance mais une légitimité contestée"),
   k(['europe', 'normative', 'geopolitique', 'limitee'],
     "l'Union a la légitimité réglementaire mais une puissance limitée"),
   k(['sectoriel', 'plusieurs niveau', 'partage', 'issue'],
     "issue possible : plusieurs leaderships sectoriels")],
 'ch24-questi-142': [
   k(['souverainete', 'efficacite', 'arbitrage'],
     "un arbitrage entre souveraineté et efficacité"),
   k(['raccourcir', 'chaine de valeur', 'resilience'],
     "raccourcir les chaînes accroît la résilience"),
   k(['cout', 'prix', 'production'],
     "mais élève les coûts de production et les prix"),
   k(['rodrik', 'trilemme', 'democratie'],
     "le trilemme de Rodrik comme formulation politique du même arbitrage"),
   k(['societe civile', 'accepter', 'acceptabilite', 'politique'],
     "la question de l'acceptation sociale du coût de la souveraineté")],
}

# Les corrigés rédigés d'origine sont conservés comme réponses modèles.
for _id, _c in CLES.items():
    FIX[_id]['ans'] = {'cles': _c}

from qz24n1 import L as _N1
from qz24n2 import L as _N2

NEW = _N1 + _N2
