# -*- coding: utf-8 -*-
"""Chapitre 25 — corrections des questions héritées, sous-parties c25-01 à c25-06."""


def f(**kw):
    return kw


FIX = {

# =============================================================== c25-01
'ch25-qcm-9': f(niv='connaitre', sp='c25-01', b=132,
 why=["La demande solvable des ménages est une notion de pouvoir d’achat, "
      "non d’anticipation.",
      "La demande réalisée ex post est constatée après coup : elle ne peut "
      "donc pas déterminer la production décidée avant.",
      "La demande publique n’est qu’une composante de la demande globale."],
 diss="Conséquence décisive : le chômage devient involontaire, puisqu’il "
      "résulte d’une insuffisance de débouchés anticipés et non d’un refus de "
      "travailler au salaire d’équilibre."),
'ch25-qcm-44': f(niv='appliquer', sp='c25-01', b=215,
 why=["PIB = C + I + G est l’égalité en économie fermée.",
      "PIB = C + S décrit l’utilisation du revenu, non l’équilibre "
      "emplois-ressources.",
      "Placer X à gauche et M à droite inverse les ressources et les "
      "emplois : les importations sont une ressource."],
 diss="Réécriture à maîtriser : PIB = C + I + G + X − M, d’où l’on tire que "
      "les exportations nettes sont une composante de la demande adressée aux "
      "producteurs nationaux."),
'ch25-qcm-45': f(niv='connaitre', sp='c25-01', b=187,
 why=["L’emploi et les prix ne constituent pas des approches du PIB mais des "
      "variables associées.",
      "La monnaie n’est pas une approche du PIB.",
      "Valeur, volume et prix désignent des modes de mesure d’une même "
      "grandeur, non trois approches."],
 diss="Les trois approches conduisent au même PIB aux ajustements "
      "statistiques près : c’est ce qui garantit la cohérence du cadre "
      "comptable."),
'ch25-qcm-46': f(niv='comprendre', sp='c25-01', b=109,
 why=["L’optimalité au sens de Pareto ne dit rien de l’équité : une "
      "répartition très inégale peut être optimale.",
      "Le plein emploi n’est pas garanti par l’optimum de Pareto.",
      "L’absence d’externalités est une hypothèse qui permet d’atteindre "
      "l’optimum, non sa définition."],
 diss="Mise en garde explicite du cours : une intervention publique peut "
      "corriger des défaillances de marché sans perte de bien-être."),
'ch25-qcm-47': f(niv='connaitre', sp='c25-01', b=95,
 why=["La négociation entre partenaires sociaux relève d’une analyse "
      "institutionnelle du marché du travail.",
      "L’ajustement par les quantités est au contraire la logique "
      "keynésienne, où ce sont les volumes et non les prix qui s’ajustent.",
      "La formation des anticipations est un autre problème, central chez "
      "Keynes puis chez les monétaristes."],
 diss="Point de méthode utile : le commissaire-priseur est une fiction "
      "théorique, un idéal-type au sens de Weber, et non une description du "
      "réel."),
'ch25-qcm-49': f(niv='connaitre', sp='c25-01', b=24,
 why=["Durkheim travaille sur le fait social et la méthode "
      "sociologique, non sur l’idéal-type.",
      "Pareto est mobilisé pour l’optimum, non pour cette notion "
      "méthodologique.",
      "Marx développe le matérialisme historique."],
 diss="Justification méthodologique à réemployer : un modèle accentue "
      "certains traits du réel pour en faciliter l’analyse, comme le fait la "
      "concurrence pure et parfaite."),
'ch25-qcm-50': f(niv='raisonner', sp='c25-01', b=46,
 why=["L’instabilité de la croissance est la conclusion de Harrod-Domar, non "
      "celle des deux modèles.",
      "La détermination de l’investissement par l’épargne est une hypothèse "
      "de certains modèles, pas la leçon de la comparaison.",
      "L’exogénéité du progrès technique caractérise Solow, mais ce n’est "
      "pas l’enseignement de la confrontation."],
 diss="Leçon d’épistémologie très valorisable : la conclusion d’un modèle est "
      "toujours relative à ses hypothèses, ce qui oblige à les expliciter "
      "avant de l’utiliser."),
'ch25-questi-115': f(niv='raisonner', sp='c25-01', b=14),

# =============================================================== c25-02
'ch25-qcm-2': f(niv='connaitre', sp='c25-02', b=361,
 why=["L’équilibre du marché de la monnaie est représenté par la courbe LM.",
      "L’équilibre extérieur est représenté par la courbe BP, dans le modèle "
      "Mundell-Fleming.",
      "Le marché du travail n’est pas représenté par une courbe du modèle "
      "IS-LM : c’est l’une de ses limites."],
 diss="Étymologie à citer : IS pour Investment-Saving, LM pour Liquidity "
      "preference-Money supply."),
'ch25-qcm-19': f(niv='connaitre', sp='c25-02', b=374,
 why=["La relation inflation-chômage est la reformulation postérieure, due à "
      "Lipsey puis à Samuelson et Solow en 1960.",
      "La relation production-chômage est la loi d’Okun (1962).",
      "La relation monnaie-prix renvoie à la théorie quantitative de la "
      "monnaie."],
 diss="Précision qui distingue une bonne copie : Phillips relie chômage et "
      "salaires nominaux, pas chômage et inflation."),
'ch25-qcm-22': f(niv='appliquer', sp='c25-02', b=429,
 why=["Une hausse simultanée de la production et des prix correspond à un "
      "choc de demande positif.",
      "Une baisse simultanée de la production et des prix correspond à un "
      "choc de demande négatif.",
      "Un choc d’offre affecte précisément les prix : les en déclarer "
      "indépendants contredit le mécanisme."],
 diss="Configuration à nommer : la stagflation des chocs pétroliers, que "
      "l’arbitrage inflation-chômage ne permettait pas d’interpréter."),
'ch25-qcm-23': f(niv='connaitre', sp='c25-02', b=433,
 why=["Les prix flexibles sont au contraire l’hypothèse du modèle OG-DG.",
      "L’ouverture de l’économie est introduite par le modèle "
      "Mundell-Fleming, avec la courbe BP.",
      "L’offre de monnaie est supposée exogène, fixée par les autorités "
      "monétaires."],
 diss="Les trois hypothèses à restituer ensemble : monnaie active, "
      "raisonnement de court terme, niveau général des prix fixe."),
'ch25-qcm-40': f(niv='connaitre', sp='c25-02', b=284,
 why=["Hansen prolonge le modèle en 1941 dans Fiscal Policy and Business "
      "Cycles : il ne le formalise pas le premier.",
      "Mundell étend le modèle à l’économie ouverte, bien plus tard.",
      "Kahn développe le multiplicateur d’emploi en 1931."],
 diss="On parle de tradition Hicks-Hansen : Hicks formalise en 1937, Hansen "
      "diffuse et prolonge."),
'ch25-qcm-62': f(niv='connaitre', sp='c25-02', b=302,
 why=["Hicks est l’auteur de la formalisation du modèle IS-LM.",
      "Mundell est associé au triangle des incompatibilités et au modèle en "
      "économie ouverte.",
      "Romer est mobilisé pour la croissance endogène."],
 diss="Notion très actuelle : la stagnation séculaire est réapparue dans le "
      "débat après 2008, ce qui éclaire la réhabilitation d’IS-LM."),
'ch25-qcm-63': f(niv='connaitre', sp='c25-02', b=447,
 why=["La courbe de Phillips est due à Phillips, puis reformulée par Lipsey, "
      "Samuelson et Solow.",
      "L’équivalence ricardienne est associée à Barro (1974).",
      "Le multiplicateur est développé par Kahn (1931) puis Keynes (1936)."],
 diss="Articulation précieuse : Romer fournit l’argument théorique des "
      "politiques visant la croissance potentielle, donc structurelles."),
'ch25-qcm-69': f(niv='comprendre', sp='c25-02', b=263,
 why=["Réduire l’investissement au seul taux d’intérêt est précisément "
      "l’analyse classique que Keynes complète.",
      "La nécessité d’une épargne préalable est la causalité classique, "
      "inversée par Keynes.",
      "Le niveau général des prix est supposé fixe dans le modèle IS-LM."],
 diss="Conséquence essentielle : une baisse des taux peut rester sans effet "
      "si les anticipations sont très pessimistes — ce qui annonce la trappe "
      "à liquidité."),
'ch25-questi-110': f(niv='raisonner', sp='c25-02', b=433),

# =============================================================== c25-03
'ch25-qcm-1': f(niv='appliquer', sp='c25-03', b=519,
 why=["Multiplier par (1 − c) au lieu de diviser inverse l’effet du "
      "multiplicateur.",
      "Ajouter c à la demande autonome n’a aucun sens dimensionnel.",
      "Diviser par c ferait de la propension à consommer, et non de la "
      "propension à épargner, le dénominateur."],
 diss="Lecture économique du dénominateur : (1 − c) est la propension "
      "marginale à épargner, c’est-à-dire la fuite qui amortit le "
      "multiplicateur."),
'ch25-qcm-20': f(niv='connaitre', sp='c25-03', b=632,
 why=["La relation inflation-chômage est celle de la courbe de Phillips "
      "reformulée.",
      "La relation monnaie-taux d’intérêt relève du marché monétaire.",
      "La relation épargne-investissement est l’égalité I = S."],
 diss="Attention à la nuance du cours : Okun relie production et chômage ; "
      "l’interprétation inflationniste de l’output gap relève d’une autre "
      "analyse."),
'ch25-qcm-21': f(niv='comprendre', sp='c25-03', b=628,
 why=["La surchauffe correspond à un output gap positif.",
      "L’excédent extérieur est un solde de balance des paiements, sans "
      "rapport direct avec l’écart de production.",
      "L’inflation importée résulte du prix des importations, non de l’écart "
      "de production."],
 diss="Symétrie à retenir : output gap négatif → sous-utilisation et "
      "chômage ; output gap positif → tensions susceptibles d’alimenter "
      "l’inflation."),
'ch25-qcm-39': f(niv='connaitre', sp='c25-03', b=465,
 why=["Hicks formalise le modèle IS-LM.",
      "Hansen prolonge la tradition keynésienne américaine.",
      "Okun est l’auteur de la loi reliant production et chômage."],
 diss="Lecture du graphique : la bissectrice rassemble les points où le "
      "revenu est égal à la demande globale, donc où la production trouve "
      "exactement ses débouchés."),
'ch25-qcm-42': f(niv='connaitre', sp='c25-03', b=475,
 why=["La consommation incompressible est précisément la lecture que le "
      "cours écarte : C₀ n’est pas un minimum physiologique.",
      "La consommation publique est une composante distincte, notée G.",
      "La consommation des ménages modestes est une catégorie sociale, non "
      "une composante de la fonction."],
 diss="Mise en garde explicite du cours : « autonome » signifie indépendante "
      "du revenu courant dans le modèle, et non impossible à réduire."),
'ch25-qcm-43': f(niv='appliquer', sp='c25-03', b=461,
 why=["L’introduction de G et de T correspond à l’économie avec État, où "
      "l’égalité devient I + G = S + T.",
      "PIB + M = C + I + G + X est l’équilibre emplois-ressources en "
      "économie ouverte.",
      "M = L est la condition d’équilibre du marché de la monnaie."],
 diss="Point d’interprétation capital : cette égalité est comptable et ex "
      "post ; ex ante, épargne désirée et investissement désiré peuvent "
      "différer."),
'ch25-qcm-48': f(niv='comprendre', sp='c25-03', b=577,
 why=["L’insuffisance de la demande globale est l’explication keynésienne, "
      "opposée à celle de Pigou.",
      "La rapidité du progrès technique n’est pas l’explication retenue dans "
      "cette analyse.",
      "Le niveau de l’inflation n’intervient pas dans l’analyse "
      "néoclassique du chômage."],
 diss="Conséquence de politique économique : si le chômage vient d’un salaire "
      "réel trop élevé, le remède est la flexibilité salariale, non la "
      "relance."),
'ch25-vraifa-77': f(niv='comprendre', sp='c25-03', b=547),
'ch25-vraifa-96': f(niv='comprendre', sp='c25-03', b=635),
'ch25-questi-109': f(niv='raisonner', sp='c25-03', b=624),
'ch25-questi-116': f(niv='raisonner', sp='c25-03', b=578),
'ch25-questi-117': f(niv='raisonner', sp='c25-03', b=596),

# =============================================================== c25-04
'ch25-qcm-4': f(niv='appliquer', sp='c25-04', b=869,
 why=["4 correspond au multiplicateur fiscal en valeur absolue, c / (1 − c), "
      "ou au multiplicateur des prestations sociales.",
      "0,8 est la propension marginale à consommer elle-même, non le "
      "multiplicateur.",
      "− 4 est le multiplicateur fiscal, négatif par construction."],
 diss="Quatre multiplicateurs à ne pas confondre : kG = 1/(1 − c), "
      "kF = c/(1 − c), kT = − c/(1 − c), et en économie ouverte "
      "1/(1 − c + m)."),
'ch25-qcm-41': f(niv='connaitre', sp='c25-04', b=749,
 why=["Keynes reprend et généralise le multiplicateur dans la Théorie "
      "générale en 1936 : il ne le développe pas le premier.",
      "Hansen diffuse le keynésianisme aux États-Unis à partir de 1941.",
      "Samuelson est associé au diagramme à 45°."],
 diss="Précision d’attribution appréciée : Kahn 1931 pour le multiplicateur "
      "d’emploi, Keynes 1936 pour sa généralisation."),
'ch25-qcm-70': f(niv='raisonner', sp='c25-04', b=772,
 why=["L’ajustement par le taux d’intérêt est la causalité classique, que "
      "Keynes inverse.",
      "La création monétaire bancaire est un autre mécanisme, qui ne relève "
      "pas du multiplicateur de revenu.",
      "L’emprunt public est un mode de financement, non l’explication de la "
      "formation de l’épargne."],
 diss="Vérification numérique à reproduire : avec s = 0,2 et ΔY = 500, "
      "l’épargne supplémentaire atteint exactement 100, soit l’investissement "
      "initial."),
'ch25-questi-99': f(niv='raisonner', sp='c25-04', b=772),
'ch25-questi-100': f(niv='appliquer', sp='c25-04', b=852),

# =============================================================== c25-05
'ch25-qcm-5': f(niv='comprendre', sp='c25-05', b=915,
 why=["Le montant n’est pas en cause : la comparaison se fait à montant "
      "égal.",
      "Le mode de financement n’explique pas l’écart entre les deux "
      "multiplicateurs.",
      "Les prestations sociales entrent bien dans la demande globale, mais "
      "indirectement, via la consommation des ménages."],
 diss="Formules à comparer : kG = 1/(1 − c) = 5 contre kF = c/(1 − c) = 4 "
      "avec c = 0,8 — l’écart est exactement d’une vague de dépense."),
'ch25-qcm-6': f(niv='comprendre', sp='c25-05', b=952,
 why=["Affirmer qu’une baisse d’impôts réduit le revenu confond le signe du "
      "multiplicateur et le sens de la variation.",
      "Dire que les impôts n’ont aucun effet contredit l’existence même du "
      "multiplicateur fiscal.",
      "Le revenu national ne devient pas négatif : c’est le multiplicateur "
      "qui l’est."],
 diss="Vérification à faire systématiquement : avec ΔT = − 100 et kT = − 4, "
      "ΔY = + 400."),
'ch25-qcm-7': f(niv='appliquer', sp='c25-05', b=1063,
 why=["1/(1 − c) est le multiplicateur en économie fermée.",
      "c/(1 − c + m) correspondrait à un multiplicateur de transfert en "
      "économie ouverte.",
      "1/(1 + c − m) inverse les signes et n’a pas de justification "
      "économique."],
 diss="Interprétation à donner : m est une fuite supplémentaire, au même "
      "titre que l’épargne — dans l’exemple du cours, le multiplicateur passe "
      "de 5 à 2."),
'ch25-qcm-8': f(niv='connaitre', sp='c25-05', b=1042,
 why=["Le rapport importations / PIB mesure un poids, pas une variation : "
      "c’est la confusion que le cours signale.",
      "La part des importations dans la consommation est un autre ratio.",
      "Le taux de couverture rapporte exportations et importations."],
 diss="Définition à écrire telle quelle : m = ΔM / ΔY."),
'ch25-qcm-71': f(niv='comprendre', sp='c25-05', b=979,
 why=["Un multiplicateur plus élevé pour l’investissement public n’est pas "
      "ce que donne le modèle simple, à montant initial égal.",
      "Un multiplicateur nul pour l’investissement public contredirait le "
      "mécanisme.",
      "Un multiplicateur toujours égal à 1 supposerait une propension "
      "marginale à consommer nulle."],
 diss="Nuance du cours à reprendre : l’intérêt propre de l’investissement "
      "public est d’accroître en plus les capacités productives futures, donc "
      "d’agir aussi sur l’offre."),
'ch25-qcm-72': f(niv='raisonner', sp='c25-05', b=1012,
 why=["Le poids électoral est un argument politique, étranger au "
      "raisonnement économique.",
      "La propension à importer des ménages modestes n’est pas l’argument "
      "retenu par le cours.",
      "L’épargne de précaution jouerait au contraire contre l’efficacité de "
      "la relance."],
 diss="Comparaison chiffrée du cours : 95 de consommation initiale pour un "
      "ménage consommant 95 % du revenu supplémentaire, contre 60 pour un "
      "ménage en consommant 60 %."),
'ch25-qcm-73': f(niv='raisonner', sp='c25-05', b=1103,
 why=["La protection des industries naissantes est l’argument de List, de "
      "logique entièrement différente.",
      "La lutte contre le dumping relève des instruments de défense "
      "commerciale.",
      "La sécurité des approvisionnements est un argument de souveraineté."],
 diss="Contrepoint à mentionner immédiatement : le cours confronte cet "
      "argument au coût des restrictions et à l’intérêt d’une coordination "
      "internationale des relances."),
'ch25-questi-111': f(niv='raisonner', sp='c25-05', b=1082),

# =============================================================== c25-06
'ch25-qcm-10': f(niv='connaitre', sp='c25-06', b=1280,
 why=["Épargne et investissement ne sont pas des motifs de détention de "
      "monnaie mais des opérations économiques.",
      "La thésaurisation est une conséquence du motif de spéculation, non un "
      "motif distinct.",
      "Liquidité, rendement et sécurité sont des caractéristiques des "
      "actifs, non les motifs keynésiens."],
 diss="Dépendances à retenir : transaction et précaution dépendent "
      "positivement du revenu, spéculation négativement du taux d’intérêt."),
'ch25-qcm-11': f(niv='comprendre', sp='c25-06', b=1221,
 why=["Une hausse du prix des obligations accompagnerait au contraire une "
      "baisse des taux.",
      "Un prix stable supposerait que les anciennes obligations restent "
      "aussi attractives que les nouvelles, ce qui n’est pas le cas.",
      "Le coupon est fixe : il ne varie pas avec le taux de marché."],
 diss="Trois notions à distinguer rigoureusement : le coupon, fixe ; le prix "
      "de marché, variable ; le rendement de marché, qui en résulte."),
'ch25-qcm-51': f(niv='comprendre', sp='c25-06', b=1148,
 why=["Le marché des fonds prêtables est le cadre de l’analyse classique, "
      "précisément rejetée.",
      "Le marché du travail détermine le salaire, non le taux d’intérêt.",
      "La banque centrale influence le taux, mais chez Keynes celui-ci "
      "résulte de la confrontation entre offre et demande de monnaie."],
 diss="Formule de rupture à citer : le taux d’intérêt devient le prix de la "
      "renonciation à la liquidité."),
'ch25-qcm-52': f(niv='comprendre', sp='c25-06', b=1130,
 why=["Le marché monétaire est le cadre de l’analyse keynésienne.",
      "La demande effective est un concept keynésien.",
      "La balance des paiements intervient dans le modèle Mundell-Fleming, "
      "bien plus tard."],
 diss="Expression à employer : la dichotomie classique sépare sphère réelle "
      "et sphère monétaire, ce que Keynes refuse en rendant la monnaie "
      "active."),
'ch25-vraifa-81': f(niv='raisonner', sp='c25-06', b=1277),
'ch25-questi-102': f(niv='raisonner', sp='c25-06', b=1261),

}
