# -*- coding: utf-8 -*-
"""Chapitre 7 — complément de questions « Appliquer ».

Le chapitre comptait peu de questions de niveau « Appliquer ». Ces
exercices portent sur la lecture des indicateurs du développement, le
dividende démographique, la séquence du vol d'oies sauvages et les
stratégies d'industrialisation. Chaque renvoi a été vérifié dans le cours.
"""


def f(**kw):
    return kw


L = [

f(id='q7-m01', sp='c7-03', niv='appliquer', type='qcm', b=660,
  q="Un pays occupe le 40ᵉ rang mondial pour son RNB par habitant mais le "
    "25ᵉ pour son IDH. Comment lire cet écart ?",
  opts=["Il transforme relativement bien sa richesse en santé et en "
        "éducation",
        "Il transforme mal sa richesse en développement humain",
        "Son IDH est nécessairement supérieur à 0,9",
        "L’écart n’a pas de sens : les deux classements sont indépendants"],
  ans=0,
  why=["Ce serait le cas inverse : un rang d’IDH moins bon que le rang de "
       "revenu.",
       "Le rang ne dit rien du niveau : un pays peut être bien classé avec un "
       "IDH modéré.",
       "C’est précisément la comparaison des deux rangs que le cours "
       "présente comme « l’un des éléments les plus intéressants »."],
  exp="L’écart entre les deux classements est l’information utile : il "
      "mesure la capacité d’un pays à convertir ses ressources en santé et "
      "en éducation. Un rang d’IDH meilleur que le rang de revenu signale "
      "une conversion efficace — le cours cite le Costa Rica. Le cas "
      "inverse — rang de revenu bien meilleur que le rang d’IDH — signale "
      "une richesse mal transformée, souvent une rente peu redistribuée.",
  diss="Comparer deux classements plutôt que de citer un niveau est la "
       "manière la plus économique de montrer que croissance et "
       "développement ne coïncident pas."),

f(id='q7-m02', sp='c7-01', niv='appliquer', type='qcm', b=211,
  q="Pourquoi la Banque mondiale classe-t-elle les pays d’après leur RNB par "
    "habitant plutôt que d’après leur seul PIB par habitant ?",
  opts=["Parce que le RNB tient compte des revenus perçus de l’étranger et "
        "versés à l’étranger, ce qui compte dans une économie mondialisée",
        "Parce que le RNB intègre l’espérance de vie et l’éducation",
        "Parce que le PIB n’est pas mesurable dans les pays en développement",
        "Parce que le RNB est exprimé en parité de pouvoir d’achat et le PIB "
        "jamais"],
  ans=0,
  why=["Santé et éducation relèvent de l’IDH, pas du RNB, qui reste un "
       "agrégat monétaire.",
       "Le PIB est mesuré partout ; la difficulté porte sur la qualité des "
       "données, non sur la possibilité.",
       "Les deux agrégats peuvent être convertis en parité de pouvoir "
       "d’achat : ce n’est pas ce qui les distingue."],
  exp="Le PIB mesure ce qui est produit sur le territoire ; le RNB mesure ce "
      "qui revient aux résidents, en ajoutant les revenus reçus de "
      "l’étranger et en retranchant ceux versés à l’étranger. L’écart est "
      "important là où les profits sont largement rapatriés par des firmes "
      "étrangères, ou là où les transferts des travailleurs émigrés pèsent "
      "lourd. Le cours souligne que ce choix est lié à la mondialisation, "
      "sans pour autant épuiser la mesure du développement.",
  diss="La distinction PIB / RNB est décisive pour les économies minières ou "
       "fortement dépendantes de l’investissement étranger : la production "
       "locale n’est pas le revenu local."),

f(id='q7-m03', sp='c7-05', niv='appliquer', type='qcm', b=833,
  q="L’IDH d’un pays passe de 0,70 à 0,75. Que sait-on exactement, et que "
    "ne sait-on pas ?",
  opts=["On sait que le développement humain progresse, mais pas si "
        "l’amélioration vient de la santé, de l’éducation ou du revenu",
        "On sait que l’espérance de vie a progressé",
        "On sait que le revenu par habitant a augmenté de 5 %",
        "On ne sait rien : l’IDH n’est pas comparable dans le temps"],
  ans=0,
  why=["L’espérance de vie n’est qu’une des trois dimensions agrégées : elle "
       "peut être restée stable.",
       "La variation de l’indice ne se traduit pas en pourcentage de revenu : "
       "les trois composantes sont normalisées puis combinées.",
       "L’IDH est précisément conçu pour la comparaison, dans le temps comme "
       "entre pays."],
  exp="C’est la rançon de tout indicateur composite : « quand l’indicateur "
      "évolue, on ne sait pas immédiatement ce qui a changé ». Le cours en "
      "tire une règle de méthode — la multiplication des indicateurs « ne "
      "supprime pas la difficulté d’analyse : elle la déplace. On gagne en "
      "précision, mais on perd en lisibilité immédiate » — et explique "
      "ainsi pourquoi les indicateurs monétaires, plus pauvres mais "
      "lisibles, n’ont pas disparu.",
  diss="Savoir dire ce qu’un indicateur ne dit pas est ce qui distingue une "
       "copie qui commente des chiffres d’une copie qui les analyse."),

f(id='q7-m04', sp='c7-04', niv='appliquer', type='assoc', b=868,
  q="Associez chaque prolongement de l’IDH à la dimension qu’il ajoute.",
  ans=[["IDHI", "L’IDH corrigé des inégalités internes de la population"],
       ["IIG", "Les inégalités entre les femmes et les hommes"],
       ["IPM", "La pauvreté comme ensemble de privations concrètes"],
       ["IDHP", "La pression exercée sur la planète, introduite en 2020"]],
  exp="Chaque prolongement répond à une critique précise adressée à l’IDH : "
      "il raisonne en moyennes, donc ignore la dispersion — d’où l’IDHI ; il "
      "agrège hommes et femmes, donc masque les écarts de genre — d’où "
      "l’IIG ; il réduit la pauvreté au revenu, alors qu’elle est faite de "
      "privations multiples — d’où l’IPM ; il ignore le coût "
      "environnemental du développement — d’où l’IDHP. Tous s’inscrivent "
      "dans la perspective d’Amartya Sen.",
  diss="Présenter les indicateurs comme des réponses à des critiques, et non "
       "comme une liste, montre que la mesure du développement est un "
       "chantier ouvert."),

f(id='q7-m05', sp='c7-06', niv='appliquer', type='qcm', b=1123,
  q="Dans un pays, la natalité a fortement baissé et les générations "
    "nombreuses nées auparavant arrivent à l’âge actif. Quel phénomène "
    "s’ouvre, et à quelle condition produit-il ses effets ?",
  opts=["Le dividende démographique : il ne se réalise que si l’économie est "
        "capable d’employer ces actifs",
        "La transition démographique, qui garantit mécaniquement la "
        "croissance",
        "Le piège malthusien, la population croissant plus vite que les "
        "ressources",
        "Le vieillissement démographique, qui pèse sur les finances "
        "publiques"],
  ans=0,
  why=["La transition est le cadre d’ensemble ; le dividende en est un moment "
       "particulier, et rien n’y est mécanique.",
       "Le piège malthusien suppose une population croissant plus vite que "
       "les subsistances : ce n’est pas la situation décrite.",
       "Le vieillissement correspond à la phase suivante, lorsque ces "
       "générations atteignent l’âge de la retraite."],
  exp="Le dividende démographique est « le gain potentiel de croissance lié "
      "à l’augmentation temporaire de la part de la population en âge de "
      "travailler ». Deux mots importent : potentiel et temporaire. "
      "Potentiel, parce que le gain n’advient que si l’économie crée les "
      "emplois correspondants — sinon la même évolution produit du chômage "
      "de masse. Temporaire, parce que la fenêtre se referme avec le "
      "vieillissement de ces mêmes générations.",
  diss="Le caractère conditionnel du dividende est l’argument qui relie "
       "démographie et politiques d’éducation et d’emploi : la structure par "
       "âge n’est qu’une opportunité."),

f(id='q7-m06', sp='c7-14', niv='appliquer', type='ordre', b=2764,
  q="Remettez dans l’ordre la séquence du rattrapage industriel décrite par "
    "le modèle du vol d’oies sauvages.",
  ans=["Le pays importe le bien, qu’il ne sait pas encore produire",
       "Il le produit localement, d’abord pour son marché intérieur",
       "Il l’exporte, une fois sa production compétitive",
       "Il abandonne cette production à des pays suiveurs et se déplace vers "
       "des biens plus élaborés"],
  exp="La séquence importer-produire-exporter-déléguer fait tout l’intérêt du "
      "modèle : elle montre que substitution aux importations et promotion "
      "des exportations ne s’opposent pas nécessairement, mais peuvent se "
      "succéder. Elle décrit aussi une division régionale du travail "
      "hiérarchisée, où les productions descendent du pays leader vers les "
      "suiveurs à mesure que celui-ci monte en gamme — ce qui en fait une "
      "lecture dynamique des avantages comparatifs.",
  diss="La séquence permet de dépasser l’opposition scolaire ISI / promotion "
       "des exportations : le débat porte sur le moment du basculement, pas "
       "sur le choix d’un camp."),

f(id='q7-m07', sp='c7-15', niv='raisonner', type='qcm', b=3022,
  q="Quelle limite majeure le cours oppose-t-il au modèle du vol d’oies "
    "sauvages appliqué au Japon ?",
  opts=["Il donne l’impression d’un développement naturel et fluide, en "
        "sous-estimant le rôle de l’État, la puissance des zaibatsu et le "
        "contexte géopolitique",
        "Il surestime le rôle des exportations",
        "Il ne s’applique qu’aux pays européens",
        "Il contredit la théorie des avantages comparatifs"],
  ans=0,
  why=["Les exportations tiennent effectivement une place centrale dans le "
       "rattrapage japonais : ce n’est pas le point critiqué.",
       "Le modèle est précisément construit à partir de l’Asie orientale.",
       "Le cours le présente au contraire comme compatible avec une vision "
       "dynamique des avantages comparatifs."],
  exp="La critique porte sur ce que le modèle laisse hors champ. Présenté "
      "comme une mécanique séquentielle, il peut faire croire à un "
      "enchaînement « presque naturel, fluide et harmonieux ». Or le cours "
      "insiste : l’État japonais a encadré, protégé et financé le "
      "rattrapage, les zaibatsu ont concentré les moyens, et le contexte "
      "géopolitique a joué. Le modèle décrit donc une trajectoire, mais "
      "n’explique pas ses conditions politiques.",
  diss="Distinguer ce qu’un modèle décrit de ce qu’il explique est une "
       "exigence méthodologique : elle permet d’utiliser le vol d’oies "
       "sauvages sans en faire une loi du développement."),

f(id='q7-m08', sp='c7-02', niv='appliquer', type='qcm', b=245,
  q="Pourquoi la pauvreté mondiale se mesure-t-elle en termes absolus, alors "
    "que les pays riches raisonnent souvent en termes relatifs ?",
  opts=["Parce qu’un seuil fixe de revenu ou de consommation permet de "
        "compter ceux qui ne couvrent pas leurs besoins essentiels, "
        "indépendamment du niveau de vie moyen du pays",
        "Parce que la pauvreté relative n’existe pas dans les pays pauvres",
        "Parce que le revenu médian n’est pas mesurable hors des pays "
        "développés",
        "Parce que la Banque mondiale ne dispose pas de données sur les "
        "revenus"],
  ans=0,
  why=["La pauvreté relative existe partout : c’est l’objet de la mesure qui "
       "diffère.",
       "Le revenu médian se mesure aussi ailleurs ; le choix du seuil absolu "
       "répond à un autre besoin.",
       "La Banque mondiale fonde justement ses estimations sur des enquêtes "
       "de revenu et de consommation."],
  exp="Les deux approches répondent à des questions différentes. La pauvreté "
      "relative — un pourcentage du revenu médian — mesure une distance au "
      "mode de vie dominant : elle décrit une exclusion sociale. La pauvreté "
      "absolue fixe un seuil minimal de revenu ou de consommation et compte "
      "ceux qui vivent en dessous : elle décrit une privation vitale, "
      "comparable d’un pays à l’autre. C’est cette comparabilité "
      "internationale qui justifie le choix de la Banque mondiale.",
  diss="Rappeler que la pauvreté absolue peut reculer pendant que la pauvreté "
       "relative progresse évite la confusion la plus fréquente sur les "
       "chiffres du développement."),

f(id='q7-m09', sp='c7-03', niv='appliquer', type='qcm', b=321,
  q="Le cours relève un écart d’espérance de vie pouvant dépasser trente ans "
    "entre des pays comme le Tchad et Hong Kong. Quelle conclusion en "
    "tire-t-il ?",
  opts=["Que le revenu ne suffit pas à résumer le développement : "
        "l’espérance de vie reflète la qualité globale de l’environnement "
        "sanitaire et social",
        "Que le PIB par habitant est mal mesuré dans les pays pauvres",
        "Que l’espérance de vie est un meilleur indicateur que l’IDH",
        "Que les écarts de développement se réduisent"],
  ans=0,
  why=["La qualité des données est un problème distinct, qui n’est pas "
       "l’objet de cette comparaison.",
       "L’espérance de vie est l’une des trois composantes de l’IDH, non un "
       "substitut à celui-ci.",
       "L’exemple illustre au contraire l’ampleur persistante des écarts."],
  exp="L’argument est un argument par l’écart : si le revenu résumait le "
      "développement, un écart de trente ans d’espérance de vie serait "
      "inexplicable. L’espérance de vie « ne dit pas seulement combien de "
      "temps une population vit : elle reflète aussi la qualité globale de "
      "l’environnement sanitaire et social ». C’est ce constat qui justifie "
      "la construction d’indicateurs multidimensionnels, à commencer par "
      "l’IDH.",
  diss="Un écart extrême bien choisi est souvent plus probant qu’une moyenne : "
       "il établit en une phrase l’insuffisance d’un indicateur unique."),

f(id='q7-m10', sp='c7-01', niv='raisonner', type='courte', b=22,
  q="La Chine est la deuxième économie mondiale. Peut-on en conclure qu’elle "
    "est un pays développé ? Argumentez à partir du cours.",
  ans={'modele':
       "Non, et le cas chinois sert précisément à montrer que croissance et "
       "développement ne se confondent pas. La puissance économique globale "
       "ne dit rien du niveau de vie moyen ni de sa répartition : la Chine "
       "conserve des inégalités internes importantes et des indicateurs "
       "sociaux qui, selon les critères retenus, ne la placent pas au niveau "
       "des économies les plus avancées. Son IDH la situe dans une position "
       "intermédiaire : forte progression, mais pas convergence totale. Le "
       "cas invite donc à abandonner l’opposition simple entre pays "
       "développés et pays en développement, au profit d’une lecture "
       "croisant plusieurs indicateurs.",
       'cles': [{'f': ['inegalit'], 'l': 'des inégalités internes importantes'},
                {'f': ['idh'], 'l': 'un IDH en position intermédiaire'},
                {'f': ['par habitant', 'moyen', 'population'],
                 'l': 'la taille de l’économie n’est pas le niveau de vie'},
                {'f': ['opposition', 'bloc', 'homogene', 'categorie'],
                 'l': 'l’opposition développés / en développement est trop simple'}]},
  exp="Le cours ouvre sur ce cas parce qu’il met en échec les deux "
      "simplifications les plus courantes : réduire le développement à la "
      "taille de l’économie, et répartir le monde en deux blocs. Il conclut "
      "que les pays en développement « ne forment pas un bloc homogène, mais "
      "un ensemble profondément fragmenté » — ce qui vaut aussi, "
      "symétriquement, pour les pays réputés développés.",
  diss="Entrer dans un sujet sur le développement par un cas qui résiste au "
       "classement vaut mieux qu’une définition : cela installe d’emblée la "
       "problématique de la mesure."),
]
