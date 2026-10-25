# -*- coding: utf-8 -*-
"""Ensemble 20 — Les changes et les déséquilibres internationaux (3/4)."""

from doss_base import d

d('n20-taux-change-nominal-reel', 20, "Taux de change nominal et réel",
  "Le cours travaille le cours nominal ; la dimension réelle n’apparaît qu’à travers la parité de pouvoir d’achat",
  "Le taux de change est le prix d’une monnaie exprimé en une autre : le "
  "cours d’une monnaie est un prix, par exemple 1 euro égale 1,10 dollar. Le "
  "cours travaille ce taux nominal — sa formation, ses régimes, ses "
  "variations — et il n’introduit pas d’indice de taux de change réel ; la "
  "dimension réelle n’apparaît que par la parité de pouvoir d’achat, qui "
  "corrige les biais des taux de change de marché.",
  "Il faut être précis sur ce que le cours contient et ce qu’il ne contient "
  "pas : il développe longuement le taux de change nominal mais ne construit "
  "pas d’indice de taux de change réel. Le taux de change nominal y est "
  "défini comme un prix : le cours d’une monnaie est un prix, et si 1 euro "
  "égale 1,10 dollar puis passe à 1 euro égale 1,17 dollar, l’euro s’est "
  "apprécié et le dollar s’est déprécié. Sa formation dépend du régime "
  "retenu. En régime de change fixe, le taux de change d’une monnaie est "
  "fixé par l’État ou la banque centrale par rapport à une autre monnaie, "
  "une monnaie locale valant par exemple un euro sans que cela ne bouge. En "
  "régime de change flottant, la valeur de la monnaie varie librement selon "
  "l’offre et la demande sur le marché des changes, le marché déterminant le "
  "taux selon la confiance, les taux d’intérêt et la croissance ; "
  "l’avantage est une grande flexibilité, la banque centrale pouvant mener "
  "une politique monétaire indépendante, l’inconvénient de fortes "
  "fluctuations qui créent de l’incertitude pour les entreprises et pour les "
  "échanges. Le cours décrit aussi les déterminants concrets du cours "
  "nominal : les mouvements internationaux de capitaux ont une dimension "
  "monétaire parce qu’ils impliquent des conversions de devises et "
  "influencent donc l’offre, la demande et le taux de change, un seul achat "
  "ayant peu d’effet mais de nombreux achats d’actifs américains élevant la "
  "demande de dollars et donc exerçant une pression à l’appréciation ; et "
  "symétriquement un déficit commercial important accroît l’offre de monnaie "
  "nationale, puisque les résidents vendent leur monnaie pour acheter des "
  "devises afin de payer les importations, ce qui déprécie cette monnaie. Il "
  "en tire la notion de risque de change, situation où un ou des acteurs "
  "économiques peuvent être affectés par une variation du taux de change : "
  "si un individu échange des francs contre des Deutschmark et que la "
  "monnaie est ensuite dévaluée, il perd de l’argent, ce qui peut dissuader "
  "et limiter les échanges. Quant à la dimension réelle, le cours ne "
  "l’aborde que par la parité de pouvoir d’achat, et de façon très "
  "explicite : un simple taux de change de marché ne reflète pas "
  "correctement le niveau de vie réel, parce qu’il dépend de la "
  "spéculation, des marchés financiers, des mouvements de capitaux, des "
  "anticipations et des déséquilibres monétaires, et il ne traduit pas "
  "nécessairement ce qu’un revenu permet réellement d’acheter dans chaque "
  "pays.",
  [("La définition du taux comme prix d’une monnaie",
    "Le cours d’une monnaie est un prix : 1 euro égale 1,10 dollar puis "
    "1,17 dollar. Toute variation de ce prix modifie simultanément la valeur "
    "relative des deux monnaies."),
   ("La formation du taux en régime flottant",
    "La valeur de la monnaie varie librement selon l’offre et la demande sur "
    "le marché des changes, le marché déterminant le taux selon la "
    "confiance, les taux d’intérêt et la croissance."),
   ("La fixation administrée en régime fixe",
    "Le taux de change est fixé par l’État ou la banque centrale par rapport "
    "à une autre monnaie, une monnaie locale valant par exemple un euro sans "
    "que cela ne bouge : le prix cesse alors d’être déterminé par le "
    "marché."),
   ("L’influence des mouvements de capitaux",
    "Les mouvements internationaux de capitaux impliquent des conversions de "
    "devises : si de nombreux investisseurs achètent des actifs américains, "
    "la demande de dollars augmente et exerce une pression à l’appréciation."),
   ("L’influence du solde commercial",
    "Un déficit commercial important accroît l’offre de monnaie nationale, "
    "puisque les résidents vendent leur monnaie pour acheter des devises "
    "afin de payer leurs importations, ce qui tend à déprécier cette "
    "monnaie."),
   ("L’apparition du risque de change",
    "Le risque de change correspond à la situation où un ou des acteurs "
    "économiques peuvent être affectés par une variation du taux de change, "
    "ce qui peut dissuader et limiter les échanges."),
   ("Le passage obligé par la parité de pouvoir d’achat",
    "Un simple taux de change de marché ne reflète pas correctement le "
    "niveau de vie réel, parce qu’il dépend de la spéculation, des marchés "
    "financiers, des mouvements de capitaux, des anticipations et des "
    "déséquilibres monétaires.")],
  [{'a': "La définition du taux comme prix permet de lire immédiatement "
         "toute variation comme une appréciation ou une dépréciation "
         "relative.",
    'cond': "La lecture suppose l’exemple du cours : le passage de 1 euro "
            "égale 1,10 dollar à 1 euro égale 1,17 dollar signifie que "
            "l’euro s’apprécie et que le dollar se déprécie.",
    'lim': "Un taux bilatéral ne dit rien de la position d’ensemble d’une "
           "monnaie : le cours ne construit pas de taux de change effectif."},
   {'a': "Le cours relie le taux de change aux deux grandes catégories de "
         "flux, commerciaux et financiers.",
    'cond': "L’argument suppose les deux mécanismes exposés : les "
            "conversions de devises liées aux mouvements de capitaux et les "
            "achats de devises destinés à payer les importations.",
    'lim': "Le cours ne hiérarchise pas ces deux canaux et n’indique pas "
           "lequel domine dans la détermination du cours à court terme."},
   {'a': "Il fait apparaître le risque de change comme un coût réel pour les "
         "échanges, et non comme une simple incertitude comptable.",
    'cond': "L’argument suppose l’exemple du cours : un individu qui change "
            "des francs contre des Deutschmark perd de l’argent si la "
            "monnaie est ensuite dévaluée.",
    'lim': "Le cours n’examine pas les instruments de couverture, de sorte "
           "que le coût du risque n’est pas chiffré."},
   {'a': "Il traite explicitement l’insuffisance du taux de marché pour "
         "comparer les niveaux de vie.",
    'cond': "L’argument suppose la justification de la parité de pouvoir "
            "d’achat : le taux de marché dépend de la spéculation, des "
            "marchés financiers, des mouvements de capitaux, des "
            "anticipations et des déséquilibres monétaires.",
    'lim': "Le cours s’arrête à la conversion statistique : il ne construit "
           "pas d’indice de taux de change réel qui corrigerait le cours "
           "nominal par les prix relatifs."},
   {'a': "Il articule le régime de change retenu aux marges de manœuvre de la politique monétaire nationale.",
    'cond': "L’articulation suppose l’avantage du flottement relevé par le "
            "cours : la banque centrale peut mener une politique monétaire "
            "indépendante.",
    'lim': "L’avantage se paie en instabilité : le cours souligne que le "
           "taux peut fortement fluctuer, ce qui crée de l’incertitude pour "
           "les entreprises et pour les échanges."}],
  [{'t': "Le taux de change de marché mesure correctement la valeur "
         "relative du revenu entre deux pays.",
    'qui': "La lecture que la justification de la parité de pouvoir d’achat "
           "réfute.",
    'rep': "Le cours objecte qu’un simple taux de change de marché ne "
           "reflète pas correctement le niveau de vie réel, parce qu’il "
           "dépend de la spéculation, des marchés financiers, des mouvements "
           "de capitaux, des anticipations et des déséquilibres monétaires, "
           "et ne traduit pas ce qu’un revenu permet réellement d’acheter."},
   {'t': "Le taux de change est déterminé par les seuls échanges de biens et de services entre les pays.",
    'qui': "La lecture que le cours complète par la dimension financière.",
    'rep': "Le cours souligne que les mouvements internationaux de capitaux "
           "ont une dimension monétaire parce qu’ils impliquent des "
           "conversions de devises et influencent donc l’offre, la demande "
           "et le taux de change des monnaies, la pression pouvant venir des "
           "achats d’actifs autant que des importations."},
   {'t': "Une variation du taux de change est une simple écriture "
         "comptable, sans effet réel sur les agents.",
    'qui': "La lecture que la notion de risque de change contredit.",
    'rep': "Le cours objecte que le risque de change correspond à la "
           "situation où un ou des acteurs économiques peuvent être affectés "
           "par une variation du taux : un individu qui change des francs "
           "contre des Deutschmark perd de l’argent si la monnaie est "
           "ensuite dévaluée, ce qui peut dissuader les échanges."},
   {'t': "Puisque le flottement laisse le marché déterminer le taux, il est "
         "toujours préférable à un régime fixe.",
    'qui': "La lecture que la comparaison des régimes du cours nuance.",
    'rep': "Le cours reconnaît l’avantage du flottement, une grande "
           "flexibilité permettant à la banque centrale de mener une "
           "politique monétaire indépendante, mais il en relève "
           "l’inconvénient : le taux peut fortement fluctuer, ce qui crée de "
           "l’incertitude pour les entreprises et pour les échanges."}],
  [{'n': "Robert Mundell",
    'i': "Trois objectifs sont souhaitables mais ne peuvent être atteints "
         "simultanément : libre circulation des capitaux, stabilité du "
         "change, autonomie monétaire.",
    'p': "Le cours situe le triangle dans les années 1960 et en détaille les "
         "combinaisons : avec politique monétaire indépendante et liberté "
         "des capitaux, le taux de change ne peut être stabilisé ; avec "
         "stabilité du change et liberté des capitaux, il faut renoncer à "
         "l’autonomie monétaire."},
   {'n': "Henri Bourguinat",
    'i': "La globalisation financière repose sur les trois D : "
         "décloisonnement, déréglementation, désintermédiation.",
    'p': "Le cours situe cette analyse en 1987 et en tire la raison pour "
         "laquelle les mouvements de capitaux déterminent largement le cours "
         "des monnaies : les conversions de devises associées à ces flux "
         "influencent l’offre, la demande et donc le taux de change."},
   {'n': "Jean Bodin",
    'i': "L’afflux de métaux précieux explique la hausse des prix, la "
         "quantité de monnaie agissant sur leur niveau.",
    'p': "Le cours mobilise cette intuition dans l’analyse de la valeur de "
         "la monnaie : le pouvoir d’achat d’une unité monétaire dépend de sa "
         "quantité relativement aux biens disponibles, ce qui fonde la "
         "distinction entre le cours nominal d’une monnaie et ce qu’elle "
         "permet réellement d’acheter."},
   {'n': "Irving Fisher",
    'i': "La quantité de monnaie et sa vitesse de circulation se rapportent "
         "au niveau des prix et au volume des transactions.",
    'p': "Le cours mobilise cette équation dans l’analyse de la valeur "
         "interne de la monnaie, ce qui éclaire par contraste la limite du "
         "taux de change nominal : deux monnaies peuvent s’échanger à un "
         "cours donné tout en ayant des pouvoirs d’achat domestiques très "
         "différents."}],
  [{'f': "Le cours d’une monnaie est un prix : si 1 euro égale 1,10 dollar "
         "puis passe à 1 euro égale 1,17 dollar, l’euro s’est apprécié et le "
         "dollar s’est déprécié.",
    'p': "L’exemple chiffré fixe la lecture du taux nominal et montre la "
         "symétrie de toute variation entre les deux monnaies concernées."},
   {'f': "En régime de change fixe, le taux de change d’une monnaie est fixé "
         "par l’État ou la banque centrale par rapport à une autre monnaie, "
         "une monnaie locale valant par exemple un euro sans que cela ne "
         "bouge.",
    'p': "Le fait montre que le taux nominal n’est pas nécessairement un "
         "prix de marché : il peut être une décision publique."},
   {'f': "En régime flottant, le marché détermine le taux selon la "
         "confiance, les taux d’intérêt et la croissance ; l’avantage est "
         "une grande flexibilité permettant une politique monétaire "
         "indépendante, l’inconvénient de fortes fluctuations créant de "
         "l’incertitude.",
    'p': "Le fait établit l’arbitrage entre autonomie monétaire et "
         "stabilité du change, qui prépare le triangle d’incompatibilité."},
   {'f': "Si de nombreux investisseurs achètent des actifs américains, la "
         "demande de dollars augmente et exerce une pression à "
         "l’appréciation du dollar, un seul achat ayant en revanche peu "
         "d’effet.",
    'p': "Le fait montre que le taux nominal est déterminé par des flux "
         "agrégés et non par des transactions individuelles."},
   {'f': "Le risque de change correspond à la situation où un ou des acteurs "
         "économiques peuvent être affectés par une variation du taux de "
         "change : un individu qui échange des francs contre des Deutschmark "
         "perd de l’argent si la monnaie est ensuite dévaluée.",
    'p': "Le fait montre que l’instabilité nominale a un coût réel, "
         "susceptible de dissuader et de limiter les échanges."},
   {'f': "Un simple taux de change de marché ne reflète pas correctement le "
         "niveau de vie réel, parce qu’il dépend de la spéculation, des "
         "marchés financiers, des mouvements de capitaux, des anticipations "
         "et des déséquilibres monétaires.",
    'p': "Le fait établit la seule voie par laquelle le cours aborde la "
         "dimension réelle du change, celle de la parité de pouvoir d’achat."}],
  [{'q': "Sujet sur la détermination du taux de change",
    'f': "Le cours distingue d’abord le régime. En change fixe, le taux est "
         "fixé par l’État ou la banque centrale par rapport à une autre "
         "monnaie. En change flottant, la valeur varie librement selon "
         "l’offre et la demande sur le marché des changes, le marché "
         "déterminant le taux selon la confiance, les taux d’intérêt et la "
         "croissance. Il identifie ensuite deux sources de pression : les "
         "conversions de devises liées aux mouvements de capitaux et les "
         "achats de devises destinés à payer les importations.",
    'r': "On montre que le taux nominal résulte simultanément de flux "
         "commerciaux et de flux financiers, ce qui explique sa volatilité "
         "dans un régime de flottement.",
    'ex': "La pression à l’appréciation du dollar lorsque de nombreux "
          "investisseurs achètent des actifs américains."},
   {'q': "Sujet sur la lecture du cours d’une monnaie",
    'f': "Le cours impose un raisonnement en prix relatif. Le cours d’une "
         "monnaie est un prix : si 1 euro égale 1,10 dollar puis passe à 1 "
         "euro égale 1,17 dollar, l’euro s’est apprécié et le dollar s’est "
         "déprécié. Toute variation est donc symétrique, et le cours ajoute "
         "la distinction de vocabulaire : la dépréciation est une baisse du "
         "cours en système de change flottant, la dévaluation une baisse "
         "décidée par l’État en système de change fixe.",
    'r': "On montre que le taux de change est un prix relatif, de sorte "
         "qu’aucune monnaie ne peut s’apprécier sans qu’une autre se "
         "déprécie, ce qui explique le caractère conflictuel des politiques "
         "de change.",
    'ex': "Le passage de 1 euro égale 1,10 dollar à 1 euro égale 1,17 "
          "dollar."},
   {'q': "Sujet sur les limites du taux de change comme instrument de "
         "comparaison internationale",
    'f': "Le cours est explicite sur ce point. Un simple taux de change de "
         "marché ne reflète pas correctement le niveau de vie réel, parce "
         "qu’il dépend de la spéculation, des marchés financiers, des "
         "mouvements de capitaux, des anticipations et des déséquilibres "
         "monétaires ; il ne traduit pas nécessairement ce qu’un revenu "
         "permet réellement d’acheter dans chaque pays. C’est pourquoi le "
         "revenu national brut de l’indicateur de développement humain est "
         "exprimé en parité de pouvoir d’achat.",
    'r': "On montre que la conversion par le taux de marché introduit un "
         "biais systématique dans les comparaisons de niveau de vie, ce qui "
         "impose une correction par les prix.",
    'ex': "Un même revenu en dollars donnant des niveaux de vie réels très "
          "différents en Suisse et en Inde."},
   {'q': "Sujet sur le risque de change et les échanges internationaux",
    'f': "Le cours en donne une définition opératoire : le risque de change "
         "correspond à la situation où un ou des acteurs économiques peuvent "
         "être affectés par une variation du taux de change. L’exemple est "
         "simple : si un individu échange des francs contre des Deutschmark "
         "et que la monnaie est ensuite dévaluée, il perd de l’argent, ce "
         "qui peut dissuader et limiter les échanges. En régime de change "
         "fixe, le risque diminue fortement, d’où la logique du système de "
         "Bretton Woods.",
    'r': "On montre que l’instabilité nominale constitue un coût de "
         "transaction qui freine le commerce, ce qui justifie "
         "historiquement les régimes de change stables.",
    'ex': "L’entreprise qui signe un contrat aujourd’hui et doit payer dans "
          "six mois, exposée à une perte si le taux fluctue fortement."}],
  voisins=['n20-appreciation-depreciation', 'n20-changes-fixes-flottants',
           'n20-parite-pouvoir-achat', 'n20-triangle-incompatibilite'])

d('n20-appreciation-depreciation', 20, "Appréciation et dépréciation",
  "Deux effets contraires : importations renchéries, exportations facilitées",
  "L’appréciation est la hausse du cours d’une monnaie, la dépréciation sa "
  "baisse, dans un système de change flottant. Le cours en souligne la "
  "symétrie — si l’euro s’apprécie, le dollar se déprécie — et surtout "
  "l’ambivalence des effets : une dépréciation renchérit les importations, "
  "ce qui peut nourrir l’inflation importée, mais rend les exportations "
  "moins chères pour les étrangers.",
  "Le cours traite ces deux mouvements comme un prix relatif dont les "
  "effets vont dans deux directions opposées. La définition est d’abord "
  "posée : le cours d’une monnaie est un prix, et si 1 euro égale 1,10 "
  "dollar puis passe à 1 euro égale 1,17 dollar, l’euro s’est apprécié et le "
  "dollar s’est déprécié ; la dépréciation est la baisse du cours d’une "
  "monnaie dans un système de change flottant, à distinguer de la "
  "dévaluation, baisse décidée par l’État dans un système de change fixe. "
  "Le cours décrit ensuite la mécanique de la dépréciation. Son origine peut "
  "être commerciale : toutes choses égales par ailleurs, un déficit "
  "commercial important accroît l’offre de monnaie nationale, puisque les "
  "résidents vendent leur monnaie pour acheter des devises afin de payer "
  "leurs importations, ce qui déprécie cette monnaie. Son premier effet est "
  "le renchérissement des importations : si la monnaie nationale perd de sa "
  "valeur, le dollar devient relativement plus cher, et comme de nombreux "
  "biens sont libellés en dollars — pétrole, matières premières, biens "
  "importés — les mêmes quantités importées coûtent davantage en monnaie "
  "nationale. De là un cercle vicieux des monnaies faibles : déficit "
  "extérieur, monnaie en baisse, importations plus chères, déficit extérieur "
  "en hausse, monnaie en baisse encore. Et de là une spirale "
  "inflationniste : importations plus chères, coûts de production en hausse, "
  "prix domestiques en hausse, ce qui peut générer une inflation importée, "
  "voire une hyperinflation dans les cas extrêmes, le cours citant "
  "l’Argentine, le Liban et la Turquie. Mais le cours insiste sur la limite : "
  "ce cercle vicieux ne s’enclenche pas nécessairement, car une monnaie plus "
  "faible peut également stimuler les exportations. Une monnaie qui se "
  "déprécie renchérit les importations mais rend aussi les exportations "
  "moins chères pour les étrangers, de sorte que les exportations peuvent "
  "augmenter et que le solde extérieur peut à terme s’améliorer : cela "
  "renvoie à la courbe en J, selon laquelle dans un premier temps la "
  "dépréciation alourdit la facture des importations et peut dégrader le "
  "solde, puis les volumes exportés augmentent, les importations diminuent "
  "et le solde s’améliore. Une dépréciation ne conduit donc pas "
  "nécessairement à un cercle vicieux : si les exportations réagissent "
  "suffisamment, le gain de compétitivité-prix peut à terme améliorer le "
  "solde extérieur. Le cours mentionne enfin l’appréciation du côté des "
  "capitaux : si de nombreux investisseurs achètent des actifs américains, "
  "la demande de dollars augmente et exerce une pression à l’appréciation.",
  [("La variation du prix relatif des monnaies",
    "Le cours d’une monnaie est un prix : si l’euro passe de 1,10 à 1,17 "
    "dollar, il s’apprécie et le dollar se déprécie. Toute variation est "
    "donc symétrique entre les deux monnaies."),
   ("L’origine commerciale de la dépréciation",
    "Un déficit commercial important accroît l’offre de monnaie nationale, "
    "puisque les résidents vendent leur monnaie pour acheter des devises "
    "afin de payer leurs importations, ce qui tend à déprécier cette "
    "monnaie."),
   ("L’origine financière de l’appréciation",
    "Les mouvements internationaux de capitaux impliquent des conversions de "
    "devises : si de nombreux investisseurs achètent des actifs américains, "
    "la demande de dollars augmente et exerce une pression à "
    "l’appréciation."),
   ("Le renchérissement des importations",
    "Si la monnaie nationale perd de sa valeur, le dollar devient "
    "relativement plus cher, et comme pétrole, matières premières et biens "
    "importés sont souvent libellés en dollars, les mêmes quantités coûtent "
    "davantage en monnaie nationale."),
   ("Le cercle vicieux des monnaies faibles",
    "Déficit extérieur, monnaie en baisse, importations plus chères, déficit "
    "extérieur en hausse, nouvelle baisse de la monnaie : la spirale "
    "s’auto-entretient tant que les volumes exportés ne réagissent pas."),
   ("La transmission à l’inflation",
    "Importations plus chères, coûts de production en hausse, prix "
    "domestiques en hausse : la dépréciation peut générer une inflation "
    "importée, voire une hyperinflation dans les cas extrêmes."),
   ("L’effet favorable sur les exportations",
    "Une monnaie qui se déprécie rend les exportations moins chères pour les "
    "étrangers : les exportations peuvent augmenter et le solde extérieur "
    "s’améliorer à terme, selon la logique de la courbe en J.")],
  [{'a': "La notion fait apparaître deux effets opposés d’un même mouvement, "
         "ce qui interdit toute conclusion mécanique.",
    'cond': "L’argument suppose la double formule du cours : une monnaie qui "
            "se déprécie renchérit les importations mais rend aussi les "
            "exportations moins chères pour les étrangers.",
    'lim': "Le solde net dépend de la réaction des volumes, que le cours ne "
           "chiffre pas : il écrit seulement que les exportations « peuvent "
           "» augmenter."},
   {'a': "Elle relie le taux de change au solde extérieur dans les deux "
         "sens, origine et conséquence.",
    'cond': "L’argument suppose les deux chaînes du cours : le déficit "
            "déprécie la monnaie, et la dépréciation modifie le déficit.",
    'lim': "Cette double causalité rend l’analyse indéterminée à court "
           "terme : le cours présente une spirale possible et un "
           "redressement possible sans trancher."},
   {'a': "Elle éclaire le canal de l’inflation importée, et donc le lien "
         "entre change et prix domestiques.",
    'cond': "L’argument suppose la dépendance aux biens libellés en devises "
            "étrangères, le cours mentionnant pétrole, matières premières et "
            "biens importés.",
    'lim': "L’intensité de ce canal dépend du degré d’ouverture et de la "
           "structure des importations, que le cours n’examine pas pays par "
           "pays."},
   {'a': "Elle distingue soigneusement le mouvement de marché de la décision publique de modifier la parité.",
    'cond': "La distinction suppose le vocabulaire du cours : dépréciation "
            "en système de change flottant, dévaluation décidée par l’État "
            "en système de change fixe.",
    'lim': "La frontière est moins nette en pratique : le cours mentionne "
           "ailleurs le dumping monétaire, où un pays maintient son taux de "
           "change artificiellement faible."},
   {'a': "Elle explique la gravité particulière des dépréciations dans les "
         "économies endettées en devises.",
    'cond': "L’argument suppose le mécanisme du cours : si les revenus sont "
            "en monnaie nationale et la dette en dollars, une dépréciation "
            "alourdit mécaniquement la dette.",
    'lim': "Ce canal est propre aux économies qui empruntent en devise "
           "étrangère : il ne concerne pas les émetteurs de monnaie de "
           "réserve."}],
  [{'t': "Une dépréciation améliore mécaniquement le solde extérieur en "
         "rendant les exportations plus compétitives.",
    'qui': "La lecture que la courbe en J et le cercle vicieux du cours "
           "corrigent.",
    'rep': "Le cours montre que dans un premier temps la dépréciation "
           "alourdit la facture des importations et peut dégrader le solde, "
           "et que si les exportations ne réagissent pas suffisamment, un "
           "cercle vicieux des monnaies faibles peut s’enclencher : déficit, "
           "monnaie en baisse, importations plus chères, déficit aggravé."},
   {'t': "Une dépréciation conduit nécessairement à l’inflation importée et "
         "à la spirale des monnaies faibles.",
    'qui': "La lecture que le cours limite explicitement.",
    'rep': "Le cours objecte que ce cercle vicieux ne s’enclenche pas "
           "nécessairement, car une monnaie plus faible peut également "
           "stimuler les exportations : si celles-ci réagissent "
           "suffisamment, le gain de compétitivité-prix peut à terme "
           "améliorer le solde extérieur."},
   {'t': "Dépréciation et dévaluation sont deux mots interchangeables pour désigner la même réalité économique.",
    'qui': "La confusion que le cours corrige dans son vocabulaire "
           "monétaire.",
    'rep': "Le cours distingue : la dépréciation est la baisse du cours "
           "d’une monnaie dans un système de change flottant, tandis que la "
           "dévaluation est une baisse décidée par l’État dans un système de "
           "change fixe. L’une est un résultat de marché, l’autre une "
           "décision publique."},
   {'t': "Une appréciation de la monnaie nationale est toujours une bonne "
         "nouvelle pour l’économie.",
    'qui': "La lecture que le cours nuance en examinant les effets sur les "
           "exportateurs.",
    'rep': "Le cours relève qu’une réévaluation rend les exportations moins "
           "compétitives, et il observe que l’appréciation d’une monnaie "
           "sert certains intérêts et pas d’autres : elle allège la facture "
           "des importations mais pénalise les producteurs exposés à la "
           "concurrence internationale."}],
  [{'n': "Robert Mundell",
    'i': "Un pays ne peut avoir simultanément liberté des capitaux, "
         "stabilité du change et autonomie monétaire.",
    'p': "Le cours en tire la conséquence pour les variations du change : "
         "avec une politique monétaire indépendante et une libre "
         "circulation des capitaux, un pays ne peut pas maintenir un taux de "
         "change stable, puisque les capitaux circulent librement et font "
         "varier la valeur de la monnaie."},
   {'n': "Henri Bourguinat",
    'i': "La globalisation financière repose sur le décloisonnement, la "
         "déréglementation et la désintermédiation.",
    'p': "Le cours situe les trois D en 1987 et en tire la raison de "
         "l’ampleur des mouvements de change contemporains : les conversions "
         "de devises associées aux flux de capitaux influencent directement "
         "l’offre, la demande et donc le cours des monnaies."},
   {'n': "Jean Bodin",
    'i': "La quantité de monnaie en circulation agit sur le niveau des prix.",
    'p': "Le cours mobilise cette intuition pour éclairer la valeur de la "
         "monnaie, ce qui permet de comprendre le canal de l’inflation "
         "importée : une dépréciation renchérit les biens libellés en "
         "devises étrangères et élève donc les prix domestiques par les "
         "coûts de production."},
   {'n': "Irving Fisher",
    'i': "La quantité de monnaie et sa vitesse de circulation se rapportent "
         "au niveau des prix et au volume des transactions.",
    'p': "Le cours mobilise cette relation dans l’analyse de la valeur "
         "interne de la monnaie, ce qui éclaire la différence entre une "
         "dépréciation externe, qui modifie le cours de la monnaie, et "
         "l’inflation interne, qui en réduit le pouvoir d’achat domestique."}],
  [{'f': "Si 1 euro égale 1,10 dollar puis passe à 1 euro égale 1,17 dollar, "
         "l’euro s’est apprécié et le dollar s’est déprécié : toute variation "
         "du cours est symétrique.",
    'p': "L’exemple chiffré établit le caractère relatif du taux de change "
         "et interdit de parler d’appréciation sans désigner la monnaie de "
         "référence."},
   {'f': "La dépréciation est la baisse du cours d’une monnaie dans un "
         "système de change flottant, tandis que la dévaluation est une "
         "baisse décidée par l’État dans un système de change fixe.",
    'p': "La distinction de vocabulaire montre que le même mouvement de prix "
         "peut relever du marché ou d’une décision publique selon le régime "
         "en vigueur."},
   {'f': "Un déficit commercial important accroît l’offre de monnaie "
         "nationale, puisque les résidents vendent leur monnaie pour acheter "
         "des devises afin de payer leurs importations, ce qui déprécie "
         "cette monnaie.",
    'p': "Le fait établit l’origine commerciale de la dépréciation et relie "
         "directement le solde extérieur au taux de change."},
   {'f': "La dépréciation renchérit les biens libellés en dollars — pétrole, "
         "matières premières, biens importés — de sorte que les mêmes "
         "quantités importées coûtent davantage en monnaie nationale, ce qui "
         "peut générer une inflation importée voire une hyperinflation, "
         "comme en Argentine, au Liban ou en Turquie.",
    'p': "Le fait montre la transmission du déséquilibre extérieur à "
         "l’économie domestique par les prix."},
   {'f': "Une monnaie qui se déprécie rend les exportations moins chères "
         "pour les étrangers, de sorte que les exportations peuvent "
         "augmenter et que le solde extérieur peut à terme s’améliorer, "
         "selon la logique de la courbe en J.",
    'p': "Le fait établit l’effet favorable et montre que le cercle vicieux "
         "des monnaies faibles ne s’enclenche pas nécessairement."},
   {'f': "Si de nombreux investisseurs achètent des actifs américains, la "
         "demande de dollars augmente et exerce une pression à "
         "l’appréciation du dollar, un seul achat ayant peu d’effet.",
    'p': "Le fait établit l’origine financière de l’appréciation et montre "
         "que les mouvements de capitaux déterminent le change au même titre "
         "que les échanges de biens."}],
  [{'q': "Sujet sur les effets d’une dépréciation monétaire",
    'f': "Le cours construit deux effets opposés. Une monnaie qui se "
         "déprécie renchérit les importations, et comme pétrole, matières "
         "premières et biens importés sont souvent libellés en dollars, les "
         "mêmes quantités coûtent davantage en monnaie nationale, ce qui "
         "peut aggraver le déficit et nourrir l’inflation importée. Mais "
         "elle rend aussi les exportations moins chères pour les étrangers, "
         "de sorte que les volumes exportés peuvent augmenter et le solde "
         "s’améliorer à terme, selon la logique de la courbe en J.",
    'r': "On montre que le signe de l’effet net dépend de la réaction des "
         "volumes, ce qui interdit de conclure mécaniquement à "
         "l’amélioration comme à la dégradation du solde.",
    'ex': "Le cercle vicieux des monnaies faibles opposé à la logique de la "
          "courbe en J."},
   {'q': "Sujet sur la transmission des déséquilibres extérieurs à "
         "l’économie domestique",
    'f': "Le cours décrit une spirale en deux temps. D’abord extérieure : "
         "déficit extérieur, monnaie en baisse, importations plus chères, "
         "déficit extérieur en hausse, nouvelle baisse de la monnaie. "
         "Ensuite inflationniste : importations plus chères, coûts de "
         "production en hausse, prix domestiques en hausse, inflation "
         "importée, voire hyperinflation dans les cas extrêmes, le cours "
         "citant l’Argentine, le Liban et la Turquie.",
    'r': "On montre que la dépréciation est le canal par lequel un "
         "déséquilibre extérieur devient un problème de prix intérieurs, ce "
         "qui en étend les conséquences à toute la population.",
    'ex': "La dépendance aux biens libellés en devises étrangères, pétrole "
          "et matières premières notamment."},
   {'q': "Sujet sur la distinction entre mouvements de marché et décisions "
         "publiques en matière de change",
    'f': "Le cours fixe le vocabulaire. La dépréciation est la baisse du "
         "cours d’une monnaie dans un système de change flottant ; la "
         "dévaluation est une baisse décidée par l’État dans un système de "
         "change fixe. La distinction a une portée analytique : elle oppose "
         "un résultat de marché, qui échappe aux autorités, à un instrument "
         "de politique économique, qu’elles peuvent mobiliser.",
    'r': "On montre que la nature du mouvement dépend du régime de change, "
         "ce qui relie le vocabulaire monétaire au choix institutionnel.",
    'ex': "Le passage historique relevé par le cours : la valeur de la "
          "monnaie est désormais fixée par le change flottant alors "
          "qu’auparavant le change était fixe."},
   {'q': "Sujet sur les origines des variations de change",
    'f': "Le cours en identifie deux. L’origine commerciale : un déficit "
         "commercial important accroît l’offre de monnaie nationale, "
         "puisque les résidents vendent leur monnaie pour acheter des "
         "devises afin de payer leurs importations, ce qui la déprécie. "
         "L’origine financière : les mouvements internationaux de capitaux "
         "impliquent des conversions de devises, et si de nombreux "
         "investisseurs achètent des actifs américains la demande de dollars "
         "augmente et exerce une pression à l’appréciation.",
    'r': "On montre que le change est déterminé simultanément par les flux "
         "réels et les flux financiers, ce qui explique que son évolution ne "
         "suive pas toujours celle des soldes commerciaux.",
    'ex': "La dimension monétaire des mouvements de capitaux relevée par le "
          "cours."}],
  voisins=['n20-taux-change-nominal-reel', 'n20-courbe-en-j',
           'n20-devaluation-reevaluation', 'n20-crise-change'])

d('n20-devaluation-reevaluation', 20, "Dévaluation et réévaluation",
  "Quand c’est l’État qui modifie le cours de la monnaie",
  "La dévaluation est une baisse du cours d’une monnaie décidée par l’État "
  "dans un système de change fixe, la réévaluation la décision symétrique de "
  "hausse. Le cours les oppose à la dépréciation et à l’appréciation, qui "
  "résultent du marché en régime flottant : la dévaluation est donc un "
  "instrument de politique économique et non un résultat.",
  "Le cours définit la dévaluation par contraste. La dépréciation est la "
  "baisse du cours d’une monnaie dans un système de change flottant ; la "
  "dévaluation est une baisse décidée par l’État dans un système de change "
  "fixe. Cette opposition suppose la distinction des régimes : en régime de "
  "change fixe, le taux de change d’une monnaie est fixé par l’État ou la "
  "banque centrale par rapport à une autre monnaie, de sorte que modifier ce "
  "taux est une décision publique ; en régime flottant, la valeur varie "
  "librement selon l’offre et la demande sur le marché des changes, et "
  "aucune décision n’est requise. Le cours relève d’ailleurs le changement "
  "historique de régime : la valeur de la monnaie est désormais fixée par le "
  "change flottant alors qu’auparavant le change était fixe, le système de "
  "Bretton Woods ayant reposé sur des taux de change fixes mais ajustables, "
  "organisés autour du dollar lui-même convertible en or pour les autorités "
  "monétaires étrangères, jusqu’à la suspension de la convertibilité du "
  "dollar en or en 1971 puis au passage progressif aux régimes de change "
  "flottants, entériné par les accords de la Jamaïque de 1976. L’objectif "
  "d’une dévaluation est d’agir sur la compétitivité-prix. Le cours en donne "
  "l’effet par symétrie avec la réévaluation : si une monnaie se réévaluait, "
  "les exportations deviendraient moins compétitives ; une dévaluation rend "
  "donc les exportations moins chères pour les étrangers et renchérit les "
  "importations. Mais les deux mêmes limites que pour la dépréciation "
  "s’appliquent. Première limite, le délai : dans un premier temps la "
  "facture des importations augmente et le solde peut se dégrader, puis les "
  "volumes exportés augmentent, les importations diminuent et le solde "
  "s’améliore, selon la logique de la courbe en J. Deuxième limite, "
  "l’inflation importée : des importations plus chères élèvent les coûts de "
  "production puis les prix domestiques. Le cours traite enfin une forme "
  "détournée de cette politique, le dumping monétaire, qui correspond à une "
  "situation dans laquelle un pays maintient son taux de change "
  "artificiellement faible : monnaie sous-évaluée, exportations moins "
  "chères, importations plus chères, compétitivité-prix des producteurs "
  "nationaux en hausse ; cela peut également rendre le coût du travail "
  "exprimé en devises étrangères plus faible et donc le territoire plus "
  "attractif pour les investissements directs. La qualification de dumping "
  "reste toutefois délicate, puisqu’il faut distinguer un avantage "
  "comparatif légitime d’une stratégie délibérée destinée à fausser la "
  "concurrence internationale.",
  [("La modification administrative du cours",
    "En régime de change fixe, le taux est fixé par l’État ou la banque "
    "centrale par rapport à une autre monnaie : le modifier est donc une "
    "décision publique, et non un résultat de marché."),
   ("La définition par contraste",
    "La dépréciation est la baisse du cours d’une monnaie dans un système de "
    "change flottant, la dévaluation une baisse décidée par l’État dans un "
    "système de change fixe : même mouvement de prix, nature différente."),
   ("L’objectif de compétitivité-prix",
    "Une dévaluation rend les exportations moins chères pour les étrangers "
    "et renchérit les importations : l’objectif est donc d’améliorer la "
    "compétitivité-prix des producteurs nationaux."),
   ("L’effet symétrique de la réévaluation",
    "Le cours le formule directement : si une monnaie se réévaluait, les "
    "exportations deviendraient moins compétitives. La réévaluation est donc "
    "l’instrument inverse, qui pèse sur les exportateurs."),
   ("Le délai d’ajustement",
    "Dans un premier temps la facture des importations augmente et le solde "
    "peut se dégrader ; puis les volumes exportés augmentent, les "
    "importations diminuent et le solde s’améliore : c’est la logique de la "
    "courbe en J."),
   ("Le risque d’inflation importée",
    "Des importations plus chères élèvent les coûts de production puis les "
    "prix domestiques, ce qui peut annuler le gain de compétitivité obtenu "
    "en renchérissant à son tour la production nationale."),
   ("La forme détournée du dumping monétaire",
    "Maintenir un taux de change artificiellement faible produit le même "
    "effet durablement : monnaie sous-évaluée, exportations moins chères, "
    "importations plus chères, compétitivité-prix des producteurs nationaux "
    "en hausse.")],
  [{'a': "La notion identifie un instrument de politique économique "
         "directement maniable par les autorités.",
    'cond': "L’argument suppose un régime de change fixe, dans lequel le "
            "taux est fixé par l’État ou la banque centrale par rapport à "
            "une autre monnaie.",
    'lim': "L’instrument a largement disparu dans les grandes économies : le "
           "cours relève que la valeur de la monnaie est désormais fixée par "
           "le change flottant."},
   {'a': "Elle agit sur la compétitivité-prix sans qu’il soit nécessaire de toucher aux salaires ni aux prélèvements.",
    'cond': "L’argument suppose l’effet retenu par le cours : une "
            "dévaluation rend les exportations moins chères pour les "
            "étrangers et renchérit les importations.",
    'lim': "Le gain peut être annulé par l’inflation importée : des "
           "importations plus chères élèvent les coûts de production puis "
           "les prix domestiques."},
   {'a': "Elle se distingue clairement de la dépréciation, ce qui discipline "
         "le vocabulaire de l’analyse monétaire.",
    'cond': "La distinction suppose la définition du cours : dépréciation en "
            "régime flottant, dévaluation décidée par l’État en régime fixe.",
    'lim': "La frontière se brouille avec le dumping monétaire, où un pays "
           "maintient son taux artificiellement faible sans dévaluation "
           "formelle."},
   {'a': "Elle éclaire par symétrie l’effet d’une réévaluation sur la position des exportateurs nationaux.",
    'cond': "L’argument suppose l’énoncé du cours : si une monnaie se "
            "réévaluait, les exportations deviendraient moins compétitives.",
    'lim': "Le cours ne développe pas les motifs d’une réévaluation, qui "
           "peut notamment viser à contenir l’inflation importée."},
   {'a': "Elle se rattache à un cadre institutionnel historique "
         "identifiable, celui de Bretton Woods.",
    'cond': "Le rattachement suppose le système décrit par le cours : des "
            "taux de change fixes mais ajustables, organisés autour du "
            "dollar convertible en or pour les autorités monétaires "
            "étrangères.",
    'lim': "Ce cadre a disparu : la convertibilité du dollar en or est "
           "suspendue en 1971 et les accords de la Jamaïque de 1976 "
           "entérinent le passage aux changes flottants."}],
  [{'t': "Dévaluer sa monnaie est le moyen le plus simple de rétablir la "
         "compétitivité d’une économie.",
    'qui': "La lecture que les deux limites du cours corrigent.",
    'rep': "Le cours objecte d’abord le délai, puisque dans un premier temps "
           "la facture des importations augmente et le solde peut se "
           "dégrader selon la logique de la courbe en J, puis l’inflation "
           "importée, des importations plus chères élevant les coûts de "
           "production et donc les prix domestiques."},
   {'t': "Dévaluation et dépréciation désignent au fond le même phénomène économique, sous deux noms différents.",
    'qui': "La confusion que le cours corrige dans son vocabulaire.",
    'rep': "Le cours distingue : la dépréciation est la baisse du cours "
           "d’une monnaie dans un système de change flottant, résultat du "
           "marché, tandis que la dévaluation est une baisse décidée par "
           "l’État dans un système de change fixe, donc un instrument de "
           "politique économique."},
   {'t': "Un pays dont la monnaie flotte ne peut plus agir d’aucune manière sur son taux de change.",
    'qui': "La lecture que la notion de dumping monétaire nuance.",
    'rep': "Le cours décrit le dumping monétaire comme une situation dans "
           "laquelle un pays maintient son taux de change artificiellement "
           "faible, avec pour conséquences une monnaie sous-évaluée, des "
           "exportations moins chères, des importations plus chères et une "
           "compétitivité-prix accrue des producteurs nationaux."},
   {'t': "Maintenir une monnaie sous-évaluée est un avantage comparatif "
         "légitime comme un autre.",
    'qui': "La lecture que le cours soumet au test de la qualification du "
           "dumping.",
    'rep': "Le cours rappelle que la qualification de dumping est délicate "
           "car elle suppose de distinguer un avantage comparatif légitime, "
           "lié au niveau de développement, d’une stratégie délibérée "
           "destinée à fausser la concurrence internationale, mais il "
           "maintient la catégorie du dumping monétaire."}],
  [{'n': "Robert Mundell",
    'i': "Liberté des capitaux, stabilité du change et autonomie monétaire "
         "ne peuvent être poursuivies ensemble.",
    'p': "Le cours en tire la condition de possibilité d’une politique de "
         "change : si un pays veut stabilité du taux de change et liberté "
         "des capitaux, il doit renoncer à sa politique monétaire autonome "
         "et aligner ses taux sur ceux du pays de référence ; s’il veut "
         "stabilité et autonomie, il doit contrôler les mouvements de "
         "capitaux."},
   {'n': "Henri Bourguinat",
    'i': "La globalisation financière repose sur le décloisonnement, la "
         "déréglementation et la désintermédiation.",
    'p': "Le cours situe les trois D en 1987 et en tire la difficulté "
         "contemporaine de toute politique de change : la libre circulation "
         "des capitaux rend coûteux le maintien d’une parité, puisque les "
         "flux font varier la valeur de la monnaie en permanence."},
   {'n': "Jean Bodin",
    'i': "La quantité de monnaie en circulation agit sur le niveau des prix.",
    'p': "Le cours mobilise cette intuition pour éclairer la limite "
         "inflationniste d’une dévaluation : en renchérissant les biens "
         "importés, elle élève les coûts de production puis les prix "
         "domestiques, ce qui réduit progressivement l’avantage de "
         "compétitivité obtenu."},
   {'n': "Irving Fisher",
    'i': "La quantité de monnaie et sa vitesse de circulation se rapportent "
         "au niveau des prix et au volume des transactions.",
    'p': "Le cours mobilise cette relation dans l’analyse de la valeur de la "
         "monnaie, ce qui permet de distinguer l’effet externe d’une "
         "dévaluation, sur le cours de la monnaie, de son effet interne, sur "
         "les prix domestiques par le canal des importations."}],
  [{'f': "La dépréciation est la baisse du cours d’une monnaie dans un "
         "système de change flottant, tandis que la dévaluation est une "
         "baisse décidée par l’État dans un système de change fixe.",
    'p': "La distinction établit que le même mouvement de prix relève du "
         "marché ou de la décision publique selon le régime de change en "
         "vigueur."},
   {'f': "Le cours relève qu’une réévaluation rendrait les exportations "
         "moins compétitives, ce qui constitue l’effet symétrique de la "
         "dévaluation.",
    'p': "Le fait montre que la politique de change est un arbitrage entre "
         "intérêts des exportateurs et coût des importations."},
   {'f': "Le système de Bretton Woods repose sur des taux de change fixes "
         "mais ajustables, organisés autour du dollar lui-même convertible "
         "en or pour les autorités monétaires étrangères.",
    'p': "Le fait situe historiquement le cadre dans lequel la dévaluation "
         "était un instrument ordinaire de politique économique."},
   {'f': "En 1971 les États-Unis suspendent la convertibilité du dollar en "
         "or, puis les principales monnaies passent progressivement à des "
         "régimes de change flottants, ce que les accords de la Jamaïque de "
         "1976 entérinent.",
    'p': "Le fait explique la quasi-disparition de la dévaluation comme "
         "instrument dans les grandes économies, remplacée par la "
         "dépréciation de marché."},
   {'f': "Le dumping monétaire correspond à une situation dans laquelle un "
         "pays maintient son taux de change artificiellement faible : "
         "monnaie sous-évaluée, exportations moins chères, importations plus "
         "chères, compétitivité-prix des producteurs nationaux en hausse.",
    'p': "Le fait montre la forme contemporaine de la politique de change "
         "offensive, qui agit sans dévaluation formelle."},
   {'f': "Une monnaie sous-évaluée rend également le coût du travail exprimé "
         "en devises étrangères plus faible, et donc le territoire plus "
         "attractif pour les investissements directs étrangers.",
    'p': "Le fait montre que la politique de change agit sur l’attractivité "
         "productive et non seulement sur les flux commerciaux."}],
  [{'q': "Sujet sur la dévaluation comme instrument de politique économique",
    'f': "Le cours en précise la nature et les limites. La dévaluation est "
         "une baisse du cours décidée par l’État dans un système de change "
         "fixe, destinée à rendre les exportations moins chères pour les "
         "étrangers et à renchérir les importations. Mais deux limites "
         "s’imposent : le délai, puisque dans un premier temps la facture "
         "des importations augmente et le solde peut se dégrader selon la "
         "logique de la courbe en J ; et l’inflation importée, des "
         "importations plus chères élevant les coûts puis les prix.",
    'r': "On montre que le gain de compétitivité est à la fois différé et "
         "partiellement auto-annulé, ce qui limite fortement l’efficacité de "
         "l’instrument.",
    'ex': "L’effet symétrique relevé par le cours : une réévaluation rendrait "
          "les exportations moins compétitives."},
   {'q': "Sujet sur l’évolution des régimes monétaires internationaux",
    'f': "Le cours retrace le basculement. Le système de Bretton Woods "
         "repose sur des taux de change fixes mais ajustables, organisés "
         "autour du dollar lui-même convertible en or pour les autorités "
         "monétaires étrangères, la stabilité des changes réduisant "
         "l’incertitude et facilitant les paiements internationaux. En 1971, "
         "les États-Unis suspendent la convertibilité du dollar en or, puis "
         "les principales monnaies passent à des régimes flottants, ce que "
         "les accords de la Jamaïque de 1976 entérinent.",
    'r': "On montre que la dévaluation était un instrument propre à un "
         "ordre monétaire déterminé, et que sa disparition découle du "
         "changement de régime et non d’un changement de doctrine.",
    'ex': "La logique de Bretton Woods : stabilité des changes, réduction de "
          "l’incertitude, facilitation des paiements, développement des "
          "échanges."},
   {'q': "Sujet sur le dumping monétaire",
    'f': "Le cours en donne une définition et un mécanisme. Le dumping "
         "monétaire correspond à une situation dans laquelle un pays "
         "maintient son taux de change artificiellement faible, avec pour "
         "conséquences une monnaie sous-évaluée, des exportations moins "
         "chères, des importations plus chères et une compétitivité-prix "
         "accrue des producteurs nationaux ; il rend aussi le coût du "
         "travail exprimé en devises étrangères plus faible, donc le "
         "territoire plus attractif pour les investissements directs.",
    'r': "On montre que la politique de change peut remplacer la "
         "dévaluation formelle et produire des effets analogues et durables, "
         "ce qui explique qu’elle soit devenue un motif de contentieux "
         "commercial.",
    'ex': "La difficulté de qualification du dumping : distinguer un "
          "avantage comparatif légitime d’une stratégie délibérée."},
   {'q': "Sujet sur les marges de manœuvre d’une politique de change",
    'f': "Le cours mobilise le triangle de Mundell. Si un pays veut une "
         "politique monétaire indépendante et la liberté des capitaux, il ne "
         "peut pas maintenir un taux de change stable, car les capitaux "
         "circulent librement et font varier la valeur de la monnaie. S’il "
         "veut la stabilité du change et la liberté des capitaux, il doit "
         "renoncer à son autonomie monétaire et aligner ses taux sur ceux du "
         "pays de référence. S’il veut stabilité et autonomie, il doit "
         "contrôler les mouvements de capitaux.",
    'r': "On montre qu’une politique de change n’est possible qu’au prix de "
         "l’abandon d’un autre objectif, ce qui transforme la dévaluation en "
         "choix institutionnel et non en simple décision technique.",
    'ex': "La Chine, qui a longtemps limité la libre circulation des "
          "capitaux pour conserver stabilité du change et autonomie "
          "monétaire."}],
  voisins=['n20-appreciation-depreciation', 'n20-changes-fixes-flottants',
           'n20-courbe-en-j', 'n20-triangle-incompatibilite'])

d('n20-parite-pouvoir-achat', 20, "Parité de pouvoir d’achat",
  "Corriger les taux de change financiers pour comparer les niveaux de vie",
  "La parité de pouvoir d’achat est la méthode de conversion qui permet de "
  "comparer les revenus entre pays en tenant compte du coût de la vie, et "
  "non du taux de change de marché. Le cours la justifie ainsi : un simple "
  "taux de change de marché ne reflète pas correctement le niveau de vie "
  "réel, car il dépend de la spéculation, des marchés financiers, des "
  "mouvements de capitaux, des anticipations et des déséquilibres "
  "monétaires.",
  "Le cours mobilise la parité de pouvoir d’achat comme un instrument de "
  "mesure, et c’est dans cet usage qu’il faut la maîtriser. La "
  "justification est donnée à propos de l’indicateur de développement "
  "humain, dont la dimension monétaire est mesurée par le revenu national "
  "brut par habitant en parité de pouvoir d’achat. Pourquoi ce choix ? "
  "Parce qu’un simple taux de change de marché ne reflète pas correctement "
  "le niveau de vie réel : ce taux dépend de la spéculation, des marchés "
  "financiers, des mouvements de capitaux, des anticipations et des "
  "déséquilibres monétaires, et il ne traduit pas nécessairement ce qu’un "
  "revenu permet réellement d’acheter dans chaque pays. La parité de pouvoir "
  "d’achat permet au contraire de comparer le pouvoir d’achat réel, le "
  "volume de biens et services accessibles et le niveau de vie concret des "
  "populations. Le cours en donne un exemple décisif : avec un même revenu "
  "exprimé en dollars, le niveau de vie réel peut être très différent entre "
  "la Suisse et l’Inde, car le coût de la vie n’est pas le même, et c’est "
  "précisément ce que corrige la parité de pouvoir d’achat. La conclusion "
  "est explicite : la parité de pouvoir d’achat corrige les biais liés aux "
  "taux de change financiers et permet de comparer plus justement les "
  "niveaux de vie entre pays, de sorte que le revenu national brut utilisé "
  "dans l’indicateur de développement humain est exprimé en parité de "
  "pouvoir d’achat afin de mieux refléter le pouvoir d’achat réel des "
  "populations et d’éviter les distorsions liées aux taux de change de "
  "marché. Le cours mobilise également cette convention dans deux autres "
  "contextes. Dans la courbe de l’éléphant de Branko Milanovic, les revenus "
  "sont mesurés en termes réels, c’est-à-dire déflatés, et en parité de "
  "pouvoir d’achat, de sorte que les résultats ne sont biaisés ni par "
  "l’inflation ni par les taux de change financiers. Et dans la mesure du "
  "basculement du poids économique mondial : la part de la Chine dans le "
  "produit intérieur brut mondial en parité de pouvoir d’achat augmente "
  "considérablement, les BRICS élargis représentant environ 36 % du produit "
  "intérieur brut mondial en parité de pouvoir d’achat en 2022 et 25 % des "
  "exportations mondiales en 2021. Il faut noter que le cours emploie la "
  "parité de pouvoir d’achat comme méthode de conversion statistique, et non "
  "comme théorie de détermination du taux de change à long terme.",
  [("Le constat d’insuffisance du taux de marché",
    "Un simple taux de change de marché ne reflète pas correctement le "
    "niveau de vie réel : il ne traduit pas nécessairement ce qu’un revenu "
    "permet réellement d’acheter dans chaque pays."),
   ("L’identification des biais du taux financier",
    "Le taux de change de marché dépend de la spéculation, des marchés "
    "financiers, des mouvements de capitaux, des anticipations et des "
    "déséquilibres monétaires : autant de facteurs étrangers au coût de la "
    "vie."),
   ("La conversion par le coût de la vie",
    "La parité de pouvoir d’achat permet de comparer le pouvoir d’achat "
    "réel, le volume de biens et services accessibles et le niveau de vie "
    "concret des populations, en tenant compte des prix locaux."),
   ("Le test par un exemple extrême",
    "Avec un même revenu exprimé en dollars, le niveau de vie réel peut être "
    "très différent entre la Suisse et l’Inde, car le coût de la vie n’est "
    "pas le même : c’est précisément ce que corrige la parité de pouvoir "
    "d’achat."),
   ("L’application à la mesure du développement",
    "Le revenu national brut utilisé dans l’indicateur de développement "
    "humain est exprimé en parité de pouvoir d’achat afin de mieux refléter "
    "le pouvoir d’achat réel des populations et d’éviter les distorsions "
    "liées aux taux de change de marché."),
   ("L’application à la mesure des inégalités mondiales",
    "Dans la courbe de l’éléphant, les revenus sont mesurés en termes réels, "
    "déflatés, et en parité de pouvoir d’achat, de sorte que les résultats "
    "ne sont biaisés ni par l’inflation ni par les taux de change "
    "financiers."),
   ("L’application à la mesure du poids économique",
    "La part de la Chine dans le produit intérieur brut mondial en parité de "
    "pouvoir d’achat augmente considérablement, les BRICS élargis "
    "représentant environ 36 % du produit intérieur brut mondial en parité "
    "de pouvoir d’achat en 2022.")],
  [{'a': "La notion corrige un biais précisément identifié et nommé par le cours, celui des taux de change financiers.",
    'cond': "La correction suppose l’énumération du cours : spéculation, "
            "marchés financiers, mouvements de capitaux, anticipations, "
            "déséquilibres monétaires.",
    'lim': "La correction repose sur un panier de biens conventionnel que le "
           "cours ne détaille pas, ce qui laisse une marge de choix "
           "méthodologique."},
   {'a': "Elle permet des comparaisons internationales de niveau de vie beaucoup plus fiables entre économies.",
    'cond': "La fiabilité suppose que l’on cherche à mesurer le pouvoir "
            "d’achat réel, le volume de biens et services accessibles et le "
            "niveau de vie concret, comme le fait le cours.",
    'lim': "Elle n’est pas pertinente pour tous les usages : pour mesurer "
           "une capacité d’achat sur les marchés internationaux, le taux de "
           "change courant reste la référence."},
   {'a': "Elle se combine avec la déflation par les prix pour neutraliser deux biais de mesure à la fois.",
    'cond': "L’argument suppose la méthodologie de la courbe de l’éléphant : "
            "revenus mesurés en termes réels, déflatés, et en parité de "
            "pouvoir d’achat.",
    'lim': "Le cours ne discute pas la sensibilité des résultats à ces "
           "conventions, alors que la forme de la courbe en dépend "
           "partiellement."},
   {'a': "Elle change la hiérarchie des puissances économiques mesurée, ce "
         "qui a une portée analytique forte.",
    'cond': "L’argument suppose les chiffres du cours : environ 36 % du "
            "produit intérieur brut mondial en parité de pouvoir d’achat "
            "pour les BRICS élargis en 2022.",
    'lim': "Cette hiérarchie ne vaut pas pour toutes les questions : le "
           "poids financier et monétaire d’un pays dépend des taux courants "
           "et non de la parité."},
   {'a': "Elle fournit un instrument de mesure du développement humain et non seulement du revenu monétaire.",
    'cond': "L’argument suppose l’usage du cours : le revenu national brut "
            "par habitant en parité de pouvoir d’achat comme dimension "
            "monétaire de l’indicateur de développement humain.",
    'lim': "Le cours souligne que cet indicateur reste imparfait, puisqu’il "
           "ne dit pas comment les ressources sont réparties à l’intérieur "
           "d’un pays."}],
  [{'t': "Le taux de change de marché est le bon instrument pour comparer "
         "les revenus entre pays.",
    'qui': "La lecture que la justification de la parité de pouvoir d’achat "
           "réfute explicitement.",
    'rep': "Le cours objecte qu’un simple taux de change de marché ne "
           "reflète pas correctement le niveau de vie réel, car il dépend de "
           "la spéculation, des marchés financiers, des mouvements de "
           "capitaux, des anticipations et des déséquilibres monétaires, et "
           "ne traduit pas ce qu’un revenu permet réellement d’acheter."},
   {'t': "La parité de pouvoir d’achat est une correction technique sans "
         "conséquence sur les conclusions économiques.",
    'qui': "La lecture que les chiffres du cours démentent.",
    'rep': "Le cours montre que la hiérarchie des puissances change : la "
           "part de la Chine dans le produit intérieur brut mondial en "
           "parité de pouvoir d’achat augmente considérablement, les BRICS "
           "élargis atteignant environ 36 % du produit intérieur brut "
           "mondial en 2022, tandis que la part relative du G7 diminue."},
   {'t': "La parité de pouvoir d’achat détermine le taux de change à long "
         "terme, de sorte que les monnaies convergent vers elle.",
    'qui': "Une thèse que le cours n’énonce pas : il n’emploie la parité que "
           "comme méthode de conversion.",
    'rep': "Le cours présente la parité de pouvoir d’achat comme une "
           "convention statistique destinée à corriger les biais liés aux "
           "taux de change financiers pour comparer les niveaux de vie, et "
           "il ne la présente pas comme une théorie de détermination du "
           "taux de change."},
   {'t': "Puisque la parité de pouvoir d’achat corrige le coût de la vie, "
         "elle mesure correctement le développement d’un pays.",
    'qui': "La lecture que le cours limite en discutant l’indicateur de "
           "développement humain.",
    'rep': "Le cours rappelle que même si cet indicateur constitue un "
           "progrès majeur, il reste imparfait : il donne une moyenne "
           "nationale et ne dit pas comment les ressources et les "
           "performances sont réparties à l’intérieur d’un pays, d’où la "
           "création de l’indicateur ajusté aux inégalités."}],
  [{'n': "Branko Milanovic",
    'i': "La courbe de l’éléphant fait apparaître les gagnants et les "
         "perdants de la mondialisation.",
    'p': "Le cours précise la méthodologie : les revenus sont mesurés en "
         "termes réels, c’est-à-dire déflatés, et en parité de pouvoir "
         "d’achat, de sorte que les résultats ne sont biaisés ni par "
         "l’inflation ni par les taux de change financiers, ce qui rend la "
         "comparaison internationale possible."},
   {'n': "Irving Fisher",
    'i': "La quantité de monnaie et sa vitesse de circulation se rapportent "
         "au niveau des prix et au volume des transactions.",
    'p': "Le cours mobilise cette relation dans l’analyse de la valeur "
         "interne de la monnaie, ce qui fonde la logique de la parité de "
         "pouvoir d’achat : ce qui compte pour le niveau de vie est le "
         "volume de biens qu’une somme permet d’acquérir, non son équivalent "
         "en devises."},
   {'n': "Jean Bodin",
    'i': "La quantité de monnaie en circulation agit sur le niveau des prix.",
    'p': "Le cours mobilise cette intuition pour éclairer l’écart entre la "
           "valeur nominale d’un revenu et son pouvoir d’achat effectif : "
         "deux pays peuvent afficher des revenus convertis identiques tout "
         "en offrant des niveaux de vie très différents si leurs niveaux de "
         "prix diffèrent."},
   {'n': "Amartya Sen",
    'i': "Le développement doit être mesuré par les capacités réelles des "
         "individus et non par le seul revenu.",
    'p': "Le cours en tire la logique de l’indicateur de développement "
         "humain, dont la dimension monétaire est précisément mesurée par le "
         "revenu national brut par habitant en parité de pouvoir d’achat, "
         "afin de mieux refléter ce que les populations peuvent réellement "
         "se procurer."}],
  [{'f': "Un simple taux de change de marché ne reflète pas correctement le "
         "niveau de vie réel, parce qu’il dépend de la spéculation, des "
         "marchés financiers, des mouvements de capitaux, des anticipations "
         "et des déséquilibres monétaires.",
    'p': "L’énumération identifie précisément les biais que la parité de "
         "pouvoir d’achat corrige, et justifie donc son emploi dans les "
         "comparaisons internationales."},
   {'f': "Avec un même revenu exprimé en dollars, le niveau de vie réel peut "
         "être très différent entre la Suisse et l’Inde, car le coût de la "
         "vie n’est pas le même.",
    'p': "L’exemple démontre l’ampleur du biais corrigé et rend immédiate la "
         "nécessité d’une conversion par les prix."},
   {'f': "Le revenu national brut utilisé dans l’indicateur de développement "
         "humain est exprimé en parité de pouvoir d’achat afin de mieux "
         "refléter le pouvoir d’achat réel des populations et d’éviter les "
         "distorsions liées aux taux de change de marché.",
    'p': "Le fait montre l’usage institutionnel de la convention et son rôle "
         "dans la mesure du développement."},
   {'f': "Dans la courbe de l’éléphant, les revenus sont mesurés en termes "
         "réels, déflatés, et en parité de pouvoir d’achat, de sorte que les "
         "résultats ne sont biaisés ni par l’inflation ni par les taux de "
         "change financiers.",
    'p': "Le fait montre que la parité de pouvoir d’achat se combine avec la "
         "déflation par les prix pour neutraliser deux biais distincts."},
   {'f': "Les BRICS élargis représentent environ 36 % du produit intérieur "
         "brut mondial en parité de pouvoir d’achat en 2022 et 25 % des "
         "exportations mondiales en 2021, tandis que la part relative du G7 "
         "diminue.",
    'p': "Les chiffres démontrent que la convention retenue change la "
         "hiérarchie mesurée des puissances économiques."},
   {'f': "La part de la Chine dans le produit intérieur brut mondial en "
         "parité de pouvoir d’achat augmente considérablement, la faisant "
         "passer d’un poids relativement faible à l’un des principaux pôles "
         "de l’économie mondiale.",
    'p': "Le fait montre l’enjeu analytique de la mesure : le basculement du "
         "centre de gravité économique mondial s’apprécie en parité de "
         "pouvoir d’achat."}],
  [{'q': "Sujet sur la comparaison internationale des niveaux de vie",
    'f': "Le cours impose une correction. Un simple taux de change de marché "
         "ne reflète pas correctement le niveau de vie réel, parce qu’il "
         "dépend de la spéculation, des marchés financiers, des mouvements "
         "de capitaux, des anticipations et des déséquilibres monétaires, et "
         "ne traduit pas nécessairement ce qu’un revenu permet réellement "
         "d’acheter. La parité de pouvoir d’achat permet au contraire de "
         "comparer le pouvoir d’achat réel, le volume de biens et services "
         "accessibles et le niveau de vie concret des populations.",
    'r': "On montre que la conversion monétaire introduit un biais "
         "systématique dans les comparaisons de revenu, ce qui impose une "
         "correction par les prix locaux.",
    'ex': "Un même revenu en dollars donnant des niveaux de vie très "
          "différents en Suisse et en Inde."},
   {'q': "Sujet sur la mesure du développement",
    'f': "Le cours explique un choix méthodologique de l’indicateur de "
         "développement humain : sa dimension monétaire est mesurée par le "
         "revenu national brut par habitant en parité de pouvoir d’achat, "
         "afin de mieux refléter le pouvoir d’achat réel des populations et "
         "d’éviter les distorsions liées aux taux de change de marché. Mais "
         "il ajoute que l’indicateur reste imparfait, puisqu’il donne une "
         "moyenne nationale sans dire comment les ressources sont réparties "
         "à l’intérieur du pays.",
    'r': "On montre que la parité de pouvoir d’achat corrige un biais de "
           "conversion sans corriger un biais de répartition, ce qui "
         "justifie les prolongements de l’indicateur.",
    'ex': "L’indicateur de développement humain ajusté aux inégalités, "
          "inférieur à l’indicateur simple dans tous les pays."},
   {'q': "Sujet sur le basculement du poids économique mondial",
    'f': "Le cours appuie ce diagnostic sur une mesure en parité de pouvoir "
         "d’achat. La part de la Chine dans le produit intérieur brut "
         "mondial en parité de pouvoir d’achat augmente considérablement, la "
         "faisant passer d’un poids relativement faible à l’un des "
         "principaux pôles de l’économie mondiale, tandis que la part "
         "relative du G7 diminue et que les BRICS élargis atteignent environ "
         "36 % du produit intérieur brut mondial en 2022.",
    'r': "On montre que la hiérarchie mesurée des puissances dépend de la "
           "convention de conversion retenue, ce qui impose de préciser "
         "l’unité de mesure avant tout diagnostic.",
    'ex': "Les 25 % des exportations mondiales détenues par les BRICS "
          "élargis en 2021."},
   {'q': "Sujet sur la mesure des inégalités mondiales",
    'f': "Le cours décrit la méthodologie de la courbe de l’éléphant de "
         "Branko Milanovic : en abscisse la population mondiale classée par "
         "revenu initial, en ordonnée le taux de croissance du revenu réel, "
         "les revenus étant mesurés en termes réels, déflatés, et en parité "
         "de pouvoir d’achat, de sorte que les résultats ne sont biaisés ni "
         "par l’inflation ni par les taux de change financiers. Trois "
         "groupes apparaissent alors.",
    'r': "On montre que la conclusion sur les gagnants et les perdants de la "
         "mondialisation dépend d’une double correction, par les prix et par "
         "la parité, ce qui en garantit la comparabilité internationale.",
    'ex': "Les plus pauvres du monde avec une croissance réelle d’environ "
          "+15 %, soit une amélioration limitée."}],
  voisins=['n20-taux-change-nominal-reel', 'n20-appreciation-depreciation',
           'n20-desequilibres-mondiaux', 'n20-balance-paiements'])
