# -*- coding: utf-8 -*-
"""Ensemble 20 — Les changes et les déséquilibres internationaux (1/4)."""

from doss_base import d

d('n20-balance-paiements', 20, "Balance des paiements",
  "Toujours équilibrée comptablement, jamais sans déséquilibres",
  "La balance des paiements est le document comptable qui recense tous les "
  "flux économiques et financiers entre résidents et non-résidents pendant "
  "une période donnée. Fonctionnant en partie double, elle est "
  "nécessairement équilibrée dans son ensemble, mais ses sous-comptes "
  "peuvent révéler d’importants déséquilibres extérieurs : déficit ou "
  "excédent commercial, déficit ou excédent courant, entrées ou sorties "
  "nettes de capitaux.",
  "Le cours fait de la balance des paiements le document de référence pour "
  "mesurer les flux entre une économie nationale et le reste du monde : "
  "elle enregistre les échanges de biens, les échanges de services, les "
  "revenus, les transferts, les investissements directs étrangers, les "
  "placements financiers, les prêts et les emprunts, et elle permet de "
  "répondre à deux grandes questions, comment un pays échange-t-il avec le "
  "reste du monde et comment finance-t-il ses éventuels déficits "
  "extérieurs. L’idée centrale à retenir est que la balance des paiements "
  "est toujours comptablement équilibrée, mais que cela ne signifie pas "
  "qu’il n’existe aucun déséquilibre. Le principe est celui de la partie "
  "double : chaque opération possède une contrepartie, de sorte que si la "
  "France exporte un bien pour 100 euros il y a sortie d’un bien et entrée "
  "d’un paiement de 100 euros, l’opération étant enregistrée deux fois. Le "
  "critère d’enregistrement n’est pas la nationalité mais le lieu principal "
  "d’activité économique : une entreprise étrangère implantée durablement "
  "en France peut être résidente française, un Français installé "
  "durablement ailleurs peut être non-résident. Le cours distingue ensuite "
  "le « haut » et le « bas » de la balance. Le haut est le compte des "
  "transactions courantes, qui comprend les biens, les services, les revenus "
  "primaires et les revenus secondaires ; les exportations y sont inscrites "
  "en crédit, c’est-à-dire en flux entrant de paiement, les importations en "
  "débit. Entre les deux figure le compte de capital, qui enregistre "
  "certains transferts en capital et certaines opérations sur actifs non "
  "financiers non produits, mais qui est quantitativement beaucoup moins "
  "central. Le bas est le compte financier, qui enregistre les mouvements de "
  "capitaux : investissements directs, investissements de portefeuille, "
  "produits dérivés, autres investissements, avoirs de réserve ; il "
  "distingue les avoirs, actifs détenus par les résidents sur le reste du "
  "monde, des engagements, actifs domestiques détenus par les "
  "non-résidents. Le cours en tire la relation macroéconomique "
  "fondamentale : le haut et le bas de la balance se répondent, un déficit "
  "courant créant un besoin de financement compensé par des entrées nettes "
  "de capitaux, un excédent courant dégageant une capacité de financement "
  "qui se traduit par des sorties nettes.",
  [("L’enregistrement de tous les flux avec le reste du monde",
    "La balance recense les échanges de biens et de services, les revenus, "
    "les transferts, les investissements directs, les placements financiers, "
    "les prêts et les emprunts entre résidents et non-résidents sur une "
    "période donnée."),
   ("Le critère de résidence et non de nationalité",
    "Ce qui compte n’est pas la nationalité mais le lieu principal "
    "d’activité économique : une entreprise étrangère implantée durablement "
    "en France peut être résidente, un Français installé durablement "
    "ailleurs peut être non-résident."),
   ("Le principe de la partie double",
    "Chaque opération possède une contrepartie : une exportation de 100 "
    "euros produit une sortie de bien et une entrée de paiement de 100 "
    "euros, enregistrées toutes deux, ce qui garantit l’équilibre comptable "
    "global."),
   ("La structure en haut et bas de balance",
    "Le haut est le compte des transactions courantes, qui réunit biens, "
    "services, revenus primaires et revenus secondaires ; le bas est le "
    "compte financier, qui enregistre les mouvements de capitaux."),
   ("La convention crédit-débit",
    "Une exportation est un crédit, c’est-à-dire un flux entrant de "
    "paiement ; une importation est un débit. Les dépenses d’un non-résident "
    "en France sont donc assimilées à des exportations de services."),
   ("La distinction avoirs et engagements",
    "Dans le compte financier, un avoir est un actif détenu par un résident "
    "sur le reste du monde, un engagement un actif domestique détenu par un "
    "non-résident : un investissement direct sortant augmente les avoirs, un "
    "investissement entrant les engagements."),
   ("La réponse entre le haut et le bas",
    "Un déficit courant crée un besoin de financement compensé par des "
    "entrées nettes de capitaux ; un excédent courant dégage une capacité de "
    "financement qui se traduit par des sorties nettes de capitaux.")],
  [{'a': "La notion fournit un cadre comptable exhaustif qui recense "
         "l’ensemble des relations économiques avec l’étranger.",
    'cond': "L’exhaustivité suppose la liste du cours : biens, services, "
            "revenus, transferts, investissements directs, placements "
            "financiers, prêts et emprunts.",
    'lim': "L’exhaustivité comptable n’est pas l’exhaustivité économique : le "
           "cours relève que le compte de capital reste quantitativement "
           "marginal et que certains flux sont difficiles à mesurer."},
   {'a': "Son équilibre comptable permet précisément de lire les "
         "déséquilibres dans les sous-comptes.",
    'cond': "L’argument suppose le principe de la partie double : toute "
            "transaction réelle ou financière possède une contrepartie.",
    'lim': "L’équilibre global peut induire en erreur : le cours insiste sur "
           "le fait que la balance toujours équilibrée ne signifie pas qu’il "
           "n’existe aucun déséquilibre."},
   {'a': "Elle relie le solde courant au financement de l’économie, ce qui "
         "en fait un instrument d’analyse macroéconomique.",
    'cond': "L’articulation suppose la relation du cours : déficit courant, "
            "donc besoin de financement, donc entrée nette de capitaux.",
    'lim': "La relation est comptable : elle dit qu’un déficit est financé, "
           "non qu’il est soutenable, ce qui exige d’examiner la position "
           "extérieure nette."},
   {'a': "Elle repose sur un critère de résidence, ce qui en fait un "
         "document d’économie territoriale et non de nationalité.",
    'cond': "Le critère suppose que l’on retienne le lieu principal "
            "d’activité économique, comme le cours l’indique.",
    'lim': "Ce critère brouille l’interprétation nationale : une filiale "
           "étrangère résidente contribue aux exportations françaises alors "
           "que ses profits reviennent à l’étranger."},
   {'a': "Elle permet une lecture par partenaire, ce qui éclaire les "
         "tensions commerciales bilatérales.",
    'cond': "L’argument suppose la disponibilité des soldes bilatéraux, que "
            "le cours fournit pour la Chine, l’Allemagne et les États-Unis.",
    'lim': "Le cours montre que le solde global masque des situations très "
           "différentes selon les partenaires, de sorte qu’un solde "
           "bilatéral n’a guère de signification isolée."}],
  [{'t': "Puisque la balance des paiements est toujours équilibrée, parler "
         "de déséquilibre extérieur n’a pas de sens.",
    'qui': "La confusion que le cours corrige dès son idée centrale.",
    'rep': "Le cours objecte que l’équilibre comptable global ne signifie "
           "pas qu’il n’existe aucun déséquilibre : il peut y avoir déficit "
           "ou excédent commercial, déficit ou excédent courant, entrées ou "
           "sorties nettes de capitaux, et ce sont ces sous-comptes qui "
           "révèlent les déséquilibres extérieurs."},
   {'t': "Le solde commercial et le solde courant mesurent la même chose, à quelques détails comptables près.",
    'qui': "La confusion que le cours dissipe explicitement.",
    'rep': "Le cours distingue : le solde commercial porte sur les biens au "
           "sens strict, ou sur les biens et services au sens élargi, tandis "
           "que le compte courant comprend en outre les revenus primaires et "
           "les revenus secondaires, ce qui peut renverser le signe du "
           "solde."},
   {'t': "La nationalité d’une entreprise détermine son inscription dans la "
         "balance des paiements.",
    'qui': "La lecture que le critère de résidence du cours écarte.",
    'rep': "Le cours précise que ce qui compte n’est pas forcément la "
           "nationalité mais le lieu principal d’activité économique : une "
           "entreprise étrangère implantée durablement en France peut être "
           "résidente française, un Français installé durablement ailleurs "
           "peut être non-résident."},
   {'t': "Un solde bilatéral négatif avec un partenaire révèle un échange "
         "déséquilibré ou injuste.",
    'qui': "Le discours politique que le cours rapporte avant de le "
           "relativiser.",
    'rep': "Le cours montre que les soldes bilatéraux français sont très "
           "différents selon les partenaires, un déficit de 36,7 milliards "
           "d’euros avec la Chine et de 10,9 avec l’Allemagne coexistant "
           "avec un excédent de 11,1 avec les États-Unis : le solde global "
           "masque donc des situations hétérogènes."}],
  [{'n': "Hélène Rey",
    'i': "Les déséquilibres mondiaux reflètent des stratégies de croissance "
         "elles-mêmes déséquilibrées.",
    'p': "Le cours en tire la lecture de fond de la balance des paiements : "
         "les déséquilibres extérieurs mondiaux ne sont pas de simples "
         "anomalies comptables, ils reflètent les faiblesses structurelles "
         "des modèles de croissance nationaux, aux États-Unis, en Chine, "
         "dans l’Union européenne et chez les pays exportateurs de pétrole."},
   {'n': "John Maynard Keynes",
    'i': "En économie ouverte, une partie du revenu supplémentaire créé par "
         "une relance fuit vers les importations.",
    'p': "Le cours en donne le mécanisme : dépense publique en hausse, "
         "revenus en hausse, consommation en hausse, mais une partie de "
         "cette consommation porte sur des importations, ce qui constitue "
         "une fuite hors du circuit économique national et dégrade le solde "
         "courant."},
   {'n': "Charles-Albert Michalet",
    'i': "Les États cherchent à séduire les firmes multinationales pour "
         "attirer leurs investissements.",
    'p': "Le cours relie cette logique au financement du déficit extérieur : "
         "pour attirer les investissements directs il faut des "
         "infrastructures de qualité, la stabilité politique, la sécurité "
         "juridique, une fiscalité attractive, un marché intéressant et une "
         "main-d’œuvre compétente."},
   {'n': "Oliver Williamson",
    'i': "La sécurité institutionnelle conditionne les décisions "
         "d’investissement de long terme.",
    'p': "Le cours mobilise cet apport dans l’analyse du financement du "
         "compte courant : les investisseurs de portefeuille recherchent un "
         "bon couple rendement et risque, et le pays doit donc proposer des "
         "actifs sûrs, des rendements intéressants et des taux d’intérêt "
         "suffisamment attractifs."}],
  [{'f': "En 2025, les exportations françaises de biens atteignent 624 "
         "milliards d’euros et les importations 682 milliards, soit un "
         "déficit commercial de biens de 58 milliards ; les services "
         "dégagent un excédent de 45 milliards, 380 de crédits contre 335 de "
         "débits.",
    'p': "Les chiffres montrent que le solde des biens et services est bien "
         "moins dégradé que celui des seuls biens, soit environ −13 "
         "milliards d’euros."},
   {'f': "Le solde français des revenus primaires s’élève à +51 milliards "
         "d’euros en 2025, le cours soulignant le rôle important des revenus "
         "du capital provenant des investissements français à l’étranger, "
         "tandis que les revenus secondaires sont de −50 milliards.",
    'p': "Les chiffres démontrent qu’un pays fortement investi à l’étranger "
         "reçoit d’importants revenus de patrimoine qui compensent une "
         "partie de son déficit de biens."},
   {'f': "Les soldes bilatéraux français de 2025 sont de −36,7 milliards "
         "d’euros avec la Chine, pour 38 milliards d’exportations et 74,7 "
         "milliards d’importations, de −10,9 milliards avec l’Allemagne et "
         "de +11,1 milliards avec les États-Unis.",
    'p': "Les chiffres montrent que le déficit global masque des situations "
         "très différentes selon les partenaires, ce qui limite la portée "
         "des raisonnements bilatéraux."},
   {'f': "Le compte financier français de 2025 fait apparaître une sortie "
         "nette de 31 milliards d’euros au titre des investissements "
         "directs, de 133 milliards au titre des investissements de "
         "portefeuille, et une entrée nette de 185 milliards au titre des "
         "autres investissements, pour un solde global de l’ordre de 8 "
         "milliards.",
    'p': "La lecture démontre que le compte financier est presque équilibré "
         "et que la composition des flux importe autant que leur solde."},
   {'f': "Un investissement direct correspond à un investissement "
         "transfrontalier permettant d’exercer une influence durable sur une "
         "entreprise étrangère, conventionnellement à partir de 10 % du "
         "capital ou des droits de vote.",
    'p': "Le seuil fonde la distinction entre logique productive et "
         "placement financier, qui structure la lecture du compte financier."},
   {'f': "Le déficit commercial des États-Unis est ancien, quasi continu "
         "depuis les années 1970 et très important, dépassant 1 200 "
         "milliards de dollars en 2025, soit environ 4 % du produit "
         "intérieur brut pour le compte courant.",
    'p': "Le fait montre que les déséquilibres extérieurs peuvent être "
         "durables, et qu’ils ne se résorbent pas spontanément."}],
  [{'q': "Sujet sur la lecture d’une balance des paiements",
    'f': "Le cours impose une méthode. La balance est toujours "
         "comptablement équilibrée en vertu de la partie double, puisque "
         "chaque opération possède une contrepartie, mais cela ne signifie "
         "pas qu’il n’existe aucun déséquilibre. Il faut donc distinguer le "
         "haut, le compte des transactions courantes avec biens, services, "
         "revenus primaires et revenus secondaires, et le bas, le compte "
         "financier avec investissements directs, investissements de "
         "portefeuille et autres investissements.",
    'r': "On montre que l’information se trouve dans les sous-comptes et "
         "non dans le solde global, ce qui impose de raisonner compte par "
         "compte.",
    'ex': "La France 2025 : −58 milliards d’euros sur les biens, +45 sur les "
          "services, +51 sur les revenus primaires, −50 sur les revenus "
          "secondaires."},
   {'q': "Sujet sur le financement du déficit extérieur d’une nation",
    'f': "Le cours établit la correspondance entre le haut et le bas de la "
         "balance. Un déficit courant signifie que le pays dépense davantage "
         "vis-à-vis du reste du monde qu’il ne reçoit : il est en besoin de "
         "financement, qui doit être compensé par des entrées nettes de "
         "capitaux. Un excédent courant signifie à l’inverse une capacité de "
         "financement, utilisable pour acheter des actifs étrangers, prêter "
         "au reste du monde ou réaliser des investissements directs "
         "sortants.",
    'r': "On montre que le solde courant détermine la position de la nation "
         "comme prêteuse ou emprunteuse, ce qui relie le commerce au "
         "financement.",
    'ex': "Le schéma du cours : déficit courant, besoin de financement, "
          "entrée nette de capitaux."},
   {'q': "Sujet sur les soldes bilatéraux et les tensions commerciales",
    'f': "Le cours met en garde contre le raisonnement bilatéral. Les soldes "
         "français de 2025 sont très contrastés : −36,7 milliards d’euros "
         "avec la Chine, −10,9 avec l’Allemagne, mais +11,1 avec les "
         "États-Unis. Il note l’intérêt politique de ces chiffres, puisque "
         "le déficit américain vis-à-vis de partenaires européens alimente "
         "le discours selon lequel les échanges seraient déséquilibrés ou "
         "injustes.",
    'r': "On montre que le solde global masque des situations très "
         "différentes selon les partenaires, ce qui prive le raisonnement "
         "bilatéral de portée analytique.",
    'ex': "Un déficit français marqué vis-à-vis de la Chine coexistant avec "
          "un excédent vis-à-vis des États-Unis."},
   {'q': "Sujet sur la mesure des relations économiques internationales",
    'f': "Le cours insiste sur le critère de résidence : ce qui compte n’est "
         "pas la nationalité mais le lieu principal d’activité économique, "
         "de sorte qu’une entreprise étrangère implantée durablement en "
         "France peut être résidente française et qu’un Français installé "
         "durablement ailleurs peut être non-résident. Il en tire également "
         "la logique des services : les dépenses d’un non-résident en France "
         "sont assimilées à des exportations.",
    'r': "On montre que la balance mesure un territoire et non une "
         "population, ce qui interdit de lire ses soldes comme un bilan de "
         "la réussite des entreprises nationales.",
    'ex': "Le touriste étranger dépensant en France, assimilé à une "
          "exportation de service."}],
  voisins=['n20-solde-courant', 'n20-balance-commerciale',
           'n20-capacite-besoin-financement', 'n20-position-exterieure-nette'])

d('n20-balance-commerciale', 20, "Balance commerciale",
  "Les biens seuls, ou les biens et services : deux soldes à ne pas confondre",
  "La balance commerciale enregistre les exportations et les importations de "
  "marchandises. Le cours en donne deux acceptions : au sens strict les "
  "biens uniquement, au sens élargi les biens et services. Il insiste sur le "
  "fait que le solde commercial ne doit pas être confondu avec le solde "
  "courant, lequel comprend en outre les revenus primaires et secondaires.",
  "Le cours traite la balance commerciale à l’intérieur du compte des "
  "transactions courantes, dont elle constitue la partie la plus intuitive. "
  "On y retrouve les exportations et les importations de marchandises, "
  "l’exportation étant inscrite en crédit, c’est-à-dire en flux entrant de "
  "paiement, et l’importation en débit. Les services suivent la même "
  "logique, avec le tourisme, le transport, les services financiers et les "
  "services aux entreprises : un touriste étranger qui dépense en France "
  "réalise l’équivalent d’une exportation de service, un Français qui "
  "dépense à l’étranger l’équivalent d’une importation. Le cours distingue "
  "alors deux acceptations du solde commercial : au sens strict les biens "
  "uniquement, au sens élargi les biens et services. L’exemple français de "
  "2025 montre l’enjeu de la distinction : les exportations de biens "
  "atteignent 624 milliards d’euros et les importations 682 milliards, soit "
  "un déficit commercial de biens de 58 milliards ; les services dégagent en "
  "revanche un excédent de 45 milliards, 380 de crédits contre 335 de "
  "débits, de sorte que le solde biens et services s’établit autour de −13 "
  "milliards d’euros. Mais le cours insiste surtout sur un point : le solde "
  "commercial n’est pas le solde courant, parce que le compte courant inclut "
  "encore les revenus primaires, revenus du travail et du capital, et les "
  "revenus secondaires, transferts sans contrepartie productive directe. En "
  "2025 la France présente ainsi un déficit courant limité, parce que "
  "l’excédent des services et l’excédent de revenus primaires de 51 "
  "milliards compensent une grande partie du déficit commercial de biens. "
  "Le cours analyse ensuite les causes d’un déficit commercial persistant : "
  "la délocalisation, selon l’enchaînement production domestique en baisse, "
  "biens réimportés en hausse, importations en hausse, déficit commercial en "
  "hausse ; la désindustrialisation, puisqu’un pays qui produit moins de "
  "biens industriels doit davantage importer pour satisfaire sa demande ; et "
  "la dépendance énergétique, un pays pouvant importer massivement pétrole, "
  "gaz, charbon ou électricité faute d’en produire assez. Le cours "
  "enregistre enfin des positions nationales durables : la Chine, "
  "l’Allemagne, le Japon et le Danemark exportent durablement beaucoup, "
  "tandis que le cas le plus emblématique de déficit est celui des "
  "États-Unis.",
  [("L’enregistrement des flux de marchandises",
    "La balance commerciale enregistre les exportations et les importations "
    "de marchandises, l’exportation étant un crédit, flux entrant de "
    "paiement, et l’importation un débit, flux sortant."),
   ("L’extension possible aux services",
    "Les services suivent la même logique, avec le tourisme, le transport, "
    "les services financiers et les services aux entreprises : le solde "
    "commercial au sens élargi additionne donc les biens et les services."),
   ("La distinction d’avec le solde courant",
    "Le compte courant comprend en outre les revenus primaires, revenus du "
    "travail et du capital, et les revenus secondaires, transferts sans "
    "contrepartie productive directe : le solde commercial n’en est qu’une "
    "composante."),
   ("Le canal de la délocalisation",
    "Le cours donne l’enchaînement : délocalisation, production domestique "
    "en baisse, biens réimportés en hausse, importations en hausse, déficit "
    "commercial en hausse. Le pays réimporte ce qu’il ne produit plus."),
   ("Le canal de la désindustrialisation",
    "Si un pays produit moins de biens industriels sur son territoire, il "
    "doit davantage importer pour satisfaire sa demande : "
    "désindustrialisation, offre domestique en baisse, importations en "
    "hausse."),
   ("Le canal de la dépendance énergétique",
    "Un pays peut importer massivement pétrole, gaz, charbon ou électricité "
    "faute d’en produire suffisamment : le déficit extérieur révèle alors "
    "une dépendance stratégique."),
   ("La persistance des positions nationales",
    "La Chine, l’Allemagne, le Japon et le Danemark exportent durablement "
    "beaucoup, tandis que le déficit commercial américain est ancien, quasi "
    "continu depuis les années 1970 et très important.")],
  [{'a': "La notion fournit un indicateur immédiatement lisible des "
         "échanges réels d’une économie avec l’extérieur.",
    'cond': "La lisibilité suppose la convention du cours : exportation "
            "égale crédit, importation égale débit, le solde étant la "
            "différence entre les deux.",
    'lim': "Le cours avertit que le solde commercial ne doit pas être "
           "confondu avec le solde courant, lequel comprend encore les "
           "revenus primaires et secondaires."},
   {'a': "Elle peut révéler des faiblesses structurelles de l’appareil "
         "productif, notamment une désindustrialisation.",
    'cond': "L’argument suppose l’enchaînement du cours : "
            "désindustrialisation, offre domestique en baisse, importations "
            "en hausse pour satisfaire la demande.",
    'lim': "Un déficit peut aussi provenir d’une demande intérieure "
           "dynamique ou d’un choc énergétique : le cours en énumère "
           "plusieurs causes distinctes."},
   {'a': "Elle révèle les dépendances stratégiques d’une économie, et notamment ses dépendances énergétiques.",
    'cond': "L’argument suppose l’exemple du cours : avant 2022, environ "
            "40 % des besoins gaziers européens étaient satisfaits par du "
            "gaz russe.",
    'lim': "Le déficit ne mesure pas la vulnérabilité : le cours rappelle "
           "ailleurs qu’une dépendance n’est stratégique que si le produit "
           "est essentiel et l’approvisionnement concentré."},
   {'a': "Sa décomposition entre biens et services nuance fortement le "
         "diagnostic d’une économie tertiarisée.",
    'cond': "L’argument suppose les chiffres français de 2025 : −58 "
            "milliards d’euros sur les biens, +45 milliards sur les "
            "services.",
    'lim': "La compensation est partielle : le solde biens et services reste "
           "négatif d’environ 13 milliards d’euros."},
   {'a': "Elle permet une lecture par partenaire, utile pour comprendre l’origine des tensions commerciales.",
    'cond': "L’argument suppose les soldes bilatéraux du cours, −36,7 "
            "milliards d’euros avec la Chine, +11,1 avec les États-Unis.",
    'lim': "Le cours souligne que le déficit global masque des situations "
           "très différentes selon les partenaires : un solde bilatéral "
           "isolé n’a guère de signification."}],
  [{'t': "Le déficit commercial mesure directement la perte de compétitivité d’une économie face à ses concurrents.",
    'qui': "La lecture que le cours nuance en énumérant les causes "
           "possibles.",
    'rep': "Le cours identifie plusieurs origines distinctes : la "
           "délocalisation, qui conduit à réimporter ce que l’on ne produit "
           "plus, la désindustrialisation, qui réduit l’offre domestique, et "
           "la dépendance énergétique, qui oblige à importer massivement "
           "pétrole, gaz, charbon ou électricité."},
   {'t': "Le solde commercial résume à lui seul l’état des échanges d’un pays avec le reste du monde.",
    'qui': "La confusion avec le solde courant que le cours dissipe.",
    'rep': "Le cours objecte que le compte courant comprend aussi les "
           "revenus primaires et secondaires : en 2025 la France présente un "
           "déficit courant limité précisément parce que ses excédents de "
           "services et de revenus primaires compensent en grande partie son "
           "déficit commercial de biens."},
   {'t': "Un pays tertiarisé n’a pas à se préoccuper de son déficit de "
         "biens, que ses services compensent.",
    'qui': "La lecture que les chiffres français relativisent.",
    'rep': "Le cours montre que la compensation n’est que partielle : "
           "l’excédent de services de 45 milliards d’euros ne couvre pas le "
           "déficit de biens de 58 milliards, le solde biens et services "
           "restant négatif d’environ 13 milliards."},
   {'t': "Les déséquilibres commerciaux sont temporaires et se corrigent par "
         "les mécanismes de marché.",
    'qui': "La lecture que la persistance des positions nationales "
           "contredit.",
    'rep': "Le cours observe que les déséquilibres extérieurs peuvent être "
           "durables : la Chine, l’Allemagne, le Japon et le Danemark "
           "exportent durablement beaucoup, tandis que le déficit américain "
           "est quasi continu depuis les années 1970 et dépasse 1 200 "
           "milliards de dollars en 2025."}],
  [{'n': "Hélène Rey",
    'i': "Les déséquilibres mondiaux reflètent des stratégies de croissance "
         "elles-mêmes déséquilibrées.",
    'p': "Le cours en tire que les soldes commerciaux durables ne sont pas "
         "des anomalies comptables mais l’expression de modèles de "
         "croissance : excès de demande intérieure et d’endettement aux "
         "États-Unis, surépargne et surcapacité en Chine, épargne élevée et "
         "sous-investissement en Allemagne."},
   {'n': "John Maynard Keynes",
    'i': "Les importations constituent une fuite hors du circuit économique "
         "national.",
    'p': "Le cours en donne le mécanisme : dépense publique en hausse, "
         "revenus en hausse, consommation en hausse, mais une partie porte "
         "sur des importations, de sorte qu’une propension à importer plus "
         "forte réduit le multiplicateur et dégrade le solde commercial."},
   {'n': "El Mouhoub Mouhoud",
    'i': "Une délocalisation détruit directement des emplois peu qualifiés "
         "mais engendre des effets indirects positifs.",
    'p': "Le cours relie cette analyse au solde commercial : la "
         "délocalisation réduit la production domestique et conduit à "
         "réimporter les biens destinés à la demande intérieure, mais elle "
         "produit aussi des effets de compensation par la compétitivité "
         "retrouvée et par la baisse des prix."},
   {'n': "Pierre Veltz",
    'i': "Industrie et services sont imbriqués dans une société "
         "hyper-industrielle.",
    'p': "Le cours en tire une mise en garde sur la lecture du solde : un "
         "excédent de services peut dépendre d’une base industrielle, "
         "puisque les services numériques reposent sur de lourdes "
         "infrastructures industrielles, de sorte que les deux soldes ne "
         "sont pas indépendants."}],
  [{'f': "En 2025, les exportations françaises de biens atteignent 624 "
         "milliards d’euros et les importations 682 milliards, soit un "
         "déficit commercial de biens de 58 milliards d’euros.",
    'p': "Le chiffre donne la mesure du déficit de marchandises et sert de "
         "point de départ à l’analyse du solde courant français."},
   {'f': "Les services français dégagent en 2025 un excédent de 45 milliards "
         "d’euros, avec 380 milliards de crédits contre 335 de débits, de "
         "sorte que le solde biens et services s’établit autour de −13 "
         "milliards.",
    'p': "Le chiffre démontre que le passage du sens strict au sens élargi "
         "change radicalement le diagnostic, sans toutefois le renverser."},
   {'f': "Les soldes bilatéraux français de 2025 : −36,7 milliards d’euros "
         "avec la Chine, pour 38 milliards d’exportations et 74,7 milliards "
         "d’importations, −10,9 milliards avec l’Allemagne, +11,1 milliards "
         "avec les États-Unis.",
    'p': "Les chiffres montrent que la Chine est l’un des principaux "
         "contributeurs au déficit commercial français, mais que le solde "
         "global masque des situations hétérogènes."},
   {'f': "Avant 2022, environ 40 % des besoins gaziers européens étaient "
         "satisfaits par du gaz russe, et après l’invasion de l’Ukraine "
         "l’Union européenne doit réduire sa dépendance, diversifier ses "
         "fournisseurs et développer de nouvelles infrastructures.",
    'p': "Le fait démontre qu’un déficit commercial peut révéler une "
         "dépendance énergétique qui devient un problème géopolitique et de "
         "sécurité."},
   {'f': "Les pays souvent excédentaires sont notamment la Chine, "
         "l’Allemagne, le Japon et le Danemark, tandis que le déficit "
         "commercial américain est ancien, quasi continu depuis les années "
         "1970 et dépasse 1 200 milliards de dollars en 2025.",
    'p': "Le fait démontre la persistance des positions nationales et "
         "interdit de traiter les déséquilibres comme des écarts "
         "transitoires."},
   {'f': "Un déficit commercial important accroît l’offre de monnaie "
         "nationale sur le marché des changes, puisque les résidents vendent "
         "leur monnaie pour acheter des devises afin de payer les "
         "importations, ce qui tend à déprécier cette monnaie.",
    'p': "Le fait relie le solde commercial au taux de change et ouvre "
         "l’analyse du cercle vicieux des monnaies faibles."}],
  [{'q': "Sujet sur l’interprétation d’un déficit commercial",
    'f': "Le cours refuse d’y voir un indicateur univoque. Un déficit "
         "persistant peut signaler une délocalisation, selon "
         "l’enchaînement production domestique en baisse, biens réimportés "
         "en hausse, importations en hausse ; une désindustrialisation, "
         "puisqu’un pays produisant moins de biens industriels doit "
         "davantage importer ; ou une dépendance énergétique, un pays "
         "pouvant importer massivement pétrole, gaz, charbon ou électricité "
         "faute d’en produire assez.",
    'r': "On montre que le même solde peut recouvrir des situations "
         "économiques très différentes, ce qui impose d’examiner la "
         "composition du déficit plutôt que son montant.",
    'ex': "Les 40 % des besoins gaziers européens satisfaits par du gaz "
          "russe avant 2022."},
   {'q': "Sujet sur la distinction entre solde commercial et solde courant",
    'f': "Le cours insiste sur une erreur fréquente. Le solde commercial "
         "porte, au sens strict, sur les biens, et au sens élargi sur les "
         "biens et services ; le compte courant comprend en outre les "
         "revenus primaires et les revenus secondaires. En 2025, la France "
         "présente ainsi un déficit courant limité précisément parce que "
         "l’excédent des services, 45 milliards d’euros, et celui des "
         "revenus primaires, 51 milliards, compensent une grande partie du "
         "déficit commercial de biens de 58 milliards.",
    'r': "On montre que le solde courant intègre le rendement du patrimoine "
         "extérieur, ce qui permet à une économie déficitaire en biens de "
         "rester proche de l’équilibre courant.",
    'ex': "Les revenus du capital provenant des investissements français à "
          "l’étranger."},
   {'q': "Sujet sur la persistance des déséquilibres commerciaux",
    'f': "Le cours montre que certains pays sont structurellement "
         "excédentaires et d’autres durablement déficitaires. La Chine, "
         "l’Allemagne, le Japon et le Danemark exportent durablement "
         "beaucoup. Le cas le plus emblématique de déficit est celui des "
         "États-Unis, dont le déficit commercial est ancien, quasi continu "
         "depuis les années 1970 et très important, dépassant 1 200 "
         "milliards de dollars en 2025, soit environ 4 % du produit "
         "intérieur brut pour le compte courant.",
    'r': "On montre que ces positions reflètent des modèles de croissance et "
         "non des écarts temporaires, ce qui explique l’échec des "
         "mécanismes spontanés de rééquilibrage.",
    'ex': "La lecture d’Hélène Rey : des déséquilibres mondiaux qui "
          "reflètent des stratégies de croissance déséquilibrées."},
   {'q': "Sujet sur le lien entre solde commercial et taux de change",
    'f': "Le cours décrit un mécanisme en chaîne. Toutes choses égales par "
         "ailleurs, un déficit commercial important accroît l’offre de "
         "monnaie nationale, puisque les résidents vendent leur monnaie pour "
         "acheter des devises afin de payer les importations, ce qui "
         "déprécie cette monnaie. La dépréciation renchérit alors les "
         "importations, ce qui peut aggraver le déficit : c’est le cercle "
         "vicieux des monnaies faibles.",
    'r': "On montre que le solde commercial et le taux de change se "
         "déterminent mutuellement, ce qui peut produire une dynamique "
         "cumulative plutôt qu’un rééquilibrage.",
    'ex': "Le cercle vicieux du cours : déficit extérieur, monnaie en "
          "baisse, importations plus chères, déficit en hausse."}],
  voisins=['n20-solde-courant', 'n20-balance-paiements',
           'n20-appreciation-depreciation', 'n19-desindustrialisation'])

d('n20-solde-courant', 20, "Solde courant",
  "Biens, services, revenus primaires et secondaires réunis",
  "Le solde courant est le solde du compte des transactions courantes, "
  "lequel comprend les biens, les services, les revenus primaires — revenus "
  "du travail et du capital — et les revenus secondaires, transferts sans "
  "contrepartie productive directe. Le cours en fait l’indicateur central "
  "du financement extérieur : un déficit courant traduit un besoin de "
  "financement, un excédent une capacité de financement.",
  "Le cours construit le solde courant par addition : en additionnant biens, "
  "services, revenus primaires et revenus secondaires, on obtient le solde "
  "du compte courant. Chaque composante a son contenu propre. Les biens et "
  "services suivent la logique crédit-débit, l’exportation étant un flux "
  "entrant de paiement. Les revenus primaires correspondent aux revenus "
  "directement liés à la participation à la production : revenus du travail, "
  "avec les travailleurs frontaliers et les expatriés, et revenus du "
  "capital, avec les dividendes, les intérêts et les revenus "
  "d’investissements directs ; un résident français détenant des actions "
  "américaines perçoit ainsi un revenu primaire entrant, tandis qu’un "
  "non-résident détenant une obligation française reçoit des intérêts "
  "payés vers l’étranger. Les revenus secondaires correspondent à des "
  "transferts sans contrepartie productive directe : aide publique au "
  "développement, transferts entre administrations publiques, certains "
  "transferts européens ; le solde français y est négatif, à −50 milliards "
  "d’euros en 2025, parce que la France, pays riche, verse davantage de "
  "transferts au reste du monde qu’elle n’en reçoit. Le cas français de "
  "2025 illustre l’intérêt analytique du solde courant : la France est en "
  "déficit courant, mais ce déficit reste relativement faible par rapport au "
  "déficit des seuls biens, parce que l’excédent des services, 45 milliards "
  "d’euros, et l’excédent des revenus primaires, 51 milliards, compensent "
  "une grande partie du déficit commercial de biens de 58 milliards. Le "
  "cours en tire la portée macroéconomique : le haut et le bas de la "
  "balance se répondent, un déficit courant signifiant que le pays dépense "
  "davantage vis-à-vis du reste du monde qu’il ne reçoit et qu’il est donc "
  "en besoin de financement, à combler par des capitaux étrangers, tandis "
  "qu’un excédent courant traduit une capacité de financement utilisable "
  "pour acheter des actifs étrangers, prêter au reste du monde ou réaliser "
  "des investissements directs sortants. Enfin, le solde courant se "
  "démontre à partir de l’équilibre emplois-ressources : de Y + M = C + I + "
  "G + X et Y = C + S + T on tire X − M = (S − I) + (T − G), le solde "
  "extérieur étant la somme du solde épargne-investissement privé et du "
  "solde budgétaire public.",
  [("L’addition des quatre composantes",
    "Le solde courant s’obtient en additionnant les biens, les services, les "
    "revenus primaires et les revenus secondaires : il est donc plus large "
    "que le solde commercial, même au sens élargi."),
   ("Le rôle des revenus primaires",
    "Les revenus primaires regroupent les revenus du travail, travailleurs "
    "frontaliers et expatriés, et les revenus du capital, dividendes, "
    "intérêts et revenus d’investissements directs : un pays fortement "
    "investi à l’étranger y dégage un excédent."),
   ("Le rôle des revenus secondaires",
    "Les revenus secondaires correspondent à des transferts sans "
    "contrepartie productive directe, comme l’aide publique au "
    "développement ou les transferts entre administrations : un pays riche y "
    "est généralement déficitaire."),
   ("La compensation possible entre composantes",
    "Un déficit de biens peut être largement compensé par un excédent de "
    "services et de revenus primaires : c’est le cas français en 2025, où le "
    "déficit courant reste limité malgré un déficit de biens de 58 milliards "
    "d’euros."),
   ("La traduction en besoin de financement",
    "Un déficit courant signifie que le pays dépense davantage vis-à-vis du "
    "reste du monde qu’il ne reçoit : il est en besoin de financement, qu’il "
    "doit combler par des capitaux étrangers, d’où une entrée nette de "
    "capitaux."),
   ("La traduction en capacité de financement",
    "Un excédent courant signifie que le pays dispose d’une épargne "
    "supérieure à ses besoins domestiques : il peut acheter des actifs "
    "étrangers, prêter au reste du monde ou réaliser des investissements "
    "directs sortants."),
   ("La décomposition par l’identité macroéconomique",
    "De l’équilibre emplois-ressources on tire X − M = (S − I) + (T − G) : "
    "le solde extérieur est la somme du solde épargne-investissement privé "
    "et du solde budgétaire public.")],
  [{'a': "La notion est plus complète que le solde commercial, puisqu’elle "
         "intègre le rendement du patrimoine extérieur.",
    'cond': "L’argument suppose la composition du cours : biens, services, "
            "revenus primaires et revenus secondaires.",
    'lim': "Cette complétude rend la lecture moins intuitive : un pays peut "
           "afficher un solde courant proche de l’équilibre tout en étant "
           "fortement déficitaire en biens."},
   {'a': "Elle se traduit directement en besoin ou en capacité de "
         "financement, ce qui en fait un indicateur macroéconomique et non "
         "seulement commercial.",
    'cond': "La traduction suppose la correspondance établie par le cours "
            "entre le haut et le bas de la balance des paiements.",
    'lim': "La relation est comptable : elle dit que le déficit est financé, "
           "non qu’il est soutenable, ce qui exige d’examiner la position "
           "extérieure nette."},
   {'a': "Elle se décompose rigoureusement en solde privé et solde public "
         "par l’identité macroéconomique.",
    'cond': "La décomposition suppose l’égalité X − M = (S − I) + (T − G), "
            "obtenue en combinant l’équilibre emplois-ressources et "
            "l’optique du revenu.",
    'lim': "L’identité est comptable et ne dit rien de la causalité : elle "
           "n’établit pas que le déficit public cause le déficit extérieur, "
           "seulement qu’ils s’additionnent."},
   {'a': "Elle permet de distinguer les origines d’un déficit, insuffisance "
         "d’épargne privée ou déficit public.",
    'cond': "La distinction suppose les deux cas du cours : si "
            "l’investissement dépasse l’épargne, ou si les dépenses "
            "publiques dépassent les recettes.",
    'lim': "Les deux composantes interagissent : le cours montre par les "
           "déficits jumeaux qu’un déficit public peut lui-même creuser le "
           "déficit courant par la demande intérieure."},
   {'a': "Elle éclaire le rôle du patrimoine extérieur dans la soutenabilité d’un déficit commercial de biens.",
    'cond': "L’argument suppose l’excédent français de revenus primaires, "
            "51 milliards d’euros en 2025, lié aux investissements français "
            "à l’étranger.",
    'lim': "Ce flux dépend du stock d’actifs détenus : il se tarit si la "
           "position extérieure nette se dégrade durablement."}],
  [{'t': "Un pays en déficit commercial se trouve nécessairement en déficit courant tout aussi marqué.",
    'qui': "La lecture que le cas français de 2025 contredit.",
    'rep': "Le cours montre que la France présente un déficit courant limité "
           "malgré un déficit commercial de biens de 58 milliards d’euros, "
           "parce que l’excédent des services, 45 milliards, et celui des "
           "revenus primaires, 51 milliards, en compensent une grande "
           "partie."},
   {'t': "Un déficit courant est toujours le signe d’un déficit public excessif, qu’il suffit de réduire.",
    'qui': "La lecture que l’identité macroéconomique du cours nuance.",
    'rep': "Le cours montre que X − M = (S − I) + (T − G) : un déficit "
           "extérieur peut provenir soit d’un investissement supérieur à "
           "l’épargne privée, soit d’un déficit public, ces deux composantes "
           "déterminant ensemble le besoin de financement de la nation."},
   {'t': "Un excédent courant constitue en soi une performance économique, que tout pays devrait rechercher.",
    'qui': "La lecture que la critique de l’excédent allemand remet en "
           "question.",
    'rep': "Le cours objecte que l’excédent courant allemand doit être "
           "nuancé, car il reflète en partie une épargne élevée associée à un "
           "investissement public et privé insuffisant, ce que l’Allemagne "
           "cherche désormais à corriger par un vaste plan d’investissement "
           "de l’ordre de 500 milliards d’euros."},
   {'t': "Puisqu’un déficit courant est toujours financé, il ne pose pas de "
         "problème économique.",
    'qui': "La lecture que le cours écarte en traitant la soutenabilité.",
    'rep': "Le cours objecte qu’un déficit courant n’est soutenable que si "
           "le pays parvient à attirer durablement les capitaux étrangers "
           "nécessaires, et que cette dépendance dégrade progressivement la "
           "position extérieure nette, le pays devenant davantage débiteur "
           "vis-à-vis du reste du monde."}],
  [{'n': "Hélène Rey",
    'i': "Les déséquilibres mondiaux reflètent des stratégies de croissance "
         "elles-mêmes déséquilibrées.",
    'p': "Le cours en tire la lecture des soldes courants durables : les "
         "déséquilibres extérieurs ne sont pas de simples anomalies "
         "comptables mais reflètent les faiblesses structurelles des modèles "
         "de croissance nationaux, aux États-Unis, en Chine, dans l’Union "
         "européenne et chez les pays exportateurs de pétrole."},
   {'n': "John Maynard Keynes",
    'i': "En économie ouverte, une partie du revenu créé par une relance "
         "fuit vers les importations.",
    'p': "Le cours en donne le mécanisme appliqué au solde courant : "
         "dépense publique en hausse, revenus en hausse, consommation en "
         "hausse, importations en hausse, solde extérieur en baisse ; une "
         "propension à importer plus forte réduit le multiplicateur et "
         "dégrade le compte courant."},
   {'n': "Charles-Albert Michalet",
    'i': "Les États cherchent à séduire les firmes multinationales pour "
         "attirer leurs investissements.",
    'p': "Le cours relie cette logique au financement du déficit courant : "
         "pour financer son déficit, un pays doit rester attractif, ce qui "
         "suppose des infrastructures de qualité, la stabilité politique, la "
         "sécurité juridique, une fiscalité attractive, un marché "
         "intéressant et une main-d’œuvre compétente."},
   {'n': "Oliver Williamson",
    'i': "Les décisions d’engagement de long terme dépendent de la sécurité "
         "institutionnelle offerte.",
    'p': "Le cours mobilise cet apport sur le financement du compte "
         "courant : les investisseurs de portefeuille recherchent un bon "
         "couple rendement et risque, de sorte que le pays doit proposer des "
         "actifs sûrs, des rendements intéressants et des taux d’intérêt "
         "suffisamment attractifs."}],
  [{'f': "En 2025, la France est en déficit courant, mais ce déficit reste "
         "relativement faible par rapport au déficit des seuls biens, de 58 "
         "milliards d’euros, grâce à l’excédent des services de 45 milliards "
         "et à l’excédent des revenus primaires de 51 milliards.",
    'p': "Le fait démontre l’intérêt analytique du solde courant : il "
         "intègre le rendement du patrimoine extérieur et des services, qui "
         "peuvent compenser un déficit de marchandises."},
   {'f': "Le solde français des revenus secondaires est de −50 milliards "
         "d’euros en 2025, la France versant davantage de transferts au "
         "reste du monde qu’elle n’en reçoit, du fait de son niveau de "
         "richesse.",
    'p': "Le fait montre que la position d’un pays riche pèse "
         "structurellement sur son solde courant par le canal des "
         "transferts."},
   {'f': "L’identité macroéconomique X − M = (S − I) + (T − G) s’obtient en "
         "combinant l’équilibre emplois-ressources Y + M = C + I + G + X et "
         "l’optique du revenu Y = C + S + T.",
    'p': "La démonstration montre que le solde extérieur est la somme du "
         "solde épargne-investissement privé et du solde budgétaire public, "
         "ce qui en fixe les deux origines possibles."},
   {'f': "Le déficit courant américain dépasse 1 200 milliards de dollars en "
         "2025, soit environ 4 % du produit intérieur brut, le déficit "
         "public étant de l’ordre de 6 % du produit intérieur brut depuis "
         "2022.",
    'p': "Les chiffres illustrent l’hypothèse des déficits jumeaux et "
         "montrent l’ampleur que peut atteindre un besoin de financement "
         "extérieur."},
   {'f': "L’excédent courant allemand reflète en partie une épargne élevée "
         "associée à un investissement public et privé insuffisant, et "
         "l’Allemagne évoque un vaste plan d’investissement de l’ordre de "
         "500 milliards d’euros pour réduire l’écart entre épargne et "
         "investissement.",
    'p': "Le fait démontre qu’un excédent courant n’est pas en soi une "
         "performance et peut signaler un sous-investissement domestique."},
   {'f': "Un déficit courant n’est soutenable que si le pays parvient à "
         "attirer durablement les capitaux étrangers nécessaires à son "
         "financement, cette dépendance dégradant progressivement la "
         "position extérieure nette.",
    'p': "Le fait relie le flux au stock et montre que la question du solde "
         "courant débouche sur celle de la soutenabilité."}],
  [{'q': "Sujet sur la signification d’un déficit courant",
    'f': "Le cours en donne la lecture macroéconomique. Un déficit courant "
         "signifie que le pays dépense davantage vis-à-vis du reste du monde "
         "qu’il ne reçoit : il est en besoin de financement, qu’il doit "
         "combler par des capitaux étrangers, selon l’enchaînement déficit "
         "courant, besoin de financement, entrée nette de capitaux. "
         "L’identité X − M = (S − I) + (T − G) en précise les deux origines "
         "possibles : un investissement supérieur à l’épargne privée, ou un "
         "déficit public.",
    'r': "On montre que le déficit extérieur est un problème de financement "
         "et non seulement de compétitivité, ce qui en déplace l’analyse vers "
         "l’épargne et le budget.",
    'ex': "Les déficits jumeaux américains : déficit public de l’ordre de "
          "6 % du produit intérieur brut et déficit courant d’environ 4 %."},
   {'q': "Sujet sur la composition du solde courant",
    'f': "Le cours décompose le compte courant en quatre postes. Les biens "
         "et services d’abord, selon la logique crédit-débit. Les revenus "
         "primaires ensuite, revenus du travail et revenus du capital, "
         "dividendes, intérêts et revenus d’investissements directs. Les "
         "revenus secondaires enfin, transferts sans contrepartie productive "
         "directe. En 2025 la France cumule −58 milliards d’euros sur les "
         "biens, +45 sur les services, +51 sur les revenus primaires et −50 "
         "sur les revenus secondaires.",
    'r': "On montre que le solde courant intègre le rendement du patrimoine "
         "extérieur, ce qui permet à une économie déficitaire en biens de "
         "rester proche de l’équilibre courant.",
    'ex': "Le résident français détenant des actions américaines, dont les "
          "dividendes constituent un revenu primaire entrant."},
   {'q': "Sujet demandant si un excédent courant est souhaitable",
    'f': "Le cours refuse d’y voir une performance en soi. L’excédent "
         "courant allemand doit être nuancé car il reflète en partie une "
         "épargne élevée associée à un investissement public et privé "
         "insuffisant. C’est précisément pour corriger ce sous-investissement "
         "que l’Allemagne cherche à assouplir ses contraintes budgétaires et "
         "évoque un vaste plan d’investissement de l’ordre de 500 milliards "
         "d’euros, ce qui réduirait l’écart entre épargne et investissement, "
         "et donc l’excédent.",
    'r': "On montre qu’un excédent peut signaler un défaut de demande "
         "intérieure plutôt qu’une réussite exportatrice, ce qui renverse "
         "l’interprétation spontanée.",
    'ex': "La lecture d’Hélène Rey : des déséquilibres qui reflètent des "
          "stratégies de croissance déséquilibrées."},
   {'q': "Sujet sur l’identité macroéconomique fondamentale",
    'f': "Le cours construit l’égalité pas à pas. L’équilibre "
         "emplois-ressources donne Y + M = C + I + G + X, donc Y = C + I + G "
         "+ X − M ; l’optique du revenu donne Y = C + S + T. En égalisant et "
         "en simplifiant la consommation, on obtient X − M = (S − I) + (T − "
         "G). Le solde extérieur correspond donc à la somme de la capacité "
         "de financement du secteur privé et du solde budgétaire public.",
    'r': "On montre que le déficit extérieur peut provenir d’un manque "
         "d’épargne privée autant que d’un déficit public, ce qui interdit "
         "d’imputer mécaniquement le déséquilibre à l’État.",
    'ex': "Le cas où l’investissement dépasse l’épargne : l’épargne "
          "nationale ne suffit pas et le pays doit obtenir de l’épargne "
          "étrangère."}],
  voisins=['n20-capacite-besoin-financement', 'n20-balance-commerciale',
           'n20-epargne-investissement-ouverte', 'n20-desequilibres-mondiaux'])

d('n20-position-exterieure-nette', 20, "Position extérieure nette",
  "Un stock, et non un flux : créancier ou débiteur net du reste du monde",
  "La position extérieure nette mesure, à une date donnée, la différence "
  "entre les actifs extérieurs détenus par les résidents et les engagements "
  "envers le reste du monde. Le cours l’oppose à la balance des paiements, "
  "qui mesure des flux sur une période : une position positive fait du pays "
  "un créancier net, une position négative un débiteur net.",
  "Le cours introduit la position extérieure nette par une distinction "
  "méthodologique essentielle : la balance des paiements mesure des flux sur "
  "une période, par exemple combien de capitaux sont entrés en 2025, tandis "
  "que la position extérieure nette mesure un stock à une date donnée, en "
  "comparant les actifs détenus par les résidents à l’étranger et les actifs "
  "nationaux détenus par les non-résidents. La formule est explicite : la "
  "position extérieure nette égale les actifs extérieurs détenus par les "
  "résidents moins les engagements envers le reste du monde. Son signe "
  "indique si le pays est créancier ou débiteur net. Si les avoirs "
  "extérieurs dépassent les engagements, la position est positive et le pays "
  "possède davantage d’actifs dans le reste du monde que les étrangers n’en "
  "possèdent chez lui : il est créancier net, le cours donnant l’exemple "
  "simplifié de résidents possédant 1 000 milliards à l’étranger et "
  "d’étrangers possédant 700 milliards dans le pays, soit une position de "
  "+300 milliards. La situation inverse caractérise un débiteur net. Le "
  "cours relie ensuite ce stock aux flux antérieurs. Les déficits courants "
  "répétés dégradent la position extérieure nette : un déficit courant crée "
  "un besoin de financement, donc des entrées nettes de capitaux, "
  "lesquelles correspondent souvent à une augmentation des engagements "
  "envers l’étranger, puisque les investisseurs étrangers achètent des "
  "obligations, des actions, investissent dans des entreprises ou accordent "
  "des prêts ; si la situation se répète, la position tend à devenir plus "
  "négative. Inversement, un pays en excédent courant dispose d’une "
  "capacité de financement qu’il peut employer à prêter à l’étranger, "
  "acheter des titres étrangers ou réaliser des investissements directs "
  "sortants, ce qui augmente ses avoirs extérieurs et tend à améliorer sa "
  "position. La France en offre l’illustration : en 2025 sa position "
  "extérieure nette est d’environ −30 % du produit intérieur brut, ce qui "
  "signifie qu’elle est débitrice nette vis-à-vis du reste du monde. Le "
  "cours prend soin de préciser que cela ne signifie pas que les Français "
  "n’investissent pas à l’étranger — ils investissent énormément — mais que "
  "leurs engagements sont supérieurs à leurs avoirs. Une position très "
  "négative peut devenir préoccupante car elle rend l’économie dépendante "
  "du maintien de la confiance des investisseurs étrangers : c’est "
  "pourquoi la procédure européenne de surveillance des déséquilibres "
  "macroéconomiques utilise un seuil d’alerte de −35 % du produit intérieur "
  "brut, sans qu’il s’agisse d’un seuil automatique d’insoutenabilité.",
  [("La mesure d’un stock à une date donnée",
    "Alors que la balance des paiements mesure des flux sur une période, la "
    "position extérieure nette mesure un stock : elle compare les actifs "
    "détenus par les résidents à l’étranger et les actifs nationaux détenus "
    "par les non-résidents."),
   ("La formule de calcul",
    "La position extérieure nette égale les actifs extérieurs détenus par "
    "les résidents moins les engagements envers le reste du monde : c’est "
    "donc un solde patrimonial et non un solde de transactions."),
   ("La lecture du signe",
    "Si les avoirs dépassent les engagements, le pays est créancier net du "
    "reste du monde ; dans le cas inverse, il est débiteur net, le stock "
    "d’actifs domestiques détenu par les non-résidents dépassant ses avoirs "
    "extérieurs."),
   ("La dégradation par les déficits répétés",
    "Le mécanisme est explicite : déficits courants répétés, entrées nettes "
    "de capitaux, engagements extérieurs en hausse, position extérieure "
    "nette en baisse. Le stock enregistre l’accumulation des flux."),
   ("L’amélioration par les excédents",
    "Un pays en excédent courant dispose d’une capacité de financement qu’il "
    "peut employer à prêter à l’étranger, acheter des titres étrangers ou "
    "réaliser des investissements directs sortants, ce qui augmente ses "
    "avoirs extérieurs."),
   ("La vulnérabilité attachée à une position négative",
    "Un pays qui finance durablement ses besoins grâce aux étrangers dépend "
    "de leur volonté de continuer à acheter sa dette, ses actions, à investir "
    "et à prêter : si la confiance baisse, les entrées de capitaux diminuent "
    "et le financement devient plus difficile."),
   ("La surveillance institutionnelle",
    "La procédure européenne de surveillance des déséquilibres "
    "macroéconomiques utilise une position inférieure à −35 % du produit "
    "intérieur brut comme signal d’alerte, sans qu’il s’agisse d’un seuil "
    "automatique d’insoutenabilité.")],
  [{'a': "La notion distingue rigoureusement le stock du flux, ce qui évite "
         "de confondre un déficit annuel et une situation patrimoniale.",
    'cond': "La distinction suppose la définition du cours : la balance des "
            "paiements mesure des flux sur une période, la position "
            "extérieure nette un stock à une date donnée.",
    'lim': "La valorisation du stock dépend des prix d’actifs et des taux de "
           "change, de sorte qu’il peut varier sans aucun flux nouveau."},
   {'a': "Elle enregistre l’accumulation des déséquilibres passés, ce qui en "
         "fait un indicateur de soutenabilité.",
    'cond': "L’argument suppose le mécanisme du cours : déficits courants "
            "répétés, entrées nettes de capitaux, engagements extérieurs en "
            "hausse, position en baisse.",
    'lim': "Le cours précise qu’une position négative n’est pas en soi "
           "insoutenable : le seuil européen est un signal d’alerte, pas un "
           "seuil automatique."},
   {'a': "Elle identifie précisément la nature de la vulnérabilité, la "
         "dépendance à la confiance des investisseurs étrangers.",
    'cond': "La vulnérabilité suppose le mécanisme du cours : dépendance aux "
            "capitaux étrangers, baisse de la confiance, baisse des entrées "
            "de capitaux, financement plus difficile.",
    'lim': "Cette dépendance dépend aussi de la monnaie d’endettement : le "
           "cours souligne ailleurs le danger particulier de la dette en "
           "devises."},
   {'a': "Elle est utilisée par un dispositif institutionnel européen, ce qui lui donne une portée pratique.",
    'cond': "L’argument suppose le seuil européen de −35 % du produit "
            "intérieur brut retenu dans la procédure de surveillance des "
            "déséquilibres macroéconomiques.",
    'lim': "Un seuil unique ne tient pas compte de la composition du stock : "
           "des engagements en investissements directs sont moins volatils "
           "que des placements de portefeuille."},
   {'a': "Elle évite une erreur d’interprétation en portant sur le solde et "
         "non sur le niveau des investissements.",
    'cond': "L’argument suppose la précision du cours : une position "
            "négative ne signifie pas que les résidents n’investissent pas à "
            "l’étranger, mais que leurs engagements dépassent leurs avoirs.",
    'lim': "Le solde masque alors des asymétries de rendement : un pays peut "
           "être débiteur net tout en percevant des revenus primaires nets "
           "positifs."}],
  [{'t': "Une position extérieure nette négative signifie que le pays "
         "n’investit pas à l’étranger.",
    'qui': "La lecture que le cours corrige explicitement à propos de la "
           "France.",
    'rep': "Le cours objecte que cela ne signifie pas que les Français "
           "n’investissent pas à l’étranger, puisqu’ils investissent "
           "énormément : la question porte sur le solde, les engagements "
           "étant simplement supérieurs aux avoirs."},
   {'t': "La balance des paiements et la position extérieure nette mesurent au fond la même réalité économique.",
    'qui': "La confusion que la distinction flux-stock du cours dissipe.",
    'rep': "Le cours distingue nettement : la balance des paiements mesure "
           "des flux sur une période, par exemple les capitaux entrés "
           "en 2025, tandis que la position extérieure nette mesure un stock "
           "d’actifs et d’engagements accumulés à une date donnée."},
   {'t': "Une position extérieure nette inférieure à −35 % du produit "
         "intérieur brut signale une situation insoutenable.",
    'qui': "La lecture que le cours corrige en qualifiant le seuil européen.",
    'rep': "Le cours précise que la procédure européenne de surveillance "
           "utilise ce niveau comme signal d’alerte, sans qu’il s’agisse "
           "pour autant d’un seuil automatique d’insoutenabilité : il "
           "déclenche un examen, non un diagnostic."},
   {'t': "Un pays débiteur net est nécessairement perdant dans ses "
         "relations financières avec le reste du monde.",
    'qui': "La lecture que les chiffres français du solde des revenus "
           "primaires nuancent.",
    'rep': "Le cours relève que la France, dont la position extérieure nette "
           "est d’environ −30 % du produit intérieur brut, dégage pourtant "
           "un solde de revenus primaires de +51 milliards d’euros en 2025, "
           "grâce aux revenus du capital provenant de ses investissements à "
           "l’étranger."}],
  [{'n': "Hélène Rey",
    'i': "Les déséquilibres mondiaux reflètent des stratégies de croissance "
         "elles-mêmes déséquilibrées.",
    'p': "Le cours en tire la lecture de la position extérieure nette : "
         "l’accumulation des engagements ou des avoirs enregistre dans un "
         "stock les faiblesses structurelles des modèles de croissance, aux "
         "États-Unis, en Chine, dans l’Union européenne et chez les pays "
         "exportateurs de pétrole."},
   {'n': "Charles-Albert Michalet",
    'i': "Les États cherchent à séduire les firmes multinationales pour "
         "attirer leurs investissements.",
    'p': "Le cours relie cette logique au financement d’une position "
         "négative : pour continuer à attirer les capitaux nécessaires, un "
         "pays doit rester attractif, ce qui suppose des infrastructures de "
         "qualité, la stabilité politique, la sécurité juridique, une "
         "fiscalité attractive et une main-d’œuvre compétente."},
   {'n': "Benjamin Lemoine",
    'i': "Certains acteurs financiers privés peuvent transformer la dette "
         "souveraine en terrain de chasse spéculatif.",
    'p': "Le cours situe Chasseurs d’États en 2024 et en tire l’emprise "
         "croissante de la finance sur les États : lorsque les engagements "
         "extérieurs d’un pays sont largement détenus par des créanciers "
         "privés, la dépendance au financement étranger devient un rapport "
         "de force."},
   {'n': "Oliver Williamson",
    'i': "La sécurité institutionnelle conditionne les engagements "
         "financiers de long terme.",
    'p': "Le cours mobilise cet apport sur le financement d’un besoin "
         "extérieur : les investisseurs de portefeuille recherchent un bon "
         "couple rendement et risque, de sorte que le pays doit proposer des "
         "actifs sûrs, des rendements intéressants et des taux d’intérêt "
         "suffisamment attractifs."}],
  [{'f': "La formule retenue par le cours est : position extérieure nette "
         "égale actifs extérieurs détenus par les résidents moins "
         "engagements envers le reste du monde.",
    'p': "La formule établit le caractère patrimonial de l’indicateur et le "
         "distingue de tout solde de transactions."},
   {'f': "L’exemple simplifié du cours : des résidents possédant 1 000 "
         "milliards à l’étranger face à des étrangers possédant 700 "
         "milliards dans le pays donnent une position extérieure nette de "
         "+300 milliards, le pays étant créancier net.",
    'p': "L’exemple montre comment lire le signe de l’indicateur et "
         "qualifier la position de la nation."},
   {'f': "En 2025, la France présente une position extérieure nette "
         "d’environ −30 % du produit intérieur brut, ce qui signifie qu’elle "
         "est débitrice nette vis-à-vis du reste du monde.",
    'p': "Le chiffre situe la France et montre la cohérence de cette "
         "position avec les déficits extérieurs observés régulièrement."},
   {'f': "La procédure européenne de surveillance des déséquilibres "
         "macroéconomiques utilise une position extérieure nette inférieure "
         "à −35 % du produit intérieur brut comme signal d’alerte.",
    'p': "Le fait montre que l’indicateur a une portée institutionnelle, "
         "tout en précisant qu’il ne s’agit pas d’un seuil automatique "
         "d’insoutenabilité."},
   {'f': "Le mécanisme de dégradation est explicite : déficits courants "
         "répétés, entrées nettes de capitaux, non-résidents détenant "
         "davantage d’actifs domestiques, engagements extérieurs en hausse, "
         "position extérieure nette en baisse.",
    'p': "Le fait relie le stock aux flux et montre que la position "
         "enregistre l’histoire des déséquilibres courants."},
   {'f': "Une part importante de la dette française est détenue par des "
         "non-résidents, ce qui illustre l’accumulation des engagements "
         "extérieurs liée aux déficits répétés.",
    'p': "Le fait rend concrète la dépendance au financement étranger et "
         "explique l’attention portée à la position extérieure nette."}],
  [{'q': "Sujet sur la soutenabilité d’un déficit extérieur",
    'f': "Le cours relie le flux au stock. Un déficit courant crée un besoin "
         "de financement comblé par des entrées nettes de capitaux, "
         "lesquelles augmentent les engagements envers l’étranger puisque "
         "les non-résidents achètent des obligations, des actions, "
         "investissent dans des entreprises ou accordent des prêts. Si la "
         "situation se répète, la position extérieure nette tend à devenir "
         "plus négative, et le pays devient davantage débiteur vis-à-vis du "
         "reste du monde.",
    'r': "On montre que la soutenabilité ne se juge pas sur le déficit annuel "
         "mais sur l’accumulation des engagements, ce qui déplace l’analyse "
         "du flux vers le stock.",
    'ex': "Le seuil européen d’alerte de −35 % du produit intérieur brut."},
   {'q': "Sujet sur la vulnérabilité d’une économie dépendante des capitaux "
         "étrangers",
    'f': "Le cours décrit le mécanisme de la fragilité. Un pays qui finance "
         "durablement ses besoins grâce aux étrangers dépend de leur volonté "
         "de continuer à acheter sa dette, ses actions, à investir dans ses "
         "entreprises et à lui accorder des prêts. Le risque apparaît si les "
         "investisseurs étrangers décident de réduire leurs "
         "investissements : dépendance aux capitaux étrangers, baisse de la "
         "confiance, baisse des entrées de capitaux, financement plus "
         "difficile.",
    'r': "On montre que la contrainte extérieure n’est pas seulement un "
         "problème de solde mais de confiance, ce qui rend la situation "
         "potentiellement discontinue.",
    'ex': "Une part importante de la dette française détenue par des "
          "non-résidents."},
   {'q': "Sujet sur la distinction entre flux et stock en économie "
         "internationale",
    'f': "Le cours en fait une distinction méthodologique centrale. La "
         "balance des paiements mesure des flux sur une période, par exemple "
         "les capitaux entrés en 2025 ; la position extérieure nette mesure "
         "un stock à une date donnée, en comparant les actifs détenus par "
         "les résidents à l’étranger et les actifs nationaux détenus par les "
         "non-résidents. Le signe du stock indique si le pays est créancier "
         "ou débiteur net.",
    'r': "On montre que les deux indicateurs répondent à des questions "
         "différentes, l’un sur l’année écoulée et l’autre sur le patrimoine "
         "accumulé, ce qui interdit de les substituer.",
    'ex': "L’exemple du cours : 1 000 milliards d’avoirs contre 700 "
          "milliards d’engagements, soit +300 milliards."},
   {'q': "Sujet sur le cas français",
    'f': "Le cours fournit un diagnostic nuancé. En 2025 la France présente "
         "une position extérieure nette d’environ −30 % du produit intérieur "
         "brut, cohérente avec les déficits extérieurs qu’elle connaît "
         "régulièrement. Mais cela ne signifie pas que les Français "
         "n’investissent pas à l’étranger : ils investissent énormément, et "
         "la question porte sur le solde, leurs engagements étant simplement "
         "supérieurs à leurs avoirs. La France dégage d’ailleurs un excédent "
         "de revenus primaires de 51 milliards d’euros.",
    'r': "On montre qu’une position négative traduit un solde patrimonial et "
         "non une absence d’investissement extérieur, ce qui évite un "
         "contresens courant.",
    'ex': "L’excédent français de revenus primaires, lié aux revenus du "
          "capital provenant des investissements à l’étranger."}],
  voisins=['n20-solde-courant', 'n20-capacite-besoin-financement',
           'n20-crise-change', 'n20-desequilibres-mondiaux'])
