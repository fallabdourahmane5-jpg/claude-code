# -*- coding: utf-8 -*-
"""Visualisation 2 — Le développement et le rattrapage (type strates)."""

from vz_base import v, nd, ln

v('vz-developpement', 'Le développement et le rattrapage',
  'Chapitre 7 · quatre étages de raisonnement',
  'strates',
  "Le développement n’est pas une croissance plus forte : c’est une "
  "transformation de structure. Cette visualisation suit les quatre étages "
  "par lesquels le chapitre y conduit : définir et mesurer, comprendre ce qui "
  "bloque, examiner les stratégies qui ont été tentées, puis trancher les "
  "débats qu’elles ont laissés ouverts. Chaque étage se lit de gauche à "
  "droite, et les flèches montrent comment l’un commande le suivant.",
  [("Quatre bandes, quatre questions",
    "La première bande définit et mesure, la deuxième explique le blocage, la "
    "troisième présente les stratégies, la quatrième ouvre les débats. Un "
    "sujet de dissertation se construit presque toujours en descendant les "
    "bandes dans cet ordre."),
   ("La controverse structurante",
    "Tout le chapitre se joue sur une question : le sous-développement est-il "
    "un retard, donc rattrapable par les mêmes étapes, ou une structure "
    "produite par l’insertion internationale ? Rostow et Prebisch tiennent "
    "les deux bouts, et chaque stratégie découle de la réponse retenue."),
   ("Ne pas opposer interne et externe",
    "Les liens « se complètent » signalent les endroits où le cours refuse de "
    "choisir : le cercle vicieux interne et l’insertion externe défavorable "
    "se renforcent au lieu de s’exclure. C’est la nuance qui fait la "
    "différence entre une copie scolaire et une copie solide.")],
  [
   # ---------------------------------------------------- 1. définir, mesurer
   nd('defi', 'Développement ≠ croissance', 'coeur',
      "Croissance : un flux de production en plus. Développement : des "
      "structures qui changent. Perroux impose la distinction, et le cours en "
      "tire que richesse et développement ne se confondent pas.",
      grp=1,
      defi="Le développement désigne l’ensemble des transformations "
           "structurelles, sociales et institutionnelles qui accompagnent et "
           "rendent durable l’élévation du niveau de vie : industrialisation, "
           "urbanisation, scolarisation, amélioration de la santé, "
           "construction d’institutions. François Perroux le distingue "
           "rigoureusement de la croissance, qui n’est qu’une augmentation "
           "quantitative de la production. La distinction n’est pas une "
           "nuance morale : elle est la distinction analytique dont tout le "
           "chapitre découle.",
      mec=[("L’élévation du revenu par habitant",
            "La croissance de la production par tête fournit les ressources "
            "matérielles sans lesquelles aucune transformation n’est "
            "finançable. Elle est nécessaire, mais elle ne détermine ni "
            "l’usage ni la répartition de ces ressources."),
           ("La transformation de la structure productive",
            "Le poids de l’agriculture recule au profit de l’industrie puis "
            "des services. Ce déplacement élève la productivité moyenne et "
            "transforme la nature des emplois et des qualifications "
            "requises."),
           ("L’investissement dans les capacités humaines",
            "Santé et éducation élèvent la productivité et la durée de vie "
            "active, mais constituent aussi des finalités en elles-mêmes : le "
            "développement est simultanément un moyen et une fin."),
           ("La construction institutionnelle",
            "Droit, administration, protection des contrats et fourniture de "
            "biens collectifs permettent aux transformations de se "
            "consolider. Sans elles, les gains de croissance restent "
            "réversibles.")],
      args=[{'a': "Le développement suppose la croissance : sans ressources "
                  "supplémentaires, ni l’investissement en santé et éducation "
                  "ni la construction institutionnelle ne sont finançables.",
             'lim': "La relation n’est pas réciproque : une croissance tirée "
                    "par une rente minière peut élever le revenu sans "
                    "transformer ni les structures ni les capacités."}],
      aut=[{'n': "François Perroux",
            'i': "La croissance est l’augmentation soutenue d’un indicateur "
                 "de dimension ; le développement est une transformation "
                 "structurelle et sociale."},
           {'n': "Amartya Sen",
            'i': "Le développement consiste en l’élargissement des "
                 "capabilités, c’est-à-dire des libertés réelles d’accomplir "
                 "ce que l’on a des raisons de valoriser."}],
      faits=[{'f': "Le classement des pays par l’indice de développement "
                   "humain diffère de leur classement par le revenu.",
              'p': "L’écart entre les deux rangs est l’argument empirique le "
                   "plus direct contre l’assimilation de la richesse au "
                   "développement."}],
      termes=['developpement', 'croissance et developpement', 'perroux'],
      dos=['n3-developpement', 'n3-sous-developpement']),

   nd('mesure', 'Mesurer : l’IDH et sa famille', 'pilier',
      "L’indice de développement humain combine revenu, espérance de vie et "
      "éducation. Il est suivi d’indices de correction, parce qu’une moyenne "
      "masque les distributions.",
      grp=1,
      defi="Le développement humain désigne l’élargissement des possibilités "
           "réelles offertes aux individus : vivre longtemps et en bonne "
           "santé, accéder au savoir, disposer d’un niveau de vie décent. "
           "L’indice de développement humain élaboré par le Programme des "
           "Nations unies pour le développement en est la mesure la plus "
           "répandue. Son intérêt pédagogique tient moins à son contenu qu’à "
           "ce que sa lecture révèle : l’écart entre le rang par l’indice et "
           "le rang par le revenu mesure la capacité d’un pays à convertir "
           "ses ressources en conditions de vie.",
      mec=[("L’agrégation de trois dimensions",
            "Revenu, espérance de vie et éducation sont normalisés puis "
            "combinés. L’indice résume en un nombre des grandeurs "
            "hétérogènes, ce qui permet la comparaison internationale."),
           ("La comparaison avec le classement par revenu",
            "L’écart entre le rang selon l’indice et le rang selon le revenu "
            "mesure la capacité d’un pays à convertir ses ressources en "
            "conditions de vie : un rang bien meilleur signale une conversion "
            "efficace, l’inverse une rente mal redistribuée."),
           ("La correction par les inégalités",
            "L’indice ajusté aux inégalités abaisse la valeur de l’indice en "
            "fonction de la dispersion observée dans chaque dimension, ce qui "
            "révèle le coût des inégalités en termes de développement."),
           ("Le passage aux privations concrètes",
            "L’indice de pauvreté multidimensionnelle ne se contente pas du "
            "revenu monétaire : il mesure des privations effectives dans "
            "plusieurs domaines, ce qui le rend plus directement "
            "opérationnel pour l’action publique.")],
      opp=[{'t': "Un indice composite masque les distributions : un pays peut "
                 "avoir un indice relativement élevé tout en conservant des "
                 "fragilités sociales profondes.",
            'qui': "le cours",
            'rep': "L’objection est admise par la construction même des "
                   "indicateurs complémentaires : elle ne disqualifie pas "
                   "l’indice, elle en borne l’usage et justifie le passage à "
                   "l’indice de pauvreté multidimensionnelle."},
           {'t': "Les indicateurs composites incorporent des choix normatifs "
                 "dans leur pondération, sous l’apparence d’une convention "
                 "technique.",
            'qui': "critique méthodologique",
            'rep': "Elle est fondée et invite à expliciter ces choix plutôt "
                   "qu’à renoncer à mesurer : l’absence d’indicateur laisse "
                   "le champ libre au seul revenu, qui incorpore lui aussi "
                   "des choix implicites."}],
      faits=[{'f': "Le Programme des Nations unies pour le développement a "
                   "élaboré l’indice de développement humain, l’indice ajusté "
                   "aux inégalités, l’indice d’inégalité de genre et l’indice "
                   "de pauvreté multidimensionnelle.",
              'p': "La progression de la liste suit celle des objections : "
                   "chaque indicateur répond à une insuffisance du "
                   "précédent."}],
      termes=['indice de developpement humain', 'idh',
              'pauvrete multidimensionnelle'],
      dos=['n3-humain', 'n3-ipm']),

   nd('capabilites', 'Les capabilités (Sen)', 'pilier',
      "Ce qui compte n’est pas le revenu mais la liberté réelle de le "
      "convertir en accomplissements. Deux personnes au même revenu peuvent "
      "avoir des possibilités très inégales.",
      grp=1,
      defi="Les capabilités désignent, chez Amartya Sen, l’ensemble des "
           "fonctionnements qu’une personne est réellement en mesure "
           "d’accomplir : se nourrir, se déplacer, se soigner, s’instruire, "
           "participer à la vie collective. L’approche déplace le critère "
           "d’évaluation du développement : ce qui compte n’est pas le revenu "
           "ou les biens détenus, mais la liberté effective de les convertir "
           "en accomplissements. La capabilité est la combinaison des "
           "ressources et des conditions — personnelles, sociales, "
           "environnementales — qui permettent cette conversion.",
      mec=[("La distinction entre moyens et possibilités",
            "Le revenu et les biens sont des moyens. La capabilité est la "
            "possibilité effective de les transformer en accomplissements, "
            "laquelle dépend de conditions extérieures aux ressources "
            "elles-mêmes."),
           ("Les facteurs de conversion",
            "Santé, âge, handicap, normes sociales, infrastructures "
            "disponibles déterminent ce qu’un même revenu permet réellement. "
            "Deux personnes également dotées peuvent donc avoir des libertés "
            "très inégales."),
           ("L’action publique sur les facteurs de conversion",
            "Éducation, santé, transports et accès à l’eau élargissent les "
            "capabilités à revenu inchangé. Ils ne redistribuent pas "
            "seulement des ressources : ils modifient ce que les ressources "
            "permettent.")],
      args=[{'a': "L’approche explique pourquoi deux pays au même revenu par "
                  "habitant présentent des conditions de vie très "
                  "différentes, et redéfinit la pauvreté comme privation de "
                  "possibilités réelles.",
             'lim': "Les facteurs de conversion sont difficiles à mesurer de "
                    "façon comparable, ce qui rend l’approche plus féconde "
                    "conceptuellement que statistiquement."}],
      aut=[{'n': "Amartya Sen",
            'i': "La pauvreté est une privation de capabilités et non un "
                 "niveau de revenu : le critère se déplace du disposer vers "
                 "le pouvoir faire."}],
      faits=[{'f': "La notion apparaît douze fois dans le chapitre consacré "
                   "au développement et dans aucun autre chapitre.",
              'p': "La concentration signale un concept propre à l’économie "
                   "du développement, à mobiliser dans ce cadre plutôt que "
                   "dans les sujets de croissance."}],
      termes=['capabilites', 'amartya sen', 'liberte reelle'],
      dos=['n3-capabilites', 'n3-humain']),

   # ------------------------------------------------- 2. pourquoi ça bloque
   nd('cercle', 'Le cercle vicieux de la pauvreté', 'pilier',
      "Faibles revenus → faible épargne → faible investissement → faible "
      "productivité → faibles revenus. Chez Nurkse, la pauvreté n’est pas "
      "seulement une conséquence : elle est une cause.",
      grp=2,
      defi="Le cercle vicieux de la pauvreté désigne l’enchaînement par "
           "lequel un faible revenu empêche l’épargne, donc l’investissement, "
           "donc les gains de productivité, donc le revenu futur. Le "
           "raisonnement s’oppose directement à la logique du rattrapage "
           "spontané : dans le modèle de Solow, un pays pauvre croît plus "
           "vite parce que le rendement du capital y est élevé ; Nurkse "
           "montre que ce raisonnement suppose une épargne disponible, "
           "condition que la pauvreté même interdit.",
      mec=[("Le faible revenu rend l’épargne impossible",
            "Lorsque le revenu couvre à peine la subsistance, la part qui "
            "peut être épargnée est négligeable : l’épargne n’est pas un "
            "choix d’arbitrage mais une impossibilité matérielle."),
           ("L’investissement ne se fait pas",
            "Sans épargne intérieure ni accès au financement extérieur, le "
            "stock de capital ne s’accroît pas. Le rendement théoriquement "
            "élevé du capital reste inexploité."),
           ("La productivité stagne et le cercle se referme",
            "Sans équipement nouveau ni formation, la productivité du travail "
            "demeure basse, ce qui maintient les revenus au niveau initial : "
            "le mécanisme se reproduit indéfiniment en l’absence d’impulsion "
            "extérieure."),
           ("La sortie suppose une impulsion extérieure",
            "Rompre le cercle suppose un apport externe — aide, "
            "investissement direct, ou mobilisation publique du capital — qui "
            "permette d’amorcer l’accumulation sans attendre l’épargne "
            "intérieure.")],
      aut=[{'n': "Ragnar Nurkse",
            'i': "Le cercle vicieux de la pauvreté : faibles revenus, faible "
                 "épargne, faible investissement, faible productivité, "
                 "faibles revenus de nouveau."}],
      faits=[{'f': "Le cours oppose explicitement Nurkse à Lewis : là où "
                   "Lewis pense le dualisme dépassable, Nurkse le juge "
                   "susceptible de s’auto-entretenir.",
              'p': "L’opposition est posée par le cours lui-même et fournit "
                   "une controverse directement exploitable en dissertation."}],
      termes=['cercle vicieux de la pauvrete', 'nurkse', 'trappe a pauvrete'],
      dos=['n3-cercle-vicieux', 'n3-trappe-pauvrete']),

   nd('dualisme', 'Le dualisme économique (Lewis)', 'detail',
      "Un secteur traditionnel agricole à faible productivité coexiste avec "
      "un secteur moderne plus productif mais limité. Passager pour Lewis, "
      "auto-entretenu pour Nurkse.",
      grp=2,
      defi="Le dualisme économique désigne la coexistence, au sein d’une même "
           "économie, d’un secteur traditionnel — surtout agricole, peu "
           "mécanisé, à faible productivité, à main-d’œuvre abondante et "
           "comportant un surplus de main-d’œuvre — et d’un secteur moderne — "
           "urbain, capitaliste, industriel, plus productif et capable "
           "d’investir, mais encore limité. L’analyse est due à Arthur Lewis, "
           "prix Nobel 1979.",
      mec=[("Le surplus de main-d’œuvre du secteur traditionnel",
            "Dans le secteur traditionnel, il y a beaucoup de travailleurs "
            "pour peu de gains de productivité : les revenus restent faibles "
            "et la demande intérieure limitée, ce qui freine à son tour "
            "l’expansion du secteur moderne."),
           ("Le transfert vers le secteur moderne",
            "Le secteur moderne attire progressivement cette main-d’œuvre. "
            "Chaque transfert élève la productivité moyenne de l’économie, "
            "puisque le travailleur passe d’un emploi à faible productivité à "
            "un emploi plus productif.")],
      opp=[{'t': "L’économie duale n’est que passagère : le secteur moderne "
                 "finira par absorber le surplus de main-d’œuvre.",
            'qui': "Arthur Lewis",
            'rep': "La thèse suppose une croissance suffisante du secteur "
                   "moderne, ce qui dépend de sa capacité d’investissement et "
                   "de l’existence de débouchés — deux conditions que la "
                   "pauvreté même peut interdire."}],
      aut=[{'n': "Arthur Lewis",
            'i': "Le sous-développement s’analyse comme un dualisme entre un "
                 "secteur traditionnel à faible productivité et un secteur "
                 "moderne plus productif mais limité."}],
      termes=['dualisme', 'secteur traditionnel', 'arthur lewis'],
      dos=['n3-dualisme']),

   nd('dependance', 'La dépendance : centre et périphérie', 'debat',
      "Pour la lecture tiers-mondiste, le sous-développement n’est pas un "
      "retard mais une relation : une insertion internationale subordonnée, "
      "durable, produite par l’échange lui-même.",
      grp=2,
      defi="La dépendance économique désigne la situation d’un pays dont "
           "l’activité, les revenus et les marges de décision sont commandés "
           "de l’extérieur : par la demande adressée à un petit nombre de "
           "produits primaires, par les importations technologiques "
           "indispensables à sa production, ou par les créanciers qui "
           "financent son déficit. Dans l’approche tiers-mondiste, elle n’est "
           "pas un retard provisoire mais une relation durable, produite par "
           "l’insertion même du pays dans l’économie mondiale.",
      mec=[("La division centre-périphérie",
            "Le monde se divise en un centre industriel et une périphérie "
            "spécialisée dans les produits primaires. La détérioration des "
            "termes de l’échange défavorise durablement la seconde, dont le "
            "pouvoir d’achat à l’exportation s’érode."),
           ("La concentration des exportations",
            "La dépendance ne se mesure pas au degré d’ouverture mais à la "
            "concentration des exportations : un pays très ouvert et "
            "diversifié est moins dépendant qu’un pays peu ouvert et "
            "mono-exportateur."),
           ("Le relais financier",
            "L’endettement extérieur ajoute un second canal : lorsque la "
            "dette est à taux variable auprès de créanciers privés, une "
            "décision monétaire prise ailleurs se transmet immédiatement aux "
            "budgets nationaux.")],
      opp=[{'t': "L’ouverture a précisément permis à certains pays dépendants "
                 "de devenir des puissances industrielles, ce qui infirmerait "
                 "la thèse du blocage.",
            'qui': "objection libérale",
            'rep': "Ces trajectoires n’ont rien d’une ouverture passive : "
                   "elles combinent intervention stratégique de l’État, "
                   "accueil sélectif des investissements étrangers et "
                   "transferts technologiques, c’est-à-dire une gestion "
                   "délibérée de la dépendance."}],
      aut=[{'n': "Raúl Prebisch",
            'i': "Le monde se divise en un centre industriel et une "
                 "périphérie primaire, et la détérioration des termes de "
                 "l’échange défavorise durablement la seconde."},
           {'n': "Arghiri Emmanuel",
            'i': "Les écarts internationaux de salaires rendent le "
                 "libre-échange structurellement inégal et défavorable à la "
                 "périphérie."},
           {'n': "Samir Amin",
            'i': "La périphérie est intégrée au capitalisme mondial, mais "
                 "dans une position subordonnée où une partie de son surplus "
                 "est captée."}],
      faits=[{'f': "À la fin des années 1970, environ 70 % de la dette du "
                   "Tiers Monde est à taux variable auprès de banques "
                   "privées.",
              'p': "Le chiffre explique mécaniquement la dépendance "
                   "financière : la hausse des taux décidée à Washington se "
                   "transmet immédiatement aux budgets des pays endettés, "
                   "sans qu’ils aient rien décidé."},
             {'f': "Arghiri Emmanuel publie L’échange inégal en 1969.",
              'p': "La référence est datable et permet de distinguer la "
                   "version structuraliste de Prebisch de la version radicale "
                   "de l’échange inégal."}],
      termes=['dependance', 'centre peripherie', 'echange inegal',
              'termes de l echange'],
      dos=['n3-dependance', 'n3-sous-developpement']),

   nd('malediction', 'La malédiction des ressources', 'limite',
      "Une rente minière ou pétrolière peut élever le revenu sans transformer "
      "les structures : revenus volatils, faible diversification, "
      "institutions fragilisées.",
      grp=2,
      defi="La malédiction des ressources naturelles désigne le paradoxe par "
           "lequel l’abondance d’une ressource exportable s’accompagne de "
           "performances de développement médiocres. Le mécanisme central est "
           "double : la rente dispense de transformer la structure "
           "productive, et elle devient un enjeu de captation qui fragilise "
           "les institutions. Le syndrome hollandais en est la forme "
           "monétaire : l’appréciation du change provoquée par les "
           "exportations de ressources dégrade la compétitivité des autres "
           "secteurs exposés.",
      mec=[("La rente dispense de la transformation",
            "Les recettes d’exportation procurent des devises sans qu’aucune "
            "montée en gamme soit nécessaire. Le revenu s’élève, mais la "
            "structure productive reste inchangée, donc le développement au "
            "sens de Perroux ne suit pas."),
           ("La volatilité des recettes",
            "Les revenus dépendent de cours mondiaux que le pays ne contrôle "
            "pas, ce qui rend la planification budgétaire et "
            "l’investissement de long terme difficiles."),
           ("Le syndrome hollandais",
            "L’afflux de devises apprécie la monnaie, renchérit les autres "
            "exportations et décourage l’industrie manufacturière : la "
            "ressource évince les activités qui auraient permis la "
            "diversification.")],
      args=[{'a': "La malédiction explique pourquoi un revenu par habitant "
                  "élevé peut coexister avec un développement humain faible : "
                  "le revenu mesure une rente, pas une capacité productive.",
             'lim': "Elle n’est pas une fatalité : la différence tient aux "
                    "institutions et à l’usage de la rente, ce qui renvoie au "
                    "débat institutionnaliste plutôt qu’à la géologie."}],
      faits=[{'f': "Certains pays restent dépendants des matières premières, "
                   "des produits agricoles ou des ressources énergétiques, ce "
                   "qui produit volatilité des revenus et faible "
                   "diversification.",
              'p': "C’est le lien direct entre spécialisation primaire et "
                   "blocage du développement : la vulnérabilité est "
                   "structurelle, non conjoncturelle."}],
      termes=['malediction des ressources', 'syndrome hollandais', 'rente'],
      dos=['n3-malediction', 'n3-hollandais']),

   # ----------------------------------------------------- 3. les stratégies
   nd('isi', 'Substituer aux importations', 'pilier',
      "Produire soi-même ce que l’on importait, derrière une protection. La "
      "réponse de Prebisch à la dépendance commerciale.",
      grp=3,
      defi="L’industrialisation par substitution aux importations consiste à "
           "développer une industrie nationale destinée à remplacer les "
           "produits manufacturés jusque-là importés, en protégeant le marché "
           "intérieur. Elle est préconisée par Prebisch, pour qui la réponse "
           "à la dépendance commerciale passe par une industrialisation "
           "protégée et une réduction de la spécialisation primaire, parfois "
           "dans une logique de développement autocentré.",
      mec=[("La protection du marché intérieur",
            "Droits de douane et contingents mettent la production nationale "
            "à l’abri de concurrents déjà installés, le temps qu’elle "
            "atteigne une échelle et une productivité suffisantes."),
           ("La montée vers les biens plus complexes",
            "La substitution commence par les biens de consommation courante, "
            "techniquement accessibles, avant de remonter vers les biens "
            "intermédiaires puis les biens d’équipement.")],
      opp=[{'t': "Tous les pays en développement n’ont pas un marché "
                 "intérieur suffisant pour permettre à une industrie protégée "
                 "d’atteindre la compétitivité.",
            'qui': "le cours",
            'rep': "L’objection est décisive pour les petits pays. Elle "
                   "conduit soit à l’intégration régionale, qui élargit le "
                   "marché protégé, soit à la stratégie inverse de promotion "
                   "des exportations."},
           {'t': "La protection prolongée engendre rente et absence "
                 "d’innovation plutôt que compétitivité.",
            'qui': "critique libérale",
            'rep': "L’objection impose une clause d’extinction et le maintien "
                   "d’une concurrence intérieure : l’échec de certaines "
                   "expériences tient à l’absence de ces garde-fous plus "
                   "qu’au principe."}],
      aut=[{'n': "Friedrich List",
            'i': "Une protection temporaire permet à une industrie naissante "
                 "d’atteindre la compétitivité, à condition de préparer sa "
                 "propre disparition."},
           {'n': "Paul Krugman",
            'i': "Une industrie potentiellement efficace peut ne jamais "
                 "émerger faute d’atteindre son échelle critique."}],
      termes=['substitution aux importations', 'industrie naissante',
              'protectionnisme educateur'],
      dos=['n3-isi']),

   nd('ipe', 'Promouvoir les exportations', 'pilier',
      "Produire pour le marché mondial : industrie légère d’abord, puis "
      "remontée de filière vers les biens intermédiaires et d’équipement.",
      grp=3,
      defi="L’industrialisation par promotion des exportations consiste à "
           "développer une industrie destinée au marché mondial plutôt qu’au "
           "seul marché intérieur. Le cours la présente comme une logique de "
           "développement extraverti, avec priorité donnée au départ à "
           "l’industrie légère exportatrice, et la distingue de la "
           "substitution d’exportations, qui vise à remplacer les produits "
           "primaires exportés par des produits à forte valeur ajoutée.",
      mec=[("L’entrée par l’industrie légère",
            "Le point d’entrée est l’industrie légère exportatrice, cohérente "
            "avec l’avantage de coût des économies à bas salaires : textile, "
            "assemblage, biens de consommation simples."),
           ("La remontée de filière",
            "La stratégie consiste ensuite à remonter les étapes de "
            "fabrication d’aval en amont : biens de consommation, puis biens "
            "intermédiaires, puis biens d’équipement. C’est elle qui "
            "transforme une spécialisation d’assemblage en capacité "
            "industrielle complète."),
           ("L’élargissement du marché accessible",
            "Viser le marché mondial lève la contrainte d’étroitesse du "
            "marché intérieur qui bloquait la substitution aux importations : "
            "l’échelle critique devient atteignable.")],
      opp=[{'t': "Sans remontée de filière, le pays reste cantonné à "
                 "l’assemblage et ne capte qu’une faible part de la valeur "
                 "ajoutée.",
            'qui': "le cours",
            'rep': "L’objection désigne la condition de réussite : la "
                   "promotion des exportations n’est développante que si elle "
                   "s’accompagne d’une stratégie explicite de remontée des "
                   "étapes de fabrication."}],
      aut=[{'n': "Paul Krugman",
            'i': "Les économies d’échelle rendent la taille du marché "
                 "accessible déterminante pour la compétitivité."}],
      faits=[{'f': "Le cours distingue la promotion des exportations de la "
                   "substitution d’exportations, qui remplace les produits "
                   "primaires par des produits à forte valeur ajoutée.",
              'p': "La distinction évite de confondre l’exportation de "
                   "produits primaires, qui prolonge la spécialisation, et "
                   "celle de produits manufacturés, qui la transforme."}],
      termes=['promotion des exportations', 'remontee de filiere',
              'developpement extraverti'],
      dos=['n3-ipe']),

   nd('etat', 'L’État développeur', 'pilier',
      "Sélectionner des secteurs stratégiques, organiser le rattrapage "
      "technologique, soutenir les exportations : au Japon, par le MITI. "
      "L’avantage comparatif y est construit, non subi.",
      grp=3,
      defi="L’État développeur désigne un État qui ne se contente pas de "
           "garantir le cadre du marché mais organise activement la "
           "transformation de la structure productive : sélection de secteurs "
           "stratégiques, organisation du rattrapage technologique, soutien "
           "aux exportations. Le cours en donne l’illustration japonaise : "
           "par l’intermédiaire du MITI, les pouvoirs publics ont accompagné "
           "la transformation des avantages comparatifs et la montée en gamme "
           "industrielle.",
      mec=[("La sélection de secteurs stratégiques",
            "L’État identifie les activités dont la maîtrise commande les "
            "suivantes et y concentre crédit, protection et commande "
            "publique, au lieu de laisser le marché seul arbitrer."),
           ("La mobilisation du capital",
            "Là où l’épargne privée est insuffisante ou dispersée, l’État, "
            "les banques ou de grandes institutions la rassemblent : c’est "
            "exactement le mécanisme que Gerschenkron décrit pour les "
            "industrialisations tardives."),
           ("L’ouverture sélective",
            "Le cours est net : un État fort ne signifie pas un État qui "
            "ferme son économie. Les trajectoires gagnantes reposent sur une "
            "ouverture sélective et pragmatique, et non sur l’autarcie.")],
      opp=[{'t': "L’État ne dispose pas de l’information nécessaire pour "
                 "sélectionner les secteurs d’avenir et se laisse guider par "
                 "les intérêts les mieux organisés.",
            'qui': "critique libérale",
            'rep': "L’expérience japonaise montre qu’une administration "
                   "insérée dans le tissu productif peut réduire l’asymétrie "
                   "d’information, mais elle confirme que l’autonomie à "
                   "l’égard des intérêts soutenus est la condition décisive."}],
      aut=[{'n': "Alexander Gerschenkron",
            'i': "Le retard peut être compensé par l’État, les banques ou de "
                 "grandes institutions mobilisant le capital."},
           {'n': "Dani Rodrik",
            'i': "Les trajectoires de développement dépendent des "
                 "institutions et des compromis politiques, sans recette "
                 "universelle."},
           {'n': "Philippe Aghion",
            'i': "La politique industrielle doit être différenciée selon la "
                 "distance à la frontière technologique."}],
      faits=[{'f': "Le cours précise que le Japon n’abandonne pas entièrement "
                   "sa spécialisation au marché : il organise la "
                   "transformation de ses avantages comparatifs.",
              'p': "La formule est essentielle : elle montre que l’avantage "
                   "comparatif est traité comme une variable construite et "
                   "non comme une donnée."}],
      termes=['etat developpeur', 'miti', 'politique industrielle',
              'gerschenkron'],
      dos=['n3-etat-developpeur']),

   nd('ajustement', 'Ajustement structurel et conditionnalité', 'limite',
      "Déréglementation, libéralisation, privatisation : les équilibres "
      "financiers sont restaurés, souvent au prix d’un coût social élevé.",
      grp=3,
      defi="Les plans d’ajustement structurel sont des programmes de réformes "
           "imposés ou fortement encouragés par le FMI et la Banque mondiale "
           "en échange d’une aide financière, d’un rééchelonnement de la dette "
           "ou d’un soutien à la solvabilité. Ils visent à rétablir les "
           "équilibres macroéconomiques et la confiance des créanciers par la "
           "stabilisation monétaire, la réduction des déficits, la "
           "libéralisation, l’ouverture, la privatisation et la "
           "déréglementation. John Williamson les rassemble en 1989 sous le "
           "nom de Consensus de Washington.",
      mec=[("Le financement contre conditionnalité",
            "Ce n’est pas une politique choisie mais une politique négociée "
            "sous contrainte de financement : l’accès aux ressources est "
            "subordonné à l’adoption du programme."),
           ("La contraction de la demande intérieure",
            "Hausse des taux, baisse des dépenses publiques, réduction des "
            "salaires publics, recul de la consommation : l’effet récessif "
            "n’est pas un accident mais la conséquence directe des "
            "instruments retenus pour dégager un excédent extérieur.")],
      opp=[{'t': "Les ajustements ont aggravé la pauvreté et les inégalités "
                 "au nom d’équilibres comptables.",
            'qui': "critique sociale",
            'rep': "Le coût social est avéré, mais la comparaison pertinente "
                   "n’est pas avec une situation stable : sans financement, "
                   "le pays aurait subi un défaut, dont le coût social aurait "
                   "pu être supérieur."},
           {'t': "La conditionnalité organise une perte de souveraineté, "
                 "puisqu’un créancier extérieur décide des choix budgétaires "
                 "du pays.",
            'qui': "critique souverainiste",
            'rep': "La perte d’autonomie est réelle, mais elle commence avec "
                   "l’endettement lui-même : la conditionnalité la rend "
                   "visible plutôt qu’elle ne la crée."}],
      aut=[{'n': "John Williamson",
            'i': "Les plans d’ajustement s’inscrivent dans ce qu’il nomme en "
                 "1989 le Consensus de Washington."},
           {'n': "Paul Volcker",
            'i': "La politique monétaire restrictive de la Fed à partir de "
                 "1979 déclenche la crise de la dette des pays en "
                 "développement."}],
      faits=[{'f': "La trilogie à retenir est : déréglementation, "
                   "libéralisation, privatisation.",
              'p': "Elle condense le contenu du programme et permet de le "
                   "restituer en une ligne avant d’en discuter les effets."}],
      termes=['ajustement structurel', 'consensus de washington',
              'conditionnalite'],
      dos=['n3-ajustement', 'n3-consensus']),

   # --------------------------------------------------------- 4. les débats
   nd('etapes', 'Retard ou structure ? Rostow contre Prebisch', 'debat',
      "Pour Rostow, le sous-développement est un retard que des étapes "
      "comblent. Pour Prebisch, c’est une position dans une relation. Tout le "
      "choix des stratégies en découle.",
      grp=4,
      defi="Le débat porte sur la nature même du sous-développement. Walt "
           "Whitman Rostow décrit une succession d’étapes par lesquelles "
           "toute économie passerait : le sous-développement n’est alors "
           "qu’un retard, et le rattrapage consiste à parcourir les mêmes "
           "étapes plus vite. Raul Prebisch soutient au contraire que le "
           "sous-développement résulte d’une insertion internationale "
           "défavorable : ce n’est pas un décalage dans le temps mais une "
           "position dans une structure. Le cours qualifie la lecture par "
           "étapes de linéaire et d’ethnocentrique.",
      mec=[("La lecture par étapes",
            "Une société traditionnelle réunit les conditions préalables, "
            "connaît un décollage, puis une marche vers la maturité et la "
            "consommation de masse. Le modèle fournit une feuille de route et "
            "explique le rôle du taux d’investissement."),
           ("L’objection structuraliste",
            "Si la périphérie est spécialisée dans les produits primaires et "
            "subit la détérioration des termes de l’échange, aucune étape ne "
            "se franchit spontanément : il faut changer la spécialisation "
            "elle-même."),
           ("La position intermédiaire de Gerschenkron",
            "Le retard modifie les modalités du rattrapage : plus un pays "
            "s’industrialise tard, plus il mobilise des institutions de "
            "substitution — banques, État — pour rassembler le capital. Les "
            "étapes ne se répètent donc pas à l’identique.")],
      opp=[{'t': "Le sous-développement n’est pas un retard mais une "
                 "structure produite par des rapports de domination "
                 "internationaux.",
            'qui': "Raul Prebisch",
            'rep': "L’objection déplace l’explication de l’intérieur vers "
                   "l’extérieur. Elle est décisive contre les lectures "
                   "purement nationales, sans pour autant exonérer les "
                   "institutions internes."}],
      aut=[{'n': "Walt Whitman Rostow",
            'i': "Le développement suit une succession d’étapes, le "
                 "sous-développement n’étant qu’un retard et non une impasse "
                 "structurelle."},
           {'n': "Alexander Gerschenkron",
            'i': "Les modalités du rattrapage dépendent du point de départ et "
                 "des institutions disponibles : le retard appelle des "
                 "substituts institutionnels."},
           {'n': "Raul Prebisch",
            'i': "Le sous-développement résulte d’une insertion "
                 "internationale défavorable et non d’un simple retard."}],
      termes=['rostow', 'etapes de la croissance', 'decollage',
              'gerschenkron'],
      dos=['n1-rattrapage', 'n3-sous-developpement']),

   nd('trappe', 'La trappe à revenu intermédiaire', 'limite',
      "Un pays qui n’est plus pauvre mais ne rejoint pas les pays "
      "développés : il lui manque innovation, capital humain, productivité et "
      "technologie.",
      grp=4,
      defi="La trappe à revenu intermédiaire désigne, selon la formulation du "
           "cours, la situation d’un pays qui n’est plus pauvre mais n’arrive "
           "pas à rejoindre les pays développés. La cause est identifiée "
           "précisément : il peut manquer d’innovation, de capital humain, de "
           "productivité et de technologie. Le blocage n’est donc pas un "
           "défaut d’accumulation mais un défaut de montée en gamme — ce qui "
           "distingue nettement cette trappe du cercle vicieux de la "
           "pauvreté, qui porte sur l’amorçage.",
      mec=[("L’épuisement de l’avantage de coût",
            "La hausse des salaires qui accompagne le rattrapage retire au "
            "pays son avantage sur les activités intensives en travail, sans "
            "lui donner encore les capacités des économies de la frontière "
            "technologique."),
           ("Le défaut de capacités d’innovation",
            "Faute de recherche, de capital humain et de technologie propres, "
            "le pays ne peut pas remplacer l’avantage perdu par un avantage "
            "de qualité ou de nouveauté.")],
      opp=[{'t': "La trappe n’est pas une fatalité : plusieurs économies "
                 "l’ont franchie en construisant des capacités d’innovation.",
            'qui': "objection empirique",
            'rep': "L’objection confirme le diagnostic plutôt qu’elle ne "
                   "l’infirme : ce sont bien les capacités d’innovation, et "
                   "non l’accumulation, qui permettent le franchissement."}],
      aut=[{'n': "Robert Lucas",
            'i': "Le capital humain est un moteur endogène de la croissance, "
                 "par les externalités qu’il engendre."},
           {'n': "Philippe Aghion",
            'i': "La politique industrielle doit être différenciée selon la "
                 "distance à la frontière technologique."}],
      termes=['trappe a revenu intermediaire', 'montee en gamme',
              'capital humain'],
      dos=['n3-trappe-intermediaire', 'n3-emergence']),
  ],
  [
   ln('defi', 'mesure', 'oblige à mesurer autrement',
      "Si le développement est multidimensionnel, aucun indicateur monétaire "
      "ne peut le saisir : c’est exactement ce qui justifie la construction "
      "d’indicateurs synthétiques par le Programme des Nations unies pour le "
      "développement. La définition commande la mesure.", 'mesure'),
   ln('mesure', 'capabilites', 'reste une approximation de',
      "Le cours présente l’indice de développement humain comme une "
      "approximation assumée des capabilités : trois dimensions ne peuvent "
      "résumer l’ensemble des libertés réelles, mais elles en donnent un "
      "indicateur comparable. Les capabilités servent donc de critère "
      "d’évaluation des indicateurs plus que d’indicateur elles-mêmes.",
      'limite'),
   ln('capabilites', 'defi', 'redéfinit la finalité',
      "Chez Sen, le développement n’est pas la transformation des structures "
      "pour elles-mêmes mais l’élargissement de ce que les individus peuvent "
      "réellement faire. Le critère se déplace du disposer vers le pouvoir "
      "faire, ce qui donne à l’éducation et à la santé un statut de fin et "
      "non de moyen.", 'conditionne'),
   ln('defi', 'cercle', 'n’est pas automatique',
      "Si le développement supposait seulement la croissance, un pays pauvre "
      "rattraperait spontanément les autres puisque le rendement du capital y "
      "est élevé. Le cercle vicieux explique pourquoi ce raisonnement "
      "échoue : il suppose une épargne que la pauvreté interdit.", 'limite'),
   ln('cercle', 'dualisme', 'explique pourquoi il persiste',
      "Là où Lewis pense que le transfert de main-d’œuvre du secteur "
      "traditionnel vers le secteur moderne résorbera le dualisme, Nurkse "
      "objecte que l’expansion du secteur moderne suppose une épargne et des "
      "débouchés que la pauvreté même interdit : le dualisme devient un "
      "équilibre et non une étape.", 'oppose'),
   ln('dependance', 'cercle', 'se complète avec',
      "Les deux explications sont compatibles et le cours les traite comme "
      "telles : une insertion internationale défavorable comprime les "
      "revenus, ce qui alimente le cercle vicieux interne. L’externe et "
      "l’interne se renforcent au lieu de s’exclure.", 'renforce'),
   ln('malediction', 'defi', 'dissocie revenu et développement',
      "Une rente minière élève le revenu sans transformer la structure "
      "productive : c’est le contre-exemple le plus net de la distinction de "
      "Perroux, puisque la croissance s’y produit sans développement.",
      'limite'),
   ln('dependance', 'isi', 'commande la stratégie',
      "C’est parce que la spécialisation primaire est jugée défavorable que "
      "Prebisch recommande de produire soi-même les biens manufacturés "
      "importés : la substitution aux importations est la conséquence "
      "logique du diagnostic de dépendance.", 'cause'),
   ln('isi', 'ipe', 'bute sur la taille du marché',
      "La substitution aux importations suppose un marché intérieur assez "
      "large pour qu’une industrie protégée atteigne la compétitivité. Les "
      "petits pays n’en disposent pas, ce qui conduit à viser le marché "
      "mondial — ou à élargir le marché protégé par l’intégration "
      "régionale.", 'limite'),
   ln('ipe', 'etat', 'suppose une remontée organisée',
      "La promotion des exportations n’est développante que si elle "
      "s’accompagne d’une remontée de filière. Or celle-ci ne va pas de soi : "
      "elle suppose un acteur capable d’orienter crédit, formation et "
      "technologie, ce que le cours appelle l’État développeur.",
      'conditionne'),
   ln('cercle', 'etat', 'justifie une impulsion publique',
      "Si l’épargne privée est structurellement insuffisante, l’amorçage "
      "suppose un apport extérieur à l’économie. Gerschenkron décrit "
      "précisément cette substitution institutionnelle : l’État ou les "
      "banques rassemblent le capital que le marché ne mobilise pas.",
      'cause'),
   ln('ajustement', 'etat', 'inverse la doctrine',
      "Le Consensus de Washington retire à l’État les instruments mêmes que "
      "l’État développeur utilise : protection, crédit dirigé, entreprises "
      "publiques. La séquence historique est donc une bascule doctrinale "
      "autant qu’un programme de stabilisation.", 'oppose'),
   ln('ajustement', 'dependance', 'rend visible la contrainte',
      "La conditionnalité ne crée pas la dépendance : elle la rend "
      "manifeste. Lorsque 70 % de la dette est à taux variable auprès de "
      "banques privées, la décision budgétaire est déjà sous contrainte "
      "extérieure avant toute négociation.", 'renforce'),
   ln('etapes', 'isi', 'oriente le choix des outils',
      "Selon que l’on tient le sous-développement pour un retard ou pour une "
      "structure, on recommande d’accélérer l’accumulation ou de changer la "
      "spécialisation. Le débat théorique commande directement le choix des "
      "instruments.", 'conditionne'),
   ln('etat', 'trappe', 'ne garantit pas le franchissement',
      "Mobiliser le capital suffit à décoller, pas à rejoindre la frontière "
      "technologique. Au stade du revenu intermédiaire, le relais doit venir "
      "de l’innovation, du capital humain et de la technologie : la politique "
      "doit être différenciée selon la distance à la frontière.", 'limite'),
   ln('trappe', 'capabilites', 'ramène à l’éducation',
      "La sortie identifiée de la trappe — capital humain, recherche, "
      "technologie — rejoint ce que l’approche par les capabilités désignait "
      "comme fin en soi : éducation et santé sont simultanément des leviers "
      "de productivité et des libertés réelles.", 'renforce'),
  ],
  bandes=[(1, 'Définir et mesurer'), (2, 'Ce qui bloque'),
          (3, 'Les stratégies'), (4, 'Les débats ouverts')],
  fam='Croissance et développement')
