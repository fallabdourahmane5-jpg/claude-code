# -*- coding: utf-8 -*-
"""Définitions rédigées pour le chapitre 5 de deuxième année — second volet :
marché de la monnaie, politiques conjoncturelles et économie ouverte.

Chaque entrée est rédigée à partir du passage du cours désigné par `anc`
(l'intitulé de la section) et n'ajoute rien qui ne s'y trouve. Aucune
attribution d'auteur n'est faite au-delà de ce que le chapitre établit.
"""

# (terme, chapitres, intitulé d'ancrage, définition, alias, distinction)
DEFS = [

 # ---------------------------------------------- le marché de la monnaie
 ("Préférence pour la liquidité", ['25'],
  "Keynes considère la monnaie comme un actif recherché pour sa liquidité",
  "La préférence pour la liquidité désigne, chez Keynes, le désir de "
  "conserver de la monnaie pour elle-même plutôt que de détenir des titres. "
  "Dans la Théorie générale (1936), Keynes rompt ainsi avec la conception "
  "classique selon laquelle la monnaie ne serait qu’un instrument de "
  "transaction : elle devient un actif, recherché pour sa liquidité, "
  "c’est-à-dire pour la facilité avec laquelle elle peut servir de moyen de "
  "paiement sans délai ni perte de valeur. Il en découle une conséquence "
  "majeure : le taux d’intérêt ne se détermine plus par la confrontation de "
  "l’épargne et du financement, mais sur le marché monétaire, comme prix du "
  "renoncement à la liquidité.",
  ["preference pour la liquidite keynesienne"],
  "Chez les classiques, le taux d’intérêt arbitre entre consommer et "
  "épargner ; chez Keynes, il arbitre entre détenir de la monnaie et "
  "détenir des titres."),

 ("Motif de transaction", ['25'],
  "Le motif de transaction : financer les échanges courants",
  "Le motif de transaction correspond à la monnaie conservée pour régler les "
  "dépenses habituelles : achats courants, versement des salaires, achat de "
  "matières premières. Cette demande de monnaie dépend positivement du "
  "revenu national, car une économie qui produit et échange davantage "
  "réalise davantage de transactions et a donc besoin de davantage de "
  "moyens de paiement. C’est le premier des trois motifs de détention de la "
  "monnaie et, avec le motif de précaution, l’une des deux composantes "
  "notées L1, qui dépendent du revenu.",
  ["demande de monnaie pour transaction", "l1"],
  "Les motifs de transaction et de précaution dépendent du revenu ; le "
  "motif de spéculation dépend du taux d’intérêt."),

 ("Motif de spéculation", ['25'],
  "Le motif de spéculation : arbitrer entre monnaie et titres financiers",
  "Le motif de spéculation correspond à la monnaie conservée en fonction des "
  "anticipations sur l’évolution future des taux d’intérêt et du prix des "
  "titres. Une fois l’épargne constituée, les agents doivent choisir "
  "comment la détenir : en monnaie liquide ou en obligations. Comme le prix "
  "des obligations varie en sens inverse du taux d’intérêt, un taux jugé "
  "anormalement élevé fait anticiper sa baisse, donc une hausse du cours des "
  "titres, et les agents achètent des obligations ; un taux jugé très faible "
  "fait anticiper sa remontée, donc une perte en capital, et les agents "
  "conservent de la monnaie. La demande spéculative dépend donc négativement "
  "du taux d’intérêt.",
  ["demande speculative de monnaie", "l2", "motif de speculation keynesien"],
  "Ce motif ne porte pas sur le niveau de l’épargne, déterminé par le revenu, "
  "mais sur la forme sous laquelle elle est détenue."),

 ("Cours d’une obligation", ['25', '2'],
  "Le prix des obligations évolue en sens inverse des taux d’intérêt",
  "Le cours d’une obligation est son prix sur le marché secondaire, qui "
  "varie en sens inverse du taux d’intérêt. Le mécanisme, parfois appelé "
  "« effet balançoire », tient au caractère fixe du coupon : si les "
  "nouvelles obligations émises offrent un rendement supérieur, une ancienne "
  "obligation ne trouve preneur qu’à un prix plus faible, baisse qui relève "
  "d’autant son rendement pour l’acheteur ; inversement, une baisse des taux "
  "rend les anciens titres plus attractifs et fait monter leur prix. Il faut "
  "donc distinguer le coupon, qui reste fixe, le prix de marché, qui varie, "
  "et le rendement de marché, qui évolue avec ce prix.",
  ["prix des obligations", "effet balancoire", "cours des obligations"],
  "C’est cette relation inverse qui permet d’anticiper des gains ou des "
  "pertes en capital, et donc qui fonde le motif de spéculation."),

 ("Coupon", ['25'],
  "Le prix des obligations évolue en sens inverse des taux d’intérêt",
  "Le coupon est le versement d’intérêt auquel donne droit une obligation. "
  "Fixé à l’émission, il demeure inchangé pendant la durée du titre : c’est "
  "précisément parce qu’il est fixe que le prix de marché de l’obligation "
  "doit s’ajuster lorsque les taux d’intérêt varient. Une obligation "
  "rapportant 5 € par an conserve ce coupon quel que soit le cours auquel "
  "elle s’échange ; seul son rendement pour un nouvel acheteur change.",
  ["coupon obligataire"],
  "Le coupon est un flux fixe, le rendement un rapport entre ce flux et le "
  "prix payé : les deux ne varient pas ensemble."),

 ("Offre de monnaie", ['25', '2'],
  "L’offre de monnaie est supposée exogène",
  "L’offre de monnaie est la quantité de monnaie mise en circulation. Dans "
  "le modèle IS-LM traditionnel, elle est supposée exogène, c’est-à-dire "
  "fixée par les autorités monétaires en dehors des mécanismes étudiés : "
  "elle est alors représentée par une droite verticale sur le marché "
  "monétaire, puisque la quantité offerte ne dépend pas du taux d’intérêt. "
  "Le cours présente cette hypothèse comme une simplification : les systèmes "
  "monétaires contemporains reposent aussi sur la création monétaire "
  "bancaire et sur le pilotage des taux directeurs.",
  ["offre de monnaie exogene", "masse monetaire offerte"],
  "Exogène ne signifie pas constante : l’offre peut être modifiée par la "
  "banque centrale, ce qui déplace la courbe LM."),

 ("Variable exogène", ['25'],
  "L’offre de monnaie est supposée exogène",
  "Une variable exogène est une variable dont la valeur est déterminée en "
  "dehors des mécanismes étudiés par le modèle : elle est une donnée, non un "
  "résultat. Dans le modèle IS-LM, l’offre de monnaie et les dépenses "
  "publiques sont exogènes, tandis que le revenu national et le taux "
  "d’intérêt sont endogènes, c’est-à-dire déterminés par le modèle "
  "lui-même. Le partage entre exogène et endogène est un choix de "
  "construction : c’est lui qui fixe ce que le modèle explique et ce qu’il "
  "suppose donné.",
  ["exogene", "variable endogene", "endogene"],
  "Rendre une variable endogène, c’est accepter de l’expliquer : c’est ce "
  "que fait la croissance endogène pour le progrès technique."),

 ("Zone classique", ['25'],
  "La phase verticale : la zone classique",
  "La zone classique est la portion verticale de la courbe LM, atteinte "
  "lorsque le taux d’intérêt est très élevé. La demande spéculative de "
  "monnaie y devient nulle ou négligeable — les agents préfèrent détenir des "
  "titres — de sorte que la demande de monnaie ne dépend plus que des "
  "besoins de transaction et de précaution, donc du revenu. À offre de "
  "monnaie donnée, le revenu compatible avec l’équilibre monétaire est alors "
  "fixé : une relance budgétaire ne peut plus augmenter la production, "
  "tandis que la politique monétaire devient particulièrement efficace.",
  ["phase verticale de lm", "zone dite classique"],
  "Symétrique de la trappe à liquidité : là, LM est horizontale et c’est la "
  "politique budgétaire qui est efficace."),

 # ------------------------------------- politiques et modèle OG-DG
 ("Politique conjoncturelle", ['25', '1'],
  "Les politiques conjoncturelles et structurelles n’ont pas le même objectif",
  "Une politique conjoncturelle cherche à influencer l’activité à court "
  "terme, en agissant principalement sur la demande globale : relance "
  "budgétaire, baisse des taux d’intérêt, soutien temporaire au revenu. Elle "
  "vise à amortir les fluctuations du cycle plutôt qu’à transformer les "
  "capacités de production. Lorsque l’économie est déjà contrainte par son "
  "niveau de production potentiel, son efficacité devient limitée : ce sont "
  "alors les politiques structurelles qui prennent le relais.",
  ["politiques conjoncturelles"],
  "Conjoncturel : agir sur la demande à court terme. Structurel : modifier "
  "durablement l’offre et les capacités productives."),

 ("Politique structurelle", ['25'],
  "Les critiques des politiques conjoncturelles conduisent à privilégier les politiques structurelles",
  "Une politique structurelle cherche à modifier durablement le "
  "fonctionnement de l’économie, en agissant sur l’offre et les capacités de "
  "production : amélioration du fonctionnement des marchés, investissement "
  "dans le capital productif, formation. Son raisonnement est le suivant : "
  "si la production est limitée par des contraintes structurelles, il faut "
  "modifier ces contraintes plutôt que stimuler une demande qui butera sur "
  "elles. L’objectif devient d’augmenter la production potentielle, "
  "c’est-à-dire ce que l’économie est capable de produire durablement.",
  ["politiques structurelles"],
  "Les deux types de politique ne s’opposent pas terme à terme : Barro "
  "critique la relance conjoncturelle tout en reconnaissant un rôle de "
  "l’État dans la croissance de long terme."),

 ("Production potentielle", ['25'],
  "L’objectif devient d’augmenter la production potentielle",
  "La production potentielle est le niveau de production que l’économie peut "
  "soutenir durablement compte tenu de ses capacités : main-d’œuvre "
  "disponible, stock de capital, technologie. Elle sert de référence pour "
  "juger de la position conjoncturelle : l’écart entre la production "
  "effective et la production potentielle est l’écart de production. "
  "Lorsque l’économie atteint ce niveau, une politique de demande ne peut "
  "plus durablement accroître l’activité et se traduit principalement par "
  "des tensions sur les prix.",
  ["pib potentiel", "niveau de production potentiel"],
  "Potentielle ne veut pas dire maximale : c’est le niveau soutenable sans "
  "tensions inflationnistes, et non la capacité physique absolue."),

 ("Croissance potentielle", ['25', '6'],
  "Le retour des politiques d’offre et de la réflexion sur la croissance potentielle",
  "La croissance potentielle est le rythme de progression de la production "
  "potentielle, c’est-à-dire la croissance que l’économie peut soutenir "
  "durablement. La stagflation des années 1970 déplace une partie de "
  "l’analyse vers ses déterminants : accumulation du capital, progrès "
  "technique, formation du capital humain. L’objectif de la politique "
  "économique ne se limite plus à corriger les fluctuations, il consiste "
  "aussi à relever cette trajectoire de long terme — réflexion qui rejoint "
  "les théories de la croissance endogène.",
  ["croissance potentielle de long terme"],
  "Relever la croissance potentielle relève des politiques d’offre ; "
  "combler un écart de production relève des politiques de demande."),

 ("Offre globale", ['25'],
  "Un modèle d’équilibre entre offre globale et demande globale",
  "L’offre globale représente les conditions de production de l’ensemble de "
  "l’économie : la quantité de biens et services que les entreprises "
  "acceptent de produire à chaque niveau général des prix. Confrontée à la "
  "demande globale dans le modèle OG-DG, elle détermine simultanément un "
  "niveau de production — mesuré par le PIB réel en abscisse — et un niveau "
  "général des prix — en ordonnée. Un choc d’offre négatif déplace la courbe "
  "d’offre globale de court terme vers la gauche : les prix augmentent "
  "pendant que la production recule, configuration que les modèles à prix "
  "fixes ne savent pas représenter.",
  ["courbe d offre globale", "og"],
  "L’offre globale n’est pas la somme de courbes d’offre microéconomiques : "
  "elle porte sur la production totale et le niveau général des prix."),

 ("Niveau général des prix", ['25', '2'],
  "Un modèle d’équilibre entre offre globale et demande globale",
  "Le niveau général des prix est l’indicateur synthétique du prix moyen de "
  "l’ensemble des biens et services d’une économie ; sa variation mesure "
  "l’inflation. Il figure en ordonnée du modèle OG-DG, ce qui permet "
  "d’étudier conjointement les variations de la production et celles des "
  "prix. Le modèle IS-LM traditionnel le suppose au contraire fixe : c’est "
  "la principale limite que la stagflation des années 1970 a mise en "
  "évidence.",
  ["niveau des prix"],
  "Un prix relatif compare deux biens ; le niveau général des prix mesure la "
  "valeur de la monnaie elle-même."),

 ("Relance budgétaire", ['25'],
  "Une politique budgétaire expansionniste stimule la demande globale",
  "Une relance budgétaire est une politique budgétaire expansionniste "
  "destinée à soutenir la demande globale lorsque l’économie fonctionne en "
  "dessous de ses capacités : hausse des dépenses publiques, augmentation "
  "des prestations sociales ou baisse des impôts. Dans le modèle IS-LM, elle "
  "déplace la courbe IS vers la droite. Son efficacité est bornée par "
  "l’effet d’éviction — la hausse du taux d’intérêt qu’elle provoque réduit "
  "l’investissement privé — et, en économie ouverte, par les fuites liées "
  "aux importations.",
  ["politique de relance budgetaire", "relance keynesienne"],
  "La relance agit sur la demande ; elle ne relève pas la production "
  "potentielle, qui relève des politiques structurelles."),

 ("Politique de rigueur", ['25', '26'],
  "Une politique de rigueur déplace IS vers la gauche",
  "Une politique de rigueur, ou politique budgétaire restrictive, réduit la "
  "demande globale par la baisse des dépenses publiques ou la hausse des "
  "prélèvements ; dans le modèle IS-LM, elle déplace la courbe IS vers la "
  "gauche. Elle peut être mobilisée pour contenir une surchauffe "
  "inflationniste, limiter un déséquilibre extérieur ou consolider les "
  "finances publiques, mais elle pèse sur l’activité et l’emploi. Le "
  "tournant de la rigueur français de 1983 en fournit l’exemple de "
  "référence.",
  ["politique budgetaire restrictive", "rigueur budgetaire", "austerite budgetaire"],
  "La rigueur vise la demande ; elle ne doit pas être confondue avec une "
  "politique structurelle, qui vise les capacités d’offre."),

 ("Politique monétaire accommodante", ['25'],
  "Premier cas : une politique budgétaire expansionniste accompagnée d’une politique monétaire accommodante",
  "Une politique monétaire est dite accommodante lorsqu’elle soutient les "
  "conditions de financement, notamment en évitant que les taux d’intérêt "
  "n’augmentent. Associée à une relance budgétaire, elle en renforce "
  "l’efficacité : en limitant la hausse du taux d’intérêt, elle réduit "
  "l’effet d’éviction qui amputerait l’investissement privé. C’est la "
  "logique du policy mix Clinton-Greenspan, où une orientation monétaire "
  "accommodante accompagne une consolidation budgétaire pour en limiter "
  "l’effet récessif.",
  ["orientation monetaire accommodante"],
  "Accommodante qualifie une orientation relative aux besoins de "
  "l’économie ; expansionniste qualifie une augmentation de l’offre de "
  "monnaie."),

 ("Critique monétariste", ['25'],
  "La critique monétariste remet en cause les fondements du modèle IS-LM",
  "La critique monétariste conteste l’efficacité durable des politiques de "
  "demande. Elle s’articule en plusieurs arguments que le cours distingue "
  "soigneusement : l’effet d’éviction réduit l’investissement privé ; "
  "l’hypothèse du revenu permanent, formulée par Friedman en 1957, limite la "
  "réponse de la consommation aux transferts temporaires ; l’équivalence "
  "ricardienne, développée par Barro en 1974, conduit des ménages rationnels "
  "à épargner une baisse d’impôts financée par l’endettement ; enfin, "
  "l’existence d’un taux de chômage naturel borne l’effet durable d’une "
  "relance monétaire, qui se dissout en inflation une fois les anticipations "
  "ajustées.",
  ["monetarisme", "critique monetariste du modele is lm"],
  "Ces critiques ne sont pas interchangeables : l’une porte sur le taux "
  "d’intérêt, l’autre sur la consommation, la troisième sur l’épargne "
  "privée, la dernière sur le chômage."),

 ("Critique post-keynésienne", ['25'],
  "Le modèle IS-LM fait l’objet de deux grands ensembles de critiques",
  "La critique post-keynésienne reproche au modèle IS-LM d’avoir trahi "
  "Keynes en transformant une théorie du déséquilibre en un modèle "
  "d’équilibre. Elle souligne notamment que l’égalité comptable entre "
  "épargne et investissement, vérifiée ex post, ne doit pas être confondue "
  "avec une égalité de leurs décisions ex ante : dans la logique du "
  "multiplicateur, c’est l’investissement qui engendre le revenu, puis "
  "l’épargne correspondante, et non l’inverse. Elle conteste ainsi l’idée "
  "qu’une épargne préalable serait nécessaire pour financer tout "
  "investissement supplémentaire au niveau macroéconomique.",
  ["post keynesiens", "critique keynesienne du modele is lm"],
  "Cette critique est interne au keynésianisme : elle vise la formalisation "
  "de Hicks et Hansen, non les conclusions de Keynes."),

 # --------------------------------------- économie ouverte et dilemmes
 ("Balance des transactions courantes", ['25', '21', '26'],
  "La balance globale compare les transactions courantes et les mouvements autonomes de capitaux",
  "La balance des transactions courantes enregistre les échanges de biens et "
  "de services, les revenus et les transferts courants avec le reste du "
  "monde. Son solde indique si le pays dégage une capacité de financement — "
  "excédent — ou présente un besoin de financement — déficit — vis-à-vis du "
  "reste du monde. Il ne suffit pourtant pas à caractériser la position "
  "extérieure : seul son rapprochement avec les mouvements autonomes de "
  "capitaux permet de déterminer la position de la balance globale, de sorte "
  "qu’un pays peut être en excédent courant tout en présentant un déficit "
  "global.",
  ["transactions courantes", "solde courant", "balance courante", "btc"],
  "Le solde courant mesure un besoin ou une capacité de financement ; la "
  "balance globale dit s’il est effectivement compensé."),

 ("Mouvements autonomes de capitaux", ['25'],
  "La balance globale compare les transactions courantes et les mouvements autonomes de capitaux",
  "Les mouvements autonomes de capitaux sont les entrées et sorties de "
  "capitaux décidées par les agents pour des motifs de rendement ou de "
  "placement, indépendamment du financement d’un déséquilibre courant. Dans "
  "le modèle IS-LM-BP, ce sont eux qui, ajoutés au solde courant, "
  "déterminent la balance globale et donc l’équilibre extérieur. Leur "
  "sensibilité aux écarts de taux d’intérêt commande la pente de la courbe "
  "BP : plus les capitaux sont mobiles, plus BP est horizontale.",
  ["solde des mouvements autonomes de capitaux", "mouvements de capitaux"],
  "La présentation du modèle est simplifiée : les opérations sur réserves "
  "officielles et le compte de capital sont laissés de côté."),

 ("Besoin de financement", ['25', '1'],
  "Un déficit courant implique un besoin de financement",
  "Un pays est en besoin de financement lorsque ses transactions courantes "
  "sont déficitaires : il dépense globalement davantage vis-à-vis du reste "
  "du monde qu’il n’en reçoit au titre de ces transactions. Il doit alors se "
  "procurer les ressources correspondantes, notamment en attirant des "
  "capitaux étrangers — ce qui suppose un taux d’intérêt suffisamment "
  "attractif — ou en puisant dans ses réserves. C’est ce lien entre déficit "
  "courant, taux d’intérêt et entrées de capitaux qui donne à la courbe BP "
  "sa pente croissante.",
  ["besoin de financement exterieur"],
  "Le besoin de financement est un solde, la dette extérieure un stock : "
  "l’un alimente l’autre année après année."),

 ("Capacité de financement", ['25'],
  "Un excédent courant correspond à une capacité de financement",
  "Un pays dispose d’une capacité de financement lorsque ses transactions "
  "courantes sont excédentaires : il reçoit du reste du monde davantage "
  "qu’il ne lui verse. Il peut alors acquérir des actifs étrangers ou prêter "
  "au reste du monde, ce qui se traduit par des sorties de capitaux. Selon "
  "l’ampleur de ces sorties, la balance globale sera équilibrée, "
  "excédentaire ou même déficitaire : un excédent courant ne garantit donc "
  "pas un excédent global.",
  ["capacite de financement exterieure"],
  "Capacité et besoin de financement sont les deux faces d’une même "
  "relation : la capacité des uns finance le besoin des autres."),

 ("Mobilité parfaite des capitaux", ['25'],
  "Deux situations extrêmes : mobilité parfaite et absence totale de mobilité",
  "La mobilité parfaite des capitaux est l’hypothèse selon laquelle les "
  "capitaux circulent librement et réagissent immédiatement au moindre écart "
  "de rendement. Le taux d’intérêt domestique s’aligne alors sur le taux "
  "international et la courbe BP devient horizontale. À l’opposé, une "
  "absence totale de mobilité rend BP verticale : l’équilibre extérieur ne "
  "peut plus être rétabli que par les transactions courantes, donc par le "
  "revenu et les importations. La réalité se situe entre les deux — risques "
  "de change, risques politiques, coûts de transaction et différences de "
  "réglementation freinent les mouvements — mais le cours retient "
  "l’hypothèse de mobilité parfaite pour représenter l’intégration "
  "financière européenne.",
  ["parfaite mobilite des capitaux", "mobilite des capitaux parfaite"],
  "C’est cette hypothèse qui rend la politique monétaire inefficace en "
  "changes fixes et la politique budgétaire inefficace en changes "
  "flexibles."),

 ("Triple équilibre", ['25'],
  "Le triple équilibre correspond à l’intersection de IS, LM et BP",
  "Le triple équilibre est l’équilibre macroéconomique complet d’une "
  "économie ouverte : il suppose la compatibilité simultanée de trois "
  "marchés — celui des biens et services (IS), celui de la monnaie (LM) et "
  "les relations avec le reste du monde (BP). Lorsque les trois courbes se "
  "croisent au même point, un couple unique de revenu national et de taux "
  "d’intérêt assure à la fois l’équilibre interne et l’équilibre externe. "
  "Rien ne garantit cependant cette coïncidence : IS et LM peuvent se "
  "croiser en dehors de BP, l’économie connaissant alors un équilibre "
  "intérieur avec déséquilibre extérieur.",
  ["triple equilibre is lm bp"],
  "Le triple équilibre est une situation particulière, non la règle : c’est "
  "de sa non-réalisation que naissent les dilemmes de politique "
  "économique."),

 ("Équilibre interne", ['25'],
  "L’équilibre interne dépend de la position du revenu national par rapport au plein emploi",
  "L’équilibre interne est l’objectif consistant à maintenir un niveau "
  "d’activité compatible avec le plein emploi tout en évitant une inflation "
  "excessive. Il se juge en comparant le revenu national au revenu de plein "
  "emploi : en deçà, l’économie connaît un sous-emploi et des capacités "
  "insuffisamment utilisées, ce qui appelle une politique expansionniste ; "
  "au-delà, la demande excède les capacités productives normales et "
  "engendre des tensions inflationnistes, ce qui appelle une politique "
  "restrictive. Le plein emploi n’y signifie pas l’absence totale de "
  "chômage, mais l’utilisation normale des capacités productives.",
  ["objectif d equilibre interne"],
  "L’équilibre interne concerne l’activité et les prix ; l’équilibre externe "
  "concerne la position vis-à-vis du reste du monde."),

 ("Équilibre externe", ['25'],
  "L’ouverture internationale crée des dilemmes entre équilibre interne et équilibre externe",
  "L’équilibre externe est l’objectif consistant à éviter des déséquilibres "
  "extérieurs incompatibles avec la stabilité de l’économie. Dans le modèle "
  "IS-LM-BP, il est atteint lorsque la balance globale est équilibrée, "
  "c’est-à-dire lorsque le solde courant est compensé par les mouvements "
  "autonomes de capitaux — ce qui ne suppose pas que les transactions "
  "courantes soient elles-mêmes équilibrées. Les politiques permettant de "
  "corriger un déséquilibre externe peuvent aggraver le déséquilibre "
  "interne, et réciproquement.",
  ["objectif d equilibre externe", "equilibre exterieur"],
  "Équilibre externe ne veut pas dire balance courante nulle : il signifie "
  "que le solde courant est financé."),

 ("Dilemme de politique économique", ['25'],
  "Le croisement des équilibres interne et externe fait apparaître quatre situations",
  "Un dilemme de politique économique apparaît lorsque la correction d’un "
  "déséquilibre en aggrave un autre. Le croisement de deux situations "
  "internes — sous-emploi ou inflation — et de deux situations externes — "
  "déficit ou excédent — fait apparaître quatre configurations. Deux ne "
  "posent pas de difficulté majeure, une même orientation améliorant les "
  "deux équilibres. Les deux autres sont des dilemmes : sous-emploi avec "
  "déficit extérieur, où la relance nécessaire à l’emploi creuse le déficit, "
  "et inflation avec excédent, où la rigueur nécessaire aux prix renforce "
  "l’excédent.",
  ["dilemmes de politique economique", "conflit d objectifs"],
  "Le dilemme naît de la rareté des instruments au regard des objectifs : "
  "c’est ce que la règle d’affectation de Mundell cherche à résoudre."),

 ("Système monétaire européen", ['25', '26'],
  "Le système monétaire européen transforme le déficit extérieur en crise de change",
  "Le Système monétaire européen (SME), créé en 1979, maintient les monnaies "
  "européennes autour de parités fixes mais ajustables, afin de limiter les "
  "fluctuations entre elles. Il interdit donc de laisser une monnaie se "
  "déprécier librement : un pays en difficulté extérieure doit défendre sa "
  "parité, ce qui transforme un déficit courant en tension de change. La "
  "France en fait l’expérience entre 1981 et 1983, les difficultés "
  "extérieures alimentant les anticipations de dévaluation et conduisant à "
  "plusieurs ajustements du franc. La libéralisation financière rendra "
  "progressivement cette stabilité difficile à maintenir, jusqu’aux crises "
  "de 1992-1993.",
  ["sme", "serpent monetaire", "parites fixes mais ajustables"],
  "Le SME n’est pas une union monétaire : les monnaies subsistent, et les "
  "parités peuvent être modifiées."),

 ("Critères de Maastricht", ['25'],
  "Les critères de Maastricht encadrent les politiques budgétaires nationales",
  "Les critères de Maastricht sont les critères de convergence posés par le "
  "traité signé en 1992 et entré en vigueur en 1993, qui organise la "
  "création de l’Union économique et monétaire. Deux références budgétaires "
  "y sont particulièrement importantes : un déficit public de 3 % du PIB et "
  "une dette publique de 60 % du PIB. Elles visent à favoriser la discipline "
  "budgétaire et à limiter les déséquilibres susceptibles d’affecter la "
  "stabilité de l’union monétaire ; le Pacte de stabilité et de croissance, "
  "adopté en 1997, complète cet encadrement. Ces seuils ne sont pas des "
  "interdictions absolues : leur application dépend du cadre juridique "
  "européen, de ses procédures et de ses flexibilités.",
  ["criteres de convergence", "pacte de stabilite et de croissance", "3 % et 60 %"],
  "Ces règles traduisent la tentative de concilier souveraineté budgétaire "
  "nationale et politique monétaire commune."),

 ("Passager clandestin", ['25', '5'],
  "L’interdépendance crée une tentation de passager clandestin",
  "Un passager clandestin est un agent qui bénéficie d’un avantage collectif "
  "sans en supporter le coût. Appliquée aux politiques de relance, la "
  "logique est la suivante : une relance étrangère stimule les exportations "
  "nationales, de sorte qu’un gouvernement peut préférer attendre que son "
  "partenaire relance à sa place plutôt que d’engager une dépense "
  "budgétaire. Mais si tous raisonnent ainsi, aucune relance suffisante "
  "n’est engagée et la demande globale demeure insuffisante — d’où l’intérêt "
  "d’une coordination internationale.",
  ["free rider", "comportement de passager clandestin"],
  "C’est le même mécanisme que pour les biens collectifs : la rationalité "
  "individuelle conduit à un résultat collectivement médiocre."),
]
