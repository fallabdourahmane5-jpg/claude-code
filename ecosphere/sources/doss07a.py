# -*- coding: utf-8 -*-
"""Ensemble 7 — La consommation, l’épargne et les comportements économiques
(1/3)."""

from doss_base import d

d('n7-consommation', 7, "Consommation",
  "L’emploi du revenu, et le principal déterminant de la demande",
  "La consommation désigne l’usage de biens et de services qui satisfont "
  "directement les besoins. Elle constitue le principal emploi du revenu des "
  "ménages et la composante majeure de la demande globale. Le cours en fait "
  "l’objet d’un débat théorique central : dépend-elle du revenu courant, comme "
  "le soutient Keynes, ou d’un revenu anticipé sur toute la vie, comme le "
  "soutiennent Friedman et Modigliani ?",
  "La consommation est un objet à la croisée de la microéconomie, de la "
  "macroéconomie et de la sociologie, et le cours l’aborde successivement par "
  "ces trois voies. La voie macroéconomique d’abord, avec Keynes, qui énonce "
  "dans la Théorie générale de l’emploi, de l’intérêt et de la monnaie (1936) "
  "la loi psychologique fondamentale : la consommation augmente avec le revenu "
  "mais à un rythme plus faible. Il en tire deux grandeurs : la propension "
  "moyenne à consommer, rapport entre la consommation totale et le revenu, "
  "qu’il juge décroissante, et la propension marginale à consommer, part du "
  "revenu supplémentaire consacrée à la consommation, comprise entre 0 et 1. "
  "La conséquence est politique : la baisse de la propension moyenne à "
  "consommer avec la croissance du revenu justifie l’intervention de l’État "
  "pour conserver l’équilibre économique. La voie de la contestation ensuite : "
  "Friedman observe que la consommation est en réalité beaucoup plus stable "
  "que le revenu, et conclut que les individus fondent leurs décisions sur le "
  "revenu qu’ils s’attendent à percevoir durablement ; Modigliani ajoute que "
  "la consommation dépend aussi de la richesse patrimoniale et de l’âge. Le "
  "cours note d’ailleurs que les vérifications empiriques ont nuancé Keynes, "
  "puisque après 1945 la part consommée du revenu s’est révélée assez stable à "
  "long terme. La voie sociologique enfin, avec Veblen : les comportements de "
  "consommation ne s’expliquent pas par la seule utilité mais par la "
  "distinction, la reconnaissance sociale et l’imitation. Reste un "
  "prolongement contemporain que le cours mentionne : le paradoxe d’Easterlin, "
  "selon lequel à long terme, quand le revenu moyen d’un pays augmente, le "
  "bonheur moyen n’augmente pas forcément.",
  [("L’arbitrage entre consommation et épargne",
    "Le revenu disponible se partage entre consommation et épargne : toute "
    "décision de consommer est simultanément une décision de ne pas épargner, "
    "et le taux d’intérêt sert d’arbitrage entre les deux."),
   ("La dépendance au revenu courant",
    "Dans l’analyse keynésienne, la consommation suit le revenu perçu à "
    "l’instant présent : elle augmente avec lui mais à un rythme plus faible, "
    "ce qui est la loi psychologique fondamentale."),
   ("Le lissage intertemporel",
    "Pour Friedman et Modigliani, les ménages lissent leur consommation sur "
    "la durée : elle dépend du revenu anticipé sur l’ensemble de la vie et du "
    "patrimoine, non du revenu du moment."),
   ("L’effet multiplicateur",
    "La consommation est une composante de la demande : une dépense "
    "supplémentaire devient le revenu d’un autre agent, qui en consomme une "
    "partie, d’où un effet cumulatif mesuré par le multiplicateur."),
   ("La détermination sociale des besoins",
    "La consommation n’exprime pas seulement une utilité individuelle : elle "
    "est aussi un instrument de distinction, de reconnaissance sociale et "
    "d’imitation, ce qui lui donne une dimension collective.")],
  [{'a': "L’analyse keynésienne donne à la consommation un rôle "
         "macroéconomique central, puisqu’elle commande la demande globale et "
         "donc l’activité.",
    'cond': "Le raisonnement suppose que la demande soit le facteur limitant "
            "de la production, hypothèse de courte période.",
    'lim': "Il suppose aussi que la propension moyenne à consommer décroisse "
           "avec le revenu, ce que les études postérieures à 1945 ont nuancé "
           "en montrant une part consommée assez stable à long terme."},
   {'a': "L’approche en revenu permanent explique une régularité robuste : la "
         "consommation est plus stable que le revenu.",
    'cond': "L’explication suppose que les ménages puissent emprunter ou "
            "désépargner pour lisser les fluctuations de revenu.",
    'lim': "Cette capacité fait défaut aux ménages contraints par la "
           "liquidité, pour lesquels la consommation suit effectivement le "
           "revenu courant."},
   {'a': "L’approche par le cycle de vie enrichit l’analyse en y intégrant "
         "la richesse patrimoniale et l’âge.",
    'cond': "Elle suppose des individus prévoyants, capables d’anticiper leurs "
            "besoins sur l’ensemble de leur existence.",
    'lim': "Cette hypothèse de prévoyance rationnelle est précisément celle "
           "que l’économie comportementale remet en cause."},
   {'a': "L’approche sociologique explique des comportements que l’utilité "
         "seule ne peut pas rendre intelligibles.",
    'cond': "Elle suppose que les biens consommés soient visibles par autrui et "
            "puissent servir de signe social.",
    'lim': "Elle s’applique mal aux consommations ordinaires et invisibles, "
           "qui constituent l’essentiel du budget des ménages."}],
  [{'t': "La consommation dépend du revenu courant, et sa propension moyenne "
         "décroît quand le revenu augmente.",
    'qui': "John Maynard Keynes, avec la loi psychologique fondamentale.",
    'rep': "Le cours relève que les vérifications empiriques postérieures à "
           "1945 ont montré une part consommée du revenu assez stable à long "
           "terme, ce qui nuance la décroissance annoncée."},
   {'t': "La consommation dépend du revenu anticipé sur toute la vie et non du "
         "revenu du moment.",
    'qui': "Milton Friedman, avec la théorie du revenu permanent.",
    'rep': "L’argument explique bien la stabilité observée de la "
           "consommation, mais il vise aussi explicitement à remettre en cause "
           "la justification keynésienne de l’intervention publique."},
   {'t': "La consommation dépend aussi de la richesse patrimoniale et de "
         "l’âge, et non du seul revenu courant.",
    'qui': "Franco Modigliani, avec le modèle du cycle de vie.",
    'rep': "Le cours souligne que son modèle complète Keynes plutôt qu’il ne "
           "le contredit : il explique comment consommation et épargne "
           "évoluent selon les étapes de la vie, ce que le modèle keynésien ne "
           "faisait pas."},
   {'t': "La consommation est un instrument de distinction sociale, non un "
         "simple acte d’utilité.",
    'qui': "Thorstein Veblen, avec la consommation ostentatoire.",
    'rep': "L’analyse est décisive pour comprendre certains biens, puisqu’elle "
           "explique des demandes croissantes avec le prix, impossibles dans "
           "le cadre standard."}],
  [{'n': "John Maynard Keynes",
    'i': "La consommation augmente avec le revenu mais à un rythme plus "
         "faible.",
    'p': "Le cours rattache cette loi psychologique fondamentale à la Théorie "
         "générale de l’emploi, de l’intérêt et de la monnaie (1936) et en "
         "tire deux grandeurs : la propension moyenne à consommer, "
         "décroissante selon lui, et la propension marginale, comprise entre "
         "0 et 1."},
   {'n': "Milton Friedman",
    'i': "La consommation est beaucoup plus stable que le revenu, car elle "
         "dépend du revenu permanent.",
    'p': "Le cours précise son intention : critiquer la thèse keynésienne du "
         "revenu courant afin de remettre en cause la justification de "
         "l’intervention publique fondée sur la baisse de la propension "
         "moyenne à consommer."},
   {'n': "Franco Modigliani",
    'i': "La consommation dépend du revenu courant, mais aussi de la richesse "
         "patrimoniale et de l’âge.",
    'p': "Son modèle du cycle de vie montre que les jeunes désépargnent, que "
         "les adultes épargnent durant leur vie active et que les retraités "
         "désépargnent à nouveau, ce qui explique l’évolution conjointe de la "
         "consommation et de l’épargne."},
   {'n': "Richard Easterlin",
    'i': "À long terme, quand le revenu moyen d’un pays augmente, le bonheur "
         "moyen n’augmente pas forcément.",
    'p': "Le cours situe ce paradoxe en 1974 et le place immédiatement après "
         "la loi psychologique fondamentale : il introduit une limite à "
         "l’identification entre hausse de la consommation et amélioration du "
         "bien-être."}],
  [{'f': "Keynes énonce la loi psychologique fondamentale dans la Théorie "
         "générale de l’emploi, de l’intérêt et de la monnaie, publiée en "
         "1936.",
    'p': "La référence est datable et permet de situer la consommation comme "
         "une variable macroéconomique à partir de la crise des années 1930."},
   {'f': "La propension moyenne à consommer est le rapport entre consommation "
         "totale et revenu ; la propension marginale est la part du revenu "
         "supplémentaire consacrée à la consommation, comprise entre 0 et 1.",
    'p': "Les deux définitions sont distinctes et souvent confondues : seule "
         "la seconde intervient dans le calcul du multiplicateur."},
   {'f': "Le cours relève qu’après 1945 les études ont montré que la part "
         "consommée du revenu reste assez stable à long terme.",
    'p': "Le fait constitue l’objection empirique à Keynes et ouvre la voie "
         "aux théories du revenu permanent et du cycle de vie."},
   {'f': "Richard Easterlin met en évidence en 1974 un paradoxe : la hausse du "
         "revenu moyen d’un pays n’augmente pas forcément le bonheur moyen.",
    'p': "Le fait relie la consommation à la question du bien-être et prépare "
         "la critique de la non-satiété par Kate Raworth."}],
  [{'q': "Sujet du type « De quoi dépend la consommation des ménages ? »",
    'f': "Trois réponses se succèdent historiquement. Pour Keynes, la "
         "consommation dépend du revenu courant selon la loi psychologique "
         "fondamentale, puisqu’elle augmente avec le revenu mais à un rythme "
         "plus faible. Pour Friedman, elle dépend du revenu permanent, car il "
         "observe qu’elle est beaucoup plus stable que le revenu. Pour "
         "Modigliani, elle dépend aussi de la richesse patrimoniale et de "
         "l’âge, les jeunes désépargnant, les adultes épargnant et les "
         "retraités désépargnant à nouveau.",
    'r': "Le raisonnement montre que chaque théorie répond à une anomalie "
         "laissée par la précédente, ce qui donne au débat une structure "
         "cumulative plutôt qu’une simple opposition d’écoles.",
    'ex': "La stabilité observée de la consommation après 1945, alors que la "
          "théorie keynésienne prévoyait une part consommée décroissante."},
   {'q': "Sujet du type « La consommation est-elle un acte individuel ? »",
    'f': "L’analyse standard la traite comme un arbitrage individuel sous "
         "contrainte de budget, mais Veblen rejette l’homo œconomicus et "
         "soutient que les comportements économiques sont socialement "
         "déterminés. La consommation devient alors un instrument de "
         "distinction, de reconnaissance sociale et de domination symbolique, "
         "et le mécanisme central est l’imitation : les classes inférieures "
         "cherchent à copier les signes de richesse de la classe de loisir.",
    'r': "Le raisonnement oppose deux définitions de l’acte de consommer, "
         "l’une par la satisfaction d’un besoin, l’autre par la production "
         "d’un signe, ce qui permet d’expliquer des comportements "
         "incompréhensibles dans le cadre standard.",
    'ex': "Les biens de Veblen, dont la demande augmente avec le prix parce "
          "que c’est le prix élevé qui fait le signe."}],
  voisins=['n7-propension', 'n7-revenu-permanent', 'n7-cycle-vie',
           'n7-ostentatoire'])


d('n7-utilite', 7, "Utilité et préférences",
  "Ordonner les paniers de biens : le socle du modèle du consommateur",
  "L’utilité désigne la satisfaction qu’un individu retire de la consommation "
  "d’un bien ; les préférences expriment la manière dont il ordonne les "
  "paniers de biens possibles. Le modèle standard suppose des préférences "
  "complètes, transitives, continues et non saturées, hypothèses qui "
  "permettent de représenter les choix par des courbes d’indifférence et de "
  "déterminer un optimum.",
  "La théorie de l’utilité est le socle de toute la microéconomie du "
  "consommateur, et le cours la présente de manière remarquablement critique, "
  "en examinant chaque hypothèse puis l’objection qu’elle appelle. La "
  "transitivité d’abord : si un individu préfère le panier D au panier A et le "
  "panier A au panier B, alors il doit préférer D à B — on ne peut pas revenir "
  "sur ses préférences de façon contradictoire. Mais le cours note que, "
  "d’après des vérifications empiriques, les individus ne sont pas transitifs "
  "dans leurs choix, et renvoie à la critique de Steve Keen dans L’imposture "
  "économique (2014). La continuité ensuite : elle n’est pas réaliste mais "
  "indispensable mathématiquement, car sans elle les courbes d’indifférence "
  "seraient discontinues, en marches d’escalier, et l’on ne pourrait ni "
  "dériver, ni optimiser, ni résoudre proprement les modèles. Le cours en tire "
  "une leçon méthodologique précieuse : l’hypothèse est faite pour résoudre "
  "des problèmes mathématiques, pas pour décrire parfaitement les "
  "comportements réels. La non-satiété enfin : le consommateur préfère "
  "toujours plus de biens à moins de biens, il n’existe pas de point de "
  "satiété et une augmentation de la consommation augmente toujours la "
  "satisfaction. Cette idée est controversée dans le contexte actuel, marqué "
  "par les critiques de la croissance infinie et la remise en cause de la "
  "surconsommation ; Kate Raworth demande pourquoi supposer que les individus "
  "veulent toujours consommer davantage et pourquoi exclure qu’on puisse "
  "préférer moins plutôt que plus. Mais l’hypothèse est nécessaire pour des "
  "raisons mathématiques : sans elle, les courbes d’indifférence pourraient "
  "devenir discontinues ou mal ordonnées, et l’on ne pourrait plus affirmer "
  "que les courbes plus éloignées de l’origine correspondent toujours à un "
  "niveau d’utilité plus élevé.",
  [("L’ordonnancement des paniers",
    "Le consommateur n’a pas besoin de mesurer sa satisfaction : il lui suffit "
    "de pouvoir classer les paniers entre eux, ce qui rend la théorie "
    "ordinale et non cardinale."),
   ("La transitivité comme condition de cohérence",
    "Si A est préféré à B et D à A, alors D doit être préféré à B : sans cette "
    "propriété, aucun classement stable n’existe et l’idée même d’optimum "
    "disparaît."),
   ("La continuité comme condition technique",
    "Sans continuité, les courbes d’indifférence seraient en marches "
    "d’escalier : on ne pourrait ni dériver, ni optimiser, ni résoudre "
    "proprement les modèles, d’où une hypothèse faite pour des raisons "
    "mathématiques."),
   ("La non-satiété et l’ordonnancement des courbes",
    "Puisque le consommateur préfère toujours plus à moins, les courbes "
    "d’indifférence plus éloignées de l’origine correspondent toujours à un "
    "niveau d’utilité plus élevé, ce qui donne un sens à la comparaison."),
   ("La convexité et le goût pour la diversité",
    "Les individus préfèrent une combinaison de biens plutôt qu’un seul bien, "
    "les biens n’étant pas des substituts parfaits : cette convexité garantit "
    "qu’il existe toujours une demande pour chaque bien.")],
  [{'a': "La théorie ordinale permet de modéliser les choix sans jamais "
         "mesurer la satisfaction, ce qui est une économie d’hypothèses "
         "considérable.",
    'cond': "Elle suppose seulement que l’individu soit capable de comparer "
            "deux paniers et de le faire de manière cohérente.",
    'lim': "Même cette exigence minimale est démentie empiriquement, le cours "
           "relevant que les individus ne sont pas transitifs dans leurs "
           "choix."},
   {'a': "Elle fournit une représentation graphique simple, les courbes "
         "d’indifférence, qui rend les arbitrages visibles.",
    'cond': "La représentation suppose la continuité des préférences, qui "
            "garantit des courbes régulières.",
    'lim': "Le cours est explicite : cette hypothèse n’est pas réaliste mais "
           "indispensable mathématiquement, ce qui en fait une convention "
           "plutôt qu’un constat."},
   {'a': "Elle permet de déduire des résultats forts, notamment l’existence "
         "d’un optimum sous contrainte de budget.",
    'cond': "L’optimum suppose la convexité des préférences, qui assure que la "
            "solution est unique et intérieure.",
    'lim': "Ces propriétés sont posées pour obtenir le résultat, ce qui expose "
           "la théorie au reproche de construire ses hypothèses en fonction de "
           "ses conclusions."},
   {'a': "Elle offre un cadre commun à l’ensemble de la microéconomie, du "
         "consommateur au producteur.",
    'cond': "La généralité suppose que les agents soient capables de "
            "maximiser, ce que l’hypothèse de rationalité postule.",
    'lim': "Herbert Simon montre que les agents recherchent des solutions "
           "satisfaisantes plutôt qu’optimales, ce qui atteint le principe "
           "même de la maximisation."}],
  [{'t': "Les individus ne sont pas transitifs dans leurs choix, comme le "
         "montrent les vérifications empiriques.",
    'qui': "Steve Keen, dans L’imposture économique (2014), très critique "
           "envers l’approche microéconomique.",
    'rep': "L’objection atteint une hypothèse minimale et donc particulièrement "
           "exposée : si le classement n’est pas cohérent, l’optimum perd son "
           "sens."},
   {'t': "Rien ne justifie de supposer que les individus veulent toujours et "
         "indéfiniment consommer davantage.",
    'qui': "Kate Raworth, avec l’économie du donut.",
    'rep': "La critique est fondée dans un contexte de remise en cause de la "
           "surconsommation, mais l’hypothèse reste nécessaire "
           "mathématiquement, faute de quoi les courbes d’indifférence "
           "pourraient devenir discontinues ou mal ordonnées."},
   {'t': "Les agents n’optimisent jamais vraiment : ils se contentent de "
         "rechercher des solutions satisfaisantes.",
    'qui': "Herbert Simon, avec la rationalité limitée.",
    'rep': "Le cours en fait le coup de grâce porté au modèle : même si les "
           "conditions mathématiques étaient remplies, les agents réels ne "
           "seraient pas capables de se comporter comme il l’exige."},
   {'t': "Les préférences ne sont pas fixes : elles dépendent de la manière "
         "dont le choix est présenté.",
    'qui': "Richard Thaler, avec le principe du nudge.",
    'rep': "L’objection est redoutable car elle ne porte pas sur la capacité "
           "de calcul mais sur l’objet même du calcul : ce n’est pas la "
           "rationalité qui change, c’est la formulation qui guide le choix."}],
  [{'n': "Steve Keen",
    'i': "Les comportements réels contredisent l’hypothèse de transitivité des "
         "préférences.",
    'p': "Le cours le cite pour L’imposture économique (2014) et le présente "
         "comme très critique envers l’approche microéconomique. Son "
         "objection porte sur l’hypothèse la plus élémentaire du modèle, celle "
         "sans laquelle aucun classement stable n’est possible."},
   {'n': "Kate Raworth",
    'i': "Pourquoi supposer que les individus veulent toujours consommer "
         "davantage, et pourquoi exclure qu’on puisse préférer moins ?",
    'p': "Sa critique de la non-satiété s’inscrit dans un contexte de remise "
         "en cause de la croissance infinie et de la surconsommation. Elle "
         "porte sur une hypothèse que le cours reconnaît par ailleurs "
         "indispensable pour des raisons purement mathématiques."},
   {'n': "Herbert Simon",
    'i': "Les individus recherchent des solutions satisfaisantes plutôt "
         "qu’optimales.",
    'p': "Sa rationalité limitée atteint non pas une hypothèse technique mais "
         "le principe du modèle : le cours souligne que la microéconomie "
         "standard est mathématiquement élégante et intellectuellement "
         "puissante, mais psychologiquement et sociologiquement très fragile."},
   {'n': "Thorstein Veblen",
    'i': "Les comportements économiques ne s’expliquent pas par l’utilité "
         "individuelle mais par les normes sociales.",
    'p': "Le cours relève qu’il rejette l’homo œconomicus, agent rationnel "
         "maximisateur, et fonde une critique du capitalisme centrée sur les "
         "institutions, les normes sociales et les comportements de "
         "consommation."}],
  [{'f': "Le cours énonce que la transitivité interdit de revenir sur ses "
         "préférences de façon contradictoire, mais que d’après les "
         "vérifications empiriques les gens ne sont pas transitifs.",
    'p': "L’écart entre l’hypothèse et l’observation est explicitement "
         "reconnu, ce qui autorise à discuter le modèle sans le caricaturer."},
   {'f': "Sans continuité, les courbes d’indifférence seraient discontinues, "
         "en marches d’escalier, et l’on ne pourrait ni dériver, ni optimiser, "
         "ni résoudre proprement les modèles.",
    'p': "La formulation montre que l’hypothèse a une fonction technique "
         "précise, ce qui permet d’en discuter l’usage sans en contester "
         "l’utilité."},
   {'f': "L’hypothèse de non-satiété signifie qu’il n’existe pas de point de "
         "satiété, que le consommateur n’est jamais totalement rassasié et "
         "qu’une augmentation de la consommation augmente toujours la "
         "satisfaction.",
    'p': "Les trois formulations équivalentes permettent de relier "
         "l’hypothèse microéconomique aux débats sur la croissance et la "
         "sobriété."},
   {'f': "Grâce à la non-satiété, les courbes d’indifférence plus éloignées de "
         "l’origine correspondent toujours à un niveau d’utilité plus élevé.",
    'p': "La conséquence graphique est ce qui rend la représentation "
         "opératoire : sans elle, on ne saurait pas dans quelle direction "
         "chercher l’optimum."}],
  [{'q': "Sujet du type « Les hypothèses de la microéconomie sont-elles "
         "réalistes ? »",
    'f': "Le cours répond franchement que non, tout en expliquant pourquoi "
         "elles sont maintenues. La continuité n’est pas réaliste mais elle "
         "est indispensable mathématiquement, car sans elle les courbes "
         "d’indifférence seraient en marches d’escalier et l’on ne pourrait ni "
         "dériver ni optimiser. La transitivité est démentie par les "
         "vérifications empiriques. La non-satiété est controversée dans un "
         "contexte de critique de la surconsommation. L’hypothèse est donc "
         "faite pour résoudre des problèmes mathématiques, pas pour décrire "
         "parfaitement les comportements réels.",
    'r': "Le raisonnement distingue la fonction instrumentale d’une hypothèse "
         "de sa prétention descriptive, ce qui permet d’évaluer le modèle sur "
         "ce qu’il prétend faire.",
    'ex': "La critique de Steve Keen dans L’imposture économique, qui attaque "
          "la transitivité à partir des comportements observés."},
   {'q': "Sujet du type « Faut-il supposer que les individus veulent toujours "
         "plus ? »",
    'f': "L’hypothèse de non-satiété pose que le consommateur préfère toujours "
         "plus de biens à moins de biens. Kate Raworth la conteste "
         "frontalement : pourquoi supposer que les individus veulent toujours "
         "consommer davantage, et pourquoi exclure l’idée que l’on puisse "
         "préférer moins plutôt que plus ? Mais le cours rappelle que "
         "l’hypothèse est nécessaire pour des raisons mathématiques, sans quoi "
         "les courbes d’indifférence pourraient devenir discontinues ou mal "
         "ordonnées.",
    'r': "Le raisonnement montre que la critique écologique de la "
         "surconsommation atteint un point technique du modèle standard, ce "
         "qui lui donne une portée théorique et pas seulement normative.",
    'ex': "Le paradoxe d’Easterlin, selon lequel la hausse du revenu moyen "
          "n’augmente pas forcément le bonheur moyen."}],
  voisins=['n7-choix', 'n7-contrainte-budgetaire', 'n7-rationalite-limitee',
           'n7-biais'])


d('n7-contrainte-budgetaire', 7, "Contrainte budgétaire",
  "Ce que le revenu et les prix rendent accessible",
  "La contrainte budgétaire délimite l’ensemble des paniers de biens qu’un "
  "consommateur peut acquérir compte tenu de son revenu et des prix. Elle se "
  "représente par la droite de budget, dont la pente est l’opposé du rapport "
  "des prix : c’est ce rapport qui exprime le taux auquel le marché permet "
  "d’échanger un bien contre l’autre.",
  "La contrainte budgétaire est l’élément qui transforme une structure de "
  "préférences en décision effective, et le cours l’analyse surtout par ses "
  "déplacements, qui sont la matière des exercices. Deux paramètres la "
  "déterminent : le revenu et les prix. Une variation de prix modifie le "
  "coefficient directeur de la droite de budget : le cours précise qu’une "
  "baisse du prix du bien X, pour un revenu considéré comme stable, rend la "
  "pente de la droite, égale à moins le rapport du prix de X sur le prix de Y, "
  "plus faible. Une variation de revenu produit un effet entièrement "
  "différent : la nouvelle droite de budget a la même pente que la précédente, "
  "elle lui est donc parallèle, mais elle se situe à droite — l’individu se "
  "déplace vers une courbe d’indifférence plus élevée puisque son revenu a "
  "augmenté. Cette distinction entre rotation et translation est la clé de "
  "l’exercice le plus classique du chapitre, la décomposition en effet de "
  "substitution et effet de revenu : une baisse de prix produit les deux "
  "simultanément, puisqu’elle modifie le rapport des prix et accroît le "
  "pouvoir d’achat réel. Le cours signale d’ailleurs que la baisse de prix "
  "donne l’impression que le revenu réel augmente alors que le revenu nominal "
  "est inchangé, ce qui permet de consommer plus des deux biens. Deux "
  "remarques complètent l’analyse. La première est que la contrainte "
  "budgétaire incarne l’idée centrale de rareté : le consommateur ne peut pas "
  "tout avoir, et s’il consomme plus du bien X il doit nécessairement renoncer "
  "à une partie du bien Y. La seconde est que, dans le modèle d’équilibre "
  "général, la question de la dotation initiale est posée explicitement : la "
  "dotation de survie d’Arrow et Debreu suppose que chaque agent possède un "
  "minimum de ressources au départ, sans quoi aucun échange n’est possible.",
  [("La délimitation de l’ensemble accessible",
    "Le revenu et les prix définissent ce que le consommateur peut acheter : "
    "tout panier situé au-delà de la droite de budget est hors d’atteinte, "
    "quelle que soit la satisfaction qu’il procurerait."),
   ("La pente comme taux d’échange marchand",
    "La pente de la droite est l’opposé du rapport des prix : elle indique "
    "combien d’unités de Y il faut céder sur le marché pour obtenir une unité "
    "supplémentaire de X."),
   ("La rotation sous l’effet d’un prix",
    "Une baisse du prix de X modifie le coefficient directeur de la droite "
    "pour un revenu stable : la pente devient plus faible, et la droite pivote "
    "autour de son point d’intersection avec l’axe de Y."),
   ("La translation sous l’effet du revenu",
    "Une hausse de revenu produit une droite de même pente, parallèle à la "
    "précédente mais située à droite : l’individu accède à une courbe "
    "d’indifférence plus élevée sans que les prix relatifs aient changé."),
   ("L’illusion de revenu réel",
    "Une baisse de prix donne l’impression que le revenu réel augmente alors "
    "que le revenu nominal est inchangé : on peut consommer plus de X et plus "
    "de Y, ce qui explique la présence simultanée de deux effets.")],
  [{'a': "La contrainte budgétaire traduit en termes opératoires la notion de "
         "rareté, qui fonde toute l’analyse économique.",
    'cond': "Elle suppose des prix donnés et un revenu connu, ce qui vaut pour "
            "un consommateur preneur de prix.",
    'lim': "Elle ne dit rien de la formation du revenu ni de celle des prix, "
           "qui sont déterminés ailleurs dans le système."},
   {'a': "Elle permet de distinguer rigoureusement l’effet d’un prix de "
         "l’effet d’un revenu, par la rotation et la translation de la droite.",
    'cond': "La distinction suppose que l’on raisonne toutes choses égales par "
            "ailleurs, en ne faisant varier qu’un paramètre à la fois.",
    'lim': "Dans la réalité, prix et revenus varient simultanément et les "
           "marchés sont interdépendants, de sorte qu’un choc se propage."},
   {'a': "Elle rend visible l’arbitrage auquel le consommateur est contraint, "
         "puisque consommer plus de X impose de renoncer à une partie de Y.",
    'cond': "L’arbitrage suppose que le revenu soit intégralement dépensé, "
            "hypothèse habituelle du modèle statique.",
    'lim': "Elle ignore l’épargne, c’est-à-dire l’arbitrage intertemporel, que "
           "les théories du revenu permanent et du cycle de vie placent au "
           "centre."},
   {'a': "Elle fournit le cadre de l’optimisation, puisque l’optimum se situe "
         "au point de tangence entre la droite et la courbe d’indifférence la "
         "plus élevée accessible.",
    'cond': "La tangence suppose des préférences convexes et continues, "
            "propriétés que le modèle se contente de postuler.",
    'lim': "Ces propriétés sont des hypothèses techniques, que le cours "
           "reconnaît faites pour des raisons mathématiques plutôt que par "
           "réalisme."}],
  [{'t': "Le modèle ignore que certains agents n’ont pas de ressources "
         "initiales suffisantes pour participer à l’échange.",
    'qui': "La condition de dotation de survie posée par Arrow et Debreu.",
    'rep': "L’objection est reconnue par le modèle lui-même, mais sa "
           "résolution suppose une intervention extérieure au marché — État, "
           "Église, institutions — ce qui contredit l’autosuffisance du "
           "marché."},
   {'t': "Raisonner toutes choses égales par ailleurs est trompeur, car les "
         "marchés sont interdépendants.",
    'qui': "La critique de l’équilibre partiel que le cours formule "
           "explicitement.",
    'rep': "La démarche reste légitime comme simplification scientifique, à "
           "condition de ne pas en conclure qu’un choc sur un marché reste "
           "sans effet sur les autres."},
   {'t': "La contrainte budgétaire statique ignore l’arbitrage entre présent "
         "et futur, qui est pourtant décisif.",
    'qui': "Les théories du revenu permanent et du cycle de vie, chez Friedman "
           "et Modigliani.",
    'rep': "L’objection est fondée : elles montrent que la consommation dépend "
           "du revenu anticipé sur toute la vie et du patrimoine, ce qui "
           "suppose une contrainte intertemporelle et non ponctuelle."},
   {'t': "Les décisions réelles ne résultent pas d’une optimisation sous "
         "contrainte mais de références arbitraires.",
    'qui': "Daniel Kahneman, avec l’effet d’ancrage.",
    'rep': "L’expérience du cours est frappante : le prix proposé pour une "
           "bouteille de vin est souvent proche du numéro de sécurité sociale "
           "des participants, pourtant sans rapport avec le vin."}],
  [{'n': "Kenneth Arrow",
    'i': "Chaque agent doit posséder un minimum de ressources au départ pour "
         "que l’échange soit possible.",
    'p': "Avec Debreu, il pose la dotation de survie parmi les sept conditions "
         "de l’équilibre général. Le cours en tire une critique majeure : "
         "cette dotation suppose une intervention extérieure au marché, ce qui "
         "contredit l’idée que le marché se suffit à lui-même."},
   {'n': "Milton Friedman",
    'i': "La contrainte pertinente n’est pas le revenu du moment mais le "
         "revenu anticipé sur toute la vie.",
    'p': "Sa théorie du revenu permanent déplace la contrainte budgétaire du "
         "plan statique au plan intertemporel : le revenu courant se "
         "décompose en une partie permanente, stable et anticipée, et une "
         "partie transitoire, temporaire et aléatoire."},
   {'n': "Daniel Kahneman",
    'i': "Les décisions sont influencées par des références arbitraires sans "
         "rapport avec l’objet du choix.",
    'p': "L’expérience que le cours rapporte est explicite : on demande aux "
         "participants leurs deux derniers chiffres de sécurité sociale, puis "
         "combien ils paieraient une bouteille de vin, et le prix donné est "
         "souvent proche de ce numéro."}],
  [{'f': "La pente de la droite de budget est l’opposé du rapport du prix de X "
         "sur le prix de Y.",
    'p': "L’expression donne le contenu économique de la pente : elle mesure "
         "le taux d’échange que le marché impose entre les deux biens."},
   {'f': "Une baisse du prix de X modifie le coefficient directeur de la "
         "droite de budget pour un revenu stable, la pente devenant plus "
         "faible.",
    'p': "La formulation du cours décrit une rotation et non un déplacement "
         "parallèle, ce qui est la différence décisive avec l’effet de revenu."},
   {'f': "Après une hausse de revenu, la nouvelle droite de budget a la même "
         "pente que la précédente, lui est parallèle, et se situe à sa droite.",
    'p': "La formulation décrit une translation : les prix relatifs étant "
         "inchangés, seul l’ensemble accessible s’élargit."},
   {'f': "Une baisse de prix donne l’impression que le revenu réel augmente "
         "alors que le revenu nominal est inchangé, de sorte qu’on peut "
         "consommer plus de X et plus de Y.",
    'p': "Le fait explique pourquoi une simple variation de prix produit deux "
         "effets distincts et prépare la décomposition en effet de "
         "substitution et effet de revenu."}],
  [{'q': "Sujet du type « Comment le consommateur choisit-il ? »",
    'f': "Le choix résulte de la rencontre entre ce qu’il souhaite et ce qu’il "
         "peut. Les préférences, représentées par les courbes d’indifférence, "
         "disent ce qu’il souhaite ; la contrainte budgétaire, représentée par "
         "la droite de budget dont la pente est l’opposé du rapport des prix, "
         "dit ce qu’il peut. L’arbitrage est inévitable, puisque le "
         "consommateur ne peut pas tout avoir : s’il consomme plus du bien X, "
         "il doit nécessairement renoncer à une partie du bien Y.",
    'r': "Le raisonnement sépare le subjectif, les préférences, de l’objectif, "
         "le revenu et les prix, ce qui permet d’attribuer chaque changement "
         "de comportement à sa cause propre.",
    'ex': "Le taux marginal de substitution, qui mesure le renoncement "
          "subjectif et que l’optimum égalise au rapport des prix."},
   {'q': "Sujet du type « Une baisse de prix améliore-t-elle le sort du "
         "consommateur ? »",
    'f': "Elle agit par deux canaux qu’il faut distinguer. D’une part elle "
         "modifie le coefficient directeur de la droite de budget, dont la "
         "pente devient plus faible : c’est le changement des prix relatifs. "
         "D’autre part elle donne l’impression que le revenu réel augmente "
         "alors que le revenu nominal est inchangé, de sorte qu’on peut "
         "consommer plus des deux biens : c’est le gain de pouvoir d’achat.",
    'r': "Le raisonnement montre qu’une seule variation observable produit "
         "deux effets théoriques distincts, ce qui est la base de la "
         "décomposition en effet de substitution et effet de revenu.",
    'ex': "Le déplacement vers une courbe d’indifférence plus élevée, qui "
          "traduit le gain de satisfaction permis par la baisse de prix."}],
  voisins=['n7-choix', 'n7-utilite', 'n7-effet-revenu-substitution',
           'n7-elasticites'])
