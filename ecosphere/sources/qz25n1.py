# -*- coding: utf-8 -*-
"""Chapitre 25 — questions nouvelles, économie ouverte (c25-11 à c25-18)."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c25-11
f(id='q25-n01', sp='c25-11', niv='connaitre', type='qcm', b=2368,
  q="À qui le modèle IS-LM-BP est-il attribué ?",
  opts=["Hicks et Hansen",
        "Mundell et Fleming",
        "Samuelson et Solow",
        "Barro et Friedman"],
  ans=1,
  why=["Hicks formalise IS-LM en 1937 et Hansen le prolonge en 1941, mais en "
       "économie fermée.",
       "Samuelson et Solow reformulent la courbe de Phillips en 1960.",
       "Barro et Friedman sont à l’origine des critiques de la relance, non "
       "du modèle ouvert."],
  exp="On parle du modèle de Mundell-Fleming : il complète IS-LM par une "
      "troisième courbe, BP, qui représente les conditions de l’équilibre "
      "extérieur. L’ajout est nécessaire parce que l’ouverture introduit les "
      "exportations et les importations dans la demande globale, les "
      "mouvements internationaux de capitaux et les interventions des banques "
      "centrales sur le marché des changes.",
  diss="Progression des trois modèles à annoncer : IS-LM pour l’économie "
       "fermée, OG-DG pour les prix, IS-LM-BP pour l’économie ouverte."),

f(id='q25-n02', sp='c25-11', niv='comprendre', type='qcm', b=2360,
  q="Comment l’ouverture modifie-t-elle l’équilibre keynésien sur le marché "
    "des biens et services ?",
  opts=["Elle supprime la notion de demande globale",
        "Elle introduit les exportations et les importations dans la demande "
        "globale, de sorte que les variations du taux de change peuvent "
        "déplacer IS",
        "Elle rend l’investissement indépendant du taux d’intérêt",
        "Elle supprime la courbe LM"],
  ans=1,
  why=["La demande globale subsiste : elle est seulement complétée.",
       "L’investissement reste sensible au taux d’intérêt : c’est la pente de "
       "IS.",
       "LM demeure : le marché de la monnaie reste représenté."],
  exp="Les exportations correspondent à une demande étrangère adressée à la "
      "production nationale ; les importations correspondent à une partie de "
      "la demande intérieure satisfaite par des producteurs étrangers. "
      "L’ouverture introduit donc une nouvelle composante de la demande, qui "
      "dépend notamment du taux de change — sous réserve que les volumes "
      "échangés réagissent suffisamment aux variations de prix.",
  diss="Condition à mentionner systématiquement : la réaction des volumes, "
       "qui renvoie aux élasticités-prix et à l’effet de courbe en J."),

f(id='q25-n03', sp='c25-11', niv='raisonner', type='qcm', b=2320,
  q="Pourquoi l’ajout de la courbe BP change-t-il la nature du problème de "
    "politique économique ?",
  opts=["Parce qu’il supprime la contrainte budgétaire",
        "Parce qu’une économie peut être à l’équilibre sur ses marchés "
        "intérieurs tout en connaissant un déséquilibre extérieur",
        "Parce qu’il rend la politique monétaire toujours efficace",
        "Parce qu’il élimine l’effet d’éviction"],
  ans=1,
  why=["La contrainte budgétaire n’est pas l’objet du modèle.",
       "L’efficacité de la politique monétaire dépend précisément du régime "
       "de change : elle n’est pas garantie.",
       "L’effet d’éviction subsiste, et s’enrichit même d’une éviction par le "
       "taux de change."],
  exp="Un déséquilibre extérieur entraîne alors une dépréciation ou une "
      "appréciation de la monnaie, des mouvements de réserves et des "
      "contraintes sur les politiques économiques. Les autorités ne peuvent "
      "donc plus rechercher le seul équilibre interne : la contrainte "
      "extérieure devient un paramètre de la décision, ce qui conduit aux "
      "dilemmes et à la règle d’affectation.",
  diss="Formule de synthèse : avec l’ouverture, le nombre d’objectifs "
       "augmente plus vite que le nombre d’instruments."),

# ------------------------------------------------------------- c25-12
f(id='q25-n04', sp='c25-12', niv='appliquer', type='assoc', b=2582,
  q="Associez chaque degré de mobilité des capitaux à la pente de la courbe "
    "BP qui en résulte.",
  ans=[["Mobilité parfaite : la moindre différence de rendement provoque des "
        "mouvements considérables", "BP horizontale"],
       ["Mobilité imparfaite : les capitaux réagissent mais partiellement au "
        "différentiel de taux", "BP croissante"],
       ["Absence totale de mobilité : aucun capital ne circule, l’équilibre "
        "extérieur exige l’équilibre courant", "BP verticale"]],
  exp="La logique est toujours la même : une hausse du revenu accroît les "
      "importations et dégrade le solde courant, ce qui exige des entrées de "
      "capitaux, donc un taux d’intérêt plus élevé. Plus les capitaux sont "
      "mobiles, moins il faut élever le taux pour les attirer — jusqu’au cas "
      "limite où le taux domestique s’aligne exactement sur le taux mondial, "
      "r = r*.",
  diss="Conséquence décisive : plus BP est horizontale, plus le triangle des "
       "incompatibilités mord, et plus le régime de change détermine "
       "l’efficacité des politiques."),

f(id='q25-n05', sp='c25-12', niv='comprendre', type='qcm', b=2634,
  q="En quoi les « trois D » de Bourguinat rendent-ils la courbe BP plus "
    "horizontale ?",
  opts=["Parce qu’ils réduisent les échanges de biens",
        "Parce que déréglementation, décloisonnement et désintermédiation "
        "accroissent la mobilité internationale des capitaux",
        "Parce qu’ils stabilisent les taux de change",
        "Parce qu’ils suppriment les banques"],
  ans=1,
  why=["Les échanges de biens ne sont pas réduits : la globalisation "
       "financière accompagne leur essor.",
       "Les taux de change deviennent au contraire plus volatils.",
       "La désintermédiation réduit le poids relatif des banques sans les "
       "supprimer."],
  exp="La déréglementation lève les restrictions sur les opérations "
      "financières, le décloisonnement relie des marchés auparavant séparés, "
      "la désintermédiation favorise les financements directs. L’effet "
      "commun est d’accroître la réactivité des capitaux aux écarts de "
      "rendement : BP tend vers l’horizontale, de sorte que le taux "
      "domestique ne peut plus s’écarter durablement du taux mondial.",
  diss="Articulation forte : ce sont ces transformations qui donnent au "
       "triangle de Mundell sa portée pratique contemporaine."),

f(id='q25-n06', sp='c25-12', niv='appliquer', type='ordre', b=2523,
  q="Remettez dans l’ordre le raisonnement qui établit la pente croissante "
    "de BP.",
  ans=["On part d’un point d’équilibre de la balance globale",
       "Le revenu national augmente, le taux d’intérêt restant inchangé",
       "Les importations augmentent et le solde courant se dégrade",
       "Faute d’entrées de capitaux supplémentaires, la balance globale "
       "devient déficitaire",
       "Pour rétablir l’équilibre, il faut attirer des capitaux, donc élever "
       "le taux d’intérêt"],
  exp="Chaque niveau de revenu plus élevé exige donc un taux d’intérêt plus "
      "élevé : la courbe BP est croissante. Les points situés au-dessous "
      "correspondent à un déficit de la balance globale — le taux d’intérêt y "
      "est insuffisant pour financer le besoin extérieur — et les points "
      "situés au-dessus à un excédent.",
  diss="Méthode de lecture graphique à systématiser : repérer d’abord la "
       "position du point par rapport à BP, puis en déduire le sens de "
       "l’ajustement."),

# ------------------------------------------------------------- c25-13
f(id='q25-n07', sp='c25-13', niv='appliquer', type='ordre', b=2726,
  q="Remettez dans l’ordre l’ajustement imposé par un déficit extérieur en "
    "changes fixes.",
  ans=["L’économie connaît un déficit extérieur",
       "La monnaie nationale subit une pression à la dépréciation",
       "La banque centrale achète sa propre monnaie et vend des devises "
       "prélevées sur ses réserves",
       "L’offre de monnaie diminue et LM se déplace vers la gauche",
       "Le taux d’intérêt augmente et l’activité ralentit, ce qui réduit les "
       "importations"],
  exp="L’ajustement extérieur se réalise donc au prix d’un ralentissement de "
      "l’activité : le déficit extérieur peut imposer une politique monétaire "
      "restrictive, même si l’économie connaît déjà une activité "
      "insuffisante. C’est la contrainte extérieure dans sa forme la plus "
      "directe.",
  diss="Conclusion de fond : en changes fixes, la politique monétaire devient "
       "endogène, puisqu’elle est commandée par la défense de la parité."),

f(id='q25-n08', sp='c25-13', niv='comprendre', type='qcm', b=2733,
  q="Que fait une banque centrale en changes fixes lorsque sa monnaie subit "
    "une pression à l’appréciation ?",
  opts=["Elle achète sa propre monnaie et vend des devises",
        "Elle vend sa propre monnaie et achète des devises, ce qui accroît la "
        "liquidité domestique",
        "Elle augmente ses taux directeurs",
        "Elle laisse la monnaie s’apprécier"],
  ans=1,
  why=["Acheter sa propre monnaie accentuerait la pression à "
       "l’appréciation : c’est la réponse à un déficit.",
       "La hausse des taux directeurs attirerait davantage de capitaux, donc "
       "aggraverait la pression.",
       "Laisser la monnaie s’apprécier reviendrait à abandonner la parité, "
       "c’est-à-dire à passer en changes flexibles."],
  exp="L’excédent extérieur se traduit donc par une expansion monétaire "
      "automatique, qui peut réduire l’excédent en stimulant l’activité et "
      "les importations. Le cours apporte toutefois une nuance importante : "
      "les banques centrales peuvent parfois stériliser les effets "
      "monétaires de leurs interventions, même si le modèle simplifié suppose "
      "qu’elles modifient directement LM.",
  diss="Symétrie à retenir : déficit → contraction monétaire, excédent → "
       "expansion monétaire — sauf stérilisation."),

f(id='q25-n09', sp='c25-13', niv='appliquer', type='assoc', b=2891,
  q="Classez chaque configuration selon qu’elle constitue ou non un dilemme "
    "de politique économique.",
  ans=[["Sous-emploi et déficit extérieur", "Dilemme"],
       ["Tensions inflationnistes et excédent extérieur", "Dilemme"],
       ["Sous-emploi et excédent extérieur", "Pas de dilemme"],
       ["Tensions inflationnistes et déficit extérieur", "Pas de dilemme"]],
  exp="Il y a dilemme lorsque la politique qui corrige le déséquilibre "
      "interne aggrave le déséquilibre externe. En sous-emploi avec déficit, "
      "une relance réduirait le chômage mais creuserait le déficit ; en "
      "inflation avec excédent, une politique restrictive calmerait les prix "
      "mais gonflerait encore l’excédent. Dans les deux autres cas, une même "
      "orientation améliore les deux équilibres.",
  diss="Outil d’analyse de Jacques Généreux à mobiliser : comparer le revenu "
       "de plein emploi Ype et le revenu équilibrant les transactions "
       "courantes YBTC."),

# ------------------------------------------------------------- c25-14
f(id='q25-n10', sp='c25-14', niv='raisonner', type='courte', b=3085,
  q="Pourquoi la relance française de 1981 constitue-t-elle une illustration "
    "des limites d’une politique nationale non coordonnée ?",
  ans={'modele': "Parce que son échec ne tient pas à une erreur de "
       "raisonnement keynésien mais au contexte dans lequel elle est "
       "appliquée. Le gouvernement de Pierre Mauroy soutient la demande "
       "intérieure — hausse du SMIC, revalorisation des prestations sociales, "
       "créations d’emplois publics — mais la croissance des partenaires "
       "commerciaux est faible et l’inflation française déjà très élevée, "
       "autour de 13 % en 1981 et 12 % en 1982. Or en économie ouverte le "
       "multiplicateur devient 1/(1 − c + m) : une partie de la demande "
       "supplémentaire s’adresse aux producteurs étrangers. Comme les "
       "partenaires ne relancent pas simultanément, la demande étrangère "
       "n’augmente pas en retour : les importations progressent, les "
       "exportations non, et les comptes extérieurs se dégradent. La "
       "contrainte extérieure devient alors décisive, puisque le maintien du "
       "franc dans le Système monétaire européen impose un choix. En mars "
       "1983, le gouvernement y renonce à la stratégie de relance : c’est le "
       "tournant de la rigueur. Une relance coordonnée entre partenaires "
       "aurait au contraire limité les fuites, chaque pays bénéficiant de la "
       "demande supplémentaire des autres.",
       'cles': [{'f': ['1981', 'mauroy', 'smic', 'prestation'],
                 'l': "la relance de 1981 et ses instruments"},
                {'f': ['partenaire', 'faible', 'non coordonn', 'seul'],
                 'l': "une relance isolée, dans un environnement peu porteur"},
                {'f': ['importation', 'fuite', 'multiplicateur', 'etranger'],
                 'l': "les fuites par les importations"},
                {'f': ['inflation', '13', '12'],
                 'l': "une inflation déjà élevée"},
                {'f': ['exterieur', 'deficit', 'contrainte', 'sme', 'franc'],
                 'l': "la dégradation des comptes extérieurs et la contrainte de change"},
                {'f': ['1983', 'rigueur', 'tournant'],
                 'l': "le tournant de mars 1983"},
                {'f': ['coordination', 'coordonn', 'simultan'],
                 'l': "l'intérêt d'une relance coordonnée"}]},
  exp="La relance intervient alors que la croissance des partenaires est "
      "faible et l’inflation française déjà élevée : une partie du "
      "multiplicateur profite aux producteurs étrangers et les comptes "
      "extérieurs se dégradent.",
  diss="Exemple à double usage : il illustre la fuite par les importations et "
       "la contrainte extérieure en changes quasi fixes."),

f(id='q25-n11', sp='c25-14', niv='raisonner', type='qcm', b=3051,
  q="Que montre l’exemple japonais sur l’autonomie des politiques en changes "
    "flexibles ?",
  opts=["Les changes flexibles suppriment toute contrainte extérieure",
        "Même en changes flexibles, un arbitrage demeure : une politique "
        "monétaire accommodante soutient l’activité mais accentue les "
        "pressions à la dépréciation, qui renchérissent les importations",
        "La politique monétaire devient inefficace",
        "L’inflation ne dépend que de la monnaie"],
  ans=1,
  why=["C’est précisément ce que l’exemple dément : la contrainte change de "
       "forme, elle ne disparaît pas.",
       "La politique monétaire est au contraire efficace en changes "
       "flexibles : c’est son coût qui est en question.",
       "Le caractère purement monétaire de l’inflation est une thèse "
       "monétariste, étrangère à cet exemple."],
  exp="Le mécanisme est le suivant : une monnaie abondante réduit "
      "l’attractivité des placements en yens, ce qui alimente les sorties de "
      "capitaux et la dépréciation ; celle-ci stimule les exportations nettes "
      "mais renchérit les importations, notamment énergétiques. L’autonomie "
      "nominale offerte par les changes flexibles ne supprime donc pas "
      "l’arbitrage réel entre soutien de l’activité et coût des importations.",
  diss="Nuance à apporter au résultat de Mundell-Fleming : l’efficacité de la "
       "politique monétaire en changes flexibles ne signifie pas son absence "
       "de coût."),

f(id='q25-n12', sp='c25-14', niv='comprendre', type='vf', b=2964,
  q="Le tournant de la rigueur de 1983 résulte du choix de maintenir le franc "
    "dans le Système monétaire européen.",
  ans=True,
  exp="En mars 1983, le gouvernement doit choisir entre poursuivre la relance "
      "— ce qui supposait d’accepter une sortie du Système monétaire européen "
      "et une dépréciation du franc — et maintenir la parité, ce qui "
      "impliquait l’abandon de la stratégie de relance et le passage à une "
      "politique plus restrictive. C’est la seconde option qui est retenue. "
      "L’épisode illustre exactement la logique du triangle de Mundell : la "
      "stabilité du change et la libre circulation croissante des capitaux "
      "limitent l’autonomie des politiques nationales.",
  diss="Lecture théorique de l’épisode : c’est un arbitrage de triangle, non "
       "un simple changement de doctrine économique."),

# ------------------------------------------------------------- c25-15
f(id='q25-n13', sp='c25-15', niv='appliquer', type='ordre', b=3212,
  q="Remettez dans l’ordre les effets d’une relance budgétaire en changes "
    "fixes avec mobilité parfaite des capitaux.",
  ans=["La hausse des dépenses publiques déplace IS vers la droite",
       "Le revenu augmente, la demande de monnaie aussi, et le taux d’intérêt "
       "dépasse le taux mondial",
       "Les capitaux entrent, créant une pression à l’appréciation de la "
       "monnaie",
       "Pour défendre la parité, la banque centrale achète des devises et "
       "émet de la monnaie",
       "LM se déplace vers la droite et le revenu augmente davantage encore"],
  exp="La politique budgétaire est donc très efficace dans ce régime : elle "
      "bénéficie d’un accompagnement monétaire automatique, puisque la "
      "défense de la parité oblige la banque centrale à créer de la monnaie. "
      "C’est le résultat exactement inverse de celui obtenu en changes "
      "flexibles, où l’appréciation évince les exportations nettes.",
  diss="Tableau à mémoriser : en changes fixes, budget efficace et monnaie "
       "inefficace ; en changes flexibles, l’inverse."),

f(id='q25-n14', sp='c25-15', niv='raisonner', type='courte', b=3224,
  q="Comment le triangle de Mundell éclaire-t-il le système de Bretton Woods "
    "puis la création de l’euro ?",
  ans={'modele': "Le triangle énonce qu’un État ne peut concilier pleinement "
       "que deux des trois objectifs suivants : changes fixes, libre "
       "circulation des capitaux, politique monétaire autonome. Bretton Woods "
       "sacrifie le troisième sommet au sens où il limite la mobilité des "
       "capitaux : les contrôles permettent de conserver à la fois des "
       "parités fixes et une certaine autonomie monétaire nationale. À partir "
       "des années 1980, les pays européens renforcent au contraire la libre "
       "circulation des capitaux tout en recherchant la stabilité de leurs "
       "changes : les deux objectifs retenus étant désormais les changes "
       "fixes et la mobilité, l’autonomie monétaire nationale devient "
       "intenable. Une politique trop expansionniste provoque des sorties de "
       "capitaux, donc une pression à la dépréciation, donc l’obligation de "
       "resserrer pour défendre la parité : les politiques monétaires "
       "nationales deviennent fortement interdépendantes. La monnaie unique "
       "peut alors se lire comme une réponse institutionnelle à cette "
       "interdépendance : les États renoncent à une autonomie qu’ils avaient "
       "déjà perdue en fait, et obtiennent en échange une participation à la "
       "décision commune.",
       'cles': [{'f': ['trois objectif', 'changes fixes', 'mobilite',
                       'autonomie'],
                 'l': "les trois sommets du triangle"},
                {'f': ['deux', 'jamais les trois', 'sacrifi'],
                 'l': "deux objectifs au maximum"},
                {'f': ['bretton woods', 'controle des capitaux', 'limite'],
                 'l': "Bretton Woods limite la mobilité des capitaux"},
                {'f': ['annees 1980', 'liberalisation', 'sme',
                       'stabilite des change'],
                 'l': "l'Europe choisit mobilité et stabilité des changes"},
                {'f': ['interdependance', 'sortie de capitaux', 'resserr',
                       'perdue'],
                 'l': "l'autonomie monétaire nationale devient intenable"},
                {'f': ['monnaie unique', 'euro', 'reponse institutionnelle',
                       'commune'],
                 'l': "l'euro comme réponse institutionnelle"}]},
  exp="Le triangle montre que l’intégration financière impose un arbitrage "
      "entre stabilité du change et souveraineté monétaire : Bretton Woods "
      "résout l’arbitrage par le contrôle des capitaux, l’Europe par la "
      "mutualisation de la politique monétaire.",
  diss="Enchaînement historique très valorisable : contrôle des capitaux, "
       "puis libéralisation, puis monnaie unique — trois réponses au même "
       "triangle."),

f(id='q25-n15', sp='c25-15', niv='comprendre', type='qcm', b=3159,
  q="Pourquoi la politique monétaire est-elle inefficace en changes fixes "
    "avec mobilité parfaite des capitaux ?",
  opts=["Parce que la banque centrale ne peut pas augmenter l’offre de "
        "monnaie",
        "Parce que la défense de la parité l’oblige à racheter sa monnaie, ce "
        "qui annule l’expansion initiale",
        "Parce que les agents thésaurisent toute monnaie supplémentaire",
        "Parce que l’investissement est insensible au taux d’intérêt"],
  ans=1,
  why=["Elle peut parfaitement l’augmenter : c’est l’effet qui est annulé, "
       "non la décision qui est empêchée.",
       "La thésaurisation caractérise la trappe à liquidité, en économie "
       "fermée.",
       "L’insensibilité de l’investissement au taux est une autre hypothèse, "
       "étrangère à ce cas."],
  exp="L’enchaînement est le suivant : LM se déplace vers la droite, le taux "
      "domestique devient inférieur au taux mondial, les capitaux sortent, la "
      "monnaie subit une pression à la dépréciation, la banque centrale "
      "achète sa propre monnaie pour défendre la parité, la masse monétaire "
      "diminue et LM revient à sa position initiale. L’autonomie monétaire "
      "est donc nulle : c’est le sommet du triangle que ce régime sacrifie.",
  diss="Conséquence institutionnelle : la politique monétaire devient un "
      "instrument de l’équilibre externe, ce qui justifie la règle "
      "d’affectation de Mundell."),

# ------------------------------------------------------------- c25-16
f(id='q25-n16', sp='c25-16', niv='appliquer', type='ordre', b=3380,
  q="Remettez dans l’ordre les effets d’une expansion monétaire en changes "
    "flexibles avec mobilité parfaite des capitaux.",
  ans=["La banque centrale augmente l’offre de monnaie et LM se déplace vers "
       "la droite",
       "Le taux d’intérêt domestique devient inférieur au taux mondial",
       "Les capitaux sortent et la monnaie se déprécie, la banque centrale "
       "n’étant pas tenue de défendre une parité",
       "La dépréciation rend les produits nationaux moins chers et les "
       "importations plus chères : les exportations nettes augmentent",
       "IS se déplace vers la droite, le revenu augmente encore et le taux "
       "d’intérêt remonte vers le niveau mondial"],
  exp="L’expansion monétaire produit donc deux effets successifs : un effet "
      "sur le marché monétaire, puis un effet sur les exportations nettes par "
      "l’intermédiaire du taux de change. C’est la combinaison des deux qui "
      "explique la forte efficacité de la politique monétaire dans ce régime. "
      "Le nouvel équilibre se caractérise par une production plus élevée et "
      "un taux d’intérêt revenu au niveau international.",
  diss="Condition à ne pas oublier : la hausse des exportations nettes "
       "suppose une réaction suffisante des volumes échangés."),

f(id='q25-n17', sp='c25-16', niv='raisonner', type='qcm', b=3348,
  q="Qu’est-ce qui distingue fondamentalement l’ajustement en changes "
    "flexibles de celui en changes fixes ?",
  opts=["Les capitaux ne circulent pas en changes flexibles",
        "La banque centrale n’est pas obligée de défendre une parité : le "
        "taux de change devient lui-même le mécanisme d’ajustement",
        "Le taux d’intérêt domestique est indépendant du taux mondial",
        "Les exportations ne dépendent plus du taux de change"],
  ans=1,
  why=["Les capitaux circulent dans les deux régimes : c’est l’hypothèse "
       "commune de mobilité parfaite.",
       "Le taux domestique revient au contraire au niveau mondial à "
       "l’équilibre final.",
       "Les exportations dépendent précisément du taux de change, et c’est "
       "ce qui rend l’ajustement possible."],
  exp="En changes fixes, c’est la masse monétaire qui s’ajuste pour maintenir "
      "la parité, de sorte que l’autonomie monétaire disparaît. En changes "
      "flexibles, c’est le taux de change qui s’ajuste, ce qui libère la "
      "politique monétaire et lui donne un second canal d’action. "
      "Symétriquement, ce même canal neutralise la politique budgétaire, par "
      "l’appréciation qu’une relance provoque.",
  diss="Principe unificateur à énoncer : dans les deux régimes, quelque chose "
       "doit s’ajuster — soit la monnaie, soit le change."),

f(id='q25-n18', sp='c25-16', niv='raisonner', type='vf', b=3327,
  q="Le triangle des incompatibilités de Mundell interdit la libre "
    "circulation des capitaux.",
  ans=False,
  exp="Le triangle n’interdit aucun objectif en particulier : il établit "
      "qu’on ne peut en poursuivre pleinement que deux sur trois. Un pays "
      "peut parfaitement autoriser la libre circulation des capitaux, à "
      "condition de renoncer soit à la fixité du change — c’est le régime de "
      "changes flexibles —, soit à l’autonomie monétaire — c’est le cas des "
      "membres d’une union monétaire. Le triangle est donc un outil "
      "d’analyse des arbitraires possibles, non une prescription.",
  diss="Trois combinaisons à savoir citer : changes flexibles et autonomie, "
       "changes fixes et contrôle des capitaux (Bretton Woods), union "
       "monétaire et mobilité (zone euro)."),

]
