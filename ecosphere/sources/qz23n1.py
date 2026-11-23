# -*- coding: utf-8 -*-
"""Chapitre 23 — questions nouvelles, sous-parties c23-01 à c23-05."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c23-01
f(id='q23-n01', sp='c23-01', niv='connaitre', type='qcm', b=6,
  q="À quelles deux grandes questions l’analyse économique du commerce "
    "international cherche-t-elle à répondre ?",
  opts=["Quel niveau de droits de douane appliquer, et à quels produits",
        "Pourquoi les pays se spécialisent et échangent, et quelles sont les "
        "conséquences de ces échanges",
        "Comment mesurer la balance commerciale, et comment la rééquilibrer",
        "Quels pays sont riches, et pourquoi"],
  ans=1,
  why=["Le choix des instruments est une question de politique commerciale, "
       "qui vient après l’analyse des échanges.",
       "La mesure des soldes extérieurs est un travail de comptabilité "
       "nationale.",
       "Les écarts de richesse entre nations sont un objet d’étude distinct."],
  exp="La première question est positive : elle porte sur les raisons qui "
      "poussent les pays à se spécialiser et sur les mécanismes qui "
      "expliquent l’existence des échanges. La seconde porte sur leurs "
      "conséquences, et conduit rapidement à un registre normatif dès qu’il "
      "s’agit d’apprécier si l’ouverture est souhaitable. Toute la structure "
      "du chapitre découle de cette distinction.",
  diss="Introduction type : annoncer que l’on traitera d’abord les "
       "déterminants des échanges, puis l’évaluation de leurs effets."),

f(id='q23-n02', sp='c23-01', niv='comprendre', type='qcm', b=58,
  q="Sur quoi repose principalement le renouvellement de la théorie du "
    "commerce international ?",
  opts=["Sur l’abandon progressif des hypothèses restrictives des modèles "
        "traditionnels",
        "Sur le remplacement de l’avantage comparatif par la balance "
        "commerciale",
        "Sur le rejet complet des travaux de Ricardo",
        "Sur l’abandon de toute modélisation mathématique"],
  ans=0,
  why=["La balance commerciale n’est pas un concept explicatif des "
       "spécialisations.",
       "Les théories contemporaines ne suppriment pas l’intuition "
       "ricardienne : elles la complètent.",
       "La formalisation s’est au contraire renforcée, notamment avec "
       "Krugman."],
  exp="Les théories contemporaines introduisent la concurrence imparfaite, "
      "les économies d’échelle, la différenciation des produits et "
      "l’hétérogénéité des firmes, précisément parce que les hypothèses "
      "traditionnelles — concurrence parfaite, rendements constants, produits "
      "homogènes, travail homogène, immobilité des facteurs — ne permettaient "
      "pas de rendre compte des échanges réellement observés, à commencer par "
      "le commerce intra-branche.",
  diss="Fil directeur du chapitre : chaque nouvelle théorie se construit en "
       "levant une hypothèse précise du modèle précédent."),

f(id='q23-n03', sp='c23-01', niv='raisonner', type='courte', b=151,
  q="Comment l’évolution des positions de Krugman illustre-t-elle le "
    "changement de regard sur la mondialisation ?",
  ans={'modele': "Dans La mondialisation n’est pas coupable (1996), Krugman "
       "soutient que la désindustrialisation des économies avancées tient "
       "d’abord au progrès technique et à l’évolution de la demande plutôt "
       "qu’à la seule concurrence internationale. Mais plusieurs décennies "
       "d’hypermondialisation modifient son appréciation : en 2019, il "
       "demande « qu’ont raté les économistes sur la mondialisation ? » et "
       "reconnaît que l’analyse dominante a sous-estimé certains effets, en "
       "particulier leur concentration sur des territoires industriels et des "
       "catégories sociales précises. L’erreur n’est pas d’avoir surestimé "
       "les gains agrégés de long terme, mais d’avoir accordé trop peu "
       "d’attention aux coûts d’ajustement de court terme : la réallocation "
       "des travailleurs n’est ni immédiate ni indolore. Cette évolution "
       "résume le passage d’une analyse centrée sur les gains agrégés à une "
       "analyse intégrant les effets distributifs.",
       'cles': [{'f': ['1996', 'pas coupable', 'progres technique'],
                 'l': "en 1996, le progrès technique plutôt que la concurrence internationale"},
                {'f': ['2019', 'rate', 'reconnait', 'revient'],
                 'l': "en 2019, un retour critique sur l'analyse dominante"},
                {'f': ['territoire', 'concentre', 'categorie', 'local'],
                 'l': "des effets très concentrés sur certains territoires et catégories"},
                {'f': ['ajustement', 'court terme', 'reallocation', 'indolore'],
                 'l': "les coûts d'ajustement de court terme sous-estimés"},
                {'f': ['agrege', 'distributif', 'repartition'],
                 'l': "le passage des gains agrégés aux effets distributifs"}]},
  exp="Krugman reconnaît que les économistes ont accordé trop d’attention aux "
      "gains agrégés de long terme de l’ouverture et insuffisamment aux coûts "
      "d’ajustement supportés à court terme par certains travailleurs et "
      "territoires.",
  diss="Exemple idéal pour montrer qu’un désaccord sur la mondialisation peut "
       "porter non sur les gains mais sur leur répartition et leur "
       "calendrier."),

f(id='q23-n04', sp='c23-01', niv='raisonner', type='qcm', b=170,
  q="Pourquoi un gain économique mondial ne garantit-il pas l’acceptabilité "
    "politique de la mondialisation ?",
  opts=["Parce que les gains mondiaux sont toujours inférieurs aux pertes "
        "nationales",
        "Parce que les individus évaluent la mondialisation à partir de ses "
        "conséquences sur leur emploi, leurs revenus et leur territoire",
        "Parce que les gains sont impossibles à mesurer",
        "Parce que les électeurs ignorent l’existence du commerce "
        "international"],
  ans=1,
  why=["Rien n’indique que les gains mondiaux soient inférieurs aux pertes : "
       "le cours admet des gains agrégés positifs.",
       "Les gains sont estimés, parfois avec précision, comme le montrent les "
       "évaluations de pouvoir d’achat.",
       "L’ignorance des électeurs n’est pas l’argument du cours : ils "
       "raisonnent au contraire à partir d’une expérience vécue."],
  exp="Le raisonnement économique traditionnel consiste à dire que les pertes "
      "subies par certains travailleurs peuvent être compensées par des gains "
      "plus larges. Mais les individus raisonnent d’abord à partir de leur "
      "propre situation : savoir que l’ouverture a permis l’enrichissement de "
      "classes moyennes dans d’autres pays ne suffit pas à rendre la "
      "mondialisation acceptable pour un travailleur industriel dont l’emploi "
      "a disparu. D’où un vote possible en faveur de davantage de protection "
      "commerciale.",
  diss="À articuler avec la courbe de l’éléphant de Milanović, qui donne la "
       "mesure statistique de ce paradoxe distributif."),

f(id='q23-n05', sp='c23-01', niv='connaitre', type='qcm', b=263,
  q="Que désigne le néo-mercantilisme, tel que le cours le définit ?",
  opts=["Une stratégie consistant à réduire l’ensemble des échanges "
        "internationaux",
        "Une stratégie consistant à favoriser les exportations tout en "
        "limitant les importations afin de renforcer la puissance économique "
        "nationale",
        "Une stratégie consistant à accumuler des réserves de change",
        "Une stratégie consistant à n’échanger qu’avec des pays alliés"],
  ans=1,
  why=["Les États protectionnistes cherchent précisément à ne pas limiter "
       "leurs propres exportations.",
       "L’accumulation de réserves est une politique monétaire, non "
       "commerciale.",
       "La restriction aux pays alliés correspond au friend-shoring, qui est "
       "une autre logique."],
  exp="Le protectionnisme contemporain prend souvent cette forme : les États "
      "cherchent moins à réduire l’ensemble des échanges qu’à limiter les "
      "importations tout en conservant un accès maximal aux marchés "
      "étrangers pour leurs propres entreprises. La logique est donc "
      "asymétrique — et c’est précisément ce qui la rend difficilement "
      "soutenable, puisque les partenaires peuvent appliquer la même "
      "stratégie.",
  diss="Cette asymétrie explique pourquoi le protectionnisme déclenche des "
       "représailles : la stratégie n’est gagnante que si l’on est seul à "
       "l’appliquer."),

f(id='q23-n06', sp='c23-01', niv='appliquer', type='assoc', b=298,
  q="Associez chaque politique publique au canal par lequel elle modifie la "
    "concurrence internationale.",
  ans=[["Harmoniser ou abaisser l’imposition des bénéfices pour attirer les "
        "entreprises", "Politique fiscale"],
       ["Subventionner une filière pour abaisser artificiellement les coûts "
        "relatifs de ses entreprises", "Politique industrielle"],
       ["Relever un droit de douane ou imposer une norme à l’importation",
        "Politique commerciale"],
       ["Empêcher une entreprise d’abuser de son pouvoir de marché sur un "
        "territoire", "Politique de la concurrence"]],
  exp="La concurrence internationale ne dépend pas uniquement de l’efficacité "
      "productive des entreprises : elle est également façonnée par les "
      "politiques fiscales, industrielles et commerciales des États. Le "
      "chapitre se concentre sur la politique commerciale, c’est-à-dire "
      "l’ensemble des interventions publiques destinées à agir sur les flux "
      "du commerce international, mais les trois autres canaux restent "
      "présents en arrière-plan.",
  diss="Articulation avec le chapitre précédent : les États interviennent "
       "dans la mondialisation par plusieurs politiques, dont la politique "
       "commerciale n’est qu’une."),

# ------------------------------------------------------------- c23-02
f(id='q23-n07', sp='c23-02', niv='comprendre', type='qcm', b=322,
  q="Quelle idée commune réunit les analyses classiques de Smith et de "
    "Ricardo ?",
  opts=["La spécialisation permet d’affecter les facteurs aux activités où "
        "ils sont relativement les plus efficaces, ce qui accroît la "
        "production mondiale",
        "L’échange international est un jeu à somme nulle entre nations",
        "Les facteurs de production circulent librement entre les pays",
        "La richesse d’une nation se mesure à son excédent commercial"],
  ans=0,
  why=["Le jeu à somme nulle est la conception mercantiliste, que Smith et "
       "Ricardo contestent.",
       "Les deux auteurs supposent au contraire l’immobilité internationale "
       "des facteurs.",
       "L’identification de la richesse à l’excédent commercial est également "
       "mercantiliste."],
  exp="Cette réallocation transforme l’échange en jeu à somme positive : la "
      "production mondiale augmente à facteurs donnés. Smith et Ricardo "
      "diffèrent cependant sur le critère de la spécialisation — avantage "
      "absolu chez le premier, avantage comparatif chez le second — et sur la "
      "forme de l’analyse, Ricardo construisant un véritable modèle avec des "
      "hypothèses explicites.",
  diss="Phrase charnière utile : c’est la même intuition, mais Ricardo la "
       "rend générale et démontrable."),

f(id='q23-n08', sp='c23-02', niv='comprendre', type='qcm', b=323,
  q="En quoi Smith présente-t-il l’ouverture internationale comme un "
    "prolongement de la division du travail ?",
  opts=["Parce que l’ouverture permet d’importer de la main-d’œuvre étrangère",
        "Parce qu’élargir le marché permet de pousser plus loin la "
        "spécialisation des producteurs, avec les mêmes effets qu’à "
        "l’intérieur d’une manufacture",
        "Parce qu’elle oblige les États à coopérer",
        "Parce qu’elle augmente les recettes douanières"],
  ans=1,
  why=["L’immigration de main-d’œuvre n’est pas le mécanisme invoqué par "
       "Smith.",
       "La coopération entre États est une conséquence institutionnelle "
       "possible, non le mécanisme économique.",
       "Les recettes douanières relèvent d’une lecture fiscale, étrangère à "
       "l’argument."],
  exp="Les trois effets de la division du travail — dextérité accrue, "
      "réduction des pertes de temps, incitation à innover — jouent d’autant "
      "plus que le marché est vaste. L’ouverture internationale élargit donc "
      "le marché et permet de pousser la spécialisation plus loin que ne le "
      "permettrait la seule demande nationale. On retrouvera exactement cette "
      "idée chez Krugman, sous le nom d’effet de dimension.",
  diss="Continuité remarquable à signaler : de Smith à Krugman, la taille du "
       "marché reste une source autonome de gain."),

f(id='q23-n09', sp='c23-02', niv='appliquer', type='ordre', b=320,
  q="Remettez dans l’ordre la construction du raisonnement classique sur "
    "l’échange international.",
  ans=["Un pays constate qu’il est plus productif que les autres dans "
       "certaines productions : c’est l’avantage absolu de Smith",
       "Mais un pays moins productif dans toutes les productions se trouve "
       "alors exclu de l’échange",
       "Ricardo propose de comparer non plus les productivités entre pays, "
       "mais les coûts d’opportunité à l’intérieur de chaque pays",
       "Chaque pays dispose donc toujours d’un avantage comparatif, et "
       "l’échange devient mutuellement avantageux pour tous",
       "Mill montre enfin entre quelles bornes doit se situer le prix "
       "international, donc comment le gain se partage"],
  exp="Cet enchaînement résume l’apport propre de chaque auteur : Smith pose "
      "le principe de la spécialisation, Ricardo le généralise en changeant "
      "la nature de la comparaison, Mill en détermine la répartition. Ricardo "
      "va plus loin que Smith non seulement par son résultat, mais aussi par "
      "sa méthode : il construit un véritable modèle, avec des hypothèses "
      "précises.",
  diss="Structure de partie toute prête pour une première sous-partie sur les "
       "théories traditionnelles."),

f(id='q23-n10', sp='c23-02', niv='raisonner', type='vf', b=415,
  q="Dans la logique mercantiliste, l’État n’a aucune raison d’intervenir "
    "dans le commerce extérieur.",
  ans=False,
  exp="C’est exactement l’inverse. Si le commerce permet d’accumuler des "
      "richesses monétaires, alors l’État doit encourager les productions "
      "exportatrices et limiter les importations : le colbertisme illustre "
      "cette volonté de développer les manufactures et des producteurs "
      "puissants capables de vendre à l’étranger. Le mercantilisme repose en "
      "outre sur une conception conflictuelle des relations internationales, "
      "dans laquelle le gain d’un pays peut être perçu comme la perte d’un "
      "autre.",
  diss="Opposition à poser nettement : le libre-échangisme raisonne en gains "
       "mutuels, le mercantilisme en compétition pour les marchés et la "
       "puissance."),

# ------------------------------------------------------------- c23-03
f(id='q23-n11', sp='c23-03', niv='connaitre', type='qcm', b=536,
  q="Comment se définit le coût d’opportunité d’une production ?",
  opts=["Le prix de vente du bien sur le marché mondial",
        "La quantité de l’autre bien à laquelle il faut renoncer pour "
        "produire une unité du premier",
        "Le coût total de production exprimé en monnaie",
        "La différence entre le prix intérieur et le prix mondial"],
  ans=1,
  why=["Le prix mondial est une donnée de marché, non un coût interne.",
       "Le coût monétaire total ne dit rien de l’arbitrage entre deux "
       "productions.",
       "L’écart entre prix intérieur et prix mondial mesure l’effet d’une "
       "protection."],
  exp="Le coût d’opportunité est une comparaison interne : il mesure ce que "
      "l’on abandonne en affectant des facteurs à une production plutôt qu’à "
      "une autre. C’est ce qui en fait une notion plus générale que l’avantage "
      "absolu : elle ne compare pas des pays entre eux mais des emplois "
      "alternatifs des facteurs à l’intérieur d’un même pays, de sorte "
      "qu’aucun pays ne peut être désavantagé partout.",
  diss="Conséquence logique à exploiter : les coûts d’opportunité étant des "
       "rapports, ils ne peuvent pas tous être défavorables."),

f(id='q23-n12', sp='c23-03', niv='appliquer', type='qcm', b=536,
  q="Dans l’exemple ricardien (drap 90/100, vin 80/120 en hommes-années), "
    "quel est le coût d’opportunité du vin en Angleterre ?",
  opts=["0,83 drap",
        "1,2 drap",
        "1,125 vin",
        "0,67 drap"],
  ans=1,
  why=["0,83 est le coût d’opportunité du drap en Angleterre, c’est-à-dire "
       "l’inverse.",
       "1,125 vin est le coût d’opportunité du drap au Portugal.",
       "0,67 ne correspond à aucun des rapports de l’exemple."],
  exp="En Angleterre, le vin exige 120 hommes-années et le drap 100 : le coût "
      "d’opportunité du vin vaut donc 120/100 = 1,2 drap. Au Portugal, il "
      "vaut 80/90 ≈ 0,89 drap. Le Portugal renonce à moins de drap pour "
      "produire du vin : son avantage comparatif est donc dans le vin, "
      "symétriquement à celui de l’Angleterre dans le drap.",
  diss="Vérification utile en copie : les deux avantages comparatifs doivent "
       "être symétriques, sinon le calcul est erroné."),

f(id='q23-n13', sp='c23-03', niv='appliquer', type='ordre', b=573,
  q="Remettez dans l’ordre le raisonnement conduisant au gain ricardien à "
    "l’échange.",
  ans=["Chaque pays compare ses coûts d’opportunité internes",
       "Chaque pays se spécialise dans la production où son coût "
       "d’opportunité est le plus faible",
       "Les facteurs sont réaffectés vers ces emplois plus efficaces",
       "La production mondiale augmente à facteurs donnés — de 4 à 4,325 "
       "unités dans l’exemple",
       "Les pays échangent, et chacun obtient davantage que ce qu’il "
       "produirait seul"],
  exp="Le même résultat peut se lire dans l’autre sens : à production "
      "mondiale inchangée, le même volume s’obtient avec moins de travail, "
      "soit 30 unités économisées dans l’exemple du cours. Les deux gains de "
      "Ricardo — hausse de la production mondiale et économie de facteurs — "
      "ne sont donc que deux manières de décrire le même effet de "
      "réallocation.",
  diss="Attention à une erreur fréquente : le gain vient de la réallocation "
       "des facteurs, pas de l’échange en lui-même."),

f(id='q23-n14', sp='c23-03', niv='raisonner', type='vf', b=1360,
  q="Le modèle de Ricardo explique pourquoi les productivités diffèrent entre "
    "les pays.",
  ans=False,
  exp="C’est la principale question laissée ouverte par Ricardo : son modèle "
      "explique comment une différence de productivité produit une "
      "spécialisation, mais pas véritablement pourquoi cette différence "
      "existe. Il constate que le Portugal est plus productif dans certaines "
      "activités sans en rendre compte. Deux prolongements s’engouffrent dans "
      "cette brèche : HOS explique l’avantage par les dotations factorielles, "
      "les approches néo-technologiques par les écarts de technologie et de "
      "capacité d’innovation.",
  diss="Transition très efficace entre les deux premières parties du "
       "chapitre : la lacune de Ricardo engendre toute la théorie "
       "postérieure."),

f(id='q23-n15', sp='c23-03', niv='comprendre', type='qcm', b=1332,
  q="Quelle hypothèse ricardienne la réalité des reconversions "
    "professionnelles met-elle le plus directement en cause ?",
  opts=["L’immobilité internationale des facteurs de production",
        "La mobilité des facteurs entre secteurs à l’intérieur d’un pays",
        "L’existence de deux biens seulement",
        "La concurrence parfaite sur les marchés"],
  ans=1,
  why=["L’immobilité internationale des facteurs reste largement vérifiée "
       "pour le travail, et le modèle ne prétend pas le contraire.",
       "Le nombre de biens est une simplification de présentation, sans "
       "conséquence sur les coûts d’ajustement.",
       "La concurrence parfaite est une hypothèse forte, mais ce n’est pas "
       "celle que les reconversions démentent."],
  exp="Le modèle suppose que les travailleurs sont suffisamment homogènes pour "
      "changer de secteur sans difficulté. Or un travailleur déplacé par "
      "l’ouverture ne dispose pas nécessairement des compétences requises dans "
      "le secteur en expansion, et la mobilité géographique a elle-même un "
      "coût : la réallocation du travail n’est jamais instantanée. Ricardo "
      "l’admet partiellement dans son analyse des Corn Laws, où il reconnaît "
      "qu’une ouverture trop brutale impose des coûts d’ajustement.",
  diss="Mot-clé à employer : chômage d’inadéquation, lorsque les compétences "
       "ou la localisation ne correspondent pas aux emplois disponibles."),

# ------------------------------------------------------------- c23-04
f(id='q23-n16', sp='c23-04', niv='appliquer', type='qcm', b=751,
  q="Dans l’exemple ricardien, le prix international du vin exprimé en drap "
    "doit se situer entre 0,88 et 1,2. Que se passe-t-il si ce prix s’établit "
    "exactement à 1,2 ?",
  opts=["Les deux pays partagent le gain à égalité",
        "L’un des deux pays se trouve à la limite de l’indifférence entre "
        "échanger et rester en autarcie, et l’autre capte l’essentiel du gain",
        "L’échange devient impossible",
        "Les deux pays perdent à l’échange"],
  ans=1,
  why=["Le partage égal supposerait un prix situé au milieu de "
       "l’intervalle.",
       "L’échange reste possible : le prix est encore dans l’intervalle, à sa "
       "borne.",
       "À l’intérieur des bornes, aucun pays ne perd par rapport à "
       "l’autarcie."],
  exp="C’est tout l’apport de Mill : le prix international détermine le "
      "partage du gain. Aux bornes de l’intervalle, un pays retrouve "
      "exactement son rapport d’échange interne : il n’a donc plus rien à "
      "gagner et préférerait l’autarcie, tandis que son partenaire capte "
      "l’essentiel du gain. Plus le prix est proche de la borne favorable à "
      "un pays, plus son gain est élevé.",
  diss="Conséquence politique immédiate : le rapport de force dans la "
       "négociation commerciale détermine le partage du gain à l’échange."),

f(id='q23-n17', sp='c23-04', niv='raisonner', type='qcmm', b=836,
  q="Quels éléments du raisonnement de Marx conduisent à la recherche de "
    "débouchés extérieurs ? (plusieurs réponses)",
  opts=["La concurrence entre capitalistes, qui impose l’accumulation",
        "La hausse de la composition du capital, qui déprime tendanciellement "
        "le taux de profit",
        "L’armée industrielle de réserve, qui maintient les salaires bas",
        "L’insuffisance de la demande intérieure pour absorber la production",
        "La recherche de variété par les consommateurs nationaux"],
  ans=[0, 1, 2, 3],
  why=["Exacte : l’accumulation n’est pas un choix mais une contrainte "
       "concurrentielle.",
       "Exacte : la plus-value venant du travail, l’élévation de la part du "
       "capital pèse sur le taux de profit.",
       "Exacte : la pression sur les salaires est un ressort central du "
       "raisonnement.",
       "Exacte : c’est la conclusion qui rend l’exportation nécessaire.",
       "Inexacte : la demande de variété est l’explication de "
       "Lassudrie-Duchêne, dans un cadre théorique entièrement différent."],
  exp="L’enchaînement transforme radicalement le sens de l’échange : "
      "l’exportation n’est plus un bienfait réciproque mais la résolution "
      "provisoire d’une contradiction interne du mode de production. Le "
      "commerce international devient alors un symptôme, et non un gain.",
  diss="Renversement à exploiter : chez les classiques le commerce crée de la "
       "richesse, chez Marx il reporte une crise."),

f(id='q23-n18', sp='c23-04', niv='comprendre', type='vf', b=738,
  q="Ricardo détermine le prix auquel les deux pays échangeront effectivement.",
  ans=False,
  exp="Ricardo établit l’existence du gain à l’échange mais laisse "
      "indéterminé le prix international, et donc le partage de ce gain. "
      "C’est précisément l’apport propre de John Stuart Mill : montrer que ce "
      "prix doit rester entre les rapports d’échange internes des deux pays, "
      "faute de quoi l’un d’eux préférerait l’autarcie. La question « l’échange "
      "est-il avantageux ? » et la question « pour qui l’est-il le plus ? » "
      "sont donc deux problèmes distincts.",
  diss="Distinction d’une grande valeur en dissertation : l’existence du gain "
       "et sa répartition ne se démontrent pas de la même manière."),

f(id='q23-n19', sp='c23-04', niv='appliquer', type='assoc', b=819,
  q="Associez chaque auteur à l’apport qui lui revient en propre.",
  ans=[["Il démontre que l’échange reste mutuellement avantageux même quand "
        "un pays est moins productif dans toutes les productions",
        "Ricardo"],
       ["Il détermine entre quelles bornes le prix international doit se "
        "situer, et donc comment le gain se partage", "John Stuart Mill"],
       ["Il fait de la recherche de débouchés extérieurs la conséquence de "
        "l’insuffisance de la demande intérieure", "Marx"],
       ["Il présente l’ouverture internationale comme un prolongement de la "
        "division du travail", "Adam Smith"]],
  exp="Ces quatre apports se complètent et ne s’annulent pas : Smith pose le "
      "principe, Ricardo le généralise, Mill en précise la répartition, Marx "
      "en conteste la signification. Les trois premiers partagent une lecture "
      "en gains mutuels ; le quatrième fait de l’exportation la résolution "
      "provisoire d’une contradiction interne.",
  diss="Attribuer à chacun son apport exact est l’un des points les mieux "
       "valorisés dans un devoir sur les théories du commerce."),

# ------------------------------------------------------------- c23-05
f(id='q23-n20', sp='c23-05', niv='appliquer', type='assoc', b=1162,
  q="Associez chaque analyse critique au mécanisme précis qu’elle met en "
    "évidence.",
  ans=[["Les prix des produits primaires progressent moins vite que ceux des "
        "produits manufacturés : il faut exporter plus pour importer autant",
        "Prebisch (1950)"],
       ["À productivité comparable, des salaires très bas se répercutent dans "
        "des prix d’exportation très bas et transfèrent de la valeur",
        "Arghiri Emmanuel"],
       ["L’offre supplémentaire d’un pays fait baisser le prix mondial, et "
        "cette perte peut dépasser le gain de volume", "Bhagwati (1958)"],
       ["La concentration du capital, la fusion banque-industrie et "
        "l’exportation de capitaux conduisent au partage des territoires",
        "Lénine"]],
  exp="Ces quatre analyses établissent qu’une spécialisation conforme aux "
      "avantages comparatifs peut être défavorable au pays qui l’adopte. "
      "Leur limite est contextuelle : elles sont formulées pendant la grande "
      "divergence, alors que l’hypermondialisation s’accompagne au contraire "
      "du rattrapage de nombreux pays émergents.",
  diss="Usage recommandé : les mobiliser pour les économies restées "
       "spécialisées dans le primaire, les nuancer pour celles qui ont monté "
       "en gamme."),

f(id='q23-n21', sp='c23-05', niv='raisonner', type='courte', b=1008,
  q="Pourquoi la thèse de Prebisch remet-elle en cause le principe même de la "
    "spécialisation selon les avantages comparatifs ?",
  ans={'modele': "Parce qu’elle montre qu’une spécialisation parfaitement "
       "conforme aux avantages comparatifs peut appauvrir relativement le "
       "pays qui l’adopte. Sur la période 1875-1938, les prix des produits "
       "primaires progressent moins vite que ceux des produits manufacturés : "
       "les termes de l’échange d’un pays spécialisé dans le primaire se "
       "dégradent tendanciellement, de sorte qu’il doit exporter des "
       "quantités croissantes pour importer la même quantité de biens "
       "manufacturés. Le raisonnement ricardien n’est pas faux, mais il est "
       "statique : il compare deux situations à prix donnés, alors que la "
       "spécialisation elle-même modifie les prix relatifs dans le temps. La "
       "conséquence pratique est décisive pour la politique économique : si "
       "toutes les spécialisations ne se valent pas, alors l’État peut avoir "
       "intérêt à en changer, ce qui fonde les stratégies "
       "d’industrialisation.",
       'cles': [{'f': ['terme de l echange', 'degradation', 'prix relatif'],
                 'l': "la dégradation tendancielle des termes de l'échange"},
                {'f': ['primaire', 'manufactur', 'matiere premiere'],
                 'l': "les produits primaires contre les produits manufacturés"},
                {'f': ['exporter plus', 'quantite croissante', 'importer autant'],
                 'l': "exporter davantage pour importer autant"},
                {'f': ['statique', 'dynamique', 'dans le temps', 'prix donne'],
                 'l': "le raisonnement ricardien est statique"},
                {'f': ['industrialisation', 'changer', 'politique', 'toutes les specialisation'],
                 'l': "toutes les spécialisations ne se valent pas"}]},
  exp="Prebisch établit que les prix des produits primaires progressent moins "
      "vite que ceux des manufacturés : une spécialisation conforme aux "
      "avantages comparatifs peut donc devenir défavorable.",
  diss="À rapprocher de Rodrik : une économie peut être enfermée dans des "
       "activités peu dynamiques, d’où la question de la montée en gamme."),

f(id='q23-n22', sp='c23-05', niv='raisonner', type='vf', b=1137,
  q="Les analyses néo-marxistes du commerce international sont démenties par "
    "le rattrapage des pays émergents.",
  ans=True,
  exp="C’est la limite principale, et elle est contextuelle. Ces analyses sont "
      "formulées au moment de la grande divergence, lorsque l’écart entre le "
      "Nord et le Sud se creuse : elles décrivent donc fidèlement leur "
      "époque. Or l’hypermondialisation s’accompagne du rattrapage de "
      "nombreuses économies émergentes, ce qui interdit d’en faire une loi "
      "générale de l’échange international. Elles conservent néanmoins une "
      "portée pour les économies restées spécialisées dans des productions à "
      "faible valeur ajoutée, dont l’insertion internationale demeure "
      "dominée.",
  diss="Formulation équilibrée : ces analyses ne sont pas invalidées, leur "
       "domaine de validité est restreint."),

]
