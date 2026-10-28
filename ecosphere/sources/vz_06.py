# -*- coding: utf-8 -*-
"""Visualisation 6 — État et marché (type duel)."""

from vz_base import v, nd, ln

v('vz-etat-marche', 'État et marché',
  'Chapitres 3 et 5 · deux doctrines, un même budget',
  'duel',
  "La question n’est pas « faut-il un État ? » — les deux camps en "
  "supposent un — mais « que doit-il faire, et selon quelles modalités ? ». "
  "À gauche, les raisons de s’en remettre au marché : information dispersée, "
  "anticipations, défaillances de l’État. À droite, les raisons d’intervenir : "
  "défaillances du marché, fonctions de l’État providence, demande globale. "
  "En bas, les contraintes qui s’imposent aux deux.",
  [("Deux camps, une même structure d’argument",
    "Chaque colonne enchaîne un diagnostic, un mécanisme et une "
    "recommandation. Les opposer ligne à ligne — information, anticipations, "
    "efficacité — donne un plan de dissertation immédiatement utilisable."),
   ("Même l’État minimal est un État",
    "Le cours est net : la croissance dépend de la crédibilité des règles, de "
    "la sécurité juridique et de la protection de la propriété. L’État "
    "minimal au sens budgétaire n’est pas l’État absent, et c’est le point "
    "qui désamorce la plupart des copies caricaturales."),
   ("Le bas de la figure n’est pas un compromis",
    "Le carré magique et le policy mix ne réconcilient pas les deux camps : "
    "ils énoncent des contraintes que les deux doivent respecter. Tout "
    "choix de politique économique est un arbitrage entre objectifs "
    "incompatibles.")],
  [
   nd('question', 'Que doit faire l’État ?', 'coeur',
      "Le débat ne porte pas sur l’existence de l’État mais sur l’étendue de "
      "ses missions et sur le mode de son action : par règles ou par "
      "décisions au coup par coup.",
      grp=0,
      defi="La question de l’intervention publique se décompose en deux "
           "questions que le cours tient séparées. La première porte sur "
           "l’étendue : l’État doit-il se borner au cadre de l’échange ou "
           "agir sur l’activité, la répartition et l’allocation des "
           "ressources ? La seconde porte sur les modalités : doit-il suivre "
           "des règles simples, crédibles et stables, ou juger de chaque "
           "situation ? Les deux débats sont indépendants : on peut vouloir "
           "un État étendu mais réglé, ou un État restreint mais "
           "discrétionnaire.",
      mec=[("Séparer l’étendue et les modalités",
            "La première question oppose État minimal et État "
            "interventionniste ; la seconde oppose règles et discrétion. "
            "Confondre les deux conduit à prêter à chaque camp des positions "
            "qu’il ne tient pas."),
           ("Partir du diagnostic, non de la doctrine",
            "Chaque camp part d’un constat sur le fonctionnement des "
            "marchés : s’ils s’auto-ajustent, l’intervention est superflue ; "
            "s’ils laissent subsister un sous-emploi durable, elle devient "
            "nécessaire. La doctrine est une conséquence, pas une prémisse."),
           ("Reconnaître ce qui est commun aux deux camps",
            "Les deux admettent un État de droit : sécurité juridique, "
            "protection de la propriété, crédibilité des règles. Le désaccord "
            "commence au-delà de ce socle, pas avant.")],
      faits=[{'f': "Le cours relève que la croissance dépend de la "
                   "crédibilité des règles, de la sécurité juridique et de la "
                   "protection de la propriété.",
              'p': "Même la position la plus favorable au marché suppose un "
                   "État : sans sécurité juridique, personne n’investit, "
                   "personne n’innove et le capital fuit."}],
      termes=['role de l etat', 'intervention publique',
              'politique economique'],
      dos=['n26-marche-etat', 'n26-liberte-intervention']),

   # --------------------------------------------- colonne 1 : le marché
   nd('minimal', 'L’État minimal', 'pilier',
      "Les prix coordonnent sans planificateur. L’information étant dispersée "
      "et subjective, aucune administration ne peut savoir ce qu’il faudrait "
      "savoir pour agir à bon escient.",
      grp=1,
      defi="L’État minimal désigne la conception selon laquelle "
           "l’intervention publique doit se limiter au cadre de l’échange, le "
           "marché assurant lui-même la coordination. Le cours en donne les "
           "éléments : la main invisible chez Smith, la supériorité du marché "
           "comme mécanisme de coordination, et la formule de la nouvelle "
           "économie classique selon laquelle la meilleure politique "
           "économique est l’absence de politique économique.",
      mec=[("La coordination par les prix",
            "Les prix transmettent l’information nécessaire à la décision : "
            "le marché ajuste l’offre et la demande sans qu’aucune instance "
            "n’ait à connaître l’ensemble des besoins."),
           ("L’impossibilité du calcul central",
            "Avec Hayek, l’information est dispersée et subjective, et aucun "
            "planificateur n’en dispose globalement : l’État ne peut donc pas "
            "savoir ce qu’il faudrait savoir pour agir à bon escient."),
           ("Le retrait au profit de règles",
            "Seules sont acceptées des règles simples, crédibles et stables "
            "dans le temps : l’État ne disparaît pas, il cesse de décider au "
            "coup par coup.")],
      aut=[{'n': "Adam Smith",
            'i': "La main invisible fait que la poursuite des intérêts "
                 "particuliers sert l’intérêt général."},
           {'n': "Friedrich Hayek",
            'i': "Le marché est un processus de découverte dans un monde "
                 "d’information dispersée."},
           {'n': "Milton Friedman",
            'i': "Il faut laisser faire le marché et laisser le chômage "
                 "revenir à son niveau naturel."}],
      faits=[{'f': "Le cours illustre le cadre institutionnel par "
                   "l’Angleterre après la Glorieuse Révolution de 1688, avec "
                   "limitation du pouvoir royal et renforcement du Parlement.",
              'p': "L’exemple montre que l’État minimal au sens budgétaire "
                   "n’est pas l’État absent : c’est la construction d’un État "
                   "de droit qui a rendu l’investissement privé possible."}],
      termes=['etat minimal', 'main invisible', 'hayek', 'laisser faire'],
      dos=['n15-etat-minimal', 'n26-liberte-intervention']),

   nd('anticipations', 'Les agents neutralisent la politique', 'pilier',
      "Si les agents anticipent correctement, la politique annoncée n’agit "
      "que sur les variables nominales : l’effet réel disparaît avant même "
      "de se produire.",
      grp=1,
      defi="L’argument des anticipations déplace la critique : la politique "
           "n’est pas seulement mal informée, elle est neutralisée par ceux "
           "qu’elle vise. Si les agents sont parfaitement rationnels, ils "
           "connaissent la règle suivie par les autorités et ajustent salaires "
           "et prix par avance : il ne reste que les variables nominales. Le "
           "cours résume la position de la nouvelle économie classique : "
           "marchés efficaces, agents parfaitement rationnels, monnaie "
           "neutre, État inutile voire nuisible.",
      mec=[("L’intégration de la règle par les agents",
            "Les agents connaissent la règle suivie par les autorités et en "
            "intègrent les effets avant qu’ils ne se produisent : la "
            "politique annoncée ne surprend personne, donc ne modifie aucune "
            "décision réelle."),
           ("La perturbation des anticipations par la discrétion",
            "Les politiques discrétionnaires créent de l’incertitude, "
            "perturbent les anticipations et accentuent l’instabilité : "
            "l’intervention devient non seulement inutile mais dangereuse."),
           ("L’action à contretemps",
            "La critique monétariste ajoute que les autorités publiques "
            "aggravent les cycles économiques au lieu de les corriger : "
            "l’action arrive trop tard et amplifie le mouvement qu’elle "
            "devait amortir.")],
      opp=[{'t': "Les quatre hypothèses — marchés efficaces, rationalité "
                 "parfaite, monnaie neutre, État inutile — tiennent ensemble "
                 "ou tombent ensemble.",
            'qui': "nouvelle économie keynésienne",
            'rep': "L’énumération montre que la conclusion sur l’État découle "
                   "d’hypothèses précises : elle tombe si l’une d’elles est "
                   "levée, ce que fait précisément la nouvelle économie "
                   "keynésienne en réintroduisant des rigidités."}],
      aut=[{'n': "Thomas Sargent",
            'i': "Une politique annoncée n’agit que sur les variables "
                 "nominales, puisque les agents en intègrent les effets par "
                 "avance."},
           {'n': "Milton Friedman",
            'i': "Il faut contrôler la croissance de la masse monétaire selon "
                 "une règle de pourcentage constant."}],
      faits=[{'f': "Le cours conclut cette position par la formule selon "
                   "laquelle la meilleure politique économique est l’absence "
                   "de politique économique.",
              'p': "La formule marque le point le plus radical du débat : "
                   "elle fait de l’abstention une politique, et non un "
                   "renoncement."}],
      termes=['anticipations rationnelles', 'monnaie neutre',
              'nouvelle economie classique'],
      dos=['n15-anticipations', 'n26-monnaie-neutre-active']),

   nd('regles', 'Des règles plutôt que de la discrétion', 'detail',
      "Le débat sur les modalités : une règle simple et crédible contre le "
      "jugement au cas par cas.",
      grp=1, par='anticipations',
      defi="L’opposition entre règles et discrétion porte sur le mode "
           "d’exercice de la politique économique et non sur son étendue. "
           "Pour la nouvelle économie classique, les politiques "
           "discrétionnaires créent de l’incertitude, perturbent les "
           "anticipations et accentuent l’instabilité, de sorte que seules "
           "sont acceptées des règles simples, crédibles et stables dans le "
           "temps. La règle de croissance constante de la masse monétaire "
           "chez Friedman en est l’exemple canonique.",
      mec=[("La crédibilité comme ressource",
            "Une règle connue et tenue rend l’action publique prévisible : "
            "les agents cessent d’anticiper des revirements, ce qui réduit "
            "l’incertitude et la prime qu’ils exigent."),
           ("Le coût de la rigidité",
            "Une règle quantitative simple ne couvre pas les situations "
            "qu’elle n’a pas prévues : c’est précisément ce que montre "
            "l’élargissement du mandat des banques centrales après 2008.")],
      opp=[{'t': "Après 2008, la banque centrale doit éviter les crises "
                 "bancaires, les paniques de liquidité, le blocage du crédit, "
                 "les faillites systémiques et les emballements spéculatifs.",
            'qui': "le cours",
            'rep': "L’énumération montre l’ampleur du mandat réel : aucune "
                   "règle quantitative simple ne couvre ces cinq risques, ce "
                   "qui réintroduit nécessairement du jugement."}],
      aut=[{'n': "John Maynard Keynes",
            'i': "L’État doit intervenir face à l’instabilité du marché, en "
                 "jugeant de la situation."}],
      termes=['regles et discretion', 'credibilite', 'banque centrale'],
      dos=['n15-regles-discretion', 'n15-politique-monetaire']),

   nd('choixpublics', 'Les défaillances de l’État', 'debat',
      "L’intervention a ses propres défauts : marché politique, groupes "
      "organisés, capture du régulateur, recherche de rente.",
      grp=1, par='minimal',
      defi="Les défaillances de l’État désignent les situations où "
           "l’intervention publique, destinée à corriger une défaillance de "
           "marché, produit elle-même des résultats inefficaces. L’école des "
           "choix publics renverse le raisonnement de Pigou en appliquant à "
           "la décision publique l’individualisme méthodologique : l’État "
           "n’est pas une entité désintéressée mais une somme d’acteurs "
           "rationnels poursuivant chacun leur utilité.",
      mec=[("Le marché politique",
            "Les électeurs sont les demandeurs, les politiciens les offreurs "
            "de politiques publiques, les promesses les biens politiques : "
            "l’analyse économique s’applique intégralement à la décision "
            "publique."),
           ("L’avantage des intérêts concentrés",
            "Les intérêts concentrés sont mieux représentés que les intérêts "
            "diffus : l’État favorise des groupes organisés au détriment de "
            "l’intérêt collectif, sans qu’aucun acteur ait agi de façon "
            "irrationnelle."),
           ("La recherche de rente",
            "Sachant que l’État distribue des aides, l’entreprise consacre "
            "des ressources à les obtenir plutôt qu’à produire : "
            "contrairement au transfert, qui change seulement de mains, ces "
            "dépenses sont une perte nette.")],
      aut=[{'n': "James Buchanan",
            'i': "L’État n’est pas un être neutre au-dessus de la société : "
                 "il est une somme d’intérêts individuels."},
           {'n': "Gordon Tullock",
            'i': "Les ressources consacrées à obtenir un avantage public sont "
                 "détournées de la production."},
           {'n': "George Stigler",
            'i': "La réglementation peut être capturée par les intérêts "
                 "privés qu’elle est censée encadrer."}],
      faits=[{'f': "Le cours relie ce tournant idéologique vers davantage de "
                   "marché à l’approfondissement de la construction "
                   "européenne, qui marginalise les politiques industrielles "
                   "verticales nationales.",
              'p': "L’argument théorique a eu une traduction "
                   "institutionnelle concrète dans l’organisation de la "
                   "politique économique européenne."}],
      termes=['defaillances de l etat', 'choix publics', 'recherche de rente'],
      dos=['n6-defaillances-etat', 'n6-rente']),

   # --------------------------------------------- colonne 2 : l’État
   nd('intervention', 'L’État interventionniste', 'pilier',
      "Les marchés ne s’auto-ajustent pas parfaitement : rigidités, "
      "asymétries, concurrence imparfaite peuvent laisser l’économie "
      "durablement en sous-emploi.",
      grp=2,
      defi="L’État interventionniste désigne l’État qui agit sur l’activité, "
           "la répartition et l’allocation des ressources plutôt que de se "
           "borner au cadre de l’échange. Le cours l’organise autour de "
           "l’État providence d’après 1945, de ses trois fonctions selon "
           "Musgrave et du carré magique de Kaldor, puis de sa crise analysée "
           "par Pierre Rosanvallon en 1981.",
      mec=[("Le constat d’une défaillance",
            "Les marchés ne s’auto-ajustent pas parfaitement : rigidités, "
            "asymétries d’information et concurrence imparfaite peuvent "
            "laisser l’économie durablement en sous-emploi."),
           ("La crise du financement",
            "Avec Rosanvallon, l’extension des missions se heurte à un "
            "problème de financement, auquel s’ajoutent une crise "
            "d’efficacité et une crise de légitimité."),
           ("La résistance fiscale",
            "Le cours relève une résistance des acteurs économiques à la "
            "hausse des impôts, et rapporte la formule de la courbe de Laffer "
            "selon laquelle trop d’impôt tue l’impôt.")],
      aut=[{'n': "John Maynard Keynes",
            'i': "Face à l’instabilité du marché, l’État doit intervenir et "
                 "peut créer une demande autonome."},
           {'n': "Pierre Rosanvallon",
            'i': "L’État providence connaît une crise à trois dimensions : "
                 "financement, efficacité et légitimité."}],
      faits=[{'f': "Pierre Rosanvallon publie La crise de l’État providence "
                   "en 1981.",
              'p': "La référence datée montre que la remise en cause est "
                   "contemporaine du tournant libéral des années quatre-"
                   "vingt, ce qui éclaire le contexte du basculement "
                   "doctrinal."},
             {'f': "Le cours relève qu’en France il existe 483 taxes et "
                   "impôts et 474 niches fiscales.",
              'p': "Les deux chiffres donnent un contenu concret à la crise "
                   "d’efficacité que Rosanvallon identifie."}],
      termes=['etat providence', 'etat interventionniste', 'rosanvallon'],
      dos=['n15-etat-interventionniste', 'n26-marche-etat']),

   nd('musgrave', 'Les trois fonctions de Musgrave', 'pilier',
      "Allocation, stabilisation, redistribution : une grille pour classer "
      "toute intervention selon le problème qu’elle traite.",
      grp=2,
      defi="Le cours énonce les trois fonctions de l’État providence selon "
           "Musgrave, dans la théorie des finances publiques de 1959 : la "
           "fonction d’allocation des ressources, la fonction de "
           "stabilisation ou de régulation, et la fonction de redistribution. "
           "Ce triptyque sert de grille générale pour classer les "
           "interventions publiques selon le problème qu’elles traitent, et "
           "non selon l’instrument qu’elles emploient.",
      mec=[("La fonction d’allocation",
            "L’État produit ou finance ce que le marché n’alloue pas "
            "correctement, en présence d’externalités ou de biens collectifs. "
            "Le cours y rattache le capital public de Barro."),
           ("La fonction de stabilisation",
            "L’État agit sur la conjoncture par le budget des administrations "
            "publiques ou par la création de monnaie, pour soutenir ou "
            "freiner la demande : relance d’un côté, rigueur de l’autre."),
           ("La fonction de redistribution",
            "Par les prestations sociales et les prélèvements obligatoires, "
            "l’État transforme les revenus primaires en revenu disponible "
            "brut : la répartition devient un objet de politique publique."),
           ("La tension entre les trois",
            "Les trois fonctions s’exercent sur le même budget : leur "
            "extension conjointe produit le problème de financement que "
            "Rosanvallon place au cœur de la crise de l’État providence.")],
      aut=[{'n': "Richard Musgrave",
            'i': "L’État providence remplit trois fonctions distinctes : "
                 "allocation, stabilisation, redistribution."}],
      faits=[{'f': "Le cours relève que la taxe sur la valeur ajoutée pèse "
                   "plus sur les revenus les plus faibles, et qu’elle n’est "
                   "donc pas un impôt juste ; l’État en tire deux cents "
                   "milliards d’euros de recettes.",
              'p': "Le rapprochement montre l’ampleur de l’arbitrage entre "
                   "rendement fiscal et justice fiscale : la fonction de "
                   "redistribution dépend du choix des assiettes."}],
      termes=['musgrave', 'redistribution', 'allocation des ressources',
              'stabilisation'],
      dos=['n15-fonctions-musgrave', 'n15-politique-budgetaire']),

   nd('relance', 'Agir sur la demande', 'detail',
      "Le budget soutient la demande, parfois sans qu’aucune décision ne soit "
      "prise : les stabilisateurs automatiques jouent seuls.",
      grp=2, par='musgrave',
      defi="Une politique de relance utilise le budget des administrations "
           "publiques ou la création de monnaie pour soutenir la demande. Le "
           "cours la définit par opposition à la politique de rigueur, qui "
           "freine la demande, et en distingue deux degrés : la réaction "
           "automatique du budget au ralentissement, et l’action volontariste "
           "par des mesures spécifiques de dépenses et de recettes.",
      mec=[("Les stabilisateurs automatiques",
            "En ralentissement, les dépenses des administrations publiques "
            "augmentent et les recettes baissent simultanément : une partie "
            "de la relance ne résulte d’aucune décision, le budget soutient "
            "la demande par sa structure même."),
           ("Le multiplicateur et son érosion par l’ouverture",
            "Le multiplicateur vaut cinq en économie fermée pour une "
            "propension à consommer de zéro virgule huit, et deux et demi en "
            "économie ouverte : l’ouverture divise par deux l’effet attendu."),
           ("Le financement par la dette",
            "Une relance se solde par un déficit public financé par émission "
            "d’obligations : son coût futur dépend des taux auxquels l’État "
            "peut emprunter.")],
      opp=[{'t': "Les politiques de relance budgétaire sont inflationnistes "
                 "et l’État aggrave les cycles au lieu de les corriger.",
            'qui': "Milton Friedman",
            'rep': "L’objection porte sur le calendrier autant que sur le "
                   "principe : elle est la raison pour laquelle les "
                   "stabilisateurs automatiques, qui n’ont pas de délai de "
                   "décision, sont moins contestés que la relance "
                   "discrétionnaire."}],
      aut=[{'n': "Paul Samuelson",
            'i': "Le multiplicateur et l’accélérateur se combinent dans "
                 "l’oscillateur en un mouvement cumulatif."},
           {'n': "Robert Barro",
            'i': "Les dépenses publiques productives améliorent la "
                 "productivité du secteur privé."}],
      faits=[{'f': "Le cours cite le plan Biden, destiné à construire et "
                   "rénover des infrastructures, routes, autoroutes et ponts.",
              'p': "L’exemple montre une relance volontariste orientée vers "
                   "le capital public : elle soutient la demande immédiate "
                   "tout en améliorant la productivité future."}],
      termes=['politique de relance', 'multiplicateur',
              'stabilisateurs automatiques'],
      dos=['n15-politique-relance', 'n15-multiplicateur-budgetaire',
           'n15-stabilisateurs-automatiques']),

   nd('capitalpublic', 'Le capital public et son niveau optimal', 'detail',
      "Dépenses trop faibles : sous-investissement collectif. Dépenses "
      "excessives : éviction du capital privé. Il existe un optimum.",
      grp=2, par='musgrave',
      defi="Le capital public est l’ensemble des dépenses publiques "
           "productives qui améliorent la productivité du secteur privé : "
           "infrastructures, ponts, routes et transports, éducation, "
           "financement de la recherche et du développement. Le modèle de "
           "Barro en tire une condition d’efficacité à double borne, qui est "
           "l’argument le plus précis en faveur d’un État ni absent ni "
           "illimité.",
      mec=[("La borne inférieure",
            "Des dépenses trop faibles produisent un sous-investissement "
            "collectif : les infrastructures, l’éducation et la recherche "
            "manquent, et la productivité privée en pâtit."),
           ("La borne supérieure",
            "Des dépenses excessives évincent le capital privé : "
            "l’intervention publique déplace l’activité privée au lieu de "
            "l’ajouter. Il existe donc un niveau optimal de capital public."),
           ("Le critère de qualité",
            "Ce sont des dépenses dont le rendement passe par la productivité "
            "privée : le critère n’est pas le montant mais la nature de la "
            "dépense.")],
      args=[{'a': "La condition de Barro transforme le débat doctrinal en "
                  "question de niveau : elle admet l’argument des deux camps "
                  "tout en leur assignant chacun une borne.",
             'lim': "Le niveau optimal n’est pas observable directement, ce "
                    "qui laisse le désaccord entier sur le point de savoir de "
                    "quel côté de l’optimum se trouve une économie donnée."}],
      aut=[{'n': "Robert Barro",
            'i': "Au-delà d’un niveau optimal, les dépenses publiques "
                 "évincent le capital privé."}],
      termes=['capital public', 'effet d eviction', 'barro',
              'depenses publiques'],
      dos=['n15-effet-eviction', 'n1-endogene']),

   # --------------------------------------------- bas : les contraintes
   nd('carre', 'Le carré magique : tout est arbitrage', 'sortie',
      "Croissance, emploi, prix, solde extérieur : les quatre objectifs ne "
      "peuvent pas être atteints simultanément. Aucune politique ne les "
      "satisfait tous.",
      grp=3,
      defi="Le carré magique de Kaldor réunit les quatre objectifs de la "
           "politique économique : la croissance, l’emploi, la stabilité des "
           "prix et l’équilibre du solde extérieur. Le cours relève qu’il est "
           "dit magique parce que l’atteinte simultanée des quatre objectifs "
           "est impossible. La conséquence est forte : l’intervention est "
           "structurellement un arbitrage, et le désaccord entre les camps "
           "porte souvent moins sur les moyens que sur l’objectif privilégié.",
      mec=[("L’incompatibilité des objectifs",
            "Soutenir l’emploi par la demande tend à dégrader le solde "
            "extérieur et à nourrir l’inflation ; stabiliser les prix par la "
            "contrainte monétaire pèse sur l’emploi. Chaque objectif se paie "
            "sur un autre."),
           ("Le classement implicite des priorités",
            "Choisir une politique, c’est hiérarchiser les quatre objectifs. "
            "Les doctrines se distinguent souvent par cette hiérarchie plus "
            "que par leur analyse des mécanismes.")],
      aut=[{'n': "Nicholas Kaldor",
            'i': "Les quatre objectifs du carré magique ne peuvent pas être "
                 "atteints simultanément."}],
      faits=[{'f': "Le cours distingue politiques conjoncturelles de court "
                   "terme et politiques structurelles de long terme, la "
                   "politique fiscale figurant dans les deux.",
              'p': "La typologie montre que les fonctions se distinguent par "
                   "leur horizon et non par leurs instruments, un même levier "
                   "pouvant servir plusieurs fins."}],
      termes=['carre magique', 'kaldor', 'objectifs de politique economique'],
      dos=['n15-politique-budgetaire', 'n26-efficacite-justice']),

   nd('mix', 'Policy mix et contrainte extérieure', 'limite',
      "Articuler budget et monnaie ne suffit pas : en économie ouverte, le "
      "triangle de Mundell interdit de tout vouloir à la fois.",
      grp=3,
      defi="Le cours définit le policy mix en une phrase : s’il y a une "
           "articulation de la politique budgétaire et de la politique "
           "monétaire, on parle de policy mix. Ce n’est pas un troisième "
           "instrument mais la manière de coordonner les deux premiers. En "
           "économie ouverte, cette coordination se heurte à une contrainte "
           "supplémentaire : on ne peut pas avoir simultanément libre "
           "circulation des capitaux, politique monétaire autonome et change "
           "stable.",
      mec=[("La cohérence ou l’amplification",
            "Les deux instruments peuvent se compenser ou s’additionner. Le "
            "cours définit l’austérité comme la situation où l’État réduit "
            "les dépenses et où les taux d’intérêt augmentent : les deux y "
            "agissent dans le même sens, ce qui amplifie la contraction."),
           ("La limite de la fusion",
            "Coordonner deux instruments est admis ; les fusionner remet en "
            "cause l’indépendance de la banque centrale. Le cours range la "
            "confusion entre politique monétaire et politique budgétaire "
            "parmi les fortes limites de l’hélicoptère monétaire."),
           ("La contrainte extérieure",
            "L’ouverture divise par deux le multiplicateur et soumet la "
            "politique monétaire au triangle d’incompatibilité : une partie "
            "de la souveraineté économique est perdue avant tout arbitrage "
            "interne.")],
      aut=[{'n': "Robert Mundell",
            'i': "On ne peut pas avoir simultanément libre circulation des "
                 "capitaux, politique monétaire autonome et change stable."}],
      termes=['policy mix', 'contrainte exterieure', 'triangle d incompatibilite'],
      dos=['n15-policy-mix', 'n15-contrainte-exterieure']),
  ],
  [
   ln('question', 'minimal', 'si les marchés s’ajustent',
      "Répondre que les marchés s’auto-ajustent conduit à limiter l’État au "
      "cadre de l’échange : il n’y a rien à corriger, et toute action "
      "ajoutée ne peut que perturber un ajustement déjà en cours.",
      'conditionne'),
   ln('question', 'intervention', 'si les marchés défaillent',
      "Répondre que rigidités, asymétries et concurrence imparfaite peuvent "
      "laisser l’économie durablement en sous-emploi conduit à l’État "
      "interventionniste : l’ajustement spontané ne se produit pas, ou pas "
      "assez vite.", 'conditionne'),
   ln('minimal', 'anticipations', 'se renforce de',
      "L’argument hayékien porte sur l’information dont dispose l’État ; "
      "celui des anticipations porte sur la réaction des agents. Les deux "
      "sont indépendants et se cumulent : même bien informée, la politique "
      "serait neutralisée.", 'renforce'),
   ln('anticipations', 'regles', 'conduit à préférer',
      "Si la discrétion perturbe les anticipations, la conclusion pratique "
      "est de s’en tenir à des règles simples, crédibles et stables : la "
      "critique théorique débouche sur une recommandation institutionnelle "
      "précise.", 'cause'),
   ln('minimal', 'choixpublics', 's’achève en',
      "L’argument commence par l’incapacité de l’État à savoir et s’achève "
      "par son absence de neutralité : l’école des choix publics applique à "
      "la décision publique l’individualisme méthodologique employé en "
      "microéconomie.", 'cause'),
   ln('intervention', 'musgrave', 's’organise en',
      "L’intervention n’est pas une improvisation : Musgrave la structure en "
      "trois fonctions distinctes, ce qui permet de rattacher chaque mesure "
      "au problème qu’elle traite plutôt qu’à l’instrument qu’elle emploie.",
      'cause'),
   ln('musgrave', 'relance', 'se déploie par',
      "La fonction de stabilisation se traduit concrètement par l’action sur "
      "la demande : stabilisateurs automatiques d’abord, mesures "
      "volontaristes ensuite, selon l’ampleur du ralentissement.", 'cause'),
   ln('musgrave', 'capitalpublic', 'prend corps dans',
      "La fonction d’allocation se traduit par le financement de ce que le "
      "marché n’alloue pas correctement : infrastructures, éducation, "
      "recherche. Barro en fait un facteur de productivité privée et non une "
      "simple dépense.", 'cause'),
   ln('choixpublics', 'relance', 'conteste l’efficacité de',
      "Le marché politique explique que la relance soit décidée au mauvais "
      "moment : la réélection commande le calendrier plus que la conjoncture, "
      "ce qui transforme l’outil de stabilisation en facteur d’instabilité.",
      'oppose'),
   ln('capitalpublic', 'choixpublics', 'borne la critique',
      "L’effet d’éviction n’est pas un argument contre la dépense publique "
      "mais une limite supérieure à son niveau : la condition de Barro admet "
      "une part de la critique libérale sans conclure à l’abstention.",
      'limite'),
   ln('regles', 'carre', 'bute sur la pluralité des objectifs',
      "Une règle quantitative simple suppose un objectif unique. Le carré "
      "magique en pose quatre, incompatibles : toute règle fixe donc "
      "implicitement une hiérarchie que personne n’a explicitement choisie.",
      'limite'),
   ln('musgrave', 'carre', 'se heurte à',
      "Les trois fonctions s’exercent sur le même budget et poursuivent des "
      "objectifs qui ne peuvent être atteints simultanément : l’extension "
      "conjointe des missions produit le problème de financement que "
      "Rosanvallon place au cœur de la crise.", 'limite'),
   ln('relance', 'mix', 'perd de sa force en économie ouverte',
      "Le multiplicateur passe de cinq à deux et demi lorsque l’économie "
      "s’ouvre : une part de la relance fuit en importations. L’arbitrage "
      "interne se double alors d’une contrainte extérieure.", 'limite'),
   ln('mix', 'carre', 'ajoute une contrainte',
      "Le triangle d’incompatibilité retire un degré de liberté : avec des "
      "capitaux libres et un change fixe, la politique monétaire cesse d’être "
      "autonome. Le carré magique devient alors encore plus difficile à "
      "satisfaire.", 'renforce'),
   ln('carre', 'question', 'ramène au choix politique',
      "Puisque aucune politique ne satisfait les quatre objectifs, le "
      "désaccord entre les deux camps porte moins sur les mécanismes que sur "
      "la hiérarchie des objectifs. La question initiale est donc, pour "
      "partie, un choix de priorités.", 'renforce'),
  ],
  bandes=[(1, 'Les raisons de s’en remettre au marché'),
          (2, 'Les raisons d’intervenir'),
          (3, 'Les contraintes communes')],
  fam='Marché, État et théories')
