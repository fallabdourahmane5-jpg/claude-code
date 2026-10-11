# -*- coding: utf-8 -*-
"""Résumé approfondi du chapitre 1 — Pauvreté monétaire, circuit économique
et consommation. Suit l'ordre des parties et sous-parties du cours.

Champs : q question centrale · ess l'essentiel · parties (t, sp[], v) où chaque
sous-partie porte t titre, d paragraphes, mec mécanisme, lim conditions et
limites · ae auteurs et exemples · arg · deb · lien · min.
"""

R = {'1': {

 'q': "Comment la comptabilité nationale permet-elle de suivre la richesse depuis sa "
      "production jusqu’à sa redistribution, et jusqu’où l’État peut-il corriger cette "
      "répartition sans rendre ses finances insoutenables ?",

 'ess':
  "Le chapitre suit un circuit, et c’est son fil directeur. Il part d’un diagnostic — le "
  "capitalisme contemporain est en polycrise — puis se donne l’instrument qui permet d’en "
  "parler sérieusement : la comptabilité nationale, qui découpe l’économie en six secteurs "
  "institutionnels et la représente comme un circuit fermé. On parcourt ensuite ce circuit "
  "dans l’ordre. Les entreprises produisent une valeur ajoutée dont le partage détermine leur "
  "taux de marge, donc leur capacité à investir ; l’investissement obéit à trois déterminants "
  "— demande, rentabilité, conditions de financement — et oppose depuis les chocs pétroliers "
  "une lecture par l’offre à une lecture par la demande, celle du multiplicateur et de "
  "l’accélérateur. Cette production distribue des revenus primaires que la redistribution "
  "transforme en revenu disponible, puis en niveau de vie par unité de consommation. La "
  "consommation qui en découle n’est pas mécanique : la fonction keynésienne, fondée sur le "
  "revenu courant, est successivement corrigée par Friedman (revenu permanent), Duesenberry "
  "(revenu relatif et effet de cliquet) et Modigliani (cycle de vie). La mesure de la pauvreté "
  "monétaire, relative par construction, conduit alors à l’État : ses trois fonctions, sa "
  "fiscalité, la résistance à l’impôt, et son endettement — un stock qu’il ne faut jamais "
  "confondre avec le déficit, qui est un flux. Le chapitre se referme sur l’instrument "
  "lui-même : le PIB mesure mal la richesse, ce qui relativise tout l’édifice construit avant.",

 'parties': [

  # ------------------------------------------------------------------ I
  {'t': "I. Introduction : un capitalisme en polycrise",
   'sp': [
    {'t': "A. Ce qu’est le capitalisme et comment il a changé de forme",
     'd': ["Le capitalisme se définit comme un régime où des individus possèdent des capitaux "
           "et des moyens de production. Le cours en retient quatre fondements, dont deux "
           "principaux : l’accumulation du capital (investir pour faire du profit, le profit "
           "permettant de réinvestir), la propriété privée, le salariat et la régulation "
           "marchande.",
           "Ces fondements n’imposent pas une seule forme historique. Le capitalisme libéral, "
           "où l’État n’intervient pas, a cédé la place après 1929 à un capitalisme "
           "interventionniste, dont le New Deal de Roosevelt en 1933 est le modèle : "
           "l’investissement public soutient la demande globale et produit des retombées "
           "supérieures à la somme initialement injectée. C’est déjà le multiplicateur, qui "
           "sera formalisé plus loin."],
     'lim': "Ces quatre fondements sont des traits structurels, pas une description de "
            "l’économie réelle à un moment donné : le cours montre justement que la régulation "
            "marchande recule aujourd’hui devant les monopoles."},
    {'t': "B. La polycrise (Plihon) et le capitalisme de la finitude (Orain)",
     'd': ["Le monde décrit par le chapitre est capitaliste mais en crise : le PIB recule de "
           "7 % en France et de 3,5 % dans le monde en 2020. Dominique Plihon, dans Les "
           "capitalismes contemporains, parle de polycrise, c’est-à-dire de quatre crises "
           "simultanées : économique et sociale (héritée de 2007-2008, inégalités de revenus), "
           "climatique, démocratique (défiance envers les institutions, abstention, recul de "
           "l’adhésion syndicale et partisane, montée du populisme opposant élites et peuple) "
           "et géopolitique (montée des émergents, affaiblissement des économies du centre, "
           "effondrement de l’ordre international bâti à partir de 1945).",
           "Arnaud Orain, dans Le monde confisqué, ajoute que le capitalisme est entré dans un "
           "âge de la finitude, qu’il caractérise par trois traits : la privatisation des "
           "espaces (les mers entre la fin du XVIᵉ siècle et 1815), la remise en cause de la "
           "concurrence par les monopoles — quelques géants dominent la recherche en ligne, le "
           "commerce électronique, l’énergie —, et la constitution d’empires privés aussi "
           "puissants que des États, qui possèdent leurs réseaux (satellites, clouds, "
           "plateformes) et discutent d’égal à égal avec les gouvernements.",
           "Le cours nuance au passage l’idée d’un capitalisme simplement mondialisé : depuis "
           "le Covid, on observe une régionalisation des échanges et une diversification des "
           "chaînes d’approvisionnement, dont les objectifs affichés sont la sécurisation et "
           "la décarbonation."],
     'lim': "La polycrise n’est pas une crise conjoncturelle aggravée : son intérêt analytique "
            "est que les quatre dimensions se renforcent mutuellement, ce qui interdit de "
            "traiter l’une sans les autres."},
    {'t': "C. La problématique du chapitre",
     'd': ["De ce diagnostic découlent deux questions qui structurent tout le chapitre : les "
           "acteurs de l’économie sont-ils complémentaires ou concurrents ? Et les économistes "
           "partagent-ils le même point de vue sur les grandes opérations économiques — "
           "investissement, consommation, répartition des revenus ?",
           "La réponse exige un instrument de description commun : c’est précisément ce que "
           "fournit la comptabilité nationale."]},
   ],
   'v': "Avant de juger le capitalisme, il faut savoir le mesurer : le cours passe donc à "
        "l’outil statistique qui représente l’activité économique."},

  # ----------------------------------------------------------------- II
  {'t': "II. Les agents économiques au sein d’un circuit",
   'sp': [
    {'t': "A. Ce qu’est la comptabilité nationale",
     'd': ["La comptabilité nationale regroupe les analyses statistiques qui donnent une "
           "représentation de l’activité économique à partir des actions des acteurs. Son "
           "origine est fiscale : au XVIIᵉ siècle, le roi cherche à mesurer le patrimoine des "
           "individus pour savoir sur qui prélever. Ragnar Frisch est le premier à saisir des "
           "données dans une perspective macroéconomique : pour obtenir une vision "
           "macroéconomique, il faut agréger des données microéconomiques.",
           "Elle retient six secteurs institutionnels : les sociétés non financières, qui "
           "produisent des biens et services marchands non financiers ; les sociétés "
           "financières, qui financent ou gèrent les moyens de financement ; les "
           "administrations publiques, qui produisent des services non marchands et "
           "redistribuent ; les ménages, qui consomment — les entreprises individuelles y sont "
           "rattachées faute de statut juridique distinct ; les institutions sans but lucratif "
           "au service des ménages ; et le reste du monde, qui retrace les relations avec "
           "l’étranger.",
           "Elle travaille sous des normes et conventions de l’ONU, adoptées par la France et "
           "les pays européens, qui ne doivent pas changer pendant cinq ans. Il faut au "
           "minimum trois années pour obtenir des données définitives : celles de 2022 n’ont "
           "été publiées par l’Insee qu’en 2025."],
     'lim': "Cette inertie est le prix de la comparabilité : des données définitives tardives, "
            "mais des séries cohérentes dans le temps et entre pays."},
    {'t': "B. Le circuit économique",
     'd': ["Le circuit se lit en cinq temps. Les entreprises produisent des biens et services, "
           "vendus à l’intérieur (consommation, investissement) ou à l’extérieur "
           "(exportations) ; en contrepartie elles versent des revenus — salaires, profits, "
           "loyers, intérêts. Les ménages et les autres acteurs reçoivent ces revenus au titre "
           "de leur participation à la production, par le travail ou le capital. L’État "
           "prélève impôts et cotisations, puis redistribue allocations, subventions et "
           "services publics, ce qui modifie la répartition des revenus disponibles. Les "
           "ménages consomment et les entreprises investissent, et ces dépenses alimentent à "
           "nouveau la production. Enfin, quand les revenus ne suffisent pas, il faut un "
           "financement : les agents en excédent d’épargne financent ceux qui ont un besoin de "
           "capitaux.",
           "D’où la distinction centrale entre capacité de financement (l’épargne excède "
           "l’investissement) et besoin de financement (l’inverse). Le circuit s’ouvre enfin "
           "sur le reste du monde par les importations et les exportations."],
     'mec': "Production → revenus distribués → redistribution par les APU → consommation et "
            "investissement → nouvelle production ; l’épargne non investie finance les besoins "
            "de financement des autres agents."},
    {'t': "C. Qui sont les agents : ménages, entreprises, administrations",
     'd': ["Le cours insiste sur un point de méthode : à chaque secteur correspond une "
           "fonction principale, et non exclusive. Les ménages consomment « mais pas qu’eux », "
           "les entreprises produisent des biens marchands « mais pas qu’elles », les "
           "administrations produisent des services non marchands. Au sens de l’Insee, un "
           "ménage réunit des personnes, apparentées ou non, vivant dans un même logement avec "
           "un budget commun ; la population hors ménage regroupe les personnes en habitation "
           "mobile, sans domicile, en prison.",
           "L’entreprise est une unité économique dont la fonction principale est de produire. "
           "On la différencie selon quatre critères : la nature du capital (qui la possède), "
           "le secteur d’activité, le statut juridique et la taille. Quand l’État vend une "
           "entreprise il privatise, quand il en récupère la totalité des parts il "
           "nationalise : SNCF, RATP et EDF sont détenues à 100 % par l’État, Air France à "
           "28 %.",
           "La démographie des entreprises est très mobile : plus d’un million de créations en "
           "2024, mais aussi beaucoup de fermetures. Une entreprise qui ne peut plus honorer "
           "ses dettes dépose son bilan ; si elle n’est pas rachetée, c’est la liquidation "
           "judiciaire. Les défaillances passent d’environ 59 000 par an sur 2010-2019 à "
           "51 462 en 2019, puis chutent artificiellement à 36 535 en 2020 et 27 562 en 2021, "
           "avant de remonter à 56 719 en 2023 et 67 000 en 2025 : les aides du Covid — "
           "chômage partiel, prise en charge des coûts fixes — ont différé des faillites qui "
           "se produisent une fois les aides retirées.",
           "Le statut d’auto-entrepreneur, créé en 2009 et rebaptisé micro-entrepreneur en "
           "2015, simplifie la création d’une entreprise individuelle : exonération de TVA "
           "sous un seuil de chiffre d’affaires, régime fiscal particulier, protection sociale "
           "proche de celle des indépendants. Près de 90 % des micro-entrepreneurs restent "
           "sous le seuil pour conserver l’exonération."],
     'lim': "Le micro-entrepreneur illustre un arbitrage : il permet à une entreprise de "
            "confier une tâche sans verser de salaire ni de cotisations — seulement une "
            "facture —, donc de réduire ses coûts, mais il cotise moins, bénéficie de moins de "
            "protections (retraite, chômage, famille, maladie) et occupe une position précaire."},
   ],
   'v': "Le circuit commence par la production : on entre donc dans l’entreprise, pour "
        "comprendre comment la valeur ajoutée se partage et ce qui déclenche l’investissement."},

  # ---------------------------------------------------------------- III
  {'t': "III. Les entreprises, la production et l’investissement",
   'sp': [
    {'t': "A. Lire une entreprise : compte de résultat et bilan",
     'd': ["Deux documents, deux natures. Le compte de résultat enregistre des flux sur une "
           "période : résultat net = production − charges. Le bilan mesure un stock, "
           "l’ensemble des richesses de l’entreprise à un instant donné, en séparant l’actif "
           "(actif immobilisé et actif circulant) et le passif (fonds propres, soit capital "
           "social plus bénéfices mis en réserve, et dettes).",
           "Le lien entre les deux colonnes est fondamental : l’actif est financé par le "
           "passif, c’est-à-dire soit par les fonds propres, soit par l’endettement. C’est la "
           "même opposition stock / flux que l’on retrouvera, à l’échelle de l’État, entre "
           "dette et déficit."]},
    {'t': "B. Le partage de la valeur ajoutée : taux de marge et autofinancement",
     'd': ["Le taux de marge, EBE / VA × 100, indique la part de la valeur ajoutée qui reste à "
           "l’entreprise après paiement des salariés, des cotisations et des impôts de "
           "production. Il s’élève à 32 % en France en 2022.",
           "Un taux de marge élevé — 40 % par exemple — signifie un excédent brut "
           "d’exploitation important, qui servira à verser des intérêts aux créanciers, payer "
           "l’impôt sur les sociétés, distribuer des dividendes et conserver une épargne brute "
           "finançant directement l’investissement : l’entreprise est alors autonome et dépend "
           "moins de l’emprunt. Un taux faible — 15 % — signifie que l’essentiel de la valeur "
           "ajoutée a déjà été distribué en salaires, cotisations et impôts de production : "
           "l’épargne brute ne suffit plus, et il faut emprunter ou lever des fonds.",
           "Le taux d’autofinancement, épargne brute / FBCF × 100, mesure la capacité à "
           "financer soi-même ses investissements. Au-dessus de 100 %, l’entreprise est "
           "autonome ; en dessous, elle recourt à l’endettement. Le cours signale un cas "
           "trompeur : une épargne brute très supérieure à l’investissement peut signifier non "
           "pas la bonne santé mais un investissement insuffisamment dynamique."],
     'lim': "D’où la question ouverte, qui relie ce chapitre à celui sur la croissance : "
            "faut-il un taux de marge élevé, et à qui doit revenir le profit ? Un taux élevé "
            "finance l’investissement futur, mais comprime la part des salaires, donc la "
            "demande."},
    {'t': "C. Ce qu’investir veut dire",
     'd': ["L’investissement est l’achat de matériel de production utilisé plus d’un an ; en "
           "deçà, il s’agit d’une consommation intermédiaire, c’est-à-dire d’un bien "
           "transformé ou entièrement consommé dans le processus de production. On distingue "
           "l’investissement matériel, mesuré par la formation brute de capital fixe — "
           "bâtiments, machines, véhicules, logiciels, dépenses de recherche et "
           "développement — et l’investissement immatériel, qui porte sur des actifs "
           "incorporels : brevets, licences, publicité, œuvres.",
           "Il ne faut pas confondre investissement et placement. Le placement est l’achat "
           "d’un actif financier — action, obligation — qui augmente le patrimoine financier ; "
           "l’investissement augmente physiquement le stock de capital. Une obligation est un "
           "titre de créance : l’acheteur prête, perçoit des coupons et se fait rembourser le "
           "capital à l’échéance ; il est créancier. L’entreprise peut aussi placer sa "
           "trésorerie en banque, le taux d’intérêt devenant alors une source de revenu.",
           "Le taux d’investissement se calcule en microéconomie comme FBCF / VA × 100 — la "
           "part de la valeur ajoutée réinvestie — et en macroéconomie comme FBCF / PIB × 100. "
           "Chez les ménages, l’investissement prend deux formes : immobilière (achat de "
           "logement) et financière (achat de titres)."],
     'mec': "Capacité de financement → arbitrage investir ou placer, selon la rentabilité "
            "attendue (mesurée par le taux de rendement interne) comparée au coût."},
    {'t': "D. Les trois déterminants de l’investissement",
     'd': ["Le cours retient trois déterminants, le profit étant un préalable et une "
           "condition. D’abord la demande : on investit surtout si la demande est forte, ce "
           "que signalent la croissance du PIB, la consommation intérieure, le carnet de "
           "commandes et les perspectives d’exportation ; une demande faible ferait créer des "
           "capacités de production inutilisées. Ensuite la rentabilité : l’entreprise compare "
           "le rendement attendu — bénéfices futurs, gains de productivité, économies de "
           "coûts — au coût initial, en intégrant le risque, la concurrence et l’incertitude "
           "politique. Enfin les conditions de financement : niveau d’épargne disponible, "
           "accès au crédit bancaire, taux d’intérêt."],
     'lim': "Les trois conditions sont cumulatives : une rentabilité attendue élevée ne "
            "déclenche pas l’investissement si la demande manque ou si le crédit est fermé, et "
            "des taux bas ne suffisent pas en l’absence de débouchés."},
    {'t': "E. Le grand débat : l’investissement vient-il de l’offre ou de la demande ?",
     'd': ["Dans les années 1940, la plupart des économistes font dépendre l’investissement et "
           "le profit de la demande. Les chocs pétroliers renversent le cadrage : en 1973 puis "
           "en 1979, le baril passe de 5 à 30 dollars, les coûts de production explosent, les "
           "licenciements se multiplient et le chômage monte. Dans les années 1990, la lecture "
           "par l’offre revient en force, portée par la formule du chancelier allemand Helmut "
           "Schmidt : « les profits d’aujourd’hui font les investissements de demain et les "
           "emplois d’après-demain ». Le profit, mesuré par le taux de marge, est alors "
           "présenté comme la condition même de l’investissement futur.",
           "Keynes défend la lecture inverse : c’est la demande qui commande. Le principe du "
           "multiplicateur énonce qu’une variation de l’investissement entraîne une variation "
           "plus que proportionnelle du revenu. La démonstration est simple : ΔY = ΔC + ΔI, "
           "avec ΔC = c × ΔY, donc ΔY (1 − c) = ΔI et ΔY = k × ΔI avec k = 1/(1 − c). Avec une "
           "propension à consommer c = 0,8 — les ménages consomment 80 % de leur revenu — le "
           "multiplicateur vaut 5 en économie fermée, mais seulement 2,5 en économie ouverte, "
           "parce qu’une partie de la demande fuit vers les importations.",
           "L’accélérateur, dû à Aftalion et Clark, dit l’inverse du multiplicateur : c’est la "
           "variation de la demande, mesurée par celle du PIB, qui provoque une variation plus "
           "que proportionnelle de l’investissement, à la hausse comme à la baisse. "
           "L’oscillateur de Samuelson (1939) combine les deux : variation de l’investissement "
           "→ variation du revenu → variation de la demande → nouvelle variation de "
           "l’investissement.",
           "La conclusion du cours est une synthèse : l’investissement est un élément clé "
           "parce qu’il appartient simultanément à la demande, comme dépense immédiate, et à "
           "l’offre, comme capacité de production future."],
     'mec': "Multiplicateur : ΔI → ΔY = k ΔI avec k = 1/(1 − c), k = 5 en économie fermée, 2,5 "
            "en économie ouverte. Accélérateur : ΔDemande → ΔI plus que proportionnelle. "
            "Oscillateur de Samuelson : les deux s’enchaînent.",
     'lim': "L’ouverture de l’économie réduit de moitié le multiplicateur : c’est l’argument "
            "le plus solide contre une relance isolée, et il se retrouve en deuxième année "
            "dans le débat sur le protectionnisme."},
    {'t': "F. Des revenus au niveau de vie des ménages",
     'd': ["Les revenus se classent par origine : revenus primaires liés à l’activité "
           "productive — revenus salariaux, revenus de la propriété (loyers, rentes, "
           "dividendes), revenus mixtes qui rémunèrent à la fois travail et capital — et "
           "revenus secondaires, ou revenus de transfert, distribués par l’État. Le revenu "
           "disponible brut s’obtient par la formule : revenus primaires + revenus secondaires "
           "− prélèvements obligatoires. C’est le revenu réellement disponible pour consommer "
           "ou épargner.",
           "Le revenu primaire le plus connu est le SMIC, plancher en deçà duquel une "
           "entreprise ne peut rémunérer sans s’exposer aux prud’hommes. La chaîne des "
           "salaires se lit en trois niveaux : salaire super-brut (coût total pour "
           "l’employeur) − cotisations patronales = salaire brut ; salaire brut − cotisations "
           "salariales (assurance maladie, allocation chômage) = salaire net.",
           "Le pouvoir d’achat est la quantité de biens et services qu’un revenu permet "
           "d’acquérir : il faut donc corriger le revenu de l’inflation — une hausse de "
           "salaire de 2 % avec des prix en hausse de 3 % est une perte de pouvoir d’achat. "
           "Le passage de la valeur courante (nominale, aux prix de l’année) au volume (réel, "
           "à prix constants) s’appelle déflater. Pour les taux de croissance on additionne et "
           "soustrait ; pour les niveaux on divise : PIB en volume = PIB en valeur / indice "
           "des prix × 100.",
           "Enfin, le niveau de vie rapporte le revenu disponible aux unités de consommation, "
           "pour comparer des ménages de taille différente : 1 UC pour le premier adulte, "
           "+0,5 UC par personne supplémentaire de plus de 14 ans, +0,3 UC par enfant de moins "
           "de 14 ans."],
     'mec': "Salaire super-brut → (− cotisations patronales) salaire brut → (− cotisations "
            "salariales) salaire net ; revenus primaires + transferts − prélèvements = revenu "
            "disponible brut ; revenu disponible / UC = niveau de vie.",
     'lim': "Le cours relève un effet pervers de l’allègement des cotisations sur les bas "
            "salaires : il réduit le coût du travail, mais incite aussi les employeurs à ne "
            "pas augmenter les salaires, pour rester dans la zone d’exonération."},
    {'t': "G. L’inflation et ses effets sur l’épargne",
     'd': ["L’inflation est l’augmentation du niveau général des prix ; elle se mesure par "
           "l’indice des prix à la consommation, construit sur un panier fixe actualisé chaque "
           "année à partir d’environ 200 000 relevés de prix. Le vocabulaire doit être "
           "précis : une inflation à deux chiffres est une hyperinflation, un ralentissement "
           "de l’inflation est une désinflation — les prix montent encore, moins vite —, et "
           "une baisse des prix est une déflation. L’inflation sous-jacente exclut les "
           "éléments volatils, énergie et alimentation, pour dégager la tendance durable. "
           "Sa cause générale : la demande augmente plus vite que l’offre.",
           "Ses effets sur l’épargne sont ambivalents. L’effet d’encaisse réelle, ou effet "
           "Pigou, pousse à épargner davantage pour conserver la valeur réelle de son "
           "patrimoine, donc à réduire les dépenses. La fuite devant la monnaie pousse au "
           "contraire à consommer immédiatement, avant que les prix ne montent encore."],
     'lim': "Les deux effets jouent en sens contraire : la vérification empirique citée par le "
            "cours indique qu’en France, c’est l’effet d’encaisse réelle qui l’emporte le plus "
            "souvent — une nuance à citer plutôt que de choisir arbitrairement."},
    {'t': "H. Mesurer la pauvreté monétaire",
     'd': ["Le revenu médian est celui qui partage la population en deux moitiés égales : il "
           "s’élève à 2 150 euros par mois en 2023. Le seuil de pauvreté se définit par "
           "rapport à lui : à 50 % du médian, il vaut 1 073 euros et compte 5,4 millions de "
           "personnes pauvres ; à 60 %, norme européenne, il vaut 1 288 euros et en compte "
           "9,8 millions. Le taux de pauvreté est la part de la population sous ce seuil. "
           "Symétriquement, le seuil de richesse vaut le double du revenu médian ; dans le "
           "haut de la distribution, le 1 % le plus riche perçoit 7 512 euros par mois, le "
           "0,1 % 19 500 euros et le 0,01 % environ 70 000 euros. Les personnes sans emploi de "
           "plus de 25 ans peuvent percevoir le RSA, qui garantit un revenu minimum variable "
           "selon la composition du foyer."],
     'lim': "La pauvreté ainsi mesurée est relative, et cela a une conséquence contre-"
            "intuitive : quand une population s’enrichit, le seuil monte mécaniquement et le "
            "nombre de pauvres ne diminue pas forcément. Si l’enrichissement ne touche que le "
            "haut de la distribution, le nombre de pauvres reste inchangé ; il ne baisse que "
            "si la hausse est générale."},
    {'t': "I. La consommation : définitions, structure et loi d’Engel",
     'd': ["La comptabilité nationale distingue la consommation intermédiaire, détruite dans "
           "la production, et la consommation finale, qui concerne les ménages et les "
           "administrations et satisfait directement les besoins. La consommation effective "
           "ajoute ce dont les individus bénéficient quel qu’en soit le financement : elle "
           "intègre donc les services individualisables fournis par les administrations, d’où "
           "des ordres de grandeur très différents selon la notion retenue.",
           "Les dépenses de logement, de chauffage et d’assurances forment les dépenses "
           "pré-engagées : elles représentent environ 30 % du revenu disponible et tendent à "
           "augmenter, ce qui réduit d’autant la marge de manœuvre réelle des ménages.",
           "Quand un pays s’enrichit, la structure de la consommation se déforme : selon la "
           "loi d’Engel, la part des dépenses alimentaires diminue à mesure que le revenu "
           "augmente. L’outil de mesure est le coefficient budgétaire, part d’un poste de "
           "dépense dans le total des dépenses de consommation."]},
    {'t': "J. La fonction de consommation de Keynes et ses trois critiques",
     'd': ["Pour Keynes, dans la Théorie générale de l’emploi, de l’intérêt et de la monnaie "
           "(1936), la consommation dépend du revenu courant — celui dont on dispose "
           "aujourd’hui, non celui qu’on anticipe. Sa loi psychologique fondamentale énonce "
           "que la consommation augmente avec le revenu, mais moins vite que lui. D’où deux "
           "propensions : la propension moyenne à consommer C/Y, décroissante, et la "
           "propension marginale à consommer ΔC/ΔY, comprise entre 0 et 1. L’épargne est un "
           "résidu : S = Y − C. Le taux d’intérêt, chez Keynes, est le prix de la renonciation "
           "à la liquidité, alors que chez les classiques et Friedman il est le prix de la "
           "renonciation à la consommation : dans les deux cas, il arbitre entre consommer et "
           "épargner.",
           "Première difficulté empirique : après 1945, les études montrent que C/Y reste "
           "assez stable à long terme, contrairement à ce que Keynes prévoyait. La loi d’Engel "
           "l’explique en partie — les ménages riches consacrent proportionnellement moins "
           "d’argent à l’alimentation mais compensent par les loisirs ou la culture : la "
           "structure change plus que la proportion globale. Richard Easterlin (1974) ajoute "
           "un paradoxe voisin : à long terme, quand le revenu moyen d’un pays augmente, le "
           "bonheur moyen n’augmente pas nécessairement.",
           "Milton Friedman répond par la théorie du revenu permanent. Il observe que la "
           "consommation est bien plus stable que le revenu et en déduit que les ménages se "
           "fondent sur le revenu qu’ils anticipent durablement. Le revenu courant se "
           "décompose en revenu permanent — part stable, liée à la qualification, "
           "l’expérience, la richesse, les perspectives d’emploi — et revenu transitoire, "
           "variation temporaire et aléatoire. Une hausse perçue comme transitoire est "
           "largement épargnée ; une baisse temporaire est amortie en puisant dans l’épargne. "
           "Friedman relie le revenu permanent à la valeur actualisée des revenus futurs, "
           "l’actualisation donnant la valeur présente d’une somme future : 1 000 euros dans "
           "un an au taux de 10 % valent 1 000/1,1 = 909 euros aujourd’hui.",
           "James Duesenberry, dans Income, Saving and the Theory of Consumer Behavior (1949), "
           "fait intervenir le social. L’effet de démonstration : les individus comparent leur "
           "niveau de vie à celui des autres et imitent les groupes plus aisés, si bien que la "
           "consommation dépend du revenu relatif et reste élevée même quand les revenus "
           "stagnent. L’effet de cliquet : les ménages refusent de réduire un niveau de vie "
           "auquel ils se sont habitués et désépargnent ou s’endettent pour le maintenir, ce "
           "qui rend la consommation rigide à la baisse et stabilise la demande globale. En "
           "une phrase, la consommation est influencée par les autres et par le passé.",
           "Franco Modigliani, entre 1953 et 1975, ajoute le patrimoine et l’âge. Le revenu "
           "est inégalement réparti sur la vie : les jeunes ont des revenus faibles et "
           "s’endettent, les actifs épargnent, les retraités désépargnent pour ne pas voir "
           "leur consommation chuter. Le modèle a trois atouts : il complète Keynes en "
           "introduisant richesse et âge, il décrit fidèlement les États-Unis des années 1950 "
           "où l’héritage était rare et le patrimoine accumulé par l’épargne, et il rejoint "
           "Friedman par la figure d’un individu rationnel qui lisse sa consommation. Il "
           "appartient à l’école de la synthèse : partant du comportement individuel pour "
           "reconstituer les agrégats, il articule micro et macro, là où Keynes raisonnait "
           "directement au niveau global."],
     'mec': "Keynes : C = f(revenu courant). Friedman : C = f(revenu permanent, actualisé). "
            "Duesenberry : C = f(revenu relatif et plus haut revenu atteint). Modigliani : "
            "C = f(revenu courant, patrimoine, âge).",
     'lim': "Les trois critiques du modèle de Modigliani sont explicitement au programme : sa "
            "portée géographique est trop large, car il suppose une retraite par "
            "capitalisation alors que l’Europe fonctionne par répartition, ce qui réduit le "
            "besoin d’épargner ; Piketty montre que l’effacement de l’héritage dans les années "
            "1950 était une exception historique et que l’héritage est redevenu central ; "
            "enfin l’hypothèse que les jeunes peuvent s’endetter suppose un accès facile au "
            "crédit, démenti lors des credit crunchs, où leur consommation redevient "
            "contrainte par le revenu courant — donc keynésienne."},
   ],
   'v': "La production et sa répartition étant décrites, et les inégalités de revenu étant "
        "mesurées par un seuil relatif, la question devient celle de l’intervention publique : "
        "que fait l’État, avec quelles ressources, et à quel coût ?"},

  # ----------------------------------------------------------------- IV
  {'t': "IV. L’État : fonctions, fiscalité et endettement",
   'sp': [
    {'t': "A. À quoi sert l’État : Kaldor, Musgrave et les deux types de politiques",
     'd': ["Le carré magique de Kaldor fixe quatre objectifs — croissance, plein emploi, "
           "stabilité des prix, équilibre extérieur mesuré par le solde des transactions "
           "courantes rapporté au PIB. Il est dit magique parce qu’atteindre les quatre "
           "simultanément est impossible : chaque politique économique arbitre.",
           "Richard Musgrave, dans sa Théorie des finances publiques (1959), distingue trois "
           "fonctions de l’État-providence : l’allocation des ressources, la stabilisation ou "
           "régulation de la conjoncture, et la redistribution.",
           "Les politiques publiques se répartissent selon leur horizon. Les politiques "
           "conjoncturelles, de court terme, sont budgétaires, monétaires ou fiscales ; "
           "l’articulation du budgétaire et du monétaire s’appelle policy mix. Les politiques "
           "structurelles, de long terme, concernent la concurrence, la fiscalité, "
           "l’industrie. Une politique de relance augmente les dépenses publiques ou baisse "
           "les impôts pour soutenir la demande — le plan Biden de rénovation des "
           "infrastructures en est l’exemple du cours ; une politique d’austérité réduit les "
           "dépenses, avec des taux d’intérêt plus élevés, pour freiner la demande.",
           "Le cours note un effet automatique : en bas de cycle, les dépenses augmentent "
           "mécaniquement (allocations chômage, prestations sociales) tandis que les recettes "
           "baissent (moins de TVA, moins de cotisations), ce qui creuse le déficit sans "
           "décision discrétionnaire."],
     'mec': "Relance : ↑ dépenses publiques → ↑ demande → ↑ investissement des entreprises → "
            "↑ PIB. Quand les dépenses dépassent les recettes, le déficit se finance par "
            "l’émission d’obligations d’État."},
    {'t': "B. La crise de l’État-providence et la courbe de Laffer",
     'd': ["Pierre Rosanvallon, dans La crise de l’État-providence (1981), identifie trois "
           "crises qui se renforcent : un problème de financement, une crise d’efficacité et "
           "une crise de légitimité — une fiscalité élevée conduit les travailleurs à douter "
           "de l’intérêt de travailler si une grande part du salaire part en impôts.",
           "La courbe de Laffer formalise l’argument libéral : « trop d’impôt tue l’impôt », "
           "au-delà d’un certain taux une hausse réduit les recettes."],
     'lim': "Le cours formule explicitement les reproches : cette courbe ne repose pas sur des "
            "faits empiriques solides selon plusieurs économistes, et certaines études "
            "montrent qu’à moyen terme une hausse du taux d’imposition reste sans effet "
            "notable, les comportements ne changeant pas immédiatement."},
    {'t': "C. La fiscalité : structure, instruments et justice",
     'd': ["On distingue les impôts directs, payés par le contribuable sur ses revenus ou son "
           "patrimoine, et les impôts indirects, perçus à l’occasion d’une transaction, "
           "principalement la TVA. Une niche fiscale est un avantage réduisant l’impôt sous "
           "conditions — le pacte Dutreil en est l’exemple. La France compte 483 taxes et "
           "impôts et 474 niches fiscales.",
           "La fiscalité n’est pas qu’un prélèvement : c’est un levier qui oriente les choix "
           "des consommateurs, favorise certains secteurs, dissuade certaines consommations "
           "(alcool, tabac, énergies polluantes) et finance les services publics. L’exemple du "
           "cours est simple : un soda acheté en magasin supporte une TVA de 5,5 %, consommé "
           "au restaurant 10 %, parce qu’on paie aussi un service considéré comme non "
           "essentiel ; le taux normal est de 20 %. La TVA rapporte environ 200 milliards "
           "d’euros par an.",
           "Un impôt progressif a un taux qui augmente avec le revenu : c’est l’impôt sur le "
           "revenu, construit par tranches de taux marginal — par exemple 0 % jusqu’à 10 000 "
           "euros, 10 % de 10 000 à 30 000, 30 % au-delà. Il est plus équitable car il réduit "
           "les inégalités. Un impôt dégressif pèse proportionnellement plus sur les revenus "
           "modestes : la TVA en relève, ce qui en fait un impôt injuste au sens de la justice "
           "fiscale. Le quotient familial — revenu imposable divisé par le nombre de parts — "
           "rend l’impôt à la fois progressif et adapté à la composition du ménage ; un foyer "
           "de deux adultes et trois enfants compte 4 parts (1 + 1 + 0,5 + 0,5 + 1), le "
           "troisième enfant valant une part entière. La France compte 41 millions de foyers "
           "fiscaux, et 45 % des personnes acquittent l’impôt sur le revenu.",
           "La CSG, créée en 1991, finance la Sécurité sociale et s’applique à tous les "
           "revenus — salaires, patrimoine, chômage —, ce qui élargit la base du financement "
           "social au-delà des seuls salaires. Son taux moyen est passé de 1,1 % en 1991 à "
           "environ 10 % aujourd’hui, avec un taux réduit d’environ 6 % sur les allocations "
           "chômage."],
     'lim': "Un impôt progressif assis sur une base étroite — moins d’une personne sur deux — "
            "redistribue moins qu’il n’y paraît, tandis que l’impôt le plus rentable, la TVA, "
            "est régressif : la structure des prélèvements compte autant que leur niveau."},
    {'t': "D. La résistance à l’impôt et le niveau de vie élargi",
     'd': ["Une hausse des impôts ou des cotisations augmente le coût du travail, donc les "
           "prix, et dégrade la compétitivité ; elle peut aussi réduire le salaire net, donc "
           "le revenu disponible, donc la consommation et l’investissement des ménages. C’est "
           "l’argument économique de la résistance.",
           "Alexis Spire, dans Résistances à l’impôt, attachement à l’État (2018), montre que "
           "les citoyens peuvent critiquer ou contourner l’impôt tout en restant attachés à "
           "l’État et aux services publics. Il souligne une asymétrie de perception : un "
           "avantage fiscal non prélevé et une aide versée coûtent autant aux finances "
           "publiques, mais ne sont pas perçus de la même manière ; les exonérations "
           "s’élevaient à 90 milliards d’euros en 2017. Le consentement à l’impôt dépend alors "
           "de trois jugements : le système est-il équitable, les contreparties sont-elles "
           "visibles, la dépense publique est-elle efficace ?",
           "D’où la notion de niveau de vie élargi, qui ajoute au revenu disponible la valeur "
           "des services publics reçus — éducation, santé, logement social. Les chiffres de "
           "2023 sont parlants : avant redistribution élargie l’écart de niveau de vie est "
           "d’environ 18 fois, après redistribution il tombe à 4 fois ; 53 % des ménages sont "
           "bénéficiaires nets, le revenu des plus modestes est multiplié par 4 tandis que les "
           "plus aisés perdent environ 40 % de leur revenu initial."],
     'lim': "Le paradoxe est explicite dans le cours : la redistribution est massive, mais "
            "largement invisible pour ceux qui en bénéficient, ce qui alimente précisément la "
            "résistance à l’impôt qu’elle devrait désamorcer."},
    {'t': "E. Les inégalités de patrimoine et le débat sur la taxe Zucman",
     'd': ["La redistribution réduit fortement les inégalités de revenu, beaucoup moins celles "
           "de patrimoine. En 2025, le patrimoine du décile le plus riche atteint 2 612 "
           "milliards d’euros, soit 42 % d’un PIB d’environ 4 350 milliards, contre 6 % en "
           "1996. Sur la période, la variation des grandes fortunes dépasse de loin celle du "
           "salaire minimum : environ +1 300 % contre +86 %.",
           "La taxe Zucman vise les patrimoines supérieurs à 100 millions d’euros, soit "
           "environ 1 800 foyers fiscaux. C’est une taxe plancher de 2 % et une taxe "
           "différentielle : on déduit les impôts déjà acquittés pour calculer le reste à "
           "payer.",
           "Le cours en expose trois critiques. L’efficacité : les 20 milliards attendus "
           "seraient surévalués, et resteraient faibles face à environ 170 milliards de "
           "déficit, avec un risque de fuite des capitaux. Les effets pervers : la taxe "
           "réduirait l’investissement, et en réduisant le patrimoine elle rétrécirait sa "
           "propre assiette les années suivantes. La justice et la constitutionnalité : la "
           "valeur taxée est souvent théorique — capitalisation boursière pour les sociétés "
           "cotées, valorisation par les investisseurs pour les non cotées — et peu liquide, "
           "si bien qu’un entrepreneur détenant 100 millions sans avoir vendu d’actions "
           "devrait payer 2 millions sans trésorerie ; or le Conseil constitutionnel prohibe "
           "l’impôt confiscatoire, le même argument que celui opposé à l’impôt sur la fortune "
           "immobilière.",
           "Xavier Jaravel propose trois réformes alternatives : taxer les plus-values "
           "latentes au moment de la transmission, puisqu’aujourd’hui on ne paie qu’à la vente "
           "et que la plus-value accumulée échappe à l’impôt lors de l’héritage ; imposer les "
           "holdings familiaux, non taxés en Europe alors qu’ils le sont aux États-Unis ; et "
           "réformer le pacte Dutreil, qui exonère jusqu’à 75 %, voire 95 %, de la valeur "
           "d’une entreprise transmise si les héritiers la conservent six ans."],
     'lim': "Le débat n’est donc pas d’abord budgétaire mais redistributif et juridique : "
            "l’assiette est difficile à évaluer, souvent illiquide, et la contrainte "
            "constitutionnelle de non-confiscation borne ce qui est faisable."},
    {'t': "F. Le financement par l’endettement : dette, déficit et charge",
     'd': ["Les administrations publiques peuvent emprunter ; l’emprunt se rembourse avec des "
           "intérêts, et le paiement des intérêts et du capital forme le service de la dette, "
           "les intérêts seuls constituant la charge de la dette. Le cours distingue un "
           "endettement sous contrainte, qui finance des dépenses nécessaires, et un "
           "endettement problématique, devenu trop élevé pour être remboursé.",
           "Les définitions doivent être tenues fermement. La dette publique est la somme de "
           "tous les emprunts des administrations — État, collectivités, Sécurité sociale : "
           "c’est un stock cumulé, d’environ 3 400 milliards d’euros, soit environ 114 % du "
           "PIB. Le déficit public est le solde négatif des recettes et des dépenses sur une "
           "année : c’est un flux, et c’est lui qui alimente la dette. Le déficit budgétaire "
           "ne concerne que l’État, le déficit public toutes les administrations. Emprunter "
           "pour rembourser une dette arrivée à échéance, c’est rouler la dette : l’échéance "
           "est repoussée, le stock n’est pas réduit. On distingue enfin dette intérieure, "
           "détenue par des créanciers résidents, et dette extérieure, détenue par des "
           "créanciers étrangers, ce qui rend le pays dépendant des marchés financiers.",
           "La charge de la dette est le véritable indicateur de soutenabilité : 39 milliards "
           "d’euros en 2019, 36,4 en 2021 grâce aux taux bas, 58 en 2024 — environ 2 % du "
           "PIB — et 62 à 67 milliards prévus en 2025. Elle augmente avec les taux d’intérêt, "
           "eux-mêmes tirés par la dégradation de la note de la France liée à l’instabilité "
           "politique. Le cours parle d’impasse : il faudrait augmenter les impôts pour "
           "compenser, ce que les contribuables refusent.",
           "Le pacte de stabilité et de croissance impose deux plafonds de nature "
           "différente : un déficit public annuel inférieur ou égal à 3 % du PIB — un flux — "
           "et une dette inférieure ou égale à 60 % du PIB — un stock.",
           "Le creusement français s’explique par un effet de ciseau : les dépenses ont "
           "augmenté avec le « quoi qu’il en coûte » — l’État prenant en charge les coûts "
           "fixes des entreprises privées de chiffre d’affaires —, les prêts garantis par "
           "l’État, de 140 à 170 milliards d’euros, l’État s’engageant à rembourser 90 % du "
           "capital en cas de défaillance, et le bouclier tarifaire limitant à 15 % la hausse "
           "des prix de l’électricité ; pendant que les recettes baissaient avec les "
           "exonérations de cotisations, engagées avant le Covid et amplifiées ensuite, et "
           "environ 70 milliards de réductions d’impôts depuis 2017.",
           "Cinq issues sont examinées. L’annulation de la dette soulage le budget mais détruit "
           "la confiance des créanciers et isole financièrement le pays. L’inflation réduit la "
           "valeur réelle de la dette, mais déstabilise l’économie si elle est forte. Le "
           "quantitative easing, par le rachat de titres publics, fait baisser les taux et "
           "soutient la liquidité, au risque de nouveaux déséquilibres. Un impôt exceptionnel "
           "peut rembourser une partie du stock. La croissance, enfin, augmente les recettes "
           "fiscales et allège le poids relatif de la dette."],
     'mec': "Déficit (flux annuel) → émission d’obligations → accroissement de la dette "
            "(stock) → charge d’intérêts annuelle, qui croît avec les taux et pèse sur le "
            "budget, donc sur le déficit suivant.",
     'lim': "Le bilan du cours est équilibré : l’endettement public est nécessaire pour "
            "financer l’action publique et amortir les crises, mais il doit rester "
            "soutenable — c’est-à-dire remboursable sans compromettre l’avenir économique."},
   ],
   'v': "Tout ce raisonnement — production, revenus, redistribution, dette — s’appuie sur un "
        "même indicateur. Encore faut-il savoir ce que le PIB mesure réellement."},

  # ------------------------------------------------------------------ V
  {'t': "V. Synthèse : mesurer la richesse par la comptabilité nationale",
   'sp': [
    {'t': "A. Deux mises au point sur le PIB",
     'd': ["Première distinction : valeur et volume. Le PIB en valeur est aux prix courants, "
           "le PIB en volume est déflaté de l’inflation. Pour les taux, taux de croissance en "
           "volume + évolution des prix = taux de croissance en valeur.",
           "Seconde distinction : effectif et potentiel. Le PIB effectif est celui que calcule "
           "la comptabilité nationale ; le PIB potentiel est celui qu’un pays aurait si tous "
           "les facteurs de production étaient utilisés, sans choc d’offre ou de demande, sans "
           "chômage ni inflation. L’écart entre les deux est l’output gap : quand la croissance "
           "effective dépasse la croissance potentielle, apparaissent des tensions "
           "inflationnistes, car les entreprises peuvent préférer augmenter leurs prix plutôt "
           "que leurs capacités de production.",
           "Le cours rappelle enfin la différence entre richesse comme flux de revenu et "
           "richesse comme patrimoine, et entre PIB et RNB : le revenu national brut retranche "
           "les revenus du capital et du travail versés au reste du monde et ajoute ceux qui "
           "en sont reçus."]},
    {'t': "B. Un PIB contesté",
     'd': ["Le travail domestique est la limite la plus frappante : selon le périmètre retenu — "
           "restreint (cuisine, ménage, linge, soins aux enfants), intermédiaire ou extensif "
           "(courses, bricolage, jardinage, trajets) — il représente en France plus d’heures "
           "que le travail rémunéré, lequel atteint 38 milliards d’heures par an. Il n’est pas "
           "intégré au PIB, même si la comptabilité nationale s’efforce de le mesurer depuis "
           "2014.",
           "L’économie non observée pose un problème voisin : activités marchandes illicites, "
           "activités dissimulées (travail au noir, évaluées à 37 milliards d’euros), "
           "activités non marchandes domestiques et bénévoles. L’Insee tente de les évaluer "
           "sans considération de légalité, pour mieux mesurer le PIB, mais ces estimations "
           "restent peu fiables.",
           "Deux prolongements corrigent partiellement l’indicateur. Depuis novembre 2024, "
           "l’Insee publie les comptes de la nation augmentée, qui intègrent la redistribution "
           "élargie — santé, éducation publique, allocations — pour mesurer le niveau de vie "
           "réel. Et le produit intérieur net ajusté, qui retranche du PIN les coûts des "
           "émissions de gaz à effet de serre, abaisse le résultat d’environ 4 %."],
     'lim': "Le PIB reste un bon indicateur de production marchande, mais il ne mesure ni le "
            "bien-être, ni la soutenabilité, ni la répartition : le critiquer n’est pas le "
            "rejeter, c’est savoir ce qu’il ne dit pas."},
    {'t': "C. Le tableau entrées-sorties et les interdépendances sectorielles",
     'd': ["L’Insee construit les comptes de la nation sur cinq grandes branches : "
           "agriculture, industrie, construction, services principalement marchands, services "
           "principalement non marchands. Le tableau entrées-sorties relie les entrées et les "
           "sorties de chaque secteur : chaque ligne représente la production d’un secteur, "
           "chaque colonne sa consommation, et le total des entrées égale le total des "
           "sorties.",
           "Son intérêt est analytique : il montre comment une variation dans un secteur se "
           "propage à tous les autres — si la construction recule, elle entraîne les "
           "matériaux, le transport et les services financiers. Il distingue aussi la part de "
           "la demande intérieure, celle des exportations et celle des importations utilisées "
           "dans la production française, ce qui permet de mesurer la dépendance du pays à "
           "l’étranger pour l’énergie ou certains composants."]},
   ],
   'v': "Le chapitre se referme sur une tension féconde : l’instrument qui sert à juger le "
        "capitalisme en polycrise est lui-même contesté — ce qui ouvre directement sur la "
        "mesure de la croissance et du développement."},
 ],

 'ae': [
  {'n': "Dominique Plihon, Les capitalismes contemporains", 'k': 'a',
   'i': "La polycrise : crise économique et sociale, climatique, démocratique et géopolitique "
        "se renforcent, ce qui interdit de traiter l’une sans les autres."},
  {'n': "Arnaud Orain, Le monde confisqué", 'k': 'a',
   'i': "Le capitalisme de la finitude : privatisation des espaces, retour des monopoles et "
        "empires privés aussi puissants que des États."},
  {'n': "Ragnar Frisch", 'k': 'a',
   'i': "Le premier à saisir des données dans une perspective macroéconomique : la macro naît "
        "de l’agrégation de données micro."},
  {'n': "John Maynard Keynes, Théorie générale (1936)", 'k': 'a',
   'i': "Loi psychologique fondamentale et multiplicateur k = 1/(1 − c) : la consommation "
        "dépend du revenu courant, et une dépense initiale a un effet amplifié."},
  {'n': "Albert Aftalion et John Bates Clark", 'k': 'a',
   'i': "L’accélérateur : une variation de la demande provoque une variation plus que "
        "proportionnelle de l’investissement."},
  {'n': "Paul Samuelson (1939)", 'k': 'a',
   'i': "L’oscillateur : multiplicateur et accélérateur s’enchaînent, ce qui engendre des "
        "fluctuations auto-entretenues."},
  {'n': "Helmut Schmidt", 'k': 'a',
   'i': "« Les profits d’aujourd’hui font les investissements de demain et les emplois "
        "d’après-demain » : la formule de la lecture par l’offre après les chocs pétroliers."},
  {'n': "Milton Friedman", 'k': 'a',
   'i': "Le revenu permanent : la consommation suit le revenu anticipé actualisé, donc une "
        "relance temporaire est largement épargnée."},
  {'n': "James Duesenberry (1949)", 'k': 'a',
   'i': "Effet de démonstration et effet de cliquet : la consommation dépend du revenu relatif "
        "et résiste à la baisse."},
  {'n': "Franco Modigliani", 'k': 'a',
   'i': "Le cycle de vie : le patrimoine et l’âge expliquent l’épargne ; un pont entre Keynes "
        "et Friedman, et entre micro et macro."},
  {'n': "Richard Easterlin (1974)", 'k': 'a',
   'i': "Le paradoxe d’Easterlin : à long terme, un revenu moyen plus élevé n’élève pas "
        "nécessairement le bonheur moyen."},
  {'n': "Ernst Engel", 'k': 'a',
   'i': "La part de l’alimentation dans le budget décroît avec le revenu : la structure de la "
        "consommation se déforme quand un pays s’enrichit."},
  {'n': "Nicholas Kaldor", 'k': 'a',
   'i': "Le carré magique : croissance, emploi, prix et solde extérieur ne peuvent être "
        "atteints simultanément."},
  {'n': "Richard Musgrave (1959)", 'k': 'a',
   'i': "Les trois fonctions de l’État : allocation, stabilisation, redistribution."},
  {'n': "Pierre Rosanvallon (1981)", 'k': 'a',
   'i': "Crise de financement, d’efficacité et de légitimité de l’État-providence."},
  {'n': "Arthur Laffer", 'k': 'a',
   'i': "« Trop d’impôt tue l’impôt » — argument très mobilisé, mais dont le cours souligne "
        "qu’il est empiriquement mal établi."},
  {'n': "Alexis Spire (2018)", 'k': 'a',
   'i': "On peut contester l’impôt tout en restant attaché à l’État : le consentement dépend "
        "de la justice perçue et de la visibilité des contreparties."},
  {'n': "Gabriel Zucman et Xavier Jaravel", 'k': 'a',
   'i': "Taxe plancher de 2 % sur les patrimoines au-delà de 100 millions d’euros, et trois "
        "réformes alternatives : plus-values latentes, holdings familiaux, pacte Dutreil."},
  {'n': "Thomas Piketty", 'k': 'a',
   'i': "Le retour de l’héritage : les années 1950 décrites par Modigliani étaient une "
        "exception historique."},
  {'n': "Le New Deal de Roosevelt (1933) et le plan Biden", 'k': 'e',
   'i': "Deux relances par l’investissement public, à quatre-vingt-dix ans d’écart : hausse "
        "des dépenses → demande → investissement privé → PIB."},
  {'n': "Le « quoi qu’il en coûte », les PGE et le bouclier tarifaire", 'k': 'e',
   'i': "140 à 170 milliards d’euros garantis à 90 %, hausse de l’électricité contenue à "
        "15 % : l’effet de ciseau sur les finances publiques se lit ici."},
  {'n': "Les défaillances d’entreprises, de 2019 à 2025", 'k': 'e',
   'i': "51 462 en 2019, 27 562 en 2021 sous perfusion d’aides, 67 000 en 2025 : les faillites "
        "différées finissent par se produire."},
  {'n': "Le pacte Dutreil", 'k': 'e',
   'i': "Jusqu’à 75 %, voire 95 %, de la valeur d’une entreprise exonérée à la transmission : "
        "la niche fiscale la plus discutée du chapitre."},
  {'n': "La TVA sur un soda : 5,5 % en magasin, 10 % au restaurant", 'k': 'e',
   'i': "La fiscalité ne fait pas que prélever : elle oriente la consommation et hiérarchise "
        "les besoins."},
 ],

 'arg': [
  "La redistribution n’est pas marginale : en niveau de vie élargi, l’écart passe d’environ "
  "×18 à ×4, 53 % des ménages sont bénéficiaires nets et les plus aisés perdent environ 40 % "
  "de leur revenu initial.",
  "Dette et déficit ne se discutent pas de la même façon : le déficit est un flux annuel "
  "(≈ 170 Md€) qui alimente un stock (≈ 3 400 Md€, ≈ 114 % du PIB). La soutenabilité se juge "
  "sur la charge d’intérêts — de 39 Md€ en 2019 à 58 Md€ en 2024 — et non sur le stock.",
  "La structure des prélèvements compte autant que leur niveau : un système reposant sur la "
  "TVA (≈ 200 Md€, régressive) redistribue moins qu’un système reposant sur un impôt "
  "progressif acquitté par seulement 45 % des personnes.",
  "La fonction de consommation keynésienne est un point de départ, pas une conclusion : "
  "Friedman, Duesenberry et Modigliani expliquent chacun pourquoi C/Y reste stable, et chacun "
  "affaiblit différemment l’efficacité d’une relance temporaire.",
  "L’ouverture de l’économie divise le multiplicateur par deux (5 → 2,5) : argument décisif "
  "contre une relance isolée, et passerelle directe vers la deuxième année.",
  "La pauvreté mesurée est relative : l’enrichissement d’un pays élève le seuil et ne réduit "
  "le nombre de pauvres que si la hausse des revenus est générale.",
  "Critiquer le PIB n’est pas le rejeter : travail domestique, économie non observée, PINA et "
  "comptes de la nation augmentée montrent qu’on peut compléter l’indicateur sans renoncer à "
  "mesurer.",
 ],

 'deb': [
  "Relance ou austérité : le multiplicateur justifie la relance, mais il s’affaisse en "
  "économie ouverte et les ménages peuvent épargner un revenu perçu comme transitoire "
  "(Friedman).",
  "À qui doit revenir le profit ? Un taux de marge élevé finance l’investissement futur "
  "(lecture par l’offre, Schmidt) mais comprime les salaires, donc la demande (Keynes).",
  "Taxer les très hauts patrimoines : question de rendement (20 Md€ attendus face à 170 Md€ "
  "de déficit) ou question de justice fiscale et de consentement à l’impôt ?",
  "La courbe de Laffer décrit-elle un comportement réel ou une croyance politique ? Le cours "
  "retient qu’elle est empiriquement mal établie.",
  "Le niveau des prélèvements est-il la cause ou la conséquence de la crise de légitimité "
  "décrite par Rosanvallon, alors que la redistribution reste invisible à ses bénéficiaires ?",
  "Faut-il remplacer le PIB, le compléter (PINA, comptes augmentés), ou accepter qu’un "
  "indicateur de production ne mesure pas le bien-être ?",
 ],

 'lien': [
  {'c': 2, 'p': "Le financement du déficit, les obligations d’État, le quantitative easing "
                "comme solution à l’endettement et le policy mix sont développés dans le "
                "chapitre monétaire : les deux chapitres se lisent ensemble."},
  {'c': 6, 'p': "Le PIB, ses limites, l’output gap et les outils de mesure des inégalités "
                "constituent la boîte à outils du chapitre sur la croissance, où l’on retrouve "
                "aussi la question du partage de la valeur ajoutée."},
  {'c': 7, 'p': "La pauvreté relative française s’oppose à la pauvreté absolue mondiale, et la "
                "dette publique interne à la dette extérieure en devises des pays en "
                "développement."},
  {'c': 5, 'p': "Les trois fonctions de Musgrave donnent la traduction budgétaire des "
                "justifications microéconomiques de l’intervention : les défaillances de "
                "marché."},
  {'c': 10, 'p': "Le SMIC, les prud’hommes, le niveau de vie et les inégalités de revenu se "
                 "prolongent dans la sociologie du travail et des inégalités d’emploi."},
  {'c': 8, 'p': "Le statut de micro-entrepreneur et la précarité qui l’accompagne annoncent "
                "l’analyse des formes d’emploi et de l’ubérisation."},
 ],

 'min': [
  "Polycrise (Plihon) : économique et sociale, climatique, démocratique, géopolitique ; "
  "capitalisme de la finitude (Orain).",
  "Six secteurs institutionnels et un circuit : production → revenus → redistribution → "
  "consommation et investissement → financement → reste du monde.",
  "Taux de marge = EBE/VA (32 % en 2022) ; taux d’autofinancement = EB/FBCF ; investissement "
  "≠ placement.",
  "Multiplicateur k = 1/(1 − c) = 5 en économie fermée, 2,5 en ouverte ; accélérateur "
  "(Aftalion-Clark) ; oscillateur de Samuelson.",
  "Consommation : Keynes (revenu courant), Friedman (revenu permanent actualisé), Duesenberry "
  "(revenu relatif, cliquet), Modigliani (cycle de vie, critiqué sur la répartition, "
  "l’héritage et le credit crunch).",
  "Revenu médian 2023 : 2 150 €/mois ; seuil à 60 % = 1 288 € (9,8 millions), à 50 % = "
  "1 073 € (5,4 millions) ; dépenses pré-engagées ≈ 30 %.",
  "Musgrave : allocation, stabilisation, redistribution. Rosanvallon : financement, "
  "efficacité, légitimité. Laffer : empiriquement contestée.",
  "Niveau de vie élargi : écart ×18 avant, ×4 après ; 53 % de ménages bénéficiaires nets ; "
  "474 niches, 90 Md€ d’exonérations en 2017.",
  "Déficit = flux (≈ 170 Md€) ; dette = stock (≈ 3 400 Md€, ≈ 114 % du PIB) ; charge 39 → "
  "58 Md€ de 2019 à 2024 ; Maastricht 3 % et 60 %.",
  "PIB : valeur/volume, effectif/potentiel, output gap ; limites : travail domestique, "
  "économie non observée (37 Md€), PINA (−4 %), comptes de la nation augmentée depuis "
  "novembre 2024.",
 ],
}}
