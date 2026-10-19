# -*- coding: utf-8 -*-
"""Ensemble 5 — Le marché, les prix et la concurrence (4/4)."""

from doss_base import d

d('n5-ententes', 5, "Ententes",
  "S’accorder plutôt que se concurrencer — une pratique efficace et instable",
  "Une entente est un accord entre plusieurs entreprises visant à limiter la "
  "concurrence ; lorsqu’elle est organisée et durable, on parle de cartel. "
  "Elle permet de maintenir des prix élevés, de protéger les profits et de se "
  "partager les marchés, mais elle demeure instable puisque chaque entreprise "
  "a individuellement intérêt à tricher pour augmenter ses gains.",
  "L’entente est la pratique anticoncurrentielle la plus étudiée par le cours, "
  "et son intérêt théorique vient de ce qu’elle réunit un raisonnement "
  "stratégique, un exemple historique précis et un dispositif juridique de "
  "lutte. Le raisonnement d’abord : dans un oligopole, deux issues sont "
  "possibles, la concurrence qui entraîne une guerre des prix et des profits "
  "faibles, ou la collusion qui permet des prix plus élevés et des profits "
  "plus importants. L’entente est donc collectivement rentable pour ses "
  "membres, mais chacun a individuellement intérêt à tricher : on retrouve "
  "exactement la logique du dilemme du prisonnier, la coopération étant "
  "collectivement préférable tandis que la rationalité individuelle pousse à "
  "la défection. L’exemple historique ensuite : le cartel de Phoebus réunit "
  "General Electric, Osram et Philips, principalement de 1929 à 1939. Il vise "
  "à limiter la concurrence, maintenir des prix élevés, protéger les profits "
  "et se partager les marchés ; pour cela les entreprises fixent des quotas de "
  "production et se répartissent géographiquement les marchés. Le raisonnement "
  "économique est explicite : si la production devient trop importante, "
  "l’offre augmente, les prix chutent et les profits diminuent. Le cartel va "
  "plus loin en réduisant volontairement la durée de vie des ampoules, "
  "d’environ 2000 heures vers 1910 à environ 1000 heures, pour pousser les "
  "consommateurs à racheter davantage : c’est l’exemple célèbre d’obsolescence "
  "programmée. Le dispositif juridique enfin. Les cartels sont généralement "
  "condamnés parce qu’ils entraînent des prix plus élevés, une réduction des "
  "quantités, une baisse du bien-être des consommateurs, une limitation de "
  "l’innovation et un partage artificiel du marché. Comme ils sont souvent "
  "secrets, les autorités utilisent la procédure de clémence, qui réduit voire "
  "supprime la sanction d’une entreprise qui dénonce le cartel : elle "
  "renforce ainsi l’instabilité déjà mise en évidence par le dilemme du "
  "prisonnier. Mais toutes les ententes ne sont pas illégales : les autorités "
  "distinguent les ententes anticoncurrentielles des coopérations économiques "
  "légitimes.",
  [("L’intérêt collectif des membres",
    "En s’entendant, les entreprises reproduisent à plusieurs le comportement "
    "d’un monopoleur : elles restreignent la quantité offerte, ce qui maintient "
    "les prix et protège leurs profits."),
   ("L’incitation individuelle à la défection",
    "Chaque membre gagnerait davantage en produisant plus que sa part tandis "
    "que les autres respectent l’accord : l’entente est donc rentable "
    "collectivement et vulnérable individuellement."),
   ("La stabilisation par des règles explicites",
    "Pour tenir, l’entente se dote de quotas de production et d’une "
    "répartition géographique des marchés : ces règles rendent la tricherie "
    "observable, ce qui est la condition de la durée."),
   ("L’extension à la qualité",
    "La collusion peut porter sur autre chose que le prix : réduire "
    "volontairement la durée de vie d’un produit augmente la fréquence des "
    "achats, ce qui est une restriction de concurrence par la qualité."),
   ("La fragilisation par la clémence",
    "La procédure de clémence réduit ou supprime la sanction de celui qui "
    "dénonce : chaque membre doit alors se demander si un autre va le "
    "précéder, ce qui ajoute une raison de rompre l’accord.")],
  [{'a': "L’analyse par le dilemme du prisonnier explique pourquoi les "
         "ententes se forment et pourquoi elles se défont.",
    'cond': "Le raisonnement suppose que les entreprises ne puissent pas "
            "s’engager de façon crédible ni surveiller parfaitement les "
            "autres.",
    'lim': "Un cartel doté de quotas et d’une répartition des marchés "
           "surmonte partiellement cette difficulté, comme le montre la durée "
           "du cartel de Phoebus."},
   {'a': "Le dommage causé aux consommateurs est identifiable et multiple, ce "
         "qui justifie une sanction sévère.",
    'cond': "La sanction suppose de prouver l’existence d’un accord, ce qui "
            "est difficile puisque les cartels sont souvent secrets.",
    'lim': "Cette difficulté de preuve explique que les autorités doivent "
           "recourir à des dispositifs incitatifs plutôt qu’à la seule "
           "enquête."},
   {'a': "La procédure de clémence transforme la logique stratégique du cartel "
         "en instrument de sa destruction.",
    'cond': "Elle suppose que la réduction de sanction promise soit "
            "suffisamment attractive pour l’emporter sur le gain attendu de "
            "l’entente.",
    'lim': "Elle peut profiter à l’entreprise la plus habile plutôt qu’à la "
           "moins fautive, puisque le premier à dénoncer obtient le meilleur "
           "traitement."},
   {'a': "La distinction entre entente anticoncurrentielle et coopération "
         "légitime évite de sanctionner des accords utiles.",
    'cond': "La distinction suppose un examen au cas par cas de l’objet et des "
            "effets de la coordination.",
    'lim': "Cette appréciation laisse une marge d’interprétation importante, "
           "le cours notant que les autorités adoptent parfois une position "
           "plus nuancée."}],
  [{'t': "Les ententes sont intrinsèquement instables, et donc finalement "
         "peu dangereuses dans la pratique des marchés.",
    'qui': "La lecture par le dilemme du prisonnier, selon laquelle chacun a "
           "intérêt à tricher.",
    'rep': "L’exemple contredit la conclusion : le cartel de Phoebus a tenu "
           "principalement de 1929 à 1939, grâce à des quotas de production et "
           "à une répartition géographique des marchés."},
   {'t': "Toute coordination entre entreprises doit être interdite, puisqu’elle "
         "réduit la concurrence.",
    'qui': "La lecture stricte du droit des ententes.",
    'rep': "Le cours écarte cette position : les autorités distinguent les "
           "ententes anticoncurrentielles des coopérations économiques "
           "légitimes, une coordination pouvant être tolérée."},
   {'t': "La sanction des cartels est inefficace, car ils sont secrets et donc "
         "difficiles à prouver.",
    'qui': "La difficulté probatoire que le cours souligne.",
    'rep': "La procédure de clémence répond précisément à cette objection en "
           "retournant la logique interne du cartel : elle incite les membres "
           "à dénoncer pour éviter la sanction."},
   {'t': "Les ententes ne portent que sur les prix, et les autres pratiques "
         "relèvent d’une logique différente.",
    'qui': "Une lecture restrictive de la collusion.",
    'rep': "L’exemple de Phoebus démontre le contraire : la réduction "
           "volontaire de la durée de vie des ampoules est une restriction de "
           "concurrence qui passe par la qualité, non par le prix."}],
  [{'n': "Joseph Schumpeter",
    'i': "Le développement du capitalisme conduit à l’effacement des "
         "innovateurs individuels au profit des grandes firmes "
         "oligopolistiques.",
    'p': "Le cours relie cette dynamique aux pratiques de restriction de "
         "concurrence : à mesure que les entreprises grossissent et que les "
         "marchés se concentrent, certaines cherchent non pas à affronter la "
         "concurrence mais à la réduire afin de préserver leurs profits."},
   {'n': "Mancur Olson",
    'i': "Un agent peut bénéficier des avantages d’une action collective sans "
         "en supporter le coût.",
    'p': "Son paradoxe de l’action collective éclaire la structure de "
         "l’entente : le membre qui triche profite des prix élevés maintenus "
         "par les autres tout en vendant davantage, ce qui est exactement un "
         "comportement de passager clandestin."},
   {'n': "Joe Bain",
    'i': "La structure du marché détermine les comportements des entreprises.",
    'p': "Avec Edward Mason, il formalise le modèle SCP dans les années 1950. "
         "Appliqué aux ententes, le schéma explique pourquoi la collusion "
         "apparaît dans les marchés concentrés : c’est la structure qui rend "
         "l’accord possible et surveillable."}],
  [{'f': "Le cours définit le cartel comme une entente entre plusieurs "
         "entreprises visant à limiter la concurrence.",
    'p': "La définition met l’objet de l’accord au centre, ce qui permet de "
         "distinguer le cartel d’une coopération poursuivant un autre but."},
   {'f': "Le cartel de Phoebus réunit General Electric, Osram et Philips, "
         "principalement de 1929 à 1939, avec des quotas de production et une "
         "répartition géographique des marchés.",
    'p': "L’exemple est daté, nommé et outillé : il établit qu’une entente "
         "peut durer une décennie et s’organiser à l’échelle internationale."},
   {'f': "Vers 1910 une ampoule pouvait durer environ 2000 heures ; le cartel "
         "décide volontairement de limiter cette durée à environ 1000 heures "
         "pour pousser les consommateurs à racheter davantage.",
    'p': "Le chiffre fournit l’exemple canonique d’obsolescence programmée et "
         "montre que la collusion peut porter sur la qualité."},
   {'f': "La procédure de clémence consiste à réduire voire supprimer la "
         "sanction d’une entreprise qui dénonce le cartel, celle-ci pouvant "
         "obtenir une baisse d’amende ou une exonération complète.",
    'p': "Le dispositif est l’illustration la plus nette d’une politique "
         "publique construite sur un raisonnement de théorie des jeux."}],
  [{'q': "Sujet du type « Les entreprises ont-elles intérêt à se faire "
         "concurrence ? »",
    'f': "Non, et c’est précisément le problème. Dans un oligopole, la "
         "concurrence entraîne une guerre des prix et des profits faibles, "
         "tandis que la collusion permet des prix plus élevés et des profits "
         "plus importants. L’entente est donc collectivement rentable pour ses "
         "membres. Mais chaque entreprise a individuellement intérêt à tricher "
         "pour augmenter ses gains : on retrouve la logique du dilemme du "
         "prisonnier, où la coopération serait collectivement préférable mais "
         "où la rationalité individuelle pousse à la défection.",
    'r': "Le raisonnement montre que l’intérêt des entreprises et celui des "
         "consommateurs divergent frontalement, ce qui fonde la nécessité d’une "
         "politique de concurrence et non d’une simple confiance au marché.",
    'ex': "Le cartel de Phoebus, qui fixait des quotas de production pour "
          "éviter que la hausse de l’offre ne fasse chuter les prix."},
   {'q': "Sujet du type « Comment lutter contre les pratiques "
         "anticoncurrentielles ? »",
    'f': "La difficulté est probatoire, les cartels étant souvent secrets. "
         "D’où un outil essentiel : la procédure de clémence, qui réduit voire "
         "supprime la sanction d’une entreprise qui dénonce l’entente, "
         "celle-ci pouvant obtenir une baisse d’amende ou une exonération "
         "complète. L’effet économique est décisif, puisque chaque entreprise "
         "doit se demander si les autres respecteront l’accord ou si l’une "
         "d’elles dénoncera le cartel : la procédure renforce ainsi "
         "l’instabilité déjà mise en évidence par le dilemme du prisonnier.",
    'r': "Le raisonnement montre qu’une politique publique peut être conçue "
         "pour exploiter la logique stratégique des agents plutôt que pour la "
         "contrarier, ce qui en fait un exemple de régulation incitative.",
    'ex': "Le choix offert à chaque membre du cartel entre respecter l’accord "
          "et dénoncer pour éviter la sanction."}],
  voisins=['n5-oligopole', 'n5-politique-concurrence', 'n5-concentration',
           'n5-pouvoir-marche'])


d('n5-discrimination', 5, "Discrimination par les prix",
  "Faire payer chacun selon sa sensibilité au prix",
  "La discrimination par les prix, que le cours désigne par le monopole "
  "discriminant et la tarification différentielle, consiste à pratiquer des "
  "prix différents selon les consommateurs. L’entreprise cherche à faire payer "
  "chacun selon sa disposition à payer, son élasticité-prix, son besoin, son "
  "moment d’achat ou son profil. On parle aussi de yield management.",
  "La discrimination par les prix prolonge l’analyse du monopole en montrant "
  "que le pouvoir de marché ne se traduit pas seulement par un prix unique "
  "élevé, mais peut prendre une forme plus fine et plus rentable encore. Le "
  "cours part d’un constat simple : tous les consommateurs n’ont pas la même "
  "sensibilité au prix. L’entreprise cherche donc à repérer ceux qui sont très "
  "sensibles et ceux qui le sont peu. Si la demande est peu élastique, elle "
  "peut augmenter le prix car le consommateur ne renonce pas facilement ; si "
  "elle est très élastique, elle doit maintenir un prix plus bas pour éviter "
  "le renoncement. La tarification différentielle repose donc entièrement sur "
  "l’élasticité-prix de la demande : les consommateurs peu sensibles au prix "
  "paient davantage, tandis que les consommateurs plus sensibles bénéficient "
  "de prix plus bas. L’exemple du cours est le cinéma, avec des séances moins "
  "chères le matin et plus chères aux horaires demandés. Le point le plus "
  "intéressant est le jugement porté sur la pratique : elle peut sembler "
  "injuste, mais elle n’est pas nécessairement condamnable. Le droit de la "
  "concurrence adopte à cet égard une position nuancée que le cours expose : "
  "certaines entreprises traitent différemment leurs clients en adaptant les "
  "prix selon le type de client, sa localisation, son revenu, son comportement "
  "ou sa disposition à payer, et cela peut être ambigu ; certaines "
  "discriminations sont interdites, mais certaines formes de tarification "
  "différenciée sont autorisées lorsqu’elles améliorent l’accès au marché ou "
  "ne nuisent pas au consommateur. Le critère n’est donc pas l’égalité des "
  "prix mais l’effet sur le consommateur et sur l’accès au marché. Il faut "
  "enfin distinguer, comme le fait le cours, la discrimination économique du "
  "dénigrement concurrentiel : une entreprise n’a pas le droit de discréditer "
  "injustement ses concurrents, alors que la publicité comparative est "
  "autorisée en France depuis 1992 si elle est objective, vérifiable, non "
  "mensongère et non diffamatoire.",
  [("L’hétérogénéité des dispositions à payer",
    "Tous les consommateurs ne valorisent pas le bien de la même façon : un "
    "prix unique laisse donc du surplus à ceux qui auraient payé davantage et "
    "exclut ceux qui auraient payé moins."),
   ("Le repérage par l’élasticité",
    "L’entreprise cherche à identifier les consommateurs très sensibles au "
    "prix et ceux qui le sont peu : c’est cette segmentation qui rend la "
    "tarification différenciée possible."),
   ("La tarification par segment",
    "Aux consommateurs peu élastiques, l’entreprise applique un prix élevé "
    "puisqu’ils ne renoncent pas ; aux plus élastiques, un prix plus bas pour "
    "éviter qu’ils n’abandonnent l’achat."),
   ("Le recours à des critères observables",
    "Faute de connaître directement la disposition à payer, l’entreprise "
    "utilise des indices : moment d’achat, profil, localisation, comportement, "
    "qui sont corrélés à la sensibilité au prix."),
   ("L’effet ambigu sur le bien-être",
    "La discrimination capte du surplus du consommateur peu élastique, mais "
    "elle permet aussi de servir des consommateurs que le prix unique aurait "
    "exclus, ce qui peut améliorer l’accès au marché.")],
  [{'a': "La discrimination permet de servir des consommateurs qu’un prix "
         "unique élevé aurait exclus du marché.",
    'cond': "Le gain d’accès suppose que le prix bas proposé au segment "
            "élastique couvre au moins le coût marginal du service rendu.",
    'lim': "L’accès amélioré pour les uns se paie par un prix plus élevé pour "
           "les autres, de sorte que l’effet net sur le bien-être est "
           "difficile à établir."},
   {'a': "Elle est économiquement rationnelle et repose sur un mécanisme "
         "identifiable, l’élasticité-prix de la demande.",
    'cond': "La pratique suppose que l’entreprise dispose d’un pouvoir de "
            "marché, puisqu’en concurrence parfaite aucun prix différencié ne "
            "pourrait tenir.",
    'lim': "Elle est donc indissociable d’une situation de concurrence "
           "imparfaite, ce qui explique le nom de monopole discriminant."},
   {'a': "Le droit apprécie la pratique selon ses effets réels, ce qui évite "
         "d’interdire des tarifications bénéfiques.",
    'cond': "L’appréciation suppose un examen au cas par cas de l’accès au "
            "marché et du préjudice causé au consommateur.",
    'lim': "Cette souplesse rend la frontière incertaine : le cours reconnaît "
           "que la pratique peut être ambiguë et que certaines "
           "discriminations sont interdites."},
   {'a': "Elle permet de couvrir des coûts fixes élevés sans imposer à tous "
         "un prix uniforme nécessairement prohibitif.",
    'cond': "L’argument vaut surtout dans les secteurs à fortes capacités et à "
            "faible coût marginal, comme le transport ou le spectacle.",
    'lim': "Il rapproche la pratique du problème du monopole naturel, où "
           "aucune tarification uniforme ne permet à la fois l’efficacité et "
           "la viabilité."}],
  [{'t': "Faire payer des prix différents à des clients pour un même service "
         "rendu est fondamentalement injuste.",
    'qui': "L’objection intuitive que le cours relève lui-même en notant que "
           "la pratique peut sembler injuste.",
    'rep': "Le cours tempère immédiatement : la pratique n’est pas "
           "nécessairement condamnable, et certaines formes de tarification "
           "différenciée sont autorisées lorsqu’elles améliorent l’accès au "
           "marché ou ne nuisent pas au consommateur."},
   {'t': "La discrimination est une pratique d’éviction qui doit être traitée "
         "comme un abus de position dominante.",
    'qui': "La lecture par les pratiques discriminatoires que le cours range "
           "parmi les formes possibles d’abus.",
    'rep': "La qualification dépend des effets : certaines discriminations "
           "sont interdites, mais le droit admet celles qui n’évincent pas les "
           "concurrents et ne nuisent pas au consommateur."},
   {'t': "La discrimination suppose un pouvoir de marché, donc elle est le "
         "symptôme d’une concurrence insuffisante plutôt qu’une pratique en "
         "soi.",
    'qui': "La lecture qui rattache le monopole discriminant à la concurrence "
           "imparfaite.",
    'rep': "L’argument est juste analytiquement : la tarification différenciée "
           "est impossible pour un price taker, de sorte qu’elle révèle "
           "toujours une demande non parfaitement élastique."},
   {'t': "La différenciation des prix se confond avec le dénigrement des "
         "concurrents, autre forme de concurrence déloyale.",
    'qui': "La confusion que le cours prend soin d’écarter.",
    'rep': "Le cours distingue explicitement les deux : une entreprise n’a pas "
           "le droit de discréditer injustement ses concurrents, tandis que la "
           "publicité comparative est autorisée si elle est objective et "
           "vérifiable."}],
  [{'n': "Edward Chamberlin",
    'i': "La différenciation réduit l’élasticité-prix de la demande adressée à "
         "l’entreprise.",
    'p': "Son analyse fournit le fondement de la discrimination par les prix : "
         "c’est parce que les consommateurs n’ont pas la même sensibilité et "
         "que la marque réduit la substituabilité que des prix différents "
         "peuvent coexister sur un même marché."},
   {'n': "Joe Bain",
    'i': "La structure du marché détermine les comportements, dont les "
         "politiques de prix.",
    'p': "Avec Edward Mason, il formalise le modèle SCP. La discrimination y "
         "apparaît comme un comportement rendu possible par une structure "
         "donnée : elle exige une demande segmentable et un pouvoir de marché, "
         "soit deux traits structurels."},
   {'n': "Arthur Pigou",
    'i': "Le prix doit refléter ce que vaut le bien pour la société et ce "
         "qu’il coûte.",
    'p': "Sa logique de correction des prix éclaire par contraste la "
         "discrimination : celle-ci ajuste le prix non au coût mais à la "
         "disposition à payer, ce qui explique qu’elle maximise le profit sans "
         "garantir l’efficacité allocative."}],
  [{'f': "Le cours définit le monopole discriminant comme un monopole qui "
         "pratique des prix différents selon les consommateurs, en fonction de "
         "leur disposition à payer, de leur élasticité-prix, de leur besoin, "
         "de leur moment d’achat ou de leur profil.",
    'p': "L’énumération des critères montre que la pratique repose sur des "
         "indices observables plutôt que sur la connaissance directe des "
         "préférences."},
   {'f': "La tarification différentielle, aussi appelée yield management, "
         "repose sur l’élasticité-prix : les consommateurs peu sensibles "
         "paient davantage, les plus sensibles bénéficient de prix plus bas.",
    'p': "La formulation du cours résume à la fois le mécanisme et sa "
         "conséquence distributive, ce qui en fait une phrase directement "
         "mobilisable."},
   {'f': "L’exemple donné est le cinéma, avec des séances moins chères le "
         "matin et plus chères aux horaires demandés.",
    'p': "L’exemple montre que le critère utilisé est le moment d’achat, "
         "variable facilement observable et corrélée à la sensibilité au prix."},
   {'f': "La publicité comparative est autorisée en France depuis 1992, à "
         "condition d’être objective, vérifiable, non mensongère et non "
         "diffamatoire.",
    'p': "Le fait permet de distinguer la concurrence par l’information, "
         "licite, du dénigrement, illicite, et de ne pas confondre les deux "
         "avec la discrimination tarifaire."}],
  [{'q': "Sujet du type « Les entreprises doivent-elles pratiquer le même prix "
         "pour tous ? »",
    'f': "La tarification différentielle repose sur l’élasticité-prix de la "
         "demande : les consommateurs peu sensibles au prix paient davantage "
         "tandis que les plus sensibles bénéficient de prix plus bas. Cette "
         "pratique peut sembler injuste, mais le cours souligne qu’elle n’est "
         "pas nécessairement condamnable : certaines discriminations sont "
         "interdites, mais certaines formes de tarification différenciée sont "
         "autorisées lorsqu’elles améliorent l’accès au marché ou ne nuisent "
         "pas au consommateur.",
    'r': "Le raisonnement remplace un critère d’égalité formelle par un "
         "critère d’effet, ce qui permet de juger la pratique sans l’approuver "
         "ni la condamner en bloc.",
    'ex': "Les séances de cinéma moins chères le matin et plus chères aux "
          "horaires demandés."},
   {'q': "Sujet du type « Quelles sont les formes du pouvoir de marché ? »",
    'f': "Le pouvoir de marché ne consiste pas seulement à fixer un prix "
         "unique élevé : il permet aussi de faire payer différemment les "
         "consommateurs. Le monopole discriminant cherche ainsi à faire payer "
         "chacun selon sa disposition à payer, son élasticité-prix, son "
         "besoin, son moment d’achat ou son profil. Cette pratique est "
         "impossible en concurrence parfaite, où la demande adressée à la "
         "firme est parfaitement élastique.",
    'r': "Le raisonnement montre que la discrimination est un révélateur du "
         "pouvoir de marché plus sûr que le niveau du prix, puisqu’elle "
         "suppose nécessairement une demande non parfaitement élastique.",
    'ex': "Le yield management, qui ajuste le prix au moment de l’achat pour "
          "capter le surplus des acheteurs les moins sensibles."}],
  voisins=['n5-monopole', 'n5-pouvoir-marche', 'n5-concurrence-monopolistique',
           'n5-surplus'])


d('n5-contestables', 5, "Marchés contestables",
  "La menace d’entrée suffit à discipliner, même sans concurrent présent",
  "Un marché contestable est un marché sur lequel une entreprise peut entrer "
  "et sortir librement. Cela suppose l’absence de barrières à l’entrée et à la "
  "sortie, un accès possible à la technologie et l’absence de coûts "
  "irrécupérables trop importants. L’idée centrale de Baumol, Panzar et "
  "Willig est que le vrai critère de la concurrence n’est pas le nombre "
  "d’entreprises présentes mais la libre entrée et la libre sortie.",
  "La théorie des marchés contestables est la reformulation la plus élégante "
  "de la notion de concurrence, et son intérêt pour une copie est qu’elle "
  "retourne complètement le critère habituel. Le point de départ est le "
  "constat des barrières à l’entrée : le modèle de concurrence pure et "
  "parfaite suppose que les entreprises peuvent entrer et sortir librement, "
  "mais il existe fréquemment des barrières — coûts élevés, brevets, "
  "réglementations. Face à cela, certains économistes ont proposé de redéfinir "
  "la concurrence non plus par le nombre d’entreprises mais par la possibilité "
  "d’entrer et de sortir du marché. Dans les années 1980, William Baumol, John "
  "Panzar et Robert Willig développent la théorie des marchés contestables. "
  "L’idée clé est spectaculaire : même s’il n’y a qu’une seule entreprise sur "
  "le marché, elle peut se comporter comme si elle était en concurrence, parce "
  "qu’elle craint l’arrivée de concurrents. Le mécanisme est celui de la "
  "concurrence potentielle : une entreprise installée qui pratiquerait un prix "
  "élevé rendrait le marché attractif, attirerait un entrant et perdrait sa "
  "position ; elle a donc intérêt à fixer un prix proche du niveau "
  "concurrentiel pour décourager l’entrée. Les conditions sont précises et "
  "constituent l’essentiel du dossier. Il faut l’absence de barrières à "
  "l’entrée, l’absence de barrières à la sortie, un accès possible à la "
  "technologie et l’absence de coûts irrécupérables trop importants. Cette "
  "dernière condition est la plus restrictive : si entrer suppose un "
  "investissement qu’on ne pourra pas récupérer en sortant, la menace d’entrée "
  "perd sa crédibilité, et avec elle tout le mécanisme disciplinaire. La "
  "théorie a deux conséquences pratiques majeures. Elle justifie de concentrer "
  "la politique de concurrence sur les barrières à l’entrée plutôt que sur les "
  "parts de marché. Et elle éclaire le raisonnement des entreprises qui, dans "
  "un contentieux de concurrence, soutiennent que leur marché pertinent est "
  "plus large qu’il n’y paraît.",
  [("La concurrence potentielle",
    "Ce n’est pas le concurrent présent mais le concurrent possible qui "
    "discipline : l’entreprise installée anticipe l’entrée et modère son prix "
    "pour la rendre non rentable."),
   ("La condition de libre entrée",
    "Aucune barrière technique, financière ou réglementaire ne doit empêcher "
    "l’arrivée d’un nouvel acteur : c’est la condition qui rend la menace "
    "possible."),
   ("La condition de libre sortie",
    "L’entrant doit pouvoir quitter le marché sans perte majeure : sans cette "
    "possibilité, le risque d’entrée devient dissuasif et la menace cesse "
    "d’être crédible."),
   ("L’accès à la technologie",
    "L’entrant doit pouvoir produire dans des conditions comparables : un "
    "savoir-faire ou un brevet inaccessible rend l’entrée impossible même en "
    "l’absence d’autre obstacle."),
   ("L’absence de coûts irrécupérables",
    "Si entrer exige un investissement non récupérable en cas de sortie, "
    "l’entrant supporte un risque asymétrique : la contestabilité disparaît "
    "alors même que l’entrée reste juridiquement libre.")],
  [{'a': "La théorie explique qu’un marché concentré puisse être "
         "concurrentiel, ce que le seul comptage des entreprises ne permet pas "
         "de comprendre.",
    'cond': "L’explication suppose que la menace d’entrée soit crédible, donc "
            "que les quatre conditions soient réunies.",
    'lim': "Ces conditions sont rarement toutes satisfaites, en particulier "
           "celle de l’absence de coûts irrécupérables."},
   {'a': "Elle réoriente la politique de concurrence vers les barrières à "
         "l’entrée, cible plus précise que la taille des entreprises.",
    'cond': "La réorientation suppose que les autorités puissent identifier et "
            "lever ces barrières, y compris lorsqu’elles sont "
            "réglementaires.",
    'lim': "Certaines barrières remplissent une fonction légitime : le brevet "
           "protège l’innovation, et la licence professionnelle peut garantir "
           "une qualité de service."},
   {'a': "Elle fournit un critère applicable aux marchés en transformation, où "
         "les concurrents actuels renseignent mal sur la pression "
         "concurrentielle future.",
    'cond': "Le critère est pertinent lorsque la technologie évolue vite et "
            "que de nouveaux entrants peuvent apparaître rapidement.",
    'lim': "Dans les secteurs où les effets de réseau jouent, la position "
           "installée devient très difficile à contester malgré une entrée "
           "formellement libre."},
   {'a': "Elle réconcilie partiellement l’efficacité des grandes entreprises "
         "et l’exigence concurrentielle.",
    'cond': "La réconciliation suppose que l’entreprise installée anticipe "
            "effectivement l’entrée, ce qui dépend de son horizon de "
            "décision.",
    'lim': "Une entreprise peut préférer ériger des barrières plutôt que "
           "modérer ses prix, ce qui transforme la menace d’entrée en objet de "
           "stratégie."}],
  [{'t': "Le critère pertinent reste le nombre d’entreprises présentes, car la "
         "menace d’entrée est souvent théorique.",
    'qui': "La lecture structurelle de la concurrence, que le modèle SCP "
           "privilégie.",
    'rep': "L’objection porte surtout lorsque les coûts irrécupérables sont "
           "élevés : la théorie elle-même pose cette condition, de sorte que "
           "les deux approches s’articulent plutôt qu’elles ne s’opposent."},
   {'t': "La contestabilité est démentie par l’existence de barrières à "
         "l’entrée nombreuses, variées et durables.",
    'qui': "Le constat du cours sur les barrières de coûts, de brevets et de "
           "réglementation.",
    'rep': "La théorie n’affirme pas que les marchés sont contestables mais "
           "indique ce qui les rendrait tels : elle fournit donc un programme "
           "d’action plutôt qu’une description."},
   {'t': "Dans les marchés numériques, l’entrée reste libre mais la position "
         "acquise est imprenable en raison des effets de réseau.",
    'qui': "L’analyse des monopoles liés aux effets de réseau que le cours "
           "développe à propos des plateformes.",
    'rep': "L’objection est forte : lorsque l’utilité du service augmente avec "
           "le nombre d’utilisateurs, l’entrant ne peut offrir une qualité "
           "comparable, d’où un risque de verrouillage du marché."},
   {'t': "Certaines grandes entreprises freinent l’innovation précisément en "
         "empêchant l’entrée de nouveaux concurrents.",
    'qui': "Philippe Aghion, dont le cours rapporte cette position.",
    'rep': "L’argument complète la théorie au lieu de la contredire : il "
           "montre que l’entreprise installée a intérêt à détruire la "
           "contestabilité de son marché, ce qui justifie la vigilance "
           "publique."}],
  [{'n': "William Baumol",
    'i': "Le vrai critère de la concurrence n’est pas le nombre d’entreprises "
         "présentes mais la libre entrée et la libre sortie du marché.",
    'p': "Le cours précise que même s’il n’y a qu’une seule entreprise sur le "
         "marché, elle peut se comporter comme si elle était en concurrence, "
         "parce qu’elle craint l’arrivée de concurrents. La discipline vient "
         "donc de la concurrence potentielle."},
   {'n': "John Panzar",
    'i': "Un marché contestable suppose l’absence de barrières à l’entrée "
         "comme à la sortie.",
    'p': "Avec Baumol et Willig, il développe la théorie dans les années 1980. "
         "La condition de libre sortie est son apport le moins intuitif et le "
         "plus décisif : sans elle, le risque d’entrée est asymétrique et la "
         "menace perd sa crédibilité."},
   {'n': "Robert Willig",
    'i': "L’absence de coûts irrécupérables trop importants est une condition "
         "de la contestabilité.",
    'p': "Le cours range cette condition parmi les quatre requises, aux côtés "
         "de l’accès possible à la technologie. C’est la plus restrictive, "
         "puisque la plupart des secteurs industriels exigent des "
         "investissements spécifiques difficilement redéployables."},
   {'n': "Joe Bain",
    'i': "La structure du marché détermine les comportements puis les "
         "performances.",
    'p': "Son modèle SCP constitue l’approche que la contestabilité vient "
         "corriger : là où le modèle lit la concurrence dans la structure "
         "observée, Baumol et ses coauteurs la lisent dans les possibilités "
         "d’entrée, c’est-à-dire dans une structure potentielle."}],
  [{'f': "William Baumol, John Panzar et Robert Willig développent la théorie "
         "des marchés contestables dans les années 1980.",
    'p': "L’attribution collective et la datation situent la théorie comme une "
         "réponse tardive au modèle SCP et aux difficultés du contrôle des "
         "concentrations."},
   {'f': "Les quatre conditions de la contestabilité sont l’absence de "
         "barrières à l’entrée, l’absence de barrières à la sortie, l’accès "
         "possible à la technologie et l’absence de coûts irrécupérables trop "
         "importants.",
    'p': "La liste est le cœur du dossier : elle permet de tester la "
         "contestabilité d’un marché donné point par point."},
   {'f': "Le cours énonce l’idée clé : même s’il n’y a qu’une seule entreprise "
         "sur le marché, elle peut se comporter comme si elle était en "
         "concurrence.",
    'p': "La formulation est paradoxale et donc marquante : elle dissocie "
         "complètement structure observée et comportement effectif."},
   {'f': "Le cours présente la théorie comme une réponse aux barrières à "
         "l’entrée, après avoir souligné leur ambivalence dans le cas des "
         "professions réglementées.",
    'p': "L’enchaînement montre que la contestabilité est une notion "
         "normative : elle indique ce qu’il faudrait lever pour que la "
         "concurrence opère."}],
  [{'q': "Sujet du type « Faut-il mesurer la concurrence par le nombre "
         "d’entreprises ? »",
    'f': "Baumol, Panzar et Willig proposent de redéfinir la concurrence non "
         "plus par le nombre d’entreprises présentes mais par la possibilité "
         "d’entrer et de sortir du marché. L’idée clé est que même s’il n’y a "
         "qu’une seule entreprise sur le marché, elle peut se comporter comme "
         "si elle était en concurrence, parce qu’elle craint l’arrivée de "
         "concurrents. Les conditions sont toutefois exigeantes : absence de "
         "barrières à l’entrée et à la sortie, accès possible à la "
         "technologie, absence de coûts irrécupérables trop importants.",
    'r': "Le raisonnement substitue un critère potentiel à un critère "
         "observable, ce qui permet d’expliquer qu’un marché concentré soit "
         "concurrentiel ou qu’un marché atomisé ne le soit pas.",
    'ex': "Les coûts irrécupérables, qui rendent la menace d’entrée non "
          "crédible même lorsque l’entrée est juridiquement libre."},
   {'q': "Sujet du type « Sur quoi la politique de concurrence doit-elle "
         "porter ? »",
    'f': "La théorie des marchés contestables déplace la cible. Si c’est la "
         "libre entrée qui discipline, alors l’action publique doit porter sur "
         "les barrières plutôt que sur les parts de marché. Or le cours montre "
         "que ces barrières sont de natures très différentes — coûts élevés, "
         "brevets, accords d’exclusivité, licences, diplômes obligatoires, "
         "normes, monopoles publics — et que certaines remplissent une "
         "fonction légitime, le brevet protégeant temporairement l’innovation.",
    'r': "Le raisonnement montre que la politique de concurrence doit trier "
         "parmi les barrières au lieu de les supprimer toutes, ce qui est plus "
         "exigeant mais plus juste que le seul contrôle des concentrations.",
    'ex': "Les licences de taxi, barrière à l’entrée mais aussi capital "
          "revendable constitué par les chauffeurs."}],
  voisins=['n5-barrieres', 'n5-monopole', 'n5-pouvoir-marche',
           'n5-politique-concurrence'])


d('n5-politique-concurrence', 5, "Politique de la concurrence",
  "Quatre domaines d’action pour empêcher que la concurrence soit faussée",
  "La politique de la concurrence regroupe les interventions publiques "
  "destinées à protéger le fonctionnement concurrentiel des marchés. Le cours "
  "en identifie quatre domaines : la surveillance des aides d’État, le "
  "contrôle des concentrations, la lutte contre les cartels et la lutte contre "
  "les abus de position dominante, résumés par le moyen mnémotechnique « État "
  "contre carabus ».",
  "La politique de la concurrence est la réponse institutionnelle à l’ensemble "
  "des problèmes analysés dans le chapitre, et son étude suppose de distinguer "
  "les fondements, les instruments et les institutions. Le fondement est "
  "simple : les grandes entreprises peuvent former des cartels, abuser de leur "
  "position dominante et limiter la concurrence, d’où la mise en place de "
  "politiques de concurrence, de lois antitrust et d’autorités de régulation "
  "destinées à protéger le fonctionnement concurrentiel des marchés. Les "
  "cadres juridiques ensuite. Aux États-Unis, la lutte repose sur les lois "
  "antitrust : le Sherman Act de 1890, le Clayton Act de 1914 et le Federal "
  "Trade Commission Act de 1914, qui visent à interdire les cartels, limiter "
  "les monopoles abusifs, sanctionner les pratiques anticoncurrentielles et "
  "protéger le consommateur. L’exemple historique majeur est le démantèlement "
  "de la Standard Oil en 1911. En Europe, la concurrence est considérée comme "
  "indispensable au bon fonctionnement du marché intérieur, et les textes "
  "essentiels sont les articles 101 et 102 du traité sur le fonctionnement de "
  "l’Union européenne, le premier interdisant les ententes, les cartels et les "
  "accords qui faussent la concurrence. En France, deux institutions "
  "coexistent : la DGCCRF, rattachée au ministère de l’Économie, qui surveille "
  "les fraudes, la consommation et les pratiques commerciales, et l’Autorité "
  "de la concurrence, autorité indépendante qui contrôle les fusions, les "
  "cartels et les abus de position dominante, et qui peut enquêter, "
  "sanctionner, imposer des amendes et refuser certaines concentrations. Trois "
  "principes encadrent cette action. Premier principe : la loi ne condamne pas "
  "la position dominante mais l’abus de position dominante. Deuxième "
  "principe : tous les monopoles ne sont pas interdits, le monopole naturel et "
  "le monopole temporaire d’innovation étant autorisés. Troisième principe : "
  "l’appréciation dépend de l’échelle, une entreprise pouvant être dominante "
  "localement tout en affrontant une forte concurrence mondiale.",
  [("La protection du processus concurrentiel",
    "L’objectif n’est pas de protéger les concurrents mais le mécanisme de "
    "concurrence lui-même : prix plus bas, innovation accrue, productivité "
    "plus forte et bien-être du consommateur amélioré."),
   ("Le contrôle ex ante des concentrations",
    "Les autorités examinent les fusions avant leur réalisation et peuvent les "
    "refuser : l’intervention est préventive, ce qui évite d’avoir à démanteler "
    "ensuite une structure acquise."),
   ("La sanction ex post des pratiques",
    "Ententes et abus de position dominante sont poursuivis après les faits, "
    "par l’enquête, l’amende et l’injonction : l’action est ici répressive et "
    "suppose une preuve."),
   ("L’encadrement des aides d’État",
    "Une entreprise subventionnée devient artificiellement plus compétitive : "
    "elle peut vendre moins cher, investir davantage et prendre des parts de "
    "marché, d’où une interdiction de principe assortie d’exceptions."),
   ("La délimitation du marché pertinent",
    "Toute décision suppose de définir le marché sur lequel la position est "
    "appréciée : local, national, européen ou mondial, et c’est ce choix qui "
    "détermine le plus souvent la conclusion.")],
  [{'a': "La politique de concurrence produit des effets favorables au "
         "consommateur, par la baisse des prix, la hausse de l’innovation et "
         "de la productivité.",
    'cond': "L’enchaînement suppose que la pression concurrentielle se "
            "traduise effectivement en baisse de prix et non en baisse de "
            "qualité.",
    'lim': "Schumpeter objecte que la concurrence parfaite n’est pas toujours "
           "la structure la plus favorable au progrès, l’innovation exigeant "
           "un avantage temporaire."},
   {'a': "Elle distingue la position dominante de l’abus, ce qui évite de "
         "sanctionner la réussite ou la taille.",
    'cond': "La distinction suppose un examen des pratiques et des effets, "
            "plus exigeant qu’un seuil de part de marché.",
    'lim': "L’appréciation peut être ambiguë, le cours notant que certaines "
           "discriminations sont interdites tandis que d’autres formes de "
           "tarification différenciée sont autorisées."},
   {'a': "Elle dispose d’instruments adaptés à la difficulté de preuve, dont "
         "la procédure de clémence.",
    'cond': "Le dispositif suppose que la réduction de sanction soit "
            "suffisamment attractive pour l’emporter sur le gain attendu de "
            "l’entente.",
    'lim': "Il peut avantager l’entreprise la plus habile à dénoncer plutôt "
           "que la moins responsable de l’infraction."},
   {'a': "Elle admet des exceptions motivées, ce qui lui permet de concilier "
         "concurrence et autres objectifs publics.",
    'cond': "Les exceptions doivent être circonscrites : le cours cite les "
            "aides à la recherche, aux PME, écologiques, de crise et à "
            "l’innovation.",
    'lim': "Cette souplesse rend la frontière mouvante, et l’Union critique "
           "les subventions chinoises tout en tolérant certaines de ses "
           "propres aides."}],
  [{'t': "La politique de concurrence européenne empêche la constitution de "
         "champions capables d’affronter la concurrence mondiale.",
    'qui': "L’argument avancé par Alstom et Siemens après le refus de leur "
           "fusion par la Commission européenne.",
    'rep': "L’argument repose sur la définition du marché pertinent : les "
           "entreprises soutenaient que leur marché est mondial, tandis que la "
           "Commission craignait un monopole en Europe."},
   {'t': "La concurrence n’est pas toujours la structure la plus favorable au "
         "progrès technique.",
    'qui': "Joseph Schumpeter, dans sa deuxième rupture avec la théorie "
           "standard.",
    'rep': "Le cours intègre l’objection plutôt que de la rejeter : tous les "
           "monopoles ne sont pas interdits, et le monopole temporaire fondé "
           "sur un brevet est accepté afin de rémunérer l’innovation."},
   {'t': "La priorité donnée à la concurrence a affaibli la politique "
         "industrielle européenne, devenue essentiellement horizontale.",
    'qui': "L’analyse que le cours propose de la transformation de la "
           "politique industrielle sous l’effet de l’intégration européenne.",
    'rep': "La transformation est réelle : l’Europe privilégie recherche, "
           "innovation, formation, infrastructures et environnement "
           "concurrentiel plutôt que la sélection d’entreprises gagnantes, "
           "conformément au raisonnement néoclassique."},
   {'t': "La surveillance des aides d’État désarme l’Europe face aux "
         "subventions massives accordées par ses concurrents.",
    'qui': "La critique que le cours rapporte à propos des subventions "
           "chinoises.",
    'rep': "L’Union critique précisément ces subventions, qui permettent aux "
           "entreprises chinoises de vendre moins cher, ce qui montre que le "
           "problème est l’asymétrie des règles plus que leur existence."}],
  [{'n': "Joseph Schumpeter",
    'i': "L’innovation doit être protégée, même si la concurrence doit rester "
         "la règle.",
    'p': "Le cours en fait la justification des monopoles autorisés : le "
         "monopole temporaire fondé sur un brevet ou sur l’innovation est "
         "accepté afin de rémunérer l’innovation, ce qui introduit une "
         "exception raisonnée au principe concurrentiel."},
   {'n': "Philippe Aghion",
    'i': "Certaines grandes entreprises peuvent freiner l’innovation en "
         "empêchant l’entrée de nouveaux concurrents.",
    'p': "Sa position fournit l’argument inverse du précédent et justifie la "
         "vigilance des autorités : la protection de la concurrence devient "
         "une condition de l’innovation future, et non son obstacle."},
   {'n': "William Baumol",
    'i': "C’est la libre entrée, plus que le nombre d’entreprises, qui "
         "discipline un marché.",
    'p': "Sa théorie des marchés contestables oriente la politique de "
         "concurrence vers les barrières à l’entrée : surveiller la "
         "contestabilité peut être plus efficace que contrôler les parts de "
         "marché."},
   {'n': "Daron Acemoglu",
    'i': "Les plateformes numériques et l’IA accroissent les asymétries de "
         "pouvoir et concentrent l’influence.",
    'p': "Avec Simon Johnson dans Power and Progress (2023), il montre que les "
         "enjeux dépassent le prix et la quantité : le contrôle des données et "
         "des flux d’information fait de la concentration un problème "
         "démocratique, ce qui élargit le mandat de la régulation."}],
  [{'f': "Les quatre grands domaines de la politique de concurrence sont les "
         "aides d’État, les concentrations, les cartels et les abus de "
         "position dominante, résumés par le moyen mnémotechnique « État "
         "contre carabus ».",
    'p': "L’énumération fournit la structure complète du dossier et permet de "
         "ne rien oublier dans une copie."},
   {'f': "Les grandes lois antitrust américaines sont le Sherman Act de 1890, "
         "le Clayton Act de 1914 et le Federal Trade Commission Act de 1914 ; "
         "la Standard Oil est démantelée en 1911.",
    'p': "Les dates montrent l’ancienneté du dispositif et son lien avec la "
         "concentration industrielle du tournant du XXᵉ siècle."},
   {'f': "En Europe, les textes essentiels sont les articles 101 et 102 du "
         "TFUE, le premier interdisant les ententes, les cartels et les "
         "accords qui faussent la concurrence.",
    'p': "La référence permet de distinguer le fondement européen, lié à la "
         "protection du marché commun, du fondement américain, lié à la "
         "limitation des monopoles."},
   {'f': "En France, la DGCCRF dépend du ministère de l’Économie tandis que "
         "l’Autorité de la concurrence est indépendante et peut enquêter, "
         "sanctionner, imposer des amendes et refuser certaines "
         "concentrations.",
    'p': "La dualité institutionnelle montre que la surveillance combine une "
         "administration et une autorité indépendante, ce qui protège la "
         "décision des pressions politiques."}],
  [{'q': "Sujet du type « L’État doit-il intervenir pour protéger la "
         "concurrence ? »",
    'f': "L’intervention se justifie par un constat précis : les grandes "
         "entreprises peuvent former des cartels, abuser de leur position "
         "dominante et limiter la concurrence. Les États mettent donc en place "
         "des politiques de concurrence, des lois antitrust et des autorités "
         "de régulation, dont l’objectif est de protéger le fonctionnement "
         "concurrentiel des marchés. La logique est explicite : concurrence, "
         "donc prix plus bas, innovation accrue, productivité plus forte et "
         "bien-être du consommateur amélioré.",
    'r': "Le raisonnement montre que l’intervention vise à préserver le marché "
         "et non à le remplacer, ce qui la place à l’abri de l’objection "
         "libérale habituelle.",
    'ex': "Les quatre domaines d’action rappelés par le moyen mnémotechnique "
          "« État contre carabus » : aides d’État, concentrations, cartels, "
          "abus de position dominante."},
   {'q': "Sujet du type « La politique de concurrence est-elle compatible avec "
         "la politique industrielle ? »",
    'f': "La tension est réelle et le cours la documente. L’intégration "
         "européenne suppose que les États ne puissent librement favoriser "
         "leurs entreprises au détriment de celles de leurs partenaires, d’où "
         "un encadrement strict des aides d’État. La conséquence est que la "
         "politique industrielle européenne est devenue essentiellement "
         "horizontale, privilégiant recherche, innovation, formation, "
         "infrastructures et environnement concurrentiel, l’État "
         "n’intervenant qu’en cas d’externalités, d’asymétries d’information, "
         "de biens publics ou de défaillances de coordination.",
    'r': "Le raisonnement montre que la contrainte concurrentielle n’interdit "
         "pas l’intervention mais en change la forme, du vertical vers "
         "l’horizontal, ce qui est une réponse plus précise qu’un simple "
         "constat d’incompatibilité.",
    'ex': "Le refus de la fusion Alstom-Siemens par la Commission européenne, "
          "malgré l’argument de la concurrence chinoise."},
   {'q': "Sujet du type « Les grandes entreprises doivent-elles être "
         "démantelées ? »",
    'f': "Le cours répond par la distinction juridique fondamentale : la loi "
         "ne condamne pas la position dominante, elle condamne l’abus de "
         "position dominante. Tous les monopoles ne sont d’ailleurs pas "
         "interdits : le monopole naturel, où une seule entreprise est plus "
         "efficace que plusieurs concurrentes, et le monopole temporaire fondé "
         "sur un brevet ou sur l’innovation sont autorisés. S’ajoute la "
         "question de l’échelle, une entreprise pouvant être dominante "
         "localement tout en affrontant une forte concurrence mondiale.",
    'r': "Le raisonnement montre que la réponse dépend de trois examens "
         "successifs — la nature du monopole, le comportement de l’entreprise "
         "et le périmètre du marché — ce qui exclut toute réponse générale.",
    'ex': "Le démantèlement de la Standard Oil en 1911, qui illustre le cas où "
          "la puissance d’une firme menace effectivement le jeu "
          "concurrentiel."}],
  voisins=['n5-ententes', 'n5-pouvoir-marche', 'n5-concentration',
           'n5-monopole', 'n5-contestables'])
