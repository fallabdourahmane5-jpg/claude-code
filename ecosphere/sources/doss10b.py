# -*- coding: utf-8 -*-
"""Ensemble 10 — Le travail, l’emploi et le chômage (2/4)."""

from doss_base import d

d('n10-chomage-conj-struct', 10, "Chômage conjoncturel et structurel",
  "Un chômage que la reprise résorbe, et un chômage qui lui survit",
  "Le chômage conjoncturel est celui qui résulte d’un ralentissement "
  "temporaire de l’activité et que la reprise résorbe ; le chômage structurel "
  "est celui qui subsiste indépendamment de la conjoncture, parce qu’il est "
  "inscrit dans les structures de l’économie. Le cours rattache le premier à "
  "l’insuffisance de la demande effective chez Keynes, et le second à "
  "plusieurs mécanismes durables.",
  "La distinction entre chômage conjoncturel et chômage structurel n’est pas "
  "présentée par le cours comme une typologie à retenir mais comme une "
  "question de diagnostic, dont dépend entièrement la politique à conduire. Du "
  "côté conjoncturel, l’analyse est keynésienne : le chômage keynésien est "
  "involontaire et lié à une insuffisance de la demande effective, et il est "
  "compatible avec un équilibre économique, l’économie pouvant rester à un "
  "équilibre de sous-emploi où les entreprises sont satisfaites de leur niveau "
  "de production et les ménages consomment ce qu’ils peuvent. Le cours "
  "détaille le cercle vicieux : les entreprises produisent peu, donc "
  "embauchent peu, donc les ménages ont peu de revenus, donc consomment peu, "
  "donc les entreprises ont raison de produire peu. Rien ne pousse "
  "spontanément l’économie à repartir, ce qui justifie l’intervention "
  "publique. Du côté structurel, le cours mobilise trois mécanismes distincts. "
  "Celui de Friedman d’abord : il existe un taux de chômage naturel, niveau "
  "incompressible lié aux frictions du marché du travail, information "
  "imparfaite et mobilité, de sorte que toute tentative de le réduire par la "
  "relance conduit uniquement à plus d’inflation, la courbe de Phillips étant "
  "verticale à long terme. Celui du désalignement démographique ensuite : si "
  "la population active augmente plus vite que les capacités productives, "
  "l’économie ne peut pas absorber toute la main-d’œuvre, et le cours parle "
  "alors de chômage structurel, précisant que ces déséquilibres ne sont pas "
  "temporaires. Celui de Marx enfin : le capitalisme entretient une "
  "surpopulation relative, excédentaire non pas absolument mais relativement "
  "aux besoins du capital, d’où un chômage structurel. Le cours ajoute un cas "
  "intermédiaire, celui de la stagnation séculaire, où croissance faible, "
  "output gaps négatifs persistants et chômage durable ne relèvent plus "
  "seulement d’un choc conjoncturel.",
  [("Le mécanisme conjoncturel de la demande",
    "Une demande anticipée insuffisante conduit les entreprises à produire et "
    "embaucher peu, ce qui réduit les revenus et donc la consommation : la "
    "boucle est stable et aucun agent n’a individuellement intérêt à en "
    "sortir."),
   ("Le caractère auto-entretenu de l’équilibre de sous-emploi",
    "Les entreprises écoulent leur production, les ménages consomment ce "
    "qu’ils peuvent, les marchés sont stables, et pourtant il subsiste du "
    "chômage : l’économie est à l’équilibre, mais à un mauvais équilibre."),
   ("Le plancher incompressible des frictions",
    "L’information imparfaite et la mobilité limitée empêchent un appariement "
    "instantané entre postes et travailleurs : un niveau de chômage subsiste "
    "même en haute conjoncture, que la relance ne peut pas réduire."),
   ("Le désalignement entre main-d’œuvre et capacités",
    "Si la population active croît plus vite que les capacités productives, "
    "l’économie ne peut pas employer toute la main-d’œuvre : le chômage "
    "procède alors d’une insuffisance de capital et non de demande."),
   ("La reproduction d’une armée de réserve",
    "Chez Marx, le capitalisme entretient une masse de travailleurs "
    "disponibles, en surpopulation relative aux besoins du capital : le "
    "chômage n’est pas un accident mais une condition du rapport salarial.")],
  [{'a': "La distinction commande le choix de la politique économique, ce qui "
         "en fait un enjeu pratique et non une classification scolaire.",
    'cond': "Elle suppose que l’on sache identifier, pour une période donnée, "
            "lequel des deux chômages est dominant.",
    'lim': "Ce diagnostic est précisément ce qui est contesté : la "
           "stagnation séculaire montre qu’un chômage durable peut "
           "longtemps être lu comme conjoncturel avant d’apparaître "
           "structurel."},
   {'a': "L’analyse keynésienne explique un fait que l’ajustement par les "
         "prix exclut : la persistance du chômage sans retour spontané au "
         "plein-emploi.",
    'cond': "Elle suppose que la demande soit le facteur limitant de la "
            "production, donc une situation de sous-utilisation des "
            "capacités.",
    'lim': "Si l’offre est le facteur limitant, faute de rentabilité, une "
           "relance alimenterait les prix plutôt que l’emploi, ce qui est "
           "précisément le cas du chômage classique."},
   {'a': "Le taux de chômage naturel fournit une borne utile à "
         "l’interprétation des statistiques de chômage.",
    'cond': "Il suppose que les frictions, information imparfaite et "
            "mobilité, soient effectivement irréductibles à court terme.",
    'lim': "Le niveau de ce taux n’est pas observable : le qualifier de "
           "naturel risque de faire passer pour une donnée ce qui dépend des "
           "institutions du marché du travail."},
   {'a': "Rapporter le chômage structurel aux capacités productives relie "
         "l’emploi à l’accumulation du capital et non au seul coût du "
         "travail.",
    'cond': "L’argument suppose les capacités productives relativement "
            "rigides à court et moyen terme, l’investissement ne "
            "s’ajustant pas immédiatement.",
    'lim': "L’investissement peut s’ajuster à la main-d’œuvre disponible, ce "
           "qui rend le désalignement transitoire plutôt que définitif."}],
  [{'t': "Le chômage est involontaire et résulte d’une insuffisance de la "
         "demande effective, de sorte qu’il peut être durable sans que les "
         "marchés le corrigent.",
    'qui': "John Maynard Keynes, avec l’équilibre de sous-emploi.",
    'rep': "Les monétaristes objectent qu’il existe un taux de chômage "
           "naturel incompressible et que toute tentative de le réduire par "
           "la relance conduit uniquement à plus d’inflation, la courbe de "
           "Phillips étant verticale à long terme."},
   {'t': "Il existe un niveau de chômage naturel, lié aux frictions du marché "
         "du travail, que la politique économique ne peut pas réduire.",
    'qui': "Milton Friedman, dans la critique monétariste du keynésianisme.",
    'rep': "La théorie du déséquilibre répond qu’il peut exister une "
           "situation stable comportant du chômage involontaire sans "
           "incitation individuelle à changer de comportement, ce qui rend "
           "l’intervention publique nécessaire."},
   {'t': "Le chômage structurel résulte du capitalisme lui-même, qui "
         "entretient une surpopulation relative aux besoins du capital.",
    'qui': "Karl Marx, dans sa critique de Malthus.",
    'rep': "L’analyse relie le chômage au rapport salarial plutôt qu’à la "
           "conjoncture, mais elle n’explique pas les variations du chômage "
           "d’une période à l’autre, que les analyses conjoncturelles "
           "rendent mieux."}],
  [{'n': "John Maynard Keynes",
    'i': "Le chômage keynésien est involontaire, lié à une insuffisance de la "
         "demande effective et compatible avec un équilibre économique.",
    'p': "Le cours en détaille le cercle vicieux : les entreprises produisent "
         "peu, donc embauchent peu, donc les ménages ont peu de revenus, donc "
         "consomment peu, donc les entreprises ont raison de produire peu, et "
         "rien ne pousse spontanément l’économie à repartir."},
   {'n': "Milton Friedman",
    'i': "Il existe un taux de chômage naturel, incompressible, lié aux "
         "frictions du marché du travail.",
    'p': "Le cours précise les frictions en jeu, information imparfaite et "
         "mobilité, et la conséquence de politique économique : toute "
         "tentative de réduire ce chômage par la relance conduit uniquement à "
         "plus d’inflation, la courbe de Phillips étant verticale à long "
         "terme."},
   {'n': "Karl Marx",
    'i': "Le capitalisme entretient une surpopulation relative, excédentaire "
         "au regard des besoins du capital.",
    'p': "Le cours l’oppose à Malthus : la pauvreté ne vient pas d’un excès "
         "naturel de population mais du capitalisme, qui par l’exploitation "
         "des travailleurs, l’accaparement de la plus-value et la faiblesse "
         "des salaires engendre un chômage structurel."},
   {'n': "Edmond Malinvaud",
    'i': "Le chômage est keynésien ou classique selon que la demande de biens "
         "ou l’offre constitue le côté court du marché.",
    'p': "Le cours en tire la conséquence décisive pour le diagnostic : "
         "lorsque la demande est le côté court, une relance est efficace ; "
         "lorsque c’est l’offre, faute de rentabilité, une relance "
         "alimenterait les prix et non l’emploi."}],
  [{'f': "Le cours décrit l’équilibre de sous-emploi comme une situation où "
         "les entreprises sont satisfaites de leur niveau de production, les "
         "ménages consomment ce qu’ils peuvent, les marchés sont stables, et "
         "où il existe pourtant du chômage.",
    'p': "La description montre que le chômage conjoncturel peut être stable, "
         "ce qui ruine l’idée qu’il se résorberait mécaniquement avec le "
         "temps."},
   {'f': "Le cours relève qu’après 2008, croissance effective durablement "
         "faible, recul de la croissance potentielle, persistance d’output "
         "gaps négatifs, faiblesse de l’investissement et chômage durable "
         "coexistent.",
    'p': "Cette conjonction de symptômes établit qu’un chômage longtemps "
         "qualifié de conjoncturel peut relever d’un problème plus "
         "structurel."},
   {'f': "Dans l’analyse du désalignement démographique, si la population "
         "active augmente plus vite que les capacités productives, l’économie "
         "ne peut pas absorber toute la main-d’œuvre, ce que le cours "
         "qualifie de chômage structurel.",
    'p': "Le mécanisme montre que le chômage structurel peut procéder d’une "
         "insuffisance de capital et non d’un défaut du marché du travail."}],
  [{'q': "La croissance suffit-elle à créer des emplois ?",
    'f': "La réponse dépend de la nature du chômage. Si le chômage est "
         "conjoncturel, lié à une insuffisance de la demande effective, la "
         "reprise de l’activité le résorbe et la relance est efficace. Si "
         "une part importante du chômage est structurelle, frictions, "
         "insuffisance de capacités productives ou mécanismes inscrits dans "
         "le rapport salarial, la croissance seule laisse subsister un "
         "noyau.",
    'r': "Le raisonnement conditionne la réponse au diagnostic, puis montre "
         "que les deux types de chômage coexistent, ce qui impose de "
         "combiner les instruments.",
    'ex': "Friedman soutient que réduire le chômage naturel par la relance ne "
          "produit que de l’inflation."},
   {'q': "Le chômage peut-il être durable sans être structurel ?",
    'f': "Oui, et c’est l’apport de l’équilibre de sous-emploi : les "
         "entreprises écoulent leur production, les ménages consomment ce "
         "qu’ils peuvent, les marchés sont stables, et pourtant du chômage "
         "subsiste. L’économie est à l’équilibre, mais à un mauvais "
         "équilibre, dont aucun agent n’a individuellement intérêt à sortir.",
    'r': "Le raisonnement dissocie la durée du chômage de sa cause "
         "structurelle, ce qui montre qu’un chômage de demande peut "
         "s’installer sans correction spontanée.",
    'ex': "Le cercle vicieux décrit par le cours est explicitement qualifié "
          "de stable."},
   {'q': "Comment distinguer en pratique les deux chômages ?",
    'f': "Malinvaud fournit le critère opératoire : il faut regarder quel "
         "côté du marché est le côté court. Si c’est la demande de biens, le "
         "chômage est keynésien et la relance efficace ; si c’est l’offre, "
         "faute de rentabilité, le chômage est classique et la relance "
         "alimenterait les prix. Le diagnostic précède donc la politique.",
    'r': "On remplace une typologie descriptive par un test, ce qui transforme "
         "la distinction en instrument de décision économique.",
    'ex': "Le cours relève qu’après 2008 les symptômes observés suggèrent un "
          "problème plus structurel que conjoncturel."}],
  voisins=['n10-chomage-classique-keynesien', 'n10-marche-travail',
           'n10-population-active', 'n10-progres-technique-biaise'])


d('n10-chomage-classique-keynesien', 10, "Chômage classique et keynésien",
  "Quel côté du marché est le côté court ?",
  "Chez Edmond Malinvaud, le chômage est keynésien lorsque la demande de biens "
  "constitue le côté court du marché, auquel cas une relance est efficace, et "
  "classique lorsque c’est l’offre qui l’est, faute de rentabilité, auquel cas "
  "une relance alimenterait les prix. Le cours fait de cette distinction le "
  "critère qui commande le choix de la politique économique.",
  "Le cours construit cette opposition en partant de l’analyse keynésienne, "
  "puis en montrant comment la théorie du déséquilibre la généralise. "
  "L’analyse keynésienne d’abord. Keynes rejette l’idée que le travail soit un "
  "marché comme les autres : les salaires sont rigides à la baisse, les "
  "travailleurs négocient surtout les salaires nominaux, le salaire réel n’est "
  "pas parfaitement ajustable, et la baisse des salaires ne supprime pas le "
  "chômage, elle peut même aggraver la crise en réduisant la demande. Le "
  "chômage keynésien est donc involontaire, lié à une insuffisance de la "
  "demande effective, et compatible avec un équilibre économique : il existe "
  "un équilibre de sous-emploi. Le cours double ce raisonnement d’un schéma "
  "microéconomique : l’offre de travail est croissante avec le salaire, la "
  "demande de travail décroissante, le salaire est fixé à un niveau minimum "
  "par les conventions, le salaire minimum, les rigidités et la négociation "
  "collective, et à ce salaire l’offre de travail dépasse la demande, ce qui "
  "fait apparaître une zone de chômage involontaire où les travailleurs "
  "veulent travailler au salaire en vigueur mais les entreprises n’embauchent "
  "pas. La théorie du déséquilibre ensuite, développée à partir de la fin des "
  "années 1960 par Clower, Leijonhufvud et Malinvaud en réaction au modèle "
  "des équilibres simultanés et au cadre walrasien : les prix et salaires sont "
  "rigides, l’ajustement se fait par les quantités, production et emploi, le "
  "rationnement est possible et le déséquilibre peut être durable. Clower "
  "distingue la demande notionnelle, ce que les agents voudraient faire, de la "
  "demande effective, ce qu’ils peuvent réellement faire compte tenu de leurs "
  "revenus : rationnés sur le marché du travail, les travailleurs voient leurs "
  "revenus diminuer et leur demande de biens contrainte. Malinvaud en tire le "
  "critère du côté court, qui décide de l’efficacité d’une relance.",
  [("La rigidité du salaire réel",
    "Les travailleurs négociant les salaires nominaux et le salaire réel "
    "n’étant pas parfaitement ajustable, le prix du travail ne descend pas "
    "librement : l’ajustement se reporte nécessairement sur les quantités, "
    "donc sur l’emploi."),
   ("L’insuffisance de la demande effective",
    "La production et l’emploi sont déterminés par la demande que les "
    "entrepreneurs anticipent : si celle-ci est insuffisante, un chômage "
    "involontaire apparaît sans qu’aucun marché ne soit en désordre."),
   ("Le rationnement et sa transmission",
    "Rationnés sur le marché du travail, les travailleurs voient leur revenu "
    "diminuer et leur demande de biens contrainte : le déséquilibre d’un "
    "marché se propage aux autres, ce que la distinction entre demande "
    "notionnelle et demande effective permet de formaliser."),
   ("Le critère du côté court",
    "Lorsque la demande de biens est le côté court du marché, augmenter la "
    "demande accroît la production et l’emploi ; lorsque c’est l’offre, faute "
    "de rentabilité, la même mesure n’augmente que les prix."),
   ("L’ajustement par les quantités",
    "Les prix étant rigides, l’économie s’ajuste par la production et "
    "l’emploi : le déséquilibre peut donc durer, et l’intervention publique "
    "devient une condition du retour à l’activité plutôt qu’une "
    "perturbation.")],
  [{'a': "La distinction fournit un critère de politique économique "
         "directement opératoire, puisqu’elle indique quand une relance est "
         "efficace.",
    'cond': "Elle suppose que l’on puisse identifier empiriquement quel côté "
            "du marché est le côté court à un moment donné.",
    'lim': "Cette identification est difficile : un même niveau de chômage "
           "peut être lu comme keynésien ou classique selon le diagnostic "
           "porté sur la rentabilité des entreprises."},
   {'a': "L’analyse keynésienne rend compte d’un fait massif que "
         "l’ajustement par les prix exclut : la Grande Dépression et le "
         "chômage de masse durable des années 1930.",
    'cond': "Elle suppose la demande comme facteur limitant, donc une "
            "sous-utilisation des capacités de production.",
    'lim': "Le cours rappelle que les années 1970 lui ont opposé la "
           "stagflation, c’est-à-dire la coexistence d’inflation et de "
           "chômage, que les modèles keynésiens traditionnels n’expliquaient "
           "pas."},
   {'a': "La théorie du déséquilibre fournit un fondement microéconomique à "
         "la persistance du chômage, ce que le modèle des équilibres "
         "simultanés ne faisait pas.",
    'cond': "Elle exige des prix et des salaires effectivement rigides et la "
            "possibilité d’un rationnement des agents.",
    'lim': "Le cours relève que ces auteurs raisonnent contre le cadre "
           "walrasien : la portée de leur analyse dépend donc du degré réel "
           "de rigidité, qui varie selon les économies et les périodes."},
   {'a': "Le chômage classique désigne un mécanisme distinct, la faiblesse de "
         "la rentabilité, et non simplement un chômage que l’on refuserait de "
         "traiter.",
    'cond': "Il suppose que la contrainte pèse sur l’offre, les entreprises "
            "n’ayant pas intérêt à produire davantage aux conditions "
            "existantes.",
    'lim': "Le remède correspondant, restaurer le taux de marge, peut réduire "
           "la demande adressée aux entreprises si la modération salariale "
           "est générale."}],
  [{'t': "Le chômage est involontaire et lié à une insuffisance de la demande "
         "effective, de sorte que la relance de la demande est le remède "
         "approprié.",
    'qui': "John Maynard Keynes, dans la Théorie générale de l’emploi, de "
           "l’intérêt et de la monnaie, en 1936.",
    'rep': "Malinvaud précise la condition de validité : la relance n’est "
           "efficace que si la demande de biens est le côté court du marché ; "
           "si c’est l’offre, faute de rentabilité, elle alimenterait les "
           "prix."},
   {'t': "Pour relancer l’économie, il faut agir sur l’offre, restaurer le "
         "taux de marge des entreprises et libéraliser les économies.",
    'qui': "Les libéraux, dans le contexte de crise du keynésianisme des "
           "années 1970.",
    'rep': "La théorie du déséquilibre objecte que les marchés ne "
           "s’auto-ajustent pas : il peut exister un équilibre de sous-emploi "
           "stable, de sorte que l’intervention de l’État devient une "
           "condition du retour à l’activité."},
   {'t': "La baisse des salaires permet de résorber le chômage en rétablissant "
         "l’équilibre du marché du travail.",
    'qui': "L’analyse néoclassique du marché du travail.",
    'rep': "Keynes répond que la baisse des salaires ne supprime pas le "
           "chômage et peut même aggraver la crise en réduisant la demande, "
           "le salaire étant à la fois un coût pour l’entreprise et un revenu "
           "pour le salarié."}],
  [{'n': "Edmond Malinvaud",
    'i': "Le chômage est keynésien lorsque la demande de biens est le côté "
         "court du marché, et classique lorsque c’est l’offre.",
    'p': "Le cours en tire la conséquence pratique : dans le premier cas une "
         "relance est efficace, dans le second, faute de rentabilité, elle "
         "alimenterait les prix. Le diagnostic sur le côté court précède donc "
         "nécessairement le choix de la politique."},
   {'n': "John Maynard Keynes",
    'i': "Le chômage keynésien est involontaire et compatible avec un "
         "équilibre économique.",
    'p': "Le cours en déduit l’équilibre de sous-emploi : les entreprises "
         "sont satisfaites de leur niveau de production, les ménages "
         "consomment ce qu’ils peuvent, les marchés sont stables, et "
         "l’économie se maintient pourtant à un mauvais équilibre dont rien "
         "ne la fait sortir."},
   {'n': "Robert Clower",
    'i': "Les agents ne prennent pas toujours leurs décisions dans un cadre "
         "libre : il faut distinguer demande notionnelle et demande "
         "effective.",
    'p': "Le cours applique la distinction au chômage : les travailleurs sont "
         "rationnés sur le marché du travail, leurs revenus diminuent et leur "
         "demande sur le marché des biens est contrainte, de sorte que les "
         "comportements observés ne sont pas des comportements d’équilibre."},
   {'n': "Axel Leijonhufvud",
    'i': "L’économie peut fonctionner durablement hors équilibre, les marchés "
         "ne s’auto-ajustant pas.",
    'p': "Le cours le range avec Clower et Malinvaud parmi les fondateurs de "
         "la théorie du déséquilibre, développée à partir de la fin des "
         "années 1960 en réaction au cadre walrasien d’équilibre général et "
         "au modèle des équilibres simultanés."},
   {'n': "Milton Friedman",
    'i': "À long terme, la courbe de Phillips est verticale : il n’existe pas "
         "d’arbitrage durable entre inflation et chômage.",
    'p': "Le cours en fait l’argument décisif de la critique monétariste : "
         "puisqu’il existe un taux de chômage naturel lié aux frictions, "
         "toute tentative de le réduire par la relance conduit uniquement à "
         "plus d’inflation."}],
  [{'f': "Le cours rappelle que Keynes écrit dans un contexte de Grande "
         "Dépression, marqué par un chômage de masse durable et par l’échec "
         "des mécanismes de marché à rétablir spontanément le plein-emploi.",
    'p': "Ce contexte justifie la rupture théorique : c’est l’incapacité "
         "observée des marchés à se corriger qui impose d’abandonner "
         "l’hypothèse d’ajustement automatique."},
   {'f': "La théorie du déséquilibre se développe à partir de la fin des "
         "années 1960 en réaction au cadre walrasien, à partir du constat que "
         "les économies connaissent un chômage durable et que les ajustements "
         "par les prix sont limités.",
    'p': "La datation montre que la critique vient de l’intérieur de la "
         "discipline et s’appuie sur des faits, et non d’une préférence "
         "doctrinale pour l’intervention publique."},
   {'f': "Les années 1970 sont marquées par les chocs pétroliers de 1973 et "
         "1979 et par une stagflation inédite associant inflation et chômage, "
         "que la courbe de Phillips n’expliquait pas.",
    'p': "Ce fait explique le basculement vers les analyses de l’offre : la "
         "coexistence d’inflation et de chômage disqualifiait le diagnostic "
         "purement keynésien."}],
  [{'q': "Le chômage s’explique-t-il par un coût du travail trop élevé ?",
    'f': "C’est exactement l’alternative que formalise Malinvaud. Si l’offre "
         "est le côté court du marché, faute de rentabilité, le diagnostic "
         "est juste et une relance de la demande n’augmenterait que les "
         "prix. Mais si la demande de biens est le côté court, baisser les "
         "salaires réduit les débouchés et peut aggraver la crise, comme "
         "Keynes le soutient.",
    'r': "Le raisonnement refuse de trancher en général et fournit un critère "
         "de diagnostic, ce qui permet de montrer que les deux thèses sont "
         "vraies dans des configurations différentes.",
    'ex': "Le cours rappelle que la baisse des salaires peut aggraver la "
          "crise en réduisant la demande."},
   {'q': "Une relance est-elle toujours efficace ?",
    'f': "Non, et la réponse est symétrique de la précédente. La relance "
         "accroît la production et l’emploi lorsque la demande de biens est "
         "le côté court du marché ; elle alimente les prix lorsque c’est "
         "l’offre qui l’est. Friedman ajoute qu’à long terme la courbe de "
         "Phillips est verticale, de sorte qu’aucune relance ne réduit "
         "durablement le chômage en dessous de son taux naturel.",
    'r': "On fait dépendre l’efficacité d’une politique de la configuration "
         "du marché, ce qui remplace une opposition doctrinale par une "
         "condition vérifiable.",
    'ex': "La stagflation des années 1970 fournit le cas où la relance "
          "n’obtient que de l’inflation."},
   {'q': "Les marchés corrigent-ils spontanément le chômage ?",
    'f': "La théorie du déséquilibre répond que non : les prix et les "
         "salaires sont rigides, l’ajustement se fait par les quantités, le "
         "rationnement est possible et le déséquilibre peut être durable. Il "
         "peut donc exister une situation stable comportant du chômage "
         "involontaire, sans incitation individuelle à changer de "
         "comportement, de sorte que l’État n’est pas une perturbation mais "
         "une condition du retour à l’activité.",
    'r': "Le raisonnement montre que l’absence d’autocorrection découle de la "
         "rigidité des prix et du rationnement, et non d’un comportement "
         "irrationnel des agents.",
    'ex': "Clower montre qu’un travailleur rationné transmet sa contrainte au "
          "marché des biens."}],
  voisins=['n10-chomage-conj-struct', 'n10-marche-travail',
           'n10-salaire-minimum', 'n10-travail-emploi'],
  comp={'titre': "Chômage keynésien et chômage classique chez Malinvaud",
        'a': "Chômage keynésien",
        'b': "Chômage classique",
        'lignes': [
          ("Côté court du marché", "La demande de biens : les entreprises ne "
           "trouvent pas de débouchés", "L’offre : les entreprises ne "
           "trouvent pas de rentabilité suffisante"),
          ("Cause immédiate", "Insuffisance de la demande effective anticipée "
           "par les entrepreneurs", "Rentabilité insuffisante de la "
           "production aux conditions existantes"),
          ("Nature du chômage", "Involontaire : les travailleurs acceptent le "
           "salaire en vigueur", "Lié aux conditions de l’offre et au "
           "partage de la valeur ajoutée"),
          ("Effet d’une relance de la demande", "Augmente la production et "
           "l’emploi, le multiplicateur jouant", "Alimente les prix sans "
           "augmenter durablement l’emploi"),
          ("Effet d’une baisse des salaires", "Réduit la demande et peut "
           "aggraver la crise", "Restaure le taux de marge et peut relancer "
           "l’offre"),
          ("Rôle attribué à l’État", "Soutenir la demande, l’État étant une "
           "condition du retour à l’activité", "Améliorer les conditions de "
           "l’offre et libéraliser l’économie"),
          ("Référence théorique", "Keynes en 1936, prolongé par la théorie du "
           "déséquilibre", "L’analyse libérale de l’offre et la critique "
           "monétariste"),
          ("Situation historique typique", "La Grande Dépression et le "
           "chômage de masse des années 1930", "La stagflation des années "
           "1970 après les chocs pétroliers"),
          ("Diagnostic requis", "Vérifier que les capacités de production "
           "sont sous-utilisées", "Vérifier que la contrainte porte sur la "
           "rentabilité et non sur les débouchés")]})


d('n10-salaire-minimum', 10, "Salaire minimum",
  "Un prix plancher sur le marché du travail : protection ou exclusion ?",
  "Le salaire minimum interprofessionnel de croissance est le revenu primaire "
  "le plus connu : une entreprise ne doit pas payer moins, sous peine de "
  "poursuites devant les prud’hommes. Le cours l’analyse comme un prix "
  "plancher, c’est-à-dire un prix minimum qui s’impose au marché, le marché du "
  "travail étant avec le marché des biens et services l’un de ses deux "
  "exemples typiques.",
  "Le cours traite le salaire minimum à la croisée de trois analyses, ce qui "
  "en fait un sujet de dissertation particulièrement bien armé. Analyse "
  "microéconomique d’abord : un prix plancher est un prix minimum fixé par "
  "l’État au-dessous duquel il est interdit de vendre, et le salaire minimum "
  "en est l’exemple typique sur le marché du travail. Le cours distingue deux "
  "cas. Si le prix plancher est inférieur au prix d’équilibre, il ne change "
  "rien et le marché fonctionne normalement. S’il est supérieur, le prix est "
  "artificiellement trop élevé, le marché est déséquilibré, et le cours "
  "énumère les effets : surproduction, perte sèche, distorsion des surplus, le "
  "surplus du producteur augmentant au détriment de celui du consommateur et "
  "le surplus total diminuant, enfin une incitation à l’illégalité, travail au "
  "noir et paiement en dessous du salaire minimum. Mais le cours apporte "
  "aussitôt une nuance majeure : l’Institut des politiques publiques, en "
  "analysant la politique agricole commune, constate que le prix plancher peut "
  "avoir un effet pervers mais être efficace en situation de monopsone, où "
  "c’est l’acheteur qui devient price maker. Analyse en termes de coût du "
  "travail ensuite : le cours rappelle que le salaire brut diffère du salaire "
  "super brut, coût total pour l’employeur, par les cotisations patronales, et "
  "que la France multiplie depuis les années 1990 les allègements de "
  "cotisations patronales sur les bas salaires afin de maintenir le salaire "
  "net tout en réduisant le coût employeur. Mais si ces allègements sont "
  "concentrés autour du salaire minimum, une hausse de salaire fait "
  "disparaître progressivement les exonérations et élève le coût marginal pour "
  "l’entreprise, ce qui peut créer une trappe à bas salaires et un effet "
  "d’aubaine. Analyse comparative enfin : l’Allemagne, après une longue "
  "modération salariale ayant favorisé les emplois faiblement rémunérés, "
  "introduit un salaire minimum légal généralisé le premier janvier 2015.",
  [("Le plancher légal du prix du travail",
    "Un prix minimum s’impose au marché : l’entreprise ne peut pas payer "
    "moins, sous peine de poursuites, ce qui retire au salaire sa liberté "
    "d’ajustement vers le bas."),
   ("L’effet nul d’un plancher inférieur à l’équilibre",
    "Si le salaire minimum est inférieur au salaire d’équilibre, il ne change "
    "rien et le marché fonctionne normalement : son effet dépend donc "
    "entièrement de son niveau relatif et non de son existence."),
   ("Le déséquilibre créé par un plancher contraignant",
    "Si le plancher dépasse le prix d’équilibre, l’offre excède la demande : "
    "apparaissent un excédent d’offre de travail, une perte sèche et une "
    "distorsion des surplus au détriment du surplus total."),
   ("Le cas du monopsone",
    "Lorsqu’un seul acheteur fait face à de nombreux vendeurs, c’est "
    "l’acheteur qui devient price maker : un prix plancher peut alors "
    "corriger son pouvoir de marché et être efficace plutôt que "
    "destructeur."),
   ("La dissociation du salaire net et du coût employeur",
    "Les allègements de cotisations patronales permettent de maintenir le "
    "salaire net tout en réduisant le coût employeur : le coût du travail "
    "peut donc baisser sans que le salaire minimum soit abaissé."),
   ("La trappe à bas salaires",
    "Si les allègements sont concentrés autour du salaire minimum, toute "
    "augmentation de salaire fait disparaître les exonérations et élève le "
    "coût marginal pour l’entreprise, qui a donc intérêt à maintenir les "
    "rémunérations basses.")],
  [{'a': "L’analyse en termes de prix plancher fournit un raisonnement clair "
         "sur les effets d’un salaire minimum contraignant.",
    'cond': "Elle suppose un marché du travail concurrentiel où le salaire "
            "équilibre librement offre et demande.",
    'lim': "Le cours relève que ce résultat s’inverse en situation de "
           "monopsone, où c’est l’acheteur qui devient price maker et où un "
           "prix plancher peut être efficace."},
   {'a': "Le salaire minimum garantit un revenu primaire plancher et évite "
         "que la concurrence entre travailleurs ne tire les salaires vers le "
         "bas.",
    'cond': "La garantie suppose que la règle soit effectivement appliquée et "
            "contrôlée, ce que rappellent les recours aux prud’hommes.",
    'lim': "Le cours relève qu’un plancher contraignant crée une incitation "
           "à l’illégalité, travail au noir et paiement en dessous du salaire "
           "minimum, qui prive les travailleurs de la protection visée."},
   {'a': "Les allègements de cotisations permettent de réduire le coût du "
         "travail sans toucher au salaire net, ce qui concilie compétitivité "
         "et pouvoir d’achat.",
    'cond': "L’efficacité suppose que l’emploi soit effectivement sensible au "
            "coût du travail dans la zone des bas salaires.",
    'lim': "Concentrés autour du salaire minimum, ces allègements produisent "
           "un effet d’aubaine et une trappe à bas salaires, et peuvent "
           "enfermer les entreprises dans une stratégie de compétitivité-coût "
           "plutôt que de montée en gamme."},
   {'a': "L’expérience allemande montre que l’absence de salaire minimum a un "
         "coût social identifiable.",
    'cond': "La comparaison suppose que l’on rapporte le développement des "
            "emplois faiblement rémunérés à la modération salariale "
            "antérieure.",
    'lim': "Le cours rappelle que le redressement allemand ne peut pas être "
           "expliqué uniquement par ces réformes, mais dépend aussi de la "
           "spécialisation industrielle et de l’intégration productive avec "
           "l’Europe centrale."}],
  [{'t': "Un prix plancher supérieur au prix d’équilibre déséquilibre le "
         "marché, crée une perte sèche et rend l’allocation sous-optimale.",
    'qui': "Le raisonnement microéconomique sur les prix plancher que le "
           "cours expose.",
    'rep': "Le cours relève que l’Institut des politiques publiques, en "
           "analysant la politique agricole commune, montre qu’un prix "
           "plancher peut avoir un effet pervers mais être efficace en "
           "situation de monopsone."},
   {'t': "Il faut réduire le coût du travail pour favoriser l’emploi, ce que "
         "les allègements de cotisations sur les bas salaires permettent sans "
         "baisser les salaires nets.",
    'qui': "La stratégie française de compétitivité-coût depuis le début des "
           "années 1990.",
    'rep': "Le cours objecte que des allègements excessivement concentrés sur "
           "les bas salaires produisent un effet d’aubaine et une trappe à "
           "bas salaires, et peuvent dissuader les entreprises d’investir "
           "pour monter en gamme."},
   {'t': "La baisse des salaires permet de résorber le chômage en rétablissant "
         "l’équilibre du marché du travail.",
    'qui': "L’analyse néoclassique du marché du travail.",
    'rep': "Keynes répond que la baisse des salaires ne supprime pas le "
           "chômage et peut aggraver la crise en réduisant la demande, et le "
           "cours rappelle que le salaire minimum figure parmi les rigidités "
           "qui empêchent l’ajustement."}],
  [{'n': "John Maynard Keynes",
    'i': "La baisse des salaires ne supprime pas le chômage et peut même "
         "aggraver la crise en réduisant la demande.",
    'p': "Le cours range le salaire minimum parmi les éléments qui fixent le "
         "salaire à un niveau donné, avec les conventions, les rigidités et "
         "la négociation collective, et montre qu’à ce salaire l’offre de "
         "travail dépasse la demande, faisant apparaître un chômage "
         "involontaire."},
   {'n': "Milton Friedman",
    'i': "Il existe un taux de chômage naturel lié aux frictions du marché du "
         "travail que la politique économique ne peut pas réduire.",
    'p': "Le cours en tire la position libérale sur les rigidités : pour "
         "relancer l’économie, il faut agir sur l’offre, restaurer le taux de "
         "marge des entreprises et libéraliser les économies, ce qui inclut "
         "la critique des contraintes pesant sur le prix du travail."},
   {'n': "John D. Rockefeller",
    'i': "Un acheteur en position dominante peut imposer ses prix à ses "
         "fournisseurs.",
    'p': "Le cours mobilise son histoire pour illustrer le monopsone, "
         "situation dans laquelle c’est l’acheteur qui devient price maker : "
         "c’est précisément le cas où un prix plancher peut être efficace "
         "plutôt que destructeur."}],
  [{'f': "Le cours rappelle que le salaire brut diffère du salaire super "
         "brut, coût total pour l’employeur, par les cotisations patronales, "
         "et que plus les salaires sont bas, plus les cotisations sont "
         "faibles.",
    'p': "Le mécanisme montre que le coût du travail au niveau du salaire "
         "minimum dépend autant du barème des cotisations que du salaire "
         "lui-même."},
   {'f': "L’Allemagne introduit un salaire minimum légal généralisé le "
         "premier janvier 2015, après une modération salariale ayant "
         "contribué au développement d’emplois faiblement rémunérés, et son "
         "coût salarial unitaire progresse ensuite davantage.",
    'p': "Le cas montre qu’un salaire minimum modifie effectivement la "
         "dynamique des coûts, et qu’un pays peut juger le coût social de son "
         "absence supérieur à son avantage compétitif."},
   {'f': "Le cours relève que les allègements de cotisations concentrés "
         "autour du salaire minimum créent un risque de trappe à bas "
         "salaires, puisqu’une augmentation de salaire fait disparaître "
         "progressivement les exonérations.",
    'p': "Le mécanisme démontre qu’un dispositif destiné à soutenir l’emploi "
         "peut freiner la progression salariale qu’il devrait accompagner."}],
  [{'q': "Le salaire minimum protège-t-il ou exclut-il ?",
    'f': "L’analyse en termes de prix plancher conclut à l’exclusion si le "
         "plancher dépasse le salaire d’équilibre : excédent d’offre de "
         "travail, perte sèche, distorsion des surplus et incitation au "
         "travail au noir. Mais le cours ajoute que le résultat s’inverse en "
         "situation de monopsone, où c’est l’acheteur qui devient price "
         "maker, et qu’un plancher inférieur à l’équilibre ne change rien.",
    'r': "Le raisonnement fait dépendre la réponse de deux paramètres, le "
         "niveau relatif du plancher et la structure du marché, ce qui "
         "interdit une conclusion générale.",
    'ex': "L’Institut des politiques publiques montre, à propos de la "
          "politique agricole commune, qu’un prix plancher peut être efficace "
          "en situation de monopsone."},
   {'q': "Faut-il baisser le coût du travail au niveau du salaire minimum ?",
    'f': "La France a choisi une voie intermédiaire : alléger les cotisations "
         "patronales sur les bas salaires plutôt que baisser les salaires "
         "nets, afin de réduire le coût employeur sans réduire le pouvoir "
         "d’achat. Mais le cours montre que la concentration de ces "
         "allègements produit un effet d’aubaine et une trappe à bas "
         "salaires, et peut dissuader la montée en gamme.",
    'r': "On montre qu’un instrument ciblé résout le problème immédiat tout "
         "en créant une incitation perverse à son propre maintien, ce qui "
         "explique la difficulté de sortir du dispositif.",
    'ex': "Une augmentation de salaire fait disparaître progressivement les "
          "exonérations et élève le coût marginal pour l’entreprise."},
   {'q': "L’absence de salaire minimum est-elle un avantage compétitif ?",
    'f': "L’Allemagne a longtemps pratiqué la modération salariale, ce qui a "
         "contribué à son avantage-coût mais aussi au développement d’emplois "
         "faiblement rémunérés ; elle a introduit un salaire minimum légal "
         "généralisé en 2015, et son coût salarial unitaire a ensuite "
         "progressé davantage. L’avantage-coût n’est donc ni gratuit ni "
         "permanent.",
    'r': "Le raisonnement met en regard le gain de compétitivité et son coût "
         "social, puis utilise le revirement allemand comme révélateur de "
         "l’arbitrage effectivement retenu.",
    'ex': "Le cours relève qu’entre 2010 et 2025 le coût unitaire du travail "
          "allemand augmente davantage que celui de la zone euro."}],
  voisins=['n10-marche-travail', 'n10-chomage-classique-keynesien',
           'n5-equilibre', 'n10-precarite'])
