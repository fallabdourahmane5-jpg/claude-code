# -*- coding: utf-8 -*-
"""Ensemble 22 — Les inégalités, la pauvreté et la justice sociale (1/5)."""

from doss_base import d

d('n22-inegalites-revenus', 22, "Inégalités de revenus",
  "Les écarts de revenu entre individus, mesurés par l’interdécile, le Palma et le Gini",
  "Les inégalités de revenus désignent les écarts de revenu entre les "
  "individus ou les ménages d’une population, le revenu étant un flux perçu "
  "sur une période donnée et comprenant les salaires, les revenus du "
  "capital et les prestations sociales. Le cours les mesure par trois "
  "indicateurs complémentaires — le rapport interdécile D9/D1, le "
  "coefficient de Palma et le coefficient de Gini construit sur la courbe "
  "de Lorenz — et distingue systématiquement les inégalités avant et après "
  "redistribution.",
  "Le cours aborde les inégalités de revenus par les outils de mesure, "
  "parce que l’ampleur constatée dépend de l’indicateur retenu. Le premier "
  "outil est le rapport interdécile. On classe la population par ordre "
  "croissant de revenu, on la divise en dix groupes de taille égale appelés "
  "déciles, et chaque seuil séparant deux groupes est un décile : D1 est le "
  "seuil en dessous duquel se situent les 10 % les plus pauvres, D9 le "
  "seuil au-dessus duquel se situent les 10 % les plus riches. Le rapport "
  "D9/D1 indique combien de fois les plus riches gagnent plus que les plus "
  "pauvres ; avec D1 = 1 200 € et D9 = 4 800 €, le rapport vaut 4. Le "
  "deuxième outil est le coefficient de Palma, qui compare la part du "
  "revenu détenue par les 10 % les plus riches à celle des 50 % les plus "
  "pauvres. Il est plus sensible que l’interdécile aux transformations "
  "contemporaines du sommet de la distribution et met en évidence la "
  "polarisation croissante des sociétés entre une élite restreinte et une "
  "large base de la population. Le cours précise ce que le Palma révèle "
  "depuis les années 1980 dans les économies développées : la part des 10 % "
  "les plus riches augmente, la part des 50 % les plus pauvres stagne ou "
  "diminue, la part des 40 % intermédiaires reste relativement stable. Le "
  "troisième outil est le coefficient de Gini, indicateur synthétique qui "
  "mesure la concentration des inégalités dans une distribution. Il est "
  "construit à partir de la courbe de Lorenz : en abscisse, la population "
  "cumulée de 0 % à 100 % ; en ordonnée, le revenu cumulé de 0 % à 100 %. "
  "Dans une société parfaitement égalitaire, 10 % de la population auraient "
  "10 % du revenu, 50 % en auraient 50 %, ce qui correspond à la droite "
  "d’équirépartition. Dans la réalité, 50 % de la population possèdent "
  "souvent bien moins que 50 % du revenu, et la courbe de Lorenz passe en "
  "dessous de cette droite : plus elle s’en éloigne, plus les inégalités "
  "sont fortes. Le Gini est compris entre 0 — égalité parfaite — et 1 — "
  "inégalité totale, une personne détenant tout. En pratique, les pays "
  "égalitaires se situent autour de 0,25 à 0,30 et les pays très "
  "inégalitaires entre 0,45 et 0,60 ; la France est autour de 0,29, soit "
  "environ 0,297 en 2023, ce qui correspond à des inégalités modérées mais "
  "persistantes. Le cours insiste enfin sur un deuxième partage, celui "
  "entre l’avant et l’après-redistribution : en France, les écarts de "
  "niveau de vie par unité de consommation en 2023 sont d’un facteur 18 "
  "avant redistribution et d’un facteur 4 après, 53 % des ménages étant "
  "bénéficiaires nets ; les ménages modestes voient leur revenu multiplié "
  "par 4 tandis que les plus aisés perdent environ 40 % de leur revenu "
  "initial à cause de la fiscalité et des cotisations.",
  [("La construction des déciles et le rapport interdécile",
    "La population est classée par revenu croissant puis divisée en dix "
    "groupes de 10 %. Les deux déciles clés sont D1, seuil en dessous "
    "duquel se trouvent les 10 % les plus pauvres, et D9, seuil au-dessus "
    "duquel se trouvent les 10 % les plus riches. Le rapport D9/D1 mesure "
    "l’écart entre les extrémités de la distribution : avec D1 = 1 200 € "
    "et D9 = 4 800 €, il vaut 4. L’indicateur est simple et parlant, mais "
    "il ne dit rien de ce qui se passe entre D1 et D9."),
   ("La courbe de Lorenz et la lecture graphique de la concentration",
    "On porte en abscisse la population cumulée et en ordonnée le revenu "
    "cumulé. La droite d’équirépartition représente l’égalité parfaite : "
    "x % de la population détiennent x % du revenu. La courbe réelle passe "
    "sous cette droite, et l’aire entre les deux mesure la concentration. "
    "Plus la courbe s’éloigne de la droite, plus les inégalités sont "
    "fortes. Le Gini formalise cet écart en un nombre compris entre 0 et "
    "1."),
   ("Le choix de l’indicateur comme choix de ce que l’on observe",
    "Les trois indicateurs ne répondent pas à la même question. "
    "L’interdécile compare deux groupes extrêmes. Le Palma compare le "
    "sommet aux 50 % du bas et capte donc la polarisation. Le Gini prend "
    "en compte l’ensemble de la distribution et mesure la concentration "
    "globale. Le cours en tire une conséquence méthodologique : un même "
    "mouvement des inégalités peut apparaître ou disparaître selon "
    "l’indicateur, ce qui interdit de conclure à partir d’un seul chiffre."),
   ("L’effet de la redistribution sur la distribution observée",
    "Les inégalités mesurées dépendent du moment où on les mesure. Avant "
    "impôts et transferts, les écarts de niveau de vie en France atteignent "
    "un facteur 18 ; après, un facteur 4. Le mécanisme est double : les "
    "prélèvements progressifs réduisent le haut — les plus aisés perdent "
    "environ 40 % de leur revenu initial — et les prestations relèvent le "
    "bas, les ménages modestes voyant leur revenu multiplié par 4. Au "
    "total, 53 % des ménages sont bénéficiaires nets.")],
  [{'a': "La mesure des inégalités de revenus dispose d’indicateurs "
         "rigoureux et complémentaires : le rapport interdécile D9/D1 "
         "compare les extrémités, le coefficient de Palma le sommet aux "
         "50 % du bas, et le coefficient de Gini synthétise la "
         "concentration de toute la distribution à partir de la courbe de "
         "Lorenz.",
    'cond': "La complémentarité n’est utile que si l’on explicite ce que "
            "chaque indicateur mesure : le Gini prend en compte "
            "l’ensemble de la distribution, contrairement à l’interdécile "
            "et au Palma qui ne comparent que des groupes précis.",
    'lim': "Chaque indicateur a un angle mort. Le Gini ne précise pas si "
           "les inégalités viennent du sommet, du bas ou des classes "
           "moyennes et peut rester stable alors que le top 1 % s’enrichit "
           "fortement. Le Palma ignore la distribution interne des 50 % "
           "intermédiaires et ne mesure pas la concentration globale."},
   {'a': "Le système fiscal et social français réduit fortement les "
         "inégalités de revenus : les écarts de niveau de vie par unité de "
         "consommation passent d’un facteur 18 avant redistribution à un "
         "facteur 4 après, et 53 % des ménages sont bénéficiaires nets du "
         "système.",
    'cond': "L’effet mesuré suppose de prendre en compte à la fois les "
            "prélèvements et les prestations, et de raisonner par unité de "
            "consommation pour neutraliser l’effet de la taille des "
            "ménages. Le cours ajoute que la redistribution est aussi en "
            "nature — école gratuite, soins remboursés, allocations "
            "logement — ce qui élève le niveau de vie élargi au-delà du "
            "revenu monétaire.",
    'lim': "Le cours note immédiatement l’asymétrie : le système fiscal et "
           "social réduit les inégalités de revenus mais beaucoup moins "
           "celles de patrimoine. La redistribution agit sur les flux, pas "
           "sur les stocks, et la concentration du capital persiste."},
   {'a': "La France présente des inégalités de revenus modérées en "
         "comparaison internationale, son coefficient de Gini se situant "
         "autour de 0,29 et à environ 0,297 en 2023, c’est-à-dire dans la "
         "fourchette de 0,25 à 0,30 qui caractérise les pays égalitaires et "
         "loin des 0,45 à 0,60 des pays très inégalitaires.",
    'cond': "La comparaison n’a de sens que si les Gini comparés portent "
            "sur la même grandeur — revenu disponible après redistribution "
            "plutôt que revenu primaire — et sur la même définition de "
            "l’unité d’observation.",
    'lim': "Un Gini modéré et stable peut masquer une forte dynamique au "
           "sommet, le cours relevant précisément que l’indicateur est "
           "insensible aux dynamiques internes fines et peut rester stable "
           "alors que le top 1 % s’enrichit. Les chiffres du seuil de "
           "richesse — 7 512 € par mois pour le 1 % le plus riche, 19 500 € "
           "pour le 0,1 %, 70 000 € pour le 0,01 % — montrent l’ampleur de "
           "ce que le Gini ne restitue pas."}],
  [{'t': "Un indicateur synthétique comme le coefficient de Gini écrase la "
         "réalité qu’il prétend décrire, puisque deux distributions très "
         "différentes peuvent produire la même valeur et qu’une hausse "
         "concentrée au sommet peut le laisser inchangé.",
    'qui': "le cours, dans son énoncé des limites du Gini",
    'rep': "Le cours formule la critique lui-même et en tire une méthode "
           "plutôt qu’un rejet. Il énumère trois limites : le Gini ignore "
           "l’origine précise des écarts — sommet, bas ou classes "
           "moyennes —, il simplifie comme tout indicateur synthétique, et "
           "il est insensible aux dynamiques internes fines, pouvant rester "
           "stable alors que le top 1 % s’enrichit fortement. La réponse "
           "est l’usage conjoint : le Palma, plus sensible au sommet, "
           "capte précisément ce que le Gini manque, et l’interdécile "
           "donne un ordre de grandeur immédiatement interprétable."},
   {'t': "Mesurer les inégalités après redistribution conduit à sous-estimer "
         "les inégalités réellement produites par l’économie, puisque le "
         "système socio-fiscal masque la distribution primaire sans la "
         "corriger durablement.",
    'qui': "le cours, lorsqu’il compare les écarts avant et après "
           "redistribution et souligne la persistance des inégalités de "
           "patrimoine",
    'rep': "Le cours présente les deux mesures et refuse de choisir : "
           "l’écart de facteur 18 avant redistribution décrit ce que "
           "produit le marché, l’écart de facteur 4 après décrit ce que "
           "vivent les ménages. Les deux sont nécessaires, et c’est leur "
           "comparaison qui mesure l’intensité de la redistribution. Il "
           "ajoute cependant une limite décisive : la redistribution "
           "monétaire et en nature améliore le niveau de vie élargi des "
           "ménages modestes, mais la concentration du capital et la hausse "
           "des grandes fortunes montrent que les inégalités structurelles "
           "persistent."},
   {'t': "La hausse des inégalités de revenus depuis les années 1980 serait "
         "une conséquence mécanique de la technologie et de la "
         "mondialisation, qui échapperait largement aux politiques "
         "publiques.",
    'qui': "Thomas Piketty, qui insiste au contraire sur les facteurs "
           "politiques et institutionnels",
    'rep': "Le cours tranche en faveur de Piketty. Pour lui, la hausse des "
           "inégalités n’est pas simplement une conséquence automatique de "
           "la technologie ou de la mondialisation : elle dépend fortement "
           "des choix politiques. Le cours donne les décisions concrètes "
           "en cause depuis les années 1980 : diminution de certains taux "
           "marginaux supérieurs d’imposition, réduction de certaines "
           "formes de taxation du capital, modification des systèmes "
           "redistributifs. La dynamique des inégalités dépend donc "
           "fondamentalement des institutions fiscales, sociales et "
           "politiques qui déterminent la répartition des revenus et du "
           "patrimoine."}],
  [{'n': "Max Lorenz",
    'i': "La répartition d’une variable dans une population se représente "
         "par une courbe comparée à la droite d’équirépartition.",
    'p': "La courbe de Lorenz porte en abscisse la population cumulée et "
         "en ordonnée le revenu ou le patrimoine cumulé. L’égalité "
         "parfaite correspond à la diagonale : 10 % de la population "
         "détiennent 10 % du revenu, 50 % en détiennent 50 %. La courbe "
         "réelle passe sous cette diagonale, et son éloignement mesure "
         "visuellement la concentration. Cette représentation est le "
         "support de construction du coefficient de Gini et permet de "
         "comparer directement distribution des revenus et distribution "
         "des patrimoines."},
   {'n': "Palma",
    'i': "La polarisation contemporaine se lit mieux en comparant le "
         "sommet aux 50 % du bas qu’en comparant les deux déciles "
         "extrêmes.",
    'p': "Le coefficient de Palma rapporte la part du revenu détenue par "
         "les 10 % les plus riches à celle détenue par les 50 % les plus "
         "pauvres. Son intérêt vient d’un constat empirique que le cours "
         "rapporte : dans les économies développées depuis les années "
         "1980, la part des 10 % les plus riches augmente, celle des 50 % "
         "les plus pauvres stagne ou diminue, celle des 40 % "
         "intermédiaires reste relativement stable. L’indicateur est donc "
         "construit pour capter précisément la zone où les choses bougent."},
   {'n': "Thomas Piketty",
    'i': "La dynamique des inégalités dépend des institutions fiscales et "
         "politiques, non des seules forces du marché.",
    'p': "Piketty insiste sur les facteurs politiques et institutionnels : "
         "la hausse des inégalités depuis les années 1980 n’est pas une "
         "conséquence automatique de la technologie ou de la "
         "mondialisation mais résulte de choix — baisse de certains taux "
         "marginaux supérieurs d’imposition, réduction de certaines formes "
         "de taxation du capital, modification des systèmes redistributifs. "
         "Le cours en tire la formule que les inégalités sont aussi un "
         "choix de société, et range Piketty du côté d’une lecture "
         "patrimoniale et critique, par contraste avec la version "
         "optimiste de Kuznets."}],
  [{'f': "Le coefficient de Gini est compris entre 0, égalité parfaite, et "
          "1, inégalité totale ; les pays égalitaires se situent autour de "
          "0,25 à 0,30 et les pays très inégalitaires entre 0,45 et 0,60.",
    'p': "Cette échelle donne le repère sans lequel une valeur de Gini "
         "n’est pas interprétable, et elle montre que l’écart entre les "
         "sociétés les plus et les moins égalitaires est considérable mais "
         "borné."},
   {'f': "La France affiche un coefficient de Gini autour de 0,29, soit "
          "environ 0,297 en 2023, ce qui la situe dans la fourchette des "
          "pays égalitaires avec des inégalités modérées mais persistantes.",
    'p': "Le chiffre sert de point de comparaison dans toute dissertation "
         "sur les inégalités françaises, et le qualificatif du cours — "
         "modérées mais persistantes — interdit à la fois l’alarmisme et "
         "la satisfaction."},
   {'f': "En France, les écarts de niveau de vie par unité de consommation "
          "en 2023 sont d’un facteur 18 avant redistribution et d’un "
          "facteur 4 après ; 53 % des ménages sont bénéficiaires nets.",
    'p': "C’est la mesure la plus directe de l’intensité de la "
         "redistribution française : elle divise l’écart initial par plus "
         "de quatre, et elle bénéficie à la majorité des ménages, ce qui "
         "éclaire aussi sa légitimité politique."},
   {'f': "Les ménages modestes voient leur revenu multiplié par 4 par la "
          "redistribution, tandis que les plus aisés perdent environ 40 % "
          "de leur revenu initial à cause de la fiscalité et des "
          "cotisations.",
    'p': "Ce double mouvement montre que la réduction de l’écart ne vient "
         "pas d’un seul côté : elle résulte simultanément du relèvement du "
         "bas par les prestations et de l’écrêtement du haut par les "
         "prélèvements."},
   {'f': "Les chiffres du seuil de richesse en France : 7 512 € par mois "
          "pour le 1 % le plus riche, 19 500 € pour le 0,1 % et 70 000 € "
          "pour le 0,01 %.",
    'p': "Cette progression très rapide à l’intérieur du dernier centile "
         "illustre exactement ce que les indicateurs synthétiques "
         "manquent : l’essentiel de la dispersion du sommet se joue dans "
         "une fraction de population que le Gini ne distingue pas."}],
  [{'q': "Comment mesurer les inégalités de revenus ?",
    'f': "La réponse consiste à présenter les trois indicateurs du cours en "
         "montrant que chacun répond à une question différente, puis à "
         "ajouter la distinction avant/après redistribution. Le rapport "
         "interdécile D9/D1 compare les 10 % les plus riches aux 10 % les "
         "plus pauvres : avec D1 = 1 200 € et D9 = 4 800 €, il vaut 4, ce "
         "qui est immédiatement interprétable mais ne dit rien de "
         "l’intérieur de la distribution. Le coefficient de Palma rapporte "
         "la part des 10 % les plus riches à celle des 50 % les plus "
         "pauvres ; il est construit pour la dynamique observée depuis les "
         "années 1980, où la part du sommet augmente, celle des 50 % du bas "
         "stagne ou diminue et celle des 40 % intermédiaires reste stable. "
         "Le coefficient de Gini, construit sur la courbe de Lorenz, "
         "synthétise la concentration de toute la distribution entre 0 et "
         "1 ; la France est autour de 0,29, les pays égalitaires entre 0,25 "
         "et 0,30, les très inégalitaires entre 0,45 et 0,60. Il faut "
         "enfin préciser le moment de la mesure : les écarts de niveau de "
         "vie français sont d’un facteur 18 avant redistribution et de 4 "
         "après. On conclut qu’aucun indicateur ne suffit seul et que le "
         "choix de l’outil est déjà une décision sur ce que l’on veut voir.",
    'r': "Ce raisonnement est préférable à l’exposé d’un seul indicateur "
         "parce que le cours documente précisément les angles morts : le "
         "Gini peut rester stable alors que le top 1 % s’enrichit "
         "fortement, le Palma ignore les 50 % intermédiaires, "
         "l’interdécile ignore tout ce qui se passe entre D1 et D9. Un "
         "sujet sur les inégalités mal mesuré est un sujet mal traité.",
    'ex': "Les seuils de richesse — 7 512 € pour le 1 %, 70 000 € pour le "
          "0,01 % — montrent une dispersion interne au sommet qu’aucun "
          "indicateur synthétique ne restitue."},
   {'q': "Les inégalités de revenus ont-elles augmenté ?",
    'f': "La réponse exige de séparer les niveaux et les échelles. Au "
         "niveau national français, le Gini reste modéré, autour de 0,29 et "
         "environ 0,297 en 2023, et la redistribution continue de diviser "
         "les écarts par plus de quatre, de 18 à 4. Dans les économies "
         "développées prises ensemble, en revanche, le cours constate un "
         "retour des inégalités depuis les années 1980 : hausse des "
         "inégalités de revenus, forte concentration des patrimoines, "
         "explosion du top 1 %, et une dynamique de Palma où la part des "
         "10 % les plus riches augmente tandis que celle des 50 % les plus "
         "pauvres stagne ou diminue. À l’échelle mondiale, la réponse "
         "s’inverse encore : Milanovic établit que les inégalités entre "
         "pays diminuent tandis que les inégalités au sein des pays "
         "augmentent. La cause du mouvement est elle-même disputée, et le "
         "cours tranche avec Piketty : la hausse ne découle pas "
         "automatiquement de la technologie ou de la mondialisation mais "
         "dépend de choix politiques — baisse de certains taux marginaux "
         "supérieurs, réduction de certaines formes de taxation du capital, "
         "modification des systèmes redistributifs.",
    'r': "Cette architecture par échelles évite la contradiction apparente "
         "entre un Gini français stable et un discours général de hausse "
         "des inégalités : les deux sont vrais parce qu’ils portent sur des "
         "populations différentes. Elle prépare aussi la discussion sur la "
         "courbe de Kuznets, puisque le retour des inégalités après 1980 "
         "contredit la phase descendante que celle-ci prévoyait.",
    'ex': "Le constat du cours pour les pays développés depuis 1980 : "
          "hausse des inégalités de revenus, forte concentration des "
          "patrimoines, explosion du top 1 %."}],
  voisins=['n22-inegalites-patrimoine', 'n22-inegalites-entre-et-au-sein',
           'n22-courbe-kuznets', 'n22-redistribution',
           'n22-repartition-primaire'])


d('n22-inegalites-patrimoine', 22, "Inégalités de patrimoine",
  "La concentration des stocks de richesse, systématiquement plus forte que celle des revenus",
  "Les inégalités de patrimoine désignent les écarts dans la détention de "
  "richesses accumulées — biens immobiliers, actifs financiers, épargne, "
  "capital productif —, le patrimoine étant un stock et non un flux. Le "
  "cours établit deux résultats : les inégalités de patrimoine sont "
  "systématiquement plus fortes que les inégalités de revenus, et le "
  "système fiscal et social les réduit beaucoup moins, parce qu’elles "
  "reposent sur une logique cumulative et sur la transmission "
  "intergénérationnelle.",
  "Le cours construit la notion par opposition au revenu. Le revenu est un "
  "flux : une somme perçue sur une période donnée, mesurée annuellement, "
  "comprenant les salaires, les revenus du capital et les prestations "
  "sociales. Le patrimoine est un stock : l’ensemble des richesses détenues "
  "à un moment donné, comprenant les biens immobiliers, les actifs "
  "financiers, l’épargne et le capital productif, accumulé dans le temps. "
  "De cette différence de nature découle un constat empirique que le cours "
  "présente comme systématique : les données issues de la courbe de Lorenz "
  "montrent que les inégalités de patrimoine sont systématiquement plus "
  "fortes que les inégalités de revenus — les 10 % les plus riches "
  "concentrent une part très importante du patrimoine total tandis qu’une "
  "large fraction de la population en détient une part très faible. Le "
  "cours explique ensuite pourquoi le patrimoine accentue les inégalités, "
  "par deux mécanismes. Le premier est cumulatif : le patrimoine génère du "
  "revenu — loyers, intérêts, dividendes — et ces revenus permettent "
  "d’accumuler davantage de capital. Le second est la transmission "
  "intergénérationnelle : le patrimoine peut être transmis par héritage ou "
  "par donation, de sorte que la concentration tend à se reproduire dans le "
  "temps. Les données françaises illustrent l’ampleur du phénomène. En "
  "1986, le patrimoine du cinquantième plus riche s’élevait à 1,4 million "
  "d’euros ; en 2025, le patrimoine total des dix plus riches atteint 2 612 "
  "milliards d’euros, soit 42 % du PIB français d’environ 4 350 milliards, "
  "contre 6 % en 1996. Le cours résume par un constat de divergence : la "
  "variation de la richesse dépasse très largement la variation du SMIC, "
  "1 300 % contre 86 %. La lecture économique et sociale qu’il en tire est "
  "nette : le système fiscal et social réduit les inégalités de revenus, "
  "mais beaucoup moins celles de patrimoine ; la redistribution monétaire "
  "et en nature — allocations, santé, éducation — aide les ménages modestes "
  "à améliorer leur niveau de vie élargi, mais la concentration du capital "
  "et la hausse des grandes fortunes montrent que les inégalités "
  "structurelles persistent. Le cours présente enfin les débats fiscaux qui "
  "en découlent : la taxe Zucman, taxe plancher de 2 % sur le patrimoine "
  "visant les familles dont le patrimoine dépasse 100 millions d’euros, "
  "soit 1 800 foyers fiscaux, et les trois réformes proposées par Xavier "
  "Jaravel sur les plus-values latentes, les holdings familiaux et le pacte "
  "Dutreil.",
  [("La différence de nature entre un stock et un flux",
    "Le revenu est mesuré sur une période — un an — et se renouvelle ; le "
    "patrimoine est mesuré à une date et résulte d’une accumulation "
    "passée. Cette différence suffit à expliquer une partie de l’écart de "
    "concentration : un flux annuel est borné par la capacité de gain "
    "d’une année, tandis qu’un stock intègre l’ensemble des années "
    "antérieures, et les écarts annuels se composent au lieu de "
    "s’additionner."),
   ("La logique cumulative du patrimoine",
    "Le patrimoine génère du revenu sous forme de loyers, d’intérêts et de "
    "dividendes, et ces revenus permettent d’accumuler davantage de "
    "capital. Le mécanisme est auto-renforçant : plus le patrimoine "
    "initial est élevé, plus le revenu qu’il procure est élevé, plus la "
    "capacité d’épargne et donc d’accumulation est grande. Le cours en "
    "déduit que la concentration du patrimoine n’est pas un état mais une "
    "dynamique."),
   ("La transmission intergénérationnelle",
    "Le patrimoine peut être transmis par héritage ou par donation. La "
    "conséquence que le cours tire explicitement est que la concentration "
    "tend à se reproduire dans le temps : la position patrimoniale d’une "
    "génération conditionne celle de la suivante, indépendamment des "
    "revenus du travail. C’est le point sur lequel Thomas Piketty insiste "
    "en montrant que l’héritage a retrouvé une place centrale dans la "
    "formation du patrimoine."),
   ("L’asymétrie de la redistribution entre revenus et patrimoine",
    "Le système socio-fiscal agit principalement sur les flux : impôt sur "
    "le revenu progressif, cotisations, prestations. Il réduit donc "
    "fortement les inégalités de revenus — d’un facteur 18 à un facteur 4 "
    "en France — mais beaucoup moins celles de patrimoine, qui "
    "échapperaient à cette mécanique. C’est précisément ce que visent les "
    "propositions de taxation du stock, comme la taxe plancher de 2 % sur "
    "le patrimoine, et la taxation des plus-values latentes au moment de "
    "la transmission.")],
  [{'a': "Les inégalités de patrimoine sont systématiquement plus fortes "
         "que les inégalités de revenus, les données issues de la courbe de "
         "Lorenz montrant que les 10 % les plus riches concentrent une part "
         "très importante du patrimoine total tandis qu’une large fraction "
         "de la population en détient une part très faible.",
    'cond': "Le constat suppose de comparer les deux distributions avec le "
            "même outil, ce que permet la courbe de Lorenz puisqu’elle "
            "s’applique indifféremment aux revenus et aux patrimoines, et "
            "de prendre le patrimoine net plutôt que brut.",
    'lim': "La mesure du patrimoine est beaucoup plus difficile que celle "
           "du revenu, et le cours le montre à propos de la taxe Zucman : "
           "pour les grandes entreprises cotées comme LVMH ou Hermès, la "
           "valeur repose sur la capitalisation boursière à un moment "
           "donné ; pour les start-ups et les entreprises non cotées, la "
           "richesse est virtuelle, dépendant de la valeur que les "
           "investisseurs attribuent à l’entreprise."},
   {'a': "La concentration patrimoniale française s’est accentuée de "
         "manière spectaculaire : le patrimoine total des dix plus riches "
         "atteint 2 612 milliards d’euros en 2025, soit 42 % du PIB "
         "français d’environ 4 350 milliards, contre 6 % en 1996.",
    'cond': "L’interprétation du chiffre suppose de rapporter le stock à "
            "une grandeur de référence, ici le PIB, et de garder en tête "
            "qu’une partie de la hausse reflète la valorisation boursière "
            "des actifs plus que l’accumulation de nouvelle épargne.",
    'lim': "Le rapport patrimoine/PIB compare un stock et un flux annuel, "
           "ce qui gonfle visuellement le ratio. Le cours corrige en "
           "ajoutant une comparaison homogène de dynamiques : la variation "
           "de la richesse, 1 300 %, face à celle du SMIC, 86 %."},
   {'a': "La taxation du patrimoine répond à une asymétrie réelle du "
         "système français, puisque le cours constate que le système fiscal "
         "et social réduit les inégalités de revenus mais beaucoup moins "
         "celles de patrimoine, et que la fiscalité des flux laisse "
         "intactes les plus-values non réalisées.",
    'cond': "L’efficacité d’une telle taxation suppose de résoudre le "
            "problème de l’évaluation et de traiter le cas des "
            "contribuables riches en patrimoine mais pauvres en revenus — "
            "l’argument utilisé contre l’impôt sur la fortune immobilière, "
            "certains propriétaires ne pouvant vendre leur bien pour payer "
            "l’impôt chaque année.",
    'lim': "Le cours énumère trois critiques de la taxe Zucman. "
           "L’efficacité est discutée : les 20 milliards évalués sont "
           "jugés surévalués et pèsent peu face aux 170 milliards de "
           "déficit, et la taxe peut provoquer une fuite des capitaux. Les "
           "effets pervers sont réels : hausse de la taxe → baisse de "
           "l’investissement, et réduction du patrimoine → réduction de "
           "l’assiette fiscale des plus riches les années suivantes. "
           "S’ajoute la question de justice et de constitutionnalité."}],
  [{'t': "La taxation du patrimoine est inefficace et contre-productive : "
         "son rendement est surestimé, elle décourage l’investissement et "
         "elle réduit sa propre assiette en poussant les contribuables "
         "concernés à expatrier leurs capitaux.",
    'qui': "le cours, dans les trois grandes critiques qu’il adresse à la "
           "taxe Zucman",
    'rep': "Le cours expose la critique complètement — rendement de 20 "
           "milliards jugé surévalué et faible au regard des 170 milliards "
           "de déficit, risque de fuite des capitaux, enchaînement hausse "
           "de la taxe → baisse de l’investissement et réduction du "
           "patrimoine → réduction de l’assiette — puis il en relativise "
           "la portée. D’une part, l’objectif invoqué n’est pas seulement "
           "budgétaire mais d’équité, le cours parlant de restaurer "
           "l’équité fiscale entre revenus du travail et du capital. "
           "D’autre part, Xavier Jaravel propose trois réformes "
           "alternatives qui contournent l’objection d’assiette : taxer "
           "les plus-values latentes au moment de la transmission, taxer "
           "les holdings familiaux comme le font les États-Unis, réformer "
           "le pacte Dutreil."},
   {'t': "La taxation du stock patrimonial pose un problème de justice et "
         "de constitutionnalité, parce qu’elle frappe une richesse dont la "
         "valeur est incertaine et parfois virtuelle, et qu’elle peut "
         "atteindre des contribuables sans liquidités pour la payer.",
    'qui': "le cours, dans son examen de la question de justice et de "
           "constitutionnalité de la taxe Zucman",
    'rep': "Le cours prend la critique au sérieux et en détaille les deux "
           "versants. Le problème d’évaluation : pour les grandes "
           "entreprises cotées comme LVMH ou Hermès, la valeur repose sur "
           "la capitalisation boursière, c’est-à-dire le prix des actions "
           "à un moment donné ; pour les start-ups et les entreprises non "
           "cotées, la richesse est virtuelle et dépend de la valeur "
           "attribuée par les investisseurs. Le problème de liquidité : "
           "certains propriétaires sont riches en patrimoine mais pauvres "
           "en revenus et ne peuvent pas vendre leur bien pour payer "
           "l’impôt chaque année, argument utilisé contre l’impôt sur la "
           "fortune immobilière. La réponse du cours n’est pas de renoncer "
           "mais de déplacer le moment de l’imposition vers la "
           "transmission, où la liquidité est disponible."},
   {'t': "La concentration du patrimoine serait le résultat normal de "
         "l’épargne accumulée au cours d’un cycle de vie, et non le produit "
         "d’une transmission héréditaire, de sorte qu’elle ne poserait pas "
         "de problème particulier d’équité.",
    'qui': "Thomas Piketty, qui critique sur ce point l’analyse de Franco "
           "Modigliani",
    'rep': "Le cours restitue le débat. Modigliani expliquait que dans les "
           "années 1950, surtout aux États-Unis, la majorité de la "
           "richesse provenait de l’épargne accumulée au cours de la vie "
           "et non de l’héritage. Piketty a montré que cette période était "
           "en réalité une exception historique et que l’héritage a "
           "retrouvé une place centrale dans la formation du patrimoine. "
           "La portée de la correction est considérable : si le patrimoine "
           "vient de l’épargne de cycle de vie, la concentration se défait "
           "à chaque génération ; s’il vient de l’héritage, elle se "
           "reproduit, ce qui est exactement le mécanisme de transmission "
           "intergénérationnelle décrit par le cours."}],
  [{'n': "Thomas Piketty",
    'i': "L’héritage a retrouvé une place centrale dans la formation du "
         "patrimoine, contrairement à ce que suggérait l’après-guerre.",
    'p': "Piketty montre que la période des années 1950, où la majorité de "
         "la richesse américaine provenait de l’épargne accumulée au cours "
         "de la vie — l’analyse de Modigliani —, constituait une exception "
         "historique. L’héritage est redevenu un déterminant majeur du "
         "patrimoine, ce qui change la nature du problème : la "
         "concentration ne se défait plus à chaque génération mais se "
         "reproduit. Le cours relie cette thèse à son insistance sur les "
         "facteurs politiques et institutionnels, la baisse des taux "
         "marginaux supérieurs et la réduction de la taxation du capital "
         "depuis les années 1980."},
   {'n': "Gabriel Zucman",
    'i': "Une taxe plancher sur le patrimoine des très grandes fortunes "
         "permettrait de corriger la régressivité du haut de la "
         "distribution.",
    'p': "La taxe Zucman s’applique aux familles dont le patrimoine dépasse "
         "100 millions d’euros, soit 1 800 foyers fiscaux. C’est une taxe "
         "différentielle — les personnes concernées retirent les taxes déjà "
         "payées pour déterminer le reste à payer — et une taxe plancher, "
         "au taux de 2 % sur le patrimoine, immobilier et professionnel "
         "inclus. Le cours en donne les trois critiques : efficacité "
         "discutée avec 20 milliards jugés surévalués, effets pervers sur "
         "l’investissement et l’assiette, et question de justice et de "
         "constitutionnalité liée à l’évaluation du patrimoine."},
   {'n': "Xavier Jaravel",
    'i': "Trois réformes ciblées permettraient d’atteindre le patrimoine "
         "des plus riches sans les difficultés d’une taxe sur le stock.",
    'p': "Jaravel propose d’abord de taxer les plus-values latentes sur les "
         "actions et les héritages, c’est-à-dire les gains non encore "
         "réalisés : en France, l’impôt n’est dû qu’à la vente, de sorte "
         "que les plus riches peuvent conserver leurs actions toute leur "
         "vie et, lors de la transmission, la plus-value accumulée n’est "
         "pas imposée ; il propose donc de taxer la différence entre la "
         "valeur d’achat et la valeur au moment de l’héritage ou de la "
         "donation. Il propose ensuite de taxer les holdings familiaux, non "
         "taxés en Europe mais imposés normalement aux États-Unis, "
         "l’objectif étant d’empêcher les très riches de transformer leurs "
         "revenus en capital non imposé et de restaurer l’équité fiscale "
         "entre revenus du travail et du capital. Il propose enfin de "
         "réformer le pacte Dutreil, qui exonère jusqu’à 75 %, voire 95 % "
         "dans certains cas, de la valeur d’une entreprise familiale "
         "transmise si les héritiers s’engagent à la conserver au moins "
         "six ans, et dont certaines grandes fortunes profitent pour "
         "transmettre d’énormes patrimoines presque sans impôt."},
   {'n': "Franco Modigliani",
    'i': "Le patrimoine résulte principalement de l’épargne accumulée au "
         "cours du cycle de vie.",
    'p': "Modigliani expliquait que dans les années 1950, surtout aux "
         "États-Unis, la majorité de la richesse provenait de l’épargne "
         "accumulée au cours de la vie et non de l’héritage. Le cours "
         "mobilise cette thèse comme point de départ nécessaire — elle "
         "fournit le modèle de référence du comportement patrimonial — "
         "avant d’en présenter les critiques, dont celle de Piketty sur le "
         "retour de l’héritage et celle qui porte sur l’hypothèse d’un "
         "accès facile au crédit pour les jeunes, contestée dès lors que "
         "les banques restreignent leurs conditions."}],
  [{'f': "Le revenu est un flux — salaires, revenus du capital, prestations "
          "sociales, mesuré annuellement — tandis que le patrimoine est un "
          "stock — biens immobiliers, actifs financiers, épargne, capital "
          "productif — accumulé dans le temps.",
    'p': "Cette distinction est la clé de tout le dossier : elle explique "
         "pourquoi les deux distributions n’ont pas la même concentration "
         "et pourquoi un système fiscal assis sur les flux agit peu sur "
         "les stocks."},
   {'f': "En 1986, le patrimoine du cinquantième plus riche s’élevait à "
          "1,4 million d’euros ; en 2025, le patrimoine total des dix plus "
          "riches atteint 2 612 milliards d’euros, soit 42 % du PIB "
          "français, contre 6 % en 1996.",
    'p': "Ces chiffres datent précisément la rupture : ce n’est pas le "
         "niveau de concentration qui est inédit mais sa vitesse de "
         "croissance, le ratio au PIB ayant été multiplié par sept en une "
         "trentaine d’années."},
   {'f': "La variation de la richesse atteint 1 300 % quand celle du SMIC "
          "atteint 86 %, ce que le cours résume par le constat variation de "
          "la richesse supérieure à variation du SMIC.",
    'p': "Cette comparaison est homogène, puisqu’elle oppose deux taux de "
         "croissance sur la même période, et elle fournit l’argument le "
         "plus direct sur la divergence entre revenus du travail et "
         "patrimoine."},
   {'f': "La taxe Zucman viserait les familles dont le patrimoine dépasse "
          "100 millions d’euros, soit 1 800 foyers fiscaux, sous la forme "
          "d’une taxe plancher différentielle de 2 % sur le patrimoine, "
          "pour un rendement évalué à 20 milliards d’euros.",
    'p': "Ces ordres de grandeur permettent de poser le débat avec "
         "précision : un nombre très restreint de contribuables, un taux "
         "modeste, et un rendement à comparer aux 170 milliards de déficit "
         "que le cours met en regard."},
   {'f': "Le pacte Dutreil exonère jusqu’à 75 %, voire 95 % dans certains "
          "cas, de la valeur d’une entreprise familiale transmise, si les "
          "héritiers s’engagent à la conserver pendant au moins six ans.",
    'p': "Ce dispositif illustre le mécanisme concret par lequel la "
         "transmission échappe à l’imposition : l’objectif initial, éviter "
         "la vente d’entreprises familiales au moment d’une succession, "
         "est légitime, mais l’exonération permet de transmettre d’énormes "
         "patrimoines presque sans impôt."}],
  [{'q': "Pourquoi les inégalités de patrimoine sont-elles plus fortes que "
         "les inégalités de revenus ?",
    'f': "Trois raisons s’enchaînent. La première est de nature : le revenu "
         "est un flux borné par la capacité de gain d’une année, tandis que "
         "le patrimoine est un stock qui intègre toutes les années "
         "antérieures ; les écarts annuels s’y composent au lieu de "
         "s’additionner. La deuxième est cumulative : le patrimoine génère "
         "du revenu — loyers, intérêts, dividendes — et ces revenus "
         "permettent d’accumuler davantage de capital, ce qui rend la "
         "concentration auto-renforçante. La troisième est "
         "intergénérationnelle : le patrimoine se transmet par héritage ou "
         "par donation, de sorte que la concentration se reproduit dans le "
         "temps, et Thomas Piketty a montré que l’héritage avait retrouvé "
         "une place centrale, la période décrite par Modigliani où la "
         "richesse venait surtout de l’épargne de cycle de vie n’étant "
         "qu’une exception historique. S’y ajoute une raison "
         "institutionnelle : le système fiscal et social réduit les "
         "inégalités de revenus mais beaucoup moins celles de patrimoine, "
         "parce qu’il est assis sur les flux. Les chiffres français "
         "confirment : écart de niveau de vie ramené d’un facteur 18 à un "
         "facteur 4 par la redistribution, mais patrimoine des dix plus "
         "riches passé de 6 % du PIB en 1996 à 42 % en 2025.",
    'r': "L’articulation de ces raisons est ce qui donne sa force au "
         "raisonnement : la première explique un écart permanent, la "
         "deuxième une divergence croissante, la troisième une "
         "reproduction, la quatrième l’absence de correction. Un sujet "
         "traité avec une seule d’entre elles manque le caractère "
         "cumulatif du phénomène.",
    'ex': "Variation de la richesse 1 300 % contre variation du SMIC 86 % : "
          "la divergence porte sur les dynamiques, pas seulement sur les "
          "niveaux."},
   {'q': "Faut-il taxer davantage le patrimoine ?",
    'f': "Le point de départ est l’asymétrie constatée par le cours : le "
         "système fiscal et social réduit les inégalités de revenus mais "
         "beaucoup moins celles de patrimoine, et la concentration du "
         "capital ainsi que la hausse des grandes fortunes montrent que les "
         "inégalités structurelles persistent. Cela fonde l’argument de "
         "l’équité fiscale entre revenus du travail et du capital. Trois "
         "objections doivent cependant être traitées. L’efficacité : les 20 "
         "milliards attendus de la taxe Zucman sont jugés surévalués et "
         "représentent peu face aux 170 milliards de déficit, avec un "
         "risque de fuite des capitaux. Les effets pervers : hausse de la "
         "taxe → baisse de l’investissement, et réduction du patrimoine → "
         "réduction de l’assiette fiscale des plus riches les années "
         "suivantes. La justice et la constitutionnalité : l’évaluation du "
         "patrimoine repose sur la capitalisation boursière pour LVMH ou "
         "Hermès et sur une valeur virtuelle pour les sociétés non cotées, "
         "et certains contribuables sont riches en patrimoine mais pauvres "
         "en revenus. La réponse que le cours privilégie consiste moins à "
         "taxer le stock qu’à taxer les moments où il devient liquide ou "
         "change de main : les trois réformes de Xavier Jaravel portent sur "
         "les plus-values latentes au moment de la transmission, les "
         "holdings familiaux et le pacte Dutreil.",
    'r': "Cette résolution est plus solide qu’un oui ou un non parce "
         "qu’elle fait porter la discussion sur l’assiette et le moment de "
         "l’imposition, qui sont précisément les points où les objections "
         "d’évaluation et de liquidité tombent. Taxer la plus-value au "
         "moment de l’héritage résout à la fois le problème de la liquidité "
         "et celui de la valeur, puisque la transmission fournit une "
         "valorisation.",
    'ex': "Le pacte Dutreil, qui exonère jusqu’à 75 % voire 95 % de la "
          "valeur d’une entreprise transmise et permet de transmettre "
          "d’énormes patrimoines presque sans impôt."}],
  voisins=['n22-inegalites-revenus', 'n22-heritage', 'n22-rente',
           'n22-fiscalite-progressive', 'n22-redistribution'],
  comp={'titre': "Revenus et patrimoine : deux logiques différentes",
        'a': "Revenus", 'b': "Patrimoine",
        'lignes': [
          ("Nature", "Flux perçu sur une période donnée",
           "Stock de richesses détenues à un moment donné"),
          ("Périodicité de mesure", "Mesuré annuellement",
           "Accumulé dans le temps, mesuré à une date"),
          ("Composantes", "Salaires, revenus du capital, prestations sociales",
           "Biens immobiliers, actifs financiers, épargne, capital productif"),
          ("Concentration", "Plus faible ; Gini français autour de 0,29",
           "Systématiquement plus forte selon la courbe de Lorenz"),
          ("Dynamique propre", "Bornée par la capacité de gain annuelle",
           "Cumulative : loyers, intérêts et dividendes nourrissent "
           "l’accumulation"),
          ("Transmission", "Non transmissible en tant que flux",
           "Transmis par héritage ou donation ; la concentration se "
           "reproduit"),
          ("Effet de la redistribution",
           "Forte : écart de niveau de vie ramené d’un facteur 18 à 4",
           "Beaucoup plus faible ; les inégalités structurelles persistent"),
          ("Instruments fiscaux mobilisés",
           "Impôt progressif sur le revenu, cotisations, CSG",
           "Taxe plancher de 2 %, plus-values latentes, holdings, pacte "
           "Dutreil"),
          ("Difficulté de mesure", "Relativement faible, revenus déclarés",
           "Élevée : capitalisation boursière, richesse virtuelle des "
           "sociétés non cotées")]})


d('n22-inegalites-entre-et-au-sein', 22,
  "Inégalités entre pays et au sein des pays",
  "La double dynamique de la mondialisation : convergence entre nations, divergence interne",
  "Cette notion désigne la décomposition des inégalités mondiales en deux "
  "composantes : les écarts de niveau de vie moyen entre nations et les "
  "écarts entre individus à l’intérieur d’un même pays. Le cours en fait un "
  "paradoxe central de la mondialisation, établi par Branko Milanovic : les "
  "inégalités entre pays diminuent tandis que les inégalités à l’intérieur "
  "des pays augmentent. L’outil de décomposition est l’indice de Theil, "
  "l’outil de lecture la courbe de l’éléphant.",
  "Le cours part d’un problème de mesure. Pour analyser précisément les "
  "inégalités mondiales, il faut distinguer les écarts entre pays des "
  "écarts internes aux pays, et c’est l’intérêt de l’indice de Theil. Comme "
  "le coefficient de Gini, une faible valeur signale une faible inégalité "
  "et une valeur élevée une forte inégalité, mais il possède un avantage "
  "important : il peut être décomposé. Il permet ainsi de distinguer les "
  "inégalités entre pays, c’est-à-dire les différences de niveau de vie "
  "moyen entre nations, et les inégalités au sein des pays, c’est-à-dire "
  "les différences entre individus appartenant à un même pays. L’idée "
  "essentielle est que les inégalités mondiales dépendent simultanément de "
  "l’écart entre pays et de la répartition interne à chaque pays. Le cours "
  "mobilise ensuite la thèse centrale de Branko Milanovic, qui met en "
  "évidence un paradoxe : les inégalités entre pays diminuent, mais les "
  "inégalités à l’intérieur des pays augmentent — convergence entre pays "
  "développés et émergents, divergence au sein des sociétés nationales. "
  "Pour comprendre cette double dynamique, Milanovic construit la courbe de "
  "l’éléphant, présentée dans Global Inequality en 2016 et portant sur la "
  "période 1988-2008. La méthodologie est précise : en abscisse, la "
  "population mondiale classée par revenu initial ; en ordonnée, le taux de "
  "croissance du revenu réel ; les revenus étant mesurés en termes réels, "
  "donc déflatés, et en parité de pouvoir d’achat, de sorte que les "
  "résultats ne sont biaisés ni par l’inflation ni par les taux de change "
  "financiers. La forme de la courbe fait apparaître trois groupes. Au "
  "point A, les plus pauvres du monde, avec une croissance réelle d’environ "
  "+15 % : une amélioration limitée, les plus pauvres bénéficiant peu de la "
  "mondialisation. Au point B, la classe moyenne des pays émergents, avec "
  "une forte croissance de +70 à +80 %, essentiellement en Chine, en Inde "
  "et en Asie : les grands gagnants, ce qui explique la réduction des "
  "inégalités entre pays. Au point C, le top 1 % mondial, avec une hausse "
  "d’environ +60 %, dont environ 50 % de cette élite est américaine, ce que "
  "le cours décrit comme la montée d’une ploutocratie mondiale. Apparaît "
  "enfin un perdant relatif : la classe moyenne des pays développés, située "
  "autour du 80e percentile mondial, avec une croissance réelle proche de "
  "0 %, d’où un sentiment de déclassement qui explique la montée des "
  "tensions sociales et politiques. Le cours ajoute une distinction "
  "décisive entre gains relatifs et gains absolus : en pourcentage, la "
  "classe moyenne émergente connaît la plus forte hausse, mais en valeur, "
  "le top 1 % capte la plus grande part du surplus mondial. Milanovic met "
  "enfin en avant une inégalité plus fondamentale encore, la rente de "
  "citoyenneté : l’inégalité majeure aujourd’hui provient du lieu de "
  "naissance, naître dans un pays riche procurant un revenu "
  "structurellement plus élevé, un meilleur accès aux opportunités et un "
  "avantage durable.",
  [("La décomposition de l’inégalité mondiale par l’indice de Theil",
    "L’indice de Theil se comporte comme le Gini — faible valeur, faible "
    "inégalité ; valeur élevée, forte inégalité — mais présente un "
    "avantage décisif : il est décomposable. Il permet de séparer la part "
    "de l’inégalité mondiale qui provient des écarts de niveau de vie "
    "moyen entre nations et la part qui provient des écarts entre "
    "individus d’un même pays. Sans cette décomposition, une inégalité "
    "mondiale stable pourrait masquer deux mouvements opposés."),
   ("Le rattrapage des émergents et la réduction des écarts entre pays",
    "L’hypermondialisation a permis le rattrapage de grands pays "
    "émergents, notamment la Chine, ce qui réduit mécaniquement les écarts "
    "de niveau de vie moyen entre nations. La courbe de l’éléphant le "
    "chiffre au point B : la classe moyenne des pays émergents, en Chine, "
    "en Inde et en Asie, connaît une croissance de son revenu réel de +70 "
    "à +80 % entre 1988 et 2008. C’est le canal par lequel la "
    "mondialisation réduit l’inégalité internationale."),
   ("La modification de la répartition interne et la divergence nationale",
    "L’ouverture internationale modifie la répartition des revenus à "
    "l’intérieur des pays, de sorte que les inégalités au sein des pays "
    "peuvent augmenter alors même qu’elles diminuent entre pays. La courbe "
    "de l’éléphant en donne les deux extrémités dans les économies "
    "avancées : le top 1 % mondial, à moitié américain, gagne environ "
    "+60 %, tandis que la classe moyenne des pays développés, autour du "
    "80e percentile mondial, connaît une croissance réelle proche de 0 %."),
   ("L’écart entre gains relatifs et gains absolus",
    "Les deux lectures ne désignent pas les mêmes gagnants. En "
    "pourcentage, la plus forte hausse va à la classe moyenne émergente. "
    "En valeur absolue, le top 1 % capte la plus grande part du surplus "
    "mondial, parce qu’un pourcentage appliqué à un revenu très élevé "
    "produit un montant très supérieur. Le cours en conclut que la "
    "mondialisation enrichit massivement le sommet en valeur absolue, "
    "quelle que soit la lecture relative."),
   ("La rente de citoyenneté",
    "Milanovic désigne comme inégalité majeure celle qui provient du lieu "
    "de naissance : naître dans un pays riche procure un revenu "
    "structurellement plus élevé, un meilleur accès aux opportunités et un "
    "avantage durable. La nationalité devient ainsi un facteur central "
    "d’inégalité mondiale, ce qui déplace l’analyse : la position d’un "
    "individu dans la distribution mondiale dépend d’abord de son pays, "
    "avant de dépendre de son effort ou de sa qualification.")],
  [{'a': "L’indice de Theil permet de résoudre un problème que les autres "
         "indicateurs ne traitent pas : étant décomposable, il sépare la "
         "part de l’inégalité mondiale qui vient des écarts entre nations "
         "de celle qui vient des écarts entre individus d’un même pays.",
    'cond': "La décomposition suppose de disposer de données comparables "
            "entre pays, ce qui exige de mesurer les revenus en parité de "
            "pouvoir d’achat, comme le fait Milanovic, afin de ne pas "
            "biaiser les comparaisons par les taux de change financiers.",
    'lim': "La décomposition dit d’où vient l’inégalité mais non pourquoi. "
           "Le cours doit lui adjoindre une analyse causale — rattrapage "
           "des émergents d’un côté, modification de la répartition "
           "interne par l’ouverture de l’autre — pour passer du constat à "
           "l’explication."},
   {'a': "La mondialisation a produit une réduction réelle des inégalités "
         "entre pays, la classe moyenne des pays émergents — Chine, Inde, "
         "Asie — voyant son revenu réel progresser de +70 à +80 % entre "
         "1988 et 2008 selon la courbe de l’éléphant.",
    'cond': "Le résultat tient à la mesure retenue : revenus en termes "
            "réels déflatés et en parité de pouvoir d’achat, afin que la "
            "progression ne soit pas un artefact de l’inflation ou des "
            "mouvements de change. Il tient aussi à la période, 1988-2008, "
            "qui correspond à l’hypermondialisation.",
    'lim': "La réduction est inégalement partagée : au point A, les plus "
           "pauvres du monde ne progressent que d’environ +15 %, "
           "amélioration limitée qui montre qu’ils bénéficient peu de la "
           "mondialisation. Et l’actualisation de la courbe par Milanovic "
           "en 2022, dans « The Three Eras of Global Inequality, "
           "1820-2020 », montre une croissance mondiale plus faible et des "
           "inégalités toujours fortes au sommet."},
   {'a': "La même mondialisation accroît les inégalités au sein des pays "
         "développés, le top 1 % mondial — à moitié américain — gagnant "
         "environ +60 % tandis que la classe moyenne des pays développés, "
         "autour du 80e percentile mondial, connaît une croissance réelle "
         "proche de 0 %.",
    'cond': "Le diagnostic suppose de raisonner sur la distribution "
            "mondiale et non nationale, puisque la classe moyenne "
            "occidentale est identifiée par sa position dans le classement "
            "mondial des revenus, autour du 80e percentile.",
    'lim': "La stagnation en termes relatifs n’équivaut pas à un "
           "appauvrissement absolu : la classe moyenne occidentale est "
           "perdante relative, non perdante absolue. Le cours insiste "
           "néanmoins sur la portée politique du phénomène, le sentiment de "
           "déclassement expliquant la montée des tensions sociales et "
           "politiques."}],
  [{'t': "La courbe de l’éléphant démontrerait que la mondialisation a été "
         "globalement favorable, puisque tous les groupes y gagnent et que "
         "les plus fortes progressions concernent les pays émergents.",
    'qui': "le cours, dans sa distinction entre gains relatifs et gains "
           "absolus",
    'rep': "Le cours bloque cette lecture par une correction technique "
           "décisive. En gains relatifs, la classe moyenne émergente "
           "connaît effectivement la plus forte hausse, +70 à +80 %. Mais "
           "en gains absolus, c’est le top 1 % qui capte la plus grande "
           "part du surplus mondial, parce qu’un pourcentage plus faible "
           "appliqué à un revenu très supérieur produit un montant très "
           "supérieur. La mondialisation enrichit donc massivement le "
           "sommet en valeur. S’y ajoutent deux nuances : les plus pauvres "
           "du monde ne gagnent qu’environ +15 %, et la classe moyenne des "
           "pays développés connaît une croissance proche de 0 %."},
   {'t': "La réduction des inégalités entre pays serait l’essentiel, les "
         "inégalités internes relevant de choix nationaux étrangers à la "
         "mondialisation elle-même.",
    'qui': "le cours, lorsqu’il montre que l’ouverture internationale "
           "modifie elle-même la répartition des revenus à l’intérieur des "
           "pays",
    'rep': "Le cours refuse de séparer les deux dynamiques. L’effet "
           "distributif de la mondialisation est double et simultané : le "
           "rattrapage des émergents tend à réduire les écarts "
           "internationaux, tandis que la modification de la répartition "
           "interne tend à accroître les écarts nationaux. Ce n’est pas une "
           "coïncidence mais le même mécanisme vu de deux côtés. Thomas "
           "Piketty ajoute cependant que les choix politiques pèsent "
           "lourdement, puisque plusieurs pays ont depuis les années 1980 "
           "diminué certains taux marginaux supérieurs, réduit certaines "
           "formes de taxation du capital et modifié leurs systèmes "
           "redistributifs."},
   {'t': "L’inégalité la plus importante serait celle qui sépare les "
         "individus par leurs revenus et leurs qualifications, et non celle "
         "qui les sépare par leur pays de naissance.",
    'qui': "Branko Milanovic, qui soutient l’inverse avec la notion de "
           "rente de citoyenneté",
    'rep': "Le cours suit Milanovic : l’inégalité majeure aujourd’hui "
           "provient du lieu de naissance, naître dans un pays riche "
           "procurant un revenu structurellement plus élevé, un meilleur "
           "accès aux opportunités et un avantage durable. La nationalité "
           "devient donc un facteur central d’inégalité mondiale. Cette "
           "thèse n’annule pas les inégalités internes — c’est précisément "
           "Milanovic qui documente leur hausse — mais elle en relativise "
           "le poids dans l’explication de la position mondiale d’un "
           "individu. Elle éclaire aussi la question migratoire, puisque "
           "l’écart le plus rémunérateur est celui que l’on franchit en "
           "changeant de pays."}],
  [{'n': "Branko Milanovic",
    'i': "Les inégalités entre pays diminuent tandis que les inégalités au "
         "sein des pays augmentent.",
    'p': "Milanovic établit ce paradoxe dans Global Inequality en 2016 et "
         "le documente par la courbe de l’éléphant portant sur 1988-2008, "
         "où la population mondiale est classée par revenu initial en "
         "abscisse et la croissance du revenu réel en ordonnée, les revenus "
         "étant déflatés et exprimés en parité de pouvoir d’achat. Trois "
         "points structurent la lecture : A, les plus pauvres du monde, "
         "environ +15 % ; B, la classe moyenne des pays émergents, +70 à "
         "+80 % ; C, le top 1 % mondial, environ +60 %, dont la moitié est "
         "américaine. Il y ajoute la notion de rente de citoyenneté et une "
         "actualisation en 2022 dans « The Three Eras of Global Inequality, "
         "1820-2020 », qui montre une croissance mondiale plus faible et "
         "des inégalités toujours fortes au sommet."},
   {'n': "Henri Theil",
    'i': "Un indice d’inégalité décomposable permet de séparer les "
         "composantes entre groupes et à l’intérieur des groupes.",
    'p': "L’indice de Theil se lit comme le coefficient de Gini — faible "
         "valeur pour une faible inégalité, valeur élevée pour une forte "
         "inégalité — mais sa propriété de décomposabilité lui donne un "
         "usage que les autres indicateurs n’ont pas : il permet de "
         "distinguer les inégalités entre pays, différences de niveau de "
         "vie moyen entre nations, et les inégalités au sein des pays, "
         "différences entre individus d’un même pays. C’est l’outil qui "
         "rend le paradoxe de Milanovic mesurable plutôt que seulement "
         "narrable."},
   {'n': "Thomas Piketty",
    'i': "La hausse des inégalités internes dépend des institutions "
         "fiscales et politiques davantage que de la mondialisation seule.",
    'p': "Piketty insiste sur les facteurs politiques et institutionnels : "
         "pour lui, la hausse des inégalités n’est pas simplement une "
         "conséquence automatique de la technologie ou de la "
         "mondialisation, elle dépend fortement des choix politiques. Le "
         "cours cite les décisions concrètes prises depuis les années 1980 "
         "dans plusieurs pays : diminution de certains taux marginaux "
         "supérieurs d’imposition, réduction de certaines formes de "
         "taxation du capital, modification des systèmes redistributifs. "
         "Appliqué au paradoxe de Milanovic, cet argument explique pourquoi "
         "la divergence interne n’a pas la même ampleur partout."}],
  [{'f': "La courbe de l’éléphant de Branko Milanovic, publiée dans Global "
          "Inequality en 2016, porte sur la période 1988-2008 et mesure les "
          "revenus en termes réels déflatés et en parité de pouvoir "
          "d’achat.",
    'p': "Le choix méthodologique est essentiel à la validité du résultat : "
         "les conclusions ne sont biaisées ni par l’inflation ni par les "
         "taux de change financiers, ce qui permet de comparer des revenus "
         "sur vingt ans et entre continents."},
   {'f': "Sur la courbe de l’éléphant, les plus pauvres du monde (point A) "
          "progressent d’environ +15 %, la classe moyenne des pays "
          "émergents (point B) de +70 à +80 %, et le top 1 % mondial "
          "(point C) d’environ +60 %.",
    'p': "Ces trois chiffres résument l’effet distributif de "
         "l’hypermondialisation : une réduction des écarts internationaux "
         "portée par l’Asie, une concentration persistante au sommet et un "
         "bénéfice faible pour les plus pauvres."},
   {'f': "Environ 50 % du top 1 % mondial est américaine, ce que le cours "
          "décrit comme la montée d’une ploutocratie mondiale.",
    'p': "Cette composition nationale du sommet relie les deux niveaux "
         "d’analyse : l’inégalité interne américaine contribue directement "
         "à la forme du sommet de la distribution mondiale."},
   {'f': "La classe moyenne des pays développés se situe autour du 80e "
          "percentile mondial et connaît une croissance réelle proche de "
          "0 % sur la période 1988-2008, d’où un sentiment de déclassement.",
    'p': "C’est le fait qui relie l’analyse économique des inégalités à la "
         "sociologie politique de la mondialisation : le cours en fait "
         "l’explication de la montée des tensions sociales et politiques "
         "dans les économies avancées."},
   {'f': "Les BRICS+ représentent 36 % du PIB mondial en parité de pouvoir "
          "d’achat en 2022 et 25 % des exportations mondiales en 2021, "
          "tandis que la part relative du G7 diminue.",
    'p': "Ce déplacement du poids économique est la contrepartie "
         "macroéconomique de la réduction des inégalités entre pays, et il "
         "traduit une redistribution progressive de la puissance au "
         "détriment relatif des puissances traditionnelles."}],
  [{'q': "La mondialisation réduit-elle ou accroît-elle les inégalités ?",
    'f': "La question est mal posée tant qu’on n’a pas décomposé "
         "l’inégalité, ce que permet l’indice de Theil en séparant les "
         "écarts entre pays et les écarts au sein des pays. Sur la première "
         "composante, la mondialisation réduit : la courbe de l’éléphant de "
         "Milanovic montre que la classe moyenne des pays émergents — "
         "Chine, Inde, Asie — gagne +70 à +80 % de revenu réel entre 1988 "
         "et 2008, et les BRICS+ atteignent 36 % du PIB mondial en PPA en "
         "2022 contre une part relative du G7 en diminution. Sur la seconde "
         "composante, elle accroît : l’ouverture modifie la répartition "
         "interne, le top 1 % mondial gagne environ +60 % dont la moitié "
         "est américaine, tandis que la classe moyenne des pays développés, "
         "autour du 80e percentile mondial, stagne à près de 0 %. Deux "
         "corrections doivent être apportées. D’abord, les plus pauvres du "
         "monde ne gagnent qu’environ +15 % : la réduction des écarts "
         "internationaux ne les concerne guère. Ensuite, en gains absolus "
         "et non relatifs, c’est le top 1 % qui capte la plus grande part "
         "du surplus mondial. On conclut que la mondialisation réduit les "
         "écarts entre nations et accroît les écarts à l’intérieur des "
         "nations, et que l’inégalité majeure demeure la rente de "
         "citoyenneté.",
    'r': "Cette résolution est la seule qui rende compte des deux séries de "
         "faits sans en sacrifier une. Elle montre aussi que le désaccord "
         "public sur la mondialisation n’est pas nécessairement un "
         "désaccord sur les faits : selon la composante observée, les deux "
         "camps ont raison, et la distinction gains relatifs / gains "
         "absolus explique qu’on puisse lire la même courbe de deux façons "
         "opposées.",
    'ex': "Le point B de la courbe de l’éléphant, +70 à +80 % pour la "
          "classe moyenne émergente, face au 80e percentile mondial à "
          "près de 0 %."},
   {'q': "Les inégalités mondiales diminuent-elles ?",
    'f': "La réponse dépend du niveau d’agrégation et de la période. "
         "Agrégées, les inégalités mondiales ont diminué sur 1988-2008, "
         "parce que la composante entre pays, qui en constituait "
         "l’essentiel, s’est réduite sous l’effet du rattrapage asiatique. "
         "Décomposées, le tableau est contradictoire : la composante entre "
         "pays baisse, la composante au sein des pays monte, et seul "
         "l’indice de Theil permet de le voir. Sur la période suivante, le "
         "cours signale que Milanovic a actualisé son analyse en 2022 dans "
         "« The Three Eras of Global Inequality, 1820-2020 » et que la "
         "dynamique change : croissance mondiale plus faible, inégalités "
         "toujours fortes au sommet. Enfin, la réponse change selon la "
         "grandeur retenue : en gains relatifs, la classe moyenne "
         "émergente est la grande gagnante ; en gains absolus, le top 1 % "
         "capte la plus grande part du surplus mondial. Et si l’on retient "
         "le critère que Milanovic juge le plus fondamental, la rente de "
         "citoyenneté, l’inégalité majeure — celle du lieu de naissance — "
         "ne se réduit qu’à mesure que les niveaux de vie moyens "
         "convergent, donc lentement.",
    'r': "Ce raisonnement tire sa valeur du fait qu’il rend explicites les "
         "trois conventions de mesure qui décident de la réponse : le "
         "niveau d’agrégation, la période, et le choix entre gains relatifs "
         "et absolus. C’est précisément la méthode que le cours applique "
         "en exigeant que l’on sache ce que mesure chaque indicateur avant "
         "d’en tirer une conclusion.",
    'ex': "La rente de citoyenneté : l’inégalité majeure provient du lieu "
          "de naissance, qui procure un avantage durable indépendant de "
          "tout effort individuel."}],
  voisins=['n22-inegalites-revenus', 'n22-courbe-kuznets', 'n22-rente',
           'n21-regionalisation', 'n22-pauvrete-absolue-relative'])


d('n22-pauvrete-absolue-relative', 22, "Pauvreté absolue et relative",
  "Deux définitions de la pauvreté : un seuil fixe de subsistance ou un écart à la médiane",
  "La pauvreté relative se définit par rapport à la distribution des "
  "revenus du pays considéré : le seuil de pauvreté est fixé à 50 % ou, "
  "selon la norme européenne, à 60 % du revenu médian. La pauvreté absolue "
  "se définit par un seuil de subsistance indépendant de la distribution "
  "nationale. Le cours ajoute une troisième approche, multidimensionnelle, "
  "qui mesure la pauvreté comme un ensemble de privations cumulées et non "
  "comme un simple manque de revenu.",
  "Le cours construit la pauvreté relative à partir du revenu médian, "
  "défini comme le revenu tel que 50 % des ménages gagnent plus et 50 % "
  "gagnent moins : en 2023 il s’élevait à 2 150 euros. Le seuil de pauvreté "
  "se calcule par rapport à ce revenu médian, à 50 % ou à 60 % si l’on suit "
  "la norme européenne. Le choix du seuil change massivement le résultat : "
  "le seuil à 50 % vaut 1 073 euros et compte 5,4 millions de pauvres, le "
  "seuil à 60 % vaut 1 288 euros et en compte 9,8 millions, ces chiffres "
  "concernant les personnes seules. Le taux de pauvreté désigne le nombre "
  "de personnes situées sous le seuil de pauvreté. Le cours ajoute les "
  "relations arithmétiques qui structurent cette échelle : seuil de "
  "pauvreté égal au revenu médian divisé par deux, donc seuil de pauvreté "
  "multiplié par deux égal au revenu médian, et seuil de richesse égal au "
  "revenu médian multiplié par deux. Il en tire une conséquence logique "
  "importante : quand une population s’enrichit, le seuil de pauvreté "
  "augmente forcément, mais le nombre de pauvres ne diminue pas "
  "nécessairement — si l’augmentation ne touche que les plus riches, le "
  "nombre de pauvres ne change pas, alors que si la hausse est générale, il "
  "peut diminuer. Le cours complète par les dispositifs : les personnes "
  "sans emploi peuvent toucher le revenu de solidarité active, qui assure "
  "aux personnes sans emploi de plus de 25 ans un niveau minimum de revenu "
  "variant selon la composition du foyer. À l’échelle mondiale, il retient "
  "l’ordre de grandeur de 700 millions de pauvres. Le chapitre consacré au "
  "développement introduit ensuite la critique de l’approche purement "
  "monétaire. L’indice de pauvreté multidimensionnelle repose sur une idée "
  "fondamentale : la pauvreté n’est pas seulement monétaire, et une "
  "personne peut avoir un revenu légèrement supérieur à un seuil de "
  "pauvreté monétaire tout en subissant de fortes privations. L’Inde en a "
  "longtemps été l’exemple classique : même avec une forte croissance "
  "économique, une partie importante de la population pouvait encore "
  "cumuler des privations en matière de logement, d’assainissement, "
  "d’éducation ou d’accès aux services essentiels. L’indice de pauvreté "
  "multidimensionnelle mesure donc la pauvreté comme un ensemble de "
  "privations cumulées en matière de santé, d’éducation et de conditions de "
  "vie, et non comme un simple manque de revenu.",
  [("La construction du seuil relatif à partir du revenu médian",
    "Le revenu médian est celui qui partage la population en deux moitiés "
    "égales : 50 % des ménages gagnent plus, 50 % gagnent moins. Il "
    "s’élevait à 2 150 euros en 2023. Le seuil de pauvreté s’en déduit par "
    "un pourcentage, 50 % ou 60 %. Ce choix de référence à la médiane, et "
    "non à la moyenne, est délibéré : la médiane est insensible aux "
    "valeurs extrêmes du haut de la distribution, ce qui rend le seuil "
    "robuste à l’enrichissement d’une petite minorité."),
   ("L’effet du choix du seuil sur le nombre de pauvres mesuré",
    "Le même pays compte 5,4 millions de pauvres avec un seuil à 50 % du "
    "revenu médian, soit 1 073 euros, et 9,8 millions avec un seuil à "
    "60 %, soit 1 288 euros, qui est la norme européenne. Un écart de 215 "
    "euros sur le seuil déplace donc 4,4 millions de personnes. La mesure "
    "de la pauvreté est ainsi inséparable d’une convention, et toute "
    "comparaison exige de savoir quel seuil est employé."),
   ("La dépendance du seuil relatif à la distribution nationale",
    "Parce qu’il est défini comme une fraction du revenu médian, le seuil "
    "relatif se déplace avec la distribution. Le cours en tire la "
    "conséquence : quand une population s’enrichit, le seuil de pauvreté "
    "augmente forcément, mais le nombre de pauvres ne diminue pas "
    "nécessairement. Si la hausse ne touche que les plus riches, le nombre "
    "de pauvres ne change pas, puisque la médiane bouge peu ; si la hausse "
    "est générale, il peut diminuer."),
   ("Le passage à une mesure multidimensionnelle",
    "L’indice de pauvreté multidimensionnelle part du constat qu’une "
    "personne peut avoir un revenu légèrement supérieur au seuil monétaire "
    "tout en subissant de fortes privations. Il agrège donc des privations "
    "cumulées en matière de santé, d’éducation et de conditions de vie. Le "
    "mécanisme de cette approche est de substituer à un critère unique un "
    "faisceau de critères, ce qui permet de détecter une pauvreté que le "
    "revenu ne révèle pas, comme en Inde où la croissance n’a pas supprimé "
    "les privations de logement, d’assainissement et d’accès aux services "
    "essentiels.")],
  [{'a': "La définition relative de la pauvreté a le mérite de rapporter la "
         "privation au niveau de vie de la société considérée, le seuil "
         "étant fixé à 50 % ou, selon la norme européenne, à 60 % du revenu "
         "médian, lui-même de 2 150 euros en France en 2023.",
    'cond': "L’approche n’est pertinente que si la référence choisie est "
            "explicite et stable dans les comparaisons, et si l’on raisonne "
            "sur la médiane plutôt que sur la moyenne, afin que le seuil ne "
            "soit pas déplacé par l’enrichissement d’une minorité.",
    'lim': "Un seuil relatif peut produire des résultats contre-intuitifs : "
           "une société qui s’enrichit uniformément voit son seuil "
           "augmenter sans que la situation matérielle des plus modestes "
           "se dégrade, et inversement une récession générale peut faire "
           "baisser le nombre de pauvres mesurés. C’est exactement ce que "
           "le cours souligne en notant que la hausse du seuil "
           "n’entraîne pas mécaniquement une variation du nombre de "
           "pauvres."},
   {'a': "Le choix du seuil est une décision de politique publique aux "
         "conséquences majeures, puisque le passage de 50 % à 60 % du "
         "revenu médian — de 1 073 à 1 288 euros — fait passer le nombre de "
         "personnes pauvres de 5,4 à 9,8 millions.",
    'cond': "La comparaison n’est valable que sur une même population et "
            "pour une même configuration familiale : le cours précise que "
            "ces montants concernent les personnes seules, la "
            "transposition aux ménages exigeant de raisonner par unité de "
            "consommation.",
    'lim': "La sensibilité du résultat au seuil est aussi une faiblesse "
           "analytique : elle signifie qu’une part importante de la "
           "population se situe juste au-dessus du seuil bas, dans une "
           "zone de fragilité que ni l’un ni l’autre des chiffres ne "
           "décrit correctement."},
   {'a': "L’approche multidimensionnelle corrige une insuffisance réelle de "
         "la mesure monétaire, puisqu’une personne peut avoir un revenu "
         "légèrement supérieur au seuil de pauvreté monétaire tout en "
         "subissant de fortes privations de logement, d’assainissement, "
         "d’éducation ou d’accès aux services essentiels.",
    'cond': "L’indice de pauvreté multidimensionnelle n’apporte un gain "
            "d’information que si les dimensions retenues — santé, "
            "éducation, conditions de vie — sont mesurables de façon "
            "comparable, ce qui suppose des enquêtes homogènes entre pays.",
    'lim': "L’agrégation de dimensions hétérogènes exige des pondérations "
           "conventionnelles, et la comparabilité internationale en "
           "souffre. Le cours maintient donc les deux approches côte à "
           "côte plutôt que de substituer l’une à l’autre, et conserve "
           "l’ordre de grandeur monétaire mondial de 700 millions de "
           "pauvres."}],
  [{'t': "La pauvreté relative ne mesure pas la pauvreté mais l’inégalité, "
         "puisqu’un seuil défini comme une fraction du revenu médian varie "
         "avec la distribution et non avec les conditions de vie réelles.",
    'qui': "le cours, lorsqu’il montre que le seuil augmente mécaniquement "
           "quand la population s’enrichit",
    'rep': "Le cours admet le mécanisme et en précise la portée exacte : "
           "quand une population s’enrichit, le seuil de pauvreté augmente "
           "forcément, mais le nombre de pauvres ne diminue pas "
           "nécessairement, car tout dépend de qui bénéficie de la hausse. "
           "Si elle ne touche que les plus riches, le nombre de pauvres ne "
           "change pas ; si elle est générale, il peut diminuer. La "
           "critique est donc partiellement fondée, et la réponse du cours "
           "consiste à adjoindre d’autres mesures : la pauvreté absolue, "
           "qui retient un seuil indépendant de la distribution, et "
           "l’indice de pauvreté multidimensionnelle, qui mesure des "
           "privations concrètes."},
   {'t': "La pauvreté monétaire, absolue ou relative, ne capte pas "
         "l’essentiel de ce que vivent les personnes pauvres, qui subissent "
         "des privations cumulées que le revenu ne révèle pas.",
    'qui': "l’approche multidimensionnelle de la pauvreté que le cours "
           "présente avec l’indice de pauvreté multidimensionnelle",
    'rep': "Le cours accepte largement cette critique et en donne "
           "l’illustration : l’Inde a longtemps été un exemple classique "
           "puisque, même avec une forte croissance économique, une partie "
           "importante de la population pouvait encore cumuler des "
           "privations de logement, d’assainissement, d’éducation ou "
           "d’accès aux services essentiels. Il conserve pourtant la mesure "
           "monétaire pour sa comparabilité et sa simplicité, et "
           "l’articule avec les autres : l’indice de développement humain "
           "ajusté aux inégalités et l’approche d’Amartya Sen par les "
           "capacités élargissent de même la mesure du développement "
           "au-delà du revenu."},
   {'t': "La lutte contre la pauvreté par les minima sociaux traiterait le "
         "symptôme sans la cause et entretiendrait la dépendance aux "
         "transferts plutôt que l’insertion.",
    'qui': "le débat sur les trappes à pauvreté, auquel le cours fait place "
           "dans sa présentation du revenu de solidarité active",
    'rep': "Le cours décrit d’abord le dispositif sans le charger : le "
           "revenu de solidarité active assure aux personnes sans emploi "
           "de plus de 25 ans un niveau minimum de revenu, variable selon "
           "la composition du foyer. Il rappelle ensuite l’efficacité "
           "globale de la redistribution française, qui ramène l’écart de "
           "niveau de vie d’un facteur 18 à un facteur 4 et dont 53 % des "
           "ménages sont bénéficiaires nets. Et il relativise la critique "
           "par un fait décisif : la pauvreté laborieuse montre que de "
           "nombreuses personnes travaillent et restent pauvres, de sorte "
           "que l’opposition entre assistance et emploi ne recouvre pas la "
           "réalité de la pauvreté contemporaine."}],
  [{'n': "Amartya Sen",
    'i': "Le développement et la pauvreté doivent être évalués en termes de "
         "capacités réelles et non de seul revenu.",
    'p': "Sen déplace le critère d’évaluation du revenu vers ce que les "
         "personnes sont effectivement en mesure de faire et d’être. Le "
         "cours mobilise cette approche pour justifier le passage de la "
         "pauvreté monétaire à la pauvreté multidimensionnelle : si ce qui "
         "compte est la capacité à se soigner, à s’instruire, à se loger, "
         "alors un indicateur de revenu ne suffit pas, et il faut mesurer "
         "les privations cumulées en matière de santé, d’éducation et de "
         "conditions de vie. C’est également le fondement conceptuel de "
         "l’indice de développement humain."},
   {'n': "Branko Milanovic",
    'i': "L’inégalité majeure provient du lieu de naissance, ce que la "
         "notion de rente de citoyenneté désigne.",
    'p': "Milanovic soutient que l’inégalité la plus importante aujourd’hui "
         "tient au pays où l’on naît : naître dans un pays riche procure un "
         "revenu structurellement plus élevé, un meilleur accès aux "
         "opportunités et un avantage durable. Appliqué à la pauvreté, cet "
         "argument explique pourquoi les seuils relatifs nationaux et le "
         "décompte mondial de 700 millions de pauvres ne mesurent pas la "
         "même chose : la pauvreté relative situe un individu dans sa "
         "société, la pauvreté absolue le situe dans l’humanité."},
   {'n': "Robert Castel",
    'i': "La question sociale ne disparaît pas avec la croissance, elle se "
         "transforme.",
    'p': "Castel montre dans Les Métamorphoses de la question sociale, "
         "publié en 1995, que la condition salariale se fragilise avec la "
         "montée du chômage et de la précarité. Le cours en tire "
         "l’avertissement qui vaut pour toute mesure de la pauvreté : au "
         "XIXe siècle la question sociale renvoyait à la misère ouvrière et "
         "à la condition du prolétariat industriel, elle prend aujourd’hui "
         "la forme du chômage, de la précarité et de la pauvreté "
         "laborieuse. Les indicateurs doivent donc suivre le déplacement de "
         "la réalité qu’ils mesurent."}],
  [{'f': "Le revenu médian français s’élevait à 2 150 euros en 2023, le "
          "revenu médian étant celui tel que 50 % des ménages gagnent plus "
          "et 50 % gagnent moins.",
    'p': "C’est la grandeur de référence de toute la mesure relative de la "
         "pauvreté et de la richesse en France, puisque le seuil de "
         "pauvreté en est une fraction et le seuil de richesse un multiple."},
   {'f': "Le seuil de pauvreté à 50 % du revenu médian vaut 1 073 euros et "
          "correspond à 5,4 millions de pauvres ; le seuil à 60 %, norme "
          "européenne, vaut 1 288 euros et correspond à 9,8 millions, pour "
          "des personnes seules.",
    'p': "Ce couple de chiffres est l’illustration la plus nette de la "
         "part conventionnelle de la mesure : un écart de 215 euros sur le "
         "seuil déplace 4,4 millions de personnes dans ou hors de la "
         "pauvreté statistique."},
   {'f': "Les relations arithmétiques retenues par le cours : seuil de "
          "pauvreté égal au revenu médian divisé par deux, et seuil de "
          "richesse égal au revenu médian multiplié par deux.",
    'p': "Cette symétrie rend la pauvreté et la richesse mesurables sur une "
         "même échelle rapportée à la médiane, ce qui facilite la lecture "
         "d’ensemble de la distribution."},
   {'f': "Le revenu de solidarité active assure aux personnes sans emploi "
          "de plus de 25 ans un niveau minimum de revenu, qui varie selon "
          "la composition du foyer ; le cours retient par ailleurs un ordre "
          "de grandeur de 700 millions de pauvres dans le monde.",
    'p': "Le rapprochement des deux échelles est instructif : un dispositif "
         "national de minimum garanti relève de la pauvreté relative, "
         "tandis que le décompte mondial relève d’un seuil absolu de "
         "subsistance."},
   {'f': "L’indice de pauvreté multidimensionnelle mesure la pauvreté comme "
          "un ensemble de privations cumulées en matière de santé, "
          "d’éducation et de conditions de vie, et non comme un simple "
          "manque de revenu.",
    'p': "C’est la réponse construite à l’insuffisance du critère "
         "monétaire, et le cas indien montre son intérêt : une forte "
         "croissance économique peut coexister avec des privations "
         "massives de logement, d’assainissement et d’accès aux services "
         "essentiels."}],
  [{'q': "Peut-on réduire la pauvreté sans réduire les inégalités ?",
    'f': "La réponse dépend de la définition retenue, et c’est tout "
         "l’intérêt du sujet. Si l’on retient la pauvreté absolue, c’est-à-"
         "dire un seuil de subsistance indépendant de la distribution, la "
         "réponse est oui : une croissance qui élève le revenu des plus "
         "modestes fait franchir ce seuil même si les écarts se creusent "
         "par ailleurs, et c’est bien ce que la courbe de l’éléphant montre "
         "au point B avec +70 à +80 % pour la classe moyenne émergente. Si "
         "l’on retient la pauvreté relative, la réponse devient largement "
         "non, puisque le seuil est défini comme 50 % ou 60 % du revenu "
         "médian : réduire le nombre de personnes sous ce seuil suppose de "
         "resserrer le bas de la distribution autour de la médiane, donc de "
         "réduire une inégalité. Le cours le formule précisément : quand "
         "une population s’enrichit, le seuil augmente forcément mais le "
         "nombre de pauvres ne diminue pas nécessairement — si la hausse ne "
         "touche que les plus riches, il ne change pas. Si l’on retient "
         "enfin l’approche multidimensionnelle, la réponse se déplace "
         "encore : réduire les privations de santé, d’éducation et de "
         "conditions de vie dépend de la fourniture de services collectifs, "
         "ce que le cas indien illustre, et cela peut être obtenu "
         "indépendamment du resserrement de la distribution monétaire.",
    'r': "Ce raisonnement est préférable à une réponse unique parce que la "
         "question contient une ambiguïté de définition qu’il faut lever "
         "avant de répondre : le mot pauvreté ne désigne pas la même chose "
         "selon qu’il renvoie à un seuil fixe, à un écart à la médiane ou à "
         "un faisceau de privations. En explicitant les trois, on obtient "
         "trois réponses cohérentes au lieu d’une réponse confuse.",
    'ex': "La redistribution française ramène l’écart de niveau de vie d’un "
          "facteur 18 à un facteur 4, agissant donc simultanément sur la "
          "pauvreté relative et sur l’inégalité."},
   {'q': "Comment mesurer la pauvreté ?",
    'f': "Il faut présenter trois approches et montrer ce que chacune "
         "capte. La pauvreté relative part du revenu médian — 2 150 euros "
         "en France en 2023 — et fixe un seuil à 50 % ou 60 % de celui-ci ; "
         "le premier donne 1 073 euros et 5,4 millions de pauvres, le "
         "second, norme européenne, 1 288 euros et 9,8 millions. Son "
         "avantage est de situer la privation dans la société considérée, "
         "son inconvénient de se déplacer avec la distribution. La pauvreté "
         "absolue retient un seuil de subsistance indépendant de la "
         "distribution nationale, ce qui autorise les comparaisons "
         "internationales et fonde l’ordre de grandeur de 700 millions de "
         "pauvres dans le monde ; son inconvénient est d’ignorer ce que "
         "vivre dans une société donnée exige réellement. L’approche "
         "multidimensionnelle, enfin, mesure des privations cumulées en "
         "matière de santé, d’éducation et de conditions de vie, parce "
         "qu’une personne peut avoir un revenu légèrement supérieur au "
         "seuil monétaire tout en subissant de fortes privations ; son coût "
         "est la pondération conventionnelle des dimensions. On conclut que "
         "les trois sont complémentaires et qu’aucune comparaison n’est "
         "recevable sans précision de la mesure employée.",
    'r': "La force de cette présentation est qu’elle fait du choix de "
         "l’indicateur un objet d’analyse et non un préalable technique. "
         "C’est exactement la méthode que le cours applique aux "
         "indicateurs d’inégalité, en montrant que le Gini, le Palma et "
         "l’interdécile ne répondent pas à la même question.",
    'ex': "L’Inde, où une forte croissance économique a longtemps coexisté "
          "avec des privations massives de logement, d’assainissement, "
          "d’éducation et d’accès aux services essentiels."}],
  voisins=['n22-travailleurs-pauvres', 'n22-exclusion-sociale',
           'n22-inegalites-revenus', 'n22-redistribution',
           'n22-inegalites-entre-et-au-sein'])
