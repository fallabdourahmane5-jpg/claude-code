# -*- coding: utf-8 -*-
"""Ensemble 26 — Grands débats entre approches économiques et sociologiques (1/5)."""

from doss_base import d

d('n26-marche-etat', 26, "Marché et État",
  "Deux modes de coordination, et la question de savoir lequel corrige l’autre",
  "Le débat porte sur le mode de coordination des décisions économiques : le "
  "marché, qui coordonne par les prix, ou l’État, qui coordonne par la "
  "décision publique. Le cours ne le traite pas comme un choix de camp mais "
  "comme une succession d’arguments : autorégulation par les prix chez Smith "
  "et Walras, défaillances de marché justifiant l’intervention chez Pigou, "
  "défaillances de l’État en retour chez les théoriciens des choix publics.",
  "Le cours construit le débat en quatre temps. Premier temps, l’argument de "
  "la coordination marchande. Chez Adam Smith, la conduite des marchés est "
  "naturellement harmonieuse parce que la concurrence se trouve au cœur du "
  "fonctionnement de l’économie : les individus sont égoïstes par nature, "
  "mais cet égoïsme est tempéré par les mécanismes du marché, les prix "
  "s’ajustant en permanence selon le rapport entre l’offre et la demande. "
  "C’est la main invisible. Walras formalise : tous les marchés — biens, "
  "travail, capital — sont interdépendants et l’économie peut atteindre un "
  "équilibre général où tous s’équilibrent simultanément, le mécanisme du "
  "commissaire-priseur ajustant les prix jusqu’à égalité de l’offre et de la "
  "demande. Deuxième temps, les défaillances de marché. Le cours en dresse "
  "la liste : les biens collectifs purs, non rivaux et non excluables, qui "
  "sont sous-produits puisqu’il est impossible de faire payer les "
  "utilisateurs ; les biens communs, rivaux et non excluables, surexploités "
  "selon la tragédie décrite par Hardin ; les externalités, qui justifient "
  "selon Pigou une taxe sur le pollueur ; les asymétries d’information, "
  "qu’Akerlof montre capables de faire disparaître un marché ; le pouvoir de "
  "marché du monopole. Lorsqu’un bien ne permet pas de faire payer "
  "correctement, ou lorsque l’usage individuel nuit à l’intérêt collectif, "
  "le marché n’aboutit pas à une allocation efficace. Troisième temps, les "
  "défaillances de l’État. L’école des choix publics répond à Pigou que "
  "l’État lui-même est imparfait et biaisé : qui décide qu’un bien doit "
  "devenir public, et pourquoi l’État plutôt que la population ? Elle "
  "reproche à la taxe pigouvienne de réduire la compétitivité, de pénaliser "
  "les ménages et de reposer sur une décision arbitraire, et demande un "
  "débat démocratique plutôt qu’une décision administrative. Elle ajoute le "
  "mécanisme de la recherche de rente, qui transforme les entreprises en "
  "chercheurs d’avantages publics. Quatrième temps, la complémentarité. Le "
  "cours montre que la nature d’un bien est parfois une décision politique — "
  "l’exemple des vaccins, techniquement privés mais rendus collectifs ou "
  "communs pour des raisons d’intérêt général — et que la fonction de l’État "
  "est alors de protéger le bien commun, d’éviter la surexploitation et de "
  "garantir l’intérêt collectif. La frontière entre marché et État n’est "
  "donc pas donnée par la technique : elle est en partie construite.",
  [("Les prix coordonnent sans coordinateur",
    "Chez Smith, les prix s’ajustent en permanence selon le rapport entre "
    "l’offre et la demande : les marchés sont flexibles et l’égoïsme "
    "individuel est tempéré par la concurrence, sans qu’aucune autorité "
    "n’ait à connaître l’ensemble du système."),
   ("La coordination peut être générale",
    "Walras démontre que tous les marchés sont interdépendants et qu’un "
    "équilibre général simultané existe : autant d’équations que "
    "d’inconnues, donc une solution. L’économie apparaît fondamentalement "
    "stable et autorégulée."),
   ("Certains biens échappent au prix",
    "Les biens collectifs purs sont non rivaux et non excluables : la "
    "non-excluabilité rend impossible de faire payer les utilisateurs, donc "
    "la production privée est non rentable et le bien est sous-produit. Le "
    "prix cesse de transmettre l’information."),
   ("L’usage individuel peut détruire la ressource",
    "Pour un bien commun, rival et non excluable, chacun raisonne ainsi : "
    "si j’utilise plus la ressource j’y gagne directement, et le coût de la "
    "dégradation est partagé par tous. Le gain est individuel, la perte "
    "collective, et la ressource s’épuise."),
   ("L’intervention publique répare, en principe",
    "Pigou en tire la règle : en cas de défaillance de marché, "
    "l’intervention de l’État est justifiée, par la taxe sur le pollueur, "
    "la production publique du bien collectif ou la réglementation qui "
    "empêche la privatisation totale des ressources communes."),
   ("Mais l’État est lui aussi un acteur intéressé",
    "L’école des choix publics objecte que l’État est imparfait et biaisé : "
    "la décision de rendre un bien public peut servir certains intérêts "
    "industriels, et la taxe repose sur une décision arbitraire. Les "
    "défaillances de l’État s’ajoutent à celles du marché."),
   ("La frontière devient un choix politique",
    "Le cours montre qu’un bien peut être techniquement privé mais rendu "
    "collectif ou commun pour des raisons d’intérêt général. Le partage "
    "entre marché et État n’est donc pas déduit des propriétés du bien, il "
    "est décidé, ce qui appelle un débat démocratique.")],
  [{'a': "Le marché est le mode de coordination le plus économe en "
         "information : il n’exige d’aucun agent une vision globale du "
         "système, puisque les prix transmettent l’information "
         "nécessaire, argument que le cours attribue à l’école "
         "autrichienne, pour laquelle l’information est dispersée, "
         "fragmentée et subjective.",
    'cond': "Il faut que les prix soient libres de s’ajuster et que les "
            "effets des décisions soient entièrement portés par leur "
            "auteur, c’est-à-dire qu’il n’y ait ni externalité ni bien "
            "collectif ni asymétrie d’information majeure.",
    'lim': "Ces conditions sont précisément celles que le chapitre sur les "
           "défaillances du marché montre régulièrement absentes : "
           "externalités, non-excluabilité, asymétries d’information et "
           "pouvoir de marché constituent la règle plus que l’exception "
           "dans les secteurs étudiés."},
   {'a': "L’intervention publique est indispensable là où le prix ne peut "
         "pas se former : un bien non excluable ne permet pas de faire "
         "payer les utilisateurs, donc sa production privée n’est pas "
         "rentable et il est sous-produit, quelle que soit son utilité "
         "sociale.",
    'cond': "L’argument suppose que l’État puisse identifier correctement "
            "le niveau souhaitable de production et le financer par "
            "prélèvement, donc qu’il dispose de l’information et de la "
            "légitimité nécessaires.",
    'lim': "L’école des choix publics conteste exactement ces deux "
           "capacités : l’État est imparfait et biaisé, et la décision de "
           "produire publiquement peut servir des intérêts particuliers. La "
           "défaillance de marché ne démontre donc pas l’efficacité de "
           "l’intervention."},
   {'a': "Marché et État ne sont pas substituables mais imbriqués : le "
         "cours montre que l’État finance souvent les innovations, que les "
         "institutions — règles et lois — conditionnent la croissance, et "
         "que le capital institutionnel figure parmi les capitaux dont "
         "dépend l’activité économique.",
    'cond': "Cette lecture exige de considérer le cadre juridique comme un "
            "facteur de production et non comme une contrainte externe, ce "
            "que la nouvelle économie institutionnelle justifie en "
            "expliquant les différences durables de développement par les "
            "institutions.",
    'lim': "Elle rend le débat moins tranchant mais aussi moins "
           "opérationnel : dire que tout marché suppose des règles ne dit "
           "pas lesquelles, ni jusqu’où l’État doit aller dans la "
           "production directe."},
   {'a': "La frontière entre marché et État relève en partie de la "
         "décision politique, et le cours le démontre par un cas : les "
         "vaccins, produits par des firmes privées et protégés par des "
         "brevets, peuvent être traités comme biens communs pour des "
         "raisons d’intérêt général.",
    'cond': "Il faut accepter que le statut d’un bien ne découle pas "
            "seulement de ses propriétés techniques de rivalité et "
            "d’excluabilité, mais aussi d’un choix collectif explicite.",
    'lim': "Reconnaître ce caractère politique ouvre la critique des choix "
           "publics : si le statut est décidé, il peut l’être au bénéfice "
           "de certains, ce qui est précisément l’objection adressée aux "
           "décisions administratives plutôt que démocratiques."}],
  [{'t': "Le marché s’autorégule et l’État est au mieux inutile, au pire "
         "nocif : les marchés sont efficaces, les agents parfaitement "
         "rationnels, la monnaie neutre, et toute intervention est "
         "anticipée puis neutralisée par les agents.",
    'qui': "La Nouvelle Économie Classique, dont le cours résume ainsi la "
           "position, en l’opposant terme à terme aux keynésiens.",
    'rep': "Le cours relève que la NEC est rapidement critiquée : "
           "hypothèses jugées irréalistes, agents trop rationnels, "
           "incapacité à expliquer les crises majeures. Ces critiques "
           "ouvrent la voie à la Nouvelle Économie Keynésienne, pour "
           "laquelle les marchés réels sont imparfaits et l’intervention "
           "peut améliorer leur fonctionnement."},
   {'t': "L’État doit intervenir parce que le marché est instable : "
         "l’emploi dépend de la demande globale et non du seul marché du "
         "travail, et l’État peut créer une demande autonome pour relancer "
         "l’activité.",
    'qui': "Keynes, dont le cours détaille l’équilibre de sous-emploi et le "
           "chômage involontaire.",
    'rep': "La thèse est puissante mais le cours en signale la limite "
           "symétrique : la Nouvelle Économie Classique objecte qu’il "
           "n’existe pas d’illusion monétaire durable et que les erreurs "
           "sont rapidement corrigées, de sorte que la relance peut être "
           "neutralisée par les anticipations."},
   {'t': "Ni le marché ni l’État ne suffisent : ce qui fait la différence "
         "est la qualité des institutions, inclusives ou extractives, qui "
         "favorisent ou freinent innovation, investissement, mobilité "
         "sociale et entrepreneuriat.",
    'qui': "Acemoglu et Robinson, dont le cours applique la grille à la "
           "précocité anglaise.",
    'rep': "Cette réponse déplace utilement le débat, mais elle ne le clôt "
           "pas : qualifier une institution d’inclusive suppose déjà un "
           "critère de ce qui est souhaitable, et la nouvelle économie "
           "institutionnelle de North explique les différences durables de "
           "développement sans fournir de règle de partage entre production "
           "publique et production privée."}],
  [{'n': "Adam Smith",
    'i': "La conduite des marchés est naturellement harmonieuse parce que "
         "la concurrence se trouve au cœur du fonctionnement de l’économie.",
    'p': "Le cours précise le mécanisme : les individus sont égoïstes par "
         "nature, mais cet égoïsme est tempéré par les mécanismes du "
         "marché, les prix s’ajustant en permanence car ils dépendent du "
         "rapport entre l’offre et la demande. C’est la main invisible, qui "
         "fait aussi du libre-échange une source d’enrichissement des "
         "nations."},
   {'n': "Léon Walras",
    'i': "Tous les marchés sont interdépendants et l’économie peut "
         "atteindre un équilibre général simultané.",
    'p': "Dans Éléments d’économie politique pure (1874), il utilise des "
         "équations mathématiques et le mécanisme du commissaire-priseur, "
         "qui ajuste les prix jusqu’à égalité entre offre et demande. Le "
         "cours souligne la spécificité de l’école de Lausanne : approche "
         "très abstraite, forte confiance dans l’équilibre, peu d’intérêt "
         "pour l’histoire ou les institutions."},
   {'n': "Arthur Pigou",
    'i': "En cas de défaillance de marché, l’intervention de l’État est "
         "justifiée.",
    'p': "Le cours en donne l’instrument : taxer le pollueur, c’est-à-dire "
         "la taxe pigouvienne, afin de faire porter à l’agent le coût "
         "social de son activité. Cette position constitue dans le cours la "
         "référence que l’école des choix publics prend explicitement pour "
         "cible, en lui opposant l’imperfection de l’État lui-même."},
   {'n': "James Buchanan",
    'i': "L’État est lui aussi imparfait et biaisé : aux défaillances du "
         "marché répondent des défaillances de l’État.",
    'p': "Le cours présente l’école des choix publics, dont il est la "
         "figure centrale avec Tullock, comme posant trois questions : qui "
         "décide qu’un bien doit devenir public, pourquoi l’État plutôt que "
         "la population, et à quels intérêts la décision profite-t-elle. "
         "Elle réclame un débat démocratique plutôt qu’une décision "
         "administrative et met en avant la recherche de rente."},
   {'n': "Garrett Hardin",
    'i': "L’intérêt individuel ne conduit pas spontanément à l’intérêt "
         "général : sur un bien commun, il le détruit.",
    'p': "Dans The Tragedy of the Commons (1968), il montre qu’un bien "
         "rival et non excluable est surexploité parce que le gain est "
         "individuel et la perte collective. Le cours souligne qu’il casse "
         "l’idée selon laquelle l’intérêt individuel conduirait "
         "spontanément à la prospérité de tous : ici c’est l’inverse."}],
  [{'f': "Walras démontre l’existence d’un équilibre général par une "
         "analogie mathématique : une économie est un système d’équations "
         "comportant autant d’équations que d’inconnues — tous les prix et "
         "toutes les quantités — donc il existe une solution.",
    'p': "L’autorégulation du marché n’est pas une opinion mais un résultat "
         "formel ; mais le cours signale aussitôt le point faible : rien ne "
         "garantit que les courbes d’offre et de demande se coupent "
         "effectivement."},
   {'f': "Le cours cite le cas des vaccins pendant le Covid pour poser la "
         "question : bien privé ou bien public ? Il note qu’il s’agit d’une "
         "décision politique pouvant servir certains intérêts industriels.",
    'p': "Le partage entre marché et État n’est pas déduit de la nature des "
         "biens : il est construit par une décision, ce qui explique que le "
         "débat soit à la fois économique et politique."},
   {'f': "Akerlof montre dans The Market for Lemons (1970) que l’asymétrie "
         "d’information peut faire disparaître un marché, par sélection "
         "adverse avant le contrat et aléa moral après.",
    'p': "La défaillance n’est pas une imperfection marginale : elle peut "
         "annuler l’existence même de l’échange, ce qui constitue "
         "l’argument le plus fort en faveur d’un encadrement public de "
         "l’information."},
   {'f': "Le cours rappelle que l’école des choix publics reproche à la "
         "taxe pigouvienne de réduire la compétitivité, de pénaliser les "
         "ménages et de reposer sur une décision arbitraire de l’État.",
    'p': "La critique porte sur les trois dimensions que doit satisfaire "
         "une intervention — efficacité, équité, légitimité — et montre "
         "qu’établir une défaillance de marché ne suffit pas à justifier un "
         "instrument précis."}],
  [{'q': "Le marché peut-il se passer de l’État ?",
    'f': "Il faut distinguer trois niveaux. Sur le plan théorique, la "
         "réponse affirmative est démontrée : chez Smith les prix "
         "coordonnent par la concurrence, chez Walras l’équilibre général "
         "existe formellement. Sur le plan des conditions, cette "
         "démonstration suppose l’absence d’externalités, de biens "
         "collectifs et d’asymétries d’information — or le chapitre sur les "
         "défaillances du marché établit que ces situations sont fréquentes "
         "et peuvent même faire disparaître un marché. Sur le plan "
         "institutionnel enfin, le marché suppose des règles et des lois, "
         "ce que la nouvelle économie institutionnelle fait du capital "
         "institutionnel un facteur de croissance.",
    'r': "Ce plan est rigoureux parce qu’il ne confond pas les trois "
         "questions — le marché peut-il coordonner, le fait-il bien, "
         "pourrait-il exister sans cadre — et parce qu’il mobilise à chaque "
         "niveau un auteur précis du cours.",
    'ex': "Le bien collectif pur, dont la non-excluabilité interdit de "
          "faire payer les utilisateurs et donc la production privée."},
   {'q': "Les défaillances du marché justifient-elles l’intervention "
         "publique ?",
    'f': "Elles la rendent nécessaire en principe mais non suffisante en "
         "pratique. Pigou tire de la défaillance la règle d’intervention et "
         "l’instrument : taxer le pollueur. L’école des choix publics "
         "répond que l’État est lui-même imparfait et biaisé, que la taxe "
         "réduit la compétitivité, pénalise les ménages et repose sur une "
         "décision arbitraire, et que la définition même du bien public "
         "peut servir des intérêts particuliers. Le raisonnement correct "
         "consiste donc à comparer deux imperfections, et non à déduire la "
         "perfection de l’une de l’imperfection de l’autre.",
    'r': "C’est la structure argumentative que le cours met explicitement "
         "en place, en présentant les choix publics comme une « critique "
         "des solutions de Pigou » et en parlant de défaillances de l’État "
         "symétriques de celles du marché.",
    'ex': "La question posée par le cours : qui décide qu’un bien doit "
          "devenir public, et pourquoi l’État plutôt que la population ?"},
   {'q': "La frontière entre sphère marchande et sphère publique est-elle "
         "déterminée par la nature des biens ?",
    'f': "Non, et le cours le montre en deux mouvements. D’abord il "
         "construit une typologie technique fondée sur la rivalité et "
         "l’excluabilité, qui classe les biens privés, collectifs purs, de "
         "club et communs. Ensuite il relativise cette typologie : la "
         "nature d’un bien est parfois une décision politique, un bien "
         "pouvant être techniquement privé mais rendu collectif ou commun "
         "pour des raisons d’intérêt général. La frontière relève donc "
         "d’une délibération, ce qui explique que les mêmes propriétés "
         "techniques puissent donner lieu à des choix opposés selon les "
         "pays et les époques.",
    'r': "Le raisonnement tient parce qu’il articule la typologie et sa "
         "limite, toutes deux fournies par le cours, et parce qu’il aboutit "
         "à une conclusion vérifiable : si le statut est décidé, il peut "
         "être contesté démocratiquement.",
    'ex': "Les vaccins, produits par des firmes privées et protégés par des "
          "brevets, traités comme un enjeu d’intérêt général."}],
  comp={'titre': "Marché et État : deux modes de coordination",
        'a': "Coordination par le marché", 'b': "Coordination par l’État",
        'lignes': [
            ("Signal", "Le prix, qui s’ajuste selon l’offre et la demande",
             "La décision publique : règle, taxe, production directe"),
            ("Information requise",
             "Dispersée : aucun agent n’a besoin d’une vision globale",
             "Centralisée : il faut connaître le niveau souhaitable"),
            ("Auteur de référence", "Smith, Walras, école autrichienne",
             "Pigou, Keynes, nouvelle économie institutionnelle"),
            ("Condition de réussite",
             "Ni externalité, ni bien collectif, ni asymétrie d’information",
             "Un État informé, légitime et non capturé"),
            ("Défaillance typique",
             "Sous-production du bien collectif, surexploitation du commun",
             "Décision arbitraire, recherche de rente, capture par un "
             "groupe"),
            ("Critique adressée",
             "Les conditions d’efficacité sont rarement réunies",
             "L’État est lui aussi imparfait et biaisé"),
            ("Traitement de l’innovation",
             "L’initiative privée et la concurrence la suscitent",
             "L’État finance souvent les innovations"),
            ("Statut d’un bien",
             "Déduit de la rivalité et de l’excluabilité",
             "En partie décidé pour des raisons d’intérêt général"),
            ("Place du conflit",
             "Absorbé par l’ajustement des prix",
             "Traité par la délibération, d’où l’appel au débat "
             "démocratique")]},
  voisins=['n26-liberte-intervention', 'n26-autoregulation-instabilite',
           'n26-interets-individuels-collectif', 'n27-institutions',
           'n27-regulation'])

d('n26-liberte-intervention', 26, "Liberté et intervention",
  "Jusqu’où l’initiative privée, à partir d’où la contrainte publique",
  "Le débat porte sur l’étendue légitime de la liberté économique des "
  "agents et sur le point à partir duquel l’intervention publique devient "
  "nécessaire. Le cours le construit historiquement, du mercantilisme "
  "interventionniste de Colbert au libéralisme des physiocrates et de "
  "Smith, puis de l’État keynésien stabilisateur à la Nouvelle Économie "
  "Classique qui juge toute intervention neutralisée, avant le retour "
  "contemporain des politiques industrielles.",
  "Le cours part d’une opposition historique précise. Dans la doctrine "
  "mercantiliste, l’État doit intervenir : Colbert fait de la main visible "
  "du monarque le substitut d’une initiative privée défaillante, crée des "
  "manufactures en vue de l’exportation, supprime les droits de douane "
  "entre les villes du pays et mène à l’extérieur un protectionnisme "
  "sélectif en choisissant les produits qui entrent, avec pour objectif "
  "d’exporter au maximum et d’attirer les capitaux. Les physiocrates s’y "
  "opposent et défendent une politique économique libérale structurée, dont "
  "le cours dit qu’elle influencera les classiques et plus tard Smith "
  "lui-même. Chez Smith, la liberté n’est pas l’absence de régulation mais "
  "une régulation d’un autre type : les individus sont égoïstes par nature, "
  "et c’est la concurrence qui tempère cet égoïsme, les prix s’ajustant en "
  "permanence. Keynes opère le renversement : face à l’instabilité du "
  "marché, l’État doit intervenir, par la politique budgétaire — dépenses "
  "publiques, déficit —, la politique de relance, le soutien à "
  "l’investissement et la stabilisation de l’économie ; il peut créer une "
  "demande autonome pour relancer l’activité. Le cours insiste sur le fait "
  "que Keynes ne rejette pas le marché : il raisonne dans une économie de "
  "marché non planifiée et critique son fonctionnement spontané. La "
  "Nouvelle Économie Classique conteste ensuite l’efficacité même de "
  "l’intervention : les agents forment des anticipations cohérentes, il "
  "n’existe pas d’illusion monétaire durable, les erreurs sont rapidement "
  "corrigées, la monnaie est neutre même à court terme, et toute "
  "intervention est anticipée puis neutralisée — si l’État relance la "
  "demande, les agents anticipent l’inflation future et ajustent leurs "
  "comportements. La Nouvelle Économie Keynésienne rouvre l’espace de "
  "l’intervention sans abandonner les microfondements : en raison des "
  "rigidités de prix et de salaires, des asymétries d’information et de la "
  "concurrence imparfaite, l’économie peut rester durablement en "
  "sous-emploi, et l’intervention de l’État peut améliorer le "
  "fonctionnement du marché plutôt que le perturber systématiquement. Le "
  "cours ajoute enfin un argument contemporain : la politique industrielle "
  "cherche à soutenir certains secteurs, favoriser l’innovation, renforcer "
  "la souveraineté et développer des activités stratégiques, mais elle peut "
  "aussi modifier la concurrence internationale et nourrir la recherche de "
  "rente.",
  [("La liberté des échanges est d’abord conquise contre l’État",
    "Le cours rappelle que les physiocrates s’opposent à l’interventionnisme "
    "mercantiliste et défendent une politique économique libérale "
    "structurée, influençant les classiques puis Smith. La liberté "
    "économique est donc une position historiquement construite."),
   ("Le marché libre est présenté comme autorégulé",
    "Chez Smith, les prix s’ajustent en permanence car ils dépendent du "
    "rapport entre l’offre et la demande. L’égoïsme est tempéré par la "
    "concurrence, de sorte que la liberté ne débouche pas sur le désordre "
    "mais sur une harmonie."),
   ("L’instabilité observée rouvre la question de l’intervention",
    "Chez Keynes, la demande globale peut être insuffisante, la production "
    "faible et le chômage involontaire. L’emploi dépend de la demande "
    "globale et non du seul marché du travail, ce qui déplace la "
    "responsabilité vers un acteur capable d’agir sur l’ensemble."),
   ("L’État peut créer une demande autonome",
    "Les moyens sont énumérés : politique budgétaire par les dépenses "
    "publiques et le déficit, politique de relance, soutien à "
    "l’investissement, stabilisation de l’économie. L’intervention ne "
    "remplace pas le marché, elle corrige son niveau d’activité."),
   ("Mais les agents anticipent l’intervention",
    "La Nouvelle Économie Classique soutient que si l’État relance la "
    "demande, les agents anticipent l’inflation future et ajustent leurs "
    "comportements : l’intervention est neutralisée, et il n’existe pas "
    "d’illusion monétaire durable."),
   ("Les imperfections réelles redonnent prise à l’action publique",
    "La Nouvelle Économie Keynésienne objecte que les prix et salaires ne "
    "s’ajustent pas instantanément — contrats de long terme, coûts de "
    "modification des prix, normes sociales, conventions salariales — et "
    "que l’information est imparfaite. L’intervention peut donc améliorer "
    "le fonctionnement du marché."),
   ("L’intervention contemporaine se déplace vers l’offre et la sécurité",
    "La politique industrielle soutient des secteurs, favorise "
    "l’innovation, renforce la souveraineté et développe des activités "
    "stratégiques. La justification n’est plus seulement la stabilisation "
    "mais la dépendance : le cours cite les masques, les médicaments, les "
    "semi-conducteurs.")],
  [{'a': "La liberté économique se justifie par un argument "
         "informationnel : pour l’école autrichienne, l’information est "
         "dispersée, fragmentée et subjective, aucun agent ne possède une "
         "vision globale, et le marché est un processus de coordination "
         "permanent dans lequel les prix transmettent l’information.",
    'cond': "L’argument exige des prix libres et significatifs, donc "
            "l’absence de contrôle administratif des prix et un degré "
            "suffisant de concurrence pour que les prix reflètent les "
            "raretés relatives.",
    'lim': "Il perd sa force quand le prix ne peut pas se former : sur un "
           "bien collectif non excluable, ou dans un marché détruit par "
           "l’asymétrie d’information comme le montre Akerlof, il n’y a "
           "précisément pas de signal à transmettre."},
   {'a': "L’intervention se justifie par l’existence d’équilibres "
         "durablement inefficaces : Keynes montre l’existence d’un "
         "équilibre de sous-emploi où le chômage est possible même à "
         "l’équilibre, l’économie pouvant être stable mais inefficace.",
    'cond': "Il faut que la demande globale soit effectivement insuffisante "
            "et que l’ajustement par les prix et les salaires soit lent ou "
            "impossible, ce que la Nouvelle Économie Keynésienne fonde sur "
            "les rigidités et les asymétries d’information.",
    'lim': "Si les agents anticipent correctement, l’effet de la relance "
           "est annulé : la Nouvelle Économie Classique soutient que toute "
           "intervention est anticipée et neutralisée, et que les erreurs "
           "sont rapidement corrigées."},
   {'a': "La liberté et l’intervention ne s’excluent pas : le cours relève "
         "que l’État finance souvent les innovations, que l’innovation est "
         "collective et que le succès entrepreneurial dépend du capital "
         "social et des réseaux, de sorte que la réussite privée repose sur "
         "un contexte collectif.",
    'cond': "Cette complémentarité suppose que l’action publique vise à "
            "élargir les capacités productives plutôt qu’à substituer la "
            "décision administrative à la décision privée.",
    'lim': "Le cours signale le risque inverse : la politique industrielle "
           "peut transformer les entreprises en chercheurs de rente, qui "
           "consacrent leurs ressources à obtenir et conserver les "
           "avantages distribués par l’État au lieu d’améliorer leur "
           "productivité."},
   {'a': "L’intervention retrouve une justification stratégique : la crise "
         "sanitaire et les tensions géopolitiques ont révélé des "
         "dépendances — masques, médicaments, respirateurs, gaz, "
         "semi-conducteurs — qui posent un problème de souveraineté "
         "industrielle et non seulement d’efficacité.",
    'cond': "L’argument vaut si la dépendance porte sur des biens "
            "réellement critiques et difficilement substituables à court "
            "terme, condition que le cours illustre par les infrastructures "
            "numériques et les métaux rares.",
    'lim': "Le cours montre le risque d’enchaînement : la recherche "
           "individuelle de sécurité économique peut contribuer "
           "collectivement à accroître l’insécurité, par fragmentation "
           "géoéconomique, diminution des interdépendances et hausse des "
           "tensions."}],
  [{'t': "Toute intervention est nocive parce qu’inefficace : les marchés "
         "sont efficaces, les agents parfaitement rationnels, la monnaie "
         "neutre même à court terme, et l’État est inutile voire nuisible.",
    'qui': "La Nouvelle Économie Classique, dont le cours souligne "
           "l’opposition irréductible avec les keynésiens.",
    'rep': "Le cours observe que cette position est rapidement critiquée "
           "pour des hypothèses jugées irréalistes, des agents trop "
           "rationnels et une incapacité à expliquer les crises majeures. "
           "La Nouvelle Économie Keynésienne montre qu’en présence de "
           "rigidités et d’asymétries, l’économie peut rester durablement "
           "en sous-emploi."},
   {'t': "La liberté économique n’est pas une fin : une situation peut être "
         "optimale au sens de Pareto tout en étant profondément inégale, "
         "car c’est un critère d’efficacité et non de justice.",
    'qui': "Le cours lui-même, qui écrit qu’un optimum de Pareto ne dit "
           "rien sur l’égalité ni sur la morale.",
    'rep': "L’objection est décisive mais déplace le débat : elle ne montre "
           "pas que l’intervention soit efficace, seulement que "
           "l’efficacité ne suffit pas à juger. Le cours la prolonge en "
           "soulignant que les inégalités sont aussi un choix de société, "
           "dépendant de la redistribution, du système fiscal, des "
           "institutions et de la protection sociale."},
   {'t': "L’intervention est capturée : les groupes organisés influencent "
         "les pouvoirs publics au détriment de l’intérêt collectif, et les "
         "entreprises consacrent leurs ressources à obtenir la protection "
         "plutôt qu’à améliorer leur productivité.",
    'qui': "L’école du Public Choice, dans la critique des politiques "
           "industrielles ciblées que le cours expose.",
    'rep': "La critique est fondée mais porte sur les modalités, non sur le "
           "principe : le cours montre par ailleurs que Pareto avait "
           "identifié l’asymétrie politique — gains concentrés, pertes "
           "diffuses — ce qui suggère des règles de procédure et de "
           "transparence plutôt que l’abstention."}],
  [{'n': "Adam Smith",
    'i': "La liberté économique n’abolit pas la régulation, elle la confie "
         "à la concurrence.",
    'p': "Le cours insiste : les individus sont égoïstes par nature, mais "
         "cet égoïsme est tempéré par les mécanismes du marché, les prix "
         "s’ajustant en permanence selon le rapport entre l’offre et la "
         "demande. La main invisible n’est donc pas une absence de règle "
         "mais un mécanisme impersonnel de discipline."},
   {'n': "John Maynard Keynes",
    'i': "Face à l’instabilité du marché, l’État doit intervenir et peut "
         "créer une demande autonome.",
    'p': "Le cours énumère ses moyens d’action : politique budgétaire par "
         "les dépenses publiques et le déficit, politique de relance, "
         "soutien à l’investissement, stabilisation de l’économie. Il "
         "précise que Keynes raisonne dans une économie de marché non "
         "planifiée : il ne rejette pas le marché, il critique son "
         "fonctionnement spontané."},
   {'n': "Friedrich Hayek",
    'i': "L’information économique est dispersée, fragmentée et "
         "subjective : aucun agent ne possède une vision globale du "
         "système.",
    'p': "Le cours présente l’école autrichienne comme rejetant l’idée d’un "
         "équilibre général et comme concevant le marché non comme un état "
         "mais comme un processus de coordination permanent, dans lequel "
         "les prix jouent un rôle central en transmettant de l’information. "
         "Elle adopte l’individualisme méthodologique et se méfie des "
         "modèles d’équilibre parfait."},
   {'n': "Gordon Tullock",
    'i': "L’intervention publique crée des rentes et déplace l’effort des "
         "entreprises vers leur captation.",
    'p': "Le cours expose le mécanisme de la recherche de rente dans la "
         "critique des politiques industrielles ciblées : rentes attendues, "
         "lobbying en hausse, ressources consacrées à obtenir la protection "
         "en hausse, efficacité économique en baisse. Les groupes organisés "
         "peuvent influencer les pouvoirs publics au détriment de l’intérêt "
         "collectif."}],
  [{'f': "Colbert supprime les droits de douane entre les villes du pays "
         "tout en menant à l’extérieur un protectionnisme sélectif, avec "
         "pour objectif d’exporter au maximum et d’attirer les capitaux.",
    'p': "L’intervention mercantiliste n’est pas une simple fermeture : "
         "elle combine libéralisation interne et sélection externe, ce qui "
         "montre que liberté et intervention se combinent selon les "
         "échelles dès l’origine du débat."},
   {'f': "La Nouvelle Économie Classique soutient que si l’État relance la "
         "demande, les agents anticipent l’inflation future et ajustent "
         "leurs comportements, de sorte que la monnaie est neutre même à "
         "court terme.",
    'p': "L’argument ne porte pas sur la légitimité de l’intervention mais "
         "sur son efficacité : c’est le déplacement le plus important du "
         "débat au XXᵉ siècle, puisqu’il rend la discussion technique "
         "plutôt que doctrinale."},
   {'f': "La Nouvelle Économie Keynésienne identifie trois sources "
         "d’imperfection : rigidités des prix et des salaires, asymétries "
         "d’information, concurrence imparfaite — et conclut que "
         "l’intervention peut améliorer le fonctionnement du marché.",
    'p': "L’espace de l’intervention est reconstruit depuis l’intérieur des "
         "microfondements néoclassiques, ce qui explique que la plupart des "
         "modèles utilisés par les banques centrales soient aujourd’hui "
         "d’inspiration nouvelle keynésienne."},
   {'f': "Le cours relie le retour du débat à des chocs précis : le Covid "
         "révèle des dépendances sur les masques, les médicaments et les "
         "respirateurs, la guerre en Ukraine une vulnérabilité énergétique.",
    'p': "La justification contemporaine de l’intervention est moins la "
         "stabilisation conjoncturelle que la sécurité "
         "d’approvisionnement : le critère devient la vulnérabilité "
         "stratégique et non le seul écart à l’optimum."}],
  [{'q': "L’État doit-il intervenir dans l’économie ?",
    'f': "La question doit être découpée en trois. L’intervention est-elle "
         "légitime : oui lorsque le marché ne peut pas produire le résultat "
         "attendu, ce qu’établit la théorie des défaillances de marché. "
         "Est-elle efficace : la Nouvelle Économie Classique en doute, "
         "puisque les agents anticipent et neutralisent la relance, mais la "
         "Nouvelle Économie Keynésienne rétablit son efficacité en "
         "montrant que les rigidités et les asymétries empêchent "
         "l’ajustement. Est-elle bien conduite : l’école des choix publics "
         "objecte que l’État est imparfait et biaisé et que les politiques "
         "ciblées nourrissent la recherche de rente.",
    'r': "Ce plan est rigoureux parce qu’il sépare trois questions que la "
         "formulation du sujet confond, et parce qu’à chaque niveau le "
         "cours fournit à la fois une position et sa réfutation.",
    'ex': "Le passage d’une Nouvelle Économie Classique jugeant l’État "
          "inutile voire nocif à des modèles de banques centrales "
          "d’inspiration nouvelle keynésienne."},
   {'q': "La liberté économique est-elle un principe ou un moyen ?",
    'f': "Le cours la traite comme un moyen, et c’est ce qui rend le débat "
         "argumentable. Chez Smith, la liberté vaut parce que la "
         "concurrence tempère l’égoïsme et fait converger l’intérêt privé "
         "et la richesse des nations. Chez l’école autrichienne, elle vaut "
         "parce que l’information est dispersée et que les prix la "
         "transmettent. Mais dès que le mécanisme cesse d’opérer — bien "
         "collectif non excluable, bien commun surexploité, marché détruit "
         "par l’asymétrie d’information — la justification tombe avec lui. "
         "La liberté est alors défendue pour ses effets, donc évaluable par "
         "eux.",
    'r': "Ce raisonnement est solide parce qu’il s’appuie sur la "
         "justification que les auteurs donnent eux-mêmes de la liberté, et "
         "non sur une préférence : il suffit alors de vérifier si les "
         "conditions du mécanisme sont réunies.",
    'ex': "La tragédie des communs, où la liberté d’usage détruit la "
          "ressource dont dépendent tous les usagers."},
   {'q': "Le retour des politiques industrielles marque-t-il la fin du "
         "libéralisme économique ?",
    'f': "Il marque un déplacement de ses justifications plutôt qu’un "
         "abandon. Les chocs récents — dépendances révélées par le Covid "
         "sur les masques et les médicaments, vulnérabilité énergétique "
         "liée à la guerre en Ukraine, tensions sur les semi-conducteurs — "
         "font de la souveraineté industrielle un objectif explicite, que "
         "la politique industrielle poursuit en soutenant des secteurs et "
         "en favorisant l’innovation. Mais les objections libérales "
         "subsistent : ces politiques modifient la concurrence "
         "internationale, entrent en tension avec le principe de "
         "non-discrimination et peuvent transformer les entreprises en "
         "chercheurs de rente.",
    'r': "Le plan tient parce qu’il confronte une justification nouvelle, "
         "la sécurité, à une critique ancienne, la capture, toutes deux "
         "documentées dans le cours, et parce qu’il évite de conclure d’un "
         "changement d’instrument à un changement de doctrine.",
    'ex': "La fragmentation géoéconomique, où la recherche individuelle de "
          "sécurité accroît collectivement l’insécurité."}],
  comp={'titre': "Liberté et intervention : les positions du cours",
        'a': "Primauté de la liberté", 'b': "Nécessité de l’intervention",
        'lignes': [
            ("Fondement",
             "La concurrence tempère l’égoïsme et ajuste les prix",
             "Le marché peut rester durablement en sous-emploi"),
            ("Auteurs", "Physiocrates, Smith, école autrichienne, NEC",
             "Colbert, Keynes, Pigou, NEK"),
            ("Vue sur l’information",
             "Dispersée : les prix la transmettent mieux que l’État",
             "Imparfaite et asymétrique : le marché ne l’agrège pas"),
            ("Vue sur l’ajustement", "Rapide, par la flexibilité des prix",
             "Lent ou impossible : contrats, menu costs, conventions"),
            ("Vue sur la monnaie", "Neutre, simple voile sur le réel",
             "Non neutre : elle agit sur l’investissement et l’emploi"),
            ("Effet attendu de la relance",
             "Anticipée puis neutralisée par les agents",
             "Soutien de la demande globale et de l’emploi"),
            ("Risque principal",
             "Équilibres inefficaces durables et coûts sociaux concentrés",
             "Décision arbitraire, capture, recherche de rente"),
            ("Instrument contemporain",
             "Ouverture, concurrence, règles multilatérales",
             "Politique industrielle, souveraineté, sécurité économique"),
            ("Critère d’évaluation",
             "Efficacité allocative, optimum de Pareto",
             "Niveau d’emploi, répartition, sécurité d’approvisionnement")]},
  voisins=['n26-marche-etat', 'n26-autoregulation-instabilite',
           'n26-efficacite-justice', 'n27-regulation', 'n27-souverainete'])

d('n26-offre-demande', 26, "Offre et demande",
  "Qui commande l’activité : la capacité de produire ou la volonté de dépenser",
  "Le débat porte sur le déterminant du niveau d’activité. Pour la loi de "
  "Say, l’offre crée sa propre demande : produire distribue des revenus qui "
  "reviennent en dépenses, d’où l’impossibilité d’une crise générale "
  "durable. Pour Keynes, la demande n’est pas automatiquement suffisante et "
  "la demande effective devient le déterminant central de l’activité, ce "
  "que le cours présente comme la rupture centrale de son analyse.",
  "Le cours expose d’abord la loi de Say dans son détail. Quand on produit, "
  "on distribue forcément des revenus : salaires aux travailleurs, profits "
  "aux entrepreneurs, rentes aux propriétaires. L’enchaînement est donc "
  "production → revenus → dépenses → demande, autrement dit les revenus "
  "créés par la production financent l’achat de cette production. Il en "
  "résulte qu’une crise générale durable est impossible : il peut y avoir "
  "des déséquilibres sectoriels, non une insuffisance globale. Le cours "
  "souligne la filiation : Say → Walras → Arrow-Debreu, c’est-à-dire "
  "l’histoire de l’optimisme néoclassique sur l’équilibre, Walras "
  "s’inspirant de Say pour construire un système d’équations comportant "
  "autant d’équations que d’inconnues et donc admettant une solution. Le "
  "cours relève immédiatement le point faible : pour qu’il y ait "
  "équilibre, il faut que les courbes se croisent, et Walras suppose "
  "implicitement que l’offre et la demande se rencontrent toujours, alors "
  "que rien ne le garantit. Il ajoute une seconde fragilité, apportée par "
  "Sonnenschein : les marchés sont interdépendants, ce qui rend la courbe "
  "de demande plus incertaine, de sorte que même si chaque agent est "
  "rationnel et chaque marché bien modélisé, l’ensemble du système peut "
  "devenir imprévisible — la microéconomie propre ne garantit plus une "
  "macroéconomie propre. Vient alors Keynes. Le cours note d’abord un point "
  "commun souvent oublié : Malthus avait montré qu’une demande effective "
  "insuffisante pouvait provoquer une crise, et Keynes généralise cette "
  "idée pour faire de la demande effective le déterminant central de "
  "l’activité. La différence est nette : là où la loi de Say rend "
  "impossible une crise générale durable, Keynes affirme la possibilité de "
  "crises durables. Le mécanisme est détaillé en deux schémas liés : une "
  "demande globale insuffisante entraîne une production faible ; une "
  "production faible entraîne peu d’emplois, donc du chômage involontaire, "
  "les travailleurs voulant travailler au salaire en vigueur sans que les "
  "entreprises embauchent. La conclusion centrale est que l’emploi dépend "
  "de la demande globale et non du seul marché du travail. Le cours montre "
  "enfin que l’opposition se rejoue dans les politiques contemporaines : "
  "les politiques de compétitivité agissent sur l’offre, par le coût du "
  "travail, la qualité et l’innovation, tandis que les politiques de "
  "soutien du pouvoir d’achat agissent sur la demande.",
  [("Produire distribue des revenus",
    "La production verse des salaires aux travailleurs, des profits aux "
    "entrepreneurs et des rentes aux propriétaires. Le cours résume "
    "l’enchaînement : production → revenus → dépenses → demande."),
   ("Les revenus distribués peuvent racheter la production",
    "Si l’intégralité des revenus est dépensée, la demande égale par "
    "construction la valeur de la production. C’est le cœur de la loi de "
    "Say : l’offre crée sa propre demande, donc pas de crise générale."),
   ("Mais une partie des revenus peut ne pas être dépensée",
    "Chez Keynes, la consommation augmente moins vite que le revenu et "
    "l’épargne n’est pas toujours bénéfique : une épargne excessive réduit "
    "la demande. Le circuit de Say est alors interrompu en son milieu."),
   ("L’investissement ne compense pas automatiquement",
    "Il dépend des anticipations des entrepreneurs, de la confiance et des "
    "esprits animaux, et non seulement du taux d’intérêt. Les décisions "
    "sont incertaines et psychologiques, donc non garanties d’égaler "
    "l’épargne au niveau de plein emploi."),
   ("La demande insuffisante détermine la production",
    "Premier schéma du cours : demande globale insuffisante, donc "
    "production faible. Les entreprises produisent ce qu’elles anticipent "
    "pouvoir vendre, non ce que la capacité installée permettrait."),
   ("La production faible détermine l’emploi",
    "Second schéma : production faible, donc peu d’emplois, donc chômage "
    "involontaire. Les travailleurs veulent travailler au salaire en "
    "vigueur mais les entreprises n’embauchent pas."),
   ("D’où l’inversion de la causalité",
    "Le cours énonce la conclusion centrale : l’emploi dépend de la demande "
    "globale et non du seul marché du travail. La baisse des salaires ne "
    "résorbe donc pas nécessairement le chômage, puisqu’elle réduit aussi "
    "la demande.")],
  [{'a': "La loi de Say fournit une cohérence comptable réelle : toute "
         "production distribue effectivement des revenus, salaires, profits "
         "et rentes, de sorte qu’il existe à chaque instant un pouvoir "
         "d’achat égal à la valeur produite.",
    'cond': "L’argument tient si les revenus distribués sont intégralement "
            "dépensés, directement en consommation ou indirectement par "
            "l’investissement financé par l’épargne, ce que les classiques "
            "admettent en jugeant l’épargne vertueuse.",
    'lim': "Keynes conteste précisément ce passage : trop d’épargne peut "
           "freiner l’activité, et l’investissement dépend des "
           "anticipations et de la confiance plutôt que du seul taux "
           "d’intérêt. La capacité de dépenser n’implique pas la décision "
           "de dépenser."},
   {'a': "La priorité à la demande explique un fait que l’analyse par "
         "l’offre n’explique pas : l’existence d’un chômage involontaire, "
         "où les travailleurs veulent travailler au salaire en vigueur mais "
         "où les entreprises n’embauchent pas.",
    'cond': "Il faut que l’ajustement par les prix et les salaires soit "
            "lent ou bloqué, ce que la Nouvelle Économie Keynésienne fonde "
            "sur les contrats de long terme, les coûts de modification des "
            "prix, les normes sociales et les conventions salariales.",
    'lim': "Si les agents anticipent correctement, la relance de la demande "
           "est neutralisée : la Nouvelle Économie Classique soutient qu’il "
           "n’existe pas d’illusion monétaire durable et que les erreurs "
           "sont rapidement corrigées."},
   {'a': "L’analyse par l’offre reste indispensable en économie ouverte : "
         "le cours montre que la compétitivité dépend du coût du travail "
         "mais aussi de la compétitivité hors-prix — qualité, innovation, "
         "montée en gamme —, ce qui relève des conditions de production.",
    'cond': "L’argument vaut lorsque la contrainte extérieure est "
            "effective, c’est-à-dire lorsqu’une relance de la demande "
            "intérieure se traduit surtout en importations plutôt qu’en "
            "production nationale.",
    'lim': "Le cours montre que la compétitivité-prix a ses propres "
           "limites : la stratégie allemande repose sur la qualité et la "
           "gamme plutôt que sur les bas coûts, et la concurrence par les "
           "coûts peut dégénérer en moins-disant social entre territoires."},
   {'a': "Les deux analyses sont articulables par l’horizon temporel : le "
         "cours oppose un raisonnement classique statique ou de long terme, "
         "avec des ajustements supposés rapides, à un temps keynésien "
         "historique et incertain où le futur n’est pas calculable.",
    'cond': "Cette articulation suppose d’admettre que les déterminants de "
            "l’activité diffèrent selon l’horizon : la demande à court "
            "terme, les capacités productives et la productivité à long "
            "terme.",
    'lim': "Le cours rappelle la critique keynésienne du long terme : les "
           "décisions sont prises sous incertitude radicale, et un "
           "équilibre de sous-emploi peut être stable, donc durable. Le "
           "long terme n’est pas un état vers lequel on converge "
           "nécessairement."}],
  [{'t': "Une crise générale durable est impossible : l’offre crée sa "
         "propre demande, de sorte que les déséquilibres ne peuvent être "
         "que sectoriels et transitoires.",
    'qui': "Say, dont le cours résume la loi par « l’offre crée sa propre "
           "demande », et les classiques au sens de Keynes.",
    'rep': "Le cours présente la réfutation en deux niveaux. "
           "Théoriquement, Keynes établit l’existence d’un équilibre de "
           "sous-emploi : le chômage est possible même à l’équilibre, "
           "l’économie pouvant être stable mais inefficace. "
           "Historiquement, Malthus avait déjà envisagé qu’une demande "
           "effective insuffisante provoque une crise."},
   {'t': "Le chômage est volontaire et dû à la rigidité des salaires : il "
         "suffirait que les salaires baissent pour que le marché du travail "
         "s’équilibre.",
    'qui': "Les classiques et néoclassiques, dans la comparaison "
           "explicite du cours.",
    'rep': "Keynes répond que le chômage est involontaire et causé par une "
           "insuffisance de la demande effective, ce qui en fait un "
           "problème macroéconomique. Le cours ajoute le mécanisme "
           "décisif : l’emploi dépend de la demande globale, et non du seul "
           "marché du travail, de sorte qu’une baisse des salaires réduit "
           "aussi les revenus et donc la demande."},
   {'t': "Même en acceptant le raisonnement en équilibre, l’existence d’un "
         "équilibre n’est pas garantie : rien n’assure que la courbe "
         "d’offre et la courbe de demande se coupent.",
    'qui': "Le cours lui-même, qui signale ce point faible chez Walras, et "
           "Sonnenschein, qui montre que l’interdépendance des marchés rend "
           "la courbe de demande plus incertaine.",
    'rep': "C’est une critique interne, et la plus forte : elle n’oppose "
           "pas une doctrine à une autre mais montre que même en acceptant "
           "les hypothèses, la conclusion ne suit pas. Le cours en tire que "
           "la microéconomie propre ne garantit plus une macroéconomie "
           "propre."}],
  [{'n': "Jean-Baptiste Say",
    'i': "L’offre crée sa propre demande : produire distribue des revenus "
         "qui financent l’achat de la production.",
    'p': "Le cours détaille la distribution — salaires aux travailleurs, "
         "profits aux entrepreneurs, rentes aux propriétaires — et "
         "l’enchaînement production → revenus → dépenses → demande. Il en "
         "tire l’impossibilité d’une crise générale durable et souligne la "
         "filiation Say → Walras → Arrow-Debreu, qui constitue l’histoire "
         "de l’optimisme néoclassique sur l’équilibre."},
   {'n': "John Maynard Keynes",
    'i': "La demande effective est le déterminant central de l’activité, et "
         "l’emploi dépend de la demande globale.",
    'p': "Le cours décrit la double chaîne : demande globale insuffisante → "
         "production faible, puis production faible → peu d’emplois → "
         "chômage involontaire. Il ajoute que la consommation augmente "
         "moins vite que le revenu, que l’épargne excessive réduit la "
         "demande et que l’investissement dépend des anticipations, de la "
         "confiance et des esprits animaux."},
   {'n': "Thomas Malthus",
    'i': "Une demande effective insuffisante peut provoquer une crise.",
    'p': "Le cours fait de cette intuition un point commun réel entre "
         "Keynes et l’un des classiques : dans sa comparaison des "
         "positions sur la régulation et les crises, Malthus est celui qui "
         "envisage une insuffisance de la demande, là où Say l’exclut et où "
         "Ricardo n’attend qu’un ralentissement progressif. Keynes "
         "généralise cette idée."},
   {'n': "Léon Walras",
    'i': "L’équilibre simultané de tous les marchés existe, parce que "
         "l’économie est un système comportant autant d’équations que "
         "d’inconnues.",
    'p': "Le cours précise qu’il s’inspire de Say et que son résultat est "
         "très optimiste : l’économie apparaît fondamentalement stable et "
         "autorégulée. Mais il signale le point faible : Walras suppose "
         "implicitement que l’offre et la demande se rencontrent toujours, "
         "alors que rien ne garantit que les courbes se coupent."}],
  [{'f': "Le cours résume la loi de Say par l’enchaînement production → "
         "revenus → dépenses → demande, et en déduit l’impossibilité d’une "
         "crise générale.",
    'p': "L’argument est comptable avant d’être comportemental : c’est "
         "précisément pourquoi sa réfutation doit porter sur les "
         "comportements, c’est-à-dire sur la décision de dépenser et non "
         "sur la capacité de dépenser."},
   {'f': "Keynes établit l’existence d’un équilibre de sous-emploi : le "
         "chômage est possible même à l’équilibre, l’économie pouvant être "
         "stable mais inefficace.",
    'p': "La notion d’équilibre cesse d’être un critère de bon "
         "fonctionnement : on peut être à l’équilibre et au chômage, ce qui "
         "retire à l’équilibre sa portée normative."},
   {'f': "Sonnenschein montre que l’interdépendance des marchés rend la "
         "courbe de demande plus incertaine, de sorte que même avec des "
         "agents rationnels, l’ensemble du système peut devenir "
         "imprévisible.",
    'p': "La critique de la primauté de l’offre ne vient pas seulement de "
         "Keynes : elle vient aussi de l’intérieur de la théorie de "
         "l’équilibre général, ce qui en renforce considérablement la "
         "portée."},
   {'f': "Le cours oppose deux stratégies de compétitivité : la "
         "robotisation pour compenser le coût du travail, et la stratégie "
         "allemande de compétitivité hors-prix fondée sur la qualité, "
         "l’innovation et la gamme.",
    'p': "Agir sur l’offre n’équivaut pas à comprimer les coûts : le débat "
         "offre/demande se rejoue à l’intérieur même des politiques "
         "d’offre, entre prix et hors-prix."}],
  [{'q': "L’activité économique est-elle déterminée par l’offre ou par la "
         "demande ?",
    'f': "Le cours fournit la confrontation complète. Pour Say, l’offre "
         "crée sa propre demande puisque produire distribue des revenus, "
         "d’où l’impossibilité d’une crise générale durable ; Walras "
         "formalise cette intuition, Arrow et Debreu la prolongent. Pour "
         "Keynes, la demande n’est pas automatiquement suffisante : une "
         "demande globale insuffisante produit une production faible, donc "
         "peu d’emplois et un chômage involontaire, l’emploi dépendant de "
         "la demande globale et non du seul marché du travail. La "
         "divergence porte donc sur une étape précise du circuit : le "
         "passage des revenus distribués aux dépenses effectives.",
    'r': "Ce raisonnement est rigoureux parce qu’il localise exactement le "
         "désaccord au lieu de l’opposer en bloc : Keynes ne nie pas que la "
         "production distribue des revenus, il nie que ces revenus soient "
         "nécessairement dépensés.",
    'ex': "Le paradoxe de l’épargne : ce qui est rationnel individuellement "
          "peut être nuisible collectivement."},
   {'q': "Le chômage est-il un problème de marché du travail ?",
    'f': "Non pour Keynes, et le cours en fournit la démonstration en deux "
         "schémas. Si la demande globale est insuffisante, la production "
         "est faible ; si la production est faible, il y a peu d’emplois et "
         "donc un chômage involontaire, les travailleurs voulant travailler "
         "au salaire en vigueur sans que les entreprises embauchent. La "
         "conclusion centrale est que l’emploi dépend de la demande "
         "globale. À l’inverse, pour les classiques et néoclassiques, le "
         "chômage est volontaire et dû à la rigidité des salaires. La "
         "divergence est donc une divergence de causalité, non de "
         "constatation.",
    'r': "Le plan est solide parce qu’il reconstitue la chaîne causale "
         "keynésienne étape par étape et parce qu’il montre que la solution "
         "préconisée découle mécaniquement du diagnostic : baisser les "
         "salaires si le marché du travail est en cause, soutenir la "
         "demande s’il ne l’est pas.",
    'ex': "La zone de chômage involontaire décrite par le cours, où l’offre "
          "de travail dépasse la demande de travail au salaire en vigueur."},
   {'q': "Les politiques d’offre et de demande sont-elles substituables ?",
    'f': "Elles répondent à des diagnostics différents et le choix dépend "
         "de la contrainte qui mord. Si la contrainte est la demande, le "
         "soutien du pouvoir d’achat accroît la production, puis l’emploi. "
         "Si la contrainte est la compétitivité, l’action porte sur les "
         "conditions de production, le cours opposant la robotisation "
         "destinée à compenser le coût du travail à la stratégie allemande "
         "de compétitivité hors-prix fondée sur la qualité, l’innovation et "
         "la gamme. Si la contrainte est l’anticipation, aucune des deux "
         "n’opère seule, puisque la relance peut être neutralisée.",
    'r': "Ce raisonnement est rigoureux parce qu’il subordonne le choix de "
         "l’instrument au diagnostic de la contrainte active, ce qui évite "
         "la querelle doctrinale et s’appuie sur trois configurations "
         "effectivement décrites dans le cours.",
    'ex': "La réindustrialisation européenne, qui pose la question du coût "
          "de production et de la vendabilité du produit."}],
  comp={'titre': "Loi de Say et demande effective",
        'a': "Primauté de l’offre (Say)",
        'b': "Primauté de la demande (Keynes)",
        'lignes': [
            ("Enchaînement de base",
             "Production → revenus → dépenses → demande",
             "Demande globale → production → emploi"),
            ("Crise générale durable", "Impossible",
             "Possible : équilibre de sous-emploi"),
            ("Statut de l’épargne",
             "Vertueuse : elle finance l’investissement",
             "Potentiellement destructrice à court terme"),
            ("Déterminant de l’investissement",
             "Le taux d’intérêt et l’épargne disponible",
             "Les anticipations, la confiance, les esprits animaux"),
            ("Nature du chômage", "Volontaire, dû à la rigidité des salaires",
             "Involontaire, dû à l’insuffisance de la demande effective"),
            ("Remède au chômage", "Flexibilité des salaires et des prix",
             "Soutien de la demande globale par l’État"),
            ("Prolongement théorique", "Walras, puis Arrow-Debreu",
             "Hicks et Samuelson, synthèse néo-keynésienne"),
            ("Critique interne",
             "Rien ne garantit que les courbes se coupent (Sonnenschein)",
             "La relance peut être anticipée et neutralisée (NEC)"),
            ("Politique correspondante",
             "Compétitivité, coûts, innovation, montée en gamme",
             "Pouvoir d’achat, dépenses publiques, investissement public")]},
  voisins=['n26-equilibre-desequilibre', 'n26-epargne-investissement',
           'n26-autoregulation-instabilite', 'n26-court-long-terme',
           'n26-marche-etat'])

d('n26-production-repartition', 26, "Production et répartition",
  "Créer la richesse et la partager : une seule question ou deux ?",
  "Le débat porte sur la relation entre la création de la richesse et son "
  "partage. Pour l’économie politique classique et pour Marx, la "
  "répartition est inséparable de la production, puisque la place occupée "
  "dans la production détermine le revenu reçu. Pour les néoclassiques, le "
  "regard se déplace vers les choix individuels et la formation des prix, "
  "et le cours note que l’on passe alors d’une économie centrée sur la "
  "répartition et les rapports sociaux à une économie des choix.",
  "Le cours construit le débat par une histoire de la pensée. Quesnay "
  "raisonne d’emblée en termes de circuit : l’économie est un circuit où la "
  "richesse circule entre classes sociales, et son tableau montre comment "
  "le produit net créé par la classe productive circule vers les "
  "propriétaires et la classe stérile. Production et répartition ne sont "
  "pas deux questions mais deux moments d’un même mouvement. Ricardo "
  "reprend le classement en classes — propriétaires, capitalistes, "
  "travailleurs — et fait de la répartition entre rente, profit et salaire "
  "le cœur de l’analyse ; le cours souligne que, par la loi des rendements "
  "décroissants, la hausse des rentes et la baisse des profits, la "
  "croissance peut finir par se bloquer dans un état stationnaire : la "
  "répartition agit donc en retour sur la production. Marx radicalise : le "
  "profit repose sur l’exploitation du travail, le capitaliste payant le "
  "travailleur moins que la valeur qu’il produit, et la différence "
  "constitue la plus-value, source du profit. Le cours précise que la rente "
  "foncière et le profit industriel sont deux formes d’appropriation de la "
  "plus-value, ce qui unifie les revenus non salariaux. La répartition "
  "détermine en retour la dynamique : la composition organique du capital "
  "augmente, le taux de profit baisse tendanciellement, et cette baisse "
  "explique crises, chômage, surproduction et tensions sociales. Le "
  "renversement néoclassique est explicite dans le cours : les "
  "néoclassiques s’intéressent moins aux classes sociales et aux "
  "contradictions historiques du capitalisme qu’aux choix individuels, aux "
  "comportements des agents et aux mécanismes de formation des prix ; on "
  "passe ainsi d’une économie politique centrée sur la production, la "
  "répartition et les rapports sociaux à une économie des choix "
  "individuels, et il n’y a plus de classes sociales dans la "
  "microéconomie. Le cours fournit enfin les instruments contemporains du "
  "lien entre les deux. Le partage de la valeur ajoutée est mesuré : taux "
  "de marge d’environ 32 % en 2022, part de la valeur ajoutée restant après "
  "rémunération des salariés, cotisations et impôts de production, et le "
  "cours montre qu’un taux de marge élevé nourrit l’épargne brute et donc "
  "l’autofinancement des investissements, tandis qu’un taux faible la "
  "réduit. La répartition primaire conditionne ainsi la capacité "
  "d’investir, c’est-à-dire la production future.",
  [("La production distribue nécessairement des revenus",
    "Toute production verse des salaires, des profits et des rentes. Le "
    "circuit de Quesnay montre que la richesse créée par une classe "
    "circule vers les autres : la répartition n’est pas une opération "
    "ajoutée après coup, elle est la forme même de la circulation."),
   ("La place dans la production fixe la forme du revenu",
    "Rente pour les propriétaires, profit pour les capitalistes, salaire "
    "pour les travailleurs. La position détermine donc non seulement le "
    "montant mais la nature du revenu, donc sa dynamique propre."),
   ("Le partage détermine le surplus disponible",
    "Le taux de marge mesure ce qui reste de la valeur ajoutée après "
    "rémunération des salariés, cotisations et impôts de production. Un "
    "taux élevé laisse un excédent brut d’exploitation important, un taux "
    "bas l’épuise."),
   ("Le surplus détermine la capacité d’investir",
    "Le cours décrit la suite : l’excédent sert à verser des intérêts, à "
    "payer l’impôt sur les sociétés, à distribuer des dividendes et à "
    "garder une épargne brute qui finance directement les investissements. "
    "Un taux de marge élevé rend l’entreprise plus autonome."),
   ("La capacité d’investir détermine la production future",
    "L’autofinancement, mesuré par le rapport de l’épargne brute à la "
    "formation brute de capital fixe, conditionne le renouvellement et "
    "l’extension de l’appareil productif. La répartition d’aujourd’hui "
    "fixe donc la production de demain."),
   ("Mais la répartition peut aussi bloquer la production",
    "Chez Ricardo, la hausse des rentes et la baisse des profits liées aux "
    "rendements décroissants peuvent conduire à l’état stationnaire. Chez "
    "Marx, la hausse de la composition organique fait baisser le taux de "
    "profit et provoque crises et surproduction."),
   ("Le changement de cadre théorique dissout la question",
    "Quand les néoclassiques partent des choix individuels et de la "
    "formation des prix, la répartition devient une conséquence des "
    "dotations et des productivités marginales, non un rapport social à "
    "expliquer : il n’y a plus de classes dans la microéconomie.")],
  [{'a': "Traiter production et répartition ensemble permet d’expliquer des "
         "dynamiques de long terme que la seule analyse de la production "
         "n’explique pas : chez Ricardo, la hausse des rentes et la baisse "
         "des profits peuvent bloquer la croissance dans un état "
         "stationnaire.",
    'cond': "L’argument suppose que les parts de revenu ne soient pas "
            "indépendantes du niveau de production, ce que fonde la loi des "
            "rendements décroissants appliquée à la terre.",
    'lim': "Le cours signale que le progrès technique contrarie ce "
           "mécanisme : chez Boserup, la pression démographique devient "
           "créatrice, et dans l’analyse de la croissance l’innovation "
           "repousse les rendements décroissants. L’état stationnaire "
           "ricardien n’a pas été observé."},
   {'a': "La répartition primaire est mesurable et commande directement "
         "l’investissement : le taux de marge, d’environ 32 % en 2022, "
         "détermine l’excédent brut d’exploitation, donc l’épargne brute, "
         "donc l’autofinancement.",
    'cond': "Le raisonnement vaut si l’entreprise finance effectivement ses "
            "investissements sur ressources propres, ce qui dépend du "
            "régime de financement — économie d’endettement ou économie de "
            "marchés financiers.",
    'lim': "Le cours relativise : l’excédent peut aussi servir à verser des "
           "intérêts, payer l’impôt sur les sociétés et distribuer des "
           "dividendes. Un taux de marge élevé n’implique donc pas "
           "mécaniquement un investissement élevé."},
   {'a': "Séparer analytiquement production et répartition a un avantage "
         "méthodologique réel : cela permet d’étudier la formation des prix "
         "et l’allocation des ressources sans préjuger des rapports "
         "sociaux, ce qui a rendu possible la microéconomie moderne.",
    'cond': "La séparation est légitime si la répartition n’agit pas sur "
            "l’efficacité de l’allocation, hypothèse implicite dans le "
            "critère de Pareto, qui juge les situations sans considérer la "
            "distribution.",
    'lim': "Le cours montre la fragilité de cette hypothèse en rappelant "
           "qu’un optimum de Pareto est un critère d’efficacité et non de "
           "justice : il ne dit rien sur l’égalité ni sur la morale, il "
           "dit seulement qu’on ne peut plus améliorer sans coût."},
   {'a': "La répartition agit sur la production par la demande : le partage "
         "de la valeur ajoutée détermine la masse salariale, donc le "
         "revenu disponible brut des ménages, donc la consommation, dont "
         "Keynes fait le déterminant de l’activité.",
    'cond': "Ce canal suppose que la propension à consommer des salariés "
            "excède celle des détenteurs de capital, de sorte qu’un "
            "déplacement du partage modifie la demande globale.",
    'lim': "En économie ouverte, une hausse de la part salariale peut "
           "augmenter le coût du travail et donc dégrader la "
           "compétitivité-prix, mécanisme que le cours décrit à propos des "
           "cotisations sociales et de la concurrence internationale."}],
  [{'t': "La répartition n’est pas un objet économique distinct : il faut "
         "partir des individus, de leurs préférences et de leurs "
         "ressources, puis agréger les comportements pour comprendre le "
         "fonctionnement du marché.",
    'qui': "Les néoclassiques, dont le cours dit qu’ils s’intéressent "
           "moins aux classes sociales et aux rapports de domination qu’aux "
           "choix individuels et à la formation des prix.",
    'rep': "Le cours ne traite pas ce déplacement comme un progrès net : il "
           "le qualifie de passage d’une économie politique centrée sur la "
           "production, la répartition et les rapports sociaux à une "
           "économie des choix individuels. Ce qui est gagné en rigueur "
           "formelle est perdu en capacité à penser le partage."},
   {'t': "La répartition est entièrement déterminée par la production : "
         "chaque facteur reçoit ce qu’il contribue à produire, de sorte "
         "qu’il n’y a pas de question distincte du partage.",
    'rep': "Marx conteste cette identité : la valeur d’échange de la force "
           "de travail est le salaire, nécessaire à la reproduction de "
           "cette force, tandis que sa valeur d’usage est la capacité à "
           "produire de la valeur nouvelle. L’écart entre les deux, la "
           "plus-value, montre qu’une contribution productive peut n’être "
           "pas rémunérée à sa hauteur."},
   {'t': "Corriger la répartition nuit à la production : une hausse des "
         "impôts ou des cotisations augmente le coût du travail, élève les "
         "prix, dégrade la compétitivité, réduit le salaire net, la "
         "consommation et donc la croissance.",
    'qui': "Le cours expose cet enchaînement à propos de la résistance aux "
           "prélèvements, et le relie à l’idée de Laffer selon laquelle "
           "trop d’impôt tue l’impôt.",
    'rep': "Le cours présente l’argument avec ses reproches et lui oppose "
           "un fait de mesure : les écarts de niveau de vie passent d’un "
           "rapport de 18 avant redistribution à 4 après, 53 % des ménages "
           "étant bénéficiaires nets. La redistribution modifie donc "
           "massivement le partage sans que la production se soit "
           "effondrée."}],
  [{'n': "François Quesnay",
    'i': "L’économie est un circuit où la richesse circule entre classes "
         "sociales.",
    'p': "Le cours en fait le premier à raisonner ainsi et souligne la "
         "portée méthodologique : penser l’économie comme un circuit fait "
         "de lui l’ancêtre de la comptabilité nationale moderne. Son "
         "tableau montre comment le produit net, créé par la seule classe "
         "productive, se répartit entre les trois classes indissociables."},
   {'n': "David Ricardo",
    'i': "La répartition entre rente, profit et salaire commande la "
         "dynamique de la croissance.",
    'p': "Le cours le présente comme un classique pessimiste : avec la loi "
         "des rendements décroissants, la hausse des rentes et la baisse "
         "des profits, la croissance peut finir par se bloquer dans un état "
         "stationnaire. La répartition n’est donc pas une conséquence de la "
         "production, elle en est aussi une cause."},
   {'n': "Karl Marx",
    'i': "La plus-value est la part de la valeur produite par le "
         "travailleur et non versée dans son salaire.",
    'p': "Le cours formule l’identité retenue — plus-value = ce que "
         "rapporte le salarié moins son salaire — et précise que la rente "
         "foncière et le profit industriel sont deux formes d’appropriation "
         "de cette plus-value, provenant toutes deux du capital. La "
         "répartition devient ainsi mesurable par le taux de plus-value "
         "PL/V."},
   {'n': "Vilfredo Pareto",
    'i': "Une situation est optimale si l’on ne peut améliorer la situation "
         "de quelqu’un sans détériorer celle d’un autre.",
    'p': "Le cours insiste sur la portée de ce critère pour le débat : il "
         "s’agit d’un critère d’efficacité et non de justice, qui ne dit "
         "rien sur l’égalité ni sur la morale. Il permet donc de juger la "
         "production sans juger la répartition, ce qui est exactement la "
         "séparation que l’économie politique classique refusait."}],
  [{'f': "Quesnay réserve le produit net à la seule classe productive, les "
         "agriculteurs fermiers, les propriétaires percevant la rente et la "
         "classe stérile ne créant pas de surplus.",
    'p': "Le partage y est déduit de la théorie de la production : changer "
         "la théorie de la valeur change immédiatement la légitimité des "
         "revenus, ce qui montre que les deux questions ne sont pas "
         "séparables dans la pensée classique."},
   {'f': "Le taux de marge atteint environ 32 % en 2022 ; il mesure la part "
         "de la valeur ajoutée restant après rémunération des salariés, "
         "cotisations sociales et impôts de production.",
    'p': "La répartition primaire est directement observable, et son niveau "
         "détermine l’excédent brut d’exploitation disponible pour les "
         "intérêts, l’impôt, les dividendes et l’autofinancement."},
   {'f': "Le cours calcule que le rapport des écarts de niveau de vie passe "
         "de 18 avant redistribution à 4 après, 53 % des ménages étant "
         "bénéficiaires nets, les plus modestes voyant leur niveau de vie "
         "multiplié par quatre.",
    'p': "La répartition secondaire modifie massivement le résultat de la "
         "répartition primaire : le partage n’est donc pas une donnée "
         "technique mais le produit conjoint du marché et de la décision "
         "publique."},
   {'f': "Le cours note explicitement qu’il n’y a plus de classes sociales "
         "dans la microéconomie, le consommateur se définissant par ses "
         "préférences et par les ressources dont il dispose.",
    'p': "La question de la répartition ne disparaît pas des faits mais du "
         "cadre d’analyse : elle devient une différence de dotation "
         "initiale, ce qui en fait un paramètre et non un objet à "
         "expliquer."}],
  [{'q': "Peut-on analyser la production indépendamment de la "
         "répartition ?",
    'f': "Le cours montre que la réponse a changé deux fois. Chez Quesnay, "
         "Ricardo et Marx, les deux questions sont inséparables : le "
         "produit net circule entre classes, la répartition entre rente, "
         "profit et salaire commande la dynamique, et la plus-value fonde "
         "le profit. Chez les néoclassiques, la séparation devient "
         "possible : on part des choix individuels et de la formation des "
         "prix, et le critère de Pareto permet d’évaluer l’efficacité sans "
         "juger la distribution. Mais le cours souligne le coût de cette "
         "séparation : ce critère ne dit rien sur l’égalité ni sur la "
         "morale.",
    'r': "Ce plan est rigoureux parce qu’il traite la séparation comme une "
         "opération théorique datée, dont le cours indique à la fois le "
         "gain — rigueur formelle, microéconomie opératoire — et la perte — "
         "disparition de la répartition comme objet.",
    'ex': "L’optimum de Pareto, compatible avec une répartition très "
          "inégale puisqu’il ne juge que l’impossibilité d’améliorer sans "
          "nuire."},
   {'q': "La répartition agit-elle sur la croissance ?",
    'f': "Le cours décrit trois canaux. Par l’investissement : le taux de "
         "marge détermine l’excédent brut d’exploitation, donc l’épargne "
         "brute et l’autofinancement, donc la capacité d’investir. Par la "
         "demande : la part salariale détermine le revenu disponible et "
         "donc la consommation, que Keynes place au centre de l’activité. "
         "Par le blocage : chez Ricardo, la hausse des rentes et la baisse "
         "des profits peuvent conduire à l’état stationnaire ; chez Marx, "
         "la hausse de la composition organique fait baisser le taux de "
         "profit et provoque crises et surproduction.",
    'r': "Le raisonnement est solide parce qu’il distingue trois canaux de "
         "sens différents — offre, demande, blocage — tous documentés dans "
         "le cours, ce qui permet de conclure que l’effet net dépend de la "
         "configuration et non d’une loi générale.",
    'ex': "Le taux de marge de 32 % en 2022, qui conditionne "
          "l’autofinancement des entreprises."},
   {'q': "Faut-il produire plus ou partager autrement ?",
    'f': "Le cours interdit de traiter l’alternative comme exclusive. D’un "
         "côté, la croissance est présentée comme la condition du "
         "développement et de la réduction de la pauvreté, et la "
         "redistribution dépend de recettes fiscales qui dépendent de "
         "l’activité. De l’autre, la phase descendante de la courbe de "
         "Kuznets repose « surtout » sur le développement de la "
         "redistribution, la hausse des recettes fiscales et les politiques "
         "sociales : les inégalités sont aussi un choix de société. "
         "Produire plus finance le partage, mais ne le réalise pas.",
    'r': "Ce plan est le plus rigoureux disponible parce qu’il s’appuie sur "
         "la hiérarchisation que le cours opère lui-même dans les "
         "mécanismes de Kuznets, où les facteurs politiques l’emportent sur "
         "les facteurs structurels.",
    'ex': "Le passage d’un rapport de 18 à 4 entre niveaux de vie extrêmes "
          "grâce à la redistribution."}],
  voisins=['n26-salaire-cout-revenu', 'n26-efficacite-justice',
           'n27-repartition', 'n26-marche-etat', 'n27-inegalites'])
