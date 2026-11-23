# -*- coding: utf-8 -*-
"""Chapitre 22 — corrections des questions héritées, sous-parties c22-01 à c22-09."""


def f(**kw):
    return kw


FIX = {

# =============================================================== c22-01
'ch22-qcm-7': f(niv='connaitre', sp='c22-01', b=108,
 exp="Richard Baldwin théorise en 2006 les « unbundlings », ou dégroupages "
     "successifs de la mondialisation. La DIPP correspond à la fragmentation "
     "internationale du processus productif : chaque étape de production est "
     "localisée dans le territoire offrant les conditions les plus "
     "avantageuses pour cette tâche. L’économie mondiale passe ainsi d’un "
     "commerce de biens à un véritable commerce de tâches.",
 why=["Michael Porter analyse la firme globale dans Competition in Global "
      "Industries (1986).",
      "Robert Reich décrit la firme réseau dans The Work of Nations (1991).",
      "Stan Shih est l’auteur de la courbe du sourire."]),
'ch22-qcm-8': f(niv='comprendre', sp='c22-01', b=112,
 exp="La « grande convergence » que Baldwin développe en 2016 repose sur un "
     "mécanisme précis : la fragmentation productive permet d’entrer dans une "
     "chaîne de valeur en maîtrisant une seule tâche, sans devoir maîtriser "
     "l’ensemble d’une industrie. L’industrialisation devient donc plus "
     "accessible aux pays en développement, ce qui réduit certains écarts "
     "avec les pays avancés — à condition toutefois de parvenir ensuite à "
     "monter en gamme.",
 why=["La convergence décrite concerne précisément l’écart entre pays "
      "développés et pays émergents.",
      "Aucune égalisation des salaires mondiaux n’est en cause : les écarts "
      "demeurent considérables.",
      "Les taux de change ne sont pas l’objet de cette analyse."],
 diss="Enchaînement à retenir : fragmentation productive → une seule tâche "
      "suffit → industrialisation plus accessible → rattrapage possible."),
'ch22-qcm-11': f(niv='comprendre', sp='c22-01', b=49,
 exp="Coase montre dès 1937 que l’existence et la taille de la firme "
     "s’expliquent par un arbitrage : d’un côté les coûts de transaction liés "
     "au recours au marché — recherche d’information, négociation, rédaction "
     "et contrôle des contrats —, de l’autre les coûts d’organisation liés à "
     "l’internalisation de la production. La frontière de la firme se situe "
     "là où ces deux coûts s’équilibrent.",
 why=["L’État n’impose pas l’existence des entreprises : Coase explique leur "
      "émergence spontanée.",
      "Les préférences des salariés ne sont pas le ressort de cet "
      "arbitrage.",
      "Les rendements croissants expliquent la taille des unités de "
      "production, non l’existence de la firme comme mode de coordination."],
 diss="Cet arbitrage structure tout le chapitre : « faire », « faire faire » "
      "ou « faire à l’étranger »."),
'ch22-qcm-12': f(niv='comprendre', sp='c22-01', b=57,
 exp="La shareholder value place la maximisation de la valeur actionnariale "
     "au centre de la gestion de l’entreprise ; la montée de cette conception "
     "avec la globalisation financière peut opposer la rentabilité financière "
     "de court terme aux investissements industriels et technologiques "
     "nécessaires à la compétitivité de long terme. Le passage à la "
     "stakeholder value élargit la responsabilité de l’entreprise aux "
     "salariés, aux fournisseurs, aux territoires et à l’environnement.",
 why=["Maximiser la valeur actionnariale est précisément la logique "
      "antérieure, celle de la shareholder value.",
      "Le mode de financement n’est pas en cause dans cette opposition.",
      "Il n’est pas question d’un retrait des marchés étrangers."]),
'ch22-qcm-31': f(niv='connaitre', sp='c22-01', b=184,
 exp="Dans La Séduction des nations (1999), Charles-Albert Michalet montre "
     "que la mondialisation met les États en concurrence pour attirer les "
     "investissements des firmes multinationales : les États développent des "
     "politiques d’attractivité, c’est-à-dire qu’ils cherchent à « séduire » "
     "les firmes plutôt qu’à les contraindre.",
 why=["Baldwin théorise les dégroupages de la mondialisation.",
      "Reich décrit la firme réseau.",
      "Porter analyse la firme globale."],
 diss="Image très citable : ce ne sont plus les firmes qui demandent "
      "l’autorisation de s’implanter, ce sont les États qui les courtisent."),
'ch22-questi-80': f(niv='raisonner', sp='c22-01', b=80,
 exp="La relation est ambiguë. Les FMN disposent de la mobilité : elles "
     "mettent les territoires en concurrence, ce qui peut pousser certains "
     "États au moins-disant fiscal ou social, et elles pratiquent "
     "l’optimisation fiscale, notamment par les prix de transfert. Mais les "
     "États conservent de puissants instruments : le filtrage des IDE, dont "
     "le nombre de régimes est passé de 21 économies en 2016 à 52 en 2025 ; la "
     "réglementation et les normes ; la taxation et la coordination fiscale "
     "internationale ; les droits de douane, qui peuvent inciter à produire "
     "sur place par tariff jumping ; les aides conditionnelles et la "
     "politique industrielle. Il ne s’agit donc pas d’une opposition mais "
     "d’une relation de coopération, de dépendance et de rapport de force "
     "variable selon les secteurs et les périodes.",
 diss="Formule d’équilibre : les États cherchent à attirer les FMN tout en "
      "tentant de préserver leur autonomie économique."),

# =============================================================== c22-02
'ch22-qcm-1': f(niv='connaitre', sp='c22-02', b=478,
 exp="Selon la définition reprise de la CNUCED, une entreprise est "
     "multinationale lorsqu’elle exerce un contrôle direct ou indirect sur "
     "des actifs ou des entreprises situés dans plusieurs pays. Exporter ne "
     "suffit donc pas : la multinationalisation suppose de produire ou de "
     "contrôler une activité productive dans au moins deux territoires "
     "différents.",
 why=["Exporter vers plusieurs pays relève du commerce international, non de "
      "la multinationalisation.",
      "Avoir des clients étrangers est le résultat de l’exportation.",
      "La cotation sur plusieurs places financières concerne le financement, "
      "pas le contrôle d’activités productives."]),
'ch22-qcm-2': f(niv='comprendre', sp='c22-02', b=616,
 exp="L’IDE horizontal consiste à reproduire à l’étranger une activité "
     "productive que la firme réalisait déjà dans son pays d’origine, afin de "
     "se rapprocher du consommateur et de réduire les coûts liés à la "
     "distance ou aux barrières commerciales. Il relève donc d’une logique de "
     "marché, et il se substitue partiellement aux exportations depuis le "
     "pays d’origine.",
 why=["Fragmenter la chaîne de valeur selon les coûts correspond à l’IDE "
      "vertical.",
      "Racheter un concurrent national n’est pas un investissement "
      "international.",
      "Placer des capitaux sans prise de contrôle est un investissement de "
      "portefeuille."]),
'ch22-qcm-4': f(niv='connaitre', sp='c22-02', b=496,
 exp="Au-delà de 50 % du capital, la société mère est actionnaire "
     "majoritaire et contrôle directement l’entreprise : on parle alors de "
     "filiale. Entre 10 % et 50 %, la participation est importante sans être "
     "majoritaire : on parle de société affiliée. En dessous de 10 %, "
     "l’objectif est considéré comme principalement financier.",
 why=["Au-delà de 10 % seulement, on parle de société affiliée : le contrôle "
      "n’est pas majoritaire.",
      "25 % ne constitue pas le seuil retenu par la comptabilité "
      "internationale.",
      "Une détention de 100 % est un cas particulier de filiale, non la "
      "définition du seuil."]),
'ch22-qcm-5': f(niv='connaitre', sp='c22-02', b=513,
 exp="En dessous d’environ 10 % du capital, l’investisseur n’est pas "
     "considéré comme cherchant à exercer une influence durable sur "
     "l’entreprise : il s’agit d’un placement financier, donc d’un "
     "investissement de portefeuille. C’est la volonté de contrôle qui "
     "distingue l’IDE du simple placement.",
 why=["Une filiale suppose une détention majoritaire, supérieure à 50 %.",
      "Une société affiliée correspond à une participation comprise entre "
      "10 % et 50 %.",
      "Un investissement greenfield est une forme d’IDE : la création d’une "
      "unité ex nihilo."]),
'ch22-qcm-13': f(niv='comprendre', sp='c22-02', b=559,
 exp="Le devoir de vigilance repose sur l’idée que la FMN est donneuse "
     "d’ordres et donc responsable : externaliser la production ne signifie "
     "pas externaliser la responsabilité. Elle doit vérifier que ses "
     "fournisseurs respectent des standards minimaux de sécurité, de "
     "conditions de travail, de droits fondamentaux et d’environnement. "
     "L’effondrement du Rana Plaza au Bangladesh en 2013 a joué un rôle "
     "décisif dans cette prise de conscience.",
 why=["La FMN n’est justement pas propriétaire de l’usine de son "
      "fournisseur : c’est précisément ce qui soulève la question.",
      "L’exonération de responsabilité est l’argument que le devoir de "
      "vigilance écarte.",
      "La qualifier de simple intermédiaire reviendrait à nier son pouvoir "
      "de donneuse d’ordres."]),
'ch22-qcm-43': f(niv='comprendre', sp='c22-02', b=1253,
 exp="Le filtrage des IDE permet à l’État de déterminer quels investissements "
     "sont compatibles avec ses intérêts stratégiques, en contrôlant leur "
     "origine et leur destination sectorielle. Sa diffusion est "
     "spectaculaire : 21 économies disposaient d’un régime de filtrage en "
     "2016, contre 52 en 2025. C’est l’un des instruments par lesquels le "
     "rapport de force peut s’inverser au profit de l’État.",
 why=["Le filtrage restreint certains investissements : il ne vise pas à en "
      "attirer davantage.",
      "La fiscalité est un autre instrument, celui de l’attractivité.",
      "Les subventions à l’exportation relèvent de la politique commerciale."],
 diss="Signe très net du retour de la souveraineté économique : les États ne "
      "cherchent plus seulement à attirer les capitaux, ils veulent les "
      "choisir."),
'ch22-qcm-44': f(niv='comprendre', sp='c22-02', b=311,
 exp="La transition vers le véhicule électrique ne constitue pas seulement un "
     "changement de motorisation : elle transforme la chaîne de valeur "
     "automobile en faisant de la batterie l’actif technologique et "
     "stratégique central. Or environ trois quarts de la production mondiale "
     "de batteries sont assurés par la Chine, CATL en étant le premier "
     "producteur mondial : la dépendance technologique devient donc une "
     "dépendance industrielle puis géopolitique.",
 why=["Le moteur thermique est précisément la technologie que la transition "
      "rend secondaire.",
      "La carrosserie reste une compétence largement maîtrisée par les "
      "constructeurs européens.",
      "Le réseau de concessions est un actif commercial, non technologique."]),
'ch22-qcm-45': f(niv='appliquer', sp='c22-02', b=322,
 exp="La réussite de BYD repose en partie sur une stratégie d’intégration "
     "verticale : l’entreprise maîtrise la technologie centrale de la "
     "batterie avant d’étendre cette compétence à l’automobile électrique, ce "
     "qui lui permet de sécuriser ses approvisionnements et de contrôler "
     "plusieurs maillons successifs de la chaîne de valeur.",
 why=["L’externalisation complète est la stratégie inverse : BYD internalise "
      "au contraire la technologie clé.",
      "Une logique de portefeuille serait purement financière, sans contrôle "
      "productif.",
      "La franchise internationale est un mode de distribution, non une "
      "stratégie industrielle."],
 diss="Illustration contemporaine de la concentration verticale : maîtriser "
      "la technologie critique avant d’aborder le produit final."),
'ch22-vraifa-65': f(niv='connaitre', sp='c22-02', b=324,
 exp="Environ trois quarts de la production mondiale de batteries pour "
     "véhicules électriques sont assurés par la Chine, CATL étant le premier "
     "producteur mondial et BYD ayant bâti sa position automobile sur cette "
     "même technologie. Produire un véhicule électrique en Europe nécessite "
     "donc encore souvent des composants ou des batteries chinois, ce qui "
     "transforme une dépendance industrielle en enjeu de souveraineté.",
 diss="Conséquence remarquable : le sens des transferts de technologie "
      "s’inverse, les groupes occidentaux cherchant désormais à accéder à "
      "certaines technologies chinoises."),
'ch22-questi-77': f(niv='comprendre', sp='c22-02', b=294,
 exp="Parce que la transition vers le véhicule électrique ne change pas "
     "seulement la motorisation : elle déplace la valeur vers la batterie, "
     "qui devient l’actif technologique central de la chaîne de valeur "
     "automobile. Or la Chine domine la production mondiale de batteries, "
     "avec environ trois quarts de la production et CATL comme premier "
     "producteur mondial, tandis que BYD a construit sa position automobile "
     "sur cette technologie par intégration verticale. Il en résulte une "
     "dépendance européenne qui justifie le retour de l’État dans la filière, "
     "par des aides publiques et des projets comme l’exploitation du lithium "
     "de l’Allier. Le problème principal est le temps : l’investissement "
     "industriel européen s’étale jusqu’en 2030 alors que la Chine continue "
     "de produire et de conserver son avance.",
 diss="Chiffre frappant : environ 60 véhicules électriques chinois sur 100 "
      "vendus dans le monde, alors que les véhicules directement importés de "
      "Chine restent minoritaires en France."),
'ch22-questi-78': f(niv='connaitre', sp='c22-02', b=559,
 exp="Le devoir de vigilance répond à la question de savoir si une FMN peut "
     "se dire non responsable des conditions de production parce qu’elle "
     "n’est pas propriétaire de l’usine. La fragmentation internationale de "
     "la production oblige en effet à repenser la responsabilité : "
     "l’effondrement du Rana Plaza au Bangladesh en 2013 a montré que le "
     "recours à la sous-traitance n’exonère pas des conséquences sociales ou "
     "environnementales des chaînes d’approvisionnement. Considérée comme "
     "donneuse d’ordres, la FMN doit donc vérifier que ses fournisseurs "
     "respectent des standards minimaux de sécurité, de conditions de "
     "travail, de droits fondamentaux et d’environnement."),

# =============================================================== c22-03
'ch22-qcm-3': f(niv='comprendre', sp='c22-03', b=642,
 exp="L’IDE vertical fragmente la chaîne de valeur en localisant chaque tâche "
     "dans le pays où les conditions de production sont les plus "
     "avantageuses : matière première dans un pays, composants dans un "
     "deuxième, assemblage dans un troisième, services dans un quatrième. "
     "C’est le cœur de la DIPP, et il relève d’une logique de rationalisation "
     "et non de marché.",
 why=["Le rapprochement du consommateur caractérise l’IDE horizontal.",
      "La diversification financière relève de l’investissement de "
      "portefeuille.",
      "La protection réglementaire renvoie plutôt au tariff jumping, qui est "
      "une logique horizontale."]),
'ch22-qcm-9': f(niv='comprendre', sp='c22-03', b=839,
 exp="La courbe du sourire de Stan Shih montre que la valeur ajoutée est "
     "forte en amont et en aval mais faible au centre : la conception et la "
     "R&D en amont, le marketing, la marque et les services en aval captent "
     "l’essentiel de la valeur, tandis que l’assemblage, situé au creux de la "
     "courbe, en crée le moins. Baldwin montre de plus que ce sourire s’est "
     "creusé entre les années 1970 et les années 2000.",
 why=["L’assemblage est au contraire l’étape la moins créatrice de valeur.",
      "La valeur n’est pas constante : c’est précisément la forme de la "
      "courbe qui l’indique.",
      "Elle n’est pas décroissante de l’amont vers l’aval, puisque l’aval est "
      "lui aussi très rémunérateur."],
 diss="Explication du creusement : la valeur des services immatériels "
      "augmente, tandis que la multiplication des pays capables d’assembler "
      "fait baisser la rémunération de cette tâche."),
'ch22-qcm-10': f(niv='connaitre', sp='c22-03', b=772,
 exp="Dans The Work of Nations (1991), Robert Reich décrit la firme réseau : "
     "la grande entreprise devient le centre organisateur d’un vaste réseau "
     "mondial de filiales et de partenaires spécialisés, chaque tâche étant "
     "localisée selon les avantages comparatifs des différents territoires. "
     "La spécialisation internationale des tâches réduit les coûts et "
     "augmente la productivité.",
 why=["Le « nœud de contrats » est la formule d’Alchian et Demsetz, dans "
      "l’approche contractuelle de la firme.",
      "Le monopole naturel est une structure de marché liée à des coûts fixes "
      "élevés.",
      "La bureaucratie est le modèle d’organisation analysé par Weber."]),
'ch22-qcm-14': f(niv='comprendre', sp='c22-03', b=918,
 exp="L’INSEE mesure le « Made in France » comme la part de valeur ajoutée "
     "française contenue dans la demande intérieure finale française : sur "
     "100 € de consommation en France, quelle fraction a réellement été "
     "produite sur le territoire ? En 2019, environ 78 % de la valeur de la "
     "demande intérieure finale est domestique, principalement grâce au poids "
     "des services.",
 why=["La nationalité des entreprises ne dit rien du lieu de création de la "
      "valeur.",
      "Le solde commercial mesure un écart entre exportations et "
      "importations.",
      "Le nombre d’usines ne mesure ni la valeur produite ni sa part dans la "
      "consommation."],
 diss="Contraste décisif : si l’on isole les produits manufacturés, le "
      "contenu français passe d’environ 82 % à 38 % entre 1965 et 2019."),
'ch22-questi-66': f(niv='comprendre', sp='c22-03', b=616,
 exp="L’IDE horizontal reproduit à l’étranger le processus productif de la "
     "maison mère : il relève d’une logique de marché, qui consiste à se "
     "rapprocher du consommateur et à réduire les coûts liés à la distance ou "
     "aux barrières commerciales. Il tend donc à se substituer aux "
     "exportations depuis le pays d’origine ; les IDE américains vers "
     "l’Europe des années 1950-1960, après le traité de Rome, en sont "
     "l’exemple. L’IDE vertical fragmente au contraire la chaîne de valeur en "
     "localisant chaque tâche là où les conditions de production sont les "
     "plus avantageuses, dans une logique de rationalisation : matière "
     "première dans un pays, composants dans un autre, assemblage dans un "
     "troisième. Il constitue le cœur de la DIPP et donne naissance aux "
     "filiales-ateliers caractéristiques de l’hypermondialisation."),
'ch22-questi-79': f(niv='comprendre', sp='c22-03', b=905,
 exp="L’INSEE définit le « Made in France » comme la part de valeur ajoutée "
     "française contenue dans la demande intérieure finale française : sur "
     "100 € dépensés en France, quelle fraction correspond à de la valeur "
     "créée sur le territoire ? Cette mesure est nécessaire car, avec la "
     "fragmentation des chaînes de valeur, le lieu d’assemblage ne suffit plus "
     "à identifier l’origine réelle de la valeur créée. Les résultats sont "
     "instructifs : en 2019, environ 78 % de la valeur de la demande "
     "intérieure finale est domestique, essentiellement grâce au poids des "
     "services, qui supposent une proximité directe avec le consommateur. "
     "Mais si l’on isole les produits manufacturés, le contenu français "
     "s’effondre, passant d’environ 82 % en 1965 à 38 % en 2019 : c’est "
     "l’effet direct de la DIPP et des délocalisations.",
 diss="La mondialisation de l’actionnariat brouille d’ailleurs aussi la "
      "nationalité des entreprises elles-mêmes : siège, capital, production, "
      "salariés et chiffre d’affaires peuvent être répartis entre de nombreux "
      "territoires."),

# =============================================================== c22-04
'ch22-qcm-15': f(niv='connaitre', sp='c22-04', b=1371,
 exp="Au sens strict, le dumping désigne une pratique consistant à vendre un "
     "produit à l’étranger à un prix inférieur à celui pratiqué sur le marché "
     "intérieur. L’exemple du cours est une voiture vendue 30 000 € sur son "
     "marché national et 22 000 € à l’exportation. Si cette différence résulte "
     "d’un soutien destiné à favoriser artificiellement l’exportation, elle "
     "procure un avantage artificiel à l’exportateur.",
 why=["Vendre en dessous du coût de production relève plutôt des prix "
      "prédateurs.",
      "L’exonération de droits de douane est une question de politique "
      "commerciale, non de prix.",
      "La subvention peut être le moyen du dumping, mais la définition porte "
      "sur l’écart de prix."],
 diss="Enjeu juridique : l’OMC autorise, dans certaines situations, un pays "
      "victime de dumping à appliquer des mesures antidumping."),
'ch22-qcm-16': f(niv='comprendre', sp='c22-04', b=1392,
 exp="Le dumping monétaire consiste à maintenir le taux de change "
     "artificiellement faible. Une monnaie sous-évaluée rend les exportations "
     "moins chères et les importations plus chères, ce qui améliore "
     "mécaniquement la compétitivité-prix des producteurs nationaux et "
     "l’attractivité du territoire pour les investisseurs étrangers.",
 why=["Subventionner les exportations est une autre pratique, relevant du "
      "dumping au sens strict.",
      "La baisse des salaires correspond au dumping social.",
      "La réduction des normes environnementales correspond au dumping "
      "environnemental."],
 diss="Les quatre formes élargies à connaître : monétaire, social, fiscal et "
      "environnemental — toutes posent la même difficulté, distinguer "
      "l’avantage volontairement entretenu du simple écart de développement."),
'ch22-qcm-17': f(niv='connaitre', sp='c22-04', b=1534,
 exp="L’Organe de règlement des différends de l’OMC vise à substituer une "
     "procédure multilatérale de règlement des litiges aux représailles "
     "commerciales unilatérales entre États. Son affaiblissement favorise "
     "précisément le retour de politiques commerciales unilatérales, les "
     "États étant moins incités à attendre une solution multilatérale.",
 why=["Le FMI intervient sur les déséquilibres de balance des paiements et "
      "les crises financières.",
      "La Banque mondiale finance le développement.",
      "L’OCDE produit des analyses et coordonne, notamment en matière "
      "fiscale, mais ne tranche pas les litiges commerciaux."]),
'ch22-qcm-18': f(niv='raisonner', sp='c22-04', b=1590,
 exp="La désindustrialisation est un phénomène multicausal. Quatre grandes "
     "explications se combinent : l’externalisation des services, qui produit "
     "une désindustrialisation en partie statistique ; le progrès technique, "
     "dont les gains de productivité permettent de produire davantage avec "
     "moins de travailleurs ; la tertiarisation de la demande, selon la loi "
     "d’Engel et le déversement de Fourastié ; et la concurrence "
     "internationale. Les délocalisations ne sont donc qu’un facteur parmi "
     "d’autres, et leur ampleur mesurée est limitée.",
 why=["Les délocalisations seules ne suffisent pas : le rapport Gallois de "
      "2012 les estime à environ un quart des pertes d’emplois industriels.",
      "La fiscalité peut jouer sur la compétitivité mais n’explique pas le "
      "mouvement de long terme.",
      "La démographie n’est pas invoquée par le cours pour expliquer le "
      "recul industriel."],
 diss="Position équilibrée à défendre : la mondialisation est une cause de "
      "désindustrialisation, mais elle n’en constitue pas la cause "
      "principale."),

# =============================================================== c22-05
'ch22-qcm-19': f(niv='connaitre', sp='c22-05', b=1687,
 exp="Dans Le Grand Espoir du XXᵉ siècle (1949), Fourastié décrit le "
     "déversement sectoriel : les gains de productivité réalisés dans "
     "l’agriculture puis dans l’industrie rendent la production moins "
     "coûteuse, font baisser les prix réels et augmentent les revenus réels, "
     "ce qui accroît la demande de services. Travail et revenu se déversent "
     "donc progressivement vers le secteur tertiaire.",
 why=["Colin Clark est associé à la distinction des trois secteurs, non au "
      "mécanisme de déversement tel que le présente ce cours.",
      "Kuznets est connu pour ses travaux sur la croissance et les "
      "inégalités.",
      "Sauvy a popularisé d’autres analyses, notamment démographiques."],
 diss="À combiner avec la loi d’Engel : quand le revenu augmente, la part du "
      "budget consacrée à l’alimentation diminue au profit des loisirs, de la "
      "santé, de l’éducation et des services."),
'ch22-questi-68': f(niv='raisonner', sp='c22-05', b=1918,
 exp="Les études empiriques montrent que l’ampleur mesurée des délocalisations "
     "reste limitée. Le cours donne des ordres de grandeur précis : environ "
     "980 délocalisations entre 1995 et 2005 contre environ 730 entre 2010 et "
     "2017 ; environ 34 000 emplois perdus par an entre 2001 et 2010, avec un "
     "pic d’environ 56 000 en 2008, contre environ 14 000 par an ensuite ; et "
     "le rapport Gallois de 2012 estime les délocalisations à environ un quart "
     "des pertes d’emplois industriels. Une part importante se dirige "
     "d’ailleurs vers d’autres économies européennes, et non vers les pays à "
     "très bas salaires. Trois autres mécanismes pèsent davantage : le progrès "
     "technique, dont les gains de productivité réduisent l’emploi nécessaire ; "
     "la transformation de la demande, avec la loi d’Engel et le déversement "
     "de Fourastié ; et l’externalisation d’activités de services auparavant "
     "comptées dans l’industrie. Krugman soutient dès les années 1990 que « la "
     "mondialisation n’est pas coupable », le principal facteur de "
     "transformation de l’emploi étant le progrès technique.",
 diss="Nuance indispensable : si les délocalisations expliquent peu, la "
      "concurrence des importations — le choc chinois — explique beaucoup, et "
      "ce sont deux phénomènes différents."),

# =============================================================== c22-06
'ch22-qcm-20': f(niv='connaitre', sp='c22-06', b=2135,
 exp="L’étude The China Syndrome (2013) est due à David Autor et ses "
     "coauteurs. Elle pose une question précise : quel est l’effet de "
     "l’augmentation des importations chinoises sur l’emploi américain ? La "
     "réponse est que les zones fortement exposées à la concurrence chinoise "
     "connaissent davantage de pertes d’emplois manufacturiers — un effet "
     "géographiquement concentré, et non uniformément réparti.",
 why=["Krugman a soutenu au contraire que la mondialisation n’était pas la "
      "cause principale des difficultés industrielles.",
      "Fontagné est l’auteur de La feuille de paye et le caddie (2021).",
      "Mouhoud analyse les effets de compensation des délocalisations."]),
'ch22-qcm-21': f(niv='raisonner', sp='c22-06', b=2163,
 exp="L’apport central d’Autor est de montrer que le problème n’est pas "
     "seulement l’ampleur du choc mais sa durée : les territoires touchés ne "
     "se rétablissent pas nécessairement rapidement. La réallocation attendue "
     "— l’industrie disparaît, les travailleurs se déplacent, de nouveaux "
     "secteurs embauchent — ne se produit pas aussi facilement, d’où des "
     "effets durables sur l’emploi, les salaires et l’activité locale. Un "
     "emploi industriel détruit entraînerait environ 1,5 emploi total détruit "
     "à terme dans la zone.",
 why=["L’ampleur seule ne suffit pas : c’est bien la persistance qui "
      "constitue le résultat marquant.",
      "Les taux de change ne sont pas l’objet de ces travaux.",
      "Les droits de douane sont une réponse politique possible, non le "
      "mécanisme analysé."],
 diss="Mécanisme multiplicateur local à retenir : revenus locaux ↓ → "
      "consommation locale ↓ → commerces et services locaux ↓ → nouvelles "
      "destructions d’emplois."),
'ch22-qcm-22': f(niv='connaitre', sp='c22-06', b=2194,
 exp="Clément Malgouyres étudie en 2018 les effets des importations chinoises "
     "sur l’emploi et les salaires en France : les territoires très exposés "
     "voient leur emploi industriel davantage affecté. Ses travaux montrent "
     "que les effets du choc chinois ne sont pas spécifiques aux États-Unis "
     "mais se retrouvent dans certains bassins industriels français.",
 why=["La fiscalité des multinationales est étudiée ailleurs dans le "
      "chapitre, notamment avec les prix de transfert.",
      "Le capital-risque relève du financement de l’innovation.",
      "Les normes environnementales sont abordées avec le dumping "
      "environnemental."]),
'ch22-questi-69': f(niv='raisonner', sp='c22-06', b=2293,
 exp="Le premier choc, analysé par Autor en 2013, correspond à l’accélération "
     "des importations manufacturières chinoises à partir des années 2000. Il "
     "touchait surtout des secteurs intensifs en travail peu qualifié — "
     "textile, ameublement, certaines activités d’assemblage — que les "
     "économies avancées abandonnaient progressivement dans le cadre de leur "
     "montée en gamme : la spécialisation internationale pouvait donc "
     "apparaître relativement complémentaire, même si les effets locaux ont "
     "été durables et concentrés. Le deuxième choc est différent par nature : "
     "il porte sur la haute technologie et les industries de la transition "
     "énergétique, c’est-à-dire précisément sur les avantages comparatifs que "
     "les pays avancés pensaient conserver grâce à leur supériorité "
     "technologique. La Chine ne concurrence donc plus seulement par les "
     "coûts mais directement sur la frontière technologique, ce qui fait "
     "disparaître la complémentarité antérieure.",
 diss="Facteur aggravant pour l’Europe : le durcissement protectionniste "
      "américain détourne une partie des exportations chinoises vers l’Union "
      "européenne, dont le déficit bilatéral avec la Chine passe d’environ "
      "180-200 milliards d’euros en 2015 à environ 360 milliards en 2025."),

# =============================================================== c22-07
'ch22-qcm-23': f(niv='comprendre', sp='c22-07', b=2319,
 exp="Le deuxième choc chinois porte principalement sur la haute technologie "
     "et les industries de la transition énergétique : véhicules électriques, "
     "batteries, équipements liés aux énergies renouvelables, électronique "
     "avancée. La montée en gamme chinoise concurrence désormais les "
     "productions européennes les plus avancées, ce qui le rend "
     "potentiellement plus dangereux que le premier.",
 why=["Le textile et le jouet relèvent du premier choc chinois, au début des "
      "années 2000.",
      "Les matières premières sont plutôt un domaine de dépendance "
      "européenne qu’un objet de concurrence chinoise.",
      "Les services financiers ne sont pas visés par ce mouvement."],
 diss="Chiffres d’exposition à retenir : près de 55 % de la production "
      "manufacturière de l’Union européenne pourrait être exposée selon une "
      "approche, environ 36 % selon l’approche par le marché intérieur."),
'ch22-qcm-24': f(niv='connaitre', sp='c22-07', b=2500,
 exp="Pour Pierre-Noël Giraud, les activités « nomades » sont celles dont la "
     "localisation peut être mise en concurrence entre plusieurs territoires : "
     "elles sont donc directement exposées à la mondialisation. Les activités "
     "« sédentaires » sont au contraire protégées par la nécessité d’une "
     "proximité géographique entre le producteur et le consommateur.",
 why=["La protection contre la concurrence internationale caractérise les "
      "sédentaires.",
      "Le statut public ou privé n’est pas le critère de la distinction.",
      "L’agriculture n’est pas la catégorie visée : le critère est la "
      "mobilité potentielle de l’activité."],
 diss="Croisement décisif avec la qualification : les nomades qualifiés sont "
      "les grands gagnants, les peu qualifiés des secteurs exposés les "
      "principaux perdants, et les sédentaires peu qualifiés conservent leur "
      "emploi mais subissent une pression salariale."),
'ch22-qcm-25': f(niv='comprendre', sp='c22-07', b=2448,
 exp="Dans La feuille de paye et le caddie (2021), Lionel Fontagné montre que "
     "les effets de la mondialisation sont ambivalents : le consommateur "
     "bénéficie de biens importés moins chers — avec un gain pouvant atteindre "
     "1 000 à 2 000 € par ménage et par an dans certains pays avancés — "
     "tandis que certains travailleurs exposés à la concurrence "
     "internationale perdent leur emploi ou subissent une pression salariale. "
     "Les gains diffus sur le caddie coexistent donc avec des pertes très "
     "concentrées sur la feuille de paye.",
 why=["Affirmer qu’elle ne fait que des gagnants ignore précisément les "
      "pertes concentrées qu’il met en évidence.",
      "Affirmer qu’elle ne fait que des perdants contredit le gain de "
      "pouvoir d’achat mesuré.",
      "Les effets sont au contraire mesurables et importants."],
 diss="C’est cette asymétrie — gains diffus, pertes concentrées — qui "
      "explique la contestation politique de la mondialisation."),
'ch22-questi-70': f(niv='comprendre', sp='c22-07', b=2497,
 exp="Chaque économie comporte des activités « nomades », exposées à la "
     "concurrence mondiale et donc potentiellement délocalisables, et des "
     "activités « sédentaires », ancrées dans un territoire et protégées par "
     "la nécessité d’une proximité avec le consommateur. Mais cette "
     "opposition doit être croisée avec le niveau de qualification, ce qui "
     "donne quatre situations. Les nomades qualifiés constituent les "
     "principaux gagnants : leurs compétences sont rares, internationalement "
     "recherchées et associées aux activités à forte valeur ajoutée. Les "
     "travailleurs peu qualifiés des secteurs exposés cumulent au contraire "
     "les effets de la concurrence internationale et du progrès technique : "
     "ce sont les principaux perdants. Les sédentaires peu qualifiés "
     "conservent davantage leur emploi mais subissent une pression salariale, "
     "car les activités nomades cherchent à réduire le coût des services "
     "locaux qu’elles consomment. La mondialisation redistribue donc les "
     "revenus entre ces ensembles, ce qui explique que certains territoires "
     "restent durablement perdants malgré la baisse générale des prix."),
'ch22-questi-81': f(niv='comprendre', sp='c22-07', b=2440,
 exp="L’image résume l’ambivalence des effets de la mondialisation. Le "
     "caddie, c’est le consommateur : il bénéficie de prix plus bas et d’une "
     "variété accrue, la fragmentation de la production permettant de produire "
     "dans les territoires les moins coûteux, avec un gain pouvant atteindre "
     "1 000 à 2 000 € par ménage et par an. La feuille de paye, c’est le "
     "travailleur : certains salariés subissent la concurrence internationale "
     "sur leur emploi ou sur leur salaire. L’apport de Fontagné est de "
     "souligner l’asymétrie de ces deux effets : les gains de consommation "
     "sont largement diffusés, les pertes d’emploi beaucoup plus concentrées "
     "sur certains groupes sociaux et certains territoires. Un même individu "
     "peut donc être simultanément gagnant et perdant, et l’effet net dépend "
     "de sa position économique.",
 diss="À articuler avec Giraud : la feuille de paye du nomade peu qualifié "
      "est la plus exposée, celle du nomade qualifié la plus favorisée."),

# =============================================================== c22-08
'ch22-qcm-26': f(niv='comprendre', sp='c22-08', b=2957,
 exp="La critique de Krugman porte sur l’assimilation d’une nation à une "
     "entreprise. Une entreprise non compétitive disparaît, pas un pays ; les "
     "échanges internationaux ne sont pas nécessairement un jeu à somme "
     "nulle ; et le solde commercial résulte d’équilibres macroéconomiques — "
     "épargne, investissement, demande intérieure — et non d’une seule "
     "performance productive. Parler de « compétitivité des nations » peut "
     "donc justifier des politiques inadaptées.",
 why=["Krugman ne remet pas en cause la théorie des avantages comparatifs : "
      "il en est au contraire un défenseur.",
      "Les droits de douane ne sont pas l’objet de cette critique "
      "particulière.",
      "Le protectionnisme éducateur est la doctrine de List."],
 diss="Définition de substitution proposée par le cours : la compétitivité "
      "d’une nation est sa capacité à tirer avantage de son insertion "
      "internationale tout en améliorant durablement le niveau de vie de ses "
      "citoyens."),
'ch22-questi-67': f(niv='comprendre', sp='c22-03', b=839,
 exp="En abscisse les étapes de la chaîne de valeur, en ordonnée la valeur "
     "ajoutée : la courbe prend la forme d’un sourire car la valeur est forte "
     "en amont — conception, R&D, qui se localisent dans les territoires "
     "disposant de compétences et d’écosystèmes avancés, par effets "
     "d’agglomération — et forte en aval — marketing, marque, services, "
     "localisés selon la proximité et la taille des marchés de consommation — "
     "mais faible au centre, à l’étape d’assemblage. Un pays cantonné à "
     "l’assemblage capte donc peu de valeur, même si ses exportations brutes "
     "sont élevées : d’où l’enjeu décisif de la montée en gamme. Baldwin "
     "ajoute que le sourire s’est creusé entre les années 1970 et les années "
     "2000, la valeur des services immatériels augmentant tandis que la "
     "multiplication des pays capables d’assembler fait baisser la "
     "rémunération de cette tâche.",
 diss="Conséquence pour les pays en développement : l’insertion dans les "
      "chaînes de valeur est une condition nécessaire mais non suffisante du "
      "développement."),
'ch22-questi-71': f(niv='raisonner', sp='c22-08', b=2957,
 exp="Parce qu’elle assimile une nation à une entreprise. Une entreprise non "
     "compétitive disparaît, pas un pays. Le commerce international n’est pas "
     "nécessairement un jeu à somme nulle : les gains des uns ne sont pas "
     "mécaniquement les pertes des autres. Le niveau de vie dépend d’abord de "
     "la productivité intérieure, et un déficit commercial ne constitue pas "
     "en lui-même une preuve de faiblesse économique, puisqu’il résulte aussi "
     "de déterminants macroéconomiques comme l’épargne, l’investissement et la "
     "demande intérieure. Parler de compétitivité nationale peut donc "
     "justifier des politiques inadaptées, notamment une course au moins-"
     "disant salarial. Le cours propose néanmoins de conserver le terme à "
     "condition de lui donner un autre sens : la capacité d’une nation à "
     "tirer avantage de son insertion internationale tout en améliorant "
     "durablement le niveau de vie de sa population.",
 diss="Argument décisif : réduire les salaires au maximum n’est pas "
      "nécessairement une stratégie de compétitivité."),

# =============================================================== c22-09
'ch22-qcm-27': f(niv='connaitre', sp='c22-09', b=3070,
 exp="Le coût unitaire du travail rapporte le coût du travail à la "
     "productivité du travail. C’est l’indicateur pertinent pour comparer la "
     "compétitivité du travail entre pays : un salaire horaire élevé "
     "n’implique pas un coût unitaire élevé si la productivité est "
     "elle-même élevée. Inversement, une main-d’œuvre peu chère mais "
     "faiblement productive peut présenter un coût unitaire proche de celui "
     "d’une économie à hauts salaires.",
 why=["Multiplier le salaire par la productivité n’a aucun sens économique "
      "ici.",
      "Le salaire horaire est le coût du travail par heure, non le coût "
      "unitaire.",
      "Le rapport masse salariale / chiffre d’affaires mesure le poids du "
      "travail dans l’activité, non son coût unitaire."],
 diss="Application immédiate : le coût horaire français est très proche de "
      "celui de l’Allemagne et des Pays-Bas, ce qui interdit d’expliquer les "
      "difficultés françaises par un coût du travail exceptionnellement "
      "élevé."),
'ch22-qcm-28': f(niv='comprendre', sp='c22-09', b=3289,
 exp="La compétitivité hors-prix désigne tous les facteurs qui permettent à "
     "une entreprise de vendre indépendamment d’un prix plus faible. Elle "
     "comporte des dimensions objectives — avance technologique, qualité des "
     "services associés, niveau de qualification de la main-d’œuvre — et des "
     "dimensions subjectives : la réputation et l’image de marque modifient "
     "la perception de la qualité et permettent de pratiquer des prix plus "
     "élevés.",
 why=["Le niveau des prix définit la compétitivité-prix, c’est-à-dire "
      "précisément l’autre forme de compétitivité.",
      "Le taux de change agit sur la compétitivité-prix.",
      "Les droits de douane sont un instrument de politique commerciale, non "
      "une qualité de l’offre."],
 diss="Point important : la compétitivité hors-prix résulte souvent d’une "
      "synergie entre investissement public dans le capital humain et la "
      "recherche, et investissement privé dans l’innovation."),
'ch22-qcm-29': f(niv='connaitre', sp='c22-09', b=3368,
 exp="Le Crédit d’impôt recherche existe depuis 1983 et a été profondément "
     "réformé en 2008. Sa logique est de corriger le sous-investissement "
     "privé en R&D : l’entreprise qui engage des dépenses de recherche "
     "bénéficie d’un crédit d’impôt, ce qui réduit le coût privé de la "
     "recherche et renforce l’incitation à investir — donc, à terme, la "
     "compétitivité hors-prix.",
 why=["1973 ne correspond à aucun dispositif du cours.",
      "1993 est postérieur à la création du CIR.",
      "2003 précède la réforme de 2008 mais ne correspond pas à la "
      "création."]),
'ch22-qcm-30': f(niv='connaitre', sp='c22-09', b=3382,
 exp="Le Crédit d’impôt pour la compétitivité et l’emploi est instauré en "
     "2013. Il vise d’abord à améliorer la compétitivité-coût en restaurant "
     "les marges des entreprises, avec l’espoir que ces ressources "
     "supplémentaires permettent ensuite l’investissement, l’emploi et la "
     "montée en gamme. À partir de 2019, il est transformé en réductions "
     "permanentes de cotisations patronales.",
 why=["2008 est l’année de la réforme du CIR, non de la création du CICE.",
      "2017 et 2020 ne correspondent à aucune de ces dates.",
      "2020 est postérieur à la transformation du CICE en allègements de "
      "cotisations."]),
'ch22-vraifa-53': f(niv='comprendre', sp='c22-09', b=3382,
 exp="Le CICE agit surtout sur le coût du travail et les marges, donc sur la "
     "compétitivité-coût ; c’est le Crédit d’impôt recherche qui vise la "
     "compétitivité hors-prix, en réduisant le coût privé de la R&D. La "
     "distinction est importante car les deux dispositifs reposent sur des "
     "diagnostics différents : un problème de coûts d’un côté, un "
     "sous-investissement en innovation de l’autre.",
 diss="Le cours souligne un paradoxe : malgré des aides importantes, les "
      "effets sur les performances extérieures sont parfois difficiles à "
      "identifier, car la compétitivité résulte d’un ensemble de déterminants "
      "complémentaires."),

}
