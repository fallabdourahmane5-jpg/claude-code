# -*- coding: utf-8 -*-
"""Ensemble 15 — L’État et les politiques économiques (3/5)."""

from doss_base import d

d('n15-stabilisateurs-automatiques', 15, "Stabilisateurs automatiques",
  "Le budget qui amortit le cycle sans qu’on décide rien",
  "Les stabilisateurs automatiques désignent la réaction spontanée du budget "
  "public à la conjoncture. Le cours en donne le mécanisme sans employer "
  "l’expression : lorsque la croissance est ralentie, les dépenses des "
  "administrations publiques augmentent, allocations chômage et prestations "
  "sociales, tandis que les recettes diminuent, la taxe sur la valeur ajoutée "
  "et les cotisations rentrant moins dans les caisses.",
  "Le cours décrit les stabilisateurs automatiques en les opposant à "
  "l’action volontariste, et cette opposition est précisément ce qui en "
  "constitue la notion. La description est détaillée. Lorsque la croissance "
  "économique est ralentie, les dépenses des administrations publiques "
  "augmentent, puisqu’il faut verser plus d’allocations chômage parce qu’il y "
  "a plus de chômeurs et plus de prestations sociales parce qu’il y a plus de "
  "pauvres ; et simultanément les recettes de l’État sont plus faibles, la "
  "consommation étant réduite ou ralentie la taxe sur la valeur ajoutée "
  "rentre moins dans les caisses, et les cotisations sur les revenus du "
  "travail sont également plus faibles puisqu’il y a plus de chômeurs. Les "
  "deux mouvements vont dans le même sens pour l’activité, ils soutiennent la "
  "demande, et dans le même sens pour le solde, ils creusent le déficit. Le "
  "cours marque ensuite la différence avec l’action discrétionnaire : l’État "
  "peut aussi être plus volontariste en mettant en œuvre des mesures "
  "spécifiques en termes de dépenses comme de recettes afin d’influer sur la "
  "conjoncture, et il renvoie alors au plan Biden. La formulation est "
  "décisive : le mot aussi indique que la première réaction s’est produite "
  "sans décision, et que la décision vient en supplément. Le mécanisme "
  "économique s’éclaire par le reste du cours. Il repose d’abord sur la "
  "structure de la redistribution, puisque le revenu disponible brut s’obtient "
  "en ajoutant les prestations sociales, allocations familiales, aides au "
  "logement, chômage et retraites, et en retirant les prélèvements "
  "obligatoires : ce sont ces deux flux qui réagissent. Il repose ensuite sur "
  "l’assiette des recettes, puisque la taxe sur la valeur ajoutée est assise "
  "sur la consommation et les cotisations sur les revenus du travail, deux "
  "grandeurs procycliques. Il s’appuie enfin sur l’analyse keynésienne, "
  "puisque soutenir le revenu des agents dont la propension à consommer est "
  "élevée est précisément ce qui évite le cercle vicieux dépressif décrit par "
  "Harrod, où la mévente entraîne des licenciements, donc une baisse des "
  "revenus, donc une nouvelle baisse de la consommation. Le cours justifie "
  "plus largement cette fonction par le rôle stabilisateur de l’État : même "
  "dans un cadre de rationalité néoclassique, les marchés ne s’auto-ajustent "
  "pas parfaitement et l’économie peut rester durablement en sous-emploi.",
  [("Le ralentissement de l’activité",
    "Le point de départ est conjoncturel : la croissance économique est "
    "ralentie, l’emploi se dégrade et les revenus d’activité progressent "
    "moins vite ou reculent."),
   ("La hausse spontanée des dépenses",
    "Il faut verser plus d’allocations chômage parce qu’il y a plus de "
    "chômeurs, et plus de prestations sociales parce qu’il y a plus de "
    "pauvres : la dépense suit le besoin sans décision nouvelle."),
   ("La baisse spontanée des recettes",
    "La consommation étant réduite ou ralentie, la taxe sur la valeur "
    "ajoutée rentre moins dans les caisses, et les cotisations sur les "
    "revenus du travail diminuent puisqu’il y a plus de chômeurs."),
   ("Le soutien du revenu disponible",
    "Les prestations compensent une partie de la perte de revenu primaire : "
    "le revenu disponible brut baisse moins que le revenu d’activité, ce qui "
    "amortit la chute de la consommation."),
   ("L’interruption du cercle vicieux",
    "Le soutien du revenu empêche l’enchaînement décrit par Harrod, mévente, "
    "licenciements, baisse des revenus, nouvelle baisse de la consommation : "
    "le cercle vicieux dépressif est freiné."),
   ("Le creusement du solde",
    "Les dépenses augmentent au moment où les recettes baissent : le déficit "
    "public se creuse mécaniquement, ce qui est le coût comptable de la "
    "stabilisation.")],
  [{'a': "Les stabilisateurs agissent sans délai de décision, ce qui leur "
         "donne une réactivité que la politique discrétionnaire n’a pas.",
    'cond': "L’automatisme suppose des prestations ouvertes selon des "
            "critères liés à la conjoncture, chômage et pauvreté, et des "
            "recettes assises sur l’activité.",
    'lim': "Leur ampleur n’est pas choisie : elle dépend de la générosité du "
           "système social existant, et non du besoin de stabilisation "
           "constaté."},
   {'a': "Ils soutiennent le revenu des ménages dont la propension à "
         "consommer est la plus élevée, ce qui maximise l’effet sur la "
         "demande.",
    'cond': "L’argument suppose que les bénéficiaires de prestations "
            "consomment une part élevée de leur revenu, les dépenses "
            "pré-engagées représentant déjà trente pour cent du revenu "
            "disponible.",
    'lim': "Le cours ne mesure pas directement ce différentiel de propension "
           "à consommer : l’argument reste déduit de la structure des "
           "dépenses contraintes."},
   {'a': "Ils interrompent le cercle vicieux dépressif qu’aucun mécanisme "
         "spontané de marché ne vient rompre de lui-même.",
    'cond': "L’argument suppose, comme chez Harrod, qu’il n’existe aucun "
            "mécanisme d’ajustement automatique vers le plein emploi.",
    'lim': "Les monétaristes contestent cette prémisse : pour eux l’État "
           "aggrave les cycles au lieu de les corriger."},
   {'a': "Ils évitent le débat politique sur chaque relance, puisque la "
         "réaction est inscrite dans la loi sociale et fiscale.",
    'cond': "L’argument suppose la stabilité des barèmes : une réforme "
            "restrictive des prestations réduit mécaniquement la capacité de "
            "stabilisation.",
    'lim': "Le cours montre que cette stabilité est précisément contestée, "
           "la crise de l’État providence portant sur le financement de ces "
           "prestations."},
   {'a': "Ils expliquent une part du déficit public sans qu’aucune décision "
         "de dépense n’ait été prise.",
    'cond': "L’explication suppose de distinguer la composante conjoncturelle "
            "du solde de sa composante structurelle.",
    'lim': "Le cours ne fait pas cette distinction explicitement : il "
           "constate seulement que dépenses et recettes évoluent en sens "
           "opposé lors d’un ralentissement."}],
  [{'t': "Les autorités publiques aggravent les cycles économiques au lieu de "
         "les corriger : l’État est la source du problème.",
    'qui': "Les monétaristes autour de Milton Friedman, dont le cours "
           "rapporte la critique du keynésianisme.",
    'rep': "Le cours répond que l’argument vise l’intervention "
           "discrétionnaire : les stabilisateurs agissent précisément sans "
           "décision, donc sans l’incertitude que cette critique reproche "
           "aux politiques conjoncturelles."},
   {'t': "Les prestations sociales créent de l’aléa moral : protégés, les "
         "agents adoptent des comportements plus risqués.",
    'qui': "L’analyse de l’aléa moral que le cours développe à partir des "
           "asymétries d’information.",
    'rep': "Le cours formule lui-même l’ambiguïté fondamentale : les "
           "dispositifs de protection sont nécessaires pour stabiliser "
           "l’économie, même s’ils créent de l’aléa moral, de sorte que la "
           "solution est en même temps une partie du problème."},
   {'t': "Le coût de ces dispositifs est devenu insoutenable : l’État "
         "providence connaît un problème de financement.",
    'qui': "Pierre Rosanvallon, dans La crise de l’État providence publiée "
           "en 1981.",
    'rep': "Le cours ne tranche pas mais relativise l’argument fiscal "
           "sous-jacent, en rapportant que la courbe de Laffer ne relève pas "
           "de faits empiriques selon certains économistes."},
   {'t': "La stabilisation automatique est illusoire : les agents anticipent "
         "le financement futur et épargnent les transferts reçus.",
    'qui': "L’argument issu des anticipations rationnelles que le cours "
           "rattache à Sargent.",
    'rep': "Le cours objecte avec Clower que les agents peuvent être "
           "rationnés : la demande d’un agent contraint n’exprime plus ses "
           "préférences mais son revenu effectif, que le transfert vient "
           "augmenter."}],
  [{'n': "Richard Musgrave",
    'i': "La stabilisation est l’une des trois fonctions de l’État "
         "providence, aux côtés de l’allocation et de la redistribution.",
    'p': "Le cours situe l’analyse dans la théorie des finances publiques de "
         "1959 : les stabilisateurs automatiques sont le point où les "
         "fonctions de redistribution et de stabilisation se confondent, "
         "puisque les mêmes prestations assurent les deux."},
   {'n': "John Maynard Keynes",
    'i': "L’emploi dépend de la demande globale, de sorte que soutenir le "
         "revenu soutient l’activité.",
    'p': "Le cours en tire que l’État doit intervenir face à l’instabilité "
         "du marché et peut créer une demande autonome : les stabilisateurs "
         "sont la version permanente et non discrétionnaire de cette "
         "intervention."},
   {'n': "Roy Harrod",
    'i': "Sans mécanisme d’ajustement, l’économie entre dans un cercle "
         "vicieux dépressif.",
    'p': "Le cours en détaille la chaîne : la demande globale devient "
         "insuffisante, les entreprises ne vendent pas toute leur "
         "production, elles licencient, les revenus des ménages diminuent et "
         "la consommation baisse encore davantage, ce que les prestations "
         "viennent freiner."}],
  [{'f': "Le cours décrit la hausse automatique des dépenses : plus "
         "d’allocations chômage parce qu’il y a plus de chômeurs, plus de "
         "prestations sociales parce qu’il y a plus de pauvres.",
    'p': "Le fait montre que la dépense suit le besoin par construction : la "
         "stabilisation résulte de la structure du système social et non "
         "d’une décision conjoncturelle."},
   {'f': "Le cours décrit la baisse simultanée des recettes : la taxe sur la "
         "valeur ajoutée rentre moins dans les caisses et les cotisations sur "
         "les revenus du travail diminuent.",
    'p': "Le fait montre que les deux côtés du budget réagissent, ce qui "
         "double l’effet stabilisateur mais explique aussi l’ampleur du "
         "creusement du déficit."},
   {'f': "Le cours emploie le mot aussi pour introduire l’action "
         "volontariste, en renvoyant au plan Biden.",
    'p': "La formulation marque que l’action discrétionnaire s’ajoute à une "
         "réaction déjà en cours : c’est l’indice textuel de la distinction "
         "entre les deux degrés."},
   {'f': "La taxe sur la valeur ajoutée rapporte deux cents milliards "
         "d’euros de recettes à l’État.",
    'p': "Le chiffre mesure l’ampleur de la recette la plus sensible à la "
         "conjoncture : c’est par elle que le ralentissement de la "
         "consommation se transmet le plus directement au solde public."}],
  [{'q': "Sujet sur l’amortissement des fluctuations",
    'f': "Une partie de la stabilisation conjoncturelle ne résulte d’aucune "
         "décision. Le cours en donne le mécanisme : lorsque la croissance "
         "économique est ralentie, les dépenses des administrations publiques "
         "augmentent, puisqu’il faut verser plus d’allocations chômage et "
         "plus de prestations sociales, tandis que les recettes de l’État "
         "sont plus faibles, la taxe sur la valeur ajoutée rentrant moins "
         "dans les caisses.",
    'r': "On montre que l’effet stabilisateur vient de l’assiette des "
         "prélèvements et des critères d’ouverture des prestations, c’est-à-"
         "dire de la structure du système et non de la politique menée.",
    'ex': "Le cercle vicieux dépressif décrit par Harrod, que le soutien du "
          "revenu vient freiner."},
   {'q': "Sujet sur les instruments de la politique conjoncturelle",
    'f': "La politique budgétaire comporte deux degrés d’action que le cours "
         "distingue par un seul mot. La réaction automatique du budget se "
         "produit d’abord ; puis, écrit le cours, l’État peut aussi être plus "
         "volontariste en mettant en œuvre des mesures spécifiques en termes "
         "de dépenses comme de recettes afin d’influer sur la conjoncture. "
         "L’automatisme précède donc la décision.",
    'r': "On montre que les deux degrés ont des propriétés inverses, l’un "
         "réactif mais non ciblé, l’autre ciblé mais retardé, ce qui plaide "
         "pour leur articulation.",
    'ex': "Le plan Biden de construction et de rénovation des "
          "infrastructures, exemple d’action volontariste du cours."},
   {'q': "Sujet sur la protection sociale et l’économie",
    'f': "La protection sociale remplit deux fonctions à la fois. Dans la "
         "grille de Musgrave, les prestations relèvent de la redistribution ; "
         "mais le cours montre qu’elles assurent simultanément la "
         "stabilisation, puisque leur hausse automatique en période de "
         "ralentissement soutient le revenu disponible et donc la "
         "consommation. Un même dispositif sert donc deux des trois "
         "fonctions de l’État providence.",
    'r': "On montre que la distinction fonctionnelle de Musgrave est "
         "analytique et non institutionnelle, un même instrument pouvant "
         "servir plusieurs fins.",
    'ex': "Le calcul du revenu disponible brut dans le cours, obtenu en "
          "ajoutant les prestations sociales aux revenus primaires."},
   {'q': "Sujet sur l’interprétation du déficit public",
    'f': "Une partie du déficit n’est pas choisie. Le cours montre qu’en "
         "ralentissement les dépenses augmentent et les recettes baissent "
         "simultanément, de sorte que le solde se dégrade sans qu’aucune "
         "décision de dépense ait été prise. Lire un déficit comme la seule "
         "marque d’une politique expansionniste est donc une erreur de "
         "diagnostic.",
    'r': "On distingue la composante conjoncturelle du solde, produite par "
         "la structure du budget, de sa composante décidée, ce qui change "
         "l’interprétation d’un même chiffre.",
    'ex': "La double réaction décrite par le cours, hausse des allocations "
          "chômage et baisse des recettes de taxe sur la valeur ajoutée."}],
  voisins=['n15-politique-relance', 'n15-deficit-public',
           'n15-fonctions-musgrave', 'n13-crises-demande'])


d('n15-effet-eviction', 15, "Effet d’éviction",
  "Quand la dépense publique prend la place du privé",
  "L’effet d’éviction désigne la situation où l’intervention publique "
  "déplace l’activité privée au lieu de l’ajouter. Le cours l’énonce dans le "
  "modèle de Barro : si les dépenses publiques sont excessives, il y a effet "
  "d’éviction du capital privé, et il existe donc un niveau optimal de "
  "capital public. Il en donne par ailleurs une version microéconomique, "
  "l’éviction d’entreprises locales par une firme multinationale.",
  "Le cours traite l’effet d’éviction à deux endroits très différents, et "
  "c’est leur comparaison qui en donne la portée générale. La première "
  "occurrence est macroéconomique et se trouve dans le modèle de croissance "
  "endogène de Robert Barro, daté de 1990. Le point de départ est favorable à "
  "l’intervention : le capital public correspond à l’ensemble des dépenses "
  "publiques productives qui améliorent la productivité du secteur privé, "
  "infrastructures comme les ponts, les routes et les transports, dépenses "
  "pour l’éducation, dépenses pour financer la recherche et le développement ; "
  "ces dépenses augmentent la productivité des entreprises privées, et "
  "l’originalité de Barro est de les intégrer explicitement dans la fonction "
  "de production, ce qui fait de l’État un facteur de croissance de long "
  "terme. Mais le cours ajoute aussitôt que cette intervention publique doit "
  "être mesurée, et énonce la condition d’efficacité : si les dépenses "
  "publiques sont trop faibles, il y a sous-investissement collectif ; si "
  "elles sont excessives, il y a effet d’éviction du capital privé ; il "
  "existe donc un niveau optimal de capital public, et la croissance dépend "
  "de la qualité des dépenses et de leur orientation vers des investissements "
  "productifs. L’effet d’éviction est ainsi présenté comme la borne "
  "supérieure d’une intervention par ailleurs légitime, et non comme un "
  "argument contre toute dépense publique. La seconde occurrence est "
  "microéconomique et se trouve dans le chapitre sur les acteurs de la "
  "mondialisation : les entreprises locales ne peuvent pas rivaliser avec une "
  "firme multinationale qui dispose d’économies d’échelle, de financement, de "
  "technologies, d’une marque et d’un réseau mondial, si bien que la "
  "concurrence augmentant, les entreprises locales fragiles disparaissent, et "
  "le cours parle alors d’effet d’éviction. Il en tire une conclusion "
  "nuancée : l’entrée d’une multinationale peut dynamiser le tissu productif "
  "local mais également évincer des entreprises domestiques incapables de "
  "soutenir la concurrence. Les deux usages partagent la même structure : un "
  "acteur disposant d’un avantage, ressources budgétaires ou avantages "
  "technologiques et financiers, se substitue à un acteur plus faible au lieu "
  "de s’y ajouter.",
  [("La mobilisation de ressources rares",
    "L’État ou la grande firme mobilise des ressources que les acteurs "
    "privés plus faibles auraient pu employer : capitaux, main-d’œuvre "
    "qualifiée, parts de marché."),
   ("L’avantage de position",
    "Le cours insiste sur l’asymétrie : la firme multinationale dispose "
    "d’économies d’échelle, de financement, de technologies, d’une marque et "
    "d’un réseau mondial que les entreprises locales n’ont pas."),
   ("La substitution au lieu de l’addition",
    "L’activité nouvelle ne s’ajoute pas à l’activité existante, elle la "
    "remplace : les entreprises locales fragiles disparaissent, ou le capital "
    "privé est évincé."),
   ("Le seuil au-delà duquel l’effet s’inverse",
    "Chez Barro, des dépenses publiques trop faibles produisent un sous-"
    "investissement collectif et des dépenses excessives un effet "
    "d’éviction : l’effet dépend du niveau atteint."),
   ("La dépendance à la qualité des dépenses",
    "Le cours précise que la croissance dépend de la qualité des dépenses et "
    "de leur orientation vers des investissements productifs : une même somme "
    "peut évincer ou entraîner."),
   ("L’ambivalence du résultat",
    "Le cours conclut que l’entrée d’une multinationale peut dynamiser le "
    "tissu productif local mais également évincer des entreprises "
    "domestiques : l’effet net n’est pas déterminé a priori.")],
  [{'a': "La notion impose de juger une dépense publique sur son effet net et "
         "non sur son montant affiché dans le budget.",
    'cond': "Le jugement suppose que l’on puisse distinguer l’activité "
            "ajoutée de l’activité déplacée, ce que la condition d’efficacité "
            "de Barro formule en termes de niveau.",
    'lim': "Le cours ne fournit pas de méthode pour estimer le niveau "
           "optimal de capital public : la borne est théorique avant d’être "
           "mesurable."},
   {'a': "Elle fournit une critique interne de l’intervention publique, "
         "formulée à l’intérieur d’un modèle qui la justifie.",
    'cond': "L’argument suppose que l’on accepte le point de départ de "
            "Barro, à savoir que les dépenses publiques productives entrent "
            "dans la fonction de production.",
    'lim': "La critique perd sa force si l’économie est en sous-emploi : la "
           "dépense publique mobilise alors des ressources inemployées plutôt "
           "que de les détourner."},
   {'a': "Elle se généralise au-delà du budget, comme le montre son emploi "
         "pour la concurrence entre firmes.",
    'cond': "La généralisation suppose la même structure : un acteur "
            "avantagé, des acteurs plus faibles, et une ressource disputée.",
    'lim': "Les deux cas diffèrent par le remède : on peut calibrer une "
           "dépense publique, on ne calibre pas l’entrée d’une firme "
           "multinationale."},
   {'a': "Elle éclaire le lien entre politique budgétaire et taux "
         "d’intérêt, puisque l’État emprunte sur le même marché que les "
         "entreprises.",
    'cond': "Le canal suppose que l’offre de financement soit limitée, de "
            "sorte que l’emprunt public renchérisse le crédit privé.",
    'lim': "Le cours montre que la création monétaire dépend largement du "
           "crédit bancaire : l’épargne disponible n’est pas une quantité "
           "fixe, ce qui atténue le mécanisme."},
   {'a': "Elle oblige à préciser l’orientation des dépenses plutôt qu’à "
         "arbitrer seulement leur volume.",
    'cond': "L’exigence suppose, comme le cours l’indique, que la croissance "
            "dépende de la qualité des dépenses et non seulement de leur "
            "quantité.",
    'lim': "La qualité est difficile à établir ex ante : le cours se borne à "
           "citer des catégories, infrastructures, éducation, recherche et "
           "développement."}],
  [{'t': "L’État est un facteur de croissance de long terme : le capital "
         "public augmente la productivité des entreprises privées.",
    'qui': "Robert Barro, dans le modèle de croissance endogène que le cours "
           "date de 1990.",
    'rep': "Le cours restitue la condition que Barro pose lui-même : "
           "l’intervention doit être mesurée, car des dépenses excessives "
           "produisent un effet d’éviction du capital privé."},
   {'t': "Il n’y a pas d’éviction en sous-emploi : la dépense publique "
         "mobilise des ressources qui seraient restées inemployées.",
    'qui': "L’analyse keynésienne de l’insuffisance de demande que le cours "
           "développe.",
    'rep': "Le cours accorde la force de cet argument dans son champ, mais "
           "maintient la borne de Barro pour une économie proche de ses "
           "capacités, où les ressources sont effectivement disputées."},
   {'t': "L’arrivée d’un acteur plus efficace est souhaitable même si elle "
         "évince les plus faibles : c’est le mécanisme de la destruction "
         "créatrice.",
    'qui': "L’analyse schumpétérienne de l’innovation que le cours expose.",
    'rep': "Le cours maintient l’ambivalence pour le cas des firmes "
           "multinationales : l’entrée peut dynamiser le tissu productif "
           "local mais aussi évincer des entreprises incapables de soutenir "
           "la concurrence, selon le pays, le secteur et la position dans la "
           "chaîne de valeur."},
   {'t': "Le vrai problème n’est pas l’éviction mais le sous-investissement "
         "collectif, plus fréquent que l’excès de dépense publique.",
    'qui': "Le versant inverse de la condition d’efficacité que le cours "
           "énonce chez Barro.",
    'rep': "Le cours tient les deux branches : des dépenses trop faibles "
           "produisent un sous-investissement collectif, des dépenses "
           "excessives une éviction, et il existe un niveau optimal entre les "
           "deux."}],
  [{'n': "Robert Barro",
    'i': "Au-delà d’un niveau optimal, les dépenses publiques évincent le "
         "capital privé.",
    'p': "Le cours énonce la condition d’efficacité complète : si les "
         "dépenses publiques sont trop faibles il y a sous-investissement "
         "collectif, si elles sont excessives il y a effet d’éviction du "
         "capital privé, et la croissance dépend de la qualité des dépenses "
         "et de leur orientation vers des investissements productifs."},
   {'n': "Robert Barro",
    'i': "Le capital public est l’ensemble des dépenses publiques productives "
         "qui améliorent la productivité du secteur privé.",
    'p': "Le cours en donne les exemples, infrastructures telles que ponts, "
         "routes et transports, éducation, financement de la recherche et du "
         "développement, et souligne son originalité : il intègre "
         "explicitement ces dépenses dans la fonction de production."},
   {'n': "Joseph Schumpeter",
    'i': "L’innovation détruit des positions établies en même temps qu’elle "
         "en crée de nouvelles.",
    'p': "Le cours fait de la destruction créatrice le mécanisme central de "
         "la dynamique capitaliste : appliquée à l’éviction, elle oblige à "
         "distinguer la disparition d’entreprises moins efficaces d’une perte "
         "nette pour l’économie."}],
  [{'f': "Le cours énonce la condition d’efficacité de Barro : dépenses trop "
         "faibles, sous-investissement collectif ; dépenses excessives, effet "
         "d’éviction du capital privé.",
    'p': "La double borne montre que l’effet d’éviction n’est pas un "
         "argument contre la dépense publique mais une limite supérieure à "
         "son niveau."},
   {'f': "Le cours cite comme capital public les infrastructures, ponts, "
         "routes et transports, l’éducation, et le financement de la "
         "recherche et du développement.",
    'p': "L’énumération montre que la qualité des dépenses est le critère "
         "retenu : ce sont des dépenses dont le rendement passe par la "
         "productivité privée."},
   {'f': "Le cours emploie l’expression effet d’éviction à propos des firmes "
         "multinationales, dont les avantages font disparaître les "
         "entreprises locales fragiles.",
    'p': "Le second usage montre la généralité de la structure : un acteur "
         "avantagé se substitue à un acteur plus faible sur une ressource "
         "disputée."},
   {'f': "Le cours énumère les avantages d’une firme multinationale : "
         "économies d’échelle, financement, technologies, marque, réseau "
         "mondial.",
    'p': "La liste identifie l’origine de l’asymétrie : l’éviction suppose "
         "un avantage structurel et non seulement une taille supérieure."}],
  [{'q': "Sujet sur les limites de l’intervention publique",
    'f': "L’argument le plus solide contre un excès de dépense publique est "
         "formulé à l’intérieur d’un modèle qui la justifie. Le cours expose "
         "la condition d’efficacité de Barro : si les dépenses publiques sont "
         "trop faibles il y a sous-investissement collectif, si elles sont "
         "excessives il y a effet d’éviction du capital privé, et il existe "
         "donc un niveau optimal de capital public.",
    'r': "On montre que la critique est quantitative et non principielle, ce "
         "qui déplace le débat du périmètre de l’État vers le calibrage de "
         "ses dépenses.",
    'ex': "Les exemples de capital public du cours : infrastructures, "
          "éducation, recherche et développement."},
   {'q': "Sujet sur l’État et la croissance",
    'f': "Le cours fait de l’État un facteur de croissance de long terme, "
         "sous condition. Avec Barro en 1990, le capital public correspond "
         "aux dépenses publiques productives qui améliorent la productivité "
         "du secteur privé, et son originalité est de les intégrer "
         "explicitement dans la fonction de production. Mais la croissance "
         "dépend de la qualité des dépenses et de leur orientation vers des "
         "investissements productifs.",
    'r': "On montre que l’effet d’une dépense dépend de sa nature avant son "
         "montant, ce qui explique qu’un même niveau de dépense publique "
         "puisse entraîner ou évincer.",
    'ex': "Le plan Biden de construction et de rénovation des "
          "infrastructures, exemple de dépense orientée vers le capital "
          "public."},
   {'q': "Sujet sur les effets de l’implantation des multinationales",
    'f': "L’effet d’éviction ne concerne pas seulement le budget. Le cours "
         "l’emploie pour les firmes multinationales : les entreprises locales "
         "ne peuvent pas rivaliser avec un groupe disposant d’économies "
         "d’échelle, de financement, de technologies, d’une marque et d’un "
         "réseau mondial, si bien que les entreprises locales fragiles "
         "disparaissent. Mais l’entrée peut aussi dynamiser le tissu "
         "productif local.",
    'r': "On montre que l’effet net dépend du pays, du secteur, du niveau de "
         "qualification et de la position dans la chaîne de valeur, ce qui "
         "interdit une conclusion générale.",
    'ex': "La conclusion du cours selon laquelle les effets de la "
          "mondialisation productive sont profondément ambivalents."},
   {'q': "Sujet sur l’efficacité d’une relance budgétaire",
    'f': "Juger une relance suppose de distinguer l’activité ajoutée de "
         "l’activité déplacée. L’effet d’éviction est l’objection la plus "
         "précise : au-delà d’un certain niveau, la dépense publique prend la "
         "place du capital privé au lieu de s’y ajouter. Mais l’objection "
         "suppose des ressources disputées, ce qui n’est pas le cas dans une "
         "économie en sous-emploi où des capacités restent inemployées.",
    'r': "On conditionne l’objection à l’état des capacités, ce qui permet "
         "de l’accepter sans renoncer à la relance en situation de "
         "sous-activité.",
    'ex': "La double borne de Barro, entre sous-investissement collectif et "
          "éviction du capital privé."}],
  voisins=['n15-politique-budgetaire', 'n15-multiplicateur-budgetaire',
           'n15-dette-publique', 'n15-fonctions-musgrave'])


d('n15-deficit-public', 15, "Déficit public",
  "Le solde négatif d’une année, et ce qu’il engage",
  "Le cours définit le déficit public comme le solde négatif entre recettes "
  "et dépenses des administrations publiques sur une année, et le distingue "
  "du déficit budgétaire, qui concerne spécifiquement l’administration "
  "centrale. Il en précise la conséquence : quand les dépenses publiques sont "
  "supérieures aux recettes publiques, l’État crée un déficit qui doit être "
  "financé par de la dette, c’est-à-dire par émission d’obligations.",
  "Le cours définit le déficit public avec soin, puis le relie à trois "
  "problèmes distincts, et c’est cette articulation qui en fait un dossier "
  "complet. La définition est précise : le déficit public est le solde "
  "négatif entre recettes et dépenses des administrations publiques sur une "
  "année. Le cours le distingue du déficit budgétaire, qui apparaît lorsque "
  "les recettes sont inférieures aux dépenses et concerne spécifiquement "
  "l’administration publique centrale, tandis que le déficit public couvre "
  "l’ensemble des administrations publiques, État, collectivités locales et "
  "sécurité sociale. Il le distingue enfin de la dette publique, qui est un "
  "stock cumulé de tous les emprunts, le déficit étant un flux annuel. Le "
  "premier problème est celui du financement : la dette publique sert à "
  "financer le déficit public, par émission d’obligations par l’État, et les "
  "intérêts constituent la charge de la dette qui pèse sur le budget. Le "
  "cours ajoute que lorsqu’on emprunte pour rembourser une dette, on roule la "
  "dette, c’est-à-dire qu’on repousse l’échéance. Le deuxième problème est "
  "celui de l’origine du déficit, et le cours distingue implicitement deux "
  "sources. L’une est automatique : lorsque la croissance est ralentie, les "
  "dépenses augmentent, allocations chômage et prestations sociales, et les "
  "recettes baissent, taxe sur la valeur ajoutée et cotisations. L’autre est "
  "volontaire : l’État peut être plus volontariste en mettant en œuvre des "
  "mesures spécifiques de dépenses et de recettes. Le troisième problème est "
  "extérieur, et le chapitre sur la mondialisation en donne l’identité "
  "comptable : le solde extérieur d’un pays correspond à la somme de la "
  "capacité de financement du secteur privé et du solde budgétaire public, de "
  "sorte qu’un déficit extérieur peut provenir d’un investissement supérieur "
  "à l’épargne privée ou d’un déficit public. Lorsque déficit public et "
  "déficit extérieur apparaissent simultanément, le cours parle de déficits "
  "jumeaux, et en donne la relation : déficit public en hausse, demande "
  "intérieure en hausse, importations en hausse, déficit courant en hausse. "
  "Le cours relie enfin le déficit au débat théorique, puisque pour "
  "Stephanie Kelton un État souverain monétairement peut financer sa dette "
  "sans contrainte financière, le seul risque étant l’inflation, alors que le "
  "cours rappelle de son côté le risque d’aléa moral public.",
  [("L’écart annuel entre recettes et dépenses",
    "Le déficit public est le solde négatif entre recettes et dépenses des "
    "administrations publiques sur une année : c’est un flux, à distinguer du "
    "stock de dette."),
   ("Le périmètre retenu",
    "Le cours distingue le déficit budgétaire, propre à l’administration "
    "centrale, et le déficit public, qui couvre toutes les administrations "
    "publiques, collectivités locales et sécurité sociale comprises."),
   ("La part conjoncturelle",
    "En ralentissement, les dépenses augmentent et les recettes baissent "
    "simultanément : une partie du déficit se forme sans qu’aucune décision "
    "de dépense soit prise."),
   ("La part décidée",
    "L’État peut être plus volontariste par des mesures spécifiques de "
    "dépenses et de recettes : cette part relève d’un choix de politique "
    "économique."),
   ("Le financement par émission",
    "La dette publique sert à financer le déficit public, par émission "
    "d’obligations par l’État : le déficit n’est soutenable que si des "
    "créanciers acceptent de le financer."),
   ("L’accumulation en stock",
    "Les déficits successifs s’additionnent en dette publique, et lorsqu’on "
    "emprunte pour rembourser une dette on roule la dette, c’est-à-dire "
    "qu’on repousse l’échéance."),
   ("La transmission à l’extérieur",
    "Un déficit public accroît la demande intérieure, donc les importations, "
    "donc le déficit courant : le cours nomme déficits jumeaux la coexistence "
    "des deux soldes négatifs.")],
  [{'a': "La distinction entre flux et stock évite de confondre déficit et "
         "dette, donc un problème annuel et un problème cumulé.",
    'cond': "La distinction suppose que l’on précise le périmètre et la "
            "période, ce que le cours fait en opposant déficit public et "
            "déficit budgétaire.",
    'lim': "Un déficit faible mais répété produit un stock élevé : la "
           "distinction clarifie la mesure sans séparer les deux problèmes."},
   {'a': "La part conjoncturelle du déficit justifie de ne pas le réduire "
         "mécaniquement en bas de cycle.",
    'cond': "L’argument suppose que les dépenses sociales et les recettes "
            "soient effectivement procycliques, ce que le cours décrit.",
    'lim': "Le cours ne distingue pas explicitement solde conjoncturel et "
           "solde structurel : la part décidée reste difficile à isoler des "
           "chiffres."},
   {'a': "L’identité comptable extérieure relie le déficit public au solde "
         "courant, ce qui élargit le diagnostic.",
    'cond': "L’identité suppose que l’on raisonne sur l’ensemble, somme de "
            "la capacité de financement du secteur privé et du solde "
            "budgétaire public.",
    'lim': "Le cours avertit qu’un déficit extérieur n’est pas "
           "automatiquement mauvais : l’identité relie les soldes sans "
           "indiquer lequel est en cause."},
   {'a': "La notion de déficits jumeaux fournit un mécanisme de transmission "
         "précis entre budget et balance courante.",
    'cond': "La relation suppose que la demande intérieure supplémentaire se "
            "porte en partie sur des importations, ce que le cours pose.",
    'lim': "Le cours montre que la même demande peut être satisfaite par la "
           "production nationale : la relation est tendancielle, non "
           "mécanique."},
   {'a': "Elle permet de poser le débat sur la contrainte de financement en "
         "termes vérifiables, par le coût de l’emprunt.",
    'cond': "Le débat suppose que l’État doive effectivement trouver des "
            "créanciers, ce que le cours établit avec l’émission "
            "d’obligations.",
    'lim': "Pour Stephanie Kelton, un État souverain monétairement n’a pas "
           "de contrainte financière : la prémisse même du débat est "
           "contestée."}],
  [{'t': "La dette publique n’est pas un problème en soi pour un État ayant "
         "sa propre monnaie : le seul risque réel est l’inflation.",
    'qui': "Stephanie Kelton, représentante de la théorie monétaire moderne "
           "que le cours présente.",
    'rep': "Le cours objecte par les incitations : l’aléa moral public fait "
           "que si l’État sait que la banque centrale peut financer ses "
           "dépenses, il n’a plus d’incitation à maîtriser le déficit ni à "
           "contrôler la dette."},
   {'t': "Le déficit doit être réduit en priorité, car la charge de la dette "
         "comprime les autres dépenses.",
    'qui': "L’argument de consolidation que le cours développe en chiffrant "
           "la charge de la dette française.",
    'rep': "Le cours décrit l’impasse de cette voie : pour compenser, il "
           "faudrait augmenter les impôts, mais les gens n’en veulent pas, et "
           "une hausse des prélèvements réduit elle-même la demande."},
   {'t': "Le déficit public est la cause du déficit extérieur : réduire l’un "
         "suffirait donc à corriger l’autre.",
    'qui': "La lecture par les déficits jumeaux que le cours expose.",
    'rep': "Le cours restitue l’identité complète : un déficit extérieur peut "
           "provenir soit d’un investissement supérieur à l’épargne privée, "
           "soit d’un déficit public, les deux composantes déterminant "
           "ensemble le besoin de financement."},
   {'t': "Un déficit n’a pas d’effet réel car les agents anticipent "
         "l’impôt futur et épargnent en conséquence.",
    'qui': "L’argument issu des anticipations rationnelles que le cours "
           "rattache à Sargent.",
    'rep': "Le cours objecte avec Clower que les agents peuvent être "
           "rationnés sur un marché : leur demande n’exprime plus leurs "
           "préférences mais leur revenu effectif, ce qu’une dépense publique "
           "vient desserrer."}],
  [{'n': "Stephanie Kelton",
    'i': "Un État souverain monétairement peut financer sa dette sans "
         "contrainte financière, le seul risque étant l’inflation.",
    'p': "Le cours la présente comme représentante de la théorie monétaire "
         "moderne et précise qu’elle conteste l’idée que la dette publique "
         "soit un problème en soi pour les États ayant leur propre monnaie, "
         "ce qui déplace le débat vers la seule question inflationniste."},
   {'n': "Richard Musgrave",
    'i': "Le budget public est l’instrument de trois fonctions distinctes, "
         "dont la stabilisation.",
    'p': "Le cours situe l’analyse dans la théorie des finances publiques de "
         "1959 : le déficit n’est pas un dérèglement mais la trace comptable "
         "de l’exercice simultané des fonctions d’allocation, de "
         "stabilisation et de redistribution."},
   {'n': "John Maynard Keynes",
    'i': "L’État peut recourir au déficit pour créer une demande autonome.",
    'p': "Le cours range le déficit parmi ses moyens d’action, aux côtés des "
         "dépenses publiques, de la politique de relance et du soutien à "
         "l’investissement : le solde négatif est l’instrument et non le "
         "symptôme."}],
  [{'f': "Le cours définit le déficit public comme le solde négatif entre "
         "recettes et dépenses des administrations publiques sur une année.",
    'p': "La définition fixe la nature de la grandeur : c’est un flux annuel, "
         "ce qui interdit de le confondre avec le stock de dette accumulé."},
   {'f': "Le cours distingue le déficit budgétaire, propre à l’administration "
         "centrale, du déficit public, qui couvre toutes les administrations "
         "publiques.",
    'p': "La distinction de périmètre montre que les chiffres cités dans le "
         "débat public ne portent pas toujours sur le même agrégat."},
   {'f': "Le cours énonce l’identité extérieure : le solde extérieur "
         "correspond à la somme de la capacité de financement du secteur "
         "privé et du solde budgétaire public.",
    'p': "L’identité relie mécaniquement le budget et la balance courante, "
         "ce qui explique la notion de déficits jumeaux."},
   {'f': "Le cours donne la relation des déficits jumeaux : déficit public en "
         "hausse, demande intérieure en hausse, importations en hausse, "
         "déficit courant en hausse.",
    'p': "La chaîne fournit le canal de transmission : le déficit public se "
         "transmet à l’extérieur par la demande d’importations qu’il "
         "engendre."}],
  [{'q': "Sujet sur l’interprétation des soldes publics",
    'f': "Un chiffre de déficit ne dit pas de quoi il est le signe. Le cours "
         "le définit comme le solde négatif entre recettes et dépenses des "
         "administrations publiques sur une année, mais montre qu’une partie "
         "se forme automatiquement : en ralentissement, les dépenses "
         "augmentent, allocations chômage et prestations sociales, tandis que "
         "les recettes baissent, taxe sur la valeur ajoutée et cotisations.",
    'r': "On distingue la composante conjoncturelle, produite par la "
         "structure du budget, de la composante décidée, ce qui change "
         "radicalement l’interprétation d’un même solde.",
    'ex': "La distinction du cours entre la réaction automatique du budget et "
          "l’action volontariste, illustrée par le plan Biden."},
   {'q': "Sujet sur le financement de l’État",
    'f': "Le déficit engage un financement, donc un créancier. Le cours "
         "l’énonce : quand les dépenses publiques sont supérieures aux "
         "recettes publiques, l’État crée un déficit public qui doit être "
         "financé par de la dette, c’est-à-dire par émission d’obligations "
         "par l’État ; et lorsqu’on emprunte pour rembourser une dette, on "
         "roule la dette, c’est-à-dire qu’on repousse l’échéance.",
    'r': "On montre que la contrainte n’est pas comptable mais contractuelle : "
         "elle dépend de la disposition des créanciers, donc des taux "
         "d’intérêt exigés.",
    'ex': "La dégradation de la note de la France relevée par le cours, les "
          "investisseurs demandant alors plus de rendement."},
   {'q': "Sujet sur déficit public et déséquilibres extérieurs",
    'f': "Le budget et la balance courante sont comptablement liés. Le cours "
         "donne l’identité : le solde extérieur d’un pays correspond à la "
         "somme de la capacité de financement du secteur privé et du solde "
         "budgétaire public, de sorte qu’un déficit extérieur peut provenir "
         "soit d’un investissement supérieur à l’épargne privée, soit d’un "
         "déficit public. Leur coexistence définit les déficits jumeaux.",
    'r': "On montre que l’identité contraint le raisonnement sans désigner la "
         "cause, ce qui oblige à examiner séparément l’épargne privée et le "
         "solde public.",
    'ex': "La relation du cours : déficit public en hausse, demande "
          "intérieure en hausse, importations en hausse, déficit courant en "
          "hausse."},
   {'q': "Sujet sur la contrainte budgétaire de l’État",
    'f': "La nature de la contrainte budgétaire est elle-même en débat. Pour "
         "Stephanie Kelton, un État souverain monétairement peut financer sa "
         "dette sans contrainte financière, le seul risque étant l’inflation. "
         "Le cours ne nie pas la possibilité technique mais objecte par les "
         "incitations : l’aléa moral public fait que l’État cesse de "
         "maîtriser son déficit s’il sait pouvoir compter sur la banque "
         "centrale.",
    'r': "On distingue la capacité technique à financer et la soutenabilité "
         "des incitations, pour montrer que la contrainte est "
         "institutionnelle plus que comptable.",
    'ex': "Le risque de dérive permanente que le cours associe au "
          "financement monétaire des dépenses publiques."}],
  voisins=['n15-dette-publique', 'n15-stabilisateurs-automatiques',
           'n15-politique-budgetaire', 'n15-soutenabilite-dette'])


d('n15-dette-publique', 15, "Dette publique",
  "Le stock accumulé des emprunts publics, et son coût",
  "Le cours définit la dette publique comme la somme de tous les emprunts "
  "réalisés par les administrations publiques, État, collectivités locales et "
  "sécurité sociale : c’est un stock accumulé au fil du temps, à distinguer "
  "du déficit qui est un flux annuel. En France, elle représente environ trois "
  "mille quatre cents milliards d’euros, soit environ cent quatorze pour cent "
  "du produit intérieur brut.",
  "Le cours traite la dette publique par sa définition, ses chiffres, son "
  "coût et ses distinctions, et c’est cette précision chiffrée qui en fait un "
  "dossier directement mobilisable. La définition est claire : la dette "
  "publique est la somme de tous les emprunts réalisés par les administrations "
  "publiques, c’est-à-dire un stock d’emprunts accumulés au fil du temps, "
  "alors que le déficit public est un solde annuel ; la dette publique sert "
  "précisément à financer le déficit public. Les chiffres sont donnés : "
  "environ trois mille quatre cents milliards d’euros en France, soit environ "
  "cent quatorze pour cent du produit intérieur brut. Le coût est détaillé "
  "par la charge de la dette, c’est-à-dire les intérêts, qui pèsent sur le "
  "budget de l’État : trente-neuf milliards d’euros en 2019, trente-six "
  "virgule quatre en 2021, cinquante-huit en 2024, et soixante-deux ou "
  "soixante-sept annoncés pour 2025. Le cours commente cette progression : la "
  "charge de la dette augmente fortement avec la hausse des taux d’intérêt. "
  "Il expose ensuite un enchaînement qu’il qualifie d’impasse. Réduire la "
  "dette publique permettrait de réduire la charge d’intérêts, qui représente "
  "environ deux pour cent du produit intérieur brut en 2024 ; mais les taux "
  "d’intérêt augmentent, car l’instabilité politique a dégradé la note de la "
  "France et les investisseurs demandent plus de rendement, ce qui accroît "
  "encore la charge de la dette ; et pour compenser il faudrait augmenter les "
  "impôts, mais les gens n’en veulent pas. Le cours introduit enfin plusieurs "
  "distinctions utiles. Il oppose un endettement sous contrainte, lorsque "
  "l’État emprunte pour financer ses dépenses nécessaires, et un endettement "
  "problématique, lorsque la dette devient trop élevée et difficile à "
  "rembourser. Il distingue la dette publique, qui concerne les "
  "administrations publiques, et la dette privée, qui concerne les entreprises "
  "et les ménages. Il distingue enfin dette intérieure, détenue par des "
  "créanciers du pays, et dette extérieure, la dette souveraine d’un État. Il "
  "précise que lorsqu’on emprunte pour rembourser une dette, on roule la "
  "dette, c’est-à-dire qu’on repousse l’échéance.",
  [("L’accumulation des déficits",
    "Chaque déficit annuel est financé par émission d’obligations : la dette "
    "publique est la somme de tous les emprunts réalisés par les "
    "administrations publiques, donc un stock cumulé."),
   ("La formation de la charge d’intérêts",
    "Les intérêts constituent la charge de la dette, qui pèse sur le budget "
    "de l’État : elle est une dépense obligatoire avant toute politique "
    "publique."),
   ("La sensibilité aux taux",
    "Le cours insiste : la charge de la dette augmente fortement avec la "
    "hausse des taux d’intérêt, puisque chaque refinancement se fait aux "
    "conditions du moment."),
   ("Le rôle du jugement des créanciers",
    "L’instabilité politique a dégradé la note de la France, les "
    "investisseurs demandant plus de rendement : le coût dépend d’une "
    "appréciation extérieure et non seulement des finances publiques."),
   ("Le roulement de la dette",
    "Lorsqu’on emprunte pour rembourser une dette, on roule la dette, "
    "c’est-à-dire qu’on repousse l’échéance : la dette n’est pas remboursée "
    "mais refinancée."),
   ("L’impasse des deux issues",
    "Réduire la charge exigerait de réduire la dette, donc d’augmenter les "
    "impôts, ce dont les gens ne veulent pas : le cours qualifie cette "
    "situation d’impasse.")],
  [{'a': "La distinction entre stock et flux évite de confondre dette et "
         "déficit, donc le cumul historique et le choix de l’année.",
    'cond': "La distinction suppose un périmètre fixe des administrations "
            "publiques, État, collectivités locales et sécurité sociale.",
    'lim': "Un déficit modéré mais répété produit un stock élevé : la "
           "distinction clarifie la mesure sans séparer les deux "
           "problèmes."},
   {'a': "La charge de la dette fournit un indicateur plus parlant que le "
         "stock, puisqu’elle mesure le coût annuel effectif.",
    'cond': "L’indicateur suppose de rapporter la charge à une grandeur de "
            "référence, ce que le cours fait en l’exprimant en pourcentage du "
            "produit intérieur brut.",
    'lim': "La charge dépend du calendrier de refinancement : un même stock "
           "peut coûter très différemment selon les taux des emprunts "
           "arrivant à échéance."},
   {'a': "La distinction entre endettement sous contrainte et endettement "
         "problématique déplace le jugement du niveau vers l’usage.",
    'cond': "Elle suppose de pouvoir qualifier les dépenses financées, le "
            "cours parlant de dépenses nécessaires dans le premier cas.",
    'lim': "Le cours ne fournit pas de critère pour trancher : la "
           "qualification de nécessaire relève d’un jugement politique autant "
           "qu’économique."},
   {'a': "La distinction entre dette intérieure et extérieure éclaire la "
         "vulnérabilité, puisque les créanciers n’ont pas les mêmes "
         "comportements.",
    'cond': "La distinction suppose d’identifier la résidence des "
            "créanciers, ce que le cours pose en définissant la dette "
            "intérieure comme détenue par des créanciers du pays.",
    'lim': "Le cours montre ailleurs que la globalisation financière "
           "brouille cette frontière : les titres circulent et changent de "
           "mains sur les marchés."},
   {'a': "La sensibilité aux taux explique pourquoi la soutenabilité peut se "
         "dégrader sans que la politique budgétaire ait changé.",
    'cond': "L’argument suppose une part significative de dette à "
            "refinancer, les conditions nouvelles s’appliquant aux emprunts "
            "arrivant à échéance.",
    'lim': "Le cours montre que la hausse des taux peut elle-même résulter "
           "d’un jugement sur l’État : la causalité va dans les deux sens."}],
  [{'t': "La dette publique n’est pas un problème en soi pour un État ayant "
         "sa propre monnaie : le seul risque réel est l’inflation.",
    'qui': "Stephanie Kelton, représentante de la théorie monétaire moderne "
           "que le cours présente.",
    'rep': "Le cours objecte par le coût observé : la charge de la dette "
           "française passe de trente-neuf milliards en 2019 à cinquante-huit "
           "en 2024, et les investisseurs demandent plus de rendement après "
           "une dégradation de la note."},
   {'t': "La dette publique doit d’abord être démocratisée : la question "
         "centrale est celle du contrôle de la monnaie et de la banque "
         "centrale.",
    'qui': "Éric Monnet, dans La Banque Providence publiée en 2021.",
    'rep': "Le cours tient les deux positions : il rapporte cet appel à "
           "démocratiser les banques centrales et la monnaie tout en "
           "maintenant qu’une banque centrale soumise au gouvernement n’est "
           "plus crédible pour lutter contre l’inflation."},
   {'t': "Le problème de la dette souveraine est devenu judiciaire plus que "
         "financier, comme le montrent les fonds vautours.",
    'qui': "Benjamin Lemoine, dont le cours expose l’analyse à propos du cas "
           "argentin.",
    'rep': "Le cours intègre cette dimension sans la substituer aux "
           "autres : la judiciarisation s’ajoute aux contraintes financières "
           "et politiques au lieu de les remplacer."},
   {'t': "L’endettement est un mode normal de financement : il permet de "
         "mobiliser immédiatement des ressources pour investir.",
    'qui': "L’analyse de l’endettement comme levier de développement que le "
           "cours expose.",
    'rep': "Le cours maintient la condition : ce n’est pas l’existence de la "
           "dette qui pose problème mais son caractère insoutenable, dès que "
           "le service de la dette devient trop lourd."}],
  [{'n': "Stephanie Kelton",
    'i': "Un État souverain monétairement peut financer sa dette sans "
         "contrainte financière, le seul risque étant l’inflation.",
    'p': "Le cours la présente comme représentante de la théorie monétaire "
         "moderne et précise qu’elle conteste l’idée que la dette publique "
         "soit un problème en soi pour les États ayant leur propre monnaie."},
   {'n': "Éric Monnet",
    'i': "La monnaie et les banques centrales devraient être soumises au "
         "débat démocratique.",
    'p': "Le cours cite La Banque Providence, publiée en 2021, parmi les "
         "analyses qui élargissent les missions des banques centrales : la "
         "question de la dette publique devient alors celle du partage des "
         "responsabilités entre État et autorité monétaire."},
   {'n': "Benjamin Lemoine",
    'i': "La dette souveraine est devenue un objet judiciaire autant que "
         "financier.",
    'p': "Le cours rattache son analyse au cas argentin et aux fonds "
         "vautours : la restructuration d’une dette publique ne dépend plus "
         "seulement d’une négociation économique mais aussi de décisions de "
         "justice."}],
  [{'f': "La dette publique française représente environ trois mille quatre "
         "cents milliards d’euros, soit environ cent quatorze pour cent du "
         "produit intérieur brut.",
    'p': "Les deux grandeurs sont nécessaires : le montant absolu mesure le "
         "stock, le rapport au produit intérieur brut mesure la capacité de "
         "l’économie à le porter."},
   {'f': "La charge de la dette passe de trente-neuf milliards d’euros en "
         "2019 à cinquante-huit en 2024, et soixante-deux ou soixante-sept "
         "annoncés pour 2025.",
    'p': "La progression montre l’effet de la hausse des taux : le coût "
         "annuel augmente alors que le stock ne progresse pas dans les mêmes "
         "proportions."},
   {'f': "La charge d’intérêts représente environ deux pour cent du produit "
         "intérieur brut en 2024.",
    'p': "Le ratio donne l’ordre de grandeur de la dépense contrainte : elle "
         "précède tout choix de politique publique dans le budget."},
   {'f': "Le cours relève que l’instabilité politique a dégradé la note de "
         "la France et que les investisseurs demandent plus de rendement.",
    'p': "Le fait montre que le coût de la dette dépend d’un jugement "
         "extérieur sur la capacité de l’État, et non seulement de ses "
         "comptes."}],
  [{'q': "Sujet sur le poids de la dette publique",
    'f': "La dette publique se juge par son coût annuel autant que par son "
         "stock. Le cours donne les deux : environ trois mille quatre cents "
         "milliards d’euros en France, soit environ cent quatorze pour cent "
         "du produit intérieur brut ; et une charge de la dette passant de "
         "trente-neuf milliards d’euros en 2019 à cinquante-huit en 2024, qui "
         "représente environ deux pour cent du produit intérieur brut.",
    'r': "On montre que le stock mesure l’engagement et la charge le coût "
         "effectif, ce qui explique qu’un même stock soit plus ou moins "
         "lourd selon les taux.",
    'ex': "Le commentaire du cours : la charge de la dette augmente "
          "fortement avec la hausse des taux d’intérêt."},
   {'q': "Sujet sur la soutenabilité des finances publiques",
    'f': "Le cours décrit une impasse plutôt qu’un simple arbitrage. Réduire "
         "la dette publique permettrait de réduire la charge d’intérêts ; "
         "mais les taux augmentent parce que l’instabilité politique a "
         "dégradé la note de la France et que les investisseurs demandent "
         "plus de rendement, ce qui accroît encore la charge ; et pour "
         "compenser il faudrait augmenter les impôts, mais les gens n’en "
         "veulent pas.",
    'r': "On montre que les deux issues, moins de dépenses ou plus d’impôts, "
         "se heurtent chacune à une contrainte, l’une de marché et l’autre "
         "politique.",
    'ex': "Le mot impasse employé par le cours pour qualifier cette "
          "situation."},
   {'q': "Sujet sur la nature de la contrainte d’endettement",
    'f': "Le cours distingue deux formes d’endettement selon leur usage : un "
         "endettement sous contrainte, lorsque l’État emprunte pour financer "
         "ses dépenses nécessaires, et un endettement problématique, lorsque "
         "la dette devient trop élevée et difficile à rembourser. Le critère "
         "n’est donc pas le niveau mais la capacité à faire face, ce que le "
         "cours formule ailleurs par la soutenabilité.",
    'r': "On déplace le jugement du montant vers l’usage et la capacité de "
         "remboursement, ce qui évite de fixer un seuil arbitraire.",
    'ex': "La définition du cours selon laquelle ce n’est pas l’existence de "
          "la dette qui pose problème, mais son caractère insoutenable."},
   {'q': "Sujet sur la dette publique et la souveraineté",
    'f': "La dette publique engage la souveraineté de plusieurs manières. Le "
         "cours distingue dette intérieure, détenue par des créanciers du "
         "pays, et dette extérieure, dette souveraine d’un État. Il y ajoute "
         "avec Benjamin Lemoine la judiciarisation de la dette souveraine et "
         "le rôle des fonds vautours, et avec Stephanie Kelton l’argument "
         "selon lequel un État souverain monétairement ne connaît d’autre "
         "risque que l’inflation.",
    'r': "On montre que la contrainte varie selon la monnaie d’émission et "
         "la résidence des créanciers, ce qui interdit de traiter toutes les "
         "dettes publiques de la même manière.",
    'ex': "Le cas argentin et les fonds vautours, que le cours mobilise avec "
          "Benjamin Lemoine."}],
  voisins=['n15-deficit-public', 'n15-soutenabilite-dette',
           'n15-politique-rigueur', 'n15-contrainte-exterieure'])
