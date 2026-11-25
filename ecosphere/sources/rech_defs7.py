# -*- coding: utf-8 -*-
"""Définitions rédigées pour le chapitre 5 de deuxième année — premier volet :
fondements du modèle, équilibre en économie fermée et marché de la monnaie.

L'audit de la rubrique « Définitions » a montré que ces notions étaient
employées par le cours sans qu'aucune entrée ne leur réponde. Chaque entrée
est rédigée à partir du passage du cours désigné par `anc` (l'intitulé de la
section) et n'ajoute rien qui ne s'y trouve. Aucune attribution d'auteur
n'est faite au-delà de ce que le chapitre établit.
"""

# (terme, chapitres, intitulé d'ancrage, définition, alias, distinction)
DEFS = [

 # ------------------------------------------- fondements et modélisation
 ("Loi des débouchés", ['25'],
  "La loi des débouchés de Say : une économie pensée du côté de l’offre",
  "Énoncée par Jean-Baptiste Say dans son Traité d’économie politique "
  "(1803), la loi des débouchés se résume par la formule « toute offre crée "
  "sa propre demande » : la production distribue les revenus nécessaires à "
  "l’achat de ce qu’elle produit. Elle suppose que les revenus non consommés "
  "se transforment en dépenses d’investissement et que la monnaie ne sert "
  "que d’intermédiaire des échanges. Dans cette perspective, une "
  "insuffisance généralisée et durable de la demande est difficile à "
  "expliquer — c’est précisément ce que la crise de 1929 et l’analyse "
  "keynésienne remettront en cause.",
  ["loi de say", "toute offre cree sa propre demande", "loi des debouches de say"],
  "À ne pas confondre avec la demande effective de Keynes, qui part du "
  "raisonnement inverse : c’est la demande anticipée qui commande la "
  "production."),

 ("Circuit économique", ['25', '1'],
  "De François Quesnay à Keynes : la représentation de l’économie sous forme de circuit",
  "Le circuit économique représente l’économie comme un ensemble de flux "
  "entre agents plutôt que comme une juxtaposition de marchés. Il repose sur "
  "deux catégories de flux : les flux réels, qui correspondent aux "
  "mouvements de biens, de services et de facteurs de production, et les "
  "flux monétaires, qui correspondent aux paiements et aux revenus associés. "
  "La production y apparaît simultanément comme une création de biens et "
  "services et comme une distribution de revenus, lesquels financent à leur "
  "tour la consommation et l’investissement. Le Tableau économique de "
  "Quesnay (1758) en constitue l’une des premières formulations ; Keynes "
  "renouvelle cette approche en plaçant au centre les relations entre "
  "production, revenus et dépenses.",
  ["circuit", "representation en circuit", "flux reels et flux monetaires"],
  "La représentation en circuit s’oppose à l’analyse par les marchés "
  "isolés : elle explique pourquoi les grandes variables macroéconomiques "
  "sont interdépendantes."),

 ("Comptabilité nationale", ['25', '1'],
  "La comptabilité nationale permet de mesurer l’activité économique",
  "La comptabilité nationale représente quantitativement les grandes "
  "opérations économiques d’un pays et leurs interdépendances. Elle repose "
  "sur l’idée que la production, les dépenses et les revenus constituent "
  "trois dimensions complémentaires d’une même activité, ce qui permet de "
  "mesurer le produit intérieur brut selon trois approches aboutissant au "
  "même résultat. Son développement moderne est lié à la crise de 1929, qui "
  "rend nécessaires des indicateurs de l’activité globale : les travaux de "
  "Simon Kuznets sur le revenu national américain, dans les années 1930, en "
  "constituent une étape fondamentale.",
  ["comptabilite nationale moderne"],
  "Elle fournit la mesure, non l’explication : l’équilibre macroéconomique "
  "est une propriété des comportements, l’identité comptable une convention "
  "d’enregistrement."),

 ("Synthèse néoclassique", ['25'],
  "John Hicks (1937) : la formalisation de l’équilibre simultané",
  "La synthèse néoclassique désigne la démarche qui combine certains "
  "mécanismes keynésiens avec une représentation de l’équilibre inspirée de "
  "l’analyse walrasienne. Le modèle IS-LM, issu de la formalisation de "
  "Hicks puis de Hansen, en est l’expression la plus connue : il conserve "
  "l’idée keynésienne d’une demande déterminante et d’une monnaie active, "
  "mais la traduit dans un cadre d’équilibre simultané de plusieurs marchés. "
  "C’est ce déplacement qui nourrira la critique de certains keynésiens, "
  "pour qui la formalisation transforme une théorie du déséquilibre en un "
  "modèle d’équilibre.",
  ["synthese keynesienne neoclassique"],
  "La synthèse n’est pas la pensée de Keynes elle-même : elle en est une "
  "mise en forme, et c’est l’objet du débat."),

 ("Tâtonnement walrasien", ['25'],
  "Léon Walras : l’équilibre simultané des marchés",
  "Le tâtonnement walrasien est le processus théorique par lequel "
  "l’équilibre général est atteint chez Walras. Un commissaire-priseur "
  "fictif centralise les offres et les demandes, constate les déséquilibres, "
  "annonce de nouveaux prix, et les ajustements se poursuivent jusqu’à ce "
  "que les marchés soient simultanément équilibrés. Il s’agit d’une "
  "construction logique destinée à montrer comment un système de prix peut "
  "rendre compatibles les décisions dispersées des agents, et non d’une "
  "description d’un mécanisme réel.",
  ["commissaire priseur", "tatonnement"],
  "Le tâtonnement décrit la façon d’atteindre l’équilibre général ; "
  "l’optimum de Pareto en qualifie la propriété d’efficacité."),

 ("Optimum de Pareto", ['25', '4'],
  "Vilfredo Pareto : l’efficacité de l’allocation des ressources",
  "Une situation est optimale au sens de Pareto lorsqu’il est impossible "
  "d’améliorer le bien-être d’un agent sans détériorer celui d’au moins un "
  "autre. Sous certaines conditions, un équilibre concurrentiel possède "
  "cette propriété : l’analyse néoclassique associe ainsi le fonctionnement "
  "concurrentiel des marchés à une allocation efficace des ressources. Le "
  "cours souligne aussitôt la limite de ce critère : l’optimalité au sens de "
  "Pareto ne garantit aucune équité dans la répartition des richesses, et "
  "toute intervention publique ne provoque pas nécessairement une perte de "
  "bien-être, puisqu’elle peut corriger des défaillances de marché.",
  ["optimalite au sens de pareto", "optimum parentien", "efficacite parenne"],
  "Critère d’efficacité et non de justice : une répartition très inégale "
  "peut être Pareto-optimale."),

 # ------------------------------- équilibre keynésien en économie fermée
 ("Diagramme à 45°", ['25'],
  "Samuelson (1949) : le diagramme à 45° permet de représenter l’équilibre macroéconomique",
  "Présenté par Paul Samuelson dans son manuel Economics, le diagramme à 45° "
  "représente l’équilibre macroéconomique en portant le revenu national en "
  "abscisse et la demande globale en ordonnée. La bissectrice figure "
  "l’ensemble des points où la production égale la demande ; l’équilibre "
  "effectif se lit à l’intersection entre cette bissectrice et la droite de "
  "demande globale, située au-dessus de la fonction de consommation d’un "
  "montant égal à l’investissement autonome. L’écart entre ce point et le "
  "niveau de plein emploi permet de visualiser directement un équilibre de "
  "sous-emploi ou un écart inflationniste.",
  ["diagramme a 45 degres", "diagramme de samuelson", "bissectrice"],
  "Le diagramme suppose des prix fixes : il représente des quantités, non de "
  "l’inflation, que seul le modèle OG-DG fait apparaître."),

 ("Fonction de consommation keynésienne", ['25', '1'],
  "La fonction de consommation keynésienne",
  "La fonction de consommation keynésienne relie la consommation des "
  "ménages au revenu courant : elle s’écrit C = C₀ + cY, où C₀ est la "
  "consommation autonome et c la propension marginale à consommer. Elle "
  "traduit la loi psychologique fondamentale énoncée par Keynes dans la "
  "Théorie générale (1936) : lorsque le revenu augmente, la consommation "
  "augmente également, mais moins que proportionnellement, de sorte qu’une "
  "partie de tout revenu supplémentaire est épargnée. C’est cette fuite par "
  "l’épargne qui borne le processus du multiplicateur.",
  ["fonction de consommation", "c0 + cy"],
  "Elle fait dépendre la consommation du revenu courant, là où Friedman la "
  "fera dépendre du revenu permanent."),

 ("Revenu d’équilibre", ['25'],
  "La détermination du revenu d’équilibre",
  "Le revenu d’équilibre est le niveau de revenu national pour lequel la "
  "production égale la demande globale. Dans le modèle keynésien simple, il "
  "s’obtient en écrivant Y = C₀ + cY + I, d’où Y* = (C₀ + I) / (1 − c) : le "
  "revenu d’équilibre est donc le produit des dépenses autonomes par le "
  "multiplicateur. C’est un équilibre au sens strict — rien ne pousse "
  "l’économie à s’en écarter — mais rien ne garantit qu’il corresponde au "
  "plein emploi.",
  ["revenu national d equilibre", "production d equilibre"],
  "Équilibre ne signifie pas plein emploi : c’est tout l’apport de Keynes "
  "avec la notion d’équilibre de sous-emploi."),

 ("Investissement autonome", ['25'],
  "L’investissement est provisoirement considéré comme autonome",
  "Un investissement est dit autonome lorsqu’il ne dépend pas du revenu "
  "courant dans le modèle considéré. Dans l’analyse générale de Keynes, "
  "l’investissement dépend des anticipations de demande et du taux "
  "d’intérêt ; mais dans le diagramme à 45° de Samuelson, on le fixe "
  "provisoirement afin d’isoler l’effet de la demande sur la production. "
  "Cette hypothèse est levée ensuite : c’est précisément en faisant dépendre "
  "l’investissement du taux d’intérêt que l’on construit la courbe IS.",
  ["investissement exogene"],
  "Autonome par rapport au revenu ne veut pas dire indépendant de tout : "
  "anticipations et taux d’intérêt continuent de le commander."),

 ("Propension marginale à épargner", ['25'],
  "L’épargne constitue une fuite à chaque période",
  "La propension marginale à épargner mesure la part d’une augmentation du "
  "revenu qui n’est pas consommée : elle vaut s = 1 − c, où c est la "
  "propension marginale à consommer. Avec c = 0,8, la propension marginale à "
  "épargner est de 0,2 : 20 % de chaque revenu supplémentaire sort du "
  "circuit des dépenses de consommation. C’est cette fuite qui explique que "
  "le processus multiplicateur s’amortisse de vague en vague et converge "
  "vers un total fini.",
  ["propension a epargner", "s = 1 - c"],
  "Elle est le complément exact de la propension marginale à consommer, et "
  "l’inverse du multiplicateur en économie fermée sans État."),

 ("Fuite", ['25'],
  "L’épargne constitue une fuite à chaque période",
  "Une fuite est la part d’un revenu supplémentaire qui sort du circuit des "
  "dépenses intérieures et cesse donc d’alimenter les vagues successives du "
  "multiplicateur. Le cours en distingue deux. En économie fermée, la fuite "
  "principale est l’épargne : la part du revenu qui n’est pas consommée. En "
  "économie ouverte s’ajoute une seconde fuite, les importations, puisqu’une "
  "partie de la demande s’adresse à des producteurs étrangers. Plus les "
  "fuites sont importantes, plus le multiplicateur est faible : avec c = 0,8 "
  "et une propension à importer de 0,2, l’ouverture fait passer le "
  "multiplicateur de 5 à 2,5 dans l’exemple du cours.",
  ["fuites du circuit", "fuite du multiplicateur"],
  "La fuite n’est pas une perte pour l’économie mondiale : les importations "
  "deviennent la demande adressée aux partenaires, d’où l’intérêt d’une "
  "relance coordonnée."),

 ("Chômage classique", ['25'],
  "Le chômage néoclassique s’explique par un salaire réel trop élevé",
  "Dans la représentation néoclassique, le travail s’échange sur un marché "
  "où l’offre croît avec le salaire réel et la demande décroît avec lui. "
  "Lorsque le salaire réel se maintient au-dessus de son niveau "
  "d’équilibre, l’offre de travail dépasse la demande : cet excès d’offre "
  "est le chômage. La rigidité du salaire réel empêche alors le retour au "
  "plein emploi, et la flexibilité salariale doit théoriquement le "
  "rétablir. Keynes inverse le raisonnement : le chômage peut provenir "
  "d’une demande globale insuffisante, et une baisse des salaires, en "
  "pesant sur les revenus et la consommation, ne garantit pas le retour au "
  "plein emploi.",
  ["chomage neoclassique", "chomage par le salaire reel"],
  "Chômage classique : le salaire est trop élevé. Chômage keynésien : la "
  "demande est trop faible. Le remède diffère dans les deux cas."),

 ("Salaire réel", ['25'],
  "Le chômage néoclassique s’explique par un salaire réel trop élevé",
  "Le salaire réel rapporte le salaire nominal au niveau général des prix "
  "(W/P) : il mesure le pouvoir d’achat de la rémunération et, du point de "
  "vue de l’entreprise, le coût du travail en termes de production. Dans le "
  "modèle néoclassique du marché du travail, il est la variable qui "
  "équilibre offre et demande de travail : porté au-dessus de son niveau "
  "d’équilibre, il engendre un excès d’offre de travail, c’est-à-dire du "
  "chômage.",
  ["salaire reel w/p"],
  "Le salaire nominal est le montant versé, le salaire réel ce qu’il permet "
  "d’acheter : l’inflation sépare les deux."),

 ("Surchauffe", ['25'],
  "Le mécanisme de la surchauffe",
  "La surchauffe désigne la situation d’une économie dont la demande globale "
  "excède durablement les capacités de production soutenables. Les "
  "entreprises utilisent alors plus intensément leurs équipements, "
  "embauchent, recourent aux heures supplémentaires ; mais lorsque "
  "l’économie est déjà proche du plein emploi, la main-d’œuvre disponible "
  "devient rare et les salaires augmentent pour recruter. L’excès de demande "
  "se transforme en tensions sur les prix : le risque est une accélération "
  "de l’inflation. C’est le contenu concret de l’écart inflationniste.",
  ["surchauffe inflationniste", "surchauffe economique"],
  "La surchauffe est le symétrique du sous-emploi : excès de demande dans un "
  "cas, insuffisance dans l’autre, mesurés l’un et l’autre par l’écart de "
  "production."),

 ("Cercle vicieux de sous-emploi", ['25'],
  "Les anticipations pessimistes entretiennent un cercle vicieux de sous-emploi",
  "Le cercle vicieux de sous-emploi décrit la façon dont le pessimisme des "
  "entreprises se valide lui-même. Anticipant une demande durablement "
  "faible, elles reportent leurs investissements et gèlent leurs "
  "recrutements ; ces décisions réduisent les revenus distribués, les "
  "ménages consomment moins, la demande devient effectivement plus faible et "
  "les anticipations initiales se trouvent confirmées. La crise devient "
  "alors cumulative : la demande privée ne permet plus de retrouver "
  "spontanément le plein emploi, ce qui justifie que l’État prenne le "
  "relais.",
  ["cercle vicieux keynesien", "crise cumulative"],
  "C’est une application de la prophétie autoréalisatrice au niveau "
  "macroéconomique : rien n’est irrationnel dans chaque décision prise "
  "isolément."),

 ("Dépenses publiques", ['25', '1'],
  "La demande globale comprend désormais les dépenses publiques",
  "Les dépenses publiques (G) sont les dépenses des administrations "
  "publiques qui entrent directement dans la demande globale : commandes "
  "aux entreprises, construction d’infrastructures, rénovation de bâtiments "
  "publics. Dans le modèle, l’essentiel est qu’elles s’adressent "
  "directement aux producteurs, contrairement aux prestations sociales ou "
  "aux baisses d’impôts qui transitent d’abord par le revenu disponible des "
  "ménages. C’est ce qui explique que leur multiplicateur soit le plus "
  "élevé des trois leviers budgétaires.",
  ["depense publique", "g"],
  "Au sens de la comptabilité nationale, G recouvre consommation publique et "
  "investissement public selon les conventions retenues."),

 ("Revenu disponible", ['25', '1'],
  "L’État intervient également sur le revenu disponible",
  "Le revenu disponible est ce qui reste aux ménages pour consommer ou "
  "épargner une fois perçues les prestations sociales et versés les "
  "prélèvements obligatoires. Avec l’État, les ménages ne consomment plus en "
  "fonction de leurs seuls revenus primaires : les impôts réduisent leur "
  "capacité de consommation, les prestations sociales l’augmentent. Deux des "
  "trois leviers de relance — hausse des prestations, baisse des impôts — "
  "passent par ce canal, ce qui atténue leur effet puisque les ménages n’en "
  "consomment qu’une partie.",
  ["revenu disponible des menages", "yd"],
  "Agir sur le revenu disponible est moins direct qu’une dépense publique : "
  "une fraction seulement, égale à la propension à consommer, revient à la "
  "demande."),

 ("Prestations sociales", ['25', '1'],
  "L’État dispose de trois leviers pour relancer la demande",
  "Les prestations sociales (F) sont les transferts versés par les "
  "administrations publiques aux ménages. Elles constituent le deuxième "
  "levier de relance : elles n’entrent pas directement dans la demande "
  "globale mais augmentent d’abord le revenu disponible, dont les ménages ne "
  "consomment qu’une partie. Leur multiplicateur est donc inférieur à celui "
  "des dépenses publiques directes. Leur efficacité dépend étroitement de la "
  "propension à consommer des ménages bénéficiaires, ce qui fournit un "
  "argument en faveur d’une redistribution verticale.",
  ["transferts sociaux", "prestation sociale"],
  "Versées aux ménages, elles passent par le revenu disponible ; les "
  "dépenses publiques, adressées aux producteurs, entrent directement dans "
  "la demande."),

 ("Multiplicateur keynésien", ['25'],
  "Kahn (1931) et Keynes (1936) : le principe du multiplicateur",
  "Le multiplicateur est le coefficient qui mesure l’effet d’une variation "
  "initiale de dépense autonome sur le revenu national. Le principe, "
  "développé par Richard Kahn en 1931 puis repris par Keynes en 1936, est "
  "qu’une dépense supplémentaire devient un revenu pour d’autres agents, qui "
  "en consomment une fraction, laquelle devient à son tour un revenu : les "
  "vagues successives s’additionnent jusqu’à une augmentation du revenu plus "
  "que proportionnelle à la dépense initiale. En économie fermée sans État, "
  "il vaut 1/(1 − c) ; chaque fuite supplémentaire — épargne, impôts, "
  "importations — le réduit.",
  ["multiplicateur keynesien de depense", "principe du multiplicateur keynesien"],
  "À ne pas confondre avec le multiplicateur de crédit, qui relie la base "
  "monétaire à la masse monétaire, ni avec l’accélérateur, qui va de la "
  "demande à l’investissement."),
]
