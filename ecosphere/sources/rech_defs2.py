# -*- coding: utf-8 -*-
"""Définitions ajoutées après l'audit par familles — 1re partie.

Les familles examinées ici : les formes de capital, les coûts, les taux, la
concurrence, les marchés, les prix et les régimes d'économie. Chaque entrée
est rédigée à partir du passage du cours indiqué par son ancre, et distingue
la notion de ses voisines lorsque la confusion est possible.

Format : (terme, chapitres, ancre, définition, alias, distinction)
"""

DEFS = [

 # ----------------------------------------------------- les formes de capital
 ("Capital technologique", ['6', '8'], "Une substitution du capital au travail",
  "Le capital technologique désigne l’ensemble des équipements, logiciels et "
  "systèmes automatisés qui incorporent une technologie, et qui peuvent se "
  "substituer au travail humain lorsqu’ils deviennent plus rapides et moins "
  "coûteux que lui. Le cours mobilise la notion à propos de l’intelligence "
  "artificielle : les entreprises remplacent du travail humain par du capital "
  "technologique, ce qui déplace la frontière entre les tâches automatisables "
  "et celles qui ne le sont pas.",
  ["capital technique", "equipement technologique"],
  "Il se distingue du capital physique, qui désigne tout équipement productif "
  "durable, et du capital humain, qui désigne les compétences incorporées "
  "dans les personnes : le capital technologique est la part du capital "
  "physique qui porte l’innovation."),

 ("Capital social", ['1', '6', '8'], "Les différentes formes de capital",
  "Le capital social a deux sens, qu’il ne faut pas confondre. Au sens "
  "comptable, employé au chapitre 1, il désigne la part des fonds propres "
  "d’une entreprise apportée par les associés, inscrite au passif du bilan à "
  "côté des bénéfices mis en réserve. Au sens sociologique, employé au "
  "chapitre 8, il désigne l’ensemble des relations et des réseaux dont "
  "dispose un individu ou un collectif, et dont le cours fait l’une des "
  "conditions de la réussite entrepreneuriale à côté des compétences "
  "techniques.",
  ["fonds propres", "reseaux sociaux"],
  "Au sens comptable, à ne pas confondre avec le capital productif, qui "
  "désigne les équipements ; au sens sociologique, à ne pas confondre avec le "
  "capital humain, qui porte sur les compétences de la personne et non sur "
  "ses relations."),

 ("Capital fixe", ['1', '3', '6', '7', '23'], "Formation brute de capital fixe",
  "Le capital fixe est l’ensemble des biens durables de production — "
  "bâtiments, machines, matériels, actifs corporels — acquis par une unité "
  "productive et utilisés pendant plus d’un an dans le processus de "
  "production. Son achat constitue l’investissement, mesuré par la formation "
  "brute de capital fixe. Les physiocrates employaient déjà la notion sous le "
  "nom d’avances foncières pour désigner les investissements durables des "
  "propriétaires.",
  ["actifs corporels", "avances foncieres", "bien d equipement"],
  "À distinguer des consommations intermédiaires, qui sont détruites ou "
  "transformées dans le cycle de production, et du capital circulant, qui ne "
  "sert qu’une fois."),

 ("Capital variable", ['3'], "La plus-value provient du travail",
  "Dans l’analyse de Marx, le capital variable est la part du capital avancée "
  "en salaires, c’est-à-dire consacrée à l’achat de force de travail. Elle est "
  "dite variable parce qu’elle est la seule à créer de la valeur nouvelle : "
  "seul le travail humain produit de la plus-value. Le cours en tire la "
  "contradiction interne du capitalisme : en investissant de plus en plus "
  "dans les machines et relativement moins dans les salaires, les capitalistes "
  "réduisent la part qui alimente leur profit, d’où la baisse tendancielle du "
  "taux de profit.",
  ["capital constant"],
  "Son pendant est le capital constant, part avancée en machines et en "
  "matières premières, qui transmet sa valeur sans en créer."),

 ("Capital par tête", ['6'], "Le modèle de Solow",
  "Le capital par tête est le stock de capital rapporté au nombre de "
  "travailleurs. Son augmentation — l’intensité capitalistique — constitue un "
  "moteur classique des gains de productivité : chaque travailleur dispose de "
  "davantage d’équipement. Dans le modèle de Solow, c’est la variable "
  "centrale : plus le capital par tête est élevé, plus l’amortissement à "
  "compenser est important, jusqu’à l’état stationnaire où l’investissement "
  "ne sert plus qu’à remplacer le capital usé.",
  ["intensite capitalistique", "capital par travailleur", "k par tete"],
  "À distinguer de la productivité globale des facteurs, qui mesure "
  "l’efficacité d’ensemble et non la quantité de capital disponible par "
  "travailleur."),

 # ----------------------------------------------------------------- les coûts
 ("Coût de production", ['1', '3', '4', '6', '8', '9', '21', '22', '23'],
  "La compétitivité-prix",
  "Le coût de production est l’ensemble des dépenses engagées pour produire : "
  "salaires et cotisations, consommations intermédiaires, énergie, "
  "amortissement du capital, fiscalité et charges réglementaires. Le cours "
  "insiste sur sa composition lorsqu’il examine les accusations de dumping : "
  "taux de change, coût du travail, fiscalité et réglementation "
  "environnementale en sont autant de dimensions, et la difficulté consiste à "
  "savoir si un avantage de coût est entretenu volontairement ou s’il reflète "
  "un niveau de développement.",
  ["cout de revient"],
  "À ne pas confondre avec le prix de vente, qui ajoute la marge, ni avec le "
  "coût unitaire, qui rapporte le coût à la quantité produite."),

 ("Coût du travail", ['1', '6', '21', '22', '23'], "La compétitivité-coût",
  "Le coût du travail est ce que l’emploi d’un salarié coûte à l’employeur : "
  "le salaire brut augmenté des cotisations patronales, soit le salaire "
  "super-brut. Le cours met en garde contre sa lecture directe : les écarts "
  "de rémunération entre pays surestiment les différences réelles de coût de "
  "production, car une main-d’œuvre peu chère mais faiblement productive peut "
  "présenter un coût unitaire proche de celui d’une économie à hauts salaires "
  "et forte productivité.",
  ["salaire super brut", "charges patronales"],
  "Le bon indicateur de comparaison internationale n’est pas le coût horaire "
  "mais le coût salarial unitaire, qui rapporte le coût du travail à la "
  "productivité."),

 ("Coût salarial unitaire", ['22', '21'], "La compétitivité-coût",
  "Le coût salarial unitaire est le coût du travail rapporté à la "
  "productivité du travail. C’est, selon le cours, le coût pertinent pour "
  "comparer la compétitivité du travail entre pays : un salaire élevé peut "
  "être compatible avec un coût unitaire faible si la productivité est forte. "
  "Le cours relève ainsi que le coût salarial unitaire allemand a davantage "
  "progressé que le coût salarial unitaire français sur la période examinée.",
  ["csu", "cout unitaire du travail"],
  "À distinguer du coût horaire du travail, qui ignore ce que le travailleur "
  "produit pendant cette heure."),

 ("Coût marginal", ['3', '4', '5', '9', '22', '23'],
  "La maximisation du profit",
  "Le coût marginal est le supplément de coût total provoqué par la "
  "production d’une unité supplémentaire. Il commande la décision de "
  "produire : le producteur augmente sa production tant que le prix reste "
  "supérieur au coût marginal, et l’optimum est atteint lorsque le prix égale "
  "le coût marginal. Ricardo en fait aussi une loi de la rente : le prix "
  "agricole est déterminé par le coût marginal de la terre la moins fertile "
  "mise en culture, de sorte que les meilleures terres, dont le coût marginal "
  "est faible, dégagent une rente différentielle.",
  ["cm", "cout marginal de production"],
  "À distinguer du coût moyen, qui rapporte le coût total à la quantité, et "
  "du coût total, qui est leur cumul."),

 ("Coût total", ['1', '4', '8', '22', '23'], "La théorie du Producteur",
  "Le coût total est la somme de toutes les dépenses engagées pour un niveau "
  "de production donné : coûts fixes, indépendants de la quantité produite, et "
  "coûts variables, qui croissent avec elle. Le cours le représente par la "
  "droite d’isocoût, qui réunit toutes les combinaisons de capital et de "
  "travail ayant le même coût total, et dont la tangence avec une isoquante "
  "détermine la combinaison productive optimale.",
  ["isocout", "cout fixe", "cout variable"],
  "Le coût moyen en est la division par la quantité, le coût marginal la "
  "variation pour une unité de plus."),

 ("Coût social", ['5', '6', '7', '8', '22', '23'],
  "Arthur Pigou : l’économie du bien être",
  "Le coût social est le coût total supporté par la collectivité, qui ajoute "
  "au coût privé payé par le producteur les dommages qu’il impose aux autres "
  "sans contrepartie. Le cours l’emploie pour caractériser l’externalité "
  "négative : l’entreprise ne prenant pas en compte le coût social de la "
  "pollution, elle produit au-delà de l’optimum collectif, d’où la "
  "justification d’une taxe pigouvienne. Il désigne aussi, dans le chapitre 6, "
  "le coût humain d’une transition — emplois détruits, reconversions — qui "
  "conditionne son acceptabilité politique.",
  ["cout prive", "cout collectif"],
  "À distinguer du coût privé, qui est le seul coût que le marché fait payer "
  "au producteur : leur écart mesure l’externalité."),

 # ------------------------------------------------------------------ les taux
 ("Taux de change", ['2', '6', '7', '21', '22', '24'],
  "Le régime de change",
  "Le taux de change est le prix d’une monnaie exprimé dans une autre. Le "
  "cours distingue deux régimes selon la manière dont il se forme : en change "
  "fixe, il est fixé par l’État ou la banque centrale par rapport à une "
  "monnaie de référence ; en change flottant, la valeur de la monnaie varie "
  "librement selon l’offre et la demande sur le marché des changes, en "
  "fonction de la confiance, des taux d’intérêt et de la croissance. Une "
  "appréciation renchérit les exportations et abaisse le prix des "
  "importations, une dépréciation produit l’effet inverse.",
  ["change", "parite monetaire", "cours de la monnaie"],
  "À distinguer du taux de change réel, qui corrige le taux nominal des "
  "écarts d’inflation entre les deux pays, et de la parité de pouvoir "
  "d’achat, qui compare ce qu’un revenu permet d’acheter."),

 ("Taux d’intérêt", ['1', '2', '3', '5', '6', '7', '21', '22', '23'],
  "Les taux directeurs",
  "Le taux d’intérêt est le prix du temps et du risque : la rémunération "
  "exigée par le prêteur pour renoncer à la liquidité, et le coût supporté par "
  "l’emprunteur. Il commande le coût du crédit, donc l’investissement et la "
  "consommation financée à crédit ; la banque centrale agit sur lui par ses "
  "taux directeurs. Le cours en relativise toutefois le pouvoir : pour "
  "Keynes, l’investissement dépend d’abord des anticipations des "
  "entrepreneurs, de la confiance et des esprits animaux, et non du seul taux "
  "d’intérêt.",
  ["interet", "loyer de l argent"],
  "Le taux nominal est le taux affiché ; le taux réel en retranche "
  "l’inflation et mesure le coût véritable d’un emprunt."),

 ("Taux de croissance", ['2', '6', '7'],
  "Les trois taux de croissance : cœur analytique du modèle",
  "Le taux de croissance mesure la variation relative de la production — le "
  "plus souvent du produit intérieur brut en volume — d’une période à la "
  "suivante. Harrod en distingue trois, dont la non-coïncidence explique "
  "l’instabilité : le taux effectif, celui que l’économie réalise "
  "réellement ; le taux garanti, celui qui satisferait les entrepreneurs et "
  "validerait leurs anticipations ; le taux naturel, celui que permettent la "
  "population active et le progrès technique disponibles.",
  ["croissance effective", "taux garanti", "taux naturel"],
  "À ne pas confondre avec le niveau de production : un taux de croissance "
  "qui ralentit décrit une production qui augmente encore, mais moins vite."),

 ("Taux d’épargne", ['6', '21'], "Taux d’épargne trop élevé",
  "Le taux d’épargne est la part du revenu disponible qui n’est pas "
  "consommée. Le cours en fait une variable à double tranchant. Trop élevé, il "
  "rend la demande globale insuffisante : les entreprises ne vendent pas toute "
  "leur production. Trop faible, il laisse l’investissement insuffisant, "
  "l’accumulation du capital ralentit et les capacités productives "
  "n’augmentent pas assez. C’est l’une des sources de l’instabilité de la "
  "croissance.",
  ["propension a epargner", "epargne nationale"],
  "À distinguer du taux d’investissement, qui mesure l’usage productif de "
  "cette épargne : l’écart entre les deux se règle par le solde extérieur."),

 ("Taux d’investissement", ['1', '6', '21', '23'],
  "Rostow : le take-off nécessite un fort taux d’investissement",
  "Le taux d’investissement mesure la part de la richesse créée — par un pays, "
  "un secteur ou une entreprise — qui est consacrée à l’investissement, soit "
  "le rapport de la formation brute de capital fixe au produit intérieur brut "
  "ou à la valeur ajoutée. Rostow en fait la condition du décollage : le "
  "take-off suppose un taux d’investissement élevé, de l’ordre de 10 % du "
  "produit intérieur brut, qui engage l’accumulation et rend la croissance "
  "auto-entretenue.",
  ["fbcf sur pib", "effort d investissement"],
  "À distinguer du taux d’épargne, qui mesure le financement disponible et "
  "non son emploi effectif."),

 ("Taux de couverture", ['7', '21'], "Le taux de couverture",
  "Le taux de couverture rapporte les exportations aux importations d’un pays, "
  "d’un secteur ou d’un produit : il renseigne sur la capacité des "
  "exportations à financer les importations. Le cours met en garde contre une "
  "lecture mécanique : un taux inférieur à 1 ne signifie pas automatiquement "
  "une faiblesse, car il peut traduire un investissement en biens "
  "d’équipement importés ou une spécialisation assumée.",
  ["couverture des importations"],
  "À distinguer du taux d’ouverture, qui mesure le poids des échanges dans "
  "l’économie et non leur équilibre."),

 ("Taux de profit", ['3', '6', '21', '23'],
  "La baisse tendancielle du taux de profit",
  "Le taux de profit rapporte le profit au capital avancé : il mesure la "
  "rentabilité de l’accumulation. Chez Ricardo, il baisse à mesure que la mise "
  "en culture de terres moins fertiles élève le prix des subsistances et la "
  "rente foncière, ce qui comprime les profits des fermiers. Chez Marx, il "
  "baisse tendanciellement parce que l’accumulation augmente la part du "
  "capital constant relativement au capital variable, seule source de "
  "plus-value : pour le restaurer, les capitalistes cherchent des débouchés "
  "et des sources de profit extérieurs.",
  ["rentabilite du capital", "baisse tendancielle du taux de profit"],
  "À distinguer de la marge, qui rapporte le profit au chiffre d’affaires et "
  "non au capital engagé."),

 ("Taux de chômage", ['2', '3', '6', '7', '10'],
  "La courbe de Phillips",
  "Le taux de chômage rapporte le nombre de chômeurs à la population active, "
  "et non à la population totale. Le cours l’emploie d’abord dans la relation "
  "observée par Phillips en 1958 entre la croissance des salaires nominaux et "
  "le chômage au Royaume-Uni entre 1861 et 1957 — relation ni linéaire ni "
  "stable — puis dans la thèse monétariste selon laquelle il existe un taux de "
  "chômage naturel, que la politique économique ne peut pas réduire "
  "durablement.",
  ["chomage", "part de chomeurs"],
  "À distinguer du nombre de chômeurs, qui varie aussi avec la taille de la "
  "population active, et du taux d’emploi, qui rapporte les actifs occupés à "
  "la population en âge de travailler."),

 # ----------------------------------------------------------- la concurrence
 ("Concurrence internationale", ['6', '7', '10', '21', '22', '23', '24'],
  "Les effets de la mondialisation sur l’emploi",
  "La concurrence internationale est la pression exercée sur les producteurs "
  "d’un pays par les producteurs étrangers, sur le marché intérieur comme sur "
  "les marchés d’exportation. Le cours en souligne l’ambivalence avec "
  "Fontagné : le consommateur bénéficie de biens importés moins chers, tandis "
  "que certains travailleurs exposés peuvent perdre leur emploi ou subir une "
  "pression sur leur salaire. Elle pèse aussi sur les politiques publiques, en "
  "nourrissant la crainte des délocalisations vers les pays moins régulés.",
  ["pression concurrentielle exterieure"],
  "À distinguer de la concurrence déloyale, qui suppose un avantage "
  "artificiellement entretenu et non une simple différence de compétitivité."),

 ("Concurrence déloyale", ['8', '9', '21', '22', '23', '24'],
  "L’argument de la concurrence déloyale",
  "La concurrence déloyale désigne une concurrence dont un État estime "
  "qu’elle repose sur des avantages artificiels : dumping, subventions, prêts "
  "bonifiés, réglementations différentes ou autres soutiens publics. Elle "
  "autorise alors des mesures correctrices — droits antidumping ou "
  "compensateurs — destinées à rééquilibrer les conditions de concurrence. Le "
  "cours souligne la difficulté : toute différence de coût n’est pas une "
  "distorsion, et compenser systématiquement un coût du travail plus faible "
  "reviendrait à nier le principe même des avantages comparatifs. Il faut donc "
  "démontrer que le concurrent a volontairement bénéficié d’une distorsion.",
  ["dumping deloyal", "distorsion de concurrence"],
  "À ne pas confondre avec un avantage comparatif légitime, qui résulte du "
  "niveau de développement ou des dotations, ni avec un déficit bilatéral, "
  "qui ne démontre à lui seul aucune déloyauté."),

 # -------------------------------------------------------------- les marchés
 ("Marché intérieur", ['7', '9', '21', '22', '23'],
  "Contourner l’étroitesse du marché intérieur",
  "Le marché intérieur est l’ensemble de la demande adressée aux producteurs "
  "sur le territoire national, résidents compris. Sa taille commande des "
  "stratégies entières : pour les firmes issues de petits marchés nationaux, "
  "l’internationalisation permet, selon le cours, de dépasser l’étroitesse de "
  "la demande intérieure et d’accéder à des débouchés plus vastes. Son degré "
  "d’exposition aux importations se mesure par le taux de pénétration.",
  ["marche domestique", "marche national"],
  "À distinguer du marché mondial, qui agrège la demande de tous les pays, et "
  "du marché commun, qui est une forme d’intégration régionale."),

 ("Marché interbancaire", ['2'], "Le refinancement des banques",
  "Le marché interbancaire est le marché sur lequel les banques se prêtent "
  "entre elles des liquidités à court terme. Une banque qui a besoin de "
  "monnaie centrale l’obtient soit auprès d’autres banques sur ce marché, soit "
  "auprès de la banque centrale par le refinancement. Le cours relève que les "
  "banques commerciales peuvent y offrir des taux supérieurs au taux de la "
  "banque centrale pour attirer les liquidités des autres banques.",
  ["refinancement interbancaire", "marche monetaire"],
  "À distinguer du marché des capitaux, où les agents non financiers "
  "émettent et échangent des titres à plus long terme."),

 ("Marché des capitaux", ['2', '4', '6'],
  "Comment le marché des capitaux a-t-il évolué ?",
  "Le marché des capitaux est le lieu d’émission et d’échange des titres par "
  "lesquels les agents se financent directement : actions, obligations, titres "
  "de créances négociables. Le cours souligne que le passage à une économie de "
  "marchés financiers ne signifie pas seulement que les agents y recourent "
  "davantage, mais que ces marchés se sont eux-mêmes transformés depuis les "
  "années 1980 sous l’effet de la globalisation financière et de la règle des "
  "trois D.",
  ["marche financier", "financement direct"],
  "À distinguer du marché interbancaire, réservé aux banques et aux "
  "liquidités de court terme."),

 # ----------------------------------------------------------------- les prix
 ("Prix d’équilibre", ['3', '4', '5', '6', '23'], "L’équilibre du marché",
  "Le prix d’équilibre est le prix auquel l’offre et la demande se "
  "rencontrent, de sorte qu’aucune quantité offerte ne reste invendue et "
  "aucune demande solvable insatisfaite. Le cours décrit le tâtonnement par "
  "lequel le marché y tend, et s’en sert pour comparer deux économies avant "
  "ouverture : dans l’exemple des boutons, les rendements croissants rendent "
  "les coûts moyens décroissants et le prix d’équilibre chinois est déjà "
  "inférieur au prix européen, ce qui confère à la Chine un avantage initial.",
  ["equilibre de marche", "prix de marche"],
  "À distinguer du prix international, qui s’établit entre pays après "
  "ouverture, et du prix administré, fixé par la puissance publique."),

 ("Prix international", ['23'],
  "John Stuart Mill : les prix internationaux doivent rester entre les bornes",
  "Le prix international est le prix relatif auquel deux biens s’échangent "
  "entre pays après ouverture. Mill montre qu’il commande la répartition du "
  "gain à l’échange : l’échange n’est mutuellement avantageux que si ce prix "
  "reste compris entre les coûts d’opportunité internes des deux partenaires, "
  "et plus il est proche de la borne favorable à un pays, plus la part du gain "
  "que ce pays capte est importante. Un prix situé hors de ces bornes conduit "
  "rationnellement un pays à refuser l’échange.",
  ["prix relatif international", "termes de l echange"],
  "À distinguer des termes de l’échange, qui mesurent l’évolution du rapport "
  "entre prix des exportations et prix des importations d’un pays."),

 ("Prix du carbone", ['7', '22', '23', '24'],
  "Le marché carbone européen et le MACF",
  "Le prix du carbone est le coût donné à l’émission d’une tonne de dioxyde de "
  "carbone, soit par une taxe, soit par un marché de quotas d’émission. Il "
  "vise à internaliser l’externalité climatique en rendant les émissions "
  "coûteuses pour celui qui les produit. Le cours en tire la justification du "
  "mécanisme d’ajustement carbone aux frontières : soutenir les producteurs "
  "européens ne suffit pas s’ils supportent un prix du carbone que leurs "
  "concurrents étrangers ne paient pas.",
  ["taxe carbone", "quota d emission", "prix du co2"],
  "À distinguer du coût de la transition, qui englobe l’ensemble des dépenses "
  "d’adaptation, et de la valeur tutélaire du carbone, qui est une référence "
  "pour l’évaluation publique."),

 # ------------------------------------------------- les régimes d'économie
 ("Économie ouverte", ['1', '2', '6', '21', '23'],
  "L’équilibre emplois-ressources en économie ouverte",
  "Une économie ouverte est une économie qui échange avec le reste du monde : "
  "ses ressources sont la production nationale augmentée des importations, et "
  "ses emplois la demande intérieure augmentée des exportations. L’ouverture "
  "modifie les mécanismes macroéconomiques : une partie de la demande "
  "supplémentaire fuit vers les importations, ce qui réduit le multiplicateur, "
  "et la politique monétaire y influence aussi la valeur externe de la "
  "monnaie.",
  ["ouverture de l economie"],
  "À distinguer de l’économie fermée, où toute la demande porte sur la "
  "production nationale : le multiplicateur keynésien y vaut 5 contre 2,5 en "
  "économie ouverte dans l’exemple du cours."),

 ("Économie fermée", ['1', '6'],
  "Le multiplicateur en économie fermée",
  "Une économie fermée est une économie sans échanges extérieurs : il n’y a ni "
  "importations ni exportations, et toute la demande porte sur la production "
  "nationale. L’hypothèse sert de point de départ au raisonnement "
  "macroéconomique : le multiplicateur keynésien y atteint sa valeur maximale, "
  "5 dans l’exemple du cours avec une propension à consommer de 0,8, contre "
  "2,5 lorsqu’on réintroduit les importations.",
  ["autarcie", "economie autarcique"],
  "C’est une hypothèse d’analyse plus qu’une situation réelle ; l’autarcie "
  "désigne, elle, une fermeture voulue par une politique."),

 ("Économie duale", ['7', '22'],
  "Les FMN peuvent favoriser la sortie de l’économie duale",
  "Une économie duale est une économie partagée entre un secteur traditionnel "
  "à faible productivité, qui emploie l’essentiel de la population active, et "
  "un secteur moderne beaucoup plus productif mais trop petit pour absorber "
  "cette main-d’œuvre. Chez Lewis, ce dualisme est un obstacle réel mais "
  "passager : le transfert de travailleurs du premier vers le second élève la "
  "productivité moyenne. Le cours relève que les firmes multinationales "
  "peuvent accélérer cette sortie en élargissant le secteur moderne.",
  ["dualisme economique", "secteur traditionnel", "secteur moderne"],
  "À distinguer de l’économie informelle, qui désigne les activités échappant "
  "à l’enregistrement, et de la segmentation du marché du travail, qui porte "
  "sur les statuts d’emploi."),
]
