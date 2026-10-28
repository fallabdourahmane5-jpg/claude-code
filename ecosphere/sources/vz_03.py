# -*- coding: utf-8 -*-
"""Visualisation 3 — Croissance et environnement (type duel)."""

from vz_base import v, nd, ln

v('vz-environnement', 'Croissance et environnement',
  'Chapitre 6 · un désaccord et son point de bascule',
  'duel',
  "Le débat sur la croissance et l’environnement n’oppose pas des valeurs "
  "mais deux réponses à une seule question technique : les différentes "
  "formes de capital sont-elles substituables ? Cette visualisation place la "
  "question au sommet, déploie à gauche la réponse de la soutenabilité "
  "faible et à droite celle de la soutenabilité forte, et montre en bas ce "
  "qui permet réellement d’arbitrer entre les deux.",
  [("Un seul désaccord, deux colonnes",
    "Colonne de gauche : si les capitaux sont substituables, la technique "
    "peut compenser et la croissance verte a un fondement. Colonne de "
    "droite : s’ils ne le sont pas, il faut agir sur les volumes, ce qui "
    "conduit à la sobriété puis à la décroissance."),
   ("Les faits qui tranchent",
    "Découplage relatif ou absolu, effet rebond, identité de Kaya, "
    "délocalisation des émissions : ce sont ces éléments, et non les "
    "intentions, qui départagent les deux colonnes. Chaque flèche renvoie au "
    "fait qui la justifie."),
   ("Ce qu’il faut éviter d’écrire",
    "Ne pas confondre développement durable et décroissance : le cours "
    "précise que le rapport Brundtland ne rejette pas la croissance. Ne pas "
    "confondre non plus efficacité et sobriété : c’est l’effet rebond qui "
    "impose de les distinguer.")],
  [
   nd('question', 'Les capitaux sont-ils substituables ?', 'coeur',
      "La croissance dépend de six capitaux : physique, humain, naturel, "
      "technologique, social, institutionnel. Tout le débat porte sur un "
      "point : peut-on remplacer le naturel par les autres ?",
      grp=0,
      defi="La question de la soutenabilité ne porte pas sur la quantité de "
           "croissance mais sur la composition du capital qui la rend "
           "possible. Le cours énumère six capitaux complémentaires — "
           "physique, humain, naturel, technologique, social et "
           "institutionnel — dont dépend la croissance. C’est parce que la "
           "croissance dépend de plusieurs capitaux que la question de leur "
           "substituabilité peut être posée : si la baisse de l’un peut être "
           "compensée par la hausse d’un autre, seul compte le stock total ; "
           "sinon, certaines pertes sont définitives.",
      mec=[("L’élargissement de la notion de capital",
            "La croissance ne dépend pas du seul capital productif : la "
            "question de la soutenabilité porte sur la préservation d’un "
            "ensemble de six capitaux, dont le capital naturel n’est qu’une "
            "composante parmi d’autres — ou la composante critique, selon la "
            "réponse retenue."),
           ("La formulation de l’arbitrage",
            "Si les capitaux sont substituables, détruire du capital naturel "
            "pour produire du capital technologique est un arbitrage "
            "acceptable. S’ils ne le sont pas, c’est une perte sèche que rien "
            "ne compense."),
           ("Le caractère non symétrique de la réponse",
            "La substituabilité n’est ni vraie ni fausse en bloc : elle varie "
            "d’une ressource à l’autre. Certaines contraintes ont été "
            "effectivement desserrées par la technique, d’autres portent sur "
            "des équilibres irréversibles.")],
      faits=[{'f': "Le cours énumère six capitaux dont dépend la croissance : "
                   "physique, humain, naturel, technologique, social et "
                   "institutionnel.",
              'p': "Cette énumération est la condition du débat : c’est parce "
                   "que la croissance dépend de plusieurs capitaux que la "
                   "question de leur substituabilité peut être posée."},
             {'f': "Le cours attribue à la soutenabilité faible une "
                   "inspiration néoclassique et à la soutenabilité forte une "
                   "inspiration écologique.",
              'p': "Le rattachement doctrinal situe les positions : "
                   "l’opposition ne tient pas à des préférences morales mais "
                   "à des conceptions différentes de la fonction de "
                   "production."}],
      termes=['soutenabilite', 'capital naturel', 'developpement durable'],
      dos=['n4-soutenabilites', 'n4-capital-naturel']),

   # ------------------------------------------------- colonne 1 : faible
   nd('faible', 'La soutenabilité faible', 'pilier',
      "D’inspiration néoclassique : les capitaux sont globalement "
      "substituables, et la baisse du capital naturel peut être compensée par "
      "le capital technologique.",
      grp=1,
      defi="La soutenabilité faible, d’inspiration néoclassique, considère "
           "que les différentes formes de capital sont globalement "
           "substituables : la baisse du capital naturel peut être compensée "
           "par davantage de capital technologique et d’innovation. Ce qui "
           "doit être transmis aux générations futures n’est pas un stock "
           "naturel déterminé mais une capacité de production, dont la "
           "composition peut varier sans dommage.",
      mec=[("L’hypothèse de substituabilité",
            "Une baisse du capital naturel est compensable par une hausse du "
            "capital technologique : seul importe le stock total de capital, "
            "dont la composition peut varier sans dommage pour les "
            "générations futures."),
           ("Les canaux concrets de la compensation",
            "Réduction de l’intensité énergétique, amélioration de "
            "l’efficacité, substitution de matières premières, dépollution, "
            "innovation verte : autant de voies par lesquelles la technique "
            "desserre la contrainte environnementale.")],
      opp=[{'t': "La substituabilité des capitaux est une hypothèse de modèle "
                 "et non un fait établi : elle est posée, pas démontrée.",
            'qui': "critique méthodologique",
            'rep': "L’objection est juste : toute la force de la "
                   "soutenabilité faible repose sur une hypothèse dont la "
                   "validité varie d’une ressource à l’autre, ce qui invite à "
                   "raisonner ressource par ressource plutôt qu’en bloc."}],
      aut=[{'n': "Robert Solow",
            'i': "La croissance dépend du capital, du travail et du progrès "
                 "technique, ce dernier étant exogène dans le modèle "
                 "initial."},
           {'n': "Gene Grossman",
            'i': "Au-delà d’un certain niveau de revenu, la hausse du revenu "
                 "peut s’accompagner d’une baisse de la pollution."}],
      termes=['soutenabilite faible', 'substituabilite', 'progres technique'],
      dos=['n4-soutenabilites']),

   nd('verte', 'La croissance verte', 'pilier',
      "On ne renonce pas à la croissance : on en transforme le contenu. "
      "Intensité carbone en baisse, technologies propres, destruction "
      "créatrice orientée vers la transition.",
      grp=1,
      defi="La croissance verte est la tentative de concilier dynamique "
           "économique et contrainte environnementale : maintenir la "
           "croissance tout en réduisant l’intensité carbone, en investissant "
           "dans les technologies propres et en favorisant l’innovation "
           "environnementale. Sa logique est schumpétérienne : l’innovation "
           "est traitée comme la solution au problème climatique, par une "
           "destruction créatrice orientée vers la transition écologique.",
      mec=[("La réduction de l’intensité carbone",
            "Plutôt que de réduire la production, on réduit les émissions par "
            "unité produite : l’investissement dans les technologies propres "
            "déplace la contrainte du volume vers le contenu de la "
            "croissance."),
           ("La création de marchés et d’emplois",
            "La transition engendre de nouveaux marchés, comme le montre la "
            "rénovation thermique, qui crée des emplois dans le bâtiment, "
            "l’isolation et l’ingénierie thermique tout en abaissant les "
            "factures."),
           ("La production de perdants à court terme",
            "La destruction créatrice détruit avant de créer : emplois "
            "supprimés, hausses de prix de l’énergie et du transport, "
            "pression sur les coûts. Sans accompagnement public, la "
            "transition devient politiquement intenable.")],
      opp=[{'t': "La croissance verte se heurte à la concurrence "
                 "internationale, qui pousse les producteurs vers les pays "
                 "moins régulés.",
            'qui': "objection commerciale",
            'rep': "L’objection a reçu une réponse institutionnelle avec le "
                   "mécanisme d’ajustement carbone aux frontières, qui réduit "
                   "l’avantage de la production non décarbonée."}],
      aut=[{'n': "Joseph Schumpeter",
            'i': "La croissance procède de la destruction créatrice, les "
                 "activités nouvelles remplaçant les anciennes."},
           {'n': "Philippe Aghion",
            'i': "La destruction créatrice exige un accompagnement public des "
                 "perdants pour être politiquement soutenable."},
           {'n': "Mario Draghi",
            'i': "L’Europe doit financer un plan d’investissement massif "
                 "ciblé sur l’innovation et la transition énergétique."}],
      faits=[{'f': "Le cours résume la logique par une formule : on ne "
                   "renonce pas à la croissance, on en transforme le contenu.",
              'p': "La formule marque la différence décisive avec la "
                   "décroissance et fournit une transition efficace en "
                   "dissertation."}],
      termes=['croissance verte', 'innovation verte', 'transition energetique'],
      dos=['n4-verte', 'n4-innovation-verte']),

   nd('decouplage', 'Le découplage et la courbe de Kuznets', 'detail',
      "Relatif : les émissions croissent moins vite que le PIB. Absolu : le "
      "PIB monte tandis que les émissions baissent. Seul le second permet "
      "d’atteindre un objectif de réduction.",
      grp=1, par='verte',
      defi="Le découplage désigne la dissociation entre l’évolution de la "
           "production et celle des pressions exercées sur l’environnement. "
           "Il est relatif lorsque les émissions augmentent moins vite que le "
           "PIB, et absolu lorsque le PIB continue d’augmenter tandis que les "
           "émissions diminuent. Le découplage absolu constitue l’objectif "
           "explicite du pilier environnemental du développement durable. "
           "Grossman et Krueger en proposent en 1995 une lecture par le "
           "revenu, sous le nom de courbe environnementale de Kuznets.",
      mec=[("Le mécanisme d’offre",
            "La hausse du revenu permet de financer des technologies plus "
            "propres : l’économie dispose des moyens d’investir dans la "
            "décarbonation, ce qu’une économie pauvre ne peut pas faire."),
           ("Le mécanisme de demande",
            "À mesure que le revenu augmente, la demande sociale de "
            "protection environnementale s’élève, ce qui se traduit en normes "
            "plus fortes, en réglementations et en prix du carbone : la "
            "contrainte vient alors des préférences des citoyens."),
           ("La compensation par les volumes",
            "L’identité de Kaya montre que les progrès sur l’intensité "
            "carbone et l’intensité énergétique peuvent être effacés par la "
            "hausse du niveau de vie et de la population : le découplage est "
            "une course entre la technique et le volume.")],
      opp=[{'t': "Le découplage absolu observé dans les pays développés n’est "
                 "qu’un transfert : la pollution a été délocalisée, non "
                 "supprimée.",
            'qui': "objection par l’empreinte",
            'rep': "L’objection est forte et impose de raisonner en émissions "
                   "liées à la consommation : une production intérieure peut "
                   "sembler propre alors qu’une partie de la pollution est "
                   "externalisée."},
           {'t': "Le découplage se produira de lui-même avec l’élévation du "
                 "revenu : il n’y a pas lieu de forcer le mouvement.",
            'qui': "lecture optimiste de la courbe",
            'rep': "Le mécanisme de demande n’opère que par la "
                   "réglementation et le prix du carbone, c’est-à-dire par "
                   "des politiques publiques : la courbe décrit une causalité "
                   "médiatisée, non automatique."}],
      aut=[{'n': "Gene Grossman",
            'i': "Au-delà d’un certain niveau de revenu, la hausse du revenu "
                 "peut faire baisser la pollution."},
           {'n': "Alan Krueger",
            'i': "La demande sociale de protection environnementale s’élève "
                 "avec le revenu et se traduit en normes et en prix du "
                 "carbone."},
           {'n': "Yoichi Kaya",
            'i': "Les émissions dépendent de quatre facteurs, dont deux de "
                 "volume : le niveau de vie et la population."}],
      faits=[{'f': "Le cours formule la séquence en deux temps : d’abord "
                   "revenu en hausse, production en hausse, pollution en "
                   "hausse ; au-delà d’un certain niveau, revenu en hausse et "
                   "pollution possiblement en baisse.",
              'p': "La formulation conditionnelle du second temps est "
                   "essentielle : le cours écrit que la pollution peut "
                   "diminuer, non qu’elle diminue nécessairement."}],
      termes=['decouplage', 'courbe environnementale de kuznets',
              'identite de kaya'],
      dos=['n4-decouplage']),

   nd('instruments', 'Prix du carbone ou règle ?', 'detail',
      "Taxe, quotas et incitations d’un côté ; normes, interdictions et "
      "standards de l’autre. Le prix cherche le moindre coût, la règle "
      "garantit le résultat.",
      grp=1, par='verte',
      defi="La taxe carbone est l’application de la logique pigouvienne aux "
           "émissions de gaz à effet de serre : elle attribue un prix à la "
           "tonne de CO₂ afin que le coût social du réchauffement soit "
           "intégré dans les décisions de production et de consommation. Le "
           "cours la range, avec le prix du carbone et le marché de quotas, "
           "dans la famille des instruments de marché, par opposition aux "
           "normes, interdictions, standards et obligations juridiques.",
      mec=[("L’égalisation des coûts marginaux de réduction",
            "Chaque agent réduit tant que le coût de sa réduction reste "
            "inférieur au prix de la tonne : à l’équilibre, la dépollution "
            "est obtenue au moindre coût collectif, ce qui fait l’efficacité "
            "économique de l’instrument."),
           ("L’incitation permanente à innover",
            "Contrairement à une norme que l’on se contente d’atteindre, le "
            "prix récompense toute réduction supplémentaire : l’incitation à "
            "chercher de nouvelles solutions ne disparaît jamais."),
           ("Le problème du périmètre et de la fuite",
            "Si le prix ne s’applique qu’à une zone, les producteurs soumis "
            "sont désavantagés et la production peut se déplacer : "
            "l’ajustement aux frontières rétablit la symétrie en faisant "
            "payer le contenu carbone des importations.")],
      opp=[{'t': "Le prix du carbone est trop faible et trop volatil pour "
                 "modifier durablement les comportements des entreprises.",
            'qui': "objection chiffrée",
            'rep': "L’objection est difficilement contestable : autour de "
                   "80 € la tonne le prix est jugé insuffisant, certains "
                   "économistes estimant qu’environ 140 € seraient "
                   "nécessaires pour être réellement dissuasifs."}],
      aut=[{'n': "Arthur Pigou",
            'i': "Corriger le prix pour qu’il reflète le vrai coût social "
                 "rétablit l’optimum collectif."},
           {'n': "Ronald Coase",
            'i': "On peut atteindre le même objectif en fixant les quantités "
                 "et en laissant le marché déterminer le prix."},
           {'n': "Mark Carney",
            'i': "Les acteurs économiques raisonnent sur un horizon plus "
                 "court que celui de la transition."}],
      termes=['taxe carbone', 'marche de quotas', 'ajustement carbone'],
      dos=['n4-taxe-carbone', 'n4-quotas']),

   # ------------------------------------------------- colonne 2 : forte
   nd('forte', 'La soutenabilité forte', 'pilier',
      "D’inspiration écologique : le capital naturel n’est pas substituable. "
      "Une espèce disparue, un climat déréglé, une forêt primaire ne se "
      "remplacent pas.",
      grp=2,
      defi="La soutenabilité forte considère que le capital naturel n’est pas "
           "substituable, certaines ressources et certains équilibres étant "
           "limités, irremplaçables et parfois irréversiblement détruits. "
           "L’exigence n’est plus de transmettre une capacité de production "
           "globale mais de préserver un stock critique, dont la disparition "
           "ne se rattrape par aucune accumulation d’un autre capital.",
      mec=[("Le caractère spécifique du capital naturel",
            "Certains éléments sont limités, non reproductibles et parfois "
            "irréversiblement détruits : une espèce disparue, un climat "
            "déréglé, une forêt primaire ou un stock minier épuisé ne se "
            "remplacent pas."),
           ("Le passage de la technique au mode de vie",
            "Si la substitution est impossible, l’ajustement ne peut plus se "
            "faire par la seule technique : il faut limiter l’extraction, "
            "réduire la consommation matérielle et modifier les modes de "
            "production et de consommation.")],
      args=[{'a': "L’argument d’irréversibilité est décisif là où il "
                  "s’applique : aucune innovation ne reconstitue un "
                  "écosystème détruit, ce qui interdit de traiter cette perte "
                  "comme un simple arbitrage entre capitaux.",
             'lim': "Il ne s’applique pas uniformément : certaines "
                    "contraintes environnementales ont effectivement été "
                    "desserrées par la substitution technique."}],
      aut=[{'n': "Kate Raworth",
            'i': "L’économie doit se tenir dans un espace sûr et juste, entre "
                 "un plancher social et un plafond écologique."}],
      termes=['soutenabilite forte', 'irreversibilite', 'capital naturel'],
      dos=['n4-soutenabilites', 'n4-capital-naturel']),

   nd('limites', 'Les limites écologiques', 'pilier',
      "Changement climatique, perte de biodiversité, pollution, épuisement "
      "des ressources : des seuils physiques que l’activité ne peut franchir "
      "sans dégradation durable.",
      grp=2,
      defi="Les limites écologiques désignent les seuils physiques que "
           "l’activité économique ne peut franchir sans provoquer une "
           "dégradation durable, voire irréversible, des conditions de la "
           "production et de la vie. Elles concernent notamment l’épuisement "
           "des ressources, le changement climatique, la perte de "
           "biodiversité et la pollution, et constituent ce que Kate Raworth "
           "appelle le plafond écologique de l’activité.",
      mec=[("Du stock au seuil",
            "Le rapport Meadows pense d’abord la limite comme un problème de "
            "stocks épuisables. La lecture contemporaine y ajoute des seuils "
            "au-delà desquels un équilibre bascule, ce qui rend la "
            "dégradation non linéaire et difficilement réversible."),
           ("Le plancher social et le plafond écologique",
            "Le Donut définit un espace compris entre un plancher social — "
            "alimentation, santé, éducation, logement, emploi, égalité — et "
            "un plafond écologique : une économie peut échouer par le bas "
            "comme par le haut.")],
      aut=[{'n': "Dennis Meadows",
            'i': "La poursuite indéfinie de la croissance se heurte à "
                 "l’épuisement des ressources et aux limites physiques de la "
                 "planète."},
           {'n': "Kate Raworth",
            'i': "L’économie standard ignore les limites planétaires et "
                 "confond le moyen, la croissance, avec la finalité, le "
                 "bien-être."}],
      faits=[{'f': "En 1972, le Club de Rome publie le rapport Meadows sur "
                   "les limites à la croissance, traduit en français par "
                   "Halte à la croissance ?",
              'p': "Le titre français, interrogatif, montre que la question a "
                   "été posée publiquement dès les années 1970 et qu’elle "
                   "précède largement le débat climatique contemporain."}],
      termes=['limites ecologiques', 'limites planetaires', 'club de rome',
              'donut'],
      dos=['n4-limites', 'n4-climat']),

   nd('rebond', 'L’effet rebond, de l’efficacité à la sobriété', 'detail',
      "Une voiture consomme moins, son usage coûte moins cher, on roule "
      "davantage. Les gains d’efficacité peuvent être partiellement, voire "
      "totalement, annulés.",
      grp=2, par='limites',
      defi="L’effet rebond, ou effet Jevons, désigne le fait que les gains "
           "d’efficacité peuvent être partiellement, voire totalement, "
           "annulés par une hausse des usages. C’est un effet-prix classique "
           "et non une anomalie comportementale : la baisse du coût d’usage "
           "accroît la quantité demandée du service devenu moins cher. Le "
           "cours le présente juste avant la distinction entre efficacité "
           "énergétique et sobriété énergétique, et cet enchaînement n’est "
           "pas fortuit.",
      mec=[("Le gain d’efficacité technique",
            "Une innovation permet d’accomplir la même tâche avec moins "
            "d’énergie : la consommation par unité de service rendu diminue "
            "effectivement, et ce premier effet est réel et mesurable."),
           ("La baisse du coût d’usage et la hausse des volumes",
            "Le prix implicite du service rendu diminue, ce qui modifie "
            "l’arbitrage du consommateur : on roule plus, on chauffe "
            "davantage, on équipe plus de pièces."),
           ("Le passage à la sobriété",
            "Si l’efficacité peut être annulée par les usages, seule une "
            "action portant directement sur les usages — la sobriété — "
            "garantit une baisse absolue. L’effet rebond est l’argument qui "
            "impose ce déplacement.")],
      opp=[{'t': "L’efficacité énergétique est le levier le plus sûr, car "
                 "elle ne demande aucun changement de comportement.",
            'qui': "argument technologique",
            'rep': "C’est précisément l’absence de changement de comportement "
                   "qui ouvre la porte au rebond : le raisonnement selon "
                   "lequel la consommation globale devrait baisser est "
                   "incomplet."}],
      faits=[{'f': "Le cours conclut que la baisse de consommation unitaire "
                   "existe mais que la consommation totale baisse moins que "
                   "prévu, voire ne baisse pas.",
              'p': "La conclusion est graduée : elle n’affirme pas que "
                   "l’efficacité est inutile, mais qu’elle ne garantit pas "
                   "automatiquement une baisse absolue."}],
      termes=['effet rebond', 'sobriete', 'efficacite energetique'],
      dos=['n4-rebond', 'n4-sobriete']),

   nd('decroissance', 'La décroissance', 'debat',
      "Version radicale de la soutenabilité forte : réduire les volumes "
      "produits et consommés, et non seulement en transformer le contenu.",
      grp=2, par='forte',
      defi="La décroissance désigne la position selon laquelle la réduction "
           "des pressions environnementales exige de diminuer la production "
           "et la consommation matérielles, et non seulement d’en transformer "
           "le contenu. Le cours la présente comme la version radicale de la "
           "soutenabilité forte, défendue par ceux qui tiennent le capital "
           "naturel pour non substituable et la croissance indéfinie pour "
           "incompatible avec la planète.",
      mec=[("La réduction des volumes",
            "Il faut limiter l’extraction et réduire la consommation "
            "matérielle : c’est la différence décisive avec la croissance "
            "verte, qui agit sur le contenu de la production et non sur son "
            "volume."),
           ("Le changement de critère d’évaluation",
            "Si l’objectif devient le bien-être dans les limites écologiques, "
            "une économie peut être performante sans croissance du PIB : la "
            "décroissance du produit cesse d’être un échec pour devenir un "
            "résultat possible.")],
      opp=[{'t': "La décroissance est socialement régressive, puisqu’elle "
                 "revient à renoncer à l’élévation du niveau de vie, "
                 "notamment dans les pays pauvres.",
            'qui': "objection sociale",
            'rep': "L’objection explique que la décroissance soit défendue "
                   "pour les économies avancées plutôt qu’universellement, le "
                   "plancher social du Donut impliquant précisément la "
                   "satisfaction des besoins fondamentaux."}],
      aut=[{'n': "Kate Raworth",
            'i': "Une économie peut être performante sans croissance du PIB, "
                 "et la croissance peut devenir inutile voire nuisible."}],
      faits=[{'f': "Le cours précise que le développement durable n’est pas "
                   "la décroissance au sens strict et qu’il ne rejette pas la "
                   "croissance.",
              'p': "La précision évite la confusion la plus fréquente : le "
                   "rapport Brundtland redéfinit l’objectif de la croissance "
                   "au lieu de la condamner."},
             {'f': "L’idée centrale du Pacte vert européen n’est ni d’arrêter "
                   "la croissance, ni d’imposer la décroissance, ni de "
                   "désindustrialiser l’Europe.",
              'p': "Le fait montre que la décroissance reste, dans les "
                   "politiques effectivement mises en œuvre, une position "
                   "minoritaire par rapport à la croissance verte."}],
      termes=['decroissance', 'sobriete', 'productivisme'],
      dos=['n4-decroissance']),

   # ------------------------------------------------- bas : ce qui arbitre
   nd('arbitrage', 'Ce qui tranche : ressource par ressource', 'sortie',
      "Ni l’une ni l’autre position n’est vraie en bloc. La substituabilité "
      "varie selon la ressource : c’est le seul terrain où le débat peut être "
      "arbitré.",
      grp=3,
      defi="Le cours ne tranche pas le débat de façon globale, et c’est "
           "précisément sa leçon de méthode : la substituabilité est une "
           "hypothèse dont la validité varie d’une ressource à l’autre. "
           "Certaines contraintes environnementales ont effectivement été "
           "desserrées par la substitution technique ; d’autres portent sur "
           "des équilibres irréversibles qu’aucune innovation ne reconstitue. "
           "La question pertinente n’est donc pas « la croissance est-elle "
           "soutenable ? » mais « quel type de croissance est compatible avec "
           "le développement durable ? ».",
      mec=[("Séparer les ressources",
            "Une énergie fossile peut être remplacée par une autre source ; "
            "une espèce disparue ne l’est pas. Raisonner ressource par "
            "ressource évite de trancher par principe un débat qui se joue "
            "cas par cas."),
           ("Poser la question du rythme",
            "L’argument selon lequel toute production exige énergie et "
            "matières vaut contre un découplage total, mais la question "
            "pertinente est celle du rythme : un découplage absolu "
            "suffisamment rapide suffirait à respecter une trajectoire "
            "d’émissions."),
           ("Combiner les leviers",
            "Efficacité et sobriété ne s’opposent pas : l’effet rebond montre "
            "que l’une sans l’autre ne garantit rien, et le cours associe "
            "instruments de marché et règles plutôt qu’il ne les oppose.")],
      faits=[{'f': "Le cours conclut que la question contemporaine n’est plus "
                   "de savoir s’il faut de la croissance mais quel type de "
                   "croissance est compatible avec le développement durable.",
              'p': "La conclusion fournit une problématique entière, et son "
                   "contenu est précis : une croissance soutenable doit être "
                   "innovante, inclusive et respectueuse des contraintes "
                   "environnementales."}],
      termes=['developpement durable', 'brundtland', 'soutenabilite'],
      dos=['n4-durable', 'n4-soutenabilites']),

   nd('justice', 'La justice climatique', 'limite',
      "Les pays riches ont la plus forte responsabilité historique ; les pays "
      "pauvres, la plus forte exposition et la plus faible capacité "
      "d’adaptation.",
      grp=3,
      defi="La justice climatique désigne l’exigence de répartir l’effort de "
           "lutte contre le changement climatique en tenant compte d’une "
           "double asymétrie : les pays développés sont historiquement les "
           "plus responsables des émissions de gaz à effet de serre, tandis "
           "que les pays les moins développés en subissent les effets les "
           "plus violents et disposent des plus faibles capacités "
           "d’adaptation.",
      mec=[("Le principe de responsabilités communes mais différenciées",
            "Les pays développés sont censés réduire davantage leurs "
            "émissions, financer une partie de la transition mondiale et "
            "aider les pays plus pauvres à se décarboner : trois obligations "
            "distinctes, dont deux financières."),
           ("L’empreinte incorporée dans les importations",
            "L’indice de développement humain classique surestime la "
            "performance des pays développés car il ne prend pas en compte "
            "l’empreinte écologique incorporée dans les importations : "
            "délocaliser la production déplace les émissions sans réduire la "
            "responsabilité du consommateur final.")],
      args=[{'a': "L’asymétrie entre responsabilité et exposition justifie "
                  "que l’effort soit réparti autrement qu’à proportion des "
                  "émissions courantes.",
             'lim': "Le principe ne dit pas comment répartir précisément : il "
                    "fixe une direction, pas une clé de calcul, ce qui "
                    "explique la difficulté des négociations climatiques."}],
      aut=[{'n': "Amartya Sen",
            'i': "Le développement se juge à l’étendue des capacités réelles "
                 "des individus, non au seul revenu."},
           {'n': "Garrett Hardin",
            'i': "Un bien commun non régulé est surexploité, chacun ayant "
                 "intérêt à laisser les autres supporter l’effort."}],
      faits=[{'f': "Le principe de responsabilités communes mais "
                   "différenciées anime l’esprit du protocole de Kyoto puis "
                   "des accords de Paris.",
              'p': "La justice climatique n’est pas une revendication "
                   "extérieure au droit international : elle y est inscrite."}],
      termes=['justice climatique', 'responsabilites communes',
              'accords de paris'],
      dos=['n4-justice-climatique', 'n4-climat']),
  ],
  [
   ln('question', 'faible', 'répondue par « oui »',
      "Répondre que les capitaux sont substituables, c’est adopter la "
      "soutenabilité faible : ce qui doit être transmis n’est pas un stock "
      "naturel déterminé mais une capacité de production dont la composition "
      "peut varier.", 'conditionne'),
   ln('question', 'forte', 'répondue par « non »',
      "Répondre que le capital naturel est irremplaçable, c’est adopter la "
      "soutenabilité forte : certaines pertes sont définitives et ne se "
      "compensent par aucune accumulation d’un autre capital.",
      'conditionne'),
   ln('faible', 'verte', 'fonde',
      "La croissance verte n’a de fondement théorique que si le capital "
      "technologique peut compenser la baisse du capital naturel. Sans "
      "l’hypothèse de substituabilité, transformer le contenu de la "
      "croissance ne suffit pas.", 'cause'),
   ln('verte', 'decouplage', 'se vérifie par',
      "La croissance verte est une promesse vérifiable : elle suppose un "
      "découplage absolu, c’est-à-dire un PIB qui augmente tandis que les "
      "émissions diminuent. Le découplage relatif, lui, ne suffit pas à "
      "atteindre un objectif de réduction.", 'mesure'),
   ln('verte', 'instruments', 'a besoin d’un signal',
      "Transformer le contenu de la croissance suppose que l’émission cesse "
      "d’être gratuite. Le prix du carbone, les quotas ou la norme sont les "
      "instruments qui rendent la décarbonation rentable pour les entreprises.",
      'conditionne'),
   ln('forte', 'limites', 'repose sur',
      "La non-substituabilité n’est pas une préférence : elle s’appuie sur "
      "l’existence de seuils physiques — climat, biodiversité, pollution, "
      "ressources — au-delà desquels la dégradation devient durable, voire "
      "irréversible.", 'cause'),
   ln('forte', 'decroissance', 'conduit, dans sa version radicale, à',
      "Si aucune compensation technique ne vaut, l’ajustement doit porter sur "
      "les quantités prélevées. Le cours indique que certaines versions "
      "radicales de la soutenabilité forte vont jusqu’à défendre la "
      "décroissance : c’est une conséquence possible, non nécessaire.",
      'cause'),
   ln('rebond', 'verte', 'ronge les gains de',
      "Les gains d’efficacité obtenus par l’innovation verte peuvent être "
      "repris par la hausse des usages. L’argument n’annule pas la croissance "
      "verte mais l’oblige à se doubler d’une action sur les usages, c’est-à-"
      "dire sur la sobriété.", 'limite'),
   ln('limites', 'rebond', 'impose d’agir sur les usages',
      "Si la contrainte est un seuil absolu et non une performance par unité "
      "produite, alors seule une baisse absolue compte. L’effet rebond montre "
      "que l’efficacité seule ne la garantit pas : d’où le passage de "
      "l’efficacité à la sobriété.", 'cause'),
   ln('decouplage', 'decroissance', 'est l’enjeu empirique contre',
      "Si un découplage absolu suffisamment rapide est possible, la "
      "décroissance perd sa nécessité. S’il ne l’est pas, elle devient la "
      "seule voie. Le débat se ramène donc à une question mesurable plutôt "
      "qu’à une opposition de valeurs.", 'oppose'),
   ln('decouplage', 'justice', 'est faussé par la délocalisation',
      "Un découplage mesuré sur la production intérieure peut n’être qu’un "
      "transfert : l’empreinte incorporée dans les importations reste "
      "attribuable au consommateur final, ce qui relie directement la mesure "
      "du découplage à la question de la responsabilité.", 'limite'),
   ln('instruments', 'justice', 'bute sur l’acceptabilité',
      "La taxe carbone frappe des consommations contraintes comme le "
      "chauffage et les déplacements. La tension entre politiques climatiques "
      "et politiques sociales plaide pour une redistribution des recettes, "
      "non pour l’abandon du signal-prix.", 'limite'),
   ln('arbitrage', 'question', 'reformule',
      "Le cours conclut que la question n’est plus de savoir s’il faut de la "
      "croissance mais quel type de croissance est compatible avec le "
      "développement durable : la substituabilité se juge ressource par "
      "ressource, non en bloc.", 'renforce'),
   ln('verte', 'arbitrage', 'y conduit par le contenu',
      "La position de la croissance verte aboutit à l’arbitrage par le "
      "contenu : innover, décarboner, accompagner les perdants. Elle accepte "
      "donc la contrainte écologique sans accepter la réduction des volumes.",
      'cause'),
   ln('decroissance', 'arbitrage', 'y conduit par les volumes',
      "La position décroissante aboutit au même arbitrage par l’autre bout : "
      "puisque le contenu ne suffit pas, il faut agir sur les volumes. Les "
      "deux colonnes se rejoignent sur la question du rythme du découplage.",
      'cause'),
  ],
  bandes=[(1, 'Si les capitaux sont substituables'),
          (2, 'Si le capital naturel est irremplaçable'),
          (3, 'Ce qui permet d’arbitrer')],
  fam='Croissance et développement')
