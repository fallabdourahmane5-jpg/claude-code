# -*- coding: utf-8 -*-
"""Chapitre 25 — corrections des questions héritées, sous-parties c25-07 à c25-12."""


def f(**kw):
    return kw


FIX = {

# =============================================================== c25-07
'ch25-qcm-3': f(niv='comprendre', sp='c25-07', b=1348,
 why=["L’investissement réagit négativement au taux d’intérêt : c’est la "
      "pente décroissante de IS, non celle de LM.",
      "L’effet d’une hausse des prix sur l’offre réelle de monnaie déplace la "
      "courbe LM, il n’explique pas sa pente.",
      "Le financement de l’investissement par l’épargne est la causalité "
      "classique, étrangère à la construction de LM."],
 diss="Enchaînement complet à restituer : Y ↑ → L1 ↑ → vente de titres → prix "
      "des obligations ↓ → r ↑."),
'ch25-qcm-12': f(niv='raisonner', sp='c25-07', b=1620,
 why=["Une politique monétaire très efficace suppose au contraire une LM "
      "pentue et une IS sensible au taux.",
      "L’effet d’éviction devient nul, et non total : le taux d’intérêt ne "
      "monte pas.",
      "LM devient horizontale dans la trappe à liquidité, et non verticale : "
      "la verticalité caractérise la zone classique."],
 diss="Configuration la plus favorable à la politique budgétaire : LM "
      "horizontale, donc pas de hausse des taux, donc pas d’éviction."),
'ch25-qcm-13': f(niv='raisonner', sp='c25-07', b=1418,
 why=["LM horizontale et politique budgétaire efficace décrivent la trappe à "
      "liquidité, situation opposée.",
      "BP n’appartient pas au modèle IS-LM fermé : elle est introduite par "
      "Mundell-Fleming.",
      "IS ne devient pas verticale : c’est LM qui l’est dans cette zone."],
 diss="Les trois zones de LM à connaître : keynésienne (horizontale), "
      "intermédiaire (croissante), classique (verticale) — et les conclusions "
      "de politique économique qui en découlent."),
'ch25-vraifa-93': f(niv='raisonner', sp='c25-07', b=1506),
'ch25-questi-101': f(niv='appliquer', sp='c25-07', b=1434),
'ch25-questi-103': f(niv='raisonner', sp='c25-07', b=1506),

# =============================================================== c25-08
'ch25-qcm-53': f(niv='connaitre', sp='c25-08', b=1728,
 why=["Amortir les fluctuations définit au contraire une politique "
      "contracyclique.",
      "Le cours nuance explicitement : une politique procyclique n’est pas "
      "nécessairement inefficace pour tous les objectifs.",
      "La notion s’applique aussi bien à la politique budgétaire qu’à la "
      "politique monétaire."],
 diss="Définition rigoureuse : est procyclique une politique qui amplifie le "
      "cycle, ce qui contredit l’objectif de stabilisation sans être "
      "nécessairement irrationnel."),
'ch25-qcm-54': f(niv='appliquer', sp='c25-08', b=1838,
 why=["Budget expansionniste et monnaie restrictive correspondent au policy "
      "mix de la réunification allemande.",
      "Deux politiques expansionnistes provoqueraient des tensions "
      "inflationnistes.",
      "Deux politiques restrictives réduiraient fortement l’activité."],
 diss="Lecture graphique à restituer : IS se déplace vers la gauche, LM vers "
      "la droite — le revenu est préservé et le taux d’intérêt baisse."),
'ch25-qcm-56': f(niv='connaitre', sp='c25-08', b=1813,
 why=["− 2,7 % à − 0,8 % sous-estime à la fois le déficit initial et le "
      "redressement obtenu.",
      "L’inversion des deux valeurs décrirait une dégradation, non un "
      "redressement.",
      "− 6 % à 0 % ne correspond pas aux chiffres du cours."],
 diss="Chiffres complémentaires à citer : la croissance atteint 3,7 % en 1998 "
      "et les taux à un an reculent de 5,5 % à 4,8 %."),
'ch25-vraifa-91': f(niv='raisonner', sp='c25-08', b=1836),

# =============================================================== c25-09
'ch25-qcm-14': f(niv='connaitre', sp='c25-09', b=2011,
 why=["La substitution des importations à la production nationale est une "
      "fuite du multiplicateur, non l’effet d’éviction.",
      "L’exclusion des ménages modestes du crédit est un phénomène de "
      "rationnement, distinct.",
      "Le remplacement de la monnaie nationale par une devise est la "
      "dollarisation."],
 diss="Enchaînement à écrire systématiquement : G ↑ → Y ↑ → demande de "
      "monnaie ↑ → r ↑ → I privé ↓."),
'ch25-qcm-15': f(niv='comprendre', sp='c25-09', b=2057,
 why=["La dépendance au revenu courant est l’hypothèse keynésienne que "
      "Friedman conteste.",
      "La dépendance de l’épargne au taux d’intérêt est une autre analyse, "
      "classique.",
      "Le revenu permanent n’est pas le seul revenu du travail : il intègre "
      "l’ensemble des ressources anticipées."],
 diss="Conséquence pour la politique économique : un transfert perçu comme "
      "temporaire est largement épargné, ce qui affaiblit le multiplicateur "
      "attendu."),
'ch25-qcm-55': f(niv='appliquer', sp='c25-09', b=1888,
 why=["Budget restrictif et monnaie accommodante correspondent au policy mix "
      "Clinton-Greenspan.",
      "Deux politiques restrictives auraient fortement comprimé l’activité, "
      "ce que les dépenses de réunification excluaient.",
      "Deux politiques expansionnistes auraient aggravé les tensions "
      "inflationnistes que la Bundesbank combattait."],
 diss="Conséquence européenne décisive : ces taux élevés se transmettent aux "
      "partenaires du Système monétaire européen, ce qui alimente la crise de "
      "1992-1993."),
'ch25-qcm-57': f(niv='connaitre', sp='c25-09', b=1870,
 why=["5,5 % sous-estime nettement la hausse effective.",
      "7,1 % reste en deçà du niveau atteint.",
      "12 % surestime le niveau retenu par le cours."],
 diss="Contexte budgétaire à joindre : le solde se dégrade de + 0,2 % du PIB "
      "en 1989 à − 2,9 % en 1991."),
'ch25-qcm-67': f(niv='raisonner', sp='c25-09', b=2011,
 why=["Un effet d’éviction faible correspond à une LM peu pentue, voire "
      "horizontale.",
      "L’inefficacité de la politique monétaire caractérise la trappe à "
      "liquidité, où LM est horizontale.",
      "BP n’intervient pas dans le modèle fermé."],
 diss="Règle générale à mémoriser : plus LM est pentue, plus l’éviction est "
      "forte et plus la politique budgétaire perd en efficacité."),
'ch25-vraifa-82': f(niv='raisonner', sp='c25-09', b=1956),
'ch25-questi-113': f(niv='raisonner', sp='c25-09', b=1911),

# =============================================================== c25-10
'ch25-qcm-16': f(niv='comprendre', sp='c25-10', b=2084,
 why=["Affirmer que la dette publique n’a aucun coût est l’inverse du "
      "raisonnement de Barro.",
      "La proportionnalité des impôts n’est pas l’objet de l’équivalence.",
      "Ricardo et Barro ne développent pas la même analyse : le nom de "
      "l’équivalence est une référence, non une identité de thèse."],
 diss="Les trois hypothèses à mentionner : des agents informés, capables "
      "d’épargner et raisonnant sur un horizon long."),
'ch25-qcm-17': f(niv='comprendre', sp='c25-10', b=2137,
 why=["Un taux naturel nul n’aurait aucun sens : il existe toujours des "
      "frictions.",
      "L’abaissement durable par la politique monétaire est exactement ce que "
      "Friedman exclut.",
      "Le chômage frictionnel n’est qu’une des composantes du chômage "
      "naturel."],
 diss="Nuance à conserver : le taux naturel n’est pas immuable, mais il se "
      "modifie par des politiques structurelles et non par une relance de la "
      "demande."),
'ch25-qcm-18': f(niv='raisonner', sp='c25-10', b=2169,
 why=["Une hausse durable de la production supposerait des capacités "
      "disponibles, ce qui est exclu au plein emploi.",
      "BP n’intervient pas dans ce raisonnement en économie fermée.",
      "Le taux d’intérêt augmente au contraire, puisque l’offre réelle de "
      "monnaie diminue."],
 diss="Enchaînement complet : prix ↑ → offre réelle de monnaie ↓ → LM vers la "
      "gauche → r ↑ → éviction de l’investissement privé → retour au niveau "
      "potentiel avec un taux plus élevé."),
'ch25-qcm-38': f(niv='comprendre', sp='c25-10', b=2233,
 why=["L’inflation importée relève de l’analyse en économie ouverte, non du "
      "modèle IS-LM fermé.",
      "Les chaînes de valeur mondiales ne figurent pas dans ce modèle.",
      "La croissance endogène est un cadre de long terme, associé à Romer."],
 diss="Argument décisif de la réhabilitation : près du plancher des taux, la "
      "politique monétaire conventionnelle perd son efficacité tandis que "
      "l’éviction budgétaire devient très limitée."),
'ch25-qcm-66': f(niv='raisonner', sp='c25-10', b=2242,
 why=["En zone classique, LM est verticale et l’éviction est au contraire "
      "totale.",
      "Les changes flexibles produisent une éviction par le taux de change, "
      "non son annulation.",
      "Une forte sensibilité de l’investissement au taux accroît l’éviction, "
      "elle ne la supprime pas."],
 diss="Symétrie à exploiter : éviction totale en zone classique, nulle dans "
      "la trappe à liquidité, partielle entre les deux."),
'ch25-qcm-68': f(niv='comprendre', sp='c25-10', b=2163,
 why=["Une hausse du taux d’intérêt accompagnerait une contraction "
      "monétaire.",
      "L’absence d’effet contredirait le mécanisme d’ajustement par le "
      "marché des titres.",
      "Une hausse de l’offre de monnaie déplace LM, non IS."],
 diss="Mécanisme d’ajustement à détailler : excès de monnaie détenue → achat "
      "de titres → prix des obligations ↑ → taux d’intérêt ↓."),
'ch25-vraifa-87': f(niv='raisonner', sp='c25-10', b=2093),
'ch25-vraifa-88': f(niv='raisonner', sp='c25-10', b=2212),
'ch25-questi-108': f(niv='raisonner', sp='c25-10', b=2102),
'ch25-questi-118': f(niv='raisonner', sp='c25-10', b=2181),
'ch25-questi-119': f(niv='raisonner', sp='c25-10', b=2274),

# =============================================================== c25-11
'ch25-qcm-24': f(niv='connaitre', sp='c25-11', b=2459,
 why=["Le marché du travail n’est pas représenté dans le modèle.",
      "L’équilibre budgétaire est une contrainte de finances publiques, non "
      "une courbe du modèle.",
      "Limiter BP au solde courant est l’erreur que le cours signale : elle "
      "intègre aussi les mouvements autonomes de capitaux."],
 diss="Définition exacte à retenir : BP rassemble les couples (Y, r) "
      "compatibles avec l’équilibre de la balance globale, somme du solde "
      "courant et des mouvements autonomes de capitaux."),
'ch25-vraifa-83': f(niv='raisonner', sp='c25-11', b=2387),

# =============================================================== c25-12
'ch25-qcm-25': f(niv='comprendre', sp='c25-12', b=2523,
 why=["L’effet du taux d’intérêt sur les importations n’est pas le canal "
      "retenu : il passe par les capitaux.",
      "L’effet des prix sur la compétitivité relève d’une autre analyse, "
      "celle du taux de change réel.",
      "Les exportations dépendent de la demande étrangère, non du taux "
      "d’intérêt domestique."],
 diss="Enchaînement à écrire : Y ↑ → M ↑ → solde courant ↓ → besoin de "
      "financement → r ↑ pour attirer des capitaux."),
'ch25-qcm-26': f(niv='connaitre', sp='c25-12', b=2582,
 why=["La verticalité de BP correspond au cas inverse, celui d’une absence "
      "totale de mobilité des capitaux.",
      "Une pente décroissante n’a pas de justification économique ici.",
      "BP et LM sont deux équilibres distincts : rien ne les confond."],
 diss="Condition à énoncer : r = r*, le taux domestique s’aligne sur le taux "
      "mondial, ce qui est l’hypothèse centrale des cas de Mundell-Fleming."),
'ch25-qcm-35': f(niv='connaitre', sp='c25-12', b=2634,
 why=["Dérégulation, délocalisation et désindustrialisation mélangent trois "
      "phénomènes distincts.",
      "Dévaluation, désinflation et déflation sont des évolutions "
      "monétaires.",
      "Dette, déficit et dépense relèvent des finances publiques."],
 diss="Conséquence pour le modèle : ces trois transformations rendent BP de "
      "plus en plus horizontale, donc le triangle de Mundell de plus en plus "
      "contraignant."),
'ch25-qcm-74': f(niv='appliquer', sp='c25-12', b=2523,
 why=["Un excédent de la balance globale correspond à un point situé "
      "au-dessus de BP.",
      "L’équilibre extérieur correspond précisément aux points situés sur la "
      "courbe BP.",
      "Un excédent courant ne suffit pas à conclure : la balance globale "
      "intègre aussi les mouvements de capitaux."],
 diss="Méthode de lecture graphique : au-dessous de BP, le taux d’intérêt est "
      "trop faible pour financer le besoin extérieur ; au-dessus, il attire "
      "plus de capitaux que nécessaire."),
'ch25-questi-114': f(niv='raisonner', sp='c25-12', b=2523),

}
