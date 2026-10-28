# -*- coding: utf-8 -*-
"""Visualisation 7 — La mondialisation (type flux)."""

from vz_base import v, nd, ln

v('vz-mondialisation', 'La mondialisation',
  '2ᵉ année, chapitre 1 · des moteurs aux débats',
  'flux',
  "La mondialisation ne se réduit pas au commerce : elle cumule trois "
  "dimensions — commerciale, productive, financière — dont la hiérarchie "
  "change d’une époque à l’autre. Cette visualisation se lit de gauche à "
  "droite : ce qui la rend possible, les formes qu’elle prend, les "
  "configurations historiques qu’elle a produites, ses effets, et les "
  "questions ouvertes aujourd’hui.",
  [("Cinq colonnes, cinq moments du raisonnement",
    "Moteurs, dimensions, configurations historiques, effets, débats "
    "contemporains. Une dissertation sur la mondialisation peut suivre cet "
    "ordre directement, ou en isoler une colonne et la traiter en "
    "profondeur."),
   ("La leçon de Michalet et celle de Berger",
    "Michalet : les configurations sont cumulatives, non successives — le "
    "commerce ne disparaît pas quand la finance domine. Berger : une "
    "mondialisation peut s’effondrer. Ces deux idées suffisent à structurer "
    "une copie sur l’histoire de la mondialisation."),
   ("Ne pas conclure trop vite sur les effets",
    "Le cours énumère cinq variables dont dépend le bilan local de "
    "l’insertion : le pays, le secteur, le niveau de qualification, la "
    "position dans la chaîne et la capacité à monter en gamme. Toute "
    "conclusion générale est donc fausse.")],
  [
   # --------------------------------------------------- colonne 1 : moteurs
   nd('transports', 'La baisse des coûts de transport', 'pilier',
      "La cause technique initiale : elle rend rentable l’échange sur de "
      "longues distances, puis la séparation des étapes de production entre "
      "pays.",
      grp=1,
      defi="Le cours fait de la baisse des coûts de transport et de "
           "communication la cause technique initiale de la mondialisation. "
           "Elle agit à deux niveaux successifs : elle rend d’abord rentable "
           "l’échange de biens sur de longues distances, puis, lorsque la "
           "communication devient elle aussi peu coûteuse, elle rend "
           "possible la coordination d’étapes de production séparées "
           "géographiquement.",
      mec=[("Le seuil de rentabilité de l’échange lointain",
            "Tant que le transport coûte cher, seuls les biens de forte "
            "valeur par unité de poids s’échangent. Sa baisse élargit "
            "progressivement la gamme des biens pour lesquels l’échange "
            "international devient avantageux."),
           ("La séparation des étapes",
            "La baisse du coût de communication permet de piloter à distance "
            "des opérations autrefois réunies sur un même site : c’est elle "
            "qui autorise la fragmentation de la production, et non la seule "
            "baisse du fret.")],
      args=[{'a': "L’explication technique rend compte du déclenchement des "
                  "deux grandes vagues : 1870-1913 par le transport, la "
                  "période contemporaine par la communication.",
             'lim': "Elle n’explique pas l’effondrement de la première "
                    "mondialisation, puisque les coûts de transport n’ont pas "
                    "augmenté : les causes de l’arrêt sont politiques."}],
      aut=[{'n': "Richard Baldwin",
            'i': "Les chaînes de valeur mondiales résultent de la baisse des "
                 "coûts de transport et de communication."}],
      termes=['couts de transport', 'revolution des transports'],
      dos=['n17-couts-transport']),

   nd('decisions', 'Les décisions politiques d’ouverture', 'pilier',
      "Rien n’est spontané : droits de douane, accords commerciaux, "
      "libéralisation des capitaux, adhésions. L’ouverture se décide.",
      grp=1,
      defi="L’ouverture commerciale et financière résulte de décisions "
           "politiques et réglementaires, non d’une évolution spontanée. Le "
           "cours est explicite pour la finance : la globalisation financière "
           "repose sur la libéralisation des mouvements de capitaux, la "
           "déréglementation financière, l’internationalisation des "
           "placements et l’intégration des marchés. Pour le commerce, les "
           "États déterminent largement les conditions d’ouverture, les "
           "droits de douane, les accords commerciaux et les relations "
           "internationales.",
      mec=[("La fixation des conditions d’accès",
            "Droits de douane, quotas, normes et accords commerciaux "
            "déterminent ce qui peut entrer et à quel coût : l’État reste "
            "l’acteur central de la dimension commerciale."),
           ("La libéralisation financière",
            "La levée du contrôle des changes et la déréglementation "
            "financière ouvrent la troisième dimension : elles sont des "
            "décisions datées et réversibles, non une tendance naturelle."),
           ("L’adhésion aux institutions multilatérales",
            "Rejoindre l’Organisation mondiale du commerce transforme "
            "l’accès aux marchés en droit opposable : la décision "
            "institutionnelle précède et conditionne l’intégration "
            "productive.")],
      faits=[{'f': "L’adhésion de la Chine à l’Organisation mondiale du "
                   "commerce en 2001 constitue un accélérateur majeur de son "
                   "insertion dans les chaînes de valeur mondiales.",
              'p': "La date montre le rôle de la décision institutionnelle : "
                   "l’intégration productive a suivi une ouverture négociée, "
                   "elle ne l’a pas précédée."}],
      termes=['ouverture commerciale', 'liberalisation',
              'organisation mondiale du commerce'],
      dos=['n17-ouverture-commerciale', 'n17-integration-economique']),

   # ------------------------------------------------ colonne 2 : dimensions
   nd('commerce', 'La dimension commerciale', 'pilier',
      "Les échanges de biens et services entre résidents et non-résidents : "
      "la première forme, et celle où l’État pèse le plus.",
      grp=2,
      defi="Le commerce international correspond à l’ensemble des opérations "
           "d’achat et de vente entre résidents et non-résidents. C’est la "
           "première des trois dimensions de la mondialisation et celle où le "
           "rôle des États est le plus direct : ils déterminent largement les "
           "conditions d’ouverture, les droits de douane, les accords "
           "commerciaux et les relations internationales.",
      mec=[("La spécialisation et l’échange",
            "Chaque pays concentre sa production sur ce qu’il produit "
            "relativement le mieux et importe le reste : c’est le gain à "
            "l’échange, qui ne suppose pas un avantage absolu mais un "
            "avantage comparatif."),
           ("La mesure par le taux d’ouverture",
            "Le poids des échanges dans l’économie est mesuré par le taux "
            "d’ouverture, ce qui permet de comparer les époques : environ "
            "quinze pour cent au sommet de la première mondialisation, trente "
            "au sommet de l’hypermondialisation.")],
      faits=[{'f': "Le taux d’ouverture passe d’environ quinze pour cent au "
                   "sommet de la première mondialisation à environ trente "
                   "pour cent au sommet de l’hypermondialisation.",
              'p': "Le chiffre mesure l’intensité de la dimension "
                   "commerciale et permet de comparer les deux grandes vagues "
                   "autrement que par impression."}],
      aut=[{'n': "David Ricardo",
            'i': "L’échange est avantageux même lorsqu’un pays est moins "
                 "productif dans toutes les activités, pourvu qu’il se "
                 "spécialise selon son avantage comparatif."}],
      termes=['commerce international', 'taux d ouverture',
              'specialisation internationale'],
      dos=['n16-specialisation-internationale', 'n17-ouverture-commerciale']),

   nd('production', 'La dimension productive', 'pilier',
      "Après 1945, les entreprises ne se contentent plus de vendre à "
      "l’étranger : elles y produisent, par filiales et investissements "
      "directs.",
      grp=2,
      defi="La dimension productive correspond au moment où les entreprises "
           "ne se contentent plus de vendre à l’étranger mais vont également "
           "y produire, par les investissements directs, les filiales et les "
           "firmes multinationales. Elle transforme la nature de la "
           "mondialisation : ce ne sont plus seulement des biens qui "
           "traversent les frontières, mais des capacités productives qui "
           "s’implantent.",
      mec=[("L’investissement direct plutôt que l’exportation",
            "Produire sur place permet de contourner les barrières "
            "commerciales, de réduire les coûts de transport et d’adapter le "
            "produit au marché local : l’entreprise choisit entre exporter et "
            "s’implanter."),
           ("La fragmentation des chaînes de valeur",
            "Les entreprises répartissent les étapes de production entre "
            "plusieurs pays : conception ici, composants ailleurs, assemblage "
            "dans un autre pays, commercialisation mondiale.")],
      faits=[{'f': "Le cours décrit la répartition des étapes : conception "
                   "ici, composants ailleurs, assemblage dans un autre pays, "
                   "commercialisation mondiale.",
              'p': "L’énumération montre que la dimension productive ne "
                   "délocalise pas des industries entières mais des "
                   "fonctions, ce qui change la nature de la concurrence "
                   "entre territoires."}],
      aut=[{'n': "Raymond Vernon",
            'i': "La délocalisation de la production suit la banalisation "
                 "progressive de la technologie au cours du cycle de vie du "
                 "produit."}],
      termes=['investissement direct etranger', 'firme multinationale',
              'fragmentation de la production'],
      dos=['n17-fragmentation-production', 'n16-cycle-vie-produit']),

   nd('finance', 'La dimension financière', 'pilier',
      "À partir des années 1980-1990, les mouvements de capitaux explosent et "
      "les marchés s’intègrent : la dimension la plus rapide et la plus "
      "volatile.",
      grp=2,
      defi="La globalisation financière repose sur la libéralisation des "
           "mouvements de capitaux, la déréglementation financière, "
           "l’internationalisation des placements et l’intégration des "
           "marchés. À partir des années 1980-1990, les mouvements "
           "internationaux de capitaux explosent et les investisseurs "
           "institutionnels prennent une place croissante. C’est la dimension "
           "dont les ajustements sont les plus rapides, donc la plus "
           "susceptible de transmettre un choc.",
      mec=[("La levée des entraves à la circulation",
            "Le contrôle des changes et les cloisonnements réglementaires "
            "disparaissent : le capital peut se placer où le rendement "
            "corrigé du risque est le plus élevé, quelle que soit la "
            "frontière."),
           ("L’intégration des marchés",
            "Les places financières cessent d’être des compartiments séparés : "
            "une variation de taux décidée dans un pays se transmet "
            "immédiatement aux conditions de financement des autres.")],
      args=[{'a': "L’intégration financière élargit le financement "
                  "disponible : un pays peut investir plus qu’il n’épargne, "
                  "ce qui desserre la contrainte de l’épargne intérieure.",
             'lim': "La même mobilité permet un retrait brutal des capitaux, "
                    "ce qui transforme un doute sur un pays en crise de "
                    "financement, sans rapport avec ses capacités "
                    "productives."}],
      aut=[{'n': "Charles-Albert Michalet",
            'i': "La mondialisation est un processus multidimensionnel dont "
                 "la hiérarchie des dimensions évolue dans le temps."}],
      termes=['globalisation financiere', 'mobilite du capital',
              'deregulation financiere'],
      dos=['n17-mobilite-capital', 'n17-mondialisation']),

   # -------------------------------------------- colonne 3 : configurations
   nd('premiere', 'La première mondialisation (1870-1913)', 'detail',
      "Dominée par le commerce, un taux d’ouverture de quatorze à quinze pour "
      "cent — et un effondrement. Une mondialisation peut échouer.",
      grp=3,
      defi="La première mondialisation est la période 1870-1913, dominée par "
           "la dimension commerciale : essor du commerce, baisse des coûts de "
           "transport, spécialisation internationale, avec un taux "
           "d’ouverture moyen d’environ quatorze à quinze pour cent à son "
           "sommet. Le cours insiste sur son effondrement : une "
           "mondialisation apparemment profonde, durable et intégrée peut "
           "s’effondrer.",
      mec=[("La division internationale du travail par produit",
            "Chaque pays se spécialise dans un produit selon le schéma "
            "ricardien : c’est la division internationale du travail que "
            "Suzanne Berger place au cœur de cette période."),
           ("La hiérarchisation centre-périphérie",
            "La division s’organise entre un centre industrialisé et une "
            "périphérie spécialisée dans l’approvisionnement en matières "
            "premières : le cours parle d’une relation structurellement "
            "asymétrique."),
           ("La dégradation politique avant la contraction des flux",
            "Tensions géopolitiques, impérialisme, protectionnisme : les "
            "conditions politiques de l’ouverture se dégradent avant que les "
            "flux ne se contractent. Guerres et crises interrompent ensuite "
            "l’intégration.")],
      aut=[{'n': "Suzanne Berger",
            'i': "Une mondialisation peut échouer : c’est la leçon d’un échec "
                 "oublié."}],
      faits=[{'f': "En Inde, la part de l’emploi industriel passe de "
                   "vingt-deux pour cent en 1810 à neuf pour cent en 1901.",
              'p': "Les deux chiffres documentent la désindustrialisation des "
                   "périphéries : ils montrent que l’intégration a pu "
                   "détruire des capacités productives."},
             {'f': "Le cours relève que la première mondialisation accompagne "
                   "l’essor de l’État social, tandis que l’hypermondialisation "
                   "présente la protection sociale comme un coût.",
              'p': "Le contraste montre que deux mondialisations d’intensité "
                   "comparable peuvent entretenir des rapports opposés à la "
                   "protection sociale : l’ouverture n’impose pas un modèle "
                   "social unique."}],
      termes=['premiere mondialisation', 'division internationale du travail',
              'centre peripherie'],
      dos=['n17-premiere-mondialisation', 'n16-division-internationale-travail']),

   nd('hyper', 'L’hypermondialisation', 'detail',
      "Le cumul des trois dimensions, un taux d’ouverture d’environ trente "
      "pour cent, et la première vague réellement mondiale.",
      grp=3,
      defi="L’hypermondialisation est la configuration contemporaine, "
           "caractérisée par le cumul des flux commerciaux, productifs et "
           "financiers. Le cours la définit par ce cumul et par son "
           "intensité : le taux d’ouverture passe d’environ quinze pour cent "
           "au sommet de la première mondialisation à environ trente pour "
           "cent, soit un poids des échanges environ deux fois plus élevé. "
           "Le passage à des niveaux historiquement inédits est situé à "
           "partir des années 1990-2000.",
      mec=[("Le cumul et non la succession",
            "Le commerce continue de croître et les investissements directs "
            "se poursuivent : la configuration précédente ne disparaît pas, "
            "elle cesse seulement d’être la dimension dominante."),
           ("L’extension géographique",
            "De nombreux pays auparavant relativement fermés participent "
            "désormais intensément aux échanges : la troisième vague est la "
            "première à rendre la mondialisation véritablement mondiale."),
           ("Le ralentissement contemporain",
            "Le taux d’ouverture cesse de progresser fortement, stagne, et "
            "peut même diminuer légèrement selon les périodes : la dynamique "
            "perd de sa vigueur sans s’inverser.")],
      aut=[{'n': "Charles-Albert Michalet",
            'i': "Les configurations de la mondialisation sont cumulatives et "
                 "non successives."}],
      faits=[{'f': "Au sommet de l’hypermondialisation, le taux d’ouverture "
                   "atteint environ trente pour cent, contre quinze lors de "
                   "la première mondialisation.",
              'p': "Le doublement mesure la rupture d’intensité et fournit le "
                   "chiffre le plus directement utilisable pour comparer les "
                   "deux vagues."}],
      termes=['hypermondialisation', 'taux d ouverture',
              'integration economique'],
      dos=['n17-hypermondialisation', 'n17-mondialisation']),

   # ------------------------------------------------- colonne 4 : les effets
   nd('chaines', 'Les chaînes de valeur mondiales', 'pilier',
      "Les étapes se répartissent par fonction et non par produit. La "
      "position dans la chaîne décide de la part de valeur captée.",
      grp=4,
      defi="Les chaînes de valeur mondiales désignent l’organisation "
           "internationale des étapes de production d’un même bien, pilotée "
           "par les firmes multinationales. Elles déterminent où la valeur "
           "est créée, quelle part chaque pays en capte, et donc la "
           "hiérarchie réelle des positions dans la production mondiale. La "
           "coordination est assurée par une décision privée et non par le "
           "marché, ce qui complique sa régulation publique.",
      mec=[("La répartition par fonction",
            "Chaque étape est implantée là où elle est la plus avantageuse : "
            "la chaîne relie des sites spécialisés par fonction et non par "
            "produit, ce qui rompt avec la spécialisation ricardienne."),
           ("La captation différenciée de la valeur",
            "Conception et marque ajoutent davantage que l’assemblage. La "
            "part de valeur ajoutée domestique mesure ce que le pays capte "
            "réellement : c’est le critère de sa position dans la chaîne."),
           ("Le biais de la mesure brute",
            "Un même bien franchissant plusieurs frontières, les échanges "
            "mesurés en valeur brute surestiment la contribution des pays "
            "d’assemblage : la mesure en valeur ajoutée corrige ce biais."),
           ("La montée en gamme",
            "Augmenter la part de valeur ajoutée domestique permet de "
            "remonter dans la chaîne : la position n’est pas figée, comme le "
            "montre la trajectoire chinoise.")],
      aut=[{'n': "Richard Baldwin",
            'i': "Les chaînes de valeur mondiales résultent de la baisse des "
                 "coûts de transport et de communication."},
           {'n': "Suzanne Berger",
            'i': "La mondialisation contemporaine repose sur la division "
                 "internationale des processus productifs."}],
      faits=[{'f': "La Chine utilise d’abord les chaînes de valeur mondiales "
                   "comme pays atelier avant de monter en gamme et "
                   "d’augmenter la part de valeur ajoutée domestique.",
              'p': "La trajectoire montre que la position dans la chaîne "
                   "n’est pas figée et qu’une remontée est possible sans "
                   "changer de secteur."}],
      termes=['chaines de valeur mondiales', 'valeur ajoutee domestique',
              'montee en gamme'],
      dos=['n17-chaines-valeur', 'n17-fragmentation-production']),

   nd('inegalites', 'Des gains très inégalement répartis', 'limite',
      "Entre pays, la mondialisation a réduit des écarts ; à l’intérieur des "
      "pays, elle en a creusé d’autres. La courbe de l’éléphant fixe les deux "
      "mouvements.",
      grp=4,
      defi="Les effets de la mondialisation sur les inégalités sont de signe "
           "opposé selon l’échelle retenue. À l’échelle mondiale, l’entrée de "
           "pays très peuplés dans les échanges a élevé les revenus "
           "intermédiaires et réduit certains écarts entre pays. À "
           "l’intérieur des pays développés, les catégories exposées à la "
           "concurrence ont décroché. La courbe de l’éléphant construite par "
           "Milanovic sur la période 1988-2008 représente simultanément ces "
           "deux mouvements.",
      mec=[("La convergence entre pays",
            "L’insertion de pays très peuplés dans les chaînes de production "
            "a élevé le revenu de catégories intermédiaires à l’échelle "
            "mondiale : c’est le sommet de la courbe."),
           ("Le décrochage des classes moyennes des pays riches",
            "Les catégories dont les emplois sont exposés à la concurrence "
            "internationale et à l’automatisation voient leur revenu relatif "
            "stagner : c’est le creux de la courbe."),
           ("L’asymétrie entre gains diffus et pertes concentrées",
            "Les gains de pouvoir d’achat sont faibles mais répartis sur de "
            "nombreux ménages, les pertes d’emploi fortes mais concentrées "
            "sur certains individus et territoires : les deux ne se "
            "compensent pas individuellement.")],
      opp=[{'t': "La polarisation des rémunérations s’explique par la "
                 "spécialisation internationale et la modification de la "
                 "demande relative de facteurs.",
            'qui': "lecture par le commerce",
            'rep': "Le cours objecte que le commerce n’explique pas à lui "
                   "seul les inégalités internes, qui dépendent également du "
                   "progrès technique, des institutions et des politiques "
                   "économiques et sociales."}],
      aut=[{'n': "Branko Milanovic",
            'i': "La mondialisation réduit certaines inégalités entre pays "
                 "tout en accroissant des inégalités internes."},
           {'n': "Pierre-Noël Giraud",
            'i': "Les activités nomades sont exposées à la concurrence "
                 "mondiale, les sédentaires sont protégées par leur ancrage "
                 "territorial."}],
      faits=[{'f': "Le cours conclut que les effets de la mondialisation "
                   "productive dépendent du pays, du secteur, du niveau de "
                   "qualification, de la position dans la chaîne et de la "
                   "capacité à monter en gamme.",
              'p': "L’énumération interdit toute conclusion générale : elle "
                   "fournit les cinq variables dont dépend le bilan local de "
                   "l’insertion."}],
      termes=['courbe de l elephant', 'inegalites mondiales',
              'polarisation des emplois'],
      dos=['n10-polarisation', 'n16-repartition-gains']),

   # ------------------------------------------------ colonne 5 : les débats
   nd('dependances', 'Les dépendances stratégiques', 'limite',
      "La défaillance d’un maillon interrompt l’ensemble : la recherche "
      "d’efficacité a réduit la robustesse.",
      grp=5,
      defi="Les dépendances stratégiques désignent les situations où "
           "l’approvisionnement d’un pays en biens essentiels repose sur un "
           "petit nombre de fournisseurs étrangers, parfois un seul. Elles "
           "résultent directement de l’organisation en chaînes de valeur : la "
           "spécialisation par fonction optimise le coût mais crée des points "
           "de passage obligés, dont la défaillance interrompt l’ensemble de "
           "la chaîne.",
      mec=[("L’arbitrage entre efficacité et robustesse",
            "Concentrer une étape là où elle coûte le moins réduit le coût "
            "total mais supprime les sources alternatives : la chaîne devient "
            "plus performante et plus fragile simultanément."),
           ("La transformation d’une dépendance en levier",
            "Lorsqu’un fournisseur est en position de point de passage "
            "obligé, la relation commerciale devient un instrument de "
            "pression : l’économique et le stratégique cessent d’être "
            "séparables.")],
      aut=[{'n': "Janet Yellen",
            'i': "La sécurité des approvisionnements est devenue un objectif "
                 "des politiques économiques."}],
      args=[{'a': "La reconnaissance des dépendances stratégiques justifie "
                  "des politiques de diversification et de relocalisation "
                  "ciblées, distinctes d’un protectionnisme généralisé.",
             'lim': "Le périmètre du stratégique est extensible : invoqué "
                    "sans critère, l’argument de sécurité peut couvrir "
                    "n’importe quelle demande de protection sectorielle."}],
      termes=['dependances strategiques', 'securite economique',
              'relocalisation'],
      dos=['n17-dependances-strategiques', 'n17-relocalisation']),

   nd('demondialisation', 'Démondialisation ou réorientation ?', 'debat',
      "Le cours refuse le terme pour la période actuelle : les flux ne se "
      "contractent pas simultanément, ils se réorganisent.",
      grp=5,
      defi="La démondialisation désigne une phase de recul de l’intégration "
           "internationale, caractérisée non par le ralentissement d’un seul "
           "flux mais par la contraction simultanée des flux commerciaux, "
           "migratoires, financiers et monétaires. Le cours en fait un "
           "phénomène multidimensionnel, dont l’entre-deux-guerres fournit le "
           "cas historique, et il refuse d’appliquer le terme au "
           "ralentissement contemporain.",
      mec=[("Le critère de simultanéité",
            "Il y a véritable démondialisation lorsque les flux commerciaux, "
            "migratoires, financiers et monétaires se contractent "
            "simultanément. Un seul flux en recul ne suffit pas à qualifier "
            "le phénomène."),
           ("L’enchaînement des années 1930",
            "La crise de 1929 est suivie d’un mouvement de démondialisation, "
            "les États cherchant à protéger leur économie nationale : hausse "
            "des barrières, contraction des échanges, multiplication des "
            "représailles, aggravation des tensions internationales."),
           ("La fermeture comme cause autant que conséquence",
            "Le cours insiste : la fermeture commerciale ne constitue pas "
            "seulement une conséquence de la crise, elle y contribue "
            "également. C’est ce qui explique la volonté d’après 1945 "
            "d’éviter le retour des politiques commerciales unilatérales."),
           ("La réorientation contemporaine",
            "Malgré les tarifs, les tensions, les sanctions et les politiques "
            "industrielles, le commerce mondial continue à progresser parce "
            "que les flux se réorganisent : la Chine exporte moins vers les "
            "États-Unis et davantage vers l’Europe et d’autres pays en "
            "développement.")],
      aut=[{'n': "Suzanne Berger",
            'i': "Une mondialisation peut échouer : la première s’est "
                 "effondrée."}],
      termes=['demondialisation', 'fragmentation geoeconomique',
              'regionalisation'],
      dos=['n17-demondialisation', 'n17-fragmentation-geoeconomique']),

   nd('rodrik', 'Le trilemme de Rodrik', 'debat',
      "Hypermondialisation, démocratie, souveraineté nationale : on ne peut "
      "combiner pleinement les trois. Il faut en sacrifier une.",
      grp=5,
      defi="Dani Rodrik développe le trilemme politique de l’économie "
           "mondiale : il est impossible de combiner pleinement "
           "hypermondialisation, démocratie et souveraineté nationale. "
           "Associer démocratie et hypermondialisation nécessiterait une "
           "gouvernance supranationale très approfondie ; conserver "
           "souveraineté et démocratie impose de borner l’intégration ; "
           "combiner hypermondialisation et souveraineté suppose de "
           "soustraire les choix économiques à la délibération démocratique.",
      mec=[("La contrainte sur les politiques nationales",
            "Plus l’intégration est profonde, plus les choix fiscaux, "
            "sociaux et réglementaires nationaux sont contraints par la "
            "mobilité des capitaux et des activités : la souveraineté "
            "s’exerce dans un espace rétréci."),
           ("La solution supranationale et son coût",
            "Transférer la décision au niveau où s’exerce l’intégration "
            "rétablit la cohérence, mais suppose une légitimité démocratique "
            "à ce niveau, que les constructions existantes n’atteignent "
            "qu’imparfaitement."),
           ("La troisième branche",
            "Conserver l’intégration et la souveraineté formelle conduit à "
            "soustraire des pans entiers de la politique économique au débat, "
            "ce qui nourrit la contestation de la mondialisation elle-même.")],
      aut=[{'n': "Dani Rodrik",
            'i': "L’approfondissement de la mondialisation entre en tension "
                 "avec la souveraineté et la démocratie nationales."}],
      args=[{'a': "Le trilemme explique pourquoi la contestation de la "
                  "mondialisation est politique autant qu’économique : elle "
                  "porte sur qui décide, pas seulement sur qui gagne.",
             'lim': "Il énonce une incompatibilité sans indiquer laquelle des "
                    "trois branches sacrifier : c’est un cadre d’analyse, non "
                    "une recommandation."}],
      termes=['trilemme', 'souverainete', 'gouvernance mondiale'],
      dos=['n17-interdependance', 'n17-mondialisation']),
  ],
  [
   ln('transports', 'commerce', 'rend l’échange rentable',
      "Tant que le transport coûte cher, seuls les biens de forte valeur par "
      "unité de poids s’échangent. Sa baisse élargit la gamme des biens pour "
      "lesquels l’échange international devient avantageux : c’est le "
      "déclencheur de la dimension commerciale.", 'cause'),
   ln('transports', 'production', 'rend la fragmentation possible',
      "La baisse du coût de communication permet de piloter à distance des "
      "opérations autrefois réunies sur un même site. C’est elle, et non le "
      "seul fret, qui autorise la séparation des étapes de production entre "
      "pays.", 'cause'),
   ln('decisions', 'finance', 'ouvre la troisième dimension',
      "La globalisation financière repose sur la libéralisation des "
      "mouvements de capitaux, la déréglementation financière, "
      "l’internationalisation des placements et l’intégration des marchés : "
      "quatre décisions, non une tendance naturelle.", 'cause'),
   ln('decisions', 'commerce', 'fixe les conditions d’accès',
      "Les États déterminent largement les conditions d’ouverture, les droits "
      "de douane, les accords commerciaux et les relations internationales : "
      "ils sont l’acteur central de la dimension commerciale.", 'conditionne'),
   ln('commerce', 'premiere', 'domine la configuration de',
      "La première mondialisation est dominée par la dimension commerciale : "
      "la spécialisation se fait par produit, selon le schéma ricardien, et "
      "l’État fixe les conditions de l’ouverture.", 'cause'),
   ln('production', 'hyper', 'alimente',
      "L’hypermondialisation ne remplace pas la dimension productive : elle "
      "l’intègre. Les investissements directs continuent et les entreprises "
      "répartissent les étapes de production entre plusieurs pays.", 'cause'),
   ln('finance', 'hyper', 'achève le cumul',
      "Le cours définit l’hypermondialisation par le cumul des trois "
      "dimensions. L’explosion des flux financiers à partir des années "
      "1980-1990 est la dernière à s’ajouter, et celle qui donne à la "
      "configuration son intensité propre.", 'cause'),
   ln('premiere', 'hyper', 'fournit l’étalon de comparaison',
      "Quinze pour cent de taux d’ouverture contre trente : le doublement "
      "mesure la rupture d’intensité entre les deux vagues et rend la "
      "comparaison historique possible autrement que par impression.",
      'mesure'),
   ln('production', 'chaines', 'se déploie en',
      "La dimension productive aboutit à l’organisation en chaînes de valeur : "
      "la spécialisation cesse de porter sur des produits pour porter sur des "
      "fonctions, ce qui change la façon dont la valeur se répartit entre "
      "pays.", 'cause'),
   ln('chaines', 'inegalites', 'hiérarchise les positions',
      "Conception et marque ajoutent davantage que l’assemblage : la position "
      "occupée dans la chaîne détermine la part de valeur captée, donc les "
      "rémunérations. La polarisation des emplois en est la traduction "
      "interne.", 'cause'),
   ln('premiere', 'inegalites', 'l’avait déjà montré',
      "La désindustrialisation de l’Inde entre 1810 et 1901 établit que "
      "l’intégration peut détruire des capacités productives. La question des "
      "perdants de l’ouverture n’est donc pas propre à la période "
      "contemporaine.", 'renforce'),
   ln('chaines', 'dependances', 'crée des points de passage obligés',
      "La défaillance d’un maillon interrompt l’ensemble : la recherche "
      "d’efficacité réduit la robustesse. C’est le mécanisme par lequel une "
      "organisation productive devient un enjeu de sécurité.", 'limite'),
   ln('inegalites', 'rodrik', 'nourrit la contestation',
      "Lorsque les pertes sont concentrées et les gains diffus, la "
      "contestation porte sur qui décide autant que sur qui gagne : le "
      "trilemme formalise cette tension entre intégration, démocratie et "
      "souveraineté.", 'cause'),
   ln('hyper', 'demondialisation', 'ralentit sans s’inverser',
      "Le taux d’ouverture cesse de progresser fortement, stagne et peut même "
      "diminuer légèrement. Mais les flux ne se contractent pas "
      "simultanément : le cours refuse donc d’appliquer le terme de "
      "démondialisation à la période actuelle.", 'limite'),
   ln('dependances', 'demondialisation', 'réoriente les flux',
      "Malgré les tarifs, les tensions, les sanctions et les politiques "
      "industrielles, le commerce mondial continue à progresser parce que les "
      "flux se réorganisent : la Chine exporte moins vers les États-Unis et "
      "davantage vers l’Europe et d’autres pays en développement.", 'cause'),
   ln('rodrik', 'decisions', 'ramène au politique',
      "Si l’intégration contraint les choix nationaux, alors son degré "
      "redevient une décision politique. Le trilemme boucle la figure : "
      "l’ouverture n’est pas un état de fait mais un arbitrage que les États "
      "reprennent périodiquement.", 'conditionne'),
  ],
  bandes=[(1, 'Les moteurs'), (2, 'Les trois dimensions'),
          (3, 'Les configurations'), (4, 'Les effets'),
          (5, 'Les débats ouverts')],
  fam='Mondialisation et échanges')
