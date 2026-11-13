# -*- coding: utf-8 -*-
"""Définitions des notions-têtes de famille.

Ces mots ouvrent chacun une famille entière de notions dans les cours
(capital, salaire, coût, taux, demande…). Les formes particulières étaient
définies, le terme générique ne l'était pas : la recherche d'un mot seul
n'avait donc pas de réponse principale.

Format : (terme, chapitres, ancre, définition, alias, distinction)
"""

DEFS = [

 ("Capital", ['1', '3', '4', '6', '8', '21'],
  "Les différentes formes de capital",
  "En économie, le capital désigne l’ensemble des moyens de production "
  "durables accumulés et utilisés pour produire : bâtiments, machines, "
  "équipements, infrastructures. Les cours en distinguent plusieurs formes "
  "selon leur nature — capital fixe et capital circulant, capital physique, "
  "capital humain, capital naturel, capital public, capital technologique — et "
  "selon leur rôle dans l’analyse — capital constant et capital variable chez "
  "Marx, capital par tête dans le modèle de Solow. Au sens comptable et "
  "financier, le mot désigne en revanche les fonds apportés par les associés, "
  "inscrits au passif du bilan sous le nom de capital social.",
  ["capital productif", "capital technique", "stock de capital"],
  "Ne pas confondre le capital au sens productif, qui est un stock "
  "d’équipements, et le capital au sens financier, qui est un apport de fonds : "
  "les deux sens coexistent dans les cours et n’obéissent pas aux mêmes "
  "mécanismes."),

 ("Salaire", ['1', '3', '8', '10', '22'], "Du salaire super-brut au salaire net",
  "Le salaire est la rémunération du travail salarié. Les cours en distinguent "
  "trois niveaux : le salaire super-brut, qui représente le coût total pour "
  "l’employeur ; le salaire brut, qui est le super-brut diminué des "
  "cotisations patronales ; le salaire net, qui est le brut diminué des "
  "cotisations salariales — assurance maladie, allocation chômage, retraite. "
  "Le salaire est à la fois un coût de production pour l’entreprise et un "
  "revenu qui alimente la demande, ce double statut étant au cœur de "
  "l’opposition entre analyses classique et keynésienne.",
  ["salaire brut", "salaire net", "salaire super brut", "remuneration"],
  "À distinguer du coût du travail, qui est le salaire super-brut vu du côté "
  "de l’employeur, et du salaire réel, qui corrige le salaire nominal de "
  "l’évolution des prix."),

 ("Pauvreté", ['1', '7', '10', '21'], "Le seuil de pauvreté",
  "La pauvreté est l’insuffisance des ressources d’un ménage au regard d’une "
  "norme. Le cours en retient d’abord une mesure monétaire et relative : le "
  "seuil de pauvreté se calcule par rapport au revenu médian, à 50 % de ce "
  "revenu ou à 60 % selon la norme européenne ; en France, le seuil à 50 % "
  "correspond à environ 1 073 euros mensuels pour une personne seule et "
  "5,4 millions de personnes pauvres, le seuil à 60 % à environ 1 288 euros et "
  "9,8 millions de personnes. Le taux de pauvreté désigne la part de la "
  "population située sous ce seuil.",
  ["seuil de pauvrete", "taux de pauvrete", "pauvrete monetaire"],
  "La pauvreté relative, définie par rapport au revenu médian national, se "
  "distingue de la pauvreté absolue, définie par un panier de biens "
  "incompressible, et de la pauvreté multidimensionnelle, qui ajoute la santé, "
  "l’éducation et les conditions de vie."),

 ("Compétitivité", ['2', '6', '7', '9', '21', '22', '23'],
  "La recherche de la compétitivité",
  "La compétitivité est la capacité d’une entreprise, d’un secteur ou d’un "
  "pays à maintenir ou à accroître ses parts de marché face à la concurrence. "
  "Les cours en distinguent deux composantes : la compétitivité-prix, qui "
  "repose sur des prix de vente plus faibles, elle-même commandée par la "
  "compétitivité-coût et par le taux de change ; et la compétitivité "
  "hors-prix, qui repose sur la qualité, l’innovation, les délais, la "
  "réputation et les services associés. Draghi en donne une lecture "
  "stratégique : la compétitivité européenne est la capacité à produire les "
  "biens stratégiques.",
  ["competitivite prix", "competitivite cout", "competitivite hors prix"],
  "À distinguer de la productivité, qui mesure l’efficacité de la production "
  "et non la position sur un marché : une productivité élevée nourrit la "
  "compétitivité sans s’y réduire."),

 ("Déficit", ['1', '7', '21', '22', '23'],
  "Déficit public et déficit budgétaire",
  "Un déficit est un solde négatif entre des recettes et des dépenses, ou "
  "entre des entrées et des sorties. Les cours en distinguent plusieurs, qu’il "
  "ne faut pas confondre : le déficit public est le solde négatif des recettes "
  "et des dépenses de l’ensemble des administrations publiques sur une année ; "
  "le déficit budgétaire ne concerne que l’État et ses administrations "
  "centrales ; le déficit commercial est le solde négatif des échanges de "
  "biens et services ; le déficit courant ajoute aux échanges les revenus et "
  "les transferts.",
  ["deficit public", "deficit budgetaire", "solde negatif"],
  "Un déficit est un flux annuel, à ne jamais confondre avec la dette, qui est "
  "le stock accumulé des déficits passés."),

 ("Demande", ['1', '3', '4', '5', '6', '21'],
  "L’offre et la demande",
  "La demande est la quantité d’un bien ou d’un service que les agents "
  "souhaitent et peuvent acheter à un prix donné. À l’échelle d’un marché, "
  "elle est décroissante avec le prix et sa sensibilité se mesure par "
  "l’élasticité. À l’échelle de l’économie, la demande globale réunit la "
  "consommation, l’investissement, les dépenses publiques et les "
  "exportations : c’est elle qui, dans l’analyse keynésienne, détermine le "
  "niveau de production et d’emploi.",
  ["demande du consommateur", "demande solvable"],
  "À distinguer du besoin, qui n’est pas nécessairement solvable, et de la "
  "demande effective, qui est la demande que les entrepreneurs anticipent."),

 ("Offre", ['1', '3', '4', '5', '6'], "L’offre et la demande",
  "L’offre est la quantité d’un bien ou d’un service que les producteurs "
  "acceptent de vendre à un prix donné. Elle est croissante avec le prix et se "
  "déduit de la maximisation du profit : le producteur offre jusqu’au point où "
  "le prix égale son coût marginal. À l’échelle macroéconomique, l’offre "
  "globale désigne l’ensemble de la production disponible ; les analyses dites "
  "de l’offre font de ses conditions — coûts, fiscalité, réglementation — le "
  "déterminant premier de l’activité.",
  ["offre globale", "offre du producteur"],
  "L’opposition entre politiques de l’offre et politiques de la demande "
  "recoupe celle entre analyses néoclassique et keynésienne."),
]
