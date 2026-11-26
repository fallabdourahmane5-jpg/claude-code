# -*- coding: utf-8 -*-
"""Première année — chapitre 2. Le financement de l'économie."""

from fc_base import lot, c

L = lot(2)

c('Quel terme Christine Lagarde emploie-t-elle pour décrire l’enchaînement des crises récentes ?',
  'La permacrise.',
  x='Elle désigne une succession continue de crises majeures et inédites, sans retour à une situation normale entre deux.',
  t='aut', b=3)

c('Qu’est-ce que la monnaie ?',
  'Un actif liquide qui sert à évaluer et à régler les échanges.',
  x='Liquide signifie mobilisable immédiatement, sans délai ni perte de valeur.',
  t='def', b=7)

c('Quelles sont les trois caractéristiques de la monnaie ?',
  'C’est un actif, une unité de compte et un moyen de règlement.',
  x='L’unité de compte mesure la valeur des biens, le moyen de règlement éteint la dette née de l’échange.',
  t='mec', b=9)

c('Pourquoi dit-on que la monnaie est à la fois un bien public et un bien privé ?',
  'Publique parce qu’elle rend service à toute la société en facilitant les échanges ; privée parce que chacun la détient et l’utilise pour son propre compte.',
  x='Comme bien public elle produit des externalités positives : en permettant le commerce, elle soutient production et croissance.',
  t='mec', b=14)

c('Quelle part de la monnaie en circulation dans la zone euro est scripturale ?',
  'Environ 91 %.',
  x='L’essentiel des opérations bancaires sont des virements et des prélèvements, non des échanges d’espèces.',
  t='fait', b=25)

c('Quel plafond s’applique au paiement en espèces en France ?',
  '1 000 euros.',
  x='Le commerçant peut par ailleurs refuser un chèque, alors qu’il ne peut en principe refuser les espèces en deçà du plafond.',
  t='fait', b=26)

c('Qu’est-ce qui distingue un compte courant d’un compte à terme ?',
  'Les sommes du compte courant sont récupérables sans délai ni coût ; celles du compte à terme sont bloquées pendant une durée convenue.',
  x='En France, la gratuité des chèques a pour contrepartie l’absence de rémunération des comptes courants.',
  t='dist', b=28)

c('Quelle différence y a-t-il entre la monnaie scripturale et son support ?',
  'La monnaie scripturale est la somme inscrite sur le compte ; le support est le moyen qui permet de la transférer.',
  x='Carte, chèque, virement, prélèvement ou application mobile ne sont donc pas de la monnaie, mais des instruments de circulation.',
  t='dist', b=33)

c('Quelles formes la monnaie a-t-elle successivement prises au cours de l’histoire ?',
  'Métallique, puis fiduciaire, puis scripturale.',
  x='La tendance longue est à la dématérialisation : chaque étape éloigne un peu plus la monnaie d’un support ayant une valeur propre.',
  t='mec', b=35)

c('Quels arguments les banques avancent-elles en faveur de la disparition des billets ?',
  'La fabrication des billets et l’entretien des distributeurs coûtent cher, et la monnaie scripturale permet de tracer les transactions.',
  x='Le paiement en espèces est le seul paiement anonyme : sa disparition met fin à la thésaurisation hors du système bancaire.',
  t='mec', b=36)

c('Quels arguments oppose-t-on à la suppression des espèces ?',
  'Le risque de fraude électronique et la règle de la zone euro qui garantit la possibilité de payer partout en liquide.',
  x='Les banques répondent par le cash back : le client paie plus que le montant dû par carte et le commerçant lui rend des billets.',
  t='mec', b=39)

c('Quel décalage observe-t-on en France entre le nombre et le montant des paiements par carte ?',
  'La carte représente 56,6 % des opérations mais seulement 1,6 % des montants échangés.',
  x='Virements et prélèvements font l’inverse : un tiers des opérations, mais près de 97 % des montants.',
  t='fait', b=45)

c('Qu’est-ce qu’un titre de créance négociable ?',
  'Un actif financier de court ou moyen terme qui permet de se procurer des fonds sur le marché monétaire, sans passer par le crédit bancaire.',
  x='Son montant unitaire minimum est de 150 000 euros : il s’adresse aux investisseurs institutionnels, non aux particuliers.',
  t='def', b=48)

c('Quelles sont les trois catégories de titres de créance négociables, et qui les émet ?',
  'Les certificats de dépôt par les banques, les billets de trésorerie par les entreprises, les bons du Trésor par l’État.',
  x='Les deux premiers courent d’un jour à un an, les bons du Trésor de treize semaines à cinq ans.',
  t='mec', b=49)

c('Qu’est-ce que la masse monétaire ?',
  'La quantité totale de monnaie en circulation dans une économie à un moment donné.',
  x='On la mesure par des agrégats emboîtés, classés du plus liquide au moins liquide.',
  t='def', b=54)

c('Que contiennent respectivement les agrégats M1, M2 et M3 ?',
  'M1 les billets et comptes courants ; M2 ajoute l’épargne courte ; M3 ajoute les placements monétaires.',
  x='Livrets et dépôts à terme pour M2, OPCVM et bons du Trésor pour M3 : c’est M3 que la banque centrale surveille.',
  t='mec', b=56)

c('Qu’est-ce qu’un OPCVM ?',
  'Un organisme de placement collectif en valeurs mobilières, qui réunit l’épargne de plusieurs investisseurs pour la placer en titres.',
  x='Il en existe deux formes : le fonds commun de placement et la société d’investissement à capital variable.',
  t='def', b=60)

c('Quelle différence sépare une SICAV d’un fonds commun de placement ?',
  'Dans une SICAV l’investisseur est actionnaire ; dans un FCP il est porteur de parts et copropriétaire du portefeuille.',
  x='Le FCP n’a pas de personnalité morale : c’est une copropriété de valeurs mobilières, non une société.',
  t='dist', b=80)

c('À quel auteur fait-on remonter les trois fonctions traditionnelles de la monnaie ?',
  'À Aristote, vers 350 avant notre ère.',
  x='Unité de compte, intermédiaire des échanges et réserve de valeur : la typologie a traversé vingt-quatre siècles.',
  t='aut', b=84)

c('Que signifie le pouvoir libératoire absolu du billet ?',
  'Il permet d’éteindre n’importe quelle dette : tout peut être acheté avec lui.',
  x='C’est ce qui distingue la monnaie légale d’un simple moyen de paiement que le créancier pourrait refuser.',
  t='def', b=86)

c('Quelle monnaie dominait les échanges internationaux jusqu’en 1914, et pourquoi a-t-elle cédé la place ?',
  'La livre sterling, détrônée par le dollar après l’endettement britannique de la Première Guerre mondiale.',
  x='Le basculement est scellé après 1945 par Bretton Woods et le plan Marshall, qui installent le dollar au centre du système.',
  t='fait', b=88)

c('Combien de fonctions Krugman reconnaît-il à une monnaie internationale, et selon quels points de vue ?',
  'Six fonctions, réparties entre le secteur privé et les banques centrales.',
  x='Trois pour chacun : une monnaie n’est internationale que si les entreprises et les États l’utilisent tous deux.',
  t='aut', b=90)

c('Qu’appelle-t-on monnaie de libellé ?',
  'La monnaie dans laquelle les prix sont exprimés, qui sert d’unité de compte internationale.',
  x='Le pétrole est coté en dollars même lorsqu’il est vendu par un pays asiatique à un pays européen.',
  t='def', b=93)

c('Qu’appelle-t-on monnaie véhiculaire ?',
  'La monnaie employée pour régler les paiements internationaux entre pays qui n’ont pas la même devise.',
  x='Elle sert de pivot : plutôt que de convertir deux fois, les partenaires passent par la monnaie la plus utilisée.',
  t='def', b=98)

c('Qu’appelle-t-on monnaie d’investissement ?',
  'La monnaie dans laquelle les investisseurs placent leurs avoirs, et qui sert de référence aux placements internationaux.',
  x='Obligations américaines et actions en dollars attirent parce que la devise est à la fois stable et liquide.',
  t='def', b=102)

c('Qu’est-ce qu’une monnaie d’ancrage ?',
  'La devise de référence à laquelle un pays fixe le taux de change de sa propre monnaie.',
  x='Le franc CFA est ancré à l’euro, le dollar de Hong Kong au dollar américain.',
  t='def', b=107)

c('Qu’est-ce qu’une monnaie d’intervention ?',
  'Celle qu’une banque centrale achète ou vend sur le marché des changes pour stabiliser le cours de sa propre devise.',
  x='La Banque du Japon vend ou achète des dollars pour tenir la valeur du yen face à la devise américaine.',
  t='def', b=110)

c('Qu’est-ce qu’une monnaie de réserve ?',
  'Celle dans laquelle les banques centrales détiennent leurs réserves officielles de change.',
  x='Cela suppose la confiance : la devise doit conserver sa valeur dans la durée. Le dollar domine encore largement ces réserves.',
  t='def', b=114)

c('Combien de pays composent la zone euro aujourd’hui, et comment ce nombre évolue-t-il ?',
  'Quinze à l’origine, vingt en 2025, vingt et un en 2026 avec l’entrée de la Bulgarie.',
  x='Avant 1999, autant de politiques monétaires que de pays ; aujourd’hui une seule, conduite par la BCE.',
  t='fait', b=121)

c('Qu’était le système monétaire européen, et pourquoi a-t-il échoué ?',
  'Un système où les monnaies européennes ne devaient pas s’écarter de plus de 2,5 % ; les banques centrales n’ont plus réussi à tenir ces marges.',
  x='Il reposait sur l’ECU, qui n’était pas une monnaie mais une unité de compte, moyenne pondérée des devises européennes.',
  t='fait', b=124)

c('Quelle est la différence entre l’Eurosystème et le Système européen de banques centrales ?',
  'L’Eurosystème réunit la BCE et les banques centrales des pays ayant adopté l’euro ; le SEBC y ajoute celles des pays de l’UE hors zone euro.',
  x='Andorre utilise l’euro sans appartenir à l’Union : elle ne fait donc partie ni de l’un ni de l’autre.',
  t='dist', b=126)

c('Quelles sont les trois missions de la Banque centrale européenne ?',
  'Assurer la stabilité des prix, garantir la liquidité du système bancaire et jouer le rôle de prêteur en dernier ressort.',
  x='La stabilité des prix est l’objectif principal, avec une cible d’inflation proche de 2 %.',
  t='mec', b=130)

c('Qu’est-ce que le risque de change ?',
  'Le risque qu’une variation du taux de change modifie la valeur d’une opération déjà engagée.',
  x='Celui qui a converti ses francs en marks perd si la monnaie est ensuite dévaluée : cette incertitude décourage les échanges.',
  t='def', b=139)

c('Quelle est la différence entre une dépréciation et une dévaluation ?',
  'La dépréciation est une baisse de marché en change flottant ; la dévaluation est une baisse décidée par l’État en change fixe.',
  x='Le critère est donc la nature du régime de change, et non l’ampleur du mouvement.',
  t='dist', b=142)

c('Qu’est-ce qui distingue un régime de change fixe d’un régime de change flottant ?',
  'Dans le premier, l’autorité publique fixe la parité ; dans le second, le marché la détermine par l’offre et la demande.',
  x='Le flottement laisse à la banque centrale une politique monétaire autonome, au prix d’une incertitude pour les entreprises.',
  t='dist', b=148)

c('Qui gagne et qui perd lorsque l’euro s’apprécie face au dollar ?',
  'Les importateurs européens et les exportateurs américains y gagnent ; les exportateurs européens et les importateurs américains y perdent.',
  x='C’est l’illustration type d’intérêts contradictoires entre agents : aucune parité n’avantage tout le monde.',
  t='mec', b=150)

c('Qu’est-ce qu’une dépréciation compétitive ?',
  'Une baisse volontaire de la valeur de la monnaie destinée à rendre les exportations plus compétitives et à relancer la croissance.',
  x='Quand plusieurs pays y recourent simultanément, on parle de dumping monétaire ou de guerre des monnaies.',
  t='def', b=155)

c('Pourquoi le dumping monétaire est-il impossible à l’intérieur de la zone euro ?',
  'Parce que les pays partagent la même monnaie : aucun ne peut dévaluer par rapport à ses partenaires.',
  x='L’ajustement par le change étant fermé, il doit passer par les coûts salariaux : c’est la dévaluation interne.',
  t='mec', b=157)

c('Qu’est-ce qu’un choc asymétrique dans une union monétaire ?',
  'Un événement qui frappe inégalement les pays membres, comme une récession espagnole sans équivalent allemand.',
  x='Il est le problème central d’une monnaie unique : une seule politique monétaire doit répondre à des situations divergentes.',
  t='def', b=158)

c('Quelles difficultés rencontrerait un pays qui quitterait la zone euro ?',
  'Sa nouvelle monnaie, plus faible, renchérirait ses importations et alourdirait une dette restée libellée en euros ou en dollars.',
  x='La défiance des marchés accélérerait la dépréciation, ce qui aggraverait les deux effets précédents.',
  t='mec', b=160)

c('Quels sont les trois objectifs du triangle d’incompatibilité de Mundell ?',
  'La libre circulation des capitaux, l’autonomie de la politique monétaire et la stabilité du taux de change.',
  x='Formulé dans les années 1960, il établit qu’on ne peut jamais en retenir que deux sur trois.',
  t='aut', b=170)

c('Que doit abandonner un pays qui veut à la fois une politique monétaire autonome et la libre circulation des capitaux ?',
  'La stabilité de son taux de change.',
  x='C’est le choix des États-Unis : politique monétaire indépendante et change flottant.',
  t='mec', b=179)

c('Que doit abandonner un pays qui veut à la fois un change stable et la libre circulation des capitaux ?',
  'Son autonomie monétaire : il doit aligner ses taux sur ceux du pays de référence.',
  x='C’est le prix d’un ancrage crédible : la banque centrale ne peut plus répondre à la conjoncture intérieure.',
  t='mec', b=180)

c('Quel pays le cours cite-t-il comme exemple d’un contrôle des capitaux assumé ?',
  'La Chine, qui a longtemps limité la libre circulation des capitaux.',
  x='Ce choix lui permettait de conserver à la fois un change stable et une politique monétaire autonome.',
  t='fait', b=182)

c('Dans quel contexte le Bitcoin a-t-il été créé, et par qui ?',
  'En 2008, après la crise financière, par une personne ou un groupe signant Satoshi Nakamoto.',
  x='L’objectif affiché était de se passer des banques et des États pour effectuer des transactions.',
  t='fait', b=185)

c('Qu’est-ce que la blockchain ?',
  'Un registre numérique décentralisé où les transactions sont enregistrées et vérifiées par les utilisateurs, sans autorité centrale.',
  x='C’est cette vérification distribuée qui remplace la confiance accordée ailleurs à une banque ou à un État.',
  t='def', b=187)

c('À combien d’unités la masse de bitcoins est-elle plafonnée ?',
  'Vingt et un millions, dont environ 19,8 millions déjà émis.',
  x='Cette masse fixe l’oppose radicalement à une monnaie classique, dont la banque centrale peut ajuster la quantité.',
  t='fait', b=189)

c('Pourquoi le Bitcoin est-il qualifié de crypto-actif plutôt que de monnaie ?',
  'Parce qu’il ne remplit pas les fonctions d’unité de compte ni de moyen d’échange : aucun prix n’est fixé en bitcoins et peu d’acteurs l’acceptent.',
  x='Il ne subsiste que la fonction de réserve de valeur, et elle-même reste très incertaine du fait de la volatilité.',
  t='mec', b=196)

c('Pourquoi dit-on que le Bitcoin n’a pas de valeur sous-jacente ?',
  'Aucun État ne le garantit, aucune banque centrale ne le soutient, et il ne produit ni intérêt ni dividende.',
  x='Son cours ne dépend donc que de l’offre et de la demande : on l’achète dans l’espoir de le revendre plus cher.',
  t='mec', b=200)

c('Qu’est-ce qu’un risque systémique ?',
  'Un événement capable d’affecter l’ensemble du système financier, comme la faillite d’une grande banque ou un krach boursier.',
  x='Le critère n’est pas la taille de la perte initiale, mais la capacité du choc à se propager par contagion.',
  t='def', b=204)

c('Le Bitcoin fait-il aujourd’hui courir un risque systémique ?',
  'Non : son marché reste étroit, isolé du système monétaire classique, et les banques y sont peu exposées.',
  x='La réponse changerait s’il était massivement adopté par les banques, les États ou les grandes entreprises.',
  t='mec', b=206)

c('Quel était le projet de John Law en 1716 ?',
  'Remplacer la monnaie métallique par des billets de banque pour relancer une économie française ruinée et à court d’or.',
  x='Sa Banque Générale émet des billets convertibles en or, puis devient Banque Royale en 1718, garantie par l’État.',
  t='fait', b=213)

c('Par quel enchaînement le système de Law produisait-il une création monétaire sans limite ?',
  'La banque émettait des billets, l’État remboursait ses dettes, les porteurs achetaient des actions de la Compagnie du Mississippi, et l’argent revenait à la banque qui émettait de nouveau.',
  x='Le cours de l’action passe de 150 à 4 100 livres : c’est la première grande bulle spéculative moderne.',
  t='mec', b=217)

c('Comment le système de Law s’est-il effondré, et avec quelles conséquences durables ?',
  'En 1720, les porteurs ont voulu convertir leurs billets en or ; faute de réserves, la panique a ruiné les épargnants.',
  x='L’épisode a nourri une méfiance française durable envers les banques et le papier-monnaie, et un retour prolongé au métal.',
  t='fait', b=218)

c('Comment Schumpeter juge-t-il l’apport de John Law ?',
  'Il y voit à la fois un monétariste et un précurseur de Keynes.',
  x='Monétariste par l’attention portée à la quantité de monnaie, pré-keynésien par l’idée que le crédit peut relancer l’activité.',
  t='aut', b=222)

c('Qu’imposait la loi bancaire de 1945 aux banques de dépôt ?',
  'De travailler sur des échéances inférieures à deux ans.',
  x='Leur rôle était d’assurer la liquidité du système, non de financer des projets longs comme des usines ou des infrastructures.',
  t='fait', b=226)

c('Qu’est-ce qu’une banque universelle ?',
  'Une banque qui exerce toutes les activités à la fois : dépôt, crédit et investissement.',
  x='Né en Allemagne au XIXᵉ siècle, le modèle s’est généralisé en France dans les années 1980 pour sa souplesse et sa rentabilité.',
  t='def', b=228)

c('Quel risque le modèle de la banque universelle fait-il courir ?',
  'Un risque de liquidité : elle finance des engagements longs avec des ressources courtes comme les dépôts.',
  x='Si les déposants retirent massivement, la banque ne peut récupérer les fonds prêtés — d’où les propositions de séparation des activités après 2008.',
  t='mec', b=231)

c('Dans quelles situations une banque de second rang crée-t-elle de la monnaie ?',
  'Lorsqu’elle accorde un crédit, lorsqu’elle convertit des devises d’un exportateur, et lorsqu’elle achète des obligations d’État.',
  x='Dans les trois cas elle inscrit une somme au passif en acquérant un actif, sans mobiliser de ressources préexistantes.',
  t='mec', b=234)

c('Que signifie la formule « les crédits font les dépôts » ?',
  'La banque n’a pas besoin de dépôts préalables pour prêter : elle crée simultanément le crédit et le dépôt qui lui correspond.',
  x='L’ordre habituellement imaginé est donc inversé : ce sont les prêts qui engendrent les dépôts, et non l’inverse.',
  t='mec', b=241)

c('Qu’est-ce que la monétisation d’une créance ?',
  'La transformation d’une promesse de remboursement en moyens de paiement immédiatement utilisables.',
  x='C’est la définition exacte de la création monétaire : une dette devient de la monnaie disponible sur un compte.',
  t='def', b=248)

c('Quelles sont les trois contreparties de la masse monétaire ?',
  'Les créances sur l’économie, les créances sur l’étranger et les créances sur le Trésor public.',
  x='À chaque euro créé correspond un actif détenu par la banque : la monnaie n’apparaît jamais sans contrepartie.',
  t='mec', b=254)

c('Qu’explique le mécanisme du multiplicateur de crédit ?',
  'Comment une base monétaire limitée engendre une quantité bien plus grande de monnaie scripturale par vagues de prêts successifs.',
  x='Chaque banque reprête ce que les clients n’ont pas retiré en billets, et le processus se répète en suite géométrique.',
  t='mec', b=260)

c('Avec un taux de retrait en billets de 20 %, que devient un crédit initial de 100 ?',
  'Il engendre au total 500 de monnaie : la suite 100, 80, 64, 51,2 converge vers un multiplicateur de 5.',
  x='Le multiplicateur est l’inverse du taux de fuite : plus les agents conservent de billets, moins la création se démultiplie.',
  t='form', b=264)

c('Que signifie l’idée d’une monnaie exogène ?',
  'Sa quantité est décidée de l’extérieur de l’économie, par la banque centrale, et non par la demande de crédit.',
  x='C’est la logique du multiplicateur : la banque centrale pilote la base monétaire, les banques en déduisent ce qu’elles peuvent prêter.',
  t='def', b=270)

c('Qu’énonce le principe du diviseur de crédit ?',
  'Les banques prêtent d’abord selon la demande, puis se refinancent ensuite auprès de la banque centrale.',
  x='La création monétaire devient endogène : l’offre de monnaie s’adapte à la demande de crédit de l’économie.',
  t='mec', b=272)

c('Pourquoi la banque centrale fournit-elle presque toujours la monnaie centrale demandée par les banques ?',
  'Parce qu’elle doit garantir la stabilité du système et le financement de l’économie.',
  x='Refuser le refinancement reviendrait à provoquer la crise de liquidité qu’elle a précisément pour mission d’éviter.',
  t='mec', b=277)

c('Qu’opposait au XIXᵉ siècle la Banking School à la Currency School ?',
  'La première voulait une émission de billets ajustée aux besoins du commerce, la seconde une couverture stricte par l’or.',
  x='On rattache la Banking School à la monnaie endogène de Keynes, la Currency School à la monnaie exogène des monétaristes.',
  t='aut', b=283)

c('Que signifie l’affirmation selon laquelle « la monnaie n’est qu’un voile » ?',
  'Elle facilite les échanges sans créer de richesse ni modifier la production : son effet se limite au niveau des prix.',
  x='C’est la position classique puis monétariste, qui sépare nettement la sphère monétaire de la sphère réelle.',
  t='mec', b=292)

c('Qu’observe Jean Bodin au XVIᵉ siècle à propos de la quantité de monnaie ?',
  'Qu’un afflux de monnaie provoque une hausse des prix sans accroître la production.',
  x='Il tire ce constat de l’arrivée des métaux précieux d’Amérique : c’est la première formulation de l’idée quantitative.',
  t='aut', b=294)

c('Qu’énonce la loi de Say ?',
  '« L’offre crée sa propre demande » : ce sont les produits qui s’échangent contre des produits.',
  x='La monnaie n’est qu’un intermédiaire technique : elle ne peut donc pas être à l’origine d’une insuffisance de débouchés.',
  t='aut', b=296)

c('Quelle thèse David Ricardo soutient-il sur les effets d’une hausse de la quantité de monnaie ?',
  'Elle élève les prix, sans modifier ni la production ni l’emploi.',
  x='Cette position strictement quantitative fonde la neutralité de la monnaie, que Fisher formalisera ensuite.',
  t='aut', b=298)

c('Quelle équation Irving Fisher formule-t-il, et que signifient ses termes ?',
  'MV = PT : quantité de monnaie, vitesse de circulation, niveau général des prix, volume des transactions.',
  x='En supposant V et T stables, toute hausse de M se traduit proportionnellement par une hausse de P.',
  t='form', b=304)

c('Quelle conclusion Fisher tire-t-il de son équation sur la nature de l’inflation ?',
  'Qu’elle est un phénomène purement monétaire.',
  x='La conséquence pratique est nette : pour agir sur les prix, il faut agir sur la quantité de monnaie, et sur rien d’autre.',
  t='aut', b=307)

c('Quelles sont les trois propositions de Friedman dans sa reformulation de la théorie quantitative en 1956 ?',
  'La monnaie est exogène, l’inflation est toujours un phénomène monétaire, et à long terme la monnaie est neutre.',
  x='Il appuie ces thèses sur une relation statistiquement stable entre les agrégats monétaires et le niveau des prix.',
  t='aut', b=310)

c('Qu’est-ce qu’une anticipation adaptative chez Friedman ?',
  'Les agents forment leurs prévisions à partir de l’inflation passée et ajustent peu à peu leurs comportements.',
  x='Les salariés réclament des hausses, les entreprises relèvent leurs prix : l’effet réel de la politique monétaire s’évanouit.',
  t='def', b=314)

c('Par quel enchaînement une politique monétaire expansionniste agit-elle à court terme ?',
  'Baisse des taux, crédit plus accessible, hausse de l’investissement et de la consommation, donc hausse de la production et recul du chômage.',
  x='Friedman admet cet effet, mais le juge instable parce que les agents finissent par voir qu’il s’agit d’inflation.',
  t='mec', b=319)

c('Pourquoi Friedman tient-il l’effet de la monnaie sur l’économie réelle pour instable ?',
  'Parce que les agents révisent leurs anticipations : la production revient à son niveau initial et seule l’inflation subsiste.',
  x='L’effet n’est donc ni durable ni prévisible, ce qui rend toute politique monétaire conjoncturelle inopérante.',
  t='mec', b=322)

c('Qu’observe Alban Phillips en 1958, et sur quelles données ?',
  'Une relation inverse entre la croissance des salaires nominaux et le chômage, au Royaume-Uni entre 1861 et 1957.',
  x='Il en déduit l’existence d’un taux de chômage pour lequel la hausse des salaires nominaux est nulle : le NAWRU.',
  t='aut', b=333)

c('Quelle lecture les keynésiens tirent-ils de la courbe de Phillips ?',
  'Qu’une inflation modérée fait baisser le chômage, car elle réduit le salaire réel et incite les entreprises à embaucher.',
  x='Samuelson et Solow confirment la relation aux États-Unis, ce qui en fait un instrument de politique dans les années 1960.',
  t='aut', b=334)

c('Qu’est-ce que l’illusion monétaire ?',
  'Le fait que les salariés ne perçoivent pas immédiatement la baisse de leur salaire réel quand les prix montent.',
  x='C’est elle, selon Friedman, qui explique que la courbe de Phillips fonctionne à court terme — et seulement à court terme.',
  t='def', b=345)

c('Pourquoi la courbe de Phillips devient-elle verticale à long terme selon Friedman ?',
  'Parce que l’illusion monétaire se dissipe : les salariés obtiennent des hausses nominales et le chômage revient à son niveau naturel.',
  x='Aucun arbitrage durable entre inflation et chômage n’est donc possible : seul le taux d’inflation s’élève.',
  t='mec', b=353)

c('Qu’est-ce que la stagflation, et pourquoi a-t-elle discrédité la courbe de Phillips ?',
  'La coexistence d’une production stagnante et d’une forte inflation, observée après le choc pétrolier.',
  x='Inflation et chômage élevés ensemble : le fait contredit directement la relation inverse que la courbe postulait.',
  t='mec', b=368)

c('Quelles sont les deux recommandations de Friedman en matière monétaire ?',
  'Laisser le chômage revenir à son niveau naturel et faire croître la masse monétaire à un rythme constant.',
  x='C’est la règle de k % : une progression fixe et annoncée, qui retire toute marge discrétionnaire à la banque centrale.',
  t='aut', b=385)

c('Comment résumer la position de Friedman sur le pouvoir de la monnaie ?',
  'La monnaie est toute-puissante puisqu’elle détermine l’inflation ; la politique monétaire est impuissante puisque les agents anticipent.',
  x='Le paradoxe n’en est pas un : c’est précisément parce que les agents anticipent que seul le niveau des prix bouge.',
  t='aut', b=389)

c('En quoi consiste l’hélicoptère monétaire ?',
  'Créer de la monnaie et la verser directement aux ménages ou à l’État, sans passer par les banques commerciales.',
  x='À la différence du quantitative easing, elle n’alimente pas le système bancaire mais directement la demande.',
  t='def', b=394)

c('Quel blocage l’hélicoptère monétaire cherche-t-il à contourner ?',
  'La trappe à liquidité : même avec des taux très bas, les banques ne prêtent pas et les agents n’investissent pas.',
  x='Injecter la monnaie dans le circuit bancaire ne sert alors à rien : il faut atteindre directement la dépense.',
  t='mec', b=399)

c('Pourquoi l’hélicoptère monétaire brouille-t-il la frontière entre politique monétaire et politique budgétaire ?',
  'Parce que décider qui reçoit combien, ou financer une dépense publique, relève d’un choix politique et non monétaire.',
  x='Financer directement l’État revient à monétiser la dette, ce que les traités européens interdisent à la BCE.',
  t='mec', b=425)

c('Quel aléa moral public l’hélicoptère monétaire fait-il naître ?',
  'Si l’État sait que la banque centrale financera ses dépenses, il perd toute incitation à maîtriser son déficit et sa dette.',
  x='S’y ajoute la perte de crédibilité de la banque centrale, devenue un instrument du gouvernement.',
  t='mec', b=445)

c('Quelle chaîne relie les taux directeurs à l’inflation ?',
  'Taux directeurs, conditions du crédit, création monétaire, demande globale, puis inflation et activité.',
  x='La politique monétaire ne fixe donc pas un prix isolé : elle encadre la circulation de la monnaie dans toute l’économie.',
  t='mec', b=459)

c('Par quel enchaînement un crédit trop dynamique produit-il de l’inflation ?',
  'La masse monétaire progresse, la demande s’élève plus vite que l’offre, et des tensions apparaissent sur les prix.',
  x='Ce n’est pas la création monétaire en soi qui est en cause, mais son écart avec la croissance de la production.',
  t='mec', b=467)

c('Quelle cible d’inflation la BCE vise-t-elle, et à quel horizon ?',
  'Environ 2 % à moyen terme.',
  x='L’horizon moyen terme compte autant que le chiffre : il autorise des écarts passagers sans réaction immédiate.',
  t='fait', b=472)

c('Par quel enchaînement une baisse des taux directeurs soutient-elle la croissance ?',
  'Le crédit devient moins cher, l’investissement et la consommation progressent, la demande globale s’élève.',
  x='C’est exactement le canal qui, poussé trop loin, nourrit l’inflation : d’où le dilemme permanent de la banque centrale.',
  t='mec', b=478)

c('Quels risques la banque centrale cherche-t-elle à écarter au titre de la stabilité financière ?',
  'Les crises bancaires, les paniques de liquidité, le blocage du crédit, les faillites systémiques et les emballements spéculatifs.',
  x='Cet objectif s’est imposé après 2008 : la banque centrale n’est plus seulement une institution anti-inflation.',
  t='mec', b=489)

c('Quelles missions nouvelles Éric Monnet assigne-t-il aux banques centrales dans La Banque Providence (2021) ?',
  'Accompagner la transition écologique, émettre une monnaie numérique de banque centrale et intervenir dans la gestion de la dette publique.',
  x='Son mot d’ordre est de démocratiser les banques centrales : elles deviennent des acteurs de la gouvernance économique.',
  t='aut', b=511)

c('Que soutient la théorie monétaire moderne reprise par Stephanie Kelton dans Le mythe du déficit (2021) ?',
  'Un État souverain monétairement n’a pas de contrainte financière à sa dépense, puisqu’il peut créer la monnaie.',
  x='La seule limite est réelle : le pays doit disposer de la main-d’œuvre et des capacités de production, sans quoi l’inflation apparaît.',
  t='aut', b=515)

c('À quel économiste des années 1940 la théorie monétaire moderne emprunte-t-elle ses fondements ?',
  'Abba Lerner, en 1943.',
  x='Il défendait que l’État se mette au service de la prospérité, la question de la dette publique restant secondaire.',
  t='aut', b=517)

c('Qu’est-ce que le taux de facilité de dépôt, et quel rôle joue-t-il ?',
  'Le taux auquel les banques placent leurs liquidités auprès de la banque centrale ; il constitue le taux plancher.',
  x='S’il est élevé, les banques préfèrent déposer leurs fonds plutôt que de prêter : le crédit se contracte.',
  t='def', b=537)

c('Qu’est-ce que le taux de facilité de prêt marginal ?',
  'Le taux auquel les banques empruntent à très court terme auprès de la banque centrale ; il constitue le taux plafond.',
  x='Il borne le coût du refinancement : aucune banque n’empruntera plus cher ailleurs sur le marché interbancaire.',
  t='def', b=542)

c('Qu’est-ce que le taux de refinancement de la banque centrale ?',
  'Le taux des opérations de crédit à une semaine ; c’est le principal signal monétaire envoyé au marché.',
  x='Les deux facilités, de dépôt et de prêt, l’encadrent : c’est le corridor des taux directeurs.',
  t='def', b=548)

c('Qu’appelle-t-on le corridor des taux directeurs, et à quoi sert-il ?',
  'L’intervalle entre la facilité de dépôt et la facilité de prêt, dans lequel évoluent les taux du marché interbancaire.',
  x='Il oriente les échanges de liquidités entre banques et assure la transmission de la politique monétaire.',
  t='def', b=552)

c('Quel taux de référence a remplacé l’EONIA dans la zone euro ?',
  'L’€STR.',
  x='Il mesure le coût réel auquel les banques se prêtent des liquidités au jour le jour sur le marché interbancaire.',
  t='fait', b=563)

c('Par quel enchaînement une baisse des taux directeurs se transmet-elle au crédit ?',
  'L’€STR recule, le refinancement des banques coûte moins cher, les taux débiteurs baissent, la demande de crédit augmente.',
  x='Le marché interbancaire est donc le premier relais : sans lui, la décision de la banque centrale reste sans effet.',
  t='mec', b=567)

c('Comment agit le canal du prix des actifs ?',
  'Une baisse des taux renchérit les obligations déjà émises ; leurs détenteurs se sentent plus riches et dépensent davantage.',
  x='C’est un effet richesse, proche de l’effet Pigou, qui joue symétriquement à la hausse comme à la baisse.',
  t='mec', b=594)

c('Qu’est-ce que la forward guidance ?',
  'L’annonce par la banque centrale de l’orientation future probable de ses taux et de sa stratégie.',
  x='Elle agit sur les anticipations : rassurer les marchés et ancrer l’inflation attendue devient un instrument à part entière.',
  t='def', b=604)

c('Comment la politique monétaire agit-elle par le canal du taux de change ?',
  'Une hausse des taux attire les capitaux étrangers, la monnaie s’apprécie et les exportations perdent en compétitivité.',
  x='La baisse produit l’effet inverse : c’est pourquoi une politique monétaire a toujours des effets internationaux.',
  t='mec', b=615)

c('Qu’est-ce que la trappe à liquidité ?',
  'La situation où les taux sont déjà très bas, les agents préfèrent conserver des liquidités et l’investissement ne repart pas.',
  x='Baisser encore les taux n’a plus d’effet : la politique monétaire conventionnelle perd sa prise sur l’économie.',
  t='def', b=638)

c('Quels objectifs les politiques monétaires non conventionnelles poursuivent-elles ?',
  'Rétablir la liquidité, débloquer le crédit, éviter la déflation, stabiliser les marchés et soutenir l’activité.',
  x='Elles n’agissent plus sur le prix de la monnaie, mais directement sur les bilans, les titres et les anticipations.',
  t='mec', b=648)

c('En quoi consiste le quantitative easing, et quel effet a-t-il sur le bilan de la banque centrale ?',
  'Des achats massifs de titres publics et privés, qui augmentent la taille de son bilan.',
  x='Il injecte de la liquidité, fait monter le prix des titres et abaisse les taux à moyen et long terme.',
  t='def', b=656)

c('Qu’est-ce qui distingue le qualitative easing du quantitative easing ?',
  'Le premier modifie la composition du bilan de la banque centrale, le second sa taille.',
  x='Elle acquiert des actifs plus risqués et élargit les garanties acceptées, sans forcément créer plus de monnaie.',
  t='dist', b=669)

c('Pourquoi certaines banques centrales ont-elles pratiqué des taux négatifs ?',
  'Pour dissuader les banques de laisser dormir leurs liquidités et les pousser à prêter davantage.',
  x='La mesure vise la facilité de dépôt, donc les banques, et non directement les ménages.',
  t='mec', b=678)

c('Quelle est la différence entre un financement intermédié et un financement direct ?',
  'Le premier passe par les banques, le second par l’émission et l’échange de titres sur les marchés.',
  x='L’opposition entre économie d’endettement et économie de marchés financiers repose sur cette distinction.',
  t='dist', b=687)

c('Pourquoi l’opposition entre économie d’endettement et économie de marchés doit-elle être nuancée aujourd’hui ?',
  'Parce que les banques restent centrales tout en intervenant elles-mêmes massivement sur les marchés.',
  x='Le basculement n’a donc pas évincé les banques : il a financiarisé leur activité.',
  t='mec', b=693)

c('Quelle est la différence entre le revenu d’une obligation et celui d’une action ?',
  'L’obligation procure un revenu fixe sous forme d’intérêts ; l’action procure un dividende variable selon les résultats.',
  x='Le rendement fixe a pour contrepartie l’absence de droit sur les bénéfices ; le dividende, l’absence de garantie.',
  t='dist', b=699)

c('Que signifie spéculer à la baisse, et par quels instruments ?',
  'Parier sur la chute future d’un actif, par la vente à découvert, les marchés à terme ou les produits dérivés.',
  x='Le marché ne sert donc pas qu’à financer : il permet aussi d’arbitrer, de se couvrir et de spéculer.',
  t='def', b=712)

c('Qu’est-ce qui distingue le marché au comptant du marché à terme ?',
  'Au comptant, paiement et livraison sont immédiats ; à terme, l’opération est conclue aujourd’hui et exécutée plus tard.',
  x='Le marché à terme sert à se couvrir contre le risque, mais c’est aussi le terrain privilégié de la spéculation.',
  t='dist', b=730)

c('Qu’est-ce qu’un marché de gré à gré ?',
  'Un marché non centralisé, où la négociation est bilatérale et sans place boursière organisée.',
  x='Souplesse accrue, transparence moindre : les marchés OTC concentrent une part importante du risque systémique.',
  t='def', b=740)

c('Que permet le service de règlement différé, et quel en est l’intérêt ?',
  'Il permet de différer le règlement d’une opération boursière, donc de prendre position sans payer immédiatement.',
  x='Il procure un effet de levier, et révèle une logique de marché tournée vers l’anticipation et la spéculation.',
  t='def', b=749)

c('Quelles sont les cinq fonctions de la Bourse ?',
  'Permettre l’émission de titres, organiser leur cotation, assurer leur liquidité, faire se rencontrer offreurs et demandeurs de capitaux, et fournir une information de prix.',
  x='La liquidité est la clé : c’est elle qui transforme un titre en actif facilement négociable.',
  t='mec', b=760)

c('Quand la Bourse de Paris a-t-elle été créée, et dans quel ensemble s’est-elle fondue ?',
  'Créée en 1724, elle est intégrée à Euronext à partir de 2000.',
  x='Lisbonne, le LIFFE londonien et Athènes rejoignent l’ensemble en 2002 : concentration et internationalisation vont de pair.',
  t='fait', b=768)

c('Quelles conditions une entreprise doit-elle remplir pour être cotée en Bourse ?',
  'Être généralement une société anonyme, publier une information financière transparente et accepter la surveillance des marchés.',
  x='Ces obligations sont la contrepartie de l’accès à l’épargne publique.',
  t='mec', b=774)

c('Quelle évolution John Hicks décrit-il dans le financement des économies ?',
  'Le passage d’une économie d’endettement, dominée par le crédit bancaire, à une économie de marchés financiers.',
  x='L’intermédiation bancaire y cède du terrain à l’émission de titres et au rôle croissant des investisseurs.',
  t='aut', b=782)

c('Qu’appelle-t-on intermédiation de marché ?',
  'La situation où les banques restent centrales mais interviennent elles-mêmes de plus en plus par les marchés.',
  x='Elles prêtent toujours, mais achètent aussi des titres, titrisent et gèrent des portefeuilles.',
  t='def', b=803)

c('Que désigne la règle des 3D formulée par Henri Bourguinat en 1987 ?',
  'La décloisonnement des marchés, la déréglementation et la désintermédiation.',
  x='Dans Les vertiges de la finance internationale, elle résume la transformation des marchés depuis les années 1980.',
  t='aut', b=820)

c('Qu’est-ce que le shadow banking system ?',
  'L’ensemble des activités de financement menées en dehors du système bancaire traditionnel ou à sa périphérie.',
  x='Fonds monétaires et véhicules de titrisation y créent de la liquidité et transforment les maturités sans les mêmes règles prudentielles.',
  t='def', b=833)

c('Qu’est-ce qu’un CDO ?',
  'Un titre construit à partir d’un panier de dettes regroupées — crédits immobiliers, prêts bancaires — puis revendu à des investisseurs.',
  x='Il mélange des créances de qualités très différentes, ce qui rend le risque réel difficile à lire.',
  t='def', b=848)

c('Pourquoi les CDO ont-ils amplifié la crise de 2008 ?',
  'Leur opacité masquait la qualité des créances, et leur diffusion mondiale a dispersé le risque sur tous les marchés.',
  x='Quand les défauts sur les subprimes se sont multipliés, la contagion a été immédiate et internationale.',
  t='mec', b=859)

c('Qu’est-ce qu’un CDS ?',
  'Un produit dérivé qui fonctionne comme une assurance : moyennant une prime, le détenteur est indemnisé si l’emprunteur fait défaut.',
  x='Son principe est sain ; c’est son usage spéculatif qui pose problème.',
  t='def', b=863)

c('Pourquoi les CDS sont-ils devenus un facteur de risque systémique ?',
  'On peut en acheter sans détenir la créance, donc parier sur une faillite — et le vendeur peut lui-même être incapable d’indemniser.',
  x='En 2008, c’est précisément cette chaîne d’engagements croisés qui a rendu certains acteurs très fragiles.',
  t='mec', b=872)

c('En quoi consiste la titrisation ?',
  'Une banque regroupe des créances, les cède à un véhicule financier qui émet des titres vendus à des investisseurs.',
  x='Elle sort les créances du bilan, récupère des liquidités et transfère le risque, ce qui lui permet de prêter de nouveau.',
  t='def', b=884)

c('Quel risque la titrisation fait-elle courir ?',
  'Elle dilue la responsabilité et rend les risques moins lisibles, ce qui favorise la formation de bulles.',
  x='Une banque qui ne porte plus le risque de ses crédits a moins d’intérêt à vérifier la solvabilité de l’emprunteur.',
  t='mec', b=898)

c('Que désigne l’expression « too big to fail » ?',
  'Des institutions financières assez grandes et centrales pour que leur faillite menace tout le système.',
  x='Elles sont perçues comme implicitement protégées, ce qui les incite à prendre davantage de risques.',
  t='def', b=902)

c('Quels sont les trois problèmes posés par les institutions « too big to fail » ?',
  'Le risque systémique, l’aléa moral et la socialisation des pertes.',
  x='Les profits restent privés quand les pertes sont supportées par les banques centrales, les États, donc la collectivité.',
  t='mec', b=910)
