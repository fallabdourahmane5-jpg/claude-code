# -*- coding: utf-8 -*-
"""Chapitre 5 — Analyse microéconomique (II) : les défaillances du marché."""

SP = {
 'c5-01': 'Défaillances du marché et monopoles : naturel, innovation, réseau',
 'c5-02': 'Biens collectifs, biens communs et passager clandestin',
 'c5-03': 'Externalités, taxe pigouvienne et tragédie des communs',
 'c5-04': 'Asymétries d’information : Akerlof, sélection adverse et aléa moral',
 'c5-05': 'Perte sèche, défaillances de l’État et choix publics',
 'c5-06': 'Pigou contre Coase : la taxe ou la négociation',
 'c5-07': 'Ostrom, communs gouvernés et tragédie des anti-communs',
}

DROP = []


def f(**kw):
    return kw


FIX = {
'ch5-qcm-1': f(niv='connaitre', sp='c5-01',
 exp="Une défaillance de marché est une situation où le marché "
     "concurrentiel, laissé à lui-même, n’aboutit pas à une allocation "
     "optimale des ressources. Le chapitre en étudie quatre : monopole "
     "naturel, biens collectifs et communs, externalités, asymétries "
     "d’information.",
 why=["La fixation des prix par l’État est une réponse possible à une "
      "défaillance, non la défaillance elle-même.",
      "Une hausse de prix peut être le signal d’une rareté : elle n’est pas "
      "en soi une défaillance.",
      "Le chômage structurel est un phénomène macroéconomique."]),
'ch5-qcm-4': f(niv='connaitre', sp='c5-01',
 exp="L’efficacité allocative exige que le prix égale le coût marginal : le "
     "prix mesure ce que l’unité supplémentaire vaut pour le consommateur, "
     "le coût marginal ce qu’elle coûte à la société. Tant qu’ils diffèrent, "
     "produire une unité de plus ou de moins améliorerait le bien-être.",
 why=["Égaliser prix et coût total n’a pas de sens dimensionnel.",
      "Recette marginale égale coût moyen ne correspond à aucune condition "
      "d’optimum.",
      "Un profit nul est une conséquence du long terme en concurrence, pas "
      "la condition d’efficacité."]),
'ch5-qcm-5': f(niv='comprendre', sp='c5-01',
 exp="Le monopoleur fixe sa quantité là où la recette marginale égale le "
     "coût marginal, puis lit le prix sur la courbe de demande : ce prix est "
     "supérieur au coût marginal. L’écart mesure son pouvoir de marché et "
     "engendre la perte sèche.",
 why=["P = Cm est la situation de concurrence pure et parfaite.",
      "P < Cm signifierait vendre à perte sur chaque unité.",
      "Un prix nul n’a pas de sens pour un monopoleur maximisant son "
      "profit."]),
'ch5-qcm-7': f(niv='connaitre', sp='c5-01',
 exp="Le monopole naturel naît de coûts fixes très élevés et de rendements "
     "croissants : le coût moyen décroît avec la quantité, si bien qu’une "
     "seule firme produit à moindre coût que plusieurs. La structure du "
     "marché n’est pas le produit d’une stratégie mais de la technologie.",
 why=["Un monopole créé par la loi est un monopole d’institution.",
      "Un monopole issu d’un brevet est un monopole d’innovation, "
      "temporaire.",
      "L’exploitation publique de ressources naturelles est un autre cas de "
      "figure."]),
'ch5-qcm-8': f(niv='raisonner', sp='c5-01',
 exp="La contradiction est insoluble par le marché : si l’on impose P = Cm, "
     "l’entreprise ne couvre pas ses coûts fixes et fait des pertes ; si on "
     "la laisse fixer son prix, elle facture bien au-dessus du coût "
     "marginal et sous-produit. Aucune des deux issues n’est optimale, d’où "
     "la nécessité d’une régulation, d’une subvention ou d’une "
     "nationalisation.",
 why=["Le monopole produit trop peu et trop cher, non l’inverse.",
      "L’effet sur l’innovation est discuté, mais ce n’est pas la raison de "
      "la défaillance.",
      "La dépendance aux subventions est une conséquence possible, pas la "
      "cause."],
 diss="Exemple idéal pour montrer qu’une défaillance appelle une "
      "intervention sans dire laquelle : les trois solutions possibles "
      "— régulation, subvention, propriété publique — ont des coûts "
      "différents."),
'ch5-qcm-9': f(niv='connaitre', sp='c5-01',
 exp="Le cours cite l’eau et les réseaux ferroviaires : dans les deux cas, "
     "l’infrastructure représente un coût fixe considérable qu’il serait "
     "absurde de dupliquer. Le réseau est le monopole naturel ; les services "
     "qui l’empruntent peuvent, eux, être ouverts à la concurrence.",
 why=["Automobile et chimie sont des industries concurrentielles.",
      "Agriculture et tourisme sont des secteurs très atomisés.",
      "Banque et assurance sont concentrées mais non monopolistiques."]),
'ch5-qcm-10': f(niv='connaitre', sp='c5-01',
 exp="Le monopole d’innovation est un monopole temporaire, accordé par un "
     "brevet pour une durée pouvant atteindre vingt ans. Il est "
     "délibérément créé : sans protection, l’innovateur ne pourrait pas "
     "s’approprier les fruits de sa recherche et investirait moins.",
 why=["Le brevet est temporaire par construction : un monopole à vie serait "
      "sans justification.",
      "La domination technologique spontanée relève d’un autre mécanisme.",
      "Le brevet n’est pas réservé aux grandes entreprises."]),
'ch5-qcm-11': f(niv='connaitre', sp='c5-01',
 exp="Schumpeter justifie le monopole temporaire : la rente d’innovation est "
     "la récompense qui finance la recherche et incite à innover. C’est "
     "l’argument central de la politique des brevets, et la raison pour "
     "laquelle le droit de la concurrence tolère cette exception.",
 why=["Pigou travaille sur les externalités et l’économie du bien-être.",
      "Marshall analyse l’équilibre partiel.",
      "Walras construit l’équilibre général."]),
'ch5-qcm-21': f(niv='connaitre', sp='c5-01',
 exp="En concurrence pure et parfaite, chaque firme est preneuse de prix et "
     "produit jusqu’à égaliser son coût marginal au prix : P = Cm. Cette "
     "égalité est la condition d’une allocation optimale, puisque la valeur "
     "de la dernière unité pour le consommateur égale son coût pour la "
     "société.",
 why=["P > Cm caractérise le monopole.",
      "Un prix administré n’est pas un prix de concurrence.",
      "Rm > Cm signifierait qu’il reste du profit à prendre en produisant "
      "davantage."]),
'ch5-qcm-23': f(niv='comprendre', sp='c5-01',
 exp="Un monopole d’effet de réseau naît de ce que l’utilité du service "
     "croît avec le nombre d’utilisateurs : plus il y a d’abonnés, plus le "
     "service vaut, donc plus il attire. Le marché bascule vers un acteur "
     "dominant sans qu’aucun coût fixe ne l’impose.",
 why=["Un brevet sur une technologie de réseau donnerait un monopole "
      "d’innovation.",
      "Un monopole public de transport est un monopole d’institution.",
      "Le caractère temporaire et le brevet caractérisent l’innovation, non "
      "l’effet de réseau."],
 diss="Ces monopoles posent un problème inédit au droit de la concurrence : "
      "la position dominante y est le résultat du choix des utilisateurs, "
      "non d’une pratique abusive."),
'ch5-qcm-25': f(niv='comprendre', sp='c5-01',
 exp="Trois réponses sont possibles face au monopole naturel : la propriété "
     "publique, la régulation du prix par une autorité, ou une subvention "
     "permettant de tarifer au coût marginal tout en couvrant les coûts "
     "fixes. Chacune a un coût : budgétaire, informationnel ou "
     "d’efficacité.",
 why=["La privatisation ne supprime pas la structure de coûts qui crée le "
      "monopole.",
      "Interdire l’entreprise supprimerait le service lui-même.",
      "Les droits de douane sont sans rapport avec un marché de réseau "
      "domestique."]),
'ch5-qcm-26': f(niv='raisonner', sp='c5-01',
 exp="Le brevet est un arbitrage entre deux objectifs contradictoires : il "
     "stimule l’innovation en garantissant une rente, mais il restreint "
     "l’accès au produit pendant vingt ans. Le cas des médicaments le rend "
     "visible : la protection finance la recherche, mais retarde l’accès aux "
     "traitements pour les patients les moins solvables.",
 why=["Le brevet ne réduit pas les coûts de recherche : il en permet le "
      "recouvrement.",
      "Il freine la diffusion plutôt qu’il ne la favorise, le temps de la "
      "protection.",
      "Il protège l’innovateur, non le consommateur."],
 diss="Arbitrage à citer dans tout sujet sur l’innovation : l’incitation à "
      "produire du savoir et l’efficacité de sa diffusion sont en tension, "
      "et la durée du brevet est la variable d’ajustement."),
'ch5-qcm-27': f(niv='connaitre', sp='c5-01',
 exp="L’économie du bien-être, dont Pigou est la figure, évalue si les "
     "allocations issues du marché maximisent l’utilité collective. C’est "
     "elle qui fournit le critère permettant de dire qu’un marché a "
     "« échoué » et de justifier, le cas échéant, une intervention.",
 why=["Les politiques de redistribution en sont une application, non la "
      "définition.",
      "L’étude des ménages pauvres est un champ empirique distinct.",
      "L’État providence est une construction institutionnelle, non une "
      "branche théorique."]),
'ch5-qcm-29': f(niv='comprendre', sp='c5-01',
 exp="En concurrence pure et parfaite, la firme est price taker : elle peut "
     "vendre toute sa production au prix du marché mais rien du tout "
     "au-dessus. La demande qui lui est adressée est donc horizontale, "
     "d’élasticité infinie — alors que la demande du marché, elle, reste "
     "décroissante.",
 why=["« Décroissante et d’élasticité infinie » est contradictoire.",
      "Une demande verticale décrirait une rigidité totale des quantités.",
      "La dépendance au revenu caractérise la demande de marché, pas la "
      "demande adressée à une firme concurrentielle."]),
'ch5-qcm-30': f(niv='connaitre', sp='c5-01',
 exp="Le price maker fixe son prix : n’ayant pas de concurrent, le "
     "monopoleur choisit le couple prix-quantité qui maximise son profit "
     "sur la courbe de demande. Son pouvoir n’est pas sans limite — la "
     "demande décroît — mais il choisit son point.",
 why=["Accepter le prix du marché, c’est être price taker, en concurrence.",
      "Un prix réglementé est imposé par l’autorité, non choisi.",
      "S’aligner sur les concurrents suppose qu’il en existe."]),
'ch5-qcm-31': f(niv='comprendre', sp='c5-01',
 exp="Comme toute entreprise, le monopoleur maximise son profit en égalisant "
     "recette marginale et coût marginal. La différence avec la concurrence "
     "est que sa recette marginale est inférieure au prix — vendre une unité "
     "de plus oblige à baisser le prix sur toutes les unités — si bien que "
     "le prix final dépasse le coût marginal.",
 why=["P = Cm est la règle en concurrence, pas la condition de "
      "maximisation.",
      "P = coût moyen correspond à un profit nul.",
      "Une recette marginale nulle correspond au maximum du chiffre "
      "d’affaires, pas du profit."]),
'ch5-qcm-35': f(niv='comprendre', sp='c5-05',
 exp="La théorie des choix publics souligne que le monopole public n’échappe "
     "pas aux défaillances : absence de pression concurrentielle, logique "
     "bureaucratique, poursuite d’objectifs propres aux administrations et "
     "aux élus. Corriger une défaillance de marché peut donc créer une "
     "défaillance de l’État.",
 why=["Le monopole public ne se caractérise pas par une surproduction à bas "
      "prix.",
      "Le financement est une contrainte, non la limite théorique "
      "identifiée.",
      "L’exposition à la concurrence internationale n’est pas le reproche "
      "adressé."]),
'ch5-qcm-38': f(niv='connaitre', sp='c5-01',
 exp="La Française des jeux illustre le monopole d’institution : l’État "
     "réserve l’activité de jeux d’argent à un opérateur, pour des raisons "
     "d’ordre public et de recettes fiscales. La structure du marché "
     "résulte d’une décision politique, non de la technologie.",
 why=["Les transports relèvent plutôt du monopole naturel de réseau.",
      "L’énergie mêle réseau régulé et production concurrentielle.",
      "Une institution financière publique n’est pas un monopole de jeu."]),
'ch5-vf-2': f(niv='raisonner', sp='c5-01',
 exp="Le monopole naturel est structurellement une défaillance : le marché "
     "ne peut pas concilier la tarification au coût marginal, nécessaire à "
     "l’efficacité, et la couverture de coûts fixes élevés, nécessaire à la "
     "survie de l’entreprise. Le constat ne préjuge pas de la solution à "
     "retenir."),
'ch5-vf-3': f(niv='connaitre', sp='c5-01',
 exp="La durée maximale de protection par brevet est de vingt ans. "
     "C’est la contrepartie temporelle de la rente : au-delà, l’innovation "
     "tombe dans le domaine public et la diffusion prime sur l’incitation."),
'ch5-vf-8': f(niv='connaitre', sp='c5-01',
 exp="C’est l’argument schumpétérien : la perspective d’une rente "
     "temporaire finance et motive la recherche. Le monopole d’innovation "
     "n’est donc pas une anomalie tolérée, mais un instrument de politique "
     "de l’innovation."),
'ch5-vf-10': f(niv='comprendre', sp='c5-01',
 exp="C’est la double caractéristique du monopole : en égalisant recette "
     "marginale et coût marginal, il restreint la quantité par rapport à "
     "l’optimum social et vend au-dessus du coût marginal. L’écart entre le "
     "surplus perdu et le profit gagné est la perte sèche."),
'ch5-vf-11': f(niv='appliquer', sp='c5-01',
 exp="Les réseaux sociaux illustrent l’effet de réseau : l’intérêt de la "
     "plateforme croît avec le nombre d’utilisateurs présents, ce qui rend "
     "l’entrée d’un concurrent très difficile même sans coût fixe "
     "considérable. La position dominante s’auto-entretient."),
'ch5-vf-14': f(niv='connaitre', sp='c5-01',
 exp="Le réseau ferroviaire est l’exemple canonique du monopole naturel : "
     "dupliquer les voies serait absurde économiquement. Le cours cite "
     "l’eau et le rail, où l’infrastructure impose l’unicité du producteur "
     "tandis que les services peuvent être ouverts."),
'ch5-vf-15': f(niv='raisonner', sp='c5-01',
 exp="L’affirmation est trop absolue. Le monopole d’institution peut "
     "souffrir de bureaucratie et d’un déficit d’innovation, mais il "
     "garantit aussi la continuité du service, la péréquation tarifaire et "
     "des objectifs d’intérêt général qu’un opérateur privé n’a aucune "
     "raison de poursuivre."),
'ch5-open-6': f(niv='comprendre', sp='c5-03',
 ans={'modele': "La tragédie des communs, formulée par Garrett Hardin, "
      "décrit la surexploitation d’une ressource commune — rivale mais non "
      "excluable. Chaque usager a intérêt à prélever davantage, puisqu’il "
      "en retire tout le bénéfice tandis que le coût de la raréfaction est "
      "partagé par tous. La somme de comportements rationnels détruit la "
      "ressource.",
      'cles': [{'f': ['commune', 'commun', 'ressource'], 'l': 'la ressource est commune'},
               {'f': ['surexploit', 'epuis', 'destruction'],
                'l': 'elle est surexploitée'},
               {'f': ['interet', 'rationnel', 'individuel'],
                'l': 'chacun agit rationnellement de son point de vue'},
               {'f': ['partage', 'collectif', 'tous'],
                'l': 'le coût est supporté par tous'}]},
 exp="Le cours nuance aussitôt la thèse avec Elinor Ostrom : des "
     "communautés organisées parviennent à gérer durablement des communs "
     "sans privatisation ni étatisation."),
'ch5-qcm-12': f(niv='connaitre', sp='c5-02',
 exp="Les biens se classent selon deux critères croisés : la rivalité — ma "
     "consommation réduit-elle celle des autres ? — et l’excluabilité — "
     "peut-on empêcher de consommer celui qui ne paie pas ? Le croisement "
     "donne quatre catégories.",
 why=["Qualité et prix sont des caractéristiques commerciales.",
      "Public et privé sont deux des quatre résultats, non les critères.",
      "Matériel et immatériel ne fondent pas cette typologie."]),
'ch5-qcm-13': f(niv='connaitre', sp='c5-02',
 exp="Un bien public au sens économique est non rival et non excluable : "
     "l’éclairage public, la défense nationale, un phare. Cette définition "
     "n’a rien à voir avec le statut du producteur : un bien produit par "
     "l’État peut être parfaitement privé au sens économique.",
 why=["Un bien produit par l’État peut être rival et excluable — une place "
      "de train, par exemple.",
      "La subvention modifie le prix, non les propriétés du bien.",
      "Un accès payant suppose précisément l’excluabilité."]),
'ch5-qcm-14': f(niv='connaitre', sp='c5-02',
 exp="Le passager clandestin bénéficie d’un bien collectif sans contribuer à "
     "son financement : comme on ne peut pas l’exclure, il a intérêt à "
     "laisser les autres payer. Si tous raisonnent ainsi, le bien n’est pas "
     "financé — d’où le recours à l’impôt.",
 why=["La copie d’innovations relève de l’imitation et des brevets.",
      "Le défaut souverain est une question de finances publiques.",
      "L’abstention syndicale est une illustration sociologique, pas la "
      "définition économique."]),
'ch5-qcm-24': f(niv='connaitre', sp='c5-02',
 exp="La défense nationale et la sécurité publique sont les exemples "
     "canoniques de biens collectifs non individualisables : on ne peut ni "
     "mesurer la part consommée par chacun, ni exclure quiconque de la "
     "protection fournie.",
 why=["Les remboursements de sécurité sociale sont individualisables.",
      "Les allocations familiales sont versées à des bénéficiaires "
      "identifiés.",
      "L’enseignement est excluable et partiellement rival : c’est un bien "
      "tutélaire, non un bien collectif pur."]),
'ch5-qcm-34': f(niv='connaitre', sp='c5-02',
 exp="Le croisement rivalité × excluabilité donne quatre cases : bien privé "
     "(rival, excluable), bien de club (non rival, excluable), bien commun "
     "(rival, non excluable) et bien public pur (non rival, non excluable). "
     "C’est cette grille qui permet d’identifier la défaillance en cause.",
 why=["Marchand et non marchand est une distinction de comptabilité "
      "nationale.",
      "Durables et périssables classent les biens selon leur usage.",
      "Supérieurs et inférieurs renvoient à l’élasticité-revenu."]),
'ch5-qcm-37': f(niv='comprendre', sp='c5-02',
 exp="Pigou est libéral : il tient le marché pour efficace en règle "
     "générale et ne justifie l’intervention que là où une défaillance "
     "empêche d’atteindre l’optimum collectif. L’intervention est donc "
     "ciblée et argumentée, non systématique.",
 why=["Une intervention systématique supposerait une défaillance "
      "généralisée, ce que Pigou ne soutient pas.",
      "Refuser toute intervention serait la position que Pigou combat.",
      "Son analyse ne se limite pas aux biens publics purs : les "
      "externalités en sont le cœur."]),
'ch5-vf-6': f(niv='connaitre', sp='c5-02',
 exp="Un bien public est non rival et non excluable : ma consommation ne "
     "réduit pas celle des autres, et l’on ne peut écarter celui qui ne "
     "paie pas. Rival et excluable définit au contraire le bien privé."),
'ch5-vf-7': f(niv='connaitre', sp='c5-02',
 exp="C’est l’inverse : le passager clandestin bénéficie du bien sans payer. "
     "Le problème qu’il pose est le sous-financement des biens collectifs, "
     "puisque chacun a intérêt à attendre que les autres contribuent."),
'ch5-vf-18': f(niv='connaitre', sp='c5-02',
 exp="Le bien de club est excluable — l’abonnement conditionne l’accès — et "
     "non rival tant que la congestion ne s’installe pas : une chaîne "
     "payante, un péage autoroutier fluide. La congestion le rapproche du "
     "bien commun."),
'ch5-open-3': f(niv='connaitre', sp='c5-02',
 ans={'modele': "Samuelson définit le bien collectif par deux critères : la "
      "non-rivalité — la consommation d’une personne n’empêche pas celle "
      "des autres — et la non-excluabilité — on ne peut pas écarter celui "
      "qui ne paie pas. Il en résulte que le marché ne peut pas le financer "
      "correctement, le comportement de passager clandestin étant rationnel.",
      'cles': [{'f': ['non rival', 'rivalite', 'rivalité'],
                'l': 'la non-rivalité'},
               {'f': ['non excluab', 'excluabilite', 'empecher'],
                'l': 'la non-excluabilité'},
               {'f': ['marche', 'finance', 'clandestin'],
                'l': 'le marché ne peut pas le financer seul'}]},
 exp="Les deux critères n’ont pas le même statut : la non-rivalité dit qu’il "
     "serait inefficace d’exclure, la non-excluabilité qu’on ne le peut "
     "pas."),
'ch5-open-4': f(niv='connaitre', sp='c5-02',
 ans={'modele': "Le passager clandestin profite d’un bien collectif — "
      "éclairage public, défense nationale — sans participer à son "
      "financement, en comptant sur la contribution des autres. Comme on ne "
      "peut pas l’exclure, son comportement est individuellement rationnel ; "
      "généralisé, il empêche le financement du bien, ce qui justifie "
      "l’impôt.",
      'cles': [{'f': ['sans payer', 'sans contribuer', 'sans participer'],
                'l': 'il bénéficie sans payer'},
               {'f': ['collectif', 'public'], 'l': 'd’un bien collectif'},
               {'f': ['impot', 'impôt', 'etat', 'financement'],
                'l': 'd’où le recours à un financement obligatoire'}]},
 exp="Le raisonnement vaut au-delà des biens publics : il explique aussi les "
     "difficultés de l’action collective, de la cotisation syndicale aux "
     "accords climatiques."),
'ch5-open-5': f(niv='comprendre', sp='c5-02',
 ans={'modele': "Les deux sont non excluables, mais le bien collectif est "
      "non rival — un phare éclaire tous les navires sans s’user — tandis "
      "que le bien commun est rival : chaque poisson pêché, chaque hectare "
      "de pâturage brouté réduit ce qui reste pour les autres. C’est cette "
      "rivalité qui engendre le risque de surexploitation.",
      'cles': [{'f': ['non excluab', 'excluabilite'],
                'l': 'les deux sont non excluables'},
               {'f': ['non rival', 'phare'],
                'l': 'le bien collectif est non rival'},
               {'f': ['rival', 'poisson', 'paturage', 'epuis'],
                'l': 'le bien commun est rival et épuisable'}]},
 exp="La distinction commande la réponse : pour le bien collectif, le "
     "problème est le financement ; pour le bien commun, c’est la "
     "régulation des prélèvements."),
}

FIX.update({
# ============================ c5-03 · externalités et communs
'ch5-qcm-6': f(niv='comprendre', sp='c5-03',
 exp="La perte sèche, ou triangle d’Harberger, mesure le bien-être perdu "
     "par la collectivité du fait du monopole : des échanges mutuellement "
     "avantageux — ceux dont la valeur pour le consommateur dépasse le coût "
     "marginal — n’ont pas lieu parce que le prix est trop élevé. Ce n’est "
     "pas un transfert vers le monopoleur, c’est une perte nette.",
 why=["La perte de revenu du monopoleur face à la concurrence n’est pas une "
      "perte collective.",
      "Les subventions sont une dépense publique, pas la perte sèche.",
      "Le surplus du producteur augmente au contraire avec le pouvoir de "
      "marché."],
 diss="La distinction transfert / perte nette est décisive : le monopole "
      "redistribue du consommateur vers le producteur, mais il détruit "
      "aussi de la valeur, et c’est ce second effet qui le condamne du "
      "point de vue du bien-être."),
'ch5-qcm-15': f(niv='connaitre', sp='c5-03',
 exp="Une externalité négative est un coût supporté par un tiers étranger à "
     "la transaction et non intégré dans le prix. Le coût privé est alors "
     "inférieur au coût social, et le marché surproduit le bien concerné.",
 why=["La baisse de profit due à la concurrence est un effet de marché "
      "normal, intégré aux prix.",
      "La baisse du surplus du consommateur est un effet prix, non une "
      "externalité.",
      "Une taxe est un instrument de correction, pas l’externalité "
      "elle-même."]),
'ch5-qcm-16': f(niv='comprendre', sp='c5-03',
 exp="La taxe pigouvienne internalise le coût externe : fixée au niveau du "
     "dommage marginal, elle élève le coût privé jusqu’au coût social, si "
     "bien que le producteur intègre spontanément la pollution dans son "
     "calcul et réduit sa production jusqu’à l’optimum.",
 why=["Supprimer le marché n’est pas une internalisation mais une "
      "interdiction.",
      "Indemniser les victimes répare le dommage sans modifier "
      "l’incitation.",
      "Un plafond de production est une réglementation quantitative, autre "
      "instrument."],
 diss="Opposer la taxe pigouvienne, qui fixe un prix, au quota échangeable, "
      "qui fixe une quantité, permet de discuter précisément des "
      "instruments de politique environnementale."),
'ch5-qcm-20': f(niv='connaitre', sp='c5-03',
 exp="Le bien commun est rival et non excluable : accessible à tous, mais "
     "épuisable. Bancs de poissons, nappes phréatiques, pâturages. Cette "
     "combinaison est la plus dangereuse, puisque personne ne peut être "
     "écarté alors que chacun réduit ce qui reste.",
 why=["Non rival et excluable définit le bien de club.",
      "Le producteur, public ou privé, n’entre pas dans la définition.",
      "Non rival et non excluable définit le bien public pur."]),
'ch5-qcm-28': f(niv='appliquer', sp='c5-03',
 exp="La vaccination et la formation sont les exemples canoniques "
     "d’externalités positives : le vacciné protège aussi son entourage, le "
     "salarié formé élève la productivité au-delà de son poste. Le bénéfice "
     "social excède le bénéfice privé, et le marché sous-produit.",
 why=["La pollution industrielle est l’exemple type d’externalité négative.",
      "La congestion routière est également une externalité négative.",
      "Le tabagisme passif est un coût imposé à des tiers."]),
'ch5-qcm-32': f(niv='connaitre', sp='c5-03',
 exp="La tragédie des communs désigne la surexploitation d’une ressource "
     "commune par des individus rationnels : chacun capte tout le bénéfice "
     "de son prélèvement mais ne supporte qu’une fraction du coût de "
     "l’épuisement. L’addition de comportements rationnels produit un "
     "résultat collectivement désastreux.",
 why=["La destruction par l’État n’est pas le mécanisme décrit.",
      "L’incapacité de l’État est une autre question, celle des défaillances "
      "publiques.",
      "La privatisation est l’une des solutions envisagées, non le "
      "problème."]),
'ch5-qcm-33': f(niv='appliquer', sp='c5-03',
 exp="Imposer P = Cm à un monopole naturel, c’est le contraindre à vendre "
     "au-dessous de son coût moyen, puisque les coûts fixes sont élevés et "
     "que le coût moyen décroît : l’entreprise fait des pertes. D’où la "
     "nécessité d’une subvention, ou d’une tarification au coût moyen qui "
     "sacrifie une part de l’efficacité.",
 why=["Des profits élevés supposeraient un prix supérieur au coût moyen.",
      "Le marché ne s’équilibre pas : c’est précisément la défaillance.",
      "Les coûts supplémentaires ne disparaissent pas avec la "
      "réglementation."]),
'ch5-vf-1': f(niv='connaitre', sp='c5-03',
 exp="En concurrence pure et parfaite, le prix égale le coût marginal : "
     "c’est la condition d’efficacité allocative. Un prix supérieur au coût "
     "marginal signale au contraire du pouvoir de marché."),
'ch5-vf-5': f(niv='comprendre', sp='c5-03',
 exp="C’est le mécanisme même de la taxe pigouvienne : en renchérissant le "
     "bien à hauteur du dommage causé, elle fait entrer le coût externe "
     "dans le prix. Le signal-prix devient juste, et la quantité échangée "
     "rejoint l’optimum social."),
'ch5-open-1': f(niv='connaitre', sp='c5-03',
 ans={'modele': "Une externalité est l’effet de l’action d’un agent sur le "
      "bien-être d’un tiers, sans compensation par le marché. Elle est "
      "négative quand elle impose un coût — la pollution d’une usine qui "
      "dégrade la santé des riverains, la congestion, le tabagisme passif. "
      "Le coût privé est alors inférieur au coût social et le marché "
      "surproduit.",
      'cles': [{'f': ['tiers', 'autrui', 'riverain'],
                'l': 'elle affecte un tiers à la transaction'},
               {'f': ['prix', 'marche', 'compens'],
                'l': 'sans être intégrée au prix de marché'},
               {'f': ['pollution', 'congestion', 'tabac'],
                'l': 'exemple d’externalité négative'}]},
 exp="La définition suppose l’absence de compensation : si le tiers est "
     "indemnisé par contrat, l’effet est internalisé et il n’y a plus "
     "d’externalité."),
'ch5-open-2': f(niv='raisonner', sp='c5-03',
 ans={'modele': "L’innovateur ne peut pas s’approprier l’intégralité des "
      "bénéfices de sa découverte : une fois connue, elle profite aussi à "
      "ses concurrents et à la société. Son rendement privé est donc "
      "inférieur au rendement social, et il investit moins que l’optimum. "
      "D’où les brevets, qui rétablissent l’appropriation, et les "
      "subventions publiques à la recherche.",
      'cles': [{'f': ['approprier', 'appropri', 'profite'],
                'l': 'l’innovateur ne capte pas tout le bénéfice'},
               {'f': ['rendement social', 'benefice social', 'optimum'],
                'l': 'le rendement social excède le rendement privé'},
               {'f': ['sous', 'moins', 'insuffisant'],
                'l': 'd’où une production inférieure à l’optimum'},
               {'f': ['brevet', 'subvention', 'etat'],
                'l': 'brevets et subventions corrigent ce défaut'}]},
 exp="La symétrie avec les externalités négatives est parfaite : on taxe ce "
     "qui est surproduit, on subventionne ce qui est sous-produit."),
'ch5-open-11': f(niv='comprendre', sp='c5-03',
 ans={'modele': "L’État dispose de trois familles d’instruments : la "
      "réglementation — normes, interdictions, plafonds ; la fiscalité — "
      "taxe pigouvienne appliquant le principe pollueur-payeur ; et la "
      "création de marchés de droits, comme les quotas d’émission "
      "échangeables. Chacun a ses limites : rigidité de la norme, "
      "difficulté d’évaluer le dommage pour la taxe, volatilité des prix et "
      "répartition initiale pour les quotas.",
      'cles': [{'f': ['reglementation', 'norme', 'interdiction'],
                'l': 'la réglementation'},
               {'f': ['taxe', 'pigou', 'pollueur'],
                'l': 'la taxe pigouvienne'},
               {'f': ['quota', 'marche de droits', 'droit', 'permis'],
                'l': 'les marchés de droits à polluer'}]},
 exp="Le cours ajoute un avertissement : toutes ces solutions sont "
     "imparfaites, car il existe aussi des défaillances de l’État et du "
     "lobbying."),
'ch5-open-12': f(niv='comprendre', sp='c5-03',
 ans={'modele': "Dans les secteurs à très forts coûts fixes — réseaux "
      "ferrés, distribution d’eau — le coût moyen décroît sur toute la "
      "gamme de production : une seule entreprise produit à moindre coût "
      "que plusieurs. Mais laissée libre, elle fixe un prix supérieur au "
      "coût marginal et sous-produit ; contrainte à P = Cm, elle ne couvre "
      "pas ses coûts fixes. Le marché seul ne peut donc pas atteindre "
      "l’optimum.",
      'cles': [{'f': ['cout fixe', 'coût fixe'], 'l': 'des coûts fixes très élevés'},
               {'f': ['une seule', 'duplic', 'moindre cout'],
                'l': 'une seule entreprise produit à moindre coût'},
               {'f': ['prix', 'trop eleve', 'sous produ'],
                'l': 'sans régulation, prix trop élevé et sous-production'},
               {'f': ['perte', 'cout marginal', 'couvre'],
                'l': 'avec P = Cm, l’entreprise ne couvre pas ses coûts'}]},
 exp="C’est le seul cas du chapitre où la défaillance tient à la structure "
     "des coûts et non au comportement des agents."),
'ch5-open-15': f(niv='raisonner', sp='c5-03',
 ans={'modele': "L’information est non rivale : la transmettre ne la "
      "détruit pas, et l’usage d’une personne n’en prive aucune autre. Elle "
      "est aussi difficilement excluable : une fois divulguée, il est "
      "coûteux d’en empêcher la diffusion. Elle réunit donc les deux "
      "critères du bien public, ce qui explique sa sous-production par le "
      "marché et l’existence des brevets.",
      'cles': [{'f': ['non rival', 'rivalite'], 'l': 'elle est non rivale'},
               {'f': ['excluab', 'empecher', 'diffusion'],
                'l': 'elle est difficilement excluable'},
               {'f': ['brevet', 'sous produ', 'marche'],
                'l': 'd’où sa sous-production et le recours aux brevets'}]},
 exp="Ce statut explique la tension de la politique d’innovation : il "
     "faudrait diffuser l’information au coût marginal, qui est nul, mais "
     "il faut rémunérer celui qui la produit."),
# ========================= c5-04 · asymétries d'information
'ch5-qcm-17': f(niv='connaitre', sp='c5-04',
 exp="La sélection adverse est une asymétrie d’information antérieure au "
     "contrat : ne pouvant distinguer la qualité, l’acheteur ne propose "
     "qu’un prix moyen, ce qui fait sortir du marché les meilleures offres "
     "et dégrade la qualité moyenne. Le processus est cumulatif.",
 why=["Le comportement opportuniste après signature est l’aléa moral.",
      "La sélection des employés est une pratique de gestion, non une "
      "défaillance.",
      "La procédure d’appel d’offres est un mécanisme d’attribution."]),
'ch5-qcm-18': f(niv='connaitre', sp='c5-04',
 exp="L’aléa moral est une asymétrie postérieure au contrat : une fois "
     "couvert, l’agent modifie son comportement parce que l’autre partie ne "
     "peut pas l’observer. L’assuré prend davantage de risques, "
     "l’emprunteur sauvé par la garantie publique aussi.",
 why=["L’information imparfaite avant la signature est la sélection "
      "adverse.",
      "Le mauvais risque sélectionné relève également de l’ex ante.",
      "La fraude fiscale n’est pas une catégorie de l’économie de "
      "l’information."]),
'ch5-qcm-19': f(niv='connaitre', sp='c5-04',
 exp="George Akerlof publie The Market for Lemons en 1970 : sur le marché "
     "des voitures d’occasion, l’acheteur ne peut pas distinguer les bonnes "
     "voitures des « lemons ». Le prix unique chasse les bonnes voitures et "
     "le marché peut s’effondrer.",
 why=["Stiglitz travaille sur l’information imparfaite, mais l’article des "
      "lemons est d’Akerlof.",
      "Pigou analyse les externalités.",
      "Schumpeter traite de l’innovation."]),
'ch5-qcm-36': f(niv='comprendre', sp='c5-04',
 exp="La différence est temporelle : la sélection adverse est une asymétrie "
     "ex ante, qui porte sur la qualité cachée au moment de contracter ; "
     "l’aléa moral est une asymétrie ex post, qui porte sur l’action cachée "
     "après la signature. Les remèdes diffèrent : signaux et garanties pour "
     "l’une, incitations et franchises pour l’autre.",
 why=["La distinction n’oppose pas l’erreur involontaire à la fraude.",
      "Les deux phénomènes se rencontrent sur tous les marchés.",
      "Ce sont deux phénomènes distincts, pas deux noms du même."],
 diss="Savoir dater l’asymétrie — avant ou après le contrat — est ce qui "
      "permet de proposer le bon remède : c’est le genre de précision qui "
      "distingue une copie technique."),
'ch5-vf-4': f(niv='connaitre', sp='c5-04',
 exp="L’aléa moral survient après la signature : c’est le changement de "
     "comportement permis par l’impossibilité d’observer l’action de "
     "l’agent. Avant la signature, l’asymétrie porte sur une qualité cachée "
     "et s’appelle sélection adverse."),
'ch5-vf-9': f(niv='connaitre', sp='c5-04',
 exp="La sélection adverse est une asymétrie ex ante : elle joue au moment "
     "de la formation du contrat, sur une caractéristique cachée. "
     "L’asymétrie postérieure, qui porte sur un comportement, est l’aléa "
     "moral."),
'ch5-vf-20': f(niv='comprendre', sp='c5-04',
 exp="Le marché des lemons illustre la sélection adverse : l’acheteur ne "
     "peut pas distinguer la qualité avant l’achat. L’aléa moral "
     "supposerait un changement de comportement après contrat, ce qui n’est "
     "pas le mécanisme décrit par Akerlof."),
'ch5-open-8': f(niv='connaitre', sp='c5-04',
 ans={'modele': "Il y a asymétrie d’information lorsqu’une partie à "
      "l’échange en sait davantage que l’autre sur la qualité du bien ou "
      "sur son propre comportement. Elle fausse la formation des prix et "
      "peut faire disparaître un marché pourtant mutuellement avantageux.",
      'cles': [{'f': ['plus d information', 'davantage', 'mieux informe'],
                'l': 'une partie est mieux informée'},
               {'f': ['qualite', 'comportement'],
                'l': 'sur la qualité du bien ou son comportement'},
               {'f': ['marche', 'prix', 'echange'],
                'l': 'ce qui fausse le marché'}]},
 exp="Deux formes se distinguent par leur date : la sélection adverse, "
     "antérieure au contrat et portant sur une qualité cachée ; l’aléa "
     "moral, postérieur et portant sur une action cachée. Les remèdes "
     "diffèrent en conséquence — signaux et garanties pour l’une, "
     "incitations et franchises pour l’autre."),
'ch5-open-9': f(niv='comprendre', sp='c5-04',
 ans={'modele': "La sélection adverse est une asymétrie d’information "
      "antérieure au contrat. L’acheteur ne distinguant pas la qualité, il "
      "n’accepte de payer qu’un prix moyen ; les vendeurs de biens de bonne "
      "qualité se retirent, la qualité moyenne baisse, le prix baisse "
      "encore : le marché se dégrade cumulativement, comme sur le marché "
      "des voitures d’occasion d’Akerlof.",
      'cles': [{'f': ['avant', 'ex ante'], 'l': 'elle joue avant le contrat'},
               {'f': ['qualite'], 'l': 'elle porte sur une qualité cachée'},
               {'f': ['bon', 'evince', 'retire', 'lemons'],
                'l': 'les bons produits sont évincés'}]},
 exp="Le cours rapproche ce mécanisme de la loi de Gresham : la mauvaise "
     "monnaie chasse la bonne, pour exactement la même raison."),
'ch5-open-10': f(niv='comprendre', sp='c5-04',
 ans={'modele': "L’aléa moral est une asymétrie d’information postérieure "
      "au contrat : l’agent couvert modifie son comportement parce que "
      "l’autre partie ne peut pas l’observer. L’assuré tous risques devient "
      "moins prudent ; une banque certaine d’être sauvée prend davantage de "
      "risques. Les remèdes sont incitatifs : franchise, bonus-malus, "
      "participation aux pertes.",
      'cles': [{'f': ['apres', 'après', 'ex post'],
                'l': 'elle joue après la signature'},
               {'f': ['comportement', 'risque', 'moins prudent'],
                'l': 'l’agent modifie son comportement'},
               {'f': ['assur', 'exemple', 'banque'],
                'l': 'exemple de l’assurance ou de la banque'}]},
 exp="Le cours relie l’aléa moral aux sauvetages bancaires : la protection "
     "qui évite la panique encourage la prise de risque qui la prépare."),
'ch5-open-14': f(niv='comprendre', sp='c5-04',
 ans={'modele': "Le signal est une information coûteuse émise par la partie "
      "la mieux informée pour prouver sa qualité : le diplôme, selon "
      "Michael Spence, signale les capacités d’un candidat à un employeur "
      "qui ne peut pas les observer. Le signal n’est crédible que s’il est "
      "plus coûteux à produire pour les mauvais candidats que pour les bons.",
      'cles': [{'f': ['signal', 'prouve', 'montre'],
                'l': 'il permet de prouver sa qualité'},
               {'f': ['diplome', 'spence'], 'l': 'le diplôme en est l’exemple'},
               {'f': ['cout', 'coût', 'credible'],
                'l': 'il doit être coûteux pour être crédible'}]},
 exp="La signalisation est l’une des trois réponses aux asymétries, avec la "
     "réputation et la réglementation : elle fonctionne sans intervention "
     "publique, mais elle a un coût social réel."),
'ch5-aut195-1': f(niv='raisonner', sp='c5-04',
 exp="« La mauvaise monnaie chasse la bonne » : si l’acheteur ne peut pas "
     "distinguer la qualité, le prix unique rémunère également les bonnes "
     "et les mauvaises unités. Les bonnes se retirent, la qualité moyenne "
     "baisse, le prix suit, et le cycle recommence. C’est exactement le "
     "mécanisme de la sélection adverse.",
 why=["L’aléa moral suppose un comportement modifié après contrat, non une "
      "éviction par les prix.",
      "L’externalité positive décrit un bénéfice non rémunéré à un tiers.",
      "Le passager clandestin profite d’un bien non excluable."],
 diss="Rapprocher Gresham d’Akerlof montre qu’un même mécanisme "
      "informationnel traverse les siècles et les marchés — monnaie, "
      "voitures, assurance, crédit."),
# ================== c5-05 à c5-07 · Coase, État, Ostrom
'ch5-qcm-2': f(niv='connaitre', sp='c5-05',
 exp="Le chapitre étudie quatre défaillances : le monopole naturel, les "
     "biens collectifs et communs, les externalités et les asymétries "
     "d’information. Chacune justifie une forme d’intervention différente, "
     "et aucune ne justifie à elle seule une intervention générale.",
 why=["Oligopole et fraude ne sont pas les quatre cas retenus.",
      "Inflation et chômage sont des déséquilibres macroéconomiques.",
      "La typologie des biens est un instrument d’analyse, pas la liste des "
      "défaillances."]),
'ch5-qcm-22': f(niv='comprendre', sp='c5-05',
 exp="La théorie des choix publics applique l’analyse économique aux "
     "décisions publiques : les responsables poursuivent leurs propres "
     "objectifs — réélection, budget, carrière — et le processus politique "
     "connaît ses propres défaillances : bureaucratie, capture, recherche "
     "de rente.",
 why=["Supposer que la décision publique maximise toujours le bien-être est "
      "précisément ce que cette théorie récuse.",
      "Elle ne soutient pas la supériorité du secteur public.",
      "Ce n’est pas l’ensemble des politiques de régulation, mais une "
      "théorie du comportement des décideurs."],
 diss="Cette théorie est l’argument obligé de la troisième partie : "
      "constater une défaillance de marché ne suffit pas à conclure à "
      "l’intervention, encore faut-il comparer les deux imperfections."),
'ch5-vf-16': f(niv='raisonner', sp='c5-05',
 exp="Avec une discrimination parfaite, le monopoleur fait payer à chacun "
     "exactement son consentement à payer : toutes les unités dont la "
     "valeur dépasse le coût marginal sont vendues, donc la perte sèche "
     "disparaît. Mais la totalité du surplus est captée par le producteur : "
     "l’efficacité est atteinte, l’équité pas du tout."),
'ch5-vf-17': f(niv='raisonner', sp='c5-05',
 exp="L’échec complet est un cas extrême. Des mécanismes correcteurs "
     "existent : signaux comme le diplôme ou la garantie, réputation "
     "entretenue par la répétition des échanges, réglementation imposant la "
     "transparence. L’asymétrie dégrade le marché, elle ne l’anéantit pas "
     "toujours."),
'ch5-vf-19': f(niv='connaitre', sp='c5-05',
 exp="C’est le programme de l’économie du bien-être : évaluer les "
     "allocations à l’aune de l’utilité collective, et identifier les "
     "situations où le marché n’y parvient pas. Pigou en tire la "
     "justification d’interventions ciblées."),
'ch5-aut195-2': f(niv='raisonner', sp='c5-05',
 exp="La recherche de rente désigne les ressources consacrées à obtenir un "
     "avantage distribué par la décision publique — lobbying, démarches, "
     "influence — plutôt qu’à produire. Ces dépenses sont rentables pour "
     "celui qui les engage et stériles pour la collectivité : elles "
     "déplacent la richesse sans en créer.",
 why=["L’investissement productif crée de la valeur : c’est l’inverse.",
      "L’épargne placée en obligations finance la dépense publique, elle ne "
      "capte pas de rente.",
      "Le loyer immobilier est un revenu de facteur, non une rente au sens "
      "de Tullock."],
 diss="Argument central contre l’interventionnisme systématique : plus "
      "l’État distribue d’avantages, plus il est rationnel de dépenser pour "
      "les obtenir, et plus la production nette diminue."),
'ch5-qcm-3': f(niv='connaitre', sp='c5-06',
 exp="Pigou est un économiste libéral : il admet l’efficacité générale du "
     "marché mais démontre qu’en présence d’externalités, le prix privé "
     "diverge du coût social. Il en tire la justification d’une "
     "intervention ciblée, la taxe, et non d’une substitution de l’État au "
     "marché.",
 why=["Pigou n’est pas marxiste : il travaille dans le cadre néoclassique.",
      "La théorie des jeux est née avec von Neumann et Morgenstern.",
      "Il analyse le monopole naturel mais n’en est pas le défenseur."]),
'ch5-vf-13': f(niv='comprendre', sp='c5-06',
 exp="Pigou est libéral, et antérieur à Keynes dans ses travaux fondateurs. "
     "Son interventionnisme est ciblé : il ne porte pas sur la demande "
     "globale mais sur la correction des externalités, par la taxe ou la "
     "subvention."),
'ch5-open-13': f(niv='comprendre', sp='c5-06',
 ans={'modele': "Internaliser une externalité, c’est faire entrer le coût "
      "ou le bénéfice externe dans le calcul de l’agent, afin que le prix "
      "de marché reflète le coût social. Deux voies : la taxe ou la "
      "subvention chez Pigou ; la définition de droits de propriété "
      "échangeables et la négociation chez Coase.",
      'cles': [{'f': ['integre', 'intègre', 'internalis'],
                'l': 'le coût externe entre dans le calcul privé'},
               {'f': ['taxe', 'subvention', 'pigou'],
                'l': 'par la taxe ou la subvention'},
               {'f': ['coase', 'droit de propriete', 'negociation', 'marche'],
                'l': 'ou par les droits de propriété et la négociation'}]},
 exp="Les deux voies visent le même résultat — un prix qui dise la vérité "
     "sociale — mais elles supposent des conditions différentes : "
     "information de l’État pour la taxe, faibles coûts de transaction pour "
     "la négociation."),
'ch5-vf-12': f(niv='raisonner', sp='c5-07',
 exp="Ostrom nuance fortement la thèse de Hardin : l’étude de nombreux "
     "communs — pêcheries, irrigation, forêts — montre que des communautés "
     "s’organisent, définissent des règles d’usage, des sanctions graduées "
     "et des mécanismes de résolution des conflits, et gèrent durablement "
     "la ressource sans privatisation ni étatisation."),
'ch5-open-7': f(niv='comprendre', sp='c5-07',
 ans={'modele': "Ostrom montre qu’une troisième voie existe entre le marché "
      "et l’État : l’auto-organisation des usagers. Les communautés qui "
      "réussissent définissent des limites claires de la ressource et du "
      "groupe, des règles d’usage adaptées au contexte local, des "
      "dispositifs de surveillance mutuelle, des sanctions graduées et des "
      "mécanismes de résolution des conflits.",
      'cles': [{'f': ['communaute', 'auto organisation', 'collectif', 'local'],
                'l': 'des communautés s’auto-organisent'},
               {'f': ['regle', 'règle', 'usage'],
                'l': 'elles définissent des règles d’usage'},
               {'f': ['sanction', 'surveillance', 'controle'],
                'l': 'avec surveillance et sanctions'},
               {'f': ['privatisation', 'etat', 'troisieme'],
                'l': 'sans privatisation ni étatisation'}]},
 exp="L’apport est double : empirique — des communs sont bien gérés depuis "
     "des siècles — et théorique : la propriété n’a pas à être soit privée "
     "soit publique, les formes collectives sont viables sous conditions."),
})


# =============================================================== questions neuves
NEW = [

f(id='q5-n01', sp='c5-01', niv='connaitre', type='assoc', b=52,
  q="Associez chaque type de monopole à son origine.",
  ans=[["Monopole naturel", "Des coûts fixes élevés et des rendements croissants rendent une seule firme efficace"],
       ["Monopole d’innovation", "Un brevet protège l’innovateur pendant une durée pouvant atteindre vingt ans"],
       ["Monopole d’effet de réseau", "L’utilité du service croît avec le nombre d’utilisateurs"],
       ["Monopole d’institution", "L’État réserve l’activité à un opérateur, comme la Française des jeux"]],
  exp="Les quatre monopoles n’appellent pas la même réponse publique : le "
      "naturel se régule, celui d’innovation se limite dans le temps, celui "
      "de réseau interroge le droit de la concurrence, celui d’institution "
      "relève d’un choix politique. Confondre leurs origines conduit à "
      "proposer le mauvais remède.",
  diss="Cette typologie permet de répondre finement à un sujet sur la "
       "concurrence : « faut-il casser les monopoles ? » n’a pas la même "
       "réponse selon leur origine."),

f(id='q5-n02', sp='c5-01', niv='raisonner', type='ordre', b=46,
  q="Remettez dans l’ordre le raisonnement qui fait du monopole naturel une "
    "défaillance de marché.",
  ans=["Les coûts fixes sont très élevés et le coût moyen décroît avec la quantité",
       "Une seule entreprise produit donc à un coût inférieur à celui de plusieurs",
       "Si on lui impose P = Cm, elle ne couvre pas ses coûts fixes et subit des pertes",
       "Si on la laisse libre, elle fixe P > Cm, sous-produit et crée une perte sèche",
       "Le marché ne peut donc pas atteindre seul l’optimum : régulation, subvention ou propriété publique"],
  exp="La défaillance tient à une impossibilité, non à un comportement "
      "fautif : aucune organisation marchande ne peut concilier efficacité "
      "allocative et viabilité financière lorsque le coût moyen décroît "
      "partout. C’est ce qui distingue ce cas des autres défaillances, où "
      "c’est le comportement des agents qui est en cause.",
  diss="Enchaînement à reproduire pour justifier rigoureusement un service "
       "public de réseau, sans se contenter de l’argument d’intérêt "
       "général."),

f(id='q5-n03', sp='c5-02', niv='appliquer', type='qcm', b=202,
  q="Une autoroute à péage, fluide, est-elle rivale ? excluable ? De quel "
    "type de bien s’agit-il ?",
  opts=["Rivale et excluable : bien privé",
        "Non rivale et excluable : bien de club",
        "Rivale et non excluable : bien commun",
        "Non rivale et non excluable : bien public pur"],
  ans=1,
  why=["Tant que la circulation est fluide, l’usage d’un automobiliste ne "
       "gêne pas les autres : il n’y a pas rivalité.",
       "Le péage permet précisément d’exclure : la non-excluabilité est "
       "exclue.",
       "Les deux critères du bien public pur sont démentis par le péage et "
       "par la fluidité."],
  exp="Le péage rend le bien excluable, la fluidité le rend non rival : "
      "c’est un bien de club. L’exemple montre que le classement dépend des "
      "conditions concrètes : en cas d’embouteillage, la rivalité "
      "apparaît et l’autoroute se rapproche du bien commun.",
  diss="Montrer qu’un même bien change de catégorie selon la congestion ou "
       "la technologie de péage évite les classements mécaniques et montre "
       "la souplesse de la grille."),

f(id='q5-n04', sp='c5-02', niv='raisonner', type='qcm', b=241,
  q="Pourquoi le problème du passager clandestin justifie-t-il le "
    "financement par l’impôt plutôt que par la vente ?",
  opts=["Parce que l’État produit toujours à moindre coût",
        "Parce qu’on ne peut pas exclure celui qui ne paie pas, si bien que "
        "personne n’a intérêt à payer volontairement",
        "Parce que les biens publics coûtent trop cher",
        "Parce que la demande de biens publics est inélastique"],
  ans=1,
  why=["Rien n’assure que l’État produise moins cher : c’est une autre "
       "question.",
       "Le coût absolu n’est pas l’argument : des biens coûteux sont vendus "
       "sur le marché.",
       "L’élasticité de la demande n’entre pas dans ce raisonnement."],
  exp="L’argument est logique, non moral : puisque l’exclusion est "
      "impossible, chacun a intérêt à attendre que les autres financent. Si "
      "tous raisonnent ainsi, le bien n’est pas produit alors même qu’il "
      "est unanimement désiré. Le caractère obligatoire de l’impôt est la "
      "réponse à ce blocage.",
  diss="Ce raisonnement est transposable à l’action collective en général : "
       "accords climatiques, cotisations syndicales, vaccination."),

f(id='q5-n05', sp='c5-03', niv='appliquer', type='qcm', b=565,
  q="Une usine produit un bien dont le coût privé marginal est de 10 € et "
    "qui impose à des riverains un dommage marginal de 4 €. Quelle taxe "
    "pigouvienne faut-il appliquer ?",
  opts=["14 €, pour couvrir le coût social total",
        "4 €, pour porter le coût privé au niveau du coût social",
        "10 €, pour doubler le coût de production",
        "Aucune : il faut interdire la production"],
  ans=1,
  why=["Taxer de 14 € ferait payer deux fois le coût de production.",
       "Doubler le coût n’a aucun fondement : la taxe se règle sur le "
       "dommage, pas sur le coût privé.",
       "L’interdiction supprimerait aussi la production socialement utile : "
       "l’optimum n’est pas une pollution nulle."],
  exp="La taxe pigouvienne est égale au dommage marginal, soit 4 € : elle "
      "porte le coût privé de 10 à 14 €, c’est-à-dire au coût social. Le "
      "producteur réduit alors sa production jusqu’au point où la valeur de "
      "la dernière unité pour le consommateur égale son coût social. "
      "L’objectif n’est pas de supprimer la pollution mais de la ramener à "
      "son niveau optimal.",
  diss="Insister sur le fait que l’optimum de pollution n’est pas nul "
       "montre qu’on a compris la logique coût-bénéfice, et évite le "
       "contresens le plus fréquent sur Pigou."),

f(id='q5-n06', sp='c5-03', niv='comprendre', type='qcmm', b=766,
  q="Quelles propositions décrivent correctement un marché de quotas "
    "d’émission échangeables ? (plusieurs réponses)",
  opts=["L’État fixe un plafond global d’émissions et attribue des quotas",
        "Les entreprises qui polluent peu peuvent vendre leurs quotas",
        "La réduction de la pollution se fait au moindre coût collectif",
        "Le prix du carbone y est fixé administrativement",
        "Le dispositif est exempt de risque de spéculation"],
  ans=[0, 1, 2],
  why=["Exacte : c’est l’architecture du système, le plafond étant la "
       "variable environnementale.",
       "Exacte : celles qui réduisent à bas coût vendent, celles pour qui "
       "c’est coûteux achètent.",
       "Exacte : la réduction est réalisée par ceux qui peuvent la faire au "
       "moindre coût.",
       "Le prix résulte au contraire de l’échange : c’est la quantité qui "
       "est fixée, non le prix.",
       "Le cours signale explicitement le risque de spéculation, avec la "
       "volatilité des prix et le problème de l’allocation initiale."],
  exp="L’opposition avec la taxe est analytique : la taxe fixe un prix et "
      "laisse la quantité s’ajuster ; le quota fixe une quantité et laisse "
      "le prix s’ajuster. Le choix dépend de ce que l’on veut garantir — "
      "la certitude environnementale ou la prévisibilité du coût."),

f(id='q5-n07', sp='c5-04', niv='appliquer', type='vf', b=624,
  q="Sur le marché des voitures d’occasion décrit par Akerlof, c’est le "
    "vendeur d’une bonne voiture qui est pénalisé par l’asymétrie "
    "d’information.",
  ans=True,
  exp="L’acheteur ne pouvant pas distinguer la qualité, il n’offre qu’un "
      "prix correspondant à la qualité moyenne. Ce prix est insuffisant "
      "pour le propriétaire d’une bonne voiture, qui renonce à vendre, "
      "tandis qu’il est avantageux pour le vendeur d’un « lemon ». La "
      "qualité moyenne baisse alors, le prix suit, et le mécanisme se "
      "répète jusqu’à l’effondrement possible du marché.",
  diss="L’intérêt de l’exemple est de montrer que l’asymétrie ne lèse pas "
       "seulement la partie mal informée : elle détruit des échanges "
       "mutuellement avantageux, ce qui est une perte collective."),

f(id='q5-n08', sp='c5-04', niv='raisonner', type='ordre', b=617,
  q="Remettez dans l’ordre le mécanisme de la sélection adverse sur le "
    "marché des voitures d’occasion.",
  ans=["L’acheteur ne peut pas distinguer les bonnes voitures des mauvaises",
       "Il ne propose qu’un prix correspondant à la qualité moyenne attendue",
       "Les propriétaires de bonnes voitures refusent de vendre à ce prix",
       "La qualité moyenne des voitures offertes baisse",
       "Le prix proposé baisse à son tour et le marché se dégrade"],
  exp="Le caractère cumulatif est l’essentiel : chaque tour aggrave le "
      "précédent, et rien dans le marché n’arrête la spirale. C’est "
      "pourquoi le cours rapproche ce mécanisme de la loi de Gresham. Les "
      "remèdes — garantie, contrôle technique, réputation, certification — "
      "visent tous à rétablir l’information au premier maillon.",
  diss="Enchaînement très efficace pour montrer qu’un marché peut "
       "disparaître sans qu’aucun agent ne se comporte de façon "
       "irrationnelle."),

f(id='q5-n09', sp='c5-06', niv='comprendre', type='qcm', b=1084,
  q="Comment Coase propose-t-il de traiter une externalité, et à quelle "
    "condition sa solution fonctionne-t-elle ?",
  opts=["Par une taxe assise sur le dommage, si l’État connaît ce dommage",
        "Par la définition de droits de propriété échangeables et la "
        "négociation privée, si les coûts de transaction sont faibles",
        "Par l’interdiction de l’activité polluante",
        "Par la nationalisation de l’entreprise responsable"],
  ans=1,
  why=["La taxe est la solution de Pigou, que Coase discute précisément.",
       "L’interdiction n’est pas une solution de marché.",
       "La nationalisation ne figure pas dans l’analyse de Coase."],
  exp="Coase déplace le problème : l’externalité n’est pas un défaut du "
      "marché mais une conséquence de droits de propriété mal définis. Si "
      "ces droits sont clairement attribués et échangeables, les parties "
      "peuvent négocier et parvenir à une allocation efficace, quelle que "
      "soit l’attribution initiale. La condition est décisive : des coûts "
      "de transaction faibles, donc peu d’acteurs et un bien délimitable.",
  diss="Opposer Pigou et Coase est l’un des exercices les plus rentables du "
       "chapitre : l’un corrige le marché par l’impôt, l’autre l’étend par "
       "la propriété ; les deux supposent une information que personne ne "
       "détient complètement."),

f(id='q5-n10', sp='c5-06', niv='raisonner', type='qcmm', b=1124,
  q="Dans quels cas la solution coasienne devient-elle inopérante, selon le "
    "cours ? (plusieurs réponses)",
  opts=["Lorsque le bien est difficile à délimiter, comme l’air ou le climat",
        "Lorsque les acteurs concernés sont trop nombreux",
        "Lorsque les coûts de transaction sont élevés",
        "Lorsque l’État refuse de taxer",
        "Lorsque les entreprises sont de grande taille"],
  ans=[0, 1, 2],
  why=["Exacte : on ne peut pas attribuer de droits de propriété sur l’air "
       "ou le climat.",
       "Exacte : la négociation devient impraticable au-delà de quelques "
       "parties.",
       "Exacte : c’est la condition centrale du théorème.",
       "L’attitude de l’État en matière fiscale est sans rapport avec la "
       "faisabilité de la négociation.",
       "La taille des entreprises n’est pas le critère : c’est le nombre de "
       "parties et le coût de la négociation."],
  exp="Le cours cite l’air, les océans, le climat et la pollution diffuse : "
      "dans ces cas, la négociation est trop coûteuse, le marché devient "
      "inefficace et l’intervention publique redevient nécessaire. Il "
      "rappelle que Coase n’est pas anti-État : il compare des coûts "
      "institutionnels, il ne récuse pas l’intervention par principe."),

f(id='q5-n11', sp='c5-05', niv='raisonner', type='qcm', b=785,
  q="Le cours conclut que « toutes ces solutions sont imparfaites ». Quel "
    "argument soutient cette conclusion ?",
  opts=["Les instruments de correction coûtent toujours plus cher que la "
        "défaillance",
        "Il existe aussi des défaillances de l’État : bureaucratie, "
        "lobbying, recherche de rente",
        "Les externalités sont impossibles à mesurer",
        "Les marchés finissent toujours par s’autoréguler"],
  ans=1,
  why=["Rien n’établit que le remède coûte systématiquement plus que le "
       "mal : c’est précisément ce qu’il faut comparer au cas par cas.",
       "La mesure des externalités est difficile mais non impossible.",
       "L’autorégulation est ce que les défaillances contredisent."],
  exp="La conclusion est une invitation à la comparaison institutionnelle : "
      "face à une défaillance de marché avérée, il faut encore montrer que "
      "l’intervention publique fera mieux, compte tenu de ses propres "
      "imperfections — information incomplète, capture par les intérêts "
      "organisés, coûts administratifs.",
  diss="C’est la bonne manière de conclure un sujet sur l’intervention de "
       "l’État : ni confiance aveugle dans le marché, ni foi automatique "
       "dans l’État, mais comparaison des imperfections."),

f(id='q5-n12', sp='c5-07', niv='comprendre', type='qcm', b=1243,
  q="Qu’appelle-t-on « tragédie des anti-communs » ?",
  opts=["La surexploitation d’une ressource commune faute de propriétaire",
        "Une situation où des droits de propriété trop nombreux et "
        "fragmentés bloquent l’usage d’une ressource",
        "La privatisation d’un bien public",
        "L’échec d’une communauté à se doter de règles"],
  ans=1,
  why=["La surexploitation faute de propriétaire est la tragédie des "
       "communs, le cas symétrique.",
       "La privatisation est un mode de gestion, non une tragédie en soi.",
       "L’échec des règles collectives est ce qu’Ostrom étudie, sous un "
       "autre angle."],
  exp="La tragédie des anti-communs est l’exact symétrique de celle de "
      "Hardin : là, trop peu de propriété conduisait à la surexploitation ; "
      "ici, trop de droits exclusifs enchevêtrés — brevets multiples sur "
      "une même technologie, parcelles trop fragmentées — empêchent "
      "l’usage, chacun pouvant bloquer les autres.",
  diss="Mettre les deux tragédies en regard montre que la propriété n’est "
       "pas une solution universelle : son défaut comme son excès "
       "engendrent des blocages."),

f(id='q5-n13', sp='c5-07', niv='raisonner', type='courte', b=1324,
  q="En quoi l’apport d’Elinor Ostrom déplace-t-il le débat entre marché et "
    "État ?",
  ans={'modele': "Hardin concluait à une alternative : privatiser la "
       "ressource ou la confier à l’État. Ostrom montre, par l’étude de "
       "communs effectivement gérés — pêcheries, systèmes d’irrigation, "
       "forêts — qu’une troisième voie existe : l’auto-organisation des "
       "usagers, fondée sur des limites claires, des règles adaptées au "
       "contexte, une surveillance mutuelle, des sanctions graduées et des "
       "mécanismes de résolution des conflits. La propriété collective "
       "devient une forme viable, à côté de la propriété privée et de la "
       "propriété publique.",
       'cles': [{'f': ['hardin', 'alternative', 'privatis', 'etat'],
                 'l': 'elle dépasse l’alternative marché / État'},
                {'f': ['communaute', 'usager', 'auto organisation', 'collectif'],
                 'l': 'par l’auto-organisation des usagers'},
                {'f': ['regle', 'sanction', 'surveillance'],
                 'l': 'avec des règles, une surveillance et des sanctions'},
                {'f': ['durable', 'empirique', 'etude', 'fonctionne'],
                 'l': 'démonstration empirique sur des communs réels'}]},
  exp="Le déplacement est aussi méthodologique : Ostrom procède par "
      "comparaison de cas réels plutôt que par déduction à partir d’un "
      "modèle, ce qui lui permet d’identifier les conditions de réussite "
      "plutôt qu’un résultat général.",
  diss="Référence précieuse en troisième partie : elle permet de sortir de "
       "l’opposition binaire et d’introduire les institutions comme "
       "variable."),

f(id='q5-n14', sp='c5-05', niv='appliquer', type='vf', b=905,
  q="Un monopole qui pratique la discrimination parfaite des prix est "
    "préférable du point de vue de l’équité comme de l’efficacité.",
  ans=False,
  exp="Il est préférable du point de vue de l’efficacité seulement : en "
      "faisant payer chacun à son consentement à payer, il vend toutes les "
      "unités dont la valeur dépasse le coût marginal et la perte sèche "
      "disparaît. Mais la totalité du surplus est captée par le "
      "producteur : le consommateur ne conserve rien. Efficacité et équité "
      "se séparent ici de la façon la plus nette.",
  diss="Cas d’école pour montrer qu’un critère d’efficacité ne dit rien de "
       "la répartition : l’optimum de Pareto est compatible avec des "
       "situations très inégalitaires."),
]
