# -*- coding: utf-8 -*-
"""Première année — chapitre 1.
Pauvreté monétaire, circuit économique et consommation."""

from fc_base import lot, c

L = lot(1)

# ------------------------------------------------- I. Introduction

c('Qu’est-ce que le capitalisme, au sens où le cours l’emploie ?',
  'Un régime économique dans lequel des individus détiennent les capitaux et les moyens de production.',
  x='La propriété privée des moyens de production est ce qui le distingue des régimes où ils sont collectifs.',
  t='def', b=1)

c('De combien le PIB a-t-il reculé en France et dans le monde en 2020 ?',
  '− 7 % en France, − 3,5 % dans le monde.',
  x='Chiffre d’accroche pour montrer qu’un choc sanitaire peut interrompre brutalement l’activité d’un régime capitaliste.',
  t='fait', b=2)

c('Quel terme Dominique Plihon emploie-t-il pour qualifier l’état du capitalisme contemporain ?',
  'La polycrise.',
  x='Il la développe dans Les capitalismes contemporains : plusieurs crises de nature différente se nourrissent les unes les autres.',
  t='aut', b=3)

c('Quelles sont les quatre crises que Dominique Plihon réunit sous le terme de polycrise ?',
  'Économique et sociale, écologique, démocratique, géopolitique.',
  x='L’intérêt de la notion est qu’aucune de ces crises ne se règle isolément des trois autres.',
  t='aut', b=4)

c('Quels signes le cours retient-il de la crise démocratique dans les pays capitalistes ?',
  'L’abstention, la baisse de l’adhésion aux syndicats et aux partis, et la montée du populisme.',
  x='Le cours cite que 70 % des jeunes jugent les responsables politiques corrompus ; le populisme oppose des élites privilégiées à un peuple.',
  t='fait', b=7)

c('Qu’est-ce que la mondialisation ?',
  'La multiplication des échanges de biens et de services entre nations, qui renforce leurs interdépendances.',
  x='C’est la définition la plus neutre : elle décrit un mouvement d’échanges, sans préjuger de ses effets.',
  t='def', b=12)

c('Qu’appelle-t-on une chaîne de valeur ?',
  'L’ensemble des activités d’une entreprise, de la conception d’un produit jusqu’à sa production finale.',
  x='Quand ces activités sont réparties entre plusieurs pays, on parle de chaîne de valeur mondiale.',
  t='def', b=13)

c('Selon Arnaud Orain, à quelle étape le capitalisme est-il parvenu ?',
  'L’étape de la finitude.',
  x='Il la décrit dans Le Monde confisqué : la croissance ne vient plus de l’extension des marchés mais de la captation de ressources limitées.',
  t='aut', b=14)

c('Pourquoi Arnaud Orain voit-il dans les monopoles un signe que le capitalisme a changé de nature ?',
  'Parce que la concurrence, censée faire vivre le capitalisme libéral, cède la place à quelques géants qui fixent leurs propres règles.',
  x='Exemples du cours : Google dans la recherche, Amazon dans le commerce en ligne, les grandes compagnies pétrolières et financières.',
  t='aut', b=17)

c('En quoi certaines entreprises constituent-elles aujourd’hui de véritables empires ?',
  'Elles possèdent leurs réseaux, leurs territoires et une influence politique qui leur permet de traiter d’égal à égal avec les États.',
  x='Satellites, clouds, plateformes, zones franches : les GAFAM gèrent une part de la communication, des paiements et de la navigation.',
  t='mec', b=19)

c('Sur quels quatre éléments le capitalisme repose-t-il ?',
  'L’accumulation du capital, la propriété privée, le salariat et la régulation marchande.',
  x='Les deux premiers sont les piliers : investir pour dégager un profit, que la propriété privée permet de conserver.',
  t='mec', b=22)

c('Qu’est-ce qui distingue un capitalisme libéral d’un capitalisme interventionniste ?',
  'La présence ou l’absence de l’État : il se tient à l’écart dans le premier, il agit sur les ménages et l’activité dans le second.',
  x='Le passage de l’un à l’autre est historique, et non définitif : les deux formes alternent selon les périodes.',
  t='dist', b=28)

c('Quel exemple le cours donne-t-il d’un basculement vers un capitalisme interventionniste ?',
  'Roosevelt en 1933, avec une politique budgétaire de soutien à la demande globale.',
  x='Les investissements publics sont engagés pour produire des retombées supérieures à la somme injectée au départ.',
  t='fait', b=30)

# --------------------------------- II.A La comptabilité nationale

c('Qu’est-ce que la comptabilité nationale ?',
  'Un ensemble d’analyses statistiques qui donne une représentation chiffrée de l’activité économique et des actions des agents.',
  x='Son approche est macroéconomique : elle agrège des données individuelles pour décrire l’économie dans son ensemble.',
  t='def', b=36)

c('Dans quel contexte historique la comptabilité nationale est-elle née ?',
  'Au XVIIᵉ siècle, lorsque le roi a voulu mesurer le patrimoine des individus pour décider de la fiscalité.',
  x='Son origine est donc fiscale : compter sert d’abord à savoir sur qui prélever.',
  t='fait', b=37)

c('Quels sont les six secteurs institutionnels retenus par la comptabilité nationale ?',
  'Sociétés non financières, sociétés financières, administrations publiques, ménages, ISBLSM, reste du monde.',
  x='Chaque unité résidente est classée dans un seul secteur, selon sa fonction principale et l’origine de ses ressources.',
  t='mec', b=38)

c('Quelle est la fonction des sociétés non financières en comptabilité nationale ?',
  'Produire des biens et des services marchands non financiers.',
  x='Marchand signifie vendu à un prix couvrant au moins la moitié du coût de production.',
  t='def', b=39)

c('Que recouvre le secteur des sociétés financières ?',
  'Les unités qui financent l’économie ou gèrent les moyens de financement.',
  x='Banques, assurances et sociétés de gestion : leur activité porte sur les flux de capitaux, non sur la production de biens.',
  t='def', b=40)

c('Quelles sont les deux fonctions des administrations publiques en comptabilité nationale ?',
  'Produire des services non marchands et redistribuer les richesses entre les agents.',
  x='La première fonction explique leurs dépenses, la seconde explique les prélèvements et les prestations.',
  t='def', b=41)

c('Pourquoi une entreprise individuelle est-elle rattachée au secteur des ménages ?',
  'Parce qu’elle n’a pas de statut juridique propre : son patrimoine ne se distingue pas de celui de la personne qui la possède.',
  x='C’est une convention comptable qui a une conséquence concrète : les dettes de l’activité engagent le patrimoine personnel.',
  t='mec', b=42)

c('Que désigne le sigle ISBLSM ?',
  'Les institutions sans but lucratif au service des ménages.',
  x='Associations, syndicats, fondations : elles fournissent aux ménages des services non marchands sans rechercher de profit.',
  t='def', b=43)

c('À quoi sert le compte du reste du monde en comptabilité nationale ?',
  'À retracer les relations économiques entre le territoire national et l’extérieur.',
  x='Ce n’est pas un secteur d’agents, mais un compte miroir qui enregistre ce qui entre et ce qui sort.',
  t='def', b=44)

c('Quel économiste est présenté comme le premier à avoir rassemblé des données pour fonder une approche macroéconomique ?',
  'Ragnar Frisch.',
  x='Sans agrégation de données individuelles, il n’existe pas de grandeur macroéconomique à observer ni à comparer.',
  t='aut', b=45)

c('Combien de temps faut-il pour que les données de la comptabilité nationale soient définitives ?',
  'Trois ans au minimum.',
  x='Le cours en donne l’illustration : les données définitives de 2022 ont été publiées par l’INSEE en 2025.',
  t='fait', b=47)

c('Qu’est-ce que l’économie nationale ?',
  'L’ensemble des unités résidentes sur un territoire économique : ménages, entreprises, associations.',
  x='Le critère est la résidence, et non la nationalité : une filiale étrangère installée en France en fait partie.',
  t='def', b=49)

# --------------------------------------- II.B Le circuit économique

c('Quel enchaînement fonde le circuit économique ?',
  'La production distribue des revenus, ces revenus financent la consommation et l’investissement, et ces dépenses relancent la production.',
  x='Le circuit est bouclé : la dépense des uns est le revenu des autres, ce qui rend les agents solidaires et non simplement concurrents.',
  t='mec', b=74)

c('Sous quelles formes les entreprises versent-elles des revenus aux autres agents ?',
  'Salaires, profits, loyers et intérêts.',
  x='Chaque forme rémunère un apport différent : le travail, le risque, la terre ou le capital prêté.',
  t='def', b=54)

c('Quelle différence y a-t-il entre une capacité et un besoin de financement ?',
  'La capacité est un excédent d’épargne, le besoin est un déficit qu’il faut couvrir par un crédit ou un emprunt.',
  x='Les agents en capacité financent ceux qui sont en besoin : c’est cet ajustement qui fait tenir le circuit.',
  t='dist', b=69)

c('Comment les échanges avec l’étranger agissent-ils sur la production nationale ?',
  'Un excédent des exportations sur les importations crée davantage de richesse sur le territoire.',
  x='Les importations, à l’inverse, sont une fuite : une part de la demande intérieure soutient la production d’un autre pays.',
  t='mec', b=72)

c('Par quels instruments l’État modifie-t-il la répartition des revenus ?',
  'Il prélève des impôts et des cotisations, puis redistribue sous forme d’allocations, de subventions et de services publics.',
  x='La redistribution agit donc en deux temps, et c’est leur solde qui détermine le revenu finalement disponible.',
  t='mec', b=60)

# ------------------------------------ II.C Les agents économiques

c('Quels sont les trois critères retenus par l’INSEE pour constituer un ménage ?',
  'Partager un même logement, avoir un budget commun, sans qu’un lien de parenté soit nécessaire.',
  x='Le ménage est donc une unité de résidence et de dépense, pas une famille au sens juridique.',
  t='def', b=83)

c('Qui compose la population hors ménage ?',
  'Les personnes vivant en habitation mobile, les sans-domicile et les personnes détenues.',
  x='Ces situations échappent au critère du logement, ce qui les rend difficiles à saisir dans les statistiques de revenu.',
  t='def', b=87)

c('Qu’est-ce qu’une entreprise en comptabilité nationale ?',
  'Une unité économique dont la fonction principale est de produire des biens et des services.',
  x='La définition est fonctionnelle : elle ne dit rien de la taille, du statut juridique ni du propriétaire.',
  t='def', b=88)

c('Sur quels quatre critères distingue-t-on les entreprises entre elles ?',
  'La nature du capital, le secteur d’activité, le statut juridique et la taille.',
  x='La nature du capital répond à la question « qui possède l’entreprise », et commande les trois autres dans bien des cas.',
  t='mec', b=91)

c('Quelle est la différence entre privatiser et nationaliser une entreprise ?',
  'Privatiser, c’est vendre une entreprise publique ; nationaliser, c’est en reprendre la totalité des parts.',
  x='Les deux mouvements traduisent un changement de doctrine sur le périmètre légitime de l’État dans la production.',
  t='dist', b=96)

c('Combien d’entreprises ont fait défaut en France en 2021, puis en 2025 ?',
  'Environ 27 500 en 2021, contre environ 67 000 en 2025.',
  x='Le creux de 2021 n’est pas un signe de bonne santé : il marque la mise sous perfusion des entreprises pendant la crise sanitaire.',
  t='fait', b=104)

c('Pourquoi les défaillances d’entreprises ont-elles bondi après la crise sanitaire ?',
  'Parce que les aides publiques avaient maintenu en vie des entreprises déjà condamnées, qui ont fermé une fois le soutien retiré.',
  x='Le chômage partiel rémunérait les salariés sans que l’activité reprenne : les défaillances ont été décalées, non évitées.',
  t='mec', b=112)

c('Quand le statut d’auto-entrepreneur a-t-il été créé, et quel nom porte-t-il depuis 2015 ?',
  'Créé en 2009, il s’appelle depuis 2015 le statut de micro-entrepreneur.',
  x='Le changement de nom accompagne un succès massif : l’activité peut être exercée à titre principal ou en complément.',
  t='fait', b=113)

c('Quelles facilités le statut de micro-entrepreneur offre-t-il ?',
  'Des démarches simplifiées, une exonération de TVA sous un seuil de chiffre d’affaires et un régime fiscal particulier.',
  x='Sa protection sociale est celle des indépendants, nettement moins étendue que celle d’un salarié.',
  t='def', b=114)

c('Pourquoi une entreprise a-t-elle intérêt à confier une tâche à un micro-entrepreneur ?',
  'Elle règle une facture au lieu de verser un salaire et des cotisations sociales, ce qui abaisse son coût.',
  x='L’économie réalisée par l’entreprise correspond très exactement à la protection dont le micro-entrepreneur ne bénéficie pas.',
  t='mec', b=121)

c('Pourquoi l’activité de micro-entrepreneur est-elle considérée comme précaire ?',
  'Parce que de faibles cotisations ouvrent de faibles droits : retraite, chômage, allocations familiales et frais de maladie sont moins couverts.',
  x='C’est l’argument central du débat sur l’ubérisation : le statut déplace le risque de l’entreprise vers le travailleur.',
  t='mec', b=123)

# ------------------- III. Entreprises, production et investissement

c('Que mesure le compte de résultat d’une entreprise, et que mesure son bilan ?',
  'Le compte de résultat retrace des flux sur une période ; le bilan photographie un stock de richesses à une date.',
  x='D’où la règle : on ne compare jamais un poste du compte de résultat à un poste du bilan sans rapporter l’un à l’autre.',
  t='dist', b=127)

c('Comment se décompose le passif d’une entreprise ?',
  'En fonds propres — capital social et bénéfices mis en réserve — et en dettes.',
  x='Le passif dit d’où vient l’argent ; l’actif dit à quoi il a servi. L’un finance donc toujours l’autre.',
  t='def', b=129)

c('Comment calcule-t-on le taux de marge d’une entreprise ?',
  'EBE / valeur ajoutée × 100.',
  x='Il indique la part de la richesse créée qui reste à l’entreprise une fois payés les salaires, les cotisations et les impôts de production.',
  t='form', b=133)

c('Comment calcule-t-on le taux d’autofinancement ?',
  'Épargne brute / FBCF × 100.',
  x='Au-delà de 100 %, l’entreprise couvre seule ses investissements ; en deçà, elle doit emprunter ou lever des fonds.',
  t='form', b=133)

c('Que signifie un taux d’autofinancement supérieur à 100 % ?',
  'L’entreprise dégage plus d’épargne qu’elle n’investit : elle finance seule ses investissements.',
  x='Le cours avertit qu’un taux très élevé peut aussi signaler un investissement trop timide plutôt qu’une bonne santé.',
  t='mec', b=135)

c('À quoi sert l’excédent brut d’exploitation dégagé par une entreprise ?',
  'À verser des intérêts aux créanciers, payer l’impôt sur les sociétés, distribuer des dividendes et constituer une épargne brute.',
  x='C’est l’ordre de passage : ce qui reste après ces trois prélèvements est ce qui finance directement l’investissement.',
  t='mec', b=144)

c('Qu’implique pour une entreprise un taux de marge de l’ordre de 15 % ?',
  'Les salaires, les cotisations et les impôts de production ont absorbé l’essentiel de la valeur ajoutée : il reste peu d’épargne.',
  x='Conséquence immédiate : pour investir, elle dépend de l’emprunt bancaire ou d’une levée de fonds.',
  t='mec', b=151)

c('Qu’est-ce qu’un investissement, et qu’est-ce qui l’en distingue d’une consommation intermédiaire ?',
  'L’investissement est l’achat d’un bien de production utilisé plus d’un an ; en deçà, il s’agit d’une consommation intermédiaire.',
  x='Le critère est donc purement la durée d’usage, non le montant ni la nature du bien.',
  t='dist', b=156)

c('Par quel agrégat mesure-t-on l’investissement matériel ?',
  'La formation brute de capital fixe (FBCF).',
  x='Elle recouvre les actifs corporels : bâtiments, machines, véhicules, logiciels, ainsi que les dépenses de recherche et développement.',
  t='def', b=159)

c('Qu’appelle-t-on un investissement immatériel ?',
  'L’achat d’actifs incorporels destinés à améliorer la production : brevets, licences, publicité, œuvres.',
  x='Son poids croissant explique que la FBCF seule sous-estime l’effort d’investissement des économies avancées.',
  t='def', b=162)

c('Quelle est la différence entre un investissement et un placement ?',
  'L’investissement augmente physiquement le stock de capital ; le placement achète un titre et accroît le patrimoine financier.',
  x='L’arbitrage entre les deux dépend de la rentabilité attendue et du taux d’intérêt servi par les titres.',
  t='dist', b=165)

c('Qu’est-ce qu’une obligation, et quelle position occupe celui qui l’achète ?',
  'Un titre de créance : l’acheteur prête de l’argent et devient créancier de l’émetteur.',
  x='L’émetteur s’engage à verser des coupons réguliers puis à rembourser le capital à l’échéance.',
  t='def', b=167)

c('Que mesure le taux de rentabilité interne (TRI) d’un projet ?',
  'La rentabilité annualisée moyenne de l’investissement.',
  x='Il se compare au coût du financement : un projet n’est engagé que si son TRI dépasse le taux d’intérêt.',
  t='def', b=177)

c('Que mesure le taux d’investissement ?',
  'La part de la richesse créée qui est consacrée à l’investissement.',
  x='Rapporté à la valeur ajoutée pour une entreprise ou une branche, au PIB pour un pays.',
  t='def', b=178)

c('Quelles sont les trois raisons qui poussent un agent à investir ?',
  'Une demande suffisante, une rentabilité attendue attractive, des conditions de financement favorables.',
  x='Le profit n’est pas une quatrième raison mais le préalable : sans lui, aucune des trois ne peut jouer.',
  t='mec', b=197)

c('Pourquoi une demande faible décourage-t-elle l’investissement ?',
  'Parce qu’investir créerait des capacités de production que personne n’utiliserait.',
  x='D’où les indicateurs surveillés : croissance du PIB, consommation intérieure, carnet de commandes, perspectives d’exportation.',
  t='mec', b=189)

c('Comment le taux d’intérêt agit-il sur la décision d’investir ?',
  'Plus il est bas et plus le crédit est accessible, plus l’investissement devient attractif.',
  x='Le taux fixe le coût du financement externe, auquel l’entreprise compare le rendement attendu du projet.',
  t='mec', b=196)

c('Quel événement des années 1970 a redonné du poids aux analyses de l’investissement par l’offre ?',
  'Les deux chocs pétroliers de 1973 et 1979, qui font passer le baril de 5 à 30 dollars.',
  x='La hausse des coûts de production entraîne des licenciements massifs : l’attention se déplace de la demande vers les marges des entreprises.',
  t='fait', b=199)

c('Quelle formule le chancelier Helmut Schmidt a-t-il donnée à l’analyse de l’investissement par les profits ?',
  '« Les profits d’aujourd’hui font les investissements de demain et les emplois d’après-demain. »',
  x='Elle résume l’argument de l’offre : restaurer la marge des entreprises est présenté comme la condition de l’emploi futur.',
  t='aut', b=199)

c('Quel économiste fonde l’analyse de l’investissement sur la demande ?',
  'John Maynard Keynes.',
  x='Pour lui, c’est l’anticipation de débouchés, et non la marge disponible, qui décide l’entrepreneur à investir.',
  t='aut', b=202)

c('Qu’énonce le principe du multiplicateur ?',
  'Une variation de l’investissement entraîne une variation plus forte du revenu.',
  x='Le revenu distribué est à son tour dépensé, ce qui relance la production : l’effet initial se propage par vagues successives.',
  t='mec', b=203)

c('Qu’énonce le principe de l’accélérateur, et à qui le doit-on ?',
  'Une variation de la demande provoque une variation plus que proportionnelle de l’investissement ; on le doit à Aftalion et Clark.',
  x='Il joue dans les deux sens : un simple ralentissement de la demande suffit à faire chuter l’investissement.',
  t='aut', b=204)

c('De combien le revenu varie-t-il pour une unité investie, en économie fermée puis en économie ouverte ?',
  'Cinq fois plus en économie fermée, deux fois et demie en économie ouverte.',
  x='L’écart vient des importations : une part de la relance fuit vers l’étranger au lieu d’alimenter la production nationale.',
  t='fait', b=207)

c('Que décrit l’oscillateur de Samuelson, formulé en 1939 ?',
  'L’enchaînement par lequel une variation de l’investissement modifie le revenu, qui modifie à son tour la demande.',
  x='En combinant multiplicateur et accélérateur, il montre que l’économie peut osciller sans choc extérieur.',
  t='aut', b=209)

c('Pourquoi l’investissement occupe-t-il une place singulière dans l’analyse économique ?',
  'Parce qu’il est à la fois une composante de la demande et un déterminant de l’offre.',
  x='Acheter une machine soutient immédiatement l’activité, puis accroît durablement les capacités de production.',
  t='mec', b=210)

c('Que vaut la propension à consommer des ménages retenue par le cours, et que signifie-t-elle ?',
  'Elle vaut 0,8 : les ménages consacrent 80 % de leur revenu à la consommation.',
  x='C’est elle qui fixe la valeur du multiplicateur : plus elle est élevée, plus une relance se diffuse.',
  t='fait', b=211)

c('Comment obtient-on le revenu disponible brut d’un ménage ?',
  'Revenus primaires + revenus de transfert − prélèvements obligatoires.',
  x='C’est le revenu réellement affecté à la consommation ou à l’épargne, donc la bonne base pour mesurer un niveau de vie.',
  t='form', b=213)

c('Qu’est-ce qui distingue un revenu primaire d’un revenu de transfert ?',
  'Le revenu primaire naît de la participation à la production ; le revenu de transfert est versé par l’État sans contrepartie productive.',
  x='Salaires, loyers et dividendes dans le premier cas ; allocations, retraites et indemnités dans le second.',
  t='dist', b=212)

c('Qu’appelle-t-on un revenu mixte ?',
  'Un revenu qui rémunère à la fois le travail et le capital de celui qui le perçoit.',
  x='C’est le cas de l’artisan ou du commerçant : son gain ne se décompose pas en salaire et en profit.',
  t='def', b=212)

c('Comment passe-t-on du salaire super brut au salaire net ?',
  'On retire les cotisations patronales pour obtenir le brut, puis les cotisations salariales pour obtenir le net.',
  x='Le super brut est le coût total du travail pour l’employeur ; l’écart avec le net finance la protection sociale.',
  t='mec', b=217)

c('Quel effet pervers le cours associe-t-il aux allégements de cotisations sur les bas salaires ?',
  'Ils peuvent dissuader les employeurs d’augmenter les salaires, pour ne pas perdre le bénéfice de l’allégement.',
  x='L’aide destinée à abaisser le coût du travail finit par enfermer des salariés juste au-dessus du minimum.',
  t='mec', b=218)

c('Qu’est-ce que le pouvoir d’achat ?',
  'La quantité de biens et de services qu’un revenu permet d’acquérir.',
  x='Il faut donc corriger le revenu de l’inflation : + 2 % de salaire avec + 3 % de prix est une perte.',
  t='def', b=229)

c('Que recouvrent les revenus primaires d’un ménage ?',
  'Les salaires, les revenus du capital — intérêts, dividendes, loyers — et les autres revenus du travail comme celui des indépendants.',
  x='Ils ont en commun de rémunérer une participation directe à l’activité productive, avant toute intervention de l’État.',
  t='def', b=222)

# ------------------------------------------ III.D Niveau de vie

c('Pourquoi rapporte-t-on le revenu d’un ménage à des unités de consommation ?',
  'Pour comparer des ménages de taille et de composition différentes à revenu identique.',
  x='Un couple avec trois enfants et une personne seule n’ont pas les mêmes besoins : sans pondération, la comparaison n’a pas de sens.',
  t='mec', b=237)

c('Comment calcule-t-on un taux de croissance entre deux valeurs ?',
  '(Valeur finale − valeur initiale) / valeur initiale × 100.',
  x='Le coefficient multiplicateur est le rapport brut VF/VI, et l’indice ce même rapport multiplié par 100.',
  t='form', b=239)

c('Comment passe-t-on d’un revenu nominal à un revenu réel ?',
  'Revenu nominal / indice des prix × 100.',
  x='Exemple du cours : 1 000 euros avec un indice de 110 donnent 909 euros de pouvoir d’achat.',
  t='form', b=242)

c('Que signifie exprimer une grandeur économique en volume ?',
  'La mesurer à prix constants, en retirant l’effet des prix par rapport à une année de référence.',
  x='On dit qu’on déflate la série. Sans cela, une hausse du PIB peut n’être qu’une hausse des prix.',
  t='def', b=245)

c('Qu’est-ce que l’inflation ?',
  'Une augmentation du niveau général des prix.',
  x='Le mot « général » est décisif : la hausse du prix d’un seul produit n’est pas de l’inflation.',
  t='def', b=247)

c('Par quel instrument mesure-t-on l’inflation, et sur quoi repose-t-il ?',
  'L’indice des prix à la consommation, construit sur un panier fixe de biens actualisé chaque année.',
  x='Le relevé porte sur environ 200 000 prix, ce qui donne une variation moyenne des prix payés par les ménages.',
  t='def', b=248)

c('Quelle différence y a-t-il entre désinflation et déflation ?',
  'La désinflation est un ralentissement de la hausse des prix ; la déflation est une baisse des prix.',
  x='Dans la désinflation les prix montent encore, mais moins vite ; au-delà de deux chiffres, on parle d’hyperinflation.',
  t='dist', b=250)

c('Qu’est-ce que l’inflation sous-jacente ?',
  'L’indice des prix dont on a retiré les postes volatils, c’est-à-dire l’énergie et l’alimentation.',
  x='Elle donne une vision plus stable de la tendance, moins sensible à un choc temporaire sur le pétrole.',
  t='def', b=251)

c('Qu’est-ce que l’effet d’encaisse réelle, aussi appelé effet Pigou ?',
  'En période de hausse des prix, les ménages épargnent davantage pour préserver la valeur de leur patrimoine, donc réduisent leurs dépenses.',
  x='Il joue contre l’inflation : la demande recule d’elle-même, sans intervention publique.',
  t='mec', b=256)

c('Qu’appelle-t-on la fuite devant la monnaie ?',
  'Le comportement inverse de l’épargne de précaution : on achète immédiatement avant que les prix ne montent encore.',
  x='En France, le cours relève que l’effet d’encaisse réelle l’emporte le plus souvent sur ce comportement.',
  t='mec', b=257)

c('Qu’est-ce que le revenu médian, et à combien s’élevait-il en France en 2023 ?',
  'Le revenu qui partage la population en deux moitiés égales ; il atteignait 2 150 euros.',
  x='On préfère la médiane à la moyenne parce qu’elle n’est pas tirée vers le haut par les très hauts revenus.',
  t='fait', b=260)

c('Comment le seuil de pauvreté est-il fixé, et quels montants donne-t-il en France ?',
  'À 50 % ou à 60 % du revenu médian, soit 1 073 euros et 1 288 euros pour une personne seule.',
  x='Le choix du seuil n’est pas technique : il fait passer le nombre de pauvres de 5,4 à 9,8 millions.',
  t='fait', b=261)

c('Pourquoi l’enrichissement d’un pays ne fait-il pas forcément reculer le nombre de pauvres ?',
  'Parce que le seuil est relatif : il monte avec le revenu médian, si bien qu’une hausse concentrée sur les plus riches ne change rien.',
  x='Seule une progression générale des revenus fait sortir des ménages de la pauvreté ainsi définie.',
  t='mec', b=265)

c('Qu’est-ce que le revenu de solidarité active ?',
  'Un revenu minimum garanti aux personnes sans emploi de plus de 25 ans, dont le montant varie selon la composition du foyer.',
  x='C’est un revenu de transfert : il n’a aucune contrepartie productive et relève de la fonction de redistribution.',
  t='def', b=267)

c('Comment le seuil de richesse est-il construit, et que gagne le 1 % le plus aisé en France ?',
  'Il vaut deux fois le revenu médian ; le 1 % le plus riche perçoit environ 7 512 euros par mois.',
  x='L’échelle se creuse ensuite très vite : 19 500 euros pour le dernier millième, 70 000 euros pour le dernier dix-millième.',
  t='fait', b=269)

# -------------------------------- III.E La consommation (macro)

c('Qu’est-ce que la consommation finale ?',
  'L’utilisation de biens et services parvenus à leur stade final, pour satisfaire directement les besoins des individus.',
  x='Elle concerne les ménages et les administrations publiques, par opposition à la consommation intermédiaire des entreprises.',
  t='def', b=275)

c('Qu’est-ce que la consommation effective d’un ménage ?',
  'Tout ce qu’il consomme réellement, quel que soit celui qui le finance.',
  x='Elle ajoute à ses propres dépenses les services que les administrations lui fournissent, comme l’école ou les soins remboursés.',
  t='def', b=276)

c('Qu’appelle-t-on dépenses pré-engagées, et quel poids représentent-elles ?',
  'Les dépenses difficilement compressibles — logement, chauffage, assurances — qui atteignent environ 30 % du revenu disponible.',
  x='Leur progression explique l’écart ressenti entre la hausse mesurée du pouvoir d’achat et le revenu réellement arbitrable.',
  t='fait', b=279)

c('Qu’énonce la loi d’Engel ?',
  'La part du budget consacrée à l’alimentation diminue à mesure que le revenu augmente.',
  x='Elle fonde une lecture du développement : la déformation de la structure de consommation signale l’enrichissement d’un pays.',
  t='aut', b=291)

c('Qu’est-ce qu’un coefficient budgétaire ?',
  'La part des dépenses consacrées à un bien dans le total des dépenses de consommation.',
  x='C’est l’outil issu des travaux d’Engel qui permet de suivre la déformation de la structure de consommation.',
  t='def', b=292)

c('De quel revenu la consommation dépend-elle selon Keynes, et dans quel ouvrage l’établit-il ?',
  'Du revenu courant, celui dont le ménage dispose aujourd’hui, dans la Théorie générale de l’emploi, de l’intérêt et de la monnaie (1936).',
  x='Le point est décisif : il s’oppose aux analyses qui font dépendre la dépense d’un revenu anticipé sur toute la vie.',
  t='aut', b=294)

c('Qu’énonce la loi psychologique fondamentale de Keynes ?',
  'La consommation augmente avec le revenu, mais moins vite que lui.',
  x='Elle implique que la propension à consommer décroît : la part épargnée grandit à mesure que le revenu s’élève.',
  t='aut', b=296)

c('Quel paradoxe Richard Easterlin met-il en évidence en 1974 ?',
  'À long terme, la hausse du revenu moyen d’un pays n’élève pas nécessairement le bonheur moyen déclaré.',
  x='Il ouvre la critique du PIB comme mesure du bien-être et justifie le recours à des indicateurs complémentaires.',
  t='aut', b=298)

# ------------------------------- III.F Les hypothèses de Keynes

c('Quelle est la différence entre propension moyenne et propension marginale à consommer ?',
  'La moyenne rapporte la consommation totale au revenu total ; la marginale ne porte que sur l’usage d’un revenu supplémentaire.',
  x='C/Y pour la première, ΔC/ΔY pour la seconde, comprise entre 0 et 1.',
  t='dist', b=303)

c('Pourquoi Keynes tient-il la propension moyenne à consommer pour décroissante ?',
  'Parce que la consommation progresse moins vite que le revenu : la part épargnée augmente avec le niveau de vie.',
  x='Cette décroissance est ce qui justifie, chez lui, l’intervention de l’État pour soutenir la demande.',
  t='mec', b=302)

c('Quel démenti empirique les travaux d’après 1945 apportent-ils à Keynes sur la consommation ?',
  'Le rapport consommation/revenu reste assez stable à long terme, au lieu de baisser.',
  x='Ce n’est pas la part consommée qui change, mais sa structure : la part alimentaire recule, les loisirs et la culture la compensent.',
  t='fait', b=309)

c('Que représente le taux d’intérêt pour les keynésiens ?',
  'Le prix de la renonciation à la liquidité.',
  x='Chez les classiques et chez Friedman, il rémunère au contraire la renonciation à la consommation présente.',
  t='dist', b=315)

c('Quelle thèse de Keynes Milton Friedman cherche-t-il à renverser avec le revenu permanent ?',
  'Celle qui fait dépendre la consommation du revenu courant, et qui justifie l’intervention de l’État.',
  x='Friedman part d’un fait : la consommation observée est bien plus stable que le revenu observé.',
  t='aut', b=325)

c('Comment Friedman décompose-t-il le revenu courant d’un individu ?',
  'En un revenu permanent, stable et anticipé, et un revenu transitoire, temporaire et aléatoire.',
  x='Qualification, expérience et perspectives d’emploi déterminent le premier ; une prime ou une maladie relèvent du second.',
  t='aut', b=327)

c('Que font les ménages d’une hausse de revenu qu’ils jugent passagère, selon Friedman ?',
  'Ils en épargnent l’essentiel, pour ne pas désorganiser un niveau de vie qu’ils tiennent à garder stable.',
  x='Symétriquement, une baisse temporaire les conduit à puiser dans leur épargne : c’est le lissage de la consommation.',
  t='mec', b=328)

c('Quelle conséquence la théorie du revenu permanent a-t-elle pour la politique budgétaire ?',
  'Une prime ponctuelle ou une baisse temporaire d’impôts a peu d’effet, puisqu’elle est perçue comme transitoire et donc épargnée.',
  x='C’est l’argument central contre les relances de court terme : seule une perspective durable modifie la dépense.',
  t='mec', b=333)

c('Qu’est-ce que l’actualisation ?',
  'L’opération qui ramène une somme future à sa valeur d’aujourd’hui, compte tenu du taux d’intérêt.',
  x='1 000 euros dans un an au taux de 10 % valent 909 euros aujourd’hui, puisque 909 placés rapporteraient ces 1 000.',
  t='def', b=331)

c('Dans quel ouvrage et en quelle année James Duesenberry expose-t-il son analyse de la consommation ?',
  'Income, Saving and the Theory of Consumer Behavior, en 1949.',
  x='Il y cherche à comprendre pourquoi la consommation varie moins que le revenu, contre la prévision keynésienne.',
  t='aut', b=336)

c('Qu’appelle-t-on effet de démonstration chez Duesenberry ?',
  'Les ménages imitent le mode de consommation des groupes plus aisés pour tenir leur rang.',
  x='La consommation dépend donc du revenu relatif, celui qu’on compare aux autres, et non du seul revenu absolu.',
  t='aut', b=347)

c('Qu’appelle-t-on effet de cliquet chez Duesenberry ?',
  'Le refus de réduire son niveau de vie quand le revenu baisse : on désépargne ou l’on s’endette pour le maintenir.',
  x='La consommation devient rigide à la baisse, ce qui stabilise la demande globale en période de récession.',
  t='aut', b=358)

c('Quelles deux variables Franco Modigliani ajoute-t-il au revenu courant pour expliquer la consommation ?',
  'Le patrimoine et l’âge.',
  x='Ils situent le ménage dans son cycle de vie, dimension absente aussi bien chez Keynes que chez Friedman.',
  t='aut', b=374)

c('Quelles sont les trois phases du cycle de vie décrites par Modigliani ?',
  'Endettement quand on est jeune, épargne pendant la vie active, désépargne à la retraite.',
  x='L’épargne y a une fonction précise : éviter que le niveau de vie ne chute au moment du passage à l’inactivité.',
  t='mec', b=378)

c('En quoi le modèle du cycle de vie rend-il compte de la situation américaine des années 1950 ?',
  'À cette époque l’héritage est rare : les ménages constituent eux-mêmes leur patrimoine par l’épargne de leur vie active.',
  x='La richesse y est donc accumulée puis consommée, exactement comme le modèle le suppose.',
  t='fait', b=393)

c('Pourquoi le modèle de Modigliani s’applique-t-il mal à l’Europe ?',
  'Parce qu’il suppose une retraite par capitalisation, alors que les systèmes européens fonctionnent par répartition.',
  x='Les actifs européens cotisent plutôt qu’ils n’épargnent : ils n’ont pas besoin d’accumuler autant pour leur retraite.',
  t='mec', b=410)

c('Quelle objection Thomas Piketty oppose-t-il au modèle du cycle de vie ?',
  'Que la période sans héritage décrite par Modigliani est une exception historique, et que l’héritage a repris une place centrale.',
  x='Si le patrimoine vient de la transmission plutôt que de l’épargne, la logique du cycle de vie cesse d’expliquer sa formation.',
  t='aut', b=414)

c('Quelle hypothèse du modèle de Modigliani le rationnement du crédit met-il en défaut ?',
  'Celle d’un endettement facile des jeunes sur la foi de leurs revenus futurs.',
  x='Lors d’un credit crunch, leur consommation redevient bornée par le revenu courant : un comportement keynésien, non anticipatif.',
  t='mec', b=418)

c('Pourquoi dit-on que Modigliani appartient à l’école de la synthèse ?',
  'Parce qu’il part du comportement d’un individu type et en agrège les décisions pour reconstituer les grandeurs globales.',
  x='Keynes refusait ce passage : pour lui, l’équilibre macroéconomique ne se déduit pas des comportements individuels.',
  t='mec', b=432)

# --------------------------------- IV. L'État, ses fonctions

c('Que représente le carré magique de Kaldor, et pourquoi le dit-on magique ?',
  'Les quatre objectifs d’une politique économique : croissance, plein emploi, stabilité des prix, équilibre extérieur. Il est magique car les atteindre tous ensemble est hors de portée.',
  x='Il sert surtout à montrer les arbitrages : soutenir la croissance dégrade souvent le solde extérieur ou les prix.',
  t='aut', b=445)

c('Comment mesure-t-on le solde extérieur dans le carré magique ?',
  'Solde de la balance des transactions courantes rapporté au PIB, en pourcentage.',
  x='La balance des transactions courantes additionne les trois balances : biens, services et revenus.',
  t='form', b=446)

c('Quelles sont les trois fonctions de l’État selon Richard Musgrave ?',
  'L’allocation des ressources, la stabilisation de l’activité et la redistribution des revenus.',
  x='Il les formule en 1959 dans sa théorie des finances publiques, et elles structurent encore l’analyse de l’État providence.',
  t='aut', b=449)

c('Qu’est-ce qui distingue une politique conjoncturelle d’une politique structurelle ?',
  'La première agit à court terme sur la demande ; la seconde transforme à long terme les structures de l’économie.',
  x='Budget et monnaie d’un côté ; concurrence, fiscalité et politique industrielle de l’autre.',
  t='dist', b=452)

c('Qu’appelle-t-on le policy mix ?',
  'L’articulation entre la politique budgétaire et la politique monétaire.',
  x='Leur cohérence décide de l’effet final : une relance budgétaire est annulée si la monnaie se resserre au même moment.',
  t='def', b=452)

c('Pourquoi un ralentissement de la croissance dégrade-t-il mécaniquement le solde public ?',
  'Les dépenses augmentent avec le chômage et la pauvreté, tandis que les recettes de TVA et de cotisations reculent.',
  x='Ce mouvement automatique est antérieur à toute décision : on l’appelle le jeu des stabilisateurs automatiques.',
  t='mec', b=457)

c('Comment un déficit public est-il financé ?',
  'Par l’endettement, c’est-à-dire l’émission d’obligations par l’État.',
  x='Le déficit est un flux annuel, la dette le stock accumulé de ces flux : confondre les deux est l’erreur la plus fréquente.',
  t='mec', b=464)

c('Quelles sont les trois crises de l’État providence identifiées par Pierre Rosanvallon en 1981 ?',
  'Une crise de financement, une crise d’efficacité et une crise de légitimité.',
  x='Elles se renforcent : le coût croissant nourrit le doute sur l’efficacité, qui mine à son tour le consentement.',
  t='aut', b=466)

c('Qu’affirme la courbe de Laffer ?',
  'Au-delà d’un certain seuil, une hausse du taux d’imposition réduit le produit de l’impôt.',
  x='Résumée par la formule « trop d’impôt tue l’impôt », elle sert d’argument aux politiques de baisse des prélèvements.',
  t='aut', b=470)

c('Quelles objections le cours oppose-t-il à la courbe de Laffer ?',
  'Son absence de fondement empirique solide, et le fait qu’à moyen terme une hausse du taux reste souvent sans effet observable.',
  x='Les comportements ne s’ajustent pas aussitôt : on ne cesse pas de travailler le lendemain d’une hausse d’impôts.',
  t='mec', b=472)

c('Quelle est la différence entre un impôt direct et un impôt indirect ?',
  'Le direct est payé par le contribuable sur son revenu ou son patrimoine ; l’indirect est perçu lors d’une transaction.',
  x='La TVA et les droits de consommation relèvent du second, ce qui les rend indolores mais régressifs.',
  t='dist', b=477)

c('Qu’est-ce qu’une niche fiscale ?',
  'Un avantage qui réduit l’impôt dû lorsque le contribuable remplit certaines conditions.',
  x='Le pacte Dutreil en est un exemple : il exonère largement la transmission d’une entreprise familiale.',
  t='def', b=478)

c('Combien la France compte-t-elle de taxes et de niches fiscales ?',
  '483 taxes et impôts, pour 474 niches fiscales.',
  x='Ce chiffre nourrit l’argument de l’illisibilité : presque autant de dérogations que de prélèvements.',
  t='fait', b=480)

c('Comment la modulation des taux de TVA illustre-t-elle l’usage de la fiscalité comme levier ?',
  'Elle rend certains produits plus ou moins chers et oriente ainsi la demande des consommateurs.',
  x='Exemple du cours : un soda à 5,5 % en magasin, à 10 % au restaurant, où la consommation sur place est traitée comme un loisir.',
  t='mec', b=486)

c('Quelle recette la TVA procure-t-elle à l’État français ?',
  'Environ 200 milliards d’euros.',
  x='C’est le premier impôt par son rendement, ce qui explique qu’on le réforme avec prudence malgré son caractère régressif.',
  t='fait', b=491)

c('Quelle est la différence entre un impôt progressif et un impôt dégressif ?',
  'Le taux s’élève avec le revenu dans le premier cas, il s’abaisse dans le second.',
  x='La TVA est de fait dégressive : à consommation égale, elle pèse davantage sur les bas revenus.',
  t='dist', b=503)

c('À quoi sert le quotient familial dans le calcul de l’impôt sur le revenu ?',
  'À diviser le revenu imposable par le nombre de parts du foyer, ce qui tient compte de sa taille.',
  x='Un couple avec trois enfants compte 4 parts : 40 000 euros de revenu donnent 10 000 euros par part, donc un taux nul.',
  t='mec', b=509)

c('Quelle part des Français s’acquitte de l’impôt sur le revenu ?',
  'Environ 45 % des contribuables.',
  x='La France compte 41 millions de foyers fiscaux, dont 1,3 million déclarent un patrimoine imposable.',
  t='fait', b=513)

c('Quand la CSG a-t-elle été créée, et dans quel but ?',
  'En 1991, pour élargir le financement de la Sécurité sociale à l’ensemble des revenus et non aux seuls salaires.',
  x='Son taux est passé de 1,1 % à sa création à environ 10 % aujourd’hui sur les revenus d’activité.',
  t='fait', b=516)

c('Par quel enchaînement une hausse des cotisations sociales peut-elle freiner la croissance ?',
  'Elle renchérit le coût du travail, pousse les prix à la hausse, dégrade la compétitivité et comprime le salaire net, donc la consommation.',
  x='C’est l’argument économique de la résistance à l’impôt, distinct de l’argument moral sur la justice fiscale.',
  t='mec', b=523)

c('Quelle thèse Alexis Spire défend-il dans Résistances à l’impôt, attachement à l’État (2018) ?',
  'Qu’on peut contester ou contourner l’impôt tout en restant attaché à l’État et à ses services publics.',
  x='La résistance ne traduit donc pas un rejet de la puissance publique, mais un doute sur l’équité du prélèvement.',
  t='aut', b=533)

c('Pourquoi Alexis Spire met-il sur le même plan une exonération et une aide versée ?',
  'Parce que dans les deux cas l’État supporte un coût et creuse son déficit.',
  x='En 2017, les exonérations fiscales représentaient 90 milliards d’euros, un montant largement invisible pour les citoyens.',
  t='fait', b=539)

c('De quoi dépend le consentement à l’impôt ?',
  'Du sentiment que le système est équitable, que les contreparties sont visibles et que la dépense publique est efficace.',
  x='Lorsque l’une de ces conditions manque, le consentement s’érode et la résistance augmente.',
  t='mec', b=541)

c('Qu’est-ce que le niveau de vie élargi ?',
  'Le revenu disponible auquel on ajoute la valeur des services publics reçus : éducation, santé, logement social.',
  x='Il montre que les inégalités réelles sont plus faibles que celles du revenu monétaire — un effet que les ménages perçoivent mal.',
  t='def', b=547)

c('Quel est l’effet de la redistribution sur les écarts de niveau de vie en France en 2023 ?',
  'Elle ramène l’écart à un rapport de 1 à 4, et 53 % des ménages reçoivent plus qu’ils ne versent.',
  x='Ce chiffre sert à répondre à l’idée que la redistribution serait sans effet sur les inégalités mesurées.',
  t='fait', b=559)

c('Comment la redistribution déforme-t-elle les revenus aux deux extrémités de l’échelle en France ?',
  'Les ménages modestes voient leur revenu multiplié par quatre, les plus aisés en perdent environ 40 %.',
  x='Chiffre utile pour objecter à l’idée que le système redistributif français serait devenu inopérant.',
  t='fait', b=560)

c('Comment la part des très grandes fortunes dans le PIB français a-t-elle évolué depuis 1996 ?',
  'Le patrimoine des dix premières fortunes est passé d’environ 6 % du PIB à 42 % en 2025, soit 2 612 milliards d’euros.',
  x='Le même cours relève que la progression de ces patrimoines dépasse largement celle du SMIC sur la période.',
  t='fait', b=567)

c('Pourquoi dit-on que le système français corrige mieux les revenus que les patrimoines ?',
  'Parce que l’impôt et les transferts agissent sur les flux annuels, tandis que le capital accumulé échappe largement au prélèvement.',
  x='D’où la persistance d’inégalités structurelles malgré une redistribution efficace sur le revenu disponible.',
  t='mec', b=570)

c('Qui serait concerné par la taxe Zucman, et selon quel principe ?',
  'Les foyers détenant plus de 100 millions d’euros, environ 1 800 en France, soumis à un impôt plancher de 2 % du patrimoine.',
  x='Elle est différentielle : on déduit du montant dû les impôts déjà acquittés, pour ne combler que l’écart au plancher.',
  t='def', b=574)

c('Quelles objections d’efficacité oppose-t-on à la taxe Zucman ?',
  'Un rendement surestimé à 20 milliards, dérisoire face à 170 milliards de déficit, et un risque de fuite des capitaux.',
  x='S’y ajoute l’effet redouté sur l’investissement, qu’une taxe sur le capital productif pourrait décourager.',
  t='mec', b=579)

c('Pourquoi l’évaluation du patrimoine rend-elle une taxe sur la fortune difficile à appliquer ?',
  'Parce que la richesse des entreprises non cotées est théorique et non liquide : elle ne peut pas servir à payer l’impôt.',
  x='Pour les sociétés cotées, la base retenue est la capitalisation boursière, qui varie fortement d’un jour à l’autre.',
  t='mec', b=588)

c('Qu’est-ce que le principe de non-confiscation en matière fiscale ?',
  'La règle, défendue par le Conseil constitutionnel, selon laquelle un impôt ne peut priver le contribuable d’une part excessive de ses revenus ou de son capital.',
  x='C’est l’argument opposé à l’IFI : un propriétaire riche en patrimoine mais pauvre en revenus ne peut vendre chaque année pour payer.',
  t='def', b=591)

c('Qu’est-ce qu’une plus-value latente, et pourquoi échappe-t-elle à l’impôt ?',
  'Un gain non encore réalisé sur un actif conservé : l’impôt n’est dû qu’à la vente, qui peut ne jamais avoir lieu.',
  x='Xavier Jaravel propose de la taxer au moment de la transmission, sur l’écart entre valeur d’achat et valeur à l’héritage.',
  t='def', b=601)

c('Qu’est-ce qu’un holding familial, et quel avantage fiscal procure-t-il en Europe ?',
  'Une société qui regroupe les actifs d’une famille ; en Europe, elle n’est pas imposée comme le serait un revenu.',
  x='Aux États-Unis ces structures sont imposées normalement, ce qui limite la transformation de revenus en capital non taxé.',
  t='def', b=611)

c('Que permet le pacte Dutreil, et à quelle condition ?',
  'Il exonère jusqu’à 75 %, voire 95 %, de la valeur d’une entreprise transmise, si les héritiers la conservent au moins six ans.',
  x='Conçu pour éviter la vente des entreprises familiales au décès, il sert parfois à transmettre d’immenses patrimoines presque sans impôt.',
  t='def', b=621)

c('Qu’appelle-t-on la charge de la dette, et quel autre nom porte-t-elle ?',
  'Les intérêts versés chaque année par l’État sur ses emprunts ; on parle aussi de service de la dette.',
  x='Elle pèse sur le budget courant sans financer aucune dépense nouvelle : c’est une charge rigide.',
  t='def', b=630)

c('À combien s’élève la dette publique française, et à quelle part du PIB ?',
  'Environ 3 400 milliards d’euros, soit à peu près 114 % du PIB.',
  x='C’est un stock accumulé d’emprunts successifs, à ne pas confondre avec le déficit, qui est le flux d’une seule année.',
  t='fait', b=639)

c('Que signifie « rouler la dette » ?',
  'Emprunter de nouveau pour rembourser un emprunt arrivé à échéance, donc repousser la date du remboursement.',
  x='L’opération est indolore tant que les taux restent bas ; elle devient coûteuse dès qu’ils remontent.',
  t='def', b=641)

c('Comment la charge de la dette française a-t-elle évolué entre 2021 et 2025 ?',
  'Elle est passée d’environ 36 milliards d’euros à près de 62 à 67 milliards.',
  x='La hausse ne vient pas d’un surcroît d’emprunt mais de la remontée des taux d’intérêt sur la dette renouvelée.',
  t='fait', b=646)

c('Pourquoi la France est-elle décrite comme prise dans une impasse budgétaire ?',
  'L’instabilité politique dégrade sa note, les investisseurs exigent davantage, la charge de la dette s’alourdit — et la hausse d’impôts qui la compenserait est refusée.',
  x='La charge d’intérêts atteignait déjà environ 2 % du PIB en 2024.',
  t='mec', b=654)

c('Quelle est la différence entre déficit public et déficit budgétaire ?',
  'Le déficit budgétaire ne concerne que l’État central, le déficit public englobe toutes les administrations.',
  x='Collectivités locales et sécurité sociale entrent dans le second : c’est lui que surveillent les règles européennes.',
  t='dist', b=662)

c('Quelle est la différence entre dette intérieure et dette extérieure ?',
  'La première est détenue par des créanciers résidents, la seconde par des créanciers étrangers.',
  x='La part extérieure crée une dépendance aux marchés : ces créanciers peuvent revendre les titres à tout moment.',
  t='dist', b=665)

c('Quels plafonds le Pacte de stabilité et de croissance impose-t-il aux États membres ?',
  'Un déficit public inférieur ou égal à 3 % du PIB et une dette publique inférieure ou égale à 60 % du PIB.',
  x='Ces deux seuils encadrent toute discussion budgétaire française, dont la dette dépasse aujourd’hui le double du plafond.',
  t='fait', b=670)

c('Qu’appelle-t-on un effet de ciseau dans les finances publiques ?',
  'La conjonction d’une hausse des dépenses et d’une baisse des recettes, qui creuse le solde des deux côtés à la fois.',
  x='En France, le « quoi qu’il en coûte » a gonflé les dépenses pendant que les exonérations de cotisations réduisaient les recettes.',
  t='mec', b=676)

c('En quoi consistait la politique du « quoi qu’il en coûte » ?',
  'L’État a pris en charge les coûts fixes des entreprises privées de chiffre d’affaires pendant la crise sanitaire.',
  x='Elle a évité une vague de faillites immédiate, au prix d’un endettement public durablement plus élevé.',
  t='fait', b=678)

c('Qu’est-ce qu’un prêt garanti par l’État, et dans quelles proportions l’État s’engage-t-il ?',
  'Un prêt bancaire dont l’État couvre la défaillance de l’emprunteur à hauteur de 90 % du capital.',
  x='Déployé en 2020 pour un montant de 140 à 170 milliards, il permettait aux PME d’emprunter jusqu’au quart de leur chiffre d’affaires.',
  t='def', b=680)

c('En quoi consistait le bouclier tarifaire mis en place en France ?',
  'Un ensemble de mesures limitant la répercussion de la flambée des prix de l’énergie, la hausse de l’électricité étant contenue à 15 %.',
  x='L’exemple sert à montrer qu’un État peut absorber un choc extérieur, au prix d’une dégradation de son solde.',
  t='fait', b=681)

c('Pourquoi l’annulation de la dette publique reste-t-elle une solution rarement retenue ?',
  'Parce qu’elle soulage le budget mais détruit la confiance des créanciers et expose le pays à l’isolement financier.',
  x='Un État qui n’honore pas sa signature ne peut plus emprunter qu’à des taux prohibitifs.',
  t='mec', b=687)

c('Par quel mécanisme l’inflation allège-t-elle le poids d’une dette publique ?',
  'Elle érode la valeur réelle des sommes dues, tandis que les recettes fiscales progressent avec les prix.',
  x='Le remède a une limite nette : une inflation trop forte déstabilise l’ensemble de l’économie.',
  t='mec', b=690)

c('En quoi consiste le quantitative easing, et quel effet a-t-il sur la dette publique ?',
  'La banque centrale rachète des titres de dette publique, ce qui abaisse les taux et soutient la liquidité.',
  x='Le remboursement devient moins coûteux, mais l’abondance de liquidités peut créer de nouveaux déséquilibres.',
  t='def', b=693)

c('Pourquoi la croissance économique est-elle présentée comme la solution la plus confortable à l’endettement ?',
  'Parce qu’elle gonfle les recettes fiscales sans qu’il soit nécessaire d’augmenter les taux ni de couper les dépenses.',
  x='Elle agit aussi sur le dénominateur du ratio : à dette constante, un PIB plus élevé abaisse le poids relatif de la dette.',
  t='mec', b=699)

c('Qu’est-ce qu’une dette publique soutenable ?',
  'Une dette que l’État peut rembourser sans compromettre son avenir économique.',
  x='Le critère n’est donc pas un niveau absolu mais un rapport entre la charge d’intérêts et la capacité à la financer.',
  t='def', b=706)

c('Quelle différence sépare la richesse comme flux de la richesse comme stock ?',
  'Le flux est le revenu perçu au cours d’une période ; le stock est le patrimoine détenu à un instant donné.',
  x='Le PIB mesure un flux ; les inégalités de patrimoine relèvent du stock, ce qui explique qu’elles se corrigent plus lentement.',
  t='dist', b=709)

c('Comment passe-t-on du PIB en valeur au PIB en volume ?',
  'PIB en valeur / indice des prix × 100.',
  x='On divise et multiplie pour des montants, alors que des taux de croissance peuvent s’additionner et se soustraire.',
  t='form', b=713)

c('Qu’est-ce que le PIB potentiel ?',
  'Le PIB qu’un pays atteindrait si tous ses facteurs de production étaient employés, sans choc, sans chômage ni inflation.',
  x='Il n’est pas observé mais estimé : c’est une référence théorique, à laquelle on compare le PIB effectif mesuré.',
  t='def', b=714)


c('Quel ordre de grandeur le travail domestique représente-t-il en France ?',
  'Davantage d’heures que le travail rémunéré.',
  x='Cuisine, ménage, linge et soins aux enfants forment le périmètre restreint ; bricolage, jardinage et courses l’élargissent.',
  t='fait', b=721)

c('Pourquoi le travail domestique constitue-t-il une limite du PIB ?',
  'Parce qu’il crée une valeur réelle qu’aucune transaction marchande n’enregistre.',
  x='Le PIB reste un bon indicateur de la production marchande, mais incomplet pour le bien-être et la valeur sociale produite.',
  t='mec', b=725)

c('Que recouvre ce que l’INSEE appelle l’économie non observée ?',
  'Les activités illicites, le travail dissimulé et les activités non marchandes comme l’économie domestique et le bénévolat.',
  x='L’activité dissimulée est évaluée à environ 37 milliards d’euros ; l’INSEE l’estime sans trancher sur sa légalité.',
  t='def', b=726)

c('Qu’apportent les comptes de la nation augmentée publiés par l’INSEE depuis novembre 2024 ?',
  'Une mesure du niveau de vie réel intégrant la redistribution élargie : santé, éducation publique, allocations.',
  x='Ils accompagnent la publication du PIB pour montrer l’effet concret de l’action des administrations sur les ménages.',
  t='fait', b=729)

c('Quelle est la différence entre le PIB et le revenu national brut ?',
  'Le PIB mesure la production sur le territoire ; le RNB retranche les revenus versés à l’étranger et ajoute ceux qui en proviennent.',
  x='L’écart devient important pour un pays à forte présence de filiales étrangères ou à nombreux travailleurs expatriés.',
  t='dist', b=732)

c('Que permet le tableau entrées-sorties établi par l’INSEE ?',
  'De relier la production de chaque secteur à ce que les autres secteurs lui achètent, ligne par ligne et colonne par colonne.',
  x='Il repose sur un principe comptable simple : le total des entrées égale le total des sorties.',
  t='def', b=743)

c('Pourquoi le tableau entrées-sorties est-il utile pour anticiper les effets d’une crise ?',
  'Parce qu’il montre comment une variation dans un secteur se propage à tous ceux qui en dépendent.',
  x='Exemple du cours : un recul de la construction entraîne les matériaux, le transport puis les services financiers.',
  t='mec', b=752)

c('Quelles sont les trois approches du PIB ?',
  'Par l’offre, par la demande et par les revenus.',
  x='La première mesure la richesse créée, la deuxième son utilisation finale, la troisième sa distribution entre les agents.',
  t='mec', b=761)

c('Que révèle la répartition des fortunes françaises par tranche de patrimoine ?',
  'Une concentration très forte dans le haut de la distribution : l’essentiel du patrimoine est détenu par une fraction réduite des ménages.',
  x='C’est ce qui distingue les inégalités de patrimoine des inégalités de revenu, bien moins concentrées.',
  t='fait', b=563)
