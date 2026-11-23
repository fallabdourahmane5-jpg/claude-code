# -*- coding: utf-8 -*-
"""Chapitre 10 — questions nouvelles, sous-parties c10-06 à c10-09."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c10-06
f(id='q10-n20', sp='c10-06', niv='connaitre', type='qcm', b=850,
  q="Quel sens le mot « apocalypse » prend-il dans le titre de l’ouvrage de "
    "Gérald Bronner, Apocalypse cognitive (2021) ?",
  opts=["Celui d’une catastrophe inévitable",
        "Celui d’une révélation : les nouveaux médias dévoilent certaines "
        "dispositions mentales profondes de l’être humain",
        "Celui d’une prophétie religieuse",
        "Celui d’une disparition annoncée du savoir scientifique"],
  ans=1,
  why=["Bronner ne prédit pas de catastrophe inéluctable : il propose "
       "d’ailleurs des solutions.",
       "Le mot a bien une origine religieuse, mais ce n’est pas le sens que "
       "Bronner mobilise.",
       "Le savoir scientifique ne disparaît pas : il est concurrencé dans "
       "l’espace de l’attention."],
  exp="Le mot possède un double sens, et Bronner utilise surtout l’idée de "
      "révélation : les médias numériques ne créent pas de toutes pièces nos "
      "travers, ils révèlent et exploitent des tendances mentales déjà "
      "présentes, en mettant en avant les contenus qui captent le plus "
      "facilement notre attention.",
  diss="C’est ce qui rend l’analyse redoutable : le problème n’est pas "
       "seulement la technique, c’est la rencontre entre une technique et des "
       "dispositions humaines stables."),

f(id='q10-n21', sp='c10-06', niv='connaitre', type='qcmm', b=865,
  q="Quels « invariants mentaux » Bronner identifie-t-il ? (plusieurs "
    "réponses)",
  opts=["L’attirance pour les contenus conflictuels, effrayants ou "
        "spectaculaires",
        "Le goût pour la visibilité sociale",
        "L’avarice cognitive",
        "La préférence pour les plaisirs à court terme",
        "Le goût spontané pour les raisonnements longs et complexes"],
  ans=[0, 1, 2, 3],
  why=["Exacte : ces contenus captent facilement l’attention et sont donc "
       "davantage regardés, partagés et commentés.",
       "Exacte : la notoriété numérique peut être perçue comme une forme de "
       "reconnaissance ou de légitimité sociale.",
       "Exacte : les individus économisent leurs efforts intellectuels.",
       "Exacte : les satisfactions immédiates sont privilégiées sur les "
       "contenus plus exigeants.",
       "C’est l’inverse de l’avarice cognitive : les individus n’aiment pas "
       "consacrer beaucoup d’énergie aux problèmes complexes."],
  exp="Les invariants mentaux sont des tendances relativement stables du "
      "fonctionnement mental humain, repérées par la psychologie cognitive. "
      "Elles influencent ce qui attire notre attention, les informations que "
      "nous choisissons et la manière dont nous raisonnons. Elles ne "
      "poseraient pas nécessairement problème si les médias étaient "
      "indifférents à notre attention — mais leur modèle économique les pousse "
      "précisément à les exploiter."),

f(id='q10-n22', sp='c10-06', niv='comprendre', type='qcm', b=950,
  q="Pourquoi le modèle économique des médias les conduit-il à exploiter nos "
    "invariants mentaux ?",
  opts=["Parce que la loi les oblige à diffuser des contenus populaires",
        "Parce que leur financement dépend largement des recettes "
        "publicitaires, donc de l’audience : ils ont intérêt à proposer des "
        "contenus capables de capter l’attention",
        "Parce que les journalistes ignorent les travaux des sciences "
        "cognitives",
        "Parce que les contenus rigoureux coûtent plus cher à produire que "
        "les fausses informations"],
  ans=1,
  why=["Aucune obligation légale de ce type n’existe.",
       "Le cours n’explique pas le phénomène par l’ignorance des "
       "journalistes mais par une contrainte économique.",
       "Le coût de production n’est pas l’argument retenu ici : c’est la "
       "course à l’audience."],
  exp="De nombreux médias fonctionnent grâce aux recettes publicitaires ; "
      "pour les obtenir, ils ont besoin d’audience. Ils ont donc intérêt à "
      "proposer des contenus qui retiennent l’attention, c’est-à-dire des "
      "contenus correspondant aux invariants mentaux décrits par Bronner. Sur "
      "les plateformes, le mécanisme est renforcé par les algorithmes.",
  diss="Articulation efficace : une offre guidée par l’audience rencontre une "
       "demande guidée par des biais — c’est bien un marché, mais un marché "
       "cognitif dérégulé."),

f(id='q10-n23', sp='c10-06', niv='comprendre', type='qcm', b=965,
  q="Comment les algorithmes renforcent-ils les préférences des internautes ?",
  opts=["En supprimant les contenus faux",
        "En observant ce que l’utilisateur regarde et ce à quoi il réagit, "
        "puis en lui proposant davantage de contenus similaires : ses "
        "préférences initiales sont renforcées au lieu d’être remises en "
        "question",
        "En hiérarchisant les informations selon leur fiabilité scientifique",
        "En imposant à chacun une sélection aléatoire de contenus"],
  ans=1,
  why=["Les algorithmes ne trient pas par véracité : c’est tout le problème.",
       "La fiabilité scientifique n’est pas le critère de la "
       "recommandation.",
       "La sélection n’est pas aléatoire : elle est au contraire très "
       "personnalisée."],
  exp="Les algorithmes observent les comportements et proposent des contenus "
      "proches de ceux auxquels l’individu a déjà réagi. Ses préférences "
      "initiales se trouvent donc confortées, ce qui peut l’enfermer "
      "progressivement dans un univers informationnel limité. Ce mécanisme "
      "nourrit l’insularité cognitive et les chambres d’écho.",
  diss="À relier à l’éditorialisation du monde : les médias ne montrent jamais "
       "l’intégralité du réel, ils sélectionnent et hiérarchisent — mais ici "
       "la sélection est automatisée et individualisée."),

f(id='q10-n24', sp='c10-06', niv='connaitre', type='qcm', b=979,
  q="Qu’appelle-t-on « éditorialisation du monde » ?",
  opts=["La transformation des lecteurs en producteurs de contenus",
        "Le fait de focaliser l’attention sur certains éléments plutôt que "
        "sur d’autres et de hiérarchiser les informations disponibles",
        "La publication d’éditoriaux politiques dans la presse",
        "La disparition progressive des médias traditionnels"],
  ans=1,
  why=["La production de contenus par les internautes est un autre "
       "phénomène, lié à la recherche de visibilité sociale.",
       "Il ne s’agit pas du genre journalistique de l’éditorial, malgré la "
       "proximité des mots.",
       "Le cours ne prédit pas la disparition des médias traditionnels, qu’il "
       "soumet au contraire aux mêmes logiques d’audience."],
  exp="Les médias ne montrent jamais l’intégralité du réel : ils doivent "
      "sélectionner certains événements, en mettre certains en avant, en "
      "laisser d’autres de côté et hiérarchiser les informations. Cette "
      "sélection est inévitable ; elle devient problématique lorsque "
      "l’individu ne reçoit plus qu’un type particulier d’informations."),

# ------------------------------------------------------------- c10-07
f(id='q10-n25', sp='c10-07', niv='comprendre', type='qcm', b=1041,
  q="Qu’est-ce que l’effet de réitération ?",
  opts=["La tendance à oublier une information qui n’est pas répétée",
        "La tendance à juger une information plus crédible simplement parce "
        "qu’elle a été répétée plusieurs fois : la familiarité est confondue "
        "avec la vérité",
        "Le fait qu’une information démentie disparaisse des esprits",
        "La multiplication automatique des contenus par les algorithmes"],
  ans=1,
  why=["Le mécanisme porte sur la crédibilité accordée, non sur l’oubli.",
       "C’est l’inverse de la persistance des premières informations : un "
       "démenti n’efface pas complètement la trace initiale.",
       "La duplication algorithmique est un support du phénomène, pas sa "
       "définition psychologique."],
  exp="Plus un individu voit une information répétée, plus il peut avoir "
      "tendance à la considérer comme vraie : la familiarité avec une "
      "information est confondue avec sa véracité. Combiné à la persistance "
      "des premières informations et à la plus grande viralité des contenus "
      "faux — environ six fois plus rapides que les vrais selon les éléments "
      "retenus par Bronner —, ce mécanisme explique la force de la "
      "désinformation."),

f(id='q10-n26', sp='c10-07', niv='connaitre', type='qcm', b=1063,
  q="Que désigne l’expression « démocratie des crédules » employée par "
    "Bronner ?",
  opts=["Un régime politique où le peuple ne vote plus",
        "Une situation dans laquelle la multiplication des sources "
        "d’information ne garantit pas que les informations les plus vraies "
        "soient les plus visibles, ce qui entraîne une forme de « déchéance "
        "de rationalité »",
        "Une démocratie où les experts décident à la place des citoyens",
        "Le refus de toute information officielle"],
  ans=1,
  why=["Il ne s’agit pas d’une transformation des institutions "
       "électorales.",
       "L’expertise n’est pas en cause : Bronner invite au contraire à ne pas "
       "confondre savoirs et opinions.",
       "Le complotisme est un symptôme possible, pas la définition du "
       "concept."],
  exp="C’est le titre d’un ouvrage de Bronner publié en 2013. La "
      "démocratisation de l’accès à l’information ne garantit pas que les "
      "informations les plus fiables soient les plus visibles : les contenus "
      "attractifs et conformes aux croyances existantes peuvent prendre une "
      "place importante. Bronner parle alors de « déchéance de rationalité », "
      "expression qu’il emploie dans un ouvrage de 2019.",
  diss="Contraste direct avec Weber : là où la diffusion des savoirs devait "
       "produire le désenchantement du monde, l’abondance d’informations peut "
       "favoriser les croyances."),

f(id='q10-n27', sp='c10-07', niv='comprendre', type='qcmm', b=1087,
  q="Quelles solutions Bronner propose-t-il pour limiter ces dérives ? "
    "(plusieurs réponses)",
  opts=["Ne pas confondre savoirs établis, croyances et simples opinions, qui "
        "ne disposent pas du même niveau de preuve",
        "Accepter la complexité et l’incertitude, y compris l’absence de "
        "réponse simple",
        "Faire preuve d’esprit critique en examinant sources, preuves et "
        "cohérence d’une information",
        "Croiser des informations issues de sources indépendantes et sortir "
        "volontairement de l’effet tunnel et du biais de confirmation",
        "Se limiter aux sources confirmant ce que l’on sait déjà, pour éviter "
        "la confusion"],
  ans=[0, 1, 2, 3],
  why=["Exacte : toutes les affirmations ne disposent pas du même niveau de "
       "preuve.",
       "Exacte : Bronner insiste sur la nécessité d’accepter l’incertitude.",
       "Exacte : il s’agit de ne pas accepter spontanément une information.",
       "Exacte : il faut vérifier l’indépendance des sources et chercher "
       "délibérément des arguments contradictoires.",
       "C’est exactement le biais de confirmation qu’il s’agit de combattre, "
       "et le moyen de s’enfermer dans une chambre d’écho."],
  exp="L’image de la sphère résume l’état d’esprit recommandé : plus nos "
      "connaissances augmentent, plus la surface en contact avec l’inconnu "
      "augmente — plus on sait de choses, plus on prend conscience de ce que "
      "l’on ignore. L’augmentation des connaissances ne supprime donc pas "
      "l’incertitude : elle la rend plus visible."),

f(id='q10-n28', sp='c10-07', niv='raisonner', type='courte', b=1143,
  q="Comment articuler l’analyse de Weber et celle de Bronner sur le lien "
    "entre savoirs et rationalité ?",
  ans={'modele': "Pour Weber, la science et la rationalisation produisent le "
       "désenchantement du monde : les savoirs scientifiques remplacent "
       "progressivement les croyances et les explications magiques, de sorte "
       "que la diffusion des savoirs accroît la rationalité. On pourrait "
       "donc attendre d’Internet, qui permet une diffusion massive des "
       "savoirs, qu’il accentue ce mouvement. Bronner montre que ce n’est pas "
       "nécessairement le cas : les humains ont des biais cognitifs, "
       "recherchent des contenus simples et attractifs, les médias "
       "recherchent l’audience, les algorithmes renforcent certaines "
       "préférences et les fausses informations circulent facilement. Dans un "
       "marché cognitif dérégulé, plus d’informations disponibles n’équivaut "
       "donc pas automatiquement à plus de rationalité : l’abondance peut "
       "même favoriser les croyances, jusqu’à une « démocratie des crédules ».",
       'cles': [{'f': ['desenchantement', 'weber', 'magique'],
                 'l': 'Weber : la science produit le désenchantement du monde'},
                {'f': ['internet', 'diffusion', 'massive', 'acces'],
                 'l': 'Internet diffuse massivement les savoirs'},
                {'f': ['biais', 'audience', 'algorithme', 'fausse'],
                 'l': 'mais biais cognitifs, audience, algorithmes et fausses informations'},
                {'f': ['pas automatiquement', 'ne garantit pas', 'credule', 'derege'],
                 'l': 'donc plus d’informations ≠ plus de rationalité'}]},
  exp="Le cours construit explicitement ce rapprochement comme une tension : "
      "l’un et l’autre lient savoirs et rationalité, mais Weber dans un "
      "mouvement d’ensemble historique, Bronner en observant le marché "
      "concret de l’attention."),

f(id='q10-n29', sp='c10-07', niv='comprendre', type='vf', b=1020,
  q="Lorsqu’une fausse information est démentie, le démenti efface "
    "généralement son effet sur les représentations individuelles.",
  ans=False,
  exp="Le cours soutient l’inverse : une information reçue en premier peut "
      "continuer à influencer l’individu même lorsqu’elle est ensuite "
      "démentie. Le démenti n’efface pas complètement l’information "
      "initiale, qui laisse une trace durable dans les représentations. C’est "
      "l’un des mécanismes expliquant la circulation des fausses "
      "informations, avec leur viralité supérieure, l’effet de réitération et "
      "la loi de Brandolini.",
  diss="Conséquence pratique : le fact-checking arrive toujours après, et son "
       "coût est bien supérieur à celui de la fausse information — c’est "
       "exactement la loi de Brandolini."),

# ------------------------------------------------------------- c10-08
f(id='q10-n30', sp='c10-08', niv='connaitre', type='qcm', b=1213,
  q="Dans quel ouvrage Christian Morel développe-t-il son analyse, et sur "
    "quels cas s’appuie-t-il ?",
  opts=["Le Phénomène bureaucratique, à partir d’une enquête dans une "
        "entreprise publique",
        "Les Décisions absurdes, trois volumes publiés entre 2002 et 2018, à "
        "partir d’accidents aéronautiques, d’accidents de sous-marins "
        "nucléaires, d’erreurs en bloc opératoire et d’accidents en haute "
        "montagne",
        "Apocalypse cognitive, à partir de l’analyse des médias numériques",
        "The Human Problems of an Industrial Civilization, à partir "
        "d’expériences en usine"],
  ans=1,
  why=["Le Phénomène bureaucratique (1963) est l’ouvrage de Crozier sur la "
       "SEITA.",
       "Apocalypse cognitive (2021) est l’ouvrage de Bronner.",
       "The Human Problems of an Industrial Civilization (1933) est celui de "
       "Mayo."],
  exp="Le paradoxe que Morel étudie est précis : ces accidents se produisent "
      "alors même que les organisations concernées disposent de spécialistes, "
      "possèdent des procédures, mettent en place des règles de sécurité et "
      "sont censées fonctionner rationnellement. Son analyse porte donc sur la "
      "dimension collective de la décision."),

f(id='q10-n31', sp='c10-08', niv='appliquer', type='qcm', b=1246,
  q="Avant le lancement de Challenger, une téléconférence réunit 34 personnes "
    "sur trois sites. Qu’en retient Morel ?",
  opts=["Que la décision a été prise par une seule personne",
        "Qu’aucune objection suffisamment forte n’a conduit à l’annulation du "
        "lancement, alors que certains ingénieurs de Thiokol avaient identifié "
        "le risque lié au froid",
        "Que les ingénieurs n’avaient pas identifié le problème des joints",
        "Que la NASA avait interdit toute discussion technique"],
  ans=1,
  why=["Le propos de Morel est justement que la décision est collective, et "
       "non imputable à un individu.",
       "Les ingénieurs avaient bien identifié le risque : c’est ce qui rend "
       "la décision si frappante.",
       "La réunion a précisément eu lieu pour discuter du lancement."],
  exp="La température en Floride était beaucoup plus basse que d’habitude ; "
      "certains ingénieurs de Thiokol, l’entreprise ayant fabriqué les joints, "
      "estimaient le lancement dangereux. Mais le dirigeant de Thiokol comme "
      "la NASA étaient favorables au lancement, et les joints n’étaient plus "
      "considérés comme une pièce déterminante. Le problème technique existait, "
      "mais l’organisation collective n’a pas su lui donner suffisamment de "
      "poids.",
  diss="Formulation à retenir : l’accident ne révèle pas seulement une "
       "défaillance technique, mais l’incapacité collective à faire remonter "
       "une objection."),

f(id='q10-n32', sp='c10-08', niv='comprendre', type='assoc', b=1289,
  q="Associez chaque comportement individuel décrit par Morel à son "
    "mécanisme.",
  ans=[["Un individu repère un problème mais hésite à contredire son supérieur par crainte de conséquences professionnelles", "La crainte de contester l’autorité"],
       ["Un individu exprime une réserve, constate qu’elle n’est pas retenue et renonce à la formuler de nouveau", "La crainte d’insister"],
       ["Un individu se dit « ce n’est pas mon domaine, les autres savent mieux que moi »", "L’autocensure liée au sentiment d’incompétence"],
       ["La division du travail fragmente les compétences et personne ne prend de vision globale", "L’autocensure liée au sentiment d’incompétence"]],
  exp="Ces trois comportements ont un effet commun redoutable : une "
      "information importante peut être connue dans l’organisation sans peser "
      "réellement dans la décision. Le troisième mécanisme est le plus "
      "proprement organisationnel : c’est la spécialisation issue de la "
      "division du travail qui produit l’autocensure.",
  diss="Lien direct avec Weber : la division du travail et la hiérarchie, "
       "présentées comme des facteurs de rationalité, produisent ici des "
       "effets pervers."),

f(id='q10-n33', sp='c10-08', niv='comprendre', type='qcm', b=1373,
  q="Qu’appelle-t-on « illusion de l’unanimité » dans la pensée de groupe ?",
  opts=["Le fait que tous les membres du groupe soient réellement d’accord",
        "Le fait que chaque membre ait des doutes mais, comme personne ne les "
        "exprime, croie que tous les autres sont d’accord — ce qui renforce la "
        "mauvaise décision",
        "Le fait que le groupe vote toujours à l’unanimité",
        "Le fait qu’un leader impose son point de vue à tous"],
  ans=1,
  why=["Il s’agit précisément d’une illusion : l’accord n’est qu’apparent.",
       "Aucune procédure de vote n’est en cause : le mécanisme est "
       "informel.",
       "L’imposition par un leader relève de la pression hiérarchique, autre "
       "mécanisme du chapitre."],
  exp="Dans un groupe, les individus cherchent souvent l’harmonie : ils "
      "évitent d’exprimer leurs désaccords, de créer un conflit ou de "
      "contester la position majoritaire. Chacun se dit alors « je ne suis pas "
      "totalement convaincu, mais puisque personne ne dit rien, les autres "
      "doivent être d’accord ». Le groupe se croit unanime et la mauvaise "
      "décision s’en trouve renforcée.",
  diss="C’est la raison pour laquelle Morel propose d’attribuer "
       "explicitement à quelqu’un le rôle d’avocat du diable : il faut "
       "fabriquer le désaccord."),

f(id='q10-n34', sp='c10-08', niv='raisonner', type='qcm', b=1556,
  q="Les groupes sont-ils plus rationnels que les individus, selon Morel ?",
  opts=["Oui, toujours : plusieurs personnes disposent de plus d’informations "
        "et corrigent mutuellement leurs erreurs",
        "Pas nécessairement : le groupe apporte des informations et des "
        "compétences, mais peut aussi produire conformisme, autocensure, biais "
        "de confirmation, illusion d’unanimité et pression hiérarchique",
        "Non, jamais : la décision individuelle est toujours supérieure",
        "La question ne se pose pas, car les décisions sont toujours "
        "individuelles"],
  ans=1,
  why=["Ces avantages existent mais ne sont pas automatiques : c’est tout "
       "l’objet de la démonstration.",
       "Morel ne soutient pas la supériorité de la décision individuelle : il "
       "propose d’organiser le collectif.",
       "Le chapitre montre au contraire que les décisions sont des œuvres "
       "collectives."],
  exp="La réponse de Morel est nuancée : un collectif n’est pas "
      "automatiquement plus rationnel qu’un individu, et la qualité de la "
      "décision dépend de la manière dont le groupe est organisé. C’est "
      "précisément ce qui justifie les métarègles : sans organisation du débat "
      "et de la contradiction, les mécanismes collectifs amplifient les "
      "erreurs individuelles.",
  diss="Conclusion utile : la rationalité n’est pas une propriété des "
       "individus ou des groupes, c’est un résultat d’organisation."),

# ------------------------------------------------------------- c10-09
f(id='q10-n35', sp='c10-09', niv='raisonner', type='assoc', b=1416,
  q="Associez chaque caractéristique de la bureaucratie wébérienne à l’effet "
    "pervers que Morel y repère.",
  ans=[["La division du travail permet la spécialisation", "Mais elle peut empêcher chacun de comprendre l’ensemble du problème"],
       ["La hiérarchie permet d’organiser l’autorité", "Mais elle peut empêcher les subordonnés de contester une mauvaise décision"],
       ["Les procédures cherchent à sécuriser l’action", "Mais elles ne suffisent pas toujours à empêcher les erreurs"],
       ["Les règles visent à réduire l’arbitraire et à accroître l’efficacité", "Mais les mêmes mécanismes peuvent favoriser l’autocensure et les décisions absurdes"]],
  exp="La phrase comparative du cours résume l’articulation : alors que Weber "
      "montre que la bureaucratie rationalise l’organisation grâce à la "
      "spécialisation, à la hiérarchie et aux procédures, Morel souligne que "
      "ces mêmes mécanismes peuvent produire des effets pervers. Morel ne "
      "considère pourtant pas ces dysfonctionnements comme inévitables : d’où "
      "les métarègles.",
  diss="Structure de dissertation possible : les mêmes dispositifs qui "
       "produisent la rationalité produisent, poussés à bout, son contraire."),

f(id='q10-n36', sp='c10-09', niv='comprendre', type='qcm', b=1459,
  q="En quoi consiste le rôle de l’« avocat du diable » dans le débat "
    "contradictoire ?",
  opts=["Défendre systématiquement la position de la direction",
        "Être explicitement chargé de contester la décision : chercher ses "
        "faiblesses, proposer des contre-arguments, imaginer ce qui pourrait "
        "mal se passer, même si tout le monde semble d’accord",
        "Arbitrer entre les points de vue exprimés",
        "Représenter les salariés dans la discussion"],
  ans=1,
  why=["Défendre la direction serait l’inverse de sa fonction.",
       "Il ne tranche pas : il conteste, l’arbitrage vient ensuite avec la "
       "recherche d’un consensus.",
       "Ce n’est pas un rôle de représentation syndicale mais une méthode de "
       "décision."],
  exp="Morel considère qu’une bonne décision doit être confrontée à des "
      "objections et à la confrontation des arguments. Attribuer "
      "explicitement à une personne le rôle de contester permet de lutter "
      "contre le conformisme, l’illusion d’unanimité et la pensée de groupe : "
      "le désaccord n’est plus un acte de courage individuel, il devient une "
      "fonction organisée.",
  diss="Détail décisif : la contradiction est institutionnalisée, donc "
       "détachée du risque personnel — c’est ce qui manquait avant "
       "Challenger."),

f(id='q10-n37', sp='c10-09', niv='comprendre', type='qcm', b=1497,
  q="Pourquoi Morel recommande-t-il de ne pas punir systématiquement les "
    "erreurs ?",
  opts=["Parce que les erreurs sont sans conséquence dans les grandes "
        "organisations",
        "Parce que si les erreurs sont systématiquement punies, les individus "
        "sont tentés de les cacher et l’organisation perd une information "
        "précieuse pour son retour d’expérience",
        "Parce que la sanction relève du droit du travail et non de "
        "l’organisation",
        "Parce que les erreurs sont toujours imputables à la hiérarchie"],
  ans=1,
  why=["Le chapitre porte précisément sur des erreurs aux conséquences "
       "dramatiques.",
       "La question n’est pas juridique mais organisationnelle : il s’agit de "
       "la qualité de l’information disponible.",
       "Morel refuse justement de chercher un responsable unique, à quelque "
       "niveau que ce soit."],
  exp="Lorsqu’une erreur se produit, l’organisation doit chercher à "
      "comprendre comment elle s’est produite, quels mécanismes l’ont "
      "favorisée et comment éviter qu’elle se répète : c’est le retour "
      "d’expérience. La punition systématique produit l’effet inverse, en "
      "incitant à la dissimulation.",
  diss="Métarègle particulièrement contre-intuitive, donc très citable : la "
       "sécurité suppose de renoncer à sanctionner."),

f(id='q10-n38', sp='c10-09', niv='comprendre', type='qcm', b=1533,
  q="Comment le cours articule-t-il Kahneman et Morel ?",
  opts=["Kahneman étudie les organisations, Morel les individus",
        "Kahneman montre que les individus utilisent des raisonnements rapides "
        "et intuitifs et sont donc soumis à des biais cognitifs ; Morel "
        "analyse comment ces biais se combinent aux mécanismes hiérarchiques "
        "et collectifs pour produire des décisions absurdes",
        "Kahneman et Morel aboutissent à des conclusions opposées",
        "Morel réfute l’existence des biais cognitifs"],
  ans=1,
  why=["C’est l’inverse : Kahneman part de l’individu, Morel ajoute "
       "l’organisation.",
       "Leurs analyses sont complémentaires et non opposées.",
       "Morel part au contraire des biais pour y ajouter une dimension "
       "collective."],
  exp="L’apport propre de Morel est cette dimension supplémentaire : il ne se "
      "contente pas de constater les biais individuels, il étudie comment ils "
      "se combinent avec la hiérarchie et la dynamique de groupe. Le cours le "
      "résume dans un triptyque : Weber montre la volonté de rationalisation "
      "des organisations, Bronner souligne les limites cognitives des "
      "individus, Morel révèle que leur mise en groupe au sein d’une "
      "hiérarchie peut amplifier ces limites."),

f(id='q10-n39', sp='c10-09', niv='appliquer', type='qcm', b=1512,
  q="Dans quels domaines les check-lists sont-elles utilisées, et avec quel "
    "résultat chiffré cité par le cours ?",
  opts=["Dans l’industrie automobile, avec une hausse de 20 % de la "
        "productivité",
        "Dans l’aéronautique depuis longtemps, puis dans les blocs "
        "opératoires, où leur utilisation a permis de réduire la mortalité de "
        "50 % dans certains cas",
        "Dans les administrations publiques, avec une réduction de moitié des "
        "délais",
        "Dans les écoles, avec une amélioration des résultats scolaires"],
  ans=1,
  why=["La hausse de 20 % concerne la productivité dans la Test Room de "
       "Mayo.",
       "Les délais administratifs ne sont pas évoqués par le cours.",
       "Aucun exemple scolaire n’est mentionné."],
  exp="Les check-lists sécurisent les procédures complexes : même un "
      "professionnel expérimenté peut oublier une étape, et elles permettent "
      "de vérifier systématiquement que toutes les opérations nécessaires ont "
      "été réalisées. Utilisées de longue date dans l’aéronautique, elles ont "
      "été introduites dans les blocs opératoires, avec une réduction de la "
      "mortalité de 50 % dans certains d’entre eux.",
  diss="Chiffre très efficace en dissertation : une métarègle simple produit "
       "un gain de sécurité considérable, sans moyens supplémentaires."),

]
