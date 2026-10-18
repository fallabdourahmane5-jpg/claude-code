# -*- coding: utf-8 -*-
"""Ensemble 4 — L’environnement et les limites de la croissance (2/4)."""

from doss_base import d

d('n4-communs', 4, "Biens communs",
  "Rivaux mais non excluables : la catégorie où le marché échoue par le haut",
  "Un bien commun est un bien rival et non excluable : sa consommation par un "
  "individu réduit la quantité disponible pour les autres, mais il est "
  "impossible d’en empêcher l’accès à qui ne paie pas. Cette combinaison le "
  "distingue du bien privé, rival et excluable, du bien de club, non rival et "
  "excluable, et du bien collectif pur, non rival et non excluable.",
  "La notion de bien commun n’a de sens qu’à l’intérieur de la typologie que "
  "le cours construit à partir de deux critères, qu’il faut absolument "
  "distinguer. La rivalité répond à la question : la consommation par un "
  "individu empêche-t-elle celle des autres ? L’excluabilité répond à une "
  "question entièrement différente : peut-on empêcher quelqu’un de consommer "
  "s’il ne paie pas ? Le cinéma et Netflix sont excluables, l’air et "
  "l’éclairage public ne le sont pas. La rivalité concerne la quantité "
  "disponible, l’excluabilité le filtrage de l’accès par le paiement : les "
  "deux notions sont totalement différentes et leur croisement donne quatre "
  "types de biens. Le bien commun occupe la case la plus problématique. "
  "Comme il est rival, l’usage de l’un prive l’autre ; comme il est non "
  "excluable, personne ne peut être écarté. La défaillance qui en résulte "
  "n’est donc pas la même que celle du bien collectif pur. Pour un bien "
  "collectif, non rival et non excluable, la non-excluabilité engendre le "
  "comportement de passager clandestin analysé par Mancur Olson et donc la "
  "sous-production : personne ne veut payer, aucun producteur privé ne peut "
  "rentabiliser, le bien n’existe pas. Pour un bien commun, la même "
  "non-excluabilité produit l’inverse : non pas la sous-production mais la "
  "surexploitation, puisque chacun a intérêt à prélever davantage sur une "
  "ressource dont nul ne peut l’exclure. Le cours résume les deux cas d’une "
  "seule formule : les biens collectifs et les biens communs constituent des "
  "défaillances de marché parce que la non-excluabilité empêche le système de "
  "prix de jouer son rôle, ce qui conduit soit à des comportements de passager "
  "clandestin et à une sous-production, soit à une surexploitation des "
  "ressources. Dernier point, décisif : le statut d’un bien n’est pas figé. Un "
  "bien peut passer de commun à privé ou l’inverse, sous l’effet de la "
  "technologie, des règles institutionnelles ou de décisions politiques.",
  [("Le croisement de la rivalité et de l’excluabilité",
    "Quatre types de biens résultent de deux critères indépendants : privé "
    "(rival, excluable), de club (non rival, excluable), commun (rival, non "
    "excluable) et collectif pur (non rival, non excluable). Toute l’analyse "
    "des défaillances part de ce tableau."),
   ("La non-excluabilité comme cause de la défaillance",
    "Dès qu’on ne peut pas faire payer, le prix cesse de jouer son rôle "
    "d’allocation : le marché ne transmet plus l’information sur la rareté, et "
    "l’allocation devient sous-optimale sans qu’aucun agent se comporte "
    "irrationnellement."),
   ("La surexploitation plutôt que la sous-production",
    "Pour un bien commun, la rivalité transforme la non-excluabilité en "
    "incitation au prélèvement : le gain est individuel, le coût de la "
    "dégradation collectif, d’où une consommation supérieure au niveau "
    "soutenable."),
   ("Le caractère non figé du statut d’un bien",
    "La technologie, les règles institutionnelles et les décisions politiques "
    "peuvent faire passer un bien d’une catégorie à l’autre : l’eau, d’abord "
    "accessible au puits collectif, devient excluable à mesure que la "
    "distribution se perfectionne et s’individualise."),
   ("Le problème spécifique des communs mondiaux",
    "Le climat est un bien commun à l’échelle de la planète : la "
    "non-excluabilité y produit du passager clandestin entre États, du "
    "sous-investissement collectif et une surexploitation des ressources "
    "planétaires, sans autorité capable d’imposer une règle.")],
  [{'a': "La typologie fournit un diagnostic avant tout remède : elle indique "
         "pourquoi le marché échoue et donc quel type d’intervention est "
         "approprié.",
    'cond': "Le diagnostic n’est valable que si l’on classe correctement le "
            "bien, ce qui suppose d’examiner séparément rivalité et "
            "excluabilité.",
    'lim': "Beaucoup de biens réels sont intermédiaires ou changent de "
           "catégorie, de sorte que le classement est souvent moins net que le "
           "tableau ne le suggère."},
   {'a': "Elle distingue deux défaillances que l’on confond souvent, la "
         "sous-production des biens collectifs et la surexploitation des "
         "communs.",
    'cond': "La distinction tient à la rivalité : c’est elle qui transforme la "
            "non-excluabilité en incitation au prélèvement.",
    'lim': "Dans les cas mixtes, les deux défaillances coexistent, comme pour "
           "le climat, à la fois surexploité et sous-protégé par "
           "l’investissement collectif."},
   {'a': "Elle fait apparaître la dimension politique des catégories "
         "économiques, puisque le statut d’un bien dépend aussi de décisions "
         "institutionnelles.",
    'cond': "Cette lecture suppose d’accepter que la nature d’un bien ne soit "
            "pas donnée par ses propriétés physiques seules.",
    'lim': "Rendre un bien excluable n’est pas toujours souhaitable, le cours "
           "soulignant la question de la marchandisation de ressources "
           "vitales."},
   {'a': "Elle donne un cadre pour penser les biens communs mondiaux, dont le "
         "climat est l’exemple le plus important.",
    'cond': "La transposition suppose de traiter les États comme les usagers "
            "d’une ressource partagée, ce que fait explicitement le cours.",
    'lim': "À cette échelle, les solutions habituelles sont inopérantes : le "
           "cours note que les mécanismes d’Ostrom sont plus difficiles à "
           "appliquer aux biens communs mondiaux."}],
  [{'t': "Les communs conduisent nécessairement à la ruine : il faut les "
         "privatiser ou les nationaliser.",
    'qui': "Garrett Hardin, pour qui deux seules solutions existent, "
           "privatiser ou nationaliser.",
    'rep': "Elinor Ostrom montre empiriquement que de nombreuses communautés "
           "gèrent durablement des biens communs sans passer ni par l’État ni "
           "par le marché : la tragédie des communs n’est pas une fatalité."},
   {'t': "Il suffit d’attribuer des droits de propriété clairement définis "
         "pour que le marché règle lui-même le problème d’allocation.",
    'qui': "Ronald Coase, dont le théorème fonde la solution par les droits "
           "échangeables.",
    'rep': "La solution ne vaut que si les coûts de transaction sont faibles "
           "et les droits faciles à définir, conditions absentes pour l’air, "
           "les océans ou le climat."},
   {'t': "Multiplier les droits de propriété sur un commun peut créer un "
         "blocage au lieu d’une allocation efficace.",
    'qui': "Michael Heller, avec la tragédie des anti-communs.",
    'rep': "L’argument est solide : trop de propriété nuit comme trop peu, "
           "puisque chaque usage exige alors royalties et autorisations "
           "multiples, ce qui ralentit et parfois bloque la recherche."}],
  [{'n': "Mancur Olson",
    'i': "Un agent peut consommer un bien sans vouloir participer à son "
         "financement : c’est le passager clandestin.",
    'p': "Le cours illustre le mécanisme par le phare : chaque bateau veut "
         "bénéficier de la lumière, aucun n’a intérêt à payer puisqu’il en "
         "profitera de toute façon, de sorte que personne ne finance, personne "
         "ne produit et le bien n’existe pas."},
   {'n': "Garrett Hardin",
    'i': "Lorsque l’usage est collectif et l’accès libre, les individus "
         "tendent à gaspiller, surexploiter et épuiser la ressource.",
    'p': "Son analyse de 1968 brise l’idée que l’intérêt individuel "
         "conduirait spontanément à l’intérêt général : ici l’intérêt "
         "individuel détruit l’intérêt collectif, car le gain du prélèvement "
         "est privé tandis que le coût de la dégradation est partagé."},
   {'n': "Elinor Ostrom",
    'i': "Les biens communs peuvent être gérés durablement par des "
         "communautés locales capables de créer leurs propres règles.",
    'p': "Première femme à recevoir le prix Nobel d’économie en 2009, elle "
         "s’inscrit dans la nouvelle économie institutionnelle et conteste "
         "l’alternative trop simple entre marché et État : il existe une "
         "troisième voie, la gestion collective par des communautés locales."},
   {'n': "Ronald Coase",
    'i': "Le marché n’est pas gratuit : son fonctionnement engendre des coûts "
         "de transaction.",
    'p': "Il énumère ces coûts — recherche d’information, négociation, "
         "rédaction des contrats, contrôle et surveillance — et en fait la "
         "condition de validité de son théorème : la solution marchande ne "
         "fonctionne que s’ils restent faibles."}],
  [{'f': "Le cours oppose le cinéma et Netflix, excluables faute de paiement, "
         "à l’air et à l’éclairage public, dont on ne peut filtrer l’accès.",
    'p': "Les exemples fixent la distinction décisive : l’excluabilité est une "
         "question technique et institutionnelle de filtrage, non une question "
         "de rareté."},
   {'f': "L’eau est d’abord un bien commun, non excluable au puits et à la "
         "fontaine mais rival, avant de devenir excluable par la distribution "
         "par immeuble puis par l’individualisation des compteurs.",
    'p': "L’exemple démontre que le statut d’un bien dépend de la technologie "
         "disponible : le progrès technique peut créer l’excluabilité, et donc "
         "faire passer un bien d’une catégorie à l’autre."},
   {'f': "Un bien collectif pur, comme la défense nationale, l’éclairage "
         "public, la sécurité ou l’air pur, souffre de sous-production faute "
         "de financement volontaire.",
    'p': "La comparaison avec le bien commun est éclairante : même cause, la "
         "non-excluabilité, mais effets opposés selon que le bien est rival ou "
         "non."},
   {'f': "Le cours cite l’accord signé en 2023 sur la haute mer, qui vise à "
         "protéger la biodiversité marine et à créer des aires marines "
         "protégées.",
    'p': "C’est un exemple concret de protection d’un bien commun mondial, et "
         "il montre que la solution passe par la règle internationale plutôt "
         "que par le prix ou la propriété."}],
  [{'q': "Sujet du type « Le marché permet-il une allocation efficace des "
         "ressources ? »",
    'f': "La typologie des biens délimite précisément le domaine où le marché "
         "fonctionne. Il suppose en effet l’excluabilité, puisque dans une "
         "économie de marché une entreprise ne peut produire que si elle peut "
         "faire payer. Or les biens communs sont rivaux et non excluables : la "
         "non-excluabilité empêche le système de prix de jouer son rôle, ce qui "
         "conduit à une surexploitation des ressources, tandis que pour les "
         "biens collectifs elle conduit à une sous-production.",
    'r': "Le raisonnement ne conteste pas l’efficacité du marché en général "
         "mais en délimite le domaine de validité par deux critères précis, ce "
         "qui est beaucoup plus solide qu’une critique globale.",
    'ex': "Le phare, non rival et non excluable, qu’aucune entreprise privée "
          "n’a intérêt à construire puisque chaque bateau en profitera sans "
          "payer."},
   {'q': "Sujet du type « La propriété est-elle la meilleure protection des "
         "ressources naturelles ? »",
    'f': "La réponse dépend du type de bien et du niveau des coûts de "
         "transaction. Pour une ressource délimitable avec peu d’acteurs, la "
         "solution de Coase fonctionne : des droits clairement définis "
         "permettent la négociation et l’internalisation. Mais le statut d’un "
         "bien n’est pas figé, et rendre un commun excluable est une décision "
         "politique autant que technique, comme le montre l’histoire de la "
         "distribution de l’eau.",
    'r': "Le raisonnement déplace la question de l’efficacité vers "
         "l’appropriabilité : avant de demander si la propriété protège, il "
         "faut demander si elle est techniquement et légitimement possible.",
    'ex': "La forêt amazonienne, qui traverse plusieurs États et que certaines "
          "communautés locales considèrent comme n’appartenant à personne."}],
  voisins=['n4-tragedie', 'n4-gouvernance-communs', 'n4-externalites-env',
           'n4-climat'])


d('n4-tragedie', 4, "Tragédie des communs",
  "Quand ce qui est rationnel pour chacun est catastrophique pour tous",
  "La tragédie des communs désigne le mécanisme par lequel une ressource "
  "rivale et non excluable est surexploitée jusqu’à l’épuisement, parce que "
  "chaque usager retire un gain individuel de son prélèvement tandis que le "
  "coût de la dégradation est partagé par tous. Garrett Hardin la formule en "
  "1968 dans The Tragedy of the Commons.",
  "La tragédie des communs est l’un des rares mécanismes du programme dont la "
  "démonstration tient en trois lignes de raisonnement, et c’est ce qui en "
  "fait un outil si puissant. Un bien commun est rival et non excluable. "
  "Chaque individu raisonne donc ainsi : si j’utilise plus la ressource, j’y "
  "gagne directement ; le coût de la dégradation est partagé par tous. Le gain "
  "est individuel, la perte est collective. Résultat : chacun surexploite, la "
  "ressource est épuisée, une partie de la communauté est appauvrie, l’intérêt "
  "général n’est pas satisfait. La portée théorique de ce résultat dépasse "
  "largement l’écologie. Hardin casse l’idée selon laquelle l’intérêt "
  "individuel conduit spontanément à l’intérêt général : ici c’est l’inverse, "
  "l’intérêt individuel détruit l’intérêt collectif, et il s’agit donc d’une "
  "remise en cause directe de la thèse libérale classique selon laquelle la "
  "somme des intérêts individuels produit l’intérêt collectif. Le cours ajoute "
  "une formalisation précieuse : la tragédie des communs s’explique par le "
  "dilemme du prisonnier. Chaque agriculteur a intérêt à faire paître le "
  "maximum de bêtes parce qu’il ne sait pas ce que feront les autres ; "
  "l’équilibre non coopératif est donc la surexploitation, alors même que tous "
  "préféreraient la modération générale. La coopération serait collectivement "
  "supérieure mais individuellement instable. Il faut enfin savoir distinguer "
  "deux usages du mécanisme. Appliqué à une ressource locale — un pâturage, "
  "une nappe, une pêcherie — il se prête à des solutions identifiables : "
  "réglementation publique par quotas ou interdictions, privatisation par "
  "attribution de droits de propriété, ou gestion collective. Appliqué au "
  "climat, bien commun mondial, il produit du passager clandestin entre États, "
  "du sous-investissement collectif et une surexploitation des ressources "
  "planétaires, sans autorité capable d’imposer la règle.",
  [("La structure du bien : rival et non excluable",
    "Le prélèvement de l’un réduit ce qui reste aux autres, mais nul ne peut "
    "être écarté : les deux propriétés ensemble, et elles seules, engendrent "
    "le mécanisme."),
   ("L’asymétrie entre gain privé et coût collectif",
    "Celui qui prélève capte la totalité du bénéfice de son prélèvement mais "
    "ne supporte qu’une fraction du dommage qu’il cause : son calcul privé le "
    "conduit donc à prélever au-delà du niveau socialement souhaitable."),
   ("Le raisonnement stratégique",
    "Formulé comme un dilemme du prisonnier, le problème devient un problème "
    "d’anticipation : chacun surexploite parce qu’il ne sait pas ce que feront "
    "les autres, et modérer son usage tout seul ne sauverait pas la ressource."),
   ("L’épuisement et l’appauvrissement collectif",
    "La somme des comportements rationnels aboutit à l’épuisement de la "
    "ressource : une partie de la communauté est appauvrie, et l’intérêt "
    "général n’est pas satisfait alors qu’aucun agent ne s’est comporté de "
    "façon irrationnelle."),
   ("La transposition à l’échelle mondiale",
    "Le climat étant un bien commun mondial, l’absence de coordination "
    "internationale produit les mêmes effets entre États : comportements de "
    "passager clandestin, sous-investissement collectif et surexploitation des "
    "ressources planétaires.")],
  [{'a': "Le mécanisme explique la dégradation environnementale sans supposer "
         "d’irrationalité ni de malveillance, ce qui en fait une explication "
         "robuste.",
    'cond': "Il suppose que les usagers soient suffisamment nombreux et "
            "anonymes pour qu’aucun ne supporte une part significative du "
            "dommage.",
    'lim': "Dans une petite communauté où chacun supporte une part notable du "
           "coût et où les comportements sont observables, le mécanisme perd "
           "une grande part de sa force."},
   {'a': "Il réfute la thèse selon laquelle la poursuite des intérêts "
         "individuels suffirait à produire l’intérêt général.",
    'cond': "La réfutation ne vaut que pour la classe de biens concernée, "
            "c’est-à-dire les biens à la fois rivaux et non excluables.",
    'lim': "Elle ne s’étend pas aux biens privés, pour lesquels le mécanisme "
           "de marché conserve ses propriétés d’efficacité."},
   {'a': "Il fournit une grille d’analyse applicable au climat, qui est "
         "l’enjeu environnemental le plus important.",
    'cond': "La transposition suppose de traiter les États comme des usagers "
            "rationnels d’une ressource partagée.",
    'lim': "À l’échelle mondiale, aucune des trois solutions habituelles n’est "
           "directement disponible, faute d’autorité capable de réglementer ou "
           "de définir des droits."},
   {'a': "Il désigne clairement les trois familles de remèdes possibles, ce "
         "qui en fait un point de départ pour la discussion des politiques "
         "publiques.",
    'cond': "Le choix du remède dépend de la nature de la ressource, du nombre "
            "d’usagers et du niveau des coûts de transaction.",
    'lim': "Hardin lui-même n’en retient que deux, privatiser ou nationaliser, "
           "ce qui conduit à sous-estimer la troisième voie."}],
  [{'t': "La tragédie des communs n’est pas une fatalité : des communautés "
         "gèrent durablement des ressources partagées.",
    'qui': "Elinor Ostrom, qui le démontre empiriquement contre Hardin.",
    'rep': "La démonstration est solide — gestion de l’eau en Espagne, "
           "pâturages suisses, forêts japonaises, irrigation en Asie — mais "
           "elle suppose des communautés capables de créer et de faire "
           "respecter leurs propres règles."},
   {'t': "Le problème n’est pas l’absence de propriété mais l’absence de "
         "prix : une taxe suffirait à rétablir l’optimum.",
    'qui': "Arthur Pigou, dont la logique est de corriger les prix pour qu’ils "
           "reflètent le vrai coût social.",
    'rep': "La taxe fonctionne si le dommage est mesurable, ce que le cours "
           "identifie comme la principale difficulté : il faut connaître le "
           "coût externe pour calibrer le prélèvement."},
   {'t': "La solution est l’attribution de droits de propriété échangeables, "
         "car les usagers négocieront eux-mêmes l’usage efficace.",
    'qui': "Ronald Coase, dont le théorème s’applique bien aux ressources "
           "localisées.",
    'rep': "Les conditions sont restrictives : la solution échoue pour les "
           "biens difficiles à délimiter, les acteurs trop nombreux et les "
           "coûts de transaction élevés, soit exactement le cas du climat."}],
  [{'n': "Garrett Hardin",
    'i': "Les biens communs ne conduisent pas naturellement au bien-être "
         "collectif mais au gaspillage et à l’épuisement.",
    'p': "Dans The Tragedy of the Commons (1968), il montre que lorsque "
         "l’usage est collectif et l’accès libre, les individus tendent à "
         "gaspiller, surexploiter et épuiser la ressource : contrairement à "
         "l’intuition, les communs ne garantissent pas la prospérité de tous."},
   {'n': "Garrett Hardin",
    'i': "Deux solutions seulement existent selon lui : privatiser ou "
         "nationaliser la ressource.",
    'p': "C’est un second apport, distinct du mécanisme, et c’est celui qu’Ostrom "
         "contestera : en réduisant les options au marché ou à l’État, Hardin "
         "ignore la capacité des communautés d’usagers à produire leurs propres "
         "règles de gestion."},
   {'n': "Elinor Ostrom",
    'i': "La tragédie des communs n’est pas une fatalité, car la coopération "
         "est possible.",
    'p': "Elle montre que les individus ne sont pas seulement égoïstes, que "
         "les institutions locales sont efficaces et que la microéconomie doit "
         "intégrer les normes sociales : sa critique porte donc moins sur le "
         "mécanisme que sur l’hypothèse comportementale qui le fonde."},
   {'n': "Mancur Olson",
    'i': "Chacun peut bénéficier d’un bien collectif sans contribuer à son "
         "financement.",
    'p': "Son analyse du passager clandestin complète celle de Hardin : la "
         "même non-excluabilité produit la surexploitation quand le bien est "
         "rival et la sous-production quand il ne l’est pas, ce qui donne deux "
         "visages à une seule défaillance."}],
  [{'f': "Garrett Hardin publie The Tragedy of the Commons en 1968, premier "
         "grand jalon de l’entrée de l’écologie en économie.",
    'p': "La date situe le mécanisme avant le rapport Meadows de 1972 : la "
         "question écologique entre dans l’analyse économique par le problème "
         "de l’accès aux ressources avant d’y entrer par celui des limites."},
   {'f': "Le cours formalise le mécanisme par deux propositions : le gain est "
         "individuel, la perte est collective.",
    'p': "Cette formulation condensée est directement utilisable et montre que "
         "la tragédie résulte d’une asymétrie d’incitations, non d’un défaut "
         "de morale."},
   {'f': "Le cours explique la tragédie des communs par le dilemme du "
         "prisonnier : chaque agriculteur a intérêt à faire paître le maximum "
         "de bêtes parce qu’il ne sait pas ce que feront les autres.",
    'p': "L’apport de la formalisation stratégique est de montrer que la "
         "surexploitation est un équilibre, donc stable, et non un simple "
         "accident de comportement."},
   {'f': "Appliqué au climat, bien commun mondial, le mécanisme produit "
         "passager clandestin, sous-investissement collectif et "
         "surexploitation des ressources planétaires.",
    'p': "La transposition justifie la gouvernance climatique internationale : "
         "sans coordination, la rationalité de chaque État conduit à un "
         "résultat que tous jugent mauvais."}],
  [{'q': "Sujet du type « L’intérêt individuel sert-il l’intérêt général ? »",
    'f': "La tragédie des communs constitue le contre-exemple le plus net. "
         "Hardin montre que lorsque l’usage est collectif et l’accès libre, ce "
         "qui est rationnel individuellement est catastrophique "
         "collectivement : le gain du prélèvement est individuel, la perte est "
         "collective, de sorte que chacun surexploite et que la ressource est "
         "épuisée. C’est une remise en cause directe de l’idée libérale "
         "classique selon laquelle la somme des intérêts individuels produit "
         "l’intérêt collectif.",
    'r': "Le raisonnement est d’autant plus fort qu’il ne suppose aucune "
         "irrationalité : il tire une conclusion collective défavorable de "
         "comportements individuellement impeccables.",
    'ex': "L’exemple du pâturage, où chaque agriculteur a intérêt à faire "
          "paître le maximum de bêtes parce qu’il ne sait pas ce que feront "
          "les autres."},
   {'q': "Sujet du type « Comment protéger les ressources naturelles ? »",
    'f': "Le diagnostic de la tragédie des communs commande les remèdes. "
         "Trois familles de solutions se présentent : la réglementation "
         "publique par quotas ou interdictions, la privatisation par "
         "attribution de droits de propriété, et la gestion collective. "
         "Hardin n’en retient que deux, privatiser ou nationaliser, tandis "
         "qu’Ostrom établit empiriquement l’existence d’une troisième voie, la "
         "gestion collective locale, qui ne passe ni par le marché ni par "
         "l’État.",
    'r': "Le raisonnement montre que la réponse dépend de caractéristiques "
         "observables de la ressource — délimitabilité, nombre d’usagers, "
         "coûts de transaction — et non d’un choix doctrinal préalable.",
    'ex': "La gestion de l’eau en Espagne et les pâturages collectifs en "
          "Suisse, que le cours cite parmi les cas étudiés par Ostrom."},
   {'q': "Sujet du type « La coopération internationale est-elle possible en "
         "matière climatique ? »",
    'f': "Le climat est un bien commun mondial, et sans coordination "
         "internationale apparaissent des comportements de passager "
         "clandestin, un sous-investissement collectif et une surexploitation "
         "des ressources planétaires. La difficulté est structurelle : il "
         "s’agit d’un dilemme du prisonnier à l’échelle des États, où chacun "
         "préfère que les autres supportent le coût de la réduction des "
         "émissions.",
    'r': "Le raisonnement explique pourquoi la coopération climatique est à la "
         "fois nécessaire et instable, ce qui éclaire le choix entre une "
         "logique contraignante et une logique volontaire.",
    'ex': "Le constat du cours selon lequel les mécanismes d’Ostrom sont plus "
          "difficiles à appliquer aux biens communs mondiaux, c’est-à-dire à "
          "grande échelle."}],
  voisins=['n4-communs', 'n4-gouvernance-communs', 'n4-externalites-env',
           'n4-climat'])


d('n4-gouvernance-communs', 4, "Gouvernance des communs",
  "Ni le marché ni l’État : des règles produites par les usagers eux-mêmes",
  "La gouvernance des communs désigne, à la suite des travaux d’Elinor "
  "Ostrom, la gestion collective d’une ressource partagée par la communauté "
  "de ses usagers, qui élaborent et font respecter leurs propres règles sans "
  "recourir ni à la privatisation ni à l’intervention directe de l’État. Elle "
  "constitue une troisième voie entre le marché et la puissance publique.",
  "Le point de départ d’Ostrom est une critique de la manière dont les "
  "économistes posent le problème. Ils présentent souvent une alternative trop "
  "simple : soit le marché règle les difficultés, soit l’État intervient. "
  "Ostrom montre que cette opposition est incomplète, et qu’il existe une "
  "troisième voie, la gestion collective par des communautés locales. Sa "
  "démonstration est empirique, et c’est ce qui lui donne sa force : elle "
  "étudie des cas concrets — gestion de l’eau en Espagne, pâturages "
  "collectifs en Suisse, forêts au Japon, systèmes d’irrigation en Asie — et "
  "constate que de nombreuses communautés parviennent à gérer durablement des "
  "biens communs sans passer ni par l’État ni par le marché. La conclusion "
  "contredit directement Hardin : la tragédie des communs n’est pas une "
  "fatalité. Le cours situe sa position dans un tableau qu’il faut savoir "
  "restituer : Hardin propose la privatisation ou l’État, Pigou l’intervention "
  "publique par taxes et réglementation, Coase les droits de propriété et le "
  "marché, Ostrom la gestion collective locale — ni marché pur ni État "
  "central, mais auto-organisation. Son apport théorique dépasse le cas des "
  "ressources naturelles, puisqu’elle montre que la coopération est possible, "
  "que les individus ne sont pas seulement égoïstes, que les institutions "
  "locales sont efficaces et que la microéconomie doit intégrer les normes "
  "sociales. Elle s’inscrit à ce titre dans la nouvelle économie "
  "institutionnelle. Le cours étend enfin la réflexion aux communs "
  "contemporains : les communs numériques comme les logiciels libres, "
  "Wikipédia et les données ouvertes, et les communs de la connaissance comme "
  "la recherche scientifique, les vaccins et les brevets — le débat sur le "
  "vaccin contre le Covid posant la question de savoir s’il relève du bien "
  "privé ou du bien commun. La limite est également donnée : ses mécanismes "
  "sont plus difficiles à appliquer aux biens communs mondiaux, à grande "
  "échelle.",
  [("Le refus de l’alternative marché-État",
    "La difficulté n’est pas de choisir entre deux institutions existantes "
    "mais de constater qu’une troisième forme de coordination fonctionne : "
    "l’auto-organisation des usagers, qui ne se réduit ni à un échange "
    "marchand ni à une contrainte publique."),
   ("La production endogène de règles",
    "Les usagers élaborent eux-mêmes les règles d’accès et de prélèvement : "
    "parce qu’ils connaissent la ressource et ses rythmes, ces règles sont "
    "mieux ajustées que des normes générales décidées à distance."),
   ("La surveillance mutuelle",
    "Dans une communauté d’usagers, les comportements sont observables : le "
    "resquilleur est identifié, ce qui réduit le coût de contrôle et rend la "
    "règle crédible sans appareil administratif."),
   ("L’hypothèse comportementale élargie",
    "La gestion collective suppose que les individus ne soient pas seulement "
    "égoïstes et que les normes sociales pèsent sur leurs décisions : "
    "l’analyse économique doit donc intégrer ces normes au lieu de les traiter "
    "comme extérieures."),
   ("La contrainte d’échelle",
    "Le dispositif repose sur l’interconnaissance et la proximité : il perd "
    "son efficacité lorsque les usagers sont très nombreux, anonymes et "
    "dispersés, ce qui le rend difficilement transposable aux communs "
    "mondiaux.")],
  [{'a': "La gouvernance collective évite les deux défauts symétriques de la "
         "privatisation et de l’étatisation : la marchandisation d’une "
         "ressource vitale et l’ignorance administrative des conditions "
         "locales.",
    'cond': "Elle suppose une communauté d’usagers identifiable, stable et "
            "capable de se doter de règles.",
    'lim': "Ces conditions sont absentes dès que la ressource est partagée par "
           "un très grand nombre d’acteurs sans lien entre eux."},
   {'a': "Elle repose sur une démonstration empirique et non sur un modèle, ce "
         "qui la rend difficilement réfutable sur le plan théorique.",
    'cond': "La portée des cas étudiés dépend de leur représentativité, et le "
            "cours en cite quatre familles distinctes.",
    'lim': "Une collection de cas réussis n’établit pas la fréquence des "
           "réussites : on ignore combien de communautés ont échoué."},
   {'a': "Elle enrichit la microéconomie en montrant que les normes sociales "
         "font partie des déterminants des comportements économiques.",
    'cond': "L’argument n’a de force que si l’on accepte de relâcher "
            "l’hypothèse d’un agent purement intéressé.",
    'lim': "Relâcher cette hypothèse rend les prédictions moins précises, ce "
           "qui est le coût habituel d’un réalisme accru."},
   {'a': "Elle s’applique aux communs contemporains, notamment numériques et "
         "de la connaissance, qui ne relèvent ni du marché pur ni de l’État.",
    'cond': "La transposition suppose que l’on puisse identifier une "
            "communauté de contributeurs dotée de règles, comme dans les "
            "logiciels libres.",
    'lim': "Pour les communs de la connaissance, la question du régime de "
           "propriété reste décisive, comme le montre le débat sur le statut "
           "du vaccin contre le Covid."}],
  [{'t': "Les communs sont nécessairement surexploités : seules la "
         "privatisation et la nationalisation peuvent les sauver.",
    'qui': "Garrett Hardin, dont Ostrom conteste directement la conclusion.",
    'rep': "La thèse est empiriquement démentie : de nombreuses communautés "
           "gèrent durablement des biens communs sans passer ni par l’État ni "
           "par le marché, ce qui prive la tragédie de son caractère fatal."},
   {'t': "La solution efficace passe par l’attribution de droits de "
         "propriété et par la négociation marchande entre les parties.",
    'qui': "Ronald Coase, dont le théorème constitue l’autre réponse "
           "classique.",
    'rep': "La solution marchande se heurte à deux limites que le cours "
           "souligne : tous les biens ne se prêtent pas à la propriété, et "
           "l’extension de la logique marchande pose la question de la "
           "marchandisation de la nature."},
   {'t': "La gestion collective locale ne peut pas répondre aux problèmes "
         "environnementaux globaux.",
    'qui': "Le constat que le cours formule lui-même à propos des biens "
           "communs mondiaux.",
    'rep': "L’objection est juste et doit être assumée : Ostrom est précieuse "
           "pour penser la gouvernance des communs, mais ses mécanismes sont "
           "plus difficiles à appliquer à grande échelle."}],
  [{'n': "Elinor Ostrom",
    'i': "Il existe une troisième voie entre le marché et l’État : la gestion "
         "collective par des communautés locales.",
    'p': "Elle part d’un constat critique : les économistes présentent une "
         "alternative trop simple entre marché et intervention publique. "
         "Première femme à recevoir le prix Nobel d’économie, en 2009, elle "
         "inscrit sa démarche dans la nouvelle économie institutionnelle."},
   {'n': "Elinor Ostrom",
    'i': "La coopération est possible et les institutions locales sont "
         "efficaces, ce qui oblige la microéconomie à intégrer les normes "
         "sociales.",
    'p': "C’est un apport distinct du précédent : au-delà du résultat sur les "
         "communs, il s’agit d’une correction de l’hypothèse comportementale "
         "standard, les individus n’étant pas seulement égoïstes. La portée en "
         "est générale et dépasse la question environnementale."},
   {'n': "Garrett Hardin",
    'i': "Les biens communs sont forcément surexploités, car chacun cherche "
         "son intérêt individuel.",
    'p': "Sa position constitue l’adversaire direct d’Ostrom et n’offre que "
         "deux issues, privatiser ou nationaliser. Le débat entre eux est le "
         "cœur du dossier : il porte moins sur le mécanisme que sur la capacité "
         "des usagers à s’auto-organiser."},
   {'n': "Arthur Pigou",
    'i': "L’externalité se corrige par l’intervention publique, taxes et "
         "réglementation.",
    'p': "Le cours le situe comme la troisième position du tableau "
         "comparatif : Hardin pour la privatisation ou l’État, Pigou pour "
         "l’intervention publique, Coase pour les droits de propriété et le "
         "marché, Ostrom pour la gestion collective locale."}],
  [{'f': "Ostrom étudie la gestion de l’eau en Espagne, les pâturages "
         "collectifs en Suisse, les forêts au Japon et les systèmes "
         "d’irrigation en Asie.",
    'p': "La diversité géographique et sectorielle des cas est l’argument "
         "central : elle interdit d’attribuer les réussites à une particularité "
         "culturelle locale."},
   {'f': "Elinor Ostrom (1933-2012) est la première femme à avoir reçu le prix "
         "Nobel d’économie, en 2009.",
    'p': "La reconnaissance institutionnelle marque l’entrée de l’analyse des "
         "institutions collectives dans le corps principal de la discipline."},
   {'f': "Le cours range parmi les communs contemporains les communs "
         "numériques — logiciels libres, Wikipédia, données ouvertes — et les "
         "communs de la connaissance — recherche scientifique, vaccins, "
         "brevets.",
    'p': "L’extension montre que la question des communs n’est pas réservée "
         "aux ressources naturelles : elle se pose partout où l’exclusion est "
         "possible techniquement mais contestable socialement."},
   {'f': "Le cours mentionne la proposition d’étendre la personnalité "
         "juridique à certains biens communs naturels — forêt, fleuve, "
         "Amazonie, écosystèmes — afin que des associations puissent agir en "
         "justice au nom de la nature.",
    'p': "Le fait montre une quatrième voie, juridique : la protection des "
         "communs peut passer par l’extension de la sphère du droit plutôt que "
         "par le prix, la propriété ou la communauté."}],
  [{'q': "Sujet du type « Faut-il choisir entre l’État et le marché ? »",
    'f': "Ostrom montre que l’alternative est mal posée. Les économistes "
         "présentent souvent une opposition trop simple entre le marché qui "
         "réglerait les problèmes et l’État qui interviendrait ; or de "
         "nombreuses communautés parviennent à gérer durablement des biens "
         "communs sans passer ni par l’un ni par l’autre, en créant leurs "
         "propres règles. La coordination économique ne se réduit donc pas à "
         "deux formes, le prix et la contrainte publique.",
    'r': "Le raisonnement transforme une question de doctrine en question "
         "d’institutions : il existe plusieurs dispositifs de coordination, et "
         "leur efficacité dépend des caractéristiques de la ressource.",
    'ex': "Le tableau du cours comparant les solutions de Hardin, Pigou, Coase "
          "et Ostrom, de la privatisation à l’auto-organisation."},
   {'q': "Sujet du type « Les institutions comptent-elles en économie ? »",
    'f': "La gouvernance des communs fournit une démonstration directe. "
         "Ostrom, qui s’inscrit dans la nouvelle économie institutionnelle, "
         "montre que la même ressource physique peut être épuisée ou préservée "
         "selon les règles que ses usagers se donnent : la coopération est "
         "possible, les institutions locales sont efficaces, et la "
         "microéconomie doit intégrer les normes sociales plutôt que de les "
         "traiter comme extérieures à son objet.",
    'r': "Le raisonnement isole la variable institutionnelle en maintenant la "
         "ressource constante, ce qui donne à la démonstration une force "
         "comparative rare.",
    'ex': "Les pâturages collectifs suisses et les forêts japonaises, gérés "
          "durablement par des règles d’usage locales."}],
  voisins=['n4-tragedie', 'n4-communs', 'n4-externalites-env',
           'n4-reglementation-env'])


d('n4-climat', 4, "Changement climatique",
  "Un bien commun mondial, une asymétrie de responsabilités, un problème d’horizon",
  "Le changement climatique est traité par le cours comme la défaillance "
  "économique la plus difficile : le climat est un bien commun mondial, rival "
  "dans sa capacité d’absorption et non excluable, dont la dégradation résulte "
  "d’externalités négatives diffuses. Son traitement suppose une coordination "
  "internationale, une mesure scientifique partagée et des instruments "
  "capables de peser sur des décisions de long terme.",
  "Le changement climatique concentre toutes les difficultés analysées "
  "séparément ailleurs, et c’est pourquoi le cours le construit en quatre "
  "repères qu’il faut savoir enchaîner. Premier repère, le problème de "
  "structure : avec Hardin, le climat apparaît comme un bien commun mondial, "
  "de sorte que l’absence de coordination internationale produit des "
  "comportements de passager clandestin, un sous-investissement collectif et "
  "une surexploitation des ressources planétaires. Deuxième repère, la mesure : "
  "le GIEC, créé en 1988, ne produit pas lui-même toutes les recherches mais "
  "réalise une synthèse scientifique mondiale sur l’état du climat, les causes "
  "du réchauffement, les scénarios d’évolution et les options d’atténuation et "
  "d’adaptation ; il consolide le consensus scientifique, guide la gouvernance "
  "et objective les risques. Troisième repère, la décomposition des causes : "
  "l’identité de Kaya, formulée dans les années 1990, décompose les émissions "
  "de CO₂ en quatre facteurs — l’intensité carbone de l’énergie, l’intensité "
  "énergétique de la production, le niveau de vie et la population. Son "
  "enseignement est décisif, parce qu’il explique pourquoi les émissions "
  "continuent d’augmenter : les gains d’efficacité énergétique et la baisse de "
  "l’intensité carbone peuvent être annulés par la hausse du niveau de vie et "
  "de la population. Quatrième repère, l’obstacle temporel : Mark Carney "
  "formule en 2015 la tragédie des horizons, décalage entre le temps long de "
  "la transition et le temps court des marchés financiers, des entreprises et "
  "des calendriers politiques — le climat impose des investissements de long "
  "terme, avec des coûts immédiats et des bénéfices futurs, tandis que les "
  "acteurs raisonnent sur la rentabilité immédiate. Reste la question des "
  "instruments, que le cours pose comme le dilemme central : marché ou règle ? "
  "D’un côté la taxe carbone, le prix du carbone, le marché de quotas et les "
  "incitations ; de l’autre les normes, interdictions, standards de production "
  "et obligations juridiques.",
  [("La structure de bien commun mondial",
    "La capacité d’absorption de l’atmosphère est rivale — ce qu’un émetteur "
    "utilise n’est plus disponible — et non excluable, aucun État ne pouvant "
    "en être écarté : d’où la logique de passager clandestin entre États."),
   ("L’externalité négative diffuse",
    "L’émetteur ne supporte pas le coût du dommage qu’il cause : le coût "
    "marginal social excède le coût marginal privé, ce qui conduit à une "
    "surproduction des activités émettrices et à un prix trop bas."),
   ("La décomposition des émissions",
    "L’identité de Kaya ramène les émissions à quatre déterminants — intensité "
    "carbone de l’énergie, intensité énergétique du PIB, niveau de vie, "
    "population — ce qui permet d’identifier sur lequel une politique agit "
    "réellement."),
   ("L’effet de compensation entre facteurs",
    "Les progrès obtenus sur l’intensité carbone et l’intensité énergétique "
    "peuvent être annulés par la hausse du niveau de vie et de la population : "
    "c’est la raison arithmétique de la poursuite de la hausse des émissions."),
   ("Le décalage des horizons",
    "Les coûts de l’action sont immédiats et les bénéfices lointains, alors "
    "que les acteurs économiques raisonnent sur la rentabilité immédiate ou le "
    "calendrier politique : l’investissement nécessaire n’est donc pas réalisé "
    "même lorsqu’il est collectivement rentable.")],
  [{'a': "La qualification du climat comme bien commun mondial fournit une "
         "justification économique rigoureuse de la coopération "
         "internationale.",
    'cond': "L’argument suppose que les États se comportent comme des usagers "
            "rationnels d’une ressource partagée, ce que fait le cours.",
    'lim': "Il ne dit pas comment faire respecter un accord faute d’autorité "
           "supranationale, difficulté que la comparaison entre Kyoto et Paris "
           "met précisément en évidence."},
   {'a': "L’identité de Kaya permet d’évaluer la portée réelle d’une "
         "politique, en identifiant le facteur sur lequel elle agit.",
    'cond': "Il s’agit d’une identité comptable : elle décompose sans établir "
            "de causalité entre les facteurs.",
    'lim': "Elle ne dit rien des interactions, alors que l’effet rebond montre "
           "précisément qu’agir sur l’intensité énergétique peut modifier les "
           "usages, donc le niveau de vie mesuré."},
   {'a': "Le GIEC objective les risques et consolide un consensus "
         "scientifique, ce qui rend la négociation politique possible.",
    'cond': "Son autorité repose sur son caractère de synthèse : il ne produit "
            "pas lui-même toutes les recherches qu’il rassemble.",
    'lim': "L’objectivation du risque ne produit pas l’action : la tragédie "
           "des horizons montre que l’information ne suffit pas à modifier des "
           "décisions dont l’horizon est court."},
   {'a': "La tragédie des horizons identifie un obstacle financier précis, "
         "donc susceptible d’un traitement par la régulation prudentielle et "
         "l’information des marchés.",
    'cond': "Le traitement suppose que les acteurs financiers intègrent "
            "effectivement le risque climatique dans la valorisation des "
            "actifs.",
    'lim': "Cette intégration suppose elle-même un horizon long, ce qui rend "
           "le remède partiellement circulaire."}],
  [{'t': "La croissance finira par résoudre le problème, car la hausse des "
         "revenus finance les technologies propres et nourrit la demande de "
         "normes.",
    'qui': "Grossman et Krueger, avec la courbe environnementale de Kuznets.",
    'rep': "Les deux mécanismes sont réels, du côté de l’offre et de la "
           "demande, mais le découplage absolu n’est pas garanti et "
           "l’identité de Kaya montre que la hausse du niveau de vie peut "
           "annuler les gains techniques."},
   {'t': "Le marché du carbone est l’instrument le plus efficace, puisqu’il "
         "donne un signal-prix et fait payer la pollution.",
    'qui': "La logique de marché que le cours oppose à celle de la règle.",
    'rep': "L’instrument n’est efficace que si le prix est assez élevé et "
           "stable : le cours relève qu’il est souvent trop faible et trop "
           "volatil, autour de 80 € la tonne quand environ 140 € seraient "
           "nécessaires."},
   {'t': "La contrainte doit venir d’en haut, par des engagements "
         "contraignants, plutôt que des engagements volontaires.",
    'qui': "Le débat top-down contre bottom-up que le cours pose explicitement.",
    'rep': "Le top-down apporte plus de contrainte, une meilleure coordination "
           "et plus de cohérence collective, mais il s’expose au refus "
           "d’obéissance, à une faible adhésion et aux contournements."},
   {'t': "Les comportements individuels sont le levier décisif, puisque c’est "
         "la consommation qui engendre les émissions.",
    'qui': "La lecture par la sobriété individuelle que le cours examine.",
    'rep': "Ces gestes sont utiles pour sensibiliser mais représentent une "
           "part limitée des grands déséquilibres : la responsabilisation "
           "individuelle ne peut masquer le poids des infrastructures et des "
           "modes de production."}],
  [{'n': "Garrett Hardin",
    'i': "Un bien commun non régulé tend à être surexploité, quelle que soit "
         "l’échelle à laquelle on l’observe.",
    'p': "Le cours applique explicitement son mécanisme au climat, bien commun "
         "mondial : sans coordination internationale apparaissent des "
         "comportements de passager clandestin, un sous-investissement "
         "collectif et une surexploitation des ressources planétaires. Le "
         "climat illustre la logique du passager clandestin à l’échelle du "
         "monde."},
   {'n': "Yoichi Kaya",
    'i': "Les émissions de CO₂ se décomposent en quatre facteurs multiplicatifs.",
    'p': "L’identité formulée dans les années 1990 distingue l’intensité "
         "carbone de l’énergie, l’intensité énergétique de la production, le "
         "niveau de vie et la population. Elle montre que les gains "
         "d’efficacité peuvent être annulés par la hausse du niveau de vie et "
         "de la population, ce qui explique la poursuite de l’augmentation des "
         "émissions."},
   {'n': "Mark Carney",
    'i': "Il existe une tragédie des horizons : le temps du climat n’est pas "
         "celui des marchés.",
    'p': "Gouverneur de la Banque d’Angleterre lorsqu’il formule cette idée en "
         "2015, il souligne que le climat impose des investissements de long "
         "terme avec des coûts immédiats et des bénéfices futurs, alors que "
         "les acteurs raisonnent à court terme, selon la rentabilité immédiate "
         "ou le calendrier politique et financier."},
   {'n': "Gene Grossman",
    'i': "Au-delà d’un certain niveau de développement, la hausse du revenu "
         "peut s’accompagner d’une baisse des émissions.",
    'p': "Avec Alan Krueger, il montre en 1995 que deux mécanismes peuvent "
         "produire un découplage absolu, où le PIB continue d’augmenter tandis "
         "que les émissions diminuent : le financement de technologies plus "
         "propres du côté de l’offre, la demande sociale de protection "
         "environnementale du côté de la demande."}],
  [{'f': "Le GIEC est créé en 1988 et réalise une synthèse scientifique "
         "mondiale sur l’état du climat et les options d’atténuation et "
         "d’adaptation.",
    'p': "La date établit que l’objectivation scientifique précède les grands "
         "accords internationaux : la connaissance partagée est la condition "
         "de la négociation."},
   {'f': "Le prix du carbone sur le marché européen s’établit autour de 80 € "
         "la tonne, jugé insuffisant, certains économistes estimant qu’environ "
         "140 € seraient nécessaires pour être réellement dissuasifs.",
    'p': "L’écart chiffré est l’argument le plus précis contre une confiance "
         "excessive dans le signal-prix : l’instrument existe mais son "
         "calibrage ne produit pas l’effet attendu."},
   {'f': "L’esprit du protocole de Kyoto puis des accords de Paris repose sur "
         "le principe de responsabilités communes mais différenciées.",
    'p': "Le principe traduit institutionnellement l’asymétrie des "
         "responsabilités historiques : les pays développés doivent réduire "
         "davantage, financer la transition mondiale et aider les pays plus "
         "pauvres à se décarboner."},
   {'f': "Les pays développés sont historiquement les plus responsables des "
         "dégradations environnementales, tandis que les pays les moins "
         "développés en subissent souvent les effets les plus violents.",
    'p': "Cette double asymétrie est ce qui rend la négociation climatique "
         "irréductible à un problème technique : elle est aussi un problème de "
         "répartition des efforts."}],
  [{'q': "Sujet du type « Pourquoi est-il si difficile de lutter contre le "
         "changement climatique ? »",
    'f': "Trois obstacles se cumulent, de nature différente. Le premier est "
         "structurel : le climat est un bien commun mondial, de sorte que sans "
         "coordination internationale apparaissent des comportements de "
         "passager clandestin et un sous-investissement collectif. Le deuxième "
         "est arithmétique : l’identité de Kaya montre que les gains "
         "d’efficacité énergétique et la baisse de l’intensité carbone peuvent "
         "être annulés par la hausse du niveau de vie et de la population. Le "
         "troisième est temporel : la tragédie des horizons oppose le temps "
         "long de la transition au temps court des marchés.",
    'r': "Hiérarchiser trois obstacles de natures distinctes — institutionnel, "
         "comptable, temporel — permet de montrer qu’aucun instrument unique "
         "ne peut suffire, puisque chacun n’en traite qu’un.",
    'ex': "La poursuite de la hausse des émissions mondiales malgré "
          "l’amélioration continue de l’efficacité énergétique."},
   {'q': "Sujet du type « Faut-il préférer le marché ou la règle pour "
         "protéger l’environnement ? »",
    'f': "Le cours pose le dilemme en deux colonnes : d’un côté le marché, "
         "avec la taxe carbone, le prix du carbone, le marché de quotas et les "
         "incitations ; de l’autre la règle, avec les normes, interdictions, "
         "standards de production et obligations juridiques. Chacune a sa "
         "faiblesse propre : le prix du carbone est souvent trop faible et "
         "trop volatil, et les règles peuvent être contournées dès lors que "
         "les acteurs disposent d’arbitrages spatiaux et logistiques.",
    'r': "Le raisonnement montre que l’opposition n’est pas entre efficacité "
         "et contrainte mais entre deux vulnérabilités, le calibrage pour le "
         "prix et le contournement pour la règle, ce qui plaide pour leur "
         "combinaison.",
    'ex': "La taxe française sur les colis aériens, contournée par une "
          "livraison dans un autre pays européen puis un transport routier "
          "vers la France."},
   {'q': "Sujet du type « La finance peut-elle financer la transition "
         "écologique ? »",
    'f': "La tragédie des horizons formulée par Mark Carney en 2015 identifie "
         "l’obstacle central : le climat impose des investissements de long "
         "terme, avec des coûts immédiats et des bénéfices futurs, alors que "
         "les acteurs économiques raisonnent à court terme, en fonction de la "
         "rentabilité immédiate ou du calendrier politique et financier. Il "
         "existe donc un décalage structurel entre l’horizon du climat et "
         "celui des marchés.",
    'r': "Le raisonnement situe l’obstacle dans la structure temporelle des "
         "décisions et non dans un manque de capitaux, ce qui déplace la "
         "solution vers la régulation des horizons plutôt que vers le volume "
         "de financement.",
    'ex': "Le risque de dévalorisation des actifs carbonés, que le cours "
          "mentionne parmi les enjeux financiers de la transition."}],
  voisins=['n4-justice-climatique', 'n4-communs', 'n4-taxe-carbone',
           'n4-quotas', 'n4-decouplage'])


d('n4-justice-climatique', 4, "Justice climatique",
  "Ceux qui ont émis et ceux qui subissent ne sont pas les mêmes",
  "La justice climatique désigne l’exigence de répartir l’effort de lutte "
  "contre le changement climatique en tenant compte d’une double asymétrie : "
  "les pays développés sont historiquement les plus responsables des émissions "
  "de gaz à effet de serre, tandis que les pays les moins développés en "
  "subissent les effets les plus violents et disposent des plus faibles "
  "capacités d’adaptation.",
  "La justice climatique transforme un problème d’efficacité en problème de "
  "répartition, et c’est ce déplacement qu’une copie doit expliciter. Le "
  "paradoxe central est posé clairement par le cours : les pays riches ont la "
  "plus forte responsabilité historique, les pays pauvres la plus forte "
  "exposition et la plus faible capacité d’adaptation. Les populations les "
  "plus vulnérables sont souvent celles qui subissent le plus fortement "
  "canicules, inondations, chocs climatiques et vulnérabilités "
  "environnementales. De cette asymétrie découlent trois exigences que le "
  "cours énumère : la justice climatique elle-même, la reconnaissance d’une "
  "responsabilité historique, et le financement climatique par les pays "
  "développés. La traduction institutionnelle en est le principe de "
  "responsabilités communes mais différenciées, que l’on retrouve dans "
  "l’esprit du protocole de Kyoto puis des accords de Paris. Concrètement, les "
  "pays développés sont censés réduire davantage leurs émissions, financer une "
  "partie de la transition mondiale et aider les pays plus pauvres à se "
  "décarboner ; à l’inverse, les pays en développement peuvent bénéficier "
  "d’une plus grande souplesse, recevoir des aides et disposer d’un calendrier "
  "plus flexible. Ce dispositif rencontre aujourd’hui une difficulté précise, "
  "que le cours identifie : si la Chine cesse d’être perçue comme un pays en "
  "développement, elle pourrait progressivement être considérée comme un pays "
  "devant contribuer davantage au financement et assumer des engagements plus "
  "lourds. La justice climatique a par ailleurs une dimension de mesure : "
  "l’IDH classique surestime la performance des pays développés parce qu’il "
  "ne prend pas en compte l’empreinte écologique incorporée dans les "
  "importations, de sorte qu’une production intérieure peut sembler propre "
  "alors qu’une partie de la pollution est externalisée. Enfin, la justice "
  "climatique se heurte à une tension interne aux pays développés eux-mêmes, "
  "puisqu’il faut concilier politiques climatiques et politiques sociales.",
  [("L’asymétrie des responsabilités historiques",
    "Le stock de gaz à effet de serre présent dans l’atmosphère résulte "
    "d’émissions cumulées depuis l’industrialisation : la responsabilité ne se "
    "mesure donc pas au flux annuel courant mais à la contribution "
    "historique."),
   ("L’asymétrie des expositions",
    "Les pays les moins développés subissent les effets les plus violents — "
    "canicules, inondations, chocs climatiques — et disposent des plus faibles "
    "capacités d’adaptation : le dommage ne frappe donc pas là où il a été "
    "causé."),
   ("La différenciation des obligations",
    "Le principe de responsabilités communes mais différenciées module "
    "l’effort : réduction plus forte, financement de la transition mondiale et "
    "aide à la décarbonation pour les pays développés, souplesse et calendrier "
    "plus flexible pour les autres."),
   ("La question du reclassement",
    "La différenciation repose sur un classement : si un pays cesse d’être "
    "perçu comme en développement, il peut être appelé à contribuer davantage "
    "au financement et à assumer des engagements plus lourds, ce que le cours "
    "signale à propos de la Chine."),
   ("L’externalisation de la pollution",
    "Une partie des émissions associées à la consommation d’un pays riche est "
    "produite ailleurs : le découpage par territoire sous-estime la "
    "responsabilité réelle, ce que l’IDH ajusté aux pressions planétaires "
    "cherche à corriger.")],
  [{'a': "La justice climatique rend la négociation possible : sans "
         "différenciation, les pays en développement n’auraient aucune raison "
         "d’accepter une contrainte.",
    'cond': "La différenciation doit être perçue comme équitable par les deux "
            "parties, ce qui suppose un critère de classement accepté.",
    'lim': "La différenciation réduit la portée de l’effort global, puisqu’une "
           "partie croissante des émissions provient précisément des pays "
           "bénéficiant de la souplesse."},
   {'a': "Elle corrige un biais de mesure réel, puisque la comptabilisation "
         "territoriale ignore l’empreinte écologique incorporée dans les "
         "importations.",
    'cond': "La correction suppose de pouvoir imputer les émissions à la "
            "consommation finale plutôt qu’au lieu de production.",
    'lim': "Cette imputation est techniquement difficile et déplace la "
           "responsabilité sans indiquer qui doit payer, le producteur ou le "
           "consommateur."},
   {'a': "Elle justifie un financement climatique des pays développés vers les "
         "pays pauvres, qui porte sur une capacité d’adaptation et pas "
         "seulement sur des émissions.",
    'cond': "Le financement n’est efficace que s’il est effectivement affecté "
            "à l’adaptation et à la décarbonation.",
    'lim': "La question de l’efficacité de l’aide se repose ici intégralement, "
           "le montant transféré ne garantissant pas l’usage."},
   {'a': "Elle met au jour une tension entre objectifs légitimes, climatiques "
         "et sociaux, qu’il vaut mieux expliciter que dissimuler.",
    'cond': "L’explicitation n’est utile que si elle débouche sur des "
            "dispositifs de compensation des perdants de la transition.",
    'lim': "Reconnaître la tension ne la résout pas : le cours constate la "
           "faible acceptabilité politique des hausses de prix de l’énergie et "
           "du transport."}],
  [{'t': "Seules les émissions actuelles devraient compter dans le partage "
         "de l’effort, car ce sont les seules qu’on puisse encore éviter.",
    'qui': "La logique d’efficacité, qui conduit à concentrer l’effort là où "
           "le coût de réduction est le plus faible.",
    'rep': "L’argument est juste en efficacité et faux en équité : le stock "
           "atmosphérique résulte d’émissions cumulées, et ignorer la "
           "responsabilité historique prive la négociation de toute base "
           "acceptable pour les pays du Sud."},
   {'t': "La différenciation est devenue obsolète, car certains grands "
         "émergents émettent désormais massivement.",
    'qui': "La lecture que le cours applique au cas chinois.",
    'rep': "La difficulté est réelle, mais elle appelle une révision du "
           "classement et non l’abandon du principe : la Chine pourrait "
           "contribuer davantage au financement sans que disparaisse la "
           "distinction entre responsabilités historiques inégales."},
   {'t': "La justice climatique est un argument rhétorique qui retarde "
         "l’action en déplaçant la discussion vers la répartition des torts.",
    'qui': "Les positions privilégiant l’urgence de la réduction sur la "
           "question de l’équité.",
    'rep': "L’objection néglige que l’asymétrie est aussi une asymétrie de "
           "capacité : un pays sans capacité d’adaptation ne peut pas agir, de "
           "sorte que le financement n’est pas un détour mais une condition de "
           "l’action."}],
  [{'n': "Garrett Hardin",
    'i': "Un bien commun non régulé est surexploité, chacun ayant intérêt à "
         "laisser les autres supporter l’effort.",
    'p': "Appliqué au climat, son mécanisme explique pourquoi la question de "
         "la répartition est inévitable : puisque chaque État préfère que les "
         "autres réduisent, aucun accord n’est stable sans une règle de partage "
         "de l’effort perçue comme équitable."},
   {'n': "Yoichi Kaya",
    'i': "Les émissions dépendent notamment du niveau de vie et de la "
         "population.",
    'p': "Sa décomposition éclaire la justice climatique : demander à un pays "
         "pauvre de réduire ses émissions revient, à technologie donnée, à lui "
         "demander de limiter la hausse de son niveau de vie, ce qui montre "
         "que la contrainte climatique n’a pas le même contenu selon le niveau "
         "de développement."},
   {'n': "Amartya Sen",
    'i': "Le développement se juge à l’étendue des capacités réelles des "
         "individus, non au seul revenu.",
    'p': "Son approche éclaire l’asymétrie des expositions : deux pays frappés "
         "par le même choc climatique n’en subissent pas le même dommage, "
         "parce que la capacité d’y faire face dépend de l’accès à la santé, à "
         "l’éducation et aux infrastructures."}],
  [{'f': "Le cours énonce le paradoxe central : les pays riches ont la plus "
         "forte responsabilité historique, les pays pauvres la plus forte "
         "exposition et la plus faible capacité d’adaptation.",
    'p': "La formulation en deux volets est directement mobilisable et montre "
         "que l’injustice est double, portant à la fois sur la cause et sur "
         "l’effet."},
   {'f': "Le principe de responsabilités communes mais différenciées anime "
         "l’esprit du protocole de Kyoto puis des accords de Paris.",
    'p': "Le fait établit que la justice climatique n’est pas une revendication "
         "extérieure au droit international mais un principe qui y est inscrit."},
   {'f': "Les pays développés sont censés réduire davantage leurs émissions, "
         "financer une partie de la transition mondiale et aider les pays plus "
         "pauvres à se décarboner.",
    'p': "L’énumération donne le contenu concret du principe : il porte sur "
         "trois obligations distinctes, dont deux sont financières."},
   {'f': "L’IDH classique surestime la performance des pays développés car il "
         "ne prend pas en compte l’empreinte écologique incorporée dans les "
         "importations.",
    'p': "Le constat relie justice climatique et commerce international : la "
         "délocalisation des productions polluantes déplace les émissions sans "
         "réduire la responsabilité du consommateur final."}],
  [{'q': "Sujet du type « L’effort climatique doit-il être partagé "
         "également ? »",
    'f': "La double asymétrie que relève le cours interdit un partage "
         "uniforme : les pays développés sont historiquement les plus "
         "responsables des dégradations environnementales, mais les pays les "
         "moins développés en subissent souvent les effets les plus violents "
         "et disposent des plus faibles capacités d’adaptation. C’est ce qui "
         "fonde le principe de responsabilités communes mais différenciées, "
         "selon lequel les pays développés doivent réduire davantage, financer "
         "une partie de la transition mondiale et aider les plus pauvres à se "
         "décarboner.",
    'r': "Le raisonnement distingue trois critères de partage — la "
         "responsabilité historique, l’exposition au dommage et la capacité "
         "d’agir — et montre qu’ils convergent tous dans le même sens, ce qui "
         "rend la différenciation difficilement contestable.",
    'ex': "L’esprit du protocole de Kyoto puis des accords de Paris, qui "
          "accordent aux pays en développement souplesse, aides et calendrier "
          "plus flexible."},
   {'q': "Sujet du type « Les politiques climatiques sont-elles socialement "
         "justes ? »",
    'f': "La question se pose à deux échelles, et c’est leur articulation qui "
         "fait la difficulté. Entre pays, la justice climatique exige un "
         "financement des pays développés vers les pays pauvres, au nom de la "
         "responsabilité historique. À l’intérieur des pays, le développement "
         "durable met en tension politiques climatiques et politiques "
         "sociales, puisque la transition crée des perdants à court terme : "
         "emplois détruits et hausses de prix de l’énergie et du transport "
         "dont l’acceptabilité politique est faible.",
    'r': "Raisonner simultanément aux deux échelles permet de montrer que la "
         "même mesure peut être juste internationalement et injuste "
         "socialement, ce qui explique les blocages politiques observés.",
    'ex': "Le constat du cours sur les reculs face au conflit entre écologie "
          "et compétitivité, et sur le coût social de la transition."}],
  voisins=['n4-climat', 'n4-durable', 'n4-transition', 'n4-limites'])
