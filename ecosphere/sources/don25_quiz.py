# -*- coding: utf-8 -*-
"""Quiz du chapitre 5 de deuxième année : connaissances et raisonnement.

Chaque entrée : (type, question, options, index de la bonne réponse,
explication, tags thématiques).
"""

Q = []


def q(t, question, opts, ans, exp, tags):
    Q.append((t, question, opts, ans, exp, tags))


# ================================================================ QCM
q('qcm', "Dans le modèle keynésien simple, le revenu national d’équilibre s’écrit :",
  ["Yₑ = (C₀ + I₀) × (1 − c)", "Yₑ = (C₀ + I₀) / (1 − c)",
   "Yₑ = C₀ + I₀ + c", "Yₑ = (C₀ + I₀) / c"], 1,
  "Bonne réponse : B. De Y = C₀ + cY + I₀ on tire Y(1 − c) = C₀ + I₀, donc Yₑ = (C₀ + I₀) / (1 − c). Le dénominateur (1 − c) est la propension marginale à épargner : plus elle est faible, plus le revenu d’équilibre est élevé.",
  ['diagramme à 45°', 'revenu d’équilibre'])
q('qcm', "La courbe IS représente :",
  ["L’équilibre du marché de la monnaie", "L’équilibre du marché des biens et services",
   "L’équilibre extérieur", "L’équilibre du marché du travail"], 1,
  "Bonne réponse : B. IS signifie Investment-Saving : la courbe rassemble les couples (Y, r) pour lesquels l’investissement est égal à l’épargne, c’est-à-dire pour lesquels le marché des biens et services est à l’équilibre.",
  ['courbe IS', 'IS-LM'])
q('qcm', "La courbe LM est croissante parce que :",
  ["Une hausse du revenu accroît la demande de monnaie, ce qui élève le taux d’intérêt à offre constante",
   "Une hausse du taux d’intérêt accroît l’investissement",
   "Une hausse des prix réduit l’offre réelle de monnaie",
   "Une hausse de l’épargne finance l’investissement"], 0,
  "Bonne réponse : A. Lorsque le revenu augmente, les transactions se multiplient et la demande de monnaie augmente ; à offre de monnaie inchangée, les agents vendent des titres, le prix des obligations baisse et le taux d’intérêt monte.",
  ['courbe LM', 'demande de monnaie'])
q('qcm', "Le multiplicateur de dépenses publiques vaut, avec c = 0,8 :",
  ["4", "5", "0,8", "− 4"], 1,
  "Bonne réponse : B. kG = 1 / (1 − c) = 1 / 0,2 = 5. Une dépense publique de 100 produit donc 500 de revenu national supplémentaire dans le modèle simple.",
  ['multiplicateur', 'politique budgétaire'])
q('qcm', "Le multiplicateur des prestations sociales est inférieur à celui des dépenses publiques parce que :",
  ["Les prestations sociales sont moins importantes en montant",
   "Les ménages épargnent une partie du transfert avant la première vague de demande",
   "Les prestations sociales sont financées par l’impôt",
   "Les prestations sociales n’entrent pas dans la demande globale"], 1,
  "Bonne réponse : B. Une dépense publique de 100 crée immédiatement 100 de demande ; une prestation de 100 augmente d’abord le revenu disponible, dont 80 seulement sont consommés avec c = 0,8. D’où kF = c / (1 − c) = 4 contre kG = 5.",
  ['multiplicateur', 'prestations sociales'])
q('qcm', "Le multiplicateur fiscal est négatif : cela signifie que",
  ["Une baisse d’impôts réduit le revenu national",
   "Une hausse d’impôts réduit le revenu national",
   "Les impôts n’ont aucun effet sur le revenu",
   "Le revenu national devient négatif"], 1,
  "Bonne réponse : B. kT = − c / (1 − c). Le signe traduit le sens de la relation : une hausse des impôts réduit le revenu disponible et la consommation, donc le revenu national ; une baisse l’augmente. Une baisse d’impôts de 100 produit + 400 avec c = 0,8.",
  ['multiplicateur fiscal', 'politique budgétaire'])
q('qcm', "En économie ouverte, le multiplicateur des dépenses autonomes devient :",
  ["1 / (1 − c)", "1 / (1 − c + m)", "c / (1 − c + m)", "1 / (1 + c − m)"], 1,
  "Bonne réponse : B. La propension marginale à importer m apparaît au dénominateur : plus l’économie importe, plus le multiplicateur national est faible. Dans l’exemple du cours, il passe de 5 à 2.",
  ['multiplicateur', 'économie ouverte'])
q('qcm', "La propension marginale à importer se définit comme :",
  ["Le rapport des importations au PIB", "La variation des importations rapportée à la variation du revenu",
   "La part des importations dans la consommation", "Le taux de couverture des importations"], 1,
  "Bonne réponse : B. m = ΔM / ΔY. Le cours insiste sur la confusion fréquente avec le ratio importations / PIB, qui mesure un poids et non une variation.",
  ['propension à importer', 'économie ouverte'])
q('qcm', "La demande effective désigne chez Keynes :",
  ["La demande solvable des ménages", "La demande anticipée par les entrepreneurs",
   "La demande réalisée ex post", "La demande publique"], 1,
  "Bonne réponse : B. C’est la demande que les entrepreneurs anticipent qui détermine leurs décisions de production et d’emploi : si elle est insuffisante, la production l’est aussi, et le chômage devient involontaire.",
  ['demande effective', 'Keynes'])
q('qcm', "Les trois motifs de détention de monnaie chez Keynes sont :",
  ["Transaction, précaution, spéculation", "Transaction, épargne, investissement",
   "Précaution, thésaurisation, placement", "Liquidité, rendement, sécurité"], 0,
  "Bonne réponse : A. Les motifs de transaction et de précaution dépendent positivement du revenu, le motif de spéculation dépend négativement du taux d’intérêt.",
  ['demande de monnaie', 'préférence pour la liquidité'])
q('qcm', "Lorsque le taux d’intérêt du marché augmente, le prix des obligations existantes :",
  ["Augmente", "Diminue", "Reste stable", "Varie dans le même sens que le coupon"], 1,
  "Bonne réponse : B. C’est l’effet balançoire : si les nouvelles obligations offrent un meilleur rendement, les anciennes ne peuvent être vendues qu’à un prix plus faible. Il faut distinguer le coupon, fixe, le prix de marché, variable, et le rendement de marché.",
  ['effet balançoire', 'obligations'])
q('qcm', "Dans une trappe à liquidité :",
  ["La politique monétaire conventionnelle devient peu efficace et la politique budgétaire particulièrement efficace",
   "La politique monétaire devient très efficace", "L’effet d’éviction devient total",
   "La courbe LM devient verticale"], 0,
  "Bonne réponse : A. LM est horizontale : toute monnaie supplémentaire est thésaurisée, le taux d’intérêt ne baisse plus, mais une relance budgétaire déplace IS sans provoquer de hausse des taux, donc sans effet d’éviction.",
  ['trappe à liquidité', 'politique budgétaire'])
q('qcm', "Dans la zone classique :",
  ["LM est horizontale et la politique budgétaire est efficace",
   "LM est verticale et l’effet d’éviction est total",
   "BP est horizontale", "IS devient verticale"], 1,
  "Bonne réponse : B. Lorsque le taux d’intérêt est très élevé, la demande spéculative devient négligeable : LM est verticale, le revenu compatible avec l’équilibre monétaire est fixé, et une relance budgétaire n’élève que le taux d’intérêt.",
  ['zone classique', 'effet d’éviction'])
q('qcm', "L’effet d’éviction désigne :",
  ["La substitution des importations à la production nationale",
   "La réduction de l’investissement privé provoquée par la hausse du taux d’intérêt liée à la relance",
   "L’éviction des ménages modestes du marché du crédit",
   "Le remplacement de la monnaie nationale par une devise"], 1,
  "Bonne réponse : B. Dépenses publiques ↑ → revenu ↑ → demande de monnaie ↑ → taux d’intérêt ↑ → investissement privé ↓. L’augmentation de la demande publique est partiellement compensée par la baisse de la demande privée.",
  ['effet d’éviction', 'critiques'])
q('qcm', "Selon l’hypothèse du revenu permanent de Friedman (1957) :",
  ["La consommation dépend du revenu courant",
   "La consommation dépend du revenu moyen de long terme anticipé",
   "L’épargne dépend du taux d’intérêt",
   "Le revenu permanent est le revenu du travail"], 1,
  "Bonne réponse : B. Un transfert perçu comme temporaire ne modifie guère le revenu permanent anticipé : il peut donc être principalement épargné, ce qui affaiblit l’effet multiplicateur attendu des relances par transferts.",
  ['revenu permanent', 'Friedman'])
q('qcm', "L’équivalence ricardienne de Barro (1974) soutient que :",
  ["Les ménages épargnent une baisse d’impôts financée par la dette en anticipant les impôts futurs",
   "La dette publique n’a aucun coût",
   "Les impôts doivent être proportionnels",
   "Ricardo et Barro ont la même analyse de la rente"], 0,
  "Bonne réponse : A. L’augmentation de l’épargne privée compense la désépargne publique et la demande globale n’est pas stimulée. Le mécanisme suppose des agents informés, capables d’épargner et raisonnant sur un horizon long.",
  ['équivalence ricardienne', 'Barro'])
q('qcm', "Le taux de chômage naturel chez Friedman :",
  ["Est nul par définition", "Peut être durablement abaissé par la politique monétaire",
   "Dépend des caractéristiques structurelles du marché du travail",
   "Correspond au chômage frictionnel uniquement"], 2,
  "Bonne réponse : C. Il dépend des frictions, de l’adéquation entre qualifications et emplois, des institutions et de la formation des salaires. Il n’est pas immuable, mais une relance de la demande ne peut pas l’abaisser durablement.",
  ['chômage naturel', 'Friedman'])
q('qcm', "Dans la critique monétariste, une relance budgétaire au plein emploi :",
  ["Augmente durablement la production", "Provoque des tensions inflationnistes qui déplacent LM vers la gauche",
   "Déplace BP vers la droite", "Réduit le taux d’intérêt"], 1,
  "Bonne réponse : B. La hausse des prix réduit l’offre réelle de monnaie, LM se déplace vers la gauche, le taux d’intérêt augmente et évince l’investissement privé : l’économie revient à son niveau potentiel avec un taux d’intérêt plus élevé.",
  ['critique monétariste', 'offre réelle de monnaie'])
q('qcm', "La courbe de Phillips (1958) relie originellement :",
  ["Inflation et chômage", "Chômage et variation des salaires nominaux",
   "Production et chômage", "Monnaie et prix"], 1,
  "Bonne réponse : B. Le cours insiste sur ce point : Phillips établit une relation entre chômage et progression des salaires nominaux au Royaume-Uni. C’est Lipsey, puis Samuelson et Solow en 1960, qui la reformulent en termes d’arbitrage inflation-chômage.",
  ['courbe de Phillips', 'salaires'])
q('qcm', "La loi d’Okun (1962) établit une relation entre :",
  ["Inflation et chômage", "Production et chômage",
   "Monnaie et taux d’intérêt", "Épargne et investissement"], 1,
  "Bonne réponse : B. Lorsqu’une économie produit moins que son potentiel, le chômage tend à être plus élevé ; une augmentation suffisamment forte de l’activité tend à le réduire.",
  ['loi d’Okun', 'output gap'])
q('qcm', "Un écart de production (output gap) négatif signale :",
  ["Une surchauffe", "Une sous-utilisation des ressources et un chômage plus élevé",
   "Un excédent extérieur", "Une inflation importée"], 1,
  "Bonne réponse : B. L’output gap négatif révèle que la production effective est inférieure au potentiel ; un output gap positif signale au contraire des tensions susceptibles d’alimenter l’inflation.",
  ['output gap', 'conjoncture'])
q('qcm', "Dans le modèle OG-DG, un choc d’offre négatif :",
  ["Augmente la production et les prix", "Réduit la production et augmente les prix",
   "Réduit la production et les prix", "Est sans effet sur les prix"], 1,
  "Bonne réponse : B. La courbe d’offre globale de court terme se déplace vers la gauche : le niveau général des prix augmente tandis que la production diminue. C’est la configuration stagflationniste des chocs pétroliers.",
  ['OG-DG', 'choc d’offre'])
q('qcm', "Le modèle IS-LM traditionnel suppose :",
  ["Des prix flexibles", "Un niveau général des prix fixe",
   "Une économie ouverte", "Une offre de monnaie endogène"], 1,
  "Bonne réponse : B. Les trois hypothèses sont : la monnaie est active, le raisonnement est de court terme, le niveau général des prix est fixe. C’est cette dernière qui empêche IS-LM d’expliquer l’inflation et justifie le recours au modèle OG-DG.",
  ['IS-LM', 'hypothèses'])
q('qcm', "La courbe BP du modèle Mundell-Fleming représente :",
  ["L’équilibre du marché du travail", "L’équilibre de la balance globale",
   "L’équilibre budgétaire", "L’équilibre des transactions courantes uniquement"], 1,
  "Bonne réponse : B. BP rassemble les couples (Y, r) compatibles avec l’équilibre de la balance globale, c’est-à-dire la somme du solde courant et des mouvements autonomes de capitaux — et non le seul solde courant.",
  ['courbe BP', 'balance globale'])
q('qcm', "La courbe BP est croissante parce que :",
  ["Une hausse du revenu accroît les importations et exige des entrées de capitaux, donc un taux plus élevé",
   "Une hausse du taux d’intérêt réduit les importations",
   "Une hausse des prix améliore la compétitivité",
   "Les exportations dépendent du taux d’intérêt"], 0,
  "Bonne réponse : A. Y ↑ → M ↑ → solde courant ↓ → besoin de financement → il faut attirer des capitaux, donc r ↑. D’où la pente positive.",
  ['courbe BP', 'mobilité des capitaux'])
q('qcm', "Avec une mobilité parfaite des capitaux, la courbe BP est :",
  ["Verticale", "Horizontale", "Décroissante", "Confondue avec LM"], 1,
  "Bonne réponse : B. La moindre différence de rendement provoque des mouvements financiers considérables : le taux domestique s’aligne sur le taux mondial, r = r*, et BP devient parfaitement horizontale.",
  ['mobilité des capitaux', 'courbe BP'])
q('qcm', "En changes fixes avec mobilité parfaite des capitaux, une politique monétaire expansionniste :",
  ["Est très efficace", "Est inefficace car la défense de la parité annule l’expansion initiale",
   "Déplace BP vers la droite", "Provoque une appréciation"], 1,
  "Bonne réponse : B. LM droite → r < r* → sorties de capitaux → pression à la dépréciation → la banque centrale achète sa monnaie → masse monétaire ↓ → LM revient à sa position initiale.",
  ['Mundell-Fleming', 'changes fixes'])
q('qcm', "En changes fixes avec mobilité parfaite des capitaux, une relance budgétaire :",
  ["Est inefficace", "Est très efficace car elle est amplifiée par l’accompagnement monétaire",
   "Provoque une dépréciation", "Déplace LM vers la gauche"], 1,
  "Bonne réponse : B. IS droite → r > r* → entrées de capitaux → pression à l’appréciation → la banque centrale achète des devises et émet de la monnaie → LM droite → Y augmente fortement.",
  ['Mundell-Fleming', 'changes fixes'])
q('qcm', "En changes flexibles avec mobilité parfaite des capitaux, la politique budgétaire :",
  ["Est très efficace", "Est neutralisée par l’appréciation de la monnaie",
   "Déplace LM vers la droite", "Provoque une dépréciation"], 1,
  "Bonne réponse : B. IS droite → r ↑ → entrées de capitaux → appréciation → exportations nettes ↓ → IS revient vers la gauche. C’est l’effet d’éviction par le taux de change.",
  ['Mundell-Fleming', 'changes flexibles'])
q('qcm', "En changes flexibles avec mobilité parfaite des capitaux, la politique monétaire :",
  ["Est inefficace", "Est très efficace car la dépréciation stimule les exportations nettes",
   "N’a d’effet que sur les prix", "Déplace BP vers le haut"], 1,
  "Bonne réponse : B. LM droite → r ↓ → sorties de capitaux → dépréciation → exportations nettes ↑ → IS droite. La politique agit par deux canaux : le taux d’intérêt puis le taux de change.",
  ['Mundell-Fleming', 'changes flexibles'])
q('qcm', "Le triangle des incompatibilités de Mundell affirme qu’un État ne peut pas simultanément :",
  ["Maîtriser l’inflation, le chômage et la dette",
   "Maintenir des changes fixes, autoriser la libre circulation des capitaux et conduire une politique monétaire autonome",
   "Exporter, importer et investir", "Taxer, dépenser et emprunter"], 1,
  "Bonne réponse : B. C’est la trinité impossible : deux objectifs au maximum peuvent être pleinement conciliés, le troisième devant être abandonné.",
  ['triangle de Mundell', 'autonomie monétaire'])
q('qcm', "Dans le système de Bretton Woods, la combinaison retenue est :",
  ["Changes fixes + mobilité des capitaux", "Changes flexibles + autonomie monétaire",
   "Changes fixes + autonomie monétaire relative grâce au contrôle des capitaux",
   "Union monétaire + mobilité des capitaux"], 2,
  "Bonne réponse : C. Les contrôles de capitaux permettaient de concilier la stabilité des parités et une certaine autonomie monétaire nationale : c’est le troisième sommet du triangle qui est sacrifié.",
  ['Bretton Woods', 'triangle de Mundell'])
q('qcm', "La règle d’affectation de Mundell consiste à :",
  ["Affecter la politique budgétaire à l’équilibre externe et la monétaire à l’interne",
   "Affecter la politique budgétaire à l’équilibre interne et la monétaire à l’externe",
   "Utiliser les deux instruments dans le même sens",
   "Confier les deux instruments à la banque centrale"], 1,
  "Bonne réponse : B. Chaque instrument est affecté à l’objectif pour lequel il possède l’efficacité relative la plus grande : le budget agit directement sur la demande, la monnaie sur les mouvements de capitaux par les taux d’intérêt.",
  ['règle de Mundell', 'policy mix'])
q('qcm', "Les deux configurations qui constituent de véritables dilemmes de politique économique sont :",
  ["Sous-emploi + excédent et inflation + déficit",
   "Sous-emploi + déficit et inflation + excédent",
   "Sous-emploi + déficit et inflation + déficit",
   "Inflation + excédent et inflation + déficit"], 1,
  "Bonne réponse : B. Dans ces deux cas, la politique qui corrige le déséquilibre interne aggrave le déséquilibre externe. Dans les deux autres, une même orientation améliore les deux équilibres.",
  ['dilemmes', 'contrainte extérieure'])
q('qcm', "Les trois D de la globalisation financière, selon Henri Bourguinat, sont :",
  ["Dérégulation, délocalisation, désindustrialisation",
   "Déréglementation, décloisonnement, désintermédiation",
   "Dévaluation, désinflation, déflation",
   "Dette, déficit, dépense"], 1,
  "Bonne réponse : B. Déréglementation des opérations financières, décloisonnement des marchés auparavant séparés, désintermédiation au profit des financements directs : ces transformations rendent BP plus horizontale.",
  ['globalisation financière', 'Bourguinat'])
q('qcm', "Le tournant de la rigueur date de :",
  ["Mai 1981", "Juin 1982", "Mars 1983", "Janvier 1986"], 2,
  "Bonne réponse : C. En mars 1983, le gouvernement choisit de maintenir le franc dans le Système monétaire européen, ce qui implique l’abandon de la stratégie de relance et le passage à une politique plus restrictive.",
  ['tournant de la rigueur', 'contrainte extérieure'])
q('qcm', "La relance française de 1981 échoue principalement parce que :",
  ["La propension à consommer était trop faible",
   "Une partie de la demande supplémentaire s’est portée sur des importations, dans un environnement international peu porteur",
   "Les taux d’intérêt étaient trop bas",
   "Les dépenses publiques n’ont pas augmenté"], 1,
  "Bonne réponse : B. La relance intervient alors que la croissance des partenaires est faible et l’inflation française déjà élevée : une partie du multiplicateur profite aux producteurs étrangers et les comptes extérieurs se dégradent.",
  ['relance de 1981', 'économie ouverte'])
q('qcm', "Le modèle IS-LM a été réhabilité après 2008 parce qu’il permet d’analyser :",
  ["L’inflation importée", "La trappe à liquidité et les limites de la politique monétaire conventionnelle",
   "Les chaînes de valeur mondiales", "La croissance endogène"], 1,
  "Bonne réponse : B. Lorsque les taux approchent leur plancher, l’expansion monétaire conventionnelle perd de son efficacité tandis que l’effet d’éviction d’une relance budgétaire devient très limité.",
  ['trappe à liquidité', 'crise de 2008'])
q('qcm', "Le diagramme à 45° est associé à :",
  ["John Hicks", "Paul Samuelson", "Alvin Hansen", "Arthur Okun"], 1,
  "Bonne réponse : B. Samuelson le présente dans son manuel Economics, notamment dans l’édition de 1949 : la bissectrice rassemble les points où le revenu est égal à la demande globale.",
  ['Samuelson', 'diagramme à 45°'])
q('qcm', "Le modèle IS-LM a été formalisé en 1937 par :",
  ["Alvin Hansen", "John Hicks", "Robert Mundell", "Richard Kahn"], 1,
  "Bonne réponse : B. Hicks publie dans Econometrica « Mr. Keynes and the “Classics”: A Suggested Interpretation ». Hansen le prolonge en 1941 dans Fiscal Policy and Business Cycles.",
  ['Hicks', 'IS-LM'])
q('qcm', "Le principe du multiplicateur a été développé en 1931 par :",
  ["Keynes", "Richard Kahn", "Alvin Hansen", "Paul Samuelson"], 1,
  "Bonne réponse : B. Kahn développe le multiplicateur d’emploi en 1931 ; Keynes le reprend et le généralise dans la Théorie générale en 1936.",
  ['Kahn', 'multiplicateur'])
q('qcm', "Dans la fonction de consommation C = C₀ + cY, le terme C₀ désigne :",
  ["La consommation incompressible", "La consommation autonome",
   "La consommation publique", "La consommation des ménages modestes"], 1,
  "Bonne réponse : B. Le cours met explicitement en garde : la consommation autonome est celle qui ne dépend pas du revenu courant dans le modèle, ce qui n’en fait pas un minimum physiologique ou incompressible.",
  ['consommation autonome', 'piège'])
q('qcm', "L’égalité I = S en économie fermée sans État s’obtient en rapprochant :",
  ["Y = C + I et Y = C + S", "Y = C + I + G et Y = C + S + T",
   "PIB + M = C + I + G + X", "M = L"], 0,
  "Bonne réponse : A. L’approche par la demande donne Y = C + I, l’approche par l’utilisation du revenu Y = C + S ; en rapprochant les deux, C + I = C + S, donc I = S.",
  ['épargne', 'investissement'])
q('qcm', "L’équilibre emplois-ressources en économie ouverte s’écrit :",
  ["PIB = C + I + G", "PIB + M = C + I + G + X",
   "PIB = C + S", "PIB + X = C + I + G + M"], 1,
  "Bonne réponse : B. Les ressources — production intérieure et importations — correspondent aux emplois : consommation, investissement, dépenses publiques et exportations. En réorganisant : PIB = C + I + G + X − M.",
  ['emplois-ressources', 'comptabilité nationale'])
q('qcm', "Les trois approches du PIB sont :",
  ["Production, demande, revenus", "Production, emploi, prix",
   "Offre, demande, monnaie", "Valeur, volume, prix"], 0,
  "Bonne réponse : A. L’approche par la production mesure la création de richesse, celle par la demande les emplois de la production, celle par les revenus la répartition primaire. Les trois conduisent au même PIB aux ajustements statistiques près.",
  ['PIB', 'comptabilité nationale'])
q('qcm', "L’optimum de Pareto garantit :",
  ["Une répartition équitable des richesses",
   "Qu’on ne peut améliorer la situation d’un agent sans détériorer celle d’un autre",
   "Le plein emploi", "L’absence d’externalités"], 1,
  "Bonne réponse : B. Le cours ajoute une mise en garde explicite : l’optimalité au sens de Pareto ne dit rien de l’équité de la répartition, et une intervention publique peut corriger des défaillances de marché sans perte de bien-être.",
  ['Pareto', 'optimum'])
q('qcm', "Le tâtonnement walrasien décrit :",
  ["La négociation entre syndicats et patronat",
   "Le processus par lequel le commissaire-priseur annonce des prix jusqu’à l’équilibre",
   "L’ajustement par les quantités", "La formation des anticipations"], 1,
  "Bonne réponse : B. Le commissaire-priseur centralise offres et demandes, constate les déséquilibres, annonce de nouveaux prix et poursuit jusqu’à l’équilibre général.",
  ['Walras', 'équilibre général'])
q('qcm', "Pour Pigou, le chômage s’explique principalement par :",
  ["Une insuffisance de la demande globale", "Un salaire réel supérieur au niveau d’équilibre",
   "Un progrès technique trop rapide", "Une inflation trop faible"], 1,
  "Bonne réponse : B. Dans l’analyse néoclassique développée notamment dans The Theory of Unemployment (1933), l’excès d’offre de travail résulte d’un salaire réel trop élevé, que la flexibilité salariale devrait résorber.",
  ['Pigou', 'chômage néoclassique'])
q('qcm', "L’idéal-type est une notion empruntée à :",
  ["Émile Durkheim", "Max Weber", "Vilfredo Pareto", "Karl Marx"], 1,
  "Bonne réponse : B. Le cours mobilise Weber pour justifier la démarche de modélisation : un idéal-type accentue certains traits du réel afin d’en faciliter l’analyse, comme le fait la concurrence pure et parfaite.",
  ['Weber', 'modélisation'])
q('qcm', "La comparaison Harrod-Domar / Solow sert dans le chapitre à montrer que :",
  ["La croissance est toujours instable", "Les conclusions dépendent étroitement des hypothèses retenues",
   "L’épargne détermine toujours l’investissement", "Le progrès technique est exogène"], 1,
  "Bonne réponse : B. Deux modèles du même objet concluent différemment — déséquilibre cumulatif chez Harrod-Domar, convergence vers un état stationnaire chez Solow — parce qu’ils ne posent pas les mêmes hypothèses.",
  ['modélisation', 'croissance'])
q('qcm', "La préférence pour la liquidité conduit Keynes à considérer que le taux d’intérêt se détermine :",
  ["Sur le marché des fonds prêtables", "Sur le marché monétaire",
   "Sur le marché du travail", "Par la banque centrale seule"], 1,
  "Bonne réponse : B. C’est la rupture avec l’analyse classique : le taux d’intérêt n’équilibre plus l’épargne et l’investissement, il devient le prix de la renonciation à la liquidité.",
  ['préférence pour la liquidité', 'taux d’intérêt'])
q('qcm', "Dans l’analyse classique, le taux d’intérêt est déterminé :",
  ["Sur le marché monétaire", "Sur le marché des fonds prêtables par l’épargne et l’investissement",
   "Par la demande effective", "Par la balance des paiements"], 1,
  "Bonne réponse : B. La dichotomie classique sépare sphère réelle et sphère monétaire : le taux d’intérêt équilibre l’offre d’épargne et la demande de financement, la monnaie n’étant qu’un instrument de transaction.",
  ['dichotomie classique', 'fonds prêtables'])
q('qcm', "Une politique procyclique :",
  ["Amortit les fluctuations", "Amplifie les fluctuations de la conjoncture",
   "Est toujours inefficace", "Concerne uniquement la politique monétaire"], 1,
  "Bonne réponse : B. Relancer une économie déjà en forte expansion ou pratiquer l’austérité en pleine récession accentue le cycle. Le cours précise qu’une telle politique n’est pas nécessairement inefficace pour tous les objectifs, mais qu’elle contredit l’objectif de stabilisation.",
  ['politique contracyclique', 'stabilisation'])
q('qcm', "Dans le policy mix Clinton-Greenspan, la combinaison est :",
  ["Budget expansionniste et monnaie restrictive", "Budget restrictif et monnaie accommodante",
   "Les deux expansionnistes", "Les deux restrictives"], 1,
  "Bonne réponse : B. La consolidation budgétaire déplace IS vers la gauche, l’assouplissement monétaire LM vers la droite : le revenu est préservé et le taux d’intérêt baisse.",
  ['policy mix', 'Clinton-Greenspan'])
q('qcm', "Lors de la réunification allemande, le policy mix associe :",
  ["Budget restrictif et monnaie accommodante", "Budget expansionniste et monnaie restrictive",
   "Les deux restrictives", "Les deux expansionnistes"], 1,
  "Bonne réponse : B. Les dépenses de réunification déplacent IS vers la droite tandis que la Bundesbank, pour contenir l’inflation, déplace LM vers la gauche : l’activité est préservée au prix de taux d’intérêt élevés.",
  ['policy mix', 'réunification allemande'])
q('qcm', "Le solde budgétaire américain passe, entre 1992 et 1998, de :",
  ["− 4,5 % à + 0,8 % du PIB", "− 2,7 % à − 0,8 % du PIB",
   "+ 0,8 % à − 4,5 % du PIB", "− 6 % à 0 %"], 0,
  "Bonne réponse : A. La croissance atteint pourtant 3,7 % en 1998 et les taux à un an reculent de 5,5 % à 4,8 % : c’est l’illustration chiffrée du policy mix Clinton-Greenspan.",
  ['chiffres', 'Clinton-Greenspan'])
q('qcm', "Les taux d’intérêt à court terme allemands passent de 4,3 % en 1988 à :",
  ["5,5 % en 1991", "7,1 % en 1991", "9,2 % en 1991", "12 % en 1991"], 2,
  "Bonne réponse : C. Cette hausse traduit la politique restrictive de la Bundesbank face aux tensions inflationnistes liées à la réunification, alors que le solde budgétaire se dégrade de + 0,2 % du PIB en 1989 à − 2,9 % en 1991.",
  ['chiffres', 'réunification allemande'])
q('qcm', "Les critères budgétaires de Maastricht retiennent :",
  ["3 % de déficit et 60 % de dette", "5 % de déficit et 90 % de dette",
   "1 % de déficit et 40 % de dette", "3 % de dette et 60 % de déficit"], 0,
  "Bonne réponse : A. Le traité est signé en 1992 et entre en vigueur en 1993 ; le Pacte de stabilité et de croissance adopté en 1997 complète cet encadrement. Le cours rappelle que ces seuils ne sont pas des interdictions absolues et inconditionnelles.",
  ['Maastricht', 'zone euro'])
q('qcm', "Le budget de l’Union européenne représente environ :",
  ["1 % du revenu national brut de l’Union", "5 % du RNB", "10 % du RNB", "20 % du RNB"], 0,
  "Bonne réponse : A. Un peu plus de 1 % dans les cadres budgétaires habituels : cette faiblesse relative limite la possibilité d’une stabilisation centralisée comparable à celle d’un État fédéral.",
  ['zone euro', 'budget européen'])
q('qcm', "Dans la zone euro, les États membres sont, entre eux, dans une situation proche :",
  ["Des changes flexibles", "Des changes fixes", "De l’autarcie", "Du flottement administré"], 1,
  "Bonne réponse : B. La monnaie unique supprime les taux de change bilatéraux : la situation est assimilable, dans le modèle simplifié, à un régime de changes fixes — tandis que la zone euro flotte face au reste du monde.",
  ['zone euro', 'régimes de change'])
q('qcm', "Un pays peut présenter un excédent courant et une balance globale déficitaire :",
  ["Jamais", "Si ses sorties de capitaux dépassent son excédent courant",
   "Seulement en changes fixes", "Seulement si l’inflation est élevée"], 1,
  "Bonne réponse : B. Avec un excédent courant de 100 et des sorties de capitaux de 140, la balance globale est déficitaire de 40. Le solde courant seul ne suffit donc jamais à conclure.",
  ['balance globale', 'piège'])
q('qcm', "La notion de stagnation séculaire est associée, dans le chapitre, à :",
  ["John Hicks", "Alvin Hansen", "Robert Mundell", "Paul Romer"], 1,
  "Bonne réponse : B. Hansen développe cette notion à la fin des années 1930, parallèlement à sa contribution à la tradition Hicks-Hansen et à la diffusion du keynésianisme aux États-Unis.",
  ['Hansen', 'stagnation séculaire'])
q('qcm', "Paul Romer est mobilisé dans le chapitre pour :",
  ["La courbe de Phillips", "La croissance endogène et les externalités de connaissance",
   "L’équivalence ricardienne", "Le multiplicateur"], 1,
  "Bonne réponse : B. Ses travaux de 1986 montrent comment l’accumulation des connaissances et les externalités peuvent soutenir une croissance durable : c’est l’argument des politiques visant la croissance potentielle.",
  ['Romer', 'politiques structurelles'])
q('qcm', "Jacques Généreux (2016) distingue, pour analyser les dilemmes :",
  ["Y et r", "Ype et YBTC", "IS et LM", "C et S"], 1,
  "Bonne réponse : B. Le revenu de plein emploi Ype et le revenu équilibrant les transactions courantes YBTC. Leur ordre relatif détermine le dilemme auquel le pays est exposé.",
  ['Généreux', 'dilemmes'])
q('qcm', "Dans le chapitre, l’exemple japonais sert à montrer que :",
  ["Les changes flexibles suppriment la contrainte extérieure",
   "Les changes flexibles ne garantissent pas l’autonomie totale des politiques économiques",
   "La trappe à liquidité n’existe pas", "L’inflation est toujours monétaire"], 1,
  "Bonne réponse : B. Une politique monétaire accommodante soutient l’activité mais réduit l’attractivité des placements en yens et accentue les pressions à la dépréciation, qui renchérissent les importations : l’arbitrage demeure.",
  ['Japon', 'contrainte extérieure'])
q('qcm', "L’effet d’éviction est nul :",
  ["En zone classique", "Dans une trappe à liquidité",
   "En changes flexibles", "Lorsque l’investissement est très sensible au taux"], 1,
  "Bonne réponse : B. LM étant horizontale, une relance budgétaire n’entraîne pas de hausse du taux d’intérêt : il n’y a pas d’éviction par les taux et la politique budgétaire est particulièrement efficace.",
  ['effet d’éviction', 'trappe à liquidité'])
q('qcm', "Lorsque LM est fortement pentue :",
  ["L’effet d’éviction est faible", "L’effet d’éviction est important",
   "La politique monétaire est inefficace", "BP devient horizontale"], 1,
  "Bonne réponse : B. Une hausse du revenu provoque alors une forte hausse du taux d’intérêt, donc une réduction importante de l’investissement privé : la relance budgétaire perd une grande partie de son efficacité.",
  ['pente de LM', 'effet d’éviction'])
q('qcm', "Une hausse de l’offre de monnaie, dans le modèle traditionnel :",
  ["Augmente le taux d’intérêt", "Fait baisser le taux d’intérêt d’équilibre",
   "Est sans effet sur le taux d’intérêt", "Déplace IS vers la droite"], 1,
  "Bonne réponse : B. Les agents détiennent plus de monnaie qu’ils ne le souhaitent, achètent des titres, le prix des obligations monte et le taux d’intérêt baisse.",
  ['politique monétaire', 'marché monétaire'])
q('qcm', "L’investissement, chez Keynes, dépend notamment :",
  ["Du seul taux d’intérêt", "Des débouchés anticipés et du taux d’intérêt",
   "De l’épargne préalable uniquement", "Du niveau général des prix"], 1,
  "Bonne réponse : B. Il dépend des débouchés futurs anticipés, du coût du financement, du rendement attendu du capital et de l’incertitude. Une baisse des taux peut rester sans effet si les anticipations sont très pessimistes.",
  ['investissement', 'anticipations'])
q('qcm', "Le chapitre soutient que l’investissement peut générer l’épargne qui lui correspond :",
  ["Parce que le taux d’intérêt s’ajuste", "Parce que l’investissement accroît le revenu, dont une partie est épargnée",
   "Parce que les banques créent de la monnaie", "Parce que l’État emprunte"], 1,
  "Bonne réponse : B. Avec s = 0,2 et ΔY = 500, l’épargne supplémentaire atteint 100, soit exactement l’investissement initial : la causalité keynésienne va de l’investissement au revenu puis à l’épargne.",
  ['multiplicateur', 'épargne'])
q('qcm', "Dans le modèle simple, le multiplicateur est :",
  ["Plus élevé pour une dépense publique d’investissement que de consommation",
   "Identique pour une dépense publique de consommation et d’investissement, à montant égal",
   "Nul pour l’investissement public", "Toujours égal à 1"], 1,
  "Bonne réponse : B. Le cours apporte cette nuance explicite : à montant initial égal le multiplicateur est le même, l’intérêt particulier de l’investissement public étant d’accroître en plus les capacités productives futures.",
  ['multiplicateur', 'investissement public'])
q('qcm', "Cibler une relance sur les ménages modestes est justifié, dans l’analyse keynésienne, par :",
  ["Leur poids électoral", "Leur propension marginale à consommer généralement plus élevée",
   "Leur propension à importer plus faible", "Leur épargne de précaution"], 1,
  "Bonne réponse : B. Une prestation versée à un ménage consommant 95 % du revenu supplémentaire engendre 95 de consommation initiale, contre 60 pour un ménage en consommant 60 % : la redistribution verticale renforce l’efficacité de la relance.",
  ['redistribution verticale', 'multiplicateur'])
q('qcm', "L’argument protectionniste tiré de l’analyse du multiplicateur repose sur :",
  ["La protection des industries naissantes", "La limitation des fuites par les importations",
   "La lutte contre le dumping", "La sécurité des approvisionnements"], 1,
  "Bonne réponse : B. Limiter les importations adresserait une part plus importante de la demande aux producteurs nationaux. Le cours confronte immédiatement cet argument aux coûts des restrictions et à l’intérêt d’une coordination des relances.",
  ['protectionnisme', 'multiplicateur'])
q('qcm', "Un équilibre IS-LM situé en dessous de la courbe BP correspond à :",
  ["Un excédent de la balance globale", "Un déficit de la balance globale",
   "Un équilibre extérieur", "Un excédent courant"], 1,
  "Bonne réponse : B. Pour un niveau de revenu donné, le taux d’intérêt y est insuffisant pour attirer les capitaux compensant le besoin de financement extérieur.",
  ['courbe BP', 'déséquilibre extérieur'])
q('qcm', "En changes fixes, un déficit extérieur conduit la banque centrale à :",
  ["Vendre sa monnaie et acheter des devises", "Acheter sa monnaie et vendre des devises",
   "Laisser la monnaie se déprécier", "Augmenter les dépenses publiques"], 1,
  "Bonne réponse : B. Pour défendre la parité menacée de dépréciation, elle achète sa propre monnaie contre ses réserves : la base monétaire diminue, LM se déplace vers la gauche et l’activité ralentit.",
  ['changes fixes', 'intervention'])
q('qcm', "L’effet de courbe en J est évoqué dans le chapitre à propos :",
  ["Du multiplicateur", "De la dépréciation et de l’ajustement du solde commercial",
   "De la trappe à liquidité", "De la courbe de Phillips"], 1,
  "Bonne réponse : B. Le cours rappelle qu’à court terme la balance commerciale peut se dégrader après une dépréciation, l’ajustement dépendant des élasticités-prix, des délais et du contenu importé des exportations.",
  ['courbe en J', 'dépréciation'])

# ========================================================== VRAI / FAUX
q('vrai/faux', "Un équilibre macroéconomique correspond nécessairement au plein emploi.",
  ["Vrai", "Faux"], 1,
  "Faux. C’est l’apport décisif de Keynes : la production peut être égale à la demande globale tout en demeurant insuffisante pour employer l’ensemble de la main-d’œuvre. L’économie connaît alors un équilibre de sous-emploi.",
  ['équilibre de sous-emploi', 'Keynes'])
q('vrai/faux', "La consommation autonome correspond à un minimum physiologique incompressible.",
  ["Vrai", "Faux"], 1,
  "Faux. C’est une mise en garde explicite du cours : la consommation autonome est indépendante du revenu courant dans la fonction retenue, ce qui ne signifie pas qu’elle soit impossible à réduire.",
  ['consommation autonome', 'piège'])
q('vrai/faux', "La propension marginale à importer et le ratio importations / PIB mesurent la même chose.",
  ["Vrai", "Faux"], 1,
  "Faux. La première mesure une variation des importations rapportée à une variation du revenu, le second le poids des importations dans le PIB.",
  ['propension à importer', 'piège'])
q('vrai/faux', "Le multiplicateur fiscal étant négatif, une baisse d’impôts réduit le revenu national.",
  ["Vrai", "Faux"], 1,
  "Faux. Le signe traduit le sens de la relation : kT = ΔY / ΔT = − c / (1 − c). Avec ΔT = − 100 et kT = − 4, ΔY = + 400. Une baisse d’impôts augmente bien le revenu national.",
  ['multiplicateur fiscal', 'piège'])
q('vrai/faux', "Dans une trappe à liquidité, toutes les formes de politique monétaire deviennent inefficaces.",
  ["Vrai", "Faux"], 1,
  "Faux. Le cours précise que c’est le canal conventionnel de baisse du taux d’intérêt qui est bloqué, et non nécessairement toute action monétaire.",
  ['trappe à liquidité', 'nuance'])
q('vrai/faux', "L’égalité comptable entre épargne et investissement réalisés signifie que les décisions des ménages et des entreprises étaient coordonnées.",
  ["Vrai", "Faux"], 1,
  "Faux. L’égalité ex post résulte des ajustements économiques et comptables ; ex ante, l’épargne désirée et l’investissement désiré peuvent parfaitement différer, puisqu’ils sont décidés par des agents différents.",
  ['ex ante ex post', 'critique post-keynésienne'])
q('vrai/faux', "La balance des paiements est comptablement équilibrée, donc chacun de ses soldes l’est aussi.",
  ["Vrai", "Faux"], 1,
  "Faux. La balance des paiements est équilibrée par construction, sous réserve des erreurs et omissions, mais ses soldes intermédiaires peuvent être déficitaires ou excédentaires. C’est précisément ce que la courbe BP exploite.",
  ['balance des paiements', 'piège'])
q('vrai/faux', "En changes flexibles avec mobilité parfaite des capitaux, la politique budgétaire est très efficace.",
  ["Vrai", "Faux"], 1,
  "Faux. C’est l’inverse : la relance élève le taux d’intérêt, attire les capitaux, apprécie la monnaie et réduit les exportations nettes ; IS revient à sa position initiale. C’est l’éviction par le taux de change.",
  ['Mundell-Fleming', 'changes flexibles'])
q('vrai/faux', "Le modèle IS-LM permet d’expliquer directement l’inflation.",
  ["Vrai", "Faux"], 1,
  "Faux. Le modèle traditionnel raisonne à prix fixes : les variations de la demande se traduisent par des modifications de la production et du taux d’intérêt. C’est le modèle OG-DG qui réintroduit explicitement le niveau général des prix.",
  ['IS-LM', 'OG-DG'])
q('vrai/faux', "La courbe de Phillips originelle relie directement l’inflation et le chômage.",
  ["Vrai", "Faux"], 1,
  "Faux. Phillips établit en 1958 une relation entre le chômage et la variation des salaires nominaux. La reformulation en termes d’inflation vient de Lipsey, Samuelson et Solow.",
  ['courbe de Phillips', 'piège'])
q('vrai/faux', "L’équivalence ricardienne est une loi empiriquement vérifiée dans tous les cas.",
  ["Vrai", "Faux"], 1,
  "Faux. Le cours la présente comme une critique théorique importante mais non universellement vérifiée : elle suppose des ménages informés, capables d’épargner, raisonnant sur un horizon long et peu contraints par leur revenu courant.",
  ['équivalence ricardienne', 'nuance'])
q('vrai/faux', "Robert Barro refuse toute intervention de l’État dans l’économie.",
  ["Vrai", "Faux"], 1,
  "Faux. Le chapitre souligne le paradoxe : critique de la relance conjoncturelle, Barro reconnaît dans ses travaux sur la croissance endogène de 1990 que certaines dépenses publiques productives, en particulier les infrastructures, soutiennent la croissance de long terme.",
  ['Barro', 'politiques structurelles'])
q('vrai/faux', "Une politique procyclique est toujours inefficace.",
  ["Vrai", "Faux"], 1,
  "Faux. Le cours nuance : elle n’est pas nécessairement inefficace pour tous les objectifs possibles, mais elle est contradictoire avec l’objectif de stabilisation du cycle économique.",
  ['politique procyclique', 'nuance'])
q('vrai/faux', "Avec une mobilité parfaite des capitaux, la courbe BP est verticale.",
  ["Vrai", "Faux"], 1,
  "Faux. Elle est horizontale : la moindre différence de rendement provoque des mouvements massifs, de sorte que le taux domestique s’aligne sur le taux mondial. C’est l’absence totale de mobilité qui rend BP verticale.",
  ['courbe BP', 'piège'])
q('vrai/faux', "L’exemple du policy mix Clinton-Greenspan prouve que la politique monétaire explique à elle seule la croissance américaine des années 1990.",
  ["Vrai", "Faux"], 1,
  "Faux. Le cours présente explicitement cette nuance : les taux américains ont connu plusieurs phases, la Fed n’a pas mené une politique continuellement expansionniste, et la croissance dépend aussi d’autres facteurs. C’est une illustration du policy mix, non une démonstration.",
  ['Clinton-Greenspan', 'nuance'])
q('vrai/faux', "La hausse du revenu accroît la demande de monnaie pour motif de spéculation.",
  ["Vrai", "Faux"], 1,
  "Faux. Les motifs de transaction et de précaution dépendent positivement du revenu ; le motif de spéculation dépend négativement du taux d’intérêt, et non du revenu.",
  ['demande de monnaie', 'piège'])
q('vrai/faux', "Une relance budgétaire est d’autant plus efficace que l’investissement privé est sensible au taux d’intérêt.",
  ["Vrai", "Faux"], 1,
  "Faux. C’est l’inverse : plus l’investissement est sensible au taux, plus la hausse des taux provoquée par la relance réduit l’investissement privé, donc plus l’effet d’éviction est important.",
  ['effet d’éviction', 'sensibilité au taux'])
q('vrai/faux', "La zone euro est en changes fixes vis-à-vis du reste du monde.",
  ["Vrai", "Faux"], 1,
  "Faux. L’euro flotte face au dollar, au yen et aux autres monnaies : la zone euro est en changes flexibles vis-à-vis de l’extérieur, alors que ses membres sont entre eux dans une situation proche des changes fixes.",
  ['zone euro', 'régimes de change'])
q('vrai/faux', "Le modèle IS-LM a été définitivement abandonné après les critiques monétaristes.",
  ["Vrai", "Faux"], 1,
  "Faux. La crise de 2008 l’a réhabilité, notamment pour analyser la trappe à liquidité et les limites de la politique monétaire conventionnelle. Le cours conclut qu’aucun modèle ne permet à lui seul d’analyser toutes les situations.",
  ['IS-LM', 'crise de 2008'])
q('vrai/faux', "La loi d’Okun établit directement que l’output gap positif provoque de l’inflation.",
  ["Vrai", "Faux"], 1,
  "Faux. Le cours est explicite : la loi d’Okun porte sur la relation entre production et chômage ; l’interprétation inflationniste de l’output gap positif relève plus largement de l’analyse des capacités de production et de la demande.",
  ['loi d’Okun', 'nuance'])
q('vrai/faux', "Le triangle de Mundell interdit toute politique monétaire autonome en régime de changes fixes.",
  ["Vrai", "Faux"], 1,
  "Faux. Il l’interdit lorsque les capitaux circulent librement. Un pays peut conserver des changes fixes et une autonomie monétaire s’il contrôle les mouvements de capitaux : c’est exactement la logique de Bretton Woods.",
  ['triangle de Mundell', 'contrôle des capitaux'])
q('vrai/faux', "Une économie en sous-emploi et en excédent extérieur fait face à un dilemme de politique économique.",
  ["Vrai", "Faux"], 1,
  "Faux. Dans cette configuration, une relance réduit simultanément le chômage et l’excédent extérieur, en augmentant les importations : les deux objectifs sont compatibles. Les dilemmes sont sous-emploi avec déficit et inflation avec excédent.",
  ['dilemmes', 'équilibre interne et externe'])

# ====================================================== QUESTIONS OUVERTES
q('question ouverte', "Expliquez le mécanisme complet du multiplicateur keynésien et sa limite.",
  [], 0,
  "Le multiplicateur repose sur la circulation successive des revenus. Une dépense initiale de 100 crée 100 de revenus ; avec une propension marginale à consommer de 0,8, ces revenus engendrent 80 de consommation, qui deviennent le revenu d’autres agents, lesquels dépensent 64, puis 51,2, et ainsi de suite. À chaque vague, 20 % du revenu supplémentaire est épargné : l’épargne est la fuite qui atténue progressivement le processus. La somme des vagues atteint 500, soit cinq fois la dépense initiale : k = 1 / (1 − c) = 5. Le mécanisme produit un résultat théorique majeur : l’investissement n’exige pas une épargne préalable équivalente, puisqu’avec s = 0,2 et ΔY = 500 l’épargne supplémentaire atteint exactement 100, soit l’investissement initial. La causalité keynésienne va donc de l’investissement au revenu puis à l’épargne, et non l’inverse. La limite tient aux fuites : en économie ouverte, les importations constituent une seconde fuite et le multiplicateur devient 1 / (1 − c + m). Dans l’exemple du cours, il passe de 5 à 2, et une dépense de 100 ne produit plus que 200 de revenu national supplémentaire.",
  ['multiplicateur', 'fuites'])
q('question ouverte', "Comparez les trois multiplicateurs budgétaires et expliquez leur hiérarchie.",
  [], 0,
  "Les trois multiplicateurs se déduisent de l’équation d’équilibre Y(1 − c) = C₀ − cT + cF + I + G. En faisant varier G seul : kG = 1 / (1 − c) = 5 avec c = 0,8. En faisant varier F seul : kF = c / (1 − c) = 4. En faisant varier T seul : kT = − c / (1 − c) = − 4. La hiérarchie kG > kF > |kT| s’explique par le point d’entrée dans le circuit. Une dépense publique de 100 constitue immédiatement une demande adressée aux entreprises : la première vague vaut 100. Une prestation sociale de 100 augmente d’abord le revenu disponible, dont 80 seulement sont consommés : la première vague ne vaut que 80. Une baisse d’impôts de 100 produit le même effet. Pour une relance de 100 millions, l’effet sur le revenu national est donc de + 500 millions pour G, + 400 pour F et + 400 pour une baisse de T. Le cours ajoute deux nuances décisives : le choix ne dépend pas seulement du multiplicateur mais aussi des objectifs sociaux poursuivis, et une redistribution vers les ménages à forte propension à consommer renforce l’efficacité des transferts.",
  ['multiplicateurs', 'politique budgétaire'])
q('question ouverte', "Construisez la courbe LM et justifiez sa pente.",
  [], 0,
  "La courbe LM rassemble les couples de revenu et de taux d’intérêt qui assurent l’égalité entre l’offre et la demande de monnaie. La demande comprend L1, les motifs de transaction et de précaution, qui dépendent positivement du revenu, et L2, le motif de spéculation, qui dépend négativement du taux d’intérêt. L’offre est supposée exogène, fixée par les autorités monétaires : elle est représentée par une droite verticale. Supposons que le revenu national augmente : les agents réalisent davantage de transactions et souhaitent détenir davantage de monnaie, la courbe de demande se déplaçant vers la droite. À offre inchangée, ils ne peuvent accroître leurs encaisses qu’en vendant des titres : l’offre de titres augmente, leur prix baisse et leur rendement de marché monte. Le taux d’intérêt augmente donc. La relation est positive, d’où une courbe LM croissante. Sa pente dépend des sensibilités : plus la demande spéculative réagit au taux d’intérêt, plus LM est plate, car une faible hausse suffit à libérer les encaisses nécessaires ; plus les besoins de monnaie augmentent avec le revenu, plus LM est pentue.",
  ['courbe LM', 'préférence pour la liquidité'])
q('question ouverte', "Expliquez la trappe à liquidité et ses conséquences de politique économique.",
  [], 0,
  "La trappe à liquidité désigne une situation dans laquelle les taux d’intérêt sont si faibles que les agents préfèrent conserver toute monnaie supplémentaire plutôt que d’acheter des titres. Le mécanisme passe par l’effet balançoire : un taux jugé anormalement bas fait anticiper sa remontée, donc une baisse du prix des obligations, donc une perte en capital pour qui en détient. La demande spéculative de monnaie devient extrêmement sensible au taux d’intérêt et, dans la représentation extrême, parfaitement élastique : toute monnaie supplémentaire est absorbée par les encaisses. Graphiquement, la courbe LM devient horizontale. Deux conséquences en découlent. D’une part, la politique monétaire conventionnelle perd son efficacité : une hausse de l’offre de monnaie ne fait plus baisser le taux, donc ne stimule plus l’investissement par le canal habituel. Le cours précise cependant que c’est ce canal qui est bloqué, et non nécessairement toute action monétaire. D’autre part, la politique budgétaire devient particulièrement efficace, puisqu’une relance déplace IS sans provoquer de hausse des taux : l’effet d’éviction est nul. C’est précisément cette configuration qui a réhabilité le modèle IS-LM après 2008.",
  ['trappe à liquidité', 'politique budgétaire'])
q('question ouverte', "Présentez l’effet d’éviction et ses déterminants.",
  [], 0,
  "L’effet d’éviction désigne la réduction de l’investissement privé provoquée par la hausse du taux d’intérêt consécutive à une relance budgétaire. L’enchaînement est le suivant : dépenses publiques ↑ → demande globale ↑ → revenu national ↑ → demande de monnaie pour transactions ↑ → à offre de monnaie inchangée, taux d’intérêt ↑ → coût du financement ↑ → investissement privé ↓. La hausse de la demande publique est donc partiellement compensée par la baisse de la demande privée, et le revenu augmente moins que si le taux était resté constant. Graphiquement, le revenu atteint Y1 et non Y3. Son intensité dépend de trois éléments. La pente de LM d’abord : plus elle est forte, plus la hausse du revenu élève le taux d’intérêt. La sensibilité de l’investissement au taux ensuite : plus elle est grande, plus l’éviction est forte. La configuration monétaire enfin : l’éviction est nulle dans une trappe à liquidité, où LM est horizontale, et totale dans la zone classique, où LM est verticale et où la relance n’élève que le taux d’intérêt. Une politique monétaire accommodante, en déplaçant LM vers la droite, permet de limiter l’éviction et de renforcer l’efficacité de la relance.",
  ['effet d’éviction', 'policy mix'])
q('question ouverte', "Expliquez pourquoi la politique monétaire est inefficace en changes fixes avec mobilité parfaite des capitaux.",
  [], 0,
  "Le cadre est celui d’une petite économie ouverte, en mobilité parfaite des capitaux et en changes fixes : la courbe BP est horizontale, le taux domestique devant rester aligné sur le taux mondial. Partons d’un triple équilibre. La banque centrale augmente l’offre de monnaie : LM se déplace vers la droite, le taux d’intérêt baisse et le revenu augmente dans un premier temps. Mais le taux domestique devient inférieur au taux mondial : r < r*. Les investisseurs, qui réagissent immédiatement aux différences de rendement, placent leurs capitaux à l’étranger. Ces sorties de capitaux créent un déficit de la balance globale et une pression à la dépréciation de la monnaie nationale. Or le pays est en changes fixes : la banque centrale doit défendre la parité. Elle achète donc sa propre monnaie en vendant des devises issues de ses réserves, ce qui retire de la monnaie nationale de la circulation. La masse monétaire diminue, LM revient vers sa position initiale, le taux d’intérêt retrouve le niveau mondial et le revenu son point de départ. L’expansion monétaire est donc intégralement neutralisée : elle n’augmente pas durablement le revenu national.",
  ['Mundell-Fleming', 'changes fixes'])
q('question ouverte', "Expliquez pourquoi la politique budgétaire est inefficace en changes flexibles avec mobilité parfaite des capitaux.",
  [], 0,
  "Partons du triple équilibre initial, en changes flexibles et mobilité parfaite. Le gouvernement augmente ses dépenses publiques : la demande globale augmente et IS se déplace vers la droite. Le revenu progresse, les transactions se multiplient, la demande de monnaie augmente et, à offre inchangée, le taux d’intérêt monte au-dessus du taux mondial : r > r*. Les placements domestiques deviennent plus attractifs et les capitaux entrent. Ces entrées accroissent la demande de monnaie nationale et provoquent une pression à l’appréciation. Comme le pays est en changes flexibles, la banque centrale n’a pas à l’empêcher : la monnaie s’apprécie. Les produits nationaux deviennent alors relativement plus chers pour les acheteurs étrangers et les produits étrangers moins chers pour les résidents : les exportations nettes diminuent et la demande globale recule. IS se déplace vers la gauche et revient à sa position initiale. Le revenu national retrouve son niveau de départ. On parle d’effet d’éviction par le taux de change : la dépense publique supplémentaire s’est substituée à une partie de la demande extérieure nette, sans augmenter la production.",
  ['Mundell-Fleming', 'changes flexibles'])
q('question ouverte', "Exposez le triangle des incompatibilités de Mundell et ses trois combinaisons.",
  [], 0,
  "Le triangle repose sur trois objectifs de politique économique : maintenir des changes fixes pour limiter l’incertitude, autoriser la libre circulation des capitaux pour favoriser l’intégration financière, conserver une politique monétaire autonome pour adapter les taux à la situation nationale. Ces trois objectifs ne peuvent pas être pleinement conciliés, car changes fixes et mobilité parfaite des capitaux contraignent le taux d’intérêt domestique à suivre le taux international. Trois combinaisons sont possibles, chacune préservant deux objectifs. Première combinaison, changes fixes et libre circulation : la baisse du taux provoque des sorties de capitaux et une pression à la dépréciation, que la banque centrale doit contrer par une contraction monétaire ; l’autonomie monétaire est perdue. Deuxième combinaison, changes flexibles et libre circulation : la dépréciation est autorisée, la banque centrale n’a pas à contracter la liquidité et conserve son autonomie, au prix d’une exposition aux fluctuations du change. Troisième combinaison, changes fixes et autonomie monétaire : il faut alors contrôler les mouvements de capitaux, ce qui correspond à la logique de Bretton Woods. La montée de la mobilité financière a rendu cette dernière combinaison de plus en plus difficile à tenir, jusqu’à la suspension de la convertibilité du dollar en or en août 1971 et au flottement généralisé de 1973.",
  ['triangle de Mundell', 'Bretton Woods'])
q('question ouverte', "Analysez la relance française de 1981 et le tournant de la rigueur de 1983.",
  [], 0,
  "En mai 1981, le gouvernement de Pierre Mauroy engage une politique de relance d’inspiration keynésienne : augmentation du SMIC, revalorisation des prestations sociales, créations d’emplois publics, soutien de la demande intérieure. Mais le contexte est doublement défavorable : la croissance des partenaires commerciaux est faible et l’inflation française déjà très élevée, autour de 13 % en 1981 et 12 % en 1982. Le mécanisme keynésien attendu fonctionne partiellement, mais une partie de la demande supplémentaire se porte sur des produits étrangers : les importations augmentent, les transactions courantes se dégradent, et l’effet multiplicateur profite en partie aux partenaires qui, eux, ne relancent pas. Le problème devient monétaire : la France participe au Système monétaire européen, où les parités sont fixes mais ajustables ; elle ne peut donc pas laisser le franc se déprécier librement. Les difficultés extérieures alimentent les anticipations de dévaluation, les investisseurs vendent des francs, et la France procède à trois dévaluations entre 1981 et 1983. En mars 1983, le gouvernement choisit de maintenir le franc dans le SME : la stratégie de relance est abandonnée au profit d’une politique restrictive visant à défendre la monnaie, contenir l’inflation et réduire les déséquilibres extérieurs. L’épisode illustre la contrainte extérieure : l’objectif externe finit par l’emporter sur l’objectif interne.",
  ['relance de 1981', 'contrainte extérieure'])
q('question ouverte', "Présentez les trois critiques de la relance budgétaire et distinguez-les.",
  [], 0,
  "Les trois critiques portent sur des canaux différents, qu’il faut absolument distinguer. La première, l’effet d’éviction, porte sur l’investissement : la relance élève le revenu, donc la demande de monnaie, donc le taux d’intérêt, ce qui réduit l’investissement privé. Elle ne met pas en cause le comportement des ménages mais le fonctionnement du marché monétaire. La deuxième, formulée par Friedman en 1957, porte sur la consommation : les ménages règlent leur consommation sur leur revenu permanent, c’est-à-dire le revenu moyen de long terme qu’ils anticipent ; un transfert perçu comme temporaire est donc principalement épargné. Le cours nuance : les ménages contraints financièrement peuvent au contraire en consommer une large part, l’effet dépendant du caractère anticipé comme durable ou temporaire du supplément de revenu. La troisième, l’équivalence ricardienne de Barro (1974), porte sur le financement : une baisse d’impôts financée par la dette fait anticiper des prélèvements futurs, de sorte que l’épargne privée compense la désépargne publique. Ces trois canaux convergent vers une même conclusion — un multiplicateur plus faible qu’attendu — mais par des mécanismes distincts, ce qui permet de les mobiliser séparément en dissertation.",
  ['critiques', 'politique budgétaire'])
q('question ouverte', "Expliquez la critique monétariste du modèle IS-LM à l’aide du graphique.",
  [], 0,
  "Supposons que l’économie produise déjà à son niveau de plein emploi YPE, à l’intersection de IS₁ et LM₁, au taux d’intérêt r₁. Le gouvernement augmente ses dépenses publiques : IS₁ se déplace vers IS₂. À prix fixes, le modèle IS-LM traditionnel laisserait apparaître une augmentation de la production. Mais les capacités productives sont déjà pleinement utilisées : la hausse de la demande exerce des tensions sur les prix. Or lorsque les prix augmentent, une quantité nominale de monnaie donnée permet d’acheter moins de biens : l’offre réelle de monnaie diminue. À offre nominale inchangée, LM₁ se déplace donc vers LM₂, c’est-à-dire vers la gauche. Cette contraction monétaire réelle élève le taux d’intérêt de r₁ à r₂, ce qui réduit l’investissement privé. Au terme de l’ajustement, l’économie retrouve exactement le même niveau de production YPE, mais avec un taux d’intérêt plus élevé : la relance n’a produit qu’une recomposition de la demande au détriment du secteur privé et une hausse des prix. La conclusion monétariste en découle : lorsque l’économie est à son potentiel, les politiques de demande ne peuvent pas accroître durablement l’activité, et il faut privilégier les politiques structurelles qui élèvent la production potentielle.",
  ['critique monétariste', 'offre réelle de monnaie'])
q('question ouverte', "Pourquoi le modèle OG-DG s’impose-t-il après les chocs pétroliers ?",
  [], 0,
  "Le modèle IS-LM traditionnel raisonne à prix fixes : il explique les variations du revenu et du taux d’intérêt, mais ne peut pas représenter les mécanismes d’inflation et de déflation. Or les années 1970 font apparaître une situation que l’arbitrage inflation-chômage ne permet pas d’interpréter : la stagflation, c’est-à-dire la coexistence d’une inflation élevée, d’une croissance faible et d’un chômage important. Le mécanisme est un choc d’offre : le premier choc pétrolier de 1973-1974 provoque une forte hausse du prix du pétrole, consommation intermédiaire majeure pour de nombreuses entreprises ; les coûts de production augmentent, l’offre globale se réduit, la production diminue et le niveau général des prix augmente. Les données de l’OCDE pour 1975 le confirment : croissance de − 1,0 % en France, − 0,9 % en Allemagne et − 0,2 % aux États-Unis, avec une inflation respectivement de 11,7 %, 5,9 % et 9,1 %. Le modèle OG-DG représente précisément cette configuration : la courbe de demande globale restant inchangée, la courbe d’offre globale de court terme se déplace vers la gauche, l’équilibre passant de E1 à E2 avec un prix plus élevé et une production plus faible. Le modèle permet donc d’analyser simultanément l’activité et les prix, et déplace l’attention vers les déterminants de l’offre et la croissance potentielle.",
  ['OG-DG', 'stagflation'])
q('question ouverte', "Comment l’ouverture internationale modifie-t-elle l’efficacité d’une relance budgétaire ?",
  [], 0,
  "L’ouverture agit par trois canaux. Le premier est l’affaiblissement du multiplicateur : les importations dépendent positivement du revenu, M = M₀ + mY, de sorte qu’une partie de la demande supplémentaire s’adresse aux producteurs étrangers. Le multiplicateur devient 1 / (1 − c + m), ou 1 / [1 − c(1 − t) + m] avec une fiscalité proportionnelle ; dans l’exemple du cours il passe de 5 à 2. Le deuxième canal est l’interdépendance : la relance d’un pays stimule les exportations de ses partenaires, dont la production et les revenus augmentent, avec de possibles effets de retour. Cela crée une tentation de passager clandestin — pourquoi financer une relance coûteuse si le partenaire peut relancer à ma place ? — et, si tous attendent, aucune relance suffisante n’est engagée. La coordination permet au contraire d’internaliser ces débordements : les importations des uns deviennent les exportations des autres. Le troisième canal est financier : selon le régime de change et la mobilité des capitaux, la relance peut être amplifiée — changes fixes et mobilité parfaite — ou totalement neutralisée par l’appréciation — changes flexibles et mobilité parfaite. L’efficacité d’une relance ne se juge donc jamais indépendamment du cadre monétaire international.",
  ['économie ouverte', 'coordination'])
q('question ouverte', "Présentez les quatre configurations d’équilibre interne et externe et les dilemmes qu’elles produisent.",
  [], 0,
  "On croise deux situations internes — sous-emploi ou tensions inflationnistes — et deux situations externes — déficit ou excédent de la balance. Première configuration, sous-emploi et excédent extérieur : une relance augmente la production et l’emploi tout en accroissant les importations, ce qui réduit l’excédent. Les deux déséquilibres se corrigent ensemble : pas de dilemme. Deuxième configuration, sous-emploi et déficit extérieur : relancer pour lutter contre le chômage augmente les importations et aggrave le déficit ; freiner la demande pour corriger le déficit aggrave le chômage. C’est un véritable dilemme, celui de la contrainte extérieure, qu’illustre la France de 1981-1983. Troisième configuration, inflation et déficit extérieur : une politique restrictive réduit à la fois les tensions sur les prix et les importations. Pas de dilemme non plus. Quatrième configuration, inflation et excédent extérieur : la rigueur nécessaire à la stabilité des prix réduit les importations et renforce l’excédent, tandis qu’une relance réduirait l’excédent mais aggraverait l’inflation. C’est le second dilemme, que le cours associe aux économies structurellement excédentaires d’Europe du Nord. Jacques Généreux en propose une lecture simplifiée à partir de l’écart entre le revenu de plein emploi Ype et le revenu équilibrant les transactions courantes YBTC.",
  ['dilemmes', 'Généreux'])
q('question ouverte', "En quoi le policy mix de la zone euro est-il institutionnellement particulier ?",
  [], 0,
  "La zone euro présente une asymétrie institutionnelle. La politique monétaire est unique : elle est conduite par la Banque centrale européenne, qui fixe les conditions monétaires communes et les principaux taux directeurs. Aucun État membre ne peut décider d’une politique monétaire nationale indépendante. Les politiques budgétaires, en revanche, demeurent principalement nationales : chaque État détermine ses dépenses, ses prélèvements et ses orientations, mais sous l’encadrement de règles européennes — critères de Maastricht de 3 % de déficit et 60 % de dette, signés en 1992 et entrés en vigueur en 1993, complétés par le Pacte de stabilité et de croissance de 1997, plusieurs fois réformé. Cette architecture pose deux difficultés. D’une part l’hétérogénéité : un pays en récession souhaiterait des taux plus bas quand un autre, confronté à l’inflation, souhaiterait des taux plus hauts, alors que la BCE doit fixer une politique commune. D’autre part la coordination : un État confronté au chômage et à un déficit extérieur ne maîtrise que l’un des deux instruments, et une décision monétaire prise pour l’ensemble de la zone peut ne pas convenir à sa situation particulière. Les crises de 2008 puis des dettes souveraines, dont la Grèce est l’exemple majeur, ont révélé ces limites, les ajustements budgétaires réduisant la demande intérieure dans des économies déjà déprimées.",
  ['zone euro', 'policy mix'])
q('question ouverte', "Expliquez pourquoi la pente de la courbe BP dépend de la mobilité des capitaux.",
  [], 0,
  "La courbe BP rassemble les couples de revenu et de taux d’intérêt assurant l’équilibre de la balance globale. Partons d’un point d’équilibre A. Si le revenu augmente sans que le taux d’intérêt bouge, les importations augmentent, le solde courant se dégrade et, faute d’entrées de capitaux supplémentaires, la balance globale devient déficitaire : le point se situe sous BP. Pour revenir à l’équilibre, il faut attirer des capitaux, donc élever le taux d’intérêt. La pente de BP mesure précisément l’ampleur de cette hausse nécessaire. Lorsque la mobilité est élevée, les investisseurs réagissent à de faibles différences de rendement : une petite hausse du taux suffit à provoquer des entrées importantes, et la courbe est relativement plate. Lorsque la mobilité est faible, une hausse modérée attire peu de capitaux : il faut augmenter beaucoup plus le taux pour obtenir les mêmes entrées, et la courbe devient plus pentue. Deux cas extrêmes en découlent. En mobilité parfaite, le taux domestique s’aligne sur le taux mondial et BP devient horizontale. En l’absence totale de mobilité, le taux ne permet plus de corriger un déséquilibre extérieur : l’ajustement doit passer par le revenu et les importations, et BP devient verticale. La globalisation financière, caractérisée par les trois D de Bourguinat, a progressivement horizontalisé BP dans les économies avancées.",
  ['courbe BP', 'mobilité des capitaux'])
q('question ouverte', "Pourquoi un modèle économique peut-il être utile sans être réaliste ?",
  [], 0,
  "Un modèle économique est une représentation abstraite et simplifiée construite à partir d’hypothèses : il ne cherche pas à reproduire la réalité mais à isoler certaines relations afin d’en expliquer le fonctionnement. Sa pertinence dépend donc de sa capacité à expliquer un phénomène dans le cadre des hypothèses retenues, et non de son réalisme descriptif. Le cours mobilise deux illustrations. D’abord la concurrence pure et parfaite, qui suppose atomicité, homogénéité, libre entrée, transparence et mobilité des facteurs : ces conditions sont rarement toutes réunies, mais elles permettent d’étudier le fonctionnement théorique d’un marché concurrentiel. Ensuite l’idéal-type de Max Weber, construction intellectuelle qui accentue certains traits du réel pour en faciliter l’analyse : la concurrence pure et parfaite est un idéal-type de concurrence, le monopole pur un idéal-type de concentration de l’offre, les marchés réels présentant des caractéristiques intermédiaires. La contrepartie est que les hypothèses commandent les conclusions. La comparaison de Harrod-Domar et de Solow le démontre : dans le premier cas, rien ne garantit que la demande suive les capacités, d’où une croissance instable ; dans le second, les rendements décroissants du capital conduisent à un état stationnaire. Même objet, hypothèses différentes, conclusions opposées.",
  ['modélisation', 'Weber'])
q('question ouverte', "Comment Keynes rompt-il avec l’analyse néoclassique du chômage ?",
  [], 0,
  "L’analyse néoclassique, développée notamment par Pigou, traite le travail comme un bien échangé sur un marché : l’offre de travail croît avec le salaire réel, la demande décroît, et leur intersection détermine un salaire et une quantité d’équilibre correspondant au plein emploi. Si le salaire réel se maintient au-dessus de ce niveau, l’offre excède la demande : l’écart est le chômage, qui s’explique donc par une rigidité salariale et devrait disparaître par la baisse du salaire réel. Keynes inverse le raisonnement. Le chômage ne provient pas nécessairement d’un salaire trop élevé mais d’une demande globale insuffisante : si les ménages consomment moins et les entreprises investissent moins, la demande anticipée ne justifie pas une production correspondant au plein emploi, et les entreprises n’ont aucun intérêt à produire davantage sans débouchés. Le chômage devient alors involontaire : des individus souhaitent travailler au salaire en vigueur mais ne trouvent pas d’emploi. Keynes ajoute une objection décisive : une baisse des salaires ne garantit pas le retour au plein emploi, car elle pèse aussi sur les revenus et la consommation, donc sur la demande elle-même. La solution n’est plus la flexibilité du marché du travail mais la stimulation de la demande globale, l’État prenant le relais lorsque la demande privée est insuffisante.",
  ['Keynes', 'chômage involontaire'])
q('question ouverte', "Expliquez comment les anticipations peuvent enfermer une économie dans un équilibre de sous-emploi.",
  [], 0,
  "L’investissement privé dépend moins de la situation présente des entreprises que de la demande qu’elles anticipent : elles investissent lorsqu’elles prévoient des débouchés suffisants, et reportent leurs projets lorsqu’elles anticipent une demande durablement faible. En période de récession, les perspectives de ventes deviennent incertaines, certaines entreprises font faillite, les autres réduisent leurs dépenses, suspendent leurs investissements, gèlent leurs recrutements ou licencient. L’enchaînement devient cumulatif : récession → anticipations pessimistes → investissement ↓ → embauches ↓ → revenus distribués ↓ → consommation ↓ → demande globale ↓ → récession aggravée. Le mécanisme devient autoréalisateur : une prophétie autoréalisatrice est une anticipation qui contribue, par les comportements qu’elle provoque, à faire apparaître la situation anticipée. Les entreprises qui pensent que la demande future sera faible décident de ne pas investir ni embaucher ; cette décision réduit les revenus distribués, les ménages consomment moins, la demande devient effectivement plus faible, et le pessimisme initial se trouve confirmé. C’est précisément ce cercle que l’intervention publique doit briser : puisque la demande privée ne permet pas de retrouver spontanément le plein emploi, l’État peut prendre le relais, directement en augmentant ses dépenses ou indirectement en soutenant le revenu disponible.",
  ['anticipations', 'prophétie autoréalisatrice'])
q('question ouverte', "Quelle est la différence entre une politique conjoncturelle et une politique structurelle, et pourquoi les critiques du modèle IS-LM conduisent-elles aux secondes ?",
  [], 0,
  "Une politique conjoncturelle cherche à influencer l’activité à court terme et agit principalement sur la demande globale : relance budgétaire, baisse des taux d’intérêt, soutien temporaire au revenu. Une politique structurelle cherche à modifier durablement le fonctionnement de l’économie et agit sur l’offre et les capacités de production : formation, innovation, infrastructures, amélioration du fonctionnement des marchés, investissement productif. Le passage des unes aux autres découle logiquement des critiques. Si l’économie se situe déjà à son niveau de production potentiel, une relance ne peut pas accroître durablement la production réelle : elle provoque des tensions sur les prix, réduit l’offre réelle de monnaie, déplace LM vers la gauche, élève le taux d’intérêt et évince l’investissement privé. De même, l’existence d’un taux de chômage naturel implique qu’une stimulation de la demande ne peut pas abaisser durablement le chômage en dessous de son niveau structurel. Si la production est limitée par des contraintes structurelles, il faut donc modifier ces contraintes : investissement productif ↑ → capacités ↑ → productivité ↑ → croissance potentielle ↑. Le chapitre souligne enfin que critiquer la relance ne revient pas à refuser toute intervention : Barro lui-même montre en 1990 que les infrastructures publiques peuvent accroître durablement la productivité.",
  ['politiques structurelles', 'critiques'])
q('question ouverte', "Pourquoi les trois modèles IS-LM, OG-DG et IS-LM-BP sont-ils complémentaires ?",
  [], 0,
  "Chacun privilégie une dimension de l’équilibre macroéconomique et répond à une question propre. Le modèle IS-LM analyse les politiques de demande en économie fermée : il montre les interactions entre la sphère réelle et la sphère monétaire, permet d’étudier les effets d’une politique budgétaire ou monétaire sur la production et le taux d’intérêt, d’analyser l’effet d’éviction et de représenter la trappe à liquidité. Sa limite est l’hypothèse de prix fixes. Le modèle OG-DG réintroduit précisément le niveau général des prix : il permet d’analyser l’inflation, la déflation, les chocs d’offre et les tensions entre activité et prix — ce que la stagflation des années 1970 rendait indispensable. Le modèle IS-LM-BP ajoute l’équilibre extérieur : il intègre les échanges internationaux, les mouvements de capitaux, les taux de change et les contraintes d’équilibre extérieur, et montre que l’efficacité des politiques dépend du régime de change et de la mobilité des capitaux. Le cours en tire une conclusion méthodologique : aucun modèle macroéconomique ne permet à lui seul d’analyser toutes les situations. La réhabilitation du modèle IS-LM après 2008 le confirme : les politiques de demande ne sont ni systématiquement efficaces ni systématiquement inefficaces, leur pertinence dépend du contexte macroéconomique, et c’est le choix du modèle pertinent qui constitue le premier acte d’analyse.",
  ['modèles', 'complémentarité'])
q('question ouverte', "Quelles sont les limites du modèle Mundell-Fleming ?",
  [], 0,
  "Le cours en identifie quatre. La première tient à son caractère statique et à l’hypothèse de rigidité des prix : dans sa version élémentaire, les variations de la demande se traduisent principalement par des variations de la production, ce qui suppose des capacités mobilisables. Lorsque l’économie se rapproche du plein emploi, une hausse de la demande se traduit davantage par de l’inflation, que le modèle ne représente pas. La deuxième porte sur le comportement des investisseurs : le modèle fait dépendre les flux de capitaux des seuls différentiels de taux d’intérêt, alors qu’un placement à 6 % peut être moins attractif qu’un placement à 3 % si une forte dépréciation est anticipée. Les investisseurs tiennent également compte du risque de défaut, du risque politique, de la liquidité des marchés, de la stabilité financière et des anticipations de politique monétaire. La troisième limite est l’hypothèse de petite économie ouverte, dont les décisions n’affecteraient pas le reste du monde : elle devient peu pertinente pour les grandes économies, une relance américaine stimulant les exportations de ses partenaires et une décision de la Fed modifiant les conditions financières internationales, avec des effets de retour. La quatrième est son incapacité à représenter la formation des prix, qui justifie son prolongement par le modèle offre globale-demande globale.",
  ['Mundell-Fleming', 'limites'])

TYPES = {'qcm': 'qcm', 'vrai/faux': 'vraifa', 'question ouverte': 'questi'}
QUIZ = []
TAGS = {}
for _i, (_t, _q, _o, _a, _e, _g) in enumerate(Q, 1):
    _id = 'ch25-%s-%d' % (TYPES[_t], _i)
    QUIZ.append({'type': _t, 'q': _q, 'opts': _o, 'ans': _a, 'exp': _e,
                 'ch': 25, 'id': _id})
    TAGS[_id] = _g
