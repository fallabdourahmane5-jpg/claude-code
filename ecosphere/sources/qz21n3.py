# -*- coding: utf-8 -*-
"""Chapitre 21 — questions nouvelles, sous-parties c21-10 à c21-13."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c21-10
f(id='q21-n41', sp='c21-10', niv='connaitre', type='assoc', b=3401,
  q="Associez chaque indicateur de la mondialisation commerciale à ce qu’il "
    "mesure.",
  ans=[["[(X + M) / 2] / PIB × 100", "Le taux d’ouverture : le poids des échanges extérieurs dans la richesse produite"],
       ["La valeur des exportations rapportée à celle des importations", "Le taux de couverture : le commerce extérieur est-il excédentaire ou déficitaire ?"],
       ["La part de la demande intérieure satisfaite par des importations", "Le taux de pénétration : la dépendance aux importations"],
       ["L’évolution relative du prix des exportations et des importations", "Les termes de l’échange"]],
  exp="Le cours ajoute la part exportée de la production, qui mesure le "
      "caractère extraverti d’une économie. Il insiste sur une nuance "
      "essentielle : les termes de l’échange ne mesurent pas des montants "
      "mais des évolutions de prix — c’est ce qui fonde l’analyse de "
      "Prebisch.",
  diss="Boîte à outils indispensable : chaque indicateur répond à une "
       "question différente, et aucun ne suffit seul."),

f(id='q21-n42', sp='c21-10', niv='comprendre', type='qcm', b=3460,
  q="Pourquoi le taux d’ouverture dépend-il fortement de la taille du pays ?",
  opts=["Parce que les grands pays interdisent les importations",
        "Parce qu’un grand territoire disposant d’un vaste marché intérieur "
        "satisfait une part importante de sa demande par sa production "
        "domestique, alors qu’un petit pays doit davantage échanger",
        "Parce que les petits pays produisent plus efficacement",
        "Parce que le PIB des grands pays est mal mesuré"],
  ans=1,
  why=["Aucune interdiction : c’est un effet de structure.",
       "L’efficacité productive n’est pas en cause.",
       "La mesure du PIB n’est pas le problème : c’est la comparaison "
       "numérateur / dénominateur."],
  exp="Les petits pays sont donc mécaniquement plus ouverts. C’est pourquoi "
      "l’Union européenne apparaît très exposée aux chocs commerciaux "
      "internationaux, tandis que les États-Unis et la Chine semblent "
      "relativement moins ouverts selon cet indicateur. La seconde limite est "
      "plus profonde encore : le taux d’ouverture compare des exportations en "
      "valeur brute à un PIB mesuré en valeur ajoutée.",
  diss="Conséquence pratique : ne jamais comparer directement les taux "
       "d’ouverture de pays de tailles très différentes."),

f(id='q21-n43', sp='c21-10', niv='appliquer', type='qcm', b=3525,
  q="Le taux d’ouverture chinois diminue depuis environ 2008, après avoir "
    "atteint environ 40 %. Comment l’interpréter ?",
  opts=["La Chine se ferme progressivement aux échanges internationaux",
        "C’est en partie l’effet de sa montée en gamme : elle produit "
        "désormais davantage d’intrants sur son territoire, de sorte que sa "
        "valeur ajoutée domestique augmente relativement aux flux bruts",
        "Ses exportations se sont effondrées",
        "Son PIB a été révisé à la baisse"],
  ans=1,
  why=["La Chine reste un acteur systémique du commerce mondial : elle ne se "
       "ferme pas.",
       "Ses exportations continuent de progresser.",
       "Aucune révision statistique n’est en cause."],
  exp="C’est l’un des résultats les plus contre-intuitifs du chapitre : "
      "valeur ajoutée domestique ↑ → PIB ↑ relativement aux flux bruts → "
      "taux d’ouverture ↓. La baisse de l’indicateur traduit donc un progrès "
      "productif, et non un repli. Elle illustre à quel point les "
      "statistiques brutes peuvent être trompeuses dans une économie "
      "fragmentée.",
  diss="Exemple idéal pour montrer la nécessité du commerce en valeur "
       "ajoutée : le même chiffre peut signifier deux choses opposées."),

f(id='q21-n44', sp='c21-10', niv='comprendre', type='assoc', b=3662,
  q="Associez chaque situation au type d’insertion dans les chaînes de valeur "
    "mondiales qu’elle décrit.",
  ans=[["Fournir des intrants fondamentaux utilisés dans les étapes suivantes de la production mondiale", "Une insertion en amont"],
       ["Les exportateurs de matières premières, peu dépendants d’intrants étrangers mais très dépendants de la demande mondiale", "Une insertion en amont"],
       ["Se spécialiser dans l’assemblage de composants importés avant réexportation", "Une insertion en aval"],
       ["Les pays ateliers, dont une grande part de la valeur exportée provient de composants importés", "Une insertion en aval"]],
  exp="La part de valeur ajoutée étrangère dans les exportations permet de "
      "repérer ces positions : plus elle est élevée, plus le pays dépend "
      "d’intrants étrangers pour produire ses exportations. Les pays avancés "
      "occupent une position intermédiaire, utilisant des intrants étrangers "
      "tout en conservant une forte capacité domestique de production à haute "
      "valeur ajoutée.",
  diss="La Chine illustre une trajectoire non linéaire, « en cloche » : "
       "intégration croissante dans les années 1990-2000, accélérée par "
       "l’adhésion à l’OMC en 2001, puis réinternalisation progressive avec la "
       "montée en gamme."),

# ------------------------------------------------------------- c21-11
f(id='q21-n45', sp='c21-11', niv='comprendre', type='qcm', b=3811,
  q="Que traduit la baisse de la part de valeur ajoutée domestique dans les "
    "exportations des grandes économies européennes, passée d’environ 85-90 % "
    "dans les années 1960 à près de 70 % aujourd’hui ?",
  opts=["Une perte de compétitivité absolue de l’industrie européenne",
        "L’internationalisation croissante des processus productifs et une "
        "dépendance accrue aux intrants étrangers",
        "Une erreur de mesure liée aux taux de change",
        "Une baisse du volume des exportations européennes"],
  ans=1,
  why=["La compétitivité peut être en cause mais l’indicateur mesure autre "
       "chose : la composition de la valeur exportée.",
       "La mesure repose sur les tableaux entrées-sorties, non sur les taux "
       "de change.",
       "Les volumes exportés ont augmenté : c’est leur contenu qui change."],
  exp="C’est la mesure du « made in » domestique : quelle part de la valeur "
      "exportée a réellement été produite sur le territoire national ? Sa "
      "baisse signifie que produire pour l’exportation suppose désormais "
      "d’importer davantage. Cette dépendance devient problématique lorsqu’elle "
      "porte sur des matériaux critiques, dont l’interruption "
      "d’approvisionnement peut perturber des secteurs entiers.",
  diss="Articulation forte : efficacité productive et vulnérabilité "
       "stratégique progressent ensemble."),

f(id='q21-n46', sp='c21-11', niv='appliquer', type='qcm', b=3836,
  q="En quoi l’exemple des infrastructures de paiement montre-t-il que la "
    "dépendance ne concerne pas seulement l’industrie ?",
  opts=["Parce que les services financiers sont par nature non échangeables",
        "Parce que les paiements dématérialisés internationaux reposent "
        "largement sur des infrastructures dominées par des acteurs "
        "étrangers, ce qui pose une question de souveraineté",
        "Parce que les banques européennes refusent d’investir dans ce "
        "secteur",
        "Parce que les paiements électroniques sont interdits hors de "
        "l’Europe"],
  ans=1,
  why=["Au contraire : le cours souligne que de nombreux services sont "
       "devenus internationalement échangeables.",
       "Le cours n’évoque aucun refus d’investissement.",
       "Aucune interdiction de ce type n’existe."],
  exp="On pourrait croire les services moins dépendants d’intrants "
      "étrangers, alors que les pays avancés sont dominés par le tertiaire. "
      "L’exemple des paiements montre le contraire, avec un mécanisme "
      "auto-renforçant : plus un moyen de paiement est accepté, plus il "
      "devient pratique, donc plus de commerçants l’acceptent et plus de "
      "consommateurs l’utilisent — plus il devient dominant.",
  diss="Lien direct avec les effets de réseau étudiés en première année : la "
       "dépendance n’est pas seulement productive, elle est aussi "
       "institutionnelle."),

f(id='q21-n47', sp='c21-11', niv='connaitre', type='qcm', b=3898,
  q="Qu’est-ce que le RCEP, et quelle est son importance ?",
  opts=["Un accord monétaire asiatique créant une monnaie commune",
        "Un vaste espace de libre-échange asiatique qui renforce "
        "l’intégration productive régionale et représente environ un tiers de "
        "l’économie mondiale",
        "Un fonds d’investissement chinois destiné aux infrastructures",
        "Une organisation de régulation des matières premières"],
  ans=1,
  why=["Aucune monnaie commune n’est en jeu.",
       "Les financements d’infrastructures relèvent plutôt des Nouvelles "
       "routes de la soie.",
       "Ce n’est pas une organisation de producteurs."],
  exp="L’Asie connaît une intégration régionale organisée autour de la "
      "Chine, que le modèle d’Akamatsu éclaire : l’industrialisation "
      "asiatique repose sur une diffusion régionale de la production et des "
      "avantages comparatifs entre économies successivement intégrées. Mais "
      "cette intégration signifie aussi qu’un ralentissement chinois se "
      "diffuse rapidement aux partenaires.",
  diss="À retenir avec l’ASEAN : la régionalisation n’est pas seulement "
       "européenne ou américaine."),

f(id='q21-n48', sp='c21-11', niv='raisonner', type='qcm', b=3921,
  q="Par quels canaux un ralentissement chinois se diffuse-t-il à ses "
    "partenaires ?",
  opts=["Uniquement par un canal monétaire, via le taux de change du yuan",
        "Par un canal commercial, combinant un effet volume — la baisse des "
        "importations chinoises réduit les exportations des partenaires — et "
        "un effet prix — la baisse de la demande chinoise fait baisser les "
        "cours mondiaux —, et par un canal financier, via les IDE, les prêts "
        "et le financement d’infrastructures",
        "Uniquement par le canal des migrations de travail",
        "Par le seul canal des matières premières agricoles"],
  ans=1,
  why=["Le taux de change joue un rôle mais ne résume pas la transmission.",
       "Les migrations ne sont pas le canal retenu ici.",
       "L’effet prix touche de nombreuses matières premières, pas seulement "
       "l’agriculture."],
  exp="La Chine pèse si lourd sur certains marchés que la baisse de sa "
      "demande fait baisser les cours mondiaux : les partenaires subissent "
      "donc simultanément une baisse des quantités exportées et des prix. Le "
      "canal financier ajoute une vulnérabilité : les prêts chinois, notamment "
      "autour de l’initiative des Nouvelles routes de la soie, peuvent "
      "soutenir l’investissement mais accroître fortement l’endettement "
      "extérieur des pays bénéficiaires.",
  diss="Conséquence majeure : la Chine est devenue un acteur systémique, "
       "c’est-à-dire que ses difficultés internes sont des chocs "
       "internationaux."),

f(id='q21-n49', sp='c21-11', niv='raisonner', type='qcm', b=3991,
  q="Pourquoi les chaînes de valeur mondiales rendent-elles le "
    "protectionnisme plus complexe ?",
  opts=["Parce que les droits de douane sont désormais interdits par l’OMC",
        "Parce que les entreprises nationales importent elles-mêmes leurs "
        "intrants : taxer les importations élève leurs coûts de production et "
        "peut donc réduire leur compétitivité",
        "Parce que le protectionnisme fait toujours baisser les prix",
        "Parce que les chaînes de valeur ne concernent que les services"],
  ans=1,
  why=["Les droits de douane restent licites dans les limites des "
       "engagements pris : le retour tarifaire récent le montre.",
       "Le protectionnisme tend au contraire à élever les prix intérieurs.",
       "Les chaînes de valeur concernent d’abord les biens industriels."],
  exp="Le raisonnement traditionnel suppose que taxer les importations "
      "protège le producteur national. Dans une économie fragmentée, la "
      "distinction entre protéger les producteurs et taxer les importations "
      "se brouille, puisque les producteurs nationaux sont eux-mêmes "
      "importateurs : droits de douane sur les intrants → coût de production "
      "↑ → compétitivité ↓. C’est l’une des difficultés des droits de douane "
      "généralisés.",
  diss="Argument technique très efficace contre un protectionnisme "
       "indifférencié, à distinguer d’un protectionnisme ciblé sur des "
       "secteurs stratégiques."),

# ------------------------------------------------------------- c21-12
f(id='q21-n50', sp='c21-12', niv='connaitre', type='ordre', b=4074,
  q="Remettez dans l’ordre les grandes vagues de la mondialisation telles que "
    "le cours les distingue.",
  ans=["La première mondialisation : environ 1870-1913",
       "Le repli et la démondialisation : de 1914 à l’après-Seconde Guerre "
       "mondiale",
       "La remondialisation progressive : après 1945",
       "L’hypermondialisation : surtout des années 1980 à 2008",
       "Le ralentissement et la recomposition : depuis 2008"],
  exp="Cette périodisation interdit de penser la mondialisation comme un "
      "processus continu et irréversible : l’histoire est faite de vagues "
      "successives d’ouverture, de fermeture et de recomposition. C’est la "
      "première leçon que le cours tire de l’étude de la première "
      "mondialisation.",
  diss="Chronologie à maîtriser absolument : elle structure toute "
       "dissertation sur l’histoire de la mondialisation."),

f(id='q21-n51', sp='c21-12', niv='comprendre', type='qcm', b=4094,
  q="Pourquoi la première mondialisation ne correspond-elle pas au début des "
    "échanges internationaux ?",
  opts=["Parce que les échanges internationaux n’existaient pas avant 1870",
        "Parce que des réseaux commerciaux anciens existaient — Méditerranée, "
        "océan Indien, routes terrestres, puis axe atlantique après 1492 : ce "
        "qui change, c’est l’intensité, la géographie, la généralisation et "
        "l’impact économique des échanges",
        "Parce que la première mondialisation est purement financière",
        "Parce que seuls les pays européens échangeaient avant 1870"],
  ans=1,
  why=["Les échanges sont très anciens : c’est leur ampleur qui change.",
       "Elle est d’abord commerciale, selon la configuration internationale "
       "de Michalet.",
       "De nombreux réseaux non européens existaient, notamment dans l’océan "
       "Indien."],
  exp="À partir des grandes découvertes, le centre de gravité du commerce se "
      "déplace vers l’Atlantique et renforce la domination européenne, avec "
      "le commerce triangulaire, exemple de mondialisation ancienne fondée "
      "sur des rapports de domination, des migrations forcées et "
      "l’exploitation coloniale. Mais ces échanges portaient souvent sur des "
      "biens complémentaires et non concurrents, ce qui limitait la "
      "convergence des prix et l’intégration réelle des marchés.",
  diss="Critère décisif de l’intégration : la convergence des prix, et non le "
       "simple volume des échanges."),

f(id='q21-n52', sp='c21-12', niv='comprendre', type='qcm', b=4116,
  q="Quelle est la logique mercantiliste du commerce international ?",
  opts=["Une recherche de gains mutuels par la spécialisation",
        "Une compétition entre nations visant à accumuler les métaux précieux "
        "grâce aux excédents commerciaux",
        "Une organisation des échanges par des institutions multilatérales",
        "Une priorité donnée aux importations de biens de consommation"],
  ans=1,
  why=["Les gains mutuels par la spécialisation sont la thèse de Smith et "
       "Ricardo, qui rompent avec le mercantilisme.",
       "Le multilatéralisme institutionnel n’apparaît qu’après 1945.",
       "Le mercantilisme cherche au contraire à limiter les importations."],
  exp="La première mondialisation accompagne le basculement doctrinal du "
      "mercantilisme vers le libre-échange, notamment sous l’influence des "
      "économistes classiques. Mais le cours insiste sur un paradoxe : cette "
      "mondialisation reste profondément structurée par l’impérialisme, le "
      "colonialisme et les rapports de puissance — elle demeure donc "
      "partiellement mercantiliste, les échanges servant la puissance "
      "politique et économique des États.",
  diss="Erreur à éviter : présenter le XIXᵉ siècle comme une période "
       "pleinement libérale."),

f(id='q21-n53', sp='c21-12', niv='appliquer', type='qcm', b=4263,
  q="Entre 1840 et 1913, comment évolue le taux d’ouverture mondial ?",
  opts=["Il passe d’environ 15 % à environ 30 %",
        "Il passe d’environ 5 % à près de 15 %, soit plus qu’un triplement",
        "Il reste stable autour de 10 %",
        "Il diminue sous l’effet du protectionnisme"],
  ans=1,
  why=["Ces valeurs correspondent au passage de la première mondialisation à "
       "l’hypermondialisation.",
       "La hausse est au contraire spectaculaire.",
       "Le protectionnisme persiste, mais l’ouverture progresse fortement "
       "malgré lui."],
  exp="Sur l’ensemble du XIXᵉ siècle jusqu’en 1913, le commerce international "
      "progresse beaucoup plus vite que la production : c’est précisément ce "
      "qui fait monter le taux d’ouverture. Cette ouverture est surtout "
      "portée par les économies européennes, les États-Unis restant "
      "relativement moins dépendants des échanges grâce à l’ampleur de leur "
      "marché intérieur et à une production diversifiée.",
  diss="Comparaison à retenir : environ 15 % en 1913 contre environ 30 % "
       "aujourd’hui — l’hypermondialisation double le maximum historique "
       "antérieur."),

f(id='q21-n54', sp='c21-12', niv='raisonner', type='qcm', b=4323,
  q="Pourquoi l’Europe de la première mondialisation présente-t-elle une "
    "balance commerciale déficitaire malgré sa domination industrielle ?",
  opts=["Parce que son industrie était en réalité peu compétitive",
        "Parce que la valeur de ses importations massives de produits "
        "primaires dépasse son excédent sur les biens manufacturés — mais son "
        "solde courant reste excédentaire grâce aux services et aux revenus de "
        "ses placements extérieurs",
        "Parce qu’elle importait l’essentiel de ses produits manufacturés",
        "Parce que ses exportations étaient taxées par ses partenaires"],
  ans=1,
  why=["Son industrie domine au contraire le commerce mondial de produits "
       "manufacturés, à hauteur d’environ 84 % pour les économies "
       "industrialisées occidentales.",
       "C’est l’inverse : elle exporte les produits manufacturés et importe "
       "les produits primaires.",
       "La fiscalité des partenaires n’est pas l’explication retenue."],
  exp="L’Europe industrielle importe massivement des produits primaires et "
      "exporte des biens manufacturés : c’est la DIT traditionnelle. Son "
      "excédent courant repose sur deux autres postes : les services, avec "
      "une spécialisation précoce du Royaume-Uni dans la finance, la banque, "
      "l’assurance et l’information ; et les revenus du capital tirés de ses "
      "investissements à l’étranger. Elle devient ainsi créancier du reste du "
      "monde.",
  diss="Démonstration parfaite de la distinction solde commercial / solde "
       "courant, directement transposable au cas français contemporain."),

# ------------------------------------------------------------- c21-13
f(id='q21-n55', sp='c21-13', niv='connaitre', type='qcm', b=4469,
  q="Quelle forme prennent majoritairement les mouvements de capitaux de la "
    "première mondialisation ?",
  opts=["Les IDE, qui représentent l’essentiel des flux",
        "Les investissements de portefeuille, qui représentent selon Béraud "
        "environ 80 à 90 % des mouvements de capitaux",
        "Les réserves de change des banques centrales",
        "Les transferts publics entre États"],
  ans=1,
  why=["Les IDE existent mais n’en représentent qu’une faible part : les "
       "premières FMN apparaissent seulement.",
       "Les réserves de change ne sont pas la forme dominante des flux "
       "privés.",
       "Les transferts publics sont marginaux à cette époque."],
  exp="La première mondialisation financière repose donc essentiellement sur "
      "les placements et les prêts. Son ampleur est néanmoins "
      "impressionnante : à la fin du XIXᵉ siècle, près de la moitié de "
      "l’épargne britannique est investie à l’étranger. Ces capitaux "
      "financent les chemins de fer, les ports et les mines des pays neufs — "
      "mais aussi les infrastructures qui permettent l’exploitation et "
      "l’exportation de leurs ressources.",
  diss="Nouveauté historique majeure : le développement d’un pays n’est plus "
       "limité à son épargne nationale."),

f(id='q21-n56', sp='c21-13', niv='comprendre', type='qcm', b=4511,
  q="Qu’est-ce qui distingue le premier dégroupage du second, chez Richard "
    "Baldwin ?",
  opts=["Le premier concerne les biens, le second les services",
        "Le premier sépare le lieu de production du lieu de consommation, "
        "rendu possible par la baisse des coûts de transport ; le second "
        "sépare les différentes étapes du processus productif lui-même",
        "Le premier concerne les pays riches, le second les pays pauvres",
        "Le premier est commercial, le second est monétaire"],
  ans=1,
  why=["La distinction ne porte pas sur la nature des produits.",
       "Les deux dégroupages concernent toutes les économies intégrées.",
       "Les deux relèvent de l’organisation de la production et des "
       "échanges, non de la monnaie."],
  exp="Le concept permet de distinguer précisément la première mondialisation "
      "de l’hypermondialisation : une usine peut produire dans un pays et les "
      "consommateurs se trouver dans un autre — c’est le premier dégroupage ; "
      "mais ce sont ensuite les étapes de fabrication d’un même bien qui se "
      "répartissent entre pays — c’est le second, qui correspond à la DIPP et "
      "transforme le commerce de biens finis en commerce de tâches et de "
      "biens intermédiaires.",
  diss="Outil de comparaison très économique : un seul concept distingue deux "
       "mondialisations."),

f(id='q21-n57', sp='c21-13', niv='appliquer', type='qcmm', b=4660,
  q="Quels facteurs matériels expliquent, selon le cours, l’essor du commerce "
    "lors de la première mondialisation ? (plusieurs réponses)",
  opts=["La quasi-division par dix du coût réel du transport au XIXᵉ siècle, "
        "selon Bairoch",
        "La généralisation du chemin de fer, qui réduit les coûts "
        "d’acheminement terrestres",
        "Le percement des grands canaux, Suez et Panama, qui réduit "
        "distances, délais et risques",
        "Les innovations de conservation et la spécialisation des navires, "
        "qui rendent transportables de nouveaux biens comme la viande "
        "réfrigérée ou le pétrole",
        "La généralisation du libre-échange dans l’ensemble des pays"],
  ans=[0, 1, 2, 3],
  why=["Exacte : c’est le principal moteur matériel identifié par le cours.",
       "Exacte : il connecte les centres de production aux marchés "
       "internationaux.",
       "Exacte : l’intégration des marchés progresse avec la réduction des "
       "distances maritimes.",
       "Exacte : la mondialisation s’élargit à des produits auparavant "
       "difficilement échangeables.",
       "Bairoch montre justement que le XIXᵉ siècle n’est pas le siècle du "
       "libre-échange : le protectionnisme demeure largement la norme."],
  exp="Le cours ajoute la révolution des communications, avec le câble "
      "transatlantique en 1865, qui réduit les coûts d’information et permet "
      "aux marchés de fonctionner de manière beaucoup plus intégrée. "
      "L’enchaînement est explicite : coûts de transport ↓ → échanges "
      "rentables ↑ → commerce international ↑ → taux d’ouverture ↑.",
  diss="Première grande leçon du chapitre : technologie > volonté politique. "
       "Une forte progression des échanges peut se produire sans "
       "généralisation du libre-échange."),

f(id='q21-n58', sp='c21-13', niv='comprendre', type='qcm', b=4730,
  q="Qu’appelle-t-on loi du prix unique, et pourquoi émerge-t-elle avec la "
    "première mondialisation ?",
  opts=["Une réglementation imposant un prix identique dans tous les pays",
        "Le constat que les possibilités d’arbitrage, facilitées par la baisse "
        "des coûts de transport, limitent durablement les écarts de prix "
        "entre marchés nationaux",
        "L’obligation pour les exportateurs de pratiquer un prix unique",
        "Le fait que tous les biens finissent par avoir le même prix"],
  ans=1,
  why=["Il ne s’agit pas d’une règle juridique mais d’un résultat de "
       "marché.",
       "Aucune obligation ne pèse sur les exportateurs.",
       "La loi porte sur un même bien dans différents lieux, non sur des "
       "biens différents."],
  exp="La baisse des coûts de transport rend l’arbitrage international "
      "rentable : si un même bien est beaucoup moins cher dans un pays, il "
      "devient profitable de l’y acheter pour le revendre ailleurs, ce qui "
      "rapproche les prix. La convergence des prix est précisément le signe "
      "d’une intégration réelle des marchés, et non d’une simple hausse des "
      "flux.",
  diss="Deuxième leçon à citer : ouverture et intégration ne sont pas la même "
       "chose — la première mesure l’intensité des flux, la seconde leurs "
       "effets sur la convergence."),

f(id='q21-n59', sp='c21-13', niv='comprendre', type='assoc', b=4744,
  q="Associez chaque auteur ou mesure à l’argument protectionniste "
    "correspondant.",
  ans=[["Alexander Hamilton, 1791", "Protéger les producteurs américains de la concurrence britannique et financer l’industrie nationale"],
       ["Friedrich List, 1841", "Le protectionnisme éducateur : une industrie naissante doit être temporairement protégée avant d’affronter la concurrence"],
       ["Les Corn Laws britanniques, à partir de 1815", "Un protectionnisme agricole défendant les revenus des propriétaires fonciers contre le blé étranger"],
       ["Le tarif Méline, 1892", "Le retour français au protectionnisme pour protéger agriculteurs et industriels"]],
  exp="Le cours ajoute une justification souvent oubliée : les droits de "
      "douane constituent une ressource fiscale importante. Le Royaume-Uni "
      "peut adopter plus facilement le libre-échange parce que son avance "
      "industrielle le lui permet et qu’il bénéficie de matières premières "
      "importées à moindre coût — et Ricardo défend l’abolition des Corn Laws "
      "pour contenir le coût des subsistances, donc les salaires, et "
      "préserver les profits nécessaires à l’accumulation.",
  diss="Étape clé de la libéralisation : le traité Cobden-Chevalier de 1860 "
       "et la diffusion de la clause de la nation la plus favorisée, qui "
       "préfigure le multilatéralisme d’après 1945."),

]
