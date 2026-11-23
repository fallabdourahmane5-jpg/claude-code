# -*- coding: utf-8 -*-
"""Chapitre 22 — questions nouvelles, sous-parties c22-12 et c22-14."""


def f(**kw):
    return kw


L = [

# ------------------------------------------------------------- c22-12
f(id='q22-n28', sp='c22-12', niv='comprendre', type='qcm', b=4222,
  q="Que désigne l’expression « industrie infantile qui ne devient jamais "
    "adulte » ?",
  opts=["Une industrie récente dont les produits s’adressent aux enfants",
        "Une industrie protégée de façon permanente, qui ne parvient jamais à "
        "devenir compétitive par elle-même",
        "Une industrie qui refuse d’exporter",
        "Une industrie dont les salariés sont très jeunes"],
  ans=1,
  why=["L’expression ne porte pas sur la clientèle mais sur la maturité "
       "économique du secteur.",
       "Le refus d’exporter peut être une conséquence, non la définition.",
       "L’âge des salariés n’a rien à voir avec cette image."],
  exp="C’est le premier risque de la politique industrielle : protéger "
      "éternellement une industrie inefficace. Le soutien aux industries "
      "naissantes n’est efficace que s’il est conditionnel et temporaire ; "
      "sinon la protection entretient des rentes et maintient "
      "artificiellement des entreprises durablement inefficaces. L’image est "
      "parlante : l’industrie reste indéfiniment au stade où elle a besoin "
      "d’être protégée.",
  diss="À opposer directement au cas de l’automobile japonaise, où "
       "l’échéance de la protection était connue et crédible."),

f(id='q22-n29', sp='c22-12', niv='raisonner', type='qcm', b=4244,
  q="En quoi consiste le deuxième risque d’une politique industrielle, "
    "particulièrement important quand le progrès technique s’accélère ?",
  opts=["Soutenir la technologie d’hier plutôt que celle qui définira la "
        "prochaine frontière productive",
        "Dépenser trop peu d’argent public",
        "Soutenir uniquement des entreprises étrangères",
        "Financer la recherche fondamentale au détriment de la recherche "
        "appliquée"],
  ans=0,
  why=["L’insuffisance des moyens est une autre limite, traitée par le "
       "trilemme d’Agarwal.",
       "Le soutien aux entreprises étrangères n’est pas le risque identifié "
       "ici.",
       "L’arbitrage entre recherche fondamentale et appliquée n’est pas "
       "l’objet de ce risque."],
  exp="Une politique de rattrapage mal ciblée peut entretenir un retard "
      "technologique si elle subventionne les technologies existantes plutôt "
      "que celles susceptibles de définir la prochaine frontière productive. "
      "Le cours donne un exemple sanitaire : maîtriser une technologie "
      "pharmaceutique ne garantit pas de maîtriser les technologies les plus "
      "récentes du domaine biotechnologique, donc pas davantage sa position "
      "dans la prochaine rupture technologique.",
  diss="À relier au diagnostic de Sarah Guillou sur les champions français "
       "restés dans le « mid-tech »."),

f(id='q22-n30', sp='c22-12', niv='appliquer', type='ordre', b=4260,
  q="Remettez dans l’ordre le schéma de construction d’un avantage "
    "comparatif nouveau.",
  ans=["Le pays ne dispose d’aucun avantage initial dans l’activité "
       "considérée",
       "Un investissement public est engagé",
       "Des compétences se constituent",
       "Des entreprises se développent dans le secteur",
       "Des économies d’échelle apparaissent, puis l’innovation",
       "Un avantage comparatif nouveau est acquis"],
  exp="C’est le schéma retenu par le cours : pas d’avantage initial → "
      "investissement public → compétences → entreprises → économies "
      "d’échelle → innovation → avantage comparatif nouveau. Il fonde l’idée "
      "que la politique industrielle peut modifier la spécialisation future "
      "d’un pays, parce que l’investissement dans le capital humain, la "
      "technologie et les infrastructures transforme progressivement les "
      "coûts relatifs et les capacités productives.",
  diss="Exemple du cours : plusieurs pays asiatiques ont construit des "
       "avantages dans l’électronique, l’automobile ou certaines technologies "
       "avancées alors qu’ils ne les possédaient pas initialement."),

f(id='q22-n31', sp='c22-12', niv='comprendre', type='qcm', b=4281,
  q="Selon Aghion, quelle politique convient à un pays éloigné de la "
    "frontière technologique ?",
  opts=["Une politique essentiellement horizontale, centrée sur la "
        "concurrence et l’entrée de nouvelles entreprises",
        "Une politique laissant davantage de place au ciblage : cibler des "
        "secteurs, coordonner l’investissement, soutenir des champions, "
        "accélérer l’apprentissage",
        "Aucune politique industrielle",
        "Une politique exclusivement monétaire"],
  ans=1,
  why=["La priorité à la concurrence et à l’entrée concerne au contraire les "
       "pays proches de la frontière.",
       "Le renoncement à toute politique n’est pas la recommandation "
       "d’Aghion.",
       "La politique monétaire n’est pas l’objet de cette analyse."],
  exp="L’idée est essentielle : les mêmes politiques ne sont pas efficaces "
      "partout. Un pays éloigné de la frontière doit surtout rattraper, ce "
      "qui laisse une place plus importante à la politique verticale. Un pays "
      "proche ou situé à la frontière doit au contraire faire venir "
      "l’innovation de nouvelles entreprises, de l’expérimentation, de la "
      "concurrence et de la destruction créatrice : politique de concurrence, "
      "politique horizontale et soutien général à la R&D et au capital humain "
      "deviennent alors prioritaires.",
  diss="Conséquence utile : citer la Corée pour défendre le ciblage en France "
       "est une erreur d’altitude, puisque les deux économies ne sont pas à la "
       "même distance de la frontière."),

f(id='q22-n32', sp='c22-12', niv='appliquer', type='ordre', b=4294,
  q="Remettez dans l’ordre le mécanisme par lequel la concurrence repousse la "
    "frontière technologique, dans l’approche d’Aghion.",
  ans=["La pression concurrentielle augmente",
       "De nouvelles entreprises entrent sur le marché",
       "L’effort d’innovation s’intensifie",
       "La destruction créatrice élimine les activités dépassées",
       "La frontière technologique est repoussée"],
  exp="C’est le mécanisme du cours : concurrence ↑ → entrée de nouvelles "
      "entreprises → innovation ↑ → destruction créatrice → frontière "
      "technologique repoussée. Il explique pourquoi, près de la frontière, "
      "la politique de concurrence devient un instrument d’innovation et pas "
      "seulement de protection du consommateur. Mais le cours précise que "
      "même à la frontière, l’intervention publique ne disparaît pas.",
  diss="Pivot de la synthèse néo-schumpétérienne : la concurrence n’est pas "
       "l’adversaire de la politique industrielle, elle en est la condition "
       "d’efficacité."),

f(id='q22-n33', sp='c22-12', niv='comprendre', type='qcm', b=4304,
  q="Quelle est la logique de la justification néoclassique de la politique "
    "industrielle ?",
  opts=["L’État intervient parce qu’il sait mieux produire que les "
        "entreprises",
        "L’État intervient parce que le marché n’aboutit pas spontanément à "
        "une allocation efficace",
        "L’État intervient pour redistribuer les revenus",
        "L’État intervient pour réduire le déficit commercial"],
  ans=1,
  why=["Le cours écarte explicitement cette idée : l’État n’intervient pas "
       "parce qu’il « sait mieux produire ».",
       "La redistribution relève de la politique sociale et fiscale, non de "
       "cette justification.",
       "Le solde commercial n’est pas le fondement de cet argument."],
  exp="La justification néoclassique repose entièrement sur la notion de "
      "défaillance de marché : l’intervention se légitime là où le marché "
      "laissé à lui-même produit un résultat inefficace. Trois défaillances "
      "sont développées par le cours : les asymétries d’information dans le "
      "financement de l’innovation, les externalités positives de la R&D, et "
      "les problèmes de coordination entre investissements complémentaires.",
  diss="Conséquence méthodologique : une bonne politique industrielle doit "
       "nommer la défaillance qu’elle corrige — sinon elle n’est qu’une "
       "dépense."),

f(id='q22-n34', sp='c22-12', niv='comprendre', type='qcm', b=4329,
  q="Pourquoi l’asymétrie d’information peut-elle empêcher le financement de "
    "projets innovants rentables ?",
  opts=["Parce que l’innovateur ignore la valeur de son propre projet",
        "Parce que l’investisseur ne peut pas correctement évaluer le risque "
        "du projet, ce qui conduit à un rationnement du crédit",
        "Parce que les banques sont légalement interdites de financer "
        "l’innovation",
        "Parce que les projets innovants sont toujours déficitaires"],
  ans=1,
  why=["C’est l’inverse : l’innovateur en sait davantage que le financeur, "
       "d’où l’asymétrie.",
       "Aucune interdiction légale n’existe.",
       "De nombreux projets innovants sont rentables : c’est précisément ce "
       "qui rend le rationnement coûteux."],
  exp="L’asymétrie d’information entre innovateurs et financeurs peut "
      "provoquer un rationnement du crédit : des projets potentiellement "
      "rentables ne sont pas financés parce que l’investisseur ne peut "
      "correctement évaluer leur risque. Deux instruments en découlent : "
      "favoriser le capital-risque, qui accepte un risque élevé en échange "
      "d’une rentabilité potentielle forte, et faire intervenir une "
      "institution publique partageant le risque initial.",
  diss="Attention à la limite signalée par le cours : plus le capital-risque "
       "se développe, plus les pertes potentielles et les bulles peuvent être "
       "importantes."),

f(id='q22-n35', sp='c22-12', niv='connaitre', type='qcm', b=4353,
  q="Depuis quand la Banque publique d’investissement — Bpifrance — "
    "existe-t-elle ?",
  opts=["2008",
        "2013",
        "2019",
        "1983"],
  ans=1,
  why=["2008 est l’année de la réforme du Crédit d’impôt recherche.",
       "2019 correspond à la transformation du CICE en allègements de "
       "cotisations.",
       "1983 est l’année de création du Crédit d’impôt recherche."],
  exp="Bpifrance existe depuis 2013. Sa logique est de corriger les "
      "imperfections du financement privé en partageant le risque initial : "
      "en acceptant d’intervenir sur un projet, l’institution publique "
      "réduit le risque perçu par les investisseurs privés et envoie un "
      "signal susceptible d’attirer ensuite banques et investisseurs. Le "
      "financement public peut donc entraîner du financement privé.",
  diss="Mécanisme à nommer précisément : effet de levier et effet de signal, "
       "et non substitution du public au privé."),

f(id='q22-n36', sp='c22-12', niv='comprendre', type='qcm', b=4389,
  q="Pourquoi le marché investit-il spontanément trop peu en recherche ?",
  opts=["Parce que la recherche n’est pas rentable",
        "Parce que l’entreprise innovante ne peut généralement pas capter "
        "l’intégralité des bénéfices qu’elle produit : le rendement social "
        "dépasse le rendement privé",
        "Parce que les chercheurs sont trop peu nombreux",
        "Parce que les brevets sont interdits"],
  ans=1,
  why=["La recherche peut être très rentable : le problème est que sa "
       "rentabilité privée est inférieure à sa rentabilité sociale.",
       "La disponibilité des chercheurs n’est pas l’argument théorique "
       "mobilisé ici.",
       "Les brevets existent précisément pour permettre une appropriation "
       "partielle des bénéfices de l’innovation."],
  exp="L’innovation génère des externalités positives : les connaissances "
      "créées bénéficient à d’autres acteurs que l’innovateur. Le mécanisme "
      "est le suivant : innovation d’une entreprise → connaissance nouvelle → "
      "diffusion à d’autres acteurs → productivité générale ↑. Le rendement "
      "social de la R&D étant supérieur à son rendement privé, l’entreprise "
      "investit moins que ce qui serait collectivement optimal. Le soutien "
      "public vise alors à rapprocher l’investissement privé du niveau "
      "socialement optimal en internalisant une partie de ces externalités.",
  diss="Cette défaillance fonde directement le Crédit d’impôt recherche et le "
       "financement public de la recherche fondamentale."),

f(id='q22-n37', sp='c22-12', niv='raisonner', type='qcm', b=4433,
  q="En quoi consiste la défaillance de coordination qui peut justifier une "
    "politique industrielle ?",
  opts=["Les entreprises refusent de communiquer entre elles",
        "La rentabilité d’un investissement dépend de la réalisation "
        "simultanée d’autres investissements complémentaires, chacun "
        "attendant que les autres se décident",
        "L’État et les entreprises poursuivent des objectifs opposés",
        "Les salariés et les actionnaires ne s’entendent pas"],
  ans=1,
  why=["Il ne s’agit pas d’un défaut de communication mais d’une structure "
       "d’incitations.",
       "L’opposition entre État et entreprises n’est pas le problème décrit.",
       "Le conflit entre salariés et actionnaires relève d’une autre "
       "question, celle du partage de la valeur ajoutée."],
  exp="Certaines industries exigent plusieurs investissements simultanés : "
      "chaque acteur raisonne alors en se disant « je n’investis pas tant que "
      "les autres n’investissent pas ». L’investissement collectivement "
      "rentable n’est donc pas réalisé. La politique industrielle peut "
      "résoudre cette défaillance en coordonnant les décisions, par exemple "
      "en garantissant qu’une infrastructure ou une filière complémentaire "
      "existera bien.",
  diss="Cas d’école : la filière du véhicule électrique, où batteries, bornes "
       "de recharge, réseau et véhicules doivent progresser ensemble."),

f(id='q22-n38', sp='c22-12', niv='raisonner', type='qcmm', b=4459,
  q="Selon la logique Aghion-Cohen, dans quels cas un ciblage top-down est-il "
    "particulièrement justifié ? (plusieurs réponses)",
  opts=["Lorsque les coûts fixes sont élevés",
        "Lorsqu’il existe de fortes externalités",
        "Lorsque de nombreuses complémentarités d’investissement sont "
        "nécessaires",
        "Lorsque la technologie est stratégique",
        "Lorsqu’une technologie de rupture est trop risquée pour le privé "
        "seul",
        "Lorsque le secteur est déjà très concurrentiel et rentable"],
  ans=[0, 1, 2, 3, 4],
  why=["Exacte : les coûts fixes élevés dissuadent l’entrée privée isolée.",
       "Exacte : les externalités creusent l’écart entre rendement privé et "
       "rendement social.",
       "Exacte : les complémentarités créent un problème de coordination.",
       "Exacte : le caractère stratégique ajoute un enjeu de souveraineté.",
       "Exacte : le risque extrême justifie une prise de risque publique.",
       "Inexacte : un secteur déjà concurrentiel et rentable n’a pas besoin "
       "de coordination publique ciblée."],
  exp="Plus une activité cumule coûts fixes élevés, externalités, "
      "complémentarités d’investissement et incertitude technologique, plus "
      "la justification d’une coordination publique ciblée est forte. La "
      "réciproque est tout aussi importante : lorsque ces conditions sont "
      "absentes, le ciblage n’a pas de fondement et expose au risque d’erreur "
      "comme à la recherche de rente.",
  diss="Grille de test à appliquer à toute politique ciblée proposée : "
       "quelle défaillance précise justifie-t-elle le ciblage ?"),

f(id='q22-n39', sp='c22-12', niv='raisonner', type='courte', b=4495,
  q="Quelle leçon le précédent européen des panneaux solaires apporte-t-il à "
    "la politique industrielle verte ?",
  ans={'modele': "L’Europe a fortement soutenu la demande de panneaux "
       "solaires sans développer simultanément les capacités industrielles "
       "permettant de les produire. Résultat : la transition énergétique a été "
       "accélérée, mais la dépendance productive extérieure s’est renforcée, "
       "la demande européenne ayant largement été satisfaite par des "
       "producteurs étrangers. La leçon est qu’une politique climatique "
       "soutenant la seule demande peut atteindre son objectif "
       "environnemental tout en manquant son objectif industriel et de "
       "souveraineté. D’où le choix des politiques contemporaines — "
       "Inflation Reduction Act, projet d’Industrial Accelerator Act — de "
       "conditionner les aides au contenu local, de façon à soutenir "
       "simultanément la demande et l’offre domestique.",
       'cles': [{'f': ['demande', 'subvention a la demande', 'soutien a la demande'],
                 'l': "un soutien centré sur la demande"},
                {'f': ['capacite industrielle', 'offre', 'production domestique',
                       'produire'],
                 'l': "sans construction simultanée d'une offre industrielle"},
                {'f': ['dependance', 'importation', 'etranger', 'exterieur'],
                 'l': "un renforcement de la dépendance productive extérieure"},
                {'f': ['transition', 'climatique', 'energetique', 'accelere'],
                 'l': "un objectif climatique néanmoins atteint"},
                {'f': ['contenu local', 'ira', 'conditionn', 'preference'],
                 'l': "d'où la conditionnalité au contenu local aujourd'hui"}]},
  exp="Le précédent photovoltaïque montre qu’une politique climatique "
      "soutenant la demande sans construire simultanément une offre "
      "industrielle domestique peut accélérer la transition énergétique tout "
      "en renforçant la dépendance productive extérieure.",
  diss="Exemple extrêmement rentable en dissertation : il articule "
       "transition écologique, souveraineté et politique industrielle en un "
       "seul cas."),

f(id='q22-n40', sp='c22-12', niv='raisonner', type='qcmm', b=4564,
  q="Quelles conditions renforcent les chances de réussite d’une politique "
    "industrielle, selon le cours ? (plusieurs réponses)",
  opts=["Un objectif clairement identifié",
        "Un soutien répondant à une défaillance précise",
        "Des aides conditionnelles plutôt qu’une rente permanente",
        "Le maintien d’une concurrence suffisante",
        "La capacité de l’État à arrêter un projet en cas d’échec durable",
        "Un montant de dépense publique aussi élevé que possible"],
  ans=[0, 1, 2, 3, 4],
  why=["Exacte : innovation, rattrapage, souveraineté, emploi, transition — "
       "l’objectif doit être nommé.",
       "Exacte : externalité, asymétrie d’information, coordination.",
       "Exacte : la conditionnalité évite la rente permanente.",
       "Exacte : il s’agit d’éviter les monopoles inefficaces.",
       "Exacte : savoir arrêter permet de réallouer les ressources.",
       "Inexacte : une politique industrielle n’est pas efficace parce "
       "qu’elle dépense beaucoup."],
  exp="Le cours ajoute trois conditions : combiner top-down et bottom-up, "
      "c’est-à-dire orientation et expérimentation ; retenir un horizon "
      "suffisamment long, car l’innovation industrielle demande du temps ; et "
      "viser les technologies futures plutôt que les seules industries "
      "historiques. Une politique industrielle n’est donc pas efficace parce "
      "qu’elle dépense beaucoup mais parce qu’elle identifie une défaillance "
      "précise, impose des conditions, préserve la concurrence et accepte de "
      "réallouer les ressources lorsque les projets échouent.",
  diss="Liste de critères idéale pour une partie d’évaluation : on juge une "
       "politique industrielle à sa conditionnalité, pas à son montant."),

# ------------------------------------------------------------- c22-14
f(id='q22-n41', sp='c22-14', niv='comprendre', type='qcm', b=4920,
  q="Pourquoi parler d’un « retour » de la politique industrielle peut-il "
    "être trompeur ?",
  opts=["Parce que la politique industrielle n’a jamais existé en France",
        "Parce que l’intervention publique n’a jamais totalement disparu : ce "
        "qui revient, c’est le ciblage sectoriel",
        "Parce que la politique industrielle est désormais interdite par les "
        "traités européens",
        "Parce que seuls les États-Unis mènent une politique industrielle"],
  ans=1,
  why=["La France possède au contraire une tradition interventionniste "
       "ancienne, remontant au XVIIᵉ siècle.",
       "Les traités encadrent fortement les aides d’État mais ne les "
       "interdisent pas absolument.",
       "L’Europe et la Chine mènent également des politiques industrielles."],
  exp="Ce qui a reculé à partir des années 1980 n’est pas l’intervention "
      "publique en général mais la politique industrielle verticale, "
      "c’est-à-dire le ciblage explicite de certains secteurs ou entreprises. "
      "Le mouvement a été : politique industrielle verticale → politique "
      "industrielle davantage horizontale. Le « retour » contemporain désigne "
      "donc le retour du ciblage sectoriel, après plusieurs décennies de "
      "priorité donnée aux politiques horizontales et concurrentielles.",
  diss="Précision de vocabulaire décisive : distinguer retour de l’État et "
       "retour du ciblage évite un contresens fréquent."),

f(id='q22-n42', sp='c22-14', niv='connaitre', type='qcm', b=4927,
  q="Quelle doctrine économique inspire la politique industrielle de Colbert, "
    "au XVIIᵉ siècle ?",
  opts=["Le libre-échange",
        "Le mercantilisme",
        "Le keynésianisme",
        "Le monétarisme"],
  ans=1,
  why=["Le libre-échange sera théorisé plus tard, notamment par Smith et "
       "Ricardo.",
       "Le keynésianisme est une doctrine du XXᵉ siècle, centrée sur la "
       "demande globale.",
       "Le monétarisme est encore plus tardif et porte sur la politique "
       "monétaire."],
  exp="Dans la pensée mercantiliste, richesse et puissance passent par "
      "l’accumulation de métaux précieux : il faut donc développer les "
      "exportations et limiter les importations, et pour cela créer des "
      "industries capables de produire et d’exporter. Le colbertisme "
      "constitue ainsi une forme ancienne de politique industrielle "
      "verticale : l’État sélectionne certaines productions jugées "
      "stratégiques afin de réduire la dépendance extérieure et de renforcer "
      "la puissance commerciale du royaume.",
  diss="Filiation éclairante : la logique « argent public → production "
       "nationale » des politiques contemporaines a plus de trois siècles."),

f(id='q22-n43', sp='c22-14', niv='appliquer', type='assoc', b=4970,
  q="Associez chaque intervention publique française à sa date.",
  ans=[["Loi ferroviaire organisant la répartition des rôles entre État et "
        "compagnies privées", "1842"],
       ["Plan Freycinet de grands travaux ferroviaires, de canaux et "
        "d’installations portuaires", "1879"],
       ["Prise de participation de l’État dans la Compagnie française des "
        "pétroles, future Total", "1931"],
       ["Création du Commissariat général au Plan, dirigé par Jean Monnet",
        "1946"]],
  exp="Ces quatre dates montrent la continuité de l’intervention industrielle "
      "française et la diversité de ses formes : partage des rôles avec le "
      "privé en 1842, grands travaux d’infrastructure en 1879, entrée au "
      "capital d’une entreprise stratégique en 1931, planification indicative "
      "en 1946. Les infrastructures relèvent d’une logique horizontale, la "
      "participation pétrolière d’une logique verticale et de souveraineté.",
  diss="Enchaînement à retenir : infrastructures publiques ↑ → coûts de "
       "transport ↓ → intégration du marché national ↑ → activité économique "
       "↑."),

f(id='q22-n44', sp='c22-14', niv='comprendre', type='qcm', b=4988,
  q="Quelle logique explique l’intervention précoce de l’État français dans "
    "le secteur énergétique ?",
  opts=["La seule recherche de profits pour l’État",
        "Une logique de souveraineté : certains secteurs sont jugés "
        "stratégiques et non seulement rentables",
        "L’application des règles européennes de concurrence",
        "La volonté de réduire les prix de l’électricité pour les ménages "
        "uniquement"],
  ans=1,
  why=["La rentabilité n’est pas le critère : le cours souligne précisément "
       "qu’elle n’est pas le seul critère.",
       "Les règles européennes de concurrence sont très postérieures et "
       "vont plutôt en sens inverse.",
       "Le prix pour les ménages n’est pas l’argument retenu ici."],
  exp="La France cherche à réduire sa dépendance énergétique : en 1931, "
      "l’État prend une participation importante dans la Compagnie française "
      "des pétroles, future Total ; après la Seconde Guerre mondiale, "
      "EDF-GDF est créé. Le contrôle public de l’énergie répond à trois "
      "objectifs : productif, de sécurité et de souveraineté. Certains "
      "secteurs ne sont donc pas considérés uniquement selon leur rentabilité "
      "mais aussi selon leur rôle stratégique pour l’économie nationale.",
  diss="Continuité frappante avec le débat contemporain sur les matériaux "
       "critiques et les batteries : le raisonnement est identique."),

f(id='q22-n45', sp='c22-14', niv='comprendre', type='qcm', b=5027,
  q="En quoi la planification française d’après-guerre se distingue-t-elle "
    "d’une planification soviétique ?",
  opts=["Elle est indicative : l’État fixe de grandes orientations et "
        "coordonne les acteurs sans supprimer les entreprises privées",
        "Elle fixe des quantités obligatoires de production pour chaque "
        "entreprise",
        "Elle supprime la propriété privée des moyens de production",
        "Elle porte uniquement sur l’agriculture"],
  ans=0,
  why=["Les objectifs quantitatifs contraignants caractérisent au contraire "
       "la planification impérative.",
       "La planification française n’abolit pas la propriété privée.",
       "Elle concerne l’ensemble de l’appareil productif, à commencer par "
       "l’industrie."],
  exp="Le Commissariat général au Plan est créé en 1946, avec Jean Monnet "
      "comme premier commissaire ; le premier plan couvre 1947-1952. Ses "
      "objectifs sont de reconstruire, moderniser, augmenter la productivité, "
      "orienter l’investissement et utiliser notamment les ressources issues "
      "du plan Marshall. La planification reste indicative : elle organise "
      "une coordination entre pouvoirs publics et entreprises privées afin "
      "d’orienter l’investissement vers les secteurs jugés prioritaires.",
  diss="Vocabulaire précis à employer : planification indicative, et non "
       "dirigiste ou impérative."),

f(id='q22-n46', sp='c22-14', niv='comprendre', type='qcm', b=5039,
  q="Quel était l’objectif de la politique française des champions nationaux "
    "pendant les Trente Glorieuses ?",
  opts=["Protéger les petites entreprises de la concurrence des grandes",
        "Créer des entreprises suffisamment grandes pour bénéficier "
        "d’économies d’échelle, investir massivement, exporter et maîtriser "
        "des technologies avancées",
        "Remplacer les entreprises privées par des coopératives",
        "Limiter les exportations françaises au marché européen"],
  ans=1,
  why=["La politique visait au contraire la constitution de grands groupes.",
       "Les coopératives ne sont pas l’instrument retenu.",
       "L’exportation était recherchée, et non limitée."],
  exp="Renault, Thomson et Usinor en sont des exemples, suivis de grands "
      "projets dans le nucléaire, le TGV et l’aéronautique avec Airbus. La "
      "taille est ici le moyen : elle permet les économies d’échelle, "
      "l’investissement de long terme, la conquête de marchés extérieurs et "
      "la maîtrise de technologies coûteuses. Airbus montre d’ailleurs qu’une "
      "politique industrielle peut dépasser le cadre national, plusieurs "
      "États européens ayant mutualisé leurs moyens pour rattraper une avance "
      "technologique étrangère.",
  diss="Airbus est l’exemple à privilégier pour défendre l’échelle "
       "européenne : coopération publique → ressources mutualisées → "
       "apprentissage → compétitivité internationale."),

f(id='q22-n47', sp='c22-14', niv='comprendre', type='qcm', b=5112,
  q="Que désigne l’expression « État brancardier », employée à propos de la "
    "France des années 1970-1980 ?",
  opts=["Un État qui finance exclusivement le système de santé",
        "Un État qui n’intervient plus que pour accompagner la disparition "
        "progressive d’activités devenues non compétitives",
        "Un État qui nationalise l’ensemble de l’industrie",
        "Un État qui se retire totalement de l’économie"],
  ans=1,
  why=["L’expression est une image : elle ne concerne pas le secteur de la "
       "santé.",
       "Les nationalisations relèvent d’une autre logique, celle de l’État "
       "stratège ou des vagues décrites par Mulder.",
       "Le retrait complet correspond plutôt au mouvement de privatisation "
       "qui suit."],
  exp="À partir de la crise industrielle des années 1970-1980, plusieurs "
      "branches industrielles traditionnelles entrent en crise. L’État "
      "français devient en partie un « État brancardier » : la politique "
      "industrielle ne vise plus seulement à créer des secteurs d’avenir mais "
      "aussi à accompagner la disparition progressive d’activités devenues "
      "non compétitives. Le mécanisme est le suivant : industrie "
      "structurellement en déclin → soutien public → restructuration étalée "
      "dans le temps → coût social immédiat réduit.",
  diss="Distinction très utile : État stratège, qui construit l’avenir, et "
       "État brancardier, qui amortit le déclin."),

f(id='q22-n48', sp='c22-14', niv='connaitre', type='qcm', b=5117,
  q="À partir de quelle année le mouvement de privatisation s’engage-t-il en "
    "France ?",
  opts=["1981",
        "1986",
        "1993",
        "2000"],
  ans=1,
  why=["1981 correspond plutôt à une période d’extension du secteur public.",
       "1993 est postérieur au début du mouvement.",
       "2000 est bien trop tardif pour marquer son amorce."],
  exp="Le mouvement de privatisation commence notamment à partir de 1986. "
      "L’objectif est de réduire la présence directe de l’État dans "
      "l’économie, alors qu’au début des années 1980 celui-ci contrôlait "
      "encore plusieurs milliers d’entreprises représentant une part "
      "importante de l’investissement et des exportations françaises. Les "
      "privatisations symbolisent le passage d’un État directement producteur "
      "à un État davantage régulateur.",
  diss="Mouvement à articuler avec la déréglementation : l’ouverture à la "
       "concurrence des anciens monopoles complète les privatisations."),

f(id='q22-n49', sp='c22-14', niv='raisonner', type='qcm', b=5171,
  q="En quoi consiste la critique informationnelle adressée à la politique "
    "industrielle verticale ?",
  opts=["L’État ne dispose pas nécessairement d’une information suffisante "
        "pour sélectionner à l’avance les entreprises ou technologies qui "
        "deviendront compétitives",
        "L’État ne publie pas assez de statistiques économiques",
        "Les entreprises refusent de transmettre leurs comptes à "
        "l’administration",
        "Les consommateurs sont mal informés sur les produits subventionnés"],
  ans=0,
  why=["La production de statistiques n’est pas l’objet de cette critique.",
       "La transmission des comptes n’est pas le problème soulevé.",
       "L’information du consommateur relève d’une autre question."],
  exp="Une politique industrielle verticale suppose que l’État sache choisir "
      "les gagnants. La critique informationnelle conteste cette capacité : "
      "l’État ne possède pas toute l’information nécessaire, d’où le risque "
      "d’un mauvais ciblage et donc d’un gaspillage de ressources publiques. "
      "Cette critique est l’une des deux grandes raisons du retournement des "
      "années 1980, avec la montée en puissance de la politique de "
      "concurrence.",
  diss="Réponse possible à cette critique : l’approche bottom-up, où l’État "
       "fixe la direction sans choisir la technologie."),

f(id='q22-n50', sp='c22-14', niv='raisonner', type='qcm', b=5192,
  q="Quelle critique l’école du Public Choice adresse-t-elle aux politiques "
    "industrielles ciblées ?",
  opts=["Elles coûtent trop peu cher pour être efficaces",
        "Elles peuvent transformer les entreprises en chercheurs de rente, "
        "qui consacrent leurs ressources à obtenir et conserver les avantages "
        "distribués par l’État",
        "Elles favorisent exclusivement les entreprises étrangères",
        "Elles sont incompatibles avec la propriété privée"],
  ans=1,
  why=["Le coût n’est pas l’argument de cette école : c’est le comportement "
       "qu’induit l’aide.",
       "La nationalité des bénéficiaires n’est pas en cause.",
       "La propriété privée n’est pas remise en question par ces "
       "politiques."],
  exp="Le mécanisme décrit est le suivant : aides publiques importantes → "
      "lobbying ↑ → ressources consacrées à obtenir la protection ↑ → "
      "efficacité économique ↓. Au lieu d’améliorer leur productivité, les "
      "entreprises peuvent consacrer leurs moyens à influencer la décision "
      "publique. Cette critique complète la critique informationnelle : l’une "
      "porte sur la capacité de l’État à bien choisir, l’autre sur les "
      "comportements que son intervention induit.",
  diss="Les deux critiques forment une partie de plan très robuste : l’État "
       "sait-il choisir, et que fait son choix aux entreprises ?"),

f(id='q22-n51', sp='c22-14', niv='comprendre', type='qcm', b=5209,
  q="Pourquoi la construction européenne a-t-elle contribué à marginaliser "
    "les politiques industrielles verticales nationales ?",
  opts=["Parce que les traités interdisent toute intervention publique dans "
        "l’économie",
        "Parce que la création d’un marché commun suppose que les États ne "
        "puissent librement favoriser leurs entreprises au détriment de "
        "celles de leurs partenaires",
        "Parce que l’Union européenne a repris à son compte toutes les "
        "politiques industrielles nationales",
        "Parce que les États membres ont perdu leur souveraineté budgétaire"],
  ans=1,
  why=["Les traités encadrent les aides d’État, mais n’interdisent pas toute "
       "intervention.",
       "L’Union n’a pas repris les politiques industrielles nationales : "
       "c’est précisément le manque de coordination européenne que le cours "
       "souligne.",
       "Les États membres conservent l’essentiel de leur compétence "
       "budgétaire."],
  exp="La construction européenne donne la priorité à la concurrence : il "
      "s’agit de supprimer les obstacles aux échanges entre États membres et "
      "de garantir une concurrence équitable entre les entreprises. Le "
      "raisonnement est le suivant : subvention ciblée d’un État → avantage "
      "artificiel pour une entreprise nationale → concurrence "
      "intra-européenne faussée. Les aides d’État sont donc fortement "
      "encadrées, et le bénéfice attendu de la concurrence est l’enchaînement "
      "prix ↓ → innovation ↑ → productivité ↑ → bien-être du consommateur ↑.",
  diss="C’est exactement cette doctrine que le projet d’Industrial "
       "Accelerator Act vient infléchir avec la préférence européenne."),

]
