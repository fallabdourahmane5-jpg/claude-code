# -*- coding: utf-8 -*-
"""Ensemble 11 — La monnaie, les banques et le crédit (3/4)."""

from doss_base import d

d('n11-preference-liquidite', 11, "Préférence pour la liquidité",
  "Le taux d’intérêt comme prix du renoncement à la liquidité",
  "Chez Keynes, les agents peuvent préférer thésauriser, c’est-à-dire garder "
  "la monnaie, plutôt qu’investir. Le cours en tire une redéfinition du taux "
  "d’intérêt : il est le prix du renoncement à la liquidité, et non simplement "
  "le prix de l’épargne. La monnaie n’est donc pas neutre : elle influence la "
  "production et l’emploi, donc la sphère réelle.",
  "Le cours introduit la préférence pour la liquidité à l’intérieur de "
  "l’analyse monétaire de Keynes, et c’est cette position qui en commande la "
  "portée. Le point de départ est une rupture : pour Keynes, la monnaie n’est "
  "pas neutre, elle influence la production et l’emploi, donc la sphère "
  "réelle, ce qui contredit directement la tradition classique pour laquelle "
  "la monnaie n’est qu’un voile. Le mécanisme est le suivant : les agents "
  "peuvent préférer thésauriser, c’est-à-dire garder la monnaie, plutôt "
  "qu’investir. Détenir de la monnaie n’est donc pas un comportement résiduel "
  "mais un choix, et ce choix a un prix. D’où la conséquence théorique "
  "décisive : le taux d’intérêt est le prix du renoncement à la liquidité, "
  "pas simplement le prix de l’épargne. Le taux d’intérêt cesse d’être la "
  "rémunération d’un sacrifice de consommation pour devenir la compensation "
  "exigée en échange de l’abandon de la disponibilité immédiate. Le cours "
  "prolonge cette analyse jusqu’à une situation limite, la trappe à "
  "liquidité : lorsque les taux sont déjà très bas, les agents préfèrent "
  "conserver des liquidités, les banques restent prudentes et "
  "l’investissement ne repart pas suffisamment ; baisser encore les taux ne "
  "suffit plus et la politique monétaire conventionnelle devient moins "
  "efficace. Le cours relie cette impasse à la crise de 2008, après laquelle "
  "les banques centrales doivent se tourner vers des instruments non "
  "conventionnels, et au débat sur l’hélicoptère monétaire, qui cherche "
  "précisément à contourner le problème central mis en évidence par Friedman "
  "et Keynes en situation de trappe à liquidité : même avec des taux très bas, "
  "les banques n’accordent pas de crédits et les ménages n’investissent pas.",
  [("Le choix de détenir de la monnaie",
    "Garder la monnaie est une décision et non un résidu : l’agent compare "
    "l’avantage de la disponibilité immédiate au rendement qu’il abandonne en "
    "ne plaçant pas ses fonds."),
   ("La redéfinition du taux d’intérêt",
    "Si détenir de la monnaie procure un avantage, il faut une compensation "
    "pour y renoncer : le taux d’intérêt devient le prix du renoncement à la "
    "liquidité et non le prix de l’épargne."),
   ("Le rôle de l’incertitude",
    "Plus l’avenir est incertain, plus la disponibilité immédiate a de la "
    "valeur : la préférence pour la liquidité s’accroît en période de crise, "
    "au moment précis où l’économie aurait besoin de dépense."),
   ("La non-neutralité de la monnaie",
    "Si la monnaie peut être désirée pour elle-même, elle n’est plus un "
    "simple voile : sa détention retire de la demande à l’économie réelle et "
    "influence donc la production et l’emploi."),
   ("La trappe à liquidité",
    "Lorsque les taux sont déjà très bas, la compensation offerte pour "
    "renoncer à la liquidité devient négligeable : les agents conservent leurs "
    "liquidités et la baisse des taux cesse d’avoir prise sur la dépense.")],
  [{'a': "Faire du taux d’intérêt le prix du renoncement à la liquidité "
         "explique pourquoi l’épargne ne se transforme pas automatiquement en "
         "investissement.",
    'cond': "L’argument suppose que la monnaie puisse être détenue pour "
            "elle-même, donc qu’elle procure un avantage propre, la "
            "disponibilité.",
    'lim': "La tradition classique objecte que la monnaie n’est qu’un voile "
           "et que sa détention est sans effet durable sur les grandeurs "
           "réelles."},
   {'a': "La préférence pour la liquidité rend compte d’un fait observé : la "
         "baisse des taux peut rester sans effet sur l’investissement.",
    'cond': "Elle exige que les agents arbitrent effectivement entre détenir "
            "de la monnaie et placer leurs fonds.",
    'lim': "Elle n’explique pas à elle seule la prudence des banques, que le "
           "cours ajoute comme second blocage de la trappe à liquidité."},
   {'a': "L’analyse justifie l’intervention budgétaire lorsque la politique "
         "monétaire se trouve désarmée par le plancher des taux.",
    'cond': "Le raisonnement suppose que la dépense publique ne soit pas "
            "elle-même absorbée par un surcroît d’épargne de précaution.",
    'lim': "Le cours relève que l’hélicoptère monétaire, qui pousse cette "
           "logique à son terme, brouille la frontière entre politique "
           "monétaire et politique budgétaire et menace l’indépendance de la "
           "banque centrale."},
   {'a': "La notion éclaire la gradation des agrégats monétaires, qui classe "
         "les actifs selon leur disponibilité.",
    'cond': "Elle suppose que les agents acceptent une rémunération "
            "croissante à mesure qu’ils renoncent à la liquidité.",
    'lim': "Cette hiérarchie suppose des marchés stables : en crise, un actif "
           "réputé liquide peut cesser de l’être, ce que le cours observe "
           "avec l’effondrement de certains actifs en 2008."}],
  [{'t': "Le taux d’intérêt est le prix du renoncement à la liquidité et non "
         "simplement le prix de l’épargne.",
    'qui': "John Maynard Keynes, dans l’analyse monétaire que le cours "
           "résume.",
    'rep': "Les classiques et les monétaristes objectent que la monnaie n’est "
           "qu’un voile : pour eux, plus de monnaie n’entraîne qu’une hausse "
           "des prix, la production et l’emploi restant inchangés."},
   {'t': "Les agents peuvent préférer thésauriser plutôt qu’investir, ce qui "
         "rend la monnaie non neutre.",
    'qui': "L’analyse keynésienne de la monnaie, telle que le cours la "
           "présente.",
    'rep': "Friedman concède une influence de la monnaie sur les variables "
           "réelles à court terme, mais soutient que cette relation est "
           "instable, alors que le lien entre quantité de monnaie et niveau "
           "général des prix reste stable."},
   {'t': "En trappe à liquidité, il faut distribuer directement la monnaie "
         "aux agents pour rétablir un effet réel de la création monétaire.",
    'qui': "L’hélicoptère monétaire, solution que le cours rattache à "
           "Friedman.",
    'rep': "Le cours en relève les limites : risque élevé d’inflation, remise "
           "en cause de l’indépendance de la banque centrale, confusion entre "
           "politique monétaire et budgétaire, et problème de crédibilité à "
           "long terme de la monnaie."}],
  [{'n': "John Maynard Keynes",
    'i': "Les agents peuvent préférer garder la monnaie plutôt que de "
         "l’investir, ce qui fait du taux d’intérêt le prix du renoncement à "
         "la liquidité.",
    'p': "Le cours en tire la non-neutralité de la monnaie : elle influence "
         "la production et l’emploi, donc la sphère réelle, ce qui rompt avec "
         "la tradition classique pour laquelle la monnaie ne modifie que le "
         "niveau général des prix."},
   {'n': "Milton Friedman",
    'i': "La monnaie peut influencer les variables réelles à court terme, "
         "mais cette relation est instable.",
    'p': "Le cours précise sa formule : il existe une influence de la monnaie "
         "sur la production, le chômage et l’investissement à court terme, "
         "mais seul le lien entre l’évolution de la quantité de monnaie et "
         "l’indice général des prix est stable."},
   {'n': "Irving Fisher",
    'i': "Sa théorie quantitative suppose la vitesse de circulation de la "
         "monnaie stable.",
    'p': "Le cours rappelle son équation reliant masse monétaire, vitesse de "
         "circulation, niveau des prix et volume des transactions : or la "
         "préférence pour la liquidité est précisément le comportement qui "
         "fait varier cette vitesse."}],
  [{'f': "Le cours énonce que pour Keynes la monnaie n’est pas neutre, "
         "qu’elle influence la production et l’emploi, et que les agents "
         "peuvent préférer thésauriser plutôt qu’investir.",
    'p': "L’énoncé montre que la préférence pour la liquidité est le "
         "mécanisme par lequel la sphère monétaire agit sur la sphère réelle, "
         "ce qui est le point de rupture avec les classiques."},
   {'f': "En trappe à liquidité, les taux sont déjà très bas, les agents "
         "préfèrent conserver des liquidités, les banques restent prudentes "
         "et l’investissement ne repart pas suffisamment.",
    'p': "La description établit que la préférence pour la liquidité n’est "
         "pas une hypothèse théorique mais une situation observée, qui a "
         "désarmé la politique monétaire après 2008."},
   {'f': "Le cours présente l’hélicoptère monétaire comme une tentative de "
         "contourner le problème central mis en évidence par Friedman et "
         "Keynes en situation de trappe à liquidité.",
    'p': "Le fait que deux courants opposés convergent sur ce diagnostic "
         "montre que la préférence pour la liquidité est reconnue au-delà du "
         "seul cadre keynésien."}],
  [{'q': "Pourquoi détient-on de la monnaie plutôt que de la placer ?",
    'f': "Parce que la disponibilité immédiate a une valeur propre. Le cours "
         "l’énonce clairement : les agents peuvent préférer thésauriser, "
         "c’est-à-dire garder la monnaie, plutôt qu’investir. Le taux "
         "d’intérêt est alors la compensation exigée pour y renoncer, ce qui "
         "en fait le prix du renoncement à la liquidité et non simplement le "
         "prix de l’épargne.",
    'r': "Le raisonnement fait de la détention de monnaie un arbitrage, ce "
         "qui transforme le taux d’intérêt en prix d’un service et non en "
         "récompense d’une abstinence.",
    'ex': "Keynes rejette explicitement l’idée que le taux d’intérêt soit le "
          "simple prix de l’épargne."},
   {'q': "La monnaie influence-t-elle durablement la production ?",
    'f': "Pour Keynes, oui, et la préférence pour la liquidité en est le "
         "mécanisme : si les agents conservent la monnaie au lieu de "
         "l’investir, la demande adressée à l’économie diminue et la "
         "production avec elle. Pour les classiques et les monétaristes, non : "
         "la monnaie n’est qu’un voile, et un excès de monnaie ne produit que "
         "de l’inflation.",
    'r': "On rapporte le désaccord à une seule question, la monnaie peut-elle "
         "être désirée pour elle-même, et l’on montre que toute la divergence "
         "en découle.",
    'ex': "Friedman concède un effet réel à court terme mais le juge "
          "instable et donc non exploitable."},
   {'q': "Pourquoi la baisse des taux peut-elle rester sans effet ?",
    'f': "Parce qu’en dessous d’un certain niveau la compensation offerte "
         "pour renoncer à la liquidité devient négligeable. Le cours décrit "
         "cette trappe à liquidité : les taux sont déjà très bas, les agents "
         "préfèrent conserver des liquidités, les banques restent prudentes et "
         "l’investissement ne repart pas, de sorte que baisser encore les taux "
         "ne suffit plus.",
    'r': "Le raisonnement identifie le plancher au-delà duquel l’instrument "
         "perd prise, ce qui explique le recours aux politiques non "
         "conventionnelles après 2008.",
    'ex': "Certaines banques centrales ont même recouru à des taux négatifs "
          "sur la facilité de dépôt."}],
  voisins=['n11-liquidite', 'n11-neutralite-monnaie',
           'n11-monnaie-activite', 'n11-banque-centrale'])


d('n11-multiplicateur-diviseur', 11, "Multiplicateur et diviseur de crédit",
  "Qui commande : la banque centrale ou la demande de crédit ?",
  "Le multiplicateur de crédit est un modèle expliquant comment une base "
  "monétaire limitée peut produire beaucoup plus de monnaie scripturale grâce "
  "aux banques commerciales : la monnaie y est exogène. Le diviseur de crédit "
  "inverse la causalité : les banques prêtent d’abord et se refinancent "
  "ensuite, de sorte que la monnaie est endogène et que l’offre de monnaie "
  "s’adapte à la demande de crédit.",
  "Le cours construit cette opposition comme une question de causalité, et "
  "c’est le meilleur moyen de la retenir : multiplicateur signifie monnaie "
  "centrale vers masse monétaire, diviseur signifie masse monétaire vers "
  "monnaie centrale. Le multiplicateur d’abord, rattaché au courant "
  "monétaire. Il repose sur une idée simple : les banques prêtent l’argent qui "
  "leur reste après les retraits en billets, de sorte que si les clients ne "
  "retirent qu’une petite partie, la banque peut reprêter le reste, ce qui "
  "crée une nouvelle vague de monnaie. Le cours chiffre l’exemple avec un taux "
  "de retrait de vingt pour cent : un crédit initial de cent laisse "
  "quatre-vingts en dépôts reprêtables, puis soixante-quatre, puis cinquante "
  "et un virgule deux, la suite géométrique convergeant vers cinq cents, "
  "c’est-à-dire cent de base monétaire devenant cinq cents de monnaie créée. "
  "Dans cette optique, la banque centrale contrôle la base monétaire, billets "
  "et réserves, et contrôle donc la masse monétaire en fixant les réserves "
  "obligatoires : la monnaie est exogène, sa quantité étant décidée de "
  "l’extérieur de l’économie. Le diviseur ensuite, rattaché au courant "
  "keynésien, qui renverse l’ordre des opérations en quatre étapes : un agent "
  "demande un crédit ; la banque crée immédiatement la somme et crédite le "
  "compte sans regarder si elle a les réserves suffisantes ; elle vérifie "
  "ensuite combien les clients retireront en billets et combien elle doit "
  "mettre en réserves obligatoires ; si elle manque de monnaie centrale, elle "
  "emprunte à la banque centrale, qui lui fournit presque toujours la monnaie "
  "nécessaire car elle doit garantir la stabilité du système et le financement "
  "de l’économie. L’idée clé est que l’offre de monnaie s’adapte à la demande "
  "de crédit. Le cours ajoute une profondeur historique : dès le dix-neuvième "
  "siècle, la Currency School et la Banking School s’opposaient déjà sur la "
  "couverture des billets par l’or.",
  [("La fuite en billets comme limite",
    "Si les clients retirent une fraction de chaque crédit en billets, la "
    "banque ne peut reprêter que le reste : c’est cette fuite qui borne la "
    "série des crédits successifs et détermine la valeur du multiplicateur."),
   ("La convergence de la série",
    "Chaque vague de crédit est plus faible que la précédente, dans la "
    "proportion de ce qui reste après retrait : la somme des vagues converge "
    "vers un multiple fini de la base monétaire initiale."),
   ("Le contrôle par les réserves obligatoires",
    "En fixant la fraction des dépôts que les banques doivent conserver à la "
    "banque centrale, celle-ci modifie le multiplicateur : elle contrôle donc "
    "indirectement la masse monétaire que la base monétaire peut engendrer."),
   ("Le renversement par la demande de crédit",
    "Dans le diviseur, la banque crée la monnaie avant de disposer des "
    "réserves : la création répond à la demande de financement des agents, "
    "et la banque centrale ne fait que suivre en fournissant la monnaie "
    "centrale."),
   ("L’obligation de refinancer",
    "La banque centrale fournit presque toujours la monnaie centrale demandée, "
    "parce qu’elle doit garantir la stabilité du système et le financement de "
    "l’économie : c’est cette contrainte qui rend la monnaie endogène.")],
  [{'a': "Le multiplicateur fournit un modèle simple et quantifiable du lien "
         "entre base monétaire et masse monétaire.",
    'cond': "Il suppose que les banques soient effectivement contraintes par "
            "leurs réserves, donc qu’elles ne puissent pas se refinancer "
            "librement.",
    'lim': "Le courant keynésien objecte que la banque centrale fournit "
           "presque toujours la monnaie centrale nécessaire, ce qui annule la "
           "contrainte supposée."},
   {'a': "Le diviseur décrit mieux le comportement bancaire observé, puisque "
         "la banque crédite le compte sans vérifier préalablement ses "
         "réserves.",
    'cond': "L’analyse exige que le refinancement soit accessible, sur le "
            "marché interbancaire ou auprès de la banque centrale.",
    'lim': "Elle réduit la banque centrale à un rôle d’accompagnement, alors "
           "que le coût du refinancement qu’elle fixe influence bien le "
           "volume du crédit."},
   {'a': "L’opposition des deux modèles clarifie un enjeu politique : qui "
         "détient le pouvoir sur la monnaie.",
    'cond': "La question suppose que l’on admette que la monnaie est créée "
            "par le crédit et non par une simple émission de billets.",
    'lim': "Le cours montre que la réponse est hybride : la banque centrale "
           "contrôle la monnaie centrale, les banques commerciales créent la "
           "monnaie scripturale, et la masse monétaire dépend de la demande "
           "de crédit."},
   {'a': "La profondeur historique du débat montre qu’il ne s’agit pas d’une "
         "querelle récente mais d’une question structurelle.",
    'cond': "La comparaison suppose que l’on reconnaisse la continuité entre "
            "la question de la couverture des billets par l’or et celle de la "
            "base monétaire.",
    'lim': "Les termes ont changé : les billets ne sont plus la contrepartie "
           "de l’or, de sorte que la Currency School du dix-neuvième siècle "
           "et le monétarisme ne défendent pas exactement la même thèse."}],
  [{'t': "La banque centrale contrôle la masse monétaire en fixant la base "
         "monétaire et les réserves obligatoires : la monnaie est exogène.",
    'qui': "Le courant monétaire, que le cours rattache à la Currency School "
           "et aux monétaristes.",
    'rep': "Le courant keynésien répond que les banques prêtent d’abord et se "
           "refinancent ensuite, et que la banque centrale leur fournit "
           "presque toujours la monnaie centrale nécessaire, de sorte que la "
           "monnaie est endogène."},
   {'t': "L’offre de monnaie s’adapte à la demande de crédit : la banque ne "
         "prête pas ce qu’elle a en réserve mais ce que les agents veulent "
         "emprunter.",
    'qui': "Le courant keynésien, que le cours rattache à la Banking School.",
    'rep': "Les monétaristes objectent qu’une telle élasticité conduit à une "
           "création monétaire excessive et donc à l’inflation, puisque "
           "l’inflation est toujours et partout un phénomène monétaire."},
   {'t': "Les billets émis par les banques doivent être strictement couverts "
         "par les stocks d’or détenus.",
    'qui': "La Currency School, dans le débat du dix-neuvième siècle que le "
           "cours rappelle.",
    'rep': "La Banking School répond que la monnaie doit s’adapter aux "
           "besoins de l’économie et naît de la demande de crédit, position "
           "que le cours rapproche de celle de Keynes."}],
  [{'n': "Milton Friedman",
    'i': "L’offre de monnaie dépend des autorités monétaires, donc la monnaie "
         "est exogène.",
    'p': "Le cours rattache à cette position le mécanisme du multiplicateur : "
         "la banque centrale crée la monnaie centrale, les banques "
         "commerciales la transforment en masse monétaire, et cent de monnaie "
         "centrale peuvent devenir cinq cents de monnaie scripturale."},
   {'n': "John Maynard Keynes",
    'i': "Ce n’est pas la banque centrale qui décide de la quantité de monnaie "
         "créée, mais la demande de crédit dans l’économie.",
    'p': "Le cours détaille les quatre étapes du diviseur : demande de "
         "crédit, création immédiate de la somme sans vérification des "
         "réserves, évaluation ensuite des besoins en billets et en réserves "
         "obligatoires, puis emprunt auprès de la banque centrale si "
         "nécessaire."},
   {'n': "Irving Fisher",
    'i': "La relation entre quantité de monnaie et niveau des prix suppose la "
         "vitesse de circulation stable.",
    'p': "Le cours rappelle son équation pour montrer le fondement de la "
         "position exogène : si la vitesse et le volume des transactions sont "
         "stables, toute hausse de la masse monétaire se traduit "
         "proportionnellement dans les prix."}],
  [{'f': "Avec un taux de retrait de vingt pour cent, un crédit initial de "
         "cent engendre des vagues successives de quatre-vingts, "
         "soixante-quatre puis cinquante et un virgule deux, la série "
         "convergeant vers cinq cents.",
    'p': "Le calcul montre que le multiplicateur est fini et dépend "
         "entièrement du taux de fuite en billets, donc du comportement des "
         "déposants."},
   {'f': "Dans le diviseur, la banque crédite immédiatement les cent mille "
         "euros demandés sans regarder si elle a les réserves suffisantes, et "
         "ne vérifie qu’ensuite ses besoins en monnaie centrale.",
    'p': "La chronologie inversée démontre que la contrainte de réserves "
         "n’est pas préalable au crédit mais consécutive, ce qui est le cœur "
         "de la thèse endogène."},
   {'f': "Dès le dix-neuvième siècle, la question était de savoir dans quelle "
         "mesure les billets émis par les banques devaient être couverts par "
         "les stocks d’or détenus par les banques centrales.",
    'p': "L’antériorité du débat montre que l’opposition entre monnaie "
         "exogène et monnaie endogène porte sur une question structurelle du "
         "système bancaire et non sur un détail technique."}],
  [{'q': "Qui crée la monnaie ?",
    'f': "La réponse dépend du modèle retenu. Avec le multiplicateur, la "
         "banque centrale crée la monnaie centrale et les banques "
         "commerciales ne font que la démultiplier dans la limite des "
         "réserves : la monnaie est exogène. Avec le diviseur, les banques "
         "créent la monnaie en répondant à la demande de crédit et la banque "
         "centrale suit : la monnaie est endogène.",
    'r': "Le raisonnement rapporte le désaccord à un sens de causalité, "
         "monnaie centrale vers masse monétaire ou inverse, ce qui permet de "
         "trancher par l’observation du comportement bancaire.",
    'ex': "Le cours formule la question ainsi : dans ce schéma, qui a le "
          "pouvoir ?"},
   {'q': "La banque centrale contrôle-t-elle la masse monétaire ?",
    'f': "Elle contrôle la monnaie centrale, non la masse monétaire. Le cours "
         "conclut en trois propositions : la banque centrale contrôle la "
         "monnaie centrale, les banques commerciales créent la monnaie "
         "scripturale, et la masse monétaire dépend de la demande de crédit. "
         "Son influence est donc indirecte, par le coût et les conditions du "
         "refinancement.",
    'r': "On distingue les deux étages du système monétaire pour montrer que "
         "le contrôle porte sur l’un et l’influence sur l’autre.",
    'ex': "La banque centrale fournit presque toujours la monnaie centrale "
          "demandée, car elle doit garantir la stabilité du système."},
   {'q': "Ce débat est-il nouveau ?",
    'f': "Non : le cours rappelle que dès le dix-neuvième siècle des courants "
         "s’opposaient sur la dynamique de la création monétaire, la question "
         "étant alors de savoir dans quelle mesure les billets devaient être "
         "couverts par les stocks d’or. La Banking School, que l’on peut "
         "rapprocher de Keynes, défendait une monnaie endogène ; la Currency "
         "School, que l’on rapproche des monétaristes, une monnaie exogène.",
    'r': "Le raisonnement établit une continuité entre deux formulations "
         "historiques d’un même problème, ce qui montre qu’il est structurel "
         "et non conjoncturel.",
    'ex': "La Banking School soutenait que la monnaie doit s’adapter aux "
          "besoins de l’économie."}],
  voisins=['n11-creation-monetaire', 'n11-refinancement',
           'n11-monnaie-activite', 'n11-banque-centrale'],
  comp={'titre': "Multiplicateur de crédit et diviseur de crédit",
        'a': "Multiplicateur de crédit",
        'b': "Diviseur de crédit",
        'lignes': [
          ("Courant de rattachement", "Le courant monétaire, prolongeant la "
           "Currency School du dix-neuvième siècle", "Le courant keynésien, "
           "prolongeant la Banking School"),
          ("Sens de la causalité", "De la monnaie centrale vers la masse "
           "monétaire", "De la masse monétaire vers la monnaie centrale"),
          ("Nature de la monnaie", "Exogène : la quantité est décidée de "
           "l’extérieur de l’économie", "Endogène : la quantité naît de la "
           "demande de crédit des agents"),
          ("Chronologie des opérations", "La banque prête ce qui lui reste "
           "après retraits et réserves", "La banque prête d’abord, puis se "
           "procure la monnaie centrale"),
          ("Rôle de la banque centrale", "Elle contrôle la base monétaire et "
           "fixe les réserves obligatoires", "Elle accompagne en fournissant "
           "presque toujours le refinancement"),
          ("Variable déterminante", "Le taux de fuite en billets et le taux "
           "de réserves obligatoires", "La demande de financement émanant des "
           "ménages et des entreprises"),
          ("Illustration chiffrée du cours", "Cent de base monétaire "
           "deviennent cinq cents de monnaie créée", "Cent mille euros "
           "demandés sont créés immédiatement, puis refinancés"),
          ("Conséquence pour la politique monétaire", "Contrôler la quantité "
           "de monnaie, d’où la règle d’une progression constante",
           "Agir sur les conditions du crédit, le volume suivant la demande"),
          ("Risque mis en avant", "Une création monétaire excessive, donc "
           "l’inflation", "Un rationnement du crédit qui bloquerait le "
           "financement de l’économie")]})


d('n11-refinancement', 11, "Refinancement bancaire",
  "Se procurer la monnaie centrale après avoir créé la monnaie scripturale",
  "Le refinancement est l’opération par laquelle une banque commerciale se "
  "procure la monnaie centrale dont elle a besoin, auprès des autres banques "
  "sur le marché interbancaire ou auprès de la banque centrale. Le cours en "
  "fait le maillon qui relie la création monétaire privée à la politique "
  "monétaire : le taux de refinancement à une semaine est le principal signal "
  "envoyé par la banque centrale.",
  "Le cours présente le refinancement comme l’étape qui vient après la "
  "création monétaire, et c’est cet ordre qui en éclaire le rôle. La nécessité "
  "d’abord : les entreprises et les ménages demandent un crédit, la banque "
  "crée de la monnaie scripturale, puis, pour sécuriser cette création, elle "
  "doit obtenir de la monnaie centrale, qu’elle trouve auprès d’autres banques "
  "sur le marché interbancaire ou auprès de la banque centrale par "
  "refinancement. Les deux sources ensuite. Le marché interbancaire est le "
  "premier relais de la politique monétaire : les banques s’y prêtent des "
  "liquidités, à un taux de référence aujourd’hui appelé €STR dans la zone "
  "euro, qui a remplacé l’ancien EONIA. Le mécanisme de transmission est "
  "explicite : une baisse des taux directeurs fait baisser l’€STR, donc le "
  "coût de refinancement des banques, donc les taux débiteurs, ce qui "
  "augmente la demande de crédit et la création monétaire. La banque centrale "
  "ensuite, qui fixe trois taux directeurs. Le taux de facilité de dépôt est "
  "celui auquel les banques peuvent placer leurs liquidités auprès d’elle, et "
  "constitue le taux plancher : s’il est élevé, les banques peuvent préférer "
  "placer leur argent plutôt que prêter. Le taux de facilité de prêt est celui "
  "auquel elles peuvent emprunter à très court terme, et constitue le taux "
  "plafond, bornant le coût maximal du refinancement de court terme. Le taux "
  "de refinancement, taux de crédit à une semaine, est le principal signal "
  "monétaire. Les deux facilités forment le corridor des taux directeurs, qui "
  "encadre les taux du marché monétaire et permet d’orienter les échanges de "
  "liquidités entre banques, de stabiliser le marché interbancaire et de "
  "transmettre efficacement la politique monétaire. Le cours ajoute les "
  "instruments de long terme, prêts accordés par la banque centrale aux "
  "banques, parfois de manière ciblée.",
  [("La séquence création puis refinancement",
    "La banque crée d’abord la monnaie scripturale en accordant le crédit, "
    "puis se procure la monnaie centrale nécessaire : le refinancement ne "
    "précède pas le prêt, il le sécurise."),
   ("Le recours au marché interbancaire",
    "Les banques excédentaires en liquidités prêtent aux banques "
    "déficitaires : ce marché mutualise les besoins de monnaie centrale et son "
    "taux de référence transmet la politique monétaire à l’ensemble du "
    "système."),
   ("Le corridor des taux directeurs",
    "La facilité de dépôt fixe le plancher et la facilité de prêt le plafond : "
    "les taux du marché monétaire évoluent entre les deux, ce qui donne à la "
    "banque centrale la maîtrise de l’intervalle sans fixer directement le "
    "prix."),
   ("La transmission aux taux bancaires",
    "Une baisse des taux directeurs réduit le taux interbancaire, donc le "
    "coût de refinancement, donc les taux débiteurs pratiqués : la demande de "
    "crédit augmente et la création monétaire avec elle."),
   ("L’arbitrage entre prêter et placer",
    "Si le taux de facilité de dépôt est élevé, les banques peuvent préférer "
    "placer leurs liquidités auprès de la banque centrale plutôt que de "
    "prêter : le plancher du corridor agit donc directement sur l’offre de "
    "crédit.")],
  [{'a': "Le refinancement donne à la banque centrale une prise réelle sur la "
         "création monétaire privée, par le coût qu’elle lui impose.",
    'cond': "La prise suppose que les banques aient effectivement besoin de "
            "monnaie centrale, donc que retraits et réserves obligatoires "
            "soient significatifs.",
    'lim': "Le courant keynésien objecte que la banque centrale fournit "
           "presque toujours la monnaie demandée, de sorte que la contrainte "
           "porte sur le prix et non sur la quantité."},
   {'a': "Le corridor est un dispositif élégant, puisqu’il borne les taux du "
         "marché sans les administrer.",
    'cond': "Il exige un marché interbancaire actif, où les banques se "
            "prêtent effectivement des liquidités entre elles.",
    'lim': "Ce marché peut se bloquer, comme en 2008 lorsque la défiance "
           "entre banques a interrompu les prêts, ce qui a contraint la "
           "banque centrale à intervenir directement."},
   {'a': "Le taux de facilité de dépôt permet d’agir sur l’arbitrage des "
         "banques entre prêter et placer leurs liquidités.",
    'cond': "L’effet suppose que les banques disposent effectivement de "
            "liquidités excédentaires à placer.",
    'lim': "Pousser ce taux en territoire négatif, comme certaines banques "
           "centrales l’ont fait, a des effets incertains et vise les banques "
           "plutôt que directement les ménages."},
   {'a': "Les prêts de long terme accordés aux banques, parfois ciblés, "
         "permettent de soutenir le crédit là où il manque.",
    'cond': "Leur efficacité suppose que les banques transmettent ce "
            "financement bon marché sous forme de crédits nouveaux.",
    'lim': "Rien ne garantit cette transmission en période de prudence "
           "bancaire, ce qui est précisément la situation de la trappe à "
           "liquidité."}],
  [{'t': "Le taux de refinancement à une semaine est le principal signal "
         "monétaire envoyé par la banque centrale.",
    'qui': "Le cours, dans sa présentation des trois taux directeurs.",
    'rep': "Le cours montre que ce signal ne suffit plus lorsque les taux "
           "approchent de zéro : il faut alors agir sur les bilans, les "
           "titres et les anticipations par des instruments non "
           "conventionnels."},
   {'t': "Le marché interbancaire est le premier relais de la transmission de "
         "la politique monétaire.",
    'qui': "L’analyse du cours sur le rôle de l’€STR, qui a remplacé "
           "l’EONIA.",
    'rep': "Ce relais est fragile : la crise de 2008 a provoqué une chute de "
           "la confiance et un blocage du crédit, ce qui a désorganisé "
           "précisément les échanges de liquidités entre banques."},
   {'t': "Puisque la banque centrale fournit le refinancement nécessaire, "
         "elle ne contraint pas réellement la création monétaire.",
    'qui': "Le courant keynésien, avec le diviseur de crédit.",
    'rep': "Le cours rappelle qu’elle en fixe le coût : en modifiant ses taux "
           "directeurs, elle modifie les taux débiteurs et donc la demande de "
           "crédit, ce qui constitue une contrainte par le prix."}],
  [{'n': "John Maynard Keynes",
    'i': "La banque se refinance après avoir prêté, et la banque centrale lui "
         "fournit presque toujours la monnaie centrale nécessaire.",
    'p': "Le cours en fait la quatrième étape du diviseur de crédit, en "
         "précisant la raison de cette fourniture : la banque centrale doit "
         "garantir la stabilité du système et le financement de l’économie, ce "
         "qui limite sa capacité de refus."},
   {'n': "Milton Friedman",
    'i': "La banque centrale doit contrôler la croissance de la masse "
         "monétaire par une règle simple et prévisible.",
    'p': "Le cours rattache à cette position l’idée que la masse monétaire "
         "devrait augmenter à un rythme constant indépendant de la "
         "conjoncture, ce qui revient à refuser d’ajuster le refinancement aux "
         "besoins du moment."},
   {'n': "Éric Monnet",
    'i': "La banque centrale est devenue un fournisseur permanent de "
         "liquidité au système bancaire.",
    'p': "Le cours mobilise La Banque Providence, en 2021, pour montrer que "
         "le refinancement, conçu comme un appoint, s’est transformé en "
         "soutien structurel, ce qui participe de l’élargissement des "
         "missions des banques centrales."}],
  [{'f': "Le cours décrit la chaîne de transmission : baisse des taux "
         "directeurs, baisse de l’€STR, baisse du coût de refinancement des "
         "banques, baisse des taux débiteurs, hausse de la demande de crédit, "
         "hausse de la création monétaire.",
    'p': "La chaîne montre que le refinancement est le point de passage "
         "obligé par lequel une décision de la banque centrale atteint les "
         "emprunteurs finaux."},
   {'f': "L’EONIA, ancien taux de référence interbancaire au jour le jour de "
         "la zone euro, a été remplacé par l’€STR.",
    'p': "Le changement de référence montre que l’infrastructure du "
         "refinancement est elle-même un objet de réforme, la fiabilité du "
         "taux de référence conditionnant la transmission."},
   {'f': "Le cours précise que si le taux de facilité de dépôt est élevé, les "
         "banques peuvent préférer placer leur argent auprès de la banque "
         "centrale plutôt que prêter.",
    'p': "L’arbitrage démontre que le plancher du corridor n’est pas un "
         "simple repère technique : il agit directement sur l’offre de crédit "
         "à l’économie."}],
  [{'q': "Pourquoi une banque doit-elle se refinancer ?",
    'f': "Parce que la monnaie qu’elle crée est scripturale, alors que ses "
         "clients retirent des billets et qu’elle doit constituer des réserves "
         "obligatoires. Le cours résume la séquence : les agents demandent un "
         "crédit, la banque crée de la monnaie scripturale, puis pour "
         "sécuriser cette création elle doit obtenir de la monnaie centrale, "
         "auprès des autres banques ou de la banque centrale.",
    'r': "Le raisonnement distingue les deux monnaies, scripturale et "
         "centrale, et montre que le refinancement est le pont obligé entre "
         "les deux étages du système.",
    'ex': "Le cours présente cette séquence en trois étapes, création puis "
          "obtention puis sources possibles."},
   {'q': "Comment la banque centrale transmet-elle ses décisions ?",
    'f': "Par le coût du refinancement, relayé par le marché interbancaire. "
         "Le cours décrit la chaîne : une baisse des taux directeurs fait "
         "baisser l’€STR, donc le coût de refinancement des banques, donc les "
         "taux débiteurs, ce qui augmente la demande de crédit puis la "
         "création monétaire. Le corridor, borné par les deux facilités, "
         "encadre cet ajustement.",
    'r': "On suit la transmission maillon par maillon, ce qui permet "
         "d’identifier où elle peut se rompre, notamment si le marché "
         "interbancaire se bloque.",
    'ex': "Le taux de refinancement à une semaine est le principal signal "
          "monétaire selon le cours."},
   {'q': "Le refinancement limite-t-il la création monétaire ?",
    'f': "Par le prix plutôt que par la quantité. Le courant keynésien "
         "souligne que la banque centrale fournit presque toujours la monnaie "
         "centrale nécessaire, car elle doit garantir la stabilité du système "
         "et le financement de l’économie. Mais elle en fixe le coût, et ce "
         "coût se répercute sur les taux débiteurs, donc sur le volume de "
         "crédit demandé.",
    'r': "Le raisonnement distingue une contrainte quantitative, largement "
         "inopérante, d’une contrainte par le prix, qui demeure, ce qui "
         "concilie les deux lectures.",
    'ex': "Le corridor des taux directeurs borne le coût maximal du "
          "refinancement de court terme."}],
  voisins=['n11-multiplicateur-diviseur', 'n11-banque-centrale',
           'n11-banques-commerciales', 'n11-preteur-dernier-ressort'])


d('n11-preteur-dernier-ressort', 11, "Prêteur en dernier ressort",
  "Fournir la liquidité que le marché refuse, au risque de l’aléa moral",
  "Le prêteur en dernier ressort est la fonction par laquelle la banque "
  "centrale fournit des liquidités aux banques en cas de crise, lorsque ni "
  "leurs déposants ni le marché interbancaire ne le font plus. Le cours la "
  "range parmi les trois missions de la Banque centrale européenne, aux côtés "
  "de la stabilité des prix et de la liquidité du système bancaire.",
  "Le cours construit cette fonction par le problème qu’elle résout, puis par "
  "le problème qu’elle crée. Le problème qu’elle résout est le risque de "
  "liquidité. Les banques utilisent des ressources à court terme, comme les "
  "dépôts de leurs clients, pour financer des activités à long terme, crédits "
  "ou investissements : si les déposants veulent retirer leur argent "
  "rapidement, la banque peut manquer de liquidités alors même que ses "
  "créances sont bonnes. Sans intervention, une difficulté de calendrier "
  "devient une faillite. Le cours en donne le cas historique avec le système "
  "de John Law : en 1720, les détenteurs veulent échanger leurs billets contre "
  "de l’or, la Banque n’a plus de réserves, et la panique provoque "
  "l’effondrement, une crise financière et la ruine des épargnants. Le cours "
  "rattache explicitement cette fonction à l’objectif de stabilité financière, "
  "devenu essentiel depuis la crise de 2008 : la banque centrale doit éviter "
  "les crises bancaires, les paniques de liquidité, le blocage du crédit, les "
  "faillites systémiques et les emballements spéculatifs, et il énumère les "
  "fonctions associées, prêteur en dernier ressort, soutien à la liquidité du "
  "système bancaire, stabilisation des marchés en période de crise et "
  "prévention du risque systémique. La banque centrale n’est donc plus "
  "seulement une institution anti-inflation, elle est aussi un pilier de la "
  "stabilité du système financier. Le problème que cette fonction crée est "
  "l’aléa moral, et le cours le nomme à plusieurs reprises. Les institutions "
  "jugées trop grandes pour faire faillite sont perçues comme implicitement "
  "protégées, ce qui peut les conduire à prendre trop de risques, à "
  "sous-estimer les conséquences et à accroître la fragilité du système, les "
  "profits restant privés tandis que les pertes sont en partie supportées par "
  "les banques centrales, les États et donc indirectement la collectivité.",
  [("La distinction entre illiquidité et insolvabilité",
    "Une banque solvable peut manquer de liquidités si ses ressources sont "
    "exigibles avant ses emplois : le prêteur en dernier ressort traite ce "
    "décalage de calendrier sans se substituer à la valeur des actifs."),
   ("L’interruption de la panique",
    "En annonçant qu’elle fournira la liquidité nécessaire, la banque "
    "centrale retire aux déposants l’intérêt de se précipiter : la garantie "
    "agit par anticipation, avant même d’être mobilisée."),
   ("La prévention de la contagion",
    "Les banques étant liées entre elles par le marché interbancaire, la "
    "défaillance de l’une menace les autres : soutenir une banque illiquide "
    "évite une chaîne de défauts, c’est-à-dire le risque systémique."),
   ("Le déblocage du crédit",
    "En période de défiance, le marché interbancaire se bloque et le crédit à "
    "l’économie se tarit : l’intervention de la banque centrale restaure la "
    "liquidité et permet aux banques de continuer à prêter."),
   ("La production d’aléa moral",
    "Ceux qui se savent protégés peuvent prendre davantage de risques et "
    "sous-estimer les conséquences de leurs décisions : la garantie qui "
    "stabilise à court terme fragilise le système à plus long terme.")],
  [{'a': "La fonction de prêteur en dernier ressort évite qu’un simple "
         "décalage d’échéances ne détruise une banque solvable.",
    'cond': "Elle suppose que l’on puisse distinguer une banque illiquide "
            "d’une banque insolvable, ce qui est difficile en pleine crise.",
    'lim': "Si la distinction est mal faite, la banque centrale soutient des "
           "établissements qu’il faudrait laisser disparaître, ce qui "
           "transfère les pertes à la collectivité."},
   {'a': "Elle prévient le risque systémique, puisque les banques sont liées "
         "entre elles et qu’une défaillance peut se propager.",
    'cond': "L’argument suppose une interdépendance réelle du système, par le "
            "marché interbancaire et par les engagements croisés.",
    'lim': "Cette interdépendance est aussi ce qui rend certains acteurs "
           "implicitement protégés, d’où le problème des institutions trop "
           "grandes pour faire faillite."},
   {'a': "La garantie agit par anticipation : sa seule existence réduit la "
         "probabilité des paniques qu’elle est censée traiter.",
    'cond': "L’effet dissuasif exige que l’engagement de la banque centrale "
            "soit jugé crédible par les déposants et par les marchés.",
    'lim': "Une garantie crédible est exactement celle qui produit le plus "
           "d’aléa moral, puisqu’elle rassure aussi ceux qui prennent des "
           "risques excessifs."},
   {'a': "Faire de la stabilité financière un objectif explicite rend "
         "l’intervention prévisible plutôt qu’improvisée.",
    'cond': "Elle suppose que la banque centrale dispose des instruments "
            "correspondants, soutien à la liquidité et stabilisation des "
            "marchés.",
    'lim': "Cet objectif entre en tension avec la stabilité des prix, "
           "puisque fournir de la liquidité soutient le crédit et donc la "
           "création monétaire."}],
  [{'t': "La banque centrale doit agir comme prêteur en dernier ressort en "
         "cas de crise des banques.",
    'qui': "Le cours, dans son énoncé des trois missions de la Banque "
           "centrale européenne.",
    'rep': "Le cours relève immédiatement la contrepartie : le soutien à la "
           "stabilité financière comporte un risque d’aléa moral et peut "
           "encourager les comportements imprudents."},
   {'t': "Les institutions trop grandes pour faire faillite doivent être "
         "secourues, puisque leur chute menacerait le système bancaire, les "
         "paiements, le crédit et l’économie réelle.",
    'qui': "La logique implicite du traitement des acteurs systémiques, que "
           "le cours décrit.",
    'rep': "Le cours objecte la socialisation des pertes : les profits "
           "peuvent être privés tandis que les pertes sont supportées par les "
           "banques centrales, les États et donc indirectement la "
           "collectivité."},
   {'t': "La séparation des activités bancaires réduirait le besoin "
         "d’intervention en dernier ressort.",
    'qui': "Les économistes qui, selon le cours, préfèrent séparer les "
           "activités bancaires pour plus de sécurité.",
    'rep': "La séparation limite le risque de liquidité mais prive l’économie "
           "d’un financement long : les banques de dépôts limitées à deux ans "
           "ne financent pas les usines ni les infrastructures."}],
  [{'n': "John Law",
    'i': "Une banque privée de réserves ne peut pas honorer une demande "
         "simultanée de conversion.",
    'p': "Le cours décrit l’effondrement de 1720 : les détenteurs veulent "
         "échanger leurs billets contre de l’or, la Banque n’a plus de "
         "réserves, la panique survient, et il en résulte une crise "
         "financière, la ruine des épargnants et une hostilité durable envers "
         "la monnaie papier."},
   {'n': "Éric Monnet",
    'i': "La banque centrale est devenue un acteur plus large de la "
         "gouvernance économique.",
    'p': "Dans La Banque Providence, en 2021, il montre que ses missions "
         "s’élargissent au-delà de la stabilité des prix, de la croissance et "
         "de la stabilité financière, jusqu’à la transition écologique, la "
         "monnaie digitale et la dette publique."},
   {'n': "Christine Lagarde",
    'i': "Les économies contemporaines connaissent une succession constante "
         "de crises inédites majeures.",
    'p': "Le cours ouvre sur ce diagnostic de permacrises, qui explique "
         "l’institutionnalisation du prêt en dernier ressort : conçu comme un "
         "recours exceptionnel, il devient un instrument régulier dans un "
         "contexte de crises répétées."}],
  [{'f': "Le cours énumère ce que la banque centrale doit éviter : crises "
         "bancaires, paniques de liquidité, blocage du crédit, faillites "
         "systémiques et emballements spéculatifs.",
    'p': "L’énumération montre que le prêt en dernier ressort s’inscrit dans "
         "un ensemble de missions de stabilité, et non dans une intervention "
         "ponctuelle de sauvetage."},
   {'f': "Les institutions trop grandes pour faire faillite sont souvent "
         "perçues comme implicitement protégées, ce qui peut les conduire à "
         "prendre trop de risques et à sous-estimer les conséquences.",
    'p': "Le mécanisme démontre que la garantie modifie le comportement de "
         "ceux qu’elle protège, ce qui est la définition même de l’aléa "
         "moral."},
   {'f': "La crise de 2008 provoque une chute de la confiance et un blocage "
         "du crédit, ce qui conduit les banques centrales à intervenir "
         "massivement.",
    'p': "Le cas montre que le prêt en dernier ressort ne concerne pas "
         "seulement des banques isolées : il peut devoir suppléer le marché "
         "interbancaire tout entier."}],
  [{'q': "Faut-il toujours sauver les banques ?",
    'f': "Le cours donne les deux faces du problème. Ne pas intervenir "
         "expose à des crises bancaires, des paniques de liquidité, un blocage "
         "du crédit et des faillites systémiques, c’est-à-dire à la "
         "destruction de l’économie réelle. Intervenir crée un aléa moral : "
         "les acteurs qui se savent protégés prennent trop de risques et "
         "accroissent la fragilité du système.",
    'r': "Le raisonnement met en regard un coût immédiat et certain, la "
         "crise, et un coût différé et probabiliste, l’imprudence encouragée, "
         "ce qui explique que l’intervention soit la règle malgré ses "
         "défauts.",
    'ex': "Le cours relève que les profits peuvent être privés tandis que les "
          "pertes sont supportées par la collectivité."},
   {'q': "Pourquoi une banque solvable peut-elle faire faillite ?",
    'f': "Parce que la solvabilité porte sur la valeur de ses actifs et la "
         "liquidité sur leur disponibilité. Le cours l’explique précisément : "
         "la banque a prêté à long terme des ressources exigibles à court "
         "terme, de sorte qu’une demande simultanée de retraits la met en "
         "défaut même si ses emprunteurs remboursent normalement.",
    'r': "On sépare deux risques que l’on confond souvent, ce qui justifie "
         "une intervention limitée à l’illiquidité et non à l’insolvabilité.",
    'ex': "La Banque Royale de 1720 détenait des actifs mais n’avait plus les "
          "réserves pour honorer les conversions."},
   {'q': "Le prêt en dernier ressort suffit-il à prévenir les crises ?",
    'f': "Il les arrête mais ne les empêche pas. Le cours montre qu’il traite "
         "le symptôme, l’assèchement de la liquidité, sans corriger la cause, "
         "le mélange des horizons dans les banques universelles et la prise "
         "de risque encouragée par la protection implicite. D’où le débat sur "
         "la séparation des activités et sur les règles prudentielles.",
    'r': "Le raisonnement distingue le traitement curatif du traitement "
         "préventif, et montre que le premier peut aggraver le besoin du "
         "second.",
    'ex': "Certains économistes préfèrent séparer les activités bancaires "
          "pour plus de sécurité selon le cours."}],
  voisins=['n11-banque-centrale', 'n13-alea-moral-sauvetages',
           'n13-crise-bancaire', 'n11-refinancement'])
