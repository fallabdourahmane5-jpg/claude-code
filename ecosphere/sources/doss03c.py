# -*- coding: utf-8 -*-
"""Ensemble 3 — Le développement et les stratégies de rattrapage (3/4)."""

from doss_base import d

d('n3-transformation', 3, "Transformation structurelle",
  "Déplacer la main-d’œuvre vers les activités les plus productives",
  "La transformation structurelle désigne le déplacement du poids relatif des "
  "secteurs dans la production et l’emploi : recul de l’agriculture, essor de "
  "l’industrie, puis des services. Elle constitue le mécanisme par lequel une "
  "économie élève sa productivité moyenne sans que la productivité d’aucun "
  "secteur n’ait nécessairement augmenté, par simple réallocation de la "
  "main-d’œuvre vers les activités les plus productives.",
  "Ce mécanisme est l’un des plus puissants de l’économie du développement, et "
  "sa logique mérite d’être exposée avec précision car elle est "
  "contre-intuitive. Supposons une économie où le secteur traditionnel emploie "
  "l’essentiel de la population active avec une productivité très faible, et un "
  "secteur moderne beaucoup plus productif mais petit. Déplacer un travailleur "
  "du premier vers le second élève la production totale, même si la "
  "productivité de chaque secteur reste inchangée : c’est un gain purement "
  "allocatif. Lewis en fait le cœur de son analyse du dualisme, et le cours "
  "signale un trait décisif — la présence d’un surplus de main-d’œuvre dans le "
  "secteur traditionnel, où beaucoup de travailleurs produisent peu de gains, "
  "signifie que ce transfert ne réduit presque pas la production agricole. Le "
  "gain est donc presque gratuit. Deux conditions limitent toutefois le "
  "mécanisme. La première est que le secteur moderne soit capable d’absorber "
  "la main-d’œuvre : le cours note précisément qu’il est trop petit pour "
  "absorber immédiatement tout le surplus, ce qui produit du sous-emploi "
  "urbain plutôt qu’un transfert productif. La seconde est que la "
  "transformation ne s’arrête pas à l’industrie : la tertiarisation pose la "
  "question de la productivité des services, que Rodrik place au cœur des "
  "politiques contemporaines.",
  [("L’existence d’un écart de productivité entre secteurs",
    "Le secteur traditionnel, surtout agricole, est peu mécanisé et faiblement "
    "productif ; le secteur moderne, urbain et industriel, l’est beaucoup plus. "
    "C’est cet écart qui rend le transfert profitable."),
   ("Le surplus de main-d’œuvre",
    "Dans le secteur traditionnel, de nombreux travailleurs produisent peu de "
    "gains supplémentaires. Leur départ ne réduit donc presque pas la "
    "production du secteur, ce qui rend le transfert quasi gratuit."),
   ("Le gain allocatif",
    "Déplacer un travailleur vers un emploi plus productif élève la production "
    "totale sans qu’aucune productivité sectorielle n’ait changé : le gain "
    "provient de la réallocation elle-même."),
   ("La contrainte d’absorption",
    "Le secteur moderne doit croître assez vite pour employer la main-d’œuvre "
    "libérée. S’il est trop petit, le transfert produit du sous-emploi urbain "
    "au lieu d’un gain de productivité."),
   ("Le passage à la tertiarisation",
    "La transformation se poursuit de l’industrie vers les services, ce qui "
    "déplace la question : les gains de productivité y sont plus difficiles à "
    "obtenir, d’où l’enjeu des emplois de qualité.")],
  [{'a': "La transformation structurelle élève la productivité moyenne sans "
         "exiger de progrès technique, par simple réallocation de la "
         "main-d’œuvre.",
    'cond': "Elle suppose un écart de productivité entre secteurs et un surplus "
            "de main-d’œuvre dans le secteur de départ.",
    'lim': "Le gain s’épuise lorsque l’écart se réduit : une fois la "
           "main-d’œuvre réallouée, la croissance doit venir du progrès "
           "technique au sein des secteurs."},
   {'a': "Elle fournit un critère d’évaluation du développement plus pertinent "
         "que la seule croissance : une économie qui croît sans transformer sa "
         "structure reste vulnérable.",
    'cond': "L’observation exige des données sectorielles sur l’emploi et la "
            "valeur ajoutée, disponibles de façon inégale.",
    'lim': "Une transformation rapide peut aussi désorganiser les équilibres "
           "sociaux et territoriaux, ce que les politiques d’accompagnement "
           "doivent traiter."},
   {'a': "Elle éclaire les politiques à mener : accompagner l’exode du secteur "
         "traditionnel suppose d’élargir simultanément le secteur moderne.",
    'cond': "Les deux mouvements doivent être coordonnés, sans quoi la "
            "main-d’œuvre quitte un emploi peu productif pour le sous-emploi.",
    'lim': "La coordination exige une capacité de planification que les "
           "économies concernées possèdent rarement."}],
  [{'t': "Le secteur moderne est trop petit pour absorber immédiatement toute la "
         "main-d’œuvre excédentaire du secteur traditionnel.",
    'qui': "Constat explicite du cours dans l’analyse du dualisme de Lewis.",
    'rep': "L’objection ne nie pas le mécanisme mais en limite le rythme : la "
           "transformation est souhaitable et lente, ce qui justifie des "
           "politiques d’accompagnement plutôt qu’une accélération forcée."},
   {'t': "La transformation peut s’interrompre avant l’industrialisation, "
         "laissant l’économie passer directement d’une agriculture peu "
         "productive à des services peu productifs.",
    'qui': "Objection tirée de l’analyse de la désindustrialisation précoce chez "
           "Dani Rodrik.",
    'rep': "L’objection est sérieuse : elle montre que la séquence historique "
           "des pays avancés n’est pas garantie, et que la tertiarisation peut "
           "survenir sans les gains que l’industrialisation aurait procurés."},
   {'t': "Dans les économies déjà tertiarisées, la poursuite de la "
         "transformation ne produit plus de gains : l’enjeu devient la "
         "productivité à l’intérieur des services.",
    'qui': "Dani Rodrik, avec la priorité donnée aux emplois de qualité dans "
           "les services.",
    'rep': "L’objection déplace utilement la question pour les économies "
           "avancées : le levier n’est plus la réallocation mais l’élévation de "
           "la productivité là où se trouve l’emploi."}],
  [{'n': "Arthur Lewis",
    'i': "Le développement procède du transfert de main-d’œuvre du secteur "
         "traditionnel vers le secteur moderne.",
    'p': "Prix Nobel 1979 (1915-1991) : le secteur traditionnel, surtout "
         "agricole, est peu mécanisé, à faible productivité et doté d’un "
         "surplus de main-d’œuvre ; le secteur moderne est urbain, capitaliste "
         "et plus productif, mais encore limité."},
   {'n': "Jean Fourastié",
    'i': "Le déversement sectoriel transforme la structure de l’emploi sous "
         "l’effet des gains de productivité.",
    'p': "Les gains réalisés dans un secteur libèrent de la main-d’œuvre qui se "
         "reporte vers d’autres activités : la transformation structurelle est "
         "la contrepartie du progrès technique, et non un phénomène distinct."},
   {'n': "Dani Rodrik",
    'i': "La désindustrialisation précoce interrompt la séquence classique de "
         "la transformation structurelle.",
    'p': "Perdre son industrie avant d’être riche prive l’économie des gains de "
         "productivité que l’industrialisation aurait procurés : la "
         "transformation structurelle ne suit donc pas nécessairement le chemin "
         "des pays avancés."},
   {'n': "Ragnar Nurkse",
    'i': "Le dualisme peut s’auto-entretenir au lieu de se résorber, parce "
         "que la faiblesse des revenus bride l’épargne et donc "
         "l’investissement.",
    'p': "Si le secteur moderne ne croît pas assez vite, le transfert de "
         "main-d’œuvre ne s’opère pas et la structure duale se perpétue, "
         "entretenant le cercle vicieux de la pauvreté : l’épargne reste "
         "trop faible pour financer l’investissement qui, seul, élargirait "
         "le secteur moderne. La transformation structurelle n’est donc pas "
         "automatique, elle suppose un effort d’accumulation suffisamment "
         "massif pour rompre le cercle."}],
  [{'f': "Dans l’analyse de Lewis, le secteur traditionnel est surtout agricole, "
         "peu mécanisé, à faible productivité et à main-d’œuvre abondante, avec "
         "présence d’un surplus de main-d’œuvre.",
    'p': "L’existence d’un surplus est la condition qui rend le transfert quasi "
         "gratuit : retirer des travailleurs ne réduit presque pas la "
         "production agricole."},
   {'f': "Le cours relève que le secteur moderne est trop petit pour absorber "
         "immédiatement toute la main-d’œuvre excédentaire.",
    'p': "La contrainte d’absorption explique que la transformation soit lente "
         "et qu’une accélération forcée produise du sous-emploi urbain."}],
  [{'q': "Sujet du type « L’industrialisation est-elle indispensable au "
         "développement ? »",
    'f': "L’industrialisation a longtemps été le vecteur privilégié de la "
         "transformation structurelle, parce qu’elle offrait un secteur "
         "d’accueil très productif à une main-d’œuvre agricole excédentaire. La "
         "question se pose autrement aujourd’hui, la désindustrialisation "
         "précoce montrant que des économies peuvent passer de l’agriculture "
         "aux services sans capter ces gains.",
    'r': "Faire porter le raisonnement sur la fonction de l’industrie — offrir "
         "un secteur d’accueil productif — plutôt que sur l’industrie en "
         "elle-même permet d’examiner si d’autres secteurs peuvent la remplir.",
    'ex': "Le surplus de main-d’œuvre du secteur traditionnel chez Lewis, et la "
          "désindustrialisation précoce analysée par Rodrik."},
   {'q': "Sujet du type « La croissance suffit-elle au développement ? »",
    'f': "La transformation structurelle fournit le chaînon : une croissance "
         "qui ne déplace pas la main-d’œuvre vers des activités plus "
         "productives n’élève pas durablement le niveau de vie, parce qu’elle "
         "laisse l’essentiel de la population dans des emplois à faible "
         "productivité.",
    'r': "Montrer que le contenu sectoriel de la croissance importe autant que "
         "son rythme permet de dépasser l’opposition entre croissance et "
         "développement.",
    'ex': "L’analyse de Lewis, où la productivité moyenne de l’économie reste "
          "faible tant que la population demeure dans le secteur traditionnel."}],
  voisins=['n3-dualisme', 'n3-emergence', 'n3-isi', 'n3-ipe',
           'n3-developpement'])

d('n3-dualisme', 3, "Dualisme économique",
  "Deux économies dans un même pays, et un transfert qui peut ne pas s’opérer",
  "Le dualisme économique désigne la coexistence, au sein d’une même économie, "
  "d’un secteur traditionnel — surtout agricole, peu mécanisé, à faible "
  "productivité, à main-d’œuvre abondante et comportant un surplus de "
  "main-d’œuvre — et d’un secteur moderne — urbain, capitaliste, industriel, "
  "plus productif et capable d’investir, mais encore limité. L’analyse est due "
  "à Arthur Lewis, prix Nobel 1979.",
  "Le dualisme explique le sous-développement par une cause interne, "
  "complémentaire des explications par l’insertion internationale. Le "
  "raisonnement est le suivant : dans le secteur traditionnel, beaucoup de "
  "travailleurs produisent peu de gains de productivité, de sorte que les "
  "revenus restent faibles ; une grande partie de la population demeure dans "
  "des activités peu productives, la productivité moyenne de l’économie reste "
  "basse et la demande intérieure demeure limitée. Le problème central est que "
  "le secteur moderne est trop petit pour absorber immédiatement toute la "
  "main-d’œuvre excédentaire. Deux lectures s’opposent alors, et elles "
  "structurent le dossier. Pour Lewis, l’économie duale n’est que passagère : "
  "le secteur moderne, capable d’investir, croît et absorbe progressivement le "
  "surplus, ce qui élève la productivité moyenne jusqu’à la disparition du "
  "dualisme. Pour Nurkse, dont le cours souligne la lecture plus pessimiste, le "
  "dualisme peut au contraire s’auto-entretenir : la pauvreté produit "
  "elle-même les conditions de sa reproduction, l’étroitesse de la demande "
  "intérieure limitant l’investissement qui permettrait au secteur moderne de "
  "croître. Le désaccord porte donc sur un point précis : la capacité du "
  "secteur moderne à s’étendre assez vite.",
  [("La coexistence de deux secteurs hétérogènes",
    "Un secteur traditionnel agricole, peu mécanisé et à faible productivité, "
    "coexiste avec un secteur moderne urbain et industriel beaucoup plus "
    "productif : l’économie n’est pas homogène."),
   ("Le surplus de main-d’œuvre",
    "Dans le secteur traditionnel, la main-d’œuvre est abondante au point que "
    "des travailleurs supplémentaires n’ajoutent presque rien à la production : "
    "ce surplus est disponible pour un transfert."),
   ("Le transfert vers le secteur moderne",
    "Le déplacement de main-d’œuvre vers le secteur plus productif élève la "
    "production totale et la productivité moyenne, sans coût significatif pour "
    "le secteur d’origine."),
   ("La limite d’absorption",
    "Le secteur moderne est trop petit pour absorber immédiatement le surplus. "
    "Le rythme du développement est donc commandé par sa capacité "
    "d’investissement et d’expansion."),
   ("Le blocage possible",
    "Si la demande intérieure reste limitée faute de revenus, l’investissement "
    "du secteur moderne reste faible, sa croissance insuffisante, et le "
    "dualisme se perpétue.")],
  [{'a': "Le dualisme identifie une réserve de croissance interne : le surplus "
         "de main-d’œuvre du secteur traditionnel peut être employé plus "
         "productivement sans coût d’opportunité significatif.",
    'cond': "Il faut que le surplus existe réellement, c’est-à-dire que la "
            "productivité marginale dans le secteur traditionnel soit "
            "quasiment nulle.",
    'lim': "Si cette hypothèse est fausse, le transfert réduit la production "
           "agricole et peut créer une tension alimentaire."},
   {'a': "Il fournit une explication du sous-développement qui ne dépend pas de "
         "l’insertion internationale, donc applicable à des contextes variés.",
    'cond': "L’explication suppose que l’écart de productivité entre secteurs "
            "soit effectivement observé.",
    'lim': "Elle risque de sous-estimer les contraintes extérieures que les "
           "analyses centre-périphérie placent au premier plan."},
   {'a': "Il désigne un levier d’action précis : élargir le secteur moderne "
         "plutôt que subventionner le secteur traditionnel.",
    'cond': "L’élargissement suppose un financement de l’investissement "
            "industriel, donc une épargne ou un apport extérieur.",
    'lim': "Une industrialisation forcée sans débouchés produit des capacités "
           "inutilisées, ce qui est l’un des reproches adressés aux politiques "
           "de substitution aux importations."}],
  [{'t': "L’économie duale n’est que passagère : le secteur moderne finira par "
         "absorber le surplus de main-d’œuvre.",
    'qui': "Arthur Lewis, dans sa lecture optimiste du dualisme.",
    'rep': "La thèse suppose une croissance suffisante du secteur moderne, ce "
           "qui dépend de sa capacité d’investissement et de l’existence de "
           "débouchés — deux conditions que la pauvreté même peut interdire."},
   {'t': "Le dualisme peut s’auto-entretenir : la pauvreté produit les "
         "conditions de sa reproduction.",
    'qui': "Ragnar Nurkse, dont le cours souligne la lecture plus pessimiste.",
    'rep': "L’objection est décisive et transforme le diagnostic : le dualisme "
           "n’est plus une étape mais un équilibre, ce qui justifie une "
           "impulsion extérieure ou institutionnelle."},
   {'t': "L’explication interne par le dualisme néglige les rapports de "
         "domination internationaux qui maintiennent la périphérie dans une "
         "spécialisation primaire.",
    'qui': "Raul Prebisch, radicalisé par Arghiri Emmanuel et Samir Amin avec "
           "l’échange inégal.",
    'rep': "Les deux explications sont compatibles : une insertion défavorable "
           "limite les revenus et la demande intérieure, ce qui freine "
           "précisément l’expansion du secteur moderne."}],
  [{'n': "Arthur Lewis",
    'i': "Le sous-développement s’analyse comme un dualisme entre un secteur "
         "traditionnel à faible productivité et un secteur moderne plus "
         "productif mais limité.",
    'p': "Prix Nobel 1979 (1915-1991) : le secteur traditionnel est surtout "
         "agricole, peu mécanisé, à revenus faibles et à main-d’œuvre "
         "abondante ; le secteur moderne est urbain, capitaliste, industriel et "
         "capable d’investir."},
   {'n': "Arthur Lewis",
    'i': "L’économie duale n’est que passagère : le transfert de main-d’œuvre "
         "doit la résorber.",
    'p': "La croissance du secteur moderne absorbe progressivement le surplus, "
         "ce qui élève la productivité moyenne. La lecture est optimiste et "
         "suppose que l’absorption soit effectivement possible."},
   {'n': "Ragnar Nurkse",
    'i': "Le dualisme peut entretenir un cercle vicieux de la pauvreté plutôt "
         "que se résorber.",
    'p': "Faibles revenus, faible épargne, faible investissement, faible "
         "productivité : si la demande intérieure reste étroite, le secteur "
         "moderne ne croît pas assez pour absorber le surplus."},
   {'n': "Raul Prebisch",
    'i': "La structure duale s’inscrit dans une insertion internationale "
         "défavorable.",
    'p': "L’économie périphérique exporte des produits primaires et importe des "
         "produits manufacturés, ce qui limite la constitution d’un secteur "
         "moderne national et renforce la dualité."}],
  [{'f': "Arthur Lewis (1915-1991), prix Nobel 1979, distingue un secteur "
         "moderne urbain et capitaliste d’un secteur traditionnel surtout "
         "agricole.",
    'p': "La datation et la distinction sectorielle sont les éléments à "
         "connaître pour mobiliser l’auteur avec précision."},
   {'f': "Le cours relève que dans le secteur traditionnel, il y a beaucoup de "
         "travailleurs pour peu de gains de productivité, de sorte que les "
         "revenus restent faibles et la demande intérieure limitée.",
    'p': "L’enchaînement relie directement la structure productive à "
         "l’étroitesse du marché intérieur, donc au blocage de "
         "l’investissement."},
   {'f': "Là où Lewis pense que le dualisme peut être dépassé, Nurkse considère "
         "qu’il peut au contraire s’auto-entretenir.",
    'p': "L’opposition est explicitement posée par le cours et fournit une "
         "controverse directement exploitable en dissertation."}],
  [{'q': "Sujet du type « Le sous-développement est-il un retard ? »",
    'f': "Le dualisme fournit une réponse nuancée : il décrit une structure "
         "interne, donc un état et non une position dans une séquence. Mais "
         "cette structure est-elle transitoire ou stable ? Lewis répond "
         "qu’elle est passagère, Nurkse qu’elle peut s’auto-entretenir — et "
         "c’est de cette alternative que dépend la réponse au sujet.",
    'r': "Faire reposer la réponse sur un désaccord documenté entre deux "
         "auteurs traitant du même objet donne au devoir une dialectique "
         "fondée sur les textes plutôt que sur une opposition construite.",
    'ex': "Le surplus de main-d’œuvre du secteur traditionnel et la limite "
          "d’absorption du secteur moderne."},
   {'q': "Sujet du type « Un pays peut-il se développer sans État fort ? »",
    'f': "Si le dualisme se résorbe spontanément, comme le pense Lewis, l’État "
         "n’est pas indispensable. S’il s’auto-entretient, comme le soutient "
         "Nurkse, seule une impulsion extérieure ou institutionnelle permet de "
         "sortir de l’équilibre — ce qui rejoint la substitution "
         "institutionnelle décrite par Gerschenkron.",
    'r': "Faire dépendre la nécessité de l’État du caractère stable ou "
         "transitoire du dualisme transforme une question doctrinale en "
         "question analytique.",
    'ex': "Le cercle vicieux de Nurkse, qui ne comporte aucun point d’entrée "
          "naturel pour une sortie spontanée."}],
  voisins=['n3-cercle-vicieux', 'n3-transformation', 'n3-sous-developpement',
           'n3-isi', 'n3-trappe-pauvrete'])

d('n3-isi', 3, "Industrialisation par substitution aux importations",
  "Produire soi-même ce que l’on importait, derrière une protection",
  "L’industrialisation par substitution aux importations consiste à développer "
  "une industrie nationale destinée à remplacer les produits manufacturés "
  "jusque-là importés, en protégeant le marché intérieur. Elle est préconisée "
  "par Prebisch, pour qui la réponse à la dépendance commerciale passe par une "
  "industrialisation protégée et une réduction de la spécialisation primaire, "
  "parfois dans une logique de développement autocentré.",
  "La stratégie découle directement du diagnostic structuraliste. Si la "
  "périphérie est enfermée dans l’exportation de produits primaires et la "
  "dépendance aux importations industrielles, et si cette configuration "
  "l’expose à une détérioration des termes de l’échange, alors il ne faut pas "
  "la laisser dans cette position : il faut construire l’industrie que le "
  "marché ne produirait pas. La protection du marché intérieur joue ici le rôle "
  "que le protectionnisme éducateur joue chez List — donner à une industrie "
  "naissante le temps d’atteindre la compétitivité. Le cours rappelle que "
  "Prebisch pousse parfois le raisonnement jusqu’au développement autocentré, "
  "c’est-à-dire jusqu’à l’idée qu’un pays doit éviter les échanges avec "
  "l’extérieur pour se développer. C’est aussi sur ce point que les critiques "
  "portent, et le cours les expose clairement : tous les pays en développement "
  "n’ont pas un marché intérieur suffisant, et tous ne peuvent donc pas se "
  "développer de manière autocentrée. Le développement autocentré est "
  "particulièrement difficile pour les petits pays et pour ceux dont le marché "
  "est étroit, puisque l’industrie protégée ne peut alors atteindre l’échelle "
  "nécessaire à la compétitivité. La stratégie se heurte ainsi à une "
  "contradiction : elle suppose un marché que le sous-développement rend "
  "précisément insuffisant.",
  [("L’identification des importations à substituer",
    "On repère les produits manufacturés importés en volume important, dont la "
    "production nationale paraît techniquement accessible : ce sont "
    "généralement des biens de consommation courante."),
   ("La protection du marché intérieur",
    "Droits de douane, quotas ou licences réservent la demande nationale aux "
    "producteurs locaux, ce qui garantit un débouché à l’industrie naissante."),
   ("L’apprentissage et la montée en échelle",
    "Protégée, l’industrie accumule de l’expérience et augmente ses volumes, ce "
    "qui doit abaisser son coût moyen jusqu’au niveau mondial."),
   ("La remontée de filière",
    "Une fois les biens de consommation produits nationalement, la stratégie "
    "vise les biens intermédiaires puis les biens d’équipement, selon une "
    "logique de remontée des étapes de fabrication."),
   ("La contrainte de taille du marché",
    "L’échelle nécessaire à la compétitivité dépend de la taille du marché "
    "protégé. Un marché intérieur étroit empêche d’atteindre cette échelle, ce "
    "qui bloque la stratégie.")],
  [{'a': "La stratégie réduit la dépendance aux importations industrielles et "
         "la vulnérabilité associée à une spécialisation primaire.",
    'cond': "Elle suppose que l’industrie protégée devienne effectivement "
            "compétitive, ce qui exige un marché intérieur suffisant et le "
            "maintien d’une concurrence interne.",
    'lim': "Si la protection se prolonge sans gain de compétitivité, elle "
           "produit une industrie durablement inefficace financée par les "
           "consommateurs."},
   {'a': "Elle permet de construire des capacités industrielles que le marché "
         "n’aurait pas créées, en donnant un débouché garanti à des producteurs "
         "naissants.",
    'cond': "Le débouché garanti doit être transitoire et assorti d’exigences "
            "de performance, faute de quoi il engendre une rente.",
    'lim': "La garantie de débouché supprime l’aiguillon concurrentiel, ce qui "
           "est le principal risque identifié pour toute protection éducatrice."},
   {'a': "Elle déplace la spécialisation vers des productions à plus forte "
         "valeur ajoutée par la remontée de filière.",
    'cond': "La remontée suppose des compétences techniques et des "
            "fournisseurs locaux, qui ne se constituent pas automatiquement.",
    'lim': "Les étapes amont sont plus capitalistiques et plus exigeantes en "
           "échelle, ce qui rend la remontée d’autant plus difficile que le "
           "marché est petit."}],
  [{'t': "Tous les pays en développement n’ont pas un marché intérieur "
         "suffisant pour permettre à une industrie protégée d’atteindre la "
         "compétitivité.",
    'qui': "Critique de Prebisch explicitement rapportée par le cours.",
    'rep': "L’objection est décisive pour les petits pays. Elle conduit soit à "
           "l’intégration régionale, qui élargit le marché protégé, soit à la "
           "stratégie inverse de promotion des exportations."},
   {'t': "Le développement autocentré, c’est-à-dire l’évitement des échanges "
         "avec l’extérieur, prive l’économie des technologies, des intrants et "
         "des débouchés nécessaires.",
    'qui': "Objection tirée des limites du développement autocentré que le "
           "cours signale pour les petits pays et les marchés étroits.",
    'rep': "La critique porte sur la version maximaliste de la stratégie : une "
           "protection sélective et temporaire n’implique pas l’autarcie, et "
           "les trajectoires réussies reposent sur une ouverture maîtrisée."},
   {'t': "La protection prolongée engendre rente et absence d’innovation plutôt "
         "que compétitivité.",
    'qui': "Risque général des protections éducatrices, dont la condition "
           "essentielle est la temporalité.",
    'rep': "L’objection impose une clause d’extinction et le maintien d’une "
           "concurrence intérieure : l’échec constaté de certaines expériences "
           "tient à l’absence de ces garde-fous plus qu’au principe."}],
  [{'n': "Raul Prebisch",
    'i': "La réponse à la dépendance commerciale passe par une industrialisation "
         "protégée et une réduction de la spécialisation primaire.",
    'p': "Économiste argentin (1901-1986) à la CEPAL : il ne faut pas laisser "
         "les pays périphériques enfermés dans l’exportation de produits "
         "primaires et la dépendance aux importations industrielles."},
   {'n': "Friedrich List",
    'i': "Une protection temporaire permet à une industrie naissante "
         "d’atteindre la compétitivité.",
    'p': "Système national d’économie politique (1841) : le mécanisme invoqué "
         "par la substitution aux importations est celui du protectionnisme "
         "éducateur, avec la même condition essentielle de temporalité."},
   {'n': "Paul Krugman",
    'i': "Une industrie potentiellement efficace peut ne jamais émerger faute "
         "d’atteindre son échelle critique.",
    'p': "La formalisation éclaire la condition de taille du marché : la "
         "protection n’est utile que si le marché protégé permet de franchir le "
         "seuil au-delà duquel le coût moyen descend sous le prix mondial."},
   {'n': "Samir Amin",
    'i': "L’échange inégal justifie une déconnexion partielle du marché "
         "mondial.",
    'p': "Avec Arghiri Emmanuel, l’analyse radicalise Prebisch : si le "
         "sous-développement est produit par l’insertion internationale, alors "
         "la réduire est la condition d’un développement autonome."}],
  [{'f': "Prebisch justifie une industrialisation protégée, une réduction de la "
         "dépendance extérieure, des politiques de substitution aux importations "
         "et parfois une logique de développement autocentré.",
    'p': "L’énumération montre la gradation de la stratégie, de la protection "
         "sélective à l’autarcie, ce qui permet de distinguer les versions "
         "modérée et maximaliste."},
   {'f': "Le cours rapporte les critiques : tous les pays en développement n’ont "
         "pas un marché intérieur suffisant, et le développement autocentré est "
         "difficile pour les petits pays et les marchés étroits.",
    'p': "La taille du marché est la variable qui décide de la viabilité de la "
         "stratégie, ce qui explique sa réussite inégale selon les pays."}],
  [{'q': "Sujet du type « Faut-il s’ouvrir pour se développer ? »",
    'f': "La substitution aux importations répond négativement, et pour une "
         "raison précise : si la spécialisation primaire résulte de l’insertion "
         "internationale et l’entretient, alors s’ouvrir davantage consolide le "
         "blocage. Mais la stratégie se heurte à une contrainte que le cours "
         "souligne : elle suppose un marché intérieur suffisant, que le "
         "sous-développement rend précisément étroit.",
    'r': "Opposer la cohérence interne de la stratégie à sa condition de "
         "viabilité permet de la discuter sans la caricaturer : "
         "l’industrialisation par substitution aux importations n’échoue pas "
         "parce que son raisonnement serait faux, mais parce que la taille "
         "du marché intérieur, que ce raisonnement suppose donnée, fait "
         "défaut dans la plupart des pays qui l’ont adoptée.",
    'ex': "La critique rapportée par le cours sur l’impossibilité du "
          "développement autocentré pour les petits pays."},
   {'q': "Sujet du type « Existe-t-il une voie unique vers le développement ? »",
    'f': "La substitution aux importations et la promotion des exportations "
         "constituent deux réponses opposées au même diagnostic de dépendance : "
         "l’une réduit les échanges pour construire l’industrie, l’autre les "
         "intensifie pour la financer. Leur réussite respective dépend de la "
         "taille du marché et de la capacité d’absorption, non d’une supériorité "
         "intrinsèque.",
    'r': "Présenter les deux stratégies comme conditionnelles plutôt que "
         "concurrentes permet de conclure par les conditions de réussite.",
    'ex': "La contrainte de taille du marché, décisive pour la substitution aux "
          "importations et secondaire pour la promotion des exportations."}],
  voisins=['n3-ipe', 'n3-dependance', 'n3-sous-developpement',
           'n3-etat-developpeur', 'n3-transformation'])

d('n3-ipe', 3, "Industrialisation par promotion des exportations",
  "Se développer en produisant pour le marché mondial",
  "L’industrialisation par promotion des exportations consiste à développer une "
  "industrie destinée au marché mondial plutôt qu’au seul marché intérieur. Le "
  "cours la présente comme une logique de développement extraverti, avec "
  "priorité donnée au départ à l’industrie légère exportatrice, et la distingue "
  "de la substitution d’exportations, qui vise à remplacer les produits "
  "primaires exportés par des produits à forte valeur ajoutée.",
  "La stratégie inverse celle de la substitution aux importations tout en "
  "partageant son objectif : transformer la spécialisation. Le cours en décrit "
  "précisément le mécanisme : le développement passe par la production de biens "
  "manufacturés destinés à l’exportation, avec une stratégie de remontée de "
  "filière consistant à remonter les étapes de fabrication d’aval en amont — "
  "biens de consommation d’abord, puis biens intermédiaires, enfin biens "
  "d’équipement. Le pays cherche ainsi à profiter de la demande étrangère tout "
  "en construisant progressivement des capacités plus complexes. Trois "
  "avantages distinguent cette voie de la précédente. D’abord, elle lève la "
  "contrainte de taille du marché intérieur, puisque le débouché est mondial : "
  "c’est l’argument décisif pour les petits pays. Ensuite, elle soumet les "
  "producteurs à la concurrence internationale, ce qui maintient l’aiguillon "
  "que la protection supprime. Enfin, elle procure des devises nécessaires à "
  "l’importation de biens d’équipement. Ses limites sont symétriques : elle "
  "expose l’économie aux fluctuations de la demande mondiale, elle suppose un "
  "accès effectif aux marchés étrangers — que la protection agricole des pays "
  "avancés limite précisément —, et elle peut enfermer le pays dans une "
  "spécialisation d’assemblage si la remontée de filière n’a pas lieu.",
  [("La priorité à l’industrie légère exportatrice",
    "Le point de départ est une production manufacturière simple, intensive en "
    "travail, pour laquelle le pays dispose d’un avantage de coût immédiat sur "
    "le marché mondial."),
   ("L’accès à une demande illimitée",
    "Le débouché étant mondial, la contrainte de taille du marché intérieur "
    "disparaît : l’échelle nécessaire à la compétitivité devient atteignable "
    "même pour une petite économie."),
   ("La discipline concurrentielle",
    "Vendre sur le marché mondial impose de soutenir la comparaison avec les "
    "producteurs étrangers, ce qui maintient la pression à la productivité que "
    "la protection supprime."),
   ("La remontée de filière",
    "La stratégie vise ensuite à remonter les étapes de fabrication d’aval en "
    "amont : biens de consommation, puis biens intermédiaires, puis biens "
    "d’équipement."),
   ("L’acquisition de devises",
    "Les recettes d’exportation financent l’importation des biens d’équipement "
    "et des technologies nécessaires à la montée en gamme.")],
  [{'a': "La promotion des exportations lève la contrainte de taille du marché "
         "intérieur, ce qui la rend accessible aux petites économies.",
    'cond': "Elle suppose un accès effectif aux marchés étrangers, donc "
            "l’absence de barrières prohibitives chez les partenaires.",
    'lim': "Cet accès n’est pas garanti : le secteur agricole, où nombre de ces "
           "pays disposent d’un avantage, reste le plus protégé dans les "
           "économies avancées."},
   {'a': "Elle maintient la discipline concurrentielle, ce qui évite la rente "
         "engendrée par une protection prolongée.",
    'cond': "L’exposition doit être progressive pour ne pas éliminer des "
            "producteurs qui n’ont pas encore atteint leur échelle.",
    'lim': "Une exposition trop précoce reproduit le problème que le "
           "protectionnisme éducateur devait résoudre : l’élimination avant "
           "maturité."},
   {'a': "Elle procure les devises nécessaires à l’importation des biens "
         "d’équipement et des technologies.",
    'cond': "Les recettes doivent être effectivement orientées vers "
            "l’investissement productif plutôt que vers la consommation ou la "
            "sortie de capitaux.",
    'lim': "La dépendance aux recettes d’exportation expose l’économie aux "
           "retournements de la demande mondiale, ce qui réintroduit une "
           "vulnérabilité."}],
  [{'t': "La stratégie expose l’économie aux fluctuations de la demande "
         "mondiale, qu’elle ne contrôle pas.",
    'qui': "Objection symétrique de celle adressée à la spécialisation "
           "primaire : la dépendance change d’objet sans disparaître.",
    'rep': "La vulnérabilité est réelle mais décroît avec la diversification "
           "des produits et des marchés, que la remontée de filière permet "
           "précisément."},
   {'t': "Sans remontée de filière, le pays reste cantonné à l’assemblage et ne "
         "capte qu’une faible part de la valeur ajoutée.",
    'qui': "Objection tirée de l’analyse des chaînes de valeur et de la montée "
           "en gamme.",
    'rep': "L’objection désigne la condition de réussite : la promotion des "
           "exportations n’est développante que si elle s’accompagne d’une "
           "stratégie explicite de remontée des étapes de fabrication."},
   {'t': "L’accès aux marchés des pays avancés reste entravé là où ces pays sont "
         "les plus compétitifs.",
    'qui': "Constat tiré de l’écart entre le droit de douane agricole moyen de "
           "15,9 % et le droit industriel d’environ 3 % en 2019.",
    'rep': "L’objection limite la portée de la stratégie pour les économies à "
           "avantage agricole, et explique pourquoi la voie manufacturière a "
           "été privilégiée par les trajectoires asiatiques."}],
  [{'n': "Raul Prebisch",
    'i': "La spécialisation primaire enferme la périphérie dans une insertion "
         "défavorable.",
    'p': "Le diagnostic est commun aux deux stratégies : la substitution aux "
         "importations et la promotion des exportations cherchent toutes deux à "
         "transformer la spécialisation, par des moyens opposés."},
   {'n': "Paul Krugman",
    'i': "Les économies d’échelle rendent la taille du marché accessible "
         "déterminante pour la compétitivité.",
    'p': "L’argument explique la supériorité pratique de la promotion des "
         "exportations pour les petits pays : le marché mondial permet "
         "d’atteindre un seuil que le marché intérieur n’autoriserait pas."},
   {'n': "Alexander Gerschenkron",
    'i': "Le rattrapage suppose des institutions capables de mobiliser le "
         "capital et d’orienter la transformation.",
    'p': "La promotion des exportations n’est pas une stratégie de laisser-faire : "
         "elle suppose une politique active de soutien aux filières "
         "exportatrices et de remontée de filière."},
   {'n': "Dani Rodrik",
    'i': "Les trajectoires de développement dépendent des institutions et des "
         "compromis politiques, sans modèle unique.",
    'p': "La réussite de la promotion des exportations dans certains pays et son "
         "échec dans d’autres confirme qu’il s’agit d’une stratégie "
         "conditionnelle et non d’une recette."}],
  [{'f': "Le cours décrit la promotion des exportations comme une logique de "
         "développement extraverti, avec priorité donnée au départ à l’industrie "
         "légère exportatrice.",
    'p': "Le choix initial de l’industrie légère est cohérent avec l’avantage de "
         "coût des économies à bas salaires, et constitue le point d’entrée de "
         "la stratégie."},
   {'f': "La stratégie de remontée de filière consiste à remonter les étapes de "
         "fabrication d’aval en amont : biens de consommation, puis biens "
         "intermédiaires, puis biens d’équipement.",
    'p': "La séquence décrit précisément comment une spécialisation d’assemblage "
         "peut devenir une capacité industrielle complète."},
   {'f': "Le cours distingue la promotion des exportations de la substitution "
         "d’exportations, qui vise à remplacer les produits primaires par des "
         "produits à forte valeur ajoutée.",
    'p': "La distinction permet de ne pas confondre l’exportation de produits "
         "primaires, qui prolonge la spécialisation, et celle de produits "
         "manufacturés, qui la transforme."}],
  [{'q': "Sujet du type « Faut-il s’ouvrir pour se développer ? »",
    'f': "La promotion des exportations répond affirmativement, mais sous une "
         "condition exigeante : l’ouverture doit s’accompagner d’une stratégie "
         "de remontée de filière, sans laquelle le pays reste cantonné à "
         "l’assemblage. L’ouverture n’est donc pas la cause du développement, "
         "elle en est le cadre.",
    'r': "Distinguer l’ouverture comme cadre et la montée en gamme comme moteur "
         "évite de trancher entre ouverture et protection et déplace la "
         "question vers le contenu de la politique industrielle.",
    'ex': "La séquence de remontée de filière : biens de consommation, biens "
          "intermédiaires, biens d’équipement."},
   {'q': "Sujet du type « Pourquoi les trajectoires asiatiques et africaines "
         "diffèrent-elles ? »",
    'f': "La promotion des exportations lève la contrainte de taille du marché "
         "intérieur mais suppose un accès effectif aux marchés étrangers et une "
         "capacité de remontée de filière. Là où ces conditions ont été "
         "réunies, la stratégie a produit un rattrapage rapide ; ailleurs, "
         "l’exportation est restée primaire et n’a pas transformé la "
         "spécialisation.",
    'r': "Comparer les conditions de réussite plutôt que les stratégies "
         "affichées permet d’expliquer des résultats divergents à partir de "
         "politiques apparemment semblables.",
    'ex': "L’écart entre le droit de douane agricole de 15,9 % et le droit "
          "industriel de 3 %, qui oriente vers la voie manufacturière."}],
  voisins=['n3-isi', 'n3-emergence', 'n3-etat-developpeur',
           'n3-trappe-intermediaire', 'n3-dependance'])

d('n3-etat-developpeur', 3, "État développeur",
  "Un État qui organise la transformation des avantages comparatifs",
  "L’État développeur désigne un État qui ne se contente pas de garantir le "
  "cadre du marché mais organise activement la transformation de la structure "
  "productive : sélection de secteurs stratégiques, organisation du rattrapage "
  "technologique, soutien aux exportations. Le cours en donne l’illustration "
  "japonaise : par l’intermédiaire du MITI, les pouvoirs publics ont accompagné "
  "la transformation des avantages comparatifs et la montée en gamme "
  "industrielle.",
  "La notion répond à une question que les stratégies d’industrialisation "
  "laissent ouverte : qui opère la transformation ? La réponse de l’État "
  "développeur est qu’elle ne se produit pas spontanément et suppose une "
  "coordination que le marché n’assure pas. L’argument est précis : les "
  "investissements nécessaires à l’émergence d’une filière sont "
  "complémentaires — il faut simultanément des producteurs, des fournisseurs, "
  "des compétences et des infrastructures — et aucun acteur privé n’a intérêt à "
  "s’engager le premier. L’État lève ce blocage en coordonnant les décisions et "
  "en garantissant des débouchés. Le cours insiste sur un point essentiel, qui "
  "évite le contresens le plus fréquent : le Japon n’abandonne pas sa "
  "spécialisation au marché, mais il organise la transformation de ses "
  "avantages comparatifs — et un État fort ne signifie pas nécessairement un "
  "État qui ferme son économie. Les trajectoires gagnantes reposent au "
  "contraire sur une ouverture sélective et pragmatique, c’est-à-dire sur une "
  "ouverture maîtrisée plutôt que brutale, qui consiste à s’ouvrir sans "
  "libéraliser tous les flux. L’État développeur n’est donc ni "
  "protectionniste ni libre-échangiste : il est sélectif.",
  [("La sélection de secteurs stratégiques",
    "L’État identifie les filières dont le développement transformera la "
    "structure productive, en fonction de leur potentiel de montée en gamme et "
    "de leurs effets d’entraînement."),
   ("La coordination des investissements complémentaires",
    "Producteurs, fournisseurs, compétences et infrastructures doivent "
    "apparaître simultanément. L’État coordonne ces décisions que le marché ne "
    "synchronise pas."),
   ("L’organisation du rattrapage technologique",
    "Acquisition de licences, imitation, formation d’ingénieurs : l’État "
    "accélère l’absorption des technologies étrangères plutôt que d’attendre "
    "leur diffusion spontanée."),
   ("Le soutien aux exportations",
    "Garantir un débouché extérieur impose aux entreprises soutenues la "
    "discipline du marché mondial, ce qui évite la rente que produirait une "
    "protection purement intérieure."),
   ("L’ouverture sélective",
    "Le pays s’ouvre sans libéraliser tous les flux : l’ouverture porte sur ce "
    "qui apporte technologies et débouchés, et reste contrôlée là où elle "
    "menacerait les filières en construction.")],
  [{'a': "L’État développeur lève un problème de coordination que le marché ne "
         "résout pas, puisque les investissements nécessaires à une filière sont "
         "complémentaires.",
    'cond': "Il faut une administration compétente, insérée dans le tissu "
            "productif et protégée de la capture par les intérêts qu’elle "
            "soutient.",
    'lim': "Cette autonomie est rare : un État proche des entreprises risque "
           "d’être capturé, un État distant manque de l’information nécessaire."},
   {'a': "L’association du soutien public et de la contrainte exportatrice évite "
         "la rente : l’entreprise aidée doit affronter la concurrence mondiale.",
    'cond': "Le soutien doit être conditionné à des résultats vérifiables à "
            "l’exportation et retiré en cas d’échec.",
    'lim': "La conditionnalité est politiquement coûteuse à appliquer, les "
           "entreprises soutenues devenant des interlocuteurs influents."},
   {'a': "L’ouverture sélective permet de capter les bénéfices de l’échange sans "
         "exposer prématurément les filières en construction.",
    'cond': "La sélection doit être explicite, bornée et révisable, sans quoi "
            "elle se transforme en protection permanente.",
    'lim': "Elle suppose une capacité de discernement sectoriel que les "
           "administrations ne possèdent pas toutes."}],
  [{'t': "L’État ne dispose pas de l’information nécessaire pour sélectionner "
         "les secteurs d’avenir et se laisse guider par les intérêts les mieux "
         "organisés.",
    'qui': "Objection informationnelle et de capture, classique en économie "
           "politique.",
    'rep': "L’expérience japonaise montre qu’une administration insérée dans le "
           "tissu productif peut réduire l’asymétrie d’information, mais elle "
           "confirme aussi que l’autonomie à l’égard des intérêts soutenus est "
           "la condition décisive."},
   {'t': "Un État fort est un État qui ferme son économie, ce qui prive le pays "
         "des technologies et des débouchés extérieurs.",
    'qui': "Contresens que le cours écarte explicitement.",
    'rep': "Le cours est net : un État fort ne signifie pas nécessairement un "
           "État qui ferme son économie, et les trajectoires gagnantes reposent "
           "sur une ouverture sélective et pragmatique."},
   {'t': "Les succès de l’État développeur ne sont pas transposables : ils "
         "dépendent de configurations historiques et institutionnelles "
         "particulières.",
    'qui': "Dani Rodrik, pour qui les trajectoires dépendent des institutions et "
           "des compromis politiques, sans modèle unique.",
    'rep': "L’objection est juste et interdit de prescrire un modèle. Elle "
           "n’annule pas le mécanisme identifié — la coordination des "
           "investissements complémentaires — qui reste général."}],
  [{'n': "Alexander Gerschenkron",
    'i': "Le retard peut être compensé par l’État, les banques ou de grandes "
         "institutions mobilisant le capital.",
    'p': "La substitution institutionnelle est le fondement théorique de l’État "
         "développeur : plus le retard est important, plus la mobilisation du "
         "capital doit être centralisée, parce que l’accumulation progressive "
         "n’a pas eu lieu."},
   {'n': "Dani Rodrik",
    'i': "Les trajectoires de développement dépendent des institutions et des "
         "compromis politiques, sans recette universelle.",
    'p': "Des arrangements institutionnels différents peuvent remplir les mêmes "
         "fonctions économiques : l’État développeur est une configuration "
         "possible, non un modèle à reproduire."},
   {'n': "Philippe Aghion",
    'i': "La politique industrielle doit être différenciée selon la distance à "
         "la frontière technologique.",
    'p': "L’État développeur agit surtout loin de la frontière, où l’imitation "
         "et la coordination suffisent ; à la frontière, les instruments "
         "doivent changer et le pari devient plus incertain."},
   {'n': "Friedrich List",
    'i': "La protection doit correspondre au stade de développement et préparer "
         "sa propre disparition.",
    'p': "L’ouverture sélective de l’État développeur applique cette logique "
         "séquentielle : protéger ce qui se construit, ouvrir ce qui est mûr, "
         "sans traiter l’ouverture comme une question de principe."}],
  [{'f': "Le cours cite, pour le Japon, la sélection de secteurs stratégiques, "
         "l’organisation du rattrapage technologique et le soutien aux "
         "exportations, conduits par l’intermédiaire du MITI.",
    'p': "L’énumération des trois instruments est directement utilisable comme "
         "définition opérationnelle de l’État développeur."},
   {'f': "Le cours précise que le Japon n’abandonne pas entièrement sa "
         "spécialisation au marché : il organise la transformation de ses "
         "avantages comparatifs.",
    'p': "La formule est essentielle : elle montre que l’avantage comparatif "
         "est traité comme une variable construite et non comme une donnée."},
   {'f': "Le cours ajoute qu’un État fort ne signifie pas nécessairement un État "
         "qui ferme son économie, les trajectoires gagnantes reposant sur une "
         "ouverture sélective et pragmatique.",
    'p': "La précision écarte l’assimilation de l’État développeur au "
         "protectionnisme et oriente vers la notion d’ouverture maîtrisée."}],
  [{'q': "Sujet du type « Un pays peut-il se développer sans État fort ? »",
    'f': "L’État développeur répond que la transformation de la structure "
         "productive suppose une coordination d’investissements complémentaires "
         "qu’aucun acteur privé n’a intérêt à amorcer seul. Mais le cours "
         "précise immédiatement qu’un État fort n’est pas un État fermé : les "
         "trajectoires gagnantes reposent sur une ouverture sélective et "
         "pragmatique.",
    'r': "Distinguer la force de l’État, qui est une capacité de coordination, "
         "de la fermeture, qui est un choix commercial, permet d’éviter la "
         "confusion la plus fréquente sur ce sujet.",
    'ex': "Le Japon et le MITI, qui organisent la transformation des avantages "
          "comparatifs et la montée en gamme industrielle."},
   {'q': "Sujet du type « L’État peut-il choisir les secteurs d’avenir ? »",
    'f': "L’expérience de l’État développeur montre que la sélection est "
         "praticable loin de la frontière technologique, où les filières à "
         "développer sont déjà identifiées ailleurs, et qu’elle devient un pari "
         "à la frontière. La question n’est donc pas la compétence de l’État en "
         "général mais la position technologique du pays.",
    'r': "Faire dépendre la capacité de sélection de la distance à la frontière "
         "technologique fournit une réponse différenciée et évite le débat "
         "doctrinal.",
    'ex': "Le rattrapage technologique organisé par le MITI, dans une phase où "
          "le Japon était encore éloigné de la frontière."}],
  voisins=['n3-isi', 'n3-ipe', 'n3-transformation', 'n3-emergence',
           'n3-dependance'])
