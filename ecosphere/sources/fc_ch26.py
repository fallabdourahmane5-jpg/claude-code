# -*- coding: utf-8 -*-
"""Deuxième année — chapitre 6 (ch. 26) : taux de change et systèmes de change."""
from fc_base import lot, c

L = lot(26)

c('Qu’est-ce qu’une devise, et en quoi se distingue-t-elle de la monnaie ?',
  'Une devise est une monnaie étrangère considérée du point de vue d’un agent ou d’un pays : ce n’est pas une catégorie monétaire distincte.',
  x='Une même unité monétaire est donc monnaie nationale ici et devise ailleurs.',
  t='def', b=66)

c('Que signifie le pouvoir libératoire de la monnaie ?',
  'Qu’elle permet de régler une dette dans les conditions prévues par le droit en vigueur.',
  x='La monnaie remplit trois fonctions : moyen d’échange, unité de compte et réserve de valeur.',
  t='def', b=54)

c('Quelle distinction la convertibilité impose-t-elle d’opérer ?',
  'Entre la convertibilité pour les transactions courantes et celle pour les opérations financières et les mouvements de capitaux.',
  x='Une monnaie peut donc être convertible pour les paiements commerciaux sans l’être librement pour toutes les opérations financières.',
  t='dist', b=100)

c('Pourquoi certains États restreignent-ils la convertibilité de leur monnaie ?',
  'Parce qu’une sortie massive de capitaux ferait monter la demande de devises, pèserait sur la monnaie nationale et fragiliserait les réserves de change.',
  x='Contrôles des capitaux, autorisations administratives, limites d’achat de devises en sont les instruments.',
  t='mec', b=95)

c('Qu’est-ce qu’une monnaie véhiculaire ?',
  'Une monnaie servant d’intermédiaire dans les échanges internationaux, y compris entre deux pays dont ce n’est pas la monnaie nationale.',
  x='Une entreprise européenne et une entreprise asiatique peuvent ainsi facturer en dollars.',
  t='def', b=117)

c('Sur quoi repose la position centrale du dollar dans le système monétaire international ?',
  'Sur la complémentarité de ses fonctions d’intermédiaire des échanges, d’unité de compte et de réserve de valeur, soutenues par des marchés profonds et des effets de réseau.',
  x='Plus une monnaie est utilisée, plus il est avantageux de continuer à l’utiliser : le mécanisme est cumulatif.',
  t='mec', b=123)

c('Pourquoi les banques centrales détiennent-elles principalement des réserves en dollars ?',
  'Parce que les actifs libellés en dollars, notamment les titres du Trésor américain, bénéficient de marchés profonds et liquides, mobilisables rapidement.',
  x='Les réserves prennent la forme de dépôts en devises, de titres étrangers ou d’autres actifs de réserve.',
  t='mec', b=136)

c('Qu’est-ce que le taux de change nominal bilatéral ?',
  'Le prix d’une monnaie exprimé dans une autre, par exemple 1 € = 1,20 USD.',
  x='Nominal parce qu’il ne corrige pas les différences de niveaux de prix, bilatéral parce qu’il ne concerne que deux monnaies.',
  t='def', b=153)

c('Qu’est-ce qui distingue cotation au certain et cotation à l’incertain ?',
  'La première exprime une unité de monnaie nationale en devises étrangères, la seconde une unité de devise étrangère en monnaie nationale.',
  x='En cotation au certain, un chiffre qui augmente signifie une appréciation de la monnaie nationale.',
  t='dist', b=163)

c('Que mesure le taux de change effectif nominal ?',
  'La valeur d’une monnaie face à un panier de devises, chacune pondérée par son poids dans les échanges commerciaux du pays.',
  x='Une monnaie peut s’apprécier face au dollar tout en se dépréciant face au yuan : la seule parité bilatérale ne suffit pas.',
  t='def', b=185)

c('Que mesure le taux de change réel, et quelle limite du taux nominal corrige-t-il ?',
  'Le prix relatif des biens domestiques par rapport aux biens étrangers, en intégrant les niveaux de prix.',
  x='Une monnaie stable peut masquer une dégradation de la compétitivité-prix si les prix intérieurs montent plus vite que ceux des partenaires.',
  t='def', b=211)

c('Quel vocabulaire distingue les mouvements de change selon le régime ?',
  'Appréciation et dépréciation pour les mouvements de marché en régime flottant ; réévaluation et dévaluation pour les modifications officielles de parité en changes fixes.',
  x='Il faut aussi distinguer le niveau du taux à une date donnée et son évolution dans le temps.',
  t='dist', b=232)

c('Qu’est-ce que la volatilité du taux de change, et pourquoi importe-t-elle aux entreprises ?',
  'L’ampleur des variations autour de sa trajectoire : elle accroît l’incertitude pour les agents exposés au risque de change.',
  x='Une entreprise devant régler un million de dollars dans six mois voit son coût en euros augmenter si le dollar s’apprécie.',
  t='def', b=243)

c('Qu’est-ce que le marché des changes ?',
  'Le Forex, marché sur lequel s’échangent les monnaies et dont la confrontation des offres et des demandes fait résulter un taux de change.',
  x='En régime flottant, ce taux est donc un prix de marché.',
  t='def', b=281)

c('Par quels moyens une banque centrale défend-elle une parité fixe ?',
  'En achetant ou vendant des devises, en mobilisant ses réserves de change, en modifiant ses taux d’intérêt ou en imposant des restrictions financières.',
  x='Le taux ne résulte alors pas de la seule confrontation des offres et demandes privées.',
  t='fait', b=301)

c('Pourquoi Dominique Plihon qualifie-t-il le Forex de « marché-réseau » ?',
  'Parce qu’il ne repose sur aucune place physique unique : les transactions passent par des réseaux électroniques et des intermédiaires spécialisés.',
  x='Référence : 2017. Cette dématérialisation lui donne une dimension véritablement mondiale.',
  t='aut', b=314)

c('Comment le Forex fonctionne-t-il pratiquement en continu ?',
  'Les grandes places — Londres, New York, Tokyo, Singapour, Hong Kong — se succèdent au fil des fuseaux horaires pendant les jours ouvrés.',
  x='Cette continuité favorise la circulation rapide de l’information et la réactivité des cours.',
  t='fait', b=321)

c('Comment l’arbitrage réduit-il les écarts de cotation entre places financières ?',
  'En achetant la devise là où elle est moins chère pour la revendre là où elle l’est plus, l’opérateur fait converger les deux cotations.',
  x='De faibles écarts subsistent, liés aux coûts de transaction et à la liquidité.',
  t='mec', b=337)

c('Dans quelle proportion des transactions de change le dollar intervient-il en 2025 ?',
  'Dans 89,2 % des transactions recensées.',
  x='Cette domination tient à ses fonctions internationales et à l’organisation financière du marché.',
  t='fait', b=351)

c('Pourquoi dit-on que le Forex est un marché de gros ?',
  'Parce que les transactions professionnelles portent sur des montants très élevés ; les opérations des ménages passent par des intermédiaires qui agrègent et compensent les besoins.',
  x='Cela explique le poids considérable des banques dans les transactions de change.',
  t='mec', b=357)

c('Comment le volume quotidien des transactions de change a-t-il évolué depuis 1992 ?',
  'D’environ 880 milliards de dollars par jour en 1992 à près de 9 600 milliards en 2025, soit une multiplication par onze environ.',
  x='Le commerce international ne suffit pas à expliquer cette progression : elle traduit la financiarisation de l’économie mondiale.',
  t='fait', b=395)

c('Quelles trois transformations expliquent l’expansion du marché des changes ?',
  'La mondialisation commerciale, la libéralisation des mouvements de capitaux et le développement des instruments dérivés.',
  x='Les dérivés servent à couvrir le risque de change, mais aussi à spéculer, ce qui gonfle les volumes.',
  t='fait', b=406)

c('Qu’est-ce qu’une opération de change à terme ?',
  'Un contrat fixant aujourd’hui le taux auquel des devises seront échangées à une date future.',
  x='Le taux à terme diffère du taux au comptant : il dépend des taux d’intérêt des deux monnaies, de la durée et des conditions de marché.',
  t='def', b=433)

c('Qu’est-ce qu’une option de change, et en quoi diffère-t-elle d’un contrat à terme ?',
  'Elle donne le droit, non l’obligation, d’acheter ou de vendre une devise à un taux déterminé, contre paiement d’une prime.',
  x='Le contrat à terme doit être exécuté même si le marché devient favorable ; l’option fonctionne comme une assurance.',
  t='def', b=454)

c('Qu’est-ce qu’un swap de change ?',
  'Un échange de devises à une première date, assorti de l’engagement d’un échange inverse à une date ultérieure.',
  x='Ce n’est pas une assurance mais un contrat à obligations réciproques, utilisé pour la couverture, le financement ou la liquidité.',
  t='def', b=473)

c('Comment les opérations de change se répartissent-elles par type ?',
  'Comptant 31 %, opérations à terme 19 %, swaps de change et de devises 44 %, options et autres produits 7 %.',
  x='Les opérations comportant une dimension temporelle forment donc la majorité des transactions.',
  t='fait', b=495)

c('Qu’est-ce qui distingue la couverture de la spéculation sur le marché des changes ?',
  'La couverture réduit l’incertitude liée aux variations monétaires ; la spéculation accepte une exposition dans l’espoir d’un gain.',
  x='Pour qu’un agent transfère son risque, il faut qu’un autre accepte la position correspondante : intermédiaires et spéculateurs y pourvoient.',
  t='dist', b=517)

c('Qu’appelle-t-on position ouverte sur le marché des changes ?',
  'La situation d’un agent qui conserve une exposition aux variations du taux de change.',
  x='Un investisseur anticipant une appréciation du dollar l’achète : il gagne si elle se produit, il perd sinon.',
  t='def', b=524)

c('Quand la spéculation est-elle stabilisatrice sur le marché des changes ?',
  'Quand les investisseurs jugent la variation temporaire : achetant la monnaie qui a baissé, ils corrigent la dépréciation initiale.',
  x='Ce raisonnement suppose qu’ils anticipent un retour vers un niveau d’équilibre.',
  t='mec', b=535)

c('Comment la spéculation devient-elle déstabilisatrice en période de crise ?',
  'Une dépréciation y est lue comme le début d’une chute prolongée : chacun vend pour éviter des pertes, ce qui amplifie le mouvement initial.',
  x='Le phénomène devient très puissant lorsque les anticipations influencent elles-mêmes la réalité.',
  t='mec', b=553)

c('Qu’est-ce qu’une anticipation autoréalisatrice sur le marché des changes ?',
  'Une croyance qui se vérifie par les comportements qu’elle provoque : la dépréciation attendue se produit parce qu’elle a été anticipée.',
  x='Ce mécanisme cumulatif accentue fortement la volatilité des changes.',
  t='def', b=564)

c('Quelles deux catégories de déterminants du taux de change faut-il distinguer ?',
  'Les déterminants réels — compétitivité, prix, inflation, échanges de biens — et les déterminants financiers — taux d’intérêt, rendements, mouvements de capitaux, anticipations.',
  x='Les premières théories privilégiaient les prix ; la globalisation financière a renforcé le poids des seconds.',
  t='dist', b=595)

c('Pourquoi une transaction de la balance des paiements ne provoque-t-elle pas toujours une conversion de devises ?',
  'Parce qu’une entreprise peut recevoir un paiement en dollars et les conserver sur un compte bancaire sans les convertir.',
  x='Il faut donc distinguer les transactions internationales des opérations effectives de change.',
  t='dist', b=608)

c('Pourquoi une hausse des exportations peut-elle apprécier la monnaie nationale ?',
  'Parce que les acheteurs étrangers doivent acquérir cette monnaie pour régler leurs achats, lorsque les ventes sont facturées dans la monnaie de l’exportateur.',
  x='Si la facturation est en dollars, l’effet dépend de la décision de convertir ou non les recettes.',
  t='mec', b=617)

c('Pourquoi un déficit commercial n’entraîne-t-il pas nécessairement une dépréciation ?',
  'Parce que les mouvements de capitaux peuvent compenser, voire dépasser, les effets des échanges commerciaux.',
  x='Des achats massifs d’obligations et d’actions par des investisseurs étrangers soutiennent la demande de monnaie nationale.',
  t='dist', b=650)

c('Que soutient la théorie de la parité des pouvoirs d’achat de Gustav Cassel en 1918 ?',
  'Qu’à long terme les taux de change tendent à refléter les écarts de prix : une même somme convertie devrait acheter des paniers comparables dans les deux pays.',
  x='Une monnaie représente un pouvoir d’achat sur les biens et services : l’écart de prix signale un déséquilibre du change.',
  t='aut', b=668)

c('Qu’énonce la loi du prix unique ?',
  'Sur des marchés parfaitement intégrés, un même bien échangeable devrait avoir le même prix exprimé dans une monnaie commune.',
  x='Les écarts créent des possibilités d’arbitrage, mais coûts de transport, taxes, réglementations et différences de qualité limitent la convergence.',
  t='def', b=677)

c('Comment s’écrit la parité des pouvoirs d’achat absolue en cotation au certain ?',
  'e = P* / P, où P est le prix du panier domestique en monnaie nationale et P* celui du panier étranger en devise.',
  x='Avec un panier à 100 € et 120 dollars, le taux théorique est 1 € = 1,20 USD.',
  t='form', b=699)

c('Comment juge-t-on qu’une monnaie est surévaluée au regard de la PPA ?',
  'Si le taux de marché dépasse le taux de PPA : à 1 € = 1,40 USD alors que la PPA donne 1,20, le panier européen coûte 140 dollars contre 120 aux États-Unis.',
  x='Une surévaluation par rapport à la PPA ne signifie pas une surévaluation au regard de tous les autres critères.',
  t='mec', b=721)

c('Qu’affirme la PPA relative ?',
  'Que les variations du taux de change compensent à long terme les écarts d’inflation entre pays.',
  x='Avec 6 % d’inflation dans la zone euro contre 2 % aux États-Unis, l’euro devrait se déprécier d’environ 4 % face au dollar.',
  t='def', b=743)

c('Pourquoi les coûts de transaction empêchent-ils l’égalisation parfaite des prix ?',
  'Parce qu’un écart inférieur au coût du transport, des droits de douane ou de l’assurance ne rend pas l’arbitrage rentable.',
  x='Un écart de 5 € ne déclenche aucun arbitrage si le transport coûte 10 €.',
  t='mec', b=775)

c('Pourquoi les biens non échangeables limitent-ils la portée de la PPA ?',
  'Parce que leur prix dépend des conditions nationales — salaires, coûts locaux — et qu’aucun arbitrage international ne peut les égaliser.',
  x='Services à la personne, loyers, prestations locales et services immobiliers en relèvent : une coupe de cheveux ne se déplace pas.',
  t='mec', b=793)

c('Qu’explique l’effet Balassa-Samuelson, formulé en 1964 ?',
  'Les écarts durables de niveaux de prix : une productivité élevée dans le secteur exposé y permet des salaires élevés, qui se diffusent au secteur abrité sans gain de productivité équivalent.',
  x='Les pays les plus productifs présentent donc des prix plus élevés, sans que leur monnaie soit pour autant surévaluée.',
  t='aut', b=808)

c('Pourquoi les mouvements de capitaux peuvent-ils éloigner le change de sa PPA ?',
  'Parce que des achats massifs d’actifs libellés dans une monnaie peuvent l’apprécier malgré un différentiel d’inflation défavorable.',
  x='La PPA est donc une référence de long terme plutôt qu’un instrument de prévision à court terme.',
  t='dist', b=826)

c('Qu’est-ce qui distingue un régime de change de jure d’un régime de facto ?',
  'Le premier est officiellement déclaré au FMI, le second effectivement pratiqué : un pays peut annoncer la flexibilité tout en intervenant massivement.',
  x='Le FMI observe les pratiques, classe les régimes et repère les écarts entre engagements et politiques réelles.',
  t='dist', b=876)

c('Qu’est-ce qu’un régime de change ?',
  'L’ensemble des règles déterminant la fixation et l’évolution du taux de change : qui le fixe, si la banque centrale intervient, et quelles fluctuations sont autorisées.',
  x='Ces règles permettent de classer les régimes selon leur degré de flexibilité.',
  t='def', b=883)

c('Que perd un pays qui choisit la dollarisation ?',
  'Toute politique monétaire indépendante : il ne crée plus sa monnaie et ne peut plus dévaluer pour améliorer sa compétitivité.',
  x='L’Équateur a dollarisé en 2000 ; ces choix suivent souvent une hyperinflation ou un effondrement monétaire, l’objectif étant de restaurer la confiance.',
  t='mec', b=907)

c('Quels avantages et quel renoncement une union monétaire implique-t-elle ?',
  'Elle supprime le risque de change entre membres et favorise échanges, investissements et comparaison des prix, mais interdit de corriger une perte de compétitivité par une dévaluation nationale.',
  x='Les pays partagent une même monnaie et une politique monétaire commune.',
  t='dist', b=927)

c('Qu’est-ce qu’une caisse d’émission ?',
  'Un régime où la monnaie nationale est convertible à taux fixe en une devise de référence, l’émission devant être couverte par des réserves en devises.',
  x='Hong Kong l’applique depuis 1983 avec le dollar américain ; l’Argentine a eu un régime de convertibilité de 1991 à 2002.',
  t='def', b=942)

c('Qu’est-ce qu’une bande de fluctuation, et jusqu’où le SME l’a-t-il élargie ?',
  'Une marge autorisée autour de la parité centrale, à l’intérieur de laquelle aucune intervention n’est nécessaire ; le Système monétaire européen l’a portée à ± 15 % en 1993.',
  x='Un régime officiellement fixe peut donc devenir très flexible quand les marges sont larges.',
  t='def', b=970)

c('Qu’est-ce qu’un ancrage glissant ?',
  'Un régime où la parité de référence évolue progressivement, selon une règle annoncée ou certains indicateurs économiques.',
  x='Un pays dont l’inflation dépasse durablement celle de son partenaire peut ainsi organiser une dépréciation graduelle pour préserver sa compétitivité.',
  t='def', b=988)

c('Qu’est-ce que le flottement administré ?',
  'Un régime où le taux est principalement déterminé par le marché, la banque centrale conservant la possibilité d’intervenir sans défendre de parité officielle.',
  x='Elle peut freiner une dépréciation excessive, une appréciation dangereuse ou une volatilité trop forte. Inde, Brésil et Hongrie en relèvent.',
  t='def', b=1002)

c('Comment une banque centrale soutient-elle sa monnaie en régime flottant ?',
  'Elle achète sa propre monnaie en vendant des devises de ses réserves ; à l’inverse, elle vend sa monnaie et achète des devises pour freiner une appréciation.',
  x='Le flottement n’implique donc pas l’inaction : les interventions peuvent être isolées ou concertées.',
  t='mec', b=1048)

c('Quel enchaînement explique l’appréciation du dollar au début des années 1980 ?',
  'La politique très restrictive de Paul Volcker à la Fed à partir de 1979 élève les taux, attire les capitaux, et les anticipations d’appréciation renforcent le mouvement.',
  x='L’objectif premier était de combattre l’inflation.',
  t='mec', b=1063)

c('Qu’appelle-t-on déficits jumeaux dans le cas américain des années 1980 ?',
  'La coexistence d’un déficit public et d’un déficit extérieur courant.',
  x='L’administration Reagan combinait baisses d’impôts et dépenses militaires, pendant que le dollar fort creusait le déficit commercial.',
  t='def', b=1086)

c('Que décident les accords du Plaza en septembre 1985, et entre quels pays ?',
  'Organiser une baisse ordonnée du dollar par des interventions coordonnées, entre États-Unis, Japon, République fédérale d’Allemagne, France et Royaume-Uni.',
  x='Les autorités vendent des dollars et achètent d’autres grandes devises : la tendance du marché s’inverse.',
  t='fait', b=1095)

c('Que visent les accords du Louvre de février 1987 ?',
  'Stabiliser les taux de change après la forte dépréciation du dollar qui a suivi le Plaza.',
  x='Les deux accords montrent qu’une gestion concertée reste possible en changes flottants.',
  t='fait', b=1112)

c('Pourquoi des taux japonais durablement faibles pèsent-ils sur le yen ?',
  'Parce que les placements en dollars apparaissent plus rémunérateurs, ce qui provoque des sorties de capitaux.',
  x='La Banque du Japon a maintenu des conditions très accommodantes face à une inflation très faible, voire déflationniste.',
  t='mec', b=1140)

c('Qu’est-ce qu’une ligne de swap entre banques centrales, et en quoi diffère-t-elle d’une intervention de change ?',
  'C’est un échange temporaire de monnaies fournissant de la liquidité en dollars ; une intervention de change, elle, achète ou vend des devises pour peser sur le taux.',
  x='Un swap n’est pas un don : une opération inverse est prévue à l’échéance.',
  t='dist', b=1175)

c('Comment se répartissent les régimes de change dans le monde en 2025 ?',
  'Arrimage ferme 29 pays soit 13 %, arrimage souple 88 soit 46 %, flottement 66 soit 34 %, autres ou non classés 13 soit 7 %.',
  x='Une majorité des pays ne pratiquent donc pas un flottement totalement libre.',
  t='fait', b=1188)

c('Pour quelles raisons de nombreux États recherchent-ils la stabilité de leur change ?',
  'Limiter l’inflation, rassurer les investisseurs, protéger les échanges, réduire les risques liés à l’endettement en devises et renforcer la crédibilité monétaire.',
  x='La flexibilité n’est donc pas un choix universellement préférable.',
  t='fait', b=1197)

c('Quels arguments les partisans des changes flottants avancent-ils ?',
  'L’ajustement automatique, une spéculation supposée stabilisatrice, l’autonomie monétaire et une moindre transmission internationale des déséquilibres.',
  x='Les partisans des changes fixes opposent la réduction du risque de change, la prévisibilité, la crédibilité et la limitation des dérives inflationnistes.',
  t='dist', b=1249)

c('Sur quelle idée Friedman fonde-t-il sa défense des changes flexibles en 1953 ?',
  'Sur l’autorégulation marchande : le taux de change étant un prix, il doit être déterminé par l’offre et la demande.',
  x='Référence : The Case for Flexible Exchange Rates. Les autorités n’ont pas l’information permettant de fixer une parité conforme aux fondamentaux.',
  t='aut', b=1264)

c('Quel contexte intellectuel accompagne la généralisation des changes flottants dans les années 1970 ?',
  'La stagflation remet en cause l’arbitrage inflation-chômage, et monétaristes puis nouveaux classiques gagnent en influence.',
  x='Ils insistent sur les mécanismes de marché, les anticipations, les contraintes d’offre et les limites de l’intervention publique.',
  t='mec', b=1278)

c('Pourquoi les gouvernements retardent-ils une dévaluation devenue nécessaire en changes fixes ?',
  'Parce qu’elle renchérit les importations, alimente l’inflation, fragilise les débiteurs en devises et peut être lue comme un échec politique.',
  x='Le flottement permettrait au contraire un ajustement continu, évitant les corrections brutales et tardives.',
  t='mec', b=1308)

c('Qu’est-ce que l’insularisation des politiques économiques ?',
  'La capacité d’un pays à limiter la transmission internationale des conséquences de sa politique, le taux de change absorbant une partie de l’ajustement.',
  x='À la fin des années 1960, la Bundesbank devait au contraire acheter des devises et fournir des deutschemarks pour contenir l’appréciation.',
  t='def', b=1373)

c('Pourquoi les changes flottants n’ont-ils pas stabilisé les monnaies autour de leurs fondamentaux ?',
  'Parce que la financiarisation du marché fait dépendre les cours des anticipations, des différentiels de taux, des arbitrages de portefeuille et des comportements mimétiques.',
  x='Une monnaie peut donc varier fortement sans modification proportionnelle de la situation économique.',
  t='mec', b=1398)

c('Pourquoi la spéculation peut-elle éloigner le change de son niveau fondamental ?',
  'Parce que les comportements mimétiques conduisent à acheter parce que les autres achètent et à vendre parce que les autres vendent : le mouvement devient cumulatif.',
  x='Elle peut aussi déclencher des attaques spéculatives contre les monnaies.',
  t='mec', b=1416)

c('Pourquoi les déséquilibres courants persistent-ils malgré le flottement ?',
  'Parce que le taux de change dépend aussi des mouvements de capitaux : un pays peut financer un déficit courant en attirant assez de capitaux pour soutenir sa monnaie.',
  x='Les États-Unis enregistrent régulièrement des déficits courants, l’Allemagne et le Japon de forts excédents.',
  t='dist', b=1429)

c('À combien s’élèvent les excédents courants cumulés de l’OPEP entre 1974 et 1981 ?',
  'Environ 450 milliards de dollars selon les chiffres du FMI cités par le cours.',
  x='Placées dans les banques internationales, ces recettes sont ensuite prêtées à d’autres pays : c’est le recyclage des pétrodollars.',
  t='fait', b=1465)

c('Pourquoi les prêts issus du recyclage des pétrodollars ont-ils créé une vulnérabilité ?',
  'Parce qu’ils étaient libellés en dollars : les pays devaient rembourser dans une monnaie différente de celle de leurs recettes.',
  x='Ils finançaient industrialisation, infrastructures et déficits extérieurs, dans des conditions monétaires alors favorables.',
  t='mec', b=1474)

c('Comment le choc Volcker alourdit-il doublement la dette des pays en développement ?',
  'La hausse des taux renchérit le service d’une dette souvent à taux variable, et l’appréciation du dollar augmente son coût en monnaie nationale.',
  x='Une dette d’un milliard de dollars passe de 5 à 8 milliards d’unités nationales si le dollar monte de 5 à 8 unités.',
  t='mec', b=1496)

c('Quel événement déclenche la crise internationale de la dette, et quand ?',
  'L’annonce par le Mexique, en août 1982, qu’il ne peut plus assurer normalement le service de sa dette extérieure.',
  x='Les banques réduisent alors leurs financements, ce qui aggrave les difficultés : la crise devient cumulative.',
  t='fait', b=1541)

c('Comment évolue la dette extérieure de l’Amérique latine entre 1975 et 1983 ?',
  'D’environ 75 milliards de dollars à 315 milliards.',
  x='Cette crise contribue à la « décennie perdue » des années 1980 : ajustements, difficultés financières et recul de l’investissement.',
  t='fait', b=1548)

c('Que démontre le choc Volcker sur l’autonomie promise par les changes flottants ?',
  'Qu’elle reste imparfaite : une décision de la Fed modifie les rendements en dollars, déclenche des mouvements de capitaux et renchérit les dettes extérieures.',
  x='Les économies demeurent exposées aux décisions des grandes banques centrales, même quand les monnaies flottent.',
  t='dist', b=1556)

c('Quel premier avantage les changes fixes procurent-ils aux entreprises ?',
  'Une moindre incertitude sur les transactions internationales, donc moins de recours coûteux aux instruments de couverture.',
  x='Un régime fixe ajustable ne supprime pourtant pas le risque de change, puisqu’une dévaluation reste possible.',
  t='fait', b=1592)

c('Comment un ancrage monétaire peut-il servir la désinflation ?',
  'En stabilisant le prix des importations et les anticipations d’inflation, il permet d’importer la crédibilité monétaire du pays de référence.',
  x='La stratégie n’est efficace que si la parité est crédible : sinon les agents continuent de vendre la monnaie nationale.',
  t='mec', b=1619)

c('Qu’est-ce que la peur du flottement, mise en évidence par Calvo et Reinhart en 2002 ?',
  'La réticence des autorités à laisser leur monnaie varier librement : officiellement flottants, de nombreux pays interviennent fortement.',
  x='Référence : « Fear of Floating », Quarterly Journal of Economics.',
  t='aut', b=1642)

c('Qu’est-ce que l’effet de bilan lié à une dépréciation ?',
  'L’alourdissement, en monnaie nationale, de dettes libellées en devises alors que les revenus restent nationaux : la situation financière se dégrade brutalement.',
  x='C’est l’un des deux mécanismes expliquant la peur du flottement, avec l’inflation importée.',
  t='def', b=1655)

c('Quels trois objectifs souhaitables le triangle de Mundell met-il en jeu, et pourquoi chacun compte-t-il ?',
  'La mobilité des capitaux, qui mobilise l’épargne internationale ; l’autonomie monétaire, instrument conjoncturel ; la stabilité du change, qui limite le risque de change.',
  x='Les banques centrales des pays avancés visent généralement une inflation proche de 2 %, ce qui suppose d’adapter les taux à la situation nationale.',
  t='aut', b=1692)

c('Pourquoi certains pays ancrent-ils leur monnaie au dollar ?',
  'Parce qu’une part importante de leurs transactions internationales, dont le pétrole, est libellée en dollars : une variation du change en modifierait le coût.',
  x='On parle selon les cas de dollarisation partielle ou de stabilisation du taux de change vis-à-vis du dollar.',
  t='mec', b=1713)

c('Qu’est-ce qu’une crise de change ?',
  'Une chute brutale de la valeur externe d’une monnaie, souvent accompagnée de sorties de capitaux, pouvant conduire à une inflation très élevée.',
  x='La stabilité du change limite donc certaines sources d’instabilité économique.',
  t='def', b=1719)

c('Que soutient Jean-Marc Daniel en 2015 à propos de l’histoire monétaire ?',
  'Que le monde a « accompli une sorte de parcours complet en essayant toutes les éventualités offertes par le triangle » de Mundell.',
  x='L’histoire du système monétaire international n’est donc pas une progression vers un régime idéal mais une succession d’arbitrages.',
  t='aut', b=1729)

c('Comment le triangle historique inversé de Plihon représente-t-il les choix monétaires ?',
  'Par les contraires des trois objectifs : autarcie financière, union monétaire et flottement des changes.',
  x='Il permet de situer Bretton Woods, le SME, la libéralisation des années 1990 et l’euro selon les objectifs abandonnés.',
  t='dist', b=1733)

c('Sur quelles règles le système de Bretton Woods repose-t-il ?',
  'Des changes fixes mais ajustables, les monnaies rattachées au dollar, lui-même convertible en or à 35 dollars l’once auprès des autorités monétaires étrangères.',
  x='Les mouvements de capitaux restaient largement contrôlés : la crise de 1929 avait montré leur rôle dans la propagation des crises.',
  t='fait', b=1754)

c('Que signifie l’expression « le bas de la balance des paiements est fermé » ?',
  'Que les États restreignent les mouvements financiers entre résidents et non-résidents, ce qui élargit la marge de manœuvre monétaire des banques centrales.',
  x='Cette limitation permet de concilier changes fixes et autonomie monétaire.',
  t='def', b=1767)

c('Quelles dates marquent le passage du système de Bretton Woods au flottement ?',
  'Le 15 août 1971, les États-Unis suspendent la convertibilité du dollar en or ; en 1973, les principales monnaies flottent.',
  x='La libéralisation des capitaux s’accélère ensuite, surtout dans les années 1980-1990.',
  t='fait', b=1774)

c('Pourquoi le SME devient-il intenable au début des années 1990 ?',
  'Parce que la libre circulation des capitaux empêche de maintenir des politiques monétaires divergentes : la France, plus inflationniste, devait relever ses taux pour défendre sa parité.',
  x='En septembre 1992, la livre sterling et la lire quittent le mécanisme de change ; en août 1993 les marges passent à ± 15 %.',
  t='mec', b=1787)

c('Quelles étapes marquent l’introduction de l’euro ?',
  'Monnaie commune pour les opérations scripturales en 1999, billets et pièces en circulation en 2002.',
  x='Les États membres renoncent à leur monnaie, à leur taux de change bilatéral et à leur autonomie monétaire, au profit de la BCE.',
  t='fait', b=1816)

c('Quelle configuration singulière l’euro crée-t-il dans le système monétaire international ?',
  'Le risque de change disparaît entre membres de l’union, mais l’euro continue de flotter face aux monnaies extérieures.',
  x='Plusieurs configurations monétaires coexistent donc au sein du système contemporain.',
  t='dist', b=1839)

c('Pourquoi la politique de change est-elle indispensable en changes fixes ?',
  'Parce que les autorités se sont engagées à maintenir une parité : elles doivent intervenir dès que le taux s’en écarte.',
  x='En flottement, les interventions ne sont que ponctuelles et facultatives.',
  t='dist', b=1866)

c('Qu’appelle-t-on guerre des monnaies ?',
  'La situation où plusieurs États cherchent un avantage commercial par des dévaluations successives, alors que les taux de change sont relatifs.',
  x='Tous ne peuvent déprécier simultanément leur monnaie les uns par rapport aux autres : l’avantage recherché s’annule.',
  t='def', b=1893)

c('Pourquoi une accusation de sous-évaluation ne prouve-t-elle pas une manipulation monétaire ?',
  'Parce que l’évaluation du niveau d’équilibre d’une monnaie dépend des méthodes retenues et reste discutée.',
  x='La Chine a régulièrement été visée par ce reproche, notamment par les États-Unis.',
  t='dist', b=1888)

c('Pourquoi défendre une monnaie contre la dépréciation est-il plus contraignant que freiner son appréciation ?',
  'Parce que la banque centrale peut créer sa propre monnaie pour la vendre, mais doit puiser dans ses réserves pour acheter des devises qu’elle n’émet pas.',
  x='La contrainte est particulièrement forte pour les pays en développement confrontés à une attaque spéculative.',
  t='dist', b=1925)

c('Quels avantages un relèvement des taux présente-t-il pour soutenir la monnaie ?',
  'Il attire les capitaux, ce qui soutient le change sans épuiser les réserves, et limite l’inflation importée par le renchérissement des produits étrangers.',
  x='Le coût est un ralentissement de l’activité : c’est l’arbitrage entre équilibre externe et équilibre interne.',
  t='mec', b=1945)

c('Qu’est-ce que le contrôle des changes, et en quoi diffère-t-il des autres instruments ?',
  'Une réglementation de l’accès aux devises et de certaines transactions : il agit sur les quantités, non sur les prix.',
  x='En Chine, les particuliers sont soumis à un plafond annuel de conversion équivalant à 50 000 dollars.',
  t='def', b=1967)

c('Qu’est-ce qui distingue une dévaluation subie d’une dévaluation compétitive ?',
  'La première est imposée par un déficit persistant ou une attaque spéculative qui épuise les réserves ; la seconde est un choix destiné à regagner de la compétitivité.',
  x='Une dévaluation abaisse officiellement la parité, dans un régime fixe ou administré.',
  t='dist', b=1993)

c('Comment les modifications de parité étaient-elles encadrées sous Bretton Woods ?',
  'Le FMI surveillait les changements ; au-delà de 10 % cumulés, une procédure particulière s’appliquait.',
  x='Le cours mentionne aussi un seuil de 15 %, sans qu’il faille en faire une règle unique : l’idée est d’éviter des dévaluations concurrentielles déstabilisatrices.',
  t='fait', b=2006)

c('Quel ordre de grandeur le tourisme représente-t-il dans le PIB français, et pourquoi le change y importe-t-il ?',
  'De l’ordre de 7 à 8 % du PIB selon le périmètre retenu ; une dépréciation de l’euro accroît le pouvoir d’achat des visiteurs étrangers.',
  x='Le taux de change influence donc les recettes touristiques, et pas seulement les ventes de marchandises.',
  t='fait', b=2034)

c('Quels risques une dépréciation comporte-t-elle malgré ses avantages commerciaux ?',
  'Elle renchérit les importations, nourrit l’inflation par les biens de consommation et les intrants, et alourdit les dettes libellées en devises.',
  x='Elle peut aussi provoquer des sorties de capitaux financiers si elle dégrade la confiance.',
  t='dist', b=2042)

c('Que représente la courbe en J après une dévaluation ?',
  'La dégradation initiale du solde commercial, suivie de son redressement progressif.',
  x='Elle traduit le décalage entre les effets-prix, immédiats, et les effets-volume, qui demandent du temps.',
  t='def', b=2075)

c('Pourquoi les effets-volume d’une dévaluation sont-ils différés ?',
  'Parce que les contrats sont déjà conclus, que les acheteurs étrangers ne changent pas instantanément de fournisseur et que les capacités de production ne s’ajustent pas immédiatement.',
  x='Les quantités échangées restent donc rigides à court terme, alors que les prix relatifs changent aussitôt.',
  t='mec', b=2088)

c('Qu’énonce la condition de Marshall-Lerner ?',
  'Une dévaluation améliore le solde commercial si la somme des élasticités-prix des demandes d’exportations et d’importations, en valeur absolue, dépasse l’unité.',
  x='La condition suppose notamment un commerce initialement équilibré ; en dessous de 1, l’effet est défavorable.',
  t='form', b=2113)

c('Que montre l’exemple chiffré d’une dévaluation de 10 % selon les élasticités ?',
  'Avec des élasticités fortes le solde passe à +4,6 ; avec des élasticités faibles il tombe à −4,8, à partir d’un solde initialement nul.',
  x='Ce n’est donc pas la baisse du change qui garantit l’amélioration, mais la réaction des volumes.',
  t='fait', b=2137)

c('Pourquoi la phase longue d’une dévaluation peut-elle effacer ses gains ?',
  'Parce que l’inflation importée renchérit durablement les coûts nationaux, érodant progressivement l’avantage de compétitivité obtenu.',
  x='Les gains ne durent que si les effets-volume l’emportent sur ce renchérissement.',
  t='mec', b=2106)

c('Pourquoi une spécialisation hors prix réduit-elle l’efficacité d’une dévaluation ?',
  'Parce que les acheteurs privilégient la qualité, l’innovation, la marque et la technologie : la demande réagit peu aux prix.',
  x='Une faible sensibilité aux prix peut d’ailleurs traduire un fort pouvoir de marché plutôt qu’un défaut de compétitivité.',
  t='mec', b=2160)

c('Pourquoi une économie désindustrialisée tire-t-elle moins profit d’une dévaluation ?',
  'Parce que ses entreprises n’ont pas les capacités de produire les substituts aux biens importés : les volumes importés ne peuvent guère diminuer.',
  x='Le résultat dépend du degré d’industrialisation, de la diversification et de la dépendance aux intrants étrangers.',
  t='mec', b=2180)

c('Comment le comportement de marge des entreprises limite-t-il les gains d’une dévaluation ?',
  'En conservant une partie du gain de change sous forme de marge plutôt qu’en baissant leurs prix de vente à l’étranger.',
  x='Ce choix est d’autant plus possible que le marché est peu concurrentiel.',
  t='mec', b=2193)

c('Quelles stratégies opposent l’Allemagne et la France au début des années 2000 ?',
  'L’Allemagne, « homme malade de l’Europe », joue la modération salariale et les réformes Hartz de 2003-2005 pour préserver marges et investissement ; les entreprises françaises subissent des pressions sur leurs marges et recourent davantage aux délocalisations.',
  x='Les marges financent la recherche, l’innovation et la qualité, donc la montée en gamme. Spécialisation et organisation productive jouent aussi.',
  t='dist', b=2215)

c('En quoi consiste le cercle vicieux de la monnaie faible ?',
  'Dévaluation, inflation importée, effets de second tour sur les salaires, perte de l’avantage de compétitivité, déficit persistant, puis nouvelle dévaluation.',
  x='L’indexation des salaires sur les prix renforce le mécanisme ; les anticipations des investisseurs l’accélèrent.',
  t='mec', b=2244)

c('Comment une dépréciation alourdit-elle une dette souveraine libellée en dollars ?',
  'Une dette d’un milliard de dollars double en monnaie nationale si le dollar passe de 100 à 200 unités, sans que le montant dû ait changé.',
  x='Le cours illustre ce risque par les fortes chutes du peso argentin, parfois qualifiées de « dévissage ».',
  t='mec', b=2283)

c('Quel niveau l’inflation française atteint-elle au début de 1982 ?',
  'Environ 14 %, nettement davantage qu’en Allemagne.',
  x='La relance du gouvernement Mauroy intervenait donc dans un contexte de prix déjà très dynamiques, au sein du SME.',
  t='fait', b=2307)

c('À quelles dates la France dévalue-t-elle le franc entre 1981 et 1983 ?',
  'En octobre 1981, juin 1982 et mars 1983.',
  x='Il s’agit principalement de dévaluations subies : les autorités cherchaient à maintenir le franc dans le SME.',
  t='fait', b=2314)

c('Pourquoi les dévaluations françaises n’ont-elles pas rétabli la compétitivité ?',
  'Parce que l’inflation française restait supérieure à celle de plusieurs partenaires, notamment l’Allemagne : l’avantage de prix s’érodait aussitôt.',
  x='La France connaît ainsi une dynamique proche d’un cercle vicieux de monnaie faible.',
  t='mec', b=2328)

c('Qu’est-ce qui distingue la désinflation de la déflation ?',
  'La désinflation est un ralentissement du rythme de hausse des prix ; la déflation une diminution du niveau général des prix.',
  x='La politique du franc fort repose sur une stratégie de désinflation, non de déflation.',
  t='dist', b=2366)

c('En quoi consiste la désinflation compétitive ?',
  'Restaurer la compétitivité-prix par la maîtrise des prix et des coûts plutôt que par la dévaluation, en maintenant une monnaie stable ou forte.',
  x='Une monnaie forte abaisse le prix en monnaie nationale des produits importés, ce qui aide à contenir l’inflation.',
  t='def', b=2372)

c('Quelles politiques structurelles accompagnent la désinflation compétitive française ?',
  'Les privatisations, l’ouverture à la concurrence de secteurs protégés et un assouplissement du fonctionnement du marché du travail.',
  x='L’objectif est de limiter le pouvoir de fixation des prix et de favoriser les gains de productivité.',
  t='fait', b=2399)

c('Quel double objectif la politique monétaire restrictive poursuit-elle dans cette stratégie ?',
  'Un objectif interne, réduire l’inflation, et un objectif externe, défendre la valeur du franc.',
  x='Des taux élevés attirent les capitaux et contiennent la demande, mais pèsent sur l’activité.',
  t='fait', b=2427)

c('Qu’appelle-t-on désinflation importée ?',
  'La baisse des coûts d’intrants — matières premières, énergie, biens intermédiaires, équipements — permise par une monnaie forte, à prix étrangers inchangés.',
  x='Elle accroît le pouvoir d’achat international des agents nationaux et facilite la maîtrise des prix.',
  t='def', b=2447)

c('Quels résultats la désinflation française obtient-elle entre le début des années 1980 et 1990 ?',
  'L’inflation passe d’environ 14 % à environ 2 %.',
  x='La référence aux 2 % mesure l’ampleur de la désinflation et ne doit pas être confondue avec une cible d’inflation moderne.',
  t='fait', b=2506)

c('Pendant quelles années la balance courante française est-elle excédentaire après la désinflation ?',
  'De 1992 à 2003.',
  x='La France améliore donc ses équilibres extérieurs sans recourir à de nouvelles dévaluations répétées.',
  t='fait', b=2514)

c('Comment le taux de marge des entreprises françaises évolue-t-il entre 1985 et 1989 ?',
  'De 25 % à 32 % de la valeur ajoutée, soit environ 7 points de plus.',
  x='Le taux de marge rapporte l’excédent brut d’exploitation à la valeur ajoutée.',
  t='fait', b=2524)

c('Qu’énonce la formule attribuée à Helmut Schmidt ?',
  '« Les profits d’aujourd’hui sont les investissements de demain et les emplois d’après-demain. »',
  x='La restauration des marges devait donc relancer l’investissement puis l’emploi — ce qui ne s’est pas vérifié en France.',
  t='aut', b=2530)

c('Pourquoi la désinflation peut-elle alourdir le coût réel de la dette ?',
  'Parce que le taux réel est le taux nominal diminué de l’inflation : à taux nominal de 10 %, une inflation qui s’effondre rend le coût réel fortement positif.',
  x='Avec une inflation élevée, le même emprunt pouvait avoir un coût réel négatif.',
  t='mec', b=2543)

c('Qu’est-ce qui distingue l’effet de levier de l’effet de massue ?',
  'Le levier joue quand la rentabilité économique dépasse le coût réel de la dette ; la massue quand ce coût la dépasse et dégrade la rentabilité financière.',
  x='Exemples : 10 % contre 4 % dans le premier cas, 5 % contre 8 % dans le second.',
  t='dist', b=2556)

c('Pourquoi les profits restaurés n’ont-ils pas relancé l’investissement français ?',
  'Parce que les entreprises ont d’abord remboursé leurs dettes face à des taux réels élevés, que la globalisation offrait des placements alternatifs, et que l’investissement dépend des débouchés anticipés.',
  x='L’amélioration des marges ne garantit donc pas leur transformation en capacités productives.',
  t='mec', b=2589)

c('Par quel enchaînement la politique du franc fort pouvait-elle freiner l’activité ?',
  'Taux élevés et modération salariale pèsent sur la demande, les entreprises réduisent production et investissement, le chômage monte, et le chômage affaiblit encore les salaires et la consommation.',
  x='La stabilité monétaire est atteinte, mais au prix d’un cercle cumulatif défavorable à l’activité.',
  t='mec', b=2635)

c('Quels repères de croissance le cours retient-il pour la France des années 1980-1990 ?',
  'Environ 2 % par an en France contre près de 3 % en moyenne dans les pays de l’OCDE.',
  x='Ce sont des repères comparatifs : demande intérieure peu dynamique, taux réels élevés et investissement insuffisant expliquent l’écart.',
  t='fait', b=2683)

c('Comment le chômage français évolue-t-il entre 1982 et 1998 ?',
  'D’environ 8 % de la population active à environ 12 %.',
  x='Le cours compare ce niveau à un chômage de l’ordre de 7 % dans les autres pays de l’OCDE.',
  t='fait', b=2694)

c('Qu’appelle-t-on effets d’hystérèse du chômage ?',
  'Le fait que des chocs initialement conjoncturels laissent des conséquences durables, un chômage prolongé devenant chômage de longue durée.',
  x='La faiblesse persistante de l’investissement limite en outre les gains futurs de productivité et les créations d’emplois.',
  t='def', b=2717)

c('Quelle précaution le cours demande-t-il avant d’imputer les difficultés françaises au franc fort ?',
  'Désindustrialisation, transformations technologiques, mondialisation et mutations du marché du travail y ont aussi contribué.',
  x='La politique du franc fort illustre les risques d’une désinflation prolongée, elle n’en est pas la cause unique.',
  t='dist', b=2720)

c('De quoi dépend l’efficacité d’une stratégie de monnaie forte ?',
  'De la structure productive, de la capacité d’innovation des entreprises, de la conjoncture, du niveau des taux, des débouchés anticipés et de la durée des politiques restrictives.',
  x='Une monnaie forte n’est donc pas une bonne monnaie pour tous les agents et dans toutes les situations.',
  t='fait', b=2742)

c('Pourquoi un même taux de change ne convient-il pas à tous les agents ?',
  'Une monnaie forte accroît le pouvoir d’achat des ménages sur les produits importés mais pénalise les exportateurs ; une entreprise importatrice de matières premières la préfère, une exportatrice non.',
  x='Les effets dépendent de la position des agents dans les échanges internationaux.',
  t='dist', b=2794)

c('Pourquoi une appréciation de l’euro ne touche-t-elle pas identiquement tous les membres de la zone ?',
  'Parce que les structures productives diffèrent : haut de gamme peu sensible aux prix, exportations sensibles aux prix, ou forte dépendance énergétique.',
  x='Il n’existe donc pas un niveau de change optimal pour tous les membres d’une union monétaire.',
  t='dist', b=2811)

c('Quelle thèse centrale Stephen Miran défend-il dans son rapport de novembre 2024 ?',
  'Que le dollar est structurellement trop fort pour l’industrie manufacturière américaine, la demande internationale d’actifs sûrs entretenant sa surévaluation.',
  x='Le dollar est à la fois monnaie de réserve, de facturation, de placement et de transaction financière.',
  t='aut', b=2846)

c('Quelle identité macroéconomique nuance l’explication du déficit courant américain par le change ?',
  'Solde courant = épargne nationale − investissement national : un déficit signifie que l’investissement dépasse l’épargne.',
  x='Il peut être associé à un déficit public important ou à une épargne privée insuffisante : le niveau du dollar n’explique pas tout.',
  t='form', b=2863)

c('Quelle contradiction le protectionnisme crée-t-il avec l’objectif d’un dollar moins fort ?',
  'Les droits de douane peuvent nourrir l’inflation, conduire la Fed à maintenir des taux plus élevés et donc soutenir le dollar.',
  x='L’effet n’est pas automatique : anticipations de croissance et réactions des partenaires jouent également.',
  t='mec', b=2878)

c('Que désignent les « accords de Mar-a-Lago » ?',
  'Un scénario discuté de dépréciation coordonnée du dollar, obtenue en incitant les partenaires à laisser leur monnaie s’apprécier.',
  x='Il s’agit d’une proposition, non d’un accord conclu ; elle fait référence au précédent du Plaza de septembre 1985.',
  t='def', b=2895)

c('Pourquoi les partenaires des États-Unis hésiteraient-ils à laisser leur monnaie s’apprécier ?',
  'La Chine dépend de ses exportations dans un contexte de demande intérieure faible, le Japon craint de compliquer la sortie d’une inflation trop basse, la zone euro de pénaliser des secteurs déjà peu dynamiques.',
  x='Les taux de change étant relatifs, l’appréciation des autres monnaies est la condition d’une dépréciation du dollar.',
  t='mec', b=2908)

c('Quel paradoxe la volonté de déprécier le dollar rencontre-t-elle ?',
  'Le dollar est la principale monnaie de réserve : une perte de confiance dans ses actifs renchérirait le financement américain et fragiliserait les marchés internationaux.',
  x='Un investisseur européen détenant 1 000 dollars voit son placement tomber de 1 000 à 800 euros si l’euro passe de 1 à 1,25 dollar.',
  t='mec', b=2934)

c('Qu’appelle-t-on fuite vers la qualité en période de crise ?',
  'La recherche par les investisseurs d’actifs très liquides et jugés sûrs, dont le dollar et les titres publics américains.',
  x='Il faut la distinguer du rôle de prêteur en dernier ressort de la Fed, qui fournit de la liquidité aux institutions éligibles.',
  t='def', b=2963)

c('Qu’est-ce qu’un stablecoin, et de quoi dépend sa stabilité ?',
  'Un jeton numérique dont l’émetteur cherche à maintenir la valeur par rapport à un actif de référence, souvent le dollar ; sa stabilité dépend de la qualité des réserves, des mécanismes de remboursement et de la confiance.',
  x='À la différence du Bitcoin, sa valeur est censée rester stable, mais il peut perdre sa parité.',
  t='def', b=2994)

c('Qu’est-ce qui distingue une monnaie numérique de banque centrale d’un stablecoin privé ?',
  'La première constitue une créance sur la banque centrale émettrice, selon son architecture ; le second est émis par un acteur privé.',
  x='Son développement soulève des enjeux de souveraineté monétaire et d’organisation des paiements.',
  t='dist', b=3005)

c('Pourquoi les stablecoins adossés au dollar peuvent-ils soutenir la demande d’actifs américains ?',
  'Parce que leurs émetteurs doivent détenir des réserves adaptées : dépôts en dollars, bons du Trésor à court terme et autres actifs liquides.',
  x='En juillet 2025, le GENIUS Act fixe aux États-Unis un cadre fédéral sur les réserves, le remboursement, la transparence et la supervision.',
  t='mec', b=3012)

c('Quelles ruptures historiques jalonnent le système monétaire international depuis 1944 ?',
  'Bretton Woods en 1944, la fin de la convertibilité en or en 1971, le flottement en 1973, le Plaza en 1985, le Louvre en 1987, l’euro en 1999, puis les tensions de 2025.',
  x='Le dollar reste central malgré la disparition de Bretton Woods, mais sa valeur externe fluctue fortement.',
  t='fait', b=3043)

c('Comment le cours de l’euro évolue-t-il entre son point bas de 2022 et le début de 2026 ?',
  'D’environ 0,97 dollar pour un euro à une valeur proche de 1,18 dollar.',
  x='Cette appréciation abaisse le prix des importations facturées en dollars mais renchérit les exportations européennes.',
  t='fait', b=3055)

c('Quels effets une appréciation du dollar produit-elle sur les économies émergentes ?',
  'Elle renchérit les dettes libellées en dollars et les importations facturées dans cette monnaie, tend les réserves de change et accentue les sorties de capitaux.',
  x='En 2024, plusieurs monnaies se déprécient face au dollar, particulièrement en Amérique latine.',
  t='mec', b=3071)

c('Quelles trois conclusions fondamentales l’étude des taux de change dégage-t-elle ?',
  'Aucun régime n’est universellement optimal, aucun niveau de change ne convient à tous les agents, et les politiques de change ont des effets internationaux majeurs.',
  x='Le cas du dollar est spécifique : son rôle mondial procure une demande structurelle d’actifs américains mais crée des risques systémiques.',
  t='fait', b=3087)
