# -*- coding: utf-8 -*-
"""Chapitre 21 (2ᵉ année, ch. 1) — La mondialisation : dimensions, asymétries,
déséquilibres extérieurs et recompositions."""

SP = {
 'c21-01': 'Les trois dimensions de l’ouverture : commerciale, productive, financière et monétaire',
 'c21-02': 'Définir la mondialisation : Michalet, Giraud, privilège du dollar, centre de gravité',
 'c21-03': 'Une mondialisation asymétrique : centre/périphérie, Prebisch, DIT, DIPP, FMN',
 'c21-04': 'Stratégies des États, gagnants et perdants, Milanovic et la mesure des inégalités',
 'c21-05': 'Montée en gamme, malédiction des ressources, Stolper-Samuelson, courbe de l’éléphant',
 'c21-06': 'La balance des paiements, besoin de financement et déficits jumeaux',
 'c21-07': 'Position extérieure nette, compétitivité et interprétation du déficit',
 'c21-08': 'Risques du déficit extérieur et financement du développement : Nurkse, Rostow, Volcker',
 'c21-09': 'Les déséquilibres mondiaux : Hélène Rey, surépargne chinoise, sous-investissement européen',
 'c21-10': 'Mesurer la mondialisation : taux d’ouverture, commerce en valeur ajoutée, chaînes de valeur',
 'c21-11': 'Les dépendances créées par les chaînes de valeur : matériaux critiques, Chine, RCEP',
 'c21-12': 'La première mondialisation (1870-1913) : mise en place et transformation des échanges',
 'c21-13': 'Capitaux et coûts de transport : Baldwin, Bairoch, Hamilton, List, convergence des prix',
 'c21-14': 'Retour du protectionnisme, asymétries coloniales et repli de l’entre-deux-guerres',
 'c21-15': 'Remondialisation 1945-1980 : GATT, Bretton Woods, Japon ; puis hypermondialisation',
 'c21-16': 'OMC, crise du multilatéralisme, régionalisation et nature des échanges',
 'c21-17': 'Migrations contemporaines, IDE et globalisation financière',
 'c21-18': 'Slowbalization : réversibilité, démondialisation, deuxième choc chinois, reshoring',
}

# Questions écartées. Les vrai/faux retirés reprennent à l'identique, sous
# forme inversée, un QCM déjà posé ailleurs dans le chapitre. ch21-qcm-33
# porte sur l'étalon-or, qui n'apparaît dans aucun cours.
DROP = [
 'ch21-vf-1',    # ≡ ch21-qcm-5 et ch21-open-1 (les trois dimensions)
 'ch21-vf-2',    # ≡ ch21-qcm-2 (IDE et logique productive)
 'ch21-vf-3',    # ≡ ch21-qcm-6 (Michalet, processus multidimensionnel)
 'ch21-vf-4',    # ≡ ch21-qcm-9 (l’hypermondialisation cumule les dimensions)
 'ch21-vf-5',    # ≡ ch21-qcm-11 (le privilège exorbitant)
 'ch21-vf-6',    # ≡ ch21-qcm-13 (Prebisch et les termes de l’échange)
 'ch21-vf-8',    # ≡ ch21-qcm-19 (la malédiction des ressources)
 'ch21-vf-9',    # ≡ ch21-qcm-21 (la courbe de l’éléphant)
 'ch21-vf-10',   # ≡ ch21-qcm-28 (la balance des paiements est équilibrée)
 'ch21-vf-12',   # ≡ ch21-qcm-26 (déficit courant et besoin de financement)
 'ch21-vf-13',   # ≡ ch21-open-10 (un déficit n’est pas toujours un problème)
 'ch21-vf-14',   # ≡ ch21-qcm-25 (l’identité macroéconomique)
 'ch21-vf-15',   # ≡ ch21-qcm-29 (définition du taux d’ouverture)
 'ch21-vf-16',   # ≡ ch21-qcm-30 (le commerce en valeur ajoutée)
 'ch21-vf-17',   # ≡ ch21-qcm-37 (une mondialisation moins migratoire)
 'ch21-vf-18',   # ≡ ch21-qcm-35 (l’entre-deux-guerres, période de repli)
 'ch21-vf-19',   # ≡ ch21-qcm-38 (la slowbalization n’est pas la démondialisation)
 'ch21-qcm-33',  # l’étalon-or n’apparaît dans aucun cours
]


def f(**kw):
    return kw


FIX = {

# =============================================================== c21-01
'ch21-qcm-1': f(niv='connaitre', sp='c21-01', b=18,
 exp="L’ouverture commerciale désigne les échanges de biens et de services "
     "entre les résidents d’un pays et le reste du monde : une entreprise "
     "française qui vend des voitures en Allemagne réalise une exportation de "
     "biens, un Français qui achète un service numérique américain une "
     "importation de services. C’est la dimension strictement commerciale de "
     "la mondialisation.",
 why=["Les capitaux financiers relèvent de l’ouverture financière et "
      "monétaire.",
      "Les devises relèvent de la dimension monétaire, qui accompagne les "
      "mouvements de capitaux.",
      "La circulation de la main-d’œuvre relève de l’ouverture productive, "
      "aux côtés des IDE."]),
'ch21-qcm-2': f(niv='comprendre', sp='c21-01', b=70,
 exp="Un IDE est un investissement réalisé dans un autre pays dans une "
     "logique productive : création d’une usine à l’étranger, acquisition "
     "d’une entreprise étrangère. Son objectif est de participer durablement "
     "à une activité productive — la convention statistique retient un seuil "
     "de 10 % du capital ou des droits de vote. L’investissement de "
     "portefeuille vise au contraire un simple placement financier.",
 why=["La taille n’est pas le critère : un IDE peut être modeste et un "
      "placement considérable.",
      "Les deux traversent les frontières par définition.",
      "Les IDE sont très majoritairement le fait d’entreprises privées."],
 diss="Conséquence importante pour la suite du chapitre : les IDE sont "
      "beaucoup plus stables que les investissements de portefeuille, dont la "
      "liquidité autorise des mouvements massifs et brutaux."),
'ch21-qcm-3': f(niv='connaitre', sp='c21-01', b=80,
 exp="Un investissement de portefeuille correspond à l’achat d’actifs "
     "financiers étrangers dans une logique de placement et de rendement : "
     "actions, obligations, titres publics étrangers. L’objectif principal "
     "n’est pas de contrôler une activité productive, ce qui le distingue "
     "nettement de l’IDE.",
 why=["La prise de contrôle d’une entreprise caractérise précisément l’IDE.",
      "Un prêt bancaire national ne franchit aucune frontière.",
      "Une exportation de services relève de l’ouverture commerciale."]),
'ch21-qcm-4': f(niv='comprendre', sp='c21-01', b=119,
 exp="Pour acheter un bon du Trésor américain, un résident français qui "
     "dispose d’euros doit d’abord obtenir des dollars : il passe par le "
     "marché des changes. L’opération augmente l’offre d’euros et la demande "
     "de dollars. Les mouvements internationaux de capitaux ont donc "
     "toujours une dimension monétaire, puisqu’ils influencent l’offre, la "
     "demande et le taux de change des monnaies.",
 why=["Les taux de change ne sont pas fixes dans le régime actuel : ils "
      "varient précisément sous l’effet de ces opérations.",
      "Aucune obligation étatique n’est en cause : c’est une nécessité "
      "technique liée à la pluralité des monnaies.",
      "Les banques exécutent l’opération, elles ne l’imposent pas."],
 diss="C’est pourquoi le cours parle d’ouverture « financière et "
      "monétaire » : la seconde dimension découle de la première."),
'ch21-qcm-5': f(niv='connaitre', sp='c21-01', b=137,
 exp="La mondialisation repose sur trois formes d’ouverture : commerciale, "
     "par les échanges de biens et de services ; productive, par la mobilité "
     "du capital productif via les IDE et du travail via les migrations ; "
     "financière et monétaire, par les mouvements de capitaux de placement et "
     "les conversions de devises qu’ils impliquent.",
 why=["La distinction agricole / industriel / tertiaire porte sur les "
      "secteurs d’activité, non sur les formes d’ouverture.",
      "Public / privé / mixte décrit des statuts juridiques.",
      "Local / national / mondial décrit des échelles géographiques."],
 diss="Cette distinction commande tout le chapitre : elle permet de séparer "
      "mondialisation économique, liée à la production et aux échanges "
      "réels, et mondialisation financière et monétaire."),
'ch21-open-1': f(niv='comprendre', sp='c21-01', b=1,
 exp="L’ouverture commerciale porte sur les échanges de biens et de services "
     "entre résidents et non-résidents : c’est la forme la plus simple "
     "d’ouverture. L’ouverture productive concerne la circulation des "
     "facteurs de production eux-mêmes : le capital productif à travers les "
     "investissements directs à l’étranger — création d’usine, acquisition "
     "d’entreprise étrangère — et le travail à travers les migrations "
     "internationales. À partir du moment où ce sont les facteurs qui "
     "circulent, on dépasse le simple commerce international, puisque c’est "
     "la localisation de la production qui se modifie. L’ouverture financière "
     "et monétaire recouvre enfin la circulation des capitaux de placement, "
     "notamment les investissements de portefeuille, et les mouvements de "
     "devises qui les accompagnent : acheter un actif étranger suppose de "
     "convertir sa monnaie, ce qui influence les taux de change.",
 diss="La mondialisation est donc multidimensionnelle, et l’une de ses "
      "dimensions peut progresser alors qu’une autre stagne — ce que Michalet "
      "formalise avec ses trois configurations."),
'ch21-open-2': f(niv='comprendre', sp='c21-01', b=69,
 exp="L’investissement direct à l’étranger est réalisé dans une logique "
     "productive : il vise une influence durable sur l’activité implantée à "
     "l’étranger, conventionnellement à partir de 10 % du capital ou des "
     "droits de vote. Il prend la forme d’une création d’usine, d’une "
     "acquisition d’entreprise étrangère ou d’une prise de participation "
     "significative. L’investissement de portefeuille est un achat d’actifs "
     "financiers étrangers — actions, obligations, titres publics — dans une "
     "logique de placement et de rendement, sans objectif de contrôle. Le "
     "premier relève donc de l’ouverture productive, le second de l’ouverture "
     "financière. Leur mobilité diffère fortement : un IDE est difficilement "
     "réversible à court terme, alors qu’un investissement de portefeuille "
     "peut être revendu immédiatement, ce qui en fait un vecteur beaucoup plus "
     "déstabilisant."),
'ch21-open-3': f(niv='comprendre', sp='c21-02', b=302,
 exp="Dans Qu’est-ce que la mondialisation ? (2002), Charles-Albert Michalet "
     "montre que la mondialisation est un processus multidimensionnel dont la "
     "hiérarchie des dimensions évolue dans le temps. La configuration "
     "internationale repose principalement sur l’ouverture des économies aux "
     "échanges de biens et services : les États y jouent un rôle "
     "fondamental, et elle domine la première mondialisation de 1870-1913, "
     "avec un taux d’ouverture atteignant environ 15 %. La configuration "
     "multinationale, après 1945, met au centre les IDE et les firmes "
     "multinationales, qui organisent directement une partie de leur "
     "production à l’étranger, puis fragmentent leurs chaînes de valeur. La "
     "configuration globale, à partir des années 1980, est marquée par la "
     "prédominance de la finance internationale : libéralisation des "
     "mouvements de capitaux, intégration des marchés financiers, montée des "
     "investisseurs institutionnels. Point essentiel : ces configurations ne "
     "se remplacent pas, elles s’accumulent — c’est ce cumul qui définit "
     "l’hypermondialisation.",
 diss="À retenir : commercial + productif + financier → hypermondialisation."),

# =============================================================== c21-02
'ch21-qcm-6': f(niv='connaitre', sp='c21-02', b=302,
 exp="Pour Michalet, la mondialisation est un processus multidimensionnel "
     "dont les composantes commerciale, productive et financière se "
     "développent successivement tout en se cumulant. Son originalité est de "
     "montrer que la hiérarchie de ces dimensions évolue : une dimension "
     "domine chaque grande période, sans que les précédentes disparaissent.",
 why=["La réduire au commerce est précisément l’erreur que Michalet "
      "dénonce.",
      "La mondialisation n’est pas une politique publique mais un processus "
      "historique.",
      "Un régime monétaire est un ensemble de règles de change : la "
      "dimension monétaire n’est qu’un aspect du phénomène."]),
'ch21-qcm-9': f(niv='comprendre', sp='c21-02', b=411,
 exp="L’hypermondialisation correspond au cumul des trois configurations : "
     "échanges commerciaux, fragmentation productive et circulation massive "
     "des capitaux. Elle se distingue des vagues précédentes par un degré "
     "d’ouverture sans précédent — le poids des échanges dans l’économie "
     "mondiale est environ deux fois plus élevé qu’en 1913 — et par "
     "l’intégration d’un nombre croissant de pays auparavant relativement "
     "fermés.",
 why=["La finance ne remplace pas le commerce : les deux progressent "
      "simultanément.",
      "La démondialisation est l’hypothèse inverse, discutée à propos de la "
      "période postérieure à 2008.",
      "Le protectionnisme est précisément ce que l’hypermondialisation "
      "réduit, avant son retour récent."],
 diss="Formule à retenir : l’hypermondialisation n’est pas une nouvelle "
      "forme de mondialisation, c’est la superposition des trois formes "
      "antérieures."),
'ch21-qcm-10': f(niv='comprendre', sp='c21-02', b=481,
 exp="Pierre-Noël Giraud analyse les globalisations comme une généralisation "
     "des compétitions. Cette compétition concerne d’abord les territoires : "
     "la mobilité des firmes leur permet d’arbitrer entre différentes "
     "localisations, ce qui contraint les États à développer des politiques "
     "d’attractivité. Elle concerne aussi les capitaux financiers, les pays "
     "devant offrir des conditions suffisamment attractives pour les attirer.",
 why=["Giraud souligne au contraire que la mondialisation n’est pas "
      "harmonieuse : elle intensifie les rapports de force.",
      "Les échanges augmentent dans cette période : ce n’est pas son "
      "constat.",
      "Sa lecture est globale — commerciale, productive, financière — et non "
      "strictement monétaire."],
 diss="Giraud sert deux fois dans le chapitre : mondialisation = émergence + "
      "fragmentation, c’est-à-dire des territoires qui montent et d’autres "
      "qui décrochent."),
'ch21-qcm-11': f(niv='connaitre', sp='c21-02', b=520,
 exp="Le « privilège exorbitant » désigne l’avantage que les États-Unis "
     "tirent du statut international du dollar. Les actifs américains, "
     "notamment les titres publics, sont particulièrement recherchés car ils "
     "associent liquidité, sécurité et rôle central du dollar dans le système "
     "monétaire international. Les États-Unis peuvent donc attirer "
     "durablement les capitaux étrangers et financer leurs déséquilibres dans "
     "des conditions particulièrement favorables, sans offrir les rendements "
     "les plus élevés.",
 why=["L’agriculture américaine est puissante mais n’explique pas cet "
      "avantage financier.",
      "La démographie n’intervient pas dans ce mécanisme.",
      "Les matières premières ne fondent pas la demande mondiale d’actifs "
      "américains."],
 diss="Ce privilège explique comment les États-Unis peuvent soutenir une "
      "position extérieure nette de l’ordre de −90 % du PIB sans crise de "
      "financement."),
'ch21-open-4': f(niv='connaitre', sp='c21-02', b=411,
 exp="L’hypermondialisation désigne une ouverture quantitativement sans "
     "précédent, née du cumul des trois dimensions identifiées par "
     "Michalet : échanges commerciaux, fragmentation productive et "
     "circulation massive des capitaux. Elle ne remplace pas les formes "
     "antérieures d’internationalisation mais les additionne, ce qui explique "
     "l’intensité des interdépendances contemporaines. Elle se caractérise "
     "aussi par sa portée véritablement mondiale : de nombreux pays "
     "auparavant relativement fermés participent désormais intensément aux "
     "échanges, le poids des échanges dans l’économie mondiale atteignant "
     "environ le double du maximum de la première mondialisation. Elle semble "
     "toutefois perdre de sa vigueur depuis la crise de 2008, le taux "
     "d’ouverture mondial stagnant autour de 30 %."),

# =============================================================== c21-03
'ch21-qcm-7': f(niv='connaitre', sp='c21-02', b=351,
 exp="La configuration multinationale de Michalet met au centre "
     "l’investissement direct et l’implantation des firmes à l’étranger. "
     "Après 1945, les entreprises ne se contentent plus de vendre à "
     "l’étranger : elles y produisent, ce qui accroît la mobilité "
     "internationale des facteurs de production. Cette organisation prépare "
     "la fragmentation internationale des processus productifs.",
 why=["Le commerce de biens domine la configuration internationale, la "
      "première.",
      "Les migrations relèvent de l’ouverture productive mais ne sont pas "
      "l’objet de cette configuration.",
      "Aucun régime monétaire n’est au cœur de cette configuration."]),
'ch21-qcm-15': f(niv='comprendre', sp='c21-03', b=820,
 exp="La division internationale du travail traditionnelle repose sur une "
     "spécialisation verticale de l’économie mondiale : les pays "
     "périphériques fournissent les matières premières, les pays du centre "
     "concentrent les activités industrielles à plus forte valeur ajoutée, "
     "puis revendent une partie de leurs produits manufacturés à la "
     "périphérie. Cette division n’est pas seulement un produit du marché : "
     "elle est largement imposée pendant la colonisation.",
 why=["La fragmentation des processus productifs est la DIPP, propre à la "
      "mondialisation contemporaine.",
      "L’autarcie est l’absence d’échange, donc le contraire d’une division "
      "internationale du travail.",
      "Le libre-échange intégral ne décrit pas cette organisation, largement "
      "contrainte et protectionniste."]),
'ch21-qcm-16': f(niv='connaitre', sp='c21-03', b=923,
 exp="La DIPP est la décomposition internationale des processus productifs : "
     "une entreprise découpe sa chaîne de production en plusieurs étapes et "
     "localise chacune là où elle est la plus rentable, selon les conditions "
     "de coût, de compétence ou d’accès au marché. Ce n’est plus le produit "
     "qui est échangé mais la tâche.",
 why=["« Division internationale des prix de production » n’existe pas.",
      "La dette des pays pauvres est un tout autre sujet.",
      "La demande intérieure par produit n’a aucun rapport avec cette "
      "notion."],
 diss="À articuler avec la courbe du sourire : la fragmentation concentre "
      "conception, R&D, marketing et services dans les économies avancées et "
      "l’assemblage dans les pays à bas coûts."),
'ch21-qcm-18': f(niv='connaitre', sp='c21-03', b=835,
 exp="Acemoglu et Robinson mettent en avant le rôle des institutions "
     "extractives : des institutions conçues pour extraire les ressources "
     "d’une partie de la population ou du territoire au bénéfice d’une "
     "minorité. La colonisation a souvent installé de telles institutions, "
     "destinées à capter les ressources locales au profit des puissances "
     "dominantes, ce qui a freiné la formation d’un développement autonome.",
 why=["Le climat n’est pas le facteur explicatif qu’ils privilégient.",
      "La démographie n’est pas au centre de leur analyse.",
      "Les transports expliquent l’essor des échanges, non les écarts "
      "institutionnels de développement."],
 diss="Argument décisif contre les lectures purement géographiques du "
      "sous-développement : ce sont les règles, non la nature, qui bloquent."),
'ch21-qcm-42': f(niv='comprendre', sp='c21-03', b=656,
 exp="Le décrochage européen se mesure par la baisse du poids de l’Europe "
     "dans le PIB mondial et par la diminution de ses parts de marché "
     "internationales. Il s’agit d’un déclin relatif et non nécessairement "
     "d’un appauvrissement absolu : les économies européennes peuvent "
     "continuer à croître tout en voyant leur poids diminuer, sous l’effet de "
     "la croissance beaucoup plus rapide des économies asiatiques.",
 why=["Le PIB européen continue de croître : ce n’est pas la mesure du "
      "décrochage.",
      "Les exportations européennes augmentent en valeur ; c’est leur part "
      "de marché qui recule.",
      "Le chômage n’est pas l’indicateur utilisé ici."],
 diss="Distinction indispensable en dissertation : décrochage relatif ≠ "
      "appauvrissement."),
'ch21-vf-7': f(niv='comprendre', sp='c21-03', b=819,
 exp="Les deux notions sont très différentes. La DIT traditionnelle est une "
     "spécialisation verticale par produits : la périphérie fournit les "
     "matières premières, le centre produit les biens manufacturés. La DIPP "
     "est une fragmentation des étapes d’un même processus de production "
     "entre plusieurs pays : ce ne sont plus des produits mais des tâches qui "
     "sont réparties internationalement.",
 diss="Repère chronologique : la DIT structure la première mondialisation, la "
      "DIPP s’impose à partir des années 1980 avec la firme globale."),
'ch21-vf-20': f(niv='comprendre', sp='c21-03', b=574,
 exp="C’est la lecture historique proposée par le cours à partir des données "
     "de Maddison : les futurs BRIC représentaient environ 51 % du PIB "
     "mondial en 1700 et encore environ 55 % en 1820, avant que "
     "l’industrialisation occidentale ne transforme totalement la hiérarchie "
     "et que leur poids ne chute fortement en 1950. L’émergence actuelle peut "
     "donc s’interpréter comme un retour vers une puissance économique "
     "historiquement ancienne."),
'ch21-open-5': f(niv='comprendre', sp='c21-03', b=856,
 exp="Prebisch montre que les pays spécialisés dans les produits primaires "
     "subissent une détérioration tendancielle de leurs termes de l’échange : "
     "le prix de leurs exportations progresse moins vite que celui de leurs "
     "importations manufacturées. Ils doivent donc exporter toujours "
     "davantage pour financer un même volume d’importations, ce qui réduit "
     "progressivement leur pouvoir d’achat extérieur et les enferme dans "
     "leur spécialisation. Cette analyse s’inscrit dans sa lecture "
     "centre/périphérie : la colonisation a imposé aux territoires dominés une "
     "spécialisation répondant aux besoins des puissances européennes, les "
     "matières premières étant transformées au centre puis en partie revendues "
     "à la périphérie. Elle nourrit ensuite des approches plus radicales, "
     "comme la théorie de l’échange inégal, selon laquelle le commerce "
     "international reproduit les rapports de domination lorsque les pays "
     "échangent des productions incorporant des niveaux de rémunération et de "
     "valeur ajoutée très différents.",
 diss="Nuance que le cours impose : un bon diagnostic ne fait pas une bonne "
      "stratégie — les politiques de fermeture complète ont souvent échoué."),

# =============================================================== c21-04
'ch21-qcm-12': f(niv='connaitre', sp='c21-03', b=575,
 q="Que montrent les données historiques de Maddison citées par le cours à "
   "propos du poids des futurs BRIC dans le PIB mondial ?",
 opts=["Leur poids a toujours été faible avant les années 1990",
       "Ils représentaient environ 51 % du PIB mondial en 1700 et encore "
       "environ 55 % en 1820, avant une chute forte de leur poids en 1950",
       "Leur poids est resté stable depuis le XVIIIᵉ siècle",
       "Ils ont dépassé l’Europe occidentale dès 1950"],
 ans=1,
 exp="Ces données donnent une perspective de long terme : c’est "
     "l’industrialisation occidentale qui transforme totalement la hiérarchie "
     "économique mondiale, faisant chuter le poids relatif des grandes "
     "économies asiatiques. L’émergence contemporaine peut donc être lue, "
     "notamment du point de vue chinois, comme un retour vers une puissance "
     "économique historiquement ancienne plutôt que comme une émergence "
     "entièrement nouvelle.",
 why=["C’est l’inverse : leur poids était historiquement majoritaire avant "
      "la révolution industrielle.",
      "Leur poids s’effondre au contraire entre 1820 et 1950.",
      "En 1950, l’Europe occidentale et surtout les États-Unis dominent "
      "largement."],
 diss="Argument puissant pour relativiser la « montée » des émergents : il "
      "s’agit d’un rééquilibrage historique après deux siècles de domination "
      "occidentale."),
'ch21-qcm-39': f(niv='comprendre', sp='c21-18', b=6363,
 exp="Depuis 2008, le commerce mondial progresse beaucoup moins vite : son "
     "élasticité au PIB s’est rapprochée de 1, alors qu’il progressait "
     "nettement plus vite que la production pendant les années 1990-2000. "
     "C’est ce qui explique la stagnation du taux d’ouverture mondial autour "
     "de 30 % et ce que l’on appelle la slowbalization.",
 why=["La progression ralentit au contraire nettement par rapport à "
      "l’hypermondialisation.",
      "Il n’y a pas d’effondrement : le commerce continue de croître, et "
      "l’OMC anticipe même une croissance positive en 2025.",
      "Les échanges demeurent massifs : les chaînes de valeur mondiales "
      "subsistent."],
 diss="Le ralentissement est à la fois conjoncturel — le commerce "
      "sur-réagit aux récessions de 2008 et 2020 — et surtout structurel."),
'ch21-aut195-3': f(niv='comprendre', sp='c21-04', b=1090,
 exp="L’indice de Theil peut être décomposé entre une composante inter-pays "
     "et une composante intra-pays. Cette propriété est décisive, car les "
     "deux composantes évoluent en sens opposé : l’hypermondialisation réduit "
     "les écarts entre pays, grâce au rattrapage des grands émergents "
     "asiatiques, tout en accompagnant la réouverture des inégalités internes "
     "depuis les années 1980.",
 why=["Sa simplicité de calcul n’est pas l’argument retenu par le cours.",
      "Ce n’est pas son insensibilité aux hauts revenus qui le distingue "
      "ici.",
      "Il porte sur les revenus comme le Gini : la différence est sa "
      "décomposabilité."],
 diss="Outil indispensable pour résoudre le paradoxe distributif de la "
      "mondialisation, que la courbe de l’éléphant illustre graphiquement."),

# =============================================================== c21-05
'ch21-qcm-13': f(niv='comprendre', sp='c21-05', b=1514,
 exp="Selon Prebisch, la spécialisation primaire conduit à une détérioration "
     "des termes de l’échange : le prix des exportations primaires progresse "
     "moins vite que celui des importations manufacturées. Le pays doit donc "
     "exporter des volumes croissants pour financer un même panier "
     "d’importations : sa spécialisation devient une « spécialisation "
     "impasse » qui l’empêche durablement d’améliorer son niveau de vie.",
 why=["Une amélioration des termes de l’échange serait l’inverse du "
      "diagnostic de Prebisch.",
      "L’industrialisation rapide est précisément ce que cette "
      "spécialisation empêche.",
      "Rien n’indique une hausse des salaires : la rente profite souvent à "
      "une minorité."]),
'ch21-qcm-14': f(niv='connaitre', sp='c21-05', b=1528,
 exp="Les termes de l’échange rapportent le prix des exportations au prix des "
     "importations. Ils ne mesurent donc pas des montants mais une évolution "
     "relative de prix : quand ils se détériorent, le pays obtient moins "
     "d’importations pour un même volume d’exportations. C’est l’indicateur "
     "central de l’analyse de Prebisch.",
 why=["Le rapport du PIB aux exportations mesurerait plutôt un degré "
      "d’ouverture.",
      "Le rapport épargne / investissement renvoie à l’identité "
      "macroéconomique du solde extérieur.",
      "Le rapport impôts / dépenses décrit le solde budgétaire."]),
'ch21-qcm-19': f(niv='comprendre', sp='c21-05', b=1405,
 exp="La malédiction des ressources désigne le paradoxe de l’abondance : "
     "disposer de matières premières en quantité peut ralentir la "
     "diversification et le développement au lieu de les favoriser. Le "
     "mécanisme économique principal passe par le taux de change — c’est la "
     "maladie hollandaise — auquel s’ajoute la très forte volatilité des prix "
     "des matières premières.",
 why=["Il ne s’agit pas de l’épuisement physique des ressources mais d’un "
      "effet économique de leur abondance.",
      "Ce n’est pas un instrument fiscal.",
      "Ce n’est pas une crise monétaire, même si le taux de change joue un "
      "rôle central dans le mécanisme."]),
'ch21-qcm-20': f(niv='connaitre', sp='c21-05', b=1642,
 exp="La courbe de l’éléphant a été popularisée par Branko Milanovic. Elle "
     "porte sur la période 1988-2008, comprise entre l’ouverture des "
     "économies anciennement socialistes et la rupture de la crise "
     "financière, et compare l’évolution des revenus des individus selon "
     "leur position dans la distribution mondiale.",
 why=["Prebisch travaille sur les termes de l’échange et le rapport "
      "centre/périphérie.",
      "Michalet est l’auteur des trois configurations de la mondialisation.",
      "Giraud analyse les globalisations comme généralisation des "
      "compétitions."]),
'ch21-qcm-21': f(niv='raisonner', sp='c21-05', b=1712,
 exp="La courbe de l’éléphant permet de résoudre un paradoxe apparent : la "
     "mondialisation réduit les inégalités entre pays, grâce au rattrapage "
     "spectaculaire des classes moyennes émergentes, tout en renforçant "
     "certaines inégalités internes, les classes populaires des économies "
     "avancées voyant leurs revenus progresser très lentement tandis que les "
     "très hauts revenus mondiaux captent des gains importants.",
 why=["Elle montre précisément que toutes les inégalités ne diminuent pas.",
      "Les inégalités entre pays diminuent au contraire sur la période "
      "étudiée.",
      "Les effets distributifs sont massifs : l’absence d’effet est exclue."],
 diss="C’est la clé du retour politique du protectionnisme : des gains "
      "agrégés peuvent coexister avec des pertes concentrées sur certaines "
      "catégories sociales."),
'ch21-open-6': f(niv='connaitre', sp='c21-05', b=1406,
 exp="La malédiction des ressources désigne le paradoxe selon lequel "
     "l’abondance de matières premières peut ralentir la diversification et "
     "le développement au lieu de les favoriser. Le mécanisme principal est "
     "la maladie hollandaise : le boom des exportations de ressources fait "
     "apprécier la monnaie nationale, ce qui rend les autres secteurs "
     "exportateurs moins compétitifs, provoque le déclin de l’industrie et "
     "renforce la dépendance aux ressources. S’y ajoute la dépendance à des "
     "prix internationaux extrêmement volatils, qui rend la croissance "
     "instable puisque les recettes dépendent simultanément des cours "
     "mondiaux et des volumes exportés. Le cours relie enfin ce phénomène aux "
     "institutions : la rente peut nourrir des institutions extractives, au "
     "sens d’Acemoglu et Robinson, qui captent les ressources au bénéfice "
     "d’une minorité.",
 diss="Articulation complète : taux de change + volatilité + institutions — "
      "trois canaux, et non un seul."),
'ch21-open-7': f(niv='comprendre', sp='c21-05', b=1673,
 exp="La courbe de l’éléphant représente les gains de revenu par percentile "
     "mondial entre 1988 et 2008. Milanovic retient cette période car elle "
     "correspond à une phase d’intensification exceptionnelle de la "
     "mondialisation, comprise entre l’ouverture des économies anciennement "
     "socialistes et la rupture provoquée par la crise financière mondiale. "
     "Elle met en évidence trois groupes : de forts gains pour les classes "
     "moyennes des pays émergents, une quasi-stagnation pour les classes "
     "populaires des pays développés, et des gains élevés pour les très hauts "
     "revenus mondiaux. Elle permet ainsi de concilier réduction des "
     "inégalités entre pays et renforcement de certaines inégalités internes. "
     "Les classes populaires des économies avancées apparaissent comme des "
     "perdants relatifs : leur niveau de vie reste élevé à l’échelle mondiale "
     "mais progresse beaucoup moins vite, ce qui peut nourrir un sentiment de "
     "déclassement et un soutien politique au protectionnisme.",
 diss="Enchaînement politique à citer : mondialisation → gains inégalement "
      "répartis → déclassement → mécontentement → populisme → "
      "protectionnisme."),
'ch21-aut195-1': f(niv='connaitre', sp='c21-05', b=1531,
 exp="La croissance appauvrissante de Bhagwati désigne une hausse des "
     "exportations qui dégrade tellement les termes de l’échange que le "
     "bien-être du pays diminue. Lorsqu’un pays pèse lourd dans l’offre "
     "mondiale d’un produit à demande peu élastique, l’offre supplémentaire "
     "fait chuter le prix : la production augmente mais le bien-être baisse. "
     "L’analyse prolonge et radicalise celle de Prebisch.",
 why=["La question de la répartition interne des gains est un autre sujet.",
      "L’épuisement des ressources naturelles n’est pas le mécanisme en "
      "cause.",
      "L’endettement extérieur relève du financement, non des termes de "
      "l’échange."]),

# =============================================================== c21-06
'ch21-qcm-22': f(niv='connaitre', sp='c21-06', b=1757,
 exp="La balance des paiements recense tous les flux économiques et "
     "financiers entre résidents et non-résidents pendant une période "
     "donnée. Le critère n’est pas la nationalité mais le lieu principal "
     "d’activité économique : une entreprise étrangère implantée durablement "
     "en France peut être résidente française.",
 why=["Le budget de l’État est retracé par les comptes publics.",
      "Les prix à la consommation sont mesurés par l’indice des prix.",
      "La masse monétaire relève des statistiques monétaires de la banque "
      "centrale."]),
'ch21-qcm-23': f(niv='connaitre', sp='c21-06', b=1779,
 exp="Le compte des transactions courantes comprend quatre composantes : les "
     "biens, les services, les revenus primaires — rémunérations du travail "
     "et du capital entre résidents et non-résidents — et les revenus "
     "secondaires, c’est-à-dire des transferts sans contrepartie productive "
     "directe comme l’aide publique au développement.",
 why=["Les biens n’en sont qu’une composante : c’est précisément la "
      "confusion entre solde commercial et solde courant.",
      "Les capitaux relèvent du compte financier, le « bas » de la balance.",
      "L’or monétaire figure dans les avoirs de réserve, pas dans le compte "
      "courant."],
 diss="Exemple du cours : la France affiche un déficit commercial sur les "
      "biens (624 contre 682 Md€) mais un déficit courant limité, grâce à "
      "l’excédent des services et des revenus primaires."),
'ch21-qcm-24': f(niv='connaitre', sp='c21-06', b=1948,
 exp="Le compte financier, le « bas » de la balance, enregistre les "
     "mouvements de capitaux entre résidents et non-résidents : IDE, "
     "investissements de portefeuille, autres investissements et avoirs de "
     "réserve. Il distingue les avoirs — actifs détenus à l’étranger par les "
     "résidents — des engagements — actifs domestiques détenus par des "
     "non-résidents.",
 why=["Les échanges de biens figurent dans le compte courant.",
      "Les impôts relèvent des comptes publics, hors transferts "
      "internationaux.",
      "Les salaires versés entre résidents et non-résidents sont des revenus "
      "primaires, donc dans le compte courant."]),
'ch21-qcm-26': f(niv='comprendre', sp='c21-06', b=2031,
 exp="Un déficit courant signifie que la nation dépense davantage vis-à-vis "
     "du reste du monde qu’elle n’en reçoit : elle est en besoin de "
     "financement et doit donc attirer des entrées nettes de capitaux "
     "étrangers. Le haut et le bas de la balance des paiements se répondent "
     "nécessairement.",
 why=["La capacité de financement correspond au cas inverse, celui d’un "
      "excédent courant.",
      "Un excédent d’épargne produirait au contraire une capacité de "
      "financement.",
      "Une baisse des importations tendrait à réduire le déficit."]),
'ch21-qcm-27': f(niv='comprendre', sp='c21-06', b=2117,
 exp="Les déficits jumeaux désignent la coexistence d’un déficit budgétaire "
     "et d’un déficit courant. Le mécanisme passe par la demande intérieure : "
     "un déficit public soutient les revenus et la consommation, dont une "
     "partie se porte sur les importations, ce qui détériore le solde "
     "extérieur. L’identité X − M = (S − I) + (T − G) en donne la traduction "
     "comptable.",
 why=["Un déficit commercial et un excédent courant peuvent coexister, mais "
      "ce n’est pas ce que désigne l’expression.",
      "Inflation et chômage renvoient à la courbe de Phillips.",
      "Dette privée et dette publique sont des stocks, non des soldes "
      "annuels."],
 diss="Trois épisodes américains à citer : Reagan dans les années 1980 — "
      "déficit public atteignant 5 % du PIB en 1985 —, George W. Bush au "
      "début des années 2000, et les mandats de Trump, avec un déficit public "
      "autour de 6 % du PIB depuis 2022."),
'ch21-qcm-28': f(niv='comprendre', sp='c21-06', b=1764,
 exp="La balance des paiements est équilibrée par construction : comme tout "
     "document comptable, elle fonctionne en partie double, toute transaction "
     "réelle ou financière possédant une contrepartie. Une exportation de "
     "100 € s’accompagne de l’entrée d’un paiement de 100 €. Ce sont donc ses "
     "soldes internes — solde commercial, solde courant, compte financier — "
     "qui peuvent révéler des déséquilibres, et non son total.",
 why=["Son total ne peut être ni déficitaire ni excédentaire.",
      "Même remarque en sens inverse.",
      "Les mouvements de capitaux en sont au contraire une composante "
      "essentielle."]),
'ch21-vf-11': f(niv='comprendre', sp='c21-06', b=1814,
 exp="Le solde commercial ne porte que sur les biens, et parfois sur les "
     "biens et services ; le solde courant intègre en plus les revenus "
     "primaires et les revenus secondaires. La France l’illustre : son "
     "déficit sur les biens est important, mais ses excédents de services et "
     "de revenus primaires le compensent en grande partie, de sorte que son "
     "déficit courant reste limité.",
 diss="Même mécanisme à la grande échelle historique : l’Europe de la "
      "première mondialisation est déficitaire sur les biens mais "
      "excédentaire en courant grâce aux services et aux revenus de ses "
      "placements extérieurs."),
'ch21-open-8': f(niv='comprendre', sp='c21-06', b=1757,
 exp="La balance des paiements enregistre toutes les opérations entre "
     "résidents et non-résidents, le critère de résidence étant le lieu "
     "principal d’activité économique et non la nationalité. Son « haut », le "
     "compte des transactions courantes, regroupe les biens, les services, "
     "les revenus primaires et les revenus secondaires. Un compte de capital, "
     "quantitativement secondaire, enregistre certains transferts en capital. "
     "Son « bas », le compte financier, enregistre les mouvements de "
     "capitaux : IDE, investissements de portefeuille, autres investissements "
     "et avoirs de réserve, en distinguant les avoirs des engagements. "
     "L’ensemble est équilibré par construction, puisque le document "
     "fonctionne en partie double : un déficit courant a donc nécessairement "
     "une contrepartie dans le compte financier, sous forme d’entrées nettes "
     "de capitaux.",
 diss="Lecture à retenir : déficit courant = besoin de financement ; "
      "excédent courant = capacité de financement."),
'ch21-open-9': f(niv='raisonner', sp='c21-06', b=2087,
 exp="Cette identité se déduit de l’équilibre emplois-ressources en économie "
     "ouverte. Elle signifie que le solde extérieur est égal à la somme de la "
     "capacité de financement du secteur privé, (S − I), et du solde "
     "budgétaire public, (T − G). Un déficit extérieur traduit donc soit un "
     "investissement supérieur à l’épargne privée, soit un déficit public, "
     "soit les deux. Cette identité déplace l’analyse : le déficit commercial "
     "n’est pas seulement un problème de compétitivité, il renvoie aux "
     "comportements d’épargne et aux finances publiques. Elle éclaire "
     "directement le cas américain, où le déficit courant s’explique en "
     "grande partie par un déficit budgétaire élevé et par un investissement "
     "supérieur à l’épargne nationale — ce que la dénonciation d’une "
     "concurrence « déloyale » des partenaires laisse entièrement de côté.",
 diss="Argument très rentable : il permet de répondre à toute dissertation "
      "attribuant un déficit extérieur aux seuls comportements étrangers."),

# =============================================================== c21-07
'ch21-qcm-25': f(niv='connaitre', sp='c21-06', b=2087,
 exp="L’identité macroéconomique fondamentale s’écrit X − M = (S − I) + "
     "(T − G) : le solde extérieur est la somme du solde épargne-"
     "investissement privé et du solde public. Elle se déduit de l’équilibre "
     "emplois-ressources en économie ouverte et constitue l’outil central du "
     "chapitre pour analyser les déséquilibres extérieurs.",
 why=["X + M = C + I n’a aucune signification comptable.",
      "Y = C + S est l’affectation du revenu en économie fermée simplifiée, "
      "sans dimension extérieure.",
      "M = X + G ne correspond à aucune identité du cours."]),

# =============================================================== c21-08
'ch21-open-10': f(niv='raisonner', sp='c21-08', b=2707,
 exp="Non. Un déficit courant traduit un besoin de financement, mais sa "
     "portée dépend de son origine. Il peut être temporaire et parfaitement "
     "normal, par exemple après une hausse exceptionnelle de la facture "
     "énergétique. Il peut même révéler un dynamisme : un investissement "
     "supérieur à l’épargne domestique, financé par l’épargne étrangère, "
     "prépare une croissance future. C’est particulièrement vrai au début du "
     "développement : Nurkse montre que la faiblesse des revenus réduit "
     "l’épargne, donc l’investissement, donc les gains de productivité, et "
     "Rostow que le décollage suppose un fort taux d’investissement — la "
     "mobilité internationale des capitaux permet alors de dépasser cette "
     "contrainte. Un déficit devient préoccupant lorsqu’il finance de la "
     "consommation ou traduit une désindustrialisation, un problème de "
     "compétitivité ou une dépendance énergétique ; lorsqu’il repose sur des "
     "capitaux volatils susceptibles d’un sudden stop ; et lorsqu’il "
     "s’accompagne d’un endettement en devises, une dépréciation alourdissant "
     "alors mécaniquement la dette. La crise de la dette latino-américaine "
     "après le choc Volcker de 1979 en est l’illustration historique.",
 diss="La bonne question n’est donc pas « le pays est-il en déficit ? » mais "
      "« pourquoi est-il en déficit, et qui le finance ? »."),

# =============================================================== c21-10
'ch21-qcm-8': f(niv='connaitre', sp='c21-02', b=375,
 exp="La configuration globale de Michalet, qui s’impose à partir des années "
     "1980, se caractérise par la fragmentation internationale de la "
     "production et par l’unification des marchés financiers : les mouvements "
     "internationaux de capitaux explosent, les marchés deviennent plus "
     "intégrés et les investisseurs institutionnels prennent une place "
     "croissante.",
 why=["Le repli national caractérise l’entre-deux-guerres, non cette "
      "configuration.",
      "Les échanges atteignent au contraire des niveaux inédits.",
      "Le troc n’a rien à voir avec cette analyse."]),
'ch21-qcm-17': f(niv='connaitre', sp='c21-10', b=3567,
 exp="Une chaîne de valeur mondiale apparaît lorsque les différentes étapes "
     "de conception, de production, d’assemblage et de commercialisation d’un "
     "bien sont réparties entre plusieurs pays selon leurs avantages "
     "comparatifs. Elle a transformé la nature du commerce international, "
     "puisque les biens intermédiaires représentent désormais environ 36 % "
     "des échanges de biens.",
 why=["Une entreprise unique peut y participer, mais la chaîne implique "
      "plusieurs pays et souvent plusieurs firmes.",
      "Ce n’est pas un accord douanier mais une organisation productive.",
      "Ce n’est pas un indice boursier."],
 diss="Deux formes à distinguer : la chaîne « en araignée », où de nombreux "
      "composants convergent vers un pays d’assemblage, et la chaîne « en "
      "serpent », où le produit passe successivement d’un pays à l’autre."),
'ch21-qcm-29': f(niv='connaitre', sp='c21-10', b=3390,
 exp="Le taux d’ouverture mesure le poids des échanges extérieurs "
     "relativement à la richesse produite sur le territoire. Il se calcule "
     "souvent comme [(X + M) / 2] / PIB × 100. En 2025, le taux d’ouverture "
     "mondial est proche de 30 %, contre environ 15 % à la veille de 1914.",
 why=["Le taux de chômage rapporte les chômeurs à la population active.",
      "Le taux d’épargne rapporte l’épargne au revenu disponible.",
      "L’inflation importée est une transmission des prix extérieurs, non un "
      "indicateur d’ouverture."],
 diss="Deux limites à citer systématiquement : l’indicateur dépend de la "
      "taille du pays, et il compare des exportations en valeur brute à un "
      "PIB mesuré en valeur ajoutée."),
'ch21-qcm-30': f(niv='comprendre', sp='c21-10', b=3542,
 exp="Le commerce en valeur ajoutée corrige le double comptage lié au "
     "passage répété des biens intermédiaires aux frontières. Il attribue à "
     "chaque pays uniquement la part de valeur qu’il a effectivement créée. "
     "L’exemple de l’iPhone est parlant : un téléphone exporté à 1 000 "
     "dollars est comptabilisé pour 1 000 dollars dans les exportations "
     "chinoises alors que la valeur créée lors de l’assemblage n’en représente "
     "qu’une faible part.",
 why=["Les variations de change sont corrigées par d’autres méthodes.",
      "Il ne s’agit pas d’erreurs statistiques mais d’une convention de "
      "mesure.",
      "L’inflation est corrigée par les prix constants."],
 diss="Conséquence frappante : certains pays ateliers peuvent afficher un "
      "taux d’ouverture supérieur à 100 %."),
'ch21-qcm-40': f(niv='raisonner', sp='c21-10', b=3455,
 exp="La stagnation récente du taux d’ouverture traduit davantage un "
     "ralentissement de l’hypermondialisation qu’un retour massif à la "
     "fermeture des économies. Le taux reste proche de 30 %, soit environ le "
     "double du maximum atteint lors de la première mondialisation, et les "
     "chaînes de valeur demeurent : c’est la progression qui s’interrompt, "
     "non le niveau d’intégration.",
 why=["Une démondialisation certaine supposerait un recul marqué de "
      "l’ouverture, qui n’est pas observé.",
      "La hausse des droits de douane est un facteur possible, pas la "
      "signification de l’indicateur.",
      "Les chaînes de valeur cessent de s’allonger mais ne disparaissent "
      "pas."],
 diss="C’est le sens du mot slowbalization : ni poursuite de "
      "l’hypermondialisation, ni démondialisation, mais recomposition."),
'ch21-qcm-31': f(niv='comprendre', sp='c21-10', b=3479,
 exp="Le double comptage provient du passage répété des biens intermédiaires "
     "aux frontières : chaque franchissement est enregistré pour la valeur "
     "totale du bien, si bien que la même valeur est comptée plusieurs fois. "
     "Le problème se double d’une incohérence de mesure, puisque le taux "
     "d’ouverture compare des exportations en valeur brute à un PIB mesuré en "
     "valeur ajoutée.",
 why=["Les services financiers ne sont pas la source de ce biais.",
      "Les migrations n’entrent pas dans les statistiques commerciales.",
      "Les transferts publics figurent dans les revenus secondaires."]),
'ch21-open-11': f(niv='raisonner', sp='c21-10', b=3479,
 exp="Les statistiques traditionnelles comptent la valeur totale d’un bien à "
     "chaque passage de frontière. Avec la fragmentation des chaînes de "
     "valeur, les biens intermédiaires traversent plusieurs fois les "
     "frontières, ce qui produit un double comptage et surestime les flux. "
     "S’y ajoute une incohérence : le numérateur du taux d’ouverture est "
     "mesuré en valeur brute, le dénominateur en valeur ajoutée. L’exemple de "
     "l’iPhone l’illustre : le téléphone est comptabilisé pour la totalité de "
     "son prix dans les exportations chinoises alors que l’assemblage ne crée "
     "qu’une faible part de cette valeur. Le commerce en valeur ajoutée, "
     "mesuré à partir des tableaux entrées-sorties, ne retient que la valeur "
     "créée dans chaque pays : il modifie sensiblement les soldes bilatéraux, "
     "révèle les dépendances aux intrants étrangers et explique des évolutions "
     "surprenantes, comme la baisse du taux d’ouverture chinois depuis 2008, "
     "qui traduit en réalité une montée en gamme — la Chine produit désormais "
     "davantage d’intrants sur son propre territoire.",
 diss="Formule à retenir : les produits sont « made in world », ce que les "
      "statistiques brutes ne savent pas dire."),
'ch21-open-12': f(niv='raisonner', sp='c21-10', b=3620,
 exp="Une chaîne de valeur mondiale correspond à la fragmentation des étapes "
     "de production entre plusieurs pays, chacune localisée selon les "
     "conditions de coût, de compétence ou d’accès au marché. Elle procure "
     "des gains d’efficacité considérables, mais crée des vulnérabilités. La "
     "défaillance d’un seul maillon peut perturber l’ensemble de la chaîne. "
     "La dépendance porte sur des intrants parfois critiques, dont "
     "l’interruption d’approvisionnement peut arrêter des secteurs entiers. "
     "Elle touche aussi les services stratégiques, comme les infrastructures "
     "de paiement, ce qui pose une question de souveraineté. Elle rend enfin "
     "le protectionnisme plus complexe : taxer les intrants importés pénalise "
     "les producteurs nationaux eux-mêmes, qui sont devenus importateurs. "
     "C’est pourquoi les chaînes de valeur créent un arbitrage entre "
     "efficacité et résilience, aujourd’hui au cœur des stratégies de "
     "reshoring, nearshoring et friendshoring."),

# =============================================================== c21-13
'ch21-aut195-2': f(niv='connaitre', sp='c21-13', b=4748,
 exp="En 1791, Alexander Hamilton, premier secrétaire au Trésor américain, "
     "propose une taxe sur les importations pour protéger les producteurs "
     "américains de la concurrence britannique et financer l’industrie "
     "nationale. Hamilton précède List de cinquante ans : c’est List qui "
     "théorisera en 1841 le protectionnisme éducateur. Chez Hamilton, le "
     "tarif protège et finance simultanément l’industrialisation.",
 why=["Aucune banque centrale européenne n’est en cause en 1791.",
      "Il propose l’inverse : le maintien et le renforcement des droits de "
      "douane.",
      "Le protectionnisme éducateur est la formulation de List, en 1841."],
 diss="Les droits de douane ont une seconde justification, souvent oubliée : "
      "ils constituent une ressource fiscale importante pour les États du "
      "XIXᵉ siècle."),

# =============================================================== c21-14
'ch21-qcm-32': f(niv='connaitre', sp='c21-12', b=4074,
 exp="La première mondialisation, qui s’étend d’environ 1870 à 1913, "
     "s’achève en 1914 avec la Première Guerre mondiale. Celle-ci désorganise "
     "les flux commerciaux, financiers et migratoires et fragilise les "
     "puissances qui l’avaient portée ; la crise de 1929 transforme ensuite "
     "ce ralentissement en véritable effondrement.",
 why=["1870 marque le début conventionnel de la première mondialisation.",
      "1945 ouvre la phase de remondialisation progressive.",
      "1971 renvoie à la fin de la convertibilité du dollar en or, hors du "
      "champ de ce chapitre."]),
'ch21-qcm-34': f(niv='connaitre', sp='c21-14', b=4366,
 exp="Entre 1872 et 1914, près de 50 millions d’Européens émigrent, "
     "principalement vers les pays neufs et en particulier vers les "
     "États-Unis, qui en accueillent environ les deux tiers. Plus de 6 % de "
     "la population mondiale est concernée par une migration internationale "
     "sur la période.",
 why=["Les flux asiatiques vers l’Europe ne caractérisent pas cette "
      "période.",
      "Les migrations Afrique-Asie ne sont pas le mouvement dominant "
      "étudié.",
      "Le sens est inverse : ce sont les Européens qui partent."],
 diss="Point de comparaison décisif : en 2020, les migrants internationaux "
      "représentent environ 3,6 % de la population mondiale, soit une "
      "proportion inférieure à celle de la première mondialisation."),
'ch21-qcm-35': f(niv='comprendre', sp='c21-14', b=5086,
 exp="L’entre-deux-guerres se caractérise par le protectionnisme et "
     "l’effondrement des flux. Après 1929, l’escalade protectionniste — dont "
     "le tarif Hawley-Smoot de 1930 aux États-Unis est le symbole, avec des "
     "droits atteignant jusqu’à environ 300 % sur certains produits — divise "
     "le commerce mondial par environ trois entre 1929 et 1933. Les "
     "migrations ralentissent avec les quotas, et des dévaluations "
     "compétitives s’ajoutent à la guerre commerciale.",
 why=["L’ouverture record caractérise l’hypermondialisation, pas cette "
      "période.",
      "Les États-nations sont au contraire renforcés par le repli.",
      "L’OMC naît en 1995, le GATT en 1947."],
 diss="C’est la démonstration la plus nette de l’échec des stratégies non "
      "coopératives : en cherchant chacun à exporter sa crise, les États "
      "provoquent collectivement un effondrement des échanges."),
'ch21-qcm-36': f(niv='connaitre', sp='c21-14', b=5251,
 exp="Le basculement de puissance de l’entre-deux-guerres profite aux "
     "États-Unis, qui dominent déjà la production industrielle mondiale à la "
     "fin des années 1920 tout en restant une économie relativement peu "
     "internationalisée. Le cours souligne cependant un décalage : avant "
     "1945, les États-Unis disposent de la puissance économique sans exercer "
     "encore le leadership institutionnel et monétaire.",
 why=["L’Empire britannique est précisément affaibli par la guerre et le "
      "repli.",
      "La Chine n’émerge qu’à la fin du XXᵉ siècle.",
      "La Russie soviétique reste à l’écart de l’économie mondiale."],
 diss="C’est seulement après 1945 que les États-Unis transforment leur "
      "suprématie économique en leadership international, en organisant les "
      "règles de la nouvelle mondialisation."),
'ch21-qcm-41': f(niv='comprendre', sp='c21-02', b=628,
 exp="L’arsenalisation de la politique économique désigne l’usage des "
     "instruments économiques comme moyens de rapport de force : tarifs "
     "douaniers, sanctions, restrictions technologiques deviennent des armes "
     "de puissance. Elle traduit le retour du politique dans les relations "
     "commerciales, dans le cadre de la rivalité entre les États-Unis et la "
     "Chine.",
 why=["La hausse des dépenses militaires est une politique budgétaire, non "
      "l’usage de l’économie comme arme.",
      "La privatisation de l’armée n’a rien à voir avec cette notion.",
      "Une politique budgétaire expansive est un instrument de régulation de "
      "la demande."],
 diss="Nuance utile : la domination monétaire et financière américaine reste "
      "beaucoup moins contestée que sa domination industrielle et "
      "technologique, en raison du rôle central du dollar."),
'ch21-open-14': f(niv='raisonner', sp='c21-14', b=5087,
 exp="La première leçon est que l’ouverture internationale n’est jamais "
     "irréversible : elle dépend de choix politiques et d’un cadre "
     "institutionnel. La Première Guerre mondiale désorganise les flux, puis "
     "la crise de 1929 conduit les États à chercher des solutions nationales "
     "à un problème mondial. Chacun cherche à protéger son marché, à limiter "
     "ses importations et à gagner en compétitivité : le tarif Hawley-Smoot "
     "de 1930, les accords d’Ottawa de 1932 organisant la préférence "
     "impériale britannique, les contingentements et les dévaluations "
     "compétitives s’enchaînent. Le résultat est collectivement désastreux : "
     "le commerce mondial est divisé par environ trois entre 1929 et 1933, et "
     "la démondialisation touche simultanément les flux commerciaux, "
     "migratoires, financiers et monétaires. La seconde leçon est que les "
     "phases de repli redistribuent les positions dominantes : la suprématie "
     "européenne est profondément affaiblie et les États-Unis deviennent la "
     "première puissance productive.",
 diss="Leçon directement mobilisable aujourd’hui : l’interdépendance "
      "économique n’empêche pas les rivalités géopolitiques de l’emporter."),
'ch21-aut195-4': f(niv='comprendre', sp='c21-14', b=4946,
 exp="D’après les séries de Maddison, l’écart de niveau de vie entre les pays "
     "les plus riches et les plus pauvres passe d’un rapport d’environ 3 en "
     "1820 à environ 10 en 1913. C’est la Grande Divergence : la première "
     "mondialisation produit une convergence au sein de l’espace atlantique "
     "tout en accentuant la divergence avec les économies périphériques, "
     "maintenues dans des spécialisations primaires.",
 why=["Le sens de l’évolution est inversé : l’écart se creuse, il ne se "
      "réduit pas.",
      "L’écart est au contraire multiplié par plus de trois.",
      "La première mondialisation accentue la divergence mondiale, même si "
      "elle rapproche les économies atlantiques."],
 diss="Troisième leçon de la période : convergence atlantique et divergence "
      "mondiale sont simultanées, ce qui interdit toute lecture univoque de "
      "l’ouverture."),
'ch21-aut195-5': f(niv='raisonner', sp='c21-14', b=5060,
 exp="Suzanne Berger tire de la première mondialisation la leçon qu’une "
     "mondialisation peut échouer lorsque les tensions politiques deviennent "
     "dominantes. Ce sont « les leçons d’un échec oublié » : tensions "
     "géopolitiques, impérialisme, protectionnisme, guerres et crises font "
     "s’effondrer une intégration qui semblait profonde et durable.",
 why=["C’est précisément la thèse inverse de la sienne.",
      "Elle ne se prononce pas sur l’efficacité du protectionnisme en "
      "général.",
      "La convergence des salaires est observée mais n’a rien "
      "d’automatique : elle suppose la mobilité du travail."]),

# =============================================================== c21-17
'ch21-qcm-37': f(niv='comprendre', sp='c21-17', b=5802,
 exp="Par rapport à la première mondialisation, la mondialisation "
     "contemporaine est moins migratoire et beaucoup plus financière. Les "
     "migrants internationaux représentent environ 3,6 % de la population "
     "mondiale en 2020, contre plus de 6 % de la population concernée entre "
     "1872 et 1914. À l’inverse, les flux de capitaux explosent avec la "
     "libéralisation financière des années 1980-1990.",
 why=["Elle est au contraire proportionnellement moins migratoire.",
      "Les différences sont profondes, tant en nature qu’en ampleur.",
      "Elle est productive et financière autant que commerciale."],
 diss="Troisième différence majeure : la première mondialisation ne "
      "connaissait pas la fragmentation internationale des processus "
      "productifs."),
'ch21-open-13': f(niv='raisonner', sp='c21-17', b=6175,
 exp="La première mondialisation, jusqu’en 1914, repose sur la révolution "
     "des transports et des communications — selon Bairoch, le coût réel du "
     "transport est quasiment divisé par dix au XIXᵉ siècle — et sur des "
     "migrations massives : près de 50 millions d’Européens émigrent entre "
     "1872 et 1914, principalement vers les pays neufs. Ses capitaux sont "
     "surtout des investissements de portefeuille et des prêts, orientés du "
     "centre européen vers les périphéries : près de la moitié de l’épargne "
     "britannique est investie à l’étranger à la fin du siècle. La "
     "mondialisation contemporaine est nettement moins migratoire — environ "
     "3,6 % de la population mondiale en 2020 — mais beaucoup plus "
     "financière : les flux de capitaux atteignent une ampleur sans précédent "
     "et sont devenus multidirectionnels, les pays émergents étant désormais "
     "destinations majeures et investisseurs importants. Elle est surtout "
     "beaucoup plus productive, avec la fragmentation internationale des "
     "processus de production que la première ne connaissait pas : Baldwin "
     "parle d’un second dégroupage, qui sépare les étapes du processus "
     "productif lui-même, là où le premier séparait seulement le lieu de "
     "production du lieu de consommation.",
 diss="Le paradoxe de Lucas, formulé en 1990, prolonge la comparaison : les "
      "capitaux ne vont pas massivement des pays riches vers les pays "
      "pauvres, malgré une rentabilité théorique plus élevée."),

# =============================================================== c21-18
'ch21-qcm-38': f(niv='connaitre', sp='c21-18', b=6235,
 exp="La slowbalization désigne un ralentissement de la progression de "
     "l’ouverture : depuis 2008, le commerce mondial progresse à un rythme "
     "proche de celui du PIB, de sorte que le taux d’ouverture mondial stagne "
     "autour de 30 %. L’ouverture ne recule donc pas massivement, mais sa "
     "progression s’interrompt et les flux se recomposent.",
 why=["Un recul massif des échanges serait une véritable démondialisation, "
      "qui n’est pas observée.",
      "L’accélération caractérise l’hypermondialisation d’avant 2008.",
      "Il ne s’agit pas d’une crise monétaire."]),
'ch21-open-15': f(niv='raisonner', sp='c21-18', b=6316,
 exp="Il faut d’abord distinguer deux sens du mot démondialisation. Au sens "
     "factuel, il désigne les stratégies par lesquelles les États cherchent à "
     "limiter leur dépendance commerciale, productive ou financière. Au sens "
     "politique, c’est un projet volontaire de réorganisation de l’économie "
     "mondiale, défendu notamment par Walden Bello au début des années 2000. "
     "Les faits montrent surtout un ralentissement : depuis 2008, "
     "l’élasticité du commerce mondial au PIB s’est rapprochée de 1 et le "
     "taux d’ouverture stagne autour de 30 % — c’est la slowbalization. Ce "
     "ralentissement est partiellement conjoncturel, le commerce "
     "sur-réagissant aux récessions de 2008 et 2020, mais surtout structurel : "
     "transformation du modèle chinois, qui réinternalise sa production et "
     "monte en gamme avec Made in China 2025 ; raccourcissement des chaînes de "
     "valeur mondiales, dont le poids stagne depuis 2008 ; stratégies de "
     "reshoring, nearshoring et friendshoring ; résurgence d’un "
     "protectionnisme d’abord furtif — normes, subventions, contenu local — "
     "puis ouvertement tarifaire. Pourtant le commerce mondial résiste : il "
     "se recompose géographiquement plutôt qu’il ne s’effondre. La période "
     "relève donc moins d’une démondialisation que d’une reconfiguration, où "
     "la recherche du coût minimal cède du terrain à la sécurité économique, "
     "à la résilience et à la proximité géopolitique.",
 diss="Formule de conclusion : la mondialisation ne disparaît pas, elle "
      "change de critère d’organisation."),

}


# Les quinze questions ouvertes héritées n'avaient aucune grille de
# correction : le corrigé rédigé sert de réponse modèle et l'on explicite les
# éléments que la réponse doit contenir.
CLES = {
 'ch21-open-1': [
   {'f': ['commercial', 'biens et services'], 'l': 'l’ouverture commerciale'},
   {'f': ['productive', 'ide', 'migration', 'facteur'],
    'l': 'l’ouverture productive : IDE et migrations'},
   {'f': ['financiere', 'placement', 'devise', 'change'],
    'l': 'l’ouverture financière et monétaire'}],
 'ch21-open-2': [
   {'f': ['productive', 'controle', 'durable', '10'],
    'l': 'l’IDE : une logique productive et de contrôle durable'},
   {'f': ['placement', 'rendement', 'portefeuille'],
    'l': 'le portefeuille : une logique de placement'},
   {'f': ['mobilite', 'liquide', 'reversible', 'volatil'],
    'l': 'une mobilité très différente'}],
 'ch21-open-3': [
   {'f': ['internationale', 'commerce', 'etat'],
    'l': 'la configuration internationale, commerciale'},
   {'f': ['multinationale', 'ide', 'firme'],
    'l': 'la configuration multinationale, productive'},
   {'f': ['globale', 'financ', 'capitaux'],
    'l': 'la configuration globale, financière'},
   {'f': ['cumul', 'accumulation', 'ne remplacent pas', 'additionne'],
    'l': 'ces configurations se cumulent'}],
 'ch21-open-4': [
   {'f': ['cumul', 'trois dimension', 'addition'],
    'l': 'le cumul des trois dimensions'},
   {'f': ['sans precedent', 'inedit', 'double', '30'],
    'l': 'un degré d’ouverture sans précédent'},
   {'f': ['nombre croissant', 'nouveaux pays', 'mondiale', 'planetaire'],
    'l': 'l’intégration d’un nombre croissant de pays'}],
 'ch21-open-5': [
   {'f': ['terme de l echange', 'detérior', 'deterior', 'prix'],
    'l': 'la détérioration des termes de l’échange'},
   {'f': ['exporter davantage', 'meme volume', 'pouvoir d achat'],
    'l': 'exporter davantage pour importer autant'},
   {'f': ['centre', 'peripherie', 'colonis'],
    'l': 'la logique centre / périphérie'}],
 'ch21-open-6': [
   {'f': ['abondance', 'paradoxe', 'freine', 'ralenti'],
    'l': 'le paradoxe de l’abondance'},
   {'f': ['maladie hollandaise', 'taux de change', 'apprecia'],
    'l': 'le mécanisme du taux de change : la maladie hollandaise'},
   {'f': ['volatil', 'prix', 'instab'],
    'l': 'la volatilité des prix des matières premières'},
   {'f': ['institution', 'extractive', 'rente'],
    'l': 'la rente et les institutions extractives'}],
 'ch21-open-7': [
   {'f': ['1988', '2008', 'percentile'],
    'l': 'la période 1988-2008 et la distribution mondiale des revenus'},
   {'f': ['classe moyenne', 'emergent'],
    'l': 'de forts gains pour les classes moyennes émergentes'},
   {'f': ['classe populaire', 'stagnation', 'pays developpe', 'avance'],
    'l': 'la quasi-stagnation des classes populaires des pays développés'},
   {'f': ['haut revenu', 'plus riche', '1 %'],
    'l': 'des gains élevés pour les très hauts revenus'}],
 'ch21-open-8': [
   {'f': ['resident', 'non resident'],
    'l': 'les opérations entre résidents et non-résidents'},
   {'f': ['courant', 'bien', 'service', 'revenu'],
    'l': 'le compte courant et ses composantes'},
   {'f': ['financier', 'capitaux'], 'l': 'le compte financier'},
   {'f': ['equilibre', 'partie double', 'contrepartie'],
    'l': 'un document équilibré par construction'}],
 'ch21-open-9': [
   {'f': ['epargne', 's i', 'investissement'],
    'l': 'le solde épargne-investissement privé'},
   {'f': ['solde public', 't g', 'budget'],
    'l': 'le solde public'},
   {'f': ['pas seulement', 'competitivite', 'deplace'],
    'l': 'le déficit n’est pas seulement un problème de compétitivité'}],
 'ch21-open-10': [
   {'f': ['besoin de financement'],
    'l': 'un déficit traduit un besoin de financement'},
   {'f': ['investissement productif', 'nurkse', 'rostow', 'take off'],
    'l': 'il peut financer un investissement productif'},
   {'f': ['consommation', 'desindustrialisation', 'competitivite'],
    'l': 'il est préoccupant s’il finance la consommation ou traduit une désindustrialisation'},
   {'f': ['volatil', 'sudden stop', 'devise', 'soutenab'],
    'l': 'la nature du financement : capitaux volatils, dette en devises'}],
 'ch21-open-11': [
   {'f': ['double comptage', 'plusieurs fois', 'repet'],
    'l': 'le double comptage des biens intermédiaires'},
   {'f': ['brute', 'valeur ajoutee', 'numerateur'],
    'l': 'valeur brute contre valeur ajoutée'},
   {'f': ['iphone', 'atelier', 'assemblage'],
    'l': 'l’exemple de l’iPhone et des pays ateliers'},
   {'f': ['solde bilateral', 'dependance', 'intrant'],
    'l': 'une mesure qui modifie les soldes et révèle les dépendances'}],
 'ch21-open-12': [
   {'f': ['fragmentation', 'etape', 'plusieurs pays'],
    'l': 'la fragmentation des étapes entre plusieurs pays'},
   {'f': ['efficacite', 'cout', 'gain'],
    'l': 'des gains d’efficacité'},
   {'f': ['rupture', 'maillon', 'critique', 'approvisionnement'],
    'l': 'les ruptures d’approvisionnement et les intrants critiques'},
   {'f': ['relocalisation', 'reshoring', 'resilience', 'souverainete'],
    'l': 'les débats sur la relocalisation et la résilience'}],
 'ch21-open-13': [
   {'f': ['transport', 'bairoch', 'communication'],
    'l': 'la révolution des transports et des communications'},
   {'f': ['migration', '50 millions', 'migratoire'],
    'l': 'des migrations massives, aujourd’hui proportionnellement moindres'},
   {'f': ['financ', 'capitaux', 'portefeuille'],
    'l': 'une mondialisation contemporaine beaucoup plus financière'},
   {'f': ['dipp', 'fragmentation', 'baldwin', 'degroupage'],
    'l': 'la fragmentation productive, absente de la première mondialisation'}],
 'ch21-open-14': [
   {'f': ['protectionnisme', 'hawley', 'droit de douane'],
    'l': 'la montée du protectionnisme'},
   {'f': ['effondrement', 'divis', 'trois', 'chute'],
    'l': 'l’effondrement des flux'},
   {'f': ['pas irreversible', 'reversib', 'choix politique', 'institutionnel'],
    'l': 'l’ouverture n’est jamais irréversible'},
   {'f': ['etats unis', 'basculement', 'puissance'],
    'l': 'le basculement de puissance vers les États-Unis'}],
 'ch21-open-15': [
   {'f': ['slowbalization', 'ralenti', 'stagn'],
    'l': 'un ralentissement : la slowbalization'},
   {'f': ['factuel', 'projet', 'politique', 'bello'],
    'l': 'deux sens du mot démondialisation'},
   {'f': ['chine', 'chaine de valeur', 'reshoring', 'protectionnisme'],
    'l': 'des causes structurelles : Chine, chaînes de valeur, protectionnisme'},
   {'f': ['recompos', 'regional', 'securite', 'fragmentation'],
    'l': 'une recomposition plutôt qu’une démondialisation'}],
}

for _id, _c in CLES.items():
    FIX[_id]['ans'] = {'modele': FIX[_id]['exp'], 'cles': _c}


from qz21n1 import L as _N1
from qz21n2 import L as _N2
from qz21n3 import L as _N3
from qz21n4 import L as _N4
from qz21n5 import L as _N5

NEW = _N1 + _N2 + _N3 + _N4 + _N5
