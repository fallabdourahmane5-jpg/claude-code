# -*- coding: utf-8 -*-
"""Visualisation 20 — La polycrise (type hub)."""

from vz_base import v, nd, ln

v('vz-polycrise', 'La polycrise du capitalisme contemporain',
  'Chapitre 1 · noyau et branches',
  'hub',
  "D. Plihon parle de polycrise pour désigner la superposition de crises "
  "qui ne sont pas de même nature et qui s’alimentent mutuellement. Le cœur "
  "en donne les quatre caractéristiques ; les branches les déploient — "
  "économique et sociale, climatique, démocratique, géopolitique — et les "
  "nœuds extérieurs montrent ce qu’elles changent au capitalisme lui-même.",
  [("Quatre crises, pas une crise à quatre faces",
    "Chacune a ses causes propres et ses instruments. Ce qui fait la "
    "polycrise est leur simultanéité et leurs renforcements croisés, non "
    "l’existence d’une cause unique que l’on pourrait traiter."),
   ("Suivre les liens croisés",
    "Les inégalités nourrissent la défiance politique, la défiance réduit "
    "l’acceptabilité des politiques climatiques, la rivalité géopolitique "
    "entrave la coopération que le climat exige. Ce sont ces flèches qui "
    "font la valeur de la notion."),
   ("Le capitalisme a changé de forme",
    "Le cours ne se contente pas du constat de crise : il décrit une "
    "reconfiguration — régionalisation des échanges, sécurisation des "
    "chaînes, concentration et puissance privée — qui modifie les "
    "mécanismes eux-mêmes.")],
  [
   nd('coeur', 'La polycrise', 'coeur',
      "Quatre crises simultanées : économique et sociale, climatique, "
      "démocratique, géopolitique. Leur superposition est ce qui fait la "
      "notion.",
      grp=0,
      defi="Le cours part d’un constat : le monde dans lequel nous évoluons "
           "est un monde capitaliste, mais qu’on caractérise en crise. "
           "D. Plihon parle de polycrise dans son livre sur les capitalismes "
           "contemporains, et en donne quatre grandes caractéristiques : une "
           "crise économique et sociale, le réchauffement climatique, une "
           "crise démocratique et une crise géopolitique. La notion ne "
           "désigne donc pas une crise plus grave que les autres, mais la "
           "simultanéité de crises de natures différentes.",
      mec=[("La superposition plutôt que l’addition",
            "Quatre crises simultanées ne font pas quatre problèmes "
            "indépendants : chacune réduit la capacité collective de traiter "
            "les autres, ce qui est précisément ce que la notion de polycrise "
            "cherche à nommer."),
           ("L’absence de cause unique",
            "Aucune des quatre ne se déduit des trois autres : les ramener à "
            "une cause commune — le capitalisme, la mondialisation — fait "
            "perdre ce que la notion apporte."),
           ("La difficulté d’ordonner les priorités",
            "Traiter l’une peut aggraver une autre : les politiques "
            "climatiques ont un coût social, la sécurisation des "
            "approvisionnements un coût économique. La polycrise est d’abord "
            "un problème d’arbitrage.")],
      faits=[{'f': "Le cours ouvre sur un ordre de grandeur : un PIB en "
                   "baisse de 7 % en France en 2020 et de 3,5 % dans le "
                   "monde.",
              'p': "Le chiffre situe le point de départ du constat : un choc "
                   "mondial simultané, dont la nature n’était pas économique, "
                   "a produit la contraction la plus forte depuis la guerre."}],
      aut=[{'n': "D. Plihon",
            'i': "Le capitalisme contemporain traverse une polycrise : crise "
                 "économique et sociale, réchauffement climatique, crise "
                 "démocratique et crise géopolitique."}],
      termes=['polycrise', 'capitalisme', 'crise'],
      dos=['n27-crise', 'n27-transformation-structurelle']),

   nd('economique', 'La crise économique et sociale', 'pilier',
      "Depuis 2007-2008 : inégalités de revenus, concentration des "
      "patrimoines, décrochage des classes moyennes des pays développés.",
      grp=1,
      defi="La première caractéristique est une crise économique et sociale, "
           "que le cours rattache à la crise de 2007-2008 et aux inégalités "
           "de revenus. Elle ne se réduit pas à un épisode récessif : c’est "
           "la persistance d’une croissance faible, d’une concentration "
           "croissante des patrimoines et d’un décrochage des catégories "
           "exposées qui en fait une crise durable.",
      mec=[("De la crise financière à la crise sociale",
            "L’effondrement du marché des subprimes se transforme en crise "
            "bancaire, crise boursière et récession mondiale : la sphère "
            "financière transmet son choc à l’emploi et aux revenus."),
           ("La persistance après le choc",
            "Croissance effective durablement faible, recul de la croissance "
            "potentielle, output gaps négatifs, faiblesse de l’investissement "
            "et chômage durable coexistent : le retour à la trajectoire "
            "antérieure n’a pas eu lieu."),
           ("Le décrochage des catégories exposées",
            "La classe moyenne des pays développés connaît une croissance "
            "réelle proche de zéro sur la période 1988-2008, d’où un "
            "sentiment de déclassement qui déborde largement l’analyse "
            "économique.")],
      aut=[{'n': "Branko Milanovic",
            'i': "La mondialisation réduit certaines inégalités entre pays "
                 "tout en accroissant des inégalités internes."},
           {'n': "Thomas Piketty",
            'i': "L’évolution des inégalités dépend des institutions et des "
                 "politiques autant que des mécanismes économiques."}],
      termes=['crise de 2008', 'inegalites de revenus', 'declassement'],
      dos=['n22-inegalites-revenus', 'n22-inegalites-entre-et-au-sein']),

   nd('climatique', 'Le réchauffement climatique', 'pilier',
      "Une contrainte physique qui ne se négocie pas, et un bien public "
      "mondial qu’aucun État ne peut produire seul.",
      grp=1,
      defi="La deuxième caractéristique est le réchauffement climatique. Il "
           "se distingue des trois autres par sa nature : ce n’est pas un "
           "déséquilibre économique ou politique mais une contrainte "
           "physique, dont le franchissement de seuils produit des effets "
           "difficilement réversibles. Le climat étant un bien public "
           "mondial, sa préservation ne peut être assurée par des États "
           "agissant isolément.",
      mec=[("Le caractère de bien public mondial",
            "Non-rivalité et non-exclusion : chaque État a intérêt à laisser "
            "les autres supporter le coût de la réduction, ce qui produit un "
            "équilibre non coopératif et une sous-production d’effort."),
           ("Le conflit avec l’horizon politique",
            "Les acteurs économiques raisonnent sur un horizon plus court que "
            "celui de la transition : le coût est immédiat et visible, le "
            "bénéfice différé et collectif."),
           ("La tension avec l’exigence sociale",
            "Les instruments efficaces frappent des consommations "
            "contraintes comme le chauffage et les déplacements : la "
            "politique climatique rencontre directement la question "
            "distributive.")],
      aut=[{'n': "Kate Raworth",
            'i': "L’économie doit se tenir dans un espace sûr et juste, entre "
                 "un plancher social et un plafond écologique."},
           {'n': "Mark Carney",
            'i': "Les acteurs économiques raisonnent sur un horizon plus "
                 "court que celui de la transition."}],
      termes=['rechauffement climatique', 'bien public mondial',
              'transition energetique'],
      dos=['n4-climat', 'n21-biens-publics-mondiaux']),

   nd('democratique', 'La crise démocratique', 'pilier',
      "Perte de confiance envers les institutions, abstention, recul de "
      "l’adhésion aux syndicats et aux partis, montée du populisme.",
      grp=1,
      defi="La troisième caractéristique est une crise démocratique, que le "
           "cours décrit par ses manifestations : perte de confiance envers "
           "les institutions et les politiques, abstention, baisse de "
           "l’adhésion aux syndicats et aux partis politiques, montée du "
           "populisme — lequel oppose des élites privilégiées à un peuple. "
           "Elle importe à l’analyse économique parce qu’elle conditionne la "
           "capacité d’adopter et de tenir des politiques de long terme.",
      mec=[("La défiance comme contrainte sur l’action publique",
            "Une politique dont le coût est immédiat et le bénéfice différé "
            "suppose que les citoyens créditent l’autorité qui la décide : la "
            "défiance supprime cette ressource."),
           ("L’affaiblissement des corps intermédiaires",
            "Le recul de l’adhésion aux syndicats et aux partis réduit les "
            "lieux où les arbitrages peuvent être négociés avant d’être "
            "imposés, ce qui déplace le conflit vers la rue ou vers "
            "l’abstention."),
           ("Le clivage élites / peuple",
            "La montée du populisme reformule les désaccords économiques en "
            "opposition de légitimité : l’argument technique perd son "
            "efficacité dès lors que son auteur est récusé.")],
      faits=[{'f': "Le cours relève que 70 % des jeunes pensent que les "
                   "politiques sont corrompus.",
              'p': "Le chiffre mesure l’ampleur de la défiance dans la "
                   "génération qui supportera le plus longtemps les effets "
                   "des décisions prises aujourd’hui."}],
      aut=[{'n': "Pierre Rosanvallon",
            'i': "L’État providence connaît une crise à trois dimensions : "
                 "financement, efficacité et légitimité."}],
      termes=['crise democratique', 'populisme', 'confiance',
              'abstention'],
      dos=['n27-confiance', 'n22-justice-sociale']),

   nd('geopolitique', 'La crise géopolitique', 'pilier',
      "Montée en puissance des pays émergents, affaiblissement des économies "
      "du centre, effondrement de l’ordre international bâti à partir de "
      "1945.",
      grp=1,
      defi="La quatrième caractéristique est une crise géopolitique, que le "
           "cours décrit en deux mouvements : la montée en puissance des pays "
           "émergents et l’affaiblissement relatif des économies du centre "
           "d’une part, l’effondrement de l’ordre international bâti à partir "
           "de 1945 d’autre part. Le second n’est pas la conséquence "
           "mécanique du premier : il tient aussi au retrait des puissances "
           "qui avaient construit cet ordre.",
      mec=[("Le déplacement du poids économique",
            "La part relative des économies traditionnelles diminue à mesure "
            "que des économies très peuplées s’industrialisent : la "
            "hiérarchie des puissances se recompose."),
           ("L’affaiblissement des règles communes",
            "Les deux principales puissances économiques adoptent de plus en "
            "plus des stratégies unilatérales et s’écartent de certaines "
            "règles : la crise vient des acteurs les plus puissants, non des "
            "plus faibles."),
           ("La recomposition de la géographie des échanges",
            "Les échanges augmentent davantage entre pays politiquement "
            "proches : le commerce ne cesse pas, il se réorganise selon les "
            "alignements.")],
      aut=[{'n': "Charles Kindleberger",
            'i': "Un ordre économique international stable nécessite qu’une "
                 "puissance dominante accepte d’assumer certaines "
                 "responsabilités collectives."},
           {'n': "Edward Luttwak",
            'i': "Après 1989, la rivalité de puissance change d’instruments : "
                 "la logique reste celle du conflit, la grammaire devient "
                 "celle du commerce."}],
      termes=['geopolitique', 'ordre international', 'emergents',
              'unilateralisme'],
      dos=['n21-gouvernance-mondiale', 'n17-fragmentation-geoeconomique']),

   nd('reconfiguration', 'La reconfiguration des échanges', 'detail',
      "Depuis le Covid : régionalisation des échanges, diversification des "
      "chaînes, sécurisation des approvisionnements et décarbonation.",
      grp=2, par='geopolitique',
      defi="Le cours ne décrit pas un simple recul de la mondialisation mais "
           "une reconfiguration : depuis le Covid, les échanges mondiaux se "
           "régionalisent et les chaînes d’approvisionnement se "
           "diversifient. Les objectifs assignés au commerce international "
           "changent en conséquence — sécurisation des chaînes "
           "d’approvisionnement et décarbonation — là où la fragmentation "
           "productive visait auparavant le seul coût.",
      mec=[("Du coût à la sécurité",
            "La mondialisation s’est longtemps basée sur la fragmentation du "
            "processus de production ; désormais ce n’est plus le seul "
            "critère, la robustesse de l’approvisionnement entrant dans "
            "l’arbitrage."),
           ("La régionalisation comme forme nouvelle",
            "Les flux ne disparaissent pas : ils se réorganisent sur des "
            "distances plus courtes et entre partenaires jugés plus sûrs, ce "
            "qui change la géographie sans réduire le volume."),
           ("La décarbonation comme critère commercial",
            "Les effets environnementaux du commerce dépendent fortement des "
            "technologies utilisées, ce qui conduit à mobiliser les "
            "politiques commerciales en faveur des productions les moins "
            "carbonées.")],
      aut=[{'n': "Janet Yellen",
            'i': "La sécurité des approvisionnements est devenue un objectif "
                 "des politiques économiques."}],
      termes=['regionalisation', 'chaines d approvisionnement',
              'securisation'],
      dos=['n17-relocalisation', 'n17-dependances-strategiques']),

   nd('finitude', 'Le capitalisme de la finitude', 'debat',
      "Chez Orain, une étape nouvelle : privatisation des espaces, "
      "concentration monopolistique, entreprises aussi puissantes que des "
      "nations.",
      grp=2, par='economique',
      defi="Le cours mobilise Arnaud Orain pour caractériser l’étape "
           "contemporaine du capitalisme : celle de la finitude. Trois "
           "traits la définissent — la privatisation des espaces, "
           "historiquement celle des mers entre la fin du XVIᵉ siècle et "
           "1815 ; la remise en cause de la concurrence par les monopoles ; "
           "et la constitution d’empires privés aussi puissants que des "
           "nations.",
      mec=[("La disparition de la concurrence qu’elle supposait",
            "Le capitalisme libéral reposait sur l’idée que plusieurs "
            "entreprises en compétition profitent aux consommateurs. Dans "
            "beaucoup de secteurs, quelques géants dominent presque tout et "
            "fixent leurs propres règles."),
           ("La constitution d’empires privés",
            "Certaines entreprises disposent de leurs propres réseaux — "
            "satellites, clouds, plateformes — de leurs propres territoires "
            "et d’une influence politique considérable : elles discutent "
            "d’égal à égal avec les gouvernements."),
           ("Le déplacement du pouvoir",
            "Le pouvoir politique et économique n’appartient plus seulement "
            "aux États mais aussi à ces acteurs qui contrôlent des pans "
            "entiers de l’activité : la souveraineté se trouve concurrencée "
            "de l’intérieur.")],
      aut=[{'n': "Arnaud Orain",
            'i': "Nous serions entrés dans un nouvel âge du capitalisme de la "
                 "finitude."},
           {'n': "Philippe Aghion",
            'i': "Certaines grandes entreprises peuvent freiner l’innovation "
                 "en empêchant l’entrée de nouveaux concurrents."}],
      termes=['capitalisme de la finitude', 'monopoles',
              'plateformes numeriques'],
      dos=['n2-plateforme', 'n18-pouvoir-multinationales']),

   nd('gouvernance', 'Le paradoxe de la coordination', 'limite',
      "Les États veulent retrouver leur souveraineté au moment précis où les "
      "problèmes exigent une coordination.",
      grp=2, par='climatique',
      defi="Le cours relève le paradoxe fondamental de la période : les États "
           "veulent retrouver leur souveraineté nationale alors que certains "
           "problèmes exigent une coordination, et la montée des tensions "
           "géopolitiques fait reculer la coopération. La difficulté n’est "
           "donc pas technique mais politique : le besoin de biens publics "
           "mondiaux s’accroît au moment où la capacité de les produire "
           "diminue.",
      mec=[("Le passager clandestin à l’échelle des États",
            "Sans coordination, chaque État a intérêt à laisser les autres "
            "supporter le coût : le comportement rationnel de chacun produit "
            "un résultat collectivement mauvais."),
           ("La voie de la puissance régulatrice",
            "À défaut de coordination mondiale, un grand marché peut imposer "
            "unilatéralement des règles servant un bien public : "
            "l’ajustement carbone aux frontières transforme la taille d’un "
            "marché en instrument climatique."),
           ("Le coût de l’absence de règle commune",
            "La fragmentation en blocs a un coût agrégé mesurable, et la "
            "rapidité de la rupture pèse autant que son ampleur : la "
            "coordination n’est pas seulement souhaitable, son absence se "
            "chiffre.")],
      aut=[{'n': "John Nash",
            'i': "Un équilibre non coopératif peut être collectivement "
                 "sous-optimal alors que chacun agit rationnellement."},
           {'n': "Dani Rodrik",
            'i': "L’hypermondialisation entre en conflit avec la démocratie "
                 "et la souveraineté nationale."}],
      termes=['cooperation internationale', 'souverainete',
              'biens publics mondiaux'],
      dos=['n21-cooperation-internationale', 'n21-biens-publics-mondiaux']),

   nd('lecture', 'Crise de régime ou succession de chocs ?', 'sortie',
      "Quatre accidents simultanés, ou l’épuisement d’une configuration "
      "institutionnelle ? Le choix de lecture commande la réponse.",
      grp=2, par='coeur',
      defi="La notion de polycrise laisse ouverte une question "
           "d’interprétation que le programme pose ailleurs avec précision : "
           "s’agit-il d’une succession de chocs, auquel cas les instruments "
           "conjoncturels suffisent, ou de l’épuisement d’un mode de "
           "régulation, auquel cas la sortie suppose une reconfiguration "
           "institutionnelle ? Robert Boyer lit ainsi 1929 comme "
           "l’épuisement du mode de régulation concurrentiel et non comme un "
           "choc accidentel.",
      mec=[("La lecture par les chocs",
            "Chaque crise a sa cause propre et son instrument : relance pour "
            "l’économique, prix du carbone pour le climatique, réforme "
            "institutionnelle pour le démocratique. Le traitement est "
            "sectoriel."),
           ("La lecture par le régime",
            "Les institutions qui soutenaient l’accumulation — formes de la "
            "concurrence, rapport salarial, régime monétaire, ordre "
            "international — cessent d’être cohérentes entre elles : la "
            "simultanéité des crises en est le symptôme."),
           ("Ce que le choix implique",
            "Dans le premier cas, les instruments existent et il reste à les "
            "employer ; dans le second, ils stabilisent sans résoudre, et la "
            "crise réapparaît tant que la configuration n’a pas changé.")],
      args=[{'a': "La lecture par le régime explique la simultanéité, que la "
                  "lecture par les chocs doit traiter comme une coïncidence.",
             'lim': "Elle est plus difficile à opérationnaliser : désigner "
                    "une configuration épuisée ne dit pas quelle "
                    "configuration lui succédera, ni par quels moyens."}],
      aut=[{'n': "Robert Boyer",
            'i': "La crise de 1929 s’analyse comme l’épuisement du mode de "
                 "régulation concurrentiel, et non comme un choc accidentel."},
           {'n': "Michel Aglietta",
            'i': "Le capitalisme s’analyse comme un système historique dont "
                 "les crises relèvent de transformations structurelles."}],
      termes=['mode de regulation', 'crise structurelle',
              'ecole de la regulation'],
      dos=['n13-cycles-economiques', 'n27-transformation-structurelle']),
  ],
  [
   ln('coeur', 'economique', 'se manifeste par',
      "La première caractéristique que le cours retient est la crise "
      "économique et sociale, rattachée à 2007-2008 et aux inégalités de "
      "revenus : c’est par elle que le constat de polycrise est introduit.",
      'cause'),
   ln('coeur', 'climatique', 'se manifeste par',
      "Le réchauffement climatique figure au même rang que les trois autres "
      "crises, alors qu’il n’est pas de même nature : c’est une contrainte "
      "physique, non un déséquilibre économique ou politique.", 'cause'),
   ln('coeur', 'democratique', 'se manifeste par',
      "Perte de confiance envers les institutions, abstention, recul de "
      "l’adhésion aux syndicats et aux partis, montée du populisme : la "
      "troisième caractéristique est celle qui conditionne la capacité à "
      "traiter les autres.", 'cause'),
   ln('coeur', 'geopolitique', 'se manifeste par',
      "Montée en puissance des pays émergents, affaiblissement des économies "
      "du centre, effondrement de l’ordre international bâti à partir de "
      "1945 : la quatrième caractéristique est celle qui défait le cadre des "
      "solutions.", 'cause'),
   ln('economique', 'democratique', 'nourrit',
      "Le décrochage des classes moyennes des pays développés et la "
      "concentration au sommet alimentent un sentiment de déclassement : "
      "c’est le lien que le cours établit entre analyse économique des "
      "inégalités et sociologie politique de la mondialisation.", 'cause'),
   ln('democratique', 'climatique', 'entrave',
      "Une politique dont le coût est immédiat et le bénéfice différé suppose "
      "que les citoyens créditent l’autorité qui la décide. Le cours en donne "
      "l’exemple : une politique environnementale soutenue puis abandonnée "
      "parce qu’elle coûte des voix.", 'limite'),
   ln('geopolitique', 'gouvernance', 'fait reculer',
      "La montée des tensions géopolitiques fait reculer la coopération au "
      "moment précis où certains problèmes l’exigent : la crise des "
      "puissances devient une crise des règles communes.", 'cause'),
   ln('climatique', 'gouvernance', 'exige une coordination',
      "Le climat est un bien public mondial : aucun État ne peut résoudre "
      "seul un problème mondial, et chacun a intérêt à laisser les autres "
      "supporter le coût.", 'conditionne'),
   ln('geopolitique', 'reconfiguration', 'réorganise les échanges',
      "Depuis le Covid, la régionalisation des échanges et la diversification "
      "des chaînes d’approvisionnement traduisent l’entrée du risque "
      "politique dans l’arbitrage de localisation.", 'cause'),
   ln('reconfiguration', 'climatique', 'intègre la décarbonation',
      "Les objectifs assignés au commerce international deviennent la "
      "sécurisation des approvisionnements et la décarbonation : la "
      "contrainte climatique entre dans la politique commerciale.",
      'renforce'),
   ln('economique', 'finitude', 'accompagne',
      "La concentration des patrimoines au sommet et la constitution "
      "d’empires privés relèvent du même mouvement : la part du pouvoir "
      "économique soustraite à la concurrence et à la décision publique "
      "s’accroît.", 'renforce'),
   ln('finitude', 'democratique', 'déplace le pouvoir',
      "Si le pouvoir politique et économique n’appartient plus seulement aux "
      "États mais à des acteurs privés qui discutent d’égal à égal avec les "
      "gouvernements, alors la décision démocratique perd une partie de son "
      "objet.", 'cause'),
   ln('finitude', 'geopolitique', 'concurrence les États',
      "Des entreprises aussi puissantes que des nations, dotées de leurs "
      "propres réseaux et territoires : la recomposition des puissances ne se "
      "joue plus seulement entre États.", 'renforce'),
   ln('gouvernance', 'lecture', 'alimente l’hypothèse structurelle',
      "Si le besoin de coordination s’accroît au moment où la capacité de la "
      "produire diminue, l’hypothèse d’une incohérence entre institutions "
      "devient plus économe que celle d’une série d’accidents.", 'cause'),
   ln('lecture', 'coeur', 'reformule la question',
      "La polycrise n’est pas seulement un constat : selon qu’on y lit une "
      "succession de chocs ou l’épuisement d’un régime, les instruments "
      "conjoncturels suffisent ou ne font que stabiliser.", 'renforce'),
   ln('reconfiguration', 'economique', 'en déplace les coûts',
      "Raccourcir et sécuriser les chaînes augmente les coûts de production "
      "et peut élever les prix : la réponse à la crise géopolitique a un prix "
      "économique et social immédiat.", 'limite'),
  ],
  fam='Société, inégalités et transversal')
