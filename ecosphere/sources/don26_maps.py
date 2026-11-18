# -*- coding: utf-8 -*-
"""Carte mentale et fiche méthode du chapitre 6 de deuxième année (clé 26).

La structure reprend exactement celle de la carte mentale transmise : quatre
branches — nature et mesure des taux de change, marché des changes et
déterminants, régimes de change et crises, politique de change et stratégies —
et leurs sous-branches. Les feuilles sont détaillées à partir du document de
cours.
"""

VMAP = {
 'title': "Deuxième année, chapitre 6 — Taux de change et systèmes de change",
 'core': "Taux de change et systèmes de change",
 'branches': [

  {'title': "Nature et mesure des taux de change", 'children': [
    {'title': "Monnaie et devise", 'children': [
      "Monnaie : créance dotée d’un pouvoir libératoire général",
      "Trois fonctions : moyen d’échange, unité de compte, réserve de valeur",
      "Devise : monnaie étrangère pour les transactions internationales",
      "Une même monnaie est nationale pour les uns et devise pour les autres",
      "Convertibilité : échange libre ou soumis à des contrôles",
      "Distinguer convertibilité courante et convertibilité financière"]},
    {'title': "Position internationale du dollar", 'children': [
      "Monnaie véhiculaire : intermédiaire des échanges entre tiers",
      "Effets de réseau : plus le dollar est utilisé, plus il est attractif",
      "Unité de compte internationale",
      "Monnaie de réserve internationale, appuyée sur les titres du Trésor",
      "Les trois fonctions se renforcent mutuellement"]},
    {'title': "Indicateurs de change", 'children': [
      "Taux nominal bilatéral : prix d’une monnaie dans une autre",
      "Cotation au certain : 1 € = 1,20 USD ; hausse = appréciation",
      "Cotation à l’incertain : une devise exprimée en monnaie nationale",
      "Taux effectif nominal : valeur face à un panier pondéré de devises",
      "Taux de change réel : mesure de la compétitivité-prix relative"]},
    {'title': "Fluctuations et volatilité", 'children': [
      "Appréciation et dépréciation en régime flottant",
      "Réévaluation et dévaluation en régime administré",
      "Volatilité : ampleur des variations et incertitude pour les agents",
      "Une facture d’un million de dollars à six mois expose au risque de change"]}]},

  {'title': "Marché des changes et déterminants", 'children': [
    {'title': "Fonctionnement du Forex", 'children': [
      "Forex : marché-réseau mondial et dématérialisé (Dominique Plihon, 2017)",
      "Fonctionnement quasi continu : Londres, New York, Tokyo, Singapour, Hong Kong",
      "Arbitrage : convergence des cotations entre les places financières",
      "Domination du dollar : 89,2 % des transactions en 2025",
      "Euro 28,9 % et yen 16,8 % ; total de 200 % car deux monnaies par transaction",
      "Acteurs : grandes banques, autres banques et investisseurs institutionnels"]},
    {'title': "Instruments financiers", 'children': [
      "Opérations au comptant : règlement souvent sous deux jours ouvrés (31 %)",
      "Opérations à terme : fixation aujourd’hui d’un taux futur (19 %)",
      "Options de change : droit, non obligation, contre paiement d’une prime (7 %)",
      "Swaps de change et de devises : échanges temporaires (44 %)",
      "Volume quotidien : de 880 milliards de dollars en 1992 à 9 600 en 2025"]},
    {'title': "Couverture et spéculation", 'children': [
      "Couverture : réduction de l’exposition au risque de change",
      "Un transfert de risque suppose une contrepartie qui l’accepte",
      "Spéculation : position ouverte prise dans l’espoir d’un gain",
      "Spéculation stabilisatrice quand les écarts sont jugés temporaires",
      "Spéculation déstabilisatrice et comportements mimétiques en crise",
      "Anticipations autoréalisatrices : la baisse anticipée se produit"]},
    {'title': "Déterminants économiques", 'children': [
      "Balance des paiements : flux commerciaux et financiers",
      "Exportations : soutien de la demande de monnaie nationale",
      "Importations : accroissement de l’offre de monnaie nationale",
      "Solde commercial : excédent ou déficit, sans automatisme sur le change",
      "La monnaie de facturation conditionne l’effet sur le marché des changes",
      "Les mouvements de capitaux peuvent dominer les flux commerciaux"]},
    {'title': "Théorie de la parité des pouvoirs d’achat", 'children': [
      "Gustav Cassel (1918) : le change reflète à long terme les niveaux de prix",
      "Loi du prix unique et arbitrage international sur les biens",
      "PPA absolue : e = P* / P, égalisation du prix des paniers",
      "PPA relative : compensation des différentiels d’inflation",
      "Limites : coûts de transaction et biens non échangeables",
      "Effet Balassa-Samuelson (1964) : productivité et niveaux de prix",
      "Les mouvements de capitaux éloignent le change de la PPA à court terme"]}]},

  {'title': "Régimes de change et crises", 'children': [
    {'title': "Typologie des régimes", 'children': [
      "Le choix du régime relève de la souveraineté monétaire, déclaré au FMI",
      "Régime de jure, officiellement annoncé, et régime de facto, effectivement pratiqué",
      "Continuum entre ancrage strict et flottement libre",
      "Ancrage ferme : dollarisation (Équateur, 2000) et union monétaire",
      "Caisse d’émission : émission couverte par les réserves (Hong Kong, 1983)",
      "Argentine : régime de convertibilité de 1991 à 2002",
      "Changes fixes conventionnels et bandes de fluctuation (SME, ± 15 % en 1993)",
      "Ancrage glissant, flottement administré (Inde, Brésil, Hongrie)",
      "Flottement libre : États-Unis, Royaume-Uni, Japon, Canada, zone euro",
      "Répartition 2025 : 29 arrimages fermes, 88 souples, 66 flottements"]},
    {'title': "Interventions et crises historiques", 'children': [
      "Même en flottement, les banques centrales peuvent intervenir",
      "Accords du Plaza (septembre 1985) : baisse concertée du dollar à cinq",
      "Accords du Louvre (février 1987) : stabilisation des parités",
      "Lignes de swap : fourniture temporaire de liquidités en devises",
      "Choc Volcker (1979) : taux américains et appréciation du dollar",
      "Recyclage des pétrodollars : 450 milliards d’excédents OPEP de 1974 à 1981",
      "Crise mexicaine d’août 1982 et dette latino-américaine de 75 à 315 milliards"]},
    {'title': "Avantages des changes fixes", 'children': [
      "Réduction de l’incertitude et des coûts de couverture",
      "Lutte contre l’inflation et importation de crédibilité monétaire",
      "Peur du flottement (Calvo et Reinhart, 2002)",
      "Effets de bilan : dettes en devises et revenus en monnaie nationale",
      "Inflation importée dans les économies dépendantes des importations"]},
    {'title': "Triangle de Mundell", 'children': [
      "Trinité impossible : stabilité du change, autonomie monétaire, mobilité des capitaux",
      "Bretton Woods (1944-1971) : changes fixes, or à 35 dollars l’once, capitaux contrôlés",
      "15 août 1971 : fin de la convertibilité du dollar en or ; 1973 : flottement",
      "SME (1979-1993) : crises de 1992-1993 et élargissement des marges",
      "Euro (1999, billets en 2002) : union monétaire et politique unique",
      "Jean-Marc Daniel (2015) : le monde a essayé toutes les combinaisons"]}]},

  {'title': "Politique de change et stratégies", 'children': [
    {'title': "Instruments de la politique de change", 'children': [
      "Intervention directe : acheter ou vendre des devises",
      "Défendre contre la dépréciation est plus contraignant : réserves épuisables",
      "Taux d’intérêt : attirer les capitaux et soutenir la monnaie",
      "Contrôle des changes : restrictions quantitatives (Chine, 50 000 dollars)",
      "Les politiques conjoncturelles influencent indirectement le change"]},
    {'title': "Dévaluation compétitive", 'children': [
      "Distinguer dévaluation subie et dévaluation compétitive",
      "Guerre des monnaies : dévaluations successives qui se neutralisent",
      "Courbe en J : dégradation initiale puis redressement du solde",
      "Condition de Marshall-Lerner : |εX| + |εM| > 1",
      "Élasticités fortes : + 4,6 ; élasticités faibles : − 4,8",
      "Comportement de marge : la dévaluation n’est pas toujours répercutée",
      "Désindustrialisation : impossible de substituer des productions nationales",
      "Cercle vicieux d’une monnaie faible en huit étapes",
      "Dévaluations du franc : octobre 1981, juin 1982, mars 1983"]},
    {'title': "Désinflation compétitive", 'children': [
      "Politique du franc fort à partir de mars 1983",
      "Désinflation ≠ déflation",
      "Politiques structurelles : privatisations, déréglementations, concurrence",
      "Politique monétaire restrictive et taux d’intérêt réels élevés",
      "Cercle vertueux d’une monnaie forte en huit étapes",
      "Résultats : inflation de 14 % à environ 2 %, courant excédentaire 1992-2003",
      "Taux de marge de 25 % en 1985 à 32 % en 1989",
      "Théorème de Schmidt : profits, investissement puis emplois",
      "Effet de levier devenu effet de massue : priorité au désendettement",
      "Effets pervers : croissance faible, chômage de 8 % en 1982 à 12 % en 1998"]},
    {'title': "Le dollar et l’avenir du système monétaire", 'children': [
      "Doctrine Miran (novembre 2024) : un dollar structurellement trop fort",
      "Solde courant = épargne nationale − investissement national",
      "Contradiction entre droits de douane, inflation et dollar faible",
      "Accords de Mar-a-Lago : projet de dépréciation coordonnée",
      "Paradoxe du dollar : déprécier la monnaie de réserve mondiale",
      "Stablecoins adossés au dollar et GENIUS Act de juillet 2025",
      "Monnaies numériques de banque centrale et souveraineté monétaire"]}]},
 ],
}

MAP = {
 'title': "Deuxième année, chapitre 6 — Taux de change et systèmes de change",
 'sub': "Monnaie, devise et mesure du change · Forex, instruments et spéculation · "
        "parité des pouvoirs d’achat et ses limites · typologie des régimes et "
        "triangle de Mundell · politique de change, dévaluation compétitive et "
        "désinflation compétitive.",
 'core': "Taux de change et systèmes de change",
 'branches': [],
 'legend': [
  {'k': "Auteurs",
   'v': "Cassel, Plihon, Friedman, Balassa et Samuelson, Calvo et Reinhart, "
        "Mundell, Jean-Marc Daniel, Volcker, Marshall et Lerner, Schmidt, Miran."},
  {'k': "Pièges",
   'v': "Dépréciation et appréciation (marché) ≠ dévaluation et réévaluation "
        "(décision officielle) ; cotation au certain ≠ cotation à l’incertain, la "
        "lecture des variations s’inverse ; taux de change nominal ≠ taux de change "
        "réel ; désinflation ≠ déflation ; un swap n’est pas une assurance mais un "
        "contrat d’échange ; l’euro est une union monétaire en interne et une "
        "monnaie flottante en externe ; une accusation de sous-évaluation ne "
        "démontre pas une manipulation ; un déficit commercial n’entraîne pas "
        "mécaniquement une dépréciation si les capitaux entrent ; la PPA est une "
        "référence de long terme, pas une prévision de court terme."},
  {'k': "Chiffres",
   'v': "Dollar : 89,2 % des transactions de change en 2025 ; volume quotidien du "
        "Forex de 880 milliards de dollars en 1992 à 9 600 en 2025 ; structure des "
        "opérations 31 % comptant, 19 % terme, 44 % swaps, 7 % options ; régimes "
        "2025 : 29 arrimages fermes, 88 souples, 66 flottements ; or à 35 dollars "
        "l’once sous Bretton Woods ; excédents OPEP d’environ 450 milliards de "
        "dollars de 1974 à 1981 ; dette latino-américaine de 75 milliards en 1975 à "
        "315 en 1983 ; inflation française de 14 % au début de 1982 à environ 2 % au "
        "début des années 1990 ; taux de marge de 25 % en 1985 à 32 % en 1989 ; "
        "chômage français d’environ 8 % en 1982 à 12 % en 1998."},
 ],
}

METHODE = (
 '<div class="nb"><h2>✏️ Méthode — Deuxième année, chapitre 6</h2>'
 '<h3>Réflexes de copie</h3><ul>'
 '<li><strong>Annoncer le sens de cotation</strong> : en cotation au certain, une '
 'hausse du taux est une appréciation de la monnaie nationale ; à l’incertain, '
 'c’est l’inverse. Une copie qui ne le précise pas rend ses propres mécanismes '
 'illisibles.</li>'
 '<li><strong>Distinguer les quatre mots</strong> : dépréciation et appréciation '
 'décrivent le marché, dévaluation et réévaluation une décision officielle en '
 'régime administré. L’erreur est si fréquente qu’elle se repère immédiatement.</li>'
 '<li><strong>Séparer déterminants réels et déterminants financiers</strong> : les '
 'premiers — prix, inflation, compétitivité — expliquent le long terme ; les '
 'seconds — taux d’intérêt, capitaux, anticipations — dominent le court terme. '
 'C’est le plan le plus solide pour un sujet sur la formation du change.</li>'
 '<li><strong>Ne jamais conclure d’une dévaluation à une amélioration du '
 'solde</strong> : poser la condition de Marshall-Lerner, la courbe en J, le '
 'comportement de marge et la capacité de l’appareil productif à substituer des '
 'productions nationales aux importations.</li>'
 '<li><strong>Le triangle de Mundell comme fil historique</strong> : Bretton Woods '
 'renonce à la mobilité des capitaux, le système post-1971 à la stabilité des '
 'changes, la zone euro à l’autonomie monétaire nationale. Trois systèmes, trois '
 'renoncements.</li>'
 '<li><strong>Toujours préciser pour qui</strong> : un même niveau de change ne '
 'convient pas à la fois aux exportateurs, aux importateurs de matières premières, '
 'aux ménages et aux débiteurs en devises. « Un bon taux de change » n’existe pas '
 'sans désignation d’un agent.</li></ul>'
 '<h3>Trois plans types</h3><ul>'
 '<li><strong>« Les taux de change reflètent-ils les fondamentaux '
 'économiques ? »</strong> I. À long terme, prix et compétitivité commandent le '
 'change (PPA, Cassel, PPA relative) — II. La financiarisation du Forex donne le '
 'premier rôle aux capitaux et aux anticipations — III. L’écart persistant entre '
 'change observé et fondamentaux nourrit l’instabilité et justifie les '
 'interventions.</li>'
 '<li><strong>« Un euro fort est-il dans l’intérêt d’une Europe forte ? »</strong> '
 'I. Une monnaie forte protège du renchérissement importé et importe de la '
 'crédibilité — II. Elle pèse sur la compétitivité-prix et sur la demande, comme '
 'le montre le franc fort — III. Son effet dépend de la spécialisation : une '
 'union monétaire hétérogène n’a pas de taux de change optimal commun.</li>'
 '<li><strong>« Faut-il choisir son régime de change ? »</strong> I. Le choix est '
 'une prérogative souveraine, déclarée au FMI — II. Il est contraint par '
 'l’endettement en devises, l’inflation et la peur du flottement — III. Le '
 'triangle de Mundell montre qu’il s’agit moins d’un choix que d’un arbitrage '
 'entre objectifs incompatibles.</li></ul>'
 '<h3>Phrases à réutiliser</h3><ul>'
 '<li>« Le taux de change est un prix relatif : aucun pays ne peut déprécier sa '
 'monnaie sans qu’un autre voie la sienne s’apprécier, ce qui rend toute guerre '
 'des monnaies collectivement perdante. »</li>'
 '<li>« Ce n’est pas la baisse du change qui corrige un déficit commercial, c’est '
 'la réaction des volumes échangés : la dévaluation ne vaut que ce que valent les '
 'élasticités. »</li>'
 '<li>« La peur du flottement rappelle qu’un régime de change n’est pas une '
 'doctrine mais une contrainte : une économie endettée en dollars ne choisit pas '
 'librement de laisser flotter sa monnaie. »</li></ul></div>')
