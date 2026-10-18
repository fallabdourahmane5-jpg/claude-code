# -*- coding: utf-8 -*-
"""Ensemble 1 — La croissance économique et ses moteurs (1/3).

Matière tirée du chapitre 6 (la croissance économique), complétée par les
chapitres 1, 3, 7 et 21. Aucune attribution n'est ajoutée de mémoire.
"""

from doss_base import d

d('n1-croissance', 1, "Croissance économique",
  "Une augmentation soutenue de la production, mesurable et distincte du développement",
  "La croissance économique désigne l’augmentation soutenue, sur une longue "
  "période, de la production de biens et de services d’une économie, mesurée "
  "par la variation du produit intérieur brut en volume. Trois mots font la "
  "définition : soutenue, ce qui exclut la simple reprise conjoncturelle ; "
  "longue période, ce qui en fait un phénomène structurel ; en volume, ce qui "
  "neutralise la hausse des prix. François Perroux insiste sur cette rigueur : "
  "la croissance est un phénomène quantitatif, à distinguer du développement, "
  "qui désigne les transformations structurelles et sociales qui "
  "l’accompagnent.",
  "La croissance se laisse analyser à trois niveaux qu’une copie doit tenir "
  "séparés. Le premier est descriptif : l’analyse de longue période dégage des "
  "régularités que Kaldor appelle les faits stylisés, et une périodisation — "
  "diffusion progressive de l’industrialisation au XIXᵉ siècle, forte "
  "croissance des pays développés entre 1945 et 1975, ralentissement depuis les "
  "années 1970. Le deuxième est comptable : on décompose la croissance entre la "
  "contribution des facteurs de production et un résidu. Lorsque la "
  "contribution des facteurs domine, la croissance est extensive ; lorsque "
  "c’est celle de la productivité globale des facteurs, elle est intensive. "
  "Carré, Dubois et Malinvaud appliquent cette méthode à la France dans La "
  "croissance française (1972) et trouvent qu’environ 60 % de la croissance des "
  "Trente Glorieuses s’explique par la productivité globale des facteurs. Le "
  "troisième niveau est explicatif, et c’est là que les théories s’opposent : "
  "pour Solow, le progrès technique reste exogène, une « manne tombée du "
  "ciel » ; pour les théories de la croissance endogène, il résulte de "
  "décisions économiques — recherche, éducation, infrastructures — ce qui "
  "change radicalement les conclusions de politique économique. Le passage d’un "
  "niveau à l’autre est le fil conducteur de tout sujet sur la croissance : "
  "mesurer, décomposer, expliquer.",
  [("L’accumulation des facteurs",
    "L’augmentation de la quantité de travail employée et du stock de capital "
    "permet de produire davantage. C’est la source la plus immédiate de "
    "croissance, mais elle se heurte aux rendements décroissants : chaque unité "
    "de capital supplémentaire ajoute moins que la précédente."),
   ("Les gains de productivité",
    "À quantité de facteurs inchangée, une meilleure organisation, une "
    "main-d’œuvre plus qualifiée ou des techniques plus efficaces augmentent la "
    "production. Cette part échappe à la comptabilisation des facteurs et "
    "constitue le résidu."),
   ("Le caractère cumulatif",
    "Les gains de productivité élèvent les revenus, qui alimentent la demande "
    "et financent l’investissement, lequel engendre de nouveaux gains. La "
    "croissance s’entretient, ce que Jean Arrous résume en la décrivant comme "
    "un processus cumulatif fondé sur la productivité."),
   ("La diffusion sectorielle",
    "Les gains obtenus dans une branche se transmettent aux autres par la baisse "
    "des prix des biens d’équipement, par la mobilité de la main-d’œuvre et par "
    "l’imitation des méthodes, ce qui transforme un progrès local en croissance "
    "d’ensemble.")],
  [{'a': "La croissance élève le niveau de vie moyen : un produit par habitant "
         "plus élevé permet une consommation, une épargne et un financement "
         "collectif supérieurs.",
    'cond': "Il faut que la croissance excède celle de la population, et que la "
            "répartition du supplément ne concentre pas l’intégralité du gain "
            "sur une fraction réduite de la société.",
    'lim': "Le produit par habitant est une moyenne : il peut progresser alors "
           "qu’une partie de la population voit sa situation stagner, ce qui "
           "explique l’écart entre performance macroéconomique et perception."},
   {'a': "La croissance finance les dépenses collectives sans augmenter les taux "
         "de prélèvement, puisqu’elle élargit l’assiette.",
    'cond': "Le supplément de recettes ne doit pas être absorbé par une "
            "progression parallèle des dépenses, et la croissance doit être "
            "assez durable pour que les engagements pris soient tenables.",
    'lim': "Adosser le financement de la protection sociale à la croissance rend "
           "le système vulnérable à son ralentissement, ce qui est précisément "
           "la situation des économies avancées depuis les années 1970."},
   {'a': "La croissance rend les arbitrages politiques moins conflictuels, "
         "puisqu’il devient possible d’améliorer la situation des uns sans "
         "dégrader celle des autres.",
    'cond': "Le gain doit être suffisamment partagé pour que chacun y "
            "reconnaisse sa part, faute de quoi l’effet d’apaisement ne se "
            "produit pas.",
    'lim': "L’argument se retourne : un ralentissement durable transforme toute "
           "politique en jeu à somme nulle et durcit mécaniquement les "
           "conflits de répartition."}],
  [{'t': "La croissance mesurée par le produit intérieur brut ignore ce qu’elle "
         "détruit : ressources naturelles, qualité de l’air, temps libre.",
    'qui': "Critique récurrente des limites du PIB, développée dans le chapitre "
           "sur la croissance et prolongée par les analyses de la soutenabilité.",
    'rep': "L’objection vise l’indicateur plus que le phénomène. Elle justifie "
           "des mesures complémentaires, sans invalider le constat qu’une "
           "production plus élevée élargit l’éventail des choix collectifs."},
   {'t': "Croissance et développement ne se confondent pas : un pays peut voir "
         "sa production augmenter sans transformation de ses structures ni "
         "amélioration des conditions de vie.",
    'qui': "François Perroux, qui distingue rigoureusement les deux notions.",
    'rep': "La distinction est fondatrice et doit être posée d’emblée. Elle "
           "n’oppose pas les deux termes : la croissance reste généralement "
           "nécessaire au développement, elle n’y suffit pas."},
   {'t': "La croissance est instable par nature : rien ne garantit qu’elle "
         "suive un sentier équilibré.",
    'qui': "Roy Harrod et Evsey Domar, avec l’instabilité de la croissance et "
           "l’image du fil du rasoir.",
    'rep': "L’instabilité décrite est théorique et suppose des coefficients "
           "rigides ; elle rappelle néanmoins que l’équilibre de longue période "
           "n’a rien d’automatique et justifie une régulation."}],
  [{'n': "François Perroux",
    'i': "La croissance est l’augmentation soutenue, sur une longue période, "
         "d’un indicateur de dimension — elle se distingue du développement.",
    'p': "La définition impose la rigueur : elle écarte l’expansion "
         "conjoncturelle, qui est de courte période, et le développement, qui "
         "suppose des transformations structurelles, mentales et sociales que "
         "la seule hausse du produit ne garantit pas."},
   {'n': "Nicholas Kaldor",
    'i': "Les faits stylisés : des régularités statistiques observées sur longue "
         "période caractérisent la croissance des économies développées.",
    'p': "Leur intérêt est méthodologique : une théorie de la croissance doit "
         "pouvoir rendre compte de ces régularités, ce qui fournit un critère "
         "de sélection entre les modèles concurrents."},
   {'n': "Jean Arrous",
    'i': "La croissance est un processus cumulatif fondé sur la productivité.",
    'p': "Le caractère cumulatif est ce qui distingue la croissance d’une "
         "succession de hausses ponctuelles : les gains d’une période "
         "engendrent les moyens de la suivante, ce qui rend le phénomène "
         "auto-entretenu."},
   {'n': "Robert Solow",
    'i': "Le progrès technique explique l’essentiel de la croissance, mais le "
         "modèle le traite comme exogène.",
    'p': "Solow parle du progrès technique comme d’une « manne tombée du "
         "ciel » : une richesse qui apparaît sans que le modèle en explique "
         "l’origine. Le résidu mesure donc autant notre ignorance que le "
         "progrès technique lui-même."}],
  [{'f': "Selon Carré, Dubois et Malinvaud dans La croissance française (1972), "
         "environ 60 % de la croissance française des Trente Glorieuses "
         "s’explique par la productivité globale des facteurs, soit 3,1 points "
         "sur une croissance totale de 5,2 %.",
    'p': "Le calcul établit que la croissance des Trente Glorieuses a été "
         "principalement intensive, donc fondée sur l’efficacité productive "
         "plutôt que sur la seule accumulation de facteurs."},
   {'f': "La périodisation retenue par le cours distingue la diffusion "
         "progressive de l’industrialisation au XIXᵉ siècle, la forte "
         "croissance des pays développés de 1945 à 1975, et le ralentissement "
         "depuis les années 1970.",
    'p': "La croissance évolue par phases historiques : elle n’est ni un état "
         "permanent ni une tendance régulière, ce qui interdit d’extrapoler une "
         "période à une autre."},
   {'f': "De 2010 à 2021, la croissance est plutôt intensive au Danemark et en "
         "Allemagne, plutôt extensive en France et aux États-Unis.",
    'p': "La distinction extensive/intensive n’est pas seulement historique : "
         "elle sépare aujourd’hui encore des trajectoires nationales aux "
         "perspectives de long terme très différentes."}],
  [{'q': "Sujet du type « D’où vient la croissance économique ? »",
    'f': "La question appelle une réponse en trois temps, correspondant aux "
         "trois niveaux d’analyse : la croissance vient d’abord de "
         "l’accumulation des facteurs, puis des gains de productivité qui "
         "constituent le résidu, enfin des décisions — recherche, éducation, "
         "infrastructures — qui produisent ce résidu et que les théories "
         "endogènes ont rendues explicites.",
    'r': "Le plan reproduit la progression de l’analyse elle-même, de la "
         "comptabilité à l’explication, ce qui évite la juxtaposition de "
         "modèles et donne au devoir une véritable dynamique.",
    'ex': "Carré, Dubois et Malinvaud attribuent environ 60 % de la croissance "
          "française des Trente Glorieuses à la productivité globale des "
          "facteurs."},
   {'q': "Sujet du type « Produire davantage signifie-t-il vivre mieux ? »",
    'f': "La distinction de Perroux entre croissance et développement fournit la "
         "réponse : la croissance est un phénomène quantitatif, le "
         "développement suppose des transformations structurelles et sociales. "
         "Produire davantage élargit l’éventail des possibles sans garantir "
         "qu’ils soient réalisés ni équitablement répartis.",
    'r': "On montre que l’écart entre les deux notions n’est pas un supplément "
         "moral mais une distinction analytique, ce qui permet de traiter "
         "ensuite la question des indicateurs et de la soutenabilité.",
    'ex': "La croissance mesurée par le PIB ignore l’épuisement des ressources "
          "et les conditions de vie, ce qui motive les indicateurs "
          "complémentaires."}],
  voisins=['n1-extensive-intensive', 'n1-pgf', 'n1-progres-technique',
           'n1-endogene', 'n1-pib', 'n1-potentielle'])

d('n1-extensive-intensive', 1, "Croissance extensive et croissance intensive",
  "Croître en employant plus, ou croître en employant mieux",
  "La croissance extensive résulte principalement de l’augmentation des "
  "quantités de facteurs de production employés : davantage de travailleurs, "
  "davantage de capital. La croissance intensive résulte principalement de "
  "l’amélioration de l’efficacité avec laquelle ces facteurs sont combinés, "
  "mesurée par la productivité globale des facteurs. La distinction n’est pas "
  "qualitative mais comptable : elle dépend de la contribution qui domine dans "
  "la décomposition de la croissance.",
  "La distinction a une portée considérable parce qu’elle commande les "
  "perspectives de long terme. Une croissance extensive se heurte "
  "nécessairement à une limite : la population active n’augmente pas "
  "indéfiniment, et l’accumulation de capital se heurte aux rendements "
  "décroissants — chaque machine supplémentaire ajoute moins de production que "
  "la précédente lorsque le nombre de travailleurs reste constant. Une "
  "croissance intensive ne rencontre pas cette borne, puisqu’elle provient "
  "d’une meilleure combinaison des facteurs plutôt que de leur augmentation. "
  "C’est la raison pour laquelle le diagnostic porté sur une économie dépend "
  "largement de la nature de sa croissance. Le cours applique la distinction à "
  "la période récente : de 2010 à 2021, la croissance est plutôt intensive au "
  "Danemark et en Allemagne, plutôt extensive en France et aux États-Unis. "
  "Cette observation ne dit pas qu’un modèle est supérieur à l’autre dans "
  "l’absolu — une croissance extensive tirée par la démographie peut être "
  "parfaitement souhaitable — mais elle indique où se situe la marge de "
  "progression et ce qu’il faudrait faire pour la mobiliser : accroître "
  "l’emploi dans un cas, élever la productivité dans l’autre.",
  [("La mesure de la contribution des facteurs",
    "On évalue séparément la contribution de la hausse du volume de travail et "
    "celle de la hausse du stock de capital à la croissance observée, chacune "
    "pondérée par la part du facteur dans la valeur ajoutée."),
   ("Le calcul du résidu",
    "La part de la croissance que les facteurs n’expliquent pas constitue le "
    "résidu, assimilé à la productivité globale des facteurs. Elle mesure "
    "l’efficacité de la combinaison productive."),
   ("Le départage entre les deux régimes",
    "Si la contribution des facteurs domine, la croissance est extensive ; si "
    "c’est celle de la productivité globale, elle est intensive. Le critère est "
    "donc relatif et peut changer d’une période à l’autre pour un même pays."),
   ("Les rendements décroissants comme borne de l’extensif",
    "À technologie inchangée, l’ajout de capital à un volume de travail constant "
    "produit des gains de moins en moins élevés. Une croissance purement "
    "extensive finit donc par s’épuiser, ce qui est le résultat central du "
    "modèle de Solow.")],
  [{'a': "La croissance intensive est soutenable à long terme, puisqu’elle ne "
         "dépend pas d’une augmentation continue des quantités de facteurs.",
    'cond': "Elle suppose un flux continu d’innovations, de formation et "
            "d’amélioration organisationnelle, qui ne se produit pas "
            "spontanément.",
    'lim': "Les gains de productivité peuvent eux-mêmes ralentir, comme le "
           "soutient Robert Gordon : l’intensif n’est pas une garantie, "
           "seulement une absence de borne mécanique."},
   {'a': "La croissance extensive permet d’absorber une population active "
         "croissante et de réduire le chômage, ce que la croissance intensive "
         "ne fait pas nécessairement.",
    'cond': "Elle suppose une demande suffisante pour écouler la production "
            "supplémentaire et des capacités de financement de "
            "l’investissement.",
    'lim': "Elle se heurte aux rendements décroissants et, dans les économies "
           "vieillissantes, à la stagnation de la population active."},
   {'a': "La distinction fournit un diagnostic opérationnel : elle indique où se "
         "situe le levier de politique économique pour un pays donné.",
    'cond': "Le calcul doit reposer sur des séries comparables, la mesure du "
            "stock de capital et de la qualité du travail étant délicate.",
    'lim': "Le résidu agrège tout ce que le modèle n’explique pas : "
           "l’attribuer intégralement à l’efficacité productive revient à "
           "nommer une ignorance."}],
  [{'t': "La distinction repose sur un résidu qui mesure autant notre ignorance "
         "que le progrès technique.",
    'qui': "Lecture critique du « résidu de Solow », que le cours formule en "
           "demandant s’il s’agit d’une manne céleste ou d’une ignorance.",
    'rep': "L’objection est juste et impose la prudence : le résidu inclut "
           "l’organisation, les institutions, la qualité du travail et les "
           "erreurs de mesure. Elle n’annule pas la distinction, elle en "
           "précise la portée."},
   {'t': "Une croissance extensive n’est pas nécessairement inférieure : "
         "accroître l’emploi est un objectif légitime en soi.",
    'qui': "Objection de politique économique à une lecture normative de la "
           "distinction.",
    'rep': "Elle est fondée : le critère pertinent dépend de la situation du "
           "pays. Une économie en sous-emploi gagne à l’extensif, une économie "
           "au plein emploi n’a d’autre marge que l’intensif."}],
  [{'n': "Robert Solow",
    'i': "À technologie donnée, l’accumulation du capital se heurte aux "
         "rendements décroissants et ne peut soutenir la croissance "
         "indéfiniment.",
    'p': "Le résultat fonde la supériorité de long terme de la croissance "
         "intensive : seule la hausse de la productivité, chez Solow assimilée "
         "au progrès technique, permet une croissance durable du produit par "
         "tête."},
   {'n': "Jean Carré",
    'i': "La décomposition de la croissance française des Trente Glorieuses "
         "entre travail, capital et résidu.",
    'p': "Avec Paul Dubois et Edmond Malinvaud, dans La croissance française "
         "(1972) : la méthode consiste à mesurer ce que les facteurs expliquent "
         "pour isoler ce qu’ils n’expliquent pas."},
   {'n': "Edmond Malinvaud",
    'i': "La mesure de la contribution des facteurs permet de caractériser le "
         "régime de croissance d’un pays.",
    'p': "Le résultat obtenu pour la France — environ 60 % de la croissance "
         "imputable à la productivité globale des facteurs — établit le "
         "caractère intensif de la croissance des Trente Glorieuses."}],
  [{'f': "Environ 60 % de la croissance française des Trente Glorieuses "
         "s’explique par la productivité globale des facteurs, soit 3,1 points "
         "sur 5,2 % de croissance totale.",
    'p': "Le chiffre caractérise la croissance des Trente Glorieuses comme "
         "intensive et fournit l’exemple canonique de la décomposition."},
   {'f': "De 2010 à 2021, la croissance apparaît plutôt intensive au Danemark et "
         "en Allemagne, plutôt extensive en France et aux États-Unis.",
    'p': "La comparaison montre que la distinction reste opérante aujourd’hui "
         "et qu’elle sépare des trajectoires nationales contemporaines."}],
  [{'q': "Sujet du type « L’accumulation du capital suffit-elle à expliquer la "
         "croissance ? »",
    'f': "La décomposition répond négativement et quantifie l’insuffisance : "
         "lorsque l’on attribue au travail et au capital leur contribution "
         "respective, il reste un résidu considérable — environ 60 % de la "
         "croissance française des Trente Glorieuses — que l’accumulation "
         "n’explique pas.",
    'r': "On part de la mesure avant de passer à la théorie : le résidu est un "
         "fait comptable qui appelle une explication, et c’est cette exigence "
         "qui produit successivement Solow puis les théories endogènes.",
    'ex': "Les 3,1 points de productivité globale des facteurs sur 5,2 % de "
          "croissance calculés par Carré, Dubois et Malinvaud."},
   {'q': "Sujet du type « Sommes-nous condamnés au ralentissement de la "
         "croissance ? »",
    'f': "La réponse dépend du régime de croissance : une croissance extensive "
         "se heurte nécessairement à la démographie et aux rendements "
         "décroissants, tandis qu’une croissance intensive n’a pas de borne "
         "mécanique — mais rien ne garantit que les gains de productivité se "
         "maintiennent, ce que soutient précisément Robert Gordon.",
    'r': "Distinguer la borne mécanique de l’extensif et l’incertitude de "
         "l’intensif permet de répondre sans trancher entre optimisme et "
         "pessimisme.",
    'ex': "La France et les États-Unis, en croissance plutôt extensive de 2010 "
          "à 2021, face au Danemark et à l’Allemagne."}],
  voisins=['n1-croissance', 'n1-pgf', 'n1-accumulation', 'n1-progres-technique',
           'n1-stagnation'])

d('n1-accumulation', 1, "Accumulation du capital",
  "Le moteur le plus immédiat de la croissance, et celui qui s’épuise",
  "L’accumulation du capital désigne l’augmentation du stock de capital "
  "productif d’une économie — machines, bâtiments, équipements, "
  "infrastructures — sous l’effet de l’investissement net, c’est-à-dire de "
  "l’investissement diminué de l’amortissement. Elle constitue le mécanisme de "
  "croissance le plus directement identifiable, et celui dont les modèles ont "
  "montré les limites les plus nettes.",
  "Le raisonnement part d’une évidence : davantage de capital par travailleur "
  "permet de produire davantage. Harrod et Domar en tirent un modèle où la "
  "croissance dépend directement du taux d’investissement et de l’efficacité "
  "du capital, ce qui place l’accumulation au centre de la dynamique "
  "économique. Mais ce modèle conclut aussi à l’instabilité : rien ne garantit "
  "que le taux de croissance effectif coïncide avec celui qu’exigerait le plein "
  "emploi, d’où l’image du fil du rasoir. Solow introduit ensuite l’hypothèse "
  "décisive : les rendements du capital sont décroissants. À technologie "
  "inchangée, chaque unité de capital ajoutée à un volume de travail constant "
  "produit un supplément de production de plus en plus faible. L’économie "
  "converge donc vers un état stationnaire où l’investissement net devient nul "
  "et où la croissance par tête s’arrête. La conséquence est fondamentale : "
  "l’accumulation du capital explique la croissance de transition, non la "
  "croissance de long terme. C’est précisément ce vide que le progrès "
  "technique, exogène chez Solow, vient combler — et que les théories "
  "endogènes chercheront ensuite à expliquer, en montrant que certains types de "
  "capital, humain, public ou technologique, échappent aux rendements "
  "décroissants.",
  [("De l’épargne à l’investissement",
    "Une partie du revenu n’est pas consommée et peut financer l’acquisition de "
    "biens de production. Le taux d’épargne détermine donc, pour une efficacité "
    "donnée du capital, le rythme de l’accumulation."),
   ("De l’investissement au stock de capital",
    "L’investissement net — brut moins amortissement — accroît le stock "
    "productif. Une partie de l’investissement sert seulement à remplacer le "
    "capital usé et ne contribue pas à l’accumulation."),
   ("Du capital à la production",
    "Un stock de capital plus élevé par travailleur élève la productivité du "
    "travail et donc la production. C’est le canal direct de l’accumulation "
    "vers la croissance."),
   ("Les rendements décroissants et l’état stationnaire",
    "À technologie constante, l’efficacité marginale du capital diminue à "
    "mesure qu’il s’accumule. L’investissement finit par ne plus faire que "
    "compenser l’amortissement, et la croissance par tête s’annule.")],
  [{'a': "L’accumulation est le levier de croissance le plus rapidement "
         "mobilisable, notamment pour une économie en rattrapage dont le stock "
         "de capital est faible.",
    'cond': "Il faut une capacité d’épargne ou un accès au financement extérieur, "
            "et des projets d’investissement dont le rendement excède le coût du "
            "capital.",
    'lim': "Le rendement élevé du capital dans les économies pauvres suppose "
           "aussi des institutions capables de protéger l’investissement, ce que "
           "l’accumulation seule ne fournit pas."},
   {'a': "Un taux d’investissement élevé accélère la convergence vers le niveau "
         "de production de long terme, ce qui explique les rattrapages rapides.",
    'cond': "La convergence prédite par Solow est conditionnelle : elle suppose "
            "que les pays partagent les mêmes paramètres structurels — taux "
            "d’épargne, démographie, technologie.",
    'lim': "Elle ne décrit qu’un rattrapage vers un état stationnaire, pas une "
           "croissance durable : une fois la convergence achevée, le moteur "
           "s’éteint."},
   {'a': "L’accumulation incorpore le progrès technique, puisque les machines "
         "nouvelles sont plus efficaces que celles qu’elles remplacent.",
    'cond': "Cet effet suppose que l’investissement porte sur des équipements "
            "récents et que la main-d’œuvre soit capable de les utiliser.",
    'lim': "Attribuer à l’accumulation ce qui relève du progrès technique "
           "incorporé brouille la décomposition : le capital et la technologie "
           "ne sont alors plus séparables."}],
  [{'t': "L’accumulation ne peut pas expliquer la croissance de long terme, car "
         "les rendements décroissants la condamnent à s’épuiser.",
    'qui': "Résultat central du modèle de Robert Solow.",
    'rep': "C’est précisément ce résultat qui donne sa place au progrès "
           "technique, et qui rend nécessaires les théories endogènes : la "
           "critique n’élimine pas l’accumulation, elle en borne la portée."},
   {'t': "Le modèle fondé sur l’accumulation est instable : rien n’assure que la "
         "croissance effective rejoigne celle qui maintiendrait le plein emploi.",
    'qui': "Roy Harrod et Evsey Domar, avec l’image du fil du rasoir.",
    'rep': "L’instabilité découle d’hypothèses rigides sur les coefficients de "
           "production ; elle rappelle néanmoins qu’un sentier de croissance "
           "équilibré n’a rien de spontané."},
   {'t': "Tout capital n’est pas soumis aux mêmes rendements : le capital "
         "humain, public ou technologique peut échapper à la décroissance.",
    'qui': "Théories de la croissance endogène, avec Lucas, Barro et Romer.",
    'rep': "L’objection est décisive et transforme le diagnostic : si certains "
           "capitaux présentent des rendements non décroissants, "
           "l’accumulation redevient un moteur durable, à condition d’être "
           "orientée vers eux."}],
  [{'n': "Roy Harrod",
    'i': "La croissance dépend du taux d’investissement et de l’efficacité du "
         "capital, mais le sentier d’équilibre est instable.",
    'p': "L’image du fil du rasoir traduit l’idée qu’un écart, même faible, "
         "entre croissance effective et croissance garantie tend à s’amplifier "
         "au lieu de se corriger."},
   {'n': "Evsey Domar",
    'i': "L’investissement a un double effet : il soutient la demande "
         "aujourd’hui et accroît les capacités de production demain.",
    'p': "Cette dualité est au cœur du modèle Harrod-Domar : pour que les "
         "capacités nouvelles soient utilisées, la demande doit croître au "
         "rythme exact de leur augmentation, ce qui n’a aucune raison de se "
         "produire spontanément."},
   {'n': "Robert Solow",
    'i': "Les rendements décroissants du capital conduisent l’économie vers un "
         "état stationnaire.",
    'p': "L’accumulation explique la croissance pendant la transition, mais la "
         "croissance par tête de long terme dépend entièrement du progrès "
         "technique, que le modèle laisse inexpliqué."}],
  [{'f': "Dans la décomposition de la croissance française des Trente "
         "Glorieuses, la contribution des facteurs — dont le capital — explique "
         "environ 40 % de la croissance, le reste relevant de la productivité "
         "globale des facteurs.",
    'p': "L’ordre de grandeur situe la part réelle de l’accumulation : "
         "substantielle, mais minoritaire, y compris pendant une période de "
         "très fort investissement."},
   {'f': "La croissance est qualifiée d’extensive lorsque la contribution des "
         "facteurs de production domine, comme en France et aux États-Unis de "
         "2010 à 2021.",
    'p': "L’accumulation reste donc aujourd’hui un déterminant majeur de la "
         "croissance de certaines économies avancées, ce qui interdit de la "
         "traiter comme un mécanisme dépassé."}],
  [{'q': "Sujet du type « L’accumulation du capital suffit-elle à expliquer la "
         "croissance ? »",
    'f': "L’accumulation explique la croissance de transition mais non celle de "
         "long terme : les rendements décroissants conduisent l’économie vers "
         "un état stationnaire où l’investissement net s’annule. C’est ce vide "
         "théorique qui donne sa place au progrès technique, puis aux théories "
         "endogènes, qui montrent que certains capitaux échappent à cette "
         "décroissance.",
    'r': "On suit l’enchaînement des modèles comme une suite de réponses à une "
         "insuffisance identifiée, ce qui transforme un catalogue en "
         "démonstration.",
    'ex': "La contribution du capital n’explique qu’une part minoritaire de la "
          "croissance française des Trente Glorieuses."},
   {'q': "Sujet du type « La croissance peut-elle s’entretenir elle-même ? »",
    'f': "Dans un cadre où les rendements du capital sont décroissants, la "
         "réponse est négative : l’accumulation s’épuise. Elle devient positive "
         "dès lors que l’on admet des capitaux à rendements non décroissants — "
         "capital humain chez Lucas, capital public chez Barro, connaissances "
         "chez Romer.",
    'r': "La réponse dépend entièrement d’une hypothèse technique sur les "
         "rendements : l’expliciter permet de montrer que l’opposition entre "
         "les modèles n’est pas idéologique mais analytique.",
    'ex': "Le passage du modèle de Solow aux théories de la croissance "
          "endogène de Lucas, Barro et Romer."}],
  voisins=['n1-investissement', 'n1-croissance', 'n1-endogene',
           'n1-extensive-intensive', 'n1-convergence'])
