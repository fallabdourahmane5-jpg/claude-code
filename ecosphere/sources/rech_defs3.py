# -*- coding: utf-8 -*-
"""Définitions ajoutées après l'audit par familles — 2e partie.

Familles examinées : production et productivité, offre et demande, effets,
revenus, soldes extérieurs, intégration et dépendances, rentes, classes et
chômage, outils d'analyse.

Format : (terme, chapitres, ancre, définition, alias, distinction)
"""

DEFS = [

 # ------------------------------------------------- production, productivité
 ("Fonction de production", ['4', '6'],
  "L’outil central : la fonction de production macroéconomique",
  "Une fonction de production décrit le lien entre la quantité produite et les "
  "facteurs de production employés — travail, capital — et le niveau de "
  "technologie disponible. À l’échelle macroéconomique, elle sert à décomposer "
  "la croissance : la part qui s’explique par la hausse du travail, celle qui "
  "s’explique par l’accumulation du capital, et le résidu, attribué à la "
  "productivité globale des facteurs.",
  ["cobb douglas", "fonction de production macroeconomique"],
  "À distinguer de l’isoquante, qui en est la représentation à production "
  "constante, et du rendement d’échelle, qui décrit sa réaction à une "
  "augmentation proportionnelle de tous les facteurs."),

 ("Coefficient de capital", ['6'],
  "Le coefficient de capital : pourquoi c’est la clé du modèle",
  "Le coefficient de capital est la quantité de capital nécessaire pour "
  "produire une unité supplémentaire : le rapport du capital à la production. "
  "C’est la clé du modèle de Harrod, puisqu’il relie l’investissement au "
  "supplément de production qu’il permet : plus il est élevé, plus "
  "l’investissement requis pour soutenir un taux de croissance donné est "
  "important.",
  ["intensite capitalistique de la production", "rapport capital production"],
  "À distinguer du capital par tête, qui rapporte le capital au nombre de "
  "travailleurs et non à la production."),

 ("Productivité du travail", ['4', '6', '7', '8', '22', '23'],
  "Productivité moyenne du travail",
  "La productivité du travail rapporte la production à la quantité de travail "
  "employée, mesurée en nombre de travailleurs ou en heures travaillées. Elle "
  "commande à la fois le niveau de vie et la compétitivité : le cours en fait "
  "le dénominateur du coût salarial unitaire, de sorte qu’un pays à hauts "
  "salaires peut rester compétitif si sa productivité est élevée. Ricardo "
  "faisait des écarts de productivité du travail la seule différence entre "
  "pays, limite que le cours relève explicitement.",
  ["productivite par tete", "productivite horaire"],
  "À distinguer de la productivité globale des facteurs, qui mesure "
  "l’efficacité conjointe du travail et du capital."),

 ("Productivité moyenne", ['4', '6', '7', '23'],
  "Productivité moyenne du travail (PML)",
  "La productivité moyenne d’un facteur est la production totale divisée par "
  "la quantité de ce facteur : la production par unité de travail, ou par "
  "unité de capital. Elle se distingue de la productivité marginale, qui "
  "mesure le supplément de production dû à une unité de facteur "
  "supplémentaire. Le cours relève que l’embauche d’un travailleur plus "
  "productif que la moyenne élève la productivité moyenne, et inversement.",
  ["pml", "productivite marginale", "production par unite de travail"],
  "La productivité marginale peut diminuer alors que la productivité moyenne "
  "augmente encore : c’est pourquoi les deux ne doivent pas être confondues."),

 ("Production de masse", ['6', '8', '9'],
  "Le fordisme : production de masse et modèle économique",
  "La production de masse est la fabrication de biens standardisés en très "
  "grandes séries, rendue possible par la mécanisation, la division poussée "
  "des tâches et le travail à la chaîne. Le cours l’associe au fordisme, où "
  "elle forme système avec la hausse des salaires et la consommation de masse. "
  "Elle appartient à une phase du développement industriel où les gains de "
  "productivité et la demande d’équipement croissent ensemble, avant "
  "l’automatisation et le recul de l’emploi industriel.",
  ["fordisme", "travail a la chaine", "standardisation"],
  "À distinguer de la consommation de masse, qui en est le débouché, et de la "
  "production flexible, qui lui succède avec le toyotisme."),

 ("Substitution du capital au travail", ['6', '8'],
  "Une substitution du capital au travail",
  "La substitution du capital au travail est le remplacement de travailleurs "
  "par des équipements lorsque le capital devient relativement moins coûteux "
  "ou plus efficace. Le cours l’examine à propos de l’intelligence "
  "artificielle : si elle est plus rapide et moins coûteuse, les entreprises "
  "remplacent du travail humain par du capital technologique. L’effet net sur "
  "l’emploi dépend alors des créations induites ailleurs et de la capacité de "
  "reconversion des travailleurs.",
  ["automatisation", "remplacement du travail par le capital"],
  "À distinguer de la complémentarité capital-travail, où l’équipement rend "
  "le travailleur plus productif au lieu de l’évincer."),

 # ----------------------------------------------------------- offre, demande
 ("Demande globale", ['1', '2', '3', '4', '6'],
  "La demande effective",
  "La demande globale est l’ensemble de la demande adressée à l’économie : "
  "consommation des ménages, investissement des entreprises, dépenses "
  "publiques, et exportations en économie ouverte. Dans l’analyse "
  "keynésienne, elle détermine le niveau de production et d’emploi : une "
  "demande globale insuffisante laisse des capacités inemployées. Le cours en "
  "donne l’illustration historique avec la politique de soutien à la demande "
  "globale menée par Roosevelt en 1933.",
  ["demande agregee", "offre globale"],
  "À distinguer de la demande effective, qui est la demande que les "
  "entrepreneurs anticipent et sur laquelle ils fondent leurs décisions."),

 ("Demande extérieure", ['7', '21', '23'],
  "La demande extérieure peut soutenir production et emploi",
  "La demande extérieure est la demande adressée aux producteurs nationaux par "
  "le reste du monde, c’est-à-dire les exportations. Elle peut soutenir "
  "directement la production, l’emploi et les revenus, et prendre le relais "
  "d’une demande intérieure défaillante. Le cours en souligne la contrepartie : "
  "une économie très dépendante de la demande extérieure voit sa croissance "
  "immédiatement fragilisée si celle-ci ralentit.",
  ["exportations", "debouches exterieurs"],
  "Son pendant est la demande intérieure, adressée par les résidents ; la "
  "somme des deux forme la demande globale."),

 ("Demande de variété", ['23'],
  "Lassudrie-Duchêne : une demande de différence",
  "La demande de variété est le goût des consommateurs pour la diversité des "
  "produits, qui les conduit à acheter des biens étrangers comparables à ceux "
  "produits chez eux. Elle explique le commerce intrabranche entre économies "
  "semblables, que les avantages comparatifs ne peuvent pas expliquer : avec "
  "l’augmentation des revenus, les consommateurs souhaitent accéder à "
  "davantage de produits différents, ce que Lassudrie-Duchêne nomme une "
  "demande de différence.",
  ["demande de difference", "gout pour la variete"],
  "À distinguer de la différenciation des produits, qui est la réponse des "
  "producteurs à cette demande."),

 ("Courbe de demande", ['3', '4', '5'], "La demande du consommateur",
  "La courbe de demande relie, pour un bien donné, le prix à la quantité que "
  "les consommateurs souhaitent acheter ; elle est décroissante, puisqu’un "
  "prix plus élevé réduit la quantité demandée. Son croisement avec la courbe "
  "d’offre détermine le prix et la quantité d’équilibre. Le cours rapporte la "
  "critique de Sonnenschein, reprise par Steve Keen : la forme de la courbe de "
  "demande agrégée n’est pas déterminée par la théorie, ce qui fragilise les "
  "conclusions qu’on en tire.",
  ["demande du consommateur"],
  "À distinguer de la demande globale, notion macroéconomique qui porte sur "
  "l’ensemble de l’économie et non sur un bien."),

 ("Courbe d’offre", ['3', '4', '5', '9'], "Maximisation du profit et courbe d’offre",
  "La courbe d’offre relie, pour un bien donné, le prix à la quantité que les "
  "producteurs acceptent de vendre ; elle est croissante, puisqu’un prix plus "
  "élevé rend rentable une production plus coûteuse. Elle se déduit de la "
  "maximisation du profit : le producteur offre jusqu’au point où le prix "
  "égale son coût marginal.",
  ["offre du producteur"],
  "À distinguer de l’offre globale, qui désigne l’ensemble de la production "
  "disponible dans l’économie."),

 ("Utilité totale", ['3', '4'], "Lien entre utilité totale et utilité marginale",
  "L’utilité totale est la satisfaction que procure l’ensemble des unités "
  "consommées d’un bien. L’utilité marginale en est la pente : comme elle "
  "décroît, la courbe d’utilité totale est croissante mais concave. Le "
  "consommateur maximise son utilité totale sous contrainte de budget, ce qui "
  "le conduit à égaliser les utilités marginales pondérées par les prix.",
  ["satisfaction totale"],
  "À distinguer de l’utilité marginale, qui porte sur la dernière unité "
  "consommée et décroît quand l’utilité totale augmente encore."),

 ("Propension moyenne à consommer", ['1', '3'],
  "Les hypothèses de Keynes",
  "La propension moyenne à consommer est la part du revenu consacrée à la "
  "consommation, soit le rapport de la consommation au revenu. Keynes la "
  "distingue de la propension marginale à consommer, qui mesure la part du "
  "revenu supplémentaire consommée : la première décroît quand le revenu "
  "augmente, la seconde reste inférieure à un, ce qui fonde le mécanisme du "
  "multiplicateur.",
  ["c sur y", "propension a consommer"],
  "La propension marginale, et non la moyenne, détermine la valeur du "
  "multiplicateur keynésien."),

 # -------------------------------------------------------------- les effets
 ("Effet d’aubaine", ['6', '22'], "L’effet d’aubaine : un problème de ciblage",
  "Il y a effet d’aubaine lorsqu’un agent bénéficie d’une aide publique alors "
  "qu’il aurait adopté le même comportement en son absence : l’aide ne change "
  "pas la décision, elle réduit simplement le coût pour celui qui l’aurait "
  "prise de toute façon. C’est un problème de ciblage, qui réduit l’efficience "
  "de la dépense publique. Le cours l’applique aux allègements de cotisations "
  "concentrés sur les bas salaires, qui peuvent enfermer les entreprises dans "
  "une trappe à bas salaires.",
  ["effet d aubaine fiscal", "mauvais ciblage"],
  "À distinguer de l’effet d’entraînement, où l’aide déclenche "
  "effectivement un comportement qui n’aurait pas eu lieu."),

 ("Effet richesse", ['2', '21'], "Les canaux de la politique monétaire",
  "L’effet richesse est l’influence de la valeur du patrimoine sur les "
  "dépenses : lorsque la valeur des actifs détenus augmente, les ménages se "
  "sentent plus riches et consomment davantage ; lorsqu’elle baisse, ils "
  "épargnent pour reconstituer leur patrimoine. Le cours y rattache l’effet "
  "Pigou dans la logique patrimoniale, et en donne un exemple négatif : la "
  "crise immobilière chinoise a renforcé l’épargne des ménages en provoquant "
  "un effet richesse négatif.",
  ["effet de patrimoine", "effet pigou"],
  "À distinguer de l’effet revenu, qui porte sur la variation du revenu "
  "courant et non sur celle du patrimoine."),

 ("Effet prix et effet revenu", ['4'], "L’effet prix et revenu",
  "La baisse du prix d’un bien agit par deux canaux distincts. L’effet de "
  "substitution, ou effet prix, conduit à remplacer un bien par un autre : la "
  "consommation du bien devenu moins cher augmente et celle de l’autre "
  "diminue. L’effet revenu vient de ce que la baisse de prix élève le pouvoir "
  "d’achat réel à revenu nominal inchangé : on peut consommer davantage des "
  "deux biens. La variation observée est la somme des deux effets.",
  ["effet de substitution", "effet revenu", "effet prix"],
  "Pour un bien normal les deux effets vont dans le même sens ; pour un bien "
  "inférieur, l’effet revenu peut s’opposer à l’effet de substitution."),

 ("Effet de serre", ['6', '7', '22', '23', '24'],
  "Les limites écologiques de la croissance",
  "L’effet de serre est le phénomène par lequel certains gaz présents dans "
  "l’atmosphère retiennent une partie du rayonnement terrestre et élèvent la "
  "température du globe. Son renforcement par les émissions d’origine humaine "
  "constitue, dans le cours, la principale externalité négative globale, celle "
  "qui justifie une gouvernance mondiale du climat. Le Pacte vert européen "
  "fixe ainsi un objectif de réduction de 55 % des émissions de gaz à effet de "
  "serre d’ici 2030 par rapport à 1990.",
  ["gaz a effet de serre", "ges", "emissions"],
  "À distinguer du dérèglement climatique, qui en est la conséquence "
  "observée, et de l’empreinte carbone, qui en est une mesure imputée à un "
  "territoire ou à un agent."),

 # ------------------------------------------------------------- les revenus
 ("Revenu courant", ['1', '3'], "Les hypothèses de Keynes",
  "Le revenu courant est le revenu disponible de la période présente, par "
  "opposition au revenu anticipé sur l’ensemble du cycle de vie. Chez Keynes, "
  "la consommation dépend principalement du revenu courant et de la propension "
  "marginale à consommer : c’est l’hypothèse qui fonde le multiplicateur. Elle "
  "est posée dans la Théorie générale de l’emploi, de l’intérêt et de la "
  "monnaie, en 1936.",
  ["revenu disponible courant"],
  "À distinguer du revenu permanent de Friedman et du revenu de cycle de vie "
  "de Modigliani, qui font dépendre la consommation d’un revenu anticipé."),

 ("Revenu réel et revenu nominal", ['1', '4', '6'],
  "Le pouvoir d’achat du revenu",
  "Le revenu nominal est le revenu exprimé en euros courants ; le revenu réel "
  "est ce même revenu corrigé de la variation des prix, c’est-à-dire le "
  "pouvoir d’achat qu’il procure. On l’obtient en divisant le revenu nominal "
  "par l’indice des prix, multiplié par cent : avec un revenu nominal de 1 000 "
  "et un indice de 110, le revenu réel vaut environ 909. Un revenu nominal qui "
  "augmente moins vite que les prix correspond donc à une perte de pouvoir "
  "d’achat.",
  ["pouvoir d achat", "revenu nominal", "revenu reel"],
  "C’est la même distinction qu’entre taux d’intérêt nominal et réel, ou "
  "entre croissance en valeur et croissance en volume."),

 ("Indice des prix", ['1', '2'], "La mesure de l’inflation",
  "Un indice des prix mesure l’évolution du niveau général des prix d’un "
  "panier de biens et de services entre une date de référence, dont l’indice "
  "vaut cent, et la date considérée. Il sert à passer des grandeurs nominales "
  "aux grandeurs réelles : le pouvoir d’achat du revenu s’obtient en divisant "
  "le revenu nominal par l’indice des prix. Sa variation annuelle est le taux "
  "d’inflation.",
  ["ipc", "indice des prix a la consommation", "deflateur"],
  "À distinguer du niveau des prix lui-même : un indice qui augmente moins "
  "vite décrit une inflation qui ralentit, non des prix qui baissent."),

 # ------------------------------------------------- les soldes extérieurs
 ("Balance courante", ['21', '23'], "La balance des paiements",
  "La balance courante est le compte de la balance des paiements qui retrace "
  "les échanges de biens et de services, les revenus primaires — revenus du "
  "travail et des investissements — et les revenus secondaires, c’est-à-dire "
  "les transferts sans contrepartie. Son solde mesure la capacité ou le besoin "
  "de financement de la nation vis-à-vis du reste du monde. Le cours souligne "
  "qu’elle doit être lue dans son ensemble : les États-Unis présentent un "
  "désavantage marqué dans les biens mais des avantages importants dans les "
  "services et les revenus primaires.",
  ["compte courant", "solde courant"],
  "À distinguer de la balance commerciale, qui ne retient que les biens et "
  "services, et de la position extérieure nette, qui est un stock et non un "
  "flux."),

 ("Déficit commercial", ['6', '7', '21', '22', '23'],
  "Une confusion fréquente : déficit commercial et compétitivité",
  "Le déficit commercial est le solde négatif des échanges de biens et de "
  "services : les importations dépassent les exportations. Le cours met en "
  "garde contre l’assimilation immédiate au manque de compétitivité : un "
  "déficit peut provenir d’une demande intérieure dynamique, d’un "
  "investissement en biens d’équipement importés, ou du rôle de la monnaie "
  "nationale dans le système monétaire international. Il doit donc être lu "
  "avec l’ensemble de la balance courante et la position extérieure nette.",
  ["solde commercial negatif", "deficit exterieur"],
  "À distinguer du déficit public, qui concerne les finances de l’État : "
  "leur lien passe par la demande intérieure, c’est le mécanisme des déficits "
  "jumeaux."),

 ("Déficit bilatéral", ['21', '22', '23'],
  "Trump II : le « Liberation Day » du 2 avril 2025",
  "Un déficit bilatéral est le solde négatif des échanges d’un pays avec un "
  "partenaire déterminé. Le cours insiste sur sa faible portée analytique : il "
  "reflète la structure des spécialisations et la place de chaque pays dans "
  "les chaînes de valeur, non la loyauté du partenaire. Un déficit bilatéral "
  "ne suffit donc pas à démontrer une concurrence déloyale, et son usage comme "
  "preuve relève d’une lecture néo-mercantiliste.",
  ["solde bilateral"],
  "À distinguer du solde global, seul pertinent pour apprécier la position "
  "extérieure d’un pays."),

 ("Excédent commercial", ['21', '23'], "Excédent commercial et appréciation",
  "L’excédent commercial est le solde positif des échanges : les exportations "
  "dépassent les importations. Le cours en décrit l’effet monétaire : les "
  "étrangers doivent demander davantage la monnaie du pays pour payer ses "
  "produits, ce qui tend à l’apprécier, et cette appréciation érode à son tour "
  "la compétitivité-prix. Il rappelle aussi que tous les pays ne peuvent pas "
  "être simultanément excédentaires.",
  ["solde commercial positif"],
  "Un excédent n’est pas en soi un succès : poursuivi pour lui-même, il "
  "relève d’un objectif mercantiliste, alors que ce sont les importations qui "
  "matérialisent le gain à l’échange."),

 # ------------------------------------------- intégration et dépendances
 ("Intégration régionale", ['7', '21', '24'],
  "Les étapes de l’intégration selon Balassa",
  "L’intégration régionale est le rapprochement économique organisé entre pays "
  "voisins. Balassa en distingue cinq niveaux croissants : zone de "
  "libre-échange, union douanière, marché commun, union économique et "
  "monétaire, intégration totale, chaque étape ajoutant une dimension à la "
  "précédente et réduisant l’autonomie économique des États membres. Le cours "
  "souligne qu’elle n’est pas un repli : la part de l’ASEAN dans les "
  "exportations mondiales passe d’environ 4 % en 1990 à environ 8 % en 2021.",
  ["regionalisation", "integration economique regionale"],
  "À distinguer du multilatéralisme, qui organise l’ouverture entre tous les "
  "membres d’un système, et du bilatéralisme, limité à deux partenaires."),

 ("Intégration commerciale", ['7', '21', '23', '24'],
  "Mesurer la mondialisation commerciale",
  "L’intégration commerciale est le degré auquel une économie participe aux "
  "échanges internationaux, mesuré par le taux d’ouverture, le taux de "
  "pénétration ou la part des échanges dans le produit intérieur brut. Le "
  "cours en relativise les effets : le cas indien montre que la modernisation "
  "partielle et l’intégration commerciale ne suffisent pas à garantir un "
  "décollage industriel si le pays reste enfermé dans une spécialisation "
  "dominée.",
  ["ouverture commerciale", "insertion commerciale"],
  "À distinguer de l’intégration régionale, qui suppose des institutions "
  "communes, et de l’intégration productive, qui porte sur les chaînes de "
  "valeur."),

 ("Dépendance extérieure", ['6', '7', '21', '22'],
  "Protection commerciale, sécurité économique et souveraineté",
  "La dépendance extérieure est la situation d’une économie dont une "
  "production, un approvisionnement ou un financement essentiels reposent sur "
  "l’étranger, sans substitut rapidement disponible. Le cours en fait le "
  "critère de la souveraineté industrielle : il n’est pas rationnel de "
  "relocaliser une production simplement parce qu’elle a disparu du "
  "territoire ; encore faut-il qu’elle soit stratégique et que la dépendance "
  "fasse peser un risque significatif.",
  ["dependance strategique", "vulnerabilite exterieure"],
  "À distinguer de l’interdépendance, qui est réciproque : c’est l’asymétrie "
  "de la relation qui transforme une interdépendance en dépendance."),

 ("Dépendance technologique", ['7', '21', '22'],
  "La montée en gamme chinoise",
  "La dépendance technologique est la situation d’un pays qui doit importer "
  "les technologies critiques qu’il ne maîtrise pas : semi-conducteurs, "
  "équipements de production, logiciels, brevets. Elle est l’objet explicite "
  "du plan Made in China 2025, destiné à produire davantage de technologies "
  "sur le territoire chinois pour la réduire. Le cours en mesure l’enjeu par "
  "l’écart des investissements privés dans l’intelligence artificielle entre "
  "2013 et 2023 : environ 289 milliards d’euros aux États-Unis contre environ "
  "89 milliards en Chine.",
  ["souverainete technologique", "autonomie technologique"],
  "À distinguer de la dépendance énergétique, qui porte sur les "
  "approvisionnements en énergie, et du retard technologique, qui est un écart "
  "et non une relation."),

 ("Dépendance énergétique", ['21', '22'],
  "Troisième signal inquiétant : la dépendance énergétique",
  "La dépendance énergétique est la part de la consommation d’énergie d’un "
  "pays qui doit être importée. Le cours en fait l’un des signaux "
  "d’affaiblissement de la position extérieure européenne : elle rend le solde "
  "commercial et le niveau général des prix sensibles aux cours mondiaux des "
  "hydrocarbures, et expose l’économie à l’instrumentalisation politique de "
  "ses approvisionnements.",
  ["taux de dependance energetique", "importations d energie"],
  "À distinguer de l’intensité énergétique, qui mesure l’énergie nécessaire "
  "pour produire une unité de richesse."),

 ("Dépendance au sentier", ['3', '6', '23'],
  "Les institutions et la trajectoire de croissance",
  "La dépendance au sentier désigne le fait qu’une trajectoire passée "
  "contraigne les choix présents : les décisions déjà prises, les "
  "investissements déjà engagés et les institutions déjà en place rendent "
  "certains changements coûteux, de sorte qu’une organisation reste souvent "
  "dans sa trajectoire antérieure même lorsqu’une autre serait préférable. Le "
  "cours l’emploie pour expliquer l’inertie des entreprises comme la "
  "persistance d’institutions inefficaces.",
  ["path dependence", "inertie institutionnelle"],
  "À distinguer du verrouillage technologique, qui en est un cas particulier "
  "portant sur un standard ou une technique."),

 ("Rattrapage technologique", ['21', '22', '23'],
  "Airbus : l’exemple du rattrapage technologique européen",
  "Le rattrapage technologique est le processus par lequel un pays ou une "
  "firme réduit son écart de maîtrise technique avec la frontière "
  "technologique, par imitation, acquisition, transfert ou effort de recherche "
  "propre. Le cours en donne deux illustrations : Airbus, où plusieurs États "
  "européens mutualisent leurs moyens pour dépasser le cadre national, et la "
  "montée en gamme chinoise, où la valeur ajoutée locale d’un même produit "
  "progresse fortement.",
  ["catch up technologique", "imitation technologique"],
  "À distinguer de l’innovation à la frontière, qui suppose de créer une "
  "technologie inexistante et non d’en acquérir une déjà disponible."),

 ("Transfert de technologie", ['21', '22', '23'],
  "Le transfert de technologie : transformer l’IDE en instrument de rattrapage",
  "Le transfert de technologie est la circulation de savoirs techniques, de "
  "procédés et de méthodes d’organisation d’une firme ou d’un pays vers un "
  "autre, par l’investissement direct, la coentreprise, la sous-traitance, la "
  "licence ou la formation. Le cours en fait l’instrument qui transforme "
  "l’investissement direct étranger en levier de rattrapage, lorsque le pays "
  "d’accueil est capable d’absorber la technologie reçue.",
  ["diffusion technologique", "coentreprise"],
  "À distinguer de la simple implantation d’une filiale, qui peut n’apporter "
  "que de l’assemblage sans diffusion de savoir."),

 ("Avance technologique", ['9', '21', '22', '23'],
  "L’écart technologique",
  "L’avance technologique est la supériorité temporaire d’un pays ou d’une "
  "firme dans la maîtrise d’une technique, qui lui confère un avantage "
  "comparatif tant qu’elle n’est pas imitée. Posner en fait l’origine d’un "
  "avantage transitoire : l’imitation réduit progressivement l’écart "
  "technologique, et le cycle de vie du produit de Vernon décrit le "
  "déplacement de la production qui s’ensuit.",
  ["ecart technologique", "avance technique"],
  "Elle est par construction provisoire, à la différence d’une dotation "
  "factorielle, qui est durable."),

 ("Droits de propriété intellectuelle", ['5', '6', '24'],
  "Les brevets et l’incitation à innover",
  "Les droits de propriété intellectuelle sont les droits exclusifs accordés à "
  "un innovateur sur l’exploitation de sa création : brevets, marques, droits "
  "d’auteur. Ils répondent à une défaillance de marché, l’innovation étant un "
  "bien non rival que chacun pourrait utiliser sans payer : en rendant le "
  "savoir temporairement excluable, le brevet rétablit l’incitation à "
  "innover.",
  ["brevet", "propriete intellectuelle", "licence"],
  "Leur contrepartie est un monopole temporaire, donc une perte d’efficience "
  "statique acceptée au nom de l’efficience dynamique."),

 # ------------------------------------------------ politique commerciale
 ("Multilatéralisme commercial", ['21', '22', '23', '24'],
  "Le GATT organise le multilatéralisme commercial à partir de 1947",
  "Le multilatéralisme commercial est l’organisation des échanges par des "
  "règles communes négociées entre au moins trois États et appliquées à tous "
  "les membres, grâce à la clause de la nation la plus favorisée qui "
  "généralise chaque concession. Institué par le GATT en 1947 puis par l’OMC, "
  "il repose sur la négociation, la réciprocité et un mécanisme de règlement "
  "des différends. Le cours décrit sa crise : échec du cycle de Doha, "
  "multiplication des accords régionaux et retour de l’unilatéralisme.",
  ["multilateralisme", "gatt", "omc"],
  "À distinguer du plurilatéralisme, limité à un groupe de membres, et du "
  "bilatéralisme, qui n’engage que deux partenaires."),

 ("Coordination internationale", ['7', '21', '24'],
  "La gouvernance mondiale du climat et de l’environnement",
  "La coordination internationale est l’ajustement concerté des politiques de "
  "plusieurs États en vue de produire des règles communes et des biens publics "
  "mondiaux. Le cours en fait le fondement de la gouvernance mondiale, dont le "
  "multilatéralisme constitue une forme particulière puisqu’il organise une "
  "action collective entre au moins trois États. Son obstacle est le passager "
  "clandestin : chacun a intérêt à bénéficier du bien commun sans en supporter "
  "le coût.",
  ["gouvernance mondiale", "cooperation internationale"],
  "À distinguer de l’harmonisation, qui suppose des règles identiques, et de "
  "la simple concertation, qui n’engage pas les politiques."),

 ("Tarif extérieur commun", ['21', '24'], "L’union douanière",
  "Le tarif extérieur commun est le droit de douane unique qu’appliquent, "
  "vis-à-vis des pays tiers, les membres d’une union douanière. Il distingue "
  "l’union douanière de la simple zone de libre-échange, où chaque membre "
  "garde sa propre politique commerciale extérieure. Le cours l’associe à la "
  "construction européenne, qui combine libre circulation interne et "
  "protection extérieure commune.",
  ["tec", "union douaniere"],
  "C’est précisément ce tarif commun qui oblige les membres à conduire une "
  "politique commerciale unique, donc à renoncer à la négocier séparément."),

 ("Tarif Méline", ['21'], "Le tarif Méline : retour du protectionnisme français",
  "Le tarif Méline est le tarif douanier français adopté en 1892, qui marque "
  "le retour du protectionnisme en France après la période libre-échangiste "
  "ouverte par le traité de 1860. Il relève les droits sur les produits "
  "agricoles et industriels afin de protéger notamment les agriculteurs "
  "français de la concurrence étrangère, dans un contexte de baisse des prix "
  "agricoles et d’arrivée des céréales américaines.",
  ["tarif de 1892", "protectionnisme meline"],
  "Il illustre concrètement le « bloc social » protectionniste analysé par "
  "Léo Charles à propos des producteurs céréaliers français."),

 ("Mobilité des facteurs de production", ['3', '4', '21', '23'],
  "La mobilité des facteurs de production",
  "La mobilité des facteurs est leur capacité à se déplacer d’un emploi, d’un "
  "secteur ou d’un territoire à un autre. La concurrence pure et parfaite la "
  "suppose parfaite, ce qui permet des ajustements rapides ; le cours souligne "
  "qu’elle est en réalité imparfaite — les diplômes ne sont pas transférables "
  "d’un métier à l’autre, les équipements ne se déplacent pas sans coût. "
  "C’est cette imperfection qui transforme l’ouverture commerciale en coûts "
  "d’ajustement durables.",
  ["mobilite du travail", "mobilite du capital", "fluidite des facteurs"],
  "La mobilité du capital est aujourd’hui beaucoup plus grande que celle du "
  "travail : c’est l’une des asymétries centrales de la mondialisation."),

 ("Spécialisation primaire", ['7', '21', '23'],
  "Prebisch : la dégradation des termes de l’échange",
  "La spécialisation primaire est la concentration des exportations d’un pays "
  "sur des produits agricoles, miniers ou énergétiques peu transformés. Le "
  "cours en fait le cœur de l’analyse de Prebisch : ces produits voient leurs "
  "prix progresser moins vite que ceux des produits manufacturés importés, "
  "d’où une dégradation des termes de l’échange, et la réponse préconisée est "
  "une industrialisation protégée réduisant cette spécialisation.",
  ["specialisation primaire", "exportation de matieres premieres"],
  "À distinguer de la malédiction des ressources, qui porte sur les effets "
  "internes de la rente, et de la spécialisation impasse, qui désigne toute "
  "spécialisation enfermante."),

 # --------------------------------------------- rentes, classes, chômage
 ("Rente différentielle", ['3', '23'], "Ricardo et la rente foncière",
  "La rente différentielle est le revenu que procure la détention d’une terre "
  "plus fertile que la terre marginale. Comme le prix agricole est déterminé "
  "par le coût marginal de la terre la moins fertile mise en culture, les "
  "meilleures terres produisent au même prix pour un coût plus faible : "
  "l’écart revient au propriétaire. Ricardo en tire une loi de répartition "
  "défavorable aux profits, puisque l’extension des cultures élève la rente et "
  "comprime le taux de profit.",
  ["rente ricardienne", "rente fonciere"],
  "À distinguer de la rente de monopole, qui provient d’une position de "
  "marché et non d’une différence de fertilité."),

 ("Rente de monopole", ['5', '9'], "Apparition d’une rente de monopole",
  "La rente de monopole est le profit élevé obtenu non par une efficacité "
  "supérieure mais par une position dominante sur le marché. Le cours en "
  "souligne l’ambivalence : elle peut récompenser l’innovation qui a permis "
  "d’atteindre cette position, mais elle se maintient ensuite par la seule "
  "barrière à l’entrée, en laissant un prix supérieur et une quantité "
  "inférieure à l’optimum concurrentiel.",
  ["profit de monopole", "surprofit"],
  "À distinguer du profit concurrentiel, qui rémunère le risque et "
  "l’efficacité, et de la recherche de rente, qui est l’activité consistant à "
  "obtenir ou défendre une telle position."),

 ("Classe ouvrière", ['10', '8'],
  "1880-1910 : émergence d’une classe ouvrière moderne",
  "La classe ouvrière désigne l’ensemble des travailleurs manuels de "
  "l’industrie, constitués en groupe social par des conditions de travail, un "
  "mode de vie et une conscience communs. Le cours en situe la formation "
  "moderne entre 1880 et 1910, période où se développent la concentration "
  "industrielle, les organisations syndicales et la mobilisation politique, "
  "avant que la société salariale puis la tertiarisation n’en recomposent les "
  "contours.",
  ["proletariat", "monde ouvrier"],
  "À distinguer de la classe moyenne salariée, dont le cours décrit la "
  "montée, et du salariat, qui est un statut juridique et non un groupe "
  "social."),

 ("Classe stérile", ['3'], "Les trois classes sociales chez Quesnay",
  "La classe stérile est, dans le Tableau économique de Quesnay, la classe des "
  "artisans, commerçants et manufacturiers : elle transforme et fait circuler "
  "la richesse sans en créer, puisque pour les physiocrates seule la terre est "
  "productive. Elle s’oppose à la classe productive, celle des fermiers, et à "
  "la classe des propriétaires, qui reçoit le produit net.",
  ["classe des artisans", "classe productive"],
  "À ne pas confondre avec la classe de loisir de Veblen, qui désigne une "
  "élite consommatrice ostentatoire et non une fonction dans la production."),

 ("Chômage involontaire", ['3', '10'],
  "Les keynésiens : rigidités et chômage involontaire",
  "Le chômage involontaire est celui de travailleurs qui souhaitent travailler "
  "au salaire en vigueur mais ne trouvent pas d’emploi, faute d’une demande "
  "suffisante adressée aux entreprises. Sa reconnaissance sépare les "
  "keynésiens des néoclassiques : pour les premiers, marchés imparfaits et "
  "rigidités de prix et de salaires rendent ce chômage possible et justifient "
  "l’intervention de l’État ; pour les seconds, le chômage durable résulte "
  "d’entraves au libre jeu du marché du travail.",
  ["chomage keynesien", "chomage de demande"],
  "À distinguer du chômage volontaire, choisi faute d’une rémunération jugée "
  "suffisante, et du chômage naturel, que la politique économique ne peut pas "
  "réduire durablement."),

 ("Chômage naturel", ['2', '3'], "La courbe de Phillips et son dépassement",
  "Le taux de chômage naturel est, dans l’analyse monétariste, le niveau de "
  "chômage compatible avec la stabilité des prix, déterminé par les "
  "caractéristiques structurelles du marché du travail. Le cours en tire la "
  "conséquence décisive : il existe un taux de chômage qu’on ne peut pas "
  "réduire par la politique monétaire ou budgétaire, de sorte que toute "
  "tentative de descendre durablement en dessous n’engendre que de "
  "l’inflation.",
  ["taux de chomage naturel", "nairu"],
  "À distinguer du chômage involontaire keynésien, qui suppose au contraire "
  "qu’une relance de la demande puisse réduire le chômage."),

 # --------------------------------------------------- firmes et capitalisme
 ("Société mère et filiale", ['22'],
  "Le vocabulaire de l’internationalisation des firmes",
  "La société mère est l’entreprise qui détient le contrôle d’autres sociétés "
  "et dans laquelle se situe le siège social du groupe ; les filiales sont les "
  "sociétés qu’elle contrôle, dans le pays d’origine ou à l’étranger. Ce "
  "couple définit la firme multinationale : une entreprise dont la société "
  "mère détient au moins une filiale implantée hors de son territoire "
  "national, l’investissement direct étranger étant l’opération qui crée ou "
  "acquiert cette filiale.",
  ["societe mere", "filiale", "maison mere", "groupe",
   "firme multinationale"],
  "À distinguer de la sous-traitance, qui organise une relation contractuelle "
  "sans prise de contrôle du capital."),

 ("Internationalisation des firmes", ['21', '22'],
  "Le vocabulaire de l’internationalisation des firmes",
  "L’internationalisation d’une firme est l’extension de son activité hors de "
  "son territoire d’origine. Le cours en distingue les degrés : exporter "
  "depuis le pays d’origine, puis implanter une filiale commerciale, puis "
  "produire à l’étranger en créant une filiale, en achetant une entreprise "
  "locale ou en construisant une usine. Elle répond à trois logiques "
  "principales : accéder à un marché, réduire les coûts, sécuriser un "
  "approvisionnement.",
  ["multinationalisation", "implantation a l etranger"],
  "À distinguer de la mondialisation, qui est le processus d’ensemble, et de "
  "la délocalisation, qui suppose le transfert d’une production existante."),

 ("Régime d’accumulation", ['3', '8'],
  "L’école de la régulation",
  "Un régime d’accumulation est, chez les régulationnistes, la configuration "
  "d’ensemble qui permet à l’accumulation du capital de se poursuivre "
  "durablement : une organisation de la production, un partage de la valeur "
  "ajoutée, un rapport salarial, un régime monétaire et une forme "
  "d’insertion internationale compatibles entre eux. Le cours s’en sert pour "
  "périodiser le capitalisme : la crise survient lorsque ces éléments cessent "
  "de s’ajuster.",
  ["mode de regulation", "ecole de la regulation", "fordisme"],
  "À distinguer du mode de régulation, qui désigne les institutions assurant "
  "la cohérence du régime, et du cycle, qui est une fluctuation à l’intérieur "
  "d’un même régime."),

 # ------------------------------------------------------------ divers utiles
 ("État stationnaire", ['3', '6'],
  "Ricardo et l’État stationnaire",
  "L’état stationnaire est la situation vers laquelle tend une économie dont "
  "la croissance s’épuise. Chez Ricardo, au début du XIXᵉ siècle, il résulte "
  "de la mise en culture de terres de moins en moins fertiles : le prix des "
  "subsistances et la rente foncière augmentent, les profits se compriment, et "
  "l’accumulation s’arrête. Le cours en fait l’antécédent intellectuel de la "
  "stagnation séculaire analysée bien plus tard par Hansen.",
  ["etat stationnaire ricardien", "epuisement de la croissance"],
  "À distinguer de l’état stationnaire du modèle de Solow, où la croissance "
  "par tête cesse faute de progrès technique et non par rareté des terres."),

 ("Zone euro", ['2', '6', '21', '22', '24'],
  "Le rôle de la BCE",
  "La zone euro est l’ensemble des États membres de l’Union européenne qui ont "
  "adopté l’euro comme monnaie unique et dont la politique monétaire est "
  "conduite par la Banque centrale européenne. Elle constitue le niveau le "
  "plus abouti de l’intégration régionale selon la typologie de Balassa, après "
  "la zone de libre-échange, l’union douanière et le marché commun. Le "
  "Système européen de banques centrales réunit l’Eurosystème et les banques "
  "centrales des États membres restés hors de la zone.",
  ["union economique et monetaire", "uem", "eurosysteme"],
  "À distinguer de l’Union européenne, dont tous les membres ne sont pas dans "
  "la zone euro, et du Système européen de banques centrales, plus large que "
  "l’Eurosystème."),

 ("Crise financière", ['2', '3', '6', '7', '21', '22', '24'],
  "Instabilité financière et crises",
  "Une crise financière est un retournement brutal sur les marchés d’actifs ou "
  "dans le système bancaire : chute des prix d’actifs, défauts en chaîne, "
  "assèchement du crédit, ruine des épargnants. Le cours en décrit "
  "l’enchaînement typique — endettement, euphorie, retournement des "
  "anticipations, contagion — et son passage à l’économie réelle par la "
  "restriction du crédit, qui transforme la crise financière en crise "
  "économique.",
  ["krach", "instabilite financiere", "panique bancaire"],
  "À distinguer de la crise économique, qui porte sur la production et "
  "l’emploi : la seconde peut suivre la première sans s’y réduire."),

 ("Libre entrée et libre sortie", ['3', '4', '9'],
  "La libre entrée et la libre sortie",
  "La libre entrée et la libre sortie sont la possibilité, pour une "
  "entreprise, d’entrer sur un marché ou de le quitter sans barrière "
  "technique, financière ou réglementaire. C’est l’une des cinq hypothèses de "
  "la concurrence pure et parfaite, et elle garantit une concurrence durable. "
  "Le cours en relève le caractère irréaliste — coûts élevés, brevets, "
  "réglementations — et en tire la théorie des marchés contestables, où la "
  "seule menace d’entrée discipline l’entreprise en place.",
  ["libre entree", "libre sortie", "liberte d entree",
   "barriere a l entree", "marche contestable"],
  "À distinguer de l’atomicité, qui porte sur le nombre d’acteurs présents et "
  "non sur la possibilité d’en ajouter de nouveaux."),

 ("Gain de pouvoir d’achat", ['21', '22', '23'],
  "Quatrième effet : baisse des prix et gain de pouvoir d’achat",
  "Le gain de pouvoir d’achat lié à l’ouverture est l’augmentation de la "
  "quantité de biens et de services qu’un revenu inchangé permet d’acquérir, "
  "lorsque les importations à bas coût font baisser les prix. Le cours en "
  "souligne la nature politique : ce gain est réel et important à l’échelle "
  "agrégée, mais réparti sur une multitude d’achats, donc peu perçu, alors "
  "que les pertes d’emplois qu’il accompagne sont concentrées et visibles.",
  ["pouvoir d achat importe", "desinflation importee"],
  "C’est l’exact miroir du coût du protectionnisme : diffus d’un côté, "
  "concentré de l’autre."),

 ("Concentration géographique", ['9', '22', '23'],
  "Les économies d’agglomération",
  "La concentration géographique est le regroupement des activités "
  "économiques d’un même secteur sur un territoire restreint. Elle engendre "
  "des économies d’agglomération : bassin de main-d’œuvre spécialisée, "
  "fournisseurs proches, circulation des savoirs. Le cours en fait le "
  "mécanisme qui rend les avantages comparatifs cumulatifs et explique la "
  "persistance des districts industriels et des clusters.",
  ["agglomeration", "cluster", "district industriel"],
  "À distinguer de la concentration économique, qui porte sur la part de "
  "marché des entreprises et non sur leur localisation."),
]
