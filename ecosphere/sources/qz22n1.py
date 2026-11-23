# -*- coding: utf-8 -*-
"""Chapitre 22 — questions nouvelles, sous-partie c22-13 (non testée auparavant)."""


def f(**kw):
    return kw


L = [

f(id='q22-n01', sp='c22-13', niv='connaitre', type='qcm', b=4617,
  q="Selon le cours, quel est le problème essentiel des stratégies "
    "d’industrialisation qui ont échoué dans les pays en développement ?",
  opts=["Un manque de capitaux étrangers",
        "Un manque de concurrence",
        "Une population trop peu nombreuse",
        "Une monnaie trop faible"],
  ans=1,
  why=["Le manque de capitaux n’est pas l’explication retenue : plusieurs de "
       "ces stratégies ont justement bénéficié d’un soutien public important.",
       "La taille de la population n’est pas invoquée par le cours.",
       "Le niveau de la monnaie n’est pas la cause de ces échecs."],
  exp="Lorsque les entreprises nationales sont durablement protégées — de la "
      "concurrence étrangère, mais aussi parfois de la concurrence intérieure "
      "—, elles peuvent perdre l’incitation à réduire leurs coûts, à améliorer "
      "leur qualité, à innover et donc à devenir réellement compétitives. Le "
      "problème n’est pas la protection en elle-même, mais la suppression "
      "durable de toute discipline concurrentielle.",
  diss="Formule efficace : ce n’est pas la protection qui échoue, c’est la "
       "protection sans concurrence."),

f(id='q22-n02', sp='c22-13', niv='appliquer', type='ordre', b=4627,
  q="Remettez dans l’ordre le mécanisme par lequel une protection permanente "
    "devient contre-productive.",
  ans=["Une industrie naissante est protégée de la concurrence, et cette "
       "protection est maintenue durablement",
       "La pression concurrentielle qui pèse sur les entreprises protégées "
       "diminue",
       "La rente que procure la position protégée augmente",
       "L’incitation à innover et à réaliser des gains de productivité "
       "diminue",
       "Les entreprises deviennent durablement dépendantes du soutien de "
       "l’État"],
  exp="C’est l’enchaînement exact retenu par le cours : protection permanente "
      "→ pression concurrentielle ↓ → rente ↑ → innovation et productivité ↓ "
      "→ entreprises durablement dépendantes de l’État. L’entreprise protégée "
      "peut alors préférer préserver sa rente plutôt que réaliser les gains "
      "de productivité nécessaires à sa compétitivité.",
  diss="Mécanisme central : il explique à la fois les échecs des stratégies "
       "d’industrialisation protégée et le risque de « l’industrie infantile "
       "qui ne devient jamais adulte »."),

f(id='q22-n03', sp='c22-13', niv='comprendre', type='qcm', b=4633,
  q="Pourquoi une entreprise durablement protégée peut-elle renoncer à "
    "améliorer sa productivité ?",
  opts=["Parce que la réglementation le lui interdit",
        "Parce que préserver la rente que lui procure sa position protégée "
        "peut être plus avantageux que réaliser des gains de productivité "
        "coûteux",
        "Parce qu’elle ne dispose d’aucune information sur ses coûts",
        "Parce que ses salariés refusent les changements techniques"],
  ans=1,
  why=["Aucune interdiction réglementaire n’est en cause : c’est l’incitation "
       "économique qui disparaît.",
       "L’information n’est pas le problème : l’entreprise connaît ses coûts "
       "mais n’a plus intérêt à les réduire.",
       "Le comportement des salariés n’est pas l’explication retenue par le "
       "cours."],
  exp="La protection publique devient contre-productive lorsqu’elle supprime "
      "durablement la discipline concurrentielle. L’entreprise compare alors "
      "deux voies : investir, se réorganiser et prendre des risques pour "
      "gagner en productivité, ou conserver sans effort une position "
      "garantie. Quand aucun concurrent ne peut lui prendre son marché, la "
      "seconde voie devient rationnelle.",
  diss="À rapprocher du Public Choice : les ressources de l’entreprise "
       "peuvent être consacrées à obtenir et conserver la protection plutôt "
       "qu’à produire mieux."),

f(id='q22-n04', sp='c22-13', niv='raisonner', type='qcmm', b=4601,
  q="Quels éléments les économies asiatiques ayant réussi leur "
    "industrialisation ont-elles combinés, selon le cours ? (plusieurs "
    "réponses)",
  opts=["Une protection temporaire",
        "Un soutien public ciblé",
        "La mise en concurrence des entreprises",
        "Une orientation vers les exportations",
        "Un investissement massif dans l’éducation et la R&D",
        "La fermeture durable de leur marché intérieur"],
  ans=[0, 1, 2, 3, 4],
  why=["Exacte : la protection est accordée pour une durée limitée.",
       "Exacte : l’État concentre des moyens sur certaines activités.",
       "Exacte : c’est précisément ce qui distingue ces réussites des échecs.",
       "Exacte : l’exportation impose une discipline par le marché mondial.",
       "Exacte : elle permet d’absorber les technologies puis d’innover.",
       "Inexacte : c’est au contraire la caractéristique des stratégies qui "
       "ont échoué."],
  exp="Le succès d’une politique industrielle ne repose pas sur la seule "
      "protection des entreprises nationales, mais sur une protection "
      "temporaire associée à une forte discipline concurrentielle, à "
      "l’apprentissage et à une montée progressive en gamme. L’exportation "
      "joue un rôle décisif : elle oblige l’entreprise protégée chez elle à "
      "affronter malgré tout les standards internationaux.",
  diss="Liste très mobilisable : protection temporaire, soutien ciblé, "
       "concurrence, exportations, éducation et R&D, montée en gamme."),

f(id='q22-n05', sp='c22-13', niv='connaitre', type='qcm', b=4646,
  q="Quel rythme de croissance annuelle moyenne la Corée du Sud a-t-elle "
    "connu entre 1963 et 1979 ?",
  opts=["Environ 4 %",
        "Environ 12 %",
        "Environ 20 %",
        "Environ 2 %"],
  ans=1,
  why=["Environ 4 % correspondrait à une croissance soutenue, mais très "
       "inférieure au rattrapage coréen.",
       "Environ 20 % serait un rythme jamais observé durablement.",
       "Environ 2 % correspond plutôt à la croissance d’une économie "
       "avancée."],
  exp="La Corée du Sud a connu environ 12 % de croissance annuelle moyenne "
      "entre 1963 et 1979, puis encore autour de 9 % dans les décennies 1980 "
      "et 1990. En quelques décennies, elle est passée d’une économie à "
      "faible revenu à une économie à haut revenu, ce qui en fait un exemple "
      "remarquable de sortie rapide de la trappe à revenu intermédiaire.",
  diss="Mais le chiffre important n’est pas le taux : c’est la "
       "transformation radicale de la spécialisation productive qui "
       "l’accompagne."),

f(id='q22-n06', sp='c22-13', niv='comprendre', type='qcm', b=4644,
  q="Pourquoi la Corée du Sud est-elle présentée comme un exemple "
    "remarquable de sortie de la trappe à revenu intermédiaire ?",
  opts=["Parce qu’elle a conservé sa spécialisation initiale tout en "
        "augmentant ses volumes de production",
        "Parce qu’elle est passée en quelques décennies d’une économie à "
        "faible revenu à une économie à haut revenu, en transformant "
        "radicalement sa spécialisation",
        "Parce qu’elle a renoncé à toute politique industrielle",
        "Parce qu’elle a bénéficié de ressources naturelles abondantes"],
  ans=1,
  why=["Conserver la spécialisation initiale aurait précisément maintenu la "
       "Corée dans la concurrence des pays à salaires plus faibles.",
       "La Corée a au contraire mené une politique industrielle verticale "
       "très active.",
       "Les ressources naturelles ne sont pas invoquées par le cours."],
  exp="La trappe à revenu intermédiaire désigne la difficulté, pour une "
      "économie, de dépasser un certain niveau de revenu : elle n’est plus "
      "assez peu coûteuse pour concurrencer les pays à bas salaires, ni assez "
      "avancée pour concurrencer les économies développées. La Corée en sort "
      "en changeant de spécialisation, et non en intensifiant sa "
      "spécialisation initiale.",
  diss="C’est l’argument décisif contre une lecture statique des avantages "
       "comparatifs."),

f(id='q22-n07', sp='c22-13', niv='appliquer', type='ordre', b=4685,
  q="Remettez dans l’ordre les étapes de la montée en gamme sud-coréenne.",
  ans=["Textile, biens simples et premières productions électroniques, grâce "
       "à une main-d’œuvre abondante et peu coûteuse",
       "Automobile, construction navale, équipements, matériel optique et "
       "chimie, à mesure que s’accumulent capital, savoir-faire et "
       "technologie",
       "Électronique avancée, informatique, télécommunications et "
       "semi-conducteurs"],
  exp="On passe donc d’une production simple à une industrie intermédiaire "
      "puis à une industrie technologique. Rester durablement sur les "
      "premières productions aurait exposé la Corée à la concurrence des pays "
      "disposant de salaires encore plus faibles : c’est la raison pour "
      "laquelle il fallait changer progressivement de spécialisation.",
  diss="Idée fondamentale à retenir : la Corée n’était pas naturellement "
       "spécialisée dans les semi-conducteurs, elle a créé les capacités "
       "permettant d’y devenir compétitive."),

f(id='q22-n08', sp='c22-13', niv='connaitre', type='qcm', b=4696,
  q="Que désigne le terme « chaebol » dans le cas sud-coréen ?",
  opts=["Une agence publique de planification",
        "Un grand conglomérat privé, comme Samsung, Hyundai ou LG",
        "Un syndicat ouvrier",
        "Une zone économique spéciale"],
  ans=1,
  why=["L’agence de planification correspondrait plutôt au Commissariat "
       "général au Plan français ou au MITI japonais.",
       "Les chaebols sont des groupes d’entreprises, non des organisations "
       "syndicales.",
       "Les zones économiques spéciales sont un instrument territorial, non "
       "une forme d’entreprise."],
  exp="La politique industrielle coréenne repose notamment sur de grands "
      "conglomérats privés appelés chaebols — Samsung, Hyundai, LG. Ils "
      "bénéficient de subventions, de crédits avantageux, de prêts bonifiés, "
      "d’un soutien à l’investissement et d’une stratégie publique de "
      "développement des exportations : l’État concentre ainsi ses ressources "
      "sur certaines entreprises capables de porter l’industrialisation.",
  diss="Point de méthode : il s’agit d’entreprises privées soutenues par "
       "l’État, non d’entreprises publiques."),

f(id='q22-n09', sp='c22-13', niv='comprendre', type='qcmm', b=4702,
  q="De quels soutiens les chaebols coréens ont-ils bénéficié ? (plusieurs "
    "réponses)",
  opts=["Des subventions",
        "Des crédits avantageux et des prêts bonifiés",
        "Un soutien à l’investissement",
        "Une stratégie publique de développement des exportations",
        "Une garantie de prix de vente sur le marché mondial"],
  ans=[0, 1, 2, 3],
  why=["Exacte : les subventions font partie des instruments mobilisés.",
       "Exacte : le crédit bonifié réduit le coût du capital.",
       "Exacte : l’État soutient directement l’effort d’investissement.",
       "Exacte : l’orientation vers l’exportation est au cœur de la "
       "stratégie.",
       "Inexacte : aucune garantie de prix mondial n’est mentionnée, et elle "
       "supprimerait la discipline que l’exportation est censée imposer."],
  exp="L’État coréen concentre ses ressources sur les entreprises jugées "
      "capables de porter l’industrialisation : nous sommes donc dans une "
      "politique industrielle verticale. Mais ces aides restent liées à une "
      "exigence de résultats à l’exportation, ce qui maintient une discipline "
      "externe sur des entreprises largement protégées chez elles.",
  diss="Comparaison utile avec la France : les aides existent dans les deux "
       "cas, la conditionnalité par l’exportation beaucoup moins."),

f(id='q22-n10', sp='c22-13', niv='comprendre', type='qcm', b=4710,
  q="À quel type de politique industrielle le soutien coréen aux chaebols "
    "correspond-il ?",
  opts=["Une politique horizontale, puisqu’elle améliore l’environnement "
        "général de l’économie",
        "Une politique verticale, puisque l’État concentre ses ressources sur "
        "certaines entreprises",
        "Une politique de la demande",
        "Une politique monétaire"],
  ans=1,
  why=["L’amélioration de l’environnement général correspond à la politique "
       "horizontale, que la Corée a menée en complément mais qui n’est pas "
       "ce dont il s’agit ici.",
       "La politique de la demande agit sur la consommation et "
       "l’investissement globaux, non sur la structure productive.",
       "La politique monétaire porte sur les taux d’intérêt et la masse "
       "monétaire."],
  exp="Choisir certaines entreprises et y concentrer des subventions, du "
      "crédit bonifié et un appui à l’exportation, c’est cibler : il s’agit "
      "donc d’une politique verticale. La Corée illustre cependant que les "
      "deux dimensions sont complémentaires, puisque ce soutien ciblé a été "
      "accompagné d’investissements massifs dans l’éducation et la recherche, "
      "qui relèvent de l’horizontal.",
  diss="À retenir pour nuancer : les politiques verticale et horizontale ne "
       "s’excluent pas, les réussites les combinent."),

f(id='q22-n11', sp='c22-13', niv='raisonner', type='courte', b=4732,
  q="Pourquoi le seul soutien financier aux chaebols n’aurait-il pas suffi au "
    "rattrapage coréen ?",
  ans={'modele': "Parce que la montée en gamme exige des capacités que "
       "l’argent public ne crée pas directement. Le soutien aux entreprises a "
       "été accompagné d’investissements massifs dans le capital humain : "
       "d’abord l’enseignement primaire et secondaire, puis l’enseignement "
       "supérieur, la formation technique, l’ingénierie et la recherche. Le "
       "mécanisme est le suivant : éducation ↑ → qualification ↑ → capacité "
       "d’absorber les technologies étrangères ↑ → productivité ↑ → montée en "
       "gamme ; puis R&D ↑ → innovation propre ↑ → frontière technologique "
       "rapprochée. Sans main-d’œuvre qualifiée, une entreprise subventionnée "
       "ne peut ni absorber les technologies étrangères ni, plus tard, "
       "innover elle-même. L’État coréen a donc simultanément soutenu les "
       "entreprises et construit les capacités humaines permettant leur "
       "montée en gamme : c’est la combinaison des deux qui explique le "
       "rattrapage.",
       'cles': [{'f': ['capital humain', 'education', 'formation', 'ecole'],
                 'l': "des investissements massifs dans l'éducation et le capital humain"},
                {'f': ['qualification', 'qualifie', 'ingenieur', 'technique'],
                 'l': "l'élévation des qualifications"},
                {'f': ['absorber', 'assimil', 'technologie etrangere', 'imiter'],
                 'l': "la capacité d'absorber les technologies étrangères"},
                {'f': ['r&d', 'recherche', 'innovation propre'],
                 'l': "la R&D et l'innovation propre"},
                {'f': ['ecosysteme', 'simultan', 'complementaire', 'combinaison'],
                 'l': "la complémentarité entre soutien aux entreprises et écosystème"}]},
  exp="Le soutien aux chaebols n’aurait pas suffi sans une politique "
      "complémentaire d’éducation, de formation et de recherche : l’État "
      "coréen a simultanément soutenu les entreprises et construit les "
      "capacités humaines permettant leur montée en gamme.",
  diss="Transposition immédiate au débat français : disposer d’instruments de "
       "soutien ne suffit pas si l’écosystème ne permet pas de les "
       "transformer en positions technologiques."),

f(id='q22-n12', sp='c22-13', niv='appliquer', type='ordre', b=4728,
  q="Remettez dans l’ordre le mécanisme par lequel l’éducation soutient la "
    "montée en gamme.",
  ans=["L’investissement public dans l’enseignement et la formation augmente",
       "Le niveau de qualification de la main-d’œuvre s’élève",
       "La capacité à absorber les technologies étrangères augmente",
       "La productivité augmente",
       "La montée en gamme devient possible, puis la R&D permet une "
       "innovation propre qui rapproche de la frontière technologique"],
  exp="C’est le mécanisme retenu par le cours : éducation ↑ → qualification ↑ "
      "→ capacité d’absorber les technologies étrangères ↑ → productivité ↑ → "
      "montée en gamme, puis R&D ↑ → innovation propre ↑ → frontière "
      "technologique rapprochée. L’ordre importe : on commence par imiter et "
      "absorber, on n’innove soi-même qu’ensuite.",
  diss="À relier à Aghion : loin de la frontière on absorbe, près de la "
       "frontière on innove — et les politiques efficaces diffèrent."),

f(id='q22-n13', sp='c22-13', niv='comprendre', type='vf', b=4688,
  q="La Corée du Sud disposait au départ d’un avantage comparatif naturel "
    "dans les semi-conducteurs.",
  ans=False,
  exp="La Corée n’était pas naturellement spécialisée dans les "
      "semi-conducteurs : elle a créé les capacités permettant d’y devenir "
      "compétitive. Sa spécialisation initiale portait sur le textile, les "
      "biens simples et les premières productions électroniques, en raison "
      "d’une main-d’œuvre abondante et peu coûteuse. Le développement "
      "sud-coréen illustre donc le caractère dynamique des avantages "
      "comparatifs : ceux-ci se construisent par l’accumulation de capital, "
      "de compétences et de connaissances.",
  diss="Conséquence théorique majeure : si les avantages comparatifs sont "
       "construits, la politique industrielle peut modifier la spécialisation "
       "future d’un pays."),

f(id='q22-n14', sp='c22-13', niv='connaitre', type='qcm', b=4743,
  q="Quelle institution a joué un rôle majeur dans la politique industrielle "
    "japonaise du rattrapage ?",
  opts=["Le MITI, ministère chargé de l’industrie et du commerce "
        "international",
        "La Banque du Japon",
        "La DARPA",
        "Le Commissariat général au Plan"],
  ans=0,
  why=["La banque centrale conduit la politique monétaire, non la politique "
       "industrielle.",
       "La DARPA est l’agence américaine créée en 1958, rattachée au "
       "Department of Defense.",
       "Le Commissariat général au Plan est l’institution française créée en "
       "1946."],
  exp="Le Japon connaît une phase spectaculaire de rattrapage après la "
      "Seconde Guerre mondiale, avec une croissance annuelle moyenne proche "
      "de 9 % dans les années 1960. Le MITI — ministère japonais chargé de "
      "l’industrie et du commerce international — a pour objectif "
      "d’organiser et d’accélérer ce rattrapage industriel.",
  diss="Trois institutions à ne pas confondre : MITI (Japon), Commissariat "
       "général au Plan (France, 1946), DARPA (États-Unis, 1958)."),

f(id='q22-n15', sp='c22-13', niv='comprendre', type='qcm', b=4759,
  q="En quoi le modèle japonais se distingue-t-il des stratégies "
    "d’industrialisation qui ont échoué ?",
  opts=["Il refusait toute protection douanière",
        "Il associait une protection extérieure temporaire à une concurrence "
        "maintenue entre entreprises sur le marché intérieur",
        "Il reposait sur la nationalisation des grandes entreprises",
        "Il interdisait les exportations pour privilégier le marché national"],
  ans=1,
  why=["Le Japon protégeait au contraire fortement certaines industries, "
       "l’automobile notamment.",
       "Les entreprises japonaises concernées restaient privées.",
       "L’orientation vers l’exportation est au contraire une caractéristique "
       "du modèle asiatique."],
  exp="L’idée est proche du protectionnisme éducateur de List : les "
      "entreprises japonaises sont temporairement protégées de la concurrence "
      "internationale, mais elles continuent à se concurrencer entre elles "
      "sur le marché intérieur. On évite ainsi l’équation « protection "
      "extérieure = monopole intérieur ». Les entreprises disposent d’un "
      "marché protégé pour apprendre, tout en restant suffisamment nombreuses "
      "pour que la concurrence stimule productivité et innovation.",
  diss="Formule à mémoriser : protection extérieure + concurrence intérieure "
       "→ apprentissage et innovation."),

f(id='q22-n16', sp='c22-13', niv='raisonner', type='qcm', b=4769,
  q="Qu’est-ce qui rend le protectionnisme automobile japonais réellement "
    "« éducateur », selon le cours ?",
  opts=["Le niveau très élevé des droits de douane appliqués aux importations",
        "Son caractère temporaire et programmé, qui donnait aux producteurs "
        "un temps limité pour atteindre les standards internationaux",
        "L’interdiction des investissements étrangers dans le secteur",
        "Le soutien direct de la banque centrale au secteur automobile"],
  ans=1,
  why=["Le niveau de la protection existait bien, mais il n’est pas "
       "l’élément déterminant : une protection élevée et permanente aurait "
       "produit l’effet inverse.",
       "L’interdiction des investissements étrangers n’est pas l’argument "
       "retenu ici.",
       "La politique monétaire n’intervient pas dans ce raisonnement."],
  exp="Le Japon protège fortement son industrie automobile, notamment par des "
      "droits de douane importants sur les importations. Mais l’élément "
      "déterminant n’est pas le niveau de la protection : c’est son caractère "
      "temporaire et programmé. Les producteurs japonais savent que la "
      "protection diminuera progressivement : ils disposent donc d’un temps "
      "limité pour atteindre les standards internationaux de productivité et "
      "de qualité.",
  diss="C’est l’exacte différence avec « l’industrie infantile qui ne devient "
       "jamais adulte » : ici, l’échéance était crédible."),

f(id='q22-n17', sp='c22-13', niv='appliquer', type='ordre', b=4775,
  q="Remettez dans l’ordre le mécanisme du protectionnisme éducateur tel "
    "qu’il a fonctionné dans l’automobile japonaise.",
  ans=["Une protection temporaire est mise en place, avec une échéance connue",
       "Les producteurs disposent d’un marché intérieur protégé",
       "Ils y réalisent un apprentissage industriel",
       "La productivité et la qualité augmentent",
       "La protection est progressivement retirée et les entreprises sont "
       "exposées à la concurrence mondiale"],
  exp="C’est l’enchaînement du cours : protection temporaire → marché "
      "intérieur protégé → apprentissage → productivité ↑ → qualité ↑ → "
      "protection progressivement retirée → exposition à la concurrence "
      "mondiale. La dernière étape est essentielle : sans elle, la protection "
      "cesse d’être éducatrice et devient une rente.",
  diss="Comparer avec le mécanisme inverse — protection permanente → rente ↑ "
       "→ productivité ↓ — fournit un plan de partie tout prêt."),

f(id='q22-n18', sp='c22-13', niv='connaitre', type='qcm', b=4781,
  q="À qui le cours associe-t-il le développement du système Toyota, puis du "
    "toyotisme ?",
  opts=["Frederick Taylor",
        "Taiichi Ohno",
        "Henry Ford",
        "Michael Porter"],
  ans=1,
  why=["Taylor est l’auteur de l’organisation scientifique du travail, "
       "antérieure et de logique différente.",
       "Ford est associé à la production de masse standardisée, précisément "
       "ce que le toyotisme transforme.",
       "Porter analyse la stratégie et la chaîne de valeur, non "
       "l’organisation de la production japonaise."],
  exp="Avec Taiichi Ohno se développe le système Toyota, puis le toyotisme, "
      "également appelé lean production. Ses principes sont la réduction des "
      "stocks, les flux tendus, l’amélioration continue, le contrôle de "
      "qualité et la flexibilité de la production. Le rattrapage japonais ne "
      "repose donc pas seulement sur le soutien public, mais aussi sur une "
      "innovation organisationnelle propre.",
  diss="Argument fort : le Japon ne se contente pas de rattraper les "
       "technologies occidentales, il crée ses propres innovations "
       "organisationnelles."),

f(id='q22-n19', sp='c22-13', niv='comprendre', type='qcmm', b=4786,
  q="Quels principes caractérisent le toyotisme, selon le cours ? (plusieurs "
    "réponses)",
  opts=["La réduction des stocks et les flux tendus",
        "L’amélioration continue",
        "Le contrôle de qualité",
        "La flexibilité de la production",
        "La constitution de stocks de sécurité importants"],
  ans=[0, 1, 2, 3],
  why=["Exacte : les flux tendus limitent le capital immobilisé en stocks.",
       "Exacte : l’amélioration continue associe les salariés au progrès de "
       "l’organisation.",
       "Exacte : la qualité est intégrée au processus et non contrôlée "
       "seulement en fin de chaîne.",
       "Exacte : la flexibilité permet d’adapter la production à la demande.",
       "Inexacte : le toyotisme réduit au contraire les stocks."],
  exp="Les conséquences de ces principes sont une hausse de la productivité "
      "et de la qualité, une diminution du gaspillage et une amélioration "
      "simultanée de la compétitivité-prix et de la compétitivité hors-prix. "
      "C’est ce qui permet aux entreprises japonaises de devenir des "
      "concurrentes directes des producteurs occidentaux.",
  diss="Articulation utile : le toyotisme montre que la compétitivité "
       "hors-prix peut venir de l’organisation, et non seulement de la "
       "technologie."),

f(id='q22-n20', sp='c22-13', niv='raisonner', type='courte', b=4818,
  q="Quel résultat paradoxal la réussite du rattrapage japonais a-t-elle "
    "produit ?",
  ans={'modele': "Une fois les entreprises japonaises devenues pleinement "
       "compétitives, les pays occidentaux leur ont reproché les aides "
       "publiques reçues, la protection antérieure et certaines pratiques "
       "commerciales : le Japon s’est vu accuser de concurrence déloyale. Le "
       "paradoxe est que ces accusations portent sur les instruments qui "
       "avaient précisément permis l’apprentissage industriel. Autrement dit, "
       "le protectionnisme éducateur a réussi : il a fait émerger de nouveaux "
       "concurrents. Le Japon devient alors une menace pour les avantages "
       "comparatifs historiques des économies avancées, et les moyens de son "
       "rattrapage deviennent eux-mêmes l’objet de la critique. On retrouve "
       "exactement cette configuration avec la Chine contemporaine, dont la "
       "trajectoire présente de fortes ressemblances.",
       'cles': [{'f': ['concurrence deloyale', 'deloyal', 'accus'],
                 'l': "des accusations de concurrence déloyale"},
                {'f': ['aide publique', 'subvention', 'protection anterieure',
                       'pratique commerciale'],
                 'l': "le reproche porte sur les aides et la protection antérieure"},
                {'f': ['reussi', 'nouveaux concurrents', 'emerger', 'educateur'],
                 'l': "le protectionnisme éducateur a réussi à faire émerger des concurrents"},
                {'f': ['avantage comparatif', 'menace', 'historique'],
                 'l': "une menace pour les avantages comparatifs des pays avancés"},
                {'f': ['chine', 'ressemblance', 'contemporain'],
                 'l': "une configuration que l'on retrouve avec la Chine"}]},
  exp="Le succès du rattrapage japonais transforme progressivement un pays "
      "protégé en concurrent de premier plan : les instruments qui avaient "
      "permis l’apprentissage industriel deviennent alors eux-mêmes l’objet "
      "de critiques pour distorsion de concurrence.",
  diss="Ce paradoxe permet une transition très élégante entre la partie "
       "consacrée au rattrapage et celle consacrée aux tensions "
       "commerciales contemporaines."),

f(id='q22-n21', sp='c22-13', niv='comprendre', type='qcmm', b=4821,
  q="Quels éléments du modèle asiatique de développement la Chine "
    "reprend-elle, selon le cours ? (plusieurs réponses)",
  opts=["Une montée progressive en gamme",
        "Un soutien massif aux entreprises",
        "La volonté de construire des champions nationaux",
        "Le développement des capacités technologiques",
        "Une orientation vers les exportations",
        "Le refus de tout investissement étranger sur son territoire"],
  ans=[0, 1, 2, 3, 4],
  why=["Exacte : productions intensives en travail, puis produits "
       "manufacturés complexes, puis technologies de pointe.",
       "Exacte : subventions, prêts à taux avantageux, instruments "
       "financiers, soutien à la R&D, marchés publics, politiques "
       "sectorielles.",
       "Exacte : la construction de champions est un objectif explicite.",
       "Exacte : le développement technologique est au cœur de la stratégie.",
       "Exacte : l’exportation reste un moteur du rattrapage.",
       "Inexacte : la Chine a au contraire accueilli des IDE, mais sous "
       "conditions."],
  exp="On retrouve donc une construction progressive des avantages "
      "comparatifs, selon la même logique qu’en Corée : la spécialisation "
      "initiale n’est pas conservée mais dépassée. Les trajectoires coréenne "
      "puis chinoise montrent que la montée en gamme peut résulter d’une "
      "politique industrielle prolongée combinant financement public, "
      "apprentissage technologique, investissement dans le capital humain et "
      "orientation vers des secteurs de plus en plus complexes.",
  diss="À mobiliser pour expliquer le deuxième choc chinois : il est le "
       "produit attendu d’une stratégie de montée en gamme, non un accident."),

f(id='q22-n22', sp='c22-13', niv='comprendre', type='qcm', b=4848,
  q="Comment la Chine a-t-elle utilisé l’accueil des entreprises étrangères "
    "dans sa stratégie de rattrapage ?",
  opts=["En interdisant aux entreprises étrangères de produire sur son "
        "territoire",
        "En associant l’accueil de certaines entreprises étrangères à des "
        "transferts de technologie",
        "En rachetant systématiquement les filiales étrangères implantées",
        "En réservant les IDE au secteur agricole"],
  ans=1,
  why=["L’interdiction aurait privé la Chine de la diffusion technologique "
       "qu’elle recherchait.",
       "Le rachat systématique n’est pas le mécanisme décrit par le cours.",
       "Les secteurs concernés sont industriels et technologiques, non "
       "agricoles."],
  exp="Le rattrapage chinois ne repose pas seulement sur des politiques "
      "internes mais aussi sur l’acquisition de technologies étrangères, "
      "notamment par des IDE sous conditions : l’accueil de certaines "
      "entreprises étrangères a pu être associé à des transferts de "
      "technologie. L’objectif est l’enchaînement suivant : l’entreprise "
      "étrangère s’implante, les techniques sont diffusées, les entreprises "
      "chinoises apprennent, la montée en gamme s’accélère.",
  diss="Rapprochement contemporain remarquable : le projet européen "
       "d’Industrial Accelerator Act envisage de conditionner certains IDE, "
       "en s’inspirant de stratégies utilisées historiquement par la Chine."),

f(id='q22-n23', sp='c22-13', niv='raisonner', type='qcm', b=4871,
  q="Quelle difficulté le rattrapage chinois soulève-t-il en matière de "
    "concurrence internationale ?",
  opts=["Il montre que les transferts de technologie sont toujours illégaux",
        "Il rend difficile la distinction entre apprentissage technologique "
        "légitime et pratiques susceptibles de fausser la concurrence",
        "Il prouve que la propriété intellectuelle n’a aucune valeur "
        "économique",
        "Il démontre que la politique industrielle est inefficace"],
  ans=1,
  why=["Le cours invite précisément à distinguer ce qui relève de politiques "
       "publiques de rattrapage et ce qui constitue éventuellement une "
       "violation des règles internationales.",
       "La protection de la propriété intellectuelle est au contraire au "
       "cœur des tensions, ce qui montre son enjeu économique.",
       "Le rattrapage chinois atteste au contraire de l’efficacité possible "
       "d’une politique industrielle prolongée."],
  exp="Les tensions portent sur les transferts technologiques, les brevets, "
      "les licences, la protection de la propriété intellectuelle et des "
      "accusations de captation ou de copie technologique. Il faut distinguer "
      "ce qui relève de politiques publiques de rattrapage — légitimes, et "
      "pratiquées par le Japon ou la Corée avant la Chine — et ce qui "
      "constitue éventuellement une violation des règles internationales. "
      "C’est précisément cette frontière qui nourrit les conflits commerciaux "
      "contemporains.",
  diss="Formule prudente et juste : la difficulté est moins de condamner que "
       "de tracer la frontière."),

f(id='q22-n24', sp='c22-13', niv='raisonner', type='courte', b=4887,
  q="Qu’est-ce que les expériences asiatiques permettent de retenir sur les "
    "conditions de réussite d’une politique industrielle ?",
  ans={'modele': "Une politique industrielle peut réussir lorsqu’elle associe "
       "une protection temporaire, le maintien d’une concurrence interne "
       "et/ou internationale, des exigences de résultats imposées aux "
       "bénéficiaires, un soutien financier, une orientation vers les "
       "exportations, un investissement dans l’éducation et la R&D, et une "
       "montée progressive en gamme. À l’inverse, l’association d’une "
       "protection permanente, d’une absence de concurrence et d’aides sans "
       "conditions engendre un risque de rente et d’inefficacité. Les succès "
       "asiatiques ne valident donc pas n’importe quelle intervention "
       "publique : ils montrent plutôt qu’une politique industrielle efficace "
       "impose une discipline aux entreprises protégées, notamment par "
       "l’exportation, par la concurrence et par l’obligation de monter "
       "progressivement en gamme. La protection est un moyen d’apprentissage, "
       "pas une fin.",
       'cles': [{'f': ['temporaire', 'duree limitee', 'echeance'],
                 'l': "une protection temporaire et non permanente"},
                {'f': ['concurrence', 'discipline', 'pression'],
                 'l': "le maintien d'une concurrence et d'une discipline"},
                {'f': ['exigence', 'condition', 'resultat', 'contrepartie'],
                 'l': "des exigences de résultats et des aides conditionnelles"},
                {'f': ['exportation', 'exporter', 'marche mondial'],
                 'l': "l'orientation vers les exportations"},
                {'f': ['education', 'r&d', 'recherche', 'formation'],
                 'l': "l'investissement dans l'éducation et la R&D"},
                {'f': ['montee en gamme', 'monter en gamme', 'gamme'],
                 'l': "la montée progressive en gamme"},
                {'f': ['rente', 'inefficacite', 'sans condition', 'permanente'],
                 'l': "à l'inverse : protection permanente et aides sans conditions → rente"}]},
  exp="Les succès asiatiques ne valident pas n’importe quelle intervention "
      "publique : ils montrent plutôt qu’une politique industrielle efficace "
      "impose une discipline aux entreprises protégées, notamment par "
      "l’exportation, la concurrence et l’obligation de monter progressivement "
      "en gamme.",
  diss="Conclusion de partie très solide : la question n’est pas « faut-il "
       "une politique industrielle ? » mais « à quelles conditions ? »."),

f(id='q22-n25', sp='c22-13', niv='appliquer', type='assoc', b=4885,
  q="Classez chaque caractéristique selon qu’elle relève, d’après le cours, "
    "d’une politique industrielle plutôt réussie ou plutôt vouée à l’échec.",
  ans=[["Une protection assortie d’une échéance connue à l’avance",
        "Plutôt réussie"],
       ["Des aides accompagnées d’exigences de résultats à l’exportation",
        "Plutôt réussie"],
       ["Le maintien d’une concurrence entre plusieurs entreprises nationales",
        "Plutôt réussie"],
       ["Une protection maintenue durablement sans échéance",
        "Plutôt vouée à l’échec"],
       ["Des aides versées sans condition ni évaluation",
        "Plutôt vouée à l’échec"],
       ["La création d’un monopole national à l’abri de toute concurrence",
        "Plutôt vouée à l’échec"]],
  exp="Le critère discriminant n’est pas l’intensité du soutien public mais "
      "la présence d’une discipline : échéance de la protection, "
      "conditionnalité des aides, maintien d’une concurrence. Les stratégies "
      "qui ont échoué ont protégé durablement des entreprises inefficaces, "
      "supprimé la pression concurrentielle, créé des monopoles nationaux peu "
      "innovants et maintenu artificiellement des secteurs non compétitifs.",
  diss="Grille d’évaluation directement applicable aux politiques "
       "industrielles contemporaines, IRA et Industrial Accelerator Act "
       "compris."),

f(id='q22-n26', sp='c22-13', niv='raisonner', type='vf', b=4887,
  q="Les réussites asiatiques montrent que toute intervention publique "
    "massive en faveur de l’industrie conduit au développement.",
  ans=False,
  exp="Les succès asiatiques ne valident pas n’importe quelle intervention "
      "publique. Plusieurs politiques d’industrialisation ont échoué "
      "précisément parce qu’elles protégeaient durablement des entreprises "
      "inefficaces et supprimaient la pression concurrentielle. Ce que ces "
      "réussites établissent est plus exigeant : une politique industrielle "
      "efficace impose une discipline aux entreprises qu’elle protège, par "
      "l’exportation, par la concurrence et par l’obligation de monter "
      "progressivement en gamme.",
  diss="Erreur classique à éviter en dissertation : citer la Corée ou le "
       "Japon comme preuve que « l’État réussit », alors qu’ils prouvent que "
       "« l’État réussit sous conditions »."),

f(id='q22-n27', sp='c22-13', niv='connaitre', type='qcm', b=4895,
  q="Pourquoi les pays avancés renouent-ils eux-mêmes avec des politiques "
    "industrielles ciblées depuis le début du XXIᵉ siècle ?",
  opts=["Parce que leur croissance démographique s’accélère",
        "Parce que leur environnement a changé : désindustrialisation, montée "
        "en puissance technologique chinoise, crises sanitaires, tensions "
        "énergétiques, dépendances stratégiques et rivalités géopolitiques",
        "Parce que les règles de l’OMC les y obligent",
        "Parce que les délocalisations ont totalement cessé"],
  ans=1,
  why=["La démographie n’est pas invoquée par le cours pour expliquer ce "
       "retour.",
       "Les règles de l’OMC vont au contraire plutôt à l’encontre de "
       "certaines de ces mesures.",
       "Les délocalisations n’ont pas cessé, même si leur rythme mesuré a "
       "diminué."],
  exp="Les expériences asiatiques étaient principalement des politiques de "
      "rattrapage et de développement. Mais la politique industrielle ne "
      "concerne plus seulement les économies émergentes : l’environnement des "
      "pays avancés s’est transformé, ce qui conduit à une nouvelle logique, "
      "celle de la politique industrielle face au défi de la souveraineté "
      "dans un monde fragmenté.",
  diss="Articulation de plan : le rattrapage explique les politiques "
       "industrielles du Sud, la souveraineté celles du Nord."),

]
