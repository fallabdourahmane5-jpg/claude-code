# -*- coding: utf-8 -*-
"""Chapitre 3 — complément de questions « Appliquer » et « Raisonner ».

Le chapitre d'histoire de la pensée était très fourni en questions de
connaissance mais presque dépourvu de niveaux hauts. Ces questions font
donc travailler les raisonnements eux-mêmes : circuit de Quesnay, coût
d'opportunité ricardien, enchaînement vers l'état stationnaire, demande
effective de Malthus puis de Keynes, équilibre général, rigidités de la
NEK, régime d'accumulation et mode de régulation. Chaque renvoi a été
vérifié dans le texte du cours.
"""


def f(**kw):
    return kw


L = [

# ------------------------------- c3-01 · mercantilistes et physiocrates
f(id='q3-m01', sp='c3-01', niv='appliquer', type='assoc', b=59,
  q="Associez chaque type d’avances de Quesnay à ce qu’il recouvre.",
  ans=[["Avances annuelles", "Semences, engrais, entretien : du capital "
                             "circulant"],
       ["Avances primitives", "Bétail et matériel agricole : du capital fixe "
                              "durable"],
       ["Avances foncières", "Les investissements des propriétaires en "
                             "capital fixe"],
       ["Produit net", "La valeur annuelle de la production moins les "
                       "dépenses en capital"]],
  exp="Les avances sont l’ancêtre de la notion de capital : Quesnay comprend "
      "qu’il faut engager des dépenses avant toute récolte. La distinction "
      "entre ce qui se consomme dans l’année — les avances annuelles — et ce "
      "qui dure — les avances primitives et foncières — préfigure "
      "l’opposition entre consommation intermédiaire et investissement. Le "
      "produit net est ce qui reste une fois les avances remboursées : c’est "
      "le surplus qui fait vivre tout le circuit.",
  diss="Montrer que la notion de capital naît avec les physiocrates permet "
       "d’ouvrir une dissertation d’histoire de la pensée autrement que par "
       "Smith, et d’éclairer ce que Marx appellera plus tard reproduction."),

f(id='q3-m02', sp='c3-01', niv='raisonner', type='ordre', b=83,
  q="Remettez dans l’ordre l’enchaînement par lequel, selon Quesnay, une "
    "intervention de l’État sur les prix agricoles ruine l’économie.",
  ans=["L’État bloque les prix ou empêche l’exportation des grains",
       "Le revenu agricole baisse",
       "Les avances engagées par les cultivateurs diminuent",
       "Le produit net créé chaque année diminue",
       "Le circuit économique tout entier s’effondre, faute de surplus à "
       "faire circuler"],
  exp="Cet enchaînement est le cœur de l’argument physiocrate : puisque le "
      "produit net agricole irrigue toutes les classes, tout ce qui réduit le "
      "revenu de l’agriculture appauvrit la société entière. La conclusion "
      "politique en découle — « laissez faire les hommes, laissez passer les "
      "marchandises » — et fonde la justification libérale de la doctrine. "
      "Le raisonnement vaut par sa logique circulaire, même si sa prémisse — "
      "l’agriculture seule créatrice de richesse — sera abandonnée.",
  diss="Première formulation d’un argument qu’on retrouvera partout : "
       "l’intervention publique est critiquée non pour elle-même, mais pour "
       "les effets en chaîne qu’elle produit dans un circuit."),

f(id='q3-m03', sp='c3-01', niv='raisonner', type='vf', b=49,
  q="Vrai ou faux : chez Quesnay, la classe stérile est celle qui ne "
    "travaille pas. Justifiez.",
  ans=False,
  exp="« Stérile » ne veut pas dire inactive : les artisans, commerçants et "
      "manufacturiers travaillent, transforment et échangent. Ils sont dits "
      "stériles parce qu’ils ne créent aucun surplus nouveau : la valeur de "
      "ce qu’ils produisent égale celle de ce qu’ils ont consommé pour le "
      "produire. Seule l’agriculture tire parti du don gratuit de la nature "
      "et dégage un produit net. Le qualificatif est donc comptable, non "
      "moral — et c’est précisément ce que les classiques renverseront en "
      "reconnaissant l’industrie comme source d’enrichissement.",
  diss="Le contresens sur le mot « stérile » est classique en copie : le "
       "lever permet de montrer qu’une catégorie d’analyse se juge à sa "
       "définition, pas à sa connotation."),

# ------------------------------------- c3-02 · Smith, Ricardo, échange
f(id='q3-m04', sp='c3-02', niv='appliquer', type='qcm', b=163,
  q="Produire une unité de vin oblige un pays à renoncer à deux unités de "
    "drap. Quel est son coût d’opportunité, et que faut-il en conclure chez "
    "Ricardo ?",
  opts=["Le coût d’opportunité d’une unité de vin est de deux unités de "
        "drap : le pays a intérêt à se spécialiser là où ce coût est le plus "
        "faible",
        "Le coût d’opportunité est nul, puisque aucune dépense monétaire "
        "n’est engagée",
        "Le coût d’opportunité est de deux unités de vin",
        "Le coût d’opportunité ne se calcule qu’en situation d’avantage "
        "absolu"],
  ans=0,
  why=["Le coût d’opportunité n’est pas une dépense : c’est ce à quoi on "
       "renonce, mesuré en quantités d’un autre bien.",
       "L’énoncé inverse les termes : on renonce à du drap pour produire du "
       "vin.",
       "C’est justement l’inverse : Ricardo montre qu’un pays désavantagé "
       "dans les deux productions garde un avantage comparatif."],
  exp="Le cours définit le coût d’opportunité comme ce à quoi on renonce pour "
      "produire une unité supplémentaire d’un bien, et donne cet exemple "
      "exact. L’apport de Ricardo tient à la conséquence : même un pays plus "
      "productif dans les deux secteurs — le Portugal de l’exemple — a "
      "intérêt à se spécialiser là où son avantage est le plus grand, "
      "laissant l’autre production à l’Angleterre. L’échange est donc "
      "mutuellement avantageux sans qu’aucun avantage absolu ne soit requis.",
  diss="La distinction avantage absolu (Smith) / avantage comparatif "
       "(Ricardo) est le passage obligé de toute dissertation sur le "
       "libre-échange : seul le second explique pourquoi même les pays les "
       "moins productifs gagnent à l’échange."),

f(id='q3-m05', sp='c3-02', niv='raisonner', type='ordre', b=159,
  q="Remettez dans l’ordre l’enchaînement qui mène, chez Ricardo, à l’état "
    "stationnaire.",
  ans=["La population augmente, donc la demande de nourriture augmente",
       "Les meilleures terres étant déjà cultivées, il faut mettre en culture "
       "des terres moins fertiles",
       "Le coût de production du blé s’élève : c’est la loi des rendements "
       "décroissants",
       "Les salaires doivent suivre la hausse du prix des subsistances",
       "Les profits chutent, l’investissement s’arrête : l’économie atteint "
       "un état stationnaire"],
  exp="Ricardo raisonne par l’offre et par la marge : c’est la terre la moins "
      "productive mise en culture qui commande le coût, donc le prix. Le "
      "mécanisme est auto-destructeur — « la croissance s’étouffe "
      "elle-même » — et conduit à la baisse tendancielle du taux de profit, "
      "puis à un point d’arrêt. Le cours en tire l’opposition entre un Smith "
      "optimiste, confiant dans la division du travail, et un Ricardo "
      "pessimiste.",
  diss="Cette chaîne fournit l’archétype du raisonnement pessimiste sur la "
       "croissance : une limite physique — la terre, aujourd’hui les "
       "ressources — finit par borner l’accumulation."),

f(id='q3-m06', sp='c3-02', niv='raisonner', type='qcm', b=244,
  q="En quoi la théorie de l’avantage absolu constitue-t-elle une rupture "
    "avec la pensée mercantiliste ?",
  opts=["Elle montre que le commerce n’est pas un jeu à somme nulle : la "
        "spécialisation accroît la richesse totale et les deux pays peuvent "
        "gagner",
        "Elle montre qu’il faut exporter plus qu’on n’importe",
        "Elle montre que l’or est la seule mesure de la richesse",
        "Elle justifie la protection du marché national"],
  ans=0,
  why=["C’est précisément la thèse mercantiliste que Smith conteste.",
       "L’assimilation de la richesse au stock de métaux précieux est la "
       "position mercantiliste, pas celle de Smith.",
       "La protection du marché est l’une des trois propositions "
       "mercantilistes que le cours énumère."],
  exp="Le cours oppose point par point les deux doctrines. Les mercantilistes "
      "tiennent qu’il faut exporter plus qu’importer, protéger son marché, et "
      "que le commerce est une lutte entre nations. Smith renverse les trois : "
      "si chaque pays se spécialise selon ses avantages, la richesse totale "
      "augmente et les deux partenaires y gagnent. C’est le passage d’une "
      "vision conflictuelle à une vision coopérative de l’échange.",
  diss="Poser d’emblée « somme nulle ou gain mutuel ? » structure toute "
       "dissertation sur le protectionnisme : le débat porte moins sur les "
       "faits que sur cette alternative."),

# -------------------------------- c3-03 · Malthus, Say, Marx
f(id='q3-m07', sp='c3-03', niv='raisonner', type='courte', b=392,
  q="En quoi Malthus s’oppose-t-il à Say, et pourquoi le cours en fait-il un "
    "précurseur de Keynes ?",
  ans={'modele':
       "Say soutient que « l’offre crée sa propre demande » : toute "
       "production distribue des revenus qui permettent de l’acheter, de "
       "sorte qu’une surproduction générale est impossible. Malthus objecte "
       "que la production n’est pas automatiquement absorbée : encore "
       "faut-il des consommateurs ayant les moyens d’acheter. Il introduit "
       "pour cela la demande effective, définie comme la quantité demandée "
       "par ceux qui ont les moyens de payer le prix. Si les travailleurs "
       "sont trop pauvres, l’économie peut connaître une surproduction et "
       "une crise de sous-consommation, que l’épargne peut aggraver. C’est "
       "l’intuition que Keynes reprendra cent cinquante ans plus tard.",
       'cles': [{'f': ['offre cree sa propre demande', 'loi des debouches',
                       'say'],
                 'l': 'la loi des débouchés de Say'},
                {'f': ['demande effective'], 'l': 'la demande effective'},
                {'f': ['solvable', 'moyens de payer', 'moyens d acheter',
                       'pauvre'],
                 'l': 'une demande solvable, pas seulement un besoin'},
                {'f': ['surproduction', 'sous consommation', 'crise'],
                 'l': 'la possibilité d’une surproduction'}]},
  exp="Le cours est explicite : Malthus « s’oppose ici directement à Say » et "
      "est « un précurseur direct de Keynes ». Il précise aussi que cet "
      "apport est « souvent attribué à tort uniquement à Keynes ». La "
      "différence avec Keynes tient au contenu de la notion : chez Malthus, "
      "la demande effective est la demande solvable ; chez Keynes, ce sera "
      "la demande anticipée par les entrepreneurs.",
  diss="Attribuer la demande effective à Malthus avant Keynes est "
       "exactement le type de précision qui distingue une copie : elle "
       "montre qu’une idée a une histoire avant d’avoir un auteur célèbre."),

f(id='q3-m08', sp='c3-03', niv='appliquer', type='ordre', b=378,
  q="Remettez dans l’ordre la formation de la rente différentielle telle que "
    "le cours l’expose.",
  ans=["La croissance démographique oblige à cultiver des terres de moins en "
       "moins fertiles",
       "Le prix agricole est fixé par le coût de production de la terre la "
       "moins productive",
       "Les terres les plus fertiles produisent au même prix pour un coût "
       "plus faible",
       "Elles dégagent un surplus : la rente différentielle",
       "Les inégalités entre propriétaires fonciers s’accroissent"],
  exp="Le point décisif est le deuxième : c’est la terre marginale qui "
      "commande le prix de marché. Les terres meilleures encaissent alors un "
      "écart qui ne rémunère aucun effort supplémentaire. Le cours attribue "
      "l’origine de cette analyse à Malthus et sa systématisation à Ricardo, "
      "et la relie aux trois lois de base de l’économie classique : "
      "population, rendements décroissants, rente.",
  diss="La rente différentielle est le premier modèle de revenu sans "
       "contrepartie productive : il arme toute discussion sur les rentes de "
       "situation, foncières ou technologiques."),

f(id='q3-m09', sp='c3-03', niv='raisonner', type='qcm', b=362,
  q="Le cours juge sévèrement la prévision de Malthus. Quelle erreur lui "
    "attribue-t-il, et comment Malthus lui-même a-t-il infléchi sa position "
    "en 1803 ?",
  opts=["Il n’a pas vu le bouleversement démographique en cours ; en 1803 il "
        "reconnaît les progrès de la productivité, les importations de blé et "
        "l’émigration",
        "Il a surestimé la fertilité des terres ; en 1803 il abandonne la loi "
        "de population",
        "Il a ignoré la rente ; en 1803 il se rallie à Ricardo",
        "Il a confondu demande et offre ; en 1803 il adopte la loi de Say"],
  ans=0,
  why=["Malthus n’abandonne pas la loi de population : il en nuance les "
       "conséquences.",
       "La rente est au contraire l’un de ses apports majeurs, que Ricardo "
       "systématisera ensuite.",
       "Malthus s’oppose à la loi de Say ; il ne s’y rallie pas."],
  exp="Le cours distingue deux moments. En 1798, la population croît "
      "géométriquement et les subsistances arithmétiquement : la misère est "
      "inévitable. En 1803, après un voyage en France et dans un contexte "
      "transformé — fin des mauvaises récoltes, essor du commerce "
      "international —, Malthus atténue sa thèse en reconnaissant trois "
      "échappatoires : gains de productivité, importations de blé, "
      "émigration. L’erreur rétrospective que le cours pointe est "
      "démographique : la hausse de la population tenait moins à la "
      "fécondité qu’à la baisse de la mortalité.",
  diss="Distinguer les deux versions d’un auteur protège de la caricature et "
       "fournit un exemple de ce qu’est une théorie révisée par les faits."),

# ----------------------------------------- c3-04 · les néoclassiques
f(id='q3-m10', sp='c3-04', niv='appliquer', type='assoc', b=613,
  q="Associez chaque école néoclassique à son fondateur et à son trait "
    "distinctif selon le cours.",
  ans=[["École de Lausanne", "Walras : l’équilibre général et le "
                             "commissaire-priseur"],
       ["École de Cambridge", "Marshall : une approche plus réaliste et "
                              "pragmatique"],
       ["École autrichienne", "Menger : l’individualisme méthodologique et le "
                              "rejet de l’équilibre général"]],
  exp="Les trois écoles partagent le marginalisme — la valeur dépend de la "
      "satisfaction procurée à la marge — mais divergent sur la méthode. "
      "Walras formalise mathématiquement un système où tous les marchés "
      "s’équilibrent simultanément. Marshall revendique le pragmatisme. "
      "L’école autrichienne rejette l’équilibre général au motif que "
      "l’information est dispersée, fragmentée et subjective : aucun agent "
      "ne la détient tout entière. Hayek en tire que la monnaie n’est pas "
      "neutre et que le capitalisme peut être instable.",
  diss="Rappeler que les néoclassiques ne forment pas un bloc évite la copie "
       "qui oppose « les néoclassiques » à Keynes : Hayek admet les crises, "
       "Walras non."),

f(id='q3-m11', sp='c3-04', niv='raisonner', type='qcm', b=656,
  q="Pourquoi l’école autrichienne rejette-t-elle l’équilibre général "
    "walrassien ?",
  opts=["Parce que l’information est dispersée, fragmentée et subjective : "
        "aucun agent ne peut la détenir tout entière",
        "Parce que les prix ne jouent aucun rôle dans la coordination",
        "Parce qu’elle considère que l’État doit fixer les prix",
        "Parce qu’elle refuse l’individualisme méthodologique"],
  ans=0,
  why=["Les Autrichiens donnent au contraire aux prix un rôle central : ils "
       "transmettent une information que personne ne détient entièrement.",
       "Le courant est au contraire le plus hostile à l’intervention.",
       "L’individualisme méthodologique est précisément leur position : seuls "
       "les individus agissent."],
  exp="La critique porte sur une hypothèse d’information, non sur le marché. "
      "L’équilibre général suppose implicitement une information complète, "
      "que le commissaire-priseur de Walras centralise. Les Autrichiens "
      "objectent que l’information réelle est dispersée et subjective : c’est "
      "justement pour cela que le marché est irremplaçable, non parce qu’il "
      "atteint un optimum calculable. Hayek ajoute que la création monétaire "
      "excessive fausse les taux, provoque un surinvestissement et engendre "
      "des crises.",
  diss="Cette critique interne au libéralisme est précieuse : elle permet de "
       "défendre le marché sans défendre la concurrence pure et parfaite."),

# ----------------------------------- c3-05 · Keynes, demande effective
f(id='q3-m12', sp='c3-05', niv='appliquer', type='qcm', b=752,
  q="Une entreprise anticipe une demande faible et réduit sa production, bien "
    "que ses capacités soient intactes. Quel concept keynésien cette décision "
    "illustre-t-elle ?",
  opts=["La demande effective : la demande que les entreprises s’attendent "
        "réellement à pouvoir vendre",
        "La loi des débouchés de Say",
        "La loi des rendements décroissants",
        "L’effet de cliquet"],
  ans=0,
  why=["La loi de Say affirme l’inverse : la production trouve "
       "automatiquement sa demande.",
       "Les rendements décroissants portent sur les conditions techniques de "
       "production, non sur les anticipations.",
       "L’effet de cliquet décrit la rigidité de la consommation des ménages, "
       "chez Duesenberry, étudié au chapitre 1."],
  exp="Chez Keynes, ce sont les anticipations des entrepreneurs qui "
      "commandent le niveau de production et d’emploi, non l’offre "
      "disponible. Si la demande attendue est insuffisante, les entreprises "
      "produisent moins, licencient, et le chômage apparaît puis persiste. "
      "La différence avec Malthus est nette : Malthus parlait de demande "
      "solvable, Keynes parle de demande anticipée.",
  diss="La demande effective est le pivot du renversement keynésien : elle "
       "fait de l’emploi une variable dépendante des anticipations, donc de "
       "la confiance."),

f(id='q3-m13', sp='c3-05', niv='raisonner', type='courte', b=789,
  q="Qu’est-ce qu’un équilibre de sous-emploi, et en quoi l’idée est-elle "
    "paradoxale ?",
  ans={'modele':
       "C’est une situation dans laquelle l’économie est bien à l’équilibre — "
       "les entreprises sont satisfaites de leur niveau de production, les "
       "ménages consomment ce qu’ils peuvent, les marchés sont stables — et "
       "où, pourtant, une partie de la population active reste sans emploi. "
       "Le paradoxe est là : l’équilibre ne garantit pas le plein emploi. Le "
       "chômage keynésien est involontaire, lié à une insuffisance de la "
       "demande effective, et compatible avec un équilibre. Rien ne ramène "
       "donc spontanément l’économie au plein emploi : il faut une "
       "intervention qui relève la demande.",
       'cles': [{'f': ['equilibre'], 'l': 'l’économie est bien à l’équilibre'},
                {'f': ['chomage', 'sans emploi'], 'l': 'le chômage subsiste'},
                {'f': ['involontaire'], 'l': 'un chômage involontaire'},
                {'f': ['demande effective', 'insuffisance de la demande'],
                 'l': 'l’insuffisance de la demande effective'},
                {'f': ['intervention', 'etat', 'politique'],
                 'l': 'd’où la nécessité d’une intervention'}]},
  exp="Le cours insiste sur la coexistence des deux termes : stabilité des "
      "marchés et chômage durable. C’est ce qui sépare Keynes des "
      "« classiques » au sens où il les désigne : pour eux, un déséquilibre "
      "durable est impossible, les prix et les salaires s’ajustant. Pour "
      "Keynes, l’ajustement peut se faire par les quantités — donc par "
      "l’emploi — et non par les prix.",
  diss="L’équilibre de sous-emploi est l’argument théorique qui légitime la "
       "politique de relance : sans lui, l’intervention n’est qu’un pis-aller "
       "temporaire."),

f(id='q3-m14', sp='c3-06', niv='raisonner', type='assoc', b=778,
  q="Associez chaque question économique à la réponse de Keynes, telle que le "
    "cours l’oppose à celle des « classiques ».",
  ans=[["D’où vient le niveau de l’emploi ?",
        "De la demande effective anticipée, non de l’offre"],
       ["L’épargne est-elle toujours vertueuse ?",
        "Non : une épargne excessive réduit la demande"],
       ["Qu’est-ce qui détermine l’investissement ?",
        "Les anticipations, la confiance et les esprits animaux, pas "
        "seulement le taux d’intérêt"],
       ["La monnaie est-elle neutre ?",
        "Non : elle influence la production et l’emploi"],
       ["Que mesure le taux d’intérêt ?",
        "Le prix du renoncement à la liquidité, non le prix de l’épargne"]],
  exp="Ces cinq réponses forment un système cohérent : si la monnaie n’est "
      "pas neutre et si le taux d’intérêt rémunère la renonciation à la "
      "liquidité, alors la thésaurisation est possible, l’épargne peut ne pas "
      "se transformer en investissement, la demande peut manquer, et l’emploi "
      "s’en ressent. Chaque pièce soutient les autres : c’est pourquoi le "
      "désaccord avec les « classiques » est global et non ponctuel.",
  diss="Présenter le keynésianisme comme un système, et non comme une liste "
       "d’idées, est ce qui distingue une dissertation d’histoire de la "
       "pensée d’une fiche de révision."),

# ---------------------------- c3-07 · nouvelle économie keynésienne
f(id='q3-m15', sp='c3-07', niv='appliquer', type='qcmm', b=1165,
  q="La nouvelle économie keynésienne conserve les outils de la nouvelle "
    "économie classique tout en concluant autrement. Quels éléments "
    "appartiennent à cette synthèse ? (plusieurs réponses)",
  opts=["Des agents rationnels qui utilisent l’information disponible",
        "Des microfondements explicites",
        "Des rigidités des prix et des salaires",
        "Des asymétries d’information, notamment sur le marché du travail",
        "L’hypothèse que les marchés s’ajustent toujours instantanément"],
  ans=[0, 1, 2, 3],
  why=["Exacte : la NEK ne renonce pas à la rationalité des agents.",
       "Exacte : elle revendique des microfondements solides.",
       "Exacte : les rigidités empêchent l’ajustement par les prix.",
       "Exacte : certains agents savent plus que d’autres, en particulier sur "
       "le marché du travail.",
       "C’est la thèse adverse : la NEK montre au contraire que les marchés "
       "réels sont imparfaits."],
  exp="L’intérêt de la NEK tient à sa stratégie : elle accepte le terrain "
      "méthodologique de ses adversaires — rationalité, anticipations "
      "cohérentes, microfondements — et montre qu’on y aboutit pourtant à des "
      "conclusions keynésiennes dès lors qu’on reconnaît trois imperfections : "
      "rigidités, asymétries d’information, concurrence imparfaite. La "
      "conséquence est que la demande globale peut rester insuffisante et le "
      "chômage involontaire durable.",
  diss="Montrer qu’un courant adopte les armes de l’autre pour le réfuter est "
       "plus convaincant que d’opposer deux blocs : c’est l’exemple type d’un "
       "débat scientifique qui progresse."),

f(id='q3-m16', sp='c3-07', niv='raisonner', type='vf', b=1188,
  q="Vrai ou faux : dans la nouvelle économie keynésienne, le chômage résulte "
    "d’un choix des travailleurs qui refusent le salaire proposé. Justifiez.",
  ans=False,
  exp="La NEK conclut à un chômage involontaire et durable. Il ne vient pas "
      "d’un arbitrage travail-loisir mais des imperfections du marché : les "
      "prix et les salaires sont rigides, l’information est asymétrique — "
      "l’employeur ignore la productivité réelle du candidat, ce qui le "
      "dissuade de baisser les salaires —, et la concurrence est imparfaite. "
      "L’ajustement ne se fait donc pas par les prix, et la demande globale "
      "peut rester insuffisante. C’est exactement ce qui sépare la NEK de la "
      "nouvelle économie classique, qui partage pourtant ses hypothèses de "
      "rationalité.",
  diss="Cette distinction chômage volontaire / involontaire commande le "
       "jugement porté sur les politiques de l’emploi : flexibiliser n’a de "
       "sens que si le chômage est volontaire."),

# ---------------------- c3-08 · institutionnalistes et régulation
f(id='q3-m17', sp='c3-08', niv='raisonner', type='qcm', b=1290,
  q="Chez Veblen, pourquoi le capitalisme peut-il sous-utiliser ses capacités "
    "productives ?",
  opts=["Parce que la logique financière des hommes d’affaires peut "
        "s’opposer à la logique industrielle des ingénieurs : freiner la "
        "production protège les profits",
        "Parce que les ingénieurs manquent de compétences techniques",
        "Parce que la demande des ménages est toujours insuffisante",
        "Parce que l’État impose des quotas de production"],
  ans=0,
  why=["Les ingénieurs sont au contraire orientés vers l’efficacité "
       "technique et l’utilisation maximale des capacités.",
       "L’insuffisance de la demande est l’explication keynésienne, non celle "
       "de Veblen, qui met en cause un comportement délibéré.",
       "Aucune contrainte publique n’intervient : la rareté est organisée par "
       "les entreprises elles-mêmes."],
  exp="Veblen oppose deux logiques internes à l’entreprise. Les ingénieurs "
      "visent l’efficacité technique, la pleine utilisation des capacités et "
      "la baisse des coûts. Les hommes d’affaires visent le profit "
      "financier, ce qui peut les conduire à freiner la production, "
      "sous-utiliser les capacités, organiser des raretés artificielles. Il "
      "en résulte un décalage entre ce que l’économie pourrait produire et "
      "ce qu’elle produit : le capitalisme devient inefficace et instable.",
  diss="Veblen offre une critique du capitalisme qui ne passe ni par la "
       "demande ni par la lutte des classes, mais par un conflit de rationalités "
       "au sein même de l’entreprise."),

f(id='q3-m18', sp='c3-08', niv='appliquer', type='qcm', b=1398,
  q="Un régime d’accumulation durable s’enraye alors que les institutions "
    "qui l’encadraient n’ont pas changé. Comment l’école de la régulation "
    "lit-elle cette situation ?",
  opts=["Comme l’épuisement d’un mode de régulation devenu incompatible avec "
        "le régime d’accumulation : la crise est structurelle, non "
        "accidentelle",
        "Comme un simple choc conjoncturel, appelé à se résorber seul",
        "Comme la preuve que le marché s’autorégule",
        "Comme un effet des rendements décroissants"],
  ans=0,
  why=["C’est exactement la lecture que les régulationnistes refusent : la "
       "crise n’est pas un accident de conjoncture.",
       "L’école de la régulation soutient au contraire que le capitalisme ne "
       "se stabilise jamais spontanément.",
       "Les rendements décroissants relèvent de l’analyse classique, pas de "
       "cette grille."],
  exp="Aglietta et Boyer distinguent le régime d’accumulation — la manière "
      "dont la production et la répartition s’articulent durablement — et le "
      "mode de régulation — l’ensemble des règles et compromis "
      "institutionnels qui le font tenir. Une crise majeure survient quand le "
      "second ne soutient plus le premier : Boyer lit ainsi 1929 comme "
      "l’épuisement du mode de régulation concurrentiel. La croissance repose "
      "donc sur des compromis historiquement situés, qui finissent par "
      "s’user.",
  diss="Le couple régime d’accumulation / mode de régulation permet de "
       "traiter une crise comme un problème d’institutions, et de relier "
       "l’histoire économique à l’analyse théorique."),

f(id='q3-m19', sp='c3-08', niv='raisonner', type='courte', b=1337,
  q="Pourquoi, selon North, deux pays dotés d’un capital comparable peuvent-ils "
    "connaître des trajectoires de croissance opposées ?",
  ans={'modele':
       "Parce que la croissance dépend moins de l’accumulation de capital ou "
       "des économies d’échelle que de la qualité des institutions. North "
       "entend par institutions l’ensemble des règles formelles — lois, "
       "droits de propriété, contrats — et informelles — coutumes, "
       "traditions — qui encadrent le comportement des agents. Les individus "
       "restent rationnels, mais leur rationalité s’exerce dans un cadre "
       "donné : selon que ce cadre sécurise ou non les droits de propriété et "
       "l’exécution des contrats, les mêmes ressources produisent des "
       "résultats très différents. Le marché ne fonctionne efficacement que "
       "s’il est soutenu par des institutions adaptées.",
       'cles': [{'f': ['institution'], 'l': 'la qualité des institutions'},
                {'f': ['formelle', 'loi', 'droit de propriete', 'contrat'],
                 'l': 'les règles formelles : lois, droits de propriété, contrats'},
                {'f': ['informelle', 'coutume', 'tradition'],
                 'l': 'les règles informelles : coutumes et traditions'},
                {'f': ['cadre', 'rationalit'],
                 'l': 'la rationalité s’exerce dans un cadre institutionnel'}]},
  exp="North renouvelle l’analyse de la croissance à partir de l’histoire : "
      "il cherche pourquoi certains pays décollent quand d’autres stagnent, "
      "et répond par les institutions. Il est l’un des fondateurs de la "
      "nouvelle économie institutionnelle, qui ne renonce pas à la "
      "rationalité des agents mais la replace dans un cadre de règles. Le "
      "cours en tire la formule : le marché ne fonctionne efficacement que "
      "s’il est soutenu par des institutions adaptées.",
  diss="L’argument institutionnel permet de répondre à « pourquoi les pays "
       "pauvres restent-ils pauvres ? » sans se limiter au capital ni au "
       "commerce : c’est un troisième terme, souvent décisif."),
]
