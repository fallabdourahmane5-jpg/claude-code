# -*- coding: utf-8 -*-
"""Ensemble 14 — L’inflation et la stabilité des prix (1/4)."""

from doss_base import d

d('n14-inflation', 14, "Inflation",
  "L’augmentation du niveau général des prix, et ce qu’elle déplace",
  "Le cours définit l’inflation comme l’augmentation du niveau général des "
  "prix. Son instrument de mesure est l’indice des prix à la consommation, "
  "qui estime entre deux périodes la variation moyenne des prix des produits "
  "consommés par les ménages, à partir d’un panier fixe de biens et services "
  "actualisé chaque année et d’un relevé portant sur deux cent mille prix.",
  "Le cours traite l’inflation à deux endroits qui se complètent, et c’est "
  "leur articulation qui donne la notion complète. Le premier est la mesure. "
  "L’inflation est l’augmentation du niveau général des prix, et l’indice des "
  "prix à la consommation en est l’instrument : il repose sur un panier fixe "
  "de biens et services, actualisé chaque année, et sur un relevé de deux "
  "cent mille prix. Le cours ajoute un raffinement important, l’inflation "
  "sous-jacente, calculée en excluant les éléments volatils tels que les prix "
  "de l’énergie et des aliments : contrairement à l’inflation globale, qui "
  "peut être affectée par des facteurs temporaires, elle offre une vision "
  "plus stable et durable des tendances inflationnistes. Le cours fixe aussi "
  "le vocabulaire des degrés : une inflation à deux chiffres est une "
  "hyperinflation, une baisse de l’inflation est une désinflation, une baisse "
  "des prix est une déflation. Le second endroit est l’explication. Le cours "
  "donne une cause générale, la demande augmente plus vite que l’offre, et "
  "une cause monétaire reprise de la tradition classique : Jean Bodin "
  "observe dès le seizième siècle que trop de monnaie égale inflation, "
  "Irving Fisher formule l’équation selon laquelle la quantité de monnaie "
  "détermine le niveau général des prix, et Friedman modernise la thèse en "
  "affirmant que l’inflation est toujours et partout un phénomène monétaire, "
  "puisque si la quantité de monnaie croît plus vite que la production, les "
  "prix augmentent. Le cours donne le canal contemporain de cette logique : "
  "un crédit trop dynamique entraîne une masse monétaire en hausse, donc une "
  "demande plus forte, donc des tensions sur les prix, donc l’inflation. Les "
  "effets, enfin, sont présentés comme ambivalents sur l’épargne : l’effet "
  "d’encaisse réelle, ou effet Pigou, veut que pour conserver la valeur de "
  "leur patrimoine les individus soient incités à épargner davantage en "
  "période d’inflation, donc à réduire leurs dépenses ; la fuite devant la "
  "monnaie veut au contraire qu’ils préfèrent acheter et consommer "
  "aujourd’hui, avant que les effets de l’inflation prennent place. Le cours "
  "tranche empiriquement : en France, on a pu constater que l’effet "
  "d’encaisse réelle était le plus fréquent. C’est pourquoi la stabilité des "
  "prix est l’objectif central des banques centrales modernes, la Banque "
  "centrale européenne visant une inflation autour de deux pour cent à moyen "
  "terme.",
  [("La mesure par un panier fixe",
    "L’indice des prix à la consommation estime entre deux périodes la "
    "variation moyenne des prix des produits consommés par les ménages, à "
    "partir d’un panier fixe actualisé chaque année et d’un relevé de deux "
    "cent mille prix."),
   ("La distinction entre valeur et volume",
    "Les grandeurs économiques peuvent être exprimées en valeur courante, "
    "aux prix de l’année en cours ; pour comparer dans le temps on déflate, "
    "c’est-à-dire qu’on calcule en volume, à prix constants."),
   ("La cause réelle : demande contre offre",
    "Le cours énonce la cause générale de l’inflation : la demande augmente "
    "plus vite que l’offre, ce qui apparaît aussi dans le vocabulaire de la "
    "croissance sous la forme d’un output gap positif et de tensions "
    "inflationnistes."),
   ("La cause monétaire",
    "Si la création monétaire et le crédit progressent trop rapidement par "
    "rapport à la production, des tensions inflationnistes apparaissent : un "
    "crédit trop dynamique, une masse monétaire en hausse, une demande plus "
    "forte, des tensions sur les prix."),
   ("Les deux réactions possibles de l’épargnant",
    "L’effet d’encaisse réelle pousse à épargner davantage pour conserver la "
    "valeur du patrimoine, donc à réduire les dépenses ; la fuite devant la "
    "monnaie pousse au contraire à acheter immédiatement."),
   ("La réponse de politique monétaire",
    "La stabilité des prix étant l’objectif central des banques centrales "
    "modernes, la banque centrale resserre les conditions du crédit pour "
    "ramener l’inflation vers sa cible, autour de deux pour cent à moyen "
    "terme dans la zone euro.")],
  [{'a': "Mesurer l’inflation par un indice permet de comparer les revenus "
         "dans le temps et de calculer le pouvoir d’achat.",
    'cond': "La comparaison suppose un panier représentatif de la "
            "consommation effective des ménages, ce que le cours assure par "
            "une actualisation annuelle.",
    'lim': "Un panier fixe lisse mal les changements de comportement : il "
           "mesure l’évolution du prix d’une consommation de référence, non "
           "celle de la consommation réellement effectuée."},
   {'a': "La notion d’inflation sous-jacente améliore le diagnostic en "
         "isolant la tendance de fond des variations purement temporaires.",
    'cond': "Elle suppose que les prix de l’énergie et des aliments soient "
            "bien les éléments volatils, affectés par des facteurs "
            "temporaires.",
    'lim': "Un choc durable sur l’énergie disparaît alors de l’indicateur "
           "alors qu’il pèse réellement sur les ménages, ce que le cours "
           "illustre par les chocs pétroliers."},
   {'a': "L’explication monétaire donne une cause unique et un levier "
         "clair : contrôler la croissance de la masse monétaire.",
    'cond': "Elle exige, comme Friedman le suppose, une vitesse de "
            "circulation et un volume de transactions stables, et une offre "
            "de monnaie décidée par les autorités monétaires.",
    'lim': "Le cours montre que dans les économies contemporaines la "
           "création monétaire dépend largement du crédit bancaire : la "
           "quantité de monnaie n’est pas décidée de l’extérieur mais naît de "
           "la demande de crédit."},
   {'a': "L’explication par la demande relie l’inflation au cycle et au degré "
         "d’utilisation des capacités productives disponibles.",
    'cond': "Elle suppose que les capacités soient déjà pleinement "
            "utilisées, situation que le cours repère par un output gap "
            "positif.",
    'lim': "Elle n’explique pas l’inflation accompagnée de chômage, que le "
           "cours constate dans les années soixante-dix sous le nom de "
           "stagflation."},
   {'a': "L’ambivalence des effets sur l’épargne est tranchée "
         "empiriquement, ce qui évite de rester au stade des hypothèses.",
    'cond': "La conclusion suppose que la vérification porte bien sur le "
            "comportement dominant, le cours observant que l’effet "
            "d’encaisse réelle était le plus fréquent en France.",
    'lim': "Un résultat national et daté ne se généralise pas : la fuite "
           "devant la monnaie reste le comportement attendu lorsque "
           "l’inflation devient très élevée."}],
  [{'t': "L’inflation est toujours et partout un phénomène monétaire : seule "
         "la quantité de monnaie l’explique.",
    'qui': "Milton Friedman, dans l’énoncé de la théorie quantitative de la "
           "monnaie que le cours date de 1956.",
    'rep': "Le cours objecte avec Keynes que la monnaie n’est pas neutre et "
           "que la demande globale détermine la production : si la demande "
           "est insuffisante, une création monétaire supplémentaire peut être "
           "thésaurisée sans faire monter les prix."},
   {'t': "La monnaie n’est qu’un voile : elle influence le niveau général des "
         "prix, jamais la production ni l’emploi.",
    'qui': "Jean Bodin, Ricardo et Say, que le cours réunit sous les "
           "arguments des auteurs classiques.",
    'rep': "Le cours oppose la position keynésienne et celle de Hayek : la "
           "monnaie influence la production et l’emploi, et une création "
           "excessive abaisse artificiellement les taux et provoque un "
           "surinvestissement."},
   {'t': "La dette publique n’est pas un problème pour un État souverain "
         "monétairement : le seul risque réel est l’inflation.",
    'qui': "Stephanie Kelton, représentante de la théorie monétaire moderne "
           "que le cours présente.",
    'rep': "Le cours relève que ce risque n’est pas mineur : il mentionne "
           "l’aléa moral public, l’État n’ayant plus d’incitation à maîtriser "
           "le déficit, et le risque inflationniste de dépenses financées par "
           "création monétaire sans contrepartie productive immédiate."},
   {'t': "Une inflation modérée est utile : elle allège les dettes et permet "
         "de réduire le chômage.",
    'qui': "La lecture keynésienne de la courbe de Phillips, dominante dans "
           "les années cinquante et soixante selon le cours.",
    'rep': "Le cours montre que cette lecture est démentie par les années "
           "soixante-dix : la stagflation associe inflation et chômage élevé, "
           "ce qui détruit expérimentalement la courbe de Phillips."}],
  [{'n': "Jean Bodin",
    'i': "Trop de monnaie égale inflation : la monnaie influence les prix "
         "mais pas la production.",
    'p': "Le cours le place au seizième siècle parmi les auteurs classiques "
         "de la neutralité : il reconnaît que le commerce passe par la "
         "monnaie, mais observe que son accumulation fait monter les prix, "
         "d’où l’idée que la monnaie n’est qu’un voile posé sur l’économie "
         "réelle."},
   {'n': "Irving Fisher",
    'i': "La quantité de monnaie détermine uniquement le niveau général des "
         "prix, sans influencer durablement la production.",
    'p': "Le cours donne son équation, le produit de la quantité de monnaie "
         "et de sa vitesse de circulation égalant le produit du niveau des "
         "prix et du volume des transactions : la vitesse et le volume étant "
         "stables, les prix varient proportionnellement à la monnaie."},
   {'n': "Milton Friedman",
    'i': "L’inflation est toujours et partout un phénomène monétaire, "
         "puisque la monnaie seule détermine les prix à long terme.",
    'p': "Le cours date son énoncé de 1956 et en détaille les thèses : la "
         "monnaie est exogène, à long terme elle est neutre, et il observe "
         "une relation stable entre les agrégats monétaires et le niveau des "
         "prix sur longue période, d’où sa règle de contrôle de la croissance "
         "de la masse monétaire."},
   {'n': "Arthur Pigou",
    'i': "L’effet d’encaisse réelle pousse à épargner davantage en période "
         "d’inflation.",
    'p': "Le cours nomme ce mécanisme effet d’encaisse réelle ou effet "
         "Pigou : pour conserver la valeur de leur patrimoine, les individus "
         "sont incités à épargner plus donc à réduire leurs dépenses, et le "
         "cours ajoute qu’en France ce comportement s’est révélé le plus "
         "fréquent."}],
  [{'f': "L’indice des prix à la consommation repose sur un panier fixe "
         "actualisé chaque année et sur un relevé portant sur deux cent mille "
         "prix.",
    'p': "Le chiffre montre l’ampleur du dispositif statistique nécessaire "
         "pour mesurer une grandeur moyenne : l’inflation n’est pas observée "
         "directement, elle est construite."},
   {'f': "Le cours fixe les seuils de vocabulaire : inflation à deux "
         "chiffres égale hyperinflation, baisse de l’inflation égale "
         "désinflation, baisse des prix égale déflation.",
    'p': "Cette gradation démontre que le phénomène est continu et que le "
         "diagnostic dépend du degré : les quatre mots désignent des "
         "situations qui n’appellent pas les mêmes politiques."},
   {'f': "Dans la zone euro, la Banque centrale européenne vise une "
         "inflation autour de deux pour cent à moyen terme.",
    'p': "Le repère montre que la stabilité des prix ne signifie pas prix "
         "constants : une inflation faible et prévisible est préférée à "
         "l’absence d’inflation, que le cours associe au risque de "
         "déflation."},
   {'f': "Le cours donne l’exemple du salaire qui augmente de deux pour cent "
         "quand les prix augmentent de trois pour cent : le pouvoir d’achat "
         "baisse.",
    'p': "L’exemple démontre que l’inflation agit par comparaison entre deux "
         "évolutions : c’est l’écart entre revenu nominal et prix qui "
         "détermine le gain ou la perte réelle."}],
  [{'q': "Sujet sur la mesure de l’inflation et ses limites",
    'f': "L’inflation est une construction statistique avant d’être un "
         "phénomène observé. Le cours définit l’indice des prix à la "
         "consommation comme l’instrument de mesure de l’inflation, qui "
         "estime entre deux périodes données la variation moyenne des prix "
         "des produits consommés par les ménages, à partir d’un panier fixe "
         "de biens et services actualisé chaque année et d’un relevé portant "
         "sur deux cent mille prix.",
    'r': "On montre que la mesure suppose des choix, le périmètre du panier "
         "et sa fixité, ce qui explique les écarts entre inflation mesurée et "
         "inflation ressentie.",
    'ex': "L’inflation sous-jacente, calculée en excluant les éléments "
          "volatils tels que les prix de l’énergie et des aliments."},
   {'q': "Sujet sur les causes de l’inflation",
    'f': "Le cours donne deux causes qu’il ne hiérarchise pas. La cause "
         "réelle est que la demande augmente plus vite que l’offre. La cause "
         "monétaire est formulée par Friedman : l’inflation est toujours et "
         "partout un phénomène monétaire, car si la quantité de monnaie croît "
         "plus vite que la production, les prix augmentent. Le canal "
         "contemporain réunit les deux : un crédit trop dynamique accroît la "
         "masse monétaire, donc la demande, donc les prix.",
    'r': "On montre que les deux explications se rejoignent par le crédit, "
         "qui est à la fois création monétaire et financement de la demande, "
         "ce qui évite d’opposer abstraitement le réel et le monétaire.",
    'ex': "L’enchaînement du cours : crédit trop dynamique, masse monétaire "
          "en hausse, demande plus forte, tensions sur les prix, inflation."},
   {'q': "Sujet sur les effets de l’inflation sur les comportements",
    'f': "L’inflation ne pousse pas les agents dans une seule direction. Le "
         "cours oppose deux effets : l’effet d’encaisse réelle, ou effet "
         "Pigou, selon lequel pour conserver la valeur de leur patrimoine les "
         "individus épargnent davantage donc réduisent leurs dépenses ; et la "
         "fuite devant la monnaie, selon laquelle ils préfèrent acheter et "
         "consommer aujourd’hui avant que les effets de l’inflation prennent "
         "place. Le cours tranche : en France, l’effet d’encaisse réelle "
         "s’est révélé le plus fréquent.",
    'r': "On montre que la direction de l’effet dépend du niveau anticipé de "
         "l’inflation, ce qui permet de conclure sans choisir abstraitement "
         "entre les deux mécanismes.",
    'ex': "La vérification empirique française citée par le cours en faveur "
          "de l’effet d’encaisse réelle."},
   {'q': "Sujet sur la stabilité des prix comme objectif",
    'f': "La stabilité des prix est devenue l’objectif central des banques "
         "centrales modernes. Le cours en donne la logique : si la création "
         "monétaire et le crédit progressent trop rapidement par rapport à la "
         "production, des tensions inflationnistes peuvent apparaître. Il "
         "ajoute le repère chiffré, une inflation autour de deux pour cent à "
         "moyen terme dans la zone euro, ce qui montre que l’objectif n’est "
         "pas l’absence d’inflation mais son caractère faible et prévisible.",
    'r': "On montre que la cible est un compromis entre deux risques "
         "symétriques, l’emballement des prix et la déflation, ce qui "
         "explique qu’elle soit positive et non nulle.",
    'ex': "Le rôle de la Banque centrale européenne tel que le cours le "
          "définit : stabilité des prix, liquidité du système bancaire et "
          "prêteur en dernier ressort."}],
  voisins=['n14-deflation', 'n14-inflation-demande', 'n14-courbe-phillips',
           'n14-pouvoir-achat', 'n11-neutralite-monnaie'])


d('n14-desinflation', 14, "Désinflation",
  "Ralentir la hausse des prix sans la faire basculer en baisse",
  "Le cours définit la désinflation par une formule brève : la baisse de "
  "l’inflation. Il ne s’agit donc pas d’une baisse des prix, qui serait une "
  "déflation, mais d’un ralentissement de leur hausse. L’exemple historique "
  "qu’il mobilise est le choc de taux conduit par Paul Volcker à la tête de "
  "la Réserve fédérale américaine à partir de 1979, dans un contexte "
  "d’inflation élevée.",
  "Le cours aborde la désinflation par la définition puis par un cas, et "
  "c’est ce cas qui en révèle le coût. La définition est posée dans la série "
  "des degrés : une inflation à deux chiffres est une hyperinflation, la "
  "baisse de l’inflation est une désinflation, la baisse des prix est une "
  "déflation. La distinction est décisive pour la lecture des statistiques : "
  "en désinflation, les prix continuent de monter, mais moins vite, et le "
  "pouvoir d’achat continue donc de s’éroder, simplement plus lentement. Le "
  "cas est celui de Volcker. En 1979, il arrive à la tête de la Réserve "
  "fédérale dans un contexte d’inflation élevée et engage une politique "
  "monétaire restrictive, c’est-à-dire une forte hausse des taux d’intérêt. "
  "Le mécanisme suit la logique du canal du crédit que le cours expose "
  "ailleurs : des taux plus élevés renchérissent le crédit, réduisent la "
  "demande de financement, donc la création monétaire et la demande globale, "
  "ce qui fait refluer les tensions sur les prix. Mais le cours s’intéresse "
  "surtout aux conséquences extérieures, et elles sont considérables. Les "
  "taux américains plus élevés rendent les placements américains plus "
  "attractifs, les capitaux mondiaux reviennent massivement vers les "
  "États-Unis, qui deviennent une pompe aspirante à capitaux. Pour les pays "
  "endettés, le choc est double : la hausse des taux renchérit brutalement le "
  "coût de la dette, et comme soixante-dix pour cent de la dette du Tiers "
  "Monde est à taux variable auprès de banques privées, les charges "
  "d’intérêts explosent ; parallèlement le dollar s’apprécie, et comme une "
  "grande partie de la dette des pays en développement est libellée en "
  "dollars, son poids réel augmente. Le cours fait de ces deux chocs "
  "combinés la cause de la crise de la dette latino-américaine qui éclate au "
  "début des années quatre-vingt. La leçon est donc double : la désinflation "
  "est possible, puisque l’instrument monétaire agit bien sur les prix, mais "
  "son coût ne se limite pas à l’économie qui la conduit. Le cours relie "
  "enfin la désinflation à la question de la crédibilité : pour les "
  "monétaristes, la politique monétaire n’est efficace que si les agents "
  "croient à la détermination des autorités, ce qui plaide pour des règles "
  "simples, crédibles et stables dans le temps plutôt que pour des décisions "
  "discrétionnaires.",
  [("Le diagnostic d’inflation élevée",
    "Le point de départ est une inflation jugée excessive et durable, ce que "
    "le cours décrit pour les États-Unis de la fin des années soixante-dix, "
    "après les deux chocs pétroliers."),
   ("Le resserrement monétaire",
    "La banque centrale relève fortement ses taux directeurs : le cours "
    "parle d’une politique monétaire restrictive, et Volcker engage une forte "
    "hausse des taux d’intérêt."),
   ("La contraction du crédit et de la demande",
    "Des taux plus élevés renchérissent le crédit, réduisent la demande de "
    "financement, donc la création monétaire et la demande globale : les "
    "tensions sur les prix refluent."),
   ("Le coût en activité",
    "La baisse de la demande se paie en production et en emploi : le cours "
    "situe au début des années quatre-vingt l’éclatement d’une crise dont les "
    "causes se construisent à la fin des années soixante-dix."),
   ("L’attraction des capitaux",
    "Les taux américains plus élevés rendent les placements américains plus "
    "attractifs : les capitaux mondiaux reviennent massivement vers les "
    "États-Unis, qui deviennent une pompe aspirante à capitaux."),
   ("Le choc en retour sur les pays endettés",
    "La hausse des taux renchérit la dette à taux variable et "
    "l’appréciation du dollar alourdit la dette libellée en dollars : le "
    "cours fait de ces deux effets la cause de la crise de la dette.")],
  [{'a': "La désinflation démontre que la politique monétaire agit "
         "effectivement sur les prix, ce qui valide le canal du crédit.",
    'cond': "L’argument suppose que la banque centrale puisse renchérir le "
            "refinancement et que les banques répercutent cette hausse sur le "
            "coût du crédit.",
    'lim': "Le cours montre que l’asymétrie est forte : la banque centrale "
           "freine efficacement mais ne peut pas relancer de la même manière, "
           "comme le révèle la trappe à liquidité."},
   {'a': "Elle justifie la priorité donnée à la stabilité des prix, puisque "
         "laisser l’inflation s’installer rend la correction plus coûteuse.",
    'cond': "Le raisonnement suppose que les anticipations s’ajustent à "
            "l’inflation passée, comme dans les anticipations adaptatives de "
            "Friedman.",
    'lim': "Le cours rappelle le dilemme classique : cet objectif peut "
           "entrer en tension avec le soutien de l’activité, entre relancer "
           "et maîtriser l’inflation."},
   {'a': "Elle montre l’intérêt de la crédibilité : une politique crue "
         "atteint son but à moindre coût en activité.",
    'cond': "L’argument exige que les agents connaissent la règle suivie par "
            "les autorités et en intègrent les effets, hypothèse que le cours "
            "rattache aux anticipations rationnelles.",
    'lim': "Dans le cas Volcker, la désinflation a été obtenue par un choc "
           "brutal et non par la seule annonce : la crédibilité a été "
           "construite par le coût payé."},
   {'a': "Elle met en évidence la dimension internationale de la politique "
         "monétaire d’une grande économie.",
    'cond': "La transmission suppose une forte mobilité des capitaux et des "
            "dettes libellées en devise étrangère ou à taux variable.",
    'lim': "Le cours relève que les effets dépendent de la structure de la "
           "dette : la vulnérabilité vient de ce que soixante-dix pour cent "
           "de la dette du Tiers Monde était à taux variable."},
   {'a': "Elle distingue nettement le ralentissement des prix de leur "
         "baisse, ce qui évite un contresens fréquent.",
    'cond': "La distinction suppose de raisonner sur la dérivée et non sur "
            "le niveau : en désinflation les prix montent toujours.",
    'lim': "Une désinflation trop rapide peut déboucher sur la déflation que "
           "le cours range parmi les risques que la banque centrale doit "
           "éviter."}],
  [{'t': "La désinflation est inutilement coûteuse : une inflation modérée "
         "permet de réduire le chômage et d’alléger les dettes.",
    'qui': "La lecture keynésienne de la courbe de Phillips que le cours "
           "présente comme dominante dans les années cinquante et soixante.",
    'rep': "Le cours répond que l’arbitrage n’existe pas durablement : à "
           "long terme la courbe de Phillips devient verticale, et la "
           "stagflation des années soixante-dix a montré que l’on peut avoir "
           "inflation et chômage élevé ensemble."},
   {'t': "Il faut une politique annoncée et graduelle plutôt qu’un choc : "
         "une règle crédible suffit à faire baisser les anticipations.",
    'qui': "Thomas Sargent et la thèse des anticipations rationnelles que le "
           "cours expose.",
    'rep': "Le cours ne tranche pas mais fournit le contre-exemple : la "
           "désinflation américaine a bien pris la forme d’un choc de taux en "
           "1979, et c’est son coût qui a rendu la politique crédible "
           "ensuite."},
   {'t': "Une banque centrale ne devrait pas poursuivre la désinflation sans "
         "considérer ses effets sur les pays tiers.",
    'qui': "L’analyse de la crise de la dette que le cours développe à "
           "propos du choc Volcker.",
    'rep': "Le cours constate le fait sans le résoudre : les économies "
           "bénéficiaires de capitaux étrangers sont exposées aux "
           "retournements des taux d’intérêt internationaux, ce qui est une "
           "contrainte structurelle et non un choix de politique."},
   {'t': "La vraie contrainte n’est pas l’inflation mais la dette publique, "
         "qu’il faut réduire en priorité.",
    'qui': "La position inverse de celle de Stephanie Kelton, telle que le "
           "cours la situe dans le débat.",
    'rep': "Le cours rapporte précisément l’argument de Kelton : pour un "
           "État souverain monétairement, le seul risque réel est "
           "l’inflation, ce qui remet la désinflation au centre plutôt que "
           "le niveau de dette."}],
  [{'n': "Paul Volcker",
    'i': "Une politique monétaire restrictive peut ramener l’inflation, au "
         "prix d’une forte hausse des taux d’intérêt.",
    'p': "Le cours précise qu’il arrive à la tête de la Réserve fédérale "
         "américaine en 1979 dans un contexte d’inflation élevée et engage "
         "une politique de forte hausse des taux, dont il fait l’un des deux "
         "chocs à l’origine de la crise de la dette du début des années "
         "quatre-vingt."},
   {'n': "Milton Friedman",
    'i': "Il faut contrôler la croissance de la masse monétaire par une "
         "règle simple plutôt que par des décisions discrétionnaires.",
    'p': "Le cours résume sa solution en trois points : laisser faire le "
         "marché, laisser le chômage revenir à son niveau naturel, contrôler "
         "la croissance de la masse monétaire selon une règle de pourcentage "
         "constant, puisque la monnaie détermine l’inflation à long terme."},
   {'n': "Thomas Sargent",
    'i': "Les agents connaissent la règle suivie par les autorités et en "
         "intègrent les effets avant qu’ils ne se produisent.",
    'p': "Le cours en tire la préférence pour des règles annoncées plutôt "
         "que pour la discrétion : une politique annoncée n’agit que sur les "
         "variables nominales, ce qui fait de la crédibilité la variable "
         "décisive d’une désinflation."}],
  [{'f': "Paul Volcker arrive à la tête de la Réserve fédérale en 1979 dans "
         "un contexte d’inflation élevée et augmente fortement les taux.",
    'p': "Le fait fournit le cas de référence : il démontre qu’une "
         "désinflation volontaire est possible, et que son instrument "
         "principal est le taux directeur."},
   {'f': "Soixante-dix pour cent de la dette du Tiers Monde était à taux "
         "variable auprès de banques privées au moment du choc de taux.",
    'p': "Le chiffre explique l’ampleur de la transmission : la hausse des "
         "taux américains s’est immédiatement répercutée sur les charges "
         "d’intérêts des pays endettés, dont elle a fait exploser le coût."},
   {'f': "L’appréciation du dollar alourdit le poids réel des dettes des "
         "pays en développement, largement libellées en dollars.",
    'p': "Le second canal montre que la désinflation d’une grande économie "
         "agit aussi par le change : le cours combine les deux chocs pour "
         "expliquer la crise de la dette."},
   {'f': "Les taux américains plus élevés font des États-Unis une pompe "
         "aspirante à capitaux, les capitaux mondiaux revenant massivement "
         "vers eux.",
    'p': "L’image du cours montre que la politique monétaire d’une économie "
         "dominante réoriente l’épargne mondiale : la désinflation d’un pays "
         "assèche le financement des autres."}],
  [{'q': "Sujet sur le coût de la lutte contre l’inflation",
    'f': "Une désinflation réussie n’est pas une désinflation sans coût. Le "
         "cours le montre par le choc Volcker : en 1979, la Réserve fédérale "
         "augmente fortement les taux d’intérêt pour lutter contre une "
         "inflation élevée, et cette hausse renchérit brutalement le coût de "
         "la dette, d’autant que soixante-dix pour cent de la dette du Tiers "
         "Monde est à taux variable auprès de banques privées, de sorte que "
         "les charges d’intérêts explosent.",
    'r': "On distingue le coût interne, en activité et en emploi, du coût "
         "externe, supporté par les pays endettés, pour montrer qu’une "
         "politique nationale peut avoir un prix international.",
    'ex': "La crise de la dette latino-américaine du début des années "
          "quatre-vingt, que le cours rattache au choc Volcker et à "
          "l’appréciation du dollar."},
   {'q': "Sujet sur désinflation et déflation",
    'f': "Confondre désinflation et déflation est l’erreur la plus coûteuse "
         "en matière de diagnostic. Le cours les distingue nettement : la "
         "baisse de l’inflation est une désinflation, la baisse des prix est "
         "une déflation. En désinflation, les prix continuent de monter mais "
         "moins vite, de sorte que le pouvoir d’achat continue de s’éroder "
         "plus lentement ; en déflation, la dynamique s’inverse et la banque "
         "centrale doit chercher à l’éviter.",
    'r': "On raisonne sur la variation de la variation, ce qui permet de "
         "montrer que les deux situations appellent des politiques opposées "
         "bien qu’elles se suivent dans les statistiques.",
    'ex': "Le vocabulaire fixé par le cours : inflation à deux chiffres, "
          "désinflation, déflation."},
   {'q': "Sujet sur la crédibilité de la politique monétaire",
    'f': "La désinflation est l’épreuve où la crédibilité se gagne ou se "
         "perd. Pour Friedman, la solution est de contrôler la croissance de "
         "la masse monétaire par une règle plutôt que par la discrétion ; "
         "pour Sargent, les agents connaissent la règle suivie par les "
         "autorités et en intègrent les effets avant qu’ils ne se produisent, "
         "si bien qu’une politique annoncée n’agit que sur les variables "
         "nominales.",
    'r': "On montre que le coût de la désinflation dépend de la croyance des "
         "agents, ce qui fait de la communication un instrument au même titre "
         "que le taux directeur.",
    'ex': "Le canal des anticipations décrit par le cours, par lequel la "
          "banque centrale annonce l’orientation future des taux pour ancrer "
          "les anticipations d’inflation."},
   {'q': "Sujet sur la politique monétaire en économie ouverte",
    'f': "La désinflation d’une grande économie est un choc pour les autres. "
         "Le cours décrit le mécanisme : les taux américains montent, les "
         "placements américains deviennent plus attractifs, les capitaux "
         "mondiaux reviennent massivement vers les États-Unis, qui "
         "deviennent une pompe aspirante à capitaux. Les pays émergents "
         "subissent alors simultanément la fuite des capitaux, la hausse du "
         "coût de leur dette et l’appréciation du dollar.",
    'r': "On montre que la mobilité des capitaux transforme un instrument "
         "national en variable mondiale, ce qui pose la question de la "
         "coordination des politiques monétaires.",
    'ex': "La formule du cours selon laquelle les investisseurs se demandent "
          "pourquoi placer dans un pays en développement risqué si les taux "
          "américains sont élevés."}],
  voisins=['n14-inflation', 'n14-deflation', 'n14-credibilite-monetaire',
           'n14-ancrage-anticipations'])


d('n14-deflation', 14, "Déflation",
  "La baisse des prix, et pourquoi la banque centrale la redoute",
  "Le cours définit la déflation par une formule brève, la baisse des prix, "
  "et la distingue ainsi de la désinflation, qui n’est qu’une baisse de "
  "l’inflation. Il en fait moins un objet d’analyse qu’un risque à "
  "combattre : éviter la déflation figure explicitement parmi les objectifs "
  "des politiques monétaires non conventionnelles et parmi les effets "
  "recherchés du rachat massif de titres.",
  "Le cours construit la déflation par contraste et par la politique qui la "
  "vise, et c’est ce double angle qui en donne le contenu. Le contraste "
  "d’abord : dans la série des degrés, une inflation à deux chiffres est une "
  "hyperinflation, la baisse de l’inflation est une désinflation, la baisse "
  "des prix est une déflation. La déflation est donc l’inverse de "
  "l’inflation, et non son simple ralentissement. Dans la tradition "
  "classique que le cours expose, elle a une cause symétrique de celle de "
  "l’inflation : les classiques considéraient qu’une abondance de monnaie "
  "provoquait l’inflation et qu’une pénurie entraînait la déflation, la "
  "monnaie n’affectant que le niveau général des prix. La politique ensuite. "
  "Le cours place éviter la déflation parmi les cinq objectifs des politiques "
  "monétaires non conventionnelles, à côté de rétablir la liquidité, "
  "débloquer le crédit, stabiliser les marchés et soutenir l’activité ; et il "
  "range la lutte contre la déflation parmi les effets recherchés du "
  "rachat massif de titres par la banque centrale, avec l’injection de "
  "liquidité, la hausse du prix des titres, la baisse des taux à moyen et "
  "long terme et le soutien au crédit et à l’investissement. Ce "
  "positionnement est éclairant : la déflation apparaît dans le cours au "
  "moment où les instruments conventionnels ne suffisent plus, c’est-à-dire "
  "dans la situation de trappe à liquidité, lorsque les taux sont déjà très "
  "bas, que les agents préfèrent conserver des liquidités, que les banques "
  "restent prudentes et que l’investissement ne repart pas suffisamment. On "
  "comprend alors pourquoi la cible d’inflation de la Banque centrale "
  "européenne est positive, autour de deux pour cent à moyen terme, et non "
  "nulle : une cible nulle exposerait en permanence au risque de basculer du "
  "mauvais côté, dans une situation où la politique monétaire "
  "conventionnelle perd son levier parce que le taux nominal ne peut guère "
  "descendre plus bas. Le cours ajoute enfin la dimension extérieure : la "
  "déflation apparaît aussi comme le pendant de l’inflation importée, les "
  "mouvements du change transmettant les prix étrangers à l’économie "
  "domestique dans les deux sens.",
  [("La baisse du niveau général des prix",
    "Le cours pose la définition par symétrie : la déflation est la baisse "
    "des prix, là où l’inflation est l’augmentation du niveau général des "
    "prix et la désinflation un simple ralentissement de cette hausse."),
   ("La cause monétaire classique",
    "Dans la tradition que le cours expose, une pénurie de monnaie entraîne "
    "la déflation comme une abondance provoque l’inflation : la monnaie "
    "n’affecte que le niveau général des prix."),
   ("Le report des achats",
    "Si les prix baissent, attendre devient rationnel : la dépense est "
    "différée, ce qui réduit la demande globale au moment même où elle serait "
    "nécessaire pour soutenir les prix."),
   ("L’alourdissement réel des dettes",
    "Les dettes étant libellées en termes nominaux, la baisse des prix "
    "augmente leur poids réel, ce qui pèse sur les emprunteurs et conduit au "
    "désendettement plutôt qu’à la dépense."),
   ("Le blocage de l’instrument conventionnel",
    "Le taux nominal ne pouvant guère descendre plus bas, la banque centrale "
    "se trouve dans la situation que le cours décrit comme la trappe à "
    "liquidité : baisser encore les taux ne suffit plus."),
   ("Le recours aux instruments non conventionnels",
    "Le cours assigne explicitement aux politiques non conventionnelles "
    "l’objectif d’éviter la déflation, par le rachat massif de titres, la "
    "baisse des taux à moyen et long terme et l’action sur les "
    "anticipations.")],
  [{'a': "La distinction entre déflation et désinflation évite un contresens "
         "de diagnostic aux conséquences opposées.",
    'cond': "Elle suppose de raisonner sur le signe de la variation des prix "
            "et non sur celui de la variation de l’inflation.",
    'lim': "La frontière est franchie insensiblement : une désinflation "
           "rapide peut conduire à la déflation sans rupture visible dans les "
           "statistiques."},
   {'a': "Elle justifie une cible d’inflation positive plutôt que nulle, en "
         "ménageant une marge de sécurité au-dessus de zéro.",
    'cond': "La justification suppose que le taux nominal ne puisse guère "
            "descendre en dessous de zéro, contrainte que le cours illustre "
            "par la trappe à liquidité et les taux négatifs.",
    'lim': "Le cours montre que certaines banques centrales ont justement "
           "utilisé des taux négatifs : la contrainte est donc forte sans "
           "être absolue."},
   {'a': "Elle explique la création des instruments non conventionnels, qui "
         "visent les bilans, les titres et les anticipations plutôt que le "
         "seul prix de la monnaie.",
    'cond': "L’argument suppose que les instruments conventionnels aient "
            "effectivement perdu leur prise, condition que le cours décrit "
            "précisément.",
    'lim': "Le cours assigne à ces instruments une limite propre, le risque "
           "d’aléa moral, puisqu’ils peuvent encourager les comportements "
           "imprudents."},
   {'a': "Elle éclaire la symétrie des missions de la banque centrale, qui "
         "doit redouter les deux sens de l’écart à sa cible.",
    'cond': "La symétrie suppose que la stabilité des prix soit définie "
            "comme une cible et non comme un plafond.",
    'lim': "Le cours relève le dilemme classique entre relancer l’activité "
           "et maîtriser l’inflation : en pratique, les deux risques ne sont "
           "pas traités avec la même urgence."},
   {'a': "Elle se relie à l’analyse du change, le mouvement des monnaies "
         "transmettant les prix étrangers dans les deux sens.",
    'cond': "Le canal suppose une dépendance aux biens libellés en devises "
            "étrangères, condition que le cours pose pour l’inflation "
            "importée.",
    'lim': "Le cours rappelle que l’effet du change est ambivalent : une "
           "appréciation modère les prix importés mais dégrade la "
           "compétitivité des exportations."}],
  [{'t': "La baisse des prix est une bonne nouvelle pour les ménages, "
         "puisqu’elle augmente leur pouvoir d’achat.",
    'qui': "La lecture intuitive que le cours écarte en faisant de la "
           "déflation un risque à éviter.",
    'rep': "Le cours répond par la place qu’il lui donne : éviter la "
           "déflation figure parmi les objectifs des politiques non "
           "conventionnelles, parce que la baisse des prix s’accompagne d’une "
           "contraction de l’activité et donc des revenus."},
   {'t': "La déflation n’est qu’un phénomène monétaire : il suffit "
         "d’augmenter la quantité de monnaie pour y mettre fin.",
    'qui': "La tradition classique et quantitativiste que le cours rattache "
           "à Bodin, Fisher et Friedman.",
    'rep': "Le cours montre la limite pratique : en trappe à liquidité, les "
           "agents conservent leurs liquidités et les banques restent "
           "prudentes, de sorte que la monnaie créée ne se transforme pas en "
           "dépense."},
   {'t': "Les instruments non conventionnels sont trop risqués pour être "
         "utilisés contre la déflation : ils encouragent l’imprudence.",
    'qui': "L’objection d’aléa moral que le cours assigne comme limite "
           "principale à ces politiques.",
    'rep': "Le cours maintient l’arbitrage sans le trancher : les "
           "dispositifs de protection sont nécessaires pour stabiliser "
           "l’économie même s’ils créent de l’aléa moral."},
   {'t': "Une cible d’inflation nulle serait préférable, la stabilité des "
         "prix signifiant littéralement des prix stables.",
    'qui': "La lecture littérale de l’objectif de stabilité des prix.",
    'rep': "Le cours fournit le repère contraire : la Banque centrale "
           "européenne vise une inflation autour de deux pour cent à moyen "
           "terme, marge qui éloigne précisément du risque de déflation."}],
  [{'n': "Irving Fisher",
    'i': "La quantité de monnaie détermine le niveau général des prix, une "
         "pénurie entraînant la déflation.",
    'p': "Le cours rapporte que les classiques considéraient qu’une "
         "abondance de monnaie provoquait l’inflation et qu’une pénurie "
         "entraînait la déflation, et donne son équation reliant la quantité "
         "de monnaie et sa vitesse au niveau des prix et au volume des "
         "transactions."},
   {'n': "John Maynard Keynes",
    'i': "Les agents peuvent préférer détenir la monnaie plutôt que la "
         "dépenser, ce qui bloque le retour de la demande.",
    'p': "Le cours en tire la situation limite de la trappe à liquidité : "
         "lorsque les taux sont déjà très bas, les agents préfèrent conserver "
         "des liquidités, les banques restent prudentes et l’investissement "
         "ne repart pas suffisamment, de sorte que la politique monétaire "
         "conventionnelle devient moins efficace."},
   {'n': "Milton Friedman",
    'i': "Si la quantité de monnaie ne croît pas assez vite, les prix "
         "cessent de monter puis baissent.",
    'p': "Le cours rapporte sa thèse symétrique de celle de l’inflation : "
         "l’inflation est toujours et partout un phénomène monétaire, ce qui "
         "implique que la déflation relève du même levier, la croissance de "
         "la masse monétaire, qu’il propose de contrôler par une règle."}],
  [{'f': "Le cours range éviter la déflation parmi les cinq objectifs des "
         "politiques monétaires non conventionnelles.",
    'p': "Le fait montre que la déflation n’est pas traitée comme une "
         "curiosité théorique mais comme un risque opérationnel justifiant "
         "des instruments exceptionnels."},
   {'f': "La lutte contre la déflation figure parmi les effets recherchés du "
         "rachat massif de titres par la banque centrale.",
    'p': "Le fait précise l’instrument : c’est par l’injection de liquidité, "
         "la hausse du prix des titres et la baisse des taux à moyen et long "
         "terme que la banque centrale cherche à faire remonter les prix."},
   {'f': "Dans la zone euro, la Banque centrale européenne vise une inflation "
         "autour de deux pour cent à moyen terme.",
    'p': "Le repère montre que la cible est volontairement positive : elle "
         "ménage une marge de sécurité au-dessus de zéro, précisément pour "
         "éloigner le risque de déflation."},
   {'f': "Le cours note que certaines banques centrales ont utilisé des taux "
         "négatifs parmi les instruments non conventionnels.",
    'p': "Le fait démontre l’ampleur de la difficulté : il a fallu franchir "
         "la borne du taux nul, ce qui mesure à quel point la déflation "
         "désarme la politique monétaire ordinaire."}],
  [{'q': "Sujet sur les risques pour la stabilité des prix",
    'f': "La stabilité des prix comporte deux risques symétriques et non un "
         "seul. Le cours fixe le vocabulaire : l’inflation est "
         "l’augmentation du niveau général des prix, la désinflation sa "
         "baisse, la déflation la baisse des prix eux-mêmes. Et il range "
         "éviter la déflation parmi les objectifs des politiques monétaires "
         "non conventionnelles, au même titre que rétablir la liquidité et "
         "débloquer le crédit.",
    'r': "On montre que la cible d’inflation est un compromis entre deux "
         "dangers, ce qui explique qu’elle soit fixée autour de deux pour "
         "cent et non à zéro.",
    'ex': "La cible de la Banque centrale européenne, une inflation autour "
          "de deux pour cent à moyen terme."},
   {'q': "Sujet sur les limites de la politique monétaire",
    'f': "La déflation est la situation où la politique monétaire "
         "conventionnelle perd sa prise. Le cours décrit la trappe à "
         "liquidité : lorsque les taux sont déjà très bas, les agents "
         "préfèrent conserver des liquidités, les banques restent prudentes "
         "et l’investissement ne repart pas suffisamment ; baisser encore les "
         "taux ne suffit plus. Il faut alors agir non plus sur le prix de la "
         "monnaie, mais sur les bilans, les titres et les anticipations.",
    'r': "On montre que la contrainte vient du plancher des taux nominaux, "
         "ce qui justifie le passage à des instruments agissant par d’autres "
         "canaux.",
    'ex': "Les taux négatifs et le rachat massif de titres, que le cours "
          "range parmi les instruments non conventionnels."},
   {'q': "Sujet sur l’analyse monétaire des prix",
    'f': "La tradition classique traite l’inflation et la déflation comme "
         "deux faces d’un même mécanisme. Le cours la résume : une abondance "
         "de monnaie provoquait l’inflation, une pénurie entraînait la "
         "déflation, la monnaie n’affectant pas l’économie réelle mais "
         "uniquement le niveau général des prix. La déflation serait donc un "
         "problème à solution simple, puisqu’il suffirait d’émettre.",
    'r': "On confronte cette symétrie théorique à la pratique décrite par le "
         "cours pour montrer qu’émettre de la monnaie ne garantit pas qu’elle "
         "soit dépensée.",
    'ex': "La trappe à liquidité, où les banques restent prudentes malgré "
          "l’abondance de liquidités fournies."},
   {'q': "Sujet sur la transmission internationale des prix",
    'f': "Les prix domestiques dépendent aussi du change, et dans les deux "
         "sens. Le cours décrit le canal pour la hausse : des importations "
         "plus chères élèvent les coûts de production, donc les prix "
         "domestiques, ce qui engendre l’inflation importée et, dans les cas "
         "extrêmes, l’hyperinflation. Le mouvement inverse d’appréciation "
         "modère les prix importés, au prix d’une perte de compétitivité des "
         "exportations.",
    'r': "On montre que le change relie mécaniquement le solde extérieur et "
         "le niveau des prix, ce qui limite l’autonomie de la politique "
         "monétaire en économie ouverte.",
    'ex': "Les exemples du cours pour l’inflation importée extrême : "
          "Argentine, Liban, Turquie."}],
  voisins=['n14-inflation', 'n14-desinflation', 'n14-inflation-importee',
           'n11-preference-liquidite'],
  comp={'titre': "Inflation et déflation",
        'a': "Inflation",
        'b': "Déflation",
        'lignes': [
          ("Définition du cours", "Augmentation du niveau général des prix",
           "Baisse des prix"),
          ("Cause monétaire classique", "Une abondance de monnaie",
           "Une pénurie de monnaie"),
          ("Cause réelle", "La demande augmente plus vite que l’offre",
           "La demande est durablement insuffisante par rapport à l’offre"),
          ("Effet sur les dettes", "Le poids réel des dettes diminue",
           "Le poids réel des dettes augmente"),
          ("Comportement d’achat induit", "Acheter maintenant, par la fuite "
           "devant la monnaie", "Attendre, puisque les prix baisseront"),
          ("Instrument conventionnel", "Hausse des taux directeurs, "
           "efficace", "Baisse des taux, bloquée par leur plancher"),
          ("Instrument mobilisé dans le cours", "Politique monétaire "
           "restrictive, comme le choc de taux de 1979",
           "Politiques non conventionnelles, rachat massif de titres et taux "
           "négatifs"),
          ("Situation limite", "Hyperinflation, soit une inflation à deux "
           "chiffres", "Trappe à liquidité, où baisser les taux ne suffit "
           "plus"),
          ("Place dans le mandat", "Objectif traditionnel de stabilité des "
           "prix", "Risque explicite que les politiques non conventionnelles "
           "doivent éviter")]})


d('n14-hyperinflation', 14, "Hyperinflation",
  "Quand l’inflation passe à deux chiffres et détruit la monnaie",
  "Le cours définit l’hyperinflation par un seuil simple : une inflation à "
  "deux chiffres. Il ne lui consacre pas de développement autonome mais en "
  "donne le mécanisme le plus net dans l’analyse du change, où la "
  "dépréciation renchérit les importations, élève les coûts de production "
  "puis les prix domestiques, ce qui engendre l’inflation importée et, dans "
  "les cas extrêmes, l’hyperinflation.",
  "Le cours aborde l’hyperinflation par deux voies distinctes, et c’est leur "
  "réunion qui en donne le contenu complet. La première est la mesure : dans "
  "la série des degrés, une inflation à deux chiffres est une "
  "hyperinflation, la baisse de l’inflation une désinflation, la baisse des "
  "prix une déflation. Le seuil est donc conventionnel mais net, et il "
  "indique un changement de nature plus qu’un simple changement de degré : à "
  "ce niveau, la monnaie cesse d’être un repère fiable pour les contrats et "
  "les anticipations. La seconde voie est le mécanisme, et le cours le situe "
  "dans l’analyse des déséquilibres extérieurs. Le point de départ est le "
  "cercle vicieux des monnaies faibles : un déficit extérieur provoque une "
  "dépréciation qui renchérit les importations et aggrave à son tour le "
  "déficit, et cette spirale extérieure peut ensuite devenir une spirale "
  "inflationniste. L’enchaînement est explicite : importations plus chères, "
  "donc coûts de production en hausse, donc prix domestiques en hausse, ce "
  "qui engendre l’inflation importée et, dans les cas extrêmes, "
  "l’hyperinflation. Le cours donne trois exemples contemporains, "
  "l’Argentine, le Liban et la Turquie, et la condition d’apparition : le "
  "phénomène est d’autant plus fort que le pays dépend d’une part importante "
  "de biens libellés en devises étrangères. Il ajoute aussitôt que le cercle "
  "vicieux ne s’enclenche pas nécessairement, puisqu’une monnaie plus faible "
  "rend aussi les exportations moins chères pour les étrangers et peut donc "
  "améliorer le solde extérieur, ce qui renvoie à la courbe en J. "
  "L’hyperinflation apparaît donc comme le point d’aboutissement d’une "
  "trajectoire plutôt que comme un état : elle se noue quand la dépréciation "
  "et la hausse des prix s’alimentent l’une l’autre sans que la "
  "compétitivité retrouvée n’interrompe la boucle. Le cours fournit par "
  "ailleurs un précédent historique qui éclaire la perte de confiance : "
  "l’effondrement du système de Law en 1720, où la création monétaire sans "
  "limite se termine par une panique, la ruine des épargnants et une "
  "hostilité durable des Français envers les banques et la monnaie papier.",
  [("Le seuil de deux chiffres",
    "Le cours fixe le repère : une inflation à deux chiffres est une "
    "hyperinflation, ce qui situe le phénomène non dans une théorie "
    "particulière mais dans une échelle de mesure continue."),
   ("Le déficit extérieur initial",
    "Un déficit extérieur pèse sur la monnaie : le cours en fait le point de "
    "départ du cercle vicieux des monnaies faibles, antérieur à toute "
    "dynamique de prix."),
   ("La dépréciation et le renchérissement des importations",
    "La monnaie se déprécie, les importations deviennent plus chères, ce qui "
    "aggrave le déficit et déprécie encore la monnaie : la boucle extérieure "
    "se referme sur elle-même."),
   ("Le passage aux prix domestiques",
    "Des importations plus chères élèvent les coûts de production, donc les "
    "prix domestiques : la spirale extérieure devient, selon les mots du "
    "cours, une spirale inflationniste."),
   ("L’emballement",
    "Dans les cas extrêmes, cette inflation importée devient "
    "hyperinflation : chaque hausse des prix nourrit la défiance envers la "
    "monnaie, donc sa dépréciation, donc une nouvelle hausse des prix."),
   ("L’interruption possible par la compétitivité",
    "Le cours ménage l’issue inverse : une monnaie qui se déprécie rend les "
    "exportations moins chères, les volumes exportés peuvent augmenter et le "
    "solde extérieur s’améliorer, ce qui renvoie à la courbe en J.")],
  [{'a': "Définir l’hyperinflation par un seuil chiffré permet un diagnostic "
         "sans recours à une théorie particulière de l’inflation.",
    'cond': "Le seuil n’a de sens que s’il marque un changement de "
            "comportement : à deux chiffres, la monnaie cesse de servir de "
            "référence stable pour les contrats.",
    'lim': "Un seuil conventionnel reste arbitraire : il ne distingue pas "
           "une inflation élevée mais stabilisée d’une inflation en "
           "accélération, qui est le vrai danger."},
   {'a': "Le mécanisme par le change explique l’hyperinflation dans des pays "
         "dont la banque centrale n’a pas nécessairement émis à l’excès.",
    'cond': "L’argument suppose une forte dépendance à des biens libellés en "
            "devises étrangères, condition que le cours énonce "
            "explicitement.",
    'lim': "Il ne couvre pas les hyperinflations d’origine strictement "
           "monétaire, que le cours illustre plutôt par la création monétaire "
           "sans limite du système de Law."},
   {'a': "Il relie l’hyperinflation aux déséquilibres extérieurs, ce qui en "
         "fait un problème de modèle de croissance et non seulement de "
         "politique monétaire.",
    'cond': "Le lien suppose que le déficit extérieur soit durable et qu’il "
            "pèse effectivement sur le change.",
    'lim': "Le cours avertit que les déséquilibres extérieurs doivent être "
           "interprétés avec prudence : un déficit n’est pas automatiquement "
           "mauvais."},
   {'a': "La réserve sur la courbe en J évite le fatalisme : la dépréciation "
         "n’enclenche pas nécessairement la spirale.",
    'cond': "L’issue favorable suppose que les volumes exportés réagissent "
            "effectivement à la baisse des prix relatifs, et avec un délai "
            "supportable.",
    'lim': "Le cours décrit précisément ce délai : dans un premier temps la "
           "facture des importations augmente et le solde peut se dégrader, "
           "ce qui laisse le temps à la spirale de s’installer."},
   {'a': "Le précédent de 1720 montre que le coût d’une hyperinflation "
         "dépasse de loin la période où elle se produit.",
    'cond': "La comparaison suppose que le mécanisme central soit la perte "
            "de confiance dans la monnaie, ce que le cours établit pour "
            "l’épisode de Law.",
    'lim': "Les cadres institutionnels sont incomparables : en 1720, une "
           "banque d’émission privée devenue royale, sans banque centrale "
           "indépendante ni régime de change moderne."}],
  [{'t': "L’hyperinflation est toujours le produit d’une création monétaire "
         "excessive par les autorités.",
    'qui': "La lecture quantitativiste que le cours rattache à Bodin, Fisher "
           "et Friedman.",
    'rep': "Le cours fournit un canal différent : la dépréciation de la "
           "monnaie renchérit les importations, élève les coûts puis les prix "
           "domestiques, ce qui peut produire l’hyperinflation sans "
           "emballement initial de l’émission."},
   {'t': "Une dépréciation est favorable : elle rétablit la compétitivité et "
         "corrige le déficit extérieur.",
    'qui': "L’argument de compétitivité que le cours présente comme limite "
           "au cercle vicieux.",
    'rep': "Le cours maintient les deux effets : la dépréciation renchérit "
           "les importations et abaisse le prix des exportations, de sorte "
           "que le résultat dépend du délai de réaction des volumes, ce que "
           "décrit la courbe en J."},
   {'t': "Le problème se règle par un ancrage du change sur une devise "
         "stable, qui supprime la dépréciation.",
    'qui': "La logique de la monnaie d’ancrage que le cours expose à propos "
           "du franc CFA et du dollar de Hong Kong.",
    'rep': "Le cours présente l’ancrage comme un moyen de stabiliser la "
           "valeur de la monnaie nationale, sans masquer qu’il transfère la "
           "contrainte : la politique monétaire devient dépendante de celle "
           "de la devise d’ancrage."},
   {'t': "Une inflation très élevée reste préférable à la déflation, "
         "puisqu’elle allège les dettes et soutient l’activité.",
    'qui': "La lecture qui assimile toute inflation à une facilité, et que "
           "le cours écarte.",
    'rep': "Le cours montre le coût propre à l’hyperinflation par l’exemple "
           "de 1720 : crise financière, ruine des épargnants et hostilité "
           "durable envers les banques et la monnaie papier."}],
  [{'n': "John Law",
    'i': "Une création monétaire sans limite détruit la confiance dans la "
         "monnaie.",
    'p': "Le cours décrit la boucle de son système, la banque émettant des "
         "billets, l’État remboursant ses dettes, les individus achetant des "
         "actions et l’argent revenant à la banque, puis l’effondrement de "
         "1720, avec panique, ruine des épargnants et retour durable à la "
         "monnaie métallique."},
   {'n': "Jean Bodin",
    'i': "Trop de monnaie égale inflation : l’accumulation monétaire fait "
         "monter les prix.",
    'p': "Le cours situe cette observation au seizième siècle, chez un "
         "mercantiliste qui s’interroge sur la probabilité d’une inflation "
         "liée à l’accumulation de métal précieux : la quantité de monnaie "
         "influence les prix, mais pas la production."},
   {'n': "Irving Fisher",
    'i': "La quantité de monnaie détermine proportionnellement le niveau "
         "général des prix.",
    'p': "Le cours donne son équation reliant quantité de monnaie et "
         "vitesse de circulation au niveau des prix et au volume des "
         "transactions, avec vitesse et volume supposés stables : c’est le "
         "cadre dans lequel une émission massive se traduit mécaniquement en "
         "hausse des prix."}],
  [{'f': "Le cours fixe le seuil : une inflation à deux chiffres est une "
         "hyperinflation.",
    'p': "Le repère donne un critère de diagnostic opérationnel, qui permet "
         "de distinguer l’hyperinflation d’une inflation simplement élevée "
         "sans entrer dans un débat théorique."},
   {'f': "Le cours cite trois exemples d’inflation importée extrême : "
         "l’Argentine, le Liban et la Turquie.",
    'p': "Les cas montrent que le phénomène est contemporain et qu’il "
         "concerne des économies dépendant fortement de biens libellés en "
         "devises étrangères."},
   {'f': "Le cours décrit l’enchaînement : importations plus chères, coûts de "
         "production en hausse, prix domestiques en hausse, inflation "
         "importée puis hyperinflation.",
    'p': "La chaîne démontre qu’une hyperinflation peut naître du change et "
         "non de l’émission : c’est le déséquilibre extérieur qui se "
         "transmet à l’économie domestique."},
   {'f': "Sous le système de Law, la création monétaire sans limite se "
         "termine en 1720 par une panique, la ruine des épargnants et le "
         "retour durable à la monnaie métallique.",
    'p': "Le précédent montre que le coût d’une destruction de la confiance "
         "monétaire se mesure en décennies : le cours relève une hostilité "
         "durable des Français envers les banques et la monnaie papier."}],
  [{'q': "Sujet sur les degrés de l’instabilité des prix",
    'f': "Le cours propose une échelle plutôt qu’une typologie. Une "
         "inflation à deux chiffres est une hyperinflation, la baisse de "
         "l’inflation est une désinflation, la baisse des prix est une "
         "déflation. Cette gradation montre que le diagnostic dépend du "
         "degré et que chaque niveau appelle une politique différente, du "
         "simple pilotage de la cible jusqu’à la reconstruction de la "
         "confiance monétaire.",
    'r': "On montre que le seuil de deux chiffres marque un changement de "
         "nature et non de degré, puisqu’à ce niveau la monnaie cesse de "
         "servir de référence pour les contrats.",
    'ex': "Les exemples du cours pour les cas extrêmes d’inflation importée : "
          "Argentine, Liban, Turquie."},
   {'q': "Sujet sur le change et les prix intérieurs",
    'f': "Une hyperinflation peut venir de l’extérieur. Le cours décrit le "
         "cercle vicieux des monnaies faibles : un déficit extérieur provoque "
         "une dépréciation qui renchérit les importations et aggrave le "
         "déficit, et cette spirale extérieure peut devenir une spirale "
         "inflationniste. Des importations plus chères élèvent les coûts de "
         "production puis les prix domestiques, ce qui engendre l’inflation "
         "importée et, dans les cas extrêmes, l’hyperinflation.",
    'r': "On montre que la cause n’est pas nécessairement monétaire : la "
         "transmission se fait par les coûts, ce qui limite l’efficacité "
         "d’une réponse purement quantitative.",
    'ex': "La condition posée par le cours : le pays dépend fortement de "
          "biens libellés en devises étrangères."},
   {'q': "Sujet sur la confiance monétaire",
    'f': "L’hyperinflation est d’abord une crise de confiance. Le cours en "
         "fournit la démonstration historique avec le système de Law : la "
         "banque émet des billets, l’État rembourse ses dettes, les individus "
         "achètent des actions, l’argent revient à la banque et de nouveaux "
         "billets sont fabriqués, soit une création monétaire sans limite. En "
         "1720 le système éclate, et il en résulte une crise financière, la "
         "ruine des épargnants et une hostilité durable envers la monnaie "
         "papier.",
    'r': "On montre que la monnaie ne vaut que par la confiance qu’elle "
         "inspire, ce qui explique pourquoi la sortie d’une hyperinflation "
         "exige un changement de régime et non un simple ajustement.",
    'ex': "Le retour à la monnaie métallique pendant longtemps, que le cours "
          "donne comme conséquence durable de 1720."},
   {'q': "Sujet sur la dépréciation monétaire et ses effets",
    'f': "La dépréciation a deux effets opposés que le cours refuse de "
         "hiérarchiser a priori. Elle renchérit les importations, ce qui "
         "peut déclencher l’inflation importée puis l’hyperinflation ; mais "
         "elle rend aussi les exportations moins chères pour les étrangers, "
         "de sorte que les volumes exportés peuvent augmenter et le solde "
         "extérieur s’améliorer. Le cours renvoie à la courbe en J pour "
         "trancher dans le temps plutôt que dans l’absolu.",
    'r': "On montre que l’issue dépend du délai de réaction des volumes "
         "d’échange, ce qui transforme une question de signe en question de "
         "calendrier.",
    'ex': "La séquence décrite par le cours : d’abord la facture des "
          "importations augmente et le solde se dégrade, puis les volumes "
          "exportés augmentent."}],
  voisins=['n14-inflation', 'n14-inflation-importee', 'n14-deflation',
           'n11-confiance'])
