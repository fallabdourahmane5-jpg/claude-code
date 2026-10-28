# -*- coding: utf-8 -*-
"""Visualisation 19 — Court terme et long terme (type duel)."""

from vz_base import v, nd, ln

v('vz-court-long', 'Court terme et long terme',
  'Transversal · une divergence sur le temps qui commande tout le reste',
  'duel',
  "La divergence sur le temps n’est pas un point secondaire : elle commande "
  "les positions sur l’équilibre, le chômage, l’épargne et la monnaie, qui "
  "en découlent toutes. À gauche, un temps où les ajustements sont rapides "
  "et l’avenir calculable ; à droite, un temps historique où le futur n’est "
  "pas probabilisable. En bas, ce qui relie les deux horizons et les "
  "arbitrages qu’il faut expliciter.",
  [("Une divergence, pas deux sujets",
    "Selon l’horizon retenu, les déterminants de l’activité et les "
    "instruments de politique économique diffèrent entièrement. Poser la "
    "question du temps avant celle des remèdes évite de comparer des "
    "réponses qui ne portent pas sur le même objet."),
   ("À court terme la demande, à long terme les capacités",
    "Court terme : demande globale insuffisante, production faible, chômage "
    "involontaire, donc politique budgétaire et monétaire. Long terme : "
    "capacités productives, productivité, institutions, donc éducation, "
    "innovation, montée en gamme. Les leviers ne sont pas "
    "interchangeables."),
   ("Les deux horizons interfèrent",
    "Une insuffisance durable de demande déprime l’investissement, donc les "
    "capacités futures : le court terme peut abîmer le long terme. C’est "
    "l’argument qui interdit de traiter les deux horizons séparément.")],
  [
   nd('horizon', 'Quel est le bon horizon d’analyse ?', 'coeur',
      "Les ajustements sont-ils rapides, et l’avenir est-il calculable ? De "
      "la réponse découlent le diagnostic du chômage, le rôle de la monnaie "
      "et le choix des instruments.",
      grp=0,
      defi="Le débat porte sur la pertinence de l’horizon d’analyse. Le cours "
           "oppose un raisonnement classique statique ou de long terme, avec "
           "des ajustements supposés rapides, et un temps keynésien "
           "historique et incertain où les décisions sont prises sous "
           "incertitude radicale et où le futur n’est pas calculable. L’enjeu "
           "n’est pas seulement de méthode : selon l’horizon retenu, les "
           "déterminants de l’activité et les instruments de politique "
           "économique diffèrent entièrement.",
      mec=[("L’horizon fixe la vitesse supposée des ajustements",
            "Si les prix et les salaires reviennent rapidement à l’équilibre, "
            "un déséquilibre observé n’est qu’un état transitoire ; s’ils "
            "sont lents ou impossibles, il peut s’installer."),
           ("L’horizon fixe la nature de l’information disponible",
            "Si l’avenir est probabilisable, les agents prévoient, anticipent "
            "et calculent. Si le temps est historique et incertain, le futur "
            "n’est pas calculable et les décisions reposent sur la "
            "confiance."),
           ("L’horizon commande le déterminant de l’activité",
            "À court terme, c’est la demande effective ; à long terme, ce "
            "sont les capacités productives, la productivité et les "
            "institutions. Le même phénomène n’a pas la même cause selon "
            "l’échelle de temps retenue.")],
      faits=[{'f': "La Nouvelle Économie Keynésienne affirme que la monnaie "
                   "n’est pas neutre à court et moyen terme, formulation qui "
                   "borne explicitement l’horizon de validité de la "
                   "proposition.",
              'p': "Les positions contemporaines ne tranchent pas entre les "
                   "deux horizons mais les distinguent : la même grandeur "
                   "peut être active à court terme et neutre à long terme."}],
      termes=['court terme', 'long terme', 'horizon temporel'],
      dos=['n26-court-long-terme', 'n26-equilibre-desequilibre']),

   # ------------------------------------- colonne 1 : le temps des ajustements
   nd('ajustement', 'Les ajustements sont rapides', 'pilier',
      "Prix et salaires reviennent à l’équilibre : un déséquilibre observé "
      "n’est qu’un état transitoire, et il suffit d’attendre.",
      grp=1,
      defi="Dans le raisonnement classique, statique ou de long terme, les "
           "ajustements sont supposés rapides : les prix et les salaires "
           "reviennent à l’équilibre, de sorte qu’un déséquilibre observé "
           "n’est qu’un état transitoire. La conséquence pratique est "
           "immédiate : l’intervention est au mieux inutile, puisque le "
           "mécanisme corrige de lui-même, et au pire nuisible, puisqu’elle "
           "perturbe la correction en cours.",
      mec=[("Le déséquilibre comme écart transitoire",
            "Si le prix s’ajuste, un excès d’offre fait baisser le prix "
            "jusqu’au rétablissement de l’équilibre : le chômage ne peut être "
            "qu’un épisode, non un état."),
           ("La conclusion sur la politique économique",
            "Puisque la correction est en cours, agir revient à ajouter une "
            "perturbation à un système qui se répare : d’où la préférence "
            "pour des règles stables plutôt que pour des décisions "
            "discrétionnaires.")],
      opp=[{'t': "À long terme, l’économie revient à l’équilibre : il suffit "
                 "de laisser les prix et les salaires s’ajuster.",
            'qui': "position classique",
            'rep': "Keynes répond qu’il existe un équilibre de sous-emploi : "
                   "le chômage est possible même à l’équilibre et l’économie "
                   "peut être stable mais inefficace. Si le mauvais état est "
                   "lui-même un équilibre, attendre ne produit aucune "
                   "correction."}],
      aut=[{'n': "Milton Friedman",
            'i': "Il existe un taux de chômage naturel, incompressible, lié "
                 "aux frictions du marché du travail."}],
      termes=['ajustement par les prix', 'equilibre', 'flexibilite'],
      dos=['n26-equilibre-desequilibre', 'n26-autoregulation-instabilite']),

   nd('calcul', 'L’avenir est calculable', 'pilier',
      "Les agents prévoient, anticipent et répartissent leur consommation sur "
      "l’ensemble de leur cycle de vie : court et long terme se confondent "
      "dans leurs décisions.",
      grp=1,
      defi="Si l’avenir est probabilisable, les agents peuvent prévoir, "
           "anticiper et calculer rationnellement. Le cours cite à ce propos "
           "le modèle du cycle de vie, où le consommateur prépare sa "
           "retraite, anticipe ses revenus futurs et organise sa "
           "consommation. Dans cette hypothèse, la distinction des horizons "
           "perd une partie de son intérêt : l’agent intègre lui-même le long "
           "terme dans ses décisions présentes.",
      mec=[("Le lissage intertemporel",
            "La consommation ne suit pas le revenu courant mais le revenu "
            "attendu sur l’ensemble du cycle de vie : l’épargne sert à "
            "transférer du pouvoir d’achat entre périodes."),
           ("La neutralisation des politiques",
            "Si les agents anticipent correctement, une politique annoncée "
            "n’agit que sur les variables nominales : l’effet réel disparaît "
            "avant même de se produire.")],
      opp=[{'t': "La distinction des horizons est artificielle : les agents "
                 "raisonnent sur l’ensemble de leur cycle de vie, de sorte "
                 "que court et long terme se confondent dans leurs "
                 "décisions.",
            'qui': "lecture par le cycle de vie",
            'rep': "Le cours oppose deux résultats : Simon montre que la "
                   "rationalité est limitée par l’information, le temps et "
                   "les capacités de calcul, et Bronner que les individus "
                   "privilégient souvent les satisfactions immédiates."}],
      aut=[{'n': "Franco Modigliani",
            'i': "Les individus répartissent consommation et épargne sur "
                 "l’ensemble de leur cycle de vie."},
           {'n': "Thomas Sargent",
            'i': "Une politique annoncée n’agit que sur les variables "
                 "nominales, puisque les agents en intègrent les effets par "
                 "avance."}],
      termes=['cycle de vie', 'anticipations rationnelles',
              'revenu permanent'],
      dos=['n26-rationalite-parfaite-limitee', 'n15-anticipations']),

   nd('capacites', 'Ce qui compte à long terme', 'detail',
      "Capital physique, humain, naturel, technologique, social, "
      "institutionnel : la croissance dépend de stocks qui se construisent "
      "lentement.",
      grp=1, par='ajustement',
      defi="À long terme, le niveau d’activité ne dépend plus de la demande "
           "mais des capacités productives : le stock de capital, la "
           "qualification de la main-d’œuvre, le progrès technique et la "
           "qualité des institutions. Le cours énumère six capitaux dont "
           "dépend la croissance — physique, humain, naturel, technologique, "
           "social et institutionnel — et c’est leur accumulation, non la "
           "dépense courante, qui détermine la trajectoire.",
      mec=[("L’accumulation plutôt que la dépense",
            "Ce qui élève durablement la production est l’investissement, "
            "l’éducation et la recherche : des dépenses dont le rendement est "
            "différé et cumulatif."),
           ("L’inertie des institutions",
            "Les institutions évoluent lentement, et les choix passés "
            "conditionnent fortement les trajectoires futures : la dépendance "
            "au sentier fait peser le passé sur l’avenir."),
           ("Les instruments correspondants",
            "Éducation, innovation, montée en gamme, qualité des "
            "institutions : ce ne sont pas des instruments conjoncturels, et "
            "ils ne produisent pas d’effet mesurable à l’échelle d’un cycle.")],
      aut=[{'n': "Douglass North",
            'i': "Les institutions évoluent lentement, et les choix passés "
                 "conditionnent fortement les trajectoires futures."}],
      termes=['croissance potentielle', 'capital humain', 'institutions',
              'productivite'],
      dos=['n1-productivite', 'n26-institutions-comportements']),

   # --------------------------------------- colonne 2 : le temps incertain
   nd('incertitude', 'Le temps est historique et incertain', 'pilier',
      "Les décisions sont prises sous incertitude radicale : le futur n’est "
      "pas calculable, et l’investissement dépend de la confiance.",
      grp=2,
      defi="Pour Keynes, le temps est historique et incertain : les décisions "
           "sont prises sous incertitude radicale et le futur n’est pas "
           "calculable. La différence avec le risque est décisive : un risque "
           "se probabilise et s’assure, une incertitude radicale ne le peut "
           "pas. L’investissement dépend alors des anticipations, de la "
           "confiance et des esprits animaux, non du seul taux d’intérêt.",
      mec=[("Incertitude et risque ne se confondent pas",
            "Si l’avenir n’est pas probabilisable, aucun calcul d’espérance "
            "ne guide la décision : ce qui la détermine est un état "
            "d’esprit collectif autant qu’un raisonnement individuel."),
           ("La conséquence sur l’investissement",
            "L’investissement devient la variable la plus volatile de "
            "l’économie : il peut s’effondrer sans qu’aucun paramètre "
            "objectif n’ait changé, par simple retournement des "
            "anticipations."),
           ("La préférence pour la liquidité",
            "Dans un monde incertain, conserver de la monnaie a une valeur "
            "propre : la rencontre entre épargne et investissement cesse "
            "d’être automatique.")],
      aut=[{'n': "John Maynard Keynes",
            'i': "Le temps est historique et incertain : les décisions sont "
                 "prises sous incertitude radicale et le futur n’est pas "
                 "calculable."},
           {'n': "Herbert Simon",
            'i': "La rationalité est limitée par l’information, le temps et "
                 "les capacités de calcul."}],
      termes=['incertitude radicale', 'esprits animaux',
              'preference pour la liquidite'],
      dos=['n26-rationalite-parfaite-limitee', 'n11-preference-liquidite']),

   nd('rigidites', 'Pourquoi les ajustements sont lents', 'pilier',
      "Contrats de long terme, coûts de modification des prix, normes "
      "sociales, conventions salariales : quatre raisons identifiées.",
      grp=2,
      defi="La Nouvelle Économie Keynésienne explique précisément pourquoi le "
           "court terme ne ressemble pas au long terme. Elle identifie quatre "
           "rigidités : contrats de long terme, coûts de modification des "
           "prix, normes sociales, conventions salariales. Les ajustements "
           "par les prix sont alors lents ou impossibles, ce qui donne au "
           "court terme une consistance propre.",
      mec=[("Les contrats et les coûts de changement",
            "Un prix ou un salaire fixé par contrat ne s’ajuste pas avant "
            "l’échéance, et modifier un prix coûte quelque chose : "
            "l’inertie n’est pas une irrationalité mais un calcul."),
           ("Les normes et les conventions",
            "Certaines rigidités ne sont pas contractuelles mais sociales : "
            "baisser un salaire nominal se heurte à une norme d’équité dont "
            "la transgression a un coût pour l’employeur."),
           ("La conséquence théorique",
            "Si l’ajustement passe par les quantités plutôt que par les prix, "
            "le rationnement devient possible et durable : production et "
            "emploi s’ajustent à la place du prix.")],
      args=[{'a': "Les rigidités fournissent un fondement microéconomique à "
                  "l’analyse keynésienne : le sous-emploi n’est plus postulé "
                  "mais déduit de comportements rationnels.",
             'lim': "La Nouvelle Économie Classique objecte que les erreurs "
                    "sont rapidement corrigées et qu’il n’existe pas "
                    "d’illusion monétaire durable : si les anticipations sont "
                    "cohérentes, le court terme se résorbe vite."}],
      termes=['rigidites', 'nouvelle economie keynesienne',
              'contrats de long terme'],
      dos=['n26-equilibre-desequilibre', 'n10-marche-travail']),

   nd('demande', 'Ce qui compte à court terme', 'detail',
      "Demande globale insuffisante, production faible, chômage "
      "involontaire : le court terme a ses propres déterminants.",
      grp=2, par='incertitude',
      defi="À court terme, le déterminant de l’activité est la demande "
           "effective : la production et l’emploi dépendent de la dépense "
           "anticipée par les entreprises. Une demande globale insuffisante "
           "produit une production faible et un chômage involontaire, et "
           "cette situation peut être stable. Les instruments correspondants "
           "sont la politique budgétaire et la politique monétaire, qui "
           "agissent sur la dépense et non sur les capacités.",
      mec=[("L’équilibre de sous-emploi",
            "Les entreprises sont satisfaites de leur production, les ménages "
            "consomment ce qu’ils peuvent, les marchés sont stables — et il "
            "existe pourtant du chômage. Le court terme n’est plus une étape "
            "vers le long terme."),
           ("Les instruments de court terme",
            "Politique budgétaire et politique monétaire soutiennent la "
            "demande : leur effet est rapide mais ne modifie pas les "
            "capacités productives, donc ne change pas la trajectoire de long "
            "terme.")],
      faits=[{'f': "La croissance potentielle est définie comme le rythme "
                   "atteignable en l’absence de choc de demande, crise, chute "
                   "de la consommation ou baisse de l’investissement.",
              'p': "La définition montre que le choc de demande est intégré "
                   "au vocabulaire courant de la croissance : une économie "
                   "peut avoir un potentiel et ne pas l’atteindre faute de "
                   "demande."}],
      aut=[{'n': "John Maynard Keynes",
            'i': "L’emploi dépend de la demande globale, pas du seul marché "
                 "du travail."}],
      termes=['demande effective', 'politique conjoncturelle',
              'chomage involontaire'],
      dos=['n13-crises-demande', 'n15-politique-relance']),

   # ---------------------------------------- bas : ce qui relie les horizons
   nd('interference', 'Le court terme abîme le long terme', 'sortie',
      "Une insuffisance durable de demande déprime l’investissement, donc les "
      "capacités futures. Les deux horizons ne sont pas étanches.",
      grp=3,
      defi="L’argument décisif contre la séparation des horizons est "
           "l’interférence. Le cours montre qu’une insuffisance durable de "
           "demande déprime l’investissement, donc les capacités productives "
           "futures : ce qui relève du court terme finit par déterminer le "
           "long terme. Symétriquement, la réduction des inégalités dépend de "
           "la redistribution et des politiques sociales, instruments de "
           "court terme aux effets durables.",
      mec=[("L’investissement comme charnière",
            "Il est à la fois un élément de la demande et un élément de "
            "l’offre : c’est par lui qu’une fluctuation conjoncturelle se "
            "transmet aux capacités productives, donc au potentiel."),
           ("L’hystérèse",
            "Un chômage prolongé dégrade les compétences et éloigne "
            "durablement de l’emploi : un choc transitoire peut produire des "
            "effets permanents, ce qui est exactement une contamination du "
            "long terme par le court terme."),
           ("La réciproque",
            "Des instruments de court terme peuvent avoir des effets "
            "durables : la redistribution et les politiques sociales "
            "modifient la trajectoire des inégalités bien au-delà de "
            "l’exercice budgétaire où elles sont décidées.")],
      opp=[{'t': "Raisonner à court terme conduit à sacrifier l’avenir : "
                 "soutenir la demande par le déficit reporte la charge sur "
                 "les générations futures et détourne des réformes "
                 "structurelles.",
            'qui': "objection de long terme",
            'rep': "Le cours fournit la réponse symétrique : une insuffisance "
                   "durable de demande déprime l’investissement, donc les "
                   "capacités productives futures. Le sacrifice peut venir "
                   "des deux côtés."}],
      termes=['hysterese', 'investissement', 'croissance potentielle'],
      dos=['n13-accelerateur', 'n26-court-long-terme']),

   nd('arbitrages', 'Les arbitrages à expliciter', 'limite',
      "Soutenabilité, protection éducatrice, inertie institutionnelle, biais "
      "pour l’immédiat : quatre terrains où l’horizon décide.",
      grp=3,
      defi="Plusieurs raisonnements du programme n’ont de sens que si l’on "
           "distingue explicitement les horizons. La soutenabilité demande si "
           "l’on peut préserver la capacité de croissance sans détruire "
           "certains capitaux. Le protectionnisme éducateur suppose une "
           "protection temporaire au bénéfice d’un avantage futur. Les "
           "institutions évoluent lentement. Et les comportements eux-mêmes "
           "privilégient l’immédiat.",
      mec=[("L’arbitrage entre stocks",
            "Un gain de court terme sur le capital physique peut se payer "
            "d’une perte durable de capital naturel : l’arbitrage temporel "
            "devient un arbitrage entre stocks."),
           ("La protection temporaire et son risque",
            "L’argument de l’industrie naissante suppose une extinction "
            "programmée. Le Public Choice montre le risque : les avantages "
            "accordés créent des rentes, le lobbying augmente, et les "
            "ressources consacrées à conserver la protection se substituent à "
            "l’amélioration de la productivité."),
           ("Le biais comportemental",
            "Les individus privilégient souvent les satisfactions immédiates "
            "plutôt que les bénéfices futurs : l’arbitrage temporel ne se "
            "règle pas spontanément, ce qui justifie des engagements "
            "institutionnels.")],
      args=[{'a': "Expliciter le taux auquel on arbitre entre présent et "
                  "futur transforme un désaccord doctrinal en question "
                  "discutable : on cesse de s’opposer sur des principes pour "
                  "discuter d’une valeur.",
             'lim': "Le cours pose la question sans la trancher et ne "
                    "fournit pas de critère permettant de déterminer quel "
                    "niveau de destruction d’un capital serait acceptable : "
                    "l’arbitrage reste une décision politique."}],
      aut=[{'n': "Gérald Bronner",
            'i': "Les individus privilégient souvent les satisfactions "
                 "immédiates plutôt que les bénéfices futurs."}],
      termes=['soutenabilite', 'protectionnisme educateur',
              'dependance au sentier'],
      dos=['n4-soutenabilites', 'le28-educateur']),
  ],
  [
   ln('horizon', 'ajustement', 'répondue par « rapides »',
      "Supposer des ajustements rapides, c’est faire du long terme l’horizon "
      "pertinent : le déséquilibre observé n’est qu’un passage, et la "
      "politique n’a rien à corriger.", 'conditionne'),
   ln('horizon', 'incertitude', 'répondue par « incalculable »',
      "Supposer un temps historique et incertain, c’est donner au court terme "
      "une consistance propre : les décisions reposent sur la confiance, et "
      "l’économie peut s’installer dans un mauvais état.", 'conditionne'),
   ln('ajustement', 'calcul', 'suppose aussi',
      "L’ajustement rapide ne suffit pas : il faut encore que les agents "
      "sachent vers quoi ils s’ajustent. L’hypothèse d’un avenir "
      "probabilisable complète celle de la flexibilité des prix.",
      'renforce'),
   ln('ajustement', 'capacites', 'renvoie l’analyse vers',
      "Si le court terme se corrige de lui-même, la seule question qui reste "
      "est celle des capacités : capital, qualification, progrès technique, "
      "institutions. Le long terme devient le seul objet digne d’analyse.",
      'cause'),
   ln('incertitude', 'rigidites', 'se complète de',
      "L’incertitude explique pourquoi les décisions sont fragiles ; les "
      "rigidités expliquent pourquoi les prix ne corrigent pas. Les deux "
      "arguments sont indépendants et se cumulent.", 'renforce'),
   ln('incertitude', 'demande', 'fait du court terme',
      "Si l’investissement dépend des anticipations et de la confiance, alors "
      "la dépense anticipée commande la production : la demande effective "
      "devient le déterminant de l’activité.", 'cause'),
   ln('rigidites', 'ajustement', 'contredit',
      "Contrats de long terme, coûts de modification des prix, normes "
      "sociales, conventions salariales : quatre raisons pour lesquelles "
      "l’ajustement supposé rapide ne se produit pas.", 'oppose'),
   ln('calcul', 'incertitude', 's’oppose frontalement à',
      "Un avenir probabilisable autorise le calcul et le lissage "
      "intertemporel ; une incertitude radicale l’interdit. Toute la "
      "divergence sur le comportement des agents se loge dans cette "
      "alternative.", 'oppose'),
   ln('demande', 'capacites', 'ne modifie pas',
      "Soutenir la dépense agit vite mais ne change pas le stock de capital "
      "ni la qualification : les instruments de court terme ne déplacent pas "
      "la trajectoire de long terme, et réciproquement.", 'limite'),
   ln('demande', 'interference', 'finit pourtant par agir sur le long terme',
      "Une insuffisance durable de demande déprime l’investissement, donc les "
      "capacités futures. L’investissement est la charnière par laquelle le "
      "court terme contamine le long terme.", 'cause'),
   ln('capacites', 'interference', 'est entamé par le court terme',
      "L’hystérèse en donne la forme la plus nette : un chômage prolongé "
      "dégrade les compétences et éloigne durablement de l’emploi. Un choc "
      "transitoire produit alors des effets permanents.", 'limite'),
   ln('interference', 'horizon', 'interdit de séparer',
      "Si les deux horizons interfèrent, la question initiale change de "
      "forme : il ne s’agit plus de choisir un horizon mais d’articuler les "
      "deux, en mesurant ce que chaque décision coûte à l’autre échelle.",
      'renforce'),
   ln('arbitrages', 'horizon', 'exige d’expliciter le taux',
      "Soutenabilité, protection temporaire, inertie institutionnelle : "
      "chacun de ces raisonnements suppose un taux auquel on arbitre entre "
      "présent et futur. L’expliciter transforme le désaccord doctrinal en "
      "question discutable.", 'conditionne'),
   ln('calcul', 'arbitrages', 'est démentie par le biais pour l’immédiat',
      "Les individus privilégient souvent les satisfactions immédiates "
      "plutôt que les bénéfices futurs : l’arbitrage intertemporel supposé "
      "par le modèle du cycle de vie ne se réalise pas spontanément.",
      'limite'),
   ln('capacites', 'arbitrages', 'rend lents les effets des politiques',
      "Les institutions évoluent lentement et la dépendance au sentier fait "
      "peser les choix passés sur les trajectoires futures : agir sur le long "
      "terme suppose d’accepter que l’effet ne soit pas visible dans "
      "l’horizon d’une décision politique.", 'conditionne'),
  ],
  bandes=[(1, 'Un temps où les ajustements sont rapides'),
          (2, 'Un temps historique et incertain'),
          (3, 'Ce qui relie les deux horizons')],
  fam='Société, inégalités et transversal')
