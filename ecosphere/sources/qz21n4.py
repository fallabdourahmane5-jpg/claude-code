# -*- coding: utf-8 -*-
"""Chapitre 21 — questions nouvelles, sous-parties c21-14 à c21-18."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c21-14
f(id='q21-n60', sp='c21-14', niv='appliquer', type='qcm', b=4889,
  q="Pourquoi le protectionnisme revient-il en force à partir de la fin des "
    "années 1870 ?",
  opts=["Parce que le libre-échange n’avait jamais été appliqué",
        "Parce que le ralentissement économique de la fin du XIXᵉ siècle "
        "ravive les revendications protectionnistes : crise → recherche d’un "
        "responsable → concurrence étrangère accusée → protection",
        "Parce que les coûts de transport augmentent",
        "Parce que l’OMC impose de nouvelles règles"],
  ans=1,
  why=["Le libre-échange avait bien progressé, notamment après le traité "
       "Cobden-Chevalier de 1860.",
       "Les coûts de transport continuent de baisser sur la période.",
       "L’OMC n’existe qu’à partir de 1995."],
  exp="La fin du XIXᵉ siècle montre la fragilité politique du libre-échange : "
      "les épisodes de crise renforcent la demande de protection des "
      "producteurs nationaux. Le tarif Méline de 1892 en est le symbole "
      "français. Après la crise de 1929, ce mouvement se transforme en "
      "véritable démondialisation, dont le tarif Hawley-Smoot de 1930 est "
      "l’illustration américaine.",
  diss="Régularité historique très utile : les crises économiques fragilisent "
       "systématiquement l’ouverture commerciale."),

f(id='q21-n61', sp='c21-14', niv='raisonner', type='qcm', b=4963,
  q="Pourquoi la DIT traditionnelle ne peut-elle être expliquée par les seuls "
    "avantages comparatifs ?",
  opts=["Parce que les avantages comparatifs n’existent pas",
        "Parce qu’elle est aussi le produit de rapports de domination : "
        "l’Inde coloniale passe d’exportatrice de textiles à fournisseur de "
        "coton et importatrice de produits manufacturés, et les guerres de "
        "l’opium imposent à la Chine une ouverture forcée",
        "Parce que les pays périphériques choisissaient librement leur "
        "spécialisation",
        "Parce que les coûts de transport la rendaient impossible"],
  ans=1,
  why=["Les avantages comparatifs existent : ils ne suffisent simplement pas "
       "à expliquer cette organisation.",
       "C’est précisément ce que la colonisation contredit.",
       "La baisse des coûts de transport la rend au contraire possible."],
  exp="La reprimarisation imposée de l’économie indienne et l’ouverture "
      "forcée du marché chinois montrent que la spécialisation internationale "
      "a été orientée en fonction des besoins du centre. Acemoglu et Robinson "
      "complètent l’analyse : les institutions coloniales sont souvent "
      "extractives, organisées pour capter les ressources au bénéfice de la "
      "métropole, ce qui limite l’émergence d’un développement autonome. La "
      "domination est donc à la fois commerciale, productive et financière.",
  diss="Conséquence méthodologique : une spécialisation observée n’est pas "
       "nécessairement une spécialisation choisie."),

f(id='q21-n62', sp='c21-14', niv='raisonner', type='qcm', b=5027,
  q="Que montre le cours en affirmant que « mondialisation et intervention de "
    "l’État ne sont pas incompatibles » ?",
  opts=["Que l’État disparaît nécessairement avec l’ouverture",
        "Que la première mondialisation s’accompagne au contraire d’une "
        "intervention croissante de l’État et de l’émergence des premières "
        "formes de protection sociale",
        "Que l’ouverture impose la privatisation des services publics",
        "Que l’État ne joue aucun rôle dans le commerce extérieur"],
  ans=1,
  why=["C’est exactement la thèse que ce passage réfute.",
       "Aucune logique de privatisation n’est associée à cette période.",
       "Les États jouent au contraire un rôle fondamental dans la "
       "configuration internationale de Michalet."],
  exp="Le contraste avec l’hypermondialisation est instructif : alors que la "
      "première mondialisation accompagne l’essor de l’État social, "
      "l’hypermondialisation tend davantage à présenter la protection sociale "
      "comme un coût susceptible d’affaiblir la compétitivité. L’articulation "
      "entre ouverture et intervention publique n’est donc pas donnée par la "
      "nature des choses : elle dépend des périodes et des choix politiques.",
  diss="Argument décisif contre l’idée d’une incompatibilité mécanique entre "
       "mondialisation et État social."),

f(id='q21-n63', sp='c21-14', niv='appliquer', type='qcmm', b=5151,
  q="Quelles formes prend le protectionnisme de l’entre-deux-guerres ? "
    "(plusieurs réponses)",
  opts=["Une forte hausse des droits de douane, avec le tarif Hawley-Smoot "
        "de 1930 aux États-Unis",
        "Les accords d’Ottawa de 1932, organisant la préférence impériale "
        "britannique au bénéfice du Commonwealth",
        "Des contingentements et des quotas limitant directement les volumes "
        "importés",
        "Des dévaluations compétitives destinées à soutenir les exportations",
        "Des subventions massives à la recherche et à l’innovation"],
  ans=[0, 1, 2, 3],
  why=["Exacte : les droits atteignent jusqu’à environ 300 % sur certains "
       "produits.",
       "Exacte : la France fait de même, l’Algérie devenant un espace "
       "préférentiel en 1934.",
       "Exacte : c’est une forme de protectionnisme non tarifaire "
       "particulièrement restrictive.",
       "Exacte : la guerre monétaire accompagne la guerre commerciale, mais "
       "la généralisation des dévaluations annule les gains relatifs.",
       "Les politiques d’innovation ne sont pas un instrument "
       "protectionniste de cette période."],
  exp="Le résultat est collectivement désastreux : entre 1929 et 1933, les "
      "échanges internationaux sont divisés par environ trois. "
      "L’enchaînement est explicite : protectionnisme ↑ → importations ↓ → "
      "exportations des partenaires ↓ → production ↓ → chômage ↑ → nouvelle "
      "protection ↑. Les migrations ralentissent également, avec la mise en "
      "place de quotas.",
  diss="Il s’agit d’une démondialisation sur tous les fronts : commerciale, "
       "migratoire, financière et monétaire."),

# ------------------------------------------------------------- c21-15
f(id='q21-n64', sp='c21-15', niv='comprendre', type='qcmm', b=5356,
  q="Quelles raisons expliquent la remondialisation progressive de 1945 à "
    "1980 ? (plusieurs réponses)",
  opts=["La baisse des coûts de transport, avec la conteneurisation, et des "
        "coûts de communication",
        "Le multilatéralisme commercial organisé par le GATT, qui réduit les "
        "droits de douane de manière coordonnée",
        "Le système de Bretton Woods, qui réduit l’incertitude liée aux "
        "fluctuations de change",
        "La construction européenne, qui renforce les échanges intra-zone",
        "La disparition des barrières politiques entre blocs"],
  ans=[0, 1, 2, 3],
  why=["Exacte : la conteneurisation est l’une des grandes innovations "
       "logistiques de l’après-guerre.",
       "Exacte : les États-Unis organisent ce cadre après 1945.",
       "Exacte : la stabilité des changes favorise le commerce.",
       "Exacte : la libéralisation se développe à la fois au niveau mondial "
       "et régional.",
       "Au contraire : la guerre froide limite géographiquement cette "
       "remondialisation, et c’est l’effondrement du bloc soviétique qui "
       "ouvrira la voie à l’hypermondialisation."],
  exp="La remondialisation reste longtemps incomplète : il faut attendre les "
      "années 1980 pour retrouver les niveaux d’ouverture commerciale de "
      "1913. Le cours ajoute le soft power économique américain, le plan "
      "Marshall consolidant le bloc occidental tout en créant des débouchés "
      "pour les entreprises américaines.",
  diss="Différence majeure avec la première mondialisation : celle-ci reposait "
       "surtout sur la technique, celle-là repose aussi sur une forte volonté "
       "institutionnelle."),

f(id='q21-n65', sp='c21-15', niv='appliquer', type='qcm', b=5421,
  q="Pourquoi le cours présente-t-il le Japon des années 1980 comme « la "
    "Chine de l’époque » ?",
  opts=["Parce que le Japon avait le même niveau de développement que la "
        "Chine actuelle",
        "Parce que sa montée en puissance industrielle, fondée sur une "
        "stratégie volontariste et une montée en gamme rapide, nourrit des "
        "accusations de concurrence déloyale et des tensions commerciales avec "
        "les États-Unis",
        "Parce que le Japon exportait surtout des matières premières",
        "Parce que le Japon était alors le premier pays exportateur mondial de "
        "textile"],
  ans=1,
  why=["La comparaison porte sur la position dans les tensions commerciales, "
       "pas sur le niveau de développement.",
       "Le Japon exporte des produits manufacturés à forte valeur ajoutée.",
       "Le textile n’est pas la spécialisation japonaise des années 1980."],
  exp="Le Japon réalise après 1945 un rattrapage exceptionnel, fondé sur une "
      "stratégie industrielle volontariste conduite notamment par le MITI. "
      "Cette montée en puissance inquiète les États-Unis, exactement comme la "
      "Chine aujourd’hui. Le cours en tire l’exemple du tariff jumping : "
      "contourner un droit de douane en produisant directement sur le marché "
      "protégé — ce que le protectionnisme produit souvent, un déplacement de "
      "la localisation des firmes plutôt qu’une réduction des échanges.",
  diss="Parallèle historique très efficace : il relativise le caractère "
       "inédit de la rivalité sino-américaine."),

f(id='q21-n66', sp='c21-15', niv='comprendre', type='qcmm', b=5452,
  q="Quels traits caractérisent l’hypermondialisation, selon le cours ? "
    "(plusieurs réponses)",
  opts=["Le deuxième dégroupage de Baldwin : la fragmentation internationale "
        "de la production transforme le commerce de biens finis en commerce "
        "de tâches",
        "La dématérialisation : les technologies numériques rendent "
        "échangeables des services autrefois non délocalisables",
        "La démocratisation : davantage de pays participent réellement aux "
        "échanges, la fragmentation permettant de se spécialiser dans une "
        "seule tâche",
        "Des flux devenus multidirectionnels et non plus seulement dominés "
        "par le Nord",
        "Une hausse continue des droits de douane"],
  ans=[0, 1, 2, 3],
  why=["Exacte : c’est le trait fondamental, qui distingue cette phase de la "
       "première mondialisation.",
       "Exacte : une partie de la mondialisation devient immatérielle.",
       "Exacte : un pays n’a plus besoin de maîtriser tout un processus "
       "industriel pour s’insérer.",
       "Exacte : la géographie des échanges se recompose.",
       "C’est l’inverse : l’hypermondialisation prolonge la libéralisation, "
       "les droits de douane moyens atteignant des niveaux historiquement très "
       "faibles."],
  exp="La Chine devient l’acteur majeur de cette phase : elle utilise d’abord "
      "les chaînes de valeur mondiales comme pays atelier, l’adhésion à l’OMC "
      "en 2001 accélérant son insertion, avant de monter progressivement en "
      "gamme. Le centre de gravité du commerce mondial se déplace de "
      "l’Atlantique vers le Pacifique.",
  diss="L’hypermondialisation commence avec la fin de la guerre froide : "
       "c’est la première mondialisation véritablement planétaire."),

f(id='q21-n67', sp='c21-15', niv='raisonner', type='qcm', b=5556,
  q="En quoi la montée en gamme chinoise change-t-elle la nature de la "
    "concurrence avec les économies avancées ?",
  opts=["Elle réduit la concurrence, la Chine se retirant des secteurs à "
        "faible valeur ajoutée",
        "Elle transforme une relation de complémentarité en concurrence "
        "directe : les pays avancés, auparavant peu menacés sur leurs secteurs "
        "à forte valeur ajoutée, le deviennent",
        "Elle n’a aucun effet sur les économies avancées",
        "Elle concerne uniquement le secteur agricole"],
  ans=1,
  why=["La Chine ne se retire pas : elle ajoute de nouveaux secteurs à sa "
       "spécialisation.",
       "L’effet est au contraire majeur : c’est l’enjeu du deuxième choc "
       "chinois.",
       "La montée en gamme concerne l’industrie et les technologies."],
  exp="Tant que la Chine se spécialisait dans l’assemblage et les activités "
      "intensives en main-d’œuvre, la relation était largement "
      "complémentaire : les pays avancés conservaient les activités à forte "
      "valeur ajoutée. En montant en gamme, la Chine se rapproche de leurs "
      "spécialisations et conteste leur position à la frontière "
      "technologique, c’est-à-dire l’ensemble des technologies et méthodes de "
      "production les plus avancées disponibles.",
  diss="C’est le passage d’une croissance extensive, fondée sur "
       "l’accumulation des facteurs, à une croissance intensive, fondée sur "
       "l’innovation."),

f(id='q21-n68', sp='c21-15', niv='connaitre', type='qcm', b=5376,
  q="En quoi le système de Bretton Woods favorise-t-il le commerce "
    "international après 1945 ?",
  opts=["En supprimant les droits de douane entre les pays membres",
        "En réduisant l’incertitude liée aux fluctuations des taux de change",
        "En créant une monnaie mondiale unique",
        "En interdisant les mouvements de capitaux"],
  ans=1,
  why=["La baisse des droits de douane relève du GATT, non de Bretton "
       "Woods.",
       "Aucune monnaie unique n’est créée : le dollar joue un rôle central "
       "mais les monnaies nationales subsistent.",
       "Les mouvements de capitaux sont encadrés, non interdits."],
  exp="La stabilité des changes réduit le risque pris par un exportateur ou "
      "un importateur : il sait à quel taux sa recette ou sa dépense sera "
      "convertie. Le cadre d’après-guerre combine donc deux piliers "
      "institutionnels : le GATT pour la libéralisation commerciale "
      "coordonnée, et Bretton Woods pour la stabilité monétaire.",
  diss="À opposer aux dévaluations compétitives de l’entre-deux-guerres : "
       "l’après-guerre est conçu pour empêcher leur retour."),

# ------------------------------------------------------------- c21-16
f(id='q21-n69', sp='c21-16', niv='connaitre', type='qcm', b=5580,
  q="Quand le GATT devient-il l’OMC, et que change cette création ?",
  opts=["En 1947, avec la création du système de Bretton Woods",
        "En 1995 : l’OMC généralise le cadre multilatéral du commerce "
        "international et étend les règles commerciales à presque toute "
        "l’économie mondiale, avec aujourd’hui environ 166 membres",
        "En 2001, avec l’adhésion de la Chine",
        "En 2008, après la crise financière"],
  ans=1,
  why=["1947 est la date du GATT lui-même.",
       "2001 est l’année de l’adhésion chinoise et du lancement du cycle de "
       "Doha.",
       "La crise de 2008 ne crée aucune institution commerciale."],
  exp="L’OMC marque l’aboutissement du multilatéralisme commercial. Mais "
      "celui-ci entre rapidement en crise : le cycle de Doha, lancé en 2001, "
      "s’essouffle, ce qui explique en partie le retour des accords régionaux "
      "et du minilatéralisme — négocier entre groupes restreints de pays "
      "quand il devient difficile de s’accorder à plus de 160.",
  diss="Trajectoire à retenir : multilatéralisme → crise du multilatéralisme "
       "→ régionalisation et minilatéralisme."),

f(id='q21-n70', sp='c21-16', niv='comprendre', type='qcm', b=5614,
  q="Pourquoi les pays échangent-ils davantage avec leurs voisins ?",
  opts=["Parce que les échanges lointains sont interdits",
        "Pour deux raisons combinées : la proximité géographique, qui réduit "
        "les coûts et les délais, et le volontarisme politique, qui organise "
        "des espaces commerciaux intégrés",
        "Parce que les voisins produisent toujours des biens complémentaires",
        "Parce que les monnaies voisines sont toujours liées"],
  ans=1,
  why=["Aucune interdiction : les échanges lointains sont massifs.",
       "La complémentarité n’est pas garantie : les échanges intra-zone sont "
       "souvent intrabranche.",
       "Les régimes monétaires varient fortement d’une région à l’autre."],
  exp="La régionalisation désigne l’augmentation des échanges entre pays "
      "appartenant à une même zone : environ deux tiers des échanges "
      "européens ont lieu avec d’autres pays européens. Elle devient aussi "
      "une réponse politique à l’échec du multilatéralisme. Le modèle du vol "
      "d’oies sauvages d’Akamatsu montre par ailleurs comment la montée en "
      "gamme d’une économie peut diffuser le développement industriel à toute "
      "une région.",
  diss="Nuance importante : la régionalisation n’est pas un recul de la "
       "mondialisation, c’est une forme particulière d’intégration."),

f(id='q21-n71', sp='c21-16', niv='comprendre', type='assoc', b=5670,
  q="Associez chaque type de commerce à sa logique.",
  ans=[["Échanger des biens appartenant à des branches différentes, selon la complémentarité des spécialisations", "Le commerce interbranche : un échange de différences"],
       ["Échanger des biens d’une même branche, mais différenciés, pour satisfaire une demande de diversité", "Le commerce intrabranche : un échange de similarité"],
       ["Des automobiles allemandes échangées contre des automobiles françaises", "Le commerce intrabranche : un échange de similarité"],
       ["Chaque pays se spécialisant dans une étape différente de la production d’un même bien", "Les chaînes de valeur, qui réintroduisent une logique interbranche au sein d’un même produit"]],
  exp="La distinction a une portée politique forte : le même commerce "
      "intrabranche est perçu comme bénéfique entre économies comparables, "
      "mais comme une menace lorsqu’il oppose des producteurs domestiques à "
      "des concurrents à bas coûts. Le cours souligne que la seconde "
      "mondialisation se distingue de la première par la domination durable "
      "des produits manufacturés — environ les trois quarts du commerce de "
      "marchandises — tandis que les services en représentent environ un "
      "quart et progressent plus vite depuis 2005.",
  diss="Idée fine à exploiter : la fragmentation productive relance une "
       "logique de différences à l’intérieur même d’un produit."),

f(id='q21-n72', sp='c21-16', niv='raisonner', type='qcm', b=5749,
  q="Pourquoi le commerce mondial est-il plus volatil que la production ?",
  opts=["Parce que les statistiques commerciales sont peu fiables",
        "Parce qu’il sur-réagit traditionnellement aux cycles économiques : il "
        "chute davantage que le PIB pendant les grandes récessions, comme en "
        "2008-2009",
        "Parce que les prix internationaux sont fixes",
        "Parce que les droits de douane varient chaque année"],
  ans=1,
  why=["La fiabilité des données n’est pas en cause.",
       "Les prix internationaux sont au contraire très variables.",
       "Les tarifs évoluent, mais ce n’est pas la cause de cette volatilité."],
  exp="Cette procyclicité explique une partie du ralentissement récent : "
      "avant 2008, le commerce progressait nettement plus vite que le PIB ; "
      "depuis, il progresse à un rythme beaucoup plus proche, ce qui suffit à "
      "faire stagner le taux d’ouverture. Le cours insiste toutefois : le "
      "ralentissement est surtout structurel, lié à la transformation des "
      "modèles productifs, des politiques publiques et des chaînes de valeur.",
  diss="Distinction essentielle en dissertation : composante conjoncturelle "
       "(récessions de 2008 et 2020) et composante structurelle."),

f(id='q21-n73', sp='c21-16', niv='raisonner', type='qcmm', b=5762,
  q="Quelles fragilités de l’hypermondialisation les économistes identifient-"
    "ils dès le début des années 2010 ? (plusieurs réponses)",
  opts=["Un risque de guerre commerciale",
        "Un enjeu environnemental",
        "Une dépendance aux ressources essentielles",
        "Une impossibilité technique de fragmenter davantage la production",
        "La disparition annoncée des firmes multinationales"],
  ans=[0, 1, 2],
  why=["Exacte : le risque se matérialise notamment à partir de 2017.",
       "Exacte : le coût environnemental des échanges devient un enjeu "
       "central.",
       "Exacte : les dépendances stratégiques sont difficilement soutenables "
       "en période de crise.",
       "Aucune impossibilité technique n’est invoquée : c’est un choix "
       "stratégique qui change.",
       "Les FMN demeurent les acteurs centraux de la mondialisation."],
  exp="L’hypermondialisation révèle ses fragilités lorsqu’elle crée des "
      "dépendances commerciales, environnementales et stratégiques "
      "difficilement soutenables. Depuis 2008, le modèle semble atteindre un "
      "plafond : la progression du commerce ralentit, les chaînes de valeur "
      "cessent de s’allonger et les États réclament davantage de "
      "souveraineté."),

# ------------------------------------------------------------- c21-17
f(id='q21-n74', sp='c21-17', niv='raisonner', type='qcmm', b=5819,
  q="Quelles idées reçues sur les migrations contemporaines le cours "
    "corrige-t-il ? (plusieurs réponses)",
  opts=["Les migrations ne sont pas principalement Sud-Nord : les migrations "
        "Sud-Sud sont au moins aussi importantes",
        "« La misère ne migre pas » : migrer suppose de disposer de "
        "ressources financières, éducatives et relationnelles minimales",
        "L’immigration concerne largement des individus jeunes, en âge de "
        "travailler, dont une part importante est qualifiée",
        "L’effet budgétaire de l’immigration est généralement proche de la "
        "neutralité",
        "L’immigration se substitue systématiquement aux travailleurs natifs"],
  ans=[0, 1, 2, 3],
  why=["Exacte : certains pays du Sud connaissent une forte croissance et "
       "attirent de la main-d’œuvre.",
       "Exacte : les plus pauvres sont précisément ceux qui ne peuvent pas "
       "partir.",
       "Exacte : c’est le profil décrit pour l’immigration en France.",
       "Exacte : les dépenses publiques supplémentaires sont largement "
       "compensées par impôts, cotisations et consommation.",
       "Faux : le cours souligne davantage de complémentarité que de "
       "substitution, migrants et natifs occupant souvent des segments "
       "différents du marché du travail."],
  exp="Le cours ajoute que la pression concurrentielle se concentre sur le "
      "marché secondaire du travail et touche souvent davantage les migrants "
      "déjà installés que l’ensemble des natifs. Il relève aussi un effet "
      "indirect : le développement de services domestiques complémentaires "
      "peut accroître la participation des femmes natives au marché du "
      "travail."),

f(id='q21-n75', sp='c21-17', niv='comprendre', type='qcm', b=5911,
  q="Comment l’immigration peut-elle soutenir à la fois la croissance "
    "extensive et la croissance intensive ?",
  opts=["Uniquement par la croissance extensive, en augmentant la population "
        "active",
        "Par la croissance extensive, en augmentant la quantité de travail "
        "disponible, et par la croissance intensive, grâce à l’innovation et "
        "à l’entrepreneuriat — environ 44 % des entreprises auraient au moins "
        "un fondateur immigré selon l’étude citée",
        "Uniquement par les transferts financiers vers les pays d’origine",
        "Elle ne soutient aucune forme de croissance"],
  ans=1,
  why=["L’effet extensif existe mais n’épuise pas l’analyse.",
       "Les transferts bénéficient aux pays d’origine, non à la croissance du "
       "pays d’accueil.",
       "Le cours établit au contraire plusieurs canaux positifs."],
  exp="L’immigration augmente mécaniquement la population active, donc la "
      "quantité de travail et la production potentielle. Mais elle peut aussi "
      "soutenir l’innovation, l’entrepreneuriat et la surreprésentation de "
      "certains migrants dans les activités technologiques. Du côté des pays "
      "d’origine, les transferts constituent une ressource majeure — environ "
      "10 % du PIB pour le Maroc selon l’ordre de grandeur évoqué — mais "
      "l’émigration qualifiée peut provoquer une fuite des cerveaux.",
  diss="La fuite des cerveaux peut contribuer à la trappe à revenu "
       "intermédiaire, en privant les émergents des compétences nécessaires à "
       "leur montée en gamme."),

f(id='q21-n76', sp='c21-17', niv='comprendre', type='assoc', b=5985,
  q="Associez chaque type d’IDE à sa logique.",
  ans=[["Reproduire à l’étranger une activité productive afin de satisfaire directement le marché local", "L’IDE horizontal"],
       ["Les IDE américains vers l’Europe dans les années 1950-1960, qui contournent les barrières commerciales", "L’IDE horizontal"],
       ["Fragmenter la production internationalement pour exploiter les différences de coûts et de dotations factorielles", "L’IDE vertical"],
       ["Les filiales-ateliers au cœur de l’hypermondialisation, entre lesquelles circulent les biens intermédiaires", "L’IDE vertical"]],
  exp="Le traité de Rome de 1957 illustre la logique horizontale : produire "
      "en Europe permet d’accéder au marché commun. À partir des années "
      "1970-1990, la logique change et devient verticale, transformant les "
      "FMN en réseaux mondiaux de production. La géographie des IDE s’est "
      "aussi rééquilibrée : près des deux tiers des flux vont désormais vers "
      "les pays émergents et en développement, qui sont également devenus des "
      "investisseurs importants.",
  diss="Nuance de méthode : la montée des émergents est très visible dans les "
       "flux récents, mais les économies avancées restent dominantes en "
       "stocks accumulés."),

f(id='q21-n77', sp='c21-17', niv='raisonner', type='qcm', b=6048,
  q="Pourquoi la Chine investit-elle massivement à l’étranger ?",
  opts=["Uniquement pour placer ses excédents financiers",
        "Pour trois raisons combinées : acquérir des technologies et du "
        "savoir-faire par rachats et prises de participation, ouvrir des "
        "débouchés, et sécuriser les approvisionnements stratégiques "
        "nécessaires au numérique et à la transition énergétique",
        "Pour délocaliser l’intégralité de sa production",
        "Pour réduire son excédent courant"],
  ans=1,
  why=["Le placement financier existe mais ne résume pas la stratégie "
       "chinoise.",
       "La Chine conserve une base productive considérable.",
       "La réduction de l’excédent n’est pas l’objectif poursuivi par ces "
       "IDE."],
  exp="L’enchaînement est explicite : IDE → rachat ou prise de participation "
      "→ savoir-faire étranger → montée en gamme. Les IDE deviennent donc un "
      "instrument de politique industrielle. La Chine est ainsi devenue "
      "exportatrice nette d’IDE, ce qui marque un renversement complet par "
      "rapport à sa position initiale de simple pays d’accueil.",
  diss="À rapprocher du cas plus général : un même pays peut changer de "
       "logique d’IDE à mesure qu’il se développe, passant de plateforme à "
       "bas coûts à grand marché recherché."),

f(id='q21-n78', sp='c21-17', niv='raisonner', type='qcm', b=6134,
  q="Pourquoi les investissements de portefeuille sont-ils plus déstabilisants "
    "que les IDE ?",
  opts=["Parce qu’ils sont toujours plus importants en volume",
        "Parce que leur forte liquidité permet des mouvements massifs et "
        "extrêmement rapides de capitaux, alors qu’un IDE est difficilement "
        "réversible à court terme",
        "Parce qu’ils sont illégaux dans certains pays",
        "Parce qu’ils ne rapportent aucun rendement"],
  ans=1,
  why=["Le volume varie selon les périodes : c’est la liquidité qui importe.",
       "Ils sont parfaitement licites, même si certains pays les encadrent.",
       "Ils sont au contraire motivés par la recherche de rendement."],
  exp="C’est une différence fondamentale de nature. Avant 2008, les flux "
      "financiers les plus volatils dominaient la mondialisation financière ; "
      "la crise a réduit leur part et augmenté le poids relatif des IDE, ce "
      "qui rend la structure des flux relativement moins instable qu’avant "
      "2008. Le choc Volcker avait montré la fragilité de cette finance "
      "mondialisée : rendement aux États-Unis ↑ → les capitaux quittent les "
      "pays en développement.",
  diss="Conséquence pour les stratégies de développement : encourager les IDE "
       "tout en contrôlant davantage les flux de portefeuille — c’est "
       "précisément l’ouverture maîtrisée asiatique."),

# ------------------------------------------------------------- c21-18
f(id='q21-n79', sp='c21-18', niv='comprendre', type='qcm', b=6260,
  q="Pourquoi l’idée d’une mondialisation irréversible a-t-elle longtemps "
    "dominé, et comment le cours la relativise-t-il ?",
  opts=["Parce que les traités internationaux l’interdisaient juridiquement",
        "Parce que, chez Ricardo comme chez Marx — pour des raisons "
        "différentes —, l’ouverture extérieure apparaît comme un mécanisme "
        "permettant au capitalisme de dépasser ses contradictions, idée "
        "résumée par le « There Is No Alternative » de Thatcher ; mais la "
        "première mondialisation et la crise de 2008 montrent que l’ouverture "
        "peut être remise en cause",
        "Parce que la mondialisation n’a jamais connu de recul",
        "Parce que les firmes multinationales sont devenues plus puissantes "
        "que les États"],
  ans=1,
  why=["Aucun traité ne rend l’ouverture irréversible.",
       "L’entre-deux-guerres est précisément un recul majeur.",
       "Le rapport de force État-firme est un enjeu du chapitre, pas "
       "l’explication de cette croyance."],
  exp="Chez Ricardo, importer du blé moins cher réduit le coût des "
      "subsistances, donc les salaires, et préserve les profits. Chez Marx, "
      "la production progresse plus vite que la demande interne, ce qui impose "
      "de trouver des débouchés extérieurs. L’hypermondialisation s’est "
      "accompagnée de l’idée que l’intégration internationale constituait une "
      "évolution inévitable — conviction que la crise de 2008 remet "
      "profondément en cause.",
  diss="Citation utile : « There Is No Alternative », formule de Thatcher au "
       "début des années 1980."),

f(id='q21-n80', sp='c21-18', niv='comprendre', type='qcm', b=6316,
  q="Quels sont les deux sens du mot « démondialisation » distingués par le "
    "cours ?",
  opts=["Un sens économique et un sens juridique",
        "Un sens factuel — les stratégies par lesquelles les États cherchent "
        "à limiter leur dépendance extérieure — et un sens politique, celui "
        "d’un projet volontaire de réorganisation de l’économie mondiale, "
        "défendu notamment par Walden Bello au début des années 2000",
        "Un sens commercial et un sens migratoire",
        "Un sens national et un sens régional"],
  ans=1,
  why=["La distinction n’est pas disciplinaire.",
       "Les deux sens recouvrent toutes les dimensions de l’ouverture.",
       "L’échelle n’est pas le critère de distinction."],
  exp="La distinction est essentielle pour répondre correctement à la "
      "question « assistons-nous à une démondialisation ? ». Au sens factuel, "
      "on observe surtout un ralentissement. Au sens politique, la "
      "démondialisation désigne un projet de réorganisation autour de "
      "relations jugées plus soutenables et plus équitables, ce qui est une "
      "tout autre question.",
  diss="Méthode de dissertation : toujours distinguer le constat statistique "
       "du projet politique."),

f(id='q21-n81', sp='c21-18', niv='appliquer', type='qcm', b=6442,
  q="Que montre la comparaison entre l’iPhone 3G de 2009 et l’iPhone X de "
    "2018 dans le cours ?",
  opts=["Que le prix de vente des téléphones a fortement augmenté",
        "Que la valeur ajoutée domestique chinoise incorporée dans les "
        "exportations a fortement progressé, la Chine réduisant sa dépendance "
        "aux composants étrangers",
        "Que la production a été relocalisée aux États-Unis",
        "Que les coûts de transport ont diminué"],
  ans=1,
  why=["Le prix de vente n’est pas l’objet de la comparaison.",
       "La production reste largement asiatique.",
       "Les coûts logistiques ne sont pas en cause ici."],
  exp="La montée en gamme chinoise se traduit par une augmentation rapide de "
      "la valeur ajoutée domestique dans ses exportations : la Chine remplace "
      "progressivement une logique d’assemblage à partir d’intrants importés "
      "par une production domestique plus complète. Le lancement de Made in "
      "China 2025, en 2015, et les plans quinquennaux récents inscrivent cette "
      "trajectoire dans une stratégie explicite d’innovation et de "
      "souveraineté technologique.",
  diss="Exemple parfait pour relier mesure en valeur ajoutée, montée en gamme "
       "et ralentissement du commerce mondial."),

f(id='q21-n82', sp='c21-18', niv='comprendre', type='assoc', b=6529,
  q="Associez chaque stratégie de recomposition des chaînes de valeur à sa "
    "définition.",
  ans=[["Relocaliser la production sur le territoire national", "Le reshoring"],
       ["Rapprocher la production de pays géographiquement proches", "Le nearshoring"],
       ["Privilégier des pays considérés comme politiquement sûrs ou alliés", "Le friendshoring"],
       ["Recourir aux normes, aux subventions et aux exigences de contenu local plutôt qu’aux droits de douane", "Le protectionnisme furtif"]],
  exp="Ces stratégies traduisent le passage d’une logique d’optimisation pure "
      "des coûts à une logique combinant efficacité, résilience et sécurité "
      "géopolitique. Elles sont portées par deux moteurs : la volonté des "
      "États, et la réévaluation par les entreprises du coût réel de la "
      "délocalisation, qui intègre désormais les risques logistiques, "
      "géopolitiques et d’approvisionnement.",
  diss="La relocalisation est plus crédible dans les industries fortement "
       "capitalistiques, où le coût du travail pèse moins lourd."),

f(id='q21-n83', sp='c21-18', niv='raisonner', type='qcm', b=6619,
  q="Pourquoi le commerce mondial résiste-t-il au retour du protectionnisme, "
    "malgré des mesures comme le « Liberation Day » du 2 avril 2025 ?",
  opts=["Parce que les droits de douane annoncés n’ont jamais été appliqués",
        "Parce que le retour du protectionnisme entraîne surtout une "
        "recomposition géographique des flux plutôt qu’un effondrement du "
        "commerce : l’OMC cite même une croissance positive du commerce "
        "mondial en 2025",
        "Parce que les entreprises cessent toute exportation",
        "Parce que le protectionnisme fait toujours augmenter les échanges"],
  ans=1,
  why=["Les mesures sont bien mises en œuvre : le cours parle d’un retour "
       "spectaculaire des droits de douane.",
       "Les exportations se poursuivent, en se réorientant.",
       "Le protectionnisme réduit en principe les échanges : c’est leur "
       "redirection qui compense."],
  exp="Le retour des droits de douane sous Trump marque le passage d’un "
      "protectionnisme largement furtif à un protectionnisme tarifaire "
      "assumé, explicitement utilisé comme instrument de puissance. Mais les "
      "flux se redirigent : la période relève donc moins d’une véritable "
      "démondialisation que d’une reconfiguration de l’intégration mondiale, "
      "marquée par davantage de régionalisation, de sécurité économique et de "
      "tensions géopolitiques.",
  diss="Conclusion générale du chapitre : la mondialisation ne disparaît pas, "
       "la recherche du coût minimal cède la place à la sécurité économique, "
       "à la résilience et à la proximité géopolitique."),

]
