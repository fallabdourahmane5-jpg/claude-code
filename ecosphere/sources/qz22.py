# -*- coding: utf-8 -*-
"""Chapitre 22 — Les acteurs de la mondialisation économique : les FMN et les États.

Audit : 88 questions héritées, 18 sous-parties, la sous-partie c22-13
(« Les échecs des stratégies d'industrialisation ») n'était pas testée.
16 questions vrai/faux supprimées (elles reformulaient à l'identique un QCM
déjà présent dans la même sous-partie), 72 questions conservées et corrigées,
une banque nouvelle ajoutée.
"""

SP = {
 'c22-01': "Firme, coûts de transaction et valeur actionnariale",
 'c22-02': "Définir la FMN : IDE, filiales, responsabilité",
 'c22-03': "DIPP, chaînes de valeur et courbe du sourire",
 'c22-04': "Dumping, règles du commerce et désindustrialisation",
 'c22-05': "Les quatre explications de la désindustrialisation",
 'c22-06': "Le choc chinois et ses effets territoriaux",
 'c22-07': "Gagnants et perdants : nomades, sédentaires, caddie et feuille de paye",
 'c22-08': "La compétitivité d'une nation : une notion contestée",
 'c22-09': "Compétitivité-prix, hors-prix et dispositifs français",
 'c22-10': "Concurrence fiscale, coordination OCDE et types de politique industrielle",
 'c22-11': "L'État entrepreneur et les justifications de l'intervention",
 'c22-12': "Protection, distance à la frontière technologique et avantages construits",
 'c22-13': "Les échecs des stratégies d'industrialisation protégée",
 'c22-14': "La tradition française : du colbertisme au colbertisme high-tech",
 'c22-15': "Le « moment 2020 », géoéconomie et stratégies de relocalisation",
 'c22-16': "Souveraineté industrielle, dépendances critiques et nationalisations",
 'c22-17': "Verdissement de la politique industrielle et surenchère des subventions",
 'c22-18': "Attractivité, effets de réseau et trilemme de la croissance",
}

# Questions supprimées : chacune reformulait en vrai/faux un QCM de la même
# sous-partie, sans apporter de contenu nouveau (répétition interdite par le
# cahier des charges).
DROP = [
 'ch22-vraifa-46',   # doublon de ch22-qcm-1 (seuil de la multinationalisation)
 'ch22-vraifa-47',   # doublon de ch22-qcm-3 (IDE vertical)
 'ch22-vraifa-48',   # doublon de ch22-qcm-14 (mesure du Made in France)
 'ch22-vraifa-49',   # doublon de ch22-qcm-8 (grande convergence)
 'ch22-vraifa-50',   # doublon de ch22-qcm-18 (causes de la désindustrialisation)
 'ch22-vraifa-51',   # doublon de ch22-qcm-26 (compétitivité des nations)
 'ch22-vraifa-52',   # doublon de ch22-qcm-27 (coût unitaire du travail)
 'ch22-vraifa-54',   # doublon de ch22-qcm-32 (dilemme du prisonnier fiscal)
 'ch22-vraifa-55',   # doublon de ch22-qcm-33 (Pilier 2)
 'ch22-vraifa-56',   # doublon de ch22-qcm-35 (politique horizontale/verticale)
 'ch22-vraifa-58',   # doublon de ch22-qcm-37 (État entrepreneur)
 'ch22-vraifa-59',   # doublon de ch22-qcm-42 (souveraineté sélective)
 'ch22-vraifa-60',   # doublon de ch22-qcm-5 (seuil de 10 %)
 'ch22-vraifa-61',   # doublon de ch22-qcm-24 (nomades / sédentaires)
 'ch22-vraifa-62',   # doublon de ch22-qcm-20 (China Syndrome)
 'ch22-vraifa-64',   # doublon de ch22-qcm-4 (seuil de 50 %)
]

from qz22f1 import FIX as _F1
from qz22f2 import FIX as _F2

FIX = dict(_F1)
FIX.update(_F2)

# Éléments attendus pour les réponses rédigées héritées.
def k(f, l):
    return {'f': f, 'l': l}


CLES = {
 'ch22-questi-66': [
   k(['horizontal', 'reproduire', 'meme production'],
     "l'IDE horizontal reproduit la production à l'étranger"),
   k(['marche', 'consommateur', 'proximite', 'distance'],
     "logique de marché : se rapprocher du consommateur"),
   k(['vertical', 'fragment', 'decompos', 'etape'],
     "l'IDE vertical fragmente la chaîne de valeur"),
   k(['rationalisation', 'cout', 'avantageu', 'bas salaire'],
     "logique de rationalisation des coûts"),
   k(['dipp', 'chaine de valeur', 'filiale-atelier', 'filiale atelier'],
     "DIPP et filiales-ateliers")],
 'ch22-questi-67': [
   k(['amont', 'conception', 'r&d', 'recherche'],
     "valeur forte en amont : conception, R&D"),
   k(['aval', 'marketing', 'marque', 'service'],
     "valeur forte en aval : marketing, marque, services"),
   k(['assemblage', 'centre', 'creux', 'milieu'],
     "valeur faible au centre : l'assemblage"),
   k(['montee en gamme', 'monter en gamme', 'gamme'],
     "enjeu de la montée en gamme"),
   k(['creuse', 'accentue', 'baldwin'],
     "le sourire s'est creusé (Baldwin)")],
 'ch22-questi-68': [
   k(['limite', 'faible', 'minoritaire', 'un quart', '25 %'],
     "l'ampleur mesurée des délocalisations est limitée"),
   k(['gallois', 'quart'],
     "environ un quart des pertes d'emplois (rapport Gallois, 2012)"),
   k(['progres technique', 'productivite', 'automatisation', 'machine'],
     "le progrès technique et les gains de productivité"),
   k(['engel', 'fourastie', 'tertiarisation', 'demande', 'service'],
     "la tertiarisation de la demande (Engel, Fourastié)"),
   k(['externalisation', 'statistique', 'comptable', 'sous-traitance'],
     "l'externalisation des services")],
 'ch22-questi-69': [
   k(['peu qualifie', 'textile', 'travail', 'simple', 'bas de gamme'],
     "premier choc : biens intensifs en travail peu qualifié"),
   k(['complementaire', 'complementarite', 'abandonn', 'montee en gamme'],
     "une complémentarité relative avec la montée en gamme occidentale"),
   k(['haute technologie', 'technologi', 'electrique', 'batterie',
      'transition'],
     "deuxième choc : haute technologie et transition énergétique"),
   k(['frontiere technologique', 'avantage comparatif', 'gamme'],
     "concurrence directe sur la frontière technologique"),
   k(['detourn', 'europe', 'deficit', 'reorient'],
     "détournement des flux chinois vers l'Union européenne")],
 'ch22-questi-70': [
   k(['nomade', 'exposee', 'delocalisable', 'mobile'],
     "activités nomades : exposées et délocalisables"),
   k(['sedentaire', 'proximite', 'ancree', 'protegee'],
     "activités sédentaires : protégées par la proximité"),
   k(['qualification', 'qualifie', 'croise', 'quatre'],
     "croisement avec le niveau de qualification"),
   k(['gagnant', 'nomade qualifie', 'rare', 'recherche'],
     "les nomades qualifiés sont les gagnants"),
   k(['perdant', 'peu qualifie', 'cumulent'],
     "les peu qualifiés des secteurs exposés sont les perdants"),
   k(['pression salariale', 'salaire', 'baisse de salaire'],
     "pression salariale sur les sédentaires peu qualifiés")],
 'ch22-questi-71': [
   k(['pas une entreprise', 'disparait pas', 'nation', 'entreprise'],
     "une nation n'est pas une entreprise"),
   k(['somme nulle', 'gain mutuel', 'avantage comparatif'],
     "le commerce n'est pas un jeu à somme nulle"),
   k(['productivite', 'niveau de vie', 'interieur'],
     "le niveau de vie dépend de la productivité intérieure"),
   k(['deficit', 'epargne', 'macroeconomique', 'demande interieure'],
     "le déficit commercial a des causes macroéconomiques"),
   k(['moins-disant', 'moins disant', 'baisse des salaires', 'inadapt'],
     "risque de politiques inadaptées et de moins-disant salarial")],
 'ch22-questi-72': [
   k(['collectivement', 'interet collectif', 'recette', 'suffisante'],
     "intérêt collectif : maintenir une fiscalité suffisante"),
   k(['individuellement', 'baisser son taux', 'attirer'],
     "intérêt individuel : baisser son taux pour attirer les capitaux"),
   k(['reagit', 'de meme', 'symetrique', 'tous'],
     "la réaction symétrique des autres États"),
   k(['avantage relatif', 'perte de recette', 'sans avantage'],
     "perte de recettes sans avantage relatif"),
   k(['coordination', 'ocde', 'pilier', '15 %'],
     "nécessité d'une coordination internationale (OCDE)")],
 'ch22-questi-73': [
   k(['verticale', 'cible', 'branche', 'technologie precise'],
     "la politique verticale cible une entreprise, une branche, une technologie"),
   k(['horizontale', 'environnement', 'ensemble', 'general'],
     "la politique horizontale agit sur l'environnement productif général"),
   k(['infrastructure', 'r&d', 'concurrence', 'formation', 'fiscalite'],
     "instruments horizontaux : infrastructures, R&D, concurrence, fiscalité"),
   k(['ciblage', 'degre', 'frontiere'],
     "la frontière tient au degré de ciblage"),
   k(['erreur', 'choisir les gagnants', 'risque', 'rente'],
     "le risque d'erreur de sélection")],
 'ch22-questi-74': [
   k(['externalite', 'rendement social', 'diffusion'],
     "les externalités positives de la R&D"),
   k(['asymetrie', 'information', 'capital-risque', 'capital risque',
      'rationnement'],
     "les asymétries d'information et le soutien au capital-risque"),
   k(['list', 'educateur', 'industrie naissante'],
     "le protectionnisme éducateur de List (1841)"),
   k(['avantage comparatif', 'construit', 'dynamique', 'faconn'],
     "les avantages comparatifs sont construits"),
   k(['erreur', 'rente', 'risque', 'limite'],
     "limite : risque d'erreur de ciblage et de rente")],
 'ch22-questi-75': [
   k(['public', 'etat', 'finance', 'investissement public'],
     "des technologies rentables issues d'investissements publics"),
   k(['risque', 'marche seul', 'incertain', 'horizon'],
     "des risques que le marché seul n'aurait pas financés"),
   k(['cree des marche', 'creer des marche', 'entrepreneur', 'cree le marche'],
     "l'État crée des marchés, il ne corrige pas seulement"),
   k(['darpa', '1958'],
     "la DARPA (1958) comme exemple emblématique"),
   k(['partage', 'profit', 'socialise', 'privatise', 'gain'],
     "la question du partage des gains")],
 'ch22-questi-76': [
   k(['exploitable', 'pression', 'strategique', 'dependance'],
     "empêcher qu'une dépendance devienne stratégiquement exploitable"),
   k(['selectivite', 'selectif', 'pas autosuffisance', 'cible'],
     "une exigence de sélectivité, non d'autosuffisance"),
   k(['cout', 'specialisation', 'couteu', 'renoncer'],
     "le coût d'une relocalisation généralisée"),
   k(['potager', 'choc domestique', 'combe', 'guillou', 'greve'],
     "le mythe du potager (Combe et Guillou)"),
   k(['diversification', 'stock', 'critique', 'materiau', 'composant'],
     "diversification, stockage et dépendances critiques")],
 'ch22-questi-77': [
   k(['batterie', 'valeur', 'actif', 'deplace'],
     "la valeur se déplace vers la batterie"),
   k(['chine', 'catl', 'trois quarts', '75'],
     "la domination chinoise de la production de batteries"),
   k(['byd', 'integration verticale', 'integr'],
     "BYD et l'intégration verticale"),
   k(['etat', 'aide', 'lithium', 'public', 'souverainete'],
     "le retour de l'État dans la filière"),
   k(['temps', 'delai', '2030', 'avance'],
     "le problème du délai d'investissement")],
 'ch22-questi-78': [
   k(['donneur', 'donneuse', 'ordre', 'responsable'],
     "la FMN est donneuse d'ordres, donc responsable"),
   k(['externalis', 'sous-traitance', 'sous traitance', 'proprietaire'],
     "externaliser la production n'externalise pas la responsabilité"),
   k(['rana plaza', 'bangladesh', '2013'],
     "le Rana Plaza au Bangladesh (2013)"),
   k(['securite', 'condition de travail', 'droit', 'environnement', 'norme'],
     "standards de sécurité, de travail, de droits et d'environnement"),
   k(['fournisseur', 'verifier', 'controle', 'vigilance'],
     "le contrôle des fournisseurs (devoir de vigilance)")],
 'ch22-questi-79': [
   k(['valeur ajoutee', 'demande interieure', 'contenu', 'part'],
     "la part de valeur ajoutée française dans la demande finale"),
   k(['fragmentation', 'chaine de valeur', 'origine', 'assemblage'],
     "la fragmentation brouille l'origine de la valeur"),
   k(['78', '2019'],
     "environ 78 % de contenu domestique en 2019"),
   k(['service', 'proximite', 'tertiaire'],
     "le poids des services explique ce niveau élevé"),
   k(['manufactur', '38', '82', '1965'],
     "les produits manufacturés : d'environ 82 % (1965) à 38 % (2019)")],
 'ch22-questi-80': [
   k(['mobilite', 'mobile', 'concurrence des territoire', 'mise en concurrence'],
     "la mobilité des FMN met les territoires en concurrence"),
   k(['optimisation', 'prix de transfert', 'fiscal', 'evasion'],
     "l'optimisation fiscale et les prix de transfert"),
   k(['filtrage', 'norme', 'reglementation', 'taxation', 'droits de douane'],
     "les instruments de l'État : filtrage, normes, fiscalité, douane"),
   k(['21', '52', '2025', '2016'],
     "le filtrage des IDE : 21 économies en 2016, 52 en 2025"),
   k(['dependance', 'rapport de force', 'cooperation', 'interdependance'],
     "une relation de dépendance mutuelle et un rapport de force variable")],
 'ch22-questi-81': [
   k(['caddie', 'consommateur', 'pouvoir d achat', 'prix plus bas'],
     "le caddie : les gains du consommateur"),
   k(['1 000', '2 000', 'menage', 'par an'],
     "un gain de 1 000 à 2 000 € par ménage et par an"),
   k(['feuille de paye', 'emploi', 'salaire', 'travailleur'],
     "la feuille de paye : emplois et salaires exposés"),
   k(['asymetrie', 'diffus', 'concentre', 'inegal'],
     "l'asymétrie : gains diffus, pertes concentrées"),
   k(['meme individu', 'gagnant et perdant', 'selon sa position', 'simultan'],
     "un même individu peut être gagnant et perdant")],
 'ch22-questi-82': [
   k(['orienter', 'volontairement', 'investissement', 'cibl'],
     "orienter volontairement les investissements vers la transition"),
   k(['batterie', 'renouvelable', 'hydrogene', 'reseau', 'pompe a chaleur'],
     "batteries, renouvelables, hydrogène, réseaux"),
   k(['verticale', 'cible', 'rehabilit'],
     "une réhabilitation des politiques verticales ciblées"),
   k(['environnement', 'souverainete', 'climat', 'decarbonation'],
     "un objectif environnemental et de souveraineté"),
   k(['surenchere', 'course', 'subvention', 'tension'],
     "le risque de surenchère des subventions")],
}

for _id, _c in CLES.items():
    FIX[_id]['ans'] = {'modele': FIX[_id]['exp'], 'cles': _c}

from qz22n1 import L as _N1
from qz22n2 import L as _N2
from qz22n3 import L as _N3
from qz22n4 import L as _N4

NEW = _N1 + _N2 + _N3 + _N4
