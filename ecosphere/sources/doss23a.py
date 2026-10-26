# -*- coding: utf-8 -*-
"""Ensemble 23 — Structure sociale et mobilité (1/3)."""

from doss_base import d

d('n23-classes-sociales', 23, "Classes sociales",
  "Découper la société en groupes pour expliquer la production et la répartition",
  "Une classe sociale est un groupe d’individus défini par une position "
  "commune dans l’organisation économique, position qui détermine la part "
  "de richesse qu’il reçoit. Le cours ne donne pas une définition unique : "
  "il présente plusieurs découpages concurrents, chacun reposant sur un "
  "critère différent — la productivité chez Quesnay, la place dans la "
  "production chez Marx, le statut social chez Veblen — et montre que le "
  "choix du critère commande l’ensemble de l’analyse économique qui suit.",
  "Le raisonnement par classes naît avec Quesnay, qui est le premier à "
  "raisonner en termes de classes sociales : selon lui l’économie est un "
  "circuit où la richesse circule entre classes. Il divise la société en "
  "trois classes indissociables : la classe productive, composée des "
  "agriculteurs fermiers, seule créatrice de produit net, c’est-à-dire de "
  "surplus après déduction des dépenses nécessaires à la production ; la "
  "classe des propriétaires, qui perçoit la rente ; la classe stérile, "
  "composée des artisans, commerçants et manufacturiers, dite stérile non "
  "parce qu’elle serait inutile mais parce qu’elle ne produit pas de "
  "produit net. Le critère de Quesnay est donc la productivité économique. "
  "Le cours souligne que Ricardo reprendra l’idée de classement en classes "
  "avec un autre contenu — propriétaires, capitalistes, travailleurs — et "
  "que cette filiation fait de Quesnay un ancêtre de la comptabilité "
  "nationale moderne. Marx déplace le critère : les classes sont définies "
  "par la place dans la production. Comme les classiques, il identifie "
  "trois classes sociales, salariés, capitalistes et propriétaires "
  "fonciers, mais il montre que la rente foncière et le profit industriel "
  "sont deux formes d’appropriation de la plus-value et proviennent tous "
  "deux du capital. Le rapport entre classes n’est donc plus un rapport de "
  "contribution mais un rapport d’exploitation, et l’histoire des sociétés "
  "est fondée sur la lutte des classes. Veblen opère un troisième "
  "déplacement : sa classe de loisir n’est pas définie par la productivité "
  "mais par le statut social, l’oisiveté et la consommation ostentatoire. "
  "Le cours insiste sur le fait qu’il ne faut pas confondre classe de "
  "loisir et classe stérile : Quesnay classe par production, Veblen classe "
  "par prestige social. Enfin, le cours documente la disparition du "
  "raisonnement par classes dans la théorie dominante : les néoclassiques "
  "cherchent à rompre avec l’analyse de Marx, jugée trop centrée sur les "
  "classes sociales et les rapports de domination, et expliquent les "
  "phénomènes globaux à partir des comportements individuels. Il est "
  "explicitement noté qu’il n’y a plus de classes sociales dans la "
  "microéconomie : le consommateur se définit par ses préférences et par "
  "les ressources dont il dispose. La notion de classe n’est donc pas un "
  "acquis cumulatif de la science économique, c’est un outil qui apparaît, "
  "se transforme et disparaît selon la question posée.",
  [("Un critère de découpage est choisi",
    "Toute analyse en classes commence par le choix d’un critère : le "
    "produit net chez Quesnay, la place dans la production chez Marx, le "
    "prestige chez Veblen. Ce choix n’est pas neutre, il décide à l’avance "
    "de ce que l’analyse pourra voir et de ce qu’elle rendra invisible."),
   ("Le critère engendre une hiérarchie",
    "Une fois le critère posé, les groupes se classent : productifs contre "
    "stériles, exploiteurs contre exploités, classe de loisir contre "
    "classes inférieures. La hiérarchie n’est pas ajoutée après coup, elle "
    "est contenue dans le critère retenu."),
   ("La hiérarchie commande la répartition",
    "À chaque position correspond un type de revenu : la rente pour les "
    "propriétaires, le profit pour les capitalistes, le salaire pour les "
    "travailleurs. La classe détermine donc non seulement le rang mais la "
    "forme du revenu perçu, et donc sa dynamique dans le temps."),
   ("La répartition engendre un rapport entre classes",
    "Selon le critère, ce rapport est de complémentarité — les trois "
    "classes de Quesnay sont indissociables et le circuit ne fonctionne que "
    "si chacune dépense — ou d’antagonisme : chez Marx la plus-value prise "
    "aux uns est le profit des autres, ce qui rend le conflit structurel."),
   ("Le rapport explique la dynamique historique",
    "Chez Marx, la lutte des classes et les contradictions du système "
    "produisent des crises structurelles et cycliques, non accidentelles. "
    "Chez Veblen, la reproduction des hiérarchies se fait par imitation et "
    "conformisme, ce qui entretient inégalités et gaspillage sans conflit."),
   ("Le changement de critère fait disparaître la classe",
    "Quand les néoclassiques remplacent la position dans la production par "
    "les préférences individuelles, la classe cesse d’être un objet : il ne "
    "reste que des consommateurs dotés de ressources inégales. L’inégalité "
    "subsiste, mais elle n’est plus pensée comme un rapport social.")],
  [{'a': "Raisonner en classes permet de relier production et répartition "
         "dans un même mouvement : le tableau de Quesnay montre comment le "
         "produit net créé par une classe circule vers les deux autres, ce "
         "qui fait de l’économie un circuit et non une collection "
         "d’échanges isolés.",
    'cond': "L’argument vaut si les groupes retenus se distinguent "
            "réellement par leur fonction économique et si leurs dépenses "
            "sont suffisamment homogènes pour que le circuit soit "
            "représentatif — c’est le cas dans l’économie agricole que "
            "Quesnay décrit.",
    'lim': "Le cours relève que la vision de Quesnay est trop restrictive, "
           "puisqu’elle refuse toute productivité à l’industrie et au "
           "commerce. Un découpage fonctionnel hérité d’une époque devient "
           "faux dès que la structure productive change."},
   {'a': "Définir les classes par la place dans la production donne un "
         "fondement mesurable à l’inégalité : le taux de plus-value PL/V "
         "mesure le degré d’exploitation du travail, et la composition "
         "organique C/V l’importance relative des machines par rapport au "
         "travail humain.",
    'cond': "Ce raisonnement suppose la théorie de la valeur-travail, "
            "c’est-à-dire que la valeur d’échange est déterminée par le "
            "temps de travail socialement nécessaire, et que seul le "
            "capital variable crée de la valeur nouvelle.",
    'lim': "Si l’on abandonne la valeur-travail, la plus-value cesse d’être "
           "mesurable et le rapport de classes perd son fondement "
           "quantitatif. C’est précisément la rupture opérée par les "
           "néoclassiques, qui font dépendre la valeur de l’utilité "
           "marginale et non du travail incorporé."},
   {'a': "Classer par le statut plutôt que par la production permet "
         "d’expliquer des comportements que la production n’explique pas : "
         "Veblen montre que l’on consomme non pour satisfaire un besoin "
         "mais pour afficher richesse et statut, la consommation devenant "
         "instrument de distinction et de domination symbolique.",
    'cond': "Il faut admettre que les comportements économiques dépendent "
            "des habitudes, des normes, des institutions et de la recherche "
            "de statut social, donc rejeter l’homo œconomicus comme agent "
            "rationnel maximisateur.",
    'lim': "Le critère du prestige est beaucoup plus difficile à mesurer "
           "que le produit net ou le salaire. Veblen décrit une "
           "hiérarchie convaincante mais ne fournit pas l’équivalent du "
           "taux de plus-value : son analyse éclaire les comportements sans "
           "produire d’indicateur."},
   {'a': "Conserver la notion de classe reste utile aujourd’hui parce que "
         "les positions économiques continuent de commander les revenus : "
         "les salaires varient selon la catégorie socioprofessionnelle, un "
         "cadre supérieur gagnant environ 2,4 fois le salaire d’un employé.",
    'cond': "Cela suppose que les catégories statistiques utilisées "
            "recoupent bien des positions sociales distinctes, et pas "
            "seulement des niveaux de revenu : la catégorie doit renvoyer à "
            "une place dans l’organisation du travail.",
    'lim': "Le cours montre que ces frontières se brouillent : les ouvriers "
           "existent toujours mais travaillent davantage dans les "
           "services, leur niveau de qualification évolue et l’ouvrier "
           "spécialisé non qualifié devient moins dominant. La classe se "
           "maintient comme inégalité mesurée plus que comme groupe "
           "identifiable."}],
  [{'t': "Le raisonnement par classes serait dépassé : il faudrait partir "
         "des individus, de leurs préférences et de leurs contraintes, puis "
         "agréger les comportements pour comprendre le fonctionnement du "
         "marché.",
    'qui': "Les néoclassiques, et la microéconomie telle que le cours la "
           "présente — « plus de classes sociales dans la microéconomie ».",
    'rep': "Le cours ne traite pas ce déplacement comme un progrès net : il "
           "note qu’on passe d’une économie politique centrée sur la "
           "production, la répartition et les rapports sociaux à une "
           "économie des choix individuels. Ce que l’on gagne en rigueur "
           "formelle, on le perd en capacité à penser la répartition."},
   {'t': "Même en gardant des classes, il n’y a pas de lutte : Smith "
         "identifie des groupes sociaux sans lutte, et le capitalisme obéit "
         "à des lois naturelles qui tendent vers l’équilibre ou vers des "
         "limites techniques.",
    'qui': "Les classiques, selon la comparaison explicite du cours entre "
           "Smith, Ricardo, Malthus et Marx.",
    'rep': "Marx rejette cette vision : pour lui les lois économiques sont "
           "historiques et liées au mode de production, et le capitalisme "
           "est fondé sur des relations antagonistes et des crises "
           "inévitables. Le désaccord ne porte pas sur l’existence des "
           "classes mais sur la nature du lien qui les unit."},
   {'t': "La hiérarchie sociale ne se maintient pas par l’exploitation mais "
         "par l’imitation : les classes inférieures cherchent à copier les "
         "signes de richesse de la classe dominante, parfois au détriment "
         "de leurs besoins essentiels.",
    'qui': "Veblen, dont le cours oppose terme à terme la lecture à celle "
           "de Marx : « Marx explique la domination par l’exploitation et "
           "le conflit. Veblen l’explique par le statut, la culture et "
           "l’émulation sociale. »",
    'rep': "Les deux lectures ne s’excluent pas : l’exploitation peut "
           "produire la hiérarchie des revenus et l’imitation en assurer "
           "l’acceptation. Une dissertation gagne à les articuler plutôt "
           "qu’à choisir, puisque le cours les présente comme deux "
           "mécanismes de reproduction et non comme deux erreurs."}],
  [{'n': "François Quesnay",
    'i': "L’économie est un circuit où la richesse circule entre classes "
         "sociales ; il est le premier à raisonner ainsi.",
    'p': "Médecin de Louis XV, fils de laboureur devenu propriétaire, il "
         "identifie trois classes indissociables : la classe productive "
         "(agriculteurs fermiers), seule créatrice de produit net ; les "
         "propriétaires, qui perçoivent la rente ; la classe stérile "
         "(artisans, commerçants, manufacturiers). Le cours retient qu’il "
         "est le premier à classer l’économie en classes sociales et à "
         "penser l’économie comme un circuit, ancêtre de la comptabilité "
         "nationale."},
   {'n': "David Ricardo",
    'i': "Il reprend de Quesnay l’idée de classement en classes, avec un "
         "contenu renouvelé : propriétaires, capitalistes, travailleurs.",
    'p': "Le cours présente cette reprise comme l’héritage direct de "
         "Quesnay dans la pensée classique. Le découpage de Ricardo n’est "
         "plus fondé sur l’agriculture comme seule source de surplus mais "
         "sur la distinction entre les trois grands types de revenus — "
         "rente, profit, salaire — ce qui fait de la répartition le cœur de "
         "l’analyse économique classique."},
   {'n': "Karl Marx",
    'i': "Les classes sont définies par la place dans la production, et "
         "l’histoire des sociétés est fondée sur la lutte des classes.",
    'p': "Il identifie comme les classiques trois classes — salariés, "
         "capitalistes, propriétaires fonciers — mais montre que la rente "
         "foncière et le profit industriel sont deux formes d’appropriation "
         "de la plus-value provenant toutes deux du capital. Le Manifeste "
         "du Parti communiste (1848), écrit avec Friedrich Engels, est à la "
         "fois un texte théorique et politique visant à donner aux "
         "travailleurs une lecture cohérente du capitalisme."},
   {'n': "Thorstein Veblen",
    'i': "La classe dominante n’est pas définie par la productivité mais "
         "par le statut social, l’oisiveté et la consommation ostentatoire.",
    'p': "Dans Théorie de la classe de loisir (1899), il montre qu’une "
         "classe dominante ne produit pas directement, vit du capital et de "
         "la rente et impose les normes du prestige. Le cours insiste sur "
         "la distinction avec Quesnay : la classe de loisir n’est pas la "
         "classe stérile, puisque le critère est le prestige social et non "
         "la productivité économique."}],
  [{'f': "Quesnay distingue la classe productive, la classe des "
         "propriétaires et la classe stérile, et réserve le produit net à "
         "la seule agriculture.",
    'p': "C’est le premier découpage de la société fondé sur un critère "
         "économique explicite, et il montre que le classement dépend "
         "entièrement de la théorie de la valeur retenue : rendre "
         "l’industrie stérile n’est pas une erreur d’observation mais la "
         "conséquence du critère choisi."},
   {'f': "Marx définit le taux de profit comme PL/(C+V), puis fait "
         "apparaître le taux de plus-value PL/V et la composition organique "
         "du capital C/V.",
    'p': "Le rapport entre classes devient une grandeur calculable : "
         "l’exploitation n’est plus une dénonciation morale mais un rapport "
         "mesuré entre la valeur créée par le travail et la part qui lui "
         "est versée."},
   {'f': "La microéconomie, telle que le cours la présente, ne comporte "
         "plus de classes sociales : le consommateur se définit par ses "
         "préférences et par les ressources dont il dispose.",
    'p': "La disparition de la classe n’est pas due à la disparition des "
         "inégalités mais à un changement d’objet théorique : l’inégalité "
         "devient une différence de dotation initiale, non un rapport "
         "social à expliquer."},
   {'f': "En France, la part des ouvriers dans la population active passe "
         "de 34,7 % en 1982 à 18,6 % en 2023, l’effectif reculant d’environ "
         "8,263 millions à 5,325 millions.",
    'p': "Le groupe qui servait de référence empirique à l’analyse en "
         "classes perd la moitié de son poids relatif en quarante ans, ce "
         "qui explique pourquoi la question des classes sociales se pose "
         "aujourd’hui en termes de recomposition plutôt que de disparition."}],
  [{'q': "Les classes sociales sont-elles encore un outil pertinent "
         "d’analyse économique ?",
    'f': "La notion de classe sociale n’est pas un acquis que la science "
         "économique aurait conservé, c’est un outil qui apparaît, se "
         "transforme et disparaît selon la question posée. Quesnay "
         "l’invente pour expliquer la circulation du produit net, Marx la "
         "refonde pour expliquer l’exploitation, Veblen la déplace pour "
         "expliquer la consommation, et les néoclassiques l’abandonnent "
         "pour expliquer les prix. Juger de sa pertinence suppose donc de "
         "préciser d’abord ce que l’on cherche à expliquer : une "
         "répartition, un conflit, un comportement ou un équilibre.",
    'r': "Ce plan évite le faux débat « les classes existent-elles encore ». "
         "Il montre que la réponse dépend du critère, et il permet de "
         "mobiliser successivement les trois découpages du cours sans les "
         "opposer artificiellement, puis de conclure par la recomposition "
         "contemporaine du monde ouvrier.",
    'ex': "Le passage de la part des ouvriers de 34,7 % à 18,6 % de la "
          "population active entre 1982 et 2023, sans disparition du groupe."},
   {'q': "En quoi le choix d’un critère de classement détermine-t-il "
         "l’analyse de la répartition ?",
    'f': "Le critère retenu pour découper la société décide à l’avance de "
         "ce que l’analyse pourra voir. Si le critère est le produit net, "
         "l’industrie devient stérile et la rente légitime. Si le critère "
         "est la place dans la production, la rente et le profit "
         "apparaissent comme deux formes d’appropriation de la plus-value. "
         "Si le critère est le prestige, la richesse se lit dans la "
         "consommation ostentatoire et non dans la production. Le "
         "classement n’est donc jamais une simple description préalable : "
         "il contient déjà la thèse.",
    'r': "Ce raisonnement est solide parce qu’il s’appuie sur une "
         "comparaison que le cours fait lui-même, en opposant explicitement "
         "classe de loisir et classe stérile et en soulignant que le "
         "critère diffère — prestige social contre productivité économique.",
    'ex': "Chez Quesnay les artisans sont stériles, chez Marx ils sont "
          "productifs : le fait n’a pas changé, le critère si."},
   {'q': "Faut-il analyser la société par les groupes ou par les individus ?",
    'f': "La microéconomie fait disparaître les classes parce qu’elle part "
         "des individus, de leurs préférences et de leurs ressources, puis "
         "agrège les comportements. Mais ce déplacement a un coût : "
         "l’inégalité y devient une différence de dotation initiale, non un "
         "rapport social à expliquer. À l’inverse, l’analyse par classes "
         "explique la répartition mais suppose des groupes homogènes que "
         "les transformations du travail rendent plus difficiles à "
         "délimiter. Les deux approches ne répondent pas à la même "
         "question, et c’est ce décalage qu’il faut exposer.",
    'r': "Le plan tient parce qu’il refuse de trancher par préférence "
         "théorique et s’appuie sur la formulation du cours : on passe "
         "d’une économie politique centrée sur la production, la "
         "répartition et les rapports sociaux à une économie des choix "
         "individuels — c’est un changement d’objet, pas une réfutation.",
    'ex': "Le consommateur de la théorie microéconomique, défini par ses "
          "préférences et son revenu, sans aucune position de classe."}],
  voisins=['n23-rapports-de-classe', 'n23-conscience-de-classe',
           'n23-categories-socioprofessionnelles', 'n23-reproduction-sociale',
           'n23-polarisation-sociale'])

d('n23-categories-socioprofessionnelles', 23,
  "Catégories socioprofessionnelles",
  "Le découpage statistique par lequel le cours mesure les inégalités de travail",
  "Les catégories socioprofessionnelles sont les groupes statistiques — "
  "cadres supérieurs, professions intermédiaires, employés, ouvriers — par "
  "lesquels le cours ordonne les inégalités de salaire, de statut et de "
  "temps de travail. Le cours les utilise comme variable explicative des "
  "écarts de rémunération et comme repère de l’évolution de la structure "
  "sociale, sans jamais présenter la construction de la nomenclature "
  "elle-même : ce point de vocabulaire doit être signalé.",
  "Le cours mobilise les catégories socioprofessionnelles en trois temps. "
  "D’abord comme variable explicative des salaires : il énonce que les "
  "salaires varient selon la catégorie socioprofessionnelle, le sexe, le "
  "statut et le temps de travail, et donne les ordres de grandeur en "
  "équivalent temps plein, environ 4 629 € nets par mois pour les cadres "
  "supérieurs contre environ 1 941 € pour les employés, soit un rapport de "
  "2,4. Ensuite comme variable de différenciation des conditions d’emploi : "
  "en 2025, 17,7 % des emplois sont à temps partiel, mais 41,7 % des "
  "employés peu qualifiés travaillent à temps partiel contre 11,1 % des "
  "cadres. Le temps partiel peut être choisi ou subi, et lorsqu’un individu "
  "souhaite travailler davantage sans trouver d’heures supplémentaires, il "
  "se rapproche d’une situation de sous-emploi. La catégorie ne détermine "
  "donc pas seulement le niveau du revenu mais la nature du contrat et le "
  "volume de travail accessible. Enfin comme repère de l’évolution "
  "historique : le cours suit précisément une catégorie, les ouvriers, dont "
  "l’effectif passe d’environ 8,263 millions en 1982 à environ 5,325 "
  "millions en 2023 et la part dans la population active de 34,7 % à "
  "18,6 %, sous l’effet de la désindustrialisation. Il insiste sur le fait "
  "que cette évolution ne fait pas disparaître le monde ouvrier mais le "
  "transforme : les ouvriers travaillent davantage dans les services, leur "
  "niveau de qualification évolue, leur scolarisation augmente et l’ouvrier "
  "spécialisé non qualifié devient moins dominant. La catégorie est donc "
  "un instrument à double tranchant : indispensable pour mesurer, mais "
  "susceptible de masquer une recomposition interne quand on se contente de "
  "lire son poids global. Il faut enfin signaler une limite de couverture : "
  "les cours utilisent la catégorie socioprofessionnelle comme variable de "
  "différenciation des salaires, mais ne présentent ni la construction de "
  "la nomenclature, ni les critères de classement, ni les débats sur sa "
  "pertinence. Une dissertation ne peut donc pas s’appuyer sur ces cours "
  "pour discuter l’outil statistique lui-même, seulement pour en utiliser "
  "les résultats.",
  [("La position professionnelle fixe le niveau de salaire",
    "Le cours établit que les salaires varient selon la catégorie "
    "socioprofessionnelle : environ 4 629 € nets mensuels en équivalent "
    "temps plein pour un cadre supérieur contre 1 941 € pour un employé. "
    "L’écart n’est pas marginal, c’est un rapport de 2,4."),
   ("La position fixe aussi le volume de travail accessible",
    "Le temps partiel ne se répartit pas uniformément : 41,7 % des employés "
    "peu qualifiés y sont contre 11,1 % des cadres. La catégorie détermine "
    "donc la quantité d’heures qu’on peut obtenir, et pas seulement le prix "
    "de l’heure travaillée."),
   ("L’effet se cumule sur le revenu total",
    "Un salaire horaire plus faible combiné à un volume d’heures plus "
    "faible produit un écart de revenu bien supérieur à l’écart de salaire "
    "en équivalent temps plein. C’est pourquoi l’écart total de masse "
    "salariale entre femmes et hommes, 23,5 %, dépasse l’écart à temps de "
    "travail égal, 14,9 %."),
   ("La position fixe enfin la sécurité du statut",
    "Le cours distingue les inégalités de statut : CDI, CDD, intérim, "
    "emplois précaires. Tous les travailleurs n’ont pas la même sécurité, "
    "et l’opposition porte entre ceux qui bénéficient d’un emploi stable et "
    "ceux qui enchaînent les contrats courts."),
   ("La structure des catégories se déforme dans le temps",
    "La désindustrialisation fait reculer la part des ouvriers de 34,7 % à "
    "18,6 % de la population active entre 1982 et 2023. La photographie "
    "statistique change donc de composition, ce qui interdit de comparer "
    "mécaniquement des moyennes catégorielles à quarante ans d’écart."),
   ("La catégorie elle-même change de contenu",
    "Les ouvriers ne disparaissent pas mais travaillent davantage dans les "
    "services, se qualifient et se scolarisent davantage. Le même mot "
    "désigne en 2023 une réalité professionnelle différente de celle de "
    "1982, ce qui est la principale précaution de lecture.")],
  [{'a': "La catégorie socioprofessionnelle est l’outil le plus efficace "
         "pour objectiver les inégalités de travail, parce qu’elle permet "
         "de rapporter un écart de salaire à une position dans "
         "l’organisation productive plutôt qu’à une caractéristique "
         "individuelle.",
    'cond': "Il faut que les catégories soient suffisamment homogènes en "
            "interne et suffisamment distinctes entre elles : le rapport de "
            "2,4 entre cadres supérieurs et employés n’a de sens que si ces "
            "deux groupes correspondent à des positions réellement "
            "différentes.",
    'lim': "Le cours montre lui-même la fragilité de cette homogénéité : la "
           "qualification des ouvriers évolue et l’ouvrier spécialisé non "
           "qualifié devient moins dominant. Une moyenne catégorielle "
           "recouvre donc des situations de plus en plus dispersées."},
   {'a': "Croiser la catégorie avec d’autres variables permet de "
         "décomposer les inégalités : le cours montre que l’écart "
         "femmes-hommes varie selon la catégorie, environ 15 % chez les "
         "cadres supérieurs, 11 % dans les professions intermédiaires, 12 % "
         "chez les ouvriers et seulement 2 % chez les employés.",
    'cond': "Cette décomposition exige des effectifs suffisants dans chaque "
            "croisement et une mesure homogène, ici l’équivalent temps "
            "plein, sans quoi les écarts observés reflètent surtout des "
            "différences de durée du travail.",
    'lim': "La décomposition ne dit pas quelle variable est première. Un "
           "écart faible chez les employés peut signaler une égalité réelle "
           "ou un écrasement général des salaires vers le bas, et le cours "
           "n’en fournit pas l’interprétation."},
   {'a': "Suivre une catégorie dans le temps éclaire les transformations "
         "structurelles de l’économie : le recul de la part des ouvriers de "
         "34,7 % à 18,6 % entre 1982 et 2023 donne une mesure concrète de "
         "la désindustrialisation française.",
    'cond': "L’argument tient si la nomenclature reste stable sur la "
            "période et si l’on distingue l’effet de composition — moins "
            "d’emplois industriels — de l’effet de contenu — des ouvriers "
            "qui travaillent dans les services.",
    'lim': "Le cours prévient précisément contre la lecture mécanique : la "
           "désindustrialisation ne fait pas disparaître le monde ouvrier, "
           "elle réduit son poids numérique et transforme ses secteurs, ses "
           "qualifications et son identité collective."},
   {'a': "La catégorie reste le meilleur relais pour articuler inégalités "
         "économiques et inégalités sociales, puisqu’elle commande "
         "simultanément le salaire, le statut, le temps de travail et, par "
         "la désindustrialisation, l’identité collective.",
    'cond': "Il faut accepter que la position professionnelle ait des "
            "effets au-delà du revenu, ce que le cours établit en liant la "
            "transformation du monde ouvrier à la perte de son identité "
            "collective et au recul de ses porte-parole.",
    'lim': "Cette articulation reste descriptive dans les cours : ils "
           "constatent la simultanéité des évolutions sans établir de lien "
           "causal mesuré entre position professionnelle et appartenance "
           "subjective."}],
  [{'t': "Les catégories socioprofessionnelles seraient devenues trop "
         "hétérogènes pour mesurer quoi que ce soit : à l’intérieur d’une "
         "même catégorie, les situations de statut, de temps de travail et "
         "de qualification diffèrent désormais plus qu’entre catégories.",
    'qui': "Le cours lui-même, qui souligne que la qualification des "
           "ouvriers évolue et que l’ouvrier spécialisé non qualifié "
           "devient moins dominant.",
    'rep': "L’objection invite à croiser plutôt qu’à abandonner. Le cours "
           "montre la voie en décomposant l’écart salarial femmes-hommes : "
           "23,5 % en masse salariale, 14,9 % à temps de travail égal, 4 % "
           "toutes choses égales par ailleurs. La catégorie reste utile dès "
           "qu’on la combine au statut, au temps de travail et au diplôme."},
   {'t': "La vraie frontière ne passerait pas entre catégories mais entre "
         "ceux qui ont un emploi et ceux qui en sont privés, le chômage "
         "fragilisant simultanément le revenu, le statut et l’intégration "
         "sociale.",
    'qui': "Le cours, qui écrit que la principale inégalité reste la "
           "distinction entre ceux qui disposent d’un emploi et ceux qui en "
           "sont privés.",
    'rep': "La remarque est juste mais ne disqualifie pas la catégorie : "
           "l’exposition au chômage est elle-même très inégale selon la "
           "position, et le halo du chômage, qui regroupe les personnes "
           "souhaitant travailler sans remplir tous les critères officiels, "
           "concerne surtout les emplois les moins qualifiés et les temps "
           "partiels subis."},
   {'t': "Le découpage par catégories serait une construction statistique "
         "arbitraire, au même titre que le chômage dont le cours montre "
         "qu’il constitue une construction sociale et statistique variant "
         "de 2,6 à plus de 7 millions selon la définition retenue.",
    'rep': "Le parallèle est éclairant mais ne conduit pas au relativisme. "
           "Le cours tire de l’exemple du chômage une règle de méthode : il "
           "faut expliciter la définition retenue, non renoncer à mesurer. "
           "Il faut cependant reconnaître une limite de couverture : ces "
           "cours n’exposent pas la construction de la nomenclature "
           "socioprofessionnelle et ne permettent donc pas de discuter "
           "l’outil lui-même."}],
  [{'n': "Karl Marx",
    'i': "La position dans la production, et non le niveau de revenu, "
         "définit la place d’un groupe dans la société.",
    'p': "Le cours fait de cette thèse l’arrière-plan théorique du "
         "classement par position professionnelle : si le salaire dépend de "
         "la place occupée dans la production, alors mesurer les écarts "
         "entre catégories revient à mesurer un rapport social. Le rapport "
         "de 2,4 entre cadres supérieurs et employés prend ainsi un sens "
         "différent d’un simple écart de dotation."},
   {'n': "Thorstein Veblen",
    'i': "La hiérarchie sociale se lit dans les modes de vie et la "
         "consommation autant que dans la position productive.",
    'p': "Son analyse éclaire ce que la catégorie statistique ne capte "
         "pas : la consommation ostentatoire, la distinction et la "
         "reconnaissance sociale. Elle explique pourquoi une catégorie peut "
         "perdre son identité collective — comme le monde ouvrier après la "
         "désindustrialisation — sans que ses effectifs disparaissent, "
         "puisque les normes de prestige ne suivent pas les effectifs."},
   {'n': "Robert Castel",
    'i': "La société salariale a stabilisé les positions professionnelles "
         "en y attachant des protections, et sa transformation les "
         "fragilise.",
    'p': "Dans Les Métamorphoses de la question sociale (1995), il montre "
         "que le statut d’emploi est le support des protections sociales. "
         "Cela éclaire les inégalités de statut relevées par le cours — "
         "CDI, CDD, intérim, emplois précaires — qui ne sont pas des "
         "variantes contractuelles mais des degrés d’appartenance à la "
         "société salariale."}],
  [{'f': "En équivalent temps plein, un cadre supérieur perçoit environ "
         "4 629 € nets par mois contre environ 1 941 € pour un employé, "
         "soit un rapport de 2,4.",
    'p': "Cela montre que la position professionnelle reste un déterminant "
         "massif du revenu du travail, indépendamment des différences de "
         "durée travaillée puisque la mesure est déjà corrigée du temps "
         "partiel."},
   {'f': "En 2025, 17,7 % des emplois sont à temps partiel, dont 41,7 % des "
         "employés peu qualifiés contre 11,1 % des cadres.",
    'p': "L’inégalité de catégorie ne porte pas seulement sur le prix de "
         "l’heure mais sur le nombre d’heures accessibles, ce qui amplifie "
         "l’écart de revenu total bien au-delà de l’écart de salaire "
         "horaire."},
   {'f': "La part des ouvriers dans la population active recule de 34,7 % "
         "en 1982 à 18,6 % en 2023, l’effectif passant d’environ 8,263 à "
         "5,325 millions.",
    'p': "La structure des catégories n’est pas un cadre fixe : elle "
           "enregistre la désindustrialisation, ce qui en fait un "
           "instrument de mesure du changement structurel autant que de "
           "l’inégalité instantanée."},
   {'f': "L’écart salarial femmes-hommes vaut environ 15 % chez les cadres "
         "supérieurs, 11 % dans les professions intermédiaires, 12 % chez "
         "les ouvriers et 2 % chez les employés.",
    'p': "Le croisement de la catégorie et du sexe montre que l’inégalité "
         "de genre n’est pas uniforme : elle est maximale là où les "
         "rémunérations sont les plus élevées et les plus "
         "individualisées."}],
  [{'q': "Les catégories socioprofessionnelles permettent-elles encore de "
         "rendre compte des inégalités de travail ?",
    'f': "Les catégories socioprofessionnelles conservent une forte "
         "capacité descriptive : elles ordonnent simultanément le salaire, "
         "avec un rapport de 2,4 entre cadres supérieurs et employés, le "
         "temps de travail, avec 41,7 % de temps partiel chez les employés "
         "peu qualifiés contre 11,1 % chez les cadres, et le statut, du CDI "
         "à l’intérim. Mais leur contenu se déforme : les ouvriers passent "
         "de 34,7 % à 18,6 % de la population active entre 1982 et 2023 "
         "tout en se qualifiant et en migrant vers les services. La "
         "catégorie reste donc un bon instrument de mesure à condition "
         "d’être lue comme une structure mobile et non comme une "
         "nomenclature intemporelle.",
    'r': "Ce raisonnement est solide parce qu’il appuie chaque affirmation "
         "sur une donnée du cours et parce qu’il reprend l’avertissement "
         "explicite du cours : la désindustrialisation ne fait pas "
         "disparaître le monde ouvrier, elle le transforme.",
    'ex': "Un ouvrier qualifié de la logistique en 2023, classé dans la "
          "même catégorie qu’un ouvrier spécialisé de 1982."},
   {'q': "Comment décomposer un écart de salaire observé ?",
    'f': "Un écart brut de salaire ne s’interprète pas tel quel : il faut "
         "le décomposer. Le cours en donne la méthode à propos des écarts "
         "femmes-hommes, qui valent 23,5 % en masse salariale totale, "
         "14,9 % à temps de travail égal, et environ 4 % toutes choses "
         "égales par ailleurs à diplôme, expérience et secteur "
         "équivalents. Chaque étape retire un effet de composition : le "
         "volume d’heures, puis la position professionnelle, pour isoler un "
         "résidu associé notamment à la discrimination.",
    'r': "C’est la démarche la plus rigoureuse disponible dans le cours, "
         "car elle évite les deux erreurs symétriques : attribuer tout "
         "l’écart brut à la discrimination, ou conclure de l’existence "
         "d’effets de structure qu’il n’y a pas de discrimination.",
    'ex': "Le passage de 23,5 % à 4 % une fois neutralisés le temps de "
          "travail et les positions professionnelles."},
   {'q': "La structure sociale française s’est-elle simplifiée ou "
         "complexifiée ?",
    'f': "La lecture globale suggère une simplification : une catégorie "
         "centrale, les ouvriers, perd la moitié de son poids relatif en "
         "quarante ans. Mais le cours corrige immédiatement cette lecture : "
         "le monde ouvrier est transformé, pas disparu, puisque les "
         "ouvriers travaillent davantage dans les services, se qualifient "
         "et se scolarisent davantage. Ce que l’on observe n’est donc pas "
         "une simplification mais une recomposition interne, à laquelle "
         "s’ajoute la montée des inégalités de statut et de temps de "
         "travail à l’intérieur des catégories.",
    'r': "Ce plan tient parce qu’il oppose explicitement la lecture par "
         "effectifs et la lecture par contenu, et parce que le cours fournit "
         "les deux séries : la part dans la population active d’un côté, "
         "les transformations de qualification et de secteur de l’autre.",
    'ex': "Les 41,7 % d’employés peu qualifiés à temps partiel, inégalité "
          "interne qu’aucune évolution d’effectifs ne révèle."}],
  voisins=['n23-classes-sociales', 'n23-conscience-de-classe',
           'n23-inegalites-genre', 'n23-discriminations',
           'n23-polarisation-sociale'])

d('n23-rapports-de-classe', 23, "Rapports de classe",
  "Exploitation, imitation ou interdépendance : trois lectures du lien entre groupes",
  "Les rapports de classe désignent la nature du lien qui unit les groupes "
  "sociaux entre eux. Le cours offre trois réponses distinctes : un rapport "
  "de complémentarité fonctionnelle chez Quesnay, où les trois classes sont "
  "indissociables ; un rapport d’exploitation et de conflit chez Marx, où "
  "la plus-value prise aux uns constitue le profit des autres ; un rapport "
  "d’émulation statutaire chez Veblen, où la hiérarchie se maintient par "
  "imitation des normes de prestige plutôt que par la lutte.",
  "Le cœur du rapport de classe chez Marx est l’exploitation, et le cours "
  "en détaille la mécanique. Toute marchandise possède une valeur d’usage, "
  "son utilité concrète, et une valeur d’échange, déterminée non par "
  "l’utilité mais par le temps de travail socialement nécessaire à sa "
  "production. Le travail lui-même devient une marchandise : le travailleur "
  "ne vend pas son travail achevé mais sa force de travail pour une durée "
  "donnée. Cette force de travail a elle aussi deux valeurs : sa valeur "
  "d’échange est le salaire, qui lui permet de subvenir à ses besoins "
  "essentiels et de reproduire sa force de travail ; sa valeur d’usage "
  "réside dans sa capacité à produire de la valeur nouvelle. De cette "
  "différence naît la plus-value : pendant la journée de travail, une "
  "partie du temps sert à produire l’équivalent du salaire, le reste "
  "produit une valeur supplémentaire non rémunérée, appropriée par le "
  "capitaliste. L’exploitation n’est donc pas un abus mais une structure : "
  "elle est le fondement du profit. Le cours ajoute que la rente foncière "
  "et le profit industriel sont deux formes d’appropriation de la "
  "plus-value et proviennent tous deux du capital, ce qui unifie les "
  "revenus non salariaux dans un même rapport. Ce rapport engendre une "
  "dynamique : les capitalistes investissent de plus en plus dans les "
  "machines, le capital constant, et relativement moins dans les salaires, "
  "le capital variable, alors que seul le travail humain crée de la valeur. "
  "La composition organique du capital C/V augmente, le taux de profit "
  "PL/(C+V) baisse tendanciellement, et cette baisse explique les crises, "
  "le chômage, la surproduction et les tensions sociales. Le système réduit "
  "ainsi sa propre source de profit : le rapport de classe est "
  "autodestructeur. Veblen propose un autre lien entre groupes. La classe "
  "de loisir ne produit pas directement, vit du capital et de la rente et "
  "impose les normes du prestige ; les classes inférieures entrent dans une "
  "dynamique d’imitation ou d’émulation, cherchant à copier les signes de "
  "richesse, parfois au détriment de leurs besoins essentiels. Le cours "
  "formule l’opposition avec netteté : Marx explique la domination par "
  "l’exploitation et le conflit, Veblen l’explique par le statut, la "
  "culture et l’émulation sociale. Une troisième lecture apparaît en "
  "sociologie des organisations : chez Crozier, le conflit est la "
  "conséquence normale de l’interdépendance des acteurs et non le produit "
  "d’un antagonisme de classe, ce qui déplace encore le fondement du "
  "rapport.",
  [("La force de travail est achetée comme marchandise",
    "Le travailleur ne vend pas un produit fini mais sa force de travail "
    "pour une durée donnée. Son prix, le salaire, correspond à ce qui lui "
    "permet de subvenir à ses besoins essentiels et de reproduire cette "
    "force de travail."),
   ("Son usage produit plus que son prix",
    "La valeur d’usage de la force de travail réside dans sa capacité à "
    "produire de la valeur nouvelle. Une partie de la journée suffit à "
    "produire l’équivalent du salaire ; le reste de la journée produit une "
    "valeur supplémentaire non versée au travailleur."),
   ("L’écart est approprié sous forme de plus-value",
    "Cette valeur non rémunérée est la plus-value, appropriée par le "
    "capitaliste. Elle constitue le fondement du profit et fait de "
    "l’exploitation un caractère structurel du capitalisme et non un abus "
    "individuel."),
   ("Le rapport se mesure et s’intensifie",
    "Le taux de plus-value PL/V mesure le degré d’exploitation. Il peut "
    "s’intensifier par l’allongement de la journée, l’accroissement de "
    "l’intensité du travail ou l’élévation de la productivité, sans que la "
    "forme du rapport change."),
   ("L’accumulation retourne le rapport contre lui-même",
    "Les capitalistes substituent du capital constant au capital variable, "
    "mais seul le travail humain crée de la valeur. La composition "
    "organique C/V monte, le taux de profit PL/(C+V) baisse "
    "tendanciellement : le système réduit sa propre source de profit."),
   ("La baisse du profit se traduit en crises",
    "Même si l’exploitation s’intensifie, elle ne compense pas "
    "l’augmentation du capital constant. Cette baisse explique les crises "
    "économiques, le chômage, la surproduction et les tensions sociales, "
    "qui sont structurelles et non accidentelles."),
   ("Une autre lecture : l’imitation remplace la lutte",
    "Chez Veblen, la classe dominante impose les normes du prestige et les "
    "classes inférieures les imitent. La reproduction des hiérarchies passe "
    "par l’imitation sociale, la diffusion des normes de prestige et le "
    "conformisme, ce qui entretient inégalités et gaspillage sans conflit "
    "ouvert.")],
  [{'a': "Penser le lien entre groupes comme un rapport d’exploitation "
         "donne une explication unifiée des revenus non salariaux : le "
         "cours établit que la rente foncière et le profit industriel sont "
         "deux formes d’appropriation de la plus-value et proviennent tous "
         "deux du capital.",
    'cond': "Cette unification suppose la théorie de la valeur-travail, "
            "c’est-à-dire que la valeur d’échange est déterminée par le "
            "temps de travail socialement nécessaire et que seul le capital "
            "variable crée de la valeur nouvelle.",
    'lim': "Si la valeur provient de l’utilité marginale et non du travail "
           "incorporé, comme le soutiennent les néoclassiques présentés "
           "dans le même chapitre, la plus-value disparaît comme grandeur "
           "et avec elle le fondement commun de la rente et du profit."},
   {'a': "Le rapport de classe explique les crises mieux que les analyses "
         "qui les traitent comme des accidents : chez Marx elles ne sont "
         "pas accidentelles mais structurelles, résultant de la lutte des "
         "classes et des contradictions du système.",
    'cond': "Il faut que la composition organique du capital augmente "
            "effectivement et que les gains de productivité ne suffisent "
            "pas à compenser la hausse du capital constant, faute de quoi "
            "la baisse du taux de profit n’a pas lieu.",
    'lim': "Le cours présente la baisse du taux de profit comme "
           "tendancielle, donc comme une tendance contrariable. Rien "
           "n’interdit que l’intensification de l’exploitation, la baisse "
           "du prix des équipements ou l’ouverture de nouveaux marchés la "
           "retardent durablement."},
   {'a': "Lire le rapport entre groupes comme une émulation statutaire "
         "explique des faits que l’exploitation n’explique pas, en "
         "particulier que les classes inférieures consomment pour paraître, "
         "parfois au détriment de leurs besoins essentiels.",
    'cond': "L’argument exige d’abandonner l’homo œconomicus : les "
            "comportements doivent dépendre des habitudes, des normes, des "
            "institutions et de la recherche de statut social, comme le "
            "soutient Veblen.",
    'lim': "L’émulation explique la stabilité de la hiérarchie mais non son "
           "origine : il faut déjà une classe dominante vivant du capital "
           "et de la rente pour qu’il y ait des normes de prestige à "
           "imiter. La lecture de Veblen complète celle de Marx plus "
           "qu’elle ne la remplace."},
   {'a': "Dans les organisations, le conflit ne nécessite pas de rapport de "
         "classe : chez Crozier il est la conséquence normale de "
         "l’interdépendance entre acteurs, chacun disposant d’une zone "
         "d’incertitude qui lui donne du pouvoir sur les autres.",
    'cond': "Cette lecture suppose un pouvoir relationnel et non "
            "attributif : le pouvoir n’est pas une propriété du statut mais "
            "la maîtrise d’une incertitude dont les autres dépendent, comme "
            "les ouvriers d’entretien du SEITA.",
    'lim': "Elle se situe à l’échelle de l’organisation et non de la "
           "société : elle explique les conflits internes à une entreprise "
           "mais ne rend pas compte de la répartition globale entre "
           "salaires, profits et rentes."}],
  [{'t': "Il n’y a pas de rapport antagonique entre groupes : Smith "
         "identifie des groupes sociaux sans lutte, et l’économie obéit à "
         "des lois naturelles tendant vers l’équilibre, l’harmonie ou des "
         "limites purement techniques.",
    'qui': "Les classiques, dans la comparaison que le cours établit entre "
           "Smith, Ricardo, Malthus et Marx.",
    'rep': "Marx rejette explicitement cette vision : les lois économiques "
           "sont historiques et liées au mode de production, et le "
           "capitalisme est fondé sur des relations antagonistes et des "
           "crises inévitables. Le désaccord porte donc sur le statut des "
           "lois économiques, naturelles ou historiques, plus que sur les "
           "faits observés."},
   {'t': "La domination ne repose pas sur l’exploitation mais sur le "
         "statut : la hiérarchie sociale se maintient surtout par "
         "l’imitation des normes de la classe dominante, prestige, "
         "consommation et modes de vie.",
    'qui': "Veblen, dont le cours résume la position en l’opposant terme à "
           "terme à celle de Marx.",
    'rep': "Les deux mécanismes opèrent à des niveaux différents : "
           "l’exploitation explique d’où vient le surplus, l’émulation "
           "explique pourquoi la hiérarchie est acceptée. Le cours "
           "n’arbitre pas et parle de deux logiques, l’une par le conflit, "
           "l’autre par le statut, la culture et l’émulation sociale."},
   {'t': "Le conflit ne découle pas d’un rapport de classe mais de "
         "l’organisation : il est la conséquence normale de "
         "l’interdépendance entre acteurs qui poursuivent des stratégies "
         "distinctes à l’intérieur d’un même système.",
    'qui': "Crozier, dans L’Acteur et le système (1977) écrit avec Erhard "
           "Friedberg, position que le cours présente explicitement comme "
           "une prise de distance avec Marx.",
    'rep': "La thèse de Crozier banalise le conflit sans le nier, et elle "
           "éclaire ce que le rapport de classe laisse de côté : les "
           "oppositions entre services, entre niveaux hiérarchiques ou "
           "entre métiers, qui ne se réduisent pas à l’opposition entre "
           "capital et travail mais qui n’annulent pas celle-ci."}],
  [{'n': "Karl Marx",
    'i': "La plus-value est la valeur produite par le travailleur et non "
         "payée dans son salaire ; elle fonde le profit.",
    'p': "Le cours détaille le raisonnement : la valeur d’échange de la "
         "force de travail est le salaire, nécessaire à la reproduction de "
         "cette force ; sa valeur d’usage est la capacité à produire de la "
         "valeur nouvelle. L’écart entre les deux, approprié par le "
         "capitaliste, révèle le caractère structurel de l’exploitation. Le "
         "cours résume : plus-value = ce que rapporte le salarié moins son "
         "salaire."},
   {'n': "Karl Marx",
    'i': "La hausse de la composition organique du capital entraîne une "
         "baisse tendancielle du taux de profit.",
    'p': "Le capital constant — machines, bâtiments, outils, matières "
         "premières — ne crée aucune valeur nouvelle et ne fait que "
         "transmettre sa valeur aux marchandises ; seul le capital variable "
         "en crée. En substituant le premier au second, le capitalisme "
         "réduit sa propre source de profit, ce qui explique crises, "
         "chômage, surproduction et tensions sociales."},
   {'n': "Thorstein Veblen",
    'i': "La hiérarchie se reproduit par imitation et conformisme, non par "
         "la lutte des classes.",
    'p': "La classe de loisir impose les normes du prestige ; les classes "
         "inférieures cherchent à copier les signes de richesse et "
         "consomment pour paraître, parfois au détriment de leurs besoins "
         "essentiels. Le cours souligne que cette reproduction par "
         "imitation entretient inégalités et gaspillage, et qu’elle diffère "
         "radicalement d’un mécanisme de conflit."},
   {'n': "Michel Crozier",
    'i': "Le conflit est la conséquence normale de l’interdépendance entre "
         "acteurs d’une même organisation.",
    'p': "Dans L’Acteur et le système (1977), écrit avec Erhard Friedberg, "
         "il montre que le pouvoir est relationnel et non attributif : il "
         "naît de la maîtrise d’une zone d’incertitude dont les autres "
         "dépendent, comme les ouvriers d’entretien du SEITA. Le conflit "
         "n’est donc ni pathologique ni nécessairement de classe."}],
  [{'f': "Marx formule le taux de profit comme PL/(C+V), puis le décompose "
         "en taux de plus-value PL/V et composition organique C/V.",
    'p': "Le rapport de classe devient une grandeur calculable : on peut "
         "distinguer l’intensité de l’exploitation du travail et le degré "
         "de mécanisation, et montrer que la seconde contrarie la première."},
   {'f': "Le Manifeste du Parti communiste est publié en 1848, fruit de la "
         "collaboration entre Marx et Friedrich Engels, fils d’un riche "
         "industriel qui finance ses recherches.",
    'p': "Le cours montre que l’analyse des rapports de classe est aussi un "
         "projet politique : le Manifeste vise à rassembler les "
         "travailleurs et à leur donner une lecture cohérente du "
         "capitalisme, ce qui est un fait d’histoire intellectuelle utile "
         "en dissertation."},
   {'f': "Marx écrit dans un contexte de Révolution industrielle marqué par "
         "l’essor du salariat, la mécanisation, l’urbanisation rapide et la "
         "paupérisation ouvrière, avec des crises, faillites, mauvaises "
         "récoltes et famines.",
    'p': "Le rapport de classe n’est pas une construction abstraite : il "
           "répond à une configuration historique précise, où le conflit "
           "central oppose désormais les capitalistes aux salariés et où "
           "apparaissent les premières organisations ouvrières."},
   {'f': "Veblen publie Théorie de la classe de loisir en 1899 et Théorie "
         "de l’entreprise d’affaires en 1904, dans un capitalisme "
         "industriel américain où la finance et les grandes entreprises "
         "prennent une place croissante.",
    'p': "Cela situe l’alternative à Marx dans un contexte différent : "
         "quand la finance s’autonomise, la domination se lit moins dans "
         "l’atelier que dans les modes de vie et dans l’opposition entre "
         "hommes d’affaires et ingénieurs."}],
  [{'q': "Le rapport entre groupes sociaux est-il de nature conflictuelle ?",
    'f': "Trois réponses coexistent dans le cours, et leur confrontation "
         "constitue le plan le plus solide. Chez Quesnay le rapport est "
         "fonctionnel : les trois classes sont indissociables et le circuit "
         "ne fonctionne que si chacune dépense. Chez Marx il est "
         "antagonique : la plus-value appropriée par le capitaliste est "
         "exactement ce qui n’est pas versé au travailleur, et "
         "l’exploitation est structurelle. Chez Veblen il est statutaire : "
         "la hiérarchie se maintient par imitation des normes de prestige, "
         "non par la lutte. La nature du rapport dépend donc du critère "
         "retenu pour définir les groupes.",
    'r': "Ce plan est rigoureux parce qu’il ne cherche pas à départager des "
         "auteurs mais à montrer que chacun répond à une question "
         "différente : comment circule le surplus, d’où vient le profit, "
         "pourquoi la hiérarchie est acceptée.",
    'ex': "La rente, revenu légitime chez Quesnay, forme d’appropriation de "
          "la plus-value chez Marx, et marque de la classe de loisir chez "
          "Veblen."},
   {'q': "Les contradictions internes du capitalisme le condamnent-elles ?",
    'f': "Le mécanisme est précis : la substitution du capital constant au "
         "capital variable élève la composition organique C/V alors que "
         "seul le travail crée de la valeur, ce qui entraîne une baisse "
         "tendancielle du taux de profit et explique crises, chômage, "
         "surproduction et tensions sociales. Mais le cours qualifie cette "
         "baisse de tendancielle, c’est-à-dire contrariable : "
         "l’intensification de l’exploitation, mesurée par PL/V, agit en "
         "sens inverse. La contradiction est donc réelle sans être "
         "mécaniquement fatale.",
    'r': "Ce raisonnement respecte la lettre du cours, qui écrit que même "
         "si l’exploitation s’intensifie elle ne compense pas "
         "l’augmentation du capital constant, formulation qui pose une "
         "tendance et non une échéance.",
    'ex': "La succession de crises que Marx décrit comme structurelles et "
          "cycliques, et non comme une crise finale unique."},
   {'q': "Exploitation ou imitation : comment se maintient une hiérarchie "
         "sociale ?",
    'f': "Les deux mécanismes se complètent plutôt qu’ils ne s’opposent. "
         "L’exploitation explique la formation du surplus et donc "
         "l’existence d’une classe qui vit du capital et de la rente. "
         "L’imitation explique la stabilité du résultat : les classes "
         "inférieures cherchent à copier les signes de richesse de la "
         "classe de loisir et consomment pour paraître, ce qui transforme "
         "la hiérarchie subie en hiérarchie désirée. Une hiérarchie "
         "durable a besoin des deux : un fondement matériel et une "
         "légitimation culturelle.",
    'r': "L’articulation est défendable parce que le cours lui-même "
         "présente les deux analyses côte à côte et compare leurs "
         "mécanismes sans en invalider aucune : Marx par l’exploitation et "
         "le conflit, Veblen par le statut, la culture et l’émulation.",
    'ex': "La consommation ostentatoire, instrument de distinction, de "
          "reconnaissance sociale et de domination symbolique."}],
  voisins=['n23-classes-sociales', 'n23-conscience-de-classe',
           'n23-reproduction-sociale', 'n23-polarisation-sociale',
           'n23-declassement'])

d('n23-conscience-de-classe', 23, "Conscience de classe",
  "Du groupe objectif au groupe qui se sait tel : formation et effacement",
  "La conscience de classe désigne le fait qu’un groupe partageant une même "
  "position économique se reconnaisse comme groupe et agisse comme tel. "
  "L’expression n’apparaît pas dans les cours, et ce point de vocabulaire "
  "doit être signalé ; mais la chose y est traitée deux fois, chez Marx — "
  "« les ouvriers prennent conscience de leur exploitation » — et dans le "
  "chapitre de sociologie, qui écrit que l’identité ouvrière repose "
  "largement sur le sentiment d’appartenir à une classe, puis décrit son "
  "effacement.",
  "Le cours fournit les deux moments de la question. Le premier est celui "
  "de la formation. Marx écrit dans un contexte de Révolution industrielle "
  "marqué par l’essor du salariat, la mécanisation, l’urbanisation rapide "
  "et la paupérisation ouvrière ; sur le plan social, le conflit central "
  "oppose désormais les capitalistes aux salariés, et le cours précise que "
  "les ouvriers prennent conscience de leur exploitation, tandis "
  "qu’apparaissent les premières organisations ouvrières et les "
  "revendications sociales. Le Manifeste du Parti communiste (1848) est "
  "présenté comme un texte à la fois théorique et politique, visant à "
  "rassembler les travailleurs et à leur donner une lecture cohérente du "
  "capitalisme : la conscience n’est donc pas un effet automatique de la "
  "position, elle se construit par un travail d’interprétation. Le second "
  "moment est celui de l’apogée puis de la décomposition, traité dans le "
  "chapitre de sociologie. Après 1945, le monde ouvrier connaît son apogée "
  "en France : nombreux, organisés syndicalement et politiquement, les "
  "ouvriers développent une forte identité collective fondée sur "
  "l’appartenance de classe, le Parti communiste français devenant un "
  "important porte-parole du monde ouvrier avec jusqu’à environ 25 % des "
  "voix aux élections. Le cours écrit explicitement que l’identité ouvrière "
  "repose alors largement sur le sentiment d’appartenir à une classe. Puis "
  "la figure se fragilise à partir des années 1970 : la crise contribue à "
  "la décomposition progressive de la figure ouvrière traditionnelle, "
  "l’effectif passe d’environ 8,263 millions en 1982 à 5,325 millions en "
  "2023 et la part dans la population active de 34,7 % à 18,6 %. Le cours "
  "insiste : la désindustrialisation ne fait pas disparaître le monde "
  "ouvrier, mais elle réduit son poids numérique et transforme profondément "
  "ses secteurs d’activité, ses qualifications et son identité collective. "
  "Trois autres mécanismes documentés dans le même chapitre convergent vers "
  "l’affaiblissement de l’appartenance collective : la désindustrialisation "
  "elle-même, l’individualisme combiné au paradoxe d’Olson, et la "
  "mondialisation — les trois causes de la crise du syndicalisme, dont le "
  "taux de syndicalisation tombe d’environ 30 % en 1949 à 10,3 % en 2019. "
  "Enfin, une alternative théorique existe : chez Veblen, les classes "
  "inférieures ne se reconnaissent pas comme classe opposée mais imitent "
  "les normes de prestige de la classe dominante, ce qui dissout la "
  "conscience collective dans l’aspiration individuelle au statut.",
  [("La position commune crée une expérience commune",
    "L’essor du salariat, la mécanisation, l’urbanisation rapide et la "
    "paupérisation ouvrière placent un grand nombre de travailleurs dans "
    "une situation identique : même rapport salarial, même instabilité, "
    "mêmes crises, faillites et famines."),
   ("L’expérience commune se traduit en interprétation partagée",
    "Le cours écrit que les ouvriers prennent conscience de leur "
    "exploitation. Le passage de la situation à la conscience suppose une "
    "lecture du monde : le Manifeste de 1848 vise précisément à donner aux "
    "travailleurs une lecture cohérente du capitalisme."),
   ("L’interprétation partagée s’institutionnalise",
    "Apparaissent les premières organisations ouvrières et les "
    "revendications sociales ; après 1945, les ouvriers sont organisés "
    "syndicalement et politiquement, le PCF réunissant jusqu’à environ "
    "25 % des voix comme porte-parole du monde ouvrier."),
   ("L’institution entretient le sentiment d’appartenance",
    "Le cours établit que l’identité ouvrière repose alors largement sur le "
    "sentiment d’appartenir à une classe. Syndicats et partis ne se "
    "contentent pas de représenter le groupe : ils en maintiennent la "
    "définition et la frontière."),
   ("La base matérielle se contracte",
    "La crise des années 1970 engage la décomposition de la figure ouvrière "
    "traditionnelle : la part des ouvriers passe de 34,7 % de la population "
    "active en 1982 à 18,6 % en 2023, et l’effectif d’environ 8,263 à 5,325 "
    "millions."),
   ("La contraction désagrège l’identité collective",
    "Les ouvriers travaillent davantage dans les services, leur "
    "qualification évolue, leur scolarisation augmente, l’ouvrier "
    "spécialisé non qualifié devient moins dominant : les situations se "
    "différencient et le groupe devient plus difficile à reconnaître de "
    "l’intérieur comme de l’extérieur."),
   ("Les relais collectifs s’affaiblissent à leur tour",
    "Le taux de syndicalisation recule d’environ 30 % en 1949 à 16,6 % en "
    "1980 puis 10,3 % en 2019 ; les trois causes avancées — "
    "désindustrialisation, individualisme et paradoxe d’Olson, "
    "mondialisation — jouent toutes contre l’appartenance collective.")],
  [{'a': "La conscience collective ne découle pas automatiquement de la "
         "position : elle exige un travail d’interprétation, ce que montre "
         "le statut du Manifeste de 1848, texte à la fois théorique et "
         "politique destiné à rassembler les travailleurs et à leur donner "
         "une lecture cohérente du capitalisme.",
    'cond': "Il faut que l’interprétation proposée rencontre l’expérience "
            "vécue : le cours situe le Manifeste dans un contexte où le "
            "conflit central oppose effectivement les capitalistes aux "
            "salariés et où les ouvriers prennent conscience de leur "
            "exploitation.",
    'lim': "Rien ne garantit la rencontre. Veblen décrit la configuration "
           "inverse, où les classes inférieures adoptent les normes de "
           "prestige de la classe dominante au lieu de se constituer contre "
           "elle : la même position économique peut produire l’émulation "
           "plutôt que l’opposition."},
   {'a': "Les institutions collectives sont le support de l’appartenance, "
         "et leur affaiblissement l’érode : le recul de la syndicalisation "
         "de 30 % en 1949 à 10,3 % en 2019 accompagne la décomposition de "
         "l’identité ouvrière.",
    'cond': "L’argument tient si les organisations jouent bien un rôle de "
            "définition du groupe et non de simple représentation, ce que "
            "suggère le cours en faisant du PCF un porte-parole capable de "
            "réunir environ 25 % des voix.",
    'lim': "La causalité est difficile à orienter : la désindustrialisation "
           "est donnée comme première cause du recul syndical, si bien que "
           "l’affaiblissement des institutions peut être l’effet autant que "
           "la cause de la désagrégation du groupe."},
   {'a': "L’individualisme et le paradoxe d’Olson expliquent la "
         "démobilisation sans invoquer un changement de position "
         "économique : chacun a intérêt à bénéficier des avantages obtenus "
         "collectivement sans supporter le coût de l’action, puisque "
         "l’avantage n’est pas réservé aux participants.",
    'cond': "Ce raisonnement suppose que les gains de l’action collective "
            "soient non excluables, comme le bien collectif qu’Olson prend "
            "pour modèle, et que les participants évaluent leur "
            "contribution à la marge.",
    'lim': "Le cours relève que les incitations sélectives, c’est-à-dire la "
           "solution qu’Olson propose à son propre paradoxe, ne sont pas "
           "développées dans ces chapitres : on dispose donc du mécanisme "
           "de démobilisation sans l’analyse des contre-mesures possibles."},
   {'a': "La conscience de classe peut se recomposer autour du sentiment de "
         "déclassement plutôt que de l’appartenance ouvrière : le cours "
         "montre que la faible progression des revenus des classes "
         "populaires des pays avancés nourrit un sentiment de déclassement "
         "aux conséquences politiques majeures.",
    'cond': "Il faut que ce sentiment se traduise en identification "
            "collective et en expression politique, ce que le cours "
            "constate : les populations se considérant comme perdantes "
            "peuvent soutenir des partis proposant droits de douane, "
            "relocalisation et préférence nationale.",
    'lim': "Cette recomposition n’est pas une conscience de classe au sens "
           "de Marx : elle s’organise autour d’un territoire et d’une "
           "nationalité autant que d’une position dans la production, ce "
           "que le cours appelle préférence nationale."}],
  [{'t': "Les classes inférieures ne se constituent pas en groupe opposé : "
         "elles imitent les normes de prestige de la classe dominante et "
         "consomment pour paraître, parfois au détriment de leurs besoins "
         "essentiels.",
    'qui': "Veblen, dont le cours oppose la lecture à celle de Marx : "
           "l’imitation et non la lutte.",
    'rep': "Les deux configurations peuvent se succéder historiquement. Le "
           "cours décrit une période d’apogée où l’identité ouvrière repose "
           "sur le sentiment d’appartenir à une classe, puis une "
           "décomposition. L’émulation statutaire décrite par Veblen éclaire "
           "mieux la seconde période que la première."},
   {'t': "L’appartenance de classe n’est plus pertinente : la "
         "désindustrialisation a réduit les ouvriers à 18,6 % de la "
         "population active et dispersé le groupe dans les services, avec "
         "des qualifications et des statuts très différents.",
    'qui': "Lecture qui s’appuie sur les données du cours sur la "
           "décomposition de la figure ouvrière traditionnelle.",
    'rep': "Le cours refuse explicitement cette conclusion : la "
           "désindustrialisation ne fait pas disparaître le monde ouvrier, "
           "elle réduit son poids numérique et transforme ses secteurs, ses "
           "qualifications et son identité collective. Ce n’est pas la "
           "disparition du groupe mais la transformation de ce qui le "
           "rassemble."},
   {'t': "La grille pertinente ne serait plus la classe mais la position "
         "dans la mondialisation : les gagnants et les perdants de "
         "l’ouverture ne se répartissent pas selon les classes mais selon "
         "les secteurs, les métiers et les territoires exposés.",
    'qui': "Lecture appuyée sur les chapitres de seconde année, qui "
           "montrent que les pertes sont concentrées sur certains "
           "individus et territoires alors que les gains sont diffus.",
    'rep': "Cette grille déplace la frontière sans supprimer la question de "
           "l’appartenance : le cours décrit bien un sentiment collectif, "
           "le sentiment de déclassement, et sa traduction politique. Ce "
           "qui change est le critère de rassemblement, pas la nécessité "
           "d’un tel critère."}],
  [{'n': "Karl Marx",
    'i': "Les ouvriers prennent conscience de leur exploitation, et "
         "l’histoire des sociétés est fondée sur la lutte des classes.",
    'p': "Le cours lie cette prise de conscience à un contexte précis — "
         "essor du salariat, mécanisation, urbanisation rapide, "
         "paupérisation ouvrière, crises et famines — et à un instrument, "
         "le Manifeste du Parti communiste (1848) écrit avec Friedrich "
         "Engels, qui vise à rassembler les travailleurs et à leur donner "
         "une lecture cohérente du capitalisme."},
   {'n': "Thorstein Veblen",
    'i': "Les classes inférieures imitent les signes de richesse de la "
         "classe de loisir au lieu de s’y opposer.",
    'p': "Pour lui la reproduction des hiérarchies passe par l’imitation "
         "sociale, la diffusion des normes de prestige et le conformisme. "
         "Le cours en tire une conclusion nette : ce n’est pas une lutte de "
         "classes mais une reproduction sociale par imitation, qui "
         "entretient inégalités et gaspillage. L’aspiration individuelle au "
         "statut se substitue à l’identification collective."},
   {'n': "Mancur Olson",
    'i': "Chacun a intérêt à bénéficier d’un avantage collectif sans "
         "supporter le coût de l’action qui l’a produit.",
    'p': "Dans The Logic of Collective Action (1965), il montre le "
         "comportement de passager clandestin. Le cours en fait l’une des "
         "trois causes de la crise du syndicalisme, aux côtés de la "
         "désindustrialisation et de la mondialisation : l’appartenance "
         "collective se heurte au calcul individuel, d’autant plus que les "
         "gains obtenus profitent aussi aux non-adhérents."},
   {'n': "Émile Durkheim",
    'i': "La conscience collective est l’ensemble des croyances et des "
         "sentiments communs à la moyenne des membres d’une même société.",
    'p': "Cette définition, donnée dans le cours à propos de la solidarité "
         "mécanique, fournit l’outil conceptuel pour penser un sentiment "
         "partagé d’appartenance. Durkheim l’associe aux sociétés "
         "segmentaires où les individus sont interchangeables, et montre "
         "qu’avec la division du travail la conscience individuelle gagne "
         "en autonomie, ce qui éclaire l’affaiblissement des appartenances "
         "collectives."}],
  [{'f': "Après 1945, les ouvriers connaissent leur apogée en France et le "
         "Parti communiste français, porte-parole du monde ouvrier, réunit "
         "jusqu’à environ 25 % des voix aux élections.",
    'p': "L’appartenance de classe se traduit alors en force électorale "
         "mesurable, ce qui montre qu’un sentiment collectif peut devenir "
         "un fait politique quantifiable et pas seulement une disposition "
         "subjective."},
   {'f': "La part des ouvriers dans la population active passe de 34,7 % en "
         "1982 à 18,6 % en 2023, l’effectif reculant d’environ 8,263 à "
         "5,325 millions.",
    'p': "La base matérielle de l’identité ouvrière se contracte de "
         "moitié en quarante ans, ce qui explique la décomposition de la "
         "figure ouvrière traditionnelle sans impliquer la disparition du "
         "groupe lui-même."},
   {'f': "Le taux de syndicalisation recule d’environ 30 % en 1949 à 20 % "
         "en 1969, 16,6 % en 1980 et 10,3 % en 2019, avec 18,4 % dans le "
         "public contre 7,8 % dans le privé.",
    'p': "Les relais collectifs qui entretenaient le sentiment "
         "d’appartenance s’affaiblissent très fortement, et l’écart entre "
         "public et privé montre que ce recul dépend des conditions "
         "concrètes d’organisation plus que d’un changement d’opinion."},
   {'f': "Le cours énonce que l’identité ouvrière repose largement sur le "
         "sentiment d’appartenir à une classe, et que la désindustrialisation "
         "transforme profondément cette identité collective.",
    'p': "C’est la formulation la plus proche de la notion de conscience de "
         "classe dans l’ensemble des chapitres : elle autorise à traiter la "
         "question, tout en imposant de signaler que le terme lui-même "
         "n’est pas employé."}],
  [{'q': "Suffit-il d’occuper une même position économique pour former un "
         "groupe social ?",
    'f': "La position commune est nécessaire mais non suffisante. Le cours "
         "montre que l’expérience partagée du salariat, de la mécanisation "
         "et de la paupérisation conduit les ouvriers à prendre conscience "
         "de leur exploitation, mais il montre aussi que cette conscience "
         "passe par un travail d’interprétation — le Manifeste de 1848 vise "
         "à donner aux travailleurs une lecture cohérente du capitalisme — "
         "et par des institutions, syndicats et partis, le PCF réunissant "
         "jusqu’à 25 % des voix. Sans interprétation ni institution, la "
         "position reste une situation statistique.",
    'r': "Le raisonnement est solide parce qu’il articule les trois niveaux "
         "que le cours fournit séparément : la situation matérielle, la "
         "lecture du monde, l’organisation. Il permet en outre d’expliquer "
         "symétriquement la décomposition quand ces niveaux se défont.",
    'ex': "Le recul de la syndicalisation de 30 % en 1949 à 10,3 % en 2019, "
          "qui affaiblit le troisième niveau."},
   {'q': "L’appartenance de classe a-t-elle disparu des sociétés "
         "contemporaines ?",
    'f': "Elle s’est transformée plutôt qu’effacée. Les ouvriers passent de "
         "34,7 % à 18,6 % de la population active entre 1982 et 2023, et le "
         "cours affirme que la désindustrialisation ne fait pas disparaître "
         "le monde ouvrier mais transforme ses secteurs, ses qualifications "
         "et son identité collective. En parallèle, un autre sentiment "
         "collectif se forme, le sentiment de déclassement des classes "
         "populaires des pays avancés, dont le cours montre les "
         "conséquences politiques majeures. Ce qui change est le principe "
         "de rassemblement, non le besoin d’en avoir un.",
    'r': "Ce plan évite à la fois la thèse de la fin des classes et celle "
         "de leur permanence, et il s’appuie sur deux séries du cours qui "
         "se répondent : la décomposition de la figure ouvrière d’un côté, "
         "la formation du sentiment de déclassement de l’autre.",
    'ex': "Le soutien, aux États-Unis, de certaines anciennes régions "
          "industrielles aux politiques protectionnistes."},
   {'q': "Pourquoi l’action collective ouvrière s’est-elle affaiblie ?",
    'f': "Le cours avance trois causes convergentes. La "
         "désindustrialisation réduit l’effectif et disperse le groupe dans "
         "les services. L’individualisme, combiné au paradoxe d’Olson, rend "
         "rationnel de bénéficier des avantages obtenus collectivement sans "
         "supporter le coût de l’adhésion. La mondialisation accroît la "
         "concurrence entre travailleurs de pays différents et affaiblit le "
         "pouvoir de négociation local. Le résultat est mesurable : la "
         "syndicalisation tombe de 30 % en 1949 à 10,3 % en 2019.",
    'r': "L’articulation est rigoureuse parce qu’elle combine une cause "
         "structurelle, une cause liée au calcul individuel et une cause "
         "externe, les trois étant explicitement données par le cours comme "
         "les causes de la crise du syndicalisme.",
    'ex': "L’écart entre 18,4 % de syndiqués dans le public et 7,8 % dans "
          "le privé, qui montre le poids des conditions d’organisation."}],
  voisins=['n23-classes-sociales', 'n23-rapports-de-classe',
           'n23-categories-socioprofessionnelles', 'n23-declassement',
           'n24-action-collective'])
