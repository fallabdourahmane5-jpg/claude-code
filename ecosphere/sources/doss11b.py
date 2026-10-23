# -*- coding: utf-8 -*-
"""Ensemble 11 — La monnaie, les banques et le crédit (2/4)."""

from doss_base import d

d('n11-credit', 11, "Crédit",
  "Le canal par lequel la monnaie entre dans l’économie",
  "Le crédit est l’opération par laquelle une banque met à disposition d’un "
  "agent une somme qu’il s’engage à rembourser. Le cours en fait le mécanisme "
  "central de la création monétaire, puisque les crédits font les dépôts, et "
  "le relais principal de la politique monétaire : dans les économies "
  "contemporaines, la création monétaire dépend largement du crédit bancaire.",
  "Le cours fait du crédit le pivot qui relie la monnaie à l’activité, et il "
  "le montre par une chaîne qu’il appelle fondamentale : taux directeurs, "
  "conditions du crédit, création monétaire, demande globale, inflation et "
  "activité. Chaque maillon est détaillé. En amont, la banque centrale agit "
  "sur le coût du refinancement : une baisse des taux directeurs fait baisser "
  "l’€STR, donc le coût de refinancement des banques, donc les taux "
  "débiteurs, ce qui augmente la demande de crédit et la création monétaire. "
  "Au centre, le crédit crée la monnaie : lorsqu’une banque accorde un prêt, "
  "elle crée simultanément la monnaie et sa contrepartie. En aval, deux "
  "effets opposés. Du côté favorable, une baisse des taux directeurs rend le "
  "crédit moins cher, fait monter l’investissement des entreprises et la "
  "consommation des ménages, donc la demande globale, ce qui soutient la "
  "croissance. Du côté défavorable, un crédit trop dynamique fait monter la "
  "masse monétaire, renforce la demande et crée des tensions sur les prix, "
  "d’où l’inflation ; c’est pourquoi la politique monétaire sert d’abord à "
  "éviter une création monétaire excessive, la Banque centrale européenne "
  "visant une inflation autour de deux pour cent à moyen terme. Le cours "
  "insiste alors sur le dilemme classique : relancer l’activité ou maîtriser "
  "l’inflation. Il montre enfin ce qui se passe quand le canal du crédit se "
  "bloque. La crise de 2008 provoque une chute de la confiance et un blocage "
  "du crédit ; après avoir fortement baissé leurs taux, les banques centrales "
  "se heurtent à la trappe à liquidité, situation où les taux sont déjà très "
  "bas, où les agents préfèrent conserver des liquidités, où les banques "
  "restent prudentes et où l’investissement ne repart pas. Il faut alors des "
  "politiques non conventionnelles pour débloquer le crédit.",
  [("La création de monnaie par le prêt",
    "Accorder un crédit, c’est inscrire au compte du client une somme qui "
    "n’existait pas : la monnaie naît de l’engagement de remboursement, ce "
    "qui fait du crédit la source principale de la monnaie en circulation."),
   ("La transmission par le coût du refinancement",
    "Une baisse des taux directeurs réduit le coût auquel les banques se "
    "refinancent, donc les taux qu’elles pratiquent : le crédit devient moins "
    "cher et la demande de financement augmente."),
   ("L’effet sur la demande globale",
    "Un crédit moins coûteux élève l’investissement des entreprises et la "
    "consommation des ménages : la demande globale augmente, ce qui soutient "
    "la production et l’emploi."),
   ("Le risque inflationniste",
    "Si le crédit progresse plus vite que la production, la masse monétaire "
    "augmente, la demande se renforce et des tensions apparaissent sur les "
    "prix : l’inflation est la contrepartie d’un crédit trop dynamique."),
   ("Le blocage du canal",
    "Lorsque les taux sont déjà très bas, que les agents préfèrent conserver "
    "leurs liquidités et que les banques restent prudentes, baisser encore "
    "les taux ne suffit plus : le crédit ne repart pas, c’est la trappe à "
    "liquidité.")],
  [{'a': "Le crédit est indispensable au financement de l’investissement, "
         "puisqu’il permet de dépenser avant d’avoir épargné.",
    'cond': "L’argument suppose que le projet financé dégage un rendement "
            "supérieur au coût du crédit, faute de quoi l’endettement est "
            "destructeur.",
    'lim': "Le crédit n’est pas une ressource neutre : il crée une dette dont "
           "le remboursement pèsera sur l’activité future, et son excès "
           "nourrit les tensions inflationnistes."},
   {'a': "Agir sur le crédit donne à la banque centrale un instrument "
         "puissant, puisqu’il commande à la fois la monnaie et la demande.",
    'cond': "La transmission suppose que les banques répercutent effectivement "
            "la baisse des taux directeurs sur leurs taux débiteurs.",
    'lim': "En trappe à liquidité, la transmission s’interrompt : les taux "
           "sont très bas et les banques n’accordent pourtant pas de "
           "crédits, ce qui rend la politique conventionnelle inefficace."},
   {'a': "Le crédit permet de lisser l’activité, en soutenant la demande "
         "quand les revenus courants sont insuffisants.",
    'cond': "Le lissage suppose que les agents puissent emprunter, donc "
            "qu’ils soient jugés solvables par les banques.",
    'lim': "Cette condition disparaît précisément en crise, lorsque la "
           "défiance restreint l’accès au crédit au moment où il serait le "
           "plus utile."},
   {'a': "La dépendance de la monnaie au crédit explique pourquoi la "
         "stabilité financière est devenue un objectif de la banque "
         "centrale.",
    'cond': "L’argument suppose que la création monétaire passe "
            "effectivement par le crédit bancaire, ce qui caractérise les "
            "économies contemporaines.",
    'lim': "Le cours relève que le soutien apporté au système bancaire crée "
           "un risque d’aléa moral, en encourageant des comportements "
           "imprudents."}],
  [{'t': "Dans les économies contemporaines, la création monétaire dépend "
         "largement du crédit bancaire, de sorte que toute action sur le "
         "crédit agit sur la monnaie.",
    'qui': "L’analyse du cours sur les liens entre politique monétaire et "
           "création monétaire.",
    'rep': "Le cours relève que ce canal peut s’interrompre : en trappe à "
           "liquidité, même avec des taux très bas, les banques n’accordent "
           "pas de crédits et les ménages n’investissent pas."},
   {'t': "Un crédit trop dynamique provoque de l’inflation par la hausse de "
         "la masse monétaire et de la demande.",
    'qui': "La logique économique que le cours présente comme justification "
           "première de la politique monétaire.",
    'rep': "Le cours ajoute aussitôt le dilemme : la politique monétaire peut "
           "aussi chercher à soutenir la croissance, l’investissement et "
           "l’emploi, et cet objectif entre en tension avec la stabilité des "
           "prix."},
   {'t': "La quantité de crédit, donc de monnaie, est déterminée par la "
         "banque centrale qui contrôle la base monétaire.",
    'qui': "Le courant monétaire, avec le mécanisme du multiplicateur de "
           "crédit.",
    'rep': "Le courant keynésien répond que l’offre de monnaie s’adapte à la "
           "demande de crédit : les banques prêtent d’abord et se refinancent "
           "ensuite, la banque centrale fournissant presque toujours la "
           "monnaie centrale nécessaire."}],
  [{'n': "John Maynard Keynes",
    'i': "L’offre de monnaie s’adapte à la demande de crédit émanant de "
         "l’économie.",
    'p': "Le cours rattache à ce courant le diviseur de crédit : un agent "
         "demande un prêt, la banque crée immédiatement la somme sans "
         "vérifier ses réserves, puis se refinance auprès de la banque "
         "centrale, qui lui fournit presque toujours la monnaie centrale "
         "nécessaire."},
   {'n': "Milton Friedman",
    'i': "Si la quantité de monnaie croît plus vite que la production, les "
         "prix augmentent.",
    'p': "Le cours en tire la justification de l’encadrement du crédit : "
         "l’inflation étant toujours et partout un phénomène monétaire, il "
         "faut contrôler la croissance de la masse monétaire, d’où la règle "
         "d’une progression constante indépendante de la conjoncture."},
   {'n': "Éric Monnet",
    'i': "La banque centrale contemporaine tend à devenir un acteur plus "
         "large de la gouvernance économique.",
    'p': "Dans La Banque Providence, en 2021, il propose de démocratiser les "
         "banques centrales et la monnaie, et envisage qu’elles accompagnent "
         "la transition écologique, créent une monnaie digitale de banque "
         "centrale et prennent en charge la dette publique."}],
  [{'f': "Le cours résume la transmission par une chaîne fondamentale : taux "
         "directeurs, conditions du crédit, création monétaire, demande "
         "globale, inflation et activité.",
    'p': "Cette chaîne montre que la politique monétaire ne se limite pas à "
         "fixer un taux : elle encadre les conditions générales de "
         "circulation de la monnaie dans l’économie."},
   {'f': "Dans la zone euro, la Banque centrale européenne vise une inflation "
         "autour de deux pour cent à moyen terme.",
    'p': "La cible chiffrée montre que l’encadrement du crédit a un critère "
         "précis : éviter une création monétaire excessive au regard de la "
         "production."},
   {'f': "La crise de 2008 provoque une chute de la confiance, un blocage du "
         "crédit, l’effondrement de certains actifs, une récession et une "
         "montée du chômage.",
    'p': "L’enchaînement démontre que le crédit n’est pas un simple "
         "accompagnement de l’activité : son interruption suffit à faire "
         "basculer l’économie réelle."}],
  [{'q': "Le crédit est-il indispensable à la croissance ?",
    'f': "Le cours l’établit par un enchaînement : une baisse des taux "
         "directeurs rend le crédit moins cher, ce qui augmente "
         "l’investissement des entreprises et la consommation des ménages, "
         "donc la demande globale, et soutient la croissance. Mais il montre "
         "aussi la contrepartie, puisqu’un crédit trop dynamique alimente la "
         "masse monétaire et les tensions sur les prix.",
    'r': "Le raisonnement suit le même canal dans les deux sens, ce qui "
         "montre que le crédit est à la fois le moteur de l’activité et la "
         "source de son déséquilibre.",
    'ex': "Le cours formule le dilemme classique entre relancer l’activité et "
          "maîtriser l’inflation."},
   {'q': "Pourquoi la politique monétaire peut-elle devenir inefficace ?",
    'f': "Parce qu’elle agit par le crédit et que ce canal peut se bloquer. "
         "En trappe à liquidité, les taux sont déjà très bas, les agents "
         "préfèrent conserver des liquidités, les banques restent prudentes "
         "et l’investissement ne repart pas suffisamment : baisser encore les "
         "taux ne suffit plus, ce qui conduit aux politiques non "
         "conventionnelles.",
    'r': "On identifie la condition de l’efficacité de la politique "
         "monétaire, la réactivité du crédit, puis la situation où cette "
         "condition cesse d’être remplie.",
    'ex': "Après 2008, les banques centrales recourent au quantitative easing "
          "pour soutenir le crédit."},
   {'q': "Faut-il encadrer le crédit ?",
    'f': "Le cours donne deux raisons de le faire et une raison d’hésiter. "
         "Il faut éviter une création monétaire excessive, qui nourrit "
         "l’inflation, et préserver la stabilité financière, devenue objectif "
         "essentiel depuis 2008. Mais encadrer trop fermement le crédit prive "
         "l’économie du financement de son investissement, d’où le dilemme "
         "entre les deux objectifs.",
    'r': "Le raisonnement met en regard les trois objectifs de la banque "
         "centrale, prix, croissance et stabilité financière, et montre que "
         "le crédit est l’instrument commun par lequel ils entrent en "
         "conflit.",
    'ex': "Le cours relève que le soutien à la stabilité financière crée un "
          "risque d’aléa moral."}],
  voisins=['n11-creation-monetaire', 'n11-banque-centrale',
           'n11-monnaie-activite', 'n11-banques-commerciales'])


d('n11-banques-commerciales', 11, "Banques commerciales",
  "Banques de dépôt, banques d’affaires, banques universelles",
  "Les banques commerciales, ou banques de second rang, sont les "
  "établissements qui collectent les dépôts, accordent les crédits et créent "
  "ainsi la monnaie scripturale. Le cours distingue les banques spécialisées, "
  "encadrées en France par la loi bancaire de 1945, et les banques "
  "universelles, qui exercent toutes les activités bancaires : dépôt, crédit "
  "et investissement.",
  "Le cours aborde les banques commerciales par leur organisation, parce que "
  "c’est elle qui détermine le risque qu’elles font courir au système. Le "
  "modèle spécialisé d’abord : la loi bancaire de 1945 prévoit que les banques "
  "de dépôts travaillent sur des échéances inférieures à deux ans, "
  "c’est-à-dire qu’elles prêtent et empruntent sur des durées courtes. Leur "
  "rôle est d’assurer la liquidité du système, les clients pouvant retirer "
  "leur argent à tout moment, et elles ne financent donc pas des projets longs "
  "comme la construction d’usines ou d’infrastructures. Le modèle universel "
  "ensuite : les banques universelles exercent toutes les activités "
  "bancaires, dépôt, crédit et investissement, une seule banque proposant "
  "tous les services, banque de dépôt et banque d’affaires ; le cours cite "
  "BNP Paribas, la Société Générale et Bank of America. Ce modèle apparaît en "
  "Allemagne au dix-neuvième siècle, puis se généralise en France dans les "
  "années 1980, avec pour avantage plus de souplesse et de rentabilité. Le "
  "risque est précisément identifié : le mélange des activités de court et de "
  "long terme peut fragiliser la stabilité financière, comme en 2008. Le cours "
  "explique le mécanisme : les banques universelles utilisent des ressources à "
  "court terme, comme les dépôts des clients, pour financer des activités à "
  "long terme, crédits ou investissements, ce qui pose un risque de "
  "liquidité ; si les déposants veulent retirer leur argent rapidement, la "
  "banque peut manquer de liquidités puisqu’elle a prêté cet argent sur une "
  "longue durée. C’est pourquoi certains économistes préfèrent séparer les "
  "activités bancaires pour plus de sécurité. Le cours rappelle enfin que les "
  "banques créent la monnaie scripturale et doivent obtenir de la monnaie "
  "centrale auprès des autres banques sur le marché interbancaire ou auprès de "
  "la banque centrale.",
  [("La transformation des échéances",
    "La banque collecte des ressources à court terme et prête à long terme : "
    "cette transformation est sa fonction économique essentielle, mais elle "
    "crée par construction un décalage entre ce qu’elle doit et ce qu’elle "
    "peut mobiliser."),
   ("La création de monnaie scripturale",
    "En accordant un crédit, la banque commerciale inscrit la somme au compte "
    "du client : elle crée de la monnaie, ce qui la distingue de tout autre "
    "intermédiaire financier."),
   ("Le besoin de monnaie centrale",
    "Pour faire face aux retraits en billets et aux réserves obligatoires, la "
    "banque doit obtenir de la monnaie centrale, auprès des autres banques sur "
    "le marché interbancaire ou auprès de la banque centrale par "
    "refinancement."),
   ("Le risque de liquidité",
    "Si les déposants veulent retirer leur argent rapidement, la banque peut "
    "manquer de liquidités puisqu’elle a prêté cet argent sur une longue "
    "durée : le risque ne vient pas de l’insolvabilité mais du calendrier."),
   ("Le cumul des activités",
    "La banque universelle réunit dépôt, crédit et investissement : elle gagne "
    "en souplesse et en rentabilité, mais le mélange des horizons rend la "
    "défaillance d’une activité contagieuse pour les autres.")],
  [{'a': "La banque universelle offre plus de souplesse et de rentabilité "
         "qu’un système cloisonné, puisqu’elle mutualise ses activités.",
    'cond': "L’avantage suppose que les risques portés par les différentes "
            "activités ne se réalisent pas simultanément.",
    'lim': "Le cours relève que le mélange des activités de court et de long "
           "terme peut fragiliser la stabilité financière, comme l’a montré "
           "la crise de 2008."},
   {'a': "La spécialisation des banques limite le risque de liquidité, "
         "puisque les échéances des ressources et des emplois restent "
         "cohérentes.",
    'cond': "Elle suppose que d’autres institutions assurent le financement "
            "long, les banques de dépôts étant limitées à des échéances "
            "inférieures à deux ans.",
    'lim': "Ce cloisonnement réduit la capacité du système à financer des "
           "projets longs comme les usines et les infrastructures, d’où son "
           "abandon progressif à partir des années 1980."},
   {'a': "La transformation des échéances est économiquement utile, puisque "
         "l’épargne disponible est courte et les besoins de financement "
         "longs.",
    'cond': "Elle n’est soutenable que si les retraits restent dispersés dans "
            "le temps, hypothèse normale en période de confiance.",
    'lim': "Cette hypothèse est précisément ce qu’une crise de confiance "
           "détruit, en concentrant les demandes de retrait, comme le montre "
           "l’effondrement de la Banque Royale en 1720."},
   {'a': "Le pouvoir de création monétaire des banques commerciales justifie "
         "leur encadrement par la banque centrale.",
    'cond': "L’argument suppose que la banque centrale dispose "
            "d’instruments effectifs, réserves obligatoires et conditions de "
            "refinancement.",
    'lim': "Le courant keynésien objecte que la banque centrale fournit "
           "presque toujours la monnaie centrale nécessaire, ce qui limite la "
           "portée réelle de cet encadrement."}],
  [{'t': "La banque universelle est préférable, car elle offre plus de "
         "souplesse et de rentabilité en réunissant toutes les activités "
         "bancaires.",
    'qui': "Le modèle apparu en Allemagne au dix-neuvième siècle et "
           "généralisé en France dans les années 1980.",
    'rep': "Le cours objecte le risque de liquidité créé par le mélange des "
           "horizons, et relève que certains économistes préfèrent séparer "
           "les activités bancaires pour plus de sécurité."},
   {'t': "Les banques de dépôts doivent travailler sur des échéances "
         "inférieures à deux ans afin d’assurer la liquidité du système.",
    'qui': "La loi bancaire française de 1945, telle que le cours la "
           "présente.",
    'rep': "Cette règle protège les déposants mais prive l’économie d’un "
           "financement long : le cours note que ces banques ne financent "
           "donc pas des projets comme la construction d’usines ou "
           "d’infrastructures."},
   {'t': "Les banques ne sont que des intermédiaires qui prêtent l’épargne "
         "qu’elles collectent.",
    'qui': "La représentation courante de la banque comme simple "
           "intermédiaire financier.",
    'rep': "Le cours objecte que les crédits font les dépôts : la banque "
           "n’a pas besoin de dépôts préalables pour accorder un crédit, elle "
           "crée simultanément la monnaie et sa contrepartie."}],
  [{'n': "John Law",
    'i': "Une banque dont les engagements dépassent les réserves ne peut pas "
         "faire face à une demande simultanée de retraits.",
    'p': "Le cours décrit l’issue de son système en 1720 : les détenteurs "
         "veulent échanger leurs billets contre de l’or, la Banque n’a plus "
         "de réserves, et la panique provoque l’effondrement, ce qui est le "
         "cas limite du risque de liquidité bancaire."},
   {'n': "John Maynard Keynes",
    'i': "Les banques prêtent d’abord et se refinancent ensuite auprès de la "
         "banque centrale.",
    'p': "Le cours détaille les quatre étapes du diviseur de crédit : un "
         "agent demande un prêt, la banque crée la somme sans vérifier ses "
         "réserves, elle évalue ensuite ses besoins en billets et en réserves "
         "obligatoires, puis emprunte à la banque centrale si nécessaire."},
   {'n': "Éric Monnet",
    'i': "Les missions des banques centrales s’élargissent au-delà de la "
         "seule stabilité des prix.",
    'p': "Le cours mobilise La Banque Providence, en 2021, pour montrer que "
         "la relation entre banques commerciales et banque centrale change : "
         "cette dernière devient un acteur plus large de la gouvernance "
         "économique, jusqu’à envisager une monnaie digitale de banque "
         "centrale."}],
  [{'f': "La loi bancaire de 1945 limite les banques de dépôts à des "
         "échéances inférieures à deux ans, afin qu’elles assurent la "
         "liquidité du système et que les clients puissent retirer leur argent "
         "à tout moment.",
    'p': "La règle montre que la stabilité bancaire a d’abord été recherchée "
         "par le cloisonnement des horizons, avant de l’être par la "
         "surveillance prudentielle."},
   {'f': "Le modèle de la banque universelle apparaît en Allemagne au "
         "dix-neuvième siècle, puis se généralise en France dans les années "
         "1980, avec BNP Paribas, la Société Générale ou Bank of America.",
    'p': "La chronologie montre que la déspécialisation accompagne la "
         "libéralisation financière des années 1980, et non une évolution "
         "technique indépendante."},
   {'f': "Le cours explique qu’une banque universelle utilise les dépôts à "
         "court terme de ses clients pour financer des crédits et des "
         "investissements à long terme.",
    'p': "Le décalage d’échéances établit que le risque de liquidité est "
         "inhérent au modèle et non le résultat d’une mauvaise gestion "
         "ponctuelle."}],
  [{'q': "Faut-il séparer les activités bancaires ?",
    'f': "Le cours donne les deux termes du débat. La banque universelle "
         "apporte plus de souplesse et de rentabilité, mais elle utilise des "
         "ressources à court terme pour financer des activités à long terme, "
         "ce qui crée un risque de liquidité : si les déposants veulent "
         "retirer rapidement leur argent, la banque peut manquer de "
         "liquidités. D’où la préférence de certains économistes pour la "
         "séparation.",
    'r': "Le raisonnement rapporte le débat à un arbitrage entre rentabilité "
         "et sécurité, puis montre que la crise de 2008 a déplacé le "
         "jugement vers le second terme.",
    'ex': "La loi bancaire de 1945 limitait les banques de dépôts aux "
          "échéances inférieures à deux ans."},
   {'q': "Les banques prêtent-elles seulement l’épargne qu’elles "
         "collectent ?",
    'f': "Non : le cours établit que les crédits font les dépôts et que la "
         "banque n’a pas besoin de dépôts préalables pour accorder un crédit. "
         "Ce qu’elle doit se procurer, c’est de la monnaie centrale, pour "
         "faire face aux retraits en billets et aux réserves obligatoires, "
         "sur le marché interbancaire ou auprès de la banque centrale.",
    'r': "On distingue la ressource en monnaie scripturale, que la banque "
         "crée, de la ressource en monnaie centrale, qu’elle doit obtenir, "
         "ce qui dissipe la confusion.",
    'ex': "Le cours détaille les quatre étapes du diviseur de crédit, où le "
          "refinancement vient après le prêt."},
   {'q': "Pourquoi une banque peut-elle faire faillite alors que ses "
         "créances sont bonnes ?",
    'f': "Parce que son problème n’est pas nécessairement de solvabilité mais "
         "de liquidité. Le cours l’explique précisément : la banque a prêté à "
         "long terme des ressources exigibles à court terme, de sorte qu’une "
         "demande simultanée de retraits la met en défaut même si ses "
         "emprunteurs sont solvables.",
    'r': "Le raisonnement distingue la valeur des actifs de leur "
         "disponibilité dans le temps, ce qui explique pourquoi un prêteur en "
         "dernier ressort est nécessaire.",
    'ex': "La Banque Royale de 1720 n’avait plus de réserves lorsque les "
          "détenteurs ont demandé la conversion."}],
  voisins=['n11-creation-monetaire', 'n11-liquidite',
           'n11-refinancement', 'n13-crise-bancaire'])


d('n11-banque-centrale', 11, "Banque centrale",
  "Stabilité des prix, liquidité du système, prêteur en dernier ressort",
  "La banque centrale est l’institution qui émet la monnaie centrale et "
  "conduit la politique monétaire. Le cours résume le rôle de la Banque "
  "centrale européenne en trois missions : assurer la stabilité des prix, "
  "objectif principal, avec une cible d’inflation de deux pour cent ; assurer "
  "la liquidité du système bancaire ; agir comme prêteur en dernier ressort en "
  "cas de crise des banques.",
  "Le cours construit la banque centrale par ses objectifs, puis par ses "
  "instruments, ce qui permet de suivre l’élargissement considérable de son "
  "rôle. Les objectifs sont au nombre de trois, hiérarchisés puis élargis. "
  "L’objectif traditionnel est la stabilité des prix : si la création "
  "monétaire et le crédit progressent trop vite par rapport à la production, "
  "des tensions inflationnistes apparaissent, et la Banque centrale "
  "européenne vise une inflation autour de deux pour cent à moyen terme. Le "
  "deuxième objectif est le soutien à la croissance de la production, par la "
  "baisse des taux directeurs qui rend le crédit moins cher et soutient "
  "l’investissement et la consommation, avec un dilemme classique entre "
  "relancer l’activité et maîtriser l’inflation. Le troisième objectif, devenu "
  "essentiel depuis 2008, est la stabilité financière : la banque centrale "
  "doit éviter les crises bancaires, les paniques de liquidité, le blocage du "
  "crédit, les faillites systémiques et les emballements spéculatifs, ce qui "
  "lui confère des fonctions de prêteur en dernier ressort, de soutien à la "
  "liquidité, de stabilisation des marchés et de prévention du risque "
  "systémique. Le cours ajoute un élargissement contemporain avec Éric Monnet, "
  "dans La Banque Providence en 2021 : la banque centrale pourrait aussi "
  "accompagner la transition écologique, créer une monnaie digitale de banque "
  "centrale et prendre en charge la dette publique. Les instruments ensuite. "
  "Avant 2008, ils sont conventionnels et centrés sur trois taux directeurs : "
  "le taux de facilité de dépôt, taux plancher, le taux de facilité de prêt, "
  "taux plafond, et le taux de refinancement à une semaine, principal signal "
  "monétaire. Ces deux facilités forment le corridor encadrant les taux du "
  "marché interbancaire. Après 2008, les instruments deviennent non "
  "conventionnels : quantitative easing, qualitative easing, taux négatifs et "
  "forward guidance.",
  [("L’ancrage de la stabilité des prix",
    "La banque centrale compare la progression du crédit et de la masse "
    "monétaire à celle de la production : une cible d’inflation chiffrée lui "
    "sert de critère pour éviter une création monétaire excessive."),
   ("Le pilotage par le corridor des taux",
    "La facilité de prêt fixe le plafond et la facilité de dépôt le plancher "
    "des taux du marché monétaire : entre les deux évolue le taux "
    "interbancaire, ce qui permet d’orienter les échanges de liquidités entre "
    "banques."),
   ("La transmission par quatre canaux",
    "La politique monétaire agit par le canal des taux d’intérêt, celui du "
    "prix des actifs avec un effet richesse, celui des anticipations par la "
    "communication, et celui du taux de change qui modifie la compétitivité "
    "extérieure."),
   ("Le prêt en dernier ressort",
    "En cas de panique, la banque centrale fournit la liquidité que le marché "
    "refuse : elle interrompt la spirale par laquelle une banque solvable "
    "mais illiquide ferait défaut, et prévient la contagion."),
   ("Le recours aux instruments non conventionnels",
    "Quand les taux sont proches de zéro, la banque centrale n’agit plus par "
    "le prix de la monnaie mais sur les bilans : achats massifs de titres, "
    "modification de la composition de son actif, taux négatifs et "
    "orientation des anticipations.")],
  [{'a': "Confier à la banque centrale un objectif de stabilité des prix "
         "fournit un critère clair et vérifiable à sa politique.",
    'cond': "L’objectif n’est opérationnel que si la relation entre monnaie, "
            "crédit et prix est suffisamment stable pour être pilotée.",
    'lim': "Friedman lui-même reconnaît que la relation entre monnaie et "
           "variables réelles est instable à court terme, ce qui rend le "
           "réglage fin difficile."},
   {'a': "L’ajout de la stabilité financière aux objectifs correspond à un "
         "besoin démontré par la crise de 2008.",
    'cond': "Il suppose que la banque centrale dispose des instruments "
            "nécessaires, prêt en dernier ressort et soutien à la liquidité.",
    'lim': "Le cours relève que ce soutien crée un risque d’aléa moral, en "
           "encourageant les comportements imprudents de ceux qui se savent "
           "protégés."},
   {'a': "Le corridor des taux directeurs permet une transmission efficace de "
         "la politique monétaire au marché interbancaire puis aux taux "
         "bancaires.",
    'cond': "La transmission suppose un marché interbancaire fonctionnel, où "
            "les banques se prêtent effectivement des liquidités.",
    'lim': "La crise de 2008 a précisément bloqué ce marché, ce qui a "
           "contraint les banques centrales à intervenir directement sur les "
           "titres."},
   {'a': "L’élargissement des missions proposé par Éric Monnet répond à des "
         "enjeux que les instruments traditionnels n’atteignent pas.",
    'cond': "Il suppose un mandat démocratique explicite, puisque ces "
            "missions comportent des choix politiques.",
    'lim': "Le cours souligne qu’une telle extension, notamment la prise en "
           "charge de la dette publique, remet en cause l’indépendance de la "
           "banque centrale et brouille la frontière avec la politique "
           "budgétaire."}],
  [{'t': "La banque centrale doit avant tout assurer la stabilité des prix, "
         "les autres objectifs lui étant subordonnés.",
    'qui': "La doctrine des banques centrales modernes, que le cours "
           "présente comme l’objectif traditionnel.",
    'rep': "Le cours montre que cet ordre a changé depuis 2008 : la stabilité "
           "financière est devenue un objectif essentiel, et la banque "
           "centrale n’est plus seulement une institution anti-inflation mais "
           "un pilier du système financier."},
   {'t': "La banque centrale devrait élargir son rôle à la transition "
         "écologique, à la monnaie digitale et à la dette publique.",
    'qui': "Éric Monnet, dans La Banque Providence, en 2021.",
    'rep': "Le cours relève les objections : financer directement l’État est "
           "de la monétisation de la dette, interdite dans l’Union "
           "européenne, et expose à une perte d’indépendance, à un aléa moral "
           "public et à un risque inflationniste."},
   {'t': "Un État souverain monétairement peut financer sa dette sans "
         "contrainte financière, le seul blocage éventuel étant réel.",
    'qui': "La théorie monétaire moderne, inspirée d’Abba Lerner et "
           "popularisée par Stephanie Kelton dans Le mythe du déficit, en "
           "2021.",
    'rep': "Le cours précise la condition que cette théorie pose elle-même : "
           "le pays doit disposer de ressources suffisantes en main-d’œuvre, "
           "en capacités de production et en ressources naturelles, faute de "
           "quoi la création monétaire se traduit par de l’inflation."}],
  [{'n': "Éric Monnet",
    'i': "La banque centrale contemporaine tend à devenir un acteur plus "
         "large de la gouvernance économique.",
    'p': "Dans La Banque Providence, en 2021, il propose de démocratiser les "
         "banques centrales et la monnaie, et envisage qu’elles accompagnent "
         "la transition écologique, créent une monnaie digitale de banque "
         "centrale et soient en charge de la dette publique."},
   {'n': "Milton Friedman",
    'i': "La banque centrale doit se contenter de contrôler la croissance de "
         "la masse monétaire selon une règle simple.",
    'p': "Le cours rattache à cette position la règle dite de k pour cent : "
         "la masse monétaire devrait augmenter à un rythme constant, "
         "indépendant de la conjoncture, puisque l’intervention "
         "discrétionnaire de l’État crée de l’instabilité."},
   {'n': "Stephanie Kelton",
    'i': "Un État souverain monétairement n’est pas soumis à une contrainte "
         "financière pour sa dépense publique.",
    'p': "Le cours rattache Le mythe du déficit, en 2021, à la théorie "
         "monétaire moderne et aux idées d’Abba Lerner formulées en 1943, "
         "pour lesquelles l’État doit se mettre au service de la prospérité, "
         "la question de la dette publique étant secondaire."},
   {'n': "Christine Lagarde",
    'i': "Les économies contemporaines traversent une succession constante de "
         "crises inédites majeures.",
    'p': "Le cours ouvre le chapitre sur ce diagnostic de permacrises, qui "
         "explique l’élargissement des missions des banques centrales : "
         "l’exception devient la règle, ce qui installe durablement les "
         "instruments non conventionnels."}],
  [{'f': "Le cours énumère les trois taux directeurs : la facilité de dépôt "
         "qui constitue le taux plancher, la facilité de prêt qui constitue le "
         "taux plafond, et le taux de refinancement à une semaine, principal "
         "signal monétaire.",
    'p': "La structure montre que la banque centrale ne fixe pas directement "
         "les taux du marché : elle en borne l’intervalle et laisse les "
         "banques s’échanger les liquidités à l’intérieur du corridor."},
   {'f': "Après la crise de 2008, la banque centrale recourt au quantitative "
         "easing, achats massifs d’obligations publiques et privées, au "
         "qualitative easing, qui modifie la composition de son bilan, et à "
         "des taux négatifs sur la facilité de dépôt.",
    'p': "Cette panoplie montre que la banque centrale a cessé d’agir "
         "seulement sur le prix de la monnaie pour agir sur les bilans, les "
         "titres et les anticipations."},
   {'f': "Le cours précise que la banque centrale européenne agit comme "
         "prêteur en dernier ressort en cas de crise des banques et doit "
         "éviter crises bancaires, paniques de liquidité, blocage du crédit, "
         "faillites systémiques et emballements spéculatifs.",
    'p': "L’énumération démontre que la stabilité financière n’est pas un "
         "objectif vague : elle désigne cinq risques identifiés dont chacun "
         "appelle un instrument propre."}],
  [{'q': "Une banque centrale doit-elle être indépendante ?",
    'f': "Le cours construit l’argument par l’absurde, à partir de "
         "l’hélicoptère monétaire. Si la banque centrale finance directement "
         "l’État, elle devient un outil du gouvernement et n’est plus "
         "crédible pour lutter contre l’inflation ; et si l’État sait qu’elle "
         "peut financer ses dépenses, il n’a plus d’incitation à maîtriser son "
         "déficit, ce qui crée un aléa moral public.",
    'r': "Le raisonnement part d’un cas limite pour isoler la fonction de "
         "l’indépendance, qui est de rendre crédible l’engagement "
         "anti-inflationniste.",
    'ex': "Le cours rappelle que dans l’Union européenne la banque centrale "
          "n’a pas le droit de financer directement l’État."},
   {'q': "Quels sont les objectifs d’une banque centrale ?",
    'f': "Trois, dont la hiérarchie a changé. La stabilité des prix reste "
         "l’objectif traditionnel, avec une cible de deux pour cent à moyen "
         "terme dans la zone euro. Le soutien à la croissance en est un "
         "second, en tension avec le premier. La stabilité financière est "
         "devenue essentielle depuis 2008, au point que la banque centrale "
         "n’est plus seulement une institution anti-inflation.",
    'r': "On suit le déplacement historique des priorités pour montrer que le "
         "mandat des banques centrales n’est pas une donnée technique mais le "
         "produit des crises traversées.",
    'ex': "Éric Monnet propose en 2021 d’y ajouter la transition écologique "
          "et la monnaie digitale de banque centrale."},
   {'q': "La politique monétaire a-t-elle encore des marges d’action ?",
    'f': "Elle en a perdu puis en a inventé. Le cadre conventionnel fonctionne "
         "tant que les taux peuvent être ajustés ; lorsqu’ils approchent de "
         "zéro, la trappe à liquidité en annule l’effet. La banque centrale a "
         "alors recouru aux instruments non conventionnels, achats massifs de "
         "titres, modification de la composition de son bilan, taux négatifs "
         "et forward guidance.",
    'r': "Le raisonnement identifie la contrainte, le plancher des taux, puis "
         "montre comment les instruments nouveaux la contournent en agissant "
         "sur les quantités et les anticipations.",
    'ex': "Les taux négatifs sur la facilité de dépôt visent à dissuader les "
          "banques de thésauriser leurs liquidités."}],
  voisins=['n11-credit', 'n11-independance-bc', 'n11-refinancement',
           'n11-monnaie-activite'])


d('n11-liquidite', 11, "Liquidité",
  "Pouvoir payer tout de suite, sans délai ni perte de valeur",
  "Un actif liquide est un actif qui peut être utilisé immédiatement pour "
  "acheter des biens ou des services, sans délai ni perte de valeur : c’est la "
  "définition que le cours donne de la monnaie elle-même. La liquidité est "
  "donc une propriété graduée, que les agrégats monétaires classent du plus "
  "liquide au moins liquide.",
  "Le cours décline la liquidité à trois niveaux, de l’actif individuel au "
  "système entier. Au niveau de l’actif d’abord : la monnaie est un actif "
  "liquide, utilisable immédiatement sans délai ni perte de valeur, et le "
  "cours gradue cette propriété. Le compte courant, ou compte à vue, permet de "
  "récupérer la somme sans délai et sans coût, alors que le compte rémunéré et "
  "le compte à terme comportent un délai. Les agrégats monétaires traduisent "
  "cette gradation : M1 réunit la monnaie liquide, billets et comptes "
  "courants ; M2 ajoute l’épargne courte, livrets et dépôts à terme ; M3 "
  "ajoute les placements monétaires, organismes de placement collectif en "
  "valeurs mobilières et bons du Trésor, et c’est M3 que la banque centrale "
  "contrôle. Au niveau du marché ensuite : la Bourse assure la liquidité des "
  "actifs, en transformant les titres en actifs plus facilement négociables, "
  "et le marché secondaire permet d’échanger les titres déjà émis. Au niveau "
  "du système enfin : la Banque centrale européenne assure la liquidité du "
  "système bancaire, c’est-à-dire qu’elle permet aux banques commerciales "
  "d’accorder des crédits, et doit éviter les paniques de liquidité. Le cours "
  "montre alors les deux pathologies de la liquidité. L’insuffisance "
  "d’abord : la banque universelle utilise des ressources à court terme pour "
  "financer des activités à long terme, de sorte que si les déposants veulent "
  "retirer leur argent rapidement elle peut manquer de liquidités, d’où le "
  "risque de liquidité. L’excès ensuite, ou plus exactement la préférence pour "
  "la liquidité : en trappe à liquidité, les taux sont déjà très bas, les "
  "agents préfèrent conserver des liquidités, les banques restent prudentes et "
  "l’investissement ne repart pas, si bien que la politique monétaire "
  "conventionnelle devient inefficace.",
  [("La gradation des actifs selon leur liquidité",
    "Du billet au placement monétaire, les actifs se classent selon le délai "
    "et le coût de leur mobilisation : c’est cette gradation que les agrégats "
    "M1, M2 et M3 enregistrent, du plus liquide au moins liquide."),
   ("La liquidité comme service rendu par le marché",
    "La Bourse transforme les titres en actifs plus facilement négociables et "
    "le marché secondaire permet d’échanger les titres déjà émis : la "
    "liquidité d’un actif dépend donc de l’existence d’un marché organisé."),
   ("La liquidité du système bancaire",
    "La banque centrale fournit aux banques commerciales la monnaie centrale "
    "qui leur permet d’accorder des crédits : la liquidité du système n’est "
    "pas donnée, elle est produite par l’institution d’émission."),
   ("Le risque de liquidité",
    "Une banque qui finance des emplois longs avec des ressources courtes "
    "peut manquer de liquidités si les retraits se concentrent, alors même que "
    "ses créances sont bonnes : le risque porte sur le calendrier et non sur "
    "la solvabilité."),
   ("La préférence pour la liquidité en période d’incertitude",
    "Quand l’incertitude augmente, les agents préfèrent conserver des "
    "liquidités plutôt qu’investir : la demande de liquidité se substitue à la "
    "dépense, ce qui neutralise la baisse des taux.")],
  [{'a': "Définir la monnaie comme l’actif parfaitement liquide permet de "
         "classer tous les autres actifs par rapport à elle.",
    'cond': "Le classement suppose que l’on puisse mesurer le délai et le "
            "coût de mobilisation de chaque actif.",
    'lim': "Les frontières sont conventionnelles : le cours note qu’il existe "
           "trois approches possibles de la masse monétaire, et que la banque "
           "centrale a choisi de contrôler M3."},
   {'a': "La liquidité apportée par les marchés est un service économique "
         "réel, puisqu’elle permet de détenir un titre sans renoncer à "
         "pouvoir le céder.",
    'cond': "Elle suppose un marché organisé assurant la cotation et la "
            "rencontre entre offreurs et demandeurs de capitaux.",
    'lim': "Cette liquidité peut disparaître brutalement : la crise de 2008 "
           "s’accompagne de l’effondrement de certains actifs, dont les "
           "détenteurs ne trouvent plus d’acheteur."},
   {'a': "La fourniture de liquidité par la banque centrale prévient qu’une "
         "difficulté de calendrier ne se transforme en faillite.",
    'cond': "Elle exige que la banque en difficulté soit solvable, le prêt en "
            "dernier ressort ne traitant que l’illiquidité.",
    'lim': "Cette garantie crée un aléa moral, en encourageant les "
           "comportements imprudents de ceux qui anticipent d’être "
           "secourus."},
   {'a': "La préférence pour la liquidité explique l’inefficacité de la "
         "politique monétaire quand les taux sont très bas.",
    'cond': "L’explication suppose que les agents arbitrent effectivement "
            "entre détenir de la monnaie et investir.",
    'lim': "Elle n’indique pas comment sortir de cette situation, d’où le "
           "recours aux instruments non conventionnels et le débat sur "
           "l’hélicoptère monétaire."}],
  [{'t': "La monnaie se définit comme l’actif parfaitement liquide, "
         "utilisable immédiatement sans délai ni perte de valeur.",
    'qui': "La définition que le cours retient pour ouvrir le chapitre sur le "
           "financement de l’économie.",
    'rep': "Le cours montre aussitôt que la liquidité est graduée et non "
           "binaire : il distingue compte courant, compte rémunéré et compte "
           "à terme, et construit trois agrégats monétaires différents."},
   {'t': "La banque centrale doit assurer la liquidité du système bancaire "
         "afin que les banques puissent accorder des crédits.",
    'qui': "Le cours, dans son énoncé des trois missions de la Banque "
           "centrale européenne.",
    'rep': "Cette mission entre en tension avec l’objectif de stabilité des "
           "prix, puisque fournir de la liquidité soutient le crédit, donc la "
           "création monétaire, donc les tensions inflationnistes."},
   {'t': "Un excès de liquidité garantit la reprise de l’activité, puisque "
         "l’argent disponible finit par être dépensé.",
    'qui': "La logique implicite des politiques d’injection de liquidité.",
    'rep': "Le cours objecte la trappe à liquidité : les taux sont très bas, "
           "les agents préfèrent conserver des liquidités, les banques "
           "restent prudentes, et l’investissement ne repart pas "
           "suffisamment."}],
  [{'n': "John Maynard Keynes",
    'i': "Les agents peuvent préférer thésauriser la monnaie plutôt que "
         "l’investir.",
    'p': "Le cours en tire la conséquence sur le taux d’intérêt, qui devient "
         "le prix du renoncement à la liquidité et non simplement le prix de "
         "l’épargne, et sur l’existence d’une trappe à liquidité qui rend la "
         "politique monétaire inefficace."},
   {'n': "Irving Fisher",
    'i': "La relation entre monnaie et prix dépend de la vitesse de "
         "circulation de la monnaie.",
    'p': "Le cours rappelle son équation reliant la masse monétaire, sa "
         "vitesse de circulation, le niveau des prix et le volume des "
         "transactions, en supposant la vitesse stable : or la préférence "
         "pour la liquidité est précisément ce qui la fait varier."},
   {'n': "Éric Monnet",
    'i': "La banque centrale est devenue un fournisseur permanent de "
         "liquidité au système financier.",
    'p': "Le cours mobilise La Banque Providence, en 2021, pour montrer que "
         "cette fonction, née dans l’urgence, s’est installée et participe de "
         "l’élargissement des missions des banques centrales vers la "
         "gouvernance économique."}],
  [{'f': "Le cours construit trois agrégats : M1, monnaie liquide avec "
         "billets et comptes courants ; M2, qui ajoute l’épargne courte ; M3, "
         "qui ajoute les placements monétaires, et que la banque centrale "
         "contrôle.",
    'p': "La construction montre que la liquidité est une échelle et non une "
         "propriété tout ou rien, et que le choix de l’agrégat piloté est une "
         "décision de politique monétaire."},
   {'f': "En France, les chèques étant gratuits, les comptes courants ne sont "
         "pas rémunérés, alors que le compte rémunéré et le compte à terme "
         "comportent un délai de mobilisation.",
    'p': "L’arbitrage montre que la liquidité a un prix : elle se paie par "
         "l’absence de rémunération, ce qui est la contrepartie de la "
         "disponibilité immédiate."},
   {'f': "En trappe à liquidité, les taux sont déjà très bas, les agents "
         "préfèrent conserver des liquidités, les banques restent prudentes "
         "et l’investissement ne repart pas suffisamment.",
    'p': "La description établit que la liquidité abondante ne garantit rien : "
         "ce qui compte est la disposition des agents à s’en séparer."}],
  [{'q': "Qu’est-ce qu’un actif liquide ?",
    'f': "Le cours en donne une définition opératoire : un actif liquide peut "
         "être utilisé immédiatement pour acheter des biens ou des services, "
         "sans délai ni perte de valeur. Les deux conditions comptent : un "
         "actif mobilisable mais avec décote, ou disponible mais après délai, "
         "n’est que partiellement liquide, ce que les agrégats monétaires "
         "enregistrent.",
    'r': "Le raisonnement décompose la liquidité en deux dimensions, délai et "
         "valeur, ce qui permet de classer les actifs et de comprendre la "
         "construction de M1, M2 et M3.",
    'ex': "Le compte courant est mobilisable sans délai et sans coût, "
          "contrairement au compte à terme."},
   {'q': "Pourquoi la liquidité peut-elle disparaître ?",
    'f': "Parce qu’elle dépend de la disposition des autres à accepter l’actif "
         "ou à le racheter. Une banque est illiquide lorsque ses déposants "
         "demandent simultanément leurs fonds qu’elle a prêtés à long terme ; "
         "un titre devient illiquide lorsque plus personne ne l’achète, ce que "
         "le cours observe avec l’effondrement de certains actifs en 2008.",
    'r': "On montre que la liquidité n’est pas une propriété intrinsèque de "
         "l’actif mais une propriété du marché et des comportements, donc "
         "susceptible de s’évanouir.",
    'ex': "Le cours range les paniques de liquidité parmi les risques que la "
          "banque centrale doit prévenir."},
   {'q': "Une liquidité abondante suffit-elle à relancer l’économie ?",
    'f': "Non, et la trappe à liquidité en est la démonstration. Le cours "
         "décrit la situation : les taux sont déjà très bas, les agents "
         "préfèrent conserver des liquidités, les banques restent prudentes, "
         "et l’investissement ne repart pas suffisamment. Baisser encore les "
         "taux ne suffit plus, d’où les politiques non conventionnelles.",
    'r': "Le raisonnement distingue la quantité de liquidité disponible de la "
         "volonté de s’en séparer, et montre que seule la seconde commande la "
         "dépense.",
    'ex': "Le quantitative easing consiste à acheter massivement des titres "
          "pour injecter de la liquidité."}],
  voisins=['n11-preference-liquidite', 'n11-monnaie-bancaire',
           'n11-banque-centrale', 'n11-banques-commerciales'])
