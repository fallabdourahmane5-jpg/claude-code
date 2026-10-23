# -*- coding: utf-8 -*-
"""Ensemble 13 — Les crises et l’instabilité économique (2/4)."""

from doss_base import d

d('n13-chocs-offre-demande', 13, "Chocs d’offre et de demande",
  "Deux façons de faire décrocher l’économie de son potentiel",
  "Un choc est une perturbation qui écarte l’activité de sa trajectoire "
  "soutenable. Le cours les classe en deux familles : les chocs d’offre, qui "
  "frappent les conditions de production, et les chocs de demande, qui "
  "frappent la dépense. Il en fait la clé de deux notions centrales, le PIB "
  "potentiel, défini sans choc d’offre ni de demande, et l’output gap, écart "
  "entre croissance effective et croissance potentielle.",
  "Le cours fait des chocs un instrument de mesure avant d’en faire un objet "
  "d’analyse, et c’est cette fonction qui en commande l’importance. Le point "
  "de départ est une définition : le PIB potentiel est le PIB qu’un État "
  "aurait dû avoir si tous les facteurs de production sont utilisés sans choc "
  "d’offres et de demande, mais aussi sans chômage et sans inflation. "
  "Autrement dit, les chocs sont par construction ce qui sépare la trajectoire "
  "réelle de la trajectoire soutenable. Le chapitre sur la croissance "
  "reprend la même construction : la croissance potentielle correspond au "
  "rythme que l’économie pourrait atteindre si tous les facteurs de "
  "production étaient pleinement utilisés, en l’absence de choc de demande, "
  "c’est-à-dire de crise, de chute de la consommation ou de baisse de "
  "l’investissement, et sans tension inflationniste. C’est une croissance "
  "théorique, une référence, la vitesse de croisière soutenable de "
  "l’économie. L’outil de diagnostic qui en découle est l’output gap, écart "
  "entre croissance effective et croissance potentielle. Le cours en déduit "
  "trois situations : si les deux grandeurs coïncident, l’économie est à "
  "l’équilibre ; si la croissance effective dépasse la croissance "
  "potentielle, l’output gap est positif et l’économie est en surchauffe, "
  "avec des tensions inflationnistes possibles, car les entreprises peuvent "
  "décider d’augmenter les prix au lieu d’augmenter les capacités de "
  "production ; dans le cas inverse, l’économie produit moins qu’elle ne "
  "pourrait. Le cours insiste sur l’asymétrie des deux familles de chocs. Un "
  "choc de demande agit sur la dépense, et le cours en donne les formes : "
  "crise, chute de la consommation, baisse de l’investissement, auxquelles "
  "s’ajoutent la confiance des ménages et la politique budgétaire et "
  "monétaire. Un choc d’offre agit sur les conditions de production, et "
  "l’exemple de référence est le choc pétrolier : en 1973 le monde connaît "
  "une forte hausse du prix du baril, suivie d’un second choc en 1979, le "
  "baril passant au total de cinq à trente dollars, ce qui provoque une forte "
  "hausse du chômage par un fort taux de licenciement en réponse à la hausse "
  "des coûts de production. La conséquence théorique est décisive : les "
  "firmes voient leurs coûts augmenter, donc elles licencient, d’où inflation "
  "et chômage simultanés, c’est-à-dire la stagflation, qui détruit "
  "expérimentalement la courbe de Phillips puisque l’inflation n’a pas fait "
  "baisser le chômage. Le modèle de Harrod intègre enfin les deux familles "
  "dans le taux de croissance effectif, qui dépend de la conjoncture, des "
  "anticipations des entreprises, des chocs d’offre comme le climat ou les "
  "crises financières, des chocs de demande et du niveau d’investissement "
  "effectivement réalisé.",
  [("La trajectoire de référence",
    "Le cours définit d’abord un repère : le PIB potentiel est celui qu’un "
    "État aurait dû avoir si tous les facteurs de production sont utilisés "
    "sans choc d’offre ni de demande, sans chômage et sans inflation."),
   ("Le choc de demande déplace la dépense",
    "Une crise, une chute de la consommation ou une baisse de "
    "l’investissement réduisent la dépense : la production suit vers le bas "
    "alors que les capacités productives restent intactes, d’où un écart "
    "négatif entre croissance effective et potentielle."),
   ("Le choc d’offre déplace les coûts",
    "Une hausse brutale du prix d’un intrant augmente les coûts de "
    "production : les entreprises répercutent sur les prix et réduisent "
    "l’emploi, de sorte que la production baisse et que les prix montent en "
    "même temps."),
   ("La stagflation comme signature du choc d’offre",
    "Le cours tire la conséquence : les firmes voient leurs coûts augmenter, "
    "donc elles licencient, d’où inflation et chômage simultanés, ce qui "
    "détruit expérimentalement la courbe de Phillips."),
   ("La lecture par l’output gap",
    "L’écart entre croissance effective et croissance potentielle sert de "
    "diagnostic : un output gap positif signale une surchauffe et des "
    "tensions inflationnistes, un output gap négatif une économie en deçà de "
    "ses capacités."),
   ("Le choix de la réponse dépend du type de choc",
    "Soutenir la dépense convient à un choc de demande, mais aggrave "
    "l’inflation après un choc d’offre : le cours montre avec la stagflation "
    "que l’outil conjoncturel perd sa prise quand le choc vient des coûts.")],
  [{'a': "La distinction des deux chocs permet de choisir l’instrument "
         "adapté, au lieu de traiter toute récession par la relance de la "
         "demande.",
    'cond': "Elle suppose que l’on puisse identifier l’origine du choc, ce "
            "que le cours rend possible en observant la direction des prix et "
            "celle de l’activité.",
    'lim': "Un épisode réel peut combiner les deux : le cours associe au "
           "choc pétrolier une hausse du chômage, donc une contraction de la "
           "demande venue d’un choc d’offre initial."},
   {'a': "Les chocs donnent un contenu opératoire au PIB potentiel, qui se "
         "définit précisément par leur absence.",
    'cond': "La mesure exige que les facteurs de production soient supposés "
            "pleinement utilisés, sans chômage ni inflation, hypothèse que le "
            "cours assume explicitement.",
    'lim': "Le cours rappelle que la croissance potentielle est une "
           "croissance théorique, une référence et non la croissance "
           "réellement observée : l’output gap hérite donc de l’incertitude "
           "de son dénominateur."},
   {'a': "La stagflation des années soixante-dix fournit une réfutation "
         "empirique forte de la courbe de Phillips.",
    'cond': "L’argument exige que l’inflation et le chômage aient bien "
            "augmenté ensemble, ce que le cours affirme : on a eu les deux, "
            "inflation et chômage élevé.",
    'lim': "Les monétaristes en tirent une autre conclusion que le cours "
           "rapporte : les agents ne sont plus victimes d’illusion monétaire "
           "et anticipent, de sorte que ce serait l’anticipation, non le "
           "choc, qui invalide la relation."},
   {'a': "Le choc d’offre a nourri le retour des analyses de "
         "l’investissement par l’offre et les profits.",
    'cond': "Le lien suppose que la hausse des coûts de production ait bien "
            "été la contrainte dominante sur les décisions d’investir.",
    'lim': "Le cours montre que l’approche par la demande n’est pas réfutée "
           "pour autant : l’investissement reste à la fois un élément de la "
           "demande et un élément de l’offre."},
   {'a': "La grille des chocs s’applique aussi aux modèles de croissance, où "
         "elle explique la volatilité du taux effectif.",
    'cond': "Elle suppose que le taux effectif dépende de la conjoncture et "
            "des anticipations, comme l’établit Harrod.",
    'lim': "Chez Harrod, l’instabilité ne vient pas des chocs mais de "
           "l’absence de coordination entre trois taux indépendants : les "
           "chocs révèlent la fragilité plus qu’ils ne la créent."}],
  [{'t': "La politique monétaire peut réduire le chômage en acceptant un peu "
         "plus d’inflation : il existe un arbitrage stable entre les deux.",
    'qui': "La lecture de la courbe de Phillips que le cours présente avant "
           "les années soixante-dix.",
    'rep': "Le cours répond par les faits : lors du choc pétrolier, les "
           "firmes licencient en réponse à la hausse des coûts, on obtient "
           "inflation et chômage élevé, et l’arbitrage supposé disparaît."},
   {'t': "Ce ne sont pas les chocs qui expliquent l’échec de la relance, mais "
         "le fait que les agents anticipent et ne sont plus victimes "
         "d’illusion monétaire.",
    'qui': "Les monétaristes autour de Milton Friedman, dont le cours "
           "rapporte la conclusion.",
    'rep': "Les deux explications se complètent plus qu’elles ne "
           "s’excluent : l’anticipation explique pourquoi la relance est "
           "inefficace, le choc d’offre explique pourquoi les coûts ont "
           "augmenté au départ."},
   {'t': "L’investissement dépend des profits et de l’offre, non de la "
         "demande anticipée : les chocs de coût sont donc le facteur "
         "décisif.",
    'qui': "Les économistes de l’offre dont le cours situe le retour dans "
           "les années quatre-vingt-dix, après les deux chocs pétroliers.",
    'rep': "Le cours maintient l’ambivalence de l’investissement, à la fois "
           "élément de la demande et élément de l’offre : privilégier l’une "
           "des deux faces revient à perdre l’autre."},
   {'t': "L’instabilité ne vient pas de perturbations extérieures mais de "
         "l’économie elle-même, dont les trois taux de croissance ne "
         "convergent pas.",
    'qui': "Roy Harrod, dont le cours expose le « fil du rasoir ».",
    'rep': "Harrod intègre lui-même les chocs dans son taux effectif, qui "
           "dépend des chocs d’offre comme le climat ou les crises "
           "financières et des chocs de demande : l’opposition est donc de "
           "hiérarchie, non de nature."}],
  [{'n': "Milton Friedman",
    'i': "Les agents anticipent l’inflation, de sorte que la politique "
         "monétaire est impuissante à réduire durablement le chômage.",
    'p': "Le cours rapporte la conclusion des friedmaniens au moment où la "
         "courbe de Phillips cesse de fonctionner : les gens ne sont plus "
         "victimes d’illusion monétaire, ils anticipent, donc la politique "
         "monétaire ne marche plus et il ne reste que l’inflation."},
   {'n': "Roy Harrod",
    'i': "Le taux de croissance effectif dépend notamment des chocs d’offre "
         "et des chocs de demande.",
    'p': "Le cours détaille les déterminants qu’il retient : la conjoncture, "
         "les anticipations des entreprises, les chocs d’offre comme le "
         "climat ou les crises financières, les chocs de demande et le niveau "
         "d’investissement effectivement réalisé, d’où un taux empirique et "
         "fluctuant."},
   {'n': "John Maynard Keynes",
    'i': "L’économie repose sur la demande, de sorte qu’un choc de dépense "
         "suffit à faire décrocher la production.",
    'p': "Le cours en fait l’économiste le plus connu défendant l’idée que "
         "l’investissement dépend de la demande, ce qui donne au choc de "
         "demande son statut de cause autonome et non de simple symptôme "
         "d’un problème d’offre."}],
  [{'f': "En 1973 survient un premier choc pétrolier, suivi d’un second en "
         "1979 ; le baril passe au total de cinq à trente dollars.",
    'p': "Le fait fournit l’exemple canonique de choc d’offre : la hausse des "
         "coûts de production entraîne un fort taux de licenciement, donc une "
         "forte hausse du chômage, sans qu’aucune insuffisance de demande "
         "initiale soit en cause."},
   {'f': "La stagflation associe stagnation de la production et inflation, "
         "configuration que la courbe de Phillips jugeait improbable.",
    'p': "Le fait démontre qu’un choc d’offre inverse le diagnostic habituel : "
         "le cours conclut que la courbe de Phillips est détruite "
         "expérimentalement puisque l’inflation n’a pas fait baisser le "
         "chômage."},
   {'f': "Le cours donne la règle de lecture de l’output gap : un écart "
         "positif signale une surchauffe et des tensions inflationnistes "
         "possibles.",
    'p': "Le fait montre pourquoi les chocs doivent être mesurés "
         "relativement à un potentiel : les entreprises peuvent décider "
         "d’augmenter les prix au lieu d’augmenter les capacités de "
         "production."},
   {'f': "Après les chocs pétroliers, le chancelier allemand Helmut Schmidt "
         "déclare que les profits d’aujourd’hui font les investissements de "
         "demain.",
    'p': "La citation, rapportée par le cours, montre l’effet doctrinal du "
         "choc d’offre : elle appuie le retour des analyses de "
         "l’investissement par l’offre et les profits dans les années "
         "quatre-vingt-dix."}],
  [{'q': "Sujet sur les fluctuations de l’activité économique",
    'f': "Toutes les récessions ne se ressemblent pas. Le cours définit le "
         "PIB potentiel comme celui qu’un État aurait dû avoir si tous les "
         "facteurs de production sont utilisés sans choc d’offre ni de "
         "demande, sans chômage et sans inflation. Les deux familles de chocs "
         "sont donc par construction ce qui sépare la trajectoire réelle de "
         "la trajectoire soutenable, et leur distinction commande le "
         "diagnostic.",
    'r': "On montre que la direction simultanée des prix et de l’activité "
         "permet d’identifier l’origine du choc, ce qui détermine ensuite "
         "l’instrument de politique économique approprié.",
    'ex': "Les chocs pétroliers de 1973 et 1979, où le baril passe de cinq à "
          "trente dollars et où le chômage augmente fortement."},
   {'q': "Sujet sur inflation et chômage",
    'f': "La relation entre inflation et chômage dépend de la nature du choc "
         "subi. Le cours l’établit à partir des années soixante-dix : lors du "
         "choc pétrolier, les firmes voient leurs coûts augmenter, donc elles "
         "sont obligées de licencier, d’où inflation et chômage. C’est la "
         "stagflation, qui détruit expérimentalement la courbe de Phillips "
         "puisque l’inflation n’a pas fait baisser le chômage.",
    'r': "Le raisonnement oppose la logique d’un choc de demande, où prix et "
         "activité varient dans le même sens, à celle d’un choc d’offre, où "
         "ils varient en sens contraire.",
    'ex': "La stagflation des années soixante-dix, avec inflation et chômage "
          "élevé simultanément."},
   {'q': "Sujet sur la mesure de la conjoncture économique",
    'f': "Mesurer la conjoncture suppose un repère théorique. Le cours le "
         "fournit avec l’output gap, écart entre croissance effective et "
         "croissance potentielle : si les deux coïncident l’économie est à "
         "l’équilibre, si l’effective dépasse la potentielle l’économie est "
         "en surchauffe avec des tensions inflationnistes possibles, car les "
         "entreprises peuvent augmenter les prix au lieu des capacités.",
    'r': "On montre que l’indicateur ne mesure pas un niveau mais un écart, "
         "ce qui explique pourquoi il relie croissance, chômage et inflation "
         "dans un même diagnostic.",
    'ex': "La définition du cours selon laquelle une économie peut avoir un "
          "potentiel de un pour cent et ne croître que de zéro virgule trois "
          "pour cent."},
   {'q': "Sujet sur les limites des politiques conjoncturelles",
    'f': "Une politique de demande ne traite pas un choc d’offre. Le cours "
         "montre qu’après le choc pétrolier, soutenir la dépense ne restaure "
         "pas l’emploi mais nourrit l’inflation, puisque la contrainte vient "
         "des coûts de production. La conclusion des friedmaniens prolonge "
         "l’argument : les agents ne sont plus victimes d’illusion monétaire, "
         "ils anticipent, donc la politique monétaire ne marche plus.",
    'r': "On établit que l’efficacité d’un instrument dépend de la nature de "
         "la contrainte, ce qui permet de critiquer la relance sans nier "
         "l’existence des crises de demande.",
    'ex': "L’impuissance de la politique monétaire à réduire le chômage que "
          "le cours constate dans les années soixante-dix."}],
  voisins=['n13-crises-demande', 'n13-cycles-economiques',
           'n13-accelerateur', 'n13-crises-surproduction'])


d('n13-accelerateur', 13, "Accélérateur d’investissement",
  "Une variation de la demande provoque une variation plus forte de "
  "l’investissement",
  "Le principe de l’accélérateur, que le cours attribue à Aftalion et Clark, "
  "énonce qu’une variation de la demande provoque une variation plus que "
  "proportionnelle de l’investissement. Mesurée par la variation du PIB, une "
  "hausse de la demande entraîne une hausse plus forte de l’investissement, "
  "et une baisse de la demande une contraction également amplifiée : "
  "l’accélérateur joue dans les deux sens.",
  "Le cours place l’accélérateur du côté de l’approche de l’investissement "
  "par la demande, et c’est ce rattachement qui en fixe la portée. "
  "L’économiste le plus connu défendant l’idée que l’investissement dépend de "
  "la demande est Keynes : selon lui, l’économie repose sur la demande. Le "
  "cours distingue alors deux principes voisins mais distincts. Le principe "
  "du multiplicateur part de l’investissement et aboutit au revenu : une "
  "variation de l’investissement entraîne une variation du revenu, qui se "
  "partage entre consommation et épargne. Le principe de l’accélérateur part "
  "de la demande et aboutit à l’investissement : variation de la demande, "
  "donc variation de l’investissement. L’argument repose sur le fait que "
  "lorsque la demande augmente, mesurée par la variation du PIB, cela "
  "provoque une hausse de l’investissement plus que proportionnelle ; "
  "autrement dit, lorsqu’il y a hausse de la demande, la variation de "
  "l’investissement est plus forte, et inversement lorsqu’il y a baisse. Le "
  "cours formalise ensuite le multiplicateur, et cette algèbre éclaire le "
  "couplage des deux mécanismes. La variation du revenu national se "
  "décompose en variation de la consommation et variation de "
  "l’investissement ; comme la variation de la consommation est "
  "proportionnelle à celle du revenu selon la propension à consommer, on "
  "obtient par substitution que la variation du revenu est égale à celle de "
  "l’investissement multipliée par un sur un moins la propension à consommer. "
  "Avec une propension à consommer de zéro virgule huit, les ménages "
  "consommant quatre-vingts pour cent de leur revenu, le multiplicateur vaut "
  "cinq en économie fermée, et deux et demi en économie ouverte. Le point "
  "décisif vient du bouclage : si l’investissement fait varier le revenu, "
  "donc la demande, et si la demande fait varier l’investissement de façon "
  "amplifiée, le mouvement s’auto-entretient. C’est ce que le cours appelle "
  "l’oscillateur de Samuelson, formulé en 1939 : variation de "
  "l’investissement, donc du revenu, donc de la demande. Le cours en tire la "
  "conclusion générale sur la place de l’investissement : il est un élément "
  "clé de l’économie car il est à la fois un élément de la demande et un "
  "élément de l’offre.",
  [("La demande anticipée commande la décision d’investir",
    "Les entreprises n’investissent pas en fonction de leur épargne mais de "
    "la demande qu’elles anticipent : le cours rattache ce principe à "
    "l’approche keynésienne selon laquelle l’économie repose sur la "
    "demande."),
   ("La réaction est plus que proportionnelle",
    "Une hausse de la demande, mesurée par la variation du PIB, provoque une "
    "hausse de l’investissement plus forte : ce n’est pas le niveau de la "
    "demande qui compte mais sa variation, d’où l’amplification."),
   ("Le mécanisme joue symétriquement à la baisse",
    "Le cours insiste sur la réciproque : lorsqu’il y a baisse de la demande, "
    "la variation de l’investissement est également plus forte, ce qui fait "
    "de l’accélérateur un amplificateur de récession autant que "
    "d’expansion."),
   ("Le couplage avec le multiplicateur",
    "Une variation de l’investissement fait varier le revenu selon le "
    "multiplicateur, donc la demande, qui à son tour fait varier "
    "l’investissement : la boucle est fermée et le mouvement s’auto-"
    "entretient."),
   ("La formule du multiplicateur",
    "La variation du revenu est égale à celle de l’investissement multipliée "
    "par un sur un moins la propension à consommer : avec zéro virgule huit, "
    "le multiplicateur vaut cinq en économie fermée."),
   ("L’oscillateur comme résultat",
    "Le cours nomme ce bouclage l’oscillateur de Samuelson, formulé en 1939, "
    "et le résume par l’enchaînement variation de l’investissement, "
    "variation du revenu, variation de la demande.")],
  [{'a': "L’accélérateur explique pourquoi l’investissement est beaucoup plus "
         "volatil que la consommation ou le produit intérieur brut.",
    'cond': "Il suppose que les entreprises ajustent leurs capacités à la "
            "demande anticipée, donc qu’elles n’aient pas de capacités "
            "inemployées disponibles.",
    'lim': "Si des capacités sont déjà sous-utilisées, la hausse de la "
           "demande se satisfait sans investissement nouveau et "
           "l’amplification ne se produit pas."},
   {'a': "Combiné au multiplicateur, il fournit un mécanisme endogène de "
         "fluctuation, sans recours à un choc extérieur.",
    'cond': "Le bouclage exige que les deux relations opèrent "
            "simultanément : l’investissement vers le revenu, le revenu vers "
            "l’investissement.",
    'lim': "Le cours précise bien que le multiplicateur ne fait pas partie de "
           "l’argument de l’accélérateur : les deux principes sont distincts "
           "et c’est leur articulation, chez Samuelson, qui produit "
           "l’oscillation."},
   {'a': "Il donne un contenu mesurable à la thèse keynésienne selon laquelle "
         "l’investissement dépend de la demande.",
    'cond': "L’argument suppose que la variation du PIB soit une bonne "
            "approximation de la variation de la demande adressée aux "
            "entreprises.",
    'lim': "L’approche par les profits, que le cours fait revenir après les "
           "chocs pétroliers, soutient au contraire que l’investissement "
           "dépend des conditions d’offre et de la rentabilité."},
   {'a': "Il éclaire la propagation des crises : une baisse modérée de la "
         "demande suffit à provoquer un effondrement de l’investissement.",
    'cond': "La propagation suppose que les anticipations se retournent "
            "effectivement, et non que les entreprises lissent leurs plans "
            "d’investissement.",
    'lim': "Le cours rappelle avec les conditions de financement, accès au "
           "crédit et autofinancement, qu’un autre canal peut dominer : une "
           "entreprise peut vouloir investir sans pouvoir se financer."},
   {'a': "Il justifie une politique de soutien de la demande en période de "
         "retournement, puisque l’effet sur l’investissement est amplifié.",
    'cond': "L’efficacité suppose un multiplicateur élevé, donc une forte "
            "propension à consommer et une économie peu ouverte.",
    'lim': "Le cours chiffre lui-même l’affaiblissement : le multiplicateur "
           "passe de cinq en économie fermée à deux et demi en économie "
           "ouverte, car une part de la relance fuit vers les importations."}],
  [{'t': "L’investissement dépend des profits et non de la demande : ce sont "
         "les profits d’aujourd’hui qui font les investissements de demain.",
    'qui': "L’approche par les profits et par l’offre, que le cours fait "
           "revenir dans les années quatre-vingt-dix après les chocs "
           "pétroliers.",
    'rep': "Le cours ne tranche pas mais resitue l’enjeu : l’investissement "
           "est à la fois un élément de la demande et un élément de l’offre, "
           "de sorte que les deux approches saisissent chacune une face du "
           "même acte."},
   {'t': "Ce sont les conditions de financement, accès au crédit et "
         "autofinancement, qui déterminent l’investissement.",
    'qui': "L’approche par le financement que le cours présente parmi les "
           "déterminants de l’investissement.",
    'rep': "Les deux canaux sont complémentaires : la demande anticipée "
           "détermine le projet, le financement en détermine la "
           "faisabilité, et une crise peut bloquer l’un comme l’autre."},
   {'t': "Un mécanisme d’amplification ne suffit pas à expliquer les cycles : "
         "il faut une cause de retournement, que l’accélérateur ne fournit "
         "pas.",
    'qui': "L’analyse schumpétérienne des cycles, qui fait de l’épuisement "
           "des grappes d’innovations la cause du retournement.",
    'rep': "L’objection est juste mais partielle : le cours rattache "
           "précisément les cycles de Juglar à l’investissement productif, de "
           "sorte que l’accélérateur explique l’amplitude du cycle moyen même "
           "s’il n’en explique pas l’origine."},
   {'t': "L’investissement n’est pas si réactif : les entreprises lissent "
         "leurs décisions sur plusieurs années plutôt que de suivre la "
         "demande courante.",
    'qui': "L’objection issue des capacités inemployées, que le cours "
           "soulève en distinguant utilisation et extension des capacités.",
    'rep': "Le cours maintient la condition de validité : l’accélérateur "
           "opère lorsque les capacités sont déjà pleinement utilisées, "
           "situation que l’output gap positif permet précisément de "
           "repérer."}],
  [{'n': "Aftalion",
    'i': "Une variation de la demande provoque une variation plus que "
         "proportionnelle de l’investissement.",
    'p': "Le cours formule le principe sous la mention « Aftalion et Clark » "
         "et le résume par l’enchaînement variation de la demande, variation "
         "de l’investissement, en précisant que la demande est mesurée par la "
         "variation du produit intérieur brut."},
   {'n': "John Maynard Keynes",
    'i': "L’investissement dépend de la demande, car l’économie repose sur la "
         "demande.",
    'p': "Le cours en fait l’économiste le plus connu de cette approche et "
         "lui rattache à la fois le principe du multiplicateur, de "
         "l’investissement vers le revenu, et le cadre dans lequel "
         "l’accélérateur prend son sens, de la demande vers "
         "l’investissement."},
   {'n': "Paul Samuelson",
    'i': "L’oscillateur relie multiplicateur et accélérateur en un même "
         "mouvement cumulatif.",
    'p': "Le cours date la formulation de 1939 et la résume par "
         "l’enchaînement variation de l’investissement, variation du revenu, "
         "variation de la demande : c’est ce bouclage qui transforme deux "
         "relations statiques en mécanisme de fluctuation."}],
  [{'f': "Avec une propension à consommer de zéro virgule huit, les ménages "
         "consommant quatre-vingts pour cent de leur revenu, le multiplicateur "
         "vaut cinq.",
    'p': "Le chiffre donne l’ordre de grandeur de l’amplification par le "
         "revenu, premier maillon du bouclage que l’accélérateur referme en "
         "ramenant la demande vers l’investissement."},
   {'f': "Le cours chiffre la perte d’efficacité de l’ouverture : le "
         "multiplicateur tombe de cinq en économie fermée à deux et demi en "
         "économie ouverte.",
    'p': "Le fait démontre qu’une part de la relance fuit vers les "
         "importations, ce qui réduit d’autant l’effet accélérateur attendu "
         "sur l’investissement national."},
   {'f': "L’oscillateur de Samuelson est daté de 1939 et résumé par "
         "l’enchaînement variation de l’investissement, variation du revenu, "
         "variation de la demande.",
    'p': "La date et la formule montrent que l’articulation des deux "
         "principes est un résultat théorique identifié, et non une simple "
         "juxtaposition du multiplicateur et de l’accélérateur."},
   {'f': "Le cours conclut que l’investissement est à la fois un élément de "
         "la demande et un élément de l’offre.",
    'p': "Cette double nature démontre pourquoi l’investissement est le "
         "maillon par lequel une fluctuation de court terme se transmet aux "
         "capacités productives, donc au potentiel de long terme."}],
  [{'q': "Sujet sur les déterminants de l’investissement",
    'f': "L’investissement ne suit pas le niveau de la demande mais sa "
         "variation. Le principe de l’accélérateur, que le cours attribue à "
         "Aftalion et Clark, l’énonce ainsi : lorsque la demande augmente, "
         "mesurée par la variation du produit intérieur brut, cela provoque "
         "une hausse de l’investissement plus que proportionnelle, et "
         "inversement lorsqu’il y a baisse. C’est pourquoi l’investissement "
         "est la composante la plus volatile de la demande.",
    'r': "On distingue niveau et variation pour expliquer l’amplitude : une "
         "entreprise déjà au plein de ses capacités doit créer des capacités "
         "nouvelles, ce qui démultiplie sa dépense.",
    'ex': "Le cours relie les cycles de Juglar, de huit à dix ans, à "
          "l’investissement productif et aux fluctuations du crédit."},
   {'q': "Sujet sur les mécanismes d’amplification des crises",
    'f': "Une économie peut fluctuer sans choc extérieur. Le cours réunit "
         "deux principes pour l’établir : le multiplicateur conduit de "
         "l’investissement au revenu, l’accélérateur conduit de la demande à "
         "l’investissement. Samuelson referme la boucle en 1939 avec "
         "l’oscillateur, enchaînement variation de l’investissement, "
         "variation du revenu, variation de la demande, qui suffit à "
         "entretenir le mouvement.",
    'r': "Le raisonnement montre que la combinaison de deux relations "
         "stables produit une dynamique instable, ce qui rend la crise "
         "endogène et non accidentelle.",
    'ex': "La formule du multiplicateur du cours, égal à cinq pour une "
          "propension à consommer de zéro virgule huit."},
   {'q': "Sujet sur la politique de relance et son efficacité",
    'f': "L’effet attendu d’une relance dépend de deux grandeurs que le cours "
         "chiffre. Le multiplicateur vaut cinq en économie fermée mais deux "
         "et demi en économie ouverte, et l’accélérateur n’opère que si les "
         "capacités sont déjà pleinement utilisées. Une relance peut donc "
         "produire un effet beaucoup plus faible qu’annoncé, non parce que le "
         "mécanisme est faux, mais parce que ses conditions ne sont pas "
         "réunies.",
    'r': "On passe du mécanisme à ses conditions de validité pour montrer "
         "que l’évaluation d’une politique dépend de l’ouverture de "
         "l’économie et de son degré d’utilisation des capacités.",
    'ex': "Le passage du multiplicateur de cinq à deux et demi lorsque "
          "l’économie est ouverte aux importations."},
   {'q': "Sujet sur le débat entre offre et demande",
    'f': "L’investissement est le point où les deux approches se rencontrent. "
         "Le cours rattache à la demande le principe de l’accélérateur, et à "
         "l’offre l’approche par les profits que les chocs pétroliers "
         "remettent en avant, résumée par la phrase du chancelier Helmut "
         "Schmidt selon laquelle les profits d’aujourd’hui font les "
         "investissements de demain. Il tranche en conservant les deux : "
         "l’investissement est à la fois un élément de la demande et un "
         "élément de l’offre.",
    'r': "On montre que les deux approches portent sur des moments "
         "différents de la décision, l’anticipation du débouché et la "
         "capacité de financement, ce qui permet de les articuler plutôt que "
         "de choisir.",
    'ex': "Le retour des analyses par l’offre dans les années "
          "quatre-vingt-dix, après les chocs pétroliers de 1973 et 1979."}],
  voisins=['n13-crises-demande', 'n13-cycles-economiques',
           'n13-chocs-offre-demande', 'n13-cycle-credit'])


d('n13-cycle-credit', 13, "Cycle du crédit",
  "Le crédit amplifie l’expansion puis la contraction",
  "Le cycle du crédit désigne l’alternance entre une phase d’expansion du "
  "crédit, qui nourrit l’investissement et la spéculation, et une phase de "
  "contraction, où le crédit se bloque et aggrave la récession. Le cours ne "
  "traite pas cette alternance pour elle-même, mais la reconstitue par trois "
  "voies : les cycles de Juglar, l’analyse de Hayek et le canal du crédit "
  "bancaire de la politique monétaire.",
  "Le cours ne consacre pas de développement autonome au cycle du crédit, "
  "mais il en fournit tous les éléments, et c’est leur rapprochement qui en "
  "donne la cohérence. Première voie, la typologie des cycles : les cycles de "
  "Juglar, d’environ huit à dix ans, sont généralement associés à "
  "l’investissement productif et aux fluctuations du crédit, avec les quatre "
  "phases classiques de reprise, expansion, crise et dépression. Le crédit "
  "n’est donc pas un simple accompagnement du cycle moyen : il en est l’un "
  "des deux ressorts. Deuxième voie, l’analyse de Hayek, que le cours résume "
  "sans ambiguïté : la monnaie n’est pas neutre, une création monétaire "
  "excessive fait baisser artificiellement les taux d’intérêt, provoque un "
  "surinvestissement et peut conduire à des crises économiques ; "
  "contrairement aux néoclassiques, Hayek admet l’instabilité du capitalisme "
  "et la possibilité de crises. On obtient là le mécanisme complet d’une "
  "phase ascendante du crédit qui engendre sa propre crise : le taux bas est "
  "un faux signal, l’investissement se porte sur des projets qui ne seraient "
  "pas rentables à un taux normal, et la correction est inévitable. Troisième "
  "voie, le fonctionnement contemporain du crédit : dans les économies "
  "actuelles, la création monétaire dépend largement du crédit bancaire, "
  "puisque lorsque les banques commerciales accordent des prêts elles créent "
  "de la monnaie scripturale. Toute action de la banque centrale sur les "
  "conditions de refinancement, sur les taux d’intérêt ou sur la liquidité "
  "influence donc indirectement le volume du crédit, donc la création "
  "monétaire. Le cours nomme ce canal : la politique monétaire agit "
  "principalement par le canal du crédit bancaire, la banque centrale "
  "modifiant ses taux directeurs, ce qui influence le marché interbancaire, "
  "les taux bancaires, le coût du crédit, la demande de financement, la "
  "création monétaire, la demande globale et l’inflation. La phase "
  "descendante apparaît en miroir dans les objectifs assignés à la banque "
  "centrale : elle doit éviter le blocage du crédit et les emballements "
  "spéculatifs, et les politiques monétaires non conventionnelles ont "
  "précisément pour objet de rétablir la liquidité et de débloquer le crédit. "
  "La trappe à liquidité montre la limite de cette action : les agents "
  "conservent leurs liquidités, les banques restent prudentes et "
  "l’investissement ne repart pas suffisamment.",
  [("La phase d’expansion du crédit",
    "Les banques accordent des prêts et créent ainsi de la monnaie "
    "scripturale : le financement devient abondant, l’investissement "
    "progresse et la demande globale s’élève, ce qui valide a posteriori les "
    "anticipations optimistes."),
   ("Le faux signal du taux bas",
    "Avec Hayek, une création monétaire excessive fait baisser "
    "artificiellement les taux d’intérêt : le coût du capital ne reflète plus "
    "la rareté réelle de l’épargne et des projets peu rentables deviennent "
    "apparemment viables."),
   ("Le surinvestissement",
    "Les capacités créées excèdent les débouchés durables : le cours relie "
    "explicitement ce surinvestissement à la possibilité de crises "
    "économiques, ce qui fait de l’abondance du crédit la cause du "
    "retournement."),
   ("Le retournement et le blocage",
    "Lorsque les pertes apparaissent, les banques restreignent l’offre de "
    "crédit : le cours fait du blocage du crédit l’un des risques que la "
    "banque centrale doit précisément éviter, aux côtés des emballements "
    "spéculatifs."),
   ("L’aggravation par la contraction monétaire",
    "Comme la création monétaire dépend largement du crédit bancaire, la "
    "restriction du crédit réduit la monnaie en circulation, donc la demande "
    "globale : la contraction financière devient contraction réelle."),
   ("La limite de l’intervention",
    "Les politiques non conventionnelles visent à rétablir la liquidité et "
    "débloquer le crédit, mais en trappe à liquidité les agents conservent "
    "leurs liquidités, les banques restent prudentes et l’investissement ne "
    "repart pas suffisamment.")],
  [{'a': "Le crédit fournit un mécanisme d’amplification qui explique "
         "l’amplitude des cycles moyens sans recourir à un choc extérieur.",
    'cond': "L’argument suppose, comme l’établit le cours, que la création "
            "monétaire dépende largement du crédit bancaire et non d’une "
            "décision exogène de la banque centrale.",
    'lim': "Dans la lecture par le multiplicateur de crédit, la causalité "
           "part au contraire de la monnaie centrale : le volume du crédit "
           "serait alors contraint, non spontané."},
   {'a': "Avec Hayek, il donne une explication endogène du retournement : "
         "c’est l’expansion elle-même qui prépare la crise.",
    'cond': "Le raisonnement exige que les taux soient effectivement "
            "abaissés en deçà de leur niveau d’équilibre par la création "
            "monétaire.",
    'lim': "Le cours ne fournit pas de critère pour mesurer cet écart : "
           "l’analyse identifie le mécanisme mais ne permet pas de dater le "
           "retournement."},
   {'a': "Il éclaire la double mission de la banque centrale, qui doit "
         "éviter à la fois les emballements spéculatifs et le blocage du "
         "crédit.",
    'cond': "La mission suppose que la banque centrale dispose d’instruments "
            "agissant réellement sur le volume du crédit, ce que le cours "
            "établit avec les trois taux directeurs.",
    'lim': "Le cours souligne la tension : préserver la stabilité financière "
           "crée un risque d’aléa moral et peut encourager les comportements "
           "imprudents, donc l’emballement suivant."},
   {'a': "Il explique pourquoi la politique monétaire est plus efficace pour "
         "freiner que pour relancer.",
    'cond': "L’asymétrie suppose que la banque centrale puisse renchérir le "
            "crédit à volonté mais ne puisse forcer les banques à prêter ni "
            "les agents à emprunter.",
    'lim': "Le cours rappelle que les instruments non conventionnels "
           "existent précisément pour contourner cette asymétrie, par le "
           "rachat de titres et l’action sur les anticipations."},
   {'a': "Il relie l’instabilité financière à l’économie réelle par un canal "
         "identifié, celui du crédit bancaire.",
    'cond': "Le canal suppose que les banques répercutent effectivement les "
            "conditions de refinancement sur les taux offerts à leurs "
            "clients.",
    'lim': "Le cours montre qu’une partie du financement échappe à ce "
           "canal : le shadow banking crée de la liquidité et transforme les "
           "maturités hors du système bancaire traditionnel."}],
  [{'t': "La monnaie est neutre : une variation de sa quantité n’affecte que "
         "le niveau général des prix, pas la production réelle.",
    'qui': "La théorie quantitative de la monnaie, que le cours rattache à "
           "Irving Fisher et à l’idée de la monnaie comme voile.",
    'rep': "Le cours oppose explicitement Hayek sur ce point : la monnaie "
           "n’est pas neutre, une création excessive abaisse artificiellement "
           "les taux, provoque un surinvestissement et peut conduire à des "
           "crises."},
   {'t': "Le volume du crédit est déterminé par la base monétaire que la "
         "banque centrale contrôle : il n’y a donc pas d’emballement "
         "spontané.",
    'qui': "La lecture par le multiplicateur de crédit, rattachée au courant "
           "monétaire dans le cours.",
    'rep': "Le cours présente la thèse inverse du diviseur de crédit : la "
           "banque prête d’abord, puis se procure la monnaie centrale, de "
           "sorte que le crédit suit la demande de financement et non la base "
           "monétaire."},
   {'t': "Le retournement vient de l’épuisement des grappes d’innovations, "
         "non d’un excès de crédit.",
    'qui': "L’analyse schumpétérienne des cycles longs que le cours expose.",
    'rep': "Les deux lectures portent sur des temporalités différentes : le "
           "cours rattache l’innovation aux cycles longs de Kondratiev et le "
           "crédit aux cycles moyens de Juglar, de sorte qu’elles se "
           "superposent au lieu de se contredire."},
   {'t': "La relance par le crédit reste efficace : il suffit d’abaisser "
         "suffisamment les taux directeurs pour redémarrer l’investissement.",
    'qui': "La logique de la politique monétaire conventionnelle telle que "
           "le cours la décrit.",
    'rep': "Le cours constate la limite dans la trappe à liquidité : les "
           "taux sont déjà très bas, les agents préfèrent conserver des "
           "liquidités, les banques restent prudentes, et baisser encore les "
           "taux ne suffit plus."}],
  [{'n': "Friedrich Hayek",
    'i': "Une création monétaire excessive abaisse artificiellement les taux, "
         "provoque un surinvestissement et peut conduire à des crises.",
    'p': "Le cours en tire la conséquence théorique : contrairement aux "
         "néoclassiques, Hayek admet l’instabilité du capitalisme et la "
         "possibilité de crises, ce qui l’écarte de la thèse de la neutralité "
         "de la monnaie tout en restant dans la tradition libérale."},
   {'n': "Clément Juglar",
    'i': "Les cycles moyens, de huit à dix ans, sont associés à "
         "l’investissement productif et aux fluctuations du crédit.",
    'p': "Le cours leur attache les quatre phases de reprise, expansion, "
         "crise et dépression, et les juge particulièrement importants dans "
         "les économies capitalistes industrielles : le crédit y figure comme "
         "l’un des deux ressorts du cycle, à côté de l’investissement."},
   {'n': "Friedrich Hayek",
    'i': "Le marché est un processus de découverte dans un monde "
         "d’information dispersée, que les prix transmettent.",
    'p': "Le cours relie cette thèse à la précédente : si les prix "
         "transmettent l’information, un taux d’intérêt artificiellement "
         "abaissé transmet une information fausse, et c’est à ce titre que la "
         "création monétaire excessive égare les décisions d’investissement."}],
  [{'f': "Le cours rattache les cycles de Juglar, de huit à dix ans, à "
         "l’investissement productif et aux fluctuations du crédit.",
    'p': "Le fait montre que le crédit figure dans la typologie des cycles "
         "au même titre que l’investissement : son alternance est un "
         "mécanisme cyclique reconnu, et non une simple circonstance."},
   {'f': "La banque centrale doit éviter les crises bancaires, les paniques "
         "de liquidité, le blocage du crédit, les faillites systémiques et "
         "les emballements spéculatifs.",
    'p': "Cette liste démontre que les deux phases du cycle du crédit sont "
         "explicitement visées par la politique monétaire : l’emballement "
         "d’un côté, le blocage de l’autre."},
   {'f': "Les politiques monétaires non conventionnelles ont pour objectifs "
         "de rétablir la liquidité, débloquer le crédit, éviter la déflation, "
         "stabiliser les marchés et soutenir l’activité.",
    'p': "Les objectifs décrivent en creux la phase descendante du cycle du "
         "crédit : c’est bien le blocage du financement, et non seulement la "
         "faiblesse de la demande, que ces instruments cherchent à lever."},
   {'f': "En trappe à liquidité, les taux sont déjà très bas, les agents "
         "préfèrent conserver des liquidités et les banques restent "
         "prudentes.",
    'p': "Le fait prouve que le cycle du crédit n’est pas symétrique : la "
         "banque centrale peut freiner un emballement mais ne peut pas "
         "contraindre les banques à prêter ni les agents à emprunter."}],
  [{'q': "Sujet sur le rôle du crédit dans les fluctuations",
    'f': "Le crédit ne finance pas seulement le cycle, il le produit. Le "
         "cours rattache les cycles de Juglar, de huit à dix ans, à "
         "l’investissement productif et aux fluctuations du crédit, avec les "
         "quatre phases de reprise, expansion, crise et dépression. Comme la "
         "création monétaire dépend largement du crédit bancaire, "
         "l’expansion du crédit alimente la demande globale, et sa "
         "contraction la détruit.",
    'r': "On montre que le crédit intervient deux fois, comme condition du "
         "financement et comme source de la monnaie, ce qui explique son rôle "
         "amplificateur dans les deux sens.",
    'ex': "Le canal du crédit bancaire du cours : les taux directeurs "
          "influencent le coût du crédit, la création monétaire, puis la "
          "demande globale et l’inflation."},
   {'q': "Sujet sur la neutralité de la monnaie",
    'f': "Hayek fournit l’argument le plus net contre la neutralité de la "
         "monnaie à l’intérieur de la tradition libérale. Le cours le résume "
         "ainsi : la monnaie n’est pas neutre, une création monétaire "
         "excessive fait baisser artificiellement les taux d’intérêt, "
         "provoque un surinvestissement et peut conduire à des crises "
         "économiques. Contrairement aux néoclassiques, Hayek admet donc "
         "l’instabilité du capitalisme.",
    'r': "Le raisonnement passe par les prix comme vecteurs d’information : "
         "un taux faussé égare les décisions, ce qui rend la non-neutralité "
         "nuisible plutôt que utile.",
    'ex': "Le surinvestissement engendré par des taux artificiellement bas, "
          "que le cours relie à la possibilité de crises économiques."},
   {'q': "Sujet sur les limites de la politique monétaire",
    'f': "La politique monétaire n’agit pas symétriquement sur le cycle du "
         "crédit. Elle peut freiner un emballement spéculatif en renchérissant "
         "le refinancement, mais elle ne peut pas forcer la reprise du "
         "crédit : en trappe à liquidité, les taux sont déjà très bas, les "
         "agents préfèrent conserver des liquidités, les banques restent "
         "prudentes et l’investissement ne repart pas suffisamment.",
    'r': "On établit l’asymétrie en distinguant ce que la banque centrale "
         "contrôle, le prix du refinancement, et ce qu’elle ne contrôle pas, "
         "la décision de prêter et celle d’emprunter.",
    'ex': "Les politiques non conventionnelles, dont le cours fixe pour "
          "objectif de rétablir la liquidité et de débloquer le crédit."},
   {'q': "Sujet sur la stabilité financière comme objectif public",
    'f': "La banque centrale est prise entre les deux phases du cycle du "
         "crédit. Le cours énumère ce qu’elle doit éviter : les crises "
         "bancaires, les paniques de liquidité, le blocage du crédit, les "
         "faillites systémiques et les emballements spéculatifs. Mais il "
         "ajoute aussitôt la contradiction : préserver la stabilité "
         "financière crée un risque d’aléa moral et peut encourager les "
         "comportements imprudents.",
    'r': "On montre que l’instrument de stabilisation nourrit le "
         "comportement qu’il doit prévenir, ce qui fait de la régulation du "
         "crédit un problème sans solution définitive.",
    'ex': "La tension relevée par le cours entre stabilité financière et "
          "aléa moral dans les objectifs de la banque centrale."}],
  voisins=['n13-instabilite-financiere', 'n13-cycles-economiques',
           'n13-accelerateur', 'n13-crise-bancaire'])
