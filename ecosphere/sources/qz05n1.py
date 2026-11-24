# -*- coding: utf-8 -*-
"""Chapitre 5 — complément de questions « Appliquer » et « Raisonner ».

Les défaillances de marché se prêtent au cas pratique : classer un bien
par ses deux critères, reconnaître un passager clandestin, distinguer
sélection adverse et aléa moral, choisir entre taxe et négociation, poser
les conditions du théorème de Coase, opposer tragédie des communs et
tragédie des anti-communs. Chaque renvoi a été vérifié dans le cours.
"""


def f(**kw):
    return kw


L = [

# ----------------------------------- c5-01 · monopoles et structure
f(id='q5-m01', sp='c5-01', niv='raisonner', type='qcm', b=136,
  q="Pourquoi le monopole constitue-t-il une défaillance de marché, même "
    "lorsqu’il se justifie par l’innovation ou les rendements croissants ?",
  opts=["Parce qu’il empêche l’égalité entre le prix et le coût marginal, que "
        "la concurrence pure et parfaite garantit",
        "Parce qu’il produit toujours à perte",
        "Parce qu’il est nécessairement public",
        "Parce qu’il ne peut pas innover"],
  ans=0,
  why=["Le monopole dégage au contraire une rente : ce n’est pas sa "
       "rentabilité qui pose problème.",
       "Un monopole peut être privé ou public : le statut n’entre pas dans "
       "la définition de la défaillance.",
       "Le cours admet au contraire que certains monopoles se justifient "
       "précisément par l’innovation."],
  exp="Le critère est l’écart au prix concurrentiel. En concurrence pure et "
      "parfaite, la demande adressée à la firme est parfaitement élastique, "
      "ce qui impose l’égalité du prix, de la recette marginale et du coût "
      "marginal : l’allocation est optimale. Le monopole, lui, fait face à "
      "la demande du marché, fixe un prix supérieur au coût marginal et "
      "réduit les quantités. La défaillance n’est donc pas morale mais "
      "allocative — ce qui n’empêche pas qu’un monopole puisse être "
      "justifié par l’innovation, les rendements croissants ou l’intérêt "
      "général.",
  diss="Formuler la défaillance comme un écart prix / coût marginal permet "
       "de la mesurer, et donc de discuter sérieusement d’une régulation "
       "plutôt que d’un démantèlement."),

f(id='q5-m02', sp='c5-01', niv='appliquer', type='qcm', b=120,
  q="L’utilité d’un réseau social augmente avec le nombre de ses "
    "utilisateurs, ce qui décourage l’entrée de concurrents. De quel type de "
    "monopole s’agit-il ?",
  opts=["Un monopole de réseau : l’utilité du service croît avec le nombre "
        "d’utilisateurs",
        "Un monopole naturel lié aux coûts fixes d’infrastructure",
        "Un monopole d’innovation protégé par un brevet",
        "Un monopole public institué par la loi"],
  ans=0,
  why=["Le monopole naturel tient aux coûts : une seule firme produit à "
       "moindre coût qu’un ensemble de firmes.",
       "Le monopole d’innovation naît d’une avance technologique protégée, "
       "non du nombre d’usagers.",
       "Aucune décision publique n’intervient ici : la position se construit "
       "par l’usage."],
  exp="Le cours distingue les origines du monopole : les coûts — monopole "
      "naturel —, l’avance technologique — monopole d’innovation — et les "
      "effets de réseau, où « l’utilité du service augmente avec le nombre "
      "d’utilisateurs ». Dans ce dernier cas, la barrière à l’entrée n’est "
      "ni technique ni juridique : elle tient à ce que rejoindre un "
      "concurrent moins fréquenté serait, pour chaque utilisateur, une perte "
      "individuelle.",
  diss="Les effets de réseau expliquent pourquoi la concurrence « pour le "
       "marché » remplace souvent la concurrence « sur le marché » dans "
       "l’économie numérique."),

# ------------------------------- c5-02 · biens collectifs et communs
f(id='q5-m03', sp='c5-02', niv='appliquer', type='assoc', b=141,
  q="Classez chaque bien selon les deux critères de rivalité et "
    "d’excluabilité.",
  ans=[["Un pain au chocolat", "Rival et excluable : un bien privé"],
       ["La lumière d’un phare", "Non rival et non excluable : un bien "
                                 "collectif pur"],
       ["Une autoroute à péage", "Non rivale tant qu’elle est fluide, mais "
                                 "excluable : un bien de club"],
       ["Un stock de poissons en haute mer", "Rival mais non excluable : un "
                                             "bien commun"]],
  exp="Les deux critères sont indépendants, et le cours insiste pour qu’on ne "
      "les confonde pas. La rivalité demande : ma consommation empêche-t-elle "
      "celle d’autrui ? L’excluabilité demande : peut-on techniquement "
      "empêcher quelqu’un de consommer ? Croiser les deux donne quatre "
      "catégories, et c’est le cas rival / non excluable — les communs — qui "
      "pose le problème le plus redoutable, puisque chaque usage réduit la "
      "ressource sans qu’on puisse en restreindre l’accès.",
  diss="Ce tableau à quatre cases est l’outil de base pour justifier une "
       "intervention publique : la nature du bien commande le type de "
       "réponse."),

f(id='q5-m04', sp='c5-02', niv='raisonner', type='ordre', b=247,
  q="Remettez dans l’ordre le raisonnement du passager clandestin, tel "
    "qu’Olson l’applique au phare.",
  ans=["Le phare est non excluable : aucun moyen technique n’empêche un "
       "bateau de profiter de sa lumière",
       "Chaque capitaine se dit qu’il bénéficiera du phare même sans payer",
       "Aucun n’a donc intérêt à contribuer volontairement",
       "Personne ne finance, aucun producteur privé ne peut rentabiliser le "
       "bien",
       "Le bien n’est pas produit, bien qu’il soit socialement utile"],
  exp="Le raisonnement n’invoque aucune malhonnêteté : chaque acteur est "
      "rationnel, et c’est précisément la somme de ces rationalités qui "
      "aboutit à un résultat collectivement désastreux. L’origine du blocage "
      "est la non-excluabilité, qui empêche le système de prix de jouer son "
      "rôle. Le cours en tire la conclusion : pour un bien collectif pur, "
      "« une seule solution existe réellement : le financement par "
      "l’impôt ».",
  diss="Le passager clandestin est le modèle de tous les problèmes d’action "
       "collective, de la défense nationale au climat : il justifie la "
       "contrainte là où la bonne volonté ne suffit pas."),

f(id='q5-m05', sp='c5-02', niv='raisonner', type='vf', b=371,
  q="Vrai ou faux : un bien commun et un bien collectif pur posent le même "
    "problème économique. Justifiez.",
  ans=False,
  exp="Ils partagent la non-excluabilité, mais diffèrent par la rivalité, et "
      "cette différence change le problème. Le bien collectif pur est non "
      "rival : le risque est la sous-production, car personne ne veut "
      "financer ce dont tout le monde profite. Le bien commun est rival : "
      "« on ne peut pas empêcher l’accès, mais chaque usage réduit la "
      "quantité disponible ». Le risque n’est donc pas l’absence de "
      "production mais la surexploitation — la tragédie des communs, où « ce "
      "qui est rationnel individuellement devient collectivement "
      "catastrophique ».",
  diss="Distinguer sous-production et surexploitation évite le contresens "
       "le plus fréquent : la solution n’est pas la même, financement public "
       "d’un côté, règle d’usage de l’autre."),

# ------------------------------- c5-03 · externalités et taxe
f(id='q5-m06', sp='c5-03', niv='appliquer', type='qcm', b=517,
  q="Un apiculteur profite gratuitement du champ de fleurs de son voisin. "
    "Quelle conséquence le cours tire-t-il de ce type de situation ?",
  opts=["L’activité qui engendre le bénéfice est sous-produite, parce que "
        "celui qui la mène n’est pas rémunéré pour cet avantage",
        "L’activité est surproduite, puisqu’elle profite à plusieurs agents",
        "Il n’y a pas d’externalité, puisque personne ne subit de coût",
        "Le marché corrige spontanément ce déséquilibre par le prix"],
  ans=0,
  why=["La surproduction caractérise l’externalité négative : le pollueur "
       "produit trop parce qu’il ne supporte pas le coût qu’il impose.",
       "Une externalité peut être positive : elle se définit par l’absence "
       "de contrepartie monétaire, non par l’existence d’un dommage.",
       "C’est tout le problème : la répercussion ne passe justement pas par "
       "le marché, donc le prix ne la reflète pas."],
  exp="Le mécanisme est symétrique. Externalité négative : l’agent n’assume "
      "pas le coût qu’il fait peser sur autrui, donc il produit plus que "
      "l’optimum social. Externalité positive : il ne perçoit pas le "
      "bénéfice qu’il procure à autrui, donc il produit moins. Dans les deux "
      "cas, « le prix de marché ne reflète pas le coût ou le bénéfice réel "
      "pour la société ». Le cours donne plusieurs exemples d’externalités "
      "positives captées sans contrepartie : l’apiculteur, le fast-food près "
      "d’un lycée, le fleuriste près d’un hôpital.",
  diss="Le couple surproduction / sous-production donne la direction de la "
       "correction attendue : taxer dans un cas, subventionner dans "
       "l’autre."),

f(id='q5-m07', sp='c5-03', niv='raisonner', type='qcm', b=797,
  q="Avant de répercuter une taxe sur ses prix, que doit examiner un "
    "producteur, selon le cours ?",
  opts=["L’élasticité-prix de la demande : si la demande est élastique, "
        "répercuter la taxe lui ferait perdre trop de volume",
        "Le niveau de ses coûts fixes uniquement",
        "Le taux de TVA appliqué au produit",
        "La structure de son capital"],
  ans=0,
  why=["Les coûts fixes déterminent le seuil de rentabilité, non le partage "
       "du fardeau fiscal.",
       "Le taux de TVA est un autre prélèvement : il ne commande pas "
       "l’incidence de la taxe considérée.",
       "La structure du capital relève du financement, pas de la décision de "
       "prix."],
  exp="L’incidence d’une taxe — qui la supporte réellement — ne dépend pas de "
      "qui la verse mais des élasticités. Si la demande est peu élastique, "
      "le producteur peut répercuter la taxe sans perdre beaucoup de volume : "
      "le consommateur la supporte. Si elle est élastique, répercuter "
      "reviendrait à perdre des ventes : le producteur en absorbe une part "
      "sur sa marge. Le cours pose exactement cette question : « taxer qui, "
      "producteur ou consommateur ? ».",
  diss="La distinction entre redevable légal et payeur effectif est "
       "indispensable pour juger de la justice d’une fiscalité écologique."),

f(id='q5-m08', sp='c5-03', niv='appliquer', type='qcm', b=799,
  q="Le Royaume-Uni instaure une taxe carbone en 2013 ; la part du charbon "
    "dans sa production électrique passe de 40 % en 2012 à 4 % en 2019. Que "
    "montre cet exemple ?",
  opts=["Qu’un signal-prix suffisamment fort peut déplacer massivement les "
        "comportements, ce qui plaide pour l’efficacité de la taxe "
        "pigouvienne",
        "Que les externalités négatives disparaissent d’elles-mêmes",
        "Que la taxe carbone n’a pas d’effet sur la consommation d’énergie",
        "Que l’effet Jevons annule toujours les gains d’efficacité"],
  ans=0,
  why=["Rien ne disparaît spontanément : c’est précisément l’instrument "
       "fiscal qui produit le résultat.",
       "L’exemple établit l’inverse, avec un chiffre précis.",
       "L’effet Jevons concerne les gains d’efficacité technique qui "
       "abaissent le coût d’usage ; il ne s’applique pas à une taxe qui le "
       "renchérit."],
  exp="L’exemple est utilisé par le cours pour montrer qu’« une taxe carbone "
      "peut être efficace ». Le mécanisme est celui de Pigou : internaliser "
      "l’externalité en faisant payer au pollueur le coût social de son "
      "activité, de sorte que son calcul privé rejoigne le calcul "
      "collectif. La chute de 40 % à 4 % en sept ans donne un ordre de "
      "grandeur rarement atteint par la réglementation seule.",
  diss="Un exemple chiffré et daté vaut mieux qu’une affirmation générale sur "
       "l’efficacité des taxes : il permet d’argumenter sans généraliser."),

# ----------------------- c5-04 · asymétries d’information
f(id='q5-m09', sp='c5-04', niv='appliquer', type='qcm', b=623,
  q="Un automobiliste bien assuré conduit plus vite qu’avant. Une "
    "bibliothèque de voitures d’occasion ne contient plus que des épaves. "
    "Comment nommer ces deux situations ?",
  opts=["Aléa moral dans le premier cas, sélection adverse dans le second",
        "Sélection adverse dans le premier cas, aléa moral dans le second",
        "Aléa moral dans les deux cas",
        "Sélection adverse dans les deux cas"],
  ans=0,
  why=["L’ordre est inversé : la sélection adverse opère avant l’échange, "
       "l’aléa moral après.",
       "La disparition des bonnes voitures est un problème de qualité cachée "
       "avant la transaction, pas de comportement après.",
       "Le changement de conduite après la souscription est un comportement "
       "caché, donc un aléa moral."],
  exp="Le critère est temporel. La sélection adverse joue avant l’échange : "
      "l’acheteur ne peut distinguer les bonnes voitures des mauvaises, il "
      "propose donc un prix moyen, les vendeurs de bonnes voitures se "
      "retirent, et il ne reste que les « lemons » — Akerlof montre ainsi "
      "qu’une asymétrie d’information « peut faire disparaître un marché ». "
      "L’aléa moral joue après : une fois protégé, l’agent adopte un "
      "comportement plus risqué qu’avant.",
  diss="Le couple avant / après l’échange permet de choisir le remède : "
       "signal et certification contre la sélection adverse, franchise et "
       "contrôle contre l’aléa moral."),

f(id='q5-m10', sp='c5-04', niv='raisonner', type='courte', b=618,
  q="Expliquez comment, chez Akerlof, une asymétrie d’information peut faire "
    "disparaître un marché.",
  ans={'modele':
       "Sur le marché des voitures d’occasion, le vendeur connaît la qualité "
       "réelle du véhicule, l’acheteur non. Ne pouvant distinguer les bonnes "
       "voitures des mauvaises, l’acheteur n’accepte de payer qu’un prix "
       "correspondant à la qualité moyenne. Ce prix est trop bas pour les "
       "propriétaires de bons véhicules, qui renoncent à vendre : la qualité "
       "moyenne offerte baisse encore, donc le prix proposé baisse à son "
       "tour. Le mécanisme s’auto-entretient jusqu’à ce qu’il ne reste que "
       "les mauvais produits, voire plus de marché du tout. C’est la "
       "sélection adverse : l’asymétrie chasse les bons produits.",
       'cles': [{'f': ['asymetrie', 'vendeur sait', 'information'],
                 'l': 'le vendeur en sait plus que l’acheteur'},
                {'f': ['prix moyen', 'qualite moyenne'],
                 'l': 'l’acheteur ne paie qu’un prix moyen'},
                {'f': ['bons', 'bonne qualite', 'se retire', 'quittent'],
                 'l': 'les bons produits se retirent'},
                {'f': ['selection adverse', 'anti selection'],
                 'l': 'c’est la sélection adverse'},
                {'f': ['disparai', 'effondre', 'plus de marche'],
                 'l': 'le marché peut disparaître'}]},
  exp="The Market for Lemons (1970) montre que le prix, censé transmettre "
      "l’information, ne peut plus le faire lorsque la qualité est cachée : "
      "il devient une moyenne qui pénalise les bons produits. Le résultat "
      "est contre-intuitif et puissant : ce n’est pas la malhonnêteté qui "
      "détruit le marché, c’est la seule inégalité d’information, même "
      "entre agents honnêtes.",
  diss="Akerlof fournit l’argument le plus efficace en faveur des "
       "certifications, labels et garanties : ils rétablissent le signal que "
       "le prix ne peut plus porter."),

# ---------------- c5-05 et c5-06 · défaillances de l’État, Pigou/Coase
f(id='q5-m11', sp='c5-05', niv='raisonner', type='qcm', b=912,
  q="Quel renversement l’école des choix publics opère-t-elle par rapport à "
    "Pigou ?",
  opts=["Elle admet les défaillances du marché, mais souligne qu’il existe "
        "aussi des défaillances de l’État, les responsables publics "
        "poursuivant eux aussi leur intérêt",
        "Elle nie l’existence des externalités",
        "Elle propose de nationaliser les secteurs défaillants",
        "Elle soutient que la taxe pigouvienne est toujours sous-évaluée"],
  ans=0,
  why=["Les défaillances de marché ne sont pas contestées : le point est "
       "ailleurs.",
       "C’est exactement la direction inverse de ce courant libéral.",
       "La critique ne porte pas sur le niveau de la taxe mais sur le "
       "présupposé d’un État désintéressé."],
  exp="L’argument tient en une phrase que le cours cite : « D’accord, il "
      "existe des défaillances du marché… mais il existe aussi des "
      "défaillances de l’État ». Le raisonnement applique aux décideurs "
      "publics l’hypothèse qu’on applique aux agents privés — « pourquoi les "
      "hommes politiques seraient-ils différents des agents "
      "économiques ? » — et en tire des conséquences concrètes : une "
      "politique environnementale soutenue au départ peut être abandonnée "
      "parce qu’elle coûte des voix.",
  diss="Mettre les deux défaillances en regard interdit la copie naïve qui "
       "corrige le marché par un État supposé parfait : il faut comparer "
       "deux imperfections."),

f(id='q5-m12', sp='c5-06', niv='appliquer', type='qcmm', b=1148,
  q="À quelles conditions, selon Coase, le marché peut-il résoudre lui-même "
    "une externalité ? (plusieurs réponses)",
  opts=["Des droits de propriété clairement définis",
        "Des droits échangeables entre les parties",
        "Des coûts de transaction faibles",
        "Un nombre très élevé de parties concernées",
        "Une taxe fixée par l’État au niveau du dommage"],
  ans=[0, 1, 2],
  why=["Exacte : sans droit clairement attribué, la négociation n’a pas "
       "d’objet.",
       "Exacte : il faut que le droit puisse être cédé contre compensation.",
       "Exacte : les coûts de transaction sont « les coûts liés au "
       "fonctionnement du marché » ; élevés, ils empêchent l’accord.",
       "Un grand nombre de parties fait au contraire exploser les coûts de "
       "transaction : c’est une limite du théorème, non une condition.",
       "La taxe est la solution de Pigou, que Coase présente comme une "
       "alternative à la sienne."],
  exp="Coase ne rejette pas l’État — le cours le précise —, il conteste que "
      "la taxe soit toujours la meilleure solution. Son théorème énonce que, "
      "sous trois conditions, les parties trouveront par la négociation une "
      "solution efficace, quel que soit le titulaire initial du droit. Mais "
      "ces conditions sont restrictives : attribuer des droits sur l’air ou "
      "l’océan est difficile, et la multiplication des parties rend "
      "l’accord coûteux. C’est pour cette attention aux règles et aux coûts "
      "de transaction que Coase est rangé parmi les néo-institutionnalistes.",
  diss="Opposer « taxe » et « négociation » comme deux manières "
       "d’internaliser une externalité donne une architecture claire à un "
       "sujet sur la régulation environnementale."),

f(id='q5-m13', sp='c5-06', niv='appliquer', type='qcm', b=774,
  q="Un marché de quotas d’émission est institué : les entreprises peu "
    "polluantes vendent leurs droits, les plus polluantes en achètent. Quelle "
    "logique ce dispositif met-il en œuvre ?",
  opts=["Une action par les quantités : on fixe un plafond puis on laisse le "
        "marché répartir l’effort, dans la logique de Coase",
        "Une action par les prix : l’État fixe le coût de la pollution, dans "
        "la logique de Pigou",
        "Une interdiction réglementaire pure",
        "Une subvention aux entreprises vertueuses"],
  ans=0,
  why=["Dans la logique de Pigou, c’est le prix qui est fixé par l’État et "
       "la quantité qui s’ajuste : ici, c’est l’inverse.",
       "Rien n’est interdit : les émissions sont permises dans la limite des "
       "droits détenus.",
       "Aucune somme n’est versée par l’État : les transferts ont lieu entre "
       "entreprises."],
  exp="Le cours oppose deux leviers. L’action par les prix — la taxe de "
      "Pigou — fixe le coût unitaire de la pollution et laisse la quantité "
      "s’ajuster. L’action par les quantités — les quotas, rattachés à "
      "Coase — fixe un plafond et laisse le prix du droit s’établir sur le "
      "marché. Le second mécanisme présente l’avantage de garantir le "
      "résultat environnemental, et conduit les entreprises dont la "
      "dépollution est peu coûteuse à la réaliser pour revendre leurs "
      "droits.",
  diss="Prix ou quantités : cette alternative est la question centrale de "
       "toute politique climatique, et se pose à l’identique pour les "
       "ressources halieutiques ou l’eau."),

# ------------------------------- c5-07 · Ostrom et les anti-communs
f(id='q5-m14', sp='c5-07', niv='raisonner', type='qcm', b=1261,
  q="Que démontre Elinor Ostrom contre la thèse de la tragédie des communs ?",
  opts=["Que de nombreuses communautés locales gèrent durablement des biens "
        "communs en créant leurs propres règles, sans passer ni par l’État ni "
        "par le marché",
        "Que les biens communs sont toujours surexploités",
        "Que seule la privatisation permet de préserver une ressource",
        "Que l’État doit systématiquement nationaliser les ressources "
        "communes"],
  ans=0,
  why=["C’est la thèse qu’elle réfute empiriquement.",
       "La privatisation est l’une des deux solutions classiques ; Ostrom "
       "montre précisément qu’il en existe une troisième.",
       "La nationalisation est l’autre solution classique, qu’elle ne "
       "retient pas davantage comme réponse unique."],
  exp="La thèse classique soutient que les biens communs sont fatalement "
      "surexploités, chacun poursuivant son intérêt individuel, d’où "
      "l’alternative : privatiser ou étatiser. Ostrom, première femme "
      "distinguée par le prix Nobel d’économie en 2009, montre "
      "empiriquement qu’« il existe une troisième voie : la gestion "
      "collective par des communautés locales » capables de créer leurs "
      "propres règles et de les faire respecter.",
  diss="Ostrom permet d’échapper à l’alternative marché / État, qui structure "
       "trop souvent les copies : la gouvernance collective est une "
       "troisième institution, pas un compromis entre les deux."),

f(id='q5-m15', sp='c5-07', niv='raisonner', type='vf', b=1198,
  q="Vrai ou faux : multiplier les droits de propriété sur une ressource "
    "garantit son usage efficace. Justifiez.",
  ans=False,
  exp="C’est exactement ce que conteste Michael Heller avec la tragédie des "
      "anti-communs (1998) : « trop de droits de propriété empêchent l’usage "
      "efficace d’une ressource ». Lorsque de multiples titulaires peuvent "
      "chacun bloquer l’utilisation d’un bien, les autorisations à réunir "
      "deviennent si nombreuses que la ressource reste sous-utilisée. C’est "
      "le miroir exact de la tragédie des communs : là, l’absence de droits "
      "conduisait à la surexploitation ; ici, leur prolifération conduit à "
      "la sous-exploitation.",
  diss="Le couple communs / anti-communs montre qu’il existe un niveau "
       "optimal de définition des droits de propriété, ce qui nuance "
       "fortement la solution coasienne."),

f(id='q5-m16', sp='c5-05', niv='appliquer', type='qcm', b=905,
  q="L’État impose un prix plafond contraignant sur un marché concurrentiel. "
    "Quel effet le cours décrit-il ?",
  opts=["Les quantités échangées deviennent sous-optimales et le surplus "
        "total diminue : une perte sèche apparaît",
        "Le surplus du consommateur et celui du producteur augmentent tous "
        "deux",
        "Le marché rejoint l’équilibre concurrentiel plus rapidement",
        "La demande devient parfaitement élastique"],
  ans=0,
  why=["Un transfert de surplus peut avoir lieu, mais la somme des deux "
       "surplus diminue : c’est la définition de la perte sèche.",
       "Un prix administré contraignant éloigne le marché de l’équilibre, il "
       "ne l’en rapproche pas.",
       "L’élasticité de la demande ne dépend pas du contrôle des prix."],
  exp="Un prix plafond contraignant se situe sous le prix d’équilibre : la "
      "quantité offerte diminue, la quantité demandée augmente, et les "
      "échanges se limitent à la plus petite des deux. Des transactions "
      "mutuellement avantageuses n’ont donc plus lieu : la somme des "
      "surplus diminue, et cette perte n’est récupérée par personne — c’est "
      "la perte sèche. Le cours place cette analyse parmi les défaillances "
      "de l’État, en regard des défaillances de marché.",
  diss="La perte sèche donne une mesure chiffrable au coût d’une "
       "intervention : elle permet de discuter un encadrement des prix sans "
       "s’en tenir aux intentions."),
]
