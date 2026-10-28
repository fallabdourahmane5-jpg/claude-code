# -*- coding: utf-8 -*-
"""Visualisation 17 — Les grands courants de la pensée (type courants)."""

from vz_base import v, nd, ln

v('vz-courants', 'Les grands courants de la pensée économique',
  'Chapitre 3 · filiations et ruptures',
  'courants',
  "Les courants ne se succèdent pas : ils se répondent. Cette visualisation "
  "les dispose par familles, de gauche à droite, et montre par les flèches "
  "ce que chacun reprend du précédent et ce qu’il lui conteste. Une "
  "dissertation sur un auteur gagne toujours à le situer dans cette chaîne "
  "d’objections plutôt qu’à l’exposer isolément.",
  [("Lire les flèches, pas seulement les colonnes",
    "Chaque courant naît d’une objection adressée au précédent. Identifier "
    "cette objection — sur la valeur, sur l’équilibre, sur la monnaie, sur "
    "les institutions — donne la structure d’une copie d’histoire de la "
    "pensée."),
   ("Ce que Keynes appelle « les classiques »",
    "Pour Keynes, les classiques regroupent les classiques historiques et "
    "les néoclassiques : ce qui les unit est la confiance fondamentale dans "
    "l’autorégulation du marché. La catégorie est polémique, il faut "
    "l’annoncer comme telle."),
   ("Orthodoxie et hétérodoxie",
    "Veblen, North, Aglietta et Boyer critiquent l’orthodoxie néoclassique "
    "sans se rattacher au marxisme : l’hétérodoxie n’est pas une position "
    "unique mais un ensemble de refus communs — de l’homo œconomicus, de "
    "l’équilibre abstrait, de l’économie hors histoire.")],
  [
   # ------------------------------------------- colonne 1 : avant les classiques
   nd('prelude', 'Mercantilistes et physiocrates', 'pilier',
      "D’où vient la richesse ? Du commerce extérieur et des métaux "
      "précieux, ou de la terre seule ? La première controverse "
      "économique.",
      grp=1,
      defi="Avant l’économie politique classique, deux réponses s’opposent "
           "sur l’origine de la richesse. Les mercantilistes la situent dans "
           "le commerce extérieur et l’accumulation de métaux précieux, ce "
           "qui justifie une politique active de l’État pour dégager un "
           "excédent commercial. Les physiocrates soutiennent au contraire "
           "que l’agriculture est la seule activité réellement productive, "
           "car la terre crée un produit net.",
      mec=[("La richesse comme stock à capter",
            "Chez les mercantilistes, le commerce est un jeu où le gain de "
            "l’un correspond à la perte de l’autre : l’excédent commercial "
            "devient un objectif de puissance, ce qui légitime "
            "l’intervention de l’État."),
           ("Le produit net de la terre",
            "Quesnay construit le premier circuit de l’économie : la terre "
            "seule dégage un surplus au-delà de ce qu’elle consomme, les "
            "autres activités ne faisant que transformer."),
           ("Ce que l’analyse annonce",
            "L’importance accordée à la terre annonce certains thèmes de "
            "l’économie classique : Ricardo reprend cette centralité mais en "
            "montre la limite avec la loi des rendements décroissants.")],
      opp=[{'t': "Le modèle physiocratique suppose une agriculture "
                 "parfaitement régulière, et ignore les variations "
                 "climatiques, les crises agricoles et les rendements "
                 "décroissants.",
            'qui': "le cours, reprenant la critique ricardienne",
            'rep': "L’objection ne détruit pas l’apport : elle montre que la "
                   "terre, source de richesse, peut aussi devenir une "
                   "contrainte pour la croissance lorsqu’on exploite des "
                   "terres de moins en moins fertiles."}],
      aut=[{'n': "François Quesnay",
            'i': "L’agriculture est la seule activité réellement productive, "
                 "car la terre dégage un produit net."},
           {'n': "David Ricardo",
            'i': "Lorsque l’on exploite des terres de moins en moins "
                 "fertiles, les gains de production diminuent : c’est la loi "
                 "des rendements décroissants."}],
      termes=['mercantilisme', 'physiocrates', 'produit net',
              'tableau economique'],
      dos=['n26-production-repartition', 'n26-marche-etat']),

   # -------------------------------------- colonne 2 : les classiques et Marx
   nd('classiques', 'Les classiques', 'pilier',
      "Smith, Ricardo, Malthus, Say : le travail au centre, la main "
      "invisible, la loi des débouchés. La richesse se produit, elle ne se "
      "capte pas.",
      grp=2,
      defi="L’économie politique classique réunit Adam Smith, David Ricardo, "
           "Thomas Malthus et Jean-Baptiste Say. Elle déplace la question de "
           "la richesse : celle-ci n’est plus un stock à capter mais un flux "
           "produit par le travail. Son argument central est que la poursuite "
           "des intérêts particuliers, encadrée par la concurrence, produit "
           "un résultat collectif satisfaisant sans qu’aucune autorité ait à "
           "l’organiser.",
      mec=[("La division du travail et la main invisible",
            "La spécialisation élève la productivité, et la concurrence fait "
            "que la poursuite des intérêts particuliers sert l’intérêt "
            "général : le marché s’autorégule par les prix."),
           ("La répartition entre salaires, profits et rentes",
            "L’analyse porte sur la production et sur la répartition de ce "
            "qui est produit : c’est la question que le siècle suivant "
            "héritera, et sur laquelle il se divisera."),
           ("La loi des débouchés",
            "Toute offre crée sa propre demande : la crise générale de "
            "surproduction est exclue par construction, ce qui fonde la "
            "confiance dans l’ajustement spontané.")],
      aut=[{'n': "Adam Smith",
            'i': "La conduite des marchés est naturellement harmonieuse parce "
                 "que la concurrence se trouve au cœur du fonctionnement de "
                 "l’économie."},
           {'n': "David Ricardo",
            'i': "La spécialisation selon les coûts comparés augmente la "
                 "production disponible pour tous les partenaires."},
           {'n': "Jean-Baptiste Say",
            'i': "La loi des débouchés exclut la possibilité d’une crise "
                 "générale de surproduction."}],
      termes=['classiques', 'main invisible', 'loi des debouches',
              'division du travail'],
      dos=['n26-marche-etat', 'n26-autoregulation-instabilite']),

   nd('marx', 'Marx et la lecture par les contradictions', 'pilier',
      "Le travail comme source de la valeur, la lutte des classes comme "
      "moteur, les crises comme structurelles et non accidentelles.",
      grp=2,
      defi="Karl Marx partage avec les classiques l’objet — la production et "
           "la répartition de la richesse — et la centralité du travail, mais "
           "en inverse la conclusion. Le travail n’est pas un facteur parmi "
           "d’autres : il est la source de la valeur. Et le système ne tend "
           "pas vers l’harmonie : il produit lui-même les contradictions qui "
           "le mènent à la crise.",
      mec=[("L’armée de réserve",
            "La pauvreté n’est pas due à une surpopulation naturelle mais à "
            "l’existence d’une armée de réserve de travailleurs qui maintient "
            "les salaires à bas niveau : on passe d’une explication "
            "démographique à une explication sociale et historique."),
           ("Les crises comme contradictions internes",
            "Les crises ne sont pas accidentelles mais structurelles : elles "
            "résultent des contradictions du système, et non d’un choc "
            "extérieur qui viendrait le perturber."),
           ("L’histoire comme lutte des classes",
            "L’analyse économique est inséparable d’une analyse historique et "
            "politique : le capitalisme est un système daté, pas un état "
            "naturel de l’économie.")],
      aut=[{'n': "Karl Marx",
            'i': "Les crises ne sont pas accidentelles mais structurelles : "
                 "elles résultent des contradictions du système."}],
      faits=[{'f': "Le Manifeste du Parti communiste est publié en 1848 avec "
                   "Friedrich Engels ; le cours précise que c’est à la fois "
                   "un texte théorique et un texte politique.",
              'p': "La double nature du texte explique la difficulté de sa "
                   "réception : l’analyse économique y est indissociable "
                   "d’un projet politique explicite."}],
      termes=['marx', 'lutte des classes', 'armee de reserve',
              'theorie de la valeur'],
      dos=['n26-production-repartition', 'n26-cooperation-conflit']),

   # ------------------------------------------- colonne 3 : les néoclassiques
   nd('neoclassiques', 'Les néoclassiques', 'pilier',
      "L’utilité remplace le travail, le marginal remplace le global, et "
      "l’équilibre général devient le cadre de référence.",
      grp=3,
      defi="L’approche néoclassique déplace le fondement de la valeur : ce "
           "n’est plus le travail incorporé mais l’utilité que le bien "
           "procure à la marge. L’analyse devient celle de choix individuels "
           "sous contrainte, et Walras montre que tous les marchés sont "
           "interdépendants et que l’économie peut atteindre un équilibre "
           "général simultané.",
      mec=[("Le raisonnement à la marge",
            "La décision porte sur l’unité supplémentaire : c’est la "
            "comparaison entre l’utilité marginale et le coût marginal qui "
            "fixe la quantité, non une grandeur moyenne."),
           ("L’équilibre général",
            "Tous les marchés étant interdépendants, un système de prix peut "
            "en principe égaliser simultanément offres et demandes partout : "
            "le marché devient un mécanisme d’ajustement démontrable."),
           ("La continuité avec les classiques",
            "Classiques et néoclassiques partagent la supériorité de "
            "l’économie de marché comme mécanisme de coordination, ainsi que "
            "la primauté de la liberté individuelle et de la propriété "
            "privée.")],
      aut=[{'n': "Léon Walras",
            'i': "Tous les marchés sont interdépendants et l’économie peut "
                 "atteindre un équilibre général simultané."},
           {'n': "Alfred Marshall",
            'i': "L’analyse en équilibre partiel permet d’étudier un marché "
                 "en supposant les autres inchangés."},
           {'n': "Vilfredo Pareto",
            'i': "Une allocation est optimale lorsqu’on ne peut améliorer la "
                 "situation de l’un sans dégrader celle d’un autre."}],
      termes=['neoclassiques', 'equilibre general', 'utilite marginale',
              'marginalisme'],
      dos=['n5-cpp', 'n5-pareto']),

   nd('hayek', 'Le marché comme processus de découverte', 'detail',
      "Chez Hayek, l’information est dispersée et subjective : aucun "
      "planificateur n’en dispose globalement. Et l’instabilité n’est pas "
      "exclue.",
      grp=3, par='neoclassiques',
      defi="Friedrich Hayek partage avec les néoclassiques la confiance dans "
           "le marché mais pour une raison différente : ce n’est pas parce "
           "qu’il calcule l’équilibre, c’est parce qu’il découvre une "
           "information que nul ne détient globalement. Le cours relève par "
           "ailleurs une divergence nette : contrairement aux néoclassiques, "
           "Hayek admet l’instabilité du capitalisme et la possibilité de "
           "crises.",
      mec=[("L’information dispersée",
            "Chaque agent détient une connaissance locale et subjective que "
            "personne ne peut centraliser : le prix est le seul dispositif "
            "capable d’en transmettre l’essentiel."),
           ("L’impossibilité du calcul central",
            "Si l’information n’est pas disponible globalement, aucun "
            "planificateur ne peut savoir ce qu’il faudrait savoir pour "
            "décider : l’argument porte sur la connaissance, non sur les "
            "incitations."),
           ("L’origine monétaire des crises",
            "Une création monétaire excessive abaisse artificiellement les "
            "taux, provoque un surinvestissement et peut conduire à des "
            "crises : l’instabilité vient de la monnaie, non du marché.")],
      aut=[{'n': "Friedrich Hayek",
            'i': "Le marché est un processus de découverte dans un monde "
                 "d’information dispersée."}],
      termes=['hayek', 'information dispersee', 'calcul economique'],
      dos=['n15-etat-minimal', 'n13-cycle-credit']),

   # ------------------------------- colonne 4 : la rupture keynésienne et la riposte
   nd('keynes', 'La rupture keynésienne', 'pilier',
      "La production dépend de la demande anticipée. Une économie peut rester "
      "durablement en sous-emploi sans qu’aucun mécanisme ne l’en sorte.",
      grp=4,
      defi="John Maynard Keynes publie en 1936 la Théorie générale de "
           "l’emploi, de l’intérêt et de la monnaie, dans un contexte de "
           "crise profonde : Grande Dépression de 1929, chômage de masse "
           "durable, échec des mécanismes de marché à rétablir spontanément "
           "le plein-emploi. Son objectif est d’expliquer pourquoi une "
           "économie peut rester durablement en crise, et de proposer des "
           "solutions.",
      mec=[("Le principe de la demande effective",
            "La production et l’emploi ne dépendent pas de l’offre mais de la "
            "demande anticipée par les entrepreneurs : l’économie peut se "
            "stabiliser en sous-emploi."),
           ("Le refus du long terme comme horizon d’analyse",
            "La formule « à long terme, nous serons tous morts » n’est pas "
            "une boutade : elle refuse une analyse qui ne vaudrait qu’à "
            "l’équilibre final et met le court terme au centre."),
           ("L’investissement et les esprits animaux",
            "L’investissement dépend des anticipations, de la confiance et "
            "des esprits animaux, non du seul taux d’intérêt : le "
            "comportement ne se déduit pas d’un calcul.")],
      opp=[{'t': "En plaçant l’État au centre de la sortie de crise, Keynes "
                 "rejetterait le marché comme mécanisme de coordination et "
                 "préconiserait une économie administrée.",
            'qui': "lecture courante",
            'rep': "Non : le cours est explicite, Keynes ne rejette pas le "
                   "marché, il critique son fonctionnement spontané. Il "
                   "raisonne dans une économie de marché, non planifiée."}],
      aut=[{'n': "John Maynard Keynes",
            'i': "L’emploi dépend de la demande globale, pas du seul marché "
                 "du travail."}],
      faits=[{'f': "Pour Keynes, les « classiques » regroupent les classiques "
                   "historiques — Smith, Ricardo, Malthus, Say — et les "
                   "néoclassiques, unis par la confiance fondamentale dans "
                   "l’autorégulation du marché.",
              'p': "La catégorie est polémique et doit être annoncée comme "
                   "telle : elle rassemble des auteurs que tout oppose par "
                   "ailleurs sur la valeur et sur la répartition."}],
      termes=['keynes', 'demande effective', 'sous emploi',
              'esprits animaux'],
      dos=['n13-crises-demande', 'n26-equilibre-desequilibre']),

   nd('riposte', 'La riposte libérale', 'pilier',
      "Taux de chômage naturel, anticipations, règles plutôt que discrétion : "
      "l’intervention est jugée inutile, puis dangereuse.",
      grp=4,
      defi="À partir des années 1970, une riposte théorique conteste le cadre "
           "keynésien. Elle procède en deux temps : d’abord l’idée d’un taux "
           "de chômage naturel que la politique ne peut pas réduire "
           "durablement ; ensuite celle d’agents dont les anticipations "
           "neutralisent la politique annoncée. Le cours en résume la "
           "position : marchés efficaces, agents parfaitement rationnels, "
           "monnaie neutre, État inutile voire nuisible.",
      mec=[("Le taux de chômage naturel",
            "Il existe un niveau incompressible lié aux frictions du marché "
            "du travail : la politique peut s’en écarter temporairement, pas "
            "durablement."),
           ("La neutralisation par les anticipations",
            "Les agents connaissent la règle suivie par les autorités et en "
            "intègrent les effets avant qu’ils ne se produisent : une "
            "politique annoncée n’agit que sur les variables nominales."),
           ("Le passage de l’inefficacité à la nuisance",
            "Les politiques discrétionnaires créent de l’incertitude et "
            "perturbent les anticipations : l’intervention devient non "
            "seulement inutile mais dangereuse, d’où la préférence pour des "
            "règles simples et stables.")],
      aut=[{'n': "Milton Friedman",
            'i': "Il existe un taux de chômage naturel, incompressible, lié "
                 "aux frictions du marché du travail."},
           {'n': "Thomas Sargent",
            'i': "Une politique annoncée n’agit que sur les variables "
                 "nominales, puisque les agents en intègrent les effets par "
                 "avance."}],
      faits=[{'f': "Les années 1970 sont marquées par les chocs pétroliers de "
                   "1973 et 1979 et par une stagflation inédite associant "
                   "inflation et chômage.",
              'p': "C’est l’observation qui rend la riposte crédible : la "
                   "coexistence d’inflation et de chômage disqualifiait le "
                   "diagnostic purement keynésien."}],
      termes=['monetarisme', 'nouvelle economie classique',
              'anticipations rationnelles', 'chomage naturel'],
      dos=['n15-anticipations', 'n15-regles-discretion']),

   # ------------------------------ colonne 5 : les hétérodoxies institutionnelles
   nd('institutions', 'Institutions et comportements', 'pilier',
      "Veblen rejette l’homo œconomicus ; North fait des institutions "
      "l’explication des trajectoires de développement.",
      grp=5,
      defi="Le courant institutionnaliste conteste l’abstraction de l’agent "
           "rationnel et replace l’économie dans l’histoire et dans la "
           "société. Thorstein Veblen adopte une position hétérodoxe : il "
           "critique l’orthodoxie néoclassique sans devenir marxiste. "
           "Douglass North prolonge la démarche en combinant économie, "
           "histoire et science politique, et fonde la Nouvelle Économie "
           "Institutionnelle.",
      mec=[("Le refus de l’homo œconomicus",
            "Les comportements économiques ne sont pas des choix purs : ils "
            "dépendent des habitudes, des normes, des institutions et surtout "
            "de la recherche de statut social."),
           ("Les institutions comme règles formelles et informelles",
            "Pour North, les institutions sont l’ensemble des règles "
            "formelles — lois, droits de propriété, contrats — et "
            "informelles — coutumes, traditions — qui encadrent le "
            "comportement des individus."),
           ("Les institutions créent des incitations",
            "Elles ne se contentent pas d’encadrer : elles orientent les "
            "comportements en modifiant ce qui est avantageux, ce qui en fait "
            "une variable explicative du développement et non un décor.")],
      aut=[{'n': "Thorstein Veblen",
            'i': "Les comportements économiques dépendent des habitudes, des "
                 "normes et de la recherche de statut social."},
           {'n': "Douglass North",
            'i': "Les institutions sont les règles formelles et informelles "
                 "qui structurent les interactions humaines et réduisent "
                 "l’incertitude."}],
      faits=[{'f': "Dans Théorie de la classe de loisir, en 1899, Veblen "
                   "montre qu’une classe dominante ne produit pas directement "
                   "et vit du capital et de la propriété.",
              'p': "L’ouvrage introduit la consommation comme signe de "
                   "statut, ce qui conteste directement la lecture de la "
                   "consommation comme satisfaction d’un besoin."}],
      termes=['institutionnalisme', 'institutions', 'veblen', 'north'],
      dos=['n26-institutions-comportements', 'n26-individu-societe']),

   nd('regulation', 'L’école de la régulation', 'debat',
      "Le capitalisme n’est pas naturel : c’est un système historique dont "
      "les crises révèlent l’épuisement d’une configuration institutionnelle.",
      grp=5,
      defi="L’école de la régulation émerge en France à partir des années "
           "1970, autour de Michel Aglietta et Robert Boyer. Son contexte de "
           "naissance est précis : ralentissement de la croissance, chômage "
           "durable, inflation, remise en cause du compromis fordiste — des "
           "transformations de long terme que les économistes néoclassiques "
           "ou keynésiens standard peinent à expliquer.",
      mec=[("Les crises comme phénomènes structurels",
            "L’objectif est de comprendre les crises non comme des écarts "
            "transitoires mais comme l’épuisement d’une configuration : la "
            "crise de 1929 révèle celui du mode de régulation concurrentiel."),
           ("Le capitalisme comme système historique",
            "Contrairement aux néoclassiques, l’école considère que le "
            "capitalisme n’est pas naturel : il prend des formes datées, "
            "dont la cohérence institutionnelle fait la stabilité."),
           ("Les institutions au centre",
            "Formes de la concurrence, rapport salarial, régime monétaire : "
            "c’est leur cohérence mutuelle qui soutient l’accumulation, et "
            "son délitement qui produit la crise.")],
      aut=[{'n': "Michel Aglietta",
            'i': "Le capitalisme s’analyse comme un système historique dont "
                 "les crises relèvent de transformations structurelles."},
           {'n': "Robert Boyer",
            'i': "La crise de 1929 s’analyse comme l’épuisement du mode de "
                 "régulation concurrentiel, et non comme un choc accidentel."}],
      faits=[{'f': "Michel Aglietta publie Régulation et crises du "
                   "capitalisme en 1976, Robert Boyer La théorie de la "
                   "régulation en 1986.",
              'p': "Les deux dates encadrent la constitution du courant et "
                   "montrent qu’il se forme en réponse directe aux crises des "
                   "années 1970."}],
      termes=['ecole de la regulation', 'mode de regulation',
              'compromis fordiste'],
      dos=['n13-cycles-economiques', 'n26-institutions-comportements']),
  ],
  [
   ln('prelude', 'classiques', 'déplace la question vers',
      "La richesse cesse d’être un stock à capter par le commerce ou un "
      "produit de la seule terre : elle devient un flux produit par le "
      "travail et la division du travail. C’est la rupture fondatrice de "
      "l’économie politique.", 'cause'),
   ln('classiques', 'marx', 'est retournée par',
      "Marx partage l’objet — production et répartition — et la centralité du "
      "travail, mais en inverse la conclusion : le travail est la source de "
      "la valeur, et le système produit lui-même les contradictions qui le "
      "mènent à la crise.", 'oppose'),
   ln('classiques', 'neoclassiques', 'est prolongée et déplacée par',
      "Les deux courants partagent la supériorité du marché comme mécanisme "
      "de coordination et la primauté de la propriété privée, mais le "
      "fondement de la valeur change : l’utilité marginale remplace le "
      "travail incorporé.", 'cause'),
   ln('neoclassiques', 'hayek', 'est nuancée par',
      "Hayek défend le marché pour une autre raison : non parce qu’il "
      "calcule l’équilibre, mais parce qu’il découvre une information "
      "dispersée. Et, contrairement aux néoclassiques, il admet "
      "l’instabilité du capitalisme.", 'oppose'),
   ln('neoclassiques', 'keynes', 'est rompue par',
      "Keynes juge l’économie dominante trop abstraite, trop éloignée de la "
      "réalité et fondée sur des hypothèses irréalistes — plein-emploi, "
      "rationalité parfaite. La demande effective remplace l’ajustement par "
      "les prix.", 'oppose'),
   ln('marx', 'keynes', 'partage le diagnostic d’instabilité avec',
      "Marx et Keynes s’accordent sur un point contre les classiques : "
      "l’économie ne tend pas spontanément vers le plein emploi. Ils "
      "divergent entièrement sur la cause et sur l’issue.", 'renforce'),
   ln('keynes', 'riposte', 'suscite',
      "La stagflation des années 1970 — inflation et chômage simultanés — "
      "disqualifie le diagnostic purement keynésien et rend crédible la "
      "critique par le chômage naturel puis par les anticipations.",
      'oppose'),
   ln('riposte', 'neoclassiques', 'retrouve les hypothèses de',
      "Marchés efficaces, agents parfaitement rationnels, monnaie neutre : la "
      "riposte reprend le socle néoclassique en y ajoutant les anticipations, "
      "ce qui en radicalise les conclusions sur l’État.", 'renforce'),
   ln('neoclassiques', 'institutions', 'est contestée par',
      "Veblen rejette l’homo œconomicus : les comportements dépendent des "
      "habitudes, des normes et de la recherche de statut. L’économie doit "
      "être analysée comme une réalité historique et sociale, pas comme un "
      "équilibre abstrait.", 'oppose'),
   ln('institutions', 'regulation', 'prépare',
      "Si les institutions encadrent et orientent les comportements, alors "
      "les trajectoires économiques s’expliquent par des configurations "
      "institutionnelles datées : c’est exactement le programme de l’école de "
      "la régulation.", 'cause'),
   ln('keynes', 'regulation', 'ne suffit plus pour',
      "Les économistes keynésiens standard peinent à expliquer le "
      "ralentissement durable, le chômage persistant et la remise en cause du "
      "compromis fordiste : c’est ce manque qui fait naître le courant.",
      'limite'),
   ln('marx', 'regulation', 'inspire sans déterminer',
      "L’école de la régulation partage avec Marx la lecture du capitalisme "
      "comme système historique traversé de contradictions, mais refuse la "
      "thèse d’un effondrement nécessaire : les crises y ouvrent des "
      "reconfigurations.", 'renforce'),
   ln('hayek', 'riposte', 'nourrit',
      "L’argument de l’information dispersée fournit à la critique libérale "
      "un fondement distinct de celui des anticipations : l’État ne peut pas "
      "savoir, avant même la question de savoir s’il peut agir.", 'cause'),
   ln('institutions', 'classiques', 'réinterprète',
      "Si les institutions créent les incitations, alors la main invisible "
      "n’opère pas dans le vide : elle suppose des droits de propriété et des "
      "contrats, c’est-à-dire un cadre institutionnel que les classiques "
      "supposaient donné.", 'limite'),
   ln('prelude', 'marx', 'annonce la question de la répartition',
      "La controverse sur l’origine de la richesse contient déjà celle de son "
      "partage : qui produit le surplus, et qui se l’approprie ? Marx fait de "
      "cette seconde question le centre de l’analyse.", 'cause'),
  ],
  bandes=[(1, 'Avant les classiques'), (2, 'Classiques et Marx'),
          (3, 'Les néoclassiques'), (4, 'Keynes et la riposte'),
          (5, 'Les hétérodoxies institutionnelles')],
  fam='Marché, État et théories')
