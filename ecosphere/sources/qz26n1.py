# -*- coding: utf-8 -*-
"""Chapitre 26 — questions nouvelles, marché des changes et régimes (c26-01 à c26-07)."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c26-01
f(id='q26-n01', sp='c26-01', niv='appliquer', type='assoc', b=183,
  q="Associez chaque mesure du taux de change à ce qu’elle permet de "
    "répondre.",
  ans=[["Combien d’unités d’une devise obtient-on pour une unité de monnaie "
        "nationale ?", "Taux de change nominal bilatéral"],
       ["Une monnaie s’est-elle appréciée ou dépréciée face à l’ensemble de "
        "ses partenaires ?", "Taux de change effectif nominal"],
       ["Les produits nationaux sont-ils devenus plus ou moins chers que les "
        "produits étrangers ?", "Taux de change réel"]],
  exp="Chaque mesure répond à une question distincte, et c’est pourquoi "
      "aucune ne suffit seule. Le bilatéral ne renseigne que sur une "
      "relation ; l’effectif pondère les taux bilatéraux par le poids des "
      "partenaires — dans l’exemple simplifié du cours, 40 % pour les "
      "États-Unis, 35 % pour la Chine et 25 % pour le Royaume-Uni ; le réel "
      "corrige par les niveaux de prix et mesure donc la compétitivité-prix.",
  diss="Conséquence très utile : une monnaie peut se déprécier face à une "
       "devise tout en s’appréciant en termes effectifs, et s’apprécier "
       "nominalement tout en se dépréciant en termes réels."),

f(id='q26-n02', sp='c26-01', niv='raisonner', type='qcm', b=147,
  q="Pourquoi le rôle de monnaie véhiculaire du dollar est-il un privilège "
    "particulier ?",
  opts=["Parce qu’il oblige les États-Unis à détenir des réserves de change "
        "importantes",
        "Parce que le dollar sert d’intermédiaire dans des transactions qui "
        "ne concernent pas directement les États-Unis, ce qui engendre une "
        "demande internationale structurelle",
        "Parce qu’il garantit un excédent commercial américain",
        "Parce qu’il interdit aux autres pays d’émettre de la monnaie"],
  ans=1,
  why=["Les États-Unis ont au contraire moins besoin de réserves, puisqu’ils "
       "s’endettent dans leur propre monnaie.",
       "Les États-Unis connaissent au contraire un déficit commercial "
       "structurel.",
       "Les autres pays conservent leur souveraineté monétaire."],
  exp="Deux autres fonctions s’y ajoutent : unité de compte, de nombreux "
      "contrats et matières premières étant libellés en dollars, et réserve "
      "de valeur internationale, les banques centrales en détenant une part "
      "importante de leurs réserves. Cette demande structurelle est au cœur "
      "de la doctrine Miran, qui y voit la cause d’une surévaluation de la "
      "monnaie américaine.",
  diss="Articulation avec la fin du chapitre : ce privilège est précisément ce "
       "que le paradoxe du dollar met en tension."),

# ------------------------------------------------------------- c26-02
f(id='q26-n03', sp='c26-02', niv='comprendre', type='qcm', b=401,
  q="Que révèle l’écart entre le volume des transactions sur le marché des "
    "changes et celui des échanges de biens et services ?",
  opts=["Une erreur de mesure statistique",
        "Une financiarisation de l’économie mondiale et une déconnexion "
        "entre transactions financières et échanges réels",
        "Une baisse du commerce international",
        "Une diminution du rôle du dollar"],
  ans=1,
  why=["Les deux agrégats sont mesurés par des sources différentes mais "
       "fiables : l’écart n’est pas un artefact.",
       "Le commerce international a au contraire fortement progressé.",
       "Le dollar domine au contraire le marché des changes."],
  exp="Trois mécanismes expliquent ce développement : l’essor du commerce "
      "international, la multiplication des produits dérivés et "
      "l’intensification des opérations financières. C’est le deuxième qui "
      "pèse le plus lourd : les opérations de couverture et de spéculation se "
      "superposent aux transactions commerciales, chaque échange réel pouvant "
      "donner lieu à plusieurs opérations financières.",
  diss="Conséquence pour l’analyse du change : le taux de change est "
       "aujourd’hui déterminé davantage par les mouvements de capitaux que "
       "par les flux commerciaux."),

f(id='q26-n04', sp='c26-02', niv='raisonner', type='vf', b=347,
  q="L’arbitrage sur le marché des changes contribue à l’efficience "
    "informationnelle des cotations.",
  ans=True,
  exp="L’arbitrage consiste à exploiter un écart de prix entre deux places ou "
      "deux circuits pour un même couple de monnaies. Or exploiter cet écart "
      "le referme : acheter là où la monnaie est moins chère en fait monter "
      "le prix, vendre là où elle est plus chère le fait baisser. Un même "
      "couple ne peut donc pas durablement s’échanger à deux prix différents, "
      "ce qui unifie les cotations à l’échelle mondiale — propriété renforcée "
      "par le caractère de marché-réseau décrit par Plihon, qui assure un "
      "fonctionnement quasi continu.",
  diss="Distinction rigoureuse à tenir : l’arbitrage est sans risque et "
       "unifie les prix, la spéculation accepte le risque et peut les "
       "éloigner de leur valeur de référence."),

# ------------------------------------------------------------- c26-03
f(id='q26-n05', sp='c26-03', niv='connaitre', type='assoc', b=473,
  q="Associez chaque instrument de gestion du risque de change à sa "
    "définition.",
  ans=[["Acheter ou vendre une devise au taux convenu aujourd’hui, avec "
        "règlement souvent sous deux jours ouvrés", "Opération au comptant"],
       ["Fixer aujourd’hui un taux de change pour un échange réalisé à une "
        "date future, avec obligation d’exécution",
        "Opération de change à terme"],
       ["Acquérir le droit, mais non l’obligation, d’acheter ou de vendre une "
        "devise à un taux déterminé, contre paiement d’une prime",
        "Option de change"],
       ["Échanger des devises à une première date en convenant d’un échange "
        "inverse à une date ultérieure", "Swap de change"]],
  exp="La différence décisive entre le contrat à terme et l’option tient à "
      "l’obligation d’exécution : l’engagement à terme doit être exécuté même "
      "si l’évolution du marché devient favorable, alors que l’option peut "
      "ne pas être exercée — mais la prime reste due. Le cours précise par "
      "ailleurs qu’un swap n’est pas une assurance : c’est un contrat "
      "d’échange comportant des obligations réciproques.",
  diss="Point souvent mal maîtrisé : ces mêmes instruments servent la "
       "couverture comme la spéculation, selon l’intention de l’opérateur."),

f(id='q26-n06', sp='c26-03', niv='appliquer', type='qcm', b=469,
  q="Une entreprise européenne doit payer 1 million de dollars dans six mois "
    "et achète une option d’achat de dollars. Que se passe-t-il si le dollar "
    "se déprécie ?",
  opts=["Elle est obligée d’exercer son option au taux prévu",
        "Elle peut renoncer à exercer l’option et acheter au taux de marché "
        "devenu plus favorable, mais elle a payé la prime",
        "L’option est automatiquement annulée et la prime remboursée",
        "Elle réalise un gain égal à la dépréciation du dollar"],
  ans=1,
  why=["L’obligation d’exécution caractérise le contrat à terme, non "
       "l’option.",
       "La prime n’est jamais remboursée : elle rémunère le vendeur de "
       "l’option.",
       "Son gain est limité à la différence entre le taux de marché et le "
       "taux garanti, diminuée de la prime."],
  exp="L’option fonctionne donc comme une assurance contre une évolution "
      "défavorable du change : elle protège contre la hausse du dollar tout "
      "en laissant bénéficier d’une baisse, et ce service a un coût, la "
      "prime. Avec un contrat à terme, l’entreprise aurait connu son coût "
      "avec certitude mais n’aurait pas profité de la dépréciation.",
  diss="Arbitrage à formuler : le terme supprime l’incertitude, l’option "
       "conserve le gain potentiel contre une prime certaine."),

f(id='q26-n07', sp='c26-03', niv='comprendre', type='qcm', b=445,
  q="Pourquoi le taux de change à terme diffère-t-il généralement du taux au "
    "comptant ?",
  opts=["Parce que les banques appliquent une commission fixe",
        "Parce qu’il dépend notamment des taux d’intérêt des deux monnaies",
        "Parce que les autorités monétaires le fixent",
        "Parce que les anticipations sont toujours erronées"],
  ans=1,
  why=["Une commission existe, mais elle n’explique pas l’écart systématique "
       "entre comptant et terme.",
       "Les autorités ne fixent pas le taux à terme, qui résulte du marché.",
       "La qualité des anticipations n’explique pas l’écart structurel."],
  exp="Placer des fonds dans l’une ou l’autre monnaie pendant la durée du "
      "contrat ne rapporte pas la même chose : l’écart de taux d’intérêt se "
      "retrouve donc dans l’écart entre le taux à terme et le taux au "
      "comptant, faute de quoi un arbitrage sans risque serait possible. "
      "C’est le même raisonnement d’arbitrage qui unifie les cotations "
      "comptant entre places financières.",
  diss="Mécanisme à relier aux instruments de la politique de change : c’est "
       "parce que les taux d’intérêt agissent sur l’attractivité des "
       "placements qu’ils constituent un levier sur le taux de change."),

# ------------------------------------------------------------- c26-05
f(id='q26-n08', sp='c26-05', niv='appliquer', type='ordre', b=894,
  q="Classez ces régimes de change du plus rigide au plus flexible.",
  ans=["La dollarisation ou l’euroïsation : abandon de la monnaie nationale",
       "L’union monétaire : partage d’une monnaie et d’une politique "
       "monétaire",
       "La caisse d’émission : convertibilité à taux fixe encadrée par une "
       "règle stricte de couverture en devises",
       "Le régime conventionnel de change fixe : parité centrale et bandes de "
       "fluctuation",
       "Le flottement administré : interventions sans engagement de parité",
       "Le flottement libre : la valeur de la monnaie est déterminée par le "
       "marché"],
  exp="Les régimes forment donc un continuum entre ancrage strict et "
      "flottement libre, et non une alternative entre deux options. Plus les "
      "autorités s’engagent à stabiliser la valeur de leur monnaie, moins le "
      "taux de change est flexible ; plus le marché la détermine librement, "
      "plus la flexibilité est grande.",
  diss="Donnée chiffrée à joindre : en 2025, arrimage ferme 29 pays (13 %), "
       "arrimage souple 88 pays (46 %), flottement 66 pays (34 %), autres ou "
       "non classés 13 pays (7 %)."),

f(id='q26-n09', sp='c26-05', niv='raisonner', type='qcm', b=880,
  q="Pourquoi le régime de change déclaré au FMI ne suffit-il pas à "
    "identifier le régime effectivement pratiqué ?",
  opts=["Parce que le FMI ne publie pas les déclarations",
        "Parce que certains pays déclarent un régime flexible tout en "
        "intervenant massivement, et qu’un pays peut annoncer un ancrage "
        "qu’il ne parvient pas à respecter durablement",
        "Parce que les régimes changent tous les ans",
        "Parce que les déclarations sont facultatives"],
  ans=1,
  why=["Le FMI observe et classe au contraire les pratiques des pays.",
       "La fréquence des changements n’est pas le problème relevé.",
       "La déclaration du régime au FMI est précisément une obligation."],
  exp="Le choix du régime relève de la souveraineté monétaire — c’est une "
      "prérogative régalienne — et doit être déclaré au FMI, qui observe les "
      "pratiques, classe les régimes et identifie les écarts entre "
      "engagements officiels et politiques réellement menées. C’est exactement "
      "ce qu’établissent Calvo et Reinhart dans « Fear of Floating » (2002) : "
      "la volatilité des réserves et des taux d’intérêt révèle les "
      "interventions mieux que les déclarations.",
  diss="Leçon de méthode : pour identifier un régime de change, regarder les "
       "réserves et les taux plutôt que les textes."),

f(id='q26-n10', sp='c26-05', niv='comprendre', type='qcm', b=942,
  q="Qu’est-ce qui contraint le plus fortement la création monétaire dans une "
    "caisse d’émission ?",
  opts=["L’interdiction d’émettre de la monnaie nationale",
        "L’obligation de couvrir l’émission de monnaie nationale par des "
        "réserves en devises, selon les règles du dispositif",
        "L’interdiction des réserves de change",
        "L’obligation de laisser flotter la monnaie"],
  ans=1,
  why=["Le pays conserve au contraire sa monnaie nationale : c’est ce qui "
       "distingue la caisse d’émission de la dollarisation.",
       "Les réserves de change sont au contraire le pilier du dispositif.",
       "Le flottement est l’opposé d’une caisse d’émission."],
  exp="Les autorités doivent pouvoir garantir à tout moment la conversion de "
      "leur monnaie à la parité annoncée : la création monétaire est donc "
      "mécaniquement liée aux entrées de devises, ce qui prive la banque "
      "centrale de toute autonomie. Le cours cite Hong Kong, lié au dollar "
      "américain depuis 1983, et le régime de convertibilité argentin de 1991 "
      "à 2002, dont l’abandon illustre la fragilité de ces ancrages.",
  diss="Lecture par le triangle de Mundell : la caisse d’émission sacrifie "
       "l’autonomie monétaire pour obtenir la stabilité du change avec "
       "mobilité des capitaux."),

f(id='q26-n11', sp='c26-05', niv='raisonner', type='courte', b=936,
  q="Que perd un pays qui adopte la dollarisation ou entre dans une union "
    "monétaire, et que gagne-t-il ?",
  ans={'modele': "Il perd d’abord la conduite d’une politique monétaire "
       "nationale indépendante : il ne peut plus créer librement sa propre "
       "monnaie ni ajuster ses taux à sa situation conjoncturelle. Il perd "
       "ensuite l’instrument de la dévaluation : une perte de compétitivité "
       "ne peut plus être corrigée par un ajustement du change, ce qui "
       "reporte l’ajustement sur les prix et les salaires internes. Il dépend "
       "enfin des conditions monétaires associées à la devise adoptée, "
       "décidées ailleurs. En contrepartie, il gagne la crédibilité "
       "monétaire : ces choix interviennent souvent après une crise majeure — "
       "effondrement de la monnaie nationale, perte de confiance dans les "
       "autorités monétaires, instabilité politique — et l’objectif est "
       "précisément de restaurer la confiance. Dans le cas d’une union "
       "monétaire, s’ajoutent la suppression du risque de change entre "
       "membres et l’approfondissement de l’intégration économique, ainsi "
       "qu’une participation à la décision monétaire commune, que la "
       "dollarisation unilatérale ne procure pas.",
       'cles': [{'f': ['politique monetaire', 'independante', 'autonomie',
                       'creer'],
                 'l': "la perte d'une politique monétaire indépendante"},
                {'f': ['devaluer', 'devaluation', 'competitivite', 'ajuster'],
                 'l': "la perte de l'instrument de la dévaluation"},
                {'f': ['depend', 'condition monetaire', 'devise adoptee',
                       'ailleurs'],
                 'l': "la dépendance aux conditions monétaires de la devise adoptée"},
                {'f': ['confiance', 'credibilite', 'crise', 'restaurer'],
                 'l': "le gain de crédibilité, souvent après une crise"},
                {'f': ['risque de change', 'integration', 'union monetaire',
                       'membre'],
                 'l': "dans une union : suppression du risque de change et intégration"},
                {'f': ['decision commune', 'participe', 'unilateral',
                       'bce'],
                 'l': "la participation à la décision commune, absente de la dollarisation"}]},
  exp="L’union monétaire approfondit l’intégration économique en supprimant "
      "le risque de change entre ses membres, mais elle implique l’abandon "
      "des politiques monétaires nationales et de l’ajustement par le taux de "
      "change.",
  diss="Comparaison payante : dollarisation et union monétaire sacrifient le "
       "même sommet du triangle, mais la seconde offre une voix dans la "
       "décision."),

# ------------------------------------------------------------- c26-06
f(id='q26-n12', sp='c26-06', niv='appliquer', type='ordre', b=1118,
  q="Remettez dans l’ordre la séquence monétaire internationale des années "
    "1980.",
  ans=["À partir de 1979, la Fed de Paul Volcker relève fortement ses taux "
       "pour casser l’inflation",
       "Les rendements en dollars montent, les capitaux affluent et le dollar "
       "s’apprécie fortement",
       "L’appréciation creuse le déficit commercial américain, qui s’ajoute "
       "au déficit public : ce sont les déficits jumeaux",
       "En septembre 1985, les accords du Plaza organisent une baisse "
       "ordonnée du dollar",
       "La dépréciation étant jugée excessive, les accords du Louvre de "
       "février 1987 cherchent à stabiliser les cours"],
  exp="Cette séquence est doublement instructive. Elle montre d’abord que les "
      "banques centrales peuvent intervenir collectivement même en régime de "
      "changes flottants. Elle fournit ensuite la contre-épreuve de "
      "l’argument d’insularisation de Friedman : le durcissement américain "
      "provoque des mouvements internationaux de capitaux et une appréciation "
      "du dollar qui fragilisent d’autres économies, notamment celles "
      "endettées en dollars.",
  diss="Séquence à réutiliser pour le chapitre sur la dette : c’est le même "
       "choc Volcker qui transforme le recyclage des pétrodollars en crise de "
       "la dette."),

f(id='q26-n13', sp='c26-06', niv='comprendre', type='qcm', b=1184,
  q="En quoi une ligne de swap entre banques centrales diffère-t-elle d’une "
    "intervention de change ?",
  opts=["Elle est décidée par le FMI",
        "Elle fournit temporairement des liquidités en devise à une autre "
        "banque centrale, au lieu de chercher à influencer le cours",
        "Elle porte sur l’or et non sur les devises",
        "Elle est irréversible"],
  ans=1,
  why=["Elle est conclue entre banques centrales, sans intervention du FMI.",
       "Elle porte sur des devises, non sur l’or.",
       "Elle est au contraire temporaire : l’échange inverse est prévu."],
  exp="Le cours insiste sur cette distinction : l’intervention de change est "
      "un achat ou une vente de devises destinée à agir sur le cours, la "
      "ligne de swap est une fourniture temporaire de liquidités, forme de "
      "coopération entre banques centrales. Les deux relèvent de la "
      "coopération monétaire internationale mais ne poursuivent pas le même "
      "objectif : agir sur le prix dans un cas, sur la liquidité dans "
      "l’autre.",
  diss="Enjeu contemporain à mentionner : ces lignes ont joué un rôle décisif "
       "lors des crises financières, en évitant l’assèchement de la liquidité "
       "en dollars."),

# ------------------------------------------------------------- c26-07
f(id='q26-n14', sp='c26-07', niv='appliquer', type='assoc', b=1456,
  q="Associez chaque argument flexibiliste de Friedman à la limite que le "
    "cours lui oppose.",
  ans=[["Le marché détermine le taux de change d’équilibre",
        "Le change peut s'écarter durablement de la parité des pouvoirs d'achat"],
       ["La spéculation est stabilisatrice",
        "En période de crise, les anticipations de tendance amplifient les déséquilibres"],
       ["La balance des paiements s’ajuste automatiquement",
        "L'ajustement suppose la condition de Marshall-Lerner et prend du temps"],
       ["Les politiques nationales sont insularisées",
        "Le choc Volcker montre que les politiques monétaires restent interdépendantes"]],
  exp="Les quatre arguments ne sont pas réfutés mais conditionnés : chacun "
      "vaut dans certaines circonstances et non dans d’autres. C’est "
      "pourquoi le cours conclut non pas à la supériorité d’un régime mais à "
      "la nécessité d’un arbitrage — ce que confirme la persistance des "
      "régimes d’ancrage, qui concernent encore 59 % des pays en 2025.",
  diss="Structure de dissertation idéale : présenter la thèse de Friedman, "
       "puis la confronter argument par argument, plutôt que de la rejeter en "
       "bloc."),

f(id='q26-n15', sp='c26-07', niv='raisonner', type='qcm', b=1425,
  q="Pourquoi la spéculation peut-elle être tour à tour stabilisatrice et "
    "déstabilisatrice ?",
  opts=["Parce que les spéculateurs changent de nationalité",
        "Parce que la nature des anticipations change : retour à la moyenne "
        "en période calme, poursuite de la tendance en période de crise",
        "Parce que les banques centrales modifient les règles",
        "Parce que les montants engagés varient"],
  ans=1,
  why=["La nationalité des opérateurs n’intervient pas dans ce mécanisme.",
       "Les règles ne changent pas selon la période : c’est le comportement "
       "des opérateurs qui change.",
       "Les montants amplifient l’effet sans en déterminer le sens."],
  exp="En période calme, les opérateurs achètent une monnaie jugée "
      "sous-évaluée et vendent une monnaie jugée surévaluée, ce qui ramène le "
      "cours vers sa valeur de référence. En période de crise, ils "
      "anticipent la poursuite du mouvement : les ventes alimentent alors la "
      "baisse qu’elles anticipaient, et le processus devient "
      "autoréalisateur. Le cours en tire une conclusion décisive : le marché "
      "des changes est simultanément stabilisateur et déstabilisateur.",
  diss="Mécanisme à réutiliser deux fois dans le chapitre : pour nuancer "
       "Friedman, et pour expliquer les anticipations autoréalisatrices de "
       "dévaluation."),

f(id='q26-n16', sp='c26-07', niv='raisonner', type='courte', b=1456,
  q="En quoi le choc Volcker constitue-t-il la contre-épreuve de l’argument "
    "d’insularisation ?",
  ans={'modele': "L’argument d’insularisation soutient qu’en régime de "
       "changes flottants, la politique monétaire, libérée de la défense "
       "d’une parité, peut se consacrer entièrement aux objectifs internes : "
       "chaque pays serait ainsi protégé des contraintes extérieures. Le choc "
       "Volcker le démentit. À partir de 1979, la Réserve fédérale relève "
       "fortement ses taux pour casser l’inflation américaine : c’est bien "
       "une décision prise au nom d’un objectif interne. Mais ses effets sont "
       "internationaux. Les rendements en dollars montent, ce qui provoque "
       "des mouvements internationaux de capitaux et une forte appréciation "
       "du dollar. Les autres économies sont alors contraintes de relever "
       "elles aussi leurs taux pour éviter des sorties de capitaux et une "
       "dépréciation, et les pays endettés en dollars voient leur dette "
       "s’alourdir mécaniquement — ce qui conduit à la crise mexicaine de "
       "1982 puis à la crise internationale de la dette. Le flottement ne "
       "supprime donc pas l’interdépendance des politiques monétaires : il en "
       "change seulement le canal de transmission, qui passe des réserves de "
       "change aux mouvements de capitaux et au taux de change.",
       'cles': [{'f': ['insularisation', 'objectif interne', 'liberee',
                       'parite'],
                 'l': "l'argument : la politique monétaire se consacre aux objectifs internes"},
                {'f': ['1979', 'volcker', 'taux', 'inflation'],
                 'l': "le relèvement des taux américains à partir de 1979"},
                {'f': ['capitaux', 'appreciation', 'dollar', 'rendement'],
                 'l': "mouvements de capitaux et appréciation du dollar"},
                {'f': ['contraint', 'relever', 'autres economie',
                       'depreciation'],
                 'l': "les autres pays contraints de suivre"},
                {'f': ['dette', 'mexique', '1982', 'endette en dollar'],
                 'l': "l'alourdissement des dettes en dollars et la crise de 1982"},
                {'f': ['interdependance', 'pas supprime', 'canal',
                       'transmission'],
                 'l': "l'interdépendance subsiste, seul le canal change"}]},
  exp="Le choc Volcker montre que les politiques monétaires restent "
      "interdépendantes malgré le flottement : le durcissement américain "
      "provoque des mouvements internationaux de capitaux et une appréciation "
      "du dollar qui fragilisent d’autres économies.",
  diss="Exemple à double emploi : il réfute l’insularisation et il explique "
       "la crise de la dette — deux usages dans deux parties différentes."),

]
