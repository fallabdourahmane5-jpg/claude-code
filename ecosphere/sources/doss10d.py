# -*- coding: utf-8 -*-
"""Ensemble 10 — Le travail, l’emploi et le chômage (4/4)."""

from doss_base import d

d('n10-polarisation', 10, "Polarisation des emplois",
  "Les qualifiés d’un côté, les exposés de l’autre, et le creux au milieu",
  "La polarisation désigne l’écartement des positions dans la distribution des "
  "emplois et des rémunérations : les activités qualifiées et immatérielles "
  "captent une part croissante de la valeur, tandis que les tâches routinières "
  "et exposées à la concurrence internationale voient leur rémunération "
  "relative reculer. Le cours la documente par la courbe du sourire et par le "
  "modèle nomades-sédentaires.",
  "Le cours construit la polarisation à partir de trois analyses "
  "complémentaires, toutes issues de l’étude de la mondialisation. Première "
  "analyse, la courbe du sourire : dans une chaîne de valeur mondiale, la "
  "valeur se concentre aux deux extrémités, conception et services "
  "immatériels, tandis que l’assemblage en capte de moins en moins ; le cours "
  "explique pourquoi, les tâches d’assemblage étant plus routinières, de "
  "nombreux pays en développement peuvent entrer rapidement sur ce segment, "
  "d’où une concurrence accrue entre territoires, une baisse du prix de la "
  "tâche et une valeur ajoutée en recul. Le creusement de la courbe du sourire "
  "traduit donc une polarisation croissante de la valeur. Deuxième analyse, le "
  "modèle de Pierre-Noël Giraud : chaque économie comporte des activités "
  "exposées à la concurrence mondiale, dites nomades, et des activités "
  "protégées par leur ancrage territorial, dites sédentaires ; la "
  "mondialisation profite surtout aux nomades qualifiés, fragilise les "
  "travailleurs peu qualifiés exposés à la concurrence internationale, et "
  "exerce aussi une pression sur les salaires des services sédentaires peu "
  "qualifiés. Le cours identifie ainsi les grands perdants, les non-qualifiés "
  "des secteurs exposés, qui cumulent deux pressions, la concurrence "
  "internationale qui permet la délocalisation d’activités routinières et le "
  "progrès technique biaisé en faveur des qualifications qui automatise ces "
  "mêmes tâches. Troisième analyse, le théorème de Stolper-Samuelson : dans "
  "les pays avancés, la spécialisation favorise relativement le travail "
  "qualifié, le capital et les activités à forte valeur ajoutée, tandis que le "
  "travail peu qualifié exposé devient moins demandé, d’où des salaires "
  "relatifs en baisse, un chômage possible, une désindustrialisation locale et "
  "une polarisation des rémunérations. Le cours ajoute que le commerce "
  "n’explique pas seul ces évolutions, qui dépendent aussi du progrès "
  "technique, des institutions et des politiques publiques.",
  [("La concentration de la valeur aux extrémités",
    "Dans une chaîne mondiale, conception et services immatériels captent une "
    "part croissante de la valeur, l’assemblage de moins en moins : la "
    "répartition des gains suit la position occupée dans la chaîne et non le "
    "volume produit."),
   ("La concurrence sur les tâches routinières",
    "Les tâches d’assemblage étant routinières, de nombreux pays peuvent y "
    "entrer : la concurrence entre territoires s’accroît, le prix de la tâche "
    "baisse et sa valeur ajoutée recule."),
   ("Le partage entre activités nomades et sédentaires",
    "Les activités nomades peuvent se localiser dans plusieurs pays et sont "
    "donc mises en concurrence internationale, les sédentaires sont protégées "
    "par leur ancrage territorial : l’exposition, et non le secteur, "
    "détermine la position."),
   ("Le cumul des deux pressions sur les non-qualifiés exposés",
    "Les travailleurs peu qualifiés des secteurs exposés subissent à la fois "
    "la concurrence internationale, qui permet la délocalisation, et le "
    "progrès technique biaisé, qui automatise les tâches routinières."),
   ("La pression indirecte sur les services locaux",
    "Les activités nomades cherchent à réduire le coût des services locaux "
    "qu’elles consomment : les travailleurs sédentaires peu qualifiés restent "
    "protégés de la concurrence directe mais subissent une pression sur leurs "
    "rémunérations."),
   ("L’asymétrie entre gains diffus et pertes concentrées",
    "Les gains de pouvoir d’achat sont faibles mais répartis sur de nombreux "
    "ménages, les pertes d’emploi fortes mais concentrées sur certains "
    "individus et territoires : les deux ne se compensent pas "
    "individuellement.")],
  [{'a': "La polarisation explique un fait que le gain agrégé de la "
         "mondialisation masque : la persistance de perdants durables.",
    'cond': "L’argument suppose que l’on distingue les effets sur le pouvoir "
            "d’achat, diffus, des effets sur l’emploi, concentrés.",
    'lim': "Il ne conclut pas contre l’ouverture : le cours maintient "
           "l’existence d’un gain agrégé, de sorte que la question devient "
           "celle de la compensation des perdants."},
   {'a': "Le modèle nomades-sédentaires fournit un critère plus pertinent que "
         "la distinction sectorielle, puisqu’il repose sur l’exposition à la "
         "concurrence.",
    'cond': "Il suppose de pouvoir classer les activités selon leur capacité "
            "effective à se localiser ailleurs.",
    'lim': "La frontière évolue avec la technologie : des services longtemps "
           "sédentaires peuvent devenir nomades, ce qui rend la "
           "classification instable."},
   {'a': "Rapporter la polarisation à la nature des tâches, routinières ou "
         "non, explique mieux les évolutions observées que le seul niveau de "
         "diplôme.",
    'cond': "Le raisonnement suppose que l’automatisation et la "
            "délocalisation touchent d’abord les tâches standardisables.",
    'lim': "Le cours rappelle que le commerce international n’est qu’un "
           "déterminant parmi d’autres des inégalités, à côté du progrès "
           "technique, des institutions et des politiques économiques et "
           "sociales."},
   {'a': "Le théorème de Stolper-Samuelson fournit un mécanisme théorique "
         "reliant commerce et répartition des revenus.",
    'cond': "Il suppose que la spécialisation modifie effectivement la "
            "demande relative de facteurs dans les pays avancés.",
    'lim': "Le cours relève que les résultats réels ne correspondent pas "
           "toujours parfaitement à cette prédiction, précisément parce que "
           "d’autres déterminants interviennent."}],
  [{'t': "La mondialisation produit des gains de consommation largement "
         "diffusés mais des pertes d’emploi concentrées, de sorte que les plus "
         "exposés restent durablement perdants.",
    'qui': "L’analyse de l’asymétrie des effets que le cours développe avant "
           "le modèle nomades-sédentaires.",
    'rep': "Le constat n’invalide pas le gain agrégé de l’ouverture : il "
           "déplace la question vers les coûts d’ajustement et la "
           "compensation des catégories et des territoires touchés."},
   {'t': "La mondialisation profite aux nomades qualifiés et fragilise les "
         "travailleurs peu qualifiés exposés à la concurrence "
         "internationale.",
    'qui': "Pierre-Noël Giraud, avec le modèle nomades-sédentaires, initié "
           "dans les années 1990 et prolongé en 2018.",
    'rep': "Le cours complète l’analyse en montrant que les sédentaires peu "
           "qualifiés ne sont pas épargnés : protégés de la concurrence "
           "directe, ils subissent une pression sur leurs rémunérations."},
   {'t': "La polarisation des rémunérations s’explique par la spécialisation "
         "internationale et la modification de la demande relative de "
         "facteurs.",
    'qui': "Le théorème de Stolper-Samuelson, tel que le cours le mobilise.",
    'rep': "Le cours objecte que le commerce n’explique pas à lui seul les "
           "inégalités internes, qui dépendent également du progrès "
           "technique, des institutions et des politiques économiques et "
           "sociales."}],
  [{'n': "Pierre-Noël Giraud",
    'i': "Les activités nomades sont exposées à la concurrence mondiale, les "
         "sédentaires sont protégées par leur ancrage territorial.",
    'p': "Le cours précise la conclusion du modèle : la mondialisation "
         "profite surtout aux nomades qualifiés, fragilise les travailleurs "
         "peu qualifiés exposés à la concurrence internationale et exerce une "
         "pression sur les salaires des services sédentaires peu qualifiés."},
   {'n': "Daron Acemoglu",
    'i': "Les effets de la mondialisation sont très inégalement répartis "
         "entre les catégories de travailleurs.",
    'p': "Le cours le range avec Giraud et Milanović parmi les auteurs dont "
         "les analyses convergent : forte progression des hauts revenus, "
         "progression dans de nombreux pays émergents, stagnation relative de "
         "certains groupes populaires des pays riches."},
   {'n': "Branko Milanovic",
    'i': "La mondialisation réduit certaines inégalités entre pays tout en "
         "accroissant des inégalités internes.",
    'p': "Le cours mobilise ses travaux pour situer la polarisation dans une "
         "lecture mondiale : la classe moyenne émergente enregistre la plus "
         "forte hausse relative, mais le sommet de la distribution capte la "
         "plus grande part du surplus en valeur absolue."},
   {'n': "Thomas Piketty",
    'i': "La répartition des revenus dépend d’institutions et de politiques "
         "et non seulement des mécanismes de marché.",
    'p': "Le cours mobilise cette perspective lorsqu’il rappelle que "
         "l’évolution des inégalités dépend aussi du progrès technique, des "
         "institutions et des politiques économiques et sociales, et non du "
         "seul commerce international."}],
  [{'f': "Le cours explique que la valeur de l’assemblage diminue parce que "
         "ces tâches sont plus routinières, que de nombreux pays en "
         "développement peuvent entrer rapidement sur ce segment, d’où une "
         "concurrence accrue et une rémunération en baisse.",
    'p': "Le mécanisme montre que la polarisation ne vient pas de la "
         "technologie seule : elle résulte du nombre de concurrents capables "
         "d’exécuter une tâche standardisée."},
   {'f': "Le cours identifie les grands perdants, les non-qualifiés des "
         "secteurs exposés, qui cumulent la concurrence internationale et le "
         "progrès technique biaisé en faveur des qualifications.",
    'p': "Le cumul de deux pressions indépendantes explique que cette "
         "catégorie décroche plus fortement que les autres, et non "
         "proportionnellement."},
   {'f': "Le cours oppose le gain du caddie, faible mais diffus sur beaucoup "
         "de ménages, à la perte d’emploi, très forte mais concentrée sur "
         "certains individus et territoires.",
    'p': "L’opposition démontre que les deux effets ne se compensent pas "
         "individuellement, même si le solde agrégé est positif."}],
  [{'q': "La mondialisation enrichit-elle tout le monde ?",
    'f': "Le cours répond par une asymétrie précise : les gains de "
         "consommation sont faibles mais diffusés sur beaucoup de ménages, "
         "tandis que les pertes d’emploi sont très fortes mais concentrées "
         "sur certains individus et territoires. Les deux ne se compensent "
         "donc pas individuellement, ce qui explique que les plus exposés "
         "puissent rester durablement perdants malgré la baisse générale des "
         "prix.",
    'r': "Le raisonnement distingue le solde agrégé de sa répartition, et "
         "montre que la seconde suffit à produire des perdants durables sans "
         "contredire le premier.",
    'ex': "Giraud montre que la mondialisation profite surtout aux nomades "
          "qualifiés."},
   {'q': "Qui sont les perdants de l’ouverture ?",
    'f': "Le cours les désigne précisément : les travailleurs peu qualifiés "
         "des secteurs exposés, qui cumulent deux pressions, la concurrence "
         "internationale, qui permet la délocalisation d’activités "
         "routinières, et le progrès technique biaisé en faveur des "
         "qualifications, qui automatise ces mêmes tâches. Les sédentaires "
         "peu qualifiés subissent, eux, une pression sur leurs "
         "rémunérations.",
    'r': "On substitue au clivage par secteur un clivage par exposition et "
         "par nature des tâches, ce qui identifie les catégories réellement "
         "concernées.",
    'ex': "Le cours cite les ouvriers industriels peu qualifiés comme "
          "exemple."},
   {'q': "Le commerce explique-t-il la polarisation ?",
    'f': "Il y contribue, et le théorème de Stolper-Samuelson en fournit le "
         "mécanisme : dans les pays avancés, la spécialisation favorise "
         "relativement le travail qualifié et le capital, ce qui réduit la "
         "demande de travail peu qualifié exposé. Mais le cours souligne que "
         "les résultats réels ne correspondent pas toujours à cette "
         "prédiction, l’évolution des inégalités dépendant aussi du progrès "
         "technique, des institutions et des politiques publiques.",
    'r': "Le raisonnement reconnaît le mécanisme théorique avant d’en borner "
         "la portée empirique, ce qui conduit à une explication multifactorielle "
         "plutôt qu’à une cause unique.",
    'ex': "Le cours relève que le progrès technique biaisé est un facteur "
          "particulièrement important à côté du commerce."}],
  voisins=['n10-progres-technique-biaise', 'n10-precarite',
           'n10-chomage-conj-struct', 'n10-travail-emploi'])


d('n10-progres-technique-biaise', 10, "Progrès technique biaisé",
  "Une innovation qui n’avantage pas tout le monde de la même manière",
  "Le progrès technique biaisé désigne une innovation qui n’avantage pas "
  "également tous les travailleurs : il peut être biaisé en faveur des "
  "travailleurs qualifiés. Le cours en donne le mécanisme : les nouvelles "
  "technologies augmentent la productivité des qualifiés, remplacent certaines "
  "tâches routinières et réduisent la demande de certains travailleurs peu "
  "qualifiés, d’où un creusement des écarts salariaux.",
  "Le cours présente le progrès technique biaisé comme l’un des grands "
  "déterminants des inégalités contemporaines, à côté de l’ouverture "
  "internationale, et il en expose le mécanisme, les interactions et les "
  "limites. Le mécanisme est formulé comme un enchaînement : la technologie "
  "élève la demande de travail qualifié, donc la rémunération des qualifiés, "
  "donc les écarts salariaux. Il se décompose en trois effets distincts que le "
  "cours énumère : les nouvelles technologies augmentent la productivité des "
  "qualifiés, elles remplacent certaines tâches routinières, et elles "
  "réduisent la demande de certains travailleurs peu qualifiés. Le biais ne "
  "porte donc pas sur les personnes mais sur les tâches : ce sont les "
  "activités standardisables qui sont automatisées. L’interaction avec "
  "l’ouverture est décisive : le cours montre que les travailleurs peu "
  "qualifiés des secteurs exposés cumulent deux pressions, la concurrence "
  "internationale, qui permet la délocalisation d’activités routinières, et le "
  "progrès technique biaisé, qui automatise ces mêmes tâches, de sorte qu’ils "
  "sont les principaux perdants. Le cours rappelle ensuite que le commerce "
  "n’explique pas à lui seul les inégalités internes, lesquelles dépendent "
  "également du progrès technique, des institutions et des politiques "
  "économiques et sociales, et qu’un facteur particulièrement important est "
  "précisément le progrès technique biaisé. Il relie enfin cette analyse à la "
  "révolution numérique : l’intelligence artificielle marque un changement "
  "important, puisque les machines ne remplacent plus seulement la force de "
  "travail physique mais également certaines capacités cognitives, et "
  "Acemoglu, dans Power and Progress, en 2023, avec son coauteur Johnson, "
  "souligne que ces technologies peuvent accroître les asymétries de pouvoir "
  "et concentrer davantage la richesse et l’influence.",
  [("L’élévation de la productivité des qualifiés",
    "Les nouvelles technologies rendent les travailleurs qualifiés plus "
    "productifs : leur rémunération s’élève, ce qui creuse l’écart avec ceux "
    "dont la productivité n’est pas augmentée par la même technologie."),
   ("Le remplacement des tâches routinières",
    "L’automatisation substitue des machines aux tâches standardisables : le "
    "biais ne porte pas sur les personnes mais sur la nature des tâches, ce "
    "qui explique que des emplois intermédiaires soient touchés."),
   ("La baisse de la demande de travail peu qualifié",
    "Une fois les tâches routinières automatisées, la demande de certains "
    "travailleurs peu qualifiés diminue : leur salaire relatif baisse et le "
    "risque de chômage s’accroît."),
   ("Le cumul avec la concurrence internationale",
    "Les mêmes tâches routinières sont à la fois délocalisables et "
    "automatisables : les travailleurs peu qualifiés des secteurs exposés "
    "subissent donc deux pressions indépendantes qui s’additionnent."),
   ("L’extension aux capacités cognitives",
    "Avec l’intelligence artificielle, les machines ne remplacent plus "
    "seulement la force de travail physique mais également certaines "
    "capacités cognitives, ce qui déplace le périmètre des tâches exposées.")],
  [{'a': "Le progrès technique biaisé explique le creusement des écarts "
         "salariaux sans invoquer de changement institutionnel.",
    'cond': "L’explication suppose que la technologie modifie effectivement "
            "la demande relative de qualifications.",
    'lim': "Le cours rappelle que les inégalités dépendent aussi des "
           "institutions et des politiques économiques et sociales, de sorte "
           "que la technologie n’est pas un déterminant isolé."},
   {'a': "Raisonner en termes de tâches plutôt que de niveaux de diplôme rend "
         "mieux compte des emplois réellement touchés.",
    'cond': "Le raisonnement suppose que l’on puisse classer les tâches selon "
            "leur caractère routinier et donc standardisable.",
    'lim': "Ce classement évolue : l’intelligence artificielle étend "
           "l’automatisation à certaines capacités cognitives jusque-là "
           "considérées comme non routinières."},
   {'a': "L’articulation avec l’ouverture internationale permet d’identifier "
         "précisément les grands perdants et non une catégorie vague.",
    'cond': "Elle suppose de distinguer les secteurs exposés à la "
            "concurrence internationale des secteurs abrités.",
    'lim': "Elle rend difficile l’attribution des causes : une perte d’emploi "
           "dans un secteur exposé peut être imputée au commerce comme à "
           "l’automatisation."},
   {'a': "Le progrès technique biaisé n’est pas une fatalité : ses effets "
         "dépendent des institutions et des choix collectifs.",
    'cond': "L’argument suppose que les politiques de formation, de "
            "redistribution et de régulation puissent effectivement modifier "
            "la répartition des gains.",
    'lim': "Acemoglu souligne que les plateformes numériques et "
           "l’intelligence artificielle peuvent accroître les asymétries de "
           "pouvoir, ce qui rend cette action publique plus difficile."}],
  [{'t': "Le progrès technique biaisé accroît les inégalités lorsqu’il "
         "augmente davantage la productivité et la rémunération des "
         "travailleurs qualifiés que celles des travailleurs peu qualifiés.",
    'qui': "L’analyse du progrès technique biaisé telle que le cours la "
           "formule.",
    'rep': "Le cours relativise la portée du facteur en rappelant que le "
           "commerce international, les institutions et les politiques "
           "économiques et sociales contribuent également à l’évolution des "
           "inégalités."},
   {'t': "La technologie et les plateformes numériques peuvent renforcer les "
         "manipulations, accroître les asymétries de pouvoir et concentrer "
         "davantage la richesse et l’influence.",
    'qui': "Daron Acemoglu, dans Power and Progress, en 2023, avec son "
           "coauteur Johnson.",
    'rep': "L’argument élargit la question des inégalités de revenus à celle "
           "du pouvoir, mais il porte sur l’usage des données et des "
           "infrastructures autant que sur la technologie elle-même."},
   {'t': "L’ouverture internationale est la cause principale de la "
         "dégradation relative de la situation des travailleurs peu "
         "qualifiés.",
    'qui': "La lecture par le commerce international, que le théorème de "
           "Stolper-Samuelson sous-tend.",
    'rep': "Le cours objecte que le commerce n’explique pas à lui seul les "
           "inégalités internes et désigne le progrès technique biaisé comme "
           "un facteur particulièrement important, les deux pressions se "
           "cumulant sur les mêmes catégories."}],
  [{'n': "Daron Acemoglu",
    'i': "L’intelligence artificielle et les plateformes numériques peuvent "
         "accroître les asymétries de pouvoir et concentrer la richesse.",
    'p': "Le cours rattache cette thèse à Power and Progress, en 2023, écrit "
         "avec Johnson, et en tire que le contrôle des données et des flux "
         "d’information devient un enjeu démocratique majeur, au-delà de la "
         "seule question des rémunérations."},
   {'n': "Pierre-Noël Giraud",
    'i': "Les travailleurs peu qualifiés exposés à la concurrence "
         "internationale sont les plus fragilisés.",
    'p': "Le cours combine son modèle nomades-sédentaires avec le progrès "
         "technique biaisé : les non-qualifiés des secteurs exposés cumulent "
         "la concurrence internationale, qui permet la délocalisation, et "
         "l’automatisation des tâches routinières."},
   {'n': "Thomas Piketty",
    'i': "L’évolution des inégalités dépend des institutions et des "
         "politiques autant que des mécanismes économiques.",
    'p': "Le cours mobilise cette perspective lorsqu’il rappelle que "
         "l’évolution des inégalités dépend du progrès technique, des "
         "institutions et des politiques économiques et sociales, ce qui "
         "interdit de lire le biais technologique comme une fatalité."},
   {'n': "Joseph Schumpeter",
    'i': "L’innovation détruit des activités anciennes en même temps qu’elle "
         "en crée de nouvelles.",
    'p': "Le cours mobilise la destruction créatrice pour situer le progrès "
         "technique biaisé dans une dynamique plus large : le problème n’est "
         "pas la disparition d’emplois en soi, mais le fait que les emplois "
         "détruits et créés n’exigent pas les mêmes qualifications."}],
  [{'f': "Le cours formule le mécanisme sous forme d’enchaînement : "
         "technologie, hausse de la demande de travail qualifié, hausse de la "
         "rémunération des qualifiés, creusement des écarts salariaux.",
    'p': "La formulation montre que le biais agit par la demande relative de "
         "facteurs, et non par une baisse absolue de la rémunération des peu "
         "qualifiés."},
   {'f': "Le cours identifie les grands perdants, les non-qualifiés des "
         "secteurs exposés, soumis à la fois à la concurrence internationale "
         "et à l’automatisation des tâches routinières.",
    'p': "Le cumul montre que les deux grands déterminants des inégalités "
         "frappent la même catégorie, ce qui explique l’ampleur de son "
         "décrochage."},
   {'f': "Le cours relève que l’intelligence artificielle marque un "
         "changement important, les machines ne remplaçant plus seulement la "
         "force de travail physique mais également certaines capacités "
         "cognitives.",
    'p': "Cette extension du périmètre de l’automatisation montre que le "
         "biais technologique n’est pas figé : les emplois exposés changent "
         "avec la technologie."}],
  [{'q': "Le progrès technique détruit-il le travail ?",
    'f': "Le cours ne soutient pas une destruction nette mais un déplacement "
         "sélectif. Les nouvelles technologies augmentent la productivité des "
         "qualifiés, remplacent certaines tâches routinières et réduisent la "
         "demande de certains travailleurs peu qualifiés : le problème n’est "
         "donc pas le volume d’emploi mais la correspondance entre les "
         "qualifications détruites et celles qui sont demandées.",
    'r': "Le raisonnement remplace la question du volume par celle de la "
         "composition, ce qui explique la coexistence d’emplois non pourvus "
         "et de travailleurs sans emploi.",
    'ex': "Le cours formule l’enchaînement par une hausse de la demande de "
          "travail qualifié et un creusement des écarts salariaux."},
   {'q': "Le progrès technique est-il neutre ?",
    'f': "Le cours répond explicitement que non : le progrès technique "
         "n’avantage pas nécessairement tous les travailleurs de la même "
         "manière, il peut être biaisé en faveur des travailleurs qualifiés. "
         "Acemoglu ajoute que l’intelligence artificielle et les plateformes "
         "peuvent accroître les asymétries de pouvoir et concentrer la "
         "richesse et l’influence.",
    'r': "Le raisonnement passe de la neutralité supposée de la technique à "
         "l’examen de sa distribution, puis à celui du pouvoir qu’elle "
         "confère.",
    'ex': "Power and Progress, en 2023, traite précisément de ces asymétries "
          "de pouvoir."},
   {'q': "Technologie ou mondialisation ?",
    'f': "Le cours refuse de choisir et montre que les deux pressions "
         "frappent les mêmes travailleurs : les non-qualifiés des secteurs "
         "exposés subissent la concurrence internationale, qui permet la "
         "délocalisation des activités routinières, et le progrès technique "
         "biaisé, qui automatise ces mêmes tâches. Il rappelle en outre que "
         "les institutions et les politiques publiques jouent aussi.",
    'r': "Le raisonnement montre que la question de l’attribution des causes "
         "est mal posée lorsque les mécanismes agissent sur les mêmes tâches, "
         "et conclut à une explication multifactorielle.",
    'ex': "Le cours relève que le commerce international n’est qu’un "
          "déterminant parmi d’autres des inégalités internes."}],
  voisins=['n10-polarisation', 'n10-chomage-conj-struct',
           'n10-travail-emploi', 'n10-precarite'])
