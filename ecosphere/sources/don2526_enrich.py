# -*- coding: utf-8 -*-
"""Chapitres 5 et 6 de 2e annee dans les sujets deja presents.

ENRICH : complement a la rubrique « Chapitres a mobiliser ». Une seule entree
         par sujet : lorsque les deux chapitres sont pertinents, les deux
         apports sont reunis dans la meme mention.
ARGS   : arguments ajoutes au corrige, uniquement la ou les nouveaux chapitres
         apportent un raisonnement que le sujet ne contenait pas.
"""

ENRICH = {
 # ---- Chapitre 1 : agents, revenus et politiques budgetaires ------------
 'ch1-1':  "2ᵉ année ch. 5 (fonction de consommation C = C₀ + cY, propension marginale à consommer, hypothèse du revenu permanent de Friedman 1957)",
 'ch1-2':  "2ᵉ année ch. 5 (investissement et débouchés anticipés, effet d’éviction, courbe IS, trappe à liquidité) · 2ᵉ année ch. 6 (effet de levier et effet de massue, taux d’intérêt réel)",
 'ch1-3':  "2ᵉ année ch. 5 (équivalence ricardienne de Barro 1974, effet d’éviction, critères de Maastricht et Pacte de stabilité de 1997)",
 'ch1-4':  "2ᵉ année ch. 5 (multiplicateurs budgétaires kG = 5, kF = 4, kT = − 4 avec c = 0,8 ; contrainte de financement et équivalence ricardienne)",
 'ch1-7':  "2ᵉ année ch. 5 (redistribution verticale et propension marginale à consommer : 95 contre 60 de consommation initiale selon le ménage ciblé)",
 'ch1-9':  "2ᵉ année ch. 5 (multiplicateur et fuites, critique monétariste et borne du potentiel) · 2ᵉ année ch. 6 (inflation importée et pouvoir d’achat)",
 'ch1-10': "2ᵉ année ch. 5 (multiplicateur de Kahn 1931 et Keynes 1936 : l’investissement engendre l’épargne, 100 d’épargne pour s = 0,2 et ΔY = 500)",
 'ch1-11': "2ᵉ année ch. 5 (I = S comme identité ex post, critique post-keynésienne, l’épargne comme fuite du multiplicateur)",
 'ch1-12': "2ᵉ année ch. 5 (multiplicateur des prestations kF = 4, ciblage des ménages à forte propension à consommer, revenu permanent de Friedman)",
 'ch1-13': "2ᵉ année ch. 5 (effet d’éviction, équivalence ricardienne, critères de Maastricht 3 % et 60 %, Pacte de stabilité de 1997)",
 'ch1-14': "2ᵉ année ch. 5 (kF = c / (1 − c) = 4, revenu permanent et transferts temporaires, ciblage de la relance)",
 'ch1-15': "2ᵉ année ch. 5 (multiplicateur et austérité, policy mix Clinton-Greenspan : solde de − 4,5 % à + 0,8 % du PIB entre 1992 et 1998 sans récession)",
 'ch1-16': "2ᵉ année ch. 5 (l’investissement dépend des débouchés anticipés et non des seuls profits) · 2ᵉ année ch. 6 (échec relatif du théorème de Schmidt, taux de marge de 25 % en 1985 à 32 % en 1989)",
 'ch1-17': "2ᵉ année ch. 5 (effet d’éviction, stabilisateurs automatiques, nuance sur les seuils de Maastricht)",
 'ch1-20': "2ᵉ année ch. 5 (prestations sociales comme instrument conjoncturel, kF = 4, stabilisateurs automatiques)",
 # ---- Chapitre 2 : monnaie, financement, politique monetaire ------------
 'ch2-3':  "2ᵉ année ch. 5 (courbe LM, préférence pour la liquidité, trappe à liquidité et limites du canal conventionnel) · 2ᵉ année ch. 6 (triangle de Mundell, autonomie monétaire)",
 'ch2-4':  "2ᵉ année ch. 6 (stablecoins adossés au dollar, 1 stablecoin ≈ 1 dollar, monnaies numériques de banque centrale, GENIUS Act de juillet 2025)",
 'ch2-5':  "2ᵉ année ch. 5 (dichotomie classique, préférence pour la liquidité, critique monétariste : prix ↑ → offre réelle de monnaie ↓ → LM à gauche → retour à YPE) · 2ᵉ année ch. 6 (inflation importée, taux de change réel)",
 'ch2-6':  "2ᵉ année ch. 5 (critique monétariste au plein emploi, chômage naturel de Friedman 1968, modèle OG-DG) · 2ᵉ année ch. 6 (dépréciation et inflation importée)",
 'ch2-7':  "2ᵉ année ch. 5 (policy mix et coordination, réunification allemande : taux courts de 4,3 % en 1988 à 9,2 % en 1991) · 2ᵉ année ch. 6 (cible d’inflation proche de 2 % et autonomie monétaire)",
 'ch2-8':  "2ᵉ année ch. 5 (modèle OG-DG, chocs d’offre, stagflation de 1975 : inflation de 11,7 % en France avec une croissance de − 1,0 %) · 2ᵉ année ch. 6 (inflation importée et effets de second tour)",
 'ch2-11': "2ᵉ année ch. 6 (stablecoins comme source de demande privée de dollars, risque de perte de parité, MNBC, GENIUS Act de juillet 2025)",
 'ch2-12': "2ᵉ année ch. 5 (trappe à liquidité, réhabilitation d’IS-LM après 2008, Mundell-Fleming : monnaie neutralisée en changes fixes) · 2ᵉ année ch. 6 (peur du flottement de Calvo et Reinhart 2002)",
 'ch2-13': "2ᵉ année ch. 5 (trappe à liquidité : LM horizontale, effet d’éviction nul, efficacité maximale de la politique budgétaire)",
 'ch2-15': "2ᵉ année ch. 5 (asymétrie institutionnelle de la zone euro : monnaie unique, budgets nationaux encadrés, budget commun d’un peu plus de 1 % du RNB) · 2ᵉ année ch. 6 (SME 1979-1993, crises de 1992-1993, euro 1999 comme réponse au triangle de Mundell)",
 'ch2-16': "2ᵉ année ch. 6 (crises de change et anticipations autoréalisatrices, choc Volcker, crise mexicaine de 1982, dette latino-américaine de 75 à 315 milliards de dollars entre 1975 et 1983)",
 'ch2-17': "2ᵉ année ch. 5 (effet d’éviction et accès au crédit) · 2ᵉ année ch. 6 (taux d’intérêt réels et bascule de l’effet de levier en effet de massue)",
 'ch2-19': "2ᵉ année ch. 6 (globalisation financière et arbitrage des entreprises entre placements financiers et investissement productif, limite du théorème de Schmidt)",
 'ch2-20': "2ᵉ année ch. 5 (courbe de Phillips de 1958 et sa reformulation par Lipsey puis Samuelson et Solow en 1960, loi d’Okun, OG-DG) · 2ᵉ année ch. 6 (désinflation compétitive : inflation de 14 % à 2 %, chômage de 8 % en 1982 à 12 % en 1998)",
 # ---- Chapitre 3 : histoire de la pensee --------------------------------
 'ch3-1':  "2ᵉ année ch. 5 (tâtonnement walrasien, équilibre de sous-emploi keynésien, ajustement par les quantités plutôt que par les prix)",
 'ch3-2':  "2ᵉ année ch. 5 (demande effective, multiplicateur, trois critiques de la relance : éviction, revenu permanent, équivalence ricardienne)",
 'ch3-3':  "2ᵉ année ch. 5 (dichotomie classique, marché des fonds prêtables, chômage classique de Pigou 1933, loi des débouchés de Say)",
 'ch3-4':  "2ᵉ année ch. 5 (demande effective et équilibre de sous-emploi, préférence pour la liquidité, formalisation IS-LM par Hicks 1937 et Hansen 1941)",
 'ch3-7':  "2ᵉ année ch. 5 (Harrod-Domar contre Solow : mêmes objets, hypothèses différentes, conclusions opposées ; idéal-type de Weber)",
 'ch3-9':  "2ᵉ année ch. 5 (loi des débouchés de Say et sa réfutation par la demande effective)",
 'ch3-10': "2ᵉ année ch. 5 (un modèle est un idéal-type au sens de Weber : il se juge à sa capacité d’expliquer sous ses hypothèses, non à son réalisme)",
 'ch3-11': "2ᵉ année ch. 5 (critique monétariste, chômage naturel, équivalence ricardienne, basculement vers les politiques structurelles) · 2ᵉ année ch. 6 (quatre arguments flexibilistes de Friedman 1953 et leurs limites)",
 'ch3-14': "2ᵉ année ch. 5 (réhabilitation d’IS-LM après 2008, trappe à liquidité, ni efficacité ni inefficacité systématiques des politiques de demande)",
 'ch3-17': "2ᵉ année ch. 5 (Walras et le tâtonnement, optimum de Pareto et sa mise en garde sur l’équité, chômage classique de Pigou)",
 'ch3-19': "2ᵉ année ch. 5 (l’optimum de Pareto ne dit rien de l’équité ; redistribution verticale comme instrument d’efficacité macroéconomique)",
 # ---- Chapitre 5 : defaillances -----------------------------------------
 'ch5-7':  "2ᵉ année ch. 5 (l’équilibre de sous-emploi comme défaillance macroéconomique que la flexibilité des prix ne corrige pas)",
 'ch5-9':  "2ᵉ année ch. 5 (délais de diagnostic et risque de politique procyclique, production potentielle non observable)",
 # ---- Chapitre 6 : croissance -------------------------------------------
 'ch6-1':  "2ᵉ année ch. 5 (distinction conjoncturel / structurel, croissance potentielle, Romer 1986 et Barro 1990)",
 'ch6-4':  "2ᵉ année ch. 6 (limites du théorème de Schmidt : taux d’intérêt réels, globalisation financière, débouchés anticipés)",
 'ch6-5':  "2ᵉ année ch. 5 (stagnation séculaire de Hansen, trappe à liquidité et réhabilitation d’IS-LM après 2008)",
 'ch6-14': "2ᵉ année ch. 6 (désindustrialisation et substituabilité des importations : sans substitut national, une dévaluation ne réduit pas les volumes importés)",
 'ch6-15': "2ᵉ année ch. 5 (comparaison Harrod-Domar / Solow : les conclusions d’un modèle dépendent de ses hypothèses)",
 'ch6-18': "2ᵉ année ch. 5 (Romer 1986 : externalités de connaissance et croissance potentielle) · 2ᵉ année ch. 6 (monnaie forte et incitation à la montée en gamme)",
 'ch6-19': "2ᵉ année ch. 5 (politiques structurelles : Romer 1986, Barro 1990 sur les infrastructures publiques productives)",
 # ---- Chapitre 7 : developpement ----------------------------------------
 'ch7-6':  "2ᵉ année ch. 6 (compétitivité-prix et compétitivité hors prix : une politique de change n’atteint pas la gamme)",
 'ch7-10': "2ᵉ année ch. 5 (effet d’éviction, équivalence ricardienne, investissement public et croissance potentielle chez Barro 1990)",
 'ch7-14': "2ᵉ année ch. 6 (peur du flottement des économies émergentes, endettement en devises et effet de bilan, accumulation de réserves)",
 # ---- Chapitre 1 de 2e annee : mondialisation ---------------------------
 'ch21-3':  "2ᵉ année ch. 5 (courbe BP et balance globale, dilemmes interne-externe, lecture de Généreux 2016 par Ype et YBTC) · 2ᵉ année ch. 6 (condition de Marshall-Lerner, courbe en J)",
 'ch21-10': "2ᵉ année ch. 5 (la balance globale, et non le seul solde courant : un excédent courant de 100 avec 140 de sorties de capitaux donne − 40) · 2ᵉ année ch. 6 (déterminants réels du change)",
 'ch21-11': "2ᵉ année ch. 5 (courbe BP, dilemmes de politique économique, règle d’affectation de Mundell) · 2ᵉ année ch. 6 (crise mexicaine de 1982, dette latino-américaine, peur du flottement)",
 'ch21-15': "2ᵉ année ch. 5 (trois D de Bourguinat, horizontalisation de BP, triangle des incompatibilités) · 2ᵉ année ch. 6 (choc Volcker, effet de bilan, Calvo et Reinhart 2002)",
 'ch21-17': "2ᵉ année ch. 5 (argument protectionniste tiré du multiplicateur ouvert 1 / (1 − c + m), et ses contreparties)",
 'ch21-18': "2ᵉ année ch. 6 (accusation de sous-évaluation du yuan et nuance du cours : l’évaluation du niveau d’équilibre d’une monnaie est complexe)",
 'ch21-19': "2ᵉ année ch. 6 (euro et autonomie financière européenne, compétitivité hors prix, intérêt européen possible d’une dépréciation du dollar)",
 'ch21-20': "2ᵉ année ch. 5 (triangle des incompatibilités, Mundell-Fleming : l’instrument efficace dépend du régime de change) · 2ᵉ année ch. 6 (quatre moments du SMI selon Jean-Marc Daniel 2015)",
 # ---- Chapitre 2 de 2e annee : FMN, competitivite -----------------------
 'ch22-9':  "2ᵉ année ch. 6 (taux de change effectif réel, compétitivité-prix et hors prix, Allemagne et France au début des années 2000) · 2ᵉ année ch. 5 (contrainte extérieure et YBTC)",
 'ch22-10': "2ᵉ année ch. 6 (désinflation compétitive : inflation de 14 % à 2 %, taux de marge de 25 % en 1985 à 32 % en 1989, croissance de 2 % contre 3 % dans l’OCDE)",
 'ch22-11': "2ᵉ année ch. 6 (taux d’intérêt comme instrument de change, et son coût interne sur le crédit et l’activité)",
 'ch22-13': "2ᵉ année ch. 5 (politiques structurelles et croissance potentielle, Barro 1990 sur les infrastructures publiques)",
 # ---- Chapitre 3 de 2e annee : commerce international -------------------
 'ch23-4':  "2ᵉ année ch. 6 (désindustrialisation et substituabilité des importations, comportement de marge, compétitivité hors prix)",
 'ch23-6':  "2ᵉ année ch. 6 (dévaluation compétitive et condition de Marshall-Lerner : + 4,6 avec des élasticités de 0,8 et 0,6, − 4,8 avec 0,3 et 0,2)",
 'ch23-8':  "2ᵉ année ch. 6 (doctrine Miran de novembre 2024, contradiction entre droits de douane et volonté de déprécier le dollar)",
 'ch23-13': "2ᵉ année ch. 5 (multiplicateur ouvert 1 / (1 − c + m), de 5 à 2 : limiter les importations pour limiter les fuites, et ses contreparties)",
 'ch23-16': "2ᵉ année ch. 6 (guerre des monnaies et sa limite fondamentale : les taux étant relatifs, tous ne peuvent pas déprécier ensemble)",
 'ch23-17': "2ᵉ année ch. 5 (coordination des relances, effets de débordement et tentation du passager clandestin) · 2ᵉ année ch. 6 (guerre des monnaies, accords du Plaza de 1985 et du Louvre de 1987)",
 'ch23-18': "2ᵉ année ch. 6 (encadrement des dévaluations sous Bretton Woods : parité cumulée au-delà de 10 % soumise au FMI)",
 # ---- Chapitre 4 de 2e annee : gouvernance ------------------------------
 'ch24-4':  "2ᵉ année ch. 5 (interdépendance des politiques conjoncturelles, effets de débordement et effets de retour)",
 'ch24-9':  "2ᵉ année ch. 6 (guerre des monnaies, intérêts divergents des grandes puissances face au projet d’accords de Mar-a-Lago)",
 'ch24-10': "2ᵉ année ch. 6 (accords du Plaza de septembre 1985 et du Louvre de février 1987, lignes de swap entre banques centrales, rôle international du dollar)",
 'ch24-11': "2ᵉ année ch. 6 (euro comme réponse au triangle de Mundell, autonomie financière européenne) · 2ᵉ année ch. 5 (budget commun d’un peu plus de 1 % du RNB)",
 'ch24-12': "2ᵉ année ch. 5 (coordination des relances comme bien public : coût national, bénéfice partiellement exporté, passager clandestin)",
 'ch24-13': "2ᵉ année ch. 6 (politique de change et ses trois instruments, doctrine Miran, retour de la monnaie comme levier de puissance)",
}

ARGS = [
 {'id': 'ch1-10', 'part': 1, 'args': [
  "Le mécanisme est quantifiable : avec une propension marginale à consommer de 0,8, une dépense initiale de 100 engendre 100, puis 80, puis 64, puis 51,2 de revenus, soit 500 au total — le multiplicateur vaut 1 / (1 − c) = 5.",
  "Et le résultat théorique est décisif : avec s = 0,2 et ΔY = 500, l’épargne engendrée atteint exactement 100, soit l’investissement initial. L’investissement n’exige donc pas une épargne préalable équivalente, il la produit.",
 ]},
 {'id': 'ch1-11', 'part': 1, 'args': [
  "L’égalité I = S doit être maniée avec précision : elle résulte du rapprochement de Y = C + I et de Y = C + S, et c’est une identité comptable ex post, non une relation de causalité.",
  "La critique post-keynésienne le souligne : ex ante, l’épargne désirée et l’investissement désiré sont décidés par des agents différents et peuvent parfaitement différer, l’écart se résorbant par les variations de stocks, du revenu et de l’emploi.",
 ]},
 {'id': 'ch1-13', 'part': 2, 'args': [
  "Trois canaux distincts limitent l’effet d’une relance financée par la dette, et il faut les séparer : l’effet d’éviction porte sur l’investissement, le revenu permanent de Friedman (1957) sur la consommation, l’équivalence ricardienne de Barro (1974) sur le financement.",
  "Mais Barro lui-même montre en 1990 que les infrastructures publiques productives soutiennent la croissance de long terme : critiquer la relance conjoncturelle n’équivaut pas à condamner tout endettement public.",
 ]},
 {'id': 'ch2-5', 'part': 2, 'args': [
  "La démonstration monétariste est graphique : au plein emploi, la relance déplace IS vers la droite, la hausse des prix réduit l’offre réelle de monnaie, LM se déplace vers la gauche, le taux d’intérêt monte et l’économie retrouve exactement YPE.",
  "La monnaie n’est donc pas neutre au même titre selon l’horizon : non neutre à court terme en situation de sous-emploi, par la préférence pour la liquidité et le canal du taux d’intérêt, elle le redevient largement à long terme au voisinage du potentiel.",
 ]},
 {'id': 'ch2-12', 'part': 2, 'args': [
  "La trappe à liquidité en fournit le cas limite : les taux étant très bas, toute monnaie supplémentaire est thésaurisée, LM devient horizontale et le canal conventionnel est bloqué — le cours précise que c’est ce canal, et non toute action monétaire.",
  "Le régime de change ajoute une seconde borne : en changes fixes avec mobilité parfaite des capitaux, une expansion monétaire est intégralement neutralisée par la défense de la parité, tandis qu’en changes flexibles elle est amplifiée par la dépréciation.",
 ]},
 {'id': 'ch2-15', 'part': 2, 'args': [
  "L’architecture est asymétrique : la politique monétaire est unique et conduite par la BCE, les politiques budgétaires restent nationales mais encadrées — 3 % de déficit et 60 % de dette depuis Maastricht, Pacte de stabilité de 1997 — et le budget commun représente un peu plus de 1 % du revenu national brut de l’Union.",
  "L’euro constitue pourtant une réponse cohérente au triangle de Mundell : les membres préservent la stabilité monétaire interne et la libre circulation des capitaux en transférant leur souveraineté monétaire, après l’échec du SME que les crises de 1992-1993 avaient sanctionné.",
 ]},
 {'id': 'ch2-20', 'part': 1, 'args': [
  "L’attribution doit être exacte : Phillips établit en 1958 une relation entre le chômage et la variation des salaires nominaux au Royaume-Uni ; la reformulation en arbitrage inflation-chômage vient de Lipsey, puis de Samuelson et Solow en 1960.",
  "C’est cette reformulation que la stagflation invalide : en 1975, la croissance est de − 1,0 % en France, − 0,9 % en Allemagne et − 0,2 % aux États-Unis, avec des inflations de 11,7 %, 5,9 % et 9,1 %.",
 ]},
 {'id': 'ch3-4', 'part': 1, 'args': [
  "La rupture porte sur la causalité : c’est la demande effective — celle que les entrepreneurs anticipent — qui détermine la production et l’emploi, de sorte que l’économie peut s’équilibrer durablement en sous-emploi.",
  "Elle porte aussi sur le taux d’intérêt, qui cesse d’équilibrer l’épargne et l’investissement pour devenir le prix de la renonciation à la liquidité, déterminé sur le marché monétaire : c’est ce que la courbe LM formalisera.",
 ]},
 {'id': 'ch3-7', 'part': 2, 'args': [
  "La démonstration la plus économique est la comparaison de deux modèles du même objet : chez Harrod et Domar, rien ne garantit que la demande suive les capacités et la croissance est instable ; chez Solow, les rendements décroissants du capital conduisent à un état stationnaire.",
  "Les hypothèses commandent donc les conclusions, ce qui ne rend aucun des deux modèles faux : un modèle est un idéal-type au sens de Weber, et sa pertinence se juge à sa capacité d’expliquer dans le cadre de ses hypothèses.",
 ]},
 {'id': 'ch3-14', 'part': 3, 'args': [
  "La crise de 2008 a réhabilité le modèle IS-LM, précisément parce qu’il représente la trappe à liquidité : près du plancher des taux, l’expansion monétaire conventionnelle perd son efficacité tandis que l’effet d’éviction d’une relance budgétaire devient très limité.",
  "Le cours en tire une conclusion mesurée : les politiques de demande ne sont ni systématiquement efficaces ni systématiquement inefficaces, leur pertinence dépend du contexte macroéconomique — ce qui déplace le débat de la doctrine vers le diagnostic.",
 ]},
 {'id': 'ch21-3', 'part': 1, 'args': [
  "La mesure pertinente est la balance globale, somme du solde courant et des mouvements autonomes de capitaux : un excédent courant de 100 accompagné de sorties de capitaux de 140 donne une balance globale déficitaire de 40.",
  "Un déficit n’est donc un problème qu’au regard de son financement : la courbe BP rassemble les couples de revenu et de taux d’intérêt qui l’assurent, et sa pente diminue à mesure que la mobilité des capitaux augmente.",
 ]},
 {'id': 'ch21-11', 'part': 2, 'args': [
  "Deux configurations seulement constituent de véritables dilemmes : sous-emploi avec déficit extérieur, et tensions inflationnistes avec excédent extérieur. Dans les deux autres, une même orientation corrige les deux déséquilibres.",
  "La France de 1981-1983 en fournit la démonstration : inflation d’environ 14 % au début de 1982, dégradation des transactions courantes, trois dévaluations subies en octobre 1981, juin 1982 et mars 1983, puis tournant de la rigueur.",
 ]},
 {'id': 'ch21-15', 'part': 2, 'args': [
  "Le choc Volcker en mesure le coût : à partir de 1979, la hausse des taux américains et l’appréciation du dollar portent la dette extérieure de l’Amérique latine d’environ 75 milliards de dollars en 1975 à 315 milliards en 1983, et son service de 12 à 66 milliards.",
  "D’où la peur du flottement établie par Calvo et Reinhart en 2002 : pour une économie endettée en devises, une dépréciation alourdit la dette par effet de bilan, de sorte que la flexibilité n’est pas une option neutre.",
 ]},
 {'id': 'ch22-10', 'part': 3, 'args': [
  "La désinflation compétitive française montre qu’une stratégie peut atteindre son objectif monétaire sans produire les effets réels attendus : l’inflation passe d’environ 14 % au début des années 1980 à environ 2 % au début des années 1990 et le taux de marge remonte de 25 % en 1985 à 32 % en 1989.",
  "Mais le théorème de Schmidt ne se vérifie pas : la désinflation porte le taux d’intérêt réel de − 4 % à + 8 % pour un taux nominal de 10 %, faisant basculer l’effet de levier en effet de massue, et la croissance reste proche de 2 % par an contre environ 3 % dans l’OCDE.",
 ]},
 {'id': 'ch23-6', 'part': 2, 'args': [
  "Une dévaluation n’améliore le solde commercial que si la condition de Marshall-Lerner est vérifiée : à partir d’exportations et d’importations de 100 et d’une dévaluation de 10 %, des élasticités de 0,8 et 0,6 donnent un solde de + 4,6, mais des élasticités de 0,3 et 0,2 le dégradent à − 4,8.",
  "S’y ajoutent la courbe en J, qui impose une dégradation initiale du solde, puis l’inflation importée, qui érode progressivement le gain : ce ne sont pas les prix affichés mais la réaction des volumes qui décide.",
 ]},
 {'id': 'ch23-17', 'part': 3, 'args': [
  "La dimension monétaire doit être intégrée : les taux de change étant des prix relatifs, tous les pays ne peuvent pas déprécier simultanément les uns par rapport aux autres, de sorte qu’une guerre des monnaies neutralise mutuellement les gains recherchés.",
  "La coopération est pourtant possible, mais réactive : les accords du Plaza de septembre 1985 organisent une baisse concertée du dollar, et ceux du Louvre de février 1987 cherchent à stabiliser les cours une fois la dépréciation jugée excessive.",
 ]},
 {'id': 'ch24-10', 'part': 2, 'args': [
  "Les accords du Plaza de septembre 1985 en fournissent l’illustration monétaire : cinq puissances — États-Unis, Japon, République fédérale d’Allemagne, France, Royaume-Uni — coordonnent leurs interventions pour organiser une baisse ordonnée du dollar.",
  "Mais la coopération a supposé une convergence d’intérêts : elle n’intervient qu’une fois l’appréciation devenue problématique pour l’économie américaine elle-même, ce qui explique que le projet contemporain d’« accords de Mar-a-Lago » bute sur des intérêts divergents.",
 ]},
 {'id': 'ch24-12', 'part': 2, 'args': [
  "La coordination des politiques conjoncturelles relève de la même logique d’action collective : la relance d’un pays stimule les exportations de ses partenaires, de sorte que le coût est national et le bénéfice partiellement exporté.",
  "D’où la tentation du passager clandestin — attendre que l’autre relance — et, si tous attendent, l’absence de relance suffisante : les importations des uns étant les exportations des autres, la coordination restitue collectivement le multiplicateur que chacun avait perdu.",
 ]},
]
