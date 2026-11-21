# -*- coding: utf-8 -*-
"""Chapitre 1 — Pauvreté monétaire, circuit économique et consommation.

Libellés des sous-parties, corrigés réécrits et questions nouvelles. Chaque
chiffre et chaque attribution a été vérifié dans le texte du cours ; les
questions portant sur des données absentes du cours sont écartées.
"""

SP = {
 'c1-01': 'Capitalisme, polycrise et circuit économique',
 'c1-02': 'Entreprises, investissement et revenus des ménages',
 'c1-03': 'La consommation : Keynes et ses critiques',
 'c1-04': 'L’État : fonctions de Musgrave, fiscalité et redistribution',
 'c1-05': 'Dette publique, déficit et limites du PIB',
}

# Données que le cours ne contient pas : la question ne peut pas être corrigée.
DROP = [
 'ch1-qcm-8',    # part des SNF dans l'investissement : chiffre absent du cours
]


def f(**kw):
    return kw


FIX = {

# ===================================================== c1-01 · circuit
'ch1-qcm-1': f(niv='connaitre', sp='c1-01',
 exp="Plihon retient quatre caractéristiques dans Les capitalismes "
     "contemporains : une crise économique et sociale, une crise écologique, "
     "une crise démocratique et une crise géopolitique. L’intérêt du terme "
     "« polycrise » est précisément de refuser de hiérarchiser ces quatre "
     "dimensions : elles se nourrissent l’une l’autre.",
 why=["Deux dimensions ne suffisent pas à justifier le préfixe « poly ».",
      "Trois : c’est le découpage habituel crise économique / sociale / "
      "écologique, mais Plihon ajoute la dimension géopolitique.",
      "Cinq : le cours n’en retient pas davantage."],
 diss="Utile en introduction d’un sujet sur le capitalisme contemporain : "
      "Plihon permet de poser que la crise n’est pas conjoncturelle mais "
      "systémique, et d’annoncer un plan qui traite successivement les "
      "dimensions économique, écologique et politique."),

'ch1-qcm-2': f(niv='connaitre', sp='c1-01',
 exp="Le capitalisme est un régime d’organisation économique où des "
     "personnes privées détiennent les capitaux et les moyens de production. "
     "La propriété privée des moyens de production en est le critère : c’est "
     "elle qui sépare le capitalisme d’une économie administrée, et non le "
     "niveau de développement ou l’ouverture internationale.",
 why=["C’est la définition d’une économie collectiviste ou administrée.",
      "L’échange entre nations est le commerce international : il existe "
      "dans tous les régimes économiques.",
      "La redistribution est une fonction de l’État, pas une définition du "
      "régime de propriété."]),

'ch1-qcm-3': f(niv='connaitre', sp='c1-01',
 exp="La comptabilité nationale regroupe les unités en six secteurs "
     "institutionnels, selon leur fonction principale et leur ressource "
     "principale : ménages, sociétés non financières, sociétés financières, "
     "administrations publiques, institutions sans but lucratif au service "
     "des ménages, et reste du monde.",
 why=["Quatre : ce serait oublier les ISBLSM et le reste du monde.",
      "Cinq : il manque alors un secteur, le plus souvent le reste du monde.",
      "Sept : la nomenclature n’en retient pas autant."]),

'ch1-qcm-5': f(niv='connaitre', sp='c1-01',
 exp="Ragnar Frisch est le premier à avoir collecté et agrégé des données "
     "pour construire une approche macroéconomique. C’est le geste fondateur "
     "de la comptabilité nationale : passer de comportements individuels à "
     "des grandeurs agrégées que l’on peut mesurer et comparer.",
 why=["Keynes fournit le cadre théorique de la macroéconomie, pas l’appareil "
      "statistique de mesure.",
      "Friedman intervient plus tard, et sur la consommation et la monnaie.",
      "Modigliani travaille sur la consommation et le cycle de vie."]),

'ch1-qcm-34': f(niv='connaitre', sp='c1-01',
 exp="Le PIB français recule d’environ 7 % en 2020, contre 3,5 % pour "
     "l’économie mondiale. L’écart s’explique par la structure de l’économie "
     "française, où les services de contact — tourisme, restauration, "
     "transport — pèsent lourd et ont été directement touchés par les "
     "mesures sanitaires.",
 why=["− 3,5 % est le recul mondial, pas le recul français.",
      "− 5,5 % ne correspond à aucun des deux chiffres du cours.",
      "− 10 % surestime nettement le choc mesuré en France."]),

'ch1-qcm-38': f(niv='connaitre', sp='c1-01',
 exp="Le micro-entrepreneur crée une entreprise individuelle sous un régime "
     "aux procédures simplifiées : déclaration allégée, calcul des "
     "cotisations proportionnel au chiffre d’affaires. Ce n’est pas une "
     "société : il n’y a pas de personne morale distincte de la personne "
     "physique.",
 why=["La SARL est une société, donc une personne morale : ce n’est pas le "
      "cadre du micro-entrepreneur.",
      "Le micro-entrepreneur n’est pas un salarié : il n’a pas de contrat de "
      "travail ni de lien de subordination.",
      "Le statut n’est pas réservé aux fonctionnaires."]),

'ch1-qcm-39': f(niv='connaitre', sp='c1-01',
 exp="Le cours donne 67 000 défaillances en 2025, après 27 562 en 2021 et "
     "56 719 en 2023. Le creux de 2020-2021 est un artefact des soutiens "
     "publics — chômage partiel, PGE, reports de charges — qui ont maintenu "
     "en vie des entreprises fragiles ; leur retrait produit ensuite un "
     "rattrapage mécanique.",
 why=["27 000 correspond à l’année 2021, en plein soutien public.",
      "45 000 ne correspond à aucune des années relevées par le cours.",
      "90 000 dépasse largement le niveau constaté."],
 diss="Bon exemple pour montrer qu’une politique de soutien déplace les "
      "défaillances dans le temps plus qu’elle ne les supprime : la "
      "comparaison 2021-2025 sert d’illustration chiffrée dans un sujet sur "
      "l’intervention de l’État face aux crises."),

'ch1-vf-1': f(niv='comprendre', sp='c1-01',
 exp="Le capitalisme libéral repose au contraire sur le principe de "
     "non-intervention : l’État garantit les règles — propriété, contrats, "
     "concurrence — mais ne dirige pas l’activité. L’intervention massive "
     "caractérise d’autres configurations, comme le capitalisme d’État ou "
     "l’économie administrée."),

'ch1-vf-2': f(niv='connaitre', sp='c1-01',
 exp="C’est bien la thèse de Plihon dans Les capitalismes contemporains : la "
     "crise actuelle est simultanément économique et sociale, écologique, "
     "démocratique et géopolitique. Le mot « polycrise » insiste sur la "
     "simultanéité et l’enchevêtrement de ces dimensions, qu’aucune "
     "politique sectorielle ne peut traiter séparément."),

'ch1-vf-3': f(niv='comprendre', sp='c1-01',
 exp="La tendance observée depuis la crise sanitaire est inverse : les "
     "chaînes de valeur se régionalisent et les approvisionnements se "
     "diversifient. Les entreprises arbitrent désormais entre le coût et la "
     "sécurité, là où la période précédente optimisait le seul coût."),

# ============================================ c1-02 · entreprises et revenus
'ch1-qcm-6': f(niv='connaitre', sp='c1-02',
 exp="Le taux de marge rapporte l’excédent brut d’exploitation à la valeur "
     "ajoutée : EBE / VA × 100. Il mesure la part de la valeur ajoutée qui "
     "reste à l’entreprise une fois payés les salaires, les cotisations et "
     "les impôts de production.",
 why=["Rapporter l’EBE au PIB mélange une grandeur d’entreprise et une "
      "grandeur nationale.",
      "Résultat net sur chiffre d’affaires est la marge nette comptable, pas "
      "le taux de marge de la comptabilité nationale.",
      "Investissement sur valeur ajoutée est le taux d’investissement."],
 diss="Le taux de marge est la charnière entre partage de la valeur ajoutée "
      "et investissement : il permet d’articuler un paragraphe sur la "
      "répartition primaire avec le théorème de Schmidt, à condition de "
      "rappeler que la transmission marges → investissement n’a rien "
      "d’automatique."),

'ch1-qcm-7': f(niv='comprendre', sp='c1-02',
 exp="Le taux d’autofinancement mesure la capacité de l’entreprise à "
     "financer ses investissements sur ses ressources propres, sans recourir "
     "au crédit ni au marché. Le cours ajoute une lecture utile : un "
     "autofinancement supérieur à l’investissement peut signaler non une "
     "bonne santé mais un investissement insuffisamment dynamique.",
 why=["La part de la valeur ajoutée consacrée aux salaires est le taux de "
      "partage salarial, complément du taux de marge.",
      "Bénéfice net sur chiffre d’affaires est une marge comptable.",
      "Le rendement d’un placement financier relève de la rentabilité "
      "financière, pas du financement de l’investissement."]),

'ch1-qcm-9': f(niv='connaitre', sp='c1-02',
 exp="Le multiplicateur keynésien vaut k = 1 / (1 − c), où c est la "
     "propension marginale à consommer. Avec c = 0,8, le cours obtient k = 5 "
     "en économie fermée : une dépense initiale de 1 engendre 5 de revenu, "
     "par vagues successives de consommation. L’ouverture ramène ce "
     "multiplicateur à 2,5, les importations constituant une seconde fuite.",
 why=["k = 1 / c donnerait 1,25 avec c = 0,8 : la formule confond la "
      "propension à consommer et la propension à épargner.",
      "k = c / (1 − c) est le multiplicateur des prestations sociales, pas "
      "celui des dépenses autonomes.",
      "k = (1 + c) / c ne correspond à aucun multiplicateur du cours."],
 diss="À mobiliser avec sa condition : le multiplicateur est d’autant plus "
      "fort que la propension à consommer est élevée et l’économie fermée. "
      "C’est l’argument qui justifie de cibler une relance sur les ménages "
      "modestes et de la coordonner entre partenaires."),

'ch1-qcm-11': f(niv='comprendre', sp='c1-02',
 exp="Le principe de l’accélérateur, formulé par Aftalion puis Clark, "
     "énonce qu’une variation de la demande entraîne une variation plus que "
     "proportionnelle de l’investissement : pour produire davantage, il faut "
     "ajouter des capacités entières, et le stock de capital nécessaire est "
     "un multiple de la production annuelle. L’effet joue symétriquement à "
     "la baisse, ce qui rend l’investissement très volatil.",
 why=["Une réaction moins que proportionnelle contredit le principe même de "
      "l’accélérateur.",
      "Un investissement stable supposerait que les capacités de production "
      "soient toujours suffisantes.",
      "La consommation n’a pas de raison de diminuer : c’est au contraire sa "
      "hausse qui déclenche le mécanisme."],
 diss="Couplé au multiplicateur, l’accélérateur donne l’oscillateur de "
      "Samuelson (1939) : il explique pourquoi l’activité fluctue au lieu de "
      "converger, argument décisif dans un sujet sur l’instabilité de la "
      "croissance."),

'ch1-qcm-13': f(niv='connaitre', sp='c1-02',
 exp="Le revenu disponible brut s’obtient en ajoutant aux revenus primaires "
     "— salaires, revenus du patrimoine, revenus mixtes — les revenus de "
     "transfert reçus, puis en retranchant les prélèvements obligatoires. "
     "C’est le revenu effectivement disponible pour consommer ou épargner.",
 why=["Additionner les deux revenus sans retrancher les prélèvements "
      "surévalue le revenu disponible.",
      "Salaire net plus prestations oublie les revenus du patrimoine et les "
      "revenus mixtes.",
      "PIB moins dépenses publiques est un solde macroéconomique sans "
      "rapport avec le revenu des ménages."]),

'ch1-qcm-14': f(niv='connaitre', sp='c1-02',
 exp="Le revenu médian français s’élève à 2 150 euros par mois en 2023. La "
     "médiane partage la population en deux moitiés égales ; elle est "
     "préférée à la moyenne parce qu’elle n’est pas tirée vers le haut par "
     "les très hauts revenus.",
 why=["1 500 € est inférieur au seuil de pauvreté à 60 % du revenu médian.",
      "1 800 € sous-estime la médiane relevée par le cours.",
      "2 500 € la surestime : c’est un ordre de grandeur proche du revenu "
      "moyen, non de la médiane."]),

'ch1-qcm-15': f(niv='appliquer', sp='c1-02',
 exp="Le seuil à 60 % du revenu médian de 2 150 euros donne 1 288 euros, et "
     "correspond à 9,8 millions de personnes pauvres. Le seuil à 50 %, soit "
     "1 073 euros, n’en compte que 5,4 millions : le choix de la convention "
     "fait varier de près du double le nombre de pauvres mesurés.",
 why=["1 073 € correspond au seuil à 50 % du revenu médian, et à "
      "5,4 millions de personnes.",
      "1 500 € ne correspond à aucune des deux conventions.",
      "1 720 € correspondrait à 80 % du revenu médian, convention qui "
      "n’existe pas."],
 diss="L’écart entre 5,4 et 9,8 millions de pauvres selon le seuil retenu "
      "est l’exemple canonique pour montrer qu’un indicateur statistique est "
      "une construction conventionnelle, argument de première partie dans un "
      "sujet sur la mesure des inégalités."),

'ch1-qcm-29': f(niv='connaitre', sp='c1-02',
 exp="L’indice des prix à la consommation mesure la variation moyenne des "
     "prix d’un panier de biens et services représentatif de la "
     "consommation des ménages. C’est un indice de Laspeyres pondéré par la "
     "structure de consommation : il sert à passer des grandeurs en valeur "
     "aux grandeurs en volume.",
 why=["L’évolution du PIB en volume est obtenue en déflatant le PIB en "
      "valeur par un indice de prix : c’est un résultat, pas l’indice.",
      "Le niveau de vie se mesure par le revenu disponible rapporté aux "
      "unités de consommation.",
      "Le chômage relève d’une autre statistique, l’enquête Emploi."]),

'ch1-qcm-30': f(niv='comprendre', sp='c1-02',
 exp="L’inflation sous-jacente exclut les composantes les plus volatiles — "
     "énergie, produits alimentaires frais, tarifs publics — pour isoler la "
     "tendance de fond des prix. Elle importe aux banques centrales, qui ne "
     "veulent pas réagir à un choc temporaire sur le pétrole comme à une "
     "dérive durable de l’inflation.",
 why=["Inclure l’énergie, c’est précisément ce que fait l’indice "
      "d’ensemble, non l’inflation sous-jacente.",
      "L’inflation sous-jacente n’a rien de spécifique aux pays en "
      "développement.",
      "La hausse des salaires est une autre grandeur, qui peut nourrir "
      "l’inflation sans se confondre avec elle."]),

'ch1-qcm-37': f(niv='comprendre', sp='c1-02',
 exp="L’effet Pigou, ou effet d’encaisse réelle, décrit la réaction des "
     "ménages à l’inflation : la valeur réelle de leur patrimoine monétaire "
     "s’érodant, ils épargnent davantage pour la reconstituer. La "
     "consommation recule donc, ce qui exerce un effet dépressif. Le cours "
     "note que cet effet a été fréquemment observé en France.",
 why=["Consommer davantage pour « prendre de vitesse » les prix est l’effet "
      "inverse, dit de fuite devant la monnaie, observé en hyperinflation.",
      "Se porter vers la bourse est un arbitrage de placement, pas l’effet "
      "d’encaisse réelle.",
      "La revendication salariale est un mécanisme de boucle prix-salaires, "
      "distinct de l’effet Pigou."]),

'ch1-qcm-40': f(niv='comprendre', sp='c1-02',
 exp="L’oscillateur de Samuelson (1939) combine multiplicateur et "
     "accélérateur : une variation de l’investissement fait varier le revenu "
     "(multiplicateur), cette variation du revenu fait varier la demande, "
     "qui fait à son tour varier l’investissement (accélérateur). "
     "L’investissement est ainsi à la fois une composante de la demande et "
     "un déterminant de l’offre, ce qui engendre des fluctuations.",
 why=["Faire partir le mécanisme de la demande vers l’épargne omet le cœur "
      "du modèle, l’investissement.",
      "« L’épargne entraîne l’investissement » est la causalité classique, "
      "que Keynes et Samuelson renversent.",
      "Inflation et stagnation n’interviennent pas dans l’oscillateur."],
 diss="Référence courte et efficace pour expliquer, dans un sujet sur les "
      "cycles, que l’instabilité n’est pas un accident mais une propriété "
      "de l’interaction entre demande et investissement."),

'ch1-vf-5': f(niv='connaitre', sp='c1-02',
 exp="La norme européenne retient 60 % du revenu médian, soit 1 288 euros "
     "pour un revenu médian de 2 150 euros, et 9,8 millions de personnes "
     "pauvres. Le seuil à 50 %, soit 1 073 euros, existe aussi mais relève "
     "d’une autre convention, plus restrictive, qui compte 5,4 millions de "
     "pauvres."),

'ch1-vf-11': f(niv='connaitre', sp='c1-02',
 exp="La formation brute de capital fixe mesure l’acquisition d’actifs "
     "produits durables utilisés plus d’un an : machines, bâtiments, "
     "matériels. Les investissements immatériels — logiciels, recherche, "
     "bases de données — y sont intégrés, mais la FBCF ne se limite "
     "certainement pas à eux."),

'ch1-vf-16': f(niv='connaitre', sp='c1-02',
 exp="La déflation est une baisse durable du niveau général des prix ; la "
     "hausse est l’inflation, et le ralentissement de la hausse la "
     "désinflation. La distinction est décisive : la déflation alourdit la "
     "valeur réelle des dettes et incite à reporter les achats, ce qui "
     "entretient la dépression."),

'ch1-open-2': f(niv='comprendre', sp='c1-02',
 ans={'modele': "La pauvreté absolue se définit par un panier de biens "
      "jugés nécessaires à la survie : on est pauvre si l’on ne peut pas se "
      "le procurer, indépendamment du niveau de vie du pays. La pauvreté "
      "relative se définit par rapport à la distribution des revenus du "
      "pays : est pauvre celui qui dispose de moins de 60 % du revenu "
      "médian, soit 1 288 euros en France. La première mesure une privation, "
      "la seconde une distance au reste de la société : quand une population "
      "s’enrichit, le seuil relatif monte et le nombre de pauvres ne "
      "diminue pas nécessairement.",
      'cles': [{'f': ['panier', 'survie', 'besoins vitaux'],
                'l': 'la pauvreté absolue renvoie à un panier de biens de survie'},
               {'f': ['relative', 'revenu median', 'médian'],
                'l': 'la pauvreté relative se définit par rapport au revenu médian'},
               {'f': ['60', '1288', '1 288'],
                'l': 'le seuil européen est fixé à 60 % du revenu médian'},
               {'f': ['enrichit', 'augmente', 'monte', 'suit'],
                'l': 'le seuil relatif suit le niveau de vie du pays'}]},
 exp="L’enjeu de la distinction est politique autant que statistique : une "
     "approche absolue conclut que la croissance supprime la pauvreté, une "
     "approche relative qu’elle ne la supprime pas si la distribution reste "
     "inchangée.",
 diss="Cette opposition structure très bien une première partie : mesurer la "
      "pauvreté, c’est déjà choisir une définition de la justice sociale."),

'ch1-open-3': f(niv='connaitre', sp='c1-02',
 ans={'modele': "L’INSEE rapporte le revenu disponible du ménage au nombre "
      "d’unités de consommation : le premier adulte compte pour 1 UC, les "
      "autres personnes de 14 ans et plus pour 0,5 UC, les enfants de moins "
      "de 14 ans pour 0,3 UC. L’échelle tient compte des économies d’échelle "
      "du ménage : deux personnes ne dépensent pas deux fois plus qu’une.",
      'cles': [{'f': ['revenu disponible'], 'l': 'on part du revenu disponible du ménage'},
               {'f': ['unite de consommation', 'uc'],
                'l': 'on divise par le nombre d’unités de consommation'},
               {'f': ['0,5', '0.5'], 'l': '0,5 UC par personne de 14 ans et plus'},
               {'f': ['0,3', '0.3'], 'l': '0,3 UC par enfant de moins de 14 ans'}]},
 exp="Sans cette correction, on compterait pauvres des ménages nombreux qui "
     "ne le sont pas, et riches des personnes seules qui ne le sont pas "
     "davantage."),

'ch1-open-4': f(niv='connaitre', sp='c1-02',
 ans={'modele': "Le seuil de pauvreté est le niveau de revenu en dessous "
      "duquel on est conventionnellement considéré comme pauvre. En France "
      "il se calcule à partir du revenu médian : 60 % selon la norme "
      "européenne, soit 1 288 euros pour une personne seule en 2023, ou 50 % "
      "selon une convention plus restrictive, soit 1 073 euros.",
      'cles': [{'f': ['median', 'médian'], 'l': 'le seuil se calcule à partir du revenu médian'},
               {'f': ['60'], 'l': 'la norme européenne retient 60 %'},
               {'f': ['1288', '1 288'], 'l': 'soit 1 288 euros par mois'},
               {'f': ['50', '1073', '1 073'], 'l': 'la convention à 50 % donne 1 073 euros'}]},
 exp="Le cours insiste sur la nature conventionnelle du seuil : le nombre de "
     "pauvres passe de 5,4 à 9,8 millions selon la convention retenue."),

'ch1-open-6': f(niv='raisonner', sp='c1-02',
 ans={'modele': "Un emploi ne garantit pas de dépasser le seuil parce que le "
      "revenu dépend du volume de travail et de la composition du ménage : "
      "temps partiel subi, contrats courts, interruptions d’activité "
      "réduisent le revenu annuel ; et le niveau de vie se calcule par unité "
      "de consommation, si bien qu’un salaire au SMIC peut placer sous le "
      "seuil un parent isolé ou une famille nombreuse.",
      'cles': [{'f': ['temps partiel', 'contrat court', 'precarite', 'précarité'],
                'l': 'la précarité de l’emploi réduit le revenu annuel'},
               {'f': ['unite de consommation', 'uc', 'famille', 'charges familiales'],
                'l': 'le niveau de vie se calcule par unité de consommation'},
               {'f': ['smic', 'salaire'], 'l': 'même un salaire au SMIC peut ne pas suffire'}]},
 exp="Le phénomène des travailleurs pauvres montre que l’emploi protège "
     "moins de la pauvreté qu’on ne le suppose : c’est la combinaison du "
     "volume de travail et de la taille du ménage qui décide.",
 diss="Argument utile contre l’idée que l’emploi suffit à sortir de la "
      "pauvreté : il justifie les dispositifs de complément de revenu plutôt "
      "que les seules politiques d’activation."),

'ch1-open-7': f(niv='connaitre', sp='c1-02',
 ans={'modele': "L’intensité de la pauvreté mesure l’écart entre le niveau "
      "de vie médian des personnes pauvres et le seuil de pauvreté, rapporté "
      "à ce seuil. Elle complète le taux de pauvreté : celui-ci dit combien "
      "de personnes sont sous le seuil, l’intensité dit à quelle distance "
      "elles en sont.",
      'cles': [{'f': ['ecart', 'écart', 'distance'], 'l': 'c’est un écart au seuil'},
               {'f': ['seuil'], 'l': 'l’écart est rapporté au seuil de pauvreté'},
               {'f': ['taux de pauvrete', 'combien', 'nombre'],
                'l': 'elle complète le taux de pauvreté, qui compte les personnes'}]},
 exp="Deux pays peuvent avoir le même taux de pauvreté et des intensités "
     "très différentes : c’est l’intensité qui renseigne sur la difficulté à "
     "franchir le seuil."),

'ch1-open-8': f(niv='raisonner', sp='c1-02',
 ans={'modele': "La pauvreté des enfants engage l’égalité des chances : elle "
      "pèse sur la santé, le logement et la réussite scolaire, donc sur le "
      "capital humain accumulé, et augmente la probabilité d’être pauvre à "
      "l’âge adulte. Elle transforme une inégalité de situation en inégalité "
      "de destin, ce qui justifie un traitement prioritaire.",
      'cles': [{'f': ['egalite des chances', 'égalité des chances', 'scolaire', 'ecole'],
                'l': 'elle compromet l’égalité des chances et la réussite scolaire'},
               {'f': ['capital humain', 'sante', 'santé'],
                'l': 'elle dégrade l’accumulation de capital humain'},
               {'f': ['reproduction', 'transmission', 'heredite', 'adulte'],
                'l': 'elle alimente la reproduction de la pauvreté'}]},
 exp="C’est l’argument de la reproduction : la pauvreté de l’enfant n’est "
     "pas seulement une privation présente, elle est un déterminant de la "
     "pauvreté future.",
 diss="À mobiliser dans un sujet sur l’État social : la lutte contre la "
      "pauvreté des enfants est l’investissement social au rendement le plus "
      "élevé, argument d’efficacité qui s’ajoute à l’argument de justice."),

'ch1-open-9': f(niv='comprendre', sp='c1-02',
 ans={'modele': "Le risque de pauvreté dépend fortement de la structure "
      "familiale : les familles monoparentales sont les plus exposées, "
      "environ une sur trois, parce qu’un seul revenu potentiel doit couvrir "
      "des charges de garde et de logement importantes, et que la "
      "contrainte de garde limite le volume de travail possible.",
      'cles': [{'f': ['monoparental'], 'l': 'les familles monoparentales sont les plus exposées'},
               {'f': ['un seul revenu', 'seul revenu', 'un revenu'],
                'l': 'un seul revenu pour l’ensemble du ménage'},
               {'f': ['garde', 'charges', 'enfants'],
                'l': 'des charges de garde et d’enfants plus lourdes'}]},
 exp="Le niveau de vie étant calculé par unité de consommation, la "
     "composition du ménage agit directement sur le classement par rapport "
     "au seuil."),

'ch1-open-11': f(niv='connaitre', sp='c1-02',
 ans={'modele': "La pauvreté en conditions de vie se mesure par des "
      "privations matérielles concrètes : ne pas pouvoir chauffer "
      "correctement son logement, se payer un repas protéiné régulièrement, "
      "faire face à une dépense imprévue, partir en vacances. Elle ne passe "
      "pas par le revenu mais par ce que le ménage peut effectivement se "
      "permettre.",
      'cles': [{'f': ['privation', 'materiel', 'matériel', 'conditions de vie'],
                'l': 'il s’agit de privations matérielles'},
               {'f': ['logement', 'chauffer', 'repas', 'vacances'],
                'l': 'mesurées par des exemples concrets de la vie quotidienne'},
               {'f': ['revenu'], 'l': 'elle ne se réduit pas à un seuil de revenu'}]},
 exp="Cette approche corrige un angle mort de la mesure monétaire : deux "
     "ménages au même revenu peuvent connaître des privations très "
     "différentes selon leur patrimoine, leurs dettes et leur logement."),

'ch1-open-13': f(niv='raisonner', sp='c1-02',
 ans={'modele': "La pauvreté se transmet parce qu’elle limite l’accumulation "
      "des trois formes de capital : le capital humain, les études étant "
      "plus difficiles à financer et à mener ; le capital social, les "
      "réseaux donnant accès à l’information et à l’emploi ; le patrimoine, "
      "qui ne peut pas être constitué ni transmis. La situation des parents "
      "détermine donc les chances des enfants.",
      'cles': [{'f': ['capital humain', 'etudes', 'études', 'diplome'],
                'l': 'moindre accumulation de capital humain'},
               {'f': ['reseau', 'réseau', 'capital social', 'relations'],
                'l': 'absence de réseaux et de capital social'},
               {'f': ['patrimoine', 'transmission', 'heritage'],
                'l': 'impossibilité de constituer et de transmettre un patrimoine'}]},
 exp="Le cours relie ce mécanisme à la concentration patrimoniale : le "
     "système fiscal et social réduit les inégalités de revenus mais "
     "beaucoup moins celles de patrimoine, ce qui entretient la "
     "reproduction."),

'ch1-open-14': f(niv='comprendre', sp='c1-02',
 ans={'modele': "Le logement pèse d’autant plus que le revenu est faible : "
      "une fois le loyer et les charges payés, le reste à vivre peut être "
      "très inférieur à ce que laisse supposer le revenu. Un ménage situé "
      "juste au-dessus du seuil de pauvreté peut ainsi être en difficulté "
      "réelle, ce que la mesure monétaire ne voit pas.",
      'cles': [{'f': ['reste a vivre', 'reste à vivre', 'apres le loyer'],
                'l': 'le logement réduit le reste à vivre'},
               {'f': ['loyer', 'charges', 'cout du logement'],
                'l': 'le coût du logement pèse davantage sur les bas revenus'},
               {'f': ['seuil', 'mesure monetaire', 'monetaire'],
                'l': 'un ménage au-dessus du seuil peut rester en difficulté'}]},
 exp="C’est l’argument central en faveur des indicateurs de conditions de "
     "vie : le revenu avant logement ne dit pas la situation réelle."),

'ch1-open-15': f(niv='comprendre', sp='c1-02',
 ans={'modele': "Le diplôme reste le principal rempart contre la pauvreté : "
      "le taux de pauvreté des non-diplômés est très supérieur à celui des "
      "diplômés du supérieur, parce que le diplôme donne accès à des emplois "
      "plus stables, mieux rémunérés et moins exposés aux interruptions "
      "d’activité.",
      'cles': [{'f': ['diplome', 'diplôme'], 'l': 'le diplôme protège de la pauvreté'},
               {'f': ['stable', 'stabilite', 'cdi', 'remunere', 'rémunéré'],
                'l': 'il donne accès à des emplois plus stables et mieux payés'},
               {'f': ['non diplome', 'sans diplome', 'superieur'],
                'l': 'l’écart entre non-diplômés et diplômés du supérieur est net'}]},
 exp="Ce constat doit être nuancé par la transmission : l’accès au diplôme "
     "dépend lui-même de l’origine sociale, ce qui ferme la boucle de la "
     "reproduction."),
}

# ========================================= c1-03 · la consommation
FIX.update({

'ch1-qcm-10': f(niv='connaitre', sp='c1-03',
 exp="La propension marginale à consommer est la part d’une unité de revenu "
     "supplémentaire qui est consommée : c = ΔC / ΔY. Elle est comprise entre "
     "0 et 1 d’après la loi psychologique fondamentale, et commande la valeur "
     "du multiplicateur, égal à 1 / (1 − c).",
 why=["La part totalement consommée est la propension moyenne, C / Y, qui "
      "est décroissante avec le revenu chez Keynes.",
      "Le rapport entre épargne et revenu est la propension à épargner.",
      "L’écart entre revenu réel et nominal relève de la correction par les "
      "prix, non du comportement de consommation."]),

'ch1-qcm-12': f(niv='connaitre', sp='c1-03',
 exp="Le revenu permanent de Friedman est la valeur actualisée des revenus "
     "anticipés sur l’ensemble du cycle de vie. Les ménages règlent leur "
     "consommation sur cette grandeur et non sur le revenu courant : un gain "
     "transitoire est donc principalement épargné.",
 why=["Le salaire du mois est précisément le revenu courant, celui que "
      "Keynes retient et que Friedman conteste.",
      "La pension de retraite n’est qu’une composante des revenus futurs.",
      "Le revenu après impôt est le revenu disponible, notion de "
      "comptabilité nationale."],
 diss="C’est l’argument central contre les relances par transferts "
      "ponctuels : si les ménages lissent leur consommation, le "
      "multiplicateur d’une prime exceptionnelle est faible. À nuancer par "
      "les contraintes de liquidité des ménages modestes."),

'ch1-qcm-16': f(niv='appliquer', sp='c1-03',
 exp="La loi d’Engel énonce que la part du budget consacrée à l’alimentation "
     "diminue lorsque le revenu augmente : la dépense alimentaire croît en "
     "valeur absolue, mais moins vite que le revenu. Le coefficient "
     "budgétaire alimentaire est donc un indicateur du niveau de vie.",
 why=["Une hausse proportionnelle correspondrait à une élasticité-revenu "
      "unitaire, ce que les données contredisent.",
      "Une part stable supposerait que l’alimentation absorbe toujours la "
      "même fraction du budget.",
      "L’inflation déforme les coefficients, mais la loi d’Engel porte sur "
      "l’effet du revenu."]),

'ch1-qcm-17': f(niv='connaitre', sp='c1-03',
 exp="Le coefficient budgétaire est la part des dépenses consacrées à un "
     "poste dans le total de la consommation. C’est l’outil de mesure de la "
     "loi d’Engel : suivre son évolution pour l’alimentation, le logement ou "
     "les loisirs renseigne sur la transformation des modes de vie.",
 why=["Le rapport entre impôts et dépenses publiques est un solde "
      "budgétaire.",
      "Le rapport salaires sur PIB est le partage de la valeur ajoutée.",
      "Le taux de couverture concerne le commerce extérieur."]),

'ch1-qcm-18': f(niv='connaitre', sp='c1-03',
 exp="Franco Modigliani développe entre 1953 et 1975 la théorie du cycle de "
     "vie : il ajoute au revenu courant le patrimoine et l’âge comme "
     "variables explicatives. La consommation s’apprécie sur la durée de vie "
     "entière, le revenu étant réparti de façon inégale selon l’âge.",
 why=["Keynes retient le revenu courant de la période.",
      "Friedman raisonne sur le revenu permanent, proche mais distinct : il "
      "insiste sur l’anticipation plutôt que sur l’âge.",
      "Duesenberry met en avant le revenu relatif et les effets de "
      "comparaison sociale."]),

'ch1-qcm-19': f(niv='comprendre', sp='c1-03',
 exp="L’effet de cliquet désigne la rigidité à la baisse de la "
     "consommation : lorsque le revenu diminue, les ménages réduisent "
     "d’abord leur épargne pour maintenir leur niveau de vie antérieur. La "
     "consommation dépend donc du revenu le plus élevé atteint dans le "
     "passé, non du seul revenu courant.",
 why=["Imiter les plus aisés est l’effet de démonstration, l’autre mécanisme "
      "de Duesenberry, qui joue dans la comparaison sociale, non dans le "
      "temps.",
      "L’effet des prix sur les quantités est l’élasticité-prix.",
      "La relation entre épargne et taux d’intérêt relève de l’arbitrage "
      "intertemporel néoclassique."],
 diss="Les deux effets de Duesenberry — cliquet dans le temps, démonstration "
      "dans l’espace social — expliquent pourquoi la propension moyenne à "
      "consommer reste stable à long terme, ce que la fonction keynésienne "
      "ne prévoyait pas."),

'ch1-qcm-33': f(niv='comprendre', sp='c1-03',
 exp="Le modèle du cycle de vie suppose que les ménages financent leur "
     "retraite par l’épargne accumulée pendant la vie active : il décrit donc "
     "mieux un système par capitalisation, comme aux États-Unis, qu’un "
     "système par répartition, où la pension est assurée par les cotisations "
     "des actifs et où l’incitation à désépargner est plus faible.",
 why=["La France, où la retraite est principalement par répartition, "
      "correspond moins bien au modèle.",
      "L’Allemagne relève également d’une logique de répartition.",
      "Le Japon a une épargne élevée, mais ce n’est pas le pays que le cours "
      "retient pour illustrer le modèle."]),

'ch1-vf-6': f(niv='comprendre', sp='c1-03',
 exp="C’est Friedman qui relie la consommation au revenu permanent anticipé. "
     "Keynes retient le revenu courant de la période : c’est précisément la "
     "différence qui fonde la critique de Friedman, selon laquelle le "
     "multiplicateur d’un revenu transitoire est faible."),

'ch1-vf-7': f(niv='connaitre', sp='c1-03',
 exp="L’effet de démonstration est bien le second mécanisme de Duesenberry : "
     "la consommation dépend du revenu relatif, c’est-à-dire du revenu "
     "comparé à celui des groupes de référence. Si les voisins consomment "
     "davantage, le ménage est incité à suivre, même à revenu inchangé."),

'ch1-vf-12': f(niv='appliquer', sp='c1-03',
 exp="Friedman prévoit l’inverse : une prime exceptionnelle est un revenu "
     "transitoire, qui ne modifie pas le revenu permanent. Les ménages "
     "l’épargnent donc en grande partie et maintiennent leur consommation. "
     "C’est l’argument qui fragilise les relances par versement ponctuel."),

'ch1-vf-14': f(niv='comprendre', sp='c1-03',
 exp="Easterlin (1974) montre exactement le contraire : à long terme, la "
     "hausse du revenu moyen d’un pays ne s’accompagne pas nécessairement "
     "d’une hausse du bonheur déclaré. Au-delà d’un certain seuil, la "
     "comparaison sociale l’emporte sur le niveau absolu de revenu.",
 diss="Le paradoxe d’Easterlin sert d’argument classique contre le PIB comme "
      "mesure du bien-être, et prolonge la logique du revenu relatif de "
      "Duesenberry."),

'ch1-vf-18': f(niv='comprendre', sp='c1-03',
 exp="C’est le profil type du cycle de vie : endettement ou faible épargne "
     "dans la jeunesse, quand le revenu est bas et les besoins élevés ; "
     "épargne pendant la période d’activité, quand le revenu culmine ; "
     "désépargne à la retraite, quand le revenu chute. La consommation est "
     "ainsi lissée alors que le revenu, lui, varie fortement."),

# ======================================= c1-04 · l'État et la fiscalité
'ch1-qcm-4': f(niv='connaitre', sp='c1-04',
 exp="APU désigne les administrations publiques : l’État et ses opérateurs, "
     "les administrations publiques locales et les administrations de "
     "sécurité sociale. C’est le secteur institutionnel dont le solde "
     "constitue le déficit public et dont les emprunts forment la dette "
     "publique.",
 why=["« Associations publiques unifiées » n’existe pas en comptabilité "
      "nationale.",
      "Les agents de production relèveraient des sociétés non financières.",
      "Les autorités de prélèvement ne forment pas un secteur "
      "institutionnel."]),

'ch1-qcm-20': f(niv='connaitre', sp='c1-04',
 exp="Musgrave (Théorie des finances publiques, 1959) distingue trois "
     "fonctions : l’allocation des ressources, qui corrige les défaillances "
     "du marché ; la stabilisation, qui amortit les fluctuations ; la "
     "redistribution, qui modifie la répartition des revenus. Les trois "
     "peuvent entrer en tension — une relance de stabilisation peut creuser "
     "le déficit et contraindre la redistribution.",
 why=["« Production, redistribution, financement » mélange des moyens et "
      "des fonctions.",
      "« Régulation, taxation, protection » décrit des instruments, pas la "
      "typologie de Musgrave.",
      "« Offre, demande, équilibre » relève de l’analyse des marchés."],
 diss="La typologie de Musgrave est l’ossature la plus solide pour un plan "
      "sur le rôle de l’État : une partie par fonction, en montrant que "
      "leurs exigences peuvent se contredire."),

'ch1-qcm-21': f(niv='comprendre', sp='c1-04',
 exp="La courbe de Laffer résume l’idée que « trop d’impôt tue l’impôt » : "
     "au-delà d’un certain taux, la contraction de l’assiette l’emporte sur "
     "la hausse du taux et les recettes diminuent. Le cours rappelle la "
     "critique : cette courbe « ne relève pas de faits empiriques » pour "
     "certains économistes, et le taux de retournement n’est pas "
     "observable.",
 why=["La relation entre PIB et chômage est la loi d’Okun.",
      "La relation entre consommation et revenu est la fonction de "
      "consommation.",
      "L’effet de l’inflation sur l’épargne est l’effet d’encaisse réelle."]),

'ch1-qcm-22': f(niv='connaitre', sp='c1-04',
 exp="La consommation sur place en restauration relève du taux intermédiaire "
     "de 10 %. La TVA comporte plusieurs taux selon les biens, ce qui en "
     "fait un instrument de politique sectorielle autant qu’un impôt de "
     "rendement.",
 why=["5,5 % est le taux réduit, appliqué notamment aux produits "
      "alimentaires de base.",
      "7 % n’est plus un taux en vigueur.",
      "20 % est le taux normal, appliqué à la plupart des biens et "
      "services."]),

'ch1-qcm-23': f(niv='connaitre', sp='c1-04',
 exp="La France compte environ 41 millions de foyers fiscaux, dont 45 % "
     "seulement acquittent l’impôt sur le revenu. L’écart tient à la "
     "progressivité du barème et au quotient familial, qui exonèrent les "
     "foyers aux revenus les plus faibles.",
 why=["20 millions sous-estime de moitié le nombre de foyers.",
      "30 millions reste très en deçà du chiffre du cours.",
      "55 millions dépasse le nombre de foyers et se rapproche de la "
      "population adulte."]),

'ch1-qcm-24': f(niv='connaitre', sp='c1-04',
 exp="La contribution sociale généralisée, créée en 1991, finance la "
     "sécurité sociale — maladie, famille, chômage, retraites. Elle a une "
     "assiette très large, qui inclut les revenus du capital, et un taux "
     "proportionnel : c’est l’exemple d’un prélèvement de rendement, non "
     "progressif.",
 why=["« Cotisation sociale généralisée » est le piège le plus fréquent : "
      "la CSG est un impôt, non une cotisation ouvrant des droits.",
      "« Charge salariale globale » n’existe pas.",
      "« Crédit social garanti » n’existe pas davantage."]),

'ch1-qcm-25': f(niv='connaitre', sp='c1-04',
 exp="Alexis Spire publie Résistances à l’impôt, attachement à l’État "
     "(2018). Sa thèse : les citoyens peuvent critiquer ou contourner "
     "l’impôt tout en restant attachés à l’État et à ses services. Le "
     "consentement fiscal dépend donc du sentiment de justice du système "
     "plus que de son niveau.",
 why=["Piketty travaille sur la concentration des patrimoines et la "
      "fiscalité progressive.",
      "Jaravel travaille sur l’inflation différenciée selon les revenus.",
      "Rosanvallon analyse la crise de l’État providence (1981)."],
 diss="Spire fournit l’argument sociologique dans un sujet sur le "
      "consentement à l’impôt : ce n’est pas le taux qui fait la révolte "
      "fiscale, c’est la perception de l’injustice."),

'ch1-qcm-26': f(niv='comprendre', sp='c1-04',
 exp="Le niveau de vie élargi ajoute au revenu disponible la valeur des "
     "services publics reçus — éducation, santé, logement social. Il montre "
     "que la redistribution en nature réduit les écarts bien davantage que "
     "la seule redistribution monétaire.",
 why=["Le salaire brut est un revenu primaire avant prélèvements.",
      "Le PIB par habitant corrigé de l’inflation est une moyenne "
      "macroéconomique, pas une mesure par ménage.",
      "La somme des revenus primaires et secondaires est le revenu avant "
      "prélèvements, sans les services publics."],
 diss="Argument décisif pour nuancer les comparaisons internationales "
      "d’inégalités : un pays à forte redistribution en nature apparaît plus "
      "inégalitaire qu’il ne l’est si l’on s’en tient au revenu monétaire."),

'ch1-qcm-28': f(niv='connaitre', sp='c1-04',
 exp="Les traités européens fixent deux références : un déficit public "
     "inférieur à 3 % du PIB et une dette inférieure à 60 % du PIB. Ce sont "
     "des valeurs de référence encadrées par des procédures, et non des "
     "interdictions absolues.",
 why=["2 % et 50 % ne correspondent à aucune règle européenne.",
      "5 % et 80 % non plus, même si la dette constatée dépasse souvent ce "
      "second niveau.",
      "Il existe bien un encadrement : l’absence de contrainte est fausse."]),

'ch1-qcm-31': f(niv='comprendre', sp='c1-04',
 exp="Le revenu national brut corrige le PIB des revenus du capital et du "
     "travail échangés avec le reste du monde : RNB = PIB − revenus versés "
     "au reste du monde + revenus reçus du reste du monde. Le PIB mesure ce "
     "qui est produit sur le territoire, le RNB ce qui revient aux résidents.",
 why=["C’est l’inverse : le PIB est territorial et ignore ces flux.",
      "Le RNB se calcule aussi bien en valeur qu’en volume.",
      "Les deux agrégats diffèrent dès qu’un pays verse ou reçoit des "
      "revenus du reste du monde."]),

'ch1-qcm-36': f(niv='connaitre', sp='c1-04',
 exp="Une niche fiscale est un avantage — déduction, réduction, crédit "
     "d’impôt — dont bénéficie un contribuable remplissant certaines "
     "conditions. Le cours relève 483 taxes et impôts pour 474 niches : "
     "l’ampleur du dispositif explique l’écart entre le taux affiché et le "
     "taux effectivement payé.",
 why=["Un impôt progressif est un mode de taxation, non une dérogation.",
      "La taxe sur le patrimoine immobilier est un impôt, pas un avantage.",
      "Un prélèvement sur les revenus du capital est également un impôt."]),

'ch1-qcm-41': f(niv='connaitre', sp='c1-04',
 exp="La taxe Zucman est une taxe plancher de 2 % sur le patrimoine des "
     "foyers détenant plus de 100 millions d’euros, soit environ 1 800 "
     "foyers fiscaux. Elle est différentielle : on déduit les impôts déjà "
     "acquittés pour ne payer que le complément permettant d’atteindre ce "
     "plancher.",
 why=["Il ne s’agit pas d’une taxe sur la consommation.",
      "Le seuil porte sur le patrimoine, non sur un revenu annuel d’un "
      "million d’euros.",
      "La taxe carbone est un instrument environnemental sans rapport."],
 diss="Les trois critiques relevées par le cours — rendement discuté et "
      "surévalué, risque de fuite des capitaux, difficulté d’évaluation du "
      "patrimoine non coté — donnent une partie de nuance toute prête dans "
      "un sujet sur la fiscalité du capital."),

'ch1-vf-9': f(niv='comprendre', sp='c1-04',
 exp="La TVA est un impôt proportionnel dans son taux, mais dégressif dans "
     "son poids : les ménages modestes consomment une part plus élevée de "
     "leur revenu, la TVA y absorbe donc une fraction plus grande. Elle pèse "
     "ainsi relativement plus sur les bas revenus, à l’inverse d’un impôt "
     "progressif comme l’impôt sur le revenu."),

'ch1-vf-15': f(niv='connaitre', sp='c1-04',
 exp="Le cours indique que 45 % des individus paient l’impôt sur le revenu, "
     "sur environ 41 millions de foyers fiscaux. Ce taux s’explique par la "
     "progressivité du barème, le quotient familial et les seuils d’entrée "
     "dans l’imposition."),

'ch1-vf-17': f(niv='connaitre', sp='c1-04',
 exp="Rosanvallon (La crise de l’État-providence, 1981) identifie bien trois "
     "crises : une crise de financement, les dépenses croissant plus vite "
     "que les recettes ; une crise d’efficacité, les dispositifs atteignant "
     "mal leurs objectifs ; une crise de légitimité, le consentement se "
     "délitant."),

'ch1-vf-20': f(niv='appliquer', sp='c1-04',
 exp="Le coefficient multiplicateur est bien le rapport de la valeur "
     "d’arrivée à la valeur de départ : il mesure par combien une grandeur a "
     "été multipliée. Un coefficient de 1,15 correspond à une hausse de "
     "15 % ; c’est l’outil de base pour comparer des évolutions."),

'ch1-open-1': f(niv='comprendre', sp='c1-02',
 ans={'modele': "L’approche est dite monétaire parce qu’elle ne retient "
      "qu’un critère, le revenu : est pauvre le ménage dont le niveau de vie "
      "est inférieur à un seuil fixé en proportion du revenu médian. Elle "
      "ignore les conditions de vie, le patrimoine, l’accès aux services "
      "publics et la dimension subjective de la privation.",
      'cles': [{'f': ['revenu', 'monetaire'], 'l': 'le critère retenu est le revenu'},
               {'f': ['seuil'], 'l': 'la comparaison se fait à un seuil'},
               {'f': ['conditions de vie', 'logement', 'sante', 'services publics'],
                'l': 'elle laisse de côté les conditions de vie'}]},
 exp="Le cours oppose cette mesure à la pauvreté en conditions de vie et au "
     "niveau de vie élargi, qui intègre la valeur des services publics reçus."),

'ch1-open-10': f(niv='raisonner', sp='c1-02',
 ans={'modele': "L’approche monétaire ignore les privations concrètes "
      "(logement, chauffage, alimentation), l’accès aux services publics, "
      "l’isolement social et le sentiment d’exclusion. Elle est sensible à "
      "la convention retenue — 50 % ou 60 % du revenu médian — et suit "
      "mécaniquement le niveau de vie du pays : quand la population "
      "s’enrichit, le seuil monte et le nombre de pauvres ne baisse pas "
      "nécessairement.",
      'cles': [{'f': ['conditions de vie', 'privation', 'logement'],
                'l': 'elle ignore les privations matérielles concrètes'},
               {'f': ['services publics', 'elargi', 'nature'],
                'l': 'elle ignore les services publics reçus'},
               {'f': ['convention', 'seuil', '50', '60'],
                'l': 'elle dépend d’une convention de seuil'},
               {'f': ['subjectif', 'exclusion', 'isolement'],
                'l': 'elle laisse de côté la dimension subjective'}]},
 exp="Le niveau de vie élargi et la pauvreté en conditions de vie ont été "
     "construits précisément pour corriger ces angles morts.",
 diss="Ces limites justifient une partie entière dans un sujet sur la mesure "
      "de la pauvreté : un indicateur n’est jamais neutre, il oriente la "
      "politique qu’il sert à évaluer."),

'ch1-aut195-1': f(niv='comprendre', sp='c1-04',
 exp="Les recettes sont le produit d’un taux par une assiette. Au-delà d’un "
     "certain taux, la contraction de l’assiette — moindre activité "
     "déclarée, optimisation, exil fiscal — l’emporte sur la hausse du taux, "
     "et le produit de l’impôt diminue. Le cours rappelle que cette courbe "
     "« ne relève pas de faits empiriques » selon certains économistes.",
 why=["Une croissance continue des recettes supposerait une assiette "
      "insensible au taux.",
      "La neutralité de l’impôt sur l’activité est précisément ce que la "
      "courbe conteste.",
      "Les recettes dépendent du taux autant que de l’assiette : les deux "
      "sont liés."]),

# ============================== c1-05 · dette, déficit et limites du PIB
'ch1-qcm-27': f(niv='connaitre', sp='c1-05',
 exp="Le cours retient environ 3 400 milliards d’euros de dette publique, "
     "soit de l’ordre de 114 % du PIB. La dette est un stock d’emprunts "
     "accumulés, à distinguer du déficit, qui est un flux annuel.",
 why=["1 500 milliards correspond à un niveau atteint bien avant.",
      "2 000 milliards reste très en deçà du chiffre du cours.",
      "5 000 milliards dépasse nettement le niveau constaté."]),

'ch1-qcm-32': f(niv='connaitre', sp='c1-05',
 exp="Le quantitative easing consiste pour la banque centrale à racheter de "
     "la dette publique sur le marché : cela fait baisser les taux, soutient "
     "la liquidité et facilite le refinancement de l’État. Le cours relève "
     "la contrepartie : le dispositif peut nourrir de nouveaux déséquilibres.",
 why=["L’austérité budgétaire est une politique budgétaire, pas une "
      "opération de banque centrale.",
      "La hausse des taux directeurs est exactement la politique inverse.",
      "La suppression de la TVA est une mesure fiscale."]),

'ch1-qcm-35': f(niv='connaitre', sp='c1-05',
 exp="Le prêt garanti par l’État a été mis en place pendant la crise "
     "sanitaire : l’État s’engage à rembourser le créancier en cas de "
     "défaillance du débiteur, à hauteur de 90 % du capital emprunté, pour "
     "un total de 140 à 170 milliards d’euros. Le crédit en a été facilité, "
     "au prix d’un accroissement de la dette publique.",
 why=["« Plan de garantie économique » n’existe pas.",
      "« Programme de gestion des entreprises » non plus.",
      "« Prélèvement global exceptionnel » désignerait un impôt, non une "
      "garantie."]),

'ch1-vf-4': f(niv='connaitre', sp='c1-05',
 exp="Le cours l’établit : en France, le travail domestique représente plus "
     "d’heures que le travail rémunéré. C’est l’illustration la plus nette "
     "d’une limite du PIB, qui ne comptabilise que la production marchande "
     "et non marchande évaluée, et laisse de côté cette production "
     "domestique."),

'ch1-vf-8': f(niv='connaitre', sp='c1-05',
 exp="La référence européenne est bien de 3 % du PIB pour le déficit public, "
     "complétée par une référence de 60 % pour la dette. Ces seuils "
     "s’appliquent au déficit de l’ensemble des administrations publiques, "
     "non au seul budget de l’État."),

'ch1-vf-10': f(niv='comprendre', sp='c1-05',
 exp="Un écart de production positif signifie que l’activité effective "
     "dépasse l’activité potentielle : les capacités sont saturées, et les "
     "entreprises peuvent répercuter la demande excédentaire sur les prix "
     "plutôt que sur les volumes. D’où la tension inflationniste."),

'ch1-vf-13': f(niv='connaitre', sp='c1-05',
 ans=True,
 q="Le pacte Dutreil est une niche fiscale qui allège l’imposition lors de "
   "la transmission d’une entreprise familiale.",
 exp="Le cours cite le pacte Dutreil comme exemple de niche fiscale : il "
     "exonère l’impôt sur l’héritage d’une entreprise sous conditions "
     "d’engagement de conservation. C’est l’un des 474 dispositifs "
     "dérogatoires recensés face à 483 taxes et impôts."),

'ch1-vf-19': f(niv='connaitre', sp='c1-05',
 exp="Le bouclier tarifaire désigne l’ensemble des mesures destinées à "
     "limiter l’effet de la flambée des prix de l’énergie, en contenant la "
     "hausse du prix de l’électricité à 15 %. C’est une dépense publique "
     "qui a pesé sur le déficit, au nom de la fonction de stabilisation."),

'ch1-open-5': f(niv='comprendre', sp='c1-04',
 ans={'modele': "La redistribution réduit le taux de pauvreté par deux "
      "canaux : les prélèvements progressifs réduisent les hauts revenus, "
      "les prestations — RSA, allocations logement, prestations familiales — "
      "relèvent le revenu disponible des ménages modestes au-dessus du "
      "seuil. Le cours ajoute une limite : le système réduit beaucoup moins "
      "les inégalités de patrimoine que celles de revenu.",
      'cles': [{'f': ['prestation', 'allocation', 'rsa'],
                'l': 'les prestations relèvent le revenu disponible'},
               {'f': ['impot', 'impôt', 'prelevement', 'progressif'],
                'l': 'les prélèvements réduisent les hauts revenus'},
               {'f': ['patrimoine', 'limite', 'moins'],
                'l': 'la redistribution agit peu sur les inégalités de patrimoine'}]},
 exp="C’est la fonction de redistribution de Musgrave à l’œuvre, et sa "
     "limite : elle agit sur les flux de revenus, bien peu sur les stocks de "
     "patrimoine."),

'ch1-open-12': f(niv='raisonner', sp='c1-05',
 ans={'modele': "L’inflation réduit le pouvoir d’achat à revenu nominal "
      "inchangé : la capacité à acquérir les biens essentiels diminue, et "
      "des ménages situés juste au-dessus du seuil basculent dans la "
      "privation réelle sans que leur revenu ait changé. L’effet est "
      "d’autant plus fort que l’inflation porte sur l’alimentation et "
      "l’énergie, postes au coefficient budgétaire élevé chez les ménages "
      "modestes.",
      'cles': [{'f': ['pouvoir d achat', 'pouvoir d’achat'],
                'l': 'l’inflation ampute le pouvoir d’achat'},
               {'f': ['seuil', 'bascule', 'limite'],
                'l': 'des ménages proches du seuil basculent'},
               {'f': ['alimentation', 'energie', 'énergie', 'coefficient'],
                'l': 'l’inflation est plus forte sur les postes contraints'}]},
 exp="Le seuil de pauvreté étant calculé en euros courants à partir du "
     "revenu médian, il suit l’inflation avec retard : la mesure réagit plus "
     "lentement que la situation vécue.",
 diss="Bon argument pour montrer qu’un indicateur monétaire peut rester "
      "stable alors que la pauvreté vécue augmente — à mobiliser dans un "
      "sujet sur la mesure du niveau de vie."),
})


# =============================================================== questions neuves
NEW = [

f(id='q1-n01', sp='c1-01', niv='connaitre', type='assoc', b=79,
  q="Associez chaque secteur institutionnel à sa fonction principale en "
    "comptabilité nationale.",
  ans=[["Sociétés non financières", "Produire des biens et des services marchands"],
       ["Sociétés financières", "Financer et gérer les moyens de financement"],
       ["Administrations publiques", "Produire des services non marchands et redistribuer"],
       ["Ménages", "Consommer ; les entreprises individuelles y sont rattachées"],
       ["Reste du monde", "Retracer les opérations avec les unités non résidentes"]],
  exp="Le classement repose sur la fonction principale et la ressource "
      "principale de l’unité. Deux pièges reviennent : les entreprises "
      "individuelles sont rattachées aux ménages, faute de personnalité "
      "juridique distincte ; et le reste du monde n’est pas un secteur "
      "« étranger » mais le miroir comptable des opérations avec les "
      "non-résidents."),

f(id='q1-n02', sp='c1-02', niv='comprendre', type='qcmm', b=185,
  q="Selon le cours, quels éléments déterminent la décision d’investir ? "
    "(plusieurs réponses)",
  opts=["Le niveau de la demande anticipée",
        "La rentabilité attendue du projet, comparée à son coût",
        "Les conditions de financement, dont le niveau de l’épargne disponible",
        "Le nombre de salariés de l’entreprise",
        "Le taux de TVA appliqué au produit"],
  ans=[0, 1, 2],
  why=["Exacte : l’investissement suit la demande anticipée, mesurée par la "
       "croissance, les commandes et les perspectives d’exportation.",
       "Exacte : l’entreprise compare rendement attendu et coût initial, en "
       "intégrant le risque.",
       "Exacte : autofinancement, coût du crédit et épargne disponible "
       "conditionnent la réalisation du projet.",
       "La taille de l’effectif n’est pas un déterminant de la décision "
       "d’investir dans le cours.",
       "Le taux de TVA pèse sur le prix final, non sur l’arbitrage "
       "d’investissement."],
  exp="Le cours retient trois déterminants — demande, rentabilité, "
      "conditions de financement — auxquels s’ajoute le profit, présenté "
      "comme un préalable et une condition. Cette liste est l’articulation "
      "directe entre l’analyse keynésienne, qui insiste sur les débouchés, "
      "et l’analyse par les coûts, qui insiste sur la rentabilité.",
  diss="Le trio demande / rentabilité / financement permet de structurer "
       "toute dissertation sur l’investissement : chaque politique publique "
       "— relance, baisse de charges, taux bas — agit sur l’un des trois."),

f(id='q1-n03', sp='c1-02', niv='raisonner', type='ordre', b=199,
  q="Remettez dans l’ordre les étapes du multiplicateur d’investissement.",
  ans=["Une dépense d’investissement supplémentaire est engagée",
       "Elle devient un revenu pour ceux qui produisent le bien d’équipement",
       "Ce revenu est consommé à hauteur de la propension marginale à consommer",
       "Cette consommation devient à son tour un revenu pour d’autres agents",
       "Les vagues successives s’amortissent et le revenu total augmente de 1/(1−c) fois la dépense initiale"],
  exp="Chaque étape engendre la suivante parce que la dépense des uns est le "
      "revenu des autres. L’amortissement vient de la fuite : à chaque tour, "
      "une fraction (1 − c) du revenu est épargnée et sort du circuit. Avec "
      "c = 0,8, la somme des vagues vaut 5 fois la dépense initiale en "
      "économie fermée ; l’ouverture ajoute une seconde fuite, les "
      "importations, et ramène le multiplicateur à 2,5 dans l’exemple du "
      "cours.",
  diss="Dérouler explicitement ces cinq étapes vaut mieux que citer la "
       "formule : le correcteur vérifie que vous savez pourquoi la série "
       "converge, c’est-à-dire pourquoi les fuites bornent le multiplicateur."),

f(id='q1-n04', sp='c1-02', niv='appliquer', type='qcm', b=199,
  q="La propension marginale à consommer d’une économie fermée passe de 0,8 "
    "à 0,75. Que devient le multiplicateur des dépenses autonomes ?",
  opts=["Il passe de 5 à 4", "Il passe de 5 à 4,5", "Il passe de 4 à 5",
        "Il reste inchangé, la propension à consommer n’entrant pas dans la formule"],
  ans=0,
  why=["Le calcul 1 / (1 − 0,75) donne 4 et non 4,5 : l’erreur vient d’une "
       "division approximative.",
       "La direction est inversée : une propension à consommer plus faible "
       "réduit le multiplicateur.",
       "La propension marginale à consommer est au contraire la seule "
       "variable de la formule k = 1 / (1 − c)."],
  exp="k = 1 / (1 − c). Avec c = 0,8, k = 1 / 0,2 = 5 ; avec c = 0,75, "
      "k = 1 / 0,25 = 4. Une baisse de cinq points de la propension à "
      "consommer fait perdre un point entier de multiplicateur : la fuite "
      "par l’épargne passe de 20 à 25 % du revenu à chaque tour.",
  diss="Ce calcul justifie de cibler une relance sur les ménages à forte "
       "propension à consommer : à dépense publique égale, l’effet sur le "
       "revenu national n’est pas le même selon le destinataire."),

f(id='q1-n05', sp='c1-03', niv='connaitre', type='assoc', b=299,
  q="Associez chaque auteur à l’idée qu’il défend sur la consommation.",
  ans=[["Keynes", "La consommation dépend du revenu courant ; la propension moyenne à consommer décroît avec le revenu"],
       ["Friedman", "La consommation dépend du revenu permanent anticipé sur le cycle de vie"],
       ["Modigliani", "L’âge et le patrimoine expliquent le profil d’épargne au cours de la vie"],
       ["Duesenberry", "La consommation dépend du revenu relatif : effet de cliquet et effet de démonstration"],
       ["Easterlin", "Au-delà d’un seuil, la hausse du revenu moyen n’élève plus le bonheur déclaré"]],
  exp="Les trois critiques de Keynes ne disent pas la même chose : Friedman "
      "déplace la variable explicative vers l’anticipation, Modigliani vers "
      "l’âge et le patrimoine, Duesenberry vers la comparaison sociale et "
      "l’habitude. Easterlin, lui, ne porte pas sur le niveau de "
      "consommation mais sur ce qu’il procure.",
  diss="Cette grille permet d’écrire une sous-partie entière : « la fonction "
       "de consommation keynésienne a été amendée dans trois directions "
       "distinctes », ce qui vaut mieux qu’une énumération d’auteurs."),

f(id='q1-n06', sp='c1-03', niv='raisonner', type='courte', b=334,
  q="Pourquoi la critique de Friedman affaiblit-elle l’efficacité d’une "
    "relance par transfert ponctuel ? Indiquez aussi sa limite.",
  ans={'modele': "Si la consommation dépend du revenu permanent, un "
       "transfert ponctuel est un revenu transitoire : il ne modifie pas le "
       "revenu anticipé sur le cycle de vie et est donc principalement "
       "épargné. Le multiplicateur de la mesure est alors faible. La limite "
       "tient aux contraintes de liquidité : un ménage modeste, endetté ou "
       "sans épargne, consomme l’essentiel d’un transfert, car il ne peut "
       "pas lisser sa consommation. L’efficacité dépend donc du ciblage.",
       'cles': [{'f': ['revenu permanent'], 'l': 'le raisonnement repose sur le revenu permanent'},
                {'f': ['transitoire', 'ponctuel', 'temporaire'],
                 'l': 'un transfert ponctuel est un revenu transitoire'},
                {'f': ['epargne', 'épargné', 'epargné'],
                 'l': 'il est donc principalement épargné'},
                {'f': ['contrainte', 'liquidite', 'modeste', 'ciblage'],
                 'l': 'la limite : les ménages contraints consomment ce transfert'}]},
  exp="La critique est conditionnelle : elle vaut pour des ménages capables "
      "d’épargner et d’emprunter librement. Dès que la contrainte de "
      "liquidité mord, la fonction de consommation keynésienne redevient la "
      "bonne description.",
  diss="C’est le type de nuance qui distingue une copie : énoncer la "
       "critique, puis la condition sous laquelle elle tombe."),

f(id='q1-n07', sp='c1-04', niv='comprendre', type='qcmm', b=449,
  q="Quelles propositions décrivent correctement les fonctions de l’État "
    "selon Musgrave ? (plusieurs réponses)",
  opts=["La fonction d’allocation corrige les défaillances du marché et "
        "fournit les biens collectifs",
        "La fonction de stabilisation cherche à amortir les fluctuations de "
        "l’activité",
        "La fonction de redistribution modifie la répartition des revenus et "
        "des patrimoines",
        "La fonction de production impose à l’État de produire lui-même "
        "l’essentiel des biens marchands",
        "La fonction d’allocation consiste à fixer les prix de marché"],
  ans=[0, 1, 2],
  why=["Exacte : l’allocation répond aux biens collectifs et aux "
       "externalités.",
       "Exacte : c’est la fonction conjoncturelle, mise en œuvre par les "
       "politiques budgétaire et monétaire.",
       "Exacte : impôts et prestations modifient la distribution, même si le "
       "cours note que l’effet sur le patrimoine reste faible.",
       "Musgrave ne retient pas de « fonction de production » : l’État "
       "produit des services non marchands, non l’essentiel des biens "
       "marchands.",
       "Fixer les prix relèverait d’une économie administrée, pas de la "
       "fonction d’allocation."],
  exp="Les trois fonctions se distinguent par leur horizon et leur "
      "instrument : l’allocation est structurelle, la stabilisation "
      "conjoncturelle, la redistribution permanente. Le cours souligne "
      "qu’elles peuvent entrer en tension, une relance de stabilisation "
      "creusant le déficit qui contraindra ensuite la redistribution."),

f(id='q1-n08', sp='c1-04', niv='appliquer', type='qcm', b=506,
  q="Deux ménages consacrent respectivement 90 % et 40 % de leur revenu à la "
    "consommation taxée au taux normal. Que peut-on en conclure sur la TVA ?",
  opts=["Elle est progressive, puisque le ménage aisé paie un montant absolu "
        "plus élevé",
        "Elle est proportionnelle au revenu des deux ménages",
        "Elle est dégressive rapportée au revenu : elle pèse relativement "
        "plus sur le ménage modeste",
        "Elle est neutre, le taux étant identique pour les deux"],
  ans=2,
  why=["Le montant absolu plus élevé ne dit rien du poids relatif, qui est "
       "le critère de progressivité.",
       "Elle serait proportionnelle si les deux ménages consommaient la même "
       "part de leur revenu : ce n’est pas le cas.",
       "Le taux identique ne vaut pas neutralité : c’est la part du revenu "
       "consommée qui fait la différence."],
  exp="Un taux unique appliqué à une base qui représente une part décroissante "
      "du revenu produit un prélèvement dégressif : le ménage qui consomme "
      "90 % de son revenu acquitte de la TVA sur 90 % de celui-ci, l’autre "
      "sur 40 % seulement. C’est l’argument central contre le recours à la "
      "TVA comme instrument de rendement.",
  diss="Opposition classique à exploiter : la TVA est un bon impôt de "
       "rendement et un mauvais impôt de justice ; l’impôt sur le revenu, "
       "progressif, fait l’inverse avec seulement 45 % de foyers imposés."),

f(id='q1-n09', sp='c1-04', niv='raisonner', type='qcm', b=561,
  q="Le cours relève que le patrimoine des dix plus grandes fortunes "
    "françaises atteint 42 % du PIB en 2025, contre 6 % en 1996, alors que "
    "le système social réduit fortement les inégalités de revenus. Qu’en "
    "conclure ?",
  opts=["La redistribution a échoué : les inégalités de revenus se sont "
        "creusées au même rythme",
        "La redistribution agit sur les flux de revenus mais très peu sur les "
        "stocks de patrimoine",
        "La concentration patrimoniale prouve que la croissance ne profite "
        "qu’aux plus riches",
        "Le PIB n’est pas un bon dénominateur pour mesurer un patrimoine"],
  ans=1,
  why=["Le cours dit l’inverse : le système fiscal et social réduit bien les "
       "inégalités de revenus.",
       "La concentration patrimoniale ne permet pas à elle seule de conclure "
       "sur la répartition des fruits de la croissance.",
       "Rapporter un stock à un flux est discutable, mais c’est une "
       "convention de comparaison, pas la conclusion du passage."],
  exp="C’est l’asymétrie que souligne le cours : la redistribution monétaire "
      "et en nature corrige la distribution des revenus, mais le patrimoine "
      "se transmet et se valorise sans être proportionnellement imposé. "
      "D’où les débats sur une fiscalité du capital, dont la taxe Zucman est "
      "l’exemple discuté.",
  diss="Articulation directe avec Piketty : si le rendement du patrimoine "
       "excède durablement la croissance, les écarts de patrimoine se "
       "creusent même lorsque les écarts de revenus sont contenus."),

f(id='q1-n10', sp='c1-05', niv='comprendre', type='qcmm', b=683,
  q="Parmi les solutions à l’endettement public examinées par le cours, "
    "lesquelles sont effectivement citées ? (plusieurs réponses)",
  opts=["L’annulation de la dette, solution extrême et rarement appliquée",
        "L’inflation, qui réduit la valeur réelle de la dette",
        "Le rachat de dette publique par la banque centrale",
        "La croissance économique, qui élève les recettes fiscales",
        "La vente des réserves d’or de la banque centrale"],
  ans=[0, 1, 2, 3],
  why=["Exacte : elle soulage le budget mais fait perdre la confiance des "
       "créanciers et menace d’isolement financier.",
       "Exacte : si les prix montent, la valeur réelle de la dette baisse — "
       "au risque de déstabiliser l’économie si l’inflation s’emballe.",
       "Exacte : c’est le quantitative easing, qui abaisse les taux et "
       "soutient la liquidité, au prix de déséquilibres nouveaux.",
       "Exacte : une croissance forte augmente les recettes et allège le "
       "ratio dette sur PIB.",
       "La vente des réserves d’or n’est pas une solution évoquée par le "
       "cours."],
  exp="Le cours ajoute un cinquième levier, l’impôt exceptionnel, et conclut "
      "par un critère : l’endettement est nécessaire pour financer l’action "
      "publique et amortir les crises, mais il doit rester soutenable, "
      "c’est-à-dire remboursable sans compromettre l’avenir."),

f(id='q1-n11', sp='c1-05', niv='raisonner', type='ordre', b=689,
  q="Remettez dans l’ordre l’enchaînement par lequel l’inflation allège la "
    "dette publique, puis se retourne contre l’État.",
  ans=["Les prix augmentent, ce qui réduit la valeur réelle de la dette déjà émise",
       "Les recettes fiscales nominales progressent avec les prix et les salaires",
       "Le ratio dette sur PIB diminue mécaniquement, le dénominateur étant en valeur",
       "Les créanciers exigent une prime d’inflation sur les nouvelles émissions",
       "La charge de la dette augmente à mesure que l’ancienne dette est refinancée"],
  exp="L’allègement porte sur le stock déjà émis, à taux fixe : c’est un "
      "transfert des créanciers vers l’emprunteur. Mais il n’est acquis "
      "qu’une fois ; dès que l’État se refinance, les prêteurs intègrent "
      "l’inflation anticipée dans le taux exigé. L’inflation est donc un "
      "soulagement transitoire, et le cours rappelle qu’une inflation trop "
      "forte déstabilise l’économie.",
  diss="Cet enchaînement est l’argument à opposer à l’idée qu’« il suffirait "
       "d’un peu d’inflation » : l’effet s’épuise, et le coût se déplace sur "
       "le refinancement futur."),

f(id='q1-n12', sp='c1-05', niv='comprendre', type='qcm', b=726,
  q="Le cours indique que l’activité dissimulée est évaluée à 37 milliards "
    "d’euros et que l’INSEE l’intègre à son estimation du PIB. Pourquoi ?",
  opts=["Pour sanctionner fiscalement les activités illégales",
        "Parce que l’objectif du PIB est de mesurer la production, "
        "indépendamment de la légalité de l’activité",
        "Parce que les activités illégales sont marchandes et génèrent donc "
        "de la TVA",
        "Pour aligner les comptes français sur ceux des pays voisins"],
  ans=1,
  why=["La comptabilité nationale mesure, elle ne sanctionne pas : la "
       "fiscalité est un autre domaine.",
       "Ces activités échappent précisément à la TVA : ce n’est pas le motif "
       "de leur intégration.",
       "L’harmonisation statistique existe, mais le cours justifie "
       "l’intégration par l’exigence de mesure, non par la comparaison."],
  exp="Le cours est explicite : l’INSEE cherche à évaluer ces secteurs « sans "
      "prendre en compte l’aspect moral et la légalité » afin de mieux "
      "mesurer le PIB. Un agrégat de production doit couvrir toute la "
      "production, sous peine de sous-estimer l’activité réelle et de rendre "
      "les comparaisons internationales trompeuses. Le cours note toutefois "
      "que l’économie non observée reste peu fiable."),

f(id='q1-n13', sp='c1-05', niv='raisonner', type='courte', b=716,
  q="Citez trois limites du PIB relevées par le cours et expliquez ce que "
    "chacune laisse de côté.",
  ans={'modele': "Le PIB ignore le travail domestique, qui représente "
       "pourtant en France plus d’heures que le travail rémunéré. Il ne "
       "soustrait pas les dégradations environnementales : le cours indique "
       "qu’en retranchant le coût des émissions de gaz à effet de serre, on "
       "obtient un PIN augmenté inférieur de 4 %. Il mesure mal l’économie "
       "non observée, l’activité dissimulée étant évaluée à 37 milliards "
       "sans fiabilité garantie. Enfin il ne dit rien de la répartition ni "
       "du bien-être, d’où les comptes de la nation augmentée publiés par "
       "l’INSEE depuis novembre 2024.",
       'cles': [{'f': ['domestique'], 'l': 'le travail domestique n’est pas compté'},
                {'f': ['environnement', 'gaz a effet de serre', 'ges', 'pollution'],
                 'l': 'les dégradations environnementales ne sont pas déduites'},
                {'f': ['non observee', 'dissimulee', 'illicite', '37'],
                 'l': 'l’économie non observée est mal mesurée'},
                {'f': ['repartition', 'bien etre', 'bien-être', 'inegalite'],
                 'l': 'le PIB ne dit rien de la répartition ni du bien-être'}]},
  exp="Ces limites ne disqualifient pas l’agrégat : elles délimitent son "
      "usage. Le PIB reste la bonne mesure de la production marchande ; il "
      "est inadapté dès qu’on veut parler de soutenabilité ou de bien-être, "
      "ce qui explique les indicateurs complémentaires.",
  diss="Une copie solide ne se contente pas d’empiler les limites : elle "
       "montre que chacune appelle un indicateur distinct — comptes "
       "domestiques, PIB vert, comptes augmentés — et que le choix de "
       "l’indicateur engage le choix de l’objectif politique."),

f(id='q1-n14', sp='c1-01', niv='appliquer', type='vf', b=47,
  q="Le fort recul des défaillances d’entreprises en 2020 et 2021 montre que "
    "la crise sanitaire a épargné le tissu productif français.",
  ans=False,
  exp="Le recul — 36 535 défaillances en 2020 et 27 562 en 2021, contre "
      "environ 59 000 en moyenne de 2010 à 2019 — ne traduit pas la santé "
      "des entreprises mais l’ampleur des soutiens publics : chômage "
      "partiel, prêts garantis par l’État, reports de charges. Le rattrapage "
      "qui suit le confirme, avec 56 719 défaillances en 2023 et 67 000 en "
      "2025.",
  diss="Exemple précieux pour montrer qu’une statistique peut être "
       "entièrement commandée par la politique publique qui la précède : on "
       "ne lit pas une série sans connaître le dispositif qui la produit."),
]
