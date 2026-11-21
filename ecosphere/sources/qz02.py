# -*- coding: utf-8 -*-
"""Chapitre 2 — Le financement de l'économie."""

SP = {
 'c2-01': 'Formes et fonctions de la monnaie, monnaie internationale',
 'c2-02': 'Création monétaire, théories de la monnaie et inflation',
 'c2-03': 'Politique monétaire de la BCE : taux directeurs et canaux',
 'c2-04': 'Crise de 2008, politiques non conventionnelles et financement',
 'c2-05': 'Marchés de capitaux, titrisation et risque systémique',
}

DROP = [
 'ch2-qcm-9',   # Palmstruch et la date de 1661 : absents du texte du cours
]


def f(**kw):
    return kw


FIX = {

# ============================================ c2-01 · formes de la monnaie
'ch2-qcm-1': f(niv='connaitre', sp='c2-01',
 exp="La monnaie est l’actif parfaitement liquide qui sert à évaluer les "
     "biens — fonction d’unité de compte — et à éteindre les dettes — "
     "fonction de moyen de paiement. La liquidité est le critère décisif : "
     "elle est transformable en bien sans délai et sans perte de valeur.",
 why=["Un titre de propriété sur des actifs réels est une action, non de la "
      "monnaie.",
      "Un placement de long terme n’est pas liquide : c’est l’inverse de la "
      "monnaie.",
      "La monnaie est émise par la banque centrale et par les banques "
      "commerciales : elle n’est pas exclusivement publique."]),

'ch2-qcm-3': f(niv='connaitre', sp='c2-01',
 exp="La monnaie scripturale est le solde créditeur des comptes à vue : une "
     "écriture qui circule d’un compte à un autre par virement, prélèvement, "
     "chèque ou carte. Dans la zone euro, elle représente 91 % de la monnaie "
     "en circulation.",
 why=["Billets et pièces forment la monnaie fiduciaire.",
      "Les pièces d’or et d’argent relèvent de la monnaie métallique, "
      "aujourd’hui disparue des échanges courants.",
      "Les titres émis par les banques sont des titres de créance "
      "négociables, pas de la monnaie au sens de M1."]),

'ch2-qcm-4': f(niv='connaitre', sp='c2-01',
 exp="91 % de la monnaie en circulation dans la zone euro est scripturale. "
     "Le cours précise la hiérarchie des usages : virements et prélèvements "
     "concentrent près de 97 % des montants échangés, pour seulement 37 % "
     "du nombre d’opérations ; les paiements par téléphone atteignent 15 % "
     "des paiements.",
 why=["50 % correspondrait à une économie encore largement fiduciaire.",
      "70 % sous-estime nettement la dématérialisation constatée.",
      "80 % reste en deçà du chiffre relevé par le cours."]),

'ch2-qcm-5': f(niv='comprendre', sp='c2-01',
 exp="La monnaie scripturale est la somme inscrite au compte ; le chèque, la "
     "carte ou le virement n’en sont que les supports de circulation. "
     "Confondre les deux conduit à croire qu’une carte « contient » de la "
     "monnaie, alors qu’elle n’est qu’un ordre de transfert.",
 why=["Les deux notions ne se confondent pas : l’une est un avoir, l’autre "
      "un instrument.",
      "Le support n’a pas de liquidité propre : il donne accès à l’avoir.",
      "Ni la monnaie scripturale ni ses supports ne sont réservés à une "
      "catégorie d’agents."]),

'ch2-qcm-6': f(niv='connaitre', sp='c2-01',
 exp="La masse monétaire est la quantité totale de monnaie en circulation "
     "dans une économie à un instant donné. Elle se mesure par des agrégats "
     "emboîtés classés du plus liquide au moins liquide : M1, M2, M3.",
 why=["Les dépenses publiques sont un flux budgétaire, non un stock de "
      "monnaie.",
      "La capitalisation boursière mesure la valeur des actions, qui ne sont "
      "pas de la monnaie.",
      "L’encours de crédit est à l’origine de la monnaie, mais ne se "
      "confond pas avec elle."]),

'ch2-qcm-7': f(niv='connaitre', sp='c2-01',
 exp="M1 regroupe la monnaie immédiatement disponible : billets, pièces et "
     "dépôts à vue. M2 y ajoute l’épargne courte — livrets, dépôts à terme ; "
     "M3 ajoute les placements monétaires. Les agrégats sont emboîtés : "
     "chacun contient le précédent.",
 why=["M0, ou base monétaire, désigne la monnaie centrale, détenue par les "
      "banques auprès de la banque centrale.",
      "M2 ajoute l’épargne courte à M1.",
      "M3 est l’agrégat large, qui ajoute les placements monétaires."]),

'ch2-qcm-10': f(niv='connaitre', sp='c2-01',
 exp="Krugman distingue, du point de vue du secteur privé, trois fonctions "
     "internationales : monnaie de libellé, qui sert à facturer ; monnaie "
     "véhiculaire, qui sert d’intermédiaire entre deux devises peu "
     "échangées ; monnaie d’investissement, qui sert de support de "
     "placement. Le secteur public y ajoute l’ancrage, l’intervention et la "
     "réserve.",
 why=["Ancrage, intervention et réserve sont les fonctions du point de vue "
      "des autorités publiques, non du secteur privé.",
      "Paiement, épargne et spéculation ne sont pas la typologie du cours.",
      "Fiduciaire et scripturale désignent des formes de monnaie, pas des "
      "fonctions internationales."],
 diss="La grille de Krugman permet d’analyser proprement la position du "
      "dollar : il cumule les six fonctions, ce qu’aucune autre monnaie ne "
      "fait, et c’est de ce cumul que vient sa position centrale."),

'ch2-qcm-11': f(niv='comprendre', sp='c2-01', b=113,
 q="Dans quelle monnaie les banques centrales détiennent-elles "
   "majoritairement leurs réserves officielles ?",
 opts=["En euros, du fait du poids du commerce européen",
       "En dollars américains",
       "En or, qui reste l’actif de réserve dominant",
       "En droits de tirage spéciaux émis par le FMI"],
 ans=1,
 exp="Le cours est explicite : les réserves mondiales sont encore aujourd’hui "
     "majoritairement détenues en dollars américains. La fonction de réserve "
     "suppose une monnaie de confiance, qui conserve sa valeur dans le "
     "temps, et des marchés profonds où l’on peut placer et mobiliser ces "
     "avoirs rapidement.",
 why=["L’euro est une monnaie de réserve importante, mais vient loin "
      "derrière le dollar.",
      "L’or reste un actif de réserve, mais il n’est plus l’actif dominant "
      "des réserves officielles.",
      "Les droits de tirage spéciaux ne forment qu’une fraction marginale "
      "des réserves."],
 diss="À relier au triangle de Mundell et aux chapitres de deuxième année : "
      "la domination du dollar donne aux États-Unis une capacité "
      "d’endettement extérieur que n’a aucun autre pays."),

'ch2-qcm-12': f(niv='connaitre', sp='c2-01',
 exp="Le triangle de Mundell énonce l’incompatibilité de trois objectifs : "
     "libre circulation des capitaux, autonomie de la politique monétaire et "
     "stabilité du taux de change. Il faut en abandonner un : la zone euro a "
     "renoncé à l’autonomie monétaire nationale, la Chine a longtemps "
     "contrôlé ses capitaux.",
 why=["Les fonctions de la monnaie internationale sont une autre typologie, "
      "celle de Krugman.",
      "M1, M2 et M3 sont des agrégats de mesure de la masse monétaire.",
      "Les objectifs de la BCE relèvent de son mandat, non du triangle."],
 diss="Le triangle est la clé de lecture de tout sujet sur l’autonomie "
      "monétaire en économie ouverte, et il est repris en deuxième année "
      "pour analyser l’histoire des régimes de change."),

'ch2-qcm-13': f(niv='connaitre', sp='c2-01',
 exp="La dépréciation est la baisse du cours d’une monnaie résultant du jeu "
     "de l’offre et de la demande sur le marché des changes. Elle est subie "
     "et continue, à la différence de la dévaluation, qui est une décision "
     "des autorités en régime de change fixe.",
 why=["Une décision politique de baisser la parité est précisément une "
      "dévaluation.",
      "La hausse d’un taux directeur est un acte de politique monétaire, qui "
      "peut au contraire soutenir la monnaie.",
      "Le retrait de billets modifie la composition de la masse monétaire, "
      "pas le cours de change."]),

'ch2-qcm-14': f(niv='comprendre', sp='c2-01',
 exp="La distinction tient au régime de change : en change flottant, la "
     "valeur résulte du marché et l’on parle de dépréciation ou "
     "d’appréciation ; en change fixe, la parité est un engagement "
     "institutionnel, et sa modification est une dévaluation ou une "
     "réévaluation, donc une décision.",
 why=["La différence est précisément celle du régime de change.",
      "Les deux termes ne sont pas attachés à une monnaie particulière.",
      "Aucune des deux n’est bénéfique ou néfaste par nature : tout dépend "
      "des élasticités et de la structure de l’économie."]),

'ch2-qcm-15': f(niv='connaitre', sp='c2-01',
 exp="Le Bitcoin est créé en 2008 sous le pseudonyme de Satoshi Nakamoto. "
     "Son émission est plafonnée à 21 millions d’unités et repose sur une "
     "chaîne de blocs, registre décentralisé validé par les utilisateurs "
     "sans autorité centrale.",
 why=["Zuckerberg a fondé Facebook en 2004 : aucun rapport.",
      "Musk a contribué à la notoriété de certaines cryptomonnaies, il n’en "
      "est pas le créateur.",
      "La BCE n’émet pas de cryptoactif : elle étudie un euro numérique, qui "
      "en est l’opposé institutionnel."]),

'ch2-qcm-16': f(niv='connaitre', sp='c2-01',
 exp="L’émission est plafonnée à 21 millions d’unités. Ce plafond est "
     "présenté comme une garantie contre l’inflation, mais c’est aussi la "
     "source de la volatilité : l’offre étant rigide, tout choc de demande "
     "se reporte intégralement sur le prix.",
 why=["10 millions ne correspond pas au protocole.",
      "15 millions non plus.",
      "100 millions contredirait la rareté programmée qui fonde l’actif."]),

'ch2-qcm-18': f(niv='connaitre', sp='c2-01',
 exp="La chaîne de blocs est un registre numérique décentralisé : chaque "
     "transaction est enregistrée dans un bloc, validé par les utilisateurs "
     "du réseau, puis chaîné aux précédents. La confiance ne repose plus sur "
     "une institution mais sur un protocole et sur le coût de la validation.",
 why=["Une banque centrale numérique est une monnaie publique : c’est "
      "l’inverse de la décentralisation.",
      "Le contrôle par les banques commerciales contredit le principe même "
      "du dispositif.",
      "Ce n’est pas un agrégat monétaire."]),

'ch2-qcm-20': f(niv='comprendre', sp='c2-01',
 exp="« Les crédits font les dépôts » signifie que la banque crée la monnaie "
     "par un simple jeu d’écritures lorsqu’elle accorde un crédit : elle "
     "inscrit la créance à son actif et le dépôt au passif. Le dépôt est "
     "donc la conséquence du crédit et non sa condition préalable.",
 why=["C’est la thèse inverse, celle de l’intermédiation pure, que le cours "
      "écarte.",
      "L’égalité comptable entre crédits et dépôts dans une banque donnée "
      "n’est pas vérifiée : les fuites existent.",
      "Prêter uniquement les dépôts reçus décrirait un simple intermédiaire, "
      "non une banque créatrice de monnaie."],
 diss="Ce renversement commande toute l’analyse de la politique monétaire : "
      "si les crédits font les dépôts, la banque centrale ne pilote pas la "
      "quantité de monnaie mais son prix, le taux d’intérêt."),

'ch2-qcm-42': f(niv='connaitre', sp='c2-01',
 exp="L’euro entre en vigueur en 1999 et l’Eurosystème — la BCE et les "
     "banques centrales nationales de la zone — est mis en place à cette "
     "date. Les billets et pièces ne circulent qu’à partir de 2002 : la "
     "monnaie unique existe donc trois ans avant sa forme fiduciaire.",
 why=["1992 est l’année du traité de Maastricht, qui organise la marche vers "
      "l’union monétaire.",
      "1995 ne correspond à aucune étape décisive de l’Eurosystème.",
      "2002 est la date de mise en circulation des billets et des pièces."]),

'ch2-vf-1': f(niv='connaitre', sp='c2-01',
 exp="La monnaie fiduciaire — billets et pièces — tire précisément son nom "
     "de la confiance (fides) accordée à son émetteur : sa valeur faciale "
     "est sans rapport avec sa valeur intrinsèque. C’est la monnaie "
     "métallique qui reposait sur la valeur du métal contenu."),

'ch2-vf-2': f(niv='appliquer', sp='c2-01',
 exp="Le cours donne les deux proportions : virements et prélèvements "
     "représentent près de 97 % des montants échangés mais seulement 37 % "
     "des opérations. L’écart s’explique par la nature des flux : salaires, "
     "loyers et règlements entre entreprises portent sur de gros montants, "
     "les paiements par carte sur des montants unitaires faibles."),

'ch2-vf-3': f(niv='comprendre', sp='c2-01',
 exp="Le Bitcoin ne remplit aucune des trois fonctions de façon "
     "satisfaisante : il n’est unité de compte nulle part, son usage comme "
     "moyen d’échange reste marginal, et sa volatilité le disqualifie comme "
     "réserve de valeur stable. C’est pourquoi le cours lui refuse le statut "
     "de monnaie."),

'ch2-vf-4': f(niv='comprendre', sp='c2-01',
 exp="C’est l’inverse : la banque crée la monnaie en accordant le crédit, et "
     "le dépôt naît de cette création. Les dépôts préalables ne sont pas la "
     "condition du crédit ; ce qui limite la banque, c’est le besoin de "
     "monnaie centrale pour faire face aux fuites — billets, règlements "
     "interbancaires, réserves obligatoires."),

'ch2-open-1': f(niv='connaitre', sp='c2-01',
 ans={'modele': "Un agent à besoin de financement est un agent dont les "
      "dépenses d’investissement excèdent l’épargne qu’il dégage : il doit "
      "donc se procurer des ressources auprès d’autres agents, par le crédit "
      "bancaire ou par l’émission de titres. Les sociétés non financières en "
      "sont l’exemple type ; les administrations publiques en déficit "
      "également.",
      'cles': [{'f': ['investissement', 'depense'], 'l': 'ses dépenses excèdent ses ressources propres'},
               {'f': ['epargne', 'épargne', 'ressources propres'],
                'l': 'son épargne est insuffisante'},
               {'f': ['entreprise', 'snf', 'societe', 'administration'],
                'l': 'les entreprises en sont l’exemple type'}]},
 exp="La symétrie importe : à tout besoin de financement correspond une "
     "capacité de financement, le plus souvent celle des ménages. C’est "
     "cette confrontation qu’organisent les banques et les marchés."),

'ch2-open-7': f(niv='connaitre', sp='c2-01',
 ans={'modele': "L’action est un titre de propriété sur une fraction du "
      "capital d’une société. Elle donne droit à un revenu variable, le "
      "dividende, versé selon les résultats, et à un droit de vote en "
      "assemblée générale. Son détenteur est associé au risque : il n’est "
      "remboursé qu’après tous les créanciers.",
      'cles': [{'f': ['propriete', 'propriété', 'capital'],
                'l': 'c’est un titre de propriété'},
               {'f': ['dividende'], 'l': 'elle donne droit à un dividende variable'},
               {'f': ['vote', 'assemblee'], 'l': 'et à un droit de vote'}]},
 exp="L’opposition action / obligation est celle du risque : revenu variable "
     "et propriété d’un côté, revenu fixe et créance de l’autre."),

'ch2-open-8': f(niv='comprendre', sp='c2-01',
 ans={'modele': "L’obligation est un titre de créance : son détenteur a "
      "prêté et perçoit un intérêt, le coupon, généralement fixe, avec "
      "remboursement du principal à l’échéance. L’actionnaire, lui, est "
      "propriétaire : son revenu est variable et il n’est remboursé qu’en "
      "dernier. L’obligataire court donc un risque plus faible et perçoit un "
      "revenu plus régulier.",
      'cles': [{'f': ['creance', 'créance', 'pret', 'prêt'],
                'l': 'l’obligation est un titre de créance'},
               {'f': ['coupon', 'interet', 'intérêt', 'fixe'],
                'l': 'elle rapporte un intérêt fixe'},
               {'f': ['remboursement', 'echeance', 'échéance'],
                'l': 'elle est remboursée à l’échéance'},
               {'f': ['action', 'proprietaire', 'propriétaire', 'dividende'],
                'l': 'l’action, elle, confère la propriété et un revenu variable'}]},
 exp="Cette différence de rang explique l’écart de rendement exigé : plus le "
     "titre est risqué, plus le rendement demandé est élevé."),

'ch2-open-14': f(niv='comprendre', sp='c2-01',
 ans={'modele': "L’autofinancement consiste à financer l’investissement sur "
      "l’épargne dégagée par l’entreprise, c’est-à-dire ses bénéfices mis en "
      "réserve. Il évite le coût du crédit et préserve l’indépendance vis-à-"
      "vis des banques et des actionnaires. Sa limite est la taille : il "
      "plafonne l’investissement au niveau des profits passés.",
      'cles': [{'f': ['epargne', 'benefice', 'reserve', 'ressources propres'],
                'l': 'il s’appuie sur les bénéfices mis en réserve'},
               {'f': ['independance', 'indépendance', 'sans emprunt'],
                'l': 'il préserve l’indépendance financière'},
               {'f': ['interet', 'intérêt', 'cout', 'coût'],
                'l': 'il évite les frais financiers'}]},
 exp="Le cours relie l’autofinancement au taux de marge : c’est parce que "
     "les marges reconstituent l’épargne de l’entreprise qu’elles "
     "conditionnent sa capacité à investir sans emprunter."),

'ch2-aut195-3': f(niv='raisonner', sp='c2-01',
 exp="Ce qui fonde la promesse — une règle d’émission intangible — est "
     "précisément ce qui empêche d’amortir les chocs de demande : l’offre "
     "étant rigide, tout afflux d’acheteurs se traduit intégralement en "
     "hausse de cours. Une monnaie, au contraire, suppose une offre "
     "élastique, ajustable aux besoins de l’économie.",
 why=["La fixité de l’offre produit au contraire une tendance "
      "déflationniste si la demande de transactions augmente.",
      "Les transactions internationales sont techniquement possibles : ce "
      "n’est pas le problème relevé.",
      "Aucune banque centrale n’est tenue d’intervenir sur un cryptoactif."],
 diss="Argument utile pour montrer qu’une monnaie n’est pas seulement un "
      "instrument d’échange mais un instrument de politique économique : "
      "renoncer à l’élasticité de l’offre, c’est renoncer à la stabilisation."),

# ===================================== c2-02 · création monétaire et théories
'ch2-qcm-2': f(niv='connaitre', sp='c2-02',
 exp="Les trois fonctions, déjà identifiées par Aristote, sont l’unité de "
     "compte, le moyen d’échange et la réserve de valeur. Elles servent de "
     "grille d’évaluation : le cours s’en sert pour refuser au Bitcoin le "
     "statut de monnaie.",
 why=["Investissement, épargne et consommation sont des emplois du revenu.",
      "Paiement, financement et placement décrivent des opérations, non les "
      "fonctions canoniques.",
      "Production, redistribution et régulation sont des fonctions de "
      "l’État."]),

'ch2-qcm-8': f(niv='connaitre', sp='c2-02',
 exp="M3 est l’agrégat large suivi par la BCE : il ajoute à M2 les "
     "placements monétaires de court terme. C’est l’indicateur le plus "
     "complet de la monnaie au sens large, celui que la banque centrale "
     "surveille pour apprécier la dynamique monétaire.",
 why=["M0 est la monnaie centrale, qui ne circule qu’entre banques et banque "
      "centrale.",
      "M1 ne couvre que la monnaie immédiatement disponible.",
      "M2 s’arrête à l’épargne courte."]),

'ch2-qcm-17': f(niv='comprendre', sp='c2-02',
 exp="Le Bitcoin échoue aux trois fonctions : il n’est unité de compte nulle "
     "part — les prix ne sont pas affichés en bitcoins —, son usage comme "
     "moyen d’échange reste marginal, et sa volatilité ruine la fonction de "
     "réserve de valeur. Le cours en conclut qu’il s’agit d’un actif "
     "spéculatif plutôt que d’une monnaie.",
 why=["Le coût de production, lié au minage, est une critique "
      "environnementale, pas monétaire.",
      "La légalité n’est pas le critère retenu : un actif légal peut ne pas "
      "être une monnaie.",
      "Le Bitcoin n’est contrôlé par aucune banque centrale : c’est son "
      "principe même."]),

'ch2-qcm-19': f(niv='comprendre', sp='c2-02',
 exp="La création ex nihilo désigne l’inscription simultanée d’une créance à "
     "l’actif et d’un dépôt au passif de la banque, au moment de l’octroi du "
     "crédit. Rien n’est prélevé sur une épargne préalable : la monnaie naît "
     "de l’opération et disparaîtra lors du remboursement.",
 why=["Les billets sont émis par la banque centrale, non par les banques "
      "commerciales.",
      "L’émission d’obligations par l’État mobilise une épargne existante, "
      "elle ne crée pas de monnaie.",
      "La distribution directe aux ménages est l’hélicoptère monétaire, cas "
      "théorique distinct."]),

'ch2-qcm-21': f(niv='appliquer', sp='c2-02',
 exp="Le multiplicateur de crédit vaut l’inverse du taux de fuite : avec un "
     "taux de retrait en billets de 20 %, une base de 100 en monnaie "
     "centrale peut soutenir 500 de masse monétaire. Le modèle suppose que "
     "la banque centrale contrôle la base et que les banques prêtent autant "
     "que la contrainte le permet.",
 why=["1 → 2 correspondrait à un taux de fuite de 50 %.",
      "1 → 3 correspondrait à un taux de fuite d’environ 33 %.",
      "100 → 200 correspondrait également à un taux de fuite de 50 %."],
 diss="Le multiplicateur est à présenter comme un modèle, non comme une "
      "description : le diviseur de crédit en propose la lecture inverse, et "
      "c’est cette seconde lecture que valide la pratique des banques "
      "centrales contemporaines."),

'ch2-qcm-22': f(niv='raisonner', sp='c2-02',
 exp="Les deux schémas inversent la causalité. Pour le multiplicateur "
     "(lecture monétariste), la banque centrale fixe la base monétaire, qui "
     "détermine la masse monétaire : la monnaie est exogène. Pour le "
     "diviseur (lecture keynésienne), c’est la demande de crédit des agents "
     "qui crée la monnaie, la banque centrale refinançant ensuite les "
     "banques : la monnaie est endogène.",
 why=["Ce ne sont pas deux noms d’un même mécanisme : la causalité est "
      "inversée.",
      "Le diviseur n’est pas un cas particulier de crise : c’est une analyse "
      "générale.",
      "La distinction ne tient pas au statut public ou privé des banques."],
 diss="Opposition centrale pour un sujet sur l’efficacité de la politique "
      "monétaire : si la monnaie est endogène, agir sur la quantité est "
      "illusoire et seul le prix du crédit compte."),

'ch2-qcm-23': f(niv='connaitre', sp='c2-02',
 exp="La Currency School, dont Ricardo est la figure, défend une couverture "
     "stricte de l’émission de billets par l’encaisse métallique : la "
     "monnaie doit être une marchandise contrainte. La Banking School, avec "
     "Tooke et Thornton, soutient au contraire que l’émission doit suivre "
     "les besoins du commerce.",
 why=["Tooke et Thornton défendent précisément la position inverse.",
      "L’école keynésienne est postérieure d’un siècle.",
      "L’institutionnalisme ne traite pas de cette controverse."],
 diss="Ce débat du XIXᵉ siècle préfigure l’opposition monétarisme / "
      "keynésianisme : règle contre discrétion, monnaie exogène contre "
      "monnaie endogène."),

'ch2-qcm-24': f(niv='connaitre', sp='c2-02',
 exp="L’équation des échanges de Fisher s’écrit MV = PT. Avec V, la vitesse "
     "de circulation, et T, le volume des transactions, supposés stables, "
     "une hausse de M se répercute proportionnellement sur P. La monnaie "
     "n’agit que sur les prix, jamais sur la production : c’est la thèse de "
     "la neutralité, « la monnaie est un voile ».",
 why=["Dire que la monnaie crée de la richesse réelle est exactement la "
      "thèse que Fisher récuse.",
      "La vitesse de circulation est supposée stable : elle n’est pas le "
      "moteur de la croissance.",
      "Le lien monnaie-investissement relève d’une analyse keynésienne."]),

'ch2-qcm-25': f(niv='connaitre', sp='c2-02',
 exp="La formule de Friedman — « l’inflation est toujours et partout un "
     "phénomène monétaire » — signifie qu’une inflation durable suppose une "
     "croissance de la quantité de monnaie supérieure à celle de la "
     "production. Un choc ponctuel peut élever les prix une fois ; seule la "
     "création monétaire entretient le mouvement.",
 why=["La demande des ménages peut provoquer une tension ponctuelle, non une "
      "inflation durable au sens de Friedman.",
      "Les inégalités de revenus ne figurent pas dans son analyse de "
      "l’inflation.",
      "Friedman ne voit dans l’inflation aucune régulation naturelle : il y "
      "voit une erreur de politique monétaire."]),

'ch2-qcm-26': f(niv='connaitre', sp='c2-02',
 exp="La courbe de Phillips décrit une relation inverse entre chômage et "
     "progression des salaires nominaux, reformulée ensuite en arbitrage "
     "entre chômage et inflation. Le cours précise que la relation observée "
     "par Phillips n’est « ni linéaire, ni stable » et qu’elle fait "
     "apparaître le NAWRU, taux de chômage auquel les salaires nominaux "
     "n’augmentent plus.",
 why=["La relation croissance-investissement est l’accélérateur.",
      "La relation monnaie-prix est la théorie quantitative.",
      "La relation taux d’intérêt-demande de crédit relève du canal des "
      "taux."]),

'ch2-qcm-27': f(niv='raisonner', sp='c2-02',
 exp="Les chocs pétroliers produisent simultanément une inflation élevée et "
     "un chômage élevé : la stagflation. Or l’arbitrage supposait qu’on ne "
     "pouvait pas avoir les deux maux à la fois. La relation est donc "
     "démentie, ce qui ouvre la voie à l’analyse de Friedman en termes "
     "d’anticipations et de chômage naturel.",
 why=["La présence des syndicats n’est pas la variable explicative retenue.",
      "L’inflation n’a pas été supprimée : elle a au contraire atteint des "
      "sommets.",
      "La mondialisation n’est pas le facteur invoqué pour les années 1970."],
 diss="C’est l’exemple canonique d’une régularité empirique invalidée par un "
      "changement de régime : à mobiliser dans tout sujet sur le statut des "
      "lois en économie."),

'ch2-qcm-28': f(niv='connaitre', sp='c2-02',
 exp="La stagflation est la coexistence d’une activité stagnante, avec un "
     "chômage élevé, et d’une inflation forte. Elle est caractéristique des "
     "années 1970 et résulte d’un choc d’offre : la hausse du prix du "
     "pétrole élève les coûts et comprime simultanément l’activité.",
 why=["Forte croissance et inflation décrivent une surchauffe, non une "
      "stagflation.",
      "Déflation et croissance forte forment une configuration opposée.",
      "Des taux bas avec chômage élevé décrivent une trappe à liquidité, "
      "sans inflation."]),

'ch2-qcm-33': f(niv='connaitre', sp='c2-02',
 exp="L’hélicoptère monétaire, évoqué par Friedman, consiste à créer de la "
     "monnaie et à la distribuer directement aux ménages ou à l’État, sans "
     "passer par le crédit bancaire. L’idée surgit lorsque la politique "
     "monétaire conventionnelle — baisse des taux, open market, "
     "assouplissement quantitatif — se heurte à son inefficacité.",
 why=["Le transport de billets n’a évidemment rien à voir.",
      "Le rachat de dettes publiques est l’assouplissement quantitatif, qui "
      "passe par les marchés.",
      "L’émission de cryptomonnaie par une banque centrale est la monnaie "
      "numérique de banque centrale."]),

'ch2-vf-5': f(niv='connaitre', sp='c2-02',
 exp="C’est la Banking School, avec Tooke et Thornton, qui défend une "
     "émission suivant les besoins du commerce. La Currency School, autour "
     "de Ricardo, exige au contraire une couverture stricte des billets par "
     "l’encaisse métallique."),

'ch2-vf-6': f(niv='comprendre', sp='c2-02',
 exp="C’est bien ce que l’équation MV = PT implique sous les hypothèses "
     "retenues : V et T étant supposés stables, toute variation de M se "
     "reporte proportionnellement sur P. L’identité comptable devient une "
     "théorie précisément par ces hypothèses, que les keynésiens contestent "
     "en soutenant que V varie et que T dépend de la demande."),

'ch2-vf-7': f(niv='comprendre', sp='c2-02',
 exp="Friedman soutient l’inefficacité à long terme : une relance monétaire "
     "peut réduire temporairement le chômage, mais les agents révisent leurs "
     "anticipations d’inflation, les salaires réels se rétablissent et le "
     "chômage revient à son niveau naturel. Seules des réformes "
     "structurelles peuvent abaisser ce dernier."),

'ch2-vf-8': f(niv='comprendre', sp='c2-02',
 exp="La stagflation dément la courbe de Phillips : inflation et chômage "
     "élevés coexistent, alors que la relation supposait qu’ils varient en "
     "sens inverse. C’est cette invalidation empirique qui ouvre la voie à "
     "la critique monétariste."),

'ch2-vf-9': f(niv='comprendre', sp='c2-02',
 exp="La trappe à liquidité désigne la situation où le taux d’intérêt est si "
     "bas que la demande de monnaie devient insensible à ses variations : "
     "les agents conservent les liquidités au lieu d’acheter des titres. La "
     "politique monétaire conventionnelle perd alors sa prise, ce qui "
     "justifie les instruments non conventionnels et la politique "
     "budgétaire."),

'ch2-vf-11': f(niv='comprendre', sp='c2-02',
 exp="L’hélicoptère monétaire reste une référence théorique : il n’a pas été "
     "mis en œuvre comme instrument régulier. Il poserait deux difficultés "
     "majeures — le risque inflationniste et la confusion entre politique "
     "monétaire et politique budgétaire, qui menacerait l’indépendance de la "
     "banque centrale."),

'ch2-open-5': f(niv='connaitre', sp='c2-02',
 ans={'modele': "La banque commerciale collecte des dépôts, accorde des "
      "crédits et gère les moyens de paiement. Sa fonction propre est la "
      "création monétaire : en accordant un crédit, elle inscrit "
      "simultanément une créance à son actif et un dépôt au passif. Elle "
      "assure aussi la transformation des échéances, en finançant des "
      "emplois longs par des ressources courtes.",
      'cles': [{'f': ['depot', 'dépôt'], 'l': 'elle collecte des dépôts'},
               {'f': ['credit', 'crédit'], 'l': 'elle accorde des crédits'},
               {'f': ['creation monetaire', 'cree de la monnaie', 'création'],
                'l': 'elle crée de la monnaie par le crédit'}]},
 exp="C’est ce pouvoir de création qui distingue la banque d’un simple "
     "intermédiaire financier et qui justifie sa régulation."),

'ch2-open-6': f(niv='comprendre', sp='c2-02',
 ans={'modele': "La banque centrale est la banque des banques : elle émet la "
      "monnaie centrale, refinance les banques commerciales, pilote les taux "
      "directeurs pour assurer la stabilité des prix, supervise le système "
      "bancaire et joue le rôle de prêteur en dernier ressort en cas de "
      "crise de liquidité.",
      'cles': [{'f': ['stabilite des prix', 'inflation'],
                'l': 'elle vise la stabilité des prix'},
               {'f': ['taux directeur', 'refinanc'],
                'l': 'elle refinance les banques et fixe les taux directeurs'},
               {'f': ['preteur en dernier ressort', 'dernier ressort', 'supervis'],
                'l': 'elle est prêteur en dernier ressort et superviseur'}]},
 exp="Le prêteur en dernier ressort est la fonction la moins visible et la "
     "plus décisive : c’est elle qui empêche qu’une crise de liquidité se "
     "transforme en faillite en chaîne."),

'ch2-open-9': f(niv='comprendre', sp='c2-02',
 ans={'modele': "Le taux d’intérêt est le prix de la monnaie prêtée. Pour "
      "l’emprunteur, c’est un coût, qui s’ajoute au remboursement du "
      "capital et conditionne la rentabilité du projet financé. Pour le "
      "prêteur, c’est une rémunération : du renoncement à la liquidité "
      "immédiate d’une part, du risque de défaut d’autre part.",
      'cles': [{'f': ['cout', 'coût', 'emprunteur'],
                'l': 'c’est un coût pour l’emprunteur'},
               {'f': ['remuneration', 'rémunération', 'preteur'],
                'l': 'c’est une rémunération pour le prêteur'},
               {'f': ['risque', 'liquidite', 'renoncement'],
                'l': 'il rémunère le risque et le renoncement à la liquidité'}]},
 exp="Cette double nature explique pourquoi une baisse des taux soutient "
     "l’investissement mais décourage l’épargne : le même prix joue en sens "
     "inverse selon la position de l’agent."),

'ch2-aut195-1': f(niv='raisonner', sp='c2-02',
 exp="MV = PT est une identité comptable : elle est vraie par construction. "
     "Ce sont deux hypothèses qui en font une théorie : la stabilité de la "
     "vitesse de circulation V, et la détermination du volume des "
     "transactions T par les seuls facteurs réels. Alors seulement la "
     "causalité devient univoque : M → P.",
 why=["Supposer P et M stables reviendrait à figer les deux termes que la "
      "théorie veut relier.",
      "La variabilité de V et de T est précisément l’objection keynésienne : "
      "elle ruine la causalité.",
      "La monnaie scripturale n’entre pas dans la construction de "
      "l’équation."],
 diss="Belle illustration de méthode : une identité n’est jamais une "
      "théorie ; ce sont les hypothèses ajoutées qui font la thèse, et c’est "
      "sur elles que porte la critique."),

'ch2-aut195-2': f(niv='connaitre', sp='c2-02',
 exp="Phillips observe en 1958, sur les données britanniques de 1861 à 1957, "
     "une relation inverse entre le taux de chômage et la croissance des "
     "salaires nominaux. Le cours souligne qu’elle n’est « ni linéaire, ni "
     "stable », et qu’elle fait apparaître le NAWRU, taux de chômage pour "
     "lequel la progression des salaires nominaux est nulle.",
 why=["La relation porte sur le chômage et les salaires, non sur l’inflation "
      "et la croissance.",
      "Phillips ne traite pas du lien monnaie-prix.",
      "Le déficit public n’intervient pas dans son étude."]),

# ==================================== c2-03 · politique monétaire de la BCE
'ch2-qcm-29': f(niv='connaitre', sp='c2-03',
 exp="La BCE vise une inflation de 2 % à moyen terme. La cible n’est ni "
     "nulle ni inférieure à 2 % : une inflation légèrement positive "
     "éloigne du risque de déflation et laisse une marge de baisse des taux "
     "réels en cas de récession.",
 why=["Une cible d’inflation nulle rapprocherait dangereusement du risque "
      "déflationniste.",
      "Une cible inférieure à 1 % laisserait trop peu de marge de manœuvre.",
      "Une cible de 3 à 5 % serait incompatible avec le mandat de stabilité "
      "des prix."]),

'ch2-qcm-32': f(niv='connaitre', sp='c2-03',
 exp="Les trois taux directeurs forment un corridor : le taux de facilité de "
     "dépôt constitue le plancher, le taux de facilité de prêt marginal le "
     "plafond, et le taux de refinancement — crédit à une semaine — se situe "
     "entre les deux. Le corridor encadre le taux du marché interbancaire.",
 why=["Croissance, inflation et chômage sont des objectifs ou des "
      "indicateurs, non des taux directeurs.",
      "Taux nominal, réel et neutre sont des notions d’analyse.",
      "Taux interbancaire, d’escompte et de change ne forment pas le triplet "
      "de la BCE."]),

'ch2-qcm-41': f(niv='comprendre', sp='c2-03',
 exp="La théorie monétaire moderne, qui prolonge les idées d’Abba Lerner "
     "(1943), soutient qu’un État souverain monétairement ne connaît pas de "
     "contrainte financière à sa dépense : il peut toujours émettre la "
     "monnaie dans laquelle il s’endette. La contrainte est réelle et non "
     "financière : c’est l’inflation, qui apparaît lorsque les ressources "
     "productives sont saturées.",
 why=["La TMM confie la monnaie à la puissance publique, non aux marchés.",
      "Elle ne hiérarchise pas les deux politiques de cette façon : elle "
      "subordonne la monnaie à l’objectif d’emploi.",
      "Elle ne repose pas sur l’idée que l’inflation rembourse la dette."],
 diss="À manier avec sa limite institutionnelle : dans la zone euro, la "
      "banque centrale n’a pas le droit de financer directement les États, "
      "ce qui rend la TMM inapplicable en l’état — argument décisif dans un "
      "sujet sur la soutenabilité de la dette."),

'ch2-vf-18': f(niv='comprendre', sp='c2-03',
 exp="C’est bien la thèse de la TMM : pour un État souverain monétairement, "
     "la limite n’est pas le financement mais l’inflation, qui survient "
     "quand la dépense excède les capacités réelles de l’économie. Le cours "
     "rappelle toutefois l’obstacle européen : l’interdiction du financement "
     "monétaire direct des États."),

# ========================= c2-04 · crise de 2008 et financement de l'économie
'ch2-qcm-30': f(niv='connaitre', sp='c2-04',
 exp="Dans la trappe à liquidité, les taux sont déjà au plancher et les "
     "agents préfèrent détenir de la monnaie plutôt que des titres dont ils "
     "anticipent la baisse. L’injection de liquidité ne fait plus baisser "
     "les taux ni repartir le crédit : la politique monétaire "
     "conventionnelle est sans prise.",
 why=["L’accumulation de réserves en or ne décrit pas la trappe.",
      "La thésaurisation face à l’inflation est un autre comportement, lié à "
      "la fuite devant la monnaie.",
      "Une limitation réglementaire des prêts est un instrument "
      "macroprudentiel."]),

'ch2-qcm-31': f(niv='connaitre', sp='c2-04',
 exp="L’assouplissement quantitatif consiste pour la banque centrale à "
     "acheter massivement des titres — publics puis privés — afin "
     "d’injecter des liquidités et de faire baisser les taux longs, que les "
     "taux directeurs n’atteignent pas. C’est un instrument non "
     "conventionnel, né de l’inefficacité des taux au plancher.",
 why=["La hausse des taux directeurs est la politique inverse.",
      "La baisse des réserves obligatoires est un autre instrument, "
      "aujourd’hui peu utilisé.",
      "Le transfert direct aux ménages est l’hélicoptère monétaire."]),

'ch2-qcm-40': f(niv='comprendre', sp='c2-04',
 exp="Hicks oppose l’économie d’endettement, où le financement passe "
     "principalement par le crédit bancaire et où l’intermédiation est "
     "forte, à l’économie de marchés financiers, où les agents se financent "
     "par émission de titres. Le passage de l’une à l’autre caractérise les "
     "transformations engagées depuis les années 1980.",
 why=["La distinction n’oppose pas le public au privé.",
      "Elle ne sépare pas les ménages des entreprises.",
      "Elle ne recouvre pas l’opposition entre pays développés et pays en "
      "développement."]),

'ch2-vf-17': f(niv='raisonner', sp='c2-04',
 exp="Le cours nuance explicitement : les banques restent centrales, mais "
     "elles interviennent elles-mêmes sur les marchés — on parle "
     "d’intermédiation de marché. Le passage à l’économie de marchés "
     "financiers n’est donc pas une disparition des banques mais une "
     "transformation de leur métier."),

'ch2-open-2': f(niv='connaitre', sp='c2-04',
 ans={'modele': "Le financement interne est l’autofinancement : l’agent "
      "mobilise sa propre épargne, c’est-à-dire ses bénéfices mis en "
      "réserve. Le financement externe fait appel à d’autres agents : soit "
      "de façon intermédiée, par le crédit bancaire, soit de façon directe, "
      "par l’émission d’actions ou d’obligations sur les marchés.",
      'cles': [{'f': ['autofinancement', 'interne', 'epargne'],
                'l': 'le financement interne est l’autofinancement'},
               {'f': ['banque', 'credit', 'intermedie'],
                'l': 'le financement externe intermédié passe par les banques'},
               {'f': ['marche', 'marché', 'titre', 'action', 'obligation'],
                'l': 'le financement externe direct passe par les marchés'}]},
 exp="La distinction interne / externe porte sur l’origine des fonds ; la "
     "distinction direct / intermédié porte sur le canal emprunté. Les deux "
     "se combinent."),

'ch2-open-3': f(niv='connaitre', sp='c2-04',
 ans={'modele': "Le financement direct, ou désintermédié, met en relation "
      "immédiate les agents à besoin de financement et les agents à "
      "capacité de financement, sur les marchés de capitaux : l’emprunteur "
      "émet des titres — actions ou obligations — que les prêteurs "
      "souscrivent. Les intermédiaires financiers n’y assurent qu’un rôle de "
      "placement et de conseil.",
      'cles': [{'f': ['marche', 'marché'], 'l': 'il passe par les marchés de capitaux'},
               {'f': ['titre', 'action', 'obligation'],
                'l': 'par l’émission de titres'},
               {'f': ['directement', 'rencontre', 'sans intermediaire'],
                'l': 'sans intermédiation bancaire du risque'}]},
 exp="Dans ce schéma, le risque est porté par le souscripteur du titre, non "
     "par une banque : c’est la différence décisive avec le crédit."),

'ch2-open-4': f(niv='connaitre', sp='c2-04',
 ans={'modele': "Le financement indirect, ou intermédié, passe par une "
      "banque qui s’interpose : elle collecte des ressources et accorde des "
      "crédits en son nom propre, assumant le risque de défaut et la "
      "transformation des échéances. Le prêteur final n’est pas en relation "
      "avec l’emprunteur.",
      'cles': [{'f': ['banque', 'intermediaire'], 'l': 'la banque s’interpose'},
               {'f': ['credit', 'crédit'], 'l': 'elle accorde des crédits'},
               {'f': ['risque', 'transformation', 'echeance'],
                'l': 'elle porte le risque et transforme les échéances'}]},
 exp="C’est l’intermédiation de bilan : la banque porte le risque, "
     "contrairement à l’intermédiation de marché où elle le place."),

# ======================== c2-05 · marchés, titrisation et risque systémique
'ch2-qcm-34': f(niv='connaitre', sp='c2-05',
 exp="Bourguinat résume par trois D la transformation des marchés financiers "
     "depuis les années 1980 : déréglementation — levée des contrôles ; "
     "désintermédiation — financement par les marchés plutôt que par le "
     "crédit ; décloisonnement — unification des compartiments et des places.",
 why=["Diversification et délocalisation ne font pas partie de la formule.",
      "Digitalisation et dématérialisation sont postérieures et étrangères à "
      "la formule de Bourguinat.",
      "Dépression, déflation et désendettement décrivent une conjoncture, "
      "pas une transformation structurelle."],
 diss="Les trois D donnent une ossature de partie : chaque D explique une "
      "part de la globalisation financière, et chacun a sa contrepartie en "
      "termes de risque."),

'ch2-qcm-35': f(niv='connaitre', sp='c2-05',
 exp="La titrisation transforme des créances bancaires — crédits immobiliers "
     "notamment — en titres négociables vendus à des investisseurs. La "
     "banque sort le risque de son bilan et récupère de la liquidité ; en "
     "contrepartie, le risque se diffuse dans le système et devient opaque.",
 why=["Transformer des obligations en actions est une conversion, non une "
      "titrisation.",
      "L’émission de titres d’État finance le déficit : c’est une émission "
      "primaire classique.",
      "La conversion de dépôts en billets est un simple retrait."]),

'ch2-qcm-36': f(niv='connaitre', sp='c2-05',
 exp="Un CDO est un titre adossé à un panier de dettes, découpé en tranches "
     "de risque et de rendement différents. Sa complexité est le problème : "
     "elle rend l’évaluation du risque sous-jacent très difficile, ce que la "
     "crise de 2008 a révélé.",
 why=["L’assurance contre le défaut est le CDS, instrument distinct.",
      "Les CDO ne sont pas émis par les banques centrales.",
      "Un contrat de change à terme est un instrument de couverture du "
      "risque de change."]),

'ch2-qcm-37': f(niv='comprendre', sp='c2-05',
 exp="Le CDS fonctionne comme une assurance contre le défaut d’un "
     "emprunteur : l’acheteur paie une prime, le vendeur s’engage à couvrir "
     "la perte. Sa particularité est qu’on peut l’acheter sans détenir la "
     "créance : il devient alors un instrument de spéculation sur la "
     "faillite d’un acteur.",
 why=["La titrisation de créances immobilières donne des titres adossés, non "
      "un CDS.",
      "Ce n’est pas un agrégat monétaire.",
      "Ce n’est pas davantage un instrument de politique monétaire."]),

'ch2-vf-19': f(niv='raisonner', sp='c2-05',
 exp="C’est l’anomalie que souligne le cours : acheter un CDS sans détenir "
     "l’obligation correspondante, c’est acheter une assurance sur la maison "
     "du voisin. L’instrument cesse d’être une couverture pour devenir un "
     "pari sur le défaut, ce qui peut même donner intérêt à la faillite de "
     "l’émetteur."),

'ch2-vf-10': f(niv='connaitre', sp='c2-04',
 exp="C’est la définition même de l’assouplissement quantitatif : des achats "
     "massifs de titres destinés à injecter des liquidités et à faire "
     "baisser les taux longs. Le cours en relève la contrepartie : "
     "déformation des prix d’actifs et risque d’aléa moral."),

'ch2-vf-12': f(niv='comprendre', sp='c2-01',
 exp="Mundell démontre l’inverse : les trois objectifs sont incompatibles "
     "deux à deux, et il faut en abandonner un. Toute l’histoire monétaire "
     "peut se lire comme une succession de choix entre les trois sommets du "
     "triangle."),

'ch2-vf-13': f(niv='comprendre', sp='c2-01',
 exp="C’est bien la définition de la dépréciation compétitive : laisser ou "
     "faire baisser la valeur de la monnaie pour abaisser le prix des "
     "exportations en devises. Le cours en signale la limite, étudiée en "
     "deuxième année : l’inflation importée érode le gain, et les "
     "partenaires peuvent riposter."),

'ch2-vf-16': f(niv='connaitre', sp='c2-01',
 ans=True,
 q="La zone euro compte vingt pays en 2025, et doit en compter vingt et un "
   "en 2026 avec l’entrée de la Bulgarie.",
 exp="Le cours donne cette progression : quinze pays au départ du projet, "
     "vingt membres en 2025, vingt et un en 2026 avec la Bulgarie. L’euro "
     "entre en vigueur en 1999 : avant cette date, il existait autant de "
     "politiques monétaires que de pays, désormais une seule, conduite par "
     "la BCE au sein de l’Eurosystème."),
}

FIX.update({

'ch2-qcm-38': f(niv='connaitre', sp='c2-05',
 exp="Le shadow banking désigne les activités de financement menées hors du "
     "système bancaire régulé, par des acteurs — fonds, véhicules de "
     "titrisation, sociétés de gestion — soumis à des exigences prudentielles "
     "plus faibles. Ils transforment eux aussi des échéances et du risque, "
     "mais sans accès au prêteur en dernier ressort.",
 why=["Il ne s’agit pas d’une question de géographie : le shadow banking "
      "prospère d’abord dans les économies développées.",
      "Il ne s’agit pas d’activités illicites : elles sont légales, "
      "seulement moins régulées.",
      "Les dépôts non déclarés relèvent de la fraude fiscale, autre sujet."]),

'ch2-qcm-39': f(niv='comprendre', sp='c2-05',
 exp="Le problème du « trop gros pour faire faillite » tient à l’aléa moral "
     "qu’il engendre : une institution dont la chute menacerait le système "
     "entier sait qu’elle sera secourue, ce qui l’incite à prendre davantage "
     "de risques. La garantie implicite est un avantage concurrentiel, et "
     "son coût est public.",
 why=["L’accès des petites banques aux marchés n’est pas le problème "
      "désigné.",
      "La question fiscale est étrangère à l’aléa moral systémique.",
      "Le défaut de contrôle des multinationales est un autre débat."],
 diss="Exemple décisif pour un sujet sur la régulation : la garantie "
      "implicite transforme une protection du système en subvention au "
      "risque, ce qui justifie les exigences de fonds propres renforcées."),

'ch2-vf-14': f(niv='raisonner', sp='c2-05',
 exp="Les CDO ont joué ce rôle de diffusion : en découpant des paniers de "
     "créances en tranches revendues dans le monde entier, ils ont dispersé "
     "le risque tout en rendant impossible l’identification de son "
     "porteur final. L’opacité a transformé un choc immobilier américain en "
     "crise de confiance générale sur le marché interbancaire."),

'ch2-vf-15': f(niv='comprendre', sp='c2-05',
 exp="C’est le contraire : le shadow banking opère précisément à la "
     "périphérie du système régulé, avec des contraintes prudentielles plus "
     "faibles. C’est ce qui en fait l’intérêt pour ses acteurs — et le "
     "danger pour le système, puisque ces entités n’ont pas accès au "
     "refinancement de la banque centrale en cas de panique."),

'ch2-vf-20': f(niv='connaitre', sp='c2-05',
 exp="Les trois D de Bourguinat sont la déréglementation, la "
     "désintermédiation et le décloisonnement. Déflation, dépréciation et "
     "désendettement décrivent une conjoncture financière, non le processus "
     "de globalisation financière."),

'ch2-open-10': f(niv='connaitre', sp='c2-05',
 ans={'modele': "Le risque de crédit, ou risque de contrepartie, est le "
      "risque que l’emprunteur ne rembourse pas tout ou partie de sa dette — "
      "capital comme intérêts. Il est rémunéré par une prime incluse dans le "
      "taux, peut être transféré par titrisation et couvert par un CDS.",
      'cles': [{'f': ['rembours', 'defaut', 'défaut'],
                'l': 'c’est le risque de non-remboursement'},
               {'f': ['capital', 'interet', 'intérêt'],
                'l': 'il porte sur le capital comme sur les intérêts'},
               {'f': ['prime', 'taux', 'cds', 'couvert'],
                'l': 'il est rémunéré par une prime ou couvert par un CDS'}]},
 exp="C’est le risque que l’intermédiation bancaire internalise : la banque "
     "le porte, l’évalue et le tarife. La titrisation le fait au contraire "
     "sortir du bilan, ce qui affaiblit l’incitation à l’évaluer."),

'ch2-open-11': f(niv='raisonner', sp='c2-05',
 ans={'modele': "Le passage décrit par Hicks est celui d’un financement "
      "dominé par le crédit bancaire, avec une forte intermédiation, à un "
      "financement dominé par l’émission de titres sur les marchés de "
      "capitaux. Il est porté depuis les années 1980 par les trois D de "
      "Bourguinat : déréglementation, désintermédiation, décloisonnement. "
      "Mais il doit être nuancé : les banques n’ont pas disparu, elles "
      "interviennent désormais sur les marchés — intermédiation de marché.",
      'cles': [{'f': ['credit bancaire', 'intermediation', 'banque'],
                'l': 'on part d’un financement par le crédit bancaire'},
               {'f': ['titre', 'marche', 'marché'],
                'l': 'on va vers un financement par les titres'},
               {'f': ['3d', 'dereglementation', 'desintermediation', 'decloisonnement', '1980'],
                'l': 'le mouvement est porté par les trois D depuis les années 1980'},
               {'f': ['nuance', 'restent', 'pas disparu', 'intermediation de marche'],
                'l': 'les banques restent centrales, par l’intermédiation de marché'}]},
 exp="La nuance finale est la plus importante : une copie qui conclut à la "
     "disparition des banques contredit le cours et passe à côté du risque "
     "systémique, qui vient précisément de leur présence sur les marchés.",
 diss="Ce mouvement est l’arrière-plan de la crise de 2008 : titrisation, "
      "produits dérivés et shadow banking sont les trois formes prises par "
      "cette transformation."),

'ch2-open-12': f(niv='connaitre', sp='c2-05',
 ans={'modele': "Le marché primaire est le marché du neuf : c’est là que "
      "les titres sont émis pour la première fois et que l’émetteur — "
      "entreprise ou État — lève effectivement des capitaux. C’est le seul "
      "moment où le marché finance réellement l’économie.",
      'cles': [{'f': ['emission', 'émis', 'neuf', 'premiere fois'],
                'l': 'c’est le marché de l’émission'},
               {'f': ['capitaux', 'finance', 'lever'],
                'l': 'l’émetteur y lève des capitaux'}]},
 exp="La distinction avec le marché secondaire est essentielle : seules les "
     "émissions primaires apportent des ressources nouvelles ; les échanges "
     "ultérieurs ne font que transférer la propriété des titres."),

'ch2-open-13': f(niv='comprendre', sp='c2-05',
 ans={'modele': "Le marché secondaire, la Bourse, est le marché de "
      "l’occasion : les titres déjà émis s’y échangent entre investisseurs. "
      "Il n’apporte pas de capitaux nouveaux à l’émetteur, mais il assure la "
      "liquidité des titres — chacun sachant pouvoir revendre, la "
      "souscription initiale devient possible — et il en détermine le prix.",
      'cles': [{'f': ['occasion', 'deja emis', 'echange'],
                'l': 'les titres déjà émis s’y échangent'},
               {'f': ['liquidite', 'liquidité', 'revendre'],
                'l': 'il assure la liquidité des titres'},
               {'f': ['prix', 'cours', 'valorisation'],
                'l': 'il en détermine le prix'}]},
 exp="La liquidité du secondaire conditionne le primaire : sans possibilité "
     "de revente, personne ne souscrirait. Les deux marchés sont donc "
     "complémentaires, même si un seul finance l’économie."),

'ch2-open-15': f(niv='comprendre', sp='c2-03',
 ans={'modele': "Une baisse des taux directeurs abaisse le coût du "
      "refinancement des banques, donc le coût du crédit : l’investissement "
      "et la consommation durables sont encouragés. Elle agit aussi par le "
      "prix des actifs, qui montent, par les anticipations, et par le taux "
      "de change, qui se déprécie et soutient les exportations. Une hausse "
      "produit les effets inverses et freine l’activité pour contenir "
      "l’inflation.",
      'cles': [{'f': ['cout du credit', 'coût du crédit', 'credit'],
                'l': 'le canal du taux d’intérêt agit sur le coût du crédit'},
               {'f': ['investissement', 'consommation'],
                'l': 'il commande l’investissement et la consommation'},
               {'f': ['actif', 'anticipation', 'change'],
                'l': 'les canaux du prix des actifs, des anticipations et du change complètent'},
               {'f': ['inflation', 'frein'],
                'l': 'une hausse freine l’activité pour contenir l’inflation'}]},
 exp="Le cours distingue quatre canaux de transmission : taux d’intérêt, "
     "prix des actifs, anticipations (forward guidance) et taux de change. "
     "Leur efficacité conjointe explique pourquoi un même mouvement de taux "
     "a des effets très différents selon la situation financière des agents."),
})


# =============================================================== questions neuves
NEW = [

f(id='q2-n01', sp='c2-01', niv='connaitre', type='assoc', b=92,
  q="Associez chaque fonction internationale d’une monnaie, selon Krugman, à "
    "sa description.",
  ans=[["Monnaie de libellé", "Elle sert à facturer les contrats commerciaux internationaux"],
       ["Monnaie véhiculaire", "Elle sert d’intermédiaire entre deux devises peu échangées entre elles"],
       ["Monnaie d’investissement", "Elle sert de support aux placements et à l’endettement extérieur"],
       ["Monnaie de réserve", "Les banques centrales y détiennent leurs réserves officielles"]],
  exp="Krugman distingue les usages privés — libellé, véhicule, "
      "investissement — des usages publics, dont la réserve. Le dollar "
      "cumule les quatre, ce qui explique sa position : chaque usage "
      "renforce les autres, puisqu’une monnaie largement utilisée est "
      "liquide, et qu’une monnaie liquide est préférée pour les contrats.",
  diss="Ce cumul est l’argument clé pour montrer que la domination d’une "
       "monnaie s’autoentretient : on l’utilise parce que les autres "
       "l’utilisent, mécanisme d’externalité de réseau."),

f(id='q2-n02', sp='c2-01', niv='appliquer', type='qcm', b=25,
  q="Un particulier règle une facture de 1 200 € par virement, puis un café "
    "de 3 € par carte. Comment la comptabilité nationale classe-t-elle ces "
    "deux opérations ?",
  opts=["Les deux sont de la monnaie fiduciaire",
        "Les deux sont de la monnaie scripturale, le virement et la carte "
        "n’étant que des supports de circulation",
        "Le virement est scriptural, le paiement par carte fiduciaire",
        "Le virement est de la monnaie centrale, la carte de la monnaie "
        "scripturale"],
  ans=1,
  why=["La monnaie fiduciaire, ce sont les billets et les pièces : aucune "
       "des deux opérations n’en relève.",
       "La carte ne transporte pas de billets : elle donne un ordre de "
       "transfert entre comptes, donc de la monnaie scripturale.",
       "La monnaie centrale circule entre banques et banque centrale ; un "
       "particulier n’en détient pas."],
  exp="Les deux opérations déplacent un solde de compte à compte : elles "
      "relèvent de la monnaie scripturale, qui représente 91 % de la monnaie "
      "en circulation dans la zone euro. Le virement et la carte sont des "
      "supports, non des formes de monnaie. Le cours ajoute l’asymétrie des "
      "statistiques : virements et prélèvements font 97 % des montants pour "
      "37 % des opérations, les paiements par carte l’inverse."),

f(id='q2-n03', sp='c2-02', niv='raisonner', type='ordre', b=241,
  q="Remettez dans l’ordre les étapes de la création monétaire par une "
    "banque commerciale, puis de sa destruction.",
  ans=["Un client sollicite un crédit et la banque évalue son risque",
       "La banque inscrit une créance à son actif et crédite le compte du client à son passif",
       "La monnaie nouvelle circule dans l’économie au gré des paiements",
       "La banque doit se procurer de la monnaie centrale pour faire face aux fuites",
       "Le remboursement du crédit annule l’écriture et détruit la monnaie créée"],
  exp="Chaque étape commande la suivante. La création est un jeu d’écritures "
      "simultanées : sans dépôt préalable, la banque fabrique le moyen de "
      "paiement qu’elle prête. Les fuites — retraits en billets, règlements "
      "vers d’autres banques, réserves obligatoires — sont ce qui borne "
      "cette création et oblige la banque à se refinancer. Le remboursement "
      "referme le cycle : la monnaie de crédit est temporaire.",
  diss="Dérouler ce cycle permet de répondre rigoureusement à la question "
       "« qui crée la monnaie ? » : les banques commerciales créent "
       "l’essentiel de la monnaie, la banque centrale en fixe le prix et "
       "fournit la monnaie centrale nécessaire aux fuites."),

f(id='q2-n04', sp='c2-02', niv='comprendre', type='qcmm', b=279,
  q="Quelles affirmations correspondent à l’analyse du diviseur de crédit, "
    "d’inspiration keynésienne ? (plusieurs réponses)",
  opts=["La monnaie est endogène : elle naît de la demande de crédit",
        "La banque centrale s’adapte en refinançant les banques après coup",
        "La base monétaire détermine mécaniquement la masse monétaire",
        "Le taux d’intérêt est l’instrument principal de la banque centrale",
        "Les banques prêtent uniquement les dépôts qu’elles ont collectés"],
  ans=[0, 1, 3],
  why=["Exacte : ce sont les crédits demandés et accordés qui font les "
       "dépôts, donc la monnaie.",
       "Exacte : la banque centrale fournit la monnaie centrale nécessaire, "
       "elle ne la rationne pas.",
       "C’est la thèse du multiplicateur, d’inspiration monétariste, qui "
       "suppose la monnaie exogène.",
       "Exacte : ne pouvant piloter la quantité, la banque centrale agit sur "
       "le prix du crédit.",
       "Ce serait l’intermédiation pure, que le cours écarte explicitement."],
  exp="Le partage entre les deux lectures n’est pas qu’académique : il "
      "détermine l’instrument. Si la monnaie est exogène, on cible un "
      "agrégat ; si elle est endogène, on cible un taux. La pratique "
      "contemporaine des banques centrales — pilotage par les taux "
      "directeurs et le corridor — valide la seconde lecture."),

f(id='q2-n05', sp='c2-02', niv='appliquer', type='qcm', b=306,
  q="Dans une économie décrite par MV = PT, la masse monétaire augmente de "
    "10 % et la production réelle de 3 %. Que prévoit la théorie quantitative "
    "si la vitesse de circulation est stable ?",
  opts=["Les prix augmentent d’environ 13 %",
        "Les prix augmentent d’environ 7 %",
        "Les prix sont stables, la production ayant absorbé la monnaie",
        "La production augmente de 10 %, la monnaie étant neutre"],
  ans=1,
  why=["Additionner les deux taux revient à faire croître les prix de la "
       "hausse de la production, ce qui inverse le raisonnement.",
       "Si les prix étaient stables, il faudrait que la production absorbe "
       "toute la création monétaire, soit 10 %.",
       "La neutralité signifie précisément que la monnaie n’agit pas sur la "
       "production réelle."],
  exp="L’équation donne, en taux de croissance, m + v = p + t. Avec v = 0, "
      "p = m − t = 10 − 3 = 7 %. C’est la mécanique de la théorie "
      "quantitative : la part de création monétaire non absorbée par la "
      "croissance réelle se déverse dans les prix.",
  diss="Ce calcul permet d’énoncer précisément la thèse monétariste, et donc "
       "de la discuter : il suffit que V varie — ce qu’observent les "
       "keynésiens — pour que la conclusion tombe."),

f(id='q2-n06', sp='c2-03', niv='comprendre', type='ordre', b=576,
  q="Remettez dans l’ordre le canal des taux d’intérêt, de la décision de la "
    "banque centrale à l’activité.",
  ans=["La banque centrale abaisse ses taux directeurs",
       "Le refinancement des banques devient moins coûteux",
       "Les banques abaissent les taux qu’elles pratiquent sur les crédits",
       "L’investissement des entreprises et la consommation durable des ménages augmentent",
       "La demande globale s’élève, ce qui soutient l’activité et les prix"],
  exp="Le canal suppose que chaque maillon tienne. Il peut se rompre en "
      "plusieurs points : des banques fragilisées peuvent ne pas répercuter "
      "la baisse, des entreprises sans débouchés peuvent ne pas emprunter "
      "même à taux nul — c’est la trappe à liquidité. Le cours ajoute trois "
      "autres canaux : prix des actifs, anticipations, taux de change.",
  diss="Montrer qu’un canal est une chaîne, et nommer le maillon qui cède, "
       "est exactement ce qu’attend un sujet sur l’efficacité de la "
       "politique monétaire."),

f(id='q2-n07', sp='c2-03', niv='appliquer', type='qcm', b=549,
  q="Une banque dispose de liquidités excédentaires pour vingt-quatre "
    "heures. À quel taux les place-t-elle auprès de la BCE, et quel rôle ce "
    "taux joue-t-il dans le corridor ?",
  opts=["Au taux de refinancement, qui constitue le milieu du corridor",
        "Au taux de facilité de dépôt, qui constitue le plancher du corridor",
        "Au taux de facilité de prêt marginal, qui constitue le plafond",
        "Au taux du marché interbancaire, fixé librement entre banques"],
  ans=1,
  why=["Le taux de refinancement est celui des opérations de crédit à une "
       "semaine : il n’est pas celui d’un dépôt.",
       "La facilité de prêt marginal est l’emprunt au jour le jour auprès de "
       "la banque centrale : c’est le plafond, pas le placement.",
       "Le taux interbancaire se forme entre banques, mais il est justement "
       "borné par le corridor."],
  exp="Aucune banque ne prêtera à une autre à un taux inférieur à celui "
      "qu’elle obtient sans risque auprès de la banque centrale : la "
      "facilité de dépôt forme donc le plancher. Symétriquement, aucune "
      "n’empruntera plus cher que la facilité de prêt marginal, qui forme le "
      "plafond. Le taux du marché interbancaire évolue dans ce corridor."),

f(id='q2-n08', sp='c2-04', niv='raisonner', type='qcm', b=645,
  q="Les politiques monétaires non conventionnelles ont été critiquées pour "
    "l’aléa moral qu’elles engendrent. En quoi consiste exactement ce "
    "reproche ?",
  opts=["Elles provoquent nécessairement de l’inflation",
        "Elles conduisent les acteurs à prendre davantage de risques en "
        "comptant sur le soutien de la banque centrale",
        "Elles font perdre leur indépendance aux banques centrales",
        "Elles profitent aux États plutôt qu’aux entreprises"],
  ans=1,
  why=["L’inflation est un risque, mais la décennie 2010 montre qu’elle "
       "n’est pas automatique : ce n’est pas la définition de l’aléa moral.",
       "La perte d’indépendance est un autre reproche, celui de la "
       "monétisation, que le cours distingue.",
       "La répartition des bénéfices entre États et entreprises est une "
       "question distincte."],
  exp="L’aléa moral désigne le changement de comportement induit par la "
      "protection : si les intervenants anticipent qu’une banque centrale "
      "achètera les titres en cas de tension, ils acceptent des risques "
      "qu’ils refuseraient autrement. La protection du système finit par "
      "encourager ce qu’elle devait prévenir.",
  diss="À articuler avec le « too big to fail » : les deux décrivent le même "
       "mécanisme, l’un pour les établissements, l’autre pour les marchés."),

f(id='q2-n09', sp='c2-04', niv='comprendre', type='vf', b=668,
  q="L’assouplissement quantitatif et l’assouplissement qualitatif désignent "
    "la même opération de banque centrale.",
  ans=False,
  exp="Le cours les distingue : l’assouplissement quantitatif porte sur le "
      "volume — acheter massivement des titres pour injecter des liquidités "
      "et abaisser les taux longs ; l’assouplissement qualitatif porte sur "
      "la composition du bilan — accepter des titres de moindre qualité ou "
      "de plus longue maturité, pour soutenir des segments de marché "
      "précis. On peut faire l’un sans l’autre.",
  diss="Distinction qui montre qu’une banque centrale n’agit pas seulement "
       "sur le prix et la quantité de monnaie, mais aussi sur la structure "
       "des risques qu’elle accepte de porter."),

f(id='q2-n10', sp='c2-05', niv='raisonner', type='ordre', b=855,
  q="Remettez dans l’ordre l’enchaînement qui transforme des crédits "
    "immobiliers en risque systémique mondial.",
  ans=["Des banques accordent des crédits immobiliers à des emprunteurs fragiles",
       "Ces créances sont titrisées et sorties des bilans bancaires",
       "Les titres sont assemblés en produits complexes vendus dans le monde entier",
       "La hausse des défauts dévalorise ces titres sans qu’on sache qui les détient",
       "La défiance gèle le marché interbancaire et la crise devient systémique"],
  exp="Le point de bascule est le quatrième : l’opacité. Tant que les "
      "défauts restent rares, la dispersion du risque paraît le réduire ; "
      "dès qu’ils augmentent, l’impossibilité d’identifier les porteurs fait "
      "que chacun soupçonne tous les autres. Le risque de contrepartie "
      "devient alors généralisé, et le marché du financement de court terme "
      "s’arrête.",
  diss="Enchaînement à connaître pour tout sujet sur la globalisation "
       "financière : il montre que la dispersion du risque n’est protectrice "
       "que si l’information circule aussi bien que les titres."),

f(id='q2-n11', sp='c2-05', niv='comprendre', type='qcmm', b=830,
  q="Quels effets la titrisation produit-elle, selon le cours ? "
    "(plusieurs réponses)",
  opts=["Elle rend de la liquidité aux banques en sortant les créances du bilan",
        "Elle diffuse le risque de crédit dans l’ensemble du système financier",
        "Elle rend l’évaluation du risque plus opaque",
        "Elle supprime le risque de défaut des emprunteurs",
        "Elle réduit mécaniquement le coût du crédit pour les États"],
  ans=[0, 1, 2],
  why=["Exacte : c’est son intérêt premier pour la banque, qui récupère des "
       "ressources pour prêter à nouveau.",
       "Exacte : le risque ne disparaît pas, il est transféré et dispersé.",
       "Exacte : l’empilement des tranches rend le sous-jacent difficile à "
       "apprécier, ce que la crise de 2008 a révélé.",
       "Le risque de défaut demeure : il change simplement de porteur.",
       "La titrisation porte sur des créances privées ; elle n’abaisse pas "
       "mécaniquement le coût de la dette publique."],
  exp="L’ambivalence est le point à retenir : le même mécanisme qui améliore "
      "la liquidité et répartit le risque affaiblit l’incitation à évaluer "
      "ce risque, puisque celui qui accorde le crédit ne le conserve pas."),

f(id='q2-n12', sp='c2-05', niv='appliquer', type='vf', b=875,
  q="Un investisseur achète des CDS sur la dette d’une entreprise dont il ne "
    "détient aucune obligation : il se couvre contre un risque qu’il porte.",
  ans=False,
  exp="Ne détenant pas la créance, il ne porte aucun risque à couvrir : son "
      "achat est un pari sur la faillite de l’entreprise. Le cours souligne "
      "cette dérive — spéculer sur le défaut d’un acteur — et son effet "
      "pervers : la demande de protection peut elle-même dégrader la "
      "perception du risque et précipiter ce qu’elle anticipait.",
  diss="Exemple à garder pour montrer qu’un instrument de couverture devient "
       "déstabilisant dès lors qu’il peut être acheté par des agents non "
       "exposés : le problème n’est pas l’outil mais son usage « à nu »."),

f(id='q2-n13', sp='c2-03', niv='connaitre', type='courte', b=503,
  q="Quel est le mandat principal de la BCE, et par quels instruments "
    "l’exerce-t-elle ?",
  ans={'modele': "La BCE a pour mandat principal la stabilité des prix, "
       "qu’elle définit comme une inflation de 2 % à moyen terme. Elle "
       "l’exerce par trois taux directeurs formant un corridor — facilité de "
       "dépôt en plancher, refinancement, facilité de prêt marginal en "
       "plafond — et, depuis la crise, par des instruments non "
       "conventionnels comme l’assouplissement quantitatif et la "
       "communication sur ses intentions futures.",
       'cles': [{'f': ['stabilite des prix', 'stabilité des prix'],
                 'l': 'son mandat est la stabilité des prix'},
                {'f': ['2 %', '2%'], 'l': 'avec une cible de 2 % à moyen terme'},
                {'f': ['taux directeur', 'corridor', 'refinanc'],
                 'l': 'elle agit par les taux directeurs'},
                {'f': ['non conventionnel', 'qe', 'quantitative', 'forward'],
                 'l': 'complétés par des instruments non conventionnels'}]},
  exp="La hiérarchie des objectifs distingue la BCE de la Réserve fédérale, "
      "dont le mandat est double — prix et emploi. Cette différence "
      "institutionnelle explique des réactions différentes face à un même "
      "choc."),

f(id='q2-n14', sp='c2-01', niv='raisonner', type='courte', b=181,
  q="Expliquez en quoi le triangle de Mundell éclaire le choix fait par les "
    "pays de la zone euro.",
  ans={'modele': "Le triangle énonce qu’on ne peut réunir simultanément "
       "libre circulation des capitaux, autonomie de la politique monétaire "
       "et stabilité du change. Les pays de la zone euro ont choisi la "
       "stabilité absolue du change entre eux — la monnaie unique — et la "
       "liberté des capitaux : ils ont donc nécessairement renoncé à toute "
       "politique monétaire nationale, désormais confiée à la BCE.",
       'cles': [{'f': ['trois objectif', 'incompatib', 'deux sur trois'],
                 'l': 'les trois objectifs sont incompatibles'},
                {'f': ['capitaux'], 'l': 'la libre circulation des capitaux est conservée'},
                {'f': ['change', 'monnaie unique'],
                 'l': 'la stabilité du change est assurée par la monnaie unique'},
                {'f': ['autonomie', 'nationale', 'bce'],
                 'l': 'l’autonomie monétaire nationale est abandonnée'}]},
  exp="Le raisonnement vaut aussi en sens inverse : un pays qui tient à son "
      "autonomie monétaire et à un change stable doit contrôler les "
      "capitaux, ce qu’a longtemps fait la Chine.",
  diss="C’est la manière la plus rigoureuse d’introduire un sujet sur l’euro "
       "ou sur la souveraineté monétaire : l’abandon n’est pas un accident "
       "politique, c’est la contrepartie logique de deux choix assumés."),
]
