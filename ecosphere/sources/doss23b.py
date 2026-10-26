# -*- coding: utf-8 -*-
"""Ensemble 23 — Structure sociale et mobilité (2/3)."""

from doss_base import d

d('n23-moyennisation', 23, "Moyennisation",
  "La montée d’une classe moyenne qui resserre la structure sociale, et sa remise en cause",
  "La moyennisation désigne le processus par lequel la croissance fait "
  "monter une large classe moyenne et resserre l’éventail des positions "
  "sociales. Le terme n’apparaît pas dans les cours et ce point de "
  "vocabulaire doit être signalé ; mais le processus y est traité deux "
  "fois : la phase descendante de la courbe de Kuznets en fait un résultat "
  "de la croissance avancée, avec la montée de la classe moyenne parmi ses "
  "mécanismes, et l’analyse de Milanovic en documente l’interruption.",
  "Le cours construit la moyennisation comme la phase 2 de la courbe de "
  "Kuznets. Observant l’évolution des inégalités aux États-Unis entre 1913 "
  "et 1948, Kuznets formule en 1955 l’hypothèse d’une relation en cloche "
  "entre croissance et inégalités : les inégalités augmentent au début du "
  "développement puis diminuent à un stade avancé, soit une courbe en U "
  "inversé. La phase de hausse s’explique par le passage d’une économie "
  "agricole à une économie industrielle, avec des différences de "
  "productivité importantes et des salaires industriels plus élevés : les "
  "écarts se creusent entre secteurs. La phase de baisse repose sur quatre "
  "transformations — généralisation de l’éducation, diffusion du progrès "
  "technique, urbanisation complète, montée de la classe moyenne — mais le "
  "cours insiste par un « mais surtout » sur trois facteurs politiques : le "
  "développement de la redistribution, la hausse des recettes fiscales et "
  "la mise en place de politiques sociales. L’État corrige les inégalités "
  "produites par le marché. Autrement dit, la moyennisation n’est pas dans "
  "le cours un effet spontané de la croissance mais le produit conjoint "
  "d’un changement de structure productive et d’une construction "
  "politique. Le cours tire immédiatement la conséquence : la réduction des "
  "inégalités n’est pas automatique, elle dépend du niveau de "
  "redistribution, du système fiscal, des institutions et du degré de "
  "protection sociale — les inégalités sont aussi un choix de société. "
  "Vient ensuite l’interruption du processus. Depuis les années 1980, dans "
  "de nombreux pays développés, on observe une hausse des inégalités de "
  "revenus, une forte concentration des patrimoines et une explosion du "
  "top 1 % : la dynamique récente semble contredire la phase descendante "
  "prévue par Kuznets. L’analyse de Milanovic apporte la mesure la plus "
  "précise de ce retournement : sur la courbe de l’éléphant, la classe "
  "moyenne des pays émergents connaît une croissance de ses revenus de +70 "
  "à +80 % entre 1988 et 2008, tandis que les classes moyennes "
  "occidentales, situées autour du 80e percentile mondial, enregistrent une "
  "croissance réelle proche de 0 % et développent un sentiment de "
  "déclassement. La moyennisation change donc d’échelle : elle se poursuit "
  "à l’échelle mondiale, portée par la Chine, l’Inde et l’Asie, et "
  "s’interrompt à l’échelle des sociétés occidentales. Le cours relie "
  "enfin ce retournement aux conséquences politiques : Rodrik soutient que "
  "la réponse au déclassement des classes moyennes ne peut se limiter à la "
  "réindustrialisation et que, dans des économies majoritairement "
  "tertiaires, la priorité est d’élever la productivité et la qualité des "
  "emplois de services.",
  [("La croissance commence par écarter les positions",
    "Le passage d’une économie agricole à une économie industrielle crée "
    "des différences de productivité importantes et des salaires "
    "industriels plus élevés : les écarts se creusent entre secteurs, "
    "première phase de la courbe de Kuznets."),
   ("La diffusion de l’éducation réduit la rareté des qualifications",
    "La généralisation de l’éducation et la diffusion du progrès technique "
    "élargissent le nombre de travailleurs qualifiés. La prime attachée à "
    "la qualification se réduit mécaniquement lorsque celle-ci cesse "
    "d’être rare, ce qui resserre l’éventail des salaires."),
   ("L’urbanisation complète efface le dualisme sectoriel",
    "Tant que coexistent un secteur agricole peu productif et un secteur "
    "industriel productif, l’écart entre secteurs nourrit l’inégalité. "
    "L’urbanisation complète supprime cette source : la population active "
    "se concentre dans les secteurs les plus productifs."),
   ("Une classe moyenne nombreuse apparaît au centre de la distribution",
    "Le cours place la montée de la classe moyenne parmi les mécanismes de "
    "la phase descendante. Un groupe central nombreux réduit la part du "
    "revenu captée aux extrêmes et resserre la distribution autour de la "
    "médiane."),
   ("Mais surtout l’État corrige la répartition de marché",
    "Le cours souligne le rôle décisif du développement de la "
    "redistribution, de la hausse des recettes fiscales et de la mise en "
    "place de politiques sociales : l’État corrige les inégalités produites "
    "par le marché, et c’est le facteur principal."),
   ("Le processus s’interrompt quand le soutien politique faiblit",
    "La réduction des inégalités n’est pas automatique : elle dépend du "
    "niveau de redistribution, du système fiscal, des institutions et du "
    "degré de protection sociale. Depuis les années 1980, hausse des "
    "inégalités de revenus, concentration des patrimoines et explosion du "
    "top 1 % contredisent la phase descendante."),
   ("La moyennisation se déplace vers les pays émergents",
    "Entre 1988 et 2008, la classe moyenne des pays émergents gagne +70 à "
    "+80 % de revenu réel, tandis que les classes moyennes occidentales, "
    "autour du 80e percentile mondial, stagnent à une croissance proche de "
    "0 % et éprouvent un sentiment de déclassement.")],
  [{'a': "La croissance avancée dispose de mécanismes propres de "
         "resserrement : généralisation de l’éducation, diffusion du "
         "progrès technique, urbanisation complète et montée de la classe "
         "moyenne agissent tous dans le sens d’une réduction des écarts.",
    'cond': "Ces mécanismes supposent que la qualification se diffuse plus "
            "vite que la demande de qualification et que le dualisme "
            "sectoriel s’efface réellement, ce que Kuznets observe aux "
            "États-Unis entre 1913 et 1948.",
    'lim': "Le cours montre que cette séquence n’est pas reproductible à "
           "volonté : l’évolution récente des économies développées invite "
           "à nuancer fortement la conclusion, et la hausse des inégalités "
           "depuis les années 1980 contredit la phase descendante."},
   {'a': "La moyennisation est d’abord une construction politique : le "
         "cours écrit « mais surtout » avant d’énumérer le développement de "
         "la redistribution, la hausse des recettes fiscales et la mise en "
         "place de politiques sociales, et conclut que l’État corrige les "
         "inégalités produites par le marché.",
    'cond': "Il faut que l’État dispose des recettes nécessaires et d’une "
            "légitimité suffisante pour redistribuer, donc d’un système "
            "fiscal, d’institutions et d’un degré de protection sociale "
            "adéquats, les quatre déterminants que le cours énumère.",
    'lim': "Cette dépendance est aussi la fragilité du processus : si les "
           "inégalités sont un choix de société, la moyennisation peut être "
           "défaite par un autre choix, sans qu’aucun mécanisme économique "
           "ne la rétablisse automatiquement."},
   {'a': "La moyennisation n’a pas cessé, elle a changé d’échelle : la "
         "classe moyenne des pays émergents gagne +70 à +80 % entre 1988 et "
         "2008, essentiellement en Chine, en Inde et en Asie, ce qui "
         "explique la réduction des inégalités entre pays.",
    'cond': "La mesure est fiable car les revenus sont exprimés en termes "
            "réels, déflatés, et en parité de pouvoir d’achat, de sorte que "
            "les résultats ne sont biaisés ni par l’inflation ni par les "
            "taux de change financiers.",
    'lim': "Milanovic établit un paradoxe : les inégalités entre pays "
           "diminuent mais les inégalités à l’intérieur des pays "
           "augmentent. La moyennisation mondiale coexiste donc avec une "
           "divergence au sein des sociétés nationales, et l’une ne "
           "compense pas l’autre pour ceux qui subissent la seconde."},
   {'a': "La remise en cause de la moyennisation occidentale a des effets "
         "politiques majeurs, ce qui en fait un objet d’analyse "
         "économique : le cours montre que la faible progression des "
         "revenus des classes populaires nourrit un sentiment de "
         "déclassement que des forces politiques hostiles à la "
         "mondialisation peuvent exploiter.",
    'cond': "L’enchaînement suppose que les individus évaluent leur "
            "situation en termes relatifs et locaux : le cours précise "
            "qu’ils raisonnent d’abord à partir de leur propre situation, "
            "et non à partir du gain mondial agrégé.",
    'lim': "Le sentiment de déclassement n’est pas une mesure du "
           "déclassement : le cours note que les gains sont relatifs quand "
           "ils sont exprimés en pourcentage et absolus quand ils sont "
           "exprimés en valeur, le top 1 % captant la plus grande part du "
           "surplus mondial en valeur."}],
  [{'t': "La baisse des inégalités serait presque mécanique à long terme : "
         "il suffirait d’atteindre un stade avancé de développement pour "
         "que l’éventail se resserre de lui-même.",
    'qui': "Lecture mécanique de la courbe de Kuznets, que le cours "
           "identifie et récuse explicitement.",
    'rep': "Le cours répond en deux temps. D’abord la réduction des "
           "inégalités n’est pas automatique : elle dépend du niveau de "
           "redistribution, du système fiscal, des institutions et du degré "
           "de protection sociale. Ensuite les faits : depuis les années "
           "1980, hausse des inégalités de revenus, forte concentration des "
           "patrimoines et explosion du top 1 %."},
   {'t': "Parler de moyennisation à l’échelle nationale n’a plus de sens : "
         "l’analyse strictement nationale de Kuznets est insuffisante et il "
         "faut raisonner à l’échelle globale, où la classe moyenne progresse "
         "fortement.",
    'qui': "Le cours lui-même, qui écrit que les transformations "
           "contemporaines imposent un changement d’échelle d’analyse, puis "
           "introduit Milanovic.",
    'rep': "Le changement d’échelle est nécessaire mais ne supprime pas la "
           "question nationale : Milanovic établit que les inégalités à "
           "l’intérieur des pays augmentent, et le cours relie cette "
           "divergence interne à des conséquences politiques majeures dans "
           "les pays avancés. Les deux échelles doivent être tenues "
           "ensemble."},
   {'t': "La stagnation des classes moyennes occidentales serait un "
         "problème de perception : en gains absolus, le niveau de vie moyen "
         "continue d’augmenter, et la plainte porte sur des positions "
         "relatives.",
    'rep': "Le cours fournit les deux lectures et refuse de réduire l’une à "
           "l’autre : en gains relatifs la classe moyenne émergente connaît "
           "la plus forte hausse, en gains absolus le top 1 % capte la plus "
           "grande part du surplus mondial. Il documente par ailleurs un "
           "écart objectif : aux États-Unis le PIB réel par habitant "
           "progresse beaucoup plus rapidement que le revenu médian des "
           "ménages."}],
  [{'n': "Simon Kuznets",
    'i': "La relation entre croissance et inégalités suit une courbe en "
         "cloche : hausse au début du développement, baisse à un stade "
         "avancé.",
    'p': "Hypothèse formulée en 1955 à partir de l’observation des "
         "inégalités aux États-Unis entre 1913 et 1948. La phase "
         "descendante repose sur la généralisation de l’éducation, la "
         "diffusion du progrès technique, l’urbanisation complète et la "
         "montée de la classe moyenne, mais le cours souligne surtout le "
         "rôle du développement de la redistribution, de la hausse des "
         "recettes fiscales et des politiques sociales."},
   {'n': "Branko Milanovic",
    'i': "Les inégalités entre pays diminuent mais les inégalités à "
         "l’intérieur des pays augmentent.",
    'p': "Dans Global Inequality (2016), il construit la courbe de "
         "l’éléphant pour la période 1988-2008 : en abscisse la population "
         "mondiale classée par revenu initial, en ordonnée le taux de "
         "croissance du revenu réel, les revenus étant déflatés et exprimés "
         "en parité de pouvoir d’achat. La classe moyenne émergente gagne "
         "+70 à +80 %, les plus pauvres environ +15 %, le top 1 % environ "
         "+60 %."},
   {'n': "Branko Milanovic",
    'i': "Les classes moyennes occidentales, autour du 80e percentile "
         "mondial, connaissent une croissance réelle proche de 0 %.",
    'p': "Le cours en tire l’explication du sentiment de déclassement et de "
         "la montée des tensions sociales et politiques. Il ajoute la "
         "distinction décisive entre gains relatifs, où la classe moyenne "
         "émergente est la plus favorisée, et gains absolus, où le top 1 % "
         "capte la plus grande part du surplus mondial, ce qui interdit de "
         "conclure trop vite à une mondialisation égalisatrice."},
   {'n': "Dani Rodrik",
    'i': "La réponse au déclassement des classes moyennes ne peut se "
         "limiter à la réindustrialisation.",
    'p': "Dans des économies majoritairement tertiaires, la priorité doit "
         "être d’élever la productivité et la qualité des emplois de "
         "services afin de permettre une progression durable des "
         "rémunérations. Le cours note que les technologies numériques et "
         "l’intelligence artificielle peuvent y contribuer, mais que la "
         "réponse politique dominante s’oriente ailleurs."}],
  [{'f': "Kuznets observe l’évolution des inégalités aux États-Unis entre "
         "1913 et 1948 et en tire, en 1955, l’hypothèse d’une courbe en U "
         "inversé.",
    'p': "La thèse de la moyennisation repose donc sur une base empirique "
         "étroite : un pays, trente-cinq ans, une période marquée par deux "
         "guerres et la crise de 1929. C’est l’argument le plus solide "
         "contre sa généralisation."},
   {'f': "Entre 1988 et 2008, la classe moyenne des pays émergents gagne "
         "+70 à +80 % de revenu réel, contre environ +15 % pour les plus "
         "pauvres et environ +60 % pour le top 1 % mondial.",
    'p': "La moyennisation existe bien mais en Chine, en Inde et en Asie. "
         "Le creux de la courbe, autour du 80e percentile, correspond "
         "précisément aux classes moyennes des pays riches."},
   {'f': "Depuis les années 1980, les pays développés connaissent une "
         "hausse des inégalités de revenus, une forte concentration des "
         "patrimoines et une explosion du top 1 %.",
    'p': "Ces trois faits contredisent ensemble la phase descendante "
         "prévue par Kuznets et confirment que le resserrement de la "
         "structure sociale dépendait de conditions politiques et non d’une "
         "loi de la croissance."},
   {'f': "Aux États-Unis, le PIB réel par habitant progresse beaucoup plus "
         "rapidement que le revenu médian des ménages, et les 10 % les plus "
         "pauvres connaissent une évolution beaucoup plus faible et plus "
         "instable.",
    'p': "L’écart entre croissance moyenne et revenu médian prouve que la "
         "croissance peut se poursuivre sans alimenter la classe moyenne : "
         "la moyennisation n’est pas un sous-produit automatique de "
         "l’enrichissement global."}],
  [{'q': "La croissance réduit-elle spontanément les inégalités ?",
    'f': "La courbe de Kuznets semble l’affirmer : après une phase de "
         "hausse liée au dualisme entre agriculture et industrie, la phase "
         "avancée voit les inégalités diminuer sous l’effet de la "
         "généralisation de l’éducation, de la diffusion du progrès "
         "technique, de l’urbanisation et de la montée de la classe "
         "moyenne. Mais le cours ajoute un « mais surtout » décisif : "
         "développement de la redistribution, hausse des recettes fiscales, "
         "politiques sociales. La baisse des inégalités est donc un "
         "résultat institutionnel, et le retour des inégalités depuis les "
         "années 1980 le confirme a contrario.",
    'r': "Ce plan est le plus rigoureux parce qu’il suit la structure même "
         "du cours : exposé du mécanisme, hiérarchisation interne des "
         "facteurs, puis réfutation par les faits récents. Il permet de "
         "conclure que les inégalités sont aussi un choix de société, "
         "formule explicite du cours.",
    'ex': "L’explosion du top 1 % dans les pays développés depuis les "
          "années 1980, en pleine phase avancée de développement."},
   {'q': "La mondialisation a-t-elle fait disparaître les classes "
         "moyennes ?",
    'f': "Elle les a déplacées. La courbe de l’éléphant montre que la "
         "classe moyenne des pays émergents gagne +70 à +80 % de revenu "
         "réel entre 1988 et 2008, essentiellement en Chine, en Inde et en "
         "Asie, ce qui explique la réduction des inégalités entre pays. "
         "Dans le même temps, les classes moyennes occidentales, situées "
         "autour du 80e percentile mondial, enregistrent une croissance "
         "proche de 0 %. La moyennisation se poursuit donc à l’échelle "
         "mondiale et s’interrompt à l’échelle nationale occidentale : "
         "c’est le paradoxe de Milanovic.",
    'r': "Le raisonnement est solide parce qu’il repose sur une mesure "
         "méthodologiquement explicite — revenus déflatés et en parité de "
         "pouvoir d’achat — et parce qu’il articule les deux échelles au "
         "lieu d’en privilégier une.",
    'ex': "Le creux de la courbe de l’éléphant au 80e percentile, qui "
          "correspond aux classes moyennes des pays riches."},
   {'q': "Le sentiment de déclassement des classes moyennes est-il "
         "fondé ?",
    'f': "Il faut distinguer la mesure et la perception, puis montrer "
         "qu’elles se rejoignent. En gains relatifs, les classes moyennes "
         "occidentales stagnent autour de 0 % quand les émergents gagnent "
         "+70 à +80 % : la perte est relative. Mais le cours fournit aussi "
         "un écart objectif, le PIB réel par habitant américain progressant "
         "beaucoup plus vite que le revenu médian des ménages. Le sentiment "
         "de déclassement repose donc sur un fait mesurable, ce qui "
         "explique ses conséquences politiques : soutien aux droits de "
         "douane, à la relocalisation et à la préférence nationale.",
    'r': "Ce plan échappe au reproche de psychologisme en appuyant la "
         "perception sur deux séries distinctes, l’une internationale "
         "(courbe de l’éléphant), l’autre nationale (écart entre PIB par "
         "habitant et revenu médian).",
    'ex': "Aux États-Unis, le soutien de certaines anciennes régions "
          "industrielles aux politiques protectionnistes."}],
  voisins=['n23-polarisation-sociale', 'n23-declassement',
           'n23-classes-sociales', 'n22-courbe-kuznets',
           'n22-inegalites-entre-et-au-sein'])

d('n23-polarisation-sociale', 23, "Polarisation sociale",
  "Quand la distribution se vide par le milieu : mesure, causes, conséquences",
  "La polarisation sociale désigne l’écartement des extrémités d’une "
  "distribution au détriment de son centre. Le cours en fait un objet de "
  "mesure explicite : le coefficient de Palma, qui compare la part du "
  "revenu détenue par les 10 % les plus riches à celle des 50 % les plus "
  "pauvres, est présenté comme un indicateur de polarisation sociale. Le "
  "cours en documente aussi les causes — mondialisation, chaînes de valeur, "
  "spécialisation — et les conséquences politiques.",
  "Le cours introduit la polarisation par un problème de mesure. Le rapport "
  "interdécile D9/D1 compare le revenu plancher des 10 % les plus riches au "
  "revenu plafond des 10 % les plus pauvres, mais il ne capte pas bien ce "
  "qui se passe au sommet. On introduit donc des indicateurs plus sensibles "
  "à la polarisation entre une élite et une large partie de la population : "
  "le coefficient de Palma compare la part du revenu détenue par les 10 % "
  "les plus riches à la part détenue par les 50 % les plus pauvres. Il met "
  "en évidence la concentration du revenu au sommet et le décrochage "
  "potentiel de la moitié inférieure, et le cours le qualifie "
  "explicitement d’indicateur de polarisation sociale : plus sensible que "
  "le rapport interdécile aux transformations contemporaines du sommet de "
  "la distribution, il met en évidence la polarisation croissante des "
  "sociétés entre une élite restreinte et une large base de la population. "
  "Son intérêt analytique est double : il capte mieux l’explosion du top "
  "1 %, la montée des très hauts revenus et les transformations liées à la "
  "mondialisation et à la financiarisation, et il offre une lecture "
  "politique immédiate du rapport entre l’élite et la majorité. Le cours "
  "complète par le coefficient de Gini, indicateur synthétique construit "
  "sur la courbe de Lorenz, en notant sa limite propre : il est peu "
  "sensible au top 1 %. Les chapitres de seconde année fournissent les "
  "causes. La polarisation des revenus est explicitement attribuée à la "
  "mondialisation, dont les effets sont très inégalement répartis : forte "
  "progression des hauts revenus, progression des revenus dans de nombreux "
  "pays émergents, stagnation des classes moyennes des pays avancés. Le "
  "mécanisme productif est la courbe du sourire : le creusement de cette "
  "courbe traduit une polarisation croissante de la valeur, les activités "
  "immatérielles et qualifiées captant une part croissante des gains alors "
  "que l’assemblage, soumis à une forte concurrence entre pays à bas "
  "salaires, génère relativement moins de valeur. L’enchaînement est "
  "précisé : concurrence entre territoires ↑ → prix ou rémunération de la "
  "tâche ↓ → valeur ajoutée de l’assemblage ↓. S’y ajoute la spécialisation "
  "commerciale : le travail peu qualifié exposé à la concurrence "
  "internationale est moins demandé, d’où baisse des salaires relatifs, "
  "chômage possible, désindustrialisation locale et polarisation des "
  "rémunérations. Enfin, la polarisation produit des effets politiques : "
  "les pertes sont très fortes mais concentrées sur certains individus et "
  "territoires, les gains faibles mais diffus, de sorte que les deux ne se "
  "compensent pas nécessairement du point de vue politique.",
  [("La mesure usuelle manque le sommet",
    "Le rapport interdécile D9/D1 ne capte pas bien ce qui se passe au "
    "sommet de la distribution, et le coefficient de Gini est peu sensible "
    "au top 1 %. Un indicateur spécifique est donc nécessaire pour saisir "
    "l’écartement entre une élite et le reste."),
   ("Le coefficient de Palma rend la polarisation visible",
    "Il compare la part du revenu détenue par les 10 % les plus riches à "
    "celle des 50 % les plus pauvres. Il met ainsi en évidence à la fois la "
    "concentration du revenu au sommet et le décrochage potentiel de la "
    "moitié inférieure de la population."),
   ("La valeur se concentre aux extrémités des chaînes productives",
    "Le creusement de la courbe du sourire traduit une polarisation de la "
    "valeur : les activités immatérielles et qualifiées, conception et "
    "services avancés en amont, marque et distribution en aval, captent une "
    "part croissante des gains."),
   ("L’assemblage subit la concurrence entre territoires",
    "L’enchaînement est explicite : concurrence entre territoires ↑ → prix "
    "ou rémunération de la tâche ↓ → valeur ajoutée de l’assemblage ↓. Les "
    "tâches les plus substituables voient leur rémunération comprimée par "
    "la mise en concurrence des sites de production."),
   ("La spécialisation déplace la demande de travail",
    "Le travail peu qualifié exposé à la concurrence internationale est "
    "moins demandé : salaires relatifs ↓, chômage possible, "
    "désindustrialisation locale, polarisation des rémunérations. Les "
    "compétences correspondent moins aux nouvelles spécialisations des "
    "économies avancées."),
   ("Les pertes se concentrent, les gains se diffusent",
    "Le gain du consommateur est faible mais diffus sur beaucoup de "
    "ménages ; la perte d’emploi est très forte mais concentrée sur "
    "certains individus et territoires. Les deux ne se compensent donc pas "
    "nécessairement, ce qui transforme la polarisation économique en "
    "conflit politique.")],
  [{'a': "La polarisation exige un indicateur dédié, et le coefficient de "
         "Palma le fournit : en comparant les 10 % les plus riches aux 50 % "
         "les plus pauvres, il capte mieux l’explosion du top 1 %, la "
         "montée des très hauts revenus et les transformations liées à la "
         "mondialisation et à la financiarisation.",
    'cond': "L’indicateur suppose des données fiables sur les très hauts "
            "revenus, qui sont précisément les plus difficiles à mesurer, "
            "et une définition stable des parts comparées.",
    'lim': "Un ratio entre deux parts ne dit rien de ce qui se passe entre "
           "elles : le coefficient de Palma ignore par construction les "
           "40 % intermédiaires, dont le cours note par ailleurs que la "
           "part est restée stable depuis 1980."},
   {'a': "La polarisation a une cause productive identifiable : le "
         "creusement de la courbe du sourire concentre la valeur sur les "
         "activités immatérielles et qualifiées tandis que l’assemblage, "
         "soumis à une forte concurrence entre pays à bas salaires, génère "
         "relativement moins de valeur.",
    'cond': "Le mécanisme suppose que les tâches d’assemblage soient "
            "effectivement substituables entre territoires et que les "
            "activités de conception et de marque restent protégées par des "
            "actifs immatériels difficiles à répliquer.",
    'lim': "Le cours relève un mouvement contraire : le raccourcissement "
           "des chaînes de valeur mondiales, dont la part recule vers 40 à "
           "45 %. Si la fragmentation se réduit, la géographie de la "
           "polarisation se modifie sans que l’inégalité disparaisse."},
   {'a': "La polarisation est d’autant plus conflictuelle que la "
         "distribution de ses coûts est asymétrique : la perte d’emploi est "
         "très forte mais concentrée sur certains individus et territoires, "
         "alors que le gain de pouvoir d’achat est faible mais diffus sur "
         "beaucoup de ménages.",
    'cond': "L’argument tient parce que les individus raisonnent d’abord à "
            "partir de leur propre situation : le cours souligne que leur "
            "expliquer l’enrichissement de classes moyennes dans d’autres "
            "pays ne suffit pas à rendre la mondialisation politiquement "
            "acceptable.",
    'lim': "L’asymétrie de perception n’établit pas que le bilan agrégé "
           "soit négatif. Le cours maintient qu’un gain économique mondial "
           "existe, mais qu’il ne garantit pas son acceptabilité politique : "
           "deux questions distinctes qu’il ne faut pas confondre."},
   {'a': "La polarisation peut être corrigée, puisqu’elle dépend du niveau "
         "de redistribution, du système fiscal, des institutions et du "
         "degré de protection sociale, comme le montre la discussion des "
         "limites de la courbe de Kuznets.",
    'cond': "La correction exige des instruments adaptés au haut de la "
            "distribution : le cours montre que les écarts de niveau de vie "
            "passent d’un rapport de 18 avant redistribution à 4 après, "
            "preuve que l’outil fiscal et social agit effectivement.",
    'lim': "Le haut de la distribution résiste davantage : le patrimoine "
           "des 10 % les plus riches atteint 2 612 milliards d’euros en "
           "2025, soit 42 % du PIB contre 6 % en 1996, évolution que la "
           "redistribution des revenus ne touche pas."}],
  [{'t': "La polarisation serait un artefact d’indicateur : en choisissant "
         "un ratio qui compare les 10 % du haut aux 50 % du bas, on "
         "construit mécaniquement un écart spectaculaire qu’un indicateur "
         "synthétique ne montrerait pas.",
    'rep': "Le cours anticipe l’objection en présentant ensemble plusieurs "
           "indicateurs et leurs limites respectives : le rapport "
           "interdécile ne capte pas le sommet, le Gini est insensible au "
           "top 1 %, le Palma est sensible aux transformations "
           "contemporaines du sommet. Ce n’est pas un choix arbitraire mais "
           "une réponse à une insuffisance identifiée."},
   {'t': "La polarisation mondiale serait en réalité une convergence : les "
         "inégalités entre pays diminuent, la classe moyenne émergente "
         "gagnant +70 à +80 % de revenu réel entre 1988 et 2008.",
    'qui': "Lecture appuyée sur la courbe de l’éléphant de Milanovic, que "
           "le cours expose intégralement.",
    'rep': "Milanovic établit précisément un double mouvement : les "
           "inégalités entre pays diminuent, les inégalités à l’intérieur "
           "des pays augmentent. La convergence internationale et la "
           "polarisation nationale sont deux faces du même processus, et le "
           "cours refuse de solder l’une par l’autre."},
   {'t': "La polarisation des rémunérations serait un coût d’ajustement "
         "transitoire : les travailleurs se redéploieraient vers les "
         "secteurs où le pays est compétitif, et l’écart se refermerait.",
    'rep': "Le cours documente la persistance : le choc chinois s’explique "
           "par la faible mobilité géographique, des compétences "
           "spécifiques, la perte de revenus locaux, le déclin des "
           "commerces, la baisse de l’investissement et des effets "
           "multiplicateurs locaux. Il ajoute que la mobilité théorique des "
           "facteurs n’équivaut pas à la mobilité réelle des travailleurs."}],
  [{'n': "Palma",
    'i': "Comparer la part du revenu des 10 % les plus riches à celle des "
         "50 % les plus pauvres mesure la polarisation d’une société.",
    'p': "Le cours présente ce coefficient comme la réponse à une "
         "insuffisance du rapport interdécile, qui ne capte pas bien ce qui "
         "se passe au sommet. Il met en évidence la concentration du revenu "
         "au sommet et le décrochage potentiel de la moitié inférieure, et "
         "il est qualifié d’indicateur de polarisation sociale, plus "
         "sensible aux transformations contemporaines du haut de la "
         "distribution."},
   {'n': "Max Lorenz",
    'i': "La distribution des revenus peut être représentée par une courbe "
         "cumulative dont l’écart à la diagonale mesure l’inégalité.",
    'p': "Le cours construit le coefficient de Gini sur cette courbe. "
         "L’intérêt pour la polarisation est indirect mais réel : il permet "
         "de comprendre pourquoi un indicateur synthétique global peut "
         "rester stable alors que la polarisation augmente, puisque deux "
         "distributions différentes peuvent produire des aires comparables."},
   {'n': "Branko Milanovic",
    'i': "Les inégalités entre pays diminuent tandis que les inégalités à "
         "l’intérieur des pays augmentent.",
    'p': "Dans Global Inequality (2016), la courbe de l’éléphant montre "
         "+70 à +80 % pour la classe moyenne émergente, environ +15 % pour "
         "les plus pauvres, environ +60 % pour le top 1 % dont la moitié "
         "environ est américaine, et une croissance proche de 0 % pour les "
         "classes moyennes occidentales au 80e percentile. Le cours parle "
         "d’une montée d’une ploutocratie mondiale."},
   {'n': "Pierre-Noël Giraud",
    'i': "Les effets de la mondialisation sont très inégalement répartis "
         "entre les groupes sociaux.",
    'p': "Le cours réunit son analyse à celles de Milanovic et d’Acemoglu "
         "pour établir une convergence de diagnostic : forte progression "
         "des hauts revenus, progression des revenus dans de nombreux pays "
         "émergents, stagnation des classes moyennes des pays avancés. "
         "C’est cette répartition inégale des gains et des pertes qui "
         "explique la montée des inégalités dans les pays avancés."},
   {'n': "Daron Acemoglu",
    'i': "La répartition des gains de la mondialisation dépend des "
         "positions occupées et non d’un effet uniforme.",
    'p': "Le cours l’associe à Giraud et à Milanovic sur ce point de "
         "convergence. Son apport propre, développé ailleurs dans les "
         "chapitres avec James Robinson, porte sur les institutions : les "
         "institutions inclusives favorisent innovation, investissement, "
         "mobilité sociale et entrepreneuriat, les institutions extractives "
         "freinent l’initiative et la diffusion du progrès."}],
  [{'f': "Le coefficient de Palma compare la part du revenu des 10 % les "
         "plus riches à celle des 50 % les plus pauvres, et le cours le "
         "qualifie d’indicateur de polarisation sociale.",
    'p': "La polarisation n’est pas une impression mais une grandeur "
         "construite : le choix de comparer un décile supérieur à la moitié "
         "inférieure de la population traduit directement l’hypothèse d’un "
         "décrochage entre une élite et une large base."},
   {'f': "Le coefficient de Gini vaut environ 0,29 en France, un pays "
         "égalitaire se situant entre 0,25 et 0,30 et un pays très "
         "inégalitaire entre 0,45 et 0,60 ; mais le Gini est insensible au "
         "top 1 %.",
    'p': "Un même niveau de Gini peut recouvrir des structures très "
         "différentes : c’est l’argument décisif en faveur d’indicateurs de "
         "polarisation, et une mise en garde contre la comparaison de pays "
         "par ce seul chiffre."},
   {'f': "Depuis 1980, la part des 10 % les plus riches augmente, celle des "
         "50 % les plus pauvres stagne, celle des 40 % intermédiaires reste "
         "stable, et le top 1 % explose.",
    'p': "La distribution ne se déforme pas uniformément : le mouvement est "
         "exactement celui que mesure le coefficient de Palma, un sommet "
         "qui monte et une moitié inférieure qui décroche, le milieu étant "
         "relativement épargné."},
   {'f': "En France, le patrimoine des 10 % les plus riches atteint 2 612 "
         "milliards d’euros en 2025, soit environ 42 % du PIB contre 6 % en "
         "1996.",
    'p': "La polarisation est plus marquée sur les patrimoines que sur les "
         "revenus, parce que le patrimoine est un stock soumis à une "
         "logique cumulative, alors que le revenu est un flux que la "
         "redistribution peut corriger chaque année."}],
  [{'q': "Comment mesurer l’inégalité d’une société ?",
    'f': "Aucun indicateur ne suffit, et c’est ce que le cours démontre en "
         "les présentant en série. Le rapport interdécile D9/D1 est simple "
         "mais ne capte pas bien ce qui se passe au sommet. Le coefficient "
         "de Gini est synthétique mais insensible au top 1 % et muet sur "
         "l’origine des écarts. Le coefficient de Palma, en comparant les "
         "10 % les plus riches aux 50 % les plus pauvres, saisit la "
         "polarisation entre une élite et une large base, mais ignore par "
         "construction les 40 % intermédiaires. Le choix de l’indicateur "
         "est donc le choix d’une question.",
    'r': "Ce plan est le plus solide parce qu’il suit la progression "
         "explicite du cours, chaque indicateur étant introduit comme "
         "réponse à l’insuffisance du précédent, et parce qu’il permet de "
         "conclure sur une règle de méthode plutôt que sur un classement.",
    'ex': "Un Gini français stable autour de 0,29 coexistant avec une "
          "explosion documentée du top 1 %."},
   {'q': "La mondialisation polarise-t-elle les sociétés ?",
    'f': "Le cours établit un enchaînement complet. Au niveau productif, le "
         "creusement de la courbe du sourire concentre la valeur sur les "
         "activités immatérielles et qualifiées, tandis que la concurrence "
         "entre territoires comprime la rémunération de l’assemblage. Au "
         "niveau du marché du travail, le travail peu qualifié exposé à la "
         "concurrence internationale est moins demandé : salaires relatifs "
         "en baisse, chômage possible, désindustrialisation locale. Au "
         "niveau politique, les pertes concentrées sur certains individus "
         "et territoires ne sont pas compensées par des gains diffus, d’où "
         "une demande de protection.",
    'r': "Le raisonnement vaut parce qu’il relie trois niveaux que le cours "
         "traite séparément — la chaîne de valeur, le marché du travail, la "
         "décision politique — et parce qu’il repose à chaque étape sur un "
         "mécanisme explicitement formulé dans le cours.",
    'ex': "Le choc chinois, dont les effets persistent par faible mobilité "
          "géographique, compétences spécifiques et effets multiplicateurs "
          "locaux."},
   {'q': "Faut-il s’inquiéter davantage de la polarisation des revenus ou "
         "des patrimoines ?",
    'f': "La polarisation patrimoniale est plus profonde et plus durable. "
         "Le revenu est un flux que la redistribution corrige chaque année, "
         "ce que montre le passage d’un rapport de 18 à 4 entre niveaux de "
         "vie extrêmes après transferts. Le patrimoine est un stock soumis "
         "à une logique cumulative — loyers, intérêts, dividendes — et "
         "transmis par héritage ou donation : les 10 % les plus riches "
         "détiennent 2 612 milliards d’euros en 2025, soit 42 % du PIB "
         "contre 6 % en 1996. La polarisation des patrimoines échappe donc "
         "largement aux instruments qui corrigent celle des revenus.",
    'r': "Ce plan est rigoureux parce qu’il repose sur la distinction "
         "flux/stock que le cours pose explicitement, et parce qu’il "
         "confronte deux séries chiffrées de nature différente sans les "
         "mélanger.",
    'ex': "La variation de la richesse des plus fortunés d’environ 1 300 % "
          "contre 86 % pour le SMIC sur la même période."}],
  voisins=['n23-moyennisation', 'n23-declassement',
           'n22-inegalites-patrimoine', 'n22-inegalites-revenus',
           'n23-classes-sociales'])

d('n23-reproduction-sociale', 23, "Reproduction sociale",
  "Les canaux par lesquels une position se transmet d’une génération à l’autre",
  "La reproduction sociale désigne le maintien des positions sociales d’une "
  "génération à la suivante. Le cours la nomme une fois, à propos de "
  "Veblen, pour qui la reproduction des hiérarchies passe par l’imitation "
  "sociale et non par la lutte des classes. Il en documente par ailleurs "
  "les canaux matériels — logique cumulative du patrimoine, transmission "
  "par héritage ou donation — et le canal éducatif, l’éducation étant "
  "présentée comme levier de transformation sociale et de transmission "
  "intergénérationnelle.",
  "Le cours fournit trois mécanismes distincts de reproduction. Le premier "
  "est culturel et vient de Veblen : la classe de loisir impose les normes "
  "du prestige, les classes inférieures entrent dans une dynamique "
  "d’imitation ou d’émulation, cherchant à copier les signes de richesse, "
  "parfois au détriment de leurs besoins essentiels. Chez Veblen, la "
  "reproduction des hiérarchies sociales se fait principalement par "
  "l’imitation sociale, la diffusion des normes de prestige et le "
  "conformisme, et le cours conclut : ce n’est pas une lutte de classes "
  "mais une reproduction sociale par imitation, qui entretient inégalités "
  "et gaspillage. Le second mécanisme est patrimonial. Le cours distingue "
  "les revenus, qui sont un flux, et le patrimoine, qui est un stock, et "
  "montre que le patrimoine suit une logique cumulative : il engendre des "
  "loyers, des intérêts et des dividendes qui permettent de nouvelles "
  "acquisitions. Il se transmet ensuite par héritage ou par donation, ce "
  "qui reporte l’avantage à la génération suivante sans qu’aucune activité "
  "productive ne soit nécessaire. Les ordres de grandeur sont fournis : le "
  "patrimoine des 10 % les plus riches atteint 2 612 milliards d’euros en "
  "2025, soit environ 42 % du PIB contre 6 % en 1996, et la variation de la "
  "richesse des plus fortunés atteint environ 1 300 % quand le SMIC "
  "progresse de 86 %. Le cours détaille aussi les dispositifs qui "
  "facilitent cette transmission : l’absence de taxation des plus-values "
  "latentes au moment de la transmission, les holdings familiaux non taxés "
  "en Europe contrairement aux États-Unis, et le pacte Dutreil qui permet "
  "un abattement de 75 % voire 95 % en contrepartie d’une conservation de "
  "six ans. Le troisième mécanisme est éducatif. L’éducation agit sur la "
  "mobilité sociale, mais le cours montre que l’accès à l’éducation varie "
  "entre milieux sociaux, entre espaces urbains et ruraux, entre régions et "
  "entre filles et garçons : les inégalités éducatives ne sont pas "
  "seulement institutionnelles, elles sont également sociales et genrées. "
  "Il écrit que sans diffusion de l’éducation, le capital humain demeure "
  "limité, les gains de productivité restent fragiles, les inégalités se "
  "reproduisent, la transformation structurelle est freinée et le "
  "développement humain reste inachevé. Il parle enfin d’une transmission "
  "intergénérationnelle du développement à propos de l’éducation des "
  "filles. Il faut signaler une limite de couverture : ces cours "
  "n’exposent ni les tables de mobilité, ni la notion d’habitus, ni la "
  "sociologie de la reproduction scolaire.",
  [("Le patrimoine engendre du revenu sans travail",
    "Le cours décrit une logique cumulative : un patrimoine détenu "
    "engendre des loyers, des intérêts et des dividendes. Ce revenu permet "
    "de nouvelles acquisitions, de sorte que l’écart initial se creuse de "
    "lui-même au fil du temps."),
   ("Le patrimoine accumulé se transmet",
    "La transmission se fait par héritage ou par donation. L’avantage "
    "acquis par une génération est donc reporté sur la suivante sans "
    "qu’aucune contribution productive ne soit requise de celle qui le "
    "reçoit."),
   ("Des dispositifs fiscaux allègent la transmission",
    "Le cours relève que les plus-values latentes ne sont pas taxées au "
    "moment de la transmission, que les holdings familiaux ne sont pas "
    "taxés en Europe contrairement aux États-Unis, et que le pacte Dutreil "
    "permet un abattement de 75 % voire 95 % moyennant six ans de "
    "conservation."),
   ("L’éducation pourrait rompre la chaîne",
    "Le cours fait de l’éducation un facteur de croissance, un facteur de "
    "développement humain et un levier de transformation sociale, agissant "
    "notamment sur l’autonomie individuelle, la mobilité sociale et la "
    "participation à la vie civique."),
   ("Mais l’accès à l’éducation est lui-même inégal",
    "L’accès varie entre milieux sociaux, entre espaces urbains et ruraux, "
    "entre régions et entre filles et garçons. Les inégalités éducatives ne "
    "sont donc pas seulement institutionnelles : elles sont également "
    "sociales et genrées, ce qui fait de l’école un canal de reproduction "
    "autant qu’un levier de mobilité."),
   ("La reproduction se boucle",
    "Le cours l’énonce directement : sans diffusion de l’éducation, le "
    "capital humain demeure limité, les gains de productivité restent "
    "fragiles, les inégalités se reproduisent, la transformation "
    "structurelle est freinée et le développement humain reste inachevé."),
   ("Une reproduction par les normes s’ajoute à la reproduction matérielle",
    "Chez Veblen, les classes inférieures imitent les signes de richesse de "
    "la classe de loisir et consomment pour paraître. La hiérarchie se "
    "maintient alors par l’imitation sociale, la diffusion des normes de "
    "prestige et le conformisme, sans transmission de patrimoine.")],
  [{'a': "La reproduction patrimoniale est le canal le mieux documenté, "
         "parce que le cours en fournit à la fois le mécanisme — logique "
         "cumulative, puis transmission par héritage ou donation — et la "
         "mesure : 2 612 milliards d’euros détenus par les 10 % les plus "
         "riches en 2025, soit 42 % du PIB contre 6 % en 1996.",
    'cond': "L’argument suppose que le rendement du patrimoine excède "
            "durablement la progression des revenus du travail, ce que le "
            "cours illustre par l’écart entre une variation de richesse "
            "d’environ 1 300 % et une progression du SMIC de 86 %.",
    'lim': "La mesure porte sur des stocks agrégés et non sur des "
           "trajectoires individuelles : elle établit une concentration "
           "croissante sans démontrer que ce sont les mêmes familles qui "
           "occupent le sommet d’une génération à l’autre."},
   {'a': "La fiscalité de la transmission est un levier identifié, "
         "puisque le cours détaille trois dispositifs qui l’allègent : "
         "plus-values latentes non taxées à la transmission, holdings "
         "familiaux non taxés en Europe, pacte Dutreil avec abattement de "
         "75 % voire 95 % pour six ans de conservation.",
    'cond': "Agir sur ces dispositifs suppose d’accepter les effets "
            "économiques invoqués pour les justifier, notamment la "
            "continuité des entreprises familiales que la condition de "
            "conservation vise à préserver.",
    'lim': "Le cours rappelle l’ordre de grandeur des rendements "
           "attendus : une taxe sur les très grands patrimoines "
           "concernerait environ 1 800 foyers pour environ 20 milliards "
           "d’euros face à un déficit d’environ 170 milliards. L’enjeu est "
           "donc plus structurel que budgétaire."},
   {'a': "L’éducation est le canal de rupture le plus puissant : le cours "
         "lui attribue des effets sur la santé, la mortalité infantile, la "
         "santé maternelle, la maîtrise de la fécondité, l’autonomie "
         "individuelle, la mobilité sociale et la participation civique.",
    'cond': "Il faut que l’accès soit effectif, et le cours distingue "
            "soigneusement la scolarisation de l’éducation : ce qui est "
            "juridiquement exigé est l’instruction et non la seule "
            "fréquentation matérielle d’une école.",
    'lim': "L’école peut aussi reproduire : l’accès varie entre milieux "
           "sociaux, entre espaces urbains et ruraux, entre régions et "
           "entre filles et garçons. Le même canal joue donc dans les deux "
           "sens selon la distribution de l’accès."},
   {'a': "La reproduction par les normes complète la reproduction "
         "matérielle : chez Veblen la hiérarchie se maintient par "
         "l’imitation sociale, la diffusion des normes de prestige et le "
         "conformisme, et non par la transmission d’un patrimoine.",
    'cond': "Ce mécanisme exige une classe dominante visible qui impose les "
            "normes du prestige, et des classes inférieures disposant d’un "
            "revenu suffisant pour imiter, ne serait-ce qu’au détriment de "
            "leurs besoins essentiels.",
    'lim': "L’analyse de Veblen explique la stabilité des hiérarchies mais "
           "ne mesure rien : le cours n’en tire aucun indicateur, "
           "contrairement au patrimoine ou à la scolarisation. Elle "
           "s’utilise comme interprétation, pas comme preuve."}],
  [{'t': "La reproduction ne passerait pas par la transmission mais par "
         "l’imitation : les hiérarchies se maintiennent parce que les "
         "classes inférieures copient les normes de prestige de la classe "
         "dominante, non parce qu’un capital change de mains.",
    'qui': "Veblen, dont le cours écrit que la reproduction sociale se fait "
           "principalement par l’imitation sociale, la diffusion des normes "
           "de prestige et le conformisme.",
    'rep': "Les deux canaux ne s’excluent pas et opèrent à des niveaux "
           "différents : la transmission explique la persistance des "
           "positions matérielles, l’imitation explique l’acceptation de la "
           "hiérarchie par ceux qu’elle défavorise. Le cours expose les "
           "deux sans les opposer en termes de validité."},
   {'t': "La croissance et l’éducation suffisent à défaire la "
         "reproduction : à un stade avancé de développement, la "
         "généralisation de l’éducation et la diffusion du progrès "
         "technique réduisent les inégalités.",
    'qui': "Lecture mécanique de la phase descendante de la courbe de "
           "Kuznets.",
    'rep': "Le cours récuse l’automaticité : la réduction des inégalités "
           "dépend du niveau de redistribution, du système fiscal, des "
           "institutions et du degré de protection sociale. Il ajoute que "
           "depuis les années 1980 on observe une forte concentration des "
           "patrimoines, ce qui est précisément le canal de reproduction le "
           "plus résistant."},
   {'t': "Taxer la transmission serait inefficace et contre-productif : au "
         "delà d’un certain seuil, trop d’impôt tue l’impôt, les "
         "patrimoines se déplaçant ou cessant de se constituer.",
    'qui': "Laffer, dont le cours expose la formule et les reproches qui "
           "lui sont adressés.",
    'rep': "Le cours présente l’argument sans le valider et lui oppose deux "
           "éléments : les reproches faits à la courbe de Laffer, et les "
           "propositions de réforme ciblées de Jaravel, qui portent sur les "
           "plus-values latentes à la transmission, les holdings familiaux "
           "et le pacte Dutreil, c’est-à-dire sur des dispositifs précis "
           "plutôt que sur un taux général."}],
  [{'n': "Thorstein Veblen",
    'i': "La reproduction des hiérarchies sociales se fait principalement "
         "par l’imitation sociale, la diffusion des normes de prestige et "
         "le conformisme.",
    'p': "Dans Théorie de la classe de loisir (1899), la classe dominante "
         "impose les normes du prestige ; les classes inférieures cherchent "
         "à copier les signes de richesse, consomment pour paraître, "
         "parfois au détriment de leurs besoins essentiels. Le cours "
         "conclut que ce n’est pas une lutte de classes mais une "
         "reproduction sociale par imitation, qui entretient inégalités et "
         "gaspillage."},
   {'n': "Xavier Jaravel",
    'i': "Trois dispositifs fiscaux précis facilitent la transmission des "
         "très grands patrimoines et pourraient être réformés.",
    'p': "Le cours expose ses propositions : taxer les plus-values latentes "
         "au moment de la transmission, soumettre les holdings familiaux à "
         "l’impôt — ils ne sont pas taxés en Europe alors qu’ils le sont "
         "aux États-Unis —, et revoir le pacte Dutreil, qui permet un "
         "abattement de 75 % voire 95 % en contrepartie d’une conservation "
         "de six ans."},
   {'n': "Gabriel Zucman",
    'i': "Une imposition plancher sur les très grands patrimoines "
         "corrigerait la dégressivité de fait au sommet de la distribution.",
    'p': "Le cours présente le dispositif — un seuil de 100 millions "
         "d’euros, environ 1 800 foyers concernés, une taxe plancher "
         "différentielle de 2 %, un rendement attendu d’environ 20 "
         "milliards d’euros face à un déficit d’environ 170 milliards — et "
         "en expose trois critiques, ce qui en fait un cas d’école pour "
         "discuter les limites de l’action sur la reproduction patrimoniale."},
   {'n': "Simon Kuznets",
    'i': "La réduction des inégalités à un stade avancé repose surtout sur "
         "la redistribution, les recettes fiscales et les politiques "
         "sociales.",
    'p': "Le cours place la généralisation de l’éducation, la diffusion du "
         "progrès technique, l’urbanisation complète et la montée de la "
         "classe moyenne parmi les mécanismes de la phase descendante, mais "
         "ajoute un « mais surtout » en faveur des facteurs politiques : "
         "l’État corrige les inégalités produites par le marché. La "
         "reproduction n’est donc pas interrompue par la croissance seule."}],
  [{'f': "Le patrimoine des 10 % les plus riches atteint 2 612 milliards "
         "d’euros en 2025, soit environ 42 % du PIB, contre 6 % en 1996.",
    'p': "La concentration patrimoniale s’est multipliée par sept en part "
         "du PIB en moins de trente ans, ce qui montre que le canal "
         "cumulatif et héréditaire est aujourd’hui le plus actif des canaux "
         "de reproduction."},
   {'f': "Sur la période étudiée, la richesse des plus fortunés varie "
         "d’environ 1 300 % tandis que le SMIC progresse de 86 %.",
    'p': "L’écart entre rendement du patrimoine et progression des revenus "
         "du travail mesure directement l’avantage de la position "
         "héritée : aucune trajectoire salariale ne peut combler un tel "
         "différentiel."},
   {'f': "Le pacte Dutreil permet un abattement de 75 %, voire 95 %, sur la "
         "transmission d’entreprise, en contrepartie d’une conservation des "
         "titres pendant six ans.",
    'p': "La reproduction n’est pas seulement un fait économique, elle est "
         "aussi un effet de règles fiscales identifiables, donc modifiables "
         "— ce qui déplace le débat du constat vers le choix politique."},
   {'f': "Le cours énonce que sans diffusion de l’éducation, les inégalités "
         "se reproduisent, le capital humain demeure limité, les gains de "
         "productivité restent fragiles et la transformation structurelle "
         "est freinée.",
    'p': "C’est la formulation la plus explicite du lien entre éducation et "
         "reproduction : l’école n’est pas seulement un facteur de "
         "croissance, elle est le point où la reproduction peut être "
         "interrompue ou confirmée."}],
  [{'q': "Les inégalités se transmettent-elles d’une génération à l’autre ?",
    'f': "Le cours identifie trois canaux de transmission. Le canal "
         "patrimonial est le plus mesuré : le patrimoine est un stock soumis "
         "à une logique cumulative, engendrant loyers, intérêts et "
         "dividendes, puis transmis par héritage ou donation, les 10 % les "
         "plus riches détenant 42 % du PIB en 2025 contre 6 % en 1996. Le "
         "canal fiscal l’amplifie, par la non-taxation des plus-values "
         "latentes, des holdings familiaux et par le pacte Dutreil. Le canal "
         "éducatif joue dans les deux sens, puisque l’éducation est un "
         "levier de mobilité sociale mais que son accès varie selon le "
         "milieu social, le territoire et le sexe.",
    'r': "Ce plan est rigoureux parce qu’il distingue les canaux selon leur "
         "degré de documentation dans le cours et parce qu’il réserve à "
         "l’éducation un statut ambivalent explicitement établi : levier de "
         "transformation sociale d’un côté, inégalités sociales et genrées "
         "de l’autre.",
    'ex': "La variation de 1 300 % de la richesse des plus fortunés contre "
          "86 % pour le SMIC."},
   {'q': "L’école réduit-elle ou reproduit-elle les inégalités ?",
    'f': "Les deux, et c’est l’articulation qu’il faut exposer. Le cours "
         "attribue à l’éducation des effets considérables : santé, "
         "mortalité infantile, santé maternelle, maîtrise de la fécondité, "
         "autonomie individuelle, mobilité sociale, participation civique, "
         "et il en fait un levier de transformation sociale. Mais il "
         "établit aussi que l’accès varie entre milieux sociaux, entre "
         "espaces urbains et ruraux, entre régions et entre filles et "
         "garçons, et que les inégalités éducatives ne sont pas seulement "
         "institutionnelles mais sociales et genrées. Le même dispositif "
         "produit donc mobilité ou reproduction selon la distribution de "
         "l’accès.",
    'r': "Le raisonnement tient parce qu’il refuse de choisir entre deux "
         "séries également présentes dans le cours, et parce qu’il "
         "s’appuie sur la distinction explicite entre scolarisation et "
         "éducation : la présence matérielle à l’école ne garantit pas "
         "l’acquisition.",
    'ex': "Les filles des pays en développement, exposées à la "
          "déscolarisation précoce, au poids des tâches domestiques et aux "
          "mariages précoces."},
   {'q': "Faut-il taxer davantage la transmission du patrimoine ?",
    'f': "Le cours fournit les deux côtés du débat avec précision. Pour : "
         "le patrimoine suit une logique cumulative et se transmet par "
         "héritage ou donation, trois dispositifs en allègent la taxation, "
         "et la concentration atteint 42 % du PIB pour les 10 % les plus "
         "riches. Contre : les critiques adressées à la taxe sur les très "
         "grands patrimoines, son rendement attendu d’environ 20 milliards "
         "face à un déficit de 170 milliards, et l’argument de Laffer selon "
         "lequel trop d’impôt tue l’impôt — argument auquel le cours "
         "associe cependant des reproches.",
    'r': "Ce plan est équilibré parce qu’il oppose un mécanisme structurel "
         "à un argument de rendement, et parce qu’il mobilise les "
         "propositions ciblées de Jaravel pour montrer qu’entre statu quo "
         "et taxation générale existe une voie intermédiaire.",
    'ex': "Les holdings familiaux, non taxés en Europe alors qu’ils le sont "
          "aux États-Unis."}],
  voisins=['n23-capital-economique-culturel-social', 'n23-ecole-inegalites',
           'n22-heritage', 'n22-inegalites-patrimoine',
           'n23-rapports-de-classe'])

d('n23-capital-economique-culturel-social', 23,
  "Capital économique, culturel et social",
  "Les formes de capital que le cours distingue, et celle qu’il ne nomme pas",
  "L’expression désigne l’idée que les ressources d’un individu ou d’une "
  "société ne sont pas seulement monétaires. Le cours ne reprend pas cette "
  "triade : il construit sa propre typologie des capitaux — physique, "
  "humain, naturel, technologique, social, institutionnel — dans le cadre "
  "de l’analyse de la croissance. Le capital économique y correspond au "
  "capital physique et au patrimoine, le capital social y est défini "
  "précisément, mais l’expression « capital culturel » est absente : ce "
  "point de vocabulaire doit être signalé.",
  "Le cours pose que, dans une lecture large, la croissance dépend de "
  "plusieurs capitaux : capital physique, capital humain, capital naturel, "
  "capital technologique, capital social et capital institutionnel. La "
  "croissance n’est donc pas seulement accumulation de machines, elle "
  "repose sur un ensemble de ressources complémentaires, et la question de "
  "la soutenabilité revient à se demander si l’on peut préserver la "
  "capacité de croissance sans détruire certains de ces capitaux. Trois "
  "d’entre eux sont définis avec précision. Le capital technologique "
  "désigne le stock de connaissances mobilisable pour produire plus "
  "efficacement : connaissances scientifiques, procédés de production, "
  "résultats de la recherche et développement. Le capital social désigne "
  "les réseaux, la réputation, les relations, la confiance et la capacité à "
  "mobiliser des partenaires ou des investisseurs ; il facilite la "
  "coordination, l’accès à l’information, le financement et l’activité "
  "entrepreneuriale. Le capital institutionnel regroupe les règles et les "
  "lois. À cette typologie s’ajoute le capital humain, que le cours "
  "mobilise massivement dans le chapitre sur le développement : "
  "l’éducation accroît la productivité mais aussi la santé, l’autonomie et "
  "la mobilité sociale, et sans diffusion de l’éducation le capital humain "
  "demeure limité. Le capital économique, enfin, apparaît sous deux "
  "formes : le capital physique dans l’analyse de la croissance, et le "
  "patrimoine dans l’analyse des inégalités, où il est présenté comme un "
  "stock soumis à une logique cumulative et transmis par héritage ou "
  "donation. Le cours fournit une application remarquable de cette "
  "pluralité : dans la critique du capitalisme entrepreneurial, il écrit "
  "que l’innovation est collective, que les salariés, ingénieurs et "
  "chercheurs y jouent un rôle essentiel, que l’État finance souvent les "
  "innovations et que le succès dépend aussi du capital social et des "
  "réseaux — la réussite entrepreneuriale dépend donc d’un contexte "
  "collectif et social. Il faut en revanche signaler nettement deux "
  "absences : l’expression « capital culturel » n’apparaît pas, et la "
  "sociologie qui articule ces capitaux en théorie de la reproduction n’est "
  "pas exposée. Le plus proche équivalent disponible est le capital humain, "
  "mais il désigne une capacité productive acquise par l’éducation et non "
  "un patrimoine de dispositions et de savoirs hérités du milieu familial. "
  "Une dissertation peut utiliser ces cours pour montrer que les ressources "
  "ne sont pas seulement monétaires, mais non pour s’appuyer sur la triade "
  "elle-même.",
  [("Le capital physique ne suffit pas à expliquer la croissance",
    "Le cours établit que la croissance n’est pas seulement accumulation de "
    "machines : elle repose sur un ensemble de ressources "
    "complémentaires, ce qui oblige à distinguer plusieurs formes de "
    "capital au lieu d’un facteur unique."),
   ("Le capital humain convertit l’éducation en capacité productive",
    "L’éducation accroît la productivité, mais aussi la santé, "
    "l’autonomie individuelle, la mobilité sociale et la participation "
    "civique. Le cours en fait simultanément un facteur de croissance, un "
    "facteur de développement humain et un levier de transformation "
    "sociale."),
   ("Le capital technologique accumule des connaissances mobilisables",
    "Il réunit les connaissances scientifiques, les procédés de production "
    "et les résultats de la recherche et développement. C’est un stock, "
    "c’est-à-dire une ressource qui demeure disponible après usage, "
    "contrairement aux facteurs consommés dans la production."),
   ("Le capital social abaisse les coûts de la coordination",
    "Réseaux, réputation, relations, confiance et capacité à mobiliser des "
    "partenaires ou des investisseurs facilitent la coordination, l’accès à "
    "l’information, le financement et l’activité entrepreneuriale. Ce qui "
    "serait coûteux à contractualiser devient accessible par la relation."),
   ("Le capital institutionnel fixe les règles du jeu",
    "Il regroupe les règles et les lois. Le cours lui donne un contenu "
    "concret avec la distinction entre institutions inclusives, qui "
    "favorisent innovation, investissement, mobilité sociale et "
    "entrepreneuriat, et institutions extractives, qui freinent "
    "l’initiative et la diffusion du progrès."),
   ("Les capitaux se combinent et se substituent mal",
    "La question de la soutenabilité consiste à se demander si l’on peut "
    "préserver la capacité de croissance sans détruire certains capitaux. "
    "Détruire du capital naturel pour accumuler du capital physique n’est "
    "donc pas un échange neutre."),
   ("La réussite individuelle repose sur ces capitaux collectifs",
    "Le cours écrit que l’innovation est collective, que les salariés, "
    "ingénieurs et chercheurs y jouent un rôle essentiel, que l’État "
    "finance souvent les innovations et que le succès dépend aussi du "
    "capital social et des réseaux : la réussite entrepreneuriale dépend "
    "d’un contexte collectif et social.")],
  [{'a': "Distinguer plusieurs formes de capital améliore l’explication de "
         "la croissance : le cours montre que la croissance dépend du "
         "capital physique, humain, naturel, technologique, social et "
         "institutionnel, et non de la seule accumulation de machines.",
    'cond': "Cette typologie n’a de valeur analytique que si chaque forme "
            "est définie opérationnellement, ce que le cours fait pour le "
            "capital technologique, le capital social et le capital "
            "institutionnel en énumérant leurs composantes.",
    'lim': "Multiplier les capitaux risque de rendre toute croissance "
           "explicable après coup : si un pays ne croît pas, on peut "
           "toujours invoquer un capital manquant. Le cours ne fournit pas "
           "de mesure pour le capital social ni pour le capital "
           "institutionnel."},
   {'a': "Le capital social a des effets économiques identifiables : il "
         "facilite la coordination, l’accès à l’information, le financement "
         "et l’activité entrepreneuriale, ce qui en fait un déterminant de "
         "la réussite et non un simple ornement sociologique.",
    'cond': "Il faut que les réseaux et la confiance réduisent effectivement "
            "des coûts que le marché supporterait autrement, notamment des "
            "coûts d’information et de contractualisation.",
    'lim': "Un capital social inégalement distribué devient un mécanisme "
           "d’inégalité : si le succès dépend des réseaux, l’accès aux "
           "réseaux devient la ressource rare, ce que le cours constate sans "
           "l’analyser comme tel."},
   {'a': "Le capital humain fonde une politique publique claire : le cours "
         "montre que sans diffusion de l’éducation, le capital humain "
         "demeure limité, les gains de productivité restent fragiles, les "
         "inégalités se reproduisent et la transformation structurelle est "
         "freinée.",
    'cond': "Le raisonnement exige de distinguer la scolarisation de "
            "l’éducation : le cours insiste sur le fait que ce qui est "
            "juridiquement exigé est l’instruction, non la seule "
            "fréquentation matérielle d’une école.",
    'lim': "Le capital humain est mesuré dans le cours par des durées de "
           "scolarisation, moyenne et attendue, dans la construction de "
           "l’IDH. Ces indicateurs saisissent un volume, non une qualité ni "
           "une transmission familiale de dispositions."},
   {'a': "Penser la richesse comme un ensemble de capitaux permet de poser "
         "correctement la soutenabilité : la question devient celle de la "
         "préservation de la capacité de croissance sans destruction de "
         "certains capitaux, et non celle du seul niveau de production.",
    'cond': "Cela suppose que les capitaux ne soient pas parfaitement "
            "substituables : si le capital physique pouvait toujours "
            "remplacer le capital naturel, la question de la soutenabilité "
            "ne se poserait pas.",
    'lim': "Le cours pose la question sans la trancher, et ne fournit pas "
           "de critère permettant de dire quel niveau de destruction d’un "
           "capital serait compensé par l’accumulation d’un autre."}],
  [{'t': "La notion de capital devrait rester réservée aux moyens de "
         "production : le capital constant désigne les machines, bâtiments, "
         "outils et matières premières, et étendre le mot à la confiance ou "
         "aux relations lui ôte toute précision.",
    'qui': "Lecture issue de l’analyse marxienne du capital exposée dans le "
           "cours, qui définit strictement capital constant et capital "
           "variable.",
    'rep': "L’objection est méthodologiquement sérieuse mais le cours "
           "justifie l’extension par un besoin explicatif : la croissance "
           "n’est pas seulement accumulation de machines. La réponse "
           "consiste à exiger pour chaque capital une définition et, si "
           "possible, une mesure — exigence que le capital social satisfait "
           "mal."},
   {'t': "Le capital social serait une manière euphémisée de nommer le "
         "privilège : si le succès dépend des réseaux, de la réputation et "
         "de la capacité à mobiliser des investisseurs, alors parler de "
         "capital valide ce qui devrait être critiqué.",
    'rep': "Le cours ne l’emploie pas pour légitimer : il s’en sert au "
           "contraire pour relativiser le mythe de la réussite "
           "individuelle, en écrivant que l’innovation est collective, que "
           "l’État finance souvent les innovations et que la réussite "
           "entrepreneuriale dépend d’un contexte collectif et social. "
           "L’usage du cours est démystificateur."},
   {'t': "La triade capital économique, culturel et social permettrait "
         "d’expliquer la reproduction des positions sociales mieux que la "
         "typologie des capitaux de croissance.",
    'rep': "C’est possible mais ces cours ne le permettent pas : "
           "l’expression « capital culturel » n’y apparaît pas et la "
           "sociologie qui articule ces capitaux en théorie de la "
           "reproduction n’y est pas exposée. Il faut donc le signaler "
           "explicitement et se limiter à ce que le cours contient — "
           "capital humain, capital social, patrimoine — plutôt que "
           "d’attribuer au cours une théorie qu’il ne développe pas."}],
  [{'n': "Daron Acemoglu",
    'i': "Les performances économiques durables dépendent du type "
         "d’institutions, inclusives ou extractives.",
    'p': "Avec James Robinson, il soutient que les institutions inclusives "
         "favorisent innovation, investissement, mobilité sociale et "
         "entrepreneuriat, tandis que les institutions extractives freinent "
         "l’initiative, la diffusion du progrès et la modernisation. Le "
         "cours applique cette grille à la précocité anglaise, qui "
         "s’expliquerait moins par les ressources que par des institutions "
         "plus favorables à l’innovation."},
   {'n': "James Robinson",
    'i': "La précocité d’une économie s’explique par ses institutions plus "
         "que par ses ressources naturelles.",
    'p': "Le cours attribue conjointement à Acemoglu et Robinson la thèse "
         "selon laquelle la précocité anglaise s’explique moins par les "
         "seules ressources que par des institutions relativement plus "
         "favorables à l’innovation et à l’investissement. Le capital "
         "institutionnel cesse ainsi d’être un facteur résiduel pour "
         "devenir le facteur premier."},
   {'n': "Amartya Sen",
    'i': "Le développement est l’accroissement des capabilités, "
         "c’est-à-dire des libertés réelles dont disposent les individus.",
    'p': "Le cours illustre la notion par des privations concrètes : vivre "
         "dans un désert médical, ne pas avoir accès à l’école, subir des "
         "discriminations réduisent les capabilités. Cette approche "
         "justifie de compter comme ressources des éléments non monétaires, "
         "ce qui éclaire pourquoi le capital humain et le capital social "
         "comptent au même titre que le capital physique."},
   {'n': "Thorstein Veblen",
    'i': "Les comportements économiques dépendent des habitudes, des "
         "normes, des institutions et de la recherche de statut social.",
    'p': "Son rejet de l’homo œconomicus fournit l’arrière-plan théorique "
         "qui permet de traiter les normes et les relations comme des "
         "ressources. Sa théorie de la consommation ostentatoire montre que "
         "les signes de statut ont une valeur économique réelle, ce qui est "
         "l’intuition la plus proche d’un capital non monétaire dans ces "
         "cours."}],
  [{'f': "Le cours énumère six capitaux dont dépend la croissance : "
         "physique, humain, naturel, technologique, social et "
         "institutionnel.",
    'p': "La richesse d’une économie n’est pas réductible à son stock "
         "d’équipements, et la question de la soutenabilité peut être posée "
         "comme celle de la préservation simultanée de plusieurs capitaux."},
   {'f': "Le capital social est défini comme les réseaux, la réputation, "
         "les relations, la confiance et la capacité à mobiliser des "
         "partenaires ou des investisseurs.",
    'p': "La définition est opérationnelle et non métaphorique : chacun de "
         "ces éléments a un effet identifiable sur la coordination, l’accès "
         "à l’information, le financement et l’activité entrepreneuriale."},
   {'f': "Le cours écrit que le succès entrepreneurial dépend aussi du "
         "capital social et des réseaux, que l’innovation est collective et "
         "que l’État finance souvent les innovations.",
    'p': "Cela montre que les capitaux non monétaires servent dans le cours "
         "à contester le récit de la réussite individuelle, et pas seulement "
         "à compléter une fonction de production."},
   {'f': "L’IDH mesure l’éducation par deux sous-indicateurs, la durée "
         "moyenne de scolarisation et la durée attendue de scolarisation, "
         "l’écart entre les deux révélant la dynamique éducative.",
    'p': "Le capital humain reçoit ainsi une mesure, contrairement au "
         "capital social : cela montre la hiérarchie de rigueur entre les "
         "formes de capital dans le cours, et borne ce qu’une dissertation "
         "peut affirmer de chacune."}],
  [{'q': "La richesse d’une société se réduit-elle à son capital "
         "productif ?",
    'f': "Le cours répond non et fournit la typologie : la croissance "
         "dépend du capital physique, humain, naturel, technologique, "
         "social et institutionnel, de sorte qu’elle n’est pas seulement "
         "accumulation de machines mais repose sur un ensemble de "
         "ressources complémentaires. Chacune reçoit un contenu précis : le "
         "capital technologique est un stock de connaissances mobilisable, "
         "le capital social réunit réseaux, réputation, relations et "
         "confiance, le capital institutionnel regroupe les règles et les "
         "lois. La question de la soutenabilité découle directement de "
         "cette pluralité.",
    'r': "Ce plan est rigoureux parce qu’il part de la typologie explicite "
         "du cours plutôt que d’une liste reconstituée, et parce qu’il "
         "aboutit à la question que le cours pose lui-même : peut-on "
         "préserver la capacité de croissance sans détruire certains "
         "capitaux.",
    'ex': "Le capital naturel, dont la destruction peut accompagner "
          "l’accumulation de capital physique sans que l’échange soit "
          "neutre."},
   {'q': "La réussite économique est-elle individuelle ?",
    'f': "Le cours construit explicitement la réponse négative. Dans sa "
         "critique du capitalisme entrepreneurial, il écrit que "
         "l’innovation est collective, que les salariés, ingénieurs et "
         "chercheurs y jouent un rôle essentiel, que l’État finance souvent "
         "les innovations et que le succès dépend aussi du capital social "
         "et des réseaux, pour conclure que la réussite entrepreneuriale "
         "dépend d’un contexte collectif et social. Les capitaux non "
         "monétaires ne sont donc pas un complément d’analyse : ils servent "
         "à déplacer l’attribution du mérite.",
    'r': "Le raisonnement s’appuie sur une conclusion que le cours formule "
         "lui-même, et il prolonge logiquement la définition du capital "
         "social, dont les quatre effets listés sont tous des effets de "
         "contexte et non de talent.",
    'ex': "L’État finançant la recherche amont dont une entreprise tire "
          "ensuite un produit commercialisable."},
   {'q': "Les ressources non monétaires expliquent-elles la persistance "
         "des positions sociales ?",
    'f': "Il faut ici une réponse prudente, car le cours fournit le "
         "matériau sans la théorie. Il définit le capital social comme un "
         "ensemble de réseaux et de relations qui facilitent l’accès au "
         "financement et à l’information ; il montre que le capital humain "
         "dépend d’un accès à l’éducation lui-même inégal entre milieux "
         "sociaux, territoires et sexes ; il décrit chez Veblen une "
         "reproduction des hiérarchies par imitation des normes de "
         "prestige. Mais il n’emploie pas l’expression « capital culturel » "
         "et n’expose pas de théorie articulant ces capitaux en mécanisme "
         "de reproduction.",
    'r': "Ce plan est le seul honnête au regard du contenu disponible : il "
         "mobilise trois éléments réellement présents et signale "
         "explicitement l’absence d’une théorie d’ensemble, ce qui évite "
         "d’attribuer au cours une position qu’il ne défend pas.",
    'ex': "L’accès à l’éducation variant entre milieux sociaux, entre "
          "espaces urbains et ruraux et entre filles et garçons."}],
  voisins=['n23-reproduction-sociale', 'n23-ecole-inegalites',
           'n23-classes-sociales', 'n22-inegalites-patrimoine',
           'n23-discriminations'])
