# -*- coding: utf-8 -*-
"""Chapitre 8 — Révolutions industrielles, entreprise, innovation et travail."""

SP = {
 'c8-01': 'La révolution industrielle : un processus long, les trois révolutions',
 'c8-02': 'Révolution agricole, enclosures, démographie, science et médecine',
 'c8-03': 'Charbon, transports et intégration des marchés',
 'c8-04': 'La précocité anglaise : Pomeranz, Allen, North, Acemoglu',
 'c8-05': 'Schumpeter : la dynamique, les cinq formes d’innovation',
 'c8-06': 'Grappes d’innovations, monopole temporaire et cycles Kitchin-Juglar-Kondratiev',
 'c8-07': 'Les limites du capitalisme schumpétérien ; le taylorisme',
 'c8-08': 'Le fordisme : chaîne, standardisation, économies d’échelle, hauts salaires',
 'c8-09': 'Le toyotisme : juste-à-temps, cinq zéros, autonomation, kaizen',
 'c8-10': 'Le capitalisme entrepreneurial : propriété et pouvoir confondus',
 'c8-11': 'Le capitalisme managérial : Fayol, Berle et Means, Galbraith, Chandler',
 'c8-12': 'Le capitalisme actionnarial : théorie de l’agence, Friedman, financiarisation',
 'c8-13': 'Limites du modèle actionnarial : parties prenantes, Polanyi, RSE',
 'c8-14': 'Le capitalisme numérique : données, plateformes, attention, surveillance',
 'c8-15': 'Un capitalisme pluriel : trois âges, diversité nationale, quatre fondements',
 'c8-16': 'Travail et emploi : salarisation, protections, ludisme',
 'c8-17': 'Formes d’emploi, précarisation et retour du travail indépendant',
 'c8-18': 'IA et emploi : tâches, qualifications, finances publiques, rôle de l’État',
}

# Question écartée : ch8-vf-14 porte sur la navette volante de Kay, qui
# n'apparaît dans aucun cours — le cours ne retient que Hargreaves, Arkwright,
# Crompton, Cartwright et Roberts.
DROP = ['ch8-vf-14']


def f(**kw):
    return kw


FIX = {

# ------------------------------------------- c8-01 nature et périodisation
'ch8-qcm-15': f(niv='comprendre', sp='c8-01', b=46,
 exp="Le mot « révolution » suggère une rupture brutale, un avant / après très "
     "net. Or les historiens insistent sur le caractère progressif, sectoriel, "
     "étalé sur plusieurs décennies et non linéaire de l’industrialisation "
     "anglaise, faite d’enchaînements cumulatifs.",
 why=["Le terme s’applique couramment à des transformations économiques : ce "
      "n’est pas une réserve de vocabulaire.",
      "L’industrialisation a au contraire profondément transformé la société "
      "britannique : c’est la rapidité, non l’ampleur, qui est discutée.",
      "La France est un pays suiveur dans cette chronologie, non un contre-"
      "exemple."],
 diss="Formule à retenir : la révolution industrielle n’est pas un choc "
      "technique ponctuel mais un processus long, progressif, cumulatif et "
      "systémique."),
'ch8-qcm-1': f(niv='connaitre', sp='c8-01', b=55,
 exp="Les historiens qualifient la révolution industrielle de processus "
     "historique long, progressif, multidimensionnel et cumulatif. Elle "
     "articule révolution agricole, croissance démographique, développement de "
     "la science, progrès de la médecine, révolution des transports, "
     "mécanisation et transformation de l’organisation du travail.",
 why=["La rupture brutale est précisément la lecture que l’historiographie "
      "récuse.",
      "Réduire le phénomène à la machine à vapeur est le contresens le plus "
      "fréquent du chapitre.",
      "Le textile est le secteur pionnier, non le seul secteur concerné."]),
'ch8-qcm-12': f(niv='comprendre', sp='c8-01', b=73,
 exp="L’industrialisation repose sur des causalités croisées et cumulatives "
     "entre agriculture, démographie, science, médecine, transports et "
     "industrie. Elle ne suit pas une chaîne simple mais un cercle cumulatif, "
     "sans point de départ unique.",
 why=["Les innovations technologiques comptent, mais le cours refuse "
      "explicitement de les ériger en cause unique.",
      "Les décisions gouvernementales interviennent — rôle du Parlement, "
      "enclosures — sans que le processus soit politique par nature.",
      "La linéarité est précisément ce que le cours rejette : le processus "
      "est non linéaire et sectoriel."]),
'ch8-qcm-14': f(niv='comprendre', sp='c8-01', b=72,
 exp="La logique est circulaire : la hausse des rendements agricoles améliore "
     "l’alimentation, ce qui soutient la croissance démographique, qui élargit "
     "la demande et la main-d’œuvre, ce qui nourrit l’urbanisation et "
     "l’industrialisation, qui développe à son tour transports et innovations, "
     "lesquels modernisent l’agriculture. Aucun élément n’est le point de "
     "départ absolu.",
 why=["Une innovation n’en déclenche pas une seule : les effets se diffusent "
      "dans plusieurs directions.",
      "Les crises cycliques relèvent de l’analyse schumpétérienne des cycles, "
      "plus loin dans le chapitre.",
      "Aucune planification étatique n’est à l’œuvre dans l’Angleterre du "
      "XVIIIᵉ siècle."]),
'ch8-qcm-32': f(niv='comprendre', sp='c8-01', b=15,
 exp="La révolution industrielle est qualifiée de mutation systémique parce "
     "qu’elle transforme l’ensemble du régime de production : urbanisation, "
     "essor du salariat, mécanisation, concentration productive, "
     "transformation des rapports sociaux. Elle ne se réduit donc pas à "
     "quelques techniques nouvelles.",
 why=["La transformation dépasse largement le système technique.",
      "Aucune coordination gouvernementale d’ensemble n’organise le "
      "processus.",
      "L’agriculture est au contraire l’un des premiers domaines transformés, "
      "avant et avec l’industrie."]),
'ch8-vf-15': f(niv='connaitre', sp='c8-01', b=15,
 exp="C’est la formulation même du cours : la révolution industrielle "
     "transforme l’ensemble du régime de production — urbanisation, salariat, "
     "mécanisation, concentration, rapports sociaux — et non seulement "
     "quelques techniques."),
'ch8-qcm-4': f(niv='connaitre', sp='c8-01', b=78,
 exp="La première révolution industrielle couvre environ 1760-1820, parfois "
     "prolongée jusqu’en 1880. Pays leader : la Grande-Bretagne, puis la "
     "France. Énergie dominante : le charbon. Secteurs moteurs : textile, "
     "sidérurgie et machine à vapeur.",
 why=["1650-1750 est antérieur au décollage : c’est la période de la "
      "révolution agricole anglaise.",
      "1820-1880 correspond à la diffusion et au prolongement, non au point "
      "de départ.",
      "1880-1945 correspond à la deuxième révolution industrielle."]),
'ch8-qcm-2': f(niv='connaitre', sp='c8-01', b=86,
 exp="James Watt dépose le brevet de la machine à vapeur en 1769, la même "
     "année que la Water Frame d’Arkwright. Le cours rappelle aussitôt que "
     "cette date est un symbole, non la cause de l’industrialisation : elle "
     "n’a de portée que replacée dans l’ensemble des transformations.",
 why=["1733 ne correspond à aucun repère du cours.",
      "1789 est la Révolution française, sans rapport.",
      "1825 est la date du perfectionnement mécanique de Roberts dans le "
      "textile."]),
'ch8-vf-6': f(niv='connaitre', sp='c8-01', b=86,
 exp="Watt dépose son brevet en 1769. Le cours en fait le repère clé de la "
     "première révolution industrielle, tout en avertissant que "
     "l’historiographie classique a eu tort d’y voir l’explication du "
     "décollage britannique."),
'ch8-vf-1': f(niv='comprendre', sp='c8-01', b=5,
 exp="C’est précisément la lecture réductrice que le cours écarte. "
     "L’historiographie classique a longtemps mis en avant quelques "
     "inventions symboliques, mais l’industrialisation résulte de "
     "l’articulation de plusieurs transformations : révolution agricole, "
     "croissance démographique, science, médecine, transports, mécanisation, "
     "organisation du travail et factory system."),
'ch8-vf-7': f(niv='comprendre', sp='c8-01', b=71,
 exp="Le cours insiste sur une logique cumulative et circulaire : "
     "agriculture, démographie, science, médecine, transports et industrie se "
     "renforcent mutuellement dans un processus d’auto-entraînement. Il ne "
     "faut pas raisonner en chaîne simple."),
'ch8-qcm-35': f(niv='comprendre', sp='c8-01', b=122,
 exp="L’histoire économique montre des vagues successives d’innovations : "
     "charbon et textile pour la première, électricité, pétrole, automobile et "
     "chimie pour la deuxième, informatique, plateformes et IA pour la "
     "troisième. Le cours précise que ce découpage est discutable mais utile : "
     "il permet de penser des vagues technologiques qui reconfigurent "
     "périodiquement les structures productives.",
 why=["Il ne s’agit pas de révolutions politiques.",
      "Le décalage chronologique entre pays est réel, mais ce n’est pas ce "
      "que désigne la succession des révolutions industrielles.",
      "Le désaccord porte sur le nombre de révolutions, non sur la définition "
      "même du concept."]),
'ch8-vf-9': f(niv='comprendre', sp='c8-01', b=119,
 exp="Le découpage fait débat : certains comptent trois révolutions "
     "industrielles, d’autres quatre en distinguant le numérique de "
     "l’intelligence artificielle. Le cours présente la révolution "
     "informatique comme commençant dans les années 1970, avec le "
     "microprocesseur en 1971, l’informatique personnelle, Internet dans les "
     "années 1990, les plateformes dans les années 2000, l’IA et le big data "
     "dans les années 2010-2020."),
'ch8-qcm-3': f(niv='connaitre', sp='c8-01', b=127,
 exp="Le textile cotonnier est le secteur pionnier, et non la machine à "
     "vapeur. Le coton bénéficie d’une forte demande, d’un approvisionnement "
     "colonial, d’innovations techniques rapides et d’un fort potentiel de "
     "gains de productivité. Le cours ajoute : pionnier n’est pas exclusif — "
     "fer, métallurgie et construction navale évoluent aussi.",
 why=["La sidérurgie est un secteur moteur, mais elle suit le textile.",
      "La chimie est un secteur de la deuxième révolution industrielle.",
      "La construction navale évolue en parallèle, sans jouer le rôle "
      "pionnier."]),
'ch8-vf-2': f(niv='connaitre', sp='c8-01', b=140,
 exp="Le textile cotonnier est bien le secteur pionnier de la première "
     "industrialisation britannique, sans résumer à lui seul l’ensemble du "
     "processus : le cours insiste sur la formule « pionnier, pas exclusif »."),
'ch8-qcm-13': f(niv='comprendre', sp='c8-01', b=129,
 exp="Quatre raisons sont données : une forte demande, un approvisionnement "
     "colonial, des innovations techniques rapides et un fort potentiel de "
     "gains de productivité. Le coton devient ainsi le laboratoire de la "
     "mécanisation britannique.",
 why=["Le coton n’est pas une ressource britannique : il est précisément "
      "importé des colonies.",
      "La mécanisation du filage et du tissage exige au contraire des "
      "investissements importants en capital fixe.",
      "Le coton est un produit nouveau dans l’économie britannique du "
      "XVIIIᵉ siècle, et non une spécialité médiévale."]),
'ch8-qcm-18': f(niv='connaitre', sp='c8-01', b=144,
 exp="La Spinning Jenny de James Hargreaves (1764) est une machine à filer "
     "permettant de travailler plusieurs bobines simultanément. Elle ouvre la "
     "série des innovations textiles que le cours demande de connaître : Water "
     "Frame d’Arkwright (1769), Mule de Crompton (1779), Power Loom de "
     "Cartwright (1785), perfectionnement de Roberts (1825).",
 why=["La machine à tisser mécanisée est le Power Loom de Cartwright, en "
      "1785.",
      "Les locomotives relèvent de la révolution des transports.",
      "Aucune machine d’égrenage ne figure dans le cours."]),
'ch8-vf-10': f(niv='connaitre', sp='c8-01', b=144,
 exp="La Spinning Jenny est une machine à filer, non à tisser : elle permet "
     "de filer plusieurs bobines à la fois. La machine à tisser de la série "
     "est le Power Loom de Cartwright (1785)."),
'ch8-qcm-17': f(niv='connaitre', sp='c8-01', b=149,
 q="Quel gain de productivité le cours retient-il dans le textile cotonnier "
   "britannique ?",
 opts=["Le temps nécessaire pour produire une livre de coton passe d’environ "
       "500 à 135 heures entre 1750 et 1830",
       "Il passe d’environ 50 000 heures à 135 heures entre 1750 et 1830",
       "Il est divisé par deux entre 1750 et 1830",
       "Il passe de 1 000 à 100 heures entre 1800 et 1850"],
 ans=1,
 why=["Le point de départ est très largement sous-estimé.",
      "Une division par deux ne rendrait pas compte du caractère « colossal » "
      "du gain souligné par le cours.",
      "Ni les dates ni les ordres de grandeur ne correspondent."],
 exp="Pour produire une livre de coton, il fallait environ 50 000 heures vers "
     "1750 contre environ 135 heures vers 1830 : le cours qualifie ce gain de "
     "colossal. Il résulte de la succession Hargreaves, Arkwright, Crompton, "
     "Cartwright, Roberts.",
 diss="Ce chiffre est le plus frappant du chapitre : il permet de montrer "
      "concrètement ce que signifie « gains de productivité » dans la "
      "première industrialisation."),
'ch8-qcm-24': f(niv='comprendre', sp='c8-01', b=156,
 q="Comment le cours décrit-il l’effet de la mécanisation sur le travail "
   "humain au XIXᵉ siècle ?",
 opts=["La machine remplace brutalement les hommes dans tous les secteurs",
       "La machine recompose le travail plus qu’elle ne l’élimine : elle "
       "mécanise certaines tâches mais crée aussi de nouveaux besoins "
       "d’extraction, de manutention, d’infrastructures et de transport",
       "La mécanisation n’a aucun effet sur l’emploi",
       "La mécanisation ne concerne que l’agriculture"],
 ans=1,
 why=["C’est le contresens que le cours signale explicitement comme le plus "
      "fréquent.",
      "Les effets sont au contraire considérables, mais ils transforment "
      "plutôt qu’ils ne suppriment.",
      "La mécanisation commence dans le textile, non dans l’agriculture."],
 exp="L’industrialisation transforme, redistribue et recompose les tâches "
     "plus qu’elle ne supprime immédiatement l’emploi. Le cours ajoute que "
     "cette progressivité se retrouve dans les formes d’organisation : "
     "domestic system, petits ateliers et usines coexistent pendant plusieurs "
     "décennies.",
 diss="Ce raisonnement est directement transposable au débat contemporain sur "
      "l’intelligence artificielle, que le chapitre aborde en fin de "
      "parcours."),
'ch8-qcm-9': f(niv='connaitre', sp='c8-02', b=188,
 exp="Le factory system désigne la concentration des ouvriers dans un même "
     "lieu de production, avec des machines plus puissantes, un contrôle du "
     "temps de travail, une supervision hiérarchique, une division des tâches "
     "et une production intensive. Il s’oppose à la dispersion du domestic "
     "system.",
 why=["L’atelier familial relève de la production artisanale antérieure.",
      "La production à domicile est le domestic system, que le factory system "
      "vient remplacer.",
      "Les manufactures royales appartiennent à une période et à une logique "
      "antérieures."]),
'ch8-vf-17': f(niv='connaitre', sp='c8-02', b=186,
 exp="Le factory system est bien une innovation organisationnelle : il "
     "concentre les ouvriers dans un même lieu et entraîne la séparation du "
     "lieu de vie et du lieu de travail, la montée du salariat industriel, la "
     "discipline du temps, une hiérarchie plus forte, une coordination "
     "centralisée et une hausse de la productivité."),
'ch8-qcm-10': f(niv='connaitre', sp='c8-02', b=176,
 q="Qu’est-ce que le domestic system ?",
 opts=["Un système de production industrielle en usine",
       "Un système de production à domicile, souvent par des paysans-ouvriers, "
       "les matières premières étant fournies par un marchand",
       "Un système d’exportation de produits industriels",
       "Un mode d’organisation fondé sur la division du travail en usine"],
 ans=1,
 why=["L’usine correspond au factory system, qui s’y oppose.",
      "Il ne s’agit pas d’un dispositif commercial international.",
      "La division du travail en usine caractérise le factory system puis le "
      "taylorisme."],
 exp="Le domestic system est une forme de proto-industrialisation : travail "
     "rural intégré à un réseau marchand, production à domicile, matières "
     "premières fournies par un marchand. Le cours insiste sur le fait qu’il "
     "coexiste longtemps avec les premières manufactures et usines, pendant "
     "une large partie de la première moitié du XIXᵉ siècle.",
 diss="Le passage du domestic system au factory system marque le passage "
      "d’une proto-industrie dispersée à l’entreprise industrielle moderne."),
'ch8-vf-4': f(niv='connaitre', sp='c8-02', b=176,
 q="Le domestic system est un système de production en usine centralisée.",
 ans=False,
 exp="C’est l’inverse : le domestic system est un système de production à "
     "domicile, où des paysans-ouvriers travaillent pour un marchand qui "
     "fournit les matières premières. L’usine centralisée correspond au "
     "factory system, qui s’impose véritablement vers 1870."),
'ch8-open-1': f(niv='comprendre', sp='c8-01', b=45,
 q="Le terme de « révolution » est-il adapté pour décrire l’industrialisation "
   "britannique ?",
 ans={'modele': "Le terme est utile mais discuté. Il est utile parce que "
      "l’industrialisation transforme l’ensemble du système productif : "
      "passage d’une économie agricole à une économie industrielle, "
      "urbanisation, essor du salariat, mécanisation, concentration "
      "productive, transformation des rapports sociaux. Il est discuté parce "
      "que le mot suggère une rupture brutale, un avant / après très net, "
      "alors que l’industrialisation anglaise est progressive, sectorielle, "
      "étalée sur plusieurs décennies, non linéaire et faite d’enchaînements "
      "cumulatifs. La bonne formulation est donc celle d’une mutation "
      "systémique et cumulative plutôt que d’un choc technique ponctuel.",
      'cles': [{'f': ['systemique', 'ensemble', 'regime de production', 'rapports sociaux'],
                'l': 'utile : la transformation est systémique'},
               {'f': ['brutale', 'rupture', 'soudain'],
                'l': 'discuté : le mot suggère une rupture brutale'},
               {'f': ['progressif', 'decennies', 'non lineaire', 'cumulatif'],
                'l': 'or le processus est progressif et cumulatif'}]},
 exp="C’est l’un des pièges les plus fréquents du chapitre : affirmer que "
     "l’industrialisation fut un « basculement radical et rapide » contredit "
     "directement l’analyse du cours."),
'ch8-open-2': f(niv='connaitre', sp='c8-01', b=81,
 ans={'modele': "Les trois secteurs moteurs de la première révolution "
      "industrielle sont le textile — le coton en particulier, secteur "
      "pionnier —, la sidérurgie et l’acier, et la machine à vapeur, "
      "alimentée par le charbon. Le cours précise que le coton est pionnier "
      "mais pas exclusif : le fer, la métallurgie et la construction navale "
      "évoluent aussi.",
      'cles': [{'f': ['textile', 'coton'], 'l': 'le textile cotonnier'},
               {'f': ['siderurgie', 'acier', 'fer', 'metallurgie'],
                'l': 'la sidérurgie et l’acier'},
               {'f': ['vapeur', 'charbon', 'energie'],
                'l': 'la machine à vapeur et le charbon'}]},
 exp="Pour la deuxième révolution industrielle, la liste change "
     "complètement : automobile, chimie, électroménager et "
     "télécommunications, avec l’électricité et le pétrole pour énergies."),
'ch8-open-4': f(niv='comprendre', sp='c8-01', b=663,
 q="Quelle place faut-il accorder à la machine à vapeur de Watt dans "
   "l’explication de l’industrialisation ?",
 ans={'modele': "La machine à vapeur, brevetée par Watt en 1769, est le "
      "repère clé et le symbole de la première révolution industrielle : elle "
      "fournit une énergie plus puissante et plus régulière, alimentée par le "
      "charbon, adaptée à la mécanisation, et elle soutient la sidérurgie "
      "comme la métallurgie. Mais le cours avertit que l’historiographie "
      "classique a eu tort d’en faire l’explication du décollage : "
      "l’industrialisation ne s’explique pas par une seule invention. Elle "
      "suppose des capitaux, des transports, des marchés, des institutions, "
      "des ressources énergétiques et une main-d’œuvre disponible. Science et "
      "industrie se renforcent mutuellement.",
      'cles': [{'f': ['energie', 'puissante', 'charbon', 'mecanisation'],
                'l': 'une énergie puissante et régulière, adossée au charbon'},
               {'f': ['symbole', 'repere', '1769'],
                'l': 'un repère et un symbole : 1769'},
               {'f': ['pas une seule', 'reducteur', 'multidimensionnel', 'combinaison'],
                'l': 'mais pas une explication suffisante à elle seule'}]},
 exp="Savoir à la fois citer la date et refuser l’explication monocausale est "
     "exactement ce que le cours attend : l’historiographie classique a "
     "longtemps mis en avant quelques inventions symboliques, et c’est "
     "précisément cette lecture que le chapitre corrige."),
'ch8-open-5': f(niv='connaitre', sp='c8-02', b=187,
 ans={'modele': "Le domestic system est une production à domicile, souvent "
      "par des paysans-ouvriers, les matières premières étant fournies par un "
      "marchand : c’est une forme de proto-industrialisation, dispersée et "
      "intégrée à un réseau marchand. Le factory system concentre au "
      "contraire les ouvriers dans un même lieu, avec des machines plus "
      "puissantes, un contrôle du temps de travail, une supervision "
      "hiérarchique, une division des tâches et une production intensive. Il "
      "entraîne la séparation du lieu de vie et du lieu de travail, la montée "
      "du salariat industriel et une coordination centralisée.",
      'cles': [{'f': ['domicile', 'marchand', 'disperse', 'paysan'],
                'l': 'domestic system : production dispersée à domicile'},
               {'f': ['concentration', 'meme lieu', 'usine'],
                'l': 'factory system : concentration dans un même lieu'},
               {'f': ['discipline', 'surveillance', 'hierarchie', 'temps'],
                'l': 'avec discipline du temps et supervision hiérarchique'},
               {'f': ['coexist', 'progressif', '1870'],
                'l': 'les deux coexistent longtemps : l’usine s’impose vers 1870'}]},
 exp="Le repère chronologique est utile : c’est vers 1870 que le factory "
     "system est véritablement imposé comme forme dominante."),

# --------------------------- c8-02 révolution agricole, démographie, science
'ch8-qcm-11': f(niv='comprendre', sp='c8-02', b=279,
 exp="La révolution agricole anglaise, située principalement entre 1700 et "
     "1750, double les rendements entre 1700 et 1850. Elle permet de nourrir "
     "des populations urbaines croissantes et de libérer des bras pour "
     "l’industrie, tout en améliorant l’alimentation, donc en faisant baisser "
     "la mortalité et en soutenant la croissance démographique.",
 why=["L’agriculture ne produit pas les machines : c’est l’industrie qui lui "
      "en fournit, en retour.",
      "Elle dégage effectivement des capitaux agricoles, mais ce n’est pas "
      "son seul apport : l’adverbe « uniquement » rend la réponse fausse.",
      "Le prix des matières premières importées ne dépend pas de "
      "l’agriculture anglaise."],
 diss="Formule clé du cours : pas d’industrialisation durable sans surplus "
      "agricole capable de nourrir les villes."),
'ch8-vf-5': f(niv='comprendre', sp='c8-02', b=286,
 exp="La révolution agricole est une condition essentielle : elle nourrit les "
     "villes, libère de la main-d’œuvre et dégage des capitaux. Mais le cours "
     "refuse la causalité à sens unique : l’industrie fournit en retour à "
     "l’agriculture machines, outils métalliques, acier, engrais, innovations "
     "chimiques et moyens de transport. La bonne lecture est circulaire, "
     "cumulative et réciproque."),
'ch8-qcm-34': f(niv='connaitre', sp='c8-02', b=287,
 exp="Trois apports sont identifiés par la lecture classique : un surplus "
     "alimentaire qui réduit la mortalité, une libération de main-d’œuvre, et "
     "des capitaux agricoles dégagés et investissables. Le cours ajoute "
     "aussitôt la réciproque : l’industrie modernise à son tour "
     "l’agriculture.",
 why=["La révolution agricole réduit au contraire le nombre de travailleurs "
      "nécessaires dans l’agriculture.",
      "Elle facilite l’industrialisation au lieu de la concurrencer pour la "
      "main-d’œuvre.",
      "La conversion de terres en usines n’est pas le mécanisme analysé."]),
'ch8-qcm-20': f(niv='connaitre', sp='c8-02', b=231,
 exp="Les enclosures désignent le mouvement de clôture et de privatisation "
     "des terres communes en Angleterre. Leurs effets économiques sont "
     "l’affirmation de la propriété privée, la sécurisation de "
     "l’investissement, la possibilité d’utiliser des machines coûteuses et la "
     "rationalisation des exploitations. Leurs effets sociaux sont la "
     "disparition des communaux, la fragilisation d’une partie de la "
     "paysannerie et un exode rural accru.",
 why=["Il ne s’agit pas de clôtures autour des usines.",
      "Les zones franches sont un dispositif contemporain.",
      "La protection douanière est une politique commerciale distincte."],
 diss="Formule du cours à retenir : les enclosures illustrent déjà la logique "
      "du capitalisme — gains d’efficacité, mais coût social élevé."),
'ch8-vf-8': f(niv='comprendre', sp='c8-02', b=238,
 exp="En faisant disparaître les communaux et en fragilisant une partie de la "
     "paysannerie, les enclosures provoquent un exode rural accru, qui alimente "
     "la main-d’œuvre disponible pour l’industrie. Le Parlement joue d’ailleurs "
     "un rôle actif dans ce mouvement, ce qui montre sa capacité politique à "
     "imposer des transformations structurelles."),
'ch8-qcm-21': f(niv='comprendre', sp='c8-02', b=270,
 exp="La révolution démographique apporte plus de main-d’œuvre, plus de "
     "salariés potentiels, plus de consommateurs et un élargissement de la "
     "taille des marchés. L’industrialisation a besoin des deux à la fois : "
     "des travailleurs et des débouchés.",
 why=["Le cours soutient exactement l’inverse : la croissance démographique "
      "est un moteur, pas un frein.",
      "L’affirmation d’absence d’impact contredit tout le raisonnement du "
      "chapitre.",
      "Les conditions de travail se dégradent mais la population croît : il "
      "n’y a pas de recul démographique."]),
'ch8-vf-18': f(niv='comprendre', sp='c8-02', b=270,
 exp="C’est l’inverse : la croissance démographique augmente à la fois "
     "l’offre de travail, la taille des marchés et la population urbaine. "
     "Elle alimente donc l’industrialisation, la rentabilité des "
     "investissements et la croissance de la demande."),
'ch8-qcm-25': f(niv='comprendre', sp='c8-02', b=325,
 exp="Le développement de la science favorise l’amélioration des procédés, la "
     "diffusion d’une culture de l’expérimentation, le perfectionnement des "
     "machines, les innovations mécaniques et la rationalisation de la "
     "production. Le cours en fait un moteur autonome, entretenant un rapport "
     "circulaire avec l’industrie.",
 why=["Le cours accorde au contraire à la science une place distincte dans "
      "le schéma des transformations.",
      "L’idée d’une science coupée de l’économie contredit le rapport "
      "circulaire décrit.",
      "La science ne remplace pas le travail artisanal : elle alimente "
      "l’innovation technique."]),
'ch8-qcm-36': f(niv='comprendre', sp='c8-02', b=335,
 exp="Les progrès de la médecine reposent sur la vaccination, les progrès de "
     "l’hygiène et l’amélioration des connaissances médicales. Le repère clé "
     "est 1797, année où Edward Jenner met au point le vaccin contre la "
     "variole. Leurs effets sont la baisse de la mortalité, l’amélioration de "
     "la santé et le soutien à la croissance démographique.",
 why=["Le cours en fait une case distincte du schéma des transformations.",
      "L’effet passe par la démographie, non par une hausse directe de la "
      "productivité.",
      "Les maladies professionnelles liées à l’usine ne sont pas l’objet de "
      "ces progrès."]),
'ch8-open-15': f(niv='comprendre', sp='c8-02', b=334,
 ans={'modele': "Les progrès de la médecine constituent, dans le schéma du "
      "cours, une case distincte des autres transformations. Ils reposent sur "
      "la vaccination — Edward Jenner met au point le vaccin contre la variole "
      "en 1797 —, sur les progrès de l’hygiène et sur l’amélioration des "
      "connaissances médicales. Leurs effets sont la baisse de la mortalité, "
      "l’amélioration de la santé et le soutien à la croissance "
      "démographique, laquelle fournit à la fois une main-d’œuvre plus "
      "nombreuse et une demande élargie.",
      'cles': [{'f': ['jenner', '1797', 'variole', 'vaccin'],
                'l': 'Jenner et le vaccin contre la variole en 1797'},
               {'f': ['hygiene', 'connaissance'],
                'l': 'les progrès de l’hygiène et des connaissances'},
               {'f': ['mortalite', 'baisse'],
                'l': 'la baisse de la mortalité'},
               {'f': ['demographique', 'main d oeuvre', 'demande'],
                'l': 'donc croissance démographique, main-d’œuvre et demande'}]},
 exp="Il faut distinguer soigneusement cette case de celle de la science : "
     "la science alimente l’innovation technique, la médecine agit par la "
     "démographie."),
'ch8-open-3': f(niv='comprendre', sp='c8-02', b=285,
 ans={'modele': "La révolution agricole anglaise, principalement entre 1700 "
      "et 1750, double les rendements entre 1700 et 1850 grâce à "
      "l’amélioration de l’outillage, à la suppression progressive de la "
      "jachère, à l’abandon de l’assolement triennal, à de meilleures "
      "rotations et à de nouveaux engrais ; les enclosures y ajoutent la "
      "sécurisation de la propriété privée. Elle permet de nourrir les villes, "
      "libère de la main-d’œuvre par l’exode rural et dégage des capitaux "
      "investissables. Mais la relation est réciproque : l’industrie fournit "
      "en retour machines, acier, engrais et transports. La bonne lecture est "
      "circulaire et cumulative.",
      'cles': [{'f': ['rendement', 'jachere', 'assolement', 'engrais', 'outillage'],
                'l': 'des progrès techniques : rendements, jachère, rotations'},
               {'f': ['enclosure', 'cloture', 'propriete'],
                'l': 'les enclosures et la propriété privée'},
               {'f': ['nourrir', 'main d oeuvre', 'exode', 'capitaux'],
                'l': 'nourrir les villes, libérer des bras, dégager des capitaux'},
               {'f': ['reciproque', 'circulaire', 'retour', 'modernise'],
                'l': 'et une causalité réciproque avec l’industrie'}]},
 exp="Le cours demande aussi de distinguer rigoureusement rendement — "
     "production par surface cultivée — et productivité — production par "
     "facteur de production."),

# ------------------------------------------- c8-03 charbon et transports
'ch8-qcm-31': f(niv='comprendre', sp='c8-03', b=360,
 exp="Avant le XVIIIᵉ siècle, l’économie repose sur le bois, la force humaine "
     "et animale, l’eau et le vent. Avec la déforestation, la hausse des "
     "besoins et les limites des énergies organiques, le charbon devient "
     "central : énergie plus abondante, plus concentrée, plus régulière, "
     "adaptée à la mécanisation, alimentant la vapeur et soutenant sidérurgie "
     "et métallurgie. Repère : la consommation de charbon est multipliée par "
     "250 entre 1750 et 1830.",
 why=["Le charbon dépasse très largement l’usage domestique.",
      "L’exportation n’est pas l’usage principal : le charbon alimente "
      "l’industrie nationale.",
      "Le basculement s’opère dès le XVIIIᵉ siècle, et non après 1850."]),
'ch8-vf-13': f(niv='connaitre', sp='c8-03', b=371,
 exp="Le charbon permet à la Grande-Bretagne de sortir des contraintes des "
     "énergies organiques — bois, force humaine et animale, eau, vent — et "
     "constitue la base énergétique de la première révolution industrielle. Sa "
     "consommation est multipliée par 250 entre 1750 et 1830."),
'ch8-qcm-19': f(niv='comprendre', sp='c8-03', b=382,
 exp="La révolution des transports comprend l’amélioration des routes, le "
     "développement des canaux — Bridgewater Canal en 1761 — puis du chemin de "
     "fer, avec l’inauguration de la ligne Liverpool-Manchester en 1830 et un "
     "développement ferroviaire majeur à partir des années 1830-1840. Ses "
     "effets : baisse des coûts de transport, meilleure circulation du "
     "charbon, élargissement des marchés, approvisionnement des villes, "
     "soutien à l’urbanisation et intégration du marché national.",
 why=["Le transport de personnes n’est qu’un aspect : le cours insiste sur le "
      "charbon et les marchandises.",
      "Les canaux précèdent le décollage ferroviaire : les transports sont "
      "une condition, non une simple conséquence.",
      "L’usage militaire n’est pas évoqué pour la Grande-Bretagne."]),
'ch8-qcm-33': f(niv='comprendre', sp='c8-03', b=388,
 exp="La révolution des transports réduit fortement les coûts de circulation, "
     "élargit la taille des marchés, soutient l’approvisionnement des villes "
     "et l’urbanisation, et renforce l’intégration du marché national. Elle "
     "est indissociable des autres transformations : sans circulation du "
     "charbon, pas de mécanisation à grande échelle.",
 why=["Le déplacement de la main-d’œuvre n’est pas l’effet principal retenu.",
      "Les canaux sont antérieurs au décollage industriel : ils en sont une "
      "condition.",
      "Les transports diffusent les innovations, ils ne les créent pas "
      "directement."]),
'ch8-vf-11': f(niv='comprendre', sp='c8-03', b=372,
 exp="La révolution des transports est au contraire intrinsèquement liée aux "
     "autres transformations : elle fait circuler le charbon, élargit les "
     "marchés, approvisionne les villes et soutient l’urbanisation. Le cours "
     "raisonne précisément en causalités croisées."),
'ch8-qcm-39': f(niv='comprendre', sp='c8-03', b=278,
 exp="Une agriculture plus productive permet de nourrir des populations "
     "urbaines croissantes et de libérer des bras pour l’industrie. "
     "L’urbanisation concentre la main-d’œuvre, élargit la demande de biens et "
     "services, et accompagne la montée du salariat industriel ainsi que la "
     "séparation du lieu de vie et du lieu de travail.",
 why=["Les problèmes sociaux sont réels, mais l’urbanisation a aussi des "
      "effets économiques majeurs.",
      "C’est l’inverse : la révolution agricole rend l’urbanisation "
      "possible.",
      "L’urbanisation alimente l’industrie en main-d’œuvre, elle ne "
      "l’affaiblit pas."]),
'ch8-open-6': f(niv='comprendre', sp='c8-03', b=373,
 ans={'modele': "La révolution des transports comprend l’amélioration des "
      "routes, le développement des canaux — le Bridgewater Canal dès 1761 — "
      "puis l’essor du chemin de fer, avec l’inauguration de la ligne "
      "Liverpool-Manchester en 1830 et un développement ferroviaire majeur "
      "dans les années 1830-1840. Ses effets sont la baisse des coûts de "
      "transport, une meilleure circulation du charbon, l’élargissement des "
      "marchés, l’approvisionnement des villes, le soutien à l’urbanisation et "
      "l’intégration du marché national.",
      'cles': [{'f': ['canaux', 'route', 'chemin de fer', 'rail'],
                'l': 'routes, canaux puis chemin de fer'},
               {'f': ['1761', '1830', 'bridgewater', 'liverpool', 'manchester'],
                'l': 'des repères : 1761, 1830'},
               {'f': ['cout', 'baisse'], 'l': 'la baisse des coûts de transport'},
               {'f': ['marche', 'national', 'integration', 'ville'],
                'l': 'l’élargissement et l’intégration des marchés'}]},
 exp="Les transports sont aussi un débouché : l’industrialisation crée une "
     "demande de rails et de locomotives, ce qui illustre les effets "
     "d’entraînement intersectoriels."),
'ch8-qcm-16': f(niv='comprendre', sp='c8-03', b=453,
 exp="Le cours retient la stabilité politique relative, la protection des "
     "droits de propriété, la crédibilité des contrats et un Parlement "
     "fonctionnel capable d’imposer des réformes structurelles — enclosures, "
     "canaux, infrastructures. Les institutions ne produisent pas directement "
     "des machines, mais elles créent un environnement favorable à "
     "l’investissement et à l’innovation.",
 why=["La Grande-Bretagne se caractérise au contraire par la limitation du "
      "pouvoir royal après 1688.",
      "Le mercantilisme strict n’est pas le cadre retenu par le cours.",
      "Les colonies fournissent matières premières et débouchés, mais le "
      "cours ne parle pas d’union douanière intégrée."],
 diss="Le repère institutionnel décisif est 1688, la Glorieuse Révolution, "
      "qu’analysent North puis Acemoglu et Robinson."),
'ch8-qcm-6': f(niv='connaitre', sp='c8-03', b=597,
 exp="La deuxième révolution industrielle, à partir de 1880, repose sur "
     "l’électricité et le pétrole. Ses secteurs moteurs sont l’automobile, la "
     "chimie, l’électroménager et les télécommunications, et ses pays leaders "
     "les États-Unis et l’Allemagne.",
 why=["Charbon et eau caractérisent la première révolution industrielle.",
      "Éolien et hydraulique font partie des énergies organiques antérieures.",
      "Vapeur et charbon sont l’énergie de la première révolution."]),
'ch8-vf-16': f(niv='connaitre', sp='c8-03', b=593,
 exp="La deuxième révolution industrielle débute à partir de 1880 et se "
     "prolonge jusqu’aux années 1970 environ. Elle correspond à l’essor de la "
     "production de masse, de la grande firme et des biens de consommation "
     "durables."),
'ch8-vf-3': f(niv='connaitre', sp='c8-03', b=594,
 exp="Les pays leaders de la deuxième révolution industrielle sont les "
     "États-Unis et l’Allemagne. Le cours en tire une leçon : être pionnier "
     "donne un avantage, mais pas une domination éternelle — ces « followers » "
     "rattrapent puis dépassent la Grande-Bretagne dans plusieurs secteurs."),

# ------------------------------------- c8-04 précocité anglaise, auteurs
'ch8-qcm-26': f(niv='comprendre', sp='c8-04', b=392,
 exp="Aucune explication monocausale ne convient. Le cours articule la "
     "révolution agricole précoce, la stabilité institutionnelle après 1688, "
     "l’accès aux marchés et aux matières premières coloniales, l’abondance de "
     "charbon proche des centres de consommation, le développement bancaire et "
     "financier, et un cadre favorable aux entrepreneurs. Il rappelle que "
     "d’autres espaces, notamment la Chine, disposaient aussi de ressources et "
     "de capacités techniques importantes.",
 why=["Le fer n’est pas la ressource décisive : c’est le charbon, et surtout "
      "sa proximité des centres de consommation.",
      "La taille de l’empire ne suffit pas : d’autres puissances coloniales ne "
      "s’industrialisent pas les premières.",
      "Aucune aide financière française n’intervient."]),
'ch8-open-10': f(niv='comprendre', sp='c8-04', b=731,
 ans={'modele': "La précocité anglaise ne relève ni d’un miracle ni d’une "
      "cause unique : elle résulte d’une conjonction de facteurs "
      "géographiques — insularité, puissance navale, charbon proche des "
      "centres de consommation —, impériaux — matières premières et débouchés "
      "coloniaux —, énergétiques, économiques — salaires élevés et énergie "
      "bon marché rendant la mécanisation rentable, développement bancaire et "
      "financier —, institutionnels — stabilité après 1688, droits de "
      "propriété, Parlement capable d’imposer des réformes — et scientifiques. "
      "S’y ajoutent la révolution agricole, la démographie, la médecine et les "
      "transports.",
      'cles': [{'f': ['charbon', 'geographique', 'insul', 'maritime'],
                'l': 'des facteurs géographiques et énergétiques'},
               {'f': ['colonial', 'empire', 'matiere premiere', 'debouche'],
                'l': 'l’empire colonial : matières premières et débouchés'},
               {'f': ['institution', 'propriete', '1688', 'parlement', 'stabilite'],
                'l': 'des institutions favorables à l’investissement'},
               {'f': ['agricole', 'demographi', 'banc', 'financier', 'science'],
                'l': 'révolution agricole, démographie, finance, science'}]},
 exp="Le cours mentionne enfin une thèse plus provocatrice : Brasseul, dans "
     "« Petite histoire des faits économiques » (2014), rapporte que Nick "
     "Crafts aurait insisté sur le caractère fortuit de la révolution "
     "industrielle anglaise. Mais le hasard pur est jugé insuffisant en "
     "histoire économique."),
'ch8-qcm-28': f(niv='raisonner', sp='c8-04', b=437,
 q="Comment Robert Allen explique-t-il que la mécanisation ait été rationnelle "
   "en Grande-Bretagne ?",
 opts=["Par l’abondance de main-d’œuvre, qui rendait les machines faciles à "
       "faire fonctionner",
       "Par une structure particulière des prix relatifs : des salaires "
       "élevés et une énergie bon marché, de sorte que substituer du capital "
       "au travail devenait rentable",
       "Par l’existence de brevets protégeant les inventeurs",
       "Par le soutien financier de l’État aux industries naissantes"],
 ans=1,
 why=["C’est l’inverse : ce sont des salaires élevés, donc un travail "
      "coûteux, qui incitent à mécaniser.",
      "Les brevets jouent un rôle — Watt en 1769 — mais ce n’est pas "
      "l’argument d’Allen.",
      "Aucune politique industrielle de ce type n’est décrite pour "
      "l’Angleterre du XVIIIᵉ siècle."],
 exp="Dans « Introduction à l’histoire économique mondiale » (2014), Allen "
     "montre que disposer de ressources ne suffit pas : encore faut-il que "
     "leur exploitation soit rentable. Comme le travail coûte cher et que le "
     "charbon est bon marché, les entrepreneurs ont intérêt à investir dans "
     "les machines et à innover pour économiser la main-d’œuvre.",
 diss="Argument décisif : il explique pourquoi la même technique peut être "
      "adoptée dans un pays et délaissée dans un autre, à niveau de "
      "connaissances égal."),
'ch8-qcm-29': f(niv='comprendre', sp='c8-04', b=447,
 exp="Dans la logique décrite par Allen, les entrepreneurs britanniques ont "
     "intérêt à substituer du capital au travail, à investir dans les machines "
     "et à innover pour économiser la main-d’œuvre, précisément parce que les "
     "salaires sont élevés et l’énergie bon marché. Le progrès technique de la "
     "première industrialisation est donc d’abord économiseur de travail.",
 why=["Il n’économise pas le capital : il en accroît au contraire l’emploi "
      "relatif.",
      "L’économie de matières premières n’est pas le mécanisme analysé ici.",
      "Le temps de commercialisation relève de l’innovation de débouchés chez "
      "Schumpeter."]),
'ch8-qcm-23': f(niv='comprendre', sp='c8-05', b=745,
 q="Comment l’analyse classique et néoclassique conçoit-elle l’entreprise, "
   "selon le cours ?",
 opts=["Comme le lieu stratégique de l’innovation",
       "Comme une unité de production relativement abstraite, insérée dans un "
       "marché qui tend vers l’équilibre, l’idéal théorique étant la "
       "concurrence pure et parfaite",
       "Comme une organisation traversée par des rapports de pouvoir entre "
       "propriétaires et managers",
       "Comme un acteur du développement durable"],
 ans=1,
 why=["C’est précisément la conception de Schumpeter, qui rompt avec la "
      "première.",
      "Les rapports de pouvoir dans l’entreprise sont analysés plus loin, à "
      "propos de la gouvernance.",
      "La RSE est une problématique contemporaine, abordée en fin de "
      "chapitre."],
 exp="Chez les marginalistes, l’idéal théorique est la concurrence pure et "
     "parfaite : grand nombre d’agents, information parfaite, homogénéité des "
     "produits, allocation optimale par le marché. Schumpeter rompt avec cette "
     "lecture en déplaçant l’analyse de l’équilibre vers la dynamique.",
 diss="Poser d’abord la conception standard permet de mesurer l’ampleur des "
      "trois ruptures schumpétériennes : dynamique contre équilibre, monopole "
      "temporaire contre CPP, et fragilité historique du capitalisme."),
'ch8-qcm-7': f(niv='connaitre', sp='c8-03', b=597,
 exp="Les secteurs moteurs de la deuxième révolution industrielle sont la "
     "chimie, l’automobile, l’électroménager et les télécommunications, "
     "portés par l’électricité et le pétrole. Elle correspond à l’essor de la "
     "production de masse, de la grande firme et des biens de consommation "
     "durables.",
 why=["Textile, sidérurgie et machine à vapeur sont les secteurs de la "
      "première révolution industrielle.",
      "Agriculture, construction et transport maritime ne figurent pas parmi "
      "les secteurs moteurs retenus.",
      "Informatique, numérique et IA relèvent de la troisième révolution, à "
      "partir des années 1970."]),
'ch8-qcm-40': f(niv='comprendre', sp='c8-02', b=70,
 exp="La causalité cumulative circulaire signifie que les transformations "
     "— agricoles, démographiques, techniques, institutionnelles — se "
     "renforcent mutuellement, sans point de départ unique : hausse des "
     "rendements, meilleure alimentation, croissance démographique, hausse de "
     "la demande, urbanisation, industrialisation, transports, diffusion des "
     "innovations, puis retour de l’industrie sur l’agriculture.",
 why=["Une innovation n’enclenche pas une seule autre innovation : les "
      "effets se diffusent dans plusieurs directions à la fois.",
      "Les crises cycliques relèvent de l’analyse schumpétérienne des cycles, "
      "une autre partie du chapitre.",
      "Aucune périodicité de ce type n’est évoquée ici : les cycles de "
      "Juglar, de 8 à 10 ans, appartiennent à une autre analyse."]),
'ch8-qcm-22': f(niv='connaitre', sp='c8-05', b=746,
 exp="Joseph Schumpeter, dans « Théorie de l’évolution économique » (1912), "
     "place l’innovation et l’entrepreneur innovateur au cœur de la dynamique "
     "capitaliste. L’entreprise n’est plus un simple lieu de production : elle "
     "devient le lieu stratégique de l’innovation.",
 why=["Marx analyse l’industrialisation capitaliste en termes de lutte des "
      "classes.",
      "Keynes n’est pas mobilisé dans ce chapitre.",
      "Ricardo appartient à l’économie politique classique, dont Schumpeter "
      "se démarque."]),
'ch8-qcm-37': f(niv='comprendre', sp='c8-07', b=1106,
 q="Sur quoi Marx fait-il porter l’analyse de la fin du capitalisme, par "
   "opposition à Schumpeter ?",
 opts=["Sur la lutte des classes et l’effondrement révolutionnaire du système",
       "Sur la bureaucratisation de l’innovation dans les grandes firmes",
       "Sur l’épuisement des ressources naturelles",
       "Sur la baisse tendancielle de la demande globale"],
 ans=0,
 why=["La bureaucratisation de l’innovation est l’argument de Schumpeter, pas "
      "celui de Marx.",
      "L’épuisement des ressources n’est pas le mécanisme invoqué dans ce "
      "chapitre.",
      "L’insuffisance de la demande relève d’une analyse keynésienne."],
 exp="Schumpeter rejoint Marx sur un point : le capitalisme n’est pas éternel "
     "et peut être historiquement dépassé. Mais il ne met au centre ni la "
     "lutte des classes ni l’effondrement révolutionnaire : il insiste sur la "
     "transformation interne du capitalisme, qui voit l’entrepreneur "
     "innovateur s’effacer au profit des grandes firmes oligopolistiques et "
     "bureaucratisées.",
 diss="Comparaison très rentable : même conclusion — le capitalisme est "
      "historiquement situé — pour des raisons opposées."),
'ch8-vf-19': f(niv='comprendre', sp='c8-07', b=1102,
 q="Selon le cours, Marx et Schumpeter annoncent tous deux la fin du "
   "capitalisme, mais pour des raisons différentes.",
 ans=True,
 exp="Marx met au centre la lutte des classes et l’effondrement "
     "révolutionnaire du système. Schumpeter insiste au contraire sur la "
     "transformation interne du capitalisme : son propre développement "
     "modifie les conditions de l’innovation, les innovateurs individuels "
     "disparaissant progressivement au profit de grandes firmes "
     "oligopolistiques. Le capitalisme peut donc être miné par sa propre "
     "réussite."),
'ch8-open-12': f(niv='raisonner', sp='c8-07', b=1101,
 q="Comparez les analyses de Marx et de Schumpeter sur le destin du "
   "capitalisme.",
 ans={'modele': "Les deux auteurs considèrent que le capitalisme n’est pas "
      "éternel et peut être historiquement dépassé. Mais les mécanismes "
      "diffèrent. Marx met au centre la lutte des classes et l’effondrement "
      "révolutionnaire du système. Schumpeter, lui, insiste sur la "
      "transformation interne : à mesure que le capitalisme se développe, les "
      "entreprises grossissent, les marchés se concentrent, la bureaucratie "
      "s’installe et l’innovation devient routinière. L’entrepreneur "
      "innovateur s’efface au profit de grandes organisations "
      "oligopolistiques. Le capitalisme serait donc miné par sa propre "
      "réussite, qui étouffe la fonction entrepreneuriale dont il tirait sa "
      "force.",
      'cles': [{'f': ['pas eternel', 'depasse', 'fin du capitalisme'],
                'l': 'les deux annoncent un dépassement historique'},
               {'f': ['lutte des classes', 'revolution', 'marx'],
                'l': 'Marx : lutte des classes et effondrement révolutionnaire'},
               {'f': ['oligopole', 'bureaucrat', 'grande firme', 'routin'],
                'l': 'Schumpeter : bureaucratisation et oligopoles'},
               {'f': ['propre reussite', 'succes', 'etouffe', 'entrepreneur'],
                'l': 'le capitalisme miné par son propre succès'}]},
 exp="Formule du cours à retenir : avec le développement du capitalisme, les "
     "innovateurs individuels disparaissent progressivement au profit des "
     "grandes firmes oligopolistiques."),
'ch8-open-11': f(niv='comprendre', sp='c8-01', b=199,
 q="Quelles transformations sociales le passage au factory system "
   "entraîne-t-il ?",
 ans={'modele': "Le factory system entraîne la séparation du lieu de vie et "
      "du lieu de travail, la montée du salariat industriel, la discipline du "
      "temps, une hiérarchie plus forte, une coordination centralisée et une "
      "hausse de la productivité. Il s’accompagne de l’urbanisation, puisque "
      "la concentration des machines et le besoin d’énergie favorisent le "
      "regroupement des ouvriers dans un même lieu. Plus largement, le cours "
      "parle de transformation des rapports sociaux : les ouvriers perdent "
      "l’autonomie du domestic system et suivent le rythme imposé par la "
      "machine et par le contremaître.",
      'cles': [{'f': ['salariat', 'salarie'], 'l': 'la montée du salariat industriel'},
               {'f': ['lieu de vie', 'separation', 'domicile'],
                'l': 'la séparation du lieu de vie et du lieu de travail'},
               {'f': ['discipline', 'hierarchie', 'temps', 'contremaitre', 'autonomie'],
                'l': 'la discipline du temps et la perte d’autonomie'},
               {'f': ['urbanisation', 'ville', 'concentration'],
                'l': 'l’urbanisation et la concentration ouvrière'}]},
 exp="Le cours relie directement ces transformations au ludisme : les "
     "luddites ne contestent pas seulement la perte d’emploi, mais aussi les "
     "nouvelles cadences, la discipline industrielle, l’autorité du "
     "contremaître et la perte d’autonomie."),
'ch8-open-7': f(niv='connaitre', sp='c8-03', b=593,
 ans={'modele': "La deuxième révolution industrielle débute à partir de 1880 "
      "et se prolonge jusqu’aux années 1970 environ. Ses pays leaders sont les "
      "États-Unis et l’Allemagne. Ses énergies dominantes sont l’électricité "
      "et le pétrole. Ses secteurs moteurs sont l’automobile, la chimie, "
      "l’électroménager et les télécommunications. Elle correspond à l’essor "
      "de la production de masse, de la grande firme et de nouveaux biens de "
      "consommation durables.",
      'cles': [{'f': ['1880'], 'l': 'à partir de 1880'},
               {'f': ['etats unis', 'allemagne'],
                'l': 'leaders : États-Unis et Allemagne'},
               {'f': ['electricite', 'petrole'],
                'l': 'énergies : électricité et pétrole'},
               {'f': ['automobile', 'chimie', 'masse', 'grande firme'],
                'l': 'automobile, chimie, production de masse'}]},
 exp="C’est aussi la période où les « followers » rattrapent puis dépassent la "
     "Grande-Bretagne dans plusieurs secteurs : la précocité donne un "
     "avantage, pas une domination éternelle."),
'ch8-open-13': f(niv='raisonner', sp='c8-14', b=2260,
 ans={'modele': "La révolution numérique peut être lue comme une nouvelle "
      "révolution industrielle parce qu’elle modifie les modes de production, "
      "transforme le travail, change les rapports entre entreprises et "
      "consommateurs, bouleverse les formes de concurrence et transforme les "
      "modes de régulation — exactement ce que firent le charbon puis "
      "l’électricité. Elle repose sur trois dynamiques : l’intelligence "
      "artificielle et la robotisation, le big data, les plateformes. Elle se "
      "distingue par sa rapidité de diffusion : là où les innovations passées "
      "mettaient des décennies, certaines technologies atteignent des millions "
      "d’utilisateurs en quelques mois. Mais ce n’est pas une rupture "
      "totale : elle prolonge l’informatique et Internet et soulève des "
      "questions anciennes — emploi, productivité, concentration du pouvoir "
      "économique.",
      'cles': [{'f': ['production', 'travail', 'concurrence', 'regulation'],
                'l': 'elle transforme production, travail, concurrence et régulation'},
               {'f': ['ia', 'big data', 'plateforme', 'donnee'],
                'l': 'trois dynamiques : IA, big data, plateformes'},
               {'f': ['rapidite', 'acceleration', 'diffusion'],
                'l': 'une diffusion beaucoup plus rapide'},
               {'f': ['continuite', 'prolonge', 'pas une rupture', 'ancien'],
                'l': 'mais une continuité avec les questions anciennes'}]},
 exp="Le cours note aussi le débat de dénombrement : certains comptent trois "
     "révolutions industrielles, d’autres quatre en distinguant le numérique "
     "de l’intelligence artificielle."),

# ---------------------------------------------- c8-06 cycles et grappes
'ch8-aut195-1': f(niv='connaitre', sp='c8-06', b=1043,
 exp="Kitchin : cycle court de 3 à 5 ans, lié aux variations de stocks et aux "
     "ajustements conjoncturels. Juglar : cycle moyen de 8 à 10 ans, lié à "
     "l’investissement productif et au crédit. Kondratiev : cycle long de 50 à "
     "60 ans, porté par les grappes d’innovations majeures. Les trois "
     "temporalités s’emboîtent : des Kitchin dans un Juglar, plusieurs Juglar "
     "dans un Kondratiev.",
 why=["Les durées de Kitchin et de Juglar sont inversées.",
      "Les trois durées sont permutées de façon incohérente.",
      "Les causes diffèrent justement : stocks, investissement, innovations."],
 diss="Chez Schumpeter, l’innovation explique surtout les cycles longs ; "
      "Kitchin et Juglar rappellent que l’économie capitaliste est traversée "
      "par plusieurs rythmes emboîtés."),

# ------------------------------------- c8-07 / c8-08 taylorisme et fordisme
'ch8-aut195-3': f(niv='comprendre', sp='c8-07', b=1326,
 exp="Georges Friedmann parle de « travail en miettes » : la parcellisation "
     "entraîne monotonie, fatigue et perte de sens, et l’ouvrier devient "
     "étranger à son travail. Le cours souligne l’enchaînement décisif : les "
     "dysfonctionnements sociaux — turn-over élevé, absentéisme, malfaçons — "
     "engendrent des coûts de recrutement, de formation, de remplacement et de "
     "retouches. Les limites sociales deviennent donc des limites économiques.",
 why=["La cage d’acier est une expression wébérienne, non mobilisée ici.",
      "La destruction créatrice est l’expression de Schumpeter.",
      "L’armée industrielle de réserve est un concept marxien."],
 diss="C’est cet enchaînement — du social vers l’économique — qui justifie le "
      "passage au fordisme puis au toyotisme."),
'ch8-open-8': f(niv='comprendre', sp='c8-07', b=1303,
 ans={'modele': "Le taylorisme est une organisation scientifique du travail. "
      "Taylor part d’un constat : dans les ateliers traditionnels, les "
      "ouvriers qualifiés maîtrisent le processus et contrôlent leur rythme, "
      "ce qui permet une « flânerie systématique ». Il transforme donc le "
      "travail en objet mesurable : observation des gestes, découpage des "
      "tâches, chronométrage. Il en résulte une division horizontale — la "
      "parcellisation en tâches simples et répétitives — et une division "
      "verticale — la séparation de la conception, confiée aux ingénieurs et "
      "au bureau des méthodes, et de l’exécution, confiée aux ouvriers. Le "
      "salaire différentiel aux pièces sert d’outil disciplinaire.",
      'cles': [{'f': ['chronometr', 'mesur', 'scientifique', 'geste'],
                'l': 'mesurer et chronométrer le travail'},
               {'f': ['horizontale', 'parcellis', 'tache simple'],
                'l': 'division horizontale : parcellisation'},
               {'f': ['verticale', 'conception', 'execution'],
                'l': 'division verticale : conception séparée de l’exécution'},
               {'f': ['salaire', 'piece', 'differentiel', 'incit'],
                'l': 'le salaire aux pièces comme incitation'}]},
 exp="Le double avantage recherché est explicite dans le cours : des gains de "
     "temps par la spécialisation, et un meilleur contrôle du travail par le "
     "contremaître. La flânerie systématique n’est d’ailleurs pas "
     "irrationnelle : produire plus peut entraîner une hausse des cadences "
     "sans garantie de hausse de salaire."),
'ch8-open-9': f(niv='comprendre', sp='c8-08', b=1337,
 ans={'modele': "Ford reprend les principes du taylorisme mais ajoute deux "
      "changements. D’abord la chaîne de montage, grâce au convoyeur : les "
      "objets se déplacent vers les ouvriers, le rythme est imposé, les temps "
      "morts sont supprimés ; avec la standardisation — un modèle unique, la "
      "Ford T — cela permet la production de masse et des économies "
      "d’échelle. Ensuite la hausse des salaires, portés de 2,5 à 5 dollars "
      "par jour : elle donne du pouvoir d’achat aux ouvriers, qui deviennent "
      "des clients, et elle fidélise une main-d’œuvre exposée à un fort "
      "turn-over en augmentant le coût d’opportunité du départ.",
      'cles': [{'f': ['chaine', 'convoyeur', 'tapis'],
                'l': 'la chaîne de montage et le convoyeur'},
               {'f': ['standardis', 'ford t', 'modele unique', 'serie'],
                'l': 'la standardisation et la production de masse'},
               {'f': ['salaire', 'cinq dollars', '5 dollars', 'pouvoir d achat'],
                'l': 'les hauts salaires : cinq dollars par jour'},
               {'f': ['turn over', 'fidelis', 'consommation de masse'],
                'l': 'pour fidéliser et soutenir la consommation de masse'}]},
 exp="Les chiffres du cours donnent la mesure du résultat : une Ford coûte "
     "690 dollars en 1913 et 290 en 1929 ; en 1914, 60 % des voitures "
     "produites aux États-Unis sont des Ford."),
'ch8-qcm-5': f(niv='connaitre', sp='c8-03', b=594,
 exp="Les pays leaders de la deuxième révolution industrielle sont les "
     "États-Unis et l’Allemagne, qui rattrapent puis dépassent la "
     "Grande-Bretagne dans plusieurs secteurs à partir de la fin du "
     "XIXᵉ siècle.",
 why=["La France et l’Italie ne figurent pas parmi les leaders.",
      "La Grande-Bretagne est le leader de la première révolution "
      "industrielle, et la France un pays suiveur.",
      "Russie et Japon ne sont pas cités dans cette chronologie."]),
'ch8-qcm-30': f(niv='connaitre', sp='c8-02', b=185,
 exp="La concentration productive désigne le regroupement des moyens de "
     "production dans de grandes unités, remplaçant la production dispersée du "
     "domestic system. Elle est favorisée par la concentration des machines, "
     "le besoin d’énergie et la volonté de mieux contrôler le travail.",
 why=["Le regroupement géographique des industries est un phénomène distinct, "
      "celui des districts industriels.",
      "Le contrôle de plusieurs usines par un propriétaire est une "
      "concentration capitalistique, non productive.",
      "La spécialisation régionale est une autre notion."]),
'ch8-qcm-41': f(niv='connaitre', sp='c8-08', b=1350,
 exp="Les économies d’échelle désignent la baisse du coût unitaire à mesure "
     "que les volumes produits augmentent. Le cours en donne les deux "
     "mécanismes : l’étalement des coûts fixes sur un plus grand nombre "
     "d’unités, et la baisse relative des coûts variables grâce aux remises et "
     "à la négociation avec les fournisseurs.",
 why=["La baisse des salaires n’est pas un mécanisme d’économie d’échelle.",
      "Les économies d’échelle permettent au contraire de baisser les prix.",
      "La spécialisation géographique relève d’une autre analyse."]),
'ch8-vf-20': f(niv='connaitre', sp='c8-08', b=1353,
 exp="C’est la définition même : le coût moyen diminue quand les volumes "
     "augmentent, par étalement des coûts fixes et baisse relative des coûts "
     "variables. Chez Ford, ce mécanisme permet de baisser les prix — de 690 "
     "dollars en 1913 à 290 en 1929 — donc d’élargir la demande."),
'ch8-qcm-38': f(niv='comprendre', sp='c8-08', b=1345,
 exp="En produisant en grande série, avec un modèle unique et une chaîne de "
     "montage, l’industrie obtient des volumes très supérieurs à ceux de "
     "l’artisanat pour un coût unitaire plus faible : étalement des coûts "
     "fixes, baisse relative des coûts variables, suppression des temps morts.",
 why=["La mécanisation accroît au contraire la valeur ajoutée par "
      "travailleur.",
      "Le coût unitaire industriel est très inférieur, ce qui change "
      "entièrement l’échelle de la production.",
      "La thèse physiocratique n’est pas mobilisée dans ce chapitre."]),
'ch8-open-14': f(niv='comprendre', sp='c8-08', b=1349,
 ans={'modele': "Les économies d’échelle désignent la baisse du coût moyen "
      "lorsque les volumes produits augmentent. Elles reposent sur deux "
      "mécanismes : l’étalement des coûts fixes sur davantage d’unités, et la "
      "baisse relative des coûts variables, obtenue par les remises et la "
      "négociation avec les fournisseurs. Leur rôle est décisif dans la "
      "compétitivité : elles permettent de baisser les prix, donc d’élargir la "
      "demande. Le cas Ford l’illustre : le prix d’une voiture passe de "
      "690 dollars en 1913 à 290 dollars en 1929, et dès 1914 six voitures "
      "américaines sur dix sont des Ford.",
      'cles': [{'f': ['cout unitaire', 'cout moyen', 'baisse'],
                'l': 'la baisse du coût unitaire avec le volume'},
               {'f': ['cout fixe', 'etalement', 'amorti'],
                'l': 'par étalement des coûts fixes'},
               {'f': ['prix', 'demande', 'competitivite'],
                'l': 'ce qui permet de baisser les prix et d’élargir la demande'},
               {'f': ['ford', '690', '290'],
                'l': 'l’exemple de Ford et de ses prix'}]},
 exp="Le cours relie aussi les économies d’échelle à la grande firme chez "
     "Chandler et aux plateformes numériques, où elles se combinent aux effets "
     "de réseau pour engendrer des positions oligopolistiques."),

# -------------------------------- c8-10 / c8-11 entrepreneur et managers
'ch8-qcm-8': f(niv='connaitre', sp='c8-01', b=104,
 exp="La révolution informatique et numérique commence dans les années 1970, "
     "avec le microprocesseur en 1971, puis l’informatique personnelle dans "
     "les années 1970-1980, Internet dans les années 1990, les plateformes "
     "dans les années 2000 et l’IA ainsi que le big data dans les années "
     "2010-2020.",
 why=["1945 correspond aux tout premiers calculateurs, hors du découpage "
      "retenu.",
      "1960 est antérieur au microprocesseur.",
      "1990 est la décennie d’Internet, c’est-à-dire une étape ultérieure."]),
'ch8-aut195-2': f(niv='comprendre', sp='c8-13', b=2053,
 exp="Dans « La Grande Transformation » (1944), Polanyi montre que l’économie "
     "ne peut être autonome : elle doit être encastrée dans la société, car un "
     "marché autorégulé exigerait de traiter le travail, la terre et la monnaie "
     "comme des marchandises ordinaires. Le marché ne peut donc pas être le "
     "seul principe d’organisation. Cette analyse fonde, dans le cours, le "
     "modèle des parties prenantes face au capitalisme actionnarial.",
 why=["Polanyi conteste précisément l’idée d’un marché autorégulateur.",
      "La neutralité de la monnaie est une thèse monétariste, étrangère à son "
      "propos.",
      "La concentration industrielle n’est pas l’objet de l’ouvrage."]),
'ch8-aut195-5': f(niv='comprendre', sp='c8-14', b=2379,
 exp="Bruno Patino développe l’idée d’une « civilisation du poisson rouge » : "
     "le numérique réduit progressivement la capacité d’attention, parce que "
     "les plateformes cherchent à capter le temps, retenir l’attention et "
     "multiplier les interactions rapides. Plus l’utilisateur reste sur les "
     "écrans, plus il produit de données, plus les algorithmes s’améliorent et "
     "plus ces données sont monétisables : l’attention humaine devient une "
     "ressource économique.",
 why=["La dématérialisation est un autre thème, que le cours qualifie "
      "d’ailleurs d’illusoire.",
      "L’ubérisation désigne la transformation des formes d’emploi par les "
      "plateformes.",
      "La concentration des plateformes relève des menaces économiques, et "
      "non de l’économie de l’attention."]),

# --------------------------------------- c8-16 / c8-17 travail et emploi
'ch8-qcm-27': f(niv='connaitre', sp='c8-16', b=2884,
 exp="Le mouvement des luddites apparaît en Angleterre entre 1811 et 1816 : "
     "des ouvriers du textile détruisent des machines industrielles, qu’ils "
     "considèrent comme une menace pour leur travail. Le ludisme désigne donc "
     "la contestation des machines perçues comme destructrices d’emploi.",
 why=["Il s’agit d’ouvriers, non de chefs d’entreprise.",
      "Les luddites contestent l’industrialisation, ils ne l’accélèrent pas.",
      "Le mouvement est antérieur au syndicalisme de négociation salariale."],
 diss="Le cours ajoute une nuance essentielle : les ouvriers ne contestent "
      "pas seulement la perte d’emploi, mais aussi les nouvelles cadences, la "
      "discipline industrielle, l’autorité du contremaître et la perte "
      "d’autonomie."),
'ch8-vf-12': f(niv='connaitre', sp='c8-16', b=2888,
 exp="Les luddites détruisent au contraire les machines, qu’ils perçoivent "
     "comme une menace pour leur emploi et pour leurs conditions de travail. "
     "Le cours rapproche explicitement cette peur de celle que suscite "
     "aujourd’hui l’intelligence artificielle."),
'ch8-aut195-4': f(niv='comprendre', sp='c8-18', b=3385,
 exp="L’estimation d’Osborne et Frey porte sur les tâches techniquement "
     "automatisables, non sur les emplois qui disparaîtraient. La distinction "
     "est décisive : un métier est composé de plusieurs tâches, et l’IA en "
     "automatise certaines sans supprimer le métier entier. Les métiers sont "
     "donc le plus souvent reconfigurés plutôt que supprimés.",
 why=["C’est la confusion la plus fréquente : le chiffre ne porte pas sur les "
      "emplois détruits.",
      "La part du tertiaire dans l’emploi est une statistique sans rapport.",
      "La proportion d’entreprises utilisant l’IA est une autre mesure."],
 diss="Exemple du cours : l’IA peut analyser des dossiers et lire des "
      "documents, mais elle ne remplace pas la relation humaine, le conseil ni "
      "l’interaction avec les clients — les salariés peuvent alors consacrer "
      "plus de temps à la relation client."),
}


# =============================================================== questions neuves
NEW = [

# ------------------------------------------- c8-05 Schumpeter, l’innovation
f(id='q8-n01', sp='c8-05', niv='comprendre', type='qcm', b=754,
  q="En quoi consiste la première rupture de Schumpeter avec l’analyse "
    "néoclassique ?",
  opts=["Il abandonne l’hypothèse de rationalité des agents",
        "Il déplace l’analyse de l’équilibre vers la dynamique : ce qui "
        "caractérise le capitalisme n’est pas sa capacité à atteindre un "
        "équilibre mais sa capacité à se transformer sans cesse",
        "Il refuse de raisonner en termes de prix",
        "Il nie l’existence de la concurrence"],
  ans=1,
  why=["La rationalité des agents n’est pas la cible de sa critique.",
       "Schumpeter ne refuse pas l’analyse des prix : il la juge "
       "insuffisante.",
       "Il réévalue la concurrence, il ne la nie pas."],
  exp="Chez les marginalistes, le raisonnement central montre comment les "
      "marchés tendent vers un équilibre assurant l’efficacité. Schumpeter "
      "considère que cette lecture passe à côté de l’essentiel : le "
      "capitalisme est un système en mouvement, instable, traversé par des "
      "ruptures et fondé sur des transformations successives de la "
      "production. L’économie devient une théorie de l’évolution.",
  diss="Formule à retenir : le capitalisme ne doit pas être pensé comme un "
       "système stable qui tend vers l’équilibre, mais comme un système "
       "dynamique dont la logique profonde est le changement."),

f(id='q8-n02', sp='c8-05', niv='connaitre', type='qcmm', b=800,
  q="Quelles formes d’innovation Schumpeter distingue-t-il dans « Théorie de "
    "l’évolution économique » (1912) ? (plusieurs réponses)",
  opts=["L’innovation de produit : un nouveau bien ou une nouvelle qualité de "
        "bien",
        "L’innovation de procédé : une nouvelle méthode de production",
        "L’innovation de débouchés : un nouveau marché, une nouvelle "
        "clientèle, une nouvelle zone géographique",
        "L’innovation organisationnelle : une nouvelle organisation de la "
        "production ou une nouvelle combinaison des facteurs",
        "L’innovation financière : un nouveau produit bancaire"],
  ans=[0, 1, 2, 3],
  why=["Exacte : elle permet de se différencier et de créer une nouvelle "
       "demande.",
       "Exacte : mécanisation, automatisation, rationalisation productive.",
       "Exacte : l’innovation peut donc être commerciale et géographique.",
       "Exacte : l’innovation peut être institutionnelle et "
       "organisationnelle, pas seulement technique.",
       "L’innovation financière ne figure pas dans la liste du cours, qui "
       "retient en revanche les nouvelles sources de matières premières."],
  exp="Le moyen mnémotechnique donné par le cours est DEPOB : débouchés, "
      "énergie, procédé, organisation, biens et services. L’essentiel est "
      "l’idée de « nouvelle combinaison » : innover ne signifie pas "
      "nécessairement inventer à partir de rien, mais réaliser une nouvelle "
      "combinaison des ressources existantes."),

f(id='q8-n03', sp='c8-05', niv='appliquer', type='assoc', b=843,
  q="Associez chaque dimension de la diffusion de l’automobile au type "
    "d’innovation qu’elle illustre.",
  ans=[["Nouveaux usages : trajets individuels, taxis, ambulances, livraisons, bus", "Innovation de débouchés"],
       ["Essence, pétrole, stations-service, approvisionnement énergétique", "Innovation d’énergie et d’infrastructures"],
       ["La chaîne de montage de Ford et son convoyeur", "Innovation de procédé"],
       ["Sidérurgie, chimie, équipements, garages, assurances, tourisme", "Biens et services induits : une grappe d’innovations"]],
  exp="L’exemple montre qu’une innovation n’apparaît jamais isolément : "
      "l’automobile transforme tout un système économique, social et "
      "technique. Le cours ajoute les transformations institutionnelles : "
      "premiers signaux routiers et panneaux de limitation de vitesse en "
      "1902, tentative d’unification internationale à Genève en 1909, "
      "panneaux de sens unique et de sens interdit en 1928, salon de "
      "l’automobile inauguré en 1889 mais réellement lancé en 1902.",
  diss="Le cours avertit toutefois : il ne faut pas attribuer cet exemple à "
       "Schumpeter lui-même ; c’est une illustration pédagogique de sa "
       "typologie."),

f(id='q8-n04', sp='c8-05', niv='comprendre', type='qcm', b=892,
  q="Comment Schumpeter définit-il l’entrepreneur ?",
  opts=["Le propriétaire du capital de l’entreprise",
        "Celui qui introduit du nouveau, rompt avec la routine, prend des "
        "risques et transforme l’organisation productive : un agent de "
        "rupture, non un simple gestionnaire",
        "Le gestionnaire chargé de la coordination quotidienne",
        "L’actionnaire majoritaire qui nomme les dirigeants"],
  ans=1,
  why=["L’entrepreneur schumpétérien ne se confond pas avec le propriétaire "
       "du capital : le cours est explicite sur ce point.",
       "Le gestionnaire ordinaire reproduit une activité existante : c’est "
       "exactement ce que l’entrepreneur n’est pas.",
       "L’actionnaire relève du capitalisme actionnarial, étudié plus loin."],
  exp="Cette précision permet de distinguer l’entreprise routinière de "
      "l’entreprise innovante. Chez Schumpeter, l’entreprise n’est plus "
      "seulement une unité de production : elle devient un espace de "
      "transformation, un centre de décision stratégique et le support "
      "institutionnel de l’innovation.",
  diss="Le cours cite aussi Weber pour éclairer l’autorité de l’entrepreneur : "
       "le pouvoir peut reposer sur le charisme, la capacité à convaincre, à "
       "entraîner et fédérer — et non seulement sur la propriété."),

f(id='q8-n05', sp='c8-05', niv='comprendre', type='qcm', b=920,
  q="Que désigne exactement la destruction créatrice ?",
  opts=["La faillite des entreprises mal gérées en période de crise",
        "Le mécanisme par lequel une innovation crée une activité nouvelle "
        "tout en rendant obsolètes des techniques, des entreprises, des "
        "métiers et des structures productives",
        "La destruction volontaire de capital pour relancer l’investissement",
        "La disparition des petites entreprises au profit des grandes"],
  ans=1,
  why=["Les faillites conjoncturelles ne sont pas le mécanisme visé : la "
       "destruction créatrice est le fonctionnement ordinaire du capitalisme.",
       "Aucune destruction volontaire de capital n’est en cause.",
       "La concentration est une conséquence possible, non la définition."],
  exp="Le progrès capitaliste est donc conflictuel : il crée de la richesse "
      "mais détruit aussi des positions acquises. Le cours donne trois "
      "exemples types : une nouvelle technologie remplace une ancienne, une "
      "nouvelle organisation productive élimine les formes moins efficaces, un "
      "nouveau produit marginalise les biens anciens.",
  diss="Exemples contemporains cités : l’automobile remplaçant les activités "
       "liées au cheval, le numérique remplaçant certaines tâches "
       "administratives, les plateformes bouleversant le commerce "
       "traditionnel."),

f(id='q8-n06', sp='c8-05', niv='comprendre', type='vf', b=839,
  q="Chez Schumpeter, innover signifie nécessairement inventer quelque chose "
    "à partir de rien.",
  ans=False,
  exp="L’innovation consiste souvent à réaliser une nouvelle combinaison des "
      "ressources existantes : une nouvelle combinaison des facteurs de "
      "production, des ressources ou des formes d’organisation. C’est "
      "précisément pourquoi l’innovation organisationnelle et l’innovation de "
      "débouchés comptent autant que l’invention technique.",
  diss="Cette définition large est ce qui permet d’analyser comme des "
       "innovations le factory system, la chaîne de montage de Ford ou le "
       "juste-à-temps de Toyota."),

f(id='q8-n07', sp='c8-05', niv='raisonner', type='courte', b=905,
  q="Pourquoi l’entreprise est-elle, chez Schumpeter, le lieu stratégique de "
    "l’innovation ?",
  ans={'modele': "Parce que l’innovation n’est pas un mécanisme impersonnel "
       "produit par le marché : elle est portée par l’entrepreneur "
       "innovateur, et c’est au sein de l’entreprise qu’elle se réalise. "
       "L’entreprise n’est donc plus seulement une unité de production où "
       "l’on combine travail et capital : elle devient un espace de "
       "transformation, un centre de décision stratégique et le support "
       "institutionnel de l’innovation. L’entreprise innovante modifie les "
       "produits, transforme les procédés, crée de nouveaux marchés et "
       "reconfigure les rapports de concurrence : elle ne s’adapte pas au "
       "marché, elle le bouleverse.",
       'cles': [{'f': ['entrepreneur', 'porte', 'incarne'],
                 'l': 'l’innovation est portée par l’entrepreneur'},
                {'f': ['pas seulement', 'unite de production', 'transformation', 'strategique'],
                  'l': 'l’entreprise devient un espace de transformation'},
                {'f': ['bouleverse', 'concurrence', 'nouveau marche'],
                 'l': 'elle bouleverse le marché au lieu de s’y adapter'}]},
  exp="C’est ce renversement qui conduit directement à la destruction "
      "créatrice : si l’entreprise innovante transforme le marché, elle rend "
      "obsolètes les positions acquises."),

# ----------------------------- c8-06 monopole temporaire, grappes, cycles
f(id='q8-n08', sp='c8-06', niv='raisonner', type='qcm', b=937,
  q="Quelle est la deuxième rupture de Schumpeter avec la théorie standard ?",
  opts=["Il montre que la concurrence pure et parfaite est impossible en "
        "pratique",
        "Il réhabilite le monopole temporaire : laisser à l’innovateur une "
        "position dominante provisoire peut être plus favorable à l’innovation "
        "que la concurrence parfaite",
        "Il défend le monopole permanent comme structure optimale",
        "Il affirme que la concurrence détruit toujours l’innovation"],
  ans=1,
  why=["La question n’est pas la faisabilité de la CPP mais son caractère "
       "souhaitable pour l’innovation.",
       "Le cours précise explicitement que Schumpeter ne défend pas le "
       "monopole permanent : il défend un avantage provisoire.",
       "La concurrence stimule aussi l’innovation : l’affirmation est trop "
       "absolue."],
  exp="L’argument est économique : l’innovation coûte cher, elle est risquée, "
      "elle exige des investissements. Si l’entreprise innovante est copiée "
      "instantanément, elle ne peut rentabiliser ni ses dépenses de recherche, "
      "ni ses prises de risque, ni ses efforts d’organisation. D’où le rôle du "
      "brevet, qui protège juridiquement l’innovation, empêche la copie "
      "immédiate et permet un surprofit temporaire : la rente d’innovation.",
  diss="Cette rente n’est pas un privilège : c’est une incitation à innover. "
       "Argument à mobiliser dans tout sujet sur la politique de la "
       "concurrence."),

f(id='q8-n09', sp='c8-06', niv='comprendre', type='qcm', b=974,
  q="Qu’appelle-t-on une grappe d’innovations ?",
  opts=["Un ensemble de brevets déposés par une même entreprise",
        "Le fait qu’une grande innovation entraîne des innovations "
        "secondaires, des adaptations techniques, des perfectionnements, de "
        "nouveaux secteurs et des transformations organisationnelles",
        "La concentration géographique des entreprises innovantes",
        "La succession régulière d’innovations dans un même secteur"],
  ans=1,
  why=["Un portefeuille de brevets n’est pas une grappe.",
       "La concentration spatiale est un autre phénomène, celui des "
       "districts.",
       "La régularité est précisément ce que Schumpeter récuse : les "
       "innovations apparaissent par vagues."],
  exp="Une innovation majeure comme l’automobile entraîne garages, "
      "stations-service, routes adaptées, signalisation, assurance, mécanique "
      "spécialisée, nouveaux matériaux et nouvelles infrastructures. Le cours "
      "en tire l’opposition décisive entre innovation fondamentale, qui ouvre "
      "un nouveau cycle, et innovation incrémentale, qui en assure la "
      "diffusion, le perfectionnement et le prolongement.",
  diss="Exemple du cours : l’automobile est l’innovation fondamentale ; les "
       "freins ABS, les boîtes automatiques, les airbags, les GPS intégrés "
       "sont des innovations incrémentales."),

f(id='q8-n10', sp='c8-06', niv='appliquer', type='qcm', b=998,
  q="Les boîtes de vitesses automatiques, les airbags et les GPS intégrés "
    "relèvent de quel type d’innovation ?",
  opts=["D’innovations fondamentales, puisqu’elles créent de nouveaux marchés",
        "D’innovations incrémentales : elles perfectionnent progressivement "
        "une innovation déjà existante",
        "D’innovations de débouchés",
        "D’innovations organisationnelles"],
  ans=1,
  why=["Une innovation fondamentale ouvre un nouveau cycle par une rupture "
       "majeure : ce n’est pas le cas ici.",
       "L’innovation de débouchés porte sur l’accès à un nouveau marché.",
       "L’innovation organisationnelle porte sur la combinaison des facteurs "
       "ou la structure de l’entreprise."],
  exp="L’innovation incrémentale ne bouleverse pas le système productif : "
      "elle améliore les performances, réduit les coûts, adapte la "
      "technologie à de nouveaux usages ou optimise l’organisation existante. "
      "Elle ne crée pas un nouveau secteur à elle seule, mais elle permet de "
      "diffuser, stabiliser et rentabiliser une innovation fondamentale.",
  diss="Formule à retenir absolument : l’innovation fondamentale ouvre un "
       "nouveau cycle, l’innovation incrémentale en assure la diffusion et le "
       "prolongement."),

f(id='q8-n11', sp='c8-06', niv='comprendre', type='ordre', b=1085,
  q="Remettez dans l’ordre le mécanisme par lequel l’innovation engendre un "
    "cycle long chez Schumpeter.",
  ans=["Une innovation majeure apparaît",
       "Elle entraîne d’autres innovations complémentaires et forme une "
       "grappe",
       "Cette grappe restructure durablement l’économie et ouvre une phase "
       "d’expansion longue",
       "Puis la vague d’innovation se banalise, se diffuse complètement ou "
       "s’épuise",
       "Les surprofits diminuent, la croissance ralentit : la phase "
       "descendante commence"],
  exp="Un cycle de Kondratiev dure 50 à 60 ans, décomposé en deux phases "
      "d’environ 25 à 30 ans chacune. La phase ascendante correspond à la "
      "diffusion des innovations en grappe, la phase descendante à "
      "l’essoufflement du rythme d’innovation, avec des prix qui peuvent "
      "baisser.",
  diss="Le cours ajoute que la première révolution industrielle illustre "
       "parfaitement cette logique : machine à vapeur, textile mécanisé, "
       "charbon, métallurgie et transports forment une grappe associable à la "
       "phase ascendante d’un cycle long."),

f(id='q8-n12', sp='c8-06', niv='appliquer', type='qcm', b=1074,
  q="Comment les trois types de cycles s’articulent-ils, selon le cours ?",
  opts=["Ils sont indépendants et s’excluent mutuellement",
        "Ils s’emboîtent : des cycles courts de Kitchin à l’intérieur d’un "
        "cycle de Juglar, plusieurs Juglar à l’intérieur d’un Kondratiev",
        "Ils se succèdent historiquement, Kitchin au XIXᵉ siècle puis "
        "Kondratiev au XXᵉ",
        "Ils ont tous la même cause : les variations de stocks"],
  ans=1,
  why=["Le cours insiste précisément sur leur superposition.",
       "Il n’y a pas de succession historique entre eux : ils coexistent.",
       "Les causes diffèrent : stocks, investissement et crédit, grappes "
       "d’innovations."],
  exp="Le capitalisme est traversé par plusieurs temporalités à la fois : une "
      "temporalité courte liée aux stocks et aux ajustements conjoncturels, "
      "une temporalité moyenne liée à l’investissement et au crédit, une "
      "temporalité longue liée aux transformations structurelles issues des "
      "innovations majeures.",
  diss="Chez Schumpeter, l’innovation explique surtout les cycles longs : "
       "c’est la précision qui évite de tout attribuer à l’innovation."),

f(id='q8-n13', sp='c8-06', niv='raisonner', type='courte', b=1146,
  q="En quoi la voiture électrique et la voiture autonome peuvent-elles être "
    "lues comme de futures grappes d’innovations ?",
  ans={'modele': "Comme l’automobile thermique en son temps, elles entraînent "
       "dans leur sillage tout un ensemble d’innovations complémentaires et "
       "d’adaptations institutionnelles. La voiture électrique suppose le "
       "développement des batteries, l’essor des bornes de recharge, une "
       "reconfiguration des filières énergétiques, de nouveaux enjeux liés aux "
       "métaux stratégiques et une adaptation des réseaux électriques. La "
       "voiture autonome exige des progrès en capteurs, en intelligence "
       "artificielle, en logiciels embarqués, en cartographie, mais aussi en "
       "réglementation, en responsabilité juridique et en infrastructures "
       "connectées. On retrouve donc la logique schumpétérienne : une "
       "innovation centrale ne reste jamais isolée.",
       'cles': [{'f': ['batterie', 'borne', 'recharge', 'reseau', 'metaux'],
                 'l': 'électrique : batteries, bornes, réseaux, métaux'},
                {'f': ['capteur', 'ia', 'logiciel', 'cartographie'],
                 'l': 'autonome : capteurs, IA, logiciels, cartographie'},
                {'f': ['reglementation', 'juridique', 'institutionnel'],
                 'l': 'et des adaptations réglementaires et juridiques'},
                {'f': ['grappe', 'jamais isolee', 'complementaire'],
                 'l': 'une grappe : l’innovation n’est jamais isolée'}]},
  exp="Cette ouverture contemporaine montre l’actualité de la grille "
      "schumpétérienne : elle permet d’analyser une transition technologique "
      "en cours, et non seulement l’histoire."),

# -------------------------------- c8-07 limites du capitalisme, taylorisme
f(id='q8-n14', sp='c8-07', niv='raisonner', type='qcm', b=1118,
  q="Pourquoi, selon Schumpeter, le succès du capitalisme peut-il le "
    "fragiliser ?",
  opts=["Parce que la concurrence internationale s’intensifie",
        "Parce qu’à mesure que les entreprises grossissent et que les marchés "
        "se concentrent, la bureaucratie s’installe et l’innovation devient "
        "routinière : l’entrepreneur innovateur s’efface au profit des "
        "oligopoles",
        "Parce que les salaires augmentent plus vite que la productivité",
        "Parce que les consommateurs se lassent des nouveautés"],
  ans=1,
  why=["La concurrence internationale n’est pas le mécanisme invoqué.",
       "Le partage salaires-profits n’est pas l’argument de Schumpeter.",
       "La demande de nouveautés n’est pas en cause."],
  exp="L’évolution est paradoxale : le capitalisme triomphe, mais ce triomphe "
      "affaiblit ce qui faisait sa force initiale. Plus il se rationalise, "
      "plus la gestion remplace l’intuition, plus la grande firme remplace "
      "l’entrepreneur, plus l’innovation s’intègre dans des structures "
      "lourdes. Le système risque alors de perdre sa spontanéité créatrice et "
      "d’étouffer la fonction entrepreneuriale.",
  diss="Conclusion schumpétérienne à citer : le capitalisme peut être miné par "
       "sa propre réussite, car la grande entreprise bureaucratique tend à "
       "remplacer l’entrepreneur innovateur."),

f(id='q8-n15', sp='c8-07', niv='comprendre', type='qcm', b=1287,
  q="Qu’appelle-t-on la « flânerie systématique » observée par Taylor, et "
    "comment l’explique-t-il ?",
  opts=["Une paresse naturelle des ouvriers, qu’il faut discipliner",
        "Un ralentissement volontaire de la production, rationnel du point de "
        "vue de l’ouvrier : produire plus peut entraîner une hausse des "
        "cadences sans garantie d’augmentation de salaire",
        "Les temps morts dus à une mauvaise disposition des machines",
        "L’absentéisme lié à la pénibilité du travail"],
  ans=1,
  why=["Le cours insiste au contraire sur le caractère rationnel du "
       "comportement.",
       "Les temps morts seront l’objet de la chaîne de montage de Ford.",
       "L’absentéisme est une conséquence ultérieure de la parcellisation."],
  exp="Dans l’organisation traditionnelle, les ouvriers qualifiés maîtrisent "
      "l’ensemble du processus et contrôlent leur rythme : le travail échappe "
      "en partie au contrôle de l’entreprise. Les ouvriers se limitent "
      "volontairement parce qu’ils anticipent une hausse des cadences sans "
      "contrepartie salariale, voire une dégradation des conditions de "
      "travail. Le problème est donc organisationnel.",
  diss="Cette analyse justifie les deux divisions du travail tayloriennes et "
       "le salaire différentiel aux pièces, qui fait de la rémunération un "
       "outil disciplinaire."),

f(id='q8-n16', sp='c8-07', niv='appliquer', type='assoc', b=1303,
  q="Associez chaque élément du taylorisme à son contenu.",
  ans=[["La division horizontale", "La parcellisation : chaque ouvrier réalise une opération élémentaire, répétitive et spécialisée"],
       ["La division verticale", "La séparation de la conception — ingénieurs, bureau des méthodes — et de l’exécution : cols blancs contre cols bleus"],
       ["Le salaire différentiel aux pièces", "Un outil disciplinaire : salaire plus élevé si la norme est respectée, plus faible sinon"],
       ["Le double avantage recherché", "Des gains de temps par la spécialisation et un meilleur contrôle du travail par le contremaître"]],
  exp="L’ouvrier perd toute autonomie : il n’a plus à penser son travail, "
      "seulement à l’exécuter. Taylor considère en effet que la motivation "
      "principale du travailleur est économique, d’où le rôle central de la "
      "rémunération aux pièces.",
  diss="Savoir distinguer les deux divisions est indispensable : la "
       "parcellisation porte sur le découpage des tâches, la division "
       "verticale sur la répartition du pouvoir de décision."),

f(id='q8-n17', sp='c8-07', niv='raisonner', type='ordre', b=1328,
  q="Remettez dans l’ordre l’enchaînement par lequel les limites sociales du "
    "taylorisme deviennent des limites économiques.",
  ans=["La parcellisation entraîne monotonie, fatigue et perte de sens",
       "L’ouvrier devient étranger à son travail : Georges Friedmann parle de "
       "« travail en miettes »",
       "Apparaissent alors turn-over élevé, absentéisme et malfaçons",
       "Ces dysfonctionnements engendrent des coûts de recrutement, de "
       "formation, de remplacement et de retouches",
       "Ces coûts annulent une partie des gains de la spécialisation"],
  exp="C’est cet enchaînement qui explique le passage au fordisme : Ford "
      "répond au turn-over par la hausse des salaires, et le toyotisme "
      "répondra plus tard aux malfaçons par la recherche du zéro défaut.",
  diss="Enchaînement très rentable : il montre qu’une organisation du travail "
       "socialement coûteuse finit par être économiquement inefficace."),

# ------------------------------------------------- c8-08 fordisme
f(id='q8-n18', sp='c8-08', niv='comprendre', type='qcm', b=1338,
  q="En quoi le convoyeur transforme-t-il l’organisation de la production ?",
  opts=["Il permet aux ouvriers de choisir leur rythme de travail",
        "Les objets se déplacent vers les ouvriers, le rythme est imposé et "
        "les temps morts sont supprimés",
        "Il remplace les ouvriers par des machines automatiques",
        "Il permet de produire plusieurs modèles simultanément"],
  ans=1,
  why=["C’est l’inverse : le rythme est imposé par la chaîne.",
       "Les ouvriers restent indispensables : ce sont les pièces qui "
       "circulent.",
       "Ford produit au contraire un modèle unique, la Ford T."],
  exp="Avant la chaîne, les ouvriers se déplaçaient dans l’atelier ; avec le "
      "convoyeur, ce sont les pièces qui viennent à eux. La production est "
      "accélérée, mais le travail devient plus pénible et plus répétitif, ce "
      "qui explique le fort turn-over auquel Ford répond par les hauts "
      "salaires.",
  diss="Le cours classe explicitement la chaîne de montage parmi les "
       "innovations de procédé au sens de Schumpeter."),

f(id='q8-n19', sp='c8-08', niv='raisonner', type='qcm', b=1366,
  q="Pourquoi Ford porte-t-il les salaires de 2,5 à 5 dollars par jour ?",
  opts=["Uniquement pour soutenir la demande de ses propres véhicules",
        "Pour deux raisons : donner du pouvoir d’achat aux salariés afin "
        "qu’ils achètent la production, et fidéliser une main-d’œuvre exposée "
        "au turn-over en augmentant le coût d’opportunité du départ",
        "Pour se conformer à une réglementation salariale",
        "Pour compenser la suppression des primes d’ancienneté"],
  ans=1,
  why=["La raison de demande est réelle mais partielle : le cours en donne "
       "explicitement deux.",
       "Aucune contrainte réglementaire n’est en cause.",
       "Aucun dispositif de prime supprimé n’est mentionné."],
  exp="Le travail à la chaîne est répétitif, intensif et fatigant : le "
      "turn-over est élevé, et il coûte cher en recrutement, formation et "
      "désorganisation. En payant plus que les autres entreprises, Ford rend "
      "le départ coûteux : quitter Ford, c’est renoncer à un salaire élevé. Le "
      "cours définit le taux de turn-over comme le nombre d’entrées ou de "
      "sorties rapporté à l’effectif total moyen.",
  diss="La double justification — demande et fidélisation — est ce qui fait du "
       "fordisme un système cohérent, articulant production de masse et "
       "consommation de masse."),

f(id='q8-n20', sp='c8-08', niv='appliquer', type='qcm', b=1347,
  q="Quels chiffres le cours retient-il pour illustrer l’effet de la "
    "production de masse chez Ford ?",
  opts=["Une Ford coûte 690 dollars en 1913 et 290 dollars en 1929 ; en 1914, "
        "60 % des voitures produites aux États-Unis sont des Ford",
        "Une Ford coûte 1 000 dollars en 1913 et 500 en 1929",
        "Les ventes de Ford doublent entre 1913 et 1929",
        "Ford produit 60 % des voitures mondiales en 1929"],
  ans=0,
  why=["Ces montants ne correspondent pas aux repères du cours.",
       "Le cours raisonne sur les prix et la part de marché, non sur le "
       "doublement des ventes.",
       "La part de 60 % concerne la production américaine en 1914, non la "
       "production mondiale en 1929."],
  exp="Le mécanisme est clair : la standardisation et la chaîne permettent des "
      "économies d’échelle, donc une baisse du coût moyen, donc une baisse du "
      "prix de vente, donc une hausse de la demande. C’est le cœur du modèle "
      "fordiste.",
  diss="Ces chiffres rendent concret ce que « production de masse » signifie, "
       "et évitent de rester au niveau du vocabulaire."),

f(id='q8-n21', sp='c8-08', niv='raisonner', type='qcmm', b=1376,
  q="Quelles limites le cours attribue-t-il au fordisme ? (plusieurs "
    "réponses)",
  opts=["La rigidité du système",
        "Une production standardisée, peu adaptable à la diversité de la "
        "demande",
        "Un travail répétitif et une faible autonomie",
        "Des conflits sociaux",
        "Des coûts unitaires trop élevés"],
  ans=[0, 1, 2, 3],
  why=["Exacte : c’est la limite que le toyotisme viendra corriger par la "
       "flexibilité.",
       "Exacte : un modèle unique ne répond pas à une demande différenciée.",
       "Exacte : la pénibilité subsiste malgré les hauts salaires.",
       "Exacte : le cours les mentionne explicitement.",
       "C’est l’inverse : le fordisme fait précisément baisser les coûts "
       "unitaires."],
  exp="Formule du cours : le système privilégie la quantité au détriment de la "
      "qualité. C’est précisément ce que le toyotisme, développé après la "
      "Seconde Guerre mondiale, va chercher à corriger."),

# ----------------------------------------------- c8-09 le toyotisme
f(id='q8-n22', sp='c8-09', niv='comprendre', type='qcm', b=1385,
  q="Qu’est-ce que la production en juste-à-temps, ou à flux tendu ?",
  opts=["Produire le plus vite possible pour constituer des stocks de "
        "sécurité",
        "Ne produire que ce qui a été vendu : ce sont les postes en aval de "
        "la production qui déterminent l’amont, à l’inverse du fordisme",
        "Produire en continu, vingt-quatre heures sur vingt-quatre",
        "Livrer les clients dans les délais contractuels"],
  ans=1,
  why=["Le juste-à-temps vise au contraire la réduction des stocks.",
       "La continuité de la production n’est pas le principe en cause.",
       "Le respect des délais de livraison est une conséquence, non la "
       "définition."],
  exp="Le principe est de produire uniquement ce qui est nécessaire, au moment "
      "nécessaire, ce qui réduit les stocks et optimise les flux. "
      "L’inversion du sens de commande — l’aval détermine l’amont — est la "
      "rupture décisive avec le modèle tayloro-fordiste, qui produisait en "
      "amont puis cherchait à écouler.",
  diss="Le toyotisme répond aux quatre défauts du modèle précédent : "
       "surproduction, stocks, défauts et rigidité."),

f(id='q8-n23', sp='c8-09', niv='connaitre', type='qcm', b=1386,
  q="Quelle est la règle des cinq zéros du Toyota Production System ?",
  opts=["Zéro stock, zéro délai, zéro panne, zéro défaut, zéro papier",
        "Zéro stock, zéro chômage, zéro accident, zéro déchet, zéro conflit",
        "Zéro défaut, zéro retard, zéro gaspillage, zéro hiérarchie, zéro "
        "contrôle",
        "Zéro stock, zéro intérim, zéro heure supplémentaire, zéro panne, "
        "zéro défaut"],
  ans=0,
  why=["Chômage, accidents, déchets et conflits ne figurent pas dans la "
       "règle.",
       "L’absence de hiérarchie et de contrôle contredirait l’organisation "
       "réelle du système.",
       "Les formes d’emploi ne font pas partie de cette règle de production."],
  exp="Les cinq zéros traduisent une logique générale d’élimination des "
      "gaspillages. Ils complètent le juste-à-temps : réduire les stocks, "
      "supprimer les délais, éviter les pannes, atteindre le zéro défaut et "
      "limiter la paperasse.",
  diss="Attention à la cohérence de l’ensemble : les cinq zéros n’ont de sens "
       "que couplés à la polyvalence des opérateurs et au contrôle continu de "
       "la qualité."),


f(id='q8-n24', sp='c8-09', niv='comprendre', type='qcm', b=1398,
  q="Qu’appelle-t-on l’« autonomation » chez Toyota ?",
  opts=["L’automatisation complète de la chaîne, sans intervention humaine",
        "Un néologisme croisant autonomie et automatisation : les opérateurs "
        "travaillent en équipes semi-autonomes et surveillent le bon "
        "fonctionnement des machines, lesquelles s’arrêtent automatiquement en "
        "cas de problème",
        "L’autonomie laissée aux cadres dans l’organisation des équipes",
        "L’indépendance juridique des sous-traitants de Toyota"],
  ans=1,
  why=["Il ne s’agit pas de supprimer l’intervention humaine mais de la "
       "redéfinir.",
       "L’autonomie visée est celle des opérateurs, non des cadres.",
       "Les relations de sous-traitance ne sont pas l’objet de ce terme."],
  exp="Le toyotisme transforme le rôle du travailleur : polyvalence, travail "
      "en équipe, responsabilité, et jusqu’à la possibilité d’arrêter la "
      "chaîne. L’ouvrier, désormais appelé opérateur, devient acteur de la "
      "qualité. S’y ajoute le kaizen : les opérateurs sont sollicités pour "
      "proposer des améliorations de leur poste de production.",
  diss="C’est l’inverse exact de la division verticale taylorienne : "
       "l’opérateur est de nouveau associé à la conception."),

f(id='q8-n25', sp='c8-09', niv='raisonner', type='qcm', b=1391,
  q="Pourquoi la recherche du zéro défaut est-elle décisive dans une chaîne "
    "de production longue ?",
  opts=["Parce que les clients exigent des garanties contractuelles",
        "Parce que même un faible taux d’erreur à chaque étape entraîne "
        "beaucoup de défauts sur le produit final",
        "Parce que les contrôles finaux coûtent cher",
        "Parce que les normes industrielles l’imposent"],
  ans=1,
  why=["Les exigences commerciales existent, mais l’argument du cours est "
       "arithmétique.",
       "Le coût du contrôle final est une conséquence du problème, non son "
       "origine.",
       "Aucune contrainte normative n’est invoquée."],
  exp="L’accumulation des petits taux d’erreur le long de la chaîne explique "
      "pourquoi Toyota met en place un contrôle continu plutôt qu’un contrôle "
      "en fin de chaîne, et pourquoi chaque opérateur devient responsable de "
      "la qualité à son poste.",
  diss="La véritable rupture du toyotisme tient là : la qualité devient un "
       "objectif de production, et non une vérification finale."),

f(id='q8-n26', sp='c8-09', niv='raisonner', type='courte', b=1401,
  q="Le toyotisme est-il une rupture ou un prolongement du taylorisme ?",
  ans={'modele': "C’est les deux. Le Toyota Production System reprend "
       "certains principes tayloriens, notamment la recherche d’une forte "
       "productivité avec chronométrage des tâches. Mais il veut en corriger "
       "les défauts : à la quantité il substitue la qualité, à la rigidité la "
       "flexibilité, aux stocks le juste-à-temps, à la parcellisation la "
       "polyvalence et le travail en équipes semi-autonomes. Là où le "
       "taylorisme séparait conception et exécution, le kaizen associe au "
       "contraire les opérateurs à l’amélioration de leur poste. La "
       "continuité porte donc sur l’objectif — l’efficacité productive — et la "
       "rupture sur les moyens.",
       'cles': [{'f': ['reprend', 'productivite', 'chronometr', 'continuite'],
                 'l': 'continuité : recherche de productivité et chronométrage'},
                {'f': ['qualite', 'quantite', 'zero defaut'],
                 'l': 'rupture : la qualité plutôt que la quantité'},
                {'f': ['polyvalence', 'equipe', 'kaizen', 'autonomation'],
                 'l': 'polyvalence, équipes semi-autonomes, kaizen'},
                {'f': ['flexib', 'juste a temps', 'stock', 'flux tendu'],
                 'l': 'flexibilité et juste-à-temps contre rigidité et stocks'}]},
  exp="Cette réponse nuancée est celle que le cours formule explicitement en "
      "conclusion : « le TPS reprend certains principes tayloriens mais veut "
      "en corriger les défauts »."),

f(id='q8-n27', sp='c8-09', niv='connaitre', type='assoc', b=1384,
  q="Associez chaque notion du toyotisme à son contenu.",
  ans=[["Le juste-à-temps", "Ne produire que ce qui est nécessaire, au moment nécessaire : l’aval commande l’amont"],
       ["Les cinq zéros", "Zéro stock, zéro délai, zéro panne, zéro défaut, zéro papier"],
       ["L’autonomation", "Des équipes semi-autonomes surveillant des machines qui s’arrêtent en cas de problème"],
       ["Le kaizen", "L’amélioration permanente : les opérateurs proposent des améliorations de leur poste"]],
  exp="Les quatre notions forment un système cohérent : sans polyvalence et "
      "sans implication des opérateurs, le juste-à-temps serait impraticable, "
      "car la moindre panne ou le moindre défaut interromprait le flux faute "
      "de stock tampon.",
  diss="C’est la fragilité du modèle : la réduction des stocks rend le système "
       "très sensible aux ruptures d’approvisionnement."),

f(id='q8-n28', sp='c8-09', niv='appliquer', type='vf', b=1381,
  q="Dans le modèle tayloro-fordiste, la production est commandée par l’amont, "
    "alors que dans le toyotisme elle est commandée par l’aval.",
  ans=True,
  exp="C’est l’inversion décisive. Le tayloro-fordisme produit en grande "
      "série puis cherche à écouler, ce qui engendre surproduction, stocks, "
      "défauts et rigidité. Le toyotisme ne produit que ce qui est vendu : "
      "les postes situés en aval de la production déterminent l’amont. D’où "
      "la réduction des stocks et l’optimisation des flux.",
  diss="Cette inversion explique aussi la vulnérabilité du flux tendu, que "
       "les ruptures d’approvisionnement récentes ont mise en évidence."),

# ------------------------------- c8-10 / c8-11 entrepreneur, managers
f(id='q8-n29', sp='c8-10', niv='comprendre', type='qcm', b=1638,
  q="Qu’est-ce qui caractérise le capitalisme entrepreneurial ?",
  opts=["La séparation entre propriété et direction",
        "La confusion entre propriété et pouvoir : l’entrepreneur cumule la "
        "propriété du capital, la direction et parfois l’activité productive "
        "elle-même",
        "La domination des marchés financiers",
        "La professionnalisation de la gestion"],
  ans=1,
  why=["La séparation définit le capitalisme managérial, qui lui succède.",
       "La domination financière caractérise le capitalisme actionnarial.",
       "La professionnalisation de la gestion marque précisément la fin du "
       "capitalisme entrepreneurial."],
  exp="Aux débuts du capitalisme industriel, l’entreprise est petite, peu "
      "complexe, centrée sur une seule personne, et souvent familiale, "
      "transmise de génération en génération. Il n’y a pas toujours de "
      "séparation entre patrimoine personnel et entreprise : l’entrepreneur "
      "engage ses biens propres, et ce risque économique renforce son pouvoir.",
  diss="Trois formes successives à retenir : capitalisme entrepreneurial, "
       "managérial, actionnarial. Le pouvoir se déplace de l’entrepreneur aux "
       "managers puis aux actionnaires."),

f(id='q8-n30', sp='c8-10', niv='raisonner', type='qcm', b=1693,
  q="Quelle critique le cours adresse-t-il, avec Galluzzo, au mythe de "
    "l’entrepreneur ?",
  opts=["L’entrepreneur ne prend en réalité aucun risque",
        "Le récit du génie solitaire parti de rien est trompeur : "
        "l’innovation est collective, les salariés, ingénieurs et chercheurs "
        "y jouent un rôle essentiel, l’État finance souvent les innovations, "
        "et le succès dépend aussi du capital social et des réseaux",
        "Les entrepreneurs sont moins efficaces que les managers",
        "L’entrepreneuriat ne crée pas d’emplois"],
  ans=1,
  why=["Le risque est réel : ce n’est pas ce que la critique met en cause.",
       "La comparaison d’efficacité n’est pas l’objet de cette critique.",
       "La création d’emplois n’est pas en débat ici."],
  exp="Le récit dominant présente l’entrepreneur comme un héros individuel, "
      "réussissant par son seul mérite. Galluzzo montre que la réussite "
      "entrepreneuriale dépend d’un contexte collectif et social. Cette "
      "critique complète celle de Weber et de Schumpeter, qui éclairaient "
      "l’autorité et la fonction de l’entrepreneur sans en faire un mythe.",
  diss="Nuance très utile : elle permet de discuter les politiques de soutien "
       "à l’entrepreneuriat en rappelant le rôle du financement public de "
       "l’innovation."),

f(id='q8-n31', sp='c8-11', niv='comprendre', type='qcm', b=1731,
  q="Quel apport Henri Fayol propose-t-il dans « Administration industrielle "
    "et générale » (1916) ?",
  opts=["Il décrit la division du travail en atelier",
        "Il montre que la gestion peut être organisée rationnellement autour "
        "de fonctions précises : prévoir, organiser, commander, coordonner, "
        "contrôler",
        "Il analyse la séparation entre propriété et contrôle",
        "Il théorise la relation d’agence"],
  ans=1,
  why=["La division du travail en atelier est l’objet du taylorisme.",
       "La séparation propriété / contrôle est analysée par Berle et Means en "
       "1932.",
       "La théorie de l’agence est celle de Jensen et Meckling, en 1976."],
  exp="Avant Fayol, diriger une entreprise relevait surtout de l’expérience "
      "personnelle ou du talent individuel. Fayol rompt avec cette vision : "
      "la gestion peut devenir une science organisée, avec des règles "
      "générales applicables à toutes les entreprises. La direction devient "
      "une compétence enseignable, d’où le développement des écoles de "
      "commerce et des formations à la gestion.",
  diss="Idée clé du cours : la direction de l’entreprise devient une "
       "compétence spécifique, distincte de la simple possession du capital."),

f(id='q8-n32', sp='c8-11', niv='comprendre', type='qcm', b=1752,
  q="Que montrent Berle et Means dans « The Modern Corporation and Private "
    "Property » (1932) ?",
  opts=["Que la propriété privée est une condition de l’efficacité productive",
        "Que le capital est dispersé entre de nombreux actionnaires qui n’ont "
        "ni le temps, ni les compétences, ni l’information pour gérer "
        "l’entreprise : ils délèguent donc le pouvoir aux managers",
        "Que les managers sont moins efficaces que les propriétaires",
        "Que les grandes entreprises doivent être nationalisées"],
  ans=1,
  why=["La défense de la propriété privée n’est pas leur propos.",
       "Ils constatent un déplacement du pouvoir, sans porter ce jugement "
       "d’efficacité.",
       "Aucune recommandation de nationalisation n’est en cause."],
  exp="Il en résulte une transformation majeure : ceux qui possèdent ne "
      "dirigent plus, et ceux qui dirigent ne possèdent pas nécessairement. "
      "Le pouvoir effectif se déplace vers les managers. C’est le fondement "
      "du capitalisme managérial.",
  diss="À compléter immédiatement par Galbraith : la dispersion du capital ne "
       "suffit pas à expliquer cette domination, qui repose aussi sur la "
       "maîtrise de l’information et des compétences."),

f(id='q8-n33', sp='c8-11', niv='comprendre', type='qcm', b=1763,
  q="Qu’est-ce que la technostructure chez Galbraith (« Le Nouvel État "
    "industriel », 1967) ?",
  opts=["L’ensemble des actionnaires institutionnels d’une grande firme",
        "L’ensemble des acteurs — dirigeants, cadres, ingénieurs, experts — "
        "qui participent à la direction effective de l’entreprise et "
        "détiennent le pouvoir réel grâce à la maîtrise des connaissances",
        "L’organigramme formel de l’entreprise",
        "Le service de recherche et développement"],
  ans=1,
  why=["Les actionnaires institutionnels relèvent du capitalisme "
       "actionnarial.",
       "L’organigramme est une représentation formelle, non un groupe "
       "détenant le pouvoir réel.",
       "La R&D n’est qu’une fonction parmi d’autres."],
  exp="Idée clé : le pouvoir dans l’entreprise repose désormais sur la "
      "maîtrise de l’information et des compétences, et non plus uniquement "
      "sur la propriété du capital. Les grandes entreprises modernes sont "
      "devenues si complexes que les actionnaires ne peuvent plus réellement "
      "les contrôler.",
  diss="Conséquence que le cours souligne : une gouvernance managériale "
       "privilégie la stabilité, l’innovation et la planification de long "
       "terme — argument à opposer au court-termisme actionnarial."),

f(id='q8-n34', sp='c8-11', niv='comprendre', type='qcm', b=1774,
  q="Que désigne la « main visible des managers » chez Chandler (1977) ?",
  opts=["Le contrôle des dirigeants par les actionnaires",
        "Le fait que, dans les grandes entreprises, la coordination des "
        "activités économiques repose sur l’organisation interne des firmes "
        "plutôt que sur le marché",
        "La transparence imposée aux grandes entreprises",
        "L’intervention de l’État dans l’industrie"],
  ans=1,
  why=["Le contrôle des dirigeants est l’objet de la gouvernance "
       "d’entreprise.",
       "La transparence est une obligation d’information, sans rapport.",
       "L’État n’est pas en cause dans cette analyse."],
  exp="Chandler, historien de l’économie, explique que le succès de "
      "l’économie américaine après 1840 vient de sa capacité à développer des "
      "firmes de grande taille, intégrées verticalement et horizontalement, à "
      "la recherche d’économies d’échelle, d’une meilleure coordination et "
      "d’une réduction de l’incertitude. La « main visible » des managers "
      "remplace donc partiellement la « main invisible » du marché.",
  diss="À relier aux formes d’organisation : la forme U, centralisée et "
       "structurée par fonctions, et la forme M, multidivisionnelle et "
       "décentralisée par produit ou zone géographique."),

f(id='q8-n35', sp='c8-11', niv='appliquer', type='assoc', b=1777,
  q="Associez chaque forme d’organisation des grandes entreprises à sa "
    "description.",
  ans=[["La forme U (unitaire)", "Une organisation centralisée, structurée par fonctions : production, finance, ressources humaines"],
       ["La forme M (multidivisionnelle)", "Une organisation décentralisée en unités autonomes par produit ou zone géographique"],
       ["Ce que conserve la forme M", "Une direction stratégique centrale, malgré l’autonomie opérationnelle des divisions"],
       ["L’intérêt de la forme M", "Gérer des entreprises complexes et diversifiées"]],
  exp="La forme M permet de gérer des entreprises complexes et diversifiées : "
      "chaque division dispose d’une autonomie opérationnelle tandis que la "
      "stratégie reste centralisée. La montée du capitalisme managérial "
      "s’accompagne ainsi d’une transformation des structures "
      "organisationnelles.",
  diss="Savoir citer les deux formes montre que l’on relie la gouvernance à "
       "l’organisation concrète, et pas seulement aux rapports de pouvoir."),

# -------------------------- c8-12 capitalisme actionnarial, agence
f(id='q8-n36', sp='c8-12', niv='comprendre', type='qcm', b=1788,
  q="Quelles trois dynamiques Henri Bourguinat identifie-t-il pour décrire la "
    "financiarisation ?",
  opts=["Déréglementation, délocalisation, désindustrialisation",
        "Désintermédiation, décloisonnement, déréglementation",
        "Dématérialisation, digitalisation, déréglementation",
        "Décentralisation, déconcentration, déréglementation"],
  ans=1,
  why=["Délocalisation et désindustrialisation relèvent de la mondialisation "
       "productive.",
       "Dématérialisation et digitalisation concernent le numérique.",
       "Décentralisation et déconcentration sont des notions "
       "administratives."],
  exp="Ces trois « D » expliquent que les entreprises accèdent directement "
      "aux marchés financiers et en deviennent dépendantes. De nouveaux "
      "acteurs prennent alors une place centrale : fonds d’investissement, "
      "private equity, investisseurs institutionnels, qui exercent une forte "
      "pression sur la rentabilité financière.",
  diss="La financiarisation est le contexte qui rend possible le retour des "
       "actionnaires : sans elle, la gouvernance managériale n’aurait pas été "
       "remise en cause."),

f(id='q8-n37', sp='c8-12', niv='comprendre', type='qcm', b=1977,
  q="Que décrit la théorie de l’agence de Jensen et Meckling (1976) ?",
  opts=["La relation entre l’entreprise et ses clients",
        "Les contrats par lesquels un principal — l’actionnaire — fait appel "
        "à un agent — le manager — pour exécuter une tâche impliquant une "
        "délégation de pouvoir, dans un contexte d’incertitude et d’asymétrie "
        "d’information",
        "La relation entre l’État et les entreprises publiques",
        "La négociation collective entre employeurs et syndicats"],
  ans=1,
  why=["La relation commerciale n’est pas une relation d’agence au sens de "
       "cette théorie.",
       "La tutelle publique n’est pas l’objet de l’article de 1976.",
       "La négociation collective relève du droit du travail."],
  exp="Deux difficultés apparaissent : une divergence d’intérêts et une "
      "asymétrie d’information. Les managers, mieux informés, peuvent chercher "
      "à maximiser leur pouvoir, leur rémunération ou la croissance de "
      "l’entreprise plutôt que le profit des actionnaires. Cela engendre des "
      "coûts d’agence, essentiellement des coûts de surveillance.",
  diss="D’où les deux familles de réponses : des dispositifs de contrôle "
       "— conseil d’administration, audit — et des dispositifs d’incitation — "
       "stock-options, rémunérations variables."),

f(id='q8-n38', sp='c8-12', niv='connaitre', type='qcm', b=2000,
  q="Que sont les stock-options, et à quoi servent-elles dans la gouvernance "
    "actionnariale ?",
  opts=["Des actions distribuées gratuitement à tous les salariés",
        "Des options d’achat sur des actions attribuées à des salariés, le "
        "plus souvent des cadres, à un prix souvent inférieur à celui du "
        "marché : elles visent à aligner les intérêts des managers sur ceux "
        "des actionnaires",
        "Des obligations convertibles émises par l’entreprise",
        "Une épargne salariale obligatoire"],
  ans=1,
  why=["Elles ne sont pas gratuites et visent le plus souvent les cadres.",
       "Les obligations convertibles sont un instrument de dette, non une "
       "incitation managériale.",
       "L’épargne salariale est un dispositif distinct."],
  exp="Le cours ajoute un avantage fiscal lorsque les actions sont conservées "
      "un certain temps. L’objectif est d’inciter les managers à augmenter la "
      "valeur actionnariale de l’entreprise. Mais ces incitations s’ajoutent "
      "à leur rémunération : Nicholas Bloom, dans « Corporations in the Age of "
      "Inequality » (Harvard Business Review, 2017), constate l’explosion des "
      "écarts de revenus dans les grandes entreprises.",
  diss="Conclusion à retenir : la gouvernance actionnariale, conçue pour "
       "résoudre un problème d’agence, devient elle-même un facteur "
       "d’inégalités."),

f(id='q8-n39', sp='c8-12', niv='comprendre', type='qcm', b=2031,
  q="Quelle est la thèse de Milton Friedman dans « The Social Responsibility "
    "of Business is to Increase its Profits » (1970) ?",
  opts=["L’entreprise doit équilibrer les intérêts de toutes ses parties "
        "prenantes",
        "La seule responsabilité de l’entreprise est de maximiser le profit "
        "pour ses actionnaires ; les dimensions sociales et environnementales "
        "sont secondaires",
        "L’entreprise doit contribuer au financement des politiques "
        "publiques",
        "L’entreprise doit être dirigée par ses salariés"],
  ans=1,
  why=["L’approche par les parties prenantes est précisément l’alternative à "
       "sa thèse.",
       "Friedman ne confie aucune mission de financement public à "
       "l’entreprise.",
       "La codétermination n’est pas sa position."],
  exp="L’entreprise est ainsi considérée comme un instrument au service des "
      "actionnaires, ce qui légitime la priorité donnée à la rentabilité "
      "financière. C’est le socle théorique du capitalisme actionnarial.",
  diss="Opposition structurante du chapitre : Friedman contre les parties "
       "prenantes, c’est-à-dire la valeur actionnariale contre la "
       "responsabilité élargie de l’entreprise."),

f(id='q8-n40', sp='c8-12', niv='raisonner', type='ordre', b=1810,
  q="Remettez dans l’ordre les trois formes historiques du capitalisme "
    "décrites par le cours.",
  ans=["Le capitalisme entrepreneurial : le pouvoir est concentré entre les "
       "mains de l’entrepreneur, qui cumule propriété et direction",
       "Le capitalisme managérial : avec la taille et la complexité des "
       "firmes, propriété et contrôle se séparent et le pouvoir passe aux "
       "managers",
       "Le capitalisme actionnarial : à partir des années 1970-1980, la "
       "financiarisation recentre le pouvoir sur les actionnaires"],
  exp="Cette évolution traduit un déplacement progressif du pouvoir, "
      "accompagné d’une transformation des objectifs : l’innovation et le "
      "risque chez l’entrepreneur, la croissance et la planification de long "
      "terme chez les managers, la création de valeur pour l’actionnaire dans "
      "le capitalisme actionnarial.",
  diss="Le cours le dit explicitement : sur un sujet du type « qu’est-ce "
       "qu’une bonne gouvernance d’entreprise ? », il faut opposer ces trois "
       "configurations."),

f(id='q8-n41', sp='c8-12', niv='raisonner', type='qcmm', b=2020,
  q="Quelles conséquences concrètes la logique de création de valeur "
    "actionnariale entraîne-t-elle ? (plusieurs réponses)",
  opts=["Des restructurations",
        "Une réduction des coûts et des licenciements",
        "Une distribution accrue de dividendes",
        "Une augmentation des rémunérations des dirigeants, souvent liées à "
        "la performance boursière",
        "Un allongement systématique de l’horizon d’investissement"],
  ans=[0, 1, 2, 3],
  why=["Exacte : elles sont citées parmi les conséquences directes.",
       "Exacte : la pression sur la rentabilité financière passe par les "
       "coûts.",
       "Exacte : les dividendes sont l’un des canaux de la création de valeur.",
       "Exacte : d’où l’explosion des écarts de revenus relevée par Bloom.",
       "C’est l’inverse : le modèle est critiqué pour son court-termisme."],
  exp="Le cours récapitule trois critiques du modèle actionnarial : une "
      "logique de court terme centrée sur la performance financière "
      "immédiate ; des dérives possibles, dont le scandale Enron en 2001, "
      "marqué par des manipulations comptables et une faillite "
      "retentissante ; et une contribution à la hausse des inégalités."),

# ------------------------- c8-13 parties prenantes, Polanyi, RSE
f(id='q8-n42', sp='c8-13', niv='comprendre', type='qcm', b=2046,
  q="Qu’implique l’approche par les parties prenantes (stakeholders) ?",
  opts=["Que les actionnaires doivent être mieux protégés",
        "Que l’entreprise ne concerne pas uniquement les actionnaires mais un "
        "ensemble d’acteurs — salariés, clients, fournisseurs, État, "
        "environnement — dont les intérêts doivent être pris en compte",
        "Que les salariés doivent devenir actionnaires",
        "Que l’État doit nationaliser les grandes entreprises"],
  ans=1,
  why=["La protection des actionnaires est l’objectif de la gouvernance "
       "actionnariale, non des parties prenantes.",
       "L’actionnariat salarié est un dispositif particulier, pas la "
       "définition de l’approche.",
       "Aucune nationalisation n’est en cause."],
  exp="Cette approche rejoint les analyses de Karl Polanyi dans « La Grande "
      "Transformation » (1944) : l’économie ne peut être autonome, elle doit "
      "être encastrée dans la société, et le marché ne peut pas être le seul "
      "principe d’organisation.",
  diss="Le lien avec Polanyi est ce qui donne à l’approche par les parties "
       "prenantes une portée théorique, et pas seulement normative."),

f(id='q8-n43', sp='c8-13', niv='connaitre', type='qcm', b=2066,
  q="Qu’introduit la loi PACTE de 2019 en France ?",
  opts=["L’obligation de publier un rapport environnemental",
        "La notion de « raison d’être » et le statut d’entreprise à mission : "
        "l’entreprise peut poursuivre des objectifs autres que le profit",
        "La représentation obligatoire des salariés au conseil "
        "d’administration",
        "La taxation des dividendes"],
  ans=1,
  why=["Les obligations de reporting relèvent d’autres dispositifs.",
       "La représentation des salariés n’est pas l’objet retenu par le "
       "cours.",
       "La fiscalité des dividendes n’est pas en cause."],
  exp="C’est la traduction juridique de la RSE, qui consiste à intégrer aux "
      "objectifs économiques des préoccupations sociales et "
      "environnementales : l’entreprise devient un acteur du développement "
      "durable.",
  diss="Limites à citer immédiatement : le greenwashing, c’est-à-dire un "
       "discours responsable sans modification réelle des pratiques, dont le "
       "scandale Volkswagen et la falsification des émissions polluantes "
       "illustrent les contradictions."),

f(id='q8-n44', sp='c8-13', niv='raisonner', type='courte', b=2076,
  q="La gouvernance des entreprises est-elle devenue hybride ?",
  ans={'modele': "Oui : le capitalisme contemporain est traversé par une "
       "tension entre deux logiques. D’un côté une logique actionnariale "
       "centrée sur la rentabilité, théorisée par Friedman et outillée par la "
       "théorie de l’agence, les stock-options et la corporate governance. De "
       "l’autre une logique élargie intégrant les parties prenantes — "
       "salariés, clients, fournisseurs, État, environnement — nourrie par "
       "Polanyi et traduite juridiquement par la RSE et la loi PACTE de 2019. "
       "Les critiques du court-termisme, les dérives comme Enron et la montée "
       "des inégalités ont affaibli la première sans la supprimer : la "
       "gouvernance évolue donc vers un modèle hybride.",
       'cles': [{'f': ['actionnarial', 'rentabilite', 'friedman', 'valeur'],
                 'l': 'une logique actionnariale centrée sur la rentabilité'},
                {'f': ['partie prenante', 'stakeholder', 'polanyi', 'rse'],
                 'l': 'une logique élargie aux parties prenantes'},
                {'f': ['court terme', 'enron', 'inegalite'],
                 'l': 'des critiques : court-termisme, dérives, inégalités'},
                {'f': ['hybride', 'tension', 'coexist'],
                 'l': 'd’où une gouvernance hybride'}]},
  exp="Le cours conclut que l’entreprise ne peut plus être réduite à un "
      "simple instrument de profit : elle apparaît comme un acteur "
      "économique, social et environnemental central."),

# ----------------------------- c8-14 capitalisme numérique
f(id='q8-n45', sp='c8-14', niv='comprendre', type='qcm', b=2250,
  q="Sur quelles trois dynamiques majeures repose la révolution numérique "
    "actuelle ?",
  opts=["Internet, le cloud et la 5G",
        "L’intelligence artificielle et la robotisation, le big data, les "
        "plateformes numériques",
        "Les télécommunications, les semi-conducteurs et les batteries",
        "Le commerce en ligne, la publicité ciblée et les cryptomonnaies"],
  ans=1,
  why=["Ces technologies sont des supports, non les trois dynamiques "
       "retenues.",
       "Ce sont des industries, non des dynamiques économiques.",
       "Ce sont des applications parmi d’autres."],
  exp="L’intelligence artificielle est définie comme l’art de faire réaliser "
      "par des machines des tâches qui, accomplies par des humains, seraient "
      "considérées comme intelligentes : elle ne remplace plus seulement la "
      "force physique, mais certaines capacités cognitives. Le big data fait "
      "des données une matière première centrale — « les données sont la "
      "nouvelle électricité », selon Satya Nadella. Les plateformes "
      "transforment la coordination en réduisant les coûts de transaction.",
  diss="Nuance importante : l’IA reste fondamentalement probabiliste ; elle "
       "repose sur des traitements statistiques et ne comprend pas le sens des "
       "informations. Formule du cours : l’IA ne pense pas, elle calcule."),

f(id='q8-n46', sp='c8-14', niv='raisonner', type='qcm', b=2330,
  q="Pourquoi le capitalisme numérique renforce-t-il la concentration "
    "économique ?",
  opts=["Parce que les coûts de production des services numériques sont "
        "élevés",
        "Parce que les plateformes bénéficient d’effets de réseau, "
        "d’économies d’échelle et d’une accumulation massive de données : plus "
        "une plateforme a d’utilisateurs, plus elle est attractive",
        "Parce que les États favorisent les champions nationaux",
        "Parce que les consommateurs refusent de changer de fournisseur"],
  ans=1,
  why=["Les coûts marginaux sont au contraire très faibles dans le "
       "numérique.",
       "Le soutien étatique n’est pas le mécanisme analysé.",
       "L’inertie des consommateurs est un effet des effets de réseau, non "
       "leur cause."],
  exp="Cette dynamique favorise des situations d’oligopole, voire de "
      "monopole : GAFAM aux États-Unis, BATX en Chine. De nombreux acteurs "
      "traditionnels dénoncent une concurrence déloyale, une fiscalité "
      "avantageuse, des positions dominantes et une captation des marchés.",
  diss="À relier à Schumpeter : le monopole temporaire peut favoriser "
       "l’innovation, mais un monopole durable adossé aux données pose la "
       "question du maintien de la pression concurrentielle."),

f(id='q8-n47', sp='c8-14', niv='comprendre', type='qcmm', b=2323,
  q="Quelles catégories de menaces le cours attribue-t-il au capitalisme "
    "numérique ? (plusieurs réponses)",
  opts=["Économiques : concentration et concurrence imparfaite",
        "Sociales : isolement, précarité, économie de l’attention",
        "Politiques : surveillance et manipulation",
        "Écologiques : le mythe de la dématérialisation",
        "Monétaires : disparition des monnaies nationales"],
  ans=[0, 1, 2, 3],
  why=["Exacte : effets de réseau, oligopoles, GAFAM et BATX.",
       "Exacte : « seuls ensemble » selon Turkle, ubérisation, civilisation "
       "du poisson rouge.",
       "Exacte : collecte des données, contrôle social, influence sur les "
       "opinions et les élections.",
       "Exacte : data centers, câbles, antennes, électricité, eau — le "
       "numérique reste profondément matériel.",
       "Aucune menace monétaire de ce type n’est évoquée."],
  exp="Le cours insiste sur l’ambivalence : la révolution numérique est "
      "porteuse d’opportunités — innovation, baisse de certains coûts, "
      "nouveaux services, économie du partage — et de menaces dans quatre "
      "dimensions. C’est cette ambivalence qu’il faut restituer."),

f(id='q8-n48', sp='c8-14', niv='comprendre', type='qcm', b=2370,
  q="Que révèle l’exemple d’Uber sur le modèle économique des plateformes ?",
  opts=["Les plateformes investissent massivement dans leurs actifs "
        "productifs",
        "Les facteurs de production sont externalisés : la voiture appartient "
        "au chauffeur, les coûts sont supportés par les travailleurs, et la "
        "plateforme capte une commission",
        "Les plateformes salarient l’essentiel de leurs travailleurs",
        "Les plateformes réduisent les coûts de transaction sans modifier les "
        "formes d’emploi"],
  ans=1,
  why=["Uber ne possède quasiment pas de véhicules : c’est précisément le "
       "point du cours.",
       "Les chauffeurs ne sont pas salariés mais indépendants.",
       "Les formes d’emploi sont au contraire profondément modifiées."],
  exp="Uber coordonne des centaines de milliers de chauffeurs sans posséder "
      "de flotte. Les plateformes favorisent ainsi la flexibilité, les "
      "emplois précaires, les contrats courts, l’auto-entrepreneuriat et le "
      "travail indépendant : c’est ce que certains auteurs appellent "
      "l’« ubérisation » du travail.",
  diss="Le cours ajoute plus loin la question du salariat déguisé : ces "
       "indépendants dépendent fortement de la plateforme et disposent "
       "parfois de très peu d’autonomie réelle."),

f(id='q8-n49', sp='c8-14', niv='raisonner', type='qcm', b=2418,
  q="Pourquoi le cours parle-t-il d’un « mythe de la dématérialisation » ?",
  opts=["Parce que les services numériques sont en réalité payants",
        "Parce que le numérique repose sur des centres de données, des "
        "infrastructures industrielles, des antennes, des câbles, de "
        "l’électricité et de l’eau : il reste profondément matériel",
        "Parce que les données ne sont pas stockées durablement",
        "Parce que le cloud est une métaphore commerciale"],
  ans=1,
  why=["La question du prix est un autre argument, celui de la fausse "
       "gratuité.",
       "La durabilité du stockage n’est pas le problème soulevé.",
       "Le caractère métaphorique du mot ne suffirait pas à établir la "
       "matérialité."],
  exp="Le numérique donne l’impression d’un monde immatériel — cloud, données "
      "virtuelles, économie dématérialisée — mais il produit des coûts "
      "écologiques importants, souvent invisibilisés. Le cloud repose sur des "
      "infrastructures industrielles gigantesques.",
  diss="Cet argument rejoint directement l’analyse de Veltz sur la société "
       "hyper-industrielle, étudiée au chapitre 6 : plus l’économie paraît "
       "immatérielle, plus elle dépend d’infrastructures lourdes."),

f(id='q8-n50', sp='c8-14', niv='raisonner', type='qcm', b=2545,
  q="En quoi la gratuité apparente des services numériques est-elle "
    "trompeuse ?",
  opts=["Parce que les utilisateurs paient par abonnement à terme",
        "Parce que le prix n’a pas disparu mais s’est déplacé : les "
        "plateformes se rémunèrent par les commissions, la publicité et la "
        "revente des données — quand c’est gratuit, c’est souvent "
        "l’utilisateur qui devient le produit",
        "Parce que les services gratuits sont de moindre qualité",
        "Parce que la gratuité est financée par les États"],
  ans=1,
  why=["L’abonnement n’est qu’un modèle parmi d’autres : l’argument du cours "
       "est plus général.",
       "La qualité n’est pas le problème soulevé.",
       "Aucun financement public n’est en cause."],
  exp="Le cours en tire une conclusion ferme : le capitalisme numérique "
      "transforme les mécanismes du marché mais ne supprime pas la logique "
      "marchande. De même, l’économie du partage semble remettre en cause la "
      "propriété privée, mais elle peut au contraire en être une extension à "
      "de nouveaux usages, puisque celui qui loue son logement ou partage sa "
      "voiture cherche souvent à en tirer un revenu.",
  diss="Raisonnement à retenir pour la question « le numérique remet-il en "
       "cause les fondements du capitalisme ? » : il les transforme, il ne "
       "les supprime pas."),

# --------------------------- c8-15 un capitalisme pluriel
f(id='q8-n51', sp='c8-15', niv='connaitre', type='assoc', b=2456,
  q="Associez chacun des trois âges du capitalisme, selon François et "
    "Mercier, à ses figures centrales.",
  ans=[["L’âge du commerce, jusqu’au XVIIIᵉ siècle", "Le marchand et le négociant"],
       ["L’âge de l’usine, avec les révolutions industrielles", "L’ouvrier et le manager"],
       ["L’âge du capital, depuis les années 1980", "L’actionnaire et l’intérimaire"]],
  exp="Cette périodisation éclaire le lien entre forme du capitalisme et "
      "figures sociales dominantes : à l’âge du capital, le capitalisme "
      "devient financiarisé, flexible et mondialisé, et le travail plus "
      "précaire. Le cours la rapproche d’autres typologies : l’École de la "
      "régulation distingue un capitalisme concurrentiel puis monopolistique, "
      "la crise de 1929 ayant profondément transformé les modes de "
      "régulation.",
  diss="Associer un âge à ses figures permet de relier structures "
       "économiques et transformations sociales en une phrase."),

f(id='q8-n52', sp='c8-15', niv='comprendre', type='qcm', b=2521,
  q="Quels sont les quatre fondements classiques du capitalisme selon le "
    "cours ?",
  opts=["La propriété privée, le salariat, le marché et les prix, la "
        "recherche du profit",
        "La concurrence, l’innovation, la monnaie et le crédit",
        "Le travail, le capital, la terre et l’entrepreneuriat",
        "La liberté d’entreprendre, le libre-échange, la propriété et "
        "l’État de droit"],
  ans=0,
  why=["Ce sont des caractéristiques du capitalisme, non ses quatre "
       "fondements au sens du cours.",
       "Ce sont les facteurs de production de l’analyse classique.",
       "Ce sont des conditions institutionnelles, également importantes mais "
       "distinctes."],
  exp="Le cours examine ensuite si la révolution numérique remet en cause ces "
      "fondements. La réponse est nuancée : l’économie du partage semble "
      "menacer la propriété privée mais peut l’étendre ; la gratuité semble "
      "menacer le marché mais le prix est seulement déplacé vers les "
      "commissions, la publicité et les données.",
  diss="Structure idéale pour un sujet du type « le numérique change-t-il la "
       "nature du capitalisme ? » : quatre fondements, examinés un à un."),

f(id='q8-n53', sp='c8-15', niv='comprendre', type='qcm', b=2484,
  q="Pourquoi le cours affirme-t-il qu’il n’existe pas un capitalisme mais "
    "des capitalismes ?",
  opts=["Parce que chaque entreprise a sa propre gouvernance",
        "Parce que les pays capitalistes diffèrent par le rôle de l’État, la "
        "protection sociale et le marché du travail : certains modèles sont "
        "plus libéraux, d’autres plus sociaux-démocrates ou plus "
        "interventionnistes",
        "Parce que le capitalisme n’existe que dans les pays développés",
        "Parce que les capitalismes nationaux convergent progressivement"],
  ans=1,
  why=["La diversité visée est nationale et institutionnelle, non "
       "microéconomique.",
       "Les pays émergents sont au contraire explicitement intégrés à "
       "l’analyse.",
       "Le cours soutient l’inverse : les capitalismes restent très "
       "différents."],
  exp="Le cours oppose un modèle privilégiant la flexibilité, le marché et "
      "une faible intervention de l’État — exemple des États-Unis — à un "
      "modèle privilégiant la protection sociale, la régulation et les droits "
      "des salariés — exemple de la France. La diversité vaut aussi pour les "
      "pays émergents, selon qu’ils misent sur l’industrialisation et les "
      "exportations manufacturières ou sur les matières premières.",
  diss="Conclusion du cours : même dans un monde largement capitaliste, les "
       "capitalismes restent très différents — les formes dépendent du rôle de "
       "l’État, de l’insertion internationale et du modèle de croissance."),

# ------------------------ c8-16 / c8-17 travail, emploi, précarisation
f(id='q8-n54', sp='c8-16', niv='comprendre', type='qcm', b=2796,
  q="Quelle distinction le cours établit-il entre travail et emploi ?",
  opts=["Les deux termes sont équivalents dans l’analyse économique",
        "Le travail désigne toute activité productive, rémunérée ou non ; "
        "l’emploi désigne un travail rémunéré, dans un cadre juridique précis",
        "Le travail concerne les salariés, l’emploi les indépendants",
        "Le travail est une notion juridique, l’emploi une notion "
        "statistique"],
  ans=1,
  why=["Le cours en fait au contraire une distinction fondamentale.",
       "La distinction ne porte pas sur le statut du travailleur.",
       "C’est plutôt l’inverse : l’emploi renvoie au cadre juridique."],
  exp="Le travail inclut le travail domestique, bénévole, associatif et "
      "salarié ; il renvoie aux tâches réalisées, aux conditions d’exercice, "
      "aux qualifications et à l’organisation. Parler de cadences, de "
      "télétravail, d’IA ou de conditions physiques, c’est parler de "
      "conditions de travail. L’emploi renvoie au statut, à la stabilité du "
      "contrat, à la durée du travail et aux protections sociales : parler de "
      "CDI, de CDD, de temps plein ou de temps partiel, c’est parler de "
      "conditions d’emploi.",
  diss="Distinction à poser en introduction de tout sujet sur le travail : "
       "elle évite de confondre dégradation des conditions de travail et "
       "précarisation de l’emploi."),

f(id='q8-n55', sp='c8-16', niv='connaitre', type='qcm', b=2846,
  q="Quelle est la répartition entre salariés et indépendants en France, "
    "selon le cours ?",
  opts=["Environ 50 % de salariés et 50 % d’indépendants",
        "Environ 86 % de salariés et 13,5 % d’indépendants",
        "Environ 95 % de salariés et 5 % d’indépendants",
        "Environ 73 % de salariés et 27 % d’indépendants"],
  ans=1,
  why=["Cette répartition correspondrait aux sociétés préindustrielles.",
       "La part des indépendants est sous-estimée.",
       "73 % est la part des salariés en CDI, non la part des salariés dans "
       "l’emploi total."],
  exp="Les indépendants travaillent pour leur propre compte, sans contrat de "
      "travail : artisans, commerçants, professions libérales, "
      "auto-entrepreneurs — devenus micro-entrepreneurs — dont la place est "
      "croissante. Le salariat reste donc la forme dominante du travail depuis "
      "les révolutions industrielles.",
  diss="Attention à ne pas confondre les deux pourcentages : 86 % de salariés "
       "dans l’emploi total, 73 % de CDI parmi les salariés."),

f(id='q8-n56', sp='c8-16', niv='comprendre', type='qcm', b=2864,
  q="Qu’appelle-t-on la salarisation, et comment s’explique-t-elle ?",
  opts=["La hausse des salaires réels au cours du XXᵉ siècle",
        "Le passage d’une population majoritairement indépendante à une "
        "population majoritairement salariée, lié au fait que les machines, "
        "plus coûteuses, exigent la concentration des travailleurs dans les "
        "usines",
        "L’extension du salaire minimum à tous les secteurs",
        "La généralisation du CDI après 1945"],
  ans=1,
  why=["L’évolution du pouvoir d’achat est une autre question.",
       "Le salaire minimum est un dispositif de politique salariale.",
       "La généralisation du CDI est une conséquence tardive, non la "
       "définition."],
  exp="Avant les révolutions industrielles, la population travaillait "
      "principalement dans l’agriculture, l’artisanat et le travail à "
      "domicile, souvent en indépendants. La concentration dans les usines "
      "transforme les ouvriers en salariés. Cette salarisation s’est "
      "accompagnée d’une extension des protections : congés payés, protection "
      "sociale, droits syndicaux, protections contre les accidents du travail, "
      "droits à la retraite, assurance chômage.",
  diss="Repère juridique à citer : la loi de 1898 sur les accidents du "
       "travail. Avant, l’accident était considéré comme la responsabilité du "
       "salarié ; après, l’employeur peut être tenu responsable."),

f(id='q8-n57', sp='c8-17', niv='connaitre', type='qcm', b=2922,
  q="Quels repères le cours donne-t-il sur le CDI en France ?",
  opts=["Il concerne environ 50 % des salariés, pour une ancienneté moyenne "
        "de 5 ans",
        "Il concerne environ 73 % des salariés, pour une durée moyenne dans "
        "l’entreprise d’environ 11 ans",
        "Il concerne environ 90 % des salariés, pour une ancienneté moyenne "
        "de 15 ans",
        "Il concerne environ 60 % des salariés, pour une ancienneté moyenne "
        "de 8 ans"],
  ans=1,
  why=["La part du CDI est nettement sous-estimée.",
       "90 % surestime la part du CDI, qui laisse place aux contrats courts.",
       "Ni la part ni l’ancienneté ne correspondent."],
  exp="Le CDI reste donc la norme traditionnelle du salariat stable. Le CDD, "
      "à l’inverse, prévoit une date de début et une date de fin, répond en "
      "principe à un besoin temporaire — remplacement, activité saisonnière, "
      "hausse ponctuelle d’activité — et ne doit pas dépasser 18 mois dans la "
      "plupart des cas.",
  diss="Ces chiffres permettent de nuancer le discours sur la précarité "
       "généralisée : la majorité des salariés restent en CDI à temps plein, "
       "même si les formes précaires augmentent."),

f(id='q8-n58', sp='c8-17', niv='comprendre', type='qcm', b=2944,
  q="Quel est le rôle des prud’hommes ?",
  opts=["Fixer le salaire minimum par branche",
        "Juger les litiges entre employeurs et salariés : abus de contrats, "
        "licenciements, conflits liés au droit du travail",
        "Négocier les conventions collectives",
        "Contrôler l’application des règles de sécurité en entreprise"],
  ans=1,
  why=["La fixation du salaire minimum relève de la loi et de la négociation "
       "de branche.",
       "La négociation collective associe syndicats et organisations "
       "patronales.",
       "Le contrôle de la sécurité relève de l’inspection du travail."],
  exp="Le cours mobilise les prud’hommes à propos des abus de contrats "
      "précaires : certaines entreprises enchaînent les contrats courts, et "
      "des salariés ont parfois travaillé des années sous ce régime. Ces "
      "conflits révèlent un déséquilibre : les entreprises cherchent à "
      "réduire les coûts, éviter les CDI et limiter les protections, les "
      "salariés cherchent la stabilité et des droits.",
  diss="Formule du cours à retenir : le marché du travail repose aussi sur un "
       "rapport de force social."),

f(id='q8-n59', sp='c8-17', niv='appliquer', type='qcm', b=2970,
  q="Qu’est-ce qui distingue le temps partiel choisi du temps partiel subi ?",
  opts=["Le temps partiel choisi est à l’initiative de l’employeur, le subi à "
        "celle du salarié",
        "Le temps partiel choisi correspond à une décision volontaire du "
        "salarié — études, sport, vie familiale — alors que le temps partiel "
        "subi désigne la situation d’un salarié qui souhaiterait travailler "
        "davantage sans que l’entreprise lui propose plus d’heures",
        "Le temps partiel choisi est rémunéré au-delà du minimum légal",
        "Le temps partiel subi concerne uniquement les contrats courts"],
  ans=1,
  why=["Les deux initiatives sont inversées.",
       "La rémunération n’entre pas dans cette distinction.",
       "Le temps partiel subi peut exister en CDI."],
  exp="Le temps partiel subi constitue une forme de précarité. En France, le "
      "temps plein est généralement fixé à 35 heures hebdomadaires, certains "
      "secteurs restant à 39 heures ; le temps partiel désigne une durée "
      "inférieure à la durée légale prévue.",
  diss="Le temps partiel subi est l’un des canaux de la pauvreté laborieuse : "
       "il faut savoir relier les deux notions."),

f(id='q8-n60', sp='c8-17', niv='raisonner', type='qcmm', b=2984,
  q="Sous quelles formes la précarisation de l’emploi s’est-elle manifestée "
    "depuis la crise de 1973 ? (plusieurs réponses)",
  opts=["La hausse des CDD",
        "La hausse du temps partiel subi",
        "Les contrats courts et l’intérim",
        "L’auto-entrepreneuriat contraint",
        "La disparition du CDI comme norme majoritaire"],
  ans=[0, 1, 2, 3],
  why=["Exacte : le CDD progresse comme forme d’ajustement.",
       "Exacte : il constitue une précarité à part entière.",
       "Exacte : contrats courts et intérim sont explicitement cités.",
       "Exacte : certaines plateformes font de l’indépendance une contrainte.",
       "Le cours précise au contraire que la majorité des salariés restent en "
       "CDI à temps plein, même si les formes précaires augmentent."],
  exp="Le cours relie cette évolution à la notion de pauvreté laborieuse : "
      "autrefois liée à l’absence d’emploi, la pauvreté touche aujourd’hui "
      "aussi des personnes qui travaillent, du fait des faibles salaires, du "
      "temps partiel subi et des contrats précaires. Le travail ne garantit "
      "donc plus automatiquement la sortie de la pauvreté."),

f(id='q8-n61', sp='c8-17', niv='raisonner', type='qcm', b=3010,
  q="Pourquoi parle-t-on de « salariat déguisé » à propos des travailleurs de "
    "plateformes ?",
  opts=["Parce qu’ils cumulent un emploi salarié et une activité indépendante",
        "Parce qu’ils sont juridiquement indépendants mais dépendent "
        "fortement de la plateforme et disposent parfois de très peu "
        "d’autonomie réelle",
        "Parce qu’ils sont rémunérés au salaire minimum",
        "Parce qu’ils bénéficient des protections du salariat sans en avoir "
        "le statut"],
  ans=1,
  why=["Le cumul d’activités est une autre situation.",
       "Le niveau de rémunération n’est pas le critère.",
       "C’est l’inverse : ils ne bénéficient pas de ces protections, ce qui "
       "fait précisément problème."],
  exp="Les plateformes évitent ainsi les cotisations sociales, certaines "
      "protections salariales et les obligations du droit du travail : le "
      "chauffeur Uber n’est pas salarié mais indépendant. Le développement des "
      "plateformes relance donc la question du rapport de force entre "
      "entreprises et travailleurs.",
  diss="À relier au mouvement historique inverse : la salarisation avait "
       "apporté les protections ; le retour de l’indépendance les remet en "
       "question."),

f(id='q8-n62', sp='c8-16', niv='raisonner', type='courte', b=2889,
  q="Que contestent exactement les luddites, et pourquoi le cours rapproche-t-il "
    "ce mouvement du débat sur l’intelligence artificielle ?",
  ans={'modele': "Entre 1811 et 1816, des ouvriers du textile anglais "
       "détruisent des machines qu’ils considèrent comme une menace pour leur "
       "travail. Mais ils ne contestent pas seulement la perte d’emploi : ils "
       "dénoncent aussi les nouvelles cadences, la discipline industrielle, "
       "l’autorité du contremaître et la perte d’autonomie, puisqu’il faut "
       "désormais suivre le rythme imposé par la machine. Le progrès technique "
       "améliore donc la productivité tout en transformant profondément les "
       "conditions de travail. Le cours rapproche ce mouvement de la crainte "
       "contemporaine que l’IA remplace des travailleurs — comptabilité, "
       "communication, rédaction, service client, traduction — en soulignant "
       "que la question reste ouverte entre destruction d’emplois et "
       "transformation des tâches.",
       'cles': [{'f': ['1811', '1816', 'textile', 'detruisent', 'machine'],
                 'l': 'des ouvriers du textile détruisent les machines'},
                {'f': ['cadence', 'discipline', 'autonomie', 'contremaitre'],
                 'l': 'ils contestent aussi cadences, discipline et perte d’autonomie'},
                {'f': ['ia', 'intelligence artificielle', 'remplace'],
                 'l': 'la même crainte se reporte sur l’IA'},
                {'f': ['transformation', 'tache', 'ouvert', 'debat'],
                 'l': 'destruction d’emplois ou transformation des tâches : débat ouvert'}]},
  exp="Le parallèle a une portée méthodologique : à chaque grande révolution "
      "technologique, la même inquiétude réapparaît, et l’histoire montre que "
      "la machine recompose le travail plus qu’elle ne l’élimine — sans "
      "garantir que ce soit toujours le cas."),

# ----------------------------------------- c8-18 IA et emploi
f(id='q8-n63', sp='c8-18', niv='comprendre', type='qcm', b=3370,
  q="Pourquoi dit-on que l’IA remplace surtout des tâches plutôt que des "
    "métiers ?",
  opts=["Parce que les entreprises préfèrent conserver leurs salariés",
        "Parce qu’un métier est composé de plusieurs tâches : l’IA en "
        "automatise certaines sans supprimer le métier entier, qui est donc "
        "reconfiguré",
        "Parce que l’IA n’est pas encore suffisamment performante",
        "Parce que la réglementation interdit les licenciements liés à "
        "l’automatisation"],
  ans=1,
  why=["Les préférences des entreprises ne sont pas l’argument : c’est la "
       "structure des métiers qui est en cause.",
       "La performance de l’IA progresse : l’argument est structurel, non "
       "technique.",
       "Aucune interdiction de ce type n’existe."],
  exp="Exemple du cours : l’IA peut analyser des dossiers et lire des "
      "documents, mais elle ne remplace pas la relation humaine, le conseil ni "
      "l’interaction avec les clients. Les salariés peuvent alors consacrer "
      "plus de temps à la relation client : le contenu du travail évolue.",
  diss="C’est exactement ce que mesure l’estimation d’Osborne et Frey : une "
       "part des tâches techniquement automatisables, et non une part des "
       "emplois condamnés."),

f(id='q8-n64', sp='c8-18', niv='raisonner', type='qcm', b=3410,
  q="En quoi l’IA constitue-t-elle une rupture historique par rapport aux "
    "révolutions industrielles antérieures ?",
  opts=["Elle se diffuse plus lentement",
        "Les anciennes révolutions remplaçaient surtout la force physique, "
        "tandis que l’IA automatise certaines tâches intellectuelles et "
        "touche des fonctions cognitives qualifiées",
        "Elle ne concerne que l’industrie",
        "Elle supprime le besoin de capital"],
  ans=1,
  why=["Sa diffusion est au contraire beaucoup plus rapide : certaines "
       "technologies atteignent des millions d’utilisateurs en quelques mois.",
       "Elle touche au contraire finance, droit, comptabilité, management et "
       "administration.",
       "Elle exige au contraire des investissements massifs : centres de "
       "données, puces, infrastructures."],
  exp="Les travailleurs diplômés sont désormais concernés par "
      "l’automatisation, ce qui est inédit. Le cours en tire un risque "
      "spécifique : les entreprises peuvent préférer des salariés moins "
      "diplômés, moins coûteux, assistés par l’IA, ce qui favoriserait une "
      "substitution du travail qualifié et un déclassement — un individu "
      "occupant un emploi inférieur à son niveau de qualification.",
  diss="Nuance symétrique : l’IA peut aussi augmenter les capacités humaines, "
       "des salariés peu qualifiés devenant plus efficaces et capables de "
       "tâches plus complexes."),

f(id='q8-n65', sp='c8-18', niv='raisonner', type='qcm', b=3357,
  q="Quel paradoxe le cours relève-t-il dans les stratégies des grandes "
    "entreprises technologiques ?",
  opts=["Elles investissent peu malgré des profits élevés",
        "Pour financer leurs investissements massifs dans l’IA, les centres "
        "de données et les puces, certaines entreprises licencient et "
        "restructurent : même très rentables, elles suppriment des emplois",
        "Elles embauchent massivement tout en réduisant leurs "
        "investissements",
        "Elles délaissent l’IA au profit des services traditionnels"],
  ans=1,
  why=["Les investissements sont au contraire massifs : Meta, Amazon, "
       "Apple sont cités.",
       "Le mouvement est inverse : investissements en hausse, effectifs "
       "parfois en baisse.",
       "L’IA est au contraire l’enjeu stratégique majeur."],
  exp="Le cours en tire une conclusion générale : le progrès technique peut "
      "simultanément créer et détruire des emplois. Des entreprises en "
      "croissance peuvent réduire l’emploi — ce qui est précisément la logique "
      "de la destruction créatrice schumpétérienne appliquée au présent.",
  diss="Lien à faire explicitement avec Schumpeter : la croissance et la "
       "destruction d’emplois ne sont pas contradictoires."),

f(id='q8-n66', sp='c8-18', niv='raisonner', type='qcmm', b=3314,
  q="Quelles conséquences une baisse de l’emploi liée à l’automatisation "
    "pourrait-elle avoir sur les finances publiques ? (plusieurs réponses)",
  opts=["Moins d’impôts sur le revenu",
        "Moins de cotisations sociales",
        "Moins de consommation, donc moins de TVA",
        "Des dépenses publiques accrues : chômage, aides sociales, "
        "reconversions professionnelles",
        "Une baisse mécanique de la dette publique"],
  ans=[0, 1, 2, 3],
  why=["Exacte : l’assiette de l’impôt sur le revenu se contracte.",
       "Exacte : les cotisations sont assises sur les salaires.",
       "Exacte : la baisse des revenus réduit la consommation taxable.",
       "Exacte : les dépenses sociales et de formation augmenteraient.",
       "C’est l’inverse : le risque est une aggravation des déficits "
       "publics."],
  exp="Ce diagnostic nourrit un débat : faut-il taxer les robots ou l’IA ? "
      "L’objectif serait de compenser la baisse des cotisations sociales et "
      "des recettes fiscales liées au travail, en faisant contribuer les "
      "machines au financement de la protection sociale.",
  diss="À compléter par l’argument d’Acemoglu, cité par le cours : les choix "
       "technologiques sont aussi des choix politiques, et l’État doit "
       "accompagner les travailleurs, financer la formation, limiter les "
       "inégalités et protéger la cohésion sociale."),

f(id='q8-n67', sp='c8-18', niv='comprendre', type='qcm', b=3455,
  q="Quels métiers le cours présente-t-il comme difficilement "
    "automatisables ?",
  opts=["La comptabilité, la traduction et le service client",
        "Les infirmiers, aides-soignants, artisans, plombiers et métiers du "
        "soin",
        "Le droit, la finance et le management",
        "La rédaction et la communication"],
  ans=1,
  why=["Ce sont précisément les activités que le cours cite comme exposées à "
       "l’IA.",
       "Droit, finance et management font partie des fonctions cognitives "
       "qualifiées désormais concernées.",
       "Rédaction et communication sont citées parmi les métiers exposés."],
  exp="Les tâches humaines relationnelles et manuelles restent essentielles. "
      "L’IA peut assister ces métiers sans les remplacer. Le cours en tire une "
      "conclusion de politique publique : l’enjeu n’est pas seulement le "
      "nombre d’emplois, mais la nature des compétences demandées et "
      "l’accompagnement des reconversions.",
  diss="Cette asymétrie — métiers cognitifs exposés, métiers manuels et "
       "relationnels protégés — renverse la hiérarchie habituelle des "
       "qualifications, ce qui en fait un excellent argument de troisième "
       "partie."),

f(id='q8-n68', sp='c8-18', niv='raisonner', type='courte', b=3389,
  q="L’IA détruit-elle les emplois ou transforme-t-elle le travail ?",
  ans={'modele': "Les deux effets coexistent et le débat reste ouvert. "
       "Effets quantitatifs : l’IA peut remplacer certains travailleurs, "
       "réduire les coûts et diminuer la masse salariale, et certaines "
       "entreprises licencient déjà pour financer leurs investissements. "
       "Effets qualitatifs : elle modifie surtout les tâches, augmente la "
       "productivité et rend certains métiers plus techniques ou plus "
       "relationnels — un métier étant composé de plusieurs tâches, il est "
       "reconfiguré plutôt que supprimé. L’IA peut même augmenter les "
       "capacités humaines, des salariés peu qualifiés devenant plus "
       "performants. Mais elle fait aussi peser un risque de substitution du "
       "travail qualifié et de déclassement des diplômés.",
       'cles': [{'f': ['remplace', 'masse salariale', 'suppression', 'licenci'],
                 'l': 'des effets quantitatifs : suppressions possibles'},
                {'f': ['tache', 'reconfigur', 'productivite', 'contenu'],
                 'l': 'des effets qualitatifs : transformation des tâches'},
                {'f': ['peu qualifie', 'augmente', 'capacite', 'assiste'],
                 'l': 'elle peut augmenter les capacités de certains travailleurs'},
                {'f': ['declassement', 'diplome', 'qualifie', 'substitution'],
                 'l': 'mais menace le travail qualifié : risque de déclassement'}]},
  exp="Le cours refuse de trancher définitivement et c’est la bonne posture : "
      "certains pensent que l’IA supprimera massivement des emplois, d’autres "
      "qu’elle augmentera les capacités des travailleurs, notamment les moins "
      "qualifiés. Les effets globaux restent débattus."),
]

from qz08n1 import L as _M1

NEW = NEW + _M1
