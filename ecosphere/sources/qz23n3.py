# -*- coding: utf-8 -*-
"""Chapitre 23 — questions nouvelles, sous-parties c23-11 à c23-14."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c23-11
f(id='q23-n46', sp='c23-11', niv='connaitre', type='qcm', b=2590,
  q="Comment se définissent des rendements d’échelle croissants ?",
  opts=["Une augmentation proportionnelle des facteurs produit une "
        "augmentation plus que proportionnelle de la production",
        "Le coût total augmente moins vite que le prix de vente",
        "La production augmente alors que les facteurs diminuent",
        "Le profit augmente avec le nombre de concurrents"],
  ans=0,
  why=["La comparaison du coût et du prix mesure une marge, non un "
       "rendement.",
       "Produire davantage avec moins de facteurs décrit un progrès "
       "technique, non un rendement d’échelle.",
       "Le nombre de concurrents n’intervient pas dans la définition."],
  exp="Les rendements croissants impliquent que le coût moyen diminue lorsque "
      "la production augmente : c’est la définition des économies d’échelle. "
      "Celles-ci peuvent apparaître à l’intérieur d’une firme — économies "
      "internes, liées à sa propre taille — ou à l’extérieur — économies "
      "externes, liées à la taille du secteur ou du territoire. Dans la "
      "nouvelle géographie économique, ce sont les secondes qui sont "
      "déterminantes.",
  diss="Distinction à ne jamais confondre : interne = taille de l’entreprise, "
       "externe = taille du cluster."),

f(id='q23-n47', sp='c23-11', niv='appliquer', type='qcmm', b=2571,
  q="Quels gains l’ouverture procure-t-elle selon Krugman, et par quels "
    "canaux ? (plusieurs réponses)",
  opts=["La concurrence étrangère élimine les firmes les moins productives et "
        "pousse les autres à innover et réduire leurs coûts",
        "Les consommateurs accèdent à davantage de produits, et les "
        "entreprises à davantage de fournisseurs et d’intrants",
        "L’élargissement du marché augmente les volumes et permet "
        "d’exploiter des économies d’échelle",
        "Les écarts de dotations factorielles s’accroissent entre les pays",
        "Les droits de douane procurent des recettes supplémentaires"],
  ans=[0, 1, 2],
  why=["Exacte : c’est l’effet de sélection par la concurrence.",
       "Exacte : c’est le gain de variété, qui concerne aussi les intrants "
       "intermédiaires.",
       "Exacte : c’est l’effet de dimension, apport décisif de Krugman.",
       "Inexacte : les gains de Krugman ne reposent sur aucune différence "
       "entre pays.",
       "Inexacte : les recettes douanières relèvent de la protection, non de "
       "l’ouverture."],
  exp="Ces trois gains existent même entre pays strictement identiques, "
      "puisqu’ils reposent sur la taille du marché et non sur des "
      "différences. L’ouverture ne se contente donc plus d’exploiter un "
      "avantage préexistant : elle peut elle-même créer et renforcer la "
      "compétitivité, ce qui renverse la causalité traditionnelle entre "
      "avantage comparatif et commerce.",
  diss="Phrase de synthèse : chez Ricardo on échange parce qu’on est "
       "différent, chez Krugman on devient compétitif parce qu’on échange."),

f(id='q23-n48', sp='c23-11', niv='comprendre', type='qcm', b=2653,
  q="Pourquoi un bassin de main-d’œuvre spécialisé profite-t-il à la fois aux "
    "entreprises et aux travailleurs ?",
  opts=["Parce qu’il permet de verser des salaires plus faibles",
        "Parce qu’il réduit simultanément le risque de pénurie de compétences "
        "pour les entreprises et le risque de chômage pour les travailleurs",
        "Parce qu’il supprime la concurrence entre employeurs",
        "Parce qu’il garantit des emplois à vie"],
  ans=1,
  why=["La concentration sectorielle ne vise pas la baisse des salaires : "
       "elle peut même les élever par la concurrence entre employeurs.",
       "La concurrence entre employeurs est au contraire renforcée par leur "
       "concentration.",
       "Aucune garantie d’emploi n’est en cause : c’est le risque qui "
       "diminue, non l’incertitude qui disparaît."],
  exp="C’est la deuxième des trois externalités marshalliennes. La "
      "concentration sectorielle crée un marché du travail spécialisé : "
      "l’entreprise trouve plus facilement les compétences dont elle a "
      "besoin, et le travailleur plus facilement un autre employeur s’il "
      "perd son emploi. Des formations spécialisées peuvent en outre "
      "apparaître sur le territoire, renforçant encore le mécanisme.",
  diss="Les trois externalités à citer ensemble : fournisseurs spécialisés, "
       "bassin de main-d’œuvre, circulation des connaissances."),

f(id='q23-n49', sp='c23-11', niv='raisonner', type='vf', b=2664,
  q="Les externalités de connaissance entre entreprises d’un même territoire "
    "supposent que les savoir-faire soient parfaitement brevetables.",
  ans=False,
  exp="C’est précisément l’inverse : les districts industriels génèrent des "
      "externalités technologiques parce que les savoir-faire ne sont pas "
      "parfaitement brevetables ni appropriables. La proximité facilite alors "
      "la circulation d’idées, de méthodes et de tours de main qui profitent "
      "à l’ensemble des entreprises du territoire. Si tout était "
      "parfaitement protégé, il n’y aurait pas de diffusion, donc pas "
      "d’externalité — et l’intérêt de la proximité géographique "
      "disparaîtrait en grande partie.",
  diss="Lien avec le chapitre sur l’innovation : c’est le caractère "
       "partiellement non appropriable de la connaissance qui engendre à la "
       "fois le sous-investissement privé et les gains d’agglomération."),

# ------------------------------------------------------------- c23-12
f(id='q23-n50', sp='c23-12', niv='comprendre', type='qcm', b=2731,
  q="Pourquoi, avec des rendements croissants, un avantage comparatif peut-il "
    "résulter de l’histoire plutôt que de conditions naturelles ?",
  opts=["Parce que les conditions naturelles n’ont jamais d’influence",
        "Parce qu’une implantation initiale suffit parfois à déclencher un "
        "processus cumulatif qui rend ensuite le territoire durablement plus "
        "compétitif",
        "Parce que les coûts de transport diminuent avec le temps",
        "Parce que les États choisissent les spécialisations"],
  ans=1,
  why=["Les conditions naturelles conservent une influence : elles cessent "
       "simplement d’être déterminantes.",
       "La baisse des coûts de transport facilite les échanges mais ne crée "
       "pas l’avantage.",
       "L’État peut amorcer le processus, mais ce n’est pas ce qui explique "
       "le caractère cumulatif."],
  exp="Un effet d’agglomération apparaît lorsque la présence d’entreprises "
      "dans une zone accroît l’intérêt pour d’autres entreprises de s’y "
      "installer. Il produit une causalité cumulative : plus une activité est "
      "concentrée dans un territoire, plus celui-ci devient compétitif et "
      "plus il attire de nouvelles entreprises, renforçant encore la "
      "spécialisation initiale. L’avantage est donc acquis et non hérité.",
  diss="Expression à employer : dépendance au sentier — l’histoire compte "
       "dans la localisation durable des industries."),

f(id='q23-n51', sp='c23-12', niv='appliquer', type='assoc', b=2777,
  q="Associez chaque cluster à l’événement initial qui l’a amorcé, d’après le "
    "cours.",
  ans=[["Une implantation de Texas Instruments dans les années 1980",
        "Bangalore"],
       ["Une décision publique de renforcer la capacité aéronautique "
        "nationale, dans une ville d’abord spécialisée dans le matériel "
        "ferroviaire", "Toulouse"],
       ["Une infrastructure scientifique initiale, dont sont issus des "
        "entrepreneurs comme Hewlett et Packard", "Silicon Valley"]],
  exp="Ces trois exemples illustrent la même logique cumulative mais avec des "
      "déclencheurs différents : une décision privée à Bangalore, une "
      "décision publique à Toulouse, une institution scientifique dans la "
      "Silicon Valley. Dans les trois cas, l’événement initial crée un noyau "
      "autour duquel s’accumulent compétences, fournisseurs et entreprises, "
      "jusqu’à rendre la spécialisation auto-entretenue.",
  diss="Exemple à privilégier selon la thèse défendue : Toulouse pour "
       "justifier l’intervention publique, Bangalore pour montrer la "
       "contingence historique."),

f(id='q23-n52', sp='c23-12', niv='raisonner', type='qcm', b=2812,
  q="Quelle distinction les rendements croissants introduisent-ils entre "
    "avantage potentiel et avantage acquis ?",
  opts=["L’avantage potentiel concerne les services, l’avantage acquis les "
        "biens",
        "Un pays peut disposer de coûts structurellement plus faibles tout en "
        "restant incapable d’entrer sur le marché faute de volumes de "
        "production suffisants",
        "L’avantage potentiel est hérité, l’avantage acquis est naturel",
        "L’avantage acquis disparaît dès l’ouverture du marché"],
  ans=1,
  why=["La distinction ne porte pas sur la nature de l’activité.",
       "C’est l’inverse : l’avantage acquis est construit, l’avantage "
       "potentiel repose sur des coûts structurels.",
       "L’avantage acquis est au contraire renforcé par l’ouverture, grâce "
       "aux volumes."],
  exp="Une industrie déjà installée bénéficie d’un avantage d’antériorité : "
      "grâce aux volumes accumulés et aux économies d’échelle, elle peut "
      "afficher des coûts effectifs inférieurs à ceux d’un nouvel entrant "
      "pourtant potentiellement plus efficient. Le seuil Q0 fonctionne alors "
      "comme une barrière à l’entrée : en dessous, le coût unitaire du "
      "nouvel entrant reste supérieur au prix pratiqué par le producteur "
      "installé.",
  diss="Conséquence majeure : l’ouverture immédiate peut empêcher "
       "l’apparition d’une industrie pourtant potentiellement compétitive."),

f(id='q23-n53', sp='c23-12', niv='appliquer', type='ordre', b=2709,
  q="Remettez dans l’ordre le mécanisme par lequel l’ouverture renforce la "
    "spécialisation chinoise dans l’exemple des boutons.",
  ans=["Avant ouverture, la Chine et l’Europe produisent chacune leurs "
       "propres boutons, avec des coûts moyens décroissants",
       "Le prix d’équilibre chinois est déjà inférieur au prix européen : la "
       "Chine dispose d’un avantage initial",
       "À l’ouverture, la demande européenne s’adresse à la Chine, dont la "
       "production passe de Q1 à Q2",
       "Les économies d’échelle font baisser son coût moyen, donc son prix, "
       "de P1 à P2",
       "L’Europe importe les boutons moins cher qu’elle ne les produisait et "
       "réaffecte ses facteurs vers d’autres productions"],
  exp="Avec des rendements croissants, la spécialisation devient cumulative : "
      "en captant la demande étrangère, le producteur augmente ses volumes, "
      "abaisse encore ses coûts et fournit aux partenaires un bien moins cher "
      "que celui qu’ils produisaient en autarcie. L’analyse de Krugman ne "
      "consiste donc pas seulement à constater que la Chine est "
      "compétitive : elle explique pourquoi cette spécialisation se renforce "
      "d’elle-même.",
  diss="Lecture à deux niveaux : les consommateurs européens gagnent, mais la "
       "possibilité d’un retour en arrière productif disparaît."),

f(id='q23-n54', sp='c23-12', niv='raisonner', type='courte', b=2861,
  q="Comment Krugman réhabilite-t-il l’argument du protectionnisme éducateur "
    "de List, et sous quelle condition ?",
  ans={'modele': "Avec des rendements croissants, une industrie doit dépasser "
       "une quantité minimale de production pour que ses coûts unitaires "
       "deviennent compétitifs. Un pays peut donc disposer d’un avantage "
       "potentiel — une courbe de coût moyen inférieure à celle du "
       "producteur installé — sans parvenir à entrer sur le marché, puisque "
       "au démarrage ses faibles volumes maintiennent son coût au-dessus du "
       "prix pratiqué par le concurrent. L’ouverture immédiate empêche alors "
       "l’apparition d’une industrie pourtant potentiellement compétitive : "
       "c’est l’exemple de la Thaïlande face aux producteurs suisses, ou du "
       "Vietnam face à la Chine. Une protection temporaire permet de réduire "
       "la concurrence étrangère le temps que la production atteigne le seuil "
       "critique, après quoi l’industrie peut devenir compétitive sans "
       "protection. L’argument de List reçoit ainsi une formalisation "
       "économique. Mais il reste conditionné par l’existence d’une demande "
       "domestique suffisamment importante : sans marché intérieur permettant "
       "d’atteindre la taille critique, la protection risque seulement de "
       "maintenir artificiellement une activité non compétitive.",
       'cles': [{'f': ['rendement croissant', 'economie d echelle',
                       'cout unitaire'],
                 'l': "les rendements croissants et la baisse du coût unitaire"},
                {'f': ['seuil', 'q0', 'quantite minimale', 'taille critique'],
                 'l': "un seuil minimal de production à franchir"},
                {'f': ['potentiel', 'plus efficace', 'exclu', 'anteriorite'],
                 'l': "un producteur potentiellement plus efficace reste exclu"},
                {'f': ['protection temporaire', 'temporaire', 'amorcer',
                       'le temps'],
                 'l': "une protection temporaire permet d'amorcer les économies d'échelle"},
                {'f': ['list', 'educateur', 'formalis'],
                 'l': "l'argument de List reçoit une formalisation"},
                {'f': ['marche domestique', 'demande domestique',
                       'marche interieur'],
                 'l': "condition : un marché domestique suffisant"}]},
  exp="Krugman renouvelle l’argument de List : lorsqu’une industrie "
      "potentiellement efficace ne peut atteindre seule l’échelle minimale "
      "nécessaire pour concurrencer un producteur déjà installé, une "
      "protection temporaire peut permettre d’amorcer les économies d’échelle "
      "et de construire un avantage comparatif.",
  diss="Argument le plus solide du chapitre en faveur de la protection : il "
       "est formalisé, conditionnel et temporaire — donc défendable."),

f(id='q23-n55', sp='c23-12', niv='raisonner', type='vf', b=2914,
  q="Les théories contemporaines du commerce international redonnent une "
    "place possible à la politique commerciale dans la formation des "
    "spécialisations.",
  ans=True,
  exp="C’est l’une de leurs conséquences les plus importantes. L’avantage "
      "comparatif n’est plus seulement le résultat d’une dotation initiale : "
      "il peut être construit par l’innovation, la demande, les économies "
      "d’échelle et les effets d’agglomération. Si la spécialisation est en "
      "partie construite, alors l’intervention publique peut en modifier le "
      "cours — ce qui justifie, dans certaines circonstances, des protections "
      "temporaires. Les théories traditionnelles concluaient au contraire que "
      "toute entrave à l’échange réduisait l’efficacité.",
  diss="Articulation de fin de partie : c’est ce renversement théorique qui "
       "ouvre la troisième partie du chapitre, consacrée à la politique "
       "commerciale."),

f(id='q23-n56', sp='c23-12', niv='comprendre', type='qcm', b=2538,
  q="En quoi Krugman renverse-t-il la causalité des théories "
    "traditionnelles ?",
  opts=["La spécialisation précède l’ouverture, qui n’en est que la "
        "conséquence",
        "L’ouverture ne se contente pas de résulter d’une spécialisation "
        "préalable : elle peut elle-même créer et renforcer la compétitivité",
        "Les dotations factorielles déterminent la localisation des activités",
        "Les préférences des consommateurs déterminent les dotations"],
  ans=1,
  why=["C’est précisément la causalité traditionnelle, que Krugman inverse.",
       "La détermination par les dotations est le raisonnement de HOS.",
       "Les préférences ne déterminent pas les dotations : c’est une "
       "confusion."],
  exp="Dans les théories traditionnelles, la dotation détermine la "
      "spécialisation, donc la localisation. Avec des rendements croissants, "
      "la relation s’inverse : une implantation initiale, parfois "
      "accidentelle, permet d’atteindre un volume qui abaisse les coûts "
      "unitaires, ce qui attire d’autres activités et consolide l’avantage. "
      "La localisation engendre alors la dotation.",
  diss="Formule à retenir : un pays ne se contente pas d’exporter parce qu’il "
       "est compétitif, il peut devenir compétitif parce qu’il exporte."),

# ------------------------------------------------------------- c23-13
f(id='q23-n57', sp='c23-13', niv='connaitre', type='qcm', b=2971,
  q="Comment le cours définit-il le protectionnisme en tant que situation "
    "concrète ?",
  opts=["Une doctrine affirmant que la fermeture enrichit un pays",
        "L’ensemble des mesures destinées à limiter ou modifier les échanges "
        "internationaux",
        "L’absence totale de commerce extérieur",
        "Un excédent commercial durable"],
  ans=1,
  why=["La doctrine correspondante est le mercantilisme, non le "
       "protectionnisme.",
       "L’absence totale d’échanges serait l’autarcie, cas extrême et "
       "rarement observé.",
       "Un excédent commercial est un résultat comptable, non une politique."],
  exp="Le libre-échange et le protectionnisme sont d’abord des situations "
      "concrètes, donc des faits : dans le premier cas les échanges circulent "
      "sans obstacles importants, dans le second ils sont volontairement "
      "entravés. Le protectionnisme contemporain ne se limite d’ailleurs plus "
      "à la défense de l’emploi industriel : les restrictions peuvent être "
      "justifiées par des objectifs de souveraineté, de sécurité ou de "
      "résilience économique.",
  diss="Rigueur de vocabulaire : réserver « libre-échangisme » et "
       "« mercantilisme » aux doctrines."),

f(id='q23-n58', sp='c23-13', niv='comprendre', type='qcm', b=3006,
  q="Quelle image le cours emploie-t-il pour résumer la doctrine "
    "libre-échangiste ?",
  opts=["Le partage d’un gâteau de taille fixe",
        "L’accroissement de la taille du gâteau mondial grâce à une "
        "utilisation plus efficace des ressources",
        "La redistribution du gâteau vers les pays pauvres",
        "La protection du gâteau national contre les appétits étrangers"],
  ans=1,
  why=["Le partage d’un gâteau fixe correspond à la conception mercantiliste, "
       "proche d’un jeu à somme nulle.",
       "La redistribution internationale n’est pas l’objet de cette "
       "doctrine.",
       "La protection du marché national relève du protectionnisme."],
  exp="La doctrine libre-échangiste considère que la spécialisation et "
      "l’échange permettent une utilisation plus efficace des ressources et "
      "peuvent ainsi enrichir simultanément plusieurs partenaires : les "
      "échanges sont un jeu à somme positive. Cette vision s’oppose à la "
      "conception mercantiliste, dans laquelle la puissance de l’un se "
      "construit davantage au détriment de l’autre.",
  diss="Attention : affirmer que le gâteau grossit ne dit rien de la manière "
       "dont il est partagé — c’est tout l’enjeu des parties suivantes."),

f(id='q23-n59', sp='c23-13', niv='raisonner', type='qcm', b=3056,
  q="Pourquoi le rattrapage technologique des grandes économies émergentes "
    "rend-il la concurrence plus conflictuelle ?",
  opts=["Parce qu’il réduit le volume total des échanges mondiaux",
        "Parce qu’il transforme un commerce initialement complémentaire en "
        "concurrence intra-branche, les nouveaux producteurs s’attaquant aux "
        "marchés autrefois dominés par les économies avancées",
        "Parce qu’il supprime les avantages comparatifs",
        "Parce qu’il rend les droits de douane inefficaces"],
  ans=1,
  why=["Le volume des échanges n’est pas réduit par le rattrapage.",
       "Les avantages comparatifs ne disparaissent pas : ils se déplacent.",
       "L’efficacité des droits de douane est une autre question."],
  exp="L’intégration de nouveaux concurrents peut être relativement bien "
      "acceptée tant que leurs spécialisations restent différentes : le "
      "commerce est alors complémentaire. Mais lorsque les pays émergents "
      "montent en gamme et investissent les activités à forte intensité "
      "technologique ou en capital humain, ils entrent en concurrence directe "
      "avec les économies avancées, ce qui renforce les tensions et "
      "réactive une lecture mercantiliste des échanges.",
  diss="Mécanisme identique à celui du deuxième choc chinois étudié au "
       "chapitre précédent : la complémentarité disparaît."),

f(id='q23-n60', sp='c23-13', niv='comprendre', type='qcmm', b=3155,
  q="Par quels mécanismes, du côté de l’offre, l’ouverture peut-elle favoriser "
    "la croissance ? (plusieurs réponses)",
  opts=["La réallocation des facteurs vers les secteurs où leur productivité "
        "relative est la plus élevée",
        "L’accès à des intrants importés moins chers",
        "La possibilité d’une division du travail plus poussée grâce à "
        "l’élargissement du marché",
        "Les gains d’apprentissage et la diffusion des technologies les plus "
        "efficaces",
        "La sélection par la concurrence, qui élimine les producteurs les "
        "moins productifs",
        "La hausse du prix des biens importés"],
  ans=[0, 1, 2, 3, 4],
  why=["Exacte : c’est le gain d’efficience productive hérité de Ricardo.",
       "Exacte : les entreprises bénéficient d’intrants et de consommations "
       "intermédiaires moins coûteux.",
       "Exacte : les producteurs ne sont plus limités à leur demande "
       "nationale.",
       "Exacte : ce sont les gains dynamiques liés à la diffusion des "
       "méthodes productives.",
       "Exacte : la concurrence exerce un effet disciplinaire sur les "
       "entreprises.",
       "Inexacte : l’ouverture fait au contraire baisser le prix des biens "
       "importés."],
  exp="Du côté de la demande s’ajoutent deux canaux : l’effet de pouvoir "
      "d’achat, important au niveau agrégé même s’il est dispersé entre de "
      "très nombreux consommateurs, et le gain de variété. Enfin la demande "
      "étrangère peut soutenir directement production et emploi par les "
      "débouchés extérieurs.",
  diss="Organisation de copie efficace : séparer les mécanismes d’offre et de "
       "demande, puis les gains statiques et dynamiques."),

f(id='q23-n61', sp='c23-13', niv='raisonner', type='qcm', b=3100,
  q="Pourquoi la prospérité ne peut-elle pas être réduite à l’augmentation de "
    "la production ?",
  opts=["Parce que le PIB est impossible à mesurer",
        "Parce qu’il faut aussi considérer la répartition des gains entre les "
        "individus et les effets sur la qualité de vie",
        "Parce que la production diminue toujours avec l’ouverture",
        "Parce que la consommation ne dépend pas du revenu"],
  ans=1,
  why=["Le PIB est mesuré, même imparfaitement : ce n’est pas l’argument.",
       "La production augmente au contraire avec l’ouverture, selon le "
       "cours.",
       "La consommation dépend bien du revenu, comme le rappelle la loi "
       "d’Engel."],
  exp="Une hausse de la production totale ne suffit pas pour parler de "
      "prospérité générale : encore faut-il savoir comment les gains sont "
      "répartis. L’ouverture peut en effet polariser certaines rémunérations "
      "dans les économies avancées. S’y ajoute une seconde limite : la "
      "qualité de vie ne dépend pas seulement du revenu. L’évaluation du "
      "commerce devient donc normative dès qu’on s’interroge sur la "
      "prospérité.",
  diss="Transition commode vers la partie sur les perdants de l’ouverture, "
       "qu’il s’agisse de pays ou de catégories sociales."),

f(id='q23-n62', sp='c23-13', niv='comprendre', type='qcm', b=3215,
  q="Pourquoi la richesse en ressources naturelles peut-elle devenir une "
    "« malédiction » ?",
  opts=["Parce que les ressources naturelles s’épuisent nécessairement",
        "Parce qu’elle peut entretenir une économie de rente, concentrer les "
        "revenus et empêcher la diversification productive nécessaire à une "
        "croissance durable",
        "Parce que leur prix est toujours en baisse",
        "Parce qu’elles ne peuvent pas être exportées"],
  ans=1,
  why=["L’épuisement est un problème réel mais distinct de ce mécanisme.",
       "Le prix des matières premières est au contraire très volatil, parfois "
       "élevé.",
       "Ces ressources sont précisément exportées en grande quantité."],
  exp="Certains pays ne parviennent pas à transformer leur richesse en "
      "ressources en développement généralisé : le cours cite le cas de pays "
      "fortement dépendants des hydrocarbures, et montre que les pays "
      "exportateurs de carburants d’Afrique subsaharienne enregistrent, sur "
      "la période présentée, une évolution du PIB par habitant moins "
      "favorable que les pays moins dépendants. Une forte spécialisation "
      "extractive ne se traduit donc pas automatiquement par un développement "
      "durable et largement partagé.",
  diss="À articuler avec Prebisch et la reprimarisation : trois façons de "
       "montrer que la spécialisation primaire peut être défavorable."),

f(id='q23-n63', sp='c23-13', niv='raisonner', type='courte', b=3276,
  q="Pourquoi les gains agrégés de l’ouverture peuvent-ils exiger des "
    "politiques complémentaires ?",
  ans={'modele': "Parce que la spécialisation impose des coûts d’ajustement. "
       "Lorsqu’un secteur recule, ses travailleurs ne se déplacent pas "
       "automatiquement vers les secteurs en expansion : il apparaît un "
       "chômage d’inadéquation, lorsque les compétences ou la localisation "
       "des travailleurs ne correspondent pas aux emplois disponibles. Dans "
       "les économies avancées, les travailleurs peu qualifiés des secteurs "
       "exposés sont les plus touchés, leurs compétences correspondant moins "
       "aux nouvelles spécialisations. Les gains agrégés ne suffisent donc "
       "pas à garantir l’acceptabilité de l’ouverture : il faut des "
       "politiques de formation, de redistribution et parfois un "
       "accompagnement temporaire des secteurs en déclin — qu’il s’agisse de "
       "ralentir la disparition d’activités vieillissantes ou de protéger "
       "temporairement une industrie naissante. Autrement dit, le "
       "libre-échange produit un surplus, mais la question de savoir qui le "
       "reçoit relève de la politique économique.",
       'cles': [{'f': ['cout d ajustement', 'ajustement', 'reconversion'],
                 'l': "la spécialisation impose des coûts d'ajustement"},
                {'f': ['inadequation', 'competence', 'localisation',
                       'mismatch'],
                 'l': "un chômage d'inadéquation de compétences ou de localisation"},
                {'f': ['peu qualifie', 'expose', 'secteur en declin'],
                 'l': "les travailleurs peu qualifiés des secteurs exposés"},
                {'f': ['formation', 'redistribution', 'accompagnement'],
                 'l': "des politiques de formation et de redistribution"},
                {'f': ['temporaire', 'protection', 'educateur', 'vieillissant'],
                 'l': "parfois un accompagnement temporaire des secteurs concernés"},
                {'f': ['acceptabilite', 'politique', 'repartition'],
                 'l': "l'enjeu de l'acceptabilité et de la répartition"}]},
  exp="Les gains agrégés de l’ouverture ne suffisent pas à garantir son "
      "acceptabilité : les coûts de reconversion rendent nécessaires des "
      "politiques de formation, de redistribution et parfois un "
      "accompagnement temporaire des secteurs en déclin.",
  diss="Position de synthèse très solide : le débat n’oppose pas ouverture et "
       "fermeture, mais ouverture seule et ouverture accompagnée."),

f(id='q23-n64', sp='c23-13', niv='raisonner', type='vf', b=3292,
  q="Selon le cours, le principe de spécialisation suffit à garantir la "
    "prospérité d’un pays.",
  ans=False,
  exp="Toutes les spécialisations ne se valent pas : certaines peuvent "
      "enfermer l’économie dans des activités peu dynamiques, aux faibles "
      "gains de productivité et aux prix relatifs défavorables. Les effets de "
      "l’ouverture dépendent donc de la nature des activités dans lesquelles "
      "un pays se spécialise, de leurs gains de productivité, et des "
      "institutions capables de répartir les bénéfices de l’échange. C’est "
      "exactement ce que montrent Prebisch, la malédiction des ressources "
      "naturelles et l’analyse de l’insertion dominée.",
  diss="Conclusion nuancée recommandée : le gain à l’échange est réel, mais "
       "il n’est ni automatique ni équitablement réparti."),

f(id='q23-n65', sp='c23-13', niv='comprendre', type='qcm', b=3236,
  q="Qu’appelle-t-on une insertion internationale « dominée » ?",
  opts=["Une situation dans laquelle un pays refuse d’exporter",
        "Une insertion qui enferme une économie dans des productions à faible "
        "valeur ajoutée dont les prix progressent moins vite que ceux des "
        "biens manufacturés importés",
        "Une insertion limitée aux pays voisins",
        "Une insertion dans laquelle un pays importe plus qu’il n’exporte"],
  ans=1,
  why=["Le refus d’exporter décrirait une autarcie choisie.",
       "La dimension géographique n’est pas le critère retenu.",
       "Un déficit commercial ne constitue pas en soi une insertion dominée."],
  exp="Le pays participe bien au commerce mondial, mais dans une position "
      "défavorable : ses exportations se concentrent sur des productions à "
      "faible valeur ajoutée, et la dégradation relative de leurs prix limite "
      "les gains qu’il peut tirer de l’ouverture. Ce n’est donc pas "
      "l’absence d’échange qui pose problème, mais la nature de la "
      "spécialisation — ce qui rejoint directement la thèse de Prebisch.",
  diss="Distinction utile : être exclu du commerce mondial et y être inséré "
       "en position dominée sont deux situations différentes."),

# ------------------------------------------------------------- c23-14
f(id='q23-n66', sp='c23-14', niv='connaitre', type='assoc', b=3409,
  q="Associez chaque protection tarifaire exceptionnelle à la situation "
    "qu’elle vise.",
  ans=[["Une entreprise étrangère vend à l’étranger à un prix inférieur à "
        "celui pratiqué sur son marché domestique", "Droit antidumping"],
       ["Un producteur étranger bénéficie d’une subvention publique qui lui "
        "procure un avantage artificiel", "Droit compensateur"],
       ["Un secteur domestique est gravement menacé par une hausse rapide des "
        "importations, sans pratique déloyale", "Clause de sauvegarde"]],
  exp="Les deux premiers instruments visent à neutraliser une distorsion : un "
      "prix jugé déloyal dans le premier cas, une subvention étrangère dans "
      "le second. La clause de sauvegarde a une logique différente : elle ne "
      "sanctionne aucune déloyauté mais amortit un choc brutal "
      "d’importations afin d’offrir au secteur domestique un délai "
      "d’ajustement. Ces instruments montrent que le système commercial "
      "multilatéral n’interdit pas toute protection : il l’encadre "
      "juridiquement.",
  diss="Précision qui fait la différence : la sauvegarde est une protection "
       "légitime sans faute du partenaire."),

f(id='q23-n67', sp='c23-14', niv='comprendre', type='qcm', b=3329,
  q="Que désigne un tarif consolidé ?",
  opts=["Le droit de douane effectivement payé par les importateurs",
        "Le niveau maximal qu’un pays s’engage à ne pas dépasser dans les "
        "conditions ordinaires",
        "Le droit réduit accordé à certains partenaires",
        "La moyenne des droits appliqués par un pays"],
  ans=1,
  why=["Le droit effectivement payé est le tarif appliqué, souvent inférieur "
       "au tarif consolidé.",
       "Le droit réduit accordé à certains partenaires est un tarif "
       "préférentiel.",
       "La moyenne des droits est un indicateur statistique, non un "
       "engagement."],
  exp="Le tarif consolidé ne correspond donc pas nécessairement au droit "
      "effectivement payé : il constitue un plafond négocié au niveau "
      "multilatéral que le pays s’engage à respecter. L’écart entre tarif "
      "consolidé et tarif appliqué mesure la marge de manœuvre dont dispose "
      "un État pour relever ses droits sans violer ses engagements — ce qui "
      "est une information stratégique importante.",
  diss="Troisième notion à maîtriser avec elles : les pics tarifaires, qui "
       "montrent qu’un tarif moyen faible n’implique pas une ouverture "
       "uniforme."),

f(id='q23-n68', sp='c23-14', niv='comprendre', type='qcmm', b=3469,
  q="Quelles formes le protectionnisme non tarifaire peut-il prendre ? "
    "(plusieurs réponses)",
  opts=["Des quotas et des contingentements",
        "Des restrictions volontaires aux exportations négociées avec le pays "
        "exportateur",
        "Des normes sanitaires, techniques et environnementales",
        "Des règles de contenu local",
        "Des subventions aux producteurs domestiques",
        "Des droits de douane différenciés selon les produits"],
  ans=[0, 1, 2, 3, 4],
  why=["Exacte : le quota fixe une quantité maximale d’importations.",
       "Exacte : le cours cite les restrictions sur certaines importations "
       "automobiles japonaises.",
       "Exacte : une norme peut poursuivre un objectif légitime tout en "
       "constituant une barrière.",
       "Exacte : elles exigent qu’une part du produit soit réalisée sur le "
       "territoire.",
       "Exacte : elles réduisent artificiellement les coûts d’un producteur "
       "national.",
       "Inexacte : les droits de douane sont par définition une protection "
       "tarifaire."],
  exp="Avec l’hypermondialisation, les restrictions quantitatives sont "
      "devenues moins centrales et les obstacles réglementaires ont pris "
      "davantage d’importance. Les subventions industrielles brouillent "
      "particulièrement la frontière entre politique productive et "
      "protectionnisme : en abaissant artificiellement les coûts d’un "
      "producteur national, elles peuvent lui procurer un avantage commercial "
      "face à ses concurrents étrangers.",
  diss="Conséquence méthodologique : mesurer la protection par le seul tarif "
       "moyen conduit à sous-estimer gravement son niveau réel."),

f(id='q23-n69', sp='c23-14', niv='raisonner', type='qcm', b=3484,
  q="Pourquoi les spécialisations reposant sur de faibles coûts sont-elles "
    "particulièrement vulnérables au protectionnisme ?",
  opts=["Parce qu’elles concernent surtout des services",
        "Parce que la demande qui leur est adressée est très élastique au "
        "prix : même une hausse modérée liée au droit de douane contracte "
        "fortement les quantités demandées",
        "Parce qu’elles ne bénéficient d’aucune protection juridique",
        "Parce qu’elles sont concentrées dans les pays avancés"],
  ans=1,
  why=["Ces spécialisations concernent largement des biens manufacturés.",
       "La protection juridique des contrats n’est pas en cause.",
       "Ces spécialisations caractérisent plutôt des économies en "
       "développement ou émergentes."],
  exp="Lorsque la compétitivité repose sur le prix, l’acheteur peut aisément "
      "se tourner vers un autre fournisseur dès que ce prix augmente : la "
      "demande est donc très élastique. Le protectionnisme pénalise ainsi "
      "d’abord les exportateurs dont les spécialisations reposent fortement "
      "sur la compétitivité-prix. Le pays qui met en place le droit de douane "
      "supporte cependant lui aussi des coûts, sous la forme des deux pertes "
      "sèches.",
  diss="À relier à la compétitivité hors-prix du chapitre précédent : une "
       "position de gamme élevée protège mieux des chocs tarifaires."),

]
