# -*- coding: utf-8 -*-
"""Ensemble 5 — Le marché, les prix et la concurrence (1/3)."""

from doss_base import d

d('n5-marche', 5, "Marché",
  "Un lieu de rencontre de l’offre et de la demande, coordonné par le prix",
  "Le marché désigne le lieu, réel ou abstrait, où se rencontrent une offre et "
  "une demande et où se forme un prix. Dans l’analyse néoclassique que le "
  "cours restitue, le prix y joue le rôle central de coordination des "
  "décisions individuelles : il transmet l’information sur la rareté et "
  "conduit les agents à ajuster spontanément leurs comportements, sans "
  "autorité centrale.",
  "Le marché doit être compris comme un dispositif de coordination, et non "
  "comme un simple lieu d’échange : c’est ce déplacement qui donne au concept "
  "sa portée théorique. Le mécanisme est simple et le cours l’énonce "
  "précisément : si la demande est supérieure à l’offre, le prix augmente ; si "
  "l’offre est supérieure à la demande, le prix diminue. Les variations de "
  "prix incitent alors les producteurs à ajuster leur production et les "
  "consommateurs à modifier leurs achats, de sorte que le marché tend "
  "progressivement vers un prix d’équilibre, celui pour lequel offre et "
  "demande se rencontrent. Chez Walras, ce mécanisme est représenté par "
  "l’image du commissaire-priseur, qui ajuste les prix jusqu’à l’équilibre — "
  "image à rapprocher de la main invisible de Smith, puisque dans les deux cas "
  "la coordination s’obtient sans ordre donné. Une fois l’équilibre atteint, "
  "le marché crée des gains à l’échange, mesurés par la somme du surplus du "
  "consommateur et du surplus du producteur : pour les néoclassiques, "
  "l’échange marchand est donc fondamentalement mutuellement avantageux, même "
  "si certains individus peuvent être exclus lorsque le prix est trop élevé. "
  "Cette efficacité n’est toutefois établie que sous conditions, celles de la "
  "concurrence pure et parfaite, et le cours consacre l’essentiel de son "
  "analyse à ce qui se passe lorsqu’elles ne sont pas réunies. Deux familles "
  "de difficultés apparaissent. Les défaillances de marché, c’est-à-dire les "
  "situations où le marché concurrentiel n’arrive pas à allouer de façon "
  "optimale les ressources — on produit trop ou pas assez, trop cher ou pas "
  "assez cher — et qui comprennent le monopole naturel, les biens collectifs "
  "et communs, les externalités et l’asymétrie d’information. Et la "
  "concurrence imparfaite, où certaines entreprises acquièrent un pouvoir de "
  "marché. Le marché n’est donc jamais, dans le cours, ni un mécanisme "
  "infaillible ni un mécanisme condamné : c’est un dispositif dont "
  "l’efficacité dépend de conditions identifiables.",
  [("La formation du prix par confrontation",
    "L’offre et la demande se rencontrent : un excès de demande fait monter "
    "le prix, un excès d’offre le fait baisser, et le mouvement se poursuit "
    "jusqu’à ce que les quantités offertes et demandées coïncident."),
   ("La transmission de l’information par le prix",
    "Le prix résume une information dispersée sur la rareté et les "
    "préférences : aucun agent n’a besoin de connaître l’ensemble du système, "
    "il lui suffit de réagir au prix pour que ses décisions s’accordent à "
    "celles des autres."),
   ("L’ajustement des comportements",
    "Les variations de prix incitent les producteurs à ajuster leur "
    "production et les consommateurs à modifier leurs achats : la "
    "coordination est obtenue par la réaction décentralisée des agents et non "
    "par une instruction."),
   ("La création de gains à l’échange",
    "À l’équilibre, le consommateur paie moins que ce qu’il était prêt à "
    "payer et le producteur reçoit plus que son prix minimal : la somme des "
    "deux surplus mesure le gain total que l’échange procure à la "
    "collectivité."),
   ("La dépendance à des conditions",
    "L’efficacité de ce dispositif suppose les hypothèses de la concurrence "
    "pure et parfaite ; dès qu’elles sont levées, des défaillances "
    "apparaissent et l’allocation obtenue n’est plus optimale.")],
  [{'a': "Le marché coordonne une multitude de décisions sans qu’aucune "
         "autorité ne détienne l’information nécessaire pour les planifier.",
    'cond': "La coordination suppose que les prix soient libres et qu’ils "
            "reflètent effectivement la rareté, donc l’absence de pouvoir de "
            "marché significatif.",
    'lim': "Dès qu’une entreprise devient price maker, le prix cesse de "
           "transmettre une information fiable et devient l’instrument d’une "
           "stratégie."},
   {'a': "Il produit des gains mutuels, mesurables par la somme du surplus du "
         "consommateur et du surplus du producteur.",
    'cond': "Le gain n’est mutuel que pour ceux qui participent effectivement "
            "à l’échange au prix formé.",
    'lim': "Le cours le souligne explicitement : certains individus peuvent "
           "être exclus lorsque le prix est trop élevé, et le surplus ne dit "
           "rien de cette exclusion."},
   {'a': "Il incite en permanence à l’ajustement, puisque tout écart entre "
         "offre et demande se traduit immédiatement par une variation de "
         "prix.",
    'cond': "L’ajustement suppose la flexibilité des prix et la mobilité des "
            "facteurs, afin que les ressources puissent se redéployer.",
    'lim': "La mobilité est souvent imparfaite : les diplômes ne sont pas "
           "toujours reconnus d’un pays à l’autre et les travailleurs ne "
           "changent pas instantanément de secteur."},
   {'a': "Il fournit un critère d’évaluation clair : l’allocation est efficace "
         "lorsque le prix égale le coût marginal.",
    'cond': "Le critère n’est atteint qu’en concurrence pure et parfaite, où "
            "la demande adressée à la firme est parfaitement élastique.",
    'lim': "Toute structure de marché qui empêche l’égalité entre prix et coût "
           "marginal conduit à une allocation sous-optimale, ce qui est le cas "
           "général plutôt que l’exception."}],
  [{'t': "L’équilibre général existe bien, mais seulement sous un ensemble "
         "d’hypothèses que rien ne vérifie dans la réalité.",
    'qui': "Kenneth Arrow et Gérard Debreu, dont le cours détaille les sept "
           "conditions.",
    'rep': "La critique est interne au modèle et d’autant plus forte : parmi "
           "ces conditions figure la dotation de survie, qui suppose une "
           "intervention extérieure au marché et contredit donc l’idée que le "
           "marché se suffit à lui-même."},
   {'t': "Même si l’équilibre existe, rien ne garantit que le système y "
         "parvienne, ni qu’il y demeure une fois atteint.",
    'qui': "Hugo Sonnenschein, Rolf Mantel et Gérard Debreu.",
    'rep': "Leur résultat est dévastateur pour l’idée d’autorégulation : une "
           "fonction de demande globale peut avoir n’importe quelle forme, de "
           "sorte que la microéconomie propre ne garantit pas une "
           "macroéconomie propre."},
   {'t': "Les agents réels ne se comportent pas comme le modèle l’exige, "
         "faute de capacités de calcul suffisantes.",
    'qui': "Herbert Simon, avec la rationalité limitée.",
    'rep': "Le cours en fait le coup de grâce : même si les conditions "
           "mathématiques étaient remplies, les agents recherchent des "
           "solutions satisfaisantes plutôt qu’optimales, ce qui rend le "
           "modèle élégant mais psychologiquement fragile."},
   {'t': "La coordination par le marché est souvent remplacée, dans le "
         "capitalisme réel, par la coordination administrative des grandes "
         "firmes.",
    'qui': "Alfred Chandler, avec la main visible des managers.",
    'rep': "Son constat est net : la main visible de la gestion remplace la "
           "main invisible des forces du marché dans la coordination des flux "
           "de marchandises, ce qui limite le domaine effectif du marché."}],
  [{'n': "Adam Smith",
    'i': "La poursuite des intérêts individuels conduit, par la main "
         "invisible, à un résultat collectivement favorable.",
    'p': "Le cours l’oppose explicitement à la main visible du monarque chez "
         "Colbert : là où le mercantilisme suppose l’intervention de l’État "
         "quand l’initiative privée est défaillante, Smith soutient que la "
         "coordination s’obtient sans ordre donné."},
   {'n': "Léon Walras",
    'i': "Le prix s’ajuste jusqu’à l’équilibre, comme sous l’effet d’un "
         "commissaire-priseur.",
    'p': "Le cours relève que l’image du commissaire-priseur remplit la même "
         "fonction que la main invisible, mais il en signale aussi le point "
         "faible : Walras suppose implicitement que les courbes d’offre et de "
         "demande se rencontrent toujours, ce que rien ne garantit."},
   {'n': "Vilfredo Pareto",
    'i': "Une situation est optimale lorsqu’on ne peut améliorer le sort de "
         "l’un sans détériorer celui d’un autre.",
    'p': "Son critère formalise l’optimalité de l’équilibre walrassien, mais "
         "le cours insiste sur sa portée limitée : c’est un critère "
         "d’efficacité et non de justice, qui ne dit rien sur l’égalité."},
   {'n': "Arthur Pigou",
    'i': "Il existe des situations où le marché est défaillant, et l’État est "
         "alors légitime pour intervenir.",
    'p': "Le cours le présente comme successeur de Marshall et rival de "
         "Keynes, libéral mais fondateur de l’économie du bien-être : "
         "analyser le bien-être consiste à chercher la situation qui maximise "
         "l’utilité collective, ce qui justifie l’intervention en cas de "
         "défaillance."}],
  [{'f': "Le cours énonce le mécanisme d’ajustement : si la demande est "
         "supérieure à l’offre le prix augmente, si l’offre est supérieure à "
         "la demande le prix diminue.",
    'p': "La formulation est la base de tout raisonnement microéconomique et "
         "montre que le prix est à la fois un résultat de l’échange et son "
         "instrument de coordination."},
   {'f': "Une défaillance de marché est une situation dans laquelle le marché "
         "concurrentiel n’arrive pas à allouer de façon optimale les "
         "ressources : on produit trop ou pas assez, trop cher ou pas assez "
         "cher.",
    'p': "La définition du cours est précieuse car elle couvre les deux sens "
         "de l’inefficacité, en quantité et en prix, et ne se réduit pas à "
         "l’idée de pénurie."},
   {'f': "Le cours recense quatre situations de défaillance : monopole "
         "naturel, biens collectifs et biens communs, externalités, asymétrie "
         "d’information.",
    'p': "L’énumération est la carte du chapitre : chaque défaillance a une "
         "cause distincte et appelle des remèdes différents."},
   {'f': "Le cours distingue deux problèmes en économie : les défaillances et "
         "la concurrence imparfaite.",
    'p': "La distinction est utile : la première porte sur la nature des biens "
         "ou de l’information, la seconde sur la structure du marché, et elles "
         "ne se confondent pas."}],
  [{'q': "Sujet du type « Le marché est-il un mode de coordination "
         "efficace ? »",
    'f': "Le marché coordonne par le prix : si la demande est supérieure à "
         "l’offre le prix augmente, si l’offre est supérieure à la demande il "
         "diminue, et ces variations incitent producteurs et consommateurs à "
         "ajuster leurs décisions jusqu’au prix d’équilibre. Cette "
         "coordination produit des gains à l’échange, mesurés par la somme du "
         "surplus du consommateur et du surplus du producteur. Mais son "
         "efficacité suppose les hypothèses de la concurrence pure et "
         "parfaite, et le cours recense quatre situations où le marché échoue "
         "à allouer les ressources de façon optimale.",
    'r': "Le raisonnement ne tranche pas en faveur ou contre le marché mais en "
         "délimite le domaine de validité, ce qui est la seule manière "
         "rigoureuse de traiter la question.",
    'ex': "L’image du commissaire-priseur chez Walras, qui ajuste les prix "
          "jusqu’à l’équilibre."},
   {'q': "Sujet du type « L’équilibre de marché est-il une réalité ou une "
         "construction théorique ? »",
    'f': "Trois critiques successives, que le cours présente comme une "
         "superposition, ruinent l’idée d’un équilibre réalisé. Arrow et "
         "Debreu montrent que l’équilibre existe mais sous des hypothèses "
         "irréalistes. Sonnenschein, Mantel et Debreu montrent que même s’il "
         "existe, rien ne garantit qu’on y parvienne ni qu’on y reste. Simon "
         "ajoute que même si les conditions mathématiques étaient remplies, "
         "les agents réels n’en sont pas capables. On obtient un équilibre "
         "théoriquement possible, pratiquement inaccessible et "
         "mathématiquement instable.",
    'r': "L’empilement des trois critiques est plus fort que chacune prise "
         "isolément, car elles portent sur l’existence, la stabilité et la "
         "plausibilité comportementale, soit les trois piliers du modèle.",
    'ex': "La dotation de survie dans les conditions d’Arrow-Debreu, qui "
          "suppose une intervention extérieure au marché — État, Église, "
          "institutions — et contredit l’idée que le marché se suffit à "
          "lui-même."},
   {'q': "Sujet du type « L’intervention de l’État sur les marchés est-elle "
         "justifiée ? »",
    'f': "La justification la plus solide ne vient pas d’une préférence "
         "doctrinale mais de l’analyse des défaillances. Pigou, libéral et "
         "fondateur de l’économie du bien-être, soutient qu’il existe des "
         "situations dans lesquelles le marché est défaillant et où l’État est "
         "alors légitime pour intervenir. Le cours en recense quatre : "
         "monopole naturel, biens collectifs et communs, externalités, "
         "asymétrie d’information.",
    'r': "Le raisonnement fonde l’intervention sur un critère d’efficacité "
         "interne à la théorie du marché, ce qui la rend beaucoup plus "
         "difficile à contester qu’un argument d’équité.",
    'ex': "La condition d’efficacité P = Cm, que toute structure de marché "
          "imparfaite empêche d’atteindre."}],
  voisins=['n5-coordination', 'n5-equilibre', 'n5-cpp', 'n5-surplus'])


d('n5-coordination', 5, "Coordination par les prix",
  "Le prix comme seul signal nécessaire pour accorder des décisions dispersées",
  "La coordination par les prix désigne le mécanisme par lequel les décisions "
  "d’une multitude d’agents indépendants s’accordent sans direction centrale, "
  "sous le seul effet des variations de prix. Le prix devient l’élément "
  "central de coordination des décisions individuelles : il incite les "
  "producteurs à ajuster leur production et les consommateurs à modifier leurs "
  "achats.",
  "La coordination par les prix est le cœur de l’analyse libérale du marché, "
  "et le cours en construit l’intelligence en l’opposant à ses alternatives "
  "historiques et théoriques. Le mécanisme d’abord : les écarts entre offre et "
  "demande se traduisent en mouvements de prix, ces mouvements modifient les "
  "incitations, et les comportements s’ajustent jusqu’à ce que l’écart "
  "disparaisse. Le prix fait donc deux choses à la fois — il informe et il "
  "incite — et c’est cette double fonction qui rend inutile toute "
  "centralisation de l’information. Deux figures expriment cette idée : la "
  "main invisible de Smith, et chez Walras le commissaire-priseur qui ajuste "
  "les prix jusqu’à l’équilibre ; le cours les rapproche explicitement, "
  "puisque dans les deux cas le résultat collectif est obtenu sans qu’il soit "
  "voulu par personne. Trois alternatives permettent de mesurer la portée du "
  "mécanisme. La première est historique : chez Colbert, c’est la main "
  "visible du monarque qui remplace l’initiative privée défaillante, dans une "
  "logique mercantiliste très interventionniste. La deuxième est "
  "organisationnelle et c’est la plus importante pour une copie : Chandler "
  "oppose à la main invisible du marché la main visible des managers, et écrit "
  "que la main visible de la gestion remplaçait la main invisible des forces "
  "du marché dans la coordination des flux de marchandises. Dans la grande "
  "entreprise intégrée, la coordination se fait donc par la hiérarchie et non "
  "par le prix. La troisième est théorique, avec Coase et Williamson : le "
  "recours au marché n’est pas gratuit, il engendre des coûts de transaction — "
  "recherche d’information, négociation, rédaction des contrats, contrôle — "
  "et l’entreprise internalise les activités lorsque ces coûts deviennent "
  "trop élevés. La coordination par les prix n’est donc qu’un mode de "
  "coordination parmi d’autres, dont l’avantage relatif dépend du coût de son "
  "usage.",
  [("Le prix comme information",
    "Le prix résume en un seul nombre l’état de la rareté relative : il "
    "dispense chaque agent de connaître les préférences et les coûts de tous "
    "les autres, ce qui rend la coordination possible malgré la dispersion de "
    "l’information."),
   ("Le prix comme incitation",
    "Une hausse de prix rend la production plus rentable et la consommation "
    "plus coûteuse : le même signal agit simultanément sur les deux côtés du "
    "marché, et dans des sens opposés, ce qui résorbe le déséquilibre."),
   ("L’ajustement décentralisé",
    "Aucun agent ne poursuit l’équilibre : chacun réagit à son propre intérêt, "
    "et l’équilibre est le résultat non intentionnel de ces réactions, ce que "
    "résument la main invisible et l’image du commissaire-priseur."),
   ("Le coût du recours au marché",
    "Coordonner par le prix suppose de rechercher l’information, de négocier, "
    "de rédiger des contrats et de contrôler leur exécution : ces coûts de "
    "transaction sont le prix du mécanisme et peuvent le rendre moins "
    "avantageux qu’une coordination interne."),
   ("La substitution par la hiérarchie",
    "Lorsque les coûts de transaction sont élevés, l’activité est internalisée "
    "dans l’entreprise et coordonnée par des managers : la main visible de la "
    "gestion remplace alors la main invisible des forces du marché.")],
  [{'a': "La coordination par les prix économise l’information : nul besoin "
         "d’un centre qui connaisse les préférences et les coûts de tous.",
    'cond': "Elle suppose des prix libres et significatifs, donc l’absence de "
            "pouvoir de marché et une information suffisamment partagée.",
    'lim': "En cas d’asymétrie d’information, le prix cesse d’informer "
           "correctement : Akerlof montre que l’acheteur propose alors un prix "
           "moyen qui chasse les bons produits du marché."},
   {'a': "Elle incite en permanence à l’ajustement, puisque tout déséquilibre "
         "se traduit en opportunité de profit ou en coût supplémentaire.",
    'cond': "L’ajustement suppose la flexibilité des prix et la mobilité des "
            "facteurs, afin que les ressources puissent effectivement se "
            "redéployer.",
    'lim': "Ces deux conditions sont souvent absentes, et le cours relève que "
           "les rigidités de mobilité ralentissent l’ajustement des marchés."},
   {'a': "Elle produit un résultat collectif sans l’avoir visé, ce qui la rend "
         "robuste à la diversité des intentions individuelles.",
    'cond': "Le résultat n’est favorable que si les intérêts individuels "
            "coïncident avec l’intérêt collectif, ce qui suppose l’absence "
            "d’externalités.",
    'lim': "Hardin montre l’inverse dans le cas des communs : ce qui est "
           "rationnel individuellement peut être catastrophique "
           "collectivement."},
   {'a': "Elle fournit un étalon de comparaison pour évaluer les autres modes "
         "de coordination, hiérarchie ou règle publique.",
    'cond': "La comparaison est pertinente si l’on prend en compte les coûts "
            "propres à chaque mode, et non seulement ses résultats.",
    'lim': "Coase montre que le marché n’est pas gratuit : la comparaison doit "
           "intégrer les coûts de transaction, qui sont souvent décisifs."}],
  [{'t': "La coordination par le marché est largement remplacée, dans le "
         "capitalisme contemporain, par la coordination administrative des "
         "grandes firmes.",
    'qui': "Alfred Chandler, avec la main visible des managers.",
    'rep': "Le constat est documenté : la grande entreprise intégrée est "
           "efficiente par les économies d’échelle et la division du travail, "
           "et les managers coordonnent directement l’activité en dehors du "
           "marché."},
   {'t': "Le recours au marché a un coût, ce qui explique que les entreprises "
         "internalisent certaines activités.",
    'qui': "Ronald Coase et Oliver Williamson, avec les coûts de transaction.",
    'rep': "L’argument ne nie pas l’efficacité des prix mais la relativise : "
           "le choix entre marché et organisation devient un arbitrage entre "
           "deux coûts, celui de la transaction et celui de l’organisation."},
   {'t': "L’État doit prendre en charge la coordination lorsque l’initiative "
         "privée se révèle insuffisante ou défaillante.",
    'qui': "La logique mercantiliste que le cours illustre par Colbert, "
           "créateur de manufactures royales comme Saint-Gobain et Sèvres.",
    'rep': "La position est historiquement située et le cours en rappelle les "
           "critiques : Colbert a négligé l’agriculture et n’a pas réussi à "
           "rendre prospère la Compagnie des Indes orientales."},
   {'t': "Le prix ne peut pas coordonner ce qui n’a pas de prix, et laisse "
         "donc hors du calcul des effets bien réels.",
    'qui': "L’analyse des externalités, qui définit celles-ci comme des "
           "répercussions ne passant pas par le marché.",
    'rep': "L’objection délimite précisément le domaine du mécanisme : la "
           "coordination par les prix échoue là où l’effet d’une décision sur "
           "autrui n’est pas tarifé, ce qui justifie la correction "
           "pigouvienne."}],
  [{'n': "Adam Smith",
    'i': "La coordination des décisions s’obtient sans ordre donné, par la "
         "main invisible.",
    'p': "Le cours l’oppose directement à Colbert, pour qui la main visible du "
         "monarque remplace l’initiative privée défaillante. Smith relie par "
         "ailleurs la richesse à la division du travail, elle-même "
         "conditionnée par la taille du marché."},
   {'n': "Léon Walras",
    'i': "L’ajustement des prix conduit à l’équilibre, comme sous l’effet d’un "
         "commissaire-priseur.",
    'p': "Le cours précise que cette figure joue le même rôle que la main "
         "invisible : elle rend intelligible un ajustement sans autorité. Mais "
         "il en relève la fragilité, puisque rien ne garantit que les courbes "
         "d’offre et de demande se croisent."},
   {'n': "Alfred Chandler",
    'i': "La main visible de la gestion remplace la main invisible des forces "
         "du marché dans la coordination des flux de marchandises.",
    'p': "Sa formule, que le cours cite textuellement, décrit une substitution "
         "historique : la grande entreprise intégrée verticalement et "
         "horizontalement coordonne par la hiérarchie, grâce aux managers, ce "
         "que le marché coordonnait par les prix."},
   {'n': "Ronald Coase",
    'i': "Le marché n’est pas gratuit : son fonctionnement engendre des coûts "
         "de transaction.",
    'p': "Il les énumère : recherche d’information, négociation, rédaction des "
         "contrats, contrôle et surveillance. C’est le niveau de ces coûts qui "
         "détermine si la coordination par les prix est préférable à la "
         "coordination interne."}],
  [{'f': "Le cours énonce que le prix devient l’élément central de "
         "coordination des décisions individuelles.",
    'p': "La formule désigne la fonction théorique du prix, qui n’est pas "
         "seulement d’enregistrer une valeur mais d’orienter des décisions "
         "indépendantes."},
   {'f': "Chandler écrit que la main visible de la gestion remplaçait la main "
         "invisible des forces du marché dans la coordination des flux de "
         "marchandises.",
    'p': "La citation est le contre-argument le plus précis à la thèse de la "
         "coordination par les prix, et elle est empirique plutôt que "
         "théorique."},
   {'f': "Colbert crée des manufactures royales comme Saint-Gobain pour le "
         "verre et Sèvres pour la porcelaine, et supprime les droits de douane "
         "entre les villes du pays tout en menant un protectionnisme sélectif "
         "à l’extérieur.",
    'p': "L’exemple montre que la coordination administrative n’est pas une "
         "invention contemporaine et qu’elle a pu viser explicitement "
         "l’exportation et l’attraction des capitaux."},
   {'f': "Williamson montre que certaines entreprises internalisent des "
         "activités afin de réduire les coûts de transaction.",
    'p': "Le fait établit que la frontière entre marché et organisation est "
         "mobile et déterminée économiquement, et non donnée une fois pour "
         "toutes."}],
  [{'q': "Sujet du type « Le marché est-il le seul mode de coordination "
         "économique ? »",
    'f': "Le cours en identifie trois, et leur comparaison structure toute "
         "l’analyse. Le marché coordonne par les prix, le prix devenant "
         "l’élément central d’ajustement des décisions individuelles. "
         "L’entreprise coordonne par la hiérarchie, et Chandler oppose à la "
         "main invisible du marché la main visible des managers. L’État "
         "coordonne par la règle, selon une logique que le cours illustre par "
         "Colbert. Le choix entre marché et organisation dépend, chez Coase et "
         "Williamson, du niveau des coûts de transaction.",
    'r': "Le raisonnement remplace une opposition binaire par une typologie à "
         "trois termes assortie d’un critère de choix, ce qui permet de "
         "conclure sans préférence doctrinale.",
    'ex': "L’internalisation d’activités par certaines entreprises afin de "
          "réduire les coûts de recours au marché."},
   {'q': "Sujet du type « Les prix transmettent-ils une information fiable ? »",
    'f': "La fonction informationnelle du prix est la condition de la "
         "coordination, mais elle n’est pas garantie. Akerlof montre en 1970, "
         "sur le marché des voitures d’occasion, que lorsque le vendeur sait "
         "si sa voiture est bonne et que l’acheteur ne le sait pas, celui-ci "
         "propose un prix moyen : ce prix est trop bas pour les bonnes "
         "voitures, leurs vendeurs quittent le marché, la qualité moyenne "
         "baisse, la confiance disparaît et le marché peut s’effondrer.",
    'r': "Le raisonnement montre que le prix peut non seulement mal informer "
         "mais détruire le marché qu’il devait coordonner, ce qui est bien "
         "plus fort qu’une simple imperfection.",
    'ex': "Le marché des voitures d’occasion analysé par Akerlof dans The "
          "Market for Lemons."}],
  voisins=['n5-marche', 'n5-equilibre', 'n5-offre-demande', 'n5-cpp'])


d('n5-offre-demande', 5, "Offre et demande",
  "Les deux comportements dont la confrontation forme le prix",
  "L’offre désigne la quantité d’un bien que les producteurs sont disposés à "
  "vendre à chaque niveau de prix, la demande la quantité que les "
  "consommateurs sont disposés à acheter. Leur confrontation détermine le prix "
  "et la quantité échangée : l’offre augmente avec le prix, la demande "
  "diminue lorsque le prix s’élève, et l’écart entre les deux commande le "
  "mouvement du prix.",
  "L’offre et la demande forment le couple analytique de base, mais le cours "
  "en propose une lecture plus riche qu’une simple intersection de courbes, et "
  "c’est cette richesse qu’il faut mobiliser. Premier point, le sens des "
  "pentes : du côté de la demande, un prix plus élevé réduit la quantité "
  "demandée, puisque le consommateur arbitre sous contrainte de budget ; du "
  "côté de l’offre, un prix plus élevé rend la production plus rentable et "
  "l’augmente. Deuxième point, le rôle du prix comme variable d’ajustement : "
  "si la demande excède l’offre, le prix monte ; dans le cas inverse, il "
  "baisse. Troisième point, décisif en dissertation, l’élasticité. Une demande "
  "peu élastique signifie que le consommateur ne renonce pas facilement à "
  "l’achat lorsque le prix augmente, une demande très élastique qu’il y "
  "renonce vite. Cette notion commande toute l’analyse du pouvoir de marché : "
  "si la demande est peu élastique, l’entreprise peut augmenter son prix ; si "
  "elle est très élastique, elle doit le maintenir bas. En concurrence pure et "
  "parfaite, la demande adressée à la firme est parfaitement élastique, ce qui "
  "la rend price taker ; en monopole, la firme fait face à une demande "
  "décroissante, ce qui lui permet de fixer son prix. Quatrième point, les "
  "limites du cadre. Le modèle standard raisonne toutes choses égales par "
  "ailleurs, en mettant un marché au microscope, mais les marchés sont "
  "interdépendants : les biens sont liés en substituts ou compléments, les "
  "revenus changent, les entreprises réagissent, de sorte qu’un choc sur un "
  "marché se propage. Le cours ajoute une critique plus profonde encore : "
  "Sonnenschein, Mantel et Debreu montrent qu’une fonction de demande globale "
  "peut avoir n’importe quelle forme, être croissante, être chaotique, et ne "
  "pas réagir normalement aux prix — ce qui interdit de passer sans précaution "
  "de la demande individuelle à la demande de marché.",
  [("La décroissance de la demande avec le prix",
    "Le consommateur arbitre sous contrainte de budget : une hausse de prix "
    "réduit la quantité qu’il peut ou souhaite acquérir, et l’incite à se "
    "reporter sur des substituts."),
   ("La croissance de l’offre avec le prix",
    "Un prix plus élevé rend rentables des unités dont le coût de production "
    "était auparavant prohibitif : l’offre s’étend donc en remontant le long "
    "de la courbe de coût marginal."),
   ("L’ajustement par le prix",
    "L’écart entre les deux quantités détermine le sens du mouvement du prix, "
    "et ce mouvement réduit l’écart : le système comporte donc un mécanisme de "
    "rappel vers le point de rencontre."),
   ("L’élasticité comme mesure de la sensibilité",
    "L’élasticité-prix indique de combien la quantité varie quand le prix "
    "varie : elle détermine qui supporte une hausse de prix et quelle marge de "
    "manœuvre une entreprise possède pour l’imposer."),
   ("L’interdépendance des marchés",
    "Les biens sont substituts ou compléments, les revenus et les décisions "
    "des entreprises varient : un choc sur un marché se propage aux autres, ce "
    "qui limite la portée du raisonnement toutes choses égales par ailleurs.")],
  [{'a': "Le couple offre-demande fournit un modèle minimal mais prédictif : "
         "il permet de déduire le sens de variation du prix et de la quantité "
         "à partir d’un choc identifié.",
    'cond': "La prédiction suppose que l’on sache quelle courbe se déplace, ce "
            "qui exige de distinguer un mouvement le long de la courbe d’un "
            "déplacement de la courbe.",
    'lim': "La démarche raisonne toutes choses égales par ailleurs, alors que "
           "les marchés sont interdépendants et qu’un choc se propage aux "
           "autres marchés."},
   {'a': "L’élasticité transforme un schéma qualitatif en instrument "
         "d’analyse quantitative des comportements et des stratégies.",
    'cond': "Elle n’est informative que si elle est estimée pour le bien et la "
            "période considérés, car elle varie fortement d’un cas à l’autre.",
    'lim': "Elle dépend elle-même des stratégies des entreprises, puisque la "
           "différenciation des produits réduit l’élasticité-prix de la "
           "demande."},
   {'a': "Le cadre éclaire la répartition des gains de l’échange, puisque le "
         "surplus de chaque côté dépend de la forme des deux courbes.",
    'cond': "La lecture en surplus suppose que les courbes représentent "
            "fidèlement les dispositions à payer et les coûts.",
    'lim': "Le surplus ignore ceux qui n’échangent pas : le cours rappelle que "
           "certains individus peuvent être exclus lorsque le prix est trop "
           "élevé."},
   {'a': "Le cadre se généralise à tous les marchés, ce qui en fait l’outil de "
         "base de l’analyse économique, du marché des biens à celui du travail "
         "ou des changes.",
    'cond': "La généralisation suppose que les mécanismes de formation du prix "
            "soient comparables d’un marché à l’autre.",
    'lim': "Sonnenschein, Mantel et Debreu montrent qu’une fonction de demande "
           "globale peut avoir n’importe quelle forme, être croissante ou "
           "chaotique, ce qui interdit l’agrégation naïve."}],
  [{'t': "On ne peut pas passer de la demande individuelle à la demande de "
         "marché sans précaution.",
    'qui': "Hugo Sonnenschein, Rolf Mantel et Gérard Debreu.",
    'rep': "Le résultat est solide et le cours le juge très fort, puisqu’il "
           "détruit l’idée que le marché se régule tout seul : même si chaque "
           "agent est rationnel, l’ensemble du système peut devenir "
           "imprévisible."},
   {'t': "Le raisonnement toutes choses égales par ailleurs est trompeur, car "
         "les marchés ne sont pas séparés.",
    'qui': "La critique de l’équilibre partiel que le cours formule "
           "explicitement.",
    'rep': "La démarche reste légitime comme simplification scientifique — on "
           "met un marché au microscope pour comprendre un mécanisme précis — "
           "à condition de ne pas en conclure qu’un choc reste localisé."},
   {'t': "L’hypothèse de non-satiété du consommateur, qui fonde la "
         "décroissance de la demande, n’a aucun fondement empirique.",
    'qui': "Kate Raworth, dont le cours rapporte la critique de la "
           "surconsommation et de la croissance infinie.",
    'rep': "La critique est pertinente, mais l’hypothèse est indispensable "
           "mathématiquement : sans elle, les courbes d’indifférence peuvent "
           "devenir discontinues ou mal ordonnées."},
   {'t': "La demande ne dépend pas seulement du prix mais de la position "
         "sociale et du désir de distinction.",
    'qui': "Thorstein Veblen, dont le cours expose la consommation "
           "ostentatoire et l’imitation sociale.",
    'rep': "L’objection élargit la fonction de demande sans la détruire : elle "
           "montre que le prix peut lui-même être un signal de prestige, de "
           "sorte que la relation entre prix et quantité n’est pas toujours "
           "décroissante."}],
  [{'n': "Léon Walras",
    'i': "Le prix s’ajuste jusqu’à ce que l’offre et la demande se rencontrent "
         "sur tous les marchés simultanément.",
    'p': "Le cours relève son point faible : il suppose implicitement que "
         "l’offre et la demande se rencontrent toujours, alors qu’on peut "
         "avoir une offre toujours au-dessus de la demande, et donc aucun prix "
         "d’équilibre possible."},
   {'n': "Hugo Sonnenschein",
    'i': "Une fonction de demande globale peut prendre n’importe quelle forme, "
         "même croissante ou chaotique.",
    'p': "Avec Mantel et Debreu, il établit que la microéconomie propre ne "
         "garantit pas une macroéconomie propre : l’agrégation de "
         "comportements rationnels ne produit pas nécessairement un système "
         "régulier, ce qui ruine la présomption d’autorégulation."},
   {'n': "Edward Chamberlin",
    'i': "La différenciation des produits réduit l’élasticité-prix de la "
         "demande adressée à chaque entreprise.",
    'p': "Le cours illustre le mécanisme par les yaourts : un consommateur "
         "indifférent change facilement de marque, un consommateur attaché à "
         "une marque ne la remplace pas facilement. La marque réduit donc la "
         "substituabilité et confère un pouvoir de marché."},
   {'n': "Herbert Simon",
    'i': "Les agents ne maximisent pas : ils recherchent des solutions "
         "satisfaisantes plutôt qu’optimales.",
    'p': "Sa rationalité limitée affecte directement la construction des "
         "courbes, puisque celles-ci supposent un arbitrage optimal sous "
         "contrainte. Le cours en fait le coup de grâce porté au modèle "
         "standard, mathématiquement élégant mais fragile."}],
  [{'f': "Le cours énonce que si la demande est supérieure à l’offre le prix "
         "augmente, et que si l’offre est supérieure à la demande le prix "
         "diminue.",
    'p': "La règle fixe le sens de l’ajustement et permet de raisonner sur un "
         "choc sans représentation graphique."},
   {'f': "Si la demande est peu élastique, l’entreprise peut augmenter le prix "
         "car le consommateur ne renonce pas facilement ; si elle est très "
         "élastique, elle doit maintenir un prix plus bas.",
    'p': "La formulation du cours fait de l’élasticité la clé du pouvoir de "
         "marché, ce qui relie l’analyse de la demande à celle des structures "
         "de marché."},
   {'f': "En concurrence pure et parfaite la demande adressée à la firme est "
         "parfaitement élastique, alors qu’en monopole la firme fait face à "
         "une demande décroissante.",
    'p': "La différence d’élasticité est ce qui distingue le price taker du "
         "price maker : elle explique pourquoi la structure du marché modifie "
         "le prix pratiqué."},
   {'f': "Le cours rappelle que dans l’économie réelle les biens sont liés, "
         "substituts ou compléments, que les revenus changent et que les "
         "entreprises réagissent, de sorte qu’un choc sur un marché se propage "
         "à d’autres.",
    'p': "Le rappel borne la portée de l’équilibre partiel et justifie le "
         "passage à l’équilibre général, avec ses propres difficultés."}],
  [{'q': "Sujet du type « Comment se forment les prix ? »",
    'f': "Le prix résulte de la confrontation de deux comportements de sens "
         "opposé : la demande décroît avec le prix, l’offre croît avec lui. "
         "Lorsque la demande est supérieure à l’offre le prix augmente, et "
         "lorsque l’offre est supérieure à la demande il diminue, de sorte que "
         "le marché tend vers un prix d’équilibre pour lequel offre et demande "
         "se rencontrent. Chez Walras, ce mécanisme est représenté par le "
         "commissaire-priseur qui ajuste les prix jusqu’à l’équilibre.",
    'r': "Le raisonnement montre que le prix n’est pas fixé par un agent mais "
         "produit par un processus, ce qui permet d’enchaîner sur les cas où "
         "une entreprise devient au contraire capable de le fixer.",
    'ex': "La demande parfaitement élastique adressée à la firme en "
          "concurrence pure et parfaite, qui la rend preneuse de prix."},
   {'q': "Sujet du type « L’élasticité de la demande explique-t-elle les "
         "stratégies des entreprises ? »",
    'f': "L’élasticité détermine la marge de manœuvre de l’entreprise sur son "
         "prix. Si la demande est peu élastique, l’entreprise peut augmenter "
         "son prix car le consommateur ne renonce pas facilement à acheter ; "
         "si elle est très élastique, elle doit maintenir un prix plus bas "
         "pour éviter le renoncement. C’est pourquoi la différenciation est "
         "une stratégie rationnelle : comme le montre Chamberlin, elle réduit "
         "la substituabilité et donc l’élasticité-prix.",
    'r': "Le raisonnement part d’une propriété de la demande pour en déduire "
         "un comportement d’offre, ce qui relie la théorie du consommateur à "
         "celle des structures de marché.",
    'ex': "L’exemple des yaourts : un consommateur attaché à une marque ne "
          "remplacera pas facilement celle-ci par une autre."}],
  voisins=['n5-marche', 'n5-equilibre', 'n5-coordination',
           'n5-concurrence-monopolistique'])


d('n5-equilibre', 5, "Équilibre de marché",
  "Le point où offre et demande se rencontrent — s’il existe, s’il est atteint",
  "L’équilibre de marché est la situation dans laquelle le prix est tel que la "
  "quantité offerte égale la quantité demandée, de sorte qu’aucune force ne "
  "pousse plus le prix à varier. Le cours en fait le point d’aboutissement du "
  "mécanisme d’ajustement par les prix, tout en consacrant une analyse "
  "détaillée aux trois questions qu’il soulève : son existence, sa stabilité "
  "et sa plausibilité.",
  "L’équilibre est le concept que le cours soumet à l’examen le plus exigeant, "
  "et c’est ce qui en fait un excellent sujet de dissertation. Le point de "
  "départ est optimiste : pour Walras, l’économie est fondamentalement stable "
  "et autorégulée, et si tous les marchés sont en équilibre en même temps, "
  "alors la situation est optimale — ce que Pareto formalise par son critère, "
  "une situation étant Pareto-optimale lorsqu’on ne peut améliorer la "
  "situation de quelqu’un sans détériorer celle d’un autre. Vient ensuite la "
  "série des difficultés, que le cours présente comme une superposition de "
  "critiques. Première difficulté, l’existence : Walras suppose implicitement "
  "que l’offre et la demande se rencontrent toujours, mais rien ne garantit "
  "que les deux courbes se coupent ; on peut avoir une offre toujours "
  "au-dessus de la demande, et alors aucun prix d’équilibre n’est possible. "
  "Avoir autant d’équations que d’inconnues ne garantit pas qu’une solution "
  "existe, puisque deux droites peuvent ne jamais se croiser. Arrow et Debreu "
  "répondent à cette question en établissant les conditions d’existence : les "
  "fonctions doivent être continues et bornées, et ils énoncent sept "
  "conditions — rationalité, concurrence pure et parfaite, marchés complets, "
  "dotation de survie, convexité des courbes d’indifférence, et autres. Mais "
  "le cours souligne la contradiction : la dotation de survie suppose une "
  "intervention extérieure au marché, État, Église ou institutions, ce qui "
  "contredit l’idée que le marché se suffit à lui-même. Deuxième difficulté, "
  "la stabilité : Sonnenschein, Mantel et Debreu montrent que même si "
  "l’équilibre existe, il n’y a aucune raison qu’on y arrive, ni aucune raison "
  "qu’on y reste. Troisième difficulté, le comportement : Simon montre que les "
  "agents réels ne sont pas capables de se comporter comme le modèle "
  "l’exige. On obtient donc un équilibre théoriquement possible, pratiquement "
  "inaccessible et mathématiquement instable.",
  [("L’égalisation des quantités",
    "L’équilibre est atteint lorsque la quantité offerte égale la quantité "
    "demandée : à ce prix, aucun agent n’a plus de raison de modifier son "
    "comportement, ce qui définit le repos du système."),
   ("Le mécanisme de rappel",
    "Hors de l’équilibre, l’écart entre offre et demande déclenche un "
    "mouvement de prix qui réduit cet écart : c’est ce mécanisme, et non "
    "l’équilibre lui-même, qui porte l’idée d’autorégulation."),
   ("La condition d’existence",
    "Pour que l’équilibre existe, il faut que les courbes se croisent, donc "
    "que les fonctions d’offre et de demande soient continues — sans saut "
    "brutal — et bornées, c’est-à-dire encadrées entre un minimum et un "
    "maximum."),
   ("L’optimalité au sens de Pareto",
    "À l’équilibre général, on ne peut plus améliorer la situation de "
    "quelqu’un sans détériorer celle d’un autre : l’optimalité est un critère "
    "d’efficacité qui ne dit rien de la justice de la répartition obtenue."),
   ("L’indétermination de la dynamique",
    "L’existence d’un équilibre ne dit rien du chemin qui y mène : la forme de "
    "la demande globale pouvant être quelconque, le système peut ne jamais "
    "converger ni demeurer au point atteint.")],
  [{'a': "L’équilibre fournit un point de référence qui permet de raisonner "
         "sur les écarts : sans lui, on ne saurait pas dire qu’un marché est "
         "en pénurie ou en excès d’offre.",
    'cond': "La référence n’a de sens que si un équilibre existe pour le "
            "marché considéré, ce que les conditions d’Arrow-Debreu "
            "précisent.",
    'lim': "Rien ne garantit l’existence dans le cas général : on peut avoir "
           "une offre toujours au-dessus de la demande, donc aucun prix "
           "d’équilibre possible."},
   {'a': "Il permet de définir rigoureusement l’efficacité, par l’égalité "
         "entre le prix et le coût marginal.",
    'cond': "Cette égalité n’est obtenue qu’en concurrence pure et parfaite, "
            "où la demande adressée à la firme est parfaitement élastique.",
    'lim': "Toute structure qui empêche P = Cm conduit à une allocation "
           "sous-optimale, ce qui fait du cas efficace l’exception plutôt que "
           "la règle."},
   {'a': "Il fournit, avec le critère de Pareto, un langage commun pour "
         "comparer deux situations économiques.",
    'cond': "La comparaison n’est possible que si l’on accepte un critère "
            "purement allocatif, indifférent à la répartition initiale.",
    'lim': "Le cours est explicite : c’est un critère d’efficacité et non de "
           "justice, qui ne dit rien sur l’égalité ni sur la morale."},
   {'a': "L’analyse de ses conditions d’existence a produit un résultat "
         "théorique majeur, en identifiant précisément ce que le modèle "
         "suppose.",
    'cond': "Le résultat vaut dans le cadre mathématique retenu, celui de la "
            "continuité et de la bornitude des fonctions.",
    'lim': "L’une des conditions, la dotation de survie, suppose une "
           "intervention extérieure au marché, ce qui contredit l’idée que le "
           "marché se suffit à lui-même."}],
  [{'t': "L’équilibre existe bien, mais seulement sous un ensemble de "
         "conditions que la réalité ne vérifie jamais toutes.",
    'qui': "Kenneth Arrow et Gérard Debreu, dont le cours détaille les sept "
           "conditions.",
    'rep': "La critique est constructive plutôt que destructrice : elle "
           "convertit une intuition en théorème conditionnel, et c’est "
           "l’examen de chaque condition qui révèle les fragilités."},
   {'t': "Même s’il existe, il n’y a aucune raison que le système y "
         "parvienne, ni aucune raison qu’il y demeure.",
    'qui': "Hugo Sonnenschein, Rolf Mantel et Gérard Debreu.",
    'rep': "L’objection porte sur la dynamique et non sur la statique, et le "
           "cours la juge dévastatrice : elle détruit l’idée que le marché se "
           "régule tout seul, alors même qu’elle admet l’existence de "
           "l’équilibre."},
   {'t': "Les agents réels ne se comportent pas comme le modèle l’exige, "
         "même lorsque ses conditions sont réunies.",
    'qui': "Herbert Simon, avec la rationalité limitée.",
    'rep': "Le cours la présente comme le coup de grâce : le modèle est "
           "mathématiquement élégant et intellectuellement puissant mais "
           "psychologiquement et sociologiquement très fragile."},
   {'t': "La transparence de l’information, que l’équilibre suppose, est "
         "l’exception et non la règle.",
    'qui': "George Akerlof, avec l’asymétrie d’information.",
    'rep': "Le cours insiste : l’asymétrie n’est pas une exception mais la "
           "situation normale des marchés, ce qui déplace l’objection du "
           "registre de l’imperfection vers celui du cas général."}],
  [{'n': "Léon Walras",
    'i': "Si tous les marchés sont en équilibre en même temps, alors la "
         "situation est optimale.",
    'p': "Le cours qualifie sa vision d’optimiste : l’économie y est "
         "fondamentalement stable et autorégulée. Mais il en souligne le point "
         "faible, à savoir l’hypothèse implicite que les courbes d’offre et de "
         "demande se rencontrent toujours."},
   {'n': "Vilfredo Pareto",
    'i': "Une situation est optimale lorsqu’on ne peut améliorer le sort de "
         "quelqu’un sans détériorer celui d’un autre.",
    'p': "Son critère formalise l’optimalité walrassienne, et le cours en "
         "précise la portée exacte : il dit seulement qu’on ne peut plus "
         "améliorer sans coût, et reste muet sur l’égalité et sur la morale."},
   {'n': "Kenneth Arrow",
    'i': "L’existence d’un équilibre général exige que les fonctions soient "
         "continues et bornées, et sept conditions économiques précises.",
    'p': "Avec Debreu, il transforme une intuition en théorème. Le cours "
         "souligne la critique majeure qui en résulte : la dotation de survie "
         "suppose une intervention extérieure au marché, ce qui contredit "
         "l’autosuffisance du marché."},
   {'n': "Gérard Debreu",
    'i': "L’existence de l’équilibre ne garantit ni sa stabilité ni la "
         "convergence du système vers lui.",
    'p': "Le cours lui attribue, avec Sonnenschein et Mantel, ce second "
         "résultat, distinct du premier : la demande globale pouvant prendre "
         "n’importe quelle forme, le système peut devenir imprévisible alors "
         "même que chaque agent est rationnel."}],
  [{'f': "Walras suppose implicitement que l’offre et la demande se "
         "rencontrent toujours, mais rien ne garantit que les deux courbes se "
         "coupent.",
    'p': "L’observation fonde la question de l’existence : sans croisement, "
         "aucun prix d’équilibre n’est possible, et le mécanisme d’ajustement "
         "ne mène nulle part."},
   {'f': "Avoir autant d’équations que d’inconnues ne garantit pas qu’une "
         "solution existe, puisque deux droites peuvent ne jamais se croiser.",
    'p': "L’argument mathématique du cours montre que le problème de "
         "l’existence est réel et non rhétorique, ce qui justifie le travail "
         "d’Arrow et Debreu."},
   {'f': "Parmi les sept conditions d’Arrow-Debreu figure la dotation de "
         "survie, selon laquelle chaque agent possède un minimum de ressources "
         "au départ.",
    'p': "Le cours en tire la critique décisive : cette dotation suppose une "
         "intervention extérieure — État, Église, institutions — ce qui "
         "contredit l’idée néoclassique que le marché se suffit à lui-même."},
   {'f': "Le cours conclut qu’on obtient un équilibre théoriquement possible, "
         "pratiquement inaccessible et mathématiquement instable.",
    'p': "La formule en trois temps résume la superposition des critiques et "
         "fournit une conclusion directement utilisable en dissertation."}],
  [{'q': "Sujet du type « L’économie de marché est-elle autorégulée ? »",
    'f': "L’idée d’autorégulation repose sur l’existence et la stabilité d’un "
         "équilibre, or le cours montre que ni l’une ni l’autre ne sont "
         "acquises. Arrow et Debreu établissent que l’équilibre existe, mais "
         "sous des hypothèses irréalistes, dont la dotation de survie qui "
         "suppose une intervention extérieure au marché. Sonnenschein, Mantel "
         "et Debreu montrent qu’il n’y a aucune raison qu’on y arrive ni qu’on "
         "y reste. On obtient un équilibre théoriquement possible, "
         "pratiquement inaccessible et mathématiquement instable.",
    'r': "Le raisonnement démonte l’autorégulation de l’intérieur, en "
         "mobilisant des résultats produits par la théorie néoclassique "
         "elle-même, ce qui le rend bien plus solide qu’une critique externe.",
    'ex': "La possibilité d’une offre toujours au-dessus de la demande, qui "
          "exclut tout prix d’équilibre."},
   {'q': "Sujet du type « L’efficacité économique suffit-elle à juger une "
         "situation ? »",
    'f': "Le critère de Pareto montre précisément les limites de "
         "l’efficacité comme critère de jugement. Une situation est "
         "Pareto-optimale lorsqu’on ne peut améliorer la situation de "
         "quelqu’un sans détériorer celle d’un autre : c’est un critère "
         "d’efficacité et non de justice, qui ne dit rien sur l’égalité ni sur "
         "la morale et affirme seulement qu’on ne peut plus améliorer sans "
         "coût.",
    'r': "Le raisonnement sépare le jugement d’efficacité du jugement de "
         "justice, ce qui permet de reconnaître la validité du premier tout en "
         "montrant qu’il ne peut tenir lieu du second.",
    'ex': "Une répartition très inégale peut être Pareto-optimale, puisque "
          "toute redistribution y détériorerait la situation de quelqu’un."}],
  voisins=['n5-marche', 'n5-pareto', 'n5-offre-demande', 'n5-cpp'])
