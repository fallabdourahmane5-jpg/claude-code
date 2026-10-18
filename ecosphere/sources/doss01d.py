# -*- coding: utf-8 -*-
"""Ensemble 1 — La croissance économique et ses moteurs (3/3, seconde partie)."""

from doss_base import d

d('n1-infrastructures', 1, "Infrastructures et capital public",
  "Un capital qui élève la productivité de tous les autres",
  "Le capital public désigne les équipements collectifs financés par la "
  "collectivité : réseaux de transport, d’énergie, de communication, "
  "équipements sanitaires et éducatifs. Sa particularité est de ne pas produire "
  "directement de valeur marchande mais d’élever la productivité du capital "
  "privé et du travail qui l’utilisent. Barro en fait, en 1990, un moteur "
  "endogène de la croissance.",
  "La logique du capital public se comprend par ce qui le distingue du capital "
  "privé ordinaire. Une route, un réseau électrique, un port ne produisent rien "
  "par eux-mêmes : ils rendent productives les activités qui s’y adossent. "
  "Leur rendement est donc largement externe à celui qui les finance, ce qui "
  "explique à la fois leur sous-production par le marché et leur prise en "
  "charge publique. Barro tire de cette propriété une conclusion forte : parce "
  "que le capital public élève la productivité de l’ensemble du capital privé, "
  "son accumulation échappe aux rendements décroissants qui bornent celle du "
  "capital privé pris isolément. La croissance peut donc être cumulative et "
  "auto-entretenue, et l’investissement public devient un déterminant du taux "
  "de croissance de long terme et non une simple dépense. Cette conclusion "
  "appelle deux précisions. D’abord, le rendement du capital public est "
  "décroissant en pratique : la première route transforme une économie, la "
  "centième autoroute parallèle n’apporte presque rien. Ensuite, le "
  "financement public de ces équipements s’effectue par prélèvement, qui a lui "
  "aussi un coût en efficience : l’effet net dépend de la comparaison entre le "
  "rendement de l’infrastructure et le coût du prélèvement, ce qui est "
  "précisément l’objet du débat sur le niveau optimal de dépense publique.",
  [("La production d’un service non marchand",
    "L’équipement collectif fournit un service — se déplacer, se raccorder, "
    "être soigné — qui n’est pas vendu à son coût mais financé "
    "collectivement, ce qui le rend accessible à tous les producteurs."),
   ("L’élévation de la productivité du capital privé",
    "L’entreprise raccordée à un réseau performant produit davantage avec le "
    "même équipement : le capital public agit comme un multiplicateur de "
    "l’efficacité du capital privé."),
   ("L’externalité et le sous-investissement privé",
    "Le rendement de l’infrastructure se disperse entre tous ses usagers. Aucun "
    "investisseur privé ne pouvant le capter, l’équipement ne serait pas "
    "produit en quantité suffisante par le marché seul."),
   ("Le financement par prélèvement et son coût",
    "La dépense publique suppose un impôt, qui distord les choix des agents. "
    "L’effet net sur la croissance dépend donc de l’écart entre le rendement de "
    "l’équipement et le coût du prélèvement qui le finance."),
   ("Les rendements décroissants en pratique",
    "Les premiers équipements transforment radicalement les conditions de "
    "production ; les suivants ajoutent de moins en moins. Le rendement du "
    "capital public est donc très élevé dans les économies peu équipées et "
    "faible dans celles qui le sont déjà.")],
  [{'a': "L’investissement public en infrastructures élève durablement la "
         "productivité de l’ensemble de l’économie, ce qui en fait un "
         "déterminant du taux de croissance et non une dépense de confort.",
    'cond': "L’équipement doit répondre à un besoin effectif et être "
            "correctement entretenu : un investissement mal ciblé produit un "
            "actif inutilisé dont le coût demeure.",
    'lim': "Le rendement décroît fortement avec le niveau d’équipement déjà "
           "atteint, ce qui réduit la portée de l’argument dans les économies "
           "avancées."},
   {'a': "Il corrige une défaillance de marché identifiée : l’externalité "
         "empêche un financement privé à hauteur de l’optimum collectif.",
    'cond': "La correction suppose que l’État sache évaluer le rendement social "
            "de l’équipement, ce qui exige des procédures d’évaluation "
            "indépendantes.",
    'lim': "La décision publique est exposée aux pressions territoriales, ce "
           "qui peut conduire à financer des équipements dont le rendement "
           "social est faible."},
   {'a': "Il complète les autres facteurs endogènes : des infrastructures de "
         "communication et d’éducation conditionnent le rendement du capital "
         "humain et de la recherche.",
    'cond': "La complémentarité suppose une cohérence des politiques : équiper "
            "sans former, ou former sans équiper, réduit le rendement des deux.",
    'lim': "Cette complémentarité rend l’évaluation séparée de chaque "
           "politique difficile, puisque leurs effets ne sont pas additifs."}],
  [{'t': "Le capital public est financé par un prélèvement dont le coût en "
         "efficience peut excéder le rendement de l’équipement financé, "
         "notamment dans une économie déjà bien dotée.",
    'qui': "Objection tirée de l’analyse du coût du prélèvement et de "
           "l’existence de rendements décroissants des équipements.",
    'rep': "L’objection impose une évaluation projet par projet plutôt qu’une "
           "règle générale : elle ne conclut pas contre l’investissement public "
           "mais contre son augmentation indifférenciée."},
   {'t': "La dépense publique d’investissement est exposée à la capture par des "
         "intérêts locaux, ce qui déconnecte la décision du rendement social "
         "attendu.",
    'qui': "Objection d’économie politique, proche de celle des choix publics.",
    'rep': "Elle justifie des dispositifs d’évaluation ex ante et ex post "
           "indépendants, et non le renoncement à un instrument dont "
           "l’externalité est bien établie."}],
  [{'n': "Robert Barro",
    'i': "Le capital public est un moteur endogène de la croissance, car il "
         "élève la productivité du capital privé qui l’utilise.",
    'p': "Contrairement à Solow, Barro ne considère plus la croissance comme "
         "dépendante d’un progrès technique exogène : elle repose sur "
         "l’accumulation d’un capital spécifique dont les rendements ne sont "
         "pas nécessairement décroissants, ce qui la rend auto-entretenue."},
   {'n': "Robert Lucas",
    'i': "L’accumulation d’un capital spécifique peut rendre la croissance "
         "cumulative et auto-entretenue.",
    'p': "Le raisonnement de Barro sur le capital public reprend la structure de "
         "celui de Lucas sur le capital humain : dans les deux cas, "
         "l’externalité fait que le rendement social excède le rendement privé "
         "et justifie une intervention structurelle de l’État."},
   {'n': "Paul Romer",
    'i': "L’accumulation d’un capital non rival autorise une croissance de long "
         "terme sans épuisement.",
    'p': "Les trois modèles — connaissances chez Romer, qualifications chez "
         "Lucas, équipements collectifs chez Barro — partagent le même "
         "mécanisme, ce qui en fait une famille théorique cohérente plutôt que "
         "trois thèses concurrentes."}],
  [{'f': "Barro publie en 1990 son modèle faisant du capital public un moteur "
         "endogène de la croissance, après Lucas en 1988 sur le capital humain.",
    'p': "L’enchaînement des deux modèles montre la méthode des théories "
         "endogènes : identifier successivement les composantes du résidu de "
         "Solow pour les transformer en variables de décision."},
   {'f': "Le capital public est mentionné douze fois dans le chapitre consacré à "
         "la croissance, exclusivement dans la section consacrée aux théories "
         "endogènes.",
    'p': "La notion n’a de portée analytique que dans ce cadre : hors de lui, "
         "l’investissement public ne serait qu’une composante de la demande."}],
  [{'q': "Sujet du type « L’État peut-il stimuler la croissance ? »",
    'f': "Le capital public fournit le mécanisme le plus clair : les "
         "infrastructures élèvent la productivité du capital privé sans que "
         "leur financeur ne capte ce rendement, ce qui explique à la fois leur "
         "sous-production par le marché et l’effet durable de leur prise en "
         "charge publique sur le taux de croissance.",
    'r': "On déduit le rôle de l’État d’une propriété du bien plutôt que d’une "
         "préférence doctrinale, ce qui rend l’argument opposable à une "
         "objection libérale.",
    'ex': "Le modèle de Barro (1990), où l’accumulation de capital public rend "
          "la croissance auto-entretenue."},
   {'q': "Sujet du type « La dépense publique est-elle un coût ou un "
         "investissement ? »",
    'f': "La distinction n’est pas comptable mais analytique : une dépense est "
         "un investissement lorsqu’elle élève la capacité productive future. Le "
         "capital public remplit ce critère, mais son rendement décroît avec le "
         "niveau d’équipement déjà atteint, ce qui interdit de généraliser "
         "l’argument à toute dépense publique.",
    'r': "On applique un critère unique — effet sur la capacité productive — "
         "puis on en examine le rendement marginal, ce qui évite à la fois "
         "l’apologie et le rejet global.",
    'ex': "Le rendement très élevé des premiers équipements dans une économie "
          "peu dotée, faible dans une économie déjà équipée."}],
  voisins=['n1-endogene', 'n1-capital-humain', 'n1-rd', 'n1-institutions',
           'n1-investissement'])

d('n1-institutions', 1, "Institutions et croissance",
  "Les règles du jeu comme cause fondamentale de la prospérité",
  "Les institutions désignent, selon Douglass North, les règles du jeu d’une "
  "société : règles formelles — droit, contrats, droits de propriété — et "
  "informelles — normes, conventions, confiance. Leur fonction économique "
  "première est de réduire l’incertitude et les coûts de transaction, donc de "
  "rendre possibles des échanges et des investissements qui ne se feraient pas "
  "sans elles.",
  "L’analyse institutionnelle de la croissance répond à une question que les "
  "modèles de facteurs laissent ouverte : pourquoi certains pays accumulent-ils "
  "du capital, forment-ils leur population et innovent-ils, tandis que d’autres "
  "ne le font pas ? La réponse de North est que l’investissement suppose un "
  "horizon : nul n’engage de ressources durables si le droit de propriété sur "
  "le résultat n’est pas protégé, ou si les règles peuvent changer "
  "arbitrairement. Les institutions sont donc antérieures aux facteurs : elles "
  "déterminent s’il est rationnel de les accumuler. Acemoglu et Robinson "
  "systématisent cette intuition dans Pourquoi les nations échouent en opposant "
  "deux configurations. Les institutions inclusives protègent les droits de "
  "propriété, assurent l’État de droit, le pluralisme politique et une "
  "concurrence ouverte : elles favorisent l’innovation, l’investissement, la "
  "mobilité sociale et l’entrepreneuriat. Les institutions extractives "
  "concentrent le pouvoir et les rentes au profit d’un petit groupe, qui a "
  "intérêt à bloquer les transformations menaçant sa position. La thèse est "
  "forte : la cause fondamentale des écarts de prospérité ne serait ni "
  "géographique, ni culturelle, mais institutionnelle. Elle appelle cependant "
  "une réserve méthodologique importante : les institutions sont en partie le "
  "produit de la prospérité qu’elles expliquent, ce qui rend le sens de la "
  "causalité difficile à établir.",
  [("La réduction de l’incertitude",
    "Des règles stables et connues permettent d’anticiper le comportement des "
    "autres. L’agent peut alors s’engager dans des opérations longues, dont le "
    "résultat dépend du respect de ses contrats."),
   ("La baisse des coûts de transaction",
    "Un cadre juridique fiable rend inutile de vérifier et de garantir chaque "
    "échange. Les ressources consacrées à se protéger deviennent disponibles "
    "pour produire."),
   ("La sécurisation de l’investissement",
    "La protection des droits de propriété garantit que celui qui investit "
    "percevra le fruit de son investissement. L’horizon de décision s’allonge, "
    "ce qui autorise l’accumulation et l’innovation."),
   ("Le blocage par les institutions extractives",
    "Lorsque le pouvoir et les rentes sont concentrés, le groupe dominant a "
    "intérêt à empêcher les innovations et la mobilité qui menaceraient sa "
    "position : le blocage n’est pas une défaillance mais un choix rationnel."),
   ("La persistance institutionnelle",
    "Les institutions se reproduisent, car ceux qu’elles avantagent contrôlent "
    "les moyens de les modifier. Les trajectoires nationales deviennent ainsi "
    "très persistantes, ce qui explique la durée des écarts de développement.")],
  [{'a': "Les institutions expliquent les écarts durables de prospérité que les "
         "différences de dotations ne suffisent pas à rendre compte.",
    'cond': "L’argument suppose de pouvoir mesurer la qualité institutionnelle "
            "indépendamment de ses effets économiques, ce qui est "
            "méthodologiquement délicat.",
    'lim': "La causalité est difficile à établir : la prospérité favorise aussi "
           "l’émergence d’institutions protectrices, ce qui rend la relation "
           "réciproque."},
   {'a': "Elles conditionnent le rendement des autres politiques : éducation, "
         "recherche et infrastructures ne produisent leurs effets que dans un "
         "cadre institutionnel fiable.",
    'cond': "La complémentarité suppose que le cadre institutionnel soit "
            "effectivement appliqué, et non seulement inscrit dans les textes.",
    'lim': "Elle rend l’évaluation des politiques sectorielles difficile, "
           "puisque leur rendement dépend d’une variable extérieure à elles."},
   {'a': "Elles fournissent un levier d’action identifié, puisque les règles "
         "peuvent être réformées alors que la géographie ne peut pas l’être.",
    'cond': "La réforme suppose de vaincre la résistance de ceux que les "
            "institutions en place avantagent, ce qui en fait un problème "
            "politique avant d’être technique.",
    'lim': "La persistance institutionnelle rend ces réformes rares et lentes : "
           "identifier le levier ne suffit pas à le manœuvrer."}],
  [{'t': "La causalité peut être inversée : ce sont les économies prospères qui "
         "se dotent d’institutions protectrices, et non l’inverse.",
    'qui': "Objection méthodologique centrale adressée à l’approche "
           "institutionnelle.",
    'rep': "La réciprocité est probable et n’annule pas la thèse : elle suggère "
           "une causalité circulaire, où institutions et prospérité se "
           "renforcent, ce qui explique précisément la persistance des écarts."},
   {'t': "D’autres facteurs que les institutions expliquent la divergence : la "
         "géographie, les ressources disponibles, l’insertion internationale.",
    'qui': "Kenneth Pomeranz, dont La grande divergence compare l’Angleterre et "
           "le delta du Yangzi.",
    'rep': "Le cours présente d’ailleurs la divergence comme plurifactorielle : "
           "l’approche institutionnelle apporte un facteur essentiel sans "
           "prétendre à une cause unique."},
   {'t': "La notion d’institution est si large qu’elle risque d’expliquer tout "
         "et donc rien : droit, normes, confiance, organisation politique y sont "
         "rassemblés.",
    'qui': "Objection sur l’opérationnalité du concept.",
    'rep': "Elle invite à préciser le canal considéré — droits de propriété, "
           "état de droit, concurrence — plutôt qu’à invoquer les institutions "
           "en général."}],
  [{'n': "Douglass North",
    'i': "Les institutions sont les règles du jeu qui réduisent l’incertitude "
         "et permettent l’engagement de long terme.",
    'p': "En abaissant les coûts de transaction et en sécurisant les droits de "
         "propriété, elles rendent rationnelle une accumulation qui, sans elles, "
         "serait trop risquée : les institutions déterminent donc s’il est "
         "rentable d’investir."},
   {'n': "Daron Acemoglu",
    'i': "Les trajectoires économiques dépendent du type d’institutions, "
         "inclusives ou extractives.",
    'p': "Les institutions inclusives protègent les droits de propriété, "
         "assurent l’état de droit, le pluralisme politique et la concurrence ; "
         "elles favorisent l’innovation, l’investissement, la mobilité sociale "
         "et l’entrepreneuriat, là où les institutions extractives les "
         "bloquent."},
   {'n': "James A. Robinson",
    'i': "Les institutions extractives concentrent les rentes et bloquent la "
         "transformation économique.",
    'p': "Co-auteur de Pourquoi les nations échouent : le groupe qui contrôle "
         "les rentes a intérêt à empêcher les innovations menaçant sa position, "
         "de sorte que le blocage est un comportement rationnel et non une "
         "incapacité."},
   {'n': "Dani Rodrik",
    'i': "Les trajectoires de développement dépendent des institutions et des "
         "compromis politiques qui les soutiennent.",
    'p': "Il n’existe pas de configuration institutionnelle unique : des "
         "arrangements différents peuvent remplir les mêmes fonctions "
         "économiques, ce qui interdit de prescrire un modèle institutionnel "
         "standard."}],
  [{'f': "Acemoglu et Robinson opposent, dans Pourquoi les nations échouent, les "
         "institutions inclusives — droits de propriété protégés, état de droit, "
         "pluralisme politique, concurrence — aux institutions extractives.",
    'p': "La typologie fournit la grille la plus utilisée pour relier "
         "organisation politique et performance économique."},
   {'f': "La notion d’institution apparaît dans les quatorze chapitres de la "
         "plateforme, avec une concentration dans ceux consacrés à la croissance "
         "et au développement.",
    'p': "Le caractère transversal de la notion en fait un dossier à mobiliser "
         "hors des seuls sujets de croissance, notamment sur le développement et "
         "la coopération internationale."},
   {'f': "Selon Maddison, le niveau de vie des pays les plus riches représentait "
         "environ trois fois celui des plus pauvres en 1820, et environ dix fois "
         "en 1913.",
    'p': "L’ampleur et la rapidité de la Grande Divergence est précisément ce "
         "que l’approche institutionnelle cherche à expliquer."}],
  [{'q': "Sujet du type « Les institutions sont-elles la cause fondamentale de "
         "la prospérité ? »",
    'f': "La thèse institutionnelle ne prétend pas que les institutions "
         "produisent directement la richesse : elle soutient qu’elles "
         "déterminent s’il est rationnel d’accumuler du capital, de se former "
         "et d’innover. Les institutions sont donc une cause fondamentale au "
         "sens où elles commandent les causes immédiates, ce qui déplace "
         "l’explication d’un cran en amont.",
    'r': "Distinguer causes fondamentales et causes immédiates permet d’articuler "
         "North et Acemoglu avec les modèles de facteurs, au lieu de les "
         "opposer.",
    'ex': "L’écart de niveau de vie, qui passe d’un rapport de trois en 1820 à "
          "un rapport de dix en 1913 selon Maddison."},
   {'q': "Sujet du type « Un pays peut-il se développer sans État fort ? »",
    'f': "L’approche institutionnelle répond que ce qui importe n’est pas la "
         "taille de l’État mais la nature des règles : un État fort mais "
         "extractif bloque le développement, un État limité mais garantissant "
         "droits de propriété et état de droit le permet. La question de la "
         "force se substitue mal à celle de la qualité institutionnelle.",
    'r': "On reformule le sujet en substituant à l’axe faible/fort l’axe "
         "inclusif/extractif, ce qui permet de traiter les cas apparemment "
         "contradictoires.",
    'ex': "L’opposition entre institutions inclusives et extractives chez "
          "Acemoglu et Robinson."}],
  voisins=['n1-droits-propriete', 'n1-endogene', 'n1-convergence',
           'n1-rattrapage', 'n1-croissance'])

d('n1-droits-propriete', 1, "Droits de propriété",
  "Sans garantie sur le fruit, pas d’engagement durable",
  "Les droits de propriété désignent l’ensemble des prérogatives juridiquement "
  "protégées permettant à un agent d’user d’un bien, d’en percevoir les revenus "
  "et de le céder. Leur protection est, chez North, la condition "
  "institutionnelle de l’investissement : elle garantit que celui qui engage "
  "des ressources percevra le fruit de son engagement, ce qui rend rationnelle "
  "une décision dont le rendement est différé.",
  "Le raisonnement est d’une grande simplicité logique et d’une portée "
  "considérable. Un investissement consiste à renoncer à une consommation "
  "présente pour un revenu futur. Si le droit sur ce revenu futur n’est pas "
  "garanti — parce qu’il peut être exproprié, taxé arbitrairement, ou "
  "contesté sans recours —, l’arbitrage se renverse : il devient rationnel de "
  "consommer immédiatement ou de placer ses ressources hors d’atteinte. "
  "L’absence de droits de propriété protégés ne produit donc pas seulement une "
  "injustice : elle produit un sous-investissement et une mauvaise allocation "
  "des ressources. Le même raisonnement s’applique à la propriété "
  "intellectuelle : sans exclusivité temporaire, l’inventeur ne capte pas le "
  "rendement de sa découverte et sous-investit en recherche. Deux précisions "
  "s’imposent cependant. D’abord, la protection des droits de propriété n’a de "
  "valeur que si elle est effective : un droit inscrit dans un texte mais non "
  "garanti par un juge indépendant ne modifie pas les anticipations. Ensuite, "
  "une protection excessive peut bloquer l’usage des ressources : la propriété "
  "intellectuelle trop étendue freine l’innovation cumulative, et l’absence de "
  "mécanismes d’expropriation pour cause d’utilité publique empêche "
  "l’aménagement collectif. Les droits de propriété ne sont donc pas un absolu "
  "à maximiser mais un dispositif à calibrer.",
  [("La garantie du revenu futur",
    "Le droit protégé assure à l’investisseur la perception des revenus de son "
    "bien. L’horizon de décision s’allonge, ce qui autorise les engagements "
    "longs et irréversibles."),
   ("L’effet sur l’allocation des ressources",
    "La possibilité de céder un bien permet qu’il aille à celui qui en tire le "
    "plus de valeur. Sans droit de cession, les ressources restent immobilisées "
    "chez des détenteurs qui les utilisent mal."),
   ("L’usage du bien comme garantie",
    "Un droit de propriété certain permet d’hypothéquer un actif pour obtenir "
    "un financement. La sécurisation juridique ouvre donc l’accès au crédit, "
    "donc à l’investissement."),
   ("Le cas de la propriété intellectuelle",
    "L’exclusivité temporaire sur une invention permet à l’inventeur de capter "
    "une rente qui finance sa recherche. Le brevet transpose la logique de la "
    "propriété à un bien non rival."),
   ("L’arbitrage entre protection et usage",
    "Une protection trop faible décourage l’investissement ; trop forte, elle "
    "bloque l’usage collectif et l’innovation cumulative. Le niveau de "
    "protection est donc l’objet d’un arbitrage, pas d’un principe absolu.")],
  [{'a': "La protection des droits de propriété est la condition de "
         "l’investissement de long terme, donc de l’accumulation et de "
         "l’innovation.",
    'cond': "La protection doit être effective, ce qui suppose un appareil "
            "judiciaire indépendant et des procédures accessibles à tous les "
            "agents, non aux seuls plus puissants.",
    'lim': "Un droit effectif pour certains seulement produit une protection "
           "sélective, qui est l’une des formes de l’institution extractive "
           "décrite par Acemoglu et Robinson."},
   {'a': "Elle améliore l’allocation des ressources, en permettant que les "
         "actifs soient cédés à ceux qui en tirent le plus de valeur.",
    'cond': "La cessibilité suppose des marchés fonctionnels et une information "
            "suffisante sur la qualité des biens échangés.",
    'lim': "Appliquée à certaines ressources — communs naturels, services "
           "essentiels — la cessibilité peut produire des exclusions socialement "
           "inacceptables."},
   {'a': "Elle élargit l’accès au crédit, puisqu’un bien dont la propriété est "
         "certaine peut servir de garantie.",
    'cond': "Il faut un cadastre ou un registre fiable, condition souvent "
            "absente dans les économies à forte informalité.",
    'lim': "L’accès au crédit par le gage expose aussi les détenteurs les plus "
           "fragiles à la perte de leur bien en cas de choc."}],
  [{'t': "Les droits de propriété peuvent protéger des rentes plutôt que des "
         "investissements, lorsqu’ils garantissent des positions acquises contre "
         "toute remise en cause.",
    'qui': "Objection tirée de l’analyse des institutions extractives et de la "
           "recherche de rente.",
    'rep': "L’objection distingue utilement la protection du fruit d’un effort "
           "et celle d’une position héritée : c’est pourquoi la protection doit "
           "aller de pair avec la concurrence et l’état de droit."},
   {'t': "Une propriété intellectuelle trop étendue freine l’innovation "
         "cumulative, puisque chaque chercheur doit négocier l’accès aux brevets "
         "antérieurs.",
    'qui': "Objection issue de l’arbitrage entre incitation et diffusion dans "
           "l’économie de l’innovation.",
    'rep': "Elle conduit à calibrer durée et étendue de la protection plutôt "
           "qu’à la supprimer : sans exclusivité, le financement privé de la "
           "recherche disparaît."}],
  [{'n': "Douglass North",
    'i': "Droits de propriété, stabilité institutionnelle et investissement "
         "forment une chaîne causale : le premier conditionne le dernier.",
    'p': "Sans garantie sur le revenu futur, l’agent préfère la consommation "
         "immédiate ou la mise à l’abri de ses ressources : l’absence de droits "
         "protégés produit mécaniquement du sous-investissement."},
   {'n': "Daron Acemoglu",
    'i': "La protection des droits de propriété est l’une des caractéristiques "
         "définissant les institutions inclusives.",
    'p': "Dans la typologie d’Acemoglu et Robinson, droits de propriété "
         "protégés, état de droit, pluralisme politique et concurrence forment "
         "un ensemble cohérent qui favorise l’innovation et l’entrepreneuriat."},
   {'n': "Ronald Coase",
    'i': "L’allocation des ressources dépend de la définition initiale des "
         "droits et du niveau des coûts de transaction.",
    'p': "Si les droits sont clairement attribués et que la négociation est peu "
         "coûteuse, les agents peuvent échanger ces droits jusqu’à une "
         "allocation efficace : la propriété devient alors un instrument de "
         "résolution des externalités."}],
  [{'f': "Les droits de propriété sont mentionnés vingt fois dans le chapitre "
         "consacré aux défaillances du marché et dix fois dans celui consacré à "
         "la croissance.",
    'p': "La notion fait le lien entre l’analyse des externalités et celle de la "
         "croissance : elle est simultanément un instrument d’allocation et une "
         "condition d’accumulation."},
   {'f': "Les institutions inclusives décrites par Acemoglu et Robinson "
         "associent droits de propriété protégés, état de droit, pluralisme "
         "politique et concurrence ouverte.",
    'p': "La protection de la propriété n’opère pas isolément : elle n’a d’effet "
         "que combinée aux autres composantes du cadre institutionnel."}],
  [{'q': "Sujet du type « Les institutions sont-elles la cause fondamentale de "
         "la prospérité ? »",
    'f': "Les droits de propriété fournissent le canal le plus précis par lequel "
         "les institutions agissent sur l’économie : ils déterminent si "
         "l’investissement est rationnel. L’argument est d’autant plus solide "
         "qu’il ne suppose aucune hypothèse sur les préférences : il suffit que "
         "les agents comparent un rendement futur incertain à une consommation "
         "présente certaine.",
    'r': "Partir d’un arbitrage individuel pour en déduire un effet "
         "macroéconomique donne au raisonnement institutionnel une base "
         "microéconomique, ce qui le rend plus difficile à contester.",
    'ex': "La chaîne décrite par North : droits de propriété, stabilité "
          "institutionnelle, investissement."},
   {'q': "Sujet du type « Faut-il breveter les innovations ? »",
    'f': "Le brevet transpose la logique de la propriété à un bien non rival, ce "
         "qui produit une tension irréductible : l’exclusivité restaure "
         "l’incitation à inventer mais ralentit la diffusion, qui est "
         "précisément la source des rendements croissants de la connaissance.",
    'r': "On montre que la question n’admet pas de réponse en oui ou non mais "
         "une réponse en durée et en étendue de protection, ce qui déplace le "
         "débat vers le calibrage.",
    'ex': "Le monopole temporaire décrit par Howitt, qui finance l’innovation "
          "avant d’être détruit par la suivante."}],
  voisins=['n1-institutions', 'n1-rd', 'n1-endogene', 'n1-croissance'])

d('n1-convergence', 1, "Convergence et divergence des économies",
  "Les écarts de richesse se résorbent-ils ou se creusent-ils ?",
  "La convergence désigne le rattrapage des économies les moins riches sur les "
  "plus riches, qui se traduirait par une réduction des écarts de produit par "
  "habitant. La divergence désigne le mouvement inverse. Le modèle de Solow "
  "prédit une convergence conditionnelle : les pays à faible stock de capital "
  "par tête ont un rendement du capital plus élevé, donc une croissance plus "
  "rapide — mais seulement à paramètres structurels comparables.",
  "La question de la convergence met à l’épreuve les théories de la croissance, "
  "et son traitement suppose de bien poser l’adjectif « conditionnelle ». Dans "
  "le modèle de Solow, le rendement décroissant du capital implique qu’un pays "
  "pauvre, peu doté en capital par travailleur, obtienne de chaque unité "
  "investie un rendement supérieur à celui d’un pays riche. Il croît donc plus "
  "vite et rattrape — mais il ne rattrape que le niveau correspondant à ses "
  "propres paramètres : taux d’épargne, démographie, accès à la technologie. "
  "Deux pays aux paramètres différents convergent vers deux états "
  "stationnaires différents, et l’écart entre eux ne se résorbe pas. C’est ce "
  "qui réconcilie le modèle avec les faits. Car les faits sont "
  "spectaculairement divergents sur longue période : d’après Maddison, le "
  "niveau de vie des pays les plus riches représentait environ trois fois celui "
  "des plus pauvres en 1820, et environ dix fois en 1913. Le cours nomme ce "
  "mouvement la Grande Divergence, en observant une convergence entre Europe "
  "occidentale et Amérique du Nord simultanée à une divergence avec une partie "
  "du reste du monde. Les théories endogènes expliquent cette persistance : si "
  "l’accumulation de connaissances et de capital humain présente des rendements "
  "non décroissants, les pays les mieux dotés accumulent plus vite, et l’écart "
  "se creuse au lieu de se combler.",
  [("Le rendement décroissant comme moteur du rattrapage",
    "Un pays peu doté en capital par travailleur tire un rendement élevé de "
    "chaque unité investie. Son taux de croissance est donc supérieur, ce qui "
    "produit mécaniquement un rattrapage."),
   ("Le caractère conditionnel de la convergence",
    "Chaque économie converge vers son propre état stationnaire, déterminé par "
    "son taux d’épargne, sa démographie et sa technologie. Des paramètres "
    "différents produisent des niveaux de long terme différents."),
   ("La divergence par les rendements non décroissants",
    "Si les connaissances et le capital humain s’accumulent à rendements non "
    "décroissants, l’avance initiale se transforme en avance croissante : la "
    "divergence devient le résultat normal."),
   ("Le rôle des institutions dans la sélection du régime",
    "Ce qui détermine si un pays converge ou décroche n’est pas seulement son "
    "stock de capital mais sa capacité à protéger l’investissement, à former sa "
    "population et à absorber les technologies — donc son cadre "
    "institutionnel.")],
  [{'a': "La convergence conditionnelle explique les rattrapages rapides "
         "observés : un pays peu doté qui adopte des paramètres structurels "
         "comparables à ceux des pays avancés croît mécaniquement plus vite.",
    'cond': "Il faut un taux d’investissement élevé, un accès effectif aux "
            "technologies et des institutions sécurisant l’accumulation.",
    'lim': "Le rattrapage s’arrête à l’état stationnaire propre au pays : sans "
           "modification de ses paramètres, la convergence est partielle."},
   {'a': "Le modèle fournit un critère de diagnostic : un pays qui ne converge "
         "pas malgré un faible stock de capital révèle un problème de "
         "paramètres, non de dotation.",
    'cond': "L’interprétation suppose de pouvoir estimer les paramètres "
            "structurels, ce qui est délicat pour les économies à forte "
            "informalité.",
    'lim': "Elle risque d’attribuer à des choix nationaux ce qui relève de "
           "contraintes extérieures, notamment de l’insertion internationale."},
   {'a': "L’approche par la divergence explique la persistance des écarts, que "
         "la seule convergence conditionnelle rendrait difficilement "
         "compréhensible.",
    'cond': "Elle suppose l’existence effective d’externalités cumulatives dans "
            "la connaissance et le capital humain.",
    'lim': "Elle prédit une divergence indéfinie, ce que contredisent les "
           "rattrapages asiatiques : les deux mécanismes coexistent donc selon "
           "les pays."}],
  [{'t': "La convergence prédite par Solow n’est pas observée sur longue "
         "période : les écarts se sont au contraire creusés.",
    'qui': "Données historiques de Maddison, qui montrent un écart passant "
           "d’environ trois à environ dix entre 1820 et 1913.",
    'rep': "Le modèle prédit une convergence conditionnelle, non absolue : des "
           "pays aux paramètres différents convergent vers des niveaux "
           "différents. L’objection vise une version du modèle qu’il ne défend "
           "pas."},
   {'t': "La convergence n’est ni générale ni automatique : certains pays "
         "rattrapent rapidement, d’autres décrochent durablement.",
    'qui': "Constat des trajectoires contrastées, notamment entre Asie et "
           "Afrique, discuté dans le chapitre consacré au développement.",
    'rep': "L’hétérogénéité des trajectoires est précisément ce que l’approche "
           "institutionnelle vient expliquer : ce n’est pas la dotation initiale "
           "mais la capacité à transformer les paramètres qui décide."}],
  [{'n': "Robert Solow",
    'i': "Le modèle implique une convergence conditionnelle : les pays à faible "
         "stock de capital ont un rendement plus élevé, donc un rattrapage plus "
         "rapide.",
    'p': "Cette vision auto-équilibrante est à la fois la force et la limite du "
         "modèle : elle explique les rattrapages mais rend la persistance des "
         "écarts difficile à comprendre sans invoquer des différences de "
         "paramètres structurels."},
   {'n': "Angus Maddison",
    'i': "Les séries longues établissent l’ampleur de la Grande Divergence et "
         "le poids historique des économies aujourd’hui émergentes.",
    'p': "En 1820, le niveau de vie des pays les plus riches représente environ "
         "trois fois celui des plus pauvres ; en 1913, environ dix fois. Les "
         "données chiffrent la divergence et rappellent qu’elle est récente à "
         "l’échelle de l’histoire."},
   {'n': "Kenneth Pomeranz",
    'i': "La Grande Divergence entre l’Angleterre et le delta du Yangzi ne "
         "s’explique pas par une supériorité préexistante.",
    'p': "La comparaison montre que deux régions comparables au départ ont "
         "bifurqué, ce qui déplace l’explication vers des facteurs "
         "institutionnels, géographiques et d’insertion internationale plutôt "
         "que vers une avance initiale."}],
  [{'f': "Selon Maddison, le niveau de vie des pays les plus riches représentait "
         "environ trois fois celui des plus pauvres en 1820, et environ dix fois "
         "en 1913.",
    'p': "L’ordre de grandeur chiffre la Grande Divergence et montre qu’elle "
         "s’est produite pendant la première mondialisation, non malgré elle."},
   {'f': "Le cours observe une convergence entre Europe occidentale et Amérique "
         "du Nord simultanée à une divergence avec une partie du reste du monde.",
    'p': "Convergence et divergence sont donc des phénomènes concomitants : la "
         "question n’est pas de choisir entre les deux mais d’identifier à "
         "quels groupes de pays chacune s’applique."}],
  [{'q': "Sujet du type « Pourquoi certains pays rattrapent-ils les pays "
         "développés tandis que d’autres restent en retard ? »",
    'f': "La convergence prédite par Solow est conditionnelle : chaque économie "
         "ne rattrape que le niveau correspondant à ses propres paramètres — "
         "taux d’épargne, démographie, accès à la technologie. Le rattrapage "
         "n’est donc pas une récompense de la pauvreté initiale mais la "
         "conséquence d’une transformation des paramètres structurels.",
    'r': "Le mot « conditionnelle » organise toute la réponse : il permet de "
         "tenir ensemble la prédiction théorique et l’observation de "
         "trajectoires contrastées.",
    'ex': "Les données de Maddison, qui montrent un écart creusé de trois à dix "
          "entre 1820 et 1913."},
   {'q': "Sujet du type « La mondialisation réduit-elle les écarts de "
         "développement ? »",
    'f': "L’histoire longue invite à la prudence : c’est pendant la première "
         "mondialisation que l’écart de niveau de vie entre pays riches et pays "
         "pauvres est passé d’un rapport de trois à un rapport de dix. "
         "L’ouverture n’a donc pas produit mécaniquement la convergence, même "
         "si certains pays l’ont utilisée pour rattraper.",
    'r': "Confronter la prédiction théorique aux séries longues évite la "
         "généralité et impose de distinguer les pays selon leur capacité "
         "d’absorption.",
    'ex': "La Grande Divergence décrite par Maddison et analysée par Pomeranz."}],
  voisins=['n1-rattrapage', 'n1-institutions', 'n1-accumulation',
           'n1-endogene', 'n1-croissance'])
