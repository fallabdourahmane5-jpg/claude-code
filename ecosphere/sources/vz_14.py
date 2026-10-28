# -*- coding: utf-8 -*-
"""Visualisation 14 — L’entreprise : nature, taille et gouvernance (hub)."""

from vz_base import v, nd, ln

v('vz-entreprise', 'L’entreprise : nature, taille et gouvernance',
  'Chapitres 8 et 9 · noyau et branches',
  'hub',
  "Une seule question commande tout le chapitre : si le marché coordonnait "
  "parfaitement les échanges, pourquoi créer de grandes organisations "
  "hiérarchiques ? Les branches en déploient les conséquences : ce qui fixe "
  "la frontière de la firme, ce qui en détermine la taille, qui la dirige "
  "réellement, pour qui elle est dirigée, et ce que cela coûte.",
  [("Partir de la question de Coase",
    "L’entreprise n’est pas une évidence : elle existe parce que recourir au "
    "marché coûte quelque chose. Toute copie sur l’entreprise gagne à partir "
    "de là plutôt que d’une définition juridique."),
   ("Trois capitalismes successifs",
    "Entrepreneurial : propriété et pouvoir confondus. Managérial : la "
    "direction se professionnalise et se sépare de la propriété. "
    "Actionnarial : les actionnaires reprennent le contrôle par la "
    "gouvernance. La séquence structure le chapitre."),
   ("Ne pas confondre taille et pouvoir de marché",
    "La concentration est un processus de croissance ; le pouvoir de marché "
    "en est une conséquence possible, pas automatique. Les formes — "
    "horizontale, verticale, conglomérale — n’ont pas les mêmes effets sur "
    "la concurrence.")],
  [
   nd('coeur', 'Pourquoi des entreprises ?', 'coeur',
      "Si le marché coordonnait parfaitement, tout pourrait être acheté "
      "directement. La firme existe parce que recourir au marché a un coût.",
      grp=0,
      defi="L’entreprise est une organisation qui combine des facteurs de "
           "production pour produire des biens et des services vendus sur un "
           "marché. Mais le cours insiste sur une question plus profonde : si "
           "le marché coordonnait parfaitement les échanges, pourquoi créer "
           "de grandes organisations hiérarchiques, salarier durablement des "
           "travailleurs et intégrer des activités, alors que tout pourrait "
           "être acheté directement sur le marché ?",
      mec=[("Le coût du recours au marché",
            "Chercher un fournisseur, négocier, rédiger un contrat, en "
            "vérifier l’exécution : ces opérations coûtent du temps et de "
            "l’argent. Ce sont ces coûts de transaction qui rendent la "
            "coordination hiérarchique parfois préférable."),
           ("Deux modes de coordination distincts",
            "Le marché coordonne par le prix, la firme par l’autorité. Ce ne "
            "sont pas deux degrés d’une même chose mais deux logiques "
            "différentes, entre lesquelles l’entreprise arbitre en "
            "permanence."),
           ("Les formes hybrides",
            "Les entreprises organisent aujourd’hui des réseaux complexes de "
            "sous-traitance et de coopération le long de chaînes de "
            "production mondialisées : la frontière entre firme et marché "
            "n’est pas une ligne nette mais un continuum.")],
      aut=[{'n': "Ronald Coase",
            'i': "La firme existe parce qu’il y a un coût à recourir au "
                 "marché, c’est-à-dire des coûts de transaction."},
           {'n': "Armen Alchian",
            'i': "La firme est un nœud de contrats entre des acteurs aux "
                 "intérêts divers tenus de travailler ensemble."}],
      faits=[{'f': "Le cours prend l’exemple d’une entreprise de "
                   "déménagement, où le travail exige coordination, confiance "
                   "et habitudes communes.",
              'p': "L’exemple établit que certaines activités ne peuvent pas "
                   "être recomposées à chaque fois sur le marché et "
                   "justifient des équipes stables, donc une entreprise."}],
      termes=['entreprise', 'cout de transaction', 'coase', 'firme'],
      dos=['n8-entreprise', 'n8-couts-de-transaction']),

   nd('frontieres', 'La frontière de la firme', 'pilier',
      "Faire ou faire faire : la firme internalise tant que le marché lui "
      "coûte plus cher que l’organisation interne.",
      grp=1,
      defi="Les frontières de la firme désignent la limite entre les "
           "activités que l’entreprise réalise elle-même et celles qu’elle "
           "achète sur le marché. Le cours les fait dépendre d’une "
           "comparaison : la firme internalise tant que les coûts de "
           "transaction du recours au marché dépassent les coûts "
           "d’internalisation. Williamson précise que ces frontières "
           "dépendent de la nature des actifs gérés et de la fréquence des "
           "transactions.",
      mec=[("L’arbitrage comptable",
            "Déléguer le nettoyage évite de gérer recrutement, formation, "
            "absences et congés ; employer directement implique salaires, "
            "cotisations sociales, retraite, congés payés et formation. "
            "L’arbitrage n’est pas idéologique mais comptable."),
           ("L’incomplétude du contrat",
            "Un contrat prévoyant un passage mensuel oblige à renégocier dès "
            "qu’un imprévu survient : ce n’est pas le prix de la prestation "
            "qui pose problème, c’est l’imprévu."),
           ("La spécificité des actifs",
            "Plus un actif est spécifique à une relation, plus le partenaire "
            "peut en abuser une fois l’investissement réalisé : "
            "l’internalisation protège contre ce risque.")],
      aut=[{'n': "Oliver Williamson",
            'i': "Les frontières de la firme dépendent de la nature des "
                 "actifs qu’elle gère et de la fréquence des transactions "
                 "qu’elle réalise."}],
      faits=[{'f': "Le capitalisme contemporain combine grandes entreprises "
                   "intégrées, petites et moyennes entreprises, plateformes, "
                   "réseaux, sous-traitance et intégration verticale.",
              'p': "Cette diversité confirme qu’il n’existe pas de frontière "
                   "optimale unique : la limite varie selon les actifs, les "
                   "fréquences et les secteurs."}],
      termes=['frontieres de la firme', 'externalisation',
              'integration verticale'],
      dos=['n8-frontieres-firme', 'n8-externalisation',
           'n8-integration-verticale']),

   nd('taille', 'La croissance et la concentration', 'pilier',
      "Croissance interne ou externe ; concentration horizontale, verticale "
      "ou conglomérale. Trois formes, trois logiques distinctes.",
      grp=1,
      defi="La concentration est le processus par lequel les entreprises "
           "augmentent leur taille, par fusion, rachat, regroupement ou "
           "augmentation des capacités de production. Le cours distingue deux "
           "voies de croissance — interne par les investissements propres, "
           "externe par fusion ou rachat — et trois formes de concentration : "
           "horizontale, verticale et conglomérale.",
      mec=[("La concentration horizontale",
            "Racheter ses concurrents sur le même marché accroît la part de "
            "marché et le pouvoir sur les prix : c’est la forme qui appelle "
            "le plus directement une réponse de la politique de la "
            "concurrence."),
           ("La concentration verticale",
            "Intégrer fournisseurs ou distributeurs supprime la marge de "
            "l’intermédiaire et sécurise l’approvisionnement : le gain est un "
            "coût évité plus qu’un pouvoir acquis."),
           ("La logique conglomérale",
            "Rassembler des activités indépendantes ne vise ni un marché ni "
            "une chaîne mais la diversification des risques entre secteurs "
            "sans rapport entre eux.")],
      aut=[{'n': "Claire Lemercier",
            'i': "Plusieurs formes d’organisation des entreprises coexistent, "
                 "distribuées et intégrées."},
           {'n': "Alfred Marshall",
            'i': "La proximité géographique des entreprises engendre des "
                 "effets d’agglomération."}],
      faits=[{'f': "John D. Rockefeller fonde la Standard Oil Company en 1870 "
                   "et passe, en rachetant ses concurrents, de dix pour cent "
                   "du marché à environ quatre-vingt-dix pour cent du "
                   "raffinage américain.",
              'p': "Le cas montre la puissance de la concentration "
                   "horizontale et la raison de son encadrement : une "
                   "réussite d’entreprise finit par inquiéter l’État et "
                   "provoque les politiques antitrust."},
             {'f': "Les grandes dépressions de 1873-1896 et de 1929 sont "
                   "suivies de vagues massives de concentration.",
              'p': "La récurrence établit que la concentration n’est pas "
                   "seulement un choix stratégique : elle est accélérée par "
                   "les crises, qui rendent les entreprises fragilisées plus "
                   "faciles à absorber."}],
      termes=['concentration', 'croissance externe', 'conglomerat',
              'fusion acquisition'],
      dos=['n8-concentration-croissance', 'n5-concentration']),

   nd('direction', 'Qui dirige : la séparation propriété / contrôle',
      'pilier',
      "Les actionnaires détiennent le capital, les managers assurent la "
      "direction. Le capitalisme entrepreneurial laisse place au capitalisme "
      "managérial.",
      grp=1,
      defi="La séparation entre propriété et contrôle désigne la situation "
           "des grandes entreprises modernes dans lesquelles les actionnaires "
           "détiennent le capital tandis que les managers assurent la "
           "direction effective. Le cours l’oppose au capitalisme "
           "entrepreneurial, où la propriété du capital et le pouvoir de "
           "décision sont confondus dans la personne de l’entrepreneur.",
      mec=[("La cause matérielle",
            "Une grande entreprise sidérurgique ou ferroviaire ne peut plus "
            "être dirigée à l’intuition par son propriétaire : il faut "
            "planifier la production, coordonner des milliers de salariés, "
            "gérer les finances et organiser les approvisionnements."),
           ("La professionnalisation de la direction",
            "Le développement des écoles de commerce et de formations dédiées "
            "à la gestion démontre que la compétence de direction est devenue "
            "un savoir transmissible, distinct de la possession du capital."),
           ("La transformation des structures internes",
            "La forme unitaire, centralisée par fonctions, cède du terrain à "
            "la forme multidivisionnelle, décentralisée en unités autonomes "
            "avec une direction stratégique centrale.")],
      aut=[{'n': "Adolf Berle",
            'i': "Dans les grandes entreprises modernes, les actionnaires "
                 "détiennent le capital mais les managers assurent la "
                 "direction."},
           {'n': "Gardiner Means",
            'i': "La délégation du pouvoir aux managers est une nécessité "
                 "organisationnelle et non un choix des actionnaires."},
           {'n': "John Kenneth Galbraith",
            'i': "La technostructure réunit dirigeants, cadres, ingénieurs et "
                 "experts qui participent à la direction effective de "
                 "l’entreprise."},
           {'n': "Henri Fayol",
            'i': "Diriger une entreprise repose sur cinq fonctions : prévoir, "
                 "organiser, commander, coordonner, contrôler."}],
      termes=['propriete et controle', 'technostructure',
              'capitalisme managerial'],
      dos=['n8-propriete-controle', 'n8-capitalisme-managerial']),

   nd('gouvernance', 'Pour qui : la gouvernance d’entreprise', 'pilier',
      "Réduire l’asymétrie entre actionnaires et managers par le contrôle et "
      "l’incitation. L’expression s’impose dans les années 1990.",
      grp=1,
      defi="La gouvernance d’entreprise désigne l’ensemble des règles de "
           "fonctionnement des sociétés anonymes visant à réduire les "
           "asymétries d’information entre actionnaires et managers, à "
           "inciter les managers à gérer l’entreprise dans l’intérêt des "
           "actionnaires et à faire en sorte que la valeur des actions "
           "augmente. L’expression s’impose dans les années 1990.",
      mec=[("La relation d’agence",
            "La gouvernance se formalise par la théorie de l’agence : un "
            "principal délègue à un agent dont les intérêts diffèrent des "
            "siens et dont il n’observe pas tous les comportements."),
           ("Les deux familles de dispositifs",
            "Le contrôle, par le conseil d’administration et l’audit ; "
            "l’incitation, par la distribution de stock-options. Deux "
            "logiques dont les effets pervers sont de nature différente."),
           ("Le coût du dispositif",
            "Le contrôle de l’agent par le principal engendre des coûts "
            "d’agence, pour l’essentiel des coûts de surveillance : la "
            "solution au problème a elle-même un prix.")],
      opp=[{'t': "La gouvernance repose sur une information produite par ceux "
                 "qu’elle est censée contrôler.",
            'qui': "leçon du scandale Enron",
            'rep': "La vulnérabilité est structurelle : en 2001, des "
                   "manipulations comptables ont conduit à une faillite "
                   "retentissante. Le remède passe par l’indépendance de "
                   "l’audit, non par davantage de la même information."}],
      aut=[{'n': "Michael Jensen",
            'i': "La gouvernance d’entreprise se formalise par la théorie de "
                 "l’agence, qui analyse la délégation de pouvoir du principal "
                 "à l’agent."},
           {'n': "William Meckling",
            'i': "Le contrôle de l’agent par le principal engendre des coûts "
                 "d’agence, pour l’essentiel des coûts de surveillance."}],
      faits=[{'f': "Les stock-options sont attribuées à un prix souvent plus "
                   "faible que celui du marché, avec une fiscalité "
                   "avantageuse lorsque les actions sont conservées un "
                   "certain temps.",
              'p': "Le détail technique montre que l’incitation est "
                   "construite pour lier durablement le dirigeant au cours de "
                   "l’action, donc à l’objectif de valeur actionnariale."}],
      termes=['gouvernance d entreprise', 'relation d agence',
              'valeur actionnariale'],
      dos=['n8-gouvernance', 'n8-relation-agence',
           'n8-valeur-actionnariale']),

   nd('rse', 'Pour qui, autrement : parties prenantes et RSE', 'debat',
      "Intégrer aux objectifs économiques des préoccupations sociales et "
      "environnementales — avec le greenwashing pour risque constitutif.",
      grp=1,
      defi="La responsabilité sociale des entreprises consiste à intégrer, "
           "aux objectifs économiques de la firme, des préoccupations "
           "sociales et environnementales, de sorte que l’entreprise devient "
           "un acteur du développement durable. Le cours la présente comme la "
           "réponse aux limites du capitalisme actionnarial, et en signale "
           "immédiatement le risque : le greenwashing.",
      mec=[("L’élargissement du cercle des destinataires",
            "Le cours précise les destinataires : les salariés, les "
            "consommateurs, l’environnement, le territoire et l’image sociale "
            "de l’entreprise. Chacun peut faire l’objet d’engagements "
            "vérifiables."),
           ("L’inscription dans le droit",
            "La loi PACTE, en 2019, introduit en France la notion de raison "
            "d’être et le statut d’entreprise à mission : l’entreprise peut "
            "désormais poursuivre des objectifs autres que le profit."),
           ("La vérifiabilité comme condition",
            "L’engagement déclaré ne vaut pas preuve : sans mesure "
            "indépendante, la responsabilité volontaire se réduit à une "
            "communication.")],
      opp=[{'t': "La responsabilité sociale de l’entreprise consiste à "
                 "augmenter ses profits ; tout autre objectif dépense l’argent "
                 "d’autrui.",
            'qui': "Milton Friedman",
            'rep': "L’objection a une portée réelle sur la légitimité du "
                   "dirigeant à arbitrer entre intérêts, mais elle suppose "
                   "que les coûts sociaux et environnementaux soient déjà "
                   "internalisés par le prix, ce que les externalités "
                   "contredisent."}],
      aut=[{'n': "Karl Polanyi",
            'i': "L’économie doit être encastrée dans la société et ne peut "
                 "pas être autonome."}],
      faits=[{'f': "Le scandale Volkswagen, lié à la falsification des "
                   "émissions polluantes, met en évidence l’écart entre le "
                   "discours responsable et les pratiques effectives.",
              'p': "Le cas établit que le greenwashing est un risque "
                   "constitutif de la responsabilité sociale volontaire, et "
                   "non un dévoiement marginal."}],
      termes=['responsabilite sociale', 'parties prenantes', 'loi pacte'],
      dos=['n8-rse', 'n8-parties-prenantes']),

   nd('financiarisation', 'La financiarisation de l’entreprise', 'limite',
      "Le cours de l’action devient le critère de gestion : horizon "
      "raccourci, pression sur les coûts, arbitrage entre dividende et "
      "investissement.",
      grp=2, par='gouvernance',
      defi="La financiarisation de l’entreprise désigne la place croissante "
           "prise par les marchés financiers et par les attentes des "
           "actionnaires dans la conduite de la firme. Elle est la "
           "conséquence logique du capitalisme actionnarial : si la "
           "gouvernance a pour objectif de faire augmenter la valeur des "
           "actions, alors le cours de Bourse devient le critère "
           "d’évaluation des décisions de gestion.",
      mec=[("Le raccourcissement de l’horizon",
            "L’évaluation trimestrielle du résultat pousse à privilégier les "
            "décisions dont l’effet est rapidement visible, au détriment "
            "d’investissements dont le rendement est différé."),
           ("L’arbitrage entre distribution et investissement",
            "Le résultat distribué aux actionnaires n’est pas réinvesti : le "
            "même excédent ne peut servir deux fois, ce qui fait du partage "
            "une décision stratégique et non comptable.")],
      args=[{'a': "La discipline actionnariale corrige un défaut réel du "
                  "capitalisme managérial : des dirigeants peu contrôlés "
                  "peuvent poursuivre la taille ou le prestige plutôt que la "
                  "performance.",
             'lim': "Elle remplace un biais par un autre : la pression sur le "
                    "cours peut conduire à sous-investir et à reporter les "
                    "coûts sur les salariés et les fournisseurs."}],
      aut=[{'n': "Nicholas Bloom",
            'i': "Les écarts de revenus sont restés constants au sein des "
                 "entreprises mais ont crû entre les entreprises."}],
      termes=['financiarisation de l entreprise', 'valeur actionnariale',
              'dividende'],
      dos=['n8-financiarisation', 'n8-capitalisme-actionnarial']),

   nd('risque', 'Le profit, le risque et l’incertitude', 'detail',
      "Le profit rémunère la prise de risque dans un monde où l’avenir n’est "
      "pas probabilisable : c’est ce qui distingue l’entrepreneur du gérant.",
      grp=2, par='coeur',
      defi="Le profit est le solde qui revient à l’entreprise après "
           "rémunération de tous les autres facteurs. Sa justification "
           "théorique tient à une distinction : le risque peut être "
           "probabilisé, donc assuré, tandis que l’incertitude ne le peut "
           "pas. L’entrepreneur engage des ressources sur un avenir qu’aucun "
           "calcul ne garantit, et le profit est la contrepartie de cet "
           "engagement.",
      mec=[("Risque et incertitude ne sont pas la même chose",
            "Un risque dont on connaît la loi de probabilité peut être "
            "transféré à un assureur ; une incertitude radicale ne le peut "
            "pas, et c’est elle que l’entrepreneur assume."),
           ("Le profit comme solde, non comme prix",
            "Contrairement au salaire ou à l’intérêt, le profit n’est pas "
            "contractuellement fixé : il est ce qui reste, et peut être "
            "négatif."),
           ("L’entrepreneur distingué du gestionnaire",
            "Réaliser de nouvelles combinaisons productives n’est pas gérer "
            "l’existant : la fonction entrepreneuriale est définie par "
            "l’innovation et la prise de risque, non par la propriété.")],
      aut=[{'n': "Joseph Schumpeter",
            'i': "L’entrepreneur innovateur est celui qui réalise de "
                 "nouvelles combinaisons productives, et non celui qui gère "
                 "l’existant."}],
      termes=['profit', 'risque et incertitude', 'entrepreneur'],
      dos=['n8-profit', 'n8-risque-incertitude', 'n8-entrepreneur']),

   nd('concurrence', 'Taille, pouvoir de marché et régulation', 'detail',
      "La taille n’est pas en soi un problème : ce sont les barrières à "
      "l’entrée qui transforment une position en rente durable.",
      grp=2, par='taille',
      defi="La croissance de la taille pose une question de politique "
           "publique dès lors qu’elle confère un pouvoir de marché, "
           "c’est-à-dire la capacité d’influencer les prix, les quantités, "
           "les conditions de vente ou l’accès des concurrents. Le cours "
           "distingue soigneusement la taille, qui peut résulter d’une "
           "efficacité supérieure, et le pouvoir durable, qui suppose des "
           "obstacles à l’entrée.",
      mec=[("Ce qui rend le pouvoir durable",
            "Sans barrières, le profit attire des entrants qui le font "
            "disparaître : la durée d’une position dominante mesure la "
            "hauteur des obstacles, non la qualité de l’entreprise."),
           ("Le ciblage de la politique de la concurrence",
            "Interdiction des ententes, contrôle des concentrations, "
            "ouverture de l’accès : l’instrument vise les entraves, non la "
            "taille elle-même."),
           ("Le risque pour l’innovation",
            "Certaines grandes entreprises peuvent freiner l’innovation en "
            "empêchant l’entrée de nouveaux concurrents : le coût du pouvoir "
            "de marché n’est pas seulement un prix plus élevé, c’est une "
            "dynamique bloquée.")],
      aut=[{'n': "Philippe Aghion",
            'i': "Certaines grandes entreprises peuvent freiner l’innovation "
                 "en empêchant l’entrée de nouveaux concurrents."}],
      termes=['pouvoir de marche', 'politique de la concurrence',
              'barriere a l entree'],
      dos=['n5-politique-concurrence', 'n5-barrieres',
           'n5-pouvoir-marche']),

   nd('capitalismes', 'Trois capitalismes successifs', 'sortie',
      "Entrepreneurial, managérial, actionnarial : la même entreprise, trois "
      "réponses différentes à la question « qui décide, et pour qui ? ».",
      grp=2, par='direction',
      defi="Le cours organise l’histoire de l’entreprise en trois "
           "configurations successives. Dans le capitalisme entrepreneurial, "
           "la propriété du capital et le pouvoir de décision sont confondus. "
           "Dans le capitalisme managérial, la taille impose une direction "
           "professionnelle distincte des propriétaires. Dans le capitalisme "
           "actionnarial, les actionnaires reprennent le contrôle par des "
           "dispositifs de gouvernance et imposent la valeur actionnariale "
           "comme critère.",
      mec=[("Le passage de l’entrepreneurial au managérial",
            "La croissance de la taille rend la direction impossible à "
            "l’intuition : la compétence de gestion devient un métier, et le "
            "pouvoir se déplace vers ceux qui la possèdent."),
           ("Le retour des actionnaires",
            "La gouvernance d’entreprise, qui s’impose dans les années 1990, "
            "est précisément le dispositif par lequel les propriétaires "
            "reprennent la main sur une direction qui leur avait échappé."),
           ("Ce que chaque configuration laisse ouvert",
            "La première pose la question du risque, la deuxième celle du "
            "contrôle, la troisième celle de la finalité : à chaque étape, "
            "la réponse précédente devient le problème suivant.")],
      args=[{'a': "La séquence fournit un plan historique immédiatement "
                  "utilisable, et chaque configuration correspond à des "
                  "auteurs et à des dispositifs identifiés.",
             'lim': "Elle ne décrit pas une succession universelle : les "
                    "trois formes coexistent aujourd’hui selon les tailles, "
                    "les secteurs et les pays."}],
      termes=['capitalisme entrepreneurial', 'capitalisme managerial',
              'capitalisme actionnarial'],
      dos=['n8-capitalisme-entrepreneurial', 'n8-capitalisme-managerial',
           'n8-capitalisme-actionnarial']),
  ],
  [
   ln('coeur', 'frontieres', 'se décide en',
      "Si la firme existe parce que le marché coûte, alors sa limite est "
      "exactement le point où ce coût devient inférieur à celui de "
      "l’organisation interne. La question d’existence commande la question "
      "de frontière.", 'cause'),
   ln('coeur', 'risque', 'suppose quelqu’un qui engage',
      "Créer une organisation, c’est engager des ressources sur un avenir "
      "incertain. Le profit est la contrepartie de cet engagement, ce qui "
      "distingue l’entrepreneur du gestionnaire de l’existant.", 'cause'),
   ln('frontieres', 'taille', 'détermine la croissance',
      "Internaliser une activité, c’est grandir. La concentration verticale "
      "n’est que la frontière de la firme déplacée vers l’amont ou vers "
      "l’aval : les deux notions décrivent le même arbitrage.", 'cause'),
   ln('taille', 'direction', 'rend nécessaire',
      "Une grande entreprise ne peut plus être dirigée à l’intuition par son "
      "propriétaire : il faut planifier, coordonner des milliers de "
      "salariés, gérer les finances. La séparation propriété / contrôle est "
      "d’abord une conséquence de la taille.", 'cause'),
   ln('direction', 'gouvernance', 'crée le problème que résout',
      "Dès lors que les dirigeants décident sans posséder, les actionnaires "
      "cherchent à s’assurer que les décisions servent leurs intérêts : la "
      "gouvernance est la réponse au problème créé par la séparation.",
      'cause'),
   ln('gouvernance', 'financiarisation', 'débouche sur',
      "Si l’objectif assigné est que la valeur des actions augmente, alors le "
      "cours de Bourse devient le critère d’évaluation des décisions : la "
      "gouvernance actionnariale produit mécaniquement la financiarisation de "
      "la gestion.", 'cause'),
   ln('financiarisation', 'rse', 'suscite en retour',
      "La responsabilité sociale est présentée par le cours comme la réponse "
      "aux limites du capitalisme actionnarial : elle élargit le cercle des "
      "destinataires au moment où la pression financière le resserre.",
      'oppose'),
   ln('rse', 'gouvernance', 'conteste le critère de',
      "Faire du profit le seul critère suppose que les coûts sociaux et "
      "environnementaux soient déjà internalisés par le prix. Les "
      "externalités montrent que ce n’est pas le cas : le critère lui-même "
      "est en débat.", 'oppose'),
   ln('taille', 'concurrence', 'appelle une régulation',
      "La croissance devient un problème public dès qu’elle confère un "
      "pouvoir durable sur les prix et sur l’accès. Rockefeller passe de dix "
      "à quatre-vingt-dix pour cent du raffinage américain : c’est ce qui "
      "provoque les politiques antitrust.", 'cause'),
   ln('concurrence', 'frontieres', 'borne l’internalisation',
      "La politique de la concurrence limite certaines intégrations : la "
      "frontière de la firme n’est donc pas seulement le produit d’un calcul "
      "privé, elle est aussi bornée par la règle publique.", 'limite'),
   ln('direction', 'capitalismes', 's’inscrit dans',
      "La séparation propriété / contrôle est le passage du premier au "
      "deuxième capitalisme : l’histoire de l’entreprise est celle du "
      "déplacement du pouvoir entre propriétaires, managers et actionnaires.",
      'cause'),
   ln('gouvernance', 'capitalismes', 'ouvre le troisième',
      "La gouvernance d’entreprise, imposée dans les années 1990, est le "
      "dispositif par lequel les actionnaires reprennent la main : elle "
      "définit le capitalisme actionnarial.", 'cause'),
   ln('risque', 'direction', 'change de porteur',
      "Dans le capitalisme entrepreneurial, celui qui décide est celui qui "
      "risque son capital. La séparation dissocie les deux : le dirigeant "
      "décide d’un risque qu’il ne supporte pas, ce qui est exactement le "
      "problème d’agence.", 'conditionne'),
   ln('capitalismes', 'coeur', 'laisse la question ouverte',
      "Chaque configuration répond à « qui décide, et pour qui ? » sans "
      "clore la question de ce qu’est une entreprise : la firme reste un "
      "arbitrage entre coordination par l’autorité et coordination par le "
      "prix.", 'renforce'),
   ln('financiarisation', 'taille', 'oriente la croissance',
      "L’évaluation par le cours de l’action privilégie les opérations dont "
      "l’effet est immédiatement lisible : la croissance externe par rachat "
      "en bénéficie plus que la croissance interne, dont le rendement est "
      "différé.", 'cause'),
   ln('concurrence', 'capitalismes', 'conditionne la dynamique',
      "Certaines grandes entreprises peuvent freiner l’innovation en "
      "empêchant l’entrée : le coût du pouvoir de marché n’est pas seulement "
      "un prix plus élevé, c’est la possibilité même de la configuration "
      "suivante.", 'limite'),
  ],
  fam='Innovation, travail et entreprise')
