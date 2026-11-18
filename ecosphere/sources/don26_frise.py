# -*- coding: utf-8 -*-
"""Frise chronologique : items du chapitre 6 de deuxieme annee.

MAJ : items deja presents auxquels le chapitre 26 est ajoute.
NOUVEAUX : items ajoutes, tous adosses au document de cours.
"""

MAJ = {
 # auteurs déjà présents
 'a322': "Robert Mundell", 'a359': "Paul Volcker",
 'a250': "Dominique Plihon", 'a320': "Dominique Plihon",
 'a252': "Milton Friedman", 'a318': "Milton Friedman",
 'a211': "Paul Samuelson", 'c24_a04': "Bela Balassa",
 'a344': "Alfred Marshall", 'a332': "Abba Lerner",
 # événements et périodes déjà présents
 'f023': "Accords de Bretton Woods",
 'f028': "Microprocesseur et fin de la convertibilité dollar-or",
 'f032': "Second choc pétrolier et choc Volcker",
 'f042': "Création de l'euro",
}

C = "Taux de change et systèmes de change"
NOUVEAUX = []


def it(idn, type_, an, titre, resume, portee, fam, courant=C,
       auteur=None, fin=None, vivant=None, oeuvres=None):
    d = {'id': 'c26_' + idn, 'type': type_, 'an': an, 'titre': titre,
         'resume': resume, 'portee': portee, 'courant': courant,
         'ch': [26], 'fam': fam}
    if auteur:
        d['auteur'] = auteur
    if fin is not None:
        d['fin'] = fin
    if vivant is not None:
        d['vivant'] = vivant
    if oeuvres:
        d['oeuvres'] = oeuvres
    NOUVEAUX.append(d)


# ------------------------------------------------------------------ auteurs
it('a01', 'auteur', 1866, "Gustav Cassel",
   "Développe en 1918 la théorie de la parité des pouvoirs d’achat : à long terme, le taux de change doit égaliser le pouvoir d’achat des monnaies.",
   "Cassel fournit la référence de long terme du change : la PPA ne prédit pas le cours de demain, mais indique vers quoi il devrait tendre si seuls les prix comptaient.",
   'monetaire', courant="École de Stockholm", auteur="Gustav Cassel",
   fin=1945, vivant=False, oeuvres=["Théorie de la parité des pouvoirs d’achat (1918)"])
it('a02', 'auteur', 1918, "Helmut Schmidt",
   "Formule le théorème selon lequel les profits d’aujourd’hui sont les investissements de demain et les emplois d’après-demain.",
   "Le chapitre montre que cette transmission ne s’est pas réalisée en France malgré la restauration du taux de marge de 25 % en 1985 à 32 % en 1989.",
   'monetaire', courant="Politique économique", auteur="Helmut Schmidt",
   fin=2015, vivant=False, oeuvres=["Formule attribuée sur les profits, l’investissement et l’emploi"])
it('a03', 'auteur', 1941, "Guillermo Calvo",
   "Montre avec Carmen Reinhart, en 2002, que de nombreux pays officiellement flottants interviennent fortement pour limiter les variations de leur monnaie.",
   "La peur du flottement n’est pas une inconséquence : pour une économie endettée en devises, une dépréciation alourdit la dette par effet de bilan.",
   'monetaire', courant="Macroéconomie internationale", auteur="Guillermo Calvo",
   vivant=True, oeuvres=["« Fear of Floating », Quarterly Journal of Economics (2002)"])
it('a04', 'auteur', 1955, "Carmen Reinhart",
   "Établit avec Guillermo Calvo l’écart systématique entre les régimes de change officiellement déclarés et les pratiques effectives d’intervention.",
   "Impose de lire les classifications de régimes avec prudence : ce qu’un État déclare ne dit pas ce qu’il fait sur le marché des changes.",
   'monetaire', courant="Macroéconomie internationale", auteur="Carmen Reinhart",
   vivant=True, oeuvres=["« Fear of Floating », Quarterly Journal of Economics (2002)"])
it('a05', 'auteur', 1954, "Jean-Marc Daniel",
   "Écrit en 2015 que « le monde a accompli une sorte de parcours complet en essayant toutes les éventualités offertes par le triangle des incompatibilités de Robert Mundell ».",
   "Interdit toute lecture téléologique de l’histoire monétaire : aucun système successif n’était plus moderne qu’un autre, chacun répondait à un arbitrage différent.",
   'histoire', courant="Histoire de la pensée économique", auteur="Jean-Marc Daniel",
   vivant=True, oeuvres=["Travaux de 2015 sur l’histoire du système monétaire international"])
it('a06', 'auteur', 1983, "Stephen Miran",
   "Soutient, dans un rapport de novembre 2024, que la demande internationale d’actifs sûrs en dollars entretient une surévaluation pénalisant l’industrie américaine.",
   "La doctrine Miran envisage une dépréciation organisée du dollar, objectif en tension avec les instruments protectionnistes qui renchérissent les importations.",
   'monetaire', courant="Économie américaine contemporaine", auteur="Stephen Miran",
   vivant=True, oeuvres=["Rapport de novembre 2024 sur la réorganisation du système monétaire international"])

# ----------------------------------------------------------------- ouvrages
it('o01', 'ouvrage', 1918, "Théorie de la parité des pouvoirs d’achat",
   "Cassel fonde l’analyse du change sur la loi du prix unique : la PPA absolue détermine un taux d’équilibre, la PPA relative explique les variations par les écarts d’inflation.",
   "Référence de long terme du chapitre, dont les limites — coûts de transaction, biens non échangeables, productivité, capitaux — sont aussitôt énoncées.",
   'monetaire', courant="École de Stockholm", auteur="Gustav Cassel")
it('o02', 'ouvrage', 1953, "The Case for Flexible Exchange Rates",
   "Friedman défend la supériorité des changes flottants : le taux de change est un prix, qui doit être déterminé par l’offre et la demande.",
   "Quatre arguments : taux d’équilibre déterminé par le marché, spéculation stabilisatrice, ajustement automatique de la balance des paiements, insularisation des politiques.",
   'monetaire', courant="Monétariste", auteur="Milton Friedman")
it('o03', 'ouvrage', 1964, "Travaux de Balassa et Samuelson sur la productivité et les niveaux de prix",
   "Les écarts de productivité entre secteurs échangeables et non échangeables engendrent des différences durables de niveaux de prix entre pays.",
   "Explique pourquoi la PPA absolue échoue systématiquement entre pays de niveaux de développement différents : les prix ne convergent pas quand la productivité ne le fait pas.",
   'monetaire', courant="Économie internationale", auteur="Bela Balassa")
it('o04', 'ouvrage', 2002, "« Fear of Floating »",
   "Calvo et Reinhart montrent dans le Quarterly Journal of Economics que de nombreux pays émergents limitent les variations de leur monnaie tout en déclarant un flottement.",
   "Fonde la distinction entre régime de jure et régime de facto, et explique la prédominance persistante des régimes d’arrimage.",
   'monetaire', courant="Macroéconomie internationale", auteur="Guillermo Calvo")
it('o05', 'ouvrage', 2015, "Travaux de Jean-Marc Daniel sur l’histoire du système monétaire international",
   "L’histoire monétaire est lue comme une succession d’arbitrages entre les trois objectifs du triangle de Mundell.",
   "Fil conducteur historique du chapitre : Bretton Woods, flottement, SME, euro — chaque système se définit par le sommet qu’il sacrifie.",
   'histoire', courant="Histoire de la pensée économique", auteur="Jean-Marc Daniel")
it('o06', 'ouvrage', 2024, "Rapport Miran sur la réorganisation du système monétaire international",
   "Publié en novembre 2024, il soutient que la surévaluation du dollar, entretenue par la demande mondiale d’actifs sûrs, pénalise l’industrie manufacturière américaine.",
   "Origine du projet dit d’« accords de Mar-a-Lago », qui envisage une dépréciation coordonnée du dollar sur le modèle du Plaza.",
   'monetaire', courant="Économie américaine contemporaine", auteur="Stephen Miran")

# ----------------------------------------------------------------- théories
it('t01', 'theorie', 1918, "Parité des pouvoirs d’achat",
   "Version absolue : le taux de change égalise le prix d’un même panier. Version relative : les variations du change compensent les différentiels d’inflation.",
   "Exemple du cours : avec 6 % d’inflation dans la zone euro et 2 % aux États-Unis, l’euro devrait se déprécier d’environ 4 %. Référence de long terme uniquement.",
   'monetaire', courant="École de Stockholm", auteur="Gustav Cassel")
it('t02', 'theorie', 1953, "Les quatre arguments flexibilistes",
   "Le marché déterminerait le taux d’équilibre, la spéculation serait stabilisatrice, la balance des paiements s’ajusterait automatiquement, les politiques seraient insularisées.",
   "Chacun reçoit sa contre-épreuve : volatilité observée, spéculation déstabilisatrice en crise, déséquilibres persistants, et choc Volcker contre l’insularisation.",
   'monetaire', courant="Monétariste", auteur="Milton Friedman")
it('t03', 'theorie', 1964, "Effet Balassa-Samuelson",
   "La productivité élevée du secteur exposé permet des salaires élevés, diffusés par la mobilité du travail vers les secteurs abrités dont les prix s’élèvent.",
   "Les pays les plus productifs présentent donc durablement des niveaux de prix plus élevés sans que leur monnaie soit surévaluée : l’écart à la PPA est structurel.",
   'monetaire', courant="Économie internationale", auteur="Bela Balassa")
it('t04', 'theorie', 1965, "Condition de Marshall-Lerner",
   "Une dévaluation n’améliore le solde commercial que si la somme des élasticités-prix, en valeur absolue, dépasse l’unité : |εX| + |εM| > 1.",
   "Illustration du cours : une dévaluation de 10 % porte le solde à + 4,6 avec des élasticités de 0,8 et 0,6, mais le dégrade à − 4,8 avec 0,3 et 0,2.",
   'monetaire', courant="Économie internationale", auteur="Alfred Marshall")
it('t05', 'theorie', 1966, "Courbe en J",
   "Trois phases : domination des effets-prix à court terme et dégradation du solde ; apparition des effets-volume à moyen terme ; amélioration ou érosion des gains ensuite.",
   "Les effets bénéfiques d’une dévaluation ne sont donc jamais immédiats, et leur persistance dépend de l’inflation importée.",
   'monetaire', courant="Économie internationale")
it('t06', 'theorie', 1980, "Théorème de Schmidt",
   "Profits ↑ → autofinancement ↑ → investissement ↑ → capacités de production ↑ → emploi ↑.",
   "Trois limites en France : taux d’intérêt réels élevés faisant basculer le levier en massue, globalisation financière offrant des placements concurrents, débouchés anticipés insuffisants.",
   'monetaire', courant="Politique économique", auteur="Helmut Schmidt")
it('t07', 'theorie', 1983, "Désinflation compétitive et cercle vertueux de la monnaie forte",
   "Monnaie forte → prix à l’importation ↓ → pression concurrentielle ↑ → productivité et compétitivité hors prix ↑ → solde extérieur ↑ → confiance ↑ → change soutenu.",
   "Stratégie inverse de la dévaluation : améliorer le taux de change réel par les prix internes plutôt que par la parité.",
   'monetaire', courant="Politique économique")
it('t08', 'theorie', 1983, "Cercle vicieux de la monnaie faible",
   "Dévaluation → inflation importée → effets de second tour sur les salaires → érosion du gain → déficit persistant → anticipations de dévaluation → nouvelle dévaluation.",
   "Les anticipations deviennent autoréalisatrices : les ventes massives épuisent les réserves et rendent la défense de la parité impossible. Exemple du peso argentin.",
   'monetaire', courant="Politique économique")
it('t09', 'theorie', 1985, "Effet de levier et effet de massue",
   "Levier : rentabilité économique (10 %) supérieure au coût réel de la dette (4 %). Massue : coût réel (8 %) supérieur à la rentabilité économique (5 %).",
   "La désinflation, en élevant le taux d’intérêt réel de − 4 % à + 8 % pour un taux nominal de 10 %, fait basculer d’un régime à l’autre et pousse au désendettement.",
   'monetaire', courant="Finance d’entreprise")
it('t10', 'theorie', 2002, "Peur du flottement",
   "De nombreux pays officiellement flottants interviennent fortement sur leur change, en raison de l’endettement en devises et du risque d’inflation importée.",
   "D’où la distinction entre régime de jure et régime de facto : en 2025, 117 pays pratiquent encore un arrimage ferme ou souple contre 66 en flottement.",
   'monetaire', courant="Macroéconomie internationale", auteur="Guillermo Calvo")
it('t11', 'theorie', 2024, "Doctrine Miran et paradoxe du dollar",
   "La demande internationale d’actifs sûrs en dollars entretiendrait une surévaluation pénalisant l’industrie américaine ; une dépréciation organisée est envisagée.",
   "Mais déprécier la monnaie de réserve mondiale réduit la valeur externe des placements en dollars et risque de miner la confiance : c’est le paradoxe du dollar.",
   'monetaire', courant="Économie américaine contemporaine", auteur="Stephen Miran")

# --------------------------------------------------------------- événements
it('e01', 'evenement', 1979, "Création du Système monétaire européen",
   "Le SME limite les fluctuations bilatérales entre monnaies européennes par des parités centrales assorties de bandes de ± 2 %.",
   "Tentative européenne de restaurer la fixité dans un monde de capitaux de plus en plus mobiles : les différentiels de taux d’intérêt y jouent un rôle central.",
   'institutionnel', courant="Europe monétaire")
it('e02', 'evenement', 1982, "Crise mexicaine et crise internationale de la dette",
   "Le Mexique révèle la vulnérabilité des économies endettées en dollars face aux décisions de la Fed : hausse des taux, appréciation du dollar, ralentissement mondial.",
   "Dette extérieure latino-américaine de 75 milliards de dollars en 1975 à 315 milliards en 1983 ; service de 12 à 66 milliards. L’autonomie promise par le flottement est démentie.",
   'mondialisation', courant="Finance internationale")
it('e03', 'evenement', 1983, "Tournant de la rigueur et politique du franc fort",
   "Mars 1983 : après trois dévaluations subies — octobre 1981, juin 1982, mars 1983 — la France renonce à la dévaluation et engage la désinflation compétitive.",
   "Résultats : inflation d’environ 14 % ramenée à environ 2 % au début des années 1990, redressement de la balance courante, taux de marge de 25 % en 1985 à 32 % en 1989.",
   'histoire', courant="Politique économique")
it('e04', 'evenement', 1985, "Accords du Plaza",
   "En septembre 1985, cinq puissances — États-Unis, Japon, RFA, France, Royaume-Uni — coordonnent leurs interventions pour organiser une baisse ordonnée du dollar.",
   "Le dollar s’était fortement apprécié depuis 1979 sous l’effet de la politique de Volcker et d’anticipations autoréalisatrices, creusant les déficits jumeaux américains.",
   'monetaire', courant="Coopération monétaire")
it('e05', 'evenement', 1987, "Accords du Louvre",
   "En février 1987, la dépréciation du dollar étant jugée excessive, les grandes puissances cherchent non plus à le faire baisser mais à stabiliser les cours.",
   "Avec le Plaza, ces accords montrent que les banques centrales peuvent intervenir collectivement dans un système de changes flottants.",
   'monetaire', courant="Coopération monétaire")
it('e06', 'evenement', 1993, "Crises du SME et élargissement des marges",
   "Les crises de 1992-1993 révèlent les contradictions des changes fixes européens : en août 1993, les marges de fluctuation sont élargies à ± 15 %.",
   "Dans un monde de capitaux mobiles, une parité fixe mais défendable devient intenable : l’échec de la voie intermédiaire prépare la monnaie unique.",
   'institutionnel', courant="Europe monétaire")
it('e07', 'evenement', 1998, "Chômage français au terme de la désinflation",
   "Le chômage passe d’environ 8 % de la population active en 1982 à environ 12 % en 1998, contre un ordre de grandeur de 7 % dans les autres pays de l’OCDE.",
   "Avec une croissance proche de 2 % par an contre environ 3 % dans l’OCDE, la stabilité monétaire a été obtenue sans retour rapide au plein emploi.",
   'histoire', courant="Politique économique")
it('e08', 'evenement', 2025, "GENIUS Act et stablecoins adossés au dollar",
   "En juillet 2025, les États-Unis adoptent un cadre fédéral encadrant les stablecoins de paiement, dont les émetteurs doivent détenir des actifs de réserve adaptés.",
   "Demande de stablecoins en dollars ↑ → demande privée de dollars et de bons du Trésor ↑ : un nouvel instrument de prolongation de la domination monétaire américaine.",
   'monetaire', courant="Monnaies numériques")
