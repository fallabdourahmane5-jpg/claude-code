# -*- coding: utf-8 -*-
"""Définitions rédigées pour le chapitre 6 de deuxième année (taux de change
et systèmes de change) — complément de l'audit.

Ce module porte trois choses :
  - DEFS, les notions du chapitre 26 qu'aucune entrée ne couvrait ;
  - REECRITES, les entrées dont le moissonnage avait retenu un passage qui
    ne définissait pas la notion, ou la définissait pour un autre chapitre ;
  - REJET, RENVOIS et ALIAS, qui corrigent la rubrique sans créer de
    doublon : on écarte les faux termes, on ajoute les renvois manquants et
    on rattache les formulations équivalentes à l'entrée qui existe déjà.

Chaque entrée est rédigée à partir du passage du cours désigné par `anc`
(l'intitulé de la section) et n'ajoute rien qui ne s'y trouve.
"""

# (terme, chapitres, intitulé d'ancrage, définition, alias, distinction)
DEFS = [

 # ------------------------------------- monnaie, devises et cotations
 ("Pouvoir libératoire", ['26'],
  "La monnaie : une créance dotée d’un pouvoir libératoire général",
  "Le pouvoir libératoire de la monnaie est sa capacité à éteindre une "
  "dette : il signifie qu’elle permet de régler une obligation dans les "
  "conditions prévues par le système monétaire et juridique. C’est ce qui "
  "distingue la monnaie des autres actifs : elle est généralement acceptée "
  "en paiement sur son territoire d’émission, et c’est en elle que les prix, "
  "les salaires et les dettes y sont exprimés. Hors de cet espace, la même "
  "unité n’a plus ce statut : elle devient une devise, dont l’usage dépend "
  "de sa convertibilité et de l’acceptation qu’elle rencontre.",
  ["pouvoir liberatoire general", "cours legal"],
  "Le pouvoir libératoire est juridique et territorial ; la convertibilité "
  "est ce qui permet l’usage international."),

 ("Réserve de valeur", ['26', '2'],
  "Le dollar comme réserve de valeur internationale",
  "La fonction de réserve de valeur est la capacité d’une monnaie à "
  "conserver du pouvoir d’achat dans le temps et donc à servir de support "
  "de conservation de la richesse. À l’échelle internationale, elle se "
  "manifeste dans les réserves de change détenues par les banques "
  "centrales, sous forme de dépôts en devises, de titres étrangers ou "
  "d’autres actifs de réserve. Le dollar y occupe la première place, parce "
  "que les actifs libellés en dollars — notamment les titres du Trésor "
  "américain — bénéficient de marchés profonds et liquides qui permettent de "
  "mobiliser rapidement ces réserves.",
  ["fonction de reserve de valeur", "monnaie de reserve"],
  "Troisième des fonctions internationales d’une monnaie, avec "
  "l’intermédiaire des échanges et l’unité de compte ; les trois se "
  "renforcent mutuellement."),

 ("Système monétaire international", ['26', '24'],
  "Le dollar occupe une position centrale dans le système monétaire international",
  "Le système monétaire international désigne l’ensemble des règles, des "
  "institutions et des pratiques qui organisent les relations monétaires "
  "entre pays : régimes de change retenus, monnaies utilisées pour les "
  "règlements et les réserves, modalités d’ajustement des déséquilibres. Le "
  "cours en souligne la hiérarchie : le dollar y occupe une position "
  "centrale parce qu’il cumule les trois fonctions internationales — "
  "véhiculaire, unité de compte et réserve de valeur — dont les effets de "
  "réseau se renforcent mutuellement. Son histoire se lit comme une "
  "succession d’arbitrages à l’intérieur du triangle de Mundell.",
  ["smi", "systeme monetaire mondial"],
  "Le système monétaire international encadre les relations entre monnaies ; "
  "un régime de change est le choix fait par un pays à l’intérieur de ce "
  "cadre."),

 ("Volatilité", ['26'],
  "La volatilité du change",
  "La volatilité désigne l’ampleur des variations d’un cours autour de sa "
  "trajectoire, généralement mesurée statistiquement sur une période "
  "donnée. Une forte volatilité du change signifie que les cours connaissent "
  "des variations importantes ou fréquentes, ce qui accroît l’incertitude "
  "pour les agents exposés au risque de change : une entreprise européenne "
  "devant régler une facture en dollars dans six mois voit son coût en euros "
  "varier avec le cours, ce qui pèse sur ses marges. Il faut distinguer "
  "cette agitation de court terme des mouvements de plus longue durée, qui "
  "reflètent des transformations de la conjoncture.",
  ["volatilite du change", "volatilite des cours"],
  "La volatilité mesure l’instabilité, non le niveau : une monnaie peut "
  "être stable à un niveau surévalué."),

 # ------------------------------------------ marché des changes
 ("Produits dérivés", ['26', '2'],
  "La multiplication des produits dérivés",
  "Les produits dérivés sont des instruments financiers dont la valeur "
  "dépend de celle d’un sous-jacent — ici le taux de change. Sur le marché "
  "des changes, ils permettent de transférer ou de modifier l’exposition "
  "aux fluctuations futures : opérations à terme, options, swaps. Ils "
  "peuvent servir à la couverture comme à la spéculation, et leur "
  "multiplication explique une part importante de l’expansion des volumes "
  "traités : les opérations au comptant ne représentent plus qu’environ un "
  "tiers des transactions, contre près de la moitié pour les seuls swaps.",
  ["instruments derives", "derives de change"],
  "Un dérivé n’est pas par nature spéculatif : le même contrat sert à se "
  "couvrir ou à prendre position, selon l’exposition initiale de l’agent."),

 ("Option de change", ['26'],
  "Les options et les swaps permettent de gérer le risque de change",
  "Une option de change donne le droit, mais non l’obligation, d’acheter ou "
  "de vendre une devise à un taux déterminé, selon les conditions du "
  "contrat ; son acheteur verse en contrepartie une prime. Une entreprise "
  "qui craint une appréciation du dollar peut ainsi s’assurer un taux "
  "d’achat : si le dollar s’apprécie fortement, elle exerce son option et "
  "limite la hausse de son coût ; s’il se déprécie, elle y renonce et "
  "achète au taux de marché devenu plus favorable, la prime restant acquise "
  "au vendeur. L’option fonctionne donc comme une assurance contre une "
  "évolution défavorable du change.",
  ["option sur devises", "prime d option"],
  "L’option laisse le choix d’exercer, le contrat à terme oblige : c’est ce "
  "qui justifie le paiement d’une prime."),

 ("Couverture", ['26'],
  "La couverture : réduire l’exposition au risque de change",
  "Se couvrir, c’est réduire son exposition au risque de change. Un agent "
  "est exposé lorsqu’une variation du taux peut modifier la valeur de ses "
  "recettes, de ses dépenses ou de ses actifs : une entreprise française "
  "payée en dollars dans six mois craint une dépréciation du dollar et peut "
  "vendre à terme les devises qu’elle recevra, sécurisant ainsi ses recettes "
  "futures. Un transfert de risque suppose toutefois qu’un autre acteur "
  "accepte la position correspondante : intermédiaires financiers et "
  "spéculateurs jouent ce rôle.",
  ["se couvrir", "operation de couverture", "hedging"],
  "La couverture réduit l’incertitude, la spéculation l’accepte "
  "volontairement : ce sont deux attitudes face au même risque, et elles "
  "sont complémentaires."),

 ("Spéculation stabilisatrice", ['26'],
  "Des anticipations de retour à la moyenne",
  "La spéculation est dite stabilisatrice lorsqu’elle ramène le taux de "
  "change vers son niveau d’équilibre. Elle repose sur des anticipations de "
  "retour à la moyenne : si les investisseurs jugent qu’une dépréciation "
  "est temporaire, ils achètent la devise devenue bon marché dans l’espoir "
  "de la revendre après sa remontée ; ces achats accroissent la demande et "
  "corrigent la baisse initiale. Le mécanisme suppose donc que les agents "
  "anticipent un retour vers un niveau de référence.",
  ["anticipations de retour a la moyenne", "speculation stabilisante"],
  "Symétrique de la spéculation déstabilisatrice : tout dépend de la façon "
  "dont les agents interprètent la variation initiale."),

 ("Spéculation déstabilisatrice", ['26'],
  "Des anticipations de poursuite de la tendance",
  "La spéculation est dite déstabilisatrice lorsqu’elle amplifie le "
  "mouvement initial du change. Elle repose sur des anticipations de "
  "poursuite de la tendance : en période de forte incertitude, une "
  "dépréciation n’est plus lue comme une occasion d’achat mais comme le "
  "début d’une chute prolongée, et les investisseurs vendent rapidement "
  "pour éviter des pertes plus importantes, ce qui accentue la baisse. Le "
  "mécanisme devient particulièrement puissant lorsque les anticipations "
  "contribuent elles-mêmes à provoquer l’événement anticipé.",
  ["speculation destabilisante", "anticipations de poursuite de la tendance",
   "anticipations mimetiques"],
  "Le marché des changes peut donc être simultanément stabilisateur et "
  "déstabilisateur, selon la période et l’interprétation des agents."),

 # ----------------------------------------------- parité des pouvoirs d'achat
 ("PPA absolue", ['26'],
  "La PPA absolue détermine un taux de change d’équilibre à partir des niveaux de prix",
  "La parité des pouvoirs d’achat absolue affirme que le taux de change "
  "d’équilibre doit égaliser le prix d’un même panier de biens et services "
  "dans deux pays. Si un panier vaut 100 € en Europe et 120 $ aux "
  "États-Unis, le taux théorique est de 1 € pour 1,20 $ : exprimés dans une "
  "même monnaie, les deux paniers coûtent alors exactement la même chose. "
  "Le taux observé sur le marché peut s’en écarter, et c’est cet écart qui "
  "permet de parler de surévaluation ou de sous-évaluation par rapport à la "
  "PPA.",
  ["parite des pouvoirs d achat absolue"],
  "La PPA absolue compare des niveaux de prix ; la PPA relative compare "
  "leurs évolutions."),

 ("PPA relative", ['26'],
  "La PPA relative repose sur les différentiels d’inflation",
  "La parité des pouvoirs d’achat relative affirme que les variations du "
  "taux de change tendent, à long terme, à compenser les différences "
  "d’inflation entre pays : la monnaie du pays dont les prix augmentent le "
  "plus vite doit se déprécier d’autant, de façon à préserver les positions "
  "relatives. Elle ne prétend donc pas fixer un niveau de change, mais "
  "expliquer son évolution par les différentiels d’inflation.",
  ["parite des pouvoirs d achat relative", "differentiel d inflation"],
  "La PPA relative est une relation de long terme : elle n’explique pas les "
  "mouvements de court terme, dominés par les capitaux et les "
  "anticipations."),

 ("Surévaluation", ['26'],
  "La comparaison entre taux de change observé et taux de PPA permet d’identifier les écarts de valorisation",
  "Une monnaie est surévaluée lorsque son cours de marché est supérieur au "
  "taux qu’indiquerait la parité des pouvoirs d’achat : un même panier y "
  "coûte alors plus cher qu’à l’étranger une fois converti. Si le taux de "
  "PPA est de 1 € pour 1,20 $ et que le marché cote 1 € pour 1,40 $, le "
  "panier européen revient à 140 $ contre 120 $ aux États-Unis : l’euro est "
  "surévalué. Une surévaluation pèse sur la compétitivité-prix des "
  "exportateurs ; mais le cours avertit qu’un écart à la PPA ne signifie pas "
  "que la monnaie soit surévaluée au regard de l’ensemble des fondamentaux.",
  ["monnaie surevaluee", "surevaluation de la monnaie"],
  "La PPA n’est qu’une référence théorique parmi d’autres pour juger d’une "
  "valorisation."),

 ("Sous-évaluation", ['26'],
  "La comparaison entre taux de change observé et taux de PPA permet d’identifier les écarts de valorisation",
  "Une monnaie est sous-évaluée lorsque son cours de marché est inférieur au "
  "taux qu’indiquerait la parité des pouvoirs d’achat : un même panier y "
  "coûte moins cher qu’à l’étranger une fois converti. Avec un taux de PPA "
  "de 1 € pour 1,20 $ et un marché cotant 1 € pour 1 $, le panier européen "
  "revient à 100 $ contre 120 $ aux États-Unis : l’euro est sous-évalué. "
  "Une sous-évaluation soutient la compétitivité-prix des exportateurs, ce "
  "qui explique qu’elle puisse être recherchée — et contestée comme une "
  "forme de concurrence déloyale.",
  ["monnaie sous evaluee", "sous evaluation de la monnaie"],
  "Symétrique de la surévaluation, et mesurée par rapport à la même "
  "référence : la PPA, non un niveau « juste » en soi."),

 ("Biens non échangeables", ['26'],
  "L’existence de biens non échangeables limite la PPA",
  "Les biens et services non échangeables sont ceux qui ne peuvent pas "
  "faire l’objet d’un commerce international aisé : certains services à la "
  "personne, les prestations locales, de nombreux services immobiliers. Leur "
  "prix dépend des conditions économiques nationales et ne peut donc pas "
  "être égalisé par l’arbitrage international. Leur poids dans le panier de "
  "consommation est l’une des raisons pour lesquelles la parité des "
  "pouvoirs d’achat n’est pas vérifiée empiriquement, au même titre que les "
  "coûts de transport, d’assurance, les différences fiscales et les "
  "obstacles réglementaires.",
  ["biens non echangeables", "services non echangeables"],
  "C’est aussi le point de départ de l’effet Balassa-Samuelson, qui explique "
  "des écarts durables de niveaux de prix entre pays."),

 # ------------------------------------------- régimes et politique de change
 ("Euroïsation", ['26'],
  "La dollarisation et l’euroïsation : l’abandon de la monnaie nationale",
  "L’euroïsation est l’adoption de l’euro comme monnaie officielle par un "
  "pays qui renonce à la sienne — la dollarisation désignant la même "
  "opération au profit du dollar. C’est la forme la plus radicale "
  "d’abandon de souveraineté monétaire : elle intervient souvent après une "
  "crise majeure, effondrement de la monnaie nationale ou perte de "
  "confiance dans les autorités monétaires, et vise à restaurer la "
  "confiance. Le pays renonce alors à toute politique monétaire autonome, "
  "ne peut plus créer librement de monnaie ni dévaluer pour améliorer sa "
  "compétitivité, et dépend des conditions monétaires de la devise adoptée.",
  ["euroisation"],
  "Contrairement à l’union monétaire, l’euroïsation est unilatérale : le "
  "pays adopte la monnaie sans participer aux décisions qui la gouvernent."),

 ("Parité centrale", ['26'],
  "Les bandes de fluctuation",
  "La parité centrale est le taux de change de référence autour duquel une "
  "monnaie est autorisée à fluctuer dans un régime de change fixe. La "
  "banque centrale ne défend pas un taux absolument immuable : elle accepte "
  "une variation limitée de part et d’autre de cette parité, à l’intérieur "
  "de bandes de fluctuation — par exemple ± 2 % autour d’une parité "
  "centrale de 1 euro pour 7 unités nationales. Il faut donc distinguer la "
  "parité centrale, qui est l’engagement, et les marges, qui mesurent la "
  "souplesse consentie.",
  ["parite officielle", "parite de reference"],
  "La parité centrale peut être modifiée : c’est une dévaluation ou une "
  "réévaluation, à distinguer d’un simple mouvement à l’intérieur des "
  "bandes."),

 ("Flottement libre", ['26'],
  "Les régimes de change forment un continuum entre ancrage strict et flottement libre",
  "Dans un régime de flottement libre, le taux de change est déterminé par "
  "l’offre et la demande sur le marché des changes, la banque centrale ne "
  "défendant aucune parité officielle. La valeur externe de la monnaie "
  "s’ajuste donc en continu, sans engagement de défense. Le flottement "
  "n’interdit pas pour autant toute intervention : les autorités peuvent "
  "intervenir ponctuellement, seules ou de façon concertée, lorsque les "
  "fluctuations deviennent problématiques. La zone euro illustre un cas "
  "intermédiaire : union monétaire entre ses membres, elle flotte vis-à-vis "
  "du dollar, du yen ou de la livre.",
  ["flottement", "changes flottants", "flottement administre", "flottement impur"],
  "Flottement libre et flottement administré diffèrent par la fréquence et "
  "l’ampleur des interventions, non par l’existence d’une parité."),

 ("Endettement en devises", ['26'],
  "L’endettement en devises rend la dépréciation particulièrement dangereuse",
  "Un pays est endetté en devises lorsque ses entreprises, ses banques ou "
  "son État ont emprunté dans une monnaie étrangère — le plus souvent le "
  "dollar — alors que leurs revenus sont perçus en monnaie nationale. Une "
  "dépréciation accroît alors mécaniquement la valeur de ces dettes "
  "exprimée en monnaie nationale, sans que les revenus suivent : c’est "
  "l’effet de bilan, qui peut dégrader brutalement la situation financière "
  "des débiteurs. C’est l’une des raisons pour lesquelles de nombreux pays "
  "émergents redoutent la flexibilité du change.",
  ["dette en devises", "dette libellee en devises"],
  "L’endettement en devises renverse l’effet attendu d’une dépréciation : "
  "au lieu de soutenir l’économie, elle peut la fragiliser."),

 ("Libre circulation des capitaux", ['26', '25'],
  "La libre circulation des capitaux",
  "La libre circulation des capitaux est l’absence d’entrave aux mouvements "
  "financiers internationaux. Le cours lui reconnaît deux avantages : elle "
  "permet aux pays dont l’épargne nationale est insuffisante de mobiliser "
  "l’épargne internationale pour financer leurs investissements — "
  "avantage particulièrement important pour les pays en développement — et "
  "elle favorise une allocation plus efficace du capital à l’échelle "
  "mondiale. C’est l’un des trois sommets du triangle de Mundell, et donc "
  "l’un des trois objectifs entre lesquels il faut arbitrer.",
  ["mobilite internationale des capitaux", "liberte de circulation des capitaux"],
  "Son corollaire est la contrainte : avec des capitaux mobiles, il faut "
  "renoncer soit à la fixité du change, soit à l’autonomie monétaire."),

 ("Autonomie de la politique monétaire", ['26', '25'],
  "L’autonomie de la politique monétaire",
  "L’autonomie de la politique monétaire est la capacité des autorités "
  "monétaires à fixer leurs taux d’intérêt en fonction de la situation "
  "économique nationale, et donc à stabiliser l’économie face aux chocs. "
  "Elle constitue à ce titre un instrument de politique conjoncturelle : "
  "dans les économies avancées, les banques centrales visent généralement "
  "une inflation proche de 2 %. C’est le deuxième sommet du triangle de "
  "Mundell : la conserver interdit de poursuivre simultanément la stabilité "
  "du change et la parfaite mobilité des capitaux.",
  ["autonomie monetaire", "independance de la politique monetaire"],
  "L’autonomie porte sur le choix des taux, non sur l’indépendance "
  "statutaire de la banque centrale vis-à-vis du pouvoir politique."),

 ("Modération salariale", ['26', '22'],
  "Une modération salariale qui entretient la faiblesse de la demande",
  "La modération salariale est la limitation volontaire ou contrainte de la "
  "progression des salaires. Dans la stratégie de désinflation compétitive, "
  "elle joue un rôle central : un chômage élevé réduit le pouvoir de "
  "négociation des salariés, les augmentations deviennent plus limitées, ce "
  "qui contribue à contenir l’inflation et à restaurer les marges des "
  "entreprises. Mais elle freine aussi la consommation des ménages, "
  "entretenant la faiblesse de la demande intérieure — c’est le paradoxe de "
  "la désinflation compétitive.",
  ["moderation des salaires"],
  "Ce qui améliore la compétitivité-coût peut dégrader la demande "
  "intérieure : le même mécanisme a deux effets opposés."),

 ("Taux de marge", ['26', '1'],
  "Une restauration du taux de marge des entreprises",
  "Le taux de marge mesure la part de la valeur ajoutée qui revient à "
  "l’entreprise sous forme d’excédent brut d’exploitation : il se calcule "
  "par le rapport EBE / VA. Il renseigne sur la rentabilité et sur la "
  "capacité d’autofinancement : une augmentation des marges permet de "
  "dégager davantage de ressources financières, ce qui est précisément la "
  "logique du théorème de Schmidt. Le cours relève qu’en France, le taux de "
  "marge passe d’environ 25 % en 1985 à environ 32 % en 1989, soit un "
  "redressement de l’ordre de sept points.",
  ["ebe / va", "taux de marge des entreprises"],
  "Un taux de marge élevé est une condition de l’investissement, non une "
  "garantie : l’investissement dépend aussi des débouchés anticipés."),

 ("Cryptoactif", ['26'],
  "Les cryptoactifs non adossés à une monnaie officielle",
  "Les cryptoactifs sont des actifs numériques reposant sur des technologies "
  "de registres distribués, notamment la blockchain, et qui ne sont pas "
  "adossés à une monnaie officielle. Leur valeur peut connaître des "
  "fluctuations importantes : ils sont donc principalement utilisés comme "
  "actifs spéculatifs ou supports de placement, même s’ils peuvent aussi "
  "servir à certains paiements. Leur forte volatilité limite précisément "
  "leur capacité à remplir de manière stable les fonctions traditionnelles "
  "de la monnaie.",
  ["crypto actif", "cryptomonnaie", "crypto monnaie", "bitcoin"],
  "À distinguer des stablecoins, dont l’émetteur cherche à maintenir la "
  "valeur par rapport à un actif de référence, et des monnaies numériques "
  "de banque centrale, qui sont une créance sur la banque centrale."),

 ("Droits de douane", ['26', '23'],
  "Les droits de douane renchérissent les importations",
  "Un droit de douane est une taxe appliquée aux produits importés, qui en "
  "augmente le coût. Les objectifs recherchés sont de favoriser la "
  "production nationale, de réduire les importations et d’améliorer le "
  "solde commercial. Le chapitre en souligne un effet monétaire moins "
  "attendu : les importateurs peuvent répercuter une partie du droit sur "
  "leurs prix de vente, alimentant l’inflation ; si la banque centrale y "
  "répond par des taux plus élevés, la monnaie peut s’apprécier — à rebours "
  "d’une politique qui chercherait à l’affaiblir. L’effet n’est toutefois "
  "pas automatique : anticipations de croissance, réactions des partenaires "
  "et confiance financière peuvent au contraire provoquer une dépréciation.",
  ["droit de douane", "tarif douanier"],
  "Instrument de politique commerciale, le droit de douane produit aussi "
  "des effets monétaires, ce qui peut contredire l’objectif de change "
  "poursuivi."),

 ("Solde commercial", ['26', '21'],
  "Précision sur la mesure du solde commercial",
  "Le solde commercial est la différence entre la valeur des exportations et "
  "celle des importations de biens. Sa réaction à une dépréciation n’est pas "
  "immédiate : à court terme, les effets-prix dominent — les importations "
  "facturées en devises coûtent aussitôt plus cher en monnaie nationale, "
  "alors que les recettes d’exportation exprimées en monnaie nationale ne "
  "diminuent pas nécessairement — et le déficit se creuse. À moyen terme "
  "apparaissent les effets-volume, les acheteurs adaptant leurs achats, et "
  "le solde s’améliore : c’est le tracé de la courbe en J.",
  ["balance commerciale", "solde du commerce exterieur"],
  "Le solde commercial ne porte que sur les biens ; la balance des "
  "transactions courantes y ajoute services, revenus et transferts."),
]


# Entrées déjà présentes dans la rubrique, mais dont le moissonnage avait
# retenu un passage qui ne les définissait pas, ou les définissait pour un
# autre chapitre. On les réécrit : la clé étant la même, l'entrée est
# remplacée et non dupliquée.
REECRITES = [

 ("Monnaie", ['26', '2'],
  "La monnaie : une créance dotée d’un pouvoir libératoire général",
  "La monnaie est un actif généralement accepté en paiement, qui prend dans "
  "les systèmes contemporains la forme d’une créance monétaire et permet "
  "d’éteindre les dettes comme de réaliser les transactions. Elle remplit "
  "trois fonctions : moyen d’échange, unité de compte et réserve de valeur. "
  "Sur son territoire d’émission, elle est dotée d’un pouvoir libératoire "
  "général : c’est en elle que les prix, les salaires et les dettes sont "
  "exprimés. Du point de vue d’agents extérieurs à cet espace, la même "
  "unité prend le statut de devise.",
  ["monnaie nationale"],
  "Il faut distinguer la nature économique de la monnaie et son statut pour "
  "un résident ou un non-résident : une monnaie chez elle est une devise "
  "ailleurs."),

 ("Unité de compte", ['26', '2'],
  "Le dollar comme unité de compte",
  "La fonction d’unité de compte est la capacité d’une monnaie à servir "
  "d’étalon commun pour exprimer et comparer les valeurs : les prix, les "
  "salaires et les dettes y sont libellés. À l’échelle internationale, elle "
  "permet de facturer et de mesurer les échanges dans une même monnaie, "
  "quelles que soient les nationalités des parties — rôle que le dollar "
  "remplit pour de nombreuses matières premières. C’est l’une des trois "
  "fonctions dont le cumul fait d’une monnaie une monnaie internationale.",
  ["fonction d unite de compte", "etalon de valeur"],
  "L’unité de compte mesure, le moyen d’échange règle, la réserve de valeur "
  "conserve : les trois fonctions sont distinctes et peuvent être remplies "
  "inégalement."),

 ("Inflation", ['26', '2', '1'],
  "La dépréciation peut alimenter l’inflation importée",
  "L’inflation est l’augmentation durable du niveau général des prix ; elle "
  "se mesure par un indice des prix à la consommation. Le chapitre en "
  "éclaire une source proprement monétaire : dans une économie dépendante "
  "des importations, une dépréciation renchérit les biens importés en "
  "monnaie nationale et provoque une inflation importée, qui réduit le "
  "pouvoir d’achat des ménages et peut contraindre la banque centrale à "
  "relever ses taux. Symétriquement, une monnaie forte abaisse les prix à "
  "l’importation et soutient la désinflation.",
  ["hausse du niveau general des prix"],
  "L’inflation est une hausse du niveau des prix ; la désinflation un "
  "ralentissement de cette hausse ; la déflation une baisse des prix."),

 ("Dépréciation", ['26', '25'],
  "Le niveau et l’évolution du taux de change",
  "La dépréciation est la diminution de la valeur d’une monnaie "
  "relativement à une autre, résultant du jeu du marché en régime flottant. "
  "Elle rend les produits nationaux moins chers pour les acheteurs "
  "étrangers et les importations plus coûteuses : elle soutient donc la "
  "compétitivité-prix tout en alimentant l’inflation importée. En régime de "
  "change fixe, une baisse équivalente décidée par les autorités porte un "
  "autre nom : la dévaluation.",
  ["depreciation monetaire", "baisse du cours d une monnaie"],
  "Dépréciation et appréciation relèvent du marché ; dévaluation et "
  "réévaluation sont des décisions officielles en changes fixes."),

 ("Appréciation", ['26', '25'],
  "Le niveau et l’évolution du taux de change",
  "L’appréciation est l’augmentation de la valeur d’une monnaie "
  "relativement à une autre, résultant du jeu du marché en régime flottant. "
  "Elle abaisse le prix des importations — ce qui contribue à contenir "
  "l’inflation — mais renchérit les produits nationaux pour les acheteurs "
  "étrangers et pèse donc sur la compétitivité-prix des exportateurs. En "
  "régime de change fixe, la hausse équivalente décidée par les autorités "
  "s’appelle une réévaluation.",
  ["appreciation monetaire", "hausse du cours d une monnaie", "reevaluation"],
  "L’appréciation est subie par les autorités en changes flottants ; la "
  "réévaluation est un acte officiel en changes fixes."),

 ("Dévaluation", ['26', '25'],
  "Dévaluation subie et dévaluation compétitive",
  "Une dévaluation est la baisse officielle de la parité d’une monnaie, "
  "décidée par les autorités dans un régime de change fixe. Le cours en "
  "distingue deux figures : la dévaluation subie, imposée par la pression "
  "des marchés lorsque la parité n’est plus tenable, et la dévaluation "
  "compétitive, recherchée pour améliorer la compétitivité-prix des "
  "producteurs nationaux. Son efficacité n’a rien d’automatique : elle "
  "dépend du décalage décrit par la courbe en J, de la condition de "
  "Marshall-Lerner, du comportement de marge des entreprises et de la place "
  "de la compétitivité hors prix dans la spécialisation du pays.",
  ["devaluation subie", "devaluation officielle"],
  "La dévaluation est une décision, la dépréciation un mouvement de "
  "marché ; la dévaluation compétitive est une stratégie, la dévaluation "
  "subie un constat d’échec."),

 ("Dette extérieure", ['26', '7', '21'],
  "L’endettement en devises rend la dépréciation particulièrement dangereuse",
  "La dette extérieure est la dette contractée auprès de créanciers "
  "étrangers, par opposition à la dette domestique. Lorsqu’elle est libellée "
  "en devises, elle expose le pays à l’effet de bilan : une dépréciation de "
  "la monnaie nationale en augmente la charge sans accroître les revenus qui "
  "la remboursent. C’est le mécanisme qui transforme une tension de change "
  "en crise de la dette, comme lors du choc Volcker du début des années "
  "1980.",
  ["dette exterieure publique", "dette souveraine exterieure"],
  "Dette extérieure désigne le créancier, dette en devises la monnaie de "
  "libellé : une dette extérieure peut être libellée en monnaie nationale, "
  "et inversement."),

 ("Financiarisation", ['26', '8', '2'],
  "Le développement spectaculaire du Forex révèle la financiarisation de l’économie mondiale",
  "La financiarisation désigne la place croissante prise par les opérations "
  "financières dans l’économie. Le marché des changes en offre une mesure "
  "directe : les volumes traités sont sans commune mesure avec les flux de "
  "biens et de services, et les opérations au comptant sont devenues "
  "minoritaires au profit des swaps, des opérations à terme et des options. "
  "Cette déconnexion entre transactions financières et échanges réels "
  "n’autorise pourtant pas à assimiler l’ensemble des opérations dérivées à "
  "de la spéculation : elles servent aussi à la couverture et à la gestion "
  "de liquidité.",
  ["financiarisation de l economie"],
  "Le volume des transactions mesure l’intensité de l’activité financière, "
  "non la part qui relève de la spéculation."),

 ("Anticipations", ['26', '25'],
  "Des anticipations de poursuite de la tendance",
  "Une anticipation est la représentation que les agents se font de "
  "l’évolution future d’une variable et sur laquelle ils fondent leurs "
  "décisions. Sur le marché des changes, leur rôle est déterminant : selon "
  "que les opérateurs interprètent une variation comme temporaire — "
  "anticipations de retour à la moyenne — ou comme le début d’une tendance "
  "— anticipations de poursuite —, la spéculation stabilise ou amplifie le "
  "mouvement. Lorsque l’anticipation contribue à provoquer ce qu’elle "
  "annonce, elle devient autoréalisatrice.",
  ["anticipation"],
  "Une anticipation n’est pas une prévision neutre : en orientant les "
  "comportements, elle agit sur la réalité qu’elle décrit."),

 ("Prix", ['26', '4'],
  "Un marché sur lequel se forme le prix des monnaies",
  "Le prix est le taux auquel un bien, un service ou un actif s’échange "
  "contre de la monnaie ; il résulte de la confrontation d’une offre et "
  "d’une demande. Le marché des changes applique cette logique aux monnaies "
  "elles-mêmes : le taux de change y est le prix d’une monnaie exprimé dans "
  "une autre, formé par l’offre et la demande de devises. Ce prix "
  "particulier n’est pas un prix comme les autres, puisqu’il commande "
  "simultanément tous les prix relatifs entre deux économies.",
  ["prix d une monnaie", "formation des prix"],
  "Le prix d’un bien ne concerne qu’un marché ; le taux de change, prix "
  "d’une monnaie, affecte l’ensemble des échanges entre deux pays."),

 ("Flexibilité", ['26', '25'],
  "La flexibilisation du marché du travail",
  "La flexibilité désigne la capacité d’un prix ou d’un marché à s’ajuster. "
  "Le cours en mobilise deux usages. La flexibilité du change est "
  "l’ajustement du taux de change par le marché, présenté comme un "
  "mécanisme d’ajustement extérieur : la dépréciation corrige les déficits, "
  "l’appréciation les excédents. La flexibilité du marché du travail "
  "désigne l’assouplissement des règles qui encadrent l’emploi et les "
  "salaires, recherchée dans la désinflation compétitive pour contenir les "
  "coûts et renforcer la compétitivité.",
  ["flexibilite du change", "flexibilite du marche du travail", "flexibilisation"],
  "Flexibilité du change et flexibilité des salaires sont deux "
  "ajustements distincts, qui ne jouent ni sur les mêmes marchés ni aux "
  "mêmes horizons."),

 # --- entrées du chapitre 25 dont le passage moissonné ne définissait rien
 ("Consommation", ['25', '1'],
  "La fonction de consommation keynésienne",
  "La consommation désigne l’utilisation de biens et de services pour la "
  "satisfaction des besoins ; elle constitue la principale composante de la "
  "demande globale. Dans l’analyse keynésienne retenue par le modèle, elle "
  "dépend principalement du revenu courant et s’écrit C = C₀ + cY : une part "
  "autonome, indépendante du revenu, et une part proportionnelle au revenu "
  "par la propension marginale à consommer. La loi psychologique "
  "fondamentale précise que la consommation augmente avec le revenu, mais "
  "moins que proportionnellement.",
  ["consommation des menages"],
  "La consommation finale est le fait des ménages ; la consommation "
  "intermédiaire est détruite dans le processus de production."),

 ("Multiplicateur", ['25', '1'],
  "Kahn (1931) et Keynes (1936) : le principe du multiplicateur",
  "Un multiplicateur est un coefficient qui mesure l’ampleur de l’effet "
  "final d’une impulsion initiale. En macroéconomie keynésienne, le "
  "multiplicateur mesure l’effet d’une variation de dépense autonome sur le "
  "revenu national : la dépense initiale devient un revenu, dont une "
  "fraction est consommée, qui devient à son tour un revenu, et ainsi de "
  "suite. En économie fermée sans État, il vaut 1/(1 − c). Le cours en "
  "décline plusieurs versions : multiplicateur d’investissement, de dépenses "
  "publiques, des prestations sociales, fiscal, et budgétaire une fois "
  "l’effet d’éviction pris en compte.",
  ["effet multiplicateur", "coefficient multiplicateur"],
  "À distinguer du multiplicateur de crédit, qui relie base monétaire et "
  "masse monétaire, et de l’accélérateur, qui relie la demande à "
  "l’investissement."),

 ("Principe du multiplicateur", ['25', '1'],
  "Kahn (1931) et Keynes (1936) : le principe du multiplicateur",
  "Le principe du multiplicateur énonce qu’une augmentation initiale de la "
  "dépense autonome entraîne une augmentation plus que proportionnelle du "
  "revenu national. Développé par Richard Kahn en 1931, d’abord à propos "
  "des effets de l’investissement sur l’emploi, il est repris et élargi par "
  "Keynes en 1936. Le mécanisme repose sur la chaîne des revenus : la "
  "dépense des uns est le revenu des autres, dont une fraction égale à la "
  "propension marginale à consommer est dépensée à son tour. Les fuites — "
  "épargne, puis impôts et importations — bornent le processus et le font "
  "converger.",
  ["principe du multiplicateur keynesien"],
  "Le principe énonce le mécanisme ; le multiplicateur en est la mesure "
  "chiffrée."),

 ("Politique budgétaire", ['25', '1', '21'],
  "Les politiques budgétaires cherchent à influencer la demande globale",
  "La politique budgétaire est l’utilisation des dépenses publiques et des "
  "prélèvements pour agir sur l’activité économique. Expansionniste, elle "
  "soutient la demande globale lorsque l’économie fonctionne en dessous de "
  "ses capacités ; restrictive, elle la freine pour contenir une surchauffe, "
  "limiter un déséquilibre extérieur ou consolider les finances publiques. "
  "Dans le modèle IS-LM, toute politique budgétaire se traduit par un "
  "déplacement de la courbe IS : vers la droite en cas de relance, vers la "
  "gauche en cas de rigueur.",
  ["politiques budgetaires"],
  "La politique budgétaire agit sur le marché des biens et déplace IS ; la "
  "politique monétaire agit sur le marché de la monnaie et déplace LM."),

 ("Politique monétaire", ['25', '2', '26'],
  "Toute politique monétaire déplace la courbe LM",
  "La politique monétaire est l’action des autorités monétaires sur la "
  "quantité de monnaie et les taux d’intérêt. Expansionniste, elle augmente "
  "l’offre de monnaie, abaisse le taux d’intérêt et déplace la courbe LM "
  "vers la droite, ce qui stimule l’investissement et le revenu ; "
  "restrictive, elle produit l’effet inverse. Son efficacité dépend de la "
  "configuration du modèle : nulle dans la trappe à liquidité, maximale "
  "dans la zone classique, et, en économie ouverte, suspendue au régime de "
  "change et à la mobilité des capitaux.",
  ["politiques monetaires"],
  "En changes fixes avec capitaux parfaitement mobiles, la politique "
  "monétaire perd toute efficacité ; en changes flexibles, elle devient "
  "particulièrement puissante."),

 ("Politique budgétaire expansionniste", ['25'],
  "Une politique budgétaire expansionniste stimule la demande globale",
  "Une politique budgétaire expansionniste soutient la demande globale par "
  "une hausse des dépenses publiques, une augmentation des prestations "
  "sociales ou une baisse des impôts, afin de stimuler la production et "
  "l’emploi lorsque l’économie fonctionne en dessous de ses capacités. Dans "
  "le modèle IS-LM, elle déplace la courbe IS vers la droite ; la hausse de "
  "l’activité accroît la demande de monnaie et, à offre de monnaie "
  "constante, élève le taux d’intérêt — d’où l’effet d’éviction qui en "
  "limite la portée.",
  ["relance budgetaire expansionniste"],
  "Son efficacité est maximale dans la trappe à liquidité, où le taux "
  "d’intérêt ne remonte pas, et nulle dans la zone classique."),

 ("Politique de relance", ['25', '1'],
  "Une politique de relance déplace IS vers la droite",
  "Une politique de relance est une politique conjoncturelle destinée à "
  "soutenir l’activité lorsque la croissance ralentit. Elle peut être "
  "budgétaire — hausse des dépenses, des prestations sociales, baisse des "
  "impôts — ou monétaire — baisse des taux d’intérêt, augmentation de "
  "l’offre de monnaie. Dans le modèle IS-LM, une relance budgétaire déplace "
  "IS vers la droite. Son efficacité dépend de la propension à consommer "
  "des bénéficiaires, de l’effet d’éviction, du degré d’ouverture de "
  "l’économie et, en économie ouverte, du régime de change.",
  ["relance"],
  "Relance et rigueur sont les deux orientations possibles d’une politique "
  "conjoncturelle ; l’une et l’autre doivent être contracycliques pour "
  "stabiliser l’activité."),

 ("Investissement", ['25', '1', '6'],
  "L’investissement dépend des anticipations et du taux d’intérêt",
  "L’investissement est l’acquisition de moyens de production destinés à "
  "durer. Dans l’analyse keynésienne, il dépend de deux éléments : les "
  "anticipations de demande, puisque les entreprises investissent "
  "lorsqu’elles prévoient des débouchés suffisants, et le taux d’intérêt, "
  "qui détermine le coût du financement et l’arbitrage entre placements. "
  "Il est favorisé lorsque l’efficacité marginale anticipée du capital "
  "dépasse le taux d’intérêt pertinent ; mais une baisse des taux peut "
  "rester sans effet si les anticipations des entreprises sont très "
  "pessimistes.",
  ["investissement des entreprises"],
  "Investir accroît le stock de capital ; placer acquiert un actif "
  "financier."),

 ("Équilibre partiel", ['25', '4', '3'],
  "Alfred Marshall : l’équilibre partiel et les défaillances du marché",
  "L’équilibre partiel consiste à étudier le fonctionnement d’un marché "
  "isolément, en supposant inchangé ce qui se passe sur les autres : c’est "
  "la démarche de Marshall, qui raisonne ceteris paribus. Elle permet "
  "d’isoler un mécanisme précis, mais se heurte à l’interdépendance réelle "
  "des marchés — critique dont l’équilibre général walrasien tire sa "
  "justification. Dans le modèle IS-LM, chaque courbe représente un "
  "ensemble d’équilibres partiels — celui du marché des biens pour IS, celui "
  "du marché de la monnaie pour LM — dont l’intersection seule assure un "
  "équilibre simultané.",
  ["equilibre partiel marshallien", "ceteris paribus"],
  "L’équilibre partiel isole un marché ; l’équilibre général les traite "
  "ensemble. Le modèle IS-LM articule deux équilibres partiels."),

 ("Ménages", ['25', '1'],
  "L’État intervient également sur le revenu disponible",
  "Les ménages constituent le secteur institutionnel dont la fonction "
  "principale est la consommation. Dans le modèle macroéconomique, leur "
  "comportement est résumé par la fonction de consommation : ils partagent "
  "leur revenu disponible entre consommation et épargne, selon la propension "
  "marginale à consommer. Avec l’introduction de l’État, ce revenu "
  "disponible n’est plus le seul revenu primaire : les prestations sociales "
  "l’augmentent, les prélèvements obligatoires le réduisent.",
  ["menage"],
  "Les ménages consomment et épargnent ; les entreprises produisent et "
  "investissent ; l’État redistribue et dépense."),
]


# Faux termes : la moisson a pris pour une notion un intitulé de lecture de
# graphique ou un fragment de phrase. Ils encombrent la rubrique sans rien
# définir.
REJET = [
 "lecture du graphique",
 "lecture du graphique de droite",
 "lecture du graphique de gauche",
 "lecture du tableau",
 "intersection is lm determine",
 "equilibre keynesien",
 "raisonnement",
 "renversement",
]


# Définitions existantes qui s'appliquent à l'un des deux derniers chapitres
# sans y renvoyer : on ajoute le renvoi vers le passage pertinent.
# (clé de l'entrée, chapitre, intitulé de la section visée)
RENVOIS = [
 ("exportation", '25', "Les exportations sont considérées comme autonomes dans le modèle simple"),
 ("importation", '25', "Les importations dépendent positivement du revenu national"),
 ("competitivite", '26', "Le taux de change réel mesure la compétitivité-prix relative"),
 ("competitivite hor prix", '26', "Spécialisation en compétitivité hors prix"),
 ("desindustrialisation", '26', "Le rôle de la désindustrialisation"),
 ("desinflation competitive", '25',
  "Le tournant de la rigueur de 1983 manifeste la priorité accordée à l’équilibre extérieur"),
 ("balance des paiement", '26', "Le rôle de la balance des paiements"),
 ("effet de bilan", '25', "Les dévaluations peuvent alimenter un cercle vicieux de la monnaie faible"),
 ("crise de change", '25', "Le système monétaire européen transforme le déficit extérieur en crise de change"),
]


# Formulations employées par les deux chapitres qui doivent conduire à une
# entrée existante plutôt qu'à une entrée nouvelle.
ALIAS = [
 ("equilibre de sou emploi", ["chomage keynesien", "equilibre de sous emploi durable"]),
 ("anticipation autorealisatrice", ["anticipation autorealisatrice sur le change"]),
 ("trappe liquidite", ["phase horizontale de lm", "preference absolue pour la liquidite"]),
 ("balance globale", ["equilibre de la balance globale"]),
 ("regime de change", ["regime de changes fixes", "regime de changes flexibles",
                       "changes fixes", "changes flexibles"]),
 ("reserve de change", ["reserves officielles de change"]),
 ("devaluation competitive", ["devaluation strategique"]),
 ("peur du flottement", ["fear of floating"]),
 ("desinflation competitive", ["politique du franc fort"]),
]
