# -*- coding: utf-8 -*-
"""Première année — chapitre 3. Les grands courants de l'analyse économique."""

from fc_base import lot, c

L = lot(3)

c('Qu’oppose-t-on en économie quand on parle d’orthodoxes et d’hétérodoxes ?',
  'Les orthodoxes sont issus du courant classique et forment le courant dominant ; les hétérodoxes regroupent les critiques et les approches alternatives.',
  x='La frontière n’est pas figée : un courant hétérodoxe peut être absorbé par la théorie standard et devenir dominant à son tour.',
  t='dist', b=4)

c('Quels sont les cinq grands courants de la pensée économique retenus par le cours ?',
  'Le classique, le marxiste, le néoclassique, l’institutionnaliste et le keynésien.',
  x='Ils se subdivisent au XXᵉ siècle en une vingtaine de courants, mais tous se rattachent à ces cinq matrices.',
  t='mec', b=9)

c('D’où vient la richesse d’une nation selon les mercantilistes ?',
  'Du commerce, qui permet d’accumuler de la monnaie métallique.',
  x='La richesse est donc un stock de métaux précieux, et non un flux de production : d’où leur obsession de l’excédent commercial.',
  t='mec', b=15)

c('Quelle formule Jean Bodin emploie-t-il en 1576 pour exprimer le populationnisme mercantiliste ?',
  '« Il n’est richesse ni force que d’hommes », dans La République.',
  x='Plus un pays est peuplé, plus il est puissant : la population est vue comme une ressource, non comme une charge.',
  t='aut', b=17)

c('Quelle politique commerciale les mercantilistes préconisent-ils ?',
  'L’intervention de l’État par les droits de douane, c’est-à-dire le protectionnisme.',
  x='Puisque la richesse est un stock de métaux, tout import qui fait sortir du métal appauvrit la nation.',
  t='mec', b=18)

c('Quelle politique industrielle Colbert met-il en œuvre sous Louis XIV ?',
  'Il crée des manufactures auxquelles il accorde un monopole de dix ans, protégées et financées par le roi.',
  x='Saint-Gobain pour le verre, Sèvres pour la porcelaine : l’État supplée l’initiative privée là où elle manque.',
  t='fait', b=20)

c('Quelle double politique douanière Colbert conduit-il ?',
  'Il supprime les droits de douane entre les villes du royaume et pratique un protectionnisme sélectif aux frontières.',
  x='L’objectif est d’exporter au maximum pour attirer les capitaux : unifier le marché intérieur sert la conquête extérieure.',
  t='mec', b=21)

c('Quelles critiques adresse-t-on à la politique de Colbert ?',
  'Avoir négligé l’agriculture, au point d’exposer la population à la faim, et avoir échoué à rendre prospère la Compagnie des Indes orientales.',
  x='Les Anglais avec l’East India Company et les Hollandais avec la VOC réussissent là où la compagnie française échoue.',
  t='mec', b=24)

c('Quelle thèse Mandeville défend-il dans La Fable des abeilles ?',
  '« Private vices, public benefits » : la poursuite des intérêts égoïstes produit le bien collectif.',
  x='C’est la défense de l’intérêt personnel qui met l’activité économique en mouvement, et la prospérité réside dans la consommation.',
  t='aut', b=26)

c('Pourquoi la thèse de Mandeville heurte-t-elle les autres économistes de son temps ?',
  'Parce qu’elle fait de la consommation la source de la prospérité, là où ils voient l’épargne comme la source de l’enrichissement.',
  x='La demande vient d’abord des plus riches, dont les dépenses profitent ensuite à toute la population.',
  t='mec', b=29)

c('Qu’est-ce qui sépare les mercantilistes des physiocrates sur l’origine de la richesse ?',
  'Pour les premiers elle est un stock de métaux ; pour les seconds elle vient de la terre.',
  x='Le déplacement est décisif : on passe d’une richesse accumulée à une richesse produite chaque année.',
  t='dist', b=33)

c('Quel livre marque la fin de la domination physiocrate, et en quelle année ?',
  'Recherches sur la nature et les causes de la richesse des nations, d’Adam Smith, en 1776.',
  x='Le même ouvrage clôt aussi la période mercantiliste : 1776 fait figure de bascule dans l’histoire de la pensée.',
  t='fait', b=12)

c('Qu’est-ce que l’ordre naturel chez François Quesnay ?',
  'L’idée que l’économie obéit à des lois fixes : respectées, elles font prospérer la société ; entravées, elles l’appauvrissent.',
  x='C’est cet ordre qui justifie la non-intervention : l’État ne peut qu’abîmer ce qu’il prétend corriger.',
  t='aut', b=39)

c('Pourquoi l’agriculture est-elle, pour Quesnay, la seule source véritable de richesse ?',
  'Parce qu’elle seule bénéficie du don gratuit de la nature : la terre rend plus qu’on ne lui a donné.',
  x='Médecin de Louis XV et fils de laboureur devenu propriétaire, il part de l’observation d’un surplus agricole réel.',
  t='aut', b=40)

c('Quelles sont les trois classes sociales distinguées par Quesnay ?',
  'La classe productive, la classe stérile et la classe des propriétaires fonciers.',
  x='Le classement est fonctionnel et non juridique : il dit ce que chaque groupe fait du produit net, non son rang social.',
  t='mec', b=43)

c('Pourquoi Quesnay qualifie-t-il de stérile la classe des artisans et des commerçants ?',
  'Parce qu’ils transforment et échangent sans créer de surplus nouveau : ils vivent de la richesse créée par l’agriculture.',
  x='Le jugement n’est pas moral mais comptable : leur activité restitue une valeur sans l’augmenter.',
  t='aut', b=49)

c('Comment Quesnay définit-il le produit net ?',
  'La valeur annuelle de la production moins les dépenses en capital.',
  x='La notion correspond à ce que la comptabilité nationale appelle aujourd’hui la valeur ajoutée.',
  t='form', b=61)

c('Quels sont les trois types d’avances distingués par Quesnay ?',
  'Les avances annuelles, les avances foncières et les avances primitives.',
  x='Semences et engrais pour les premières, investissements des propriétaires pour les deuxièmes, bétail et matériel durable pour les troisièmes.',
  t='mec', b=57)

c('Qu’est-ce que le Tableau économique de Quesnay, et de quand date-t-il ?',
  'Le premier schéma de circulation des richesses de l’histoire économique, publié en 1758 et révisé en 1766.',
  x='Il montre comment le produit net agricole circule entre les trois classes et permet de reconstituer les avances chaque année.',
  t='aut', b=64)

c('Pourquoi la politique physiocrate est-elle non interventionniste en matière agricole ?',
  'Parce que le revenu des agriculteurs dépend du prix du blé : bloquer les prix ou l’exportation réduit les avances, donc le produit net.',
  x='L’effondrement est en chaîne : moins d’avances, moins de surplus, et c’est tout le circuit qui se grippe.',
  t='mec', b=83)

c('Quelle formule Vincent de Gournay donne-t-il à la doctrine libérale physiocrate ?',
  '« Laissez faire les hommes, laissez passer les marchandises. »',
  x='Elle exprime que l’ordre naturel exige la liberté : la première partie vise la production, la seconde le commerce.',
  t='aut', b=91)

c('Quelle limite Adam Smith oppose-t-il dès 1776 à la conception physiocrate de la richesse ?',
  'Que toute production créant de la valeur ajoutée est productive, y compris la manufacture.',
  x='La richesse cesse d’être liée à un secteur pour devenir liée au travail, quel que soit l’endroit où il s’exerce.',
  t='mec', b=102)

c('Quelle place le travail humain occupe-t-il chez Quesnay, et pourquoi est-ce une limite ?',
  'Il n’y est qu’un auxiliaire de la terre, alors que Smith et Ricardo en feront la source même de l’enrichissement.',
  x='Cette sous-estimation explique que la physiocratie ne puisse pas penser l’industrialisation qui s’annonce.',
  t='mec', b=104)

c('Qui forme la classe productive chez Quesnay, et qu’a-t-elle de particulier ?',
  'Les agriculteurs fermiers : seuls à créer un produit net, c’est-à-dire un surplus après déduction des dépenses de production.',
  x='Tout le circuit physiocratique part de ce surplus : sans lui, les deux autres classes n’auraient rien à se partager.',
  t='aut', b=46)

c('De quoi vivent les propriétaires fonciers dans le schéma de Quesnay ?',
  'Des rentes, impôts et fermages financés par le produit net agricole.',
  x='Nobles, Église et État y sont rangés ensemble : ce qui les définit est de percevoir, non de produire.',
  t='aut', b=52)

c('Pourquoi dit-on que le modèle de Quesnay décrit une économie figée ?',
  'Parce que le circuit s’y reproduit à l’identique d’une année sur l’autre : c’est un modèle de reproduction, non de croissance.',
  x='Cette limite le rend incapable d’expliquer l’industrialisation et la croissance moderne qui s’amorcent alors.',
  t='mec', b=111)

c('Quels aléas l’agriculture idéalisée de Quesnay ignore-t-elle ?',
  'Les variations climatiques, les crises agricoles et les rendements décroissants.',
  x='C’est précisément sur ce dernier point que Ricardo prolongera puis retournera l’analyse physiocratique.',
  t='mec', b=116)

c('Dans quel ouvrage et en quelle année Ricardo expose-t-il la loi des rendements décroissants ?',
  'Des principes de l’économie politique et de l’impôt, en 1817.',
  x='Il y reprend la centralité physiocratique de la terre, mais pour montrer qu’elle devient une contrainte.',
  t='aut', b=130)

c('Qu’énonce la loi des rendements décroissants chez Ricardo ?',
  'Comme les meilleures terres sont cultivées en premier, chaque terre nouvellement mise en culture rend moins que la précédente.',
  x='À travail égal, la récolte progresse de moins en moins vite et le coût de production du blé s’élève.',
  t='aut', b=137)

c('Par quel enchaînement les rendements décroissants font-ils chuter les profits chez Ricardo ?',
  'Les coûts de production montent, le prix du blé s’élève, la rente des propriétaires augmente et les profits des fermiers diminuent.',
  x='C’est la baisse tendancielle du taux de profit : la rente capte ce que le profit perd.',
  t='mec', b=155)

c('Qu’est-ce que l’état stationnaire chez Ricardo ?',
  'Une situation où les profits ont disparu, donc l’investissement et la croissance aussi : l’économie s’arrête d’elle-même.',
  x='Vision pessimiste qui marque toute l’école classique : la croissance porte en elle sa propre extinction.',
  t='aut', b=158)

c('Qu’est-ce qu’un coût d’opportunité ?',
  'Ce à quoi l’on renonce pour produire une unité supplémentaire d’un bien.',
  x='C’est la notion sur laquelle repose l’avantage comparatif : on compare des renoncements, non des performances absolues.',
  t='def', b=163)

c('Qu’énonce la théorie ricardienne de l’avantage comparatif ?',
  'Chaque pays gagne à se spécialiser là où son coût d’opportunité est le plus faible, même s’il est moins productif partout.',
  x='Un pays en retard dans tous les secteurs se spécialise dans celui où son retard est le plus faible, et l’échange profite aux deux.',
  t='aut', b=162)

c('Pourquoi oppose-t-on un Smith optimiste à un Ricardo pessimiste ?',
  'Smith voit une richesse qui croît durablement par la division du travail ; Ricardo voit la croissance se bloquer dans un état stationnaire.',
  x='Malthus se range du côté pessimiste : les quatre figures classiques ne partagent donc pas le même pronostic.',
  t='dist', b=169)

c('En quoi Smith s’écarte-t-il des physiocrates sur l’origine de la richesse ?',
  'Il refuse de la réserver à l’agriculture : elle vient du travail humain et de la manière dont il est divisé, industrie comprise.',
  x='La poursuite de l’intérêt personnel n’y est pas un danger mais le ressort même de l’activité économique.',
  t='aut', b=177)

c('Quel exemple Smith emploie-t-il pour démontrer les effets de la division du travail ?',
  'La manufacture d’épingles : vingt épingles par ouvrier sans division des tâches, 4 800 avec.',
  x='Tirer le fil, couper, aiguiser, emballer : chaque geste confié à un ouvrier différent multiplie la productivité par plusieurs centaines.',
  t='aut', b=183)

c('Par quels trois effets la division du travail augmente-t-elle la productivité selon Smith ?',
  'L’habileté acquise par la répétition, le temps gagné en évitant les changements de tâche, et l’invention de machines par les travailleurs.',
  x='Le troisième effet est le plus important à long terme : la spécialisation engendre le progrès technique.',
  t='aut', b=195)

c('Quelle condition préalable la division du travail suppose-t-elle chez Smith ?',
  'L’échange et l’étendue du marché : on ne se spécialise que si l’on peut vendre ce que l’on produit.',
  x='C’est l’argument central en faveur du commerce intérieur et international : agrandir le marché, c’est permettre de se spécialiser davantage.',
  t='mec', b=197)

c('Comment le marché rétablit-il spontanément l’équilibre chez Smith ?',
  'Une hausse de la demande élève le prix et les profits, attire de nouveaux offreurs, accroît la production, ce qui fait redescendre le prix.',
  x='Le mouvement joue symétriquement à la baisse : c’est le fonctionnement concret de la main invisible.',
  t='mec', b=207)

c('Qu’est-ce qu’un avantage absolu selon Adam Smith ?',
  'La capacité à produire un bien avec moins de travail, à moindre coût ou avec une productivité supérieure à celle des autres pays.',
  x='La règle de spécialisation est donc simple : chacun produit ce qu’il fait le mieux, puis les pays échangent.',
  t='aut', b=216)

c('Quel exemple chiffré Ricardo utilise-t-il pour illustrer l’avantage comparatif ?',
  'Le Portugal et l’Angleterre, le vin et le drap : le Portugal produit 10 unités de vin par journée de travail contre 4 pour l’Angleterre.',
  x='Même supérieur dans les deux productions, le Portugal gagne à se concentrer là où son avance est la plus forte.',
  t='aut', b=224)

c('Qu’est-ce que la main invisible chez Adam Smith ?',
  'Le mécanisme par lequel la poursuite de l’intérêt personnel, tempérée par la concurrence et la flexibilité des prix, sert l’intérêt général.',
  x='Les prix s’ajustent en permanence au rapport de l’offre et de la demande : l’équilibre est spontané, non organisé.',
  t='aut', b=259)

c('Quelles sont les trois classes économiques chez Smith, et quel revenu perçoit chacune ?',
  'Les propriétaires fonciers perçoivent la rente, les industriels le profit, les travailleurs le salaire.',
  x='À la différence de Quesnay, elles fonctionnent sans hiérarchie : aucune n’est stérile.',
  t='aut', b=268)

c('Qu’énonce la loi d’airain des salaires ?',
  'Les salaires tendent inéluctablement à baisser vers le minimum de subsistance.',
  x='Elle explique que les classiques, malgré leur optimisme sur la richesse des nations, soient pessimistes sur le sort des travailleurs.',
  t='def', b=276)

c('Quel cercle vertueux de la croissance Smith décrit-il ?',
  'L’épargne finance l’investissement, qui fournit des machines, qui élèvent la productivité, donc les revenus, donc l’épargne.',
  x='La condition est de ne pas alourdir les coûts des entreprises : ni droits de douane, ni protectionnisme.',
  t='mec', b=282)

c('Qu’était le mouvement des enclosures, et quelles conséquences sociales a-t-il eues ?',
  'La clôture obligatoire des terres en grandes propriétés privées, qui a accru la productivité agricole mais expulsé les petits paysans.',
  x='Ces paysans deviennent des ouvriers pauvres : c’est l’un des trois faits qui nourrissent le pessimisme de Malthus.',
  t='fait', b=295)

c('Qu’étaient les poor laws anglaises ?',
  'Des aides aux pauvres organisées par les paroisses, étendues en 1722 à ceux qui vivaient en asile pour sédentariser les vagabonds.',
  x='Elles sont la cible directe de Malthus, qui y voit une cause de la misère plutôt qu’un remède.',
  t='fait', b=308)

c('Pourquoi Malthus s’oppose-t-il aux aides publiques aux pauvres ?',
  'Parce qu’elles les encouragent à avoir plus d’enfants, ce qui accroît la pression sur les ressources et aggrave la misère.',
  x='Sa conclusion est brutale : aider les pauvres les maintient dans la pauvreté.',
  t='aut', b=310)

c('Qu’énonce le principe de population formulé par Malthus en 1798 ?',
  'La population croît plus vite que la production agricole, qui ne pourra jamais la suivre.',
  x='Il en déduit la hausse du prix du blé, la baisse des salaires réels, une pauvreté structurelle et la famine comme frein naturel.',
  t='aut', b=317)

c('Pourquoi la pauvreté est-elle inévitable selon Malthus ?',
  'Parce qu’elle découle d’une loi naturelle et non d’une injustice sociale.',
  x='Cette naturalisation de la misère est exactement ce qui lui vaut d’être rangé parmi les classiques pessimistes.',
  t='aut', b=325)

c('Qu’est-ce que la rente différentielle ?',
  'L’écart de revenu entre une terre fertile et la terre marginale, dont le coût fixe le prix du blé.',
  x='La terre marginale ne dégage aucun surplus ; les meilleures, vendant au même prix pour un coût moindre, en dégagent un.',
  t='def', b=345)

c('En quoi Malthus annonce-t-il Keynes ?',
  'Il montre qu’une économie peut connaître la surproduction parce que les travailleurs sont trop pauvres pour acheter ce qu’ils produisent.',
  x='Il introduit ainsi la demande effective, c’est-à-dire la demande réellement solvable, cent cinquante ans avant la Théorie générale.',
  t='aut', b=350)

c('Pourquoi Malthus atténue-t-il sa thèse dans la version révisée de 1803 ?',
  'Les gains de productivité permettent de mieux nourrir la population, les importations de blé accroissent l’offre, et l’émigration déverse les excédents.',
  x='Son voyage en France et la paix d’Amiens de 1802, qui relance le commerce international, modifient son diagnostic.',
  t='aut', b=360)

c('Quelle erreur démographique reproche-t-on rétrospectivement à Malthus ?',
  'Avoir attribué la croissance de la population à la hausse de la fécondité, alors qu’elle venait de la baisse de la mortalité.',
  x='Il n’a pas vu le basculement démographique en cours sous ses yeux, ce qui fausse tout son pronostic.',
  t='mec', b=362)

c('Quel principe Malthus place-t-il à la base de toute l’économie politique ?',
  'Le principe de rareté : des besoins illimités affrontent une nature avare aux ressources limitées.',
  x='Il est le premier à faire de l’activité économique une lutte permanente, et à l’étudier sur des trajectoires longues.',
  t='aut', b=364)

c('Quelles sont les trois lois de base de l’économie classique que l’on doit à Malthus ?',
  'La loi de population, la loi des rendements décroissants et la théorie de la rente.',
  x='Population plus rapide que les ressources, terres nouvelles moins productives, rente née des écarts de fertilité.',
  t='aut', b=369)

c('Comment Malthus définit-il la demande effective ?',
  'La quantité d’un bien demandée par ceux qui ont les moyens d’en payer le prix.',
  x='C’est la demande solvable : si elle manque, les entreprises ne vendent plus et des crises de surproduction apparaissent.',
  t='aut', b=386)

c('Pourquoi un excès d’épargne peut-il déclencher une crise selon Malthus ?',
  'L’épargne finance l’investissement, mais si elle est trop forte elle ampute la consommation, donc la demande effective.',
  x='Il anticipe là encore un raisonnement que Keynes développera : l’épargne n’est pas automatiquement vertueuse.',
  t='aut', b=396)

c('Comment Marx explique-t-il la pauvreté, contre Malthus ?',
  'Non par une surpopulation naturelle, mais par l’exploitation capitaliste et l’armée de réserve qui maintient les salaires bas.',
  x='On passe d’une explication démographique de la misère à une explication sociale et historique.',
  t='aut', b=402)

c('Quel rôle Friedrich Engels joue-t-il auprès de Marx ?',
  'Fils d’industriel, il devient son soutien financier et son collaborateur, notamment pour le Manifeste du parti communiste en 1848.',
  x='La rente qu’il lui verse permet à Marx de poursuivre ses recherches sans exercer d’autre activité.',
  t='fait', b=407)

c('Quelle thèse historique le Manifeste du parti communiste énonce-t-il ?',
  'Que l’histoire des sociétés est fondée sur la lutte des classes.',
  x='Le texte est à la fois théorique et politique : il donne aux travailleurs une lecture cohérente du capitalisme.',
  t='aut', b=408)

c('Quelle est la différence entre valeur d’usage et valeur d’échange chez Marx ?',
  'La valeur d’usage est l’utilité concrète du bien ; la valeur d’échange est sa valeur marchande, fixée par le temps de travail socialement nécessaire.',
  x='L’utilité ne détermine donc pas le prix : c’est le travail incorporé qui le fait.',
  t='dist', b=417)

c('Que vend le travailleur au capitaliste selon Marx ?',
  'Non son travail achevé, mais sa force de travail pour une durée donnée.',
  x='La distinction est décisive : c’est elle qui permet de dire que la valeur créée excède la valeur payée.',
  t='aut', b=419)

c('Comment naît la plus-value chez Marx ?',
  'Une partie de la journée suffit à produire l’équivalent du salaire ; le reste produit une valeur supplémentaire non payée.',
  x='La plus-value est donc l’écart entre ce que rapporte le salarié et ce qu’il reçoit.',
  t='mec', b=420)

c('Quelle différence Marx fait-il entre capital constant et capital variable ?',
  'Le capital constant — machines, bâtiments, matières — ne crée aucune valeur nouvelle ; le capital variable, qui paie le travail, en crée.',
  x='Seul le travail vivant produit plus de valeur qu’il n’en coûte : c’est ce qui rend le profit possible.',
  t='dist', b=423)

c('Qu’est-ce que la composition organique du capital ?',
  'Le rapport du capital constant au capital variable, c’est-à-dire la part des machines par rapport au travail.',
  x='Combinée au taux de plus-value, elle détermine le taux de profit dans la formule de Marx.',
  t='def', b=426)

c('Pourquoi le taux de profit baisse-t-il tendanciellement selon Marx ?',
  'Parce que la composition organique du capital s’élève : on emploie plus de machines et moins de travail, seule source de valeur.',
  x='L’intensification de l’exploitation ne suffit pas à compenser ce mouvement : la baisse est structurelle.',
  t='mec', b=428)

c('Quel enchaînement conduit à la crise de surproduction chez Marx ?',
  'La baisse du taux de profit provoque des faillites, donc du chômage, donc une baisse de la consommation face à une production restée élevée.',
  x='Chaque crise relance temporairement l’accumulation, mais les contradictions se reforment : les crises sont structurelles.',
  t='mec', b=438)

c('En quoi la conception marxiste des lois économiques s’oppose-t-elle à celle des classiques ?',
  'Les classiques les tiennent pour naturelles et tendant vers l’équilibre ; Marx les tient pour historiques et liées au mode de production.',
  x='Pour lui, le capitalisme repose sur des relations antagonistes et produit nécessairement des crises.',
  t='dist', b=431)

c('Que partage Marx avec les économistes classiques ?',
  'La théorie de la valeur-travail, la distinction valeur d’usage / valeur d’échange, et le découpage en trois classes sociales.',
  x='Schumpeter le qualifie d’ailleurs de « dernier des classiques », malgré ses conclusions opposées.',
  t='aut', b=433)

c('Comment Marx explique-t-il la rente foncière et le profit industriel ?',
  'Comme deux formes d’appropriation d’une même plus-value, issues l’une et l’autre du capital.',
  x='Les classiques y voyaient des revenus de nature différente : Marx les ramène à une origine unique.',
  t='aut', b=434)

c('Quelle forme contemporaine de l’exploitation la sociologue Alizée Delpierre met-elle en évidence ?',
  'Une domination rapprochée : des employés domestiques bien rémunérés mais soumis à une disponibilité totale et à une dépendance affective.',
  x='L’exploitation y devient invisible parce qu’elle ne passe plus par le niveau du salaire mais par la perte d’autonomie.',
  t='aut', b=442)

c('Qu’est-ce qui oppose Marx et Say sur l’origine de la valeur ?',
  'Marx la fonde sur le travail, Say sur l’utilité.',
  x='C’est l’opposition la plus nette entre les deux : elle commande ensuite toute la lecture du profit et du salaire.',
  t='dist', b=471)

c('Comment les classiques et Marx expliquent-ils différemment le profit ?',
  'Les classiques y voient le revenu légitime du capital ou la rémunération de l’entrepreneur ; Marx y voit du travail non payé.',
  x='Le même fait comptable reçoit donc deux lectures incompatibles : un revenu ou un prélèvement.',
  t='dist', b=477)

c('Comment les différents auteurs classiques expliquent-ils le niveau du salaire ?',
  'Smith par le rapport de force, Ricardo et Malthus par la pression démographique, Say par la productivité.',
  x='Marx y voit le prix de la force de travail, maintenu bas par le chômage et la domination capitaliste.',
  t='dist', b=486)

c('Quel déplacement du regard les néoclassiques opèrent-ils à partir des années 1870 ?',
  'Ils abandonnent les classes sociales et les contradictions historiques pour les choix individuels et la formation des prix.',
  x='On passe d’une économie politique de la répartition à une économie formalisée de l’individu rationnel et de l’équilibre.',
  t='mec', b=516)

c('Comment les néoclassiques définissent-ils l’économie ?',
  'Comme la science des choix sous contrainte de rareté.',
  x='Ressources limitées et besoins illimités obligent à arbitrer : toute décision a un coût d’opportunité.',
  t='def', b=526)

c('Qu’est-ce que l’individualisme méthodologique ?',
  'La méthode qui explique les phénomènes collectifs à partir des comportements individuels agrégés.',
  x='Elle fonde l’approche microéconomique, à l’opposé d’un raisonnement partant des classes ou des structures historiques.',
  t='def', b=533)

c('Qu’est-ce que l’homo œconomicus ?',
  'L’agent type qui compare coûts et bénéfices et agit de façon cohérente pour améliorer sa situation.',
  x='Le consommateur y maximise son utilité sous contrainte de revenu, le producteur son profit sous contrainte de coûts.',
  t='def', b=548)

c('Qu’est-ce que l’utilité marginale, et pourquoi est-elle décroissante ?',
  'La satisfaction apportée par une unité supplémentaire consommée ; elle décroît car chaque unité de plus satisfait un besoin moins pressant.',
  x='Cette loi explique la demande : on achète tant que le gain de satisfaction dépasse le prix payé.',
  t='def', b=552)

c('Quel personnage Walras imagine-t-il pour expliquer la formation du prix d’équilibre ?',
  'Le commissaire-priseur, qui ajuste les prix jusqu’à ce que l’offre égale la demande.',
  x='Il joue chez Walras le rôle que la main invisible joue chez Smith : rendre intelligible une régulation sans organisateur.',
  t='aut', b=563)

c('Qu’est-ce que le surplus du consommateur ?',
  'L’écart entre ce qu’il était prêt à payer et ce qu’il paie réellement.',
  x='Ajouté au surplus du producteur, il forme le gain total à l’échange : c’est ce qui rend le marché mutuellement avantageux.',
  t='def', b=566)

c('Quelles sont les cinq conditions de la concurrence pure et parfaite ?',
  'Homogénéité des produits, atomicité des agents, mobilité des facteurs, libre entrée et sortie, transparence de l’information.',
  x='Réunies, elles garantissent une allocation efficace ; rarement vérifiées, elles expliquent les dysfonctionnements observés.',
  t='mec', b=572)

c('Quelle structure de marché naît de la différenciation des produits, et à quel auteur la doit-on ?',
  'La concurrence monopolistique, mise en évidence par Edward Chamberlin.',
  x='Marque, qualité, design donnent à chaque producteur un pouvoir de marché : le prix cesse d’être la seule variable.',
  t='aut', b=583)

c('Que signifie l’atomicité des agents, et qu’est-ce qui la remet en cause ?',
  'Chaque agent est trop petit pour influencer le prix ; la concentration des activités en oligopoles et monopoles la dément.',
  x='Les agents sont alors preneurs de prix en théorie, faiseurs de prix en pratique.',
  t='mec', b=585)

c('Qu’est-ce qu’un marché contestable, et à quel économiste doit-on cette notion ?',
  'Un marché où la seule menace d’entrée de concurrents suffit à discipliner les entreprises en place ; on la doit à William Baumol.',
  x='Elle nuance l’hypothèse de libre entrée : ce qui compte est moins l’entrée effective que sa possibilité crédible.',
  t='aut', b=592)

c('Quelle hypothèse de la concurrence pure et parfaite George Akerlof met-il en défaut ?',
  'La transparence de l’information : il montre que l’information est souvent asymétrique entre les agents.',
  x='Certains échanges deviennent alors impossibles, ou se font à des conditions faussées.',
  t='aut', b=595)

c('Qu’est-ce que tous les néoclassiques rejettent, et par quoi le remplacent-ils ?',
  'Ils rejettent la valeur-travail et expliquent la valeur par l’utilité marginale.',
  x='La valeur d’un bien dépend donc de la satisfaction qu’il procure à la marge, non du temps de travail qu’il a coûté.',
  t='mec', b=599)

c('Que cherche à démontrer Walras dans ses Éléments d’économie politique pure (1874) ?',
  'Que tous les marchés sont interdépendants et peuvent s’équilibrer simultanément : c’est l’équilibre général.',
  x='Son approche est très abstraite et mathématique, avec peu d’intérêt pour l’histoire ou les institutions.',
  t='aut', b=614)

c('En quoi l’approche de Marshall se distingue-t-elle de celle de Walras ?',
  'Il étudie les marchés un par un en équilibre partiel, distingue court et long terme, et réintroduit les coûts de production à côté de l’utilité.',
  x='Son école de Cambridge est plus pragmatique, là où celle de Lausanne est plus formelle.',
  t='dist', b=629)

c('Quelle image Marshall emploie-t-il pour expliquer la formation du prix ?',
  'Les deux lames d’une paire de ciseaux : la demande dépend de l’utilité marginale, l’offre des coûts.',
  x='Aucune des deux lames ne coupe seule : ni l’utilité ni le coût ne suffisent à expliquer le prix.',
  t='aut', b=636)

c('Qu’est-ce qui distingue l’école autrichienne des autres néoclassiques ?',
  'Elle refuse la formalisation mathématique et l’idée d’un équilibre général : le marché y est un processus de découverte.',
  x='Carl Menger la fonde en 1871 ; elle insiste sur le temps, l’incertitude et le caractère dispersé de l’information.',
  t='dist', b=644)

c('Pourquoi l’école autrichienne rejette-t-elle l’idée d’équilibre général ?',
  'Parce que l’information est dispersée, fragmentée et subjective : aucun agent ne possède une vision globale du système.',
  x='La concurrence y est par nature imparfaite et dynamique : elle repose sur l’ignorance et sur l’innovation.',
  t='mec', b=656)

c('Quelle thèse Hayek défend-il sur la neutralité de la monnaie ?',
  'Il la refuse : une création monétaire excessive abaisse artificiellement les taux, provoque un surinvestissement et mène à la crise.',
  x='Contrairement aux autres néoclassiques, il admet donc l’instabilité du capitalisme.',
  t='aut', b=658)

c('Qu’est-ce que classiques et néoclassiques partagent sur le rôle de l’État ?',
  'Les deux le cantonnent à garantir les règles, protéger la propriété et assurer le cadre institutionnel.',
  x='Le marché doit fonctionner sans pilotage central : le libéralisme économique est leur socle commun.',
  t='mec', b=679)

c('Sur quel objet d’analyse classiques et néoclassiques diffèrent-ils ?',
  'Les classiques étudient la croissance longue et la répartition des revenus ; les néoclassiques l’équilibre des marchés et la formation des prix.',
  x='Les uns raisonnent dans le temps long, les autres dans l’équilibre instantané.',
  t='dist', b=692)

c('En quoi la méthode des néoclassiques rompt-elle avec celle des classiques ?',
  'Ils substituent modèles, équations et courbes au raisonnement littéraire et qualitatif.',
  x='Walras, en 1874, fait basculer l’économie dans la formalisation mathématique.',
  t='dist', b=719)

c('Dans quel contexte Keynes écrit-il la Théorie générale en 1936 ?',
  'La Grande Dépression de 1929, un chômage de masse durable et l’échec du marché à rétablir seul le plein-emploi.',
  x='Son objectif est d’expliquer pourquoi une économie peut rester durablement en crise, et d’y proposer un remède.',
  t='fait', b=739)

c('Que reproche Keynes à l’économie dominante de son temps ?',
  'D’être trop abstraite et fondée sur des hypothèses irréalistes, au premier rang desquelles le plein-emploi et la rationalité parfaite.',
  x='Sa formule « à long terme, nous serons tous morts » justifie qu’il place le court terme au centre de l’analyse.',
  t='aut', b=744)

c('Comment Keynes définit-il la demande effective ?',
  'La demande que les entreprises s’attendent réellement à pouvoir écouler.',
  x='La production et l’emploi dépendent donc d’une anticipation des entrepreneurs, et non des capacités d’offre disponibles.',
  t='aut', b=752)

c('Pourquoi le chômage est-il involontaire chez Keynes ?',
  'Parce qu’il résulte d’une demande insuffisante qui conduit les entreprises à licencier, et non d’un refus de travailler.',
  x='Les chômeurs acceptent le salaire en vigueur : ce n’est pas leur comportement qui est en cause.',
  t='mec', b=755)

c('Quel est l’ordre du circuit keynésien ?',
  'La demande effective détermine la production, qui détermine l’emploi, donc les revenus, donc la consommation, qui alimente la demande.',
  x='La demande commande l’offre : l’enchaînement est l’inverse exact de la loi de Say.',
  t='mec', b=760)

c('Qu’est-ce que le paradoxe de l’épargne chez Keynes ?',
  'Ce qui est rationnel pour un individu — épargner davantage — devient nuisible collectivement en réduisant la demande.',
  x='L’épargne cesse d’être automatiquement vertueuse, contre la position des classiques.',
  t='aut', b=772)

c('Qu’appelle-t-on les esprits animaux chez Keynes ?',
  'Les ressorts psychologiques — confiance, optimisme, peur — qui commandent la décision d’investir.',
  x='L’investissement ne dépend donc pas du seul taux d’intérêt : il est incertain et en partie irrationnel.',
  t='def', b=775)

c('Pourquoi la monnaie n’est-elle pas neutre chez Keynes ?',
  'Parce que les agents peuvent préférer la conserver plutôt que l’investir, ce qui agit directement sur la production et l’emploi.',
  x='Le taux d’intérêt y est le prix du renoncement à la liquidité, non le prix de l’épargne.',
  t='mec', b=778)

c('Pourquoi une baisse des salaires ne résorbe-t-elle pas le chômage selon Keynes ?',
  'Parce qu’elle réduit la demande, ce qui peut aggraver la crise au lieu de la corriger.',
  x='Les salariés négocient d’ailleurs des salaires nominaux, rigides à la baisse : le salaire réel ne s’ajuste pas librement.',
  t='mec', b=785)

c('Quelle rupture majeure l’équilibre keynésien introduit-il face aux classiques ?',
  'L’économie peut être à l’équilibre sans être au plein emploi.',
  x='L’équilibre cesse d’être un état souhaitable : il peut être un mauvais équilibre dont rien ne fait sortir.',
  t='mec', b=819)

c('Sur quoi l’emploi repose-t-il chez Keynes ?',
  'Sur le niveau de la demande globale, et non sur le fonctionnement du marché du travail.',
  x='C’est pourquoi agir sur les salaires est inefficace : il faut agir sur les débouchés.',
  t='mec', b=852)

c('Quels moyens Keynes assigne-t-il à l’État pour sortir d’un équilibre de sous-emploi ?',
  'La politique budgétaire — dépenses publiques et déficit — et le soutien à l’investissement.',
  x='L’État crée une demande autonome, qui ne dépend d’aucun revenu préalable et peut donc amorcer la reprise.',
  t='mec', b=856)

c('Qui Keynes range-t-il sous le nom de « classiques » ?',
  'Les classiques historiques — Smith, Ricardo, Malthus, Say — et les néoclassiques.',
  x='Ce qui les unit à ses yeux est la confiance dans l’autorégulation du marché, non une doctrine commune de la valeur.',
  t='aut', b=860)

c('Qu’est-ce que Keynes ne reproche pas au marché ?',
  'Son existence : il raisonne dans une économie de marché non planifiée et reconnaît la place des choix privés.',
  x='Le désaccord ne porte pas sur l’existence des décisions individuelles mais sur leur coordination spontanée.',
  t='mec', b=871)

c('Comment les classiques et Keynes expliquent-ils différemment le chômage ?',
  'Les classiques y voient un chômage volontaire dû à la rigidité des salaires ; Keynes un chômage involontaire dû à l’insuffisance de la demande.',
  x='Le chômage cesse d’être un problème de marché du travail pour devenir un problème macroéconomique.',
  t='dist', b=906)

c('Comment Keynes conçoit-il le temps, face aux classiques ?',
  'Comme un temps historique et incertain, où les décisions se prennent sous incertitude radicale.',
  x='Le futur n’est pas calculable : il ne s’agit pas d’un risque probabilisable mais d’une véritable ignorance.',
  t='dist', b=934)

c('Pourquoi Hicks et Samuelson entreprennent-ils de reformuler Keynes ?',
  'Parce que la Théorie générale est peu mathématisée et s’intègre mal aux outils néoclassiques dominants.',
  x='Leur projet est une conciliation : sauver Keynes sans rejeter la théorie dominante.',
  t='aut', b=945)

c('Que représentent les courbes IS et LM dans le modèle de Hicks ?',
  'IS les couples revenu–taux d’intérêt qui équilibrent le marché des biens ; LM ceux qui équilibrent le marché de la monnaie.',
  x='Leur intersection détermine simultanément un revenu et un taux d’intérêt d’équilibre.',
  t='aut', b=966)

c('Quelle critique adresse-t-on au modèle IS-LM de Hicks au regard de la pensée de Keynes ?',
  'Il transforme une théorie du déséquilibre en un modèle d’équilibre.',
  x='Keynes montrait qu’une économie pouvait rester durablement en crise ; Hicks ramène son analyse à un raisonnement d’équilibre.',
  t='mec', b=971)

c('Comment Samuelson articule-t-il court et long terme dans la synthèse ?',
  'À court terme l’économie est keynésienne — prix rigides, rôle de la demande ; à long terme les mécanismes néoclassiques reprennent le dessus.',
  x='Ce partage permet de défendre l’intervention conjoncturelle sans renoncer à l’efficacité des marchés.',
  t='aut', b=977)

c('Quelles critiques adresse-t-on à la synthèse néo-keynésienne ?',
  'Avoir affaibli la rupture de Keynes, sous-estimé l’incertitude et les anticipations, et réintroduit trop fortement l’équilibre.',
  x='Elle a pourtant dominé l’enseignement et inspiré les politiques des Trente Glorieuses.',
  t='mec', b=985)

c('Que cherche à établir la théorie du déséquilibre développée à partir des années 1960 ?',
  'Qu’une économie peut fonctionner durablement hors équilibre et que les marchés ne s’auto-ajustent pas.',
  x='Clower, Leijonhufvud et Malinvaud partent du chômage durable et de crises qui ne se résorbent pas seules.',
  t='aut', b=999)

c('Par quoi l’ajustement se fait-il dans la théorie du déséquilibre, à défaut des prix ?',
  'Par les quantités : la production et l’emploi, avec un rationnement possible.',
  x='Prix et salaires étant rigides, c’est le volume d’activité qui absorbe le choc, et le déséquilibre peut durer.',
  t='mec', b=1008)

c('Quelle distinction Robert Clower introduit-il entre deux types de demande ?',
  'La demande notionnelle, ce que les agents voudraient faire, et la demande effective, ce qu’ils peuvent faire compte tenu de leur revenu.',
  x='Un travailleur rationné sur le marché du travail voit son revenu baisser, donc sa demande de biens contrainte.',
  t='aut', b=1014)

c('Quelle critique la théorie du déséquilibre adresse-t-elle au modèle IS-LM ?',
  'Il suppose des comportements d’équilibre et l’absence de rationnement, si bien que son équilibre peut masquer un déséquilibre réel.',
  x='En situation de chômage, la demande est contrainte par les revenus : les marchés ne s’ajustent pas comme le modèle le prévoit.',
  t='mec', b=1022)

c('Quels faits des années 1970 ébranlent la crédibilité du keynésianisme ?',
  'Les chocs pétroliers de 1973 et 1979, une stagflation inédite et la hausse continue des déficits publics.',
  x='La courbe de Phillips, qui postulait un arbitrage stable entre inflation et chômage, n’explique pas ces phénomènes.',
  t='fait', b=1039)

c('D’où viennent les déséquilibres économiques selon les monétaristes ?',
  'D’une mauvaise gestion de la monnaie, et non d’un manque de demande.',
  x='Ils replacent ainsi la monnaie au cœur de la macroéconomie, contre l’analyse keynésienne par les débouchés.',
  t='mec', b=1046)

c('Quelle critique les monétaristes adressent-ils aux politiques de relance ?',
  'Elles sont inflationnistes et l’intervention discrétionnaire de l’État aggrave les cycles au lieu de les corriger.',
  x='L’État cesse d’être une solution pour devenir, dans cette lecture, une source du problème.',
  t='mec', b=1061)

c('Quelle règle monétaire Friedman préconise-t-il ?',
  'Faire croître la masse monétaire à un rythme constant, indépendant de la conjoncture.',
  x='L’objectif est de retirer toute marge discrétionnaire à l’État : seule la stabilité monétaire lui revient.',
  t='aut', b=1079)

c('Quelles politiques les idées monétaristes ont-elles inspirées dans les années 1980 ?',
  'Celles conduites par Reagan aux États-Unis et Thatcher au Royaume-Uni.',
  x='Elles privilégient l’offre : restaurer le taux de marge des entreprises et libéraliser l’économie.',
  t='fait', b=1086)

c('Qui sont les principaux représentants de la Nouvelle Économie classique ?',
  'Robert Lucas et Thomas Sargent.',
  x='Ils ne corrigent pas le keynésianisme comme les monétaristes : ils cherchent à rompre entièrement avec lui.',
  t='aut', b=1093)

c('Qu’est-ce qu’une anticipation rationnelle chez Lucas ?',
  'Les agents utilisent toute l’information disponible, comprennent le fonctionnement de l’économie et anticipent correctement les politiques.',
  x='Contrairement aux anticipations adaptatives de Friedman, elles ne laissent aucune place à une illusion monétaire durable.',
  t='aut', b=1096)

c('Pourquoi la Nouvelle Économie classique juge-t-elle les politiques de relance totalement inefficaces ?',
  'Parce que les agents anticipent l’inflation future, ajustent salaires, prix et épargne, et annulent ainsi l’effet réel de la politique.',
  x='La monnaie y est neutre même à court terme, là où Friedman lui laissait encore un effet transitoire.',
  t='mec', b=1111)

c('À quoi la NEC attribue-t-elle les fluctuations économiques ?',
  'À des chocs exogènes, technologiques ou monétaires, et non à une insuffisance de la demande.',
  x='Le chômage y redevient volontaire ou frictionnel, jamais durable.',
  t='mec', b=1119)

c('Quelle politique économique la NEC recommande-t-elle ?',
  'Aucune politique discrétionnaire : seulement des règles simples, crédibles et stables dans le temps.',
  x='L’intervention est jugée non seulement inutile mais dangereuse, car elle perturbe les anticipations.',
  t='mec', b=1128)

c('Quelles critiques sont adressées à la Nouvelle Économie classique ?',
  'Des hypothèses jugées irréalistes, des agents trop rationnels et l’incapacité à expliquer les crises majeures.',
  x='Ces objections ouvrent la voie, dans les années 1980, à la Nouvelle Économie keynésienne.',
  t='mec', b=1140)

c('Quel est l’objectif central de la Nouvelle Économie keynésienne ?',
  'Montrer que même avec des agents rationnels et des marchés concurrentiels, le chômage involontaire et les déséquilibres durables sont possibles.',
  x='Elle conserve donc les conclusions de Keynes, mais les fonde sur des microfondements néoclassiques.',
  t='mec', b=1157)

c('Qu’est-ce qu’un menu cost ?',
  'Le coût que représente pour une entreprise la modification de ses prix affichés.',
  x='Avec les contrats longs et les conventions salariales, il explique que prix et salaires ne s’ajustent pas instantanément.',
  t='def', b=1169)

c('Quelles imperfections la NEK oppose-t-elle à la NEC ?',
  'Les rigidités de prix et de salaires, les asymétries d’information et la concurrence imparfaite.',
  x='Ces trois imperfections suffisent à faire réapparaître un chômage involontaire durable.',
  t='mec', b=1165)

c('Que dit la NEK du rôle de la monnaie et de l’État ?',
  'La monnaie n’est pas neutre à court et moyen terme, et les politiques budgétaire et monétaire peuvent stabiliser l’économie.',
  x='L’intervention publique peut améliorer le fonctionnement du marché, au lieu de le perturber systématiquement.',
  t='mec', b=1191)

c('Quel est le positionnement de Thorstein Veblen dans la pensée économique ?',
  'Hétérodoxe : il critique l’orthodoxie néoclassique sans devenir marxiste.',
  x='Il écrit à la fin du XIXᵉ siècle, quand le capitalisme industriel américain et la finance prennent leur essor.',
  t='aut', b=1215)

c('Pourquoi Veblen rejette-t-il l’homo œconomicus ?',
  'Parce que les comportements économiques dépendent des habitudes, des normes, des institutions et de la recherche de statut.',
  x='L’économie doit donc s’analyser comme une réalité historique et sociale, non comme un équilibre abstrait.',
  t='aut', b=1218)

c('Qu’est-ce que la classe de loisir chez Veblen, et dans quel ouvrage l’introduit-il ?',
  'Une classe dominante qui ne produit pas, vit du capital et de la rente, et impose les normes du prestige ; dans Théorie de la classe de loisir (1899).',
  x='Son pouvoir ne repose pas sur la production mais sur la hiérarchie sociale qu’elle institue.',
  t='aut', b=1227)

c('Qu’est-ce que la consommation ostentatoire ?',
  'Consommer non pour satisfaire un besoin, mais pour afficher sa richesse et son statut.',
  x='Elle devient un instrument de distinction, de reconnaissance sociale et de domination symbolique.',
  t='def', b=1233)

c('Par quel mécanisme les hiérarchies sociales se reproduisent-elles chez Veblen ?',
  'Par l’imitation : les classes inférieures copient les signes de richesse de la classe dominante, parfois au détriment de leurs besoins essentiels.',
  x='Ce n’est donc pas une lutte des classes mais une émulation sociale, qui entretient inégalités et gaspillage.',
  t='mec', b=1241)

c('Qu’est-ce qui sépare l’analyse des classes chez Marx et chez Veblen ?',
  'Marx définit les classes par la place dans la production et explique la domination par l’exploitation ; Veblen la fonde sur le statut et l’émulation.',
  x='Conflit d’un côté, conformisme culturel de l’autre : les deux mécanismes de reproduction n’ont rien de commun.',
  t='dist', b=1252)

c('Pourquoi la classe de loisir de Veblen ne se confond-elle pas avec la classe stérile de Quesnay ?',
  'Quesnay classe selon la productivité économique, Veblen selon le prestige social.',
  x='La classe stérile travaille sans créer de produit net ; la classe de loisir se définit précisément par son oisiveté affichée.',
  t='dist', b=1257)

c('Quelles deux logiques Veblen oppose-t-il dans Théorie de l’entreprise d’affaires (1904) ?',
  'Celle des ingénieurs, tournée vers l’efficacité technique, et celle des hommes d’affaires, tournée vers le profit monétaire.',
  x='Produire mieux et plus d’un côté, maximiser la rentabilité de l’autre : les deux objectifs ne coïncident pas.',
  t='aut', b=1270)

c('Qu’appelle-t-on le sabotage de la production chez Veblen ?',
  'Le fait, pour les hommes d’affaires, de freiner volontairement la production et d’organiser des raretés artificielles pour maintenir des prix élevés.',
  x='Produire davantage ferait baisser les prix, donc les profits : l’intérêt financier s’oppose à l’efficacité productive.',
  t='mec', b=1285)

c('Quel constat conduit Douglass North à renouveler l’analyse économique par l’histoire ?',
  'Que l’accumulation de capital et le progrès technique n’expliquent pas les écarts durables de développement entre pays.',
  x='Il cherche ce qui fait que certaines économies se développent durablement et d’autres non.',
  t='aut', b=1297)

c('Comment Douglass North définit-il les institutions ?',
  'L’ensemble des règles formelles — lois, droits de propriété, contrats — et informelles — coutumes, traditions — qui encadrent les comportements.',
  x='Les individus restent rationnels, mais leur rationalité s’exerce toujours dans un cadre institutionnel donné.',
  t='aut', b=1317)

c('Qu’est-ce qu’un coût de transaction ?',
  'Le coût d’information, de négociation, de contrôle et d’exécution qu’implique tout échange.',
  x='De bonnes institutions les réduisent, de mauvaises les augmentent : le marché n’est jamais gratuit.',
  t='def', b=1331)

c('De quoi dépend la croissance durable selon North ?',
  'De la qualité des institutions : droits de propriété protégés, règles stables et crédibles, incitations à investir et à innover.',
  x='Moins de l’accumulation de capital ou des économies d’échelle que les théories standard mettaient en avant.',
  t='aut', b=1337)

c('Qu’est-ce que la dépendance au sentier chez North ?',
  'Le fait que les choix institutionnels passés conditionnent fortement les trajectoires futures.',
  x='Une organisation institutionnelle défaillante peut ainsi enfermer durablement une économie dans un équilibre inefficace.',
  t='def', b=1350)

c('Quelle position North adopte-t-il sur le rôle de l’État ?',
  'Il le juge indispensable pour définir et faire respecter les règles, mais nuisible s’il devient prédateur ou instable.',
  x='Le problème n’est donc pas la présence de l’État mais la qualité de ses institutions.',
  t='aut', b=1358)

c('Quels ouvrages fondent l’école de la régulation, et qui en sont les auteurs ?',
  'Régulation et crises du capitalisme de Michel Aglietta (1976) et La théorie de la régulation de Robert Boyer (1986).',
  x='Elle naît en France dans les années 1970, face à des crises que ni les néoclassiques ni les keynésiens standard n’expliquent.',
  t='aut', b=1369)

c('Qu’est-ce qu’un régime d’accumulation ?',
  'La manière dont la production, la répartition et la consommation s’articulent dans le temps.',
  x='Il peut être extensif, fondé sur les quantités, ou intensif, fondé sur la productivité ; il n’est viable que s’il est cohérent.',
  t='def', b=1391)

c('Qu’est-ce qu’un mode de régulation ?',
  'L’ensemble des institutions qui stabilisent temporairement le capitalisme.',
  x='Il comprend le rapport salarial, la concurrence, la monnaie, l’État et l’insertion internationale.',
  t='def', b=1398)

c('Qu’est-ce que la régulation concurrentielle qui précède 1929 ?',
  'Un régime à salaires flexibles, faible intervention de l’État, ajustement par les prix et accumulation extensive.',
  x='La surproduction devait se résorber par la baisse des prix et des salaires : elle a produit une insuffisance de demande.',
  t='def', b=1410)

c('Comment l’école de la régulation interprète-t-elle la crise de 1929 ?',
  'Non comme un choc accidentel, mais comme l’épuisement du mode de régulation concurrentiel.',
  x='La crise révèle une incompatibilité entre le régime d’accumulation et les institutions censées le stabiliser.',
  t='aut', b=1422)

c('Sur quels éléments repose la régulation fordiste installée après 1945 ?',
  'Des salaires indexés sur la productivité, une consommation de masse, une forte intervention de l’État et des politiques keynésiennes.',
  x='Ce compromis explique la croissance et la stabilité relative des Trente Glorieuses.',
  t='mec', b=1425)

c('Qu’est-ce qui fissure le compromis fordiste à partir des années 1970 ?',
  'Le ralentissement des gains de productivité, les tensions inflationnistes, la montée du chômage et la mondialisation.',
  x='Pour les régulationnistes, le capitalisme entre alors dans une nouvelle phase de crise structurelle, non conjoncturelle.',
  t='mec', b=1435)

c('Quelle place l’école de la régulation accorde-t-elle à l’État ?',
  'Un élément central de la régulation, qui structure les marchés et stabilise la demande, sans pouvoir empêcher toutes les crises.',
  x='Il ne fait que les déplacer ou les transformer : aucune institution ne stabilise le capitalisme définitivement.',
  t='mec', b=1443)

c('Dans quel contexte Kate Raworth formule-t-elle la théorie du donut ?',
  'La crise financière de 2008, l’aggravation des inégalités, l’urgence climatique et la remise en cause du PIB.',
  x='Elle publie L’économie du donut en 2017, sous-titré « l’économie de demain en 7 principes ».',
  t='aut', b=1461)

c('Que reproche Kate Raworth à l’économie standard ?',
  'D’ignorer les limites planétaires, de tolérer des inégalités massives et de confondre le moyen — la croissance — avec la finalité — le bien-être.',
  x='Elle remet aussi en cause l’homo œconomicus isolé et l’idée que le marché s’autorégule naturellement.',
  t='aut', b=1478)

c('Entre quelles deux limites le donut de Kate Raworth définit-il un espace sûr et juste ?',
  'Un plancher social, qui couvre les besoins humains fondamentaux, et un plafond écologique, formé des limites planétaires.',
  x='Alimentation, santé, éducation, logement pour le premier ; climat, biodiversité, pollution, ressources pour le second.',
  t='aut', b=1484)
