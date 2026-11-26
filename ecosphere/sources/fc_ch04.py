# -*- coding: utf-8 -*-
"""Première année — chapitre 4. Analyse microéconomique (I) : le consommateur."""

from fc_base import lot, c

L = lot(4)

c('Par quoi le consommateur se définit-il en microéconomie ?',
  'Par ses préférences et par les ressources dont il dispose, et non par son appartenance à une classe sociale.',
  x='Le changement de cadre est complet : l’analyse part de l’individu arbitrant, non d’un groupe social.',
  t='mec', b=10)

c('Qu’est-ce qu’une courbe d’indifférence ?',
  'L’ensemble des combinaisons de deux biens qui procurent au consommateur le même niveau de satisfaction.',
  x='On la dit d’indifférence parce que le consommateur n’a aucune raison de préférer un panier plutôt qu’un autre sur la même courbe.',
  t='def', b=18)

c('Qu’appelle-t-on la carte du consommateur ?',
  'L’ensemble de ses courbes d’indifférence.',
  x='Chaque courbe correspond à un niveau de satisfaction ; plus elle est éloignée de l’origine, plus ce niveau est élevé.',
  t='def', b=21)

c('Que suppose l’hypothèse de complétude des préférences ?',
  'Que l’individu peut se prononcer sur n’importe quelle combinaison de biens, présents comme futurs.',
  x='La dimension intertemporelle est incluse : il sait aussi comparer un panier d’aujourd’hui à un panier de demain.',
  t='def', b=23)

c('Que signifie l’hypothèse de transitivité, et quelle conséquence graphique a-t-elle ?',
  'Si le panier D est préféré à C et C à B, alors D est préféré à B ; les courbes d’indifférence ne peuvent donc pas se croiser.',
  x='Elle énonce la cohérence logique des choix ; les observations empiriques montrent qu’elle est souvent mise en défaut.',
  t='def', b=25)

c('Quel économiste critique frontalement l’approche microéconomique dans L’imposture économique (2014) ?',
  'Steve Keen.',
  x='Il s’appuie notamment sur le fait que les préférences observées ne respectent pas la transitivité postulée.',
  t='aut', b=28)

c('Qu’énonce l’hypothèse de non-satiété ?',
  'Le consommateur préfère toujours plus de biens à moins : il n’existe pas de point de satiété.',
  x='Kate Raworth la conteste : pourquoi supposer qu’on veuille toujours consommer davantage, et exclure de préférer moins ?',
  t='def', b=29)

c('Pourquoi l’hypothèse de non-satiété est-elle indispensable au modèle, malgré son irréalisme ?',
  'Sans elle, les courbes d’indifférence pourraient devenir discontinues ou mal ordonnées.',
  x='Grâce à elle, une courbe plus éloignée de l’origine correspond toujours à une utilité plus élevée : il n’existe pas de courbe maximale.',
  t='mec', b=36)

c('Que suppose l’hypothèse de continuité des préférences ?',
  'Que l’on peut toujours faire varier la consommation d’un bien d’une très petite quantité, sans saut brutal.',
  x='Elle repose sur une condition forte : que tous les biens soient suffisamment divisibles.',
  t='def', b=42)

c('Quel exemple le cours donne-t-il d’un bien indivisible qui contredit l’hypothèse de continuité ?',
  'Les médicaments, vendus en boîtes de 16 ou 30 comprimés.',
  x='D’où gaspillage, surconsommation et coût pour la Sécurité sociale ; certains pays pratiquent la vente à l’unité.',
  t='fait', b=56)

c('Pourquoi les économistes conservent-ils l’hypothèse de continuité ?',
  'Pour des raisons mathématiques : sans elle, on ne pourrait ni dériver, ni optimiser, ni résoudre proprement les modèles.',
  x='Elle n’est donc pas faite pour décrire les comportements réels, mais pour rendre le modèle maniable.',
  t='mec', b=61)

c('Que mesure le taux marginal de substitution ?',
  'Le nombre d’unités du bien Y auxquelles il faut renoncer pour obtenir une unité supplémentaire du bien X, à satisfaction constante.',
  x='Graphiquement, c’est la pente en un point de la courbe d’indifférence.',
  t='def', b=70)

c('Pourquoi le taux marginal de substitution est-il négatif ?',
  'Parce que les courbes d’indifférence sont décroissantes : consommer plus d’un bien impose de consommer moins de l’autre.',
  x='Le signe traduit donc le renoncement, non une perte de satisfaction : on reste sur la même courbe.',
  t='mec', b=74)

c('Qu’est-ce qui distingue une courbe d’indifférence d’une courbe d’utilité ?',
  'La courbe d’indifférence porte deux biens en abscisse et en ordonnée ; la courbe d’utilité porte un bien et le niveau d’utilité.',
  x='La première est bidimensionnelle et sert à comparer des paniers ; la seconde est unidimensionnelle.',
  t='dist', b=96)

c('Que mesure l’utilité marginale ?',
  'La satisfaction supplémentaire apportée par la consommation d’une unité de plus d’un bien.',
  x='Graphiquement, c’est la pente de la courbe d’utilité totale.',
  t='def', b=115)

c('Qu’énonce la loi de Gossen ?',
  'L’utilité marginale est décroissante : chaque unité supplémentaire apporte moins de satisfaction que la précédente.',
  x='L’utilité totale continue donc d’augmenter, mais de moins en moins vite : la courbe est croissante et concave.',
  t='aut', b=118)

c('Quelle condition caractérise l’équilibre du consommateur ?',
  'Le taux marginal de substitution égale le rapport des prix des deux biens.',
  x='Tant qu’ils diffèrent, le consommateur peut améliorer sa satisfaction en modifiant la composition de son panier.',
  t='form', b=128)

c('Qu’est-ce que l’effet de substitution ?',
  'Lorsque le prix d’un bien baisse, le consommateur en achète davantage et réduit sa consommation de l’autre bien.',
  x='Exemple du cours : le prix du burger baisse, celui de la glace non ; on consomme plus de burgers et moins de glaces.',
  t='def', b=129)

c('Qu’est-ce que l’effet revenu, et en quoi diffère-t-il de l’effet de substitution ?',
  'La baisse d’un prix élève le revenu réel, ce qui permet de consommer davantage des deux biens, et non d’un seul.',
  x='Toute variation de prix combine donc les deux effets : l’un déforme le panier, l’autre le dilate.',
  t='dist', b=131)

c('Que mesure une élasticité en économie ?',
  'Le rapport entre deux variations : de combien une grandeur réagit quand une autre change.',
  x='Un bien est dit élastique quand il réagit fortement à la variation considérée, inélastique quand il y réagit peu.',
  t='def', b=135)

c('Pourquoi l’élasticité d’un bien est-elle avantageuse pour le consommateur ?',
  'Parce qu’il dispose de substituts : si le prix monte, il peut changer de produit ou réduire facilement sa consommation.',
  x='Il n’est donc pas prisonnier du prix d’un seul bien, à la différence du cas inélastique.',
  t='mec', b=146)

c('Pourquoi une demande inélastique est-elle à double tranchant pour le producteur ?',
  'Il peut augmenter ses prix sans perdre de clients, mais baisser ses prix ne lui rapporte alors aucune demande supplémentaire.',
  x='L’inélasticité est aussi un signal : les consommateurs ne réagissent pas au prix, dans un sens comme dans l’autre.',
  t='mec', b=156)

c('Par rapport à quelles trois variables peut-on calculer l’élasticité de la demande ?',
  'Le prix du bien lui-même, le revenu du consommateur et le prix d’un autre bien.',
  x='Élasticité-prix, élasticité-revenu et élasticité-prix croisée : chacune sert à classer les biens différemment.',
  t='mec', b=187)

c('Que mesure l’élasticité-revenu, et que distingue-t-elle ?',
  'La variation de la demande quand le revenu varie ; elle sépare les biens inférieurs, dont la demande baisse, des biens normaux.',
  x='Une élasticité-revenu négative signale un bien inférieur : on l’abandonne dès qu’on en a les moyens.',
  t='def', b=195)

c('Quelle différence sépare un bien de Giffen d’un bien de Veblen ?',
  'Le bien de Giffen est un bien inférieur consommé par contrainte dans la pauvreté extrême ; le bien de Veblen est un bien de luxe consommé pour l’affichage social.',
  x='Les deux ont une demande qui monte avec le prix, mais pour des raisons exactement opposées.',
  t='dist', b=203)

c('Quel lien existe-t-il entre la loi d’Engel et l’élasticité-revenu ?',
  'La loi d’Engel décrit la déformation de la structure de consommation quand le revenu augmente : c’est une question d’élasticité-revenu avant la lettre.',
  x='Elle nomme un fait qui sera plus tard mesuré par un coefficient précis pour chaque poste de dépense.',
  t='mec', b=212)

c('Que signale une élasticité-prix croisée négative ?',
  'Que les deux biens sont complémentaires : la hausse du prix de l’un fait reculer la demande de l’autre.',
  x='Exemple du cours : si la place de cinéma renchérit, la consommation de popcorn diminue.',
  t='mec', b=222)

c('Que signale une élasticité-prix croisée positive ?',
  'Que les deux biens sont substituables : la hausse du prix de l’un accroît la demande de l’autre.',
  x='Exemple du cours : si le cinéma devient cher, les spectateurs se reportent sur la vidéo à la demande.',
  t='mec', b=233)

c('L’élasticité de la demande est-elle plus forte à court ou à long terme ?',
  'À long terme : les consommateurs ont le temps de s’adapter, de changer d’équipement et de chercher des alternatives.',
  x='À court terme, habitudes et équipements les immobilisent : la demande reste peu sensible au prix.',
  t='mec', b=250)

c('Comment les chocs pétroliers illustrent-ils le rôle du temps dans l’élasticité ?',
  'À court terme les acheteurs n’ont aucun substitut et continuent de consommer ; à long terme les entreprises modifient leurs procédés.',
  x='Le baril passe de 5 à 15 dollars en 1973 puis à 30 en 1979, sans effet immédiat sur les quantités consommées.',
  t='fait', b=256)

c('Quelle règle relie le nombre de substituts à l’élasticité de la demande ?',
  'Plus il existe de substituts, plus la demande est élastique ; sans substitut, elle est inélastique.',
  x='Or les substituts apparaissent surtout à long terme : les deux facteurs se renforcent l’un l’autre.',
  t='mec', b=264)

c('Comment la largeur de la catégorie de biens retenue modifie-t-elle l’élasticité mesurée ?',
  'Plus la catégorie est précise, plus la demande est élastique ; plus elle est large, plus elle est inélastique.',
  x='Exemple du cours : le skyr d’une marque a beaucoup de substituts, les produits laitiers dans leur ensemble n’en ont presque aucun.',
  t='mec', b=283)

c('Qu’est-ce qu’une fonction de production ?',
  'Une relation qui lie la quantité produite à la combinaison des facteurs travail et capital, notée Q = f(K, L).',
  x='Elle est au producteur ce que la fonction d’utilité est au consommateur : l’objet que l’on optimise.',
  t='def', b=294)

c('Comment les néoclassiques distinguent-ils court terme et long terme ?',
  'Le court terme est la période où au moins un facteur est fixe ; le long terme celle où tous sont variables.',
  x='Le temps est donc logique et non chronologique : sa durée dépend du secteur, de la technologie et de l’organisation.',
  t='dist', b=305)

c('Pourquoi suppose-t-on qu’à court terme le capital est fixe et le travail variable ?',
  'Parce qu’une entreprise confrontée à plus de commandes augmente d’abord les heures et les embauches, sans acheter aussitôt de machines.',
  x='Le travail est flexible, le capital demande du temps : l’hypothèse décrit un comportement réellement observé.',
  t='mec', b=300)

c('Qu’énonce la loi de la productivité marginale décroissante ?',
  'À capital fixe, ajouter du travail finit par faire baisser la production apportée par chaque travailleur supplémentaire.',
  x='Au début l’effet est fort ; au-delà d’un certain point, chaque embauche apporte de moins en moins.',
  t='def', b=315)

c('Quelle relation géométrique lie productivité marginale et productivité moyenne ?',
  'La productivité marginale coupe la productivité moyenne exactement à son maximum.',
  x='Tant que la marginale est au-dessus de la moyenne, celle-ci monte ; dès qu’elle passe en dessous, elle baisse.',
  t='mec', b=322)

c('Quelle différence y a-t-il entre rendements factoriels et rendements d’échelle ?',
  'Les rendements factoriels font varier un seul facteur à court terme ; les rendements d’échelle font varier tous les facteurs à long terme.',
  x='Les premiers mesurent une productivité marginale, les seconds un changement de taille de l’entreprise.',
  t='dist', b=327)

c('Qu’est-ce que l’intensité capitalistique ?',
  'Le rapport du capital au travail, c’est-à-dire la quantité de capital utilisée par unité de travail.',
  x='On la suppose constante quand on étudie les rendements d’échelle ; elle sert aussi à comparer pays et secteurs.',
  t='def', b=343)

c('Quels sont les trois types de rendements d’échelle ?',
  'Constants, croissants et décroissants, selon que la production augmente autant, plus ou moins que les facteurs.',
  x='Doubler les facteurs double la production dans le premier cas, fait davantage dans le deuxième, moins dans le troisième.',
  t='mec', b=347)

c('À quoi associe-t-on des rendements d’échelle croissants ?',
  'Aux économies d’échelle, à une meilleure organisation et à la spécialisation du travail.',
  x='On retrouve ici l’analyse de Smith : agrandir la production permet de diviser davantage le travail.',
  t='mec', b=356)

c('Qu’est-ce qui explique des rendements d’échelle décroissants ?',
  'Une mauvaise coordination, une gestion plus complexe et une taille devenue trop grande.',
  x='L’entreprise se heurte à des coûts d’organisation qui croissent plus vite que sa production.',
  t='mec', b=363)

c('Qu’est-ce qu’une isoquante ?',
  'L’ensemble des combinaisons de travail et de capital permettant d’obtenir un même niveau de production.',
  x='Elle est au producteur ce que la courbe d’indifférence est au consommateur : décroissante, elle traduit la substituabilité imparfaite des facteurs.',
  t='def', b=384)

c('Pourquoi deux isoquantes ne peuvent-elles jamais se croiser ?',
  'Parce qu’une même combinaison de facteurs donnerait alors deux niveaux de production différents.',
  x='C’est l’analogue de la transitivité chez le consommateur : une incohérence logique, non une impossibilité technique.',
  t='mec', b=398)

c('Qu’est-ce qu’une droite d’isocoût ?',
  'L’ensemble des combinaisons de capital et de travail ayant le même coût total, compte tenu du salaire et du coût du capital.',
  x='Elle joue pour le producteur le rôle de la droite budgétaire du consommateur.',
  t='def', b=410)

c('Où se situe la combinaison optimale de facteurs pour le producteur ?',
  'Au point de tangence entre l’isoquante visée et la droite d’isocoût.',
  x='C’est la combinaison qui permet d’atteindre un niveau de production donné au moindre coût.',
  t='mec', b=412)

c('Que mesure le taux marginal de substitution technique ?',
  'La quantité de capital à laquelle le producteur peut renoncer en employant une unité de travail de plus, à production constante.',
  x='Il est négatif et décroissant : plus on emploie de travail, moins chaque unité supplémentaire remplace de capital.',
  t='def', b=414)

c('À quoi le taux marginal de substitution technique est-il égal ?',
  'Au rapport des productivités marginales des deux facteurs.',
  x='Le producteur compare donc ce que rapporte une unité de travail de plus à ce que rapporte une unité de capital de plus.',
  t='form', b=440)

c('Quel arbitrage une hausse des cotisations sociales déclenche-t-elle chez le producteur ?',
  'Un effet de substitution : le travail renchérit, il est remplacé par du capital.',
  x='S’y ajoute un effet de budget : le producteur rationnel voit son budget réel baisser et réduit les deux facteurs.',
  t='mec', b=444)

c('Quelle est la différence entre coûts fixes et coûts variables ?',
  'Les coûts fixes existent même à production nulle ; les coûts variables augmentent avec la quantité produite.',
  x='Loyers, machines et assurances d’un côté ; matières premières, énergie et main-d’œuvre productive de l’autre.',
  t='dist', b=457)

c('Pourquoi le coût fixe moyen est-il toujours décroissant ?',
  'Parce qu’un coût constant se répartit sur un nombre croissant d’unités produites.',
  x='C’est le mécanisme élémentaire des économies d’échelle : produire plus dilue la charge fixe unitaire.',
  t='mec', b=470)

c('Pourquoi le coût variable moyen a-t-il une forme de U ?',
  'Il baisse d’abord grâce à une meilleure organisation, puis remonte sous l’effet des rendements décroissants.',
  x='La même logique donne au coût moyen total et au coût marginal leur forme en U.',
  t='mec', b=474)

c('Qu’est-ce que le coût marginal, et quelles relations géométriques vérifie-t-il ?',
  'Le coût de la dernière unité produite ; il coupe le coût moyen et le coût variable moyen en leur minimum.',
  x='Tant qu’il est en dessous d’une moyenne, celle-ci baisse ; dès qu’il passe au-dessus, elle remonte.',
  t='def', b=481)

c('Comment coûts et productivités varient-ils l’un par rapport à l’autre ?',
  'En sens inverse : le coût marginal baisse quand la productivité marginale monte, et le coût moyen baisse quand la productivité moyenne monte.',
  x='C’est pourquoi le maximum de la productivité marginale correspond exactement au minimum du coût marginal.',
  t='mec', b=502)

c('À quelle condition une entreprise est-elle rentable, et à quelle condition peut-elle continuer à court terme ?',
  'Elle est rentable si le prix couvre le coût moyen ; elle peut poursuivre à court terme tant que le prix couvre le coût variable moyen.',
  x='Dans ce second cas elle ne couvre pas ses coûts fixes, mais fermer coûterait davantage que continuer.',
  t='mec', b=506)

c('Qu’est-ce que la courbe de longue période chez le producteur ?',
  'La courbe qui enveloppe toutes les courbes de coût de courte période.',
  x='À long terme, l’entreprise peut choisir la taille d’équipement qui minimise son coût pour chaque niveau de production.',
  t='def', b=514)

c('Qu’est-ce qu’une déséconomie d’échelle ?',
  'Une situation où les coûts augmentent plus vite que la production.',
  x='C’est le pendant des économies d’échelle : au-delà d’une certaine taille, l’organisation devient plus coûteuse qu’efficace.',
  t='def', b=520)

c('Pourquoi le producteur néoclassique est-il dit price taker ?',
  'Parce que les hypothèses de la concurrence pure et parfaite lui retirent tout pouvoir sur le prix : c’est le marché qui le fixe.',
  x='Il ne décide donc que de la quantité à produire, en comparant le prix donné à son coût marginal.',
  t='mec', b=524)

c('Qu’est-ce qu’un équilibre partiel, et quelle critique lui adresse-t-on ?',
  'L’étude d’un marché indépendamment des autres, toutes choses égales par ailleurs ; on lui reproche que cette clause ne tienne pas.',
  x='Les effets prix et revenu le montrent : une variation sur un marché se répercute aussitôt sur les autres.',
  t='mec', b=526)

c('Quelle critique Steve Keen reprend-il de Hugo Sonnenschein sur la courbe de demande ?',
  'Que l’interdépendance des marchés rend sa forme incertaine : rien ne garantit qu’elle soit décroissante.',
  x='Les travaux de Sonnenschein datent de 1972-1974 ; la courbe décroissante reste pourtant utilisée comme si de rien n’était.',
  t='aut', b=530)

c('Pourquoi, même sur un seul marché, la réaction de la demande n’est-elle pas toujours prévisible ?',
  'Parce que l’effet de substitution et l’effet revenu jouent simultanément et peuvent se contrarier.',
  x='Selon le type de bien, le second renforce le premier ou le perturbe : la relation prix-quantité n’est pas mécanique.',
  t='mec', b=554)

c('Qu’est-ce qu’une boucle de rétroaction entre marchés ?',
  'Un choc sur un marché modifie les autres marchés, dont les effets reviennent ensuite affecter le marché de départ.',
  x='Un prix plus élevé enrichit le producteur, qui embauche, investit et emprunte : l’emploi et le crédit en sont modifiés à leur tour.',
  t='def', b=574)

c('Sur quel raisonnement Jean-Baptiste Say fonde-t-il sa loi des débouchés ?',
  'Produire distribue nécessairement des revenus — salaires, profits, rentes — qui servent à acheter les biens produits.',
  x='Il ne peut donc exister de manque global de débouchés : les crises sont sectorielles et temporaires, jamais générales.',
  t='aut', b=583)

c('Comment Walras transforme-t-il l’intuition de Say en système ?',
  'Il pose qu’une économie est un système d’équations comportant autant d’équations que d’inconnues, donc doté d’une solution.',
  x='Les inconnues sont tous les prix et toutes les quantités : l’équilibre général est simultané sur l’ensemble des marchés.',
  t='aut', b=609)

c('Quelle faille le raisonnement de Walras comporte-t-il ?',
  'Il suppose implicitement que les courbes d’offre et de demande se rencontrent toujours, ce que rien ne garantit.',
  x='Une offre durablement au-dessus de la demande ne donne aucun prix d’équilibre : l’existence de l’équilibre n’est pas automatique.',
  t='mec', b=619)

c('Quel problème Arrow et Debreu entreprennent-ils de résoudre ?',
  'Déterminer sous quelles conditions offre et demande se croisent nécessairement, sur tous les marchés en même temps.',
  x='Avoir autant d’équations que d’inconnues ne suffit pas : deux droites peuvent ne jamais se couper.',
  t='aut', b=628)

c('Quelles propriétés mathématiques Arrow et Debreu exigent-ils des fonctions d’offre et de demande ?',
  'Qu’elles soient continues et bornées.',
  x='Économiquement : pas de saut brutal, pas de comportement extrême, pas de coût ni de demande infinis.',
  t='aut', b=633)

c('Que signifie l’hypothèse de marchés complets chez Arrow et Debreu ?',
  'Qu’il existe un marché pour chaque bien présent, chaque bien futur et chaque service.',
  x='C’est l’hypothèse la plus irréaliste : elle suppose que l’on puisse acheter aujourd’hui tout bien livrable demain.',
  t='def', b=650)

c('Qu’est-ce que la dotation de survie dans le modèle d’Arrow-Debreu, et pourquoi pose-t-elle problème ?',
  'Un minimum de ressources que chaque agent possède au départ ; elle suppose une intervention extérieure au marché.',
  x='État, Église ou institutions doivent la fournir, ce qui contredit l’idée que le marché se suffit à lui-même.',
  t='mec', b=657)

c('Pourquoi Arrow et Debreu ont-ils besoin de rendements d’échelle décroissants ?',
  'Parce qu’ils rendent le coût marginal croissant, donc la courbe d’offre croissante, ce qui assure une intersection avec la demande.',
  x='Sans eux, l’offre pourrait ne jamais croiser la demande, et aucun prix d’équilibre n’existerait.',
  t='mec', b=672)

c('Pourquoi l’hypothèse d’absence de coûts fixes est-elle intenable économiquement ?',
  'Parce que l’industrie, les infrastructures et le numérique reposent entièrement sur d’énormes coûts fixes.',
  x='Elle n’est maintenue que pour assurer la continuité mathématique des fonctions.',
  t='mec', b=678)

c('Que démontre exactement le théorème d’Arrow-Debreu ?',
  'Que si des conditions très strictes sont réunies, alors un équilibre général existe — et rien de plus.',
  x='Il ne dit pas que l’économie réelle est à l’équilibre : il montre au contraire la fragilité de cette construction.',
  t='aut', b=685)

c('Quelle différence sépare la démarche positive de la démarche normative après Arrow-Debreu ?',
  'La positive cherche pourquoi les conditions ne sont pas remplies sans que l’économie sombre ; la normative tient l’équilibre pour un idéal à atteindre.',
  x='La seconde est l’approche néoclassique dominante : rapprocher le réel du modèle plutôt que l’inverse.',
  t='dist', b=696)

c('Quelle question Sonnenschein, Mantel et Debreu posent-ils, après celle de l’existence de l’équilibre ?',
  'Celle de la stabilité : le système converge-t-il vers l’équilibre, et y reste-t-il après un choc ?',
  x='Leur réponse est négative : rien ne garantit ni la convergence, ni le maintien, ni le retour.',
  t='aut', b=713)

c('Que montrent précisément les travaux de Sonnenschein, Mantel et Debreu sur la demande globale ?',
  'Qu’elle peut prendre n’importe quelle forme, être croissante ou chaotique, et ne pas réagir normalement aux prix.',
  x='Même avec des agents rationnels et des marchés bien modélisés, l’ensemble du système peut devenir imprévisible.',
  t='aut', b=742)

c('Qu’est-ce qu’une situation Pareto-optimale ?',
  'Une situation où l’on ne peut améliorer le sort d’un agent sans détériorer celui d’un autre.',
  x='C’est un critère d’efficacité et non de justice : il ne dit rien de l’égalité de la répartition.',
  t='def', b=753)

c('Qu’appelle-t-on rationalité substantielle dans le modèle néoclassique ?',
  'Une rationalité parfaite : l’agent connaît toutes les options et leurs conséquences, et maximise toujours son utilité ou son profit.',
  x='C’est cette hypothèse que Herbert Simon attaque, au nom de l’information et des capacités cognitives réellement disponibles.',
  t='def', b=783)

c('Quels trois arguments Herbert Simon oppose-t-il à la rationalité parfaite ?',
  'L’information est limitée, les capacités de calcul sont limitées, et les préférences ne sont pas toujours claires ni stables.',
  x='Personne ne compare toutes les formations de Parcoursup : on choisit dans un ensemble restreint, par habitude ou imitation.',
  t='aut', b=786)

c('Qu’est-ce que la rationalité limitée chez Herbert Simon ?',
  'Les individus restent rationnels, mais dans les bornes de leur information, de leur temps et de leurs capacités de calcul.',
  x='Ils ne cherchent donc pas le meilleur choix possible mais un choix suffisamment bon.',
  t='aut', b=811)

c('Que signifie le satisficing chez Herbert Simon ?',
  'Les agents ne maximisent pas : ils s’arrêtent dès qu’ils trouvent une solution acceptable et praticable.',
  x='Le mot combine satisfy et suffice : la recherche cesse au seuil du satisfaisant, non à l’optimum.',
  t='def', b=821)

c('Pourquoi la critique de Simon est-elle présentée comme un coup de grâce au modèle standard ?',
  'Parce que même si les conditions mathématiques étaient réunies, les agents réels seraient incapables de se comporter comme le modèle l’exige.',
  x='Le modèle reste élégant mathématiquement, mais fragile psychologiquement et sociologiquement.',
  t='mec', b=832)

c('Quel raisonnement George Akerlof développe-t-il dans The Market for Lemons (1970) ?',
  'Le vendeur connaît la qualité de sa voiture, l’acheteur non : celui-ci propose un prix moyen, qui chasse les bonnes voitures du marché.',
  x='Il ne reste que les mauvaises, la qualité moyenne baisse, la confiance disparaît et le marché peut s’effondrer.',
  t='aut', b=850)

c('Qu’est-ce qu’une asymétrie d’information bilatérale, et quel exemple le cours en donne-t-il ?',
  'Une situation où chacune des deux parties ignore quelque chose que l’autre sait ; l’embauche en est l’exemple type.',
  x='L’employeur ignore la motivation réelle du candidat, le candidat ignore l’ambiance et la charge de travail à venir.',
  t='def', b=870)

c('En quoi les critiques de Simon et d’Akerlof sont-elles complémentaires ?',
  'Simon pointe une limite cognitive, Akerlof une asymétrie stratégique : l’information peut aussi être volontairement cachée.',
  x='La transparence reste une hypothèse théorique ; l’asymétrie d’information est, elle, une réalité économique.',
  t='mec', b=890)

c('Que montre l’exemple des CDO sur le traitement de l’information ?',
  'Même disponible, légale et écrite, l’information n’est pas lue ni exploitée quand elle est trop longue et trop technique.',
  x='Le problème n’est donc pas seulement l’accès à l’information, mais le coût en temps et en attention de son traitement.',
  t='mec', b=902)

c('Quels sont les deux systèmes de pensée décrits par Daniel Kahneman en 2011 ?',
  'Le système 1, rapide, intuitif et émotionnel, et le système 2, lent, réfléchi et calculateur.',
  x='Le système 2 étant coûteux en effort, c’est le système 1 qui gouverne la plupart des décisions quotidiennes.',
  t='aut', b=918)

c('Qu’est-ce qu’un biais cognitif ?',
  'Une erreur systématique de jugement qui éloigne l’individu de la décision rationnelle du modèle standard.',
  x='Elle n’est pas aléatoire : elle va toujours dans le même sens, ce qui la rend prévisible et exploitable.',
  t='def', b=930)

c('En quoi consiste le biais de confirmation ?',
  'À chercher et retenir les seules informations qui confirment ce que l’on croit déjà, en écartant celles qui contredisent.',
  x='Après un accident d’avion, on remarque les autres accidents aériens en oubliant que la voiture est statistiquement plus dangereuse.',
  t='def', b=936)

c('En quoi consiste le biais d’ancrage ?',
  'Un chiffre initial, même arbitraire, influence toutes les évaluations qui suivent.',
  x='Dans l’expérience citée, le prix proposé pour une bouteille de vin se rapproche des deux derniers chiffres du numéro de sécurité sociale.',
  t='def', b=946)

c('Qu’est-ce qu’un nudge selon Richard Thaler ?',
  'Une manière d’orienter les comportements sans interdire ni obliger, en modifiant seulement la présentation des options.',
  x='Le don d’organes en est l’exemple type : ce n’est pas la rationalité qui change, c’est la formulation qui guide le choix.',
  t='def', b=959)

c('En quoi l’économie expérimentale consiste-t-elle ?',
  'À placer des individus réels dans des situations contrôlées et à comparer leurs décisions aux prédictions de l’homo œconomicus.',
  x='On y recrée des situations de marché, de négociation, de coopération ou de conflit.',
  t='def', b=978)

c('Quels comportements l’économie expérimentale observe-t-elle, contre le modèle de l’agent égoïste ?',
  'De l’altruisme, une recherche d’équité, la volonté de punir l’injustice et des comportements coopératifs.',
  x='L’homo œconomicus reste une abstraction utile, mais insuffisante pour décrire les comportements réels.',
  t='mec', b=988)

c('Quelle est la structure du dilemme du prisonnier ?',
  'Chaque joueur a intérêt individuellement à trahir, mais si les deux trahissent le résultat est pire que s’ils avaient coopéré.',
  x='Le problème n’est pas l’égoïsme mais l’incertitude : aucun joueur ne sait ce que l’autre va faire.',
  t='mec', b=994)

c('Quelle conclusion le dilemme du prisonnier impose-t-il à la théorie néoclassique ?',
  'La rationalité individuelle ne conduit pas nécessairement à la rationalité collective.',
  x='Sans coordination, la décision collective est sous-optimale : la somme des comportements rationnels n’est pas un optimum.',
  t='mec', b=997)

c('Pourquoi une entente entre entreprises d’un oligopole est-elle instable ?',
  'Parce que chaque entreprise a individuellement intérêt à tricher pour augmenter ses gains.',
  x='On retrouve exactement la logique du dilemme du prisonnier : la coopération est préférable mais la défection est rationnelle.',
  t='mec', b=1010)

c('Qu’est-ce qu’une prophétie autoréalisatrice, et quel exemple le cours en donne-t-il ?',
  'Une croyance qui provoque les comportements qui la rendent vraie ; la panique bancaire en est l’exemple type.',
  x='On croit la banque menacée, les déposants retirent leur argent, et la banque fait effectivement faillite.',
  t='def', b=1016)

c('Qu’est-ce qu’une défaillance de marché ?',
  'Une situation dans laquelle le marché concurrentiel n’alloue pas efficacement les ressources.',
  x='Elle apparaît dès qu’une des conditions de la concurrence pure et parfaite cesse d’être vérifiée.',
  t='def', b=1024)
