# -*- coding: utf-8 -*-
"""Chapitre 24 — corrections des questions héritées, sous-parties c24-01 et c24-02."""


def f(**kw):
    return kw


FIX = {

# =============================================================== c24-01
'ch24-qcm-1': f(niv='connaitre', sp='c24-01', b=150,
 why=["Un accord entre deux États est du bilatéralisme.",
      "Une décision prise sans négociation relève de l’unilatéralisme.",
      "Un accord entre pays géographiquement proches est du régionalisme."],
 diss="Quatre modes de coordination à distinguer d’emblée : unilatéralisme, "
      "bilatéralisme, plurilatéralisme et multilatéralisme, auxquels s’ajoute "
      "le régionalisme."),
'ch24-qcm-2': f(niv='connaitre', sp='c24-01', b=155,
 why=["Efficacité et efficience sont des critères d’évaluation des "
      "politiques, non les principes du multilatéralisme.",
      "Souveraineté et subsidiarité renvoient à la répartition des "
      "compétences, notamment dans l’Union européenne.",
      "La transparence est bien un principe du GATT, mais la "
      "proportionnalité relève du droit des mesures de sauvegarde."]),
'ch24-qcm-4': f(niv='connaitre', sp='c24-01', b=42,
 why=["Banques centrales et ménages ne sont pas retenus comme catégories "
      "d’acteurs de la mondialisation dans ce découpage.",
      "OMC, FMI et Banque mondiale sont des institutions, c’est-à-dire des "
      "produits de l’action des États, non les acteurs eux-mêmes.",
      "Exportateurs, importateurs et consommateurs sont des rôles "
      "économiques, non des catégories d’acteurs politiques."],
 diss="Découpage à garder comme plan possible : ce que veut chaque acteur, et "
      "ce que son pouvoir lui permet d’obtenir."),
'ch24-qcm-5': f(niv='comprendre', sp='c24-01', b=20,
 why=["La réduction du volume total n’est pas automatique : les flux peuvent "
      "se réorienter à volume comparable.",
      "L’effet sur la géographie est précisément le plus important : "
      "l’affirmer nul contredit les observations du cours.",
      "L’OMC admet de nombreuses exceptions — sauvegardes, antidumping, "
      "droits compensateurs, sécurité nationale."]),
'ch24-qcm-6': f(niv='raisonner', sp='c24-01', b=41,
 why=["La fiscalité peut jouer un rôle, mais elle n’explique pas "
      "l’attachement structurel des FMN au libre-échange.",
      "La soumission aux règles de l’OMC concerne les États, non directement "
      "les firmes.",
      "Les IDE horizontaux sont au contraire une réponse possible aux "
      "barrières commerciales, par tariff jumping."],
 diss="Conséquence politique : les FMN constituent un puissant groupe de "
      "pression en faveur de l’ouverture, ce qui pèse sur la formation des "
      "politiques commerciales."),
'ch24-qcm-7': f(niv='connaitre', sp='c24-01', b=35,
 why=["Produire à proximité des consommateurs étrangers définit l’IDE "
      "horizontal, qui relève d’une logique de marché.",
      "Le rachat d’un concurrent du même secteur est une concentration "
      "horizontale, et non nécessairement un IDE vertical.",
      "Un investissement sans prise de contrôle est un investissement de "
      "portefeuille, non un IDE."]),
'ch24-qcm-8': f(niv='comprendre', sp='c24-01', b=59,
 why=["Le manque d’information n’est pas l’explication retenue : "
      "l’ambivalence est réelle, pas illusoire.",
      "L’influence des syndicats n’est pas invoquée par Fontagné dans ce "
      "raisonnement.",
      "La volatilité des prix mondiaux n’est pas le mécanisme décrit."],
 diss="Conséquence majeure pour l’analyse politique : l’opinion d’un "
      "individu sur la mondialisation dépend de celle de ses positions qui "
      "domine son expérience."),
'ch24-qcm-9': f(niv='connaitre', sp='c24-01', b=73,
 why=["Smith défend le libre-échange mais ce n’est pas lui qui formule la "
      "thèse du doux commerce.",
      "Ricardo développe l’avantage comparatif, non l’argument pacificateur.",
      "Kindleberger est l’auteur de la théorie de la stabilité hégémonique."]),
'ch24-qcm-10': f(niv='comprendre', sp='c24-01', b=81,
 why=["L’enrichissement et la démocratie ne sont pas les maillons retenus : "
      "le mécanisme est plus direct.",
      "Le désarmement n’apparaît pas dans la chaîne causale du cours.",
      "Le passage par les institutions et le droit international décrit une "
      "autre voie vers la paix, qui n’est pas celle de Montesquieu."],
 diss="Précision décisive : le mécanisme est économique et non moral — c’est "
      "une incitation, non une vertu."),
'ch24-qcm-11': f(niv='connaitre', sp='c24-01', b=77,
 why=["1944 est l’année de la conférence de Bretton Woods.",
      "1947 est l’année de la signature du GATT.",
      "1957 est l’année du traité de Rome, postérieur à la CECA."],
 diss="Exemple à citer comme application institutionnelle du doux commerce : "
      "mettre en commun le charbon et l’acier rend la guerre matériellement "
      "plus difficile et économiquement plus coûteuse."),
'ch24-qcm-12': f(niv='comprendre', sp='c24-01', b=91,
 why=["La garantie de la paix est précisément la thèse libérale que ces "
      "analyses contestent.",
      "L’absence d’effet sur la répartition contredit le cœur de "
      "l’argument : les gains sont inégalement répartis.",
      "Les rapports de puissance ne sont pas supprimés mais déplacés sur le "
      "terrain économique."],
 diss="Contrepoint utile à Montesquieu : l’interdépendance peut aussi "
      "produire de la dépendance, donc un moyen de pression."),
'ch24-qcm-13': f(niv='connaitre', sp='c24-01', b=106,
 why=["Luttwak n’annonce pas une reprise militaire de la guerre froide.",
      "Il soutient au contraire que les rivalités de puissance persistent.",
      "La fragmentation en trois blocs n’est pas sa thèse."],
 diss="Référence de 1990 très utile pour montrer que la géoéconomie "
      "contemporaine avait été anticipée dès la fin de la guerre froide."),
'ch24-qcm-14': f(niv='raisonner', sp='c24-01', b=119,
 why=["La protection de l’emploi industriel est l’objectif du "
      "protectionnisme traditionnel, précisément dépassé ici.",
      "Ces mesures sont au contraire difficilement compatibles avec les "
      "règles de l’OMC.",
      "Elles concernent largement l’industrie et les technologies, non les "
      "seuls produits agricoles."]),
'ch24-qcm-15': f(niv='connaitre', sp='c24-01', b=132,
 why=["La suppression de tous les échanges correspondrait au découplage, "
      "voire à une rupture complète.",
      "L’assurance contre le risque de change est une technique financière "
      "sans rapport.",
      "La diversification des placements est une stratégie de portefeuille."],
 diss="Couple à retenir : découplage (rupture générale) et dérisquage "
      "(réduction ciblée des dépendances dangereuses)."),
'ch24-qcm-16': f(niv='connaitre', sp='c24-01', b=133,
 why=["La proximité géographique correspond au nearshoring, non au "
      "friendshoring.",
      "Le critère des coûts les plus faibles est celui de la mondialisation "
      "fondée sur l’efficacité, que le friendshoring abandonne.",
      "L’appartenance à l’OMC n’est pas le critère retenu : la fiabilité "
      "politique l’est."]),
'ch24-qcm-17': f(niv='raisonner', sp='c24-01', b=145,
 why=["L’affirmation « moins d’échanges, plus de croissance » n’est "
      "soutenue par aucun passage du cours.",
      "La fragmentation réduit au contraire le PIB mondial dans toutes les "
      "simulations citées.",
      "Les blocs économiques n’empêchent aucune guerre : le raisonnement du "
      "cours est exactement inverse."],
 diss="Cercle vicieux à nommer explicitement : la recherche individuelle de "
      "sécurité économique peut produire collectivement de l’insécurité "
      "géopolitique."),
'ch24-qcm-97': f(niv='connaitre', sp='c24-01', b=158,
 why=["Les pays les moins avancés constituent une catégorie statistique "
      "distincte.",
      "Le groupe de Cairns rassemble des exportateurs agricoles, dans un "
      "tout autre contexte.",
      "Les économies en transition désignent les anciens pays à économie "
      "planifiée."],
 diss="Image à réutiliser : ni éléphant ni dragon, ces puissances "
      "intermédiaires répondent à l’unilatéralisme par la multiplication des "
      "accords commerciaux."),
'ch24-questi-121': f(niv='raisonner', sp='c24-01', b=60),

# =============================================================== c24-02
'ch24-qcm-18': f(niv='connaitre', sp='c24-02', b=175,
 why=["La rivalité et l’exclusion caractérisent un bien privé ordinaire.",
      "La rivalité associée à la non-exclusion caractérise un bien commun, "
      "exposé à la surexploitation.",
      "La non-rivalité associée à l’exclusion caractérise un bien de club, "
      "comme un péage."],
 diss="Les quatre cas se distinguent par deux critères croisés : il est très "
      "payant de les poser clairement avant d’analyser le climat."),
'ch24-qcm-19': f(niv='comprendre', sp='c24-02', b=185,
 why=["Un optimum de Pareto serait précisément la situation que l’absence de "
      "coordination empêche d’atteindre.",
      "La concurrence pure et parfaite est une structure de marché, sans "
      "rapport avec ce problème d’action collective.",
      "L’équilibre budgétaire est une notion de finances publiques."],
 diss="Mécanisme central du chapitre : comportement de passager clandestin → "
      "sous-production du bien public mondial → nécessité d’une gouvernance."),
'ch24-qcm-94': f(niv='connaitre', sp='c24-02', b=259,
 why=["Le XVIᵉ siècle correspond au premier âge, celui du mercantilisme.",
      "La première mondialisation et l’impérialisme colonial forment le "
      "deuxième âge.",
      "1947 est la date du GATT, qui relève au contraire de la période "
      "d’ouverture multilatérale."]),
'ch24-qcm-95': f(niv='comprendre', sp='c24-02', b=245,
 why=["La disparition du marché n’est pas en cause : c’est sa "
      "renationalisation qui est décrite.",
      "L’inversion des termes — mercantilisme à l’intérieur, libéralisme à "
      "l’extérieur — décrirait une économie administrée ouverte, ce qui n’est "
      "pas la configuration analysée.",
      "Le consensus de Washington associait au contraire libéralisation "
      "interne et externe : il s’agit d’une rupture avec lui."]),
'ch24-qcm-96': f(niv='connaitre', sp='c24-02', b=269,
 why=["Libéralisation, dérégulation et privatisation résument le consensus "
      "de Washington, c’est-à-dire la période précédente.",
      "Croissance, inflation et chômage sont des variables "
      "macroéconomiques.",
      "Régionalisation, numérisation et financiarisation décrivent des "
      "transformations réelles, mais ne constituent pas cette typologie."],
 diss="Fil conducteur à retenir : derrière les stratégies unilatérales, "
      "bilatérales et régionales se trouve une même préoccupation, la "
      "souveraineté."),
'ch24-qcm-98': f(niv='raisonner', sp='c24-02', b=303,
 why=["L’arbitrage inflation-chômage est la courbe de Phillips, sans rapport "
      "ici.",
      "L’équilibre entre épargne et investissement est une identité "
      "macroéconomique.",
      "L’opposition court terme / long terme intervient, mais elle ne résume "
      "pas l’arbitrage central."],
 diss="Question finale du chapitre, à poser explicitement en conclusion : la "
      "société civile acceptera-t-elle le coût économique de la "
      "souveraineté ?"),
'ch24-questi-142': f(niv='raisonner', sp='c24-02', b=303),

}
