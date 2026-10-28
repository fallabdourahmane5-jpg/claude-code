# -*- coding: utf-8 -*-
"""Visualisation 11 — Inégalités, pauvreté et justice sociale (type flux)."""

from vz_base import v, nd, ln

v('vz-inegalites', 'Inégalités, pauvreté et justice sociale',
  'Chapitres 1 et 6 · de la formation des écarts à leur correction',
  'flux',
  "Les inégalités ne se produisent pas au même endroit que là où on les "
  "mesure, ni là où on les corrige. Cette visualisation suit la chaîne "
  "complète : où les écarts se forment, comment on les mesure, comment ils "
  "ont évolué, par quels instruments on les réduit, et ce que ces "
  "instruments ne peuvent pas atteindre.",
  [("Flux et stocks, deux distributions différentes",
    "Le revenu est un flux, le patrimoine un stock. Les deux n’ont ni la "
    "même concentration ni les mêmes déterminants, et un système fiscal "
    "assis sur les flux agit peu sur les stocks. C’est la distinction qui "
    "commande tout le reste."),
   ("Deux échelles qui donnent des réponses opposées",
    "Entre pays, les écarts se réduisent ; à l’intérieur des pays, ils se "
    "creusent. La courbe de l’éléphant représente les deux mouvements "
    "simultanément : ne jamais répondre à « les inégalités augmentent-elles ? » "
    "sans préciser l’échelle."),
   ("Mécanisme ou institution ?",
    "Kuznets attendait une baisse automatique à un stade avancé ; le cours "
    "note que la phase descendante repose « surtout » sur la redistribution. "
    "Le retour des inégalités depuis 1980 tranche en faveur de "
    "l’institution.")],
  [
   # ------------------------------------- colonne 1 : où les écarts se forment
   nd('primaire', 'La répartition primaire', 'pilier',
      "Avant tout impôt : le partage de la valeur ajoutée entre rémunération "
      "du travail et profit. En 2022, le taux de marge s’élevait à 32 %.",
      grp=1,
      defi="La répartition primaire désigne la distribution des revenus telle "
           "qu’elle résulte de la participation à la production, avant toute "
           "intervention redistributive. Le cours l’analyse par le taux de "
           "marge, qui indique la part de la valeur ajoutée restant à "
           "l’entreprise après avoir payé les salariés, les cotisations et "
           "les impôts de production. Un taux élevé signifie que l’essentiel "
           "de la valeur ajoutée va au profit ; un taux faible qu’elle va à "
           "la rémunération des salariés.",
      mec=[("Le partage comme conflit distributif",
            "Il n’existe pas de niveau neutre du taux de marge : tout "
            "déplacement favorise l’une des deux parts. C’est ce qui en fait "
            "un indicateur du conflit distributif et non une simple donnée "
            "comptable."),
           ("Le lien avec l’investissement",
            "Lorsque l’excédent brut d’exploitation est suffisant, "
            "l’entreprise peut financer son investissement elle-même ; sinon "
            "elle recourt à l’endettement. C’est le canal principal par "
            "lequel le partage agit sur la croissance."),
           ("Le partage comme variable de politique économique",
            "Pour relancer l’économie, les libéraux défendent l’idée qu’il "
            "faut agir sur l’offre en restaurant le taux de marge des "
            "entreprises : le partage a été explicitement traité comme un "
            "levier, et non seulement comme un résultat du marché.")],
      aut=[{'n': "Thomas Piketty",
            'i': "La répartition entre revenus du travail et revenus du "
                 "capital dépend d’institutions et de choix politiques."}],
      faits=[{'f': "En 2022, le taux de marge des entreprises françaises "
                   "s’élevait à 32 % de la valeur ajoutée.",
              'p': "C’est le chiffre de référence du partage français : "
                   "environ un tiers reste à l’entreprise, environ deux tiers "
                   "vont à la rémunération du travail et aux prélèvements qui "
                   "l’accompagnent."}],
      termes=['partage de la valeur ajoutee', 'taux de marge',
              'repartition primaire'],
      dos=['n22-partage-valeur-ajoutee', 'n22-repartition-primaire']),

   nd('patrimoine', 'Le patrimoine : un stock cumulatif', 'pilier',
      "Les inégalités de patrimoine sont systématiquement plus fortes que "
      "celles de revenus, parce qu’elles s’accumulent et se transmettent.",
      grp=1,
      defi="Les inégalités de patrimoine désignent les écarts dans la "
           "détention de richesses accumulées — biens immobiliers, actifs "
           "financiers, épargne, capital productif. Le cours établit deux "
           "résultats : elles sont systématiquement plus fortes que les "
           "inégalités de revenus, et le système fiscal et social les réduit "
           "beaucoup moins, parce qu’elles reposent sur une logique "
           "cumulative et sur la transmission intergénérationnelle.",
      mec=[("La distinction flux / stock",
            "Le revenu est un flux mesuré annuellement ; le patrimoine est un "
            "stock accumulé dans le temps. Cette distinction explique "
            "pourquoi les deux distributions n’ont pas la même concentration."),
           ("Le caractère cumulatif",
            "Le patrimoine engendre un revenu qui peut être réinvesti : "
            "l’écart initial se creuse mécaniquement en l’absence de "
            "prélèvement sur le stock."),
           ("La transmission intergénérationnelle",
            "L’héritage reconduit la position d’une génération à l’autre, ce "
            "qui soustrait une part de la distribution au mérite comme à la "
            "mobilité.")],
      aut=[{'n': "Thomas Piketty",
            'i': "L’héritage a retrouvé une place centrale dans la formation "
                 "du patrimoine, contrairement à ce que suggérait "
                 "l’après-guerre."},
           {'n': "Franco Modigliani",
            'i': "Le patrimoine résulte principalement de l’épargne accumulée "
                 "au cours du cycle de vie."}],
      faits=[{'f': "En 2025, le patrimoine total des dix plus riches atteint "
                   "2 612 milliards d’euros, soit 42 % du PIB français, "
                   "contre 6 % en 1996.",
              'p': "Le chiffre date précisément la rupture : ce n’est pas le "
                   "niveau de concentration qui est inédit mais sa vitesse de "
                   "croissance, le ratio au PIB ayant été multiplié par sept "
                   "en une trentaine d’années."}],
      termes=['inegalites de patrimoine', 'heritage', 'capital'],
      dos=['n22-inegalites-patrimoine', 'n22-heritage']),

   # ------------------------------------------- colonne 2 : comment on mesure
   nd('mesure', 'Mesurer : indicateurs et décomposition', 'pilier',
      "Courbe de Lorenz, coefficient de Gini, indice de Theil : le dernier "
      "sépare ce qui vient des écarts entre groupes et ce qui vient des "
      "écarts internes.",
      grp=2,
      defi="La mesure des inégalités suppose de choisir un indicateur, et ce "
           "choix oriente la conclusion. La courbe de Lorenz représente "
           "graphiquement l’écart à l’égalité parfaite ; le coefficient de "
           "Gini le résume en un nombre ; l’indice de Theil, décomposable, "
           "permet de séparer la part des inégalités qui provient des écarts "
           "entre groupes de celle qui provient des écarts à l’intérieur des "
           "groupes. C’est cette décomposition qui rend lisible le paradoxe "
           "de la mondialisation.",
      mec=[("De la courbe à l’indice",
            "La courbe de Lorenz montre quelle part du revenu total revient "
            "aux x % les plus pauvres ; le coefficient de Gini mesure l’aire "
            "entre cette courbe et la diagonale d’égalité parfaite."),
           ("La décomposabilité",
            "Un indice décomposable permet de répondre séparément à deux "
            "questions distinctes : les pays se rapprochent-ils, et les "
            "individus d’un même pays s’écartent-ils ?"),
           ("Le choix de l’unité et de la période",
            "Mesurer en parité de pouvoir d’achat et en termes réels "
            "déflatés évite que les conclusions soient biaisées par "
            "l’inflation ou par les taux de change financiers.")],
      aut=[{'n': "Henri Theil",
            'i': "Un indice d’inégalité décomposable permet de séparer les "
                 "composantes entre groupes et à l’intérieur des groupes."}],
      args=[{'a': "Disposer de plusieurs indicateurs permet de distinguer "
                  "une hausse de la dispersion générale d’une concentration "
                  "au sommet, qui n’appellent pas les mêmes réponses.",
             'lim': "Un indicateur synthétique reste une moyenne : deux "
                    "distributions très différentes peuvent produire le même "
                    "coefficient."}],
      termes=['coefficient de gini', 'courbe de lorenz', 'indice de theil'],
      dos=['n22-inegalites-revenus', 'n22-inegalites-entre-et-au-sein']),

   nd('echelles', 'Entre pays et au sein des pays', 'detail',
      "Les écarts entre nations diminuent, les écarts internes augmentent. La "
      "courbe de l’éléphant montre les deux à la fois.",
      grp=2, par='mesure',
      defi="Cette notion désigne la décomposition des inégalités mondiales en "
           "deux composantes : les écarts de niveau de vie moyen entre "
           "nations et les écarts entre individus à l’intérieur d’un même "
           "pays. Le cours en fait un paradoxe central de la mondialisation, "
           "établi par Branko Milanovic : les inégalités entre pays diminuent "
           "tandis que les inégalités à l’intérieur des pays augmentent.",
      mec=[("La convergence entre nations",
            "L’industrialisation de pays très peuplés élève leur revenu moyen "
            "plus vite que celui des économies avancées : l’écart entre "
            "moyennes nationales se réduit."),
           ("La divergence interne",
            "Dans les économies avancées, les catégories exposées à la "
            "concurrence et à l’automatisation décrochent tandis que le "
            "sommet se concentre : la dispersion interne s’accroît."),
           ("La lecture par la courbe de l’éléphant",
            "La courbe classe la population mondiale par percentile de revenu "
            "et représente la croissance réelle de chacun : elle rend visibles "
            "simultanément la progression des émergents, la stagnation des "
            "classes moyennes occidentales et la concentration au sommet.")],
      aut=[{'n': "Branko Milanovic",
            'i': "Les inégalités entre pays diminuent tandis que les "
                 "inégalités au sein des pays augmentent."}],
      faits=[{'f': "Sur la courbe de l’éléphant (1988-2008), les plus pauvres "
                   "du monde progressent d’environ +15 %, la classe moyenne "
                   "des pays émergents de +70 à +80 %, et le top 1 % mondial "
                   "d’environ +60 %.",
              'p': "Les trois chiffres résument l’effet distributif de "
                   "l’hypermondialisation : réduction des écarts "
                   "internationaux portée par l’Asie, concentration "
                   "persistante au sommet, bénéfice faible pour les plus "
                   "pauvres."},
             {'f': "La classe moyenne des pays développés se situe autour du "
                   "80ᵉ percentile mondial et connaît une croissance réelle "
                   "proche de 0 % sur la période 1988-2008.",
              'p': "C’est le fait qui relie l’analyse économique des "
                   "inégalités à la sociologie politique de la "
                   "mondialisation : il explique le sentiment de "
                   "déclassement."}],
      termes=['courbe de l elephant', 'inegalites mondiales',
              'convergence entre pays'],
      dos=['n22-inegalites-entre-et-au-sein', 'n3-emergence']),

   # ------------------------------------------- colonne 3 : comment ça évolue
   nd('kuznets', 'La courbe de Kuznets', 'detail',
      "Les inégalités monteraient puis baisseraient avec le développement. "
      "Une hypothèse formulée en 1955 sur un pays et trente-cinq années.",
      grp=3,
      defi="La courbe de Kuznets est l’hypothèse, formulée en 1955 à partir "
           "de l’observation des inégalités aux États-Unis entre 1913 et "
           "1948, selon laquelle la relation entre croissance et inégalités "
           "suit une courbe en cloche : les inégalités augmentent au début du "
           "développement puis diminuent à un stade avancé, soit "
           "graphiquement un U inversé.",
      mec=[("La phase ascendante",
            "Le passage d’une économie agricole à une économie industrielle "
            "crée des différences de productivité importantes et des salaires "
            "industriels plus élevés : les écarts se creusent entre secteurs."),
           ("La phase descendante",
            "Généralisation de l’éducation, diffusion du progrès technique, "
            "urbanisation complète, montée de la classe moyenne — mais "
            "surtout développement de la redistribution, hausse des recettes "
            "fiscales et politiques sociales."),
           ("Le poids du « mais surtout »",
            "L’expression employée par le cours est décisive : elle place "
            "l’institution avant le mécanisme économique et prépare la "
            "critique de l’automaticité.")],
      aut=[{'n': "Simon Kuznets",
            'i': "La relation entre croissance et inégalités suivrait une "
                 "courbe en cloche, en U inversé."}],
      faits=[{'f': "L’hypothèse repose sur l’observation d’un seul pays entre "
                   "1913 et 1948.",
              'p': "La base empirique est précise et limitée, ce qui explique "
                   "à la fois la force de l’intuition et la fragilité de sa "
                   "généralisation à tous les développements."}],
      termes=['courbe de kuznets', 'u inverse', 'croissance et inegalites'],
      dos=['n22-courbe-kuznets', 'n22-inegalites-revenus']),

   nd('retour', 'Le retour des inégalités depuis 1980', 'limite',
      "Hausse des inégalités de revenus, forte concentration des patrimoines, "
      "explosion du top 1 % : la phase descendante ne s’est pas poursuivie.",
      grp=3,
      defi="Depuis les années 1980, dans de nombreux pays développés, on "
           "observe une hausse des inégalités de revenus, une forte "
           "concentration des patrimoines et une explosion du top 1 %. Cette "
           "dynamique contredit la phase descendante prévue par Kuznets : des "
           "économies parvenues au stade avancé voient leurs inégalités "
           "remonter, ce que la courbe ne prévoit pas.",
      mec=[("Le reflux de la redistribution",
            "Si la phase descendante reposait « surtout » sur la "
            "redistribution, alors la modification des systèmes redistributifs "
            "depuis les années 1980 suffit à expliquer le retournement sans "
            "invoquer aucun mécanisme nouveau."),
           ("La concentration au sommet plutôt que la dispersion générale",
            "Le mouvement observé n’est pas un écartement uniforme : c’est "
            "une concentration des revenus et des patrimoines dans le dernier "
            "centile, ce qui appelle des instruments spécifiques."),
           ("La composition nationale du sommet",
            "Environ 50 % du top 1 % mondial est américaine, ce que le cours "
            "décrit comme la montée d’une ploutocratie mondiale : "
            "l’inégalité interne d’un pays contribue directement à la forme "
            "du sommet de la distribution mondiale.")],
      aut=[{'n': "Thomas Piketty",
            'i': "La réduction des inégalités dépend de choix politiques et "
                 "non d’une trajectoire mécanique."}],
      opp=[{'t': "La hausse des inégalités internes serait l’effet mécanique "
                 "de la mondialisation et du progrès technique biaisé.",
            'qui': "lecture par les facteurs économiques",
            'rep': "Le cours objecte que la hausse des inégalités internes "
                   "dépend des institutions fiscales et politiques davantage "
                   "que de la mondialisation seule : les pays exposés aux "
                   "mêmes chocs ont connu des évolutions très différentes."}],
      termes=['top 1', 'concentration des patrimoines',
              'hausse des inegalites'],
      dos=['n22-inegalites-revenus', 'n22-inegalites-patrimoine']),

   # ------------------------------------------- colonne 4 : les instruments
   nd('redistribution', 'La redistribution', 'pilier',
      "En France, les écarts de niveau de vie passent d’un facteur 18 avant "
      "redistribution à un facteur 4 après. 53 % des ménages sont "
      "bénéficiaires nets.",
      grp=4,
      defi="La redistribution désigne l’action par laquelle l’État collecte "
           "des impôts et des cotisations puis redistribue sous forme "
           "d’allocations, de subventions et de services publics, ce qui "
           "modifie la répartition des revenus disponibles. Le cours en fait "
           "l’une des trois fonctions de l’État-providence selon Musgrave et "
           "en mesure l’effet avec précision.",
      mec=[("Le double mouvement",
            "Les ménages modestes voient leur revenu multiplié par 4, tandis "
            "que les plus aisés perdent environ 40 % de leur revenu initial : "
            "la réduction de l’écart résulte de la combinaison des "
            "prélèvements et des prestations, non d’un seul instrument."),
           ("Le niveau de vie élargi",
            "Une famille modeste qui paie peu d’impôts mais reçoit école "
            "gratuite, soins remboursés et allocations logement a un niveau "
            "de vie bien plus élevé que son revenu primaire ne le laisse "
            "penser."),
           ("L’invisibilité d’une partie du dispositif",
            "Beaucoup de bénéficiaires ne perçoivent pas cette part en "
            "nature, ce qui contribue à la résistance à l’impôt : la "
            "redistribution invisible ne nourrit pas l’adhésion qu’elle "
            "justifierait.")],
      aut=[{'n': "Richard Musgrave",
            'i': "La redistribution est l’une des trois fonctions propres de "
                 "l’État, à côté de l’allocation et de la stabilisation."}],
      faits=[{'f': "En France, les écarts de niveau de vie par unité de "
                   "consommation en 2023 sont d’un facteur 18 avant "
                   "redistribution et d’un facteur 4 après ; 53 % des "
                   "ménages sont bénéficiaires nets.",
              'p': "C’est la mesure de référence de l’intensité redistributive "
                   "française, et le fait que la majorité des ménages y gagne "
                   "éclaire la base politique du dispositif."}],
      termes=['redistribution', 'prestations sociales', 'niveau de vie'],
      dos=['n22-redistribution', 'n22-protection-sociale']),

   nd('fiscalite', 'La fiscalité progressive et ses tensions', 'detail',
      "Chacun contribue selon ses moyens. Mais la TVA pèse davantage sur les "
      "bas revenus tout en rapportant 200 milliards.",
      grp=4, par='redistribution',
      defi="Le cours définit la justice fiscale comme le fait que chacun "
           "contribue selon ses moyens, et en déduit que l’impôt progressif "
           "est plus équitable car il réduit les inégalités. Un impôt "
           "progressif est un impôt dont le taux augmente avec le revenu. "
           "Mais tout système fiscal arbitre entre deux exigences — le "
           "rendement et la justice — qui ne désignent pas les mêmes "
           "instruments.",
      mec=[("La progressivité du barème",
            "Une personne gagnant 1 500 euros par mois paie un taux faible, "
            "une autre gagnant 5 000 euros un taux plus élevé : c’est le cas "
            "de l’impôt sur le revenu en France."),
           ("La pondération par la composition du ménage",
            "Le quotient familial divise le revenu imposable par le nombre de "
            "parts : dans un foyer de trois enfants, 40 000 divisé par 4 "
            "donne 10 000, donc un taux nul. L’équité consiste ici à traiter "
            "différemment des revenus identiques."),
           ("L’arbitrage rendement / justice",
            "La TVA pèse davantage sur les revenus les plus faibles, ce qui "
            "n’en fait pas un impôt juste, alors qu’elle procure à l’État 200 "
            "milliards de recettes : c’est la tension qui rend toute réforme "
            "fiscale difficile.")],
      aut=[{'n': "Arthur Laffer",
            'i': "Au-delà d’un certain niveau, une hausse du taux "
                 "d’imposition réduit les recettes fiscales."}],
      termes=['fiscalite progressive', 'impot sur le revenu',
              'quotient familial'],
      dos=['n22-fiscalite-progressive', 'n22-justice-sociale']),

   # --------------------------------------------- colonne 5 : ce qui résiste
   nd('assiette', 'La limite d’assiette : les stocks', 'limite',
      "Le système réduit les inégalités de revenus mais beaucoup moins celles "
      "de patrimoine : agir sur les stocks exige d’autres instruments.",
      grp=5,
      defi="La limite centrale du dispositif redistributif est une limite "
           "d’assiette. Le système fiscal et social réduit fortement les "
           "inégalités de revenus mais beaucoup moins celles de patrimoine : "
           "la concentration du capital et la hausse des grandes fortunes "
           "montrent que les inégalités structurelles persistent. Agir sur "
           "les stocks exige d’autres instruments que ceux qui agissent sur "
           "les flux.",
      mec=[("Pourquoi un impôt sur le flux n’atteint pas le stock",
            "Un patrimoine peut croître sans produire de revenu imposable "
            "lorsque la plus-value n’est pas réalisée : l’assiette du revenu "
            "ne capte pas l’enrichissement."),
           ("La régressivité au sommet",
            "La part des revenus effectivement soumise au barème progressif "
            "diminue à mesure que l’on monte dans la distribution, ce qui "
            "peut rendre le prélèvement effectif régressif au sommet."),
           ("Les instruments envisagés",
            "Une taxe plancher sur le patrimoine des très grandes fortunes, "
            "ou des réformes ciblées atteignant ce patrimoine sans les "
            "difficultés d’une taxe sur le stock.")],
      aut=[{'n': "Gabriel Zucman",
            'i': "Une taxe plancher sur le patrimoine des très grandes "
                 "fortunes permettrait de corriger la régressivité du haut de "
                 "la distribution."},
           {'n': "Xavier Jaravel",
            'i': "Trois réformes ciblées permettraient d’atteindre le "
                 "patrimoine des plus riches sans les difficultés d’une taxe "
                 "sur le stock."}],
      termes=['taxation du patrimoine', 'regressivite', 'grandes fortunes'],
      dos=['n22-inegalites-patrimoine', 'n22-rente']),

   nd('justice', 'Égalité, équité, justice sociale', 'debat',
      "Trois exigences distinctes : contribuer selon ses moyens, traiter "
      "différemment des situations différentes, et juger la répartition des "
      "gains d’une politique.",
      grp=5,
      defi="La justice sociale désigne l’exigence d’une répartition "
           "acceptable des revenus, des charges et des opportunités. Le cours "
           "ne la traite pas comme une théorie philosophique autonome mais la "
           "mobilise sous trois formes précises : la justice fiscale, définie "
           "comme le fait que chacun contribue selon ses moyens ; le pilier "
           "social du développement durable formalisé par le rapport "
           "Brundtland de 1987 ; et l’équité comme critère d’évaluation de la "
           "répartition des gains et des pertes d’une politique.",
      mec=[("Égalité et équité ne se confondent pas",
            "L’égalité traite tout le monde de la même manière ; l’équité "
            "traite différemment des situations différentes. Le quotient "
            "familial relève de la seconde, le barème unique de la première."),
           ("La justice entre générations",
            "Le rapport Brundtland ajoute une dimension temporelle : "
            "répondre aux besoins du présent sans compromettre la capacité "
            "des générations futures à répondre aux leurs."),
           ("L’équité comme critère d’évaluation des politiques",
            "Une politique efficace dont les gains sont captés par quelques-"
            "uns et les coûts supportés par d’autres peut être rejetée : "
            "l’acceptabilité est une condition d’efficacité, pas une "
            "considération extérieure.")],
      aut=[{'n': "Amartya Sen",
            'i': "L’évaluation du bien-être doit porter sur les capacités "
                 "réelles des personnes et non sur leurs seules ressources "
                 "monétaires."},
           {'n': "Pierre Rosanvallon",
            'i': "L’État-providence connaît une triple crise de financement, "
                 "d’efficacité et de légitimité."}],
      faits=[{'f': "Le rapport Brundtland de 1987 définit le développement "
                   "durable sur trois piliers : économique, social et "
                   "environnemental.",
              'p': "Le rapport inscrit la justice sociale dans un cadre à "
                   "trois dimensions et y ajoute une justice entre "
                   "générations."}],
      termes=['justice sociale', 'equite', 'etat providence'],
      dos=['n22-justice-sociale', 'n22-egalite-equite']),
  ],
  [
   ln('primaire', 'mesure', 'fournit la distribution à mesurer',
      "C’est la répartition primaire que les indicateurs décrivent d’abord : "
      "avant impôts et prestations, la distribution des revenus résulte du "
      "partage de la valeur ajoutée et de la structure des rémunérations.",
      'cause'),
   ln('patrimoine', 'mesure', 'exige une autre mesure',
      "Un indicateur calculé sur les revenus annuels ne dit rien de la "
      "concentration des stocks. Mesurer le patrimoine suppose de changer "
      "d’objet : ce n’est pas la même distribution, ni la même "
      "concentration.", 'conditionne'),
   ln('primaire', 'patrimoine', 'alimente',
      "La part de la valeur ajoutée qui va au profit, puis l’épargne qu’elle "
      "permet, alimentent l’accumulation patrimoniale : le partage du flux "
      "détermine progressivement la répartition du stock.", 'cause'),
   ln('mesure', 'echelles', 'se décompose en',
      "L’indice de Theil, parce qu’il est décomposable, permet de séparer ce "
      "qui provient des écarts entre pays de ce qui provient des écarts "
      "internes : sans cette décomposition, le paradoxe de la mondialisation "
      "reste invisible.", 'mesure'),
   ln('echelles', 'retour', 'documente',
      "La stagnation du 80ᵉ percentile mondial — la classe moyenne des pays "
      "développés — sur vingt ans est l’une des manifestations les plus "
      "nettes du retour des inégalités internes dans les économies avancées.",
      'renforce'),
   ln('kuznets', 'retour', 'est contredite par',
      "Des économies parvenues au stade avancé voient leurs inégalités "
      "remonter depuis les années 1980 : c’est le fait qui invalide "
      "l’automaticité de la phase descendante, sans invalider le mécanisme de "
      "la phase ascendante.", 'oppose'),
   ln('kuznets', 'redistribution', 'reposait surtout sur',
      "Le cours écrit que la phase descendante tient à l’éducation, au "
      "progrès technique et à l’urbanisation, « mais surtout » à la "
      "redistribution : la baisse attendue était institutionnelle avant "
      "d’être mécanique.", 'conditionne'),
   ln('retour', 'redistribution', 's’explique par son reflux',
      "Si la baisse reposait sur la redistribution, la modification des "
      "systèmes redistributifs depuis les années 1980 suffit à expliquer le "
      "retournement : aucun mécanisme économique nouveau n’est nécessaire.",
      'cause'),
   ln('redistribution', 'fiscalite', 'passe par',
      "La redistribution n’opère que par des prélèvements dont le barème "
      "décide de l’effet : un impôt progressif réduit les écarts, un impôt "
      "proportionnel sur la consommation les aggrave.", 'conditionne'),
   ln('fiscalite', 'assiette', 'bute sur l’assiette',
      "La progressivité s’applique au revenu déclaré. Un patrimoine qui "
      "s’apprécie sans produire de revenu imposable échappe au barème : la "
      "limite n’est pas celle des taux mais celle de l’assiette.", 'limite'),
   ln('patrimoine', 'assiette', 'échappe largement à l’impôt',
      "Le système fiscal et social réduit les inégalités de revenus mais "
      "beaucoup moins celles de patrimoine : c’est le constat qui justifie "
      "les propositions de taxation des très grandes fortunes.", 'limite'),
   ln('redistribution', 'justice', 'se justifie par',
      "Prélever et redistribuer suppose un critère : contribuer selon ses "
      "moyens. La justice fiscale est la forme sous laquelle le cours "
      "mobilise la justice sociale, et elle est immédiatement opératoire.",
      'conditionne'),
   ln('assiette', 'justice', 'relance le débat',
      "Lorsque le prélèvement effectif devient régressif au sommet, "
      "l’exigence « contribuer selon ses moyens » cesse d’être satisfaite : "
      "la limite technique devient une question de légitimité.", 'cause'),
   ln('echelles', 'justice', 'déplace la question à l’échelle mondiale',
      "Si les écarts se réduisent entre nations mais se creusent en leur "
      "sein, l’exigence de justice ne se pose plus au même niveau que les "
      "instruments qui pourraient y répondre, lesquels restent nationaux.",
      'limite'),
   ln('retour', 'justice', 'alimente la contestation',
      "La concentration au sommet et la stagnation des classes moyennes des "
      "pays développés expliquent la montée des tensions sociales et "
      "politiques : l’inégalité devient un enjeu de légitimité du système "
      "économique lui-même.", 'cause'),
  ],
  bandes=[(1, 'Où les écarts se forment'), (2, 'Comment on les mesure'),
          (3, 'Comment ils évoluent'), (4, 'Les instruments'),
          (5, 'Ce qui résiste')],
  fam='Société, inégalités et transversal')
