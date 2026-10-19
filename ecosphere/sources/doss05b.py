# -*- coding: utf-8 -*-
"""Ensemble 5 — Le marché, les prix et la concurrence (2/3)."""

from doss_base import d

d('n5-cpp', 5, "Concurrence pure et parfaite",
  "Cinq hypothèses qui garantissent, en théorie, l’efficacité du marché",
  "La concurrence pure et parfaite est le modèle de référence construit par "
  "les néoclassiques pour formaliser l’efficacité du marché. Il repose sur "
  "cinq conditions : homogénéité des produits, atomicité des agents, mobilité "
  "des facteurs de production, libre entrée et libre sortie, transparence de "
  "l’information. Si ces conditions sont réunies, le marché conduit à une "
  "allocation jugée efficace des ressources.",
  "La concurrence pure et parfaite doit être traitée comme un étalon et non "
  "comme une description : son intérêt est de rendre visible, par contraste, "
  "ce qui se passe lorsque l’une de ses hypothèses tombe. Le cours organise "
  "d’ailleurs l’analyse exactement ainsi, en examinant chaque hypothèse puis "
  "l’auteur qui en montre la fragilité. L’homogénéité suppose des produits "
  "parfaitement interchangeables, ne se distinguant que par le prix ; or les "
  "entreprises cherchent à différencier leurs produits par la marque, la "
  "qualité ou le design, et cette différenciation, mise en évidence par Edward "
  "Chamberlin, conduit à une concurrence monopolistique où chaque producteur "
  "dispose d’un certain pouvoir de marché. L’atomicité suppose une multitude "
  "d’offreurs et de demandeurs, chacun trop petit pour influencer le prix, "
  "donc price takers ; or on observe une concentration des activités, qui "
  "conduit à l’oligopole ou au monopole. La mobilité des facteurs suppose que "
  "travail et capital se déplacent librement d’un secteur à l’autre ; or elle "
  "est souvent imparfaite, les diplômes n’étant pas toujours reconnus d’un "
  "pays à l’autre et les travailleurs ne pouvant changer instantanément de "
  "secteur. La libre entrée et la libre sortie supposent l’absence de "
  "barrières techniques, financières ou réglementaires ; or ces barrières "
  "existent fréquemment — coûts élevés, brevets, réglementations — et c’est "
  "pourquoi William Baumol insiste sur les marchés contestables, où la seule "
  "menace d’entrée suffit à discipliner les entreprises en place. La "
  "transparence suppose une information parfaite, gratuite et symétrique ; or "
  "l’asymétrie d’information est la règle plutôt que l’exception, comme "
  "George Akerlof l’a montré en 1970. Le résultat théorique du modèle est "
  "précis : la demande adressée à la firme y est parfaitement élastique, ce "
  "qui garantit l’égalité entre le prix, la recette marginale et le coût "
  "marginal, et donc une allocation optimale. Toute structure de marché qui "
  "empêche l’égalité P = Cm conduit à l’inverse à une allocation "
  "sous-optimale.",
  [("L’homogénéité des produits",
    "Les biens sont parfaitement interchangeables et ne se distinguent que par "
    "le prix : aucun producteur ne peut fidéliser une clientèle, de sorte "
    "qu’une hausse de prix lui ferait perdre tous ses clients."),
   ("L’atomicité des agents",
    "Les offreurs et les demandeurs sont si nombreux qu’aucun ne pèse sur le "
    "prix : chacun est preneur de prix, et la décision individuelle n’a aucun "
    "effet observable sur le marché."),
   ("La mobilité des facteurs",
    "Travail et capital se déplacent librement d’un secteur à l’autre : cette "
    "mobilité est ce qui permet aux ressources de se redéployer rapidement "
    "vers les emplois les plus rentables, donc l’ajustement du système."),
   ("La libre entrée et la libre sortie",
    "Aucune barrière technique, financière ou réglementaire n’empêche "
    "d’entrer ou de quitter le marché : cette liberté garantit qu’un profit "
    "anormal attire des concurrents et disparaît, donc une concurrence "
    "durable."),
   ("La transparence de l’information",
    "Tous les agents connaissent les prix et les caractéristiques des "
    "produits, l’information étant parfaite, gratuite et symétrique : c’est "
    "cette hypothèse qui garantit que le prix suffit à décider.")],
  [{'a': "Le modèle fournit un étalon d’efficacité précis, puisqu’il conduit à "
         "l’égalité du prix et du coût marginal, condition d’une allocation "
         "optimale.",
    'cond': "L’égalité P = Cm ne s’obtient que si la demande adressée à la "
            "firme est parfaitement élastique, ce que seule l’atomicité "
            "jointe à l’homogénéité garantit.",
    'lim': "Toute structure de marché qui empêche cette égalité conduit à une "
           "allocation sous-optimale, ce qui est le cas général dans "
           "l’économie observée."},
   {'a': "Il permet de classer les imperfections, chaque hypothèse levée "
         "renvoyant à une structure ou à une défaillance identifiée.",
    'cond': "Le classement suppose que l’on sache quelle hypothèse est "
            "précisément en défaut, ce qui exige une analyse empirique du "
            "marché considéré.",
    'lim': "Plusieurs hypothèses tombent en général simultanément, de sorte "
           "que les effets se combinent et ne s’additionnent pas simplement."},
   {'a': "Il rend le raisonnement économique cumulatif, chaque auteur "
         "s’attaquant à une hypothèse précise du modèle.",
    'cond': "La lecture cumulative suppose de rattacher chaque auteur à "
            "l’hypothèse qu’il met en cause, comme le fait le cours.",
    'lim': "Elle peut donner l’impression que le modèle est seulement "
           "incomplet, alors que certaines critiques, comme celle de "
           "Sonnenschein-Mantel-Debreu, en atteignent le principe."},
   {'a': "Il demeure le cadre de référence de nombreuses théories appliquées, "
         "notamment des premières théories du commerce international.",
    'cond': "Son emploi reste légitime lorsque l’objet d’étude ne dépend pas, "
            "de façon décisive, des hypothèses que l’on relâche.",
    'lim': "Les théories contemporaines du commerce ont précisément dû "
           "introduire concurrence imparfaite, économies d’échelle et "
           "hétérogénéité des firmes pour rendre compte des échanges réels."}],
  [{'t': "La différenciation des produits détruit l’homogénéité et confère à "
         "chaque producteur un pouvoir de marché.",
    'qui': "Edward Chamberlin, avec la concurrence monopolistique.",
    'rep': "L’objection est décisive pour la plupart des marchés de biens de "
           "consommation : la marque réduit la substituabilité, donc "
           "l’élasticité-prix, et le prix n’est plus purement concurrentiel."},
   {'t': "L’atomicité est contredite par la concentration observée des "
         "activités, qui fait apparaître des firmes dominantes.",
    'qui': "Le constat que le cours tire de l’existence des multinationales, "
           "des grandes firmes et des concentrations.",
    'rep': "Le cours formule l’objection comme un paradoxe : dans la "
           "concurrence parfaite, aucune entreprise ne devrait avoir un "
           "pouvoir important, or la réalité montre des groupes dominants."},
   {'t': "Ce n’est pas le nombre d’entreprises qui compte mais la possibilité "
         "d’entrer et de sortir du marché.",
    'qui': "William Baumol, avec la théorie des marchés contestables.",
    'rep': "La reformulation sauve une partie du modèle : même seule sur son "
           "marché, une entreprise peut se comporter comme en concurrence si "
           "elle craint l’arrivée de concurrents."},
   {'t': "L’asymétrie d’information n’est pas une exception mais la situation "
         "normale des marchés.",
    'qui': "George Akerlof, dans The Market for Lemons (1970).",
    'rep': "Son mécanisme va plus loin qu’une simple imperfection : le prix "
           "moyen proposé chasse les bonnes voitures, la qualité moyenne "
           "baisse, la confiance disparaît et le marché peut s’effondrer."}],
  [{'n': "Edward Chamberlin",
    'i': "Les entreprises peuvent être en concurrence tout en disposant d’un "
         "pouvoir de marché grâce à la différenciation.",
    'p': "Il développe cette idée en 1933. Le cours la rattache directement à "
         "l’hypothèse d’homogénéité : la différenciation par la marque, la "
         "qualité ou le design fait que le prix n’est plus purement "
         "concurrentiel."},
   {'n': "William Baumol",
    'i': "Le vrai critère de la concurrence n’est pas le nombre d’entreprises "
         "mais la libre entrée et la libre sortie.",
    'p': "Avec John Panzar et Robert Willig, il développe dans les années "
         "1980 la théorie des marchés contestables. Le cours la présente comme "
         "une réponse aux barrières à l’entrée : la menace d’entrée suffit à "
         "discipliner l’entreprise en place."},
   {'n': "George Akerlof",
    'i': "L’asymétrie d’information peut faire disparaître les bons produits "
         "et détruire le marché.",
    'p': "Son article The Market for Lemons (1970) montre que si le vendeur "
         "connaît la qualité de sa voiture et l’acheteur non, celui-ci propose "
         "un prix moyen, trop bas pour les bonnes voitures, dont les vendeurs "
         "quittent alors le marché."},
   {'n': "Herbert Simon",
    'i': "Les agents recherchent des solutions satisfaisantes plutôt "
         "qu’optimales.",
    'p': "Le cours présente sa rationalité limitée comme une critique très "
         "cohérente du modèle de concurrence pure et parfaite : même si les "
         "conditions mathématiques étaient remplies, les agents réels ne "
         "seraient pas capables de se comporter comme il l’exige."}],
  [{'f': "Les cinq conditions du modèle sont l’homogénéité des produits, "
         "l’atomicité des agents, la mobilité des facteurs, la libre entrée et "
         "libre sortie, et la transparence de l’information.",
    'p': "L’énumération est à connaître intégralement, car chaque hypothèse "
         "relâchée ouvre sur une structure de marché ou une défaillance "
         "distincte."},
   {'f': "Le cours précise que ces hypothèses sont rarement vérifiées dans la "
         "réalité, ce qui explique les dysfonctionnements possibles des "
         "marchés.",
    'p': "La formulation indique le statut du modèle : il sert à expliquer les "
         "écarts observés plutôt qu’à décrire le fonctionnement courant des "
         "marchés."},
   {'f': "En concurrence pure et parfaite, la demande adressée à la firme est "
         "parfaitement élastique, ce qui garantit l’égalité entre le prix, la "
         "recette marginale et le coût marginal.",
    'p': "C’est le résultat technique central : il relie la structure du "
         "marché à la propriété d’efficacité et permet de démontrer plutôt que "
         "d’affirmer."},
   {'f': "Les premières théories du commerce international reposent largement "
         "sur le cadre de la concurrence pure et parfaite, que les théories "
         "contemporaines relâchent progressivement.",
    'p': "Le fait montre la fécondité du modèle comme point de départ et la "
         "nécessité de l’amender : les théories récentes introduisent "
         "concurrence imparfaite, économies d’échelle et hétérogénéité des "
         "firmes."}],
  [{'q': "Sujet du type « La concurrence pure et parfaite est-elle un modèle "
         "utile ? »",
    'f': "Son utilité ne tient pas à son réalisme mais à sa fonction d’étalon. "
         "Les cinq hypothèses — homogénéité, atomicité, mobilité des "
         "facteurs, libre entrée et sortie, transparence — garantissent en "
         "théorie l’auto-régulation par les prix, mais le cours souligne "
         "qu’elles sont rarement vérifiées, ce qui explique précisément les "
         "dysfonctionnements possibles des marchés. Le modèle sert donc à "
         "identifier, hypothèse par hypothèse, l’origine des imperfections "
         "observées.",
    'r': "Le raisonnement renverse l’objection habituelle sur l’irréalisme du "
         "modèle : c’est parce qu’il est irréaliste qu’il permet de classer "
         "les écarts à la réalité.",
    'ex': "La différenciation des produits mise en évidence par Chamberlin, "
          "qui dérive directement de la levée de l’hypothèse d’homogénéité."},
   {'q': "Sujet du type « Les marchés sont-ils concurrentiels ? »",
    'f': "Chacune des cinq hypothèses est démentie par un fait établi. "
         "L’homogénéité est contredite par la différenciation des produits, "
         "l’atomicité par la concentration des activités qui conduit à "
         "l’oligopole ou au monopole, la mobilité par la non-reconnaissance "
         "des diplômes et l’impossibilité de changer instantanément de "
         "secteur, la libre entrée par les barrières de coûts, de brevets et "
         "de réglementation, la transparence par l’asymétrie d’information qui "
         "constitue la situation normale des marchés.",
    'r': "Le raisonnement procède hypothèse par hypothèse, ce qui permet une "
         "démonstration systématique au lieu d’une affirmation générale sur "
         "l’imperfection des marchés.",
    'ex': "Le marché des voitures d’occasion d’Akerlof, où l’asymétrie "
          "d’information peut faire s’effondrer l’échange."}],
  voisins=['n5-monopole', 'n5-concurrence-monopolistique', 'n5-contestables',
           'n5-efficacite', 'n5-marche'],
  comp={'titre': "Concurrence pure et parfaite et monopole",
        'a': "Concurrence pure et parfaite", 'b': "Monopole",
        'lignes': [
          ("Nombre de vendeurs", "Une multitude, par hypothèse d’atomicité",
           "Un seul, sans substitut proche"),
          ("Position de la firme sur le prix", "Price taker (preneuse de prix)",
           "Price maker (faiseuse de prix)"),
          ("Demande adressée à la firme", "Parfaitement élastique",
           "Décroissante"),
          ("Règle de décision",
           "Prix = recette marginale = coût marginal",
           "Recette marginale = coût marginal, avec prix supérieur au coût "
           "marginal"),
          ("Référence du prix fixé", "Le coût marginal",
           "La disposition à payer des consommateurs"),
          ("Quantité produite", "Quantité socialement optimale",
           "Quantité plus faible que l’optimum social"),
          ("Niveau du prix", "Le plus bas compatible avec la couverture des "
           "coûts", "Plus élevé"),
          ("Surplus", "Surplus total maximal, ni pénurie ni gaspillage",
           "Surplus du consommateur réduit, rente de monopole, perte sèche"),
          ("Évaluation en termes d’allocation", "Allocation optimale",
           "Allocation sous-optimale"),
        ]})


d('n5-surplus', 5, "Surplus du consommateur et du producteur",
  "Mesurer en monnaie le gain que l’échange procure à chaque partie",
  "Le surplus du consommateur correspond à la différence entre ce qu’il était "
  "prêt à payer et ce qu’il paie réellement ; le surplus du producteur à la "
  "différence entre le prix minimal qu’il était prêt à accepter et le prix "
  "obtenu. La somme des deux constitue le gain total à l’échange, et c’est "
  "l’instrument par lequel l’analyse économique évalue le bien-être produit "
  "par un marché.",
  "Le surplus est l’outil qui transforme un jugement qualitatif sur l’échange "
  "en évaluation quantifiable, et c’est pourquoi il revient dans tous les "
  "chapitres du programme. Son principe est simple : chaque participant à "
  "l’échange en retire un gain, égal à l’écart entre ce qu’il aurait accepté "
  "et ce qu’il obtient. Du côté du consommateur, l’écart entre la disposition "
  "à payer et le prix effectivement payé ; du côté du producteur, l’écart "
  "entre le prix minimal acceptable et le prix reçu. Leur somme mesure le gain "
  "total à l’échange, ce qui fonde la thèse néoclassique selon laquelle le "
  "marché est fondamentalement mutuellement avantageux — avec une réserve que "
  "le cours énonce lui-même, puisque certains individus peuvent être exclus "
  "lorsque le prix est trop élevé. Trois usages donnent à la notion toute sa "
  "portée. Premier usage, l’évaluation des structures de marché : en "
  "concurrence pure et parfaite le surplus total est maximal, sans pénurie ni "
  "gaspillage, tandis que le monopole réduit le surplus du consommateur, fait "
  "apparaître une rente de monopole et une perte sèche — le triangle "
  "d’Harberger — donc une allocation sous-optimale. Deuxième usage, "
  "l’évaluation des politiques commerciales : le cours montre qu’un droit de "
  "douane redistribue une partie du surplus des consommateurs vers les "
  "producteurs et l’État, mais crée aussi deux pertes sèches, une production "
  "domestique inefficiente et une consommation abandonnée du fait de la hausse "
  "des prix, de sorte que le bien-être collectif diminue. Troisième usage, la "
  "comparaison des instruments : les mesures protectionnistes tendent toutes à "
  "augmenter le surplus des producteurs et à réduire celui des consommateurs, "
  "mais diffèrent par leurs effets sur les recettes publiques — recettes "
  "fiscales pour un droit de douane, dépenses publiques pour une subvention, "
  "création de rentes pour un quota.",
  [("L’écart entre disposition à payer et prix payé",
    "Le consommateur qui aurait accepté de payer davantage conserve la "
    "différence : ce gain n’apparaît dans aucune transaction mais il est réel, "
    "et il se mesure sous la courbe de demande au-dessus du prix."),
   ("L’écart entre prix minimal et prix reçu",
    "Le producteur dont le coût est inférieur au prix de marché encaisse la "
    "différence : son surplus se mesure au-dessus de la courbe d’offre et "
    "au-dessous du prix."),
   ("L’agrégation en gain total à l’échange",
    "La somme des deux surplus donne le bien-être créé par le marché : c’est "
    "ce total que l’analyse chercher à maximiser, indépendamment de sa "
    "répartition entre les deux parties."),
   ("La redistribution entre les parties",
    "Une mesure qui déplace le prix transfère du surplus d’un côté à l’autre "
    "sans nécessairement en détruire : le droit de douane transfère du "
    "consommateur vers le producteur et l’État."),
   ("La perte sèche",
    "Certaines mesures détruisent du surplus sans le transférer à personne : "
    "une production domestique inefficiente et une consommation abandonnée du "
    "fait du prix plus élevé constituent deux pertes nettes de bien-être.")],
  [{'a': "Le surplus transforme l’évaluation du bien-être en grandeur "
         "mesurable, ce qui permet de comparer des situations et des "
         "politiques.",
    'cond': "La mesure suppose que les courbes d’offre et de demande "
            "reflètent fidèlement les dispositions à payer et les coûts.",
    'lim': "Elle attribue le même poids à un euro de surplus quel que soit "
           "celui qui le perçoit, ce qui en fait un critère d’efficacité et "
           "non de justice."},
   {'a': "Il distingue ce qui est redistribué de ce qui est détruit, "
         "distinction essentielle pour juger une politique économique.",
    'cond': "La distinction n’est nette que si l’on identifie les "
            "bénéficiaires du transfert, qui diffèrent selon l’instrument.",
    'lim': "Le cours montre que selon l’instrument le transfert bénéficie à "
           "l’État, aux producteurs protégés ou même aux producteurs "
           "étrangers, ce qui complique la comparaison."},
   {'a': "Il fournit une démonstration rigoureuse de l’avantage mutuel de "
         "l’échange, puisque les deux parties y gagnent simultanément.",
    'cond': "L’avantage mutuel ne concerne que ceux qui participent "
            "effectivement à l’échange au prix formé sur le marché.",
    'lim': "Le cours souligne que certains individus peuvent être exclus "
           "lorsque le prix est trop élevé, et le surplus ne rend pas compte "
           "de cette exclusion."},
   {'a': "Il relie l’analyse microéconomique des structures de marché à "
         "l’évaluation macroéconomique des politiques publiques.",
    'cond': "Le passage de l’une à l’autre suppose que les effets d’équilibre "
            "général soient négligeables, ce qui n’est pas toujours le cas.",
    'lim': "Dans un grand pays, la mesure modifie le prix mondial, de sorte "
           "que l’analyse en équilibre partiel sous-estime les effets."}],
  [{'t': "Le surplus est un critère d’efficacité qui reste muet sur la "
         "justice de la répartition obtenue.",
    'qui': "La critique du critère de Pareto que le cours formule, puisque "
           "celui-ci ne dit rien sur l’égalité ni sur la morale.",
    'rep': "L’objection est exacte et doit être assumée : le surplus mesure un "
           "gain agrégé, et deux situations de surplus total identique peuvent "
           "répartir ce gain de façon radicalement différente."},
   {'t': "Le surplus ignore ceux qui ne participent pas à l’échange, alors que "
         "l’exclusion est précisément un enjeu central.",
    'qui': "La réserve que le cours apporte à l’avantage mutuel de l’échange "
           "néoclassique.",
    'rep': "L’objection est fondée, le cours admettant que certains individus "
           "peuvent être exclus lorsque le prix est trop élevé ; elle "
           "n’invalide pas l’instrument mais borne son usage."},
   {'t': "Le calcul de surplus suppose des courbes connues, alors que la "
         "demande globale peut prendre n’importe quelle forme.",
    'qui': "Hugo Sonnenschein, Rolf Mantel et Gérard Debreu.",
    'rep': "La difficulté est réelle au niveau agrégé ; elle est moins "
           "contraignante pour l’analyse d’un marché particulier, où les "
           "élasticités peuvent être estimées."},
   {'t': "La mesure en surplus néglige les externalités, qui ne passent pas "
         "par le marché et donc n’apparaissent pas dans les courbes.",
    'qui': "L’analyse pigouvienne des externalités, dont le cours rappelle "
           "qu’elles ne sont pas prises en compte dans le prix.",
    'rep': "L’objection est décisive pour les biens polluants : le surplus "
           "calculé sur le coût privé surestime le bien-être, puisque la "
           "courbe de coût marginal social se situe au-dessus de la courbe de "
           "coût marginal privé."}],
  [{'n': "Léon Walras",
    'i': "Une fois l’équilibre atteint, le marché permet la création de gains "
         "à l’échange.",
    'p': "Le cours rattache le surplus au mécanisme d’équilibre : c’est parce "
         "que le prix s’ajuste jusqu’au point de rencontre que l’échange "
         "devient mutuellement avantageux, le consommateur payant moins qu’il "
         "n’aurait accepté et le producteur recevant plus qu’il n’exigeait."},
   {'n': "Vilfredo Pareto",
    'i': "L’optimalité signifie seulement qu’on ne peut améliorer la situation "
         "de l’un sans détériorer celle d’un autre.",
    'p': "Son critère éclaire la portée du surplus : maximiser le surplus "
         "total est un objectif d’efficacité, et le cours insiste sur le fait "
         "que cela ne dit rien sur l’égalité, ni sur la morale."},
   {'n': "Arthur Pigou",
    'i': "Le prix de marché ne reflète pas le coût social lorsqu’il existe une "
         "externalité.",
    'p': "Son analyse limite directement la portée du calcul de surplus : si "
         "la courbe de coût marginal social se situe au-dessus de la courbe de "
         "coût marginal privé, le surplus calculé sur les coûts privés "
         "surestime le bien-être réellement produit."}],
  [{'f': "Le cours définit le surplus du consommateur comme la différence "
         "entre ce qu’il était prêt à payer et ce qu’il paie réellement, et "
         "celui du producteur comme la différence entre son prix minimal et le "
         "prix obtenu.",
    'p': "Les deux définitions sont symétriques et doivent être restituées "
         "ensemble, car c’est leur somme qui mesure le gain à l’échange."},
   {'f': "En concurrence pure et parfaite le surplus total est maximal, il n’y "
         "a ni pénurie ni gaspillage et le bien-être collectif est maximisé.",
    'p': "L’énoncé fait du surplus le critère par lequel la concurrence pure "
         "et parfaite est jugée efficace, ce qui en fait un instrument de "
         "démonstration et non une simple illustration."},
   {'f': "Le monopole entraîne une réduction du surplus du consommateur, "
         "l’apparition d’une rente de monopole et une perte sèche, le triangle "
         "d’Harberger.",
    'p': "Les trois effets doivent être distingués : le premier est une perte, "
         "le deuxième un transfert, le troisième une destruction nette de "
         "bien-être."},
   {'f': "Le cours montre qu’un droit de douane redistribue du surplus des "
         "consommateurs vers les producteurs et l’État, mais crée deux pertes "
         "sèches, une distorsion productive et une distorsion de consommation.",
    'p': "L’analyse est directement transposable : elle montre comment "
         "décomposer l’effet d’une mesure en transferts et en pertes nettes."}],
  [{'q': "Sujet du type « Qui gagne à l’échange marchand ? »",
    'f': "Les deux parties y gagnent simultanément, et le surplus le mesure. "
         "Le consommateur gagne la différence entre ce qu’il était prêt à "
         "payer et ce qu’il paie réellement, le producteur la différence entre "
         "son prix minimal et le prix obtenu, et la somme des deux constitue "
         "le gain total à l’échange. Pour les néoclassiques, le marché est "
         "donc fondamentalement mutuellement avantageux, même si certains "
         "individus peuvent être exclus lorsque le prix est trop élevé.",
    'r': "Le raisonnement établit l’avantage mutuel sans le confondre avec un "
         "avantage universel, ce qui permet d’introduire la question de "
         "l’exclusion sans contredire l’analyse.",
    'ex': "La réserve explicite du cours sur l’exclusion des individus "
          "lorsque le prix est trop élevé."},
   {'q': "Sujet du type « Comment évaluer une politique économique ? »",
    'f': "L’analyse en surplus permet de distinguer ce qui est transféré de ce "
         "qui est détruit. Un droit de douane relève le prix intérieur : les "
         "producteurs domestiques gagnent du surplus, les recettes publiques "
         "augmentent, les importations reculent, mais le surplus des "
         "consommateurs diminue fortement et deux pertes sèches apparaissent, "
         "une distorsion productive et une distorsion de consommation. Le "
         "bien-être collectif diminue donc.",
    'r': "Le raisonnement décompose un effet global en transferts identifiés "
         "et en pertes nettes, ce qui permet de dire qui gagne, qui perd et ce "
         "que personne ne récupère.",
    'ex': "La comparaison des instruments protectionnistes : recettes fiscales "
          "pour le droit de douane, dépenses publiques pour la subvention, "
          "création de rentes pour le quota."},
   {'q': "Sujet du type « L’efficacité du marché garantit-elle le bien-être ? »",
    'f': "Le surplus mesure un gain agrégé, non sa répartition. En "
         "concurrence pure et parfaite le surplus total est maximal, mais le "
         "critère de Pareto auquel cette optimalité renvoie est un critère "
         "d’efficacité et non de justice : il ne dit rien sur l’égalité ni sur "
         "la morale, et affirme seulement qu’on ne peut plus améliorer la "
         "situation de l’un sans détériorer celle d’un autre.",
    'r': "Le raisonnement sépare deux questions que le vocabulaire du "
         "bien-être tend à confondre, le niveau du gain collectif et sa "
         "distribution, ce qui est indispensable pour conclure.",
    'ex': "Une répartition très inégale peut maximiser le surplus total tout "
          "en excluant du marché ceux pour qui le prix est trop élevé."}],
  voisins=['n5-cpp', 'n5-efficacite', 'n5-pareto', 'n5-monopole'])


d('n5-efficacite', 5, "Efficacité économique",
  "Une allocation est efficace quand le prix égale le coût marginal",
  "L’efficacité économique désigne la situation dans laquelle les ressources "
  "sont utilisées de manière optimale. Sa condition fondamentale, en "
  "microéconomie standard, est l’égalité entre le prix et le coût marginal : "
  "lorsqu’elle est respectée, la quantité produite est optimale, le surplus "
  "total est maximal, il n’y a ni pénurie ni gaspillage, et le bien-être "
  "collectif est maximisé.",
  "L’efficacité économique est le critère par lequel tout le chapitre juge les "
  "marchés, et sa force vient de ce qu’il est à la fois simple et "
  "démontrable. La condition P = Cm s’interprète ainsi : le prix mesure ce que "
  "la dernière unité vaut pour le consommateur, le coût marginal ce qu’elle "
  "coûte à la collectivité ; les égaliser signifie que l’on produit exactement "
  "jusqu’au point où l’unité supplémentaire vaut ce qu’elle coûte. Produire "
  "moins priverait la collectivité d’unités dont la valeur excède le coût, "
  "produire plus ajouterait des unités dont le coût excède la valeur. Cette "
  "situation correspond à la concurrence pure et parfaite, qui sert de "
  "référence théorique : la demande adressée à la firme y étant parfaitement "
  "élastique, prix, recette marginale et coût marginal coïncident. Le cours en "
  "tire une conséquence générale qu’il faut savoir mobiliser : toute structure "
  "de marché qui empêche l’égalité P = Cm conduit à une allocation "
  "sous-optimale. Le monopole en est l’illustration directe, puisqu’il "
  "maximise son profit en égalisant recette marginale et coût marginal, ce qui "
  "conduit à P supérieur au coût marginal, une quantité plus faible et des "
  "prix plus élevés. Les défaillances de marché produisent le même résultat "
  "par d’autres voies : une défaillance est précisément une situation dans "
  "laquelle le marché concurrentiel n’arrive pas à allouer de façon optimale "
  "les ressources, c’est-à-dire où l’on produit trop ou pas assez, trop cher "
  "ou pas assez cher. Deux précautions s’imposent. La première est que "
  "l’efficacité n’est pas la justice : le critère de Pareto, qui lui "
  "correspond, ne dit rien sur l’égalité ni sur la morale. La seconde est que "
  "l’efficacité statique n’est pas l’efficacité dynamique : Schumpeter "
  "soutient que le monopole temporaire peut être plus favorable à l’innovation "
  "que la concurrence parfaite, ce qui oppose deux conceptions du résultat à "
  "atteindre.",
  [("L’égalisation de la valeur et du coût à la marge",
    "Le prix mesure la valeur de la dernière unité pour le consommateur et le "
    "coût marginal ce qu’elle coûte à produire : leur égalité signifie qu’on "
    "ne peut plus gagner en modifiant la quantité produite."),
   ("La maximisation du surplus total",
    "À l’optimum, la somme des surplus du consommateur et du producteur est "
    "maximale : tout écart à P = Cm détruit du surplus, ce qui fournit la "
    "mesure du coût de l’inefficacité."),
   ("L’absence de pénurie et de gaspillage",
    "La quantité produite correspond exactement à ce que les agents "
    "souhaitent échanger à ce prix : aucune ressource n’est employée à "
    "produire ce que personne ne veut, et rien de désiré ne manque."),
   ("L’effet du pouvoir de marché",
    "Lorsque la firme fait face à une demande décroissante, elle maximise son "
    "profit en égalisant recette marginale et coût marginal, ce qui laisse le "
    "prix au-dessus du coût marginal et la quantité en dessous de l’optimum."),
   ("La distinction entre efficacité statique et dynamique",
    "L’efficacité statique juge l’allocation à un instant donné ; l’efficacité "
    "dynamique juge la capacité du système à innover, et les deux peuvent "
    "appeler des structures de marché opposées.")],
  [{'a': "Le critère P = Cm est opératoire : il permet de dire si une "
         "situation est efficace sans avoir à comparer toutes les allocations "
         "possibles.",
    'cond': "Il suppose que le coût marginal privé reflète bien le coût social, "
            "donc l’absence de toute externalité.",
    'lim': "En présence d’externalité négative, la courbe de coût marginal "
           "social se situe au-dessus de la courbe de coût marginal privé, de "
           "sorte que P = Cm privé n’est plus efficace."},
   {'a': "Il fournit une justification précise de l’intervention publique, "
         "fondée sur l’efficacité et non sur l’équité.",
    'cond': "L’intervention est justifiée lorsqu’une défaillance identifiable "
            "empêche l’égalité, et doit viser à la rétablir.",
    'lim': "Dans le cas du monopole naturel, aucune solution ne rétablit "
           "simplement l’égalité : à P = Cm l’entreprise ne couvre pas ses "
           "coûts fixes et subit des pertes."},
   {'a': "Il relie structure de marché et performance, ce qui permet de "
         "classer les situations par leur degré d’inefficacité.",
    'cond': "Le classement suppose que l’on observe l’écart entre prix et coût "
            "marginal, ce qui est rarement direct.",
    'lim': "Le modèle SCP montre que la structure détermine les comportements "
           "puis les performances, mais la causalité peut aussi s’inverser, "
           "les performances modifiant la structure."},
   {'a': "Il offre un langage commun pour discuter des politiques "
         "commerciales, environnementales et de concurrence.",
    'cond': "L’usage transversal suppose que les pertes sèches soient "
            "identifiées dans chaque cas, ce que le cours fait pour le droit "
            "de douane.",
    'lim': "Il reste indifférent à la répartition, alors que les politiques "
           "sont le plus souvent discutées sur ce terrain."}],
  [{'t': "L’efficacité n’est pas la justice : une allocation parfaitement "
         "efficace peut être extrêmement inégale.",
    'qui': "La lecture du critère de Pareto que le cours propose "
           "explicitement.",
    'rep': "L’objection est exacte et le cours l’énonce lui-même : c’est un "
           "critère d’efficacité et non de justice, qui ne dit rien sur "
           "l’égalité ni sur la morale."},
   {'t': "Le monopole temporaire peut être plus favorable à l’innovation que "
         "la concurrence parfaite.",
    'qui': "Joseph Schumpeter, dont le cours expose la deuxième rupture avec "
           "la théorie standard.",
    'rep': "L’argument oppose efficacité dynamique et efficacité statique : "
           "l’innovation coûte cher, est risquée et ne peut être copiée "
           "immédiatement sans décourager l’innovateur, d’où la nécessité d’un "
           "avantage provisoire."},
   {'t': "La condition P = Cm est inapplicable dans certains secteurs, où elle "
         "conduit l’entreprise à la faillite.",
    'qui': "L’analyse du monopole naturel, où les coûts fixes sont très élevés "
           "et les coûts marginaux très faibles.",
    'rep': "L’objection est structurelle et le cours en tire la conclusion : "
           "le marché ne peut pas résoudre seul ce problème, d’où la "
           "nécessité d’une nationalisation, d’une régulation des prix ou de "
           "subventions permettant P = Cm."},
   {'t': "Le critère suppose des agents capables de maximiser, hypothèse "
         "comportementale que rien ne vient confirmer.",
    'qui': "Herbert Simon, avec la rationalité limitée.",
    'rep': "La critique affaiblit la portée descriptive du critère sans en "
           "détruire l’usage normatif : il reste possible de juger une "
           "allocation même si les agents ne l’atteignent pas spontanément."}],
  [{'n': "Arthur Pigou",
    'i': "Analyser le bien-être consiste à chercher la situation qui maximise "
         "l’utilité collective.",
    'p': "Le cours le présente comme le fondateur de l’économie du bien-être, "
         "libéral mais convaincu qu’il existe des situations où le marché est "
         "défaillant et où l’État est légitime pour intervenir. L’efficacité "
         "devient alors un objectif de politique publique et non un simple "
         "constat."},
   {'n': "Vilfredo Pareto",
    'i': "Une situation est optimale lorsqu’on ne peut améliorer le sort de "
         "l’un sans détériorer celui d’un autre.",
    'p': "Son critère donne à l’efficacité une définition qui ne dépend "
         "d’aucune comparaison interpersonnelle d’utilité, mais le cours en "
         "souligne la contrepartie : il est muet sur l’égalité et sur la "
         "morale."},
   {'n': "Joseph Schumpeter",
    'i': "La concurrence parfaite n’est pas toujours la structure la plus "
         "favorable au progrès.",
    'p': "Le cours en fait sa deuxième rupture avec la théorie standard : le "
         "monopole temporaire peut être plus favorable à l’innovation que la "
         "concurrence parfaite, car il permet de rentabiliser dépenses de "
         "recherche, prises de risque et efforts d’organisation."},
   {'n': "Joe Bain",
    'i': "La structure du marché détermine les comportements des firmes, qui "
         "déterminent ensuite leurs performances.",
    'p': "Avec Edward Mason, il construit dans les années 1950 le modèle SCP, "
         "à partir d’analyses historiques des marchés américains. Le modèle "
         "fournit la chaîne causale qui relie l’organisation d’un marché à son "
         "efficacité constatée."}],
  [{'f': "Le cours énonce la condition fondamentale d’efficacité : prix égal "
         "au coût marginal.",
    'p': "La formule est le pivot de tout le chapitre, et son énoncé doit "
         "précéder toute discussion d’une structure de marché particulière."},
   {'f': "Lorsque P = Cm est respectée, la quantité produite est optimale, le "
         "surplus total est maximal, il n’y a ni pénurie ni gaspillage et le "
         "bien-être collectif est maximisé.",
    'p': "Les quatre conséquences énumérées par le cours montrent que la "
         "condition résume à elle seule plusieurs propriétés distinctes de "
         "l’allocation."},
   {'f': "Toute structure de marché qui empêche l’égalité P = Cm conduit à une "
         "allocation sous-optimale.",
    'p': "L’énoncé donne la règle générale qui permet de traiter d’un seul "
         "mouvement monopole, oligopole et concurrence monopolistique."},
   {'f': "Une défaillance de marché est une situation dans laquelle on produit "
         "trop ou pas assez, trop cher ou pas assez cher.",
    'p': "La définition du cours montre que l’inefficacité peut porter sur la "
         "quantité comme sur le prix, et qu’elle peut aller dans les deux sens."}],
  [{'q': "Sujet du type « Qu’est-ce qu’une allocation efficace des "
         "ressources ? »",
    'f': "Une allocation est efficace lorsque les ressources sont utilisées de "
         "manière optimale, ce que la microéconomie traduit par une condition "
         "précise : prix égal au coût marginal. Lorsqu’elle est respectée, la "
         "quantité produite est optimale, le surplus total est maximal, il n’y "
         "a ni pénurie ni gaspillage et le bien-être collectif est maximisé. "
         "Cette situation correspond à la concurrence pure et parfaite, qui "
         "sert de référence théorique.",
    'r': "Le raisonnement part d’une définition opératoire plutôt que d’une "
         "intuition, ce qui permet ensuite de démontrer l’inefficacité de "
         "chaque structure de marché au lieu de l’affirmer.",
    'ex': "Le monopole, qui égalise recette marginale et coût marginal et "
          "laisse donc le prix au-dessus du coût marginal."},
   {'q': "Sujet du type « Faut-il préférer la concurrence ou l’innovation ? »",
    'f': "Les deux objectifs peuvent appeler des structures de marché "
         "opposées. L’efficacité statique exige P = Cm, donc la concurrence "
         "pure et parfaite. Mais Schumpeter soutient que la concurrence "
         "parfaite n’est pas toujours la structure la plus favorable au "
         "progrès : l’innovation coûte cher, est risquée et ne peut être "
         "copiée immédiatement sans décourager l’innovateur, de sorte qu’il "
         "faut parfois laisser à l’innovateur une position dominante "
         "temporaire.",
    'r': "Le raisonnement oppose deux critères d’efficacité, l’un statique et "
         "l’autre dynamique, ce qui permet de montrer que le débat ne porte "
         "pas sur le niveau d’exigence mais sur l’horizon retenu.",
    'ex': "Le brevet, droit de propriété intellectuelle qui donne une "
          "exclusivité d’exploitation pour une durée maximale de vingt ans sur "
          "un territoire donné."}],
  voisins=['n5-pareto', 'n5-cpp', 'n5-surplus', 'n5-monopole'])


d('n5-pareto', 5, "Optimum de Pareto",
  "Un critère d’efficacité sans jugement sur la justice",
  "Une situation est Pareto-optimale si l’on ne peut pas améliorer la "
  "situation de quelqu’un sans détériorer celle d’un autre : tout le monde est "
  "au mieux compte tenu des autres, et l’on ne peut plus faire mieux sans "
  "faire pire ailleurs. Le cours insiste sur la nature exacte du critère : "
  "c’est un critère d’efficacité, pas de justice.",
  "L’optimum de Pareto est un concept dont la puissance tient précisément à sa "
  "modestie, et c’est ce paradoxe qu’une bonne copie doit exposer. Son origine "
  "est la formalisation d’une affirmation de Walras : si tous les marchés sont "
  "en équilibre en même temps, alors la situation est optimale. Pareto "
  "transforme cette intuition en critère vérifiable, qui présente deux "
  "avantages décisifs. Premier avantage, il n’exige aucune comparaison "
  "interpersonnelle d’utilité : il ne demande pas de mesurer le bonheur des "
  "uns et des autres, mais seulement de savoir s’il existe un changement qui "
  "profite à l’un sans nuire à personne. Second avantage, il est "
  "unanimement acceptable : un changement qui améliore la situation de "
  "quelqu’un sans détériorer celle d’un autre ne peut être refusé par "
  "personne. Mais cette modestie est aussi la limite du critère, et le cours "
  "l’énonce sans ambiguïté : il ne dit rien sur l’égalité, rien sur la morale, "
  "il dit juste qu’on ne peut plus améliorer sans coût. Une répartition "
  "extrêmement inégale peut donc être Pareto-optimale, dès lors que toute "
  "redistribution détériorerait la situation de quelqu’un. Le critère est "
  "ensuite pris dans la série des difficultés qui touchent l’équilibre "
  "général, puisqu’il en est l’évaluation. Arrow et Debreu montrent que "
  "l’équilibre existe mais sous des hypothèses irréalistes, dont la dotation "
  "de survie qui suppose une intervention extérieure au marché. Sonnenschein, "
  "Mantel et Debreu montrent que même s’il existe, rien ne garantit qu’on y "
  "arrive ni qu’on y reste. Le cours résume cette superposition en montrant "
  "que l’optimum ainsi défini est théoriquement possible, pratiquement "
  "inaccessible et mathématiquement instable. L’optimum de Pareto reste donc "
  "un instrument indispensable de raisonnement, à condition de ne jamais "
  "confondre l’efficacité qu’il mesure avec la désirabilité de la situation "
  "qu’il qualifie.",
  [("La définition par l’impossibilité d’améliorer sans nuire",
    "Une situation est optimale au sens de Pareto lorsqu’aucun changement ne "
    "peut profiter à quelqu’un sans faire perdre quelqu’un d’autre : "
    "l’optimalité se définit donc par l’épuisement des gains mutuels."),
   ("L’absence de comparaison interpersonnelle",
    "Le critère ne demande pas de mesurer ni de comparer les utilités : il lui "
    "suffit de constater un gain pour l’un et l’absence de perte pour les "
    "autres, ce qui le rend applicable sans hypothèse sur le bonheur."),
   ("L’unanimité comme fondement",
    "Une amélioration au sens de Pareto ne peut être refusée par personne, "
    "puisque nul n’y perd : le critère tire sa légitimité de cette unanimité "
    "potentielle plutôt que d’un jugement de valeur."),
   ("L’indifférence à la répartition",
    "Comme toute redistribution détériore la situation de celui qui donne, une "
    "répartition très inégale peut être optimale : le critère ne hiérarchise "
    "donc pas les répartitions entre elles."),
   ("Le lien avec l’équilibre général",
    "L’optimum de Pareto est l’évaluation de l’équilibre walrassien : il "
    "hérite donc de toutes les difficultés qui touchent l’existence et la "
    "stabilité de cet équilibre.")],
  [{'a': "Le critère permet de juger une situation sans avoir à mesurer ni "
         "comparer les utilités individuelles.",
    'cond': "Il suppose seulement que l’on sache si un agent est mieux ou moins "
            "bien qu’avant, et non de combien.",
    'lim': "Cette économie de moyens se paie en pouvoir de discrimination : "
           "une grande partie des situations possibles sont toutes "
           "Pareto-optimales et donc incomparables entre elles."},
   {'a': "Il fournit le fondement théorique de la thèse selon laquelle la "
         "concurrence pure et parfaite est efficace.",
    'cond': "Le lien suppose que tous les marchés soient en équilibre "
            "simultanément, comme le pose Walras.",
    'lim': "Rien ne garantit la réalisation de cet équilibre général : "
           "Sonnenschein, Mantel et Debreu montrent qu’il n’y a aucune raison "
           "qu’on y arrive ni qu’on y reste."},
   {'a': "Il clarifie les débats de politique économique en séparant ce qui "
         "relève de l’efficacité de ce qui relève de la redistribution.",
    'cond': "La clarification n’est utile que si l’on reconnaît explicitement "
            "que la seconde question n’est pas traitée par le critère.",
    'lim': "Utilisé sans cette précaution, il peut faire passer un choix de "
           "répartition pour une exigence technique."},
   {'a': "Il peut être appliqué à des contextes très divers, du marché des "
         "biens aux politiques commerciales.",
    'cond': "L’application suppose que les effets sur les tiers soient "
            "intégrés, donc l’absence d’externalité non corrigée.",
    'lim': "En présence d’externalités, le prix de marché ne reflète pas le "
           "coût social, et l’optimalité calculée sur les coûts privés est "
           "illusoire."}],
  [{'t': "Le critère est entièrement muet sur la justice : il ne dit rien "
         "sur l’égalité, ni sur la morale.",
    'qui': "La limite que le cours énonce lui-même à propos du critère de "
           "Pareto.",
    'rep': "L’objection est inscrite dans la définition et doit être assumée "
           "plutôt que combattue : le critère dit seulement qu’on ne peut plus "
           "améliorer sans coût."},
   {'t': "L’équilibre dont l’optimum est l’évaluation n’existe que sous des "
         "hypothèses irréalistes.",
    'qui': "Kenneth Arrow et Gérard Debreu.",
    'rep': "La critique atteint indirectement le critère : si l’équilibre "
           "général suppose une dotation de survie assurée par une "
           "intervention extérieure, l’optimalité qu’on lui attribue n’est pas "
           "le produit du seul marché."},
   {'t': "Même si l’optimum existe, rien ne garantit que le système y parvienne "
         "ni qu’il y demeure.",
    'qui': "Hugo Sonnenschein, Rolf Mantel et Gérard Debreu.",
    'rep': "Le résultat est décisif pour l’usage politique du critère : on ne "
           "peut pas invoquer l’optimalité d’un équilibre dont on ne sait pas "
           "s’il sera atteint."},
   {'t': "Le critère suppose des agents capables d’optimiser, ce que la "
         "psychologie des décisions démentit.",
    'qui': "Herbert Simon, avec la rationalité limitée.",
    'rep': "L’objection porte sur la réalisation et non sur la définition : le "
           "critère reste un étalon de jugement même si aucun agent ne se "
           "comporte comme il le suppose."}],
  [{'n': "Vilfredo Pareto",
    'i': "Une situation est optimale lorsqu’on ne peut améliorer la situation "
         "de quelqu’un sans détériorer celle d’un autre.",
    'p': "Le cours précise la portée exacte du critère : tout le monde est au "
         "mieux compte tenu des autres, et il s’agit d’un critère "
         "d’efficacité et non de justice, qui ne dit rien sur l’égalité ni sur "
         "la morale."},
   {'n': "Léon Walras",
    'i': "Si tous les marchés sont en équilibre en même temps, alors la "
         "situation est optimale.",
    'p': "Le cours fait de cette affirmation le point de départ que Pareto "
         "formalise : l’optimum de Pareto est donc d’abord l’évaluation de "
         "l’équilibre général walrassien, dont il hérite les difficultés."},
   {'n': "Kenneth Arrow",
    'i': "L’existence de l’équilibre général repose sur sept conditions "
         "précises, dont plusieurs sont irréalistes.",
    'p': "Avec Debreu, il montre qu’il faut notamment la rationalité, la "
         "concurrence pure et parfaite, des marchés complets et une dotation "
         "de survie. Cette dernière suppose une intervention extérieure au "
         "marché, ce qui contredit l’idée que le marché se suffit à lui-même."},
   {'n': "Hugo Sonnenschein",
    'i': "L’existence de l’équilibre ne garantit ni sa stabilité ni la "
         "convergence du système vers lui.",
    'p': "Avec Mantel et Debreu, il montre qu’une fonction de demande globale "
         "peut avoir n’importe quelle forme, être croissante ou chaotique : la "
         "microéconomie propre ne garantit donc pas une macroéconomie propre, "
         "et l’optimum peut rester hors d’atteinte."}],
  [{'f': "Le cours formule le critère ainsi : une situation est "
         "Pareto-optimale si l’on ne peut pas améliorer la situation de "
         "quelqu’un sans détériorer celle d’un autre.",
    'p': "La formulation est à citer telle quelle, car toute reformulation "
         "approximative conduit à confondre optimalité et désirabilité."},
   {'f': "Le cours précise que c’est un critère d’efficacité, pas de justice, "
         "qu’il ne dit rien sur l’égalité ni sur la morale, et qu’il dit juste "
         "qu’on ne peut plus améliorer sans coût.",
    'p': "La précision est l’élément le plus utile du dossier : elle fournit "
         "la limite du critère en même temps que sa définition."},
   {'f': "Pareto formalise une affirmation de Walras selon laquelle "
         "l’équilibre simultané de tous les marchés est optimal.",
    'p': "La filiation montre que l’optimum n’est pas un critère indépendant "
         "mais l’évaluation d’un état précis du système, celui d’équilibre "
         "général."},
   {'f': "Le cours conclut que l’on obtient un équilibre théoriquement "
         "possible, pratiquement inaccessible et mathématiquement instable.",
    'p': "La conclusion vise l’équilibre mais atteint l’optimum qui lui est "
         "attaché : elle interdit d’invoquer l’optimalité comme une propriété "
         "effective des économies de marché."}],
  [{'q': "Sujet du type « L’efficacité économique est-elle un critère "
         "suffisant ? »",
    'f': "Le critère de Pareto en montre les limites de la façon la plus "
         "nette. Une situation est optimale lorsqu’on ne peut améliorer la "
         "situation de quelqu’un sans détériorer celle d’un autre : c’est un "
         "critère d’efficacité et non de justice, qui ne dit rien sur "
         "l’égalité ni sur la morale et affirme seulement qu’on ne peut plus "
         "améliorer sans coût. Une répartition très inégale peut donc être "
         "Pareto-optimale.",
    'r': "Le raisonnement montre que l’insuffisance du critère n’est pas un "
         "défaut mais une propriété voulue : c’est en renonçant à juger la "
         "répartition qu’il acquiert son caractère incontestable.",
    'ex': "Toute redistribution détériore la situation de celui qui donne, de "
          "sorte qu’elle ne constitue jamais une amélioration au sens de "
          "Pareto."},
   {'q': "Sujet du type « Le marché conduit-il à l’optimum ? »",
    'f': "Walras affirme que si tous les marchés sont en équilibre en même "
         "temps la situation est optimale, et Pareto formalise cette "
         "optimalité. Mais trois critiques superposées ruinent la conclusion "
         "pratique. Arrow et Debreu montrent que l’équilibre existe sous des "
         "hypothèses irréalistes, dont une dotation de survie qui suppose une "
         "intervention extérieure au marché. Sonnenschein, Mantel et Debreu "
         "montrent qu’il n’y a aucune raison qu’on y arrive ni qu’on y reste. "
         "Simon ajoute que les agents réels n’en sont pas capables.",
    'r': "Le raisonnement distingue l’optimalité comme propriété théorique "
         "d’un état et l’optimalité comme résultat effectif d’un processus, "
         "distinction qui règle la question.",
    'ex': "La dotation de survie, qui suppose État, Église ou institutions, et "
          "contredit l’idée que le marché se suffit à lui-même."}],
  voisins=['n5-efficacite', 'n5-equilibre', 'n5-surplus', 'n5-cpp'])


d('n5-monopole', 5, "Monopole",
  "Un seul vendeur, un prix supérieur au coût marginal, une perte sèche",
  "Un monopole est une situation de marché dans laquelle une seule entreprise "
  "produit et vend un bien ou un service, sans substitut proche, le "
  "monopoleur étant price maker. Il maximise son profit en égalisant recette "
  "marginale et coût marginal, ce qui conduit à un prix supérieur au coût "
  "marginal et à une quantité plus faible que la quantité socialement "
  "optimale.",
  "Le monopole est traité par le cours avec une nuance qu’il faut absolument "
  "restituer : à la question de savoir s’il est toujours une défaillance de "
  "marché, la réponse est non. Le mécanisme d’abord. Le monopoleur fait face à "
  "une demande décroissante, et non parfaitement élastique comme en "
  "concurrence pure et parfaite. Il choisit donc le couple prix-quantité qui "
  "maximise son profit, selon la règle Rm = Cm, et fixe son prix en fonction "
  "de la disposition à payer des consommateurs plutôt que de son coût "
  "marginal. Les conséquences sont au nombre de quatre : réduction du surplus "
  "du consommateur, apparition d’une rente de monopole, perte sèche — le "
  "triangle d’Harberger — et allocation sous-optimale des ressources. Mais le "
  "cours distingue ensuite plusieurs types de monopoles qui n’ont ni les mêmes "
  "causes ni les mêmes effets. Le monopole naturel est la véritable "
  "défaillance de marché : il apparaît lorsque les coûts fixes sont très "
  "élevés, les coûts marginaux très faibles et les rendements croissants, de "
  "sorte qu’une seule entreprise produit à moindre coût que plusieurs — eau, "
  "électricité, gaz, chemins de fer, télécommunications, réseaux. Le blocage y "
  "est structurel : à P = Cm l’entreprise ne couvre pas ses coûts fixes et "
  "subit des pertes, à P supérieur au coût marginal elle survit mais le prix "
  "est trop élevé et la quantité trop faible ; le marché ne peut pas résoudre "
  "seul ce problème, d’où nationalisation, régulation des prix par des prix "
  "plafonds, tarification au coût moyen ou subventions permettant P = Cm. Le "
  "monopole d’innovation est au contraire acceptable mais doit rester "
  "temporaire : protégé par un brevet, exclusivité d’exploitation d’une durée "
  "maximale de vingt ans sur un territoire donné, il incite à innover et "
  "finance la R&D, Schumpeter soutenant que la concurrence doit être la règle "
  "mais que l’innovation doit être protégée. Enfin les monopoles de réseau, où "
  "l’utilité du service augmente avec le nombre d’utilisateurs, combinent "
  "efficacité et standardisation avec des risques de verrouillage du marché.",
  [("La demande décroissante et le pouvoir sur le prix",
    "Seul sur son marché, le monopoleur n’est plus confronté à une demande "
    "parfaitement élastique : il peut augmenter son prix sans perdre toute sa "
    "clientèle, ce qui le rend price maker."),
   ("La maximisation du profit par Rm = Cm",
    "Le monopoleur choisit la quantité qui égalise recette marginale et coût "
    "marginal. Comme la recette marginale est inférieure au prix sur une "
    "demande décroissante, le prix retenu excède le coût marginal."),
   ("La tarification à la disposition à payer",
    "Le monopoleur observe la demande, connaît le prix maximum que les "
    "consommateurs acceptent et fixe son prix en fonction de cette "
    "disposition à payer, et non du coût de production."),
   ("La réduction de la quantité et la perte sèche",
    "La quantité produite est inférieure à la quantité socialement optimale : "
    "une partie des échanges mutuellement avantageux n’a pas lieu, ce qui "
    "constitue une perte nette de bien-être, le triangle d’Harberger."),
   ("Le blocage spécifique du monopole naturel",
    "Avec des coûts fixes très élevés et des coûts marginaux très faibles, "
    "aucun prix ne permet à la fois l’efficacité et la viabilité : à P = Cm "
    "l’entreprise perd de l’argent, au-dessus elle survit mais produit trop "
    "peu.")],
  [{'a': "Le monopole naturel permet de produire à moindre coût qu’une "
         "pluralité d’entreprises, grâce aux rendements croissants.",
    'cond': "L’avantage suppose des coûts fixes élevés et des coûts marginaux "
            "faibles, caractéristiques des réseaux.",
    'lim': "Cette supériorité de coût ne se traduit pas en prix bas sans "
           "intervention, puisque l’entreprise reste incitée à fixer un prix "
           "supérieur au coût marginal."},
   {'a': "Le monopole temporaire d’innovation incite à innover, permet de "
         "financer la R&D et favorise le progrès technique.",
    'cond': "La justification suppose que le monopole reste temporaire : "
            "Schumpeter ne défend pas le monopole permanent mais un avantage "
            "provisoire qui récompense l’innovation.",
    'lim': "Le cours en relève les aspects négatifs : prix élevés, accès "
           "limité aux innovations comme pour les médicaments, ralentissement "
           "possible de la diffusion, stratégies de verrouillage par brevets "
           "abusifs."},
   {'a': "Les monopoles de réseau apportent efficacité, standardisation et "
         "innovation rapide, l’utilité du service augmentant avec le nombre "
         "d’utilisateurs.",
    'cond': "Le bénéfice suppose que l’effet de réseau profite effectivement "
            "aux utilisateurs et ne serve pas seulement à les retenir.",
    'lim': "Les risques énumérés sont lourds : domination durable, "
           "verrouillage du marché, abus de position dominante, exploitation "
           "des données."},
   {'a': "La réponse publique est identifiée et graduée, de la nationalisation "
         "à la tarification réglementée.",
    'cond': "Chaque solution a son coût : la tarification au coût moyen écarte "
            "de l’optimum, la subvention pèse sur le budget.",
    'lim': "Le cours rappelle les limites du monopole public : manque "
           "d’efficacité, absence de concurrence donc pas forcément "
           "d’innovation, risques de bureaucratie et défaillance de l’État."}],
  [{'t': "Le monopole n’est pas automatiquement une défaillance de marché, "
         "et ne doit donc pas être condamné en bloc.",
    'qui': "Le cours lui-même, qui répond explicitement non à cette question.",
    'rep': "La réponse est juste et structure tout le dossier : seul le "
           "monopole naturel constitue une véritable défaillance, par un "
           "blocage structurel que le marché ne peut résoudre seul."},
   {'t': "Le monopole temporaire peut être plus favorable à l’innovation que "
         "la concurrence parfaite.",
    'qui': "Joseph Schumpeter, dans sa deuxième rupture avec la théorie "
           "standard.",
    'rep': "L’argument est solide : si l’entreprise innovante est copiée "
           "instantanément, elle ne peut rentabiliser ses dépenses de "
           "recherche, ses prises de risque et ses efforts d’organisation."},
   {'t': "La domination d’une entreprise doit s’apprécier à la bonne échelle, "
         "car un acteur dominant localement peut affronter une forte "
         "concurrence mondiale.",
    'qui': "La question de l’échelle de la concurrence que le cours illustre "
           "par le projet de fusion entre Alstom et Siemens.",
    'rep': "L’argument a été avancé par les entreprises elles-mêmes face au "
           "refus de la Commission européenne, qui craignait un monopole en "
           "Europe : l’analyse dépend donc du marché pertinent retenu."},
   {'t': "Ce n’est pas le nombre d’entreprises qui compte mais la possibilité "
         "d’entrer sur le marché.",
    'qui': "William Baumol, avec la théorie des marchés contestables.",
    'rep': "La reformulation est importante : même seule, une entreprise peut "
           "se comporter comme en concurrence si elle craint l’arrivée de "
           "concurrents, ce qui déplace l’analyse vers les barrières à "
           "l’entrée."}],
  [{'n': "Joseph Schumpeter",
    'i': "La concurrence doit être la règle, mais l’innovation doit être "
         "protégée.",
    'p': "Le cours en fait la justification théorique du monopole temporaire : "
         "l’innovation coûte cher, est risquée, exige des investissements et "
         "ne peut être copiée immédiatement sans décourager l’innovateur. "
         "Schumpeter ne défend pas le monopole permanent mais un avantage "
         "provisoire."},
   {'n': "Arthur Pigou",
    'i': "Le marché est parfois défaillant, et l’État est alors légitime pour "
         "intervenir.",
    'p': "Le cours le présente comme successeur de Marshall et fondateur de "
         "l’économie du bien-être. Le monopole naturel est le cas type où son "
         "argument s’applique, puisque le marché ne peut pas résoudre seul le "
         "blocage entre efficacité et viabilité."},
   {'n': "William Baumol",
    'i': "Même seule sur son marché, une entreprise peut se comporter comme si "
         "elle était en concurrence.",
    'p': "Sa théorie des marchés contestables, développée avec Panzar et "
         "Willig dans les années 1980, déplace le critère du nombre "
         "d’entreprises vers la libre entrée et la libre sortie : c’est la "
         "crainte de l’entrée qui discipline le monopoleur."},
   {'n': "Joe Bain",
    'i': "La structure du marché détermine les comportements des entreprises, "
         "qui déterminent leurs performances.",
    'p': "Avec Edward Mason, il formalise le modèle SCP dans les années 1950 à "
         "partir d’analyses historiques des marchés américains. Appliqué au "
         "monopole, le schéma explique pourquoi une structure concentrée "
         "engendre des prix élevés et des profits durables."}],
  [{'f': "Le monopoleur applique la règle Rm = Cm et aboutit à P supérieur au "
         "coût marginal, avec une quantité plus faible que la quantité "
         "socialement optimale.",
    'p': "Le résultat technique est la base de toute démonstration sur le "
         "monopole : il relie le comportement de maximisation à "
         "l’inefficacité constatée."},
   {'f': "Les conséquences du monopole sont la réduction du surplus du "
         "consommateur, l’apparition d’une rente de monopole, une perte sèche "
         "— le triangle d’Harberger — et une allocation sous-optimale.",
    'p': "L’énumération distingue perte, transfert et destruction nette, trois "
         "effets de nature différente qu’il faut éviter de confondre."},
   {'f': "Le monopole naturel apparaît avec des coûts fixes très élevés, des "
         "coûts marginaux très faibles et des rendements croissants ; les "
         "exemples donnés sont l’eau, l’électricité, le gaz, les chemins de "
         "fer, les télécommunications et les réseaux.",
    'p': "La liste permet d’identifier immédiatement les secteurs concernés et "
         "montre que la défaillance est liée à une technologie de production, "
         "non à un comportement."},
   {'f': "Le brevet est un droit de propriété intellectuelle qui donne une "
         "exclusivité d’exploitation pour une durée maximale de vingt ans sur "
         "un territoire donné.",
    'p': "La précision juridique est précieuse : elle montre que le monopole "
         "d’innovation est borné dans le temps et dans l’espace, ce qui "
         "correspond exactement à l’argument de Schumpeter."}],
  [{'q': "Sujet du type « Le monopole est-il nécessairement nuisible ? »",
    'f': "Le cours répond explicitement non. Le monopole conduit certes à P "
         "supérieur au coût marginal, donc à une allocation sous-optimale, "
         "mais il faut distinguer plusieurs types de monopoles qui n’ont ni "
         "les mêmes causes ni les mêmes effets. Le monopole naturel est la "
         "véritable défaillance, par un blocage structurel que le marché ne "
         "peut résoudre seul. Le monopole d’innovation est acceptable mais "
         "doit rester temporaire, puisqu’il incite à innover et finance la "
         "R&D.",
    'r': "Le raisonnement remplace un jugement global par une typologie "
         "assortie de causes distinctes, ce qui permet de conclure "
         "différemment selon le cas examiné.",
    'ex': "Le brevet, qui donne une exclusivité d’exploitation d’une durée "
          "maximale de vingt ans afin de rémunérer l’innovation."},
   {'q': "Sujet du type « Comment réguler un monopole naturel ? »",
    'f': "Le problème est structurel : avec des coûts fixes très élevés et des "
         "coûts marginaux très faibles, à P = Cm l’entreprise ne couvre pas "
         "ses coûts fixes et subit des pertes, tandis qu’à un prix supérieur "
         "elle survit mais le prix est trop élevé et la quantité trop faible. "
         "Le marché ne peut pas résoudre seul ce problème, d’où les solutions "
         "que le cours énumère : nationalisation, régulation des prix par des "
         "prix plafonds, tarification au coût moyen, ou subventions permettant "
         "P = Cm.",
    'r': "Le raisonnement montre que l’intervention n’est pas un choix "
         "idéologique mais la conséquence d’une impossibilité technique, ce "
         "qui est l’argument le plus fort en sa faveur.",
    'ex': "Les réseaux d’eau, d’électricité, de gaz et de chemins de fer, où "
          "une seule entreprise produit à moindre coût que plusieurs."},
   {'q': "Sujet du type « Faut-il démanteler les grandes entreprises ? »",
    'f': "La réponse dépend du marché pertinent retenu, et le cours en donne "
         "une illustration précise. Alstom et Siemens souhaitaient "
         "fusionner ; la Commission européenne a refusé en invoquant un risque "
         "de monopole en Europe, mais les entreprises répondaient que leur "
         "marché est mondial et qu’elles doivent affronter les groupes "
         "chinois. Une entreprise peut donc être dominante localement tout en "
         "restant confrontée à une forte concurrence mondiale.",
    'r': "Le raisonnement montre que la définition du marché précède le "
         "diagnostic de pouvoir de marché, ce qui déplace le débat d’un "
         "jugement sur la taille vers une question de périmètre.",
    'ex': "Le démantèlement de la Standard Oil en 1911, qui illustre à "
          "l’inverse la volonté de limiter les abus lorsque la puissance d’une "
          "firme menace le jeu concurrentiel."}],
  voisins=['n5-cpp', 'n5-pouvoir-marche', 'n5-barrieres', 'n5-discrimination',
           'n5-politique-concurrence'])


d('n5-oligopole', 5, "Oligopole",
  "Peu de producteurs, des décisions interdépendantes, une entente instable",
  "L’oligopole est une structure de marché dans laquelle il y a peu de "
  "producteurs et où chaque entreprise dépend des décisions des autres. Deux "
  "issues sont possibles : la concurrence, qui entraîne une guerre des prix et "
  "des profits faibles, ou la collusion, c’est-à-dire l’entente, qui permet "
  "des prix plus élevés et des profits plus importants.",
  "L’oligopole se distingue des autres structures par une propriété qui change "
  "la nature du raisonnement : l’interdépendance stratégique. En concurrence "
  "pure et parfaite comme en monopole, l’entreprise raisonne sur une courbe de "
  "demande donnée ; en oligopole, le résultat de sa décision dépend de ce que "
  "feront ses rivaux, ce qui fait passer l’analyse de l’optimisation à la "
  "théorie des jeux. Le cours utilise explicitement le dilemme du prisonnier. "
  "Chaque entreprise a individuellement intérêt à tricher pour augmenter ses "
  "gains, de sorte que l’entente est instable : la coopération serait "
  "collectivement préférable, mais la rationalité individuelle pousse à la "
  "défection. L’oligopole fournit donc le cas d’école d’une situation où "
  "l’intérêt individuel ne produit pas le meilleur résultat collectif pour les "
  "participants eux-mêmes, ce qui en fait un pendant exact de la tragédie des "
  "communs. Deux prolongements donnent à la notion toute sa portée. Le premier "
  "est historique et institutionnel : lorsque l’entente parvient à se "
  "maintenir, elle devient un cartel, et le cours en donne un exemple majeur "
  "avec le cartel de Phoebus, qui réunit General Electric, Osram et Philips "
  "de 1929 à 1939, fixe des quotas de production, se répartit géographiquement "
  "les marchés et réduit volontairement la durée de vie des ampoules "
  "d’environ 2000 heures à environ 1000 heures. Le second est "
  "schumpétérien : le développement du capitalisme conduit l’entrepreneur "
  "innovateur à s’effacer au profit des grandes organisations et des "
  "oligopoles, à mesure que les entreprises grossissent, que les marchés se "
  "concentrent et que l’innovation devient plus routinière — évolution "
  "paradoxale, puisque le triomphe du capitalisme affaiblit ce qui faisait sa "
  "force initiale.",
  [("Le petit nombre et l’interdépendance",
    "Avec peu de producteurs, la décision de chacun modifie sensiblement le "
    "marché : chaque entreprise doit donc anticiper les réactions des autres, "
    "ce qui transforme le calcul en problème stratégique."),
   ("L’issue concurrentielle",
    "Si les entreprises se font concurrence, elles entrent en guerre des prix "
    "et leurs profits deviennent faibles : la rivalité détruit la rente que la "
    "structure concentrée rendait possible."),
   ("L’issue collusive",
    "Si elles s’entendent, elles peuvent maintenir des prix plus élevés et "
    "obtenir des profits plus importants : la collusion reproduit, à plusieurs, "
    "le comportement d’un monopoleur."),
   ("L’instabilité de l’entente",
    "Chaque entreprise a individuellement intérêt à tricher pour augmenter ses "
    "gains : la coopération serait collectivement préférable mais la "
    "rationalité individuelle pousse à la défection, exactement comme dans le "
    "dilemme du prisonnier."),
   ("La stabilisation par le cartel",
    "Pour tenir, l’entente doit se doter de règles explicites : quotas de "
    "production et répartition géographique des marchés, ce qui la rend "
    "efficace mais aussi détectable et sanctionnable.")],
  [{'a': "L’oligopole explique les comportements de prix observés dans de "
         "nombreux secteurs, que ni la concurrence parfaite ni le monopole ne "
         "rendent intelligibles.",
    'cond': "L’analyse suppose que le nombre d’acteurs soit assez réduit pour "
            "que chacun observe et anticipe les décisions des autres.",
    'lim': "Elle ne prédit pas une issue unique : selon les circonstances, la "
           "structure peut déboucher sur une guerre des prix ou sur une "
           "entente."},
   {'a': "Il fournit une application directe de la théorie des jeux, en "
         "montrant que la rationalité individuelle peut produire un résultat "
         "collectivement inférieur.",
    'cond': "Le résultat suppose que les entreprises ne puissent pas "
            "s’engager de façon crédible, ce que le cours souligne en "
            "rappelant qu’en microéconomie on n’est pas censé communiquer avec "
            "les autres.",
    'lim': "Dans la réalité, les entreprises communiquent et peuvent établir "
           "des mécanismes de surveillance mutuelle, ce qui stabilise des "
           "ententes que la théorie prédit instables."},
   {'a': "Il concilie grande taille et efficacité, puisque les grandes firmes "
         "permettent l’innovation, les économies d’échelle et la compétitivité "
         "internationale.",
    'cond': "Le bénéfice suppose que la pression concurrentielle subsiste, par "
            "la rivalité entre oligopoleurs ou par la menace d’entrée.",
    'lim': "Les mêmes firmes peuvent au contraire limiter la concurrence, "
           "influencer les prix, constituer des cartels et renforcer leur "
           "pouvoir de marché."},
   {'a': "Il éclaire une dynamique historique de long terme, celle du passage "
         "de l’entrepreneur individuel aux grandes organisations.",
    'cond': "La lecture suppose d’accepter l’analyse schumpétérienne de "
            "l’innovation comme fonction entrepreneuriale.",
    'lim': "Elle conduit Schumpeter à une conclusion pessimiste, le "
           "capitalisme s’affaiblissant parce que son propre développement "
           "modifie les conditions de l’innovation."}],
  [{'t': "L’entente est intrinsèquement instable, puisque chaque participant a "
         "intérêt à tricher.",
    'qui': "L’analyse par le dilemme du prisonnier que le cours applique à "
           "l’oligopole.",
    'rep': "L’argument est théoriquement juste, mais l’exemple du cartel de "
           "Phoebus montre qu’une entente peut durer une décennie lorsqu’elle "
           "se dote de quotas et d’une répartition géographique des marchés."},
   {'t': "La concentration en oligopole est favorable à l’économie, car elle "
         "permet l’innovation et les économies d’échelle.",
    'qui': "L’argument que le cours prête aux grandes firmes, à côté de la "
           "compétitivité internationale.",
    'rep': "Le cours pose immédiatement la contrepartie : les mêmes firmes "
           "peuvent limiter la concurrence, influencer les prix, constituer "
           "des cartels et renforcer leur pouvoir de marché."},
   {'t': "La montée des oligopoles signe l’épuisement progressif du "
         "dynamisme innovateur du capitalisme lui-même.",
    'qui': "Joseph Schumpeter, pour qui les innovateurs disparaissent "
           "progressivement au profit des grandes firmes oligopolistiques.",
    'rep': "La thèse est paradoxale et assumée comme telle : le capitalisme "
           "triomphe, mais ce triomphe affaiblit ce qui faisait sa force "
           "initiale, l’entrepreneur innovateur s’effaçant devant la "
           "bureaucratie."},
   {'t': "Le nombre d’entreprises présentes importe moins, pour juger la "
         "concurrence, que la liberté d’entrée et de sortie.",
    'qui': "William Baumol, avec la théorie des marchés contestables.",
    'rep': "La reformulation s’applique particulièrement à l’oligopole : "
           "quelques entreprises peuvent se comporter concurrentiellement si "
           "elles craignent l’entrée de nouveaux acteurs."}],
  [{'n': "Joseph Schumpeter",
    'i': "Avec le développement du capitalisme, les innovateurs individuels "
         "disparaissent progressivement au profit des grandes firmes "
         "oligopolistiques.",
    'p': "Le cours en fait sa troisième rupture : les entreprises grossissent, "
         "les marchés se concentrent, la bureaucratie s’installe et "
         "l’innovation devient plus routinière, de sorte que le capitalisme "
         "peut s’affaiblir parce que son propre développement modifie les "
         "conditions de l’innovation."},
   {'n': "Edward Chamberlin",
    'i': "La différenciation permet à une entreprise de se comporter comme un "
         "petit monopole sur sa clientèle.",
    'p': "Son analyse éclaire la stratégie des oligopoleurs : plutôt que "
         "d’affronter une guerre des prix, chacun peut chercher à rendre son "
         "produit unique pour réduire l’élasticité de la demande qui lui est "
         "adressée."},
   {'n': "Joe Bain",
    'i': "La structure du marché détermine les comportements, qui déterminent "
         "les performances.",
    'p': "Avec Edward Mason, il formalise le modèle SCP dans les années 1950. "
         "Appliqué à l’oligopole, le schéma explique pourquoi un petit nombre "
         "d’acteurs engendre des comportements de collusion ou de guerre des "
         "prix selon les caractéristiques structurelles du marché."}],
  [{'f': "Le cartel de Phoebus réunit General Electric, Osram et Philips, "
         "principalement de 1929 à 1939.",
    'p': "L’exemple est daté et nommé, ce qui en fait une référence solide : il "
         "montre qu’une entente peut durer et s’organiser à l’échelle "
         "internationale."},
   {'f': "Le cartel fixe des quotas de production et se répartit "
         "géographiquement les marchés, car si la production devient trop "
         "importante l’offre augmente, les prix chutent et les profits "
         "diminuent.",
    'p': "Le raisonnement économique du cartel est explicite : il reproduit la "
         "restriction de quantité du monopoleur, mais par coordination entre "
         "plusieurs firmes."},
   {'f': "Vers 1910 une ampoule pouvait durer environ 2000 heures ; le cartel "
         "de Phoebus décide volontairement de limiter cette durée à environ "
         "1000 heures.",
    'p': "Le chiffre donne un exemple célèbre d’obsolescence programmée et "
         "montre que la collusion peut porter sur la qualité et non seulement "
         "sur le prix."},
   {'f': "Dans un oligopole, deux issues sont possibles : la concurrence, qui "
         "entraîne une guerre des prix et des profits faibles, ou la "
         "collusion, qui permet des prix plus élevés et des profits plus "
         "importants.",
    'p': "L’alternative est la structure même du dossier : elle montre que la "
         "structure de marché ne détermine pas mécaniquement le résultat."}],
  [{'q': "Sujet du type « La concurrence entre quelques grandes firmes "
         "est-elle réelle ? »",
    'f': "L’oligopole admet deux issues opposées, et c’est ce qui rend la "
         "question indécidable a priori. Soit les entreprises se font "
         "concurrence, ce qui entraîne une guerre des prix et des profits "
         "faibles ; soit elles s’entendent, ce qui permet des prix plus élevés "
         "et des profits plus importants. L’entente reste toutefois instable, "
         "chaque entreprise ayant individuellement intérêt à tricher : on "
         "retrouve exactement la logique du dilemme du prisonnier, où la "
         "coopération serait collectivement préférable mais où la rationalité "
         "individuelle pousse à la défection.",
    'r': "Le raisonnement montre que la structure de marché ne détermine pas "
         "le comportement, ce qui justifie une politique de concurrence "
         "attentive aux pratiques plutôt qu’aux seules parts de marché.",
    'ex': "Le cartel de Phoebus, qui a maintenu une entente entre General "
          "Electric, Osram et Philips de 1929 à 1939 grâce à des quotas de "
          "production."},
   {'q': "Sujet du type « L’intérêt individuel conduit-il au meilleur "
         "résultat collectif ? »",
    'f': "L’oligopole fournit un contre-exemple qui vaut même du point de vue "
         "des participants. Dans une entente, chaque entreprise a "
         "individuellement intérêt à tricher pour augmenter ses gains, de "
         "sorte que la coopération serait collectivement préférable mais que "
         "la rationalité individuelle pousse à la défection. Le cours relève "
         "que ce dilemme montre que lorsque les agents ne sont pas coordonnés, "
         "ils font de mauvais choix collectifs.",
    'r': "Le raisonnement est plus fort que celui de la tragédie des communs "
         "sur un point : ici, le résultat est mauvais pour les acteurs "
         "eux-mêmes et pas seulement pour des tiers.",
    'ex': "Le dilemme du prisonnier, que le cours applique explicitement aux "
          "marchés d’oligopole."},
   {'q': "Sujet du type « Le capitalisme épuise-t-il son propre dynamisme ? »",
    'f': "Schumpeter soutient que oui, et l’oligopole est le mécanisme de cet "
         "épuisement. Au début, le capitalisme est porté par des entrepreneurs "
         "audacieux et des innovateurs individuels ; mais à mesure qu’il se "
         "développe, les entreprises grossissent, les marchés se concentrent, "
         "la bureaucratie s’installe et l’innovation devient plus routinière. "
         "L’entrepreneur innovateur s’efface au profit de grandes "
         "organisations et d’oligopoles.",
    'r': "Le raisonnement est dialectique : c’est le succès du système qui "
         "produit les conditions de son affaiblissement, ce qui rapproche "
         "Schumpeter de Marx tout en changeant complètement le mécanisme.",
    'ex': "La formule du cours selon laquelle le capitalisme triomphe, mais ce "
          "triomphe affaiblit ce qui faisait sa force initiale."}],
  voisins=['n5-ententes', 'n5-monopole', 'n5-concentration',
           'n5-politique-concurrence'])
