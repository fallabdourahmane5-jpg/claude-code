# -*- coding: utf-8 -*-
"""Visualisation 13 — Crises et politiques publiques (type cycle)."""

from vz_base import v, nd, ln

v('vz-crises', 'Crises économiques et réponses des politiques publiques',
  'Chapitre 2 · du choc initial au retour du cycle',
  'cycle',
  "Une crise n’est jamais un événement isolé : un choc initial est amplifié "
  "par le revenu, par l’investissement et par le crédit, puis les politiques "
  "publiques tentent de briser l’enchaînement — avec leurs propres limites. "
  "Cette visualisation suit ce cycle complet et montre où chaque instrument "
  "s’insère.",
  [("Identifier le choc avant de prescrire",
    "Un choc d’offre et un choc de demande n’appellent pas le même remède : "
    "soutenir la demande face à un choc d’offre nourrit l’inflation sans "
    "rétablir la production. La stagflation des années 1970 est le cas "
    "d’école."),
   ("Trois amplificateurs, pas un",
    "Le multiplicateur amplifie par le revenu, l’accélérateur par "
    "l’investissement, le cycle du crédit par le financement. L’oscillateur "
    "de Samuelson relie les deux premiers ; le troisième explique pourquoi "
    "les crises financières sont les plus profondes."),
   ("Le cycle se referme",
    "Les limites des politiques — dette, éviction, ouverture, anticipations — "
    "déterminent la marge disponible lors du choc suivant. C’est ce bouclage "
    "qui fait des crises une série plutôt qu’une succession d’accidents.")],
  [
   nd('cycles', 'Cycles, potentiel et output gap', 'coeur',
      "Kitchin 3-5 ans, Juglar 8-10 ans, Kondratiev 50-60 ans : trois "
      "temporalités qui se superposent. L’écart au potentiel mesure la "
      "position dans le cycle.",
      grp=0,
      defi="Les cycles économiques sont des mouvements récurrents "
           "d’expansion et de ralentissement de l’activité. Le cours en "
           "distingue trois types selon leur durée : les cycles courts de "
           "Kitchin, de trois à cinq ans ; les cycles moyens de Juglar, de "
           "huit à dix ans ; les cycles longs de Kondratiev, de cinquante à "
           "soixante ans. Ces trois temporalités ne s’excluent pas : elles se "
           "superposent et s’emboîtent.",
      mec=[("Le classement par la durée",
            "Les trois ordres de grandeur sont l’outil de classement du "
            "cours : ils permettent de rattacher un épisode observé à sa "
            "cause dominante — stocks, investissement et crédit, ou grappe "
            "d’innovations — plutôt que de parler de « crise » "
            "indistinctement."),
           ("Le PIB potentiel comme référence",
            "Le potentiel est défini comme le rythme atteignable en "
            "l’absence de choc d’offre et de demande : il fournit la "
            "trajectoire par rapport à laquelle un écart devient mesurable."),
           ("La lecture de l’output gap",
            "Un écart positif signale une surchauffe et des tensions "
            "inflationnistes possibles : les entreprises peuvent décider "
            "d’augmenter les prix au lieu d’augmenter les capacités de "
            "production.")],
      aut=[{'n': "Joseph Kitchin",
            'i': "Les cycles courts, de trois à cinq ans, tiennent aux "
                 "variations de stocks."},
           {'n': "Clément Juglar",
            'i': "Les cycles moyens, de huit à dix ans, suivent "
                 "l’investissement productif et le crédit."},
           {'n': "Nikolaï Kondratiev",
            'i': "Les cycles longs, de cinquante à soixante ans, se "
                 "décomposent en une phase ascendante et une phase "
                 "descendante."}],
      termes=['cycles economiques', 'output gap', 'croissance potentielle'],
      dos=['n13-cycles-economiques', 'n13-chocs-offre-demande']),

   nd('choc', 'Le choc initial : offre ou demande', 'pilier',
      "Les chocs d’offre frappent les conditions de production, les chocs de "
      "demande frappent la dépense. Le diagnostic commande le remède.",
      grp=1,
      defi="Un choc est une perturbation qui écarte l’activité de sa "
           "trajectoire soutenable. Le cours les classe en deux familles : "
           "les chocs d’offre, qui frappent les conditions de production, et "
           "les chocs de demande, qui frappent la dépense. La distinction "
           "n’est pas académique : elle détermine entièrement la réponse "
           "pertinente.",
      mec=[("Le choc d’offre",
            "Une hausse des coûts de production entraîne un fort taux de "
            "licenciement, donc une forte hausse du chômage, sans qu’aucune "
            "insuffisance de demande initiale soit en cause."),
           ("Le choc de demande",
            "L’économie repose sur la demande : une chute de la consommation "
            "ou de l’investissement suffit à faire décrocher la production, "
            "indépendamment de l’état des capacités productives."),
           ("La configuration qui tranche",
            "La stagflation associe stagnation de la production et inflation, "
            "configuration que la courbe de Phillips jugeait improbable : "
            "c’est l’observation qui a imposé de distinguer les deux "
            "familles.")],
      aut=[{'n': "Roy Harrod",
            'i': "Le taux de croissance effectif dépend notamment des chocs "
                 "d’offre et des chocs de demande."},
           {'n': "John Maynard Keynes",
            'i': "L’économie repose sur la demande, de sorte qu’un choc de "
                 "dépense suffit à faire décrocher la production."}],
      faits=[{'f': "En 1973 survient un premier choc pétrolier, suivi d’un "
                   "second en 1979 ; le baril passe au total de cinq à trente "
                   "dollars.",
              'p': "Le fait fournit l’exemple canonique de choc d’offre, et "
                   "le cours conclut que la courbe de Phillips est détruite "
                   "expérimentalement puisque l’inflation n’a pas fait "
                   "baisser le chômage."}],
      termes=['choc d offre', 'choc de demande', 'stagflation'],
      dos=['n13-chocs-offre-demande', 'n13-crises-demande']),

   nd('multiplicateur', 'L’amplification par le revenu', 'pilier',
      "Mévente, licenciements, baisse des revenus, nouvelle baisse de la "
      "consommation : un cercle vicieux dépressif qui s’auto-entretient.",
      grp=1,
      defi="Le multiplicateur décrit l’amplification d’une variation "
           "initiale de dépense par les revenus qu’elle engendre ou "
           "supprime. Dans une crise de demande, il joue à la baisse : le "
           "cours décrit explicitement un cercle vicieux dépressif — "
           "mévente, licenciements, baisse des revenus, nouvelle baisse de la "
           "consommation. L’enchaînement est cumulatif : il ne tend pas vers "
           "un équilibre de plein emploi.",
      mec=[("La propagation par le revenu",
            "La dépense de l’un est le revenu de l’autre : toute variation "
            "initiale se répercute en vagues successives, dont l’ampleur "
            "dépend de la part du revenu effectivement consommée."),
           ("L’absence de retour spontané",
            "Rien dans le mécanisme ne ramène l’économie au plein emploi : "
            "elle peut se stabiliser durablement en sous-emploi, ce qui "
            "justifie une intervention extérieure au circuit."),
           ("L’érosion par l’ouverture",
            "Le multiplicateur tombe de cinq en économie fermée à deux et "
            "demi en économie ouverte : une part de la relance fuit vers les "
            "importations.")],
      aut=[{'n': "John Maynard Keynes",
            'i': "L’emploi dépend de la demande globale, pas du seul marché "
                 "du travail."},
           {'n': "Thomas Malthus",
            'i': "La demande effective est la demande réellement solvable, et "
                 "son insuffisance bloque l’économie."},
           {'n': "Robert Clower",
            'i': "Un agent rationné sur un marché transmet cette contrainte à "
                 "l’autre marché."}],
      faits=[{'f': "Avec une propension à consommer de zéro virgule huit, les "
                   "ménages consommant quatre-vingts pour cent de leur "
                   "revenu, le multiplicateur vaut cinq.",
              'p': "Le chiffre donne l’ordre de grandeur de l’amplification "
                   "par le revenu, premier maillon du bouclage que "
                   "l’accélérateur referme."}],
      termes=['multiplicateur', 'demande effective',
              'cercle vicieux depressif'],
      dos=['n13-crises-demande', 'n15-multiplicateur-budgetaire']),

   nd('accelerateur', 'L’amplification par l’investissement', 'pilier',
      "Une variation de la demande provoque une variation plus que "
      "proportionnelle de l’investissement — dans les deux sens.",
      grp=1,
      defi="Le principe de l’accélérateur, que le cours attribue à Aftalion "
           "et Clark, énonce qu’une variation de la demande provoque une "
           "variation plus que proportionnelle de l’investissement. Mesurée "
           "par la variation du PIB, une hausse de la demande entraîne une "
           "hausse plus forte de l’investissement, et une baisse une "
           "contraction également amplifiée : l’accélérateur joue dans les "
           "deux sens.",
      mec=[("L’amplification du retournement",
            "Il suffit que la demande cesse de croître pour que "
            "l’investissement de capacité devienne inutile : la commande "
            "d’équipements chute bien plus vite que la demande finale."),
           ("Le bouclage avec le multiplicateur",
            "L’oscillateur de Samuelson, daté de 1939, relie les deux "
            "principes en un mouvement cumulatif : variation de "
            "l’investissement, variation du revenu, variation de la demande."),
           ("La double nature de l’investissement",
            "L’investissement est à la fois un élément de la demande et un "
            "élément de l’offre : c’est le maillon par lequel une "
            "fluctuation de court terme se transmet aux capacités "
            "productives, donc au potentiel de long terme.")],
      aut=[{'n': "Aftalion",
            'i': "Une variation de la demande provoque une variation plus que "
                 "proportionnelle de l’investissement."},
           {'n': "Paul Samuelson",
            'i': "L’oscillateur relie multiplicateur et accélérateur en un "
                 "même mouvement cumulatif."}],
      termes=['accelerateur', 'oscillateur', 'investissement'],
      dos=['n13-accelerateur', 'n13-cycles-economiques']),

   nd('credit', 'Le relais du crédit', 'limite',
      "Expansion du crédit qui nourrit l’investissement et la spéculation, "
      "puis blocage qui aggrave la récession. Le cycle n’est pas symétrique.",
      grp=1,
      defi="Le cycle du crédit désigne l’alternance entre une phase "
           "d’expansion du crédit, qui nourrit l’investissement et la "
           "spéculation, et une phase de contraction, où le crédit se bloque "
           "et aggrave la récession. Le cours le reconstitue par trois "
           "voies : les cycles de Juglar, l’analyse de Hayek et le canal du "
           "crédit bancaire de la politique monétaire.",
      mec=[("L’emballement par les taux bas",
            "Une création monétaire excessive abaisse artificiellement les "
            "taux, provoque un surinvestissement et peut conduire à des "
            "crises : l’expansion contient la cause de son retournement."),
           ("Le blocage et la panique",
            "Au retournement, le financement se tarit : une panique bancaire "
            "survient lorsque les déposants réclament simultanément leur "
            "argent, de sorte que la banque ne peut plus faire face."),
           ("L’asymétrie du cycle",
            "La banque centrale peut freiner un emballement mais ne peut pas "
            "contraindre les banques à prêter ni les agents à emprunter : en "
            "trappe à liquidité, les taux sont déjà très bas et "
            "l’investissement ne repart pas.")],
      aut=[{'n': "Friedrich Hayek",
            'i': "Une création monétaire excessive abaisse artificiellement "
                 "les taux, provoque un surinvestissement et peut conduire à "
                 "des crises."},
           {'n': "Robert Merton",
            'i': "Une prophétie autoréalisatrice est une croyance qui "
                 "provoque les comportements qui la rendent vraie."}],
      faits=[{'f': "En 1720, les détenteurs veulent échanger leurs billets "
                   "contre de l’or, la Banque n’a plus de réserves, et c’est "
                   "la panique et l’effondrement.",
              'p': "Le cas d’école montre que l’éclatement vient d’une "
                   "demande de conversion vers un actif sûr, et non d’une "
                   "révision du jugement sur l’actif lui-même."}],
      termes=['cycle du credit', 'panique bancaire', 'trappe a liquidite'],
      dos=['n13-cycle-credit', 'n13-panique-bancaire',
           'n15-trappe-liquidite']),

   nd('budget', 'La réponse budgétaire', 'pilier',
      "Les stabilisateurs jouent seuls, puis la relance volontariste : "
      "soutenir la demande pour briser le cercle dépressif.",
      grp=1,
      defi="La réponse budgétaire utilise le budget des administrations "
           "publiques pour soutenir la demande. Le cours en distingue deux "
           "degrés : la réaction automatique du budget au ralentissement, et "
           "l’action volontariste par des mesures spécifiques de dépenses et "
           "de recettes. Le premier degré ne suppose aucune décision : il "
           "agit par la structure même du budget.",
      mec=[("Les stabilisateurs automatiques",
            "En ralentissement, les dépenses des administrations publiques "
            "augmentent et les recettes baissent simultanément : une partie "
            "du soutien est immédiate et n’attend aucune décision, donc "
            "aucun délai politique."),
           ("La relance volontariste",
            "Des mesures spécifiques — investissement public, transferts, "
            "baisses ciblées de prélèvements — complètent les stabilisateurs "
            "lorsque l’ampleur du choc les dépasse."),
           ("Le financement par la dette",
            "Une relance se solde par un déficit public financé par émission "
            "d’obligations : son coût futur dépend des taux auxquels l’État "
            "peut emprunter.")],
      faits=[{'f': "Le cours cite le plan Biden, destiné à construire et "
                   "rénover des infrastructures, routes, autoroutes et ponts.",
              'p': "L’exemple montre une relance orientée vers le capital "
                   "public : elle soutient la demande immédiate tout en "
                   "améliorant la productivité future."}],
      aut=[{'n': "Richard Musgrave",
            'i': "La stabilisation est l’une des trois fonctions propres de "
                 "l’État, à côté de l’allocation et de la redistribution."}],
      termes=['politique budgetaire', 'relance',
              'stabilisateurs automatiques'],
      dos=['n15-politique-relance', 'n15-stabilisateurs-automatiques']),

   nd('monetaire', 'La réponse monétaire', 'pilier',
      "Baisser les taux, puis, quand ils ne descendent plus, agir sur les "
      "bilans : quantitative easing, taux négatifs, liquidité.",
      grp=1,
      defi="La réponse monétaire agit d’abord sur le prix de la monnaie en "
           "abaissant les taux directeurs, ce qui réduit le coût du crédit et "
           "soutient l’investissement et la consommation. Lorsque les taux "
           "atteignent leur plancher, la banque centrale agit sur les bilans "
           "et les anticipations : achats massifs de titres, modification de "
           "la composition de son bilan, taux négatifs sur la facilité de "
           "dépôt.",
      mec=[("Le canal du taux",
            "Le taux directeur se transmet au coût du refinancement des "
            "banques, donc au taux des crédits accordés : c’est le canal "
            "conventionnel, rapide mais borné par le plancher des taux."),
           ("Les instruments non conventionnels",
            "Leurs objectifs sont de rétablir la liquidité, débloquer le "
            "crédit, éviter la déflation, stabiliser les marchés et soutenir "
            "l’activité : ils visent le blocage du financement, et pas "
            "seulement la faiblesse de la demande."),
           ("Le prêteur en dernier ressort",
            "Face à une panique de liquidité, la banque centrale fournit la "
            "monnaie centrale qui manque : elle empêche qu’un problème de "
            "liquidité ne devienne un problème de solvabilité.")],
      opp=[{'t': "En trappe à liquidité, les agents préfèrent conserver des "
                 "liquidités, les banques restent prudentes et "
                 "l’investissement ne repart pas suffisamment.",
            'qui': "le cours",
            'rep': "Le fait prouve qu’une crise de demande peut résister à "
                   "l’outil monétaire : baisser encore les taux ne suffit "
                   "plus et la politique monétaire conventionnelle devient "
                   "moins efficace, ce qui renvoie au budget."}],
      aut=[{'n': "Éric Monnet",
            'i': "La banque centrale contemporaine tend à devenir un acteur "
                 "plus large de la gouvernance économique."}],
      termes=['politique monetaire', 'quantitative easing',
              'taux directeurs'],
      dos=['n15-politique-monetaire', 'n11-banque-centrale']),

   nd('limites', 'Les limites des réponses', 'limite',
      "Dette, effet d’éviction, fuite par les importations, anticipations : "
      "chaque instrument porte sa propre contrainte.",
      grp=1,
      defi="Les politiques de stabilisation ne sont pas sans coût ni sans "
           "borne. Quatre limites reviennent dans le cours : le financement "
           "par la dette et sa soutenabilité, l’effet d’éviction du capital "
           "privé au-delà d’un certain niveau de dépense, la fuite d’une "
           "part de la relance vers les importations en économie ouverte, et "
           "la neutralisation par des agents qui anticipent la politique.",
      mec=[("La double borne de la dépense publique",
            "Dépenses trop faibles, sous-investissement collectif ; dépenses "
            "excessives, effet d’éviction du capital privé. Il existe donc un "
            "niveau optimal, ce qui transforme le débat doctrinal en question "
            "de niveau."),
           ("La contrainte extérieure",
            "L’ouverture divise par deux le multiplicateur : une relance "
            "isolée perd la moitié de son effet, ce qui plaide pour une "
            "coordination entre pays plutôt que pour l’abstention."),
           ("Le reproche du contretemps",
            "La critique monétariste soutient que les autorités publiques "
            "aggravent les cycles au lieu de les corriger : l’action arrive "
            "trop tard et amplifie le mouvement qu’elle devait amortir.")],
      aut=[{'n': "Milton Friedman",
            'i': "Les politiques de relance budgétaire sont inflationnistes "
                 "et l’État aggrave les cycles au lieu de les corriger."},
           {'n': "Robert Barro",
            'i': "Au-delà d’un niveau optimal, les dépenses publiques "
                 "évincent le capital privé."}],
      faits=[{'f': "Le multiplicateur tombe de cinq en économie fermée à deux "
                   "et demi en économie ouverte.",
              'p': "L’écart chiffré fournit le principal argument quantitatif "
                   "contre une relance isolée : l’ouverture divise par deux "
                   "l’effet attendu."}],
      termes=['effet d eviction', 'dette publique', 'contrainte exterieure'],
      dos=['n15-effet-eviction', 'n15-dette-publique',
           'n15-contrainte-exterieure']),

   nd('regime', 'Crise de cycle ou crise de régime ?', 'debat',
      "Boyer lit 1929 comme l’épuisement d’un mode de régulation, non comme "
      "un choc accidentel : le débat d’interprétation central du chapitre.",
      grp=1,
      defi="Un même épisode peut être lu de deux façons : comme une phase "
           "basse d’un cycle, donc comme un écart transitoire à une "
           "trajectoire inchangée, ou comme l’épuisement d’un régime "
           "d’accumulation, donc comme la fin d’une configuration "
           "institutionnelle. Robert Boyer analyse la crise de 1929 comme "
           "l’épuisement du mode de régulation concurrentiel, et non comme un "
           "choc accidentel. C’est le principal débat d’interprétation du "
           "cours sur les crises.",
      mec=[("La lecture cyclique",
            "Le choc écarte l’activité de son potentiel ; les politiques "
            "ramènent l’économie vers sa trajectoire. Le régime "
            "institutionnel n’est pas en cause et n’a pas à changer."),
           ("La lecture régulationniste",
            "Les institutions qui soutenaient l’accumulation — formes de la "
            "concurrence, rapport salarial, régime monétaire — cessent d’être "
            "cohérentes entre elles : la sortie de crise suppose alors une "
            "reconfiguration, non un simple soutien de la demande."),
           ("Ce que le choix implique pour l’action",
            "Dans le premier cas, l’instrument conjoncturel suffit ; dans le "
            "second, il stabilise sans résoudre, et la crise réapparaît tant "
            "que le régime n’a pas changé.")],
      aut=[{'n': "Robert Boyer",
            'i': "La crise de 1929 s’analyse comme l’épuisement du mode de "
                 "régulation concurrentiel, et non comme un choc accidentel."},
           {'n': "Joseph Schumpeter",
            'i': "Le capitalisme n’évolue pas de manière régulière mais par "
                 "grandes vagues d’innovations majeures."}],
      termes=['regulation', 'regime d accumulation', 'crise de 1929'],
      dos=['n13-cycles-economiques', 'n13-crises-surproduction']),
  ],
  [
   ln('cycles', 'choc', 'se déclenche par',
      "Le cycle fournit la trajectoire de référence ; le choc est ce qui l’en "
      "écarte. Mesurer l’écart au potentiel suppose donc d’avoir d’abord "
      "identifié la nature du choc, faute de quoi le diagnostic porte sur un "
      "symptôme.", 'cause'),
   ln('choc', 'multiplicateur', 'est amplifié par',
      "Un choc de demande ne reste pas localisé : la dépense de l’un étant le "
      "revenu de l’autre, la contraction se propage en vagues successives et "
      "s’auto-entretient — mévente, licenciements, baisse des revenus, "
      "nouvelle baisse de la consommation.", 'cause'),
   ln('multiplicateur', 'accelerateur', 'se double de',
      "L’oscillateur de Samuelson relie les deux principes : la variation de "
      "l’investissement modifie le revenu, qui modifie la demande, qui "
      "modifie à nouveau l’investissement. L’amplification devient "
      "cumulative.", 'renforce'),
   ln('accelerateur', 'credit', 'se transmet au',
      "L’investissement étant largement financé, son retournement se "
      "répercute immédiatement sur la demande de crédit. Les cycles de "
      "Juglar, de huit à dix ans, associent précisément investissement "
      "productif et fluctuations du crédit.", 'cause'),
   ln('credit', 'cycles', 'nourrit le cycle moyen',
      "L’alternance expansion-contraction du crédit est l’un des mécanismes "
      "cycliques reconnus par le cours : elle explique la périodicité de huit "
      "à dix ans mieux que les variations de stocks ou les grappes "
      "d’innovations.", 'renforce'),
   ln('credit', 'monetaire', 'appelle',
      "Le blocage du financement et la panique de liquidité sont deux des "
      "cinq risques que la banque centrale doit éviter : c’est au point où le "
      "crédit se bloque que l’intervention monétaire devient indispensable.",
      'cause'),
   ln('multiplicateur', 'budget', 'justifie',
      "Puisque rien dans le mécanisme ne ramène l’économie au plein emploi, "
      "il faut une dépense extérieure au circuit. Le multiplicateur est "
      "l’argument théorique de la relance autant que celui de la crise.",
      'cause'),
   ln('budget', 'multiplicateur', 'joue dans l’autre sens',
      "Le même mécanisme qui amplifie la contraction amplifie la relance : "
      "une dépense publique initiale engendre des revenus qui engendrent des "
      "dépenses. L’instrument et le problème partagent leur logique.",
      'renforce'),
   ln('monetaire', 'credit', 'tente de débloquer',
      "Les instruments non conventionnels visent à rétablir la liquidité, "
      "débloquer le crédit, éviter la déflation et stabiliser les marchés : "
      "ils s’attaquent au canal financier plutôt qu’à la demande elle-même.",
      'cause'),
   ln('monetaire', 'limites', 'bute sur',
      "En trappe à liquidité, les taux sont déjà très bas, les agents "
      "préfèrent conserver des liquidités et les banques restent prudentes : "
      "l’outil monétaire conventionnel perd son effet, ce qui renvoie au "
      "budget.", 'limite'),
   ln('budget', 'limites', 'rencontre',
      "Dette à financer, effet d’éviction au-delà d’un certain niveau, fuite "
      "par les importations : la relance budgétaire est bornée, et c’est sur "
      "ces bornes que se concentre la critique monétariste.", 'limite'),
   ln('limites', 'cycles', 'détermine la marge du choc suivant',
      "Le niveau d’endettement et la crédibilité acquises pendant un cycle "
      "fixent la capacité d’intervention lors du cycle suivant : c’est ce "
      "bouclage qui fait des crises une série plutôt qu’une succession "
      "d’accidents.", 'conditionne'),
   ln('regime', 'cycles', 'conteste la lecture par',
      "Lire 1929 comme l’épuisement d’un mode de régulation revient à nier "
      "que l’économie revienne spontanément à une trajectoire inchangée : la "
      "crise ne serait pas une phase du cycle mais la fin d’une "
      "configuration institutionnelle.", 'oppose'),
   ln('limites', 'regime', 'alimente le soupçon de',
      "Lorsque les instruments conjoncturels stabilisent sans résoudre et que "
      "la crise réapparaît, l’hypothèse d’une crise de régime devient la plus "
      "économe : ce ne sont pas les remèdes qui manquent, c’est le diagnostic "
      "qui est mal posé.", 'cause'),
  ],
  fam='Monnaie, finance et crises')
