# -*- coding: utf-8 -*-
"""Chapitre 6 — La croissance économique : mesure, théories, inégalités,
soutenabilité."""

SP = {
 'c6-01': 'Définir et mesurer la croissance : Perroux, Arrous, faits stylisés de Kaldor',
 'c6-02': 'Rostow et Gerschenkron : étapes universelles ou trajectoires différenciées',
 'c6-03': 'Stagnation séculaire : Hansen, Summers, Gordon, croissance potentielle',
 'c6-04': 'Décomposer la croissance : Cobb-Douglas et Carré-Dubois-Malinvaud',
 'c6-05': 'Croissance extensive : travail, capital, FBCF et intensité capitalistique',
 'c6-06': 'Productivité du travail : mesure, déterminants et répartition des gains',
 'c6-07': 'Productivité, compétitivité, rapport Draghi, brevets et prix réels',
 'c6-08': 'Loi des trois secteurs et déversement : Clark, Fourastié, Sauvy',
 'c6-09': 'Désindustrialisation, externalisation et société hyper-industrielle (Veltz)',
 'c6-10': 'Mesurer les inégalités : interdécile, Palma, Gini, Kuznets, Milanovic',
 'c6-11': 'Revenus et patrimoines ; Harrod-Domar : la croissance déséquilibrée',
 'c6-12': 'Harrod-Domar : coefficient de capital, trois taux et fil du rasoir',
 'c6-13': 'Solow et Lucas : état stationnaire, convergence, capital humain',
 'c6-14': 'Barro, Romer, Aghion, Banerjee & Duflo : capital public, R&D, allocation',
 'c6-15': 'Institutions et développement durable : North, Acemoglu, Brundtland',
 'c6-16': 'Formes de capital, soutenabilité faible ou forte, Kuznets environnementale',
 'c6-17': 'Économie circulaire, efficacité, sobriété, effet rebond, Green Deal',
 'c6-18': 'Financer et contraindre la transition ; critiques de Fressoz et Jarrige',
}

# Questions écartées :
#   ch6-qcm-27  : taux de croissance 2024 (+1,2 %) absent du cours.
#   ch6-qcm-29  : le carré magique de Kaldor relève du cours du chapitre 1.
#   ch6-qcm-31  : le PINA relève du cours du chapitre 1 (déjà testé là-bas).
#   ch6-qcm-33  : le paradoxe d'Easterlin relève du cours du chapitre 1.
#   ch6-qcm-34  : PINA, même raison.
#   ch6-qcm-35  : la commission Stiglitz n'apparaît dans aucun cours.
#   ch6-qcm-38  : même raison.
#   ch6-vf-12   : Easterlin, même raison.
#   ch6-vf-15   : PINA, même raison.
#   ch6-open-14 : les grappes d'innovations relèvent du cours du chapitre 8.
DROP = ['ch6-qcm-27', 'ch6-qcm-29', 'ch6-qcm-31', 'ch6-qcm-33', 'ch6-qcm-34',
        'ch6-qcm-35', 'ch6-qcm-38', 'ch6-vf-12', 'ch6-vf-15', 'ch6-open-14']


def f(**kw):
    return kw


FIX = {

# ------------------------------------------------------------- c6-01 définitions
'ch6-qcm-1': f(niv='connaitre', sp='c6-01', b=6,
 exp="Perroux retient quatre éléments : une augmentation soutenue, sur une ou "
     "plusieurs périodes longues, d’un indicateur de dimension (le produit "
     "global net), en termes réels. La croissance est donc un phénomène "
     "durable et mesurable, et non une embellie passagère.",
 why=["Une hausse ponctuelle du PIB nominal ne remplit aucun des critères : "
      "ni la durée, ni la mesure en termes réels.",
      "L’amélioration du bien-être collectif relève du développement, que le "
      "cours distingue soigneusement de la croissance.",
      "La réduction de la pauvreté est une dimension du développement, pas "
      "la définition de la croissance."],
 diss="Ouvrir une dissertation sur la croissance par cette définition permet "
      "de poser d’emblée les deux bornes du sujet : le long terme et la "
      "mesure réelle."),
'ch6-qcm-2': f(niv='connaitre', sp='c6-01', b=14,
 exp="Arrous insiste sur la dimension dynamique : la croissance est un "
     "processus cumulatif d’interactions qui se traduit par une hausse "
     "continue de la productivité. Là où Perroux décrit un résultat mesurable, "
     "Arrous décrit un mécanisme.",
 why=["La hausse des exportations peut accompagner la croissance mais ne la "
      "définit pas.",
      "L’accumulation de capital physique est un facteur de croissance, non "
      "le mécanisme cumulatif qu’Arrous met au centre.",
      "La politique monétaire agit sur la conjoncture, non sur la "
      "productivité de long terme."],
 diss="Croiser Perroux et Arrous en introduction montre que la croissance est "
      "à la fois un fait mesurable et un processus : c’est la définition la "
      "plus complète."),
'ch6-qcm-4': f(niv='appliquer', sp='c6-01', b=166,
 q="Que permet d’illustrer concrètement le caractère cumulatif de la "
   "croissance, selon le cours ?",
 opts=["Un taux de 1 % par an pendant 100 ans équivaut à une hausse de 100 %",
       "Un taux de 2 % par an permet environ un doublement de la production "
       "en 35 ans",
       "Un taux de 7 % par an double la production en 7 ans exactement",
       "La production augmente de 70 % tous les vingt ans"],
 ans=1,
 why=["C’est précisément l’erreur que le cours dénonce : 1 % pendant cent ans "
      "donne une hausse bien supérieure à 100 %, parce que la croissance se "
      "multiplie au lieu de s’additionner.",
      "Le cours ne donne pas ce repère, et une telle égalité exacte "
      "n’existerait pas.",
      "Aucune règle de ce genre ne figure dans le cours."],
 exp="Le cours retient un repère simple : environ 2 % par an doublent la "
     "production en trente-cinq ans. La raison est que chaque année la "
     "croissance s’applique au niveau déjà atteint l’année précédente : la "
     "progression est exponentielle, non linéaire.",
 diss="Ce repère sert à chiffrer un argument : un écart de croissance d’un "
      "point entre deux pays, maintenu une génération, suffit à creuser des "
      "écarts de niveau de vie considérables."),
'ch6-qcm-5': f(niv='connaitre', sp='c6-01', b=55,
 exp="Un fait stylisé est une régularité statistique observée sur longue "
     "période et commune à plusieurs pays. Son intérêt méthodologique est "
     "précis : il décrit la croissance avant d’en expliquer les causes, et "
     "fournit ainsi les faits que les théories devront rendre compréhensibles.",
 why=["Un exemple inventé est une illustration pédagogique, pas une "
      "régularité observée.",
      "Un fait exceptionnel est le contraire d’une régularité.",
      "Une donnée provisoire de la comptabilité nationale est une statistique "
      "ponctuelle, pas une régularité de long terme."]),
'ch6-qcm-6': f(niv='connaitre', sp='c6-01', b=50,
 exp="Le cours associe les faits stylisés de la croissance à Kaldor. Ils "
     "aboutissent à trois constats : la croissance durable est récente, elle "
     "est instable dans le temps et elle est inégalement répartie entre pays.",
 why=["Rostow propose une théorie des étapes, pas un relevé de régularités "
      "statistiques.",
      "Solow construit un modèle explicatif de la croissance.",
      "Romer endogénéise le progrès technique : il intervient bien plus tard "
      "dans le chapitre."]),
'ch6-qcm-7': f(niv='comprendre', sp='c6-01', b=67,
 exp="Avant la Révolution industrielle, toute hausse de la production était "
     "absorbée par la croissance démographique : le niveau de vie restait "
     "stable. C’est ce que le cours appelle le régime malthusien, qui montre "
     "que la croissance moderne est historiquement située.",
 why=["Le régime keynésien n’est pas une catégorie historique de ce type.",
      "Le cours ne parle pas de « régime smithien ».",
      "Un régime schumpetérien supposerait des innovations en chaîne, soit "
      "l’inverse de la stagnation décrite."],
 diss="Partir du régime malthusien permet de montrer que la croissance n’est "
      "pas un état naturel de l’économie, mais une rupture datée de la fin du "
      "XVIIIᵉ siècle."),
'ch6-qcm-8': f(niv='connaitre', sp='c6-02', b=194,
 exp="Le sous-titre « un manifeste non communiste » dit l’intention politique "
     "du livre : écrit en pleine guerre froide, il veut montrer que le "
     "développement n’est pas réservé aux pays socialistes et que le "
     "capitalisme ouvre lui aussi une trajectoire de croissance durable.",
 why=["Ce titre évoque Smith, non Rostow.",
      "Rostow ne critique pas le libéralisme : il le défend.",
      "Le développement durable n’apparaîtra dans le débat qu’une génération "
      "plus tard."],
 diss="Rappeler ce sous-titre permet de montrer qu’une théorie de la "
      "croissance est aussi un discours daté, inscrit dans un contexte "
      "idéologique."),
'ch6-qcm-9': f(niv='connaitre', sp='c6-01', b=87,
 exp="Les Trente Glorieuses désignent la période 1945-1975 de forte "
     "croissance dans les pays développés. Le cours les cite comme illustration "
     "du fait stylisé selon lequel la croissance est inégale dans le temps : "
     "elle connaît des phases d’accélération puis de ralentissement.",
 why=["Ce sont les pays développés, et non les pays en développement, qui "
      "connaissent cette phase.",
      "L’expression désigne une période, pas un groupe de pays.",
      "La reconstruction n’est qu’une partie de la période : la croissance se "
      "poursuit bien au-delà."]),
'ch6-qcm-10': f(niv='comprendre', sp='c6-01', b=127,
 exp="La relation fondamentale du cours s’écrit : croissance du PIB = "
     "croissance de la population + croissance du PIB par habitant. Elle "
     "explique qu’un pays puisse voir sa richesse totale augmenter sans que "
     "le niveau de vie moyen progresse, si la population croît aussi vite.",
 why=["Cette égalité n’a aucun sens : le PIB ne se décompose pas en un "
      "produit par les exportations.",
      "Le PIB par habitant est un rapport à la population, non une "
      "soustraction des dépenses publiques.",
      "Cette formule mélange des grandeurs sans rapport."],
 diss="Cette décomposition permet de trancher une question classique : la "
      "croissance enrichit-elle la population ? Seule la composante « par "
      "habitant » le dit."),
'ch6-qcm-11': f(niv='connaitre', sp='c6-01', b=140,
 exp="La productivité mesure la quantité produite par unité de facteur, le "
     "travail le plus souvent. Son importance vient de la relation établie "
     "par le cours : seule une croissance fondée sur des gains de productivité "
     "permet une amélioration durable du niveau de vie par habitant.",
 why=["Le salaire horaire est un prix du travail, qui peut d’ailleurs évoluer "
      "indépendamment de la productivité à court terme.",
      "Le taux d’emploi mesure la part de la population qui travaille, pas "
      "l’efficacité de ce travail.",
      "La valeur ajoutée générée par le capital correspondrait à une "
      "productivité du capital, pas du travail."]),
'ch6-qcm-22': f(niv='comprendre', sp='c6-01', b=104,
 exp="Le cours constate que certains pays connaissent un rattrapage rapide "
     "(Japon, Asie de l’Est, Chine) tandis que d’autres restent durablement "
     "en retard : les écarts de PIB par habitant demeurent importants et la "
     "convergence n’est pas automatique.",
 why=["Les pays émergents en rattrapage bénéficient aussi de la croissance : "
      "l’affirmation est trop absolue.",
      "Les différences de mesure existent mais ne sont pas la raison avancée "
      "par le cours.",
      "La répartition des ressources naturelles n’est pas l’explication "
      "retenue : le cours insiste sur les trajectoires et les institutions."],
 diss="Cette non-convergence est le fait que les théories devront expliquer : "
      "Solow prédit une convergence conditionnelle, les modèles endogènes "
      "admettent au contraire des écarts cumulatifs."),
'ch6-qcm-24': f(niv='connaitre', sp='c6-01', b=2,
 exp="La croissance se mesure par l’évolution du PIB en volume, c’est-à-dire "
     "corrigé de l’inflation : on parle de croissance réelle, et non nominale. "
     "Sans cette correction, une simple hausse générale des prix "
     "apparaîtrait comme un enrichissement.",
 why=["Le PIB nominal mêle effet prix et effet volume : il surestime la "
      "croissance en période d’inflation.",
      "Le chômage renseigne sur l’emploi, pas sur la production.",
      "L’IDH mesure le développement humain, qui relève d’une autre notion."]),
'ch6-qcm-26': f(niv='comprendre', sp='c6-01', b=157,
 exp="La croissance s’applique chaque année au niveau déjà atteint : elle "
     "progresse par multiplication et non par addition. C’est ce mécanisme "
     "qui fait qu’une différence apparemment faible entre deux taux produit, "
     "sur plusieurs décennies, des écarts de richesse considérables.",
 why=["Augmenter de la même quantité chaque année serait précisément une "
      "progression linéaire, que le cours oppose à la réalité.",
      "La politique monétaire agit sur la conjoncture, pas sur la forme "
      "mathématique de la croissance.",
      "Le taux de population active intervient dans la décomposition du PIB, "
      "pas dans son caractère exponentiel."]),
'ch6-qcm-37': f(niv='appliquer', sp='c6-01', b=2,
 exp="En première approximation, le taux en volume s’obtient en retranchant "
     "l’évolution des prix au taux en valeur : c’est l’opération de "
     "déflation. Si le PIB en valeur progresse de 4 % et les prix de 3 %, la "
     "croissance réelle est voisine de 1 %. C’est une approximation, exacte "
     "seulement pour de faibles taux.",
 why=["Ajouter l’évolution des prix revient à compter l’inflation deux fois.",
      "Multiplier par l’indice des prix amplifie l’effet prix au lieu de "
      "l’éliminer.",
      "La division par l’indice est la forme rigoureuse du calcul sur les "
      "niveaux, non sur les taux : appliquée aux taux, elle n’a pas de sens."]),
'ch6-vf-2': f(niv='connaitre', sp='c6-01', b=166,
 exp="Le cours retient ce repère : environ 2 % par an doublent la production "
     "en trente-cinq ans. Il illustre la loi de la croissance cumulée — la "
     "croissance agit lentement mais puissamment, d’autant plus qu’elle est "
     "régulière et durable."),
'ch6-vf-3': f(niv='comprendre', sp='c6-01', b=50,
 exp="C’est l’inverse : les faits stylisés établissent que la croissance est "
     "instable, qu’elle évolue par cycles et grandes phases historiques, et "
     "qu’elle est inégalement répartie entre les pays. Sa régularité "
     "apparente sur très longue période masque des accélérations, des "
     "ralentissements et des crises."),
'ch6-vf-7': f(niv='comprendre', sp='c6-01', b=32,
 exp="Le cours est explicite : la croissance est souvent une condition "
     "nécessaire du développement, mais elle n’est pas suffisante. Un pays "
     "peut croître sans réduire ses inégalités, sans améliorer le bien-être "
     "et sans protéger son environnement.",
 diss="Cette formule — nécessaire mais non suffisante — est la charnière de "
      "tout sujet opposant croissance et développement."),
'ch6-vf-9': f(niv='connaitre', sp='c6-01', b=2,
 exp="Le PIB en volume est le PIB nominal corrigé de l’inflation. C’est la "
     "grandeur pertinente pour mesurer la croissance, puisqu’elle isole "
     "l’évolution des quantités produites de celle des prix."),
'ch6-vf-10': f(niv='comprendre', sp='c6-02', b=194,
 exp="Rostow s’oppose explicitement au modèle socialiste : son livre de 1960 "
     "est sous-titré « un manifeste non communiste ». Il veut montrer que le "
     "capitalisme ouvre lui aussi une trajectoire de croissance durable, "
     "aboutissant à la société de consommation de masse."),
'ch6-vf-13': f(niv='connaitre', sp='c6-01', b=156,
 exp="La croissance est cumulative parce qu’elle fonctionne selon une "
     "logique exponentielle : chaque année, le taux s’applique au niveau déjà "
     "augmenté de l’année précédente. Le temps devient alors une variable "
     "centrale de la dynamique."),
'ch6-vf-14': f(niv='comprendre', sp='c6-01', b=58,
 exp="La croissance durable est un phénomène récent à l’échelle de "
     "l’histoire humaine : elle apparaît avec la Révolution industrielle, à "
     "la fin du XVIIIᵉ siècle au Royaume-Uni. Avant cela, les économies "
     "agricoles connaissaient une productivité faible et un niveau de vie "
     "globalement stable."),
'ch6-vf-17': f(niv='connaitre', sp='c6-01', b=87,
 exp="Les Trente Glorieuses (1945-1975) sont au contraire la période de plus "
     "forte croissance qu’aient connue les pays développés. Le ralentissement "
     "commence dans les années 1970."),
'ch6-vf-18': f(niv='comprendre', sp='c6-01', b=138,
 q="Selon le cours, seule une croissance fondée sur des gains de productivité "
   "permet une amélioration durable du niveau de vie par habitant.",
 ans=True,
 exp="La croissance démographique peut accroître le PIB total, mais elle "
     "répartit la richesse entre davantage d’habitants. Seuls les gains de "
     "productivité permettent de produire davantage avec la même quantité de "
     "travail, donc d’élever durablement le revenu par habitant.",
 diss="C’est l’argument qui justifie de placer la productivité au cœur de "
      "tout sujet sur le niveau de vie, et non la démographie."),
'ch6-vf-19': f(niv='appliquer', sp='c6-01', b=2,
 exp="En période d’inflation, le taux en valeur inclut l’effet prix positif "
     "et dépasse donc le taux en volume. Les deux coïncident si les prix sont "
     "stables ; en cas de déflation, le taux en valeur serait au contraire "
     "inférieur — l’affirmation est donc vraie pour la situation ordinaire "
     "décrite par le cours, où les prix augmentent."),
'ch6-open-1': f(niv='connaitre', sp='c6-01', b=6,
 ans={'modele': "François Perroux définit la croissance comme "
      "« l’augmentation soutenue pendant une ou plusieurs périodes longues "
      "d’un indicateur de dimension, pour une nation, le produit global net "
      "en termes réels ». Quatre éléments sont à retenir : l’augmentation "
      "soutenue, la longue période, le caractère quantitatif de la mesure et "
      "l’expression en termes réels.",
      'cles': [{'f': ['soutenue', 'durable', 'continue'],
                'l': 'une augmentation soutenue'},
               {'f': ['longue', 'periode', 'long terme'],
                'l': 'sur une ou plusieurs périodes longues'},
               {'f': ['indicateur', 'dimension', 'produit global'],
                'l': 'un indicateur de dimension (produit global net)'},
               {'f': ['reel', 'volume', 'inflation'],
                'l': 'en termes réels'}]},
 exp="L’intérêt de cette définition est de refuser à la fois le court terme "
     "et le nominal : une embellie d’un trimestre ou une hausse des prix ne "
     "sont pas de la croissance."),

# ------------------------------------------------- c6-02 Rostow, Gerschenkron
'ch6-qcm-36': f(niv='connaitre', sp='c6-02', b=201,
 exp="Rostow soutient que toutes les économies traversent cinq étapes "
     "successives : société traditionnelle, conditions préalables au "
     "décollage, décollage (take-off), marche vers la maturité, ère de la "
     "consommation de masse. Les dates varient, mais la trajectoire est "
     "présentée comme universelle.",
 why=["L’épargne joue un rôle dans le décollage, mais le modèle ne s’y réduit "
      "pas.",
      "Rostow ne conditionne pas la croissance à l’aide internationale.",
      "Son modèle décrit au contraire l’ensemble des pays, pionniers "
      "compris."],
 diss="Les cinq étapes servent de repoussoir utile : c’est leur linéarité que "
      "Gerschenkron, puis les économistes tiers-mondistes, contestent."),
'ch6-qcm-20': f(niv='comprendre', sp='c6-02', b=104,
 exp="La convergence désigne la tendance des pays pauvres à croître plus vite "
     "que les pays riches et à rattraper leur niveau de vie. Le cours souligne "
     "aussitôt la nuance décisive : cette convergence n’est pas automatique, "
     "et certains pays restent durablement en retard.",
 why=["La convergence des politiques monétaires est une question "
      "institutionnelle propre à la zone euro.",
      "L’uniformisation mondiale des salaires n’est observée nulle part.",
      "La convergence des taux d’intérêt est un phénomène financier, sans "
      "rapport avec les niveaux de vie."]),

# ----------------------------------------------- c6-03 stagnation séculaire
'ch6-qcm-23': f(niv='connaitre', sp='c6-03', b=507,
 q="Qu’est-ce que la croissance potentielle ?",
 opts=["La croissance observée dans les statistiques officielles",
       "Le rythme de croissance qu’une économie pourrait atteindre si tous "
       "ses facteurs de production étaient pleinement utilisés, sans tension "
       "inflationniste",
       "La croissance prévue par les organismes internationaux pour l’année "
       "suivante",
       "La croissance calculée à parité de pouvoir d’achat"],
 ans=1,
 why=["C’est la définition de la croissance effective, que le cours oppose "
      "précisément à la croissance potentielle.",
      "Une prévision est une anticipation conjoncturelle, alors que la "
      "croissance potentielle est une norme structurelle.",
      "La parité de pouvoir d’achat est une méthode de conversion entre "
      "monnaies, sans lien avec cette notion."],
 exp="La croissance potentielle est une croissance théorique : la « vitesse "
     "de croisière » soutenable de l’économie. Elle dépend de facteurs "
     "structurels — productivité, démographie, stock de capital, progrès "
     "technique. Sur la période 2009-2018 étudiée par le cours, elle est "
     "estimée à environ 0,8 %.",
 diss="Elle sert de norme de référence : c’est en la comparant à la "
      "croissance effective qu’on diagnostique une surchauffe ou une "
      "sous-activité."),
'ch6-qcm-21': f(niv='connaitre', sp='c6-03', b=547,
 exp="L’output gap est l’écart entre la croissance effective et la croissance "
     "potentielle. Trois situations sont possibles : nul, l’économie est à "
     "l’équilibre ; positif, elle est en surchauffe avec risque "
     "d’inflation ; négatif, elle est en sous-activité, avec chômage et "
     "capacités inutilisées.",
 why=["L’écart entre PIB nominal et PIB réel mesure l’effet des prix, pas "
      "celui du cycle.",
      "L’écart entre importations et exportations est le solde commercial.",
      "L’écart au plein emploi est une mesure du sous-emploi, qui "
      "accompagne un output gap négatif sans s’y confondre."],
 diss="C’est l’outil qui relie dans une même analyse croissance, chômage et "
      "inflation."),
'ch6-vf-8': f(niv='comprendre', sp='c6-03', b=550,
 exp="Un output gap positif signifie que la croissance effective dépasse la "
     "croissance potentielle : l’économie produit plus qu’elle ne peut "
     "soutenir durablement. Les conséquences possibles sont des pénuries de "
     "capacités, une hausse des salaires et un risque d’inflation."),
'ch6-open-10': f(niv='connaitre', sp='c6-03', b=373,
 ans={'modele': "La stagnation séculaire désigne une situation dans laquelle "
      "une économie connaît une croissance durablement faible, voire quasi "
      "nulle, sur une longue période. Le terme « séculaire » marque qu’il "
      "s’agit d’une tendance de long terme et non d’une simple fluctuation "
      "conjoncturelle. L’idée centrale est que la croissance n’est ni "
      "automatique ni éternelle, et que le lien entre progrès technique et "
      "croissance n’est pas mécanique.",
      'cles': [{'f': ['faible', 'nulle', 'ralentissement'],
                'l': 'une croissance durablement faible'},
               {'f': ['long', 'seculaire', 'durable', 'prolonge'],
                'l': 'sur une longue période, non conjoncturelle'},
               {'f': ['automatique', 'progres technique', 'mecanique'],
                'l': 'remise en cause du lien automatique entre progrès technique et croissance'}]},
 exp="Le concept est formulé par Hansen en 1938, oublié pendant les Trente "
     "Glorieuses, puis réactivé par Summers en 2013 et diffusé en France par "
     "Daniel Cohen."),
'ch6-aut195-7': f(niv='connaitre', sp='c6-03', b=397,
 exp="Observant après 2008 une croissance faible malgré des taux d’intérêt "
     "très bas et un investissement qui ne repart pas, Larry Summers "
     "réutilise l’expression en 2013 et y voit un déséquilibre structurel "
     "durable entre l’épargne et l’investissement. En France, Daniel Cohen "
     "diffuse le débat avec « Le monde est clos et le désir infini » (2015).",
 why=["Krugman partage l’explication par la demande, mais ce n’est pas lui "
      "qui réactive l’expression.",
      "Daniel Cohen diffuse le débat en France ; il ne le relance pas aux "
      "États-Unis.",
      "Robert Gordon défend l’explication concurrente, par l’offre."],
 diss="Hansen 1938, Summers 2013, Cohen 2015 : cette chronologie montre qu’un "
      "concept économique peut sommeiller un demi-siècle avant d’être "
      "réactivé par les faits."),

# --------------------------------------------- c6-04 décomposer la croissance
'ch6-aut195-4': f(niv='connaitre', sp='c6-04', b=629,
 exp="Jean Carré, Paul Dubois et Edmond Malinvaud publient « La croissance "
     "française » en 1972. Ils transposent à la France la méthode de Solow : "
     "une fonction de production de type Cobb-Douglas permet de mesurer la "
     "contribution du capital et du travail, puis d’isoler le résidu "
     "d’efficacité globale.",
 why=["Perroux, Sauvy et Fourastié interviennent ailleurs dans le chapitre, "
      "sur la définition de la croissance et la transformation sectorielle.",
      "Aglietta, Boyer et Lipietz sont des théoriciens de la régulation.",
      "Piketty, Saez et Zucman travaillent sur les inégalités."]),

# ------------------------------------------------ c6-05 croissance extensive
'ch6-qcm-30': f(niv='connaitre', sp='c6-05', b=718,
 exp="Les deux facteurs classiques sont le capital et le travail. La "
     "croissance obtenue en augmentant leur quantité est dite extensive ; "
     "celle qui provient d’une utilisation plus efficace des mêmes facteurs "
     "est dite intensive.",
 why=["La technologie n’est pas un facteur de production au même titre : "
      "elle apparaît dans la PGF, qui mesure l’efficacité des facteurs.",
      "La monnaie n’est pas un facteur de production.",
      "Énergie et information ne figurent pas parmi les facteurs retenus par "
      "la décomposition classique."]),
'ch6-open-2': f(niv='comprendre', sp='c6-05', b=721,
 ans={'modele': "La croissance extensive provient de l’augmentation "
      "quantitative des facteurs de production : plus de travail (démographie, "
      "taux d’activité, durée du travail) et plus de capital (investissement, "
      "FBCF). La croissance intensive provient de l’amélioration de "
      "l’efficacité de ces facteurs, mesurée par la productivité globale des "
      "facteurs : on produit davantage avec la même quantité de travail et de "
      "capital. La première rencontre des limites démographiques et des "
      "rendements décroissants ; la seconde est seule durable à long terme.",
      'cles': [{'f': ['quantite', 'plus de travail', 'plus de capital', 'extensive'],
                'l': 'extensive : augmentation quantitative des facteurs'},
               {'f': ['efficacite', 'productivite', 'pgf', 'progres technique'],
                'l': 'intensive : amélioration de l’efficacité des facteurs'},
               {'f': ['limite', 'decroissant', 'demographique', 'durable'],
                'l': 'les limites de l’extensive justifient le rôle de l’intensive'}]},
 exp="Le cours donne des exemples de classement : croissance plutôt "
     "intensive au Danemark et en Allemagne, plutôt extensive en France et "
     "aux États-Unis."),

# ----------------------------------------------- c6-06 productivité du travail
'ch6-open-3': f(niv='comprendre', sp='c6-06', b=1016,
 q="Comment mesure-t-on la productivité globale des facteurs, et quelle "
   "difficulté cette méthode soulève-t-elle ?",
 ans={'modele': "La productivité globale des facteurs mesure ce qui, dans la "
      "croissance, ne s’explique ni par l’augmentation du travail ni par "
      "celle du capital. Elle se calcule par déduction : croissance de la "
      "production moins contribution du travail moins contribution du "
      "capital. C’est donc un résidu, qui capte le progrès technique, "
      "l’innovation, l’organisation, le savoir-faire et la qualité du capital "
      "humain.",
      'cles': [{'f': ['ni le travail', 'pas explique', 'residu', 'deduction'],
                'l': 'un résidu, mesuré par déduction'},
               {'f': ['progres technique', 'innovation', 'efficacite'],
                'l': 'elle capte le progrès technique et l’innovation'},
               {'f': ['organisation', 'savoir', 'capital humain', 'formation'],
                'l': 'mais aussi l’organisation et le capital humain'}]},
 exp="D’où les deux formules du cours : certains y voient une « manne tombée "
     "du ciel », d’autres la mesure de « notre part d’ignorance ». On observe "
     "ses effets sans savoir précisément comment elle se forme."),
'ch6-qcm-32': f(niv='connaitre', sp='c6-06', b=1019,
 exp="La PGF est la part de la croissance qui reste après avoir imputé "
     "l’augmentation du capital et celle du travail. Elle est attribuée au "
     "progrès technique au sens large : innovations, organisation, "
     "apprentissage, diffusion des technologies.",
 why=["La productivité du travail est un rapport entre la production et le "
      "seul facteur travail.",
      "Le rapport entre PIB et nombre d’entreprises n’a pas de sens "
      "économique établi.",
      "L’efficacité des politiques de R&D est une question d’évaluation des "
      "politiques publiques, non une définition de la PGF."]),
'ch6-open-5': f(niv='comprendre', sp='c6-06', b=705,
 ans={'modele': "Le résidu est la part de la croissance qui reste inexpliquée "
      "après avoir comptabilisé l’apport du travail et celui du capital. "
      "Solow l’assimile au progrès technique, qu’il décrit comme une « manne "
      "tombée du ciel » : une richesse qui apparaît sans que l’on sache d’où "
      "elle vient. D’autres économistes préfèrent dire que ce résidu mesure "
      "notre ignorance, car on y range pêle-mêle l’organisation, les "
      "compétences, la technologie et les institutions.",
      'cles': [{'f': ['inexplique', 'reste', 'residu', 'deduction'],
                'l': 'la part inexpliquée par le travail et le capital'},
               {'f': ['progres technique', 'manne', 'ciel', 'exogene'],
                'l': 'assimilée au progrès technique, exogène'},
               {'f': ['ignorance', 'organisation', 'institution'],
                'l': 'ou, selon d’autres, la mesure de notre ignorance'}]},
 exp="Dans le cas français des Trente Glorieuses, ce résidu représente 3,1 "
     "points sur 5,2, soit environ 60 % de la croissance : l’essentiel de "
     "celle-ci échappe donc à la simple accumulation des facteurs."),
'ch6-open-11': f(niv='comprendre', sp='c6-01', b=155,
 ans={'modele': "La croissance est cumulative pour deux raisons que le cours "
      "articule. Mathématiquement, le taux de croissance s’applique chaque "
      "année au niveau déjà atteint : la progression est exponentielle, non "
      "linéaire, et les effets s’accumulent. Économiquement, la production "
      "d’aujourd’hui dégage des revenus et de l’épargne qui financent "
      "l’investissement de demain, donc une production plus élevée encore. "
      "C’est le processus cumulatif d’interactions dont parle Arrous.",
      'cles': [{'f': ['exponentiel', 'niveau atteint', 'multiplication'],
                'l': 'le taux s’applique au niveau déjà atteint'},
               {'f': ['epargne', 'investissement', 'revenu'],
                'l': 'la production finance l’investissement futur'},
               {'f': ['productivite', 'arrous', 'interaction'],
                'l': 'processus cumulatif d’interactions et de productivité'}]},
 exp="C’est ce caractère cumulatif qui explique qu’un écart de croissance "
     "faible mais durable creuse des divergences considérables de niveau de "
     "vie entre pays."),
'ch6-open-9': f(niv='raisonner', sp='c6-10', b=1939,
 q="Comment Kuznets explique-t-il que les inégalités augmentent d’abord au "
   "cours du développement ?",
 ans={'modele': "Dans la première phase, l’économie passe de l’agriculture à "
      "l’industrie. Les écarts de productivité entre les deux secteurs sont "
      "importants et les salaires industriels sont plus élevés : les écarts "
      "de revenus se creusent entre secteurs, donc entre individus. Dans la "
      "seconde phase, la généralisation de l’éducation, la diffusion du "
      "progrès technique, l’urbanisation complète et la montée de la classe "
      "moyenne réduisent ces écarts, mais surtout la redistribution — hausse "
      "des recettes fiscales, politiques sociales — corrige les inégalités "
      "produites par le marché.",
      'cles': [{'f': ['agricole', 'industrie', 'secteur', 'transfert'],
                'l': 'le passage de l’agriculture à l’industrie'},
               {'f': ['productivite', 'salaire', 'ecart'],
                'l': 'des écarts de productivité et de salaires entre secteurs'},
               {'f': ['education', 'classe moyenne', 'urbanisation'],
                'l': 'puis généralisation de l’éducation et montée de la classe moyenne'},
               {'f': ['redistribution', 'fiscal', 'social', 'etat'],
                'l': 'et surtout la redistribution par l’État'}]},
 exp="Le cours insiste sur le second point : la baisse des inégalités n’est "
     "pas mécanique, elle dépend du niveau de redistribution, du système "
     "fiscal et des institutions. Les inégalités sont aussi un choix de "
     "société.",
 diss="Cette précision est décisive : elle permet d’expliquer pourquoi la "
      "phase descendante prévue par Kuznets ne s’est pas poursuivie après "
      "1980."),

# ---------------------------------------- c6-07 productivité et compétitivité
'ch6-open-13': f(niv='comprendre', sp='c6-07', b=1216,
 q="Pourquoi une innovation ne fait-elle pas immédiatement baisser les prix ?",
 ans={'modele': "L’entreprise qui innove a engagé des coûts importants de "
      "R&D et protège son innovation par un brevet, qui la place "
      "temporairement en situation de monopole. Elle répercute donc le coût "
      "de l’innovation sur le prix : le produit nouveau est cher au "
      "lancement. Ce n’est qu’ensuite, avec la diffusion massive, "
      "l’élargissement des unités de production et les économies d’échelle, "
      "que le coût unitaire diminue et que le prix baisse. Le progrès "
      "technique profite donc d’abord à l’innovateur, puis à la collectivité.",
      'cles': [{'f': ['brevet', 'monopole', 'propriete'],
                'l': 'le brevet confère un monopole temporaire'},
               {'f': ['cout', 'r&d', 'recherche', 'repercute'],
                'l': 'les coûts de R&D sont répercutés sur le prix'},
               {'f': ['economie d echelle', 'diffusion', 'masse', 'taille'],
                'l': 'la baisse vient ensuite des économies d’échelle'}]},
 exp="Le cours illustre par les premiers téléviseurs, téléphones et "
     "automobiles : chers au lancement, accessibles après la diffusion de "
     "masse.",
 diss="Ce double effet du progrès technique — hausse des prix à court terme, "
      "baisse à moyen terme — évite la présentation naïve de l’innovation "
      "comme bienfait immédiat."),
'ch6-open-15': f(niv='comprendre', sp='c6-08', b=1341,
 ans={'modele': "Le brevet protège l’innovateur, sécurise son investissement "
      "en R&D et lui garantit une rémunération temporaire : c’est un droit de "
      "propriété favorable à l’innovation, et Romer comme Aghion y voient une "
      "mission légitime de l’État. Mais le cours ajoute aussitôt la limite : "
      "certaines entreprises déposent des brevets défensifs, non pour "
      "exploiter une innovation mais pour bloquer l’entrée de concurrents, et "
      "l’accumulation de technologies brevetées engendre des coûts de "
      "transaction — identifier les détenteurs, négocier des licences — qui "
      "découragent l’innovation.",
      'cles': [{'f': ['protege', 'remuneration', 'rentabilis', 'securise'],
                'l': 'il sécurise la rémunération de la R&D'},
               {'f': ['monopole', 'temporaire', 'droit de propriete'],
                'l': 'par un monopole temporaire, droit de propriété'},
               {'f': ['defensif', 'bloquer', 'verrouill', 'transaction'],
                'l': 'mais brevets défensifs et coûts de transaction peuvent freiner'}]},
 exp="La propriété intellectuelle protège donc l’innovation mais peut aussi "
     "en freiner la diffusion : tout l’enjeu est l’équilibre entre les deux."),

# ---------------------------------------------- c6-13 Solow, Lucas, convergence
'ch6-qcm-12': f(niv='comprendre', sp='c6-13', b=2338,
 exp="Chez Solow, le progrès technique est exogène : il est le moteur ultime "
     "de la croissance par tête, mais le modèle ne dit pas comment il est "
     "produit. D’où l’image de la « manne tombée du ciel » et le statut de "
     "résidu de la PGF.",
 why=["C’est précisément la position des modèles de croissance endogène, qui "
      "naissent de cette insatisfaction.",
      "La hausse de la productivité due au capital est l’effet de "
      "l’accumulation, que Solow distingue du progrès technique.",
      "L’augmentation du nombre de travailleurs relève de la croissance "
      "extensive."],
 diss="C’est la limite centrale du modèle, et le point de départ de Romer, "
      "Lucas et Barro."),
'ch6-qcm-13': f(niv='connaitre', sp='c6-13', b=2397,
 exp="La croissance est dite endogène quand ses moteurs sont produits par "
     "l’activité économique elle-même : accumulation de connaissances et R&D "
     "chez Romer, capital humain chez Lucas, capital public chez Barro. Le "
     "progrès technique n’est plus une donnée extérieure mais le résultat de "
     "décisions économiques.",
 why=["Une croissance expliquée par des facteurs externes est au contraire "
      "une croissance exogène, à la Solow.",
      "« Endogène » ne signifie pas « intérieur au territoire » : le terme "
      "porte sur le modèle, non sur les frontières.",
      "L’austérité n’a aucun rapport avec cette notion."]),
'ch6-qcm-14': f(niv='comprendre', sp='c6-13', b=2515,
 exp="Les trois modèles endogénéisent la croissance par trois canaux "
     "distincts : la R&D et l’accumulation de connaissances chez Romer, le "
     "capital humain — formation et santé — chez Lucas, le capital public "
     "productif — infrastructures, éducation, R&D financée publiquement — "
     "chez Barro. Dans les trois cas, le mécanisme est le même : des "
     "externalités positives qui empêchent les rendements de décroître.",
 why=["Ces trois facteurs sont ceux de la croissance extensive classique.",
      "Exportations, investissement étranger et politique monétaire ne sont "
      "pas les moteurs retenus par ces modèles.",
      "Les trois secteurs de Clark et Fourastié relèvent d’une autre partie "
      "du chapitre."]),
'ch6-qcm-18': f(niv='connaitre', sp='c6-13', b=2407,
 exp="Le capital humain désigne le stock de caractéristiques physiques et "
     "intellectuelles incorporées aux individus et valorisables "
     "économiquement. Les deux variables essentielles sont la formation — "
     "notamment l’allongement des études — et la santé. Il ne s’agit donc "
     "plus de la quantité de travail, mais de sa qualité.",
 why=["Machines et équipements constituent le capital physique.",
      "Le capital financier placé en bourse n’est pas incorporé aux "
      "individus.",
      "Les droits de propriété intellectuelle relèvent du capital "
      "technologique."]),
'ch6-qcm-19': f(niv='comprendre', sp='c6-13', b=2390,
 exp="La critique centrale est que le moteur ultime de la croissance par "
     "tête — le progrès technique — reste exogène : le modèle montre qu’il "
     "est décisif mais ne dit pas comment le produire. C’est cette lacune que "
     "les théories de la croissance endogène viendront combler.",
 why=["Le capital physique est au contraire au cœur du modèle, avec "
      "l’épargne et l’amortissement.",
      "Solow ne prédit pas une croissance négative mais une croissance par "
      "tête qui s’éteint à l’état stationnaire.",
      "Le modèle est construit pour les économies développées de "
      "l’après-guerre, et sa portée est générale."]),
'ch6-qcm-28': f(niv='comprendre', sp='c6-13', b=2396,
 exp="L’apport des théories endogènes est d’expliquer le progrès technique "
     "par des décisions économiques : investir en R&D, se former, financer "
     "des infrastructures. La croissance devient alors cumulative et "
     "auto-entretenue, et l’état stationnaire n’est plus une fatalité.",
 why=["C’est l’inverse : elles endogénéisent ce que Solow laissait exogène.",
      "Elles rendent au contraire la convergence incertaine, puisque les "
      "rendements croissants peuvent creuser les écarts.",
      "Les dotations en ressources naturelles ne jouent aucun rôle dans ces "
      "modèles."]),
'ch6-qcm-39': f(niv='comprendre', sp='c6-13', b=2363,
 q="Qu’appelle-t-on l’état stationnaire dans le modèle de Solow ?",
 opts=["Le niveau de capital par tête où l’investissement compense exactement "
       "l’usure du capital, de sorte que la production par tête devient "
       "constante",
       "Une situation où la production totale cesse d’augmenter, quelle que "
       "soit la démographie",
       "Un sentier de croissance sans inflation",
       "Le moment où l’épargne devient nulle"],
 ans=0,
 why=["La production totale peut continuer de croître avec la population : "
      "c’est la production par tête qui se stabilise.",
      "L’inflation n’intervient pas dans le modèle de Solow.",
      "L’épargne reste au contraire positive à l’état stationnaire : elle "
      "finance exactement le remplacement du capital usé."],
 exp="L’état stationnaire découle de la productivité marginale décroissante "
     "du capital : à mesure que k augmente, l’investissement s f(k) progresse "
     "de moins en moins vite tandis que l’amortissement δk croît "
     "proportionnellement. Au point où les deux s’égalisent, le capital par "
     "tête cesse d’augmenter. La croissance du niveau de vie s’éteint donc si "
     "rien d’autre ne change.",
 diss="C’est la limite interne du modèle, et la raison pour laquelle Solow "
      "doit introduire le progrès technique pour prolonger la croissance."),
'ch6-vf-4': f(niv='comprendre', sp='c6-13', b=2338,
 exp="Dans le modèle de Solow, le progrès technique est exogène : il n’est ni "
     "expliqué ni produit par le modèle. Ce sont Romer, Lucas et Barro qui, "
     "dans les années 1980, l’expliqueront par la R&D, le capital humain et "
     "le capital public."),
'ch6-vf-6': f(niv='raisonner', sp='c6-13', b=2545,
 exp="C’est l’inverse. Chez Solow, les rendements décroissants du capital "
     "assurent une convergence conditionnelle : les pays à faible capital par "
     "tête ont un rendement du capital plus élevé et rattrapent plus vite. "
     "Les théories endogènes supposent au contraire des rendements constants "
     "voire croissants, ce qui permet aux écarts entre pays de se creuser "
     "durablement.",
 diss="Cette opposition est très rentable : selon le modèle retenu, le "
      "rattrapage est mécanique ou au contraire improbable sans politique "
      "publique."),
'ch6-open-6': f(niv='comprendre', sp='c6-13', b=2397,
 ans={'modele': "Les théories de la croissance endogène expliquent le progrès "
      "technique par des décisions économiques des agents : investir dans la "
      "R&D (Romer), se former et se soigner (Lucas), financer des "
      "infrastructures et la recherche publique (Barro). Ces investissements "
      "produisent des externalités positives : le rendement social dépasse le "
      "rendement privé, les rendements ne sont plus nécessairement "
      "décroissants, et la croissance devient cumulative et auto-entretenue. "
      "Il en découle une justification structurelle — et non conjoncturelle — "
      "de l’intervention de l’État.",
      'cles': [{'f': ['decision', 'r&d', 'education', 'investissement'],
                'l': 'le progrès technique résulte de décisions économiques'},
               {'f': ['externalite', 'spillover', 'rendement social'],
                'l': 'des externalités positives : rendement social > rendement privé'},
               {'f': ['cumulative', 'auto entretenue', 'stationnaire'],
                'l': 'croissance cumulative, l’état stationnaire n’est plus fatal'},
               {'f': ['etat', 'public', 'intervention', 'structurel'],
                'l': 'justification structurelle de l’intervention publique'}]},
 exp="Le point commun des trois auteurs est donc double : un capital "
     "spécifique qui s’accumule sans se déprécier comme une machine, et des "
     "externalités qui justifient que l’État intervienne."),
'ch6-open-7': f(niv='comprendre', sp='c6-13', b=2434,
 ans={'modele': "Chez Lucas, l’accumulation de capital humain — formation et "
      "santé — accroît la productivité de celui qui se forme, mais produit "
      "surtout des externalités positives : un salarié formé améliore "
      "l’efficacité collective, et un environnement riche en compétences "
      "élève la productivité globale. Le rendement social du capital humain "
      "dépasse donc son rendement privé. La productivité marginale de la "
      "formation est constante voire croissante, le capital humain ne s’use "
      "pas comme une machine : l’état stationnaire n’est plus une fatalité et "
      "la croissance peut être auto-entretenue.",
      'cles': [{'f': ['formation', 'education', 'sante', 'competence'],
                'l': 'formation et santé élèvent la qualité du travail'},
               {'f': ['externalite', 'collectif', 'rendement social'],
                'l': 'externalités positives : rendement social supérieur au privé'},
               {'f': ['decroissant', 'stationnaire', 'cumulative'],
                'l': 'rendements non décroissants, croissance auto-entretenue'},
               {'f': ['etat', 'public', 'sous investi'],
                'l': 'd’où un sous-investissement privé que l’État doit corriger'}]},
 exp="C’est ce dernier point qui justifie l’intervention : les agents ne "
     "prennent pas en compte l’ensemble des bénéfices collectifs de leur "
     "formation, si bien que le marché seul investit trop peu dans "
     "l’éducation."),
'ch6-aut195-3': f(niv='connaitre', sp='c6-13', b=2406,
 exp="Gary Becker popularise la notion de capital humain dans les années "
     "1960 : le stock de caractéristiques physiques et intellectuelles "
     "incorporées aux individus et valorisables économiquement. Lucas s’en "
     "servira en 1988 pour endogénéiser la croissance.",
 why=["Solow raisonne sur le capital physique et laisse le progrès technique "
      "exogène.",
      "Romer met au centre l’accumulation des connaissances et la R&D.",
      "Lucas utilise le concept mais ne l’a pas forgé."]),

# ------------------------------- c6-14 Barro, Romer, Aghion, Banerjee & Duflo
'ch6-qcm-15': f(niv='comprendre', sp='c6-14', b=2599,
 q="Qu’est-ce que la destruction créatrice, telle que le chapitre la mobilise "
   "à propos d’Aghion ?",
 opts=["La destruction de ressources naturelles pour financer la croissance",
       "Le processus par lequel chaque innovation rend obsolète la technologie "
       "antérieure et renouvelle le tissu productif",
       "La faillite des entreprises mal gérées dans un marché concurrentiel",
       "La réallocation des ressources après une crise financière"],
 ans=1,
 why=["La destruction dont il s’agit est technologique et organisationnelle, "
      "non écologique.",
      "Des faillites peuvent accompagner le processus, mais elles n’en sont "
      "pas la définition : ce qui compte est l’obsolescence provoquée par "
      "l’innovation.",
      "La réallocation après une crise est un phénomène conjoncturel, alors "
      "que la destruction créatrice est le moteur ordinaire de la croissance."],
 exp="Dans le modèle d’Aghion et Howitt, la croissance procède d’innovations "
     "successives : chacune rend l’ancienne technologie obsolète. Le tissu "
     "productif se renouvelle donc en permanence, ce qui suppose des "
     "destructions — emplois, entreprises, savoir-faire — et explique pourquoi "
     "l’État doit à la fois garantir la concurrence et amortir les coûts du "
     "processus.",
 diss="Le mot clé pour la copie est « renouvellement » : la croissance n’est "
      "pas une accumulation paisible, elle détruit ce qu’elle remplace."),
'ch6-open-4': f(niv='comprendre', sp='c6-14', b=2599,
 ans={'modele': "La destruction créatrice désigne le processus par lequel le "
      "tissu productif se renouvelle au gré des innovations : chaque "
      "innovation rend obsolète la technologie antérieure, les nouvelles "
      "entreprises remplacent les anciennes. Aghion et Howitt en font le "
      "moteur de la croissance et montrent que son intensité dépend de deux "
      "déterminants : l’intensité de la R&D, qui augmente la probabilité "
      "d’innover, et le régime de concurrence, qui pousse les firmes à se "
      "dépasser — même si les leaders cherchent à l’entraver pour protéger "
      "leurs rentes.",
      'cles': [{'f': ['obsolete', 'remplace', 'renouvelle', 'perime'],
                'l': 'l’innovation rend obsolète la technologie antérieure'},
               {'f': ['r&d', 'recherche', 'innovation'],
                'l': 'l’intensité de la R&D en augmente la probabilité'},
               {'f': ['concurrence', 'rente', 'barriere', 'entree'],
                'l': 'le régime de concurrence en conditionne la vigueur'},
               {'f': ['chomage', 'reconversion', 'amortisseur', 'cout'],
                'l': 'elle a des coûts sociaux que l’État doit amortir'}]},
 exp="Le cours insiste sur les cinq rôles de l’État qui en découlent : "
     "investisseur dans l’innovation, protecteur des droits de propriété, "
     "garant de la concurrence, amortisseur des effets négatifs, et "
     "orienteur de l’innovation — par exemple vers les technologies vertes."),
'ch6-vf-5': f(niv='comprendre', sp='c6-14', b=2599,
 exp="La destruction créatrice est le moteur de la croissance : elle "
     "renouvelle le tissu productif en remplaçant les technologies obsolètes "
     "par de plus efficaces. Mais le cours ne la présente pas comme indolore : "
     "elle produit du chômage, des reconversions et des chocs locaux, ce qui "
     "justifie que l’État en amortisse les effets."),
'ch6-vf-11': f(niv='connaitre', sp='c6-14', b=2515,
 exp="Le capital humain est bien l’un des trois moteurs identifiés par les "
     "modèles de croissance endogène : capital humain chez Lucas, R&D et "
     "connaissances chez Romer, capital public productif chez Barro."),
'ch6-aut195-1': f(niv='comprendre', sp='c6-14', b=2600,
 exp="Dans le modèle d’Aghion et Howitt, la croissance procède d’innovations "
     "successives qui rendent obsolètes les technologies antérieures. Deux "
     "déterminants la commandent : l’intensité de la R&D, qui augmente la "
     "probabilité d’innover — toutes les dépenses de R&D ne débouchant pas sur "
     "une innovation —, et le régime de concurrence, qui pousse les firmes à "
     "se dépasser mais que les leaders cherchent à restreindre.",
 why=["Épargne et démographie sont les variables de Harrod-Domar et de Solow.",
      "Capital humain et institutions sont les moteurs retenus par Lucas et "
      "par North ou Acemoglu.",
      "Monnaie et crédit n’interviennent pas dans ce modèle de croissance."]),
'ch6-aut195-2': f(niv='raisonner', sp='c6-14', b=2628,
 exp="La politique industrielle optimale dépend de la distance à la frontière "
     "technologique, c’est-à-dire au niveau le plus avancé de technologie à "
     "un moment donné. Loin de la frontière, l’enjeu est le rattrapage : "
     "aider à adopter et améliorer les innovations existantes, mener une "
     "politique de R&D d’imitation. À la frontière, l’innovation de pointe "
     "exige de libéraliser le financement des projets risqués, de miser sur "
     "l’enseignement supérieur et de protéger la propriété intellectuelle.",
 why=["Le niveau des taux d’intérêt n’est pas le critère de différenciation "
      "retenu.",
      "La taille de la population active ne joue aucun rôle dans ce "
      "raisonnement.",
      "Le taux d’ouverture commerciale n’est pas le critère : c’est bien la "
      "position technologique relative."],
 diss="C’est l’argument le plus utile pour nuancer un sujet sur la politique "
      "industrielle : la bonne politique n’est pas la même selon le niveau "
      "technologique du pays."),

# ------------------------------------ c6-15 institutions, développement durable
'ch6-open-8': f(niv='comprendre', sp='c6-15', b=2752,
 ans={'modele': "Pour North, les institutions sont les règles formelles et "
      "informelles qui structurent les interactions humaines : lois, justice, "
      "droits de propriété, normes sociales, constitutions, organisations "
      "publiques. Leur fonction économique est de réduire l’incertitude. Une "
      "économie croît lorsque les investisseurs acceptent de prendre des "
      "risques, que les contrats sont respectés et que la propriété est "
      "protégée ; sans sécurité juridique, personne n’investit, personne "
      "n’innove, le capital fuit. La croissance dépend donc de la crédibilité "
      "des règles.",
      'cles': [{'f': ['regle', 'formelle', 'informelle', 'institution'],
                'l': 'les règles formelles et informelles du jeu économique'},
               {'f': ['incertitude', 'cout de transaction', 'confiance'],
                'l': 'elles réduisent l’incertitude'},
               {'f': ['propriete', 'contrat', 'justice', 'juridique'],
                'l': 'droits de propriété et respect des contrats'},
               {'f': ['investi', 'innov', 'risque'],
                'l': 'd’où investissement et innovation'}]},
 exp="Le cours illustre par l’Angleterre : après la Glorieuse Révolution de "
     "1688, la limitation du pouvoir royal et le renforcement du Parlement "
     "instaurent un État de droit, les droits de propriété sont protégés, les "
     "brevets se développent, le crédit s’étend. La part britannique dans la "
     "production industrielle mondiale passe de 2 % en 1750 à 23 % en 1880.",
 diss="L’explication institutionnelle concurrence les explications "
      "géographiques ou énergétiques de la Révolution industrielle : ce n’est "
      "pas d’abord le charbon, ce sont les règles."),
'ch6-qcm-3': f(niv='comprendre', sp='c6-15', b=2864,
 exp="La croissance est l’augmentation quantitative du PIB, une mesure "
     "comptable ; le développement est une amélioration multidimensionnelle "
     "des conditions de vie : éducation, santé, réduction de la pauvreté et "
     "des inégalités, accès aux services essentiels. On peut donc avoir de la "
     "croissance sans amélioration globale du bien-être.",
 why=["L’inversion est exactement fausse : c’est la croissance qui est "
      "quantitative.",
      "La distinction est au contraire l’un des points les plus insistants du "
      "chapitre.",
      "Les deux notions s’appliquent à tous les pays : il ne s’agit pas d’une "
      "répartition géographique."]),
'ch6-qcm-16': f(niv='connaitre', sp='c6-15', b=2864,
 exp="La définition est celle du rapport Brundtland (1987) : un développement "
     "qui répond aux besoins du présent sans compromettre la capacité des "
     "générations futures à répondre aux leurs. Elle fait apparaître la notion "
     "de responsabilité intergénérationnelle. Le cours la situe après le "
     "rapport du Club de Rome, « Limits to Growth » (1972).",
 why=["Une croissance fondée sur les fossiles est l’inverse de ce que la "
      "notion désigne.",
      "La durabilité ne se mesure pas à la régularité du taux de croissance.",
      "Le mode de financement de la croissance n’entre pas dans la "
      "définition."]),
'ch6-vf-1': f(niv='connaitre', sp='c6-15', b=2864,
 exp="Les deux notions sont distinctes : la croissance est l’augmentation "
     "quantitative du PIB, le développement une amélioration qualitative "
     "portant sur la santé, l’éducation, la pauvreté et les inégalités. Le "
     "cours ajoute une troisième exigence contemporaine : la soutenabilité "
     "environnementale."),
'ch6-vf-16': f(niv='connaitre', sp='c6-15', b=2864,
 exp="C’est la définition centrale du rapport Brundtland de 1987, qui "
     "introduit la responsabilité intergénérationnelle dans l’analyse "
     "économique."),
'ch6-open-12': f(niv='comprendre', sp='c6-15', b=2864,
 ans={'modele': "Le PIB mesure la valeur de la production réalisée sur un "
      "territoire : c’est une grandeur quantitative, qui renseigne sur "
      "l’augmentation des richesses produites. Ses limites sont que le PIB ne "
      "mesure ni les inégalités, ni la qualité de vie, ni la santé, ni "
      "l’environnement, ni le bien-être. On peut donc avoir de la croissance "
      "sans amélioration globale des conditions de vie, d’où le recours à "
      "d’autres indicateurs comme l’IDH, qui combine revenu, santé et "
      "éducation.",
      'cles': [{'f': ['production', 'territoire', 'valeur ajoutee', 'richesse'],
                'l': 'la valeur de la production sur un territoire'},
               {'f': ['inegalite', 'repartition'],
                'l': 'il ignore la répartition'},
               {'f': ['environnement', 'ecologique', 'pollution'],
                'l': 'il ignore les atteintes à l’environnement'},
               {'f': ['bien etre', 'sante', 'qualite de vie', 'idh'],
                'l': 'il ne dit rien du bien-être : d’où l’IDH'}]},
 exp="Le cours met en garde contre une réduction fréquente : le "
     "développement durable n’est pas seulement environnemental, il repose "
     "sur trois piliers — économique, social et environnemental."),
'ch6-qcm-25': f(niv='connaitre', sp='c6-01', b=99,
 exp="Le cours cite comme pays en rattrapage le Japon après 1945, les pays "
     "d’Asie de l’Est, puis la Chine à la fin du XXᵉ siècle. Ces trajectoires "
     "montrent que le rattrapage est possible, sans pour autant être "
     "automatique.",
 why=["Afrique du Sud et Mexique ne figurent pas parmi les exemples retenus.",
      "France et Allemagne font partie des premiers pays industrialisés, non "
      "des pays en rattrapage.",
      "États-Unis et Royaume-Uni sont les pionniers de la croissance "
      "moderne."]),

# ------------------------------------- c6-16 / c6-17 soutenabilité, Kuznets env
'ch6-qcm-17': f(niv='connaitre', sp='c6-16', b=3028,
 exp="La courbe environnementale de Kuznets postule une relation en U inversé "
     "entre dégradation de l’environnement et PIB par habitant : la pollution "
     "croît d’abord avec le développement, puis diminue au-delà d’un certain "
     "seuil de richesse, grâce à la technologie et à la régulation.",
 why=["La relation entre inégalités et revenu est la courbe de Kuznets "
      "d’origine, celle de 1955 : la transposition à l’environnement est "
      "postérieure.",
      "La relation entre croissance et chômage relève d’une autre analyse.",
      "Le lien entre R&D et croissance est l’objet des modèles endogènes."],
 diss="Attention à la portée : le cours en fait un outil de réflexion, "
      "explicitement pas une loi générale."),
'ch6-vf-20': f(niv='comprendre', sp='c6-16', b=3029,
 exp="La courbe prédit l’inverse : une relation en U inversé, où la pollution "
     "augmente d’abord puis diminue au-delà d’un certain niveau de revenu par "
     "habitant. C’est précisément cet optimisme que le cours discute, en "
     "montrant que le profil ne se vérifie pas pour le CO₂ ni pour les "
     "pollutions globales."),
'ch6-aut195-5': f(niv='connaitre', sp='c6-10', b=1825,
 exp="Le coefficient de Palma rapporte la part du revenu détenue par les "
     "10 % les plus riches à celle des 50 % les plus pauvres. Proposé au "
     "début des années 2010, il est plus sensible que le rapport interdécile "
     "aux transformations du sommet de la distribution : c’est un indicateur "
     "de polarisation, qui oppose une élite restreinte à une large base de "
     "la population.",
 why=["Comparer le 9ᵉ et le 1ᵉʳ décile est la définition du rapport "
      "interdécile D9/D1, que le Palma vient précisément compléter.",
      "La comparaison du revenu moyen et du revenu médian mesure "
      "l’asymétrie de la distribution, mais ce n’est pas le Palma.",
      "Le partage entre salaires et profits est le partage de la valeur "
      "ajoutée, une autre question."],
 diss="Son intérêt est de rester sensible quand le D9/D1 ne bouge plus : "
      "depuis 1980, la part des 10 % les plus riches augmente et celle des "
      "50 % les plus pauvres stagne ou diminue."),
'ch6-aut195-6': f(niv='connaitre', sp='c6-16', b=3039,
 exp="La transposition de la courbe de Kuznets à l’environnement est associée "
     "à Grossman et Krueger, dans le Quarterly Journal of Economics en 1995. "
     "Le profil en U inversé se vérifie pour certaines pollutions locales — "
     "dioxyde de soufre, pollution de l’air localisée — mais non pour le CO₂, "
     "les déchets ou la biodiversité ; et il peut masquer une externalisation "
     "géographique des nuisances.",
 why=["Nordhaus et Stern travaillent sur l’économie du climat, mais ce n’est "
      "pas à eux que le cours attribue cette transposition.",
      "Meadows signe le rapport du Club de Rome et Brundtland le rapport de "
      "1987 : ni l’un ni l’autre ne formalise cette courbe.",
      "Hardin et Ostrom analysent les communs, au chapitre précédent."]),
}


# =============================================================== questions neuves
NEW = [

# -------------------------------------------------- c6-01 définir et mesurer
f(id='q6-n01', sp='c6-01', niv='appliquer', type='qcm', b=129,
  q="Le PIB d’un pays progresse de 3 % et sa population de 2,5 %. Que peut-on "
    "en conclure sur le niveau de vie ?",
  opts=["Il progresse nettement, de 3 %",
        "Il progresse faiblement, d’environ 0,5 %",
        "Il recule, puisque la population augmente",
        "On ne peut rien en conclure sans connaître l’inflation"],
  ans=1,
  why=["3 % est la croissance de la richesse totale, pas du revenu par "
       "habitant.",
       "Le PIB par habitant augmente bien, de 0,5 point : il recule seulement "
       "si la population croît plus vite que le PIB.",
       "L’énoncé porte sur le PIB, donc déjà en volume ; l’inflation est "
       "neutralisée."],
  exp="La relation du cours s’écrit : croissance du PIB = croissance de la "
      "population + croissance du PIB par habitant. Ici 3 − 2,5 = 0,5 %. Le "
      "pays s’enrichit globalement, mais la richesse supplémentaire est "
      "répartie entre presque autant d’habitants de plus.",
  diss="Ce calcul suffit à désamorcer l’argument du « miracle de croissance » "
       "de certains pays à forte démographie."),

f(id='q6-n02', sp='c6-01', niv='raisonner', type='ordre', b=152,
  q="Remettez dans l’ordre l’enchaînement par lequel le cours relie "
    "productivité, niveau de vie et cumulativité.",
  ans=["La croissance économique repose sur deux moteurs : la quantité de "
       "travail et la productivité",
       "Seule la croissance du PIB par habitant améliore durablement le "
       "niveau de vie",
       "Or cette croissance dépend principalement des gains de productivité",
       "Ces gains, même modérés, s’appliquent chaque année au niveau déjà "
       "atteint",
       "Sur longue période, les effets cumulés transforment profondément "
       "l’économie"],
  exp="L’enchaînement montre pourquoi la productivité est le cœur du "
      "chapitre : elle est le seul moteur qui améliore durablement le niveau "
      "de vie, et son effet est amplifié par la cumulativité. Une différence "
      "de quelques dixièmes de point devient, sur une génération, un écart de "
      "richesse considérable.",
  diss="Enchaînement très utile pour construire une première partie : il "
       "relie mesure, moteur et dynamique en cinq étapes."),

# ------------------------------------------- c6-02 Rostow et Gerschenkron
f(id='q6-n03', sp='c6-02', niv='connaitre', type='ordre', b=201,
  q="Remettez dans l’ordre les cinq étapes de la croissance selon Rostow.",
  ans=["La société traditionnelle",
       "Les conditions préalables au décollage",
       "Le décollage (take-off)",
       "La marche vers la maturité",
       "L’ère de la consommation de masse"],
  exp="Rostow considère que tous les pays sont appelés à traverser ces cinq "
      "étapes, les dates et la durée pouvant seules varier. La société "
      "traditionnelle est agricole et stable, les conditions préalables "
      "peuvent durer un siècle, le décollage est l’étape centrale, la "
      "maturité diffuse le progrès technique à toute l’économie, et la "
      "consommation de masse constitue l’horizon du modèle.",
  diss="Connaître l’ordre exact permet de situer un pays dans le modèle, et "
       "donc de montrer ce que la linéarité de Rostow a de simplificateur."),

f(id='q6-n04', sp='c6-02', niv='connaitre', type='qcm', b=219,
  q="Quels éléments caractérisent le décollage (take-off) chez Rostow ?",
  opts=["Une baisse du taux d’investissement et une spécialisation agricole",
        "Une accélération du progrès technique, un taux d’investissement "
        "d’environ 10 % du PIB et des secteurs moteurs qui entraînent "
        "l’économie",
        "Une généralisation de l’État-providence et la tertiarisation",
        "L’ouverture complète aux capitaux étrangers"],
  ans=1,
  why=["Le décollage fait au contraire sortir l’économie de la "
       "prédominance agricole.",
       "État-providence et tertiarisation caractérisent la cinquième étape, "
       "celle de la consommation de masse.",
       "L’ouverture commerciale peut déclencher le décollage, mais ce n’est "
       "pas sa définition."],
  exp="Le take-off est l’étape décisive : le progrès technique s’accélère, "
      "l’investissement atteint environ 10 % du PIB, des secteurs moteurs — "
      "le textile en Grande-Bretagne — entraînent le reste de l’économie, et "
      "un appareil politique soutient l’expansion des secteurs modernes. "
      "L’économie devient industrielle et la croissance auto-entretenue.",
  diss="Insister sur le caractère auto-entretenu permet de relier Rostow à "
       "l’idée de dynamique cumulative, point commun avec Gerschenkron."),

f(id='q6-n05', sp='c6-02', niv='comprendre', type='qcmm', b=255,
  q="Quelles critiques le cours adresse-t-il au modèle de Rostow ? "
    "(plusieurs réponses)",
  opts=["Son analyse est descriptive et linéaire, sans différencier les "
        "formes de développement",
        "Il n’intègre pas les facteurs démographiques",
        "Il suppose l’absence de blocage du développement",
        "Il risque l’ethnocentrisme, le modèle étant calqué sur l’expérience "
        "occidentale",
        "Il nie l’importance de l’industrialisation"],
  ans=[0, 1, 2, 3],
  why=["Exacte : c’est la première critique mentionnée.",
       "Exacte : l’omission des facteurs démographiques est explicitement "
       "relevée.",
       "Exacte : cette hypothèse est contestée par les économistes "
       "tiers-mondistes.",
       "Exacte : le modèle est largement construit sur le cas britannique.",
       "Rostow place au contraire l’industrialisation au cœur de la "
       "croissance : c’est même son point commun avec Gerschenkron."],
  exp="Le cours conclut que Rostow propose « un modèle puissant mais "
      "simplificateur » : son optimisme — tous les pays finiront par "
      "atteindre la consommation de masse — reflète l’état d’esprit des "
      "années 1950-1960 plus qu’une loi universelle."),

f(id='q6-n06', sp='c6-02', niv='comprendre', type='qcm', b=283,
  q="Comment Gerschenkron répond-il à la question posée par Rostow — tous les "
    "pays suivent-ils le même chemin de développement ?",
  opts=["Oui, mais avec des durées différentes selon les pays",
        "Non : les trajectoires dépendent du retard initial et du cadre "
        "institutionnel",
        "Oui, à condition que l’État n’intervienne pas",
        "Non, parce que seuls les pays dotés de charbon peuvent "
        "s’industrialiser"],
  ans=1,
  why=["C’est la position de Rostow, pour qui seules les dates varient.",
       "Gerschenkron accorde au contraire un rôle central à l’État, aux "
       "banques et aux grandes entreprises.",
       "L’explication par les ressources naturelles n’est pas la sienne : il "
       "raisonne en termes de retard et d’institutions."],
  exp="Dans « Economic Backwardness in Historical Perspective » (1962), "
      "Gerschenkron distingue early starters, followers et late comers. Un "
      "pays qui s’industrialise tard ne peut pas reproduire le modèle "
      "britannique : ses contraintes de financement, de main-d’œuvre et de "
      "structure productive diffèrent, donc sa trajectoire aussi. Il parle de "
      "« déviations graduelles ».",
  diss="L’opposition se résume en une phrase : Rostow explique la croissance "
       "par une succession d’étapes, Gerschenkron par une trajectoire "
       "dépendante du retard et du contexte."),

f(id='q6-n07', sp='c6-02', niv='raisonner', type='qcm', b=309,
  q="Pourquoi le retard peut-il devenir un avantage, selon Gerschenkron ?",
  opts=["Parce que les pays tardifs disposent d’une main-d’œuvre moins chère",
        "Parce qu’ils peuvent adopter directement les technologies modernes "
        "déjà existantes, substituer plus vite le capital au travail et "
        "créer de grandes entreprises",
        "Parce qu’ils bénéficient d’une aide internationale plus importante",
        "Parce que leur demande intérieure est plus dynamique"],
  ans=1,
  why=["Le coût du travail n’est pas l’argument retenu par Gerschenkron.",
       "L’aide internationale n’intervient pas dans son analyse.",
       "Rien n’indique que la demande intérieure des pays tardifs soit plus "
       "dynamique."],
  exp="Le pays retardataire peut sauter des étapes en profitant des "
      "innovations déjà disponibles : transferts technologiques, imitation, "
      "adoption directe de procédés avancés. Il accélère ainsi son "
      "industrialisation, souvent de façon plus brutale et plus concentrée que "
      "les pionniers.",
  diss="Idée contre-intuitive très efficace en dissertation : elle permet "
       "d’expliquer la rapidité des rattrapages japonais, coréen ou chinois."),

f(id='q6-n08', sp='c6-02', niv='comprendre', type='qcm', b=316,
  q="Quel rôle Gerschenkron attribue-t-il aux institutions dans "
    "l’industrialisation tardive ?",
  opts=["Elles freinent le rattrapage en multipliant les normes",
        "Elles sont indispensables : banques puissantes pour financer "
        "l’industrie, État coordonnateur, grandes entreprises capables "
        "d’investir massivement",
        "Elles n’ont d’effet que dans les pays pionniers",
        "Elles se limitent à la protection des droits de propriété"],
  ans=1,
  why=["C’est l’inverse : sans institutions adaptées, le rattrapage rapide "
       "est impossible.",
       "L’argument porte précisément sur les pays tardifs.",
       "Les droits de propriété relèvent de l’analyse de North, plus loin "
       "dans le chapitre."],
  exp="Pour rattraper vite, il faut mobiliser des capitaux massifs en peu de "
      "temps : d’où le rôle des grandes banques, cité à propos de "
      "l’Allemagne, celui de l’État qui coordonne et accélère, et celui des "
      "grandes entreprises qui réalisent des économies d’échelle. La "
      "croissance n’est donc pas seulement une histoire d’étapes, mais aussi "
      "d’organisation.",
  diss="Ce point annonce la troisième grande question du chapitre, celle du "
       "rôle de l’État dans la croissance."),

f(id='q6-n09', sp='c6-02', niv='comprendre', type='assoc', b=324,
  q="Associez chaque auteur à la caractéristique de son analyse.",
  ans=[["Rostow", "Un modèle linéaire, des étapes universelles, une vision optimiste"],
       ["Gerschenkron", "Des trajectoires multiples, la possibilité de sauter des étapes"],
       ["Point commun aux deux", "L’industrialisation comme moteur historique de la croissance"],
       ["Autre point commun", "La croissance devient cumulative une fois enclenchée"]],
  exp="Opposer les deux auteurs sans voir leurs points communs serait une "
      "erreur : tous deux partent de la Révolution industrielle anglaise, "
      "tous deux font du passage de l’agriculture à l’industrie le moment "
      "déterminant, et tous deux croient à la possibilité du rattrapage. Leur "
      "désaccord porte sur l’unicité du chemin, non sur le moteur.",
  diss="Cette grille — opposition sur la forme, accord sur le moteur — est le "
       "modèle d’une comparaison d’auteurs réussie."),

# ------------------------------------------- c6-03 stagnation séculaire
f(id='q6-n10', sp='c6-03', niv='comprendre', type='qcm', b=452,
  q="Sur quoi Robert Gordon fait-il reposer la stagnation séculaire dans "
    "« The Rise and Fall of American Growth » (2016) ?",
  opts=["Sur une insuffisance chronique de la demande globale",
        "Sur des faiblesses structurelles de l’offre : baisse de la "
        "productivité, faiblesse de l’investissement, innovations moins "
        "transformatrices",
        "Sur un excès d’épargne mondiale",
        "Sur la montée des inégalités"],
  ans=1,
  why=["L’insuffisance de la demande est l’explication concurrente, défendue "
       "par Summers et Krugman.",
       "L’excès d’épargne appartient aussi à la lecture par la demande.",
       "La montée des inégalités est invoquée par les tenants de "
       "l’explication par la demande, comme facteur d’épargne excessive."],
  exp="Pour Gordon, les innovations numériques améliorent le confort et "
      "modifient les usages, mais génèrent peu de gains de productivité "
      "comparés à l’électricité, au moteur, à l’eau courante ou aux "
      "transports. La croissance potentielle des économies développées serait "
      "donc structurellement plus faible, et ce pour au moins vingt-cinq ans.",
  diss="Opposer Gordon (offre) à Summers et Krugman (demande) est la façon la "
       "plus claire de structurer une partie sur la stagnation séculaire — et "
       "les remèdes diffèrent : R&D et éducation d’un côté, politique "
       "budgétaire de l’autre."),

f(id='q6-n11', sp='c6-03', niv='raisonner', type='qcmm', b=472,
  q="Quels mécanismes les partisans de l’explication par la demande "
    "avancent-ils ? (plusieurs réponses)",
  opts=["Une montée des inégalités, qui accroît la part de revenu épargnée "
        "par les plus riches",
        "Un excès d’épargne mondiale",
        "Une faiblesse persistante de l’investissement privé",
        "Un ralentissement de la croissance démographique",
        "Un épuisement des innovations réellement transformatrices"],
  ans=[0, 1, 2, 3],
  why=["Exacte : les hauts revenus épargnent une part plus élevée de leur "
       "revenu.",
       "Exacte : le cours mentionne l’épargne excédentaire de certains pays.",
       "Exacte : même avec des taux très bas, l’investissement ne repart pas.",
       "Exacte : moins de population active signifie moins de débouchés "
       "anticipés.",
       "C’est l’argument de Gordon, qui relève de l’explication par l’offre."],
  exp="Le paradoxe central est que l’épargne abondante ne finance pas "
      "l’investissement productif : elle alimente les marchés financiers et "
      "parfois des bulles. Contrairement à la vision classique où l’épargne "
      "finance l’investissement, l’excès d’épargne devient ici un frein. D’où "
      "la conclusion : les politiques monétaires seules sont insuffisantes, "
      "des politiques budgétaires actives sont nécessaires."),

f(id='q6-n12', sp='c6-03', niv='connaitre', type='assoc', b=446,
  q="Associez chaque auteur à sa contribution au débat sur la stagnation "
    "séculaire.",
  ans=[["Alvin Hansen", "Formule le concept en 1938 : démographie, investissement, innovation"],
       ["Larry Summers", "Le réactive en 2013 : déséquilibre durable entre épargne et investissement"],
       ["Robert Gordon", "Thèse par l’offre : des innovations moins transformatrices (2016)"],
       ["Daniel Cohen", "Diffuse le débat en France : une révolution industrielle sans croissance (2015)"],
       ["David Ricardo", "Ancêtre lointain : l’état stationnaire du début du XIXᵉ siècle"]],
  exp="Cette généalogie montre que le doute sur la durabilité de la "
      "croissance accompagne l’analyse économique depuis longtemps. Hansen "
      "craignait en 1938 un ralentissement démographique et une baisse des "
      "opportunités d’innovation ; la forte croissance de l’après-guerre "
      "semble le démentir et le concept tombe dans l’oubli, avant que 2008 ne "
      "le réactive.",
  diss="Pouvoir citer cinq auteurs sur une même notion, avec leurs dates, "
       "transforme un développement scolaire en démonstration."),

f(id='q6-n13', sp='c6-03', niv='comprendre', type='qcm', b=434,
  q="Quel paradoxe Daniel Cohen souligne-t-il dans « Le monde est clos et le "
    "désir infini » (2015) ?",
  opts=["Les innovations numériques transforment nos modes de vie sans "
        "générer une forte croissance mesurée du PIB",
        "La croissance augmente alors que le bien-être diminue",
        "Les pays pauvres croissent plus vite que les pays riches",
        "L’inflation reste faible malgré la création monétaire"],
  ans=0,
  why=["Cette opposition entre croissance et bien-être n’est pas la "
       "formulation retenue par le cours.",
       "La convergence des pays pauvres est une autre question, celle du "
       "rattrapage.",
       "La faiblesse de l’inflation est un symptôme de la stagnation "
       "séculaire, non le paradoxe de Cohen."],
  exp="Cohen parle d’une « révolution industrielle sans croissance » : le "
      "progrès technique ne se traduit plus nécessairement par une hausse "
      "soutenue de la productivité et des revenus. Il insiste sur le décalage "
      "entre transformation technologique et performance macroéconomique.",
  diss="Formule très citable, qui résume en quatre mots tout le débat sur la "
       "productivité à l’ère numérique."),

f(id='q6-n14', sp='c6-03', niv='appliquer', type='qcm', b=558,
  q="Une économie dont la croissance potentielle est de 0,8 % enregistre une "
    "croissance effective de 0,3 %. Que peut-on en déduire ?",
  opts=["L’output gap est positif : il y a risque d’inflation",
        "L’output gap est négatif : une partie des capacités productives est "
        "inutilisée",
        "L’économie est à l’équilibre",
        "La croissance potentielle doit être révisée à la hausse"],
  ans=1,
  why=["Un output gap positif suppose une croissance effective supérieure à "
       "la potentielle, ce qui n’est pas le cas ici.",
       "L’équilibre correspond à un output gap nul.",
       "Rien ne justifie de réviser la norme : c’est l’activité qui est "
       "en deçà."],
  exp="L’écart est de −0,5 point : l’économie produit moins que ce qu’elle "
      "pourrait. Les conséquences attendues sont un chômage élevé, du "
      "sous-emploi, une faible pression inflationniste et un ralentissement de "
      "l’investissement. Le cours souligne que c’est la situation prolongée "
      "des économies développées après 2008.",
  diss="Savoir lire un output gap permet de distinguer ce qui relève du cycle "
       "et ce qui relève du potentiel — distinction indispensable pour parler "
       "de stagnation séculaire sans confusion."),

f(id='q6-n15', sp='c6-03', niv='raisonner', type='courte', b=601,
  q="Quels symptômes conduisent le cours à parler de stagnation séculaire "
    "plutôt que de simple crise conjoncturelle ?",
  ans={'modele': "Le cours relève une croissance potentielle affaiblie, une "
       "croissance effective durablement faible, des output gaps négatifs "
       "persistants, un affaiblissement de la productivité malgré le progrès "
       "technique, une faiblesse de l’investissement, une inflation contenue "
       "et un chômage durable. La combinaison de ces signes, et surtout leur "
       "persistance après le retour de la croissance, indique un problème "
       "structurel et non un choc temporaire : les économies développées ne "
       "retrouvent pas les rythmes d’avant-crise.",
       'cles': [{'f': ['potentielle', 'affaibli', 'recul'],
                 'l': 'une croissance potentielle affaiblie'},
                {'f': ['output gap', 'negatif', 'sous activite'],
                 'l': 'des output gaps négatifs persistants'},
                {'f': ['productivite', 'ralentissement'],
                 'l': 'un affaiblissement de la productivité'},
                {'f': ['investissement', 'faible'],
                 'l': 'une faiblesse de l’investissement'},
                {'f': ['durable', 'structurel', 'persist', 'prolonge'],
                 'l': 'et surtout leur persistance : un problème structurel'}]},
  exp="Le critère décisif est la durée : une crise conjoncturelle se "
      "referme, une stagnation séculaire s’installe. C’est pourquoi le cours "
      "souligne que, même lorsque la reprise intervient après 2008, elle "
      "reste plus faible que lors des cycles précédents."),

# ------------------------------------- c6-04 décomposer, comparer euro / US
f(id='q6-n16', sp='c6-04', niv='comprendre', type='qcmm', b=644,
  q="Sur quelles hypothèses repose la fonction de Cobb-Douglas utilisée par "
    "Carré, Dubois et Malinvaud ? (plusieurs réponses)",
  opts=["Les facteurs de production sont substituables",
        "Les rendements d’échelle sont constants",
        "Le paramètre A représente l’efficacité globale de l’économie",
        "Les facteurs de production sont strictement complémentaires",
        "Le progrès technique est endogène"],
  ans=[0, 1, 2],
  why=["Exacte : on peut remplacer du travail par du capital, et "
       "réciproquement.",
       "Exacte : doubler capital et travail double la production.",
       "Exacte : c’est ce terme qui portera le résidu, donc la PGF.",
       "La complémentarité est l’hypothèse de Harrod-Domar, et la critique "
       "adressée à Cobb-Douglas — le cours reconnaît d’ailleurs qu’une "
       "machine sans travailleur ne produit rien.",
       "Le progrès technique reste exogène : c’est justement ce que la PGF "
       "mesure sans l’expliquer."],
  exp="La substituabilité et les rendements constants ne sont pas des "
      "descriptions fidèles de la réalité : ce sont des hypothèses qui "
      "permettent de décomposer proprement la croissance. Le cours le dit "
      "explicitement : dans la réalité, travail et capital sont largement "
      "complémentaires."),

f(id='q6-n17', sp='c6-04', niv='appliquer', type='qcm', b=702,
  q="La croissance française annuelle moyenne est de 5,2 % entre 1951 et "
    "1973, dont 0,5 point imputable au travail et 1,5 point au capital. Que "
    "vaut la part de la PGF ?",
  opts=["2,0 points, soit environ 40 % de la croissance",
        "3,1 points, soit environ 60 % de la croissance",
        "3,7 points, soit environ 70 % de la croissance",
        "5,2 points, soit la totalité de la croissance"],
  ans=1,
  why=["2,0 points correspondraient à la somme des contributions du travail "
       "et du capital, non au résidu.",
       "3,7 points supposerait une contribution du capital plus faible que "
       "celle retenue par les auteurs.",
       "La PGF est un résidu : elle ne peut pas absorber la totalité de la "
       "croissance alors que travail et capital y contribuent."],
  exp="5,2 − 0,5 − 1,5 = 3,1 points, soit 3,1/5,2 ≈ 60 %. Le résultat est "
      "spectaculaire : l’essentiel de la croissance des Trente Glorieuses ne "
      "s’explique ni par davantage de travailleurs, ni par davantage de "
      "machines, mais par une utilisation plus efficace des deux.",
  diss="Ce chiffre est le plus rentable du chapitre : il justifie à lui seul "
       "que l’on place le progrès technique au centre de toute analyse de la "
       "croissance de long terme."),

f(id='q6-n18', sp='c6-04', niv='comprendre', type='qcm', b=581,
  q="Quelle divergence majeure le cours relève-t-il entre la zone euro et les "
    "États-Unis après 2008 ?",
  opts=["La zone euro connaît une croissance potentielle plus élevée",
        "La dette publique progresse d’environ 20 points de PIB en zone euro "
        "contre plus de 40 points aux États-Unis",
        "Les États-Unis ont connu des output gaps positifs",
        "L’inflation a été plus forte en zone euro"],
  ans=1,
  why=["La croissance potentielle recule dans les deux zones ; la zone euro "
       "partait d’un niveau déjà plus modéré.",
       "Les deux zones connaissent des output gaps négatifs persistants.",
       "Le cours ne relève pas d’écart d’inflation : il souligne au contraire "
       "une inflation contenue de part et d’autre."],
  exp="Cette divergence signale une réponse budgétaire américaine beaucoup "
      "plus expansive : les États-Unis ont accepté un endettement bien plus "
      "important pour soutenir l’activité. Le second écart notable concerne "
      "le chômage, historiquement plus faible aux États-Unis, dont le marché "
      "du travail apparaît plus flexible et plus réactif aux chocs.",
  diss="Même diagnostic, intensités différentes : la comparaison montre que "
       "les trajectoires dépendent des choix institutionnels, et pas "
       "seulement du choc subi."),

f(id='q6-n19', sp='c6-04', niv='connaitre', type='vf', b=624,
  q="La décomposition de la croissance pratiquée par Carré, Dubois et "
    "Malinvaud s’inspire de la méthode de Robert Solow.",
  ans=True,
  exp="Le cours est explicite : aux États-Unis, Solow a été l’un des premiers "
      "à chercher à mesurer ce qui explique la croissance ; en France, Carré, "
      "Dubois et Malinvaud reprennent cette méthode dans « La croissance "
      "française » (1972) pour expliquer la forte croissance des Trente "
      "Glorieuses et isoler un résidu d’efficacité globale."),

f(id='q6-n20', sp='c6-04', niv='raisonner', type='courte', b=662,
  q="Pourquoi décomposer la croissance en contributions du travail, du "
    "capital et d’un résidu ?",
  ans={'modele': "La décomposition répond à une question précise : la "
       "croissance vient-elle de ce qu’on utilise plus de travail, plus de "
       "capital, ou de ce qu’on produit plus efficacement ? Grâce à la "
       "fonction de production, on mesure la contribution de chaque facteur "
       "puis on isole ce qui reste inexpliqué, la productivité globale des "
       "facteurs. Cela permet de distinguer croissance extensive et "
       "croissance intensive, et d’en tirer des conclusions de politique "
       "économique : une croissance de résidu est durable, une croissance par "
       "accumulation de facteurs se heurte aux rendements décroissants et aux "
       "limites démographiques.",
       'cles': [{'f': ['travail', 'capital', 'contribution'],
                 'l': 'mesurer la contribution de chaque facteur'},
                {'f': ['residu', 'pgf', 'inexplique', 'efficacite'],
                 'l': 'isoler le résidu, la PGF'},
                {'f': ['extensive', 'intensive'],
                 'l': 'distinguer croissance extensive et intensive'},
                {'f': ['durable', 'limite', 'decroissant', 'politique'],
                 'l': 'en tirer les limites de l’accumulation des facteurs'}]},
  exp="La décomposition a aussi une portée critique : la taille du résidu — "
      "60 % de la croissance française des Trente Glorieuses — mesure "
      "l’étendue de ce que le modèle n’explique pas."),

# ----------------------------------------- c6-05 croissance extensive
f(id='q6-n21', sp='c6-05', niv='connaitre', type='qcm', b=728,
  q="De quelles deux composantes dépend l’évolution de la population, moteur "
    "du facteur travail ?",
  opts=["Le solde naturel et le solde migratoire",
        "Le taux d’activité et le taux de chômage",
        "La durée des études et l’âge de la retraite",
        "La natalité et l’espérance de vie uniquement"],
  ans=0,
  why=["Taux d’activité et chômage décrivent la participation au marché du "
       "travail, pas l’évolution de la population.",
       "Durée des études et âge de la retraite déterminent le délai entre la "
       "naissance et l’entrée dans la population active, non la population "
       "elle-même.",
       "La natalité et l’espérance de vie composent le solde naturel : il "
       "manque le solde migratoire."],
  exp="Le solde naturel est la différence entre naissances et décès, le solde "
      "migratoire entre entrées et sorties du territoire. Le cours en tire un "
      "enseignement direct : les flux migratoires sont un enjeu économique "
      "majeur, parce qu’ils peuvent accroître rapidement le facteur travail, "
      "alors que la natalité n’agit qu’avec un long délai."),

f(id='q6-n22', sp='c6-05', niv='comprendre', type='qcm', b=733,
  q="Pourquoi le cours qualifie-t-il la population active de « variable "
    "institutionnelle autant que démographique » ?",
  opts=["Parce que l’État fixe le nombre d’emplois disponibles",
        "Parce que la durée des études et l’âge de la retraite déterminent le "
        "délai entre la naissance et l’entrée dans la population active",
        "Parce que les statistiques de population active sont établies par "
        "l’INSEE",
        "Parce que les migrations sont contrôlées par la loi"],
  ans=1,
  why=["L’État ne fixe pas le nombre d’emplois : il n’est pas l’employeur "
       "unique.",
       "Le mode de production des statistiques ne change pas la nature de la "
       "variable.",
       "Les migrations relèvent effectivement de la loi, mais ce n’est pas "
       "l’argument développé ici."],
  exp="La démographie n’affecte pas immédiatement la population active : un "
      "allongement des études la retarde, un report de l’âge de la retraite "
      "l’augmente, un abaissement la réduit. Des décisions institutionnelles "
      "modifient donc la quantité de travail disponible, indépendamment de la "
      "démographie.",
  diss="Argument utile pour discuter une réforme des retraites en termes de "
       "croissance potentielle et non seulement d’équilibre financier."),

f(id='q6-n23', sp='c6-05', niv='connaitre', type='vf', b=744,
  q="Dans le cas français, une grande partie de la croissance du facteur "
    "travail au XXᵉ siècle provient de l’entrée des femmes sur le marché du "
    "travail et de leur maintien durable dans l’emploi.",
  ans=True,
  exp="Le cours distingue soigneusement ce mouvement des périodes de guerre, "
      "où les femmes remplaçaient temporairement les hommes sans hausse "
      "durable du taux d’activité. À partir de la fin des années 1960, les "
      "taux d’activité féminins augmentent fortement et se rapprochent "
      "aujourd’hui de ceux des hommes : c’est une transformation "
      "structurelle, qui a directement contribué à la croissance extensive."),

f(id='q6-n24', sp='c6-05', niv='connaitre', type='qcm', b=767,
  q="Pourquoi la FBCF est-elle centrale dans l’analyse de la croissance ?",
  opts=["Parce qu’elle mesure la consommation des ménages",
        "Parce qu’elle accroît le stock de capital, augmente la capacité de "
        "production et prépare la croissance future",
        "Parce qu’elle mesure l’épargne des entreprises",
        "Parce qu’elle correspond aux dépenses publiques d’investissement "
        "uniquement"],
  ans=1,
  why=["La consommation des ménages est un autre agrégat de la demande.",
       "L’épargne des entreprises est une ressource de financement, non "
       "l’investissement lui-même.",
       "La FBCF couvre l’investissement de tous les agents, pas seulement "
       "celui de l’État."],
  exp="La formation brute de capital fixe est le flux par lequel s’accumule "
      "le capital. Son triple effet — hausse du stock de capital, hausse de "
      "la capacité de production, préparation de la croissance future — "
      "explique qu’une hausse durable de l’investissement soit considérée "
      "comme un indicateur avancé de croissance."),

f(id='q6-n25', sp='c6-05', niv='appliquer', type='qcm', b=774,
  q="Dans une économie, le stock de capital augmente de 4 % et le volume de "
    "travail de 1 %. Que peut-on dire de l’intensité capitalistique ?",
  opts=["Elle diminue, puisque le travail augmente",
        "Elle augmente : il y a davantage de machines par travailleur",
        "Elle reste stable, les deux facteurs augmentant",
        "On ne peut rien dire sans connaître la productivité"],
  ans=1,
  why=["L’intensité capitalistique diminuerait si le travail croissait plus "
       "vite que le capital.",
       "Elle ne serait stable que si les deux facteurs progressaient au même "
       "rythme.",
       "La productivité est une conséquence possible de ce mouvement, pas une "
       "donnée nécessaire pour le constater."],
  exp="L’intensité capitalistique est le rapport capital / travail. Comme le "
      "capital augmente plus vite que le travail, ce rapport s’élève : chaque "
      "travailleur dispose de plus d’équipements, donc d’une capacité de "
      "production potentiellement plus élevée. Le cours voit dans ce "
      "mécanisme une grande partie de la croissance extensive des économies "
      "industrialisées.",
  diss="Attention à la nuance : plus de capital par tête élève la production "
       "par tête, mais avec des rendements décroissants — c’est précisément ce "
       "qui conduit Solow à l’état stationnaire."),

f(id='q6-n26', sp='c6-05', niv='connaitre', type='qcm', b=762,
  q="Quel exemple fondateur le cours retient-il pour illustrer le rôle "
    "historique du capital dans la croissance ?",
  opts=["Le métier à tisser mécanique de 1850",
        "La machine à vapeur, brevetée par James Watt en 1769",
        "La chaîne de montage de Ford en 1913",
        "L’ordinateur personnel des années 1980"],
  ans=1,
  why=["Le textile est bien un secteur moteur chez Rostow, mais l’exemple "
       "fondateur cité ici est la machine à vapeur.",
       "La chaîne de montage relève des innovations organisationnelles du "
       "XXᵉ siècle.",
       "L’informatique personnelle intervient dans le débat sur les NTIC, "
       "beaucoup plus loin dans le chapitre."],
  exp="La machine à vapeur, brevetée par Watt en 1769, permet de remplacer la "
      "force animale et hydraulique par une énergie mécanique plus puissante "
      "et plus flexible. C’est un tournant décisif dans la capacité "
      "productive des économies, et le point de départ du lien entre "
      "révolutions technologiques et croissance."),

f(id='q6-n27', sp='c6-05', niv='raisonner', type='qcmm', b=782,
  q="Quelles limites le cours assigne-t-il à la croissance extensive ? "
    "(plusieurs réponses)",
  opts=["Des limites démographiques : vieillissement, faible natalité",
        "Des limites économiques : rendements décroissants",
        "Des contraintes budgétaires",
        "Des limites sociales : emploi, conditions de travail",
        "L’impossibilité d’accumuler du capital dans une économie ouverte"],
  ans=[0, 1, 2, 3],
  why=["Exacte : la démographie plafonne la quantité de travail disponible.",
       "Exacte : chaque unité supplémentaire de facteur rapporte moins.",
       "Exacte : le cours les mentionne parmi les limites.",
       "Exacte : allonger la durée du travail se heurte à la fatigue et aux "
       "conditions de travail.",
       "Rien de tel dans le cours : l’ouverture n’empêche pas "
       "l’accumulation."],
  exp="Ces limites expliquent le basculement du chapitre : puisque la "
      "croissance ne peut pas reposer indéfiniment sur l’accumulation des "
      "facteurs, l’analyse se déplace vers le progrès technique, la PGF et la "
      "distinction extensive / intensive — et prépare le débat sur la "
      "stagnation séculaire."),

# -------------------------------------- c6-06 productivité du travail
f(id='q6-n28', sp='c6-06', niv='comprendre', type='qcm', b=811,
  q="Pourquoi la productivité horaire est-elle une mesure plus pertinente que "
    "la productivité par tête ?",
  opts=["Parce qu’elle intègre la qualité du capital utilisé",
        "Parce que deux pays peuvent employer autant de travailleurs avec des "
        "durées de travail très différentes",
        "Parce qu’elle est plus facile à calculer",
        "Parce qu’elle élimine l’effet de l’inflation"],
  ans=1,
  why=["La qualité du capital n’est captée par aucune des deux mesures : "
       "elle relève de la PGF.",
       "C’est l’inverse : les données sur les heures travaillées ne sont pas "
       "toujours disponibles, ce que le cours signale.",
       "La correction de l’inflation vient du passage au PIB en volume, "
       "indépendamment du dénominateur choisi."],
  exp="Le cours donne l’exemple d’une durée du travail souvent supérieure à "
      "45 heures en Chine contre une durée légale de 35 heures en France : "
      "compter seulement les effectifs ne suffit pas. La productivité horaire "
      "rapporte le PIB au nombre total d’heures travaillées, qui dépend à la "
      "fois des effectifs et de la durée du travail. C’est la mesure la plus "
      "précise pour les comparaisons internationales.",
  diss="Préciser la mesure retenue évite les contresens classiques sur la "
       "« productivité française », élevée à l’heure mais pesée par un faible "
       "volume d’heures travaillées."),

f(id='q6-n29', sp='c6-06', niv='raisonner', type='ordre', b=846,
  q="Remettez dans l’ordre le mécanisme par lequel la réforme de "
    "l’apprentissage a fait baisser la productivité moyenne en France.",
  ans=["La réforme instaure des primes aux entreprises, des exonérations de "
       "cotisations et un élargissement des conditions",
       "Le nombre d’apprentis passe d’environ 400 000 à plus d’un million en "
       "2024",
       "Or un apprenti est comptabilisé dans l’emploi, travaille moins qu’un "
       "salarié classique et est encore en formation",
       "Le nombre de travailleurs augmente rapidement, mais la production pas "
       "dans les mêmes proportions",
       "La productivité moyenne diminue mécaniquement"],
  exp="L’enchaînement est purement arithmétique : la productivité est un "
      "rapport, et c’est le dénominateur qui augmente le plus vite. Le cours "
      "en tire une idée essentielle : une baisse de la productivité peut être "
      "le résultat d’une bonne politique de l’emploi, et non d’une "
      "inefficacité économique.",
  diss="Exemple précieux pour montrer qu’un indicateur peut se dégrader pour "
       "de bonnes raisons — nuance qui distingue une copie fine d’une copie "
       "mécanique."),

f(id='q6-n30', sp='c6-06', niv='appliquer', type='qcm', b=857,
  q="Une entreprise perçoit une prime à l’embauche d’un apprenti qu’elle "
    "aurait recruté de toute façon. Comment nomme-t-on cette situation ?",
  opts=["Un effet d’aubaine",
        "Un effet de levier",
        "Un aléa moral",
        "Un effet d’éviction"],
  ans=0,
  why=["L’effet de levier désigne l’amplification d’un rendement par "
       "l’endettement.",
       "L’aléa moral est un problème d’information, lié à un comportement "
       "caché après la signature d’un contrat.",
       "L’effet d’éviction désigne le recul de l’investissement privé causé "
       "par l’emprunt public."],
  exp="On parle d’effet d’aubaine lorsqu’un agent bénéficie d’une aide "
      "publique alors qu’il aurait adopté le même comportement en son "
      "absence : l’aide ne change pas la décision, elle réduit seulement le "
      "coût. La subvention ne crée alors pas d’emploi supplémentaire, elle "
      "constitue un transfert financier, pour un coût budgétaire élevé sans "
      "effet additionnel équivalent.",
  diss="Le cours précise la portée du débat : il porte sur l’efficacité du "
       "ciblage, non sur la légitimité d’aider."),

f(id='q6-n31', sp='c6-06', niv='comprendre', type='qcm', b=877,
  q="Comment la crise du Covid a-t-elle pesé sur la productivité mesurée en "
    "France ?",
  opts=["Le chômage a explosé, ce qui a mécaniquement élevé la productivité",
        "Le chômage partiel a maintenu l’emploi tandis que la production "
        "reculait, ce qui a fait baisser la productivité",
        "La productivité est restée stable, l’emploi et la production "
        "baissant au même rythme",
        "Les entreprises les moins productives ont disparu, ce qui a élevé la "
        "productivité moyenne"],
  ans=1,
  why=["Contrairement aux États-Unis, le chômage n’a pas explosé en France : "
       "c’est précisément le point du cours.",
       "La production a reculé bien plus vite que l’emploi : les deux n’ont "
       "pas évolué au même rythme.",
       "C’est l’inverse : le dispositif a permis la survie d’entreprises à "
       "faible productivité, dites entreprises zombies."],
  exp="Le mécanisme est le même que pour l’apprentissage : le dénominateur "
      "— la main-d’œuvre — ne diminue pas, alors que le numérateur — la "
      "production — recule. La productivité baisse mécaniquement. Le cours y "
      "voit la contrepartie statistique d’un choix social : préserver "
      "l’emploi pendant la crise.",
  diss="Mettre l’apprentissage et le chômage partiel en série montre que le "
       "« décrochage de productivité » français s’explique en partie par des "
       "politiques de l’emploi, et non seulement par un retard technologique."),

f(id='q6-n32', sp='c6-06', niv='raisonner', type='assoc', b=893,
  q="Associez chaque explication du ralentissement de la productivité à son "
    "contenu.",
  ans=[["Robert Gordon", "Les innovations numériques sont moins transformatrices que celles du passé"],
       ["L’explication par le délai", "Il faut du temps pour adapter l’organisation et former les salariés"],
       ["L’argument de mesure (Aghion)", "Une partie des innovations est gratuite et la qualité est mal mesurée"],
       ["L’explication par l’emploi", "La hausse du volume de travail n’est pas suivie d’une hausse équivalente du PIB"]],
  exp="Les quatre lectures n’ont pas les mêmes implications. Si Gordon a "
      "raison, le ralentissement est durable et structurel. Si c’est une "
      "question de délai, la productivité accélérera plus tard. Si c’est un "
      "problème de mesure, la productivité réelle est sous-estimée. Si c’est "
      "l’emploi, la baisse est l’envers d’un succès social.",
  diss="Présenter ces quatre lectures côte à côte est la meilleure façon de "
       "traiter un sujet sur le ralentissement de la productivité sans "
       "trancher trop vite."),

f(id='q6-n33', sp='c6-06', niv='comprendre', type='qcmm', b=1038,
  q="Selon le cours, comment les gains de productivité peuvent-ils être "
    "répartis ? (plusieurs réponses)",
  opts=["En hausse des salaires, donc de pouvoir d’achat et de consommation",
        "En hausse des profits, donc d’autofinancement et d’investissement",
        "En baisse des prix, donc en compétitivité-prix et parts de marché",
        "En hausse des recettes fiscales de l’État",
        "En baisse mécanique du taux d’épargne des ménages"],
  ans=[0, 1, 2, 3],
  why=["Exacte : c’est le premier canal, avec une limite — si la "
       "consommation porte sur des produits importés, la relance ne profite "
       "pas à l’économie nationale.",
       "Exacte : favorable à la croissance de long terme par l’innovation "
       "future.",
       "Exacte : la baisse des prix est rentable si la hausse des quantités "
       "compense la baisse de la marge unitaire.",
       "Exacte : salaires et profits en hausse élargissent l’assiette "
       "fiscale, ce qui finance redistribution et services publics.",
       "Le cours n’établit aucun lien de ce genre."],
  exp="La question du partage des gains de productivité est au moins aussi "
      "importante que celle de leur existence : selon le canal retenu, ce "
      "sont les salariés, les actionnaires, les consommateurs ou l’État qui "
      "en bénéficient."),

f(id='q6-n34', sp='c6-06', niv='raisonner', type='qcm', b=1115,
  q="Comment le cours interprète-t-il la baisse de la durée du travail en "
    "France — de 3 000 à 1 500 heures annuelles entre 1870 et aujourd’hui ?",
  opts=["Comme un échec économique qui explique le ralentissement de la "
        "croissance",
        "Comme un produit des gains de productivité, et non comme leur cause "
        "négative",
        "Comme une conséquence exclusive des lois sociales",
        "Comme une illusion statistique"],
  ans=1,
  why=["Le cours soutient exactement l’inverse : la réduction du temps de "
       "travail est « un produit de la croissance, pas son échec ».",
       "Les lois sociales y contribuent — congés payés, 35 heures — mais la "
       "cause de fond est la hausse de la productivité, qui permet de "
       "produire autant en moins de temps.",
       "La baisse est bien réelle et documentée."],
  exp="Le raisonnement est clair : si chaque heure devient beaucoup plus "
      "productive, on peut produire autant en travaillant moins. Le cours "
      "chiffre le mouvement : à la fin du XXᵉ siècle, chaque actif est "
      "environ quinze fois plus productif qu’en 1880 et chaque heure de "
      "travail vingt-huit fois.",
  diss="Renverser l’argument — moins d’heures parce que plus de productivité, "
       "et non l’inverse — est l’un des retournements les plus utiles du "
       "chapitre."),

f(id='q6-n35', sp='c6-06', niv='comprendre', type='qcm', b=991,
  q="Pourquoi parle-t-on de productivité « apparente » du travail ?",
  opts=["Parce qu’elle est mesurée avec un retard statistique",
        "Parce qu’elle attribue au seul travail une performance qui doit "
        "aussi au capital, à la formation et à l’organisation",
        "Parce qu’elle n’est qu’une estimation, jamais un calcul exact",
        "Parce qu’elle varie fortement d’un trimestre à l’autre"],
  ans=1,
  why=["Le délai de publication n’est pas la raison de ce qualificatif.",
       "Le calcul est au contraire parfaitement défini : PIB rapporté au "
       "travail.",
       "La volatilité conjoncturelle existe, mais ce n’est pas le sens du "
       "mot « apparente »."],
  exp="Si un travailleur produit plus, ce n’est pas seulement parce qu’il "
      "travaille mieux : il est mieux équipé, mieux formé, aidé par des "
      "machines et inséré dans une meilleure organisation. Le cours prend "
      "l’exemple du caissier, plus productif grâce au scan automatique et aux "
      "logiciels. La productivité du travail intègre donc l’effet du capital "
      "et de la technologie : d’où l’adjectif.",
  diss="Cette précision justifie le passage à la PGF, qui tente de distinguer "
       "ce qui revient à chaque facteur."),

# ----------------------------- c6-07 compétitivité, Draghi, prix réels
f(id='q6-n36', sp='c6-07', niv='connaitre', type='qcm', b=1136,
  q="Quelle distinction le cours établit-il au sein de la compétitivité ?",
  opts=["Compétitivité interne et compétitivité externe",
        "Compétitivité-prix, qui consiste à produire à moindre coût, et "
        "compétitivité hors-prix, fondée sur la qualité, l’innovation et la "
        "technologie",
        "Compétitivité nominale et compétitivité réelle",
        "Compétitivité sectorielle et compétitivité globale"],
  ans=1,
  why=["Cette distinction n’est pas celle du cours.",
       "Nominale et réelle qualifient des grandeurs monétaires, non la "
       "compétitivité.",
       "La distinction sectoriel / global ne figure pas ici."],
  exp="La compétitivité est la capacité d’un pays à gagner des parts de "
      "marché, à exporter et à maintenir son niveau de vie. Une hausse de "
      "productivité agit sur les deux formes : elle réduit les coûts "
      "unitaires, donc améliore la compétitivité-prix, ou permet d’améliorer "
      "la qualité à prix constant, donc la compétitivité hors-prix.",
  diss="Le cours applique ensuite cette grille : la France a davantage joué "
       "la compétitivité-prix, l’Allemagne la compétitivité hors-prix, ce qui "
       "explique en partie des désindustrialisations d’ampleur différente."),

f(id='q6-n37', sp='c6-07', niv='comprendre', type='qcmm', b=1145,
  q="Quels problèmes le rapport Draghi (2024) identifie-t-il pour expliquer "
    "la faiblesse de la productivité européenne ? (plusieurs réponses)",
  opts=["Une demande insuffisante, liée à la fragmentation des marchés",
        "Des structures trop rigides : complexité réglementaire, "
        "superposition des normes, bureaucratie",
        "Un déficit d’investissement : retard en R&D, fragmentation des "
        "marchés de capitaux",
        "Un excès de concurrence intra-européenne",
        "Une démographie trop dynamique"],
  ans=[0, 1, 2],
  why=["Exacte : sans perspective de marché élargi, les entreprises "
       "investissent et innovent moins.",
       "Exacte : l’environnement institutionnel freine l’initiative et la "
       "prise de risque.",
       "Exacte : or l’innovation dépend de l’investissement.",
       "Le diagnostic est inverse : c’est l’intégration des marchés qui "
       "manque, non la concurrence qui serait excessive.",
       "La démographie européenne n’est pas présentée comme trop dynamique."],
  exp="Les solutions proposées répondent terme à terme au diagnostic : "
      "construire un véritable marché européen des capitaux, simplifier la "
      "réglementation, et lancer un plan d’investissement d’environ "
      "800 milliards d’euros par an ciblé sur l’innovation, la transition "
      "énergétique et les technologies. Le cours relève le caractère mixte de "
      "cette stratégie : une partie libérale, une partie keynésienne."),

f(id='q6-n38', sp='c6-07', niv='raisonner', type='qcm', b=1190,
  q="Quel héritage intellectuel le cours reconnaît-il au raisonnement de "
    "Draghi sur la taille du marché ?",
  opts=["Celui de Ricardo et des avantages comparatifs",
        "Celui d’Adam Smith : plus le marché est vaste, plus la "
        "spécialisation est poussée, plus la productivité augmente",
        "Celui de Keynes et du multiplicateur",
        "Celui de Schumpeter et des grappes d’innovations"],
  ans=1,
  why=["Les avantages comparatifs portent sur la spécialisation entre pays, "
       "non sur la taille du marché et la division du travail.",
       "Le multiplicateur est bien présent dans la dimension keynésienne du "
       "plan d’investissement, mais ce n’est pas l’héritage invoqué ici.",
       "Schumpeter n’est pas mobilisé sur ce point."],
  exp="Smith liait la productivité à la division du travail, elle-même "
      "conditionnée par l’étendue du marché. Draghi transpose : passer d’un "
      "marché national à un marché européen intégré élargit les débouchés, "
      "encourage la spécialisation et permet des économies d’échelle. "
      "L’intégration européenne devient ainsi un levier direct de "
      "productivité.",
  diss="Faire remonter un rapport de 2024 à Smith montre la continuité des "
       "mécanismes économiques : c’est exactement ce qu’attend un correcteur."),

f(id='q6-n39', sp='c6-07', niv='appliquer', type='qcm', b=1255,
  q="Comment le cours définit-il le prix réel relatif d’un bien ?",
  opts=["Le prix du bien divisé par l’indice général des prix",
        "Le prix du bien divisé par le salaire horaire, ce qui mesure le "
        "temps de travail nécessaire pour l’acheter",
        "Le prix du bien exprimé dans la monnaie d’un autre pays",
        "Le prix du bien corrigé de la qualité"],
  ans=1,
  why=["Diviser par l’indice général des prix donne un prix réel, mais le "
       "cours retient précisément le rapport au salaire horaire.",
       "La conversion monétaire est une question de taux de change.",
       "La correction par la qualité est un problème de mesure distinct, que "
       "le cours évoque ailleurs."],
  exp="Mesurer un prix en heures de travail rend la comparaison indépendante "
      "de l’inflation et centrée sur le pouvoir d’achat réel. Piketty "
      "l’illustre par la bicyclette : environ six mois de salaire au début de "
      "sa diffusion, un mois après la production de masse, quelques jours ou "
      "une semaine aujourd’hui malgré une sophistication bien supérieure.",
  diss="L’exemple permet de répondre à une objection courante : « tout "
       "augmente ». En prix nominal, oui ; en temps de travail, beaucoup de "
       "biens sont devenus très accessibles."),

f(id='q6-n40', sp='c6-07', niv='comprendre', type='vf', b=1273,
  q="Selon le cours, les ménages raisonnent le plus souvent en prix nominaux, "
    "ce qui leur donne le sentiment que « tout devient plus cher » alors que "
    "certains biens sont plus accessibles qu’avant.",
  ans=True,
  exp="C’est l’erreur courante que le cours signale : comparer des prix en "
      "monnaie courante sur longue période n’a pas de sens, puisque les prix "
      "et les revenus ont tous les deux évolué. Il faut déflater ou raisonner "
      "en prix relatifs. Le progrès technique fait baisser le prix réel des "
      "biens, même quand leur prix nominal augmente."),

f(id='q6-n41', sp='c6-07', niv='raisonner', type='courte', b=1237,
  q="Expliquez le double effet du progrès technique sur les prix.",
  ans={'modele': "À court terme, l’innovation peut faire monter les prix : "
       "l’entreprise a engagé des coûts de R&D, son brevet la place en "
       "situation de monopole temporaire, et elle répercute ce coût sur le "
       "prix de vente — les premiers téléviseurs, téléphones ou automobiles "
       "étaient chers. À moyen et long terme, la production augmente, les "
       "unités de production s’élargissent, les économies d’échelle font "
       "baisser le coût unitaire : les prix diminuent et les gains se "
       "diffusent à l’ensemble de la collectivité. Le progrès technique "
       "bénéficie donc in fine à la société, même s’il est d’abord capté par "
       "l’innovateur.",
       'cles': [{'f': ['brevet', 'monopole', 'r&d', 'cout'],
                 'l': 'à court terme, brevet et coûts de R&D élèvent le prix'},
                {'f': ['economie d echelle', 'taille', 'diffusion', 'masse'],
                 'l': 'à moyen terme, les économies d’échelle font baisser le coût unitaire'},
                {'f': ['collectivite', 'accessib', 'pouvoir d achat', 'niveau de vie'],
                 'l': 'les gains se diffusent ensuite à la collectivité'}]},
  exp="Le cours insiste sur l’ordre des effets : la baisse des prix "
      "intervient après la diffusion massive, et non au moment de "
      "l’invention. Atteindre une taille critique de production est "
      "indispensable pour rentabiliser l’innovation."),

# ------------------------------- c6-08 trois secteurs, déversement, marchés
f(id='q6-n42', sp='c6-08', niv='connaitre', type='assoc', b=1375,
  q="Associez chaque auteur à son ouvrage et à son apport sur la "
    "transformation sectorielle.",
  ans=[["Colin Clark", "Les conditions du progrès économique (1941)"],
       ["Jean Fourastié", "Le grand espoir du XXᵉ siècle (1949)"],
       ["Alfred Sauvy", "La machine et le chômage (1980) : la théorie du déversement"],
       ["Pierre Veltz", "La société hyper-industrielle (2017)"]],
  exp="Clark et Fourastié établissent que la productivité progresse à des "
      "rythmes différents selon les secteurs, et que ces écarts expliquent la "
      "transformation de la structure de l’emploi. Sauvy explique comment la "
      "main-d’œuvre passe d’un secteur à l’autre. Veltz, bien plus tard, "
      "conteste l’idée d’une économie devenue post-industrielle.",
  diss="Ces quatre références couvrent à elles seules toute une partie sur la "
       "désindustrialisation, du constat statistique à sa critique."),

f(id='q6-n43', sp='c6-08', niv='comprendre', type='qcm', b=1387,
  q="Pourquoi l’emploi agricole a-t-il fortement diminué alors que la "
    "production agricole augmentait ?",
  opts=["Parce que la demande alimentaire a reculé",
        "Parce que la productivité y a progressé très vite tandis que la "
        "demande alimentaire est peu élastique au revenu",
        "Parce que les agriculteurs ont été remplacés par des importations",
        "Parce que les prix agricoles ont augmenté"],
  ans=1,
  why=["La demande alimentaire n’a pas reculé : elle a seulement progressé "
       "moins vite que la productivité.",
       "Les importations existent, mais ce n’est pas le mécanisme retenu par "
       "la loi des trois secteurs.",
       "Les prix agricoles ont au contraire tendance à baisser en termes "
       "réels avec les gains de productivité."],
  exp="Mécanisation, engrais, sélection, irrigation et organisation ont "
      "produit des gains de productivité très élevés sur longue période. "
      "Mais, même quand le revenu augmente, on ne consomme pas "
      "proportionnellement plus de nourriture : la demande est peu élastique. "
      "La production peut donc augmenter tandis que l’emploi diminue — c’est "
      "l’exode rural.",
  diss="Le même raisonnement, appliqué à l’industrie puis aux services, donne "
       "toute la loi des trois secteurs : c’est le rapport entre croissance de "
       "la productivité et croissance de la demande qui décide du sort de "
       "l’emploi."),

f(id='q6-n44', sp='c6-08', niv='raisonner', type='qcm', b=1410,
  q="Pourquoi l’emploi tertiaire augmente-t-il « mécaniquement », selon la "
    "loi des trois secteurs ?",
  opts=["Parce que les services sont plus rentables que l’industrie",
        "Parce que la demande de services croît avec le niveau de vie alors "
        "que la productivité y est structurellement faible",
        "Parce que les services sont protégés de la concurrence "
        "internationale",
        "Parce que l’État emploie massivement dans le tertiaire"],
  ans=1,
  why=["La rentabilité n’est pas le critère : le raisonnement porte sur "
       "productivité et demande.",
       "Certains services sont effectivement peu exposés, mais ce n’est pas "
       "l’explication retenue.",
       "L’emploi public relève du tertiaire, mais la loi des trois secteurs "
       "ne repose pas sur ce point."],
  exp="Dans de nombreux services, le temps humain est incompressible : le "
      "coiffeur ne peut pas couper deux têtes à la fois, le soin et "
      "l’éducation exigent un temps relationnel. Comme la demande de santé, "
      "d’éducation, de loisirs et de services aux entreprises augmente avec "
      "le niveau de vie et que la productivité y progresse peu, il faut "
      "davantage de travailleurs.",
  diss="Attention à la nuance apportée plus loin par Veltz : le tertiaire "
       "n’est pas homogène — finance et numérique y sont très productifs."),

f(id='q6-n45', sp='c6-08', niv='comprendre', type='qcm', b=1425,
  q="Qu’appelle-t-on la théorie du déversement chez Alfred Sauvy ?",
  opts=["Le transfert des capitaux des secteurs anciens vers les secteurs "
        "nouveaux",
        "Le mécanisme par lequel les gains de productivité d’un secteur "
        "libèrent de la main-d’œuvre, qui se « déverse » vers un autre "
        "secteur",
        "La délocalisation de la production vers les pays à bas coûts",
        "La redistribution des gains de productivité vers les salaires"],
  ans=1,
  why=["Le déversement porte sur la main-d’œuvre, non sur les capitaux.",
       "La délocalisation est un déplacement géographique de la production, "
       "analysé plus loin.",
       "La répartition des gains de productivité est une autre question, "
       "traitée dans la partie sur la PGF."],
  exp="La chaîne historique typique comporte deux déversements : de "
      "l’agriculture vers l’industrie au XIXᵉ et au début du XXᵉ siècle, puis "
      "de l’industrie vers les services. Dans « La machine et le chômage » "
      "(1980), Sauvy répond à l’idée que les machines détruisent l’emploi : "
      "le progrès technique détruit des emplois dans certains secteurs mais "
      "en crée dans d’autres ; le chômage vient des difficultés d’adaptation, "
      "non des machines.",
  diss="C’est la référence à mobiliser face à tout sujet sur « le progrès "
       "technique détruit-il l’emploi ? » — en prenant soin d’en exposer "
       "ensuite la limite contemporaine."),

f(id='q6-n46', sp='c6-08', niv='raisonner', type='qcm', b=1452,
  q="Quelle limite inédite le cours oppose-t-il aujourd’hui à la théorie du "
    "déversement ?",
  opts=["Les gains de productivité agricoles sont désormais nuls",
        "Le tertiaire représente 70 à 75 % de l’emploi et connaît lui aussi "
        "des gains de productivité et une automatisation croissante : où la "
        "main-d’œuvre pourra-t-elle se déverser ?",
        "La population active diminue trop vite",
        "Les services ne sont pas délocalisables"],
  ans=1,
  why=["Les gains de productivité agricoles se poursuivent : ce n’est pas le "
       "problème soulevé.",
       "La démographie n’est pas l’argument retenu ici.",
       "La délocalisation des services est au contraire une réalité "
       "croissante, mais ce n’est pas la limite évoquée."],
  exp="Caisses automatiques, guichets bancaires numérisés, transports "
      "automatisés, tâches administratives automatisées : le secteur qui "
      "accueillait la main-d’œuvre devient lui-même productif. L’intelligence "
      "artificielle aggrave la question en touchant les tâches "
      "intellectuelles et les emplois qualifiés — juristes, comptables, "
      "traducteurs, métiers de la création — Frey et Osborne évoquant 47 % "
      "des tâches concernées.",
  diss="La réponse du cours n’est pas la disparition de l’emploi mais sa "
       "recomposition : des tâches disparaissent, d’autres apparaissent "
       "(conseil, supervision, accompagnement humain). L’enjeu devient la "
       "reconversion et la nature des compétences."),

f(id='q6-n47', sp='c6-08', niv='comprendre', type='qcm', b=1330,
  q="Pourquoi les rentes de monopole peuvent-elles ralentir les gains de "
    "productivité ?",
  opts=["Parce qu’elles réduisent le profit des entreprises",
        "Parce qu’en abaissant la pression concurrentielle, elles diminuent "
        "l’incitation à innover",
        "Parce qu’elles empêchent les économies d’échelle",
        "Parce qu’elles font baisser les prix"],
  ans=1,
  why=["Les rentes élèvent au contraire le profit de l’entreprise qui en "
       "bénéficie.",
       "Les positions dominantes permettent plutôt d’atteindre des économies "
       "d’échelle importantes.",
       "Une rente de monopole se traduit par des prix plus élevés, non plus "
       "bas."],
  exp="Dans une économie concurrentielle, la pression incite à innover, les "
      "entreprises inefficaces disparaissent et les ressources se réallouent "
      "vers les plus productives. À l’inverse, effets de réseau, barrières à "
      "l’entrée élevées et rentes de monopole desserrent cette pression. "
      "S’ajoutent les brevets défensifs, déposés non pour exploiter une "
      "innovation mais pour verrouiller un marché, et les coûts de "
      "transaction qu’engendrent les technologies brevetées multiples.",
  diss="Ce passage rejoint directement Aghion : la concurrence stimule "
       "l’innovation, mais les leaders cherchent à l’entraver — d’où le rôle "
       "de l’État garant de la concurrence."),

f(id='q6-n48', sp='c6-08', niv='connaitre', type='vf', b=1308,
  q="Selon les études citées par le cours, à caractéristiques proches, les "
    "différences de management peuvent expliquer jusqu’à 20 % d’écart de "
    "productivité entre entreprises.",
  ans=True,
  exp="Le management a longtemps été une variable sous-estimée. Le cours "
      "précise que, dans certains cas comme le commerce, un changement de "
      "manager peut entraîner une hausse très significative de la "
      "performance. Il relie ces écarts à la manière dont l’autorité, "
      "l’autonomie et l’innovation sont encouragées : un management trop "
      "vertical réduit l’initiative et l’expérimentation, dont dépend "
      "l’innovation."),

# ------------------ c6-09 désindustrialisation, externalisation, Veltz
f(id='q6-n49', sp='c6-09', niv='comprendre', type='qcm', b=1587,
  q="Quelle est la différence entre externaliser et délocaliser ?",
  opts=["Externaliser, c’est déplacer la production à l’étranger ; "
        "délocaliser, c’est la confier à un sous-traitant national",
        "Externaliser, c’est confier une activité à une autre entreprise, sur "
        "le territoire national ou non ; délocaliser, c’est déplacer la "
        "production à l’étranger",
        "Les deux termes sont équivalents",
        "Externaliser concerne les services, délocaliser l’industrie"],
  ans=1,
  why=["Les deux définitions sont inversées.",
       "Le cours insiste précisément sur le fait qu’externaliser n’est pas "
       "délocaliser.",
       "La distinction ne porte pas sur le secteur : on peut externaliser une "
       "production industrielle et délocaliser un service."],
  exp="Les deux opérations sont indépendantes : on peut externaliser sans "
      "délocaliser, délocaliser sans externaliser, ou faire les deux. "
      "Confondre les deux conduit à surestimer l’effet de la mondialisation "
      "sur la désindustrialisation.",
  diss="Distinction peu coûteuse à retenir et très valorisée : elle montre "
       "qu’on ne confond pas réorganisation productive et transfert "
       "géographique."),

f(id='q6-n50', sp='c6-09', niv='raisonner', type='qcm', b=1529,
  q="Qu’appelle-t-on l’« effet d’optique » de la désindustrialisation ?",
  opts=["Une erreur de mesure du PIB industriel",
        "Le fait que l’externalisation transforme un emploi industriel en "
        "emploi tertiaire sans que la production change",
        "Le fait que l’industrie polluante soit comptée dans les services",
        "Le fait que la valeur ajoutée industrielle soit sous-estimée par "
        "l’inflation"],
  ans=1,
  why=["Il ne s’agit pas d’une erreur de mesure du PIB, mais d’un "
       "reclassement d’emplois entre secteurs.",
       "Rien de tel dans le cours.",
       "L’inflation n’intervient pas dans ce mécanisme."],
  exp="Quand une entreprise industrielle confie à un prestataire sa "
      "comptabilité, son nettoyage, son gardiennage ou son informatique, ces "
      "emplois quittent les statistiques de l’industrie pour celles des "
      "services, sans que la production de voitures change. C’est ce qui "
      "explique l’énigme des années 1980-1990 : la part de l’emploi "
      "industriel baisse fortement alors que la valeur ajoutée industrielle "
      "reste relativement stable.",
  diss="Cet effet oblige à préciser l’indicateur retenu : part de l’industrie "
       "dans la valeur ajoutée, ou part dans l’emploi. Le diagnostic diffère "
       "selon le choix."),

f(id='q6-n51', sp='c6-09', niv='connaitre', type='qcmm', b=1549,
  q="Quelles sont les trois causes majeures de la désindustrialisation "
    "retenues par le cours ? (plusieurs réponses)",
  opts=["Les gains de productivité industriels, très supérieurs à la moyenne",
        "L’externalisation des tâches non productives",
        "La mondialisation et les délocalisations",
        "La baisse de la demande de biens industriels",
        "La disparition des brevets industriels"],
  ans=[0, 1, 2],
  why=["Exacte : environ 3,4 % par an dans l’industrie contre 1,3 % en "
       "moyenne en France, d’où une substitution du capital au travail.",
       "Exacte : les entreprises se recentrent sur leur cœur de métier et "
       "confient le reste au tertiaire.",
       "Exacte : la recherche de coûts plus faibles conduit à externaliser ou "
       "à délocaliser.",
       "La demande de biens industriels n’a pas reculé : c’est la "
       "productivité qui a progressé plus vite qu’elle.",
       "Rien de tel dans le cours."],
  exp="Le cours ajoute une comparaison internationale : la France a "
      "davantage recouru aux délocalisations, tandis que l’Allemagne et "
      "l’Italie ont mieux maintenu la production sur leur territoire, ce qui "
      "s’explique par un choix stratégique — compétitivité-prix d’un côté, "
      "compétitivité hors-prix de l’autre."),

f(id='q6-n52', sp='c6-09', niv='comprendre', type='qcm', b=1640,
  q="Pourquoi Pierre Veltz parle-t-il de société « hyper-industrielle » "
    "plutôt que post-industrielle ?",
  opts=["Parce que l’emploi industriel augmente de nouveau",
        "Parce que plus l’économie semble immatérielle, plus elle dépend "
        "d’infrastructures industrielles lourdes",
        "Parce que l’industrie représente désormais la majorité de la valeur "
        "ajoutée",
        "Parce que les services ont disparu au profit de l’industrie"],
  ans=1,
  why=["L’emploi industriel ne repart pas : c’est la matérialité du "
       "numérique qui est en cause, pas le volume d’emplois.",
       "L’industrie reste stable en part de valeur ajoutée mondiale, elle "
       "n’est pas majoritaire.",
       "Veltz montre au contraire l’imbrication des deux, non la disparition "
       "de l’un."],
  exp="Le numérique n’est pas immatériel : il repose sur des câbles "
      "sous-marins — environ 98 % des flux mondiaux —, des data centers "
      "énergivores, des serveurs, des antennes, des métaux rares et des "
      "infrastructures électriques massives. La « dématérialisation » cache "
      "donc une matérialité renforcée : le numérique est une industrie "
      "cachée.",
  diss="Thèse très efficace pour nuancer un sujet sur l’économie de la "
       "connaissance : l’immatériel repose sur du très matériel, ce qui a des "
       "conséquences géopolitiques."),

f(id='q6-n53', sp='c6-09', niv='appliquer', type='qcm', b=1651,
  q="Michelin vend des kilomètres parcourus, Airbus des heures de vol, "
    "Renault de la mobilité. Comment le cours qualifie-t-il ce mouvement ?",
  opts=["La délocalisation des services",
        "L’industrie servicielle : la valeur ne repose plus seulement sur le "
        "bien matériel mais sur l’usage et le service associé",
        "L’économie de la fonctionnalité au sens de l’économie circulaire "
        "uniquement",
        "La tertiarisation statistique"],
  ans=1,
  why=["Aucune production n’est déplacée à l’étranger dans ces exemples.",
       "L’économie de la fonctionnalité est bien un pilier de l’économie "
       "circulaire, mais ici le cours nomme explicitement l’industrie "
       "servicielle.",
       "La tertiarisation statistique désigne le reclassement des emplois, "
       "non la transformation de l’offre."],
  exp="Le mouvement est symétrique : l’industrie devient servicielle — "
      "maintenance, logiciels, contrats d’usage, solutions globales — tandis "
      "que les services deviennent industriels — usines de données, chaînes "
      "d’approvisionnement complexes, forte intensité énergétique, logistique "
      "mondiale. Ce brouillage remet en cause la typologie sectorielle "
      "traditionnelle de Clark et Fourastié.",
  diss="Conclusion de Veltz : la productivité devient systémique, elle dépend "
       "de l’ensemble du système productif et non d’un secteur isolé."),

f(id='q6-n54', sp='c6-09', niv='raisonner', type='courte', b=1734,
  q="Pourquoi la réindustrialisation ne garantit-elle pas une amélioration du "
    "solde commercial ?",
  ans={'modele': "Parce que la production est fragmentée en chaînes de valeur "
       "mondiales. Même en fabriquant à nouveau des voitures en France, on ne "
       "produit pas tout de A à Z : le produit final incorpore des "
       "consommations intermédiaires — pièces détachées, composants, métaux "
       "et matériaux, semi-conducteurs, logiciels — largement importées. "
       "Réindustrialiser peut donc réduire les importations de produits finis "
       "tout en augmentant celles de biens intermédiaires. L’effet net sur le "
       "solde commercial n’est pas automatique.",
       'cles': [{'f': ['chaine de valeur', 'cvm', 'fragmentation'],
                 'l': 'la fragmentation des chaînes de valeur mondiales'},
                {'f': ['consommation intermediaire', 'composant', 'piece', 'semi conducteur'],
                 'l': 'des consommations intermédiaires importées'},
                {'f': ['solde', 'importation', 'pas automatique', 'commercial'],
                 'l': 'donc un effet sur le solde commercial non automatique'}]},
  exp="Le cours relève une seconde limite : la compétitivité. Produire en "
      "Europe pose la question du coût et de la vendabilité du produit, d’où "
      "deux réponses évoquées — la robotisation, qui réduit le poids du coût "
      "du travail, et la stratégie allemande de compétitivité hors-prix.",
  diss="Il faut aussi distinguer le diagnostic français du diagnostic "
       "européen : tous les pays européens se tertiarisent, mais la "
       "désindustrialisation est plus marquée en France."),

# ----------------------------------------- c6-10 mesurer les inégalités
f(id='q6-n55', sp='c6-10', niv='appliquer', type='qcm', b=1771,
  q="Dans un pays, D1 = 1 200 € et D9 = 4 800 €. Que vaut le rapport "
    "interdécile et comment l’interpréter ?",
  opts=["3 600 : c’est l’écart absolu entre les deux groupes",
        "4 : les 10 % les plus riches gagnent quatre fois plus que les 10 % "
        "les plus pauvres",
        "0,25 : les plus pauvres gagnent un quart de ce que gagnent les plus "
        "riches",
        "40 % : la part du revenu détenue par le dernier décile"],
  ans=1,
  why=["3 600 € est bien l’écart absolu, mais le rapport interdécile est un "
       "quotient, non une différence.",
       "0,25 est le rapport inverse, D1/D9, qui n’est pas l’indicateur "
       "usuel.",
       "La part du revenu détenue par un groupe est ce que mesure le "
       "coefficient de Palma, pas l’interdécile."],
  exp="Le rapport interdécile D9/D1 vaut 4 800 / 1 200 = 4. Il indique "
      "combien de fois les plus riches gagnent plus que les plus pauvres. "
      "Attention à la nature des grandeurs : D1 et D9 sont des seuils, non "
      "des parts de revenu.",
  diss="Préciser qu’il s’agit de seuils permet d’enchaîner naturellement sur "
       "la limite de l’indicateur : il ne dit rien de la distribution à "
       "l’intérieur des déciles."),

f(id='q6-n56', sp='c6-10', niv='raisonner', type='qcmm', b=1795,
  q="Quelles limites le cours attribue-t-il au rapport interdécile ? "
    "(plusieurs réponses)",
  opts=["Il ignore les inégalités intermédiaires et ne dit rien des 80 % "
        "centraux",
        "Il ne distingue pas le top 1 % du reste des 10 % les plus riches",
        "Il peut rester stable alors que les très hauts revenus explosent",
        "Il ne mesure pas la concentration globale des revenus",
        "Il est impossible à comparer entre pays"],
  ans=[0, 1, 2, 3],
  why=["Exacte : il ne capte pas non plus les évolutions à l’intérieur des "
       "déciles.",
       "Exacte : or les inégalités récentes se concentrent dans le top 1 %, "
       "le top 0,1 % et le top 0,01 %.",
       "Exacte : c’est la conséquence directe du point précédent.",
       "Exacte : contrairement au Gini, il ne synthétise pas toute la "
       "distribution.",
       "Au contraire, sa simplicité en fait un bon outil de comparaison "
       "internationale et de suivi temporel."],
  exp="Ces limites expliquent l’ordre du cours : l’interdécile, simple et "
      "lisible, est complété par le Palma, plus sensible au sommet, puis par "
      "le Gini, qui prend en compte l’ensemble de la distribution."),

f(id='q6-n57', sp='c6-10', niv='appliquer', type='qcm', b=1828,
  q="Les 10 % les plus riches détiennent 35 % du revenu national, les 50 % "
    "les plus pauvres 20 %. Que vaut le coefficient de Palma ?",
  opts=["0,57", "1,75", "15 points", "2,5"],
  ans=1,
  why=["0,57 est le rapport inverse, qui n’est pas l’indicateur retenu.",
       "15 points est l’écart entre les deux parts, non leur rapport.",
       "2,5 ne correspond à aucun calcul possible à partir de ces données."],
  exp="Palma = 35 / 20 = 1,75 : les 10 % les plus riches captent 1,75 fois "
      "plus de revenu que la moitié la plus pauvre de la population. "
      "Contrairement à l’interdécile qui compare des seuils, le Palma compare "
      "des parts totales de revenu.",
  diss="Le Palma est l’indicateur de la polarisation : il oppose une élite "
       "restreinte à une large base, ce qui correspond aux évolutions "
       "observées depuis 1980."),

f(id='q6-n58', sp='c6-10', niv='comprendre', type='qcm', b=1867,
  q="Comment le coefficient de Gini est-il construit et interprété ?",
  opts=["Il compare les deux déciles extrêmes et varie de 1 à l’infini",
        "Il est construit à partir de la courbe de Lorenz, varie entre 0 "
        "(égalité parfaite) et 1 (inégalité totale), et prend en compte "
        "l’ensemble de la distribution",
        "Il mesure la part du revenu du top 1 % et s’exprime en pourcentage",
        "Il compare le revenu moyen au revenu médian"],
  ans=1,
  why=["C’est la logique du rapport interdécile, dont le Gini se distingue "
       "précisément.",
       "La part du top 1 % est un autre indicateur, auquel le Gini est "
       "d’ailleurs peu sensible.",
       "Le rapport moyenne / médiane mesure l’asymétrie, non la "
       "concentration globale."],
  exp="La courbe de Lorenz porte la population cumulée en abscisse et le "
      "revenu cumulé en ordonnée ; la droite d’équirépartition correspondrait "
      "à une société parfaitement égalitaire. Plus la courbe réelle s’éloigne "
      "de cette droite, plus les inégalités sont fortes. En pratique, les "
      "pays égalitaires se situent autour de 0,25-0,30 — la France environ "
      "0,29, et 0,297 en 2023 — les pays très inégalitaires entre 0,45 et "
      "0,60.",
  diss="Ses limites doivent être dites : peu intuitif, il ne montre pas où se "
       "situent les écarts et peut rester stable alors que le top 1 % "
       "s’enrichit."),

f(id='q6-n59', sp='c6-10', niv='raisonner', type='qcm', b=1903,
  q="Pourquoi le coefficient de Gini du patrimoine est-il systématiquement "
    "plus élevé que celui du revenu ?",
  opts=["Parce que le patrimoine est plus difficile à mesurer",
        "Parce que le patrimoine se transmet, génère lui-même du revenu et "
        "s’accumule dans le temps",
        "Parce que les revenus sont davantage redistribués par l’impôt",
        "Parce que le patrimoine est concentré dans l’immobilier"],
  ans=1,
  why=["Les difficultés de mesure existent mais n’expliquent pas l’écart "
       "systématique.",
       "La redistribution des revenus joue dans le même sens, mais le cours "
       "retient d’abord la logique cumulative du patrimoine.",
       "La composition du patrimoine ne détermine pas sa concentration."],
  exp="Le patrimoine est un stock, le revenu un flux. Le stock génère des "
      "revenus — loyers, intérêts, dividendes — qui permettent d’accumuler "
      "davantage de capital, et il se transmet par héritage ou donation. La "
      "concentration tend donc à se reproduire dans le temps : les inégalités "
      "patrimoniales sont structurellement plus fortes.",
  diss="Articuler flux et stock permet de passer d’un constat statique à une "
       "dynamique : c’est l’argument central de toute analyse patrimoniale "
       "des inégalités."),

f(id='q6-n60', sp='c6-10', niv='connaitre', type='qcm', b=1931,
  q="Sur quelle observation Simon Kuznets fonde-t-il son hypothèse de 1955 ?",
  opts=["L’évolution des inégalités aux États-Unis entre 1913 et 1948",
        "L’évolution des inégalités mondiales entre 1988 et 2008",
        "Le rattrapage des pays d’Asie de l’Est après 1945",
        "La comparaison des coefficients de Gini européens"],
  ans=0,
  why=["La période 1988-2008 est celle de la courbe de l’éléphant de "
       "Milanovic.",
       "Le rattrapage asiatique relève d’une autre partie du chapitre.",
       "Kuznets ne procède pas par comparaison internationale de Gini."],
  exp="Kuznets observe les États-Unis sur 1913-1948 et formule l’hypothèse "
      "d’une relation en cloche — une courbe en U inversé : au début du "
      "développement, les inégalités augmentent ; à un stade avancé, elles "
      "diminuent. Le cours insiste ensuite sur la limite : cette baisse n’est "
      "pas automatique, elle dépend de la redistribution et des choix "
      "politiques.",
  diss="Depuis 1980, la hausse des inégalités de revenus, la concentration "
       "des patrimoines et l’explosion du top 1 % semblent contredire la "
       "phase descendante : c’est l’objection décisive."),

f(id='q6-n61', sp='c6-10', niv='comprendre', type='assoc', b=1997,
  q="Associez chaque point de la courbe de l’éléphant de Milanovic à sa "
    "signification.",
  ans=[["Point A — les plus pauvres du monde", "Croissance réelle d’environ +15 % : ils bénéficient peu de la mondialisation"],
       ["Point B — la classe moyenne des pays émergents", "+70 à +80 % : les grands gagnants, surtout en Chine, en Inde et en Asie"],
       ["Point C — le top 1 % mondial", "Environ +60 %, dont la moitié d’Américains : une ploutocratie mondiale"],
       ["Le creux autour du 80ᵉ percentile", "Les classes moyennes occidentales : croissance proche de 0 %, sentiment de déclassement"]],
  exp="La méthode importe autant que le résultat : l’abscisse classe la "
      "population mondiale par revenu initial, l’ordonnée donne le taux de "
      "croissance du revenu réel, mesuré en parité de pouvoir d’achat. Les "
      "résultats ne sont donc biaisés ni par l’inflation ni par les taux de "
      "change. La thèse centrale est que les inégalités entre pays diminuent "
      "tandis que les inégalités à l’intérieur des pays augmentent.",
  diss="La courbe explique économiquement un fait politique : la montée des "
       "tensions dans les démocraties occidentales, dont les classes moyennes "
       "sont les perdantes relatives de la mondialisation."),

f(id='q6-n62', sp='c6-10', niv='raisonner', type='qcm', b=2026,
  q="Qu’appelle-t-on la « rente de citoyenneté » chez Milanovic ?",
  opts=["Le revenu que l’État verse à ses ressortissants",
        "Le fait que l’inégalité majeure aujourd’hui provienne du lieu de "
        "naissance, qui détermine largement le revenu et les opportunités",
        "Les droits sociaux acquis par l’ancienneté dans un pays",
        "La prime de salaire versée aux travailleurs nationaux"],
  ans=1,
  why=["Il ne s’agit pas d’un transfert monétaire mais d’un avantage "
       "structurel.",
       "Les droits sociaux relèvent d’un autre débat.",
       "Aucune prime de ce type n’est en cause."],
  exp="Naître dans un pays riche procure un revenu structurellement plus "
      "élevé, un meilleur accès aux opportunités et un avantage durable. La "
      "nationalité devient donc un facteur central d’inégalité mondiale — "
      "plus déterminant, pour un individu, que sa position dans la "
      "distribution de son propre pays.",
  diss="Argument très fort dans un sujet sur les inégalités mondiales : il "
       "déplace la question de la redistribution interne vers la mobilité et "
       "l’aide internationale."),

f(id='q6-n63', sp='c6-10', niv='comprendre', type='qcm', b=1958,
  q="Pourquoi le cours affirme-t-il que « les inégalités sont aussi un choix "
    "de société » ?",
  opts=["Parce que les individus choisissent leur niveau de revenu",
        "Parce que la réduction des inégalités n’est pas automatique : elle "
        "dépend du niveau de redistribution, du système fiscal, des "
        "institutions et de la protection sociale",
        "Parce que les inégalités sont acceptées par les électeurs",
        "Parce que le coefficient de Gini dépend des conventions de mesure"],
  ans=1,
  why=["Le revenu ne résulte pas d’un simple choix individuel.",
       "L’acceptation électorale est une question politique, non le "
       "mécanisme économique visé.",
       "Les conventions de mesure affectent le chiffre, pas le niveau réel "
       "des inégalités."],
  exp="C’est la principale limite opposée à Kuznets : il avait fait de la "
      "phase descendante une évolution presque mécanique, alors que le cours "
      "montre que la baisse des inégalités dépend de décisions publiques. Le "
      "retour des inégalités depuis 1980 dans de nombreux pays développés "
      "confirme ce point.",
  diss="Cette formule est la bonne manière de conclure une partie sur "
       "croissance et inégalités : refuser l’automaticité sans nier les "
       "mécanismes économiques."),

# -------------------- c6-11 revenus et patrimoines ; Harrod-Domar (cadre)
f(id='q6-n64', sp='c6-11', niv='connaitre', type='qcm', b=2047,
  q="Quelle distinction sépare le revenu du patrimoine ?",
  opts=["Le revenu est un stock, le patrimoine un flux",
        "Le revenu est un flux perçu sur une période, le patrimoine un stock "
        "détenu à un moment donné",
        "Le revenu concerne le travail, le patrimoine le capital productif "
        "uniquement",
        "Le revenu est imposable, le patrimoine non"],
  ans=1,
  why=["Les deux notions sont inversées.",
       "Le revenu comprend aussi les revenus du capital et les prestations "
       "sociales ; le patrimoine comprend l’immobilier et les actifs "
       "financiers, pas seulement le capital productif.",
       "La fiscalité n’entre pas dans la définition."],
  exp="Le revenu — salaires, revenus du capital, prestations sociales — est "
      "mesuré annuellement. Le patrimoine — biens immobiliers, actifs "
      "financiers, épargne, capital productif — est accumulé dans le temps. "
      "Cette différence de nature explique le constat empirique : les "
      "inégalités de patrimoine sont systématiquement plus fortes que celles "
      "de revenus.",
  diss="Toujours préciser laquelle des deux grandeurs on mesure : une même "
       "société paraît modérément ou très inégalitaire selon le choix."),

f(id='q6-n65', sp='c6-11', niv='connaitre', type='qcm', b=2089,
  q="Dans quel courant et dans quel contexte le modèle de Harrod-Domar "
    "s’inscrit-il ?",
  opts=["Néoclassique, dans le contexte des Trente Glorieuses",
        "(Post-)keynésien, à partir de l’expérience de la crise des années "
        "1930",
        "Monétariste, dans le contexte de l’inflation des années 1970",
        "Institutionnaliste, à partir de la Révolution industrielle anglaise"],
  ans=1,
  why=["C’est Solow, en 1956, qui propose la réponse néoclassique dans le "
       "contexte de la reconstruction.",
       "Le monétarisme et l’inflation des années 1970 n’ont rien à voir avec "
       "ce modèle.",
       "L’analyse institutionnelle est celle de North et d’Acemoglu, en fin "
       "de chapitre."],
  exp="Roy Harrod publie son article en 1939 (repris en 1948), Evsey Domar en "
      "1947. Tous deux ont assisté à la crise de 1929 et contestent l’idée "
      "néoclassique selon laquelle les marchés seraient naturellement à "
      "l’équilibre. Leur objectif est de montrer que la croissance n’est pas "
      "naturellement équilibrée mais structurellement déséquilibrée.",
  diss="Situer le modèle dans son contexte permet d’expliquer ses hypothèses : "
       "si l’on écrit après 1929, l’absence de mécanisme d’ajustement "
       "automatique n’est pas une hypothèse arbitraire."),

f(id='q6-n66', sp='c6-11', niv='comprendre', type='qcm', b=2126,
  q="D’où vient la croissance dans le modèle de Harrod-Domar ?",
  opts=["De l’offre : la croissance dépend des capacités productives "
        "disponibles",
        "De la demande : les entreprises produisent si elles anticipent "
        "vendre, et l’investissement dépend des débouchés",
        "Du progrès technique, endogénéisé par la R&D",
        "De la démographie seule"],
  ans=1,
  why=["C’est la logique néoclassique, que Harrod et Domar récusent "
       "précisément.",
       "Le progrès technique reste exogène dans ce modèle : il ne crée aucun "
       "mécanisme d’ajustement.",
       "La démographie détermine le taux naturel, soit l’un des trois taux, "
       "mais n’est pas l’origine de la croissance."],
  exp="La filiation keynésienne est ici centrale : la croissance dépend de la "
      "demande effective. Il faut augmenter la demande pour que les "
      "entreprises décident de produire plus, et l’investissement dépend des "
      "débouchés anticipés. La variable centrale devient donc "
      "l’investissement, avec son double effet — revenu et capacité."),

f(id='q6-n67', sp='c6-11', niv='comprendre', type='qcmm', b=2108,
  q="Quelles hypothèses caractérisent le modèle de Harrod-Domar ? "
    "(plusieurs réponses)",
  opts=["Économie fermée",
        "Facteurs de production complémentaires, sans substituabilité "
        "capital / travail",
        "Coefficients techniques stables à court terme",
        "Absence de mécanisme automatique d’ajustement",
        "Prix et salaires parfaitement flexibles"],
  ans=[0, 1, 2, 3],
  why=["Exacte : ni importations ni exportations.",
       "Exacte : c’est l’hypothèse décisive, inverse de celle de "
       "Cobb-Douglas et de Solow.",
       "Exacte : les rapports K/Y et L/Y sont supposés stables.",
       "Exacte : rien ne ramène spontanément l’économie à l’équilibre.",
       "La flexibilité des prix et des salaires est au contraire une "
       "hypothèse de Solow, qui lui permet d’obtenir un ajustement."],
  exp="Ces hypothèses sont essentielles parce qu’elles expliquent le "
      "résultat : si les facteurs ne sont pas substituables, si les "
      "coefficients techniques sont rigides et si aucun prix ne s’ajuste, "
      "l’économie ne peut pas corriger spontanément un déséquilibre. "
      "L’instabilité n’est donc pas un accident du modèle : elle en découle."),

# ----------------- c6-12 coefficient de capital, trois taux, fil du rasoir
f(id='q6-n68', sp='c6-12', niv='comprendre', type='qcm', b=2143,
  q="Qu’est-ce que le coefficient de capital, et pourquoi est-il la clé du "
    "modèle de Harrod-Domar ?",
  opts=["Le rapport entre l’investissement et l’épargne ; il détermine le "
        "taux d’intérêt",
        "La quantité de capital nécessaire pour produire une unité de "
        "production ; supposé constant et rigide, il impose un rythme précis "
        "d’accumulation",
        "La part du capital dans la valeur ajoutée ; il mesure le partage des "
        "revenus",
        "Le taux de dépréciation annuel du capital"],
  ans=1,
  why=["Le rapport épargne-investissement est la condition d’équilibre, non "
       "le coefficient de capital.",
       "Le partage de la valeur ajoutée est une autre question.",
       "Le taux de dépréciation est l’amortissement, central chez Solow et "
       "non ici."],
  exp="Si v = 3, il faut trois unités de capital pour produire une unité de "
      "richesse. Comme les facteurs sont complémentaires et le coefficient "
      "constant à court terme, produire plus exige proportionnellement plus "
      "de capital : on ne peut pas compenser un manque de capital par plus de "
      "travail. L’économie est structurellement rigide, et si "
      "l’investissement n’est pas exactement au niveau requis, les capacités "
      "sont soit insuffisantes, soit excessives.",
  diss="Règle à retenir : plus le coefficient de capital est élevé, plus la "
       "croissance exige d’investissement, plus l’économie est rigide."),

f(id='q6-n69', sp='c6-12', niv='comprendre', type='qcm', b=2132,
  q="Quel est le double effet de l’investissement chez Harrod et Domar ?",
  opts=["Un effet revenu, par le multiplicateur, et un effet de capacité, par "
        "l’accumulation de capital",
        "Un effet prix et un effet volume",
        "Un effet d’éviction et un effet de levier",
        "Un effet de substitution et un effet de revenu"],
  ans=0,
  why=["Effet prix et effet volume décomposent une variation de valeur, non "
       "l’investissement.",
       "Éviction et levier sont des notions de finance publique et "
       "d’entreprise.",
       "Substitution et revenu décomposent l’effet d’une variation de prix "
       "sur la demande du consommateur."],
  exp="L’investissement alimente la demande — c’est le multiplicateur "
      "keynésien — mais il accroît aussi les capacités de production. Pour "
      "qu’il n’y ait ni surproduction ni pénurie, il faut que ces deux "
      "effets se compensent exactement : l’investissement doit croître à un "
      "taux constant égal au rapport entre le taux d’épargne et le "
      "coefficient de capital. C’est la définition du taux garanti.",
  diss="Comprendre ce double effet est indispensable : c’est de là que naît "
       "l’instabilité, puisque rien n’assure l’égalité des deux effets."),

f(id='q6-n70', sp='c6-12', niv='connaitre', type='assoc', b=2177,
  q="Associez chacun des trois taux de croissance de Harrod à sa définition.",
  ans=[["Le taux effectif (g)", "La croissance réellement observée, dépendant de la conjoncture et des anticipations"],
       ["Le taux garanti (g_w)", "Le taux assurant l’équilibre épargne-investissement : s / v"],
       ["Le taux naturel (g_n)", "Le taux compatible avec le plein emploi, déterminé par la population active"]],
  exp="L’essentiel est que ces trois taux dépendent de mécanismes "
      "indépendants : la conjoncture pour le premier, le comportement "
      "d’épargne et la structure productive pour le deuxième, la démographie "
      "pour le troisième. Aucun mécanisme automatique ne les fait converger, "
      "et c’est de cette non-coïncidence que naît l’instabilité fondamentale "
      "du modèle.",
  diss="Savoir dire de quoi dépend chaque taux permet d’expliquer pourquoi "
       "leur égalité est improbable — tout l’argument du fil du rasoir."),

f(id='q6-n71', sp='c6-12', niv='raisonner', type='qcm', b=2235,
  q="Que désigne l’image du « fil du rasoir » chez Harrod ?",
  opts=["La difficulté de mesurer précisément le coefficient de capital",
        "Le fait que la croissance équilibrée suppose une triple "
        "coïncidence improbable, dont la moindre déviation entraîne une "
        "divergence cumulative",
        "La nécessité d’un taux d’épargne très élevé",
        "Le risque d’inflation lié à une croissance trop rapide"],
  ans=1,
  why=["La mesure du coefficient de capital n’est pas le problème : c’est sa "
       "rigidité.",
       "Un taux d’épargne élevé peut au contraire provoquer une insuffisance "
       "de demande.",
       "L’inflation n’est pas le mécanisme central de ce modèle."],
  exp="La croissance équilibrée suppose une parfaite correspondance entre "
      "épargne et investissement, une parfaite adéquation entre capacités "
      "productives et main-d’œuvre, et une stabilité des anticipations. Cette "
      "triple condition est extrêmement improbable : l’équilibre est "
      "exceptionnel, fragile, et dépend d’un concours heureux de "
      "circonstances. La moindre déviation entraîne une divergence "
      "cumulative, vers la récession ou vers la surchauffe.",
  diss="C’est la formule à opposer à Solow : chez Harrod, l’équilibre est "
       "l’exception ; chez Solow, l’économie y converge naturellement."),

f(id='q6-n72', sp='c6-12', niv='raisonner', type='ordre', b=2257,
  q="Remettez dans l’ordre l’impasse provoquée par un taux d’épargne trop "
    "élevé.",
  ans=["Le taux d’épargne augmente fortement",
       "La consommation diminue, la demande globale devient insuffisante",
       "Les entreprises ne vendent pas toute leur production : surproduction",
       "Elles licencient, les revenus des ménages diminuent",
       "La consommation baisse encore : cercle vicieux dépressif"],
  exp="Le cours insiste sur la symétrie du problème : un taux d’épargne trop "
      "faible produit l’impasse inverse — investissement insuffisant, "
      "accumulation ralentie, capacités productives qui progressent trop "
      "lentement, contrainte d’offre. Le vrai problème n’est donc pas "
      "« trop » ou « pas assez » d’épargne, mais l’absence de mécanisme "
      "d’ajustement automatique.",
  diss="Présenter les deux impasses côte à côte montre que l’instabilité est "
       "structurelle, et non liée à une mauvaise valeur d’un paramètre."),

f(id='q6-n73', sp='c6-12', niv='comprendre', type='qcm', b=2306,
  q="Comment Harrod et Domar justifient-ils l’intervention de l’État ?",
  opts=["Par la nécessité de réduire les inégalités",
        "Parce que l’équilibre n’est pas automatique : les marchés ne sont pas "
        "coordonnés, les anticipations peuvent être pessimistes et la demande "
        "durablement insuffisante",
        "Par la nécessité de financer la R&D",
        "Parce que le progrès technique est endogène"],
  ans=1,
  why=["La réduction des inégalités n’est pas l’argument de ce modèle.",
       "Le financement de la R&D est la justification de Romer et d’Aghion, "
       "beaucoup plus tard.",
       "Le progrès technique est au contraire exogène chez Harrod-Domar."],
  exp="L’État peut stimuler la demande par des politiques budgétaires, "
      "soutenir l’investissement, stabiliser les anticipations et réduire le "
      "chômage. L’intervention est donc une réponse à l’instabilité "
      "structurelle du capitalisme, et non un correctif ponctuel.",
  diss="Comparer les justifications de l’intervention selon les modèles est "
       "très rentable : conjoncturelle chez Harrod-Domar, inutile à long "
       "terme chez Solow, structurelle chez Lucas, Barro, Romer et Aghion."),

f(id='q6-n74', sp='c6-12', niv='raisonner', type='courte', b=2320,
  q="Comment Solow répond-il au pessimisme de Harrod et Domar ?",
  ans={'modele': "Solow change les hypothèses. Là où Harrod et Domar "
       "supposaient des facteurs complémentaires, des coefficients techniques "
       "rigides et des prix fixes, Solow suppose des facteurs substituables, "
       "une productivité marginale décroissante du capital et des prix et "
       "salaires flexibles. Des mécanismes d’ajustement redeviennent alors "
       "possibles : les déséquilibres ne sont plus cumulatifs, l’économie "
       "converge vers un sentier stable. La croissance peut être régulière et "
       "équilibrée, mais elle rencontre une autre limite, interne : l’état "
       "stationnaire, que seul le progrès technique permet de repousser.",
       'cles': [{'f': ['substituable', 'flexible', 'hypothese'],
                 'l': 'il change les hypothèses : substituabilité et flexibilité'},
                {'f': ['ajustement', 'converge', 'stable', 'equilibre'],
                 'l': 'des mécanismes d’ajustement rendent la croissance stable'},
                {'f': ['stationnaire', 'decroissant', 'limite'],
                 'l': 'mais une nouvelle limite apparaît : l’état stationnaire'},
                {'f': ['progres technique', 'exogene', 'repousser'],
                 'l': 'que seul le progrès technique, exogène, permet de repousser'}]},
  exp="La leçon de méthode est importante : les conclusions opposées des deux "
      "modèles ne viennent pas des faits mais des hypothèses. Discuter un "
      "modèle de croissance consiste d’abord à discuter ses hypothèses.",
  diss="Opposition centrale du chapitre : « l’équilibre à long terme est-il "
       "la règle ou l’exception ? » — première des trois questions que le "
       "cours assigne aux théories de la croissance."),

# ----------------------------------------- c6-13 Solow, Lucas
f(id='q6-n75', sp='c6-13', niv='comprendre', type='qcmm', b=2331,
  q="Quelles hypothèses structurent le modèle de Solow ? (plusieurs réponses)",
  opts=["Facteurs substituables entre capital et travail",
        "Productivité marginale décroissante du capital",
        "Rendements d’échelle constants",
        "Toute l’épargne est investie (S = I)",
        "Progrès technique endogène, produit par la R&D"],
  ans=[0, 1, 2, 3],
  why=["Exacte : c’est la rupture décisive avec Harrod-Domar.",
       "Exacte : elle engendre l’état stationnaire.",
       "Exacte : doubler les facteurs double la production.",
       "Exacte : l’épargne finance intégralement l’investissement.",
       "Le progrès technique reste exogène : c’est la limite centrale du "
       "modèle, et le point de départ des théories endogènes."],
  exp="Le cours ajoute deux hypothèses : la concurrence pure et parfaite, "
      "simplement posée, et la flexibilité des prix et des salaires, qui "
      "rend possibles les mécanismes d’ajustement. Chaque hypothèse est "
      "l’inverse d’une hypothèse de Harrod-Domar, ce qui suffit à expliquer "
      "l’opposition de leurs conclusions."),

f(id='q6-n76', sp='c6-13', niv='raisonner', type='ordre', b=2360,
  q="Remettez dans l’ordre le mécanisme qui conduit à l’état stationnaire "
    "chez Solow.",
  ans=["L’épargne par tête s·f(k) finance l’investissement par tête",
       "Mais la productivité marginale du capital est décroissante : f(k) est "
       "concave",
       "L’amortissement δk, lui, croît proportionnellement au stock de capital",
       "À mesure que k augmente, l’investissement progresse moins vite que "
       "l’amortissement",
       "Au point k* où s·f(k) = δk, le capital par tête cesse d’augmenter : "
       "la production par tête devient constante"],
  exp="La convergence est bilatérale : si s·f(k) dépasse δk, le capital par "
      "tête augmente ; s’il est inférieur, l’investissement ne compense plus "
      "l’usure et k diminue. L’économie revient donc naturellement vers k*. "
      "C’est ce mécanisme d’auto-équilibrage qui distingue Solow de "
      "Harrod-Domar.",
  diss="Enchaînement à maîtriser pour justifier proprement la limite interne "
       "de la croissance par accumulation, sans se contenter d’affirmer que "
       "« les rendements sont décroissants »."),

f(id='q6-n77', sp='c6-13', niv='appliquer', type='qcm', b=2379,
  q="Pourquoi le modèle de Solow implique-t-il une convergence seulement "
    "« conditionnelle » ?",
  opts=["Parce que la convergence suppose que les pays aient les mêmes "
        "paramètres — taux d’épargne, démographie, technologie",
        "Parce que seuls les pays développés convergent",
        "Parce que la convergence dépend de l’aide internationale",
        "Parce qu’elle n’a jamais été observée"],
  ans=0,
  why=["Le modèle ne réserve pas la convergence à un groupe de pays.",
       "L’aide internationale n’intervient pas dans le modèle.",
       "Des rattrapages ont bien été observés : Japon, Asie de l’Est, Chine."],
  exp="Le mécanisme est clair : un pays à faible capital par tête a un "
      "rendement du capital plus élevé, donc il accumule et rattrape plus "
      "vite. Mais chaque économie converge vers son propre état "
      "stationnaire, déterminé par son taux d’épargne, sa démographie et sa "
      "technologie. Deux pays aux paramètres différents convergent donc vers "
      "des niveaux différents : la convergence est conditionnelle, non "
      "absolue.",
  diss="Cette précision permet de répondre finement à un sujet sur le "
       "rattrapage : Solow prédit un rattrapage, mais pas l’égalisation des "
       "niveaux de vie."),

f(id='q6-n78', sp='c6-13', niv='comprendre', type='qcm', b=2382,
  q="Quel rôle Solow assigne-t-il à l’État dans la croissance de long terme ?",
  opts=["Un rôle central : seule l’intervention publique permet la croissance",
        "Un rôle non structurel : la croissance de long terme n’en dépend "
        "pas, les mécanismes de marché assurant la coordination",
        "Un rôle limité à la redistribution des revenus",
        "Un rôle de financement de la R&D"],
  ans=1,
  why=["C’est la position des modèles endogènes, non celle de Solow.",
       "La redistribution n’est pas traitée dans ce modèle.",
       "Le financement de la R&D est l’argument de Romer et d’Aghion, qui "
       "naît précisément du caractère exogène du progrès technique chez "
       "Solow."],
  exp="La vision est auto-équilibrante : puisque les prix s’ajustent et que "
      "l’économie converge d’elle-même vers un sentier stable, la croissance "
      "de long terme ne dépend pas structurellement de l’État. C’est "
      "exactement ce que Lucas, Barro, Romer et Aghion renverseront, en "
      "montrant que les externalités positives engendrent un "
      "sous-investissement privé.",
  diss="Le rôle de l’État est la troisième des trois questions que le cours "
       "assigne aux théories de la croissance : suivre son évolution d’un "
       "modèle à l’autre est un fil directeur très solide."),

f(id='q6-n79', sp='c6-13', niv='comprendre', type='qcm', b=2414,
  q="En quoi Lucas (1988) rompt-il avec Solow ?",
  opts=["Il remplace le capital physique par le capital public",
        "Il affirme que la productivité marginale de la formation est "
        "constante voire croissante, de sorte que l’état stationnaire n’est "
        "plus une fatalité",
        "Il abandonne l’hypothèse de rendements d’échelle constants",
        "Il nie l’existence du progrès technique"],
  ans=1,
  why=["Le capital public est le facteur retenu par Barro.",
       "La rupture ne porte pas sur les rendements d’échelle mais sur les "
       "rendements du facteur accumulé.",
       "Lucas ne nie pas le progrès technique : il l’explique par "
       "l’accumulation du capital humain."],
  exp="Chez Solow, le capital physique subit des rendements décroissants et "
      "l’économie converge vers un état stationnaire où la croissance par "
      "tête s’éteint. Lucas objecte que le capital humain ne s’use pas comme "
      "une machine, que la productivité marginale de la formation ne décroît "
      "pas nécessairement et qu’il génère des externalités positives. La "
      "croissance peut donc être durable, cumulative et auto-entretenue.",
  diss="La formule la plus efficace : chez Solow la croissance s’éteint faute "
       "de moteur interne ; chez Lucas, le moteur est à l’intérieur."),

# ------------------- c6-14 Barro, Romer, Aghion, Banerjee & Duflo
f(id='q6-n80', sp='c6-14', niv='connaitre', type='qcm', b=2477,
  q="Qu’est-ce que le capital public chez Barro (1990) ?",
  opts=["L’ensemble des actifs détenus par l’État",
        "L’ensemble des dépenses publiques productives qui améliorent la "
        "productivité du secteur privé : infrastructures, éducation, R&D",
        "Le budget d’investissement des collectivités locales",
        "La dette publique accumulée"],
  ans=1,
  why=["Le patrimoine de l’État est une notion comptable, non le facteur de "
       "production que Barro modélise.",
       "Le budget local n’est qu’une partie des dépenses visées.",
       "La dette est un mode de financement, non un capital productif."],
  exp="L’originalité de Barro est d’intégrer explicitement ces dépenses dans "
      "la fonction de production : le capital public améliore l’efficacité du "
      "capital privé et accroît la productivité globale. Une route profite à "
      "toutes les entreprises, une population mieux formée élève la "
      "productivité collective, la recherche publique bénéficie à l’ensemble "
      "de l’économie : le rendement social dépasse le rendement privé.",
  diss="Le cours relève le paradoxe intéressant : ces auteurs sont libéraux "
       "et réhabilitent pourtant l’État — non dans une optique "
       "conjoncturelle, mais structurelle."),

f(id='q6-n81', sp='c6-14', niv='raisonner', type='qcm', b=2507,
  q="Quelle condition d’efficacité Barro assigne-t-il au capital public ?",
  opts=["Les dépenses publiques doivent être les plus élevées possible",
        "Il existe un niveau optimal de capital public : la croissance dépend "
        "de la qualité des dépenses et de leur orientation vers des "
        "investissements productifs",
        "Le capital public doit être financé par l’emprunt",
        "Le capital public doit se limiter aux infrastructures de transport"],
  ans=1,
  why=["Le modèle n’implique aucune maximisation des dépenses : au-delà d’un "
       "seuil, elles pèsent sur l’économie.",
       "Le mode de financement n’est pas la condition retenue.",
       "Les trois exemples du cours incluent l’éducation et la R&D, pas "
       "seulement les transports."],
  exp="L’intervention publique doit être mesurée : c’est la composition des "
      "dépenses, et non leur volume, qui détermine leur effet sur la "
      "croissance. Cette nuance distingue Barro d’une justification "
      "inconditionnelle de la dépense publique.",
  diss="Argument précieux pour nuancer un sujet sur l’investissement public : "
       "la question n’est pas « plus ou moins d’État » mais « quelles "
       "dépenses »."),

f(id='q6-n82', sp='c6-14', niv='comprendre', type='qcm', b=2534,
  q="Quelle propriété de la connaissance fonde le modèle de Romer ?",
  opts=["Sa rareté, qui permet de la vendre cher",
        "Sa non-rivalité : elle ne s’use pas et peut être utilisée "
        "simultanément par plusieurs agents",
        "Son caractère excluable grâce aux brevets",
        "Sa dépréciation rapide"],
  ans=1,
  why=["La connaissance n’est pas rare au sens économique : son usage par "
       "l’un n’empêche pas celui de l’autre.",
       "Le brevet rend la connaissance partiellement excluable, mais c’est un "
       "dispositif juridique, pas la propriété économique fondatrice du "
       "modèle.",
       "C’est l’inverse : la connaissance ne s’use pas."],
  exp="Contrairement au capital physique, la connaissance ne se déprécie pas, "
      "peut servir à plusieurs agents en même temps et se diffuse. Cette "
      "non-rivalité change la logique des rendements : plus il y a de "
      "connaissances, plus il est facile d’innover. Les idées engendrent donc "
      "des rendements croissants, et la croissance devient auto-entretenue.",
  diss="Le lien avec le chapitre sur les défaillances du marché est direct : "
       "la connaissance se comporte comme un bien collectif, d’où un "
       "sous-investissement privé."),

f(id='q6-n83', sp='c6-14', niv='raisonner', type='qcm', b=2549,
  q="Qu’appelle-t-on spillovers chez Romer, et quelle conséquence en "
    "tire-t-il ?",
  opts=["Les débordements budgétaires de la recherche publique ; il faut les "
        "limiter",
        "Les externalités positives des connaissances : le rendement social "
        "dépasse le rendement privé, donc le marché seul investit "
        "insuffisamment en R&D",
        "La fuite des cerveaux vers l’étranger ; il faut retenir les "
        "chercheurs",
        "La diffusion des brevets à l’expiration de leur protection ; il faut "
        "en allonger la durée"],
  ans=1,
  why=["Le terme ne désigne pas un dépassement de budget.",
       "La fuite des cerveaux est une autre question, absente ici.",
       "L’expiration des brevets n’est pas le mécanisme visé."],
  exp="Une innovation bénéficie à son auteur, mais aussi à toute l’économie : "
      "les idées se diffusent, les chercheurs s’inspirent des découvertes "
      "existantes, les innovations en stimulent d’autres. Comme l’entreprise "
      "ne capte pas l’ensemble des bénéfices sociaux, elle investit moins que "
      "l’optimum. D’où une intervention structurelle de l’État : financer la "
      "recherche publique, subventionner la R&D, protéger la propriété "
      "intellectuelle, soutenir l’enseignement supérieur.",
  diss="Le même raisonnement — rendement social supérieur au rendement privé "
       "— se retrouve chez Lucas et chez Barro : c’est la matrice commune des "
       "trois modèles endogènes."),

f(id='q6-n84', sp='c6-14', niv='comprendre', type='qcm', b=2661,
  q="Quel est, pour Banerjee et Duflo, le véritable problème du développement ?",
  opts=["Le manque de capital disponible",
        "La mauvaise allocation des ressources : le capital, les talents et "
        "les entrepreneurs existent, mais sont mal utilisés",
        "L’absence d’ouverture commerciale",
        "La faiblesse de l’épargne nationale"],
  ans=1,
  why=["C’est précisément la thèse qu’ils récusent : on peut accumuler du "
       "capital sans développer l’économie.",
       "L’ouverture commerciale n’est pas leur variable centrale.",
       "L’épargne est au cœur de Harrod-Domar et de Solow, pas de leur "
       "analyse."],
  exp="Deux mauvaises allocations sont distinguées. Celle du capital "
      "matériel : les entreprises productives n’obtiennent pas les "
      "financements, les moins productives survivent par relations ou "
      "favoritisme. Celle du capital humain : talents non repérés, formation "
      "inadéquate, entrepreneurs choisis pour des raisons familiales ou "
      "sociales plutôt que pour leur compétence. C’est un gaspillage "
      "économique.",
  diss="Leur conclusion ouvre sur la partie institutionnelle : si les "
       "ressources sont mal allouées, c’est que les règles du jeu — droits de "
       "propriété, sécurité juridique, structure du pouvoir — sont en cause."),

f(id='q6-n85', sp='c6-14', niv='comprendre', type='qcmm', b=2684,
  q="Quelles structures expliquent, selon Banerjee et Duflo, la mauvaise "
    "allocation du capital ? (plusieurs réponses)",
  opts=["La domination des banques et la faiblesse des marchés financiers",
        "Des entreprises trop petites, qui n’accèdent pas au financement ni "
        "aux économies d’échelle",
        "Un capitalisme familial où le dirigeant est choisi pour son statut "
        "plutôt que pour sa compétence",
        "Un excès de capital-risque",
        "Une fiscalité trop progressive"],
  ans=[0, 1, 2],
  why=["Exacte : les banques favorisent les grandes entreprises, les PME "
       "innovantes accèdent peu au crédit, le risque est mal diversifié.",
       "Exacte : une économie de microentreprises peine à décoller.",
       "Exacte : le problème n’est pas l’héritage en soi, mais l’absence de "
       "sélection par la compétence.",
       "Le cours déplore au contraire le manque de capital-risque.",
       "La fiscalité n’est pas invoquée dans cette analyse."],
  exp="Ces trois structures convergent vers le même effet : les projets "
      "innovants sont sous-financés et la productivité stagne. D’où leur "
      "plaidoyer pour une croissance inclusive — qui profite au plus grand "
      "nombre, n’est pas captée par une élite, réduit les inégalités et "
      "utilise mieux les talents disponibles."),

# ----------------------- c6-15 institutions, développement durable
f(id='q6-n86', sp='c6-15', niv='comprendre', type='assoc', b=2796,
  q="Associez chaque type d’institutions, chez Acemoglu et Robinson, à ses "
    "caractéristiques et à ses effets.",
  ans=[["Institutions inclusives — caractéristiques", "Droits de propriété protégés, État de droit, pluralisme, contre-pouvoirs"],
       ["Institutions inclusives — effets", "Investissement, innovation, destruction créatrice, croissance durable"],
       ["Institutions extractives — caractéristiques", "Concentration du pouvoir, captation par une élite, insécurité juridique"],
       ["Institutions extractives — effets", "Sous-investissement, protection des rentes, stagnation de long terme"]],
  exp="Le mécanisme se résume en deux chaînes : institutions inclusives → "
      "confiance → investissement → innovation → croissance durable ; "
      "institutions extractives → rente → blocage → stagnation. Le cours "
      "ajoute aussitôt les débats : le cas chinois, qui combine "
      "centralisation politique et quarante ans de croissance rapide, et la "
      "double causalité — les institutions favorisent la croissance, mais la "
      "croissance permet aussi de créer de nouvelles institutions.",
  diss="Toujours mentionner le cas chinois : Acemoglu et Robinson répondent "
       "qu’une croissance est possible à court et moyen terme sans "
       "institutions inclusives, mais qu’elle serait instable à long terme — "
       "et que la question reste ouverte."),

f(id='q6-n87', sp='c6-15', niv='appliquer', type='qcm', b=2789,
  q="Quels chiffres le cours retient-il pour illustrer l’effet "
    "institutionnel de la Glorieuse Révolution anglaise ?",
  opts=["La part britannique dans la production industrielle mondiale passe "
        "de 2 % en 1750 à 23 % en 1880",
        "Le PIB britannique double entre 1688 et 1750",
        "La population anglaise triple au XVIIIᵉ siècle",
        "Le taux d’investissement atteint 10 % du PIB dès 1688"],
  ans=0,
  why=["Le cours ne donne pas ce repère.",
       "La démographie n’est pas l’indicateur retenu ici.",
       "Le seuil de 10 % du PIB est le repère du take-off chez Rostow, pas "
       "celui de la Glorieuse Révolution."],
  exp="Après 1688, la limitation du pouvoir royal, le renforcement du "
      "Parlement et l’instauration d’un État de droit protègent les droits de "
      "propriété, favorisent les brevets, nourrissent la confiance des "
      "investisseurs et l’essor du crédit. Le cours conclut que l’explication "
      "de la Révolution industrielle n’est pas seulement géographique ou "
      "liée au charbon : elle est institutionnelle.",
  diss="Ce chiffre est le plus parlant pour défendre une thèse "
       "institutionnaliste : un changement de règles précède un décollage "
       "industriel sans équivalent."),

f(id='q6-n88', sp='c6-15', niv='raisonner', type='qcm', b=2847,
  q="Qu’appelle-t-on la « double causalité » dans le débat sur les "
    "institutions ?",
  opts=["Le fait que deux institutions puissent avoir le même effet",
        "Le fait que les institutions favorisent la croissance, mais que la "
        "croissance permette aussi de créer de nouvelles institutions",
        "Le fait que les institutions agissent à la fois sur l’offre et sur "
        "la demande",
        "Le fait que les institutions produisent des effets opposés selon les "
        "pays"],
  ans=1,
  why=["Il ne s’agit pas d’une équivalence entre institutions.",
       "L’opposition offre / demande relève du débat sur la stagnation "
       "séculaire.",
       "La variabilité des effets selon les pays est une autre objection, "
       "illustrée par le cas chinois."],
  exp="Le cours cite l’État-providence, les prud’hommes, l’autorité de la "
      "concurrence et la régulation financière : autant d’institutions "
      "rendues possibles par la richesse déjà acquise. La relation est donc "
      "potentiellement circulaire, ce qui complique l’identification d’un "
      "sens de causalité unique.",
  diss="Soulever la double causalité évite de présenter l’explication "
       "institutionnaliste comme une démonstration achevée : c’est la nuance "
       "qui distingue une bonne copie."),

f(id='q6-n89', sp='c6-15', niv='connaitre', type='qcm', b=2864,
  q="Quelles deux étapes le cours retient-il dans l’émergence du "
    "développement durable ?",
  opts=["Le rapport Brundtland (1987) puis l’Accord de Paris (2015)",
        "Le rapport du Club de Rome « Limits to Growth » (1972) puis le "
        "rapport Brundtland (1987)",
        "La conférence de Rio (1992) puis le protocole de Kyoto (1997)",
        "Le rapport Meadows (1972) puis le Green Deal (2019)"],
  ans=1,
  why=["L’Accord de Paris n’est pas l’étape retenue par ce passage du cours.",
       "Rio et Kyoto ne sont pas mentionnés ici.",
       "Le Green Deal intervient bien plus loin, dans la partie sur les "
       "politiques publiques."],
  exp="Le Club de Rome met en garde en 1972 contre l’épuisement des "
      "ressources et introduit l’idée de limites physiques à la croissance. "
      "Le rapport Brundtland donne en 1987 la définition centrale — répondre "
      "aux besoins du présent sans compromettre la capacité des générations "
      "futures à répondre aux leurs — et fait apparaître la notion de "
      "responsabilité intergénérationnelle."),

f(id='q6-n90', sp='c6-15', niv='connaitre', type='qcmm', b=2865,
  q="Sur quels piliers repose le développement durable ? (plusieurs réponses)",
  opts=["Un pilier économique : croissance, emploi, innovation, productivité",
        "Un pilier social : réduction des inégalités, lutte contre la "
        "pauvreté, inclusion",
        "Un pilier environnemental : préservation des ressources, réduction "
        "des émissions, protection des écosystèmes",
        "Un pilier monétaire : stabilité des prix",
        "Un pilier démographique : maîtrise de la natalité"],
  ans=[0, 1, 2],
  why=["Exacte : le développement durable ne supprime pas la croissance.",
       "Exacte : c’est ce que le cours appelle la croissance inclusive.",
       "Exacte : l’objectif est de découpler croissance et destruction "
       "écologique.",
       "La stabilité des prix n’est pas un pilier du développement durable.",
       "La démographie n’en fait pas partie dans cette présentation."],
  exp="Le cours met explicitement en garde : il ne faut pas réduire le "
      "développement durable à l’environnement. C’est l’articulation des "
      "trois piliers qui définit la notion, et c’est aussi ce qui en rend la "
      "mise en œuvre conflictuelle, chaque pilier pouvant contrarier les "
      "autres à court terme."),

f(id='q6-n91', sp='c6-15', niv='connaitre', type='qcm', b=2881,
  q="Quelles dimensions l’IDH combine-t-il ?",
  opts=["Le revenu, l’emploi et le logement",
        "Le revenu, la santé mesurée par l’espérance de vie, et l’éducation",
        "Le revenu, les inégalités et les émissions de CO₂",
        "La santé, l’éducation et la protection sociale"],
  ans=1,
  why=["L’emploi et le logement ne figurent pas dans l’indice.",
       "Ni les inégalités ni les émissions n’entrent dans l’IDH.",
       "Le revenu est l’une des trois dimensions : l’omettre est une erreur "
       "fréquente."],
  exp="L’IDH est l’indicateur que le cours oppose au PIB : la croissance est "
      "une mesure quantitative, qui renseigne sur l’augmentation des "
      "richesses produites mais ne dit pas à elle seule si la population vit "
      "mieux. L’IDH introduit les dimensions qualitatives du développement.",
  diss="Mobiliser l’IDH permet d’illustrer concrètement la distinction "
       "croissance / développement, au lieu de la laisser abstraite."),

# -------------------- c6-16 formes de capital et soutenabilité
f(id='q6-n92', sp='c6-16', niv='connaitre', type='qcm', b=2887,
  q="Comment le cours définit-il le capital, pour pouvoir en élargir la "
    "notion ?",
  opts=["Toute richesse détenue par un agent économique",
        "Un stock d’actifs mobilisables dans le processus productif et "
        "capables de générer des revenus futurs",
        "L’ensemble des machines et bâtiments d’une économie",
        "L’épargne accumulée par les ménages"],
  ans=1,
  why=["Toute richesse n’est pas du capital : le cours précise qu’il s’agit "
       "d’une richesse utile à la production.",
       "Machines et bâtiments constituent le seul capital physique.",
       "L’épargne est une ressource de financement, non un stock productif."],
  exp="Cette définition permet d’élargir la notion au-delà du capital "
      "physique : capital humain, naturel, technologique, social, "
      "institutionnel. Le cours ajoute une précision utile sur le capital "
      "humain : une compétence n’en relève que si elle est valorisable "
      "économiquement.",
  diss="C’est cet élargissement qui rend possible la question de la "
       "soutenabilité : peut-on préserver la capacité de croissance sans "
       "détruire certains capitaux, notamment le capital naturel ?"),

f(id='q6-n93', sp='c6-16', niv='connaitre', type='assoc', b=2890,
  q="Associez chaque forme de capital à son contenu.",
  ans=[["Capital physique", "Machines, bâtiments, équipements, infrastructures"],
       ["Capital humain", "Compétences, formation, éducation, qualifications, savoir-faire"],
       ["Capital naturel", "Ressources énergétiques, minerais, forêts, eau, biodiversité, écosystèmes"],
       ["Capital technologique", "Brevets, innovations, connaissances scientifiques, résultats de la R&D"],
       ["Capital social", "Réseaux, réputation, relations, confiance"],
       ["Capital institutionnel", "Règles, lois, droits de propriété, stabilité politique, qualité de la justice"]],
  exp="Cette typologie récapitule tout le chapitre : chaque forme de capital "
      "correspond à un modèle étudié — capital physique chez Solow, humain "
      "chez Lucas, technologique chez Romer, public et institutionnel chez "
      "Barro, North et Acemoglu. La croissance n’est donc pas seulement une "
      "accumulation de machines, mais repose sur un ensemble de ressources "
      "complémentaires.",
  diss="Excellente grille de plan pour un sujet large sur les facteurs de la "
       "croissance : six formes de capital, six familles d’auteurs."),

f(id='q6-n94', sp='c6-16', niv='comprendre', type='qcm', b=2968,
  q="Qu’est-ce que la soutenabilité faible ?",
  opts=["L’idée que la croissance doit être ralentie pour préserver "
        "l’environnement",
        "L’idée, d’inspiration néoclassique, que les formes de capital sont "
        "globalement substituables : une baisse du capital naturel peut être "
        "compensée par plus de capital technologique",
        "L’idée que la soutenabilité ne concerne que les pays développés",
        "L’idée que le capital naturel est irremplaçable"],
  ans=1,
  why=["Le ralentissement de la croissance est au contraire la conclusion "
       "possible de la soutenabilité forte.",
       "La soutenabilité ne se limite à aucun groupe de pays.",
       "L’irremplaçabilité du capital naturel définit la soutenabilité "
       "forte, l’exact opposé."],
  exp="Dans cette vision, le progrès technique permet de compenser les "
      "contraintes environnementales : réduire l’intensité énergétique, "
      "améliorer l’efficacité, produire autant avec moins de ressources, "
      "trouver des substituts, dépolluer, innover « vert ». La croissance "
      "n’est alors pas le problème : elle peut même devenir la solution. "
      "C’est le socle théorique de la croissance verte.",
  diss="Toute la question tient dans un mot : les capitaux sont-ils "
       "substituables ? La réponse détermine la position que l’on défend."),

f(id='q6-n95', sp='c6-16', niv='raisonner', type='qcm', b=2992,
  q="Sur quoi repose la soutenabilité forte, et quelles conséquences en "
    "tire-t-elle ?",
  opts=["Sur l’idée que le capital naturel n’est pas substituable : il faut "
        "limiter l’extraction, réduire la consommation matérielle et changer "
        "les modes de production et de consommation",
        "Sur l’idée que la croissance doit être financée autrement",
        "Sur l’idée que seuls les pays riches doivent réduire leurs émissions",
        "Sur l’idée que le marché corrigera spontanément les externalités"],
  ans=0,
  why=["Le mode de financement n’est pas en cause.",
       "La répartition de l’effort entre pays est une autre question.",
       "C’est l’inverse d’une position écologique critique."],
  exp="Certaines ressources ou équilibres écologiques sont limités, "
      "irremplaçables, non reproductibles, parfois irréversiblement détruits : "
      "on ne remplace pas une espèce disparue, un climat déréglé, une forêt "
      "primaire ou un stock minier épuisé. Le progrès technique ne suffit donc "
      "pas. Cette approche remet en cause le productivisme et la logique "
      "d’accumulation infinie, certaines versions radicales défendant la "
      "décroissance.",
  diss="Opposer les deux soutenabilités est la meilleure structure pour un "
       "sujet « la croissance durable est-elle possible ? » : pour l’une, "
       "c’est un programme ; pour l’autre, une contradiction dans les termes."),

f(id='q6-n96', sp='c6-16', niv='raisonner', type='qcmm', b=3056,
  q="Quelles limites le cours oppose-t-il à la courbe environnementale de "
    "Kuznets ? (plusieurs réponses)",
  opts=["Elle ne vaut pas pour toutes les pollutions : elle fonctionne mal "
        "pour le CO₂, les déchets et la biodiversité",
        "Un pays riche peut sembler moins polluer en important des biens "
        "produits ailleurs : la pollution est externalisée",
        "Certaines destructions sont irréversibles et le climat fonctionne "
        "par seuils",
        "Le temps écologique n’est pas le temps économique",
        "Elle n’a jamais été vérifiée pour aucun indicateur"],
  ans=[0, 1, 2, 3],
  why=["Exacte : or ce sont les pollutions les plus décisives aujourd’hui.",
       "Exacte : la baisse de la pollution nationale ne signifie pas une "
       "baisse de l’empreinte réelle.",
       "Exacte : d’où l’impossibilité d’un « rattrapage tardif ».",
       "Exacte : on ne peut pas polluer d’abord et réparer plus tard.",
       "Le profil en U inversé se vérifie pour certaines pollutions locales, "
       "comme le dioxyde de soufre."],
  exp="Le cours conclut que la courbe est utile comme outil de réflexion mais "
      "ne doit surtout pas être prise pour une loi générale : la simple "
      "croissance ne suffit pas à garantir une trajectoire soutenable. C’est "
      "ce constat qui conduit à envisager une transformation des modes de "
      "production — l’économie circulaire."),

# ------------- c6-17 économie circulaire, efficacité, sobriété, Green Deal
f(id='q6-n97', sp='c6-17', niv='comprendre', type='qcm', b=3110,
  q="Qu’oppose l’économie circulaire au modèle linéaire ?",
  opts=["Elle remplace la production industrielle par des services",
        "Elle cherche à boucler les cycles : réduire les déchets, réutiliser, "
        "recycler, allonger la durée de vie des produits, limiter "
        "l’extraction",
        "Elle vise uniquement le recyclage des déchets ménagers",
        "Elle interdit l’extraction de ressources nouvelles"],
  ans=1,
  why=["Il ne s’agit pas de substituer les services à l’industrie.",
       "Le recyclage n’est qu’un des piliers, parmi l’éco-conception, le "
       "réemploi ou l’économie de la fonctionnalité.",
       "L’économie circulaire limite l’extraction, elle ne l’interdit pas."],
  exp="Le modèle linéaire repose sur l’abondance supposée des ressources et "
      "l’acceptation implicite des déchets : il est très consommateur de "
      "ressources et peu soutenable. L’économie circulaire fait passer d’une "
      "logique de flux jetables à une logique de boucles. Le cours énumère "
      "ses piliers : approvisionnement durable, éco-conception, économie de "
      "la fonctionnalité, consommation responsable, allongement de la durée "
      "d’usage, réemploi, recyclage, écologie industrielle et territoriale.",
  diss="Ne pas la présenter comme une solution miracle : le recyclage a un "
       "coût, tous les matériaux ne sont pas recyclables à l’infini, il y a "
       "des pertes de matière et il faut de l’énergie pour recycler."),

f(id='q6-n98', sp='c6-17', niv='comprendre', type='qcm', b=3143,
  q="Quelle différence sépare l’efficacité énergétique de la sobriété "
    "énergétique ?",
  opts=["L’efficacité concerne l’industrie, la sobriété les ménages",
        "L’efficacité consiste à produire la même chose avec moins d’énergie, "
        "par amélioration technique ; la sobriété consiste à réduire la "
        "consommation en modifiant les comportements et les usages",
        "L’efficacité est une politique publique, la sobriété une "
        "contrainte réglementaire",
        "Les deux notions sont équivalentes"],
  ans=1,
  why=["La distinction ne porte pas sur le type d’agent concerné.",
       "Ni l’une ni l’autre ne se réduit à un instrument juridique.",
       "Le cours en fait au contraire une distinction décisive."],
  exp="L’efficacité relève d’une logique technologique : moteurs plus "
      "efficaces, bâtiments mieux isolés, appareils moins énergivores, "
      "procédés industriels plus performants. La sobriété relève d’une "
      "logique comportementale, sociale et politique : moins se déplacer, "
      "privilégier les transports collectifs, réduire la taille des "
      "véhicules, baisser le chauffage, mutualiser les équipements. "
      "L’efficacité réduit l’intensité énergétique ; la sobriété interroge le "
      "volume même des usages.",
  diss="Cette opposition structure deux visions de la transition : on garde "
       "le même modèle en l’améliorant techniquement, ou on modifie les "
       "usages et on accepte certaines limites."),

f(id='q6-n99', sp='c6-17', niv='raisonner', type='qcm', b=3185,
  q="Qu’est-ce que l’effet rebond, aussi appelé effet Jevons ?",
  opts=["Le fait qu’une innovation provoque une hausse temporaire des prix",
        "Le fait que les gains d’efficacité soient partiellement, voire "
        "totalement, annulés par une hausse des usages",
        "Le fait que la pollution se déplace vers les pays moins régulés",
        "Le fait qu’une politique écologique provoque des résistances "
        "sociales"],
  ans=1,
  why=["La hausse temporaire des prix relève du brevet et du monopole "
       "d’innovation.",
       "Le déplacement de la pollution est l’externalisation, une critique "
       "distincte de la courbe de Kuznets environnementale.",
       "Les résistances sociales sont un autre problème, abordé à propos du "
       "Green Deal."],
  exp="L’exemple du cours est limpide : une voiture consomme moins, donc son "
      "usage coûte moins cher, donc on roule davantage. La baisse de la "
      "consommation unitaire est réelle, mais la consommation totale baisse "
      "moins que prévu, voire pas du tout. L’efficacité ne garantit donc pas "
      "automatiquement une baisse absolue des consommations.",
  diss="Argument décisif en faveur de la sobriété : sans action sur les "
       "usages, le progrès technique seul peut ne rien réduire."),

f(id='q6-n100', sp='c6-17', niv='connaitre', type='qcm', b=3243,
  q="Quels objectifs chiffrés le Green Deal européen fixe-t-il ?",
  opts=["Réduire les émissions de 40 % d’ici 2030 par rapport à 2005, et de "
        "80 % en 2050",
        "Réduire de 55 % les émissions de gaz à effet de serre d’ici 2030 par "
        "rapport à 1990, et atteindre la neutralité carbone en 2050",
        "Atteindre la neutralité carbone dès 2030",
        "Réduire de 55 % la consommation d’énergie d’ici 2050"],
  ans=1,
  why=["Ni le pourcentage ni l’année de référence ne correspondent.",
       "La neutralité carbone est l’objectif de 2050, non de 2030.",
       "L’objectif porte sur les émissions de gaz à effet de serre, non sur "
       "la consommation d’énergie."],
  exp="L’année 1990 sert de point de référence historique commun et de base "
      "statistique retenue au niveau européen. La neutralité carbone en 2050 "
      "signifie que des émissions résiduelles peuvent subsister, à condition "
      "d’être compensées par des capacités d’absorption. Annoncé en 2019, le "
      "Pacte vert ne vise ni l’arrêt de la croissance, ni la décroissance, ni "
      "la désindustrialisation, mais la transformation de la production pour "
      "continuer à croître autrement.",
  diss="Souligner cette logique de croissance verte permet de situer le Green "
       "Deal du côté de la soutenabilité faible."),

f(id='q6-n101', sp='c6-17', niv='comprendre', type='qcm', b=3264,
  q="Pourquoi la rénovation thermique des bâtiments est-elle un levier "
    "privilégié du Green Deal ?",
  opts=["Parce qu’elle ne coûte rien aux finances publiques",
        "Parce qu’elle combine un intérêt écologique — moins de consommation "
        "et d’émissions — et un intérêt économique et social : factures "
        "allégées et emplois créés dans le bâtiment",
        "Parce qu’elle concerne surtout les bâtiments publics",
        "Parce qu’elle ne nécessite aucune compétence nouvelle"],
  ans=1,
  why=["Elle suppose au contraire des financements publics importants.",
       "Elle concerne l’ensemble du parc immobilier.",
       "Elle crée précisément des besoins de compétences en isolation et en "
       "ingénierie thermique."],
  exp="Les bâtiments mal isolés consomment beaucoup d’énergie et pèsent "
      "lourd dans la consommation énergétique. Mieux les isoler réduit la "
      "consommation, les émissions et les factures, tout en créant des "
      "emplois dans le bâtiment, l’isolation, la rénovation et l’ingénierie "
      "thermique. Le cours en fait « un très bon exemple de croissance verte "
      "créatrice d’emplois ».",
  diss="Exemple à mobiliser pour montrer qu’écologie et emploi ne sont pas "
       "nécessairement antagonistes — ce qui est exactement le pari du Green "
       "Deal."),

f(id='q6-n102', sp='c6-17', niv='raisonner', type='courte', b=3316,
  q="Quel problème social la transition écologique soulève-t-elle, et quelle "
    "réponse le Green Deal y apporte-t-il ?",
  ans={'modele': "Transformer les systèmes productifs fait reculer certaines "
       "activités et monte en puissance d’autres secteurs : certains métiers "
       "deviennent fragiles, d’autres sont créés. Si l’on réduit la voiture "
       "thermique, que deviennent les salariés formés pour cette industrie ? "
       "La transition pose donc la question de la reconversion, des "
       "compétences, du risque de chômage sectoriel et des coûts sociaux du "
       "changement. La réponse du Green Deal est que la transition n’est pas "
       "censée détruire l’emploi en net, mais le déplacer : des emplois "
       "apparaissent dans la rénovation thermique, les énergies "
       "renouvelables, les infrastructures vertes, la mobilité propre et "
       "l’ingénierie environnementale.",
       'cles': [{'f': ['recul', 'secteur', 'metier', 'detruit'],
                 'l': 'certaines activités reculent, certains métiers sont fragilisés'},
                {'f': ['reconversion', 'competence', 'formation'],
                 'l': 'd’où un enjeu de reconversion et de compétences'},
                {'f': ['deplace', 'net', 'structure'],
                 'l': 'la transition déplace l’emploi plutôt qu’elle ne le détruit en net'},
                {'f': ['renovation', 'renouvelable', 'vert', 'mobilite'],
                 'l': 'des emplois apparaissent dans les secteurs verts'}]},
  exp="Le cours relie ce point à Aghion : la destruction créatrice orientée "
      "vers la transition écologique produit des perdants à court terme, "
      "d’où la nécessité d’un accompagnement et d’un rôle structurel de "
      "l’État. Une politique écologique n’est politiquement soutenable que si "
      "elle traite les coûts sociaux de la transformation."),

# ------------- c6-18 financer, contraindre, critiquer la transition
f(id='q6-n103', sp='c6-18', niv='connaitre', type='qcm', b=3356,
  q="Qu’est-ce que Next Generation EU ?",
  opts=["Un programme européen de recherche doté de 100 milliards d’euros",
        "Un plan de 750 milliards d’euros mis en place en 2020, finançant "
        "notamment la transition écologique, la transformation numérique et "
        "la cohésion économique et sociale",
        "Le nom du marché européen des quotas d’émission",
        "Le volet social du Green Deal, adopté en 2019"],
  ans=1,
  why=["Ni le montant ni l’objet ne correspondent.",
       "Le marché des quotas est un instrument distinct.",
       "Le Green Deal est la stratégie ; Next Generation EU en est l’un des "
       "financements."],
  exp="La transition écologique ne peut pas reposer uniquement sur des "
      "interdictions, des injonctions ou des objectifs symboliques : elle "
      "suppose un financement massif. C’est le sens de ce plan de 2020 : la "
      "transition est aussi une politique d’investissement.",
  diss="Associer un objectif chiffré (−55 % en 2030) et un financement "
       "(750 milliards) rend un développement sur les politiques européennes "
       "beaucoup plus solide."),

f(id='q6-n104', sp='c6-18', niv='comprendre', type='qcm', b=3376,
  q="Quel est l’objet de la CSRD ?",
  opts=["Taxer les entreprises les plus émettrices",
        "Obliger les entreprises à publier des informations sur la "
        "durabilité de leur système productif, leurs impacts "
        "environnementaux et leurs pratiques sociales",
        "Interdire la vente de véhicules thermiques",
        "Subventionner la rénovation thermique"],
  ans=1,
  why=["La CSRD n’est pas un instrument fiscal.",
       "L’interdiction des véhicules thermiques est un autre dispositif, "
       "visant 2035.",
       "Les subventions relèvent des plans d’investissement."],
  exp="L’objectif est la transparence, la comparabilité, l’évitement du "
      "greenwashing et une pression réglementaire et réputationnelle : on ne "
      "veut plus seulement des promesses « vertes », mais des indicateurs "
      "mesurables. Le cours relève ensuite deux reculs : un report "
      "d’application de deux ans, et un relèvement des seuils — de 250 à "
      "1 000 salariés, de 50 à 550 millions d’euros de chiffre d’affaires — "
      "qui sortirait 50 à 80 % des entreprises du champ.",
  diss="Ces reculs illustrent la thèse du cours : « l’écologie devient "
       "conflictuelle quand elle cesse d’être un discours et devient une "
       "contrainte juridique et économique »."),

f(id='q6-n105', sp='c6-18', niv='comprendre', type='qcm', b=3419,
  q="En quoi le devoir de vigilance va-t-il plus loin que la CSRD ?",
  opts=["Il impose une taxe carbone aux fournisseurs",
        "Il fait passer d’une logique d’information à une logique de "
        "responsabilité : l’entreprise doit surveiller et prévenir les "
        "atteintes dans ses filiales, chez ses sous-traitants et ses "
        "fournisseurs",
        "Il s’applique à toutes les entreprises sans seuil",
        "Il remplace la CSRD"],
  ans=1,
  why=["Il ne s’agit pas d’un instrument fiscal.",
       "Il connaît les mêmes reculs de seuils que la CSRD.",
       "Les deux dispositifs se superposent, le second prolongeant le "
       "premier."],
  exp="Avant, une entreprise pouvait externaliser sa production, "
      "sous-traiter dans des pays moins réglementés, profiter de coûts plus "
      "faibles puis affirmer que ce n’était pas sa responsabilité. Le devoir "
      "de vigilance empêche cela : il vise à empêcher l’externalisation des "
      "coûts sociaux et environnementaux. L’entreprise devient responsable de "
      "sa chaîne de valeur.",
  diss="Le cours signale l’argument des opposants : la perte de "
       "compétitivité, les entreprises américaines n’étant pas soumises aux "
       "mêmes contraintes."),

f(id='q6-n106', sp='c6-18', niv='raisonner', type='qcm', b=3480,
  q="Quelle est la thèse centrale de Jean-Baptiste Fressoz dans « Sans "
    "transition » (2024) ?",
  opts=["Les énergies renouvelables sont moins efficaces que les fossiles",
        "Dans l’histoire réelle, les énergies ne se substituent pas : elles "
        "s’additionnent, elles s’empilent",
        "La transition énergétique est trop lente mais inéluctable",
        "Les États n’ont pas les moyens financiers de la transition"],
  ans=1,
  why=["Fressoz ne raisonne pas en termes d’efficacité comparée des sources "
       "d’énergie.",
       "Il conteste le récit même de la transition, non son rythme.",
       "La question du financement n’est pas son objet."],
  exp="Le récit dominant raconte l’histoire de l’énergie comme une "
      "succession de substitutions : bois vers charbon, charbon vers pétrole, "
      "pétrole vers électricité et renouvelables. Fressoz montre que ce récit "
      "est trompeur : l’essor du charbon mobilise encore du bois pour les "
      "galeries et les infrastructures, le pétrole se développe dans un monde "
      "déjà structuré par le charbon, et les renouvelables exigent "
      "aujourd’hui extraction minière, acier, béton, transport mondial et "
      "chaînes industrielles énergivores.",
  diss="Portée théorique : c’est une critique de l’optimisme technologique et, "
       "implicitement, de la soutenabilité faible — l’histoire ne confirme pas "
       "la substitution simple et linéaire sur laquelle repose le récit de la "
       "croissance verte."),

f(id='q6-n107', sp='c6-18', niv='raisonner', type='qcm', b=3551,
  q="Que montre François Jarrige à propos de la voiture électrique ?",
  opts=["Qu’elle est plus polluante que la voiture thermique sur l’ensemble "
        "de son cycle de vie",
        "Qu’elle réduit certaines émissions directes mais tend à déplacer les "
        "coûts écologiques — batteries, métaux, infrastructures, recyclage",
        "Qu’elle ne sera jamais économiquement rentable",
        "Que l’interdiction des véhicules thermiques en 2035 supprimera le "
        "parc existant"],
  ans=1,
  why=["Le cours reconnaît que la voiture électrique présente un avantage "
       "par rapport au thermique : la thèse est le déplacement du problème, "
       "non son aggravation globale.",
       "La rentabilité économique n’est pas son objet.",
       "L’objectif de 2035 porte sur la commercialisation de véhicules neufs, "
       "non sur l’interdiction des véhicules déjà fabriqués — le cours le "
       "précise explicitement."],
  exp="Le problème est déplacé plutôt que supprimé : les batteries "
      "concentrent une part importante du coût matériel et écologique, leur "
      "fabrication est énergivore, leur recyclage reste incomplet, difficile "
      "et coûteux. S’y ajoutent les infrastructures nécessaires — bornes de "
      "recharge, renforcement des réseaux, capacités de production "
      "d’électricité supplémentaires. On ne supprime pas la pollution : on "
      "transforme sa nature et on déplace les externalités dans l’espace et "
      "dans la chaîne de valeur.",
  diss="La conclusion est géopolitique : les métaux critiques sont rares, "
       "concentrés géographiquement et stratégiques, si bien que la "
       "transition redessine les rapports de puissance et crée de nouvelles "
       "dépendances industrielles."),

f(id='q6-n108', sp='c6-18', niv='comprendre', type='vf', b=3594,
  q="Selon le cours, la transition écologique crée de nouvelles dépendances "
    "industrielles plutôt qu’elle ne les supprime.",
  ans=True,
  exp="Les métaux critiques nécessaires aux batteries, aux éoliennes et aux "
      "panneaux solaires sont rares, concentrés géographiquement et "
      "stratégiques pour l’industrie. Les États cherchent donc à sécuriser "
      "leurs approvisionnements et les firmes à contrôler des chaînes de "
      "valeur entières. La transition est aussi une question de puissance : "
      "elle redessine les rapports de force au lieu d’abolir les "
      "dépendances.",
  diss="Ce constat rejoint Veltz — l’immatériel repose sur du très matériel — "
       "et Draghi — la compétitivité européenne passe par la capacité à "
       "produire les biens stratégiques."),
]

from qz06n1 import L as _M1

NEW = NEW + _M1
