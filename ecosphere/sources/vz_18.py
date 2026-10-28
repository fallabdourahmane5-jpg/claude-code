# -*- coding: utf-8 -*-
"""Visualisation 18 — Le marché, les prix et la concurrence (type flux)."""

from vz_base import v, nd, ln

v('vz-marche-prix', 'Le marché, les prix et la concurrence',
  'Chapitre 5 · de la coordination par les prix à la régulation',
  'flux',
  "Le prix est censé coordonner des décisions que personne ne centralise. "
  "Cette visualisation suit la démonstration complète : comment le prix "
  "coordonne, sous quelles hypothèses l’équilibre existe, comment on mesure "
  "le gain obtenu, ce qui se passe lorsque la concurrence est imparfaite, et "
  "ce que la puissance publique peut faire.",
  [("Toujours exhiber les hypothèses",
    "Le résultat d’efficacité n’est pas une propriété du marché en général : "
    "il tient sous les cinq hypothèses de la concurrence pure et parfaite. "
    "Les lever une à une donne le plan du chapitre."),
   ("Mesurer avant de juger",
    "Le surplus est l’instrument : il permet de décomposer l’effet d’une "
    "mesure en transferts et en pertes nettes. C’est ce qui distingue une "
    "démonstration d’une opinion."),
   ("Ne pas confondre les deux problèmes",
    "Le cours distingue les défaillances de marché, qui portent sur la "
    "nature des biens ou de l’information, et la concurrence imparfaite, qui "
    "porte sur la structure du marché. Les remèdes ne sont pas les mêmes.")],
  [
   # ------------------------------------------ colonne 1 : le mécanisme
   nd('coordination', 'La coordination par les prix', 'coeur',
      "Si la demande dépasse l’offre, le prix monte ; dans le cas inverse, il "
      "baisse. Des décisions indépendantes s’accordent sans autorité "
      "centrale.",
      grp=1,
      defi="La coordination par les prix désigne le mécanisme par lequel les "
           "décisions d’une multitude d’agents indépendants s’accordent sans "
           "direction centrale, sous le seul effet des variations de prix. Le "
           "prix devient l’élément central de coordination des décisions "
           "individuelles : il incite les producteurs à ajuster leur "
           "production et les consommateurs à modifier leurs achats.",
      mec=[("Le mécanisme d’ajustement",
            "Si la demande est supérieure à l’offre, le prix augmente ; si "
            "l’offre est supérieure à la demande, le prix diminue. Le prix "
            "est à la fois un résultat de l’échange et son instrument de "
            "coordination."),
           ("Le prix comme signal d’information",
            "Il transmet l’information sur la rareté sans qu’aucun agent "
            "n’ait à connaître l’état de l’ensemble du système : c’est "
            "l’économie d’information qui fait la force du dispositif."),
           ("Les deux fonctions à distinguer",
            "Informer sur la rareté et répartir le produit sont deux "
            "fonctions distinctes : un prix peut bien remplir la première et "
            "produire une répartition jugée inacceptable.")],
      opp=[{'t': "La main visible de la gestion remplace la main invisible "
                 "des forces du marché dans la coordination des flux de "
                 "marchandises.",
            'qui': "Alfred Chandler",
            'rep': "L’objection est empirique plutôt que théorique, et elle "
                   "est la plus précise contre la thèse de la coordination "
                   "par les prix : dans la grande entreprise moderne, la "
                   "coordination passe par la hiérarchie, pas par le prix."}],
      aut=[{'n': "Adam Smith",
            'i': "La poursuite des intérêts individuels conduit, par la main "
                 "invisible, à un résultat collectivement favorable."},
           {'n': "Ronald Coase",
            'i': "Le marché n’est pas gratuit : son fonctionnement engendre "
                 "des coûts de transaction."}],
      termes=['coordination par les prix', 'marche', 'main invisible'],
      dos=['n5-marche', 'n5-coordination']),

   # ------------------------------------------ colonne 2 : l’équilibre
   nd('equilibre', 'L’équilibre et ses trois questions', 'pilier',
      "Existe-t-il ? Est-il stable ? Est-il plausible ? Le cours conclut : "
      "théoriquement possible, pratiquement inaccessible, mathématiquement "
      "instable.",
      grp=2,
      defi="L’équilibre de marché est la situation dans laquelle le prix est "
           "tel que la quantité offerte égale la quantité demandée, de sorte "
           "qu’aucune force ne pousse plus le prix à varier. Le cours en fait "
           "le point d’aboutissement du mécanisme d’ajustement, tout en "
           "consacrant une analyse détaillée aux trois questions qu’il "
           "soulève : son existence, sa stabilité et sa plausibilité.",
      mec=[("La question de l’existence",
            "Walras suppose implicitement que l’offre et la demande se "
            "rencontrent toujours, mais rien ne garantit que les deux courbes "
            "se coupent : avoir autant d’équations que d’inconnues ne suffit "
            "pas, deux droites pouvant ne jamais se croiser."),
           ("Les conditions d’Arrow-Debreu",
            "L’existence d’un équilibre général exige que les fonctions "
            "soient continues et bornées, et sept conditions économiques "
            "précises : le résultat est conditionnel, et ses conditions sont "
            "exigeantes."),
           ("La dotation de survie et son paradoxe",
            "Parmi ces conditions figure la dotation de survie, selon "
            "laquelle chaque agent possède un minimum de ressources au "
            "départ. Or cette dotation suppose une intervention extérieure — "
            "État, Église, institutions — ce qui contredit l’idée que le "
            "marché se suffit à lui-même.")],
      aut=[{'n': "Léon Walras",
            'i': "Le prix s’ajuste jusqu’à l’équilibre, comme sous l’effet "
                 "d’un commissaire-priseur."},
           {'n': "Kenneth Arrow",
            'i': "L’existence d’un équilibre général exige que les fonctions "
                 "soient continues et bornées, et sept conditions économiques "
                 "précises."},
           {'n': "Gérard Debreu",
            'i': "L’existence de l’équilibre ne garantit ni sa stabilité ni "
                 "la convergence du système vers lui."}],
      faits=[{'f': "Le cours conclut qu’on obtient un équilibre "
                   "théoriquement possible, pratiquement inaccessible et "
                   "mathématiquement instable.",
              'p': "La formule en trois temps résume la superposition des "
                   "critiques et fournit une conclusion directement "
                   "utilisable en dissertation."}],
      termes=['equilibre de marche', 'equilibre general',
              'arrow debreu', 'walras'],
      dos=['n5-equilibre', 'n5-cpp']),

   nd('cpp', 'Les cinq hypothèses', 'detail',
      "Atomicité, homogénéité, transparence, libre entrée, libre circulation "
      "des facteurs. Chaque défaillance est la levée de l’une d’elles.",
      grp=2, par='equilibre',
      defi="La concurrence pure et parfaite est le modèle de référence sous "
           "lequel le marché atteint une allocation efficace. Elle repose sur "
           "cinq hypothèses : atomicité des agents, homogénéité du produit, "
           "transparence de l’information, libre entrée et sortie, libre "
           "circulation des facteurs. L’intérêt du modèle n’est pas sa "
           "réalisme mais sa fonction de référence : chaque situation réelle "
           "se décrit par l’hypothèse qui n’y tient pas.",
      mec=[("Atomicité et homogénéité",
            "De nombreux agents de petite taille échangeant un produit "
            "identique : aucun ne peut influencer le prix, chacun est price "
            "taker."),
           ("Transparence et libre entrée",
            "L’information est disponible et nul ne peut empêcher un "
            "concurrent d’entrer : toute rente attire des entrants qui la "
            "font disparaître."),
           ("Le modèle comme grille de diagnostic",
            "Lever l’atomicité donne le pouvoir de marché ; lever la "
            "transparence donne l’asymétrie d’information ; lever la libre "
            "entrée donne les barrières. Le modèle sert à classer les "
            "problèmes réels.")],
      args=[{'a': "Le modèle fournit un étalon mesurable : l’écart au "
                  "résultat concurrentiel se chiffre en perte de surplus, ce "
                  "qui permet d’évaluer une situation plutôt que de la "
                  "commenter.",
             'lim': "Il n’est jamais réalisé : en faire une norme à atteindre "
                    "plutôt qu’un instrument de comparaison conduit à "
                    "prescrire l’impossible."}],
      aut=[{'n': "Vilfredo Pareto",
            'i': "Une situation est optimale lorsqu’on ne peut améliorer le "
                 "sort de l’un sans détériorer celui d’un autre."}],
      termes=['concurrence pure et parfaite', 'atomicite', 'price taker'],
      dos=['n5-cpp', 'n5-pareto']),

   # ------------------------------------------ colonne 3 : mesurer le gain
   nd('surplus', 'Le surplus : mesurer le gain à l’échange', 'pilier',
      "Ce que le consommateur économise, ce que le producteur gagne au-delà "
      "de son prix minimal. Leur somme mesure le bien-être produit.",
      grp=3,
      defi="Le surplus du consommateur correspond à la différence entre ce "
           "qu’il était prêt à payer et ce qu’il paie réellement ; le surplus "
           "du producteur à la différence entre le prix minimal qu’il était "
           "prêt à accepter et le prix obtenu. La somme des deux constitue le "
           "gain total à l’échange, et c’est l’instrument par lequel "
           "l’analyse économique évalue le bien-être produit par un marché.",
      mec=[("Le critère d’efficacité",
            "En concurrence pure et parfaite le surplus total est maximal, il "
            "n’y a ni pénurie ni gaspillage et le bien-être collectif est "
            "maximisé : le surplus fait de l’efficacité un résultat "
            "démontrable."),
           ("Transfert et perte nette",
            "Il faut distinguer ce qui change de mains de ce qui disparaît : "
            "une rente est un transfert, une perte sèche est une destruction "
            "de bien-être que personne ne récupère."),
           ("Un outil transposable",
            "Le même raisonnement s’applique à un droit de douane : il "
            "redistribue du surplus des consommateurs vers les producteurs et "
            "l’État, mais crée deux pertes sèches, une distorsion productive "
            "et une distorsion de consommation.")],
      aut=[{'n': "Arthur Pigou",
            'i': "Le prix de marché ne reflète pas le coût social lorsqu’il "
                 "existe une externalité."}],
      faits=[{'f': "Le monopole entraîne une réduction du surplus du "
                   "consommateur, l’apparition d’une rente de monopole et une "
                   "perte sèche, le triangle d’Harberger.",
              'p': "Les trois effets sont de nature différente : le premier "
                   "est une perte, le deuxième un transfert, le troisième une "
                   "destruction nette de bien-être."}],
      termes=['surplus du consommateur', 'perte seche',
              'triangle de harberger'],
      dos=['n5-surplus', 'n5-efficacite']),

   # ------------------------------------- colonne 4 : la concurrence imparfaite
   nd('monopole', 'Le monopole', 'pilier',
      "Une seule entreprise, price maker : recette marginale égale coût "
      "marginal, donc prix supérieur au coût marginal et quantité trop "
      "faible.",
      grp=4,
      defi="Un monopole est une situation de marché dans laquelle une seule "
           "entreprise produit et vend un bien ou un service, sans substitut "
           "proche, le monopoleur étant price maker. Il maximise son profit "
           "en égalisant recette marginale et coût marginal, ce qui conduit à "
           "un prix supérieur au coût marginal et à une quantité plus faible "
           "que la quantité socialement optimale.",
      mec=[("La règle de maximisation",
            "Le monopoleur applique Rm = Cm, mais sa recette marginale est "
            "inférieure à son prix puisqu’il doit baisser le prix sur toutes "
            "les unités pour en vendre une de plus : d’où un prix supérieur "
            "au coût marginal."),
           ("Le monopole naturel",
            "Il apparaît avec des coûts fixes très élevés, des coûts "
            "marginaux très faibles et des rendements croissants : eau, "
            "électricité, gaz, chemins de fer, télécommunications, réseaux. "
            "La défaillance tient à une technologie de production, non à un "
            "comportement."),
           ("Le monopole temporaire d’innovation",
            "Le brevet donne une exclusivité d’exploitation pour une durée "
            "maximale de vingt ans sur un territoire donné : le monopole y "
            "est borné dans le temps et dans l’espace, ce qui correspond à "
            "l’argument de Schumpeter.")],
      aut=[{'n': "Joseph Schumpeter",
            'i': "La concurrence doit être la règle, mais l’innovation doit "
                 "être protégée."},
           {'n': "Joe Bain",
            'i': "La structure du marché détermine les comportements des "
                 "entreprises, qui déterminent leurs performances."}],
      termes=['monopole', 'monopole naturel', 'brevet', 'price maker'],
      dos=['n5-monopole', 'n2-brevets']),

   nd('structures', 'Oligopole et différenciation', 'detail',
      "Entre le monopole et la concurrence parfaite : peu de vendeurs qui "
      "s’observent, ou des produits que l’on rend différents.",
      grp=4, par='monopole',
      defi="Entre les deux cas extrêmes, le cours situe deux structures "
           "intermédiaires. L’oligopole réunit un petit nombre de vendeurs "
           "dont chacun doit anticiper les réactions des autres : la décision "
           "devient stratégique. La concurrence monopolistique réunit de "
           "nombreux vendeurs qui différencient leur produit, ce qui leur "
           "confère un pouvoir de marché limité mais réel sur leur propre "
           "variété.",
      mec=[("L’interdépendance stratégique",
            "En oligopole, le profit de chacun dépend des décisions des "
            "autres : baisser son prix peut déclencher une guerre des prix, "
            "ce qui explique la fréquence des ententes et la nécessité de les "
            "interdire."),
           ("La différenciation comme source de pouvoir",
            "Rendre son produit non substituable — par la qualité, la marque, "
            "le service — crée une demande propre, moins sensible au prix des "
            "concurrents."),
           ("Le lien structure-comportement-performance",
            "La structure du marché détermine les comportements des "
            "entreprises, qui déterminent leurs performances : le schéma "
            "fournit la grille d’analyse de l’économie industrielle.")],
      aut=[{'n': "Edward Chamberlin",
            'i': "La différenciation des produits confère à chaque vendeur un "
                 "pouvoir de marché limité sur sa propre variété."}],
      termes=['oligopole', 'concurrence monopolistique',
              'differenciation', 'entente'],
      dos=['n5-oligopole', 'n5-concurrence-monopolistique', 'n5-ententes']),

   # ------------------------------------------ colonne 5 : la régulation
   nd('contestables', 'Les marchés contestables', 'debat',
      "Même seule sur son marché, une entreprise peut se comporter comme si "
      "elle était en concurrence — si l’entrée reste possible.",
      grp=5,
      defi="La théorie des marchés contestables soutient que ce n’est pas le "
           "nombre de concurrents effectivement présents qui discipline une "
           "entreprise, mais la possibilité crédible qu’un concurrent entre. "
           "Même seule sur son marché, une entreprise peut se comporter comme "
           "si elle était en concurrence, dès lors que l’entrée et la sortie "
           "sont peu coûteuses.",
      mec=[("La menace plutôt que la présence",
            "Si l’entrée est libre et la sortie sans coût irrécupérable, tout "
            "profit anormal attire un entrant : l’entreprise installée "
            "anticipe et renonce d’elle-même à exploiter sa position."),
           ("Le rôle décisif des coûts irrécupérables",
            "Ce qui bloque l’entrée n’est pas le capital à engager mais la "
            "part qu’on ne peut pas récupérer en sortant : c’est elle qui "
            "transforme une position en rente durable.")],
      args=[{'a': "La théorie déplace la cible de la politique de la "
                  "concurrence : il faut agir sur les barrières à l’entrée "
                  "plutôt que sur la taille ou sur le nombre d’acteurs.",
             'lim': "Elle suppose une entrée réellement crédible et "
                    "instantanée, condition rarement remplie lorsque "
                    "l’activité exige des investissements lourds et "
                    "spécifiques."}],
      aut=[{'n': "William Baumol",
            'i': "Même seule sur son marché, une entreprise peut se comporter "
                 "comme si elle était en concurrence."}],
      termes=['marches contestables', 'barriere a l entree',
              'couts irrecuperables'],
      dos=['n5-contestables', 'n5-barrieres']),

   nd('politique', 'La politique de la concurrence', 'sortie',
      "Interdire les ententes, contrôler les concentrations, ouvrir l’accès : "
      "l’instrument vise les entraves, pas la réussite.",
      grp=5,
      defi="La politique de la concurrence est l’ensemble des règles et des "
           "interventions destinées à préserver le fonctionnement "
           "concurrentiel des marchés. Elle ne sanctionne pas la taille ni le "
           "profit, qui peuvent résulter d’une efficacité supérieure, mais "
           "les comportements et les structures qui ferment l’accès au "
           "marché.",
      mec=[("L’interdiction des ententes",
            "Un accord entre concurrents sur les prix ou les quantités "
            "reproduit l’effet d’un monopole sans sa justification "
            "technologique : c’est le comportement le plus directement "
            "sanctionné."),
           ("Le contrôle des concentrations",
            "L’examen préalable d’une fusion évalue l’effet probable sur la "
            "concurrence : l’intervention est ex ante, ce qui évite d’avoir à "
            "défaire après coup une structure installée."),
           ("La régulation du monopole naturel",
            "Lorsque la technologie impose un opérateur unique, la "
            "concurrence ne peut pas être rétablie : on régule alors le prix "
            "et l’accès au réseau plutôt que de fractionner l’entreprise.")],
      args=[{'a': "Cibler les entraves plutôt que la taille permet de "
                  "préserver les gains d’échelle tout en maintenant la "
                  "pression concurrentielle.",
             'lim': "La règle produite est exposée à la capture : les "
                    "barrières protectrices prennent souvent la forme de "
                    "licences ou de normes justifiées par l’intérêt général."}],
      aut=[{'n': "Philippe Aghion",
            'i': "Certaines grandes entreprises peuvent freiner l’innovation "
                 "en empêchant l’entrée de nouveaux concurrents."}],
      termes=['politique de la concurrence', 'ententes',
              'controle des concentrations'],
      dos=['n5-politique-concurrence', 'n5-concentration']),

   nd('defaillances', 'Quand le prix ne peut plus coordonner', 'limite',
      "Monopole naturel, biens collectifs et communs, externalités, asymétrie "
      "d’information : les quatre situations où le marché échoue.",
      grp=5,
      defi="Une défaillance de marché est une situation dans laquelle le "
           "marché concurrentiel n’arrive pas à allouer de façon optimale les "
           "ressources : on produit trop ou pas assez, trop cher ou pas assez "
           "cher. Le cours en recense quatre : monopole naturel, biens "
           "collectifs et biens communs, externalités, asymétrie "
           "d’information. Il distingue par ailleurs ce problème de celui de "
           "la concurrence imparfaite.",
      mec=[("Deux problèmes distincts",
            "La défaillance porte sur la nature des biens ou de "
            "l’information ; la concurrence imparfaite porte sur la structure "
            "du marché. Les confondre conduit à prescrire le mauvais "
            "remède."),
           ("Une cause, un remède",
            "Chaque défaillance a une cause distincte — absence de prix pour "
            "un effet, impossibilité d’exclure, inégale information, "
            "technologie à rendements croissants — et appelle un instrument "
            "différent."),
           ("L’inefficacité en quantité et en prix",
            "La définition du cours couvre les deux sens : on peut produire "
            "la mauvaise quantité, ou la bonne quantité au mauvais prix. "
            "L’inefficacité ne se réduit pas à la pénurie.")],
      termes=['defaillance de marche', 'externalite', 'bien collectif',
              'asymetrie d information'],
      dos=['n5-marche', 'n6-externalites', 'n6-biens-collectifs']),
  ],
  [
   ln('coordination', 'equilibre', 'aboutit à',
      "Le mécanisme d’ajustement n’a de sens que s’il mène quelque part : "
      "l’équilibre est le point où aucune force ne pousse plus le prix à "
      "varier. Encore faut-il qu’il existe, qu’il soit stable et qu’il soit "
      "atteignable.", 'cause'),
   ln('equilibre', 'cpp', 'tient sous',
      "Le résultat d’efficacité n’est pas une propriété du marché en "
      "général : il tient sous les cinq hypothèses de la concurrence pure et "
      "parfaite. Les énoncer, c’est déjà annoncer les cas où il tombe.",
      'conditionne'),
   ln('cpp', 'surplus', 'maximise',
      "En concurrence pure et parfaite le surplus total est maximal, sans "
      "pénurie ni gaspillage : c’est cette propriété qui fait du modèle une "
      "référence et non une description.", 'cause'),
   ln('surplus', 'coordination', 'mesure le gain de',
      "Le surplus donne le contenu du bénéfice que la coordination par les "
      "prix est censée produire : sans lui, l’efficacité resterait une "
      "affirmation.", 'mesure'),
   ln('cpp', 'monopole', 'tombe avec l’atomicité',
      "Lever l’hypothèse d’atomicité suffit : l’entreprise cesse d’être price "
      "taker, sa recette marginale devient inférieure à son prix, et la "
      "quantité produite tombe sous l’optimum social.", 'limite'),
   ln('monopole', 'surplus', 'se chiffre par',
      "Réduction du surplus du consommateur, rente de monopole, triangle "
      "d’Harberger : le surplus permet de distinguer ce qui est perdu, ce qui "
      "est transféré et ce qui est détruit.", 'mesure'),
   ln('monopole', 'structures', 'se décline en',
      "Entre le monopole et la concurrence parfaite, l’oligopole et la "
      "concurrence monopolistique décrivent des pouvoirs de marché partiels, "
      "obtenus par le petit nombre ou par la différenciation.", 'cause'),
   ln('structures', 'politique', 'appelle la surveillance des ententes',
      "En oligopole, le profit de chacun dépend des décisions des autres : "
      "l’entente devient la solution rationnelle pour les firmes, ce qui en "
      "fait le comportement le plus directement sanctionné.", 'cause'),
   ln('contestables', 'monopole', 'relativise',
      "Si l’entrée est crédible, une entreprise seule se comporte comme si "
      "elle était en concurrence : ce n’est pas le nombre d’acteurs présents "
      "qui discipline, mais la possibilité d’en voir arriver un autre.",
      'oppose'),
   ln('contestables', 'politique', 'redéfinit la cible de',
      "La politique de la concurrence doit viser les barrières à l’entrée — "
      "et notamment les coûts irrécupérables — plutôt que la taille ou le "
      "profit, qui peuvent résulter d’une efficacité supérieure.",
      'conditionne'),
   ln('monopole', 'defaillances', 'devient naturel et donc',
      "Avec des coûts fixes très élevés et des rendements croissants, un "
      "seul opérateur est moins coûteux que plusieurs : la défaillance tient "
      "à la technologie, et la concurrence ne peut pas être rétablie.",
      'cause'),
   ln('defaillances', 'coordination', 'suspend',
      "Lorsque le prix ne peut pas se former — faute de pouvoir exclure — ou "
      "qu’il ne reflète pas tous les effets, le signal devient faux : la "
      "coordination par les prix cesse d’être efficace.", 'limite'),
   ln('defaillances', 'politique', 'appelle d’autres instruments que',
      "La politique de la concurrence traite la structure du marché. Les "
      "défaillances portant sur la nature des biens ou de l’information "
      "appellent d’autres instruments : taxation, réglementation, "
      "financement public.", 'oppose'),
   ln('equilibre', 'defaillances', 'suppose une dotation qu’il n’explique pas',
      "La dotation de survie figure parmi les conditions d’existence de "
      "l’équilibre général, mais elle suppose une intervention extérieure — "
      "État, Église, institutions — ce qui contredit l’idée que le marché se "
      "suffit à lui-même.", 'limite'),
   ln('politique', 'cpp', 'cherche à s’en rapprocher',
      "L’objectif n’est pas d’atteindre la concurrence pure et parfaite, qui "
      "n’est jamais réalisée, mais de réduire l’écart mesurable entre la "
      "situation observée et le résultat qu’elle décrit.", 'renforce'),
  ],
  bandes=[(1, 'Le mécanisme'), (2, 'L’équilibre et ses conditions'),
          (3, 'Mesurer le gain'), (4, 'La concurrence imparfaite'),
          (5, 'Réguler')],
  fam='Marché, État et théories')
