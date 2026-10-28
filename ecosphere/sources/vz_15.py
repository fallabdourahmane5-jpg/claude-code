# -*- coding: utf-8 -*-
"""Visualisation 15 — Le travail, l’emploi et le chômage (type flux)."""

from vz_base import v, nd, ln

v('vz-travail', 'Le travail, l’emploi et le chômage',
  'Chapitres 8 et 10 · du statut au diagnostic du chômage',
  'flux',
  "Le travail n’est pas qu’un revenu, l’emploi n’est pas qu’un contrat, et "
  "le chômage n’a pas une cause unique. Cette visualisation se lit de gauche "
  "à droite : ce qu’est le travail et ce qu’apporte l’emploi, comment on "
  "l’analyse comme un marché, les formes du chômage, les politiques qui en "
  "découlent, et les transformations qui déplacent le problème.",
  [("Toujours commencer par le diagnostic",
    "Keynésien ou classique, conjoncturel ou structurel : le choix de la "
    "politique découle entièrement du diagnostic. Malinvaud fournit le "
    "critère — quel côté du marché est le côté court."),
   ("Le statut avant le salaire",
    "Le cours insiste : le travail joue un rôle essentiel dans l’identité, "
    "l’intégration sociale et l’appartenance à un collectif. La chronologie "
    "des protections montre que la condition salariale est une construction "
    "juridique, pas une propriété du marché."),
   ("Ce qui est flexibilité pour l’un est incertitude pour l’autre",
    "La même mesure se lit comme adaptation pour l’entreprise et comme "
    "risque transféré pour le salarié. Garder les deux lectures évite les "
    "copies à sens unique.")],
  [
   # ------------------------------------ colonne 1 : travail, emploi, statut
   nd('travail', 'Travail et emploi : deux notions', 'pilier',
      "Le travail est l’activité ; l’emploi, le statut et les droits qui s’y "
      "attachent. Le travail n’est pas qu’un revenu : il intègre.",
      grp=1,
      defi="Le travail désigne l’activité productive elle-même ; l’emploi, le "
           "statut dans lequel elle s’exerce et les droits qui s’y attachent. "
           "Le cours insiste sur le fait que le travail ne sert pas seulement "
           "à obtenir un revenu : il joue un rôle essentiel dans l’identité "
           "individuelle, l’intégration sociale, l’appartenance à un "
           "collectif et la construction des relations sociales.",
      mec=[("La fonction intégratrice",
            "Le travail relie les individus entre eux, les intègre dans des "
            "groupes et crée de l’interdépendance : sa disparition ne retire "
            "pas seulement un revenu mais une position."),
           ("Le statut attaché au salariat",
            "La société salariale associe au salaire un statut, des droits, "
            "une protection sociale et une place dans la société : c’est "
            "l’emploi, et non le travail, qui ouvre ces droits."),
           ("La désaffiliation",
            "La perte d’emploi enclenche un processus qui prive l’individu de "
            "ses appartenances successives : le chômage se double d’un "
            "délitement des liens.")],
      aut=[{'n': "Émile Durkheim",
            'i': "Le travail relie les individus entre eux, les intègre dans "
                 "des groupes et crée de l’interdépendance."},
           {'n': "Robert Castel",
            'i': "La société salariale associe au salaire un statut, des "
                 "droits, une protection sociale et une place dans la "
                 "société."}],
      faits=[{'f': "En 2025, quatre-vingt-six virgule cinq pour cent des "
                   "personnes en emploi sont salariées, contre treize virgule "
                   "cinq pour cent d’indépendants.",
              'p': "Le chiffre établit que le salariat est la forme très "
                   "largement dominante de l’emploi, ce qui donne au statut "
                   "salarial son importance décisive pour l’accès aux "
                   "droits."}],
      termes=['travail et emploi', 'salariat', 'societe salariale'],
      dos=['n10-travail-emploi', 'n10-population-active']),

   nd('protections', 'La construction juridique de l’emploi', 'detail',
      "Grève en 1864, syndicats en 1884, accidents du travail en 1898, "
      "Matignon en 1936, Sécurité sociale en 1945 : une accumulation de "
      "conquêtes.",
      grp=1, par='travail',
      defi="La condition salariale contemporaine résulte d’une accumulation "
           "de conquêtes juridiques, et non d’une propriété spontanée du "
           "marché du travail. Le cours en jalonne la chronologie : droit de "
           "grève en 1864, légalisation des syndicats en 1884, loi sur les "
           "accidents du travail en 1898, repos hebdomadaire en 1906, accords "
           "Matignon en 1936, Sécurité sociale en 1945, trente-cinq heures en "
           "1998.",
      mec=[("Le passage de la faute au risque",
            "La loi de 1898 sur les accidents du travail fait cesser de "
            "considérer l’accident comme une faute personnelle du salarié : "
            "le déplacement de la responsabilité fonde la protection sociale "
            "moderne."),
           ("La reconnaissance du collectif",
            "La légalisation des syndicats et le droit de grève transforment "
            "la relation de travail : la négociation cesse d’être un "
            "face-à-face entre un employeur et un individu isolé.")],
      args=[{'a': "La chronologie démontre que ce qui apparaît comme le "
                  "fonctionnement normal du marché du travail est en réalité "
                  "un encadrement construit par étapes.",
             'lim': "Une construction peut se défaire : le cours relève que "
                    "la condition salariale s’effrite avec la montée du "
                    "chômage et de la précarité."}],
      aut=[{'n': "Robert Castel",
            'i': "La perte d’emploi enclenche un processus de désaffiliation "
                 "qui prive l’individu de ses appartenances."}],
      termes=['protection sociale', 'syndicats', 'droit du travail'],
      dos=['n22-protection-sociale', 'n10-precarite']),

   # ------------------------------------------ colonne 2 : le marché du travail
   nd('marche', 'Un marché comme les autres ?', 'pilier',
      "Offre croissante, demande décroissante, salaire d’équilibre — sauf "
      "que Keynes rejette explicitement cette lecture.",
      grp=2,
      defi="Le marché du travail est le lieu de rencontre entre une offre de "
           "travail émanant des ménages et une demande de travail émanant des "
           "entreprises, dont la confrontation détermine le salaire et le "
           "niveau d’emploi. Le cours en fait immédiatement un objet de "
           "controverse : Keynes rejette explicitement l’idée que le travail "
           "soit un marché comme les autres.",
      mec=[("Le schéma standard",
            "Offre de travail croissante avec le salaire, demande de travail "
            "décroissante, et salaire fixé à un niveau minimum par les "
            "conventions, le salaire minimum, les rigidités et la négociation "
            "collective."),
           ("D’où vient alors le chômage involontaire",
            "Dans ce cadre, il ne vient pas d’un refus de travailler mais "
            "d’un prix qui ne s’ajuste pas à la baisse : le chômage est un "
            "déséquilibre de prix."),
           ("L’ajustement par les quantités",
            "Dans la théorie du déséquilibre, les prix et les salaires sont "
            "rigides, l’ajustement se fait par les quantités — production et "
            "emploi — et le rationnement est possible, donc durable.")],
      opp=[{'t': "Le travail est un marché comme les autres, analysable avec "
                 "les mêmes outils que le marché des biens.",
            'qui': "lecture microéconomique",
            'rep': "Keynes conteste précisément ce point : les salaires sont "
                   "rigides à la baisse et la demande de travail dépend des "
                   "débouchés anticipés par les entrepreneurs, non des seules "
                   "conditions d’embauche."}],
      aut=[{'n': "John Maynard Keynes",
            'i': "Le travail n’est pas un marché comme les autres, et les "
                 "salaires sont rigides à la baisse."},
           {'n': "Robert Clower",
            'i': "Il faut distinguer la demande notionnelle, ce que les "
                 "agents voudraient faire, de la demande effective, ce "
                 "qu’ils peuvent réellement faire."}],
      termes=['marche du travail', 'offre de travail', 'rigidite des salaires'],
      dos=['n10-marche-travail', 'n26-salaire-cout-revenu']),

   nd('salaire', 'Le salaire : coût ou revenu ?', 'detail',
      "Pour l’entreprise un coût à comprimer, pour l’économie un revenu qui "
      "soutient la demande. Le salaire minimum est un prix plancher.",
      grp=2, par='marche',
      defi="Le salaire occupe une position double qui explique la plupart des "
           "désaccords : il est un coût de production pour l’entreprise qui "
           "le verse, et un revenu qui alimente la demande pour l’économie "
           "prise dans son ensemble. Le salaire minimum interprofessionnel de "
           "croissance en est l’illustration la plus nette : une entreprise "
           "ne doit pas payer moins, et le cours l’analyse comme un prix "
           "plancher qui s’impose au marché.",
      mec=[("La lecture par le coût",
            "Un salaire supérieur au prix d’équilibre réduit la quantité de "
            "travail demandée : c’est le raisonnement du prix plancher, "
            "appliqué au marché du travail comme au marché des biens."),
           ("La lecture par le revenu",
            "La baisse des salaires ne supprime pas le chômage et peut même "
            "aggraver la crise en réduisant la demande : ce qui est une "
            "économie pour une entreprise est une perte de débouchés pour "
            "toutes."),
           ("Le rôle des cotisations",
            "Le salaire brut diffère du salaire super brut, coût total pour "
            "l’employeur, par les cotisations patronales : le coût du travail "
            "au niveau du salaire minimum dépend autant du barème que du "
            "salaire lui-même.")],
      faits=[{'f': "Les allègements de cotisations concentrés autour du "
                   "salaire minimum créent un risque de trappe à bas "
                   "salaires, puisqu’une augmentation de salaire fait "
                   "disparaître progressivement les exonérations.",
              'p': "Le mécanisme démontre qu’un dispositif destiné à soutenir "
                   "l’emploi peut freiner la progression salariale qu’il "
                   "devrait accompagner."},
             {'f': "L’Allemagne introduit un salaire minimum légal généralisé "
                   "le premier janvier 2015, après une modération salariale "
                   "ayant contribué au développement d’emplois faiblement "
                   "rémunérés.",
              'p': "Le cas montre qu’un pays peut juger le coût social de "
                   "l’absence de salaire minimum supérieur à son avantage "
                   "compétitif."}],
      termes=['salaire minimum', 'cout du travail', 'prix plancher'],
      dos=['n10-salaire-minimum', 'n26-salaire-cout-revenu']),

   # --------------------------------------------- colonne 3 : formes du chômage
   nd('formes', 'Conjoncturel ou structurel', 'pilier',
      "L’un se résorbe avec la reprise, l’autre subsiste indépendamment de la "
      "conjoncture. Et un chômage conjoncturel durable devient structurel.",
      grp=3,
      defi="Le chômage conjoncturel est celui qui résulte d’un ralentissement "
           "temporaire de l’activité et que la reprise résorbe ; le chômage "
           "structurel est celui qui subsiste indépendamment de la "
           "conjoncture, parce qu’il est inscrit dans les structures de "
           "l’économie. Le cours rattache le premier à l’insuffisance de la "
           "demande effective, et le second à plusieurs mécanismes durables.",
      mec=[("L’équilibre de sous-emploi",
            "Les entreprises sont satisfaites de leur niveau de production, "
            "les ménages consomment ce qu’ils peuvent, les marchés sont "
            "stables — et il existe pourtant du chômage. La situation est "
            "stable, donc ne se résorbe pas mécaniquement."),
           ("Le glissement du conjoncturel au structurel",
            "Après 2008, croissance effective durablement faible, recul de la "
            "croissance potentielle, output gaps négatifs persistants, "
            "faiblesse de l’investissement et chômage durable coexistent : un "
            "chômage longtemps qualifié de conjoncturel peut relever d’un "
            "problème plus structurel."),
           ("Le désalignement démographique",
            "Si la population active augmente plus vite que les capacités "
            "productives, l’économie ne peut pas absorber toute la "
            "main-d’œuvre : le chômage structurel peut procéder d’une "
            "insuffisance de capital et non d’un défaut du marché du "
            "travail.")],
      aut=[{'n': "Milton Friedman",
            'i': "Il existe un taux de chômage naturel, incompressible, lié "
                 "aux frictions du marché du travail."},
           {'n': "Karl Marx",
            'i': "Le capitalisme entretient une surpopulation relative, "
                 "excédentaire au regard des besoins du capital."}],
      termes=['chomage conjoncturel', 'chomage structurel',
              'equilibre de sous emploi'],
      dos=['n10-chomage-conj-struct', 'n10-travail-emploi']),

   nd('malinvaud', 'Keynésien ou classique : le côté court', 'pilier',
      "Si la demande de biens est le côté court, la relance marche. Si c’est "
      "l’offre, elle alimente les prix. Le critère commande la politique.",
      grp=3,
      defi="Chez Edmond Malinvaud, le chômage est keynésien lorsque la "
           "demande de biens constitue le côté court du marché, auquel cas "
           "une relance est efficace, et classique lorsque c’est l’offre qui "
           "l’est, faute de rentabilité, auquel cas une relance alimenterait "
           "les prix. Le cours fait de cette distinction le critère qui "
           "commande le choix de la politique économique.",
      mec=[("Le principe du côté court",
            "Sur un marché en déséquilibre, la quantité échangée est "
            "déterminée par le côté le plus faible : identifier ce côté, "
            "c’est identifier la contrainte qui bloque l’emploi."),
           ("Le chômage keynésien",
            "La demande de biens est insuffisante : les capacités existent "
            "mais ne trouvent pas de débouchés. Soutenir la dépense lève "
            "directement la contrainte."),
           ("Le chômage classique",
            "L’offre est le côté court, faute de rentabilité : relancer la "
            "demande ne fait alors pas augmenter la production mais les prix, "
            "et le remède porte sur les conditions de rentabilité.")],
      aut=[{'n': "Edmond Malinvaud",
            'i': "Le chômage est keynésien lorsque la demande de biens est le "
                 "côté court du marché, et classique lorsque c’est l’offre."},
           {'n': "Axel Leijonhufvud",
            'i': "L’économie peut fonctionner durablement hors équilibre, les "
                 "marchés ne s’auto-ajustant pas."}],
      faits=[{'f': "Les années 1970 sont marquées par les chocs pétroliers de "
                   "1973 et 1979 et par une stagflation inédite associant "
                   "inflation et chômage, que la courbe de Phillips "
                   "n’expliquait pas.",
              'p': "Le fait explique le basculement vers les analyses de "
                   "l’offre : la coexistence d’inflation et de chômage "
                   "disqualifiait le diagnostic purement keynésien."}],
      termes=['chomage classique', 'chomage keynesien', 'cote court',
              'desequilibre'],
      dos=['n10-chomage-classique-keynesien', 'n13-chocs-offre-demande']),

   # ------------------------------------------- colonne 4 : les politiques
   nd('politiques', 'Agir sur la demande ou sur l’offre', 'pilier',
      "Relance, abaissement du coût du travail, formation : trois familles "
      "d’instruments, chacune pertinente pour un diagnostic différent.",
      grp=4,
      defi="Les politiques de l’emploi se rangent selon le diagnostic "
           "qu’elles supposent. Face à un chômage keynésien, elles soutiennent "
           "la demande adressée aux entreprises. Face à un chômage classique, "
           "elles agissent sur les conditions de rentabilité, notamment par "
           "les allègements de cotisations. Face à un chômage structurel "
           "d’inadéquation, elles agissent sur les qualifications et sur "
           "l’appariement entre offres et demandes.",
      mec=[("L’action sur la demande",
            "Si les capacités existent mais que les débouchés manquent, "
            "soutenir la dépense publique ou le revenu disponible relance "
            "directement la production, donc l’emploi."),
           ("L’action sur le coût du travail",
            "Si la contrainte est la rentabilité, l’abaissement du coût du "
            "travail au voisinage du salaire minimum élargit la zone où "
            "l’embauche est rentable — au risque de la trappe à bas salaires."),
           ("L’action sur les qualifications",
            "Lorsque les emplois existent mais que les compétences ne "
            "correspondent pas, seule la formation déplace la contrainte : "
            "ni la demande ni le coût ne sont en cause.")],
      args=[{'a': "Classer les instruments par le diagnostic qu’ils supposent "
                  "évite la juxtaposition de mesures et permet de justifier "
                  "un choix plutôt que d’en énumérer plusieurs.",
             'lim': "Les trois diagnostics coexistent souvent dans une même "
                    "économie, ce qui explique que les politiques réelles "
                    "combinent les instruments au risque de brouiller "
                    "l’évaluation de chacun."}],
      aut=[{'n': "John Maynard Keynes",
            'i': "La demande de travail dépend des débouchés anticipés par "
                 "les entrepreneurs et non des seules conditions d’embauche."}],
      termes=['politiques de l emploi', 'allegements de cotisations',
              'formation'],
      dos=['n15-politique-relance', 'n10-salaire-minimum']),

   nd('flexibilite', 'La flexibilité et son revers', 'limite',
      "Embaucher, licencier, modifier les horaires, recourir aux contrats "
      "temporaires : ce qui est adaptation pour l’entreprise est incertitude "
      "pour le salarié.",
      grp=4, par='politiques',
      defi="La flexibilité de l’emploi désigne la capacité pour une "
           "entreprise d’adapter rapidement la quantité ou les conditions de "
           "travail à ses besoins : facilité à embaucher, à licencier, à "
           "modifier les horaires, recours aux contrats temporaires, "
           "adaptation du temps de travail. Le cours souligne aussitôt que ce "
           "qui est flexibilité pour l’entreprise devient incertitude pour le "
           "salarié.",
      mec=[("Le transfert du risque",
            "Chacun des dispositifs déplace un risque déterminé — de volume, "
            "d’horaire, de durée — de l’entreprise vers le salarié : la "
            "flexibilité n’annule pas l’aléa, elle le réattribue."),
           ("La concentration sur certaines catégories",
            "Chez les quinze-vingt-quatre ans, seulement trente-neuf virgule "
            "huit pour cent sont en contrat à durée indéterminée en 2025 : la "
            "flexibilité se concentre, ce qui en fait un facteur d’inégalité "
            "entre générations."),
           ("La fragilité partagée",
            "Les flux tendus rendent la production plus vulnérable aux "
            "perturbations : la flexibilité expose aussi l’entreprise, et pas "
            "seulement le salarié.")],
      aut=[{'n': "Florence Aubenas",
            'i': "La précarité professionnelle produit de faibles revenus "
                 "mais aussi des difficultés d’accès à l’emploi et un "
                 "isolement social."},
           {'n': "Taiichi Ohno",
            'i': "La production doit être tirée par l’aval, ce qui exige une "
                 "organisation flexible."}],
      termes=['flexibilite', 'precarite', 'contrats temporaires'],
      dos=['n10-flexibilite', 'n10-precarite']),

   # ------------------------------------- colonne 5 : ce qui déplace le problème
   nd('transformations', 'Ce qui déplace le problème', 'debat',
      "Automatisation, polarisation, concurrence internationale : le chômage "
      "change de visage avant de changer de niveau.",
      grp=5,
      defi="Les transformations contemporaines ne modifient pas seulement le "
           "niveau du chômage mais sa composition. Le progrès technique "
           "biaisé automatise les tâches routinières et élève la demande de "
           "qualifications ; la concurrence internationale expose certaines "
           "catégories et pas d’autres. Les deux pressions frappent les mêmes "
           "travailleurs — les non-qualifiés des secteurs exposés — ce qui "
           "explique l’ampleur de leur décrochage.",
      mec=[("Le déplacement du périmètre des tâches",
            "L’automatisation substitue des machines aux tâches "
            "standardisables : le biais porte sur la nature des tâches, ce "
            "qui explique que des emplois intermédiaires soient touchés."),
           ("Le cumul avec l’exposition internationale",
            "Les mêmes tâches routinières sont à la fois délocalisables et "
            "automatisables : deux pressions indépendantes s’additionnent sur "
            "la même catégorie."),
           ("La réponse par les capacités plutôt que par le volume",
            "Si le problème est la composition des emplois et non leur "
            "nombre, la réponse relève de la formation et de la qualité des "
            "emplois plus que du soutien de la demande.")],
      aut=[{'n': "Dani Rodrik",
            'i': "La réponse au déclassement ne peut pas se limiter à la "
                 "réindustrialisation : il faut élever la qualité des emplois "
                 "de services, où se concentre l’emploi."},
           {'n': "Pierre-Noël Giraud",
            'i': "Les activités nomades sont exposées à la concurrence "
                 "mondiale, les sédentaires sont protégées par leur ancrage "
                 "territorial."}],
      termes=['polarisation des emplois', 'progres technique biaise',
              'automatisation'],
      dos=['n10-polarisation', 'n10-progres-technique-biaise']),

   nd('sens', 'Le sens du travail', 'sortie',
      "Si l’emploi donne un statut et une place, alors sa qualité compte "
      "autant que son existence : autonomie, reconnaissance, sens.",
      grp=5,
      defi="La question du sens et de la souffrance au travail prolonge "
           "directement la définition initiale : si le travail construit "
           "l’identité et l’appartenance, alors un emploi peut échouer à "
           "remplir sa fonction sociale tout en fournissant un revenu. "
           "L’autonomie laissée au salarié, la reconnaissance de sa "
           "contribution et la cohérence entre ce qu’on lui demande et ce "
           "qu’il juge bien fait deviennent des variables économiques et pas "
           "seulement morales.",
      mec=[("L’autonomie comme ressource productive",
            "Un salarié qui dispose d’une marge de décision mobilise une "
            "connaissance de la situation qu’aucune prescription ne contient : "
            "l’autonomie n’est pas une concession mais une condition "
            "d’efficacité."),
           ("L’écart entre travail prescrit et travail réel",
            "Ce que l’organisation demande ne recouvre jamais exactement ce "
            "que la situation exige : c’est dans cet écart que se logent à la "
            "fois l’initiative et la souffrance."),
           ("La qualité de l’emploi comme objectif de politique",
            "Si l’emploi vaut par le statut qu’il procure, alors une "
            "politique qui crée des emplois sans droits ni perspectives "
            "manque une partie de son objectif.")],
      args=[{'a': "Poser la question de la qualité de l’emploi évite de "
                  "réduire le problème au taux de chômage, qui ne dit rien de "
                  "ce que valent les emplois occupés.",
             'lim': "La qualité est plus difficile à mesurer que le volume, "
                    "ce qui explique que les politiques s’en tiennent "
                    "souvent au second."}],
      aut=[{'n': "Robert Castel",
            'i': "La condition salariale s’effrite avec la montée du chômage "
                 "et de la précarité."}],
      termes=['sens du travail', 'autonomie au travail',
              'souffrance au travail'],
      dos=['n9-souffrance-sens', 'n9-autonomie']),
  ],
  [
   ln('travail', 'protections', 'a été construit par',
      "Ce qui apparaît comme le fonctionnement normal du marché du travail "
      "est un encadrement construit par étapes : grève en 1864, syndicats en "
      "1884, accidents du travail en 1898, Sécurité sociale en 1945.",
      'cause'),
   ln('travail', 'marche', 'est analysé comme',
      "La microéconomie traite le travail avec les mêmes outils que les "
      "autres marchés : offre, demande, prix d’équilibre. C’est précisément "
      "ce que Keynes conteste, et le désaccord porte sur la nature de l’objet "
      "avant de porter sur les remèdes.", 'conditionne'),
   ln('protections', 'marche', 'introduit des rigidités dans',
      "Conventions, salaire minimum et négociation collective fixent un "
      "plancher : dans le schéma standard, c’est de là que vient le chômage "
      "involontaire, non d’un refus de travailler.", 'limite'),
   ln('marche', 'salaire', 'se joue sur',
      "Le salaire est la variable d’ajustement supposée du marché du travail. "
      "Sa double nature — coût pour l’entreprise, revenu pour l’économie — "
      "explique pourquoi sa baisse n’a pas l’effet attendu.", 'cause'),
   ln('salaire', 'formes', 'ne résorbe pas',
      "La baisse des salaires ne supprime pas le chômage et peut même "
      "aggraver la crise en réduisant la demande : l’ajustement par le prix "
      "échoue, ce qui oblige à distinguer les formes du chômage.", 'limite'),
   ln('marche', 'formes', 'laisse subsister',
      "L’équilibre de sous-emploi est stable : entreprises satisfaites de "
      "leur production, ménages consommant ce qu’ils peuvent, marchés "
      "stables — et du chômage malgré tout.", 'cause'),
   ln('formes', 'malinvaud', 'se précise par',
      "Conjoncturel et structurel décrivent la durée ; keynésien et classique "
      "désignent la cause. Malinvaud fournit le critère opératoire : quel "
      "côté du marché est le côté court.", 'mesure'),
   ln('malinvaud', 'politiques', 'commande le choix des',
      "Si la demande de biens est le côté court, la relance est efficace ; si "
      "c’est l’offre, elle alimente les prix. Le diagnostic détermine "
      "entièrement l’instrument.", 'conditionne'),
   ln('formes', 'politiques', 'oriente aussi',
      "Un chômage structurel d’inadéquation ne se traite ni par la demande ni "
      "par le coût : seule la formation déplace la contrainte, ce qui en fait "
      "une troisième famille d’instruments.", 'conditionne'),
   ln('politiques', 'flexibilite', 'passe souvent par',
      "L’assouplissement des conditions d’embauche et de licenciement est "
      "présenté comme un moyen d’abaisser le coût implicite de l’embauche. "
      "L’argument relève du diagnostic classique, non du diagnostic "
      "keynésien.", 'cause'),
   ln('flexibilite', 'travail', 'fragilise le statut',
      "Ce qui est flexibilité pour l’entreprise devient incertitude pour le "
      "salarié : la condition salariale s’effrite, et avec elle les droits et "
      "la place que l’emploi procurait.", 'limite'),
   ln('transformations', 'formes', 'change la composition du chômage',
      "Automatisation des tâches routinières et exposition internationale "
      "frappent la même catégorie : le chômage change de visage — plus "
      "concentré, plus durable — avant même de changer de niveau.", 'cause'),
   ln('transformations', 'politiques', 'déplace les instruments',
      "Si le problème est la composition des emplois et non leur nombre, la "
      "réponse relève de la formation et de la qualité des emplois plus que "
      "du soutien de la demande.", 'conditionne'),
   ln('flexibilite', 'sens', 'pose la question de la qualité',
      "Un emploi peut fournir un revenu sans procurer le statut, la "
      "perspective et la reconnaissance qui en font une place dans la "
      "société : le volume ne dit rien de ce que valent les emplois occupés.",
      'cause'),
   ln('sens', 'travail', 'renvoie à la définition initiale',
      "Si le travail construit l’identité et l’appartenance, alors sa qualité "
      "fait partie de ce qu’on attend de lui : la boucle revient au point de "
      "départ du chapitre.", 'renforce'),
  ],
  bandes=[(1, 'Travail, emploi, statut'), (2, 'Le marché du travail'),
          (3, 'Les formes du chômage'), (4, 'Les politiques'),
          (5, 'Ce qui déplace le problème')],
  fam='Innovation, travail et entreprise')
