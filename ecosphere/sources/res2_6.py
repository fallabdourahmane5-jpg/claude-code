# -*- coding: utf-8 -*-
"""Résumé approfondi du chapitre 6 — La croissance économique."""

R = {'6': {

 'q': "D’où vient la croissance, pourquoi n’est-elle ni spontanée, ni continue, ni également "
      "partagée, et peut-elle se poursuivre sous contrainte écologique ?",

 'ess':
  "Le chapitre avance en quatre temps : décrire, décomposer, expliquer, soutenir. On définit "
  "d’abord la croissance — augmentation soutenue du PIB en volume — et on la distingue du "
  "développement, avant de rappeler qu’elle est historiquement récente, cumulative et "
  "inégalement répartie dans le temps comme dans l’espace. On examine ensuite les trajectoires "
  "d’industrialisation, de Rostow à Gerschenkron, puis la possibilité d’un épuisement : "
  "stagnation séculaire, croissance potentielle en baisse. Vient alors le cœur analytique du "
  "chapitre : la comptabilité de la croissance, qui décompose les 5,2 % des Trente Glorieuses "
  "françaises en 0,5 point de travail, 1,5 point de capital et 3,1 points de productivité "
  "globale des facteurs — soit 60 % de résidu inexpliqué. Ce résidu commande toute la suite : "
  "on cherche ses déterminants (démographie, durée et qualification du travail, intensité "
  "capitalistique, innovation, management, concurrence), puis on observe qu’il déplace "
  "l’emploi entre secteurs, ce qui conduit à la désindustrialisation et à la thèse "
  "hyper-industrielle de Veltz. La croissance se répartit ensuite inégalement : outils de "
  "mesure, courbe de Kuznets, courbe de l’éléphant de Milanovic. Les modèles prennent alors le "
  "relais — Harrod-Domar, Solow, croissance endogène, mauvaise allocation, institutions — "
  "avant la dernière contrainte, écologique : capital naturel, soutenabilité faible ou forte, "
  "découplage, et les critiques du récit de la transition.",

 'parties': [

  # ------------------------------------------------------------------ I
  {'t': "I. Définir la croissance et la situer historiquement",
   'sp': [
    {'t': "A. Deux définitions d’auteurs, et une distinction décisive",
     'd': ["La croissance économique est l’augmentation soutenue et durable de la production "
           "d’un pays sur longue période, mesurée par l’évolution du PIB en volume, "
           "c’est-à-dire corrigé de l’inflation : on parle de croissance réelle, non nominale.",
           "François Perroux la définit comme « l’augmentation soutenue pendant une ou "
           "plusieurs périodes longues d’un indicateur de dimension, pour une nation, le "
           "produit global net en termes réels » : quatre éléments à retenir — augmentation "
           "soutenue, longue période, mesure quantitative, termes réels. Jean Arrous insiste "
           "sur une autre dimension : la croissance est « un processus cumulatif "
           "d’interactions qui se traduit par une hausse continue de la productivité » — "
           "processus dynamique, mécanisme cumulatif, rôle central de la productivité.",
           "La distinction avec le développement est posée d’emblée : la croissance est une "
           "augmentation quantitative du PIB, une mesure comptable de dimension économique ; "
           "le développement est une amélioration des conditions de vie — santé, éducation, "
           "réduction de la pauvreté et des inégalités."],
     'lim': "La formule à retenir est que la croissance est souvent une condition nécessaire du "
            "développement, mais jamais suffisante : un pays peut croître sans réduire les "
            "inégalités, sans améliorer le bien-être et sans protéger l’environnement."},
    {'t': "B. Une croissance cumulative, récente et inégale",
     'd': ["Les faits stylisés de Kaldor désignent les régularités statistiques observées sur "
           "longue période dans plusieurs pays : ils permettent de décrire les caractéristiques "
           "de la croissance avant d’en expliquer les causes.",
           "La croissance moderne est historiquement située. Avant la révolution industrielle, "
           "le régime est celui de la stagnation : toute hausse de production est absorbée par "
           "la croissance démographique, ce qui interdit une amélioration durable du niveau de "
           "vie — c’est le régime malthusien. La rupture vient de la fin du XVIIIᵉ siècle en "
           "Angleterre, avec la machine à vapeur et la mécanisation.",
           "Elle est ensuite inégale dans le temps — diffusion progressive au XIXᵉ siècle, "
           "forte croissance des Trente Glorieuses entre 1945 et 1975, ralentissement des pays "
           "développés depuis les années 1970 — et inégale selon les pays, puisque tous "
           "n’entrent pas dans la croissance au même moment."],
     'mec': "Régime malthusien : ↑ production → ↑ population → niveau de vie inchangé. Rupture "
            "industrielle : gains de productivité durables → ↑ PIB par habitant."},
    {'t': "C. PIB total, PIB par habitant et loi de la croissance cumulée",
     'd': ["La relation fondamentale est que la croissance du PIB se décompose en croissance "
           "démographique et croissance du PIB par habitant. Un pays peut donc connaître une "
           "forte croissance du PIB total sans amélioration du niveau de vie si sa population "
           "augmente autant : le PIB par habitant est l’indicateur central du niveau de vie "
           "moyen.",
           "La croissance obéit à une logique exponentielle : avec la formule (1 + t)ⁿ, un taux "
           "de 2 % par an pendant 35 ans suffit à doubler la production. C’est le principe de "
           "cumulativité, et sa conséquence est contre-intuitive : des écarts modestes de taux "
           "produisent, sur longue période, des différences énormes de niveau de vie."]},
   ],
   'v': "Si la croissance moderne commence avec l’industrialisation, encore faut-il expliquer "
        "pourquoi certains pays décollent et d’autres non."},

  # ----------------------------------------------------------------- II
  {'t': "II. Les trajectoires d’industrialisation : Rostow contre Gerschenkron",
   'sp': [
    {'t': "A. Les cinq étapes de Rostow",
     'd': ["Rostow propose un modèle en cinq étapes. La société traditionnelle, d’organisation "
           "féodale ou autarcique, se caractérise par un faible progrès technique. Les "
           "préconditions au décollage voient apparaître l’épargne et l’entrepreneuriat. Le "
           "décollage, ou take-off, est l’étape centrale : le taux d’investissement atteint "
           "environ 10 % du PIB et des secteurs moteurs entraînent le reste de l’économie. "
           "Suit la marche vers la maturité, avec une croissance d’environ 2 % par an, une "
           "transformation profonde du système productif et une accélération du progrès "
           "technique. L’aboutissement est l’ère de la consommation de masse.",
           "Cette dernière étape n’est pas seulement économique : c’est pour Rostow un stade "
           "social et civilisationnel, l’horizon souhaitable du développement. Le contexte "
           "l’explique — il écrit dans les années 1950-1960, en pleine croissance occidentale, "
           "quand l’accès au confort matériel est récent et que le progrès technique est tenu "
           "pour intrinsèquement positif, profitant à tous."],
     'lim': "Les critiques sont nombreuses et explicites : l’analyse est descriptive et "
            "linéaire, elle ne différencie ni les formes de développement ni les spécificités "
            "nationales, elle néglige les facteurs démographiques, elle suppose l’absence de "
            "blocage — ce que contestent les économistes tiers-mondistes —, elle est trop "
            "optimiste en supposant que tous les pays atteindront la consommation de masse, et "
            "elle est ethnocentrique puisque calquée sur l’expérience occidentale."},
    {'t': "B. Gerschenkron et l’avantage du retard",
     'd': ["Gerschenkron s’intéresse aux late comers, les pays industrialisés tardivement. Sa "
           "thèse est que la trajectoire britannique n’est pas universelle : les pays en "
           "retard rattrapent autrement et parfois plus vite, en mobilisant des institutions "
           "de substitution — l’État, les banques, les grandes entreprises — là où "
           "l’Angleterre s’était appuyée sur l’initiative privée et l’épargne diffuse. Le "
           "retard peut donc devenir un avantage.",
           "Malgré leur opposition sur la linéarité, Rostow et Gerschenkron convergent sur un "
           "point essentiel : l’industrialisation est le moteur historique de la croissance, "
           "et l’accélération suppose des appuis puissants — d’où la question décisive de "
           "savoir qui finance, qui coordonne et qui organise."]},
   ],
   'v': "Une fois le décollage acquis, rien ne garantit pourtant que la croissance se "
        "poursuive : la question du ralentissement durable se pose."},

  # ---------------------------------------------------------------- III
  {'t': "III. La croissance n’est pas garantie : stagnation séculaire et croissance potentielle",
   'sp': [
    {'t': "A. La stagnation séculaire, de Hansen à Summers",
     'd': ["Le concept naît avec Alvin Hansen en 1938 : une économie développée peut connaître "
           "une phase prolongée de faible croissance. Summers le réactive en 2013 à partir "
           "d’un diagnostic précis : un excès durable de l’épargne sur l’investissement "
           "exigerait, pour rétablir l’équilibre, un taux d’intérêt d’équilibre si bas que la "
           "politique monétaire ne peut l’atteindre.",
           "Le cours rappelle l’héritage intellectuel : l’idée prolonge, sous une autre forme, "
           "l’état stationnaire de Ricardo. La crise de 2008 constitue une rupture commune aux "
           "économies développées, mais les trajectoires divergent ensuite — nettement sur "
           "l’endettement public, structurellement sur le chômage."]},
    {'t': "B. La croissance potentielle",
     'd': ["La croissance potentielle est celle que permettent les facteurs de production "
           "pleinement employés, sans choc d’offre ou de demande, sans chômage ni inflation. "
           "L’écart avec la croissance effective constitue l’output gap : lorsque la croissance "
           "effective dépasse la croissance potentielle, des tensions inflationnistes "
           "apparaissent.",
           "En France, la croissance potentielle n’est plus estimée qu’à environ 0,8 % par an "
           "sur la période 2009-2018 — ordre de grandeur qui donne sa portée concrète au débat "
           "sur la stagnation séculaire."]},
   ],
   'v': "Pour trancher ces débats, il faut d’abord savoir décomposer la croissance : d’où "
        "vient-elle exactement ?"},

  # ----------------------------------------------------------------- IV
  {'t': "IV. Décomposer la croissance : la comptabilité de la croissance",
   'sp': [
    {'t': "A. La fonction de Cobb-Douglas et la méthode",
     'd': ["Carré, Dubois et Malinvaud reprennent la démarche macroéconomique héritée de Solow "
           "et utilisent une fonction de production de type Cobb-Douglas, reliant la "
           "production Y au capital K, au travail L et à un paramètre A qui mesure le niveau "
           "de technologie, c’est-à-dire l’efficacité globale de l’économie.",
           "Deux hypothèses la fondent. Les facteurs sont substituables : on peut remplacer du "
           "travail par du capital, ou l’inverse, ce qui reflète la possibilité pour une "
           "entreprise de modifier sa combinaison productive. Et les rendements d’échelle sont "
           "constants, ce qui permet de raisonner proprement sur la croissance globale. "
           "L’intérêt de cette formalisation est opératoire : elle permet de mesurer la "
           "contribution du capital, celle du travail, et d’isoler ce qui reste inexpliqué."]},
    {'t': "B. Le résultat sur les Trente Glorieuses françaises (1951-1973)",
     'd': ["Le taux de croissance annuel moyen de la France sur la période est de 5,2 %, "
           "niveau jamais atteint avant ni retrouvé depuis. La décomposition est la suivante : "
           "l’augmentation du facteur travail — population active, emploi — explique 0,5 point "
           "de croissance, et l’accumulation de capital fixe 1,5 point. Le total expliqué par "
           "les facteurs n’est donc que de 2,1 points.",
           "Il reste 5,2 − 2,1 = 3,1 points, que l’on appelle productivité globale des "
           "facteurs : ce qui ne s’explique ni par le travail ni par le capital. Soit environ "
           "60 % de la croissance française des Trente Glorieuses. À l’époque, on interprète "
           "cette PGF comme la mesure du progrès technique : meilleure organisation du travail, "
           "innovations, gains d’efficacité, apprentissage, diffusion des technologies.",
           "Le cours signale aussi une contribution spécifique au facteur travail : le rôle "
           "décisif de la montée de l’activité féminine sur la période."],
     'mec': "5,2 % = 0,5 (travail) + 1,5 (capital) + 3,1 (PGF) ; 3,1/5,2 ≈ 60 %.",
     'lim': "Le statut du résidu est débattu, et la formulation du cours est précise : Solow "
            "parlait d’une « manne tombée du ciel », une richesse qui apparaît sans qu’on sache "
            "d’où ; d’autres répondent que la PGF mesure surtout notre ignorance, car on "
            "peine à décomposer finement ce qui relève de l’organisation, des compétences, de "
            "la technologie et des institutions."},
    {'t': "C. Croissance extensive et croissance intensive",
     'd': ["La distinction se lit directement sur la décomposition. Quand la contribution "
           "majeure vient des facteurs de production, la croissance est extensive : on produit "
           "plus parce qu’on mobilise plus de travail et de capital, sans devenir plus "
           "efficace. Quand elle vient de la PGF, la croissance est intensive : on produit plus "
           "avec les mêmes facteurs.",
           "Sur la période 2010-2021, le cours classe le Danemark et l’Allemagne du côté de la "
           "croissance intensive, la France et les États-Unis du côté de la croissance "
           "extensive."],
     'lim': "La conséquence est fondamentale : seule la croissance intensive améliore "
            "durablement le PIB par habitant, puisque l’accumulation de facteurs se heurte tôt "
            "ou tard aux rendements décroissants."},
   ],
   'v': "Puisque l’essentiel vient du résidu, l’enjeu devient d’identifier ce qui le "
        "détermine : quantité de travail, capital, et surtout productivité."},

  # ------------------------------------------------------------------ V
  {'t': "V. Les déterminants : travail, capital et productivité",
   'sp': [
    {'t': "A. Le facteur travail : démographie, durée, qualification",
     'd': ["La démographie importe parce que la population totale détermine à terme la "
           "population active, laquelle conditionne la quantité de travail disponible. S’y "
           "ajoutent la participation au marché du travail — la montée de l’activité féminine "
           "a joué un rôle décisif — et la durée du travail, variable clé de long terme : la "
           "durée légale est de 35 heures depuis 1998, applicable à 70 % des salariés, les "
           "autres relevant de 39 heures, et les congés payés sont de cinq semaines depuis "
           "1982. Deux évolutions majeures du XXᵉ siècle sont l’entrée plus tardive sur le "
           "marché du travail, liée à l’allongement des études, et la formation plus longue.",
           "L’exemple développé est celui de l’apprentissage, passé d’environ 400 000 apprentis "
           "à plus d’un million en 2024 grâce à des primes massives aux entreprises, des "
           "exonérations de cotisations et un élargissement des conditions. L’objectif est "
           "double : répondre au chômage élevé des jeunes et investir en capital humain pour "
           "améliorer leur insertion et réduire le chômage futur."],
     'lim': "Le cours soulève un débat budgétaire explicite : l’apprenti est comptabilisé dans "
            "l’emploi mais travaille moins qu’un salarié classique et reste en formation ; "
            "surtout, l’aide crée un effet d’aubaine — un problème de ciblage — lorsqu’elle "
            "subventionne des embauches qui auraient eu lieu sans elle. Elle devient alors un "
            "simple transfert financier, au coût budgétaire important et à faible efficacité "
            "marginale."},
    {'t': "B. Le facteur capital et l’intensité capitalistique",
     'd': ["L’investissement, mesuré par la formation brute de capital fixe, accroît le stock "
           "de capital par travailleur : c’est l’intensité capitalistique K/L. Son élévation "
           "est l’un des canaux par lesquels la productivité du travail augmente.",
           "Le cours liste cinq déterminants de la croissance de la productivité : la quantité "
           "d’heures travaillées, l’intensité capitalistique, le progrès technique mesuré par "
           "la PGF, la qualification, et l’organisation du travail."]},
    {'t': "C. Ce que produisent les gains de productivité, et pourquoi ils ralentissent",
     'd': ["Les gains de productivité se diffusent par plusieurs canaux : hausse des salaires, "
           "hausse des profits, baisse des prix et des coûts, et hausse des recettes de l’État. "
           "C’est le partage de ces gains qui détermine qui en bénéficie.",
           "Le ralentissement observé fait l’objet de deux explications structurelles "
           "concurrentes. Robert Gordon défend une thèse pessimiste : les grandes innovations "
           "passées — électricité, moteur thermique, eau courante, transports — ont "
           "profondément transformé la production et la vie quotidienne, tandis que les "
           "innovations numériques seraient moins transformatrices ; la productivité ne "
           "pourrait donc plus croître au même rythme, d’où une croissance durablement faible "
           "et une stagnation séculaire possible. L’hypothèse du décalage temporel est plus "
           "nuancée : il existe un délai entre l’apparition d’une innovation et ses effets sur "
           "la productivité.",
           "D’autres déterminants sont institutionnels ou organisationnels : la concurrence "
           "stimule les gains de productivité ; la taille du marché joue, dans l’héritage "
           "direct d’Adam Smith ; et les pratiques de management expliquent jusqu’à 20 % "
           "d’écart de productivité entre entreprises comparables, le management vertical et "
           "fortement hiérarchisé pouvant freiner l’innovation et l’initiative. Les "
           "comparaisons internationales montrent des gains plus élevés aux États-Unis et une "
           "progression rapide de la Chine grâce à l’investissement massif et à la montée en "
           "gamme."]},
    {'t': "D. Innovation, brevet et prix réels",
     'd': ["Le progrès technique a un double effet sur les prix, et l’enchaînement doit être "
           "respecté. L’innovation ne fait pas immédiatement baisser les prix : le brevet crée "
           "un monopole temporaire, donc des prix élevés qui permettent de récupérer les coûts "
           "de recherche et développement. C’est seulement dans un second temps, avec la "
           "diffusion massive et les économies d’échelle, que le coût unitaire baisse et que "
           "les prix réels reculent. Le progrès technique bénéficie donc in fine à la société, "
           "même s’il est d’abord capté par l’innovateur.",
           "Encore faut-il raisonner sur les bons prix. Le prix nominal est trompeur parce "
           "qu’il intègre l’inflation ; le prix réel relatif rapporte le prix au salaire "
           "horaire et mesure donc le temps de travail nécessaire pour acquérir un bien. "
           "L’exemple de Piketty est celui de la bicyclette : elle coûtait plusieurs mois de "
           "salaire au début de la période, quelques jours aujourd’hui.",
           "Le cours nuance toutefois le rôle du brevet : sa fonction économique normale est de "
           "protéger temporairement l’innovation, mais les brevets défensifs, déposés pour "
           "bloquer des concurrents, élèvent les coûts de transaction et freinent "
           "l’innovation."]},
    {'t': "E. Le diagnostic européen : le rapport Draghi",
     'd': ["Le rapport sur la compétitivité européenne établit un retard face aux grandes "
           "puissances et l’explique par trois causes : une demande insuffisante, des "
           "structures trop rigides, et un déficit d’investissement.",
           "Les solutions proposées forment une stratégie mixte : simplifier la réglementation "
           "d’un côté, lancer un plan massif d’investissement européen de l’autre, estimé à "
           "environ 800 milliards d’euros par an, ciblé sur l’innovation, la transition "
           "énergétique et les technologies."],
     'lim': "L’intérêt analytique du rapport est de combiner une dimension keynésienne — "
            "relancer la demande et moderniser l’appareil productif par l’investissement — et "
            "une dimension libérale — déréglementer et simplifier : il ne se range dans aucun "
            "camp."},
   ],
   'v': "Ces gains de productivité ne restent pas dans le secteur où ils naissent : ils "
        "déplacent l’emploi et transforment la structure productive."},

  # ----------------------------------------------------------------- VI
  {'t': "VI. Les transformations structurelles : tertiarisation et désindustrialisation",
   'sp': [
    {'t': "A. La loi des trois secteurs et le déversement",
     'd': ["La loi des trois secteurs, de Clark, Fourastié et Sauvy, explique la tertiarisation "
           "par la combinaison des gains de productivité et de l’élasticité-revenu de la "
           "demande. Dans le primaire, les gains sont élevés et la demande inélastique : "
           "l’emploi chute. Dans le secondaire, l’industrialisation crée d’abord des emplois, "
           "puis l’automatisation les réduit. Dans le tertiaire, la productivité est plus "
           "faible et la demande croissante : l’emploi augmente mécaniquement.",
           "Sauvy formalise le mécanisme du déversement dans La machine et le chômage (1980) : "
           "les gains de productivité libèrent du revenu et de la main-d’œuvre, qui se "
           "déversent vers d’autres secteurs. La chaîne historique est typique : "
           "agriculture → industrie → services. Aujourd’hui, le tertiaire représente 70 à 75 % "
           "de l’emploi dans les pays développés, l’industrie et la construction 19 à 20 %."],
     'mec': "Gains de productivité sectoriels + demande inélastique → libération de "
            "main-d’œuvre → déversement vers les secteurs à demande croissante."},
    {'t': "B. La désindustrialisation et ses trois causes",
     'd': ["Le phénomène est paradoxal : dans les années 1980-1990, la part de l’emploi "
           "industriel baisse fortement alors que la production industrielle ne s’effondre "
           "pas. Trois causes se combinent.",
           "Les gains de productivité industriels d’abord : on produit autant avec moins "
           "d’emplois. L’externalisation ensuite : des activités autrefois internes à "
           "l’industrie — comptabilité, informatique, maintenance, centres d’appels, "
           "logistique, services administratifs — sont confiées à des prestataires et "
           "basculent statistiquement dans le tertiaire, alors que l’activité productive reste "
           "liée à l’industrie. La mondialisation et les délocalisations enfin.",
           "Le cours insiste sur une distinction : délocaliser, c’est transférer une activité à "
           "l’étranger ; externaliser, c’est la confier à un tiers, en France ou ailleurs. "
           "L’effet sur les statistiques n’est donc pas le même, et l’externalisation exagère "
           "mécaniquement le recul apparent de l’industrie."]},
    {'t': "C. Veltz : nous ne sommes pas post-industriels mais hyper-industriels",
     'd': ["Pierre Veltz conteste l’illusion de la société post-industrielle. Sa thèse tient "
           "en deux mouvements : l’industrie devient servicielle — elle vend des services "
           "associés à ses produits — et les services deviennent industriels — ils reposent "
           "sur des systèmes productifs intégrés et des infrastructures lourdes.",
           "L’argument matériel est décisif : plus l’économie semble immatérielle, plus elle "
           "dépend d’infrastructures industrielles lourdes — serveurs, data centers, câbles "
           "sous-marins par lesquels transitent environ 98 % des flux mondiaux de données. "
           "Industrie et services sont donc imbriqués, non opposés.",
           "Les enjeux deviennent géopolitiques : semi-conducteurs, composants, pièces "
           "détachées, métaux et matériaux conditionnent la production. D’où trois objectifs "
           "associés à la réindustrialisation : retrouver l’autonomie stratégique, accélérer "
           "la transition écologique et améliorer le commerce extérieur."],
     'lim': "Le cours relève aussi la limite propre aux services : certains ont une "
            "productivité structurellement faible — santé, éducation, soin — ce qui pèse "
            "mécaniquement sur la productivité agrégée d’une économie tertiarisée."},
   ],
   'v': "Reste à savoir qui bénéficie de cette croissance ainsi transformée : la question de "
        "la répartition."},

  # ---------------------------------------------------------------- VII
  {'t': "VII. Croissance et inégalités : mesurer, puis interpréter",
   'sp': [
    {'t': "A. Les trois outils de mesure et leurs limites",
     'd': ["Le rapport interdécile D9/D1 repose sur la division de la population en dix "
           "groupes égaux : il compare le seuil au-dessus duquel se situent les 10 % les plus "
           "riches à celui en dessous duquel se situent les 10 % les plus pauvres. Son intérêt "
           "est d’être simple, utilisable comme outil de suivi temporel et politiquement "
           "parlant. Ses trois limites sont explicites : il ignore les inégalités "
           "intermédiaires, il ne saisit pas l’explosion du sommet, et il reste un indicateur "
           "partiel.",
           "Le coefficient de Palma rapporte la part du revenu détenue par les 10 % les plus "
           "riches à celle des 50 % les plus pauvres. Il est plus sensible aux inégalités "
           "contemporaines, car il capte précisément les transformations du sommet et du bas "
           "de la distribution, et se prête à une lecture politique directe.",
           "Le coefficient de Gini se construit à partir de la courbe de Lorenz, qui confronte "
           "la part cumulée de la population à la part cumulée du revenu qu’elle détient : "
           "plus la courbe s’éloigne de la droite d’équirépartition, plus les inégalités sont "
           "fortes. Ses limites sont aussi listées : il est peu intuitif, il ne montre pas où "
           "se situent les écarts, et il est insensible aux dynamiques internes fines.",
           "Le cours ajoute une distinction essentielle : les inégalités de revenus et les "
           "inégalités de patrimoine ne se mesurent pas de la même manière et n’évoluent pas "
           "de la même façon."],
     'lim': "Choisir l’indicateur fait donc partie de l’argument : D9/D1 lisse les extrêmes, "
            "Gini résume mal la forme de la distribution, Palma capte mieux le sommet. Citer "
            "un seul indicateur sans justifier son choix est une faiblesse."},
    {'t': "B. La courbe de Kuznets et ses limites",
     'd': ["Kuznets formule en 1955 l’hypothèse d’une relation en cloche entre développement "
           "et inégalités. Les mécanismes explicatifs sont en deux temps : dans la phase de "
           "hausse, l’industrialisation et l’exode rural créent des écarts entre secteurs "
           "modernes et traditionnels ; dans la phase de baisse, la généralisation de "
           "l’éducation, la diffusion du progrès technique et la mise en place de la "
           "redistribution réduisent ces écarts.",
           "Les faits contemporains contredisent cette trajectoire optimiste : hausse des "
           "inégalités de revenus, forte concentration des patrimoines, explosion du top 1 %."],
     'lim': "Deux limites sont retenues : la courbe n’est pas universellement vérifiée, et "
            "surtout la baisse des inégalités dépend de choix politiques — redistribution, "
            "fiscalité, droit du travail — et non d’un mécanisme automatique du développement."},
    {'t': "C. Milanovic : la courbe de l’éléphant et la rente de citoyenneté",
     'd': ["La mondialisation produit un double mouvement : convergence entre pays développés "
           "et émergents, divergence au sein des sociétés nationales. Pour le représenter, "
           "Milanovic construit la courbe de l’éléphant (1988-2008), dans Global Inequality "
           "(2016) : en abscisse la population mondiale classée par revenu initial, en "
           "ordonnée le taux de croissance du revenu réel.",
           "Trois points structurent la lecture. Les classes moyennes émergentes, "
           "principalement asiatiques, connaissent une croissance réelle de +70 à +80 %. Le "
           "top 1 % mondial gagne environ +60 %. Les classes populaires des pays du Nord "
           "stagnent autour de 0 %. Le cours insiste sur la distinction entre gains relatifs "
           "et gains absolus : un gain relatif élevé sur un revenu faible représente peu en "
           "valeur absolue, alors qu’un gain plus modeste au sommet représente des sommes "
           "considérables.",
           "Milanovic en tire la notion de rente de citoyenneté : l’essentiel de l’inégalité "
           "mondiale s’explique désormais par le pays de naissance, ce qui fait de la "
           "nationalité un facteur central d’inégalité. Une version actualisée de la courbe, "
           "publiée en 2022 sous le titre The Three Eras of Global Inequality, 1820-2020, "
           "montre une croissance mondiale plus faible et des inégalités toujours fortes au "
           "sommet."],
     'lim': "Le bilan du cours est nuancé : la mondialisation réduit les écarts entre pays et "
            "les accroît au sein des pays ; les grands gagnants sont les classes moyennes "
            "émergentes et la ploutocratie mondiale, les perdants relatifs les classes "
            "moyennes occidentales."},
    {'t': "D. La logique cumulative des patrimoines",
     'd': ["Les patrimoines obéissent à une dynamique propre : ils produisent des revenus — "
           "loyers, intérêts, dividendes — qui, réinvestis, accroissent le patrimoine, lequel "
           "produit davantage de revenus. C’est une logique cumulative, que Piketty résume par "
           "r > g : si le rendement du capital excède le taux de croissance, les patrimoines "
           "se concentrent mécaniquement.",
           "S’y ajoute la transmission intergénérationnelle, par héritage et par donation, qui "
           "reproduit la concentration d’une génération à l’autre — ce qui explique que les "
           "inégalités de patrimoine résistent mieux à la redistribution que les inégalités de "
           "revenu."]},
   ],
   'v': "Décrire et mesurer ne suffit pas : il faut des modèles qui expliquent d’où vient la "
        "croissance et pourquoi elle peut s’arrêter."},

  # --------------------------------------------------------------- VIII
  {'t': "VIII. Les modèles : de Harrod-Domar aux institutions",
   'sp': [
    {'t': "A. Harrod-Domar : la croissance sur le fil du rasoir",
     'd': ["Harrod et Domar, marqués par la crise de 1929 — Domar publie son article en "
           "1947 —, construisent un modèle post-keynésien de court terme dans lequel la "
           "croissance vient de la demande, le progrès technique est exogène et il n’existe "
           "aucun mécanisme automatique d’ajustement.",
           "Le sentier de croissance équilibrée y est un « fil du rasoir » : il dépend d’un "
           "équilibre très précis entre le taux d’épargne et le coefficient de capital, et "
           "rien ne ramène spontanément l’économie sur ce sentier. Trois impasses sont "
           "identifiées : un taux d’épargne trop élevé, un taux d’épargne trop faible, et un "
           "désalignement démographique. Les crises en découlent naturellement, et "
           "l’intervention de l’État devient nécessaire."],
     'mec': "Croissance équilibrée seulement si taux d’épargne et coefficient de capital "
            "s’accordent exactement ; tout écart s’amplifie au lieu de se corriger."},
    {'t': "B. Solow : rendements décroissants, état stationnaire et convergence",
     'd': ["Solow répond à l’instabilité de Harrod-Domar par un modèle néoclassique à "
           "rendements décroissants du capital. L’accumulation se heurte à l’amortissement : "
           "une part du capital doit être renouvelée chaque année, ce qui finit par absorber "
           "l’investissement. L’économie converge donc vers un état stationnaire où le capital "
           "par tête cesse de croître.",
           "Plusieurs leviers permettent de repousser cet état stationnaire — hausse du taux "
           "d’épargne, baisse de la croissance démographique — mais aucun ne permet une "
           "croissance soutenue du revenu par tête : seul le progrès technique le peut.",
           "Le modèle implique une convergence conditionnelle : les pays à faible stock de "
           "capital ont un rendement du capital plus élevé, donc rattrapent plus vite. Et il "
           "assigne à l’État un rôle limité : la croissance de long terme ne dépend pas "
           "structurellement de lui, les mécanismes de marché assurant la coordination."],
     'lim': "La limite centrale est admise par Solow lui-même : il montre que le progrès "
            "technique est décisif, mais ne l’explique pas — c’est un résidu exogène. C’est "
            "précisément ce que les théories de la croissance endogène chercheront à "
            "internaliser."},
    {'t': "C. La croissance endogène : capital humain, capital public, connaissance, innovation",
     'd': ["Lucas place le capital humain au centre : l’ensemble des connaissances et "
           "compétences issues de l’éducation et de la formation s’accumule, accroît la "
           "productivité future et engendre des externalités positives — une population mieux "
           "formée élève la productivité collective. La croissance devient cumulative et "
           "auto-entretenue, et l’État a un rôle dans le financement de l’éducation.",
           "Barro ajoute le capital public productif : une route profite à toutes les "
           "entreprises, la recherche publique bénéficie à l’ensemble de l’économie. C’est une "
           "réhabilitation du rôle de l’État, sous condition d’efficacité de la dépense.",
           "Romer fait de la connaissance un bien non rival : elle peut être utilisée "
           "simultanément par plusieurs agents sans diminuer, ce qui engendre des spillovers — "
           "externalités positives — et permet d’échapper aux rendements décroissants. L’État "
           "finance ou encourage l’innovation par le soutien à la recherche et développement.",
           "Aghion et Howitt formalisent enfin la destruction créatrice : l’innovation détruit "
           "les rentes existantes tout en créant de nouvelles activités. Aghion ajoute la "
           "notion de distance à la frontière technologique, qui commande la politique "
           "appropriée : loin de la frontière, il faut cibler, coordonner et imiter pour "
           "rattraper ; près de la frontière, il faut au contraire la concurrence et la "
           "liberté d’entrée pour stimuler l’innovation."],
     'lim': "Le risque que le cours souligne pour le capital humain est celui des inégalités : "
            "si l’accès à l’éducation est inégal, le mécanisme amplifie les écarts au lieu de "
            "les réduire."},
    {'t': "D. La mauvaise allocation : Banerjee, Duflo et la croissance inclusive",
     'd': ["Le point de départ est un paradoxe : le capital existe, les talents existent, les "
           "entrepreneurs existent — et pourtant la croissance ne vient pas. L’explication "
           "tient à la mauvaise allocation.",
           "Mauvaise allocation du capital matériel d’abord : le capital ne circule pas "
           "efficacement, les entreprises les moins productives survivent par relations ou "
           "favoritisme, d’où une productivité faible et une croissance freinée. Mauvaise "
           "allocation du capital humain ensuite : talents non repérés, formation inadéquate, "
           "transmission familiale inefficace.",
           "Le système financier aggrave le problème : une banque dominante et un marché "
           "financier faible limitent la diversification du risque et le capital-risque, de "
           "sorte que les projets innovants sont sous-financés ; des entreprises trop petites "
           "accèdent mal au financement et ne réalisent pas d’économies d’échelle ; et un "
           "capitalisme familial mal gouverné conduit au sous-investissement et freine "
           "l’innovation.",
           "D’où la notion de croissance inclusive : une croissance qui profite au plus grand "
           "nombre, n’est pas captée par une élite, réduit les inégalités et utilise mieux les "
           "talents disponibles — l’inclusion devient ici un facteur d’efficacité, pas "
           "seulement de justice."]},
    {'t': "E. Les institutions : North, Acemoglu et Robinson",
     'd': ["North établit que la croissance dépend de la qualité des institutions, règles "
           "formelles et informelles qui créent les incitations et réduisent les coûts de "
           "transaction. Acemoglu et Robinson en tirent l’opposition devenue centrale : les "
           "institutions inclusives favorisent l’innovation, l’investissement, les droits et "
           "la mobilité ; les institutions extractives concentrent le pouvoir et les "
           "richesses au profit d’une élite, créent une insécurité juridique et bloquent la "
           "concurrence.",
           "Le mécanisme est enchaîné : avec des institutions extractives, les élites captent "
           "les rentes, les droits de propriété sont fragiles, donc personne n’investit, "
           "personne n’innove, et le capital fuit. L’exemple historique est anglais : le "
           "passage d’un pouvoir royal fort et d’un arbitrage politique instable à une "
           "limitation du pouvoir royal, un renforcement du Parlement, un État de droit et une "
           "stabilité institutionnelle — ce qui accompagne la montée de la part britannique "
           "dans la production industrielle mondiale, de 2 % en 1750 à 23 % en 1880.",
           "Les institutions concernées sont larges : lois, justice, droits de propriété, "
           "normes sociales, constitutions, organisations publiques — et aussi l’État "
           "providence, les prud’hommes, l’autorité de la concurrence et la régulation "
           "financière."],
     'lim': "Deux objections sont explicitement posées. Le cas chinois : centralisation "
            "politique, parti unique et absence de pluralisme n’ont pas empêché quarante ans "
            "de croissance rapide, d’industrialisation massive et de montée technologique. Et "
            "la double causalité : de bonnes institutions favorisent-elles la croissance, ou "
            "est-ce la richesse qui permet de bonnes institutions ?"},
   ],
   'v': "Ces modèles laissent de côté une contrainte qui s’impose désormais à tous : "
        "l’environnement."},

  # ----------------------------------------------------------------- IX
  {'t': "IX. Croissance et soutenabilité",
   'sp': [
    {'t': "A. Le capital élargi et les deux soutenabilités",
     'd': ["Le cours élargit la notion de capital à six formes : capital physique ou technique, "
           "capital humain, capital naturel, capital technologique, capital social et capital "
           "institutionnel. C’est le statut du capital naturel qui fait débat.",
           "La soutenabilité faible, d’inspiration néoclassique, suppose que le capital naturel "
           "peut être substitué par du capital physique ou humain : le progrès technique joue "
           "alors un rôle central, et la croissance reste possible indéfiniment par "
           "substitution. La soutenabilité forte, d’inspiration écologique, soutient au "
           "contraire que certains capitaux naturels — climat, biodiversité — sont "
           "irremplaçables : la croissance doit alors être découplée de l’usage des "
           "ressources.",
           "La courbe environnementale de Kuznets transpose à l’environnement la relation en "
           "cloche : la dégradation augmenterait d’abord avec le développement, puis "
           "diminuerait une fois un certain niveau de richesse atteint."],
     'lim': "Le cours est net sur ce point : cette conclusion est loin d’être universellement "
            "valable — elle peut traduire un simple déplacement de la pollution vers d’autres "
            "pays plutôt qu’une réduction réelle."},
    {'t': "B. Les leviers : efficacité, sobriété, économie circulaire, découplage",
     'd': ["L’efficacité énergétique relève du « faire mieux » : moteurs plus efficaces, "
           "bâtiments mieux isolés, appareils moins énergivores, procédés industriels plus "
           "performants. La sobriété relève du « faire moins ou autrement » : elle suppose une "
           "modification des comportements et des usages. L’économie circulaire vise le "
           "recyclage, le réemploi, la réparation et la réduction des déchets.",
           "La notion centrale et discutée est le découplage : la dissociation entre croissance "
           "économique et pression environnementale. Toute la question est de savoir s’il est "
           "relatif — la pression croît moins vite que le PIB — ou absolu — elle diminue en "
           "valeur."],
     'lim': "L’effet rebond limite l’efficacité énergétique : une technique plus performante "
            "abaisse le coût d’usage et peut faire augmenter la consommation, annulant tout ou "
            "partie du gain."},
    {'t': "C. Les politiques publiques de transition",
     'd': ["Les repères historiques encadrent le débat : le rapport du Club de Rome (1972) sur "
           "les limites physiques de la croissance, et le rapport Brundtland (1987) qui "
           "formule la définition du développement durable — répondre aux besoins présents "
           "sans compromettre ceux des générations futures — autour de trois piliers : "
           "économique, social, environnemental.",
           "Les politiques européennes actuelles s’empilent : le Green Deal vise la neutralité "
           "carbone dans une logique de croissance verte ; Next Generation EU mobilise "
           "750 milliards d’euros à partir de 2020 pour la transition écologique, la "
           "transformation numérique et la cohésion ; l’objectif climatique est une baisse des "
           "émissions de 55 % d’ici 2030 par rapport à 1990. La CSRD impose un reporting de "
           "durabilité — transparence, comparabilité, lutte contre le greenwashing — et le "
           "devoir de vigilance étend la responsabilité de l’entreprise à ses filiales, "
           "sous-traitants et fournisseurs, c’est-à-dire à toute sa chaîne de valeur.",
           "Le cours insiste sur un point : la transition devient conflictuelle dès qu’elle se "
           "traduit par de véritables contraintes juridiques, financières et concurrentielles "
           "pour les entreprises. D’où des reculs, notamment le relèvement du seuil "
           "d’application du reporting de 50 à 550 millions d’euros de chiffre d’affaires."],
     'lim': "L’externalisation des coûts sociaux et environnementaux reste le point aveugle : "
            "une entreprise peut transférer à d’autres acteurs ou territoires le coût "
            "écologique de sa production, notamment par la sous-traitance — ce que le devoir "
            "de vigilance cherche précisément à corriger."},
    {'t': "D. Croissance verte ou récit contesté : Aghion, Fressoz, Jarrige",
     'd': ["Aghion prolonge Schumpeter et défend la croissance verte : la concurrence stimule "
           "l’invention, et la destruction créatrice peut être orientée vers la transition. On "
           "ne renonce pas à la croissance, on en change le contenu, une politique industrielle "
           "publique pouvant diriger l’innovation vers des technologies bas carbone.",
           "Jean-Baptiste Fressoz conteste le récit même de la transition : l’histoire de "
           "l’énergie est un empilement des sources, non une suite de substitutions — le "
           "charbon n’a pas disparu avec le pétrole, et les nouvelles chaînes énergétiques "
           "s’installent sur des bases matérielles héritées. La sortie des fossiles est donc "
           "plus lente et plus complexe qu’on ne le dit.",
           "François Jarrige applique la critique à la voiture électrique : elle déplace la "
           "pollution plus qu’elle ne la supprime — batteries nécessitant lithium et cobalt, "
           "bornes de recharge, réseaux électriques, recyclage incomplet. On passe d’une "
           "dépendance aux hydrocarbures à une dépendance aux métaux critiques, rares et "
           "géographiquement concentrés, ce qui fait de la transition une question "
           "géopolitique."],
     'lim': "Le cours referme le chapitre sur une tension non résolue : la croissance est à la "
            "fois le problème — par la pression qu’elle exerce — et le moyen revendiqué de la "
            "transition, puisque l’innovation et l’investissement qu’elle finance en sont les "
            "conditions."},
   ],
   'v': "Le chapitre se termine donc sur la question qui ouvre le chapitre suivant : la "
        "croissance suffit-elle à produire du développement, et à quelles conditions ?"},
 ],

 'ae': [
  {'n': "François Perroux et Jean Arrous", 'k': 'a',
   'i': "Deux définitions complémentaires : augmentation soutenue d’un indicateur de dimension "
        "en termes réels, et processus cumulatif d’interactions élevant la productivité."},
  {'n': "Nicholas Kaldor", 'k': 'a',
   'i': "Les faits stylisés : décrire des régularités de longue période avant de prétendre les "
        "expliquer."},
  {'n': "Walt Rostow", 'k': 'a',
   'i': "Cinq étapes et un décollage à environ 10 % d’investissement — modèle linéaire, "
        "optimiste et ethnocentrique, marqué par les années 1950-1960."},
  {'n': "Alexander Gerschenkron", 'k': 'a',
   'i': "L’avantage du retard : les late comers rattrapent en mobilisant l’État, les banques "
        "et les grandes entreprises comme institutions de substitution."},
  {'n': "Alvin Hansen (1938) et Larry Summers (2013)", 'k': 'a',
   'i': "La stagnation séculaire : un excès durable d’épargne sur l’investissement que la "
        "politique monétaire ne peut corriger."},
  {'n': "Carré, Dubois et Malinvaud", 'k': 'a',
   'i': "La décomposition des Trente Glorieuses par une fonction de Cobb-Douglas : 0,5 point "
        "de travail, 1,5 de capital, 3,1 de PGF."},
  {'n': "Robert Solow", 'k': 'a',
   'i': "Rendements décroissants, amortissement, état stationnaire et convergence "
        "conditionnelle — et un progrès technique exogène, « manne tombée du ciel »."},
  {'n': "Roy Harrod et Evsey Domar (1947)", 'k': 'a',
   'i': "Le fil du rasoir : la croissance équilibrée est un cas exceptionnel, sans mécanisme "
        "automatique d’ajustement."},
  {'n': "Robert Lucas, Robert Barro, Paul Romer", 'k': 'a',
   'i': "Croissance endogène : capital humain, capital public productif, connaissance comme "
        "bien non rival engendrant des spillovers."},
  {'n': "Philippe Aghion et Peter Howitt", 'k': 'a',
   'i': "Destruction créatrice formalisée et distance à la frontière technologique : ciblage "
        "loin de la frontière, concurrence à proximité."},
  {'n': "Abhijit Banerjee et Esther Duflo", 'k': 'a',
   'i': "La mauvaise allocation du capital matériel et humain explique qu’une économie "
        "stagne alors que capital, talents et entrepreneurs existent."},
  {'n': "Douglass North, Daron Acemoglu et James Robinson", 'k': 'a',
   'i': "Institutions inclusives contre extractives : droits de propriété fragiles → personne "
        "n’investit → le capital fuit."},
  {'n': "Simon Kuznets (1955)", 'k': 'a',
   'i': "La courbe en cloche des inégalités, et sa transposition environnementale — deux "
        "hypothèses que le cours juge non universellement vérifiées."},
  {'n': "Branko Milanovic (2016, actualisé en 2022)", 'k': 'a',
   'i': "La courbe de l’éléphant et la rente de citoyenneté : convergence entre pays, "
        "divergence au sein des pays."},
  {'n': "Thomas Piketty", 'k': 'a',
   'i': "r > g et la logique cumulative des patrimoines ; et l’exemple de la bicyclette pour "
        "distinguer prix nominal et prix réel relatif."},
  {'n': "Robert Gordon", 'k': 'a',
   'i': "Les innovations numériques seraient moins transformatrices que l’électricité ou le "
        "moteur thermique : d’où une croissance durablement faible."},
  {'n': "Alfred Sauvy, La machine et le chômage (1980)", 'k': 'a',
   'i': "Le déversement : les gains de productivité libèrent main-d’œuvre et revenu, qui se "
        "redéploient vers d’autres secteurs."},
  {'n': "Pierre Veltz", 'k': 'a',
   'i': "Nous ne sommes pas post-industriels mais hyper-industriels : l’industrie devient "
        "servicielle et les services industriels."},
  {'n': "Jean-Baptiste Fressoz et François Jarrige", 'k': 'a',
   'i': "L’histoire de l’énergie est un empilement, non une substitution ; et la voiture "
        "électrique déplace la pollution vers les métaux critiques."},
  {'n': "Les Trente Glorieuses françaises (1951-1973)", 'k': 'e',
   'i': "5,2 % de croissance annuelle, dont 3,1 points de PGF : la démonstration empirique que "
        "la productivité, et non l’accumulation, porte la croissance."},
  {'n': "L’apprentissage en France (400 000 → plus d’un million en 2024)", 'k': 'e',
   'i': "Investissement en capital humain ou effet d’aubaine ? Le cas d’école du ciblage d’une "
        "politique de l’emploi."},
  {'n': "Le rapport Draghi", 'k': 'e',
   'i': "Retard de productivité européen, besoin d’environ 800 milliards d’euros par an : un "
        "diagnostic keynésien assorti de remèdes en partie libéraux."},
  {'n': "Les câbles sous-marins (≈ 98 % des flux de données)", 'k': 'e',
   'i': "La preuve matérielle de la thèse hyper-industrielle : plus l’économie semble "
        "immatérielle, plus elle dépend d’infrastructures lourdes."},
  {'n': "Next Generation EU (750 Md€) et l’objectif −55 % en 2030", 'k': 'e',
   'i': "L’échelle des moyens européens — et, face à eux, le relèvement du seuil de reporting "
        "de 50 à 550 millions d’euros, qui mesure la résistance à la contrainte."},
  {'n': "La part britannique dans la production industrielle mondiale (2 % en 1750, 23 % en "
        "1880)", 'k': 'e',
   'i': "Le basculement institutionnel anglais — limitation du pouvoir royal, Parlement, État "
        "de droit — accompagne la montée industrielle."},
 ],

 'arg': [
  "Croissance extensive et croissance intensive n’ont pas les mêmes conséquences : seule la "
  "seconde élève durablement le PIB par habitant, puisque l’accumulation de facteurs se heurte "
  "aux rendements décroissants.",
  "La décomposition de Carré, Dubois et Malinvaud est l’argument chiffré le plus solide du "
  "chapitre : 5,2 % = 0,5 + 1,5 + 3,1, soit 60 % de résidu — ce qui déplace toute la question "
  "vers les déterminants de la productivité.",
  "Le résidu de Solow n’est pas une explication mais un aveu : c’est précisément ce que les "
  "théories de la croissance endogène internalisent, chacune par un canal différent.",
  "La convergence prévue par Solow n’est que conditionnelle : elle suppose des paramètres "
  "structurels comparables, ce qui renvoie aux institutions et au capital humain.",
  "La désindustrialisation n’a pas une cause unique : gains de productivité, externalisation "
  "statistique et concurrence internationale se combinent, et la thèse de Veltz interdit de "
  "parler de société post-industrielle.",
  "Les inégalités ne se mesurent pas d’une seule façon : D9/D1 ignore les extrêmes, le Gini "
  "résume mal, le Palma capte mieux le sommet — justifier son indicateur fait partie de "
  "l’argument.",
  "La croissance verte n’est ni évidente ni impossible : elle suppose un découplage absolu que "
  "les données ne montrent pas encore à l’échelle mondiale, et que Fressoz conteste sur le "
  "plan historique.",
 ],

 'deb': [
  "La croissance a-t-elle une limite ? État stationnaire de Ricardo, Club de Rome, stagnation "
  "séculaire de Hansen et Summers contre croissance endogène.",
  "Le progrès technique actuel est-il comparable à celui du passé ? Gordon pessimiste contre "
  "l’hypothèse du décalage temporel et l’optimisme d’Aghion.",
  "Les inégalités sont-elles un moteur ou un frein de la croissance ? Incitation à innover "
  "contre mauvaise allocation du capital humain et croissance inclusive.",
  "Croissance verte ou décroissance ? Soutenabilité faible contre soutenabilité forte, et la "
  "question du découplage absolu.",
  "Les institutions expliquent-elles la croissance, ou la croissance permet-elle de bonnes "
  "institutions ? Le cas chinois et le problème de la double causalité.",
  "Faut-il subventionner l’apprentissage ? Investissement en capital humain contre effet "
  "d’aubaine et coût budgétaire.",
 ],

 'lien': [
  {'c': 8, 'p': "Schumpeter, les révolutions industrielles, le taylorisme et l’IA donnent le "
                "contenu historique et concret du progrès technique ici modélisé."},
  {'c': 7, 'p': "Rostow, Gerschenkron, les institutions et la soutenabilité y sont repris sous "
                "l’angle du développement et du rattrapage des pays pauvres."},
  {'c': 1, 'p': "Le PIB, ses limites, l’output gap, le partage de la valeur ajoutée et les "
                "outils de mesure des inégalités viennent du premier chapitre."},
  {'c': 22, 'p': "Désindustrialisation, réindustrialisation et politique industrielle "
                 "européenne prolongent directement la partie sur les transformations "
                 "structurelles."},
  {'c': 5, 'p': "La connaissance comme bien non rival, les externalités positives et les "
                "brevets relient croissance endogène et défaillances de marché."},
  {'c': 9, 'p': "Concurrence, brevets défensifs et rentes de position relient les déterminants "
                "de la productivité à l’économie industrielle."},
 ],

 'min': [
  "Croissance = ↑ soutenue du PIB en volume (Perroux) et processus cumulatif élevant la "
  "productivité (Arrous) ; croissance ≠ développement.",
  "Loi de la croissance cumulée : 2 % par an pendant 35 ans → doublement. PIB total ≠ PIB par "
  "habitant.",
  "Rostow : cinq étapes, décollage à ≈ 10 % du PIB investi — linéaire et ethnocentrique. "
  "Gerschenkron : avantage du retard.",
  "Trente Glorieuses : 5,2 % = 0,5 (travail) + 1,5 (capital) + 3,1 (PGF), soit ≈ 60 % de "
  "résidu.",
  "Croissance potentielle française ≈ 0,8 % (2009-2018) ; stagnation séculaire (Hansen 1938, "
  "Summers 2013).",
  "Loi des trois secteurs et déversement (Sauvy) ; désindustrialisation : productivité, "
  "externalisation, mondialisation ; Veltz : société hyper-industrielle.",
  "Inégalités : D9/D1, Lorenz et Gini, Palma ; Kuznets en cloche ; éléphant de Milanovic "
  "(1988-2008) et rente de citoyenneté ; r > g chez Piketty.",
  "Harrod-Domar : fil du rasoir. Solow : amortissement, état stationnaire, convergence "
  "conditionnelle, progrès technique exogène.",
  "Croissance endogène : Lucas (capital humain), Barro (capital public), Romer (bien non "
  "rival, spillovers), Aghion-Howitt (destruction créatrice, frontière technologique).",
  "Institutions inclusives / extractives (Acemoglu et Robinson) ; mauvaise allocation "
  "(Banerjee et Duflo) ; croissance inclusive.",
  "Soutenabilité faible contre forte ; découplage ; Club de Rome (1972), Brundtland (1987), "
  "Next Generation EU (750 Md€, −55 % en 2030), CSRD ; critiques de Fressoz et Jarrige.",
 ],
}}
