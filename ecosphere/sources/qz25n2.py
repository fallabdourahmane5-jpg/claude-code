# -*- coding: utf-8 -*-
"""Chapitre 25 — questions nouvelles, zone euro, policy mix et économie fermée."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c25-17
f(id='q25-n19', sp='c25-17', niv='raisonner', type='qcm', b=3560,
  q="Comment le triangle de Mundell éclaire-t-il la création de l’euro ?",
  opts=["Il montre que la monnaie unique était interdite par la théorie",
        "La combinaison de la libre circulation des capitaux et de la "
        "recherche de stabilité des changes rendait difficile le maintien de "
        "politiques monétaires nationales autonomes",
        "Il prouve que les changes flexibles étaient préférables",
        "Il impose un budget fédéral européen"],
  ans=1,
  why=["Le triangle n’interdit rien : il décrit des arbitrages.",
       "Le choix des changes flexibles entre pays européens était possible, "
       "mais c’est précisément ce que les États ont refusé.",
       "Le triangle ne dit rien du budget : la question budgétaire est "
       "distincte."],
  exp="À partir des années 1980, les pays européens renforcent la libre "
      "circulation des capitaux tout en cherchant à stabiliser leurs changes. "
      "Dès lors, une politique monétaire nationale trop expansionniste "
      "provoque des sorties de capitaux, donc une pression à la dépréciation, "
      "donc l’obligation de resserrer pour défendre la parité. Les politiques "
      "monétaires nationales deviennent fortement interdépendantes : la "
      "monnaie unique est une réponse institutionnelle à cette "
      "interdépendance, les États renonçant à une autonomie individuelle pour "
      "participer à une décision commune.",
  diss="Formule efficace : l’euro ne supprime pas une autonomie, il "
       "institutionnalise la perte d’une autonomie déjà effective."),

f(id='q25-n20', sp='c25-17', niv='raisonner', type='qcmm', b=3581,
  q="Quelles difficultés une relance budgétaire nationale soulève-t-elle dans "
    "la zone euro ? (plusieurs réponses)",
  opts=["Les États membres ne disposent pas chacun d’une banque centrale "
        "défendant leur propre parité, ce qui limite l’accompagnement "
        "monétaire automatique",
        "Elle produit des effets de débordement vers les partenaires "
        "européens",
        "Elle se heurte aux règles budgétaires européennes",
        "Elle pose une question de soutenabilité de la dette",
        "Elle suppose une dépréciation de la monnaie nationale"],
  ans=[0, 1, 2, 3],
  why=["Exacte : l’application du modèle de changes fixes doit donc être "
       "nuancée.",
       "Exacte : une partie de la demande supplémentaire s’adresse aux "
       "producteurs des autres États membres.",
       "Exacte : les critères de Maastricht et le Pacte de stabilité "
       "encadrent cette souveraineté.",
       "Exacte : l’absence de banque centrale nationale rend la question du "
       "financement plus sensible.",
       "Inexacte : il n’existe plus de monnaie nationale à déprécier entre "
       "membres de la zone."],
  exp="Le modèle prédit qu’en changes fixes avec forte mobilité des capitaux "
      "la politique budgétaire est particulièrement efficace, ce qui donne "
      "aux États membres un instrument important. Mais l’union monétaire "
      "n’est pas un simple régime de changes fixes : l’accompagnement "
      "monétaire n’est pas automatique au niveau national, et les effets de "
      "débordement créent un problème de coordination.",
  diss="Articulation décisive : les effets de débordement rendent la "
       "coordination budgétaire souhaitable, exactement comme pour les "
       "relances nationales non coordonnées."),

f(id='q25-n21', sp='c25-17', niv='comprendre', type='qcm', b=3630,
  q="Pourquoi la faiblesse du budget européen limite-t-elle la stabilisation "
    "macroéconomique de la zone ?",
  opts=["Parce qu’un budget d’environ 1 % du revenu national brut ne permet "
        "pas d’absorber les chocs comme le ferait un budget fédéral",
        "Parce que le budget européen est interdit par les traités",
        "Parce que la BCE refuse de financer les États",
        "Parce que les États membres n’ont plus de budget national"],
  ans=0,
  why=["Le budget européen existe et est prévu par les traités.",
       "Le mandat de la BCE est une question distincte de la taille du "
       "budget.",
       "Les États membres conservent au contraire leurs budgets nationaux, "
       "qui sont l’essentiel de la dépense publique."],
  exp="Dans un État fédéral, le budget central absorbe une partie des chocs "
      "asymétriques par des transferts automatiques entre régions. La "
      "faiblesse relative du budget européen — un peu plus de 1 % du revenu "
      "national brut dans les cadres budgétaires habituels — interdit une "
      "stabilisation centralisée comparable. La charge de l’ajustement "
      "repose donc sur les budgets nationaux, eux-mêmes encadrés par les "
      "règles européennes.",
  diss="Conséquence à formuler : la zone euro a mutualisé la monnaie sans "
       "mutualiser la stabilisation budgétaire."),

# ------------------------------------------------------------- c25-18
f(id='q25-n22', sp='c25-18', niv='raisonner', type='qcm', b=3811,
  q="Sur quel principe repose la règle d’affectation de Mundell ?",
  opts=["Chaque instrument doit être utilisé dans le même sens que l’autre",
        "Chaque instrument doit être affecté à l’objectif pour lequel il "
        "possède l’efficacité relative la plus grande",
        "Les deux instruments doivent être confiés à une même autorité",
        "La politique budgétaire doit toujours être restrictive"],
  ans=1,
  why=["Utiliser les deux instruments dans le même sens revient à renoncer à "
       "l’idée même d’affectation.",
       "La règle suppose au contraire deux autorités distinctes, chacune "
       "responsable d’un objectif.",
       "Aucune orientation n’est prescrite a priori : elle dépend du "
       "déséquilibre constaté."],
  exp="Concrètement, le budget est affecté à l’équilibre interne parce qu’il "
      "agit directement sur la demande globale, et la monnaie à l’équilibre "
      "externe parce qu’elle agit sur les mouvements de capitaux par les taux "
      "d’intérêt. La règle permet ainsi de traiter deux objectifs avec deux "
      "instruments, ce qui résout en principe les dilemmes identifiés "
      "précédemment.",
  diss="Limite à mentionner : la règle suppose une coordination parfaite "
       "entre autorité budgétaire et autorité monétaire, ce que la zone euro "
       "ne garantit pas."),

f(id='q25-n23', sp='c25-18', niv='appliquer', type='assoc', b=3917,
  q="Associez chaque régime de change, en mobilité parfaite des capitaux, à "
    "l’efficacité des deux politiques.",
  ans=[["Changes fixes : la politique monétaire",
        "Inefficace, l'expansion initiale est annulée"],
       ["Changes fixes : la politique budgétaire",
        "Très efficace, amplifiée par l'accompagnement monétaire"],
       ["Changes flexibles : la politique monétaire",
        "Très efficace, renforcée par la dépréciation"],
       ["Changes flexibles : la politique budgétaire",
        "Neutralisée par l'appréciation de la monnaie"]],
  exp="Ce tableau est le résultat central du modèle Mundell-Fleming. Sa "
      "logique est unique : dans chaque régime, l’une des deux variables — "
      "masse monétaire ou taux de change — doit s’ajuster pour maintenir "
      "r = r*. En changes fixes, c’est la masse monétaire, ce qui annule la "
      "politique monétaire et amplifie la politique budgétaire. En changes "
      "flexibles, c’est le change, ce qui amplifie la politique monétaire et "
      "neutralise la politique budgétaire.",
  diss="Tableau à reproduire systématiquement en introduction de partie : il "
       "structure à lui seul toute l’analyse en économie ouverte."),

f(id='q25-n24', sp='c25-18', niv='comprendre', type='qcm', b=3917,
  q="Pourquoi un solde courant excédentaire ne suffit-il pas à conclure à un "
    "excédent de la balance globale ?",
  opts=["Parce que le solde courant est toujours faux",
        "Parce que la balance globale intègre aussi les mouvements autonomes "
        "de capitaux, qui peuvent excéder l’excédent courant",
        "Parce que la balance des paiements n’est jamais équilibrée",
        "Parce que le solde courant ne comprend pas les services"],
  ans=1,
  why=["Le solde courant est un agrégat statistique valide : il mesure "
       "simplement autre chose.",
       "La balance des paiements est équilibrée par construction, sous "
       "réserve des erreurs et omissions, mais ses soldes intermédiaires ne "
       "le sont pas.",
       "Le solde courant comprend bien les échanges de services."],
  exp="L’exemple du cours est parlant : avec un excédent courant de 100 et "
      "des sorties de capitaux de 140, la balance globale est déficitaire de "
      "40. C’est précisément cette distinction qu’exploite la courbe BP, qui "
      "représente l’équilibre de la balance globale et non celui du seul "
      "solde courant.",
  diss="Rigueur comptable qui fait la différence : toujours préciser de quel "
       "solde on parle avant de conclure à un déséquilibre."),

f(id='q25-n25', sp='c25-18', niv='raisonner', type='qcm', b=3917,
  q="Pourquoi l’effet d’une dépréciation sur le solde commercial peut-il être "
    "d’abord défavorable ?",
  opts=["Parce que la dépréciation réduit les exportations",
        "Parce que les volumes réagissent avec retard tandis que les prix "
        "changent immédiatement : c’est l’effet de courbe en J",
        "Parce que la dépréciation augmente le taux d’intérêt",
        "Parce que les importations deviennent moins chères"],
  ans=1,
  why=["La dépréciation rend au contraire les produits nationaux moins chers "
       "pour l’étranger.",
       "La dépréciation n’agit pas directement sur le taux d’intérêt.",
       "Les importations deviennent plus chères, non moins chères."],
  exp="À court terme, la facture des importations se renchérit immédiatement "
      "alors que les volumes exportés n’ont pas encore progressé : la balance "
      "commerciale se dégrade avant de s’améliorer, d’où la forme en J. "
      "L’ampleur et le délai de l’ajustement dépendent de trois facteurs : "
      "les élasticités-prix, les délais de réaction des acheteurs et le "
      "contenu importé des exportations — une dépréciation renchérit en "
      "effet les intrants importés des exportateurs eux-mêmes.",
  diss="Nuance indispensable à apporter au résultat « changes flexibles = "
       "politique monétaire efficace » : l’efficacité suppose du temps."),

# ------------------------------------------------------------- c25-08
f(id='q25-n26', sp='c25-08', niv='appliquer', type='assoc', b=1838,
  q="Associez chaque policy mix historique à sa combinaison d’instruments.",
  ans=[["La réunification allemande du début des années 1990",
        "Budget expansionniste et monnaie restrictive"],
       ["Le policy mix Clinton-Greenspan des années 1990",
        "Budget restrictif et monnaie accommodante"],
       ["La relance française de mai 1981",
        "Budget expansionniste, dans un environnement non coordonné"],
       ["Le tournant de la rigueur de mars 1983",
        "Orientation restrictive, pour maintenir la parité du franc"]],
  exp="Les deux cas sont symétriques et permettent de comprendre la logique "
      "du policy mix. En Allemagne, les dépenses de réunification déplacent "
      "IS vers la droite tandis que la Bundesbank déplace LM vers la gauche "
      "pour contenir l’inflation : l’activité est préservée au prix de taux "
      "d’intérêt élevés, qui passent de 4,3 % en 1988 à 9,2 % en 1991. Aux "
      "États-Unis, la consolidation budgétaire déplace IS vers la gauche et "
      "l’assouplissement monétaire LM vers la droite : le solde budgétaire "
      "passe de − 4,5 % à + 0,8 % du PIB entre 1992 et 1998, la croissance "
      "atteint 3,7 % en 1998 et les taux à un an reculent de 5,5 % à 4,8 %.",
  diss="Leçon générale : ce n’est pas l’orientation de chaque politique qui "
       "compte, c’est leur combinaison."),

f(id='q25-n27', sp='c25-08', niv='raisonner', type='qcm', b=1728,
  q="Pourquoi une politique procyclique n’est-elle pas nécessairement "
    "irrationnelle, selon la nuance du cours ?",
  opts=["Parce qu’elle amortit toujours les fluctuations",
        "Parce qu’elle peut servir d’autres objectifs que la stabilisation du "
        "cycle, même si elle contredit celui-ci",
        "Parce qu’elle est imposée par les traités",
        "Parce qu’elle réduit mécaniquement la dette publique"],
  ans=1,
  why=["Elle amplifie les fluctuations par définition : c’est le sens du "
       "terme.",
       "Aucun traité n’impose une politique procyclique, même si des règles "
       "budgétaires peuvent y conduire.",
       "La réduction de la dette n’est pas mécanique : une austérité en "
       "récession peut même dégrader le ratio."],
  exp="Le cours précise explicitement qu’une politique procyclique n’est pas "
      "nécessairement inefficace pour tous les objectifs possibles — elle "
      "peut par exemple viser la soutenabilité des finances publiques ou le "
      "respect d’un engagement de change — mais qu’elle est contradictoire "
      "avec l’objectif de stabilisation du cycle économique. Le jugement "
      "dépend donc de l’objectif retenu.",
  diss="Méthode d’évaluation à appliquer : toujours nommer l’objectif avant "
       "de juger une politique efficace ou non."),

# ------------------------------------------------------------- c25-04
f(id='q25-n28', sp='c25-04', niv='appliquer', type='qcm', b=915,
  q="Avec c = 0,8, quel est l’effet sur le revenu national d’une baisse "
    "d’impôts de 50 ?",
  opts=["+ 250",
        "+ 200",
        "− 200",
        "+ 50"],
  ans=1,
  why=["+ 250 correspondrait à l’application de kG = 5, qui vaut pour une "
       "dépense publique directe.",
       "− 200 confond le signe du multiplicateur avec le sens de la "
       "variation : ΔT est négatif.",
       "+ 50 supposerait un multiplicateur unitaire, donc une propension "
       "marginale à consommer nulle."],
  exp="Le multiplicateur fiscal vaut kT = − c/(1 − c) = − 0,8/0,2 = − 4. Avec "
      "ΔT = − 50, on obtient ΔY = − 4 × (− 50) = + 200. La baisse d’impôts "
      "est donc moins efficace, à montant égal, qu’une dépense publique "
      "directe de 50, qui produirait + 250 : la différence tient au point "
      "d’entrée dans le circuit, puisqu’une partie du revenu disponible "
      "supplémentaire est épargnée avant la première vague de demande.",
  diss="Hiérarchie à justifier, pas seulement à retenir : kG > kF > |kT|, "
       "parce que la dépense publique est directement de la demande."),

f(id='q25-n29', sp='c25-04', niv='raisonner', type='vf', b=772,
  q="Dans l’analyse keynésienne, une épargne préalable est nécessaire pour "
    "financer l’investissement.",
  ans=False,
  exp="La causalité est inversée par rapport à l’analyse classique : c’est "
      "l’investissement qui engendre l’épargne correspondante, par "
      "l’intermédiaire du revenu. Le calcul du cours le vérifie : avec une "
      "propension marginale à épargner de 0,2 et un revenu supplémentaire de "
      "500, l’épargne supplémentaire atteint exactement 100, soit "
      "l’investissement initial. L’égalité I = S est donc un résultat ex "
      "post, et non une contrainte de financement préalable.",
  diss="Nuance de rigueur : l’égalité comptable ex post ne signifie pas que "
       "les décisions d’épargne et d’investissement étaient coordonnées ex "
       "ante."),

# ------------------------------------------------------------- c25-01
f(id='q25-n30', sp='c25-01', niv='appliquer', type='assoc', b=187,
  q="Associez chaque approche du PIB à ce qu’elle mesure.",
  ans=[["La somme des valeurs ajoutées créées par les unités résidentes",
        "Approche par la production"],
       ["La somme des emplois de la production : consommation, "
        "investissement, dépenses publiques, exportations nettes",
        "Approche par la demande"],
       ["La somme des revenus distribués lors de la répartition primaire",
        "Approche par les revenus"]],
  exp="Les trois approches conduisent au même PIB, aux ajustements "
      "statistiques près : c’est ce qui garantit la cohérence du cadre "
      "comptable et permet de passer d’une lecture à l’autre. En économie "
      "ouverte, l’équilibre emplois-ressources s’écrit PIB + M = C + I + G + "
      "X, soit PIB = C + I + G + X − M.",
  diss="Usage analytique : l’approche par la demande est celle qui permet de "
       "construire la courbe IS, l’approche par les revenus celle qui ouvre "
       "la question du partage de la valeur ajoutée."),

# ------------------------------------------------------------- c25-06
f(id='q25-n31', sp='c25-06', niv='appliquer', type='ordre', b=1221,
  q="Remettez dans l’ordre l’effet balançoire entre taux d’intérêt et prix "
    "des obligations.",
  ans=["Le taux d’intérêt du marché augmente",
       "Les obligations nouvellement émises offrent un meilleur rendement",
       "Les anciennes obligations, dont le coupon est fixe, deviennent moins "
       "attractives",
       "Elles ne peuvent être vendues qu’à un prix plus faible",
       "Le prix des obligations existantes diminue, ce qui élève leur "
       "rendement de marché"],
  exp="Trois notions doivent être soigneusement distinguées : le coupon, "
      "fixé à l’émission et invariable ; le prix de marché, qui varie en sens "
      "inverse du taux ; et le rendement de marché, qui résulte du rapport "
      "entre les deux. C’est ce mécanisme qui fonde la demande spéculative de "
      "monnaie : si un taux jugé anormalement bas fait anticiper sa "
      "remontée, détenir des obligations expose à une perte en capital, et "
      "les agents préfèrent la liquidité.",
  diss="Mécanisme indispensable pour comprendre la trappe à liquidité, qui "
       "n’est rien d’autre que la généralisation de cette anticipation."),

f(id='q25-n32', sp='c25-06', niv='raisonner', type='courte', b=1148,
  q="En quoi la préférence pour la liquidité rompt-elle avec l’analyse "
    "classique du taux d’intérêt ?",
  ans={'modele': "Dans l’analyse classique, la dichotomie sépare sphère "
       "réelle et sphère monétaire : le taux d’intérêt se détermine sur le "
       "marché des fonds prêtables, où il équilibre l’offre d’épargne et la "
       "demande de financement, la monnaie n’étant qu’un instrument de "
       "transaction. Chez Keynes, le taux d’intérêt se détermine sur le "
       "marché monétaire, par la confrontation entre l’offre de monnaie et la "
       "demande de monnaie. Celle-ci comprend trois motifs : la transaction "
       "et la précaution, qui dépendent positivement du revenu, et la "
       "spéculation, qui dépend négativement du taux d’intérêt. Le taux "
       "d’intérêt devient donc le prix de la renonciation à la liquidité, et "
       "non la rémunération d’une épargne préalable. La conséquence est "
       "décisive : la monnaie devient active, puisqu’elle influence le taux "
       "d’intérêt, donc l’investissement, donc la production. C’est ce qui "
       "rend possible une politique monétaire, et c’est ce qui justifie "
       "l’articulation des deux courbes du modèle IS-LM.",
       'cles': [{'f': ['dichotomie', 'classique', 'fonds pretables',
                       'sphere'],
                 'l': "l'analyse classique : le marché des fonds prêtables"},
                {'f': ['epargne', 'investissement', 'equilibre'],
                 'l': "le taux y équilibre épargne et investissement"},
                {'f': ['marche monetaire', 'offre et demande de monnaie'],
                 'l': "chez Keynes, le taux se forme sur le marché monétaire"},
                {'f': ['transaction', 'precaution', 'speculation', 'motif'],
                 'l': "les trois motifs de détention de monnaie"},
                {'f': ['renonciation', 'liquidite', 'prix'],
                 'l': "le taux devient le prix de la renonciation à la liquidité"},
                {'f': ['monnaie active', 'active', 'influence',
                       'politique monetaire'],
                 'l': "la monnaie devient active"}]},
  exp="C’est la rupture avec l’analyse classique : le taux d’intérêt "
      "n’équilibre plus l’épargne et l’investissement, il devient le prix de "
      "la renonciation à la liquidité.",
  diss="Conséquence à exploiter : rendre la monnaie active est la condition "
       "même de l’existence d’une politique monétaire."),

# ------------------------------------------------------------- c25-03
f(id='q25-n33', sp='c25-03', niv='appliquer', type='qcm', b=519,
  q="Avec C₀ = 200, I₀ = 100 et c = 0,75, quel est le revenu national "
    "d’équilibre ?",
  opts=["1 200",
        "900",
        "400",
        "225"],
  ans=0,
  why=["900 correspondrait à un multiplicateur de 3, donc à c = 2/3.",
       "400 correspondrait à un multiplicateur proche de 1,33.",
       "225 appliquerait la propension à consommer à la demande autonome au "
       "lieu du multiplicateur."],
  exp="On applique Yₑ = (C₀ + I₀)/(1 − c) = 300/0,25 = 1 200. Le "
      "multiplicateur vaut ici 4, puisque la propension marginale à épargner "
      "est de 0,25. On vérifie la cohérence : la consommation d’équilibre "
      "vaut 200 + 0,75 × 1 200 = 1 100, à laquelle s’ajoute un "
      "investissement de 100, soit bien 1 200.",
  diss="Réflexe de vérification toujours payant : recalculer la demande "
       "globale au revenu d’équilibre trouvé."),

f(id='q25-n34', sp='c25-03', niv='raisonner', type='vf', b=547,
  q="Chez Keynes, l’économie peut connaître un équilibre durable "
    "accompagné d’un chômage important.",
  ans=True,
  exp="C’est l’apport décisif de la Théorie générale : la production peut "
      "être exactement égale à la demande globale — donc l’économie est bien "
      "à l’équilibre — tout en demeurant insuffisante pour employer "
      "l’ensemble de la main-d’œuvre disponible. On parle d’équilibre de "
      "sous-emploi. Rien ne garantit donc que les mécanismes de marché "
      "ramènent spontanément l’économie au plein emploi, ce qui justifie une "
      "intervention sur la demande globale.",
  diss="Opposition à poser nettement : chez Pigou le chômage est un "
       "déséquilibre à résorber par les prix, chez Keynes un équilibre à "
       "déplacer par la demande."),

# ------------------------------------------------------------- c25-07
f(id='q25-n35', sp='c25-07', niv='appliquer', type='assoc', b=1418,
  q="Associez chaque zone de la courbe LM à ses conséquences de politique "
    "économique.",
  ans=[["Zone keynésienne : LM horizontale, la demande spéculative de monnaie "
        "est très élevée",
        "Politique budgétaire très efficace, monétaire peu efficace"],
       ["Zone intermédiaire : LM croissante",
        "Les deux politiques ont un effet, l'éviction est partielle"],
       ["Zone classique : LM verticale, la demande spéculative est "
        "négligeable",
        "Politique budgétaire sans effet sur le revenu, éviction totale"]],
  exp="La pente de LM détermine l’ampleur de l’effet d’éviction. En zone "
      "keynésienne — la trappe à liquidité — une relance déplace IS sans "
      "élever le taux d’intérêt : il n’y a pas d’éviction. En zone classique, "
      "le revenu compatible avec l’équilibre monétaire est fixé : une relance "
      "n’élève que le taux d’intérêt, et l’investissement privé recule "
      "exactement autant que la dépense publique augmente.",
  diss="Enseignement général : le même modèle produit des recommandations "
       "opposées selon la zone, ce qui interdit toute conclusion universelle "
       "sur l’efficacité des politiques."),

f(id='q25-n36', sp='c25-07', niv='raisonner', type='qcm', b=1506,
  q="Quels éléments déterminent l’ampleur de l’effet d’éviction ?",
  opts=["Le seul niveau de la dette publique",
        "La pente de LM et la sensibilité de l’investissement privé au taux "
        "d’intérêt",
        "Le niveau général des prix",
        "Le taux de change"],
  ans=1,
  why=["Le niveau de la dette peut influencer les taux par d’autres canaux, "
       "mais il n’intervient pas dans ce mécanisme.",
       "Le niveau général des prix est supposé fixe dans le modèle IS-LM "
       "traditionnel.",
       "Le taux de change n’intervient qu’en économie ouverte, où il produit "
       "une éviction d’une autre nature."],
  exp="Deux conditions doivent être réunies pour que l’éviction soit forte : "
      "que la hausse du revenu provoque une forte hausse du taux d’intérêt — "
      "donc une LM très pentue — et que cette hausse de taux réduise "
      "fortement l’investissement — donc une IS très sensible au taux. Si "
      "l’une des deux fait défaut, l’éviction reste limitée.",
  diss="Conséquence paradoxale à exploiter : une relance est d’autant plus "
       "efficace que l’investissement privé est peu sensible au taux "
       "d’intérêt."),

]
