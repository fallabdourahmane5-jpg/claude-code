# -*- coding: utf-8 -*-
"""Chapitre 9 — questions nouvelles, sous-parties c9-12 à c9-15."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c9-12
f(id='q9-n64', sp='c9-12', niv='comprendre', type='qcm', b=2046,
  q="Pourquoi les coûts fixes sont-ils une barrière à l’entrée « tolérée » "
    "par la théorie économique ?",
  opts=["Parce qu’ils sont toujours faibles",
        "Parce qu’ils font partie du fonctionnement normal de l’activité "
        "économique : à court terme, il suffit à l’entreprise de couvrir son "
        "coût variable moyen pour rester sur le marché",
        "Parce que l’État les prend en charge",
        "Parce qu’ils disparaissent à long terme"],
  ans=1,
  why=["Ils peuvent être énormes : entrer dans l’industrie ferroviaire "
       "suppose rails, gares, matériel roulant et systèmes de sécurité.",
       "Aucune prise en charge publique générale n’est évoquée.",
       "À long terme, l’entreprise doit au contraire couvrir ses coûts fixes "
       "en plus de ses coûts variables et dégager un profit."],
  exp="La théorie admet qu’une entreprise ne couvre pas forcément "
      "immédiatement tous ses coûts fixes. Deux seuils doivent être "
      "distingués : le seuil de fermeture, atteint quand l’entreprise ne "
      "couvre plus son coût variable moyen — en dessous, elle doit cesser de "
      "produire ; et le seuil de rentabilité, qui suppose à long terme de "
      "couvrir coûts variables et coûts fixes et de dégager un profit.",
  diss="Hiérarchie utile des barrières : les coûts fixes et les brevets sont "
       "tolérés, les prix prédateurs et les exclusivités verrouillantes ne le "
       "sont pas."),

f(id='q9-n65', sp='c9-12', niv='appliquer', type='qcm', b=2133,
  q="Au lancement de l’iPhone en France, Apple avait conclu un accord "
    "d’exclusivité avec Orange. Quel problème cela pose-t-il, et pourquoi de "
    "tels accords ne sont-ils pas toujours interdits ?",
  opts=["Aucun problème : les accords d’exclusivité sont toujours licites",
        "Il limite l’accès des concurrents à un produit très attractif, mais "
        "de tels accords peuvent être tolérés s’ils sont temporaires, "
        "justifiés économiquement ou utiles à l’innovation",
        "Il s’agit d’un cartel entre Apple et Orange sur les prix",
        "Il s’agit d’une vente liée imposée au consommateur"],
  ans=1,
  why=["Ils peuvent au contraire constituer des barrières à l’entrée quand "
       "ils verrouillent l’accès au marché.",
       "Il n’y a ni fixation commune des prix ni partage de marché entre "
       "concurrents : Apple et Orange ne sont pas concurrents.",
       "La vente liée consiste à imposer un second produit : ce n’est pas le "
       "mécanisme ici."],
  exp="Un accord d’exclusivité réserve un produit, un service ou une "
      "technologie à un seul partenaire, ce qui peut empêcher les concurrents "
      "d’accéder au produit, à la clientèle ou à un réseau de distribution. "
      "Orange pouvait proposer l’iPhone, les autres opérateurs non. Ces "
      "accords peuvent toutefois être tolérés s’ils sont temporaires, "
      "justifiés économiquement, utiles à l’innovation ou nécessaires à un "
      "partenariat spécifique — le cours cite un partenariat ponctuel autour "
      "d’un événement comme Roland-Garros."),

f(id='q9-n66', sp='c9-12', niv='raisonner', type='courte', b=2172,
  q="Pourquoi le cas des licences de taxi montre-t-il l’ambivalence des "
    "barrières réglementaires ?",
  ans={'modele': "Les licences de taxi sont une barrière à l’entrée : il "
       "fallait en acheter une, parfois très cher, pour exercer. Cette "
       "barrière limitait le nombre de taxis, maintenait les revenus des "
       "chauffeurs et donnait à la licence une valeur patrimoniale, que le "
       "chauffeur pouvait revendre pour financer sa retraite : la licence "
       "était donc aussi un capital. L’arrivée d’Uber a eu des effets "
       "positifs — baisse des prix, amélioration et disponibilité du service, "
       "concurrence renforcée — mais elle a aussi fait perdre leur valeur aux "
       "licences, fragilisé les taxis et posé la question de la protection "
       "sociale des chauffeurs. L’État était pris dans une impasse : "
       "supprimer brutalement les licences pénalisait ceux qui les avaient "
       "payées très cher, les racheter aurait coûté énormément. Lever une "
       "barrière peut donc améliorer la concurrence tout en produisant des "
       "coûts sociaux importants.",
       'cles': [{'f': ['licence', 'barriere', 'limiter le nombre'],
                 'l': 'la licence est une barrière à l’entrée'},
                {'f': ['capital', 'patrimonial', 'retraite', 'revendre'],
                 'l': 'elle est aussi un capital revendable'},
                {'f': ['uber', 'baisse des prix', 'service'],
                 'l': 'l’arrivée d’Uber a fait baisser les prix et amélioré le service'},
                {'f': ['cout social', 'penalis', 'racheter', 'protection sociale'],
                 'l': 'la levée de la barrière produit des coûts sociaux'}]},
  exp="Les barrières réglementaires sont des obstacles créés par des règles "
      "juridiques ou administratives : licences, diplômes obligatoires, "
      "droits de douane, normes, monopoles publics, fiscalité spécifique. "
      "Elles peuvent protéger certaines professions — notaires, taxis, "
      "professions à autorisation — mais aussi limiter la concurrence. Le cas "
      "des taxis est le plus net : la même règle est à la fois protection et "
      "entrave.",
  diss="Exemple à réutiliser pour toute question sur les réformes "
       "structurelles : l’efficacité concurrentielle ne dit rien de "
       "l’acceptabilité sociale."),

f(id='q9-n67', sp='c9-12', niv='appliquer', type='qcm', b=2246,
  q="En quoi la portabilité du numéro a-t-elle rendu le marché de la "
    "téléphonie mobile plus contestable ?",
  opts=["En augmentant le nombre d’opérateurs présents sur le marché",
        "En réduisant les coûts de sortie des consommateurs, ce qui leur "
        "permet de changer d’opérateur plus facilement et renforce la "
        "pression concurrentielle",
        "En plafonnant les prix des forfaits",
        "En interdisant les offres promotionnelles"],
  ans=1,
  why=["Ce n’est pas le nombre d’opérateurs qui a changé mais la mobilité des "
       "clients.",
       "Aucun plafonnement des prix n’est en cause ici.",
       "Les promotions ne sont pas visées par cette mesure."],
  exp="Changer d’opérateur signifiait auparavant perdre son numéro : cette "
      "contrainte constituait une barrière à la sortie pour les "
      "consommateurs, qui devenaient captifs. Avec la portabilité, ils "
      "peuvent changer plus facilement, les opérateurs doivent davantage les "
      "retenir et la concurrence augmente. Le cours en tire une conclusion "
      "importante : la contestabilité ne concerne pas seulement l’entrée des "
      "entreprises, mais aussi la capacité des consommateurs à changer "
      "d’offre.",
  diss="Idée puissante : agir sur les coûts de changement du consommateur "
       "peut être plus efficace que multiplier le nombre d’offreurs."),

# ------------------------------------------------------------- c9-13
f(id='q9-n68', sp='c9-13', niv='connaitre', type='qcm', b=2270,
  q="Qu’étudie l’économie industrielle, et pourquoi son nom peut-il induire "
    "en erreur ?",
  opts=["Elle étudie uniquement le secteur secondaire, donc l’industrie au "
        "sens strict",
        "Elle étudie le fonctionnement des marchés, les stratégies des "
        "entreprises, les comportements concurrentiels, les ententes et les "
        "performances des firmes : « industrielle » ne renvoie pas au seul "
        "secteur secondaire",
        "Elle étudie la politique industrielle de l’État",
        "Elle étudie l’organisation du travail dans les usines"],
  ans=1,
  why=["C’est précisément le contresens que le cours signale : le terme ne se "
       "limite pas au secteur secondaire.",
       "La politique industrielle est une politique publique, pas cette "
       "branche de l’analyse.",
       "L’organisation du travail relève du taylorisme et du toyotisme, "
       "traités dans la conclusion."],
  exp="L’économie industrielle se développe au XXe siècle. Elle analyse la "
      "structure des marchés, les comportements des entreprises et leurs "
      "effets sur les performances économiques : politiques de prix, "
      "ententes, stratégies concurrentielles. Le terme « industrielle » "
      "désigne plus largement l’étude des activités économiques et des "
      "stratégies des entreprises.",
  diss="C’est de cette branche que sort le modèle SCP, construit par Mason "
       "puis Bain à partir d’analyses historiques des marchés américains."),

f(id='q9-n69', sp='c9-13', niv='connaitre', type='assoc', b=2299,
  q="Associez chaque élément à la dimension du modèle SCP à laquelle il "
    "appartient.",
  ans=[["Degré de concentration et barrières à l’entrée", "Structure"],
       ["Nombre d’entreprises et intensité concurrentielle", "Structure"],
       ["Politique de prix, ententes, différenciation, prix prédateurs", "Comportements"],
       ["Profits, marges, parts de marché, efficacité productive", "Performances"]],
  exp="La structure désigne la configuration du marché : nombre "
      "d’entreprises, degré de concentration, barrières à l’entrée, intensité "
      "concurrentielle, pouvoir de marché. Les comportements sont les "
      "stratégies adoptées : prix, ententes, cartels, différenciation, "
      "innovation, monopole discriminant, prix prédateurs. Les performances "
      "sont les résultats obtenus : profits, rentabilité, marges, parts de "
      "marché, croissance, efficacité productive.",
  diss="Le modèle vaut autant comme grille de lecture que comme théorie : il "
       "fournit un plan d’analyse de n’importe quel marché."),

f(id='q9-n70', sp='c9-13', niv='appliquer', type='ordre', b=2382,
  q="Remettez dans l’ordre l’enchaînement par lequel une stratégie "
    "d’entreprise transforme la structure du marché — l’argument qui limite "
    "le modèle SCP.",
  ans=["Une entreprise différencie fortement son produit",
       "Les consommateurs deviennent fidèles à la marque",
       "La demande devient moins élastique au prix",
       "L’entreprise augmente ses profits",
       "Elle peut ensuite racheter des concurrents et modifier la structure "
       "du marché"],
  exp="Le modèle SCP suppose une causalité simple : la structure détermine "
      "les comportements, qui déterminent les performances. Cette "
      "vision est trop mécanique, car la relation peut aller dans l’autre "
      "sens. Une stratégie efficace — différenciation, innovation, "
      "fidélisation, politique de marque, baisse des coûts — permet "
      "d’augmenter les profits, de gagner des parts de marché et de racheter "
      "des concurrents : le comportement transforme alors la structure.",
  diss="Cette inversion de causalité est la limite à citer systématiquement "
       "avec le modèle SCP."),

f(id='q9-n71', sp='c9-13', niv='raisonner', type='qcmm', b=2458,
  q="Selon l’approche élargie de la concurrence, que doivent viser les "
    "politiques de concurrence ? (plusieurs réponses)",
  opts=["Réduire les barrières à l’entrée",
        "Limiter les coûts irrécupérables",
        "Empêcher les verrouillages technologiques et contrôler les abus de "
        "position dominante",
        "Faciliter l’entrée de nouveaux acteurs",
        "Empêcher les entreprises de devenir grandes"],
  ans=[0, 1, 2, 3],
  why=["Exacte : c’est la condition première de la contestabilité.",
       "Exacte : des coûts irrécupérables élevés rendent la menace d’entrée "
       "non crédible.",
       "Exacte : le verrouillage est la forme contemporaine de la fermeture "
       "du marché.",
       "Exacte : l’entrée effective ou potentielle est le critère retenu.",
       "Faux : l’objectif n’est pas d’empêcher les entreprises de grandir "
       "mais d’éviter qu’elles bloquent durablement le marché."],
  exp="Dans l’approche standard, il faut surtout lutter contre la "
      "concentration ; dans l’approche élargie, maintenir la contestabilité "
      "du marché. Le monopole n’est pas un problème en soi : le problème "
      "apparaît quand il est protégé, quand le marché est fermé, quand les "
      "concurrents ne peuvent pas entrer. Les politiques modernes cherchent "
      "donc moins à empêcher toute concentration qu’à garantir que les "
      "marchés restent ouverts.",
  diss="Opposition à exploiter chez Emmanuel Combe : concurrence comme "
       "structure (atomicité) contre concurrence comme processus de sélection "
       "des firmes les plus efficaces."),

# ------------------------------------------------------------- c9-14
f(id='q9-n72', sp='c9-14', niv='connaitre', type='assoc', b=2484,
  q="Associez chaque texte ou institution à son rôle dans la politique de "
    "concurrence.",
  ans=[["Sherman Act 1890, Clayton Act 1914, Federal Trade Commission Act 1914", "États-Unis : les lois antitrust"],
       ["Article 101 du TFUE", "Union européenne : interdiction des ententes et des cartels"],
       ["Article 102 du TFUE", "Union européenne : interdiction des abus de position dominante"],
       ["DGCCRF et Autorité de la concurrence", "France : administration rattachée à l’État et autorité indépendante"]],
  exp="Aux États-Unis, les lois antitrust visent à interdire les cartels, à "
      "limiter les monopoles abusifs, à sanctionner les pratiques "
      "anticoncurrentielles et à protéger le consommateur. En Europe, la "
      "concurrence est considérée comme indispensable au bon fonctionnement "
      "du marché intérieur : l’article 101 interdit les ententes, l’article "
      "102 les abus de position dominante. En France, la DGCCRF dépend du "
      "ministère de l’Économie tandis que l’Autorité de la concurrence est "
      "une autorité indépendante qui peut enquêter, sanctionner, imposer des "
      "amendes et refuser certaines concentrations.",
  diss="Si une pratique concerne plusieurs États membres, le droit européen "
       "peut s’appliquer : la compétence dépend de l’étendue de l’atteinte."),

f(id='q9-n73', sp='c9-14', niv='comprendre', type='qcm', b=2557,
  q="Quelle est la position du droit européen sur les aides d’État ?",
  opts=["Elles sont toutes autorisées, car elles soutiennent l’emploi",
        "Elles sont en principe interdites lorsqu’elles faussent la "
        "concurrence, mais certaines sont tolérées : recherche, PME, aides "
        "écologiques, aides de crise, innovation",
        "Elles sont toutes interdites sans exception",
        "Elles relèvent uniquement du droit national de chaque État membre"],
  ans=1,
  why=["Une autorisation générale viderait de son sens la surveillance des "
       "aides d’État.",
       "L’interdiction n’est pas absolue : le cours énumère explicitement des "
       "aides tolérées.",
       "C’est précisément un domaine où l’Union européenne exerce un contrôle "
       "fort."],
  exp="Une aide publique peut fausser la concurrence : l’entreprise "
      "subventionnée devient artificiellement plus compétitive, elle peut "
      "vendre moins cher, investir davantage et prendre des parts de marché "
      "au détriment de firmes plus efficaces. D’où la surveillance "
      "européenne. Le cours ajoute que l’Union critique souvent les "
      "subventions chinoises, qui permettent aux entreprises chinoises de "
      "vendre moins cher sur les marchés internationaux."),

f(id='q9-n74', sp='c9-14', niv='raisonner', type='qcm', b=2580,
  q="Selon Emmanuel Combe, environ 1 % des fusions ont été refusées entre "
    "2010 et 2020. Comment interpréter ce chiffre ?",
  opts=["Les autorités de concurrence sont inefficaces",
        "La concentration n’est pas automatiquement condamnée : ce qui compte "
        "est son effet sur la concurrence, et certaines fusions apportent "
        "économies d’échelle, innovation, compétitivité internationale et "
        "baisse des coûts",
        "Les fusions sont devenues rares",
        "Le contrôle des concentrations a été supprimé en Europe"],
  ans=1,
  why=["Le faible taux de refus n’est pas un indice d’inefficacité mais le "
       "résultat d’un examen au cas par cas.",
       "Les fusions sont au contraire nombreuses : seule une petite part est "
       "refusée.",
       "Le contrôle des concentrations est au contraire l’un des quatre "
       "domaines de la politique de concurrence."],
  exp="Les autorités doivent vérifier si la fusion risque de nuire au "
      "consommateur : une concentration excessive peut réduire la "
      "concurrence, créer un monopole ou un oligopole, renforcer une position "
      "dominante, augmenter les prix. Mais elle peut aussi permettre des "
      "économies d’échelle, de l’innovation et une meilleure compétitivité "
      "internationale. L’analyse est donc toujours au cas par cas, et dépend "
      "fortement de la définition du marché pertinent — local, national, "
      "européen ou mondial.",
  diss="À articuler avec Alstom-Siemens : l’argument du « champion européen » "
       "contre celui de la position dominante sur le marché ferroviaire "
       "européen."),

f(id='q9-n75', sp='c9-14', niv='comprendre', type='qcmm', b=2640,
  q="Que le DMA interdit-il aux plateformes désignées comme « contrôleurs "
    "d’accès » ? (plusieurs réponses)",
  opts=["Favoriser leurs propres produits",
        "Exploiter les données de leurs concurrents contre eux",
        "Imposer certains services et bloquer l’accès au marché",
        "Rendre les utilisateurs captifs",
        "Réaliser des bénéfices supérieurs à 10 % de leur chiffre d’affaires"],
  ans=[0, 1, 2, 3],
  why=["Exacte : l’auto-préférence est la pratique visée en premier.",
       "Exacte : les plateformes sont à la fois arbitres et joueurs sur leur "
       "propre marché.",
       "Exacte : le verrouillage de l’accès est au cœur du règlement.",
       "Exacte : la captivité des utilisateurs réduit la contestabilité du "
       "marché.",
       "Le DMA n’encadre pas le niveau de profit : les 10 % du chiffre "
       "d’affaires mondial sont le plafond des amendes, porté à 20 % en cas "
       "de récidive."],
  exp="Le DMA, adopté en 2022, vise les grandes plateformes qui contrôlent "
      "l’accès à des marchés numériques essentiels : Google, Amazon, Apple, "
      "Meta, Microsoft. Son originalité est d’interdire a priori certaines "
      "pratiques à des acteurs désignés, au lieu d’attendre la constatation "
      "d’un abus au cas par cas.",
  diss="Le DMA est l’illustration la plus récente de l’approche élargie : il "
       "cherche à restaurer la contestabilité de marchés verrouillés par les "
       "effets de réseau."),

# ------------------------------------------------------------- c9-15
f(id='q9-n76', sp='c9-15', niv='raisonner', type='qcm', b=2685,
  q="Dans les années 1990, Exxon et Mobil, issues du démantèlement de la "
    "Standard Oil, refusionnent. Que montre cette « ironie de l’histoire » ?",
  opts=["Que le démantèlement est juridiquement illégal",
        "Que les politiques de démantèlement peuvent restaurer "
        "temporairement la concurrence, mais que les dynamiques de "
        "concentration réapparaissent, notamment avec la mondialisation",
        "Que la Standard Oil n’avait jamais été démantelée",
        "Que la concentration est toujours bénéfique"],
  ans=1,
  why=["Le démantèlement est au contraire l’arme la plus radicale des "
       "politiques antitrust, prévue par le droit.",
       "Le démantèlement de 1911 a bien eu lieu : ce sont ses héritières qui "
       "refusionnent.",
       "Le cours ne tire aucune conclusion de ce genre : il souligne un cycle, "
       "pas un jugement favorable."],
  exp="Le démantèlement consiste à découper une entreprise dominante en "
      "plusieurs sociétés indépendantes afin de recréer de la concurrence et "
      "de réduire le pouvoir de marché. Mais l’histoire économique est "
      "marquée par des cycles : concentration, démantèlement, "
      "reconcentration. La refusion d’Exxon et de Mobil dans un contexte de "
      "mondialisation en est l’illustration.",
  diss="Argument fort pour une conclusion : la politique de concurrence ne "
       "résout pas la concentration une fois pour toutes, elle l’encadre "
       "continuellement."),

f(id='q9-n77', sp='c9-15', niv='connaitre', type='qcm', b=2698,
  q="Quels autres exemples de démantèlement ou de menace de démantèlement le "
    "cours retient-il ?",
  opts=["IBM dans les années 1960 et Apple dans les années 2000",
        "AT&T, démantelée dans les années 1980, et Microsoft, poursuivie dans "
        "les années 1990 mais qui échappe finalement au démantèlement",
        "General Electric et Samsung",
        "Alstom et Siemens"],
  ans=1,
  why=["Ni IBM ni Apple ne sont cités dans ce passage du cours.",
       "GE et Samsung illustrent la concentration conglomérale et la décote "
       "de conglomérat, pas le démantèlement antitrust.",
       "Alstom-Siemens est un refus de fusion, c’est-à-dire du contrôle des "
       "concentrations, non un démantèlement."],
  exp="Dans les années 1980, AT&T subit un démantèlement afin de réduire sa "
      "domination et d’ouvrir le marché des télécommunications. Dans les "
      "années 1990, Microsoft est poursuivie pour abus de position dominante "
      "et les autorités envisagent de séparer Windows, Internet Explorer et "
      "les logiciels, mais l’entreprise évite finalement la sanction. Même "
      "lorsqu’il n’est pas appliqué, le démantèlement reste un outil de "
      "pression important."),

f(id='q9-n78', sp='c9-15', niv='comprendre', type='qcm', b=2719,
  q="Comment le cours situe-t-il la position de Milton Friedman sur les "
    "objectifs de l’entreprise, et comment la nuance-t-il ?",
  opts=["Friedman soutient que l’entreprise doit poursuivre des objectifs "
        "sociaux et environnementaux",
        "Pour Friedman, la responsabilité principale de l’entreprise est de "
        "maximiser le profit ; cette vision est aujourd’hui largement "
        "nuancée par la logique de la RSE",
        "Friedman défend la nationalisation des grandes entreprises",
        "Friedman analyse l’entreprise comme un nœud de contrats"],
  ans=1,
  why=["C’est précisément la position que la RSE oppose à la sienne.",
       "Rien de tel n’est attribué à Friedman dans le cours.",
       "Le nœud de contrats est la formule d’Alchian et Demsetz."],
  exp="Dans la vision classique associée à Milton Friedman, la responsabilité "
      "principale de l’entreprise est de maximiser le profit. L’analyse "
      "contemporaine dépasse cette seule recherche : l’entreprise peut aussi "
      "poursuivre des objectifs sociaux, environnementaux et sociétaux, selon "
      "la logique de la responsabilité sociale des entreprises. Elle doit "
      "alors tenir compte de ses salariés, des consommateurs, de "
      "l’environnement, de son territoire et de son image sociale.",
  diss="Conclusion du chapitre : la firme n’est pas seulement un acteur "
       "financier, c’est une organisation ayant des responsabilités."),

f(id='q9-n79', sp='c9-15', niv='raisonner', type='qcm', b=2758,
  q="En quoi l’entreprise est-elle, selon la conclusion du chapitre, une "
    "organisation ambivalente ?",
  opts=["Parce qu’elle est à la fois publique et privée",
        "Parce qu’elle repose sur la coopération des acteurs pour produire, "
        "tout en étant traversée par des conflits d’intérêts entre salariés, "
        "dirigeants, actionnaires et consommateurs",
        "Parce qu’elle poursuit à la fois des objectifs de court et de long "
        "terme",
        "Parce qu’elle est à la fois intégrée et distribuée"],
  ans=1,
  why=["Le statut juridique n’est pas l’ambivalence visée ici.",
       "L’horizon temporel n’est pas la tension analysée dans ce passage.",
       "L’articulation intégré / distribué concerne l’organisation "
       "productive, traitée plus haut avec François et Lemercier."],
  exp="Pour produire, les individus doivent coopérer : coordonner les tâches, "
      "organiser le travail, combiner les compétences — le cours rappelle que "
      "même chez Marx, bourgeois et prolétaires s’opposent mais doivent "
      "coopérer dans la production. Mais les acteurs n’ont pas les mêmes "
      "intérêts : les actionnaires veulent des profits, les salariés de "
      "meilleurs salaires, les managers du pouvoir ou une carrière, les "
      "consommateurs des prix bas. L’entreprise est donc à la fois un lieu de "
      "coordination et un lieu de conflictualité.",
  diss="Cette ambivalence est aussi la limite que le cours oppose à "
       "Williamson : réduire l’entreprise à l’opportunisme en fait un lieu de "
       "triche et oublie la coopération."),

f(id='q9-n80', sp='c9-15', niv='raisonner', type='courte', b=2913,
  q="Quelles sont, selon la conclusion du chapitre, la force et la faiblesse "
    "de la méthode des économistes ?",
  ans={'modele': "La force de l’économie est de généraliser : l’économiste "
       "part de faits empiriques — entreprises, marchés, comportements —, "
       "repère des régularités, c’est-à-dire des phénomènes qui se répètent "
       "assez pour autoriser une généralisation, puis construit des modèles "
       "qui font apparaître des mécanismes valables au-delà d’un pays, d’une "
       "époque ou d’un cas particulier. Le modèle SCP, construit par Mason "
       "puis Bain à partir de cas historiques américains, et la théorie de "
       "l’agence, dont la relation actionnaire-manager n’est qu’une "
       "application d’un schéma général de délégation et d’incitation, en "
       "sont deux illustrations. La faiblesse est le risque de trop "
       "généraliser : une théorie peut être vraie à une époque, dans un pays, "
       "dans un contexte particulier, et ne plus fonctionner ailleurs — le "
       "cours cite la courbe de Phillips. Les théories économiques doivent "
       "donc toujours être replacées dans leur contexte historique et "
       "géographique.",
       'cles': [{'f': ['regularite', 'generalis', 'modele'],
                 'l': 'repérer des régularités et construire des modèles généraux'},
                {'f': ['scp', 'agence', 'exemple', 'application'],
                 'l': 'le modèle SCP et la théorie de l’agence comme exemples'},
                {'f': ['trop generalis', 'contexte', 'phillips', 'epoque'],
                 'l': 'le risque de généraliser hors de son contexte (courbe de Phillips)'}]},
  exp="La conclusion du chapitre énonce ce double mouvement : la force de "
      "l’économie est de dégager des mécanismes généraux, sa faiblesse est "
      "d’oublier parfois que ces mécanismes sont construits à partir de "
      "contextes historiques précis. Le cours ajoute qu’il ne faut pas "
      "confondre la théorie générale et son application concrète.",
  diss="Conclusion citable telle quelle : l’entreprise révèle des tensions "
       "entre profit et responsabilité, coopération et conflit, rationalité "
       "et incertitude, tout en montrant comment les économistes généralisent "
       "des régularités à partir d’un réel toujours plus complexe."),

]
