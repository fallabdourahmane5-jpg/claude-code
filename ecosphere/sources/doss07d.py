# -*- coding: utf-8 -*-
"""Ensemble 7 — La consommation, l’épargne et les comportements économiques
(4/4)."""

from doss_base import d

d('n7-revenu-disponible', 7, "Revenu disponible",
  "Ce qui reste effectivement à arbitrer entre consommation et épargne",
  "Le revenu disponible brut des ménages est égal à la somme des revenus "
  "primaires et des revenus secondaires, diminuée des prélèvements "
  "obligatoires. Il constitue la grandeur à partir de laquelle les ménages "
  "arbitrent entre consommation et épargne, et c’est donc lui, et non le "
  "revenu primaire, qui intervient dans les fonctions de consommation.",
  "Le revenu disponible est la notion comptable qui rend opératoires toutes "
  "les théories de la consommation, et sa construction doit être restituée "
  "avec précision. Le cours distingue d’abord les types de revenus. Les "
  "revenus primaires sont liés à l’activité productive : revenus salariaux, "
  "qui rémunèrent le travail salarié et non indépendant ; revenus de la "
  "propriété, c’est-à-dire loyers, rentes et dividendes ; revenus mixtes, qui "
  "rémunèrent à la fois le travail et le capital. Le revenu primaire le plus "
  "connu est celui qu’encadre le salaire minimum interprofessionnel de "
  "croissance. Les revenus secondaires, ou revenus de transfert, sont "
  "distribués par l’État : ils correspondent à des transferts sans "
  "contrepartie productive directe. La formule qui en résulte est simple : "
  "revenu disponible brut égale revenus primaires plus revenus secondaires "
  "moins prélèvements obligatoires. Cette construction a deux portées. La "
  "première est analytique : c’est le revenu disponible qui est pertinent pour "
  "l’analyse de la consommation, puisque c’est lui qui est effectivement "
  "arbitrable ; la propension à consommer se calcule par rapport à lui. La "
  "seconde est distributive : l’écart entre revenu primaire et revenu "
  "disponible mesure l’effet de la redistribution. Le cours signale d’ailleurs "
  "l’existence d’une mesure élargie intégrant la redistribution en nature — "
  "santé gratuite, éducation publique, allocations et prestations sociales — "
  "qui permet de mesurer plus précisément le niveau de vie réel et de mieux "
  "évaluer l’impact de la redistribution opérée par les administrations "
  "publiques. Enfin, le revenu disponible permet de définir le taux "
  "d’épargne, et le cours en donne un ordre de grandeur frappant pour la "
  "Chine, où le taux d’épargne des ménages dépasse 40 % du revenu disponible.",
  [("L’addition des revenus primaires",
    "Les revenus liés à l’activité productive — salaires, revenus de la "
    "propriété, revenus mixtes — forment la première composante : ils "
    "rémunèrent une contribution à la production."),
   ("L’ajout des transferts",
    "Les revenus secondaires, distribués par l’État, correspondent à des "
    "transferts sans contrepartie productive directe : ils corrigent la "
    "répartition primaire en faveur de certains ménages."),
   ("La soustraction des prélèvements",
    "Impôts et cotisations viennent en déduction : ce qui reste est "
    "effectivement disponible pour l’arbitrage entre consommation et épargne, "
    "d’où le nom de la grandeur."),
   ("La mesure de la redistribution",
    "L’écart entre revenu primaire et revenu disponible mesure l’effet des "
    "transferts et des prélèvements : la redistribution se lit dans cette "
    "transformation."),
   ("L’extension à la redistribution en nature",
    "Une mesure élargie intègre la santé gratuite, l’éducation publique et les "
    "prestations sociales, afin de mesurer plus précisément le niveau de vie "
    "réel des ménages.")],
  [{'a': "Le revenu disponible est la bonne grandeur pour analyser la "
         "consommation, puisque c’est lui qui est effectivement arbitrable.",
    'cond': "L’argument suppose que les ménages ne puissent ni emprunter ni "
            "désépargner, hypothèse du cadre statique.",
    'lim': "Les théories du revenu permanent et du cycle de vie montrent "
           "précisément que les ménages lissent leur consommation au-delà du "
           "revenu de la période."},
   {'a': "Il permet de mesurer l’effet de la redistribution, par comparaison "
         "avec le revenu primaire.",
    'cond': "La mesure suppose de recenser l’ensemble des transferts et des "
            "prélèvements, y compris indirects.",
    'lim': "Elle ignore la redistribution en nature, ce que le cours corrige "
           "par une mesure élargie intégrant santé, éducation et prestations."},
   {'a': "Il fournit le dénominateur des taux d’épargne et de consommation, "
         "indispensables aux comparaisons internationales.",
    'cond': "La comparaison internationale suppose des conventions comptables "
            "suffisamment homogènes entre pays.",
    'lim': "Les systèmes de protection sociale différant fortement, un même "
           "taux d’épargne peut recouvrir des situations très distinctes."},
   {'a': "Il relie les agrégats de la comptabilité nationale aux "
         "comportements microéconomiques des ménages.",
    'cond': "Le lien suppose que la moyenne agrégée soit représentative, ce "
            "qui n’est pas garanti en cas de forte dispersion des revenus.",
    'lim': "Une même moyenne peut recouvrir des comportements opposés selon "
           "les déciles, les propensions à consommer variant avec le niveau de "
           "revenu."}],
  [{'t': "La consommation dépend du revenu courant disponible, ce qui justifie "
         "l’intervention de l’État.",
    'qui': "John Maynard Keynes, dont la loi psychologique fondamentale fonde "
           "la fonction de consommation.",
    'rep': "Friedman conteste précisément ce point, en observant que la "
           "consommation est beaucoup plus stable que le revenu, ce qui suggère "
           "qu’elle dépend d’un revenu anticipé plutôt que perçu."},
   {'t': "Le revenu disponible purement monétaire sous-estime sensiblement "
         "le niveau de vie réel des ménages.",
    'qui': "La mesure élargie que le cours mentionne, intégrant la "
           "redistribution en nature.",
    'rep': "L’objection est fondée : santé gratuite, éducation publique, "
           "allocations et prestations sociales élèvent le niveau de vie réel "
           "sans apparaître dans le revenu monétaire."},
   {'t': "Un taux d’épargne élevé traduit moins une préférence pour l’avenir "
         "qu’une faiblesse de la protection sociale.",
    'qui': "L’analyse de l’épargne chinoise que le cours développe.",
    'rep': "Le mécanisme est explicite : une protection sociale faible accroît "
           "l’incertitude, donc l’épargne de précaution, ce qui montre que le "
           "taux d’épargne dépend des institutions autant des préférences."},
   {'t': "Le revenu disponible agrégé ne dit rien de la manière dont il se "
         "répartit entre les différents ménages.",
    'qui': "La limite des indicateurs moyens que le cours relève à plusieurs "
           "reprises.",
    'rep': "L’objection vaut pour tout agrégat : une même moyenne peut "
           "recouvrir des situations très contrastées, ce qui impose de "
           "compléter par des indicateurs de dispersion."}],
  [{'n': "John Maynard Keynes",
    'i': "La consommation dépend du revenu courant et augmente avec lui à un "
         "rythme plus faible.",
    'p': "Sa loi psychologique fondamentale fait du revenu disponible la "
         "variable explicative de la consommation. Il en tire la propension "
         "moyenne à consommer, rapport de la consommation au revenu, et la "
         "propension marginale, part du revenu supplémentaire consacrée à la "
         "consommation."},
   {'n': "Milton Friedman",
    'i': "Le revenu courant se décompose en un revenu permanent et un revenu "
         "transitoire.",
    'p': "Le revenu permanent correspond à la partie stable, anticipée et "
         "durable, déterminée par la qualification, l’expérience, la richesse "
         "et les perspectives d’emploi ; le revenu transitoire représente la "
         "variation temporaire et aléatoire, comme une prime exceptionnelle."},
   {'n': "Franco Modigliani",
    'i': "La consommation dépend aussi de la richesse patrimoniale et de "
         "l’âge, et pas seulement du revenu.",
    'p': "Son modèle du cycle de vie complète la lecture comptable : à revenu "
         "disponible identique, deux ménages n’auront pas le même comportement "
         "selon leur patrimoine accumulé et leur position dans le cycle de "
         "vie."}],
  [{'f': "Le revenu disponible brut est égal au revenu primaire augmenté du "
         "revenu secondaire et diminué des prélèvements obligatoires.",
    'p': "La formule est la définition comptable exacte et doit être restituée "
         "telle quelle pour toute analyse des comportements des ménages."},
   {'f': "Les revenus primaires comprennent les revenus salariaux, qui "
         "rémunèrent le travail salarié et non indépendant, les revenus de la "
         "propriété — loyers, rentes, dividendes — et les revenus mixtes, qui "
         "rémunèrent travail et capital.",
    'p': "La typologie permet de situer chaque flux et d’analyser le partage "
         "de la valeur ajoutée entre travail et capital."},
   {'f': "Les revenus secondaires sont des transferts distribués par l’État, "
         "sans contrepartie productive directe.",
    'p': "La définition relie le revenu disponible à l’analyse de la "
         "redistribution et au rôle des administrations publiques."},
   {'f': "Le taux d’épargne des ménages chinois dépasse 40 % du revenu "
         "disponible.",
    'p': "Le chiffre fournit un ordre de grandeur exceptionnel et montre que "
         "le partage entre consommation et épargne dépend fortement du "
         "contexte institutionnel."}],
  [{'q': "Sujet du type « Comment se forme le revenu des ménages ? »",
    'f': "La comptabilité nationale procède en trois temps. Les revenus "
         "primaires rémunèrent la participation à l’activité productive : "
         "revenus salariaux, revenus de la propriété sous forme de loyers, "
         "rentes et dividendes, et revenus mixtes qui rémunèrent à la fois "
         "travail et capital. S’y ajoutent les revenus secondaires, transferts "
         "distribués par l’État sans contrepartie productive directe. En sont "
         "retranchés les prélèvements obligatoires, ce qui donne le revenu "
         "disponible brut.",
    'r': "Le raisonnement distingue la répartition primaire, issue de la "
         "production, de la répartition secondaire, issue de la "
         "redistribution, ce qui permet d’évaluer séparément le marché et "
         "l’État.",
    'ex': "Le salaire minimum interprofessionnel de croissance, que le cours "
          "donne comme le revenu primaire le plus connu."},
   {'q': "Sujet du type « Le revenu mesure-t-il le niveau de vie ? »",
    'f': "Pas entièrement, et le cours en donne la raison. Une mesure élargie "
         "intègre la redistribution en nature — santé gratuite, éducation "
         "publique, allocations et prestations sociales — ce qui permet de "
         "mesurer plus précisément le niveau de vie réel et de mieux évaluer "
         "l’impact de la redistribution opérée par les administrations "
         "publiques. Le revenu disponible monétaire sous-estime donc le niveau "
         "de vie effectif des ménages bénéficiaires de services publics.",
    'r': "Le raisonnement montre que le périmètre de mesure détermine la "
         "conclusion sur l’efficacité de la redistribution, ce qui est "
         "essentiel pour les comparaisons internationales.",
    'ex': "La prise en compte des services non marchands fournis par les "
          "administrations publiques dans l’évaluation du niveau de vie."}],
  voisins=['n7-propension', 'n7-revenu-permanent', 'n7-cycle-vie',
           'n7-consommation'])


d('n7-propension', 7, "Propension à consommer",
  "La part du revenu consommée, et le multiplicateur qui en découle",
  "La propension moyenne à consommer est le rapport entre la consommation "
  "totale et le revenu ; la propension marginale à consommer est la part du "
  "revenu supplémentaire consacrée à la consommation, comprise entre 0 et 1. "
  "Keynes soutient que la première est décroissante, ce qui fonde la loi "
  "psychologique fondamentale selon laquelle la consommation augmente avec le "
  "revenu mais à un rythme plus faible.",
  "Les propensions sont l’outil par lequel une hypothèse psychologique devient "
  "un résultat macroéconomique, et il faut en suivre toute la chaîne. Le point "
  "de départ est la loi psychologique fondamentale, énoncée par Keynes dans la "
  "Théorie générale de l’emploi, de l’intérêt et de la monnaie (1936) : la "
  "consommation augmente avec le revenu mais à un rythme plus faible. Deux "
  "grandeurs en découlent. La propension moyenne, rapport entre la "
  "consommation totale et le revenu, est décroissante selon Keynes : plus le "
  "revenu augmente, plus la part consacrée à la consommation diminue, "
  "puisqu’on épargne davantage. La propension marginale, rapport entre la "
  "variation de consommation et la variation de revenu, est comprise entre 0 "
  "et 1 : si le revenu augmente de 100, on n’en consomme pas 100 mais une "
  "partie, par exemple 70, le reste allant à l’épargne. La conséquence "
  "macroéconomique est le multiplicateur : le cours mène le calcul, en partant "
  "d’une variation de revenu égale à la propension marginale multipliée par "
  "cette variation, plus la variation d’investissement, pour aboutir à un "
  "coefficient égal à l’inverse de un moins la propension marginale. Avec une "
  "propension de 0,8, le multiplicateur vaut 5 en économie fermée, et 2,5 en "
  "économie ouverte — l’ouverture réduisant l’effet puisqu’une partie de la "
  "demande fuit vers les importations. Le cours ajoute l’oscillateur de "
  "Samuelson (1939) : une variation d’investissement entraîne une variation de "
  "revenu, qui entraîne une variation de demande. Deux limites sont enfin "
  "signalées. La vérification empirique d’abord : après 1945, les études ont "
  "montré que la part consommée du revenu reste assez stable à long terme. "
  "L’enjeu politique ensuite : c’est la baisse de la propension moyenne qui "
  "justifiait l’intervention de l’État, et c’est pourquoi Friedman la "
  "conteste.",
  [("La loi psychologique fondamentale",
    "La consommation augmente avec le revenu mais à un rythme plus faible : "
    "une partie du revenu supplémentaire est épargnée, ce qui crée un écart "
    "croissant entre revenu et consommation."),
   ("La distinction entre moyenne et marginale",
    "La propension moyenne rapporte la consommation totale au revenu total ; "
    "la propension marginale rapporte la variation de consommation à la "
    "variation de revenu : seule la seconde entre dans le multiplicateur."),
   ("L’enchaînement multiplicateur",
    "Une dépense supplémentaire devient le revenu d’un autre agent, qui en "
    "consomme une fraction, laquelle devient à son tour un revenu : la somme "
    "de ces vagues est égale à la dépense initiale multipliée par l’inverse de "
    "un moins la propension marginale."),
   ("L’atténuation par l’ouverture",
    "Une partie de la demande supplémentaire se porte sur des produits "
    "importés et quitte le circuit national : le multiplicateur passe ainsi de "
    "5 en économie fermée à 2,5 en économie ouverte pour une propension de "
    "0,8."),
   ("L’interaction avec l’investissement",
    "L’oscillateur de Samuelson relie les deux variables : une variation "
    "d’investissement entraîne une variation de revenu, qui entraîne une "
    "variation de demande, et donc de nouveaux investissements.")],
  [{'a': "Les propensions transforment une régularité de comportement en "
         "résultat macroéconomique quantifié, le multiplicateur.",
    'cond': "Le calcul suppose une propension marginale stable sur la période "
            "et une économie en sous-emploi, où l’offre suit la demande.",
    'lim': "En situation de plein emploi des capacités, la dépense "
           "supplémentaire se traduit en hausse des prix plutôt qu’en hausse "
           "de la production."},
   {'a': "Elles justifient une politique de relance, puisqu’une dépense "
         "initiale produit un effet supérieur à son montant.",
    'cond': "L’effet suppose que la propension marginale soit élevée, donc que "
            "la dépense soit orientée vers des ménages qui consomment.",
    'lim': "Le cours montre que l’ouverture réduit fortement l’effet, le "
           "multiplicateur tombant de 5 à 2,5 pour une même propension."},
   {'a': "Elles fournissent une explication de l’insuffisance de la demande "
         "globale, et donc du chômage involontaire.",
    'cond': "L’explication suppose la décroissance de la propension moyenne "
            "avec le revenu, qui creuse l’écart entre revenu et consommation.",
    'lim': "Les vérifications empiriques postérieures à 1945 ont montré que la "
           "part consommée du revenu reste assez stable à long terme."},
   {'a': "Elles relient directement la théorie de la consommation à la "
         "politique économique, ce qui en fait un outil opératoire.",
    'cond': "Le lien suppose que l’État puisse agir sur le revenu disponible "
            "des ménages par la dépense ou les transferts.",
    'lim': "Friedman conteste précisément cette justification en montrant que "
           "les ménages fondent leur consommation sur le revenu permanent et "
           "non sur le revenu courant."}],
  [{'t': "La propension moyenne à consommer n’est pas décroissante : la part "
         "consommée reste assez stable à long terme.",
    'qui': "Les vérifications empiriques postérieures à 1945 que le cours "
           "rapporte.",
    'rep': "L’objection est empirique et décisive : elle a conduit au "
           "développement des théories du revenu permanent et du cycle de vie, "
           "qui expliquent cette stabilité."},
   {'t': "Les ménages ne consomment pas en fonction du revenu courant mais du "
         "revenu permanent.",
    'qui': "Milton Friedman, avec la théorie du revenu permanent.",
    'rep': "Le cours précise son intention : critiquer la thèse keynésienne du "
           "revenu courant afin de remettre en cause la justification de "
           "l’intervention publique fondée sur la baisse de la propension "
           "moyenne."},
   {'t': "La loi d’Engel explique la stabilité de la part consommée, les "
         "ménages riches compensant par d’autres postes de dépense.",
    'qui': "Ernst Engel, dont le cours rappelle la loi à ce propos.",
    'rep': "L’argument est juste : les ménages riches dépensent "
           "proportionnellement moins dans certains biens, comme "
           "l’alimentation, mais compensent par d’autres postes, ce qui "
           "stabilise la part globale."},
   {'t': "Le multiplicateur est fortement atténué dans une économie ouverte "
         "sur l’extérieur, donc peu efficace.",
    'qui': "Le calcul que le cours mène explicitement.",
    'rep': "L’objection est chiffrée : pour une propension marginale de 0,8, "
           "le multiplicateur vaut 5 en économie fermée mais seulement 2,5 en "
           "économie ouverte."}],
  [{'n': "John Maynard Keynes",
    'i': "La consommation augmente avec le revenu mais à un rythme plus "
         "faible.",
    'p': "Le cours rattache cette loi psychologique fondamentale à la Théorie "
         "générale (1936) et en tire deux grandeurs : la propension moyenne, "
         "qu’il juge décroissante, et la propension marginale, comprise entre "
         "0 et 1."},
   {'n': "Paul Samuelson",
    'i': "Une variation d’investissement entraîne une variation de revenu, qui "
         "entraîne une variation de demande.",
    'p': "Le cours date son oscillateur de 1939 et en tire une conclusion sur "
         "le statut de l’investissement : il est à la fois un élément de la "
         "demande et un élément de l’offre, ce qui en fait une variable clé de "
         "la dynamique économique."},
   {'n': "Milton Friedman",
    'i': "La consommation dépend du revenu permanent et non du revenu courant.",
    'p': "Sa critique vise directement l’usage politique des propensions : "
         "dans la théorie keynésienne, la baisse de la propension moyenne à "
         "consommer avec la croissance du revenu justifie l’intervention de "
         "l’État pour conserver l’équilibre économique."},
   {'n': "Ernst Engel",
    'i': "Quand le revenu augmente, la structure de la consommation change.",
    'p': "Le cours mobilise sa loi pour expliquer la stabilité empirique de la "
         "part consommée : les ménages riches dépensent proportionnellement "
         "moins dans certains biens mais compensent par d’autres postes de "
         "dépense."}],
  [{'f': "La propension moyenne à consommer est le rapport entre la "
         "consommation totale et le revenu ; la propension marginale est la "
         "part du revenu supplémentaire consacrée à la consommation, comprise "
         "entre 0 et 1.",
    'p': "Les deux définitions doivent être restituées ensemble, car seule la "
         "propension marginale intervient dans le calcul du multiplicateur."},
   {'f': "Le cours illustre la propension marginale ainsi : si le revenu "
         "augmente de 100, on n’en consomme pas 100 mais une partie, par "
         "exemple 70, le reste allant à l’épargne.",
    'p': "L’exemple numérique rend immédiatement intelligible la différence "
         "entre consommer la totalité et consommer une fraction du supplément."},
   {'f': "Avec une propension marginale de 0,8, le multiplicateur vaut 5 en "
         "économie fermée et 2,5 en économie ouverte.",
    'p': "Les deux valeurs montrent que l’ouverture divise l’effet par deux, "
         "ce qui est un argument central contre les relances isolées."},
   {'f': "Après 1945, les études ont montré que la part consommée du revenu "
         "reste assez stable à long terme, ce que le cours relie à la loi "
         "d’Engel.",
    'p': "Le fait constitue l’objection empirique décisive à la thèse "
         "keynésienne et ouvre la voie aux théories du revenu permanent et du "
         "cycle de vie."}],
  [{'q': "Sujet du type « Une relance budgétaire est-elle efficace ? »",
    'f': "Son efficacité dépend de la propension marginale à consommer. Le "
         "multiplicateur est égal à l’inverse de un moins cette propension : "
         "avec une propension de 0,8, il vaut 5 en économie fermée, de sorte "
         "qu’une dépense initiale produit un effet cinq fois supérieur. Mais "
         "en économie ouverte il ne vaut plus que 2,5, car une partie de la "
         "demande supplémentaire se porte sur des produits importés et quitte "
         "le circuit national.",
    'r': "Le raisonnement quantifie l’effet au lieu de l’affirmer, et montre "
         "que la contrainte extérieure réduit de moitié la portée de "
         "l’instrument.",
    'ex': "L’oscillateur de Samuelson (1939), selon lequel une variation "
          "d’investissement entraîne une variation de revenu, puis de "
          "demande."},
   {'q': "Sujet du type « L’État doit-il soutenir la demande ? »",
    'f': "La réponse keynésienne repose sur la décroissance de la propension "
         "moyenne à consommer : puisque la part du revenu consacrée à la "
         "consommation diminue quand le revenu augmente, la demande risque de "
         "devenir insuffisante, ce qui justifie l’intervention de l’État pour "
         "conserver l’équilibre économique. C’est précisément cette "
         "justification que Friedman entend détruire en montrant que la "
         "consommation dépend du revenu permanent, beaucoup plus stable que le "
         "revenu courant.",
    'r': "Le raisonnement montre que le débat théorique sur la fonction de "
         "consommation a un enjeu directement politique, ce qui explique son "
         "intensité.",
    'ex': "La stabilité observée après 1945 de la part consommée du revenu, "
          "contraire à la prévision keynésienne."}],
  voisins=['n7-consommation', 'n7-revenu-permanent', 'n7-revenu-disponible',
           'n7-cycle-vie'])


d('n7-revenu-permanent', 7, "Revenu permanent",
  "Consommer selon ce qu’on pense gagner durablement, non selon le mois",
  "La théorie du revenu permanent, formulée par Milton Friedman, soutient que "
  "les individus fondent leurs décisions de consommation non sur leur revenu "
  "du moment mais sur le revenu qu’ils s’attendent à percevoir durablement "
  "tout au long de leur vie. Le revenu courant se décompose alors en un revenu "
  "permanent, stable et anticipé, et un revenu transitoire, temporaire et "
  "aléatoire.",
  "La théorie du revenu permanent est née d’une observation empirique et d’une "
  "intention politique, et il faut restituer les deux. L’observation : "
  "Friedman constate que la consommation est en réalité beaucoup plus stable "
  "que le revenu et ne varie pas autant d’une période à l’autre. Il en conclut "
  "que les individus ne fondent pas leurs décisions de consommation uniquement "
  "sur leur revenu du moment, mais plutôt sur le revenu qu’ils s’attendent à "
  "percevoir durablement tout au long de leur vie. L’intention : le cours est "
  "explicite, Friedman cherche à remettre en cause la justification "
  "keynésienne de l’intervention publique, puisque dans la théorie keynésienne "
  "c’est la baisse de la propension moyenne à consommer avec la croissance du "
  "revenu qui justifie l’intervention de l’État pour conserver l’équilibre "
  "économique en économie fermée. La décomposition proposée est précise. Le "
  "revenu permanent correspond à la partie stable, anticipée et durable du "
  "revenu, déterminée par des éléments tels que la qualification, "
  "l’expérience, la richesse et les perspectives d’emploi de la personne. Le "
  "revenu transitoire représente au contraire la variation temporaire et "
  "aléatoire du revenu, comme une prime exceptionnelle. La conséquence "
  "pratique est décisive : un supplément de revenu perçu comme transitoire est "
  "largement épargné, tandis qu’un supplément perçu comme permanent est "
  "consommé. Une relance ponctuelle, nécessairement transitoire, aurait donc "
  "un effet faible sur la consommation, ce qui ruine le multiplicateur. Le "
  "cours situe enfin cette théorie dans une opposition plus large : Keynes est "
  "un économiste interventionniste, Friedman un libéral, et tous deux "
  "cherchaient à comprendre ce qui fait la consommation ; pour les keynésiens "
  "le taux d’intérêt est le prix de la renonciation à la liquidité, pour "
  "Friedman et les classiques le prix de la renonciation à la consommation.",
  [("L’observation de la stabilité de la consommation",
    "La consommation varie beaucoup moins que le revenu d’une période à "
    "l’autre : cette régularité empirique est incompatible avec une fonction "
    "de consommation fondée sur le seul revenu courant."),
   ("La décomposition du revenu",
    "Le revenu courant se décompose en une partie permanente, stable et "
    "anticipée, déterminée par la qualification, l’expérience, la richesse et "
    "les perspectives d’emploi, et une partie transitoire, temporaire et "
    "aléatoire."),
   ("La consommation indexée sur le permanent",
    "Les ménages consomment en proportion de leur revenu permanent : le revenu "
    "transitoire, étant imprévisible et non reconductible, est principalement "
    "épargné."),
   ("Le lissage par l’épargne",
    "L’épargne sert d’amortisseur entre un revenu variable et une "
    "consommation stable : elle absorbe les hausses transitoires et "
    "compense les baisses passagères."),
   ("L’affaiblissement du multiplicateur",
    "Une relance ponctuelle est perçue comme transitoire : elle est donc "
    "largement épargnée, et son effet sur la demande est bien inférieur à "
    "celui que prédit la propension marginale keynésienne.")],
  [{'a': "La théorie explique une régularité empirique que le modèle keynésien "
         "ne prévoyait pas, la stabilité de la consommation.",
    'cond': "L’explication suppose que les ménages distinguent effectivement "
            "le permanent du transitoire dans leurs revenus.",
    'lim': "Cette distinction exige une capacité d’anticipation que les "
           "travaux sur la rationalité limitée et les biais cognitifs rendent "
           "douteuse."},
   {'a': "Elle rend compte de la différence de comportement entre une prime "
         "exceptionnelle et une hausse durable de salaire.",
    'cond': "L’argument suppose que le ménage perçoive correctement le "
            "caractère durable ou non de la variation.",
    'lim': "En pratique, la frontière est incertaine : une hausse présentée "
           "comme durable peut être révisée, et inversement."},
   {'a': "Elle fournit une critique puissante des politiques de relance "
         "ponctuelles, qui seraient largement épargnées.",
    'cond': "La critique suppose que les ménages aient effectivement la "
            "possibilité d’épargner le supplément reçu.",
    'lim': "Les ménages contraints par la liquidité consomment immédiatement "
           "tout supplément de revenu, ce qui restaure l’efficacité de la "
           "relance ciblée sur eux."},
   {'a': "Elle s’articule avec la théorie du cycle de vie pour former une "
         "approche intertemporelle cohérente de la consommation.",
    'cond': "L’articulation suppose des individus rationnels et prévoyants, "
            "hypothèse commune aux deux approches.",
    'lim': "Le cours relève précisément que Modigliani rejoint Friedman en "
           "considérant l’individu comme rationnel et prévoyant, ce qui rend "
           "les deux théories vulnérables à la même objection comportementale."}],
  [{'t': "La consommation dépend du revenu courant perçu, ce qui justifie "
         "l’intervention stabilisatrice de l’État.",
    'qui': "John Maynard Keynes, dont Friedman conteste explicitement la "
           "thèse.",
    'rep': "Le cours souligne que la critique est dirigée contre l’usage "
           "politique de la théorie : c’est la baisse de la propension moyenne "
           "qui justifiait l’intervention publique."},
   {'t': "La consommation dépend aussi du patrimoine et de l’âge, que le "
         "revenu permanent n’intègre pas directement.",
    'qui': "Franco Modigliani, avec le modèle du cycle de vie.",
    'rep': "Le cours relève la proximité des deux auteurs : Modigliani rejoint "
           "Friedman en considérant l’individu comme rationnel et prévoyant, "
           "mais il introduit explicitement l’âge et la richesse patrimoniale."},
   {'t': "L’hypothèse d’individus rationnels et prévoyants est démentie par "
         "l’économie comportementale.",
    'qui': "Daniel Kahneman, pour qui les individus utilisent le plus souvent "
           "un système de pensée rapide et intuitif.",
    'rep': "L’objection atteint le cœur de la théorie, qui suppose une "
           "anticipation correcte du revenu futur sur l’ensemble de "
           "l’existence."},
   {'t': "Les ménages contraints par la liquidité consomment tout supplément "
         "de revenu, quel qu’il soit.",
    'qui': "La limite habituelle opposée aux théories du lissage "
           "intertemporel.",
    'rep': "L’objection est forte pour les ménages modestes et restaure "
           "l’efficacité d’une relance ciblée, puisqu’elle suppose "
           "l’impossibilité d’épargner le transitoire."}],
  [{'n': "Milton Friedman",
    'i': "La consommation est beaucoup plus stable que le revenu, car elle "
         "dépend du revenu permanent.",
    'p': "Le cours expose sa décomposition : le revenu permanent est la partie "
         "stable, anticipée et durable, déterminée par la qualification, "
         "l’expérience, la richesse et les perspectives d’emploi ; le revenu "
         "transitoire est la variation temporaire et aléatoire, comme une "
         "prime exceptionnelle."},
   {'n': "Milton Friedman",
    'i': "Le taux d’intérêt est le prix de la renonciation à la consommation.",
    'p': "C’est un second apport, que le cours oppose à la lecture "
         "keynésienne : pour les keynésiens le taux d’intérêt est le prix de "
         "la renonciation à la liquidité, de sorte que les deux écoles ne "
         "donnent pas le même sens à la même variable."},
   {'n': "John Maynard Keynes",
    'i': "La consommation dépend du revenu courant, selon la loi psychologique "
         "fondamentale.",
    'p': "Le cours en fait la cible explicite de Friedman et précise l’enjeu : "
         "la baisse de la propension moyenne à consommer avec la croissance du "
         "revenu justifie l’intervention de l’État pour conserver l’équilibre "
         "économique en économie fermée."},
   {'n': "Franco Modigliani",
    'i': "L’individu est rationnel et prévoyant, et répartit sa consommation "
         "sur l’ensemble de son existence.",
    'p': "Le cours souligne qu’il rejoint Friedman sur ce point, tout en "
         "introduisant deux variables supplémentaires que le revenu permanent "
         "n’intègre pas directement : la richesse patrimoniale et l’âge."}],
  [{'f': "Friedman observe que la consommation est en réalité beaucoup plus "
         "stable que le revenu et ne varie pas autant d’une période à l’autre.",
    'p': "L’observation est le point de départ empirique de toute la théorie "
         "et explique pourquoi elle s’est imposée face au modèle keynésien."},
   {'f': "Le revenu permanent est déterminé par la qualification, "
         "l’expérience, la richesse et les perspectives d’emploi de la "
         "personne.",
    'p': "L’énumération montre que le revenu permanent n’est pas une moyenne "
         "passée mais une anticipation fondée sur des caractéristiques "
         "durables."},
   {'f': "Le revenu transitoire représente la variation temporaire et "
         "aléatoire du revenu, comme une prime exceptionnelle.",
    'p': "L’exemple est celui qui permet de tester la théorie : une prime "
         "doit être largement épargnée si la théorie est exacte."},
   {'f': "Le cours oppose Keynes, économiste interventionniste, à Friedman, "
         "libéral, en notant que tous deux cherchaient à comprendre ce qui "
         "fait la consommation.",
    'p': "La mise en perspective montre que le désaccord théorique recouvre "
         "une divergence sur le rôle de l’État, ce qui éclaire l’enjeu du "
         "débat."}],
  [{'q': "Sujet du type « La consommation dépend-elle du revenu courant ? »",
    'f': "Friedman répond que non, à partir d’une observation : la "
         "consommation est beaucoup plus stable que le revenu et ne varie pas "
         "autant d’une période à l’autre. Il en conclut que les individus ne "
         "fondent pas leurs décisions sur leur revenu du moment, mais sur le "
         "revenu qu’ils s’attendent à percevoir durablement tout au long de "
         "leur vie. Le revenu courant se décompose donc en un revenu "
         "permanent, stable et anticipé, et un revenu transitoire, temporaire "
         "et aléatoire.",
    'r': "Le raisonnement part d’une anomalie empirique pour reconstruire la "
         "fonction de consommation, ce qui lui donne une force que n’aurait "
         "pas une simple objection théorique.",
    'ex': "Une prime exceptionnelle, revenu transitoire qui sera largement "
          "épargné plutôt que consommé."},
   {'q': "Sujet du type « Les politiques de relance de la demande sont-elles "
         "efficaces ? »",
    'f': "La théorie du revenu permanent en conteste le fondement même. Si les "
         "ménages consomment en proportion de leur revenu permanent, un "
         "supplément ponctuel de revenu, perçu comme transitoire, sera "
         "largement épargné et n’alimentera pas la demande. Le cours est "
         "explicite sur l’intention de Friedman : il s’agit de remettre en "
         "cause la justification keynésienne de l’intervention publique, "
         "fondée sur la baisse de la propension moyenne à consommer.",
    'r': "Le raisonnement attaque le multiplicateur par son paramètre central, "
         "la propension marginale, en montrant qu’elle dépend de la "
         "perception du caractère durable du revenu supplémentaire.",
    'ex': "Les ménages contraints par la liquidité, qui consomment tout "
          "supplément de revenu et restaurent l’efficacité d’une relance "
          "ciblée."}],
  voisins=['n7-propension', 'n7-cycle-vie', 'n7-consommation',
           'n7-epargne-precaution'])


d('n7-cycle-vie', 7, "Cycle de vie",
  "Épargner pendant la vie active pour désépargner ensuite",
  "Le modèle du cycle de vie, formulé par Franco Modigliani, établit que la "
  "consommation des ménages dépend en partie du revenu courant, mais aussi de "
  "la richesse, c’est-à-dire du patrimoine, et de l’âge. La consommation varie "
  "donc selon la position de la personne dans son cycle de vie : les jeunes "
  "désépargnent, les adultes épargnent durant leur vie active, et les "
  "retraités désépargnent à nouveau.",
  "Le modèle du cycle de vie complète celui de Keynes plutôt qu’il ne le "
  "contredit, et c’est ainsi que le cours le présente. Son mécanisme repose "
  "sur une idée simple : l’individu cherche à lisser sa consommation sur "
  "l’ensemble de son existence, alors que son revenu, lui, suit un profil en "
  "cloche. Trois phases en découlent. Pendant la jeunesse, le revenu est "
  "inférieur à la consommation souhaitée : l’individu désépargne ou emprunte. "
  "Pendant la vie active, le revenu dépasse la consommation : l’individu "
  "épargne. Pendant la retraite, il désépargne pour subvenir à sa consommation "
  "grâce à ce qu’il a accumulé au cours de sa vie. Le cours énumère trois "
  "atouts du modèle. Premier atout, il complète celui de Keynes en montrant "
  "que la consommation ne dépend pas seulement du revenu courant mais aussi de "
  "la richesse patrimoniale — épargne, biens, actifs détenus — et de l’âge, ce "
  "que le modèle keynésien ne faisait pas. Deuxième atout, il explique de "
  "façon réaliste la situation économique américaine des années 1950 : "
  "l’héritage y est très peu courant et la majorité des ménages doivent "
  "constituer eux-mêmes leur patrimoine au cours de leur vie, de sorte que la "
  "richesse n’est pas héritée mais accumulée progressivement grâce à l’épargne "
  "pendant les années d’activité, puis utilisée pendant la retraite. "
  "Troisième atout, il rejoint Friedman en considérant l’individu comme "
  "rationnel et prévoyant. Le cours signale cependant que le modèle présente "
  "aussi des défauts, ce qui invite à en discuter les hypothèses : la "
  "prévoyance supposée, la faiblesse de l’héritage et l’absence de contrainte "
  "de liquidité ne valent pas partout ni à toute époque.",
  [("Le profil en cloche du revenu",
    "Le revenu est faible dans la jeunesse, élevé pendant la vie active et "
    "faible à la retraite : c’est cette asymétrie entre le profil du revenu et "
    "celui des besoins qui crée le problème."),
   ("Le lissage de la consommation",
    "L’individu cherche à maintenir un niveau de consommation régulier sur "
    "l’ensemble de sa vie, ce qui l’oblige à transférer du pouvoir d’achat "
    "d’une période à l’autre."),
   ("La désépargne des jeunes",
    "Avant que le revenu n’atteigne son niveau courant, la consommation "
    "souhaitée excède les ressources : les jeunes ont tendance à désépargner "
    "ou à s’endetter."),
   ("L’accumulation pendant la vie active",
    "Pendant la période où le revenu dépasse la consommation, les ménages "
    "épargnent : cette accumulation constitue le patrimoine qui financera la "
    "retraite."),
   ("La désépargne des retraités",
    "À la retraite, l’individu désépargne pour subvenir à sa consommation "
    "grâce à ce qu’il a accumulé : le patrimoine est consommé plutôt que "
    "transmis.")],
  [{'a': "Le modèle complète Keynes en introduisant deux variables absentes de "
         "sa fonction de consommation, la richesse patrimoniale et l’âge.",
    'cond': "L’apport suppose que le patrimoine soit effectivement mobilisable "
            "pour financer la consommation.",
    'lim': "Une part importante du patrimoine des ménages est immobilière, "
           "donc peu liquide, ce qui limite la désépargne effective."},
   {'a': "Il explique de façon réaliste la situation américaine des années "
         "1950, où l’héritage est peu courant.",
    'cond': "L’explication est historiquement située : elle vaut pour une "
            "société où la majorité des ménages constituent eux-mêmes leur "
            "patrimoine.",
    'lim': "Dans une société où l’héritage redevient important, le motif "
           "d’accumulation n’est plus seulement la retraite, ce qui modifie le "
           "profil d’épargne."},
   {'a': "Il fournit une explication du taux d’épargne agrégé à partir de la "
         "structure par âge de la population.",
    'cond': "L’agrégation suppose que les générations soient de tailles "
            "comparables et que les comportements soient stables.",
    'lim': "Le vieillissement démographique modifie cette structure, ce qui "
           "rend le taux d’épargne agrégé dépendant de la démographie autant "
           "que des comportements."},
   {'a': "Il s’articule avec la théorie du revenu permanent pour former une "
         "approche intertemporelle cohérente.",
    'cond': "L’articulation repose sur une hypothèse commune, celle d’un "
            "individu rationnel et prévoyant.",
    'lim': "Le cours indique que le modèle présente aussi des défauts, et "
           "cette hypothèse est la plus exposée aux objections de l’économie "
           "comportementale."}],
  [{'t': "La consommation dépend du seul revenu courant, et non du "
         "patrimoine accumulé ni de l’âge du ménage.",
    'qui': "John Maynard Keynes, dont la fonction de consommation ignore ces "
           "deux variables.",
    'rep': "Le cours présente Modigliani comme complétant Keynes plutôt que "
           "comme le réfutant : son modèle explique l’évolution conjointe de "
           "la consommation et de l’épargne selon les étapes de la vie, ce que "
           "le modèle keynésien ne faisait pas."},
   {'t': "L’hypothèse d’un individu rationnel et prévoyant sur plusieurs "
         "décennies est beaucoup trop forte.",
    'qui': "Herbert Simon, avec la rationalité limitée.",
    'rep': "L’objection est particulièrement sérieuse ici, car le modèle exige "
           "une planification sur plusieurs décennies, alors que les agents "
           "recherchent des solutions satisfaisantes plutôt qu’optimales."},
   {'t': "L’épargne ne vise pas seulement la retraite mais aussi la "
         "précaution face à l’incertitude.",
    'qui': "L’analyse de l’épargne de précaution que le cours développe à "
           "propos de l’Allemagne et de la Chine.",
    'rep': "L’argument complète le modèle : quand la protection sociale "
           "devient moins généreuse, les ménages peuvent augmenter leur "
           "épargne de précaution, motif que le cycle de vie n’intègre pas."},
   {'t': "Le modèle suppose un patrimoine entièrement consommé, ce que "
         "contredit l’importance de l’héritage.",
    'qui': "La limite que le cours suggère en signalant que le modèle "
           "présente aussi des défauts.",
    'rep': "L’objection est historiquement datée : le modèle décrit bien une "
           "société où l’héritage est peu courant, moins bien une société où "
           "la transmission redevient un motif d’accumulation."}],
  [{'n': "Franco Modigliani",
    'i': "La consommation dépend du revenu courant, mais aussi de la richesse "
         "patrimoniale et de l’âge.",
    'p': "Son modèle du cycle de vie distingue trois phases : les jeunes "
         "désépargnent, les adultes épargnent durant leur vie active, et les "
         "retraités désépargnent à nouveau grâce à ce qu’ils ont accumulé au "
         "cours de leur vie."},
   {'n': "Franco Modigliani",
    'i': "L’individu est rationnel et prévoyant, ce qui lui permet de planifier "
         "sur l’ensemble de son existence.",
    'p': "C’est un second apport, de nature méthodologique, et le cours "
         "souligne qu’il rejoint Friedman sur ce point : les deux théories de "
         "la consommation reposent sur la même hypothèse d’anticipation "
         "rationnelle du revenu futur."},
   {'n': "Milton Friedman",
    'i': "La consommation dépend du revenu anticipé sur l’ensemble de la "
         "vie, et non du revenu du moment.",
    'p': "Sa théorie du revenu permanent est la plus proche du cycle de vie : "
         "toutes deux déplacent la fonction de consommation du plan statique "
         "au plan intertemporel, mais Modigliani y ajoute explicitement l’âge "
         "et le patrimoine."},
   {'n': "John Maynard Keynes",
    'i': "La consommation augmente avec le revenu courant mais à un rythme "
         "plus faible.",
    'p': "Le cours fait de sa fonction de consommation le point de départ que "
         "Modigliani élargit : le modèle du cycle de vie montre comment "
         "consommation et épargne évoluent selon les étapes de la vie, ce que "
         "le modèle keynésien ne faisait pas."}],
  [{'f': "Dans le modèle du cycle de vie, les jeunes désépargnent, les adultes "
         "épargnent durant leur vie active, et les retraités désépargnent à "
         "nouveau.",
    'p': "Les trois phases forment la structure complète du modèle et "
         "permettent de relier le comportement individuel au taux d’épargne "
         "agrégé."},
   {'f': "Le cours énonce que la consommation des ménages dépend en partie du "
         "revenu courant, mais aussi de la richesse, à savoir le patrimoine, "
         "et de l’âge.",
    'p': "La formulation montre que le modèle n’abandonne pas le revenu "
         "courant mais lui adjoint deux déterminants supplémentaires."},
   {'f': "Dans les années 1950 aux États-Unis, l’héritage est très peu courant "
         "et la majorité des ménages doivent constituer eux-mêmes leur "
         "patrimoine au cours de leur vie.",
    'p': "Le contexte historique explique la pertinence du modèle à l’époque "
         "et signale du même coup sa dépendance à une configuration sociale "
         "particulière."},
   {'f': "Le cours relève que Modigliani rejoint Friedman en considérant "
         "l’individu comme rationnel et prévoyant.",
    'p': "Le rapprochement permet de traiter les deux théories ensemble et de "
         "leur opposer une même objection comportementale."}],
  [{'q': "Sujet du type « Pourquoi les ménages épargnent-ils ? »",
    'f': "Le modèle du cycle de vie fournit une première réponse : pour lisser "
         "leur consommation. Le revenu suivant un profil en cloche, les jeunes "
         "désépargnent, les adultes épargnent durant leur vie active, et les "
         "retraités désépargnent à nouveau grâce à ce qu’ils ont accumulé. "
         "Mais l’épargne de précaution fournit une seconde réponse : le cours "
         "montre que lorsque la protection sociale devient moins généreuse, "
         "les ménages augmentent leur épargne de précaution face à "
         "l’incertitude.",
    'r': "Le raisonnement distingue un motif de lissage, lié au temps, d’un "
         "motif de précaution, lié au risque, ce qui permet d’expliquer des "
         "taux d’épargne très différents à structure démographique "
         "comparable.",
    'ex': "Le taux d’épargne des ménages chinois, qui dépasse 40 % du revenu "
          "disponible en raison notamment d’une protection sociale "
          "relativement peu développée."},
   {'q': "Sujet du type « Les théories de la consommation sont-elles "
         "concurrentes ou complémentaires ? »",
    'f': "Le cours penche nettement pour la complémentarité. Il présente le "
         "modèle de Modigliani comme élargissant la vision keynésienne en "
         "montrant que la consommation ne dépend pas seulement du revenu "
         "courant, mais aussi de la richesse patrimoniale et de l’âge : le "
         "modèle explique donc comment la consommation et l’épargne évoluent "
         "selon les étapes de la vie, ce que le modèle keynésien ne faisait "
         "pas.",
    'r': "Le raisonnement montre que chaque théorie ajoute une variable que la "
         "précédente ignorait, ce qui produit une accumulation de savoir "
         "plutôt qu’une succession de réfutations.",
    'ex': "La situation américaine des années 1950, où l’héritage étant peu "
          "courant les ménages constituaient eux-mêmes leur patrimoine."}],
  voisins=['n7-revenu-permanent', 'n7-epargne-precaution', 'n7-propension',
           'n7-revenu-disponible'])


d('n7-epargne-precaution', 7, "Épargne de précaution",
  "Épargner contre l’incertitude, et non pour un projet",
  "L’épargne de précaution désigne la part de l’épargne constituée en réponse "
  "à l’incertitude sur les revenus et les dépenses futures. Le cours en fait "
  "un déterminant majeur des taux d’épargne nationaux et en donne le mécanisme "
  "central : lorsque la protection sociale devient moins généreuse ou est peu "
  "développée, l’incertitude augmente et les ménages accroissent leur épargne "
  "de précaution.",
  "L’épargne de précaution est le motif d’épargne que ni le cycle de vie ni le "
  "revenu permanent ne prennent directement en charge, et c’est ce qui en fait "
  "l’intérêt. Son ressort est l’incertitude : un ménage qui ne sait pas s’il "
  "conservera son emploi, s’il devra faire face à une dépense de santé ou de "
  "quelle retraite il disposera constitue une réserve, indépendamment de tout "
  "projet de consommation future. Le cours en donne deux illustrations "
  "nationales très éclairantes. Le cas allemand d’abord : l’Allemagne présente "
  "traditionnellement une épargne élevée, expliquée par le vieillissement de "
  "la population, le comportement prudent des ménages, les réformes de la "
  "protection sociale et l’anticipation de dépenses futures ; le cours en tire "
  "une idée essentielle, quand la protection sociale devient moins généreuse, "
  "les ménages peuvent augmenter leur épargne de précaution. Le cas chinois "
  "ensuite, plus spectaculaire : le taux d’épargne des ménages chinois dépasse "
  "40 % du revenu disponible, ce qui est exceptionnellement élevé ; la "
  "première raison avancée est précisément l’épargne de précaution, la "
  "protection sociale chinoise étant relativement moins développée que dans "
  "les économies occidentales, de sorte que les ménages épargnent pour la "
  "santé, la retraite, le chômage et les dépenses futures. Le mécanisme est "
  "formulé par le cours en une chaîne : protection sociale faible, incertitude "
  "en hausse, épargne de précaution en hausse. Les conséquences "
  "macroéconomiques sont considérables. Une épargne de précaution élevée "
  "réduit la consommation, donc la demande intérieure, ce qui contribue aux "
  "excédents courants de l’Allemagne et de la Chine ; le cours relie "
  "d’ailleurs l’incertitude accrue sur l’emploi, favorisant l’épargne de "
  "précaution, aux mécanismes invoqués pour expliquer la stagnation séculaire.",
  [("L’incertitude sur les revenus futurs",
    "Un ménage qui ne peut prévoir son revenu — risque de chômage, de maladie, "
    "de baisse d’activité — constitue une réserve pour y faire face, en dehors "
    "de tout projet déterminé."),
   ("Le rôle de la protection sociale",
    "La protection sociale mutualise ces risques : plus elle est développée, "
    "moins le ménage a besoin de s’auto-assurer, et inversement sa réduction "
    "accroît l’épargne de précaution."),
   ("La substitution entre assurance collective et épargne individuelle",
    "Épargne et protection sociale remplissent la même fonction face au "
    "risque : elles sont donc substituables, ce qui explique que les taux "
    "d’épargne varient avec les institutions."),
   ("L’effet sur la demande intérieure",
    "Une épargne de précaution élevée réduit la consommation des ménages, donc "
    "la demande intérieure : l’économie produit alors davantage que sa demande "
    "interne ne peut absorber."),
   ("La traduction en excédent extérieur",
    "L’écart entre épargne et investissement se traduit en excédent courant : "
    "une forte épargne de précaution contribue ainsi aux déséquilibres "
    "mondiaux.")],
  [{'a': "La notion explique des écarts de taux d’épargne que ni le cycle de "
         "vie ni le revenu permanent ne peuvent rendre intelligibles.",
    'cond': "L’explication suppose que l’incertitude soit effectivement "
            "perçue, ce qui dépend de l’information et de l’expérience des "
            "ménages.",
    'lim': "Elle est difficile à isoler empiriquement des autres motifs "
           "d’épargne, qui jouent simultanément."},
   {'a': "Elle relie directement les institutions sociales aux comportements "
         "économiques, ce qui en fait un argument de politique publique.",
    'cond': "Le lien suppose que les ménages anticipent correctement le niveau "
            "de couverture dont ils bénéficieront.",
    'lim': "Cette anticipation suppose une information sur des dispositifs "
           "complexes, souvent mal connus des ménages concernés."},
   {'a': "Elle éclaire les déséquilibres courants mondiaux, en montrant que "
         "l’excédent peut refléter une faiblesse de la demande interne.",
    'cond': "L’argument suppose que l’investissement intérieur n’absorbe pas la "
            "totalité de l’épargne dégagée.",
    'lim': "Le cas allemand montre que l’excédent résulte aussi d’un "
           "investissement public insuffisant, lié à une tradition "
           "ordolibérale, et pas seulement de l’épargne."},
   {'a': "Elle fournit un levier d’action : renforcer la protection sociale "
         "peut soutenir la consommation.",
    'cond': "Le levier suppose que la réduction de l’incertitude soit "
            "perçue comme durable et crédible.",
    'lim': "Le renforcement a un coût budgétaire et peut lui-même nourrir une "
           "incertitude sur sa pérennité, ce qui atténue l’effet attendu."}],
  [{'t': "L’épargne élevée traduit une préférence culturelle pour la prudence "
         "plutôt qu’une réponse institutionnelle.",
    'qui': "La lecture par le comportement prudent des ménages que le cours "
           "mentionne pour l’Allemagne.",
    'rep': "Le cours cite ce facteur mais l’associe à d’autres explicitement "
           "institutionnels : vieillissement de la population, réformes de la "
           "protection sociale et anticipation de dépenses futures."},
   {'t': "Un excédent courant élevé est toujours le signe d’une économie "
         "performante et compétitive.",
    'qui': "La lecture mercantiliste traditionnelle de l’excédent.",
    'rep': "Le cours la conteste pour l’Allemagne : l’excédent doit être "
           "nuancé car il reflète en partie une épargne élevée associée à un "
           "investissement public et privé insuffisant."},
   {'t': "La faible protection sociale chinoise n’est qu’une explication parmi "
         "d’autres du taux d’épargne.",
    'qui': "L’analyse en trois raisons que le cours développe pour la Chine.",
    'rep': "L’objection est juste : le cours ajoute le déséquilibre "
           "démographique lié à la politique de l’enfant unique, certaines "
           "familles ayant accru leur épargne pour améliorer la position de "
           "leur fils."},
   {'t': "L’épargne abondante finance mécaniquement l’investissement "
         "productif et soutient donc la croissance.",
    'qui': "La conception classique du lien entre épargne et investissement.",
    'rep': "Le cours objecte que paradoxalement l’épargne abondante ne finance "
           "pas l’investissement productif, alimente parfois les marchés "
           "financiers et des bulles spéculatives, sans générer de gains de "
           "croissance réels."}],
  [{'n': "Franco Modigliani",
    'i': "L’épargne se constitue pendant la vie active pour financer la "
         "retraite.",
    'p': "Son modèle du cycle de vie fournit un motif d’épargne distinct du "
         "motif de précaution : l’un répond au profil temporel du revenu, "
         "l’autre à l’incertitude, et les deux peuvent se cumuler chez un même "
         "ménage."},
   {'n': "Milton Friedman",
    'i': "Le revenu transitoire, imprévisible et non reconductible, est "
         "principalement épargné.",
    'p': "Sa théorie éclaire le lien entre incertitude et épargne : un revenu "
         "perçu comme aléatoire ne modifie pas la consommation, ce qui "
         "rapproche le comportement décrit du motif de précaution."},
   {'n': "Hélène Rey",
    'i': "Les déséquilibres mondiaux excessifs reflètent des stratégies de "
         "croissance déséquilibrées.",
    'p': "Le cours la mobilise à propos des excédents courants : l’épargne "
         "élevée de certains pays, associée à un investissement insuffisant, "
         "traduit un modèle de croissance qui ne repose pas sur la demande "
         "interne."}],
  [{'f': "Le cours formule le mécanisme en une chaîne : protection sociale "
         "faible, incertitude en hausse, épargne de précaution en hausse.",
    'p': "La chaîne est directement reproductible et établit le lien causal "
         "entre institutions sociales et comportement d’épargne."},
   {'f': "Le taux d’épargne des ménages chinois dépasse 40 % du revenu "
         "disponible, ce qui est exceptionnellement élevé.",
    'p': "Le chiffre donne un ordre de grandeur frappant et montre l’ampleur "
         "possible de l’effet des institutions sur les comportements."},
   {'f': "L’épargne élevée de l’Allemagne s’explique par le vieillissement de "
         "la population, le comportement prudent des ménages, les réformes de "
         "la protection sociale et l’anticipation de dépenses futures.",
    'p': "L’énumération montre que plusieurs causes se cumulent, dont deux "
         "sont institutionnelles et une démographique."},
   {'f': "Le cours cite l’incertitude accrue sur l’emploi, favorisant "
         "l’épargne de précaution, parmi les mécanismes invoqués pour "
         "expliquer la stagnation séculaire.",
    'p': "Le fait relie un comportement microéconomique à un diagnostic "
         "macroéconomique de long terme, ce qui en montre la portée."}],
  [{'q': "Sujet du type « Pourquoi certains pays épargnent-ils autant ? »",
    'f': "Le cours met l’accent sur les institutions plutôt que sur les "
         "préférences. La chaîne causale est explicite : une protection "
         "sociale faible accroît l’incertitude, ce qui augmente l’épargne de "
         "précaution. La Chine en fournit l’illustration la plus nette, son "
         "taux d’épargne dépassant 40 % du revenu disponible, les ménages "
         "épargnant pour la santé, la retraite, le chômage et les dépenses "
         "futures faute d’une couverture comparable à celle des économies "
         "occidentales.",
    'r': "Le raisonnement remplace une explication culturelle par une "
         "explication institutionnelle, ce qui a l’avantage d’être testable et "
         "de désigner un levier d’action.",
    'ex': "L’Allemagne, où les réformes de la protection sociale et "
          "l’anticipation de dépenses futures contribuent à une épargne "
          "traditionnellement élevée."},
   {'q': "Sujet du type « Un excédent courant est-il un signe de "
         "performance ? »",
    'f': "Pas nécessairement, car il peut refléter une insuffisance de la "
         "demande intérieure. Le cours est explicite pour l’Allemagne : "
         "l’excédent courant doit être nuancé car il reflète en partie une "
         "épargne élevée associée à un investissement public et privé "
         "insuffisant, lié à une tradition ordolibérale marquée par la "
         "discipline budgétaire et la méfiance envers les déficits.",
    'r': "Le raisonnement décompose l’excédent en ses deux déterminants, "
         "l’épargne et l’investissement, ce qui permet de distinguer un "
         "excédent de compétitivité d’un excédent de faiblesse de la demande.",
    'ex': "Le plan d’investissement allemand de l’ordre de 500 milliards "
          "d’euros, destiné à réduire l’écart entre épargne et investissement."}],
  voisins=['n7-cycle-vie', 'n7-revenu-permanent', 'n7-propension',
           'n7-revenu-disponible'])


d('n7-rationalite-limitee', 7, "Rationalité limitée",
  "Chercher une solution satisfaisante plutôt que la meilleure",
  "La rationalité limitée, formulée par Herbert Simon, établit que les "
  "individus ne maximisent pas leurs choix mais recherchent des solutions "
  "satisfaisantes plutôt qu’optimales. Leurs capacités de calcul sont bornées, "
  "leur information est incomplète et le temps dont ils disposent est limité, "
  "de sorte qu’ils s’arrêtent dès qu’une option atteint un seuil "
  "d’acceptabilité.",
  "La rationalité limitée est la critique la plus profonde adressée au modèle "
  "standard, et le cours en mesure précisément la portée. Il la situe à la fin "
  "d’une série : après Arrow et Debreu, qui montrent que les conditions "
  "d’existence de l’équilibre sont irréalistes ; après Pareto, dont le critère "
  "est une efficacité sans justice ; après Sonnenschein, Mantel et Debreu, qui "
  "établissent que la stabilité n’est pas garantie — Simon arrive comme le "
  "coup de grâce : même si les conditions mathématiques étaient remplies, les "
  "agents réels ne seraient pas capables de se comporter comme le modèle "
  "l’exige. Le cours en tire une formule qui résume tout le chapitre : la "
  "microéconomie standard est mathématiquement élégante et intellectuellement "
  "puissante, mais psychologiquement et sociologiquement très fragile. Le "
  "contenu de la critique est double. D’une part l’information : la théorie "
  "néoclassique suppose une information parfaite, gratuite et symétrique entre "
  "tous les agents, ce qu’elle appelle la transparence, alors qu’en réalité "
  "c’est l’asymétrie qui domine. D’autre part le traitement : le cours formule "
  "la distinction décisive, on ne possède pas l’information, mais aussi on ne "
  "traite pas l’information. Simon s’attaque donc non à la disponibilité des "
  "données mais à la capacité cognitive de les exploiter. Sa portée dépasse "
  "largement la théorie du consommateur : le cours mobilise sa rationalité "
  "limitée dans l’analyse de la firme, où elle explique que l’entreprise ne "
  "soit pas un simple automate réagissant aux prix, et dans l’analyse des "
  "organisations, où elle prépare les travaux sur les décisions absurdes et "
  "sur les stratégies d’acteurs. Elle ouvre enfin directement sur l’économie "
  "comportementale de Kahneman et Thaler.",
  [("La limitation des capacités cognitives",
    "Le cerveau humain ne traite pas l’information comme un ordinateur : les "
    "capacités de calcul sont bornées, ce qui interdit de comparer toutes les "
    "options possibles."),
   ("Le coût du temps et de l’information",
    "Chercher et traiter l’information prend du temps et coûte des ressources : "
    "au-delà d’un certain point, le coût de la recherche excède le gain attendu "
    "d’une meilleure décision."),
   ("Le recours à un seuil d’acceptabilité",
    "Plutôt que de chercher le maximum, l’agent se fixe un niveau "
    "d’aspiration : il retient la première option qui l’atteint, ce qui "
    "remplace l’optimisation par la satisfaction."),
   ("La distinction entre posséder et traiter",
    "Le problème n’est pas seulement qu’on ne possède pas l’information, c’est "
    "aussi qu’on ne la traite pas : même disponible, elle excède les capacités "
    "de traitement de l’agent."),
   ("L’extension aux organisations",
    "Ce qui vaut pour l’individu vaut pour les entreprises et les "
    "administrations : elles ne sont pas des automates réagissant "
    "mécaniquement aux signaux, mais des organisations aux capacités de "
    "décision bornées.")],
  [{'a': "La rationalité limitée atteint le modèle standard à un point que "
         "les autres critiques épargnent, celui de la capacité à décider.",
    'cond': "L’argument suppose que la maximisation exige des capacités "
            "cognitives supérieures à celles des agents réels.",
    'lim': "Elle ne propose pas de modèle alternatif aussi général, ce qui "
           "explique la persistance du cadre standard."},
   {'a': "Elle explique des comportements observés que l’optimisation ne "
         "prédit pas, comme l’arrêt précoce de la recherche d’information.",
    'cond': "L’explication suppose un niveau d’aspiration identifiable, qui "
            "dépend du contexte et de l’expérience de l’agent.",
    'lim': "Ce niveau étant variable, les prédictions sont moins précises que "
           "celles du modèle standard."},
   {'a': "Elle s’applique aussi bien à l’individu qu’à l’organisation, ce qui "
         "en fait un outil transversal.",
    'cond': "La transposition suppose que l’organisation soit traitée comme un "
            "lieu de décision et non comme une fonction de production.",
    'lim': "Elle gomme les différences entre décision individuelle et décision "
           "collective, que Crozier et Morel analysent séparément."},
   {'a': "Elle ouvre la voie à l’économie comportementale, qui en précise "
         "expérimentalement les mécanismes.",
    'cond': "L’articulation suppose que les écarts à la rationalité soient "
            "systématiques et non aléatoires.",
    'lim': "C’est précisément ce que Kahneman établit avec les biais "
           "cognitifs, qui sont des erreurs systématiques de jugement."}],
  [{'t': "Même si les conditions mathématiques du modèle étaient remplies, les "
         "agents réels n’en seraient pas capables.",
    'qui': "Herbert Simon, dont le cours fait le coup de grâce porté au modèle "
           "standard.",
    'rep': "L’objection est imparable dans son ordre : elle ne conteste pas la "
           "cohérence du modèle mais sa pertinence descriptive, ce que le "
           "cours résume par une microéconomie élégante mais fragile."},
   {'t': "La vraie difficulté n’est pas la quantité d’information mais la "
         "façon dont elle est traitée.",
    'qui': "La distinction que le cours formule : on ne possède pas "
           "l’information, mais aussi on ne traite pas l’information.",
    'rep': "La distinction est essentielle : elle sépare le problème "
           "informationnel d’Akerlof, qui porte sur la répartition, du "
           "problème cognitif de Simon, qui porte sur le traitement."},
   {'t': "Les écarts à la rationalité sont systématiques et prennent la forme "
         "de biais cognitifs.",
    'qui': "Daniel Kahneman, dont le cours expose les deux systèmes de pensée.",
    'rep': "L’apport précise la rationalité limitée : le système 1 rapide, "
           "intuitif et émotionnel, utilisé dans la plupart des situations, "
           "produit des erreurs de jugement régulières et prévisibles."},
   {'t': "Dans les organisations, la rationalité limitée se combine à des "
         "stratégies de pouvoir.",
    'qui': "Michel Crozier, avec l’analyse stratégique des organisations.",
    'rep': "Le prolongement est important : les acteurs ne subissent pas "
           "seulement l’incertitude, ils l’utilisent à leur avantage, ce qui "
           "transforme une limite cognitive en ressource stratégique."}],
  [{'n': "Herbert Simon",
    'i': "Les individus ne maximisent pas leurs choix mais recherchent des "
         "solutions satisfaisantes plutôt qu’optimales.",
    'p': "Le cours le place après Arrow-Debreu, Pareto et "
         "Sonnenschein-Mantel-Debreu, comme coup de grâce : même si les "
         "conditions mathématiques étaient remplies, les agents réels ne "
         "seraient pas capables de se comporter comme le modèle l’exige."},
   {'n': "Daniel Kahneman",
    'i': "Le comportement repose sur un système 1 rapide, intuitif et "
         "émotionnel, et un système 2 lent et réfléchi.",
    'p': "Le cours précise que dans la plupart des situations les individus "
         "utilisent le système 1, ce qui conduit à des biais cognitifs, "
         "c’est-à-dire des erreurs de jugement qui éloignent de la rationalité "
         "au sens de la théorie standard."},
   {'n': "George Akerlof",
    'i': "L’information est asymétrique : certains agents en savent plus que "
         "d’autres.",
    'p': "Le cours distingue soigneusement son apport de celui de Simon : "
         "Akerlof porte sur la répartition de l’information entre agents, "
         "Simon sur la capacité de chacun à la traiter, deux problèmes "
         "différents qui se cumulent."},
   {'n': "Michel Crozier",
    'i': "Les acteurs utilisent les zones d’incertitude à leur avantage.",
    'p': "Son analyse prolonge la rationalité limitée dans les "
         "organisations : l’incertitude n’y est pas seulement subie, elle est "
         "entretenue par ceux à qui elle profite, ce qui en fait un enjeu de "
         "pouvoir."}],
  [{'f': "Le cours formule la double limite ainsi : on ne possède pas "
         "l’information, mais aussi on ne traite pas l’information.",
    'p': "La formulation sépare nettement deux critiques du modèle standard "
         "souvent confondues, l’une informationnelle et l’autre cognitive."},
   {'f': "Le cours conclut que la microéconomie standard est mathématiquement "
         "élégante et intellectuellement puissante, mais psychologiquement et "
         "sociologiquement très fragile.",
    'p': "La formule est directement citable comme conclusion d’une "
         "dissertation sur les limites du modèle standard."},
   {'f': "Le cours présente Simon comme arrivant après Arrow-Debreu, Pareto et "
         "Sonnenschein-Mantel-Debreu, en coup de grâce.",
    'p': "L’ordre des critiques montre qu’elles portent successivement sur "
         "l’existence, l’optimalité, la stabilité et enfin la plausibilité "
         "comportementale."},
   {'f': "Le cours mobilise la rationalité limitée dans l’analyse de la firme, "
         "où elle explique que l’entreprise ne soit pas un simple automate "
         "réagissant aux prix.",
    'p': "L’application montre la portée de la notion au-delà de la théorie du "
         "consommateur, jusqu’à la théorie de l’entreprise."}],
  [{'q': "Sujet du type « Les agents économiques sont-ils rationnels ? »",
    'f': "Simon répond qu’ils le sont, mais de façon limitée : les individus "
         "ne maximisent pas leurs choix et recherchent des solutions "
         "satisfaisantes plutôt qu’optimales. Le cours précise la nature de la "
         "limite en distinguant deux problèmes : on ne possède pas "
         "l’information, mais aussi on ne traite pas l’information. Il en tire "
         "une conclusion générale : la microéconomie standard est "
         "mathématiquement élégante et intellectuellement puissante, mais "
         "psychologiquement et sociologiquement très fragile.",
    'r': "Le raisonnement distingue la rationalité comme intention, qui n’est "
         "pas contestée, de la rationalité comme capacité, qui l’est, ce qui "
         "évite de caricaturer les agents en êtres irrationnels.",
    'ex': "L’arrêt de la recherche d’information dès qu’une option atteint un "
          "niveau jugé acceptable."},
   {'q': "Sujet du type « Faut-il abandonner le modèle de l’homo "
         "œconomicus ? »",
    'f': "La critique de Simon invite à le relativiser plutôt qu’à l’abandonner. "
         "Le cours la situe dans une série : Arrow-Debreu montrent que les "
         "conditions d’existence sont irréalistes, Pareto que l’optimalité est "
         "une efficacité sans justice, Sonnenschein-Mantel-Debreu que la "
         "stabilité n’est pas garantie, et Simon ajoute que même si les "
         "conditions mathématiques étaient remplies, les agents réels n’en "
         "seraient pas capables.",
    'r': "Le raisonnement montre que les critiques sont cumulatives et portent "
         "sur des points distincts, ce qui interdit de répondre à l’une pour "
         "sauver le modèle de toutes les autres.",
    'ex': "L’économie comportementale de Kahneman et Thaler, qui prolonge "
          "Simon en identifiant des biais cognitifs systématiques."}],
  voisins=['n7-biais', 'n7-utilite', 'n7-choix', 'n6-asymetries'])


d('n7-biais', 7, "Biais comportementaux",
  "Des erreurs de jugement régulières, donc prévisibles",
  "Les biais cognitifs sont des erreurs systématiques de jugement qui "
  "éloignent les individus de la rationalité au sens de la théorie standard. "
  "L’économie comportementale, portée par Daniel Kahneman et Richard Thaler, "
  "montre que notre cerveau ne fonctionne pas comme un ordinateur rationnel : "
  "nous utilisons des raccourcis mentaux et commettons des erreurs "
  "systématiques.",
  "L’économie comportementale prolonge la rationalité limitée en la rendant "
  "prédictive, et c’est ce passage qui fait tout l’intérêt du dossier. Le "
  "point de départ est critique : la théorie microéconomique repose sur "
  "l’hypothèse d’un individu parfaitement rationnel, l’homo œconomicus, "
  "capable d’optimiser ses choix grâce à une information complète et à des "
  "capacités de calcul illimitées. Les travaux comportementaux montrent qu’il "
  "n’en est rien. Kahneman établit que le comportement repose sur deux "
  "systèmes de pensée : un système 1 rapide, intuitif et émotionnel, et un "
  "système 2 lent, réfléchi et rationnel ; or dans la plupart des situations "
  "les individus utilisent le système 1, ce qui conduit à des biais cognitifs. "
  "Le cours en donne une démonstration expérimentale frappante, l’effet "
  "d’ancrage : on demande à des participants leurs deux derniers chiffres de "
  "sécurité sociale, puis combien ils seraient prêts à payer pour une bonne "
  "bouteille de vin ; le prix donné est souvent proche du numéro de sécurité "
  "sociale, pourtant totalement sans rapport avec le vin. La conséquence "
  "économique est explicite : les prix et les décisions ne sont pas uniquement "
  "rationnels, ils sont influencés par des références arbitraires, ce qui "
  "contredit la théorie standard. Thaler va plus loin : nos préférences ne "
  "sont pas fixes, elles dépendent de la manière dont on formule un choix. "
  "C’est le principe du nudge, qui consiste à influencer les comportements "
  "sans interdire ni obliger, simplement en modifiant la présentation des "
  "options — l’exemple du don d’organes est net, une case déjà cochée produit "
  "beaucoup plus de donneurs qu’une case non cochée. La conclusion du cours "
  "est à retenir : ce n’est pas la rationalité qui change, c’est la "
  "formulation qui guide le choix, et l’homo œconomicus n’existe pas dans la "
  "réalité.",
  [("La prédominance du système intuitif",
    "Face à une décision, le système 1 — rapide, intuitif et émotionnel — "
    "s’active en premier ; le système 2, lent et réfléchi, n’intervient que si "
    "l’effort est consenti, ce qui est rare."),
   ("Le recours aux raccourcis mentaux",
    "Pour économiser l’effort, l’individu applique des règles simples plutôt "
    "qu’un calcul complet : ces raccourcis fonctionnent souvent mais "
    "produisent des erreurs dans certaines configurations."),
   ("Le caractère systématique des erreurs",
    "Les écarts à la rationalité ne sont pas aléatoires : ce sont des erreurs "
    "régulières, donc prévisibles, ce qui permet d’en faire un objet de "
    "science et un levier d’action."),
   ("L’ancrage sur une référence arbitraire",
    "Une information sans rapport avec la décision oriente néanmoins le "
    "jugement : les prix et les décisions sont influencés par des références "
    "arbitraires, ce qui contredit la théorie standard."),
   ("La dépendance au cadrage",
    "Les préférences ne sont pas fixes mais dépendent de la manière dont le "
    "choix est formulé : modifier la présentation des options change le "
    "résultat sans rien interdire ni obliger.")],
  [{'a': "L’approche comportementale rend les écarts à la rationalité "
         "prévisibles, ce qui en fait une science et non un simple constat "
         "d’imperfection.",
    'cond': "La prédictibilité suppose que les biais soient systématiques et "
            "reproductibles en laboratoire.",
    'lim': "Le passage du laboratoire aux marchés réels n’est pas immédiat, "
           "les incitations et l’expérience pouvant atténuer certains biais."},
   {'a': "Elle fournit un instrument d’action publique peu coûteux et très "
         "peu contraignant, le nudge.",
    'cond': "L’instrument suppose qu’une option par défaut puisse être "
            "définie, ce qui n’est pas toujours le cas.",
    'lim': "Il pose une question de légitimité : influencer sans informer "
           "revient à décider pour autrui sans le lui dire."},
   {'a': "Elle précise la rationalité limitée de Simon en identifiant les "
         "mécanismes concrets des écarts observés.",
    'cond': "L’articulation suppose d’admettre que les deux systèmes de pensée "
            "décrivent effectivement le fonctionnement cognitif.",
    'lim': "Elle ne fournit pas de modèle unifié de remplacement, mais une "
           "collection de biais documentés séparément."},
   {'a': "Elle a des conséquences directes sur l’analyse des marchés, "
         "puisqu’elle remet en cause la formation rationnelle des prix.",
    'cond': "L’argument suppose que les biais ne se compensent pas "
            "statistiquement à l’échelle du marché.",
    'lim': "C’est précisément parce que les erreurs sont systématiques et non "
           "aléatoires qu’elles ne se compensent pas, ce qui renforce "
           "l’objection."}],
  [{'t': "L’homo œconomicus parfaitement rationnel n’existe tout simplement "
         "pas dans la réalité observée.",
    'qui': "La conclusion que le cours tire des travaux d’économie "
           "comportementale.",
    'rep': "L’affirmation est forte mais documentée expérimentalement : "
           "l’effet d’ancrage montre que le jugement est influencé par des "
           "informations sans rapport avec la décision."},
   {'t': "Les préférences ne sont pas fixes mais dépendent étroitement de la "
         "formulation du choix proposé.",
    'qui': "Richard Thaler, avec le principe du nudge.",
    'rep': "La formulation du cours est précise : ce n’est pas la rationalité "
           "qui change, c’est la formulation qui guide le choix, ce qui atteint "
           "l’hypothèse de préférences données et stables."},
   {'t': "Les biais individuels s’aggravent dans les organisations par le "
         "conformisme et la pensée de groupe.",
    'qui': "Christian Morel, dont le cours analyse les décisions absurdes.",
    'rep': "Le prolongement est essentiel : les biais cognitifs individuels, "
           "la pression hiérarchique et le conformisme peuvent transformer une "
           "organisation censée rationnelle en système producteur d’erreurs "
           "radicales."},
   {'t': "La préférence pour les raisonnements simples et rapides accroît la "
         "vulnérabilité aux biais cognitifs.",
    'qui': "Gérald Bronner, avec l’avarice cognitive.",
    'rep': "Le mécanisme est rattaché par le cours au système 1 de Kahneman : "
           "les individus privilégient les explications simples et les "
           "réponses rapides, ce qui les expose davantage aux erreurs de "
           "jugement."}],
  [{'n': "Daniel Kahneman",
    'i': "Le comportement repose sur deux systèmes de pensée, et c’est le "
         "système intuitif qui prévaut le plus souvent.",
    'p': "Le cours définit le biais cognitif comme une erreur de jugement que "
         "l’on commet et qui éloigne de la rationalité au sens de la théorie "
         "standard, ce qui remet en cause l’hypothèse de rationalité parfaite "
         "de la microéconomie."},
   {'n': "Daniel Kahneman",
    'i': "Les jugements de prix sont ancrés sur des références arbitraires.",
    'p': "C’est un second apport, expérimental : interrogés après avoir donné "
         "leurs deux derniers chiffres de sécurité sociale, les participants "
         "proposent pour une bouteille de vin un prix souvent proche de ce "
         "numéro, pourtant totalement sans rapport."},
   {'n': "Richard Thaler",
    'i': "On peut influencer les comportements sans interdire ni obliger, en "
         "modifiant la présentation des options.",
    'p': "C’est le principe du nudge, que le cours illustre par le don "
         "d’organes : une case déjà cochée produit beaucoup plus de donneurs "
         "qu’une case non cochée, sans qu’aucune règle n’ait changé."},
   {'n': "Christian Morel",
    'i': "Les biais individuels se combinent dans les organisations pour "
         "produire des décisions absurdes.",
    'p': "Le cours précise la solution qu’il propose : organiser la "
         "contradiction, l’apprentissage et la remontée de l’expertise, ainsi "
         "que recourir à des check-lists, dont l’usage a permis de réduire la "
         "mortalité dans certains blocs opératoires de 50 %."}],
  [{'f': "Le cours définit le biais cognitif comme une erreur de jugement que "
         "l’on commet et qui éloigne de la rationalité au sens de la théorie "
         "standard.",
    'p': "La définition rattache explicitement le biais à un référentiel, "
         "celui du modèle standard, ce qui évite d’en faire un simple jugement "
         "sur les capacités humaines."},
   {'f': "Dans l’expérience d’ancrage, on demande aux participants leurs deux "
         "derniers chiffres de sécurité sociale puis combien ils paieraient "
         "une bonne bouteille de vin, et le prix donné est souvent proche de "
         "ce numéro.",
    'p': "L’expérience est la démonstration la plus nette du dossier : elle "
         "isole une influence dont l’absurdité est manifeste."},
   {'f': "Pour le don d’organes, une case déjà cochée produit beaucoup plus de "
         "donneurs qu’une case non cochée.",
    'p': "L’exemple montre qu’une politique publique peut obtenir un résultat "
         "majeur sans contrainte ni dépense, par la seule architecture du "
         "choix."},
   {'f': "L’usage des check-lists a permis de réduire la mortalité dans "
         "certains blocs opératoires de 50 %.",
    'p': "Le chiffre montre que la correction des biais peut produire des "
         "effets considérables et qu’elle relève de l’organisation autant que "
         "de la psychologie."}],
  [{'q': "Sujet du type « L’hypothèse de rationalité est-elle encore "
         "défendable ? »",
    'f': "Les travaux d’économie comportementale la contestent "
         "expérimentalement. Kahneman montre que le comportement repose sur un "
         "système 1 rapide, intuitif et émotionnel, et un système 2 lent et "
         "réfléchi, et que dans la plupart des situations les individus "
         "utilisent le système 1, ce qui conduit à des biais cognitifs, "
         "c’est-à-dire des erreurs de jugement qui éloignent de la rationalité "
         "au sens de la théorie standard.",
    'r': "Le raisonnement montre que les écarts sont systématiques et non "
         "aléatoires, ce qui interdit de les traiter comme un bruit qui se "
         "compenserait à l’échelle du marché.",
    'ex': "L’effet d’ancrage, où un numéro de sécurité sociale influence le "
          "prix proposé pour une bouteille de vin."},
   {'q': "Sujet du type « Comment orienter les comportements sans "
         "contraindre ? »",
    'f': "Thaler répond par le nudge : on influence les comportements sans "
         "interdire ni obliger, simplement en modifiant la présentation des "
         "options, puisque nos préférences ne sont pas fixes et dépendent de "
         "la manière dont on formule un choix. L’exemple du don d’organes est "
         "décisif, une case déjà cochée produisant beaucoup plus de donneurs "
         "qu’une case non cochée. Comme le résume le cours, ce n’est pas la "
         "rationalité qui change, c’est la formulation qui guide le choix.",
    'r': "Le raisonnement identifie un instrument de politique publique "
         "entièrement distinct des trois familles classiques — règle, prix, "
         "quantité — puisqu’il n’agit ni sur les contraintes ni sur les coûts.",
    'ex': "Les check-lists, dont l’usage a réduit la mortalité dans certains "
          "blocs opératoires de 50 %."}],
  voisins=['n7-rationalite-limitee', 'n7-utilite', 'n7-choix',
           'n6-asymetries'])
