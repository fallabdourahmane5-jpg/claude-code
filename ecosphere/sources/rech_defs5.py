# -*- coding: utf-8 -*-
"""Définitions rédigées pour les notions du chapitre 5 de deuxième année
(« L'équilibre macroéconomique : IS-LM, IS-LM-BP et OG-DG »).

Chaque entrée est rédigée à partir du passage du cours désigné par `anc`
(l'intitulé de la section) et n'ajoute rien qui ne s'y trouve. Aucune
attribution d'auteur n'est faite au-delà de ce que le chapitre établit.
"""

# (terme, chapitres, intitulé d'ancrage, définition, alias, distinction)
DEFS = [

 ("Modèle économique", ['25'],
  "Les modèles économiques : des représentations simplifiées du fonctionnement "
  "de l’économie",
  "Un modèle économique est une représentation simplifiée du fonctionnement de "
  "l’économie : il isole quelques variables jugées essentielles et les relie "
  "par des relations explicites, au prix d’une abstraction de la réalité. Sa "
  "valeur ne se juge donc pas à son réalisme descriptif mais à sa capacité à "
  "faire comprendre un mécanisme et à éclairer une décision de politique "
  "économique. Le chapitre insiste sur le rôle décisif des hypothèses : "
  "Harrod-Domar, en supposant les coefficients techniques fixes, obtient une "
  "croissance potentiellement déséquilibrée, tandis que Solow, en rendant les "
  "facteurs substituables, obtient une convergence vers un état stationnaire.",
  ["modelisation economique", "representation simplifiee de l economie"],
  "Un modèle n’est ni une prévision ni une description : changer une "
  "hypothèse change la conclusion, ce qui explique que deux modèles "
  "rigoureux puissent s’opposer."),

 ("Idéal-type", ['25'],
  "Le rapprochement avec les idéaux-types de Max Weber",
  "L’idéal-type est une construction intellectuelle qui accentue "
  "volontairement certains traits de la réalité pour en rendre la logique "
  "intelligible. Le chapitre s’en sert pour expliquer ce qu’est un modèle "
  "économique : comme l’idéal-type wébérien, le modèle n’est pas la réalité, "
  "il en propose une épure cohérente qui sert d’instrument de comparaison.",
  ["ideal type weberien", "construction ideale typique"],
  "L’idéal-type n’est pas une moyenne ni un cas réel : c’est un repère "
  "construit auquel on confronte les situations observées."),

 ("Demande effective", ['25'],
  "La demande effective détermine la production et l’emploi",
  "La demande effective est la demande que les entrepreneurs anticipent et sur "
  "laquelle ils règlent leur décision de produire et d’embaucher. Dans "
  "l’analyse keynésienne, c’est elle, et non le prix ou le salaire réel, qui "
  "détermine le niveau de la production et de l’emploi : l’ajustement "
  "s’effectue principalement par les quantités. Il en résulte que le "
  "plein-emploi n’est pas garanti, puisque rien n’assure que la demande "
  "anticipée corresponde au niveau d’activité de plein-emploi.",
  ["demande anticipee par les entrepreneurs", "demande globale anticipee"],
  "À distinguer de la demande observée : la demande effective est "
  "l’anticipation qui précède la production."),

 ("Équilibre de sous-emploi", ['25'],
  "Keynes montre qu’un équilibre de sous-emploi peut exister",
  "Un équilibre de sous-emploi est une situation dans laquelle l’économie est "
  "durablement stabilisée à un niveau de production inférieur au plein-emploi : "
  "les marchés sont équilibrés au sens où la production égale la demande, mais "
  "une partie de la main-d’œuvre reste sans emploi. Cet équilibre s’explique "
  "par une insuffisance de la demande globale et non par un salaire réel trop "
  "élevé ; il se maintient parce que les anticipations pessimistes des "
  "entreprises entretiennent un cercle vicieux. C’est ce qui justifie, chez "
  "Keynes, l’intervention publique pour déplacer l’économie vers un niveau "
  "d’activité plus élevé.",
  ["equilibre de sous emploi keynesien", "chomage d equilibre keynesien"],
  "À distinguer du chômage néoclassique, qui résulte d’un déséquilibre sur le "
  "marché du travail imputé à un salaire réel trop élevé."),

 ("Écart inflationniste", ['25'],
  "Le second dysfonctionnement correspond à un écart inflationniste",
  "L’écart inflationniste est la situation inverse du sous-emploi : la demande "
  "globale excède les capacités de production de l’économie. Les quantités ne "
  "pouvant plus s’ajuster, l’excès de demande se reporte sur les prix et "
  "alimente une surchauffe, éventuellement accompagnée d’une dégradation du "
  "solde extérieur lorsque le surcroît de demande se porte sur les "
  "importations.",
  ["surchauffe", "exces de demande globale"],
  "Symétrique de l’écart déflationniste : dans un cas la demande manque, dans "
  "l’autre elle excède le potentiel."),

 ("Écart de production", ['25'],
  "Okun (1962) : l’écart de production permet d’identifier le sous-emploi et "
  "la surchauffe",
  "L’écart de production mesure la distance entre la production effective et "
  "la production potentielle, c’est-à-dire le niveau d’activité soutenable "
  "compte tenu des capacités de l’économie. Un écart négatif signale un "
  "sous-emploi des facteurs et appelle un soutien de la demande ; un écart "
  "positif signale une surchauffe et appelle un freinage. C’est l’indicateur "
  "qui permet de rattacher un diagnostic conjoncturel au choix d’une politique "
  "économique.",
  ["output gap", "ecart de production potentiel"],
  "À distinguer du taux de croissance : l’écart de production situe le niveau "
  "de l’activité par rapport au potentiel, non sa variation."),

 ("Loi d’Okun", ['25'],
  "Okun met en évidence le lien entre activité économique et chômage",
  "La loi d’Okun énonce une relation empirique entre l’activité économique et "
  "le chômage : le chômage ne recule que si la croissance dépasse un certain "
  "seuil, parce qu’une partie de la reprise est absorbée par des gains de "
  "productivité et par la reprise des heures travaillées avant toute "
  "embauche. Elle justifie l’usage de l’écart de production comme indicateur "
  "de sous-emploi ou de surchauffe.",
  ["loi d okun", "relation croissance chomage", "okun 1962"],
  "Relation empirique et non loi mécanique : le seuil varie selon les pays et "
  "les périodes."),

 ("Propension marginale à consommer", ['25'],
  "La propension marginale à consommer c",
  "La propension marginale à consommer est la part d’un revenu supplémentaire "
  "qui est consommée : elle est comprise entre 0 et 1, le reste étant épargné. "
  "Elle gouverne la pente de la fonction de consommation keynésienne, qui "
  "ajoute à la consommation autonome une consommation proportionnelle au "
  "revenu, et elle commande la valeur du multiplicateur : plus elle est "
  "élevée, plus une impulsion initiale se diffuse dans le circuit.",
  ["pmc", "part du revenu supplementaire consommee"],
  "À distinguer de la propension moyenne à consommer, qui rapporte la "
  "consommation totale au revenu total, et de la propension marginale à "
  "épargner, son complément à 1."),

 ("Loi psychologique fondamentale", ['25'],
  "La loi psychologique fondamentale de Keynes",
  "La loi psychologique fondamentale énoncée par Keynes affirme que lorsque le "
  "revenu augmente, la consommation augmente, mais moins que le revenu : une "
  "part croissante du supplément est épargnée. Elle fonde la fonction de "
  "consommation keynésienne et explique qu’une économie laissée à elle-même "
  "puisse souffrir d’une demande insuffisante, l’épargne constituant une fuite "
  "du circuit.",
  ["loi psychologique fondamentale de keynes"],
  "Porte sur la consommation marginale, non sur un comportement individuel "
  "d’avarice : c’est une régularité d’ensemble."),

 ("Multiplicateur d’investissement", ['25'],
  "Kahn (1931) et Keynes (1936) : le principe du multiplicateur",
  "Le multiplicateur d’investissement est le rapport entre la variation du "
  "revenu national et la variation initiale de l’investissement qui l’a "
  "déclenchée. Formulé par Kahn en 1931 puis intégré par Keynes dans la "
  "Théorie générale en 1936, il repose sur un enchaînement de vagues de "
  "dépense : le revenu distribué est pour partie consommé, ce qui engendre un "
  "nouveau revenu, et ainsi de suite. Sa valeur est l’inverse de la propension "
  "marginale à épargner : avec une propension à consommer de 0,8, le "
  "multiplicateur vaut 5. Son corollaire inverse la logique classique : au "
  "terme du processus, l’épargne supplémentaire égale exactement "
  "l’investissement initial, donc c’est l’investissement qui engendre son "
  "épargne.",
  ["multiplicateur keynesien", "principe du multiplicateur", "kahn 1931"],
  "À distinguer de l’accélérateur, et du multiplicateur budgétaire, qui "
  "s’applique à une dépense publique et non à un investissement privé."),

 ("Multiplicateur de dépenses publiques", ['25'],
  "Le multiplicateur de dépenses publiques",
  "Le multiplicateur de dépenses publiques mesure l’effet sur le revenu "
  "national d’une hausse des dépenses publiques directes. Comme la totalité de "
  "la dépense entre immédiatement dans le circuit, il est égal à l’inverse de "
  "la propension marginale à épargner et constitue le plus puissant des trois "
  "leviers budgétaires : avec une propension à consommer de 0,8, il vaut 5, "
  "contre 4 pour les prestations sociales et − 4 pour une baisse d’impôt.",
  ["multiplicateur budgetaire", "kg"],
  "Supérieur au multiplicateur fiscal et à celui des prestations, parce que "
  "ces derniers ne se diffusent qu’à travers la consommation des ménages."),

 ("Multiplicateur fiscal", ['25'],
  "Le multiplicateur fiscal",
  "Le multiplicateur fiscal mesure l’effet sur le revenu national d’une "
  "variation des prélèvements. Il est négatif — une hausse d’impôt réduit le "
  "revenu — et plus faible en valeur absolue que le multiplicateur de dépenses "
  "publiques, parce qu’une baisse d’impôt n’est dépensée qu’à hauteur de la "
  "propension marginale à consommer : une part en est épargnée dès la première "
  "vague. Avec une propension à consommer de 0,8, il vaut − 4 contre 5 pour "
  "les dépenses directes.",
  ["kt", "multiplicateur des prelevements", "multiplicateur d impot"],
  "À distinguer du multiplicateur des prestations sociales, positif, qui vaut "
  "4 dans le même exemple."),

 ("Propension marginale à importer", ['25'],
  "Les importations dépendent positivement du revenu national",
  "La propension marginale à importer est la part d’un revenu supplémentaire "
  "qui se porte sur des biens et services étrangers. Elle introduit une "
  "seconde fuite dans le circuit, à côté de l’épargne, et réduit donc la "
  "valeur du multiplicateur : dans l’exemple du chapitre, l’ouverture fait "
  "passer le multiplicateur de 5 à 2. C’est le fondement de la contrainte "
  "extérieure pesant sur une relance menée seule, et l’un des arguments "
  "protectionnistes que le chapitre examine.",
  ["pmi", "propension a importer", "fuite par les importations"],
  "À ne pas confondre avec le taux d’ouverture : la propension marginale "
  "porte sur le supplément de revenu, non sur le niveau des échanges."),

 ("Courbe IS", ['25'],
  "La courbe IS : l’équilibre sur le marché des biens et services",
  "La courbe IS est l’ensemble des couples revenu-taux d’intérêt pour lesquels "
  "le marché des biens et services est équilibré, c’est-à-dire pour lesquels "
  "l’investissement égale l’épargne. Elle est décroissante : une baisse du "
  "taux d’intérêt rend des projets d’investissement rentables, la demande "
  "augmente et le revenu d’équilibre s’élève. Toute politique budgétaire la "
  "déplace — vers la droite pour une relance, vers la gauche pour une rigueur.",
  ["is", "equilibre du marche des biens et services"],
  "Chaque point de IS n’est qu’un équilibre partiel : l’équilibre "
  "macroéconomique exige la rencontre de IS et de LM."),

 ("Courbe LM", ['25'],
  "La courbe LM : l’équilibre sur le marché de la monnaie",
  "La courbe LM est l’ensemble des couples revenu-taux d’intérêt pour lesquels "
  "le marché de la monnaie est équilibré, l’offre de monnaie étant supposée "
  "exogène. Elle est croissante : une hausse du revenu accroît la demande de "
  "monnaie pour motifs de transaction et de précaution, et le taux d’intérêt "
  "doit s’élever pour rétablir l’équilibre. Le chapitre en distingue trois "
  "phases : horizontale dans la trappe à liquidité, croissante en régime "
  "normal, verticale dans la zone classique où toute la monnaie est absorbée "
  "par les transactions. Une politique monétaire expansionniste la déplace "
  "vers la droite.",
  ["lm", "equilibre du marche de la monnaie"],
  "La pente de LM commande l’efficacité comparée des politiques budgétaire et "
  "monétaire."),

 ("Trappe à liquidité", ['25'],
  "La trappe à liquidité constitue un cas extrême de préférence pour la monnaie",
  "La trappe à liquidité est la situation dans laquelle le taux d’intérêt est "
  "si bas que les agents préfèrent conserver la monnaie plutôt que d’acheter "
  "des obligations dont ils anticipent la baisse de prix. La demande de "
  "monnaie devient alors insensible au taux d’intérêt, la courbe LM est "
  "horizontale et toute création monétaire supplémentaire est absorbée sans "
  "faire reculer les taux : la politique monétaire conventionnelle perd son "
  "efficacité, ce qui redonne un rôle décisif à la politique budgétaire. Le "
  "chapitre y voit la raison de la réhabilitation du modèle IS-LM après la "
  "crise de 2008.",
  ["preference absolue pour la liquidite", "lm horizontale"],
  "Opposée à la zone classique, où LM est verticale et où la politique "
  "monétaire est au contraire la plus efficace."),

 ("Motifs de la demande de monnaie", ['25'],
  "La demande de monnaie repose sur trois motifs",
  "Chez Keynes, la monnaie n’est pas seulement demandée pour effectuer des "
  "transactions : elle est un actif recherché pour sa liquidité. La demande de "
  "monnaie répond à trois motifs — le motif de transaction, pour financer les "
  "échanges courants, le motif de précaution, pour faire face à l’incertitude, "
  "et le motif de spéculation, qui conduit à arbitrer entre monnaie et titres "
  "selon le niveau du taux d’intérêt. Les deux premiers dépendent du revenu, "
  "le troisième du taux d’intérêt : c’est cette composition qui donne à la "
  "courbe LM sa forme.",
  ["demande de monnaie keynesienne", "preference pour la liquidite",
   "motif de transaction", "motif de precaution", "motif de speculation"],
  "S’oppose à l’analyse classique, où la monnaie n’est demandée que pour les "
  "transactions et reste neutre."),

 ("Effet d’éviction", ['25'],
  "L’effet d’éviction limite l’efficacité de la relance budgétaire",
  "L’effet d’éviction désigne la réduction de l’investissement privé provoquée "
  "par une relance budgétaire : la hausse de l’activité accroît la demande de "
  "monnaie, le taux d’intérêt s’élève et une partie des projets privés "
  "devient non rentable. L’effet obtenu est donc inférieur à l’effet "
  "théorique du multiplicateur. Son ampleur dépend de la pente des courbes IS "
  "et LM, et une politique monétaire accommodante peut le limiter en "
  "déplaçant LM vers la droite.",
  ["eviction de l investissement prive", "crowding out"],
  "À distinguer des deux autres critiques de la relance : le revenu permanent "
  "et l’équivalence ricardienne portent sur le comportement des ménages, non "
  "sur le taux d’intérêt."),

 ("Policy mix", ['25'],
  "Le policy mix correspond à la combinaison des politiques budgétaire et "
  "monétaire",
  "Le policy mix est la combinaison des politiques budgétaire et monétaire, "
  "dont les effets se lisent dans le modèle IS-LM comme deux déplacements "
  "simultanés de courbes. Il permet d’atteindre des objectifs que chaque "
  "instrument isolé n’atteindrait pas : le policy mix Clinton-Greenspan associe "
  "ainsi une consolidation budgétaire à une détente monétaire, ramenant le "
  "solde fédéral de − 4,5 % du PIB en 1992 à + 0,8 % en 1998 sans récession. "
  "Le policy mix allemand de la réunification illustre la combinaison inverse, "
  "impulsion budgétaire et rigueur monétaire, avec des taux courts portés de "
  "4,3 % en 1988 à 9,2 % en 1991.",
  ["combinaison des politiques budgetaire et monetaire",
   "clinton greenspan"],
  "Dans la zone euro, le policy mix est institutionnellement particulier : la "
  "politique monétaire est commune, les politiques budgétaires restent "
  "nationales."),

 ("Courbe BP", ['25'],
  "La courbe BP représente les conditions de l’équilibre extérieur",
  "La courbe BP est l’ensemble des couples revenu-taux d’intérêt pour lesquels "
  "l’équilibre extérieur est assuré, c’est-à-dire pour lesquels la balance "
  "globale est équilibrée. Elle est croissante : une hausse du revenu dégrade "
  "le solde courant par les importations, et il faut un taux d’intérêt plus "
  "élevé pour attirer les capitaux qui compensent ce déficit. Sa pente dépend "
  "de la mobilité internationale des capitaux : plus les capitaux sont "
  "mobiles, plus BP est plate, jusqu’à devenir horizontale en mobilité "
  "parfaite.",
  ["bp", "equilibre exterieur", "courbe d equilibre de la balance des paiements"],
  "L’équilibre comptable de la balance des paiements est toujours vérifié : "
  "BP porte sur la balance globale, hors mouvements de financement de la "
  "banque centrale."),

 ("Modèle IS-LM-BP", ['25'],
  "Fleming et Mundell complètent IS-LM par une courbe d’équilibre extérieur",
  "Le modèle IS-LM-BP, dit modèle Mundell-Fleming, prolonge IS-LM en économie "
  "ouverte en ajoutant la courbe BP de l’équilibre extérieur : l’équilibre "
  "macroéconomique devient un triple équilibre, à l’intersection de IS, LM et "
  "BP. Il montre que l’efficacité des politiques conjoncturelles dépend du "
  "régime de change et de la mobilité des capitaux : en changes fixes et "
  "mobilité parfaite, la politique monétaire est neutralisée par la défense de "
  "la parité tandis que la politique budgétaire est efficace ; en changes "
  "flexibles, la conclusion s’inverse, l’ajustement du change amplifiant la "
  "politique monétaire et neutralisant la relance budgétaire. Le chapitre "
  "rattache ces travaux à Fleming en 1962 et à Mundell en 1963.",
  ["mundell fleming", "is lm bp", "modele de mundell fleming"],
  "Le chapitre distingue trois modèles complémentaires : IS-LM pour "
  "l’économie fermée, OG-DG pour les prix, IS-LM-BP pour l’économie ouverte."),

 ("Triangle des incompatibilités de Mundell", ['25', '26'],
  "Le triangle des incompatibilités de Mundell montre les limites de "
  "l’autonomie monétaire",
  "Le triangle des incompatibilités de Mundell énonce que trois objectifs "
  "souhaitables — la libre circulation des capitaux, l’autonomie de la "
  "politique monétaire et la stabilité des taux de change — ne peuvent pas "
  "être poursuivis simultanément : il faut en abandonner un. Il fournit une "
  "grille de lecture de l’histoire monétaire : Bretton Woods de 1944 à 1971 "
  "renonce à la mobilité des capitaux, le flottement postérieur à 1971 renonce "
  "à la stabilité du change, le SME puis l’euro renoncent à l’autonomie "
  "monétaire nationale.",
  ["triangle de mundell", "triangle d incompatibilite",
   "triangle des incompatibilites"],
  "À distinguer de la règle de Mundell, qui porte sur l’affectation des "
  "instruments et non sur l’incompatibilité des objectifs."),

 ("Règle de Mundell", ['25'],
  "La règle de Mundell repose sur le principe d’affectation des instruments",
  "La règle de Mundell, ou principe d’affectation, recommande d’affecter "
  "chaque instrument à l’objectif sur lequel il agit le plus efficacement : la "
  "politique budgétaire à l’équilibre interne, la politique monétaire à "
  "l’équilibre externe, le taux d’intérêt commandant les mouvements de "
  "capitaux. Elle permet de définir quatre combinaisons de politiques selon la "
  "situation du pays, et de sortir des dilemmes dans lesquels un seul "
  "instrument ne peut satisfaire deux objectifs opposés. Son application à la "
  "zone euro rencontre des limites institutionnelles, les deux instruments "
  "n’étant pas exercés au même niveau.",
  ["principe d affectation des instruments", "regle d affectation"],
  "Ne supprime pas la contrainte extérieure : elle organise l’usage des "
  "instruments disponibles."),

 ("Contrainte extérieure", ['25'],
  "La contrainte extérieure limite l’autonomie des politiques économiques",
  "La contrainte extérieure est la limite que l’équilibre des échanges et des "
  "paiements impose aux politiques économiques nationales : une relance accroît "
  "les importations, dégrade le solde courant et peut provoquer une crise de "
  "change, obligeant les autorités à renoncer. La relance française de 1981 en "
  "fournit l’illustration : une partie de l’impulsion fuit vers les "
  "importations, le Système monétaire européen transforme le déficit extérieur "
  "en crise de change, et le tournant de la rigueur de 1983 manifeste la "
  "priorité accordée à l’équilibre extérieur.",
  ["contrainte exterieure sur les politiques economiques",
   "contrainte de balance des paiements"],
  "Les changes flexibles atténuent les dilemmes sans les supprimer, comme "
  "l’illustre le cas japonais."),

 ("Modèle OG-DG", ['25'],
  "Un modèle d’équilibre entre offre globale et demande globale",
  "Le modèle OG-DG représente l’équilibre macroéconomique par la rencontre "
  "d’une offre globale et d’une demande globale dans un plan production-prix. "
  "Il complète IS-LM, qui raisonne à prix fixes, en permettant d’analyser les "
  "effets d’un choc sur la production et sur le niveau des prix. Il rend ainsi "
  "intelligible la stagflation, qu’un choc d’offre négatif explique par une "
  "hausse des prix accompagnée d’une baisse de la production, et il ouvre sur "
  "les politiques d’offre et la réflexion sur la croissance potentielle.",
  ["og dg", "offre globale demande globale"],
  "Complémentaire d’IS-LM et non concurrent : l’un raisonne à prix fixes, "
  "l’autre réintroduit les prix."),

 ("Choc d’offre", ['25'],
  "Un choc d’offre négatif provoque une hausse des prix et une baisse de la "
  "production",
  "Un choc d’offre est une variation des conditions de production — coût des "
  "matières premières, fiscalité, réglementation, productivité — qui déplace "
  "la courbe d’offre globale. Un choc négatif renchérit la production : les "
  "prix montent et l’activité recule simultanément, configuration qu’une "
  "politique de demande ne peut corriger sans aggraver l’un des deux maux. "
  "C’est la lecture que le modèle OG-DG donne des chocs pétroliers et de la "
  "stagflation des années 1970.",
  ["choc d offre negatif", "choc petrolier et offre globale"],
  "À distinguer d’un choc de demande, qui déplace production et prix dans le "
  "même sens."),

 ("Stagflation", ['25'],
  "La stagflation : la coexistence de l’inflation et de la stagnation",
  "La stagflation est la coexistence d’une inflation élevée et d’une "
  "stagnation de l’activité accompagnée de chômage. Elle contredit l’arbitrage "
  "inflation-chômage que la courbe de Phillips semblait établir et révèle les "
  "limites de l’analyse keynésienne traditionnelle, puisqu’aucune politique de "
  "demande ne permet d’agir sur les deux maux à la fois. En 1975, la "
  "croissance est négative en France, en Allemagne et aux États-Unis "
  "— respectivement − 1,0 %, − 0,9 % et − 0,2 % — alors que l’inflation "
  "atteint 11,7 %, 5,9 % et 9,1 %.",
  ["stagflation des annees 1970", "inflation et stagnation"],
  "Ni simple inflation ni simple récession : c’est leur simultanéité qui fait "
  "la difficulté théorique."),

 ("Courbe de Phillips", ['25'],
  "Phillips (1958) : une relation inverse entre chômage et progression des "
  "salaires",
  "La courbe de Phillips est la relation inverse, mise en évidence en 1958, "
  "entre le taux de chômage et le rythme de progression des salaires "
  "nominaux : plus le chômage est faible, plus les salaires augmentent "
  "rapidement. Lipsey, Samuelson et Solow l’ont reformulée en arbitrage entre "
  "inflation et chômage, ce qui en faisait un instrument de politique "
  "économique. La stagflation des années 1970 a démenti cet arbitrage, et "
  "Friedman en a proposé la critique monétariste.",
  ["relation inverse inflation chomage", "arbitrage inflation chomage",
   "phillips 1958"],
  "La relation originelle porte sur les salaires nominaux ; la version en "
  "termes d’inflation est une reformulation ultérieure."),

 ("Taux de chômage naturel", ['25'],
  "Le taux de chômage naturel correspond à des caractéristiques structurelles "
  "de l’économie",
  "Le taux de chômage naturel est le niveau de chômage qui résulte des "
  "caractéristiques structurelles de l’économie — fonctionnement du marché du "
  "travail, qualifications, mobilité, institutions. Dans l’analyse de "
  "Friedman, une relance monétaire peut en écarter temporairement l’économie, "
  "mais l’inflation finit par modifier les anticipations et le chômage revient "
  "à son niveau naturel : les politiques de demande ne peuvent donc pas le "
  "réduire durablement, seules des politiques structurelles le peuvent.",
  ["chomage naturel", "taux de chomage structurel"],
  "À distinguer du chômage conjoncturel, que les politiques de demande "
  "peuvent effectivement réduire."),

 ("Revenu permanent", ['25'],
  "Friedman considère que la consommation dépend surtout du revenu permanent",
  "Le revenu permanent est le revenu que l’agent anticipe sur l’ensemble de "
  "son cycle de vie et sur lequel, selon l’hypothèse formulée par Friedman en "
  "1957, il règle sa consommation. Il en résulte qu’une augmentation "
  "temporaire du revenu — un transfert ponctuel, une baisse d’impôt annoncée "
  "comme provisoire — est principalement épargnée, ce qui affaiblit le "
  "multiplicateur et constitue l’une des trois critiques adressées à la "
  "relance budgétaire.",
  ["hypothese du revenu permanent", "friedman 1957"],
  "S’oppose au rôle du revenu courant dans la fonction de consommation "
  "keynésienne."),

 ("Équivalence ricardienne", ['25'],
  "Troisième critique : Barro et l’équivalence ricardienne (1974)",
  "L’équivalence ricardienne, formulée par Barro en 1974, énonce qu’une "
  "relance financée par le déficit implique un financement futur : les ménages "
  "anticipant la hausse d’impôts à venir augmentent leur épargne, qui compense "
  "la désépargne publique et annule l’effet de la relance. Le chapitre "
  "souligne que ce résultat repose sur des hypothèses fortes — information "
  "parfaite, horizon long, absence de contrainte de liquidité.",
  ["barro 1974", "equivalence ricardienne de barro"],
  "Troisième critique de la relance, distincte de l’effet d’éviction et du "
  "revenu permanent."),

 ("Ex ante et ex post", ['25'],
  "Ex ante : les décisions sont prises avant leur réalisation",
  "La distinction ex ante / ex post sépare les décisions prises avant leur "
  "réalisation des grandeurs constatées après coup. Elle éclaire la première "
  "grande critique adressée au modèle IS-LM : l’épargne et l’investissement ne "
  "sont pas nécessairement égaux ex ante, puisqu’ils résultent de décisions "
  "d’agents différents ; c’est le multiplicateur qui, en engendrant le revenu "
  "et donc l’épargne, rend l’égalité vraie ex post.",
  ["ex ante", "ex post", "distinction ex ante ex post"],
  "L’égalité comptable constatée ex post ne prouve aucun ajustement "
  "automatique ex ante."),

 ("Balance globale", ['25'],
  "La balance globale compare les transactions courantes et les mouvements "
  "autonomes de capitaux",
  "La balance globale rassemble les transactions courantes et les mouvements "
  "autonomes de capitaux : son solde indique si le pays reçoit ou cède des "
  "moyens de paiement internationaux, et c’est son équilibre que représente la "
  "courbe BP. Dans l’exemple du chapitre, un excédent courant de 100 "
  "accompagné de 140 de sorties de capitaux donne une balance globale "
  "déficitaire de 40. Un déficit courant correspond à un besoin de "
  "financement, un excédent à une capacité de financement.",
  ["balance globale des paiements", "solde de la balance globale"],
  "La balance des paiements est comptablement équilibrée dans son ensemble : "
  "seule la balance globale peut être excédentaire ou déficitaire."),

 ("Les trois D", ['25'],
  "Henri Bourguinat : les trois D de la globalisation financière",
  "Les trois D désignent, selon Henri Bourguinat, les trois mouvements qui "
  "constituent la globalisation financière : la désintermédiation, le "
  "financement passant des banques aux marchés ; la déréglementation, c’est-à-"
  "dire la levée des contrôles et des cloisonnements ; le décloisonnement, qui "
  "unifie les compartiments du marché et les places financières. Le chapitre "
  "s’en sert pour expliquer l’horizontalisation de la courbe BP dans les "
  "économies avancées, la mobilité des capitaux y étant devenue très forte.",
  ["desintermediation", "dereglementation", "decloisonnement",
   "globalisation financiere trois d"],
  "Décrit un processus institutionnel et non un choc : c’est ce qui rend la "
  "courbe BP plus plate au fil du temps."),

 ("Anticipations autoréalisatrices", ['25', '26'],
  "Les anticipations peuvent devenir autoréalisatrices",
  "Une anticipation est autoréalisatrice lorsque le comportement qu’elle "
  "induit la rend vraie : les entreprises qui anticipent une demande faible "
  "renoncent à investir et à embaucher, ce qui déprime effectivement la "
  "demande et entretient le cercle vicieux du sous-emploi. Le même mécanisme "
  "opère sur le marché des changes, où l’anticipation d’une dévaluation nourrit "
  "les attaques qui la rendent inévitable.",
  ["anticipation autorealisatrice", "prophetie autorealisatrice"],
  "À distinguer d’une simple prévision : ici l’anticipation modifie la "
  "réalité qu’elle décrit."),

 ("Politique contracyclique", ['25'],
  "Une politique de stabilisation doit être contracyclique",
  "Une politique contracyclique agit en sens inverse de la conjoncture : "
  "soutien de la demande lorsque l’activité est inférieure à son potentiel, "
  "freinage lorsqu’elle le dépasse. C’est la définition même d’une politique "
  "de stabilisation, dont l’écart de production fournit le diagnostic et dont "
  "IS-LM représente les effets par les déplacements de IS et de LM.",
  ["politique de stabilisation", "politique conjoncturelle contracyclique"],
  "S’oppose à une politique procyclique, qui amplifie le cycle, et aux "
  "politiques structurelles, qui visent la production potentielle."),
]
