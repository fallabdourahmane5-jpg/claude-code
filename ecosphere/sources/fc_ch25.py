# -*- coding: utf-8 -*-
"""Deuxième année — chapitre 5 (ch. 25) : l'équilibre macroéconomique (IS-LM, IS-LM-BP, OG-DG)."""
from fc_base import lot, c

L = lot(25)

c('Qu’est-ce qu’un modèle économique ?',
  'Une représentation abstraite et simplifiée d’une réalité économique, construite à partir d’hypothèses qui isolent certaines relations.',
  x='Sa pertinence tient moins à son réalisme qu’à sa capacité d’explication dans le cadre des hypothèses retenues.',
  t='def', b=12)

c('Qu’est-ce qu’un idéal-type chez Max Weber, et à quoi le cours le rapproche-t-il ?',
  'Une construction intellectuelle qui accentue certains traits de la réalité pour en faciliter l’analyse ; la démarche de modélisation économique en relève.',
  x='La concurrence pure et parfaite et le monopole pur sont deux idéaux-types, entre lesquels se situent les marchés réels.',
  t='aut', b=24)

c('Quel double effet de l’investissement Harrod et Domar mettent-ils en évidence ?',
  'Il stimule la demande et accroît les capacités de production, sans que rien ne garantisse la correspondance durable des deux.',
  x='La croissance peut donc être instable, avec des déséquilibres cumulatifs.',
  t='aut', b=36)

c('Vers quoi l’économie converge-t-elle dans le modèle de Solow de 1956 ?',
  'Vers un état stationnaire, du fait des rendements décroissants du capital.',
  x='Contrairement à Harrod-Domar, le modèle décrit une convergence vers une trajectoire équilibrée.',
  t='aut', b=42)

c('Que signifie raisonner en équilibre partiel chez Marshall ?',
  'Étudier un marché isolément : l’intersection d’une offre croissante et d’une demande décroissante détermine un prix et une quantité, l’ajustement passant par les prix.',
  x='Référence : Principles of Economics, 1890. L’équilibre général de Walras considère au contraire tous les marchés simultanément.',
  t='aut', b=59)

c('Quelle défaillance de marché Pigou analyse-t-il en 1920, et par quel instrument la corriger ?',
  'Les externalités négatives, coûts imposés à la collectivité sans être intégrés par le producteur ; une taxation permet de les internaliser.',
  x='Référence : The Economics of Welfare. C’est le principe de la taxe pigouvienne.',
  t='aut', b=77)

c('Comment Pigou explique-t-il le chômage en 1933 ?',
  'Par un salaire réel maintenu au-dessus du niveau d’équilibre : une baisse suffisante rétablirait l’équilibre du marché du travail.',
  x='Référence : The Theory of Unemployment. Keynes contestera cette analyse en montrant que le chômage peut être involontaire.',
  t='aut', b=82)

c('Qu’est-ce que le tâtonnement walrasien ?',
  'Le processus par lequel un commissaire-priseur centralise offres et demandes, constate les déséquilibres et annonce de nouveaux prix jusqu’à l’équilibre.',
  x='Référence : Éléments d’économie politique pure, 1874. Walras cherche un système de prix rendant tous les marchés simultanément compatibles.',
  t='aut', b=91)

c('Qu’est-ce qu’un optimum de Pareto ?',
  'Une situation où il est impossible d’améliorer le bien-être d’un agent sans détériorer celui d’un autre.',
  x='Sous certaines conditions, un équilibre concurrentiel est optimal en ce sens.',
  t='def', b=103)

c('Quelle précaution faut-il garder à l’esprit à propos de l’optimum de Pareto ?',
  'Il ne garantit pas une répartition équitable des richesses : plusieurs allocations très inégales peuvent être optimales.',
  x='D’où la distinction entre analyse positive, qui explique, et analyse normative, qui juge le caractère souhaitable.',
  t='dist', b=109)

c('Que soutient la loi des débouchés de Jean-Baptiste Say ?',
  'Que la production engendre les revenus nécessaires à l’achat de ce qui est produit : l’offre crée sa propre demande.',
  x='Référence : Traité d’économie politique, 1803. La monnaie n’y est qu’un intermédiaire des échanges, ce qui rend une insuffisance durable de demande difficile à concevoir.',
  t='aut', b=115)

c('Pourquoi, chez Keynes, l’économie peut-elle rester durablement en sous-emploi ?',
  'Parce que les revenus distribués ne sont pas intégralement dépensés : les agents peuvent conserver de la monnaie pour des motifs de précaution et de spéculation.',
  x='Référence : Théorie générale de l’emploi, de l’intérêt et de la monnaie, 1936. Il en résulte un équilibre de sous-emploi.',
  t='aut', b=123)

c('Qu’est-ce que la demande effective chez Keynes ?',
  'La demande anticipée par les entrepreneurs, qui détermine leurs décisions de production et d’embauche.',
  x='Le chômage peut dès lors être involontaire : des individus veulent travailler au salaire en vigueur sans trouver d’emploi.',
  t='def', b=132)

c('Quelle représentation François Quesnay propose-t-il en 1758 ?',
  'Le Tableau économique, l’une des premières représentations systématiques des interdépendances économiques, sous forme de flux entre classes sociales.',
  x='Keynes renouvellera cette approche en reliant production, revenus, consommation, épargne, investissement et monnaie.',
  t='aut', b=138)

c('Qu’est-ce qui distingue flux réels et flux monétaires dans le circuit économique ?',
  'Les premiers sont les mouvements de biens, de services et de facteurs ; les seconds les paiements et revenus associés à ces opérations.',
  x='Production, revenus et dépenses sont ainsi interdépendants.',
  t='dist', b=148)

c('Quel rôle Simon Kuznets joue-t-il dans la comptabilité nationale ?',
  'Il élabore les premières estimations systématiques du revenu national américain, à l’origine de la comptabilité nationale moderne.',
  x='La crise de 1929 avait révélé la nécessité de mesurer l’activité économique.',
  t='aut', b=158)

c('De combien le PIB réel américain recule-t-il entre 1929 et 1933 ?',
  'D’environ 25 à 30 % selon les séries statistiques et les conventions retenues.',
  x='Cette contraction s’accompagne d’une forte hausse du chômage.',
  t='fait', b=163)

c('Selon quelles trois approches le PIB peut-il être calculé ?',
  'Par la production, somme des valeurs ajoutées ; par la demande, C + I + G + X − M ; par les revenus distribués.',
  x='Les trois doivent conduire au même résultat, sous réserve des ajustements statistiques.',
  t='fait', b=169)

c('Quelles valeurs le PIB français atteint-il en 2019, 2020 et 2025 dans les données présentées ?',
  '2 437,6 milliards d’euros en 2019, 2 317,8 en 2020, puis 2 953,5 en 2025.',
  x='La baisse de 2020 traduit le choc de la pandémie ; les valeurs étant à prix courants, leur évolution mêle volumes et prix.',
  t='fait', b=189)

c('Qu’est-ce qu’un équilibre macroéconomique ?',
  'Une situation où les grandes variables sont compatibles entre elles : épargne et investissement, offre et demande de monnaie, équilibre extérieur, offre et demande globales.',
  x='Il ne suppose pas la rencontre d’une offre et d’une demande sur un marché, mais la cohérence d’ensemble des relations économiques.',
  t='def', b=193)

c('Comment s’écrit l’équilibre emplois-ressources en économie ouverte ?',
  'PIB + M = C + I + G + X : les ressources, production intérieure et importations, égalent leurs emplois.',
  x='C’est une identité comptable fondamentale, qui tient compte notamment des variations de stocks.',
  t='form', b=214)

c('Quelle égalité constitue la condition d’équilibre en économie fermée sans État ?',
  'I = S : en rapprochant Y = C + I et Y = C + S, l’investissement doit égaler l’épargne.',
  x='L’égalité des grandeurs réalisées est vérifiée comptablement ex post ; celle des grandeurs désirées est une condition économique.',
  t='form', b=231)

c('Quelle différence sépare l’égalité comptable et la condition d’équilibre entre épargne et investissement ?',
  'La première porte sur les montants réalisés, toujours vérifiés ex post ; la seconde sur les montants désirés par les agents.',
  x='Si les entreprises investissent moins que ce que les ménages veulent épargner, la demande devient insuffisante.',
  t='dist', b=232)

c('Pourquoi l’ajustement s’effectue-t-il par les quantités dans le cadre keynésien de court terme ?',
  'Parce que prix et salaires peuvent être rigides : face à une baisse de la demande, l’entreprise réduit sa production, ses investissements et ses effectifs.',
  x='L’emploi, et non le prix, supporte donc l’ajustement.',
  t='mec', b=246)

c('De quoi l’investissement dépend-il chez Keynes ?',
  'Des débouchés futurs anticipés, du coût du financement, du rendement attendu du capital et de l’incertitude.',
  x='Il est entrepris lorsque l’efficacité marginale anticipée du capital dépasse le taux d’intérêt ; une baisse du taux peut rester inopérante si les anticipations sont dégradées.',
  t='mec', b=261)

c('Quels trois motifs déterminent la demande de monnaie chez Keynes ?',
  'La transaction, la précaution et la spéculation.',
  x='Cette préférence pour la liquidité contribue à déterminer le taux d’intérêt, qui influence ensuite l’investissement.',
  t='fait', b=272)

c('Que propose John Hicks en 1937 dans Econometrica ?',
  'Une formalisation de la Théorie générale articulant l’équilibre du marché des biens et celui de la monnaie, le taux d’intérêt faisant le lien.',
  x='Référence : « Mr. Keynes and the “Classics”: A Suggested Interpretation ». Cette démarche nourrit la synthèse néoclassique.',
  t='aut', b=284)

c('Quel rôle Alvin Hansen joue-t-il dans la diffusion du modèle en 1941 ?',
  'Il en fait un instrument d’analyse des politiques conjoncturelles, fondant la tradition Hicks-Hansen.',
  x='Référence : Fiscal Policy and Business Cycles. Il est aussi associé à la notion de stagnation séculaire, développée à la fin des années 1930.',
  t='aut', b=295)

c('Que représente la courbe BP introduite par Fleming et Mundell ?',
  'Les combinaisons de revenu et de taux d’intérêt compatibles avec l’équilibre extérieur, sous une hypothèse donnée de mobilité des capitaux.',
  x='Fleming publie en 1962, Mundell en 1963 : le modèle IS-LM-BP permet d’étudier l’efficacité des politiques selon le régime de change.',
  t='aut', b=308)

c('Quelles trois hypothèses fondent le modèle IS-LM traditionnel ?',
  'La monnaie est active, le raisonnement est de court terme, et le niveau général des prix est fixe.',
  x='Le modèle ne permet donc pas, à lui seul, d’expliquer l’inflation ni la croissance potentielle.',
  t='fait', b=323)

c('Que représente la courbe IS, et pourquoi est-elle décroissante ?',
  'Les combinaisons de revenu et de taux d’intérêt équilibrant le marché des biens et services ; une baisse du taux réduit le coût du financement, stimule l’investissement et élève le revenu.',
  x='IS signifie Investment-Saving : la relation entre taux d’intérêt et revenu d’équilibre est inverse.',
  t='def', b=339)

c('Que représente la courbe LM, et pourquoi est-elle croissante ?',
  'Les combinaisons de revenu et de taux d’intérêt équilibrant le marché de la monnaie ; une hausse du revenu accroît la demande de monnaie pour transactions, donc exige un taux plus élevé à offre constante.',
  x='LM signifie Liquidity Preference-Money Supply : la condition s’écrit M = L.',
  t='def', b=349)

c('Que détermine l’intersection des courbes IS et LM ?',
  'Le revenu d’équilibre et le taux d’intérêt d’équilibre, simultanément compatibles avec les deux marchés.',
  x='Cet équilibre ne correspond pas nécessairement au plein-emploi.',
  t='fait', b=361)

c('Quelle relation Phillips met-il en évidence en 1958 ?',
  'Une relation statistique inverse entre le taux de chômage et la variation des salaires nominaux.',
  x='La courbe originelle porte donc sur les salaires, non directement sur le niveau général des prix.',
  t='aut', b=374)

c('Comment Lipsey, Samuelson et Solow transforment-ils la courbe de Phillips ?',
  'Ils la reformulent comme un arbitrage de court terme entre inflation et chômage : réduire l’un accélérerait l’autre.',
  x='Lipsey approfondit l’analyse théorique en 1960, Samuelson et Solow popularisent la version en termes d’inflation la même année.',
  t='aut', b=383)

c('Qu’est-ce que la stagflation, et par quel choc apparaît-elle dans les années 1970 ?',
  'La coexistence d’une inflation élevée, d’une croissance faible et d’un chômage important ; le choc pétrolier de 1973-1974 renchérit une consommation intermédiaire essentielle.',
  x='La hausse des coûts de production permet d’observer simultanément dégradation de l’activité et accélération des prix.',
  t='def', b=394)

c('Quelle critique Friedman adresse-t-il à l’arbitrage inflation-chômage en 1968 ?',
  'Il peut exister à court terme mais disparaît à long terme : une politique monétaire expansionniste ne maintient pas durablement le chômage sous son niveau naturel.',
  x='« L’inflation est toujours et partout un phénomène monétaire » : à long terme la monnaie est neutre dans le cadre monétariste.',
  t='aut', b=406)

c('Que représente le modèle OG-DG, et sur quels axes ?',
  'L’interaction entre offre globale et demande globale, avec le PIB réel en abscisse et le niveau général des prix en ordonnée.',
  x='Il détermine simultanément un niveau de production et un niveau de prix, ce qu’IS-LM à prix fixes ne peut faire.',
  t='def', b=417)

c('Quels effets un choc d’offre négatif produit-il dans le modèle OG-DG ?',
  'La courbe d’offre globale se déplace vers la gauche : le niveau général des prix augmente et la production diminue.',
  x='En 1975, la croissance du PIB est négative en France, à −1,0 %, en même temps qu’une inflation élevée.',
  t='mec', b=429)

c('Vers quels déterminants la stagflation déplace-t-elle l’analyse économique ?',
  'Vers ceux de l’offre : accumulation du capital, progrès technique, capital humain, innovation, infrastructures, productivité.',
  x='La réflexion rejoint les théories de la croissance endogène, dont les travaux de Paul Romer en 1986 sur les externalités de connaissance.',
  t='fait', b=436)

c('Que permet le diagramme à 45° présenté par Samuelson en 1949 ?',
  'Comparer directement le revenu national et la demande globale, et repérer le point où la demande égale la production.',
  x='La fonction de consommation C = C₀ + cY y est tracée face à la bissectrice.',
  t='aut', b=465)

c('Qu’est-ce que la consommation autonome, et à quoi ne faut-il pas la confondre ?',
  'La part de la consommation indépendante du revenu courant dans la fonction retenue ; elle ne correspond pas à un minimum physiologique ni à une consommation incompressible.',
  x='Dans la Théorie générale, Keynes fait dépendre la consommation principalement du revenu courant.',
  t='def', b=473)

c('Que mesure la propension marginale à consommer, et quel est son intervalle ?',
  'La part d’une hausse du revenu consacrée à la consommation, comprise entre 0 et 1.',
  x='Selon la loi psychologique fondamentale, la consommation augmente avec le revenu mais moins que proportionnellement.',
  t='def', b=478)

c('Quelle expression du revenu d’équilibre obtient-on en économie fermée sans État ?',
  'Y = (C₀ + I₀) / (1 − c), en résolvant Y = C₀ + cY + I₀.',
  x='Le revenu dépend donc positivement des dépenses autonomes et d’autant plus fortement que la propension à consommer est élevée.',
  t='form', b=513)

c('Qu’est-ce qu’un équilibre de sous-emploi ?',
  'Une situation où la production égale la demande globale mais reste insuffisante pour employer l’ensemble des travailleurs.',
  x='Le problème n’est pas l’impossibilité d’atteindre l’équilibre, mais le niveau trop faible auquel il se réalise.',
  t='def', b=534, aussi=['3'])

c('Comment le modèle néoclassique explique-t-il le chômage sur le marché du travail ?',
  'Par un salaire réel supérieur au niveau d’équilibre : l’offre de travail excède alors la demande, et cet excès constitue le chômage.',
  x='La flexibilité du salaire réel devrait rétablir le plein emploi ; c’est sa rigidité qui l’empêche.',
  t='mec', b=568)

c('Pourquoi, chez Keynes, une baisse des salaires ne garantit-elle pas le retour au plein emploi ?',
  'Parce que le sous-emploi vient d’une demande globale insuffisante : comprimer les salaires pèse aussi sur les revenus et la consommation.',
  x='Les entreprises n’ont pas intérêt à produire davantage sans débouchés anticipés.',
  t='dist', b=580)

c('Qu’est-ce qu’un écart inflationniste ?',
  'Une situation où la demande globale dépasse les capacités de production de plein emploi, poussant l’économie en surchauffe.',
  x='Le diagramme à 45° suppose des prix fixes : l’interprétation inflationniste suppose de tenir compte des limites des capacités productives.',
  t='def', b=603)

c('Par quel enchaînement une demande excessive engendre-t-elle des tensions sur les prix ?',
  'Les entreprises utilisent plus intensément leurs équipements, embauchent et recourent aux heures supplémentaires ; la main-d’œuvre devenant rare, elles relèvent les salaires.',
  x='Le risque est alors une accélération de l’inflation.',
  t='mec', b=612)

c('Qu’énonce la loi d’Okun établie en 1962 ?',
  'Quand une économie produit moins que son potentiel, le chômage tend à être plus élevé ; une reprise suffisamment forte le réduit.',
  x='Elle porte sur la relation entre production et chômage ; l’interprétation inflationniste d’un écart positif relève d’une autre analyse.',
  t='aut', b=630)

c('Qu’est-ce qu’une prophétie autoréalisatrice en période de récession ?',
  'Une anticipation qui se vérifie par les comportements qu’elle provoque : croyant la demande future faible, les entreprises réduisent leurs dépenses, ce qui la fait effectivement reculer.',
  x='La crise devient alors cumulative, d’où l’idée qu’on ne peut compter sur le seul investissement privé pour en sortir.',
  t='def', b=664)

c('Sur quel enchaînement le multiplicateur keynésien repose-t-il ?',
  'Une dépense initiale crée un revenu, partiellement consommé, qui devient le revenu d’autres agents, et ainsi de suite.',
  x='À chaque étape une part est épargnée, ce qui atténue progressivement le processus sans l’annuler.',
  t='mec', b=706)

c('Qui développe le principe du multiplicateur, et en quelle année ?',
  'Richard Kahn en 1931, à propos des effets de l’investissement sur l’emploi ; Keynes le reprend et le développe en 1936.',
  x='Le multiplicateur est le coefficient mesurant l’effet d’une variation de dépense autonome sur le revenu national.',
  t='aut', b=749)

c('Quel résultat l’exemple des 100 millions consacrés aux lycées illustre-t-il ?',
  'Une dépense initiale de 100 porte le revenu national à 500 dans ce modèle, soit un multiplicateur de 5.',
  x='La commande publique crée d’abord 100 de revenus, dont une partie est consommée, nourrissant les vagues suivantes.',
  t='fait', b=758)

c('Pourquoi le processus multiplicateur ne se poursuit-il pas indéfiniment avec la même intensité ?',
  'Parce que l’épargne constitue une fuite hors du circuit des dépenses de consommation : une part de chaque revenu supplémentaire n’est pas dépensée.',
  x='Avec une propension à consommer de 0,8, la propension à épargner est de 0,2.',
  t='mec', b=780)

c('Quel renversement le multiplicateur opère-t-il entre épargne et investissement ?',
  'L’investissement n’exige pas une épargne préalable équivalente : en élevant les revenus, il engendre lui-même l’épargne qui lui correspond.',
  x='Cela ne signifie pas que les entreprises n’ont pas besoin de financement, mais qu’au niveau macroéconomique l’épargne réalisée s’ajuste.',
  t='dist', b=795)

c('Pourquoi les trois instruments budgétaires n’ont-ils pas le même multiplicateur ?',
  'Une dépense publique entre directement dans la demande globale, tandis qu’une prestation ou une baisse d’impôt accroît d’abord le revenu disponible, dont une partie est épargnée.',
  x='Les trois soutiennent la demande, mais leur transmission à la production diffère.',
  t='dist', b=743)

c('Quelle est la formule du multiplicateur de dépenses publiques, et sa valeur pour c = 0,8 ?',
  'k = 1 / (1 − c), soit 5 : une dépense de 100 porte le revenu national à 500.',
  x='Les dépenses publiques entrent directement dans la demande globale dès la première vague.',
  t='form', b=864)

c('Quelle est la formule du multiplicateur des prestations sociales, et sa valeur pour c = 0,8 ?',
  'k = c / (1 − c), soit 4 : une hausse de 100 accroît le revenu national de 400.',
  x='La première vague de demande n’est que de 80, puisque 20 sont épargnés.',
  t='form', b=893)

c('Pourquoi le multiplicateur des prestations sociales est-il inférieur à celui des dépenses publiques ?',
  'Parce que le transfert passe d’abord par le revenu disponible des ménages, qui n’en consomment qu’une partie.',
  x='La différence vient donc de la toute première vague : 100 contre 80 avec une propension à consommer de 0,8.',
  t='dist', b=900)

c('Quelle est la formule du multiplicateur fiscal, et comment interpréter son signe ?',
  'k = −c / (1 − c) : le signe négatif signifie qu’une hausse des prélèvements réduit le revenu national, et qu’une baisse l’augmente.',
  x='Avec c = 0,8, une réduction d’impôts de 100 millions accroît le revenu national de 400 millions.',
  t='form', b=934)

c('Quelle hiérarchie des multiplicateurs le modèle simple établit-il ?',
  'Dépenses publiques en premier, avec 500 pour 100 dépensés, puis prestations sociales et baisse d’impôts, avec 400 chacune.',
  x='Les transferts et allègements transitent par le revenu disponible, dont une part est épargnée avant la première vague de consommation.',
  t='fait', b=957)

c('Pourquoi une politique keynésienne ne se réduit-elle pas à soutenir la consommation ?',
  'Parce qu’elle peut reposer prioritairement sur l’investissement public, qui crée directement des débouchés puis des vagues de revenus.',
  x='Dans le modèle simple, le multiplicateur est le même pour une dépense de consommation et d’investissement publics ; l’investissement accroît en outre les capacités futures.',
  t='dist', b=966)

c('Pourquoi cibler les ménages modestes renforce-t-il l’efficacité d’une relance ?',
  'Parce que leur propension marginale à consommer est plus élevée : une même somme se transforme en davantage de demande.',
  x='Une redistribution verticale peut ainsi poursuivre à la fois un objectif social et un objectif conjoncturel.',
  t='mec', b=995)

c('Que mesure la propension marginale à importer, et à quoi ne faut-il pas la confondre ?',
  'L’augmentation des importations provoquée par une unité supplémentaire de revenu ; elle se distingue du ratio importations sur PIB, qui mesure un poids.',
  x='Avec une valeur de 0,3, une hausse du revenu de 100 accroît les importations de 30.',
  t='def', b=1042)

c('Comment s’écrit le multiplicateur en économie ouverte ?',
  'k = 1 / (1 − c + m) : la propension marginale à importer apparaît au dénominateur et réduit donc le multiplicateur.',
  x='Plus la demande supplémentaire se porte sur l’étranger, plus l’effet sur la production nationale est faible.',
  t='form', b=1062)

c('De combien l’ouverture fait-elle passer le multiplicateur dans l’application numérique du cours ?',
  'De 5 à 2 : une dépense initiale de 100 n’engendre plus 500 de revenu supplémentaire mais 200.',
  x='Les importations constituent une seconde fuite, qui s’ajoute à l’épargne.',
  t='fait', b=1068)

c('Quel argument protectionniste la baisse du multiplicateur en économie ouverte nourrit-elle, et quelles limites ?',
  'Limiter les importations retiendrait la relance sur le territoire ; mais les restrictions renchérissent les intrants, pénalisent les entreprises importatrices et appellent des représailles.',
  x='Une coordination internationale des relances répond autrement au problème : les importations des uns sont les exportations des autres.',
  t='dist', b=1086)

c('Qu’est-ce que la dichotomie classique, et où le taux d’intérêt y est-il déterminé ?',
  'La sphère réelle détermine production, emploi et échanges, la sphère monétaire le niveau général des prix ; le taux d’intérêt se forme sur le marché des fonds prêtables.',
  x='La monnaie n’y est qu’un instrument de transaction, non un actif recherché pour lui-même.',
  t='dist', b=1124)

c('Qu’est-ce que la préférence pour la liquidité chez Keynes ?',
  'Le fait de conserver de la monnaie, actif parfaitement liquide, plutôt que de placer toute son épargne dans des titres à convertir et à risque de valeur.',
  x='Le taux d’intérêt devient alors le prix de la renonciation à la liquidité, déterminé sur le marché de la monnaie.',
  t='def', b=1134)

c('De quoi dépend la demande de monnaie pour motif de transaction ?',
  'Positivement du revenu national : une économie qui produit et échange davantage réalise plus de paiements.',
  x='Le motif de précaution, lié aux dépenses imprévues, dépend lui aussi positivement du revenu.',
  t='mec', b=1160)

c('Comment le prix d’une obligation varie-t-il avec le taux d’intérêt ?',
  'En sens inverse : si les nouvelles émissions offrent un meilleur rendement, le cours de l’ancien titre doit baisser pour rester attractif.',
  x='C’est l’« effet balançoire » ; il faut distinguer le coupon, fixe, du prix de marché et du rendement de marché.',
  t='mec', b=1210)

c('Pourquoi la demande spéculative de monnaie est-elle faible quand le taux d’intérêt est élevé ?',
  'Parce que les agents anticipent sa baisse, donc une plus-value sur les obligations : ils achètent des titres et réduisent leurs encaisses.',
  x='Le raisonnement s’inverse quand le taux est jugé exceptionnellement bas : on craint une moins-value et on garde la monnaie.',
  t='mec', b=1230)

c('Qu’est-ce que la trappe à liquidité ?',
  'Une situation où les taux sont si faibles que les agents préfèrent détenir de la monnaie, anticipant une remontée des taux et donc des pertes en capital sur les obligations.',
  x='La demande spéculative devient alors extrêmement sensible au taux, jusqu’à absorber toute monnaie supplémentaire.',
  t='def', b=1261, aussi=['2'])

c('Pourquoi la trappe à liquidité limite-t-elle la politique monétaire conventionnelle ?',
  'La monnaie supplémentaire est conservée en encaisses, le taux ne baisse plus sensiblement, l’investissement n’est pas stimulé et la demande ne progresse pas par ce canal.',
  x='Cela ne condamne pas toutes les formes de politique monétaire, mais le canal du taux directeur devient inopérant.',
  t='mec', b=1269)

c('Comment s’écrit la demande totale de monnaie dans le modèle keynésien ?',
  'L = L1(Y) + L2(r) : une composante liée positivement au revenu, pour les transactions et la précaution, et une composante liée négativement au taux d’intérêt, pour la spéculation.',
  x='L’offre de monnaie est, elle, supposée exogène, fixée par les autorités monétaires.',
  t='form', b=1293)

c('Qu’est-ce qu’une variable exogène, et comment l’offre de monnaie est-elle traitée dans IS-LM ?',
  'Une variable dont la valeur est déterminée en dehors du modèle ; l’offre de monnaie y est fixée par les autorités, donc représentée par une droite verticale.',
  x='C’est une simplification : les systèmes contemporains reposent aussi sur la création monétaire bancaire.',
  t='def', b=1300)

c('Par quel enchaînement une hausse de l’offre de monnaie fait-elle baisser le taux d’intérêt ?',
  'Les agents détiennent plus de monnaie qu’ils ne le souhaitent, achètent des titres, dont le prix monte, ce qui abaisse leur rendement de marché.',
  x='Une politique monétaire expansionniste réduit donc normalement le taux d’équilibre.',
  t='mec', b=1309)

c('Pourquoi une hausse du revenu élève-t-elle le taux d’intérêt à offre de monnaie constante ?',
  'Les agents, voulant accroître leurs encaisses, vendent des titres : l’offre de titres augmente, leur prix baisse et leur rendement monte.',
  x='C’est ce mécanisme qui donne à la courbe LM sa pente croissante.',
  t='mec', b=1334)

c('De quoi dépend la pente de la courbe LM ?',
  'Du rapport entre la sensibilité de la demande de monnaie au revenu et sa sensibilité au taux d’intérêt.',
  x='Plus la demande spéculative réagit au taux, plus LM est plate ; plus les besoins de transaction croissent avec le revenu, plus elle est pentue.',
  t='mec', b=1374)

c('Quelles trois configurations la courbe LM peut-elle présenter ?',
  'Horizontale dans la trappe à liquidité, croissante en situation normale, verticale dans la zone dite classique.',
  x='Dans la zone classique, la demande spéculative est négligeable : le revenu compatible avec l’équilibre monétaire est fixé.',
  t='fait', b=1414)

c('Quelle politique reste efficace dans la phase horizontale de LM ?',
  'La politique budgétaire : elle peut accroître le revenu sans provoquer de hausse du taux d’intérêt.',
  x='La politique monétaire conventionnelle, elle, ne parvient plus à abaisser davantage les taux.',
  t='dist', b=1396)

c('Pourquoi un équilibre IS-LM peut-il coexister avec du chômage involontaire ?',
  'Parce que la demande globale peut rester insuffisante : les deux marchés sont équilibrés à un niveau de production inférieur au plein emploi.',
  x='C’est le prolongement, dans le modèle, de l’équilibre de sous-emploi keynésien.',
  t='dist', b=1455)

c('Quelle courbe chaque politique conjoncturelle déplace-t-elle dans le modèle IS-LM ?',
  'La politique budgétaire déplace IS, en agissant sur la demande globale ; la politique monétaire déplace LM, en agissant sur les conditions monétaires.',
  x='Leur efficacité dépend de la réaction de l’investissement et de la demande de monnaie au taux d’intérêt.',
  t='dist', b=1476)

c('Qu’est-ce que l’effet d’éviction dans le modèle IS-LM ?',
  'La réduction de l’investissement privé provoquée par la hausse du taux d’intérêt consécutive à une relance budgétaire.',
  x='Le revenu augmente donc moins que si le taux était resté constant : la baisse de l’investissement compense une partie de la stimulation.',
  t='def', b=1506)

c('Dans quels cas l’effet d’éviction est-il le plus fort, et quand disparaît-il ?',
  'Il est fort quand LM est très pentue ou quand l’investissement est très sensible au taux ; il est nul quand LM est horizontale, dans une trappe à liquidité.',
  x='La politique budgétaire devient donc particulièrement efficace en trappe à liquidité.',
  t='dist', b=1521)

c('Par quel enchaînement une politique monétaire expansionniste stimule-t-elle le revenu ?',
  'La hausse de l’offre de monnaie abaisse le taux d’intérêt, ce qui rend des projets rentables, accroît l’investissement, donc la demande globale et la production.',
  x='Le multiplicateur amplifie l’effet initial ; LM se déplace vers la droite et l’équilibre associe taux plus bas et revenu plus élevé.',
  t='mec', b=1557)

c('Pourquoi la politique monétaire devient-elle inefficace en trappe à liquidité ?',
  'Parce que les agents absorbent toute monnaie supplémentaire : le taux ne baisse plus significativement et l’investissement n’est pas stimulé.',
  x='La politique budgétaire, elle, accroît le revenu sans hausse des taux : il n’y a pas d’éviction.',
  t='mec', b=1612)

c('Pourquoi la politique budgétaire est-elle inefficace dans la zone classique ?',
  'Parce que LM étant verticale, le revenu ne peut augmenter à offre de monnaie constante : l’ajustement se fait par une forte hausse du taux, et l’éviction devient totale.',
  x='Seule la politique monétaire, en déplaçant LM, peut alors élever le revenu d’équilibre.',
  t='mec', b=1622)

c('Qu’est-ce que le policy mix ?',
  'La combinaison des politiques budgétaire et monétaire, qui peuvent agir dans le même sens, en sens opposés, ou se compléter pour limiter leurs effets indésirables.',
  x='L’objectif général est de stabiliser l’activité : soutenir la demande en récession, la freiner en surchauffe.',
  t='def', b=1648)

c('Quels trois objectifs une politique budgétaire restrictive peut-elle poursuivre ?',
  'Contenir une surchauffe inflationniste, réduire un déficit extérieur en freinant les importations, et consolider les finances publiques.',
  x='Il faut distinguer l’objectif de consolidation de ses effets restrictifs sur l’activité.',
  t='fait', b=1689)

c('Qu’est-ce qui distingue une politique contracyclique d’une politique procyclique ?',
  'La première agit en sens opposé à la conjoncture spontanée pour atténuer les fluctuations ; la seconde l’accompagne et les amplifie.',
  x='Relancer alors que l’économie est déjà en forte expansion est procyclique, donc contradictoire avec l’objectif de stabilisation.',
  t='dist', b=1710)

c('Pourquoi le déplacement de la courbe IS provoqué par une politique budgétaire est-il parallèle ?',
  'Parce que les comportements des agents, qui déterminent la pente, sont supposés inchangés : seule la position de la courbe se modifie.',
  x='Retenir la correspondance : IS pour la politique budgétaire, LM pour la politique monétaire.',
  t='mec', b=1744)

c('Pourquoi associer une relance budgétaire à une politique monétaire accommodante ?',
  'Pour éviter que la hausse de la demande de monnaie n’élève le taux d’intérêt et n’évince l’investissement privé.',
  x='La banque centrale déplace LM vers la droite, ce qui permet de soutenir davantage l’activité sans tension excessive sur les taux.',
  t='mec', b=1782)

c('Quelle amélioration du solde budgétaire américain observe-t-on entre 1992 et 1998 ?',
  'Le passage d’un déficit de 4,5 % du PIB à un excédent de 0,8 %, avec une croissance de 2,7 % puis 3,7 %.',
  x='Les taux à un an reculent de 5,5 % à 4,8 % : la consolidation n’a pas provoqué de récession.',
  t='fait', b=1813)

c('Quelle configuration de policy mix le cas Clinton-Greenspan illustre-t-il ?',
  'Une consolidation budgétaire — IS vers la gauche — compensée par une orientation monétaire plus accommodante — LM vers la droite.',
  x='Le cours précise qu’il s’agit d’une illustration simplifiée : les taux américains ont connu plusieurs phases et la croissance dépendait d’autres facteurs.',
  t='dist', b=1825)

c('Quelle combinaison de politiques la réunification allemande de 1990 illustre-t-elle ?',
  'Une politique budgétaire expansionniste, pour financer l’intégration, associée à une politique monétaire restrictive de la Bundesbank contre la surchauffe.',
  x='Les deux poursuivent des objectifs différents : soutenir l’activité d’un côté, contenir l’inflation de l’autre.',
  t='dist', b=1853)

c('Quels chiffres allemands traduisent la tension entre les deux politiques entre 1989 et 1991 ?',
  'Le solde budgétaire passe de +0,2 % du PIB à −2,9 %, les taux courts de 7,1 % à 9,2 %, et la croissance de 4,5 % en 1990 à 3,1 % en 1991.',
  x='L’investissement bondit de 10,5 % en 1990 avant de ralentir à 6,7 %.',
  t='fait', b=1874)

c('Quelle asymétrie institutionnelle caractérise le policy mix de la zone euro ?',
  'Les politiques budgétaires restent nationales, encadrées par des règles européennes, tandis que la politique monétaire est unique et décidée par la BCE.',
  x='La difficulté vient de ce que les États ne connaissent pas la même conjoncture.',
  t='dist', b=1897)

c('Quelle critique keynésienne est adressée au modèle IS-LM de Hicks et Hansen ?',
  'D’avoir privilégié l’équilibre au détriment de l’incertitude, des anticipations et du caractère dynamique du processus économique.',
  x='Le modèle appartient à l’économie de la synthèse, qui cherche à représenter Keynes dans un cadre d’équilibre.',
  t='dist', b=1919)

c('Que signifient ex ante et ex post à propos de l’épargne et de l’investissement ?',
  'Ex ante, les décisions d’investir et d’épargner, prises par des agents différents, peuvent diverger ; ex post, les grandeurs réalisées sont rendues compatibles par les ajustements.',
  x='L’égalité comptable ne dit donc rien de la coordination des projets initiaux.',
  t='dist', b=1925)

c('Pourquoi l’hypothèse de prix fixes devient-elle une limite majeure du modèle IS-LM ?',
  'Parce qu’elle empêche de représenter l’inflation et la déflation, alors que les chocs pétroliers des années 1970 mettent les prix au premier plan.',
  x='Le modèle OG-DG est alors mobilisé pour représenter simultanément production et niveau des prix.',
  t='dist', b=1963)

c('Quels trois mécanismes les monétaristes et nouveaux classiques opposent-ils à la relance budgétaire ?',
  'L’effet d’éviction, le revenu permanent et l’équivalence ricardienne.',
  x='Ils ne contestent pas seulement la fidélité du modèle à Keynes, mais l’efficacité même des politiques conjoncturelles.',
  t='fait', b=1982)

c('De quoi dépend l’intensité de l’effet d’éviction ?',
  'Des conditions monétaires, de la sensibilité de l’investissement au taux d’intérêt et de la situation de l’économie.',
  x='Elle n’est donc pas nécessairement totale ; une politique monétaire accommodante peut la neutraliser.',
  t='fait', b=2005)

c('Qu’est-ce que le revenu permanent chez Friedman ?',
  'Le revenu moyen de long terme que les ménages anticipent percevoir durablement, et sur lequel ils calent leur consommation.',
  x='Référence : A Theory of the Consumption Function, 1957. Un revenu exceptionnel ne modifie donc pas fortement la consommation.',
  t='def', b=2042)

c('Pourquoi une aide exceptionnelle a-t-elle, selon Friedman, un effet multiplicateur réduit ?',
  'Jugée temporaire, elle ne modifie pas le revenu permanent anticipé : elle est donc largement épargnée.',
  x='Les ménages contraints financièrement peuvent toutefois en consommer une part importante : tout dépend du caractère anticipé comme durable.',
  t='mec', b=2046)

c('Qu’énonce l’équivalence ricardienne formulée par Barro en 1974 ?',
  'Des ménages rationnels épargnent une baisse d’impôts financée par la dette, anticipant la hausse future des prélèvements : la demande globale n’est pas stimulée.',
  x='L’augmentation de l’épargne privée compense exactement la réduction de l’épargne publique dans la version stricte.',
  t='aut', b=2062)

c('Quelles hypothèses fortes l’équivalence ricardienne exige-t-elle ?',
  'Que les ménages anticipent les conséquences budgétaires, puissent épargner, raisonnent à long horizon et ne soient pas contraints par leur revenu courant.',
  x='Un ménage modeste consommera immédiatement une aide pour satisfaire des besoins essentiels : la proposition n’est pas une loi universelle.',
  t='fait', b=2086)

c('Qu’est-ce que le taux de chômage naturel chez Friedman ?',
  'Le taux vers lequel l’économie tend compte tenu du fonctionnement du marché du travail : frictions, adéquation des qualifications, institutions, formation des salaires.',
  x='Il n’est pas immuable, mais ne peut être durablement abaissé par une simple stimulation de la demande.',
  t='def', b=2109, aussi=['3'])

c('Par quel enchaînement une relance monétaire ramène-t-elle l’économie à son chômage naturel ?',
  'Les agents sous-estiment d’abord la hausse des prix, puis adaptent leurs anticipations : les salariés réclament des hausses nominales et les entreprises révisent leurs prix.',
  x='L’économie revient à son taux naturel, mais avec un niveau de prix plus élevé : à long terme les effets sont nominaux.',
  t='mec', b=2124)

c('Comment la critique monétariste explique-t-elle l’échec d’une relance au plein emploi ?',
  'La hausse des prix réduit l’offre réelle de monnaie, LM se déplace vers la gauche, le taux d’intérêt monte et évince l’investissement privé.',
  x='L’économie revient à sa production potentielle, mais avec un taux d’intérêt plus élevé.',
  t='mec', b=2148)

c('Qu’est-ce qui distingue une politique conjoncturelle d’une politique structurelle ?',
  'La première agit à court terme sur la demande globale ; la seconde modifie durablement les capacités de production — formation, innovation, infrastructures, fonctionnement des marchés.',
  x='Quand l’économie est contrainte par sa production potentielle, seules les politiques structurelles élèvent ce que l’économie peut produire.',
  t='dist', b=2175, aussi=['1'])

c('Quel paradoxe apparent la position de Barro présente-t-elle ?',
  'Il critique l’efficacité de la relance budgétaire conjoncturelle, mais reconnaît en 1990 que les infrastructures publiques contribuent à la croissance de long terme.',
  x='Critiquer la relance ne revient donc pas à refuser toute intervention publique.',
  t='aut', b=2197)

c('Pourquoi la crise de 2008 a-t-elle réhabilité le modèle IS-LM ?',
  'Parce qu’elle a ramené au premier plan la trappe à liquidité : les taux très bas ont rendu les injections de liquidités peu efficaces pour relancer l’activité.',
  x='La politique budgétaire y retrouve de l’efficacité, l’effet d’éviction devenant très limité.',
  t='mec', b=2218)

c('À quelle question chacun des trois modèles macroéconomiques répond-il ?',
  'IS-LM : l’effet des politiques de demande en économie fermée ; OG-DG : les variations conjointes de la production et des prix ; IS-LM-BP : les politiques en économie ouverte.',
  x='Les modèles ne sont donc pas concurrents mais complémentaires.',
  t='fait', b=2249)

c('Quels éléments l’ouverture oblige-t-elle à intégrer dans le modèle IS-LM ?',
  'Les exportations, les importations, les mouvements internationaux de capitaux, les variations du taux de change et les interventions des banques centrales.',
  x='La courbe BP représente alors les conditions de l’équilibre extérieur.',
  t='fait', b=2311)

c('Quelles trois conditions une économie ouverte doit-elle satisfaire simultanément dans Mundell-Fleming ?',
  'L’équilibre du marché des biens et services, celui du marché de la monnaie, et l’équilibre extérieur.',
  x='Fleming publie en 1962, Mundell en 1963 : IS, LM et BP doivent se couper en un même point.',
  t='fait', b=2365)

c('Qu’enregistre la balance des paiements, et pourquoi son équilibre comptable ne suffit-il pas ?',
  'Les transactions entre résidents et reste du monde, réparties en transactions courantes, compte de capital et compte financier ; elle est équilibrée par construction, mais ses soldes intermédiaires peuvent être déséquilibrés.',
  x='La courbe BP représente un équilibre économique, non cette identité comptable.',
  t='def', b=2380)

c('Que représente la balance globale dans le modèle simplifié ?',
  'La somme du solde courant et du solde des mouvements autonomes de capitaux.',
  x='Les opérations sur réserves officielles, certains dérivés et le compte de capital sont laissés de côté dans le raisonnement élémentaire.',
  t='def', b=2392)

c('Un déficit courant de 100 compensé par 60 d’entrées de capitaux donne quelle balance globale ?',
  'Un déficit global de 40 : −100 + 60 = −40.',
  x='Avec 100 d’entrées la balance globale serait équilibrée, avec 140 excédentaire : tout dépend des mouvements de capitaux.',
  t='fait', b=2418)

c('Un pays en excédent courant peut-il présenter un déficit de balance globale ?',
  'Oui : avec un excédent de 100 et des sorties de capitaux de 140, la balance globale est déficitaire de 40.',
  x='Un excédent courant est une capacité de financement, employée à acquérir des actifs étrangers ou à prêter au reste du monde.',
  t='dist', b=2435)

c('Pourquoi la courbe BP est-elle croissante ?',
  'Parce qu’une hausse du revenu accroît les importations et dégrade le solde courant : il faut un taux d’intérêt plus élevé pour attirer les capitaux qui le financent.',
  x='À taux inchangé, un revenu plus élevé place donc l’économie sous la courbe BP.',
  t='mec', b=2481)

c('Que signifient les positions au-dessus et au-dessous de la courbe BP ?',
  'Au-dessus, la balance globale est excédentaire, le taux attirant plus de capitaux que nécessaire ; au-dessous, elle est déficitaire, le taux étant insuffisant.',
  x='Sur la courbe, les mouvements de capitaux compensent exactement le solde courant.',
  t='dist', b=2514)

c('De quoi dépend la pente de la courbe BP ?',
  'De la sensibilité des mouvements internationaux de capitaux aux écarts de rendement : forte mobilité, courbe plate ; faible mobilité, courbe pentue.',
  x='Quand les capitaux circulent mal, il faut relever davantage le taux pour obtenir les mêmes entrées.',
  t='mec', b=2529)

c('Quelles formes BP prend-elle en mobilité parfaite et en immobilité totale des capitaux ?',
  'Horizontale en mobilité parfaite, le taux domestique s’alignant sur le taux international ; verticale en immobilité totale, l’équilibre extérieur dépendant alors du seul revenu.',
  x='Ces deux cas sont des hypothèses théoriques : la réalité comporte des frictions, risques de change, coûts de transaction, risques de défaut.',
  t='dist', b=2571)

c('Pourquoi la mobilité des capitaux était-elle encadrée après la Seconde Guerre mondiale ?',
  'Parce que les États cherchaient, dans le système de Bretton Woods, à préserver leur autonomie monétaire, ce que les contrôles de capitaux facilitaient.',
  x='La situation change à partir des années 1970 et surtout 1980 avec la globalisation financière.',
  t='mec', b=2604)

c('Quels sont les trois D de la globalisation financière selon Henri Bourguinat ?',
  'Déréglementation, décloisonnement et désintermédiation.',
  x='Réduction des restrictions réglementaires, interconnexion des marchés auparavant séparés, et financements directs au-delà du crédit bancaire.',
  t='aut', b=2621)

c('Pourquoi un équilibre interne ne garantit-il pas l’équilibre extérieur ?',
  'Parce que IS et LM peuvent se couper en dehors de BP : l’économie est alors en déficit ou en excédent de balance globale.',
  x='Un mécanisme d’ajustement est donc nécessaire, et il dépend du régime de change.',
  t='dist', b=2656)

c('Comment une dépréciation rétablit-elle l’équilibre extérieur en changes flexibles ?',
  'Elle rend les biens nationaux moins chers pour l’étranger et les produits importés plus chers, ce qui améliore le solde et déplace IS vers la droite.',
  x='L’ajustement dépend des élasticités-prix, des délais et du contenu importé des exportations : à court terme la balance peut se dégrader, c’est l’effet de courbe en J.',
  t='mec', b=2679)

c('Que doit faire une banque centrale en changes fixes face à un déficit extérieur ?',
  'Acheter sa propre monnaie en vendant des devises prélevées sur ses réserves, ce qui réduit l’offre de monnaie et déplace LM vers la gauche.',
  x='Le déficit extérieur peut donc imposer une politique monétaire restrictive, même si l’activité est déjà insuffisante.',
  t='mec', b=2714)

c('Quel effet monétaire un excédent extérieur produit-il en changes fixes ?',
  'Pour empêcher l’appréciation, la banque centrale vend sa monnaie et achète des devises : la liquidité domestique augmente et LM se déplace vers la droite.',
  x='Les banques centrales peuvent toutefois stériliser ces effets ; le modèle simplifié les suppose directs.',
  t='mec', b=2728)

c('Quelles quatre configurations le croisement des équilibres interne et externe fait-il apparaître ?',
  'Sous-emploi avec excédent, sous-emploi avec déficit, inflation avec déficit, inflation avec excédent.',
  x='Deux de ces situations n’opposent pas les objectifs, les deux autres constituent de véritables dilemmes.',
  t='fait', b=2776)

c('Pourquoi sous-emploi et déficit extérieur constituent-ils un dilemme ?',
  'Relancer pour réduire le chômage accroît les importations et creuse le déficit ; freiner la demande pour corriger le déficit aggrave le chômage.',
  x='C’est l’expression de la contrainte extérieure pesant sur les politiques keynésiennes de relance.',
  t='mec', b=2809)

c('Pourquoi inflation et déficit extérieur ne posent-ils pas de dilemme majeur ?',
  'Parce qu’une politique restrictive contient simultanément les tensions sur les prix et réduit les importations.',
  x='Une même orientation corrige donc les deux déséquilibres.',
  t='dist', b=2830)

c('Pourquoi inflation et excédent extérieur constituent-ils un dilemme ?',
  'Freiner la demande pour contenir les prix réduit les importations et gonfle encore l’excédent ; relancer pour résorber l’excédent aggrave l’inflation.',
  x='Le cours évoque les économies structurellement excédentaires d’Europe du Nord, en particulier l’Allemagne.',
  t='mec', b=2841)

c('Quelle simplification Jacques Généreux propose-t-il en 2016 pour analyser les dilemmes ?',
  'Comparer le revenu de plein emploi au revenu qui équilibre les transactions courantes, sans tenir compte du rôle compensateur des mouvements de capitaux.',
  x='Cette représentation n’est donc pas celle de la courbe BP, mais elle éclaire les déséquilibres courants persistants.',
  t='aut', b=2854)

c('Que signifie, chez Généreux, un revenu d’équilibre courant inférieur au revenu de plein emploi ?',
  'L’économie est structurellement déficitaire : entre les deux niveaux elle connaît encore du sous-emploi tout en présentant déjà un déficit courant.',
  x='Le cas inverse, revenu d’équilibre courant supérieur au plein emploi, décrit une économie structurellement excédentaire.',
  t='dist', b=2866)

c('Qu’appelle-t-on contrainte extérieure ?',
  'Les limites imposées aux politiques nationales par la nécessité de préserver l’équilibre des échanges et la stabilité monétaire.',
  x='Une politique souhaitable pour l’emploi peut être insoutenable au regard du déficit extérieur ou des mouvements de capitaux.',
  t='def', b=2899)

c('En quoi consistait la relance française de 1981 ?',
  'Une hausse du SMIC, une revalorisation des prestations sociales et des créations d’emplois publics, pour soutenir le pouvoir d’achat et l’activité.',
  x='Engagée par le gouvernement de Pierre Mauroy après l’élection de François Mitterrand en mai 1981.',
  t='fait', b=2911)

c('Quel niveau d’inflation la France connaissait-elle au moment de la relance de 1981 ?',
  'Environ 13 % en 1981 et 12 % en 1982.',
  x='La croissance des partenaires commerciaux était par ailleurs faible : la relance intervenait dans un environnement défavorable.',
  t='fait', b=2928)

c('Pourquoi la relance de 1981 a-t-elle dégradé les transactions courantes françaises ?',
  'Parce qu’une partie de la demande supplémentaire s’est portée sur des biens étrangers, et qu’aucune relance équivalente n’avait lieu chez les partenaires.',
  x='L’effet multiplicateur a donc partiellement profité aux économies voisines.',
  t='mec', b=2930)

c('Comment le Système monétaire européen a-t-il transformé le déficit français en crise de change ?',
  'Les parités étant fixes mais ajustables, le franc ne pouvait se déprécier librement : les anticipations de dévaluation ont nourri les ventes de francs.',
  x='La France procède à plusieurs dévaluations entre 1981 et 1983.',
  t='mec', b=2939)

c('Qu’est-ce que le cercle vicieux de la monnaie faible ?',
  'Une dévaluation renchérit les importations, nourrit l’inflation, dégrade à nouveau la compétitivité et alimente les anticipations de nouvelles dévaluations.',
  x='L’effet d’une dévaluation dépend pourtant de la réaction des volumes : elle ne dégrade pas nécessairement durablement la balance commerciale.',
  t='mec', b=2952)

c('Que décide le gouvernement français en mars 1983, et avec quelles conséquences ?',
  'Maintenir le franc dans le Système monétaire européen, ce qui implique d’abandonner la relance au profit d’une orientation restrictive.',
  x='Priorité donnée à la défense de la monnaie, à la désinflation et à la crédibilité financière, au prix d’un chômage plus difficile à réduire.',
  t='fait', b=2964)

c('Comment les changes flexibles peuvent-ils atténuer le dilemme sous-emploi / déficit extérieur ?',
  'La monnaie se déprécie, ce qui accroît la demande adressée aux producteurs nationaux et réduit simultanément le déficit.',
  x='Le taux de change devient un instrument d’ajustement, ce qu’il ne peut être en changes fixes.',
  t='mec', b=2995)

c('Pourquoi la flexibilité des changes ne supprime-t-elle pas toutes les contraintes extérieures ?',
  'Parce que les mouvements de capitaux restent importants et instables, et qu’une dépréciation renchérit les importations, nourrit l’inflation importée et alourdit une dette libellée en devises.',
  x='La compétitivité-prix n’est en outre pas le seul déterminant des exportations : capacités, adaptation des produits et compétitivité hors prix comptent aussi.',
  t='dist', b=3019)

c('Quelle contradiction le cas japonais met-il en évidence en changes flexibles ?',
  'Des taux faibles soutiennent l’activité mais réduisent l’attractivité des placements en yens, ce qui déprécie la monnaie et renchérit les importations.',
  x='Relever les taux pour soutenir le change freinerait au contraire la demande intérieure.',
  t='mec', b=3036)

c('Comment s’écrit le multiplicateur des dépenses publiques avec fiscalité proportionnelle et ouverture ?',
  'k = 1 / [1 − c(1 − t) + m], où c est la propension à consommer, t le taux d’imposition et m la propension à importer.',
  x='Deux fuites s’ajoutent donc à l’épargne : les prélèvements et les importations.',
  t='form', b=3076)

c('Qu’est-ce qu’un effet de débordement international d’une relance ?',
  'Une partie de la demande supplémentaire se porte sur les produits des partenaires, dont la production et les revenus augmentent, et qui importent à leur tour.',
  x='La relance d’un pays stimule donc l’activité de ses voisins.',
  t='def', b=3087)

c('Quel comportement de passager clandestin l’interdépendance commerciale encourage-t-elle ?',
  'Attendre que le partenaire relance, pour bénéficier de la demande extérieure sans supporter le coût budgétaire.',
  x='Si tous attendent, aucune relance suffisante n’est engagée et la demande globale reste insuffisante.',
  t='mec', b=3097)

c('Pourquoi la coordination internationale renforce-t-elle l’efficacité des relances ?',
  'Parce que les fuites par les importations deviennent partiellement des effets de retour : chacun stimule à la fois sa demande intérieure et les exportations des autres.',
  x='L’enjeu est décisif dans une zone fortement intégrée comme l’Union européenne.',
  t='mec', b=3105)

c('Pourquoi la politique monétaire est-elle inefficace en changes fixes avec mobilité parfaite des capitaux ?',
  'La baisse du taux sous le niveau mondial provoque des sorties de capitaux ; pour défendre la parité, la banque centrale rachète sa monnaie et ramène LM à sa position initiale.',
  x='Le revenu revient à son point de départ : l’expansion monétaire est entièrement neutralisée.',
  t='mec', b=3131)

c('Pourquoi la politique budgétaire est-elle très efficace en changes fixes avec mobilité parfaite des capitaux ?',
  'La hausse du taux attire des capitaux ; pour empêcher l’appréciation, la banque centrale achète des devises et émet de la monnaie, ce qui déplace LM vers la droite.',
  x='La défense de la parité amplifie donc la relance : le revenu final est plus élevé et le taux revient au niveau mondial.',
  t='mec', b=3164)

c('Quels trois objectifs le triangle des incompatibilités de Mundell met-il en concurrence ?',
  'La stabilité du taux de change, la libre circulation des capitaux et l’autonomie de la politique monétaire.',
  x='On parle aussi de trinité impossible : deux objectifs peuvent être tenus, jamais les trois.',
  t='aut', b=3223)

c('À quoi un pays doit-il renoncer en choisissant changes fixes et libre circulation des capitaux ?',
  'À l’autonomie monétaire : toute baisse du taux provoque des sorties de capitaux que la défense de la parité contraint à neutraliser.',
  x='La politique monétaire devient subordonnée à la stabilité du change.',
  t='dist', b=3248)

c('Que permet la combinaison changes flexibles et libre circulation des capitaux ?',
  'De conserver l’autonomie monétaire : la banque centrale n’a pas à défendre une parité et peut laisser la monnaie se déprécier.',
  x='Cette autonomie s’accompagne en revanche d’une exposition aux fluctuations du taux de change.',
  t='dist', b=3267)

c('À quelle condition un pays peut-il tenir changes fixes et autonomie monétaire ?',
  'En contrôlant les mouvements internationaux de capitaux, ce qui limite les sorties et entrées provoquées par les écarts de taux.',
  x='C’est la logique du système de Bretton Woods : changes fixes mais ajustables et contrôles de capitaux.',
  t='dist', b=3286)

c('Comment le triangle de Mundell éclaire-t-il la fin du système de Bretton Woods ?',
  'La montée de la mobilité des capitaux rendait intenable la combinaison changes fixes et autonomie monétaire que les contrôles permettaient.',
  x='Les États-Unis suspendent la convertibilité du dollar en or en août 1971, et les principales monnaies flottent à partir de 1973.',
  t='mec', b=3306)

c('Par quels deux canaux la politique monétaire agit-elle en changes flexibles ?',
  'Par le taux d’intérêt, qui stimule l’investissement, et par le taux de change, dont la dépréciation accroît les exportations nettes.',
  x='La banque centrale n’ayant pas de parité à défendre, elle ne doit pas annuler sa création monétaire : la relance est durable dans le modèle.',
  t='mec', b=3366)

c('Pourquoi la politique budgétaire devient-elle inefficace en changes flexibles avec mobilité parfaite ?',
  'La hausse du taux attire des capitaux, ce qui apprécie la monnaie, dégrade les exportations nettes et neutralise la relance.',
  x='IS, d’abord déplacée vers la droite, est ramenée en arrière par la perte de compétitivité.',
  t='mec', b=3403)

c('Qu’appelle-t-on effet d’éviction par le taux de change ?',
  'La substitution d’une dépense publique supplémentaire à une partie de la demande extérieure nette, l’appréciation réduisant les exportations nettes.',
  x='La relance stimule bien la demande intérieure, mais ce gain est annulé par la perte de demande extérieure.',
  t='def', b=3453)

c('Que montre le tableau de synthèse de Mundell-Fleming en mobilité parfaite des capitaux ?',
  'En changes fixes la politique budgétaire est très efficace et la monétaire inefficace ; en changes flexibles c’est l’inverse.',
  x='En faible mobilité, les deux politiques peuvent être efficaces en changes flexibles, et l’effet budgétaire reste limité en changes fixes.',
  t='fait', b=3497)

c('À quelles deux échelles faut-il analyser le régime de change de la zone euro ?',
  'Entre États membres, la monnaie unique s’apparente à un régime de changes fixes ; face au reste du monde, l’euro flotte.',
  x='Une union monétaire va pourtant plus loin que des parités fixes ajustables : les monnaies nationales ont disparu.',
  t='dist', b=3509)

c('Comment les instruments de politique économique sont-ils répartis dans la zone euro ?',
  'La politique monétaire est conduite par la Banque centrale européenne ; les politiques budgétaires restent nationales, encadrées par des règles européennes.',
  x='Un État membre ne peut donc pas fixer seul son taux directeur.',
  t='fait', b=3530)

c('Pourquoi l’intégration financière européenne a-t-elle réduit l’autonomie monétaire nationale ?',
  'Parce que libre circulation des capitaux et stabilité des changes européens occupent deux sommets du triangle de Mundell : le troisième doit être abandonné.',
  x='Une politique nationale trop expansionniste aurait provoqué des sorties de capitaux.',
  t='mec', b=3548)

c('En quoi la création de l’euro peut-elle se lire comme une réponse au triangle de Mundell ?',
  'Libre circulation des capitaux et stabilité des changes européens rendaient les politiques monétaires nationales interdépendantes : les États ont échangé leur autonomie individuelle contre une politique commune.',
  x='Une politique nationale trop expansionniste aurait contraint la banque centrale à resserrer pour tenir la parité.',
  t='mec', b=3552)

c('Quelles valeurs budgétaires de référence le traité de Maastricht retient-il ?',
  'Un déficit public de 3 % du PIB et une dette publique de 60 % du PIB.',
  x='Signé en 1992 et en vigueur en 1993, complété par le Pacte de stabilité et de croissance de 1997 ; ces seuils ne sont pas des interdictions absolues.',
  t='fait', b=3587)

c('Quel poids le budget de l’Union européenne représente-t-il ?',
  'Un peu plus de 1 % du revenu national brut de l’Union dans les cadres budgétaires pluriannuels récents.',
  x='Il ne se confond pas avec la somme des budgets nationaux et n’est pas propre à la seule zone euro.',
  t='fait', b=3626)

c('Pourquoi l’hétérogénéité économique complique-t-elle la politique monétaire unique ?',
  'Un pays en récession souhaiterait des taux plus bas quand un autre, confronté à l’inflation, les voudrait plus hauts ; la BCE ne peut adapter ses taux à chaque État.',
  x='La difficulté est accentuée par la répartition des instruments entre plusieurs niveaux de décision.',
  t='mec', b=3642)

c('Que révèle le cas grec sur le policy mix de la zone euro ?',
  'Les ajustements budgétaires destinés à restaurer la soutenabilité financière ont aggravé la contraction de la demande intérieure dans une économie déjà en récession.',
  x='L’épisode dépend aussi de problèmes structurels propres à la Grèce et des décisions européennes : le seul modèle IS-LM-BP ne l’explique pas.',
  t='fait', b=3686)

c('Quel principe la règle d’affectation de Mundell énonce-t-elle en 1963 ?',
  'Chaque instrument doit être affecté à l’objectif pour lequel son efficacité relative est la plus forte.',
  x='Une mauvaise affectation peut rendre les politiques contradictoires et les ajustements instables.',
  t='aut', b=3708)

c('À quels objectifs la règle de Mundell affecte-t-elle chacun des deux instruments ?',
  'La politique budgétaire à l’équilibre interne, parce qu’elle agit directement sur la demande ; la politique monétaire à l’équilibre externe, parce qu’elle agit sur les mouvements de capitaux.',
  x='Cette affectation relève d’un cadre théorique : la BCE a pour objectif principal la stabilité des prix.',
  t='fait', b=3729)

c('Quelle combinaison la règle de Mundell prescrit-elle face à du chômage et un déficit extérieur ?',
  'Une politique budgétaire expansionniste pour l’emploi et une politique monétaire restrictive pour attirer les capitaux.',
  x='Combinaison délicate : le resserrement monétaire freine aussi l’investissement, d’où l’importance de l’efficacité relative des instruments.',
  t='fait', b=3787)

c('Quelle combinaison la règle de Mundell prescrit-elle face à de l’inflation et un excédent extérieur ?',
  'Une politique budgétaire restrictive contre les tensions sur les prix et une politique monétaire expansionniste pour réduire l’excédent.',
  x='Les deux instruments jouent alors en sens opposés : c’est précisément l’intérêt de la règle d’affectation.',
  t='fait', b=3773)

c('Pourquoi la règle de Mundell est-elle difficile à appliquer dans la zone euro ?',
  'Parce que les politiques budgétaires sont nationales et la politique monétaire commune : aucun État ne dispose des deux instruments.',
  x='L’affectation suppose que les autorités maîtrisent effectivement les instruments qu’elles doivent répartir.',
  t='dist', b=3817)
