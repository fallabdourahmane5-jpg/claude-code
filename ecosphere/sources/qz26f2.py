# -*- coding: utf-8 -*-
"""Chapitre 26 — corrections des questions héritées, sous-parties c26-07 à c26-12."""


def f(**kw):
    return kw


FIX = {

# =============================================================== c26-07
'ch26-qcm-13': f(niv='comprendre', sp='c26-07', b=1353,
 why=["Les anticipations de poursuite de la tendance sont au contraire "
      "déstabilisatrices, et caractérisent les périodes de crise.",
      "Les opérateurs ne suivent pas de consignes : ils forment leurs "
      "propres anticipations.",
      "La couverture systématique à terme neutraliserait le risque sans "
      "ramener le cours vers une valeur de référence."],
 diss="Mécanisme stabilisateur à décrire : achat d’une monnaie jugée "
      "sous-évaluée, vente d’une monnaie jugée surévaluée, donc retour vers "
      "la valeur de référence."),
'ch26-qcm-34': f(niv='connaitre', sp='c26-07', b=1271,
 why=["A Theory of the Consumption Function (1957) expose l’hypothèse du "
      "revenu permanent.",
      "Capitalisme et liberté (1962) est un ouvrage de philosophie "
      "politique libérale.",
      "« Fear of Floating » (2002) est l’article de Calvo et Reinhart, qui "
      "nuance précisément la thèse de Friedman."],
 diss="Conception sous-jacente à expliciter : le taux de change est un prix, "
      "qui doit être déterminé par l’offre et la demande, les autorités ne "
      "disposant pas nécessairement de l’information permettant de fixer une "
      "parité correcte."),
'ch26-qcm-35': f(niv='connaitre', sp='c26-07', b=1356,
 why=["La détermination du taux d’équilibre par le marché est bien le "
      "premier argument.",
      "Le caractère stabilisateur de la spéculation est le deuxième.",
      "L’ajustement automatique de la balance des paiements est le "
      "troisième."],
 diss="Les quatre arguments à restituer dans l’ordre : taux d’équilibre "
      "déterminé par le marché, spéculation stabilisatrice, ajustement "
      "automatique de la balance des paiements, insularisation des politiques "
      "nationales."),
'ch26-qcm-36': f(niv='comprendre', sp='c26-07', b=1456,
 why=["L’isolement des marchés financiers n’est pas le sens de l’argument : "
      "le flottement suppose au contraire leur intégration.",
      "La protection des exportateurs contre le risque de change est "
      "exactement ce que le flottement ne procure pas.",
      "Le flottement n’a pas pour objet de réduire les mouvements de "
      "capitaux."],
 diss="Contre-épreuve décisive : le choc Volcker montre que les politiques "
      "monétaires restent interdépendantes malgré le flottement."),
'ch26-qcm-37': f(niv='raisonner', sp='c26-07', b=1456,
 why=["Les accords du Plaza illustrent la possibilité d’interventions "
      "collectives, non la limite de l’insularisation.",
      "Les crises du SME concernent un régime de changes fixes, non le "
      "flottement.",
      "Le currency board argentin illustre la fragilité des ancrages "
      "rigides."],
 diss="Enchaînement à exposer : durcissement américain → mouvements "
      "internationaux de capitaux → appréciation du dollar → fragilisation "
      "des autres économies."),
'ch26-vraifa-100': f(niv='raisonner', sp='c26-07', b=1425),
'ch26-questi-128': f(niv='raisonner', sp='c26-07', b=1271),

# =============================================================== c26-08
'ch26-qcm-38': f(niv='connaitre', sp='c26-08', b=1465,
 why=["150 milliards sous-estime nettement le cumul retenu par le cours.",
      "750 milliards le surestime.",
      "1 200 milliards est très au-delà des ordres de grandeur de la "
      "période."]),
'ch26-qcm-39': f(niv='connaitre', sp='c26-08', b=1489,
 why=["La conversion en or n’est pas le mécanisme : les recettes sont "
      "placées en actifs financiers.",
      "L’indexation du prix du pétrole sur le dollar est un fait distinct, "
      "qui explique la dénomination « pétrodollars » mais non le recyclage.",
      "Le réinvestissement dans l’exploration est un emploi industriel des "
      "profits, non un recyclage financier international."],
 diss="Enchaînement à retenir : excédents OPEP → dépôts dans les banques "
      "occidentales → prêts aux pays en développement → expansion du crédit "
      "international dans les années 1970."),
'ch26-qcm-40': f(niv='raisonner', sp='c26-08', b=1522,
 why=["Le prix du pétrole et la récession jouent un rôle aggravant par les "
      "recettes d’exportation, mais ce n’est pas le double mécanisme "
      "principal.",
      "La dévaluation des monnaies émergentes est une conséquence, non la "
      "cause.",
      "La fuite des capitaux et le contrôle des changes sont des réactions "
      "ultérieures."],
 diss="Double effet à nommer précisément : les taux variables renchérissent "
      "le service de la dette, l’appréciation du dollar alourdit le principal "
      "libellé en monnaie américaine."),
'ch26-qcm-41': f(niv='connaitre', sp='c26-08', b=1548,
 why=["120 et 450 milliards ne correspondent pas aux chiffres du cours.",
      "L’inversion des deux valeurs décrirait un désendettement.",
      "66 et 12 milliards sont les montants du service de la dette, non de "
      "la dette elle-même."],
 diss="Chiffre complémentaire décisif : le service de la dette passe "
      "d’environ 12 à 66 milliards de dollars sur la même période."),
'ch26-qcm-42': f(niv='connaitre', sp='c26-08', b=1554,
 why=["La crise asiatique intervient en 1997-1998, bien après.",
      "La crise argentine de 2002 marque l’abandon du currency board, autre "
      "épisode.",
      "Les crises du SME de 1992-1993 concernent les changes fixes "
      "européens."],
 diss="Enchaînement causal complet : choc Volcker → hausse des taux "
      "américains et appréciation du dollar → crise mexicaine de 1982 → crise "
      "internationale de la dette."),
'ch26-qcm-43': f(niv='connaitre', sp='c26-08', b=1618,
 why=["Les changes fixes ne suppriment pas la contrainte extérieure : ils "
      "la renforcent, puisqu’il faut défendre la parité.",
      "La stimulation des exportations relève d’une dévaluation, non de la "
      "fixité en elle-même.",
      "La baisse des taux d’intérêt n’est pas un avantage propre des changes "
      "fixes : la défense de la parité peut au contraire les élever."],
 diss="Les deux avantages à formuler précisément : réduire l’incertitude et "
      "les coûts de transaction pour les agents engagés dans les échanges, et "
      "discipliner la politique monétaire en ancrant les anticipations "
      "d’inflation."),
'ch26-qcm-44': f(niv='connaitre', sp='c26-08', b=1671,
 why=["Friedman (1953) défend au contraire les changes flottants.",
      "Balassa et Samuelson (1964) analysent les écarts de prix liés à la "
      "productivité.",
      "Jean-Marc Daniel (2015) propose une lecture historique du triangle de "
      "Mundell."]),
'ch26-qcm-45': f(niv='comprendre', sp='c26-08', b=1671,
 why=["La faiblesse des réserves et l’absence de convertibilité sont des "
      "contraintes réelles, mais ce ne sont pas les deux raisons retenues.",
      "L’inflation intérieure et le déficit budgétaire sont des déséquilibres "
      "internes.",
      "La spéculation et les coûts de transaction sont des caractéristiques "
      "du marché des changes."],
 diss="Effet de bilan à expliciter : les dettes libellées en devises "
      "s’alourdissent après une dépréciation, alors que les revenus restent "
      "en monnaie nationale."),
'ch26-questi-129': f(niv='raisonner', sp='c26-08', b=1489),
'ch26-questi-130': f(niv='raisonner', sp='c26-08', b=1642),

# =============================================================== c26-09
'ch26-qcm-25': f(niv='connaitre', sp='c26-09', b=1810,
 why=["Mars 1983 est le tournant de la rigueur en France.",
      "Janvier 1979 est la date d’entrée en vigueur du Système monétaire "
      "européen.",
      "Janvier 1999 est la création de l’euro."],
 diss="Lecture théorique de l’épisode : les crises de 1992-1993 révèlent la "
      "contradiction entre changes fixes européens et mobilité croissante des "
      "capitaux — exactement le triangle de Mundell."),
'ch26-qcm-46': f(niv='connaitre', sp='c26-09', b=1726,
 why=["Croissance, emploi et stabilité des prix sont des objectifs de "
      "politique macroéconomique interne.",
      "Équilibre interne, externe et budgétaire relèvent de l’analyse des "
      "dilemmes de politique économique.",
      "Convertibilité, flottement et union monétaire sont des modalités "
      "d’organisation monétaire, non les trois sommets."]),
'ch26-qcm-47': f(niv='comprendre', sp='c26-09', b=1705,
 why=["La possibilité de dévaluer relève de la politique de change, non de "
      "l’autonomie monétaire au sens du triangle.",
      "La suppression du risque de change est l’avantage attendu de la "
      "stabilité des changes.",
      "L’attraction des capitaux étrangers est une conséquence possible d’un "
      "taux élevé, non la justification de l’autonomie."],
 diss="Repère concret à citer : dans les économies avancées, les banques "
      "centrales visent généralement une inflation proche de 2 %, ce qui "
      "suppose de pouvoir ajuster les taux à la situation nationale."),
'ch26-qcm-48': f(niv='raisonner', sp='c26-09', b=1730,
 why=["La convergence vers le flottement généralisé est précisément la "
      "lecture téléologique que Daniel écarte.",
      "Il ne démontre la supériorité d’aucun régime : il constate que tous "
      "ont été essayés.",
      "L’histoire monétaire ne se réduit pas à celle du dollar dans cette "
      "lecture."],
 diss="Citation très utilisable : « Le monde a accompli une sorte de parcours "
      "complet en essayant toutes les éventualités offertes par le triangle "
      "des incompatibilités de Robert Mundell. »"),
'ch26-qcm-49': f(niv='comprendre', sp='c26-09', b=1746,
 why=["La convertibilité du dollar en or est un élément du système, mais "
      "elle n’est pas ce qui permet de concilier les deux objectifs.",
      "Les interventions coordonnées des banques centrales caractérisent "
      "plutôt le Plaza et le Louvre, en régime flottant.",
      "Le rôle du FMI comme prêteur accompagne le système sans résoudre le "
      "triangle."],
 diss="Expression à employer : la « fermeture du bas de la balance des "
      "paiements » — en limitant la mobilité des capitaux, le système "
      "sacrifie le troisième sommet."),
'ch26-qcm-51': f(niv='connaitre', sp='c26-09', b=1775,
 why=["Février 1973 marque le passage au flottement généralisé des "
      "principales monnaies, postérieur à la suspension.",
      "Septembre 1985 est la date des accords du Plaza.",
      "Août 1993 est l’élargissement des marges du SME."],
 diss="Conséquence sur le triangle : à partir de 1973, le système privilégie "
      "la mobilité des capitaux et l’autonomie monétaire, au prix de la "
      "stabilité des changes."),
'ch26-qcm-52': f(niv='raisonner', sp='c26-09', b=1844,
 why=["La libre circulation des capitaux est au contraire pleinement "
      "préservée dans l’Union.",
      "La stabilité des changes entre membres est précisément ce que la "
      "monnaie unique garantit de façon absolue.",
      "Aucun dispositif ne permet de sortir du triangle : il s’agit "
      "toujours d’un arbitrage entre trois objectifs."],
 diss="Formule à retenir : l’euro est une réponse institutionnelle au "
      "triangle, et non une exception à celui-ci."),
'ch26-questi-131': f(niv='raisonner', sp='c26-09', b=1726),

# =============================================================== c26-10
'ch26-qcm-26': f(niv='appliquer', sp='c26-10', b=1930,
 why=["Vendre des devises et acheter sa monnaie reviendrait à soutenir la "
      "monnaie, donc à accentuer l’appréciation.",
      "Relever le taux directeur attirerait davantage de capitaux et "
      "renforcerait l’appréciation.",
      "Réduire les réserves de change n’est pas une opération : c’est la "
      "conséquence d’une défense contre une dépréciation."],
 diss="Asymétrie fondamentale à souligner : freiner une appréciation est "
      "relativement facile, puisque la banque centrale peut créer sa propre "
      "monnaie, alors que la défense contre une dépréciation est limitée par "
      "ses réserves."),
'ch26-qcm-53': f(niv='appliquer', sp='c26-10', b=1911,
 why=["L’appréciation accompagnerait au contraire une politique monétaire "
      "restrictive.",
      "L’affirmer sans effet contredirait le mécanisme de parité des taux "
      "d’intérêt.",
      "Aucune intervention n’est requise en changes flottants : c’est "
      "précisément la différence avec les changes fixes."],
 diss="Enchaînement complet : offre de monnaie ↑ → taux d’intérêt ↓ → sorties "
      "de capitaux → dépréciation → compétitivité-prix ↑ → exportations "
      "nettes ↑ → IS vers la droite."),
'ch26-qcm-54': f(niv='raisonner', sp='c26-10', b=1899,
 why=["Le FMI n’interdit pas les dévaluations : il encadre certaines "
      "procédures.",
      "L’inflation importée est un coût réel, mais le cours présente la "
      "relativité des taux de change comme la limite fondamentale.",
      "La limitation des réserves concerne la défense d’une parité, non la "
      "guerre des monnaies."],
 diss="Nature de l’argument à préciser : c’est une impossibilité logique, et "
      "non seulement un coût — une dépréciation chez l’un est une "
      "appréciation chez l’autre."),
'ch26-qcm-55': f(niv='raisonner', sp='c26-10', b=1891,
 why=["La manipulation n’est pas démontrée : c’est exactement la nuance que "
      "le cours apporte.",
      "Le yuan n’est pas librement flottant, mais ce n’est pas la raison de "
      "la prudence du cours.",
      "Le FMI n’a pas tranché la question dans les termes du cours."],
 diss="Distinction méthodologique à conserver : le mécanisme invoqué est "
      "clair — monnaie sous-évaluée → produits moins chers → "
      "compétitivité-prix ↑ — mais sa preuve ne l’est pas."),
'ch26-qcm-56': f(niv='connaitre', sp='c26-10', b=1984,
 why=["Dévaluation, réévaluation et flottement sont des régimes ou des "
      "décisions de parité, non les trois instruments.",
      "Réserves et swaps sont des moyens, et les droits de douane relèvent "
      "de la politique commerciale.",
      "Politiques budgétaire, monétaire et structurelle sont les grandes "
      "catégories de politique économique."],
 diss="Les trois instruments à détailler : intervention directe sur le "
      "marché des changes, taux d’intérêt agissant sur l’attractivité des "
      "placements, contrôle des changes restreignant les opérations en "
      "devises."),
'ch26-qcm-57': f(niv='raisonner', sp='c26-10', b=1942,
 why=["La position des marchés n’entre pas dans ce raisonnement.",
      "La coordination internationale peut être utile dans les deux cas : ce "
      "n’est pas le critère.",
      "L’effet sur l’inflation n’explique pas l’asymétrie des moyens."],
 diss="Conséquence majeure à tirer : c’est cette asymétrie qui rend les "
      "attaques spéculatives possibles contre une monnaie, puisque les "
      "réserves sont nécessairement finies."),
'ch26-questi-132': f(niv='raisonner', sp='c26-10', b=1921),

# =============================================================== c26-11
'ch26-qcm-50': f(niv='connaitre', sp='c26-11', b=2008,
 why=["5 % ne correspond pas au seuil mentionné.",
      "15 % est également évoqué dans la retranscription, mais le cours "
      "retient 10 % comme référence.",
      "20 % ne figure pas dans le cours."],
 diss="Prudence que le cours recommande explicitement : ne pas présenter ces "
      "chiffres comme une règle générale et permanente d’autorisation "
      "automatique."),
'ch26-qcm-59': f(niv='connaitre', sp='c26-11', b=2131,
 why=["Une somme inférieure à 1 correspond au cas où le solde se détériore.",
      "Le produit des élasticités n’est pas le critère retenu.",
      "La différence des élasticités n’a pas de signification dans cette "
      "condition."],
 diss="Les trois cas à distinguer : somme supérieure à 1 (amélioration), "
      "égale à 1 (effet nul dans le cadre simplifié), inférieure à 1 "
      "(détérioration)."),
'ch26-qcm-60': f(niv='appliquer', sp='c26-11', b=2072,
 why=["− 4,8 est le résultat du cas inverse, avec des élasticités de 0,3 et "
      "0,2.",
      "+ 8 correspondrait au seul effet sur les exportations, sans tenir "
      "compte des importations.",
      "− 2,4 ne correspond à aucun des deux calculs du cours."],
 diss="Détail du calcul à reproduire : exportations 108, importations "
      "100 × 1,10 × 0,94 = 103,4, donc solde + 4,6."),
'ch26-qcm-61': f(niv='raisonner', sp='c26-11', b=2134,
 why=["Affirmer qu’une dévaluation de 10 % améliore toujours le solde "
      "contredit directement l’illustration chiffrée.",
      "Les élasticités ne sont pas toujours supérieures à 1 : c’est tout "
      "l’enjeu de la condition de Marshall-Lerner.",
      "L’effet-prix est au contraire déterminant à court terme, comme le "
      "montre la courbe en J."],
 diss="Déterminants des élasticités à mentionner : la spécialisation "
      "productive et la structure des importations."),
'ch26-qcm-62': f(niv='connaitre', sp='c26-11', b=2082,
 why=["La domination des effets-volume correspond à la phase 2.",
      "L’érosion des gains par l’inflation importée correspond à la phase 3.",
      "L’amélioration du solde est précisément ce qui n’a pas encore lieu en "
      "phase 1."],
 diss="Les trois phases à restituer : effets-prix et dégradation à court "
      "terme, effets-volume et redressement à moyen terme, puis amélioration "
      "ou érosion selon l’inflation importée."),
'ch26-qcm-63': f(niv='raisonner', sp='c26-11', b=2167,
 why=["Une économie spécialisée hors prix bénéficie au contraire faiblement "
      "d’une dévaluation.",
      "Rien ne l’empêche de dévaluer : c’est l’efficacité de la mesure qui "
      "est en cause.",
      "Ses élasticités sont au contraire plutôt faibles."],
 diss="Nuance du cours à reprendre : une faible sensibilité aux prix peut "
      "traduire un fort pouvoir de marché plutôt qu’un manque de "
      "compétitivité."),
'ch26-qcm-64': f(niv='raisonner', sp='c26-11', b=2170,
 why=["La désindustrialisation réduit au contraire la capacité d’ajustement "
      "par les volumes.",
      "Le comportement de marge est un mécanisme distinct, lié aux décisions "
      "de prix des exportateurs.",
      "L’inflation importée est une conséquence de la dévaluation, non le "
      "canal propre à la désindustrialisation."],
 diss="Mécanisme à expliciter : sans appareil productif national, il n’existe "
      "pas de substitut aux importations — la facture augmente sans que les "
      "volumes diminuent."),
'ch26-questi-133': f(niv='raisonner', sp='c26-11', b=2072),

# =============================================================== c26-12
'ch26-qcm-58': f(niv='connaitre', sp='c26-12', b=2347,
 why=["L’ampleur ne distingue pas les deux : une dévaluation subie peut être "
      "considérable.",
      "La notion de dévaluation suppose un régime de changes fixes : une "
      "monnaie flottante se déprécie.",
      "L’autorisation du FMI concerne une procédure, non la nature de la "
      "décision."],
 diss="Application décisive : les trois dévaluations françaises de 1981-1983 "
      "sont principalement subies, non compétitives."),
'ch26-qcm-65': f(niv='comprendre', sp='c26-12', b=2212,
 why=["L’augmentation des volumes exportés est l’effet attendu, précisément "
      "contrarié par ce comportement.",
      "La délocalisation est une stratégie distincte.",
      "L’augmentation des importations d’intrants est un autre canal "
      "d’affaiblissement, lié au contenu importé des exportations."],
 diss="Arbitrage à nommer : baisser ses prix en devises pour gagner des "
      "volumes, ou maintenir ses prix pour reconstituer ses marges — le degré "
      "de concurrence détermine le choix."),
'ch26-qcm-66': f(niv='raisonner', sp='c26-12', b=2300,
 why=["L’enchaînement vertueux décrit l’effet attendu d’une dévaluation "
      "réussie, non le cercle vicieux.",
      "La hausse des réserves et de la crédibilité décrirait une "
      "stabilisation, à l’inverse.",
      "L’excédent et l’appréciation décriraient un ajustement complet et "
      "favorable."],
 diss="Mécanisme central à maîtriser : les effets de second tour sur les "
      "salaires et les coûts érodent le gain initial, le déficit persiste, la "
      "spéculation à la baisse s’installe."),
'ch26-qcm-67': f(niv='raisonner', sp='c26-12', b=2266,
 why=["L’annonce des intentions de la banque centrale n’est pas le mécanisme "
      "décrit : elle cherche au contraire à défendre la parité.",
      "La validation du FMI n’intervient pas dans ce processus de marché.",
      "L’inflation importée est une conséquence de la dévaluation, non la "
      "cause de son déclenchement."],
 diss="Exemple cité par le cours : le peso argentin, dont la défense de la "
      "parité devient impossible lorsque les réserves s’épuisent."),
'ch26-qcm-68': f(niv='connaitre', sp='c26-12', b=2306,
 why=["Raymond Barre est Premier ministre jusqu’en 1981, avant la relance.",
      "Laurent Fabius devient Premier ministre en 1984, après le tournant de "
      "la rigueur.",
      "Michel Rocard est Premier ministre à partir de 1988."],
 diss="Enchaînement défavorable à décrire : relance de la demande → "
      "importations ↑ → déséquilibre extérieur accentué."),
'ch26-qcm-69': f(niv='connaitre', sp='c26-12', b=2308,
 why=["8 % sous-estime nettement le niveau atteint.",
      "11 % reste en deçà du chiffre retenu par le cours.",
      "18 % le surestime."],
 diss="Comparaison indispensable : nettement davantage qu’en Allemagne, d’où "
      "la dégradation de la compétitivité-prix française à parité "
      "inchangée."),
'ch26-qcm-70': f(niv='connaitre', sp='c26-12', b=2347,
 why=["Mai 1981 est la date de la relance, non d’une dévaluation.",
      "Juin 1981 et mars 1982 ne correspondent pas aux dates retenues.",
      "Ces dates sont toutes postérieures d’un an aux dévaluations "
      "effectives."],
 diss="Qualification à justifier : il s’agit principalement de dévaluations "
      "subies, les autorités cherchant initialement à maintenir le franc dans "
      "le SME."),
'ch26-qcm-71': f(niv='raisonner', sp='c26-12', b=2347,
 why=["Le franc n’est pas sorti du SME : c’est précisément le choix "
      "inverse.",
      "L’euro est créé en 1999.",
      "L’élargissement des marges du SME intervient en août 1993."],
 diss="Logique du retournement à expliquer : les dévaluations n’ayant pas "
      "restauré la compétitivité — elles renchérissaient les importations et "
      "entretenaient l’inflation — la stratégie est inversée."),
'ch26-questi-134': f(niv='raisonner', sp='c26-12', b=2300),
'ch26-questi-135': f(niv='raisonner', sp='c26-12', b=2306),

}
