# -*- coding: utf-8 -*-
"""Résumé approfondi du chapitre 8 — Révolutions industrielles, entreprise, travail et IA.

Tous les chiffres, dates, titres d'ouvrages et attributions proviennent de la section « Cours »
du chapitre et de ses notions.
"""

R = {'8': {

 'q': "La révolution industrielle est-elle une rupture technique ou un processus cumulatif, et "
      "comment l’innovation, l’organisation du travail, la gouvernance puis le numérique et l’IA "
      "transforment-ils sans cesse le capitalisme et le travail ?",

 'ess':
  "Le chapitre suit une progression en entonnoir : d’abord le régime productif, puis son moteur, "
  "puis son organisation interne, puis son pouvoir, enfin ses mutations contemporaines. On "
  "montre d’abord que la révolution industrielle n’est ni un choc technique ponctuel ni l’effet "
  "de la seule machine à vapeur, mais un processus long, cumulatif et circulaire où agriculture, "
  "démographie, science, médecine, charbon, transports et usine se renforcent mutuellement — ce "
  "qui permet d’expliquer la précocité anglaise par une conjonction de facteurs (Pomeranz, "
  "Allen, North, Acemoglu et Robinson) plutôt que par une cause unique. Vient ensuite le moteur "
  "interne du système : Schumpeter, qui rompt avec l’équilibre au profit de la dynamique, place "
  "l’entrepreneur innovateur et la destruction créatrice au cœur du capitalisme, réhabilite le "
  "monopole temporaire, relie les grappes d’innovations aux cycles longs de Kondratiev, et "
  "annonce que le succès du capitalisme peut étouffer l’entrepreneur au profit des oligopoles. "
  "L’analyse descend alors dans l’entreprise : taylorisme, fordisme et toyotisme rationalisent "
  "le travail, chacun corrigeant les limites du précédent. Puis elle pose la question du "
  "pouvoir : qui dirige ? L’entrepreneur-propriétaire, puis les managers (Berle et Means, "
  "Galbraith, Chandler), puis les actionnaires (Bourguinat, Jensen et Meckling, Friedman), avant "
  "que ce modèle soit contesté au nom des parties prenantes et de la RSE. Dernier mouvement : le "
  "capitalisme numérique de plateforme, ses opportunités et ses quatre familles de menaces, la "
  "pluralité historique et géographique des capitalismes, la précarisation de l’emploi depuis "
  "les années 1970, et enfin l’IA, qui automatise pour la première fois des fonctions "
  "cognitives.",

 'parties': [

  # ------------------------------------------------------------------ I
  {'t': "I. La révolution industrielle : un processus long, cumulatif et multidimensionnel",
   'sp': [
    {'t': "A. Définition, et la critique du mot « révolution »",
     'd': ["La révolution industrielle désigne le passage d’une économie dominée par "
           "l’agriculture à une économie dominée par l’industrie, avec montée de l’urbanisation, "
           "essor du salariat, mécanisation, concentration productive et transformation des "
           "rapports sociaux. L’idée essentielle est qu’elle transforme l’ensemble du système "
           "productif, et non seulement quelques techniques.",
           "L’historiographie classique a longtemps mis en avant quelques inventions "
           "symboliques, notamment la machine à vapeur de James Watt (brevet de 1769). Cette "
           "lecture est trop réductrice : l’industrialisation britannique n’est ni un simple "
           "choc technique, ni un phénomène instantané.",
           "Le mot « révolution » est d’ailleurs discuté, car il suggère une rupture brutale, un "
           "avant/après très net, un basculement rapide. Or les historiens insistent sur le fait "
           "que l’industrialisation anglaise est progressive, sectorielle, étalée sur plusieurs "
           "décennies, non linéaire, faite d’enchaînements cumulatifs. De nombreux secteurs "
           "restent artisanaux longtemps et les innovations diffusent lentement."],
     'lim': "Le terme reste utile pour désigner un changement de régime productif, mais il ne "
            "doit pas être interprété comme une rupture soudaine : il exagère la brutalité du "
            "changement."},
    {'t': "B. Une mutation systémique : plusieurs révolutions articulées",
     'd': ["La première industrialisation britannique n’est pas une révolution mais la "
           "combinaison de plusieurs : révolution agricole, révolution démographique, "
           "développement de la science, progrès de la médecine, révolution des transports, et "
           "révolution industrielle au sens strict (mécanisation et usine). L’expression "
           "« révolution industrielle » est en réalité un raccourci pour désigner une mutation "
           "générale du système économique et social.",
           "Le point décisif n’est pas l’existence de ces transformations mais leur articulation. "
           "Il ne faut pas raisonner en chaîne simple — agriculture → industrie → fin — mais en "
           "cercle cumulatif."],
     'mec': "La boucle d’auto-entraînement s’écrit ainsi : révolution agricole → hausse des "
            "rendements et de la productivité → meilleure alimentation → baisse de la mortalité → "
            "révolution démographique → plus de main-d’œuvre et taille des marchés accrue, "
            "urbanisation → hausse de la demande → industrialisation. Puis le retour : "
            "l’industrialisation accroît la demande de produits agricoles améliorés (engrais, "
            "charrues) et de biens d’équipement (rails, locomotives) ; les transports élargissent "
            "les marchés, ce qui renforce l’industrialisation ; la science nourrit l’innovation, "
            "et l’industrie crée en retour de nouveaux besoins techniques qui renforcent la "
            "science."},
    {'t': "C. Une ou plusieurs révolutions industrielles ?",
     'd': ["La première révolution industrielle court approximativement de 1760 à 1820, parfois "
           "prolongée jusqu’en 1880. Pays leader : la Grande-Bretagne, puis la France. Énergie "
           "dominante : le charbon. Secteurs moteurs : textile, sidérurgie et acier, machine à "
           "vapeur — avec pour repère clé le brevet de Watt en 1769. Elle repose sur la "
           "mécanisation, l’essor du textile et de l’industrie lourde, et l’apparition de "
           "l’usine moderne.",
           "La deuxième révolution industrielle commence vers 1880 et court jusqu’aux années 1970 "
           "environ. Pays leaders : les États-Unis et l’Allemagne. Énergies dominantes : "
           "électricité et pétrole. Secteurs moteurs : chimie, automobile, électroménager et "
           "télécommunications. Elle correspond à l’essor de la production de masse, de la "
           "grande firme et de nouveaux biens de consommation durables.",
           "La révolution informatique et numérique s’ouvre dans les années 1970, avec pour "
           "repères le microprocesseur (1971), l’informatique personnelle (années 1970-1980), "
           "Internet (années 1990), les plateformes (années 2000), puis l’IA et le big data "
           "(années 2010-2020). Secteurs moteurs : informatique, logiciels, télécommunications, "
           "plateformes, cloud, IA, données."],
     'lim': "Le découpage est discutable : certains parlent de trois révolutions industrielles, "
            "d’autres de quatre en distinguant le numérique et l’IA. Il reste utile parce qu’il "
            "permet de penser des vagues technologiques qui reconfigurent périodiquement les "
            "structures productives."},
   ],
   'v': "Reste à voir comment cette transformation s’opère concrètement : dans quels secteurs, et "
        "selon quelles formes d’organisation de la production."},

  # ------------------------------------------------------------------ II
  {'t': "II. La transformation sectorielle et organisationnelle : du coton au factory system",
   'sp': [
    {'t': "A. Le textile cotonnier, secteur pionnier",
     'd': ["Si la machine à vapeur symbolise la révolution industrielle, le premier secteur "
           "véritablement moteur est le textile cotonnier. Le coton est central car il bénéficie "
           "d’une forte demande, d’un approvisionnement colonial, d’innovations techniques "
           "rapides et d’un fort potentiel de gains de productivité. Attention toutefois : il est "
           "pionnier, pas exclusif — le fer, la métallurgie et la construction navale évoluent "
           "également.",
           "Les innovations à retenir se succèdent rapidement : la Spinning Jenny de James "
           "Hargreaves (1764), la Water Frame de Richard Arkwright (1769), la Mule de Samuel "
           "Crompton (1779), le Power Loom d’Edmund Cartwright (1785), puis le perfectionnement "
           "mécanique de Roberts (1825).",
           "Le gain de productivité est colossal et se mesure : pour produire une livre de coton, "
           "il fallait environ 50 000 heures vers 1750, contre environ 135 heures vers 1830. Le "
           "coton est le laboratoire de la mécanisation britannique."]},
    {'t': "B. Une mécanisation progressive qui recompose le travail",
     'd': ["L’un des contresens les plus fréquents consiste à imaginer que la machine remplace "
           "brutalement les hommes. L’industrialisation mécanise certaines tâches mais ne "
           "supprime pas immédiatement le travail manuel : elle crée aussi de nouveaux besoins — "
           "extraction, manutention, infrastructures, terrassements, construction ferroviaire, "
           "transport.",
           "La machine ne se substitue donc pas systématiquement au travail humain : "
           "l’industrialisation transforme, redistribue et recompose les tâches plus qu’elle ne "
           "supprime immédiatement l’emploi — argument qui reviendra, mot pour mot, dans le débat "
           "sur l’IA en fin de chapitre."]},
    {'t': "C. Du domestic system au factory system",
     'd': ["Pendant une large partie de la première moitié du XIXᵉ siècle, petits ateliers et "
           "domestic system restent importants et coexistent avec les premières manufactures. Le "
           "domestic system est un système de production à domicile, souvent assuré par des "
           "paysans-ouvriers, dont les matières premières sont fournies par un marchand : un "
           "travail rural intégré à un réseau marchand, c’est-à-dire une forme de "
           "proto-industrialisation.",
           "Le factory system désigne au contraire la concentration des ouvriers dans un même "
           "lieu de production, avec usage de machines plus puissantes, contrôle du temps de "
           "travail, supervision hiérarchique, division des tâches et production intensive. Il "
           "s’oppose directement à la dispersion du domestic system.",
           "Mais cette concentration n’est pas seulement technique : elle entraîne la séparation "
           "du lieu de vie et du lieu de travail, la montée du salariat industriel, la discipline "
           "du temps, une hiérarchie plus forte, une coordination centralisée et une hausse de la "
           "productivité. C’est le passage d’une proto-industrie dispersée à l’entreprise "
           "industrielle moderne."],
     'lim': "La transition est longue : le factory system ne s’impose véritablement que vers "
            "1870, soit plus d’un siècle après les premières innovations textiles."},
   ],
   'v': "Cette dynamique sectorielle et organisationnelle ne dit toujours pas pourquoi elle "
        "commence précisément en Grande-Bretagne : il faut maintenant expliquer la précocité "
        "anglaise."},

  # ------------------------------------------------------------------ III
  {'t': "III. La précocité anglaise : une conjonction de facteurs, non une cause unique",
   'sp': [
    {'t': "A. La révolution agricole et la distinction rendement / productivité",
     'd': ["La révolution agricole anglaise se situe principalement entre 1700 et 1750, avec des "
           "prolongements ultérieurs. Elle se caractérise par une hausse des rendements et de la "
           "productivité, une transformation des techniques de culture et une évolution des "
           "structures de propriété : l’agriculture anglaise devient plus efficace, plus "
           "intensive et plus capitalistique. Repère chiffré : les rendements doublent entre 1700 "
           "et 1850.",
           "Les changements techniques sont identifiables : amélioration de l’outillage (batteuse, "
           "moissonneuse), suppression progressive de la jachère, abandon de l’assolement "
           "triennal, amélioration des rotations culturales, recours à de nouveaux engrais.",
           "S’y ajoute une transformation foncière décisive : les enclosures, mouvement de clôture "
           "et de privatisation des terres communes. Effets économiques : affirmation de la "
           "propriété privée, sécurisation de l’investissement, possibilité d’utiliser des "
           "machines coûteuses, rationalisation des exploitations, hausse de l’efficacité. Effets "
           "sociaux : disparition des communaux, fragilisation d’une partie de la paysannerie, "
           "exode rural accru. Les enclosures illustrent déjà la logique du capitalisme : gains "
           "d’efficacité, mais coût social élevé.",
           "Une distinction doit être maîtrisée rigoureusement. Le rendement est le rapport de la "
           "production à la surface cultivée — par exemple la quantité de blé par hectare. La "
           "productivité est le rapport de la production aux facteurs de production : "
           "productivité du travail = production / travail, productivité du capital = production "
           "/ capital. Formule à retenir : rendement = rapport à la terre, productivité = rapport "
           "aux facteurs."],
     'mec': "La révolution agricole agit par trois canaux. Une meilleure alimentation fait baisser "
            "la mortalité, améliore l’espérance de vie et soutient la croissance de la population "
            "— la Grande-Bretagne passe de 7 millions d’habitants en 1780 à 16 millions en 1840. "
            "Une population plus nombreuse fournit à la fois plus de main-d’œuvre et plus de "
            "consommateurs, donc élargit les marchés. Enfin une agriculture plus productive "
            "permet de nourrir des populations urbaines croissantes et de libérer des bras : pas "
            "d’industrialisation durable sans surplus agricole capable de nourrir les villes.",
     'lim': "La causalité ne va pas dans un seul sens. La thèse classique fait précéder "
            "l’agriculture (révolution agricole → exode rural → industrialisation), mais "
            "l’industrie fournit en retour à l’agriculture machines, outils métalliques, acier, "
            "engrais, innovations chimiques et moyens de transport. La bonne réponse est donc une "
            "causalité circulaire, cumulative et réciproque."},
    {'t': "B. Science et médecine : deux moteurs distincts",
     'd': ["Le développement de la science favorise l’amélioration des procédés, la diffusion "
           "d’une culture de l’expérimentation, le perfectionnement des machines, les innovations "
           "mécaniques et la rationalisation de la production. Son rapport avec l’industrie est "
           "circulaire : la science nourrit l’innovation, et l’industrie crée de nouveaux besoins "
           "techniques qui relancent la science.",
           "Les progrès de la médecine jouent un rôle plus directement démographique : "
           "vaccination, progrès de l’hygiène, amélioration des connaissances médicales. Repère "
           "clé : en 1797, Edward Jenner met au point le vaccin contre la variole. Effets : baisse "
           "de la mortalité, amélioration de la santé, soutien à la croissance démographique.",
           "Ces deux cases doivent rester distinctes dans un plan : la science agit par "
           "l’innovation technique, la médecine par la démographie."]},
    {'t': "C. Les supports matériels : charbon et transports",
     'd': ["Avant le XVIIIᵉ siècle, l’économie repose sur le bois, la force humaine, la force "
           "animale, l’eau et le vent. Avec la déforestation, la hausse des besoins et les "
           "limites des énergies organiques, le charbon devient central : énergie plus abondante, "
           "plus concentrée, plus régulière, adaptée à la mécanisation, alimentant la vapeur et "
           "soutenant la sidérurgie et la métallurgie. Repère chiffré : la consommation de "
           "charbon est multipliée par 250 entre 1750 et 1830.",
           "Mais l’énergie ne suffit pas : il faut faire circuler le charbon, les matières "
           "premières et les produits finis. D’où la révolution des transports — amélioration des "
           "routes, développement des canaux avec le Bridgewater Canal en 1761, puis du chemin de "
           "fer avec l’inauguration de la ligne Liverpool-Manchester en 1830 et un développement "
           "ferroviaire majeur à partir des années 1830-1840.",
           "Les effets sont cumulatifs : baisse des coûts de transport, meilleure circulation du "
           "charbon, élargissement des marchés, approvisionnement des villes, soutien à "
           "l’urbanisation, intégration du marché national."]},
    {'t': "D. Géographie, empire et prix relatifs : Pomeranz et Allen",
     'd': ["L’industrialisation anglaise n’a rien d’évident : d’autres espaces, notamment la "
           "Chine, disposent au XVIIIᵉ siècle de ressources, de marchés et de capacités "
           "techniques importantes. Kenneth Pomeranz (La grande divergence, 2010) compare "
           "précisément l’Angleterre et le delta du Yangzi : les deux régions sont relativement "
           "avancées, mais leurs trajectoires divergent ensuite. Pour lui, la Grande-Bretagne "
           "bénéficie d’un charbon proche des centres de consommation, d’un système "
           "impérial-maritime et d’un accès aux matières premières coloniales — un avantage "
           "géologique et impérial décisif.",
           "S’y ajoutent des facteurs géographiques et commerciaux : l’Angleterre est une île et "
           "une puissance navale, ouverte sur le commerce maritime et relativement protégée des "
           "invasions continentales, ce qui favorise la sécurité, la circulation des marchandises "
           "et l’expansion commerciale. Les colonies procurent bois, coton, sucre, matières "
           "premières et débouchés, alimentant le textile, le commerce et l’accumulation de "
           "richesse.",
           "Mais disposer de ressources ne suffit pas : encore faut-il que leur exploitation soit "
           "rentable. C’est l’apport de Robert Allen (Introduction à l’histoire économique "
           "mondiale, 2014) : la Grande-Bretagne combine des salaires élevés et une énergie bon "
           "marché. Le travail coûtant cher et le charbon peu, la mécanisation devient "
           "économiquement rationnelle — les entrepreneurs ont intérêt à substituer du capital au "
           "travail, à investir dans les machines et à innover pour économiser la main-d’œuvre."],
     'mec': "L’argument d’Allen est celui des prix relatifs : ce n’est pas la disponibilité "
            "technique d’une invention qui décide de son adoption, mais le rapport entre le coût "
            "du facteur qu’elle économise et celui du facteur qu’elle mobilise."},
    {'t': "E. Les institutions : North, le Parlement, Acemoglu et Robinson",
     'd': ["Douglass North (Institutions, changements institutionnels et performances "
           "économiques) montre qu’après 1688 et la Glorious Revolution, la Grande-Bretagne "
           "bénéficie d’un régime parlementaire stabilisé, d’une meilleure protection des droits "
           "de propriété, d’une plus grande sécurité juridique et d’un environnement favorable à "
           "l’investissement : la stabilité institutionnelle réduit l’incertitude et encourage "
           "l’investissement productif.",
           "Le Parlement ne se contente d’ailleurs pas de garantir les droits de propriété et la "
           "crédibilité des contrats : il possède la capacité politique d’imposer des "
           "transformations structurelles, en agissant sur les enclosures, les canaux, certains "
           "travaux d’infrastructure et la réorganisation foncière — parfois au détriment de "
           "certains groupes sociaux. Les institutions ne produisent pas directement des "
           "machines, mais elles créent un environnement favorable à l’investissement et à "
           "l’innovation.",
           "Acemoglu et Robinson (Why Nations Fail / Pourquoi les nations échouent) généralisent : "
           "les trajectoires économiques dépendent du type d’institutions. Les institutions "
           "inclusives favorisent innovation, investissement, mobilité sociale et "
           "entrepreneuriat ; les institutions extractives freinent l’initiative, la diffusion du "
           "progrès et la modernisation. La précocité anglaise s’explique donc moins par les "
           "seules ressources que par des institutions relativement plus favorables."]},
    {'t': "F. Effets d’entraînement, take-off, et la thèse du hasard",
     'd': ["L’industrialisation produit de puissants effets d’entraînement intersectoriels : elle "
           "génère une demande accrue de produits industriels pour l’agriculture (engrais, "
           "charrues) et de biens d’équipement et d’infrastructures (rails, locomotives), créant "
           "des liaisons amont/aval entre secteurs. Avec l’élargissement des marchés, la hausse "
           "de la population, l’urbanisation, les progrès techniques et l’amélioration des "
           "transports, la croissance devient plus cumulative — ce que Rostow appelle le take-off, "
           "situé pour la Grande-Bretagne entre 1783 et 1802.",
           "Une thèse plus provocatrice mérite d’être connue. Jacques Brasseul (Petite histoire "
           "des faits économiques, 2014) note que tous ces facteurs ne suffisent pas, car un "
           "certain nombre d’entre eux sont communs à d’autres pays d’Europe ; il rapporte que "
           "l’auteur anglais Nick Crafts aurait insisté sur le caractère fortuit de la révolution "
           "industrielle anglaise, la Grande-Bretagne ayant réalisé par hasard les premières "
           "inventions décisives."],
     'lim': "Le hasard peut jouer un rôle conjoncturel — opportunités historiques, inventions, "
            "conjonctures particulières — mais en histoire économique la thèse du hasard pur est "
            "insuffisante : la précocité anglaise résulte surtout de facteurs structurels et de "
            "leur articulation."},
   ],
   'v': "Cette conjonction débouche sur un double résultat : l’affirmation du factory system et "
        "une hégémonie économique mondiale — qui n’est pourtant pas définitive."},

  # ------------------------------------------------------------------ IV
  {'t': "IV. L’aboutissement : hégémonie britannique et contestation par les followers",
   'sp': [
    {'t': "A. Une domination mesurable",
     'd': ["Les chiffres sont spectaculaires : la part britannique dans l’industrie mondiale "
           "passe de 2 % en 1750 à 23 % en 1880, alors que la population britannique représente "
           "environ 2 % de la population mondiale. Avec un vingtième de la population, la "
           "Grande-Bretagne réalise près d’un quart de la production industrielle mondiale.",
           "Cette avance productive se prolonge en hégémonie systémique : au XIXᵉ siècle, la "
           "Grande-Bretagne est première puissance industrielle, premier exportateur, grand "
           "investisseur international, puissance commerciale dominante et cœur financier mondial "
           "avec la City de Londres."]},
    {'t': "B. Une avance historiquement située",
     'd': ["À partir de la fin du XIXᵉ siècle, l’Allemagne et les États-Unis rattrapent puis "
           "dépassent progressivement la Grande-Bretagne dans plusieurs secteurs : être pionnier "
           "donne un avantage, mais pas une domination éternelle.",
           "La trajectoire britannique montre ainsi qu’une industrialisation précoce peut produire "
           "une domination mondiale, tout en restant historiquement située et susceptible d’être "
           "contestée par de nouveaux centres du capitalisme — ceux de la seconde révolution "
           "industrielle."]},
   ],
   'v': "Cette analyse est historique et macroéconomique. Pour comprendre le mécanisme interne de "
        "transformation du capitalisme, il faut passer à Schumpeter, qui place l’innovation et "
        "l’entrepreneur au cœur de la dynamique."},

  # ------------------------------------------------------------------ V
  {'t': "V. Schumpeter : l’innovation comme moteur, et les trois ruptures",
   'sp': [
    {'t': "A. Première rupture : la dynamique contre l’équilibre",
     'd': ["Dans l’analyse classique puis néoclassique, l’entreprise est une unité de production "
           "abstraite insérée dans un marché qui tend vers l’équilibre ; chez les marginalistes, "
           "l’idéal théorique est la concurrence pure et parfaite — grand nombre d’agents, "
           "information parfaite, homogénéité des produits, allocation optimale des ressources.",
           "Schumpeter rompt avec cette lecture dans Théorie de l’évolution économique (1912) : "
           "le capitalisme ne doit pas être analysé à partir de l’équilibre mais à partir de la "
           "dynamique. Ce qui le caractérise n’est pas sa capacité à atteindre un équilibre mais "
           "sa capacité à se transformer sans cesse — un système en mouvement, instable, traversé "
           "par des ruptures et des innovations.",
           "Il ne cherche donc pas seulement à expliquer comment les prix se forment ou comment "
           "les marchés se stabilisent, mais pourquoi la croissance apparaît, pourquoi les "
           "structures productives se transforment, pourquoi certaines entreprises disparaissent "
           "tandis que d’autres émergent, et pourquoi l’économie évolue par phases plutôt que de "
           "manière linéaire. L’économie devient une théorie de l’évolution."]},
    {'t': "B. Les cinq formes d’innovation (DEPOB) et l’exemple de l’automobile",
     'd': ["L’apport majeur de Schumpeter est de montrer que l’innovation ne se réduit pas à "
           "l’invention d’une machine. Dans Théorie de l’évolution économique (1912), il "
           "distingue cinq formes, que le moyen mnémotechnique DEPOB récapitule : débouchés, "
           "énergie (matières premières), procédé, organisation, biens et services.",
           "L’innovation de produit met sur le marché un nouveau bien ou une nouvelle qualité de "
           "bien, ce qui permet de se différencier et de créer une demande. L’innovation de "
           "procédé introduit une nouvelle méthode de production, une nouvelle technique ou un "
           "nouveau mode d’organisation du travail — mécanisation, automatisation, rationalisation "
           "— et permet des gains de productivité et une baisse des coûts. L’innovation de "
           "débouchés donne accès à un nouveau marché, une nouvelle clientèle, une nouvelle zone "
           "géographique : l’innovation peut donc être commerciale et géographique. L’innovation "
           "de matière première ou d’énergie se lit dans l’automobile, qui suppose l’essence tirée "
           "du pétrole, donc la mise en place de stations-service. L’innovation organisationnelle "
           "enfin inclut une nouvelle organisation de la production, une nouvelle combinaison des "
           "facteurs, une nouvelle structure d’entreprise ou de marché.",
           "Le point fondamental est que l’innovation ne signifie pas inventer à partir de rien : "
           "elle consiste souvent à réaliser une nouvelle combinaison des ressources existantes.",
           "L’automobile illustre toute la typologie — et il faut préciser qu’il s’agit d’une "
           "illustration pédagogique, non nécessairement de l’exemple historique de Schumpeter "
           "lui-même. Débouchés : transports longue distance, trajets individuels, taxis, "
           "ambulances, livraisons, bus urbains. Énergie et infrastructures : essence, pétrole, "
           "stations-service. Procédés : la chaîne de montage de Ford, où le convoyeur fait venir "
           "les pièces aux ouvriers au lieu de les faire se déplacer. Biens et services induits : "
           "sidérurgie (acier, aluminium), chimie (caoutchouc, peinture), équipements "
           "automobiles, parkings, garages, assurances, écoles de conduite, tourisme, adaptation "
           "des routes.",
           "L’automobile transforme même l’environnement institutionnel. La signalisation routière "
           "se développe : premiers signaux et premiers panneaux de limitation de vitesse dès "
           "1902 ; première tentative d’unification internationale à Genève en 1909 ; panneaux de "
           "sens unique et de sens interdit en 1928. Le premier salon de l’automobile est inauguré "
           "en 1889, mais son véritable succès date surtout de 1902. Le réseau routier doit être "
           "adapté et étendu, ce qui renforce le rôle de la puissance publique."]},
    {'t': "C. L’entrepreneur innovateur et la destruction créatrice",
     'd': ["L’entrepreneur schumpétérien ne se confond ni avec le propriétaire du capital ni avec "
           "le gestionnaire ordinaire. Il n’est pas celui qui possède, qui administre ou qui "
           "reproduit une activité existante : il est celui qui introduit du nouveau, rompt avec "
           "la routine, prend des risques et transforme l’organisation productive. C’est un agent "
           "de rupture, non un gestionnaire.",
           "L’entreprise cesse dès lors d’être une simple unité de production pour devenir un "
           "espace de transformation, un centre de décision stratégique, le support institutionnel "
           "de l’innovation : c’est en son sein que se réalise le changement économique.",
           "D’où l’expression la plus célèbre de Schumpeter : la destruction créatrice. "
           "L’innovation crée une activité nouvelle, mais rend en même temps obsolètes des "
           "techniques anciennes, des entreprises installées, des métiers, des structures "
           "productives. Le progrès capitaliste est donc conflictuel : il crée de la richesse "
           "mais détruit des positions acquises. Le capitalisme n’est pas seulement un système de "
           "croissance, c’est un système de recomposition permanente."]},
    {'t': "D. Deuxième rupture : le monopole temporaire contre l’idéal de CPP",
     'd': ["Les marginalistes considèrent que la concurrence pure et parfaite est la structure de "
           "marché idéale. Schumpeter s’y oppose dans le domaine de l’innovation, pour une raison "
           "précise : l’innovation coûte cher, est risquée, exige des investissements, et ne peut "
           "pas être immédiatement copiée sans décourager l’innovateur. Si l’entreprise innovante "
           "est copiée instantanément, elle ne peut rentabiliser ni ses dépenses de recherche, ni "
           "ses prises de risque, ni ses efforts d’organisation.",
           "Il faut donc parfois laisser à l’innovateur une position dominante temporaire : "
           "avantage technologique, avance stratégique, brevet, quasi-monopole provisoire. Le "
           "brevet joue ici un rôle clé en protégeant juridiquement l’innovation, en empêchant la "
           "copie immédiate et en permettant un surprofit — la rente d’innovation. Cette rente "
           "n’est pas un privilège, c’est une incitation à innover.",
           "L’idée essentielle est contre-intuitive et doit être retenue comme telle : le monopole "
           "temporaire peut être plus favorable à l’innovation que la concurrence parfaite."],
     'lim': "Schumpeter ne défend jamais le monopole permanent : il défend un avantage provisoire "
            "qui récompense l’innovation, pas une rente de situation installée."},
    {'t': "E. Grappes d’innovations et cycles : Kitchin, Juglar, Kondratiev",
     'd': ["Une grande innovation ne reste jamais isolée : elle entraîne des innovations "
           "secondaires, des adaptations techniques, des perfectionnements, de nouveaux secteurs "
           "et des transformations organisationnelles. Schumpeter parle de grappes d’innovations "
           "— l’automobile entraînant garages, stations-service, routes adaptées, signalisation, "
           "assurance, mécanique spécialisée, nouveaux matériaux, nouvelles infrastructures.",
           "Deux niveaux doivent être distingués. L’innovation fondamentale ouvre un nouveau "
           "cycle : rupture majeure, nouveau secteur, nouvelle logique productive. L’innovation "
           "incrémentale est mineure ou progressive : elle ne bouleverse pas le système productif "
           "mais perfectionne un produit ou un procédé déjà introduit, améliore ses performances, "
           "réduit les coûts, adapte la technologie à de nouveaux usages. Elle ne crée pas un "
           "secteur à elle seule, mais elle permet de diffuser, stabiliser et rentabiliser "
           "l’innovation fondamentale. L’automobile est une innovation fondamentale ; "
           "l’amélioration des moteurs, les freins ABS, les boîtes automatiques, les airbags, les "
           "GPS intégrés sont des innovations incrémentales. Formule à retenir : l’innovation "
           "fondamentale ouvre un nouveau cycle, l’innovation incrémentale en assure la diffusion "
           "et le prolongement.",
           "Trois types de cycles, emboîtés, structurent alors le capitalisme. Les cycles de "
           "Kitchin, du nom de Joseph Kitchin, sont courts — environ 3 à 5 ans — et liés aux "
           "variations de stocks, aux ajustements rapides de la production et aux fluctuations de "
           "court terme. Les cycles de Juglar, du nom de Clément Juglar, sont moyens — environ 8 à "
           "10 ans — et associés à l’investissement productif et aux fluctuations du crédit, avec "
           "les phases classiques de reprise, expansion, crise et dépression. Les cycles de "
           "Kondratiev, du nom de l’économiste soviétique Nikolaï Kondratiev (1892-1938), sont "
           "longs — environ 50 à 60 ans — et se décomposent en une phase ascendante de 25 à 30 "
           "ans, où les innovations en grappe transforment les structures productives et "
           "stimulent l’investissement, et une phase descendante de durée comparable, où les "
           "innovations majeures ont été diffusées, les surprofits diminuent et la croissance "
           "ralentit.",
           "Ces cycles se superposent : des cycles de Kitchin apparaissent à l’intérieur d’un "
           "cycle de Juglar, et plusieurs cycles de Juglar s’inscrivent dans un cycle long de "
           "Kondratiev. Le capitalisme est traversé par plusieurs temporalités à la fois — courte "
           "(stocks), moyenne (investissement et crédit), longue (transformations structurelles "
           "liées aux innovations majeures)."],
     'mec': "Le lien avec Schumpeter est précis : tous les cycles ne s’expliquent pas par "
            "l’innovation. Les grappes d’innovations alimentent surtout les cycles longs de type "
            "Kondratiev, tandis que Kitchin et Juglar rappellent que l’économie capitaliste est "
            "traversée par plusieurs rythmes emboîtés. La première révolution industrielle est à "
            "cet égard un excellent exemple de grappe associable à une phase ascendante de cycle "
            "long : machine à vapeur, textile mécanisé, charbon, métallurgie et transports se "
            "combinent et se renforcent mutuellement."},
    {'t': "F. Troisième rupture : le capitalisme miné par son propre succès",
     'd': ["Schumpeter rejoint Marx sur un point — le capitalisme n’est pas éternel, il peut être "
           "historiquement dépassé — mais pour des raisons entièrement différentes : il ne met au "
           "centre ni la lutte des classes ni l’effondrement révolutionnaire, mais la "
           "transformation interne du système lui-même.",
           "Au début, le capitalisme est porté par des entrepreneurs audacieux, des innovateurs "
           "individuels, des figures de rupture. Mais à mesure qu’il se développe, les entreprises "
           "grossissent, les marchés se concentrent, les grandes firmes dominent, la bureaucratie "
           "s’installe et l’innovation devient plus routinière. L’entrepreneur innovateur tend "
           "donc à s’effacer au profit de grandes organisations, d’oligopoles et de structures "
           "bureaucratisées.",
           "L’évolution est paradoxale : le capitalisme triomphe, mais ce triomphe affaiblit ce "
           "qui faisait sa force initiale. Plus il se rationalise, plus la gestion remplace "
           "l’intuition, plus la grande firme remplace l’entrepreneur, plus l’innovation s’intègre "
           "dans des structures lourdes — au risque de perdre sa spontanéité créatrice et "
           "d’étouffer la fonction entrepreneuriale."],
     'lim': "Ouverture contemporaine : de la même façon que l’automobile thermique a formé une "
            "grande grappe, la voiture électrique (batteries, bornes de recharge, reconfiguration "
            "des filières énergétiques, métaux stratégiques, adaptation des réseaux) et la voiture "
            "autonome (capteurs, IA, logiciels embarqués, cartographie, réglementation, "
            "responsabilité juridique, infrastructures connectées) peuvent être lues comme de "
            "futures grappes d’innovations."},
   ],
   'v': "Pour que ces innovations produisent pleinement leurs effets, encore faut-il que les "
        "entreprises transforment leurs méthodes de production : c’est l’objet du taylorisme, puis "
        "du fordisme et du toyotisme."},

  # ------------------------------------------------------------------ VI
  {'t': "VI. L’organisation du travail : du taylorisme au toyotisme",
   'sp': [
    {'t': "A. Le problème auquel répond Taylor : la flânerie systématique",
     'd': ["À la fin du XIXᵉ siècle, malgré les progrès techniques, la productivité reste limitée "
           "par une organisation du travail héritée de l’artisanat : dans les ateliers "
           "traditionnels, les ouvriers sont qualifiés, maîtrisent l’ensemble du processus de "
           "production et contrôlent leur rythme de travail. Cette autonomie limite la capacité "
           "de l’entreprise à organiser efficacement la production : le travail échappe en partie "
           "à son contrôle.",
           "Taylor observe alors un phénomène central, qu’il nomme flânerie systématique "
           "(soldiering) : les ouvriers ralentissent volontairement leur production et limitent "
           "leur effort. Il faut comprendre que ce comportement est rationnel — produire plus peut "
           "entraîner une hausse des cadences sans garantie d’augmentation de salaire, voire avec "
           "un risque de dégradation des conditions de travail. Le problème est donc "
           "organisationnel, non moral."]},
    {'t': "B. L’OST : double division du travail et salaire comme instrument",
     'd': ["Le projet de Taylor consiste à transformer le travail en objet mesurable et "
           "rationnel : observation des gestes, découpage des tâches, chronométrage, avec pour "
           "objectif d’identifier la manière la plus efficace de produire — le one best way. Le "
           "travail n’est plus laissé à l’initiative de l’ouvrier : il est défini, standardisé et "
           "imposé.",
           "La rationalisation passe par une double division du travail. La division horizontale "
           "est la parcellisation : le travail est découpé en tâches simples, chaque ouvrier "
           "réalisant une opération élémentaire, répétitive et spécialisée — le travail perd son "
           "unité globale. La division verticale est la séparation entre conception (ingénieurs, "
           "bureau des méthodes) et exécution (ouvriers), d’où l’opposition entre cols blancs et "
           "cols bleus : l’ouvrier n’a plus à penser son travail, seulement à l’exécuter.",
           "Pour que le système fonctionne, il faut inciter les ouvriers à respecter les normes. "
           "Taylor considère que leur motivation principale est économique et met en place le "
           "salaire différentiel aux pièces : respect de la norme, salaire plus élevé ; "
           "non-respect, salaire plus faible. La rémunération devient un outil disciplinaire.",
           "Le double avantage est net : gains de temps par la spécialisation de chaque ouvrier "
           "dans une seule tâche, et meilleur contrôle du travail par le contremaître."],
     'lim': "Les limites sociales deviennent des limites économiques, et c’est l’enchaînement à "
            "retenir. La parcellisation entraîne monotonie, fatigue et perte de sens — Georges "
            "Friedmann parle de « travail en miettes » et l’ouvrier devient étranger à son "
            "travail, c’est-à-dire aliéné. Ces dysfonctionnements produisent un turn-over élevé, "
            "de l’absentéisme et des malfaçons, donc des coûts de recrutement, de formation, de "
            "remplacement et de retouches. La chaîne causale s’écrit : perte de sens → "
            "démotivation → erreurs → coûts → baisse de productivité."},
    {'t': "C. Le fordisme : chaîne, standardisation, et le compromis salarial",
     'd': ["Ford reprend les principes du taylorisme mais y ajoute deux changements décisifs : la "
           "chaîne de montage, qui vise la production de masse par standardisation, et "
           "l’augmentation des salaires, qui vise la consommation de masse.",
           "L’innovation majeure est le convoyeur : les objets se déplacent vers les ouvriers, le "
           "rythme est imposé, les temps morts sont supprimés. La standardisation suit : Ford "
           "produit un modèle unique, la Ford T, d’où simplification, fabrication en série et "
           "réduction des coûts. Les chiffres montrent l’ampleur du phénomène : une Ford coûte "
           "690 dollars en 1913 et 290 dollars en 1929 ; dès 1914, 60 % des voitures produites "
           "aux États-Unis sont des Ford.",
           "Le mécanisme sous-jacent est celui des économies d’échelle, qui reposent sur deux "
           "effets : l’étalement des coûts fixes et la baisse relative des coûts variables par "
           "remises et négociation. Le coût moyen — coût total divisé par la quantité produite — "
           "diminue, ce qui permet une baisse des prix et donc une augmentation de la demande.",
           "La hausse des salaires a deux justifications, et il faut les distinguer. D’abord une "
           "logique de débouchés : donner du pouvoir d’achat aux salariés pour qu’ils achètent la "
           "production — les ouvriers deviennent des clients potentiels. Ensuite une logique de "
           "fidélisation : le travail à la chaîne est répétitif, intensif et fatigant, donc le "
           "turn-over est élevé et coûteux (recrutement, formation, désorganisation). Ford fait "
           "passer les salaires de 2,5 dollars par jour, moyenne de l’époque, à 5 dollars la "
           "journée. En payant plus que les autres entreprises, il augmente le coût d’opportunité "
           "du départ : quitter Ford revient à renoncer à un salaire élevé, donc les ouvriers "
           "restent. Le taux de turn-over se mesure comme le nombre d’entrées ou de sorties "
           "rapporté à l’effectif total moyen de l’entreprise."],
     'lim': "Les limites du fordisme sont celles de la rigidité : production standardisée, travail "
            "répétitif, faible autonomie, conflits sociaux. Le système privilégie la quantité au "
            "détriment de la qualité. Les crises des années 1970 révèlent le ralentissement des "
            "gains de productivité, la saturation des marchés et la montée des conflits — le "
            "fordisme entre en crise."},
    {'t': "D. Le toyotisme : flux tendu, qualité, autonomation, kaizen",
     'd': ["Le modèle tayloro-fordiste entraîne surproduction, stocks, défauts et rigidité. Toyota "
           "cherche à optimiser l’ensemble du système : produire mieux, plus rapidement et sans "
           "gaspillage.",
           "Le juste-à-temps, ou flux tendu, en est le principe central : on ne produit que ce "
           "qu’on a vendu, et ce sont les postes en aval de la production qui déterminent "
           "l’amont — exactement l’inverse du fordisme. Pour éviter les gaspillages, le TPS "
           "(Toyota Production System) met en place la règle des cinq zéros : zéro stock, zéro "
           "délai, zéro panne, zéro défaut, zéro papier.",
           "La véritable rupture concerne la qualité. Dans une chaîne longue, même un faible taux "
           "d’erreur à chaque étape entraîne beaucoup de défauts au final : Toyota met donc en "
           "place un contrôle continu et un objectif de zéro défaut.",
           "Cela suppose de transformer le rôle des travailleurs : polyvalence, travail en équipe, "
           "responsabilité, et possibilité d’arrêter la chaîne — l’ouvrier devient acteur de la "
           "qualité. Le néologisme d’« autonomation », qui croise autonomie et automatisation, "
           "désigne cette organisation : les ouvriers, désormais appelés opérateurs, travaillent "
           "en équipes semi-autonomes et surveillent le bon fonctionnement des machines afin "
           "d’éviter erreurs et malfaçons, les machines s’arrêtant automatiquement en cas de "
           "problème. Les opérateurs sont par ailleurs sollicités pour proposer des améliorations "
           "de leur poste : c’est la démarche du kaizen, l’amélioration continue."],
     'lim': "Rupture ou prolongement ? Le TPS reprend certains principes tayloriens, notamment la "
            "recherche d’une forte productivité avec chronométrage des tâches, mais veut en "
            "corriger les défauts en privilégiant la qualité sur la quantité. Ses propres limites "
            "sont l’intensification du travail, la pression permanente, le stress et la dépendance "
            "aux chaînes logistiques : les flux tendus rendent la production plus vulnérable aux "
            "perturbations, de sorte que la flexibilité peut accroître la fragilité des "
            "entreprises comme des salariés."},
   ],
   'v': "Derrière ces transformations organisationnelles surgit une question de pouvoir : la "
        "question n’est plus comment produire efficacement, mais qui décide dans l’entreprise."},

  # ------------------------------------------------------------------ VII
  {'t': "VII. Le capitalisme entrepreneurial : propriété et pouvoir confondus",
   'sp': [
    {'t': "A. La confusion originelle entre propriété et contrôle",
     'd': ["Aux débuts du capitalisme industriel, la gouvernance repose sur une logique simple : "
           "celui qui possède l’entreprise est aussi celui qui la dirige. Au XIXᵉ siècle, "
           "l’entreprise est de petite taille, peu complexe, et repose sur une personne centrale. "
           "L’entrepreneur cumule la propriété du capital, la direction de l’entreprise et "
           "souvent l’activité productive elle-même : il y a confusion totale entre propriété et "
           "contrôle.",
           "Ce capitalisme est fréquemment familial et personnalisé : les entreprises sont "
           "transmises de génération en génération, liées à une dynastie, et le nom de "
           "l’entreprise reflète souvent la famille — Peugeot, Hermès.",
           "L’entrepreneur est une figure économique totale : apporteur de capital, organisateur "
           "de la production, décideur, parfois travailleur lui-même. Il n’est pas salarié, il "
           "est son propre patron. À l’origine, en entrepreneur individuel, il n’existe pas de "
           "séparation entre patrimoine personnel et patrimoine de l’entreprise : il engage ses "
           "biens professionnels mais aussi ses biens personnels. Ce risque maximal renforce "
           "précisément la centralité de sa position."]},
    {'t': "B. Une figure valorisée : Weber et Schumpeter",
     'd': ["Max Weber distingue trois formes de domination : rationnelle-légale, traditionnelle et "
           "charismatique. L’entrepreneur peut incarner la domination charismatique, par sa "
           "capacité à entraîner, à convaincre, à susciter l’adhésion. Chez Weber, le pouvoir ne "
           "repose pas uniquement sur la richesse ou la position hiérarchique mais peut reposer "
           "sur une qualité personnelle : si les individus suivent l’entrepreneur, ce n’est pas "
           "seulement parce qu’il est propriétaire, mais parce qu’il inspire, motive et fédère.",
           "Schumpeter fournit l’autre pilier de la valorisation : l’entrepreneur est un "
           "innovateur, un preneur de risque, un agent de transformation, une sorte d’« aventurier "
           "de l’économie ». L’économie n’avance pas toute seule : elle progresse grâce à des "
           "individus qui cassent les routines."]},
    {'t': "C. Le mythe de l’entrepreneur : la critique de Galluzzo",
     'd': ["Le récit dominant est puissant : un individu seul, parti de rien, doté d’un génie "
           "créatif, qui réussit par son mérite — Steve Jobs, Elon Musk, Renault, Vuitton.",
           "Galluzzo (Le mythe de l’entrepreneur, 2023) critique cette vision héroïque. Son idée "
           "centrale est que le capitalisme moderne construit une image héroïque de "
           "l’entrepreneur pour légitimer l’ordre économique et social. Ce récit cache plusieurs "
           "réalités : l’innovation est collective ; les salariés, ingénieurs, chercheurs et "
           "managers jouent un rôle majeur ; l’État finance souvent une partie essentielle des "
           "innovations ; beaucoup d’entrepreneurs viennent déjà de milieux favorisés ; le succès "
           "dépend aussi des réseaux, du capital et du contexte historique.",
           "L’entrepreneur n’est jamais seul : l’entreprise est une production collective, et la "
           "figure héroïque masque la dimension socialement déterminée de la réussite."],
     'lim': "Au-delà de la critique idéologique, le capitalisme entrepreneurial rencontre une "
            "limite pratique : avec les révolutions industrielles, les entreprises grandissent, "
            "les techniques se complexifient, la gestion devient plus difficile — une seule "
            "personne ne peut plus tout contrôler efficacement."},
   ],
   'v': "Il devient nécessaire de mobiliser des compétences spécialisées : la séparation entre "
        "propriété et direction s’amorce, et avec elle le capitalisme managérial."},

  # ------------------------------------------------------------------ VIII
  {'t': "VIII. Du capitalisme managérial au capitalisme actionnarial",
   'sp': [
    {'t': "A. La professionnalisation de la direction : Fayol",
     'd': ["Avec les révolutions industrielles, les techniques deviennent plus complexes "
           "(sidérurgie, chemins de fer, machines sophistiquées), les infrastructures se "
           "développent, l’organisation de la production s’élargit. Il faut mobiliser des savoirs "
           "spécialisés, ce qui explique la montée des ingénieurs, formés dans les écoles "
           "techniques et scientifiques : ils conçoivent, organisent et améliorent les processus "
           "productifs, prolongeant la logique taylorienne de séparation entre conception et "
           "exécution.",
           "Mais la technique ne suffit pas : une grande entreprise doit gérer des flux complexes "
           "— salariés, finances, approvisionnements, stratégie. Apparaît alors la figure du "
           "manager, et une division du travail au sein même de la direction, avec des fonctions "
           "distinctes (production, finance, ressources humaines, stratégie).",
           "Henri Fayol, dans Administration industrielle et générale (1916), montre que la "
           "gestion peut être organisée rationnellement autour de fonctions précises : prévoir, "
           "organiser, commander, coordonner, contrôler. Avant lui, diriger relevait surtout de "
           "l’expérience personnelle ou du talent individuel ; Fayol rompt avec cette vision en "
           "montrant que la gestion peut devenir une science organisée, avec des règles générales "
           "applicables à toutes les entreprises. La direction devient une compétence enseignable, "
           "d’où le développement des écoles de commerce et des formations à la gestion."],
     'mec': "L’exemple est éclairant : une grande entreprise sidérurgique ou ferroviaire ne peut "
            "plus être dirigée à l’intuition par son propriétaire, car il faut planifier la "
            "production, coordonner des milliers de salariés, gérer les finances et organiser les "
            "approvisionnements. La direction devient une compétence spécifique, distincte de la "
            "simple possession du capital."},
    {'t': "B. La séparation propriété / contrôle : Berle et Means, Galbraith",
     'd': ["Berle et Means, dans The Modern Corporation and Private Property (1932), analysent la "
           "rupture : dans les grandes entreprises modernes, les actionnaires détiennent le "
           "capital tandis que les managers assurent la direction. Le capital est dispersé entre "
           "de nombreux actionnaires, qui ne disposent ni du temps, ni des compétences, ni de "
           "l’information nécessaires pour gérer l’entreprise : ils délèguent donc le pouvoir aux "
           "managers. Ceux qui possèdent ne dirigent plus, ceux qui dirigent ne possèdent pas "
           "nécessairement.",
           "Mais la domination des managers ne s’explique pas seulement par la dispersion du "
           "capital. Galbraith, dans Le Nouvel État industriel (1967), l’explique par la maîtrise "
           "de l’information et des compétences, à travers le concept de technostructure : "
           "l’ensemble des dirigeants, cadres, ingénieurs et experts qui participent à la "
           "direction effective de l’entreprise. Ce groupe détient le pouvoir réel parce qu’il "
           "maîtrise les connaissances nécessaires à la décision.",
           "L’idée clé est donc que le pouvoir dans l’entreprise repose désormais sur la maîtrise "
           "de l’information et des compétences, et non plus uniquement sur la propriété du "
           "capital. Les grandes entreprises sont devenues si complexes que les actionnaires ne "
           "peuvent plus réellement les contrôler. Cette gouvernance managériale a d’ailleurs un "
           "avantage : elle privilégie la stabilité, l’innovation et la planification de long "
           "terme."]},
    {'t': "C. La « main visible » des managers : Chandler, formes U et M",
     'd': ["Chandler, dans La main visible des managers (1977), montre à partir d’une analyse "
           "historique que le succès de l’économie américaine, notamment après 1840, vient de sa "
           "capacité à développer des firmes de grande taille intégrées verticalement et "
           "horizontalement. La grande entreprise peut être efficiente en réalisant des économies "
           "d’échelle, en s’appuyant sur la division du travail et en faisant appel aux managers "
           "pour coordonner les activités en dehors du marché.",
           "D’où la formule qui structure tout l’argument : à la main invisible du marché chère à "
           "Adam Smith, Chandler oppose la main visible des managers — « la main visible de la "
           "gestion remplaçait la main invisible des forces du marché dans la coordination des "
           "flux de marchandises ». La coordination ne repose plus uniquement sur le marché mais "
           "sur l’organisation interne des firmes.",
           "Cette transformation se traduit par de nouvelles structures. La forme U (unitaire) est "
           "une organisation centralisée, structurée par fonctions — production, finance, etc. La "
           "forme M (multidivisionnelle) est décentralisée, divisée en unités autonomes par "
           "produit ou par zone géographique, tout en conservant une direction stratégique "
           "centrale : c’est elle qui permet de gérer des entreprises complexes et diversifiées."]},
    {'t': "D. Le retour des actionnaires : Bourguinat, Jensen et Meckling, Friedman",
     'd': ["À partir des années 1970-1980, le développement des marchés financiers, la "
           "mondialisation et la libéralisation renforcent le rôle des investisseurs. Henri "
           "Bourguinat résume cette transformation par trois dynamiques, les « 3D » : "
           "désintermédiation, décloisonnement, déréglementation. Les entreprises accèdent "
           "directement aux marchés financiers et en deviennent dépendantes.",
           "De nouveaux acteurs prennent une place centrale — fonds d’investissement, private "
           "equity, investisseurs institutionnels — et exercent une pression forte pour améliorer "
           "la rentabilité financière. Cela se traduit par des restructurations, des réductions de "
           "coûts, des licenciements et une distribution accrue de dividendes, ainsi que par une "
           "hausse des rémunérations des dirigeants souvent liées à la performance boursière.",
           "Se met alors en place un ensemble de mécanismes regroupés sous le terme de corporate "
           "governance, ou gouvernance d’entreprise : dans les sociétés anonymes, il s’agit de "
           "faire en sorte que les managers agissent dans l’intérêt des actionnaires, en réduisant "
           "les asymétries d’information et en faisant augmenter la valeur des actions.",
           "Le support théorique est la théorie de l’agence, formalisée par Jensen et Meckling "
           "dans Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure "
           "(1976). Elle analyse les contrats par lesquels un principal fait appel à un agent pour "
           "exécuter en son nom une tâche impliquant la délégation d’un certain pouvoir. Ici, le "
           "principal est l’actionnaire et l’agent le manager, et la relation présente deux "
           "caractéristiques : incertitude et asymétrie d’information. Les managers disposant "
           "d’informations supérieures peuvent poursuivre leurs propres objectifs — maximiser leur "
           "pouvoir, leur rémunération ou la croissance de l’entreprise plutôt que le profit des "
           "actionnaires.",
           "Le contrôle de l’agent engendre des coûts d’agence, essentiellement des coûts de "
           "surveillance. L’enjeu pour le principal est donc de recourir à des incitations : "
           "dispositifs de contrôle (conseil d’administration, audit) et dispositifs d’incitation "
           "(stock-options, rémunérations variables). Les stock-options sont des options d’achat "
           "sur des actions attribuées à des salariés, le plus souvent des cadres, à un prix "
           "souvent plus faible que celui du marché et avec une fiscalité avantageuse quand les "
           "actions sont conservées un certain temps.",
           "Milton Friedman fournit enfin la justification normative dans The Social "
           "Responsibility of Business is to Increase its Profits (1970) : la seule responsabilité "
           "de l’entreprise est de maximiser le profit. L’entreprise est un instrument au service "
           "des actionnaires, les dimensions sociales et environnementales étant secondaires."],
     'mec': "L’histoire de la gouvernance se résume donc en trois temps : capitalisme "
            "entrepreneurial, pouvoir concentré entre les mains de l’entrepreneur ; capitalisme "
            "managérial, pouvoir exercé par les managers ; capitalisme actionnarial, pouvoir "
            "recentré sur les actionnaires. Un sujet sur la bonne gouvernance d’entreprise "
            "s’organise d’ailleurs naturellement en opposant ces trois configurations."},
   ],
   'v': "Mais cette domination actionnariale soulève rapidement ses propres limites : "
        "court-termisme, inégalités, scandales — d’où la contestation du modèle."},

  # ------------------------------------------------------------------ IX
  {'t': "IX. Les limites du capitalisme actionnarial : parties prenantes et RSE",
   'sp': [
    {'t': "A. Les critiques du modèle actionnarial",
     'd': ["Première critique, le court terme : les entreprises recherchent une hausse rapide de "
           "la valeur boursière, une rentabilité immédiate, la satisfaction des marchés "
           "financiers, au détriment de l’horizon long.",
           "Deuxième critique, les dérives : le scandale Enron en 2001, marqué par des "
           "manipulations comptables et une faillite retentissante, en fournit l’illustration la "
           "plus citée.",
           "Troisième critique, les inégalités. Les dispositifs d’incitation utilisés pour motiver "
           "les managers viennent s’ajouter à leur rémunération. Nicholas Bloom, dans Corporations "
           "in the Age of Inequality (Harvard Business Review, 2017), constate des écarts de "
           "revenus restés constants au sein des entreprises, mais croissants entre les "
           "entreprises — la gouvernance actionnariale peut donc accentuer les inégalités, et pas "
           "seulement à l’intérieur des firmes.",
           "S’y ajoute une pression excessive sur les salariés, dérivée de la recherche permanente "
           "de rentabilité."]},
    {'t': "B. Les parties prenantes et Polanyi",
     'd': ["Une approche alternative se développe, celle des parties prenantes (stakeholders) : "
           "l’entreprise ne concerne pas uniquement les actionnaires mais un ensemble d’acteurs — "
           "salariés, clients, fournisseurs, État, territoires, environnement. Les intérêts à "
           "prendre en compte sont donc multiples.",
           "Cette perspective rejoint Karl Polanyi (La Grande Transformation, 1944), pour qui "
           "l’économie ne peut être autonome : elle doit être encastrée dans la société. "
           "L’encastrement désigne l’insertion nécessaire des relations économiques dans des "
           "rapports sociaux, des règles et des institutions — le marché ne peut pas être le seul "
           "principe d’organisation de la société.",
           "Le modèle des parties prenantes remet ainsi en cause la centralité des actionnaires en "
           "intégrant des intérêts multiples dans la gouvernance : l’entreprise devient un acteur "
           "économique, social et environnemental."]},
    {'t': "C. La RSE, la loi PACTE et le risque de greenwashing",
     'd': ["La responsabilité sociale des entreprises consiste à intégrer aux objectifs "
           "économiques des préoccupations sociales et environnementales : l’entreprise devient un "
           "acteur du développement durable.",
           "Cette évolution se traduit juridiquement. En France, la loi PACTE (2019) introduit la "
           "notion de « raison d’être » et le statut d’entreprise à mission : l’entreprise peut "
           "désormais poursuivre des objectifs autres que le profit.",
           "Mais la limite est immédiate : certaines entreprises adoptent un discours responsable "
           "sans modifier réellement leurs pratiques — c’est le greenwashing. Le scandale "
           "Volkswagen, lié à la falsification des émissions polluantes, illustre ces "
           "contradictions."],
     'lim': "Le capitalisme contemporain est donc traversé par une tension entre une logique "
            "actionnariale centrée sur la rentabilité et une logique élargie intégrant les parties "
            "prenantes : la gouvernance évolue vers un modèle hybride, et l’entreprise ne peut "
            "plus être réduite à un simple instrument de profit."},
   ],
   'v': "Cette redéfinition du rôle de l’entreprise se heurte alors à une nouvelle mutation : "
        "l’essor des plateformes, du big data et de l’IA fait émerger un capitalisme numérique."},

  # ------------------------------------------------------------------ X
  {'t': "X. Le capitalisme numérique de plateforme : opportunités et menaces",
   'sp': [
    {'t': "A. Trois dynamiques : IA, big data, plateformes",
     'd': ["La révolution numérique actuelle repose sur trois dynamiques : l’intelligence "
           "artificielle et la robotisation, le big data, et les plateformes numériques.",
           "L’IA peut être définie comme l’art de faire réaliser par des machines des tâches qui, "
           "si elles étaient effectuées par des humains, seraient considérées comme "
           "intelligentes. Elle marque un changement important : les machines ne remplacent plus "
           "seulement la force de travail physique mais aussi certaines capacités cognitives — "
           "produire des textes, analyser des données massives, aider à la décision. Elle reste "
           "cependant fondamentalement probabiliste : elle repose sur des traitements statistiques "
           "et ne comprend pas réellement le sens des informations qu’elle manipule. L’IA ne pense "
           "pas, elle calcule.",
           "Le big data fait des données une matière première centrale du système productif. Satya "
           "Nadella résume la chose d’une formule : « les données sont la nouvelle électricité ». "
           "Les entreprises accumulent les données parce qu’elles permettent de faire fonctionner "
           "les algorithmes, d’améliorer l’IA, de mieux connaître les consommateurs, de cibler les "
           "comportements, d’anticiper les achats, d’orienter la publicité.",
           "Les plateformes transforment enfin la coordination économique en mettant en relation "
           "offreurs et demandeurs tout en réduisant fortement les coûts de transaction : Amazon, "
           "Google, Uber, Airbnb, Meta, Alibaba, Tencent deviennent les acteurs centraux du "
           "système. Le capitalisme contemporain est ainsi qualifié de capitalisme numérique, de "
           "capitalisme de surveillance ou de capitalisme de plateforme."],
     'mec': "Une caractéristique distingue cette révolution des précédentes : sa vitesse de "
            "diffusion. Là où les innovations passées mettaient plusieurs décennies à s’imposer, "
            "certaines technologies actuelles atteignent des millions d’utilisateurs en quelques "
            "mois. Il y a donc une accélération historique — mais pas une rupture totale : la "
            "révolution prolonge l’informatique et internet et soulève des questions déjà "
            "anciennes (impact sur l’emploi, gains de productivité, concentration du pouvoir "
            "économique)."},
    {'t': "B. Les opportunités : économie du partage et économie servicielle",
     'd': ["La révolution numérique permet l’innovation, la rapidité des échanges, la baisse de "
           "certains coûts, le développement de nouveaux services, la circulation rapide de "
           "l’information et l’économie collaborative. Les plateformes mettent directement en "
           "relation producteurs et consommateurs, réduisent certains coûts de transaction et "
           "mutualisent certains usages — covoiturage, location de logements, vente d’objets "
           "d’occasion, plateformes de travail.",
           "C’est ce que certains appellent l’économie du partage : les individus n’achètent plus "
           "seulement des biens, ils partagent leur usage — louer une voiture plutôt que "
           "l’acheter, partager un trajet, louer un appartement temporairement.",
           "Cette logique rejoint l’économie servicielle développée notamment par Pierre Veltz : "
           "on vend moins le bien lui-même que l’accès au service rendu par ce bien. Renault peut "
           "louer l’usage d’une voiture, Spotify vend l’accès à la musique plus que la propriété "
           "matérielle des albums."]},
    {'t': "C. Les menaces économiques : concentration et effets de réseau",
     'd': ["Le capitalisme numérique renforce la concentration économique, parce que les "
           "plateformes bénéficient d’effets de réseau, d’économies d’échelle et d’une "
           "accumulation massive de données. Le mécanisme est auto-renforçant : plus une "
           "plateforme possède d’utilisateurs, plus elle devient attractive, donc plus elle attire "
           "de nouveaux utilisateurs.",
           "Cela favorise des situations d’oligopole, voire de monopole, et confère aux grandes "
           "plateformes un pouvoir économique considérable : les GAFAM aux États-Unis, les BATX en "
           "Chine. De nombreux acteurs traditionnels dénoncent une concurrence déloyale, une "
           "fiscalité avantageuse, des positions dominantes et une captation des marchés."]},
    {'t': "D. Les menaces sociales : ubérisation, isolement, économie de l’attention",
     'd': ["Les plateformes modifient le travail en favorisant la flexibilité, les emplois "
           "précaires, les contrats courts, l’auto-entrepreneuriat et le travail indépendant. "
           "L’exemple canonique est Uber, qui ne possède quasiment pas de véhicules mais coordonne "
           "des centaines de milliers de chauffeurs : les facteurs de production sont externalisés "
           "— la voiture appartient au chauffeur, les coûts sont supportés par les travailleurs — "
           "tandis que la plateforme capte une commission. D’où le terme d’ubérisation du travail.",
           "Le numérique transforme aussi les rapports sociaux, et de façon paradoxale : nous "
           "sommes plus connectés que jamais, mais de nombreux auteurs soulignent une montée du "
           "sentiment de solitude — c’est l’idée résumée par Sherry Turkle dans l’expression "
           "« seuls ensemble ». Hyperconnexion technique, mais isolement social parfois accru.",
           "Bruno Patino développe enfin l’idée de « civilisation du poisson rouge » : le "
           "numérique réduit progressivement notre capacité d’attention. Les plateformes cherchent "
           "à capter notre temps, retenir notre attention, multiplier les interactions rapides, "
           "parce que plus nous restons sur les écrans, plus nous produisons de données, plus les "
           "algorithmes s’améliorent et plus ces données sont monétisables. Le capitalisme "
           "numérique devient un capitalisme de l’attention, dans lequel l’attention humaine "
           "devient une ressource économique — l’attention et les données constituant les intrants "
           "non rémunérés du système."]},
    {'t': "E. Les menaces politiques et écologiques",
     'd': ["Sur le plan politique, les données que nous fournissons ne nous appartiennent plus "
           "réellement : elles sont collectées, stockées, analysées, revendues. Cela pose des "
           "questions de surveillance, de contrôle social et de manipulation politique. Les "
           "réseaux sociaux peuvent influencer les comportements, les opinions et les élections, "
           "et les algorithmes orientent les informations visibles, les contenus recommandés et "
           "les débats publics — d’où l’expression de capitalisme de surveillance. Cette logique "
           "est particulièrement visible dans certains régimes autoritaires, le cas chinois "
           "articulant capitalisme numérique et contrôle politique.",
           "Sur le plan écologique, le numérique donne l’impression d’un monde immatériel — cloud, "
           "données virtuelles, économie dématérialisée. Mais cette dématérialisation est "
           "largement illusoire : le numérique repose sur des centres de données, des "
           "infrastructures industrielles, des antennes, des câbles, de l’électricité et de l’eau. "
           "Le cloud repose sur des infrastructures gigantesques, et le capitalisme numérique "
           "produit donc des coûts écologiques importants, souvent invisibilisés."]},
   ],
   'v': "Ces transformations invitent à une question plus large : le capitalisme change-t-il de "
        "nature, ou ne fait-il que changer de forme ? C’est la question de sa pluralité."},

  # ------------------------------------------------------------------ XI
  {'t': "XI. Le capitalisme est historique et pluriel",
   'sp': [
    {'t': "A. Pluralité dans le temps : régulation et trois âges",
     'd': ["Marx et Schumpeter annoncent tous deux la fin du capitalisme, mais pour des raisons "
           "très différentes. La plupart des auteurs considèrent au contraire qu’il se transforme "
           "mais perdure, et s’intéressent donc à ses formes historiques.",
           "L’École de la régulation distingue par exemple un capitalisme concurrentiel puis un "
           "capitalisme monopolistique, la crise de 1929 ayant profondément transformé les modes "
           "de régulation. D’autres distinguent, comme on l’a vu, capitalisme entrepreneurial, "
           "managérial et actionnarial. Le capitalisme change ainsi selon les structures de "
           "propriété, les modes de gouvernance et les révolutions technologiques.",
           "François et Mercier proposent une périodisation en trois âges. L’âge du commerce, "
           "jusqu’au XVIIIᵉ siècle, a pour figures centrales le marchand et le négociant : le "
           "capitalisme repose principalement sur le commerce. L’âge de l’usine, avec les "
           "révolutions industrielles, a pour figures l’ouvrier puis le manager : le capitalisme "
           "devient industriel. L’âge de la finance, depuis les années 1980, a pour figures "
           "l’actionnaire et l’intérimaire : le capitalisme devient financiarisé, flexible et "
           "mondialisé, et le travail plus précaire."]},
    {'t': "B. Pluralité dans l’espace : modèles nationaux et émergents",
     'd': ["Les pays capitalistes ne fonctionnent pas tous de la même manière : certains modèles "
           "sont plus libéraux, d’autres plus sociaux-démocrates, d’autres plus interventionnistes. "
           "Les différences portent notamment sur le rôle de l’État, la protection sociale et le "
           "marché du travail. Certains privilégient la flexibilité, le marché et une faible "
           "intervention publique — les États-Unis ; d’autres la protection sociale, la régulation "
           "et les droits des salariés — la France.",
           "La diversité se retrouve chez les émergents, qui n’adoptent pas tous la même "
           "stratégie : certains privilégient l’industrialisation et les exportations "
           "manufacturières, d’autres reposent davantage sur les matières premières et les "
           "ressources énergétiques. Le Mexique relève d’une logique industrielle, le Venezuela "
           "d’une logique rentière pétrolière. Les formes du capitalisme dépendent donc du rôle de "
           "l’État, de l’insertion internationale et du modèle de croissance choisi."]},
    {'t': "C. Les quatre piliers du capitalisme sont-ils remis en cause ?",
     'd': ["Le capitalisme repose traditionnellement sur quatre piliers : la propriété privée, le "
           "salariat, le marché et les prix — c’est-à-dire la régulation marchande — et la "
           "recherche du profit. La révolution numérique semble parfois les remettre en cause, "
           "mais cette remise en cause est ambiguë.",
           "La propriété privée d’abord. L’économie du partage — covoiturage, Airbnb, échange de "
           "logements — semble la réduire. Mais derrière le partage il existe souvent une logique "
           "de rentabilisation : quand un individu loue son logement, revend ses vêtements ou "
           "partage sa voiture, il cherche aussi à tirer un revenu de son bien. L’économie du "
           "partage peut donc correspondre à une extension de la logique marchande à de nouveaux "
           "usages, non à sa disparition.",
           "Le marché ensuite. Beaucoup de services numériques paraissent gratuits — Wikipédia, "
           "réseaux sociaux, versions gratuites d’IA. Mais cette gratuité est trompeuse : quand "
           "c’est gratuit, c’est souvent l’utilisateur qui devient le produit, les plateformes se "
           "rémunérant par les commissions, la publicité et la revente des données. Le prix n’a "
           "pas disparu, il est simplement déplacé.",
           "Conclusion : le capitalisme numérique transforme les mécanismes du marché mais ne "
           "supprime pas la logique marchande."]},
   ],
   'v': "Reste le pilier du salariat, et c’est le plus directement affecté : les transformations "
        "technologiques modifient en profondeur les statuts d’emploi et les protections qui leur "
        "sont attachées."},

  # ------------------------------------------------------------------ XII
  {'t': "XII. Travail, emploi et précarisation",
   'sp': [
    {'t': "A. Deux notions à ne pas confondre",
     'd': ["Le travail désigne toute activité productive, rémunérée ou non : travail domestique, "
           "bénévole, associatif, salarié. Il renvoie aux tâches réalisées, aux conditions "
           "d’exercice, aux qualifications et à l’organisation du travail. Quand on parle de "
           "cadences, de télétravail, d’IA ou de conditions physiques, on parle des conditions de "
           "travail.",
           "L’emploi correspond à un travail rémunéré : exercer une activité professionnelle dans "
           "un cadre juridique précis, généralement avec un contrat. Il renvoie au statut du "
           "travailleur, à la stabilité du contrat, à la durée du travail et aux protections "
           "sociales. Quand on parle de CDI, de CDD, de temps plein ou de temps partiel, on parle "
           "des conditions d’emploi.",
           "En France, les actifs occupés se répartissent en deux grandes catégories. Les "
           "indépendants travaillent pour leur propre compte sans être liés par un contrat de "
           "travail — artisans, commerçants, professions libérales, auto-entrepreneurs : environ "
           "13,5 % des actifs, avec une place croissante des micro-entrepreneurs. Les salariés "
           "travaillent pour le compte d’un employeur et représentent environ 86 % des actifs "
           "occupés."]},
    {'t': "B. La salarisation et la construction des droits sociaux",
     'd': ["Avant les révolutions industrielles, la population travaillait principalement dans "
           "l’agriculture, l’artisanat et le travail à domicile, et les travailleurs étaient "
           "souvent indépendants. Avec les révolutions industrielles, les machines deviennent plus "
           "importantes, plus coûteuses, et nécessitent une concentration des travailleurs dans "
           "les usines : les ouvriers deviennent salariés. La salarisation désigne ce passage "
           "d’une population majoritairement indépendante à une population majoritairement "
           "salariée.",
           "Le développement du salariat s’est accompagné d’une extension des protections "
           "sociales : congés payés, protection sociale, droits syndicaux, protections contre les "
           "accidents du travail, droits à la retraite, assurances chômage.",
           "L’exemple le plus important est la loi de 1898 sur les accidents du travail. Avant "
           "cette loi, un accident du travail était considéré comme relevant de la responsabilité "
           "du salarié ; après elle, l’employeur peut être tenu responsable des accidents liés au "
           "travail. Les révolutions industrielles ont donc aussi contribué à améliorer "
           "progressivement les protections des travailleurs."]},
    {'t': "C. Le ludisme : la résistance au progrès technique",
     'd': ["À chaque grande révolution technologique, des travailleurs ont craint la destruction "
           "de leurs emplois. Le mouvement des luddites apparaît en Angleterre entre 1811 et "
           "1816 : des ouvriers du textile détruisent des machines industrielles, considérant "
           "qu’elles remplacent leur travail. Le ludisme désigne cette contestation des machines "
           "perçues comme une menace pour l’emploi.",
           "Mais les ouvriers ne contestent pas seulement la perte d’emploi : ils dénoncent aussi "
           "les nouvelles cadences, la discipline industrielle, l’autorité du contremaître et la "
           "perte d’autonomie — avec les machines, les travailleurs doivent suivre le rythme "
           "imposé par la machine. Le progrès technique améliore la productivité, mais transforme "
           "aussi profondément les conditions de travail."],
     'lim': "Cette question reste entièrement actuelle : la peur d’une destruction massive "
            "d’emplois par l’IA rappelle directement le mouvement des luddites, et c’est le fil "
            "qui relie cette partie à la dernière."},
    {'t': "D. Contrats, prud’hommes et temps partiel",
     'd': ["Le CDI, contrat à durée indéterminée, est associé à la stabilité de l’emploi : en "
           "France, 73 % des salariés sont en CDI, et la durée moyenne dans une entreprise est "
           "d’environ 11 ans. Il constitue la norme traditionnelle du salariat stable.",
           "Le CDD, contrat à durée déterminée, concerne 27 % des salariés. Il prévoit une date de "
           "début et une date de fin et répond en principe à un besoin temporaire — remplacement, "
           "activité saisonnière, hausse ponctuelle d’activité. En principe, un CDD ne doit pas "
           "dépasser 18 mois dans la plupart des cas. Il est considéré comme plus précaire "
           "puisque le salarié sait que son contrat prendra fin. Certaines entreprises en font "
           "toutefois un usage abusif, des salariés travaillant parfois des années avec des "
           "contrats précaires successifs — ce qui conduit à des conflits devant les prud’hommes.",
           "Les prud’hommes sont des tribunaux spécialisés dans les conflits du travail : litiges "
           "entre employeurs et salariés, abus de contrats, licenciements, conflits de droit du "
           "travail. Ces conflits révèlent un déséquilibre : les entreprises peuvent chercher à "
           "réduire les coûts, éviter les CDI et limiter les protections sociales, tandis que les "
           "salariés cherchent la stabilité, des protections et des droits. Le marché du travail "
           "repose donc aussi sur un rapport de force social.",
           "Le temps plein est généralement fixé en France à 35 heures hebdomadaires, certains "
           "secteurs restant à 39 heures. Le temps partiel désigne une durée inférieure au temps "
           "légal, et il faut distinguer le temps partiel choisi — volontairement, pour des "
           "études, du sport, la vie familiale — du temps partiel subi, où le salarié souhaiterait "
           "travailler davantage mais où l’entreprise ne propose pas plus d’heures. Le temps "
           "partiel subi constitue une forme de précarité."]},
    {'t': "E. La précarisation depuis les années 1970 et le retour de l’indépendance",
     'd': ["Depuis la crise de 1973, on observe une précarisation croissante de l’emploi, qui "
           "prend plusieurs formes : hausse des CDD, hausse du temps partiel subi, contrats "
           "courts, intérim, auto-entrepreneuriat contraint. Même si la majorité des salariés "
           "restent en CDI à temps plein, les formes précaires augmentent.",
           "Une conséquence majeure est la pauvreté laborieuse. Autrefois, la pauvreté était "
           "surtout liée à l’absence d’emploi ; aujourd’hui, certaines personnes sont pauvres "
           "malgré le travail, c’est-à-dire travaillent sans gagner suffisamment pour vivre "
           "correctement. Cette situation est liée aux faibles salaires, au temps partiel subi et "
           "aux contrats précaires : le travail ne garantit plus automatiquement la sortie de la "
           "pauvreté.",
           "Les plateformes numériques favorisent par ailleurs le retour du travail indépendant. "
           "Chez Uber, les chauffeurs ne sont pas salariés mais indépendants, ce qui permet à "
           "l’entreprise d’éviter les cotisations sociales, certaines protections salariales et "
           "les obligations du droit du travail. Certains considèrent que ces indépendants sont en "
           "réalité des salariés déguisés, parce qu’ils dépendent fortement de la plateforme et "
           "disposent parfois de très peu d’autonomie réelle. Le développement des plateformes "
           "relance donc la question du rapport de force entre entreprises et travailleurs."]},
   ],
   'v': "Si le capitalisme numérique a déjà transformé les conditions d’emploi, l’IA apparaît "
        "aujourd’hui comme une rupture supplémentaire : elle automatise des tâches intellectuelles "
        "jusque-là réservées aux travailleurs qualifiés."},

  # ------------------------------------------------------------------ XIII
  {'t': "XIII. IA et emploi : destruction, transformation ou amélioration ?",
   'sp': [
    {'t': "A. Des investissements massifs… financés par des licenciements",
     'd': ["De grandes entreprises technologiques comme Meta, Amazon ou Apple investissent "
           "massivement dans l’intelligence artificielle. Ces investissements sont extrêmement "
           "coûteux : centres de données, puces électroniques, infrastructures, modèles d’IA, "
           "énergie, recherche.",
           "Pour les financer, certaines entreprises réduisent leurs effectifs, suppriment des "
           "postes et restructurent leurs activités. Même des entreprises très rentables peuvent "
           "donc licencier pour financer leurs investissements technologiques.",
           "La contradiction est apparente plus que réelle : les entreprises de la tech sont en "
           "pleine croissance tout en supprimant des emplois, parce qu’elles cherchent à réduire "
           "leurs coûts, à augmenter leur productivité et à investir dans les nouvelles "
           "technologies. Le progrès technique peut donc créer certains emplois tout en en "
           "détruisant d’autres."]},
    {'t': "B. La distinction décisive : tâches contre métiers",
     'd': ["Les économistes insistent aujourd’hui sur une distinction essentielle : un métier est "
           "composé de plusieurs tâches, et l’IA ne remplace pas toujours un métier entier — elle "
           "remplace surtout certaines tâches.",
           "L’exemple du conseiller bancaire l’illustre bien : il lit des documents, analyse des "
           "dossiers, parle aux clients, conseille, résout des problèmes. L’IA peut automatiser "
           "l’analyse documentaire, mais pas forcément la relation humaine. Le métier est donc "
           "reconfiguré, pas nécessairement supprimé.",
           "Osborne et Frey (2017) estiment qu’environ 47 % des tâches pourraient devenir "
           "automatisables : les entreprises devront donc réorganiser les métiers autour de ces "
           "nouvelles frontières."]},
    {'t': "C. Effet quantitatif et effet qualitatif",
     'd': ["L’effet quantitatif correspond à une baisse du nombre d’emplois. La logique est "
           "simple : si l’IA est plus rapide et moins coûteuse, les entreprises peuvent remplacer "
           "du travail humain par du capital technologique, d’où des suppressions de postes, une "
           "réduction des coûts et une diminution de la masse salariale. Certains métiers risquent "
           "donc de disparaître partiellement ou totalement.",
           "L’effet qualitatif correspond à une transformation du contenu du travail : l’IA "
           "modifie les tâches réalisées, et les métiers deviennent plus techniques, plus "
           "relationnels, plus complexes ou plus spécialisés. Dans l’assurance, l’IA peut lire "
           "rapidement des milliers de pages de documents, ce qui permet au salarié de consacrer "
           "davantage de temps à la relation client. L’IA transforme alors les tâches sans "
           "supprimer l’emploi."]},
    {'t': "D. La rupture historique : l’automatisation cognitive",
     'd': ["Pendant des siècles, le progrès technique remplaçait surtout des tâches physiques — "
           "agriculture, textile, industrie. Aujourd’hui, l’IA remplace des fonctions "
           "intellectuelles : c’est la grande originalité de cette révolution technologique.",
           "Les tâches désormais automatisables sont cognitives et qualifiées, dans des domaines "
           "comme la finance, le droit, la comptabilité, le management ou l’administration. L’IA "
           "touche donc des travailleurs diplômés, ce qui déplace le centre de gravité du débat "
           "sur l’emploi : les craintes ne concernent plus seulement les ouvriers peu qualifiés."]},
    {'t': "E. Le paradoxe de l’augmentation : valorisation puis déclassement",
     'd': ["Des études montrent que des salariés peu qualifiés deviennent plus performants grâce à "
           "l’IA : elle agit comme un assistant, leur permettant de commettre moins d’erreurs et "
           "de réaliser des tâches plus complexes. C’est un effet qualitatif positif, qui valorise "
           "certains travailleurs.",
           "Mais ce même mécanisme produit un risque. Si un salarié peu qualifié aidé par une IA "
           "devient très performant, l’entreprise peut préférer embaucher un salarié moins "
           "diplômé, moins coûteux, utilisant l’IA — ce qui conduit à remplacer des travailleurs "
           "qualifiés. Un bac+2 aidé par une IA pourrait effectuer certaines tâches auparavant "
           "réservées à des bac+5.",
           "Les conséquences possibles sont la réduction de la valeur des diplômes, la "
           "modification des choix d’études et le déclassement — situation où un individu occupe "
           "un emploi inférieur à son niveau de qualification. Autrement dit, l’effet positif sur "
           "les moins qualifiés et l’effet négatif sur les plus qualifiés sont les deux faces du "
           "même mécanisme."],
     'lim': "Certains métiers restent peu automatisables : les métiers techniques, artisanaux, "
            "manuels et relationnels — infirmiers, aides-soignants, plombiers, artisans, métiers "
            "du soin. Ils peuvent être aidés par l’IA mais pas supprimés : c’est la complémentarité "
            "homme-machine."},
    {'t': "F. Conséquences macroéconomiques, taxe sur les robots et rôle de l’État",
     'd': ["L’IA peut conduire à une substitution du capital au travail, donc à réduire la part du "
           "travail dans l’économie. Les conséquences sur les finances publiques sont directes : "
           "si l’emploi diminue, les recettes publiques peuvent baisser — moins d’impôt sur le "
           "revenu, moins de cotisations sociales, moins de consommation donc moins de TVA. Dans "
           "le même temps, les dépenses publiques pourraient augmenter : chômage, aides sociales, "
           "reconversions professionnelles. Le risque est donc une aggravation des déficits "
           "publics.",
           "D’où un nouveau débat fiscal : faut-il taxer les robots ? Certains économistes "
           "proposent de taxer les robots ou l’IA afin de compenser la baisse des cotisations "
           "sociales et la diminution des recettes fiscales liées au travail, en faisant "
           "contribuer les machines au financement de la protection sociale.",
           "Des économistes comme Acemoglu insistent enfin sur le rôle essentiel des pouvoirs "
           "publics : les technologies ne sont pas neutres, et les choix technologiques sont aussi "
           "des choix politiques. L’État doit accompagner les travailleurs, financer la formation, "
           "limiter les inégalités et protéger la cohésion sociale. Les effets de l’IA dépendent "
           "donc aussi des décisions politiques et sociales, non de la seule technique.",
           "Le chapitre se referme sur une ouverture vers Dominique Plihon (Les capitalismes "
           "contemporains, 2025) et sa notion de polycrise : la combinaison de crises financière, "
           "sociale, écologique, démocratique et géopolitique du capitalisme contemporain."]},
   ],
   'v': "La boucle est bouclée : du luddisme de 1811 au débat sur l’IA, la même question revient — "
        "le progrès technique détruit-il l’emploi ou le recompose-t-il ? — et la réponse dépend "
        "chaque fois moins de la technique que des institutions et des politiques qui "
        "l’encadrent."},
 ],

 'ae': [
  {'n': "Joseph Schumpeter", 'k': 'a',
   'i': "Théorie de l’évolution économique (1912) : l’innovation, portée par l’entrepreneur, est "
        "le moteur du capitalisme — cinq formes (DEPOB), destruction créatrice, monopole "
        "temporaire, grappes, cycles longs, puis bureaucratisation."},
  {'n': "Kenneth Pomeranz", 'k': 'a',
   'i': "La grande divergence (2010) : l’Angleterre et le delta du Yangzi sont comparables au "
        "XVIIIᵉ siècle ; c’est l’avantage géologique (charbon proche) et impérial-maritime qui "
        "fait diverger les trajectoires."},
  {'n': "Robert C. Allen", 'k': 'a',
   'i': "Introduction à l’histoire économique mondiale (2014) : salaires élevés et énergie bon "
        "marché rendent la mécanisation économiquement rationnelle en Angleterre — l’argument des "
        "prix relatifs."},
  {'n': "Douglass North", 'k': 'a',
   'i': "Institutions, changements institutionnels et performances économiques : après 1688, "
        "stabilité parlementaire et sécurisation des droits de propriété réduisent l’incertitude "
        "et encouragent l’investissement."},
  {'n': "Daron Acemoglu et James Robinson", 'k': 'a',
   'i': "Why Nations Fail : institutions inclusives contre institutions extractives ; la précocité "
        "anglaise tient moins aux ressources qu’à des institutions favorables à l’innovation."},
  {'n': "Walt Rostow", 'k': 'a',
   'i': "Le take-off : phase où la croissance devient auto-entretenue — située pour la "
        "Grande-Bretagne entre 1783 et 1802, aboutissement des effets d’entraînement "
        "intersectoriels."},
  {'n': "Jacques Brasseul et Nick Crafts", 'k': 'a',
   'i': "Petite histoire des faits économiques (2014) rapporte la thèse du caractère fortuit de la "
        "révolution industrielle anglaise — utile pour nuancer, insuffisante comme explication."},
  {'n': "Nikolaï Kondratiev, Clément Juglar, Joseph Kitchin", 'k': 'a',
   'i': "Trois temporalités emboîtées : 3-5 ans (stocks), 8-10 ans (investissement et crédit), "
        "50-60 ans (grappes d’innovations) — c’est le cycle long que Schumpeter relie à "
        "l’innovation."},
  {'n': "Frederick Winslow Taylor", 'k': 'a',
   'i': "OST : contre la flânerie systématique, chronométrage et one best way, double division "
        "horizontale (parcellisation) et verticale (conception/exécution), salaire différentiel "
        "aux pièces."},
  {'n': "Georges Friedmann", 'k': 'a',
   'i': "Le « travail en miettes » : privé d’un travail qui fasse sens, l’ouvrier devient étranger "
        "à son activité, et la démotivation engendre des coûts qui annulent une partie des gains "
        "de spécialisation."},
  {'n': "Henry Ford", 'k': 'a',
   'i': "Convoyeur, Ford T et doublement du salaire journalier : production de masse et "
        "consommation de masse se tiennent, la hausse salariale servant à la fois de débouché et "
        "d’outil anti-turn-over."},
  {'n': "Max Weber", 'k': 'a',
   'i': "Trois formes de domination — rationnelle-légale, traditionnelle, charismatique : "
        "l’autorité de l’entrepreneur peut reposer sur une aura personnelle, non sur la seule "
        "propriété."},
  {'n': "Anthony Galluzzo", 'k': 'a',
   'i': "Le mythe de l’entrepreneur (2023) : le récit du fondateur génial et solitaire légitime "
        "l’ordre économique en masquant le caractère collectif de l’innovation et le rôle de "
        "l’État."},
  {'n': "Henri Fayol", 'k': 'a',
   'i': "Administration industrielle et générale (1916) : prévoir, organiser, commander, "
        "coordonner, contrôler — la direction devient une science enseignable, distincte de la "
        "propriété du capital."},
  {'n': "Adolf Berle et Gardiner Means", 'k': 'a',
   'i': "The Modern Corporation and Private Property (1932) : la dispersion du capital impose la "
        "séparation propriété/contrôle — ceux qui possèdent ne dirigent plus."},
  {'n': "John Kenneth Galbraith", 'k': 'a',
   'i': "Le Nouvel État industriel (1967) : la technostructure — dirigeants, cadres, ingénieurs, "
        "experts — détient le pouvoir réel parce qu’elle maîtrise l’information."},
  {'n': "Alfred Chandler", 'k': 'a',
   'i': "La main visible des managers (1977) : la coordination par l’organisation interne remplace "
        "partiellement celle du marché ; grandes firmes intégrées, formes U et M."},
  {'n': "Henri Bourguinat", 'k': 'a',
   'i': "Les « 3D » — désintermédiation, décloisonnement, déréglementation — expliquent la "
        "financiarisation des années 1970-1980 et la dépendance des entreprises aux marchés."},
  {'n': "Michael Jensen et William Meckling", 'k': 'a',
   'i': "Theory of the Firm (1976) : relation d’agence entre principal-actionnaire et "
        "agent-manager, marquée par l’incertitude et l’asymétrie d’information, d’où coûts "
        "d’agence et stock-options."},
  {'n': "Milton Friedman", 'k': 'a',
   'i': "The Social Responsibility of Business is to Increase its Profits (1970) : la seule "
        "responsabilité de l’entreprise est de maximiser le profit — fondement normatif du "
        "capitalisme actionnarial."},
  {'n': "Nicholas Bloom", 'k': 'a',
   'i': "Corporations in the Age of Inequality (Harvard Business Review, 2017) : les écarts de "
        "revenus restent constants au sein des entreprises mais croissent entre elles."},
  {'n': "Karl Polanyi", 'k': 'a',
   'i': "La Grande Transformation (1944) : l’encastrement — les relations économiques doivent "
        "s’insérer dans des rapports sociaux et des institutions ; socle théorique de l’approche "
        "par les parties prenantes."},
  {'n': "Pierre Veltz", 'k': 'a',
   'i': "L’économie servicielle : on vend moins le bien que l’accès au service qu’il rend — "
        "Spotify, location automobile, plateformes d’usage."},
  {'n': "Sherry Turkle", 'k': 'a',
   'i': "« Seuls ensemble » : le paradoxe d’une hyperconnexion technique qui coexiste avec un "
        "isolement social accru."},
  {'n': "Bruno Patino", 'k': 'a',
   'i': "La civilisation du poisson rouge : l’économie de l’attention, où le revenu de la "
        "plateforme croît avec le temps d’écran capté et non avec la satisfaction procurée."},
  {'n': "François et Mercier", 'k': 'a',
   'i': "Les trois âges du capitalisme : âge du commerce (marchand), âge de l’usine (ouvrier puis "
        "manager), âge de la finance depuis les années 1980 (actionnaire, intérimaire)."},
  {'n': "Michael Osborne et Carl Frey", 'k': 'a',
   'i': "Estimation (2017) : environ 47 % des tâches pourraient devenir automatisables — à lire "
        "comme une mesure sur les tâches, non sur les métiers entiers."},
  {'n': "Dominique Plihon", 'k': 'a',
   'i': "Les capitalismes contemporains (2025) : la polycrise, combinaison de crises financière, "
        "sociale, écologique, démocratique et géopolitique."},
  {'n': "Le coton : 50 000 heures vers 1750, 135 heures vers 1830", 'k': 'e',
   'i': "Pour produire une livre de coton — l’illustration la plus frappante des gains de "
        "productivité du secteur pionnier de la première industrialisation."},
  {'n': "Charbon multiplié par 250 entre 1750 et 1830", 'k': 'e',
   'i': "Mesure de la sortie du régime des énergies organiques (bois, force humaine et animale, "
        "eau, vent) et de la base énergétique de la première RI."},
  {'n': "Rendements agricoles doublés entre 1700 et 1850", 'k': 'e',
   'i': "Condition du décollage : nourrir des villes croissantes et libérer de la main-d’œuvre, la "
        "population britannique passant de 7 millions en 1780 à 16 millions en 1840."},
  {'n': "Bridgewater Canal (1761) et ligne Liverpool-Manchester (1830)", 'k': 'e',
   'i': "Les deux repères de la révolution des transports : canaux puis rail, d’où baisse des "
        "coûts, élargissement des marchés et intégration du marché national."},
  {'n': "Grande-Bretagne : 2 % de l’industrie mondiale en 1750, 23 % en 1880", 'k': 'e',
   'i': "Avec environ 2 % de la population mondiale — mesure de l’hégémonie, bientôt contestée par "
        "l’Allemagne et les États-Unis."},
  {'n': "L’automobile comme grappe d’innovations", 'k': 'e',
   'i': "Débouchés, énergie, procédé, organisation, biens induits : elle entraîne aussi la "
        "signalisation (1902, Genève 1909, sens interdit 1928) et le salon de l’automobile (1889, "
        "succès en 1902)."},
  {'n': "Ford T : 690 $ en 1913, 290 $ en 1929", 'k': 'e',
   'i': "Effet des économies d’échelle sur le coût moyen et le prix de vente ; dès 1914, 60 % des "
        "voitures produites aux États-Unis sont des Ford."},
  {'n': "Salaire Ford porté de 2,5 à 5 dollars par jour", 'k': 'e',
   'i': "Double justification : créer des consommateurs, et augmenter le coût d’opportunité du "
        "départ pour fixer une main-d’œuvre usée par les cadences."},
  {'n': "Les cinq zéros du Toyota Production System", 'k': 'e',
   'i': "Zéro stock, délai, panne, défaut, papier : traduction opérationnelle du juste-à-temps, où "
        "l’aval commande l’amont — l’inverse du fordisme."},
  {'n': "Peugeot, Hermès", 'k': 'e',
   'i': "Le capitalisme entrepreneurial est souvent familial : le nom de l’entreprise est celui de "
        "la dynastie fondatrice, et propriété et contrôle restent confondus."},
  {'n': "Enron (2001) et Volkswagen", 'k': 'e',
   'i': "Les deux dérives emblématiques : manipulations comptables du capitalisme actionnarial "
        "d’un côté, greenwashing et falsification des émissions de l’autre."},
  {'n': "Loi PACTE (2019)", 'k': 'e',
   'i': "Introduit la « raison d’être » et le statut d’entreprise à mission : juridiquement, "
        "l’entreprise peut poursuivre des objectifs autres que le profit."},
  {'n': "Uber", 'k': 'e',
   'i': "Ne possède quasiment pas de véhicules mais coordonne des centaines de milliers de "
        "chauffeurs : externalisation des facteurs, commission captée, et débat sur le salariat "
        "déguisé."},
  {'n': "Les luddites (1811-1816)", 'k': 'e',
   'i': "Destruction de machines textiles en Angleterre : la matrice historique de toutes les "
        "peurs technologiques, y compris celle de l’IA aujourd’hui."},
  {'n': "Loi de 1898 sur les accidents du travail", 'k': 'e',
   'i': "Bascule de la responsabilité du salarié vers l’employeur : point de départ de la "
        "construction des protections attachées au salariat."},
  {'n': "France : 73 % de CDI, 27 % de CDD, 13,5 % d’indépendants", 'k': 'e',
   'i': "Le salariat reste dominant (≈ 86 % des actifs occupés) avec une ancienneté moyenne "
        "d’environ 11 ans, mais les formes précaires progressent depuis 1973."},
 ],

 'arg': [
  "La révolution industrielle n’est pas un choc technique mais un processus cumulatif et "
  "circulaire : la machine à vapeur de 1769 ne suffit pas, il faut l’articulation agriculture – "
  "démographie – science – médecine – charbon – transports – usine.",
  "La précocité anglaise ne s’explique par aucune cause unique : géographie et empire "
  "(Pomeranz), prix relatifs (Allen), institutions (North, Acemoglu et Robinson) se combinent, "
  "et la thèse du hasard de Crafts ne suffit pas.",
  "L’industrialisation recompose le travail plus qu’elle ne le détruit : la machine crée de "
  "nouveaux besoins (extraction, manutention, infrastructures) — argument transposable au débat "
  "sur l’IA.",
  "La transition organisationnelle est longue : domestic system, ateliers et usines coexistent "
  "pendant des décennies, le factory system ne s’imposant que vers 1870.",
  "Chez Schumpeter, le capitalisme ne doit pas être jugé sur son équilibre mais sur sa capacité "
  "de transformation : l’innovation, et non la concurrence par les prix, en est le moteur.",
  "Le monopole temporaire peut être plus favorable à l’innovation que la concurrence parfaite, "
  "car la rente d’innovation rémunère le risque et l’investissement — mais il doit rester "
  "temporaire.",
  "Les limites sociales d’une organisation deviennent ses limites économiques : perte de sens → "
  "démotivation → erreurs et turn-over → coûts → baisse de productivité (Taylor critiqué par "
  "Friedmann, corrigé par Ford puis Toyota).",
  "Chaque modèle d’organisation corrige le précédent et crée ses propres rigidités : le fordisme "
  "répond au turn-over taylorien, le toyotisme à la rigidité fordiste, mais le flux tendu "
  "fragilise face aux perturbations.",
  "Le pouvoir dans l’entreprise se déplace en trois temps — entrepreneur, managers, actionnaires "
  "— et chaque déplacement change la finalité poursuivie : survie et innovation, croissance et "
  "planification, valeur actionnariale.",
  "Le pouvoir managérial repose sur l’information et la compétence, non sur la propriété "
  "(Galbraith) ; la coordination interne peut être plus efficiente que le marché (Chandler).",
  "La théorie de l’agence est une réponse à un problème réel (asymétrie d’information) dont le "
  "remède produit ses propres effets pervers : stock-options, court-termisme et creusement des "
  "écarts de revenus entre entreprises (Bloom).",
  "Le capitalisme numérique ne supprime pas les piliers du capitalisme : l’économie du partage "
  "étend la logique marchande à de nouveaux usages, et la gratuité déplace le prix vers la "
  "publicité et les données.",
  "Le numérique n’est pas dématérialisé : centres de données, câbles, antennes, énergie et eau en "
  "font un système profondément matériel, dont le coût écologique est invisibilisé.",
  "L’IA remplace des tâches plus que des métiers (Osborne et Frey : ≈ 47 % des tâches), ce qui "
  "déplace l’analyse de la destruction d’emplois vers la reconfiguration des métiers.",
  "L’IA constitue une rupture historique parce qu’elle automatise des fonctions cognitives "
  "qualifiées, donc touche pour la première fois massivement les diplômés.",
  "Les effets de l’IA ne sont pas déterminés par la technique : les technologies ne sont pas "
  "neutres (Acemoglu), et dépendent des choix politiques de formation, de fiscalité et de "
  "protection sociale.",
 ],

 'deb': [
  "« Révolution » ou évolution ? Le mot suggère une rupture brutale alors que l’industrialisation "
  "est progressive, sectorielle et cumulative — débat historiographique fondateur du chapitre.",
  "L’agriculture précède-t-elle l’industrie ? Thèse classique (surplus agricole, exode rural) "
  "contre thèse inverse (l’industrie modernise l’agriculture par machines, acier et engrais) : la "
  "bonne réponse est circulaire.",
  "Trois ou quatre révolutions industrielles ? Le découpage dépend de la décision de séparer ou "
  "non le numérique et l’IA — question de périodisation, pas seulement de vocabulaire.",
  "Facteurs structurels ou hasard ? Pomeranz, Allen, North et Acemoglu contre la thèse du "
  "caractère fortuit rapportée par Brasseul à propos de Crafts.",
  "Concurrence parfaite ou monopole temporaire ? Les marginalistes contre Schumpeter : quelle "
  "structure de marché favorise réellement l’innovation ?",
  "Marx et Schumpeter annoncent tous deux la fin du capitalisme — par la lutte des classes pour "
  "l’un, par la bureaucratisation qui étouffe l’entrepreneur pour l’autre. Le capitalisme est-il "
  "miné par ses contradictions ou par son succès ?",
  "Le toyotisme est-il une rupture ou un prolongement du taylorisme ? Il conserve le chronométrage "
  "et la recherche de productivité, mais substitue la qualité à la quantité et rend l’opérateur "
  "acteur.",
  "Qu’est-ce qu’une bonne gouvernance d’entreprise ? Entrepreneur innovateur, manager planificateur "
  "ou actionnaire disciplinant : trois réponses, trois finalités, trois séries de limites.",
  "Shareholder ou stakeholder ? Friedman (le profit comme seule responsabilité) contre l’approche "
  "par les parties prenantes adossée à Polanyi (l’économie encastrée).",
  "La RSE est-elle une transformation réelle ou un discours ? Loi PACTE et raison d’être d’un côté, "
  "greenwashing et Volkswagen de l’autre.",
  "Le capitalisme numérique est-il rupture ou continuité ? Rupture par la vitesse, la puissance de "
  "calcul et l’IA ; continuité par la concentration, l’extension marchande et la logique "
  "d’accumulation.",
  "Existe-t-il un capitalisme ou des capitalismes ? Pluralité historique (École de la régulation, "
  "François et Mercier) et géographique (États-Unis contre France, Mexique contre Venezuela).",
  "L’IA détruit-elle ou transforme-t-elle l’emploi ? Effet quantitatif (substitution capital/"
  "travail) contre effet qualitatif (complémentarité, augmentation des capacités), le débat "
  "restant explicitement ouvert.",
  "L’IA favorise-t-elle ou déclasse-t-elle les qualifiés ? Elle rend les peu qualifiés plus "
  "performants, ce qui peut précisément conduire à substituer un bac+2 assisté à un bac+5.",
  "Faut-il taxer les robots ? Argument du financement de la protection sociale face à l’érosion "
  "des cotisations, contre le risque de pénaliser l’investissement productif.",
 ],

 'lien': [
  {'c': 6, 'p': "La croissance, la comptabilité de la croissance, le progrès technique, la "
                "destruction créatrice, la croissance endogène et les institutions y sont traités "
                "sous l’angle macroéconomique : ce chapitre en donne le contenu historique, "
                "organisationnel et microéconomique."},
  {'c': 9, 'p': "La taille des firmes, les économies d’échelle, l’intégration verticale et "
                "horizontale, les brevets, les positions dominantes et les stratégies "
                "oligopolistiques prolongent directement Chandler, Schumpeter et le capitalisme "
                "de plateforme."},
  {'c': 10, 'p': "La sociologie des organisations et du travail reprend taylorisme, fordisme, "
                 "toyotisme, autonomie, aliénation et rapports de pouvoir dans l’entreprise avec "
                 "les outils de la sociologie."},
  {'c': 7, 'p': "Rostow, Gerschenkron, Allen sur l’Inde, les institutions d’Acemoglu et la "
                "soutenabilité y sont mobilisés pour penser le rattrapage des pays en "
                "développement et les stratégies d’industrialisation."},
  {'c': 5, 'p': "Externalités, biens non rivaux, brevets, concurrence imparfaite et défaillances "
                "de marché fondent théoriquement le monopole temporaire schumpétérien et la "
                "régulation des plateformes."},
  {'c': 2, 'p': "Financiarisation, marchés financiers, 3D de Bourguinat, désintermédiation et rôle "
                "des investisseurs institutionnels y reçoivent leur traitement complet, ici "
                "appliqué à la gouvernance d’entreprise."},
  {'c': 3, 'p': "Classiques, marginalistes, Marx, Keynes et Schumpeter y sont présentés comme "
                "courants : ce chapitre met en œuvre la rupture schumpétérienne avec l’équilibre "
                "néoclassique."},
  {'c': 1, 'p': "Salariat, revenus primaires, consommation de masse, pauvreté et seuils de "
                "pauvreté éclairent le compromis fordiste comme la pauvreté laborieuse "
                "contemporaine."},
 ],

 'min': [
  "La révolution industrielle = processus long, progressif, multidimensionnel et cumulatif ; pas "
  "la seule machine à vapeur de Watt (1769). Boucle : agriculture → démographie → marchés → "
  "industrie → agriculture et équipements.",
  "Trois RI : 1760-1820/1880 (GB, charbon, textile et sidérurgie) ; à partir de 1880 (États-Unis "
  "et Allemagne, électricité et pétrole, production de masse) ; depuis les années 1970 "
  "(microprocesseur 1971, Internet, plateformes, IA).",
  "Coton pionnier : Hargreaves 1764, Arkwright 1769, Crompton 1779, Cartwright 1785 ; une livre "
  "de coton passe de ≈ 50 000 heures (1750) à ≈ 135 heures (1830).",
  "Rendement = production / surface ; productivité = production / facteurs. Rendements doublés "
  "1700-1850 ; enclosures = efficacité contre coût social ; charbon ×250 entre 1750 et 1830.",
  "Précocité anglaise : Pomeranz (charbon et empire contre le Yangzi), Allen (salaires élevés + "
  "énergie bon marché), North (1688), Acemoglu-Robinson (institutions inclusives), take-off de "
  "Rostow 1783-1802 ; 2 % → 23 % de l’industrie mondiale (1750 → 1880).",
  "Schumpeter, trois ruptures : dynamique contre équilibre ; monopole temporaire contre CPP ; le "
  "capitalisme miné par son succès (oligopoles contre entrepreneurs).",
  "Cinq formes d’innovation (DEPOB) ; destruction créatrice ; innovation fondamentale ouvre un "
  "cycle, incrémentale le prolonge ; Kitchin 3-5 ans, Juglar 8-10 ans, Kondratiev 50-60 ans "
  "(grappes).",
  "Taylorisme : flânerie systématique, OST et one best way, division horizontale (parcellisation) "
  "et verticale (conception/exécution), salaire aux pièces ; limite = « travail en miettes » "
  "(Friedmann) et coûts du turn-over.",
  "Fordisme : convoyeur + Ford T + 5 $/jour (contre 2,5) ; économies d’échelle, Ford T de 690 $ "
  "(1913) à 290 $ (1929) ; production de masse ⇄ consommation de masse ; limite = rigidité.",
  "Toyotisme : juste-à-temps (l’aval commande l’amont), cinq zéros, qualité totale, autonomation, "
  "kaizen ; limite = intensification et vulnérabilité des flux tendus.",
  "Qui dirige ? Entrepreneur (propriété = contrôle ; Weber, Schumpeter, critiqué par Galluzzo "
  "2023) → managers (Fayol 1916, Berle et Means 1932, Galbraith 1967, Chandler 1977, formes U et "
  "M) → actionnaires (Bourguinat 3D, Jensen et Meckling 1976, Friedman 1970).",
  "Limites actionnariales : court-termisme, Enron 2001, inégalités (Bloom 2017) → parties "
  "prenantes et encastrement (Polanyi 1944), RSE et loi PACTE 2019, mais greenwashing "
  "(Volkswagen).",
  "Capitalisme numérique : données (« la nouvelle électricité »), plateformes, IA probabiliste "
  "(elle calcule, ne pense pas) ; opportunités = économie du partage et économie servicielle "
  "(Veltz).",
  "Quatre menaces : économiques (effets de réseau, GAFAM/BATX), sociales (ubérisation, Turkle "
  "« seuls ensemble », Patino et l’économie de l’attention), politiques (surveillance), "
  "écologiques (mythe de la dématérialisation).",
  "Capitalisme pluriel : École de la régulation (concurrentiel / monopolistique) ; François et "
  "Mercier (commerce, usine, finance) ; modèles nationaux (États-Unis / France) et émergents "
  "(Mexique / Venezuela). Les quatre piliers sont déplacés, non supprimés.",
  "Travail ≠ emploi. France : ≈ 86 % de salariés, 13,5 % d’indépendants, 73 % de CDI (ancienneté "
  "≈ 11 ans) contre 27 % de CDD (≤ 18 mois) ; 35 h ; temps partiel subi, pauvreté laborieuse "
  "depuis 1973, salariat déguisé des plateformes.",
  "IA : remplace des tâches plus que des métiers (Osborne et Frey ≈ 47 %) ; effet quantitatif "
  "contre effet qualitatif ; rupture = automatisation cognitive des diplômés ; risque de "
  "déclassement ; métiers du soin peu automatisables ; débat sur la taxe robots ; Acemoglu : les "
  "technologies ne sont pas neutres ; Plihon 2025 : polycrise.",
 ],
}}
