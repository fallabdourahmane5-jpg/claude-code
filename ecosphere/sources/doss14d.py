# -*- coding: utf-8 -*-
"""Ensemble 14 — L’inflation et la stabilité des prix (4/4)."""

from doss_base import d

d('n14-pouvoir-achat', 14, "Pouvoir d’achat",
  "La quantité de biens et de services qu’un revenu permet d’acquérir",
  "Le cours définit le pouvoir d’achat comme la quantité de biens et de "
  "services qu’un revenu peut acquérir. Il s’obtient en corrigeant le revenu "
  "disponible brut des effets de l’inflation, selon la formule du revenu "
  "nominal divisé par l’indice des prix et multiplié par cent. C’est donc une "
  "grandeur relative : elle dépend de l’écart entre l’évolution du revenu et "
  "celle des prix.",
  "Le cours construit le pouvoir d’achat à l’intérieur d’une chaîne de "
  "notions, et c’est cette position qui en fixe le sens exact. La chaîne part "
  "des revenus primaires, salaires, revenus du capital et autres revenus du "
  "travail ; elle passe au revenu disponible brut, obtenu en ajoutant les "
  "prestations sociales et en retirant les prélèvements obligatoires, "
  "c’est-à-dire le revenu réellement disponible pour consommer ou épargner ; "
  "et elle aboutit au pouvoir d’achat, défini comme la quantité de biens et "
  "de services qu’un revenu peut acquérir. Le cours précise l’opération : le "
  "revenu disponible brut est corrigé en retirant les effets de l’inflation, "
  "ce qui permet de mesurer combien de biens et services on peut réellement "
  "acheter. Il donne l’exemple décisif : si le salaire augmente de deux pour "
  "cent mais que les prix augmentent de trois pour cent, le pouvoir d’achat "
  "baisse. La formule est ensuite explicitée : le pouvoir d’achat du revenu "
  "égale le revenu nominal divisé par l’indice des prix et multiplié par "
  "cent, et le cours applique le calcul à un revenu nominal de mille avec un "
  "indice de cent dix, ce qui donne un revenu réel de neuf cent neuf. Cette "
  "même logique s’étend à toutes les grandeurs économiques : produit "
  "intérieur brut, consommation, investissement, revenu ou exportations "
  "peuvent être exprimés en valeur courante, aux prix de l’année en cours, ou "
  "en volume, à prix constants, en fixant une année de référence, ce que le "
  "cours appelle déflater. Le pouvoir d’achat est donc le cas particulier, "
  "appliqué aux ménages, d’une opération générale de passage du nominal au "
  "réel. Le cours ajoute enfin une précision de comparaison : pour comparer "
  "les ménages entre eux, on raisonne en niveau de vie, en pondérant par les "
  "unités de consommation, le premier adulte comptant pour une unité, chaque "
  "personne supplémentaire de plus de quatorze ans pour un demi et chaque "
  "enfant de moins de quatorze ans pour trois dixièmes, parce qu’un couple "
  "avec trois enfants n’a pas les mêmes besoins qu’une personne seule même à "
  "revenu disponible identique.",
  [("Le calcul du revenu disponible",
    "On part des revenus primaires, on ajoute les prestations sociales et on "
    "retire les prélèvements obligatoires : on obtient le revenu réellement "
    "disponible pour consommer ou épargner."),
   ("La correction par les prix",
    "On retire les effets de l’inflation en divisant le revenu nominal par "
    "l’indice des prix et en multipliant par cent : le cours donne l’exemple "
    "d’un revenu de mille et d’un indice de cent dix, soit neuf cent neuf en "
    "termes réels."),
   ("La comparaison de deux évolutions",
    "Ce qui compte est l’écart entre la hausse du revenu et celle des prix : "
    "le cours montre qu’un salaire en hausse de deux pour cent avec des prix "
    "en hausse de trois pour cent fait baisser le pouvoir d’achat."),
   ("Le passage de la valeur au volume",
    "La même opération s’applique à toutes les grandeurs : on déflate en "
    "fixant une année de référence, pour raisonner à prix constants plutôt "
    "qu’aux prix de l’année en cours."),
   ("La pondération par la taille du ménage",
    "Pour comparer les ménages, on passe au niveau de vie en pondérant par "
    "les unités de consommation, un pour le premier adulte, un demi par "
    "personne de plus de quatorze ans, trois dixièmes par enfant."),
   ("Le lien avec les dépenses contraintes",
    "Le cours relève qu’une partie de la consommation des ménages est "
    "pré-engagée, logement, chauffage et assurances, soit trente pour cent du "
    "revenu disponible et une part qui tend à augmenter, ce qui réduit la "
    "marge réellement arbitrable.")],
  [{'a': "La notion transforme une question de ressenti en grandeur "
         "calculable, par comparaison de deux taux de variation.",
    'cond': "Le calcul suppose un indice des prix pertinent pour le ménage "
            "considéré, ce que l’indice des prix à la consommation vise par "
            "son panier représentatif.",
    'lim': "Le panier est fixe et actualisé annuellement : il ne reflète pas "
           "la structure de consommation propre à chaque ménage, d’où l’écart "
           "fréquent entre inflation mesurée et inflation ressentie."},
   {'a': "Elle fournit la clé du passage du nominal au réel, applicable à "
         "toutes les grandeurs macroéconomiques.",
    'cond': "L’extension suppose que l’on dispose d’un déflateur adapté à la "
            "grandeur considérée, et d’une année de référence fixée.",
    'lim': "Le choix de l’année de référence influence les comparaisons de "
           "longue période : la grandeur en volume n’est jamais une donnée "
           "brute mais une construction."},
   {'a': "Elle articule le revenu et la protection sociale, puisque le revenu "
         "disponible intègre les prestations et les prélèvements.",
    'cond': "L’articulation suppose que l’on raisonne sur le revenu "
            "disponible brut et non sur les seuls revenus primaires.",
    'lim': "Le cours montre qu’une part croissante de ce revenu est "
           "pré-engagée, trente pour cent pour le logement, le chauffage et "
           "les assurances : le pouvoir d’achat mesuré surestime la marge "
           "réellement disponible."},
   {'a': "Elle se complète par le niveau de vie, qui rend les ménages "
         "comparables malgré des compositions différentes.",
    'cond': "La comparaison suppose l’échelle des unités de consommation du "
            "cours, un pour le premier adulte, un demi au-delà de quatorze "
            "ans, trois dixièmes en dessous.",
    'lim': "Cette échelle est conventionnelle : elle suppose des économies "
           "d’échelle domestiques dont l’ampleur réelle varie selon les "
           "postes de dépense."},
   {'a': "Elle explique pourquoi l’inflation est un enjeu de répartition et "
         "pas seulement de niveau général des prix.",
    'cond': "L’argument suppose que les revenus ne soient pas tous indexés "
            "de la même manière sur les prix.",
    'lim': "Le cours reste prudent sur les effets : il montre que les effets "
           "de l’inflation sur l’épargne sont ambivalents, entre effet "
           "d’encaisse réelle et fuite devant la monnaie."}],
  [{'t': "L’inflation ne réduit pas le pouvoir d’achat puisque les salaires "
         "finissent par suivre les prix.",
    'qui': "La lecture par l’indexation, que le cours expose dans la boucle "
           "entre prix et salaires.",
    'rep': "Le cours fournit le contre-exemple chiffré : si le salaire "
           "augmente de deux pour cent et les prix de trois pour cent, le "
           "pouvoir d’achat baisse ; le rattrapage, lorsqu’il a lieu, est "
           "décalé et partiel."},
   {'t': "La hausse de l’indice des prix surestime la perte de pouvoir "
         "d’achat, car le panier ne suit pas les substitutions des "
         "consommateurs.",
    'qui': "L’objection méthodologique liée au caractère fixe du panier.",
    'rep': "Le cours admet le caractère fixe du panier tout en précisant "
           "qu’il est actualisé chaque année et appuyé sur un relevé de deux "
           "cent mille prix : la mesure est conventionnelle mais non "
           "arbitraire."},
   {'t': "Le pouvoir d’achat mesuré décrit mal la situation réelle des "
         "ménages, car une large part de leurs dépenses est contrainte.",
    'qui': "L’analyse des dépenses pré-engagées que le cours développe.",
    'rep': "Le cours donne raison à cette objection en la chiffrant : les "
           "dépenses pré-engagées représentent trente pour cent du revenu "
           "disponible et tendent à augmenter, ce qui réduit d’autant la "
           "marge arbitrable."},
   {'t': "Raisonner en pouvoir d’achat moyen masque les écarts : seule la "
         "distribution des revenus importe.",
    'qui': "L’argument issu de l’analyse de la pauvreté monétaire que le "
           "cours développe au même endroit.",
    'rep': "Le cours intègre cette critique en passant du revenu au niveau "
           "de vie par unité de consommation, puis au revenu médian et au "
           "seuil de pauvreté, qui situent chaque ménage dans la "
           "distribution."}],
  [{'n': "Arthur Pigou",
    'i': "En période d’inflation, les agents épargnent davantage pour "
         "conserver la valeur réelle de leur patrimoine.",
    'p': "Le cours nomme ce mécanisme effet d’encaisse réelle ou effet "
         "Pigou : les individus sont incités à épargner plus donc à réduire "
         "leurs dépenses, et le cours ajoute qu’en France ce comportement "
         "s’est révélé plus fréquent que la fuite devant la monnaie."},
   {'n': "Irving Fisher",
    'i': "La monnaie n’affecte que le niveau général des prix, ce qui impose "
         "de distinguer grandeurs nominales et réelles.",
    'p': "Le cours donne son équation reliant la quantité de monnaie et sa "
         "vitesse au niveau des prix et au volume des transactions : c’est "
         "cette distinction entre le nominal et le réel qui fonde le calcul "
         "du pouvoir d’achat par déflation du revenu."},
   {'n': "Alban William Phillips",
    'i': "La croissance des salaires nominaux dépend du niveau du chômage.",
    'p': "Le cours rapporte son observation de 1958 sur le Royaume-Uni entre "
         "1861 et 1957 : elle éclaire le pouvoir d’achat en montrant que la "
         "progression du revenu nominal n’est pas indépendante de la "
         "conjoncture du marché du travail."}],
  [{'f': "Le cours donne la formule : pouvoir d’achat du revenu égale revenu "
         "nominal divisé par l’indice des prix et multiplié par cent.",
    'p': "La formule montre que le pouvoir d’achat n’est pas une grandeur "
         "observée mais le résultat d’une déflation : il suppose toujours un "
         "indice de prix de référence."},
   {'f': "Avec un revenu nominal de mille et un indice de cent dix, le revenu "
         "réel est de neuf cent neuf.",
    'p': "Le calcul chiffré rend l’effet tangible : dix pour cent "
         "d’inflation retirent environ neuf pour cent du pouvoir d’achat, ce "
         "qui n’est pas symétrique de la hausse des prix."},
   {'f': "Si le salaire augmente de deux pour cent et les prix de trois pour "
         "cent, le pouvoir d’achat baisse.",
    'p': "L’exemple démontre que la grandeur est relative : une hausse "
         "nominale du revenu peut parfaitement coexister avec une perte "
         "réelle."},
   {'f': "Les dépenses pré-engagées, logement, chauffage et assurances, "
         "représentent trente pour cent du revenu disponible et tendent à "
         "augmenter.",
    'p': "Le chiffre montre que le pouvoir d’achat mesuré surestime la marge "
         "d’arbitrage réelle des ménages, ce qui explique une partie de "
         "l’écart avec l’inflation ressentie."}],
  [{'q': "Sujet sur l’inflation et le niveau de vie des ménages",
    'f': "L’inflation ne se juge pas seule mais par comparaison avec les "
         "revenus. Le cours définit le pouvoir d’achat comme la quantité de "
         "biens et de services qu’un revenu peut acquérir, et donne "
         "l’exemple décisif : si le salaire augmente de deux pour cent mais "
         "que les prix augmentent de trois pour cent, le pouvoir d’achat "
         "baisse. La perte réelle peut donc coexister avec une hausse "
         "nominale du revenu.",
    'r': "On montre que la grandeur pertinente est un écart entre deux taux "
         "de variation, ce qui interdit de conclure d’un seul des deux "
         "mouvements.",
    'ex': "Le calcul du cours : un revenu nominal de mille avec un indice de "
          "cent dix donne un revenu réel de neuf cent neuf."},
   {'q': "Sujet sur la mesure des grandeurs économiques",
    'f': "Le pouvoir d’achat est un cas particulier d’une opération "
         "générale. Le cours l’énonce ainsi : les grandeurs économiques, "
         "produit intérieur brut, consommation, investissement, revenu ou "
         "exportations, peuvent être exprimées en valeur courante, aux prix "
         "de l’année en cours, mais pour comparer dans le temps il faut "
         "enlever l’effet des prix et calculer en volume, à prix constants, "
         "en fixant une année de référence.",
    'r': "On montre que toute comparaison temporelle suppose une déflation, "
         "donc le choix d’un indice et d’une année de base, ce qui rend la "
         "mesure dépendante de conventions explicites.",
    'ex': "La distinction du cours entre produit intérieur brut en valeur, "
          "courant et nominal, et en volume, constant et réel."},
   {'q': "Sujet sur l’écart entre inflation mesurée et inflation ressentie",
    'f': "L’écart entre inflation mesurée et inflation ressentie a des "
         "causes identifiables dans le cours. D’un côté l’indice repose sur "
         "un panier fixe de biens et services actualisé chaque année, qui ne "
         "correspond à la consommation d’aucun ménage en particulier. De "
         "l’autre, les dépenses pré-engagées, logement, chauffage et "
         "assurances, représentent trente pour cent du revenu disponible et "
         "tendent à augmenter, ce qui concentre la perte sur la part "
         "arbitrable.",
    'r': "On montre que la moyenne statistique et l’expérience individuelle "
         "ne portent pas sur le même objet, ce qui explique un désaccord sans "
         "supposer d’erreur de mesure.",
    'ex': "La définition du cours de la consommation pré-engagée, dont il "
          "chiffre la part et note la progression."},
   {'q': "Sujet sur les effets de l’inflation sur la consommation",
    'f': "L’inflation n’a pas un effet univoque sur la dépense des ménages. "
         "Le cours oppose deux mécanismes : l’effet d’encaisse réelle, ou "
         "effet Pigou, pousse à épargner davantage pour conserver la valeur "
         "du patrimoine, donc à réduire les dépenses ; la fuite devant la "
         "monnaie pousse au contraire à acheter aujourd’hui avant que les "
         "effets de l’inflation prennent place. En France, l’effet "
         "d’encaisse réelle s’est révélé le plus fréquent.",
    'r': "On montre que l’effet dominant dépend du niveau anticipé de "
         "l’inflation, ce qui permet de trancher empiriquement plutôt que "
         "théoriquement.",
    'ex': "La vérification empirique française que le cours mentionne en "
          "faveur de l’effet d’encaisse réelle."}],
  voisins=['n14-inflation', 'n14-boucle-prix-salaires', 'n14-deflation',
           'n14-desinflation'])


d('n14-credibilite-monetaire', 14, "Crédibilité monétaire",
  "Une politique n’agit que si les agents y croient",
  "La crédibilité monétaire est la capacité d’une banque centrale à être crue "
  "lorsqu’elle annonce son objectif. Le cours en fait une condition "
  "d’efficacité et non un supplément : si les agents anticipent la règle "
  "suivie, seule une politique crédible modifie leurs comportements. Il "
  "l’aborde par trois voies, l’indépendance de la banque centrale, la "
  "préférence des monétaristes pour les règles, et la limite du financement "
  "monétaire des déficits.",
  "Le cours ne consacre pas de section autonome à la crédibilité, mais elle "
  "commande trois raisonnements distincts qu’il développe, et leur "
  "rapprochement en donne la notion complète. Première voie, "
  "l’indépendance. Le cours énonce ce qui arrive lorsqu’elle disparaît : la "
  "banque centrale devient un outil du gouvernement et elle n’est plus "
  "crédible pour lutter contre l’inflation. Il ajoute le mécanisme "
  "d’incitation qui en découle, l’aléa moral public : si l’État sait que la "
  "banque centrale peut financer ses dépenses, il n’a plus d’incitation à "
  "maîtriser le déficit ni à contrôler la dette, d’où un risque de dérive "
  "permanente et un risque inflationniste, puisque des dépenses financées par "
  "création monétaire sans contrepartie productive immédiate alimentent "
  "l’inflation à long terme. La crédibilité est donc d’abord une question "
  "institutionnelle : elle se construit en retirant à l’autorité monétaire la "
  "possibilité d’être instrumentalisée. Deuxième voie, les règles. Pour les "
  "monétaristes, la solution est de contrôler la croissance de la masse "
  "monétaire selon une règle de pourcentage constant, plutôt que de décider "
  "au coup par coup. La nouvelle économie classique radicalise l’argument : "
  "les politiques discrétionnaires créent de l’incertitude, perturbent les "
  "anticipations et accentuent l’instabilité économique, de sorte que la "
  "meilleure politique économique est l’absence de politique économique, et "
  "que seules sont acceptées des règles simples, crédibles et stables dans le "
  "temps. Avec Sargent, le fondement est explicite : les agents connaissent "
  "la règle suivie par les autorités et en intègrent les effets avant qu’ils "
  "ne se produisent, d’où la préférence pour les règles. Troisième voie, les "
  "instruments exceptionnels. Le cours range le problème de crédibilité à "
  "long terme de la monnaie parmi les fortes limites de l’hélicoptère "
  "monétaire, aux côtés du risque élevé d’inflation si la création monétaire "
  "est excessive, de la remise en cause de l’indépendance de la banque "
  "centrale et de la confusion entre politique monétaire et politique "
  "budgétaire, ce qui explique qu’il reste une solution exceptionnelle et "
  "surtout théorique. La crédibilité apparaît ainsi comme ce que la banque "
  "centrale risque de perdre chaque fois qu’elle élargit son action, et le "
  "cours signale d’ailleurs que la croissance dépend plus généralement de la "
  "crédibilité des règles.",
  [("L’annonce d’un objectif",
    "La banque centrale rend public son objectif, par exemple une inflation "
    "autour de deux pour cent à moyen terme dans la zone euro : la "
    "crédibilité porte sur cet engagement vérifiable."),
   ("L’anticipation de la règle par les agents",
    "Avec Sargent, les agents connaissent la règle suivie par les autorités "
    "et en intègrent les effets avant qu’ils ne se produisent : c’est la "
    "règle, et non la décision, qu’ils anticipent."),
   ("L’ajustement des comportements",
    "Si l’objectif est cru, les salariés et les entreprises fixent salaires "
    "et prix en conséquence : la désinflation s’obtient alors sans que la "
    "banque centrale ait à provoquer une contraction."),
   ("La protection par l’indépendance",
    "Sans indépendance, la banque centrale devient un outil du gouvernement "
    "et n’est plus crédible pour lutter contre l’inflation : l’autonomie est "
    "la garantie institutionnelle de l’engagement."),
   ("L’aléa moral public",
    "Si l’État sait que la banque centrale peut financer ses dépenses, il n’a "
    "plus d’incitation à maîtriser le déficit ni à contrôler la dette, d’où "
    "un risque de dérive permanente."),
   ("L’usure par les instruments exceptionnels",
    "Chaque élargissement de l’action monétaire pose un problème de "
    "crédibilité à long terme de la monnaie : le cours le range parmi les "
    "fortes limites de l’hélicoptère monétaire.")],
  [{'a': "La crédibilité réduit le coût de la désinflation, puisqu’une "
         "annonce crue modifie les comportements sans contraction préalable.",
    'cond': "L’argument suppose que les agents anticipent la règle, ce que le "
            "cours rattache aux anticipations rationnelles et à Sargent.",
    'lim': "Le cas Volcker montre l’inverse : la crédibilité a été acquise "
           "par un choc de taux assumé, donc par le coût payé plutôt que par "
           "l’annonce."},
   {'a': "Elle fonde l’indépendance de la banque centrale sur un argument "
         "d’efficacité économique et non sur un principe doctrinal.",
    'cond': "Le fondement suppose que l’absence d’indépendance détruise "
            "effectivement la crédibilité, ce que le cours affirme.",
    'lim': "Le cours rapporte la critique démocratique avec Éric Monnet, qui "
           "appelle à démocratiser les banques centrales et la monnaie : "
           "l’indépendance a un coût de légitimité."},
   {'a': "Elle justifie la préférence pour des règles simples, crédibles et "
         "stables dans le temps plutôt que pour la discrétion.",
    'cond': "La préférence suppose que les politiques discrétionnaires "
            "créent de l’incertitude et perturbent les anticipations, comme "
            "le soutient la nouvelle économie classique.",
    'lim': "Une règle rigide prive la banque centrale de réaction en cas de "
           "choc imprévu, ce que le cours illustre par la nécessité "
           "d’instruments non conventionnels après 2008."},
   {'a': "Elle explique pourquoi certains instruments restent théoriques "
         "malgré leur efficacité apparente.",
    'cond': "L’argument suppose que le coût en crédibilité l’emporte sur le "
            "gain d’activité attendu, ce que le cours affirme pour "
            "l’hélicoptère monétaire.",
    'lim': "Le cours relève que cet instrument est néanmoins utilisé dans "
           "les débats : la frontière entre exceptionnel et impossible n’est "
           "pas fixe."},
   {'a': "Elle relie la politique monétaire à l’analyse institutionnelle de la "
         "croissance, où la prévisibilité des règles conditionne "
         "l’investissement.",
    'cond': "Le rapprochement suppose que la crédibilité des règles soit un "
            "facteur de décision économique, ce que le cours affirme en "
            "écrivant que la croissance dépend de la crédibilité des règles.",
    'lim': "Le contexte y est différent : le cours parle alors de sécurité "
           "juridique et de protection de la propriété, non de politique "
           "monétaire."}],
  [{'t': "La banque centrale doit pouvoir financer l’État : un État souverain "
         "monétairement n’a pas de contrainte financière, le seul risque "
         "étant l’inflation.",
    'qui': "Stephanie Kelton, représentante de la théorie monétaire moderne "
           "que le cours présente.",
    'rep': "Le cours objecte par l’incitation : si l’État sait que la banque "
           "centrale peut financer ses dépenses, il n’a plus d’incitation à "
           "maîtriser le déficit, d’où un aléa moral public et un risque de "
           "dérive permanente."},
   {'t': "L’indépendance de la banque centrale est un déficit démocratique : "
         "la monnaie est un bien commun qui doit être soumis au débat public.",
    'qui': "Éric Monnet, dans La Banque Providence, que le cours cite en "
           "2021.",
    'rep': "Le cours tient les deux bouts : il rapporte l’appel à "
           "démocratiser les banques centrales et la monnaie tout en "
           "maintenant qu’une banque centrale soumise au gouvernement n’est "
           "plus crédible pour lutter contre l’inflation."},
   {'t': "La crédibilité ne se décrète pas par une règle : elle s’acquiert "
         "par les actes, donc par le coût accepté.",
    'qui': "La lecture que suggère le cas Volcker, tel que le cours le "
           "présente.",
    'rep': "Le cours ne tranche pas mais fournit les deux voies : la règle "
           "de pourcentage constant proposée par Friedman et le choc de taux "
           "effectivement conduit en 1979."},
   {'t': "Une règle stricte est dangereuse : elle empêche la banque centrale "
         "d’agir en cas de crise financière.",
    'qui': "L’argument issu de l’élargissement des missions de la banque "
           "centrale que le cours décrit depuis 2008.",
    'rep': "Le cours donne raison à l’objection en pratique : la banque "
           "centrale doit éviter les crises bancaires, les paniques de "
           "liquidité et le blocage du crédit, ce qu’une règle quantitative "
           "simple ne permet pas."}],
  [{'n': "Milton Friedman",
    'i': "Il faut contrôler la croissance de la masse monétaire selon une "
         "règle de pourcentage constant.",
    'p': "Le cours présente cette règle comme sa solution, aux côtés du "
         "laisser-faire et du retour du chômage à son niveau naturel : "
         "puisque la monnaie détermine l’inflation à long terme, une règle "
         "prévisible vaut mieux qu’une décision discrétionnaire."},
   {'n': "Thomas Sargent",
    'i': "Les agents connaissent la règle suivie par les autorités et en "
         "intègrent les effets avant qu’ils ne se produisent.",
    'p': "Le cours en tire la conséquence décisive pour la crédibilité : une "
         "politique annoncée n’agit que sur les variables nominales, d’où la "
         "préférence pour des règles plutôt que pour la discrétion, puisque "
         "seule une règle peut être connue à l’avance."},
   {'n': "Éric Monnet",
    'i': "Il faut démocratiser les banques centrales et la monnaie, donc "
         "soumettre leur mandat au débat public.",
    'p': "Le cours cite La Banque Providence, publiée en 2021, parmi les "
         "analyses qui soulignent depuis les années 2020 un élargissement des "
         "missions des banques centrales : la crédibilité ne se réduit alors "
         "plus à la lutte contre l’inflation mais engage la légitimité de "
         "l’institution."},
   {'n': "Stephanie Kelton",
    'i': "Un État souverain monétairement peut financer sa dette sans "
         "contrainte financière, le seul risque étant l’inflation.",
    'p': "Le cours la présente comme représentante de la théorie monétaire "
         "moderne et précise qu’elle conteste l’idée que la dette publique "
         "soit un problème en soi : sa position déplace donc la question de "
         "la solvabilité vers celle de la crédibilité anti-inflationniste."}],
  [{'f': "Le cours énonce que sans indépendance la banque centrale devient un "
         "outil du gouvernement et n’est plus crédible pour lutter contre "
         "l’inflation.",
    'p': "Le fait montre que la crédibilité est pensée comme une propriété "
         "institutionnelle avant d’être une propriété de communication."},
   {'f': "Le cours nomme aléa moral public le fait qu’un État cesse de "
         "maîtriser son déficit s’il sait que la banque centrale peut "
         "financer ses dépenses.",
    'p': "Le fait identifie le mécanisme d’incitation qui mine la "
         "crédibilité : le problème n’est pas une faute mais une logique de "
         "comportement prévisible."},
   {'f': "Le cours range le problème de crédibilité à long terme de la "
         "monnaie parmi les fortes limites de l’hélicoptère monétaire.",
    'p': "Le fait montre que la crédibilité fonctionne comme un budget "
         "limité : chaque instrument exceptionnel en consomme une part, ce "
         "qui explique que celui-ci reste surtout théorique."},
   {'f': "Pour la nouvelle économie classique, seules sont acceptées des "
         "règles simples, crédibles et stables dans le temps.",
    'p': "Le fait montre la conséquence institutionnelle de l’hypothèse "
         "d’anticipations rationnelles : la crédibilité se construit par la "
         "prévisibilité plutôt que par la fermeté ponctuelle."}],
  [{'q': "Sujet sur l’indépendance des banques centrales",
    'f': "L’indépendance se justifie par la crédibilité avant de se "
         "justifier par la doctrine. Le cours énonce ce qui se produit en son "
         "absence : la banque centrale devient un outil du gouvernement et "
         "elle n’est plus crédible pour lutter contre l’inflation. Il ajoute "
         "l’aléa moral public : si l’État sait que la banque centrale peut "
         "financer ses dépenses, il n’a plus d’incitation à maîtriser le "
         "déficit ni à contrôler la dette.",
    'r': "On montre que l’argument porte sur les incitations et non sur la "
         "compétence des autorités, ce qui le rend indépendant du jugement "
         "porté sur tel ou tel gouvernement.",
    'ex': "Le risque de dérive permanente et le risque inflationniste que le "
          "cours associe au financement monétaire des dépenses publiques."},
   {'q': "Sujet sur règles et discrétion en politique monétaire",
    'f': "La crédibilité est l’argument central en faveur des règles. Avec "
         "Sargent, les agents connaissent la règle suivie par les autorités "
         "et en intègrent les effets avant qu’ils ne se produisent, de sorte "
         "qu’une politique annoncée n’agit que sur les variables nominales. "
         "La nouvelle économie classique en déduit que les politiques "
         "discrétionnaires créent de l’incertitude et que seules sont "
         "acceptées des règles simples, crédibles et stables dans le temps.",
    'r': "On montre que l’avantage d’une règle tient à sa prévisibilité et "
         "non à son contenu, ce qui explique que l’argument traverse les "
         "courants.",
    'ex': "La règle de contrôle de la croissance de la masse monétaire à "
          "pourcentage constant que Friedman propose."},
   {'q': "Sujet sur les limites des instruments monétaires exceptionnels",
    'f': "Un instrument peut être efficace et pourtant inemployable. Le cours "
         "le montre pour l’hélicoptère monétaire, dont il énumère les fortes "
         "limites : risque élevé d’inflation si la création monétaire est "
         "excessive, remise en cause de l’indépendance de la banque "
         "centrale, confusion entre politique monétaire et politique "
         "budgétaire, problème de crédibilité à long terme de la monnaie. "
         "C’est pourquoi il reste une solution exceptionnelle, surtout "
         "théorique.",
    'r': "On montre que le coût pertinent n’est pas celui de l’opération "
         "mais celui de l’engagement rompu, ce qui place la crédibilité au "
         "rang de ressource rare.",
    'ex': "La conclusion du cours selon laquelle l’hélicoptère monétaire est "
          "utilisé dans les débats mais très rarement en pratique."},
   {'q': "Sujet sur la dette publique et la contrainte monétaire",
    'f': "Le débat sur la dette publique est aussi un débat sur la "
         "crédibilité. Stephanie Kelton soutient qu’un État souverain "
         "monétairement peut financer sa dette sans contrainte financière et "
         "que le seul risque est l’inflation. Le cours ne nie pas la "
         "possibilité technique mais objecte par l’incitation : l’aléa moral "
         "public fait que l’État cesse de maîtriser son déficit dès qu’il "
         "sait pouvoir compter sur la banque centrale.",
    'r': "On distingue la capacité technique à financer et la soutenabilité "
         "des incitations, pour montrer que la contrainte est "
         "institutionnelle plutôt que financière.",
    'ex': "L’aléa moral public tel que le cours le nomme parmi les risques "
          "de la perte d’indépendance de la banque centrale."}],
  voisins=['n14-ancrage-anticipations', 'n14-anticipations-inflation',
           'n14-desinflation', 'n11-independance-bc'])


d('n14-ancrage-anticipations', 14, "Ancrage des anticipations",
  "Faire de la croyance des agents un instrument de politique monétaire",
  "Ancrer les anticipations d’inflation consiste, pour une banque centrale, à "
  "faire en sorte que les agents attendent durablement une inflation conforme "
  "à sa cible. Le cours en fait un objectif explicite du canal des "
  "anticipations, ou forward guidance : la banque centrale annonce "
  "l’orientation future probable des taux et sa stratégie pour rassurer les "
  "marchés, réduire l’incertitude, encourager l’investissement et ancrer les "
  "anticipations d’inflation.",
  "Le cours introduit l’ancrage des anticipations parmi les canaux de "
  "transmission de la politique monétaire, et cette place marque un "
  "renversement théorique qu’il faut mesurer. Jusque-là, les anticipations "
  "étaient dans le cours un obstacle : chez Friedman, les agents forment des "
  "anticipations adaptatives, apprennent de l’inflation passée et adaptent "
  "leurs comportements, de sorte que la politique monétaire marche au début "
  "puis cesse d’agir sur la production ; chez les tenants des anticipations "
  "rationnelles, les agents connaissent la règle suivie et en intègrent les "
  "effets avant qu’ils ne se produisent, si bien qu’une politique annoncée "
  "n’agit que sur les variables nominales. Dans les deux cas, l’anticipation "
  "neutralise l’action. Le canal des anticipations renverse ce rapport : "
  "puisque les agents anticipent, la banque centrale va précisément agir sur "
  "ce qu’ils anticipent. Le cours en donne le principe : la banque centrale "
  "agit aussi par sa communication, elle annonce l’orientation future "
  "probable des taux, sa stratégie, sa volonté de soutenir l’activité ou de "
  "combattre l’inflation, par exemple en annonçant une baisse des taux. Et il "
  "en donne les effets recherchés : modifier les anticipations des agents, "
  "rassurer les marchés, réduire l’incertitude, encourager l’investissement, "
  "ancrer les anticipations d’inflation. La conclusion du cours est "
  "catégorique : les anticipations deviennent un outil monétaire à part "
  "entière. L’ancrage suppose deux conditions que le cours fournit "
  "ailleurs. La première est une cible publique et stable : la Banque "
  "centrale européenne vise une inflation autour de deux pour cent à moyen "
  "terme, ce qui donne aux anticipations un point fixe auquel se rattacher. "
  "La seconde est la crédibilité, puisqu’une annonce n’ancre que si elle est "
  "crue : le cours rappelle qu’une banque centrale devenue outil du "
  "gouvernement n’est plus crédible pour lutter contre l’inflation, et que "
  "les politiques discrétionnaires perturbent les anticipations. L’ancrage "
  "est enfin ce qui rend la politique monétaire encore opérante lorsque les "
  "instruments ordinaires sont bloqués : en situation de trappe à liquidité, "
  "les taux ne peuvent guère baisser davantage, et la banque centrale "
  "intervient alors sur les bilans, les titres et les anticipations.",
  [("La fixation d’un point de référence",
    "La banque centrale rend publique une cible chiffrée, une inflation "
    "autour de deux pour cent à moyen terme dans la zone euro : les agents "
    "disposent d’un repère stable auquel rattacher leurs prévisions."),
   ("La communication sur l’avenir",
    "Elle annonce l’orientation future probable des taux, sa stratégie et sa "
    "volonté de soutenir l’activité ou de combattre l’inflation : le cours "
    "nomme ce canal forward guidance."),
   ("La réduction de l’incertitude",
    "Les effets recherchés sont de rassurer les marchés et de réduire "
    "l’incertitude : les agents n’ont plus à deviner la réaction des "
    "autorités, ce qui stabilise leurs décisions."),
   ("L’alignement des comportements",
    "Les salaires, les prix et les décisions d’investissement se fixent en "
    "fonction de l’inflation attendue : si celle-ci est conforme à la cible, "
    "elle se réalise d’elle-même."),
   ("Le soutien à l’investissement",
    "Le cours range encourager l’investissement parmi les effets "
    "recherchés : la visibilité sur les taux futurs réduit le risque attaché "
    "aux projets longs."),
   ("Le recours en situation bloquée",
    "Lorsque les taux ne peuvent guère baisser davantage, la banque centrale "
    "intervient sur les bilans, les titres et les anticipations : l’ancrage "
    "devient le levier restant.")],
  [{'a': "L’ancrage transforme un obstacle théorique en instrument, puisque "
         "l’anticipation des agents devient le canal de l’action.",
    'cond': "Le renversement suppose que les agents forment effectivement "
            "leurs prévisions à partir des annonces officielles et non du "
            "seul passé.",
    'lim': "Avec des anticipations purement adaptatives, les agents "
           "extrapolent l’inflation passée : l’annonce n’a alors de prise "
           "qu’une fois les faits conformes."},
   {'a': "Il fournit un instrument sans coût budgétaire et sans mouvement de "
         "taux, donc utilisable lorsque les autres sont bloqués.",
    'cond': "L’efficacité suppose une crédibilité préalablement acquise, le "
            "cours rappelant qu’une banque centrale non indépendante n’est "
            "plus crédible.",
    'lim': "L’instrument s’épuise s’il est démenti : une annonce non suivie "
           "d’effet détruit la ressource même qu’elle mobilisait."},
   {'a': "Il justifie la publication d’une cible chiffrée plutôt qu’un "
         "objectif implicite de stabilité des prix.",
    'cond': "La cible n’ancre que si elle est stable et atteinte en moyenne, "
            "ce que la formulation à moyen terme ménage.",
    'lim': "Une cible publique devient un engagement mesurable : s’en "
           "écarter longuement désancre les anticipations qu’elle devait "
           "fixer."},
   {'a': "Il explique pourquoi une inflation modérée et prévisible est "
         "préférable à une inflation nulle mais incertaine.",
    'cond': "L’argument suppose que les agents valorisent la prévisibilité "
            "dans leurs décisions de salaire, de prix et d’investissement.",
    'lim': "Le cours montre que la prévisibilité ne protège pas d’un choc "
           "d’offre : la stagflation a déplacé l’inflation sans qu’aucune "
           "communication ne puisse l’empêcher."},
   {'a': "Il relie la politique monétaire à l’analyse des croyances "
         "collectives, en faisant de l’anticipation partagée un fait "
         "économique.",
    'cond': "Le rapprochement suppose, comme chez Merton, que les "
            "représentations collectives influencent directement la "
            "réalité.",
    'lim': "Ce même mécanisme joue en sens inverse : une anticipation "
           "d’inflation partagée peut se réaliser contre la cible, ce qui "
           "rend l’ancrage fragile autant qu’utile."}],
  [{'t': "Les anticipations sont subies : une banque centrale ne peut pas en "
         "faire un instrument, puisque les agents anticipent déjà sa règle.",
    'qui': "La position des anticipations rationnelles que le cours rattache "
           "à Sargent et à la nouvelle économie classique.",
    'rep': "Le cours répond que c’est précisément parce que les agents "
           "anticipent la règle que l’annonce de la règle devient agissante : "
           "il range ancrer les anticipations d’inflation parmi les effets "
           "recherchés du canal des anticipations."},
   {'t': "Seuls les actes comptent : une annonce sans mouvement de taux est "
         "une parole sans effet.",
    'qui': "L’objection que suggère le cas Volcker, où la crédibilité est "
           "acquise par un choc de taux.",
    'rep': "Le cours tient les deux : il décrit la communication comme un "
           "canal à part entière, tout en montrant par l’exemple de 1979 que "
           "la crédibilité qui la rend efficace peut avoir été acquise par "
           "l’action."},
   {'t': "La communication accroît l’instabilité : elle multiplie les "
         "signaux et perturbe les anticipations.",
    'qui': "L’argument de la nouvelle économie classique contre les "
           "politiques discrétionnaires, tel que le cours le présente.",
    'rep': "Le cours distingue les deux cas : ce sont les politiques "
           "discrétionnaires qui perturbent les anticipations, alors que le "
           "forward guidance vise au contraire à réduire l’incertitude en "
           "annonçant une orientation."},
   {'t': "L’ancrage est une illusion lorsque les prix dépendent de "
         "l’extérieur : aucune annonce ne contient une inflation importée.",
    'qui': "L’analyse du cercle vicieux des monnaies faibles que le cours "
           "développe.",
    'rep': "Le cours accorde cette limite mais fournit un canal : la "
           "politique monétaire agit aussi par le taux de change, puisque si "
           "les taux montent les capitaux étrangers sont attirés et la "
           "monnaie s’apprécie."}],
  [{'n': "Thomas Sargent",
    'i': "Les agents connaissent la règle suivie par les autorités et en "
         "intègrent les effets avant qu’ils ne se produisent.",
    'p': "Le cours en tire qu’une politique annoncée n’agit que sur les "
         "variables nominales, d’où la préférence pour les règles : c’est "
         "cette hypothèse qui rend l’ancrage possible, puisqu’elle suppose "
         "des agents attentifs aux engagements des autorités."},
   {'n': "Milton Friedman",
    'i': "Les agents apprennent de l’inflation passée et adaptent leurs "
         "comportements en conséquence.",
    'p': "Le cours en donne l’exemple, les salariés demandant des hausses de "
         "salaires et les entreprises augmentant leurs prix : dans cette "
         "version adaptative, l’ancrage par la seule annonce est plus "
         "difficile, puisque ce sont les faits passés qui guident les "
         "prévisions."},
   {'n': "Robert Merton",
    'i': "Les représentations collectives influencent directement la "
         "réalité économique.",
    'p': "Le cours en fait un concept clé en économie, avec pour exemples la "
         "panique bancaire et la bulle spéculative : appliqué aux prix, le "
         "caractère autoréalisateur des croyances explique pourquoi une "
         "anticipation ancrée sur la cible tend à la réaliser."}],
  [{'f': "Le cours range ancrer les anticipations d’inflation parmi les "
         "effets recherchés du canal des anticipations, aussi nommé forward "
         "guidance.",
    'p': "Le fait montre que l’ancrage est un objectif explicite de "
         "politique monétaire, et non une conséquence espérée d’autres "
         "actions."},
   {'f': "Le cours conclut que les anticipations deviennent un outil "
         "monétaire à part entière.",
    'p': "La formule mesure le renversement accompli : la variable qui "
         "neutralisait la politique monétaire dans l’analyse monétariste en "
         "est devenue un instrument."},
   {'f': "La Banque centrale européenne vise une inflation autour de deux "
         "pour cent à moyen terme.",
    'p': "La cible fournit le point fixe sans lequel l’ancrage n’a pas "
         "d’objet : les agents ont besoin d’un repère chiffré et public pour "
         "y rattacher leurs prévisions."},
   {'f': "Le cours décrit les politiques non conventionnelles comme "
         "intervenant sur les bilans, les titres et les anticipations.",
    'p': "L’énumération place les anticipations au même rang que les bilans "
         "et les titres : elles constituent l’un des trois terrains d’action "
         "lorsque les taux ne suffisent plus."}],
  [{'q': "Sujet sur la communication des banques centrales",
    'f': "La parole de la banque centrale est devenue un instrument au même "
         "titre que ses taux. Le cours décrit le canal des anticipations : la "
         "banque centrale agit aussi par sa communication, elle annonce "
         "l’orientation future probable des taux, sa stratégie et sa volonté "
         "de soutenir l’activité ou de combattre l’inflation, afin de "
         "rassurer les marchés, réduire l’incertitude, encourager "
         "l’investissement et ancrer les anticipations d’inflation.",
    'r': "On montre que ce canal agit sans mouvement de taux, ce qui en fait "
         "un instrument décisif quand les taux sont déjà au plus bas.",
    'ex': "La conclusion du cours : les anticipations deviennent un outil "
          "monétaire à part entière."},
   {'q': "Sujet sur le rôle des anticipations en macroéconomie",
    'f': "Les anticipations sont passées du statut d’obstacle à celui "
         "d’instrument. Chez Friedman, les anticipations adaptatives "
         "neutralisent la politique monétaire, puisque les agents apprennent "
         "de l’inflation passée et adaptent leurs comportements. Avec le "
         "canal des anticipations, la banque centrale agit précisément sur ce "
         "que les agents anticipent, ce qui retourne l’argument en sa "
         "faveur.",
    'r': "On montre que le même mécanisme peut neutraliser ou servir "
         "l’action publique selon qu’il est subi ou mobilisé, ce qui invite à "
         "lire l’histoire de la politique monétaire comme une adaptation à "
         "ses propres critiques.",
    'ex': "La formule du cours selon laquelle la politique monétaire marche "
          "au début, mais ensuite les gens s’adaptent."},
   {'q': "Sujet sur les cibles d’inflation",
    'f': "Une cible publique est la condition de l’ancrage. Le cours donne "
         "le repère de la zone euro, une inflation autour de deux pour cent à "
         "moyen terme, et place l’ancrage des anticipations d’inflation parmi "
         "les effets recherchés de la communication officielle. La cible "
         "fournit aux agents un point fixe : sans elle, l’annonce "
         "d’orientation n’aurait pas de référence à laquelle rattacher les "
         "prévisions.",
    'r': "On montre que la cible agit moins comme une contrainte technique "
         "que comme un repère collectif, ce qui explique le soin apporté à sa "
         "formulation à moyen terme.",
    'ex': "La définition du rôle de la Banque centrale européenne dans le "
          "cours : la stabilité des prix comme objectif principal."},
   {'q': "Sujet sur la politique monétaire en situation de taux bas",
    'f': "Quand les taux ne peuvent plus baisser, il reste les "
         "anticipations. Le cours décrit la trappe à liquidité, où les agents "
         "préfèrent conserver des liquidités, les banques restent prudentes "
         "et l’investissement ne repart pas suffisamment, puis le passage à "
         "des instruments qui interviennent non plus seulement sur le prix de "
         "la monnaie mais sur les bilans, les titres et les anticipations.",
    'r': "On montre que la contrainte du plancher des taux déplace l’action "
         "vers des canaux indirects, ce qui explique l’importance prise par "
         "la communication depuis 2008.",
    'ex': "Le forward guidance tel que le cours le décrit, par lequel la "
          "banque centrale annonce par exemple une baisse des taux."}],
  voisins=['n14-credibilite-monetaire', 'n14-anticipations-inflation',
           'n14-inflation', 'n11-banque-centrale'])
