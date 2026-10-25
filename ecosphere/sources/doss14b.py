# -*- coding: utf-8 -*-
"""Ensemble 14 — L’inflation et la stabilité des prix (2/4)."""

from doss_base import d

d('n14-inflation-demande', 14, "Inflation par la demande",
  "Les prix montent parce que la dépense dépasse les capacités",
  "Le cours énonce la cause générale de l’inflation en une ligne : la "
  "demande augmente plus vite que l’offre. L’inflation par la demande "
  "désigne ce mécanisme, où la dépense excède ce que l’appareil productif "
  "peut fournir. Le chapitre sur la croissance en donne la mesure avec "
  "l’output gap positif, qui signale une économie en surchauffe et des "
  "tensions inflationnistes possibles.",
  "Le cours traite l’inflation par la demande à trois endroits qui "
  "s’emboîtent, et cette dispersion est elle-même instructive. Le premier "
  "est la cause posée directement : la cause de l’inflation est que la "
  "demande augmente plus vite que l’offre. L’énoncé est volontairement "
  "général, puisqu’il ne dit pas d’où vient le surcroît de demande. Le "
  "deuxième endroit en donne la mesure. Le chapitre sur la croissance "
  "définit la croissance potentielle comme le rythme que l’économie pourrait "
  "atteindre si tous les facteurs de production étaient pleinement utilisés, "
  "sans tension inflationniste, puis l’output gap comme l’écart entre "
  "croissance effective et croissance potentielle. Lorsque la croissance "
  "effective dépasse la croissance potentielle, l’output gap est positif et "
  "l’économie est en surchauffe, avec pour conséquences possibles des "
  "pénuries de capacités de production, une hausse des salaires et un risque "
  "d’inflation. Le chapitre sur la pauvreté et le circuit économique donne "
  "la même idée sous une autre forme : lorsque l’output gap est positif, les "
  "entreprises peuvent décider d’augmenter les prix au lieu d’augmenter les "
  "capacités de production. Le mécanisme est donc précis : le surcroît de "
  "demande se heurte à une contrainte de capacité, et l’ajustement se fait "
  "par les prix parce qu’il ne peut plus se faire par les quantités. Le "
  "troisième endroit est monétaire, et il explique d’où vient le surcroît de "
  "demande dans les économies contemporaines : un crédit trop dynamique "
  "entraîne une masse monétaire en hausse, donc une demande plus forte, donc "
  "des tensions sur les prix, donc l’inflation. C’est ce que le cours appelle "
  "le canal du crédit bancaire, et c’est par lui que la banque centrale agit, "
  "en modifiant ses taux directeurs pour influencer le coût du crédit, la "
  "demande de financement, la création monétaire, la demande globale et "
  "l’inflation. L’inflation par la demande est donc le cas où l’instrument "
  "monétaire est le mieux adapté : freiner la dépense traite directement la "
  "cause. Le cours relie enfin ce mécanisme à l’analyse keynésienne, qui "
  "fait de la demande globale le déterminant de la production : "
  "l’intervention publique qui soutient la demande en sous-activité devient "
  "inflationniste lorsque l’économie est déjà proche de ses capacités, ce qui "
  "est exactement l’objet de la critique monétariste.",
  [("Le surcroît de dépense",
    "La demande adressée aux entreprises augmente, qu’elle vienne de la "
    "consommation, de l’investissement, de la dépense publique ou des "
    "exportations : le cours résume cette situation en disant que la demande "
    "augmente plus vite que l’offre."),
   ("La contrainte de capacité",
    "L’appareil productif ne peut suivre : le cours décrit des pénuries de "
    "capacités de production lorsque l’économie produit plus que ce qu’elle "
    "peut soutenir durablement."),
   ("L’arbitrage de l’entreprise",
    "Le cours énonce le choix décisif : avec un output gap positif, les "
    "entreprises peuvent décider d’augmenter les prix au lieu d’augmenter "
    "les capacités de production."),
   ("La tension sur les salaires",
    "L’économie en surchauffe connaît une hausse des salaires, le cours "
    "l’inscrivant parmi les conséquences possibles d’un output gap positif, "
    "ce qui alimente à son tour les coûts."),
   ("L’origine monétaire du surcroît de demande",
    "Un crédit trop dynamique accroît la masse monétaire, donc la demande, "
    "donc les tensions sur les prix : le cours en fait l’enchaînement central "
    "de la politique monétaire."),
   ("La réponse par le resserrement",
    "La banque centrale relève ses taux directeurs, ce qui renchérit le "
    "crédit, réduit la demande de financement puis la demande globale : "
    "l’instrument agit sur la cause même.")],
  [{'a': "L’explication par la demande donne un diagnostic mesurable grâce à "
         "l’écart entre croissance effective et croissance potentielle.",
    'cond': "La mesure suppose une estimation fiable de la croissance "
            "potentielle, définie comme le rythme atteignable sans tension "
            "inflationniste.",
    'lim': "Le cours rappelle que la croissance potentielle est une "
           "croissance théorique, une référence et non la croissance "
           "réellement observée : l’output gap hérite de cette incertitude."},
   {'a': "Elle désigne l’instrument adapté, puisque freiner la dépense traite "
         "directement la cause du mouvement des prix.",
    'cond': "L’efficacité suppose que les banques répercutent la hausse du "
            "refinancement sur le coût du crédit et que la demande y soit "
            "sensible.",
    'lim': "Le cours relève le dilemme classique : freiner l’inflation peut "
           "entrer en tension avec le soutien de l’activité, entre relancer "
           "et maîtriser les prix."},
   {'a': "Elle explique pourquoi une relance budgétaire ou monétaire peut "
         "devenir inflationniste selon le moment où elle intervient.",
    'cond': "L’argument suppose que l’économie soit déjà proche du plein "
            "emploi de ses facteurs, sans quoi la relance mobilise des "
            "ressources inemployées.",
    'lim': "Les monétaristes en tirent une conclusion plus radicale que le "
           "cours : pour eux les politiques de relance budgétaire sont "
           "inflationnistes en toute circonstance."},
   {'a': "Elle articule l’analyse réelle et l’analyse monétaire par le "
         "crédit, qui est à la fois dépense et création de monnaie.",
    'cond': "L’articulation suppose, comme le cours l’établit, que la "
            "création monétaire dépende largement du crédit bancaire.",
    'lim': "Dans la lecture quantitativiste, la causalité est inverse : la "
           "monnaie est exogène et décidée par les autorités monétaires, non "
           "engendrée par la demande de crédit."},
   {'a': "Elle fournit le fondement de l’objectif traditionnel de stabilité "
         "des prix assigné aux banques centrales.",
    'cond': "Le fondement suppose que la banque centrale puisse agir sur le "
            "rythme du crédit avant que les tensions ne se transmettent aux "
            "salaires.",
    'lim': "Le cours montre que l’outil est asymétrique : il freine mieux "
           "qu’il ne relance, comme l’atteste la trappe à liquidité."}],
  [{'t': "L’inflation ne vient pas de la demande mais de la quantité de "
         "monnaie : elle est toujours et partout un phénomène monétaire.",
    'qui': "Milton Friedman, dans l’énoncé de la théorie quantitative que le "
           "cours date de 1956.",
    'rep': "Le cours réunit les deux lectures par le canal du crédit : un "
           "crédit trop dynamique accroît à la fois la masse monétaire et la "
           "demande, de sorte que la cause monétaire et la cause réelle "
           "coïncident dans le même mécanisme."},
   {'t': "La hausse des prix vient des coûts, non de la demande : les "
         "entreprises répercutent ce qu’elles subissent en amont.",
    'qui': "La lecture par les coûts que le cours illustre avec le choc "
           "pétrolier des années soixante-dix.",
    'rep': "Le cours distingue les deux cas par la direction de l’activité : "
           "une inflation par la demande s’accompagne d’une production "
           "élevée, une inflation par les coûts d’un chômage en hausse, "
           "c’est-à-dire de la stagflation."},
   {'t': "Soutenir la demande ne crée pas d’inflation puisque l’économie est "
         "presque toujours en deçà de ses capacités.",
    'qui': "La lecture keynésienne de l’insuffisance de demande que le cours "
           "développe avec Keynes et Harrod.",
    'rep': "Le cours maintient la condition : l’argument vaut en "
           "sous-activité, mais avec un output gap positif les entreprises "
           "peuvent décider d’augmenter les prix au lieu des capacités."},
   {'t': "Une demande forte est désirable : les tensions sur les prix sont le "
         "signe d’une économie dynamique, non un problème.",
    'qui': "La lecture qui privilégie l’activité sur la stabilité des prix, "
           "que le cours situe dans les années soixante et soixante-dix.",
    'rep': "Le cours rappelle que l’objectif central des banques centrales "
           "modernes est la stabilité des prix, et que la surchauffe se paie "
           "en pénuries de capacités et en perte de pouvoir d’achat."}],
  [{'n': "John Maynard Keynes",
    'i': "L’économie repose sur la demande, qui détermine la production et "
         "l’emploi.",
    'p': "Le cours en fait l’économiste le plus connu de cette approche. "
         "Appliquée à l’inflation, la thèse implique qu’un surcroît de "
         "demande augmente d’abord la production, puis les prix lorsque les "
         "capacités sont saturées : c’est la bascule que mesure l’output "
         "gap."},
   {'n': "Milton Friedman",
    'i': "Un crédit et une masse monétaire trop dynamiques font monter les "
         "prix plus que la production.",
    'p': "Le cours rapporte sa formule selon laquelle si la quantité de "
         "monnaie croît plus vite que la production, les prix augmentent, et "
         "précise qu’à long terme la monnaie est neutre : elle n’influence ni "
         "la production ni l’emploi, seulement le niveau des prix."},
   {'n': "Alban William Phillips",
    'i': "Quand le chômage est faible, les salaires nominaux progressent "
         "plus vite.",
    'p': "Le cours rapporte son observation de 1958 sur le Royaume-Uni entre "
         "1861 et 1957, et en tire le lien avec l’inflation par la demande : "
         "un marché du travail tendu alimente les salaires, donc les coûts, "
         "donc les prix."}],
  [{'f': "Le cours énonce directement la cause de l’inflation : la demande "
         "augmente plus vite que l’offre.",
    'p': "La formule montre que l’inflation est d’abord pensée comme un "
         "déséquilibre entre deux flux, et non comme une propriété de la "
         "monnaie : c’est le point de départ de toute l’analyse."},
   {'f': "Un output gap positif signale une économie en surchauffe, avec "
         "pénuries de capacités de production, hausse des salaires et risque "
         "d’inflation.",
    'p': "L’énumération donne les trois symptômes à repérer : elle "
         "transforme un énoncé théorique en grille de diagnostic "
         "conjoncturel."},
   {'f': "Avec un output gap positif, les entreprises peuvent décider "
         "d’augmenter les prix au lieu d’augmenter les capacités de "
         "production.",
    'p': "Le fait désigne le moment de la décision : l’inflation naît d’un "
         "choix d’entreprise rendu possible par la saturation, et non d’un "
         "automatisme."},
   {'f': "Le cours décrit l’enchaînement monétaire : crédit trop dynamique, "
         "masse monétaire en hausse, demande plus forte, tensions sur les "
         "prix, inflation.",
    'p': "La chaîne montre que la demande excédentaire a une source "
         "identifiable et contrôlable, ce qui justifie que la banque centrale "
         "agisse sur le coût du crédit."}],
  [{'q': "Sujet sur les causes de l’inflation",
    'f': "La cause la plus simple de l’inflation est aussi celle que le "
         "cours retient d’abord : la demande augmente plus vite que l’offre. "
         "Le mécanisme se précise avec l’output gap, écart entre croissance "
         "effective et croissance potentielle : lorsqu’il est positif, "
         "l’économie est en surchauffe, et les entreprises peuvent décider "
         "d’augmenter les prix au lieu d’augmenter les capacités de "
         "production.",
    'r': "On montre que l’inflation naît d’une contrainte de capacité, ce "
         "qui explique pourquoi la même hausse de demande est bénéfique en "
         "sous-activité et inflationniste en surchauffe.",
    'ex': "Les conséquences d’un output gap positif selon le cours : "
          "pénuries de capacités, hausse des salaires, risque d’inflation."},
   {'q': "Sujet sur l’efficacité des politiques de relance",
    'f': "Une relance n’a pas les mêmes effets selon l’état de l’économie. "
         "Le cours permet de le montrer précisément : en sous-activité, "
         "soutenir la demande mobilise des capacités inemployées et accroît "
         "la production ; avec un output gap positif, la même impulsion se "
         "heurte à des pénuries de capacités et se transmet aux prix. "
         "L’efficacité d’une relance dépend donc du diagnostic conjoncturel "
         "qui la précède.",
    'r': "On conditionne l’effet d’un instrument à l’état des capacités, ce "
         "qui permet de dépasser l’opposition abstraite entre keynésiens et "
         "monétaristes.",
    'ex': "Le choix d’entreprise décrit par le cours entre augmenter les prix "
          "et augmenter les capacités."},
   {'q': "Sujet sur monnaie, crédit et prix",
    'f': "L’inflation par la demande et l’explication monétaire ne "
         "s’opposent pas, elles se rejoignent par le crédit. Le cours donne "
         "l’enchaînement : un crédit trop dynamique accroît la masse "
         "monétaire, donc la demande, donc les tensions sur les prix. La "
         "politique monétaire agit alors principalement par le canal du "
         "crédit bancaire, la banque centrale modifiant ses taux directeurs "
         "pour influencer le coût du crédit puis la demande globale.",
    'r': "On montre que le crédit est simultanément création de monnaie et "
         "financement de la dépense, ce qui fait coïncider la cause monétaire "
         "et la cause réelle.",
    'ex': "La chaîne de transmission du cours : taux directeurs, marché "
          "interbancaire, taux bancaires, coût du crédit, demande de "
          "financement, création monétaire, demande globale, inflation."},
   {'q': "Sujet sur l’arbitrage entre croissance et stabilité des prix",
    'f': "Le cours présente la stabilité des prix et le soutien de "
         "l’activité comme deux objectifs potentiellement contradictoires. "
         "Il nomme ce conflit le dilemme classique : relancer l’activité ou "
         "maîtriser l’inflation. L’inflation par la demande est précisément "
         "le cas où ce dilemme est le plus vif, puisque le même instrument, "
         "le taux directeur, agit en sens inverse sur les deux objectifs.",
    'r': "On montre que l’arbitrage n’existe que dans la zone où la demande "
         "bute sur les capacités, ce qui ramène le débat à une question de "
         "position dans le cycle.",
    'ex': "Le dilemme classique tel que le cours le formule parmi les "
          "objectifs de la politique monétaire."}],
  voisins=['n14-inflation', 'n14-inflation-couts', 'n14-boucle-prix-salaires',
           'n13-chocs-offre-demande'])


d('n14-inflation-couts', 14, "Inflation par les coûts",
  "Les prix montent parce que produire coûte plus cher",
  "L’inflation par les coûts désigne la hausse des prix provoquée par le "
  "renchérissement des facteurs de production, et non par un excès de "
  "demande. Le cours en donne le cas de référence avec les chocs pétroliers : "
  "les firmes voient leurs coûts augmenter, donc elles sont obligées de "
  "licencier, d’où inflation et chômage simultanés, configuration que le "
  "cours nomme stagflation.",
  "Le cours n’emploie pas l’expression consacrée mais décrit le mécanisme "
  "avec une grande précision, et c’est sa conséquence théorique qui en fait "
  "l’intérêt. Le point de départ est factuel : dans les années quarante, la "
  "majorité des économistes défendent l’idée que l’investissement et le "
  "profit dépendent de la demande. Mais en 1973 le monde connaît un choc "
  "pétrolier, c’est-à-dire une forte hausse du prix du baril, puis un second "
  "en 1979, le baril passant au total de cinq à trente dollars, ce qui "
  "entraîne une forte hausse du chômage en raison d’un fort taux de "
  "licenciement en réponse à la hausse des coûts de production. Le mécanisme "
  "est donc explicite : lors du choc pétrolier, les firmes voient leurs coûts "
  "augmenter, donc elles sont obligées de licencier, d’où inflation et "
  "chômage. La conséquence est décisive pour l’analyse : c’est la "
  "stagflation, stagnation de la production et inflation, et cela détruit "
  "expérimentalement la courbe de Phillips, parce que l’inflation n’a pas "
  "fait baisser le chômage et qu’on a eu les deux, inflation et chômage "
  "élevé. L’inflation par les coûts est donc le mécanisme par lequel une "
  "relation empirique jusque-là tenue pour stable s’effondre. Le cours en "
  "tire aussi un effet doctrinal : dans les années quatre-vingt-dix, les "
  "économistes qui défendent l’idée que l’investissement et le profit "
  "reposent sur l’offre reprennent de l’élan, appuyés par le discours du "
  "chancelier allemand Helmut Schmidt selon lequel les profits d’aujourd’hui "
  "font les investissements de demain. Le cours ajoute une seconde source de "
  "renchérissement, extérieure celle-là : des importations plus chères "
  "élèvent les coûts de production, donc les prix domestiques, ce qui engendre "
  "l’inflation importée. Enfin, les salaires peuvent eux-mêmes constituer le "
  "coût qui s’élève, selon l’enchaînement que le cours expose à propos de la "
  "courbe de Phillips : quand le chômage est faible, les salariés demandent "
  "des hausses de salaires, ce qui augmente les coûts, donc les prix. "
  "L’inflation par les coûts est ainsi le point où les prix cessent d’être un "
  "signal de rareté pour devenir la répercussion d’une contrainte subie.",
  [("Le renchérissement d’un facteur",
    "Le prix d’un intrant essentiel augmente brutalement : le cours prend "
    "l’exemple du pétrole, dont le baril passe de cinq à trente dollars entre "
    "1973 et 1979."),
   ("La hausse des coûts de production",
    "Les entreprises subissent une hausse de leurs coûts qu’elles n’ont pas "
    "décidée : le cours parle d’une hausse des coûts de production à laquelle "
    "elles doivent répondre."),
   ("La répercussion sur les prix de vente",
    "Pour préserver leurs marges, les entreprises augmentent leurs prix : "
    "l’inflation apparaît sans qu’aucun excès de demande ne soit en cause."),
   ("La réduction de l’emploi",
    "Le cours insiste sur le second effet, simultané : les firmes sont "
    "obligées de licencier, ce qui produit une forte hausse du chômage en "
    "raison d’un fort taux de licenciement."),
   ("La stagflation",
    "Inflation et chômage augmentent ensemble : c’est la stagflation, "
    "stagnation de la production et inflation, configuration que la courbe de "
    "Phillips jugeait improbable."),
   ("La version extérieure du mécanisme",
    "Des importations plus chères élèvent les coûts de production puis les "
    "prix domestiques : le cours en fait l’inflation importée, variante du "
    "même enchaînement dont la cause est le change."),
   ("La version salariale du mécanisme",
    "Quand le chômage est faible, les salariés demandent des hausses de "
    "salaires, ce qui augmente les coûts puis les prix : les salaires "
    "deviennent le coût qui s’élève.")],
  [{'a': "L’explication par les coûts rend compte d’une configuration que "
         "l’explication par la demande ne peut pas produire, l’inflation avec "
         "chômage.",
    'cond': "L’argument suppose que les entreprises puissent répercuter la "
            "hausse de leurs coûts sur leurs prix, donc qu’elles disposent "
            "d’un pouvoir de marché.",
    'lim': "Si la concurrence est vive, la hausse des coûts comprime les "
           "marges plutôt que les prix : l’effet se manifeste alors en "
           "faillites et en chômage plus qu’en inflation."},
   {'a': "Elle fournit la réfutation empirique de la courbe de Phillips, que "
         "le cours qualifie de destruction expérimentale.",
    'cond': "La réfutation exige que l’inflation et le chômage aient "
            "effectivement augmenté ensemble, ce que le cours affirme pour "
            "les années soixante-dix.",
    'lim': "Les monétaristes proposent une autre explication du même fait, "
           "l’abandon de l’illusion monétaire : le choc d’offre n’est alors "
           "que l’occasion du retournement, non sa cause."},
   {'a': "Elle montre les limites des politiques de demande, qui aggravent "
         "l’inflation sans restaurer l’emploi.",
    'cond': "La conclusion suppose que la contrainte dominante soit bien le "
            "coût de production et non l’insuffisance de débouchés.",
    'lim': "Le cours rappelle que l’investissement est à la fois un élément "
           "de la demande et un élément de l’offre : négliger la demande "
           "conduit à une erreur symétrique."},
   {'a': "Elle explique le retournement doctrinal en faveur des analyses par "
         "l’offre et par les profits.",
    'cond': "Le lien suppose que la rentabilité ait été la contrainte "
            "effective sur l’investissement après les chocs pétroliers.",
    'lim': "Le cours présente ce retour comme un mouvement d’idées daté, "
           "appuyé par un discours politique, et non comme une démonstration "
           "économique achevée."},
   {'a': "Elle se décline en une version extérieure qui relie les prix "
         "domestiques au taux de change.",
    'cond': "La déclinaison suppose une dépendance forte à des biens "
            "libellés en devises étrangères, condition que le cours énonce "
            "pour l’inflation importée.",
    'lim': "Le cours rappelle que la dépréciation a aussi un effet "
           "favorable, en rendant les exportations moins chères, de sorte que "
           "le résultat net dépend du délai de réaction des volumes."}],
  [{'t': "L’inflation reste toujours et partout un phénomène monétaire : un "
         "choc de coût ne peut pas élever durablement le niveau général des "
         "prix.",
    'qui': "Milton Friedman et l’école monétariste, dont le cours expose la "
           "thèse quantitative.",
    'rep': "Le cours constate pourtant le fait : le choc pétrolier produit "
           "inflation et chômage, et les monétaristes eux-mêmes expliquent "
           "l’épisode par les anticipations plutôt que par la quantité de "
           "monnaie, ce qui déplace leur propre argument."},
   {'t': "Il n’existe pas d’inflation par les coûts : une hausse de prix "
         "relatif n’est pas une hausse du niveau général des prix.",
    'qui': "L’objection analytique issue de la tradition quantitativiste.",
    'rep': "Le cours répond par le canal de l’emploi : la hausse du prix du "
           "pétrole ne se limite pas à un prix relatif, elle provoque des "
           "licenciements et une hausse générale des prix, ce qu’atteste la "
           "stagflation."},
   {'t': "La solution est de modérer les salaires, puisque c’est la "
         "répercussion salariale qui transforme un choc en inflation "
         "durable.",
    'qui': "L’argument issu de l’analyse de la boucle entre prix et "
           "salaires que le cours expose.",
    'rep': "Le cours montre que la modération salariale a un coût de "
           "demande : la compression des salaires limite la demande "
           "domestique, ce qui peut conduire à la surproduction selon "
           "l’enchaînement qu’il rattache à Marx."},
   {'t': "Un choc d’offre justifie au contraire une politique de soutien de "
         "la demande, pour éviter que le chômage ne s’installe.",
    'qui': "La lecture keynésienne du soutien de l’activité que le cours "
           "présente ailleurs.",
    'rep': "Le cours relève l’impasse : soutenir la dépense après un choc de "
           "coût nourrit l’inflation sans lever la contrainte, et le constat "
           "des années soixante-dix est que la politique monétaire est "
           "impuissante à réduire le chômage."}],
  [{'n': "Milton Friedman",
    'i': "Les agents ne sont plus victimes de l’illusion monétaire, ils "
         "anticipent, donc la politique monétaire ne marche plus.",
    'p': "Le cours rapporte cette lecture monétariste de la stagflation : "
         "là où les keynésiens voyaient un choc de coût, les friedmaniens "
         "voient la fin de l’illusion monétaire, les salariés réclamant des "
         "hausses de salaires nominaux dès qu’ils voient monter les prix."},
   {'n': "Alban William Phillips",
    'i': "Il existe une relation inverse entre le chômage et la croissance "
         "des salaires nominaux.",
    'p': "Le cours rapporte son étude de 1958 sur le Royaume-Uni entre 1861 "
         "et 1957, et précise que la relation n’est ni linéaire ni stable : "
         "c’est cette instabilité que la stagflation des années soixante-dix "
         "rend manifeste."},
   {'n': "John Maynard Keynes",
    'i': "L’inflation peut réduire le chômage parce que la hausse des prix "
         "abaisse le salaire réel.",
    'p': "Le cours présente cette lecture, partagée avec Phillips, Samuelson "
         "et Solow, comme l’analyse dominante des années cinquante et "
         "soixante : inflation, baisse des salaires réels, hausse des "
         "embauches, c’est précisément ce que le choc de coût vient "
         "démentir."}],
  [{'f': "En 1973 survient un premier choc pétrolier, puis un second en "
         "1979 ; le baril passe au total de cinq à trente dollars.",
    'p': "Le chiffre donne l’ampleur du renchérissement : il explique "
         "pourquoi un seul prix a pu déplacer le niveau général des prix de "
         "toutes les économies industrielles."},
   {'f': "Le cours relie le choc à une forte hausse du chômage, en raison "
         "d’un fort taux de licenciement en réponse à la hausse des coûts de "
         "production.",
    'p': "Le fait démontre la signature propre de l’inflation par les "
         "coûts : prix et chômage augmentent ensemble, alors qu’une inflation "
         "par la demande s’accompagne d’un chômage faible."},
   {'f': "Le cours conclut que la stagflation détruit expérimentalement la "
         "courbe de Phillips, puisque l’inflation n’a pas fait baisser le "
         "chômage.",
    'p': "Le fait montre la portée théorique du mécanisme : un choc de coût "
         "ne modifie pas seulement la conjoncture, il invalide une relation "
         "empirique sur laquelle reposait la politique économique."},
   {'f': "Le chancelier allemand Helmut Schmidt déclare que les profits "
         "d’aujourd’hui font les investissements de demain.",
    'p': "La citation, rapportée par le cours, montre l’effet doctrinal du "
         "choc : elle appuie le retour des analyses de l’investissement par "
         "l’offre et les profits dans les années quatre-vingt-dix."}],
  [{'q': "Sujet sur inflation et chômage",
    'f': "Un choc de coût rend possible ce qu’aucune analyse par la demande "
         "n’autorise : l’inflation avec le chômage. Le cours le démontre par "
         "le choc pétrolier, où les firmes voient leurs coûts augmenter, donc "
         "elles sont obligées de licencier, d’où inflation et chômage. C’est "
         "la stagflation, qui détruit expérimentalement la courbe de Phillips "
         "puisque l’inflation n’a pas fait baisser le chômage.",
    'r': "On montre que la direction conjointe des prix et de l’emploi "
         "suffit à identifier l’origine du choc, ce qui fait de la "
         "stagflation la signature de l’inflation par les coûts.",
    'ex': "Les chocs de 1973 et 1979, le baril passant de cinq à trente "
          "dollars."},
   {'q': "Sujet sur les déterminants de l’investissement",
    'f': "Le choc de coût a déplacé la doctrine autant que l’économie. Le "
         "cours rappelle que dans les années quarante la majorité des "
         "économistes défendent l’idée que l’investissement et le profit "
         "dépendent de la demande, mais qu’après les deux chocs pétroliers, "
         "dans les années quatre-vingt-dix, ceux qui défendent l’idée que "
         "l’investissement repose sur l’offre reprennent de l’élan, appuyés "
         "par le discours du chancelier Helmut Schmidt.",
    'r': "On montre qu’un choc exogène peut modifier la hiérarchie des "
         "causes reconnues, ce qui invite à historiciser les théories plutôt "
         "qu’à les opposer abstraitement.",
    'ex': "La formule rapportée par le cours : les profits d’aujourd’hui "
          "font les investissements de demain."},
   {'q': "Sujet sur les limites des politiques conjoncturelles",
    'f': "Une inflation par les coûts met les deux instruments "
         "conjoncturels en échec. Soutenir la demande nourrit l’inflation "
         "sans lever la contrainte de coût ; resserrer la monnaie aggrave le "
         "chômage déjà provoqué par les licenciements. Le cours constate "
         "d’ailleurs qu’à l’issue de l’épisode la politique monétaire est "
         "impuissante à réduire le chômage, et que les monétaristes en "
         "concluent à l’inefficacité des politiques discrétionnaires.",
    'r': "On montre que l’impasse vient de ce qu’un seul instrument doit "
         "traiter deux déséquilibres de sens opposé, ce qui déplace la "
         "réponse vers les politiques structurelles.",
    'ex': "La conclusion des friedmaniens rapportée par le cours : la "
          "monnaie est puissante mais la politique monétaire est "
          "impuissante."},
   {'q': "Sujet sur la transmission internationale de l’inflation",
    'f': "L’inflation par les coûts a une variante extérieure que le cours "
         "nomme inflation importée. Le mécanisme est le même, seule la "
         "source change : des importations plus chères élèvent les coûts de "
         "production, donc les prix domestiques, et dans les cas extrêmes "
         "l’hyperinflation. Le phénomène est d’autant plus fort que le pays "
         "dépend de biens libellés en devises étrangères.",
    'r': "On montre que le change joue le rôle du prix de l’intrant, ce qui "
         "fait de la contrainte extérieure une source autonome d’inflation "
         "par les coûts.",
    'ex': "Les trois cas extrêmes cités par le cours en matière d’inflation "
          "importée : l’Argentine, le Liban et la Turquie."}],
  voisins=['n14-inflation-demande', 'n14-stagflation',
           'n14-inflation-importee', 'n13-chocs-offre-demande'],
  comp={'titre': "Inflation par la demande et inflation par les coûts",
        'a': "Inflation par la demande",
        'b': "Inflation par les coûts",
        'lignes': [
          ("Origine", "La demande augmente plus vite que l’offre",
           "Le prix d’un facteur de production augmente brutalement"),
          ("Formule du cours", "Cause de l’inflation : la demande augmente "
           "plus vite que l’offre", "Les firmes voient leurs coûts augmenter, "
           "donc elles sont obligées de licencier"),
          ("Effet sur l’activité", "Production élevée, capacités saturées",
           "Production en recul, licenciements"),
          ("Effet sur le chômage", "Chômage faible, marché du travail tendu",
           "Chômage en hausse, d’où la stagflation"),
          ("Indicateur de repérage", "Output gap positif, économie en "
           "surchauffe", "Hausse simultanée des prix et du chômage"),
          ("Exemple du cours", "Un crédit trop dynamique accroissant la "
           "masse monétaire puis la demande",
           "Les chocs pétroliers de 1973 et 1979, le baril passant de cinq à "
           "trente dollars"),
          ("Rapport à la courbe de Phillips", "Compatible : inflation forte "
           "et chômage faible", "Incompatible : elle en est détruite "
           "expérimentalement"),
          ("Instrument adapté", "Resserrement monétaire, qui agit "
           "directement sur la dépense",
           "Aucun instrument conjoncturel ne lève la contrainte de coût"),
          ("Doctrine qu’elle soutient", "L’analyse par la demande, de "
           "tradition keynésienne",
           "Le retour des analyses par l’offre et les profits dans les années "
           "quatre-vingt-dix")]})


d('n14-inflation-importee', 14, "Inflation importée",
  "Les prix étrangers entrent par le change et par les coûts",
  "L’inflation importée désigne la hausse des prix domestiques provoquée par "
  "le renchérissement des produits achetés à l’étranger. Le cours en donne "
  "l’enchaînement exact : des importations plus chères élèvent les coûts de "
  "production, donc les prix domestiques, ce qui engendre l’inflation "
  "importée et, dans les cas extrêmes, l’hyperinflation, avec pour exemples "
  "l’Argentine, le Liban et la Turquie.",
  "Le cours installe l’inflation importée dans l’analyse des déséquilibres "
  "extérieurs, et cette place est décisive : elle fait de la hausse des prix "
  "un symptôme de la position extérieure du pays et non un problème "
  "monétaire interne. Le point de départ est le cercle vicieux des monnaies "
  "faibles : un déficit extérieur provoque une dépréciation qui renchérit "
  "les importations et aggrave à son tour le déficit, et cette spirale "
  "extérieure peut ensuite devenir une spirale inflationniste. "
  "L’enchaînement vers les prix est explicite : importations plus chères, "
  "coûts de production en hausse, prix domestiques en hausse, ce qui peut "
  "générer l’inflation importée et, dans les cas extrêmes, l’hyperinflation. "
  "Le cours pose la condition d’intensité : le mécanisme est d’autant plus "
  "fort que le pays dépend fortement de biens libellés en devises "
  "étrangères. Mais il ajoute immédiatement une limite majeure, qui empêche "
  "d’en faire une fatalité : ce cercle vicieux ne s’enclenche pas "
  "nécessairement, car une monnaie plus faible renchérit les importations "
  "mais rend aussi les exportations moins chères pour les étrangers, de "
  "sorte que les exportations peuvent augmenter et le solde extérieur "
  "s’améliorer à terme. Le cours renvoie ici à la courbe en J : dans un "
  "premier temps, la dépréciation alourdit la facture des importations et le "
  "solde peut se dégrader ; puis les volumes exportés augmentent et les "
  "importations diminuent. Tout dépend donc du délai de réaction des "
  "volumes, et c’est dans ce délai que la spirale inflationniste peut "
  "s’installer. Le cours fournit par ailleurs l’instrument de prévention : "
  "la monnaie d’ancrage, devise de référence à laquelle un pays fixe son "
  "taux de change et qui sert à stabiliser la valeur de la monnaie "
  "nationale, avec pour exemples le franc CFA ancré à l’euro et le dollar de "
  "Hong Kong ancré au dollar américain. Enfin l’inflation importée éclaire "
  "une limite générale de la politique monétaire : le canal du taux de change "
  "fait que si les taux montent, les capitaux étrangers sont attirés et la "
  "monnaie s’apprécie, ce qui modère les prix importés, de sorte que la "
  "banque centrale dispose d’un levier, mais au prix d’un effet sur la "
  "compétitivité.",
  [("Le déficit extérieur et la pression sur la monnaie",
    "Un déficit extérieur pèse sur le change : le cours en fait le point de "
    "départ du cercle vicieux des monnaies faibles, antérieur à toute "
    "dynamique de prix intérieure."),
   ("La dépréciation",
    "La monnaie nationale perd de la valeur face aux devises : le même "
    "volume d’importations coûte désormais davantage en monnaie "
    "domestique."),
   ("Le renchérissement des intrants",
    "Les importations plus chères élèvent les coûts de production des "
    "entreprises qui utilisent des biens étrangers, énergie, matières "
    "premières ou composants."),
   ("La répercussion sur les prix domestiques",
    "Les entreprises répercutent cette hausse sur leurs prix de vente : le "
    "cours écrit directement que les prix domestiques augmentent, ce qui "
    "constitue l’inflation importée."),
   ("L’aggravation du déficit",
    "La facture des importations s’alourdit, ce qui creuse le déficit "
    "extérieur et déprécie encore la monnaie : la boucle se referme et peut "
    "conduire à l’hyperinflation."),
   ("L’interruption possible par les volumes",
    "La dépréciation rend les exportations moins chères pour les étrangers : "
    "si les volumes exportés augmentent assez vite, le solde s’améliore et la "
    "spirale s’arrête, selon la logique de la courbe en J."),
   ("La prévention par l’ancrage",
    "Fixer le taux de change sur une devise de référence stabilise la valeur "
    "de la monnaie nationale : le cours cite le franc CFA ancré à l’euro et "
    "le dollar de Hong Kong ancré au dollar américain.")],
  [{'a': "La notion explique une inflation qu’aucune politique monétaire "
         "interne n’a provoquée, ce qui déplace la responsabilité vers la "
         "position extérieure.",
    'cond': "Elle suppose une dépendance forte à des biens libellés en "
            "devises étrangères, condition que le cours énonce "
            "explicitement.",
    'lim': "Une économie peu ouverte ou peu dépendante des intrants importés "
           "n’est guère exposée : le mécanisme est conditionnel et non "
           "général."},
   {'a': "Elle relie la hausse des prix au modèle de croissance du pays, "
         "puisque le déficit extérieur en est le point de départ.",
    'cond': "Le lien suppose que le déficit soit durable et traduise un "
            "déséquilibre interne, ce que le cours affirme en faisant des "
            "soldes extérieurs les symptômes de problèmes domestiques.",
    'lim': "Le cours avertit qu’un déficit n’est pas automatiquement mauvais, "
           "ni un excédent automatiquement positif : le diagnostic ne peut "
           "pas se lire sur le seul solde."},
   {'a': "Elle fournit une explication des hyperinflations contemporaines "
         "sans supposer un emballement de l’émission monétaire.",
    'cond': "L’explication exige que la dépréciation et la hausse des prix "
            "s’alimentent mutuellement, ce que le cours décrit comme une "
            "spirale.",
    'lim': "Elle n’exclut pas la cause monétaire : le cours fournit "
           "ailleurs, avec le système de Law, le cas d’une création monétaire "
           "sans limite conduisant à l’effondrement."},
   {'a': "Elle justifie les régimes de change fixes ou ancrés comme "
         "instrument de stabilité des prix.",
    'cond': "La justification suppose que la devise d’ancrage soit "
            "elle-même stable et que le pays puisse défendre la parité.",
    'lim': "Le cours présente l’ancrage comme un transfert de contrainte : "
           "la politique monétaire devient dépendante de celle de la devise "
           "de référence."},
   {'a': "Elle met en évidence le canal du taux de change dans la "
         "transmission de la politique monétaire.",
    'cond': "Le canal suppose une mobilité des capitaux suffisante pour que "
            "la hausse des taux attire les capitaux et apprécie la monnaie.",
    'lim': "L’appréciation modère les prix importés mais dégrade la "
           "compétitivité des exportations : l’instrument agit sur deux "
           "objectifs en sens contraire."}],
  [{'t': "Une dépréciation est favorable : elle restaure la compétitivité et "
         "corrige le déficit extérieur.",
    'qui': "L’argument de compétitivité que le cours présente comme limite "
           "au cercle vicieux des monnaies faibles.",
    'rep': "Le cours conserve les deux effets et les ordonne dans le temps "
           "avec la courbe en J : d’abord la facture des importations "
           "augmente et le solde se dégrade, puis les volumes exportés "
           "augmentent."},
   {'t': "L’inflation importée n’est pas de l’inflation : c’est une "
         "modification des prix relatifs qui ne peut pas élever durablement "
         "le niveau général des prix.",
    'qui': "L’objection analytique issue de la tradition quantitativiste que "
           "le cours rattache à Fisher et Friedman.",
    'rep': "Le cours répond par la spirale : la hausse des prix nourrit la "
           "défiance envers la monnaie, donc sa dépréciation, donc une "
           "nouvelle hausse, ce qui donne au mouvement un caractère général "
           "et cumulatif."},
   {'t': "La solution est l’ancrage sur une devise forte, qui supprime à la "
         "racine la source du problème en fixant le taux de change.",
    'qui': "La logique de la monnaie d’ancrage que le cours expose à propos "
           "du franc CFA et du dollar de Hong Kong.",
    'rep': "Le cours rappelle que l’ancrage a un coût d’autonomie : la "
           "monnaie de référence sert à stabiliser la valeur de la monnaie "
           "nationale, mais la politique monétaire nationale perd alors son "
           "indépendance."},
   {'t': "Le problème est d’abord interne : seule une politique monétaire "
         "crédible peut stabiliser le change et donc les prix.",
    'qui': "La lecture par la crédibilité que le cours rattache aux "
           "monétaristes et aux anticipations rationnelles.",
    'rep': "Le cours admet le rôle des anticipations mais maintient la cause "
           "première : c’est le déficit extérieur qui enclenche la "
           "dépréciation, et la crédibilité ne supprime pas le déséquilibre "
           "réel qui la nourrit."}],
  [{'n': "Irving Fisher",
    'i': "Le niveau général des prix dépend de la quantité de monnaie et de "
         "sa vitesse de circulation.",
    'p': "Le cours donne son équation reliant la monnaie et sa vitesse au "
         "niveau des prix et au volume des transactions : l’inflation "
         "importée fournit précisément un contre-exemple, puisque les prix "
         "montent sans que la quantité de monnaie se soit emballée."},
   {'n': "Milton Friedman",
    'i': "L’inflation est toujours et partout un phénomène monétaire, donc "
         "indépendante des prix extérieurs.",
    'p': "Le cours rapporte que la monnaie est pour lui exogène et que "
         "l’offre de monnaie dépend des autorités monétaires, ce qui laisse "
         "peu de place à une inflation venue du change : c’est sur ce point "
         "que l’analyse des monnaies faibles s’écarte de la sienne."},
   {'n': "Henri Bourguinat",
    'i': "L’ouverture internationale des capitaux transforme les conditions "
         "de la politique monétaire nationale.",
    'p': "Le cours situe la règle des trois D dans Les vertiges de la "
         "finance internationale en 1987 : le décloisonnement des places et "
         "l’ouverture des capitaux rendent le change sensible aux mouvements "
         "de capitaux, donc les prix domestiques dépendants de l’extérieur."}],
  [{'f': "Le cours décrit l’enchaînement : importations plus chères, coûts de "
         "production en hausse, prix domestiques en hausse, inflation "
         "importée.",
    'p': "La chaîne montre que le mécanisme passe par les coûts et non par "
         "la monnaie : l’inflation importée est une variante de l’inflation "
         "par les coûts dont la source est extérieure."},
   {'f': "Le cours cite trois cas d’inflation importée extrême : "
         "l’Argentine, le Liban et la Turquie.",
    'p': "Les exemples montrent que le phénomène est contemporain et qu’il "
         "frappe des économies fortement dépendantes de biens libellés en "
         "devises étrangères."},
   {'f': "Le franc CFA est ancré à l’euro et le dollar de Hong Kong au "
         "dollar américain.",
    'p': "Les deux exemples montrent l’existence d’une réponse "
         "institutionnelle : la monnaie d’ancrage sert à stabiliser la valeur "
         "de la monnaie nationale, donc à couper le canal de transmission."},
   {'f': "Le cours relève que si les taux montent, les capitaux étrangers "
         "sont attirés et la monnaie s’apprécie.",
    'p': "Le fait identifie le canal du taux de change dans la politique "
         "monétaire : la banque centrale peut modérer les prix importés, mais "
         "au prix d’une perte de compétitivité."}],
  [{'q': "Sujet sur la contrainte extérieure et les prix",
    'f': "Une économie ouverte n’est pas maîtresse de ses prix. Le cours "
         "décrit le cercle vicieux des monnaies faibles : un déficit "
         "extérieur provoque une dépréciation qui renchérit les importations "
         "et aggrave à son tour le déficit, et cette spirale extérieure peut "
         "devenir une spirale inflationniste, puisque des importations plus "
         "chères élèvent les coûts de production, donc les prix domestiques.",
    'r': "On montre que la hausse des prix est ici un symptôme de la "
         "position extérieure, ce qui déplace le traitement du terrain "
         "monétaire vers celui du modèle de croissance.",
    'ex': "Les cas extrêmes cités par le cours : Argentine, Liban, "
          "Turquie."},
   {'q': "Sujet sur les effets d’une dépréciation monétaire",
    'f': "La dépréciation a deux effets contraires que le cours ordonne dans "
         "le temps. Elle renchérit les importations, ce qui nourrit "
         "l’inflation importée ; mais elle rend aussi les exportations moins "
         "chères pour les étrangers, de sorte que les volumes exportés "
         "peuvent augmenter et le solde extérieur s’améliorer. Le cours "
         "renvoie à la courbe en J : d’abord la facture s’alourdit, ensuite "
         "les volumes réagissent.",
    'r': "On transforme une question de signe en question de calendrier, ce "
         "qui permet de conclure que l’issue dépend de l’élasticité des "
         "volumes d’échange.",
    'ex': "La séquence du cours : dans un premier temps le solde peut se "
          "dégrader, puis les volumes exportés augmentent et les importations "
          "diminuent."},
   {'q': "Sujet sur les régimes de change",
    'f': "Le choix d’un régime de change est aussi un choix de politique des "
         "prix. Le cours définit la monnaie d’ancrage comme la devise de "
         "référence à laquelle un pays fixe son taux de change, qui sert à "
         "stabiliser la valeur de la monnaie nationale, et cite le franc CFA "
         "ancré à l’euro et le dollar de Hong Kong ancré au dollar "
         "américain. L’ancrage coupe ainsi le canal de l’inflation importée.",
    'r': "On met en balance la stabilité des prix gagnée et l’autonomie "
         "monétaire perdue, pour montrer qu’un régime de change est un "
         "arbitrage et non une technique neutre.",
    'ex': "L’ancrage du franc CFA à l’euro, que le cours donne comme exemple "
          "de stabilisation par la devise de référence."},
   {'q': "Sujet sur la politique monétaire en économie ouverte",
    'f': "En économie ouverte, la politique monétaire agit aussi par le "
         "change. Le cours décrit ce canal : si les taux montent, les "
         "capitaux étrangers sont attirés et la monnaie s’apprécie, ce qui "
         "modère le prix des importations. La banque centrale dispose donc "
         "d’un second levier contre l’inflation importée, mais ce levier "
         "renchérit simultanément les exportations.",
    'r': "On montre qu’un même instrument agit sur deux objectifs en sens "
         "contraire, les prix et la compétitivité, ce qui limite l’autonomie "
         "de la politique monétaire.",
    'ex': "Le canal du taux de change tel que le cours l’énumère parmi les "
          "canaux de transmission de la politique monétaire."}],
  voisins=['n14-inflation-couts', 'n14-hyperinflation', 'n14-inflation',
           'n13-contagion-financiere'])


d('n14-boucle-prix-salaires', 14, "Boucle prix-salaires",
  "Quand la hausse des prix entretient la hausse des salaires, et l’inverse",
  "La boucle prix-salaires désigne le mécanisme par lequel la hausse des prix "
  "provoque des demandes de hausses de salaires, qui augmentent les coûts, "
  "donc les prix, et ainsi de suite. Le cours en donne les deux versions : "
  "celle de Phillips, où un chômage faible fait monter les salaires puis les "
  "prix, et celle de Friedman, où les anticipations adaptatives entretiennent "
  "indéfiniment le mouvement.",
  "Le cours décrit la boucle deux fois, dans deux cadres théoriques "
  "opposés, et cette double présentation en fait tout l’intérêt. La première "
  "version est keynésienne et sert à établir la courbe de Phillips. Le cours "
  "l’énonce en trois temps : quand le chômage est faible, les salariés "
  "demandent des hausses de salaires ; plus de salaires signifie une hausse "
  "des coûts ; une hausse des coûts signifie une hausse des prix, donc de "
  "l’inflation. On obtient la relation inverse entre chômage et inflation. "
  "Alban William Phillips lui donne son assise empirique en observant en "
  "1958 une relation inverse entre le taux de croissance des salaires "
  "nominaux et celui du chômage, à partir d’une étude sur le Royaume-Uni "
  "entre 1861 et 1957 ; le cours précise que la relation n’est ni linéaire ni "
  "stable et qu’il existe un taux de chômage pour lequel la croissance des "
  "salaires nominaux est nulle. Dans cette version, la boucle est un "
  "mécanisme de transmission du marché du travail vers les prix, et elle est "
  "bornée par le niveau du chômage. La seconde version est monétariste et "
  "sert à détruire la même courbe. Friedman explique que les agents forment "
  "des anticipations adaptatives : quand les prix augmentent, les agents "
  "apprennent de l’inflation passée et adaptent leurs comportements, les "
  "salariés demandant des hausses de salaires et les entreprises augmentant "
  "leurs prix. La boucle n’est plus bornée : elle devient le mécanisme par "
  "lequel une politique monétaire expansionniste perd tout effet réel. Le "
  "cours détaille cette perte : au début les agents pensent que la hausse de "
  "la demande est réelle, donc ils produisent plus ; mais rapidement ils "
  "voient que les prix montent, comprennent qu’il s’agit d’inflation, "
  "réclament des hausses de salaires et les entreprises augmentent leurs "
  "prix, de sorte que la production retourne à son niveau initial et que "
  "seule l’inflation reste. Le cours en tire la version la plus radicale : "
  "les entreprises anticipent immédiatement que l’inflation entraînera une "
  "hausse future des salaires nominaux, par les syndicats, donc elles "
  "n’embaucheront pas plus, et il n’y a ni baisse du chômage ni autre "
  "résultat que davantage d’inflation. La boucle prix-salaires est ainsi le "
  "mécanisme par lequel une politique nominale reste nominale.",
  [("La tension sur le marché du travail",
    "Le cours part d’un chômage faible : les salariés sont en position de "
    "demander des hausses de salaires, ce que Phillips établit "
    "empiriquement par la croissance des salaires nominaux."),
   ("La transmission aux coûts",
    "Plus de salaires signifie une hausse des coûts de production, le "
    "salaire étant pour les entreprises une charge et non seulement un "
    "revenu pour les ménages."),
   ("La répercussion sur les prix",
    "La hausse des coûts se traduit en hausse des prix : le cours écrit "
    "directement que plus de salaires entraîne une hausse des coûts donc une "
    "hausse des prix, c’est-à-dire de l’inflation."),
   ("L’apprentissage par les agents",
    "Avec les anticipations adaptatives de Friedman, les agents apprennent "
    "de l’inflation passée et adaptent leurs comportements : les salariés "
    "demandent des hausses, les entreprises augmentent leurs prix."),
   ("Le bouclage et la perte de l’effet réel",
    "La production retourne à son niveau initial, l’effet réel disparaît et "
    "seule l’inflation reste : la boucle a transformé une impulsion "
    "monétaire en pure hausse des prix."),
   ("L’anticipation immédiate",
    "Dans la version la plus forte que le cours rapporte, les entreprises "
    "anticipent immédiatement la hausse future des salaires nominaux par les "
    "syndicats, donc n’embauchent pas plus : l’effet réel est nul dès le "
    "départ.")],
  [{'a': "La boucle explique pourquoi une inflation, une fois installée, "
         "tend à se prolonger même sans nouvelle impulsion.",
    'cond': "L’argument suppose que les agents forment des anticipations "
            "adaptatives, c’est-à-dire qu’ils apprennent de l’inflation "
            "passée.",
    'lim': "Avec des anticipations rationnelles, le mécanisme change de "
           "nature : les agents n’extrapolent pas le passé mais anticipent la "
           "règle suivie par les autorités."},
   {'a': "Elle fournit le fondement microéconomique de la courbe de "
         "Phillips, en reliant chômage, salaires et prix.",
    'cond': "Le fondement suppose que les salariés aient un pouvoir de "
            "négociation effectif, que le cours associe notamment aux "
            "syndicats.",
    'lim': "Le cours souligne que la relation observée par Phillips n’est ni "
           "linéaire ni stable : la boucle n’a pas une intensité constante."},
   {'a': "Elle explique l’inefficacité de la politique monétaire à long "
         "terme sans supposer l’irrationalité des agents.",
    'cond': "La conclusion exige que les agents finissent par distinguer "
            "hausse nominale et hausse réelle, ce que le cours appelle la fin "
            "de l’illusion monétaire.",
    'lim': "Le cours reconnaît avec Friedman qu’à court terme l’effet réel "
           "existe : la boucle met du temps à se refermer, et c’est dans ce "
           "délai que la politique agit."},
   {'a': "Elle justifie l’attention portée à l’indexation et aux modes de "
         "fixation des salaires dans la conduite de la désinflation.",
    'cond': "L’argument suppose que les salaires suivent effectivement les "
            "prix passés, par la négociation ou par des règles d’ajustement "
            "automatiques.",
    'lim': "Le cours montre ailleurs le coût de la modération salariale : la "
           "compression des salaires limite la demande domestique et peut "
           "conduire à la surproduction."},
   {'a': "Elle éclaire la logique de l’ancrage des anticipations comme "
         "objectif de politique monétaire.",
    'cond': "L’ancrage suppose que la banque centrale puisse convaincre par "
            "sa communication, ce que le cours décrit comme le canal des "
            "anticipations.",
    'lim': "Le cours relève que ce canal fait des anticipations un outil "
           "monétaire à part entière, mais il n’en garantit pas "
           "l’efficacité : il dépend de la crédibilité acquise."}],
  [{'t': "La boucle justifie d’accepter un peu d’inflation : elle accompagne "
         "un marché du travail tendu, donc un chômage faible.",
    'qui': "La lecture keynésienne de la courbe de Phillips que le cours "
           "présente comme dominante dans les années cinquante et soixante.",
    'rep': "Le cours objecte avec Friedman que l’avantage est transitoire : "
           "à long terme il n’y a plus d’illusion monétaire, le chômage "
           "revient à son niveau naturel et la courbe de Phillips devient "
           "verticale."},
   {'t': "La boucle est la cause réelle de l’inflation : ce sont les "
         "salaires, non la monnaie, qui font monter les prix.",
    'qui': "La lecture par les coûts salariaux que le cours expose dans la "
           "construction de la courbe de Phillips.",
    'rep': "Le cours maintient la distinction : la boucle propage "
           "l’inflation mais ne la déclenche pas ; la cause initiale est soit "
           "un excès de demande, soit un choc de coût, soit une création "
           "monétaire excessive."},
   {'t': "La modération salariale est donc la clé de la désinflation, puisque "
         "c’est elle qui referme la boucle par où l’inflation se propage.",
    'qui': "La conclusion de politique économique qui découle "
           "mécaniquement de l’analyse de la boucle.",
    'rep': "Le cours rappelle le contre-effet : la compression des salaires "
           "limite la demande domestique et pousse les entreprises à chercher "
           "des débouchés extérieurs, selon l’enchaînement qu’il rattache à "
           "Marx."},
   {'t': "Avec des anticipations rationnelles, la boucle disparaît : les "
         "agents intègrent immédiatement l’effet de la politique et rien ne "
         "se propage.",
    'qui': "Thomas Sargent et la nouvelle économie classique, telle que le "
           "cours la présente.",
    'rep': "Le cours rapporte précisément cette version chez Friedman "
           "lui-même : les entreprises anticipent immédiatement la hausse "
           "future des salaires nominaux, donc n’embauchent pas plus, ce qui "
           "annule l’effet réel dès le départ."}],
  [{'n': "Alban William Phillips",
    'i': "Il existe une relation inverse entre le taux de croissance des "
         "salaires nominaux et celui du chômage.",
    'p': "Le cours date son observation de 1958 et en précise la base, une "
         "étude empirique sur le Royaume-Uni entre 1861 et 1957 ; il relève "
         "que la relation n’est ni linéaire ni stable et qu’il existe un "
         "taux de chômage pour lequel la croissance des salaires nominaux est "
         "nulle."},
   {'n': "Milton Friedman",
    'i': "Les agents forment des anticipations adaptatives : ils apprennent "
         "de l’inflation passée et adaptent leurs comportements.",
    'p': "Le cours en donne l’exemple exact : les salariés demandent des "
         "hausses de salaires, les entreprises augmentent leurs prix. La "
         "politique monétaire marche donc au début, mais ensuite les gens "
         "s’adaptent, l’effet sur la production disparaît et l’inflation "
         "continue."},
   {'n': "Milton Friedman",
    'i': "Les entreprises anticipent immédiatement la hausse future des "
         "salaires nominaux, donc n’embauchent pas plus.",
    'p': "Le cours rapporte cette version forte, qui passe par les "
         "syndicats : il n’y a alors pas de baisse du chômage mais seulement "
         "plus d’inflation, et la politique monétaire est impuissante à "
         "réduire le chômage."},
   {'n': "Thomas Sargent",
    'i': "Les agents connaissent la règle suivie par les autorités et en "
         "intègrent les effets avant qu’ils ne se produisent.",
    'p': "Le cours en tire que la politique annoncée n’agit que sur les "
         "variables nominales, d’où la préférence pour des règles plutôt que "
         "pour la discrétion : la boucle prix-salaires devient alors "
         "instantanée au lieu d’être progressive."}],
  [{'f': "Le cours énonce la chaîne keynésienne : chômage faible, demandes "
         "de hausses de salaires, hausse des coûts, hausse des prix.",
    'p': "L’enchaînement montre que la boucle relie le marché du travail au "
         "niveau général des prix, ce qui fournit le fondement de la relation "
         "inverse entre chômage et inflation."},
   {'f': "Phillips observe en 1958 une relation inverse entre croissance des "
         "salaires nominaux et chômage sur le Royaume-Uni entre 1861 et 1957.",
    'p': "La période couverte, près d’un siècle, explique l’autorité "
         "qu’avait acquise la relation, et donc le retentissement de son "
         "démenti dans les années soixante-dix."},
   {'f': "Avec les anticipations adaptatives, la production retourne à son "
         "niveau initial, l’effet réel disparaît et seule l’inflation reste.",
    'p': "Le fait montre la conséquence décisive de la boucle : elle ne "
         "transmet pas seulement l’inflation, elle annule l’effet réel de "
         "l’impulsion qui l’a déclenchée."},
   {'f': "Le cours rapporte qu’il existe un taux de chômage pour lequel le "
         "taux de croissance des salaires nominaux est nul.",
    'p': "Le repère montre que la boucle a un point d’arrêt identifiable : "
         "c’est à ce niveau de chômage que la pression salariale cesse "
         "d’alimenter les prix."}],
  [{'q': "Sujet sur la propagation de l’inflation",
    'f': "Une inflation se propage par les salaires avant de se propager par "
         "la monnaie. Le cours donne la chaîne keynésienne : quand le chômage "
         "est faible, les salariés demandent des hausses de salaires ; plus de "
         "salaires signifie une hausse des coûts ; une hausse des coûts "
         "signifie une hausse des prix. Friedman reprend le même mécanisme "
         "sous le nom d’anticipations adaptatives, où les agents apprennent "
         "de l’inflation passée et adaptent leurs comportements.",
    'r': "On montre que le même enchaînement sert à deux usages opposés, "
         "fonder la courbe de Phillips puis la détruire, ce qui éclaire la "
         "différence entre un mécanisme et sa portée.",
    'ex': "L’exemple donné par le cours chez Friedman : les salariés "
          "demandent des hausses de salaires, les entreprises augmentent "
          "leurs prix."},
   {'q': "Sujet sur l’efficacité de la politique monétaire",
    'f': "La boucle prix-salaires est le mécanisme qui annule l’effet réel "
         "d’une politique monétaire expansionniste. Le cours en détaille les "
         "étapes : au début les agents pensent que la hausse de la demande "
         "est réelle, donc ils produisent plus ; mais rapidement ils voient "
         "que les prix montent, réclament des hausses de salaires et les "
         "entreprises augmentent leurs prix, de sorte que la production "
         "retourne à son niveau initial et que seule l’inflation reste.",
    'r': "On montre que l’efficacité d’une politique dépend du délai de "
         "refermeture de la boucle, ce qui explique la distinction "
         "friedmanienne entre court et long terme.",
    'ex': "La formule du cours : la monnaie est puissante, mais la politique "
          "monétaire est inefficace."},
   {'q': "Sujet sur le rôle des anticipations",
    'f': "Le statut de la boucle dépend entièrement de la façon dont les "
         "agents anticipent. Avec les anticipations adaptatives de Friedman, "
         "les agents extrapolent l’inflation passée et la boucle se referme "
         "progressivement. Avec les anticipations rationnelles de Sargent, "
         "les agents connaissent la règle suivie par les autorités et en "
         "intègrent les effets avant qu’ils ne se produisent, de sorte que la "
         "boucle est instantanée et qu’une politique annoncée n’agit que sur "
         "les variables nominales.",
    'r': "On montre que la vitesse de fermeture de la boucle est la variable "
         "décisive, ce qui transforme la question théorique en question de "
         "délai observable.",
    'ex': "La version forte rapportée par le cours : les entreprises "
          "anticipent immédiatement la hausse future des salaires nominaux "
          "via les syndicats."},
   {'q': "Sujet sur les salaires et la compétitivité",
    'f': "Agir sur les salaires pour casser la boucle a un coût du côté de "
         "la demande. Le cours montre d’un côté que plus de salaires entraîne "
         "une hausse des coûts donc des prix, et de l’autre que la "
         "compression des salaires limite la demande domestique et pousse les "
         "entreprises à chercher à l’étranger les débouchés qu’elles ne "
         "trouvent plus sur leur marché intérieur.",
    'r': "On met en évidence la double nature du salaire, coût pour "
         "l’entreprise et revenu pour le ménage, ce qui interdit de traiter "
         "la modération salariale comme une solution sans contrepartie.",
    'ex': "L’enchaînement que le cours rattache à Marx : pression salariale, "
          "demande interne insuffisante, risque de surproduction, nécessité "
          "d’exporter."}],
  voisins=['n14-courbe-phillips', 'n14-anticipations-inflation',
           'n14-inflation-couts', 'n14-stagflation'])
