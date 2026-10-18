# -*- coding: utf-8 -*-
"""Ensemble 1 — La croissance économique et ses moteurs (3/3, première partie)."""

from doss_base import d

d('n1-endogene', 1, "Croissance endogène",
  "La croissance comme résultat de décisions économiques, non comme donnée extérieure",
  "Les théories de la croissance endogène, développées à partir des années "
  "1980, expliquent le progrès technique au lieu de le supposer. Elles "
  "soutiennent que la croissance résulte de l’accumulation de capitaux "
  "particuliers — connaissances, capital humain, capital public — dont les "
  "rendements ne sont pas décroissants, parce qu’ils engendrent des "
  "externalités. La croissance devient alors auto-entretenue et sensible aux "
  "politiques publiques.",
  "Le point de départ de ces théories est une insatisfaction précise à l’égard "
  "du modèle de Solow : celui-ci conclut que la croissance de long terme dépend "
  "entièrement du progrès technique, tout en traitant ce dernier comme une "
  "donnée extérieure. La croissance devient ainsi inexplicable et la politique "
  "économique impuissante. Les modèles endogènes lèvent la difficulté en "
  "identifiant des formes de capital échappant aux rendements décroissants. "
  "Romer met au centre la recherche et développement et les idées : une "
  "connaissance peut être utilisée par plusieurs agents simultanément sans se "
  "détruire, ce qui rend son rendement collectif supérieur à son rendement "
  "privé. Lucas met au centre le capital humain : la formation d’un individu "
  "élève sa propre productivité et celle de ceux qui travaillent avec lui. "
  "Barro met au centre le capital public : infrastructures et équipements "
  "collectifs élèvent la productivité de tout le capital privé. Dans les trois "
  "cas, le mécanisme est le même et c’est lui qu’il faut exposer : "
  "l’accumulation produit des externalités positives, donc le rendement social "
  "excède le rendement privé, donc l’agent privé sous-investit, donc "
  "l’intervention publique est fondée. La conclusion de politique économique "
  "est inverse de celle de Solow : les dépenses d’éducation, de recherche et "
  "d’infrastructures ne sont pas des charges mais les déterminants du taux de "
  "croissance de long terme.",
  [("L’identification d’un capital à rendements non décroissants",
    "Connaissances, qualifications ou infrastructures présentent la propriété "
    "d’être non rivales ou de produire des effets au-delà de leur détenteur. "
    "Leur accumulation ne se heurte donc pas à la décroissance qui bloque le "
    "capital physique ordinaire."),
   ("L’externalité et l’écart entre rendement privé et rendement social",
    "Celui qui finance l’accumulation ne capte qu’une partie du bénéfice : le "
    "reste profite aux autres agents. Le rendement social excède donc le "
    "rendement privé, ce qui est la définition même d’une externalité positive."),
   ("Le sous-investissement privé",
    "Puisque l’agent privé ne perçoit que le rendement privé, il investit moins "
    "que ne le voudrait l’optimum collectif. La défaillance n’est pas un défaut "
    "de rationalité mais sa conséquence."),
   ("La justification de l’intervention publique",
    "Financement de la recherche, de l’éducation et des infrastructures, "
    "protection de la propriété intellectuelle : l’État comble l’écart entre "
    "les deux rendements, et agit donc directement sur le taux de croissance de "
    "long terme."),
   ("Le caractère auto-entretenu de la croissance",
    "Le stock accumulé élève la productivité, donc le revenu, donc la capacité "
    "à accumuler davantage. La croissance ne converge plus vers un état "
    "stationnaire : elle se nourrit d’elle-même.")],
  [{'a': "La croissance endogène explique les écarts durables de croissance "
         "entre pays, que la convergence prédite par Solow ne permettait pas de "
         "comprendre.",
    'cond': "Il faut que les externalités soient effectives, donc que les "
            "connaissances et les qualifications circulent réellement au sein "
            "de l’économie considérée.",
    'lim': "La contrepartie est inquiétante : sans convergence automatique, un "
           "retard initial peut se creuser indéfiniment, les pays les mieux "
           "dotés accumulant plus vite."},
   {'a': "Elle fonde théoriquement les politiques d’éducation, de recherche et "
         "d’infrastructures en en faisant des déterminants de la croissance et "
         "non des dépenses de confort.",
    'cond': "L’efficacité suppose que la dépense publique soit effectivement "
            "productive et non captée, ce qui renvoie à la qualité des "
            "institutions.",
    'lim': "Rien ne garantit qu’une dépense publique accrue produise les "
           "externalités attendues : le mécanisme indique une direction, pas un "
           "rendement."},
   {'a': "Elle réconcilie la croissance et l’intervention publique, en montrant "
         "que celle-ci peut corriger une défaillance de marché plutôt que la "
         "créer.",
    'cond': "La correction doit être calibrée sur l’écart entre rendement social "
            "et rendement privé, ce qui exige une évaluation difficile.",
    'lim': "Le même raisonnement, mal appliqué, justifie n’importe quelle "
           "dépense : l’externalité est un argument puissant et facilement "
           "abusif."}],
  [{'t': "Les théories endogènes supposent des externalités dont l’ampleur est "
         "difficile à établir empiriquement, ce qui fragilise les conclusions de "
         "politique économique qu’on en tire.",
    'qui': "Objection méthodologique classique adressée à ces modèles.",
    'rep': "La difficulté est réelle, mais l’existence d’externalités de "
           "connaissance est l’un des faits les mieux établis de l’économie de "
           "l’innovation : c’est leur mesure, non leur existence, qui est "
           "incertaine."},
   {'t': "En supprimant la convergence automatique, ces théories prédisent une "
         "divergence durable entre économies, ce qui contredit le rattrapage "
         "observé de plusieurs pays asiatiques.",
    'qui': "Objection empirique tirée des trajectoires de rattrapage.",
    'rep': "Les deux lectures se complètent : la convergence conditionnelle de "
           "Solow explique le rattrapage des pays qui adoptent les mêmes "
           "paramètres structurels, la croissance endogène explique pourquoi "
           "les autres décrochent."},
   {'t': "Si la croissance dépend de l’accumulation de connaissances, le "
         "ralentissement contemporain devient difficile à expliquer alors même "
         "que l’effort de recherche n’a jamais été aussi élevé.",
    'qui': "Objection tirée du diagnostic de Robert Gordon sur l’efficacité "
           "décroissante des innovations récentes.",
    'rep': "L’objection est forte : elle suggère que le rendement de la "
           "recherche n’est pas constant et que l’accumulation de connaissances "
           "pourrait elle-même rencontrer des rendements décroissants."}],
  [{'n': "Paul Romer",
    'i': "La recherche et développement et les idées constituent des moteurs "
         "internes de la croissance, car les connaissances se cumulent sans se "
         "détruire.",
    'p': "Une idée peut être utilisée simultanément par plusieurs agents : son "
         "rendement collectif excède donc son rendement privé, ce qui explique "
         "à la fois le sous-investissement privé et la possibilité d’une "
         "croissance durable."},
   {'n': "Robert Lucas",
    'i': "Le capital humain est un moteur endogène de la croissance : "
         "l’éducation élève la productivité de celui qui la reçoit et de ceux "
         "qui l’entourent.",
    'p': "L’externalité est ici interindividuelle : travailler avec des "
         "personnes qualifiées rend plus productif. La croissance peut donc "
         "être cumulative et auto-entretenue, ce qui justifie une intervention "
         "structurelle de l’État dans l’éducation et la formation."},
   {'n': "Robert Barro",
    'i': "Le capital public et les infrastructures sont des moteurs endogènes "
         "de la croissance, parce qu’ils élèvent la productivité du capital "
         "privé.",
    'p': "Contrairement à Solow, Barro montre que la croissance peut être "
         "cumulative et auto-entretenue, qu’elle repose sur l’accumulation d’un "
         "capital spécifique, et que les rendements de ce capital ne sont pas "
         "nécessairement décroissants."},
   {'n': "Philippe Aghion",
    'i': "La croissance par destruction créatrice dépend du niveau de recherche "
         "et développement et de l’intensité de la concurrence.",
    'p': "L’innovation est financée par la perspective d’une rente temporaire, "
         "que l’innovation suivante détruit. Le rythme de la croissance devient "
         "donc sensible à la politique de concurrence et au financement de la "
         "recherche."}],
  [{'f': "Les théories de la croissance endogène naissent dans les années 1980 "
         "en expliquant le progrès technique par l’innovation, la recherche et "
         "développement et le capital humain.",
    'p': "La datation permet de présenter ces théories comme une réponse à une "
         "insuffisance identifiée du modèle de Solow, et non comme une école "
         "concurrente parmi d’autres."},
   {'f': "Lucas publie son modèle de croissance fondé sur le capital humain en "
         "1988, Barro son modèle fondé sur le capital public en 1990.",
    'p': "Les deux dates encadrent le moment où la croissance cesse d’être "
         "traitée comme une donnée pour devenir un objet de politique "
         "économique."},
   {'f': "Comme Lucas et Romer, Barro montre que la croissance peut être "
         "auto-entretenue et qu’elle repose sur l’accumulation d’un capital "
         "spécifique aux rendements non décroissants.",
    'p': "La convergence des trois modèles sur un même mécanisme — externalité, "
         "rendements non décroissants, rôle de l’État — est ce qui en fait une "
         "famille théorique cohérente."}],
  [{'q': "Sujet du type « La croissance peut-elle s’entretenir elle-même ? »",
    'f': "Les théories de la croissance endogène répondent affirmativement, à "
         "une condition précise : qu’il existe des capitaux dont les rendements "
         "ne soient pas décroissants. Connaissances chez Romer, capital humain "
         "chez Lucas, capital public chez Barro partagent la propriété de "
         "produire des externalités, de sorte que leur accumulation élève la "
         "productivité de l’ensemble de l’économie et non du seul investisseur.",
    'r': "On isole l’hypothèse technique qui fait toute la différence — la "
         "nature des rendements — ce qui permet d’opposer rigoureusement Solow "
         "et les modèles endogènes au lieu de les juxtaposer.",
    'ex': "Le modèle de Lucas (1988) sur le capital humain et celui de Barro "
          "(1990) sur le capital public, qui aboutissent au même résultat par "
          "deux canaux distincts."},
   {'q': "Sujet du type « Les institutions sont-elles la cause fondamentale de "
         "la prospérité ? »",
    'f': "Les théories endogènes fournissent le chaînon manquant entre "
         "institutions et croissance : si la croissance dépend d’externalités "
         "que les agents privés ne captent pas, alors la capacité d’une société "
         "à financer collectivement la recherche, l’éducation et les "
         "infrastructures devient déterminante — et cette capacité est une "
         "propriété institutionnelle.",
    'r': "On relie le mécanisme économique au cadre institutionnel, ce qui "
         "permet d’articuler Romer, Lucas et Barro avec North et Acemoglu dans "
         "un même raisonnement.",
    'ex': "La correction publique de l’écart entre rendement privé et rendement "
          "social de la recherche, qui suppose un État capable de prélever et de "
          "dépenser efficacement."}],
  voisins=['n1-progres-technique', 'n1-capital-humain', 'n1-rd',
           'n1-infrastructures', 'n1-institutions', 'n1-accumulation'])

d('n1-capital-humain', 1, "Capital humain",
  "Les qualifications comme stock productif accumulable",
  "Le capital humain désigne l’ensemble des caractéristiques productives "
  "incorporées dans les individus : qualifications, savoir-faire, expérience, "
  "santé. Gary Becker en donne la définition canonique comme stock de "
  "caractéristiques productives, ce qui autorise à traiter la formation comme "
  "un investissement : elle a un coût présent, une durée de vie et un "
  "rendement, mesurable par le supplément de revenu qu’elle procure.",
  "Le concept de capital humain opère un déplacement décisif : il fait de "
  "l’éducation un acte économique, susceptible d’être analysé avec les outils "
  "de l’investissement. L’individu compare le coût de la formation — dépenses "
  "directes et revenus auxquels il renonce pendant ses études — au supplément "
  "de rémunération qu’il en attend. Cette lecture explique des régularités "
  "observées : on se forme plutôt jeune, puisque la durée d’amortissement est "
  "plus longue ; on se forme davantage lorsque l’écart de salaire entre "
  "qualifications est important. Mais le concept prend toute sa portée "
  "macroéconomique avec Lucas, qui identifie une externalité : la "
  "qualification d’un individu élève non seulement sa propre productivité mais "
  "aussi celle de ceux qui travaillent avec lui. Cette externalité change "
  "tout. Elle implique d’abord que le rendement social de l’éducation excède "
  "son rendement privé, donc que l’individu laissé à lui-même se forme moins "
  "que l’optimum collectif ne le voudrait — ce qui justifie un financement "
  "public. Elle implique ensuite que l’accumulation de capital humain échappe "
  "aux rendements décroissants, donc qu’elle peut soutenir une croissance "
  "durable. Le capital humain est ainsi le pont le plus solide entre la "
  "microéconomie de la décision individuelle et la macroéconomie de la "
  "croissance de long terme.",
  [("La décision individuelle d’investissement",
    "L’individu compare le coût de la formation, y compris le revenu auquel il "
    "renonce, au supplément de rémunération attendu sur sa carrière. La "
    "formation est donc un investissement au sens strict, avec un rendement "
    "actualisable."),
   ("L’effet sur la productivité individuelle",
    "Un travailleur plus qualifié produit davantage ou mieux à poste donné, ce "
    "qui justifie un salaire plus élevé et explique le rendement privé de "
    "l’éducation."),
   ("L’externalité interindividuelle",
    "La présence de travailleurs qualifiés élève la productivité de leurs "
    "collègues, par imitation, transmission et division du travail plus fine. "
    "Le bénéfice dépasse donc celui qui a financé la formation."),
   ("Le sous-investissement privé et la réponse publique",
    "L’individu n’intégrant que son rendement privé, il se forme moins que "
    "l’optimum social. Le financement public de l’éducation comble cet écart, "
    "ce qui en fait une politique de croissance et non de redistribution seule."),
   ("L’accumulation à rendements non décroissants",
    "Le stock de capital humain élève la capacité à en accumuler davantage : une "
    "population plus éduquée forme mieux la génération suivante, ce qui rend le "
    "processus cumulatif.")],
  [{'a': "L’investissement en capital humain soutient une croissance durable, "
         "puisqu’il échappe aux rendements décroissants qui bornent "
         "l’accumulation de capital physique.",
    'cond': "L’externalité doit être effective : il faut que les qualifications "
            "circulent dans l’économie, donc une mobilité professionnelle et "
            "des organisations de travail qui permettent la transmission.",
    'lim': "Un diplôme n’est pas automatiquement productif : si les "
           "qualifications acquises ne correspondent pas aux besoins, le "
           "rendement privé comme social reste faible."},
   {'a': "Il réduit les inégalités en élevant la productivité des moins "
         "qualifiés, et conditionne la mobilité sociale.",
    'cond': "L’accès à la formation doit être effectivement ouvert, ce qui "
            "suppose un financement collectif et la neutralisation des "
            "obstacles sociaux.",
    'lim': "Si l’accès reste socialement déterminé, l’investissement éducatif "
           "reproduit les inégalités au lieu de les corriger, ce qui en fait un "
           "instrument ambivalent."},
   {'a': "Il améliore la capacité d’absorption technologique : une population "
         "qualifiée adopte et adapte plus vite les techniques étrangères.",
    'cond': "L’argument suppose un accès aux technologies et un tissu "
            "productif capable de les mettre en œuvre.",
    'lim': "La capacité d’absorption ne suffit pas à produire l’innovation "
           "elle-même : elle permet le rattrapage, pas nécessairement le "
           "passage à la frontière technologique."}],
  [{'t': "Le diplôme peut jouer un rôle de signal plutôt que de capital : il "
         "révélerait une aptitude préexistante sans l’accroître réellement.",
    'qui': "Objection classique à la théorie du capital humain, qui oppose "
           "l’effet de signalement à l’effet de formation.",
    'rep': "Les deux effets coexistent probablement. L’objection invite à "
           "évaluer les contenus de formation plutôt qu’à renoncer au concept, "
           "car même un signal a une valeur d’appariement sur le marché du "
           "travail."},
   {'t': "Traiter l’éducation comme un investissement réduit à un calcul de "
         "rendement une activité qui a d’autres finalités, culturelles et "
         "civiques.",
    'qui': "Objection sur la portée du concept plutôt que sur sa validité "
           "interne.",
    'rep': "Elle est légitime mais ne contredit pas l’analyse : constater que "
           "l’éducation a un rendement économique n’implique pas qu’elle n’ait "
           "que celui-là."},
   {'t': "Le rendement de l’éducation dépend de la structure de la demande de "
         "travail : accroître l’offre de diplômés sans débouchés produit du "
         "déclassement plutôt que de la croissance.",
    'qui': "Objection tirée de l’analyse du marché du travail et du "
           "déclassement.",
    'rep': "L’objection est forte et impose d’articuler politique éducative et "
           "politique industrielle : l’offre de qualifications ne crée pas à "
           "elle seule les emplois correspondants."}],
  [{'n': "Gary Becker",
    'i': "Le capital humain est un stock de caractéristiques productives "
         "incorporées dans les individus, accumulable par l’investissement.",
    'p': "La définition permet d’appliquer à l’éducation et à la formation la "
         "logique de l’investissement : coût présent, durée d’amortissement, "
         "rendement mesurable par le supplément de revenu obtenu."},
   {'n': "Robert Lucas",
    'i': "Le capital humain est un moteur endogène de la croissance, parce que "
         "la qualification produit des externalités positives.",
    'p': "La présence de travailleurs qualifiés élève la productivité de leur "
         "environnement : le rendement social de l’éducation excède donc son "
         "rendement privé, ce qui justifie une intervention structurelle de "
         "l’État dans l’éducation et la formation."},
   {'n': "Paul Romer",
    'i': "L’accumulation de connaissances et le capital humain se renforcent "
         "mutuellement dans la production d’innovations.",
    'p': "La recherche exige du capital humain et en produit : une population "
         "qualifiée innove davantage, et l’innovation élève le rendement de la "
         "qualification, ce qui boucle le mécanisme de croissance endogène."}],
  [{'f': "Le capital humain apparaît 28 fois dans le chapitre consacré à la "
         "croissance et 15 fois dans celui consacré au développement, ce qui "
         "signale son caractère transversal.",
    'p': "La notion fait le lien entre croissance et développement : elle est "
         "simultanément un facteur de production et une dimension du "
         "développement humain."},
   {'f': "Lucas publie son modèle fondé sur le capital humain en 1988, dans le "
         "mouvement de rupture avec le modèle de Solow.",
    'p': "La date situe l’entrée du capital humain dans la théorie de la "
         "croissance de long terme, après avoir été d’abord un concept de "
         "microéconomie du travail chez Becker."}],
  [{'q': "Sujet du type « L’école réduit-elle ou reproduit-elle les "
         "inégalités ? »",
    'f': "La théorie du capital humain prédit que l’éducation élève la "
         "productivité et donc le revenu de ceux qui la reçoivent, ce qui en "
         "fait un instrument de mobilité. Mais cette prédiction suppose un "
         "accès effectivement ouvert : si l’accès à la formation reste "
         "socialement déterminé, le même mécanisme transmet les positions au "
         "lieu de les redistribuer.",
    'r': "On montre que l’effet égalisateur n’est pas inscrit dans le mécanisme "
         "lui-même mais dépend des conditions d’accès, ce qui articule analyse "
         "économique et analyse sociologique.",
    'ex': "Becker traite la formation comme un investissement dont le rendement "
          "dépend du coût supporté, lui-même inégalement réparti."},
   {'q': "Sujet du type « D’où vient la croissance économique ? »",
    'f': "Le capital humain fournit l’une des réponses les plus solides à "
         "l’énigme du résidu : si la qualification élève la productivité de son "
         "détenteur et de son environnement, alors une part de ce que la "
         "comptabilité attribuait à un progrès technique inexpliqué relève en "
         "réalité d’un investissement identifiable.",
    'r': "On présente le capital humain comme une décomposition du résidu, ce "
         "qui inscrit le dossier dans la progression générale du sujet sur la "
         "croissance.",
    'ex': "Le modèle de Lucas (1988), qui endogénéise la croissance par "
          "l’accumulation de qualifications."}],
  voisins=['n1-endogene', 'n1-rd', 'n1-progres-technique', 'n1-croissance',
           'n1-institutions'])

d('n1-rd', 1, "Recherche et développement",
  "Produire des connaissances dont on ne capte pas tout le rendement",
  "La recherche et développement désigne l’ensemble des activités "
  "systématiques visant à accroître les connaissances et à les appliquer à de "
  "nouveaux produits ou procédés. Elle constitue, chez Romer, le moteur interne "
  "de la croissance : son produit est une connaissance, bien non rival qui peut "
  "être utilisé simultanément par plusieurs agents sans se détruire, ce qui lui "
  "confère des rendements non décroissants.",
  "L’analyse économique de la recherche repose entièrement sur la nature "
  "particulière de son produit, et c’est par là qu’il faut commencer. Une "
  "connaissance est non rivale : son usage par un agent ne prive pas les autres "
  "de son usage. Elle est en revanche partiellement excluable, ce qui permet "
  "des brevets. De cette asymétrie découle tout le reste. Parce qu’elle est non "
  "rivale, la connaissance accumulée élève le rendement de la recherche "
  "suivante — on invente sur les épaules des inventions précédentes — ce qui "
  "produit des rendements croissants à l’échelle de l’économie et autorise une "
  "croissance durable. Parce qu’elle n’est qu’imparfaitement excluable, "
  "l’inventeur ne capte qu’une fraction du rendement social de sa découverte : "
  "il sous-investit donc, et le marché laissé à lui-même produit moins de "
  "recherche que l’optimum collectif. Deux réponses existent, et elles sont en "
  "tension. La première est le brevet : il restaure l’incitation en créant un "
  "monopole temporaire, mécanisme que Howitt place au cœur de l’innovation "
  "verticale, mais il ralentit la diffusion. La seconde est le financement "
  "public, qui favorise la diffusion mais suppose de savoir quoi financer. "
  "Aghion ajoute que l’intensité de la concurrence détermine l’incitation à "
  "innover, ce qui fait du rythme du progrès technique une variable de "
  "politique économique.",
  [("La production de connaissances",
    "L’effort de recherche mobilise du capital humain et des équipements pour "
    "produire des connaissances nouvelles, dont une partie seulement donnera "
    "lieu à des applications commercialisables."),
   ("La non-rivalité et le cumul",
    "Une connaissance peut servir simultanément à plusieurs agents sans se "
    "dégrader. Le stock accumulé élève donc la productivité de la recherche "
    "ultérieure, ce qui engendre des rendements croissants à l’échelle "
    "collective."),
   ("L’écart entre rendement privé et rendement social",
    "L’inventeur ne capte qu’une partie du bénéfice de sa découverte, le reste "
    "se diffusant aux concurrents, aux fournisseurs et aux clients. Il investit "
    "donc moins que l’optimum social."),
   ("Le brevet comme restauration de l’incitation",
    "En conférant un monopole temporaire, le brevet permet de capter une rente "
    "qui finance la recherche. Howitt montre que cette rente est détruite par "
    "l’innovation suivante, ce qui entretient la dynamique."),
   ("L’arbitrage entre incitation et diffusion",
    "Protéger fortement l’innovation accroît l’incitation à innover mais "
    "ralentit la diffusion des connaissances, qui est précisément la source des "
    "rendements croissants. La durée optimale du brevet résulte de cet "
    "arbitrage.")],
  [{'a': "La recherche et développement est la source d’une croissance durable, "
         "puisque son produit se cumule sans se détruire.",
    'cond': "Il faut un stock de capital humain capable de produire et "
            "d’absorber les connaissances, et des institutions assurant la "
            "circulation des résultats.",
    'lim': "Le rendement de la recherche n’est pas constant : il peut décroître "
           "si les découvertes faciles ont déjà été faites, ce que suggère le "
           "diagnostic de Robert Gordon."},
   {'a': "Le financement public de la recherche corrige une défaillance de "
         "marché identifiée : l’écart entre rendement social et rendement privé.",
    'cond': "L’intervention doit porter en priorité sur la recherche "
            "fondamentale, dont les externalités sont les plus fortes et "
            "l’appropriation la plus faible.",
    'lim': "L’État doit choisir ses axes sans connaître à l’avance les "
           "découvertes, ce qui rend l’allocation incertaine et exposée aux "
           "pressions."},
   {'a': "Le brevet permet de financer l’innovation par le marché, sans "
         "prélèvement public, en créant une rente temporaire.",
    'cond': "La durée et l’étendue de la protection doivent être calibrées : "
            "trop faibles, elles n’incitent pas ; trop fortes, elles bloquent "
            "la diffusion et les innovations suivantes.",
    'lim': "Un système de brevets trop protecteur peut freiner l’innovation "
           "cumulative, puisque chaque nouvelle recherche doit négocier l’accès "
           "aux brevets antérieurs."}],
  [{'t': "L’effort de recherche n’a jamais été aussi élevé et les gains de "
         "productivité ralentissent pourtant : le rendement de la recherche "
         "serait décroissant.",
    'qui': "Objection tirée du diagnostic de Robert Gordon sur l’efficacité des "
           "innovations récentes.",
    'rep': "L’objection est sérieuse. On peut y opposer le délai de diffusion "
           "des technologies générales et les difficultés de mesure dans les "
           "services, mais elle oblige à ne pas traiter la recherche comme un "
           "levier à rendement garanti."},
   {'t': "La protection intellectuelle transforme l’innovation en rente et peut "
         "bloquer la diffusion plutôt que la favoriser.",
    'qui': "Objection tirée de l’arbitrage entre incitation et diffusion, et des "
           "analyses sur les rentes d’innovation.",
    'rep': "Elle justifie un calibrage de la protection plutôt que son "
           "abandon : sans exclusivité temporaire, le financement privé de la "
           "recherche se tarit."}],
  [{'n': "Paul Romer",
    'i': "La recherche et développement et les idées sont les moteurs internes "
         "de la croissance, en raison de la non-rivalité des connaissances.",
    'p': "Parce qu’une idée peut être utilisée par tous simultanément, son "
         "rendement collectif excède son rendement privé : l’investissement "
         "privé est insuffisant, et l’accumulation de connaissances échappe aux "
         "rendements décroissants."},
   {'n': "Philippe Aghion",
    'i': "La croissance par destruction créatrice dépend conjointement de "
         "l’effort de recherche et de l’intensité de la concurrence.",
    'p': "L’innovation est motivée par la perspective d’une rente, mais une "
         "concurrence trop faible réduit la pression à innover : le rythme du "
         "progrès technique dépend donc d’un dosage que la politique de "
         "concurrence peut influencer."},
   {'n': "Peter Howitt",
    'i': "L’innovation verticale améliore la qualité d’un produit existant et "
         "procure à son auteur un monopole temporaire.",
    'p': "La rente obtenue finance la recherche, puis disparaît avec "
         "l’innovation suivante : le progrès technique prend la forme d’une "
         "succession de monopoles provisoires, ce qui en fait un processus de "
         "remplacement continu."},
   {'n': "Joseph Schumpeter",
    'i': "L’innovation est le fait de l’entrepreneur et procède par destruction "
         "créatrice.",
    'p': "L’innovation ne s’ajoute pas à l’existant : elle le remplace, "
         "détruisant des positions établies en même temps qu’elle crée des "
         "activités nouvelles. La recherche s’inscrit ainsi dans une dynamique "
         "conflictuelle et non cumulative au niveau des firmes."}],
  [{'f': "Les théories de la croissance endogène expliquent le progrès "
         "technique par l’innovation, la recherche et développement et le "
         "capital humain, à partir des années 1980.",
    'p': "La recherche et développement devient ainsi une variable de politique "
         "économique agissant sur le taux de croissance de long terme, et non "
         "une dépense annexe."},
   {'f': "Selon Robert Gordon, les innovations récentes présentent une moindre "
         "efficacité productive que celles des révolutions industrielles "
         "précédentes.",
    'p': "Le constat met en question l’hypothèse d’un rendement constant de la "
         "recherche, et donc la capacité de la seule intensification de "
         "l’effort de recherche à relancer la croissance."}],
  [{'q': "Sujet du type « La concurrence stimule-t-elle toujours "
         "l’innovation ? »",
    'f': "L’innovation est financée par la perspective d’une rente temporaire : "
         "une concurrence trop intense peut donc détruire l’incitation, tandis "
         "qu’une concurrence trop faible supprime la pression à innover. "
         "Aghion situe précisément l’enjeu dans ce dosage, ce qui interdit de "
         "répondre par une relation monotone.",
    'r': "On remplace une relation supposée croissante par un arbitrage, ce qui "
         "permet de traiter les cas extrêmes et d’en déduire une recommandation "
         "de politique de concurrence.",
    'ex': "Le monopole temporaire décrit par Howitt, qui finance l’innovation "
          "avant d’être détruit par la suivante."},
   {'q': "Sujet du type « Quand l’intervention de l’État est-elle "
         "nécessaire ? »",
    'f': "La recherche fournit le cas le plus net d’externalité positive : "
         "l’inventeur ne capte qu’une fraction du rendement social de sa "
         "découverte, donc il sous-investit. L’intervention publique ne corrige "
         "pas une injustice mais une défaillance d’incitation, ce qui en fait un "
         "argument d’efficacité et non de redistribution.",
    'r': "Partir de la nature du bien — non rival, imparfaitement excluable — "
         "permet de déduire la défaillance plutôt que de la postuler.",
    'ex': "Le financement public de la recherche fondamentale, dont les "
          "externalités sont les plus fortes et l’appropriation la plus faible."}],
  voisins=['n1-endogene', 'n1-progres-technique', 'n1-capital-humain',
           'n1-institutions', 'n1-croissance'])
