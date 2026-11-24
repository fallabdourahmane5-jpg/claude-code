# -*- coding: utf-8 -*-
"""Chapitre 8 — complément de questions « Appliquer ».

Le chapitre comptait peu de questions de niveau « Appliquer ». Ces
exercices font reconnaître un cycle à sa durée et à sa cause, distinguer
taylorisme, fordisme et toyotisme sur des cas concrets, et identifier le
type de capitalisme à l'œuvre dans une situation donnée. Chaque renvoi a
été vérifié dans le texte du cours.
"""


def f(**kw):
    return kw


L = [

f(id='q8-m01', sp='c8-06', niv='appliquer', type='assoc', b=1092,
  q="Associez chaque cycle à sa durée et à sa cause principale, selon le "
    "cours.",
  ans=[["Cycle de Kitchin", "3 à 5 ans : les stocks et les ajustements "
                            "conjoncturels de court terme"],
       ["Cycle de Juglar", "8 à 10 ans : l’investissement et le crédit"],
       ["Cycle de Kondratiev", "50 à 60 ans : les grappes d’innovations "
                               "majeures"]],
  exp="Les trois cycles s’emboîtent : des cycles courts de Kitchin "
      "apparaissent à l’intérieur d’un cycle moyen de Juglar, et plusieurs "
      "Juglar s’inscrivent dans un cycle long de Kondratiev. L’articulation "
      "avec Schumpeter est explicite dans le cours : ce sont les grappes "
      "d’innovations qui alimentent les cycles longs, tandis que Kitchin et "
      "Juglar relèvent d’ajustements de plus court terme.",
  diss="Rattacher chaque cycle à sa cause, et non seulement à sa durée, "
       "permet d’utiliser Kondratiev pour périodiser les grandes "
       "transformations du capitalisme sans tomber dans le déterminisme."),

f(id='q8-m02', sp='c8-06', niv='appliquer', type='qcm', b=1097,
  q="Un faisceau d’innovations — machine à vapeur, textile mécanisé, "
    "sidérurgie au coke — se diffuse en quelques décennies et transforme "
    "l’ensemble de l’économie. À quel élément de l’analyse de Schumpeter "
    "cette configuration correspond-elle ?",
  opts=["Une grappe d’innovations, associée à la phase ascendante d’un cycle "
        "long",
        "Un cycle de Juglar, lié au crédit",
        "Un monopole temporaire protégé par brevet",
        "Un cycle de Kitchin, lié aux stocks"],
  ans=0,
  why=["Le cycle de Juglar porte sur l’investissement et le crédit, à "
       "horizon de huit à dix ans.",
       "Le monopole temporaire concerne l’innovateur isolé, non la diffusion "
       "simultanée de plusieurs innovations.",
       "Les stocks produisent des ajustements de trois à cinq ans, sans "
       "transformation structurelle."],
  exp="Le cours donne précisément cet exemple : « la 1ʳᵉ RI est un bon "
      "exemple de grappe d’innovations pouvant être associée à une phase "
      "ascendante d’un cycle long ». Le mécanisme schumpétérien est que les "
      "innovations ne se répartissent pas uniformément dans le temps : elles "
      "surviennent en grappes, chacune ouvrant une phase ascendante d’environ "
      "vingt-cinq à trente ans, avant que l’épuisement du potentiel "
      "d’innovation ne fasse basculer le cycle.",
  diss="L’exemple historique daté donne de la chair à la notion de grappe, et "
       "prépare l’ouverture contemporaine sur la voiture électrique ou "
       "autonome comme grappes futures."),

f(id='q8-m03', sp='c8-06', niv='raisonner', type='qcm', b=951,
  q="Pourquoi Schumpeter réhabilite-t-il le monopole temporaire contre "
    "l’idéal de concurrence pure et parfaite ?",
  opts=["Parce que la perspective d’une rente temporaire, protégée par le "
        "brevet, est ce qui rend l’innovation rentable et donc possible",
        "Parce que le monopole produit à moindre coût",
        "Parce que la concurrence parfaite n’existe nulle part",
        "Parce que le monopole protège l’emploi"],
  ans=0,
  why=["L’argument des coûts est celui du monopole naturel : ce n’est pas le "
       "raisonnement de Schumpeter.",
       "L’irréalisme de la CPP est un argument distinct, qui ne justifierait "
       "pas à lui seul de préférer le monopole.",
       "La destruction créatrice détruit au contraire des emplois dans les "
       "secteurs anciens."],
  exp="L’argument est dynamique, non statique. En concurrence parfaite, une "
      "innovation serait immédiatement imitée et ne rapporterait rien à son "
      "auteur : personne n’aurait intérêt à engager les dépenses de "
      "recherche. Le monopole temporaire — garanti notamment par le brevet — "
      "assure une rente qui finance l’innovation. Le coût statique, un prix "
      "supérieur au coût marginal pendant quelques années, est donc le prix "
      "d’un gain dynamique.",
  diss="Opposer efficacité statique et efficacité dynamique est "
       "indispensable pour traiter un sujet sur la politique de la "
       "concurrence ou sur les brevets."),

f(id='q8-m04', sp='c8-08', niv='appliquer', type='qcm', b=1365,
  q="En 1914, Ford porte le salaire journalier de 2,5 à 5 dollars. Quelle "
    "logique économique cette décision sert-elle, au-delà de la "
    "philanthropie ?",
  opts=["Stabiliser une main-d’œuvre soumise au travail à la chaîne et "
        "solvabiliser la demande pour les biens produits en masse",
        "Compenser la baisse de la productivité due à la chaîne de montage",
        "Répondre à une obligation légale de salaire minimum",
        "Réduire le nombre d’ouvriers nécessaires"],
  ans=0,
  why=["La chaîne accroît fortement la productivité : c’est son objet même.",
       "Aucun salaire minimum fédéral n’existe alors : la décision est "
       "unilatérale.",
       "La hausse du salaire n’a pas pour but de réduire les effectifs, mais "
       "de les stabiliser."],
  exp="Le fordisme ajoute au taylorisme deux éléments : la chaîne de montage, "
      "qui permet la production de masse par standardisation, et les hauts "
      "salaires. Ceux-ci répondent à deux problèmes simultanés : la rotation "
      "élevée d’une main-d’œuvre épuisée par un travail parcellisé, et "
      "l’absence de débouchés pour une production massive. Payer "
      "cinq dollars, c’est retenir l’ouvrier et en faire un client.",
  diss="Le doublement du salaire chez Ford est l’exemple canonique du "
       "compromis fordiste : il relie organisation du travail, répartition "
       "des gains de productivité et régime de croissance."),

f(id='q8-m05', sp='c8-09', niv='appliquer', type='qcm', b=1385,
  q="Une usine ne lance la production d’une pièce qu’une fois la commande du "
    "poste situé en aval reçue. De quel principe s’agit-il, et à quel modèle "
    "appartient-il ?",
  opts=["Le juste-à-temps, ou flux tendu, principe du toyotisme : c’est "
        "l’aval qui commande l’amont",
        "La standardisation fordiste",
        "La division scientifique du travail de Taylor",
        "L’autonomation, qui consiste à arrêter la chaîne en cas de défaut"],
  ans=0,
  why=["La standardisation fordiste produit en série pour le stock, selon "
       "des prévisions.",
       "La division scientifique du travail porte sur la décomposition des "
       "gestes, non sur le déclenchement de la production.",
       "L’autonomation est un autre principe du toyotisme : elle combine "
       "autonomie et automatisation dans le contrôle de la qualité."],
  exp="Le cours est explicite : « on ne produit que ce qu’on a vendu. Ce sont "
      "les postes en AVAL de la production qui déterminent l’AMONT ». Le "
      "renversement est complet par rapport au tayloro-fordisme, qui "
      "produisait en flux poussé et engendrait « surproduction, stocks, "
      "défauts, rigidité ». Le juste-à-temps s’accompagne de la règle des "
      "cinq zéros : zéro stock, zéro délai, zéro panne, zéro défaut, zéro "
      "papier.",
  diss="Opposer flux poussé et flux tendu permet de montrer qu’un modèle "
       "productif répond aux défauts du précédent, et non à une logique "
       "d’amélioration continue abstraite."),

f(id='q8-m06', sp='c8-09', niv='raisonner', type='vf', b=1401,
  q="Vrai ou faux : le toyotisme rompt totalement avec le taylorisme. "
    "Justifiez.",
  ans=False,
  exp="Le cours pose explicitement la question « rupture ou prolongement ? » "
      "et refuse de trancher dans un sens unique. Le système de production "
      "Toyota reprend des principes tayloriens, notamment la recherche "
      "d’une forte productivité et le chronométrage. Mais il les infléchit : "
      "les ouvriers deviennent des opérateurs travaillant en équipes "
      "semi-autonomes, l’autonomation leur donne le pouvoir d’arrêter la "
      "production en cas de défaut, et le kaizen les sollicite pour "
      "améliorer leur propre poste. La rupture porte donc sur l’usage de "
      "l’intelligence ouvrière, non sur l’objectif de productivité.",
  diss="La formule « prolongement infléchi » est plus juste que « rupture » "
       "et vaut mieux en copie : elle oblige à préciser sur quel point porte "
       "la continuité et sur lequel porte la nouveauté."),

f(id='q8-m07', sp='c8-11', niv='appliquer', type='qcm', b=1752,
  q="Dans une grande société cotée, le capital est dispersé entre des "
    "milliers d’actionnaires et les décisions sont prises par des dirigeants "
    "salariés. Quel phénomène, et quels auteurs ?",
  opts=["La séparation entre propriété et contrôle, analysée par Berle et "
        "Means dans The Modern Corporation and Private Property (1932)",
        "La théorie de l’agence de Jensen et Meckling",
        "La main visible des managers décrite par Chandler",
        "La destruction créatrice de Schumpeter"],
  ans=0,
  why=["La théorie de l’agence vient ensuite : elle analyse le conflit "
       "d’intérêts que cette séparation engendre, elle ne la constate pas.",
       "Chandler montre que les managers coordonnent ce que le marché "
       "coordonnait auparavant : c’est une thèse voisine mais distincte.",
       "La destruction créatrice porte sur la dynamique de l’innovation, non "
       "sur la gouvernance."],
  exp="Berle et Means établissent le fait : dans la grande entreprise "
      "moderne, la propriété est dispersée et le contrôle effectif revient "
      "aux dirigeants. Ce constat ouvre deux prolongements que le cours "
      "distingue : Chandler montre que ces managers remplacent partiellement "
      "le marché dans la coordination, et Jensen et Meckling théorisent le "
      "problème d’agence — comment aligner l’intérêt du dirigeant sur celui "
      "du propriétaire.",
  diss="Distinguer le constat (Berle et Means), l’analyse organisationnelle "
       "(Chandler) et la réponse contractuelle (théorie de l’agence) montre "
       "la construction progressive d’un problème."),

f(id='q8-m08', sp='c8-12', niv='raisonner', type='qcm', b=1806,
  q="Selon Friedman (1970), quelle est la responsabilité sociale de "
    "l’entreprise, et sur quel raisonnement repose cette position ?",
  opts=["Accroître ses profits : le dirigeant est mandaté par les "
        "actionnaires, et disposer de leurs fonds à d’autres fins reviendrait "
        "à lever un impôt sans mandat",
        "Équilibrer les intérêts de toutes les parties prenantes",
        "Garantir l’emploi de ses salariés avant tout",
        "Réduire son empreinte environnementale"],
  ans=0,
  why=["L’approche par les parties prenantes est précisément celle qui "
       "s’oppose à Friedman.",
       "La garantie de l’emploi relève d’une conception que Friedman "
       "récuse : le dirigeant n’en a pas le mandat.",
       "L’objectif environnemental relève de la responsabilité sociale que "
       "Friedman conteste comme fin propre de l’entreprise."],
  exp="L’argument de The Social Responsibility of Business is to Increase its "
      "Profits est juridique autant qu’économique : le dirigeant est "
      "l’agent des actionnaires, et affecter les ressources de l’entreprise "
      "à des objectifs sociaux revient à dépenser l’argent d’autrui sans "
      "mandat. Cette position fonde le capitalisme actionnarial. Le cours la "
      "présente ensuite comme contestée, à la fois par l’approche des "
      "parties prenantes et par Polanyi, pour qui l’économie doit rester "
      "encastrée dans la société.",
  diss="Restituer l’argument de Friedman dans sa logique, avant de le "
       "critiquer, évite la caricature et rend la critique plus solide."),

f(id='q8-m09', sp='c8-13', niv='appliquer', type='qcm', b=2053,
  q="Une entreprise associe salariés, fournisseurs, riverains et "
    "collectivités à sa gouvernance. À quelle conception se rattache-t-elle, "
    "et de quelle analyse se rapproche-t-elle ?",
  opts=["La conception des parties prenantes, qui rejoint l’idée de Polanyi "
        "selon laquelle l’économie doit être encastrée dans la société",
        "Le capitalisme actionnarial théorisé par Jensen et Meckling",
        "Le capitalisme entrepreneurial, où propriété et pouvoir se "
        "confondent",
        "Le capitalisme managérial décrit par Chandler"],
  ans=0,
  why=["Le capitalisme actionnarial fait précisément de l’actionnaire le "
       "seul mandant.",
       "Le capitalisme entrepreneurial suppose un propriétaire-dirigeant "
       "unique, et non une gouvernance élargie.",
       "Le capitalisme managérial déplace le pouvoir vers les dirigeants, "
       "non vers les parties prenantes."],
  exp="L’approche par les parties prenantes élargit le cercle de ceux dont "
      "les intérêts comptent dans la décision : salariés, fournisseurs, "
      "clients, riverains, environnement. Le cours la relie explicitement à "
      "La Grande Transformation (1944), où Polanyi montre que « l’économie "
      "ne peut être autonome : elle doit être encastrée dans la société ». "
      "C’est la réponse théorique aux limites du modèle actionnarial.",
  diss="Le couple Friedman / Polanyi donne une colonne vertébrale à toute "
       "dissertation sur la finalité de l’entreprise : deux conceptions du "
       "rapport entre économie et société."),

f(id='q8-m10', sp='c8-07', niv='raisonner', type='qcm', b=1143,
  q="Pourquoi Schumpeter juge-t-il que le capitalisme peut être « miné par "
    "sa propre réussite » ?",
  opts=["Parce que la grande entreprise bureaucratique tend à remplacer "
        "l’entrepreneur innovateur, en routinisant l’innovation",
        "Parce que la concurrence parfaite finit par s’imposer",
        "Parce que les cycles longs s’arrêtent",
        "Parce que les brevets protègent trop longtemps les innovateurs"],
  ans=0,
  why=["Schumpeter ne prévoit pas un retour à la concurrence parfaite, dont "
       "il conteste d’ailleurs la pertinence.",
       "Rien dans le raisonnement ne suppose l’arrêt des cycles.",
       "La durée des brevets n’est pas l’argument retenu par le cours."],
  exp="Le paradoxe est que le succès du capitalisme engendre de grandes "
      "firmes capables de financer la recherche de façon systématique. "
      "L’innovation devient alors une fonction bureaucratique, planifiée par "
      "des services spécialisés, et la figure de l’entrepreneur — qui prend "
      "le risque et bouscule l’ordre établi — perd sa raison d’être. "
      "Schumpeter y voit un affaiblissement du ressort même du système, non "
      "un échec économique.",
  diss="Ce pessimisme schumpétérien est précieux en dissertation : il montre "
       "qu’un système peut être menacé par sa propre dynamique, et non "
       "seulement par ses crises."),
]
