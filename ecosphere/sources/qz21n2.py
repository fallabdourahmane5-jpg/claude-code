# -*- coding: utf-8 -*-
"""Chapitre 21 — questions nouvelles, sous-parties c21-06 à c21-09."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c21-06
f(id='q21-n20', sp='c21-06', niv='connaitre', type='qcm', b=1758,
  q="Quel critère détermine si un agent est « résident » au sens de la "
    "balance des paiements ?",
  opts=["Sa nationalité",
        "Son lieu principal d’activité économique : une entreprise étrangère "
        "implantée durablement en France peut être résidente française",
        "Son lieu de naissance",
        "Le pays où il paie ses impôts sur le revenu"],
  ans=1,
  why=["La nationalité est précisément le critère que la comptabilité "
       "nationale écarte.",
       "Le lieu de naissance n’intervient pas.",
       "La fiscalité peut s’en rapprocher mais n’est pas le critère retenu."],
  exp="Cette convention a des conséquences concrètes : les opérations d’une "
      "filiale étrangère implantée durablement en France avec le reste du "
      "monde figurent dans la balance des paiements française. De même, les "
      "dépenses d’un touriste non-résident en France sont assimilées à des "
      "exportations de services, et celles d’un résident français à "
      "l’étranger à des importations.",
  diss="Attention au piège : « résident » n’est pas « national »."),

f(id='q21-n21', sp='c21-06', niv='appliquer', type='assoc', b=1834,
  q="Classez chaque opération dans la composante du compte courant à laquelle "
    "elle appartient.",
  ans=[["La vente de voitures françaises à l’étranger", "Les biens"],
       ["Les dépenses d’un touriste étranger en France", "Les services"],
       ["Les dividendes reçus par un résident français depuis les États-Unis", "Les revenus primaires"],
       ["L’aide publique au développement versée à un État étranger", "Les revenus secondaires"]],
  exp="Les revenus primaires correspondent aux revenus directement liés à la "
      "participation à la production : rémunérations du travail et revenus du "
      "capital, comme les intérêts versés à un non-résident détenteur d’une "
      "obligation française. Les revenus secondaires sont des transferts sans "
      "contrepartie productive directe. Un pays fortement investi à "
      "l’étranger peut ainsi recevoir d’importants revenus de patrimoine.",
  diss="C’est ce qui explique le cas français : un déficit sur les biens, "
       "mais un déficit courant limité grâce aux services et aux revenus "
       "primaires."),

f(id='q21-n22', sp='c21-06', niv='appliquer', type='qcm', b=1821,
  q="En 2025, la France exporte 624 Md€ de biens et en importe 682 Md€. Quel "
    "est son solde commercial sur les biens, et que faut-il en conclure sur "
    "son solde courant ?",
  opts=["−58 Md€, et le solde courant est nécessairement du même montant",
        "−58 Md€, mais le solde courant est bien moins dégradé car les "
        "services et les revenus primaires sont excédentaires",
        "+58 Md€, le pays étant excédentaire",
        "Le solde ne peut pas être calculé sans connaître le compte financier"],
  ans=1,
  why=["Confondre solde commercial et solde courant est l’erreur la plus "
       "fréquente du chapitre.",
       "Le signe est négatif : les importations dépassent les exportations.",
       "Le solde commercial se calcule directement : 624 − 682."],
  exp="624 − 682 = −58 Md€. Mais le compte courant comprend aussi les "
      "services — dont les crédits dépassent les débits selon les données du "
      "cours —, les revenus primaires et les revenus secondaires. Le déficit "
      "courant français reste donc relativement faible par rapport au seul "
      "déficit des biens.",
  diss="Lecture complémentaire à connaître : les soldes bilatéraux montrent "
       "un déficit marqué vis-à-vis de la Chine mais un excédent vis-à-vis "
       "des États-Unis."),

f(id='q21-n23', sp='c21-06', niv='comprendre', type='qcm', b=1976,
  q="Dans le compte financier, comment distingue-t-on les avoirs des "
    "engagements ?",
  opts=["Les avoirs sont les flux entrants, les engagements les flux sortants",
        "Un avoir est un actif détenu par un résident sur le reste du monde ; "
        "un engagement est un actif domestique détenu par un non-résident",
        "Les avoirs concernent les IDE, les engagements les investissements "
        "de portefeuille",
        "Les avoirs appartiennent à l’État, les engagements aux entreprises"],
  ans=1,
  why=["La distinction n’est pas celle du sens du flux mais de la propriété "
       "de l’actif.",
       "Les deux catégories recouvrent tous les types d’investissement.",
       "Le statut public ou privé du détenteur n’intervient pas."],
  exp="Cette distinction est la clé de la position extérieure nette, qui se "
      "calcule comme la différence entre les avoirs extérieurs détenus par "
      "les résidents et les engagements envers le reste du monde. Le compte "
      "financier français de 2025 illustre ce jeu : les investissements de "
      "portefeuille présentent un solde de +133 Md€ (335 contre 202), les "
      "autres investissements un solde de −185 Md€ (281 contre 466)."),

f(id='q21-n24', sp='c21-06', niv='raisonner', type='qcm', b=2173,
  q="Par quel mécanisme un déficit public peut-il creuser le déficit "
    "extérieur ?",
  opts=["En augmentant directement les droits de douane",
        "En stimulant la demande intérieure : les revenus et la consommation "
        "progressent, et une partie de cette demande supplémentaire porte sur "
        "des importations",
        "En réduisant l’épargne des entreprises",
        "En faisant baisser les taux d’intérêt mondiaux"],
  ans=1,
  why=["Le déficit public n’a pas d’effet direct sur la fiscalité "
       "douanière.",
       "L’épargne des entreprises figure dans (S − I) mais n’est pas le canal "
       "décrit.",
       "Un déficit public tend plutôt à exercer une pression haussière sur "
       "les taux."],
  exp="L’enchaînement est explicite : politique budgétaire expansionniste → "
      "demande ↑ → importations ↑ → déficit courant ↑. L’identité "
      "X − M = (S − I) + (T − G) en fournit la traduction comptable. Les "
      "trois épisodes américains cités par le cours — Reagan, George W. Bush, "
      "puis les mandats de Trump — illustrent cette relation, avec un déficit "
      "public autour de 6 % du PIB depuis 2022 et un déficit extérieur "
      "supérieur à 1 200 Md$.",
  diss="Attention à la prudence du cours : il s’agit d’une « hypothèse » des "
       "déficits jumeaux, c’est-à-dire d’une relation possible et non d’une "
       "loi mécanique."),

# ------------------------------------------------------------- c21-07
f(id='q21-n25', sp='c21-07', niv='connaitre', type='qcm', b=2192,
  q="Qu’est-ce qui distingue la balance des paiements de la position "
    "extérieure nette ?",
  opts=["La première porte sur les biens, la seconde sur les capitaux",
        "La première retrace des flux sur une période donnée, la seconde "
        "mesure un stock d’actifs et d’engagements accumulés vis-à-vis du "
        "reste du monde",
        "La première est comptable, la seconde est une prévision",
        "La première concerne le secteur privé, la seconde le secteur public"],
  ans=1,
  why=["Les deux documents couvrent l’ensemble des opérations extérieures.",
       "La PEN est une mesure comptable, pas une prévision.",
       "Les deux agrègent public et privé."],
  exp="La PEN se calcule comme les actifs extérieurs détenus par les "
      "résidents moins les engagements envers le reste du monde. Si un pays "
      "détient 1 000 milliards d’actifs à l’étranger et que les non-résidents "
      "détiennent 700 milliards d’actifs domestiques, la PEN vaut +300 "
      "milliards : le pays est créancier net. Dans le cas inverse, il est "
      "débiteur net.",
  diss="Formule à retenir : la PEN est la trace patrimoniale de "
       "l’accumulation passée des déséquilibres extérieurs."),

f(id='q21-n26', sp='c21-07', niv='appliquer', type='qcm', b=2298,
  q="Quel seuil de position extérieure nette la procédure européenne de "
    "surveillance des déséquilibres macroéconomiques utilise-t-elle comme "
    "signal d’alerte, et comment l’interpréter ?",
  opts=["−10 % du PIB, seuil au-delà duquel un pays est automatiquement "
        "insolvable",
        "−35 % du PIB, qui constitue un signal d’alerte et non un seuil "
        "automatique d’insoutenabilité",
        "−90 % du PIB, niveau atteint par les États-Unis",
        "−120 % du PIB, correspondant à la dette publique américaine"],
  ans=1,
  why=["Aucun seuil ne rend un pays automatiquement insolvable.",
       "−90 % du PIB est l’ordre de grandeur de la PEN américaine, pas le "
       "seuil européen.",
       "120 % du PIB renvoie à la dette publique américaine, autre "
       "indicateur."],
  exp="La France présente en 2025 une PEN d’environ −30 % du PIB : elle est "
      "donc débitrice nette, ce qui est cohérent avec ses déficits extérieurs "
      "réguliers. Cela ne signifie pas que les Français n’investissent pas à "
      "l’étranger, mais que la valeur de leurs avoirs extérieurs reste "
      "inférieure à celle des actifs français détenus par des non-résidents.",
  diss="Le cours insiste : la soutenabilité d’une PEN négative dépend moins "
       "de son montant que de la capacité durable du pays à attirer les "
       "capitaux."),

f(id='q21-n27', sp='c21-07', niv='raisonner', type='qcm', b=2304,
  q="Comment les États-Unis peuvent-ils maintenir une position extérieure "
    "nette d’environ −90 % du PIB sans crise de financement ?",
  opts=["Parce qu’ils imposent à leurs partenaires d’acheter leurs titres",
        "Parce que leurs actifs sont extrêmement demandés et que le rôle "
        "international du dollar leur permet de financer durablement leurs "
        "déficits",
        "Parce que leur position extérieure nette est en réalité positive",
        "Parce que leur dette est intégralement détenue par des résidents"],
  ans=1,
  why=["Aucune contrainte de ce type n’existe : la demande est volontaire.",
       "Leur PEN est au contraire très négative, conséquence de décennies de "
       "déficits.",
       "Une part importante est précisément détenue par des non-résidents."],
  exp="C’est le privilège exorbitant : la demande mondiale d’actifs "
      "américains reste exceptionnellement forte parce que les titres du "
      "Trésor jouent le rôle d’actif sûr mondial. Le cours souligne toutefois "
      "une inquiétude nouvelle : avec une dette publique supérieure à 120 % "
      "du PIB et des projections autour de 140 %, la question se pose de "
      "savoir si ces titres resteront perçus comme totalement sûrs.",
  diss="Question de soutenabilité à formuler correctement : non pas « le "
       "montant est-il trop élevé ? » mais « le pays conserve-t-il la "
       "capacité d’attirer durablement des capitaux ? »."),

f(id='q21-n28', sp='c21-07', niv='comprendre', type='qcm', b=2514,
  q="Que signifie une élasticité-prix des exportations faible, et qu’en "
    "déduit-on sur la compétitivité d’un pays ?",
  opts=["Que les exportations réagissent fortement aux variations de prix, "
        "signe d’une forte compétitivité-prix",
        "Que la demande étrangère est peu sensible aux prix, ce qui traduit "
        "généralement une forte compétitivité hors prix",
        "Que le pays exporte peu",
        "Que les prix à l’exportation sont fixes"],
  ans=1,
  why=["C’est l’inverse : une élasticité élevée signale une forte sensibilité "
       "au prix.",
       "Le volume des exportations n’est pas ce que mesure l’élasticité.",
       "Les prix ne sont pas fixes : l’élasticité mesure précisément la "
       "réaction à leurs variations."],
  exp="L’élasticité-prix des exportations rapporte la variation en "
      "pourcentage des exportations à la variation en pourcentage des prix. "
      "Une élasticité faible signifie que les acheteurs étrangers continuent "
      "d’acheter même si les prix augmentent : l’entreprise dispose d’une "
      "compétitivité hors prix — qualité, innovation, différenciation. La "
      "France présente une élasticité plus élevée, ce qui révèle une plus "
      "forte dépendance à la compétitivité-prix.",
  diss="Le problème français est précisément un décalage : des coûts proches "
       "de ceux des économies haut de gamme pour une spécialisation plus "
       "souvent moyenne gamme."),

f(id='q21-n29', sp='c21-07', niv='raisonner', type='qcmm', b=2492,
  q="Quels signaux inquiétants un déficit extérieur persistant peut-il "
    "révéler, selon le cours ? (plusieurs réponses)",
  opts=["Un problème de compétitivité, qu’elle soit de prix ou hors prix",
        "Une désindustrialisation obligeant à réimporter les biens destinés à "
        "la demande intérieure",
        "Une dépendance énergétique vis-à-vis d’un fournisseur étranger",
        "Un risque de cercle vicieux des monnaies faibles et d’inflation "
        "importée",
        "Une capacité de financement excessive de la nation"],
  ans=[0, 1, 2, 3],
  why=["Exacte : le décalage entre coûts et gamme en est une forme.",
       "Exacte : délocalisation → production domestique ↓ → biens réimportés "
       "↑ → déficit ↑.",
       "Exacte : avant 2022, environ 40 % des besoins gaziers européens "
       "étaient satisfaits par du gaz russe.",
       "Exacte : déficit → monnaie ↓ → importations plus chères → déficit ↑.",
       "Un déficit traduit précisément un besoin, et non une capacité de "
       "financement."],
  exp="Le cours ajoute un cinquième signal : le déficit doit être financé, ce "
      "qui crée une dépendance aux capitaux étrangers et dégrade "
      "progressivement la position extérieure nette. Il nuance toutefois le "
      "quatrième : une dépréciation ne conduit pas nécessairement à un cercle "
      "vicieux, puisque si les exportations réagissent suffisamment, le gain "
      "de compétitivité-prix peut à terme améliorer le solde, selon la "
      "logique de la courbe en J."),

# ------------------------------------------------------------- c21-08
f(id='q21-n30', sp='c21-08', niv='comprendre', type='ordre', b=2589,
  q="Remettez dans l’ordre le cercle vicieux des monnaies faibles.",
  ans=["Le pays présente un déficit commercial important",
       "Les résidents vendent leur monnaie pour obtenir des devises et payer "
       "leurs importations : l’offre de monnaie nationale augmente",
       "La monnaie se déprécie",
       "Les importations deviennent plus chères en monnaie nationale",
       "Le déficit extérieur s’aggrave, ce qui alimente une nouvelle "
       "dépréciation"],
  exp="Ce cercle peut en outre se transmettre à l’économie domestique par "
      "l’inflation importée : des importations plus chères élèvent les coûts "
      "de production, donc les prix intérieurs, particulièrement lorsque le "
      "pays dépend de biens libellés en devises. Le cours rappelle toutefois "
      "que le mécanisme n’est pas automatique, une dépréciation pouvant aussi "
      "améliorer la compétitivité-prix.",
  diss="Mécanisme à mobiliser pour les économies émergentes très dépendantes "
       "des importations et endettées en devises."),

f(id='q21-n31', sp='c21-08', niv='connaitre', type='qcm', b=2682,
  q="Qu’est-ce qu’un sudden stop, et pourquoi est-il particulièrement "
    "dangereux ?",
  opts=["Un arrêt brutal des exportations d’un pays",
        "Un arrêt brutal des entrées de capitaux étrangers, susceptible de "
        "provoquer une crise de financement dans une économie qui en dépend",
        "Une suspension des paiements décidée par le FMI",
        "Une fermeture temporaire des marchés financiers"],
  ans=1,
  why=["Ce sont les capitaux, et non les exportations, qui s’interrompent.",
       "Aucune décision institutionnelle n’est en cause : ce sont les "
       "investisseurs qui se retirent.",
       "La fermeture des marchés est une mesure administrative, pas ce "
       "phénomène."],
  exp="Le risque est d’autant plus fort que les acteurs domestiques se sont "
      "endettés en devises étrangères : une dépréciation de la monnaie "
      "nationale augmente alors mécaniquement le poids réel de la dette — "
      "monnaie ↓ → valeur de la dette en dollars ↑ → difficultés de "
      "remboursement ↑. Un déficit courant n’est donc soutenable que si le "
      "pays parvient à attirer durablement les capitaux nécessaires.",
  diss="Illustration historique : la crise mexicaine de 1982, après le "
       "retournement des taux américains."),

f(id='q21-n32', sp='c21-08', niv='raisonner', type='qcm', b=2745,
  q="Comment Nurkse et Rostow permettent-ils de justifier qu’un déficit "
    "courant soit normal au début du développement ?",
  opts=["Parce qu’un pays pauvre doit d’abord accumuler des réserves de change",
        "Parce que la faiblesse des revenus réduit l’épargne, donc "
        "l’investissement et les gains de productivité (Nurkse), alors que le "
        "décollage suppose un fort taux d’investissement (Rostow) : le "
        "financement extérieur permet de briser ce cercle vicieux",
        "Parce que les pays pauvres ont des termes de l’échange favorables",
        "Parce que le déficit courant augmente automatiquement l’épargne "
        "domestique"],
  ans=1,
  why=["L’accumulation de réserves correspond plutôt à une stratégie "
       "d’excédents.",
       "Prebisch montre l’inverse pour les économies spécialisées dans le "
       "primaire.",
       "Un déficit courant signifie précisément que l’épargne domestique est "
       "insuffisante."],
  exp="L’enchaînement est le suivant : capitaux étrangers → investissement ↑ "
      "→ productivité ↑ → croissance ↑. La mobilité internationale des "
      "capitaux permet donc à une économie pauvre de dépasser la contrainte "
      "de l’épargne domestique en finançant son développement par l’épargne "
      "du reste du monde.",
  diss="Idée forte : un déficit extérieur peut être le signe d’un dynamisme "
       "d’investissement, et non d’une faiblesse."),

f(id='q21-n33', sp='c21-08', niv='appliquer', type='ordre', b=2780,
  q="Remettez dans l’ordre l’enchaînement qui relie le recyclage des "
    "pétrodollars à la crise de la dette latino-américaine.",
  ans=["Dans les années 1970, les chocs pétroliers enrichissent fortement les "
       "pays exportateurs de pétrole",
       "Leurs systèmes financiers domestiques ne peuvent absorber toute cette "
       "épargne, qui est placée dans les banques occidentales",
       "Ces banques prêtent massivement aux économies en développement à la "
       "recherche de financements",
       "En 1979, Paul Volcker arrive à la Fed et relève fortement les taux "
       "d’intérêt : les capitaux repartent vers les États-Unis",
       "Le coût des dettes libellées en dollars explose : le Mexique entre en "
       "crise en 1982"],
  exp="Le recyclage des pétrodollars illustre la capacité de la finance "
      "internationale à financer le développement : l’épargne des pays "
      "excédentaires se dirige vers les économies en besoin de financement. "
      "Mais il illustre aussi la fragilité de ce financement : les "
      "États-Unis deviennent une « pompe aspirante » à capitaux dès lors "
      "qu’ils offrent un rendement élevé.",
  diss="Leçon centrale : les capitaux étrangers peuvent accélérer le "
       "développement, mais aussi transformer brutalement un déficit "
       "soutenable en crise de dette."),

f(id='q21-n34', sp='c21-08', niv='raisonner', type='qcm', b=2855,
  q="Quelle est, selon le cours, la bonne question à se poser devant un "
    "déficit courant ?",
  opts=["Quel est son montant en points de PIB ?",
        "Pourquoi le pays est-il en déficit : un déficit finançant une "
        "accumulation productive et le rattrapage est moins préoccupant qu’un "
        "déficit de consommation et de désindustrialisation",
        "Depuis combien d’années dure-t-il ?",
        "Quel partenaire commercial en est responsable ?"],
  ans=1,
  why=["Le montant seul ne dit rien de la soutenabilité.",
       "La durée importe, mais elle ne suffit pas à juger : certains "
       "déficits durables sont soutenables.",
       "Chercher un responsable étranger est précisément la lecture que "
       "l’identité macroéconomique invalide."],
  exp="L’interprétation d’un déficit doit porter sur son origine et sur la "
      "nature de son financement. Le cours ajoute la symétrie : un excédent "
      "n’est pas toujours une bonne nouvelle, car il peut refléter une "
      "épargne excessive relativement à un investissement domestique "
      "insuffisant.",
  diss="Phrase de conclusion possible : ce n’est pas le solde qui informe, "
       "c’est ce qu’il finance et qui le finance."),

# ------------------------------------------------------------- c21-09
f(id='q21-n35', sp='c21-09', niv='comprendre', type='qcm', b=2951,
  q="Que révèle, selon le cours, l’excédent courant allemand ?",
  opts=["Une compétitivité parfaite de son industrie",
        "En partie une épargne élevée associée à un investissement public et "
        "privé insuffisant",
        "Une sous-évaluation volontaire de sa monnaie",
        "Un excès d’importations de biens d’équipement"],
  ans=1,
  why=["La compétitivité allemande est réelle, mais le cours invite à "
       "nuancer : l’excédent n’est pas qu’un succès.",
       "L’Allemagne partage l’euro : elle ne peut pas le sous-évaluer "
       "unilatéralement.",
       "Un excès d’importations réduirait l’excédent."],
  exp="Un excédent courant peut révéler une forte compétitivité, mais "
      "également un sous-investissement domestique lorsque l’épargne excède "
      "durablement l’investissement. Le cours relève aussi une spécialisation "
      "encore très liée aux technologies de la deuxième révolution "
      "industrielle. C’est précisément pour corriger ce sous-investissement "
      "que l’Allemagne a engagé un vaste plan d’investissement de l’ordre de "
      "500 milliards d’euros.",
  diss="Rappel de l’identité : X − M = (S − I) + (T − G). Un excédent "
       "extérieur peut donc signaler un (S − I) trop élevé, c’est-à-dire un "
       "investissement trop faible."),

f(id='q21-n36', sp='c21-09', niv='comprendre', type='qcm', b=2996,
  q="Quelle est la thèse d’Hélène Rey sur les déséquilibres mondiaux ?",
  opts=["Qu’ils résultent d’erreurs de mesure statistique",
        "Qu’ils ne sont pas de simples anomalies comptables mais reflètent "
        "les faiblesses structurelles des modèles de croissance nationaux",
        "Qu’ils s’annulent automatiquement à long terme",
        "Qu’ils sont dus exclusivement aux politiques de change"],
  ans=1,
  why=["Ce ne sont pas des artefacts statistiques : les soldes sont "
       "massifs.",
       "Le cours souligne au contraire leur persistance et leur réouverture "
       "depuis la fin des années 2010.",
       "Le taux de change joue un rôle, notamment pour la Chine, mais il "
       "n’explique pas tout."],
  exp="Les déséquilibres excessifs sont la conséquence de stratégies de "
      "croissance elles-mêmes déséquilibrées. Le cours en dresse la "
      "typologie : les États-Unis combinent déficit public et manque "
      "d’épargne ; la Chine cumule surépargne, surinvestissement et "
      "surcapacités ; l’Europe associe une épargne élevée à un "
      "sous-investissement. La mondialisation financière permet à ces modèles "
      "de coexister, puisque l’épargne des pays excédentaires finance les "
      "pays déficitaires.",
  diss="Triptyque à mémoriser : États-Unis / Chine / Europe — trois "
       "déséquilibres de nature différente, mais complémentaires."),

f(id='q21-n37', sp='c21-09', niv='raisonner', type='qcmm', b=3021,
  q="Quels facteurs expliquent le taux d’épargne très élevé des ménages "
    "chinois, selon le cours ? (plusieurs réponses)",
  opts=["Une protection sociale relativement moins développée que dans les "
        "économies occidentales, qui encourage une épargne de précaution",
        "Les déséquilibres démographiques issus de la politique de l’enfant "
        "unique, qui ont renforcé les incitations patrimoniales des ménages",
        "La crise immobilière depuis environ 2020, qui provoque un effet "
        "richesse négatif incitant à reconstituer son patrimoine",
        "Une fiscalité de l’épargne particulièrement avantageuse",
        "Un taux d’intérêt réel très élevé imposé par la banque centrale"],
  ans=[0, 1, 2],
  why=["Exacte : c’est le facteur principal retenu par le cours.",
       "Exacte : certaines familles ont accru leur épargne pour améliorer la "
       "position de leur fils sur le marché matrimonial.",
       "Exacte : la perte de valeur du patrimoine immobilier pousse à "
       "épargner davantage.",
       "La fiscalité de l’épargne n’est pas évoquée.",
       "Le cours ne mentionne pas de politique de taux réels élevés."],
  exp="Cette surépargne a une contrepartie : la consommation intérieure reste "
      "insuffisante au regard de capacités productives massives. La Chine est "
      "donc en situation de surcapacité, ce qui exerce une pression "
      "déflationniste sur ses prix domestiques et renforce la compétitivité-"
      "prix de ses exportations."),

f(id='q21-n38', sp='c21-09', niv='raisonner', type='ordre', b=3091,
  q="Remettez dans l’ordre le mécanisme reliant le modèle de croissance "
    "chinois à son excédent courant.",
  ans=["Le taux d’épargne des ménages est très élevé et la protection sociale "
       "relativement limitée",
       "L’investissement productif est massif, au point de créer des "
       "surcapacités",
       "La consommation intérieure ne suffit pas à absorber la production",
       "La Chine doit exporter ses surplus",
       "L’excédent courant s’accroît, d’autant que la banque centrale limite "
       "l’appréciation du yuan"],
  exp="L’excédent chinois reflète donc en partie un modèle de croissance "
      "déséquilibré, dans lequel la production progresse plus rapidement que "
      "la consommation intérieure. Le rééquilibrage suppose de réduire le "
      "poids de l’investissement productif et de renforcer la protection "
      "sociale et les services afin de stimuler la consommation.",
  diss="À mettre en regard des recommandations faites aux autres pôles : "
       "assainissement budgétaire aux États-Unis, mobilisation de l’épargne "
       "vers l’investissement en Europe."),

f(id='q21-n39', sp='c21-09', niv='raisonner', type='courte', b=3244,
  q="Pourquoi les déséquilibres mondiaux inquiètent-ils aujourd’hui ?",
  ans={'modele': "Pour trois raisons. D’abord parce qu’ils révèlent des "
       "fragilités internes susceptibles de se transformer en crises "
       "économiques ou financières : ils ne sont pas de simples anomalies "
       "comptables mais le reflet de modèles de croissance déséquilibrés. "
       "Ensuite à cause du précédent de 2008 : des déséquilibres extérieurs "
       "importants combinés à une forte intégration financière peuvent "
       "transformer une crise locale en crise mondiale. Enfin parce qu’ils "
       "alimentent les tensions protectionnistes, en nourrissant les "
       "accusations de concurrence déloyale. Le cours ajoute deux nouveautés "
       "inquiétantes : ces déséquilibres sont de plus en plus financés par "
       "des institutions financières non bancaires, plus enclines au risque "
       "et moins strictement encadrées que les banques par les dispositifs "
       "prudentiels ; et les capitaux étrangers se dirigent davantage vers "
       "les actions, notamment technologiques américaines, ce qui accroît le "
       "risque systémique si les valorisations liées à l’intelligence "
       "artificielle se révélaient excessives. S’y ajoute l’interrogation "
       "croissante sur la soutenabilité de la dette américaine, supérieure à "
       "120 % du PIB.",
       'cles': [{'f': ['fragilite interne', 'modele', 'desequilibre'],
                 'l': 'ils révèlent des fragilités internes'},
                {'f': ['2008', 'precedent', 'systemique', 'mondiale'],
                 'l': 'le précédent de 2008 et le risque systémique'},
                {'f': ['protectionnis', 'tension', 'deloyale'],
                 'l': 'ils alimentent les tensions protectionnistes'},
                {'f': ['non bancaire', 'nbfi', 'regulation', 'action', 'technologique'],
                 'l': 'un financement par des acteurs non bancaires et une concentration sur les actions'}]},
  exp="Le cours conclut que les déséquilibres contemporains sont moins "
      "préoccupants par leur niveau — ils n’ont pas retrouvé les sommets "
      "d’avant 2008 — que par les fragilités qu’ils révèlent et par la nature "
      "de leur financement."),

f(id='q21-n40', sp='c21-09', niv='comprendre', type='qcm', b=3173,
  q="À quoi servent les avoirs de réserve détenus par une banque centrale ?",
  opts=["À financer directement le budget de l’État",
        "À constituer un stock de devises mobilisable pour faire face aux "
        "besoins de paiements extérieurs ou aux tensions financières",
        "À garantir les dépôts bancaires domestiques",
        "À rémunérer les actionnaires de la banque centrale"],
  ans=1,
  why=["Le financement du budget relève du Trésor et des marchés "
       "obligataires.",
       "La garantie des dépôts repose sur des dispositifs distincts.",
       "Une banque centrale ne distribue pas de dividendes dans cette "
       "logique."],
  exp="Lorsque les capitaux privés cessent d’entrer, les réserves peuvent "
      "temporairement financer le déficit extérieur — mais leur épuisement "
      "conduit à une crise de paiement : c’est ce qui s’est produit au "
      "Mexique en 1982. À l’inverse, les économies excédentaires accumulent "
      "devises et actifs étrangers, parfois gérés par des fonds souverains "
      "chargés de placer cette épargne sur les marchés internationaux.",
  diss="Symétrie utile : les réserves sont le dernier amortisseur du pays "
       "déficitaire et le produit de l’excédent chez le pays créancier."),

]
