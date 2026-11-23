# -*- coding: utf-8 -*-
"""Chapitre 26 — corrections des questions héritées, sous-parties c26-01 à c26-06."""


def f(**kw):
    return kw


FIX = {

# =============================================================== c26-01
'ch26-qcm-1': f(niv='connaitre', sp='c26-01', b=45,
 why=["La convertibilité est une propriété distincte : elle permet "
      "l’utilisation internationale d’une monnaie, mais toute devise n’est "
      "pas nécessairement convertible.",
      "Une monnaie de réserve est une devise particulière, détenue par les "
      "banques centrales : c’est un cas, non la définition.",
      "Un billet est un support matériel de la monnaie, non une catégorie "
      "monétaire."],
 diss="Définition à poser d’emblée : la monnaie est une créance dotée d’un "
      "pouvoir libératoire général ; la devise est cette même monnaie "
      "considérée depuis un autre espace monétaire."),
'ch26-qcm-2': f(niv='connaitre', sp='c26-01', b=45,
 why=["La convertibilité en or est une propriété historique particulière, "
      "abandonnée depuis 1971.",
      "L’acceptation mondiale est le fait de quelques monnaies seulement : "
      "le pouvoir libératoire est territorial.",
      "L’émission par la banque centrale concerne une partie de la monnaie "
      "seulement, la monnaie scripturale étant créée par les banques."]),
'ch26-qcm-3': f(niv='connaitre', sp='c26-01', b=147,
 why=["Monnaie fiduciaire et monnaie scripturale désignent des formes de "
      "monnaie, non des fonctions internationales.",
      "Monnaie unique et monnaie commune renvoient à l’intégration "
      "monétaire régionale.",
      "Étalon, numéraire et moyen de paiement national décrivent les "
      "fonctions internes de la monnaie."],
 diss="Les trois fonctions à définir précisément : véhiculaire "
      "(intermédiaire dans des transactions qui ne concernent pas les "
      "États-Unis), unité de compte (contrats et matières premières libellés "
      "en dollars), réserve de valeur internationale."),
'ch26-qcm-4': f(niv='connaitre', sp='c26-01', b=163,
 why=["C’est la définition de la cotation à l’incertain, qui fait "
      "exactement l’inverse.",
      "Le taux de change à terme concerne l’échéance de l’opération, non le "
      "sens de la cotation.",
      "Le taux de change effectif est une moyenne pondérée multilatérale."],
 diss="Précaution de lecture indispensable : vérifier le sens de la cotation "
      "avant d’interpréter une hausse comme une appréciation."),
'ch26-qcm-5': f(niv='comprendre', sp='c26-01', b=183,
 why=["Un taux bilatéral corrigé de l’inflation est le taux de change réel "
      "bilatéral.",
      "Le taux d’équilibre de la parité des pouvoirs d’achat est une "
      "référence théorique, non une moyenne observée.",
      "Les banques centrales n’affichent pas un taux : en changes flottants, "
      "il résulte du marché."],
 diss="Utilité du concept : une monnaie peut se déprécier face à une devise "
      "tout en s’appréciant en termes effectifs — seul le taux effectif "
      "décrit la position d’ensemble."),
'ch26-questi-125': f(niv='comprendre', sp='c26-01', b=163),
'ch26-questi-126': f(niv='raisonner', sp='c26-01', b=147),

# =============================================================== c26-02
'ch26-qcm-8': f(niv='connaitre', sp='c26-02', b=318,
 why=["Un marché organisé suppose une chambre de compensation et des "
      "contrats standardisés : ce n’est pas la caractéristique retenue.",
      "Le marché des changes est au contraire un marché de gros.",
      "Il n’est pas réglementé au sens d’un marché centralisé soumis à une "
      "autorité unique."],
 diss="Conséquence du caractère de réseau : une dimension mondiale et un "
      "fonctionnement quasi continu, qui rendent les interventions des "
      "banques centrales plus difficiles."),
'ch26-qcm-9': f(niv='comprendre', sp='c26-02', b=347,
 why=["L’arbitrage réduit au contraire les écarts, donc contribue à la "
      "cohérence des prix.",
      "La parité centrale est fixée par les autorités en régime de changes "
      "fixes.",
      "L’arbitrage augmente les volumes échangés, puisqu’il suppose des "
      "transactions."],
 diss="Mécanisme à expliciter : un même couple de monnaies ne peut pas "
      "durablement s’échanger à deux prix différents, car l’écart serait "
      "immédiatement exploité."),
'ch26-qcm-10': f(niv='connaitre', sp='c26-02', b=355,
 why=["Les ménages n’y représentent qu’une part marginale : c’est un marché "
      "de gros.",
      "Le marché interbancaire des changes est mondial, non limité à la zone "
      "euro.",
      "Le FMI ne contrôle pas le marché des changes."],
 diss="Deux faits structurants à retenir : le rôle central des banques, "
      "rejointes par les investisseurs institutionnels, et la domination du "
      "dollar."),
'ch26-qcm-11': f(niv='raisonner', sp='c26-02', b=401,
 why=["La croissance du commerce de marchandises explique une partie du "
      "mouvement, mais pas son ampleur : les transactions financières "
      "progressent beaucoup plus vite.",
      "L’élargissement de la zone euro ne joue pas dans ce développement.",
      "Les régimes d’ancrage n’ont pas disparu : ils demeurent majoritaires "
      "en 2025."],
 diss="Trois mécanismes à citer ensemble : essor du commerce international, "
      "multiplication des produits dérivés, intensification des opérations "
      "financières."),

# =============================================================== c26-03
'ch26-qcm-7': f(niv='connaitre', sp='c26-03', b=518,
 why=["Une hausse décidée par les autorités en changes fixes est une "
      "réévaluation.",
      "Une hausse du taux directeur est une décision de politique "
      "monétaire, qui peut provoquer une appréciation sans se confondre avec "
      "elle.",
      "Le taux de change réel intègre les niveaux de prix : sa hausse n’est "
      "pas l’appréciation nominale."],
 diss="Vocabulaire strict dont la confusion est pénalisée : appréciation et "
      "dépréciation résultent du marché, réévaluation et dévaluation sont des "
      "décisions des autorités."),
'ch26-qcm-12': f(niv='comprendre', sp='c26-03', b=527,
 why=["Le montant ne distingue pas les deux opérations : une couverture peut "
      "être considérable.",
      "Le type d’intervenant ne les distingue pas non plus : une même banque "
      "peut faire les deux.",
      "La durée des contrats est indifférente : les mêmes échéances servent "
      "les deux logiques."],
 diss="Point souvent mal compris : les mêmes instruments — options, swaps, "
      "opérations à terme — servent la couverture comme la spéculation ; "
      "c’est l’intention qui diffère."),
'ch26-qcm-14': f(niv='raisonner', sp='c26-03', b=575,
 why=["Les anticipations de retour à la moyenne sont au contraire "
      "stabilisatrices, et caractérisent les périodes calmes.",
      "Les anticipations adaptatives sur les prix concernent l’inflation, "
      "non le change.",
      "Les anticipations d’inflation sont un autre objet."],
 diss="Conclusion décisive du cours : le marché des changes est "
      "simultanément stabilisateur et déstabilisateur, selon la nature des "
      "anticipations qui dominent."),

# =============================================================== c26-04
'ch26-qcm-6': f(niv='comprendre', sp='c26-04', b=768,
 why=["La valeur nominale d’une monnaie est mesurée par le taux de change "
      "nominal.",
      "Le rendement des placements en devises relève de la parité des taux "
      "d’intérêt.",
      "Le pouvoir d’achat intérieur de la monnaie est mesuré par l’inverse "
      "du niveau général des prix."],
 diss="Formule à retenir pour l’interprétation : une monnaie stable "
      "nominalement perd en compétitivité si l’inflation nationale dépasse "
      "celle des partenaires."),
'ch26-qcm-15': f(niv='comprendre', sp='c26-04', b=660,
 why=["L’offre de monnaie nationale est accrue par les importations, non par "
      "les exportations.",
      "Les échanges de biens affectent bien le change, par l’offre et la "
      "demande de devises.",
      "L’effet sur le taux de change réel dépend aussi des prix relatifs : "
      "l’affirmation est trop directe."],
 diss="Symétrie à poser clairement : exportations → demande de monnaie "
      "nationale ↑ ; importations → offre de monnaie nationale ↑."),
'ch26-qcm-16': f(niv='connaitre', sp='c26-04', b=667,
 why=["1906 ne correspond à aucune étape de cette théorie.",
      "1936 est l’année de la Théorie générale de Keynes.",
      "1953 est l’année de The Case for Flexible Exchange Rates de "
      "Friedman."]),
'ch26-qcm-17': f(niv='comprendre', sp='c26-04', b=698,
 why=["L’égalité des prix à l’intérieur d’un pays n’est pas l’objet de la "
      "loi, qui porte sur la comparaison internationale.",
      "L’égalité des rythmes de hausse des prix décrirait une convergence des "
      "taux d’inflation, ce qui est différent.",
      "Les biens non échangeables sont précisément ceux auxquels la loi ne "
      "s’applique pas."],
 diss="Mécanisme fondateur : faute d’égalité des prix après conversion, des "
      "arbitrages s’enclencheraient jusqu’à refermer l’écart."),
'ch26-qcm-18': f(niv='appliquer', sp='c26-04', b=758,
 why=["Une appréciation correspondrait à une inflation plus faible que celle "
      "des partenaires : c’est l’inverse.",
      "La stabilité supposerait des inflations égales.",
      "8 % additionnerait les deux taux d’inflation au lieu de les "
      "soustraire."],
 diss="Règle de calcul de la PPA relative : la monnaie du pays le plus "
      "inflationniste se déprécie d’un montant proche de l’écart "
      "d’inflation."),
'ch26-qcm-19': f(niv='connaitre', sp='c26-04', b=808,
 exp="Le cours date explicitement cet apport de 1964 et l’attribue à Béla "
     "Balassa et Paul Samuelson. Son objet est de rendre compte d’un fait que "
     "la parité des pouvoirs d’achat ne peut expliquer : les pays les plus "
     "productifs présentent durablement des niveaux de prix plus élevés, sans "
     "que leur monnaie soit pour autant surévaluée. L’effet constitue donc "
     "l’une des quatre limites de la PPA retenues par le chapitre.",
 why=["Cassel développe la PPA en 1918 et Friedman défend les changes "
      "flottants en 1953.",
      "Calvo et Reinhart publient « Fear of Floating » en 2002.",
      "Mundell et Fleming développent le modèle IS-LM-BP en 1963."]),
'ch26-qcm-20': f(niv='raisonner', sp='c26-04', b=821,
 why=["Des monnaies sous-évaluées sont le résultat inverse de celui que "
      "décrit l’effet.",
      "Le niveau des taux d’intérêt n’est pas en cause dans ce mécanisme.",
      "Les excédents commerciaux structurels relèvent d’autres "
      "déterminants."],
 diss="Enchaînement complet à restituer : productivité élevée du secteur "
      "exposé → salaires élevés → diffusion par la mobilité du travail vers "
      "les secteurs non échangeables → coûts puis prix ↑ → niveau général des "
      "prix ↑."),
'ch26-qcm-21': f(niv='connaitre', sp='c26-04', b=835,
 why=["Les coûts de transaction figurent bien parmi les quatre limites "
      "retenues.",
      "L’existence de biens non échangeables en est la deuxième.",
      "Les mouvements de capitaux en sont la quatrième, et peuvent éloigner "
      "durablement le change de la PPA."],
 diss="Les quatre limites à énumérer : coûts de transaction, biens non "
      "échangeables, effet Balassa-Samuelson, mouvements de capitaux."),
'ch26-questi-127': f(niv='raisonner', sp='c26-04', b=667),

# =============================================================== c26-05
'ch26-qcm-22': f(niv='connaitre', sp='c26-05', b=894,
 why=["Le niveau d’équilibre du taux de change est une grandeur économique, "
      "non un ensemble de règles.",
      "La politique de taux d’intérêt est la politique monétaire, distincte "
      "du régime de change.",
      "Le montant des réserves est un moyen de la politique de change, non "
      "sa définition."],
 diss="Idée directrice : les régimes forment un continuum entre ancrage "
      "strict et flottement libre, et leur choix relève de la souveraineté "
      "monétaire."),
'ch26-qcm-23': f(niv='connaitre', sp='c26-05', b=952,
 why=["L’Équateur depuis 2000 illustre la dollarisation, forme d’ancrage "
      "encore plus rigide.",
      "Hong Kong pratique effectivement un currency board, mais ce n’est pas "
      "l’exemple retenu par le cours.",
      "Le Panama illustre lui aussi la dollarisation."],
 diss="Nuance historique à mentionner : l’abandon du régime argentin en 2002 "
      "illustre la fragilité des ancrages très rigides."),
'ch26-qcm-24': f(niv='connaitre', sp='c26-05', b=984,
 why=["La distinction entre taux nominal et taux réel porte sur la "
      "correction par les prix.",
      "La distinction entre comptant et terme porte sur l’échéance des "
      "opérations.",
      "L’opposition entre ancrage ferme et ancrage souple est une "
      "classification de régimes, non la structure interne d’un régime "
      "conventionnel."],
 diss="Repère chiffré indispensable : dans le SME, les marges sont de ± 2 %, "
      "élargies à ± 15 % en août 1993 après les crises de 1992-1993."),

# =============================================================== c26-06
'ch26-qcm-27': f(niv='connaitre', sp='c26-06', b=1095,
 why=["Février 1987 correspond aux accords du Louvre, qui visent au "
      "contraire à stabiliser le dollar.",
      "Août 1993 est l’élargissement des marges du SME.",
      "Novembre 2024 est la date du rapport de Stephen Miran."],
 diss="Cinq puissances à nommer : États-Unis, Japon, République fédérale "
      "d’Allemagne, France et Royaume-Uni."),
'ch26-qcm-28': f(niv='comprendre', sp='c26-06', b=1090,
 why=["Les États-Unis connaissent au contraire un déficit commercial "
      "croissant sur la période.",
      "Les accords du Louvre sont postérieurs : ils datent de 1987.",
      "La dollarisation de plusieurs économies est un phénomène distinct et "
      "plus tardif."],
 diss="Mécanisme autoréalisateur à souligner : les anticipations "
      "d’appréciation attirent des capitaux, qui provoquent l’appréciation "
      "anticipée."),
'ch26-qcm-29': f(niv='appliquer', sp='c26-06', b=1090,
 why=["Déficit commercial et déficit de la balance des capitaux ne peuvent "
      "coexister durablement : les deux se compensent comptablement.",
      "Le déficit de la Sécurité sociale est une composante du déficit "
      "public, non un second déficit distinct.",
      "L’inflation n’est pas un solde : elle ne peut pas être l’un des deux "
      "déficits jumeaux."],
 diss="Application du cours : l’administration Reagan combine réductions "
      "d’impôts, dépenses militaires et déficits budgétaires élevés, tandis "
      "que l’appréciation du dollar creuse le déficit commercial."),
'ch26-qcm-30': f(niv='connaitre', sp='c26-06', b=1118,
 why=["Faire baisser davantage le dollar était l’objet du Plaza, en 1985.",
      "L’euro est créé en 1999, bien plus tard.",
      "L’élargissement des marges du SME intervient en août 1993."],
 diss="Enseignement commun aux deux accords : les banques centrales peuvent "
      "intervenir collectivement même en régime de changes flottants."),
'ch26-qcm-31': f(niv='connaitre', sp='c26-06', b=1184,
 why=["L’achat ou la vente de devises pour influencer le change est une "
      "intervention de change, instrument distinct.",
      "Un prêt du FMI relève de l’assistance financière à un État, non de la "
      "coopération entre banques centrales.",
      "Un contrat à terme sur devises est un instrument de marché."],
 diss="Distinction que le cours souligne explicitement : l’intervention de "
      "change modifie le cours, la ligne de swap fournit de la liquidité."),
'ch26-qcm-32': f(niv='connaitre', sp='c26-06', b=1190,
 why=["29 pays et 13 % correspondent à l’arrimage ferme.",
      "88 pays et 46 % correspondent à l’arrimage souple.",
      "13 pays et 7 % correspondent aux régimes autres ou non classés."],
 diss="Précaution de méthode à mentionner : les parts sont arrondies et la "
      "classification dépend des critères retenus."),
'ch26-qcm-33': f(niv='raisonner', sp='c26-06', b=1191,
 why=["Le flottement libre ne concerne que 34 % des pays : il n’est pas "
      "généralisé.",
      "Les régimes d’ancrage n’ont pas disparu : ils représentent au "
      "contraire 59 % des cas.",
      "Les choix monétaires sont au contraire très diversifiés."],
 diss="Motifs de l’ancrage à énumérer : limiter l’inflation, sécuriser les "
      "échanges, protéger un endettement libellé en devises."),
'ch26-vraifa-105': f(niv='comprendre', sp='c26-06', b=1116),

}
