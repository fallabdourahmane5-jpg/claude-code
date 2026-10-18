# -*- coding: utf-8 -*-
"""Ensemble 28 — quatrième série : durée, sélectivité etLa comparaison porte sur l’incidence — qui paie — et sur le nombre "
       "de distorsions introduites, ce qui donne un critère clairPartir de la décomposition des surplus permet de répondre sans "
              "généralité : chaque catégorie d’agent est traitée séparément, ceLe droit protège un secteur en pénalisant les entreprises situées en "
                     "aval, qui utilisent le produit taxé comme intrant et perdent en "
                     "compétitivité, y compris sur leurs marchés d’exportation.fait apparaître que le coût du protectionnisme est diffus alors que "
              "son bénéfice est concentré.hiérarchisation des instruments et permet de conclure autrement que "
       "par une préférence doctrinale."""

from doss_base import d

# ---------------------------------------------------------------- 28.10
d('le28-vieillissantes', 28,
  "Protection des industries vieillissantes ou en déclin",
  "Le raisonnement de List retourné : protéger ce qui s’achève plutôt que ce qui commence",
  "La protection des industries vieillissantes désigne le soutien temporaire "
  "accordé à une branche ancienne menacée de disparition par la concurrence "
  "internationale, afin de lui permettre de se reconvertir ou de monter en "
  "gamme. Elle inverse la cible du protectionnisme éducateur : la mesure ne "
  "vise plus une industrie qui vient de naître mais une industrie installée dont "
  "l’avantage s’est érodé.",
  "Kaldor transpose en 1966 aux industries vieillissantes la logique de la "
  "protection temporaire conçue pour les industries naissantes. Le raisonnement "
  "conserve sa structure : un délai est accordé contre une transformation "
  "attendue. Mais la nature du pari change du tout au tout, et c’est le point "
  "décisif d’une copie. Dans le cas de l’industrie naissante, le handicap est "
  "un seuil d’échelle non encore franchi : il est identifiable, mesurable, et "
  "l’on sait ce que la protection doit produire. Dans le cas de l’industrie "
  "vieillissante, le handicap est généralement structurel — un écart de coûts "
  "salariaux, une technologie dépassée, une position perdue dans la chaîne de "
  "valeur — et rien ne garantit qu’un délai suffise à le renverser. La "
  "protection peut alors financer deux choses très différentes : une "
  "restructuration réelle, qui déplace la branche vers des segments de gamme "
  "moins exposés, ou le simple maintien d’une activité condamnée, ce que le "
  "cours nomme l’entretien de « canards boiteux ». Le coût collectif est élevé "
  "dans les deux cas ; seul le second est pure perte. Il faut enfin noter que "
  "cette protection répond à un problème que la théorie du commerce ne traite "
  "pas bien : la concentration territoriale et sociale des pertes, qui rend "
  "l’ajustement politiquement inacceptable même lorsqu’il est économiquement "
  "souhaitable.",
  [("L’érosion de l’avantage et la menace de disparition",
    "La branche perd en compétitivité face à des producteurs étrangers moins "
    "coûteux ou plus avancés. Les parts de marché reculent, les marges se "
    "compriment, l’investissement s’arrête, ce qui accélère encore le déclin."),
   ("Le délai accordé par la protection",
    "La mesure ralentit la pénétration des importations et stabilise la demande "
    "adressée à la branche. Elle ne restaure pas la compétitivité : elle achète "
    "du temps, dont l’usage détermine le résultat final."),
   ("La bifurcation : restructuration ou survie",
    "Le temps obtenu peut servir à moderniser l’outil, à monter en gamme, à "
    "réorienter la production — ou à ne rien changer. Rien dans l’instrument ne "
    "détermine la branche choisie ; seuls la conditionnalité et le calendrier le "
    "font."),
   ("Le coût collectif et l’immobilisation de facteurs",
    "La protection fait supporter un prix plus élevé aux consommateurs et aux "
    "entreprises utilisatrices, et maintient du travail et du capital dans une "
    "activité peu productive, ce qui les détourne des secteurs en croissance.")],
  [{'a': "La protection temporaire peut faciliter une reconversion ou une montée "
         "en gamme que l’ajustement brutal rendrait impossible.",
    'cond': "La branche doit disposer d’un segment de marché atteignable où elle "
            "redeviendrait compétitive, et la protection doit être assortie "
            "d’engagements d’investissement vérifiables.",
    'lim': "Lorsque le désavantage est structurel, aucun délai ne le renverse : "
           "la protection finance alors un report, pas une transformation."},
   {'a': "Elle réduit le coût social et territorial d’un ajustement brutal, dont "
         "les effets sont cumulatifs et difficilement réversibles.",
    'cond': "Le délai doit être utilisé par des politiques de formation, de "
            "reconversion et de mobilité agissant simultanément.",
    'lim': "Si l’accompagnement social n’accompagne pas la protection, celle-ci "
           "préserve l’emploi sans préparer l’après, et le choc différé sera "
           "subi dans les mêmes conditions."},
   {'a': "Elle préserve des capacités productives dont la disparition serait "
         "irréversible, notamment lorsqu’une filière entière en dépend.",
    'cond': "L’argument suppose que la capacité soit réellement stratégique pour "
            "l’aval, et non simplement ancienne.",
    'lim': "La qualification de « stratégique » est politiquement élastique : "
           "elle tend à s’étendre à toute branche capable de se faire entendre."}],
  [{'t': "La protection des industries en déclin entretient des « canards "
         "boiteux » : elle maintient artificiellement des activités "
         "structurellement non compétitives.",
    'qui': "Limite posée explicitement dans le cours à la suite de Kaldor.",
    'rep': "L’objection est juste mais ne vise que l’usage non conditionnel de "
           "l’instrument. Elle impose une clause d’extinction et une évaluation, "
           "non l’abandon de tout accompagnement."},
   {'t': "Mieux vaut transférer directement des revenus aux salariés concernés "
         "que protéger la branche par les prix.",
    'qui': "Conséquence de l’analyse en surplus : la protection par les prix est "
           "un instrument coûteux et imprécis.",
    'rep': "L’argument est solide en théorie ; en pratique, le transfert "
           "monétaire ne reconstitue ni le capital humain spécifique ni le tissu "
           "productif local, ce qui explique sa faible acceptabilité."}],
  [{'n': "Nicholas Kaldor",
    'i': "Transposer aux industries vieillissantes la logique de la protection "
         "temporaire (1966).",
    'p': "Protéger temporairement une branche menacée par la concurrence pour "
         "permettre sa reconversion ou sa montée en gamme : la justification "
         "reste la transformation attendue, jamais la préservation en l’état."},
   {'n': "Nicholas Kaldor",
    'i': "La limite est intégrée au raisonnement : la mesure devient coûteuse "
         "lorsqu’elle maintient des activités structurellement non compétitives.",
    'p': "Le risque des « canards boiteux » n’est pas une critique extérieure "
         "mais la contrepartie reconnue de l’instrument, ce qui impose d’en "
         "borner strictement la durée."},
   {'n': "Friedrich List",
    'i': "L’argument de la protection temporaire visait initialement les "
         "industries naissantes.",
    'p': "La comparaison des deux usages éclaire leur différence : chez List le "
         "handicap est un seuil à franchir, chez Kaldor un désavantage à "
         "renverser — le premier pari est plus favorable que le second."}],
  [{'f': "Le cours décrit l’enchaînement : activité maintenue artificiellement, "
         "coût collectif élevé, risque d’entretenir des « canards boiteux ».",
    'p': "Il fournit le critère d’échec et rappelle que le coût est diffus alors "
         "que le bénéfice est concentré sur une branche identifiable."},
   {'f': "Le cours admet qu’une protection temporaire puisse ralentir la "
         "disparition d’activités vieillissantes, en précisant qu’il s’agit d’un "
         "accompagnement et non d’un protectionnisme éducateur.",
    'p': "La distinction terminologique a une portée analytique : elle interdit "
         "de justifier l’accompagnement d’une branche en déclin par l’argument "
         "de List, qui suppose une compétitivité future."}],
  [{'q': "Sujet du type « Faut-il protéger les industries naissantes ou les "
         "industries vieillissantes ? »",
    'f': "Les deux protections partagent la même forme — un délai contre une "
         "transformation — mais pas la même probabilité de succès : l’industrie "
         "naissante doit franchir un seuil identifiable, l’industrie "
         "vieillissante doit renverser un désavantage souvent structurel. "
         "Protéger la seconde relève donc davantage de la politique sociale que "
         "de la politique industrielle, ce qui ne la disqualifie pas mais change "
         "le critère d’évaluation.",
    'r': "On compare la nature du handicap à surmonter plutôt que la "
         "légitimité des bénéficiaires, ce qui permet de hiérarchiser les deux "
         "politiques selon leur probabilité de succès et de conclure sans "
         "moraliser le débat.",
    'ex': "Krugman et le seuil Q0 d’un côté, Kaldor et les « canards boiteux » "
          "de l’autre."},
   {'q': "Sujet du type « Peut-on prospérer sans industrie ? »",
    'f': "La question du déclin industriel ne se réduit pas à un arbitrage entre "
         "protection et ouverture : elle porte sur la capacité d’une économie à "
         "conserver des capacités productives dont dépendent l’innovation, les "
         "exportations et des filières entières situées en aval.",
    'r': "Relier la protection des branches en déclin à la question des "
         "capacités productives permet de dépasser le cadre purement "
         "commercial du sujet et de poser la vraie question : que perd une "
         "économie lorsqu’une filière disparaît entièrement de son "
         "territoire ?",
    'ex': "Le projet européen d’Industrial Accelerator Act vise 20 % du PIB "
          "européen pour l’industrie d’ici 2035."}],
  voisins=['le28-defensif', 'le28-educateur', 'le28-temporaire-permanent',
           'le28-couts-ouverture', 'le28-rente'])

# ---------------------------------------------------------------- 28.11
d('le28-temporaire-permanent', 28,
  "Protectionnisme temporaire et protectionnisme permanent",
  "La durée n’est pas un détail d’application : elle change la nature de la mesure",
  "Le protectionnisme temporaire est une protection bornée dans le temps, "
  "justifiée par une transformation attendue de la branche protégée. Le "
  "protectionnisme permanent est une protection reconduite sans terme, qui "
  "devient un transfert durable des consommateurs vers les producteurs abrités. "
  "La différence n’est pas d’intensité mais de nature : la première est un "
  "investissement, la seconde une rente.",
  "La condition de temporalité est, chez List, la condition essentielle : la "
  "protection doit disparaître lorsque l’industrie atteint sa maturité. Elle "
  "l’est pour une raison économique précise. Une protection temporaire modifie "
  "les anticipations de l’entreprise abritée : sachant que l’exposition "
  "surviendra, elle investit pour y survivre. Une protection perçue comme "
  "permanente produit l’effet inverse : l’entreprise n’a plus d’incitation à "
  "réduire ses coûts, et l’investissement le plus rentable devient le lobbying "
  "destiné à maintenir l’abri. Le cours décrit précisément cet enchaînement : "
  "protection permanente, rente, lobbying, absence d’innovation, gaspillage des "
  "ressources. Le problème pratique est que la temporalité annoncée n’est pas "
  "la temporalité effective. Dès qu’une protection existe, elle crée des "
  "intérêts organisés qui ont tout à gagner à sa prolongation, tandis que ses "
  "victimes — consommateurs, entreprises en aval — sont dispersées et peu "
  "mobilisées. L’asymétrie entre bénéfices concentrés et coûts diffus rend la "
  "sortie politiquement plus difficile que l’entrée. C’est pourquoi la question "
  "pertinente n’est pas « faut-il protéger temporairement ? » mais « quels "
  "dispositifs rendent la sortie crédible ? » : dégressivité automatique "
  "inscrite dès l’origine, clause d’extinction, évaluation indépendante, "
  "conditionnalité des aides à des résultats vérifiables.",
  [("L’effet d’annonce sur les anticipations",
    "Une protection annoncée comme temporaire et crédible conduit l’entreprise à "
    "investir pour affronter l’exposition future. La même protection perçue "
    "comme reconductible supprime cette incitation."),
   ("La constitution d’intérêts organisés",
    "La protection crée immédiatement une rente dont bénéficie un groupe "
    "identifiable, qui s’organise pour la préserver. Plus la mesure dure, plus "
    "ce groupe devient influent."),
   ("L’asymétrie entre bénéficiaires et payeurs",
    "Les bénéfices sont concentrés sur une branche, les coûts dispersés entre "
    "des millions de consommateurs. La mobilisation politique est donc "
    "structurellement déséquilibrée en faveur du maintien."),
   ("Les dispositifs d’engagement",
    "Dégressivité programmée, clause d’extinction automatique, conditionnalité "
    "liée à des indicateurs vérifiables et évaluation indépendante permettent de "
    "rendre la sortie moins dépendante d’une décision politique ultérieure.")],
  [{'a': "La protection temporaire peut être économiquement rationnelle : elle "
         "finance un apprentissage ou un franchissement de seuil dont le gain "
         "futur excède le coût présent.",
    'cond': "Le gain futur doit être identifiable et plausible, et la date de "
            "sortie doit être fixée au moment où la protection est accordée, "
            "non négociée ensuite.",
    'lim': "Le calcul suppose de comparer un coût certain et immédiat à un gain "
           "incertain et différé, ce qui rend l’évaluation fragile et "
           "manipulable."},
   {'a': "Une protection permanente peut se justifier dans des cas très "
         "restreints, lorsque l’objectif poursuivi n’est pas la compétitivité "
         "mais la sécurité d’approvisionnement.",
    'cond': "Il faut que la dépendance évitée soit réellement critique et que le "
            "surcoût soit explicitement assumé comme une prime d’assurance.",
    'lim': "La justification sécuritaire est extensible à volonté : sans critère "
           "strict, elle permet de pérenniser n’importe quelle protection."},
   {'a': "La dégressivité programmée concilie délai et incitation : elle donne du "
         "temps tout en rendant l’échéance certaine.",
    'cond': "Le calendrier doit être inscrit dans la mesure initiale et son "
            "exécution soustraite à une renégociation annuelle.",
    'lim': "Aucun dispositif juridique n’empêche un gouvernement ultérieur de "
           "revenir sur l’engagement, surtout lors d’un choc conjoncturel."}],
  [{'t': "Toute protection temporaire devient permanente : l’histoire des "
         "politiques commerciales le montre.",
    'qui': "Argument de recherche de rente développé dans le cours.",
    'rep': "La régularité est réelle mais pas universelle ; elle dépend des "
           "dispositifs d’engagement. L’argument plaide pour mieux concevoir les "
           "mesures, non pour refuser toute protection."},
   {'t': "Fixer une échéance est illusoire puisque l’industrie protégée aura "
         "toujours une raison de demander un délai supplémentaire.",
    'qui': "Observation du cours : les entreprises protégées cherchent à "
           "maintenir politiquement leur protection même lorsqu’elle n’est plus "
           "justifiée.",
    'rep': "C’est pourquoi l’extinction doit être automatique plutôt que "
           "décidée : une mesure qui expire d’elle-même déplace la charge de "
           "l’initiative politique vers ceux qui veulent la prolonger."}],
  [{'n': "Friedrich List",
    'i': "La condition essentielle est la temporalité : la protection doit "
         "disparaître lorsque l’industrie atteint sa maturité.",
    'p': "Sans cette condition, le protectionnisme éducateur cesse d’être "
         "éducateur : il protège l’inefficacité plutôt que l’apprentissage, ce "
         "qui en fait l’exact contraire de ce qu’il prétend être."},
   {'n': "Paul Krugman",
    'i': "Le seuil d’échelle fournit un critère objectif pour fixer la date "
         "de sortie de la protection, indépendamment du rapport de force "
         "politique.",
    'p': "Une fois le seuil franchi, l’industrie est compétitive sans "
         "protection : le modèle indique donc non seulement qu’il faut sortir, "
         "mais à quel moment, ce qui rend l’engagement plus facile à formuler."}],
  [{'f': "Le cours décrit l’enchaînement : protection permanente, rente, "
         "lobbying, absence d’innovation, gaspillage des ressources.",
    'p': "Cette séquence est le mécanisme central à citer pour montrer que la "
         "durée transforme la nature économique d’une même mesure."},
   {'f': "Le régime de quotas textiles de l’accord multifibres, entré en vigueur "
         "en 1974, n’a pris fin que le 1ᵉʳ janvier 2005, au terme d’un "
         "démantèlement de dix ans décidé à l’Uruguay Round.",
    'p': "Plus de trente ans séparent la mise en place d’un dispositif présenté "
         "comme transitoire de sa suppression : l’exemple chiffre la difficulté "
         "réelle de sortir d’une protection."}],
  [{'q': "Sujet du type « Comment empêcher une protection temporaire de devenir "
         "permanente ? »",
    'f': "Le problème est un problème d’engagement, non de volonté : dès qu’une "
         "protection existe, elle crée un groupe organisé qui a intérêt à sa "
         "prolongation et dont les coûts sont supportés par une masse dispersée "
         "de consommateurs. La sortie doit donc être rendue automatique au "
         "moment même où la protection est accordée.",
    'r': "On raisonne en économie politique plutôt qu’en économie pure : ce sont "
         "les incitations des acteurs, et non la justification initiale, qui "
         "déterminent la durée effective.",
    'ex': "L’accord multifibres de 1974, dont le régime de quotas n’a pris fin "
          "qu’au 1ᵉʳ janvier 2005."},
   {'q': "Sujet du type « Quelles sont les conditions d’efficacité d’une "
         "protection temporaire ? »",
    'f': "Quatre conditions se dégagent : une industrie dont la compétitivité "
         "future est plausible, un marché intérieur suffisant pour atteindre "
         "l’échelle, le maintien de la concurrence à l’intérieur du marché "
         "protégé, et une échéance crédible fixée dès l’origine. L’absence d’une "
         "seule suffit à transformer la protection en rente.",
    'r': "Énoncer les conditions comme une liste vérifiable permet d’évaluer "
         "n’importe quelle mesure concrète plutôt que de discuter le "
         "principe, et transforme une question doctrinale en grille "
         "d’analyse applicable à un cas.",
    'ex': "Les quatre causes d’échec recensées par le cours : protection "
          "permanente, suppression de la concurrence interne, marché national "
          "insuffisant, industrie qui ne devient jamais compétitive."}],
  voisins=['le28-educateur', 'le28-rente', 'le28-vieillissantes',
           'le28-ouverture-progressive', 'le28-sauvegarde'])

# ---------------------------------------------------------------- 28.12
d('le28-selectif-generalise', 28,
  "Protectionnisme sélectif et protectionnisme généralisé",
  "Protéger un secteur ou fermer une économie : deux politiques sans rapport",
  "Le protectionnisme sélectif vise un nombre restreint de produits, de secteurs "
  "ou de partenaires ; le protectionnisme généralisé élève les barrières sur "
  "l’ensemble des importations. La distinction est décisive parce que les "
  "effets, les justifications et les ripostes diffèrent radicalement : la "
  "plupart des arguments théoriques en faveur de la protection ne valent que "
  "pour des mesures sélectives.",
  "Tous les arguments sérieux du protectionnisme sont sectoriels. L’argument de "
  "List vise une industrie naissante précise ; celui de Kaldor une branche "
  "vieillissante précise ; celui de Brander et Spencer un oligopole précis ; les "
  "droits antidumping une pratique précise. Aucun ne justifie une élévation "
  "uniforme des barrières, pour une raison simple : le gain attendu provient "
  "d’un mécanisme particulier — seuil d’échelle, reconversion, déplacement de "
  "profit, correction d’une distorsion — qui n’existe pas dans l’ensemble des "
  "branches. Le protectionnisme généralisé relève d’une autre logique, "
  "macroéconomique ou politique : réduire les fuites d’une relance, restaurer un "
  "excédent, affirmer une souveraineté. Ses effets sont aussi d’une autre "
  "nature. Une protection sélective renchérit un produit et peut pénaliser la "
  "filière située en aval ; une protection généralisée renchérit l’ensemble des "
  "intrants importés, dégrade la compétitivité de tous les exportateurs, et "
  "appelle des représailles proportionnées. S’y ajoute une différence "
  "d’économie politique : la protection sélective est négociable et peut rester "
  "dans le cadre des règles multilatérales, tandis que la protection généralisée "
  "constitue une rupture visible qui déclenche la riposte. Enfin, la "
  "sélectivité a son propre défaut : elle désigne des gagnants, donc elle "
  "appelle le lobbying de ceux qui veulent en être.",
  [("Le ciblage sur un mécanisme identifié",
    "Une mesure sélective s’appuie sur un raisonnement propre au secteur visé : "
    "seuil d’échelle, distorsion de concurrence, dépendance critique. Sa "
    "justification est vérifiable, donc discutable."),
   ("La diffusion du coût par les consommations intermédiaires",
    "Une protection généralisée renchérit tous les intrants importés : chaque "
    "entreprise exportatrice voit ses coûts augmenter, ce qui dégrade la "
    "compétitivité y compris des secteurs qu’on ne cherchait pas à protéger."),
   ("L’ampleur de la riposte",
    "Une mesure ciblée appelle une riposte ciblée, souvent négociable ; une "
    "mesure générale appelle une riposte générale, qui frappe les exportations "
    "les plus performantes du pays initiateur."),
   ("La course à l’exemption",
    "La sélectivité crée une frontière entre secteurs protégés et non protégés, "
    "donc une incitation puissante à obtenir d’y figurer. Le choix des secteurs "
    "devient un enjeu politique autant qu’économique.")],
  [{'a': "La protection sélective permet d’appliquer un argument théorique là où "
         "il est valide, sans en étendre les coûts à l’ensemble de l’économie.",
    'cond': "Le secteur visé doit correspondre au mécanisme invoqué, et la "
            "mesure doit être proportionnée à l’écart qu’elle prétend corriger.",
    'lim': "La sélection est capturable : les secteurs retenus sont souvent les "
           "mieux organisés plutôt que ceux où l’argument s’applique."},
   {'a': "La protection généralisée peut se concevoir comme instrument "
         "macroéconomique, pour réduire les fuites d’une relance ou corriger un "
         "déséquilibre extérieur.",
    'cond': "Économie en sous-emploi, capacités de production disponibles, "
            "absence de représailles — conditions rarement réunies simultanément.",
    'lim': "Son caractère non coopératif la rend instable : si les partenaires "
           "répliquent, la demande extérieure se contracte et le gain disparaît."},
   {'a': "La sélectivité est plus compatible avec les règles multilatérales, qui "
         "prévoient des instruments ciblés — sauvegardes, antidumping, droits "
         "compensateurs.",
    'cond': "Il faut respecter les critères juridiques applicables et accepter "
            "le contrôle qui les accompagne.",
    'lim': "Ces instruments peuvent être détournés pour obtenir une protection "
           "ordinaire sous couvert de correction d’une distorsion."}],
  [{'t': "La sélectivité est illusoire : protéger un secteur en pénalise "
         "nécessairement d’autres, en aval ou par les représailles.",
    'qui': "Conséquence des effets de filière et du risque de riposte signalés "
           "dans le cours.",
    'rep': "L’objection rappelle qu’aucune protection n’est neutre, mais la "
           "comparaison pertinente reste entre une mesure ciblée et une mesure "
           "générale : les effets indirects de la seconde sont d’un tout autre "
           "ordre de grandeur."},
   {'t': "La sélectivité ouvre la porte au clientélisme : elle fait du choix des "
         "secteurs un marché politique.",
    'qui': "Argument de recherche de rente, présent dans le cours à propos du "
           "lobbying des entreprises protégées.",
    'rep': "Le remède est procédural : critères publics, évaluation "
           "indépendante, durée limitée. Une protection générale évite le "
           "clientélisme en généralisant le coût, ce qui est pire."}],
  [{'n': "Friedrich List",
    'i': "La protection vise une phase et des branches précises, non l’ensemble "
         "de l’économie.",
    'p': "La doctrine listienne est intrinsèquement sélective et séquentielle : "
         "elle protège l’industrie naissante pendant le démarrage, pas "
         "l’agriculture ni les branches déjà matures."},
   {'n': "James Brander",
    'i': "La politique commerciale stratégique ne vaut que dans des marchés "
         "oligopolistiques identifiés.",
    'p': "Le mécanisme de déplacement de profit suppose un nombre restreint de "
         "firmes et des profits à capter : appliqué à un secteur concurrentiel, "
         "il n’a aucun fondement."}],
  [{'f': "Les règles commerciales prévoient des instruments explicitement ciblés "
         "— droits antidumping, droits compensateurs, clauses de sauvegarde.",
    'p': "L’architecture multilatérale admet donc la sélectivité encadrée tout "
         "en prohibant la discrimination générale, ce qui traduit la différence "
         "de nature entre les deux formes de protection."},
   {'f': "Le droit de douane moyen de 15,9 % dans l’agriculture contre environ "
         "3 % dans l’industrie en 2019 illustre une protection fortement "
         "sélective.",
    'p': "L’écart montre que le protectionnisme contemporain est sectoriel et "
         "résulte de rapports de force internes autant que de raisonnements "
         "économiques."}],
  [{'q': "Sujet du type « Le protectionnisme est-il toujours néfaste ? »",
    'f': "Juger le protectionnisme en bloc revient à confondre deux politiques "
         "sans rapport : une protection sélective appuyée sur un mécanisme "
         "identifié, et une fermeture générale dont les coûts se diffusent par "
         "les consommations intermédiaires et appellent des représailles "
         "proportionnées.",
    'r': "La distinction fournit un principe de tri : on évalue chaque "
         "mesure selon la validité du mécanisme invoqué dans le secteur "
         "visé, ce qui permet d’approuver certaines protections ciblées tout "
         "en rejetant la fermeture générale.",
    'ex': "L’écart entre 15,9 % de droits agricoles et 3 % de droits industriels "
          "en 2019."},
   {'q': "Sujet du type « Un pays peut-il améliorer sa situation par la "
         "protection sans dégrader celle de ses partenaires ? »",
    'f': "La réponse dépend de l’ampleur de la mesure : une protection ciblée "
         "corrigeant une distorsion avérée peut être acceptée dans le cadre "
         "multilatéral, tandis qu’une protection généralisée est perçue comme "
         "une rupture et appelle une riposte qui annule le gain recherché.",
    'r': "On relie l’ampleur de la mesure à la probabilité de représailles, "
         "ce qui transforme une question de principe en question stratégique "
         ": l’effet d’une protection dépend de la réaction des partenaires "
         "autant que de son contenu.",
    'ex': "Les sauvegardes et droits compensateurs, prévus par les règles, "
          "s’opposent aux hausses générales de droits qui déclenchent les "
          "guerres commerciales."}],
  voisins=['le28-protectionnisme', 'le28-droits-douane', 'le28-representailles',
           'le28-sauvegarde', 'le28-rente'])

# ---------------------------------------------------------------- 28.13
d('le28-droits-douane', 28, "Protectionnisme tarifaire : droits de douane",
  "L’instrument le plus transparent, et le plus facile à mesurer",
  "Un droit de douane est un impôt prélevé lors de l’importation d’un bien. Il "
  "renchérit le produit étranger sur le marché intérieur, réoriente une partie "
  "de la demande vers les producteurs nationaux et procure une recette à "
  "l’État. C’est l’instrument protectionniste le plus visible, le plus "
  "mesurable et le plus facilement négociable — trois propriétés qui expliquent "
  "qu’il ait été au centre des négociations commerciales multilatérales.",
  "L’analyse d’un droit de douane se fait en termes de surplus, et c’est la "
  "seule façon rigoureuse d’en évaluer le bilan. La hausse du prix intérieur "
  "augmente le surplus des producteurs nationaux, qui vendent davantage et plus "
  "cher ; elle réduit le surplus des consommateurs, qui paient davantage et "
  "consomment moins ; elle procure une recette à l’État, égale au droit "
  "multiplié par le volume importé restant. La somme de ces trois effets est "
  "négative : une partie du surplus perdu par les consommateurs n’est transférée "
  "à personne. Elle correspond d’une part à une production nationale réalisée à "
  "un coût supérieur au prix mondial, d’autre part à une consommation qui "
  "disparaît. Ce résultat statique est robuste, mais il doit être complété par "
  "trois considérations. La première est l’effet de filière : lorsque le bien "
  "taxé est un intrant, le droit renchérit la production des entreprises en "
  "aval, qui perdent en compétitivité. La deuxième est la réaction des "
  "partenaires : une hausse appelle des représailles qui frappent les "
  "exportations. La troisième est dynamique : si la protection permet "
  "d’atteindre un seuil d’échelle, la perte statique peut être compensée par un "
  "gain futur — c’est tout l’enjeu du protectionnisme éducateur. Le bilan d’un "
  "droit de douane ne se lit donc jamais sur le seul graphique des surplus.",
  [("La hausse du prix intérieur",
    "Le droit s’ajoute au prix mondial : le produit importé devient plus cher "
    "sur le marché national, ce qui permet aux producteurs nationaux de vendre à "
    "un prix plus élevé que sans protection."),
   ("Le transfert vers les producteurs et l’État",
    "Les producteurs nationaux gagnent en volume et en marge ; l’État encaisse "
    "le droit sur les importations restantes. Ces deux gains sont des transferts "
    "prélevés sur les consommateurs."),
   ("La perte sèche",
    "Une partie du surplus perdu n’est transférée à personne : elle correspond à "
    "des unités produites nationalement à un coût supérieur au prix mondial, et "
    "à une consommation renoncée. C’est le coût net pour la collectivité."),
   ("L’effet sur les entreprises utilisatrices",
    "Si le bien taxé entre dans la production d’autres biens, les entreprises "
    "situées en aval supportent un coût d’intrant plus élevé et perdent en "
    "compétitivité, y compris à l’exportation."),
   ("La riposte des partenaires",
    "Les pays affectés peuvent relever leurs propres droits sur les exportations "
    "du pays initiateur, ce qui réduit ses débouchés et peut annuler le gain "
    "sectoriel recherché.")],
  [{'a': "Le droit de douane procure une recette fiscale, argument "
         "particulièrement pertinent lorsque la base fiscale intérieure est "
         "étroite.",
    'cond': "Il faut que les importations restent significatives : un droit "
            "prohibitif ne rapporte rien, puisqu’il supprime l’assiette.",
    'lim': "Le prélèvement pèse sur la consommation, souvent de manière "
           "régressive, et décroît à mesure que le droit atteint son objectif "
           "protecteur."},
   {'a': "Il est transparent et mesurable, donc négociable : c’est ce qui a rendu "
         "possible la libéralisation multilatérale par concessions réciproques.",
    'cond': "La transparence suppose que la protection passe effectivement par "
            "le tarif, et non par des barrières non tarifaires plus difficiles à "
            "chiffrer.",
    'lim': "Sa visibilité même en fait la cible privilégiée des représailles : "
           "ce qui se mesure se riposte facilement."},
   {'a': "Comparé au quota, il laisse jouer le mécanisme de prix et transfère la "
         "rente à l’État plutôt qu’à des opérateurs privés.",
    'cond': "L’avantage suppose que le droit soit effectivement perçu et que les "
            "procédures douanières ne créent pas elles-mêmes une barrière "
            "supplémentaire.",
    'lim': "Il demeure coûteux pour les consommateurs : le fait que la rente "
           "soit publique améliore la répartition du coût, pas son montant."}],
  [{'t': "Le droit de douane est payé par les consommateurs nationaux, non par "
         "l’exportateur étranger.",
    'qui': "Résultat de l’analyse en surplus développée dans le cours.",
    'rep': "L’incidence réelle dépend des élasticités : un pays assez grand peut "
           "faire baisser le prix mondial et reporter une partie du droit sur "
           "l’exportateur. Le cas est réel mais restreint, et il appelle des "
           "représailles."},
   {'t': "Le droit protège un secteur en pénalisant ceux qui utilisent son "
         "produit comme intrant.",
    'qui': "Effet de filière, signalé dans le cours à propos des entreprises "
           "importatrices.",
    'rep': "L’objection impose d’examiner la position du bien dans la chaîne de "
           "valeur avant de conclure : protéger un bien final et protéger un "
           "bien intermédiaire n’ont pas le même bilan."},
   {'t': "Les droits de douane sont contournables : les firmes réorganisent "
         "leurs chaînes de valeur ou transitent par des pays tiers.",
    'qui': "Le cours note que les mesures protectionnistes peuvent être "
           "contournées par les firmes.",
    'rep': "Le contournement réduit l’efficacité protectrice sans supprimer le "
           "coût pour le consommateur : la mesure peut donc échouer tout en "
           "restant coûteuse."}],
  [{'n': "David Ricardo",
    'i': "Le droit de douane éloigne la spécialisation de celle que commandent "
         "les coûts comparés.",
    'p': "En renchérissant l’importation, il maintient une production nationale "
         "dont le coût d’opportunité est plus élevé que le prix mondial : la "
         "perte d’efficience est le pendant exact du gain à l’échange."},
   {'n': "Paul Krugman",
    'i': "Le droit de douane peut être l’instrument qui permet de franchir un "
         "seuil d’échelle.",
    'p': "Dans l’exemple vietnamien du cours, droits de douane ou restriction "
         "des importations chinoises réorientent la demande vers les producteurs "
         "domestiques, font croître la production et abaissent le coût moyen."},
   {'n': "Edward Luttwak",
    'i': "Les droits de douane contemporains peuvent viser un objectif "
         "stratégique plutôt que sectoriel.",
    'p': "Les droits américains récents dépassent la protection de l’emploi : ils "
         "visent la domination technologique et le rapport de force, ce qui "
         "interdit de les évaluer avec les seuls outils de l’analyse en surplus."}],
  [{'f': "Les droits de douane moyens sur les produits manufacturés dans les "
         "économies avancées passent d’environ 40 % en 1947 à environ 4 % à "
         "l’issue de l’Uruguay Round.",
    'p': "L’ampleur de la baisse mesure le résultat du marchandage multilatéral "
         "et rappelle que le tarif a été l’objet central des négociations, "
         "précisément parce qu’il est chiffrable."},
   {'f': "En 2019, le droit de douane moyen atteint 15,9 % du prix dans "
         "l’agriculture contre environ 3 % dans l’industrie.",
    'p': "La protection tarifaire résiduelle est concentrée sur l’agriculture, "
         "ce qui explique que ce secteur reste le point de blocage des "
         "négociations."},
   {'f': "Les cibles successives des rounds du GATT portent le droit moyen à "
         "environ 12 % en 1962, puis 7 %, puis 5 %.",
    'p': "La progression par paliers négociés illustre la logique de réciprocité "
         "et le caractère graduel de la libéralisation tarifaire."}],
  [{'q': "Sujet du type « Les subventions peuvent-elles être plus efficaces que "
         "les droits de douane ? »",
    'f': "Le droit de douane et la subvention poursuivent le même but mais "
         "n’ont pas la même incidence : le premier fait payer le consommateur et "
         "renchérit les intrants de toute la filière en aval, la seconde fait "
         "payer le contribuable sans distordre le prix relatif à la "
         "consommation. À objectif donné, la subvention est généralement moins "
         "coûteuse en efficience.",
    'r': "La comparaison porte sur l’incidence et sur le nombre de distorsions "
         "introduites, ce qui donne un critère clair de hiérarchisation des "
         "instruments.",
    'ex': "Brander et Spencer raisonnent d’ailleurs sur un instrument relevant "
          "en pratique largement de la subvention, notamment à la recherche."},
   {'q': "Sujet du type « Qui paie le protectionnisme ? »",
    'f': "L’analyse en surplus répond précisément : les consommateurs paient, "
         "les producteurs protégés et l’État reçoivent, et une partie de ce qui "
         "est perdu n’est transférée à personne. S’y ajoutent les entreprises "
         "utilisatrices du bien protégé, dont le coût d’intrant augmente.",
    'r': "Partir de la décomposition des surplus permet de répondre sans "
         "généralité : chaque catégorie d’agent est traitée séparément.",
    'ex': "Le droit agricole moyen de 15,9 % en 2019 pèse d’abord sur les "
          "consommateurs et sur les exportateurs agricoles des pays en "
          "développement."}],
  voisins=['le28-protectionnisme', 'le28-non-tarifaire', 'le28-subventions',
           'le28-couts-protectionnisme', 'le28-representailles'])
