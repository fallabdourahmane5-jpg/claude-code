# -*- coding: utf-8 -*-
"""Ensemble 7 — La consommation, l’épargne et les comportements économiques
(2/3)."""

from doss_base import d

d('n7-choix', 7, "Choix du consommateur",
  "Égaliser le renoncement subjectif et le taux d’échange du marché",
  "Le choix du consommateur résulte de la confrontation entre ses "
  "préférences, représentées par les courbes d’indifférence, et sa contrainte "
  "budgétaire. Le taux marginal de substitution, pente en un point de la "
  "courbe d’indifférence, mesure le nombre d’unités du bien Y auxquelles "
  "l’individu doit renoncer pour obtenir une unité supplémentaire du bien X "
  "tout en restant sur la même courbe.",
  "Le modèle du choix du consommateur est la pièce centrale de la "
  "microéconomie, et le cours en expose le ressort avec netteté : l’idée de "
  "base est l’arbitrage. Le consommateur ne peut pas tout avoir ; s’il "
  "consomme plus du bien X, il doit nécessairement renoncer à une partie du "
  "bien Y, et cet arbitrage est au cœur de la microéconomie. Pour le mesurer, "
  "les microéconomistes ont introduit le taux marginal de substitution, défini "
  "comme la pente en un point de la courbe d’indifférence : il mesure le "
  "nombre d’unités du bien Y auxquelles un individu doit renoncer pour "
  "obtenir une unité supplémentaire du bien X, tout en restant sur la même "
  "courbe d’indifférence — autrement dit, on reste au même niveau de "
  "satisfaction et l’on échange un bien contre l’autre. Le cours précise "
  "pourquoi ce taux est négatif : les courbes d’indifférence sont "
  "décroissantes et convexes, consommer plus de X impliquant de consommer "
  "moins de Y, de sorte que le signe négatif traduit le renoncement. Il donne "
  "un exemple numérique : pour passer de 1 à 3 unités de X, l’individu doit "
  "renoncer à 3 unités de Y en restant sur la même courbe. L’optimum s’obtient "
  "alors par la rencontre des deux logiques : le taux marginal de "
  "substitution exprime ce que l’individu est prêt à céder, la pente de la "
  "droite de budget ce que le marché exige. Tant que les deux diffèrent, il "
  "reste un gain à réaliser en modifiant le panier ; l’optimum est atteint "
  "lorsqu’ils coïncident. Mais le cours ne cache pas la fragilité de cette "
  "construction : les hypothèses de transitivité, de continuité et de "
  "non-satiété sont posées pour des raisons mathématiques, et l’économie "
  "comportementale montre que les agents réels utilisent des raccourcis "
  "mentaux et commettent des erreurs systématiques.",
  [("L’arbitrage comme point de départ",
    "Le consommateur ne peut pas tout avoir : toute unité supplémentaire d’un "
    "bien se paie d’un renoncement sur l’autre, ce qui fait de la décision un "
    "problème d’échange plutôt que de niveau."),
   ("La mesure du renoncement par le taux marginal de substitution",
    "Le TMS indique combien d’unités de Y il faut abandonner pour consommer "
    "une unité de plus de X en restant au même niveau de satisfaction : c’est "
    "le prix subjectif de X en unités de Y."),
   ("La décroissance et la convexité des courbes",
    "Les courbes d’indifférence sont décroissantes et convexes : plus on "
    "dispose de X, moins on accepte d’abandonner de Y pour en obtenir encore, "
    "ce qui traduit le goût pour la diversité."),
   ("La comparaison des deux taux",
    "Le TMS exprime le taux d’échange subjectif, la pente de la droite de "
    "budget le taux d’échange marchand : leur écart indique dans quel sens "
    "modifier le panier pour gagner en satisfaction."),
   ("La condition d’optimum",
    "Tant que les deux taux diffèrent, un réaménagement du panier améliore la "
    "situation : l’optimum est atteint lorsqu’ils coïncident, c’est-à-dire au "
    "point de tangence entre la droite de budget et la courbe d’indifférence "
    "la plus élevée accessible.")],
  [{'a': "Le modèle ramène une décision complexe à une comparaison entre deux "
         "taux, l’un subjectif et l’autre objectif.",
    'cond': "La comparaison suppose des préférences continues et convexes, "
            "sans quoi aucun point de tangence n’existe.",
    'lim': "Le cours reconnaît que ces hypothèses sont faites pour résoudre "
           "des problèmes mathématiques et non pour décrire parfaitement les "
           "comportements réels."},
   {'a': "Il rend l’arbitrage explicite et mesurable, ce qui permet de prévoir "
         "la réaction du consommateur à une variation de prix ou de revenu.",
    'cond': "La prévision suppose que les préférences de l’individu restent "
            "inchangées pendant la variation étudiée.",
    'lim': "Thaler montre que les préférences ne sont pas fixes et dépendent "
           "de la manière dont on formule un choix, ce qui fragilise la "
           "stabilité supposée."},
   {'a': "Il fournit un fondement microéconomique à la courbe de demande, "
         "obtenue en faisant varier le prix et en relevant les optima "
         "successifs.",
    'cond': "L’agrégation en demande de marché suppose que l’on puisse "
            "sommer les demandes individuelles.",
    'lim': "Sonnenschein, Mantel et Debreu montrent qu’une fonction de demande "
           "globale peut avoir n’importe quelle forme, ce qui interdit "
           "l’agrégation naïve."},
   {'a': "Il s’applique bien au-delà de la consommation, à tout arbitrage "
         "entre deux usages concurrents d’une ressource rare.",
    'cond': "La généralisation suppose que les deux termes de l’arbitrage "
            "soient substituables au moins partiellement.",
    'lim': "Elle échoue pour des éléments non substituables, ce que la "
           "soutenabilité forte objecte précisément à propos du capital "
           "naturel."}],
  [{'t': "Les individus ne classent pas leurs préférences de façon cohérente, "
         "contrairement à ce que suppose le modèle.",
    'qui': "Steve Keen, dans L’imposture économique (2014).",
    'rep': "L’objection vise l’hypothèse de transitivité, et le cours "
           "reconnaît que d’après les vérifications empiriques les gens ne "
           "sont pas transitifs dans leurs choix."},
   {'t': "Les agents ne disposent pas des capacités de calcul et "
         "d’information que l’optimisation exige d’eux.",
    'qui': "Herbert Simon, avec la rationalité limitée.",
    'rep': "Le cours formule la conséquence : les individus ne maximisent pas "
           "leurs choix mais recherchent des solutions satisfaisantes plutôt "
           "qu’optimales."},
   {'t': "Les choix dépendent de la façon dont les options sont présentées, "
         "et non seulement des préférences.",
    'qui': "Richard Thaler, avec le nudge.",
    'rep': "L’objection est décisive : ce n’est pas la rationalité qui change, "
           "c’est la formulation qui guide le choix, comme le montre l’effet "
           "d’une case précochée sur le don d’organes."},
   {'t': "Les choix sont influencés par des références arbitraires sans "
         "rapport avec l’objet du choix.",
    'qui': "Daniel Kahneman, avec l’effet d’ancrage.",
    'rep': "L’expérience du cours est probante : interrogés après avoir donné "
           "leurs deux derniers chiffres de sécurité sociale, les participants "
           "proposent pour une bouteille de vin un prix proche de ce numéro."}],
  [{'n': "Herbert Simon",
    'i': "Les individus ne maximisent pas leurs choix mais recherchent des "
         "solutions satisfaisantes plutôt qu’optimales.",
    'p': "Le cours présente sa rationalité limitée comme le coup de grâce "
         "porté au modèle : même si les conditions mathématiques étaient "
         "remplies, les agents réels ne seraient pas capables de se comporter "
         "comme le modèle l’exige."},
   {'n': "Daniel Kahneman",
    'i': "Le comportement repose sur deux systèmes de pensée, l’un rapide et "
         "intuitif, l’autre lent et réfléchi.",
    'p': "Le cours précise que dans la plupart des situations les individus "
         "utilisent le système 1, ce qui conduit à des biais cognitifs, "
         "c’est-à-dire des erreurs de jugement qui éloignent de la "
         "rationalité au sens de la théorie standard."},
   {'n': "Richard Thaler",
    'i': "Nos préférences ne sont pas fixes : elles dépendent de la manière "
         "dont on formule un choix.",
    'p': "C’est le principe du nudge : on influence les comportements sans "
         "interdire ni obliger, simplement en modifiant la présentation des "
         "options, comme le montre l’exemple du don d’organes selon que la "
         "case est précochée ou non."},
   {'n': "Steve Keen",
    'i': "Les comportements observés contredisent l’hypothèse de transitivité "
         "des préférences.",
    'p': "Le cours le cite pour L’imposture économique (2014) et le présente "
         "comme très critique à l’égard de l’approche microéconomique, son "
         "objection portant sur l’hypothèse sans laquelle aucun classement "
         "stable des paniers n’est possible."}],
  [{'f': "Le taux marginal de substitution est défini comme la pente en un "
         "point de la courbe d’indifférence d’un consommateur.",
    'p': "La définition géométrique permet de relier immédiatement "
         "l’arbitrage subjectif à la représentation graphique utilisée en "
         "exercice."},
   {'f': "Le TMS est négatif parce que les courbes d’indifférence sont "
         "décroissantes et convexes, le signe négatif traduisant le "
         "renoncement.",
    'p': "La précision évite une erreur fréquente et montre que le signe n’est "
         "pas une convention mais la traduction du caractère inévitable de "
         "l’arbitrage."},
   {'f': "Le cours donne un exemple chiffré : pour passer de 1 à 3 unités de "
         "X, l’individu doit renoncer à 3 unités de Y en restant sur la même "
         "courbe d’indifférence.",
    'p': "L’exemple rend concret le calcul du TMS et montre qu’il se lit comme "
         "un rapport de variations entre deux points d’une même courbe."},
   {'f': "L’économie comportementale montre que les agents utilisent des "
         "raccourcis mentaux et commettent des erreurs systématiques appelées "
         "biais cognitifs.",
    'p': "Le fait situe la critique du modèle non dans ses hypothèses "
         "mathématiques mais dans la psychologie effective des décideurs."}],
  [{'q': "Sujet du type « Le consommateur est-il rationnel ? »",
    'f': "Le modèle standard le suppose capable d’ordonner ses préférences et "
         "d’optimiser sous contrainte, en égalisant son taux marginal de "
         "substitution au rapport des prix. L’économie comportementale "
         "conteste cette description : Kahneman montre que le comportement "
         "repose sur un système 1 rapide, intuitif et émotionnel, et un "
         "système 2 lent et réfléchi, et que dans la plupart des situations "
         "les individus utilisent le système 1, ce qui conduit à des biais "
         "cognitifs.",
    'r': "Le raisonnement montre que la critique ne porte pas sur les "
         "capacités de calcul mais sur le mode de pensée effectivement "
         "mobilisé, ce qui est une objection plus profonde que celle de la "
         "complexité.",
    'ex': "L’effet d’ancrage, où le prix proposé pour une bouteille de vin est "
          "influencé par un numéro de sécurité sociale sans aucun rapport."},
   {'q': "Sujet du type « Comment se mesure l’arbitrage économique ? »",
    'f': "Le taux marginal de substitution en fournit la mesure exacte : il "
         "indique le nombre d’unités du bien Y auxquelles un individu doit "
         "renoncer pour obtenir une unité supplémentaire du bien X, tout en "
         "restant sur la même courbe d’indifférence. On reste donc au même "
         "niveau de satisfaction et l’on échange simplement un bien contre "
         "l’autre, ce qui isole le renoncement pur de tout gain ou perte de "
         "bien-être.",
    'r': "Le raisonnement montre que l’arbitrage se mesure à satisfaction "
         "constante, ce qui permet de le comparer au taux d’échange du marché "
         "et d’en déduire la direction de l’ajustement optimal.",
    'ex': "Le passage de 1 à 3 unités de X contre l’abandon de 3 unités de Y "
          "sur une même courbe d’indifférence."}],
  voisins=['n7-utilite', 'n7-contrainte-budgetaire', 'n7-rationalite-limitee',
           'n7-biais'])


d('n7-effet-revenu-substitution', 7,
  "Effet revenu et effet substitution",
  "Une variation de prix agit par deux canaux qu’il faut séparer",
  "Une variation du prix d’un bien produit deux effets simultanés. L’effet de "
  "substitution traduit le changement de consommation entre les deux biens : "
  "on substitue un bien à l’autre, la consommation de X augmente et celle de Y "
  "diminue. L’effet de revenu traduit le fait que la baisse du prix donne "
  "l’impression que le revenu réel augmente, à revenu nominal inchangé, ce qui "
  "permet de consommer plus des deux biens.",
  "La décomposition en effet de substitution et effet de revenu est l’exercice "
  "le plus exigeant du chapitre, et le cours en donne les deux lectures, "
  "graphique et économique. Du côté de l’effet de substitution : la baisse du "
  "prix de X entraîne un changement de consommation entre les deux biens, "
  "puisqu’on substitue un bien à l’autre, la consommation de X augmentant et "
  "celle de Y diminuant. Graphiquement, on reste sur la même courbe "
  "d’indifférence, mais on se déplace le long de cette courbe vers un point "
  "situé plus bas, puisque X augmente et Y diminue. Sur la droite budgétaire, "
  "la baisse du prix de X modifie le coefficient directeur pour un revenu "
  "considéré comme stable : la pente, égale à l’opposé du rapport du prix de X "
  "sur celui de Y, devient plus faible. Du côté de l’effet de revenu : la "
  "baisse du prix donne l’impression que le revenu réel augmente alors que le "
  "revenu nominal est inchangé, de sorte qu’on peut consommer plus de X et "
  "plus de Y. Graphiquement, l’individu se déplace vers une courbe "
  "d’indifférence plus élevée puisque son revenu a augmenté, et la nouvelle "
  "droite de budget a la même pente que la précédente — elle lui est "
  "parallèle — mais se situe à sa droite. Le cours résume la difficulté par "
  "une question : dans les deux cas la consommation de burger augmente, mais "
  "la question est de savoir pourquoi. C’est exactement l’enjeu de la "
  "décomposition : distinguer ce qui relève du changement de prix relatif de "
  "ce qui relève du gain de pouvoir d’achat. La distinction prend toute sa "
  "portée avec les cas atypiques : pour un bien inférieur, les deux effets "
  "jouent en sens contraire, et le bien de Giffen est le cas extrême où "
  "l’effet de revenu l’emporte, la consommation augmentant lorsque le prix "
  "augmente.",
  [("La modification du prix relatif",
    "Une baisse du prix de X rend ce bien moins cher relativement à Y : "
    "l’arbitrage se déplace en faveur de X, indépendamment de tout gain de "
    "pouvoir d’achat."),
   ("Le déplacement le long de la courbe d’indifférence",
    "Pour isoler l’effet de substitution, on reste sur la même courbe "
    "d’indifférence et l’on se déplace vers un point situé plus bas, puisque X "
    "augmente et Y diminue : la satisfaction est maintenue constante."),
   ("La rotation de la droite de budget",
    "La baisse du prix de X modifie le coefficient directeur de la droite pour "
    "un revenu stable : la pente devient plus faible, ce qui traduit le "
    "nouveau taux d’échange offert par le marché."),
   ("Le gain de pouvoir d’achat réel",
    "La baisse de prix donne l’impression que le revenu réel augmente alors "
    "que le revenu nominal est inchangé : on peut consommer plus de X et plus "
    "de Y, ce qui est un effet de niveau et non de structure."),
   ("La translation vers une courbe supérieure",
    "L’effet de revenu déplace l’individu vers une courbe d’indifférence plus "
    "élevée, la nouvelle droite de budget étant parallèle à la précédente mais "
    "située à sa droite.")],
  [{'a': "La décomposition explique pourquoi deux causes différentes "
         "produisent la même observation, une hausse de la consommation de X.",
    'cond': "La séparation suppose que l’on puisse isoler analytiquement la "
            "variation à satisfaction constante, ce que la courbe "
            "d’indifférence permet.",
    'lim': "Cette séparation est une construction théorique : dans "
           "l’observation, seul l’effet total est mesurable."},
   {'a': "Elle fournit le fondement de la loi de la demande, puisque l’effet "
         "de substitution joue toujours dans le même sens.",
    'cond': "La conclusion suppose que l’effet de revenu ne contrarie pas "
            "l’effet de substitution, ce qui vaut pour les biens normaux.",
    'lim': "Pour un bien inférieur, les deux effets s’opposent, et le bien de "
           "Giffen est le cas où l’effet de revenu l’emporte, la consommation "
           "augmentant quand le prix augmente."},
   {'a': "Elle permet d’évaluer l’effet d’une politique de prix sur le "
         "bien-être et sur la structure de consommation séparément.",
    'cond': "L’évaluation suppose de connaître l’élasticité-revenu du bien "
            "concerné, qui détermine l’ampleur du second effet.",
    'lim': "Ces élasticités varient fortement selon les biens et les niveaux "
           "de revenu, ce qui rend l’évaluation sensible à la catégorie de "
           "ménages considérée."},
   {'a': "Elle éclaire les effets distributifs d’une variation de prix, "
         "puisque le gain de pouvoir d’achat est proportionnellement plus "
         "important pour les bas revenus.",
    'cond': "L’argument suppose que le bien concerné occupe une part "
            "importante du budget des ménages modestes.",
    'lim': "Il ne vaut pas pour les biens dont la consommation est "
           "concentrée sur les hauts revenus, où l’effet de revenu est "
           "négligeable."}],
  [{'t': "La distinction entre les deux effets est purement théorique, "
         "puisque seul l’effet total est observable.",
    'qui': "La critique empiriste des décompositions microéconomiques.",
    'rep': "L’objection est juste mais la décomposition reste utile : elle "
           "seule permet de prévoir le sens de la réaction lorsque les deux "
           "effets s’opposent, comme pour un bien inférieur."},
   {'t': "La loi de la demande est démentie par l’existence de biens dont la "
         "consommation augmente avec le prix.",
    'qui': "Les cas du bien de Giffen et du bien de Veblen que le cours "
           "distingue soigneusement.",
    'rep': "Les deux cas ne relèvent pas du même mécanisme : le bien de Giffen "
           "est un bien inférieur consommé par contrainte en contexte de "
           "pauvreté extrême, le bien de Veblen un bien de luxe consommé par "
           "affichage social."},
   {'t': "Le raisonnement toutes choses égales par ailleurs ignore que la "
         "variation d’un prix se propage aux autres marchés.",
    'qui': "La critique de l’équilibre partiel que le cours formule.",
    'rep': "La démarche reste une simplification scientifique légitime — on "
           "met un marché au microscope — mais le cours rappelle que les biens "
           "sont liés, substituts ou compléments, et que les revenus changent."},
   {'t': "Les consommateurs ne réagissent pas aux prix relatifs mais à des "
         "références arbitraires.",
    'qui': "Daniel Kahneman, avec l’effet d’ancrage.",
    'rep': "L’objection limite la portée du mécanisme sans l’annuler : elle "
           "montre que le niveau du prix de référence est manipulable, non que "
           "la substitution n’opère pas."}],
  [{'n': "Thorstein Veblen",
    'i': "Certains biens voient leur demande augmenter avec leur prix, par "
         "affichage social.",
    'p': "Le cours distingue soigneusement le bien de Veblen, bien supérieur "
         "de luxe consommé dans un contexte de richesse pour sa valeur de "
         "signe, du bien de Giffen, bien inférieur consommé par contrainte en "
         "situation de pauvreté extrême."},
   {'n': "Ernst Engel",
    'i': "Quand le revenu augmente, la structure de la consommation change.",
    'p': "Le cours précise que sa loi est exactement une question "
         "d’élasticité-revenu, même si elle n’avait pas été nommée ainsi à "
         "l’époque : les ménages riches dépensent proportionnellement moins "
         "dans certains biens, comme l’alimentation, et compensent par "
         "d’autres postes."},
   {'n': "Daniel Kahneman",
    'i': "Les décisions de prix sont influencées par des références "
         "arbitraires.",
    'p': "L’expérience de l’ancrage que rapporte le cours montre que le prix "
         "proposé pour une bouteille de vin est souvent proche du numéro de "
         "sécurité sociale des participants, ce qui contredit l’idée d’une "
         "réaction purement objective aux prix relatifs."}],
  [{'f': "Le cours décrit l’effet de substitution ainsi : la baisse du prix de "
         "X entraîne un changement de consommation entre les deux biens, on "
         "substitue un bien à l’autre, la consommation de X augmente et celle "
         "de Y diminue.",
    'p': "La formulation isole le mécanisme sans faire intervenir le pouvoir "
         "d’achat, ce qui est exactement ce que la décomposition cherche à "
         "obtenir."},
   {'f': "Pour l’effet de substitution, on reste sur la même courbe "
         "d’indifférence et l’on se déplace vers un point situé plus bas, "
         "puisque X augmente et Y diminue.",
    'p': "La lecture graphique est le critère de reconnaissance de l’effet : "
         "rester sur la courbe signifie que la satisfaction est inchangée."},
   {'f': "Pour l’effet de revenu, la nouvelle droite de budget a la même pente "
         "que la précédente, lui est parallèle, mais se situe à sa droite.",
    'p': "Le parallélisme est le critère graphique de l’effet de revenu, à "
         "opposer à la rotation qui caractérise l’effet de substitution."},
   {'f': "Le cours résume la difficulté par une question : dans les deux cas "
         "la consommation de burger augmente, mais la question est de savoir "
         "pourquoi.",
    'p': "La formulation montre l’enjeu exact de la décomposition : expliquer "
         "une observation unique par deux causes distinctes."}],
  [{'q': "Sujet du type « Comment les consommateurs réagissent-ils à une "
         "variation de prix ? »",
    'f': "Par deux canaux simultanés qu’il faut séparer. L’effet de "
         "substitution d’abord : la baisse du prix de X entraîne un changement "
         "de consommation entre les deux biens, on substitue un bien à "
         "l’autre, la consommation de X augmente et celle de Y diminue. "
         "L’effet de revenu ensuite : la baisse de prix donne l’impression que "
         "le revenu réel augmente alors que le revenu nominal est inchangé, de "
         "sorte qu’on peut consommer plus de X et plus de Y.",
    'r': "Le raisonnement explique une même observation par deux causes de "
         "nature différente, l’une portant sur les prix relatifs et l’autre "
         "sur le pouvoir d’achat, ce qui permet de prévoir les cas où elles "
         "s’opposent.",
    'ex': "Le bien de Giffen, bien inférieur en contexte de pauvreté extrême, "
          "dont la consommation augmente quand le prix augmente, par "
          "contrainte."},
   {'q': "Sujet du type « La demande décroît-elle toujours avec le prix ? »",
    'f': "Deux exceptions sont à distinguer, que le cours met en garde de ne "
         "pas confondre. Le bien de Giffen apparaît dans un contexte de "
         "pauvreté extrême : c’est un bien inférieur dont la hausse du prix "
         "accroît la consommation, par contrainte, l’effet de revenu "
         "l’emportant sur l’effet de substitution. Le bien de Veblen apparaît "
         "au contraire dans un contexte de richesse : c’est un bien supérieur "
         "de luxe dont la hausse du prix accroît la consommation, par "
         "affichage social.",
    'r': "Le raisonnement montre que deux exceptions apparemment identiques "
         "reposent sur des mécanismes opposés, l’un économique et contraint, "
         "l’autre social et volontaire.",
    'ex': "La loi d’Engel, selon laquelle la structure de la consommation "
          "change quand le revenu augmente."}],
  voisins=['n7-contrainte-budgetaire', 'n7-elasticites', 'n7-choix',
           'n7-ostentatoire'])


d('n7-elasticites', 7, "Élasticités",
  "Mesurer la sensibilité de la demande, et classer les biens",
  "L’élasticité mesure la sensibilité de la demande d’un bien à la variation "
  "d’une grandeur. Le cours en distingue trois : l’élasticité-prix, par "
  "rapport au prix du bien lui-même ; l’élasticité-revenu, qui mesure la "
  "variation de la demande lorsque le revenu varie ; l’élasticité-prix "
  "croisée, qui mesure l’effet d’une variation du prix d’un autre bien. Leur "
  "usage principal est de classer les biens.",
  "Les élasticités sont l’outil qui transforme la théorie du consommateur en "
  "instrument d’analyse, et le cours en donne un usage très précis : elles "
  "servent à classer les biens, à faire une typologie, et à comprendre les "
  "comportements. La formule qu’il retient est frappante : dire le nom du "
  "bien, c’est déjà dire comment sa demande réagit. La typologie obtenue "
  "distingue les biens normaux, supérieurs, inférieurs, de Giffen, de Veblen, "
  "complémentaires et substituables. L’élasticité-revenu permet la première "
  "série de distinctions : un bien inférieur a une élasticité-revenu "
  "négative, puisque la demande baisse quand le revenu augmente ; un bien "
  "normal a une élasticité comprise entre 0 et 1 ; un bien supérieur a une "
  "élasticité supérieure à 1, la demande augmentant fortement avec le revenu. "
  "Parmi les biens inférieurs on trouve les biens de Giffen, parmi les biens "
  "supérieurs souvent les biens de Veblen — et le cours met explicitement en "
  "garde contre la confusion : le bien de Giffen relève d’un contexte de "
  "pauvreté extrême et sa consommation augmente avec le prix par contrainte, "
  "tandis que le bien de Veblen relève d’un contexte de richesse et sa "
  "consommation augmente avec le prix par affichage social. L’élasticité-prix "
  "croisée permet la seconde série : négative, elle indique des biens "
  "complémentaires, puisque la hausse du prix de l’un réduit la demande de "
  "l’autre — l’exemple du cours est la place de cinéma et le popcorn ; "
  "positive, elle indique des biens substituables ; nulle, des biens "
  "indépendants. Le cours relie enfin les élasticités à la loi d’Engel : "
  "quand le revenu augmente, la structure de la consommation change, ce qui "
  "est exactement une question d’élasticité-revenu. Et il montre leur usage "
  "stratégique : si la demande est peu élastique, l’entreprise peut augmenter "
  "le prix ; si elle est très élastique, elle doit le maintenir bas.",
  [("La mesure de la sensibilité relative",
    "L’élasticité rapporte une variation de demande à une variation de la "
    "grandeur qui l’a provoquée : elle est sans unité, ce qui permet de "
    "comparer des biens très différents."),
   ("La classification par l’élasticité-revenu",
    "Une élasticité-revenu négative désigne un bien inférieur, une élasticité "
    "comprise entre 0 et 1 un bien normal, une élasticité supérieure à 1 un "
    "bien supérieur : le signe et le niveau suffisent à classer."),
   ("La classification par l’élasticité croisée",
    "Une élasticité croisée négative signale des biens complémentaires, une "
    "élasticité positive des biens substituables, une élasticité nulle des "
    "biens indépendants."),
   ("Le lien avec la structure de consommation",
    "Quand le revenu augmente, la structure de la consommation change : la loi "
    "d’Engel est une proposition sur les élasticités-revenu comparées des "
    "différents postes de dépense."),
   ("L’usage stratégique par les entreprises",
    "Si la demande est peu élastique, l’entreprise peut augmenter le prix car "
    "le consommateur ne renonce pas facilement ; si elle est très élastique, "
    "elle doit maintenir un prix plus bas pour éviter le renoncement.")],
  [{'a': "Les élasticités transforment une analyse qualitative en mesure "
         "comparable entre biens et entre périodes.",
    'cond': "La comparaison suppose que l’élasticité soit estimée sur la même "
            "plage de prix et de revenus.",
    'lim': "L’élasticité n’est pas constante : elle varie le long de la courbe "
           "de demande, ce qui interdit de la traiter comme une "
           "caractéristique fixe du bien."},
   {'a': "Elles permettent de classer les biens, ce qui est leur usage "
         "principal selon le cours : dire le nom du bien, c’est déjà dire "
         "comment sa demande réagit.",
    'cond': "Le classement n’est pertinent que rapporté à un niveau de revenu "
            "donné, un bien pouvant être normal pour les uns et inférieur pour "
            "les autres.",
    'lim': "Cette dépendance au revenu rend la typologie moins stable qu’elle "
           "ne le paraît et impose de préciser la population considérée."},
   {'a': "Elles relient la théorie du consommateur à la stratégie des "
         "entreprises, par le lien entre élasticité et pouvoir de marché.",
    'cond': "Le lien suppose que l’entreprise puisse estimer l’élasticité de "
            "la demande qui lui est adressée.",
    'lim': "Cette élasticité dépend elle-même des stratégies de "
           "différenciation, de sorte qu’elle est en partie construite par "
           "l’entreprise, comme le montre Chamberlin."},
   {'a': "Elles éclairent l’effet distributif d’une taxe ou d’une variation de "
         "prix selon la catégorie de biens touchée.",
    'cond': "L’analyse suppose de connaître précisément la structure de "
            "consommation des ménages concernés.",
    'lim': "Elle suppose aussi que les comportements restent stables, "
           "hypothèse que l’économie comportementale remet en cause."}],
  [{'t': "Il ne faut pas confondre bien de Giffen et bien de Veblen, qui "
         "relèvent de mécanismes opposés.",
    'qui': "La mise en garde explicite du cours sur cette confusion "
           "fréquente.",
    'rep': "La distinction est nette : le bien de Giffen est un bien inférieur "
           "consommé par contrainte en contexte de pauvreté extrême, le bien "
           "de Veblen un bien supérieur de luxe consommé par affichage social "
           "en contexte de richesse."},
   {'t': "La loi d’Engel avait déjà formulé le contenu de "
         "l’élasticité-revenu, avant que la notion soit nommée.",
    'qui': "Ernst Engel, dont le cours rappelle la loi.",
    'rep': "Le rapprochement est explicite dans le cours : la loi d’Engel dit "
           "que quand le revenu augmente la structure de la consommation "
           "change, ce qui est exactement une question d’élasticité-revenu."},
   {'t': "L’élasticité de la demande n’est pas une donnée mais le résultat des "
         "stratégies des entreprises.",
    'qui': "Edward Chamberlin, avec la différenciation des produits.",
    'rep': "L’objection est forte : la différenciation réduit "
           "l’élasticité-prix de la demande, car le consommateur fidèle à une "
           "marque ne substitue plus facilement un produit à un autre."},
   {'t': "Les élasticités supposent des comportements stables, ce que "
         "l’économie comportementale conteste.",
    'qui': "Richard Thaler, pour qui les préférences ne sont pas fixes.",
    'rep': "L’objection limite la portée prédictive de l’outil sans en annuler "
           "l’usage descriptif : les élasticités restent une mesure des "
           "comportements observés."}],
  [{'n': "Ernst Engel",
    'i': "Quand le revenu augmente, la structure de la consommation change.",
    'p': "Le cours relie sa loi à l’élasticité-revenu et en précise le "
         "contenu : les ménages riches dépensent proportionnellement moins "
         "dans certains biens, comme l’alimentation, mais compensent par "
         "d’autres postes de dépense."},
   {'n': "Thorstein Veblen",
    'i': "Certains biens supérieurs voient leur demande augmenter avec leur "
         "prix, par affichage social.",
    'p': "Le cours en fait une catégorie de la typologie des biens et insiste "
         "sur la distinction avec le bien de Giffen : contexte de richesse "
         "contre contexte de pauvreté extrême, affichage social contre "
         "contrainte."},
   {'n': "Edward Chamberlin",
    'i': "La différenciation des produits réduit l’élasticité-prix de la "
         "demande.",
    'p': "Le cours illustre le mécanisme par les yaourts : un consommateur "
         "indifférent change facilement de marque, un consommateur attaché à "
         "une marque ne la remplace pas facilement, de sorte que la marque "
         "réduit la substituabilité."},
   {'n': "Alfred Marshall",
    'i': "L’analyse économique procède par comparaison marginale des "
         "variations.",
    'p': "Le cours le présente comme le prédécesseur de Pigou et l’un des "
         "fondateurs de l’analyse néoclassique ; les élasticités relèvent "
         "directement de ce raisonnement marginal, puisqu’elles rapportent une "
         "variation à une autre."}],
  [{'f': "Le cours résume l’usage des élasticités par une formule : dire le "
         "nom du bien, c’est déjà dire comment sa demande réagit.",
    'p': "La formule montre que la typologie n’est pas descriptive mais "
         "prédictive : nommer un bien revient à annoncer sa réaction aux "
         "variations de prix et de revenu."},
   {'f': "Une élasticité-revenu négative désigne un bien inférieur, comprise "
         "entre 0 et 1 un bien normal, supérieure à 1 un bien supérieur.",
    'p': "Les trois seuils sont à connaître précisément, car ils fondent toute "
         "la typologie et permettent de classer un bien à partir d’une seule "
         "mesure."},
   {'f': "Une élasticité-prix croisée négative signale des biens "
         "complémentaires : si le prix de la place de cinéma augmente, la "
         "consommation de popcorn diminue.",
    'p': "L’exemple rend immédiatement intelligible le signe de l’élasticité "
         "croisée et son interprétation en termes de complémentarité."},
   {'f': "Si la demande est peu élastique, l’entreprise peut augmenter le prix "
         "car le consommateur ne renonce pas facilement ; si elle est très "
         "élastique, elle doit maintenir un prix plus bas.",
    'p': "Le fait relie directement la théorie du consommateur à la stratégie "
         "tarifaire des entreprises et au pouvoir de marché."}],
  [{'q': "Sujet du type « Comment classer les biens selon leur demande ? »",
    'f': "Les élasticités fournissent la typologie complète. "
         "L’élasticité-revenu distingue le bien inférieur, dont la demande "
         "baisse quand le revenu augmente, le bien normal, dont l’élasticité "
         "est comprise entre 0 et 1, et le bien supérieur, dont la demande "
         "augmente fortement. L’élasticité croisée distingue les biens "
         "complémentaires, dont l’élasticité est négative, les biens "
         "substituables, dont elle est positive, et les biens indépendants. "
         "Comme le résume le cours, dire le nom du bien, c’est déjà dire "
         "comment sa demande réagit.",
    'r': "Le raisonnement fait de la mesure un instrument de classement, ce "
         "qui transforme l’élasticité en outil de prévision et non seulement "
         "de description.",
    'ex': "La place de cinéma et le popcorn, biens complémentaires dont "
          "l’élasticité croisée est négative."},
   {'q': "Sujet du type « Pourquoi certains biens voient-ils leur demande "
         "augmenter quand leur prix monte ? »",
    'f': "Deux cas opposés existent et le cours met en garde contre leur "
         "confusion. Le bien de Giffen relève d’un contexte de pauvreté "
         "extrême : c’est un bien inférieur dont la hausse du prix accroît la "
         "consommation par contrainte. Le bien de Veblen relève d’un contexte "
         "de richesse : c’est un bien supérieur, de luxe, dont la hausse du "
         "prix accroît la consommation par affichage social. Parmi les biens "
         "inférieurs on trouve les premiers, parmi les biens supérieurs "
         "souvent les seconds.",
    'r': "Le raisonnement montre que deux exceptions apparemment identiques "
         "s’expliquent par des mécanismes contraires, l’un relevant du budget "
         "contraint et l’autre de la signification sociale du prix.",
    'ex': "Les biens de luxe, dont le prix élevé est précisément ce qui fait "
          "la valeur de signe."}],
  voisins=['n7-effet-revenu-substitution', 'n7-ostentatoire', 'n7-choix',
           'n5-concurrence-monopolistique'])
