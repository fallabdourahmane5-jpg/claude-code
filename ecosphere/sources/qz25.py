# -*- coding: utf-8 -*-
"""Chapitre 25 — Les modèles macroéconomiques et les politiques conjoncturelles.

Audit : 120 questions héritées, 18 sous-parties. Les corrigés étaient
développés mais aucune des 76 questions à choix multiple ne réfutait ses
distracteurs, aucune des 22 réponses rédigées n'avait de grille d'évaluation,
et 118 questions sur 120 étaient étiquetées « comprendre ». Dix questions
vrai/faux reformulant à l'identique un QCM de la même sous-partie sont
écartées, 110 questions sont corrigées et une banque nouvelle est ajoutée,
concentrée sur les sous-parties qui ne comptaient qu'une à cinq questions.
"""

SP = {
 'c25-01': "Modèles, idéal-type et comptabilité du PIB",
 'c25-02': "IS-LM, OG-DG et courbe de Phillips : les cadres disponibles",
 'c25-03': "L'équilibre de sous-emploi sur le marché des biens et services",
 'c25-04': "L'État dans le circuit et le multiplicateur de Kahn",
 'c25-05': "Les multiplicateurs : dépenses, transferts, impôts, ouverture",
 'c25-06': "Préférence pour la liquidité et rupture avec l'analyse classique",
 'c25-07': "La courbe LM, ses trois zones et l'effet d'éviction",
 'c25-08': "Politiques conjoncturelles, policy mix et procyclicité",
 'c25-09': "Réunification allemande, revenu permanent et éviction",
 'c25-10': "Les trois critiques de la relance et la réhabilitation d'IS-LM",
 'c25-11': "Du modèle fermé à Mundell-Fleming : la courbe BP",
 'c25-12': "Pente de BP, mobilité des capitaux et globalisation financière",
 'c25-13': "Changes fixes, défense de la parité et dilemmes de Généreux",
 'c25-14': "La relance de 1981, le tournant de 1983 et le cas japonais",
 'c25-15': "Changes fixes et mobilité parfaite : les deux politiques",
 'c25-16': "Changes flexibles et triangle des incompatibilités",
 'c25-17': "La zone euro : monnaie unique et budgets nationaux",
 'c25-18': "La règle d'affectation de Mundell et les quatre configurations",
}

# Questions supprimées : chacune reformulait en vrai/faux un QCM de la même
# sous-partie, sans apporter de contenu nouveau.
DROP = [
 'ch25-vraifa-78',   # doublon de ch25-qcm-42 (consommation autonome)
 'ch25-vraifa-79',   # doublon de ch25-qcm-8 (propension marginale à importer)
 'ch25-vraifa-80',   # doublon de ch25-qcm-6 (signe du multiplicateur fiscal)
 'ch25-vraifa-84',   # doublon de ch25-qcm-29 (budget en changes flexibles)
 'ch25-vraifa-85',   # doublon de ch25-qcm-23 (IS-LM et inflation)
 'ch25-vraifa-86',   # doublon de ch25-qcm-19 (courbe de Phillips originelle)
 'ch25-vraifa-89',   # doublon de ch25-qcm-53 (politique procyclique)
 'ch25-vraifa-90',   # doublon de ch25-qcm-26 (pente de BP)
 'ch25-vraifa-92',   # doublon de ch25-qcm-10 (motifs de détention de monnaie)
 'ch25-vraifa-95',   # doublon de ch25-qcm-38 (réhabilitation d'IS-LM)
]

from qz25f1 import FIX as _F1
from qz25f2 import FIX as _F2
from qz25f3 import FIX as _F3

FIX = dict(_F1)
FIX.update(_F2)
FIX.update(_F3)


# Éléments attendus pour les réponses rédigées héritées.
def k(f, l):
    return {'f': f, 'l': l}


CLES = {
 'ch25-questi-99': [
   k(['vague', 'successiv', 'circulation', '100'],
     "la circulation successive des revenus"),
   k(['0,8', '80', '64', 'propension marginale'],
     "80 puis 64 : chaque vague est réduite par la propension à épargner"),
   k(['epargne', 'fuite', '20'],
     "l'épargne est la fuite qui atténue le processus"),
   k(['1 / (1', 'multiplicateur', '5', 'somme'],
     "la somme des vagues donne le multiplicateur 1/(1 − c)"),
   k(['limite', 'capacite', 'importation', 'inflation', 'delai'],
     "limites : capacités de production, importations, délais")],
 'ch25-questi-100': [
   k(['kg', '1 / (1', '5', 'depense publique'],
     "kG = 1/(1 − c) = 5"),
   k(['kf', 'c / (1', '4', 'prestation', 'transfert'],
     "kF = c/(1 − c) = 4"),
   k(['kt', '- c', 'negatif', 'impot'],
     "kT = − c/(1 − c) = − 4"),
   k(['point d entree', 'immediat', 'premiere vague', 'circuit'],
     "la hiérarchie s'explique par le point d'entrée dans le circuit"),
   k(['hierarchie', 'superieur', 'plus eleve'],
     "d'où kG > kF > |kT|")],
 'ch25-questi-101': [
   k(['couple', 'offre', 'demande de monnaie', 'egalite'],
     "LM rassemble les couples (Y, r) équilibrant le marché de la monnaie"),
   k(['l1', 'transaction', 'precaution', 'positivement'],
     "L1 dépend positivement du revenu"),
   k(['l2', 'speculation', 'negativement', 'taux'],
     "L2 dépend négativement du taux d'intérêt"),
   k(['exogene', 'verticale', 'autorite monetaire'],
     "l'offre de monnaie est exogène"),
   k(['croissante', 'pente', 'positive'],
     "d'où une pente croissante"),
   k(['titre', 'obligation', 'prix', 'vend'],
     "l'ajustement passe par le marché des titres")],
 'ch25-questi-102': [
   k(['taux tres faible', 'plancher', 'anormalement bas'],
     "des taux d'intérêt très faibles"),
   k(['balancoire', 'remontee', 'perte en capital', 'prix des obligation'],
     "l'effet balançoire et l'anticipation d'une remontée des taux"),
   k(['demande speculative', 'infinie', 'thesauris', 'conserve'],
     "la demande spéculative de monnaie devient très élevée"),
   k(['lm horizontale', 'horizontale'],
     "LM devient horizontale"),
   k(['monetaire', 'inefficace', 'conventionnelle'],
     "la politique monétaire conventionnelle devient peu efficace"),
   k(['budgetaire', 'efficace', 'eviction'],
     "la politique budgétaire devient particulièrement efficace")],
 'ch25-questi-103': [
   k(['investissement prive', 'reduction', 'baisse'],
     "la réduction de l'investissement privé"),
   k(['taux d interet', 'hausse', 'r'],
     "provoquée par la hausse du taux d'intérêt"),
   k(['demande de monnaie', 'revenu', 'transaction'],
     "elle-même liée à la hausse de la demande de monnaie"),
   k(['pente', 'lm', 'sensibilite'],
     "déterminants : pente de LM et sensibilité de l'investissement au taux"),
   k(['trappe', 'nul', 'classique', 'total'],
     "éviction nulle dans la trappe, totale en zone classique")],
 'ch25-questi-104': [
   k(['bp horizontale', 'mobilite parfaite', 'r*'],
     "BP horizontale : le taux domestique doit rester aligné sur r*"),
   k(['lm droite', 'offre de monnaie', 'augmente'],
     "la hausse de l'offre de monnaie déplace LM vers la droite"),
   k(['r < r*', 'inferieur', 'sortie de capitaux'],
     "le taux devient inférieur au taux mondial et les capitaux sortent"),
   k(['depreciation', 'parite', 'defend', 'achete sa monnaie'],
     "la banque centrale défend la parité en achetant sa monnaie"),
   k(['masse monetaire', 'diminue', 'revient', 'annul'],
     "la masse monétaire diminue et LM revient à sa position initiale")],
 'ch25-questi-105': [
   k(['is droite', 'depense publique', 'demande globale'],
     "la relance déplace IS vers la droite"),
   k(['r > r*', 'superieur', 'taux monte'],
     "le taux d'intérêt dépasse le taux mondial"),
   k(['entree de capitaux', 'attractif', 'capitaux entrent'],
     "les capitaux entrent"),
   k(['appreciation', 'apprecie', 'change'],
     "la monnaie s'apprécie"),
   k(['exportation nette', 'competitivite', 'is revient'],
     "les exportations nettes diminuent et IS revient en arrière"),
   k(['eviction', 'taux de change'],
     "c'est l'effet d'éviction par le taux de change")],
 'ch25-questi-106': [
   k(['changes fixes', 'parite', 'incertitude'],
     "premier objectif : des changes fixes"),
   k(['mobilite', 'libre circulation', 'capitaux'],
     "deuxième objectif : la libre circulation des capitaux"),
   k(['autonomie monetaire', 'politique monetaire autonome'],
     "troisième objectif : une politique monétaire autonome"),
   k(['deux', 'trois', 'impossible', 'sacrifi'],
     "deux objectifs au maximum peuvent être conciliés"),
   k(['bretton woods', 'controle des capitaux'],
     "Bretton Woods sacrifie la mobilité des capitaux"),
   k(['flexible', 'flottement', 'euro', 'union monetaire'],
     "les autres combinaisons : changes flexibles, ou union monétaire")],
 'ch25-questi-107': [
   k(['1981', 'mauroy', 'smic', 'prestation', 'emploi public'],
     "la relance de mai 1981 et ses instruments"),
   k(['partenaire', 'faible', 'international', 'peu porteur'],
     "un environnement international peu porteur"),
   k(['inflation', '13', '12', 'elevee'],
     "une inflation française déjà élevée"),
   k(['importation', 'fuite', 'multiplicateur', 'etranger'],
     "une part du multiplicateur profite aux producteurs étrangers"),
   k(['deficit', 'exterieur', 'commerce', 'devaluation'],
     "la dégradation des comptes extérieurs"),
   k(['1983', 'rigueur', 'sme', 'franc'],
     "le tournant de mars 1983 et le maintien dans le SME")],
 'ch25-questi-108': [
   k(['eviction', 'taux d interet', 'investissement prive'],
     "première critique : l'effet d'éviction"),
   k(['friedman', 'revenu permanent', '1957', 'temporaire'],
     "deuxième critique : le revenu permanent de Friedman"),
   k(['barro', 'equivalence', 'ricardienne', '1974', 'impot futur'],
     "troisième critique : l'équivalence ricardienne de Barro"),
   k(['canal', 'different', 'distinguer'],
     "trois canaux différents, à ne pas confondre"),
   k(['marche monetaire', 'menage', 'anticipation'],
     "marché monétaire d'un côté, comportement des ménages de l'autre")],
 'ch25-questi-109': [
   k(['plein emploi', 'ype', 'potentiel', 'capacite'],
     "le point de départ : une économie au plein emploi"),
   k(['is', 'droite', 'depense publique'],
     "la relance déplace IS vers la droite"),
   k(['prix', 'tension', 'inflation', 'augmente'],
     "les prix augmentent"),
   k(['offre reelle', 'lm', 'gauche', 'm/p'],
     "l'offre réelle de monnaie diminue et LM se déplace vers la gauche"),
   k(['taux', 'eviction', 'investissement prive'],
     "le taux d'intérêt monte et évince l'investissement privé"),
   k(['retour', 'potentiel', 'inefficace'],
     "l'économie revient à son niveau potentiel")],
 'ch25-questi-110': [
   k(['prix fixe', 'rigidite', 'is-lm traditionnel'],
     "IS-LM raisonne à prix fixes"),
   k(['inflation', 'deflation', 'ne peut pas'],
     "il ne peut donc représenter l'inflation"),
   k(['stagflation', 'annees 1970', 'choc petrolier'],
     "or les années 1970 produisent la stagflation"),
   k(['phillips', 'arbitrage', 'remis en cause'],
     "l'arbitrage inflation-chômage ne permet pas de l'interpréter"),
   k(['og-dg', 'offre globale', 'demande globale', 'niveau general des prix'],
     "le modèle OG-DG réintroduit le niveau général des prix"),
   k(['choc d offre', 'gauche', 'production', 'prix'],
     "un choc d'offre négatif y réduit la production et élève les prix")],
 'ch25-questi-111': [
   k(['multiplicateur', 'affaibli', '1 / (1', 'm'],
     "l'affaiblissement du multiplicateur par la propension à importer"),
   k(['5', '2', 'passe de'],
     "dans l'exemple du cours, il passe de 5 à 2"),
   k(['interdependance', 'partenaire', 'coordination', 'relance commune'],
     "l'interdépendance et l'intérêt d'une coordination"),
   k(['contrainte exterieure', 'deficit', 'balance', 'change'],
     "la contrainte extérieure et le solde commercial"),
   k(['1981', 'france', 'exemple'],
     "l'exemple de la relance française de 1981")],
 'ch25-questi-112': [
   k(['sous-emploi', 'excedent', 'pas de dilemme', 'compatible'],
     "sous-emploi et excédent : pas de dilemme"),
   k(['sous-emploi', 'deficit', 'dilemme'],
     "sous-emploi et déficit : dilemme"),
   k(['inflation', 'excedent', 'dilemme'],
     "inflation et excédent : dilemme"),
   k(['inflation', 'deficit', 'pas de dilemme', 'restrictive'],
     "inflation et déficit : pas de dilemme"),
   k(['interne', 'externe', 'aggrave', 'corrige'],
     "le critère : la politique qui corrige l'interne aggrave-t-elle "
     "l'externe ?"),
   k(['affectation', 'mundell', 'deux instrument'],
     "d'où l'intérêt de la règle d'affectation de Mundell")],
 'ch25-questi-113': [
   k(['unique', 'bce', 'commune', 'monetaire'],
     "une politique monétaire unique, conduite par la BCE"),
   k(['budgetaire', 'national', 'etat membre'],
     "des politiques budgétaires demeurées nationales"),
   k(['asymetrie', 'dissymetrie', 'particuliere'],
     "une asymétrie institutionnelle"),
   k(['maastricht', '3 %', '60 %', 'pacte de stabilite'],
     "un encadrement par les critères de Maastricht et le Pacte"),
   k(['budget europeen', '1 %', 'federal', 'stabilisation'],
     "un budget européen d'environ 1 % du RNB, trop faible pour stabiliser"),
   k(['coordination', 'divergence', 'policy mix'],
     "d'où un problème de coordination du policy mix")],
 'ch25-questi-114': [
   k(['couple', 'balance globale', 'equilibre'],
     "BP rassemble les couples assurant l'équilibre de la balance globale"),
   k(['revenu', 'importation', 'solde courant', 'degrade'],
     "une hausse du revenu dégrade le solde courant"),
   k(['attirer', 'capitaux', 'taux', 'r'],
     "il faut attirer des capitaux, donc élever le taux"),
   k(['mobilite', 'forte', 'faible', 'sensibilite'],
     "la pente dépend de la sensibilité des capitaux au taux"),
   k(['horizontale', 'parfaite', 'verticale', 'nulle'],
     "horizontale si mobilité parfaite, verticale si mobilité nulle")],
 'ch25-questi-115': [
   k(['abstrait', 'simplifi', 'hypothese', 'representation'],
     "un modèle est une représentation abstraite construite sur des hypothèses"),
   k(['isoler', 'relation', 'expliquer', 'mecanisme'],
     "il isole certaines relations pour en expliquer le fonctionnement"),
   k(['pertinence', 'cadre', 'pas le realisme', 'descriptif'],
     "sa pertinence ne tient pas à son réalisme descriptif"),
   k(['concurrence pure', 'ideal-type', 'weber'],
     "la concurrence pure et parfaite comme idéal-type au sens de Weber"),
   k(['harrod', 'domar', 'solow', 'conclusion', 'depend'],
     "Harrod-Domar et Solow : les conclusions dépendent des hypothèses")],
 'ch25-questi-116': [
   k(['pigou', 'neoclassique', 'marche du travail'],
     "l'analyse néoclassique du marché du travail"),
   k(['salaire reel', 'offre', 'demande', 'equilibre'],
     "offre et demande de travail déterminent un salaire d'équilibre"),
   k(['rigidite', 'trop eleve', 'volontaire', 'flexibilite'],
     "le chômage résulte d'un salaire réel trop élevé"),
   k(['demande effective', 'anticip', 'entrepreneur'],
     "chez Keynes, la demande effective détermine la production"),
   k(['involontaire', 'sous-emploi', 'debouche'],
     "le chômage devient involontaire"),
   k(['relance', 'demande globale', 'politique'],
     "d'où un remède par la demande et non par les salaires")],
 'ch25-questi-117': [
   k(['anticipation', 'demande anticipee', 'debouche'],
     "l'investissement dépend de la demande anticipée"),
   k(['recession', 'incertitude', 'report', 'pessimiste'],
     "en récession, les projets sont reportés"),
   k(['revenu', 'baisse', 'consommation', 'demande'],
     "la demande baisse, ce qui valide les anticipations"),
   k(['autoreal', 'cumulatif', 'cercle', 'spirale'],
     "les anticipations deviennent autoréalisatrices"),
   k(['sous-emploi', 'equilibre', 'durable', 'piege'],
     "l'économie s'installe dans un équilibre de sous-emploi"),
   k(['etat', 'relance', 'rompre', 'public'],
     "d'où la nécessité d'une impulsion extérieure, notamment publique")],
 'ch25-questi-118': [
   k(['conjoncturelle', 'court terme', 'demande globale'],
     "la politique conjoncturelle agit à court terme sur la demande"),
   k(['structurelle', 'durablement', 'offre', 'capacite'],
     "la politique structurelle agit durablement sur l'offre"),
   k(['formation', 'innovation', 'infrastructure', 'marche'],
     "ses instruments : formation, innovation, infrastructures, marchés"),
   k(['eviction', 'revenu permanent', 'equivalence', 'critique'],
     "les critiques limitent l'efficacité de la relance de demande"),
   k(['potentielle', 'croissance potentielle', 'romer', 'naturel'],
     "d'où un déplacement vers la croissance potentielle")],
 'ch25-questi-119': [
   k(['is-lm', 'ferme', 'demande', 'eviction', 'trappe'],
     "IS-LM : les politiques de demande en économie fermée"),
   k(['og-dg', 'prix', 'inflation', 'choc d offre', 'stagflation'],
     "OG-DG : le niveau général des prix et les chocs d'offre"),
   k(['is-lm-bp', 'ouverte', 'change', 'mundell', 'capitaux'],
     "IS-LM-BP : l'économie ouverte et les régimes de change"),
   k(['question', 'dimension', 'complementaire', 'chacun'],
     "chacun répond à une question propre"),
   k(['aucun modele', 'toutes les situations', 'ensemble'],
     "aucun modèle ne suffit à lui seul")],
 'ch25-questi-120': [
   k(['statique', 'rigidite', 'prix fixe', 'plein emploi'],
     "un modèle statique à prix rigides"),
   k(['anticipation', 'credibilite', 'agent', 'absente'],
     "l'absence des anticipations des agents"),
   k(['mobilite parfaite', 'extreme', 'cas limite', 'simplifi'],
     "des hypothèses de mobilité des capitaux très simplifiées"),
   k(['dette', 'solvabilite', 'finance', 'bilan'],
     "l'absence des contraintes financières et de la dette"),
   k(['utile', 'pedagogique', 'cadre', 'raisonnement'],
     "malgré ces limites, un cadre de raisonnement utile")],
}

# Les corrigés rédigés d'origine sont conservés comme réponses modèles.
for _id, _c in CLES.items():
    FIX[_id]['ans'] = {'cles': _c}

from qz25n1 import L as _N1
from qz25n2 import L as _N2

NEW = _N1 + _N2
