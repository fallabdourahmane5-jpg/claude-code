# -*- coding: utf-8 -*-
"""Quiz du chapitre 4 de deuxieme annee : connaissances et raisonnement.

Chaque entree : (type, question, options, index de la bonne reponse,
explication, tags thematiques).
"""

Q = []


def q(t, question, opts, ans, exp, tags):
    Q.append((t, question, opts, ans, exp, tags))


# ---------------------------------------------------------------- QCM
q('qcm', "Le multilatéralisme se définit comme :",
  ["Un accord négocié entre deux États",
   "Une décision prise par un État sans négociation",
   "Une action collective entre au moins trois États établissant des règles communes",
   "Un accord entre pays géographiquement proches"], 2,
  "Bonne réponse : C. Le multilatéralisme organise les relations internationales autour de règles négociées collectivement entre au moins trois États. A décrit le bilatéralisme, B l’unilatéralisme, D le régionalisme.",
  ['multilatéralisme', 'gouvernance mondiale'])
q('qcm', "Les deux principes essentiels sur lesquels repose le multilatéralisme sont :",
  ["Efficacité et efficience", "Réciprocité et équité",
   "Souveraineté et subsidiarité", "Transparence et proportionnalité"], 1,
  "Bonne réponse : B. Le cours insiste sur la réciprocité et l’équité. La transparence est un principe du GATT, mais les deux principes fondateurs du multilatéralisme comme mode de coordination sont la réciprocité et l’équité.",
  ['multilatéralisme', 'réciprocité'])
q('qcm', "Le plurilatéralisme désigne :",
  ["Un accord négocié entre un groupe limité de pays",
   "Un accord nécessairement régional",
   "Un accord engageant tous les membres de l’OMC",
   "Une décision unilatérale collective"], 0,
  "Bonne réponse : A. Le plurilatéralisme réunit un groupe limité de pays sans engager l’ensemble des membres du système commercial ; il ne se confond pas systématiquement avec le régionalisme, puisqu’il ne suppose aucune proximité géographique.",
  ['plurilatéralisme', 'multilatéralisme'])
q('qcm', "Dans le document, les trois catégories d’acteurs de la mondialisation sont :",
  ["Les États, les banques centrales et les ménages",
   "Les États, les firmes multinationales et la société civile",
   "L’OMC, le FMI et la Banque mondiale",
   "Les exportateurs, les importateurs et les consommateurs"], 1,
  "Bonne réponse : B. Les États définissent les politiques commerciales et industrielles, les FMN organisent les chaînes de valeur mondiales, la société civile regroupe citoyens, syndicats et ONG.",
  ['acteurs', 'mondialisation'])
q('qcm', "Un protectionnisme discriminant, c’est-à-dire dirigé contre certains pays :",
  ["Réduit nécessairement le volume total des échanges",
   "N’a aucun effet sur la géographie des échanges",
   "Peut réorienter les flux vers d’autres partenaires plutôt que les réduire",
   "Est interdit par tous les accords de l’OMC sans exception"], 2,
  "Bonne réponse : C. Le cours insiste sur ce point : un protectionnisme ciblé agit sur la géographie des échanges, pas seulement sur leur volume. C’est ce qui explique le détournement des flux chinois vers des pays tiers.",
  ['protectionnisme', 'politique commerciale'])
q('qcm', "Pourquoi les FMN sont-elles structurellement favorables à la liberté des échanges ?",
  ["Parce qu’elles paient moins d’impôts à l’étranger",
   "Parce que la fragmentation internationale de la production rend coûteux tout retour en arrière",
   "Parce qu’elles sont soumises aux règles de l’OMC",
   "Parce que les IDE horizontaux exigent le libre-échange"], 1,
  "Bonne réponse : B. Ayant organisé la fragmentation internationale de la production, les FMN ont construit des systèmes productifs interdépendants : le protectionnisme remet en cause l’organisation même de leurs chaînes de valeur.",
  ['fmn', 'chaînes de valeur'])
q('qcm', "Un IDE vertical correspond à :",
  ["Produire à proximité des consommateurs étrangers",
   "Racheter un concurrent du même secteur",
   "Fragmenter la production pour exploiter les avantages comparatifs des territoires",
   "Investir dans un fonds étranger sans prise de contrôle"], 2,
  "Bonne réponse : C. L’IDE vertical fragmente la production ; l’IDE horizontal, décrit par la réponse A, relève d’une logique de marché.",
  ['ide', 'fmn'])
q('qcm', "Selon Fontagné, l’ambivalence des citoyens face à la mondialisation s’explique par :",
  ["Un manque d’information économique",
   "La position multiple d’un même individu : consommateur, travailleur, épargnant",
   "L’influence des syndicats",
   "La volatilité des prix mondiaux"], 1,
  "Bonne réponse : B. Un même individu peut gagner comme consommateur (produits importés moins chers) et comme épargnant (internationalisation des capitaux), tout en perdant comme travailleur exposé à la concurrence.",
  ['fontagné', 'société civile'])
q('qcm', "La thèse du « doux commerce » est développée par :",
  ["Adam Smith dans la Richesse des nations",
   "Montesquieu dans De l’esprit des lois (1748)",
   "Ricardo dans les Principes",
   "Kindleberger dans La Grande Dépression mondiale"], 1,
  "Bonne réponse : B. Montesquieu écrit en 1748 que « partout où il y a du commerce, il y a des mœurs douces » et souligne que deux nations qui commercent deviennent réciproquement dépendantes.",
  ['montesquieu', 'doux commerce'])
q('qcm', "Le mécanisme pacificateur du doux commerce est :",
  ["Commerce → enrichissement → démocratie → paix",
   "Commerce → interdépendance → coût plus élevé d’un conflit → incitation à la paix",
   "Commerce → spécialisation → désarmement → paix",
   "Commerce → institutions → droit international → paix"], 1,
  "Bonne réponse : B. C’est la chaîne exacte du cours : l’interdépendance élève le coût économique du conflit et agit donc comme une incitation, non comme une vertu morale.",
  ['montesquieu', 'interdépendance', 'paix'])
q('qcm', "La CECA est créée en :",
  ["1944", "1947", "1951", "1957"], 2,
  "Bonne réponse : C. En 1951, six pays européens créent la Communauté européenne du charbon et de l’acier : la mise en commun de deux productions stratégiques vise à rendre un nouveau conflit plus difficile et surtout plus coûteux.",
  ['ceca', 'construction européenne'])
q('qcm', "Pour les analyses marxistes, l’interdépendance internationale :",
  ["Garantit la paix entre les nations",
   "Peut devenir une source de dépendance et de domination si les échanges sont asymétriques",
   "N’a aucun effet sur la répartition des gains",
   "Supprime les rapports de puissance"], 1,
  "Bonne réponse : B. Les échanges peuvent répartir inégalement les gains : certains pays captent l’essentiel du surplus, d’autres peuvent être perdants. L’interdépendance cesse alors d’être synonyme de sécurité.",
  ['marx', 'interdépendance', 'domination'])
q('qcm', "Dans son article de 1990, Luttwak soutient que :",
  ["La guerre froide va reprendre militairement",
   "La fin de la guerre froide supprime les rivalités de puissance",
   "La rivalité de puissance se déplace vers le terrain économique",
   "L’économie mondiale va se fragmenter en trois blocs"], 2,
  "Bonne réponse : C. « From Geopolitics to Geo-Economics » : la logique du conflit demeure, mais les instruments deviennent commerciaux, financiers et technologiques.",
  ['luttwak', 'géoéconomie'])
q('qcm', "Les droits de douane américains contemporains se distinguent du protectionnisme traditionnel parce qu’ils :",
  ["Visent uniquement à protéger l’emploi industriel",
   "Répondent à une logique de compétition stratégique et de domination technologique",
   "Sont conformes aux règles de l’OMC",
   "Ne concernent que les produits agricoles"], 1,
  "Bonne réponse : B. Ils relèvent d’une logique de rapport de force et de menace visant à obtenir des concessions, et cherchent à préserver les puissances technologique, commerciale et monétaire américaines.",
  ['géoéconomie', 'droits de douane', 'états-unis'])
q('qcm', "Le « dérisquage » consiste à :",
  ["Supprimer tous les échanges avec un partenaire",
   "Réduire certaines dépendances jugées dangereuses sans supprimer tous les échanges",
   "Assurer les exportateurs contre le risque de change",
   "Diversifier les placements financiers"], 1,
  "Bonne réponse : B. Le dérisquage se distingue du découplage : il cible les dépendances considérées comme stratégiquement risquées sans viser une rupture générale des relations économiques.",
  ['dérisquage', 'friendshoring'])
q('qcm', "Le friendshoring consiste à privilégier les échanges avec :",
  ["Les pays les plus proches géographiquement",
   "Les pays aux coûts de production les plus faibles",
   "Les pays considérés comme politiquement fiables ou alliés",
   "Les pays membres de l’OMC"], 2,
  "Bonne réponse : C. Le critère devient la fiabilité politique et non la seule efficacité économique, ce qui favorise la constitution de blocs géoéconomiques.",
  ['friendshoring', 'fragmentation'])
q('qcm', "Le paradoxe de la fragmentation géoéconomique énonce que :",
  ["Moins d’échanges signifie plus de croissance",
   "En réduisant leurs interdépendances, les États diminuent le coût d’un conflit et peuvent accroître les tensions",
   "La fragmentation augmente toujours le PIB mondial",
   "Les blocs économiques empêchent toute guerre"], 1,
  "Bonne réponse : B. La recherche individuelle de sécurité économique peut contribuer collectivement à accroître l’insécurité géopolitique : c’est un cercle vicieux explicite dans le cours.",
  ['fragmentation', 'paradoxe', 'géoéconomie'])
q('qcm', "Un bien public mondial se caractérise par :",
  ["La rivalité et l’exclusion", "La non-rivalité et la non-exclusion",
   "La rivalité et la non-exclusion", "La non-rivalité et l’exclusion"], 1,
  "Bonne réponse : B. Non-rivalité : la consommation par un acteur n’empêche pas les autres d’en bénéficier. Non-exclusion : il est difficile d’empêcher un acteur d’en bénéficier. Le climat en est l’exemple majeur.",
  ['bien public mondial', 'gouvernance'])
q('qcm', "En l’absence de coordination internationale, la production de biens publics mondiaux conduit à :",
  ["Un optimum de Pareto", "Un équilibre de Nash sous-optimal",
   "Une concurrence pure et parfaite", "Un équilibre budgétaire"], 1,
  "Bonne réponse : B. Chaque État a intérêt à laisser les autres supporter le coût : le comportement de passager clandestin aboutit à un équilibre où personne n’a intérêt à dévier seul, mais où le bien collectif est sous-produit.",
  ['passager clandestin', 'nash', 'bien public mondial'])
q('qcm', "La théorie de la stabilité hégémonique est développée par :",
  ["Paul Krugman", "Charles Kindleberger", "Jacob Viner", "Bela Balassa"], 1,
  "Bonne réponse : B. Kindleberger développe cette analyse dans La Grande Dépression mondiale, 1929-1939 (1973) puis dans son article de 1981 sur la domination et le leadership dans l’économie internationale.",
  ['kindleberger', 'stabilité hégémonique'])
q('qcm', "Dans la matrice du cours, lorsque le leader coopère et que le suiveur fait défection, les gains sont :",
  ["(4 ; 4)", "(3 ; 5)", "(2 ; 3)", "(5 ; 3)"], 1,
  "Bonne réponse : B. Le suiveur obtient 5 tandis que le leader coopérant n’obtient que 3 : c’est la traduction chiffrée du comportement de passager clandestin.",
  ['kindleberger', 'théorie des jeux'])
q('qcm', "Le cours précise que la matrice de Kindleberger :",
  ["Est un dilemme du prisonnier classique",
   "N’est pas exactement un dilemme du prisonnier, car A préfère toujours coopérer et B toujours faire défection",
   "N’a aucun équilibre",
   "Comporte deux équilibres symétriques"], 1,
  "Bonne réponse : B. Le cours le signale explicitement : les gains illustrent une situation asymétrique entre leader et suiveur, et non le dilemme du prisonnier classique.",
  ['kindleberger', 'théorie des jeux', 'piège'])
q('qcm', "Après 1945, la position hégémonique américaine repose notamment sur :",
  ["40 % de la production mondiale et 50 % des réserves d’or",
   "Environ 60 % de la production mondiale et 70 % des réserves mondiales d’or",
   "La maîtrise exclusive de l’arme nucléaire",
   "Un excédent commercial permanent"], 1,
  "Bonne réponse : B. Ce sont les deux ordres de grandeur retenus par le cours, qui expliquent la capacité américaine à financer la reconstruction, soutenir la stabilité monétaire et relancer les échanges.",
  ['états-unis', 'hégémonie', 'après-guerre'])
q('qcm', "Les accords de Bretton Woods de 1944 réunissent :",
  ["23 pays", "33 pays", "44 pays", "106 pays"], 2,
  "Bonne réponse : C. 44 pays participent à la conférence de Bretton Woods, qui conduit notamment à la création du FMI. Les 23 pays sont les signataires du GATT en 1947.",
  ['bretton woods', 'fmi', 'piège'])
q('qcm', "Le GATT est signé en 1947 par :",
  ["23 pays", "44 pays", "48 pays", "99 pays"], 0,
  "Bonne réponse : A. 23 pays signent le GATT en 1947. 48 participants concerneront le Kennedy Round, 99 le Tokyo Round.",
  ['gatt', 'chiffres'])
q('qcm', "Pourquoi le GATT n’est-il pas une organisation internationale à sa création ?",
  ["Parce que les pays ont refusé toute règle commune",
   "Parce que le projet d’OIC n’aboutit pas, les États-Unis ne ratifiant pas la Charte de La Havane",
   "Parce que le FMI en assurait déjà les fonctions",
   "Parce que l’ONU s’y opposait"], 1,
  "Bonne réponse : B. À défaut d’une véritable organisation, les pays mettent en place un simple accord commercial. L’institution permanente n’apparaît qu’en 1995 avec l’OMC.",
  ['gatt', 'oic', 'charte de la havane'])
q('qcm', "La clause de la nation la plus favorisée correspond à :",
  ["L’article I du GATT", "L’article III du GATT",
   "L’article XI du GATT", "L’article XIX du GATT"], 0,
  "Bonne réponse : A. L’article I pose la clause NPF ; l’article III le traitement national, l’article XI l’interdiction des restrictions quantitatives, l’article XIX les mesures de sauvegarde.",
  ['npf', 'gatt', 'articles'])
q('qcm', "Le traitement national signifie qu’un produit importé :",
  ["Doit être taxé comme dans son pays d’origine",
   "Ne doit pas être traité moins favorablement qu’un produit national comparable une fois entré sur le marché",
   "Doit bénéficier d’un avantage fiscal",
   "Est exonéré de droits de douane"], 1,
  "Bonne réponse : B. Un véhicule électrique importé ne peut subir une discrimination fiscale du seul fait de son origine : c’est l’article III du GATT.",
  ['traitement national', 'non-discrimination'])
q('qcm', "Pourquoi le système commercial multilatéral privilégie-t-il les droits de douane aux restrictions quantitatives ?",
  ["Parce qu’ils protègent mieux les producteurs",
   "Parce qu’ils sont identifiables, mesurables et donc négociables",
   "Parce qu’ils rapportent moins de recettes",
   "Parce qu’ils sont interdits par l’article XI"], 1,
  "Bonne réponse : B. C’est le principe de transparence : une mesure non tarifaire — norme, procédure, quota — peut être difficile à mesurer et dissimuler un protectionnisme.",
  ['transparence', 'droits de douane'])
q('qcm', "L’article XI du GATT interdit en principe :",
  ["Les subventions à l’exportation", "Les restrictions quantitatives",
   "Les droits antidumping", "Les accords régionaux"], 1,
  "Bonne réponse : B. Les restrictions quantitatives, dont le contingentement, peuvent bloquer directement les échanges, d’où leur interdiction de principe.",
  ['article xi', 'contingentement'])
q('qcm', "Les accords commerciaux régionaux dérogent à la clause NPF sur le fondement de :",
  ["L’article I", "L’article III", "L’article XXIV", "L’Accord SMC"], 2,
  "Bonne réponse : C. L’article XXIV du GATT prévoit une exception pour les zones de libre-échange et les unions douanières, sous réserve de conditions juridiques et d’obligations de notification.",
  ['acr', 'article xxiv', 'npf'])
q('qcm', "Le système généralisé de préférences se caractérise par :",
  ["Une réciprocité stricte entre pays développés et PED",
   "Des préférences tarifaires accordées aux PED sans réciprocité équivalente",
   "Une interdiction des droits de douane sur les produits agricoles",
   "Un tarif extérieur commun"], 1,
  "Bonne réponse : B. Apparu à la fin des années 1960 et mis en œuvre à partir des années 1970, le SGP facilite l’accès des PED aux marchés développés ; les préférences peuvent être retirées lorsque les conditions d’éligibilité ne sont plus remplies.",
  ['sgp', 'traitement spécial et différencié'])
q('qcm', "En septembre 2025, la Chine a annoncé :",
  ["Qu’elle quittait l’OMC",
   "Qu’elle ne demanderait plus de nouveaux avantages de traitement spécial et différencié",
   "Qu’elle perdait son statut de pays en développement",
   "Qu’elle renonçait à tous ses avantages existants"], 1,
  "Bonne réponse : B. Le cours précise explicitement que cela ne signifie ni la perte formelle de son statut de pays en développement à l’OMC, ni la disparition automatique de ses avantages existants.",
  ['chine', 'traitement spécial et différencié', 'piège'])
q('qcm', "Une mesure de sauvegarde suppose notamment :",
  ["La preuve d’un dumping", "La preuve d’une subvention étrangère",
   "Une augmentation des importations causant un dommage grave, établie par une enquête",
   "Un accord préalable de tous les membres de l’OMC"], 2,
  "Bonne réponse : C. La sauvegarde répond à un dommage provoqué par la hausse des importations, même en l’absence de concurrence déloyale ; elle exige un lien de causalité, une enquête et une mesure temporaire et proportionnée.",
  ['sauvegarde', 'article xix'])
q('qcm', "Les subventions subordonnées aux résultats à l’exportation relèvent de :",
  ["La catégorie rouge, en principe prohibée",
   "La catégorie orange, contestable",
   "La catégorie verte, autorisée",
   "Aucune catégorie de l’Accord SMC"], 0,
  "Bonne réponse : A. Comme les subventions subordonnées à l’utilisation de produits nationaux, elles favorisent directement les producteurs nationaux et sont en principe interdites par l’Accord SMC.",
  ['smc', 'subventions'])
q('qcm', "La catégorie « verte » de l’Accord SMC :",
  ["Autorise définitivement toutes les aides environnementales",
   "A expiré en 1999", "A été créée en 2015", "Concerne uniquement l’agriculture"], 1,
  "Bonne réponse : B. Le cours met explicitement en garde : il serait incorrect d’affirmer que toutes les subventions écologiques ou de recherche sont automatiquement autorisées aujourd’hui.",
  ['smc', 'subventions', 'piège'])
q('qcm', "L’Organe de règlement des différends est créé :",
  ["En 1947 avec le GATT", "En 1979 au Tokyo Round",
   "En 1995 avec l’OMC", "En 2001 au lancement de Doha"], 2,
  "Bonne réponse : C. La création de l’OMC institutionnalise le règlement des conflits commerciaux ; les États-Unis et l’Union européenne figurent parmi les acteurs les plus présents dans les différends.",
  ['ord', 'omc'])
q('qcm', "En 2019, le droit de douane moyen mondial s’élève à :",
  ["3 % dans l’agriculture et 15,9 % dans l’industrie",
   "15,9 % dans l’agriculture et 3 % dans l’industrie",
   "7 % dans les deux secteurs",
   "4 % dans l’agriculture et 4 % dans l’industrie"], 1,
  "Bonne réponse : B. L’agriculture est beaucoup plus protégée que l’industrie, pour des raisons de sécurité alimentaire, de revenus agricoles, de stabilité des territoires ruraux et de souveraineté.",
  ['agriculture', 'droits de douane', 'chiffres'])
q('qcm', "L’Agricultural Adjustment Act date de :",
  ["1929", "1933", "1947", "1962"], 1,
  "Bonne réponse : B. Adopté dans le cadre du New Deal, il constitue une étape majeure du soutien public aux revenus agricoles américains, structuré ensuite par les Farm Bills.",
  ['agriculture', 'états-unis', 'new deal'])
q('qcm', "La politique agricole commune est mise en œuvre en :",
  ["1951", "1957", "1962", "1986"], 2,
  "Bonne réponse : C. En 1962, la CEE met en œuvre la PAC, dont les objectifs initiaux comprennent la productivité agricole, un niveau de vie équitable, la stabilisation des marchés, la sécurité des approvisionnements et des prix raisonnables.",
  ['pac', 'agriculture', 'europe'])
q('qcm', "Le groupe de Cairns rassemble :",
  ["Des pays importateurs nets de produits agricoles",
   "Des pays exportateurs agricoles favorables à la libéralisation des échanges agricoles",
   "Les membres fondateurs du GATT",
   "Les pays les moins avancés"], 1,
  "Bonne réponse : B. Dans les négociations de Doha, ces pays et des coalitions de PED, notamment autour du Brésil, contestent les subventions américaines et européennes — l’exemple du coton américain et de ses effets sur les producteurs africains est explicite dans le cours.",
  ['cairns', 'agriculture', 'doha'])
q('qcm', "Au Sénégal, la filière arachide a représenté jusqu’à :",
  ["10 % des terres cultivées", "25 % des terres cultivées",
   "40 % des terres cultivées", "60 % des terres cultivées"], 2,
  "Bonne réponse : C. Cette spécialisation s’est faite au détriment de la diversification agricole, des cultures vivrières, de la sécurité alimentaire et de la préservation des sols.",
  ['sénégal', 'arachide', 'agriculture'])
q('qcm', "Après les émeutes de la faim de 2007-2008, le Sénégal lance notamment :",
  ["Un programme d’intensification de la riziculture",
   "Une interdiction totale des importations alimentaires",
   "Une spécialisation accrue dans l’arachide",
   "Un retrait de l’OMC"], 0,
  "Bonne réponse : A. L’objectif est d’augmenter la production nationale de riz et de réduire la dépendance aux importations ; mais l’intensification pouvant appauvrir les sols, le pays cherche désormais à diversifier vers d’autres céréales, notamment le mil, et vers les fruits et légumes.",
  ['sénégal', 'sécurité alimentaire', 'diversification'])
q('qcm', "L’accord multifibres entre en vigueur en :",
  ["1962", "1974", "1986", "1995"], 1,
  "Bonne réponse : B. Il permet aux pays développés de limiter par des quotas certaines importations textiles, constituant une dérogation protectionniste durable au principe de libéralisation.",
  ['accord multifibres', 'textile'])
q('qcm', "Le démantèlement des quotas de l’accord multifibres s’achève le :",
  ["1er janvier 1995", "1er janvier 2001", "1er janvier 2005", "1er janvier 2010"], 2,
  "Bonne réponse : C. L’accord sur les textiles et les vêtements prévoit un démantèlement progressif sur dix ans ; à partir du 1er janvier 2005, le secteur est pleinement intégré aux règles générales de l’OMC.",
  ['accord multifibres', 'uruguay round', 'textile'])
q('qcm', "Le Kennedy Round (1964-1967) aboutit notamment à :",
  ["La création de l’OMC", "Un premier code antidumping",
   "L’accord sur les subventions et mesures compensatoires",
   "Le démantèlement de l’accord multifibres"], 1,
  "Bonne réponse : B. Au-delà de la baisse des droits de douane vers une cible d’environ 7 %, le Kennedy Round précise les conditions dans lesquelles les pays peuvent réagir aux pratiques commerciales préjudiciables.",
  ['kennedy round', 'antidumping'])
q('qcm', "L’apport essentiel du Tokyo Round (1973-1979) est :",
  ["La baisse des droits de douane uniquement",
   "L’encadrement des obstacles non tarifaires et des subventions",
   "L’intégration de l’agriculture",
   "La création de l’Organe de règlement des différends"], 1,
  "Bonne réponse : B. Dans un contexte de crise, les négociations portent sur les subventions, les mesures compensatoires, les obstacles techniques et certaines procédures ; un accord sur les subventions est conclu en 1979.",
  ['tokyo round', 'obstacles non tarifaires'])
q('qcm', "L’Uruguay Round se conclut avec :",
  ["48 participants", "99 participants", "123 participants", "166 participants"], 2,
  "Bonne réponse : C. Il rassemble 106 participants au départ et 123 à la conclusion. 166 est le nombre de membres de l’OMC en 2026.",
  ['uruguay round', 'chiffres'])
q('qcm', "Le principe de l’engagement unique signifie que :",
  ["Chaque pays choisit les concessions qu’il accepte",
   "Rien n’est convenu tant que tout n’est pas convenu",
   "Un seul cycle de négociation est autorisé",
   "Les accords sont signés par un seul représentant"], 1,
  "Bonne réponse : B. Il empêche une libéralisation sélective, mais en multipliant les sujets et les participants, il multiplie aussi les possibilités de blocage : c’est l’une des causes de l’enlisement de Doha.",
  ['doha', 'engagement unique'])
q('qcm', "La conférence de Seattle de 1999 est importante parce qu’elle :",
  ["Crée l’OMC", "Lance le cycle de Doha",
   "Révèle la crise de légitimité du multilatéralisme commercial",
   "Conclut l’Uruguay Round"], 2,
  "Bonne réponse : C. Elle devait préparer un nouveau cycle mais se déroule dans un contexte de contestation : PED, pays développés et mouvements altermondialistes critiquent simultanément l’OMC pour des raisons différentes.",
  ['seattle', 'altermondialisme', 'légitimité'])
q('qcm', "Selon la décomposition attribuée à Findlay et O’Rourke (2002), le principal facteur de croissance du commerce mondial entre les années 1950 et 1980 est :",
  ["La réduction des droits de douane (25 %)",
   "La hausse des revenus (67 %)",
   "La baisse des coûts de transport (8 %)",
   "La création du GATT"], 1,
  "Bonne réponse : B. La croissance économique explique environ deux tiers de l’expansion commerciale ; la libéralisation joue un rôle réel mais non majoritaire, et la conteneurisation environ 8 %.",
  ['findlay', 'o’rourke', 'commerce mondial', 'chiffres'])
q('qcm', "En 2026, l’OMC compte :",
  ["123 membres", "150 membres", "166 membres", "190 membres"], 2,
  "Bonne réponse : C. Le système passe de 23 pays en 1947 à 123 participants à la conclusion de l’Uruguay Round, puis à 166 membres ; la Chine rejoint l’OMC en 2001.",
  ['omc', 'chiffres', 'élargissement'])
q('qcm', "Au 1er septembre 2026, le nombre d’accords commerciaux régionaux en vigueur est de :",
  ["181", "388", "642", "166"], 1,
  "Bonne réponse : B. 642 accords ont été notifiés à l’OMC et 388 sont en vigueur ; 181 est le nombre de notifications concernant l’Europe.",
  ['acr', 'chiffres', 'régionalisation'])
q('qcm', "Dans une zone de libre-échange, les pays membres :",
  ["Adoptent un tarif extérieur commun",
   "Conservent chacun leur propre politique commerciale envers les pays tiers",
   "Partagent une monnaie commune",
   "Transfèrent leur politique commerciale à une autorité supranationale"], 1,
  "Bonne réponse : B. C’est la différence décisive avec l’union douanière : deux membres d’une zone de libre-échange peuvent appliquer des droits différents à un même produit extérieur, d’où l’importance des règles d’origine.",
  ['balassa', 'zone de libre-échange', 'piège'])
q('qcm', "L’Union européenne constitue :",
  ["Une simple zone de libre-échange",
   "Une union douanière, un marché commun et, pour une partie de ses membres, une union monétaire",
   "Une intégration totale au sens de Balassa",
   "Un accord plurilatéral sans institution commune"], 1,
  "Bonne réponse : B. La France ne décide pas seule des droits de douane applicables aux produits extérieurs : la politique commerciale relève du niveau européen. Tous les États membres n’appartiennent cependant pas à la zone euro.",
  ['balassa', 'union européenne', 'intégration'])
q('qcm', "La cinquième étape de la typologie de Balassa est :",
  ["L’union douanière", "Le marché commun",
   "L’union économique et monétaire", "L’intégration totale"], 3,
  "Bonne réponse : D. L’intégration totale unifie les principales politiques économiques sous une autorité supranationale : l’intégration économique devient alors également politique.",
  ['balassa', 'intégration totale'])
q('qcm', "La création de trafic au sens de Viner correspond à :",
  ["Une hausse des échanges avec les pays tiers",
   "Le remplacement d’une production domestique coûteuse par une importation moins chère d’un partenaire",
   "Le remplacement d’un fournisseur extérieur efficace par un partenaire moins efficace",
   "Une hausse des recettes douanières"], 1,
  "Bonne réponse : B. La zone fonctionne alors comme un petit espace de libre-échange : les pays peuvent davantage se spécialiser selon leurs avantages comparatifs, ce qui améliore le bien-être.",
  ['viner', 'création de trafic'])
q('qcm', "Le détournement de trafic réduit l’efficience parce que :",
  ["Il augmente les droits de douane sur les produits internes",
   "Un fournisseur mondial plus efficace est remplacé par un partenaire régional moins efficace",
   "Il supprime les échanges intra-zone",
   "Il interdit les importations"], 1,
  "Bonne réponse : B. Après la création de l’union, le prix du partenaire hors droits peut devenir inférieur au prix du fournisseur mondial augmenté du droit de douane, alors même que ce dernier est intrinsèquement plus efficace.",
  ['viner', 'détournement de trafic'])
q('qcm', "Un accord régional améliore globalement le bien-être lorsque :",
  ["Les échanges intra-zone augmentent",
   "La création de trafic l’emporte sur le détournement de trafic",
   "Le tarif extérieur commun augmente",
   "Tous les membres ont le même niveau de développement"], 1,
  "Bonne réponse : B. La hausse des échanges internes ne prouve rien : le détournement de trafic les augmente aussi tout en dégradant l’allocation mondiale des ressources.",
  ['viner', 'évaluation', 'piège'])
q('qcm', "L’ASEAN est créée en :",
  ["1957", "1967", "1992", "2001"], 1,
  "Bonne réponse : B. Créée en 1967 par cinq pays puis élargie à dix, elle naît en pleine guerre froide : sa dimension est dès l’origine politique autant qu’économique.",
  ['asean', 'régionalisation'])
q('qcm', "La part de l’ASEAN dans les exportations mondiales de biens est passée :",
  ["De 2 % à 4 %", "D’environ 4 % en 1990 à environ 8 % aujourd’hui",
   "De 8 % à 15 %", "De 10 % à 8 %"], 1,
  "Bonne réponse : B. Sa part a approximativement doublé en une trentaine d’années, atteignant un poids proche de celui des États-Unis : l’intégration régionale y a accompagné une forte insertion mondiale.",
  ['asean', 'chiffres', 'création de trafic'])
q('qcm', "En 2020, la part des exportations africaines destinées à l’Afrique est d’environ :",
  ["5 %", "13,9 %", "26,8 %", "40 %"], 1,
  "Bonne réponse : B. Les projections envisagent 26,8 % en 2045 avec la ZLECAf : la zone devrait renforcer le commerce intra-africain sans supprimer la forte orientation extérieure des échanges.",
  ['zlecaf', 'chiffres', 'afrique'])
q('qcm', "La principale limite structurelle de la ZLECAf est :",
  ["L’absence de volonté politique",
   "La faible complémentarité productive entre économies aux spécialisations proches",
   "L’interdiction par l’OMC",
   "L’absence de droits de douane à supprimer"], 1,
  "Bonne réponse : B. De nombreuses économies africaines exportent des produits similaires — agriculture, ressources naturelles, matières premières minières — ce qui limite la demande mutuelle et donc le commerce intra-zone.",
  ['zlecaf', 'complémentarité', 'afrique'])
q('qcm', "Chez Robert Lawrence, l’intégration profonde consiste à :",
  ["Supprimer les droits de douane et les quotas",
   "Rapprocher les règles internes : normes sociales, environnement, concurrence, investissements",
   "Créer une monnaie commune",
   "Adopter un tarif extérieur commun"], 1,
  "Bonne réponse : B. L’intégration superficielle supprime les barrières aux frontières ; l’intégration profonde harmonise partiellement les réglementations internes des économies partenaires.",
  ['lawrence', 'intégration profonde'])
q('qcm', "Dans l’accord de libre-échange entre l’Union européenne et le Vietnam :",
  ["Seuls les droits de douane sont concernés",
   "Le Vietnam s’engage également sur certaines normes fondamentales du travail",
   "L’UE renonce à ses normes sanitaires",
   "Les investissements sont exclus"], 1,
  "Bonne réponse : B. Liberté syndicale, droits des travailleurs et conventions fondamentales de l’OIT font partie de l’accord : les accords commerciaux deviennent des instruments de diffusion de normes.",
  ['lawrence', 'ue-vietnam', 'normes sociales'])
q('qcm', "L’opposition la plus forte à l’accord UE-Mercosur vient :",
  ["Des industries automobiles européennes",
   "Des producteurs agricoles européens exposés à une concurrence accrue",
   "Des exportateurs de vins et spiritueux",
   "Des consommateurs sud-américains"], 1,
  "Bonne réponse : B. Les pays du Mercosur disposent d’avantages dans certaines productions agricoles — vastes superficies, économies d’échelle, coûts parfois plus faibles — tandis que l’industrie européenne espère au contraire un meilleur accès au marché.",
  ['ue-mercosur', 'effets distributifs'])
q('qcm', "Le débat sur la « réciprocité des normes » dans l’accord UE-Mercosur porte sur :",
  ["Le niveau des droits de douane",
   "Le fait qu’un produit importé puisse respecter la norme finale tout en ayant été produit selon des règles différentes",
   "La monnaie de facturation",
   "Le nombre de pays signataires"], 1,
  "Bonne réponse : B. Les producteurs européens peuvent considérer qu’ils subissent des contraintes réglementaires — pesticides, normes sanitaires, traçabilité — que leurs concurrents ne supportent pas, d’où le soupçon de concurrence déloyale.",
  ['ue-mercosur', 'normes', 'réciprocité'])
q('qcm', "L’image du « bol de spaghettis » est due à :",
  ["Richard Baldwin", "Jagdish Bhagwati", "Jacob Viner", "Bela Balassa"], 1,
  "Bonne réponse : B. Bhagwati la propose en 1995 dans « US Trade Policy: The Infatuation with Free Trade Agreements » ; Baldwin l’illustre en 2008 avec le cas de l’Amérique latine.",
  ['bhagwati', 'bol de spaghettis', 'attribution'])
q('qcm', "L’effet domino en matière d’accords commerciaux signifie que :",
  ["Un accord entraîne automatiquement la dissolution des autres",
   "Plus les blocs se forment, plus le coût d’en rester exclu augmente et incite à conclure de nouveaux accords",
   "Les accords régionaux se transforment nécessairement en unions douanières",
   "Les pays tiers gagnent toujours à rester extérieurs"], 1,
  "Bonne réponse : B. La multiplication des ACR est auto-entretenue : le désavantage relatif subi par les producteurs des pays exclus les pousse à rejoindre ou conclure d’autres accords.",
  ['effet domino', 'régionalisation'])
q('qcm', "L’expression « multilatéralisme sans OMC » désigne :",
  ["Le retrait des États-Unis de l’OMC",
   "La diffusion de règles internationales par l’interconnexion d’accords préférentiels plutôt que par une négociation universelle",
   "Un accord secret entre grandes puissances",
   "La suppression de la clause NPF"], 1,
  "Bonne réponse : B. Baldwin propose l’image d’un ordre commercial en « système solaire » : les grandes puissances réglementaires constituent les centres autour desquels gravitent les partenaires.",
  ['baldwin', 'multilatéralisme sans omc'])
q('qcm', "La gouvernance mondiale contemporaine est qualifiée d’« hybride » parce que :",
  ["Elle mélange droit public et droit privé",
   "Aucune institution unique ne détermine plus les règles, qui résultent de l’interaction de multiples acteurs",
   "Elle combine libre-échange et autarcie",
   "Elle repose sur deux organisations seulement"], 1,
  "Bonne réponse : B. OMC, États, ACR, firmes multinationales, G7 et G20, organisations régionales et société civile produisent des règles qui peuvent être contradictoires.",
  ['gouvernance hybride', 'régulation'])
q('qcm', "Le pouvoir réglementaire indirect des FMN provient :",
  ["De leur droit de vote à l’OMC",
   "De la mobilité de leurs investissements, qui met les territoires en concurrence",
   "De leur participation au G20",
   "De leur capacité à fixer les droits de douane"], 1,
  "Bonne réponse : B. Le chantage à la localisation peut conduire à un moins-disant fiscal, social ou réglementaire : l’État n’est plus l’unique producteur des règles.",
  ['fmn', 'attractivité', 'gouvernance'])
q('qcm', "Le G20 réunit ses chefs d’État et de gouvernement pour la première fois en :",
  ["1999", "2008", "2015", "2023"], 1,
  "Bonne réponse : B. Le G20 existe dès 1999 au niveau des ministres des Finances et des gouverneurs de banques centrales, mais c’est la crise financière mondiale qui lui donne, en novembre 2008, un rôle politique majeur.",
  ['g20', 'crise de 2008'])
q('qcm', "En 2023, le G20 accueille comme membre permanent :",
  ["L’Union africaine", "L’ASEAN", "Le Mercosur", "L’OPEP"], 0,
  "Bonne réponse : A. L’Union africaine devient membre permanent en 2023, le groupe conservant son appellation de G20.",
  ['g20', 'union africaine'])
q('qcm', "Le taux minimum d’imposition coordonné au niveau international concerne :",
  ["Toutes les entreprises", "Certaines grandes multinationales, à hauteur de 15 %",
   "Les seules banques", "Les exportateurs agricoles"], 1,
  "Bonne réponse : B. Cet accord illustre la capacité du G20 à produire des règles communes sans disposer du pouvoir juridique de l’OMC.",
  ['g20', 'fiscalité internationale'])
q('qcm', "Le trilemme de Rodrik oppose :",
  ["Croissance, emploi et inflation",
   "Hypermondialisation, démocratie et souveraineté nationale",
   "Efficacité, équité et liberté",
   "Commerce, finance et migrations"], 1,
  "Bonne réponse : B. On peut conserver deux de ces objectifs, jamais les trois pleinement et simultanément.",
  ['rodrik', 'trilemme'])
q('qcm', "Dans le trilemme de Rodrik, associer hypermondialisation et souveraineté nationale conduit à :",
  ["Renforcer la démocratie", "Fragiliser l’autonomie démocratique",
   "Supprimer les États-nations", "Créer une gouvernance supranationale"], 1,
  "Bonne réponse : B. Les décisions nationales doivent alors se plier aux contraintes des marchés internationaux : c’est ce que Rodrik nomme la « camisole dorée ».",
  ['rodrik', 'trilemme', 'camisole dorée'])
q('qcm', "Rodrik rapproche l’association démocratie et souveraineté nationale :",
  ["Du consensus de Washington", "Du compromis de Bretton Woods",
   "De l’étalon-or", "De l’union douanière"], 1,
  "Bonne réponse : B. L’ouverture reste importante mais les États conservent des marges de manœuvre en matière de redistribution, de fiscalité et de politique sociale.",
  ['rodrik', 'bretton woods'])
q('qcm', "Aux États-Unis depuis 1984, le PIB réel par habitant et le revenu médian des ménages :",
  ["Progressent au même rythme", "Divergent, le revenu médian progressant beaucoup plus lentement",
   "Baissent tous les deux", "Divergent au profit du revenu médian"], 1,
  "Bonne réponse : B. Une partie des gains se concentre vers le haut de la distribution : la croissance moyenne ne décrit donc pas correctement l’évolution du niveau de vie de tous les ménages.",
  ['inégalités', 'revenu médian', 'états-unis'])
q('qcm', "Pour Rodrik, la réponse au déclassement des classes moyennes passe prioritairement par :",
  ["La seule réindustrialisation",
   "L’élévation de la productivité et de la qualité des emplois de services",
   "La fermeture des frontières",
   "La baisse des salaires"], 1,
  "Bonne réponse : B. Les économies avancées étant majoritairement tertiaires, l’industrie n’emploie qu’une minorité d’actifs : les « good jobs » doivent donc être recherchés dans la santé, l’éducation, les services à la personne et les activités locales.",
  ['rodrik', 'good jobs', 'services'])
q('qcm', "Dans le deuxième scénario de Sébastien Jean, on observe :",
  ["Un renforcement de l’OMC",
   "Une guerre froide économique avec découplage, relocalisations et friend-shoring",
   "Un retour au multilatéralisme des années 1990",
   "La disparition des accords régionaux"], 1,
  "Bonne réponse : B. Les sanctions se multiplient, les chaînes se réorganisent selon les alliances et les pays tiers subissent des pressions pour choisir leur camp : c’est la fragmentation géo-économique.",
  ['sébastien jean', 'scénarios', 'fragmentation'])
q('qcm', "Selon Bolhuis, Chen et Kett (FMI, 2023), une fragmentation complète en deux blocs coûterait environ :",
  ["0,3 % du PIB mondial", "2,3 % du PIB mondial",
   "5,1 % du PIB mondial", "7 % du PIB mondial"], 1,
  "Bonne réponse : B. Un découplage stratégique limité coûte déjà environ 0,3 % ; une transition très brutale peut atteindre 7 % dans certains scénarios.",
  ['fmi', 'fragmentation', 'chiffres'])
q('qcm', "Les pays les plus affectés par une fragmentation en blocs sont :",
  ["Les économies avancées", "Les pays à faible revenu",
   "Les pays exportateurs de pétrole", "Les membres du G7"], 1,
  "Bonne réponse : B. Ils sont plus dépendants des importations, moins diversifiés, moins capables de reconstruire rapidement leurs chaînes de valeur et plus vulnérables aux hausses de prix.",
  ['fmi', 'fragmentation', 'développement'])
q('qcm', "Dans les simulations de l’OMC pour 2026, un monde organisé uniquement par des accords de libre-échange :",
  ["Est plus favorable qu’un monde fragmenté",
   "Est plus coûteux qu’un monde géopolitiquement fragmenté (−6,9 % contre −5,1 % de PIB)",
   "Laisse le PIB mondial inchangé",
   "Augmente les exportations mondiales"], 1,
  "Bonne réponse : B. Les accords préférentiels fragmentent les règles, discriminent les économies extérieures et amplifient le « bol de spaghettis » : le PIB recule de 6,9 % et les exportations de 26,9 %.",
  ['omc', 'scénarios', 'chiffres'])
q('qcm', "Selon ces mêmes simulations, une coopération multilatérale renforcée produirait :",
  ["+2,9 % de PIB mondial et +17,9 % d’exportations",
   "−2,9 % de PIB mondial", "Aucun effet", "+10 % de PIB mondial"], 0,
  "Bonne réponse : A. Le gain de PIB pourrait atteindre environ +7,7 % pour les pays les moins avancés : la coopération universelle bénéficie surtout aux économies petites et pauvres, dont le pouvoir de négociation bilatéral est faible.",
  ['omc', 'coopération', 'chiffres'])
q('qcm', "Entre 2010 et 2024, selon les données du Trésor citées par le cours :",
  ["Les échanges entre alliés américains reculent de 40 %",
   "Les importations des alliés américains provenant d’autres alliés augmentent d’environ 40 % relativement aux autres partenaires",
   "Les échanges avec les alliés de la Russie augmentent de 80 %",
   "Aucune réorientation n’est observable"], 1,
  "Bonne réponse : B. Symétriquement, les échanges avec les alliés de la Russie reculent d’environ 80 % relativement aux pays n’appartenant pas à ces blocs : la fragmentation est déjà visible dans les flux réels.",
  ['fragmentation', 'chiffres', 'géopolitique'])
q('qcm', "Un découplage complet avec la Chine est difficilement compatible avec la transition écologique parce que :",
  ["La Chine produit la totalité des éoliennes mondiales",
   "Le raffinage et la transformation de nombreux minerais critiques y sont très concentrés",
   "Les technologies bas-carbone sont brevetées en Chine",
   "La Chine finance la transition européenne"], 1,
  "Bonne réponse : B. L’extraction du cuivre, du nickel, du cobalt, des terres rares et du lithium est déjà concentrée, mais leur traitement l’est davantage encore, et la Chine y occupe une place centrale.",
  ['minerais critiques', 'transition écologique', 'dépendance'])
q('qcm', "La « grande convergence » désigne :",
  ["La convergence des politiques monétaires",
   "La réduction des écarts de revenu entre économies avancées et émergentes",
   "L’harmonisation des normes comptables",
   "La convergence des taux de change"], 1,
  "Bonne réponse : B. La fragmentation menace cette dynamique : en réduisant l’accès aux marchés, aux capitaux et aux technologies, elle pourrait ralentir davantage la croissance des PED et rouvrir les écarts de revenu.",
  ['convergence', 'développement', 'fragmentation'])
q('qcm', "Le MACF consiste à :",
  ["Subventionner les exportations européennes",
   "Faire supporter à certaines importations un coût carbone correspondant à celui applicable dans l’UE",
   "Interdire les importations carbonées",
   "Taxer les entreprises européennes polluantes"], 1,
  "Bonne réponse : B. Il calcule les émissions incorporées, tient compte du prix du carbone déjà payé à l’étranger et limite ainsi les fuites de carbone tout en incitant les producteurs étrangers à décarboner.",
  ['macf', 'climat', 'europe'])
q('qcm', "La puissance normative européenne repose principalement sur :",
  ["Sa puissance militaire", "La taille de son marché, environ 450 millions de consommateurs",
   "Son excédent commercial", "Sa monnaie unique"], 1,
  "Bonne réponse : B. De nombreuses entreprises étrangères ne peuvent pas renoncer à ce marché : l’Union peut donc imposer indirectement ses normes en conditionnant l’accès à son respect.",
  ['europe', 'puissance normative', 'chiffres'])
q('qcm', "Selon Bensidoun et Péron, la difficulté européenne tient principalement à :",
  ["Une absence totale de puissance économique",
   "La difficulté à transformer ses ressources en capacité d’action stratégique",
   "L’absence d’industries avancées",
   "Le refus des États membres de coopérer"], 1,
  "Bonne réponse : B. L’Union possède un grand marché, une puissance normative, des industries avancées et un capital humain qualifié, mais elle a été construite pour un ordre fondé sur les règles alors que les États-Unis et la Chine privilégient les rapports de force.",
  ['bensidoun', 'péron', 'europe'])
q('qcm', "Pour Kindleberger, un leader hégémonique doit réunir :",
  ["Une armée puissante et une monnaie forte",
   "Une puissance suffisante pour faire respecter les règles et une légitimité suffisante pour être suivi",
   "Un excédent commercial et un excédent budgétaire",
   "Une population nombreuse et un territoire vaste"], 1,
  "Bonne réponse : B. C’est pourquoi la crise actuelle est aussi une crise d’hégémonie : la Chine dispose de la puissance économique mais son aptitude à être acceptée comme leader bienveillant est contestée, tandis que l’Union européenne possède la légitimité réglementaire mais une puissance géopolitique plus limitée.",
  ['kindleberger', 'hégémonie', 'crise'])
q('qcm', "Une issue envisagée par le cours à la crise d’hégémonie est :",
  ["Le retour d’un hégémon unique",
   "Plusieurs leaderships sectoriels : sécurité et finance, climat et normes, autres biens publics",
   "La disparition de toute règle internationale",
   "La fusion de l’OMC et du FMI"], 1,
  "Bonne réponse : B. On passerait d’un leader hégémonique unique à une gouvernance à plusieurs niveaux, chaque acteur assumant la fourniture de biens publics mondiaux dans le domaine où il dispose d’une capacité d’entraînement.",
  ['hégémonie', 'leadership sectoriel', 'gouvernance'])
q('qcm', "Pour Arnaud Orain, le troisième âge du capitalisme de la finitude apparaît :",
  ["Au XVIe siècle", "Pendant la première mondialisation",
   "Après la crise des subprimes, renforcé après 2020", "En 1947"], 2,
  "Bonne réponse : C. Le premier âge est la période mercantiliste, le deuxième la première mondialisation et l’impérialisme colonial, le troisième la réapparition contemporaine de cette logique.",
  ['orain', 'finitude', 'mercantilisme'])
q('qcm', "Selon Milanovic, le « libéralisme de marché national » signifie :",
  ["La fin du marché", "Libéralisme à l’intérieur et mercantilisme à l’extérieur",
   "Mercantilisme à l’intérieur et libéralisme à l’extérieur",
   "Le retour au consensus de Washington"], 1,
  "Bonne réponse : B. La grande transformation contemporaine n’est pas la disparition du marché mais sa renationalisation, ce qui constitue une rupture avec le consensus de Washington.",
  ['milanovic', 'libéralisme de marché national'])
q('qcm', "Les trois caractéristiques de la « mondialisation fragmentée » selon Kesslassy et Rodrigues sont :",
  ["Libéralisation, dérégulation et privatisation",
   "Reprise en main du politique, recul du multilatéralisme, captation des ressources stratégiques",
   "Croissance, inflation et chômage",
   "Régionalisation, numérisation et financiarisation"], 1,
  "Bonne réponse : B. Derrière les stratégies unilatérales, bilatérales et régionales se trouve une même préoccupation : la souveraineté. Le risque associé est celui d’une tragédie des biens communs.",
  ['kesslassy', 'rodrigues', 'mondialisation fragmentée'])
q('qcm', "Le cours qualifie de « zèbres » :",
  ["Les pays les moins avancés", "Les puissances intermédiaires situées entre États-Unis et Chine",
   "Les membres du groupe de Cairns", "Les économies en transition"], 1,
  "Bonne réponse : B. Ces puissances intermédiaires répondent à l’unilatéralisme des deux grandes puissances notamment par la multiplication des accords commerciaux.",
  ['zèbres', 'puissances intermédiaires'])
q('qcm', "L’arbitrage fondamental de la réduction des dépendances stratégiques oppose :",
  ["Inflation et chômage", "Souveraineté et efficacité",
   "Épargne et investissement", "Court terme et long terme uniquement"], 1,
  "Bonne réponse : B. Raccourcir les chaînes de valeur accroît la résilience mais élève les coûts de production et donc potentiellement les prix : la question devient de savoir si la société civile acceptera le coût économique de la souveraineté.",
  ['souveraineté', 'arbitrage', 'chaînes de valeur'])

# ----------------------------------------------------------- vrai / faux
q('vrai/faux', "Le GATT était dès 1947 une organisation internationale dotée de la personnalité juridique.",
  ["Vrai", "Faux"], 1,
  "Faux. Le projet d’Organisation internationale du commerce n’a pas abouti, notamment faute de ratification de la Charte de La Havane par les États-Unis. Le GATT n’est qu’un accord commercial ; l’institution permanente naît en 1995 avec l’OMC.",
  ['gatt', 'oic', 'piège'])
q('vrai/faux', "La clause de la nation la plus favorisée oblige à étendre à tous les membres un avantage accordé à un partenaire.",
  ["Vrai", "Faux"], 0,
  "Vrai. C’est l’article I du GATT : la clause transforme une concession bilatérale en instrument de libéralisation multilatérale et rend l’adhésion attractive, puisqu’un nouvel entrant bénéficie des concessions déjà négociées. Les ACR y dérogent au titre de l’article XXIV.",
  ['npf', 'gatt'])
q('vrai/faux', "Un accord commercial régional est, par principe, interdit par les règles de l’OMC.",
  ["Vrai", "Faux"], 1,
  "Faux. Il déroge à la clause NPF, mais le GATT prévoit des exceptions pour les zones de libre-échange et les unions douanières, notamment à l’article XXIV, sous réserve de conditions juridiques et d’obligations de notification.",
  ['acr', 'article xxiv', 'piège'])
q('vrai/faux', "Toute subvention écologique est automatiquement autorisée par l’Accord SMC.",
  ["Vrai", "Faux"], 1,
  "Faux. La catégorie dite « verte », qui abritait certaines aides à la recherche, régionales ou d’adaptation environnementale, a expiré en 1999. Ces aides doivent être examinées au regard des règles actuellement applicables.",
  ['smc', 'subventions', 'piège'])
q('vrai/faux', "Une mesure de sauvegarde suppose de démontrer une pratique déloyale de la part du partenaire.",
  ["Vrai", "Faux"], 1,
  "Faux. La sauvegarde répond à un dommage grave causé par une augmentation des importations, même en l’absence de concurrence déloyale. C’est précisément ce qui la distingue de l’antidumping et des droits compensateurs.",
  ['sauvegarde', 'antidumping', 'piège'])
q('vrai/faux', "Dans une union douanière, chaque membre conserve sa propre politique commerciale vis-à-vis des pays tiers.",
  ["Vrai", "Faux"], 1,
  "Faux. C’est le cas dans une zone de libre-échange. L’union douanière ajoute précisément un tarif extérieur commun, ce qui conduit les États à renoncer à une partie de leur autonomie commerciale.",
  ['balassa', 'union douanière', 'piège'])
q('vrai/faux', "Une hausse du commerce intra-zone prouve qu’un accord régional améliore le bien-être.",
  ["Vrai", "Faux"], 1,
  "Faux. Le détournement de trafic augmente lui aussi les échanges internes tout en dégradant l’allocation mondiale des ressources, puisqu’un fournisseur plus efficace est abandonné. Seule la comparaison avec la création de trafic permet de conclure.",
  ['viner', 'piège', 'évaluation'])
q('vrai/faux', "Le cycle de Doha a abouti à un accord global en 2015.",
  ["Vrai", "Faux"], 1,
  "Faux. L’incapacité des membres à s’accorder en 2015-2016 confirme au contraire l’impasse des négociations globales. Certains accords sectoriels ou plus limités ont toutefois continué d’être conclus : l’échec concerne l’ambition d’un grand compromis unique.",
  ['doha', 'piège'])
q('vrai/faux', "La libéralisation commerciale explique l’essentiel de la croissance du commerce mondial depuis 1945.",
  ["Vrai", "Faux"], 1,
  "Faux. Dans la décomposition attribuée à Findlay et O’Rourke (2002), la hausse des revenus explique environ 67 % de la croissance du commerce, la réduction des droits de douane 25 % et la baisse des coûts de transport 8 %.",
  ['findlay', 'o’rourke', 'piège'])
q('vrai/faux', "La Chine a formellement perdu son statut de pays en développement à l’OMC en septembre 2025.",
  ["Vrai", "Faux"], 1,
  "Faux. Elle a annoncé qu’elle ne demanderait plus de nouveaux avantages de traitement spécial et différencié dans les négociations actuelles et futures : son statut n’a pas été formellement supprimé et ses avantages existants n’ont pas automatiquement disparu.",
  ['chine', 'omc', 'piège'])
q('vrai/faux', "La fragmentation géoéconomique signifie la disparition du commerce international.",
  ["Vrai", "Faux"], 1,
  "Faux. Les flux ne disparaissent pas, ils se recomposent selon les alliances géopolitiques. Guimbard et les travaux cités montrent que le commerce résiste mais change de géographie ; la fragmentation a un coût, elle n’est pas une démondialisation.",
  ['fragmentation', 'piège'])
q('vrai/faux', "Le G20 dispose d’un pouvoir juridiquement contraignant comparable à celui de l’OMC.",
  ["Vrai", "Faux"], 1,
  "Faux. Le G20 ne constitue pas une organisation internationale dotée de règles contraignantes : il coordonne les grandes puissances sur des orientations communes, comme l’engagement de novembre 2008 contre le protectionnisme ou le taux minimum d’imposition.",
  ['g20', 'piège', 'gouvernance'])
q('vrai/faux', "Pour Montesquieu, le commerce pacifie parce qu’il rend les nations réciproquement dépendantes.",
  ["Vrai", "Faux"], 0,
  "Vrai. Le mécanisme est économique et non moral : l’interdépendance élève le coût d’un conflit et crée donc une incitation à la paix. La CECA de 1951 en constitue l’application institutionnelle.",
  ['montesquieu', 'ceca'])
q('vrai/faux', "Selon le trilemme de Rodrik, il est possible de maximiser simultanément hypermondialisation, démocratie et souveraineté nationale.",
  ["Vrai", "Faux"], 1,
  "Faux. On peut en conserver deux, jamais les trois. Préserver démocratie et souveraineté implique de limiter l’hypermondialisation ; conserver hypermondialisation et souveraineté réduit l’autonomie démocratique ; associer démocratie et hypermondialisation exigerait une gouvernance supranationale très approfondie.",
  ['rodrik', 'trilemme', 'piège'])
q('vrai/faux', "L’agriculture est aujourd’hui moins protégée que l’industrie.",
  ["Vrai", "Faux"], 1,
  "Faux. En 2019, le droit de douane moyen mondial atteint 15,9 % dans l’agriculture contre environ 3 % dans l’industrie : l’agriculture demeure l’exception sectorielle majeure à la libéralisation.",
  ['agriculture', 'chiffres', 'piège'])
q('vrai/faux', "Le groupe de Cairns défend le maintien des subventions agricoles des pays développés.",
  ["Vrai", "Faux"], 1,
  "Faux. Il rassemble au contraire des pays exportateurs agricoles favorables à une plus grande libéralisation des échanges agricoles et conteste, avec des coalitions de PED, les subventions américaines et européennes.",
  ['cairns', 'piège', 'agriculture'])
q('vrai/faux', "L’accord multifibres constituait une dérogation protectionniste aux règles générales du GATT.",
  ["Vrai", "Faux"], 0,
  "Vrai. Entré en vigueur en 1974, il permettait aux pays développés de limiter par des quotas certaines importations textiles face à la concurrence des pays à faibles coûts salariaux. L’Uruguay Round en organise le démantèlement, achevé le 1er janvier 2005.",
  ['accord multifibres', 'textile'])
q('vrai/faux', "La création de l’ASEAN en 1967 répond à des motifs exclusivement économiques.",
  ["Vrai", "Faux"], 1,
  "Faux. Sa création intervient en pleine guerre froide, dans un environnement marqué par la Chine communiste, la guerre du Vietnam et les tensions idéologiques régionales : la dimension est dès l’origine politique autant qu’économique.",
  ['asean', 'piège', 'géopolitique'])
q('vrai/faux', "Supprimer les droits de douane suffit à créer une forte intégration commerciale régionale.",
  ["Vrai", "Faux"], 1,
  "Faux. La ZLECAf le montre : lorsque les économies ont des structures productives proches et des infrastructures insuffisantes, la complémentarité reste limitée et le commerce intra-zone faible malgré la libéralisation.",
  ['zlecaf', 'complémentarité', 'piège'])
q('vrai/faux', "Les accords commerciaux contemporains se limitent à la réduction des droits de douane.",
  ["Vrai", "Faux"], 1,
  "Faux. Les accords profonds portent sur les normes sociales, l’environnement, le droit du travail, la concurrence, les investissements, la propriété intellectuelle, les marchés publics et les normes sanitaires : ils deviennent des instruments de diffusion de normes.",
  ['lawrence', 'accords profonds', 'piège'])
q('vrai/faux', "Le climat est un bien public mondial parce qu’il est rival et excluable.",
  ["Vrai", "Faux"], 1,
  "Faux. C’est l’inverse : la stabilité climatique est non rivale — le fait qu’un pays en bénéficie n’empêche pas les autres — et difficilement excluable, puisqu’on ne peut la réserver aux seuls pays ayant financé les réductions d’émissions.",
  ['climat', 'bien public mondial', 'piège'])
q('vrai/faux', "Un monde organisé uniquement autour d’accords de libre-échange serait, selon l’OMC, préférable à un monde fragmenté en blocs.",
  ["Vrai", "Faux"], 1,
  "Faux. Les simulations donnent −6,9 % de PIB mondial et −26,9 % d’exportations pour le scénario des accords préférentiels, contre −5,1 % et −18,6 % pour le scénario géopolitiquement fragmenté : la fragmentation des règles coûte encore plus cher.",
  ['omc', 'scénarios', 'piège'])

# ------------------------------------------------------ questions ouvertes
q('question ouverte', "Expliquez le passage de la « mondialisation heureuse » à la « mondialisation dangereuse ».",
  [], 0,
  "Au début des années 1990, un consensus associe ouverture, prospérité et pacification : la mondialisation apparaît comme une dynamique historique et une source de progrès, et le taux d’ouverture s’élève. Ce consensus repose sur la lecture de Montesquieu — le commerce crée de l’interdépendance, donc un coût du conflit, donc une incitation à la paix — dont la CECA de 1951 est l’application. Il se défait pour trois raisons. D’abord, les analyses marxistes rappellent que des échanges asymétriques produisent dépendance et domination. Ensuite, Luttwak annonce dès 1990 que la fin de la guerre froide déplace la rivalité vers le terrain économique : les droits de douane deviennent des instruments de domination technologique et monétaire. Enfin, Baldwin formule le renversement : le commerce, opportunité, devient vulnérabilité. Les États cherchent alors à dérisquer et à pratiquer le friendshoring, ce qui engendre des blocs géoéconomiques.",
  ['mondialisation dangereuse', 'luttwak', 'baldwin'])
q('question ouverte', "Pourquoi une gouvernance mondiale est-elle nécessaire ? Appuyez-vous sur la notion de bien public mondial.",
  [], 0,
  "Un bien public mondial est non rival — sa consommation par un acteur n’empêche pas les autres d’en bénéficier — et non excluable — il est difficile d’en empêcher l’accès. Climat et biodiversité, stabilité financière, stabilité du commerce international et règles commerciales équitables en relèvent. Ces deux propriétés créent un problème d’action collective : chaque État a intérêt à laisser les autres supporter le coût, ce qui est le comportement de passager clandestin. Le résultat est un équilibre de Nash sous-optimal, dans lequel aucun acteur n’a intérêt à dévier unilatéralement alors même que le bien collectif est sous-produit. La gouvernance mondiale vise à sortir de cet équilibre en établissant des règles de bonne conduite qui coordonnent les comportements nationaux. Kindleberger ajoute que cette coordination est fragile si aucune puissance n’accepte d’en assumer le coût.",
  ['bien public mondial', 'passager clandestin', 'nash'])
q('question ouverte', "Présentez la théorie de la stabilité hégémonique de Kindleberger et son application après 1945.",
  [], 0,
  "Kindleberger soutient dans La Grande Dépression mondiale, 1929-1939 (1973) puis dans son article de 1981 qu’un ordre économique international stable suppose qu’une puissance dominante accepte d’assumer des responsabilités collectives : système monétaire stable, cadre commercial ouvert, liquidités en période de crise, mécanismes de coopération. Ces biens profitant à tous, chacun est tenté de laisser les autres les financer. La matrice du cours formalise cette asymétrie : coopération mutuelle (4 ; 4), défection du suiveur (3 ; 5), double défection (2 ; 3) — le suiveur gagne donc à ne pas coopérer tant que le leader coopère. Après 1945, seuls les États-Unis disposent des moyens nécessaires, avec environ 60 % de la production mondiale et 70 % des réserves d’or. Ils organisent les trois piliers de l’ordre nouveau : plan Marshall et BIRD pour la reconstruction, Bretton Woods et le FMI pour la stabilité monétaire, le GATT pour la relance des échanges.",
  ['kindleberger', 'hégémonie', 'après-guerre'])
q('question ouverte', "Qu’appelle-t-on « mercantilisme éclairé » et pourquoi cette logique a-t-elle produit la libéralisation ?",
  [], 0,
  "Dans les théories traditionnelles — Ricardo, modèle HOS — l’importation est le gain même de l’échange, puisqu’elle procure à moindre coût ce qu’il serait coûteux de produire nationalement. Or dans les négociations du GATT, les États raisonnent politiquement à l’inverse : les exportations sont traitées comme un gain et les importations comme une concession. Krugman nomme cette logique mercantilisme éclairé. Le paradoxe est qu’elle fonctionne : parce que chaque pays veut obtenir des débouchés, il accepte d’ouvrir son propre marché, et la réciprocité transforme le marchandage en libéralisation collective. La clause de la nation la plus favorisée généralise ensuite les concessions à tous les membres. La libéralisation du second XXe siècle n’est donc pas le produit d’une conversion théorique des gouvernements, mais d’un mécanisme institutionnel qui rend l’ouverture politiquement acceptable.",
  ['krugman', 'mercantilisme éclairé', 'réciprocité'])
q('question ouverte', "Présentez les trois principes du GATT et montrez que les exceptions ne les contredisent pas.",
  [], 0,
  "La non-discrimination repose sur deux clauses : la nation la plus favorisée (article I), qui étend à tous un avantage accordé à un partenaire, et le traitement national (article III), qui interdit de traiter un produit importé moins favorablement qu’un produit national comparable. La réciprocité rend l’ouverture politiquement acceptable en garantissant des contreparties. La transparence privilégie des instruments identifiables et négociables — les droits de douane — aux mesures opaques. Les exceptions ne ruinent pas ces principes : elles les rendent praticables. Les ACR dérogent à la NPF au titre de l’article XXIV mais doivent respecter des conditions et être notifiés. Le traitement spécial et différencié et le SGP reconnaissent que l’égalité formelle des règles ne garantit pas l’égalité des capacités. Les sauvegardes de l’article XIX offrent un délai d’ajustement sans légaliser une protection permanente. L’Accord SMC distingue les subventions prohibées, contestables et, jusqu’en 1999, non actionnables.",
  ['gatt', 'principes', 'exceptions'])
q('question ouverte', "Pourquoi l’agriculture constitue-t-elle l’exception majeure à la libéralisation commerciale ?",
  [], 0,
  "En 2019, le droit de douane moyen mondial atteint 15,9 % dans l’agriculture contre environ 3 % dans l’industrie. Cette protection s’explique par des enjeux de sécurité alimentaire, de maintien des revenus agricoles, de stabilité des territoires ruraux, de souveraineté et de protection contre la volatilité des prix mondiaux. Elle est ancienne : l’Agricultural Adjustment Act de 1933, dans le cadre du New Deal, inaugure un soutien structuré ensuite par les Farm Bills ; la PAC de 1962 reprend l’idée d’un soutien aux revenus et aux prix. Mais ces politiques peuvent fausser la concurrence internationale au détriment des pays qui n’ont pas les mêmes moyens budgétaires. Le groupe de Cairns et des coalitions de PED, notamment autour du Brésil, les contestent — l’exemple du coton américain et de ses effets sur les producteurs africains est explicite. C’est l’un des principaux facteurs d’enlisement du cycle de Doha.",
  ['agriculture', 'pac', 'cairns'])
q('question ouverte', "Que montre l’exemple sénégalais sur les limites des politiques de soutien agricole ?",
  [], 0,
  "Le Sénégal a historiquement soutenu sa production d’arachides, filière ayant représenté jusqu’à 40 % des terres cultivées. Le développement d’une culture largement destinée à l’exportation s’est fait au détriment de la diversification agricole, des cultures vivrières destinées à la population locale, de la sécurité alimentaire et de la préservation des sols. Les émeutes de la faim de 2007-2008 constituent un tournant : le pays cherche à renforcer son autosuffisance et lance un programme d’intensification de la riziculture afin de réduire sa dépendance aux importations alimentaires. Mais l’intensification peut elle-même appauvrir les sols, et le Sénégal s’oriente désormais vers une diversification plus large — autres céréales, notamment le mil, fruits et légumes. L’exemple montre qu’une politique de soutien peut renforcer une spécialisation au détriment de la résilience, et que la recherche d’autosuffisance doit être conciliée avec la soutenabilité environnementale.",
  ['sénégal', 'arachide', 'sécurité alimentaire'])
q('question ouverte', "Retracez les grands cycles de négociation du GATT et leur élargissement progressif.",
  [], 0,
  "Les quatre premiers cycles — Genève 1947 (23 participants), Annecy 1949 (33), Torquay 1951 (34), Genève 1955-1956 (34) — visent essentiellement la réduction des droits de douane sur les produits manufacturés, avec un ordre de grandeur d’environ 12 % en 1962. Le Kennedy Round (1964-1967, 48 participants) poursuit la baisse vers environ 7 % et produit un premier code antidumping. Le Tokyo Round (1973-1979, 99 participants) se déroule dans un contexte de crise — chocs pétroliers, inflation, fin du système de Bretton Woods confirmée par les accords de la Jamaïque de 1976 — et son apport essentiel est l’encadrement des obstacles non tarifaires, avec un accord sur les subventions en 1979. L’Uruguay Round (1986-1994, 106 puis 123 participants) abaisse les droits vers environ 4 %, étend les règles à l’agriculture, au textile, aux services et à la propriété intellectuelle, et crée l’OMC. Le cycle de Doha, lancé en 2001, échoue : l’élargissement des participants et des sujets rend le compromis global impossible.",
  ['rounds', 'gatt', 'doha'])
q('question ouverte', "Pourquoi le cycle de Doha s’est-il enlisé ?",
  [], 0,
  "Doha est présenté comme un cycle pour le développement : les PED estiment que les règles antérieures ont surtout bénéficié aux économies avancées et demandent un meilleur accès aux marchés, une réduction des soutiens agricoles du Nord, davantage de flexibilités et un accès facilité aux technologies. Le programme comporte un ensemble très large de sujets, souvent présenté comme 21 thèmes : agriculture, propriété intellectuelle et accès aux médicaments, concurrence, environnement, transferts de technologie, services. Pour éviter une libéralisation sélective, les négociations reposent sur l’engagement unique — « rien n’est convenu tant que tout n’est pas convenu ». Or plus le nombre de pays, de sujets et d’intérêts divergents augmente, plus le compromis devient difficile : les pays avancés veulent l’ouverture des marchés industriels et des services, les PED exigent en contrepartie une réduction des protections agricoles que les premiers refusent. L’ambition du cycle devient ainsi sa principale faiblesse, confirmée par l’échec de 2015-2016.",
  ['doha', 'engagement unique', 'blocage'])
q('question ouverte', "Dressez le bilan du multilatéralisme commercial : succès et limites.",
  [], 0,
  "Trois succès. D’abord une réduction spectaculaire des droits de douane, d’environ 40 % au départ à 3 ou 4 % sur les produits manufacturés dans les économies avancées. Ensuite un élargissement considérable : 23 pays en 1947, 123 participants à la conclusion de l’Uruguay Round, 166 membres de l’OMC en 2026, la Chine ayant adhéré en 2001. Enfin une extension des domaines régulés : du seul tarif au dumping, aux subventions, aux obstacles non tarifaires, à l’agriculture, au textile, aux services et à la propriété intellectuelle. Trois limites symétriques. La multiplication des participants et des thèmes rend les compromis plus difficiles, puisque pays avancés, PED et émergents poursuivent des objectifs opposés. Le retour des intérêts nationaux et des rivalités stratégiques transforme la coopération commerciale en concurrence économique. Enfin l’essoufflement déplace les négociations vers des cadres plus restreints, ce qui fragmente les règles. Il faut ajouter que la libéralisation n’explique qu’une part de la croissance du commerce : 25 % contre 67 % pour la hausse des revenus dans la décomposition de Findlay et O’Rourke.",
  ['bilan', 'multilatéralisme', 'findlay'])
q('question ouverte', "Présentez la typologie de Balassa et dites ce qu’elle permet d’éviter comme confusion.",
  [], 0,
  "Balassa distingue en 1961 cinq étapes. La zone de libre-échange supprime les droits internes, chaque membre conservant sa politique commerciale extérieure : deux membres peuvent donc appliquer des droits différents au même produit tiers — d’où l’importance des règles d’origine. L’union douanière ajoute un tarif extérieur commun, ce qui fait renoncer les États à une part de leur autonomie commerciale. Le marché commun ajoute la libre circulation du travail et du capital. L’union économique et monétaire coordonne les politiques économiques et peut conduire à une monnaie commune. L’intégration totale unifie les politiques sous une autorité supranationale, l’intégration économique devenant politique. Cette typologie évite deux confusions fréquentes : traiter toute zone préférentielle d’union douanière, et croire que l’Union européenne serait une simple zone de libre-échange, alors que la politique commerciale y relève du niveau européen et qu’une partie de ses membres partage l’euro.",
  ['balassa', 'intégration', 'typologie'])
q('question ouverte', "Expliquez l’analyse de Viner et son intérêt pour évaluer un accord régional.",
  [], 0,
  "Viner montre en 1950 qu’une union douanière n’améliore pas nécessairement le bien-être parce qu’elle produit simultanément deux effets. La création de trafic apparaît lorsqu’une production domestique coûteuse est remplacée par une importation moins chère venant d’un partenaire : les coûts baissent, la spécialisation progresse, le bien-être augmente. Le détournement de trafic apparaît lorsque la préférence tarifaire conduit à abandonner un fournisseur extérieur pourtant plus efficace, parce que son prix augmenté du droit de douane devient supérieur à celui du partenaire exonéré : l’allocation mondiale se dégrade. Le bilan dépend donc de l’effet dominant. L’intérêt analytique est décisif : la hausse des échanges intra-zone ne prouve rien, puisque le détournement de trafic l’augmente aussi. L’ASEAN illustre une création de trafic dominante — 4 % à 8 % des exportations mondiales — tandis que la ZLECAf montre qu’une libéralisation sans complémentarité productive ne suffit pas.",
  ['viner', 'asean', 'zlecaf'])
q('question ouverte', "En quoi les accords commerciaux contemporains sont-ils de moins en moins « régionaux » et de moins en moins « commerciaux » ?",
  [], 0,
  "De moins en moins régionaux : les accords relient désormais des économies très éloignées géographiquement — Union européenne et Canada, Union européenne et Vietnam, Union européenne et Mercosur, accords avec l’Inde, partenariats transpacifiques — sans correspondre à une région cohérente. De moins en moins commerciaux : suivant la distinction de Lawrence entre intégration superficielle et intégration profonde, ils ne se contentent plus de supprimer les barrières aux frontières mais rapprochent les règles internes — normes sociales, environnement, droit du travail, concurrence, investissements, propriété intellectuelle, marchés publics, normes sanitaires. L’accord UE-Vietnam engage ainsi le Vietnam sur la liberté syndicale et les conventions fondamentales de l’OIT. Ces accords profonds reprennent les thèmes que les négociations multilatérales n’ont pas su traiter : ils deviennent des instruments de gouvernance et de diffusion de normes, ce qui explique aussi l’intensité des oppositions qu’ils suscitent.",
  ['lawrence', 'accords profonds', 'normes'])
q('question ouverte', "Qu’est-ce que le « bol de spaghettis » et quel est son coût économique ?",
  [], 0,
  "Bhagwati critique en 1995 la multiplication des accords préférentiels. Chaque accord fixe ses propres droits, règles d’origine, normes, exceptions, procédures et mécanismes de règlement ; or un même pays participe à plusieurs accords et doit donc respecter plusieurs ensembles de règles superposées. Bhagwati compare ces accords entremêlés à des spaghettis, image que Baldwin illustre en 2008 avec l’Amérique latine. Le coût n’est plus tarifaire mais administratif : multiplication des règles d’origine, hausse des coûts de conformité, incertitude accrue pour les entreprises, perte de lisibilité du système. La régionalisation peut donc paradoxalement compliquer le commerce qu’elle prétend faciliter. Les simulations de l’OMC chiffrent cette intuition : un monde organisé uniquement autour d’accords de libre-échange coûterait 6,9 % de PIB mondial et 26,9 % d’exportations, soit davantage encore qu’un monde fragmenté en blocs géopolitiques.",
  ['bhagwati', 'bol de spaghettis', 'omc'])
q('question ouverte', "Pourquoi parle-t-on d’une gouvernance « hybride » de la mondialisation ?",
  [], 0,
  "Parce qu’il n’existe plus une seule institution capable de déterminer les règles. Celles-ci sont désormais produites par l’OMC, par les États, par les accords commerciaux régionaux, par les grandes puissances réglementaires, par les firmes multinationales et par les forums intergouvernementaux comme le G7 et le G20. Trois évolutions expliquent ce basculement. L’échec de Doha prive l’OMC de sa capacité à produire de nouvelles règles consensuelles et la fragilise comme institution. Sa légitimité est contestée sur le fond : les PED estiment que l’ordre construit par les économies avancées les défavorise, l’agriculture et la propriété intellectuelle en étant les exemples majeurs — les débats sur l’accès aux trithérapies puis lors de la pandémie de Covid-19 montrent la tension entre brevets et objectif sanitaire mondial. Enfin les FMN, par la mobilité de leurs investissements, mettent les territoires en concurrence. Le risque est que la multiplication des niveaux produise des normes contradictoires.",
  ['gouvernance hybride', 'omc', 'fmn'])
q('question ouverte', "Expliquez le trilemme de Rodrik et les trois configurations possibles.",
  [], 0,
  "Rodrik soutient qu’il est impossible de combiner pleinement hypermondialisation, démocratie et souveraineté nationale : on peut en conserver deux, jamais les trois. Première configuration : souveraineté et démocratie supposent de limiter l’hypermondialisation, puisque la mobilité du capital intensifie la concurrence fiscale et réduit la capacité de taxation nationale ; Rodrik rapproche cette solution du compromis de Bretton Woods, où l’ouverture reste importante mais où les États conservent des marges de manœuvre. Deuxième configuration : hypermondialisation et souveraineté nationale fragilisent la démocratie, les politiques devant se conformer aux exigences des marchés internationaux — c’est la « camisole dorée ». Troisième configuration : hypermondialisation et démocratie exigeraient une gouvernance politique mondiale, donc le transfert d’une part importante des compétences nationales à des institutions supranationales démocratiques, ce qui reste très difficile à construire. Le trilemme montre donc que l’intégration économique a un coût politique qu’aucune réforme technique ne supprime.",
  ['rodrik', 'trilemme', 'démocratie'])
q('question ouverte', "Quelle est la base sociale du rejet de l’hypermondialisation ?",
  [], 0,
  "Elle tient à la divergence entre croissance moyenne et niveaux de vie effectifs. Aux États-Unis, le PIB par habitant progresse fortement depuis les années 1980 alors que le revenu médian des ménages progresse beaucoup plus lentement : une partie des gains se concentre vers le haut de la distribution. En France, le niveau de vie des 10 % les plus riches progresse nettement, celui des catégories médianes plus modérément, celui des 10 % les plus pauvres de manière beaucoup plus faible et instable. Il en résulte un sentiment de déclassement relatif, même lorsque le niveau de vie moyen augmente. Deux réponses sont alors possibles : la redistribution interne ou la protection contre la concurrence étrangère. Une partie croissante du débat politique privilégie la seconde, car il est plus simple d’attribuer les difficultés à une cause extérieure — la logique MAGA aux États-Unis s’inscrit dans cette volonté de rétablir une souveraineté économique et productive. Rodrik objecte que la réponse durable passe par des « good jobs » et la productivité des services.",
  ['inégalités', 'rodrik', 'protectionnisme'])
q('question ouverte', "Présentez les trois scénarios de Sébastien Jean pour l’avenir du commerce international.",
  [], 0,
  "Premier scénario, la continuité sous tensions : l’OMC reste le cadre principal mais les tensions sino-américaines persistent et les pays recourent davantage aux exceptions — droits compensateurs, sanctions ciblées, restrictions temporaires, accords administrés. Les chaînes de valeur ne se réorganisent que dans les secteurs les plus stratégiques et l’économie mondiale reste globalement intégrée : le multilatéralisme est affaibli mais maintenu. Deuxième scénario, la confrontation : les sanctions se multiplient, les États-Unis cherchent à réduire fortement leur dépendance envers la Chine, les chaînes se réorganisent selon les alliances géopolitiques, les pays tiers subissent des pressions pour choisir leur camp — découplage, relocalisations, friend-shoring, blocs : c’est la fragmentation géo-économique. Troisième scénario, le compromis : les grandes puissances jugent le coût du conflit trop élevé et négocient une réforme portant sur les subventions industrielles, le statut des pays en développement, les transferts technologiques et le règlement des différends. Les évolutions récentes rapprochent du deuxième sans rendre les autres impossibles.",
  ['sébastien jean', 'scénarios', 'fragmentation'])
q('question ouverte', "Quel est le coût économique de la fragmentation géoéconomique ?",
  [], 0,
  "Bolhuis, Chen et Kett (FMI, 2023) chiffrent plusieurs scénarios. Un découplage stratégique limité — suppression de certains échanges entre la Russie et le bloc occidental, réduction du commerce technologique entre la Chine et les États-Unis ou l’Union européenne — entraîne déjà une perte permanente d’environ 0,3 % du PIB mondial. Une fragmentation complète en deux blocs coûte environ 2,3 % du PIB mondial, les pertes étant particulièrement fortes pour les pays à faible revenu, plus dépendants des importations et moins capables de reconstruire rapidement leurs chaînes. Une rupture brutale peut atteindre 7 % dans certains scénarios. L’OMC, dans son rapport de 2026, pousse l’analyse plus loin : un monde géopolitiquement fragmenté coûterait 5,1 % de PIB et 18,6 % d’exportations à l’horizon 2050, un monde d’accords préférentiels 6,9 % et 26,9 %, tandis qu’une coopération renforcée apporterait +2,9 % et +17,9 %, et jusqu’à +7,7 % de PIB pour les pays les moins avancés. La fragmentation menace donc aussi la grande convergence.",
  ['fmi', 'omc', 'coût de la fragmentation'])
q('question ouverte', "Pourquoi le climat impose-t-il de maintenir une gouvernance mondiale, et quel rôle l’Europe peut-elle y jouer ?",
  [], 0,
  "La stabilité climatique est non rivale et difficilement excluable : c’est un bien public mondial, donc exposé au passager clandestin. Si un pays réduit ses émissions pendant qu’un autre continue de polluer, le bénéfice reste mondial alors que le coût est national : chaque État a une incitation individuelle à laisser les autres agir, ce qui conduit à une production insuffisante du bien climatique. On retrouve exactement le problème de Kindleberger : il faudrait un acteur acceptant un rôle moteur. L’Union européenne peut partiellement le remplir, non par la puissance militaire ou technologique, mais par son marché : environ 450 millions de consommateurs au niveau de vie élevé auxquels les entreprises étrangères ne peuvent renoncer. Elle exerce ainsi une puissance normative, dont le MACF est l’instrument climatique : en faisant supporter aux importations un coût carbone équivalent à celui payé dans l’Union, il limite les fuites de carbone et incite les producteurs étrangers à décarboner pour conserver leur accès au marché.",
  ['climat', 'macf', 'europe'])
q('question ouverte', "En quoi la crise du multilatéralisme est-elle aussi une crise d’hégémonie ?",
  [], 0,
  "Pour Kindleberger, l’hégémon doit réunir deux conditions : être assez puissant pour faire respecter les règles et assez légitime pour que les autres acceptent de le suivre. Après 1945, les États-Unis réunissaient les deux et avaient intérêt à reconstruire les marchés étrangers pour disposer de débouchés. Aujourd’hui, leur puissance relative a reculé et, surtout, ils remettent eux-mêmes en cause des règles qu’ils avaient contribué à construire : le leadership est donc contesté. La Chine dispose de la puissance économique mais son aptitude à être acceptée comme garant impartial est discutée — subventions, entreprises publiques, restrictions commerciales, instrumentalisation des dépendances. L’Union européenne possède la légitimité réglementaire et une culture du multilatéralisme, mais une puissance géopolitique plus limitée, et Bensidoun et Péron montrent qu’elle est prise dans un étau entre America First et la concurrence industrielle chinoise. L’issue envisagée n’est donc pas un nouvel hégémon mais plusieurs leaderships sectoriels.",
  ['kindleberger', 'hégémonie', 'europe'])
q('question ouverte', "Comment le chapitre articule-t-il souveraineté et efficacité ?",
  [], 0,
  "La réduction des dépendances se heurte à un arbitrage explicite. Raccourcir les chaînes de valeur mondiales accroît la résilience mais augmente les coûts de production et donc potentiellement les prix : la question est de savoir si la société civile acceptera le coût économique de la souveraineté. Cet arbitrage se retrouve à tous les niveaux du chapitre. Chez Rodrik, il prend la forme du trilemme : préserver démocratie et souveraineté impose de limiter l’intégration. Chez Bolhuis, Chen et Kett, il se chiffre : 0,3 % du PIB mondial pour un découplage limité, 2,3 % pour deux blocs, jusqu’à 7 % en cas de transition brutale. Dans les simulations de l’OMC, il se complique : un monde d’accords préférentiels, pourtant présenté comme une alternative souple, coûterait plus cher qu’un monde de blocs. Enfin, le paradoxe de la fragmentation ajoute une dimension stratégique : moins d’interdépendance signifie un conflit moins coûteux, donc potentiellement plus probable. L’enjeu n’est donc pas mondialisation ou démondialisation, mais quelle forme de mondialisation et à quel niveau organiser les règles.",
  ['souveraineté', 'efficacité', 'arbitrage'])

TYPES = {'qcm': 'qcm', 'vrai/faux': 'vraifa', 'question ouverte': 'questi'}
QUIZ = []
TAGS = {}
for _i, (_t, _q, _o, _a, _e, _g) in enumerate(Q, 1):
    _id = 'ch24-%s-%d' % (TYPES[_t], _i)
    QUIZ.append({'type': _t, 'q': _q, 'opts': _o, 'ans': _a, 'exp': _e, 'ch': 24, 'id': _id})
    TAGS[_id] = _g
