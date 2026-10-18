# -*- coding: utf-8 -*-
"""Ensemble 28 — Le libre-échange, les protectionnismes et les stratégies
commerciales. Première série de dossiers.

Toute la matière provient des cours chargés dans ÉcoSphère, principalement du
chapitre 3 de deuxième année (analyse économique du commerce international) et
du chapitre 4 (régionalisation, gouvernance et régulations internationales),
complétés par les chapitres 1 et 2 de deuxième année et par le chapitre 7.
Aucune attribution d'auteur n'est ajoutée de mémoire.
"""

from doss_base import d

# ---------------------------------------------------------------- 28.01
d('le28-libre-echange', 28, "Libre-échange",
  "Une situation d’échanges peu entravés, et une doctrine qui la recommande",
  "Le libre-échange désigne une situation dans laquelle les échanges "
  "internationaux de biens et de services ne sont pas, ou sont peu, entravés "
  "par des obstacles publics : droits de douane, quotas, normes discriminantes, "
  "exigences administratives. Il faut le distinguer de la doctrine libre- "
  "échangiste, qui soutient que cette situation est souhaitable. La première "
  "est un fait mesurable, la seconde un jugement : un pays peut être très ouvert "
  "sans adhérer à la doctrine, et inversement.",
  "La confusion la plus coûteuse, dans une copie, consiste à traiter le libre- "
  "échange comme une doctrine homogène qu’il faudrait approuver ou rejeter en "
  "bloc. Le cours impose d’emblée une distinction : le libre-échange et le "
  "protectionnisme sont d’abord des situations concrètes, c’est-à-dire des états "
  "observables de la politique commerciale d’un pays, avant d’être des doctrines. "
  "Une fois cette distinction posée, le raisonnement économique se déroule en "
  "trois temps. D’abord, l’ouverture permet la spécialisation : chaque pays "
  "concentre ses facteurs là où son coût d’opportunité est le plus faible, ce qui "
  "élève la production mondiale à ressources inchangées. Ensuite, l’importation "
  "n’est pas une concession mais le gain même de l’échange, puisqu’elle permet "
  "d’obtenir à moindre coût ce qu’il serait relativement plus coûteux de produire "
  "nationalement ; l’exportation n’en est que le moyen de financement. Enfin, "
  "l’ouverture agit aussi par des canaux que les théories traditionnelles "
  "n’avaient pas isolés : elle élargit la variété offerte aux consommateurs, elle "
  "permet des économies d’échelle en agrandissant le marché pertinent, et elle "
  "soumet les producteurs nationaux à une pression concurrentielle qui réduit les "
  "rentes. Le point décisif est que ces trois mécanismes produisent un gain "
  "agrégé, c’est-à-dire une somme positive à l’échelle du pays — ce qui ne dit "
  "rien de sa répartition entre les groupes sociaux. C’est très exactement sur "
  "cet écart entre gain agrégé et répartition que se construit tout le débat avec "
  "le protectionnisme.",
  [("La spécialisation selon les coûts d’opportunité",
    "Chaque pays cesse de produire les biens dont la production lui coûte "
    "relativement cher en facteurs et se concentre sur ceux où il sacrifie le "
    "moins. À dotation inchangée, la production mondiale augmente, et chaque "
    "partenaire peut obtenir davantage de biens qu’en autarcie."),
   ("L’importation comme gain, l’exportation comme financement",
    "Le pays importe ce qu’il produirait de façon relativement plus coûteuse : "
    "l’écart entre le prix mondial et le coût national est le gain réel. "
    "L’exportation sert à régler ces importations, ce qui interdit de lire un "
    "excédent commercial comme un gain en soi."),
   ("L’élargissement du marché et les économies d’échelle",
    "Dans les secteurs à rendements croissants, l’accès à un marché plus vaste "
    "permet d’allonger les séries, donc de faire baisser le coût moyen. "
    "L’ouverture crée ici des gains même entre pays aux dotations identiques, ce "
    "que les théories traditionnelles ne prévoyaient pas."),
   ("La pression concurrentielle et la variété",
    "La concurrence étrangère réduit les marges des producteurs nationaux "
    "abrités, ce qui diminue les prix payés par les consommateurs, tandis que la "
    "diversité des produits disponibles s’accroît. Le gain porte donc aussi sur "
    "le pouvoir d’achat et sur le choix, pas seulement sur l’allocation."),
   ("Le transfert et l’imitation technologiques",
    "L’ouverture met les producteurs nationaux en contact avec des biens, des "
    "procédés et des exigences de qualité étrangers. Cela peut accélérer la "
    "montée en gamme, à condition que le pays dispose des capacités "
    "d’absorption nécessaires.")],
  [{'a': "L’ouverture augmente le revenu réel disponible : à production "
         "nationale inchangée, importer moins cher libère du pouvoir d’achat "
         "pour les ménages et abaisse le coût des intrants pour les entreprises.",
    'cond': "Le mécanisme suppose que les facteurs libérés par les secteurs qui "
            "reculent soient effectivement réemployés ailleurs, donc une mobilité "
            "suffisante du travail et du capital, et des marchés intérieurs qui "
            "transmettent la baisse des prix plutôt que de l’absorber en marges.",
    'lim': "Si les facteurs ne se redéploient pas, le gain de pouvoir d’achat "
           "coexiste avec un chômage durable dans les régions spécialisées : le "
           "solde agrégé reste positif alors que des territoires entiers perdent, "
           "ce qui explique le rejet politique d’une politique pourtant rentable."},
   {'a': "L’ouverture discipline les producteurs nationaux : elle réduit les "
         "rentes de situation et contraint les firmes abritées à baisser leurs "
         "prix ou à améliorer leur qualité.",
    'cond': "Il faut que la concurrence étrangère soit réellement praticable — "
            "absence de barrières non tarifaires résiduelles, coûts de transport "
            "modérés — et que le marché intérieur ne soit pas structuré par des "
            "ententes qui neutralisent la pression.",
    'lim': "La discipline concurrentielle peut détruire des producteurs "
           "potentiellement efficaces qui n’ont pas encore atteint leur échelle "
           "critique : c’est l’objection des industries naissantes, qui montre "
           "que la pression n’est bénéfique que sur des producteurs comparables."},
   {'a': "L’ouverture agrandit le marché pertinent et permet donc des économies "
         "d’échelle inaccessibles sur le seul marché national.",
    'cond': "L’argument ne vaut que dans les secteurs à rendements croissants, et "
            "suppose que les producteurs nationaux soient en situation de "
            "capter ce marché élargi plutôt que de le céder à des concurrents "
            "déjà installés à grande échelle.",
    'lim': "Le même mécanisme joue contre le pays qui s’ouvre en second : celui "
           "qui est déjà à grande échelle bénéficie d’un avantage de coût que "
           "l’ouverture fige, ce qui peut verrouiller la répartition des "
           "spécialisations plutôt que de la rendre efficiente."},
   {'a': "L’ouverture permet de diversifier les approvisionnements, donc de "
         "réduire l’exposition à un choc national de production.",
    'cond': "La diversification n’est protectrice que si les sources "
            "d’approvisionnement sont réellement multiples et substituables ; "
            "importer d’un fournisseur unique n’est pas une diversification.",
    'lim': "Lorsque l’approvisionnement se concentre sur un petit nombre de "
           "pays, l’ouverture crée au contraire une dépendance que l’État "
           "fournisseur peut instrumentaliser, ce qui retourne l’argument."}],
  [{'t': "Le libre-échange produit un gain agrégé mais crée des perdants "
         "identifiables, dont les pertes ne sont pas automatiquement compensées.",
    'qui': "Le cours insiste sur les coûts d’ajustement et sur la nécessité de "
           "politiques de formation, de reconversion et de redistribution.",
    'rep': "L’objection ne conteste pas le gain, elle conteste l’idée que le "
           "gain suffise. Elle appelle donc une politique d’accompagnement "
           "plutôt qu’une fermeture : si l’on renonce à l’ouverture, on perd le "
           "gain sans résoudre le problème de répartition."},
   {'t': "Toutes les spécialisations ne se valent pas : se spécialiser selon son "
         "avantage comparatif immédiat peut enfermer un pays dans des "
         "productions à faible contenu technologique.",
    'qui': "Argument développé dans le cours à propos des spécialisations "
           "primaires et de la croissance appauvrissante.",
    'rep': "C’est l’argument le plus solide contre l’automatisme libre-échangiste "
           "et il fonde le protectionnisme éducateur. Il ne condamne pas "
           "l’ouverture, il la rend conditionnelle au moment : ouvrir après "
           "avoir construit un appareil productif, et non avant."},
   {'t': "Le libre-échange historique n’a jamais été la règle : les pays "
         "aujourd’hui développés se sont industrialisés derrière des protections.",
    'qui': "Paul Bairoch décrit le XIXᵉ siècle comme un « océan de "
           "protectionnisme » et rappelle qu’autour de 1820, les droits de douane "
           "britanniques figurent parmi les plus élevés d’Europe.",
    'rep': "Le fait historique est établi et interdit de présenter l’ouverture "
           "comme la norme dont le protectionnisme serait l’exception. Il "
           "n’établit cependant pas que la protection ait causé le rattrapage : "
           "corrélation et causalité restent à distinguer."}],
  [{'n': "David Ricardo",
    'i': "L’avantage comparatif : c’est le coût d’opportunité, et non la "
         "productivité absolue, qui commande la spécialisation.",
    'p': "Un pays moins productif dans toutes les branches a malgré tout intérêt "
         "à l’échange : il se spécialise là où son désavantage est le plus "
         "faible. Ce résultat rend le gain à l’échange mutuel et fonde la thèse "
         "selon laquelle aucun pays n’est trop peu productif pour échanger."},
   {'n': "David Ricardo",
    'i': "L’importation est le gain de l’échange, l’exportation son financement.",
    'p': "Conséquence directe de l’avantage comparatif, et point de friction avec "
         "la pratique des négociations commerciales, qui traite politiquement "
         "l’exportation comme un gain et l’importation comme une concession."},
   {'n': "Modèle HOS (Heckscher, Ohlin, Samuelson)",
    'i': "La spécialisation dépend des dotations relatives en facteurs de "
         "production.",
    'p': "Un pays exporte le bien intensif dans le facteur dont il est "
         "relativement le mieux doté. La conclusion rejoint Ricardo sur les gains "
         "de l’échange, mais ajoute une clé de lecture des effets distributifs : "
         "le facteur abondant y gagne, le facteur rare y perd."},
   {'n': "Paul Krugman",
    'i': "Les rendements croissants créent des gains à l’ouverture même entre "
         "pays identiques.",
    'p': "Trois gains distincts apparaissent : la baisse du coût moyen par "
         "allongement des séries, l’élargissement de la variété disponible et la "
         "réduction des marges sous l’effet de la concurrence. L’ouverture cesse "
         "ainsi de dépendre de l’existence d’une différence entre les pays."},
   {'n': "Paul Bairoch",
    'i': "Le XIXᵉ siècle n’est pas un siècle uniformément libre-échangiste.",
    'p': "Il décrit un « océan de protectionnisme » : Corn Laws renforcées à "
         "partir de 1815, interdiction d’exporter certaines machines jusqu’en "
         "1842, préférence commerciale coloniale, droits élevés. Le Royaume-Uni "
         "ne devient véritablement libre-échangiste que dans la seconde moitié du "
         "siècle."}],
  [{'f': "Les droits de douane moyens sur les produits manufacturés dans les "
         "économies avancées passent d’environ 40 % en 1947 à environ 4 % à "
         "l’issue de l’Uruguay Round.",
    'p': "L’ordre de grandeur mesure l’ampleur réelle de la libéralisation "
         "d’après-guerre et montre que l’ouverture contemporaine est une "
         "construction institutionnelle récente, non un état naturel."},
   {'f': "Selon Findlay et O’Rourke (2002), la croissance du commerce mondial des "
         "années 1950 aux années 1980 s’explique à 67 % par la hausse des "
         "revenus, à 25 % par la baisse des droits de douane et à 8 % par celle "
         "des coûts de transport.",
    'p': "La décomposition relativise le rôle de la politique commerciale : "
         "l’ouverture accompagne la croissance autant qu’elle la produit, ce qui "
         "interdit d’attribuer au seul libre-échange l’essor des échanges."},
   {'f': "Autour de 1820, les droits de douane britanniques figurent parmi les "
         "plus élevés d’Europe, alors même que le Royaume-Uni est la première "
         "puissance industrielle.",
    'p': "Le fait contredit frontalement le récit selon lequel la puissance "
         "industrielle britannique aurait reposé sur une ouverture précoce, et "
         "sert d’appui à l’argument du protectionnisme éducateur."}],
  [{'q': "Sujet du type « Le libre-échange est-il toujours préférable au "
         "protectionnisme ? »",
    'f': "Poser d’abord que le libre-échange et le protectionnisme sont des "
         "situations avant d’être des doctrines permet d’éviter le faux débat : "
         "la question n’est pas de choisir un camp mais d’identifier à quelles "
         "conditions l’ouverture produit effectivement les gains qu’elle promet, "
         "et ce qu’il advient lorsque ces conditions ne sont pas réunies.",
    'r': "On établit en première partie le gain agrégé par la spécialisation, les "
         "économies d’échelle et la pression concurrentielle ; on montre en "
         "deuxième partie que ce gain se répartit inégalement et suppose une "
         "mobilité des facteurs qui n’est jamais parfaite ; on conclut sur la "
         "conditionnalité plutôt que sur une préférence générale.",
    'ex': "Le passage de droits de douane d’environ 40 % à environ 4 % sur les "
          "manufactures entre 1947 et l’Uruguay Round donne la mesure du gain "
          "possible ; les coûts d’ajustement en donnent le prix."},
   {'q': "Sujet du type « Dans quelles conditions le libre-échange profite-t-il à "
         "un pays ? »",
    'f': "Le gain à l’ouverture n’a rien d’automatique : il suppose que les "
         "facteurs libérés soient réemployés, que la spécialisation obtenue "
         "porte sur des activités à fort contenu technologique, et que le pays "
         "dispose des capacités d’absorption lui permettant de transformer "
         "l’exposition internationale en montée en gamme.",
    'r': "On transforme la question en liste de conditions vérifiables — "
         "mobilité, nature de la spécialisation, capacité d’absorption, "
         "diversification des fournisseurs — ce qui permet de traiter "
         "successivement les cas où elles sont réunies et ceux où elles ne le "
         "sont pas.",
    'ex': "La décomposition de Findlay et O’Rourke rappelle que la baisse des "
          "droits n’explique qu’un quart de la croissance du commerce : le reste "
          "dépend des revenus, donc de la capacité productive."},
   {'q': "Sujet du type « Le commerce international est-il un jeu à somme "
         "positive ? »",
    'f': "Le commerce est un jeu à somme positive à l’échelle des nations prises "
         "globalement, mais il est simultanément un jeu à somme nulle entre les "
         "groupes sociaux d’un même pays lorsque la compensation n’est pas "
         "organisée : c’est cette superposition, et non le signe du solde "
         "agrégé, qui explique la conflictualité politique de l’ouverture.",
    'r': "On distingue explicitement les deux niveaux d’agrégation, ce qui permet "
         "de tenir ensemble le résultat théorique et le constat politique sans "
         "les opposer artificiellement.",
    'ex': "Le modèle HOS fournit le mécanisme : le facteur abondant gagne, le "
          "facteur rare perd, alors même que le pays dans son ensemble gagne."}],
  voisins=['le28-arguments-le', 'le28-gains-repartition', 'le28-couts-ouverture',
           'le28-protectionnisme', 'le28-ouverture-progressive'])

# ---------------------------------------------------------------- 28.02
d('le28-arguments-le', 28,
  "Arguments en faveur du libre-échange et conditions de validité",
  "Quatre familles d’arguments, et ce qu’il faut supposer pour qu’elles tiennent",
  "Les arguments favorables au libre-échange se rangent en quatre familles : "
  "l’argument allocatif (la spécialisation accroît la production mondiale), "
  "l’argument d’échelle (l’élargissement du marché abaisse les coûts moyens), "
  "l’argument concurrentiel (l’ouverture réduit les rentes et les prix) et "
  "l’argument dynamique (l’exposition internationale accélère l’apprentissage et "
  "la montée en gamme). Chacun repose sur des hypothèses explicites, et c’est la "
  "discussion de ces hypothèses, bien plus que l’énoncé des arguments, qui fait "
  "la valeur d’une copie.",
  "L’erreur la plus fréquente consiste à empiler les arguments favorables à "
  "l’ouverture sans dire sous quelles conditions ils valent, puis à les "
  "« nuancer » en deuxième partie par des considérations sociales extérieures au "
  "raisonnement. La démarche rigoureuse est inverse : chaque argument porte en "
  "lui-même ses conditions de validité, et c’est en les explicitant qu’on obtient "
  "une analyse plutôt qu’un catalogue. L’argument allocatif suppose que les "
  "facteurs soient mobiles entre branches, faute de quoi la réallocation promise "
  "ne se produit pas et la spécialisation se traduit par du chômage plutôt que "
  "par un gain. L’argument d’échelle suppose des rendements croissants et la "
  "capacité des producteurs nationaux à conquérir le marché élargi : s’ils "
  "démarrent trop petits face à des concurrents déjà installés, le même mécanisme "
  "les élimine au lieu de les faire grandir — c’est exactement le point où "
  "Krugman réhabilite l’argument des industries naissantes. L’argument "
  "concurrentiel suppose que la pression étrangère soit effective et que le "
  "marché intérieur transmette les baisses de prix. L’argument dynamique, enfin, "
  "suppose une capacité d’absorption : un pays ne monte en gamme au contact de la "
  "concurrence que s’il dispose du capital humain et des institutions permettant "
  "d’imiter puis d’innover. Autrement dit, les quatre arguments sont solides, "
  "mais ils sont conditionnels — et la liste de leurs conditions constitue, telle "
  "quelle, le plan d’une deuxième partie.",
  [("Condition de mobilité des facteurs",
    "Le gain allocatif exige que le travail et le capital quittent les branches "
    "en recul pour rejoindre les branches en expansion. Cette mobilité est "
    "coûteuse, lente et géographiquement inégale ; lorsqu’elle fait défaut, la "
    "spécialisation produit un gain de prix et une perte d’emploi simultanés."),
   ("Condition d’échelle atteignable",
    "Les économies d’échelle ne bénéficient au pays qui s’ouvre que s’il peut "
    "franchir le seuil de production au-delà duquel son coût moyen descend sous "
    "celui des concurrents. En dessous de ce seuil, l’ouverture consolide la "
    "position de l’opérateur déjà installé."),
   ("Condition de concurrence effective en aval",
    "La baisse des prix à l’importation n’atteint le consommateur que si la "
    "distribution et les marchés intérieurs sont eux-mêmes concurrentiels. Dans "
    "le cas contraire, la baisse est captée en marges et le gain de pouvoir "
    "d’achat annoncé ne se matérialise pas."),
   ("Condition de capacité d’absorption",
    "Le transfert technologique associé à l’ouverture suppose un niveau de "
    "qualification, des infrastructures et des institutions permettant "
    "d’assimiler les techniques étrangères. Sans cela, l’ouverture donne accès à "
    "des produits importés sans produire de montée en gamme."),
   ("Condition de qualité de la spécialisation",
    "Le gain statique de l’échange est compatible avec une spécialisation "
    "défavorable à long terme. Un pays peut gagner à court terme en se "
    "spécialisant dans des productions à faible contenu technologique et perdre "
    "en trajectoire de croissance.")],
  [{'a': "L’ouverture améliore l’allocation des ressources : chaque facteur est "
         "employé là où il est relativement le plus productif, ce qui élève la "
         "production mondiale sans augmenter les dotations.",
    'cond': "Mobilité intersectorielle des facteurs, absence de distorsions "
            "internes majeures, et transmission des prix mondiaux aux producteurs "
            "nationaux — faute de quoi le signal qui déclenche la réallocation "
            "n’existe pas.",
    'lim': "Le résultat est statique : il décrit un niveau de production plus "
           "élevé, pas un rythme de croissance plus rapide. Il ne dit rien sur "
           "la capacité du pays à changer de spécialisation ensuite."},
   {'a': "L’ouverture abaisse les coûts moyens par les économies d’échelle, y "
         "compris entre pays aux dotations semblables.",
    'cond': "Présence de rendements croissants, et possibilité effective "
            "d’atteindre l’échelle critique — ce qui dépend de la taille du "
            "marché accessible et de l’avance des concurrents installés.",
    'lim': "Le mécanisme est asymétrique : il favorise celui qui a déjà la "
           "taille. C’est pourquoi le même raisonnement, poussé jusqu’au bout, "
           "débouche sur une justification de la protection temporaire."},
   {'a': "L’ouverture accroît le pouvoir d’achat et la variété disponible : elle "
         "donne accès à des biens moins chers et plus diversifiés qu’en autarcie.",
    'cond': "Concurrence effective en aval, stabilité des approvisionnements, et "
            "absence de coûts cachés — logistiques, sanitaires ou "
            "environnementaux — qui annuleraient le gain de prix.",
    'lim': "Le gain de pouvoir d’achat est diffus, étalé sur l’ensemble des "
           "consommateurs, tandis que les pertes d’emploi sont concentrées : "
           "cette asymétrie explique que l’ouverture soit politiquement perdante "
           "même lorsqu’elle est économiquement gagnante."},
   {'a': "L’ouverture discipline les producteurs et réduit les rentes de "
         "situation que l’abri national autorisait.",
    'cond': "Les producteurs nationaux doivent pouvoir répondre par la "
            "productivité ou la qualité, donc disposer d’un accès au "
            "financement et à la main-d’œuvre qualifiée nécessaires.",
    'lim': "Si la réponse est impossible, la discipline se transforme en "
           "élimination : la rente disparaît, mais la capacité productive aussi."}],
  [{'t': "Les arguments favorables à l’ouverture reposent sur des hypothèses de "
         "concurrence et de mobilité que la réalité ne vérifie qu’imparfaitement.",
    'qui': "Objection interne à l’analyse économique, reprise dans le cours à "
           "propos des coûts d’ajustement et des perdants de l’ouverture.",
    'rep': "L’objection est recevable mais ne conclut pas à la fermeture : elle "
           "conclut à l’accompagnement. Renoncer à l’ouverture supprime le gain "
           "sans restaurer la mobilité ni la concurrence."},
   {'t': "Le gain agrégé ne justifie pas l’ouverture tant que la compensation des "
         "perdants reste théorique.",
    'qui': "Argument développé dans le cours autour de la nécessité de "
           "politiques de formation, de reconversion, de mobilité et de "
           "redistribution.",
    'rep': "Le critère pertinent devient alors politique autant qu’économique : "
           "une ouverture dont les gains ne sont pas redistribués est "
           "soutenable économiquement et intenable politiquement, ce que "
           "confirme le retour contemporain du protectionnisme."},
   {'t': "L’argument d’échelle peut être retourné : il justifie la protection "
         "temporaire aussi bien que l’ouverture.",
    'qui': "Paul Krugman, qui formalise le mécanisme des industries naissantes.",
    'rep': "C’est effectivement le même modèle qui produit les deux conclusions. "
           "Ce qui les sépare n’est pas la théorie mais la position du pays : "
           "déjà à l’échelle, il gagne à l’ouverture ; en dessous du seuil, il "
           "gagne à une protection transitoire."}],
  [{'n': "David Ricardo",
    'i': "L’argument allocatif : la spécialisation selon les coûts comparés "
         "augmente la production disponible pour tous les partenaires.",
    'p': "Le raisonnement vaut même lorsqu’un pays est moins productif partout, "
         "ce qui lui donne sa portée universelle. Sa condition implicite est la "
         "mobilité interne des facteurs, puisqu’il faut que les ressources "
         "quittent effectivement la branche abandonnée."},
   {'n': "Modèle HOS (Heckscher, Ohlin, Samuelson)",
    'i': "L’argument allocatif reformulé par les dotations factorielles, avec sa "
         "conséquence distributive.",
    'p': "En reliant la spécialisation à l’abondance relative des facteurs, le "
         "modèle prédit que l’ouverture enrichit le facteur abondant et appauvrit "
         "le facteur rare : il fournit ainsi, dans le même mouvement, l’argument "
         "favorable et l’explication de la contestation sociale."},
   {'n': "Paul Krugman",
    'i': "Les rendements croissants fondent trois gains distincts : coût moyen, "
         "variété, pression concurrentielle.",
    'p': "Ces gains n’exigent aucune différence préalable entre les pays, ce qui "
         "explique l’intensité des échanges entre économies semblables et "
         "complète les théories traditionnelles au lieu de les contredire."},
   {'n': "Paul Krugman",
    'i': "Le seuil critique : l’ouverture immédiate peut empêcher l’émergence "
         "d’une industrie viable.",
    'p': "Même cadre analytique, conclusion inverse : tant que la production "
         "nationale reste inférieure au seuil permettant les économies "
         "d’échelle, le producteur potentiellement le plus efficace ne peut pas "
         "entrer. La condition de validité de l’argument d’échelle devient alors "
         "un argument en faveur d’une protection temporaire."}],
  [{'f': "Les rounds du GATT font passer les droits de douane sur les produits "
         "manufacturés d’environ 40 % à environ 4 %, les concessions négociées "
         "étant ensuite généralisées par la clause de la nation la plus favorisée.",
    'p': "La libéralisation a donc été obtenue par un marchandage réciproque et "
         "non par l’adhésion des gouvernements à la théorie : les arguments "
         "favorables au libre-échange n’ont pas été la cause de son adoption."},
   {'f': "Le droit de douane moyen atteint 15,9 % du prix dans l’agriculture "
         "contre environ 3 % dans l’industrie en 2019.",
    'p': "L’écart montre que les arguments favorables à l’ouverture n’ont pas été "
         "appliqués uniformément : le secteur où les pays en développement "
         "disposent d’avantages comparatifs est précisément le plus protégé."},
   {'f': "Les simulations de l’OMC de 2026 associent à une coopération "
         "multilatérale renforcée un gain d’environ +2,9 % de PIB mondial à "
         "l’horizon 2050, et d’environ +7,7 % de PIB pour les pays les moins "
         "avancés.",
    'p': "L’ordre de grandeur donne une mesure contemporaine du gain attendu de "
         "l’ouverture coordonnée, et indique que ce gain est plus élevé pour les "
         "économies les plus pauvres."}],
  [{'q': "Sujet du type « Un gain global lié au commerce suffit-il à justifier "
         "l’ouverture ? »",
    'f': "Les arguments favorables au libre-échange ne sont pas des énoncés "
         "inconditionnels mais des propositions assorties d’hypothèses : "
         "mobilité des facteurs, échelle atteignable, concurrence effective en "
         "aval, capacité d’absorption. Un gain global ne justifie donc "
         "l’ouverture que dans la mesure où ces conditions sont réunies et où la "
         "répartition du gain est organisée.",
    'r': "Le plan se déduit des conditions : une première partie établit les "
         "gains, une deuxième examine une à une les hypothèses qui les "
         "soutiennent, une troisième tire les conséquences de politique "
         "économique — accompagner plutôt que fermer.",
    'ex': "Les simulations de l’OMC chiffrent le gain d’une coopération renforcée "
          "à +2,9 % de PIB mondial en 2050 ; encore faut-il que ce gain atteigne "
          "ceux qui subissent l’ajustement."},
   {'q': "Sujet du type « Les avantages comparatifs sont-ils donnés ou "
         "construits ? »",
    'f': "Les théories traditionnelles traitent l’avantage comparatif comme une "
         "donnée — technologique chez Ricardo, factorielle dans le modèle HOS — "
         "tandis que l’analyse en termes de rendements croissants en fait un "
         "résultat de l’histoire : celui qui a commencé le premier conserve "
         "l’avantage de coût, ce qui ouvre la possibilité de le construire par "
         "la politique économique.",
    'r': "Le basculement d’une conception donnée à une conception construite est "
         "le fil conducteur : il explique pourquoi les mêmes modèles servent à "
         "justifier l’ouverture et, sous d’autres hypothèses, l’intervention.",
    'ex': "Krugman montre qu’une industrie potentiellement plus efficace peut ne "
          "jamais émerger faute d’atteindre son échelle critique."},
   {'q': "Sujet du type « Tous les groupes sociaux bénéficient-ils du "
         "libre-échange ? »",
    'f': "Le modèle HOS répond précisément : l’ouverture enrichit le facteur "
         "relativement abondant et appauvrit le facteur relativement rare. La "
         "contestation sociale du libre-échange n’est donc pas une mauvaise "
         "compréhension de la théorie, elle en est une prédiction.",
    'r': "Partir de la prédiction distributive du modèle plutôt que d’un constat "
         "sociologique permet de relier rigoureusement l’analyse économique et "
         "l’analyse politique de l’ouverture.",
    'ex': "L’écart entre la protection agricole — 15,9 % — et la protection "
          "industrielle — 3 % — montre quels groupes ont effectivement obtenu "
          "d’être exemptés de cet ajustement."}],
  voisins=['le28-libre-echange', 'le28-gains-repartition', 'le28-couts-ouverture',
           'le28-educateur', 'le28-protectionnisme'])

# ---------------------------------------------------------------- 28.03
d('le28-gains-repartition', 28, "Gains du commerce et répartition de ces gains",
  "Un gain agrégé positif n’interdit ni les perdants ni le rejet politique",
  "Les gains du commerce désignent l’augmentation du revenu réel permise par "
  "l’échange : accès à des biens moins chers, allongement des séries de "
  "production, variété accrue, pression sur les marges. Leur répartition désigne "
  "la manière dont ce supplément se distribue entre les pays, entre les facteurs "
  "de production et entre les groupes sociaux. La distinction est essentielle : "
  "le gain est agrégé, la répartition ne l’est pas.",
  "Toute la difficulté du sujet tient à ce que les deux questions — y a-t-il un "
  "gain ? comment se partage-t-il ? — appellent des réponses de nature "
  "différente, la première théorique et la seconde empirique et politique. Sur "
  "la première, les modèles convergent : l’échange élève la production "
  "disponible, que l’avantage vienne des coûts comparés, des dotations "
  "factorielles ou des rendements croissants. Sur la seconde, les mêmes modèles "
  "livrent des prédictions distributives précises. Le modèle HOS établit que le "
  "facteur relativement abondant voit sa rémunération augmenter et le facteur "
  "relativement rare la voir baisser : dans une économie avancée riche en travail "
  "qualifié, l’ouverture avec des économies riches en travail peu qualifié élève "
  "le rendement de la qualification et déprime celui du travail peu qualifié. La "
  "répartition entre pays, elle, dépend des termes de l’échange : un pays dont "
  "les prix d’exportation baissent relativement à ses prix d’importation peut "
  "voir son gain s’éroder, jusqu’au cas limite de la croissance appauvrissante, "
  "où produire davantage réduit le revenu réel. S’ajoute enfin une asymétrie "
  "politique décisive : les gains sont diffus — quelques euros de pouvoir d’achat "
  "pour des millions de consommateurs — tandis que les pertes sont concentrées "
  "sur des branches et des territoires identifiables, donc capables de "
  "s’organiser. Un gain agrégé positif peut ainsi produire une majorité politique "
  "hostile, ce qui n’est pas une irrationalité mais une conséquence de la "
  "structure du problème.",
  [("Du gain agrégé au gain individuel",
    "Le supplément de production permis par la spécialisation se traduit en "
    "baisse de prix pour les consommateurs et en hausse de revenu pour les "
    "facteurs employés dans les branches exportatrices. Rien, dans ce mécanisme, "
    "ne garantit que chaque agent reçoive une part positive."),
   ("La répartition entre facteurs",
    "Dans le cadre HOS, l’ouverture modifie les prix relatifs des biens, donc la "
    "demande relative des facteurs : le facteur intensément utilisé dans la "
    "branche exportatrice voit sa rémunération augmenter, l’autre la voit "
    "baisser. La redistribution est interne et systématique, non accidentelle."),
   ("La répartition entre pays par les termes de l’échange",
    "Le partage du gain dépend du rapport entre le prix des exportations et celui "
    "des importations. Une dégradation durable de ce rapport transfère une "
    "partie du gain au partenaire, même si le volume échangé augmente."),
   ("L’asymétrie entre gains diffus et pertes concentrées",
    "Le gain de pouvoir d’achat est réparti sur l’ensemble des consommateurs, "
    "chacun en percevant une fraction minime ; la perte est supportée par un "
    "nombre restreint d’actifs et de territoires, qui en perçoivent toute "
    "l’ampleur et disposent d’une capacité d’action collective."),
   ("La compensation et son caractère hypothétique",
    "Le raisonnement économique suppose qu’un gain agrégé permet en principe de "
    "compenser les perdants tout en laissant les gagnants mieux lotis. Cette "
    "compensation reste une possibilité : si elle n’est pas organisée par des "
    "politiques explicites, l’argument perd sa force normative.")],
  [{'a': "Le commerce élève le revenu réel agrégé : à dotations inchangées, la "
         "spécialisation et l’échange permettent de consommer davantage.",
    'cond': "Le résultat suppose la réallocation effective des facteurs et la "
            "stabilité des termes de l’échange ; il est établi à un niveau "
            "d’agrégation national et ne dit rien des situations individuelles.",
    'lim': "Un gain agrégé compatible avec une majorité de perdants n’est pas "
           "politiquement soutenable, ce qui en fait un argument économiquement "
           "juste et politiquement insuffisant."},
   {'a': "Les gains sont d’autant plus élevés que les économies sont différentes, "
         "puisque l’écart de coûts d’opportunité est plus grand.",
    'cond': "Encore faut-il que la différence porte sur des productions "
            "substituables et que les infrastructures d’échange existent, sans "
            "quoi l’écart théorique reste inexploité.",
    'lim': "Cette même différence maximise les effets distributifs internes : le "
           "commerce le plus rentable est aussi le plus conflictuel socialement, "
           "ce qui explique que le commerce intrabranche entre pays semblables "
           "soit politiquement moins contesté."},
   {'a': "Les gains peuvent être redistribués : formation, reconversion, "
         "mobilité et redistribution permettent de transformer un gain agrégé en "
         "amélioration partagée.",
    'cond': "Il faut une capacité budgétaire, des dispositifs efficaces de "
            "reconversion et une volonté politique durable — conditions plus "
            "exigeantes que la simple existence du gain.",
    'lim': "Les politiques de compensation sont lentes et imparfaites alors que "
           "les pertes sont immédiates : le décalage temporel suffit à nourrir "
           "le rejet de l’ouverture avant même que la compensation n’agisse."}],
  [{'t': "Le gain agrégé masque une redistribution massive que les perdants n’ont "
         "aucune raison d’accepter.",
    'qui': "Prédiction du modèle HOS, confirmée dans le cours par l’analyse des "
           "perdants de l’ouverture et des coûts d’ajustement.",
    'rep': "L’objection impose de traiter la compensation comme partie intégrante "
           "de la politique d’ouverture, et non comme un supplément facultatif : "
           "c’est la condition de sa soutenabilité."},
   {'t': "Le gain peut être capté par le partenaire si les termes de l’échange se "
         "dégradent, jusqu’à la croissance appauvrissante.",
    'qui': "Jagdish Bhagwati, avec la croissance appauvrissante : exporter "
           "davantage peut réduire le revenu réel.",
    'rep': "Le cas est théoriquement précis et empiriquement restrictif : il "
           "suppose un pays assez grand pour peser sur les prix mondiaux et une "
           "demande peu élastique. Il invalide l’automatisme du gain, pas le "
           "principe de l’échange."},
   {'t': "La répartition internationale des gains dépend du rapport de force "
         "autant que de l’efficacité.",
    'qui': "Les analyses marxistes de l’asymétrie des échanges, reprises dans le "
           "cours.",
    'rep': "L’argument déplace utilement la question vers les conditions "
           "institutionnelles de l’échange, mais il ne supprime pas le gain : il "
           "explique pourquoi celui-ci peut être très inégalement partagé."}],
  [{'n': "Modèle HOS (Heckscher, Ohlin, Samuelson)",
    'i': "La répartition des gains entre facteurs est déterminée par l’intensité "
         "factorielle des branches qui s’étendent et de celles qui reculent.",
    'p': "Le facteur abondant gagne, le facteur rare perd. Cette prédiction "
         "transforme la question sociale du libre-échange en résultat de modèle, "
         "ce qui permet de l’argumenter au lieu de la constater."},
   {'n': "Jagdish Bhagwati",
    'i': "La croissance appauvrissante : produire et exporter davantage peut "
         "réduire le revenu réel.",
    'p': "Si l’augmentation des volumes exportés dégrade suffisamment les termes "
         "de l’échange, la perte sur les prix l’emporte sur le gain sur les "
         "quantités. Le cas montre que le gain du commerce dépend du prix relatif "
         "obtenu, non du seul volume échangé."},
   {'n': "Branko Milanovic",
    'i': "La courbe de l’éléphant : la mondialisation a des gagnants et des "
         "perdants identifiables dans la distribution mondiale des revenus.",
    'p': "La forme de la courbe donne un contenu empirique à la question de la "
         "répartition : des classes moyennes émergentes et les très hauts revenus "
         "progressent fortement, tandis que les classes moyennes des pays "
         "avancés stagnent — ce qui éclaire la géographie politique du rejet."},
   {'n': "Lionel Fontagné",
    'i': "L’ouverture produit des effets ambivalents qu’il faut évaluer "
         "séparément.",
    'p': "Distinguer l’effet sur le pouvoir d’achat des ménages de l’effet sur "
         "les revenus du travail permet de comprendre qu’un même individu puisse "
         "gagner comme consommateur et perdre comme salarié."}],
  [{'f': "Selon la courbe de l’éléphant, les classes moyennes des pays avancés "
         "connaissent une progression de revenu beaucoup plus faible que les "
         "classes moyennes émergentes et que les très hauts revenus mondiaux.",
    'p': "Le fait donne une base empirique à l’asymétrie de répartition et "
         "explique pourquoi le rejet de l’ouverture se concentre dans les pays "
         "riches alors même qu’ils en tirent un gain agrégé."},
   {'f': "Le droit de douane moyen de 15,9 % dans l’agriculture contre 3 % dans "
         "l’industrie en 2019 traduit un partage politique des gains : les "
         "secteurs organisés ont obtenu de rester protégés.",
    'p': "La répartition des gains ne résulte pas seulement du marché : elle "
          "dépend aussi de la capacité des groupes à obtenir des exceptions, ce "
          "qui relie la question distributive à l’économie politique."},
   {'f': "Les simulations de l’OMC de 2026 attribuent aux pays les moins avancés "
         "un gain d’environ +7,7 % de PIB dans le scénario de coopération "
         "renforcée, contre +2,9 % pour le PIB mondial.",
    'p': "L’écart indique que les gains potentiels de l’ouverture coordonnée sont "
         "plus que proportionnels pour les économies les plus pauvres, ce qui "
         "nuance la lecture selon laquelle l’ouverture profiterait d’abord aux "
         "pays riches."}],
  [{'q': "Sujet du type « Faut-il indemniser les perdants du libre-échange ? »",
    'f': "La question de l’indemnisation n’est pas un supplément moral apporté à "
         "l’analyse économique : elle en découle directement, puisque le "
         "raisonnement qui établit le gain de l’ouverture postule précisément "
         "qu’il serait possible de compenser les perdants tout en laissant les "
         "gagnants mieux lotis. Ne pas organiser cette compensation revient à "
         "invoquer un argument dont on refuse d’appliquer la condition.",
    'r': "On montre d’abord que la compensation est la condition logique de "
         "l’argument, puis on examine sa faisabilité — coût budgétaire, "
         "efficacité des dispositifs de reconversion, décalage temporel —, enfin "
         "on en tire la conséquence politique.",
    'ex': "La courbe de l’éléphant localise les perdants : les classes moyennes "
          "des économies avancées, dont la stagnation alimente la contestation."},
   {'q': "Sujet du type « Le commerce international profite-t-il à tous les "
         "pays ? »",
    'f': "Le gain à l’échange est mutuel dans les modèles, mais son partage "
         "dépend des termes de l’échange : un pays dont les prix d’exportation "
         "se dégradent relativement à ses prix d’importation voit son gain "
         "s’éroder, jusqu’au cas limite de la croissance appauvrissante décrit "
         "par Bhagwati.",
    'r': "On distingue l’existence du gain, qui est robuste, de son partage, qui "
         "dépend des prix relatifs et donc de la structure de la spécialisation. "
         "Cette séparation permet de soutenir simultanément que l’échange est "
         "mutuellement avantageux et que certains pays en captent une part bien "
         "plus faible que d’autres.",
    'ex': "La croissance appauvrissante : une hausse des volumes exportés qui "
          "déprime les prix mondiaux peut réduire le revenu réel du pays "
          "exportateur."},
   {'q': "Sujet du type « La mondialisation réduit-elle ou accroît-elle les "
         "inégalités ? »",
    'f': "Il faut répondre à deux niveaux distincts : entre pays, l’intégration "
         "commerciale a accompagné un rattrapage de plusieurs économies "
         "émergentes ; au sein des pays avancés, elle a coïncidé avec la "
         "stagnation relative des classes moyennes. L’apparente contradiction "
         "disparaît dès lors qu’on précise le niveau d’agrégation retenu.",
    'r': "Le plan s’organise autour de ces deux échelles, ce qui évite la "
         "juxtaposition d’arguments contradictoires et transforme la "
         "contradiction apparente en résultat.",
    'ex': "La courbe de l’éléphant représente graphiquement cette double "
          "évolution."}],
  voisins=['le28-libre-echange', 'le28-arguments-le', 'le28-couts-ouverture',
           'le28-couts-protectionnisme'])

# ---------------------------------------------------------------- 28.04
d('le28-couts-ouverture', 28,
  "Coûts de l’ouverture et ajustements économiques et sociaux",
  "Ce que coûte la réallocation, et pourquoi elle ne se fait pas toute seule",
  "Les coûts de l’ouverture désignent les pertes supportées pendant et après la "
  "réallocation des facteurs provoquée par la concurrence internationale : "
  "destructions d’emplois dans les branches exposées, dépréciation de "
  "qualifications devenues inutiles, dévitalisation de territoires spécialisés, "
  "coûts budgétaires de l’accompagnement. L’ajustement désigne le processus par "
  "lequel l’économie se réorganise ; il n’est ni instantané, ni gratuit, ni "
  "nécessairement complet.",
  "La théorie du commerce raisonne le plus souvent en comparant deux états — "
  "l’autarcie et l’ouverture — sans décrire le chemin qui mène de l’un à "
  "l’autre. Or c’est ce chemin qui fait l’essentiel du débat politique. "
  "L’ajustement suppose qu’un salarié dont l’usine ferme retrouve un emploi dans "
  "une branche en expansion ; cela exige qu’il possède ou acquière les "
  "qualifications demandées, qu’il accepte une mobilité géographique, et que des "
  "emplois existent effectivement là où il se trouve. Chacune de ces conditions "
  "peut faire défaut. Le coût n’est donc pas seulement transitoire : lorsque la "
  "reconversion échoue, la perte devient permanente et se transmet "
  "territorialement, par la baisse des revenus locaux, puis des services, puis "
  "de l’attractivité. Le cours en tire une conséquence explicite : les gains "
  "agrégés de l’ouverture ne suffisent pas à garantir son acceptabilité, et des "
  "politiques de formation, de reconversion, de mobilité et de redistribution "
  "sont nécessaires. Il admet même qu’une protection temporaire puisse ralentir "
  "la disparition d’activités vieillissantes — non comme un protectionnisme "
  "éducateur visant une industrie naissante, mais comme un accompagnement. "
  "Reconnaître les coûts d’ajustement ne conduit donc pas mécaniquement au "
  "protectionnisme : cela conduit à poser la question du rythme et de "
  "l’accompagnement de l’ouverture.",
  [("Le choc de compétitivité et la destruction d’emplois",
    "L’arrivée de producteurs étrangers à coûts plus faibles réduit la demande "
    "adressée aux producteurs nationaux de la branche exposée, ce qui comprime "
    "l’emploi et les salaires avant même que des fermetures n’interviennent."),
   ("La dépréciation du capital humain spécifique",
    "Les qualifications acquises dans une branche ne sont pas intégralement "
    "transférables. Un salarié expérimenté peut se retrouver en concurrence avec "
    "des débutants dans un autre secteur, ce qui transforme une perte d’emploi "
    "en perte durable de revenu."),
   ("La concentration territoriale des pertes",
    "Les branches exposées sont souvent géographiquement concentrées. La "
    "fermeture d’un établissement réduit les revenus locaux, puis la demande "
    "adressée aux commerces et aux services, enchaînement qui dévitalise un "
    "bassin d’emploi entier."),
   ("L’hystérèse de l’ajustement",
    "Plus l’épisode de chômage se prolonge, plus la réinsertion devient "
    "difficile : les compétences se dégradent et le signal envoyé aux employeurs "
    "se détériore. Un choc transitoire peut ainsi produire des effets durables."),
   ("Le décalage temporel entre gains et pertes",
    "La baisse des prix à l’importation est immédiate et diffuse ; les pertes "
    "d’emploi se matérialisent progressivement et sont concentrées. Le bilan "
    "social perçu est donc plus défavorable que le bilan comptable.")],
  [{'a': "Les coûts d’ajustement justifient des politiques d’accompagnement : "
         "formation, reconversion, aides à la mobilité et redistribution.",
    'cond': "Ces politiques doivent être financées, rapides et ciblées sur les "
            "bassins d’emploi touchés ; une compensation tardive ou diffuse ne "
            "répare pas une perte concentrée et immédiate.",
    'lim': "Leur efficacité est inégale : la reconversion d’un salarié "
           "expérimenté vers une branche différente reste difficile, et aucune "
           "politique ne reconstitue intégralement un capital humain spécifique "
           "devenu inutile."},
   {'a': "Une protection temporaire peut ralentir la disparition d’activités "
         "vieillissantes afin d’étaler le choc dans le temps.",
    'cond': "La protection doit être explicitement transitoire, assortie "
            "d’engagements de restructuration, et accompagnée d’un plan de "
            "reconversion — sans quoi elle finance la survie sans préparer la "
            "transformation.",
    'lim': "Le risque d’entretenir des « canards boiteux » est réel : une "
           "protection prolongée maintient artificiellement des activités "
           "structurellement non compétitives et détourne des ressources des "
           "secteurs en croissance."},
   {'a': "Étaler le rythme de l’ouverture réduit l’ampleur instantanée de "
         "l’ajustement et laisse le temps aux réallocations de s’opérer.",
    'cond': "Le calendrier doit être annoncé, crédible et respecté, faute de quoi "
            "les entreprises diffèrent leurs investissements d’adaptation en "
            "pariant sur une prolongation.",
    'lim': "Un étalement trop long revient à une protection permanente de fait, "
           "et produit exactement les rentes qu’il s’agissait d’éviter."}],
  [{'t': "Les coûts d’ajustement ne sont pas un argument contre l’ouverture mais "
         "contre une ouverture non accompagnée.",
    'qui': "Position défendue dans le cours, qui lie explicitement l’acceptabilité "
           "de l’ouverture aux politiques de formation et de redistribution.",
    'rep': "La thèse est solide, mais elle suppose que l’État dispose des moyens "
           "et de la durée nécessaires ; lorsque ce n’est pas le cas, le choix "
           "pratique se réduit effectivement à ouvrir ou protéger."},
   {'t': "L’accompagnement arrive trop tard : lorsque les politiques de "
         "reconversion se déploient, les pertes sont déjà irréversibles.",
    'qui': "Objection tirée du caractère cumulatif de la dévitalisation "
           "territoriale décrite dans le cours.",
    'rep': "Elle plaide pour anticiper l’accompagnement avant l’ouverture plutôt "
           "que pour y renoncer : c’est l’argument en faveur d’une ouverture "
           "progressive et annoncée."},
   {'t': "Les coûts d’ajustement servent d’argument commode à des secteurs qui "
         "cherchent surtout à préserver une rente.",
    'qui': "Argument de recherche de rente, présent dans le cours à propos des "
           "protections prolongées et du lobbying des entreprises protégées.",
    'rep': "La difficulté est de distinguer l’accompagnement d’une transformation "
           "réelle du financement d’un statu quo. Le critère opérationnel est "
           "l’existence d’engagements vérifiables de restructuration et d’une "
           "date de sortie."}],
  [{'n': "Dani Rodrik",
    'i': "La réponse au déclassement ne peut pas se limiter à la "
         "réindustrialisation : il faut élever la qualité des emplois de "
         "services, où se concentre l’emploi.",
    'p': "Puisque l’industrie n’emploie qu’une minorité des actifs dans les "
         "économies avancées, une politique sociale adossée au seul retour des "
         "emplois industriels ne peut, par construction, traiter qu’une fraction "
         "du problème d’ajustement."},
   {'n': "Branko Milanovic",
    'i': "La courbe de l’éléphant situe précisément les perdants relatifs de la "
         "mondialisation.",
    'p': "Elle montre que la stagnation touche les classes moyennes des économies "
         "avancées, ce qui donne une localisation sociale et géographique aux "
         "coûts d’ajustement et explique leur traduction politique."},
   {'n': "Lionel Fontagné",
    'i': "Les effets de l’ouverture sont ambivalents et doivent être évalués "
         "canal par canal.",
    'p': "Le même ménage peut gagner comme consommateur, par la baisse des prix, "
         "et perdre comme salarié, par la pression sur les salaires : agréger les "
         "deux effets en un solde unique fait disparaître le mécanisme qu’il "
         "s’agit d’expliquer."},
   {'n': "Nicholas Kaldor",
    'i': "La logique de la protection temporaire peut être transposée aux "
         "industries vieillissantes.",
    'p': "Il s’agit alors de protéger temporairement une branche menacée pour lui "
         "permettre de se restructurer ou de monter en gamme, au risque "
         "d’entretenir des activités structurellement non compétitives."}],
  [{'f': "Le cours relève que les mesures protectionnistes provoquent souvent des "
         "représailles et peuvent être contournées par les firmes.",
    'p': "Le coût de l’ouverture doit donc être comparé au coût de la protection, "
         "et non à un état idéal sans ajustement : le bon contrefactuel n’est pas "
         "l’absence de coûts."},
   {'f': "L’ouverture s’est accompagnée, dans les économies avancées, d’une "
         "désindustrialisation dont le cours analyse les causes multiples — "
         "gains de productivité, évolution de la demande, concurrence "
         "internationale.",
    'p': "Attribuer l’intégralité des pertes d’emploi industriel à l’ouverture "
         "serait inexact : la part imputable au commerce doit être distinguée de "
         "celle qui relève de la productivité et de la tertiarisation."},
   {'f': "Les estimations du FMI de 2023 — M. Bolhuis, J. Chen et B. Kett — "
         "évaluent à environ −0,3 % du PIB mondial un découplage stratégique "
         "limité, et à environ −2,3 % une fragmentation en deux blocs.",
    'p': "Le chiffrage donne l’ordre de grandeur du coût de la fermeture, ce qui "
         "permet de mettre en regard les coûts de l’ouverture et ceux de son "
         "inverse."}],
  [{'q': "Sujet du type « Le protectionnisme défensif préserve-t-il l’emploi ou "
         "retarde-t-il les reconversions ? »",
    'f': "Les coûts d’ajustement sont réels, concentrés et parfois irréversibles, "
         "ce qui justifie une intervention ; mais la forme de cette intervention "
         "détermine son résultat. Ralentir le choc pour organiser une "
         "reconversion n’a pas les mêmes effets que financer durablement une "
         "activité qui ne redeviendra pas compétitive.",
    'r': "Le critère discriminant est la présence ou non d’une transformation "
         "effective de la branche protégée : c’est lui qui sépare "
         "l’accompagnement du maintien artificiel. On examine donc successivement "
         "le calendrier de sortie, les engagements de restructuration et le "
         "devenir des salariés, plutôt que le seul niveau de l’emploi préservé.",
    'ex': "Kaldor transpose la protection temporaire aux industries "
          "vieillissantes, en assumant le risque des « canards boiteux »."},
   {'q': "Sujet du type « Faut-il indemniser les perdants du libre-échange ? »",
    'f': "L’indemnisation ne suffit pas si elle se limite à un transfert "
         "monétaire : ce que perd un salarié dont la branche disparaît, c’est "
         "aussi un capital humain spécifique et un environnement productif local. "
         "L’accompagnement efficace combine donc revenu, formation et politique "
         "territoriale.",
    'r': "Décomposer la perte en ses trois dimensions — revenu, qualification, "
         "territoire — permet de montrer pourquoi les dispositifs purement "
         "monétaires échouent à restaurer l’acceptabilité de l’ouverture.",
    'ex': "Rodrik déplace précisément la réponse vers la qualité des emplois de "
          "services, puisque c’est là que se trouve l’emploi."},
   {'q': "Sujet du type « L’ouverture est-elle soutenable politiquement ? »",
    'f': "L’ouverture se heurte à une asymétrie structurelle : ses gains sont "
         "diffus et différés, ses coûts concentrés et immédiats. Cette asymétrie "
         "ne relève pas d’une erreur de perception des électeurs, elle décrit "
         "fidèlement la distribution réelle des effets.",
    'r': "Partir de l’asymétrie plutôt que de la pédagogie permet d’expliquer le "
         "retour du protectionnisme sans invoquer l’irrationalité des opinions, "
         "et conduit à chercher la solution du côté du calendrier et de la "
         "compensation plutôt que du côté de l’explication.",
    'ex': "La courbe de l’éléphant montre où se concentrent les perdants relatifs "
          "dans les économies avancées."}],
  voisins=['le28-gains-repartition', 'le28-vieillissantes', 'le28-defensif',
           'le28-ouverture-progressive', 'le28-libre-echange'])
