# -*- coding: utf-8 -*-
"""Visualisation 4 — Innovation et emploi (type cycle)."""

from vz_base import v, nd, ln

v('vz-innovation-emploi', 'Innovation et emploi',
  'Chapitres 6 et 8 · un cycle qui se referme',
  'cycle',
  "L’innovation ne supprime pas l’emploi et ne le crée pas non plus "
  "automatiquement : elle le déplace. Cette visualisation suit le cycle "
  "complet, de l’innovation fondamentale à la grappe qu’elle entraîne, de la "
  "destruction des emplois anciens au déversement vers de nouveaux, puis aux "
  "institutions qui décident si le bilan sera positif — et qui conditionnent "
  "l’innovation suivante.",
  [("Un cycle, pas une flèche",
    "Chaque étape conditionne la suivante et la dernière revient à la "
    "première : les institutions qui accompagnent la reconversion décident "
    "si l’innovation suivante sera possible. C’est ce bouclage qui distingue "
    "une copie construite d’une copie qui aligne des effets."),
   ("Le bilan est conditionnel",
    "Le point décisif du cours : la destruction créatrice est globalement "
    "bénéfique si le réemploi s’opère. Elle décrit un mécanisme, pas un "
    "résultat garanti. Tous les débats du chapitre se logent dans cette "
    "condition."),
   ("Deux pressions, une même catégorie",
    "Progrès technique biaisé et concurrence internationale frappent les "
    "mêmes travailleurs : les non-qualifiés des secteurs exposés. Suivre les "
    "deux flèches qui convergent sur la polarisation donne l’argument le "
    "plus solide sur les inégalités.")],
  [
   nd('coeur', 'La destruction créatrice', 'coeur',
      "Le progrès ne s’ajoute pas à l’existant : il le remplace. Schumpeter "
      "décrit le capitalisme comme un processus de transformation "
      "permanente.",
      grp=0,
      defi="La destruction créatrice désigne le processus par lequel "
           "l’innovation détruit des activités, des emplois et des positions "
           "établies en même temps qu’elle en crée de nouveaux. "
           "L’expression est de Schumpeter et elle décrit le capitalisme "
           "comme un processus de transformation permanente. Le point "
           "essentiel est que son bilan est conditionnel : le processus est "
           "globalement bénéfique si le réemploi s’opère, et seulement à "
           "cette condition.",
      mec=[("La dévalorisation de l’ancien",
            "Les capitaux, les compétences et les organisations adaptés à "
            "l’ancienne technique perdent leur valeur. La perte est réelle et "
            "immédiate pour ceux qui les détiennent."),
           ("La réallocation des ressources",
            "Travail et capital libérés se redéploient vers les activités "
            "nouvelles. C’est ce redéploiement, et lui seul, qui transforme "
            "la destruction en gain collectif."),
           ("L’asymétrie temporelle et sociale",
            "La destruction est concentrée et immédiate, la création diffuse "
            "et différée. La perception du processus est donc "
            "systématiquement plus défavorable que son bilan comptable.")],
      opp=[{'t': "La destruction créatrice conduit-elle nécessairement au "
                 "progrès ? Rien ne garantit que les ressources détruites "
                 "soient réemployées.",
            'qui': "objection centrale du cours",
            'rep': "L’objection est exacte et rend le bilan conditionnel : la "
                   "destruction créatrice décrit un mécanisme, elle ne "
                   "garantit pas un résultat. C’est ce qui fonde les "
                   "politiques de reconversion."}],
      aut=[{'n': "Joseph Schumpeter",
            'i': "Le capitalisme progresse par destruction créatrice : "
                 "l’innovation remplace l’existant au lieu de s’y ajouter."},
           {'n': "Peter Howitt",
            'i': "Chaque innovation détruit la rente de la précédente, ce qui "
                 "entretient la dynamique."}],
      faits=[{'f': "La destruction créatrice est mentionnée dix fois dans le "
                   "chapitre consacré à la croissance et douze fois dans "
                   "celui consacré aux révolutions industrielles.",
              'p': "La notion fait le lien entre l’analyse de la croissance "
                   "et l’histoire économique : elle est à la fois un "
                   "mécanisme de modèle et une description de transformation "
                   "historique."}],
      termes=['destruction creatrice', 'schumpeter', 'innovation'],
      dos=['n2-destruction-creatrice', 'n2-entrepreneur']),

   nd('invention', 'De l’invention à l’innovation', 'pilier',
      "Une invention est une découverte ; une innovation est son "
      "introduction effective dans l’économie. Seule la seconde a des effets "
      "sur l’emploi.",
      grp=1,
      defi="L’invention désigne la découverte d’un principe ou d’un procédé "
           "nouveau ; l’innovation désigne son introduction effective dans "
           "l’économie, c’est-à-dire sa mise en œuvre productive et "
           "commerciale. La distinction est décisive pour l’emploi : une "
           "invention qui reste au laboratoire ne détruit ni ne crée aucun "
           "poste. Le cours distingue par ailleurs innovation de produit et "
           "innovation de procédé, ainsi qu’innovations radicales et "
           "incrémentales, deux partitions qui ne se recouvrent pas.",
      mec=[("Le passage à l’usage productif",
            "L’innovation suppose un entrepreneur qui prend le risque de la "
            "mise en œuvre : c’est à ce moment seulement que les emplois "
            "anciens sont menacés et que de nouveaux deviennent possibles."),
           ("Produit ou procédé",
            "L’innovation de procédé réduit le travail nécessaire pour une "
            "production donnée et menace donc directement l’emploi existant ; "
            "l’innovation de produit ouvre un marché nouveau et crée de la "
            "demande de travail."),
           ("Radicale ou incrémentale",
            "Une innovation fondamentale ouvre un nouveau cycle, avec rupture "
            "majeure, nouveau secteur et nouvelle logique productive ; "
            "l’innovation incrémentale apporte perfectionnements et "
            "ajustements techniques. La destruction est massive dans le "
            "premier cas, limitée dans le second.")],
      aut=[{'n': "Joseph Schumpeter",
            'i': "L’entrepreneur innovateur est celui qui réalise de "
                 "nouvelles combinaisons productives, et non celui qui gère "
                 "l’existant."}],
      termes=['invention', 'innovation de procede', 'innovation de produit',
              'innovation radicale'],
      dos=['n2-invention-innovation', 'n2-produit-procede',
           'n2-radicales-incrementales']),

   nd('grappe', 'La grappe d’innovations', 'pilier',
      "Une innovation fondamentale en appelle des dizaines d’autres : "
      "techniques, mais aussi juridiques et organisationnelles. D’où le "
      "caractère discontinu du progrès.",
      grp=1,
      defi="Une grappe d’innovations désigne l’ensemble des innovations "
           "secondaires, adaptations techniques, perfectionnements, créations "
           "de secteurs et transformations organisationnelles qu’entraîne une "
           "innovation fondamentale. La notion est de Schumpeter et elle "
           "explique le caractère discontinu du progrès économique : les "
           "innovations ne sont pas uniformément réparties dans le temps mais "
           "se groupent autour de ruptures majeures.",
      mec=[("L’appel d’innovations complémentaires",
            "L’innovation initiale est inutilisable seule : elle exige des "
            "infrastructures, des services, des normes. Chacun de ces "
            "compléments est lui-même une innovation, et chacun crée des "
            "emplois propres."),
           ("Les adaptations institutionnelles",
            "La grappe comprend des transformations non techniques : règles "
            "de responsabilité, formes d’assurance, organisation du travail, "
            "cadre réglementaire. Le cours les mentionne explicitement pour "
            "le véhicule autonome."),
           ("L’épuisement de la grappe",
            "Lorsque les applications complémentaires sont réalisées, les "
            "gains s’amenuisent : la phase d’expansion s’achève, en attente "
            "d’une nouvelle innovation fondamentale.")],
      aut=[{'n': "Nikolaï Kondratiev",
            'i': "L’activité économique suit des cycles longs de cinquante à "
                 "soixante ans, portés par les grappes d’innovations."},
           {'n': "Clément Juglar",
            'i': "Les cycles de durée intermédiaire, d’environ huit à dix "
                 "ans, se superposent aux cycles longs."}],
      faits=[{'f': "Le cours applique la logique des grappes au véhicule "
                   "autonome : intelligence artificielle, logiciels "
                   "embarqués, cartographie, réglementation, responsabilité "
                   "juridique, infrastructures connectées.",
              'p': "L’exemple montre que la grappe comprend des innovations "
                   "juridiques et institutionnelles, et pas seulement "
                   "techniques : l’emploi créé déborde largement le secteur "
                   "d’origine."},
             {'f': "Les cycles de Kondratiev durent cinquante à soixante ans "
                   "et se superposent aux cycles de Kitchin et de Juglar.",
              'p': "L’ordre de grandeur situe l’horizon d’une grappe : son "
                   "déploiement complet excède largement la durée d’un cycle "
                   "conjoncturel ordinaire, donc celle d’un mandat politique."}],
      termes=['grappe d innovations', 'kondratiev', 'cycle long'],
      dos=['n2-grappes', 'n2-revolutions-tech']),

   nd('detruit', 'Les emplois détruits', 'limite',
      "La perte est concentrée, immédiate et identifiable : un site, un "
      "métier, un bassin d’emploi. C’est elle que l’on voit, et elle est "
      "réelle.",
      grp=1,
      defi="La destruction d’emplois est le versant immédiat et visible du "
           "processus : les capitaux, les compétences et les organisations "
           "adaptés à l’ancienne technique perdent leur valeur, et les "
           "emplois qui en dépendaient disparaissent. Le cours insiste sur "
           "l’asymétrie : la destruction est concentrée sur des personnes et "
           "des territoires précis, tandis que la création est diffuse et "
           "différée. Les deux ne se compensent donc pas individuellement, "
           "même lorsque le solde agrégé est positif.",
      mec=[("La perte de valeur du capital spécifique",
            "Les machines, les locaux et surtout les compétences acquises "
            "n’ont de valeur que dans l’ancienne technique. Leur "
            "dévalorisation est instantanée et ne donne lieu à aucune "
            "compensation automatique."),
           ("La concentration territoriale",
            "Un secteur ancien est souvent concentré géographiquement : sa "
            "disparition frappe un bassin entier, ce qui transforme un choc "
            "sectoriel en crise locale durable.")],
      opp=[{'t': "Le processus est socialement coûteux de manière "
                 "asymétrique : les pertes sont concentrées, les gains "
                 "dispersés.",
            'qui': "objection sociale",
            'rep': "L’asymétrie explique la contestation sans invalider le "
                   "mécanisme : elle plaide pour une socialisation des coûts "
                   "de transition plutôt que pour un blocage de l’innovation."}],
      faits=[{'f': "Le cours oppose le gain du caddie, faible mais diffus sur "
                   "beaucoup de ménages, à la perte d’emploi, très forte mais "
                   "concentrée sur certains individus et territoires.",
              'p': "L’opposition démontre que les deux effets ne se "
                   "compensent pas individuellement, même si le solde agrégé "
                   "est positif. C’est l’argument central sur l’acceptabilité."}],
      termes=['destruction d emplois', 'reconversion', 'chomage structurel'],
      dos=['n10-chomage-conj-struct', 'n2-destruction-creatrice']),

   nd('biais', 'Le progrès technique biaisé', 'pilier',
      "L’innovation n’avantage pas également tous les travailleurs : elle "
      "élève la productivité des qualifiés et automatise les tâches "
      "routinières.",
      grp=1,
      defi="Le progrès technique biaisé désigne une innovation qui n’avantage "
           "pas également tous les travailleurs : il peut être biaisé en "
           "faveur des travailleurs qualifiés. Le cours en donne le "
           "mécanisme : les nouvelles technologies augmentent la productivité "
           "des qualifiés, remplacent certaines tâches routinières et "
           "réduisent la demande de certains travailleurs peu qualifiés, d’où "
           "un creusement des écarts salariaux. Le biais porte sur la nature "
           "des tâches, non sur les personnes.",
      mec=[("L’élévation de la productivité des qualifiés",
            "Les nouvelles technologies rendent les travailleurs qualifiés "
            "plus productifs : leur rémunération s’élève, ce qui creuse "
            "l’écart avec ceux dont la productivité n’est pas augmentée par "
            "la même technologie."),
           ("Le remplacement des tâches routinières",
            "L’automatisation substitue des machines aux tâches "
            "standardisables : le biais ne porte pas sur les personnes mais "
            "sur la nature des tâches, ce qui explique que des emplois "
            "intermédiaires soient touchés."),
           ("La baisse de la demande de travail peu qualifié",
            "Une fois les tâches routinières automatisées, la demande de "
            "certains travailleurs peu qualifiés diminue : leur salaire "
            "relatif baisse et le risque de chômage s’accroît.")],
      opp=[{'t': "L’ouverture internationale est la cause principale de la "
                 "dégradation relative de la situation des travailleurs peu "
                 "qualifiés.",
            'qui': "lecture par le commerce",
            'rep': "Le cours objecte que le commerce n’explique pas à lui "
                   "seul les inégalités internes et désigne le progrès "
                   "technique biaisé comme un facteur particulièrement "
                   "important, les deux pressions se cumulant sur les mêmes "
                   "catégories."}],
      aut=[{'n': "Thomas Piketty",
            'i': "L’évolution des inégalités dépend des institutions et des "
                 "politiques autant que des mécanismes économiques."}],
      faits=[{'f': "Le cours formule l’enchaînement : technologie, hausse de "
                   "la demande de travail qualifié, hausse de la rémunération "
                   "des qualifiés, creusement des écarts salariaux.",
              'p': "La formulation montre que le biais agit par la demande "
                   "relative de facteurs, et non par une baisse absolue de la "
                   "rémunération des peu qualifiés."}],
      termes=['progres technique biaise', 'automatisation',
              'taches routinieres'],
      dos=['n10-progres-technique-biaise', 'n10-polarisation']),

   nd('ia', 'L’intelligence artificielle', 'detail',
      "Les machines ne remplacent plus seulement la force physique mais "
      "certaines capacités cognitives : la frontière des tâches exposées se "
      "déplace.",
      grp=1,
      defi="L’intelligence artificielle désigne les techniques permettant à "
           "des systèmes informatiques d’accomplir des tâches de traitement "
           "de l’information jusque-là réservées à l’activité humaine. Le "
           "cours la situe dans la révolution informatique et numérique, dont "
           "elle constitue le jalon des années 2010-2020, après le "
           "microprocesseur de 1971, l’informatique personnelle, Internet et "
           "les plateformes.",
      mec=[("Le déplacement de la frontière des tâches",
            "L’intelligence artificielle étend l’automatisation à des "
            "opérations cognitives, ce qui déplace la frontière entre tâches "
            "automatisables et tâches humaines vers des activités jusque-là "
            "protégées."),
           ("La dépendance à une infrastructure préexistante",
            "Son déploiement suppose des données massives, une puissance de "
            "calcul et des réseaux, tous produits par les phases antérieures "
            "de la révolution numérique : elle en est tributaire."),
           ("L’effet incertain sur la productivité mesurée",
            "Les gains peuvent rester invisibles dans les indicateurs si les "
            "services sont gratuits ou si les améliorations portent sur la "
            "qualité, ce qu’Aghion souligne à propos du numérique en "
            "général.")],
      opp=[{'t': "Les innovations récentes, intelligence artificielle "
                 "comprise, produisent peu de gains de productivité comparés "
                 "à ceux des innovations passées.",
            'qui': "Robert Gordon",
            'rep': "Le diagnostic est empiriquement étayé mais contesté par "
                   "les difficultés de mesure et par le délai de constitution "
                   "des grappes, qui a été de plusieurs décennies pour "
                   "l’électricité."}],
      aut=[{'n': "Robert Gordon",
            'i': "Les innovations récentes améliorent le confort et modifient "
                 "les usages sans produire de gains de productivité "
                 "comparables aux précédentes."},
           {'n': "Philippe Aghion",
            'i': "Les gains du numérique pourraient être sous-estimés par les "
                 "indicateurs existants."},
           {'n': "Daron Acemoglu",
            'i': "Les technologies ne sont pas neutres : leurs effets sur "
                 "l’emploi et les salaires dépendent de l’usage qui en est "
                 "fait."}],
      faits=[{'f': "Le cours rapporte le débat : certains comptent trois "
                   "révolutions industrielles, d’autres quatre en "
                   "distinguant numérique et intelligence artificielle.",
              'p': "Le désaccord porte sur un critère et non sur un fait : il "
                   "faut donc expliciter le critère retenu pour trancher."}],
      termes=['intelligence artificielle', 'economie numerique',
              'revolution numerique'],
      dos=['n2-ia', 'n2-numerique']),

   nd('polarisation', 'La polarisation des emplois', 'limite',
      "Les extrémités de la chaîne captent la valeur, le milieu décroche. "
      "Giraud oppose activités nomades, exposées, et sédentaires, protégées "
      "par leur ancrage.",
      grp=1,
      defi="La polarisation désigne l’écartement des positions dans la "
           "distribution des emplois et des rémunérations : les activités "
           "qualifiées et immatérielles captent une part croissante de la "
           "valeur, tandis que les tâches routinières et exposées à la "
           "concurrence internationale voient leur rémunération relative "
           "reculer. Le cours la documente par la courbe du sourire et par le "
           "modèle nomades-sédentaires.",
      mec=[("La concentration de la valeur aux extrémités",
            "Dans une chaîne mondiale, conception et services immatériels "
            "captent une part croissante de la valeur, l’assemblage de moins "
            "en moins : la répartition des gains suit la position occupée "
            "dans la chaîne et non le volume produit."),
           ("Le partage entre activités nomades et sédentaires",
            "Les activités nomades peuvent se localiser dans plusieurs pays "
            "et sont donc mises en concurrence internationale, les "
            "sédentaires sont protégées par leur ancrage territorial : "
            "l’exposition, et non le secteur, détermine la position."),
           ("Le cumul des deux pressions",
            "Les travailleurs peu qualifiés des secteurs exposés subissent à "
            "la fois la concurrence internationale, qui permet la "
            "délocalisation, et le progrès technique biaisé, qui automatise "
            "les tâches routinières.")],
      aut=[{'n': "Pierre-Noël Giraud",
            'i': "Les activités nomades sont exposées à la concurrence "
                 "mondiale, les sédentaires sont protégées par leur ancrage "
                 "territorial."},
           {'n': "Branko Milanovic",
            'i': "La mondialisation réduit certaines inégalités entre pays "
                 "tout en accroissant des inégalités internes."}],
      faits=[{'f': "Le cours identifie les grands perdants : les non-qualifiés "
                   "des secteurs exposés, qui cumulent la concurrence "
                   "internationale et le progrès technique biaisé.",
              'p': "Le cumul de deux pressions indépendantes explique que "
                   "cette catégorie décroche plus fortement que les autres, "
                   "et non proportionnellement."}],
      termes=['polarisation des emplois', 'nomades et sedentaires',
              'courbe du sourire'],
      dos=['n10-polarisation', 'n10-precarite']),

   nd('deversement', 'Le déversement vers de nouveaux emplois', 'pilier',
      "Les gains de productivité libèrent de la main-d’œuvre, que les "
      "secteurs nouveaux absorbent : agriculture vers industrie, puis "
      "industrie vers services.",
      grp=1,
      defi="Le déversement désigne le mécanisme par lequel les gains de "
           "productivité d’un secteur libèrent de la main-d’œuvre que les "
           "secteurs en expansion absorbent. Il décrit la transformation "
           "séculaire de la structure des emplois : l’agriculture se vide au "
           "profit de l’industrie, puis l’industrie au profit des services. "
           "C’est le versant créateur de la destruction créatrice, et la "
           "raison pour laquelle le progrès technique n’a pas produit de "
           "chômage de masse permanent.",
      mec=[("La libération de main-d’œuvre",
            "Une hausse de productivité permet de produire autant avec moins "
            "de travail : à demande inchangée, des emplois sont libérés dans "
            "le secteur concerné."),
           ("L’absorption par les secteurs en expansion",
            "La baisse des prix permise par les gains de productivité "
            "augmente le pouvoir d’achat, qui se porte sur d’autres biens et "
            "services : la demande adressée aux secteurs nouveaux s’élève, et "
            "avec elle leur besoin de main-d’œuvre."),
           ("La condition de réussite",
            "Le déversement suppose que les travailleurs libérés soient "
            "employables dans les activités nouvelles. Lorsque les "
            "qualifications requises diffèrent trop, le transfert ne se fait "
            "pas et le chômage devient structurel.")],
      aut=[{'n': "Alfred Sauvy",
            'i': "Les gains de productivité déversent la main-d’œuvre d’un "
                 "secteur vers les secteurs en expansion."},
           {'n': "Jean Fourastié",
            'i': "Loi des trois secteurs : les gains de productivité "
                 "transforment la structure de l’emploi et conduisent à la "
                 "tertiarisation des économies avancées."}],
      faits=[{'f': "Les gains de productivité globale des facteurs inégaux "
                   "déplacent l’emploi : agriculture vers industrie, puis "
                   "industrie vers services.",
              'p': "La séquence historique est l’argument empirique le plus "
                   "direct contre la thèse d’une destruction nette d’emplois "
                   "par le progrès technique."}],
      termes=['deversement', 'gains de productivite', 'tertiarisation'],
      dos=['n1-productivite', 'n10-travail-emploi']),

   nd('institutions', 'Reconversion, formation, institutions', 'sortie',
      "Le bilan n’est positif que si le réemploi s’opère. Formation, "
      "accompagnement et institutions décident du solde — et de la "
      "possibilité de l’innovation suivante.",
      grp=1,
      defi="Les institutions déterminent si la destruction créatrice produit "
           "effectivement un gain collectif. Deux fonctions distinctes leur "
           "incombent : accompagner les perdants, sans quoi la transition "
           "devient politiquement intenable, et empêcher les positions "
           "acquises de bloquer les entrants, sans quoi l’innovation "
           "suivante n’a pas lieu. Le cours relie explicitement ces deux "
           "conditions : la destruction créatrice n’est ni automatique ni "
           "spontanément bénéfique.",
      mec=[("L’accompagnement des perdants",
            "Formation, indemnisation et reconversion transforment une perte "
            "individuelle en transition. Sans elles, la destruction subsiste "
            "sans la création pour les personnes et les territoires "
            "concernés."),
           ("La protection des entrants",
            "Les acteurs installés ont les moyens de retarder les innovations "
            "qui menacent leur position : le droit de la concurrence et "
            "l’ouverture à l’entrée sont donc des conditions de la dynamique "
            "elle-même."),
           ("Le bouclage sur l’innovation suivante",
            "Une main-d’œuvre formée et des marchés ouverts sont les "
            "conditions de la grappe suivante : les institutions ne se "
            "contentent pas de réparer, elles rendent possible le cycle "
            "ultérieur.")],
      args=[{'a': "Les politiques de reconversion ne sont pas une "
                  "compensation morale : elles sont la condition pour que le "
                  "redéploiement des ressources ait lieu, donc pour que le "
                  "gain collectif se réalise.",
             'lim': "Elles ne garantissent pas le réemploi au même niveau de "
                    "salaire ni dans le même territoire, ce qui laisse "
                    "subsister une perte pour les personnes concernées."}],
      aut=[{'n': "Philippe Aghion",
            'i': "La croissance par destruction créatrice dépend du niveau de "
                 "recherche et développement et de l’intensité de la "
                 "concurrence, et exige un accompagnement public des "
                 "perdants."},
           {'n': "Daron Acemoglu",
            'i': "Les institutions déterminent si la destruction créatrice "
                 "peut s’opérer."}],
      termes=['politiques de l emploi', 'formation', 'employabilite',
              'flexicurite'],
      dos=['n10-flexibilite', 'n10-travail-emploi']),
  ],
  [
   ln('coeur', 'invention', 'commence par',
      "Le cycle démarre lorsqu’une invention devient innovation, "
      "c’est-à-dire lorsqu’un entrepreneur prend le risque de la mettre en "
      "œuvre. Tant qu’elle reste au laboratoire, elle ne détruit ni ne crée "
      "aucun emploi.", 'cause'),
   ln('invention', 'grappe', 'entraîne',
      "Une innovation fondamentale n’est jamais isolée : elle appelle des "
      "innovations complémentaires, des infrastructures, des normes et des "
      "règles de responsabilité. C’est la grappe qui transforme une rupture "
      "technique en transformation économique.", 'cause'),
   ln('grappe', 'detruit', 'dévalorise l’ancien',
      "Le déploiement d’une grappe rend obsolètes les capitaux et les "
      "compétences de l’ancienne technique. La perte est immédiate, "
      "concentrée sur des personnes et des territoires identifiables : c’est "
      "le versant visible du processus.", 'cause'),
   ln('biais', 'detruit', 'cible les tâches routinières',
      "L’automatisation ne frappe pas au hasard : elle substitue des machines "
      "aux tâches standardisables. Le biais porte sur la nature des tâches, "
      "ce qui explique que des emplois intermédiaires, et pas seulement les "
      "moins qualifiés, soient touchés.", 'cause'),
   ln('ia', 'biais', 'déplace la frontière',
      "Avec l’intelligence artificielle, les machines ne remplacent plus "
      "seulement la force de travail physique mais certaines capacités "
      "cognitives. Le périmètre des tâches exposées change, donc le biais "
      "lui-même se déplace vers des emplois jusque-là protégés.",
      'renforce'),
   ln('grappe', 'ia', 'est en formation pour',
      "L’intelligence artificielle s’appuie sur l’infrastructure numérique "
      "constituée depuis les années 1970 et sa propre grappe est encore en "
      "formation : c’est précisément ce qui rend le débat sur ses effets "
      "indécidable aujourd’hui.", 'conditionne'),
   ln('biais', 'polarisation', 'creuse les écarts',
      "En élevant la productivité des qualifiés et en automatisant les tâches "
      "routinières, le progrès technique biaisé modifie la demande relative "
      "de facteurs : les rémunérations s’écartent sans qu’aucune baisse "
      "absolue soit nécessaire.", 'cause'),
   ln('detruit', 'polarisation', 'se concentre sur les exposés',
      "Les destructions ne se répartissent pas uniformément : les "
      "non-qualifiés des secteurs exposés cumulent la concurrence "
      "internationale et l’automatisation. Deux pressions indépendantes "
      "frappent la même catégorie, ce qui explique l’ampleur de son "
      "décrochage.", 'renforce'),
   ln('grappe', 'deversement', 'crée les secteurs d’accueil',
      "Les innovations complémentaires donnent naissance à des branches "
      "entières, dont l’emploi peut excéder celui du secteur d’origine. Sans "
      "ces secteurs nouveaux, la main-d’œuvre libérée n’aurait nulle part où "
      "se déverser.", 'cause'),
   ln('deversement', 'coeur', 'rend le bilan positif',
      "C’est le réemploi, et lui seul, qui transforme la destruction en gain "
      "collectif. Le cours est explicite : le processus est globalement "
      "bénéfique si le réemploi s’opère ; sinon la destruction subsiste sans "
      "la création.", 'conditionne'),
   ln('polarisation', 'institutions', 'appelle une réponse publique',
      "Les gains de l’innovation sont diffus et les pertes concentrées : les "
      "deux ne se compensent pas individuellement. L’asymétrie plaide pour "
      "une socialisation des coûts de transition plutôt que pour un blocage "
      "de l’innovation.", 'cause'),
   ln('institutions', 'deversement', 'conditionne',
      "Le déversement suppose que les travailleurs libérés soient employables "
      "dans les activités nouvelles. Lorsque les qualifications requises "
      "diffèrent trop, le transfert ne se fait pas : la formation est donc le "
      "maillon décisif.", 'conditionne'),
   ln('institutions', 'invention', 'rend possible le cycle suivant',
      "Les acteurs installés peuvent retarder les innovations qui menacent "
      "leur position : le cycle ne se referme que si les institutions "
      "protègent l’entrée. C’est ce bouclage qui fait de la destruction "
      "créatrice un processus et non un épisode.", 'conditionne'),
   ln('detruit', 'institutions', 'met à l’épreuve',
      "Chaque vague de destructions teste la capacité des institutions à "
      "accompagner : c’est à ce moment que se décide si l’innovation sera "
      "acceptée socialement ou contestée, et donc si elle pourra se "
      "poursuivre.", 'cause'),
  ],
  fam='Innovation, travail et entreprise')
