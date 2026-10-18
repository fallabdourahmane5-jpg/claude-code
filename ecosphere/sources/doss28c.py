# -*- coding: utf-8 -*-
"""Ensemble 28 — troisième série : défensif, offensif, industries vieillissantes,
durée et sélectivité de la protection.

La comparaison approfondie entre protectionnisme défensif et offensif est
partagée par les deux dossiers correspondants.
"""

from doss_base import d

# Comparaison commune aux dossiers « défensif » et « offensif ».
COMP = {
 'titre': "Protectionnisme défensif et protectionnisme offensif : comparaison",
 'a': "Protectionnisme défensif",
 'b': "Protectionnisme offensif",
 'lignes': [
  ("Objectif poursuivi",
   "Préserver une activité, un emploi ou une capacité productive menacés par la "
   "concurrence étrangère. Le point de départ est une perte à éviter.",
   "Développer une capacité nouvelle et conquérir une position dans un secteur "
   "jugé stratégique. Le point de départ est un gain à construire."),
  ("Secteurs concernés",
   "Branches matures ou vieillissantes, souvent intensives en main-d’œuvre, "
   "géographiquement concentrées et politiquement organisées : sidérurgie, "
   "textile, assemblage.",
   "Branches à rendements croissants, intensives en recherche et en capital, à "
   "forte valeur ajoutée future : semi-conducteurs, batteries, véhicules "
   "électriques, technologies bas-carbone."),
  ("Horizon temporel",
   "Court à moyen terme : il s’agit d’étaler un choc et d’organiser une "
   "reconversion. L’échéance est celle de la restructuration.",
   "Long terme : il s’agit d’atteindre un seuil d’échelle ou une position "
   "technologique. L’échéance est celle de la compétitivité acquise."),
  ("Instruments privilégiés",
   "Droits de douane, clauses de sauvegarde, droits antidumping et "
   "compensateurs, quotas : des instruments de frontière, correctifs et "
   "réversibles.",
   "Subventions, soutien à la recherche et développement, commande publique, "
   "exigences de contenu local, politique industrielle : des instruments de "
   "soutien à la production plus que de blocage à la frontière."),
  ("Mécanisme économique",
   "Renchérir l’importation pour maintenir la demande adressée aux producteurs "
   "nationaux, le temps que l’adaptation ou la sortie s’organise.",
   "Abaisser le coût ou le risque supporté par le producteur national afin qu’il "
   "franchisse un seuil d’échelle, ou déplacer un profit oligopolistique vers "
   "lui en dissuadant l’investissement du rival."),
  ("Référence théorique",
   "Kaldor (1966) : transposer la logique de la protection temporaire aux "
   "industries vieillissantes pour permettre reconversion ou montée en gamme.",
   "List puis Krugman pour les industries naissantes ; Brander et Spencer (1983) "
   "pour la politique commerciale stratégique en oligopole."),
  ("Effet attendu",
   "Lissage du choc social, maintien temporaire de l’emploi, temps donné à la "
   "restructuration et à la requalification.",
   "Création d’une capacité productive durable, baisse du coût moyen par les "
   "économies d’échelle, captation d’une part de marché et d’un profit futurs."),
  ("Risque principal",
   "Entretenir des « canards boiteux » : maintenir artificiellement des "
   "activités structurellement non compétitives, au prix d’un coût collectif "
   "élevé et d’un report indéfini de l’ajustement.",
   "Déclencher une surenchère de subventions et des représailles, puisque le "
   "gain repose sur le fait que le rival renonce. Risque aussi d’erreur de "
   "sélection si le secteur choisi ne décolle pas."),
  ("Coût supporté par",
   "Les consommateurs, par les prix, et les entreprises utilisatrices du bien "
   "protégé, par le coût de leurs intrants.",
   "Le contribuable, par la subvention, et les secteurs non soutenus, par "
   "l’éviction des ressources budgétaires et des facteurs rares."),
  ("Condition d’efficacité",
   "Être strictement temporaire et assortie d’engagements de restructuration "
   "vérifiables, faute de quoi elle finance la survie sans préparer la sortie.",
   "Porter sur un secteur réellement viable, préserver la concurrence interne, "
   "et anticiper la réaction des partenaires, sans quoi l’avantage obtenu est "
   "annulé par la riposte."),
  ("Exemples tirés des cours",
   "Clauses de sauvegarde face à un afflux brutal d’importations ; droits "
   "antidumping et compensateurs ; accompagnement des branches en déclin décrit "
   "par Kaldor.",
   "Inflation Reduction Act aux États-Unis, dont les aides sont liées au contenu "
   "local ; projet européen d’Industrial Accelerator Act du 4 mars 2026 visant "
   "20 % du PIB européen pour l’industrie d’ici 2035."),
  ("Chevauchement",
   "Une sauvegarde présentée comme défensive peut servir à gagner le temps "
   "nécessaire à une montée en gamme : elle devient alors offensive par ses "
   "effets.",
   "Une politique industrielle offensive est souvent justifiée publiquement par "
   "la défense de l’emploi menacé : la même mesure se présente différemment "
   "selon l’auditoire visé."),
 ]}

# ---------------------------------------------------------------- 28.08
d('le28-defensif', 28, "Protectionnisme défensif",
  "Protéger ce qui existe et se trouve menacé",
  "Le protectionnisme défensif désigne les mesures destinées à préserver des "
  "activités, des emplois ou des capacités productives existants et menacés par "
  "la concurrence étrangère. Il se définit par son point de départ : une perte "
  "à éviter, et non une position à conquérir. Son horizon est celui de "
  "l’ajustement — étaler un choc, organiser une reconversion — et ses "
  "instruments sont des instruments de frontière, correctifs et en principe "
  "réversibles.",
  "Le protectionnisme défensif répond à un problème réel, que la théorie du "
  "commerce reconnaît sans toujours en tirer les conséquences : l’ouverture "
  "produit des pertes concentrées, immédiates et parfois irréversibles. Un "
  "bassin d’emploi spécialisé qui perd son établissement principal ne retrouve "
  "pas spontanément une activité équivalente ; les qualifications se "
  "déprécient, la demande locale se contracte, la dévitalisation devient "
  "cumulative. Protéger défensivement revient à introduire un délai dans cet "
  "enchaînement. Deux usages très différents se cachent toutefois sous le même "
  "mot, et c’est la distinction essentielle à faire. Dans le premier, la "
  "protection sert à organiser la sortie : elle finance le temps nécessaire à "
  "la requalification des salariés, à la reconversion du site ou à la montée en "
  "gamme de la production — c’est la logique que Kaldor propose en transposant "
  "aux industries vieillissantes le raisonnement de la protection temporaire. "
  "Dans le second, la protection sert à éviter la sortie : elle maintient "
  "l’activité en l’état, sans transformation, et devient alors un transfert "
  "permanent des consommateurs vers une branche qui ne redeviendra pas "
  "compétitive. Le premier usage est une politique d’ajustement, le second "
  "produit ce que le cours appelle des « canards boiteux ». Rien, dans "
  "l’instrument lui-même, ne permet de les distinguer : seuls le calendrier, la "
  "conditionnalité et l’évaluation le permettent.",
  [("Le renchérissement de l’importation",
    "Droit de douane, quota ou mesure correctrice élèvent le prix du produit "
    "importé, ce qui ramène vers le producteur national une partie de la demande "
    "qui s’en détournait. L’effet est immédiat et visible, ce qui explique son "
    "attrait politique."),
   ("Le maintien temporaire de l’emploi",
    "La demande préservée soutient le niveau de production, donc l’emploi, dans "
    "la branche concernée. Ce maintien est réel mais borné : il dure ce que dure "
    "la mesure, sauf si la branche se transforme entre-temps."),
   ("Le temps donné à la restructuration",
    "Le délai obtenu peut être employé à moderniser l’outil productif, à "
    "requalifier les salariés, à réorienter la production vers des segments de "
    "gamme moins exposés. C’est la seule justification qui résiste à long terme."),
   ("Le report du coût sur l’aval et sur les consommateurs",
    "Le prix plus élevé est payé par les ménages et, lorsque le bien protégé est "
    "un intrant, par les entreprises utilisatrices, qui perdent en compétitivité. "
    "Protéger un maillon peut fragiliser toute la filière située en aval."),
   ("Le risque de verrouillage politique",
    "La branche protégée s’organise pour obtenir le maintien de la mesure. Plus "
    "la protection dure, plus les intérêts constitués rendent sa suppression "
    "coûteuse politiquement, indépendamment de sa justification économique.")],
  [{'a': "La protection défensive évite une destruction brutale de capital "
         "humain et productif que l’ajustement spontané ne permettrait pas "
         "d’éviter.",
    'cond': "Le choc doit être transitoire ou la branche doit pouvoir se "
            "transformer ; et le délai obtenu doit être effectivement employé à "
            "la restructuration, ce qui suppose des engagements vérifiables.",
    'lim': "Si le désavantage est structurel, le délai ne fait que repousser la "
           "perte en la rendant plus coûteuse, puisque l’économie aura entre- "
           "temps immobilisé des facteurs dans une activité condamnée."},
   {'a': "Elle rend l’ouverture politiquement soutenable en montrant que "
         "l’ajustement n’est pas abandonné aux seuls salariés exposés.",
    'cond': "La mesure doit être perçue comme une contrepartie explicite de "
            "l’ouverture, et non comme une faveur accordée à un secteur bien "
            "organisé.",
    'lim': "Le soupçon de capture est difficile à lever : les branches qui "
           "obtiennent une protection sont rarement celles qui en auraient le "
           "plus besoin, mais celles qui savent le mieux la demander."},
   {'a': "Certains instruments défensifs sont juridiquement encadrés et "
         "légitimes : clauses de sauvegarde, droits antidumping, droits "
         "compensateurs.",
    'cond': "Leur usage suppose l’établissement d’une distorsion ou d’un afflux "
            "brutal d’importations selon les critères applicables, et une "
            "proportionnalité de la mesure.",
    'lim': "Ces instruments peuvent être détournés : la qualification de "
           "« pratique déloyale » offre une base commode à une protection "
           "ordinaire, ce qui nourrit les contentieux."}],
  [{'t': "La protection défensive ne préserve pas l’emploi, elle retarde la "
         "reconversion et rend l’ajustement final plus douloureux.",
    'qui': "Objection centrale rappelée par le cours à travers le risque des "
           "« canards boiteux ».",
    'rep': "Elle est fondée lorsque la protection n’est assortie d’aucune "
           "transformation. Elle tombe si la mesure finance une montée en gamme "
           "effective : le critère n’est donc pas la protection elle-même mais "
           "ce qu’on en fait."},
   {'t': "Le coût par emploi préservé est très élevé, puisqu’il est supporté par "
         "l’ensemble des consommateurs et par les entreprises utilisatrices.",
    'qui': "Analyse en termes de surplus développée dans le cours à propos des "
           "droits de douane.",
    'rep': "La comparaison pertinente n’est pas avec un ajustement sans coût "
           "mais avec le coût social réel du chômage et de la dévitalisation "
           "territoriale. Elle plaide néanmoins pour préférer des transferts "
           "directs à une protection par les prix."},
   {'t': "La protection appelle des représailles qui frappent les secteurs "
         "exportateurs, souvent plus productifs que la branche protégée.",
    'qui': "Le cours souligne que les mesures protectionnistes provoquent "
           "souvent des représailles.",
    'rep': "L’argument est décisif pour les mesures unilatérales de grande "
           "ampleur, moins pour les instruments encadrés multilatéralement, "
           "dont l’usage est précisément prévu et borné."}],
  [{'n': "Nicholas Kaldor",
    'i': "Transposer aux industries vieillissantes la logique de la protection "
         "temporaire conçue pour les industries naissantes (1966).",
    'p': "Il s’agit de protéger temporairement une branche menacée par la "
         "concurrence afin de lui permettre de se reconvertir ou de monter en "
         "gamme. La protection reste justifiée par une transformation attendue, "
         "non par la préservation d’un état."},
   {'n': "Nicholas Kaldor",
    'i': "La protection des industries vieillissantes devient coûteuse "
         "lorsqu’elle maintient artificiellement des activités structurellement "
         "non compétitives.",
    'p': "La limite est posée dans le raisonnement lui-même : le risque des "
         "« canards boiteux » n’est pas une objection extérieure mais la "
         "contrepartie reconnue de la mesure, ce qui impose d’en borner la durée."},
   {'n': "Dani Rodrik",
    'i': "La réponse au déclassement ne peut pas se limiter à préserver ou "
         "reconstruire l’industrie.",
    'p': "Puisque l’industrie n’emploie qu’une minorité des actifs dans les "
         "économies avancées, une politique défensive centrée sur elle ne peut "
         "traiter qu’une part limitée du problème social : la priorité doit "
         "porter sur la productivité et la qualité des emplois de services."}],
  [{'f': "Une clause de sauvegarde permet de protéger temporairement une "
         "industrie domestique gravement menacée par une hausse rapide des "
         "importations, afin de laisser du temps à l’adaptation et à la "
         "restructuration.",
    'p': "L’instrument illustre la forme juridiquement encadrée du "
         "protectionnisme défensif : la protection y est explicitement liée à un "
         "objectif d’ajustement et bornée dans le temps."},
   {'f': "Les droits antidumping et les droits compensateurs permettent de "
         "relever temporairement les droits de douane pour corriger une "
         "distorsion de concurrence.",
    'p': "Ces mesures sont défensives par leur objectif — rétablir des "
         "conditions de concurrence — et montrent que le protectionnisme "
         "défensif n’est pas nécessairement hors des règles multilatérales."},
   {'f': "Le cours décrit l’enchaînement : activité maintenue artificiellement, "
         "coût collectif élevé, risque d’entretenir des « canards boiteux ».",
    'p': "Il fournit le critère d’échec du protectionnisme défensif et rappelle "
         "que son coût est supporté collectivement alors que son bénéfice est "
         "concentré."}],
  [{'q': "Sujet du type « Le protectionnisme défensif préserve-t-il l’emploi ou "
         "retarde-t-il les reconversions ? »",
    'f': "Le protectionnisme défensif fait les deux, et ce qui détermine lequel "
         "l’emporte n’est pas l’instrument mais son usage : une protection qui "
         "finance une montée en gamme ou une requalification organise la "
         "transition, tandis qu’une protection reconduite sans contrepartie "
         "finance la survie d’une activité condamnée en la faisant payer aux "
         "consommateurs et aux entreprises situées en aval.",
    'r': "On refuse l’alternative posée par le sujet pour lui substituer un "
         "critère : la présence ou l’absence d’une transformation effective de "
         "la branche protégée, vérifiable par le calendrier, la conditionnalité "
         "et l’évaluation.",
    'ex': "Kaldor assume explicitement cette ambivalence en transposant la "
          "protection temporaire aux industries vieillissantes."},
   {'q': "Sujet du type « Faut-il protéger les industries naissantes ou les "
         "industries vieillissantes ? »",
    'f': "Les deux protections obéissent au même raisonnement — un délai "
         "permettant une transformation — mais leurs probabilités de succès "
         "diffèrent : l’industrie naissante doit franchir un seuil d’échelle "
         "identifiable, tandis que l’industrie vieillissante doit renverser un "
         "désavantage souvent structurel. Le pari est donc moins favorable dans "
         "le second cas.",
    'r': "La comparaison porte sur la nature du handicap à surmonter — un seuil "
         "d’échelle non encore atteint d’un côté, un désavantage installé de "
         "l’autre —, ce qui permet de hiérarchiser les deux politiques selon "
         "leur probabilité de succès plutôt que de les opposer par principe.",
    'ex': "List et Krugman d’un côté, Kaldor et le risque des « canards "
          "boiteux » de l’autre."}],
  voisins=['le28-offensif', 'le28-vieillissantes', 'le28-sauvegarde',
           'le28-dumping', 'le28-temporaire-permanent', 'le28-couts-ouverture'],
  comp=COMP)

# ---------------------------------------------------------------- 28.09
d('le28-offensif', 28, "Protectionnisme offensif",
  "Construire une position plutôt que défendre un acquis",
  "Le protectionnisme offensif désigne les mesures destinées à développer des "
  "capacités productives nouvelles et à conquérir des positions dans des "
  "secteurs jugés stratégiques. Son point de départ est un gain à construire, "
  "non une perte à éviter. Il mobilise davantage des instruments de soutien à "
  "la production — subventions, aide à la recherche, commande publique, "
  "exigences de contenu local — que des barrières à la frontière, et son "
  "horizon est long.",
  "Deux raisonnements théoriques distincts fondent le protectionnisme offensif, "
  "et il faut les séparer. Le premier est celui des industries naissantes : "
  "lorsqu’il existe un seuil de production au-delà duquel le coût moyen national "
  "descend sous le prix mondial, un soutien transitoire permet de franchir ce "
  "seuil et crée un avantage comparatif qui n’existait pas — c’est la "
  "formalisation de List par Krugman. Le second est celui de la politique "
  "commerciale stratégique de Brander et Spencer : dans un secteur "
  "oligopolistique où le profit n’est accessible qu’à un petit nombre de firmes, "
  "un engagement public crédible de soutien modifie le calcul du concurrent "
  "étranger, qui renonce à investir ; le profit se déplace alors vers la firme "
  "nationale. La différence est importante. Dans le premier cas, la politique "
  "crée de la valeur en rendant viable une production qui ne l’était pas ; dans "
  "le second, elle déplace une valeur existante d’un pays vers un autre, ce qui "
  "en fait un jeu à somme nulle entre partenaires et explique qu’elle appelle "
  "des représailles. Le cours souligne d’ailleurs que l’instrument étudié par "
  "Brander et Spencer relève en pratique largement de la subvention, notamment à "
  "la recherche, plus que du droit de douane : le protectionnisme offensif "
  "contemporain se joue moins à la frontière que dans le budget. L’Inflation "
  "Reduction Act américain et le projet européen d’Industrial Accelerator Act en "
  "sont les illustrations directes.",
  [("L’identification d’un secteur stratégique",
    "L’État sélectionne une filière jugée déterminante pour la croissance "
    "future, la sécurité ou la transition écologique. Cette sélection est le "
    "point de départ — et le point faible — de toute la politique."),
   ("L’abaissement du coût ou du risque privé",
    "Subventions, crédits d’impôt, financement de la recherche et commande "
    "publique réduisent le coût ou l’incertitude supportés par l’entreprise, ce "
    "qui rend rentable un investissement qui ne l’était pas."),
   ("Le franchissement du seuil d’échelle",
    "La production soutenue croît, les économies d’échelle se réalisent, le coût "
    "moyen baisse jusqu’à passer sous celui des concurrents. L’avantage "
    "comparatif est alors construit et peut survivre à l’arrêt du soutien."),
   ("Le déplacement du profit oligopolistique",
    "Dans un marché où quelques firmes seulement peuvent être rentables, "
    "l’engagement public crédible de soutenir la firme nationale dissuade le "
    "rival d’investir. Le profit qu’il aurait réalisé revient au producteur "
    "national."),
   ("Le verrouillage par la demande publique et le contenu local",
    "Réserver la commande publique ou conditionner les aides au contenu local "
    "garantit un débouché minimal à la production nationale, ce qui sécurise "
    "l’investissement initial sans recourir à un droit de douane.")],
  [{'a': "Le soutien public peut créer un avantage comparatif là où le marché "
         "n’en aurait pas produit, lorsque des rendements croissants verrouillent "
         "la position du premier entrant.",
    'cond': "Il faut que les rendements croissants soient réels, que le seuil "
            "d’échelle soit atteignable compte tenu du marché accessible, et que "
            "la concurrence interne soit maintenue pour éviter la rente.",
    'lim': "Si le secteur ne décolle pas, le coût budgétaire est engagé sans "
           "contrepartie, et les ressources mobilisées ont été détournées "
           "d’emplois plus productifs."},
   {'a': "Dans un oligopole, un engagement public crédible déplace le profit "
         "vers la firme nationale en dissuadant l’investissement du rival.",
    'cond': "L’engagement doit être crédible et antérieur à la décision du "
            "concurrent ; le marché doit effectivement être oligopolistique, "
            "avec des profits à capter.",
    'lim': "Le raisonnement suppose que l’État étranger ne fasse pas de même. "
           "Généralisé, il produit une surenchère de subventions où chacun "
           "dépense sans que personne ne capte de profit supplémentaire."},
   {'a': "Les instruments offensifs pèsent sur le contribuable plutôt que sur le "
         "consommateur, ce qui les rend moins régressifs qu’un droit de douane.",
    'cond': "Encore faut-il que le financement soit assuré et que la dépense ne "
            "se substitue pas à d’autres investissements publics productifs.",
    'lim': "La subvention est moins visible que le droit de douane, donc moins "
           "facilement contestée : son coût réel est plus difficile à évaluer "
           "démocratiquement."}],
  [{'t': "La politique commerciale stratégique est un jeu à somme nulle : elle "
         "déplace un profit existant plutôt que d’en créer.",
    'qui': "Lecture du modèle de Brander et Spencer, dont le gain national "
           "correspond au renoncement du concurrent étranger.",
    'rep': "C’est exact pour le volet « déplacement de profit », mais pas pour le "
           "volet « industries naissantes », où le soutien rend viable une "
           "production qui ne l’était pas. Les deux justifications doivent donc "
           "être évaluées séparément."},
   {'t': "L’État ne sait pas choisir les secteurs d’avenir et se laisse guider "
         "par les intérêts les mieux organisés.",
    'qui': "Objection d’information et de capture, présente dans le cours à "
           "travers les causes d’échec des protections.",
    'rep': "Elle plaide pour des critères explicites — existence de rendements "
           "croissants, taille du marché, externalités technologiques — et pour "
           "une évaluation indépendante, plutôt que pour l’abstention : l’erreur "
           "de sélection est un coût borné si le soutien est conditionnel."},
   {'t': "Les politiques offensives déclenchent une course aux subventions qui "
         "annule l’avantage recherché et dégrade les finances publiques de tous.",
    'qui': "Conséquence directe du caractère non coopératif du raisonnement, et "
           "constat du cours sur les représailles.",
    'rep': "L’objection explique pourquoi ces politiques appellent une "
           "coordination internationale. Elle n’annule pas leur rationalité "
           "individuelle, ce qui est précisément la structure d’un dilemme."}],
  [{'n': "James Brander",
    'i': "La politique commerciale stratégique : utiliser l’intervention "
         "publique pour modifier la concurrence entre quelques grandes firmes "
         "internationales.",
    'p': "Avec Barbara Spencer, International R&D Rivalry and Industrial "
         "Strategy (1983). Il ne s’agit plus de protéger une industrie existante "
         "mais de changer l’issue d’un jeu entre firmes, ce qui déplace le débat "
         "de la frontière vers la politique industrielle."},
   {'n': "Barbara Spencer",
    'i': "L’instrument mobilisé relève en pratique largement de la subvention, "
         "notamment à la recherche.",
    'p': "Le cours insiste sur ce point : le protectionnisme offensif "
         "contemporain passe moins par le droit de douane que par le budget, ce "
         "qui le rend plus difficile à identifier comme une mesure commerciale "
         "et plus difficile à sanctionner."},
   {'n': "Paul Krugman",
    'i': "Le franchissement du seuil d’échelle construit un avantage comparatif "
         "qui n’existait pas.",
    'p': "Le soutien temporaire est ici créateur de valeur, et non seulement "
         "redistributeur entre pays : il fait émerger un producteur "
         "potentiellement plus efficace que l’opérateur installé."},
   {'n': "Friedrich List",
    'i': "Le soutien à l’industrie se justifie par le stade de développement et "
         "la perspective d’un rattrapage.",
    'p': "La filiation est explicite dans le cours : le protectionnisme offensif "
         "contemporain réactive l’argument de List, en l’appliquant non plus à "
         "un pays en retard mais à une filière en retard dans un pays avancé."}],
  [{'f': "L’Inflation Reduction Act lie certaines aides et bonifications au "
         "contenu local de la production : plus la chaîne de valeur est "
         "localisée aux États-Unis, plus l’aide est importante.",
    'p': "L’exemple montre la forme contemporaine du protectionnisme offensif : "
         "un objectif écologique, un objectif industriel et un objectif de "
         "souveraineté poursuivis par un même instrument budgétaire."},
   {'f': "Le projet européen d’Industrial Accelerator Act du 4 mars 2026 vise à "
         "porter la part de l’industrie à 20 % du PIB européen d’ici 2035, en "
         "combinant préférence européenne dans les marchés publics et les aides, "
         "conditionnement de certains investissements étrangers et exigences de "
         "transfert technologique.",
    'p': "Le projet illustre la généralisation des instruments offensifs et la "
         "convergence des grandes puissances vers une politique industrielle "
         "assumée."},
   {'f': "L’Union européenne accuse un retard dans le numérique, les "
         "semi-conducteurs et certaines technologies vertes, ce qui conduit à "
         "parler de nouvelles « industries naissantes » dans une économie "
         "avancée.",
    'p': "Le constat justifie le passage d’une politique défensive, centrée sur "
         "la préservation, à une politique offensive, centrée sur le rattrapage "
         "sectoriel."}],
  [{'q': "Sujet du type « Le protectionnisme offensif peut-il construire de "
         "nouveaux avantages comparatifs ? »",
    'f': "La réponse dépend du mécanisme invoqué. Lorsque le soutien permet de "
         "franchir un seuil d’échelle au-delà duquel le producteur national "
         "devient durablement le moins coûteux, l’avantage comparatif est "
         "réellement construit et survit à l’arrêt de l’aide. Lorsqu’il se borne "
         "à déplacer un profit oligopolistique, aucun avantage n’est créé : une "
         "rente change simplement de pays, et la mesure appelle une riposte.",
    'r': "Séparer les deux justifications — Krugman d’un côté, Brander et "
         "Spencer de l’autre — permet de répondre de façon différenciée au lieu "
         "de trancher globalement.",
    'ex': "L’Inflation Reduction Act, dont les aides conditionnées au contenu "
          "local visent à faire naître une capacité productive nationale."},
   {'q': "Sujet du type « L’État peut-il choisir les secteurs d’avenir ? »",
    'f': "La politique offensive suppose une capacité de sélection que l’État "
         "n’a pas a priori, mais qu’il peut partiellement objectiver : "
         "l’existence de rendements croissants, la taille du marché accessible "
         "et la présence d’externalités technologiques constituent des critères "
         "vérifiables, et la conditionnalité limite le coût d’une erreur.",
    'r': "On transforme une objection de principe — l’État ne sait pas choisir — "
         "en question de dispositif : quels critères de sélection, quelle "
         "conditionnalité des aides, quelle évaluation indépendante, et quel "
         "mécanisme d’arrêt lorsque les résultats ne sont pas au rendez-vous.",
    'ex': "Le projet européen visant 20 % du PIB industriel en 2035 par la "
          "préférence européenne et le conditionnement des investissements."},
   {'q': "Sujet du type « Protectionnisme offensif et défensif sont-ils toujours "
         "séparables ? »",
    'f': "La distinction est analytiquement nette — préserver un acquis ou "
         "conquérir une position — mais elle se brouille dans la pratique, car "
         "une même mesure peut poursuivre les deux objectifs : une sauvegarde "
         "accordée à une filière menacée peut financer sa montée en gamme, et "
         "une politique industrielle offensive est presque toujours justifiée "
         "publiquement par la défense de l’emploi.",
    'r': "On montre que le critère de distinction n’est pas l’instrument mais "
         "l’intention et surtout l’effet constaté, ce qui conduit à évaluer les "
         "mesures sur leurs résultats plutôt que sur leur présentation.",
    'ex': "Les droits compensateurs européens, défendus comme correction d’une "
          "distorsion et comme protection temporaire permettant la "
          "réindustrialisation."}],
  voisins=['le28-defensif', 'le28-politique-strategique', 'le28-educateur',
           'le28-subventions', 'le28-contenu-local', 'le28-marches-publics'],
  comp=COMP)
