# -*- coding: utf-8 -*-
"""Première année — chapitre 6. La croissance économique."""

from fc_base import lot, c

L = lot(6)

c('Qu’est-ce que la croissance économique ?',
  'L’augmentation soutenue et durable de la production d’un pays sur longue période.',
  x='On la mesure par le PIB en volume, corrigé de l’inflation : c’est une croissance réelle, non nominale.',
  t='def', b=1)

c('Comment François Perroux définit-il la croissance ?',
  'L’augmentation soutenue, pendant une ou plusieurs périodes longues, d’un indicateur de dimension : pour une nation, le produit global net en termes réels.',
  x='Quatre éléments à retenir : augmentation soutenue, longue période, mesure quantitative, termes réels.',
  t='aut', b=6)

c('Comment Jean Arrous définit-il la croissance ?',
  'Un processus cumulatif d’interactions qui se traduit par une hausse continue de la productivité.',
  x='La croissance n’est donc pas une hausse mécanique du PIB mais repose sur des transformations profondes de l’économie.',
  t='aut', b=14)

c('Pourquoi la croissance ne se confond-elle pas avec le développement ?',
  'Elle est une condition souvent nécessaire mais jamais suffisante : un pays peut croître sans réduire les inégalités ni améliorer le bien-être.',
  x='La croissance est quantitative et comptable, le développement qualitatif : santé, éducation, pauvreté, inégalités.',
  t='dist', b=32)

c('Que signifie le caractère cumulatif de la croissance ?',
  'Une hausse annuelle faible mais maintenue longtemps produit des effets très importants.',
  x='La croissance est exponentielle et non linéaire : le temps est un facteur aussi décisif que le taux lui-même.',
  t='mec', b=38)

c('Qu’est-ce qu’un fait stylisé ?',
  'Une régularité statistique observée sur longue période et commune à plusieurs pays.',
  x='Il décrit les grandes caractéristiques de la croissance sans encore chercher à les expliquer.',
  t='def', b=51)

c('Qu’est-ce qu’un régime malthusien, au sens du chapitre sur la croissance ?',
  'Un régime où toute hausse de la production est absorbée par la croissance démographique, sans amélioration durable du niveau de vie.',
  x='Il caractérise les siècles qui précèdent la Révolution industrielle : agriculture dominante, productivité faible, techniques stables.',
  t='def', b=66)

c('Quelles transformations font apparaître la croissance moderne à la fin du XVIIIᵉ siècle ?',
  'Les innovations techniques, dont la machine à vapeur, la mécanisation, l’essor de l’industrie et la division du travail.',
  x='Elles produisent pour la première fois des gains de productivité durables, au Royaume-Uni d’abord.',
  t='fait', b=69)

c('Quelles grandes phases la croissance des pays développés a-t-elle connues depuis le XIXᵉ siècle ?',
  'Diffusion de l’industrialisation au XIXᵉ, forte croissance de 1945 à 1975, puis ralentissement depuis les années 1970.',
  x='La croissance évolue donc par cycles : elle n’est ni linéaire ni constante.',
  t='fait', b=86)

c('Pourquoi la convergence des pays n’est-elle pas automatique ?',
  'Parce que les écarts de PIB par habitant restent importants et que certains pays demeurent durablement en retard.',
  x='Le Japon après 1945, l’Asie de l’Est puis la Chine montrent que le rattrapage est possible, mais non garanti.',
  t='mec', b=103)

c('Pourquoi le PIB par habitant est-il préféré au PIB total pour mesurer le niveau de vie ?',
  'Parce que le PIB total ignore la taille de la population : la richesse créée peut être répartie entre bien plus d’habitants.',
  x='Un pays peut donc enregistrer une forte croissance globale sans que le revenu moyen progresse.',
  t='dist', b=117)

c('Comment décompose-t-on la croissance du PIB ?',
  'Croissance de la population + croissance du PIB par habitant.',
  x='Cette décomposition explique qu’une démographie dynamique gonfle le PIB total sans enrichir les individus.',
  t='form', b=127)

c('Quels sont les deux moteurs de la croissance économique ?',
  'L’augmentation de la quantité de travail et l’augmentation de la productivité.',
  x='Seule la seconde permet une amélioration durable du niveau de vie, puisqu’elle élève le produit par habitant.',
  t='mec', b=135)

c('Combien de temps faut-il pour doubler la production avec une croissance annuelle de 2 % ?',
  'Environ trente-cinq ans.',
  x='Illustration du caractère cumulatif : la croissance agit lentement mais puissamment dès qu’elle est régulière.',
  t='fait', b=166)

c('Pourquoi 1 % de croissance pendant cent ans ne donne-t-il pas une hausse de 100 % ?',
  'Parce que la croissance est exponentielle : chaque année, le taux s’applique au niveau déjà augmenté.',
  x='La progression se fait par multiplication et non par addition, ce qui creuse les écarts sur longue période.',
  t='mec', b=163)

c('Dans quel contexte et avec quelle intention Rostow publie-t-il Les étapes de la croissance économique en 1960 ?',
  'En pleine guerre froide, avec le sous-titre « un manifeste non communiste » : il veut montrer que le capitalisme permet aussi une croissance durable.',
  x='Il s’appuie sur le Royaume-Uni, premier pays industrialisé, pour en faire un modèle universel.',
  t='aut', b=194)

c('Quelles sont les cinq étapes de la croissance selon Rostow ?',
  'La société traditionnelle, les conditions préalables au décollage, le décollage, la marche vers la maturité et l’ère de la consommation de masse.',
  x='Il les tient pour successives et universelles : seuls les dates et la durée varient d’un pays à l’autre.',
  t='aut', b=201)

c('Qu’est-ce que le take-off chez Rostow, et à quoi le reconnaît-on ?',
  'L’étape centrale du modèle : le progrès technique s’accélère et le taux d’investissement atteint environ 10 % du PIB.',
  x='Des secteurs moteurs entraînent l’économie entière — le textile britannique — et la croissance devient auto-entretenue.',
  t='aut', b=220)

c('Qu’appelle-t-on leading sectors chez Rostow ?',
  'Les secteurs moteurs dont l’expansion entraîne l’ensemble de l’économie lors du décollage.',
  x='Le textile en Grande-Bretagne en est l’exemple ; un appareil politique vient soutenir leur développement.',
  t='def', b=225)

c('Que caractérise la marche vers la maturité chez Rostow ?',
  'La diffusion du progrès technique à toute l’économie, une industrialisation généralisée, l’urbanisation et l’exode rural.',
  x='La croissance devient la fonction normale de l’économie, autour de 2 % par an : le Royaume-Uni vers 1840.',
  t='aut', b=234)

c('Que caractérise l’ère de la consommation de masse chez Rostow ?',
  'L’amélioration des conditions de vie, le développement de l’État-providence, la tertiarisation et la hausse rapide du revenu par tête.',
  x='Elle correspond à l’Europe occidentale après 1945 : c’est l’horizon souhaitable du développement dans son modèle.',
  t='aut', b=242)

c('Quelles critiques majeures adresse-t-on au modèle de Rostow ?',
  'Une analyse descriptive et linéaire, l’absence des facteurs démographiques, l’hypothèse qu’aucun blocage n’existe, un optimisme excessif et un risque d’ethnocentrisme.',
  x='Le modèle est calqué sur l’expérience occidentale et suppose que tous les pays atteindront la consommation de masse.',
  t='mec', b=255)

c('Quelle réponse Gerschenkron oppose-t-il à Rostow sur les trajectoires de croissance ?',
  'Il n’existe pas de chemin unique : les trajectoires dépendent du retard initial et des conditions propres à chaque pays.',
  x='Dans Economic Backwardness in Historical Perspective (1962), il distingue early starters, followers et late comers.',
  t='aut', b=281)

c('Qu’implique le retard initial d’un pays selon Gerschenkron ?',
  'Plus un pays s’industrialise tard, plus sa trajectoire est spécifique : il ne peut pas reproduire le modèle britannique.',
  x='Financement, main-d’œuvre et structures diffèrent : le retard impose d’autres institutions, non les mêmes en différé.',
  t='aut', b=290)

c('Qu’appelle-t-on déviations graduelles chez Gerschenkron ?',
  'Le fait que deux pays partis de situations proches voient leurs trajectoires d’industrialisation diverger selon leur contexte national.',
  x='L’histoire, les institutions et la structure économique comptent : il n’existe pas de modèle universel identique pour tous.',
  t='def', b=297)

c('Pourquoi un pays retardataire peut-il sauter des étapes selon Gerschenkron ?',
  'Parce qu’il profite des innovations déjà existantes chez les pionniers, par transfert, imitation ou adoption directe de procédés avancés.',
  x='C’est l’inverse de Rostow : les étapes ne sont pas un passage obligé mais un chemin déjà défriché.',
  t='aut', b=302)

c('En quoi le retard peut-il devenir un avantage selon Gerschenkron ?',
  'Le pays tardif adopte directement des technologies modernes, substitue plus vite le capital au travail et crée de grandes entreprises.',
  x='Il saute les générations techniques intermédiaires que les pionniers ont dû traverser une à une.',
  t='aut', b=309)

c('Quelles institutions le rattrapage accéléré suppose-t-il selon Gerschenkron ?',
  'Des banques puissantes pour financer l’industrie, un État coordinateur et de grandes entreprises capables d’investir massivement.',
  x='L’Allemagne en est l’exemple : plus le retard est grand, plus les institutions de substitution doivent être puissantes.',
  t='aut', b=316)

c('Sur quel point essentiel Rostow et Gerschenkron convergent-ils ?',
  'L’industrialisation est le moteur historique de la croissance moderne.',
  x='Tous deux partent de la Révolution industrielle anglaise et voient dans le passage de l’agricole à l’industriel le fait décisif.',
  t='mec', b=339)

c('Qu’est-ce que la stagnation séculaire ?',
  'Une croissance durablement faible, voire quasi nulle, installée sur une très longue période.',
  x='Le mot séculaire marque qu’il ne s’agit pas d’un creux conjoncturel mais d’un régime appelé à durer.',
  t='def', b=373)

c('Qui introduit la notion de stagnation séculaire, et dans quel contexte ?',
  'Alvin Hansen, en 1938, alors président de l’American Economic Association.',
  x='Il observe le ralentissement démographique américain, l’insuffisance de l’investissement privé et la raréfaction des grandes innovations.',
  t='aut', b=388)

c('Pourquoi le concept de stagnation séculaire tombe-t-il dans l’oubli après 1945 ?',
  'Parce que la forte croissance de l’après-guerre paraît démentir les craintes de Hansen.',
  x='Il faudra la crise de 2008 pour que le diagnostic d’une faible croissance durable redevienne crédible.',
  t='fait', b=395)

c('Qui réactive le concept de stagnation séculaire, et sur quel constat ?',
  'Larry Summers en 2013 : une croissance faible malgré des taux très bas et des politiques monétaires très expansionnistes.',
  x='Il y voit un déséquilibre structurel durable entre épargne et investissement, et non un simple creux conjoncturel.',
  t='aut', b=397)

c('En quoi la crise de 2008 marque-t-elle une rupture dans les trajectoires de croissance ?',
  'Chute du PIB, hausse du chômage, envolée du ratio dette publique sur PIB et ralentissement durable de la croissance potentielle.',
  x='Même lorsque la reprise vient, elle est plus faible que lors des cycles précédents : le niveau d’avant n’est pas retrouvé.',
  t='fait', b=413)

c('Quel paradoxe Daniel Cohen souligne-t-il dans Le monde est clos et le désir infini (2015) ?',
  'Les innovations numériques transforment profondément les modes de vie sans produire de forte croissance mesurée du PIB.',
  x='Il parle d’une « révolution industrielle sans croissance » : le progrès technique s’est détaché de la productivité.',
  t='aut', b=434)

c('Quel précédent ancien la stagnation séculaire retrouve-t-elle chez Ricardo ?',
  'L’état stationnaire : hausse du prix des terres, baisse tendancielle du profit et coûts croissants finissent par arrêter la croissance.',
  x='Le contexte diffère, mais l’intuition est la même : la croissance n’est pas nécessairement illimitée.',
  t='aut', b=441)

c('Quelle est la thèse de Robert Gordon dans The Rise and Fall of American Growth (2016) ?',
  'Les innovations actuelles sont moins transformatrices que celles des grandes révolutions industrielles, d’où une croissance potentielle durablement plus faible.',
  x='Électricité, moteur, eau courante et transports avaient changé la production ; le numérique change surtout les usages.',
  t='aut', b=452)

c('Pourquoi Gordon situe-t-il la stagnation séculaire du côté de l’offre ?',
  'Parce que le problème vient selon lui de l’incapacité du système productif à générer assez de progrès technique, non d’un manque de débouchés.',
  x='Baisse de productivité, faiblesse de l’investissement et ralentissement de l’innovation forment un cercle vicieux.',
  t='mec', b=454)

c('Quels mécanismes Summers et Krugman invoquent-ils pour expliquer l’insuffisance de la demande ?',
  'La montée des inégalités, un excès d’épargne mondiale, la faiblesse de l’investissement privé, le ralentissement démographique et l’épargne de précaution.',
  x='Les ménages les plus riches épargnent une part plus forte de leur revenu : les inégalités pèsent directement sur les débouchés.',
  t='aut', b=473)

c('En quoi l’excès d’épargne renverse-t-il la vision classique ?',
  'Loin de financer l’investissement productif, il alimente les marchés financiers et des bulles, sans gain de croissance réelle.',
  x='Même avec des taux très bas, l’investissement ne repart pas : c’est le signe d’un déséquilibre structurel entre épargne et investissement.',
  t='mec', b=484)

c('Pourquoi le diagnostic sur la stagnation séculaire commande-t-il le remède ?',
  'Un problème d’offre appelle recherche, éducation et innovation ; un problème de demande appelle réduction des inégalités et politiques budgétaires actives.',
  x='C’est pourquoi le débat offre/demande n’est pas académique : il décide de la politique économique à conduire.',
  t='mec', b=494)

c('Qu’est-ce que la croissance potentielle ?',
  'Le rythme qu’une économie pourrait soutenir si tous ses facteurs étaient pleinement employés, sans choc de demande ni tension inflationniste.',
  x='C’est une référence théorique, la vitesse de croisière soutenable, et non la croissance observée.',
  t='def', b=507)

c('De quels facteurs la croissance potentielle dépend-elle ?',
  'De facteurs structurels : la productivité, la démographie, le stock de capital et le progrès technique.',
  x='La croissance effective, elle, dépend de facteurs conjoncturels, ce qui la rend bien plus volatile.',
  t='mec', b=517)

c('Que signale un output gap positif ?',
  'L’économie produit au-delà de ce qu’elle peut soutenir : pénuries de capacités, hausse des salaires, risque d’inflation.',
  x='Un output gap négatif signale au contraire une sous-activité : chômage et capacités inutilisées.',
  t='mec', b=550, aussi=['1'])

c('Comment la réponse budgétaire à la crise de 2008 a-t-elle différé entre la zone euro et les États-Unis ?',
  'La dette publique a progressé d’environ 20 points de PIB en zone euro contre plus de 40 aux États-Unis.',
  x='La réponse américaine a donc été nettement plus expansive : l’endettement y a été assumé pour soutenir l’activité.',
  t='fait', b=583)

c('Comment la baisse de la croissance potentielle se lit-elle différemment des deux côtés de l’Atlantique ?',
  'Aux États-Unis elle marque une rupture avec les années 1998-2007 ; en zone euro elle prolonge une tendance déjà modérée.',
  x='Le recul est commun, mais sa signification diffère : dégradation d’une norme d’un côté, continuité de l’autre.',
  t='mec', b=597)

c('Quels symptômes combinés font évoquer une stagnation séculaire plutôt qu’un simple choc conjoncturel ?',
  'Croissance potentielle affaiblie, output gaps négatifs persistants, productivité en recul malgré le progrès technique, investissement faible, inflation contenue et chômage durable.',
  x='C’est leur persistance conjointe, et non chacun pris isolément, qui oriente vers un diagnostic structurel.',
  t='mec', b=602)

c('Qui a cherché le premier à mesurer les sources de la croissance, et qui a repris sa méthode en France ?',
  'Robert Solow aux États-Unis ; en France Jean Carré, Paul Dubois et Edmond Malinvaud dans La croissance française (1972).',
  x='Leur objectif était d’expliquer la forte croissance française des Trente Glorieuses.',
  t='aut', b=624)

c('Sur quelles deux hypothèses repose la fonction de production de Cobb-Douglas ?',
  'La substituabilité des facteurs de production et des rendements d’échelle constants.',
  x='Doubler capital et travail double la production, et l’on peut remplacer l’un par l’autre : deux hypothèses contestées.',
  t='mec', b=644)

c('Quelle objection oppose-t-on à l’hypothèse de substituabilité des facteurs ?',
  'Dans la réalité, travail et capital sont largement complémentaires : une machine sans opérateur ne produit rien.',
  x='Leur combinaison accroît la production bien plus que chacun pris isolément.',
  t='mec', b=650)

c('Que permet la décomposition de la croissance par la fonction de production ?',
  'De mesurer séparément la contribution du capital et celle du travail, puis d’isoler ce qui reste inexpliqué.',
  x='Ce résidu inexpliqué est précisément ce que l’on appellera la productivité globale des facteurs.',
  t='mec', b=659)

c('Quel était le taux de croissance annuel moyen de la France entre 1951 et 1973 ?',
  '5,2 % par an.',
  x='Un niveau jamais atteint auparavant et jamais retrouvé depuis : c’est lui que Carré, Dubois et Malinvaud cherchent à expliquer.',
  t='fait', b=666)

c('Quelles contributions respectives le travail et le capital apportent-ils à la croissance française des Trente Glorieuses ?',
  '0,5 point pour le travail et 1,5 point pour le capital, sur 5,2 points au total.',
  x='Ensemble ils n’expliquent donc que 2 points : l’essentiel de la croissance reste à expliquer.',
  t='fait', b=675)

c('Qu’est-ce que la productivité globale des facteurs ?',
  'La part de la croissance qui ne s’explique ni par le travail, ni par le capital.',
  x='Dans la France des Trente Glorieuses, elle pèse 3,1 points sur 5,2, soit environ 60 % de la croissance.',
  t='def', b=689)

c('Comment interprétait-on la productivité globale des facteurs à l’époque de Carré, Dubois et Malinvaud ?',
  'Comme la mesure du progrès technique : organisation du travail, innovations, apprentissage, diffusion des technologies.',
  x='C’est l’interprétation la plus courante du résidu, mais elle n’est pas la seule possible.',
  t='mec', b=693)

c('Pourquoi certains économistes disent-ils que le résidu de Solow mesure surtout notre ignorance ?',
  'Parce qu’on sait seulement qu’il ne vient ni du travail ni du capital, sans pouvoir y distinguer organisation, compétences, technologie et institutions.',
  x='Solow lui-même parlait d’une « manne tombée du ciel » : une richesse dont on ignore la source précise.',
  t='aut', b=706)

c('Qu’est-ce que la croissance extensive ?',
  'Une croissance obtenue en mobilisant davantage de travail et de capital, sans que l’économie devienne plus efficace.',
  x='Elle s’oppose à la croissance intensive, qui repose sur les gains de productivité.',
  t='def', b=721)

c('Par quels deux soldes la population d’un pays augmente-t-elle ?',
  'Le solde naturel, différence entre naissances et décès, et le solde migratoire, différence entre entrées et sorties.',
  x='C’est pourquoi les flux migratoires sont un enjeu économique : ils accroissent rapidement le facteur travail.',
  t='mec', b=728)

c('Pourquoi la population active est-elle autant une variable institutionnelle que démographique ?',
  'Parce que la durée des études et l’âge de la retraite déterminent le moment d’entrée et de sortie du marché du travail.',
  x='Un report de l’âge de la retraite accroît la population active sans aucune naissance supplémentaire.',
  t='mec', b=733)

c('Quelle évolution explique une grande part de la croissance du facteur travail en France au XXᵉ siècle ?',
  'L’entrée massive des femmes sur le marché du travail et surtout leur maintien durable dans l’emploi à partir de la fin des années 1960.',
  x='À la différence des périodes de guerre, où le remplacement était temporaire, c’est ici une transformation structurelle.',
  t='fait', b=744)

c('Quelle innovation le cours retient-il comme tournant de l’accumulation du capital, et à quelle date ?',
  'La machine à vapeur, brevetée par James Watt en 1769.',
  x='Elle remplace la force animale et hydraulique par une énergie mécanique plus puissante et plus flexible.',
  t='fait', b=762)

c('Pourquoi la FBCF est-elle un indicateur avancé de croissance ?',
  'Parce qu’elle accroît le stock de capital et la capacité de production : elle prépare la croissance future.',
  x='C’est la traduction comptable du théorème de Schmidt : les investissements d’aujourd’hui font les emplois d’après-demain.',
  t='mec', b=767)

c('Quelles limites la croissance extensive rencontre-t-elle ?',
  'Des limites démographiques, les rendements décroissants, les contraintes budgétaires et des limites sociales.',
  x='À long terme, la croissance ne peut donc pas reposer sur la seule accumulation des facteurs : d’où l’attention portée à la productivité.',
  t='mec', b=782)

c('Pourquoi mesure-t-on la productivité en heures travaillées plutôt qu’en effectifs ?',
  'Parce que deux pays peuvent employer autant de travailleurs avec des durées de travail très différentes.',
  x='La Chine dépasse souvent 45 heures quand la durée légale française est de 35 : compter les têtes fausserait la comparaison.',
  t='mec', b=804)

c('Comment calcule-t-on la productivité horaire du travail ?',
  'PIB divisé par le nombre total d’heures travaillées.',
  x='C’est la mesure la plus précise pour les comparaisons internationales, quand les données existent.',
  t='form', b=812)

c('Pourquoi la productivité baisse-t-elle mécaniquement quand l’emploi progresse plus vite que la production ?',
  'Parce que le dénominateur augmente sans que le numérateur suive : le rapport diminue de lui-même.',
  x='Une baisse de productivité peut donc résulter d’une politique de l’emploi réussie, et non d’une inefficacité.',
  t='mec', b=828)

c('Comment la réforme de l’apprentissage a-t-elle pesé sur la productivité française ?',
  'Le nombre d’apprentis est passé d’environ 400 000 à plus d’un million en 2024, or un apprenti travaille moins et se forme encore.',
  x='L’emploi croît vite, la production non : le ratio baisse sans que l’économie soit devenue moins efficace.',
  t='fait', b=845)

c('Qu’est-ce qu’un effet d’aubaine ?',
  'Le fait qu’un agent bénéficie d’une aide publique alors qu’il aurait adopté le même comportement sans elle.',
  x='L’aide ne change alors pas la décision : elle en réduit seulement le coût, et devient un simple transfert.',
  t='def', b=857)

c('Qu’est-ce qu’une entreprise zombie, et comment la crise sanitaire en a-t-elle créé ?',
  'Une entreprise à faible productivité maintenue en vie artificiellement ; le chômage partiel a préservé leurs emplois pendant la crise.',
  x='Contrairement aux États-Unis, le chômage n’a pas explosé en France : la main-d’œuvre est restée, la production a reculé.',
  t='def', b=884)

c('Quelle explication plus optimiste oppose-t-on à la thèse pessimiste de Gordon sur la productivité ?',
  'Il existe un délai entre l’apparition d’une innovation et ses effets : il faut adapter l’organisation et former les salariés.',
  x='La productivité pourrait donc accélérer plus tard : le ralentissement serait transitoire et non structurel.',
  t='mec', b=899)

c('Pourquoi Philippe Aghion estime-t-il que la productivité réelle est sous-estimée ?',
  'Une partie des innovations numériques est gratuite et les améliorations de qualité sont mal mesurées par le PIB.',
  x='Le PIB ne capte donc pas toute la valeur créée : le ralentissement mesuré serait en partie un problème de mesure.',
  t='aut', b=904)

c('Quels sont les cinq déterminants de la productivité du travail ?',
  'La quantité d’heures travaillées, l’intensité capitalistique, le progrès technique, le capital humain et l’organisation du travail.',
  x='À long terme, le progrès technique est le déterminant fondamental : les autres finissent par buter sur des rendements décroissants.',
  t='mec', b=967)

c('Pourquoi allonger la durée du travail n’élève-t-il pas proportionnellement la production ?',
  'À cause de la fatigue, des rendements décroissants et de la baisse d’efficacité marginale.',
  x='Plus d’heures ne signifie donc pas plus de production dans la même proportion.',
  t='mec', b=918)

c('Qu’est-ce que le progrès technique en macroéconomie ?',
  'Tout ce qui permet de produire plus avec la même quantité de facteurs, ou autant avec moins.',
  x='Il recouvre les innovations technologiques, organisationnelles, la formation et une meilleure allocation des ressources.',
  t='def', b=937)

c('Comment la durée annuelle du travail a-t-elle évolué en France depuis 1870 ?',
  'Elle est passée d’environ 3 000 heures à 1 500 heures.',
  x='Chaque actif y est aujourd’hui bien plus productif : la baisse du temps de travail est le produit de la croissance, non son échec.',
  t='fait', b=985)

c('Quand la cinquième semaine de congés payés et les 35 heures ont-elles été instaurées en France ?',
  'En 1982 pour les congés, en 1998 pour la durée hebdomadaire.',
  x='Environ 70 % des salariés sont aux 35 heures, les autres restant soumis à une durée légale de 39 heures.',
  t='fait', b=980)

c('Pourquoi parle-t-on de productivité « apparente » du travail ?',
  'Parce qu’elle intègre aussi l’effet du capital, de la formation et de l’organisation, et pas seulement l’effort humain.',
  x='Le caissier n’est pas plus habile qu’avant : il dispose du scan automatique et de logiciels.',
  t='def', b=991)

c('Comment calcule-t-on la productivité globale des facteurs ?',
  'Croissance de la production moins contribution du travail moins contribution du capital.',
  x='On ne la mesure donc jamais directement : c’est un résidu, ce qui explique les réserves sur son interprétation.',
  t='form', b=1019)

c('Entre quels usages les gains de productivité peuvent-ils être répartis ?',
  'Une hausse des salaires, une hausse des profits, ou une baisse des prix.',
  x='Le choix décide de qui en profite : les ménages, les actionnaires et l’investissement, ou les clients et la compétitivité.',
  t='mec', b=1038)

c('Quelle limite affecte la répartition des gains de productivité par les salaires ?',
  'Si la consommation supplémentaire porte sur des produits importés, la relance ne profite pas à l’économie nationale.',
  x='L’ouverture de l’économie peut donc annuler l’effet d’entraînement attendu d’une hausse du pouvoir d’achat.',
  t='mec', b=1044)

c('À quelle condition une baisse de prix consécutive à un gain de productivité est-elle rentable ?',
  'Si l’augmentation des quantités vendues compense la baisse de la marge unitaire.',
  x='Face à une demande peu élastique, la baisse des prix détruit au contraire de la valeur.',
  t='mec', b=1056)

c('Qu’est-ce que la croissance intensive ?',
  'Une croissance du PIB reposant principalement sur la productivité globale des facteurs, sans hausse proportionnelle du travail ou du capital.',
  x='Elle vient du progrès technique, de l’innovation, de l’organisation et de la diffusion des connaissances.',
  t='def', b=1076)

c('Qu’est-ce que le productivisme, et quelles professions en subissent le plus les effets ?',
  'Pousser les travailleurs à produire toujours plus dans un temps donné ; les métiers du care y sont particulièrement exposés.',
  x='Infirmiers, aides-soignants et services à la personne : la pression à la rentabilité y réduit le temps relationnel et le sens du travail.',
  t='def', b=1089)

c('Quels effets sur la santé au travail le productivisme peut-il entraîner ?',
  'Troubles musculo-squelettiques, tendinites, pénibilité physique, stress et épuisement professionnel.',
  x='C’est la limite sociale de la croissance intensive : efficace économiquement, coûteuse humainement.',
  t='mec', b=1102)

c('Qu’est-ce que la compétitivité, et quelles formes prend-elle ?',
  'La capacité d’un pays à gagner des parts de marché, exporter et maintenir son niveau de vie ; elle est soit prix, soit hors-prix.',
  x='La compétitivité-prix repose sur le coût, la hors-prix sur la qualité, l’innovation et la technologie.',
  t='def', b=1132)

c('Quel décrochage de productivité le diagnostic de Draghi met-il en évidence ?',
  'Depuis les années 2010, les États-Unis engrangent des gains plus élevés et la Chine progresse vite, tandis que l’Europe ralentit durablement.',
  x='Ce différentiel se traduit mécaniquement par un risque de perte de compétitivité européenne.',
  t='fait', b=1127)

c('Quels trois problèmes Mario Draghi identifie-t-il dans son rapport de 2024 ?',
  'Une demande insuffisante, des structures trop rigides et un déficit d’investissement.',
  x='Marchés fragmentés, complexité réglementaire et retard en recherche et développement se renforcent mutuellement.',
  t='aut', b=1145)

c('Pourquoi Draghi réclame-t-il un véritable marché européen des capitaux ?',
  'Parce que l’Europe a une monnaie unique sans marché des capitaux intégré, ce qui empêche les PME de grandir et de financer de gros investissements.',
  x='Un marché élargi permet des économies d’échelle, donc une productivité accrue.',
  t='aut', b=1167)

c('Quel plan d’investissement le rapport Draghi propose-t-il, et pour quels objectifs ?',
  'Environ 800 milliards d’euros par an, ciblés sur l’innovation, la transition énergétique et les technologies.',
  x='La dimension est keynésienne : relancer la demande tout en modernisant l’appareil productif.',
  t='fait', b=1185)

c('Quel héritage d’Adam Smith le rapport Draghi mobilise-t-il ?',
  'L’idée que la productivité dépend de la division du travail, elle-même limitée par l’étendue du marché.',
  x='Passer d’un marché national à un marché européen intégré élargit les débouchés et encourage la spécialisation.',
  t='aut', b=1192)

c('Pourquoi une innovation ne fait-elle pas immédiatement baisser les prix ?',
  'Parce que le brevet place l’innovateur en monopole temporaire, et qu’il répercute ses coûts de recherche sur le prix de lancement.',
  x='Premiers téléviseurs, premiers téléphones, premières automobiles : le produit nouveau est toujours cher au départ.',
  t='mec', b=1213)

c('Pourquoi les prix d’une innovation finissent-ils par baisser ?',
  'Parce que la production augmente, les unités s’agrandissent et le coût unitaire diminue : ce sont les économies d’échelle.',
  x='La baisse intervient donc après la diffusion massive, et non au moment de l’invention.',
  t='mec', b=1229)

c('Quel double effet le progrès technique exerce-t-il sur les prix ?',
  'À court terme une hausse possible, liée au brevet et au monopole ; à moyen terme une baisse des coûts et des prix.',
  x='Le gain est d’abord capté par l’innovateur, puis diffusé à l’ensemble de la collectivité.',
  t='mec', b=1239)

c('Comment définit-on le prix réel relatif d’un bien, et pourquoi cette mesure ?',
  'Le prix du bien divisé par le salaire horaire : il mesure le temps de travail nécessaire pour l’acheter.',
  x='Indépendante de l’inflation, cette mesure dit l’accessibilité réelle, ce qu’un prix affiché ne dit jamais.',
  t='form', b=1255)

c('Comment le prix réel de la bicyclette a-t-il évolué, selon l’exemple de Thomas Piketty ?',
  'D’environ six mois de salaire à ses débuts, à un mois après la production de masse, à quelques jours aujourd’hui.',
  x='En prix nominal elle coûte plus cher ; en prix réel elle est devenue incomparablement plus accessible.',
  t='aut', b=1262)

c('Pourquoi les ménages ont-ils le sentiment que tout devient plus cher ?',
  'Parce qu’ils raisonnent en prix affichés et non en prix réels rapportés au salaire.',
  x='Certains biens sont en réalité plus accessibles qu’avant : il faut déflater ou raisonner en prix relatifs.',
  t='mec', b=1274)

c('Quel poids le management peut-il avoir dans les écarts de productivité entre entreprises ?',
  'À caractéristiques comparables, jusqu’à 20 % d’écart de productivité.',
  x='Un simple changement de manager peut entraîner une hausse très significative de la performance.',
  t='fait', b=1308)

c('Quels effets le cours attribue-t-il à un management trop vertical ?',
  'Une moindre autonomie des salariés, moins de prise d’initiative et moins d’expérimentation.',
  x='Or l’innovation repose aussi sur l’imagination et la capacité d’initiative de ceux qui exécutent.',
  t='mec', b=1313)

c('Pourquoi la concurrence stimule-t-elle les gains de productivité ?',
  'Elle pousse à innover, élimine les entreprises inefficaces et réalloue les ressources vers les plus productives.',
  x='À l’inverse, effets de réseau, barrières à l’entrée et rentes de monopole relâchent cette pression.',
  t='mec', b=1325)

c('Qu’est-ce qu’un brevet défensif ?',
  'Un brevet déposé non pour exploiter une innovation mais pour bloquer l’entrée de concurrents et verrouiller un marché.',
  x='Il détourne un instrument conçu pour encourager l’innovation en obstacle juridique à celle des autres.',
  t='def', b=1348)

c('Comment les brevets peuvent-ils freiner la diffusion technologique ?',
  'Un produit intégrant de nombreuses technologies brevetées impose d’identifier les détenteurs, de négocier des licences et de payer des frais juridiques.',
  x='Ces coûts de transaction peuvent décourager l’innovation qu’ils étaient censés protéger.',
  t='mec', b=1354)

c('Quelle idée commune Colin Clark et Jean Fourastié défendent-ils ?',
  'La productivité progresse à des rythmes différents selon les secteurs, et ces écarts transforment la structure de l’emploi.',
  x='Clark dans Les conditions du progrès économique (1941), Fourastié dans Le grand espoir du XXᵉ siècle (1949).',
  t='aut', b=1378)

c('Pourquoi l’emploi agricole recule-t-il malgré la hausse de la production ?',
  'Parce que les gains de productivité y sont très élevés alors que la demande alimentaire est peu élastique au revenu.',
  x='On produit autant avec moins de bras, et la main-d’œuvre libérée alimente l’exode rural.',
  t='mec', b=1391)

c('Quelles sont les deux phases de l’emploi industriel selon la loi des trois secteurs ?',
  'Une phase d’industrialisation créatrice d’emplois, puis une phase d’automatisation où l’emploi recule malgré une production élevée.',
  x='Demande dynamique d’abord, robotisation ensuite : c’est le passage de l’industrialisation à la désindustrialisation.',
  t='mec', b=1398)

c('Pourquoi l’emploi tertiaire augmente-t-il mécaniquement ?',
  'Parce que la productivité y est structurellement faible alors que la demande de services croît avec le niveau de vie.',
  x='Le temps relationnel du soin ou de l’éducation est incompressible : un coiffeur ne coupe pas deux têtes à la fois.',
  t='mec', b=1412)

c('Qu’est-ce que la théorie du déversement d’Alfred Sauvy ?',
  'Les gains de productivité d’un secteur libèrent de la main-d’œuvre qui se déverse vers un autre secteur.',
  x='Deux déversements historiques : agriculture vers industrie au XIXᵉ, industrie vers services au XXᵉ.',
  t='aut', b=1425)

c('Que répond Alfred Sauvy dans La Machine et le chômage (1980) à l’idée que les machines détruisent l’emploi ?',
  'Que le progrès technique détruit des emplois dans certains secteurs mais en crée dans d’autres.',
  x='La tertiarisation est ainsi la conséquence logique de gains de productivité inégaux et de la réallocation du travail.',
  t='aut', b=1431)

c('Quelle limite inédite la théorie du déversement rencontre-t-elle aujourd’hui ?',
  'Le tertiaire représente 70 à 75 % de l’emploi et connaît à son tour gains de productivité et automatisation : où la main-d’œuvre se déversera-t-elle ?',
  x='Caisses automatiques, guichets bancaires numérisés, tâches administratives automatisées : le dernier secteur refuge se referme.',
  t='mec', b=1442)

c('En quoi l’intelligence artificielle diffère-t-elle des automatisations précédentes ?',
  'Elle touche des tâches intellectuelles et des emplois qualifiés : juristes, comptables, traducteurs, métiers de la création.',
  x='Frey et Osborne estiment que 47 % des tâches sont automatisables : ce sont des tâches, et non nécessairement des emplois entiers.',
  t='fait', b=1455)

c('Quelles deux réponses théoriques oppose-t-on à la crainte d’une destruction d’emplois par l’IA ?',
  'La recomposition des emplois, avec de nouvelles tâches de conseil et de supervision, et le changement de la nature des compétences demandées.',
  x='Le problème se déplace alors vers la transition : reconversion des actifs et formation des jeunes sur un marché instable.',
  t='mec', b=1465)

c('Par quels deux indicateurs mesure-t-on la désindustrialisation ?',
  'La part de l’industrie dans la valeur ajoutée et la part de l’emploi industriel dans la population active.',
  x='Le diagnostic diffère selon l’indicateur : l’industrie peut produire autant en employant beaucoup moins.',
  t='mec', b=1487)

c('Comment se répartit la population active française entre les trois secteurs ?',
  'Environ 2 à 3 % dans l’agriculture, 19 à 20 % dans l’industrie et la construction, et 77 % dans le tertiaire.',
  x='L’industrie seule pèse environ 18 % : ces ordres de grandeur sont à connaître pour toute copie sur la désindustrialisation.',
  t='fait', b=1514)

c('Quel paradoxe statistique les économistes observent-ils dans les années 1980-1990 ?',
  'La part de l’emploi industriel chute fortement alors que la valeur ajoutée industrielle reste relativement stable.',
  x='Moins de travailleurs industriels mais pas moins de production : d’où est passée la main-d’œuvre ?',
  t='fait', b=1523)

c('Qu’est-ce que l’externalisation, et quel effet d’optique produit-elle ?',
  'Confier à une autre entreprise des activités réalisées en interne ; les salariés concernés basculent statistiquement dans le tertiaire.',
  x='Comptabilité, juridique, nettoyage, informatique : l’emploi industriel recule sans qu’aucune production ne disparaisse.',
  t='def', b=1530)

c('Comment la productivité industrielle se compare-t-elle à la productivité moyenne en France ?',
  'Environ 3,4 % par an dans l’industrie contre à peu près 1,3 % en moyenne.',
  x='Cet écart explique à lui seul une part de la baisse de l’emploi industriel, même lorsque la production augmente.',
  t='fait', b=1554)

c('Quelles sont les trois causes majeures de la désindustrialisation ?',
  'Les gains de productivité industriels, l’externalisation des tâches non productives et la mondialisation avec les délocalisations.',
  x='Seule la troisième correspond à une perte réelle de production sur le territoire ; les deux premières déplacent les comptages.',
  t='mec', b=1552)

c('Quelle différence sépare externaliser et délocaliser ?',
  'Externaliser, c’est confier une activité à une autre entreprise ; délocaliser, c’est déplacer la production à l’étranger.',
  x='On peut externaliser sans délocaliser, délocaliser sans externaliser, ou faire les deux.',
  t='dist', b=1589)

c('Pourquoi la désindustrialisation est-elle plus marquée en France qu’en Allemagne ?',
  'La France a misé sur la compétitivité-prix, l’Allemagne sur la compétitivité hors-prix fondée sur la qualité et l’innovation.',
  x='Avec des salaires élevés et une protection sociale développée, la France peine à rivaliser par les prix : l’incitation à délocaliser est plus forte.',
  t='mec', b=1599)

c('Quelle thèse Pierre Veltz défend-il dans La Société hyper-industrielle (2017) ?',
  'L’industrie n’a pas disparu : elle s’est transformée, intégrée au numérique et renforcée.',
  x='Il conteste ainsi l’idée dominante d’une société devenue post-industrielle, tertiaire et immatérielle.',
  t='aut', b=1616)

c('Pourquoi Pierre Veltz refuse-t-il l’idée d’une économie dématérialisée ?',
  'Parce que le numérique repose sur des câbles sous-marins, des data centers énergivores, des métaux rares et de lourdes infrastructures électriques.',
  x='Environ 98 % des flux mondiaux passent par des câbles sous-marins : la dématérialisation cache une matérialité renforcée.',
  t='aut', b=1629)

c('Qu’entend Pierre Veltz par société hyper-industrielle ?',
  'Plus l’économie paraît immatérielle, plus elle dépend d’infrastructures industrielles lourdes.',
  x='L’industrie structure les flux mondiaux, fournit les équipements du numérique et organise les réseaux logistiques.',
  t='aut', b=1640)

c('Qu’appelle-t-on industrie servicielle, et quels exemples le cours en donne-t-il ?',
  'Des entreprises industrielles qui vendent un usage plutôt qu’un bien : Michelin des kilomètres, Airbus des heures de vol, Renault de la mobilité.',
  x='La valeur ne repose plus sur l’objet mais sur le service associé : maintenance, logiciels, contrats d’usage.',
  t='def', b=1652)

c('En quoi les services sont-ils devenus industriels ?',
  'Les services numériques exigent des usines de données, des chaînes d’approvisionnement complexes et une forte intensité énergétique.',
  x='Un service numérique mobilise autant de capital et d’infrastructures qu’une usine classique.',
  t='mec', b=1665)

c('Quelle critique Veltz adresse-t-il à la typologie en trois secteurs ?',
  'Le tertiaire n’est pas homogène : finance et numérique y ont une forte productivité, santé et éducation une productivité structurellement faible.',
  x='Parler de désindustrialisation devient trompeur quand une part de l’activité industrielle est simplement reclassée en services.',
  t='aut', b=1674)

c('Pourquoi la productivité devient-elle systémique dans la société hyper-industrielle ?',
  'Parce qu’elle dépend des réseaux, des interconnexions mondiales, de l’organisation et des infrastructures numériques, et non d’un secteur isolé.',
  x='Industrie et services sont interdépendants : la performance de l’un suppose celle de l’autre.',
  t='mec', b=1683)

c('Quels chocs ont ramené la réindustrialisation au centre du débat après 2020 ?',
  'La crise sanitaire et ses pénuries, la guerre en Ukraine et la dépendance au gaz, puis les tensions géopolitiques entre États-Unis et Chine.',
  x='Masques, paracétamol et respirateurs ont rendu visible une dépendance industrielle devenue un problème de souveraineté.',
  t='fait', b=1711)

c('Quels sont les trois objectifs officiels de la réindustrialisation ?',
  'Retrouver l’autonomie stratégique, accélérer la transition écologique et améliorer le solde commercial.',
  x='Produire sur le territoire des biens critiques, sous des normes plus strictes, tout en substituant des importations.',
  t='mec', b=1717)

c('Pourquoi l’effet de la réindustrialisation sur le solde commercial n’est-il pas automatique ?',
  'Parce que la fragmentation des chaînes de valeur fait qu’on importe alors des composants au lieu de produits finis.',
  x='Refaire des voitures en France n’évite ni les pièces détachées, ni les semi-conducteurs, ni les métaux importés.',
  t='mec', b=1735)

c('Quelles solutions sont évoquées pour rendre la réindustrialisation européenne compétitive ?',
  'La robotisation, qui réduit le poids du coût du travail, et la stratégie allemande de compétitivité hors-prix par la qualité et la gamme.',
  x='Produire en Europe pose d’abord la question du coût : le produit doit rester vendable face à la concurrence mondiale.',
  t='mec', b=1749)

c('Qu’est-ce que le rapport interdécile, et comment le construit-on ?',
  'Le rapport entre D9 et D1 : on classe la population par revenu croissant, on la divise en dix groupes égaux et l’on compare les seuils extrêmes.',
  x='Avec D1 à 1 200 euros et D9 à 4 800, les 10 % les plus aisés perçoivent quatre fois plus que les 10 % les plus modestes.',
  t='form', b=1761)

c('Quelles limites affectent le rapport interdécile ?',
  'Il ne dit rien des 80 % centraux, ne capte pas les évolutions internes aux déciles, ni l’explosion du sommet de la distribution.',
  x='Il compare deux seuils et ignore donc tout ce qui se passe entre eux et au-delà du neuvième décile.',
  t='mec', b=1798)

c('Pourquoi le rapport interdécile ne capte-t-il pas les inégalités contemporaines ?',
  'Parce qu’elles se concentrent dans le top 1 %, que le neuvième décile ne distingue pas du reste des 10 % les plus aisés.',
  x='L’indicateur peut donc rester stable alors même que les très hauts revenus explosent.',
  t='mec', b=1801)

c('Que compare le coefficient de Palma ?',
  'La part du revenu détenue par les 10 % les plus riches à celle détenue par les 50 % les plus pauvres.',
  x='Proposé en 2011, il mesure une polarisation : non plus pauvres contre riches, mais une élite contre une large base.',
  t='form', b=1815)

c('Comment interprète-t-on un coefficient de Palma de 1,75 ?',
  'Les 10 % les plus riches captent 1,75 fois plus de revenu que la moitié la plus pauvre de la population.',
  x='Par exemple 35 % du revenu national pour les premiers contre 20 % pour les seconds.',
  t='mec', b=1828)

c('Quelle évolution le coefficient de Palma met-il en évidence depuis les années 1980 ?',
  'La part des 10 % les plus riches augmente, celle des 50 % les plus pauvres stagne ou recule, celle des 40 % intermédiaires reste stable.',
  x='C’est exactement la configuration qu’un indicateur centré sur les seuils extrêmes ne permet pas de voir.',
  t='fait', b=1858)

c('Sur quelle construction graphique le coefficient de Gini repose-t-il ?',
  'La courbe de Lorenz, qui porte la population cumulée en abscisse et le revenu cumulé en ordonnée.',
  x='Plus la courbe s’éloigne de la droite d’équirépartition, plus les inégalités sont fortes.',
  t='def', b=1868)

c('Qu’est-ce qui distingue le coefficient de Gini des deux autres indicateurs d’inégalité ?',
  'Il prend en compte l’ensemble de la distribution, au lieu de comparer seulement deux groupes précis.',
  x='Compris entre 0 et 1, il mesure une concentration globale, là où l’interdécile et le Palma mesurent un écart.',
  t='dist', b=1869)

c('Quelles valeurs de coefficient de Gini caractérisent un pays égalitaire et un pays très inégalitaire ?',
  'Environ 0,25 à 0,30 pour un pays égalitaire, 0,45 à 0,60 pour un pays très inégalitaire.',
  x='La France se situe autour de 0,29, soit environ 0,297 en 2023 : des inégalités modérées mais persistantes.',
  t='fait', b=1890)

c('Pourquoi le Gini du patrimoine dépasse-t-il toujours celui du revenu ?',
  'Parce que le patrimoine se transmet, engendre lui-même du revenu et s’accumule dans le temps.',
  x='Les inégalités patrimoniales sont donc structurellement plus fortes que les inégalités de revenu.',
  t='mec', b=1903)

c('Quelles limites le coefficient de Gini présente-t-il ?',
  'Il ne dit pas où se situent les écarts, deux pays peuvent partager le même indice avec des structures opposées, et il reste insensible à l’enrichissement du sommet.',
  x='Un seul chiffre synthétise toute la distribution, au prix d’une perte d’information sur sa forme.',
  t='mec', b=1911)

c('Quelle hypothèse Simon Kuznets formule-t-il en 1955 ?',
  'La relation entre croissance et inégalités suit une courbe en cloche : les inégalités augmentent d’abord, puis diminuent.',
  x='Il l’établit en observant l’évolution des inégalités aux États-Unis entre 1913 et 1948.',
  t='aut', b=1931)

c('Pourquoi les inégalités augmentent-elles dans la première phase de la courbe de Kuznets ?',
  'Le passage d’une économie agricole à une économie industrielle crée de forts écarts de productivité et des salaires industriels plus élevés.',
  x='Les écarts se creusent donc entre secteurs avant de se creuser entre individus.',
  t='aut', b=1940)

c('Qu’est-ce qui ferait baisser les inégalités dans la seconde phase de la courbe de Kuznets ?',
  'La généralisation de l’éducation, la diffusion du progrès technique, la montée de la classe moyenne et surtout le développement de la redistribution.',
  x='L’État corrige alors les inégalités produites par le marché, financé par des recettes fiscales en hausse.',
  t='aut', b=1947)

c('Quelles observations contredisent la phase descendante prévue par Kuznets ?',
  'Depuis les années 1980 : hausse des inégalités de revenus, forte concentration des patrimoines et explosion du top 1 %.',
  x='La baisse des inégalités n’est donc pas mécanique : elle dépend du système fiscal, des institutions et de la protection sociale.',
  t='fait', b=1967)

c('Quel paradoxe central Branko Milanovic met-il en évidence ?',
  'Les inégalités entre pays diminuent tandis que les inégalités à l’intérieur des pays augmentent.',
  x='Convergence entre économies développées et émergentes d’un côté, divergence au sein des sociétés nationales de l’autre.',
  t='aut', b=1981)

c('Comment la courbe de l’éléphant est-elle construite ?',
  'La population mondiale classée par revenu initial en abscisse, le taux de croissance du revenu réel en ordonnée.',
  x='Les revenus sont déflatés et exprimés en parité de pouvoir d’achat, pour neutraliser inflation et taux de change.',
  t='form', b=1990)

c('Qui sont les grands gagnants de la mondialisation selon la courbe de l’éléphant ?',
  'La classe moyenne des pays émergents, surtout en Chine, en Inde et en Asie, avec une croissance de 70 à 80 % de ses revenus.',
  x='C’est ce groupe qui explique la réduction des inégalités entre pays sur la période 1988-2008.',
  t='aut', b=2002)

c('Quelle croissance le top 1 % mondial a-t-il connue entre 1988 et 2008, et d’où vient-il ?',
  'Environ + 60 % de revenu réel ; la moitié de cette élite est américaine.',
  x='Milanovic parle de l’émergence d’une ploutocratie mondiale, qui capte l’essentiel du surplus en valeur absolue.',
  t='fait', b=2008)

c('Qui sont les perdants relatifs de la mondialisation dans la courbe de l’éléphant ?',
  'Les classes moyennes occidentales, autour du 80ᵉ percentile mondial, dont le revenu réel progresse d’environ 0 %.',
  x='Ce décrochage nourrit un sentiment de déclassement, que Milanovic relie à la montée des tensions politiques.',
  t='aut', b=2014)

c('Pourquoi faut-il distinguer gains relatifs et gains absolus dans la lecture de la courbe de l’éléphant ?',
  'En pourcentage, les classes moyennes émergentes progressent le plus ; en valeur, c’est le top 1 % qui capte la plus grande part du surplus mondial.',
  x='Le même graphique raconte donc deux histoires opposées selon l’unité de lecture retenue.',
  t='mec', b=2023)

c('Qu’appelle-t-on rente de citoyenneté chez Milanovic ?',
  'L’avantage durable que procure le seul fait de naître dans un pays riche : revenu plus élevé et meilleur accès aux opportunités.',
  x='La nationalité devient ainsi un facteur central d’inégalité mondiale, devant la position sociale au sein du pays.',
  t='def', b=2028)

c('Quelle différence sépare un revenu d’un patrimoine ?',
  'Le revenu est un flux perçu sur une période ; le patrimoine est un stock de richesses détenues à un instant donné.',
  x='Salaires, revenus du capital et prestations pour le premier ; immobilier, actifs financiers et capital productif pour le second.',
  t='dist', b=2048)

c('Pourquoi les inégalités de patrimoine se reproduisent-elles dans le temps ?',
  'Le patrimoine engendre des revenus — loyers, intérêts, dividendes — qui permettent d’en accumuler davantage, et il se transmet par héritage ou donation.',
  x='La logique est cumulative : la concentration se renforce d’elle-même d’une génération à l’autre.',
  t='mec', b=2070)

c('Quels trois débats structurent les théories de la croissance ?',
  'L’équilibre de long terme est-il la règle ou l’exception, quels sont les facteurs de croissance et la place du progrès technique, et quel rôle pour l’État.',
  x='Les modèles diffèrent par leurs réponses, mais tous se lisent à travers ces trois mêmes questions.',
  t='mec', b=2082)

c('Dans quel contexte Harrod et Domar élaborent-ils leur modèle de croissance ?',
  'Après la crise de 1929, pour contester l’idée néoclassique selon laquelle les marchés sont naturellement à l’équilibre.',
  x='Harrod publie en 1939, Domar en 1947 : tous deux relèvent d’une approche post-keynésienne.',
  t='aut', b=2096)

c('Pourquoi parle-t-on de croissance « sur le fil du rasoir » chez Harrod et Domar ?',
  'Parce que le chemin de croissance équilibrée est extrêmement étroit et relève du hasard : la croissance n’est pas auto-stabilisatrice.',
  x='Elle dépend de variables exogènes et reste instable par nature, contrairement au modèle néoclassique.',
  t='mec', b=2100)

c('Quelle hypothèse sur les facteurs de production distingue Harrod-Domar du modèle néoclassique ?',
  'Les facteurs y sont complémentaires et non substituables : on ne peut pas remplacer le travail par du capital.',
  x='Les coefficients techniques K/Y et L/Y sont stables à court terme, ce qui interdit tout ajustement automatique.',
  t='dist', b=2111)

c('D’où vient la croissance chez Harrod et Domar ?',
  'De la demande, et non de l’offre : les entreprises ne produisent que si elles anticipent de vendre.',
  x='L’investissement dépend des débouchés : la croissance repose donc sur la demande effective, dans la filiation de Keynes.',
  t='mec', b=2126)

c('Quels sont les deux effets de l’investissement chez Harrod et Domar ?',
  'Un effet revenu, par le multiplicateur, et un effet de capacité, par l’accroissement du stock de capital.',
  x='C’est la tension entre ces deux effets qui rend l’équilibre si difficile à atteindre : la demande créée doit absorber la capacité créée.',
  t='mec', b=2133)

c('Que mesure le coefficient de capital, et pourquoi est-il central chez Harrod-Domar ?',
  'La quantité de capital nécessaire pour produire une unité de production ; supposé constant, il interdit tout ajustement.',
  x='Avec un coefficient de 3, il faut trois unités de capital par unité de richesse : on ne peut pas y substituer du travail.',
  t='def', b=2144)

c('Quel effet un coefficient de capital élevé a-t-il sur la croissance ?',
  'Il exige beaucoup d’investissement pour un seul point de croissance, donc un taux d’épargne élevé, et rend l’économie plus rigide.',
  x='Un coefficient faible rend au contraire l’investissement plus efficace et la croissance plus facile à maintenir.',
  t='mec', b=2159)

c('Qu’est-ce que le taux de croissance effectif chez Harrod ?',
  'Le taux réellement observé, qui dépend de la conjoncture, des anticipations et des chocs d’offre comme de demande.',
  x='Empirique et fluctuant, il ne possède aucun mécanisme interne garantissant sa stabilité.',
  t='def', b=2181)

c('Qu’est-ce que le taux de croissance garanti, et de quoi dépend-il ?',
  'Le taux qui assure l’équilibre entre épargne et investissement ; il vaut le taux d’épargne divisé par le coefficient de capital.',
  x='Il dépend donc du comportement d’épargne et de la structure productive, mais pas du tout de la démographie.',
  t='form', b=2197)

c('Qu’est-ce que le taux de croissance naturel chez Harrod ?',
  'Le taux compatible avec le plein emploi, déterminé par la croissance de la population active et la participation au marché du travail.',
  x='Il ne dépend ni de l’épargne ni de l’investissement : c’est le rythme auquel la main-d’œuvre disponible augmente.',
  t='def', b=2214)

c('Pourquoi l’équilibre est-il si improbable dans le modèle de Harrod ?',
  'Parce que les trois taux — effectif, garanti et naturel — sont déterminés par des mécanismes totalement indépendants.',
  x='Conjoncture, épargne et structure productive, démographie : rien ne les fait converger, d’où le fil du rasoir.',
  t='mec', b=2229)

c('Quel cercle vicieux un taux d’épargne trop élevé déclenche-t-il chez Harrod-Domar ?',
  'La consommation recule, la demande devient insuffisante, les entreprises licencient, les revenus baissent et la consommation recule encore.',
  x='C’est un blocage keynésien par insuffisance de demande effective, sans aucune correction spontanée.',
  t='mec', b=2258)

c('Que se passe-t-il chez Harrod-Domar si le taux d’épargne est trop faible ?',
  'L’investissement est insuffisant, l’accumulation ralentit et la croissance potentielle est limitée : c’est une contrainte d’offre.',
  x='Le modèle montre donc que le problème n’est ni le trop ni le trop peu, mais l’absence de mécanisme d’ajustement.',
  t='mec', b=2271)

c('Quel est le statut du progrès technique chez Harrod et Domar ?',
  'Il est exogène : il ne résulte d’aucun mécanisme économique interne et ne supprime pas l’instabilité.',
  x='Il peut modifier le taux naturel, mais ne crée aucun ajustement automatique entre les trois taux.',
  t='mec', b=2301)

c('Pourquoi l’intervention de l’État est-elle justifiée chez Harrod et Domar ?',
  'Parce que l’équilibre n’est pas automatique, les marchés ne sont pas coordonnés et la demande peut rester durablement insuffisante.',
  x='L’État stimule la demande, soutient l’investissement et stabilise les anticipations : il répond à une instabilité structurelle.',
  t='mec', b=2307)

c('Dans quel article et en quelle année Solow publie-t-il son modèle de croissance ?',
  'A Contribution to the Theory of Economic Growth, en 1956.',
  x='Il cherche, contre le pessimisme de Harrod-Domar, une théorie où la croissance de long terme est stable et équilibrée.',
  t='aut', b=2324)

c('Quelles hypothèses Solow modifie-t-il par rapport à Harrod-Domar ?',
  'Il rend les facteurs substituables, les prix et salaires flexibles, et pose des rendements d’échelle constants avec une productivité marginale du capital décroissante.',
  x='Ce sont ces changements qui rendent possible un mécanisme d’ajustement, donc un équilibre stable.',
  t='dist', b=2333)

c('Pourquoi la fonction de production par tête est-elle concave chez Solow ?',
  'Parce que la productivité marginale du capital est décroissante : chaque unité de capital par travailleur rapporte moins que la précédente.',
  x='C’est cette concavité qui fait buter l’accumulation sur une limite, et produit l’état stationnaire.',
  t='mec', b=2346)

c('Qu’est-ce que l’état stationnaire chez Solow ?',
  'Le niveau de capital par tête où l’investissement sert exactement à compenser l’usure du capital.',
  x='Le capital et la production par tête y deviennent constants : la croissance du niveau de vie s’éteint si rien ne change.',
  t='def', b=2363)

c('Par quel mécanisme l’économie converge-t-elle vers l’état stationnaire chez Solow ?',
  'Si l’investissement est inférieur à l’amortissement, le capital par tête diminue et ramène l’économie vers son niveau d’équilibre.',
  x='Le mouvement joue dans les deux sens : la convergence est automatique, à l’inverse du fil du rasoir de Harrod.',
  t='mec', b=2365)

c('Qu’est-ce que la convergence conditionnelle impliquée par le modèle de Solow ?',
  'Les pays à faible capital par tête ont un rendement du capital plus élevé et rattrapent donc plus vite les pays avancés.',
  x='Elle est dite conditionnelle car elle suppose des paramètres comparables : taux d’épargne, démographie, technologie.',
  t='def', b=2379)

c('Quelle place le modèle de Solow laisse-t-il à l’État ?',
  'Aucune place structurelle : la croissance de long terme ne dépend pas de lui, les mécanismes de marché assurant la coordination.',
  x='C’est l’opposé exact de la conclusion de Harrod-Domar, tirée d’hypothèses différentes sur l’ajustement.',
  t='dist', b=2383)

c('Quelle est la limite centrale du modèle de Solow ?',
  'Le moteur ultime de la croissance par tête est le progrès technique, mais il reste exogène : le modèle ne dit pas comment le produire.',
  x='C’est précisément cette lacune que les théories de la croissance endogène entreprendront de combler.',
  t='mec', b=2390)

c('Quel levier Solow identifie-t-il pour repousser l’état stationnaire ?',
  'Une hausse du taux d’épargne, qui permet d’atteindre un niveau de capital par tête plus élevé.',
  x='Elle repousse l’échéance sans la supprimer : seul le progrès technique soutient durablement la croissance par tête.',
  t='aut', b=2395)

c('Qui a popularisé la notion de capital humain, et que désigne-t-elle ?',
  'Gary Becker dans les années 1960 : le stock de caractéristiques physiques et intellectuelles incorporées aux individus et valorisables économiquement.',
  x='Ce n’est plus la quantité de travail qui compte mais sa qualité, à travers la formation et la santé.',
  t='aut', b=2406)

c('En quoi Robert Lucas rompt-il avec Solow en 1988 ?',
  'Il fait venir la croissance de l’accumulation du capital humain, et non d’un progrès technique extérieur au modèle.',
  x='La productivité marginale de la formation y est constante voire croissante : les rendements décroissants ne s’imposent plus.',
  t='aut', b=2403)

c('Quel mécanisme rend la croissance cumulative chez Lucas ?',
  'Les externalités positives : le capital humain d’un individu accroît aussi la productivité de ceux qui l’entourent.',
  x='Le rendement social de la formation dépasse donc son rendement privé, ce qui entretient la dynamique.',
  t='aut', b=2435)

c('Pourquoi Lucas justifie-t-il une intervention structurelle de l’État ?',
  'Parce que les agents ne tiennent pas compte des bénéfices collectifs de leur formation : le marché sous-investit dans l’éducation.',
  x='Ce n’est pas une politique conjoncturelle keynésienne mais une politique de long terme fondée sur les externalités.',
  t='aut', b=2454)

c('Quelles limites le modèle de Lucas présente-t-il ?',
  'L’hypothèse forte de rendements non décroissants, la difficulté de mesurer le capital humain et le risque d’inégalités si l’accès à l’éducation est inégal.',
  x='Le modèle reste par ailleurs abstrait au regard des réalités sectorielles.',
  t='mec', b=2465)

c('Qu’est-ce que le capital public chez Robert Barro ?',
  'L’ensemble des dépenses publiques productives qui améliorent la productivité du secteur privé.',
  x='Infrastructures, éducation et recherche-développement : Barro les intègre explicitement dans la fonction de production.',
  t='def', b=2477)

c('Pourquoi Barro, économiste libéral, réhabilite-t-il le rôle de l’État ?',
  'Parce que le capital public produit des externalités dont le rendement social dépasse le rendement privé.',
  x='Il ne défend pas la relance keynésienne mais une intervention structurelle orientée vers l’investissement productif.',
  t='aut', b=2500)

c('Quelle condition d’efficacité Barro pose-t-il à la dépense publique ?',
  'Il existe un niveau optimal de capital public : au-delà, la dépense cesse d’être productive.',
  x='La croissance dépend donc de la qualité des dépenses et de leur orientation, non de leur seul volume.',
  t='mec', b=2509)

c('Qu’est-ce qui distingue le moteur de croissance de Barro de ceux de Lucas et Romer ?',
  'Chez Barro c’est le capital public productif, chez Lucas le capital humain individuel, chez Romer la recherche privée.',
  x='Tous trois partagent la même structure : un capital spécifique à rendements non décroissants rend la croissance auto-entretenue.',
  t='dist', b=2520)

c('Quelle propriété de la connaissance fonde le modèle de Romer ?',
  'Sa non-rivalité : elle ne s’use pas, peut être utilisée simultanément par plusieurs agents et se diffuse.',
  x='C’est cette propriété qui fait échapper les idées à la logique des rendements décroissants du capital physique.',
  t='aut', b=2530)

c('Pourquoi les idées engendrent-elles des rendements croissants chez Romer ?',
  'Parce que plus il existe de connaissances accumulées, plus il devient facile d’innover.',
  x='La logique est cumulative : la croissance peut s’auto-entretenir sans converger vers un état stationnaire.',
  t='aut', b=2545)

c('Qu’est-ce qu’un spillover chez Romer ?',
  'L’externalité positive d’une innovation, qui profite à l’innovateur mais aussi à toute l’économie.',
  x='D’où l’écart entre rendement privé et rendement social, qui justifie un soutien public à la recherche.',
  t='def', b=2550)

c('Quelles interventions Romer assigne-t-il à l’État ?',
  'Financer la recherche publique, subventionner la R&D, protéger la propriété intellectuelle et soutenir l’enseignement supérieur.',
  x='Les entreprises ne captant pas tous les bénéfices sociaux de l’innovation, le marché seul sous-investit.',
  t='aut', b=2565)

c('Quelles limites le modèle de Romer présente-t-il ?',
  'La difficulté de mesurer la connaissance, l’hypothèse forte de rendements croissants et le risque de concentration des rentes d’innovation.',
  x='Il suppose en outre un cadre institutionnel solide en matière de brevets et de concurrence.',
  t='mec', b=2587)

c('Dans quel ouvrage Philippe Aghion présente-t-il son modèle de destruction créatrice, et avec qui ?',
  'Le Pouvoir de la destruction créatrice (2020), avec Céline Antonin et Simon Bunel.',
  x='Il y reprend le modèle de croissance endogène qu’il avait élaboré avec Peter Howitt dans les années 1980.',
  t='aut', b=2594)

c('Quels sont les deux déterminants de l’innovation chez Aghion ?',
  'L’intensité de la recherche et développement et le régime de concurrence.',
  x='Toutes les dépenses de R&D n’aboutissent pas, et sans concurrence l’innovation ne décolle pas même avec de la recherche.',
  t='aut', b=2600)

c('Pourquoi la concurrence est-elle à la fois stimulante et menacée chez Aghion ?',
  'Elle pousse les firmes à innover pour rester leaders, mais les leaders cherchent précisément à l’étouffer par des barrières à l’entrée.',
  x='D’où la nécessité d’un État garant de la concurrence, qui lève les obstacles à la destruction créatrice.',
  t='mec', b=2606)

c('Quels rôles Aghion assigne-t-il à l’État dans la croissance ?',
  'Investisseur dans l’innovation, protecteur des droits de propriété, garant de la concurrence, amortisseur des effets négatifs et orienteur des nouvelles directions.',
  x='Ce dernier rôle répond à la dépendance au sentier : l’automobile thermique ne bascule pas spontanément vers l’électrique.',
  t='aut', b=2610)

c('Qu’est-ce que la frontière technologique, et quelle conséquence en tire Aghion ?',
  'Le niveau de technologie le plus avancé à un moment donné ; la politique industrielle doit distinguer les entreprises selon leur distance à cette frontière.',
  x='Près de la frontière, il faut libéraliser et miser sur l’enseignement supérieur ; loin d’elle, les politiques efficaces sont différentes.',
  t='aut', b=2626)

c('Quelle thèse Banerjee et Duflo opposent-ils à l’analyse standard du sous-développement ?',
  'Le problème n’est pas le manque de capital mais sa mauvaise allocation : capital, talents et entrepreneurs existent, mais sont mal employés.',
  x='On peut accumuler du capital sans développer l’économie si les entreprises productives n’obtiennent pas les financements.',
  t='aut', b=2662)

c('Comment le capital humain est-il mal alloué selon Banerjee et Duflo ?',
  'Les talents ne sont pas repérés, la formation est inadéquate et les entrepreneurs sont choisis selon le statut familial plutôt que la compétence.',
  x='Le problème n’est pas l’héritage en soi, mais l’absence de sélection par la compétence : c’est un gaspillage économique.',
  t='aut', b=2679)

c('Qu’est-ce qu’une croissance inclusive selon Banerjee et Duflo ?',
  'Une croissance qui profite au plus grand nombre, n’est pas captée par une élite, réduit les inégalités et emploie mieux les talents disponibles.',
  x='Une économie peut croître sans réellement se développer : la distinction est au cœur de leur démonstration.',
  t='def', b=2722)

c('Quel tournant institutionnel de 1688 North met-il en avant pour expliquer la Révolution industrielle anglaise ?',
  'La limitation du pouvoir royal au profit du Parlement, qui installe l’état de droit et la stabilité institutionnelle.',
  x='S’ensuivent la protection des droits de propriété, l’essor des brevets, la confiance des investisseurs et du crédit.',
  t='aut', b=2771)

c('Quel chiffre illustre la trajectoire industrielle anglaise entre 1750 et 1880 ?',
  'La part britannique dans la production industrielle mondiale passe de 2 % à 23 %.',
  x='Pour North, l’explication n’est ni géographique ni liée au charbon : elle est institutionnelle.',
  t='fait', b=2792)

c('Qu’est-ce qu’une institution inclusive selon Acemoglu et Robinson ?',
  'Une institution qui protège les droits de propriété, garantit l’état de droit, le pluralisme politique, les contre-pouvoirs et la concurrence ouverte.',
  x='Elle encourage l’investissement, l’innovation et la destruction créatrice, donc une croissance durable.',
  t='def', b=2798)

c('Qu’est-ce qu’une institution extractive selon Acemoglu et Robinson ?',
  'Une institution fondée sur la concentration du pouvoir, la captation des richesses par une élite, l’insécurité juridique et le blocage de la concurrence.',
  x='Elle conduit au sous-investissement et à la protection des rentes, donc à une croissance qui s’épuise.',
  t='def', b=2811)

c('Quelle objection le cas chinois oppose-t-il à la typologie d’Acemoglu et Robinson ?',
  'La Chine combine des institutions que la typologie rangerait parmi les extractives avec une croissance forte et durable.',
  x='Leur réponse : une telle croissance reste possible à court et moyen terme, mais instable à long terme.',
  t='mec', b=2836)

c('Pourquoi la relation entre institutions et croissance est-elle circulaire ?',
  'Les institutions favorisent la croissance, mais la croissance permet à son tour de créer de nouvelles institutions.',
  x='Cette circularité rend difficile d’établir le sens de la causalité dans les comparaisons entre pays.',
  t='mec', b=2848)

c('Qu’est-ce que le capital, au sens large retenu pour penser la soutenabilité ?',
  'Un stock d’actifs mobilisables dans la production et capables d’engendrer des revenus futurs.',
  x='Ce n’est donc pas simplement une richesse, mais une richesse utile à la production.',
  t='def', b=2887)

c('Que recouvre le capital naturel ?',
  'Les ressources énergétiques, minerais, forêts, eau, terres agricoles, la biodiversité et les écosystèmes.',
  x='C’est l’ensemble des ressources et services fournis par la nature, intégré au raisonnement sur la soutenabilité.',
  t='def', b=2910)

c('Que recouvre le capital technologique ?',
  'Les brevets, les innovations, les connaissances scientifiques, les procédés de production et les résultats de la R&D.',
  x='C’est le stock de connaissances mobilisable pour produire plus efficacement.',
  t='def', b=2922)

c('Que recouvre le capital social, et à quoi sert-il ?',
  'Les réseaux, la réputation, les relations et la confiance ; il facilite la coordination, l’accès à l’information et au financement.',
  x='Il n’apparaît dans aucun bilan comptable mais conditionne fortement l’activité entrepreneuriale.',
  t='def', b=2932)

c('À quelle condition une compétence constitue-t-elle du capital humain ?',
  'Seulement si elle est valorisable économiquement.',
  x='Le capital humain n’est donc pas l’ensemble des savoirs d’un individu, mais la part productive de ses capacités.',
  t='mec', b=2907)

c('Quelles sont les six formes de capital dont dépend la croissance dans une lecture élargie de Solow ?',
  'Capital physique, humain, naturel, technologique, social et institutionnel.',
  x='La croissance n’est donc pas une simple accumulation de machines mais repose sur des ressources complémentaires.',
  t='mec', b=2952)

c('Qu’affirme la thèse de la soutenabilité faible ?',
  'Les différentes formes de capital sont globalement substituables : la baisse du capital naturel peut être compensée par du capital technologique.',
  x='Le progrès technique permettrait de réduire l’intensité énergétique, de trouver des substituts et de dépolluer.',
  t='def', b=2968)

c('Qu’affirme la thèse de la soutenabilité forte ?',
  'Le capital naturel n’est pas substituable : certaines ressources et certains équilibres sont irremplaçables et parfois détruits de façon irréversible.',
  x='On ne remplace ni une espèce disparue, ni un climat déréglé, ni une forêt primaire, ni un stock minier épuisé.',
  t='def', b=2992)

c('Quelles conséquences pratiques la soutenabilité forte entraîne-t-elle ?',
  'Limiter l’extraction, réduire la consommation matérielle, protéger les écosystèmes et transformer les modes de production et de consommation.',
  x='Le progrès technique n’y suffit pas seul : certaines versions radicales de cette approche défendent la décroissance.',
  t='mec', b=3005)

c('Qu’énonce la courbe environnementale de Kuznets ?',
  'La croissance dégraderait d’abord l’environnement, puis créerait à terme les conditions de sa protection.',
  x='C’est la transposition écologique du U inversé que Kuznets avait proposé pour les inégalités.',
  t='aut', b=3028)

c('À quels auteurs et à quelle date doit-on la transposition écologique de la courbe de Kuznets ?',
  'À Grossman et Krueger, dans le Quarterly Journal of Economics en 1995.',
  x='Ils appliquent la logique du U inversé à certains indicateurs de pollution, ce qui en fait un argument de la soutenabilité faible.',
  t='aut', b=3039)

c('Pour quelles pollutions la courbe environnementale de Kuznets fonctionne-t-elle, et pour lesquelles échoue-t-elle ?',
  'Elle vaut parfois pour des pollutions locales comme le dioxyde de soufre, mais pas pour le CO₂, les gaz à effet de serre, les déchets ou la biodiversité.',
  x='Or ce sont précisément les pollutions globales qui sont aujourd’hui les plus décisives.',
  t='mec', b=3060)

c('Quel biais statistique affaiblit la courbe environnementale de Kuznets ?',
  'Un pays riche peut sembler moins polluer chez lui tout en important des biens produits ailleurs et en délocalisant les activités polluantes.',
  x='La baisse de la pollution nationale ne signifie donc pas la baisse de l’empreinte écologique réelle.',
  t='mec', b=3073)

c('Pourquoi la temporalité écologique interdit-elle la logique du « polluons d’abord, réparons plus tard » ?',
  'Parce que certaines destructions sont irréversibles, les ressources épuisables, et le climat fonctionne par seuils et effets cumulatifs.',
  x='Le temps écologique n’est pas le temps économique : le rattrapage tardif y est souvent impossible.',
  t='mec', b=3084)

c('Sur quelle logique repose l’économie linéaire ?',
  'Sur l’abondance supposée des ressources et l’acceptation implicite des déchets.',
  x='Très consommatrice de matières et génératrice de rebuts, elle n’est pas soutenable à long terme.',
  t='def', b=3103)

c('Que cherche à faire l’économie circulaire ?',
  'Boucler les cycles de production : réduire les déchets, réutiliser, recycler, allonger la durée de vie et limiter l’extraction.',
  x='On passe d’une logique de flux jetables à une logique de boucles, donc d’une croissance matérielle à une croissance plus qualitative.',
  t='def', b=3111)

c('Pourquoi l’économie circulaire n’est-elle pas une solution miracle ?',
  'Le recyclage a un coût, tous les matériaux ne sont pas recyclables à l’infini, des pertes de matière subsistent et recycler demande de l’énergie.',
  x='Elle réduit certaines pressions sans supprimer les contraintes physiques fondamentales.',
  t='mec', b=3131)

c('Quelle différence sépare efficacité et sobriété énergétiques ?',
  'L’efficacité produit la même chose avec moins d’énergie ; la sobriété réduit la consommation en modifiant les usages eux-mêmes.',
  x='Logique technologique d’un côté, logique comportementale, sociale et politique de l’autre.',
  t='dist', b=3144)

c('Qu’est-ce que l’effet rebond ?',
  'Les gains d’efficacité énergétique sont partiellement, voire totalement, annulés par une hausse des usages.',
  x='L’efficacité ne garantit donc pas une baisse absolue des consommations : c’est l’argument central en faveur de la sobriété.',
  t='def', b=3186)

c('Quelle est la logique générale du Pacte vert européen annoncé en 2019 ?',
  'Non pas arrêter la croissance mais transformer la production pour continuer à croître autrement.',
  x='Il s’inscrit donc dans la croissance verte : la transition y est présentée comme compatible avec l’investissement et l’emploi.',
  t='fait', b=3216)

c('Quels sont les deux objectifs climatiques chiffrés du Green Deal européen ?',
  'Réduire de 55 % les émissions de gaz à effet de serre d’ici 2030 par rapport à 1990, et atteindre la neutralité carbone en 2050.',
  x='La neutralité n’est pas l’absence d’émissions : les émissions résiduelles doivent être compensées par des capacités d’absorption.',
  t='fait', b=3242)

c('Comment le Green Deal présente-t-il l’effet de la transition sur l’emploi ?',
  'Elle ne détruit pas l’emploi en net mais le déplace vers la rénovation thermique, les renouvelables, les infrastructures vertes et la mobilité propre.',
  x='Reste la question centrale de la reconversion : que deviennent les salariés formés pour la voiture thermique ?',
  t='mec', b=3331)

c('Quel plan européen finance la transition écologique, et pour quel montant ?',
  'Next Generation EU, mis en place en 2020, doté de 750 milliards d’euros.',
  x='Il finance aussi la transformation numérique et la cohésion économique et sociale : la transition est une politique d’investissement.',
  t='fait', b=3357)

c('Qu’impose la CSRD aux entreprises européennes ?',
  'Publier des informations vérifiables sur la durabilité de leur système productif, leurs impacts environnementaux et leurs pratiques sociales.',
  x='Son entrée en vigueur a été reportée de deux ans et son périmètre réduit aux très grandes entreprises : un recul concret.',
  t='def', b=3380)

c('Qu’ajoute le devoir de vigilance par rapport à la CSRD ?',
  'Il fait passer d’une logique d’information à une logique de responsabilité : l’entreprise répond des atteintes commises dans toute sa chaîne de valeur.',
  x='Filiales, sous-traitants et fournisseurs sont inclus : il s’agit d’empêcher l’externalisation des coûts sociaux et environnementaux.',
  t='def', b=3424)

c('Quel argument est invoqué pour justifier les reculs sur la CSRD et le devoir de vigilance ?',
  'La perte de compétitivité, les entreprises américaines n’étant pas soumises aux mêmes contraintes.',
  x='L’écologie devient conflictuelle dès qu’elle cesse d’être un discours pour devenir une contrainte juridique.',
  t='mec', b=3444)

c('Quelle critique Jean-Baptiste Fressoz adresse-t-il au récit de la transition énergétique ?',
  'Les énergies ne se substituent pas les unes aux autres : elles s’additionnent.',
  x='L’histoire réelle est un empilement — le charbon n’a jamais disparu — et non la succession de substitutions que raconte le récit habituel.',
  t='aut', b=3479)

c('Comment Fressoz illustre-t-il le cumul des énergies plutôt que leur substitution ?',
  'L’essor du charbon mobilise encore du bois pour les galeries et les infrastructures minières ; le pétrole se développe dans un monde déjà structuré par le charbon.',
  x='Une énergie nouvelle s’appuie sur les anciennes au lieu de les effacer : les systèmes sont emboîtés dans le temps.',
  t='aut', b=3491)

c('Pourquoi les renouvelables restent-elles, selon Fressoz, enchâssées dans un monde fossile ?',
  'Parce qu’elles exigent extraction minière, acier, béton, transport mondial et chaînes industrielles énergivores.',
  x='Présentées comme la sortie des fossiles, elles en dépendent encore matériellement pour exister.',
  t='aut', b=3510)

c('Quelle portée théorique la thèse de Fressoz a-t-elle au-delà de l’histoire de l’énergie ?',
  'Elle affaiblit le récit de la croissance verte : innover n’entraîne pas automatiquement la disparition des anciens systèmes énergétiques.',
  x='Elle contredit donc l’hypothèse de substituabilité sur laquelle repose la soutenabilité faible.',
  t='aut', b=3524)

c('Quelle critique François Jarrige adresse-t-il à la voiture électrique ?',
  'Elle réduit certaines émissions directes mais déplace les coûts écologiques dans l’espace et dans la chaîne de valeur.',
  x='On ne supprime pas la pollution : on en change la nature et le lieu, notamment vers l’extraction des métaux critiques.',
  t='aut', b=3551)

c('Que prévoit l’échéance européenne de 2035 pour l’automobile ?',
  'La fin de la commercialisation de véhicules thermiques neufs, sans interdire la circulation de ceux déjà en service.',
  x='La distinction est importante : le parc existant continuera de rouler bien au-delà de cette date.',
  t='fait', b=3552)
