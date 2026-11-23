# -*- coding: utf-8 -*-
"""Chapitre 26 — Taux de change, régimes de change et politiques monétaires.

Audit : 140 questions héritées, 16 sous-parties. Les corrigés étaient
développés mais aucune des 97 questions à choix multiple ne réfutait ses
distracteurs, aucune des 16 réponses rédigées n'avait de grille d'évaluation,
et 135 questions sur 140 étaient étiquetées « comprendre ». Vingt-et-une
questions vrai/faux reformulant à l'identique un QCM de la même sous-partie
sont écartées, 119 questions sont corrigées et une banque nouvelle est
ajoutée, concentrée sur les sous-parties qui ne comptaient que trois à sept
questions.
"""

SP = {
 'c26-01': "Monnaie, devise et les trois mesures du taux de change",
 'c26-02': "Le marché des changes : un marché-réseau dominé par le dollar",
 'c26-03': "Comptant, terme, couverture et spéculation",
 'c26-04': "Déterminants du change : PPA, Cassel et effet Balassa-Samuelson",
 'c26-05': "La typologie des régimes de change, de la dollarisation au flottement",
 'c26-06': "Interventions en changes flottants : Plaza, Louvre et régimes en 2025",
 'c26-07': "Friedman et les quatre arguments flexibilistes, et leurs limites",
 'c26-08': "Pétrodollars, choc Volcker, crise de la dette et peur du flottement",
 'c26-09': "Le triangle de Mundell et la lecture historique de Jean-Marc Daniel",
 'c26-10': "Les instruments de la politique de change et la guerre des monnaies",
 'c26-11': "Marshall-Lerner, courbe en J et conditions d'une dévaluation",
 'c26-12': "Le cercle vicieux de la monnaie faible et la séquence française 1981-1983",
 'c26-13': "La désinflation compétitive et le théorème de Schmidt",
 'c26-14': "Levier, massue et bilan contrasté du franc fort",
 'c26-15': "Existe-t-il un bon taux de change ? Doctrine Miran et Mar-a-Lago",
 'c26-16': "Rôle d'assurance du dollar, stablecoins et monnaies numériques",
}

# Questions supprimées : chacune reformulait en vrai/faux un QCM de la même
# sous-partie, sans apporter de contenu nouveau.
DROP = [
 'ch26-vraifa-98',    # doublon de ch26-qcm-7 (dévaluation / dépréciation)
 'ch26-vraifa-99',    # doublon de ch26-qcm-5 (taux de change effectif)
 'ch26-vraifa-101',   # doublon de ch26-qcm-16 (Cassel, 1918)
 'ch26-vraifa-102',   # doublon de ch26-qcm-20 (effet Balassa-Samuelson)
 'ch26-vraifa-103',   # doublon de ch26-qcm-22 (continuum des régimes)
 'ch26-vraifa-104',   # doublon de ch26-qcm-32 et -33 (régimes en 2025)
 'ch26-vraifa-106',   # doublon de ch26-qcm-57 (asymétrie des interventions)
 'ch26-vraifa-107',   # doublon de ch26-qcm-37 (choc Volcker)
 'ch26-vraifa-108',   # doublon de ch26-qcm-39 (recyclage des pétrodollars)
 'ch26-vraifa-109',   # doublon de ch26-qcm-42 (crise mexicaine de 1982)
 'ch26-vraifa-110',   # doublon de ch26-qcm-46 (triangle de Mundell)
 'ch26-vraifa-111',   # doublon de ch26-qcm-52 (choix de la zone euro)
 'ch26-vraifa-112',   # doublon de ch26-qcm-54 (guerre des monnaies)
 'ch26-vraifa-113',   # doublon de ch26-qcm-55 (accusation de sous-évaluation)
 'ch26-vraifa-114',   # doublon de ch26-qcm-59 (condition de Marshall-Lerner)
 'ch26-vraifa-115',   # doublon de ch26-qcm-62 (courbe en J)
 'ch26-vraifa-116',   # doublon de ch26-qcm-63 (compétitivité hors prix)
 'ch26-vraifa-118',   # doublon de ch26-qcm-75 (taux de marge 1985-1989)
 'ch26-vraifa-120',   # doublon de ch26-qcm-78 (taux d'intérêt réel)
 'ch26-vraifa-122',   # doublon de ch26-qcm-86 (nuance du bilan)
 'ch26-vraifa-124',   # doublon de ch26-qcm-92 (accords de Mar-a-Lago)
]

from qz26f1 import FIX as _F1
from qz26f2 import FIX as _F2
from qz26f3 import FIX as _F3

FIX = dict(_F1)
FIX.update(_F2)
FIX.update(_F3)


# Éléments attendus pour les réponses rédigées héritées.
def k(f, l):
    return {'f': f, 'l': l}


CLES = {
 'ch26-questi-125': [
   k(['bilateral', 'deux monnaie', 'nominal'],
     "le taux nominal bilatéral mesure la valeur relative de deux monnaies"),
   k(['certain', 'incertain', 'cotation'],
     "cotations au certain et à l'incertain"),
   k(['effectif', 'moyenne ponderee', 'multilateral', 'partenaire'],
     "le taux effectif est une moyenne pondérée multilatérale"),
   k(['reel', 'prix', 'inflation', 'competitivite'],
     "le taux réel corrige par les niveaux de prix et mesure la compétitivité"),
   k(['limite', 'une seule relation', 'ensemble'],
     "limite du bilatéral : il ne décrit qu'une relation")],
 'ch26-questi-126': [
   k(['plihon', 'marche-reseau', 'reseau', 'electronique'],
     "un marché-réseau au sens de Plihon"),
   k(['couverture', 'risque', 'reduire'],
     "la couverture réduit l'exposition au risque de change"),
   k(['speculation', 'accepte', 'gain'],
     "la spéculation accepte le risque en espérant un gain"),
   k(['retour a la moyenne', 'sous-evaluee', 'surevaluee', 'calme'],
     "en période calme, les anticipations de retour à la moyenne stabilisent"),
   k(['poursuite', 'tendance', 'crise', 'amplifi'],
     "en période de crise, les anticipations de tendance amplifient"),
   k(['autorealisatrice', 'alimentent', 'simultanement'],
     "le marché est donc simultanément stabilisateur et déstabilisateur")],
 'ch26-questi-127': [
   k(['cassel', '1918'],
     "Cassel développe la PPA en 1918"),
   k(['prix unique', 'arbitrage', 'meme prix'],
     "son fondement est la loi du prix unique"),
   k(['absolue', 'niveau de prix', 'taux d equilibre'],
     "la PPA absolue détermine un taux d'équilibre"),
   k(['relative', 'differentiel', 'inflation'],
     "la PPA relative explique les variations par les différentiels d'inflation"),
   k(['cout de transaction', 'non echangeable', 'balassa', 'capitaux'],
     "quatre limites : coûts de transaction, biens non échangeables, "
     "Balassa-Samuelson, mouvements de capitaux")],
 'ch26-questi-128': [
   k(['1953', 'flexible exchange', 'friedman'],
     "The Case for Flexible Exchange Rates (1953)"),
   k(['equilibre', 'marche determine', 'information'],
     "premier argument : le marché détermine le taux d'équilibre"),
   k(['speculation stabilisatrice', 'stabilisatrice'],
     "deuxième argument : la spéculation est stabilisatrice"),
   k(['ajustement automatique', 'balance des paiement'],
     "troisième argument : l'ajustement automatique de la balance"),
   k(['insularisation', 'autonomie', 'nationale'],
     "quatrième argument : l'insularisation des politiques nationales"),
   k(['volcker', 'interdependance', 'limite', 'nuance'],
     "limites, dont le choc Volcker contre l'insularisation")],
 'ch26-questi-129': [
   k(['450', 'opep', 'excedent', '1974'],
     "les excédents de l'OPEP, environ 450 milliards de dollars"),
   k(['recyclage', 'banque occidentale', 'depot', 'credit'],
     "le recyclage par les banques occidentales"),
   k(['taux variable', 'hausse des taux', 'volcker'],
     "la hausse des taux américains sur des emprunts à taux variable"),
   k(['appreciation', 'dollar', 'dette libellee'],
     "l'appréciation du dollar alourdit les dettes libellées en dollars"),
   k(['recette d exportation', 'recession', 'matiere premiere'],
     "la dégradation des recettes d'exportation"),
   k(['mexique', '1982', 'crise de la dette'],
     "la crise mexicaine de 1982 déclenche la crise de la dette")],
 'ch26-questi-130': [
   k(['calvo', 'reinhart', '2002', 'fear of floating'],
     "Calvo et Reinhart, « Fear of Floating » (2002)"),
   k(['officiellement', 'declaration', 'en realite', 'intervien'],
     "des pays officiellement flottants interviennent en réalité"),
   k(['reserve', 'taux d interet', 'volatilite', 'revele'],
     "la volatilité des réserves et des taux le révèle"),
   k(['endettement en devise', 'effet de bilan', 'alourdi'],
     "première raison : l'endettement en devises et l'effet de bilan"),
   k(['inflation importee', 'relever ses taux', 'activite'],
     "seconde raison : le risque d'inflation importée")],
 'ch26-questi-131': [
   k(['capitaux', 'libre circulation', 'epargne internationale'],
     "premier sommet : la libre circulation des capitaux"),
   k(['autonomie', 'choc', '2 %', 'stabiliser'],
     "deuxième sommet : l'autonomie de la politique monétaire"),
   k(['stabilite des change', 'incertitude', 'parite'],
     "troisième sommet : la stabilité des taux de change"),
   k(['bretton woods', 'controle', '1944', '1971'],
     "Bretton Woods : contrôle des capitaux"),
   k(['1973', 'flottement', '1971', 'suspension'],
     "après 1971-1973 : flottement généralisé"),
   k(['euro', '1999', 'bce', 'souverainete'],
     "l'euro en 1999 : abandon de l'autonomie nationale"),
   k(['daniel', 'parcours complet', 'toutes les eventualite'],
     "la lecture de Jean-Marc Daniel : un parcours complet du triangle")],
 'ch26-questi-132': [
   k(['intervention directe', 'achete', 'vend', 'devise'],
     "premier instrument : l'intervention directe"),
   k(['asymetrie', 'creer sa monnaie', 'reserve limitee'],
     "l'asymétrie décisive entre les deux sens d'intervention"),
   k(['taux d interet', 'attractivite', 'placement'],
     "deuxième instrument : le taux d'intérêt"),
   k(['controle des change', 'restrein', 'operation'],
     "troisième instrument : le contrôle des changes"),
   k(['limite', 'speculation', 'guerre des monnaie', 'relatif'],
     "limites : attaques spéculatives et relativité des taux de change")],
 'ch26-questi-133': [
   k(['subie', 'competitive', 'distinguer', 'deliberee'],
     "distinguer dévaluation subie et dévaluation compétitive"),
   k(['marshall-lerner', 'elasticite', 'superieur a 1'],
     "la condition de Marshall-Lerner"),
   k(['courbe en j', 'delai', 'court terme', 'phase'],
     "les délais et la courbe en J"),
   k(['marge', 'repercut', 'comportement'],
     "le comportement de marge des exportateurs"),
   k(['inflation importee', 'intrant', 'cout', 'second tour'],
     "l'inflation importée et les effets de second tour"),
   k(['substitut', 'desindustrialisation', 'appareil productif'],
     "l'existence de substituts nationaux aux importations")],
 'ch26-questi-134': [
   k(['inflation importee', 'renchéri', 'importation', 'intrant'],
     "le point de départ : l'inflation importée"),
   k(['second tour', 'salaire', 'revendication', 'cout'],
     "les effets de second tour sur les salaires et les coûts"),
   k(['competitivite', 'erode', 'gain initial', 'annule'],
     "l'érosion du gain de compétitivité initial"),
   k(['deficit', 'persiste', 'confiance', 'degrade'],
     "le déficit persiste et la confiance se dégrade"),
   k(['anticipation', 'speculation', 'reserve', 'epuise'],
     "les anticipations de dévaluation et l'épuisement des réserves"),
   k(['nouvelle devaluation', 'cercle', 'appelle'],
     "une nouvelle dévaluation, et le cercle se referme")],
 'ch26-questi-135': [
   k(['sme', 'parite', 'franc', 'defendre'],
     "l'appartenance au Système monétaire européen"),
   k(['1981', 'mauroy', 'relance', 'chomage'],
     "la relance de 1981 contre le chômage de masse"),
   k(['inflation', '14', 'elevee', 'allemagne'],
     "une inflation déjà élevée, nettement supérieure à l'allemande"),
   k(['importation', 'deficit', 'exterieur', 'degrade'],
     "la dégradation du déséquilibre extérieur"),
   k(['octobre 1981', 'juin 1982', 'mars 1983', 'trois devaluation'],
     "les trois dévaluations d'octobre 1981, juin 1982 et mars 1983"),
   k(['subie', 'rigueur', 'tournant', 'desinflation competitive'],
     "des dévaluations subies, puis le tournant de la rigueur")],
 'ch26-questi-136': [
   k(['mars 1983', 'sans devaluer', 'parite inchangee'],
     "restaurer la compétitivité sans dévaluer, à parité inchangée"),
   k(['taux de change reel', 'inflation inferieure', 'partenaire'],
     "obtenir une inflation inférieure à celle des partenaires"),
   k(['monetaire restrictive', 'taux', 'structurelle', 'budgetaire'],
     "trois familles d'instruments"),
   k(['prix a l importation', 'pression concurrentielle', 'productivite'],
     "le cercle vertueux : prix à l'importation ↓, pression concurrentielle ↑"),
   k(['hors prix', 'solde exterieur', 'confiance', 'soutien au change'],
     "compétitivité hors prix, solde extérieur, confiance, soutien au change")],
 'ch26-questi-137': [
   k(['schmidt', 'profit', 'investissement', 'emploi'],
     "la formule de Schmidt"),
   k(['taux de marge', '25', '32', 'restaure'],
     "la condition initiale semblait réunie : marges restaurées"),
   k(['taux reel', 'desendettement', 'massue', 'levier'],
     "première limite : taux réels élevés et désendettement"),
   k(['globalisation financiere', 'placement', 'titre', 'arbitrage'],
     "deuxième limite : la globalisation financière"),
   k(['debouche', 'demande anticipee', 'rigueur', 'keynes'],
     "troisième limite : la faiblesse des débouchés anticipés")],
 'ch26-questi-138': [
   k(['desinflation', '14', '2', 'inflation'],
     "succès : la désinflation"),
   k(['balance', 'courante', 'redress', 'exterieur'],
     "succès : le redressement de la balance courante"),
   k(['marge', '25', '32', 'restauration'],
     "succès : la restauration des marges"),
   k(['croissance', '2', '3', 'ocde', 'faible'],
     "coût : une croissance plus faible que l'OCDE"),
   k(['chomage', '8', '12', 'hysterese'],
     "coût : un chômage élevé et des effets d'hystérèse"),
   k(['nuance', 'excessif', 'desindustrialisation', 'autres facteur'],
     "nuance : d'autres facteurs expliquent les difficultés ultérieures")],
 'ch26-questi-139': [
   k(['complexe', 'avantage', 'inconvenient', 'selon les agent'],
     "la question est complexe : avantages et inconvénients selon les agents"),
   k(['determinant', 'niveau', 'comprendre', 'expliquer'],
     "première dimension : comprendre le niveau et les déterminants"),
   k(['consequence', 'competitivite', 'inflation importee', 'effet'],
     "deuxième dimension : analyser les conséquences"),
   k(['acteur', 'etat', 'banque centrale', 'zone monetaire'],
     "troisième dimension : identifier les acteurs concernés"),
   k(['faible', 'eleve', 'arbitrage', 'pas de bon taux'],
     "il n'existe donc pas de bon taux de change en soi")],
 'ch26-questi-140': [
   k(['miran', 'novembre 2024', 'rapport'],
     "la doctrine Miran (novembre 2024)"),
   k(['actif sur', 'demande internationale', 'surevaluation'],
     "la demande d'actifs sûrs entretiendrait une surévaluation"),
   k(['droit de douane', 'inflation', 'contradiction'],
     "la contradiction avec le protectionnisme"),
   k(['mar-a-lago', 'plaza', 'depreciation coordonnee'],
     "le projet d'accords de Mar-a-Lago"),
   k(['assurance', 'confiance', 'reserve', 'paradoxe'],
     "le paradoxe : fragiliser la monnaie de réserve mondiale"),
   k(['stablecoin', 'genius', 'bon du tresor', 'mnbc'],
     "stablecoins, GENIUS Act et demande de bons du Trésor")],
}

# Les corrigés rédigés d'origine sont conservés comme réponses modèles.
for _id, _c in CLES.items():
    FIX[_id]['ans'] = {'cles': _c}

from qz26n1 import L as _N1
from qz26n2 import L as _N2

NEW = _N1 + _N2
