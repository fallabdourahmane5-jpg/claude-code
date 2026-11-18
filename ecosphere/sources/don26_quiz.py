# -*- coding: utf-8 -*-
"""Quiz du chapitre 6 de deuxième année : taux de change et systèmes de change.

Chaque question est adossée au contenu du document de cours. Aucune donnée ni
attribution n'est ajoutée de mémoire.
"""

Q = []


def q(t, question, opts, ans, exp, tags):
    Q.append((t, question, opts, ans, exp, tags))


# ================================================================ QCM
q('qcm', "Une devise désigne :",
  ["Une monnaie étrangère", "Une monnaie convertible",
   "Une monnaie de réserve", "Un billet de banque centrale"], 0,
  "Bonne réponse : A. La devise est une monnaie étrangère, c’est-à-dire une monnaie considérée depuis un autre espace monétaire. La monnaie, elle, se définit comme une créance dotée d’un pouvoir libératoire général.",
  ['monnaie', 'devise'])
q('qcm', "Le pouvoir libératoire général de la monnaie signifie qu’elle :",
  ["Peut être échangée contre de l’or", "Permet d’éteindre une dette là où elle a cours légal",
   "Est acceptée dans le monde entier", "Est émise par la banque centrale"], 1,
  "Bonne réponse : B. C’est la définition retenue par le cours : la monnaie est une créance dotée d’un pouvoir libératoire général. La convertibilité, distincte, permet son utilisation internationale.",
  ['monnaie', 'définitions'])
q('qcm', "Dans le chapitre, le dollar remplit trois fonctions internationales :",
  ["Monnaie véhiculaire, unité de compte, réserve de valeur",
   "Monnaie d’ancrage, monnaie fiduciaire, monnaie scripturale",
   "Monnaie de réserve, monnaie unique, monnaie commune",
   "Étalon, numéraire, moyen de paiement national"], 0,
  "Bonne réponse : A. Monnaie véhiculaire — il sert d’intermédiaire dans des transactions qui ne concernent pas directement les États-Unis ; unité de compte — de nombreux contrats et matières premières sont libellés en dollars ; réserve de valeur internationale — les banques centrales en détiennent une part importante de leurs réserves.",
  ['dollar', 'SMI'])
q('qcm', "La cotation au certain exprime :",
  ["Le nombre d’unités de monnaie nationale pour une unité étrangère",
   "Le nombre d’unités de monnaie étrangère pour une unité de monnaie nationale",
   "Le taux de change à terme", "Le taux de change effectif"], 1,
  "Bonne réponse : B. Au certain, on indique combien d’unités étrangères on obtient pour une unité nationale. La cotation à l’incertain fait l’inverse.",
  ['cotation', 'définitions'])
q('qcm', "Le taux de change effectif nominal est :",
  ["Un taux bilatéral corrigé de l’inflation",
   "Une moyenne pondérée des taux bilatéraux selon le poids des partenaires",
   "Le taux de change d’équilibre de la PPA", "Le taux affiché par la banque centrale"], 1,
  "Bonne réponse : B. C’est l’approche multilatérale : un taux bilatéral ne dit rien de la position d’ensemble d’une monnaie. Dans l’exemple simplifié du cours, les pondérations retenues sont de 40 % pour les États-Unis, 35 % pour la Chine et 25 % pour le Royaume-Uni.",
  ['taux de change effectif', 'pondération'])
q('qcm', "Le taux de change réel mesure :",
  ["La valeur nominale d’une monnaie", "La compétitivité-prix relative",
   "Le rendement des placements en devises", "Le pouvoir d’achat intérieur de la monnaie"], 1,
  "Bonne réponse : B. En corrigeant le taux nominal par les niveaux de prix des deux économies, il indique le prix relatif des produits nationaux et étrangers : une monnaie stable nominalement peut perdre en compétitivité si l’inflation nationale dépasse celle de ses partenaires.",
  ['taux de change réel', 'compétitivité'])
q('qcm', "Une appréciation désigne :",
  ["Une hausse de la monnaie décidée par les autorités en changes fixes",
   "Une hausse de la monnaie résultant du marché",
   "Une hausse du taux d’intérêt directeur", "Une hausse du taux de change réel"], 1,
  "Bonne réponse : B. Le vocabulaire est strict : appréciation et dépréciation résultent du marché ; réévaluation et dévaluation sont des décisions des autorités en régime de changes fixes. La confusion est pénalisée.",
  ['vocabulaire', 'piège'])
q('qcm', "Dominique Plihon qualifie le marché des changes de :",
  ["Marché organisé", "Marché-réseau", "Marché de détail", "Marché réglementé"], 1,
  "Bonne réponse : B. Il ne repose pas sur une place physique unique : les intervenants échangent par réseaux électroniques et intermédiaires spécialisés, ce qui lui donne une dimension mondiale et un fonctionnement quasi continu.",
  ['Plihon', 'marché des changes'])
q('qcm', "Sur le marché des changes, l’arbitrage a pour effet de :",
  ["Accroître la volatilité", "Unifier les cotations",
   "Fixer la parité centrale", "Réduire les volumes échangés"], 1,
  "Bonne réponse : B. Un même couple de monnaies ne peut pas durablement s’échanger à deux prix différents : les opérateurs exploiteraient immédiatement l’écart, ce qui le referme.",
  ['arbitrage', 'Forex'])
q('qcm', "Le Forex est principalement :",
  ["Un marché de détail animé par les ménages",
   "Un marché de gros dominé par les institutions financières",
   "Un marché interbancaire limité à la zone euro",
   "Un marché contrôlé par le FMI"], 1,
  "Bonne réponse : B. Les banques y jouent un rôle central, rejointes par la montée des investisseurs institutionnels. Le marché est en outre dominé par le dollar.",
  ['Forex', 'acteurs'])
q('qcm', "Le développement spectaculaire du marché des changes révèle :",
  ["La croissance du commerce de marchandises",
   "La financiarisation de l’économie mondiale et une déconnexion entre transactions financières et échanges réels",
   "L’élargissement de la zone euro", "La fin des régimes d’ancrage"], 1,
  "Bonne réponse : B. Trois mécanismes l’expliquent selon le cours : l’essor du commerce international, la multiplication des produits dérivés et l’intensification des opérations financières. La structure des transactions confirme cette financiarisation.",
  ['financiarisation', 'Forex'])
q('qcm', "La couverture et la spéculation se distinguent par :",
  ["Le montant des opérations", "L’attitude face au risque de change",
   "Le type d’intervenant", "La durée des contrats"], 1,
  "Bonne réponse : B. La couverture vise à réduire l’exposition au risque de change ; la spéculation consiste à l’accepter dans l’espoir d’un gain. Les mêmes instruments — options, swaps, opérations à terme — servent les deux logiques.",
  ['couverture', 'spéculation'])
q('qcm', "En période calme, la spéculation peut stabiliser le taux de change parce que les opérateurs :",
  ["Anticipent la poursuite de la tendance",
   "Forment des anticipations de retour à la moyenne",
   "Suivent les consignes de la banque centrale",
   "Se couvrent systématiquement à terme"], 1,
  "Bonne réponse : B. Ils achètent une monnaie jugée sous-évaluée et vendent une monnaie jugée surévaluée, ce qui ramène le cours vers sa valeur de référence.",
  ['spéculation stabilisatrice', 'anticipations'])
q('qcm', "En période de crise, la spéculation peut amplifier les déséquilibres parce que les anticipations deviennent :",
  ["Des anticipations de retour à la moyenne",
   "Des anticipations de poursuite de la tendance",
   "Des anticipations adaptatives sur les prix",
   "Des anticipations d’inflation"], 1,
  "Bonne réponse : B. Les ventes alimentent alors la baisse qu’elles anticipaient. Le cours en tire une conclusion décisive : le marché des changes peut être simultanément stabilisateur et déstabilisateur.",
  ['spéculation déstabilisatrice', 'anticipations'])
q('qcm', "Dans le chapitre, les exportations d’un pays :",
  ["Accroissent l’offre de monnaie nationale", "Accroissent la demande de monnaie nationale",
   "Sont sans effet sur le change", "Font baisser le taux de change réel"], 1,
  "Bonne réponse : B. L’acheteur étranger doit se procurer la monnaie nationale pour régler sa facture. Symétriquement, les importations accroissent l’offre de monnaie nationale.",
  ['déterminants', 'balance des paiements'])
q('qcm', "La théorie de la parité des pouvoirs d’achat est développée par Gustav Cassel en :",
  ["1906", "1918", "1936", "1953"], 1,
  "Bonne réponse : B. Cassel développe en 1918 la théorie de la parité des pouvoirs d’achat, dont la loi du prix unique constitue le fondement.",
  ['Cassel', 'PPA'])
q('qcm', "La loi du prix unique énonce que :",
  ["Un bien doit avoir le même prix dans toutes les régions d’un pays",
   "Un même bien devrait, après conversion, coûter le même prix dans deux économies",
   "Les prix augmentent au même rythme partout",
   "Un bien non échangeable a un prix unique"], 1,
  "Bonne réponse : B. Sinon des arbitrages s’enclencheraient. C’est le fondement de la PPA, dont la version absolue détermine un taux de change d’équilibre à partir des niveaux de prix.",
  ['loi du prix unique', 'PPA'])
q('qcm', "Dans l’exemple du cours, avec une inflation de 6 % dans la zone euro et de 2 % aux États-Unis, la PPA relative prévoit que l’euro :",
  ["S’apprécie d’environ 4 %", "Se déprécie d’environ 4 %",
   "Reste stable", "Se déprécie d’environ 8 %"], 1,
  "Bonne réponse : B. La PPA relative explique les variations du change par les différentiels d’inflation : l’économie la plus inflationniste voit sa monnaie se déprécier d’un montant correspondant à l’écart, soit environ 4 points ici.",
  ['PPA relative', 'inflation'])
q('qcm', "L’effet Balassa-Samuelson est attribué, dans le chapitre, à :",
  ["Cassel et Friedman", "Béla Balassa et Paul Samuelson, 1964",
   "Calvo et Reinhart, 2002", "Mundell et Fleming, 1963"], 1,
  "Bonne réponse : B. Le cours date explicitement cet apport de 1964 et l’attribue à Béla Balassa et Paul Samuelson.",
  ['Balassa-Samuelson', 'datation'])
q('qcm', "Selon l’effet Balassa-Samuelson, les pays les plus productifs peuvent présenter durablement :",
  ["Des monnaies sous-évaluées", "Des niveaux de prix plus élevés sans surévaluation de leur monnaie",
   "Des taux d’intérêt plus faibles", "Des excédents commerciaux structurels"], 1,
  "Bonne réponse : B. La productivité élevée du secteur exposé permet des salaires élevés, que la mobilité du travail diffuse vers les secteurs non échangeables dont la productivité progresse moins : leurs coûts puis leurs prix s’élèvent, et avec eux le niveau général des prix.",
  ['Balassa-Samuelson', 'PPA absolue'])
q('qcm', "Parmi les limites de la PPA retenues par le cours, ne figure PAS :",
  ["Les coûts de transaction", "L’existence de biens non échangeables",
   "Les mouvements de capitaux", "L’absence de monnaie de réserve internationale"], 3,
  "Bonne réponse : D. Le cours retient quatre limites : coûts de transaction, biens non échangeables, effet Balassa-Samuelson et mouvements de capitaux — ces derniers pouvant éloigner durablement le change de la PPA.",
  ['PPA', 'limites'])
q('qcm', "Un régime de change se définit comme :",
  ["Le niveau d’équilibre du taux de change",
   "Un ensemble de règles encadrant la détermination du taux de change",
   "La politique de la banque centrale sur les taux d’intérêt",
   "Le montant des réserves de change détenues"], 1,
  "Bonne réponse : B. Son choix relève de la souveraineté monétaire, et les régimes forment un continuum entre ancrage strict et flottement libre — non une alternative entre deux options.",
  ['régimes de change', 'définitions'])
q('qcm', "La caisse d’émission, ou currency board, est illustrée dans le cours par :",
  ["L’Équateur depuis 2000", "Le régime de convertibilité argentin de 1991 à 2002",
   "Le currency board de Hong Kong depuis 1983", "La dollarisation du Panama"], 1,
  "Bonne réponse : B. Le cours cite le régime de convertibilité argentin, en vigueur de 1991 à 2002, comme exemple de ce type d’ancrage rigide.",
  ['currency board', 'Argentine'])
q('qcm', "Dans un régime conventionnel de change fixe, il faut distinguer :",
  ["Le taux nominal et le taux réel", "La parité centrale et les bandes de fluctuation",
   "Le comptant et le terme", "L’ancrage ferme et l’ancrage souple"], 1,
  "Bonne réponse : B. La parité centrale est la référence officielle ; les bandes de fluctuation sont les marges autorisées autour d’elle. Dans le SME, ces marges sont de ± 2 %, élargies à ± 15 % en août 1993.",
  ['parité centrale', 'bandes de fluctuation'])
q('qcm', "Les marges de fluctuation du SME sont élargies à ± 15 % en :",
  ["Mars 1983", "Janvier 1979", "Août 1993", "Janvier 1999"], 2,
  "Bonne réponse : C. Cet élargissement intervient à la suite des crises du SME de 1992-1993, qui avaient révélé les contradictions des changes fixes européens dans un contexte de mobilité croissante des capitaux.",
  ['SME', 'chronologie'])
q('qcm', "Pour freiner une appréciation de sa monnaie, une banque centrale :",
  ["Vend des devises et achète sa monnaie", "Vend sa monnaie et achète des devises",
   "Relève son taux directeur", "Réduit ses réserves de change"], 1,
  "Bonne réponse : B. Elle fait l’inverse du marché. Le cours souligne que cette intervention est relativement facile, puisque la banque centrale peut créer sa propre monnaie — alors que la défense contre une dépréciation est limitée par ses réserves.",
  ['intervention', 'asymétrie'])
q('qcm', "Les accords du Plaza sont conclus en :",
  ["Février 1987", "Septembre 1985", "Août 1993", "Novembre 2024"], 1,
  "Bonne réponse : B. En septembre 1985, cinq grandes puissances — États-Unis, Japon, République fédérale d’Allemagne, France, Royaume-Uni — se réunissent à New York pour organiser une baisse ordonnée du dollar.",
  ['Plaza', 'chronologie'])
q('qcm', "L’appréciation du dollar au début des années 1980 s’explique principalement par :",
  ["Un excédent commercial américain",
   "La politique monétaire très restrictive de Paul Volcker et les anticipations des investisseurs",
   "Les accords du Louvre", "La dollarisation de plusieurs économies"], 1,
  "Bonne réponse : B. À partir de 1979, la Fed augmente fortement ses taux : les rendements en dollars montent, les capitaux affluent, la demande de dollars s’accroît. Les anticipations d’appréciation renforcent le mouvement de façon autoréalisatrice.",
  ['Volcker', 'dollar'])
q('qcm', "On parle de déficits jumeaux lorsqu’un pays connaît simultanément :",
  ["Un déficit public et un déficit extérieur courant",
   "Un déficit commercial et un déficit de la balance des capitaux",
   "Un déficit budgétaire et un déficit de la Sécurité sociale",
   "Un déficit courant et une inflation élevée"], 0,
  "Bonne réponse : A. Le cours mobilise cette notion pour les États-Unis du début des années 1980 : l’administration Reagan combine réductions d’impôts, dépenses militaires importantes et déficits budgétaires élevés, tandis que l’appréciation du dollar creuse le déficit commercial.",
  ['déficits jumeaux', 'États-Unis'])
q('qcm', "Les accords du Louvre de février 1987 visaient à :",
  ["Faire baisser davantage le dollar", "Stabiliser les taux de change après la forte dépréciation du dollar",
   "Créer l’euro", "Élargir les marges du SME"], 1,
  "Bonne réponse : B. Une fois la dépréciation du dollar jugée excessive, les grandes puissances cherchent non plus à le faire baisser mais à stabiliser les cours. Avec le Plaza, ces accords montrent que les banques centrales peuvent intervenir collectivement en changes flottants.",
  ['Louvre', 'coopération'])
q('qcm', "Une ligne de swap entre banques centrales désigne :",
  ["Un achat ou une vente de devises pour influencer le change",
   "Une fourniture temporaire de liquidités entre banques centrales",
   "Un prêt du FMI à un pays en difficulté",
   "Un contrat à terme sur devises"], 1,
  "Bonne réponse : B. Le cours insiste sur cette distinction : l’intervention de change est un achat ou une vente de devises ; la ligne de swap est une fourniture temporaire de liquidités, forme de coopération entre banques centrales.",
  ['swap', 'distinctions'])
q('qcm', "D’après les données de 2025 présentées dans le cours, les régimes de flottement concernent :",
  ["29 pays, soit 13 %", "88 pays, soit 46 %", "66 pays, soit 34 %", "13 pays, soit 7 %"], 2,
  "Bonne réponse : C. Répartition complète : arrimage ferme 29 pays (13 %), arrimage souple 88 pays (46 %), flottement 66 pays (34 %), autres ou non classés 13 pays (7 %). Les parts sont arrondies et la classification dépend des critères retenus.",
  ['chiffres', 'régimes de change'])
q('qcm', "Ce que montre la répartition des régimes de change en 2025 :",
  ["La généralisation du flottement libre",
   "Qu’une majorité de pays ne pratiquent pas un flottement totalement libre",
   "La disparition des régimes d’ancrage", "L’uniformisation des choix monétaires"], 1,
  "Bonne réponse : B. Les régimes d’arrimage — fermes et souples — restent particulièrement importants, pour des motifs variés : limiter l’inflation, sécuriser les échanges, protéger un endettement en devises.",
  ['régimes de change', 'diversité'])
q('qcm', "Milton Friedman défend les changes flottants dans :",
  ["A Theory of the Consumption Function (1957)",
   "The Case for Flexible Exchange Rates (1953)",
   "Capitalisme et liberté (1962)", "Fear of Floating (2002)"], 1,
  "Bonne réponse : B. Dans cette conception libérale, le taux de change est un prix qui doit être déterminé par l’offre et la demande : les autorités ne disposent pas nécessairement de l’information permettant de fixer une parité correcte.",
  ['Friedman', 'changes flottants'])
q('qcm', "Parmi les quatre arguments flexibilistes de Friedman ne figure PAS :",
  ["Le marché détermine le taux de change d’équilibre",
   "La spéculation est stabilisatrice",
   "La balance des paiements s’ajuste automatiquement",
   "Les réserves de change deviennent inutiles à la banque centrale"], 3,
  "Bonne réponse : D. Les quatre arguments retenus par le cours sont : détermination du taux d’équilibre par le marché, spéculation stabilisatrice, ajustement automatique de la balance des paiements, et insularisation des politiques économiques nationales.",
  ['Friedman', 'arguments flexibilistes'])
q('qcm', "L’argument d’insularisation signifie que le flottement :",
  ["Protège les politiques économiques nationales des contraintes extérieures",
   "Isole les marchés financiers les uns des autres",
   "Protège les exportateurs du risque de change",
   "Réduit les mouvements de capitaux"], 0,
  "Bonne réponse : A. Libérée de la défense d’une parité, la politique monétaire pourrait se consacrer entièrement aux objectifs internes. Le choc Volcker constitue précisément la contre-épreuve de cet argument.",
  ['insularisation', 'Friedman'])
q('qcm', "La quatrième limite des arguments flexibilistes, selon le cours, est illustrée par :",
  ["Les accords du Plaza", "Le choc Volcker",
   "Les crises du SME", "Le currency board argentin"], 1,
  "Bonne réponse : B. Le choc Volcker montre que les politiques monétaires restent interdépendantes malgré le flottement : le durcissement américain provoque des mouvements internationaux de capitaux et une appréciation du dollar qui fragilisent d’autres économies.",
  ['choc Volcker', 'insularisation'])
q('qcm', "Les excédents courants cumulés des pays de l’OPEP entre 1974 et 1981 atteignent environ :",
  ["150 milliards de dollars", "450 milliards de dollars",
   "750 milliards de dollars", "1 200 milliards de dollars"], 1,
  "Bonne réponse : B. Ces excédents, placés dans le système financier international, alimentent le recyclage des pétrodollars qui finance l’endettement de nombreux pays en développement.",
  ['pétrodollars', 'chiffres'])
q('qcm', "Le recyclage des pétrodollars désigne :",
  ["La conversion des recettes pétrolières en or",
   "Le processus par lequel les recettes pétrolières, placées dans le système financier international, financent d’autres économies",
   "L’indexation du prix du pétrole sur le dollar",
   "Le réinvestissement des profits pétroliers dans l’exploration"], 1,
  "Bonne réponse : B. Les excédents des pays exportateurs, déposés dans les banques occidentales, sont réorientés vers les pays en développement : le mécanisme favorise l’expansion du crédit international dans les années 1970.",
  ['pétrodollars', 'endettement'])
q('qcm', "Le choc Volcker transforme l’endettement extérieur en crise de la dette par un double mécanisme :",
  ["Hausse des taux américains et appréciation du dollar",
   "Baisse du prix du pétrole et récession mondiale",
   "Dévaluation des monnaies émergentes et inflation importée",
   "Fuite des capitaux et contrôle des changes"], 0,
  "Bonne réponse : A. La hausse des taux renchérit le coût d’emprunts souvent conclus à taux variable, tandis que l’appréciation du dollar alourdit le poids des dettes libellées en monnaie américaine. La dégradation des recettes d’exportation aggrave encore la situation.",
  ['choc Volcker', 'crise de la dette'])
q('qcm', "La dette extérieure de l’Amérique latine passe, selon le cours, de :",
  ["75 milliards de dollars en 1975 à 315 milliards en 1983",
   "120 milliards en 1975 à 450 milliards en 1983",
   "315 milliards en 1975 à 75 milliards en 1983",
   "66 milliards en 1975 à 12 milliards en 1983"], 0,
  "Bonne réponse : A. Dans le même temps, le service de la dette passe d’environ 12 à 66 milliards de dollars : c’est ce basculement qui conduit à la crise.",
  ['chiffres', 'crise de la dette'])
q('qcm', "La crise internationale de la dette est déclenchée par :",
  ["La crise asiatique", "La crise mexicaine de 1982",
   "La crise argentine de 2002", "Les crises du SME de 1992-1993"], 1,
  "Bonne réponse : B. La crise mexicaine de 1982 révèle la vulnérabilité des économies endettées en dollars face aux décisions de la Réserve fédérale : hausse des taux américains, appréciation du dollar et ralentissement mondial se conjuguent.",
  ['crise mexicaine', '1982'])
q('qcm', "Les deux avantages des changes fixes retenus par le cours sont :",
  ["Réduire l’incertitude et les coûts de transaction ; lutter contre l’inflation et restaurer la crédibilité",
   "Supprimer la contrainte extérieure ; accroître les réserves",
   "Stimuler les exportations ; attirer les capitaux",
   "Réduire les taux d’intérêt ; soutenir la demande"], 0,
  "Bonne réponse : A. La stabilité du change sécurise les agents engagés dans les échanges internationaux ; l’engagement de parité discipline la politique monétaire et ancre les anticipations d’inflation.",
  ['changes fixes', 'avantages'])
q('qcm', "La peur du flottement est mise en évidence par :",
  ["Friedman (1953)", "Calvo et Reinhart (2002)",
   "Balassa et Samuelson (1964)", "Jean-Marc Daniel (2015)"], 1,
  "Bonne réponse : B. Dans « Fear of Floating », publié en 2002 dans le Quarterly Journal of Economics, ils montrent que de nombreux pays officiellement flottants interviennent fortement pour limiter les variations de leur monnaie.",
  ['Calvo et Reinhart', 'peur du flottement'])
q('qcm', "Les deux raisons de la peur du flottement sont :",
  ["L’endettement en devises et le risque d’inflation importée",
   "La faiblesse des réserves et l’absence de convertibilité",
   "L’inflation intérieure et le déficit budgétaire",
   "La spéculation et les coûts de transaction"], 0,
  "Bonne réponse : A. L’endettement en devises rend toute dépréciation dangereuse par effet de bilan — les dettes s’alourdissent alors que les revenus restent en monnaie nationale ; l’inflation importée peut contraindre la banque centrale à relever ses taux et freiner l’activité.",
  ['peur du flottement', 'effet de bilan'])
q('qcm', "Les trois objectifs du triangle de Mundell sont :",
  ["Croissance, emploi, stabilité des prix",
   "Libre circulation des capitaux, autonomie de la politique monétaire, stabilité des taux de change",
   "Équilibre interne, équilibre externe, équilibre budgétaire",
   "Convertibilité, flottement, union monétaire"], 1,
  "Bonne réponse : B. Chacun est souhaitable, mais Mundell montre qu’il est impossible de les atteindre simultanément : les États doivent arbitrer.",
  ['triangle de Mundell', 'arbitrage'])
q('qcm', "Dans le chapitre, l’autonomie de la politique monétaire est justifiée par le fait que :",
  ["Elle permet de dévaluer librement",
   "Elle permet de stabiliser l’économie face aux chocs, les banques centrales visant généralement une inflation proche de 2 %",
   "Elle supprime le risque de change", "Elle attire les capitaux étrangers"], 1,
  "Bonne réponse : B. Le cours précise que, dans les économies avancées, les banques centrales visent généralement une inflation proche de 2 % — ce qui suppose de pouvoir ajuster les taux à la situation nationale.",
  ['autonomie monétaire', 'triangle de Mundell'])
q('qcm', "Selon Jean-Marc Daniel (2015), l’histoire monétaire internationale :",
  ["Converge vers le flottement généralisé",
   "A parcouru toutes les éventualités offertes par le triangle des incompatibilités",
   "Démontre la supériorité des changes fixes",
   "Se réduit à l’histoire du dollar"], 1,
  "Bonne réponse : B. « Le monde a accompli une sorte de parcours complet en essayant toutes les éventualités offertes par le triangle des incompatibilités de Robert Mundell. » La formule interdit toute lecture téléologique : aucun système n’était plus moderne qu’un autre.",
  ['Jean-Marc Daniel', 'SMI'])
q('qcm', "Bretton Woods (1944-1971) concilie changes fixes et autonomie monétaire grâce :",
  ["À la convertibilité du dollar en or", "Au contrôle des mouvements de capitaux",
   "Aux interventions coordonnées des banques centrales", "Au rôle du FMI comme prêteur"], 1,
  "Bonne réponse : B. C’est la « fermeture du bas de la balance des paiements » : en limitant la mobilité des capitaux, le système sacrifie le troisième sommet du triangle de Mundell et peut tenir les deux autres.",
  ['Bretton Woods', 'triangle de Mundell'])
q('qcm', "Dans le dispositif initial de Bretton Woods, les changements cumulés de parité dépassant un certain seuil relevaient d’une procédure d’examen par le FMI. Ce seuil est de :",
  ["5 %", "10 %", "15 %", "20 %"], 1,
  "Bonne réponse : B. Le cours mentionne 10 %, tout en précisant qu’un seuil de 15 % est également évoqué dans la retranscription et qu’il ne faut pas présenter ces chiffres comme une règle générale et permanente d’autorisation automatique.",
  ['Bretton Woods', 'encadrement des dévaluations'])
q('qcm', "La convertibilité du dollar en or est suspendue le :",
  ["15 août 1971", "février 1973", "septembre 1985", "août 1993"], 0,
  "Bonne réponse : A. En 1973, les principales monnaies passent ensuite à un flottement généralisé : le système privilégie désormais la mobilité des capitaux et l’autonomie monétaire, au prix de la stabilité des changes.",
  ['chronologie', 'SMI'])
q('qcm', "L’euro (1999) constitue, au regard du triangle de Mundell :",
  ["Un abandon de la libre circulation des capitaux",
   "Un abandon de l’autonomie monétaire nationale au profit de la stabilité et de la mobilité",
   "Un abandon de la stabilité des changes", "Une sortie du triangle"], 1,
  "Bonne réponse : B. L’union monétaire européenne est une réponse institutionnelle au triangle : les États membres préservent la stabilité monétaire interne et la libre circulation des capitaux en transférant leur souveraineté monétaire à la BCE.",
  ['euro', 'triangle de Mundell'])
q('qcm', "Une politique monétaire expansionniste en changes flottants avec forte mobilité des capitaux :",
  ["Apprécie la monnaie et freine les exportations",
   "Déprécie la monnaie et amplifie l’effet de relance",
   "Est sans effet sur le taux de change", "Impose une intervention de la banque centrale"], 1,
  "Bonne réponse : B. Offre de monnaie ↑ → taux d’intérêt ↓ → sorties de capitaux → dépréciation → compétitivité-prix ↑ → exportations ↑. Dans le modèle IS-LM-BP de Mundell-Fleming, la hausse des exportations nettes déplace IS vers la droite.",
  ['Mundell-Fleming', 'politique monétaire'])
q('qcm', "La limite fondamentale d’une guerre des monnaies est que :",
  ["Les dévaluations sont interdites par le FMI",
   "Les taux de change étant relatifs, tous les pays ne peuvent pas déprécier simultanément les uns par rapport aux autres",
   "L’inflation importée annule les gains",
   "Les réserves de change sont limitées"], 1,
  "Bonne réponse : B. C’est une impossibilité logique, et non seulement un coût : une dépréciation chez l’un est une appréciation chez l’autre. Le cours la formule comme limite fondamentale.",
  ['guerre des monnaies', 'prix relatif'])
q('qcm', "À propos de l’accusation de sous-évaluation adressée à la Chine, le cours précise que :",
  ["La manipulation monétaire est démontrée",
   "Une accusation de sous-évaluation ne démontre pas à elle seule une manipulation, l’évaluation du niveau d’équilibre étant complexe",
   "Le yuan est librement flottant",
   "Le FMI a tranché la question"], 1,
  "Bonne réponse : B. C’est une nuance explicite du chapitre. Le mécanisme invoqué est clair — monnaie sous-évaluée → produits moins chers à l’étranger → compétitivité-prix ↑ — mais sa preuve ne l’est pas.",
  ['manipulation monétaire', 'nuance'])
q('qcm', "Les trois instruments de la politique de change retenus par le cours sont :",
  ["Intervention directe, taux d’intérêt, contrôle des changes",
   "Dévaluation, réévaluation, flottement",
   "Réserves, swaps, droits de douane",
   "Politique budgétaire, politique monétaire, politique structurelle"], 0,
  "Bonne réponse : A. L’intervention directe consiste à acheter ou vendre sa monnaie contre des devises ; le taux d’intérêt agit sur l’attractivité des placements ; le contrôle des changes restreint les opérations en devises.",
  ['politique de change', 'instruments'])
q('qcm', "Pourquoi l’intervention contre une appréciation est-elle plus facile que contre une dépréciation ?",
  ["Parce que les marchés y sont favorables",
   "Parce que la banque centrale peut créer sa propre monnaie, alors que ses réserves de devises sont limitées",
   "Parce qu’elle ne nécessite pas de coordination internationale",
   "Parce qu’elle réduit l’inflation"], 1,
  "Bonne réponse : B. Pour freiner une appréciation, elle vend sa monnaie — qu’elle peut émettre. Pour contrer une dépréciation, elle doit vendre des devises prélevées sur des réserves nécessairement finies : c’est ce qui rend les attaques spéculatives possibles.",
  ['intervention', 'réserves de change'])
q('qcm', "Une dévaluation subie se distingue d’une dévaluation compétitive en ce qu’elle :",
  ["Est de plus faible ampleur", "Est imposée par les déséquilibres et les pressions des marchés",
   "Concerne une monnaie flottante", "Est autorisée par le FMI"], 1,
  "Bonne réponse : B. La dévaluation compétitive est une stratégie délibérée de conquête de parts de marché. La distinction est décisive pour analyser la France de 1981-1983, dont les trois dévaluations sont principalement subies.",
  ['dévaluation subie', 'France'])
q('qcm', "La condition de Marshall-Lerner s’écrit :",
  ["|εX| + |εM| > 1", "|εX| + |εM| < 1", "|εX| × |εM| > 1", "|εX| − |εM| > 0"], 0,
  "Bonne réponse : A. Si la somme des élasticités-prix, prises en valeur absolue, est supérieure à 1, les effets-volume l’emportent sur les effets-prix et le solde commercial s’améliore. Égale à 1, l’effet global est nul dans le cadre simplifié ; inférieure à 1, le solde se détériore.",
  ['Marshall-Lerner', 'élasticités'])
q('qcm', "Dans l’illustration du cours, avec |εX| = 0,8 et |εM| = 0,6 et une dévaluation de 10 %, le solde commercial passe de 0 à :",
  ["+ 4,6", "− 4,8", "+ 8", "− 2,4"], 0,
  "Bonne réponse : A. Exportations 108, importations 100 × 1,10 × 0,94 = 103,4, donc solde + 4,6. Dans le cas inverse (0,3 et 0,2), les exportations atteignent 103 et les importations 107,8, soit un solde de − 4,8.",
  ['Marshall-Lerner', 'chiffres'])
q('qcm', "La leçon que le cours tire de cette illustration chiffrée est que :",
  ["Une dévaluation de 10 % améliore toujours le solde",
   "Ce n’est pas la baisse du taux de change qui garantit l’amélioration du solde, mais la réaction des volumes échangés",
   "Les élasticités sont toujours supérieures à 1",
   "L’effet-prix est négligeable"], 1,
  "Bonne réponse : B. Une dévaluation de même ampleur peut produire des effets opposés selon la sensibilité des exportations et des importations aux prix, elle-même dépendante de la spécialisation productive et de la structure des importations.",
  ['Marshall-Lerner', 'volumes'])
q('qcm', "La phase 1 de la courbe en J correspond à :",
  ["La domination des effets-volume", "La domination des effets-prix et la dégradation du solde",
   "L’érosion des gains par l’inflation importée", "L’amélioration du solde commercial"], 1,
  "Bonne réponse : B. Trois phases : effets-prix à court terme (dégradation), effets-volume à moyen terme (redressement), puis amélioration ou érosion des gains à plus long terme selon que l’inflation importée renchérit ou non durablement les coûts nationaux.",
  ['courbe en J', 'temporalité'])
q('qcm', "Une économie spécialisée en compétitivité hors prix :",
  ["Bénéficie fortement d’une dévaluation",
   "Voit ses volumes exportés réagir plus faiblement aux variations de prix",
   "Ne peut pas dévaluer", "A toujours des élasticités supérieures à 1"], 1,
  "Bonne réponse : B. Les acheteurs y privilégient la qualité, l’innovation, la marque et la technologie. Nuance du cours : une faible sensibilité aux prix peut traduire un fort pouvoir de marché plutôt qu’un manque de compétitivité.",
  ['compétitivité hors prix', 'élasticités'])
q('qcm', "Le rôle de la désindustrialisation dans l’efficacité d’une dévaluation est que :",
  ["Elle augmente la sensibilité des exportations aux prix",
   "Elle réduit l’existence de substituts nationaux aux importations",
   "Elle renforce le comportement de marge", "Elle accélère l’inflation importée"], 1,
  "Bonne réponse : B. Pour qu’une dévaluation réduise les volumes importés, il faut pouvoir renoncer aux produits étrangers ou les remplacer. Sans appareil productif national, il n’existe pas de substitut : la facture augmente sans que les volumes diminuent.",
  ['désindustrialisation', 'substituabilité'])
q('qcm', "Le comportement de marge peut limiter les gains d’une dévaluation parce que les entreprises :",
  ["Augmentent leurs volumes exportés", "Peuvent ne pas répercuter intégralement la dévaluation sur leurs prix",
   "Délocalisent leur production", "Augmentent leurs importations d’intrants"], 1,
  "Bonne réponse : B. Plutôt que de baisser leurs prix en devises pour gagner des volumes, elles peuvent reconstituer leurs marges. Le rôle de la concurrence détermine cet arbitrage.",
  ['comportement de marge', 'dévaluation'])
q('qcm', "Dans le cercle vicieux de la monnaie faible, l’enchaînement est :",
  ["Dévaluation → inflation importée → coûts ↑ → compétitivité ↓ → déficit persistant → anticipations de dévaluation → nouvelle dévaluation",
   "Dévaluation → exportations ↑ → croissance ↑ → inflation ↓",
   "Dévaluation → réserves ↑ → crédibilité ↑ → monnaie stable",
   "Dévaluation → importations ↓ → excédent → appréciation"], 0,
  "Bonne réponse : A. Les effets de second tour sur les salaires et les coûts érodent le gain initial ; le déficit persiste, la confiance se dégrade, la spéculation à la baisse s’installe et les réserves s’épuisent jusqu’à une nouvelle dévaluation.",
  ['cercle vicieux', 'monnaie faible'])
q('qcm', "Les anticipations autoréalisatrices de dévaluation fonctionnent parce que :",
  ["La banque centrale annonce ses intentions",
   "Les ventes massives épuisent les réserves et rendent la défense de la parité impossible",
   "Le FMI valide la dévaluation", "L’inflation importée s’accélère"], 1,
  "Bonne réponse : B. Un investisseur qui anticipe une dévaluation vend la monnaie avant sa baisse pour la racheter plus bas. Si de nombreux opérateurs agissent ainsi, la pression devient telle que la dévaluation anticipée se produit effectivement. Le cours cite l’exemple du peso argentin.",
  ['anticipations autoréalisatrices', 'peso argentin'])
q('qcm', "La relance française de 1981 est menée par le gouvernement de :",
  ["Raymond Barre", "Pierre Mauroy", "Laurent Fabius", "Michel Rocard"], 1,
  "Bonne réponse : B. La relance vise à lutter contre le chômage de masse, mais intervient dans un contexte d’inflation déjà élevée : relance de la demande → importations ↑ → déséquilibre extérieur accentué.",
  ['France', 'relance de 1981'])
q('qcm', "L’inflation française atteint, au début de 1982, environ :",
  ["8 %", "11 %", "14 %", "18 %"], 2,
  "Bonne réponse : C. Nettement davantage qu’en Allemagne : l’écart dégrade la compétitivité-prix française, détériore la balance des transactions courantes et nourrit les anticipations de dévaluation.",
  ['chiffres', 'inflation'])
q('qcm', "Les trois dévaluations françaises du début des années 1980 interviennent en :",
  ["Octobre 1981, juin 1982, mars 1983", "Mai 1981, janvier 1982, mars 1983",
   "Juin 1981, mars 1982, juin 1983", "Octobre 1982, juin 1983, mars 1984"], 0,
  "Bonne réponse : A. Il s’agit principalement de dévaluations subies : les autorités cherchaient initialement à maintenir le franc dans le SME, mais les déséquilibres et les pressions financières ont rendu la défense de la parité intenable.",
  ['chronologie', 'dévaluations'])
q('qcm', "Mars 1983 marque, dans le chapitre :",
  ["La sortie du franc du SME", "Le tournant de la rigueur et un changement de logique économique",
   "La création de l’euro", "L’élargissement des marges du SME"], 1,
  "Bonne réponse : B. C’est le point de départ de la désinflation compétitive : les dévaluations n’ayant pas restauré la compétitivité — elles renchérissaient les importations et entretenaient l’inflation — la stratégie est inversée.",
  ['tournant de la rigueur', 'mars 1983'])
q('qcm', "L’instrument privilégié de la désinflation compétitive française est :",
  ["La politique budgétaire", "La politique monétaire restrictive",
   "Le contrôle des changes", "La dévaluation maîtrisée"], 1,
  "Bonne réponse : B. Elle s’accompagne de politiques structurelles — déréglementations, ouverture à la concurrence, flexibilisation du marché du travail — et d’une politique budgétaire de maîtrise de la demande et des dépenses.",
  ['désinflation compétitive', 'instruments'])
q('qcm', "Dans le cercle vertueux de la monnaie forte, la baisse des prix à l’importation est censée produire :",
  ["Une hausse des marges sans effort",
   "Une pression concurrentielle accrue qui pousse aux gains de productivité et à la compétitivité hors prix",
   "Une dépréciation du taux de change réel", "Une hausse des exportations en volume"], 1,
  "Bonne réponse : B. L’enchaînement complet : monnaie forte et stable → prix à l’importation ↓ → pression concurrentielle ↑ → efforts de productivité et de compétitivité hors prix → amélioration du solde extérieur → confiance ↑ → soutien au change → monnaie forte maintenue.",
  ['cercle vertueux', 'monnaie forte'])
q('qcm', "L’inflation française passe, grâce à la désinflation compétitive, d’environ :",
  ["14 % au début des années 1980 à environ 2 % au début des années 1990",
   "13 % en 1981 à 5 % en 1989",
   "11 % en 1982 à 4 % en 1992",
   "14 % en 1982 à 6 % en 1990"], 0,
  "Bonne réponse : A. Nuance du cours : cette référence à 2 % permet de mesurer l’ampleur de la désinflation et ne doit pas être confondue avec la cible institutionnelle de la BCE, créée ultérieurement.",
  ['chiffres', 'désinflation'])
q('qcm', "Le taux de marge des entreprises françaises passe, selon le cours, de :",
  ["32 % en 1985 à 25 % en 1989", "25 % en 1985 à 32 % en 1989",
   "20 % en 1985 à 30 % en 1989", "25 % en 1983 à 32 % en 1993"], 1,
  "Bonne réponse : B. Soit environ 7 points de redressement. Le taux de marge se calcule comme EBE / VA × 100 : il mesure la part de la valeur ajoutée correspondant à l’excédent brut d’exploitation.",
  ['taux de marge', 'chiffres'])
q('qcm', "Le taux de marge se calcule comme :",
  ["VA / EBE × 100", "EBE / VA × 100", "EBE / CA × 100", "VA / PIB × 100"], 1,
  "Bonne réponse : B. L’excédent brut d’exploitation rapporté à la valeur ajoutée mesure la part de la richesse créée qui reste à l’entreprise après rémunération du travail et impôts sur la production.",
  ['taux de marge', 'définitions'])
q('qcm', "Le théorème de Schmidt énonce l’enchaînement :",
  ["Profits ↑ → autofinancement ↑ → investissement ↑ → capacités ↑ → emploi ↑",
   "Salaires ↑ → consommation ↑ → production ↑ → emploi ↑",
   "Monnaie forte → désinflation → compétitivité ↑",
   "Marges ↑ → dividendes ↑ → épargne ↑"], 0,
  "Bonne réponse : A. Selon la formule attribuée à Helmut Schmidt, les profits d’aujourd’hui sont les investissements de demain et les emplois d’après-demain. Le cours montre que cette transmission ne s’est pas réalisée comme attendu en France.",
  ['théorème de Schmidt', 'investissement'])
q('qcm', "Avec un taux d’intérêt nominal de 10 % et une inflation de 14 %, le taux d’intérêt réel vaut environ :",
  ["+ 24 %", "+ 4 %", "− 4 %", "− 14 %"], 2,
  "Bonne réponse : C. Taux réel ≈ taux nominal − taux d’inflation. Le coût réel de l’emprunt est donc négatif : l’inflation réduit la valeur réelle des sommes à rembourser. Avec la même inflation ramenée à 2 %, le taux réel devient + 8 %.",
  ['taux d’intérêt réel', 'calcul'])
q('qcm', "On parle d’effet de levier lorsque :",
  ["Le coût réel de l’endettement dépasse la rentabilité économique",
   "La rentabilité économique dépasse le coût réel de l’endettement",
   "L’entreprise se désendette", "Les taux d’intérêt réels sont négatifs"], 1,
  "Bonne réponse : B. Exemple du cours : rentabilité économique de 10 % et coût réel de la dette de 4 %. L’endettement améliore alors la rentabilité des capitaux propres.",
  ['effet de levier', 'endettement'])
q('qcm', "On parle d’effet de massue lorsque :",
  ["Rentabilité économique de 10 % et coût réel de 4 %",
   "Rentabilité économique de 5 % et coût réel de 8 %",
   "Taux nominal de 10 % et inflation de 14 %",
   "Taux de marge de 32 % et investissement en hausse"], 1,
  "Bonne réponse : B. Lorsque le coût réel de l’endettement dépasse la rentabilité économique, l’endettement dégrade la rentabilité financière. La désinflation, en élevant les taux réels, fait basculer du levier à la massue.",
  ['effet de massue', 'désinflation'])
q('qcm', "La première limite du théorème de Schmidt identifiée par le cours est :",
  ["La hausse des taux d’intérêt réels, qui pousse les entreprises au désendettement",
   "La faiblesse des marges", "La hausse des salaires", "La concurrence étrangère"], 0,
  "Bonne réponse : A. Inflation ↓ → taux d’intérêt réels ↑ → poids réel de l’endettement ↑ → priorité au désendettement. Les entreprises qui retrouvent des marges remboursent leurs dettes et consolident leur bilan plutôt que d’investir.",
  ['théorème de Schmidt', 'désendettement'])
q('qcm', "Les deux autres limites du théorème de Schmidt retenues par le cours sont :",
  ["La globalisation financière et la faiblesse de la demande anticipée",
   "La concurrence chinoise et le coût du travail",
   "L’inflation importée et les taux de change", "Le déficit public et la dette"], 0,
  "Bonne réponse : A. La globalisation financière multiplie les possibilités de placement — titres, actifs étrangers, diversification — tandis que l’investissement dépend avant tout des débouchés anticipés, que les politiques de rigueur compriment.",
  ['théorème de Schmidt', 'limites'])
q('qcm', "La croissance française pendant la période du franc fort est, selon les repères du cours, proche de :",
  ["1 % par an, contre 2 % dans l’OCDE", "2 % par an, contre 3 % dans l’OCDE",
   "3 % par an, contre 2 % dans l’OCDE", "2 % par an, contre 2 % dans l’OCDE"], 1,
  "Bonne réponse : B. Le cours précise qu’il s’agit de repères comparatifs, et non de moyennes statistiques uniformes pour chacune des deux décennies.",
  ['chiffres', 'croissance'])
q('qcm', "Le taux de chômage français passe, selon le cours, d’environ :",
  ["8 % en 1982 à environ 12 % en 1998", "10 % en 1982 à 14 % en 1998",
   "12 % en 1982 à 8 % en 1998", "7 % en 1982 à 10 % en 1998"], 0,
  "Bonne réponse : A. Le cours compare ce niveau à un taux de l’ordre de 7 % dans les autres pays de l’OCDE, selon le périmètre et la période retenus : la désinflation et le redressement extérieur ne se sont pas accompagnés d’un retour rapide au plein emploi.",
  ['chiffres', 'chômage'])
q('qcm', "On parle d’effets d’hystérèse du chômage lorsque :",
  ["Le chômage varie avec la conjoncture",
   "Des chocs initialement conjoncturels laissent des conséquences persistantes sur le niveau du chômage",
   "Le chômage résulte d’un salaire trop élevé",
   "Le chômage diminue avec la croissance"], 1,
  "Bonne réponse : B. Mécanisme : chômage prolongé → perte de compétences et éloignement du marché du travail → difficultés de retour à l’emploi. C’est l’un des coûts durables de la stratégie de désinflation prolongée.",
  ['hystérèse', 'chômage'])
q('qcm', "La nuance essentielle que le cours apporte au bilan du franc fort est que :",
  ["La politique a échoué sur tous ses objectifs",
   "Il serait excessif d’attribuer l’ensemble des difficultés françaises ultérieures à la seule politique du franc fort",
   "Les coûts sociaux ont été négligeables",
   "La désinflation n’a pas eu lieu"], 1,
  "Bonne réponse : B. La désindustrialisation, les transformations technologiques, la mondialisation, les mutations du marché du travail et les autres choix de politique économique jouent également un rôle.",
  ['nuance', 'franc fort'])
q('qcm', "La conclusion du chapitre sur la monnaie forte est que :",
  ["Une monnaie forte est toujours préférable",
   "Une monnaie forte n’est pas nécessairement une bonne monnaie pour tous les agents et dans toutes les situations",
   "Une monnaie faible est toujours préférable",
   "Le taux de change est sans effet réel"], 1,
  "Bonne réponse : B. Son efficacité dépend de la structure productive, de la capacité des entreprises à innover, de la situation conjoncturelle, du niveau des taux d’intérêt, des débouchés anticipés et de la durée des politiques restrictives.",
  ['monnaie forte', 'conclusion'])
q('qcm', "Pour déterminer un « bon » taux de change, le cours distingue trois dimensions :",
  ["Les déterminants, les conséquences et les acteurs concernés",
   "Le nominal, le réel et l’effectif",
   "Le court, le moyen et le long terme",
   "Les exportations, les importations et les capitaux"], 0,
  "Bonne réponse : A. Il faut d’abord expliquer le niveau du change, puis analyser ses conséquences — avantageuses pour certains agents, défavorables pour d’autres — puis identifier les acteurs concernés : l’État et la banque centrale, mais aussi les différents pays d’une même zone monétaire.",
  ['conclusion', 'méthode'])
q('qcm', "La doctrine Miran est exposée dans un rapport publié en :",
  ["Novembre 2024", "Juillet 2025", "Septembre 1985", "Février 1987"], 0,
  "Bonne réponse : A. Stephen Miran y propose une réflexion sur la réorganisation du commerce mondial et du système monétaire international.",
  ['Miran', 'actualité'])
q('qcm', "Selon la doctrine Miran, le dollar fort :",
  ["Favorise l’industrie américaine",
   "Pénalise la compétitivité manufacturière américaine en raison de la demande internationale d’actifs sûrs en dollars",
   "Résulte du déficit commercial", "Est une conséquence des droits de douane"], 1,
  "Bonne réponse : B. La demande internationale d’actifs sûrs libellés en dollars entretiendrait une surévaluation de la monnaie américaine. Le cours précise que cette explication est à nuancer.",
  ['Miran', 'dollar fort'])
q('qcm', "La contradiction interne de la politique américaine relevée par le cours est que :",
  ["Les droits de douane renchérissent les importations et peuvent alimenter l’inflation, ce qui contrarie l’objectif de dépréciation",
   "La Fed refuse de baisser ses taux",
   "Les accords du Plaza sont caducs",
   "Les stablecoins affaiblissent le dollar"], 0,
  "Bonne réponse : A. Le protectionnisme et la volonté de déprécier le dollar poursuivent des logiques potentiellement incompatibles.",
  ['protectionnisme', 'contradiction'])
q('qcm', "Les « accords de Mar-a-Lago » désignent :",
  ["Un accord commercial signé en 2025",
   "Le projet d’une dépréciation coordonnée du dollar, à l’image des accords du Plaza",
   "Un dispositif d’encadrement des stablecoins",
   "Un accord monétaire entre les États-Unis et la Chine"], 1,
  "Bonne réponse : B. L’expression fait référence à la résidence de Donald Trump. Le projet se heurte aux intérêts divergents des grandes puissances, dont les modèles économiques ne bénéficieraient pas également d’une dépréciation du dollar.",
  ['Mar-a-Lago', 'coordination'])
q('qcm', "Le paradoxe du dollar évoqué dans l’ouverture est que :",
  ["Le dollar s’apprécie quand l’économie américaine se dégrade",
   "Déprécier la monnaie de réserve mondiale risque de fragiliser le système monétaire international et la confiance dans les actifs américains",
   "Les droits de douane renforcent le dollar",
   "Le dollar est à la fois fort et sous-évalué"], 1,
  "Bonne réponse : B. Le dollar bénéficie d’une demande internationale structurelle et joue un rôle d’assurance ; une dépréciation réduit la valeur externe des placements en dollars — dans l’exemple du cours, un patrimoine perd 20 % de sa valeur externe — et fait courir un risque de perte de confiance.",
  ['paradoxe du dollar', 'SMI'])
q('qcm', "Un stablecoin est :",
  ["Une monnaie numérique de banque centrale",
   "Un jeton numérique dont l’émetteur cherche à maintenir la valeur par rapport à un actif de référence",
   "Un cryptoactif non adossé", "Une obligation du Trésor américain"], 1,
  "Bonne réponse : B. Les plus importants sont généralement indexés sur le dollar, soit 1 stablecoin ≈ 1 dollar. Le cours précise qu’un stablecoin peut perdre sa parité, temporairement ou durablement.",
  ['stablecoin', 'définitions'])
q('qcm', "Les stablecoins peuvent soutenir la demande de dollars parce que leurs émetteurs :",
  ["Achètent des devises étrangères",
   "Doivent détenir des actifs de réserve adaptés, notamment des bons du Trésor américain",
   "Émettent des monnaies numériques de banque centrale",
   "Interviennent sur le marché des changes"], 1,
  "Bonne réponse : B. Mécanisme : demande de stablecoins en dollars ↑ → demande privée de dollars et de bons du Trésor ↑. Les stablecoins peuvent ainsi prolonger la domination monétaire américaine.",
  ['stablecoin', 'dollar'])
q('qcm', "Le GENIUS Act, cadre fédéral encadrant les stablecoins de paiement, est adopté en :",
  ["Novembre 2024", "Janvier 2025", "Juillet 2025", "Septembre 2025"], 2,
  "Bonne réponse : C. Cette réglementation peut favoriser le développement d’un marché des stablecoins adossés au dollar, ce qui présente un intérêt stratégique pour la demande internationale d’actifs américains.",
  ['GENIUS Act', 'actualité'])
q('qcm', "Les monnaies numériques de banque centrale (MNBC) se distinguent des stablecoins en ce qu’elles sont :",
  ["Adossées à l’or", "Des formes numériques de monnaie de banque centrale",
   "Émises par des entreprises privées", "Non convertibles"], 1,
  "Bonne réponse : B. Elles se distinguent des stablecoins privés, dont l’émetteur cherche à maintenir une parité avec un actif de référence, et des cryptoactifs non adossés à une monnaie officielle.",
  ['MNBC', 'définitions'])

# ========================================================== VRAI / FAUX
q('vrai/faux', "Une dévaluation et une dépréciation désignent le même phénomène.",
  ["Vrai", "Faux"], 1,
  "Faux. La dévaluation est une décision des autorités en régime de changes fixes ; la dépréciation résulte du jeu du marché. Confondre les deux est une erreur de vocabulaire pénalisée.",
  ['vocabulaire', 'piège'])
q('vrai/faux', "Le taux de change effectif est une moyenne pondérée des taux bilatéraux selon le poids des partenaires.",
  ["Vrai", "Faux"], 0,
  "Vrai. C’est l’approche multilatérale : un taux bilatéral ne dit rien de la position d’ensemble d’une monnaie, qui peut se déprécier face à une devise tout en s’appréciant en termes effectifs.",
  ['taux de change effectif', 'mesure'])
q('vrai/faux', "Selon le cours, la spéculation est toujours stabilisatrice sur le marché des changes.",
  ["Vrai", "Faux"], 1,
  "Faux. C’est le deuxième argument flexibiliste de Friedman, mais le chapitre le nuance fortement : en période calme, les anticipations de retour à la moyenne stabilisent ; en période de crise, les anticipations de poursuite de la tendance amplifient les déséquilibres. Le marché est simultanément stabilisateur et déstabilisateur.",
  ['spéculation', 'Friedman'])
q('vrai/faux', "La parité des pouvoirs d’achat a été développée par Gustav Cassel en 1918.",
  ["Vrai", "Faux"], 0,
  "Vrai. Elle repose sur la loi du prix unique : la PPA absolue détermine un taux d’équilibre à partir des niveaux de prix, la PPA relative explique les variations par les différentiels d’inflation.",
  ['Cassel', 'datation'])
q('vrai/faux', "L’effet Balassa-Samuelson implique qu’un pays dont les prix sont élevés a nécessairement une monnaie surévaluée.",
  ["Vrai", "Faux"], 1,
  "Faux. C’est exactement l’inverse : les écarts de productivité entre secteurs échangeables et non échangeables engendrent des différences durables de niveaux de prix, de sorte que les pays les plus productifs peuvent présenter des prix plus élevés sans surévaluation.",
  ['Balassa-Samuelson', 'piège'])
q('vrai/faux', "Les régimes de change se répartissent en deux catégories étanches : changes fixes et changes flottants.",
  ["Vrai", "Faux"], 1,
  "Faux. Le cours insiste sur le fait qu’ils forment un continuum entre ancrage strict et flottement libre : dollarisation, union monétaire, caisse d’émission, régimes conventionnels fixes avec bandes de fluctuation, flottement administré, flottement libre.",
  ['régimes de change', 'continuum'])
q('vrai/faux', "En 2025, une majorité de pays pratiquent un flottement totalement libre de leur monnaie.",
  ["Vrai", "Faux"], 1,
  "Faux. D’après les données du cours, le flottement concerne 66 pays (34 %), contre 29 en arrimage ferme (13 %) et 88 en arrimage souple (46 %) : les régimes d’arrimage restent majoritaires.",
  ['chiffres', 'régimes de change'])
q('vrai/faux', "Même en régime de changes flottants, les banques centrales peuvent intervenir sur le marché des changes.",
  ["Vrai", "Faux"], 0,
  "Vrai. Elles le font pour soutenir leur monnaie ou freiner une appréciation ; les accords du Plaza de 1985 et du Louvre de 1987 montrent qu’elles peuvent même intervenir collectivement.",
  ['intervention', 'flottement'])
q('vrai/faux', "Défendre sa monnaie contre une dépréciation est aussi facile que freiner une appréciation.",
  ["Vrai", "Faux"], 1,
  "Faux. Pour freiner une appréciation, la banque centrale vend sa propre monnaie, qu’elle peut créer. Pour contrer une dépréciation, elle doit vendre des devises prélevées sur des réserves nécessairement limitées : c’est cette asymétrie qui rend les attaques spéculatives possibles.",
  ['intervention', 'asymétrie'])
q('vrai/faux', "Le choc Volcker confirme l’argument d’insularisation des politiques économiques en changes flottants.",
  ["Vrai", "Faux"], 1,
  "Faux. Il le réfute : malgré le flottement, le durcissement de la politique américaine provoque des mouvements internationaux de capitaux et une appréciation du dollar qui fragilisent d’autres économies. Les politiques monétaires restent interdépendantes.",
  ['choc Volcker', 'insularisation'])
q('vrai/faux', "Le recyclage des pétrodollars a favorisé l’expansion du crédit international dans les années 1970.",
  ["Vrai", "Faux"], 0,
  "Vrai. Les excédents des pays exportateurs de pétrole — environ 450 milliards de dollars cumulés entre 1974 et 1981 — déposés dans les banques occidentales, ont été réorientés vers les pays en développement.",
  ['pétrodollars', 'endettement'])
q('vrai/faux', "La crise internationale de la dette est déclenchée par la crise asiatique.",
  ["Vrai", "Faux"], 1,
  "Faux. C’est la crise mexicaine de 1982 qui la déclenche, à la suite du choc Volcker : hausse des taux américains, appréciation du dollar et dégradation des recettes d’exportation.",
  ['crise mexicaine', 'piège'])
q('vrai/faux', "Le triangle de Mundell permet d’atteindre deux des trois objectifs au maximum.",
  ["Vrai", "Faux"], 0,
  "Vrai. Libre circulation des capitaux, autonomie de la politique monétaire et stabilité des taux de change sont tous souhaitables, mais Mundell montre qu’il est impossible de les atteindre simultanément.",
  ['triangle de Mundell', 'arbitrage'])
q('vrai/faux', "La zone euro a renoncé à la libre circulation des capitaux pour préserver la stabilité des changes.",
  ["Vrai", "Faux"], 1,
  "Faux. Elle a renoncé à l’autonomie monétaire nationale : les États membres préservent la stabilité monétaire interne et la libre circulation des capitaux en transférant leur souveraineté monétaire à la BCE.",
  ['euro', 'triangle de Mundell'])
q('vrai/faux', "Tous les pays peuvent déprécier simultanément leur monnaie les uns par rapport aux autres.",
  ["Vrai", "Faux"], 1,
  "Faux. C’est la limite fondamentale de toute guerre des monnaies : les taux de change étant relatifs, une dépréciation chez l’un est une appréciation chez l’autre.",
  ['guerre des monnaies', 'prix relatif'])
q('vrai/faux', "Une accusation de sous-évaluation suffit à démontrer qu’un pays manipule sa monnaie.",
  ["Vrai", "Faux"], 1,
  "Faux. Le cours formule explicitement cette nuance à propos de la Chine : l’évaluation du niveau d’équilibre d’une monnaie est complexe, et le mécanisme invoqué ne vaut pas preuve.",
  ['manipulation monétaire', 'nuance'])
q('vrai/faux', "Une dévaluation améliore mécaniquement le solde commercial.",
  ["Vrai", "Faux"], 1,
  "Faux. Elle ne l’améliore que si la condition de Marshall-Lerner est vérifiée : |εX| + |εM| > 1. Avec des élasticités de 0,3 et 0,2, l’illustration du cours donne un solde de − 4,8 au lieu de + 4,6.",
  ['Marshall-Lerner', 'piège'])
q('vrai/faux', "Les effets bénéfiques d’une dévaluation sont immédiats.",
  ["Vrai", "Faux"], 1,
  "Faux. La courbe en J décrit trois phases : domination des effets-prix à court terme, avec dégradation du solde ; apparition des effets-volume à moyen terme ; amélioration ou érosion des gains à plus long terme selon l’inflation importée.",
  ['courbe en J', 'temporalité'])
q('vrai/faux', "Une faible sensibilité des exportations aux prix traduit nécessairement un manque de compétitivité.",
  ["Vrai", "Faux"], 1,
  "Faux. Le cours apporte explicitement cette nuance : elle peut au contraire traduire un fort pouvoir de marché, lié à la qualité, à l’innovation, à la marque ou à la technologie.",
  ['compétitivité hors prix', 'nuance'])
q('vrai/faux', "La désinflation compétitive consiste à dévaluer régulièrement la monnaie.",
  ["Vrai", "Faux"], 1,
  "Faux. C’est la stratégie inverse, adoptée en mars 1983 : maintenir la parité et comprimer l’inflation interne par des politiques monétaire restrictive, budgétaire et structurelles, les dévaluations antérieures n’ayant pas restauré la compétitivité.",
  ['désinflation compétitive', 'piège'])
q('vrai/faux', "Le taux de marge des entreprises françaises a baissé entre 1985 et 1989.",
  ["Vrai", "Faux"], 1,
  "Faux. Il a été restauré : de 25 % en 1985 à 32 % en 1989, soit environ 7 points de redressement. C’est l’un des trois succès de la politique du franc fort, avec la désinflation et le redressement de la balance courante.",
  ['taux de marge', 'piège'])
q('vrai/faux', "Le théorème de Schmidt s’est vérifié en France pendant la période du franc fort.",
  ["Vrai", "Faux"], 1,
  "Faux. Les marges ont bien été restaurées, mais la transmission vers l’investissement et l’emploi ne s’est pas réalisée : hausse des taux d’intérêt réels et bascule du levier vers la massue, globalisation financière offrant des placements concurrents, et faiblesse des débouchés anticipés.",
  ['théorème de Schmidt', 'limites'])
q('vrai/faux', "La désinflation réduit le coût réel de l’endettement des entreprises.",
  ["Vrai", "Faux"], 1,
  "Faux. Elle l’augmente. Taux réel ≈ nominal − inflation : avec un taux nominal de 10 %, le taux réel passe de − 4 % (inflation à 14 %) à + 8 % (inflation à 2 %). La désinflation alourdit donc le coût réel de la dette.",
  ['taux d’intérêt réel', 'piège'])
q('vrai/faux', "Une entreprise investit dès lors qu’elle dispose de ressources financières suffisantes.",
  ["Vrai", "Faux"], 1,
  "Faux. Le cours rappelle le rôle central de la demande anticipée dans l’analyse keynésienne de l’investissement : la restauration des marges est une condition favorable, mais non suffisante. L’investissement dépend aussi du coût du financement et des arbitrages financiers.",
  ['investissement', 'débouchés anticipés'])
q('vrai/faux', "L’ensemble des difficultés économiques françaises ultérieures peut être imputé à la politique du franc fort.",
  ["Vrai", "Faux"], 1,
  "Faux. Le cours formule cette nuance essentielle : la désindustrialisation, les transformations technologiques, la mondialisation, les mutations du marché du travail et les autres choix de politique économique y contribuent également.",
  ['nuance', 'franc fort'])
q('vrai/faux', "Un stablecoin peut perdre sa parité avec son actif de référence.",
  ["Vrai", "Faux"], 0,
  "Vrai. Le cours le précise explicitement : l’émetteur cherche à maintenir la valeur — 1 stablecoin ≈ 1 dollar pour les plus importants — mais cette parité peut être perdue temporairement ou durablement.",
  ['stablecoin', 'risque'])
q('vrai/faux', "Le projet d’accords de Mar-a-Lago fait explicitement référence au précédent des accords du Plaza.",
  ["Vrai", "Faux"], 0,
  "Vrai. Il viserait à organiser une dépréciation concertée du dollar à l’image du Plaza de 1985, mais se heurte aux intérêts divergents des grandes puissances, dont les modèles économiques ne bénéficieraient pas également d’une telle dépréciation.",
  ['Mar-a-Lago', 'Plaza'])

# ====================================================== QUESTIONS OUVERTES
q('question ouverte', "Distinguez taux de change nominal bilatéral, taux de change effectif et taux de change réel.",
  [], 0,
  "Le taux de change nominal bilatéral mesure la valeur relative de deux monnaies. Il s’exprime soit à la cotation au certain — nombre d’unités de monnaie étrangère obtenues pour une unité de monnaie nationale — soit à la cotation à l’incertain, qui fait l’inverse. Sa limite est évidente : il ne renseigne que sur une relation, alors qu’une économie commerce avec de nombreux partenaires. Le taux de change effectif nominal répond à cette limite en proposant une approche multilatérale : il est une moyenne pondérée des taux bilatéraux, les pondérations reflétant le poids des partenaires dans les échanges. Dans l’exemple simplifié du cours, ces poids sont de 40 % pour les États-Unis, 35 % pour la Chine et 25 % pour le Royaume-Uni. Une monnaie peut ainsi se déprécier face à une devise tout en s’appréciant en termes effectifs. Le taux de change réel introduit une troisième dimension, celle des prix : il corrige le taux nominal par les niveaux de prix des deux économies et mesure donc la compétitivité-prix relative. Son intérêt est décisif, car une monnaie parfaitement stable nominalement peut faire perdre de la compétitivité à son économie si l’inflation nationale dépasse celle des partenaires. Réciproquement, un pays peut améliorer sa compétitivité sans dévaluer, en désinflatant plus vite que ses concurrents : c’est exactement la logique de la désinflation compétitive française engagée en mars 1983.",
  ['mesure du change', 'compétitivité'])
q('question ouverte', "Expliquez en quoi le marché des changes peut être simultanément stabilisateur et déstabilisateur.",
  [], 0,
  "Le marché des changes confronte une offre et une demande de devises : c’est sur lui que se forme le prix des monnaies. Dominique Plihon le qualifie de marché-réseau, car il ne repose pas sur une place physique unique mais sur des réseaux électroniques et des intermédiaires spécialisés, ce qui lui donne une dimension mondiale et un fonctionnement quasi continu. Sur ce marché coexistent deux attitudes face au risque : la couverture, qui vise à réduire l’exposition au risque de change, et la spéculation, qui consiste à l’accepter dans l’espoir d’un gain. C’est le comportement spéculatif qui explique l’ambivalence. En période calme, les opérateurs forment des anticipations de retour à la moyenne : ils achètent une monnaie qu’ils jugent sous-évaluée et vendent une monnaie qu’ils jugent surévaluée, ce qui ramène le cours vers sa valeur de référence. La spéculation stabilise alors le change, conformément au deuxième argument flexibiliste de Friedman. Mais en période de crise, les anticipations changent de nature : elles portent sur la poursuite de la tendance. Les opérateurs vendent une monnaie qui baisse parce qu’ils anticipent qu’elle continuera de baisser, et ces ventes alimentent effectivement la baisse. Le mécanisme devient autoréalisateur. Cette ambivalence a une portée considérable : elle signifie que l’argument de Friedman n’est pas faux mais conditionnel, et elle explique pourquoi les changes flottants n’ont pas stabilisé les taux autour de leurs fondamentaux comme la théorie l’annonçait.",
  ['spéculation', 'Forex'])
q('question ouverte', "Présentez la théorie de la parité des pouvoirs d’achat et ses limites.",
  [], 0,
  "Gustav Cassel développe en 1918 la théorie de la parité des pouvoirs d’achat. Son fondement est la loi du prix unique : un même bien devrait, après conversion, coûter le même prix dans deux économies, faute de quoi des arbitrages s’enclencheraient jusqu’à refermer l’écart. Deux versions en découlent. La PPA absolue détermine un taux de change d’équilibre à partir des niveaux de prix : la comparaison entre le taux observé et ce taux de PPA permet d’identifier les écarts de valorisation d’une monnaie. La PPA relative, moins exigeante, explique les variations du change par les différentiels d’inflation : dans l’exemple du cours, avec une inflation de 6 % dans la zone euro et de 2 % aux États-Unis, l’euro devrait se déprécier d’environ 4 % face au dollar. Le chapitre identifie quatre limites. D’abord les coûts de transaction — transport, assurance, droits de douane — qui empêchent l’égalisation parfaite des prix. Ensuite l’existence de biens non échangeables : services abrités, immobilier et une large part de la consommation locale échappent à l’arbitrage international. Troisièmement l’effet Balassa-Samuelson, formulé par Béla Balassa et Paul Samuelson en 1964 : la productivité élevée du secteur exposé permet des salaires élevés, que la mobilité du travail diffuse vers les secteurs non échangeables dont la productivité progresse moins ; leurs coûts puis leurs prix s’élèvent, de sorte que les pays les plus productifs présentent durablement des niveaux de prix plus élevés sans que leur monnaie soit surévaluée. Enfin les mouvements de capitaux, qui peuvent éloigner durablement le taux de change de la PPA. Celle-ci ne fournit donc qu’une référence de long terme, non une loi.",
  ['PPA', 'Cassel'])
q('question ouverte', "Exposez les quatre arguments de Friedman en faveur des changes flottants et leurs limites.",
  [], 0,
  "Dans The Case for Flexible Exchange Rates (1953), Milton Friedman défend la supériorité des changes flottants dans une conception libérale où les marchés disposent de mécanismes autorégulateurs. Premier argument : le marché permettrait de déterminer le taux de change d’équilibre, car les autorités politiques ne disposent pas nécessairement de l’information permettant de fixer une parité correcte, laquelle peut s’écarter durablement des fondamentaux. Deuxième argument : la spéculation serait stabilisatrice, les investisseurs achetant les monnaies sous-évaluées et vendant les surévaluées. Troisième argument : la balance des paiements s’ajusterait automatiquement, un déficit provoquant une dépréciation qui restaure la compétitivité. Quatrième argument : le flottement insulariserait les politiques économiques nationales, libérées de la défense d’une parité. Le chapitre confronte chacun à l’expérience. Première limite : les changes flottants n’ont pas stabilisé les taux autour de leurs fondamentaux, la volatilité observée étant forte. Deuxième limite : la spéculation peut devenir déstabilisatrice lorsque les anticipations portent sur la poursuite de la tendance plutôt que sur un retour à la moyenne. Troisième limite : les déséquilibres extérieurs persistent en changes flottants, l’ajustement automatique promis ne s’observant pas. Quatrième limite, la plus démonstrative : le choc Volcker montre que les politiques monétaires restent interdépendantes. À partir de 1979, la hausse des taux américains provoque des mouvements internationaux de capitaux et une appréciation du dollar, fragilisant les pays endettés en dollars jusqu’à la crise de la dette. L’insularisation est donc imparfaite.",
  ['Friedman', 'changes flottants'])
q('question ouverte', "Comment le choc Volcker a-t-il transformé le recyclage des pétrodollars en crise de la dette ?",
  [], 0,
  "Les chocs pétroliers des années 1970 provoquent d’importants excédents courants dans les pays de l’OPEP : leur montant cumulé entre 1974 et 1981 atteint environ 450 milliards de dollars. Ces recettes sont placées dans le système financier international, notamment déposées dans les banques occidentales, qui les réorientent vers d’autres économies : c’est le recyclage des pétrodollars, qui favorise l’expansion du crédit international et finance l’endettement de nombreux pays en développement. À court terme, le mécanisme paraît vertueux : les pétrodollars contribuent à financer leur développement économique. Le basculement vient de la politique monétaire américaine. À partir de 1979, Paul Volcker, à la tête de la Réserve fédérale, engage une politique très restrictive pour lutter contre l’inflation et relève fortement les taux d’intérêt. Un double mécanisme frappe alors les pays endettés. D’une part, la hausse des taux américains renchérit le coût de dettes souvent contractées à taux variable : le service de la dette augmente mécaniquement. D’autre part, l’appréciation du dollar — provoquée par l’afflux de capitaux attirés par ces rendements — alourdit le poids des dettes libellées en monnaie américaine, puisque les revenus des pays débiteurs restent en monnaie nationale. S’y ajoute un troisième facteur : la dégradation des recettes d’exportation, liée au ralentissement mondial. Les chiffres l’attestent : la dette extérieure de l’Amérique latine passe d’environ 75 milliards de dollars en 1975 à 315 milliards en 1983, et son service d’environ 12 à 66 milliards. La crise mexicaine de 1982 marque le déclenchement de la crise internationale de la dette, et démontre que la flexibilité des changes ne supprime pas l’interdépendance monétaire internationale.",
  ['choc Volcker', 'crise de la dette'])
q('question ouverte', "Expliquez la peur du flottement mise en évidence par Calvo et Reinhart.",
  [], 0,
  "Dans « Fear of Floating », publié en 2002 dans le Quarterly Journal of Economics, Guillermo Calvo et Carmen Reinhart établissent un constat empirique : de nombreux pays officiellement en changes flottants interviennent en réalité fortement pour limiter les fluctuations de leur monnaie. La volatilité de leurs réserves de change et de leurs taux d’intérêt le révèle, bien davantage que leurs déclarations officielles. Cette observation impose de distinguer le régime de jure, celui qu’un État déclare, du régime de facto, celui qu’il pratique effectivement — distinction que les classifications internationales doivent prendre en compte. Deux mécanismes expliquent ce comportement. Le premier est l’endettement en devises. Lorsqu’une économie, ses entreprises ou son État se sont endettés en monnaie étrangère, une dépréciation alourdit mécaniquement la charge de cette dette en monnaie nationale, alors que les revenus qui doivent la servir restent libellés dans la monnaie locale : c’est l’effet de bilan. Le flottement n’est donc pas une option neutre pour une telle économie, il est un risque de solvabilité. Le second mécanisme est le risque d’inflation importée : dans les économies fortement dépendantes de leurs importations, une dépréciation renchérit l’énergie, les matières premières et les intrants, et peut contraindre la banque centrale à relever ses taux, ce qui freine l’activité. La conséquence est structurelle : les régimes d’arrimage demeurent majoritaires, et les données de 2025 du cours le confirment — 29 pays en arrimage ferme et 88 en arrimage souple, contre 66 en flottement.",
  ['Calvo et Reinhart', 'peur du flottement'])
q('question ouverte', "Présentez le triangle de Mundell et la lecture historique qu’en propose Jean-Marc Daniel.",
  [], 0,
  "Le triangle des incompatibilités de Robert Mundell repose sur trois objectifs, tous souhaitables. La libre circulation des capitaux permet aux pays dont l’épargne est insuffisante de mobiliser l’épargne internationale et favorise une allocation plus efficace du capital. L’autonomie de la politique monétaire permet de stabiliser l’économie face aux chocs, les banques centrales des économies avancées visant généralement une inflation proche de 2 %. La stabilité des taux de change limite le risque de change, facilite les échanges — le cours cite le cas des pays de l’OPEP — et limite le risque de crise de change. Mais Mundell montre qu’il est impossible d’atteindre simultanément ces trois objectifs : il faut en sacrifier un. Jean-Marc Daniel écrit en 2015 que « le monde a accompli une sorte de parcours complet en essayant toutes les éventualités offertes par le triangle des incompatibilités de Robert Mundell », formule qui fournit au chapitre son fil conducteur. Bretton Woods, de 1944 à 1971, associe changes fixes et autonomie monétaire relative grâce au contrôle des mouvements de capitaux — la fermeture du bas de la balance des paiements. Après la suspension de la convertibilité du dollar en or le 15 août 1971 et le passage au flottement généralisé en 1973, ce sont la mobilité des capitaux et l’autonomie monétaire qui l’emportent, au prix de la stabilité. Le Système monétaire européen, de 1979 à 1993, tente de restaurer la fixité en Europe et bute sur les crises de 1992-1993, qui conduisent à élargir les marges à ± 15 % en août 1993. L’euro, en 1999, assure stabilité et mobilité en transférant la souveraineté monétaire à la BCE. La portée de cette lecture est méthodologique : elle interdit toute vision téléologique, aucun système n’étant plus moderne qu’un autre.",
  ['triangle de Mundell', 'Jean-Marc Daniel'])
q('question ouverte', "Quels sont les trois instruments de la politique de change et quelles sont leurs limites ?",
  [], 0,
  "La politique de change vise à agir sur la valeur externe de la monnaie. Elle est particulièrement importante en changes fixes, où il faut défendre une parité existante. Le premier instrument est l’intervention directe sur le marché des changes : la banque centrale achète ou vend sa monnaie contre des devises. Le cours souligne une asymétrie décisive. Pour lutter contre une appréciation, elle vend sa monnaie et achète des devises : l’opération est relativement facile, puisqu’elle peut créer sa propre monnaie. Pour lutter contre une dépréciation, elle doit au contraire vendre des devises et acheter sa monnaie : elle est alors limitée par ses réserves de change, nécessairement finies. C’est précisément cette limite que les attaques spéculatives exploitent. Le deuxième instrument est le taux d’intérêt : une hausse accroît le rendement des placements dans la monnaie nationale, attire les capitaux et soutient le change. Elle permet ainsi de préserver les réserves de change et de lutter contre l’inflation importée, puisqu’en soutenant la monnaie elle contient le prix des importations. Mais son coût est interne : des taux élevés renchérissent le crédit et freinent la consommation et l’investissement. Le troisième instrument est le contrôle des changes, qui restreint les opérations en devises afin de limiter les pressions sur la monnaie. Son objectif est de rétablir une marge de manœuvre en réduisant la mobilité des capitaux — ce qui revient, dans les termes du triangle de Mundell, à renoncer à un sommet pour tenir les deux autres. S’y ajoutent les effets indirects des politiques conjoncturelles : une politique monétaire expansionniste en changes flottants déprécie la monnaie et amplifie l’effet de relance, ce qui peut faire naître des tensions avec les partenaires sans aucune dévaluation officielle.",
  ['politique de change', 'instruments'])
q('question ouverte', "Quelles sont les conditions d’efficacité d’une dévaluation compétitive ?",
  [], 0,
  "Il faut d’abord distinguer la dévaluation subie, imposée par les déséquilibres et les pressions des marchés, de la dévaluation compétitive, stratégie délibérée de conquête de parts de marché. Les effets attendus sont connus : la dévaluation modifie les prix relatifs, les volumes échangés réagissent, le solde commercial s’améliore et l’activité est stimulée. Mais quatre séries de conditions commandent le résultat. La première est temporelle : la courbe en J décrit trois phases — domination des effets-prix à court terme, avec dégradation du solde ; apparition des effets-volume à moyen terme ; amélioration ou érosion des gains à plus long terme selon que l’inflation importée renchérit durablement les coûts nationaux. La deuxième est la condition de Marshall-Lerner, |εX| + |εM| > 1. L’illustration du cours est décisive : à partir d’exportations et d’importations de 100 et d’une dévaluation de 10 %, des élasticités de 0,8 et 0,6 donnent 108 − 103,4 = + 4,6, tandis que des élasticités de 0,3 et 0,2 donnent 103 − 107,8 = − 4,8. Ce n’est donc pas la baisse du taux de change qui garantit l’amélioration du solde, mais la réaction des volumes. La troisième condition porte sur les exportations : elles doivent être sensibles aux prix, ce qui dépend de la spécialisation — une économie positionnée sur la compétitivité hors prix, où les acheteurs privilégient qualité, innovation, marque et technologie, réagit faiblement. Le cours nuance toutefois : une faible sensibilité aux prix peut traduire un fort pouvoir de marché. La quatrième porte sur les importations, qui doivent être substituables : il faut pouvoir renoncer aux produits étrangers ou disposer de substituts nationaux, ce que la désindustrialisation compromet. S’y ajoute le comportement de marge : les entreprises peuvent préférer reconstituer leurs marges plutôt que baisser leurs prix en devises.",
  ['dévaluation compétitive', 'Marshall-Lerner'])
q('question ouverte', "Expliquez le cercle vicieux de la monnaie faible.",
  [], 0,
  "Le cercle vicieux de la monnaie faible décrit la manière dont une dévaluation peut appeler la suivante. Le point de départ est l’inflation importée : la dévaluation renchérit le prix des produits importés, biens de consommation finale comme intrants utilisés par les entreprises nationales. Suivent les effets de second tour : l’inflation réduit le pouvoir d’achat, les salariés formulent des revendications salariales pour le préserver, les salaires et les coûts de production augmentent — mécanisme renforcé lorsque certains salaires sont indexés sur les prix. L’étape suivante est l’érosion du gain de compétitivité : la hausse des coûts nationaux se répercute dans les prix domestiques et réduit l’avantage initialement procuré par la dévaluation. Le déficit extérieur persiste alors, les effets-volume ne compensant pas suffisamment les effets-prix. Cette persistance a un effet sur les anticipations : la perte de confiance s’installe et la spéculation à la baisse se développe. Le mécanisme devient autoréalisateur. Un investisseur qui anticipe une dévaluation vend la monnaie avant sa baisse, espérant la racheter à un cours inférieur ; si de nombreux opérateurs adoptent simultanément ce comportement, les ventes massives exercent une pression considérable sur le change. La banque centrale doit alors mobiliser ses réserves pour défendre la parité, mais celles-ci sont limitées : lorsqu’elles deviennent insuffisantes, la défense devient impossible et une nouvelle dévaluation intervient, relançant tout le mécanisme. Le cours cite l’exemple du peso argentin et établit le lien avec les crises de dette souveraine, ainsi qu’avec la peur du flottement des pays émergents. La leçon est que la dévaluation peut initialement améliorer la compétitivité-prix, mais que si l’inflation importée neutralise rapidement cet avantage, le pays se trouve enfermé dans une spirale.",
  ['cercle vicieux', 'anticipations autoréalisatrices'])
q('question ouverte', "Analysez la séquence française de 1981 à 1983.",
  [], 0,
  "Au début des années 1980, la France appartient au Système monétaire européen : elle doit donc défendre la parité du franc face aux monnaies européennes. En 1981, le gouvernement de Pierre Mauroy mène une politique de relance pour lutter contre le chômage de masse. Mais cette politique intervient dans un contexte d’inflation déjà élevée, et elle produit un enchaînement défavorable : relance de la demande, importations en hausse, déséquilibre extérieur accentué. L’inflation française atteint environ 14 % au début de 1982, nettement davantage qu’en Allemagne. L’écart d’inflation dégrade mécaniquement la compétitivité-prix : les prix français deviennent relativement plus élevés, la balance des transactions courantes se détériore, et les investisseurs anticipent une dévaluation du franc. Les attaques se déclenchent alors : les anticipations de dévaluation provoquent des ventes de francs et des sorties de capitaux, qui exercent une pression croissante sur la parité. La France doit défendre sa monnaie, mais elle est contrainte de procéder à trois dévaluations : octobre 1981, juin 1982 et mars 1983. Le cours insiste sur leur nature : il s’agit principalement de dévaluations subies, puisque les autorités cherchaient initialement à maintenir le franc dans le SME et que ce sont les déséquilibres et les pressions financières qui ont rendu la défense de la parité intenable. Ces dévaluations ne correspondent donc pas à une stratégie volontaire de conquête de parts de marché. Elles ne suffisent pas davantage : en renchérissant les importations, elles entretiennent l’inflation qu’elles devaient compenser — c’est exactement le cercle vicieux de la monnaie faible. D’où le tournant de mars 1983, qui marque un véritable changement de logique économique : renoncer à la dévaluation et comprimer l’inflation interne pour restaurer la compétitivité, c’est-à-dire passer à la désinflation compétitive.",
  ['France 1981-1983', 'dévaluations subies'])
q('question ouverte', "Présentez la stratégie de désinflation compétitive et le cercle vertueux attendu de la monnaie forte.",
  [], 0,
  "La désinflation compétitive est engagée en mars 1983. Son objectif est de restaurer la compétitivité sans dévaluer, en comprimant l’inflation interne : puisque la compétitivité-prix dépend du taux de change réel, obtenir une inflation inférieure à celle des partenaires améliore progressivement la position du pays à parité inchangée. Trois familles d’instruments sont mobilisées. Les politiques structurelles renforcent la concurrence par les déréglementations et l’ouverture, et flexibilisent le marché du travail. La politique budgétaire maîtrise la demande et les dépenses. La politique monétaire restrictive constitue l’instrument privilégié : des taux élevés soutiennent la monnaie et freinent les tensions inflationnistes. Le cercle vertueux attendu s’enchaîne ainsi. Une monnaie forte et stable abaisse les prix à l’importation, ce qui réduit directement les coûts des entreprises utilisatrices d’intrants importés et contient l’inflation. Cette baisse des prix importés accroît la pression concurrentielle sur les entreprises nationales, qui ne peuvent plus se protéger par le prix. Elles sont donc conduites à des efforts de productivité et de compétitivité hors prix — qualité, innovation, montée en gamme. Il en résulte une amélioration de la compétitivité et du solde extérieur, puis un renforcement de la confiance dans la monnaie, qui soutient le taux de change et permet le maintien d’une monnaie forte et stable : la boucle est refermée. La logique profonde de cette stratégie est donc contraignante : c’est en interdisant le recours au prix qu’on force l’appareil productif à se transformer. Le chapitre montre cependant que ce cercle vertueux a coexisté avec un cercle défavorable, et c’est de cette coexistence que naît le bilan contrasté du franc fort.",
  ['désinflation compétitive', 'cercle vertueux'])
q('question ouverte', "Pourquoi le théorème de Schmidt ne s’est-il pas vérifié en France ?",
  [], 0,
  "Selon la formule attribuée à Helmut Schmidt, les profits d’aujourd’hui sont les investissements de demain et les emplois d’après-demain : profits en hausse, autofinancement en hausse, investissement en hausse, capacités de production en hausse, emploi en hausse. La politique du franc fort semblait avoir créé la condition initiale, puisque le taux de marge des entreprises — EBE / VA × 100 — remonte de 25 % en 1985 à 32 % en 1989, soit environ 7 points. Pourtant la transmission ne s’est pas réalisée. Le chapitre identifie trois raisons. La première tient aux taux d’intérêt réels. Le taux réel vaut approximativement le taux nominal moins l’inflation : avec un taux nominal de 10 % et une inflation de 14 %, il s’établit à − 4 %, de sorte que le coût réel de l’emprunt est négatif ; avec la même inflation ramenée à 2 %, il atteint + 8 %. La désinflation alourdit donc le coût réel de la dette, et fait basculer l’effet de levier — rentabilité économique de 10 % supérieure à un coût réel de 4 % — en effet de massue — coût réel de 8 % supérieur à une rentabilité de 5 %. Les entreprises qui retrouvent des marges financières choisissent alors de rembourser leurs dettes, de réduire leurs charges financières et de consolider leur bilan plutôt que d’investir. La deuxième raison est la globalisation financière : à partir des années 1980, la libéralisation offre de nouvelles possibilités de placement — titres financiers, actifs étrangers, diversification internationale — de sorte que les profits peuvent alimenter l’accumulation financière sans accroître les capacités productives. La troisième, et la plus keynésienne, est que l’investissement dépend avant tout des débouchés anticipés : or les politiques de rigueur affaiblissent la demande intérieure et la demande extérieure ne compense pas suffisamment. La restauration des marges est donc une condition favorable à l’investissement, mais non suffisante.",
  ['théorème de Schmidt', 'investissement'])
q('question ouverte', "Dressez le bilan contrasté de la politique du franc fort.",
  [], 0,
  "Les succès sont réels et mesurables. La désinflation d’abord : l’inflation française, d’environ 14 % au début des années 1980, revient autour de 2 % au début des années 1990 — le cours précisant que cette référence mesure l’ampleur de la désinflation et ne doit pas être confondue avec la cible institutionnelle de la BCE, créée ultérieurement. Le redressement de la balance des transactions courantes ensuite. La restauration du taux de marge des entreprises enfin, de 25 % en 1985 à 32 % en 1989. S’y ajoutent une désinflation importée, une maîtrise des coûts, une amélioration potentielle de la compétitivité hors prix et une confiance accrue dans la monnaie. Les coûts sont tout aussi réels. Les taux d’intérêt réels élevés font basculer l’effet de levier en effet de massue et poussent au désendettement plutôt qu’à l’investissement ; la globalisation financière détourne une partie des profits vers les placements ; et la rigueur comprime la demande intérieure, donc les débouchés anticipés. Un cercle cumulatif défavorable s’installe : politique restrictive, affaiblissement de la demande, ralentissement de la croissance, hausse du chômage, modération salariale liée à la perte de pouvoir de négociation des salariés, consommation limitée, demande durablement faible — et le mécanisme recommence. Les chiffres le confirment : croissance française proche de 2 % par an contre environ 3 % en moyenne dans l’OCDE ; chômage passant d’environ 8 % de la population active en 1982 à environ 12 % en 1998, contre un ordre de grandeur de 7 % dans les autres pays de l’OCDE. Le chômage prolongé engendre en outre des effets d’hystérèse : perte de compétences, éloignement du marché du travail, difficultés de retour à l’emploi. Le cours formule enfin une nuance essentielle : il serait excessif d’attribuer l’ensemble des difficultés françaises ultérieures à la seule politique du franc fort, la désindustrialisation, les transformations technologiques, la mondialisation et d’autres choix y contribuant. La conclusion est que « une monnaie forte n’est pas nécessairement une bonne monnaie pour tous les agents économiques et dans toutes les situations ».",
  ['franc fort', 'bilan'])
q('question ouverte', "Existe-t-il un « bon » taux de change ? Présentez les trois dimensions du problème.",
  [], 0,
  "La conclusion générale du chapitre répond que la question est complexe, parce qu’un taux de change élevé présente des avantages pour certains agents économiques et des inconvénients pour d’autres, et qu’un taux faible améliore la compétitivité-prix tout en provoquant de l’inflation importée. Trois dimensions doivent donc être distinguées. La première consiste à comprendre le niveau et les déterminants du taux de change : avant d’évaluer les conséquences d’un change, il faut expliquer pourquoi il se situe à ce niveau. Cela suppose de mobiliser les mécanismes étudiés dans le chapitre — les échanges internationaux de biens et services, les mouvements de capitaux, les différentiels de taux d’intérêt et les anticipations — en rappelant que leur poids relatif varie selon l’horizon considéré. La deuxième consiste à analyser les conséquences du taux de change, qui ne sont jamais univoques : une dépréciation améliore la compétitivité-prix des exportateurs mais renchérit les importations, alourdit les dettes libellées en devises et réduit le pouvoir d’achat des ménages ; une appréciation produit les effets symétriques. La troisième, souvent négligée, consiste à identifier les acteurs concernés. L’État et la banque centrale n’ont pas nécessairement les mêmes priorités que les entreprises exportatrices, les entreprises importatrices ou les ménages. Et au sein d’une même zone monétaire, les différents pays membres peuvent être affectés très différemment par un même niveau de change, puisque leurs structures productives, leurs spécialisations et leurs dépendances aux importations diffèrent. Il n’existe donc pas de bon taux de change en soi : il n’existe qu’un taux de change plus ou moins favorable à des objectifs déterminés, pour des agents déterminés et dans une situation conjoncturelle déterminée. C’est exactement la conclusion que le chapitre tire de la stratégie du franc fort.",
  ['conclusion', 'bon taux de change'])
q('question ouverte', "Quels enjeux monétaires soulève la politique économique américaine contemporaine ?",
  [], 0,
  "Le chapitre s’ouvre, pour conclure, sur les conséquences monétaires de la politique économique de Donald Trump. Le point de départ est la doctrine Miran, exposée par Stephen Miran dans un rapport publié en novembre 2024 : la demande internationale d’actifs sûrs libellés en dollars entretiendrait une surévaluation de la monnaie américaine, laquelle pénaliserait les exportateurs et l’industrie manufacturière et contribuerait au déficit commercial. Le cours précise que cette explication est à nuancer. Pour y remédier, la doctrine envisage une dépréciation organisée du dollar, mais cet objectif entre en contradiction avec les instruments protectionnistes : les droits de douane renchérissent les importations et peuvent alimenter l’inflation, ce qui contrarie la stratégie de dépréciation. D’où le projet dit d’« accords de Mar-a-Lago », en référence à la résidence de Donald Trump : une coordination internationale destinée à réduire la valeur du dollar, sur le modèle du précédent historique des accords du Plaza de 1985. Mais ce projet se heurte aux intérêts divergents des grandes puissances, dont les modèles économiques ne bénéficieraient pas également d’une dépréciation du dollar — même s’il pourrait présenter un intérêt pour l’autonomie financière européenne. Reste le paradoxe du dollar : comment déprécier la monnaie de réserve mondiale sans fragiliser le système monétaire international ? Le dollar bénéficie d’une demande internationale structurelle et joue un rôle d’assurance ; une dépréciation réduit la valeur externe des placements en dollars — dans l’exemple du cours, un patrimoine perd 20 % de sa valeur externe — et fait courir un risque de perte de confiance dans les actifs américains. Face à ce risque, les autorités cherchent de nouvelles sources de demande privée de dollars, notamment par les stablecoins, dont les émetteurs doivent détenir des actifs de réserve adaptés : demande de stablecoins en dollars en hausse, demande de dollars et de bons du Trésor en hausse. Le GENIUS Act de juillet 2025 leur fournit un cadre fédéral. Le chapitre se clôt sur quatre-vingts ans de domination du dollar, l’appréciation de l’euro depuis son point bas de 2022 et la dépréciation de plusieurs monnaies émergentes.",
  ['Miran', 'actualité'])

TYPES = {'qcm': 'qcm', 'vrai/faux': 'vraifa', 'question ouverte': 'questi'}
QUIZ = []
TAGS = {}
for _i, (_t, _q, _o, _a, _e, _g) in enumerate(Q, 1):
    _id = 'ch26-%s-%d' % (TYPES[_t], _i)
    QUIZ.append({'type': _t, 'q': _q, 'opts': _o, 'ans': _a, 'exp': _e,
                 'ch': 26, 'id': _id})
    TAGS[_id] = _g
