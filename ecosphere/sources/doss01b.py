# -*- coding: utf-8 -*-
"""Ensemble 1 — La croissance économique et ses moteurs (2/3)."""

from doss_base import d

d('n1-investissement', 1, "Investissement",
  "Une dépense qui soutient la demande aujourd’hui et l’offre demain",
  "L’investissement désigne l’acquisition de biens de production durables "
  "destinés à être utilisés dans le processus productif : équipements, "
  "bâtiments, logiciels, mais aussi, dans une acception élargie, recherche et "
  "formation. Sa particularité est d’avoir deux effets de nature différente et "
  "de calendrier distinct : un effet immédiat de demande, puisqu’il constitue "
  "une dépense, et un effet différé d’offre, puisqu’il accroît les capacités "
  "productives.",
  "Cette dualité est le cœur de l’analyse de l’investissement, et Domar en a "
  "fait le ressort de son modèle. L’effet de demande est keynésien : "
  "l’investissement est une composante de la demande globale, et il se "
  "multiplie, puisque les revenus qu’il distribue sont en partie dépensés. "
  "L’effet d’offre est classique : les capacités installées doivent être "
  "utilisées, ce qui exige que la demande croisse au rythme exact de leur "
  "augmentation — condition qui n’a aucune raison d’être spontanément "
  "satisfaite, d’où l’instabilité mise en évidence par Harrod. Du côté des "
  "déterminants, trois variables dominent. La première est la demande "
  "anticipée : on n’investit que si l’on prévoit de vendre, ce qui rend "
  "l’investissement procyclique et explique le mécanisme de l’accélérateur. La "
  "deuxième est le coût du financement rapporté au rendement attendu : un taux "
  "d’intérêt élevé élimine les projets les moins rentables. La troisième, "
  "souvent décisive, est l’incertitude : un projet irréversible engagé dans un "
  "environnement imprévisible sera repoussé même s’il est rentable en moyenne. "
  "C’est pourquoi l’investissement est la composante la plus volatile de la "
  "demande, et le canal par lequel les anticipations se transmettent à "
  "l’économie réelle.",
  [("L’effet multiplicateur de demande",
    "La dépense d’investissement distribue des revenus qui sont partiellement "
    "consommés, lesquels distribuent à leur tour des revenus. L’effet total sur "
    "la production excède la dépense initiale."),
   ("L’effet capacité",
    "L’équipement installé élève la production potentielle. Pour que cette "
    "capacité soit utilisée, la demande doit progresser au même rythme, sans "
    "quoi apparaissent des surcapacités qui découragent l’investissement "
    "suivant."),
   ("L’accélérateur",
    "Une variation de la demande provoque une variation proportionnellement "
    "plus forte de l’investissement, puisqu’il faut ajuster le stock de capital "
    "à un nouveau niveau d’activité. Le mécanisme amplifie les fluctuations."),
   ("L’arbitrage rendement–coût du capital",
    "Un projet est engagé si son rendement anticipé excède le coût du "
    "financement. La politique monétaire agit sur l’investissement par ce "
    "canal, en déplaçant le seuil de rentabilité."),
   ("Le rôle de l’incertitude",
    "L’investissement est largement irréversible : une fois engagé, il ne peut "
    "être défait sans perte. L’incertitude a donc une valeur d’attente, et "
    "reporter la décision peut être rationnel même pour un projet rentable.")],
  [{'a': "L’investissement est le levier par lequel une politique de relance "
         "agit à la fois sur la conjoncture et sur les capacités futures.",
    'cond': "Il faut des projets disponibles, des capacités de financement et "
            "une anticipation de demande suffisante pour que les entreprises "
            "suivent.",
    'lim': "En situation d’incertitude forte, la baisse du coût du capital ne "
           "suffit pas à déclencher la dépense : l’attente reste la stratégie "
           "dominante."},
   {'a': "L’investissement incorpore le progrès technique : les équipements "
         "nouveaux sont plus efficaces que ceux qu’ils remplacent.",
    'cond': "Cela suppose un renouvellement effectif du stock de capital et une "
            "main-d’œuvre formée aux techniques nouvelles.",
    'lim': "Un investissement de simple remplacement n’accroît pas le stock et "
           "ne contribue donc pas à l’accumulation, même s’il élève la "
           "productivité."},
   {'a': "L’investissement en recherche et en formation échappe aux rendements "
         "décroissants et peut donc soutenir une croissance durable.",
    'cond': "L’argument suppose des externalités effectives, c’est-à-dire une "
            "diffusion des connaissances au-delà de l’entreprise qui les "
            "finance.",
    'lim': "Ces externalités font précisément que l’investisseur privé ne "
           "capte pas tout le rendement, donc qu’il sous-investit : le "
           "mécanisme justifie une intervention publique."}],
  [{'t': "L’investissement ne crée de la croissance durable que si la demande "
         "suit : sinon, il installe des surcapacités.",
    'qui': "Conséquence directe du double effet mis en évidence par Domar.",
    'rep': "L’objection est structurelle et justifie la coordination des "
           "politiques : l’investissement n’est pas un remède en soi, il "
           "suppose un débouché."},
   {'t': "Une baisse du taux d’intérêt peut rester sans effet sur "
         "l’investissement lorsque les anticipations sont dégradées.",
    'qui': "Analyse keynésienne du rôle des anticipations, prolongée par le cas "
           "de la trappe à liquidité.",
    'rep': "Elle montre que le canal du coût du capital n’est ni unique ni "
           "toujours dominant, et que la politique monétaire a besoin d’un "
           "relais budgétaire lorsque la confiance manque."}],
  [{'n': "Evsey Domar",
    'i': "L’investissement a un double effet : demande immédiate et capacité "
         "future.",
    'p': "La croissance n’est équilibrée que si la demande progresse au rythme "
         "exact de l’augmentation des capacités installées, ce qui fait de "
         "l’équilibre un cas particulier et non la règle."},
   {'n': "Roy Harrod",
    'i': "Le sentier de croissance fondé sur l’investissement est instable.",
    'p': "L’image du fil du rasoir traduit l’idée qu’un écart entre croissance "
         "effective et croissance garantie s’amplifie : un excès de capacité "
         "décourage l’investissement, ce qui réduit encore la demande."},
   {'n': "Robert Solow",
    'i': "Le taux d’investissement détermine le niveau de production de long "
         "terme, non son taux de croissance.",
    'p': "Un pays qui investit davantage atteint un état stationnaire plus "
         "élevé, mais il n’y croît pas plus vite : la distinction entre niveau "
         "et rythme est l’un des résultats les plus contre-intuitifs du modèle."}],
  [{'f': "La décomposition de la croissance française des Trente Glorieuses "
         "attribue environ 40 % de la croissance à la contribution des facteurs, "
         "dont le capital issu de l’investissement.",
    'p': "L’ordre de grandeur montre que l’investissement a joué un rôle "
         "substantiel sans être le déterminant principal, même pendant la "
         "période de plus fort effort d’équipement."},
   {'f': "Les théories de la croissance endogène élargissent la notion "
         "d’investissement à la recherche et développement chez Romer, au "
         "capital humain chez Lucas et au capital public chez Barro.",
    'p': "L’élargissement de la notion est ce qui permet de lui restituer un "
         "rôle dans la croissance de long terme, que le modèle de Solow lui "
         "refusait."}],
  [{'q': "Sujet du type « Dans quelles conditions une relance est-elle "
         "efficace ? »",
    'f': "L’investissement est le canal privilégié d’une relance parce qu’il "
         "agit sur les deux horizons : il soutient la demande immédiatement et "
         "élève les capacités productives ensuite. Mais cette double nature est "
         "aussi sa fragilité, puisque la capacité installée exige un débouché "
         "qui n’est pas garanti.",
    'r': "On utilise la dualité demande/capacité pour organiser les "
         "conditions d’efficacité au lieu de les énumérer sans lien : chaque "
         "condition se rattache à l’un des deux effets de l’investissement.",
    'ex': "Le modèle Harrod-Domar, où l’équilibre exige que la demande croisse "
          "au rythme exact des capacités nouvelles."},
   {'q': "Sujet du type « Pourquoi l’investissement est-il si volatile ? »",
    'f': "Trois mécanismes se cumulent : l’accélérateur, qui amplifie les "
         "variations de demande ; la sensibilité au coût du financement ; et "
         "l’irréversibilité, qui donne une valeur à l’attente en situation "
         "d’incertitude. La volatilité de l’investissement n’est donc pas une "
         "anomalie, c’est une conséquence de sa nature.",
    'r': "On construit la réponse par superposition de mécanismes, ce qui "
         "montre que la volatilité de l’investissement est surdéterminée "
         "plutôt que fortuite, et qu’aucun instrument unique ne suffit à la "
         "contenir.",
    'ex': "L’accélérateur d’investissement, qui lie une variation de la demande "
          "à une variation plus forte du stock de capital désiré."}],
  voisins=['n1-accumulation', 'n1-croissance', 'n1-endogene', 'n1-rd',
           'n1-infrastructures'])

d('n1-productivite', 1, "Productivité et gains de productivité",
  "Le rapport entre ce qu’on produit et ce qu’on y consacre",
  "La productivité est le rapport entre une production et les moyens employés "
  "pour l’obtenir. La productivité du travail rapporte la production au volume "
  "de travail, la productivité du capital à la quantité de capital. Les gains "
  "de productivité désignent l’augmentation de ce rapport : produire autant "
  "avec moins, ou davantage avec autant. Ils constituent, selon Jean Arrous, le "
  "fondement du caractère cumulatif de la croissance.",
  "Les gains de productivité sont le mécanisme central de l’enrichissement "
  "d’une société, et il faut en suivre la chaîne complète pour comprendre "
  "pourquoi. Un gain de productivité crée un surplus : la même production "
  "mobilise moins de ressources, ou les mêmes ressources en produisent "
  "davantage. Ce surplus se répartit ensuite entre quatre usages, et c’est "
  "cette répartition qui détermine ses effets macroéconomiques. Il peut être "
  "versé en salaires, ce qui soutient la consommation ; en profits, ce qui "
  "finance l’investissement ; répercuté en baisse de prix, ce qui élève le "
  "pouvoir d’achat de tous les acheteurs ; ou converti en réduction du temps de "
  "travail. Chacun de ces canaux alimente l’activité, ce qui boucle le circuit "
  "et rend la croissance cumulative. Mais le même mécanisme emporte une "
  "conséquence que les sujets exploitent constamment : à demande inchangée, un "
  "gain de productivité réduit le besoin de main-d’œuvre. L’emploi n’est "
  "préservé que si la demande croît au moins aussi vite que la productivité — "
  "ce qui a été le cas pendant les Trente Glorieuses et beaucoup moins ensuite. "
  "La question de l’emploi n’est donc pas extérieure à celle de la "
  "productivité : elle est contenue dans sa définition même.",
  [("La création d’un surplus",
    "Produire autant avec moins de facteurs, ou davantage avec les mêmes, "
    "dégage une marge que l’économie peut affecter à différents usages. C’est "
    "l’origine du supplément de richesse."),
   ("La répartition du surplus",
    "Le gain se distribue en hausse des salaires, en profits, en baisse des prix "
    "ou en réduction du temps de travail. Le choix de cette répartition "
    "détermine qui bénéficie de la croissance."),
   ("Le bouclage par la demande",
    "Salaires et profits plus élevés, prix plus bas soutiennent la consommation "
    "et l’investissement, donc la production : le gain de productivité engendre "
    "la demande qui permettra de l’absorber."),
   ("L’effet sur l’emploi",
    "À production donnée, un gain de productivité réduit le volume de travail "
    "nécessaire. L’emploi n’est maintenu que si la production augmente au moins "
    "autant, ce qui lie l’emploi au rythme de la demande."),
   ("La diffusion intersectorielle",
    "Les gains obtenus dans un secteur se transmettent aux autres par la baisse "
    "du prix des biens qu’il produit, notamment des équipements, et par la "
    "diffusion des méthodes d’organisation.")],
  [{'a': "Les gains de productivité sont la seule source durable "
         "d’augmentation du niveau de vie, puisqu’ils ne dépendent pas d’une "
         "hausse des quantités de facteurs.",
    'cond': "Le surplus doit être effectivement réparti : un gain intégralement "
            "capté sous forme de marges n’élève pas le niveau de vie moyen.",
    'lim': "Ils peuvent détruire de l’emploi lorsque la demande ne suit pas, ce "
           "qui en fait un mécanisme favorable en longue période et "
           "potentiellement douloureux à court terme."},
   {'a': "Ils améliorent la compétitivité : une productivité plus élevée "
         "abaisse le coût salarial unitaire à salaire donné.",
    'cond': "L’effet suppose que les salaires ne progressent pas plus vite que "
            "la productivité, sans quoi le coût unitaire augmente malgré le "
            "gain.",
    'lim': "La compétitivité ainsi obtenue est relative : elle dépend de "
           "l’évolution comparée chez les partenaires, et sa recherche "
           "généralisée peut déprimer la demande mondiale."},
   {'a': "Ils permettent de financer la protection sociale et la réduction du "
         "temps de travail sans appauvrissement.",
    'cond': "Il faut un rythme de gains suffisant et une négociation collective "
            "capable d’en organiser l’affectation.",
    'lim': "Un ralentissement durable des gains rend ces engagements "
           "insoutenables, ce qui est l’un des ressorts des tensions sur les "
           "systèmes sociaux depuis les années 1970."}],
  [{'t': "Les gains de productivité détruisent des emplois, puisque la "
         "machine remplace le travailleur et qu’il faut moins de "
         "main-d’œuvre pour une même production.",
    'qui': "Objection ancienne, discutée dans le cours à propos du progrès "
           "technique et de l’emploi.",
    'rep': "Elle est exacte à production constante et fausse en dynamique : la "
           "baisse des prix et la hausse des revenus engendrent une demande "
           "nouvelle. Tout dépend donc de la vitesse relative de la demande et "
           "de la productivité."},
   {'t': "Les gains de productivité ralentissent structurellement dans les "
         "économies avancées, et non pour des raisons conjoncturelles qu’une "
         "reprise suffirait à corriger.",
    'qui': "Robert Gordon, qui attribue la faiblesse de la croissance à un "
           "ralentissement des gains de productivité et à une moindre "
           "efficacité des innovations récentes.",
    'rep': "Le diagnostic est contesté, notamment par les tenants d’un délai "
           "de diffusion des technologies numériques, mais il est empiriquement "
           "sérieux et doit être discuté plutôt qu’écarté."},
   {'t': "La productivité est mal mesurée dans les services, où la production "
         "est difficile à quantifier.",
    'qui': "Difficulté de mesure signalée par la tertiarisation des économies.",
    'rep': "L’objection est méthodologique et importante : elle peut expliquer "
           "une partie du ralentissement apparent, sans suffire à le dissoudre "
           "entièrement."}],
  [{'n': "Jean Arrous",
    'i': "La croissance est un processus cumulatif fondé sur la productivité.",
    'p': "Les gains de productivité engendrent les revenus qui financent la "
         "demande et l’investissement, lesquels produisent de nouveaux gains : "
         "c’est ce bouclage qui rend la croissance auto-entretenue."},
   {'n': "Robert Gordon",
    'i': "Le ralentissement structurel de la productivité explique la faiblesse "
         "de la croissance contemporaine.",
    'p': "Historien de l’économie américaine, il soutient que les innovations "
         "récentes ont une efficacité productive moindre que celles des "
         "révolutions industrielles précédentes, ce qui pèse durablement sur la "
         "croissance potentielle."},
   {'n': "Jean Fourastié",
    'i': "Le déversement sectoriel : les gains de productivité transforment la "
         "structure de l’emploi.",
    'p': "Les gains réalisés dans un secteur libèrent de la main-d’œuvre qui se "
         "reporte vers d’autres activités, ce qui explique le passage de "
         "l’agriculture à l’industrie puis aux services sans destruction nette "
         "d’emploi."}],
  [{'f': "Environ 60 % de la croissance française des Trente Glorieuses "
         "s’explique par la productivité globale des facteurs, soit 3,1 points "
         "sur 5,2 %.",
    'p': "Le chiffre établit la primauté des gains de productivité dans la "
         "période de croissance la plus forte, et fournit le point de "
         "comparaison du ralentissement ultérieur."},
   {'f': "Selon Robert Gordon, la faiblesse de la croissance s’explique par un "
         "ralentissement des gains de productivité et une moindre efficacité "
         "des innovations récentes.",
    'p': "Le diagnostic situe la cause du ralentissement du côté de l’offre et "
         "non de la demande, ce qui oriente différemment les politiques "
         "économiques à préconiser."}],
  [{'q': "Sujet du type « Le progrès technique détruit-il le travail ? »",
    'f': "Le mécanisme de destruction est réel mais partiel : à production "
         "donnée, un gain de productivité réduit le besoin de main-d’œuvre. La "
         "question est donc celle de la vitesse relative de la demande et de la "
         "productivité — et le déversement sectoriel décrit par Fourastié "
         "montre que, historiquement, la main-d’œuvre libérée a été réemployée "
         "ailleurs.",
    'r': "On oppose l’effet statique, négatif, à l’effet dynamique, "
         "compensateur, ce qui permet de conclure sur les conditions du "
         "réemploi plutôt que sur le signe du solde.",
    'ex': "Le déversement de l’agriculture vers l’industrie puis vers les "
          "services."},
   {'q': "Sujet du type « Sommes-nous condamnés au ralentissement de la "
         "croissance ? »",
    'f': "Puisque les gains de productivité sont la source durable de la "
         "croissance, la question se ramène à celle de leur rythme. Robert "
         "Gordon soutient que les innovations récentes sont moins efficaces que "
         "celles des révolutions industrielles antérieures, ce qui implique un "
         "ralentissement structurel et non conjoncturel.",
    'r': "Ramener la question de la croissance à celle de la productivité évite "
         "de disperser le devoir et permet de confronter directement les thèses "
         "de l’offre et celles de la demande.",
    'ex': "Le contraste entre les 3,1 points de productivité globale des "
          "facteurs des Trente Glorieuses et le ralentissement observé depuis "
          "les années 1970."}],
  voisins=['n1-pgf', 'n1-progres-technique', 'n1-croissance',
           'n1-extensive-intensive', 'n1-stagnation'])

d('n1-pgf', 1, "Productivité globale des facteurs",
  "Ce que la croissance doit à l’efficacité de la combinaison productive",
  "La productivité globale des facteurs rapporte la production à l’ensemble des "
  "facteurs employés, travail et capital pris conjointement. Elle se mesure par "
  "différence : on retranche de la croissance observée la part attribuable à "
  "l’augmentation des quantités de facteurs, et l’on obtient un résidu. Ce "
  "résidu, appelé résidu de Solow, est identifié à l’efficacité avec laquelle "
  "les facteurs sont combinés.",
  "La productivité globale des facteurs est à la fois l’outil le plus "
  "fécond et le plus fragile de l’analyse de la croissance, et une bonne copie "
  "doit dire les deux. Sa fécondité est évidente : en isolant ce que "
  "l’accumulation n’explique pas, elle a révélé que la croissance ne vient pas "
  "principalement de l’accumulation. Carré, Dubois et Malinvaud, appliquant la "
  "méthode de Solow à la France dans La croissance française (1972), trouvent "
  "qu’environ 60 % de la croissance des Trente Glorieuses relève de la "
  "productivité globale des facteurs : 3,1 points sur 5,2 %. Ce résultat a "
  "orienté toute la théorie ultérieure. Sa fragilité est de nature logique : la "
  "productivité globale des facteurs n’est pas mesurée, elle est déduite. Elle "
  "recueille tout ce que le modèle n’a pas su attribuer — progrès technique, "
  "mais aussi qualité de l’organisation, niveau de qualification, qualité des "
  "institutions, et erreurs de mesure du stock de capital. Le cours pose "
  "d’ailleurs la question frontalement : le résidu de Solow est-il une manne "
  "céleste ou l’aveu d’une ignorance ? Solow lui-même parlait du progrès "
  "technique comme d’une richesse « tombée du ciel ». Toute l’histoire "
  "ultérieure de la théorie de la croissance consiste à réduire ce résidu en "
  "expliquant ce qu’il contient.",
  [("La mesure de la croissance observée",
    "On part du taux de croissance effectif du produit sur la période "
    "considérée, mesuré en volume afin de neutraliser l’effet des prix "
    "et de ne retenir que la variation réelle des quantités produites."),
   ("L’attribution aux facteurs",
    "On calcule la contribution de la hausse du volume de travail et celle de "
    "la hausse du stock de capital, chacune pondérée par la part du facteur dans "
    "la valeur ajoutée."),
   ("Le calcul du résidu",
    "La différence entre croissance observée et contributions des facteurs "
    "constitue la productivité globale des facteurs. Elle est donc obtenue par "
    "soustraction et non par observation directe."),
   ("L’interprétation du résidu",
    "On l’identifie à l’efficacité de la combinaison productive, c’est-à-dire "
    "au progrès technique au sens large : techniques, organisation, "
    "qualification, institutions.")],
  [{'a': "La productivité globale des facteurs permet de caractériser le régime "
         "de croissance d’une économie et de situer sa marge de progression.",
    'cond': "Le calcul exige des séries longues et homogènes sur le produit, "
            "l’emploi et le stock de capital.",
    'lim': "La mesure du stock de capital est particulièrement incertaine, ce "
           "qui se répercute intégralement sur le résidu."},
   {'a': "Elle a établi empiriquement que l’accumulation n’explique pas "
         "l’essentiel de la croissance, ce qui a réorienté toute la théorie.",
    'cond': "Le résultat suppose que la pondération des facteurs par leur part "
            "dans la valeur ajoutée soit justifiée, ce qui repose sur des "
            "hypothèses de concurrence.",
    'lim': "Un résidu élevé n’explique rien par lui-même : il signale une "
           "question plutôt qu’il n’apporte une réponse."},
   {'a': "Elle fournit un indicateur comparable entre pays et entre périodes, "
         "utile au diagnostic de politique économique.",
    'cond': "La comparabilité suppose des conventions statistiques communes, "
            "notamment sur l’amortissement et la qualité du travail.",
    'lim': "Les différences de structure sectorielle biaisent les comparaisons, "
           "la mesure de la productivité étant plus difficile dans les services."}],
  [{'t': "Le résidu mesure notre ignorance plutôt que le progrès technique : "
         "il recueille tout ce que le modèle n’a pas su attribuer aux "
         "facteurs.",
    'qui': "Question posée explicitement par le cours à propos du résidu de "
           "Solow, et par Solow lui-même évoquant une « manne tombée du ciel ».",
    'rep': "L’objection est recevable et féconde : c’est précisément pour la "
           "lever que les théories endogènes ont décomposé le résidu en capital "
           "humain, recherche et capital public."},
   {'t': "La méthode suppose l’existence d’une fonction de production "
         "agrégée, hypothèse contestable dès lors que les capitaux sont "
         "hétérogènes et non réductibles à une grandeur unique.",
    'qui': "Objection théorique à l’agrégation des capitaux hétérogènes.",
    'rep': "Elle limite la portée théorique du calcul sans supprimer son "
           "intérêt descriptif : le résidu reste un fait comptable qui demande "
           "une explication."}],
  [{'n': "Robert Solow",
    'i': "Le résidu mesure la part de la croissance que l’accumulation "
         "n’explique pas, assimilée au progrès technique.",
    'p': "Solow a été l’un des premiers à chercher à mesurer ce qui explique la "
         "croissance ; il décrit le progrès technique comme une « manne tombée "
         "du ciel », formule qui dit à la fois son importance et le fait que le "
         "modèle n’en rende pas compte."},
   {'n': "Jean Carré",
    'i': "L’application de la méthode à la France : décomposer la croissance "
         "entre travail, capital et résidu.",
    'p': "Avec Paul Dubois et Edmond Malinvaud, La croissance française (1972) : "
         "l’objectif est d’expliquer la forte croissance française de "
         "l’après-guerre en mesurant la part de chaque source."},
   {'n': "Paul Dubois",
    'i': "La croissance française des Trente Glorieuses est principalement "
         "intensive.",
    'p': "Le résultat — environ 60 % de la croissance imputable à la "
         "productivité globale des facteurs — établit que l’efficacité "
         "productive, et non le seul effort d’équipement, a porté la période."}],
  [{'f': "Carré, Dubois et Malinvaud, La croissance française (1972) : environ "
         "60 % de la croissance française des Trente Glorieuses s’explique par "
         "la productivité globale des facteurs, soit 3,1 points sur 5,2 %.",
    'p': "C’est le chiffre de référence sur la décomposition de la croissance "
         "française, et la démonstration empirique que l’accumulation ne suffit "
         "pas."},
   {'f': "Une croissance est dite intensive lorsque la contribution de la "
         "productivité globale des facteurs domine, extensive lorsque c’est "
         "celle des facteurs de production.",
    'p': "La productivité globale des facteurs est donc le critère même de la "
         "distinction entre les deux régimes de croissance."}],
  [{'q': "Sujet du type « D’où vient la croissance économique ? »",
    'f': "La décomposition comptable fournit le point de départ obligé : une "
         "fois attribuée aux facteurs la part qui leur revient, il reste un "
         "résidu considérable — environ 60 % de la croissance française des "
         "Trente Glorieuses — que l’accumulation n’explique pas et qu’il faut "
         "donc expliquer autrement.",
    'r': "Partir d’un fait comptable plutôt que d’un modèle donne au devoir une "
         "assise empirique et justifie l’enchaînement des théories.",
    'ex': "Les 3,1 points de productivité globale des facteurs mesurés par "
          "Carré, Dubois et Malinvaud."},
   {'q': "Sujet du type « La croissance peut-elle s’entretenir elle-même ? »",
    'f': "Tout dépend de ce que contient le résidu. S’il désigne un progrès "
         "technique exogène, la croissance de long terme échappe à la décision "
         "économique ; s’il recouvre des investissements identifiables en "
         "recherche, en éducation et en infrastructures, alors la croissance "
         "devient endogène et peut être entretenue par des politiques.",
    'r': "Faire de l’interprétation du résidu l’enjeu du sujet permet de "
         "montrer que l’opposition entre Solow et les théories endogènes porte "
         "sur une seule question analytique.",
    'ex': "La question posée par le cours : le résidu de Solow, manne céleste ou "
          "ignorance ?"}],
  voisins=['n1-productivite', 'n1-progres-technique', 'n1-extensive-intensive',
           'n1-endogene', 'n1-croissance'])

d('n1-progres-technique', 1, "Progrès technique",
  "D’une manne tombée du ciel à un résultat de décisions économiques",
  "Le progrès technique désigne l’ensemble des améliorations qui permettent de "
  "produire davantage ou mieux avec les mêmes facteurs : techniques nouvelles, "
  "procédés plus efficaces, organisation améliorée, produits inédits. Dans la "
  "comptabilité de la croissance, il est approché par la productivité globale "
  "des facteurs. Son statut théorique a changé : exogène chez Solow, il devient "
  "endogène dans les modèles des années 1980.",
  "Le déplacement du statut du progrès technique est l’un des épisodes les plus "
  "instructifs de l’histoire de la pensée économique, et il structure à lui "
  "seul un sujet. Dans le modèle de Solow, le progrès technique est le "
  "déterminant unique de la croissance par tête de long terme — puisque "
  "l’accumulation s’épuise — mais il est traité comme une donnée extérieure, "
  "une « manne tombée du ciel ». Cette position est intenable "
  "intellectuellement : elle fait dépendre l’essentiel de la croissance d’un "
  "facteur que la théorie n’explique pas et sur lequel la politique économique "
  "n’a aucune prise. Les théories de la croissance endogène lèvent cette "
  "difficulté en montrant que le progrès technique résulte de décisions "
  "économiques identifiables : la recherche et développement et l’accumulation "
  "d’idées chez Romer, l’investissement en capital humain chez Lucas, "
  "l’investissement public en infrastructures chez Barro. Aghion et Howitt "
  "ajoutent un mécanisme concurrentiel : l’innovation résulte d’une course où "
  "la perspective d’un monopole temporaire finance la recherche. La conséquence "
  "de politique économique est directe et doit être soulignée : si le progrès "
  "technique est endogène, alors l’éducation, la recherche et les "
  "infrastructures ne sont pas des dépenses de confort mais les déterminants du "
  "taux de croissance de long terme.",
  [("L’invention et l’innovation",
    "L’invention est la découverte d’un principe nouveau ; l’innovation son "
    "application économique. Seule la seconde produit des effets sur la "
    "production, ce qui explique les délais entre découverte et croissance."),
   ("L’incorporation dans le capital",
    "Une partie du progrès technique ne se diffuse qu’à travers les équipements "
    "nouveaux. Le renouvellement du stock de capital est donc le vecteur "
    "matériel de la diffusion technique."),
   ("Les externalités de connaissance",
    "Une innovation profite au-delà de celui qui l’a financée, puisque les "
    "connaissances se diffusent. L’investisseur privé ne captant pas tout le "
    "rendement, il sous-investit : d’où la justification d’un soutien public."),
   ("La course à l’innovation",
    "La perspective d’un monopole temporaire sur une innovation finance l’effort "
    "de recherche. L’innovation suivante détruit cette rente, ce qui enclenche "
    "une dynamique de remplacement continu."),
   ("Le biais du progrès technique",
    "Le progrès technique n’est pas neutre : il peut accroître davantage la "
    "demande de travail qualifié que celle de travail peu qualifié, ce qui "
    "modifie la distribution des revenus.")],
  [{'a': "Le progrès technique est la seule source de croissance durable du "
         "produit par tête, puisque l’accumulation de capital s’épuise.",
    'cond': "Il faut un flux continu d’innovations et une capacité de l’économie "
            "à les absorber, donc une main-d’œuvre formée et des institutions "
            "favorables.",
    'lim': "Son rythme n’est pas garanti : Robert Gordon soutient que les "
           "innovations récentes ont une efficacité productive moindre que "
           "celles des révolutions industrielles antérieures."},
   {'a': "Son caractère endogène rend la croissance de long terme sensible aux "
         "politiques publiques d’éducation, de recherche et d’infrastructures.",
    'cond': "L’argument suppose l’existence d’externalités et de rendements non "
            "décroissants dans l’accumulation de ces capitaux particuliers.",
    'lim': "Il implique aussi que les écarts de croissance entre pays peuvent "
           "devenir permanents : sans convergence automatique, les retards "
           "peuvent se creuser."},
   {'a': "Le progrès technique élève le niveau de vie par la baisse des prix "
         "relatifs des biens produits, au bénéfice de tous les acheteurs.",
    'cond': "La baisse des coûts doit être répercutée, ce qui suppose une "
            "concurrence suffisante en aval.",
    'lim': "Il déplace simultanément la structure de l’emploi et peut "
           "déqualifier des compétences, ce qui concentre les coûts sur certains "
           "groupes."}],
  [{'t': "Traiter le progrès technique comme exogène équivaut à renoncer à "
         "l’expliquer, donc à renoncer à agir sur la croissance.",
    'qui': "Critique adressée au modèle de Solow par les théories de la "
           "croissance endogène.",
    'rep': "La critique est juste et historiquement féconde : c’est elle qui "
           "produit les modèles de Romer, Lucas et Barro, qui décomposent le "
           "résidu en décisions économiques identifiables."},
   {'t': "Le progrès technique récent produit moins de gains de productivité que "
         "celui des révolutions industrielles précédentes.",
    'qui': "Robert Gordon, dans son analyse du ralentissement de la "
           "productivité.",
    'rep': "Le diagnostic est discuté : on peut y opposer le délai de diffusion "
           "des technologies générales et les difficultés de mesure dans les "
           "services, mais il est empiriquement étayé."},
   {'t': "Le progrès technique n’est pas neutre socialement : il peut accroître "
         "les inégalités en favorisant le travail qualifié.",
    'qui': "Daron Acemoglu, pour qui les technologies ne sont pas neutres.",
    'rep': "L’objection déplace utilement le débat de l’efficacité vers la "
           "répartition : le progrès technique élève le revenu global et peut "
           "simultanément dégrader la position relative de certains groupes."}],
  [{'n': "Robert Solow",
    'i': "Le progrès technique est le déterminant de la croissance de long "
         "terme, mais il reste exogène au modèle.",
    'p': "Solow le décrit comme une « manne tombée du ciel » : une richesse qui "
         "apparaît sans explication. La formule résume la force du résultat et "
         "la faiblesse du modèle."},
   {'n': "Paul Romer",
    'i': "La recherche et développement et les idées sont des moteurs internes "
         "de la croissance.",
    'p': "Les connaissances se cumulent sans se détruire et se diffusent, ce qui "
         "leur confère des rendements non décroissants : l’investissement dans "
         "la recherche peut donc soutenir une croissance durable."},
   {'n': "Philippe Aghion",
    'i': "La croissance par destruction créatrice dépend de la recherche et "
         "développement et de la concurrence.",
    'p': "La perspective d’une rente temporaire finance l’innovation, et la "
         "concurrence détermine l’intensité de l’incitation : le rythme du "
         "progrès technique devient donc une variable de politique économique."},
   {'n': "Peter Howitt",
    'i': "L’innovation verticale améliore la qualité d’un produit existant "
         "et procure un monopole temporaire à son auteur.",
    'p': "Chaque innovation améliore la qualité d’un produit existant et "
         "procure à son auteur un monopole provisoire, détruit par l’innovation "
         "suivante : le progrès technique est un processus de remplacement "
         "continu."}],
  [{'f': "Solow parlait du progrès technique comme d’une « manne tombée du "
         "ciel », c’est-à-dire d’une richesse apparaissant sans que le modèle en "
         "rende compte.",
    'p': "La formule est la citation la plus efficace pour caractériser le "
         "statut du progrès technique avant les théories endogènes."},
   {'f': "Environ 60 % de la croissance française des Trente Glorieuses "
         "s’explique par la productivité globale des facteurs, qui approche le "
         "progrès technique.",
    'p': "L’ordre de grandeur montre que le progrès technique n’est pas un "
         "facteur secondaire mais le déterminant principal de la croissance "
         "observée."},
   {'f': "Les théories de la croissance endogène se développent dans les années "
         "1980 en expliquant le progrès technique par l’innovation, la recherche "
         "et développement et le capital humain.",
    'p': "La datation permet de présenter l’endogénéisation comme une réponse "
         "théorique à une insuffisance identifiée, et non comme une simple "
         "alternative."}],
  [{'q': "Sujet du type « La croissance peut-elle s’entretenir elle-même ? »",
    'f': "La réponse dépend entièrement du statut accordé au progrès technique. "
         "Exogène, il fait de la croissance de long terme une donnée extérieure "
         "sur laquelle nulle politique n’agit ; endogène, il la transforme en "
         "résultat de décisions d’investissement en recherche, en éducation et "
         "en infrastructures.",
    'r': "Faire du statut du progrès technique le pivot du devoir permet de "
         "présenter Solow et les théories endogènes comme deux réponses à une "
         "même question, au lieu de les juxtaposer.",
    'ex': "La « manne tombée du ciel » de Solow face aux modèles de Romer, Lucas "
          "et Barro."},
   {'q': "Sujet du type « L’innovation profite-t-elle à tous ? »",
    'f': "Le progrès technique élève le revenu global et peut simultanément "
         "dégrader la position relative de certains groupes, parce qu’il n’est "
         "pas neutre : il modifie la demande relative de qualifications. "
         "L’effet agrégé et l’effet distributif doivent donc être traités "
         "séparément.",
    'r': "On distingue les deux niveaux dès l’introduction, ce qui évite la "
         "contradiction apparente entre enrichissement collectif et "
         "contestation sociale.",
    'ex': "Acemoglu montre que les technologies ne sont pas neutres dans leurs "
          "effets sur les qualifications."}],
  voisins=['n1-pgf', 'n1-endogene', 'n1-rd', 'n1-productivite',
           'n1-croissance', 'n1-stagnation'])
