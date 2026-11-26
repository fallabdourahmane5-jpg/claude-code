# -*- coding: utf-8 -*-
"""Première année — chapitre 5. Analyse microéconomique (II) : les défaillances du marché."""

from fc_base import lot, c

L = lot(5)

c('Qu’est-ce qu’une défaillance de marché ?',
  'Une situation où le marché concurrentiel n’alloue pas les ressources de façon optimale.',
  x='Concrètement : on produit trop ou pas assez, à un prix trop élevé ou trop bas.',
  t='def', b=1, aussi=['4'])

c('Quelles sont les quatre situations de défaillance de marché retenues par le cours ?',
  'Le monopole naturel, les biens collectifs et communs, les externalités et les asymétries d’information.',
  x='Chacune empêche pour une raison différente l’égalité entre le prix et le coût marginal.',
  t='mec', b=3)

c('Quelle position Arthur Pigou défend-il sur l’intervention de l’État ?',
  'Libéral, il juge l’État légitime à intervenir précisément là où le marché est défaillant.',
  x='Il développe cette position dans l’économie du bien-être, qui cherche à maximiser l’utilité collective.',
  t='aut', b=9)

c('Quelle condition définit une allocation efficace en microéconomie ?',
  'L’égalité entre le prix et le coût marginal.',
  x='Lorsqu’elle est vérifiée, le surplus total est maximal, sans pénurie ni gaspillage.',
  t='form', b=17)

c('Qu’est-ce qu’un monopole ?',
  'Un marché où une seule entreprise vend un bien sans substitut proche, et fixe elle-même son prix.',
  x='Le monopoleur est price maker, là où le producteur en concurrence pure et parfaite est price taker.',
  t='def', b=26)

c('Sur quoi le monopoleur fonde-t-il son prix, à la différence du producteur concurrentiel ?',
  'Sur la disposition à payer des consommateurs, et non sur son coût marginal.',
  x='Il observe la demande et fixe le prix maximum que le marché accepte pour la quantité qu’il choisit de produire.',
  t='mec', b=36)

c('Quelles sont les quatre conséquences d’un monopole sur le bien-être ?',
  'La réduction du surplus du consommateur, une rente de monopole, une perte sèche et une allocation sous-optimale.',
  x='La perte sèche porte le nom de triangle d’Harberger : c’est du surplus détruit, qui ne profite à personne.',
  t='mec', b=41)

c('À quelles conditions un monopole est-il dit naturel ?',
  'Coûts fixes très élevés, coûts marginaux très faibles et rendements croissants.',
  x='Une seule entreprise produit alors à moindre coût que plusieurs concurrentes : eau, électricité, gaz, rail, réseaux.',
  t='def', b=51)

c('Pourquoi le monopole naturel est-il une véritable défaillance de marché ?',
  'Parce que le blocage est structurel : le marché ne peut pas résoudre seul le couple prix trop élevé, quantité trop faible.',
  x='Contrairement aux autres monopoles, aucune entrée de concurrent ne viendra corriger la situation.',
  t='mec', b=63)

c('Quelles solutions l’État peut-il opposer à un monopole naturel ?',
  'La nationalisation, la régulation par des prix plafonds, la tarification au coût moyen, ou une subvention permettant de tarifer au coût marginal.',
  x='Tarifer au coût marginal rendrait l’entreprise déficitaire du fait des coûts fixes : d’où la nécessité de la subvention.',
  t='mec', b=71)

c('Qu’est-ce qu’un brevet, et quelle protection confère-t-il ?',
  'Un droit de propriété intellectuelle qui donne une exclusivité d’exploitation pour vingt ans au maximum, sur un territoire donné.',
  x='Il crée volontairement un monopole temporaire, pour que l’innovation puisse être financée.',
  t='def', b=79)

c('Comment Schumpeter justifie-t-il le monopole d’innovation ?',
  'La concurrence doit rester la règle, mais l’innovation doit être protégée pour être rentable.',
  x='Le monopole temporaire incite à innover, finance la recherche et développement et nourrit le progrès technique.',
  t='aut', b=81)

c('Quels sont les risques d’un monopole d’innovation trop protégé ?',
  'Un accès limité aux innovations, un ralentissement de leur diffusion et des stratégies de verrouillage par brevets abusifs.',
  x='L’exemple le plus discuté est celui des médicaments, où l’exclusivité se heurte à l’accès aux soins.',
  t='mec', b=93)

c('Qu’est-ce qu’un monopole d’institution, et quels objectifs poursuit-il ?',
  'Un monopole créé par la loi, pour garantir un service public, contrôler un secteur sensible ou protéger l’intérêt général.',
  x='La Française des jeux et la SNCF en sont les exemples cités : continuité du service contre absence de concurrence.',
  t='def', b=98)

c('Quelles limites le cours relève-t-il aux monopoles d’État ?',
  'Un manque d’efficacité, l’absence d’incitation à innover, des risques de bureaucratie et la possibilité d’une défaillance de l’État.',
  x='Cette dernière renvoie à l’école du Public Choice : l’État n’est pas plus vertueux que le marché par nature.',
  t='mec', b=116)

c('Comment un effet de réseau peut-il engendrer un monopole ?',
  'L’utilité du service augmente avec le nombre d’utilisateurs, ce qui concentre spontanément la demande sur un seul acteur.',
  x='Réseaux sociaux, moteurs de recherche et plateformes numériques en relèvent : le risque est le verrouillage durable du marché.',
  t='mec', b=120)

c('Pourquoi la demande adressée à la firme diffère-t-elle entre concurrence parfaite et monopole ?',
  'Elle est parfaitement élastique en concurrence parfaite, décroissante en monopole.',
  x='Dans le premier cas prix, recette marginale et coût marginal coïncident ; dans le second le prix excède le coût marginal.',
  t='dist', b=136)

c('Que signifie qu’un bien est rival ?',
  'Que sa consommation par un individu prive les autres : ce qui est pris n’est plus disponible.',
  x='Un pain au chocolat l’est, l’éclairage public ne l’est pas : un usager de plus n’en coûte rien.',
  t='def', b=145)

c('Que signifie qu’un bien est excluable ?',
  'Qu’on peut empêcher d’y accéder celui qui ne paie pas.',
  x='Le cinéma et un abonnement en ligne le sont ; l’air et l’éclairage public ne le sont pas.',
  t='def', b=152)

c('Quelle différence essentielle sépare la rivalité de l’excluabilité ?',
  'La rivalité porte sur la quantité disponible, l’excluabilité sur la possibilité de filtrer l’accès par le paiement.',
  x='Les deux critères sont indépendants : c’est leur croisement qui donne les quatre types de biens.',
  t='dist', b=159)

c('Qu’est-ce qu’un bien privé au sens économique ?',
  'Un bien à la fois rival et excluable.',
  x='C’est le bien que le marché traite sans difficulté : il faut payer pour l’obtenir, et l’obtenir prive les autres.',
  t='def', b=167)

c('Qu’est-ce qu’un bien de club, et à quelle condition cesse-t-il d’en être un ?',
  'Un bien non rival mais excluable, comme l’autoroute à péage ; il devient rival dès qu’il est saturé.',
  x='Tant qu’il n’est pas saturé, le marché fonctionne bien puisqu’on peut faire payer l’accès.',
  t='def', b=173)

c('Qu’est-ce qu’un bien commun, et quel problème pose-t-il ?',
  'Un bien rival mais non excluable, comme les poissons de la mer ou les forêts ; il est surexploité.',
  x='Chacun a intérêt à prélever avant les autres : c’est la tragédie des biens communs décrite par Hardin.',
  t='def', b=179)

c('Qu’est-ce qu’un bien collectif pur, et quel exemple en est l’archétype ?',
  'Un bien non rival et non excluable ; le phare en est l’exemple parfait.',
  x='Un bateau de plus n’enlève rien à la lumière, et aucun dispositif technique ne permet d’en facturer l’usage.',
  t='def', b=188)

c('Pourquoi un public good anglais n’est-il pas nécessairement un bien fourni par l’État ?',
  'Parce que public y signifie collectif par nature, alors qu’en français le mot renvoie à l’État.',
  x='Dans les faits l’État les prend souvent en charge, mais c’est une conséquence de leur nature, non sa définition.',
  t='dist', b=209)

c('Qu’est-ce qu’un passager clandestin, et à quel auteur doit-on cette analyse ?',
  'Celui qui consomme un bien sans vouloir participer à son financement ; la notion est développée par Mancur Olson.',
  x='Chacun se dit qu’il profitera du bien même sans payer : personne ne finance, donc rien n’est produit.',
  t='aut', b=242)

c('Pourquoi une entreprise privée ne peut-elle pas produire un bien collectif pur ?',
  'Elle ne peut ni faire payer ni contrôler l’accès : son activité ne peut donc pas être rentable.',
  x='Seul un financement par l’impôt permet l’existence du bien, puisque l’intérêt est collectif et non individuel.',
  t='mec', b=249)

c('Le statut d’un bien est-il figé dans le temps ?',
  'Non : un bien peut passer de commun à privé ou l’inverse, selon la technologie, les règles ou les décisions politiques.',
  x='L’eau en est l’exemple : non excluable au puits, elle devient excluable dès qu’un réseau et un compteur existent.',
  t='mec', b=272)

c('Comment la technologie a-t-elle fait de l’eau un bien privé ?',
  'En individualisant les compteurs : chacun paie ce qu’il consomme et peut être exclu en cas de non-paiement.',
  x='Trois étapes : fontaines collectives, distribution par immeuble, puis compteur par logement.',
  t='mec', b=289)

c('Comment la réglementation empêche-t-elle la privatisation totale d’une rivière ?',
  'L’État impose des quotas et le maintien d’un débit minimal, interdisant de s’approprier tout le cours d’eau.',
  x='La technique permettrait de capter l’eau ; c’est la règle, et non la faisabilité, qui préserve le bien commun.',
  t='mec', b=306)

c('En quoi le cas des vaccins montre-t-il que le statut d’un bien est politique ?',
  'Produits par des firmes privées et protégés par des brevets, ils peuvent être traités en bien commun au nom de la santé publique.',
  x='Le statut dépend donc de choix politiques, et non seulement de critères techniques ou économiques.',
  t='mec', b=319)

c('De quel type de défaillance les biens collectifs purs relèvent-ils ?',
  'D’une défaillance par sous-production : le bien est socialement utile mais aucun producteur privé ne peut le rentabiliser.',
  x='La non-excluabilité empêche le prix de jouer son rôle d’allocation.',
  t='mec', b=357)

c('De quel type de défaillance les biens communs relèvent-ils ?',
  'D’une défaillance par surexploitation : chaque usage réduit la ressource sans qu’aucun prix ni règle ne dissuade de prélever.',
  x='« Si je ne consomme pas maintenant, quelqu’un d’autre le fera » : le raisonnement individuel épuise la ressource.',
  t='mec', b=370)

c('Quelles sont les trois solutions envisageables face à la tragédie des biens communs ?',
  'La réglementation publique par quotas, la privatisation par attribution de droits de propriété, ou la gestion collective.',
  x='La troisième voie est celle d’Elinor Ostrom : les usagers peuvent s’auto-organiser sans État ni marché.',
  t='mec', b=390)

c('Quelle idée Garrett Hardin renverse-t-il en 1968 dans The Tragedy of the Commons ?',
  'Celle selon laquelle l’intérêt individuel conduirait spontanément à l’intérêt général.',
  x='En accès libre, l’intérêt individuel détruit au contraire l’intérêt collectif par surexploitation.',
  t='aut', b=401)

c('Quelle asymétrie explique la tragédie des communs selon Hardin ?',
  'Le gain de la surexploitation est individuel, tandis que le coût de la dégradation est partagé par tous.',
  x='Chacun a donc intérêt à prélever davantage, et la somme de ces décisions épuise la ressource.',
  t='mec', b=412)

c('Comment le dilemme du prisonnier éclaire-t-il la tragédie des communs ?',
  'Ne sachant pas ce que feront les autres, chaque agriculteur anticipe leur surexploitation et surexploite à son tour pour se protéger.',
  x='Le comportement est individuellement rationnel et collectivement désastreux : la terre est détruite et tous y perdent.',
  t='mec', b=430)

c('Qu’établit Mancur Olson dans The Logic of Collective Action (1965) ?',
  'Même quand tous ont intérêt à ce qu’un bien collectif existe, il reste rationnel pour chacun de ne pas contribuer.',
  x='Le bénéfice est collectif mais le coût est individuel : chacun préfère laisser payer les autres.',
  t='aut', b=443)

c('Comment la grève illustre-t-elle le paradoxe de l’action collective ?',
  'Faire grève coûte une journée de salaire, mais les bénéfices obtenus profitent aussi à ceux qui n’y participent pas.',
  x='Ne pas faire grève est individuellement rationnel ; sans grévistes, rien n’est pourtant obtenu.',
  t='mec', b=465)

c('Que montrent ensemble Hardin et Olson ?',
  'Que sans règles, institutions ni contrainte collective, ni les biens communs ni les biens collectifs ne peuvent être préservés ou produits.',
  x='Hardin décrit la destruction par surexploitation, Olson l’impossibilité de financer volontairement.',
  t='mec', b=478)

c('Qu’est-ce qu’une externalité ?',
  'La répercussion, positive ou négative, de l’activité d’un agent sur un autre, sans passer par le marché ni donner lieu à compensation.',
  x='Le marché ne prend en compte que ce qui est payé : une externalité est précisément ce qui ne l’est pas.',
  t='def', b=488)

c('Pourquoi une externalité négative conduit-elle à une surproduction ?',
  'Parce que le producteur n’intègre pas le coût imposé aux autres : son prix est trop bas et sa quantité trop élevée.',
  x='Une usine qui pollue l’air d’un village supporte ses coûts de production, mais pas le dommage causé aux riverains.',
  t='mec', b=504)

c('Pourquoi une externalité positive conduit-elle à une sous-production ?',
  'Parce que le bénéfice procuré aux autres n’est pas rémunéré : l’activité est moins développée qu’il ne serait souhaitable.',
  x='L’apiculteur voisin d’un champ de fleurs en profite sans payer ; rien n’incite donc à multiplier ces champs.',
  t='mec', b=510)

c('Quel est le problème commun à toutes les externalités ?',
  'Le prix de marché ne reflète ni le coût ni le bénéfice réels pour la société.',
  x='Le niveau de production retenu n’est donc jamais socialement optimal : c’est bien une défaillance de marché.',
  t='mec', b=519)

c('En cas d’externalité négative, laquelle des deux courbes de coût passe au-dessus de l’autre ?',
  'Celle du coût social : l’entreprise ne supporte qu’une part du coût réellement engendré.',
  x='Le prix observé ne couvre que le coût de l’entreprise : une part du coût réel est cachée.',
  t='mec', b=564)

c('En cas d’externalité positive, laquelle des deux courbes de coût passe au-dessus de l’autre ?',
  'Celle du coût privé : il faut en retrancher le bénéfice que l’activité procure gratuitement aux autres.',
  x='La courbe sociale passe donc sous la courbe privée : la société supporte moins que l’entreprise seule.',
  t='mec', b=591)

c('Quelle est la conséquence d’une externalité positive sur le prix et la quantité ?',
  'Une sous-production et un prix trop élevé par rapport à l’optimum collectif.',
  x='Le marché empêche ainsi une activité socialement bénéfique de se développer autant qu’il le faudrait.',
  t='mec', b=603)

c('Qu’est-ce qu’une asymétrie d’information ?',
  'Une situation où, dans un échange ou un contrat, un agent détient plus d’informations que l’autre.',
  x='L’échange en devient biaisé : c’est une défaillance de marché identifiée dans les années 1970.',
  t='def', b=610)

c('Quels sont les deux grands types d’asymétrie d’information, et comment les distingue-t-on ?',
  'La sélection adverse, avant la signature du contrat, et l’aléa moral, après.',
  x='Le moment décide : ce qu’on ignore avant de s’engager, ou ce qui change une fois l’engagement pris.',
  t='dist', b=620)

c('Qu’est-ce que la sélection adverse ?',
  'Le mécanisme par lequel les produits de mauvaise qualité restent sur le marché tandis que les bons en sortent.',
  x='Méfiant, l’acheteur baisse son consentement à payer ; les bons vendeurs renoncent et la qualité moyenne s’effondre.',
  t='def', b=623)

c('À quelle loi monétaire compare-t-on la sélection adverse ?',
  'À la loi de Gresham : la mauvaise monnaie chasse la bonne.',
  x='Les mauvaises voitures chassent les bonnes selon exactement le même mécanisme d’éviction par la méfiance.',
  t='mec', b=634)

c('Comment la sélection adverse se manifeste-t-elle sur le marché du crédit ?',
  'La banque relève ses taux pour se protéger ; les emprunteurs prudents renoncent, seuls les plus risqués acceptent.',
  x='La protection recherchée attire donc précisément les profils dont la banque voulait se garder.',
  t='mec', b=640)

c('Qu’est-ce que l’aléa moral ?',
  'Le fait qu’un agent, une fois protégé, adopte un comportement plus risqué qu’auparavant.',
  x='Il survient après la signature du contrat, ce qui le distingue de la sélection adverse.',
  t='def', b=648)

c('Comment le rôle de prêteur en dernier ressort engendre-t-il un aléa moral ?',
  'Les banques, sachant qu’elles seront sauvées, prennent davantage de risques.',
  x='C’est le ressort du « too big to fail » : la protection du système encourage ce dont elle devait prémunir.',
  t='mec', b=652)

c('Quelle ambiguïté affecte tous les dispositifs de protection économique ?',
  'Nécessaires à la stabilité, ils engendrent eux-mêmes de l’aléa moral.',
  x='La solution fait donc partie du problème : protéger contre un risque encourage à le prendre.',
  t='mec', b=666)

c('Pourquoi l’asymétrie d’information suffit-elle à elle seule à créer une défaillance de marché ?',
  'Parce que même avec des agents rationnels, sans monopole ni externalité, le marché cesse d’allouer efficacement.',
  x='Le défaut ne vient ni de la structure du marché ni du comportement des agents, mais de l’information disponible.',
  t='mec', b=672)

c('Qu’est-ce que l’effet Jevons ?',
  'Quand le progrès technique abaisse le coût d’usage d’une ressource, la consommation totale de cette ressource augmente.',
  x='Jevons l’avait constaté sur le charbon ; l’argument sert aujourd’hui contre les politiques d’efficacité énergétique seules.',
  t='aut', b=680)

c('Quelles sont les trois grandes familles de solutions aux défaillances de marché ?',
  'L’action par les règles, l’action par les prix et l’action par les quantités.',
  x='Réglementation d’un côté, taxes et subventions pigouviennes ensuite, quotas échangeables enfin.',
  t='mec', b=692)

c('Quelles réglementations l’État oppose-t-il aux situations de monopole ?',
  'Les lois antitrust, comme le Sherman Act de 1890, l’interdiction de certaines fusions et le contrôle de la concurrence.',
  x='L’action porte ici sur la structure du marché plutôt que sur le prix ou la quantité produite.',
  t='fait', b=700)

c('Quelles limites le cours relève-t-il à la voie réglementaire ?',
  'Elle est peu incitative, sensible au lobbying, peu flexible et exposée au contournement.',
  x='Peu incitative parce qu’on respecte la norme sans chercher à faire mieux : elle fixe un plafond autant qu’un plancher.',
  t='mec', b=725)

c('Qu’est-ce qu’une taxe pigouvienne, et quel principe applique-t-elle ?',
  'Une taxe qui fait payer à l’entreprise le coût qu’elle impose à la société : c’est le principe pollueur-payeur.',
  x='Elle relève le coût marginal privé jusqu’au coût social, ce qui élève le prix et réduit la quantité vers l’optimum.',
  t='aut', b=735)

c('Comment une subvention corrige-t-elle une externalité positive ?',
  'En rémunérant le bénéfice collectif créé : le coût baisse, le prix diminue et la quantité produite augmente.',
  x='C’est l’exact symétrique de la taxe pigouvienne, appliqué à l’écart inverse entre coût privé et coût social.',
  t='mec', b=747)

c('Quelles limites l’instrument fiscal pigouvien rencontre-t-il ?',
  'La difficulté de mesurer précisément le coût externe, une faible acceptabilité politique et un effet inflationniste possible.',
  x='Mal calibrée, la taxe corrige trop ou trop peu : son efficacité dépend entièrement de l’évaluation du dommage.',
  t='mec', b=761)

c('Comment fonctionne un marché de quotas d’émission ?',
  'L’État fixe un plafond global, attribue des quotas, et les entreprises les échangent entre elles.',
  x='Celles qui polluent peu vendent, celles qui polluent beaucoup achètent : la réduction se fait au moindre coût collectif.',
  t='mec', b=771)

c('Quelles limites le cours relève-t-il aux marchés de quotas ?',
  'Un prix volatil, une grande complexité, un risque de spéculation et le problème de la répartition initiale des quotas.',
  x='L’allocation de départ est décisive : elle distribue une rente avant même que le marché ne fonctionne.',
  t='mec', b=781)

c('Pourquoi n’existe-t-il pas de solution parfaite aux défaillances de marché ?',
  'Parce que s’y ajoutent des défaillances de l’État, le lobbying, des effets pervers et des problèmes d’acceptabilité politique.',
  x='Le choix entre réglementation, taxe et quota relève donc d’un arbitrage, non d’une démonstration.',
  t='mec', b=786)

c('Quel résultat la taxe carbone britannique instaurée en 2013 a-t-elle produit ?',
  'La part du charbon dans la production électrique est passée de 40 % en 2012 à 4 % en 2019.',
  x='L’exemple sert à montrer qu’un signal-prix suffisamment net peut transformer un mix énergétique en quelques années.',
  t='fait', b=799)

c('Qu’est-ce qu’un bien tutélaire selon les Musgrave ?',
  'Un bien que l’État met à disposition de la population quasi gratuitement parce qu’il juge sa consommation souhaitable.',
  x='L’État ne se contente pas de taxer ou de subventionner : il produit lui-même, en se substituant au choix des agents.',
  t='aut', b=802)

c('Qu’est-ce qu’un prix plancher, et quand devient-il problématique ?',
  'Un prix minimum en dessous duquel il est interdit de vendre ; il ne pose problème que s’il dépasse le prix d’équilibre.',
  x='SMIC et prix garantis agricoles en sont les exemples : en deçà de l’équilibre, ils ne changent rien.',
  t='def', b=822)

c('Quels effets économiques un prix plancher contraignant produit-il ?',
  'Une surproduction, un gaspillage des ressources, une perte sèche et une incitation au contournement.',
  x='Stocks détruits sur un marché de biens, chômage sur le marché du travail, travail au noir dans les deux cas.',
  t='mec', b=833)

c('Quels effets économiques un prix plafond contraignant produit-il ?',
  'Une pénurie, une perte sèche, le développement d’une économie illégale et une dégradation de la qualité.',
  x='L’encadrement des loyers en est l’exemple : moins d’entretien, moins de rénovations, dessous-de-table.',
  t='mec', b=872)

c('Comment les surplus se déforment-ils sous un prix plafond ?',
  'Le surplus du consommateur augmente, celui du producteur diminue, et le surplus total recule.',
  x='Sous un prix plancher, le mouvement est inverse pour les deux premiers, mais le total recule également.',
  t='mec', b=886)

c('Quelle hypothèse centrale l’école des choix publics oppose-t-elle à Pigou ?',
  'L’État n’est pas un être neutre au-dessus de la société : il est composé d’acteurs rationnels qui maximisent leur utilité.',
  x='C’est l’individualisme méthodologique appliqué à la politique : les gouvernants ne sont pas d’une autre espèce que les agents.',
  t='mec', b=925)

c('Qui sont les principaux auteurs de l’école des choix publics ?',
  'James Buchanan, Gordon Tullock et George Stigler.',
  x='Le courant s’épanouit dans les années 1970-1980, avec Thatcher, Reagan et le succès de Friedman.',
  t='aut', b=914)

c('Quelles dérives l’école des choix publics impute-t-elle à l’intervention publique ?',
  'Agir par électoralisme, favoriser les groupes organisés, produire des politiques inefficaces et des effets pervers.',
  x='Exemple cité : une politique environnementale soutenue puis abandonnée parce qu’elle coûte des voix.',
  t='mec', b=950)

c('Comment résumer l’opposition entre Pigou et l’école des choix publics ?',
  'Pour Pigou le marché est imparfait et l’État peut l’améliorer ; pour le Public Choice l’État est imparfait et peut aggraver le marché.',
  x='Le débat ne porte donc pas sur l’existence des défaillances, mais sur la fiabilité du correcteur.',
  t='dist', b=967)

c('Qu’est-ce qu’une rente de monopole ?',
  'Un profit élevé obtenu par la seule position dominante, et non par l’innovation ou la productivité.',
  x='C’est l’objection majeure à confier un monopole naturel à une entreprise privée.',
  t='def', b=1012)

c('D’où viennent les externalités selon Ronald Coase ?',
  'D’un problème d’organisation et de droits de propriété, plus que d’un problème de comportement.',
  x='Il déplace ainsi la question : pourquoi faire intervenir l’État si les agents peuvent s’entendre entre eux ?',
  t='aut', b=1052)

c('Que signifie internaliser une externalité ?',
  'Faire entrer les coûts ou bénéfices externes dans le calcul économique des agents.',
  x='Pigou l’obtient par la taxe, Coase par la négociation entre détenteurs de droits.',
  t='def', b=1082)

c('Comment l’exemple des éléphants illustre-t-il la solution de Coase ?',
  'Attribuer un propriétaire identifié à chaque troupeau lui donne intérêt à le protéger et à négocier avec les braconniers.',
  x='Sans propriétaire, l’éléphant est un bien commun que les lois contournées ne suffisent pas à préserver.',
  t='mec', b=1067)

c('À quelles trois conditions le théorème de Coase s’applique-t-il ?',
  'Des coûts de transaction faibles, des acteurs peu nombreux et des droits de propriété faciles à définir.',
  x='Réunies, elles permettent une négociation privée ; absentes, elles rendent le marché inefficace.',
  t='mec', b=1109)

c('Dans quels cas la solution de Coase devient-elle inapplicable ?',
  'Pour les biens diffus et transfrontaliers : l’air, les océans, le climat, la pollution diffuse.',
  x='La négociation y devient trop coûteuse, et l’intervention publique ou collective redevient nécessaire.',
  t='mec', b=1132)

c('Pourquoi Coase est-il classé parmi les néo-institutionnalistes malgré sa solution de marché ?',
  'Parce qu’il juge l’État indispensable pour définir les droits de propriété, les garantir et faire appliquer les contrats.',
  x='Une fois ce cadre posé, le marché peut fonctionner seul : l’État construit le marché plus qu’il ne le corrige.',
  t='aut', b=1138)

c('Quelle troisième voie Elinor Ostrom ouvre-t-elle entre le marché et l’État ?',
  'La gestion collective des biens communs par les communautés locales, qui créent et font respecter leurs propres règles.',
  x='Première femme lauréate du prix Nobel d’économie en 2009, elle s’inscrit dans la nouvelle économie institutionnelle.',
  t='aut', b=1253)

c('Sur quelles observations Elinor Ostrom fonde-t-elle sa critique de Hardin ?',
  'Des cas concrets : gestion de l’eau en Espagne, pâturages suisses, forêts japonaises, systèmes d’irrigation asiatiques.',
  x='Ces communautés gèrent durablement des biens communs sans passer ni par l’État ni par le marché.',
  t='aut', b=1264)

c('Qu’appelle-t-on arrangements institutionnels chez Ostrom ?',
  'Des règles construites par les utilisateurs eux-mêmes, adaptées au contexte local, flexibles et évolutives.',
  x='Quotas décidés collectivement, tours de rôle, surveillance mutuelle et sanctions graduées en sont les formes.',
  t='def', b=1281)

c('À quelles conditions la gouvernance collective d’Ostrom fonctionne-t-elle ?',
  'Une communauté de petite taille dont les membres se connaissent, avec confiance, communication facile et surveillance possible.',
  x='Le modèle n’est donc pas universel mais local : il ne se transpose pas tel quel à l’échelle d’un pays.',
  t='mec', b=1295)

c('Quels types de communs la grille d’Ostrom permet-elle aujourd’hui d’analyser ?',
  'Les communs naturels, culturels, numériques et les communs de la connaissance.',
  x='Logiciels libres, Wikipédia, données ouvertes et recherche scientifique relèvent des deux derniers.',
  t='mec', b=1304)
