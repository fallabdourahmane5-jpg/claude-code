# -*- coding: utf-8 -*-
"""Ensemble 13 — Les crises et l’instabilité économique (4/4)."""

from doss_base import d

d('n13-risque-systemique', 13, "Risque systémique",
  "Le risque que la défaillance d’un acteur emporte tout le système",
  "Le cours définit le risque systémique comme un événement qui affecte tout "
  "le système économique mondial, et donne pour exemples la faillite d’une "
  "grande banque, un krach boursier ou un effondrement du crédit, la crise de "
  "2008 en étant la réalisation. Ce n’est donc pas l’ampleur d’une perte qui "
  "le caractérise, mais sa capacité à se transmettre à l’ensemble des "
  "circuits de financement et de paiement.",
  "Le cours introduit le risque systémique par une définition brève puis "
  "l’éprouve sur plusieurs cas, et c’est cette méthode qui en fixe le "
  "contenu. La définition est explicite : le risque systémique désigne un "
  "événement qui affecte tout le système économique mondial, la crise de 2008 "
  "servant de référence, avec pour exemples la faillite d’une grande banque, "
  "un krach boursier ou un effondrement du crédit. Le premier test porte sur "
  "le bitcoin, et il est instructif parce que le cours répond non : pas "
  "vraiment aujourd’hui, car le bitcoin représente une faible partie du "
  "système financier mondial et est peu utilisé, étant surtout thésaurisé ou "
  "revendu plutôt qu’employé dans la vie quotidienne ; de même, les banques "
  "centrales et les banques commerciales sont peu exposées à la cryptomonnaie "
  "et son marché reste isolé du reste du système monétaire classique. Mais le "
  "cours ajoute la condition de bascule : s’il devenait massivement utilisé "
  "par les banques, les États ou les grandes entreprises, alors une chute "
  "brutale pourrait déstabiliser une partie du système financier. On en tire "
  "le critère opératoire : ce qui fait le caractère systémique n’est ni la "
  "volatilité d’un actif ni sa taille absolue, mais le degré d’exposition des "
  "acteurs centraux du système. Les autres tests confirment ce critère. Les "
  "marchés de gré à gré sont plus difficiles à surveiller et peuvent "
  "accroître le risque systémique. Les contrats d’assurance contre le défaut "
  "en créent une forme particulière : le vendeur de la protection peut "
  "lui-même ne pas être capable d’indemniser, et le cours relève que c’est "
  "exactement ce qui a rendu certains acteurs ultra fragiles en 2008. La "
  "concentration financière en fournit la version institutionnelle avec les "
  "établissements trop grands pour faire faillite, très grandes institutions "
  "dont la défaillance pourrait provoquer des dégâts systémiques majeurs : "
  "elles sont si grandes et si centrales que leur faillite menacerait le "
  "système bancaire, les paiements, le crédit et l’économie réelle, de sorte "
  "que la chute d’un grand acteur peut contaminer tout le système. Le cours "
  "élargit enfin le raisonnement à l’échelle internationale : les "
  "déséquilibres extérieurs deviennent un problème collectif lorsqu’ils sont "
  "entretenus par des flux internationaux de capitaux, et l’accumulation de "
  "déficits et d’excédents peut transformer des déséquilibres nationaux en "
  "risque systémique mondial. La réponse institutionnelle est inscrite dans "
  "les missions de la banque centrale : parmi ses fonctions associées "
  "figurent le soutien à la liquidité du système bancaire, la stabilisation "
  "des marchés en période de crise et la prévention du risque systémique.",
  [("Une exposition commune",
    "Plusieurs acteurs détiennent le même type d’actif ou sont engagés "
    "envers le même débiteur : un choc unique frappe alors simultanément "
    "l’ensemble des bilans, au lieu de rester circonscrit."),
   ("La centralité des acteurs touchés",
    "Le cours en fait le critère décisif : l’événement devient systémique "
    "parce qu’il atteint des acteurs centraux, banques et institutions dont "
    "dépendent le système bancaire, les paiements et le crédit."),
   ("La défaillance du garant",
    "Lorsqu’un acteur a vendu une protection contre le défaut d’autrui, son "
    "incapacité à indemniser retourne l’assurance en facteur de risque : "
    "c’est ce qui a rendu certains acteurs ultra fragiles en 2008."),
   ("La contamination en chaîne",
    "La chute d’un grand acteur peut contaminer tout le système, parce que "
    "ses engagements sont les créances des autres : la perte se propage de "
    "bilan en bilan."),
   ("Le passage au circuit réel",
    "Le crédit et les paiements étant atteints, la défaillance financière "
    "devient une contrainte pour toutes les entreprises, ce que le cours "
    "constate en 2008 avec la contraction du crédit et la récession "
    "mondiale."),
   ("La dimension internationale",
    "Les flux internationaux de capitaux permettent aux déséquilibres de "
    "durer et peuvent transformer des déséquilibres nationaux en risque "
    "systémique mondial.")],
  [{'a': "Le critère d’exposition permet de hiérarchiser les menaces au lieu "
         "de traiter tout actif volatil comme un danger systémique.",
    'cond': "Il suppose que l’on puisse mesurer l’exposition des acteurs "
            "centraux, ce que le cours fait pour le bitcoin en observant que "
            "banques centrales et banques commerciales y sont peu exposées.",
    'lim': "L’exposition peut croître vite et par des canaux peu visibles : "
           "le cours réserve explicitement le cas où le bitcoin deviendrait "
           "massivement utilisé par les banques, les États ou les grandes "
           "entreprises."},
   {'a': "La notion justifie une surveillance portant sur les liens entre "
         "acteurs, et non seulement sur la solidité de chacun pris "
         "séparément.",
    'cond': "L’argument exige que le risque naisse des engagements croisés, "
            "ce que le cours établit avec les contrats d’assurance contre le "
            "défaut et la chaîne de pertes qu’ils créent.",
    'lim': "Les marchés de gré à gré sont précisément ceux que le cours juge "
           "plus difficiles à surveiller : le besoin d’information est le "
           "plus fort là où elle est la moins disponible."},
   {'a': "Elle explique pourquoi certains établissements bénéficient d’une "
         "garantie implicite qu’aucun texte ne leur accorde.",
    'cond': "La garantie implicite suppose que leur faillite menacerait "
            "effectivement le système bancaire, les paiements, le crédit et "
            "l’économie réelle.",
    'lim': "Le cours en tire aussitôt le coût : si les acteurs pensent "
           "qu’ils seront sauvés, ils peuvent prendre trop de risques, "
           "sous-estimer les conséquences et accroître la fragilité du "
           "système."},
   {'a': "Elle fonde l’inscription de la stabilité financière parmi les "
         "objectifs de la banque centrale, à côté de la stabilité des prix.",
    'cond': "L’élargissement suppose que la banque centrale puisse soutenir "
            "la liquidité du système bancaire et stabiliser les marchés en "
            "période de crise.",
    'lim': "Le cours relève le dilemme classique : cet objectif peut entrer "
           "en tension avec la stabilité des prix, entre relancer l’activité "
           "et maîtriser l’inflation."},
   {'a': "Elle transpose à l’échelle mondiale : des soldes extérieurs "
         "nationaux peuvent devenir un risque collectif.",
    'cond': "La transposition suppose que les déséquilibres soient "
            "entretenus par des flux internationaux de capitaux, condition "
            "que le cours pose explicitement.",
    'lim': "Le cours avertit que les déséquilibres extérieurs doivent être "
           "interprétés avec prudence : un déficit n’est pas automatiquement "
           "mauvais, ni un excédent automatiquement positif."}],
  [{'t': "La volatilité d’un actif suffit à en faire une menace pour "
         "l’ensemble du système financier, quelle que soit sa place dans "
         "celui-ci.",
    'qui': "Le raisonnement que le cours met à l’épreuve en examinant le "
           "bitcoin et sa grande volatilité.",
    'rep': "Le cours répond non : le bitcoin représente une faible partie du "
           "système financier mondial, les banques y sont peu exposées et son "
           "marché reste isolé, de sorte que la volatilité ne suffit pas sans "
           "exposition."},
   {'t': "Transférer le risque à ceux qui acceptent de le porter réduit le "
         "risque systémique au lieu de l’augmenter.",
    'qui': "La justification des produits dérivés d’assurance contre le "
           "défaut que le cours présente avant d’en montrer les effets.",
    'rep': "Le cours objecte que le vendeur de la protection peut lui-même "
           "ne pas être capable d’indemniser, ce qui a rendu certains acteurs "
           "ultra fragiles en 2008 : le transfert concentre le risque sur le "
           "garant."},
   {'t': "Il faut laisser faire faillite les très grandes institutions, pour "
         "supprimer la garantie implicite et rétablir la discipline.",
    'qui': "L’argument d’aléa moral que le cours développe à propos des "
           "institutions trop grandes pour faire faillite.",
    'rep': "Le cours rappelle que la faillite d’une grande banque figure "
           "précisément parmi ses exemples de risque systémique : la "
           "sanction visée est elle-même l’événement que l’on cherche à "
           "éviter."},
   {'t': "Les déséquilibres extérieurs sont les problèmes isolés de certains "
         "pays, à régler nationalement.",
    'qui': "La lecture que le cours écarte en traitant des déséquilibres "
           "mondiaux.",
    'rep': "Le cours répond qu’ils sont liés entre eux, le déficit des uns "
           "correspondant à la capacité de financement des autres, et que les "
           "flux de capitaux leur permettent de durer, donc de créer un "
           "risque systémique."}],
  [{'n': "Satoshi Nakamoto",
    'i': "Une monnaie décentralisée à masse monétaire fixe, hors du contrôle "
         "d’une banque centrale.",
    'p': "Le cours se sert de ce cas pour tester la notion de risque "
         "systémique : la masse est plafonnée à vingt et un millions "
         "d’unités, la valeur dépend uniquement de l’offre et de la demande "
         "donc elle est hautement spéculative, mais l’exposition du système "
         "bancaire reste faible."},
   {'n': "Henri Bourguinat",
    'i': "Le décloisonnement est l’un des trois D qui transforment les "
         "marchés financiers depuis les années 1980.",
    'p': "Le cours situe la règle dans Les vertiges de la finance "
         "internationale en 1987 : en supprimant les cloisons entre "
         "compartiments et entre places financières, le décloisonnement crée "
         "précisément les voies par lesquelles un choc local devient "
         "systémique."},
   {'n': "Éric Monnet",
    'i': "La banque centrale n’est plus seulement une institution "
         "anti-inflation mais un pilier de la stabilité financière.",
    'p': "Le cours cite La Banque Providence, publiée en 2021, au moment où "
         "il énumère les fonctions associées à cet objectif : prêteur en "
         "dernier ressort, soutien à la liquidité du système bancaire, "
         "stabilisation des marchés en période de crise et prévention du "
         "risque systémique."}],
  [{'f': "Le cours définit le risque systémique comme un événement qui "
         "affecte tout le système économique mondial, avec la crise de 2008 "
         "pour référence.",
    'p': "La définition montre que le critère est la portée et non le "
         "montant : faillite d’une grande banque, krach boursier ou "
         "effondrement du crédit sont systémiques par leur capacité de "
         "transmission."},
   {'f': "Le cours conclut que le bitcoin ne crée pas vraiment aujourd’hui de "
         "risque systémique, banques centrales et banques commerciales y "
         "étant peu exposées.",
    'p': "Le jugement démontre que l’exposition des acteurs centraux est le "
         "critère décisif : un actif très volatil mais isolé du système "
         "monétaire classique ne le menace pas."},
   {'f': "Le cours relève que l’incapacité du vendeur d’une protection à "
         "indemniser a rendu certains acteurs ultra fragiles en 2008.",
    'p': "Le fait montre qu’un instrument de couverture peut concentrer le "
         "risque au lieu de le disperser, et devenir ainsi la source même du "
         "risque systémique."},
   {'f': "Le cours note que l’accumulation de déficits et d’excédents peut "
         "transformer des déséquilibres nationaux en risque systémique "
         "mondial.",
    'p': "Le fait étend la notion au-delà des bilans bancaires : les flux "
         "internationaux de capitaux jouent le rôle de courroie, comme les "
         "engagements croisés à l’intérieur d’un système financier."}],
  [{'q': "Sujet sur la stabilité du système financier",
    'f': "Un risque n’est pas systémique par sa taille mais par son "
         "exposition. Le cours le prouve par un cas négatif : le bitcoin est "
         "hautement spéculatif, sa valeur dépendant uniquement de l’offre et "
         "de la demande, et pourtant il ne crée pas vraiment aujourd’hui de "
         "risque systémique, car il représente une faible partie du système "
         "financier mondial et les banques centrales comme les banques "
         "commerciales y sont peu exposées.",
    'r': "On construit le critère par contraste : en montrant ce qui "
         "manque au bitcoin pour être systémique, on isole la variable "
         "pertinente, l’exposition des acteurs centraux.",
    'ex': "La réserve du cours : s’il devenait massivement utilisé par les "
          "banques, les États ou les grandes entreprises, une chute brutale "
          "pourrait déstabiliser une partie du système financier."},
   {'q': "Sujet sur la concentration des acteurs financiers",
    'f': "La taille d’une institution financière modifie la nature du risque "
         "qu’elle porte. Le cours définit les établissements trop grands pour "
         "faire faillite comme de très grandes institutions dont la faillite "
         "pourrait provoquer des dégâts systémiques majeurs, parce qu’elles "
         "sont si grandes et si centrales que leur défaillance menacerait le "
         "système bancaire, les paiements, le crédit et l’économie réelle.",
    'r': "Le raisonnement passe de la solidité individuelle à la position "
         "dans le réseau : ce n’est pas la probabilité de défaut qui compte "
         "mais le nombre d’acteurs qu’un défaut entraînerait.",
    'ex': "La socialisation des pertes relevée par le cours : les profits "
          "peuvent être privés, mais les pertes supportées par les banques "
          "centrales, les États, donc la collectivité."},
   {'q': "Sujet sur les produits dérivés et la couverture des risques",
    'f': "Un instrument de couverture peut devenir un instrument de risque "
         "systémique. Le cours montre que les contrats d’assurance contre le "
         "défaut permettent de parier sur la faillite d’un acteur, créent un "
         "effet de contagion si beaucoup d’acteurs y sont liés, et "
         "engendrent un risque systémique parce que le vendeur de la "
         "protection peut lui-même ne pas être capable d’indemniser, ce qui a "
         "rendu certains acteurs ultra fragiles en 2008.",
    'r': "On distingue la fonction d’un instrument et sa position dans le "
         "réseau d’engagements, pour montrer que la couverture déplace le "
         "risque vers le garant au lieu de le supprimer.",
    'ex': "La possibilité, relevée par le cours, d’acheter une protection "
          "contre le défaut sans détenir l’obligation correspondante."},
   {'q': "Sujet sur les déséquilibres mondiaux",
    'f': "Un solde extérieur national peut devenir un risque collectif. Le "
         "cours l’établit en montrant que les déséquilibres mondiaux ne sont "
         "pas les problèmes isolés de certains pays : le déficit des uns "
         "correspond à la capacité de financement des autres, les flux de "
         "capitaux permettent à ces déséquilibres de durer, et leur "
         "accumulation peut transformer des déséquilibres nationaux en risque "
         "systémique mondial.",
    'r': "On montre que l’interdépendance transforme la nature du problème : "
         "ce qui serait un choix national dans une économie fermée devient "
         "une externalité dans un système financier intégré.",
    'ex': "Le précédent de 2008 rappelé par le cours : une crise "
          "initialement localisée dans le marché américain des subprimes est "
          "devenue une crise financière mondiale."}],
  voisins=['n13-contagion-financiere', 'n13-alea-moral-sauvetages',
           'n13-crise-bancaire', 'n13-instabilite-financiere'])


d('n13-contagion-financiere', 13, "Contagion financière",
  "Comment une perte locale devient une crise mondiale",
  "La contagion financière est le processus par lequel une défaillance "
  "initialement localisée se propage aux autres acteurs et aux autres pays. "
  "Le cours en identifie deux canaux : la dispersion internationale des "
  "titres issus de la titrisation, qui fait que la crise se propage très "
  "vite, et les engagements croisés, qui font que la défaillance d’un gros "
  "débiteur peut provoquer une chaîne de pertes.",
  "Le cours ne consacre pas de définition abstraite à la contagion mais la "
  "décrit à travers les instruments qui la produisent, et c’est cette "
  "approche concrète qui en fait la force démonstrative. Premier canal, la "
  "dispersion des titres. Les produits issus de la titrisation sont "
  "construits à partir d’un panier de dettes, crédits immobiliers, prêts "
  "bancaires et autres créances, regroupées puis transformées en titres "
  "négociables vendus à des investisseurs. Comme ces titres sont vendus à "
  "travers le monde, le risque est dispersé internationalement ; le cours en "
  "tire le résultat décisif : quand les défauts augmentent, par exemple sur "
  "les crédits immobiliers à risque, la crise se propage très vite. "
  "L’opacité aggrave le phénomène, puisque l’investisseur ne voit plus "
  "toujours clairement la qualité réelle des créances contenues dans le "
  "panier, mélange d’actifs peu risqués et d’actifs très risqués : ne sachant "
  "pas qui détient les mauvaises créances, chacun se méfie de tous. Le cours "
  "conclut que ces titres augmentent la liquidité mais rendent les risques "
  "plus opaques et ont fortement contribué à la diffusion internationale de "
  "la crise de 2008. Second canal, les engagements croisés. Avec les contrats "
  "d’assurance contre le défaut, si beaucoup d’acteurs sont liés entre eux, "
  "la défaillance d’un gros débiteur peut provoquer une chaîne de pertes, et "
  "le vendeur de la protection peut lui-même ne pas être capable "
  "d’indemniser. La contagion ne suit donc pas seulement la circulation des "
  "titres mais la structure des promesses réciproques. Le cours valide "
  "ensuite ces mécanismes par l’expérience historique : avant 2008 les "
  "déséquilibres mondiaux avaient fortement augmenté, ils ont participé à la "
  "circulation internationale des capitaux et donc à la diffusion de la crise "
  "financière, si bien qu’une crise initialement localisée dans le marché "
  "américain des subprimes a fini par devenir une crise financière mondiale, "
  "parce que les systèmes financiers étaient fortement interconnectés. Il en "
  "tire une leçon générale : des déséquilibres extérieurs importants combinés "
  "à une forte intégration financière peuvent transformer une crise locale en "
  "crise mondiale. Le cours applique enfin la même grille au présent : la "
  "concentration des flux internationaux sur les actions technologiques "
  "américaines fait que si une bulle liée à l’intelligence artificielle "
  "éclatait, on observerait des pertes financières, des sorties de capitaux "
  "et une contagion internationale.",
  [("La mise en commun des créances",
    "Plusieurs dettes de qualité inégale sont regroupées dans un même "
    "panier puis transformées en titres négociables : le titre vendu ne "
    "correspond plus à un emprunteur identifiable."),
   ("La dispersion internationale",
    "Ces titres étant vendus à travers le monde, le risque est dispersé "
    "internationalement : chaque place financière détient une fraction du "
    "même risque sans le savoir précisément."),
   ("L’opacité et la méfiance généralisée",
    "L’investisseur ne voit plus clairement la qualité réelle des créances "
    "du panier : ne pouvant identifier les porteurs des mauvaises créances, "
    "les acteurs suspendent leurs engagements envers tous."),
   ("La chaîne des engagements croisés",
    "Si beaucoup d’acteurs sont liés par des contrats d’assurance contre le "
    "défaut, la défaillance d’un gros débiteur provoque une chaîne de "
    "pertes, chaque perte en déclenchant une autre."),
   ("La défaillance du garant",
    "Le vendeur de la protection peut lui-même ne pas être capable "
    "d’indemniser : le maillon censé arrêter la propagation devient le point "
    "par lequel elle s’étend."),
   ("La transmission par les capitaux internationaux",
    "Les flux internationaux de capitaux font circuler la crise d’un pays à "
    "l’autre : le cours montre qu’ils ont participé à la diffusion de la "
    "crise financière après 2008."),
   ("Le passage à l’économie réelle",
    "La contagion financière se termine en contraction du crédit : le cours "
    "décrit en 2008 des faillites bancaires et une chute des marchés "
    "entraînant une baisse brutale de l’activité économique mondiale.")],
  [{'a': "Analyser la contagion par ses canaux permet de désigner des "
         "mécanismes précis plutôt que d’invoquer une psychologie "
         "collective.",
    'cond': "L’argument suppose que les deux canaux identifiés par le cours, "
            "la dispersion des titres et les engagements croisés, soient "
            "effectivement présents.",
    'lim': "Le cours laisse une place à la dimension des représentations, "
           "puisque l’opacité produit une méfiance qui frappe aussi les "
           "acteurs sains."},
   {'a': "Elle explique pourquoi la dispersion du risque n’est pas sa "
         "réduction, mais souvent le moyen de sa généralisation.",
    'cond': "Le raisonnement exige que les porteurs du risque soient "
            "nombreux mais incapables de l’évaluer, ce que l’opacité des "
            "paniers de créances produit.",
    'lim': "Dispersion et opacité sont deux choses distinctes : une "
           "dispersion transparente réduirait effectivement la vulnérabilité "
           "de chaque porteur."},
   {'a': "Elle montre que l’intégration financière a un coût collectif, "
         "indépendant de la qualité des politiques nationales.",
    'cond': "L’argument suppose une forte interconnexion des systèmes "
            "financiers, condition que le cours tient pour établie en 2008.",
    'lim': "Le cours rappelle aussi la fonction utile de cette "
           "intégration : la mondialisation financière permet à l’épargne des "
           "pays excédentaires de financer les pays déficitaires."},
   {'a': "Elle fournit une grille applicable aux risques contemporains, non "
         "seulement à l’épisode de 2008.",
    'cond': "L’application suppose une concentration comparable des flux, "
            "que le cours observe aujourd’hui sur les actions "
            "technologiques américaines.",
    'lim': "La lecture reste conditionnelle : le cours écrit que les "
           "conséquences suivraient si la bulle liée à l’intelligence "
           "artificielle éclatait, sans l’affirmer."},
   {'a': "Elle justifie que la stabilisation des marchés en période de crise "
         "figure parmi les fonctions de la banque centrale.",
    'cond': "La justification suppose que l’intervention publique puisse "
            "interrompre la chaîne en garantissant la liquidité des acteurs "
            "solvables.",
    'lim': "Le cours relève que cette garantie nourrit l’aléa moral et "
           "qu’une partie des acteurs concernés, dans le shadow banking, "
           "échappe aux règles prudentielles."}],
  [{'t': "Répartir un risque entre de nombreux porteurs le rend "
         "supportable : la titrisation est donc stabilisatrice.",
    'qui': "La justification de la titrisation que le cours expose avant "
           "d’en examiner les effets pervers.",
    'rep': "Le cours objecte que les titres augmentent la liquidité mais "
           "rendent les risques plus opaques et ont fortement contribué à la "
           "diffusion internationale de la crise de 2008 : la dispersion "
           "transporte le risque autant qu’elle l’allège."},
   {'t': "La crise de 2008 est d’abord une crise américaine : sa "
         "mondialisation relève de circonstances plus que d’un mécanisme.",
    'qui': "La lecture nationale de la crise que le cours écarte.",
    'rep': "Le cours répond par la cause : une crise initialement localisée "
           "dans le marché américain des subprimes est devenue mondiale "
           "parce que les systèmes financiers étaient fortement "
           "interconnectés."},
   {'t': "La contagion viendrait surtout des croyances : ce sont les "
         "représentations collectives, non les bilans, qui propagent la "
         "crise.",
    'qui': "La lecture par la prophétie autoréalisatrice que le cours "
           "rattache à Robert Merton.",
    'rep': "Les deux explications se complètent : l’opacité des paniers de "
           "créances rend la méfiance rationnelle, de sorte que la croyance "
           "se greffe sur une incertitude réelle au lieu de l’inventer."},
   {'t': "Fermer les frontières financières supprimerait la contagion : "
         "l’isolement protège, comme le montre le marché du bitcoin.",
    'qui': "L’argument que le cours suggère en relevant que le marché du "
           "bitcoin reste isolé du système monétaire classique.",
    'rep': "Le cours rappelle le coût d’un tel isolement : la mondialisation "
           "financière permet à l’épargne des pays excédentaires de financer "
           "les besoins des autres, et le décloisonnement est aussi ce qui a "
           "élargi l’accès au financement."}],
  [{'n': "Henri Bourguinat",
    'i': "Le décloisonnement supprime les barrières entre compartiments et "
         "entre places financières.",
    'p': "Le cours situe la règle des trois D dans Les vertiges de la "
         "finance internationale en 1987 : en abolissant les cloisons, le "
         "décloisonnement crée les voies par lesquelles une défaillance "
         "locale peut atteindre l’ensemble des marchés, ce que 2008 vérifie."},
   {'n': "Robert Merton",
    'i': "Les représentations collectives influencent directement la "
         "réalité économique.",
    'p': "Le cours en fait un concept clé en économie, avec pour exemples la "
         "panique bancaire et la bulle spéculative : appliquée à la "
         "contagion, la prophétie autoréalisatrice explique pourquoi la "
         "méfiance atteint aussi des acteurs dont les bilans sont sains."},
   {'n': "Éric Monnet",
    'i': "La stabilisation des marchés en période de crise fait partie des "
         "missions de la banque centrale.",
    'p': "Le cours cite La Banque Providence, publiée en 2021, parmi les "
         "analyses qui élargissent ces missions : au soutien de la liquidité "
         "du système bancaire et à la prévention du risque systémique "
         "s’ajoute la stabilisation des marchés, seul moyen d’interrompre une "
         "chaîne de pertes."}],
  [{'f': "Les titres issus de la titrisation sont vendus à travers le monde, "
         "si bien que le risque est dispersé internationalement.",
    'p': "Le fait démontre le premier canal de contagion : quand les défauts "
         "augmentent, par exemple sur les crédits immobiliers à risque, la "
         "crise se propage très vite à l’ensemble des porteurs."},
   {'f': "Si beaucoup d’acteurs sont liés par des contrats d’assurance "
         "contre le défaut, la défaillance d’un gros débiteur peut provoquer "
         "une chaîne de pertes.",
    'p': "Le fait démontre le second canal : la contagion suit la structure "
         "des engagements réciproques, indépendamment de la circulation des "
         "titres eux-mêmes."},
   {'f': "Une crise initialement localisée dans le marché américain des "
         "subprimes a fini par devenir une crise financière mondiale.",
    'p': "Le fait fournit la vérification historique et sa cause : les "
         "systèmes financiers étaient fortement interconnectés, de sorte "
         "qu’une crise locale devient mondiale sans qu’aucun choc "
         "supplémentaire soit nécessaire."},
   {'f': "Le cours relève qu’une bulle liée à l’intelligence artificielle "
         "entraînerait pertes financières, sorties de capitaux et contagion "
         "internationale.",
    'p': "Le fait montre que la grille reste opératoire : la concentration "
         "croissante des flux internationaux sur les actions technologiques "
         "américaines accroît le risque systémique si les valorisations se "
         "révèlent excessives."}],
  [{'q': "Sujet sur la mondialisation financière et les crises",
    'f': "L’intégration financière ne fait pas que déplacer les capitaux, "
         "elle transporte les crises. Le cours l’établit pour 2008 : avant la "
         "crise, les déséquilibres mondiaux avaient fortement augmenté, ils "
         "ont participé à la circulation internationale des capitaux et donc "
         "à la diffusion de la crise financière, si bien qu’une crise "
         "initialement localisée dans le marché américain des subprimes est "
         "devenue mondiale parce que les systèmes financiers étaient "
         "fortement interconnectés.",
    'r': "On montre que le canal de la contagion est le même que celui du "
         "financement, ce qui interdit de conserver l’un en supprimant "
         "l’autre.",
    'ex': "La leçon que le cours en tire : des déséquilibres extérieurs "
          "importants combinés à une forte intégration financière peuvent "
          "transformer une crise locale en crise mondiale."},
   {'q': "Sujet sur la titrisation et le transfert des risques",
    'f': "La titrisation disperse le risque sans le réduire. Le cours "
         "l’énonce sans détour : les titres issus de la titrisation "
         "augmentent la liquidité mais rendent les risques plus opaques et "
         "ont fortement contribué à la diffusion internationale de la crise "
         "de 2008. Comme ces titres sont vendus à travers le monde, le risque "
         "est dispersé internationalement, et quand les défauts augmentent, "
         "la crise se propage très vite.",
    'r': "On sépare deux effets souvent confondus, la dispersion qui allège "
         "chaque porteur et l’opacité qui empêche de savoir qui porte quoi, "
         "pour montrer que c’est la seconde qui rend la contagion générale.",
    'ex': "Le panier mêlant actifs peu risqués et très risqués, dont "
          "l’investisseur ne voit plus la qualité réelle."},
   {'q': "Sujet sur l’interdépendance des économies",
    'f': "L’interdépendance financière crée une responsabilité collective "
         "que les politiques nationales ne peuvent pas porter seules. Le "
         "cours montre que le déficit des uns correspond à la capacité de "
         "financement des autres et que les flux de capitaux permettent à ces "
         "déséquilibres de durer, de sorte qu’ils peuvent créer un risque "
         "systémique. La contagion n’est alors pas un accident mais la "
         "contrepartie de la circulation de l’épargne.",
    'r': "On passe de l’analyse des soldes à celle de leur financement pour "
         "montrer que c’est le mode de financement, et non le niveau du "
         "déséquilibre, qui engendre la fragilité.",
    'ex': "Le constat du cours : les déséquilibres actuels révèlent des "
          "modèles de croissance profondément différents que la "
          "mondialisation financière permet de faire coexister."},
   {'q': "Sujet sur les risques financiers contemporains",
    'f': "La grille de la contagion s’applique aux risques d’aujourd’hui. Le "
         "cours observe que les investisseurs privés achètent davantage "
         "d’actions américaines, notamment dans les entreprises liées à "
         "l’intelligence artificielle, ce qui renforce la concentration "
         "financière, les valorisations élevées et le risque de bulle ; si "
         "cette bulle éclatait, on observerait pertes financières, sorties de "
         "capitaux et contagion internationale.",
    'r': "On applique le mécanisme établi pour 2008 à une configuration "
         "nouvelle, en vérifiant que ses deux conditions, concentration des "
         "expositions et interconnexion, sont réunies.",
    'ex': "La conclusion du cours : la concentration croissante des flux "
          "internationaux sur les actions technologiques américaines accroît "
          "le risque systémique."}],
  voisins=['n13-risque-systemique', 'n13-instabilite-financiere',
           'n13-crise-bancaire', 'n13-panique-bancaire'])


d('n13-alea-moral-sauvetages', 13, "Aléa moral des sauvetages",
  "Protéger le système, c’est aussi encourager l’imprudence",
  "L’aléa moral apparaît lorsqu’un agent, une fois protégé, adopte un "
  "comportement plus risqué qu’avant ; il se produit après la signature du "
  "contrat. Appliqué aux sauvetages financiers, il désigne le fait que la "
  "garantie implicite offerte aux grandes institutions les incite à prendre "
  "davantage de risques. Le cours en tire une ambiguïté fondamentale : la "
  "solution est en même temps une partie du problème.",
  "Le cours construit l’aléa moral comme une défaillance de marché avant de "
  "l’appliquer aux sauvetages, et cet ordre est décisif pour la rigueur du "
  "raisonnement. Le cadre général est celui des asymétries d’information, "
  "dont le cours distingue deux types selon leur moment : avant la signature "
  "du contrat, la sélection adverse ; après la signature, l’aléa moral. "
  "L’aléa moral apparaît donc lorsqu’un agent, une fois protégé, adopte un "
  "comportement plus risqué qu’avant. Le cours en donne trois exemples qui "
  "fonctionnent exactement de la même manière. Le premier est la banque "
  "centrale prêteur en dernier ressort : elle protège le système bancaire, "
  "mais les banques savent qu’elles seront sauvées, donc elles prennent plus "
  "de risques, ce qui conduit à la formule des institutions trop grandes pour "
  "faire faillite. Le deuxième est l’assurance : elle protège contre les "
  "accidents, mais elle peut encourager l’imprudence, conduite plus risquée "
  "et moins de vigilance, selon le raisonnement que l’assurance paiera. Le "
  "troisième est l’annulation des dettes : si les agents savent que leurs "
  "dettes peuvent être annulées, ils prennent plus de risques "
  "d’endettement. Le cours énonce alors la thèse qui fait la valeur de la "
  "notion : les dispositifs de protection sont nécessaires pour stabiliser "
  "l’économie, mais ils créent aussi de l’aléa moral, donc la solution est en "
  "même temps une partie du problème. Et il précise pourquoi c’est une "
  "défaillance de marché : même avec des agents rationnels, le résultat "
  "collectif est sous-optimal. L’application aux sauvetages financiers est "
  "ensuite développée dans le chapitre sur le financement. Les institutions "
  "trop grandes pour faire faillite sont de très grandes institutions "
  "financières dont la faillite pourrait provoquer des dégâts systémiques "
  "majeurs ; elles sont donc souvent perçues comme implicitement protégées, "
  "et le cours tire les trois conséquences : un risque systémique, puisque la "
  "chute d’un grand acteur peut contaminer tout le système ; un aléa moral, "
  "puisque si les acteurs pensent qu’ils seront sauvés ils peuvent prendre "
  "trop de risques, sous-estimer les conséquences et accroître la fragilité "
  "du système ; une socialisation des pertes, puisque les profits peuvent "
  "être privés mais les pertes, en cas de crise, supportées en partie par les "
  "banques centrales, les États, donc indirectement la collectivité. Le cours "
  "retrouve enfin le même mécanisme ailleurs : préserver la stabilité "
  "financière comporte un risque d’aléa moral et peut encourager les "
  "comportements imprudents, les politiques monétaires non conventionnelles "
  "ont pour limite ce même risque, et il existe un aléa moral public, "
  "puisque si l’État sait que la banque centrale peut financer ses dépenses, "
  "il n’a plus d’incitation à maîtriser le déficit ni à contrôler la dette.",
  [("La protection est accordée",
    "Une garantie explicite ou implicite est mise en place : prêteur en "
    "dernier ressort, contrat d’assurance, perspective d’annulation de dette "
    "ou statut d’institution trop grande pour faire faillite."),
   ("Le comportement se modifie après le contrat",
    "Le cours insiste sur la chronologie : l’aléa moral se produit après la "
    "signature du contrat, ce qui le distingue de la sélection adverse, "
    "laquelle opère avant l’échange."),
   ("La prise de risque augmente",
    "Les banques savent qu’elles seront sauvées, donc elles prennent plus de "
    "risques : la garantie modifie le calcul puisqu’elle retire une partie "
    "des conséquences défavorables."),
   ("La fragilité du système s’accroît",
    "Les acteurs peuvent prendre trop de risques, sous-estimer les "
    "conséquences et accroître la fragilité du système : le risque "
    "systémique que la garantie devait prévenir augmente."),
   ("La dissymétrie des résultats",
    "Les profits peuvent être privés, mais les pertes, en cas de crise, être "
    "en partie supportées par les banques centrales, les États, donc "
    "indirectement la collectivité."),
   ("L’impasse",
    "Les dispositifs de protection sont nécessaires pour stabiliser "
    "l’économie mais créent aussi de l’aléa moral : la solution est en même "
    "temps une partie du problème, et le cours n’en propose pas de sortie."),
   ("La version publique du mécanisme",
    "Si l’État sait que la banque centrale peut financer ses dépenses, il "
    "n’a plus d’incitation à maîtriser le déficit ni à contrôler la dette : "
    "le cours parle d’aléa moral public.")],
  [{'a': "La notion explique pourquoi un dispositif de stabilisation peut "
         "produire l’instabilité qu’il devait prévenir, sans supposer "
         "d’irrationalité.",
    'cond': "L’argument suppose que les acteurs anticipent correctement la "
            "garantie, ce que le cours établit par la formule selon laquelle "
            "ils sont perçus comme implicitement protégés.",
    'lim': "Il ne mesure pas l’ampleur de l’effet : savoir que la garantie "
           "existe ne dit pas de combien la prise de risque augmente."},
   {'a': "Elle fonde une critique rigoureuse des sauvetages, interne à la "
         "logique économique et non morale.",
    'cond': "La critique exige que la perte évitée par le sauvetage soit "
            "comparable au surcroît de risque qu’il engendre pour l’avenir.",
    'lim': "Le cours rappelle que la faillite d’une grande banque est "
           "elle-même un exemple de risque systémique : renoncer au "
           "sauvetage ne supprime pas le coût, il le déplace."},
   {'a': "Elle unifie des situations très différentes, du prêteur en dernier "
         "ressort à l’assurance et à l’annulation des dettes.",
    'cond': "L’unification suppose un même mécanisme : une protection "
            "accordée après le contrat qui modifie le comportement du "
            "protégé.",
    'lim': "Les trois cas diffèrent par la réversibilité : un assureur peut "
           "ajuster sa prime ou sa franchise, une banque centrale ne peut "
           "pas tarifer sa garantie implicite."},
   {'a': "Elle éclaire le débat sur l’indépendance de la banque centrale par "
         "la notion d’aléa moral public.",
    'cond': "Le lien suppose que l’État puisse effectivement compter sur la "
            "banque centrale pour financer ses dépenses.",
    'lim': "Le cours note le revers : sans cette possibilité, la banque "
           "centrale perd un instrument, et son indépendance pose le "
           "problème démocratique que soulèvent les analyses récentes."},
   {'a': "Elle qualifie précisément le problème comme une défaillance de "
         "marché, et non comme une faute des acteurs.",
    'cond': "La qualification suppose que le résultat collectif soit "
            "sous-optimal même avec des agents rationnels, ce que le cours "
            "affirme explicitement.",
    'lim': "Cette qualification ferme la voie d’une solution par "
           "l’information : contrairement à la sélection adverse, l’aléa "
           "moral ne se corrige pas en révélant une qualité cachée avant "
           "l’échange."}],
  [{'t': "Il faut supprimer les garanties implicites et laisser faire "
         "faillite les institutions imprudentes, seule manière de rétablir "
         "la discipline.",
    'qui': "La conclusion que l’on tire habituellement de l’analyse de "
           "l’aléa moral.",
    'rep': "Le cours refuse cette issue en rappelant que les dispositifs de "
           "protection sont nécessaires pour stabiliser l’économie : la "
           "faillite d’une grande banque figure parmi ses exemples de risque "
           "systémique, donc la sanction est elle-même le dommage."},
   {'t': "Le problème n’est pas l’aléa moral mais la taille : il suffirait de "
         "séparer les activités bancaires pour que la garantie devienne "
         "inutile.",
    'qui': "L’argument de la séparation des activités que le cours présente "
           "à propos de la banque universelle.",
    'rep': "Le cours admet l’intérêt de cette séparation pour la stabilité, "
           "mais le risque de liquidité subsiste dans toute banque de "
           "dépôts : il faut donc toujours un soutien de liquidité, donc une "
           "garantie."},
   {'t': "L’aléa moral relève de l’information imparfaite et se corrigerait "
         "par plus de transparence sur les engagements des acteurs.",
    'qui': "La lecture par l’asymétrie d’information que le cours rattache à "
           "George Akerlof.",
    'rep': "Le cours distingue les deux types : la transparence traite la "
           "sélection adverse, qui opère avant l’échange, tandis que l’aléa "
           "moral se produit après la signature du contrat et porte sur un "
           "comportement, non sur une qualité cachée."},
   {'t': "Les politiques monétaires non conventionnelles sont justifiées par "
         "l’urgence : l’objection d’aléa moral est secondaire face au risque "
         "de déflation.",
    'qui': "La justification des instruments non conventionnels que le cours "
           "expose avant d’en indiquer la limite.",
    'rep': "Le cours maintient l’objection comme limite principale de ces "
           "politiques, précisément parce que l’urgence invoquée se "
           "reproduira si la garantie a nourri entre-temps des comportements "
           "plus imprudents."}],
  [{'n': "George Akerlof",
    'i': "L’asymétrie d’information peut faire disparaître un marché, les "
         "mauvais produits chassant les bons.",
    'p': "Le cours cite The Market for Lemons, publié en 1970, et organise "
         "autour de cette analyse la distinction des deux grands types "
         "d’asymétrie : avant la signature du contrat la sélection adverse, "
         "après la signature l’aléa moral."},
   {'n': "George Akerlof",
    'i': "La sélection adverse fait que les mauvaises voitures chassent les "
         "bonnes sur le marché de l’occasion.",
    'p': "Le cours détaille le mécanisme, le vendeur sachant si la voiture "
         "est bonne et l’acheteur l’ignorant, puis le transpose au crédit "
         "bancaire : la banque relève ses taux, les emprunteurs prudents "
         "renoncent et elle attire surtout les mauvais profils."},
   {'n': "Éric Monnet",
    'i': "La banque centrale est devenue un pilier de la stabilité "
         "financière, ce qui pose la question de son contrôle démocratique.",
    'p': "Le cours cite La Banque Providence, publiée en 2021, et son mot "
         "d’ordre de démocratiser les banques centrales et la monnaie, au "
         "moment précis où il relève que la garantie de stabilité financière "
         "comporte un risque d’aléa moral."}],
  [{'f': "Le cours définit l’aléa moral comme le fait qu’un agent, une fois "
         "protégé, adopte un comportement plus risqué qu’avant, après la "
         "signature du contrat.",
    'p': "La définition montre que le problème est chronologique et non "
         "informationnel au sens strict : il ne porte pas sur une qualité "
         "cachée mais sur une conduite qui change une fois la protection "
         "acquise."},
   {'f': "Le cours donne trois exemples parallèles : la banque centrale "
         "prêteur en dernier ressort, l’assurance et l’annulation des dettes.",
    'p': "Le parallélisme démontre la généralité du mécanisme : qu’il "
         "s’agisse d’une banque, d’un conducteur ou d’un débiteur, la "
         "protection retire une partie des conséquences et modifie le "
         "calcul."},
   {'f': "Le cours énonce l’ambiguïté fondamentale : les dispositifs de "
         "protection sont nécessaires pour stabiliser l’économie, mais ils "
         "créent aussi de l’aléa moral.",
    'p': "La formule démontre qu’il n’existe pas de solution sans coût, le "
         "cours concluant que la solution est en même temps une partie du "
         "problème."},
   {'f': "Avec les institutions trop grandes pour faire faillite, les profits "
         "peuvent être privés mais les pertes supportées par les banques "
         "centrales, les États, donc la collectivité.",
    'p': "Le fait montre la dissymétrie que produit la garantie implicite : "
         "elle ne supprime pas la perte, elle en change le porteur, ce qui "
         "explique l’enjeu politique des sauvetages."}],
  [{'q': "Sujet sur les défaillances de marché",
    'f': "L’aléa moral est une défaillance de marché qui résiste à "
         "l’information. Le cours le définit comme le fait qu’un agent, une "
         "fois protégé, adopte un comportement plus risqué qu’avant, et "
         "précise que cela se produit après la signature du contrat. C’est "
         "pourquoi il s’agit d’une défaillance : même avec des agents "
         "rationnels, le résultat collectif est sous-optimal, et la "
         "transparence ne corrige pas un comportement futur.",
    'r': "On distingue la sélection adverse, qui porte sur une qualité "
         "cachée avant l’échange, et l’aléa moral, qui porte sur une conduite "
         "après l’échange, afin de montrer que les remèdes ne sont pas les "
         "mêmes.",
    'ex': "Les trois exemples du cours : prêteur en dernier ressort, "
          "assurance et annulation des dettes."},
   {'q': "Sujet sur les sauvetages bancaires et leur légitimité",
    'f': "Le sauvetage d’une grande banque est à la fois nécessaire et "
         "coûteux. Le cours montre que les institutions trop grandes pour "
         "faire faillite sont si grandes et si centrales que leur faillite "
         "menacerait le système bancaire, les paiements, le crédit et "
         "l’économie réelle, ce qui les fait percevoir comme implicitement "
         "protégées ; mais si les acteurs pensent qu’ils seront sauvés, ils "
         "peuvent prendre trop de risques et accroître la fragilité du "
         "système.",
    'r': "On met en balance le coût immédiat d’une faillite systémique et le "
         "coût différé de l’incitation qu’engendre la garantie, pour montrer "
         "que le choix est un arbitrage temporel et non un choix entre bien "
         "et mal.",
    'ex': "La socialisation des pertes relevée par le cours : profits privés, "
          "pertes supportées en partie par les banques centrales et les "
          "États."},
   {'q': "Sujet sur les limites de la politique monétaire",
    'f': "L’aléa moral est la limite que le cours assigne explicitement aux "
         "politiques monétaires non conventionnelles. Celles-ci visent à "
         "rétablir la liquidité, débloquer le crédit, éviter la déflation, "
         "stabiliser les marchés et soutenir l’activité, mais elles "
         "encouragent les comportements imprudents. Le même mécanisme vaut "
         "pour la stabilité financière elle-même, dont le cours précise "
         "qu’elle comporte un risque d’aléa moral.",
    'r': "On montre que la limite n’est pas technique mais incitative : "
         "l’instrument fonctionne, et c’est son efficacité même qui modifie "
         "les comportements futurs.",
    'ex': "La mention du cours sur les politiques non conventionnelles, dont "
          "il fait de l’aléa moral la limite principale."},
   {'q': "Sujet sur l’indépendance de la banque centrale",
    'f': "L’aléa moral existe aussi du côté de l’État. Le cours le nomme "
         "aléa moral public : si l’État sait que la banque centrale peut "
         "financer ses dépenses, il n’a plus d’incitation à maîtriser le "
         "déficit ni à contrôler la dette, la banque centrale devenant un "
         "outil du gouvernement et perdant sa crédibilité dans la lutte "
         "contre l’inflation.",
    'r': "On transpose le mécanisme du secteur bancaire à l’État pour "
         "montrer que l’argument d’indépendance repose sur une logique "
         "d’incitation, et non sur une défiance envers le politique.",
    'ex': "Le risque de dérive permanente relevé par le cours, avec des "
          "dépenses financées par création monétaire sans contrepartie "
          "productive immédiate."}],
  voisins=['n13-risque-systemique', 'n13-crise-bancaire',
           'n13-panique-bancaire', 'n13-instabilite-financiere'])
