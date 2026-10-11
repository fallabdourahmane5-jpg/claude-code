# -*- coding: utf-8 -*-
"""Résumé approfondi du chapitre 4 — Analyse microéconomique : le consommateur
et le producteur."""

R = {'4': {

 'q': "Jusqu’où les mathématiques rendent-elles compte des comportements humains : le modèle "
      "du consommateur et du producteur rationnels décrit-il la réalité, et aboutit-il "
      "seulement à un équilibre stable ?",

 'ess':
  "Le chapitre construit le modèle standard pièce par pièce, puis le démonte avec la même "
  "rigueur. Il prolonge directement la partie du chapitre 3 consacrée aux néoclassiques : "
  "ceux-ci veulent mettre l’économie en équations, ce qui suppose un individu parfaitement "
  "rationnel. On part du consommateur, qui maximise une utilité sous contrainte de revenu, et "
  "dont l’équilibre se lit comme une tangence où le taux marginal de substitution égale le "
  "rapport des prix. Les élasticités traduisent ce comportement en grandeurs mesurables et "
  "font apparaître les premiers cas rebelles — biens de Giffen et de Veblen. On passe ensuite "
  "au producteur, avec un raisonnement volontairement parallèle : isoquantes au lieu de "
  "courbes d’indifférence, isocoût au lieu de contrainte budgétaire, taux marginal de "
  "substitution technique au lieu de TMS — puis toute la famille des coûts, dont la forme "
  "s’explique par la productivité. L’agrégation conduit à l’équilibre général : Say donne "
  "l’intuition, Walras la formalise, Arrow et Debreu en posent sept conditions très "
  "restrictives. Et c’est de l’intérieur que vient le coup le plus dur : le théorème de "
  "Sonnenschein, Mantel et Debreu montre que l’existence d’un équilibre ne garantit ni sa "
  "stabilité ni la convergence vers lui. Le dernier mouvement du chapitre porte sur les "
  "agents eux-mêmes : rationalité limitée chez Simon, asymétries d’information chez Akerlof, "
  "biais cognitifs chez Kahneman et Thaler, et interactions stratégiques en théorie des jeux.",

 'parties': [

  # ------------------------------------------------------------------ I
  {'t': "I. Introduction : le projet marginaliste et ses trois questions",
   'sp': [
    {'t': "A. Mettre l’économie en équations",
     'd': ["Le point de départ est un projet intellectuel : faire de l’économie une science "
           "aussi rigoureuse que les mathématiques, en rompant avec une opposition française "
           "entre lettrés sans culture mathématique et calculateurs sans culture "
           "philosophique. Les marginalistes développent ainsi l’approche qui constitue "
           "aujourd’hui la théorie standard.",
           "Cette théorie part de l’individu, supposé parfaitement rationnel, et utilise les "
           "mathématiques pour formaliser ce comportement. Le chapitre est explicitement "
           "présenté comme le complément de la partie du chapitre 3 consacrée aux "
           "néoclassiques, et il pose trois questions : quels outils la microéconomie "
           "fournit-elle ? jusqu’où les mathématiques rendent-elles compte des comportements "
           "humains ? quel regard critique porter sur cette vision ?"],
     'lim': "Une rupture de méthode est à noter d’emblée : il n’y a plus de classes sociales en "
            "microéconomie. Le consommateur se définit par ses préférences et par les "
            "ressources dont il dispose, non par sa position dans la production — c’est tout "
            "l’écart avec les classiques et Marx."},
   ],
   'v': "Le premier objet de cette construction est le consommateur, dont il faut d’abord "
        "représenter les préférences."},

  # ----------------------------------------------------------------- II
  {'t': "II. La théorie du consommateur : maximiser une utilité sous contrainte",
   'sp': [
    {'t': "A. Utilité, panier de consommation et courbes d’indifférence",
     'd': ["L’ensemble des biens et services consommés forme un panier de consommation, et le "
           "consommateur cherche à maximiser la satisfaction qu’il en retire. Les "
           "microéconomistes simplifient en supposant un arbitrage entre deux biens X et Y : "
           "l’utilité est le résultat de leur combinaison, U = f(X, Y).",
           "Une courbe d’indifférence réunit toutes les combinaisons (X, Y) procurant le même "
           "niveau de satisfaction : le consommateur est indifférent entre les paniers situés "
           "sur une même courbe. Sur une même courbe, diminuer X oblige à augmenter Y, et "
           "inversement. L’ensemble des courbes d’indifférence constitue la carte du "
           "consommateur."]},
    {'t': "B. Les quatre hypothèses sur les préférences, et pourquoi elles sont contestées",
     'd': ["La complétude suppose que tout individu peut se prononcer sur n’importe quelle "
           "combinaison de biens, présents comme futurs : elle introduit une dimension "
           "intertemporelle.",
           "La transitivité suppose que les choix sont logiquement cohérents : si D est "
           "préféré à C et C à B, alors D est préféré à B. Cette hypothèse a une conséquence "
           "graphique directe : les courbes d’indifférence ne peuvent pas se croiser. Or les "
           "vérifications empiriques montrent que les individus ne sont pas toujours "
           "transitifs — c’est l’un des arguments de Steve Keen dans L’imposture économique "
           "(2014).",
           "La non-satiété suppose qu’on préfère toujours plus à moins : il n’existe pas de "
           "point de satiété. Elle est indispensable mathématiquement, car sans elle les "
           "courbes d’indifférence pourraient devenir discontinues ou mal ordonnées ; grâce à "
           "elle, une courbe plus éloignée de l’origine correspond toujours à une utilité plus "
           "élevée. Mais elle est contestée, notamment par Kate Raworth : pourquoi supposer "
           "qu’on veut toujours consommer davantage, et exclure qu’on puisse préférer moins ?",
           "La continuité suppose qu’on peut toujours faire varier la consommation d’une très "
           "petite quantité, donc que les biens sont divisibles. Or beaucoup ne le sont pas : "
           "on n’achète pas un quart de voiture, et les médicaments sont vendus par boîtes de "
           "16 ou 30 comprimés — ce qui provoque gaspillage, surconsommation et coûts pour la "
           "Sécurité sociale, certains pays ayant adopté la vente à l’unité."],
     'lim': "Le cours est explicite sur le statut de ces hypothèses : elles ne sont pas faites "
            "pour décrire les comportements réels mais pour rendre les modèles solubles — sans "
            "continuité, on ne pourrait ni dériver, ni optimiser, et les courbes seraient en "
            "marches d’escalier."},
    {'t': "C. Le taux marginal de substitution et la loi de Gossen",
     'd': ["Le consommateur ne peut pas tout avoir : consommer plus de X impose de renoncer à "
           "une partie de Y. Le taux marginal de substitution mesure cet arbitrage — le nombre "
           "d’unités de Y auxquelles il faut renoncer pour obtenir une unité supplémentaire de "
           "X, tout en restant sur la même courbe d’indifférence. C’est donc la pente de la "
           "courbe en un point.",
           "Le TMS est nécessairement négatif, puisque les courbes sont décroissantes et "
           "convexes : plus de X implique moins de Y. Quand on raisonne entre deux points "
           "éloignés, on écrit ΔY/ΔX ; quand on raisonne en un point, sur une variation "
           "infinitésimale, on écrit dY/dX — c’est une dérivée.",
           "Il ne faut pas confondre courbe d’indifférence et courbe d’utilité. La première a "
           "deux biens en axes, compare des paniers et porte le TMS : c’est un outil "
           "bidimensionnel. La seconde a en abscisse la quantité d’un seul bien et en ordonnée "
           "l’utilité : c’est un outil unidimensionnel, croissant mais concave.",
           "Cette concavité s’explique par la loi de Gossen : l’utilité marginale — la "
           "satisfaction apportée par une unité supplémentaire — est décroissante. L’utilité "
           "totale augmente donc toujours, mais de moins en moins vite, l’utilité marginale "
           "étant la pente de la courbe d’utilité totale."],
     'mec': "Utilité totale croissante et concave ⇔ utilité marginale décroissante (Gossen) ; "
            "TMS = dY/dX < 0, décroissant du fait de la convexité."},
    {'t': "D. L’équilibre du consommateur et la décomposition d’une variation de prix",
     'd': ["Le consommateur maximise son utilité sous contrainte budgétaire : l’équilibre est "
           "atteint au point de tangence entre la droite de budget et la courbe d’indifférence "
           "la plus élevée accessible, c’est-à-dire là où TMS = −Px/Py.",
           "Une variation de prix produit deux effets distincts qu’il faut savoir séparer. "
           "L’effet de substitution : si le prix d’un bien baisse, on en consomme davantage au "
           "détriment de l’autre — on reste sur la même courbe d’indifférence, mais on se "
           "déplace le long de celle-ci, et la pente de la droite de budget change. L’effet de "
           "revenu : la baisse du prix donne l’impression que le revenu réel augmente à revenu "
           "nominal inchangé, de sorte qu’on peut consommer plus des deux biens — on passe "
           "alors à une courbe d’indifférence plus élevée, sur une droite de budget parallèle "
           "déplacée vers la droite.",
           "L’exemple du cours est simple : si le prix du burger baisse et celui de la glace "
           "ne change pas, la consommation de burgers augmente dans les deux cas ; la vraie "
           "question est de savoir si, pour la glace, l’effet de substitution l’emporte sur "
           "l’effet de revenu."],
     'lim': "C’est précisément parce que ces deux effets peuvent jouer en sens contraire que "
            "la demande n’est pas toujours mécaniquement décroissante — point sur lequel "
            "reviendront les biens de Giffen puis la critique de l’équilibre partiel."},
   ],
   'v': "Pour sortir du graphique et mesurer les comportements, il faut un outil quantitatif : "
        "l’élasticité."},

  # ---------------------------------------------------------------- III
  {'t': "III. Les élasticités : mesurer la sensibilité et classer les biens",
   'sp': [
    {'t': "A. Ce qu’est une élasticité, et pour qui c’est un avantage",
     'd': ["Une élasticité est un rapport entre deux variations : elle mesure à quel point une "
           "grandeur réagit quand une autre change. Un bien est élastique quand il est "
           "sensible à la variation des prix, inélastique quand il l’est peu.",
           "Le cours insiste sur le fait que la même propriété n’a pas la même valeur selon "
           "l’agent. Pour le consommateur, un bien élastique est un avantage : il existe des "
           "substituts, il n’est pas prisonnier d’un prix, il peut changer de produit ou "
           "réduire sa consommation. Pour le producteur, une demande inélastique est une "
           "assurance : une hausse de prix ne fait presque pas baisser les quantités, donc le "
           "chiffre d’affaires augmente — mais c’est aussi un signal, car baisser les prix ne "
           "servirait à rien. Pour le consommateur, l’inélasticité est au contraire un "
           "problème : sans alternative, il est contraint de payer plus."]},
    {'t': "B. Trois élasticités et la typologie des biens",
     'd': ["L’élasticité-prix rapporte la variation relative de la demande à celle du prix du "
           "bien lui-même : e = (ΔQ/Q) ÷ (ΔP/P). Elle est généralement négative ; |e| > 1 "
           "signale un bien élastique, |e| < 1 un bien inélastique.",
           "L’élasticité-revenu mesure la réaction de la demande à une variation du revenu et "
           "fournit une typologie : bien inférieur si e < 0 — la demande baisse quand le "
           "revenu monte ; bien normal si 0 < e < 1 ; bien supérieur si e > 1 — la demande "
           "augmente plus vite que le revenu. Le cours fait le lien explicite avec la loi "
           "d’Engel : dire que la structure de consommation change quand le revenu augmente, "
           "c’est déjà parler d’élasticité-revenu.",
           "Deux cas particuliers contredisent la loi de la demande, et il ne faut pas les "
           "confondre. Le bien de Giffen est un bien inférieur consommé en contexte de grande "
           "pauvreté : quand son prix augmente, sa consommation augmente, par contrainte, "
           "faute de pouvoir se payer un substitut plus cher. Le bien de Veblen est un bien de "
           "luxe : quand son prix augmente, sa consommation augmente aussi, mais par affichage "
           "social. Même courbe, raisons opposées — l’une par pauvreté, l’autre par richesse.",
           "L’élasticité-prix croisée mesure l’effet du prix d’un bien B sur la demande du "
           "bien A. Si elle est négative, les biens sont complémentaires : le prix de la place "
           "de cinéma augmente, la consommation de popcorn baisse. Si elle est positive, ils "
           "sont substituables : le prix du cinéma augmente, on se reporte sur la vidéo à la "
           "demande. Si elle est nulle, les biens sont indépendants."],
     'mec': "Élasticité-revenu : e < 0 inférieur, 0 < e < 1 normal, e > 1 supérieur. Croisée : "
            "négative = complémentaires, positive = substituables, nulle = indépendants."},
    {'t': "C. Ce qui détermine le niveau de l’élasticité",
     'd': ["L’élasticité n’est pas une constante. Le temps joue d’abord : à court terme, les "
           "consommateurs sont coincés par leurs habitudes et leurs équipements, donc la "
           "demande est peu élastique ; à long terme, ils s’adaptent et cherchent des "
           "alternatives, donc la demande devient plus élastique. L’exemple historique est le "
           "choc pétrolier : le baril passe de 5 à 15 dollars en 1973, puis à 30 dollars en "
           "1979 ; à court terme il n’existe aucun substitut immédiat et la demande est "
           "inélastique ; à long terme les entreprises modifient leurs procédés et réduisent "
           "leur consommation de matière première.",
           "L’existence de substituts est le deuxième facteur, et la règle est simple : plus "
           "il existe de substituts, plus la demande est élastique. Or les substituts "
           "apparaissent surtout à long terme — les deux facteurs se renforcent.",
           "Le troisième facteur est plus subtil : l’élasticité dépend du degré de précision "
           "de la catégorie étudiée. Pour un produit très précis — le skyr d’une marque — il "
           "existe beaucoup de substituts, donc la demande est très élastique. Pour une "
           "catégorie intermédiaire — les yaourts — il y en a moins. Pour une catégorie large "
           "— les produits laitiers — il n’y a guère de substituts proches dans les habitudes "
           "alimentaires, donc la demande est inélastique."],
     'lim': "La conséquence méthodologique est importante : une élasticité mesurée n’a de sens "
            "que si l’on précise sur quelle catégorie de biens et sur quel horizon elle a été "
            "calculée."},
   ],
   'v': "Le même raisonnement marginaliste s’applique maintenant à celui qui produit, avec un "
        "parallélisme voulu dans les outils."},

  # ----------------------------------------------------------------- IV
  {'t': "IV. La théorie du producteur : facteurs, rendements et coûts",
   'sp': [
    {'t': "A. La fonction de production et la définition logique du court terme",
     'd': ["Produire, c’est créer un output en combinant des inputs : le travail L et le "
           "capital K. La fonction de production Q = f(K, L) est l’équivalent de la fonction "
           "d’utilité du consommateur.",
           "L’hypothèse centrale est qu’à court terme, un seul facteur est variable — en "
           "général le travail, le capital étant fixe. Elle est réaliste : face à plus de "
           "commandes, une entreprise augmente les heures de travail ou embauche, mais "
           "n’achète pas immédiatement de nouvelles machines.",
           "Le cours insiste sur un point de vocabulaire décisif : chez les néoclassiques, le "
           "temps n’est pas chronologique mais logique. Le court terme n’est pas « moins de "
           "deux ans » : c’est la situation où au moins un facteur est fixe. Le long terme est "
           "celle où tous les facteurs sont variables — ce qui dépend du secteur, de la "
           "technologie et de l’organisation de la production."]},
    {'t': "B. Les productivités et la loi des rendements décroissants",
     'd': ["La productivité moyenne du travail, PM = Q/L, mesure ce que produit un "
           "travailleur en moyenne. La productivité marginale, Pm = ΔQ/ΔL, mesure ce "
           "qu’apporte le dernier travailleur embauché. On peut aussi raisonner sur la "
           "productivité globale, ΔQ/Δ(K + L).",
           "La loi de la productivité marginale décroissante énonce qu’à capital fixe, "
           "l’augmentation du travail finit par faire baisser la productivité marginale : au "
           "début ajouter du travail augmente fortement la production, puis chaque travailleur "
           "supplémentaire apporte de moins en moins.",
           "Trois relations sont à connaître : si Pm > PM la productivité moyenne augmente ; "
           "si Pm < PM elle baisse ; si Pm = PM elle est maximale. Autrement dit, la courbe de "
           "productivité marginale coupe la courbe de productivité moyenne en son maximum."],
     'mec': "Pm > PM → PM ↑ ; Pm < PM → PM ↓ ; Pm = PM → PM maximale."},
    {'t': "C. Rendements factoriels et rendements d’échelle",
     'd': ["Les deux notions correspondent à deux horizons différents. On parle de rendements "
           "factoriels quand un seul facteur varie, les autres étant fixes : c’est le court "
           "terme, et c’est l’objet de la loi des rendements marginaux décroissants.",
           "On parle de rendements d’échelle quand tous les facteurs varient dans les mêmes "
           "proportions : c’est le long terme, et l’on observe ce qui arrive à la production "
           "lorsque l’entreprise change d’échelle. L’hypothèse implicite est que l’intensité "
           "capitalistique K/L — la quantité de capital par unité de travail — reste constante.",
           "Trois cas. Rendements constants : +10 % de K et +10 % de L donnent +10 % de Q — "
           "doubler les facteurs double la production. Rendements croissants : +10 % et +10 % "
           "donnent +15 %, ce qui renvoie aux économies d’échelle, à une meilleure "
           "organisation et à la spécialisation du travail, en lien direct avec Smith. "
           "Rendements décroissants : +10 % et +10 % ne donnent que +5 %, du fait d’une "
           "mauvaise coordination, d’une gestion plus complexe ou d’une taille excessive."]},
    {'t': "D. Isoquantes, isocoût et taux marginal de substitution technique",
     'd': ["Le programme du producteur est construit en parallèle de celui du consommateur, "
           "avec un vocabulaire différent. Sur un graphique ayant le travail en abscisse et le "
           "capital en ordonnée, une isoquante est l’équivalent de la courbe d’indifférence : "
           "l’ensemble des combinaisons de K et L permettant d’obtenir un même niveau de "
           "production. Ses propriétés sont les mêmes : une isoquante par niveau de "
           "production, décroissante, ne se croisant jamais — sinon une même combinaison "
           "donnerait deux niveaux de production différents — et convexe, ce qui traduit "
           "qu’une combinaison des deux facteurs vaut mieux que tout capital ou tout travail.",
           "La droite d’isocoût est l’équivalent de la droite budgétaire : elle réunit toutes "
           "les combinaisons de K et L ayant le même coût total, compte tenu du salaire w et "
           "du coût du capital r. Le producteur choisit le point de tangence entre "
           "l’isoquante visée et la droite d’isocoût : c’est la combinaison qui produit un "
           "niveau donné au moindre coût.",
           "Le taux marginal de substitution technique mesure la quantité de capital à "
           "laquelle on peut renoncer en employant une unité de travail de plus, à production "
           "constante : TMST = −ΔK/ΔL. Il est négatif, puisqu’il faut réduire un facteur pour "
           "augmenter l’autre, et décroissant, puisque les isoquantes sont convexes et que les "
           "facteurs ne sont pas parfaitement substituables.",
           "La démonstration à connaître consiste à multiplier numérateur et dénominateur par "
           "ΔQ : TMST = −(ΔK/ΔQ)/(ΔL/ΔQ). Or ΔQ/ΔK est la productivité marginale du capital et "
           "ΔQ/ΔL celle du travail, donc TMST = −PmL/PmK. Économiquement, le producteur "
           "compare ce que rapporte une unité de travail supplémentaire à ce que rapporte une "
           "unité de capital supplémentaire."],
     'mec': "TMST = −ΔK/ΔL = −PmL/PmK. Application : une hausse des cotisations sociales élève "
            "le coût du travail → effet de substitution en faveur du capital (caisses "
            "automatiques) ; et comme le budget réel diminue, le producteur rationnel réduit "
            "aussi l’usage des deux facteurs."},
    {'t': "E. Les coûts de production et leur lien avec la productivité",
     'd': ["Les coûts fixes ne dépendent pas du niveau de production et existent même si elle "
           "est nulle : loyers, machines déjà achetées, assurances, salaires administratifs. "
           "Les coûts variables dépendent de la quantité produite : matières premières, "
           "énergie, main-d’œuvre productive. Leur somme est le coût total, CT = CF + CV.",
           "Le producteur veut aussi connaître son coût unitaire. Le coût moyen CM = CT/Q se "
           "décompose en coût fixe moyen CFM = CF/Q, strictement décroissant puisque CF est "
           "constant, et coût variable moyen CVM = CV/Q, qui diminue d’abord grâce à une "
           "meilleure organisation puis augmente avec les rendements décroissants — d’où une "
           "forme en U. Le minimum du coût moyen correspond au seuil de rentabilité.",
           "Le coût marginal Cm = ΔCT/ΔQ répond à la question : combien coûte une unité "
           "supplémentaire ? Il est lui aussi en U, et surtout il coupe le coût moyen et le "
           "coût variable moyen en leur minimum. Les règles à connaître : si Cm < CM, le coût "
           "moyen diminue ; si Cm > CM, il augmente.",
           "La forme de ces courbes s’explique entièrement par la productivité : le coût "
           "marginal varie en sens inverse de la productivité marginale, et le coût moyen en "
           "sens inverse de la productivité moyenne. C’est pourquoi le maximum de Pm "
           "correspond au minimum de Cm, et le maximum de PM au minimum de CM."],
     'mec': "Pm ↑ → Cm ↓ ; Pm ↓ → Cm ↑ ; PM ↑ → CM ↓ ; PM ↓ → CM ↑. D’où : max de Pm ⇔ min de "
            "Cm, max de PM ⇔ min de CM."},
    {'t': "F. Rentabilité, seuils et maximisation du profit",
     'd': ["Une entreprise est rentable lorsque P ≥ CM : si P > CM elle fait un profit, si "
           "P = CM elle est au seuil de rentabilité, si P < CM elle fait des pertes. Mais à "
           "court terme elle peut continuer tant que P ≥ CVM : même sans couvrir ses coûts "
           "fixes, elle couvre au moins ses coûts variables. Le cours justifie ce point : en "
           "début d’activité, une entreprise doit d’abord couvrir ses coûts variables, les "
           "investissements se rentabilisant au fil des années.",
           "À long terme, la courbe de coût moyen de longue période est l’enveloppe des "
           "courbes de courte période : l’entreprise choisit l’échelle qui minimise son coût. "
           "Quand produire davantage réduit le coût unitaire, on parle d’économies d’échelle ; "
           "quand les coûts augmentent plus vite que la production, de déséconomies d’échelle.",
           "Le profit se calcule comme CA − CT, avec CA = P × Q et CT = CM × Q. Dans la "
           "logique néoclassique, le producteur ne fixe pas son prix : en raison des "
           "hypothèses de la concurrence pure et parfaite, il est preneur de prix."],
     'lim': "Steve Keen objecte que ce schéma décrit l’industrie mais plus l’économie "
            "numérique : produire un film coûte cher, le dupliquer ne coûte presque rien, si "
            "bien que plus on produit, plus c’est rentable — l’inverse de la logique en U "
            "héritée de l’industrie automobile."},
   ],
   'v': "Reste à savoir si tous ces équilibres partiels peuvent tenir ensemble : c’est le "
        "passage à l’équilibre général."},

  # ------------------------------------------------------------------ V
  {'t': "V. De l’équilibre partiel à l’équilibre général — et sa critique interne",
   'sp': [
    {'t': "A. L’équilibre partiel et les limites du ceteris paribus",
     'd': ["Marshall raisonne ceteris paribus, toutes choses égales par ailleurs : on étudie "
           "un marché isolément, comme on place un objet au microscope. C’est une démarche "
           "scientifique de simplification, assumée comme telle.",
           "Le danger est d’en conclure que ce qui se passe sur ce marché n’a aucun effet "
           "ailleurs. Or les biens sont liés par des relations de substitution et de "
           "complémentarité, les revenus changent, les entreprises réagissent, l’emploi et le "
           "crédit bougent : un choc se propage.",
           "Le cours détaille la boucle de rétroaction côté producteur : si le prix du bien "
           "vendu augmente, le producteur s’enrichit, donc il embauche davantage, investit, "
           "emprunte et consomme plus — ce qui modifie les coûts, les revenus, les demandes "
           "des autres biens, et finit par modifier la demande du bien initial. Choc sur un "
           "marché → effets sur d’autres marchés → retour sur le marché de départ."],
     'lim': "S’y ajoute une incertitude interne au marché lui-même : effet de substitution et "
            "effet de revenu peuvent jouer en sens contraire, si bien que la demande n’est pas "
            "toujours mécaniquement décroissante."},
    {'t': "B. De Say à Walras : l’intuition puis la formalisation",
     'd': ["La filiation que retient le cours est Say → Walras → Arrow-Debreu : c’est "
           "l’histoire de l’optimisme néoclassique sur l’équilibre.",
           "Say pose que produire distribue nécessairement des revenus — salaires, profits, "
           "rentes — qui servent à acheter ce qui est produit : l’offre crée sa propre "
           "demande, il ne peut donc pas y avoir de manque global de débouchés. Dans son "
           "contexte — économie agricole, besoins vitaux, peu de biens inutiles — cela paraît "
           "logique : on ne fabrique pas ce que personne ne veut. Les crises existent, mais "
           "elles sont sectorielles et temporaires, jamais générales.",
           "Walras transforme cette intuition en système. Premièrement, à l’échelle de toute "
           "l’économie, la valeur de l’offre globale égale celle de la demande globale, "
           "puisque les producteurs vendent, paient travail et capital, et que les ménages "
           "utilisent ces revenus pour acheter : comptablement, rien ne fuit du système. "
           "Deuxièmement, chaque marché a son propre équilibre, donc l’économie est un système "
           "d’équations comportant autant d’équations que d’inconnues — tous les prix et "
           "toutes les quantités. Il en conclut qu’un équilibre général simultané existe, et "
           "que l’économie est fondamentalement stable et autorégulée."],
     'lim': "Le point faible est immédiat : avoir autant d’équations que d’inconnues ne "
            "garantit pas qu’une solution existe — deux droites peuvent ne jamais se croiser. "
            "Rien n’assure donc que l’offre et la demande se rencontrent sur chaque marché."},
    {'t': "C. Arrow et Debreu : sept conditions pour que l’équilibre existe",
     'd': ["Arrow et Debreu posent la bonne question : sous quelles conditions les courbes "
           "d’offre et de demande se croisent-elles nécessairement sur tous les marchés en "
           "même temps ? Leur méthode mobilise un théorème mathématique : un système admet une "
           "solution si les fonctions sont continues — pas de saut brutal — et bornées — ni "
           "prix ni quantités infinis. Économiquement : pas de comportements extrêmes, pas de "
           "demandes infinies, pas de marchés qui disparaissent.",
           "Les sept conditions sont les suivantes. La rationalité : les individus maximisent "
           "leur utilité, les entreprises leur profit. La concurrence pure et parfaite, avec "
           "ses cinq attributs — atomicité, homogénéité, transparence, libre entrée et sortie, "
           "mobilité des facteurs — qui garantit que les prix sont donnés et acceptés. Les "
           "marchés complets : il existe un marché pour chaque bien présent et futur, chaque "
           "service, chaque facteur, de sorte qu’on peut échanger aujourd’hui ce qui sera "
           "livré demain. La dotation de survie : chaque agent possède un minimum de "
           "ressources au départ, sans quoi aucun échange n’est possible. La convexité des "
           "courbes d’indifférence, qui garantit qu’il existe toujours une demande pour chaque "
           "bien et qu’aucun marché ne s’effondre. Les rendements d’échelle décroissants, qui "
           "assurent une courbe d’offre croissante, donc une intersection avec la demande. "
           "L’absence de coûts fixes enfin, cruciale pour la continuité des fonctions.",
           "Ce que démontre le théorème doit être énoncé avec précision : il ne dit pas que "
           "l’économie réelle est en équilibre général, mais que si toutes ces conditions sont "
           "réunies, alors un équilibre existe."],
     'lim': "Deux conditions sont particulièrement fragiles, et le cours les souligne. La "
            "dotation de survie suppose une intervention extérieure au marché — État, charité, "
            "institutions — ce qui contredit l’idée que le marché se suffit à lui-même. Et "
            "l’absence de coûts fixes est économiquement absurde : l’industrie, les "
            "infrastructures et le numérique reposent précisément sur d’énormes coûts fixes. "
            "L’intérêt du théorème est donc inverse de celui qu’on lui prête : il montre que "
            "l’équilibre général est une construction théorique fragile."},
    {'t': "D. Pareto : efficacité et non justice",
     'd': ["Une situation est Pareto-optimale lorsqu’il est impossible d’améliorer la "
           "situation d’un agent sans détériorer celle d’un autre. L’équilibre walrassien est "
           "interprété comme un tel optimum.",
           "Mais c’est un critère d’efficacité, pas de justice : il ne dit rien sur l’égalité "
           "ni sur la morale, seulement qu’on ne peut plus améliorer sans coût pour quelqu’un. "
           "Le critère de Hicks-Kaldor élargit le raisonnement : une situation est préférable "
           "si les gagnants pourraient théoriquement compenser les perdants."],
     'lim': "Le mot « théoriquement » est décisif : la compensation est possible en principe, "
            "elle n’est pas réalisée en pratique — c’est l’angle mort normatif du critère, "
            "qu’on retrouvera dans le débat sur les gains du libre-échange."},
    {'t': "E. Sonnenschein, Mantel et Debreu : l’équilibre peut exister sans être atteint",
     'd': ["La question change de nature. Il ne s’agit plus de savoir si l’équilibre existe, "
           "mais si le système y converge et s’il y est stable. L’idée standard était simple : "
           "en cas de déséquilibre les prix s’ajustent et le marché revient automatiquement à "
           "l’équilibre.",
           "Dans les années 1970, Sonnenschein, Mantel et Debreu démontrent mathématiquement "
           "que, même si un équilibre existe, rien ne garantit que le système y arrive, qu’il "
           "y reste, ni qu’il y retourne après un choc. Concrètement, ils prouvent que la "
           "fonction de demande globale peut prendre à peu près n’importe quelle forme — "
           "croissante, chaotique, ne réagissant pas « normalement » aux prix.",
           "La conséquence est radicale : même si chaque agent est rationnel et chaque marché "
           "bien modélisé, l’ensemble du système peut devenir imprévisible. Une microéconomie "
           "rigoureuse ne garantit donc pas une macroéconomie rigoureuse. Steve Keen reprendra "
           "ce résultat pour contester la légitimité du modèle standard."],
     'lim': "La superposition des deux critiques donne l’argument le plus fort du chapitre : "
            "avec Arrow-Debreu, l’équilibre existe mais sous des hypothèses irréalistes ; avec "
            "Sonnenschein-Mantel-Debreu, même s’il existe, rien n’assure qu’on l’atteigne ni "
            "qu’on y reste. L’équilibre est théoriquement possible, pratiquement inaccessible "
            "et mathématiquement instable."},
   ],
   'v': "Si le modèle vacille de l’intérieur, l’observation des comportements réels achève de "
        "le déplacer : qui sont vraiment les agents que ce modèle suppose ?"},

  # ----------------------------------------------------------------- VI
  {'t': "VI. Regard critique : quelle rationalité pour les agents réels ?",
   'sp': [
    {'t': "A. Simon : de la rationalité substantielle à la rationalité limitée",
     'd': ["Herbert Simon — économiste, sociologue, psychologue et informaticien, lauréat du "
           "prix Turing — attaque la rationalité supposée par le modèle standard : information "
           "parfaite, connaissance de tous les prix, de toutes les options et de toutes les "
           "conséquences, préférences claires, maximisation systématique. C’est la rationalité "
           "substantielle.",
           "Il lui oppose trois limites. L’information est limitée : on ne connaît jamais "
           "toutes les options — devant des milliers de formations, aucun élève ne les compare "
           "toutes, il regarde celles de sa région et de son niveau. Les capacités de calcul "
           "sont limitées : même avec toute l’information, le cerveau ne traite pas une "
           "infinité de données. Et les préférences ne sont pas toujours claires : on hésite, "
           "on change d’avis, on décide par habitude ou par imitation.",
           "D’où la rationalité limitée : les individus restent rationnels, mais dans les "
           "limites de leur information, de leur temps et de leurs capacités. Ils ne cherchent "
           "pas le meilleur choix possible mais un choix satisfaisant, et s’arrêtent dès "
           "qu’ils trouvent une solution acceptable — c’est le satisficing, opposé à la "
           "maximisation."],
     'lim': "Le cours situe précisément cette critique : après les conditions irréalistes "
            "d’Arrow-Debreu, l’efficacité sans justice de Pareto et l’absence de stabilité, "
            "Simon ajoute que même si les conditions mathématiques étaient remplies, les "
            "agents réels seraient incapables de se comporter comme le modèle l’exige."},
    {'t': "B. Akerlof : l’asymétrie d’information est la règle, pas l’exception",
     'd': ["La concurrence pure et parfaite suppose une information parfaite, gratuite et "
           "symétrique. Or c’est l’inverse qui domine : un agent sait ce que l’autre ignore, "
           "et cette information influence l’échange — c’est la situation normale des marchés.",
           "Akerlof le démontre en 1970 dans The Market for Lemons. Sur le marché des voitures "
           "d’occasion, le vendeur connaît la qualité de son véhicule, pas l’acheteur. "
           "Celui-ci propose donc un prix moyen, trop bas pour les bonnes voitures, dont les "
           "vendeurs quittent le marché ; il ne reste que les mauvaises, la qualité moyenne "
           "baisse, la confiance disparaît et le marché peut s’effondrer. L’asymétrie "
           "d’information peut donc détruire un marché.",
           "Le cours multiplie les exemples : acheter un appartement sans connaître les "
           "nuisances réelles ; le marché du travail, où l’employeur ignore la motivation réelle "
           "du candidat et le salarié la charge et la pression futures — asymétrie "
           "bilatérale ; et les produits de consommation, où trop d’information rend "
           "l’information inutilisable, de sorte que transparence ne vaut pas compréhension.",
           "Simon et Akerlof sont complémentaires : Simon décrit une limite cognitive, Akerlof "
           "une asymétrie stratégique. L’exemple des CDO l’illustre : l’information existait, "
           "sur cent ou deux cents pages, mais personne ne la lisait vraiment, parce que "
           "c’était trop long, trop technique et trop coûteux en temps."],
     'lim': "La formule à retenir est celle du cours : la transparence de l’information est "
            "une hypothèse théorique, l’asymétrie d’information est une réalité économique — "
            "et le problème n’est pas seulement qu’on ne nous donne pas l’information, mais "
            "qu’on ne la traite pas."},
    {'t': "C. Kahneman et Thaler : biais cognitifs et architecture des choix",
     'd': ["Kahneman (Système 1 / Système 2 : les deux vitesses de la pensée, 2011) montre que "
           "le cerveau fonctionne selon deux systèmes. Le Système 1 est rapide, intuitif, "
           "automatique, émotionnel — et fait des erreurs. Le Système 2 est lent, réfléchi, "
           "rationnel, calculateur — mais coûteux. La plupart du temps nous utilisons le "
           "Système 1, même quand nous pourrions raisonner : la rationalité parfaite n’est "
           "pas humaine.",
           "Un biais cognitif est une erreur systématique de jugement qui éloigne de la "
           "décision rationnelle au sens de la théorie standard. Le biais de confirmation "
           "consiste à ne retenir que les informations qui confirment ce que l’on croit déjà — "
           "après un accident d’avion, on remarque surtout les accidents aériens, en oubliant "
           "que la voiture est statistiquement plus dangereuse. Le biais d’ancrage (Prelec, "
           "2003) montre qu’un chiffre initial, même arbitraire, influence les décisions "
           "suivantes : dans l’expérience citée, le prix que les individus acceptent de payer "
           "pour une bouteille de vin se rapproche des deux derniers chiffres de leur numéro "
           "de sécurité sociale.",
           "Thaler en tire une conséquence pratique : nos préférences ne sont pas fixes, elles "
           "dépendent de la façon dont le choix est formulé. C’est le principe du nudge — "
           "influencer sans interdire ni obliger, en modifiant la présentation des options. "
           "L’exemple canonique est le don d’organes : une case déjà cochée produit beaucoup "
           "plus de donneurs qu’une case à cocher."],
     'lim': "Le cours refuse la conclusion radicale : ces biais ne détruisent pas la théorie "
            "économique, ils l’enrichissent en la rendant plus réaliste. Ce n’est pas la "
            "rationalité qui change, c’est la formulation qui guide le choix."},
    {'t': "D. Économie expérimentale, théorie des jeux et croyances collectives",
     'd': ["L’économie expérimentale place des individus réels dans des situations "
           "contrôlées — marché, négociation, coopération ou conflit — et compare leurs "
           "décisions aux prédictions de l’homo œconomicus. Le résultat est net : on observe "
           "de l’altruisme, une recherche d’équité, une volonté de punir les comportements "
           "jugés injustes et des comportements coopératifs. L’homo œconomicus est une "
           "abstraction utile mais insuffisante.",
           "La théorie des jeux étudie les situations où le résultat de chacun dépend des "
           "choix des autres. Le dilemme du prisonnier en est l’exemple fondamental : chacun a "
           "intérêt individuellement à trahir, mais si les deux trahissent le résultat est "
           "pire que s’ils avaient coopéré. La conclusion centrale est que la rationalité "
           "individuelle ne conduit pas nécessairement à la rationalité collective — sans "
           "coopération, la décision collective est sous-optimale.",
           "Cette logique se retrouve en oligopole : peu de producteurs, chacun dépendant des "
           "décisions des autres. Deux issues sont possibles — la concurrence, avec guerre des "
           "prix et profits faibles, ou la collusion, avec prix élevés et profits importants. "
           "Mais chaque entreprise a individuellement intérêt à tricher : l’entente est donc "
           "instable.",
           "Enfin, les croyances agissent directement sur le réel. Une prophétie "
           "autoréalisatrice, au sens de Merton, est une croyance qui provoque les "
           "comportements qui la rendent vraie : on croit qu’une banque va faire faillite, les "
           "déposants retirent massivement leur argent, et la banque fait effectivement "
           "faillite."],
     'lim': "Ce résultat atteint le cœur de l’argument néoclassique : la somme des "
            "comportements rationnels individuels ne conduit pas automatiquement à une "
            "situation optimale pour la société — ce qui ouvre directement sur les "
            "défaillances de marché."},
   ],
   'v': "Dès qu’une condition de la concurrence pure et parfaite est violée, des défaillances "
        "apparaissent et l’intervention publique redevient une question : c’est l’objet du "
        "chapitre suivant."},
 ],

 'ae': [
  {'n': "Hermann Gossen", 'k': 'a',
   'i': "L’utilité marginale décroissante : l’utilité totale augmente mais de moins en moins "
        "vite, d’où une courbe croissante et concave."},
  {'n': "Alfred Marshall", 'k': 'a',
   'i': "L’équilibre partiel et le raisonnement ceteris paribus : un outil de simplification, "
        "pas une description du réel."},
  {'n': "Jean-Baptiste Say", 'k': 'a',
   'i': "L’offre crée sa propre demande : l’intuition que Walras formalisera, et qui fonde "
        "l’optimisme néoclassique sur l’équilibre."},
  {'n': "Léon Walras", 'k': 'a',
   'i': "L’économie comme système d’équations : autant d’équations que d’inconnues, donc un "
        "équilibre général simultané — mais rien ne garantit que les courbes se croisent."},
  {'n': "Kenneth Arrow et Gérard Debreu", 'k': 'a',
   'i': "Sept conditions pour l’existence de l’équilibre — dont la dotation de survie et "
        "l’absence de coûts fixes, les deux plus fragiles."},
  {'n': "Vilfredo Pareto", 'k': 'a',
   'i': "L’optimum : on ne peut améliorer la situation d’un agent sans détériorer celle d’un "
        "autre — un critère d’efficacité, pas de justice."},
  {'n': "Sonnenschein, Mantel et Debreu (années 1970)", 'k': 'a',
   'i': "La demande agrégée peut prendre n’importe quelle forme : l’existence de l’équilibre "
        "n’entraîne ni sa stabilité ni la convergence vers lui."},
  {'n': "Steve Keen, L’imposture économique (2014)", 'k': 'a',
   'i': "Reprend Sonnenschein pour contester le modèle standard, et objecte que la courbe de "
        "coût en U ne décrit plus l’économie numérique."},
  {'n': "Herbert Simon", 'k': 'a',
   'i': "Rationalité limitée : information, temps et capacités de calcul bornés — on "
        "« satisfait » au lieu de maximiser."},
  {'n': "George Akerlof, The Market for Lemons (1970)", 'k': 'a',
   'i': "L’asymétrie d’information est la règle : la qualité invisible chasse les bons "
        "produits et peut détruire le marché."},
  {'n': "Daniel Kahneman (2011)", 'k': 'a',
   'i': "Système 1 rapide et intuitif contre Système 2 lent et coûteux : les biais cognitifs "
        "sont la règle, non l’exception."},
  {'n': "Richard Thaler", 'k': 'a',
   'i': "Le nudge : les préférences ne sont pas fixes, la formulation du choix oriente le "
        "comportement sans interdire ni obliger."},
  {'n': "Robert Merton", 'k': 'a',
   'i': "La prophétie autoréalisatrice : une croyance collective produit les comportements qui "
        "la rendent vraie."},
  {'n': "Kate Raworth", 'k': 'a',
   'i': "Conteste l’hypothèse de non-satiété : pourquoi supposer qu’on veut toujours consommer "
        "davantage ?"},
  {'n': "La manufacture d’épingles et les rendements d’échelle croissants", 'k': 'e',
   'i': "Le lien explicite avec Smith : la spécialisation et une meilleure organisation "
        "expliquent qu’on produise plus que proportionnellement."},
  {'n': "Le choc pétrolier (5 $, 15 $ en 1973, 30 $ en 1979)", 'k': 'e',
   'i': "La démonstration empirique que l’élasticité est faible à court terme et plus forte à "
        "long terme, le temps que des substituts apparaissent."},
  {'n': "Le skyr d’une marque, les yaourts, les produits laitiers", 'k': 'e',
   'i': "Plus la catégorie est précise, plus la demande est élastique : une élasticité ne se "
        "cite jamais sans son périmètre."},
  {'n': "Les caisses automatiques et la hausse des cotisations", 'k': 'e',
   'i': "Un renchérissement du travail déclenche un effet de substitution vers le capital : le "
        "TMST en application directe."},
  {'n': "Les médicaments vendus par boîtes", 'k': 'e',
   'i': "Le conflit entre l’hypothèse de continuité et des biens indivisibles : gaspillage, "
        "surconsommation et coût pour la Sécurité sociale."},
  {'n': "Le don d’organes par défaut", 'k': 'e',
   'i': "Une case déjà cochée change massivement le comportement : la preuve empirique du "
        "nudge."},
  {'n': "Les CDO de 2008", 'k': 'e',
   'i': "L’information existait sur des centaines de pages mais n’était pas traitée : "
        "transparence ne vaut pas compréhension."},
 ],

 'arg': [
  "Les hypothèses du modèle ne sont pas des descriptions mais des conditions de solvabilité "
  "mathématique : la continuité et la non-satiété existent pour qu’on puisse dériver et "
  "optimiser, pas parce qu’elles seraient réalistes.",
  "L’équilibre du consommateur se cite précisément — TMS = −Px/Py — et celui du producteur de "
  "même — TMST = −PmL/PmK : ce parallélisme est la structure du chapitre.",
  "Une variation de prix se décompose toujours en effet de substitution et effet de revenu ; "
  "c’est parce qu’ils peuvent jouer en sens contraire que la demande n’est pas mécaniquement "
  "décroissante.",
  "Seuil de rentabilité (P = CM) et seuil de fermeture (P = CVM) ne se confondent pas : c’est "
  "ce qui explique qu’une entreprise continue de produire à perte à court terme.",
  "Critiquer l’équilibre général par son irréalisme est faible ; le critiquer par "
  "Sonnenschein-Mantel-Debreu est fort, car la critique est interne au cadre lui-même.",
  "Giffen et Veblen ne sont pas des curiosités : ils montrent que la loi de la demande dépend "
  "du contexte social — la pauvreté dans un cas, la distinction dans l’autre.",
  "L’économie comportementale ne détruit pas le modèle standard, elle en déplace la frontière "
  "de validité : c’est la nuance que le cours formule lui-même.",
 ],

 'deb': [
  "L’homo œconomicus est-il une hypothèse de travail utile ou une description fausse qui "
  "fausse les conclusions ? Simon, Akerlof et Kahneman contre le modèle standard.",
  "Le marché conduit-il à un optimum ? Optimum de Pareto et critère de Hicks-Kaldor : "
  "efficacité contre justice, et compensation théorique contre compensation réelle.",
  "La rationalité individuelle produit-elle la rationalité collective ? Le dilemme du "
  "prisonnier et l’instabilité des ententes montrent que non.",
  "Le nudge est-il une politique publique respectueuse de la liberté ou une manipulation de "
  "l’architecture des choix ?",
  "La courbe de coût en U décrit-elle encore l’économie contemporaine, où la duplication "
  "numérique a un coût marginal quasi nul (Keen) ?",
 ],

 'lien': [
  {'c': 3, 'p': "Ce chapitre est la mise en équations du courant néoclassique issu de la "
                "révolution marginaliste : Walras, Marshall, Menger y sont présentés, ici "
                "formalisés."},
  {'c': 5, 'p': "Les cinq conditions de la CPP servent de grille aux quatre défaillances de "
                "marché : chaque défaillance est la violation d’une condition, et Akerlof "
                "comme Pigou y sont développés."},
  {'c': 9, 'p': "L’abandon de l’atomicité et de l’homogénéité ouvre l’analyse de la "
                "concurrence imparfaite : oligopole, collusion, différenciation, "
                "contestabilité."},
  {'c': 10, 'p': "La rationalité limitée de Simon irrigue la sociologie des organisations, les "
                 "décisions absurdes de Morel et l’analyse stratégique de Crozier."},
  {'c': 1, 'p': "Élasticité-revenu et loi d’Engel éclairent la structure de la consommation "
                "des ménages et la part croissante des dépenses pré-engagées."},
  {'c': 2, 'p': "Les prophéties autoréalisatrices de Merton expliquent les paniques bancaires "
                "et le rôle de la confiance dans le système monétaire."},
 ],

 'min': [
  "Quatre hypothèses sur les préférences : complétude, transitivité, non-satiété, continuité "
  "— faites pour la solvabilité mathématique, pas pour le réalisme.",
  "Loi de Gossen : utilité marginale décroissante ; TMS = dY/dX < 0 ; équilibre du "
  "consommateur : TMS = −Px/Py.",
  "Toute variation de prix = effet de substitution + effet de revenu.",
  "Élasticité-prix |e| > 1 ou < 1 ; élasticité-revenu e < 0, 0 < e < 1, e > 1 ; croisée "
  "négative (complémentaires) ou positive (substituables). Giffen ≠ Veblen.",
  "Court terme = au moins un facteur fixe (définition logique, non chronologique) ; Pm coupe "
  "PM en son maximum.",
  "Isoquante + isocoût → tangence ; TMST = −ΔK/ΔL = −PmL/PmK.",
  "CT = CF + CV ; CM = CFM + CVM ; Cm coupe CM et CVM en leur minimum ; Pm ↑ → Cm ↓.",
  "Rentabilité : P ≥ CM ; poursuite à court terme : P ≥ CVM ; producteur preneur de prix en "
  "CPP.",
  "Say → Walras → Arrow-Debreu (7 conditions, dont dotation de survie et absence de coûts "
  "fixes) ; Pareto : efficacité sans justice.",
  "Sonnenschein-Mantel-Debreu : l’équilibre peut exister sans être stable ni atteint.",
  "Simon (rationalité limitée, satisficing), Akerlof (lemons, 1970), Kahneman (Systèmes 1 et "
  "2), Thaler (nudge), Merton (prophétie autoréalisatrice).",
 ],
}}
