# -*- coding: utf-8 -*-
"""Chapitre 6 — complément de questions « Appliquer ».

Le chapitre était riche en questions de compréhension mais pauvre en
exercices : décomposition de la croissance, lecture des indicateurs
d'inégalité, coefficient de capital et trois taux de Harrod, convergence
chez Solow. Chaque renvoi a été vérifié dans le texte du cours.
"""


def f(**kw):
    return kw


L = [

f(id='q6-m01', sp='c6-04', niv='appliquer', type='qcm', b=676,
  q="Carré, Dubois et Malinvaud mesurent une croissance annuelle moyenne de "
    "5,2 % en France entre 1951 et 1973, dont 0,5 point imputable au travail "
    "et 1,5 point au capital. Que vaut le résidu, et comment l’interpréter ?",
  opts=["Environ 3,2 points, soit près de 60 % de la croissance : c’est la "
        "productivité globale des facteurs",
        "Environ 2 points, soit l’apport du capital humain",
        "Zéro : les deux facteurs expliquent toute la croissance",
        "Environ 3,2 points, correspondant à la seule hausse de la population "
        "active"],
  ans=0,
  why=["Le capital humain n’est pas isolé dans cette décomposition : il fait "
       "partie de ce que le résidu recouvre.",
       "C’est précisément le constat inverse qui frappe les auteurs : "
       "l’essentiel échappe aux deux facteurs mesurés.",
       "La population active relève du facteur travail, déjà compté pour "
       "0,5 point."],
  exp="5,2 − 0,5 − 1,5 = 3,2 points, soit environ 60 % de la croissance "
      "française des Trente Glorieuses. Ce résidu est la productivité globale "
      "des facteurs : « ce qui ne s’explique ni par le travail, ni par le "
      "capital ». Le résultat est capital pour l’analyse : la croissance "
      "n’est pas d’abord extensive — plus de travailleurs, plus de "
      "machines — mais intensive, liée à l’efficacité de la combinaison "
      "productive.",
  diss="Le calcul en trois lignes vaut mieux qu’une affirmation : il montre "
       "que l’essentiel de la croissance tient à ce que l’on mesure le "
       "moins bien."),

f(id='q6-m02', sp='c6-04', niv='raisonner', type='vf', b=706,
  q="Vrai ou faux : la productivité globale des facteurs mesure le progrès "
    "technique. Justifiez.",
  ans=False,
  exp="Elle mesure ce qui reste une fois retirés les apports du travail et du "
      "capital — d’où son nom de résidu. Solow lui-même parlait du progrès "
      "technique comme d’une « manne tombée du ciel », « sans que l’on sache "
      "précisément d’où elle vient ». Le résidu recouvre donc le progrès "
      "technique, mais aussi la qualification de la main-d’œuvre, "
      "l’organisation, les institutions, et tout ce que la mesure n’a pas su "
      "isoler. L’appeler « progrès technique » revient à nommer une "
      "ignorance.",
  diss="Rappeler que le résidu est une mesure de notre ignorance ouvre "
       "directement sur la théorie de la croissance endogène, qui cherche "
       "précisément à l’expliquer."),

f(id='q6-m03', sp='c6-10', niv='appliquer', type='qcm', b=1776,
  q="Dans un pays, D9 vaut 48 000 € et D1 12 000 €. Que vaut le rapport "
    "interdécile et que mesure-t-il exactement ?",
  opts=["4 : les 10 % les plus riches disposent d’un revenu au moins quatre "
        "fois supérieur au seuil des 10 % les plus pauvres",
        "4 % : la part du revenu détenue par les plus riches",
        "0,25 : le coefficient de Gini correspondant",
        "36 000 € : l’écart absolu entre les deux groupes"],
  ans=0,
  why=["L’interdécile est un rapport, pas une part : il ne s’exprime pas en "
       "pourcentage.",
       "Le Gini se construit à partir de la courbe de Lorenz et porte sur "
       "toute la distribution : il ne se déduit pas de deux déciles.",
       "L’écart absolu existe, mais l’indicateur demandé est un rapport, qui "
       "permet les comparaisons entre pays et dans le temps."],
  exp="D9 / D1 = 48 000 / 12 000 = 4. L’indicateur compare deux seuils, non "
      "deux moyennes : D1 est le seuil en dessous duquel se situent les 10 % "
      "les plus pauvres, D9 celui au-dessus duquel se situent les 10 % les "
      "plus riches. Sa force est la lisibilité ; sa faiblesse, de ne rien "
      "dire de ce qui se passe entre les deux seuils ni au sommet de la "
      "distribution.",
  diss="Donner la valeur puis sa limite — l’interdécile ignore le top 1 % — "
       "est exactement ce qu’attend un correcteur sur un indicateur."),

f(id='q6-m04', sp='c6-10', niv='appliquer', type='qcm', b=1850,
  q="Dans un pays, le rapport interdécile reste stable pendant que la part "
    "du revenu captée par le 1 % le plus riche double. Quel indicateur "
    "rendra le mieux compte de cette évolution ?",
  opts=["Le coefficient de Palma, plus sensible aux transformations du "
        "sommet",
        "Le rapport interdécile, qui suffit à décrire toute la distribution",
        "Le seuil D1, qui mesure la pauvreté",
        "Aucun : une telle évolution est impossible"],
  ans=0,
  why=["C’est l’indicateur dont l’énoncé dit précisément qu’il ne bouge pas.",
       "D1 décrit le bas de la distribution, pas la concentration au sommet.",
       "Le cours signale expressément cette configuration : « le rapport "
       "interdécile peut rester stable alors que la part du top 1 % "
       "explose »."],
  exp="Le Palma rapporte la part du revenu des 10 % les plus riches à celle "
      "des 50 % les plus pauvres. Comparant des parts de revenu, et non des "
      "seuils, il réagit à ce qui se passe au sommet là où l’interdécile "
      "reste muet. Il ne remplace pas le Gini pour autant : le cours note "
      "qu’il « ne tient pas compte de toute la distribution ». Trois "
      "indicateurs, trois questions distinctes.",
  diss="Montrer qu’un indicateur stable peut masquer une transformation "
       "profonde est l’argument le plus solide en faveur du croisement des "
       "mesures."),

f(id='q6-m05', sp='c6-10', niv='raisonner', type='qcm', b=1912,
  q="Deux pays affichent le même coefficient de Gini. Que peut-on en "
    "conclure ?",
  opts=["Rien sur la forme de leurs inégalités : un même Gini peut recouvrir "
        "des structures très différentes",
        "Que leurs distributions de revenu sont identiques",
        "Que leurs rapports interdéciles sont égaux",
        "Que leur courbe de Lorenz est la droite d’équirépartition"],
  ans=0,
  why=["Le Gini résume la distribution en un seul chiffre : deux "
       "distributions différentes peuvent donner le même résumé.",
       "Rien n’impose l’égalité des interdéciles : l’un peut concentrer en "
       "haut, l’autre creuser en bas.",
       "La droite d’équirépartition correspond à un Gini nul, c’est-à-dire à "
       "l’égalité parfaite."],
  exp="Le Gini mesure l’aire entre la courbe de Lorenz et la droite "
      "d’équirépartition : c’est un indicateur synthétique, qui gagne en "
      "généralité ce qu’il perd en détail. Le cours le dit sans détour : "
      "« deux pays peuvent avoir le même Gini avec des structures très "
      "différentes ». Il ajoute un fait robuste : le Gini du patrimoine est "
      "partout plus élevé que celui du revenu.",
  diss="L’opposition entre indicateur synthétique et indicateurs de position "
       "permet de traiter sérieusement un sujet sur la mesure des "
       "inégalités, sans se contenter d’un chiffre."),

f(id='q6-m06', sp='c6-12', niv='appliquer', type='qcm', b=2146,
  q="Le coefficient de capital d’une économie vaut 3 et son taux d’épargne "
    "15 %. Que vaut le taux de croissance garanti au sens de Harrod ?",
  opts=["5 %, soit le taux d’épargne divisé par le coefficient de capital",
        "45 %, soit le produit des deux",
        "3 %, soit le coefficient de capital lui-même",
        "20 %, soit le coefficient de capital rapporté au taux d’épargne"],
  ans=0,
  why=["Multiplier les deux n’a aucun sens dimensionnel : le coefficient "
       "indique combien de capital il faut par unité produite.",
       "Le coefficient de capital n’est pas un taux de croissance : c’est un "
       "rapport technique.",
       "Le rapport est inversé : on divise l’épargne par le coefficient, non "
       "l’inverse."],
  exp="Le coefficient de capital v mesure la quantité de capital nécessaire "
      "pour produire une unité supplémentaire : v = 3 signifie « il faut "
      "3 unités de capital pour produire 1 unité de richesse ». Le taux "
      "garanti vaut s / v, soit 0,15 / 3 = 5 %. Le cours en tire la règle "
      "générale : « plus le coefficient de capital est élevé, plus la "
      "croissance nécessite d’investissement, plus l’économie est rigide ».",
  diss="Ce rapport simple rend tangible l’idée d’une croissance contrainte "
       "par l’investissement, et prépare la discussion du fil du rasoir."),

f(id='q6-m07', sp='c6-12', niv='appliquer', type='assoc', b=2178,
  q="Associez chacun des trois taux de croissance de Harrod à ce qu’il "
    "désigne.",
  ans=[["Le taux effectif", "Le taux de croissance réellement observé dans "
                            "l’économie"],
       ["Le taux garanti", "Celui qui assure l’équilibre sur le marché des "
                           "biens et services, déterminé par l’épargne et la "
                           "structure productive"],
       ["Le taux naturel", "Celui qui est compatible avec le plein emploi, "
                           "fixé par la croissance de la main-d’œuvre "
                           "disponible"]],
  exp="L’intérêt du modèle tient à ce que ces trois taux sont déterminés par "
      "des mécanismes indépendants : l’investissement réalisé pour le "
      "premier, l’épargne et la technique pour le deuxième, la démographie "
      "pour le troisième. Aucun mécanisme automatique ne les fait converger. "
      "La croissance équilibrée exige donc leur coïncidence, « extrêmement "
      "improbable » : c’est le « fil du rasoir ».",
  diss="Nommer les trois taux et dire d’où vient chacun suffit à expliquer "
       "pourquoi, chez Harrod, l’équilibre est l’exception et non la règle."),

f(id='q6-m08', sp='c6-13', niv='appliquer', type='qcm', b=2395,
  q="Un pays relève durablement son taux d’épargne. Que prévoit le modèle de "
    "Solow à long terme ?",
  opts=["Un niveau de capital par tête et un revenu par tête plus élevés, "
        "mais pas un taux de croissance de long terme durablement plus fort",
        "Une croissance définitivement plus rapide, sans limite",
        "Aucun effet, l’épargne n’entrant pas dans le modèle",
        "Un recul du revenu par tête, l’épargne réduisant la consommation"],
  ans=0,
  why=["C’est précisément ce que Solow exclut : les rendements décroissants "
       "du capital ramènent l’économie vers un état stationnaire.",
       "L’épargne est au contraire l’un des leviers que Solow identifie.",
       "Le niveau de consommation par tête peut baisser à court terme, mais "
       "le modèle conclut à un revenu par tête plus élevé à terme."],
  exp="C’est le résultat le plus contre-intuitif du modèle : l’épargne a un "
      "effet de niveau, non un effet de taux. Augmenter s permet d’atteindre "
      "un état stationnaire plus riche, donc de repousser l’échéance, mais "
      "ne modifie pas le rythme de croissance de long terme, qui dépend du "
      "progrès technique — lequel reste exogène. Le cours résume : Solow est "
      "« optimiste mais lucide ».",
  diss="La distinction effet de niveau / effet de taux est ce qui sépare "
       "Solow des théories de la croissance endogène : elle doit être posée "
       "explicitement."),

f(id='q6-m09', sp='c6-13', niv='raisonner', type='qcm', b=2320,
  q="En quoi la réponse de Solow s’oppose-t-elle au diagnostic de "
    "Harrod-Domar ?",
  opts=["Là où Harrod-Domar font de l’équilibre une exception faute de "
        "mécanisme d’ajustement, Solow rend les facteurs substituables et "
        "les prix flexibles, ce qui permet la convergence",
        "Solow nie l’existence du progrès technique",
        "Solow conserve les hypothèses de Harrod mais change les conclusions",
        "Solow montre que la croissance est encore plus instable"],
  ans=0,
  why=["Solow en fait au contraire le moteur de la croissance de long terme, "
       "tout en le laissant inexpliqué.",
       "Il change précisément les hypothèses : c’est ce qui lui permet de "
       "changer de conclusion.",
       "Sa conclusion est inverse : la croissance converge vers un équilibre "
       "stable."],
  exp="Le désaccord porte sur les hypothèses, non sur la logique. Chez "
      "Harrod-Domar, les facteurs sont complémentaires et les prix rigides : "
      "rien ne ramène l’économie vers le taux garanti. Solow suppose la "
      "substituabilité des facteurs et la flexibilité des prix, ce qui "
      "autorise l’ajustement et conduit l’économie vers un état stationnaire "
      "stable. Changer les hypothèses d’ajustement suffit à transformer "
      "l’instabilité en convergence.",
  diss="Comparer deux modèles par leurs hypothèses, et non par leurs "
       "conclusions, est la manière la plus rigoureuse de traiter un débat "
       "théorique."),

f(id='q6-m10', sp='c6-05', niv='appliquer', type='qcm', b=655,
  q="Une économie double simultanément son stock de capital et son volume de "
    "travail, et sa production double exactement. Que peut-on en dire dans le "
    "cadre de la fonction de Cobb-Douglas retenue par le cours ?",
  opts=["Les rendements d’échelle sont constants : la croissance est "
        "purement extensive",
        "Les rendements d’échelle sont croissants",
        "La productivité globale des facteurs a augmenté",
        "L’intensité capitalistique a doublé"],
  ans=0,
  why=["Des rendements croissants auraient conduit la production à plus que "
       "doubler.",
       "C’est l’inverse : rien n’est gagné en efficacité, donc la PGF est "
       "inchangée — le résidu est nul.",
       "L’intensité capitalistique est le rapport du capital au travail : "
       "les deux ayant doublé, elle est inchangée."],
  exp="La croissance est dite extensive lorsqu’elle provient de "
      "l’augmentation des quantités de facteurs, et intensive lorsqu’elle "
      "provient de leur meilleure utilisation. Ici, la production suit "
      "exactement les facteurs : aucun gain d’efficacité, donc un résidu "
      "nul. C’est le contraire de ce que Carré, Dubois et Malinvaud "
      "observent pour la France des Trente Glorieuses, où la PGF explique "
      "environ 60 % de la croissance.",
  diss="Opposer croissance extensive et intensive permet de poser "
       "immédiatement la question de la soutenabilité : la première bute sur "
       "les quantités disponibles, la seconde non."),
]
