# -*- coding: utf-8 -*-
"""Visualisation 1 — La croissance économique (type hub)."""

from vz_base import v, nd, ln

v('vz-croissance', 'La croissance économique',
  'Chapitre 6 · noyau et branches',
  'hub',
  "La croissance n’est pas un phénomène naturel mais un régime historique, "
  "apparu avec la Révolution industrielle. Cette visualisation en sépare les "
  "cinq questions que les cours traitent séparément : comment on la mesure, "
  "ce qui l’alimente, ce qui l’explique durablement, ce qui la freine, et ce "
  "sur quoi les économistes continuent de s’opposer.",
  [("Lire du centre vers l’extérieur",
    "Le cœur donne la définition et la rupture historique. Les cinq branches "
    "sont les cinq questions du chapitre : mesurer, accumuler, innover, "
    "instituer, buter sur des limites. Les nœuds extérieurs détaillent chaque "
    "branche avec ses auteurs et ses chiffres."),
   ("Suivre les liens, pas seulement les nœuds",
    "Chaque flèche porte une étiquette et s’ouvre sur une explication. C’est "
    "là que se trouve l’essentiel pour une dissertation : pourquoi "
    "l’accumulation seule ne suffit pas, pourquoi le résidu conduit à la "
    "croissance endogène, pourquoi les institutions commandent le reste."),
   ("Deux lectures possibles",
    "Pour une copie sur les facteurs de la croissance, suivez mesurer → "
    "accumuler → innover. Pour une copie sur ses limites ou sa soutenabilité, "
    "suivez innover → limites → débats, qui mène à l’arbitrage entre "
    "soutenabilité faible et forte.")],
  [
   nd('coeur', 'La croissance économique', 'coeur',
      "Augmentation durable de la production. Un phénomène récent : avant la "
      "Révolution industrielle, toute hausse de production était absorbée par "
      "la démographie.",
      grp=0,
      defi="La croissance désigne l’augmentation durable de la production d’une "
           "économie, mesurée par le produit intérieur brut. Le cours insiste "
           "sur son caractère historiquement situé : la croissance durable est "
           "un phénomène récent à l’échelle de l’histoire humaine, apparu à la "
           "fin du XVIIIᵉ siècle au Royaume-Uni. Elle se distingue du "
           "développement, qui désigne l’amélioration des conditions de vie et "
           "constitue un changement structurel et social.",
      mec=[("Le régime pré-industriel bloque le niveau de vie",
            "Pendant des siècles les économies sont principalement agricoles, "
            "la productivité est faible et les techniques évoluent lentement. "
            "Toute hausse de production est absorbée par la croissance "
            "démographique : c’est le régime malthusien, où la production "
            "augmente mais la population aussi, ce qui empêche toute "
            "amélioration durable du niveau de vie."),
           ("La rupture industrielle",
            "À la fin du XVIIIᵉ siècle au Royaume-Uni, les innovations "
            "techniques, la mécanisation, le développement de l’industrie et "
            "la division du travail permettent des gains de productivité "
            "durables, une hausse soutenue de la production et une "
            "amélioration progressive du niveau de vie."),
           ("La croissance devient cumulative",
            "Le cours souligne la puissance des effets sur longue période : "
            "même de faibles différences de taux de croissance, maintenues "
            "pendant plusieurs décennies, conduisent à des divergences "
            "considérables de niveau de vie entre pays.")],
      faits=[{'f': "Depuis le XIXᵉ siècle, la production mondiale augmente plus "
                   "rapidement que la population et le PIB par habitant "
                   "progresse sur longue période.",
              'p': "La croissance n’est pas seulement une hausse de la "
                   "production : c’est le premier régime historique où la "
                   "production distance durablement la démographie, ce qui "
                   "rend possible l’élévation du niveau de vie."},
             {'f': "Les trajectoires restent très contrastées selon les "
                   "régions, malgré cette progression mondiale.",
              'p': "La croissance moderne est un phénomène diffusé "
                   "inégalement : c’est précisément ce que les analyses de la "
                   "divergence et du rattrapage cherchent à expliquer."}],
      termes=['croissance economique', 'pib', 'regime malthusien',
              'revolution industrielle'],
      dos=['n1-croissance', 'n1-extensive-intensive']),

   nd('mesure', 'Mesurer la croissance', 'pilier',
      "Croissance extensive ou intensive, productivité globale des facteurs, "
      "croissance effective ou potentielle : quatre distinctions qui changent "
      "le diagnostic.",
      grp=1, par='coeur',
      defi="Mesurer la croissance ne consiste pas seulement à calculer un taux "
           "de variation du PIB. Le cours construit quatre distinctions : la "
           "contribution majeure des facteurs de production correspond à une "
           "croissance extensive, la contribution majeure de la productivité "
           "globale des facteurs à une croissance intensive ; et la croissance "
           "effective, volatile, se distingue de la croissance potentielle, "
           "l’écart entre les deux formant l’output gap.",
      mec=[("Décomposer la croissance",
            "On impute d’abord la part due à l’augmentation des facteurs — "
            "travail et capital — puis on attribue le reste à la productivité "
            "globale des facteurs. Ce résidu est obtenu par soustraction et non "
            "observé directement."),
           ("Distinguer effective et potentielle",
            "La croissance effective dépend de facteurs conjoncturels : niveau "
            "de la demande, confiance des ménages, investissement des "
            "entreprises, politique budgétaire et monétaire, chocs extérieurs. "
            "Elle est donc plus volatile que la croissance potentielle."),
           ("Lire l’output gap",
            "L’écart entre croissance effective et potentielle permet de "
            "relier croissance, chômage et inflation. En période d’expansion "
            "forte, l’effective peut dépasser temporairement le potentiel.")],
      faits=[{'f': "Pendant les Trente Glorieuses, la croissance française "
                   "atteint 5,2 % par an en moyenne, dont 0,5 point pour la "
                   "contribution du facteur travail et 3,1 points pour la "
                   "productivité globale des facteurs.",
              'p': "Environ 60 % de la croissance s’explique par la "
                   "productivité et non par l’accumulation de facteurs : la "
                   "croissance de cette période est intensive, et le cours "
                   "précise que ce niveau n’a jamais été atteint avant ni "
                   "retrouvé après."},
             {'f': "De 2010 à 2021, le Danemark et l’Allemagne connaissent une "
                   "croissance intensive, la France et les États-Unis une "
                   "croissance extensive.",
              'p': "Deux économies de niveau comparable peuvent croître par "
                   "des canaux différents : le régime de croissance dépend de "
                   "choix et d’institutions, pas du seul niveau de "
                   "développement."}],
      opp=[{'t': "Le résidu ne mesurerait rien : attribuer 60 % de la "
                 "croissance à la productivité globale des facteurs "
                 "reviendrait à nommer notre ignorance plutôt qu’à expliquer.",
            'qui': "Le cours rapporte cette critique en l’opposant à la formule "
                   "de Solow sur la « manne tombée du ciel ».",
            'rep': "L’objection est juste mais ne détruit pas le résultat : "
                   "elle établit que la croissance ne vient ni seulement du "
                   "travail ni seulement du capital, ce qui oriente la "
                   "recherche vers l’innovation, l’éducation, l’organisation et "
                   "les institutions — les quatre pistes que le chapitre "
                   "explore ensuite."}],
      aut=[{'n': "Robert Solow",
            'i': "Le progrès technique explique l’essentiel de la croissance de "
                 "long terme, mais il reste exogène au modèle : Solow en parle "
                 "comme d’une manne tombée du ciel."}],
      termes=['croissance extensive', 'croissance intensive',
              'productivite globale des facteurs', 'croissance potentielle',
              'output gap'],
      dos=['n1-pgf', 'n1-extensive-intensive', 'n27-productivite']),

   nd('accumuler', 'Accumuler les facteurs', 'pilier',
      "Investissement et capital font la croissance extensive. Mais "
      "l’accumulation seule bute sur les rendements décroissants.",
      grp=1, par='coeur',
      defi="L’accumulation désigne la croissance du stock de capital par "
           "l’investissement, et l’augmentation de la quantité de travail "
           "employée. Elle constitue la source de la croissance extensive. Le "
           "cours la traite par deux modèles : Harrod-Domar, qui montre une "
           "croissance structurellement déséquilibrée, et Solow, qui montre une "
           "convergence vers un état stationnaire si le progrès technique est "
           "absent.",
      mec=[("L’investissement accroît le stock de capital",
            "L’épargne finance la formation brute de capital fixe, qui "
            "augmente la capacité productive. Dans le modèle de Solow, "
            "l’hypothèse est explicite : la totalité de l’épargne est "
            "investie, S = I."),
           ("Les rendements du capital décroissent",
            "Solow pose une productivité marginale décroissante du capital : "
            "chaque unité supplémentaire rapporte moins que la précédente. "
            "L’accumulation seule ne peut donc pas entretenir indéfiniment la "
            "croissance par tête."),
           ("D’où un état stationnaire",
            "Sans progrès technique, l’économie converge vers un état où "
            "l’investissement ne fait plus que compenser l’usure du capital : "
            "la croissance par tête s’arrête. C’est la raison pour laquelle le "
            "progrès technique devient le facteur décisif.")],
      args=[{'a': "L’accumulation reste la condition matérielle de la "
                  "croissance : sans investissement, aucune amélioration de la "
                  "productivité ne peut être incorporée dans l’appareil "
                  "productif, et le cours fait du capital un moteur historique "
                  "de la croissance aux côtés du travail.",
             'lim': "Elle n’explique pas la croissance de long terme : dans la "
                    "décomposition française des Trente Glorieuses, les "
                    "facteurs n’apportent que 0,5 point sur 5,2 %."}],
      opp=[{'t': "La croissance serait naturellement équilibrée, les marchés "
                 "assurant l’ajustement entre épargne et investissement et la "
                 "convergence vers un sentier stable.",
            'qui': "Position néoclassique que Harrod et Domar contestent, ayant "
                   "assisté à la crise de 1929.",
            'rep': "Chez Harrod-Domar la croissance est déséquilibrée : elle "
                   "dépend de variables exogènes, elle est instable par nature, "
                   "le chemin de la croissance équilibrée est très étroit et "
                   "relève du hasard — c’est l’image du « fil du rasoir ». Les "
                   "facteurs y sont complémentaires et non substituables, et "
                   "aucun mécanisme automatique d’ajustement n’existe."}],
      aut=[{'n': "Roy Harrod",
            'i': "La croissance n’est pas auto-stabilisatrice : le chemin de la "
                 "croissance équilibrée est si étroit qu’il relève du hasard, "
                 "d’où l’image du fil du rasoir."},
           {'n': "Evsey Domar",
            'i': "Avec Harrod, il montre que la croissance dépend de variables "
                 "exogènes et qu’elle est structurellement déséquilibrée, "
                 "contre l’idée néoclassique d’un équilibre naturel des "
                 "marchés."},
           {'n': "Robert Solow",
            'i': "Avec des facteurs substituables, une productivité marginale "
                 "décroissante du capital et des rendements d’échelle "
                 "constants, l’économie converge vers un état stationnaire : "
                 "seul le progrès technique prolonge la croissance par tête."}],
      termes=['accumulation du capital', 'investissement',
              'etat stationnaire', 'fil du rasoir', 'rendements decroissants'],
      dos=['n1-accumulation', 'n1-investissement']),

   nd('innover', 'Innover : la croissance endogène', 'pilier',
      "Le progrès technique cesse d’être une manne extérieure : capital humain, "
      "connaissances, capital public et concurrence le produisent.",
      grp=1, par='coeur',
      defi="Les théories de la croissance endogène expliquent l’origine interne "
           "du progrès technique, que Solow laissait hors du raisonnement. Le "
           "cours en expose quatre versions, qui diffèrent par le capital "
           "spécifique dont l’accumulation entretient la croissance : le "
           "capital humain chez Lucas, la connaissance et la recherche chez "
           "Romer, le capital public chez Barro, l’innovation sous contrainte "
           "de concurrence chez Aghion.",
      mec=[("Identifier un facteur à rendements non décroissants",
            "Toutes ces théories rompent avec les rendements décroissants du "
            "capital physique. Chez Lucas, la productivité marginale de la "
            "formation est constante voire croissante et le capital humain ne "
            "s’use pas comme une machine ; chez Romer, les idées génèrent des "
            "rendements croissants."),
           ("Faire jouer les externalités",
            "Le capital humain d’un individu profite aux autres : un salarié "
            "formé améliore l’efficacité collective, et un environnement riche "
            "en compétences augmente la productivité globale. Chez Romer, ce "
            "sont les spillovers de connaissance."),
           ("Boucler la logique cumulative",
            "Le cours résume l’enchaînement de Romer : recherche et "
            "développement, innovation, nouvelles idées, nouvelles "
            "innovations. La connaissance ne s’use pas, peut être utilisée "
            "simultanément par plusieurs agents et se diffuse : elle est non "
            "rivale, ce qui change la logique des rendements."),
           ("Introduire la sélection par la concurrence",
            "Chez Aghion, le tissu productif se renouvelle au gré des "
            "innovations, chacune rendant l’ancienne technologie obsolète. Le "
            "taux de croissance dépend alors de deux déterminants : "
            "l’intensité de la recherche et le régime de concurrence.")],
      args=[{'a': "La croissance devient un objet de politique économique : si "
                  "elle dépend de la formation, de la recherche et du capital "
                  "public, alors l’éducation, le financement de la recherche "
                  "et l’investissement public en deviennent les leviers "
                  "directs.",
             'lim': "Le cours nuance deux fois : toutes les dépenses de "
                    "recherche ne débouchent pas sur des innovations, les "
                    "découvertes étant plus ou moins aléatoires, et "
                    "l’innovation ne décolle pas sans un bon régime de "
                    "concurrence."}],
      aut=[{'n': "Robert Lucas",
            'i': "La croissance ne vient pas d’un facteur extérieur mais de "
                 "l’accumulation du capital humain, dont les rendements ne sont "
                 "pas nécessairement décroissants et qui génère des "
                 "externalités positives."},
           {'n': "Gary Becker",
            'i': "Il popularise le capital humain, défini comme le stock de "
                 "caractéristiques physiques et intellectuelles incorporées aux "
                 "individus et valorisables économiquement : ce n’est plus la "
                 "quantité de travail qui compte mais sa qualité."},
           {'n': "Paul Romer",
            'i': "L’accumulation de connaissances et la recherche produisent le "
                 "progrès technique ; la connaissance étant non rivale, elle "
                 "engendre des rendements croissants et des spillovers."},
           {'n': "Robert Barro",
            'i': "Le capital public productif est le moteur de la croissance : "
                 "il existe un niveau optimal, des dépenses trop faibles "
                 "produisant un sous-investissement collectif et des dépenses "
                 "excessives un effet d’éviction du capital privé."},
           {'n': "Philippe Aghion",
            'i': "Le taux de croissance dépend de l’intensité de la recherche "
                 "et du régime de concurrence, chaque innovation rendant "
                 "l’ancienne technologie obsolète par destruction créatrice."}],
      termes=['croissance endogene', 'capital humain', 'spillovers',
              'recherche et developpement', 'destruction creatrice'],
      dos=['n27-innovation', 'n27-capital-humain', 'n1-endogene']),

   nd('institutions', 'Les institutions', 'pilier',
      "Règles formelles et informelles : elles créent les incitations et pèsent "
      "sur les coûts de transaction. La croissance en dépend plus que de "
      "l’accumulation.",
      grp=1, par='coeur',
      defi="Les institutions sont l’ensemble des règles formelles — lois, "
           "droits de propriété, contrats — et informelles — coutumes, "
           "traditions — qui encadrent le comportement des individus. Le cours "
           "en fait le facteur explicatif des différences durables de "
           "développement entre pays, que l’accumulation de capital et le "
           "progrès technique n’expliquent pas à eux seuls.",
      mec=[("Les règles créent des incitations",
            "Elles orientent les choix des agents et réduisent ou augmentent "
            "l’incertitude. Les individus restent rationnels, mais leur "
            "rationalité s’exerce dans un cadre institutionnel donné."),
           ("Elles pèsent sur les coûts de transaction",
            "Le fonctionnement du marché n’est jamais gratuit : les échanges "
            "impliquent des coûts d’information, de négociation, de contrôle et "
            "d’exécution des contrats. De bonnes institutions les réduisent, de "
            "mauvaises les augmentent."),
           ("Elles sécurisent l’investissement de long terme",
            "Si les droits de propriété sont protégés et les règles stables et "
            "crédibles, l’horizon de calcul s’allonge. Le cours relie ainsi, "
            "dans le cas anglais, la sécurité juridique à la confiance des "
            "investisseurs et à l’essor du crédit."),
           ("Elles s’installent dans la durée",
            "North parle de dépendance au sentier : les institutions évoluent "
            "lentement et les choix passés conditionnent fortement les "
            "trajectoires futures, ce qui peut enfermer une économie dans un "
            "équilibre inefficace durable.")],
      faits=[{'f': "La part anglaise de la production industrielle mondiale "
                   "passe d’environ 2 % en 1750 à 23 % en 1880, après la "
                   "limitation du pouvoir royal, le renforcement du Parlement "
                   "et l’instauration de l’État de droit.",
              'p': "Le cours en tire explicitement que l’explication n’est pas "
                   "seulement géographique ni liée au charbon, mais "
                   "institutionnelle : c’est le cas d’école de la thèse."},
             {'f': "Le cours résume le mécanisme : institutions inclusives, "
                   "donc confiance, investissement, innovation, croissance "
                   "durable ; institutions extractives, donc rente, blocage, "
                   "stagnation.",
              'p': "La chaîne causale passe par des grandeurs observables, la "
                   "confiance et l’investissement, et non par un effet direct "
                   "des règles sur la production."}],
      opp=[{'t': "La typologie entre institutions inclusives et extractives "
                 "serait démentie par les faits : la Chine combine "
                 "centralisation politique, parti unique et absence de "
                 "pluralisme avec une croissance très forte.",
            'qui': "Le cours formule lui-même cette objection comme première "
                   "limite du modèle d’Acemoglu et Robinson.",
            'rep': "Le cours ne la résout pas et la présente comme un débat "
                   "majeur. On peut distinguer institutions politiques et "
                   "institutions économiques : la sécurité des contrats et des "
                   "investissements peut être assurée sans pluralisme "
                   "politique, ce qui conduit à préciser quelle dimension "
                   "institutionnelle importe pour la croissance."}],
      aut=[{'n': "Douglass North",
            'i': "La croissance dépend moins de l’accumulation de capital et "
                 "des économies d’échelle que de la qualité des institutions, "
                 "qui réduisent les coûts de transaction et l’incertitude."},
           {'n': "Daron Acemoglu",
            'i': "Les institutions inclusives favorisent innovation, "
                 "investissement, mobilité sociale et entrepreneuriat ; les "
                 "institutions extractives freinent l’initiative et la "
                 "diffusion du progrès."},
           {'n': "James A. Robinson",
            'i': "Avec Acemoglu, il explique la précocité anglaise moins par "
                 "les seules ressources que par des institutions relativement "
                 "plus favorables à l’innovation et à l’investissement."}],
      termes=['institutions', 'droits de propriete', 'couts de transaction',
              'institutions inclusives', 'dependance au sentier'],
      dos=['n27-institutions', 'n26-institutions-comportements']),

   nd('limites', 'Les limites de la croissance', 'pilier',
      "Rendements décroissants, état stationnaire, stagnation séculaire, "
      "contrainte écologique : quatre familles de limites, de nature "
      "différente.",
      grp=1, par='coeur',
      defi="Les limites de la croissance sont de quatre ordres dans le cours. "
           "Une limite technique, les rendements décroissants, qui conduit à "
           "l’état stationnaire. Une limite historique et démographique, la "
           "stagnation séculaire. Une limite écologique, l’épuisement des "
           "ressources et la question de la soutenabilité. Une limite "
           "distributive enfin, puisque la croissance peut se poursuivre sans "
           "profiter au revenu médian.",
      mec=[("La limite technique",
            "La productivité marginale décroissante du capital fait converger "
            "l’économie vers un état stationnaire si le progrès technique est "
            "absent. C’est la limite que les théories de la croissance "
            "endogène cherchent à lever."),
           ("La limite de régime",
            "La crise de 2008 marque une rupture nette : chute du PIB, hausse "
            "du chômage, montée du ratio dette publique sur PIB, ralentissement "
            "durable de la croissance potentielle. Même lorsque la reprise "
            "intervient, elle reste plus faible que lors des cycles "
            "précédents."),
           ("La limite écologique",
            "Le rapport du Club de Rome en 1972 met en garde contre "
            "l’épuisement des ressources et avance l’idée de limites physiques "
            "à la croissance. La question devient alors celle de la "
            "soutenabilité : peut-on préserver la capacité de croissance sans "
            "détruire certains capitaux, notamment le capital naturel ?")],
      faits=[{'f': "Après 2008, les gains de productivité ralentissent, la "
                   "croissance reste faible et l’investissement demeure "
                   "insuffisant dans plusieurs pays, alors qu’on croyait que la "
                   "révolution des technologies de l’information garantirait "
                   "une croissance durable.",
              'p': "La crise remet en question l’idée selon laquelle "
                   "l’innovation technologique suffit à assurer une croissance "
                   "forte et durable, ce qui alimente l’hypothèse d’une "
                   "stagnation structurelle plutôt que d’un cycle défavorable."},
             {'f': "Le rapport Brundtland, en 1987, définit le développement "
                   "durable comme un développement qui répond aux besoins du "
                   "présent sans compromettre la capacité des générations "
                   "futures à répondre aux leurs.",
              'p': "Le critère d’évaluation se déplace du niveau de production "
                   "vers la transmission des capacités, ce qui rend possible "
                   "l’élargissement de la notion de capital à six formes."}],
      aut=[{'n': "Alvin Hansen",
            'i': "Une économie peut connaître un ralentissement durable de sa "
                 "croissance, qu’il qualifie de stagnation séculaire, et que le "
                 "cours relie notamment aux évolutions démographiques."},
           {'n': "Daniel Cohen",
            'i': "Dans Le monde est clos et le désir infini (2015), il diffuse "
                 "en France l’idée d’un paradoxe entre l’intensité des "
                 "innovations et la faiblesse des gains de croissance "
                 "observés."},
           {'n': "Dennis Meadows",
            'i': "Le rapport Limits to Growth met en garde contre l’épuisement "
                 "des ressources et avance l’idée de limites physiques à la "
                 "croissance, ce qui ouvre le débat sur la soutenabilité."}],
      termes=['etat stationnaire', 'stagnation seculaire', 'soutenabilite',
              'limites de la croissance', 'capital naturel'],
      dos=['n27-soutenabilite', 'n1-croissance']),

   nd('debats', 'Les débats ouverts', 'debat',
      "Trois questions que le cours ne tranche pas : la croissance réduit-elle "
      "les inégalités, est-elle soutenable, et quel rôle pour l’État ?",
      grp=1, par='coeur',
      defi="Le cours pose explicitement trois débats que les théories de la "
           "croissance laissent ouverts : l’équilibre de long terme est-il la "
           "règle ou l’exception, quels sont les facteurs de croissance et "
           "quelle place y tient le progrès technique, et quel est le rôle de "
           "l’État. Toutes les théories de la croissance peuvent se lire à "
           "travers ces trois questions communes, même si leurs réponses "
           "diffèrent.",
      mec=[("Croissance et inégalités",
            "Kuznets propose une relation en U inversé : les inégalités "
            "augmentent au début du développement puis diminuent à un stade "
            "avancé. Mais le cours souligne par un « mais surtout » que la "
            "phase descendante repose sur le développement de la "
            "redistribution, la hausse des recettes fiscales et les politiques "
            "sociales."),
           ("Croissance et environnement",
            "Le débat se ramène à une question technique : les capitaux "
            "sont-ils substituables ? La soutenabilité faible le soutient, la "
            "soutenabilité forte le nie pour certains capitaux naturels."),
           ("Croissance et État",
            "Barro montre qu’il existe un niveau optimal de capital public, et "
            "Aghion assigne à l’État quatre fonctions : protéger les droits de "
            "propriété, garantir la concurrence, amortir les effets de la "
            "destruction créatrice et orienter l’innovation.")],
      opp=[{'t': "La réduction des inégalités serait presque mécanique à long "
                 "terme : il suffirait d’atteindre un stade avancé de "
                 "développement pour que l’éventail des revenus se resserre de "
                 "lui-même.",
            'qui': "Lecture mécanique de la courbe de Kuznets, que le cours "
                   "identifie et récuse.",
            'rep': "Le cours répond que la réduction des inégalités n’est pas "
                   "automatique : elle dépend du niveau de redistribution, du "
                   "système fiscal, des institutions et du degré de protection "
                   "sociale. Et depuis les années 1980, la hausse des "
                   "inégalités de revenus, la concentration des patrimoines et "
                   "l’explosion du top 1 % contredisent la phase descendante."}],
      aut=[{'n': "Simon Kuznets",
            'i': "La relation entre croissance et inégalités suit une courbe en "
                 "U inversé, hypothèse formulée en 1955 à partir des inégalités "
                 "américaines observées entre 1913 et 1948."},
           {'n': "Branko Milanovic",
            'i': "Les inégalités entre pays diminuent tandis que les inégalités "
                 "à l’intérieur des pays augmentent : la courbe de l’éléphant "
                 "en donne la mesure pour 1988-2008."}],
      termes=['courbe de kuznets', 'soutenabilite faible',
              'soutenabilite forte', 'inegalites'],
      dos=['n22-courbe-kuznets', 'n27-inegalites', 'n27-soutenabilite']),

   nd('pgf', 'Le résidu de Solow', 'detail',
      "La productivité globale des facteurs : 3,1 points sur 5,2 % en France, "
      "soit 60 % de la croissance — mais obtenus par soustraction.",
      grp=2, par='mesure',
      defi="La productivité globale des facteurs est la part de la croissance "
           "qui n’est pas imputable à l’augmentation des quantités de travail "
           "et de capital. Elle est donc obtenue par soustraction, ce qui en "
           "fait à la fois l’indicateur le plus important de l’analyse de la "
           "croissance et le plus fragile théoriquement.",
      mec=[("Imputer les facteurs",
            "On calcule la contribution de l’augmentation du facteur travail, "
            "soit 0,5 point pour la France des Trente Glorieuses, puis celle du "
            "capital, et l’on attribue le reste à la productivité globale des "
            "facteurs."),
           ("Interpréter le reste",
            "Le cours rapporte deux lectures opposées : Solow parlait du "
            "progrès technique comme d’une manne tombée du ciel, une richesse "
            "qui apparaît sans que l’on sache précisément d’où elle vient ; "
            "d’autres économistes estiment que la productivité globale des "
            "facteurs mesure surtout notre ignorance."),
           ("Chercher ce qu’il contient",
            "On sait que la croissance ne vient ni seulement du travail ni "
            "seulement du capital, mais on peine à décomposer finement ce qui "
            "relève de l’organisation et des compétences. C’est précisément "
            "l’objet des théories de la croissance endogène.")],
      faits=[{'f': "Pour la France des Trente Glorieuses : productivité globale "
                   "des facteurs de 3,1 points sur une croissance totale de "
                   "5,2 %, soit un rapport de 3,1/5,2 ≈ 60 %.",
              'p': "Le calcul est explicite dans le cours : c’est le chiffre à "
                   "retenir pour établir que la croissance de cette période est "
                   "intensive."}],
      termes=['productivite globale des facteurs', 'residu de solow',
              'manne tombee du ciel'],
      dos=['n1-pgf']),

   nd('deversement', 'Le déversement sectoriel', 'detail',
      "Les gains de productivité inégaux déplacent l’emploi : agriculture vers "
      "industrie, puis industrie vers services.",
      grp=2, par='mesure',
      defi="Le déversement désigne le déplacement de la main-d’œuvre d’un "
           "secteur vers un autre sous l’effet de gains de productivité "
           "inégaux. Le cours décrit une chaîne historique typique en deux "
           "temps : de l’agriculture vers l’industrie aux XIXᵉ et début du XXᵉ "
           "siècle, puis de l’industrie vers les services aux XXᵉ et XXIᵉ "
           "siècles.",
      mec=[("Les secteurs productifs libèrent de la main-d’œuvre",
            "Les secteurs dont la productivité augmente le plus vite libèrent "
            "de la main-d’œuvre, qui se déverse vers un autre secteur. La "
            "tertiarisation est donc une conséquence logique de gains de "
            "productivité inégaux et de la réallocation de la main-d’œuvre."),
           ("La baisse des prix réels libère du revenu",
            "Chez Fourastié, les gains de productivité industriels rendent la "
            "production moins coûteuse, les prix réels baissent, les revenus "
            "réels augmentent et la demande de services augmente, d’où le "
            "déversement de l’emploi vers les services."),
           ("Le progrès technique ne détruit pas l’emploi net",
            "Sauvy répond dans La Machine et le chômage (1980) à l’idée que les "
            "machines détruiraient l’emploi : le progrès technique détruit des "
            "emplois dans certains secteurs mais en crée dans d’autres, le "
            "chômage ne venant pas mécaniquement des machines.")],
      aut=[{'n': "Jean Fourastié",
            'i': "Les gains de productivité industriels abaissent les prix "
                 "réels, élèvent les revenus réels et déplacent la demande vers "
                 "les services : Le Grand Espoir du XXᵉ siècle, 1949."},
           {'n': "Alfred Sauvy",
            'i': "Le progrès technique détruit des emplois dans certains "
                 "secteurs mais en crée dans d’autres : le chômage ne vient pas "
                 "mécaniquement des machines."}],
      termes=['deversement', 'tertiarisation', 'gains de productivite'],
      dos=['n27-transformation-structurelle']),

   nd('etapes', 'Décollage et rattrapage', 'detail',
      "Rostow et Gerschenkron : la croissance comme processus historique de "
      "transformation structurelle, et la question de son universalité.",
      grp=2, par='accumuler',
      defi="Rostow décompose la croissance en étapes successives dont le "
           "décollage est le moment décisif : passage d’une économie agricole à "
           "une économie industrielle et transformation profonde du système "
           "productif. Gerschenkron conteste l’universalité de ce schéma en "
           "montrant que les pays qui s’industrialisent tardivement ne "
           "reproduisent pas la trajectoire des pionniers.",
      mec=[("La société traditionnelle",
            "Économie reposant sur l’agriculture, la terre étant la principale "
            "source de richesse ; faible progrès technique ; société stable qui "
            "se reproduit à l’identique, avec une absence de mobilité "
            "sociale ; croissance très faible voire inexistante."),
           ("Les conditions préalables et le décollage",
            "La phase préalable, qui peut durer jusqu’à un siècle, se "
            "caractérise par la valorisation du profit, le développement de "
            "l’entrepreneuriat et l’essor de l’épargne et de l’investissement. "
            "Le décollage est ensuite le moment décisif du passage à une "
            "économie industrielle."),
           ("La consommation de masse",
            "L’étape finale associe amélioration des conditions de vie, "
            "développement du rôle de l’État avec l’État-providence, "
            "tertiarisation de l’économie et hausse rapide du revenu par tête, "
            "ce qui correspond surtout à l’après-1945 dans les pays "
            "développés.")],
      opp=[{'t': "Toutes les économies suivraient la même séquence d’étapes, de "
                 "la société traditionnelle à la consommation de masse.",
            'qui': "Lecture linéaire du modèle de Rostow, que le cours "
                   "interroge face à la diversité historique des trajectoires "
                   "d’industrialisation.",
            'rep': "Gerschenkron soutient que les pays tardifs ne reproduisent "
                   "pas la trajectoire des pionniers. Le cours relève toutefois "
                   "leur accord de fond : tous deux voient la croissance comme "
                   "un processus historique de transformation structurelle "
                   "fondé sur l’industrialisation, reconnaissent la possibilité "
                   "du rattrapage et insistent sur la dynamique cumulative."}],
      aut=[{'n': "Walt Whitman Rostow",
            'i': "La croissance passe par une succession d’étapes dont le "
                 "décollage est le moment décisif, marquant le passage d’une "
                 "économie agricole à une économie industrielle."},
           {'n': "Alexander Gerschenkron",
            'i': "Les pays qui s’industrialisent tardivement ne reproduisent "
                 "pas la trajectoire des pionniers, ce qui conteste "
                 "l’universalité du schéma en étapes."}],
      termes=['decollage', 'take-off', 'rattrapage',
              'transformation structurelle'],
      dos=['n27-industrialisation']),

   nd('concurrence', 'Concurrence et innovation', 'detail',
      "La concurrence stimule l’innovation, mais les firmes installées peuvent "
      "l’étouffer : d’où un rôle précis pour l’État.",
      grp=2, par='innover',
      defi="Dans le modèle d’Aghion, la concurrence est le second déterminant "
           "du taux de croissance, aux côtés de l’intensité de la recherche. "
           "Elle est stimulante mais menacée : elle pousse les firmes à se "
           "dépasser pour rester leaders, mais les firmes leaders peuvent "
           "vouloir la limiter en créant des barrières à l’entrée.",
      mec=[("La concurrence pousse à innover",
            "Elle contraint les firmes à se dépasser pour rester leaders. "
            "L’ouverture internationale produit le même effet : concurrence "
            "accrue, pression sur les marges, recherche de productivité, "
            "innovation, disparition des producteurs les moins efficaces."),
           ("Mais les leaders peuvent la bloquer",
            "Aghion souligne que certaines grandes entreprises peuvent freiner "
            "l’innovation en empêchant l’entrée de nouveaux concurrents, par "
            "des barrières, du lobbying et la défense de leurs rentes."),
           ("D’où quatre fonctions pour l’État",
            "Protéger les droits de propriété par les brevets afin de rendre "
            "rentable l’investissement en recherche ; garantir la concurrence "
            "en empêchant les leaders d’étouffer l’entrée ; amortir les effets "
            "négatifs de la destruction créatrice — chômage, reconversions, "
            "chocs locaux ; orienter l’innovation vers de nouvelles directions "
            "comme les innovations vertes.")],
      args=[{'a': "La politique d’innovation doit être différenciée selon la "
                  "distance à la frontière technologique : un pays en "
                  "rattrapage peut justifier davantage de ciblage, un pays "
                  "proche de la frontière doit privilégier la concurrence, "
                  "l’entrée et l’expérimentation.",
             'lim': "Même à la frontière, l’intervention ne disparaît pas "
                    "puisque les marchés présentent des défaillances : le "
                    "critère fournit un dosage et non une règle "
                    "d’abstention."}],
      aut=[{'n': "Philippe Aghion",
            'i': "Certaines grandes entreprises peuvent freiner l’innovation en "
                 "empêchant l’entrée de nouveaux concurrents, ce qui justifie "
                 "que l’État lève les obstacles à la destruction créatrice."},
           {'n': "Mariana Mazzucato",
            'i': "Une grande partie des technologies qui deviennent ensuite "
                 "rentables dans le secteur privé repose initialement sur des "
                 "investissements publics risqués."}],
      termes=['concurrence', 'destruction creatrice', 'frontiere technologique',
              'politique industrielle'],
      dos=['n27-concurrence', 'n27-innovation']),

   nd('capitaux', 'Les six capitaux', 'detail',
      "Physique, humain, naturel, technologique, social, institutionnel : la "
      "croissance n’est pas seulement une accumulation de machines.",
      grp=2, par='limites',
      defi="Pour penser la soutenabilité, le cours élargit la notion de "
           "capital, défini comme un stock d’actifs mobilisables dans le "
           "processus productif et capables de générer des revenus futurs. Il "
           "distingue six formes : capital physique, humain, naturel, "
           "technologique, social et institutionnel. La croissance repose donc "
           "sur un ensemble de ressources complémentaires.",
      mec=[("Définir chaque capital",
            "Le capital technologique est le stock de connaissances "
            "mobilisable pour produire plus efficacement : connaissances "
            "scientifiques, procédés de production, résultats de la recherche. "
            "Le capital social désigne les réseaux, la réputation, les "
            "relations, la confiance et la capacité à mobiliser des "
            "partenaires. Le capital institutionnel regroupe les règles et les "
            "lois."),
           ("Poser la question de la substituabilité",
            "Le cours qualifie cette question de cœur théorique du débat : si "
            "les capitaux sont substituables, la destruction de l’un peut être "
            "compensée par l’accumulation d’un autre ; sinon, elle est une "
            "perte nette."),
           ("Trancher entre deux visions",
            "La soutenabilité faible, de tradition néoclassique, considère que "
            "les différentes formes de capital sont substituables. La "
            "soutenabilité forte le nie : certains capitaux naturels sont "
            "irremplaçables et doivent être préservés en tant que tels.")],
      args=[{'a': "L’élargissement de la notion de capital permet de poser la "
                  "soutenabilité comme une question de préservation de stocks "
                  "et non comme une limitation du niveau de production, ce qui "
                  "la rend argumentable économiquement.",
             'lim': "Le cours ne fournit pas d’indicateur pour le capital "
                    "naturel, social ou institutionnel : la comptabilité "
                    "élargie reste une intention théorique."}],
      termes=['capital naturel', 'capital social', 'capital institutionnel',
              'soutenabilite', 'substituabilite'],
      dos=['n27-soutenabilite', 'n26-marche-etat']),

   nd('kuznets', 'La courbe de Kuznets', 'detail',
      "Un U inversé entre croissance et inégalités — dont la phase descendante "
      "repose « surtout » sur la redistribution.",
      grp=2, par='debats',
      defi="Kuznets formule en 1955, à partir de l’évolution des inégalités aux "
           "États-Unis entre 1913 et 1948, l’hypothèse d’une relation en cloche "
           "entre croissance et inégalités : les inégalités augmentent au début "
           "du développement puis diminuent à un stade avancé, soit une courbe "
           "en U inversé.",
      mec=[("La phase de hausse",
            "Au début du développement, le passage d’une économie agricole à "
            "une économie industrielle crée des différences de productivité "
            "importantes et des salaires industriels plus élevés : les écarts "
            "se creusent entre secteurs."),
           ("La phase de baisse",
            "À un stade avancé jouent la généralisation de l’éducation, la "
            "diffusion du progrès technique, l’urbanisation complète et la "
            "montée de la classe moyenne. Mais le cours ajoute un « mais "
            "surtout » : développement de la redistribution, hausse des "
            "recettes fiscales, mise en place de politiques sociales. L’État "
            "corrige les inégalités produites par le marché."),
           ("Le démenti contemporain",
            "Depuis les années 1980, dans de nombreux pays développés, on "
            "observe une hausse des inégalités de revenus, une forte "
            "concentration des patrimoines et une explosion du top 1 % : la "
            "dynamique récente contredit la phase descendante prévue.")],
      faits=[{'f': "L’hypothèse repose sur l’observation d’un seul pays, les "
                   "États-Unis, sur trente-cinq ans, de 1913 à 1948 — une "
                   "période marquée par deux guerres et la crise de 1929.",
              'p': "C’est l’argument le plus solide contre la généralisation de "
                   "la courbe : sa base empirique est étroite et "
                   "historiquement très particulière."}],
      aut=[{'n': "Simon Kuznets",
            'i': "La relation entre croissance et inégalités suit une courbe en "
                 "cloche, mais la phase descendante repose surtout sur la "
                 "redistribution et les politiques sociales."}],
      termes=['courbe de kuznets', 'u inverse', 'redistribution'],
      dos=['n22-courbe-kuznets', 'n23-moyennisation'])
  ],
  [
   ln('coeur', 'mesure', 'se constate d’abord',
      "On ne peut discuter des causes de la croissance qu’après avoir choisi "
      "comment la mesurer : selon que l’on retient les facteurs ou la "
      "productivité globale des facteurs, la même croissance de 5,2 % devient "
      "extensive ou intensive, et le diagnostic sur ses moteurs change "
      "entièrement.", 'mesure'),
   ln('coeur', 'accumuler', 'premier moteur',
      "L’accumulation de capital et l’augmentation du travail sont la source "
      "immédiate de la croissance : c’est la réponse que donnent Harrod-Domar "
      "et Solow, chacun avec sa conclusion — instabilité structurelle pour le "
      "premier, convergence vers un état stationnaire pour le second."),
   ln('mesure', 'innover', 'le résidu oblige à chercher ailleurs',
      "La décomposition attribue 60 % de la croissance française des Trente "
      "Glorieuses à un résidu que l’on n’observe pas directement. C’est "
      "exactement ce vide que les théories de la croissance endogène viennent "
      "combler en expliquant d’où vient le progrès technique.", 'cause'),
   ln('accumuler', 'innover', 'les rendements décroissants imposent le relais',
      "Si le capital physique subit des rendements décroissants, "
      "l’accumulation seule conduit à l’état stationnaire. Il faut donc un "
      "facteur dont les rendements ne décroissent pas : le capital humain chez "
      "Lucas, la connaissance non rivale chez Romer, le capital public chez "
      "Barro.", 'limite'),
   ln('institutions', 'accumuler', 'sécurisent l’investissement',
      "Des droits de propriété protégés et des règles stables allongent "
      "l’horizon de calcul des investisseurs. Le cours relie explicitement, "
      "dans le cas anglais, la sécurité juridique à la confiance des "
      "investisseurs puis à l’essor du crédit, condition de l’accumulation.",
      'conditionne'),
   ln('institutions', 'innover', 'rendent l’innovation rentable',
      "Protéger l’innovation par les brevets rend rentable l’investissement en "
      "recherche, tandis que garantir la concurrence empêche les firmes "
      "installées de bloquer le renouvellement. L’institution est donc une "
      "condition de l’innovation et non son décor.", 'conditionne'),
   ln('accumuler', 'limites', 'bute sur les rendements décroissants',
      "La productivité marginale décroissante du capital fait converger "
      "l’économie vers un état stationnaire : la limite n’est pas ajoutée de "
      "l’extérieur, elle est contenue dans la logique même de l’accumulation.",
      'limite'),
   ln('innover', 'limites', 'ne lève pas toutes les limites',
      "L’innovation repousse la limite technique mais pas la limite "
      "écologique : après 2008, les gains de productivité ralentissent malgré "
      "la révolution numérique, ce qui remet en cause l’idée que l’innovation "
      "suffit à assurer une croissance forte et durable.", 'limite'),
   ln('limites', 'debats', 'ouvrent le débat normatif',
      "Dès que l’on admet des limites, la question cesse d’être « comment "
      "croître » pour devenir « quel type de croissance voulons-nous » : "
      "croissance inclusive, développement durable, croissance verte. Le cours "
      "opère explicitement ce passage.", 'cause'),
   ln('mesure', 'pgf', 'se décompose en',
      "La productivité globale des facteurs est le terme central de la "
      "décomposition : c’est elle qui fait basculer le diagnostic d’une "
      "croissance extensive à une croissance intensive, et c’est elle que l’on "
      "mesure le moins bien.", 'mesure'),
   ln('mesure', 'deversement', 'se lit aussi par secteur',
      "Des gains de productivité inégaux entre secteurs déplacent l’emploi "
      "sans réduire la production : la tertiarisation n’est donc pas un déclin "
      "mais la conséquence logique d’une productivité industrielle qui "
      "progresse plus vite que celle des services.", 'cause'),
   ln('accumuler', 'etapes', 's’inscrit dans une histoire',
      "L’accumulation ne commence pas n’importe quand : chez Rostow, le "
      "décollage suppose une phase préalable de valorisation du profit, "
      "d’entrepreneuriat et d’essor de l’épargne, qui peut durer jusqu’à un "
      "siècle.", 'conditionne'),
   ln('innover', 'concurrence', 'dépend du régime de concurrence',
      "Chez Aghion, l’intensité de la recherche ne suffit pas : l’innovation ne "
      "décolle pas sans un bon régime de concurrence, et les firmes leaders "
      "peuvent précisément chercher à l’étouffer en empêchant l’entrée de "
      "nouveaux concurrents.", 'conditionne'),
   ln('limites', 'capitaux', 'se pose en termes de stocks',
      "Élargir la notion de capital à six formes transforme la question des "
      "limites : il ne s’agit plus de brider la production mais de savoir si "
      "l’on peut préserver la capacité de croissance sans détruire certains "
      "capitaux, notamment naturel.", 'cause'),
   ln('debats', 'kuznets', 'se cristallise sur',
      "La courbe de Kuznets est le point de rencontre des trois débats : elle "
      "porte sur la croissance, sur les inégalités et sur le rôle de l’État, "
      "puisque sa phase descendante repose « surtout » sur la redistribution "
      "et les politiques sociales.", 'mesure'),
   ln('capitaux', 'debats', 'alimente l’arbitrage',
      "La question de la substituabilité des capitaux est ce qui sépare "
      "soutenabilité faible et soutenabilité forte : selon la réponse, la "
      "destruction du capital naturel est un arbitrage acceptable ou une perte "
      "irréversible.", 'oppose')
  ],
  fam='Croissance et développement')
