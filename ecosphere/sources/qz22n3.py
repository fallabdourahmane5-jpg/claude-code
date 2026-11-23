# -*- coding: utf-8 -*-
"""Chapitre 22 — questions nouvelles, sous-parties c22-17 et c22-18."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c22-17
f(id='q22-n52', sp='c22-17', niv='comprendre', type='qcm', b=6200,
  q="Pourquoi la transition écologique ne signifie-t-elle pas la disparition "
    "de l’industrie ?",
  opts=["Parce que l’industrie émet moins de gaz à effet de serre que les "
        "services",
        "Parce que les technologies nécessaires à la transition doivent "
        "elles-mêmes être produites industriellement",
        "Parce que la consommation de biens manufacturés va cesser",
        "Parce que les normes environnementales interdisent les importations"],
  ans=1,
  why=["L’industrie émet au contraire généralement davantage de gaz à effet "
       "de serre que les services : c’est précisément l’objection à laquelle "
       "le cours répond.",
       "Rien n’indique une disparition de la consommation de biens.",
       "Aucune interdiction générale d’importer n’existe."],
  exp="Décarboner l’économie suppose de développer les capacités "
      "industrielles capables de produire les technologies du changement de "
      "modèle énergétique : batteries, véhicules électriques, pompes à "
      "chaleur, énergies renouvelables, nucléaire, captage du carbone, "
      "recyclage. L’enchaînement est le suivant : transition écologique → "
      "besoin de nouvelles technologies → besoin de capacités industrielles → "
      "soutien public ciblé → politique industrielle verte.",
  diss="Reformulation utilisable : la transition ne supprime pas "
       "l’industrie, elle en change le contenu."),

f(id='q22-n53', sp='c22-17', niv='raisonner', type='qcm', b=6223,
  q="Pourquoi une relocalisation industrielle dans un pays avancé peut-elle "
    "augmenter les émissions territoriales tout en réduisant les émissions "
    "mondiales ?",
  opts=["Parce que les émissions territoriales ne sont pas mesurables",
        "Parce que produire sur le territoire y ajoute des émissions, mais "
        "remplace une production étrangère beaucoup plus carbonée",
        "Parce que le transport maritime n’émet aucun gaz à effet de serre",
        "Parce que les pays avancés ne comptabilisent pas leurs émissions "
        "industrielles"],
  ans=1,
  why=["Les émissions territoriales sont précisément ce que mesurent les "
       "inventaires nationaux.",
       "Le transport émet des gaz à effet de serre : c’est d’ailleurs l’un "
       "des arguments en faveur du rapprochement de la production.",
       "Les émissions industrielles sont bien comptabilisées dans les pays "
       "avancés."],
  exp="Deux mécanismes jouent. D’abord, produire plus près des consommateurs "
      "réduit les émissions liées au transport. Ensuite, les pays avancés "
      "disposent souvent de réglementations environnementales plus strictes, "
      "de technologies propres et d’une électricité moins carbonée. Une "
      "relocalisation peut donc augmenter les émissions comptabilisées sur le "
      "territoire national tout en réduisant l’empreinte carbone mondiale, si "
      "elle substitue à une production très carbonée une production moins "
      "émettrice.",
  diss="Distinction indispensable : émissions territoriales et empreinte "
       "carbone ne se confondent pas, et les conclusions politiques diffèrent "
       "selon l’indicateur retenu."),

f(id='q22-n54', sp='c22-17', niv='connaitre', type='qcm', b=6226,
  q="Comment le cours définit-il une politique industrielle verte ?",
  opts=["Une politique horizontale améliorant l’environnement général des "
        "entreprises",
        "Une politique industrielle verticale ciblant les activités "
        "nécessaires à la transition écologique",
        "Une taxe carbone appliquée uniformément à tous les secteurs",
        "Une politique de réduction de la consommation des ménages"],
  ans=1,
  why=["La politique verte est au contraire ciblée, donc verticale.",
       "Une taxe carbone uniforme est un instrument de prix, non une "
       "politique industrielle ciblée.",
       "La réduction de la consommation relève de la politique de la "
       "demande."],
  exp="Le verdissement de la politique industrielle consiste à orienter "
      "volontairement les investissements vers les secteurs susceptibles de "
      "rendre possible la décarbonation de la production et de la "
      "consommation. Le mécanisme attendu est le suivant : État → soutien aux "
      "technologies vertes → investissement privé ↑ → capacités productives ↑ "
      "→ diffusion des technologies bas carbone → émissions potentielles ↓.",
  diss="Point fort du raisonnement : la transition écologique réhabilite "
       "précisément le type de politique — verticale et ciblée — que les "
       "années 1980 avaient disqualifié."),

f(id='q22-n55', sp='c22-17', niv='comprendre', type='qcm', b=6255,
  q="Sur quel principe repose le système d’aides de l’Inflation Reduction "
    "Act ?",
  opts=["Les aides sont identiques quelle que soit la localisation de la "
        "production",
        "Plus la chaîne de valeur est localisée aux États-Unis, plus les "
        "aides dont peuvent bénéficier l’entreprise ou le consommateur sont "
        "importantes",
        "Les aides sont réservées aux entreprises étrangères investissant aux "
        "États-Unis",
        "Les aides sont versées uniquement sous forme de prêts remboursables"],
  ans=1,
  why=["L’uniformité supprimerait l’incitation à la relocalisation, qui est "
       "l’objet du dispositif.",
       "Les aides ne sont pas réservées aux entreprises étrangères : le "
       "critère est la localisation de la production.",
       "La forme juridique des aides n’est pas le principe structurant."],
  exp="Le dispositif conditionne le montant des aides à la part de la valeur "
      "ajoutée ou des intrants produits sur le territoire américain : c’est "
      "une logique de contenu local. L’enchaînement visé est le suivant : "
      "aides publiques → préférence pour le contenu local → investissements "
      "industriels aux États-Unis ↑ → capacités nationales ↑ → dépendance "
      "extérieure ↓. Une politique présentée comme écologique devient donc "
      "simultanément un instrument de relocalisation, de souveraineté et de "
      "compétition internationale.",
  diss="Mot-clé à employer : hybridation des objectifs — climat, "
       "souveraineté et puissance dans un seul dispositif."),

f(id='q22-n56', sp='c22-17', niv='comprendre', type='qcm', b=6272,
  q="Quelle dimension le CHIPS Act ajoute-t-il à la politique industrielle "
    "contemporaine ?",
  opts=["Il se limite à financer la recherche fondamentale",
        "Il sert aussi à ralentir l’accès des puissances rivales aux "
        "technologies considérées comme stratégiques",
        "Il interdit toute exportation américaine de semi-conducteurs",
        "Il supprime les aides aux entreprises américaines du secteur"],
  ans=1,
  why=["Le financement de la recherche en fait partie, mais ne résume pas la "
       "portée du dispositif.",
       "Il ne s’agit pas d’une interdiction générale d’exporter.",
       "Le dispositif soutient au contraire les entreprises américaines du "
       "secteur."],
  exp="Le CHIPS Act montre que la politique industrielle contemporaine ne se "
      "limite plus à soutenir l’innovation nationale : elle sert aussi à "
      "ralentir l’accès des puissances rivales aux technologies stratégiques. "
      "L’enjeu central devient la maîtrise de la frontière technologique, ce "
      "qui place la politique industrielle au cœur de la géoéconomie — "
      "l’utilisation d’instruments économiques au service d’objectifs de "
      "puissance.",
  diss="Articulation forte : avec le CHIPS Act, la politique industrielle "
       "devient offensive, et non plus seulement protectrice."),

f(id='q22-n57', sp='c22-17', niv='connaitre', type='qcm', b=6286,
  q="Quel objectif chiffré l’Industrial Accelerator Act, présenté le 4 mars "
    "2026, fixe-t-il à l’industrie européenne ?",
  opts=["Porter la part de l’industrie dans le PIB européen d’environ 14,3 % "
        "à 20 % en 2035",
        "Porter la part de l’industrie à 30 % du PIB dès 2030",
        "Maintenir la part de l’industrie à son niveau actuel",
        "Réduire la part de l’industrie au profit des services"],
  ans=0,
  why=["Aucun objectif de 30 % en 2030 n’est formulé.",
       "Le projet vise une progression, non un maintien.",
       "L’objectif est exactement inverse : réindustrialiser."],
  exp="L’Industrial Accelerator Act est présenté le 4 mars 2026, associé à "
      "une logique « Made in Europe ». Il s’agit encore d’un projet en "
      "discussion, donc pas pleinement appliqué. Son objectif général est de "
      "réindustrialiser l’Union européenne, avec une cible précise : faire "
      "passer la part de l’industrie dans le PIB européen d’environ 14,3 % "
      "aujourd’hui à 20 % en 2035.",
  diss="Prudence de méthode à conserver : il s’agit d’un projet en "
       "discussion, ce qui doit être mentionné quand on le cite."),

f(id='q22-n58', sp='c22-17', niv='comprendre', type='qcmm', b=6303,
  q="Quels secteurs la préférence européenne envisagée par ce projet cible-t-"
    "elle particulièrement ? (plusieurs réponses)",
  opts=["L’aluminium, le ciment et l’acier",
        "L’automobile électrique et les batteries",
        "L’éolien et les pompes à chaleur",
        "Le nucléaire et les technologies propres",
        "Le tourisme et la restauration"],
  ans=[0, 1, 2, 3],
  why=["Exacte : ces matériaux de base sont intensifs en énergie et "
       "stratégiques.",
       "Exacte : ce sont les filières au cœur de la transition automobile.",
       "Exacte : elles relèvent des équipements de la transition "
       "énergétique.",
       "Exacte : production d’énergie décarbonée et technologies propres sont "
       "visées.",
       "Inexacte : ces activités de services ne sont pas concernées par une "
       "logique de contenu local industriel."],
  exp="La préférence européenne concerne les marchés publics, certaines aides "
      "à la production et les financements publics : lorsque de l’argent "
      "public est mobilisé, il doit davantage servir la production "
      "européenne. On se rapproche ainsi d’une logique de contenu local, "
      "comparable à celle du Buy American Act américain, qui réserve une "
      "place à la production nationale dans certaines commandes publiques "
      "fédérales.",
  diss="Rupture doctrinale à souligner : l’origine géographique de la "
       "production devient un critère, alors que l’Union défendait une "
       "neutralité concurrentielle."),

f(id='q22-n59', sp='c22-17', niv='appliquer', type='qcmm', b=6377,
  q="Quelles contreparties le projet européen envisage-t-il d’exiger de "
    "certains investisseurs étrangers ? (plusieurs réponses)",
  opts=["Consacrer environ 1 % de leur chiffre d’affaires mondial à la R&D "
        "dans l’Union européenne",
        "Acheter au moins 30 % de leurs composants dans la chaîne de valeur "
        "européenne",
        "Créer des emplois européens, pour éviter une implantation ne "
        "bénéficiant que marginalement au marché du travail",
        "Accepter qu’une entité européenne reste majoritaire dans certains "
        "cas",
        "Renoncer à toute activité commerciale hors de l’Union européenne"],
  ans=[0, 1, 2, 3],
  why=["Exacte : l’exigence porte sur l’effort de recherche réalisé en "
       "Europe.",
       "Exacte : elle vise les effets d’entraînement sur les fournisseurs "
       "européens.",
       "Exacte : c’est l’objectif d’entraînement local recherché.",
       "Exacte : la structure du capital fait partie des points envisagés.",
       "Inexacte : aucune restriction de ce type n’est envisagée."],
  exp="Le projet envisage un encadrement renforcé de certains IDE très "
      "importants dans les secteurs stratégiques, notamment au-delà de 100 "
      "millions d’euros ou lorsqu’une part très importante du marché mondial "
      "est en jeu. L’Europe cherche ainsi à transformer l’IDE d’une simple "
      "entrée de capital en instrument de développement industriel : "
      "l’investissement étranger doit générer emplois, R&D, transferts "
      "technologiques et commandes pour les fournisseurs européens.",
  diss="Renversement notable : ces exigences rappellent des stratégies "
       "utilisées historiquement par la Chine pour accueillir les IDE "
       "étrangers."),

f(id='q22-n60', sp='c22-17', niv='raisonner', type='courte', b=6421,
  q="Pourquoi peut-on parler d’un moment de bascule du modèle européen ?",
  ans={'modele': "Historiquement, l’Union européenne s’est construite autour "
       "de la concurrence, de l’ouverture commerciale et d’une relative "
       "neutralité vis-à-vis de l’origine du capital : la priorité allait au "
       "bien-être du consommateur, selon l’enchaînement concurrence → prix ↓ "
       "→ innovation ↑ → productivité ↑. Les politiques désormais envisagées "
       "introduisent une logique différente : une préférence européenne dans "
       "les marchés publics et les aides, un conditionnement de certains "
       "investissements étrangers, des exigences de R&D et de contenu "
       "européen, un contrôle accru des prises de participation étrangères, "
       "une simplification administrative destinée à accélérer les "
       "investissements, et éventuellement des droits de douane plus élevés. "
       "On passe donc d’une logique « concurrence et ouverture » à une "
       "logique « souveraineté, préférence européenne et politique "
       "industrielle verticale ». La bascule n’est pas acquise, puisqu’il "
       "s’agit encore d’un projet en discussion, mais sa direction est "
       "nette.",
       'cles': [{'f': ['concurrence', 'ouverture', 'neutralite', 'consommateur'],
                 'l': "l'ancienne doctrine : concurrence, ouverture, neutralité"},
                {'f': ['preference europeenne', 'contenu local', 'marche public'],
                 'l': "la préférence européenne dans l'argent public"},
                {'f': ['conditionn', 'ide', 'investissement etranger', 'controle'],
                 'l': "le conditionnement des investissements étrangers"},
                {'f': ['souverainete', 'securite', 'reindustrialisation'],
                 'l': "la priorité donnée à la souveraineté et à la réindustrialisation"},
                {'f': ['verticale', 'cible', 'politique industrielle'],
                 'l': "le retour d'une politique industrielle verticale"},
                {'f': ['projet', 'discussion', 'pas encore', 'envisage'],
                 'l': "une bascule encore à l'état de projet"}]},
  exp="L’Union européenne semble entrer dans une phase de redéfinition "
      "profonde de son modèle : la priorité donnée depuis des décennies à la "
      "concurrence et à l’ouverture commerciale est progressivement "
      "concurrencée par des objectifs de souveraineté, de sécurité et de "
      "réindustrialisation.",
  diss="Sujet de dissertation presque tout fait : l’Europe peut-elle "
       "concilier politique de concurrence et politique industrielle ?"),

f(id='q22-n61', sp='c22-17', niv='comprendre', type='qcm', b=6524,
  q="Que désigne la « greenflation » ?",
  opts=["La baisse des prix provoquée par les énergies renouvelables",
        "Une hausse des prix liée directement ou indirectement à la "
        "transition écologique",
        "L’inflation causée par la hausse des salaires industriels",
        "La hausse des prix alimentaires liée au climat uniquement"],
  ans=1,
  why=["Le cours décrit un effet inflationniste, non déflationniste.",
       "La dynamique salariale est une autre source d’inflation.",
       "Le phénomène dépasse les seuls prix alimentaires."],
  exp="La transition écologique suppose des investissements considérables, une "
      "substitution à certaines énergies fossiles et le développement de "
      "technologies parfois encore coûteuses. Le mécanisme est le suivant : "
      "transition écologique accélérée → demande de matières premières et "
      "d’investissements ↑ → coûts ↑ → inflation potentielle. Plus largement, "
      "une production relocalisée dans les pays avancés peut être plus "
      "coûteuse et soumise à des exigences environnementales plus strictes, "
      "ce qui crée une tension avec l’objectif de stabilité des prix poursuivi "
      "par la banque centrale.",
  diss="Contradiction à exploiter : la politique industrielle verte peut "
       "entrer en conflit avec la politique monétaire."),

f(id='q22-n62', sp='c22-17', niv='raisonner', type='ordre', b=6550,
  q="Remettez dans l’ordre l’enchaînement de la course aux subventions entre "
    "grandes puissances.",
  ans=["Les États-Unis mettent en place des subventions massives en faveur de "
       "certaines industries stratégiques",
       "Des investissements sont attirés vers le territoire américain",
       "L’Union européenne réagit pour éviter le départ de ses "
       "investissements",
       "De nouvelles aides européennes sont annoncées",
       "D’autres pays réagissent à leur tour, et une course aux subventions "
       "s’installe"],
  exp="Lorsque plusieurs puissances utilisent simultanément les subventions et "
      "les préférences nationales pour attirer les mêmes industries "
      "stratégiques, la politique industrielle devient un instrument de "
      "rivalité internationale. Chacun dépense davantage pour un avantage net "
      "faible : la structure est exactement celle de la concurrence fiscale, "
      "c’est-à-dire un dilemme du prisonnier.",
  diss="Rapprochement payant : concurrence fiscale et course aux subventions "
       "sont deux formes du même piège collectif."),

f(id='q22-n63', sp='c22-17', niv='comprendre', type='qcm', b=6557,
  q="Pourquoi certaines mesures de politique industrielle posent-elles un "
    "problème au regard des règles du commerce international ?",
  opts=["Parce qu’elles sont toujours moins efficaces que le libre-échange",
        "Parce que les échanges internationaux reposent, depuis le GATT de "
        "1947 puis l’OMC, sur des règles communes avec lesquelles les "
        "préférences nationales et certaines subventions entrent en "
        "contradiction",
        "Parce qu’elles nécessitent l’accord unanime des États membres de "
        "l’OMC",
        "Parce qu’elles sont incompatibles avec la souveraineté budgétaire"],
  ans=1,
  why=["L’efficacité comparée est un autre débat, et le cours ne tranche pas "
       "en ces termes.",
       "Les politiques industrielles nationales ne requièrent pas "
       "l’unanimité à l’OMC.",
       "La souveraineté budgétaire n’est pas en cause : ces politiques en "
       "sont au contraire l’expression."],
  exp="Depuis le GATT de 1947 puis la création de l’OMC, les échanges "
      "internationaux reposent sur des règles communes, notamment la "
      "non-discrimination. Or la préférence nationale dans les marchés "
      "publics, le contenu local conditionnant les aides ou les subventions "
      "ciblées entrent en tension avec ces principes. L’affaiblissement de "
      "l’Organe de règlement des différends rend par ailleurs ces tensions "
      "plus difficiles à arbitrer.",
  diss="À articuler avec le Pilier 2 de l’OCDE : dans un cas la coordination "
       "progresse, dans l’autre elle s’affaiblit."),

# ------------------------------------------------------------- c22-18
f(id='q22-n64', sp='c22-18', niv='connaitre', type='qcm', b=6674,
  q="Qu’est-ce qu’un effet de réseau ?",
  opts=["Une baisse du coût unitaire liée à l’augmentation des quantités "
        "produites",
        "Une situation dans laquelle la valeur d’un produit ou d’un service "
        "augmente avec le nombre de ses utilisateurs",
        "Un accord entre entreprises d’un même secteur",
        "Une dépendance à l’égard d’un fournisseur unique"],
  ans=1,
  why=["La baisse du coût unitaire avec les quantités définit les économies "
       "d’échelle classiques, du côté de l’offre.",
       "Un accord entre entreprises est une entente, tout autre chose.",
       "La dépendance à un fournisseur unique est un problème "
       "d’approvisionnement."],
  exp="Le cours propose d’interpréter l’effet de réseau comme une forme "
      "d’économie d’échelle du côté de la demande : ce n’est pas la "
      "production qui devient moins coûteuse, c’est le service qui devient "
      "plus utile à mesure que les utilisateurs se multiplient. Les "
      "plateformes numériques, le cloud, les réseaux sociaux et certains "
      "services d’intelligence artificielle en relèvent directement.",
  diss="Expression à employer telle quelle : économie d’échelle du côté de la "
       "demande."),

f(id='q22-n65', sp='c22-18', niv='appliquer', type='ordre', b=6690,
  q="Remettez dans l’ordre le cercle qui renforce un acteur numérique déjà "
    "dominant.",
  ans=["Un acteur dispose d’une base d’utilisateurs plus large que ses "
       "concurrents",
       "Il collecte davantage de données",
       "Il améliore son service et ses coûts moyens peuvent diminuer",
       "Il attire de nouveaux utilisateurs",
       "Sa domination se renforce encore"],
  exp="C’est le mécanisme du cours : grand acteur → davantage d’utilisateurs "
      "→ service amélioré → nouveaux utilisateurs → domination renforcée. "
      "Dans les industries numériques, le retard initial peut donc "
      "s’auto-entretenir : les effets de réseau renforcent les entreprises "
      "déjà dominantes et rendent coûteuse l’émergence tardive de concurrents "
      "européens.",
  diss="Conséquence pour la politique industrielle : dans ces secteurs, "
       "arriver tard coûte beaucoup plus cher qu’ailleurs, ce qui plaide pour "
       "une intervention précoce et massive."),

f(id='q22-n66', sp='c22-18', niv='comprendre', type='qcm', b=6710,
  q="En quoi consiste le handicap institutionnel européen en matière de "
    "politique industrielle ?",
  opts=["L’Europe manque de compétences scientifiques",
        "Ses compétences sont fragmentées : sans institution capable de "
        "sélectionner rapidement des priorités et de concentrer les "
        "financements, la juxtaposition des politiques nationales dilue "
        "l’effort",
        "Les États européens refusent toute politique industrielle",
        "L’Union européenne ne dispose d’aucun budget"],
  ans=1,
  why=["Le cours souligne au contraire l’excellence scientifique "
       "européenne : le problème est sa transformation industrielle.",
       "Plusieurs États mènent des politiques industrielles actives.",
       "L’Union dispose d’un budget, même s’il est limité au regard des "
       "programmes américains."],
  exp="Une politique industrielle européenne suppose de coordonner 27 États "
      "dont les intérêts ne sont pas toujours identiques. Le handicap tient "
      "donc moins à l’absence de compétences qu’à leur fragmentation. C’est "
      "aussi ce qui explique le retour régulier de l’idée d’une « DARPA "
      "européenne » : combler l’écart entre l’excellence scientifique "
      "européenne et sa capacité de transformation industrielle, en "
      "concentrant des financements importants sur des projets "
      "technologiques risqués et stratégiques.",
  diss="Diagnostic en une phrase : l’Europe sait découvrir, elle sait moins "
       "industrialiser ses découvertes."),

f(id='q22-n67', sp='c22-18', niv='comprendre', type='assoc', b=6799,
  q="Associez chaque stratégie du trilemme d’Agarwal aux deux objectifs "
    "qu’elle privilégie.",
  ans=[["Stratégie A : des champions nationaux soutenus mais avec des moyens "
        "limités, donc un effet sur la croissance restreint",
        "Champions nationaux et stabilité budgétaire"],
       ["Stratégie B : le « pari audacieux », qui accepte une dégradation des "
        "finances publiques pour financer de très grands programmes",
        "Champions nationaux et forte croissance"],
       ["Stratégie C : un environnement concurrentiel favorable à toutes les "
        "entreprises, sans sélection de champions",
        "Forte croissance et stabilité budgétaire"]],
  exp="Le trilemme oppose trois objectifs : promouvoir des champions "
      "nationaux par la politique industrielle, maintenir la stabilité "
      "financière et budgétaire, et obtenir une forte croissance. Les trois "
      "ne peuvent être maximisés simultanément, d’où trois stratégies "
      "possibles, chacune renonçant à l’un des sommets. Le cours associe "
      "plutôt le « pari audacieux » aux États-Unis, qui peuvent financer de "
      "très grands programmes en acceptant des déficits publics élevés.",
  diss="Lecture très efficace des choix nationaux : demander, pour chaque "
       "pays, auquel des trois sommets il a renoncé."),

f(id='q22-n68', sp='c22-18', niv='raisonner', type='qcm', b=6757,
  q="Quel risque le cours associe-t-il à une politique industrielle "
    "sous-financée ?",
  opts=["Elle provoque nécessairement de l’inflation",
        "Elle disperse les moyens sur une multitude de projets incapables "
        "d’atteindre la taille critique nécessaire pour modifier durablement "
        "la spécialisation productive",
        "Elle entraîne la faillite des entreprises aidées",
        "Elle réduit automatiquement la dette publique"],
  ans=1,
  why=["L’inflation est plutôt le risque d’une politique très expansive, "
       "associée à la greenflation.",
       "La faillite des bénéficiaires n’est pas le mécanisme décrit.",
       "Préserver les finances publiques n’équivaut pas à réduire la dette."],
  exp="C’est la limite de la stratégie A du trilemme : en conservant une "
      "forte discipline budgétaire, l’État limite les moyens consacrés aux "
      "projets industriels, de sorte que leur financement peut être "
      "insuffisant par rapport aux ambitions affichées. Une politique "
      "industrielle sous-financée préserve donc les finances publiques mais "
      "risque de saupoudrer les aides sans atteindre la taille critique.",
  diss="Argument à double tranchant utile en dissertation : trop peu de "
       "moyens disperse, trop de moyens déséquilibre — d’où l’exigence de "
       "sélectivité."),

f(id='q22-n69', sp='c22-18', niv='comprendre', type='qcm', b=6819,
  q="Pourquoi l’Union européenne peut-elle plus difficilement que les "
    "États-Unis financer un « pari audacieux » ?",
  opts=["Parce que les États européens sont plus riches",
        "Parce que sa structure budgétaire est beaucoup plus fragmentée, "
        "tandis que les États-Unis attirent massivement les capitaux mondiaux "
        "et peuvent accepter plus facilement des déficits élevés",
        "Parce que les traités interdisent tout endettement public",
        "Parce qu’elle ne possède pas de monnaie unique"],
  ans=1,
  why=["Le niveau de richesse n’est pas l’argument retenu.",
       "Les traités encadrent les déficits sans interdire l’endettement.",
       "La zone euro dispose d’une monnaie unique : ce n’est pas le "
       "problème soulevé ici."],
  exp="Les États-Unis bénéficient d’un écosystème important de capital-risque "
      "et attirent massivement les capitaux mondiaux, ce qui leur permet "
      "d’accepter plus facilement des déficits élevés. L’Union européenne "
      "dispose d’une capacité d’endettement et d’une architecture budgétaire "
      "différentes, beaucoup plus fragmentées entre États membres : "
      "reproduire simplement le modèle américain y est donc difficile.",
  diss="À relier au chapitre sur le dollar : la capacité de financement "
       "dépend aussi du statut de la monnaie internationale."),

f(id='q22-n70', sp='c22-18', niv='raisonner', type='qcm', b=6848,
  q="Pourquoi le nombre d’usines ouvertes et fermées ne suffit-il pas à "
    "mesurer une réindustrialisation ?",
  opts=["Parce que les statistiques d’ouvertures et de fermetures ne sont pas "
        "publiées",
        "Parce que les usines n’ont pas toutes la même taille : le solde de "
        "l’emploi industriel peut rester légèrement positif malgré davantage "
        "de fermetures que d’ouvertures",
        "Parce que les fermetures sont toujours temporaires",
        "Parce que seules les ouvertures sont comptabilisées"],
  ans=1,
  why=["Ces données existent : le cours en cite les ordres de grandeur.",
       "Rien n’indique que les fermetures soient temporaires.",
       "Les fermetures sont bien comptabilisées, et comparées aux "
       "ouvertures."],
  exp="Pendant quelques années, les ouvertures d’usines dépassaient les "
      "fermetures en France. En 2025 la dynamique s’inverse, avec un ordre de "
      "grandeur d’environ 116 ouvertures contre environ 179 fermetures. Cela "
      "n’implique pourtant pas une baisse équivalente de l’emploi "
      "industriel : une économie peut enregistrer davantage de fermetures que "
      "d’ouvertures tout en créant encore légèrement des emplois industriels "
      "si les nouvelles unités sont plus grandes ou plus productives.",
  diss="Leçon de méthode statistique applicable partout : compter des "
       "établissements n’est pas mesurer de l’emploi."),

f(id='q22-n71', sp='c22-18', niv='appliquer', type='assoc', b=6856,
  q="Classez chaque branche industrielle française selon la dynamique "
    "d’emploi que le cours lui associe.",
  ans=[["Aéronautique", "Secteur qui crée des emplois"],
       ["Production et distribution d’électricité et d’énergie",
        "Secteur qui crée des emplois"],
       ["Gestion des déchets", "Secteur qui crée des emplois"],
       ["Automobile", "Secteur en recul"],
       ["Métallurgie", "Secteur en recul"],
       ["Habillement", "Secteur en recul"]],
  exp="La ligne de partage suit les transitions : les branches liées à "
      "l’énergie, à l’aéronautique et à l’économie circulaire créent des "
      "emplois, tandis que plusieurs secteurs associés à la deuxième "
      "révolution industrielle reculent. L’automobile est l’un des plus "
      "touchés : depuis 2009, plus de 50 000 emplois nets auraient disparu "
      "dans cette branche selon le document présenté.",
  diss="Conclusion à retenir : réindustrialisation éventuelle ne signifie pas "
       "retour de toutes les anciennes industries — il s’agit d’une "
       "transformation structurelle."),

f(id='q22-n72', sp='c22-18', niv='connaitre', type='qcm', b=6874,
  q="Quelles catégories Sarah Guillou distingue-t-elle dans son analyse de la "
    "politique industrielle française (2024) ?",
  opts=["Les causes, les conséquences et les remèdes",
        "Les démons, les dieux et les défis",
        "Le court terme, le moyen terme et le long terme",
        "Les gagnants, les perdants et les indifférents"],
  ans=1,
  why=["Ce découpage n’est pas celui de l’ouvrage.",
       "Les horizons temporels sont évoqués dans l’analyse, mais ne "
       "constituent pas ses catégories.",
       "La distinction gagnants/perdants relève plutôt de Giraud et de "
       "Fontagné."],
  exp="Dans « La politique industrielle française : Démons, Dieux et Défis » "
      "(2024), Sarah Guillou distingue les démons, les dieux et les défis de "
      "la politique industrielle française. Premier démon : la tradition "
      "interventionniste française n’a pas empêché la désindustrialisation — "
      "malgré aides publiques, crédits d’impôt, programmes industriels, "
      "commandes publiques, banques publiques et politiques de R&D, la France "
      "reste l’un des pays européens les plus désindustrialisés.",
  diss="Conclusion forte à citer : le volume des aides n’est pas une garantie "
       "d’efficacité."),

f(id='q22-n73', sp='c22-18', niv='raisonner', type='qcm', b=6923,
  q="En quoi consiste la contradiction temporelle qui affecte la "
    "planification industrielle ?",
  opts=["Les entreprises investissent trop rapidement",
        "Les transformations productives exigent une stratégie stable sur "
        "plusieurs décennies alors que les gouvernements doivent répondre en "
        "permanence à des contraintes de court terme",
        "Les technologies changent trop lentement",
        "Les plans sont publiés trop tôt"],
  ans=1,
  why=["La lenteur de l’investissement industriel est plutôt le problème "
       "inverse.",
       "Les technologies changent rapidement, ce qui aggrave la difficulté "
       "plutôt que de la créer.",
       "La date de publication des plans n’est pas le problème."],
  exp="L’exemple du cours est éclairant : une énergie fossile chère encourage "
      "l’électrification à long terme, mais protéger les ménages de la hausse "
      "de son prix à court terme affaiblit le signal favorable à la "
      "transition. La planification industrielle se heurte donc à une "
      "contradiction temporelle : le long terme est constamment rattrapé par "
      "les urgences sociales et économiques du court terme.",
  diss="Exemple parfait pour une partie sur les limites politiques, et non "
       "seulement économiques, de la politique industrielle."),

f(id='q22-n74', sp='c22-18', niv='raisonner', type='courte', b=6951,
  q="Pourquoi les champions nationaux français constituent-ils à la fois un "
    "atout et une difficulté, selon Sarah Guillou ?",
  ans={'modele': "Ils sont un atout parce que la France dispose de grandes "
       "entreprises internationales, longtemps placées au cœur de sa "
       "politique industrielle, capables d’investir, d’exporter et de "
       "maîtriser des technologies avancées. Mais plusieurs d’entre elles "
       "restent spécialisées dans des technologies dites « mid-tech », "
       "c’est-à-dire des technologies matures, souvent héritées des grandes "
       "industries de la deuxième révolution industrielle. Le risque est donc "
       "de rester performant dans les industries anciennes pendant que la "
       "frontière technologique se déplace vers le numérique, l’intelligence "
       "artificielle, les nouvelles générations de batteries et les "
       "technologies vertes. L’automobile l’illustre : la longue tradition "
       "automobile européenne ne garantit pas la maîtrise du véhicule "
       "électrique, car le passage à cette technologie transforme la chaîne "
       "de valeur. Un ancien avantage comparatif n’est donc pas un avantage "
       "comparatif garanti dans la nouvelle technologie : il doit être "
       "reconstruit.",
       'cles': [{'f': ['grande entreprise', 'champion', 'international',
                       'exporter'],
                 'l': "un atout : de grandes entreprises internationales"},
                {'f': ['mid-tech', 'mid tech', 'mature', 'ancienne'],
                 'l': "un enfermement dans des technologies mid-tech et matures"},
                {'f': ['deuxieme revolution', 'heritee', 'historique'],
                 'l': "un héritage de la deuxième révolution industrielle"},
                {'f': ['frontiere technologique', 'numerique', 'intelligence artificielle',
                       'batterie', 'verte'],
                 'l': "un déplacement de la frontière technologique"},
                {'f': ['automobile', 'vehicule electrique', 'electrique'],
                 'l': "l'automobile et le véhicule électrique comme illustration"},
                {'f': ['reconstruit', 'reconstruire', 'pas garanti', 'construire'],
                 'l': "un avantage comparatif à reconstruire"}]},
  exp="Le défi français n’est plus seulement de préserver ses champions "
      "historiques mais d’éviter que ceux-ci restent enfermés dans le "
      "« mid-tech » pendant que la frontière technologique se déplace vers le "
      "numérique, l’intelligence artificielle et les technologies vertes.",
  diss="Articulation remarquable avec Aghion : la France est proche de la "
       "frontière dans les industries anciennes et éloignée dans les "
       "nouvelles, ce qui complique le choix des instruments."),

f(id='q22-n75', sp='c22-18', niv='raisonner', type='qcm', b=6987,
  q="Comment le cours caractérise-t-il le problème français en matière "
    "d’innovation ?",
  opts=["La France ne dispose d’aucun instrument de soutien à l’innovation",
        "Les instruments existent — Crédit d’impôt recherche, pôles de "
        "compétitivité, soutien public à l’innovation — mais leur traduction "
        "en positions dominantes à la frontière technologique reste "
        "insuffisante",
        "Les entreprises françaises refusent les aides publiques",
        "La recherche publique française est inexistante"],
  ans=1,
  why=["Le cours énumère au contraire plusieurs instruments existants.",
       "Rien n’indique un refus des aides : le problème est leur "
       "transformation en résultats.",
       "La recherche publique française existe, et c’est son articulation "
       "avec l’industrie qui pose problème."],
  exp="Le mécanisme attendu est pourtant clair : R&D ↑ → innovations ↑ → "
      "productivité ↑ → montée en gamme → compétitivité hors-prix ↑. La "
      "difficulté est de constater une traduction suffisamment forte dans "
      "l’émergence de technologies de rupture. Le problème français n’est "
      "donc pas l’absence d’instruments mais l’écart persistant entre "
      "l’importance des moyens mobilisés et la capacité de l’économie à les "
      "transformer en nouvelles positions dominantes.",
  diss="À rapprocher du handicap européen : excellence scientifique d’un "
       "côté, faiblesse de la transformation industrielle de l’autre."),

f(id='q22-n76', sp='c22-18', niv='comprendre', type='qcmm', b=6988,
  q="Quels défis le cours identifie-t-il pour la politique industrielle "
    "française ? (plusieurs réponses)",
  opts=["L’intelligence artificielle, technologie générale susceptible de "
        "transformer l’ensemble de l’économie",
        "La décarbonation du tissu productif",
        "L’articulation entre politique française et politique européenne",
        "La réduction du nombre d’entreprises exportatrices"],
  ans=[0, 1, 2],
  why=["Exacte : le retard européen y pose un problème de compétitivité et "
       "de souveraineté.",
       "Exacte : il faut réduire les émissions des industries existantes tout "
       "en développant celles de la transition.",
       "Exacte : les technologies stratégiques exigent un marché et des "
       "moyens dépassant l’échelle nationale.",
       "Inexacte : aucun objectif de ce genre n’est formulé, et il serait "
       "contraire à la logique du chapitre."],
  exp="Le troisième défi est le plus structurant : la France dispose d’un "
      "marché et de ressources financières trop limités pour rivaliser "
      "durablement avec les plus grandes puissances. Il faut donc définir des "
      "priorités communes, répartir les activités entre pays, éviter la "
      "concurrence interne entre États européens et articuler politique de "
      "concurrence et politique industrielle. La souveraineté industrielle "
      "doit donc être pensée moins comme nationale que comme européenne.",
  diss="Conclusion générale possible du chapitre : la bonne échelle de la "
       "politique industrielle est désormais l’échelle européenne."),

f(id='q22-n77', sp='c22-18', niv='raisonner', type='vf', b=7065,
  q="Selon le cours, une politique industrielle efficace doit être conçue "
    "comme une protection générale de l’appareil productif national.",
  ans=False,
  exp="La politique industrielle doit au contraire être conçue comme un "
      "instrument ciblé : l’intervention publique peut corriger certaines "
      "défaillances et accélérer des transformations stratégiques, mais elle "
      "devient inefficace lorsqu’elle protège durablement des activités "
      "incapables de devenir compétitives. L’analyse d’Agarwal rappelle que "
      "la politique industrielle peut être utile mais que son usage excessif "
      "devient contre-productif : des entreprises artificiellement "
      "maintenues, des ressources publiques immobilisées, une discipline "
      "concurrentielle supprimée. Toute la difficulté est de soutenir "
      "suffisamment pour permettre l’émergence d’activités stratégiques sans "
      "supprimer cette discipline.",
  diss="Phrase de conclusion possible : la sélectivité n’est pas une "
       "concession faite au marché, c’est la condition d’efficacité de "
       "l’intervention publique."),

]
