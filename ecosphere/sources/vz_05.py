# -*- coding: utf-8 -*-
"""Visualisation 5 — Les défaillances du marché (type arbre)."""

from vz_base import v, nd, ln

v('vz-defaillances', 'Les défaillances du marché',
  'Chapitre 5 · de l’efficacité du marché au doute sur l’État',
  'arbre',
  "Le chapitre part d’un résultat fort — le marché concurrentiel conduit à "
  "une allocation efficace — puis recense les cas où ce résultat tombe. "
  "Cette visualisation descend l’arbre niveau par niveau : la promesse "
  "d’efficacité, les quatre familles de défaillances, les remèdes "
  "disponibles, et le retour de la critique contre l’État lui-même.",
  [("Descendre, puis remonter",
    "Niveau 1 : pourquoi le marché est efficace. Niveau 2 : les quatre cas "
    "où il ne l’est plus. Niveau 3 : les remèdes. Niveau 4 : pourquoi le "
    "remède est lui-même imparfait. C’est le plan type d’une dissertation "
    "sur l’intervention publique."),
   ("Identifier la cause, pas le symptôme",
    "Chaque défaillance a une cause précise : absence de prix pour "
    "l’externalité, non-excluabilité pour le bien collectif, entrave à "
    "l’entrée pour le pouvoir de marché, inégale information pour "
    "l’asymétrie. Le remède découle de la cause, jamais du symptôme."),
   ("La conclusion du cours",
    "Il n’existe pas de solution parfaite, seulement des arbitrages. Le "
    "dernier niveau n’annule pas les précédents : il interdit de présenter "
    "l’intervention publique comme la réponse évidente.")],
  [
   # ------------------------------------------------- niveau 1 : la promesse
   nd('marche', 'Le marché concurrentiel est efficace', 'coeur',
      "En concurrence pure et parfaite, les prix coordonnent sans "
      "planificateur et l’équilibre atteint un optimum de Pareto : personne "
      "ne peut gagner sans qu’un autre perde.",
      grp=1,
      defi="Le résultat de référence du chapitre est que, sous les "
           "hypothèses de la concurrence pure et parfaite, le marché conduit "
           "à une allocation efficace des ressources. Les prix transmettent "
           "l’information nécessaire à la décision, l’offre et la demande "
           "s’ajustent sans qu’aucune instance n’ait à connaître l’ensemble "
           "des besoins, et l’équilibre obtenu est un optimum de Pareto : "
           "aucune réallocation ne peut améliorer la situation de l’un sans "
           "dégrader celle d’un autre. Toutes les défaillances se définissent "
           "par rapport à cette référence.",
      mec=[("La coordination par les prix",
            "Le prix résume en un seul nombre la rareté relative d’un bien. "
            "Il n’exige de personne qu’il connaisse les besoins de tous : "
            "chacun décide à partir de son information propre et du signal "
            "qu’il reçoit."),
           ("Les cinq hypothèses de la concurrence pure et parfaite",
            "Atomicité, homogénéité du produit, transparence de "
            "l’information, libre entrée et sortie, libre circulation des "
            "facteurs. Chaque défaillance correspond à la levée de l’une ou "
            "de plusieurs d’entre elles."),
           ("Le surplus maximal à l’équilibre",
            "À l’équilibre concurrentiel, la somme du surplus du "
            "consommateur et du surplus du producteur est maximale : c’est la "
            "traduction graphique de l’efficacité, et la mesure de ce que "
            "coûte chaque défaillance.")],
      aut=[{'n': "Adam Smith",
            'i': "La main invisible fait que la poursuite des intérêts "
                 "particuliers sert l’intérêt général."},
           {'n': "Friedrich Hayek",
            'i': "Le marché est un processus de découverte dans un monde où "
                 "l’information est dispersée et subjective."}],
      termes=['concurrence pure et parfaite', 'optimum de pareto',
              'surplus', 'equilibre de marche'],
      dos=['n5-cpp', 'n5-pareto', 'n5-surplus']),

   # -------------------------------------- niveau 2 : les quatre défaillances
   nd('externalites', 'Les externalités', 'pilier',
      "Un effet sur autrui qui ne passe pas par le prix. Négative : "
      "surproduction et prix trop bas. Positive : sous-production d’un bien "
      "pourtant utile.",
      grp=2,
      defi="Une externalité est l’effet positif ou négatif de l’activité d’un "
           "agent économique sur un autre, sans compensation monétaire : une "
           "répercussion qui ne passe pas par le marché et n’est pas prise en "
           "compte dans le prix. L’externalité négative conduit à une "
           "surproduction et à un prix trop bas, l’externalité positive à une "
           "sous-production d’un bien pourtant socialement utile.",
      mec=[("La divergence entre coût privé et coût social",
            "L’agent ne supporte qu’une partie des conséquences de sa "
            "décision : l’écart entre le coût marginal social et le coût "
            "marginal privé mesure exactement l’externalité, et c’est lui que "
            "la correction doit annuler."),
           ("La surproduction en cas d’externalité négative",
            "Comme l’entreprise ignore le coût qu’elle impose, elle produit "
            "trop et vend trop bon marché : l’équilibre s’établit à un prix "
            "inférieur et une quantité supérieure à l’optimum, d’où une perte "
            "de bien-être."),
           ("La sous-production en cas d’externalité positive",
            "Le producteur ne perçoit pas la valeur du bénéfice qu’il crée "
            "pour les autres : il arrête son activité avant le point "
            "socialement optimal, de sorte que la collectivité est privée "
            "d’un gain gratuit.")],
      faits=[{'f': "L’exemple d’externalité positive donné par le cours est "
                   "la proximité d’une université pour un commerce : il "
                   "existe un gain réel pour la collectivité, mais il est "
                   "gratuit.",
              'p': "L’exemple montre que l’externalité positive est aussi une "
                   "défaillance : la gratuité du bénéfice conduit à "
                   "sous-produire une activité socialement utile."}],
      aut=[{'n': "Arthur Pigou",
            'i': "Il faut corriger les prix pour qu’ils reflètent le vrai "
                 "coût ou le vrai bénéfice pour la société."}],
      termes=['externalite', 'cout social', 'cout prive'],
      dos=['n6-externalites', 'n4-externalites-env']),

   nd('collectifs', 'Biens collectifs et biens communs', 'pilier',
      "Non-excluabilité : le prix ne peut plus jouer son rôle. Le bien "
      "collectif est sous-produit, le bien commun surexploité.",
      grp=2,
      defi="Les biens collectifs purs sont des biens non rivaux et non "
           "excluables : on ne peut empêcher personne de consommer, et la "
           "consommation de l’un ne gêne pas celle des autres. Faute de "
           "pouvoir faire payer, aucun producteur privé ne peut rentabiliser "
           "la production. Les biens communs sont rivaux mais non "
           "excluables : la non-excluabilité y produit l’effet inverse, une "
           "surexploitation. Le cours résume : la non-excluabilité empêche le "
           "système de prix de jouer son rôle.",
      mec=[("L’impossibilité de faire payer",
            "Faute d’excluabilité, l’entreprise ne peut conditionner l’accès "
            "au paiement : le prix cesse de jouer son rôle d’allocation, et "
            "l’activité devient non rentabilisable pour un producteur privé."),
           ("Le comportement de passager clandestin",
            "Chaque agent raisonne en se disant qu’il bénéficiera du bien "
            "même sans payer : la somme de ces calculs rationnels aboutit à "
            "ce que personne ne finance et donc à ce que le bien n’existe "
            "pas."),
           ("La surexploitation du bien commun",
            "Lorsque le bien est rival, la non-excluabilité conduit chacun à "
            "prélever davantage puisque l’abstention ne profite qu’aux "
            "autres : la ressource s’épuise, ce que Hardin appelle la "
            "tragédie des communs.")],
      aut=[{'n': "Mancur Olson",
            'i': "Un passager clandestin est quelqu’un qui consomme un bien "
                 "sans vouloir participer à son financement."},
           {'n': "Garrett Hardin",
            'i': "Une ressource commune non régulée tend à être surexploitée, "
                 "car chacun y gagne à prélever davantage."},
           {'n': "Richard Musgrave",
            'i': "Certains biens sont tutélaires : institutionnellement pris "
                 "en charge par l’État."}],
      faits=[{'f': "Contrairement à l’autoroute à péage, il n’existe aucun "
                   "moyen technique de contrôler qui paie pour la lumière "
                   "d’un phare.",
              'p': "La comparaison isole la variable décisive : ce n’est pas "
                   "l’utilité du bien qui change mais la possibilité "
                   "technique d’exclure."}],
      termes=['bien collectif', 'bien commun', 'passager clandestin',
              'non excluabilite'],
      dos=['n6-biens-collectifs', 'n6-biens-communs',
           'n6-passager-clandestin']),

   nd('pouvoir', 'Le pouvoir de marché', 'pilier',
      "Dès qu’une hypothèse de la concurrence parfaite tombe, l’entreprise "
      "cesse d’être price taker et devient price maker.",
      grp=2,
      defi="Le pouvoir de marché désigne la capacité d’une entreprise à agir "
           "sur le marché, c’est-à-dire à influencer les prix, les quantités, "
           "les conditions de vente ou l’accès des concurrents au marché. En "
           "concurrence parfaite ce pouvoir n’existe pas, l’entreprise étant "
           "price taker ; en concurrence imparfaite, certaines entreprises "
           "deviennent price maker.",
      mec=[("L’acquisition du pouvoir",
            "Dès qu’une hypothèse de la concurrence parfaite tombe, la "
            "demande adressée à l’entreprise cesse d’être parfaitement "
            "élastique : elle peut augmenter son prix sans perdre toute sa "
            "clientèle."),
           ("L’élargissement au-delà du prix",
            "Le pouvoir de marché ne porte pas seulement sur les prix mais "
            "aussi sur les quantités, les conditions de vente et l’accès des "
            "concurrents : il peut donc s’exercer sans hausse de prix "
            "visible."),
           ("La perte de surplus",
            "Le producteur restreint la quantité pour élever le prix : une "
            "partie du surplus du consommateur lui est transférée, et une "
            "autre partie disparaît purement et simplement, faute "
            "d’échanges qui auraient été mutuellement avantageux.")],
      args=[{'a': "Les barrières à l’entrée expliquent la durée du pouvoir de "
                  "marché : sans elles, le profit attirerait des entrants qui "
                  "le feraient disparaître.",
             'lim': "La théorie des marchés contestables objecte que la seule "
                    "menace crédible d’entrée suffit à discipliner un "
                    "monopole, ce qui déplace la cible de la politique de la "
                    "concurrence vers les barrières plutôt que vers la "
                    "taille."}],
      termes=['pouvoir de marche', 'monopole', 'barriere a l entree',
              'oligopole'],
      dos=['n5-pouvoir-marche', 'n5-monopole', 'n5-barrieres']),

   nd('asymetries', 'Les asymétries d’information', 'pilier',
      "Un agent en sait plus que l’autre : l’acheteur applique un prix moyen, "
      "la qualité haute se retire, le marché peut disparaître.",
      grp=2,
      defi="Il y a asymétrie d’information lorsque, dans un échange ou un "
           "contrat, un agent possède plus d’informations que l’autre. "
           "L’échange est alors biaisé et le marché ne fonctionne plus "
           "correctement. Le cours en fait une défaillance identifiée dans "
           "les années 1970, dont l’auteur principal est George Akerlof.",
      mec=[("La réaction défensive de la partie mal informée",
            "Ne pouvant distinguer les bons des mauvais, l’acheteur applique "
            "un traitement moyen : ce prix moyen est trop bas pour la qualité "
            "haute et trop élevé pour la qualité basse."),
           ("L’éviction de la qualité haute",
            "Les détenteurs de biens de bonne qualité refusent un prix moyen "
            "qui les sous-évalue et quittent le marché : la qualité moyenne "
            "baisse, ce qui abaisse encore le prix accepté. La spirale peut "
            "faire disparaître le marché."),
           ("La distinction temporelle",
            "Avant le contrat, l’asymétrie produit une sélection adverse sur "
            "les caractéristiques cachées ; après le contrat, un aléa moral "
            "sur les comportements non observables : deux problèmes distincts "
            "et deux remèdes différents.")],
      aut=[{'n': "George Akerlof",
            'i': "L’asymétrie d’information peut non seulement dégrader un "
                 "marché, mais le faire disparaître entièrement."},
           {'n': "Joseph Stiglitz",
            'i': "L’information imparfaite empêche les marchés d’atteindre "
                 "l’allocation efficace décrite par le modèle concurrentiel."}],
      faits=[{'f': "George Akerlof publie The Market for Lemons en 1970, sur "
                   "le marché des voitures d’occasion.",
              'p': "La date situe l’asymétrie d’information comme une "
                   "défaillance identifiée dans les années 1970, postérieure "
                   "donc aux externalités et aux biens collectifs."}],
      termes=['asymetrie d information', 'selection adverse', 'alea moral'],
      dos=['n6-asymetries', 'n6-selection-adverse', 'n6-alea-moral']),

   # ----------------------------------------------- niveau 3 : les remèdes
   nd('pigou', 'Corriger le prix : taxe et subvention', 'detail',
      "La taxe relève le coût privé jusqu’au coût social, la subvention fait "
      "l’inverse. On ne remplace pas le marché : on répare son signal.",
      grp=3,
      defi="Le remède pigouvien consiste à modifier le prix pour qu’il "
           "intègre l’effet externe. La taxe relève le coût marginal privé "
           "jusqu’au coût social : le prix monte et la quantité baisse "
           "jusqu’au point optimal. La subvention abaisse le coût : le prix "
           "baisse et la quantité augmente. Dans les deux cas, l’État "
           "rétablit le signal-prix sans se substituer au marché, ce qui "
           "distingue cet instrument de la production publique.",
      mec=[("L’internalisation de l’effet externe",
            "Le montant de la taxe est calibré sur l’écart entre coût social "
            "et coût privé : l’agent décide alors en tenant compte de ce "
            "qu’il impose aux autres, sans qu’aucune interdiction soit "
            "prononcée."),
           ("La symétrie du traitement",
            "Pigou ne raisonne pas seulement sur le dommage : une externalité "
            "positive doit être subventionnée, de la même façon qu’une "
            "externalité négative doit être taxée.")],
      opp=[{'t': "La taxe suppose de connaître le montant du dommage, ce "
                 "qu’aucune administration ne sait mesurer exactement.",
            'qui': "objection pratique",
            'rep': "L’objection est réelle et explique l’attrait du marché de "
                   "quotas, qui fixe la quantité et laisse le prix se former. "
                   "Elle ne supprime pas le principe : un signal approximatif "
                   "vaut mieux qu’un prix nul."}],
      aut=[{'n': "Arthur Pigou",
            'i': "Une externalité positive doit être subventionnée, et pas "
                 "seulement une externalité négative taxée."}],
      termes=['taxation', 'subvention', 'pigou', 'internalisation'],
      dos=['n6-taxation', 'n4-taxe-carbone']),

   nd('coase', 'Attribuer des droits de propriété', 'detail',
      "Si les droits sont clairement définis et la négociation peu coûteuse, "
      "les parties trouvent elles-mêmes l’arrangement efficace.",
      grp=3,
      defi="Ronald Coase objecte que l’externalité n’appelle pas "
           "nécessairement l’État : elle traduit l’absence de droits de "
           "propriété bien définis. Si ces droits sont attribués et si la "
           "négociation est peu coûteuse, les parties concernées trouvent "
           "elles-mêmes l’arrangement efficace, quelle que soit la "
           "répartition initiale des droits. Le marché de quotas d’émission "
           "applique cette logique : on fixe les quantités et l’on laisse le "
           "prix se former.",
      mec=[("La définition des droits",
            "Tant que nul ne possède le droit d’émettre ou le droit d’être "
            "préservé, aucune transaction n’est possible. Créer le droit crée "
            "le marché."),
           ("La négociation entre les parties",
            "Celui pour qui l’activité vaut le plus rachète le droit à "
            "l’autre : le résultat est efficace, et seule la répartition des "
            "gains dépend de l’attribution initiale.")],
      opp=[{'t': "La solution par les droits suppose des coûts de transaction "
                 "négligeables, ce qui n’est jamais le cas lorsque les "
                 "parties sont nombreuses et dispersées.",
            'qui': "limite reconnue",
            'rep': "L’objection est décisive pour les pollutions diffuses, où "
                   "les victimes se comptent par millions. Elle explique que "
                   "la solution coasienne soit retenue pour des pollueurs peu "
                   "nombreux et identifiables, comme dans les marchés de "
                   "quotas."}],
      aut=[{'n': "Ronald Coase",
            'i': "Les externalités peuvent être résolues par le marché si des "
                 "droits de propriété clairement définis sont attribués."}],
      termes=['droits de propriete', 'coase', 'cout de transaction',
              'marche de quotas'],
      dos=['n6-couts-transaction', 'n4-quotas']),

   nd('ostrom', 'La gestion collective des communs', 'detail',
      "Entre le marché et l’État, une troisième voie : des communautés "
      "locales qui se dotent de règles, de surveillance et de sanctions "
      "graduées.",
      grp=3,
      defi="Elinor Ostrom montre qu’entre la privatisation et la "
           "nationalisation existe une troisième voie : la gestion collective "
           "par les communautés d’usagers. L’argument est empirique autant "
           "que théorique : de nombreuses ressources communes ont été gérées "
           "durablement par des règles locales, sans propriété privée ni "
           "autorité centrale. La tragédie des communs décrite par Hardin "
           "n’est donc pas une fatalité mais le résultat d’une absence "
           "d’institution.",
      mec=[("Des règles définies par les usagers eux-mêmes",
            "Ceux qui connaissent la ressource fixent les limites de "
            "prélèvement : la règle est mieux informée et mieux acceptée "
            "qu’une norme imposée de l’extérieur."),
           ("La surveillance mutuelle et les sanctions graduées",
            "Le respect de la règle est contrôlé par les usagers, et les "
            "sanctions montent par paliers : le dispositif est peu coûteux et "
            "n’exclut pas d’emblée celui qui s’écarte.")],
      args=[{'a': "La gestion collective évite à la fois les coûts "
                  "d’information de l’État et l’exclusion produite par la "
                  "privatisation d’une ressource dont dépendent des usagers "
                  "nombreux.",
             'lim': "Elle suppose une communauté identifiable et un intérêt "
                    "durable à la ressource : elle se transpose mal aux "
                    "communs globaux comme le climat, dont les usagers sont "
                    "l’humanité entière."}],
      aut=[{'n': "Elinor Ostrom",
            'i': "Une troisième voie existe entre le marché et l’État : la "
                 "gestion collective par des communautés locales."}],
      termes=['gouvernance des communs', 'ostrom', 'tragedie des communs'],
      dos=['n4-gouvernance-communs', 'n4-tragedie']),

   nd('regle', 'Réglementer et informer', 'detail',
      "Normes, interdictions, obligation d’information : la règle garantit le "
      "résultat mais ignore les coûts de chacun.",
      grp=3,
      defi="La réglementation agit sur les quantités ou les comportements "
           "plutôt que sur les prix : normes, interdictions, standards, "
           "obligations juridiques. Pour les asymétries d’information, elle "
           "prend une forme particulièrement économe : rendre l’information "
           "disponible plutôt qu’interdire l’échange. Garanties légales, "
           "étiquetage et obligation d’information rétablissent la symétrie "
           "sans supprimer le marché.",
      mec=[("La garantie du résultat",
            "Une norme fixe directement le niveau admissible : le résultat "
            "environnemental ou sanitaire est obtenu avec certitude, ce que "
            "le prix ne garantit jamais."),
           ("L’uniformité comme coût",
            "La règle ignore que le coût de la mise en conformité diffère "
            "d’un acteur à l’autre : la dépollution n’est donc pas obtenue au "
            "moindre coût collectif, contrairement au signal-prix."),
           ("La réduction de l’asymétrie par l’information",
            "Obliger à informer coûte peu et restaure la capacité de choisir. "
            "Le cours cite la garantie légale de conformité portée à douze "
            "mois comme exemple de protection du consommateur.")],
      opp=[{'t': "La règle est préférable au prix, car elle seule garantit "
                 "que le résultat visé sera bien atteint.",
            'qui': "argument réglementaire",
            'rep': "La garantie est fragile : le cours montre qu’une règle "
                   "isolée à petite échelle est inefficace dès lors que les "
                   "acteurs disposent d’arbitrages spatiaux et logistiques "
                   "pour la contourner."}],
      termes=['reglementation', 'norme', 'protection du consommateur'],
      dos=['n6-reglementation', 'n5-politique-concurrence']),

   # ------------------------------------------- niveau 4 : le retour critique
   nd('etat', 'Les défaillances de l’État', 'debat',
      "L’école des choix publics renverse Pigou : il existe des défaillances "
      "du marché, mais aussi des défaillances de l’État.",
      grp=4,
      defi="Les défaillances de l’État désignent les situations dans "
           "lesquelles l’intervention publique, destinée à corriger une "
           "défaillance de marché, produit elle-même des résultats "
           "inefficaces. L’école des choix publics renverse le raisonnement "
           "de Pigou en appliquant à la décision publique l’individualisme "
           "méthodologique : l’État n’est pas une entité désintéressée mais "
           "une somme d’acteurs rationnels poursuivant chacun leur utilité.",
      mec=[("La maximisation de l’utilité des gouvernants",
            "Pour un politicien, l’utilité est la réélection : ses décisions "
            "s’expliquent donc par le calendrier électoral et non seulement "
            "par l’intérêt général, ce qui rend ses choix prévisibles et "
            "critiquables."),
           ("Le marché politique",
            "Les électeurs sont les demandeurs, les politiciens les offreurs "
            "de politiques publiques, les promesses les biens politiques : "
            "l’analyse économique s’applique intégralement à la décision "
            "publique."),
           ("L’influence des groupes organisés",
            "Les intérêts concentrés sont mieux représentés que les intérêts "
            "diffus : l’État favorise alors des groupes organisés au "
            "détriment de l’intérêt collectif, sans qu’aucun acteur ait agi "
            "de façon irrationnelle.")],
      aut=[{'n': "James Buchanan",
            'i': "L’État n’est pas un être neutre au-dessus de la société : "
                 "il est une somme d’intérêts individuels."},
           {'n': "Gordon Tullock",
            'i': "Les ressources consacrées à obtenir un avantage public sont "
                 "détournées de la production."},
           {'n': "George Stigler",
            'i': "La réglementation peut être capturée par les intérêts "
                 "privés qu’elle est censée encadrer."}],
      faits=[{'f': "Le contexte d’apparition est le retour du libéralisme : "
                   "Thatcher au Royaume-Uni, Reagan aux États-Unis, le succès "
                   "de Milton Friedman et la redécouverte de Hayek.",
              'p': "La contextualisation situe la doctrine dans une séquence "
                   "historique précise et la relie au tournant des politiques "
                   "économiques."},
             {'f': "Le cours donne l’exemple d’une politique "
                   "environnementale soutenue au départ puis abandonnée parce "
                   "qu’elle coûte des voix.",
              'p': "L’exemple relie la défaillance de l’État aux difficultés "
                   "de la transition écologique et à la faible acceptabilité "
                   "politique des mesures."}],
      termes=['defaillances de l etat', 'choix publics', 'public choice'],
      dos=['n6-defaillances-etat', 'n6-choix-publics']),

   nd('capture', 'Capture du régulateur et recherche de rente', 'limite',
      "La règle finit façonnée par ceux qu’elle devait encadrer, et "
      "l’entreprise investit dans l’influence plutôt que dans la production.",
      grp=4,
      defi="La capture du régulateur désigne la situation dans laquelle la "
           "réglementation est façonnée par les intérêts qu’elle était censée "
           "encadrer. La recherche de rente en est le pendant du côté de "
           "l’entreprise : sachant que l’État distribue des aides, elle "
           "consacre des ressources non pas à produire ou à innover mais à "
           "obtenir l’aide. Aucun acteur n’agit illégalement : le mécanisme "
           "résulte de la rationalité ordinaire des parties.",
      mec=[("L’asymétrie entre intérêts concentrés et diffus",
            "Un petit groupe ayant beaucoup à gagner s’organise aisément ; un "
            "grand nombre d’agents ayant peu à perdre chacun ne s’organise "
            "pas : la représentation des intérêts est structurellement "
            "déséquilibrée."),
           ("L’avantage informationnel du régulé",
            "Les entreprises du secteur connaissent mieux que le régulateur "
            "leurs coûts et leurs contraintes : l’administration dépend de "
            "l’information qu’elles lui fournissent, ce qui oriente la règle "
            "produite."),
           ("L’arbitrage entre produire et obtenir",
            "L’entreprise compare le rendement d’un euro investi dans la "
            "production et d’un euro investi dans l’influence. Les moyens "
            "consacrés au lobbying ne produisent rien : contrairement au "
            "transfert, qui change seulement de mains, ces dépenses sont une "
            "perte nette.")],
      faits=[{'f': "Le cours formule la chaîne : aides publiques importantes, "
                   "lobbying en hausse, ressources consacrées à obtenir la "
                   "protection en hausse, efficacité économique en baisse.",
              'p': "La chaîne montre que le coût principal n’est pas le "
                   "transfert mais la dépense engagée pour l’obtenir."}],
      aut=[{'n': "Mancur Olson",
            'i': "Les intérêts concentrés s’organisent plus facilement que "
                 "les intérêts diffus."},
           {'n': "Philippe Aghion",
            'i': "Certaines grandes entreprises peuvent freiner l’innovation "
                 "en empêchant l’entrée de nouveaux concurrents."}],
      termes=['capture du regulateur', 'recherche de rente', 'lobbying'],
      dos=['n6-capture', 'n6-rente']),

   nd('arbitrage', 'Pas de solution parfaite, des arbitrages', 'sortie',
      "Chaque remède a son défaut propre : mesure du dommage, coûts de "
      "transaction, effet de seuil, capture. On arbitre entre imperfections.",
      grp=4,
      defi="La conclusion du chapitre est explicite : il n’existe pas de "
           "solution parfaite, seulement des arbitrages, puisqu’il existe "
           "aussi des défaillances de l’État, du lobbying, des effets pervers "
           "et des problèmes d’acceptabilité politique. Chaque remède porte "
           "son défaut propre — mesure du dommage pour la taxe, coûts de "
           "transaction pour les droits de propriété, effet de seuil et "
           "contournement pour la norme — de sorte que le choix ne se fait "
           "jamais entre une solution et un échec, mais entre deux "
           "imperfections.",
      mec=[("Comparer des imperfections, non un idéal",
            "La bonne comparaison n’oppose pas l’intervention à un marché "
            "parfait, ni le marché à un État omniscient : elle met face à "
            "face deux dispositifs réels avec leurs coûts respectifs."),
           ("Choisir l’instrument selon la défaillance",
            "La cause détermine le remède : correction du prix pour "
            "l’externalité, financement obligatoire pour le bien collectif, "
            "ouverture à l’entrée pour le pouvoir de marché, obligation "
            "d’information pour l’asymétrie."),
           ("Tenir compte de l’acceptabilité",
            "Un instrument efficace mais rejeté ne produit rien. "
            "L’acceptabilité politique est une contrainte d’efficacité, et "
            "non une considération extérieure à l’analyse.")],
      args=[{'a': "Reconnaître les défaillances de l’État ne conduit pas à "
                  "l’abstention : cela conduit à choisir l’instrument le "
                  "moins exposé à la capture et au moindre coût "
                  "d’information.",
             'lim': "Ce critère ne départage pas toujours : pour les "
                    "pollutions diffuses, ni la négociation coasienne ni la "
                    "gestion collective ne s’appliquent, et il reste à "
                    "arbitrer entre un prix imprécis et une norme rigide."}],
      termes=['defaillance de marche', 'intervention publique', 'arbitrage'],
      dos=['n6-defaillances-etat', 'n6-reglementation']),
  ],
  [
   ln('marche', 'externalites', 'tombe si le prix ignore un effet',
      "L’efficacité suppose que le prix résume tous les effets de la "
      "décision. Dès qu’une conséquence échappe au prix, le signal devient "
      "faux et l’équilibre cesse d’être optimal : la quantité produite "
      "s’écarte de l’optimum social.", 'limite'),
   ln('marche', 'collectifs', 'tombe si l’on ne peut exclure',
      "Le prix ne peut allouer que ce dont on peut refuser l’accès. La "
      "non-excluabilité supprime la possibilité même de faire payer : le "
      "marché ne produit pas le bien, ou laisse épuiser la ressource.",
      'limite'),
   ln('marche', 'pouvoir', 'tombe si l’entrée n’est pas libre',
      "L’atomicité et la libre entrée sont deux des cinq hypothèses de la "
      "concurrence pure et parfaite. Lorsqu’elles tombent, l’entreprise "
      "devient price maker et restreint la quantité pour élever le prix.",
      'limite'),
   ln('marche', 'asymetries', 'tombe si l’information est inégale',
      "La transparence de l’information est une hypothèse, pas un fait. "
      "Lorsqu’un agent en sait plus que l’autre, l’échange se conclut sur des "
      "bases différentes selon la partie, et la qualité haute finit par "
      "quitter le marché.", 'limite'),
   ln('externalites', 'pigou', 'se corrige par le prix',
      "Puisque la cause est l’absence de prix pour l’effet externe, le remède "
      "consiste à en créer un : la taxe relève le coût privé jusqu’au coût "
      "social, la subvention fait l’inverse pour les externalités positives.",
      'cause'),
   ln('externalites', 'coase', 'peut aussi se résoudre par le droit',
      "Coase déplace le diagnostic : l’externalité ne traduit pas une "
      "défaillance du marché mais l’absence de droits de propriété. Définir "
      "ces droits suffit, si la négociation est peu coûteuse, à obtenir "
      "l’arrangement efficace.", 'oppose'),
   ln('collectifs', 'ostrom', 'trouve une troisième voie',
      "Entre la privatisation et la nationalisation, Ostrom documente des "
      "communautés qui gèrent durablement une ressource commune par des "
      "règles locales, une surveillance mutuelle et des sanctions graduées.",
      'cause'),
   ln('collectifs', 'regle', 'appelle un financement obligatoire',
      "Puisque le passager clandestin rend le financement volontaire "
      "impossible, l’État rend la contribution obligatoire : l’impôt supprime "
      "la possibilité de se dérober, et la production peut être publique ou "
      "confiée par commande publique.", 'cause'),
   ln('pouvoir', 'regle', 'appelle la politique de la concurrence',
      "Le remède ne porte pas sur la taille mais sur les entraves : "
      "interdiction des ententes, contrôle des concentrations, ouverture de "
      "l’accès. C’est l’entrée, et non le profit, qui discipline le pouvoir "
      "de marché.", 'cause'),
   ln('asymetries', 'regle', 'se réduit par l’information',
      "La réponse publique à l’asymétrie est souvent peu coûteuse et consiste "
      "à rendre l’information disponible plutôt qu’à interdire l’échange : "
      "garanties légales, étiquetage, obligation d’information.", 'cause'),
   ln('pigou', 'etat', 'suppose un État bien informé',
      "La taxe optimale suppose de connaître le dommage, et l’État de "
      "vouloir le corriger. L’école des choix publics conteste les deux "
      "prémisses : l’administration n’a ni l’information ni l’indépendance "
      "qu’on lui prête.", 'limite'),
   ln('regle', 'capture', 'est exposée à la capture',
      "La règle capturée prend souvent la forme d’obstacles à l’entrée — "
      "licences, diplômes obligatoires, normes exigeantes — qui protègent les "
      "acteurs installés sous couvert d’intérêt général.", 'limite'),
   ln('etat', 'capture', 'se manifeste par',
      "La capture et la recherche de rente sont les deux formes concrètes que "
      "prend la défaillance de l’État : la première du côté de la règle "
      "produite, la seconde du côté des ressources que l’entreprise détourne "
      "de la production.", 'cause'),
   ln('capture', 'arbitrage', 'impose de comparer les imperfections',
      "Puisque l’intervention a ses défauts propres, la bonne comparaison "
      "n’oppose pas l’État à un marché parfait : elle met face à face deux "
      "dispositifs réels, avec leurs coûts d’information et leur exposition "
      "aux intérêts organisés.", 'cause'),
   ln('coase', 'arbitrage', 'bute sur les coûts de transaction',
      "La solution par les droits suppose des coûts de transaction "
      "négligeables : elle s’applique à des pollueurs peu nombreux et "
      "identifiables, non aux pollutions diffuses dont les victimes se "
      "comptent par millions.", 'limite'),
   ln('ostrom', 'arbitrage', 'ne se transpose pas au global',
      "La gestion collective suppose une communauté identifiable et un "
      "intérêt durable à la ressource. Elle se transpose mal aux communs "
      "globaux comme le climat, dont les usagers sont l’humanité entière : "
      "l’arbitrage reste ouvert.", 'limite'),
  ],
  bandes=[(1, 'Le point de départ'), (2, 'Les quatre défaillances'),
          (3, 'Les remèdes'), (4, 'Le retour critique')],
  fam='Marché, État et théories')
