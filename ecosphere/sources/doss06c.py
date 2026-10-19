# -*- coding: utf-8 -*-
"""Ensemble 6 — Les défaillances du marché et les limites de l’intervention
publique (3/4)."""

from doss_base import d

d('n6-coordination', 6, "Défaillances de coordination",
  "Chacun agit rationnellement et tous perdent, faute de s’être accordés",
  "Une défaillance de coordination désigne la situation dans laquelle des "
  "agents, faute de pouvoir s’accorder, aboutissent collectivement à un "
  "résultat que tous jugent inférieur à celui qu’une action concertée aurait "
  "produit. Le cours en donne la formalisation par le dilemme du prisonnier et "
  "l’applique aussi bien aux marchés d’oligopole qu’à la coopération entre "
  "États.",
  "La défaillance de coordination est le mécanisme qui relie plusieurs "
  "chapitres du programme, et sa force vient de ce qu’elle n’invoque aucune "
  "irrationalité. Le cours en donne d’abord la formalisation : le dilemme du "
  "prisonnier montre que lorsque les gens ne sont pas coordonnés, ils font de "
  "mauvais choix collectifs, et que dans certaines situations la coopération "
  "l’emporte sur le choix égoïste. Le cours ajoute une précision importante "
  "sur le cadre : en microéconomie, on n’est pas censé communiquer avec les "
  "autres, et c’est précisément cette impossibilité de s’engager qui engendre "
  "le résultat sous-optimal. Première application, l’oligopole : il y a peu de "
  "producteurs et chaque entreprise dépend des décisions des autres ; la "
  "concurrence entraîne une guerre des prix et des profits faibles, tandis que "
  "la collusion permettrait des prix plus élevés, mais chaque entreprise a "
  "individuellement intérêt à tricher, de sorte que l’entente est instable. "
  "Deuxième application, les biens publics mondiaux : sans coordination "
  "internationale, chaque État a intérêt à laisser les autres supporter le "
  "coût, d’où un comportement de passager clandestin et un équilibre de Nash "
  "sous-optimal ; la gouvernance internationale trouve là sa justification, "
  "puisqu’elle établit des règles de bonne conduite afin de coordonner les "
  "comportements nationaux. Troisième application, la politique industrielle : "
  "le cours range les défaillances de coordination parmi les motifs "
  "d’intervention publique admis par le raisonnement néoclassique, aux côtés "
  "des externalités, des asymétries d’information et des biens publics. Le "
  "point théorique décisif est que cette défaillance ne tient ni à la nature "
  "du bien, ni à la structure du marché, ni à l’information disponible, mais à "
  "l’absence d’un mécanisme d’engagement crédible : les agents savent ce "
  "qu’il faudrait faire, mais aucun ne peut s’engager à le faire si les autres "
  "ne s’engagent pas aussi.",
  [("L’interdépendance des décisions",
    "Le résultat obtenu par chacun dépend de ce que font les autres : le "
    "calcul individuel ne suffit donc plus, il faut anticiper des "
    "comportements que l’on ne contrôle pas."),
   ("L’impossibilité de s’engager",
    "Faute de communication ou d’engagement crédible, chacun doit choisir sans "
    "savoir ce que feront les autres : la prudence conduit alors à la "
    "stratégie défensive plutôt qu’à la coopération."),
   ("L’équilibre non coopératif",
    "Les choix défensifs se répondent et forment un équilibre : personne n’a "
    "intérêt à en dévier unilatéralement, ce qui rend la situation stable "
    "alors même que tous la jugent inférieure."),
   ("L’écart au résultat coopératif",
    "La coopération serait collectivement préférable, mais la rationalité "
    "individuelle pousse à la défection : l’écart entre les deux résultats "
    "mesure exactement le coût de la défaillance."),
   ("Le rôle des règles comme substitut d’engagement",
    "Une règle extérieure — contrat, loi, accord international — rend "
    "l’engagement crédible et permet d’atteindre le résultat coopératif sans "
    "modifier les préférences des agents.")],
  [{'a': "Le mécanisme explique des résultats collectivement mauvais sans "
         "supposer d’erreur, d’ignorance ou de malveillance.",
    'cond': "Il suppose que la coopération soit effectivement préférable pour "
            "tous, et non seulement pour certains.",
    'lim': "Lorsque les intérêts divergent réellement, le problème n’est plus "
           "de coordination mais de répartition, et la règle ne suffit pas à "
           "le résoudre."},
   {'a': "Il justifie l’existence de règles et d’institutions comme "
         "dispositifs d’engagement, et non comme contraintes arbitraires.",
    'cond': "L’argument suppose que la règle soit crédible, donc assortie "
            "d’une sanction ou d’un mécanisme de vérification.",
    'lim': "À l’échelle internationale, aucune autorité ne peut imposer la "
           "sanction, de sorte que les règles reposent sur des engagements "
           "révocables."},
   {'a': "Il s’applique à des objets très différents, de l’entente entre "
         "firmes à la négociation climatique.",
    'cond': "La transposition suppose que les acteurs soient en nombre réduit "
            "et que leurs décisions soient mutuellement observables.",
    'lim': "Avec un très grand nombre d’acteurs, la logique devient celle du "
           "passager clandestin, où l’abstention de chacun est imperceptible."},
   {'a': "Il figure parmi les motifs d’intervention publique admis par le "
         "raisonnement néoclassique lui-même.",
    'cond': "L’intervention est justifiée lorsqu’elle fournit le mécanisme "
            "d’engagement qui manque, et non lorsqu’elle se substitue au "
            "choix des agents.",
    'lim': "L’État peut lui-même être défaillant, le cours rappelant qu’il "
           "existe des défaillances de l’État, du lobbying et des effets "
           "pervers."}],
  [{'t': "La coordination s’obtient spontanément par le marché, puisque les "
         "prix transmettent l’information nécessaire.",
    'qui': "La logique de la coordination par les prix, que le cours expose à "
           "propos du marché.",
    'rep': "Elle vaut lorsque les décisions sont indépendantes, mais non "
           "lorsqu’elles sont stratégiquement interdépendantes : dans un "
           "oligopole, le prix dépend de ce que fera le rival, qu’aucun prix "
           "n’indique."},
   {'t': "Les acteurs peuvent résoudre eux-mêmes le problème de coordination "
         "en se dotant de règles communes.",
    'qui': "Elinor Ostrom, pour qui les communautés créent leurs propres "
           "règles de gestion.",
    'rep': "Sa démonstration est solide à petite échelle mais le cours en "
           "signale la limite : ses mécanismes sont plus difficiles à "
           "appliquer aux biens communs mondiaux."},
   {'t': "La coordination internationale est illusoire, chaque État "
         "poursuivant son intérêt propre.",
    'qui': "La lecture réaliste que le cours décrit à propos du recul du "
           "multilatéralisme.",
    'rep': "Le constat est en partie vérifié — le multilatéralisme recule au "
           "profit de l’unilatéralisme, du bilatéralisme et de la "
           "régionalisation — mais il décrit le coût de la défaillance plutôt "
           "qu’il ne la réfute."},
   {'t': "La coordination par la hiérarchie est plus efficace que la "
         "coordination par la négociation.",
    'qui': "Alfred Chandler, avec la main visible des managers.",
    'rep': "L’argument vaut à l’intérieur d’une organisation, où l’autorité "
           "fournit l’engagement manquant ; il ne se transpose pas entre "
           "acteurs souverains, où aucune hiérarchie n’existe."}],
  [{'n': "Mancur Olson",
    'i': "Chacun peut avoir intérêt à laisser les autres supporter le coût de "
         "l’action collective.",
    'p': "Son paradoxe fournit la version de la défaillance de coordination "
         "qui joue en grand nombre : l’abstention de chacun étant "
         "imperceptible, la contribution volontaire ne se produit pas, ce qui "
         "explique la sous-production des biens collectifs."},
   {'n': "Elinor Ostrom",
    'i': "Des communautés d’usagers parviennent à se doter de règles qui "
         "résolvent le problème de coordination.",
    'p': "Son apport conteste la fatalité du résultat non coopératif : elle "
         "montre empiriquement que la coopération est possible, que les "
         "individus ne sont pas seulement égoïstes et que la microéconomie "
         "doit intégrer les normes sociales."},
   {'n': "Robert Merton",
    'i': "Une anticipation partagée peut se réaliser par le seul fait d’être "
         "partagée.",
    'p': "Le cours mobilise ses prophéties autoréalisatrices juste après le "
         "dilemme du prisonnier, pour montrer que les comportements "
         "économiques ne sont pas seulement déterminés par les calculs "
         "rationnels mais aussi par les croyances collectives."},
   {'n': "Alfred Chandler",
    'i': "La main visible de la gestion remplace la main invisible du marché "
         "dans la coordination des flux de marchandises.",
    'p': "Sa thèse montre qu’une solution au problème de coordination consiste "
         "à internaliser les décisions interdépendantes dans une même "
         "organisation, où la hiérarchie fournit l’engagement que la "
         "négociation ne permettait pas."}],
  [{'f': "Le cours tire du dilemme du prisonnier deux enseignements : lorsque "
         "les gens ne sont pas coordonnés ils font de mauvais choix "
         "collectifs, et dans certaines situations la coopération l’emporte "
         "sur le choix égoïste.",
    'p': "Les deux formulations sont directement citables et résument "
         "l’apport du mécanisme à l’analyse économique."},
   {'f': "Le cours précise qu’en microéconomie on n’est pas censé communiquer "
         "avec les autres.",
    'p': "La remarque identifie la cause exacte du résultat sous-optimal : ce "
         "n’est pas l’égoïsme mais l’impossibilité de s’engager qui produit la "
         "défaillance."},
   {'f': "Sans coordination internationale, chaque État a intérêt à laisser "
         "les autres supporter le coût, ce qui conduit à un équilibre de Nash "
         "sous-optimal.",
    'p': "La référence à l’équilibre de Nash établit que le mauvais résultat "
         "est stable, ce qui explique qu’il persiste malgré un accord général "
         "sur l’objectif."},
   {'f': "Le cours range les défaillances de coordination parmi les motifs "
         "d’intervention publique admis par le raisonnement néoclassique, avec "
         "les externalités, les asymétries d’information et les biens publics.",
    'p': "Le classement montre que l’intervention pour coordination est "
         "justifiée à l’intérieur même du cadre théorique le plus favorable au "
         "marché."}],
  [{'q': "Sujet du type « Faut-il coordonner les décisions économiques ? »",
    'f': "La coordination devient nécessaire dès que les décisions sont "
         "interdépendantes. Le dilemme du prisonnier le démontre : lorsque les "
         "gens ne sont pas coordonnés, ils font de mauvais choix collectifs, "
         "et dans certaines situations la coopération l’emporte sur le choix "
         "égoïste. Le cours relie ce mécanisme à l’oligopole, où chaque "
         "entreprise a intérêt à tricher, et aux biens publics mondiaux, où "
         "chaque État a intérêt à laisser les autres supporter le coût, d’où "
         "un équilibre de Nash sous-optimal.",
    'r': "Le raisonnement montre que la défaillance tient à l’impossibilité "
         "de s’engager et non aux préférences des agents, ce qui désigne "
         "immédiatement le remède : une règle qui rende l’engagement "
         "crédible.",
    'ex': "La gouvernance internationale, qui établit des règles de bonne "
          "conduite afin de coordonner les comportements nationaux."},
   {'q': "Sujet du type « Quels motifs justifient l’intervention de "
         "l’État ? »",
    'f': "Le cours en énumère quatre, admis par le raisonnement néoclassique "
         "lui-même : les externalités, les asymétries d’information, les biens "
         "publics et les défaillances de coordination. Le dernier est le moins "
         "souvent mobilisé et le plus utile, car il justifie une intervention "
         "qui ne corrige aucun prix et n’ajoute aucune ressource : elle "
         "fournit seulement l’engagement crédible qui manquait aux agents.",
    'r': "Le raisonnement distingue quatre causes de défaillance appelant "
         "quatre types d’action, ce qui évite de traiter l’intervention "
         "publique comme un bloc indifférencié.",
    'ex': "La politique industrielle horizontale, que l’Europe justifie "
          "précisément par les externalités, les asymétries d’information, les "
          "biens publics et les défaillances de coordination."}],
  voisins=['n6-passager-clandestin', 'n5-oligopole', 'n6-biens-collectifs',
           'n6-defaillances-etat'])


d('n6-reglementation', 6, "Réglementation",
  "Imposer directement la règle, avec la garantie et les défauts qui en découlent",
  "La réglementation est l’action par les règles : l’État impose directement "
  "des normes et des interdictions pour encadrer les comportements. Le cours "
  "en fait la première des trois grandes familles de solutions aux "
  "défaillances de marché, devant l’action par les prix de Pigou et l’action "
  "par les quantités de Coase, et en énumère les limites : peu incitative, "
  "sensible au lobbying, peu flexible, contournable et pas toujours efficace "
  "économiquement.",
  "La réglementation est l’instrument le plus immédiat et le moins "
  "satisfaisant économiquement, ce qui en fait un excellent objet de "
  "discussion. Son principe est de prescrire le comportement plutôt que de "
  "modifier le calcul des agents. Le cours en détaille les applications en les "
  "rattachant à chaque défaillance : pour le monopole, les lois antitrust, "
  "avec le Sherman Act de 1890, l’interdiction de certaines fusions et le "
  "contrôle de la concurrence ; pour les biens communs, les quotas de pêche, "
  "la limitation de l’accès aux ressources et la protection contre la "
  "surexploitation, en référence à Hardin ; pour les externalités négatives, "
  "les normes environnementales — normes d’émission, de production, de "
  "procédés, de qualité — avec pour exemples l’interdiction des sacs "
  "plastiques, les normes automobiles et l’interdiction de certains "
  "emballages ; pour les asymétries d’information, la protection du "
  "consommateur par garanties légales, étiquetage et obligation d’information, "
  "la garantie légale de conformité étant portée à douze mois. Le cours "
  "mentionne enfin une forme particulière de réglementation, l’encadrement des "
  "prix : puisque l’État est en charge de l’allocation des ressources et que "
  "le marché est défaillant, une solution consiste à fixer un prix plafond ou "
  "un prix plancher, le prix plancher étant un prix minimum qui s’impose au "
  "marché, dont l’exemple typique est le SMIC. Les limites sont énumérées avec "
  "précision et constituent l’essentiel du dossier : la réglementation est peu "
  "incitative, puisqu’on respecte la norme mais sans faire mieux ; elle est "
  "sensible au lobbying ; elle est peu flexible ; elle présente un risque de "
  "contournement ; elle n’est pas toujours efficace économiquement. S’y ajoute "
  "l’effet des prix administrés : toute intervention empêchant le prix de "
  "s’ajuster librement peut réduire les quantités échangées, créer une perte "
  "sèche et rendre l’allocation sous-optimale.",
  [("La prescription directe du comportement",
    "La règle définit ce qui est permis et ce qui est interdit : le résultat "
    "devient prévisible, mais l’agent perd la possibilité de choisir le moyen "
    "le moins coûteux d’atteindre l’objectif."),
   ("L’effet de seuil",
    "Une norme fixe une cible et non une pente : une fois le niveau exigé "
    "atteint, l’agent n’a plus aucun intérêt à faire mieux, de sorte que "
    "l’incitation à l’amélioration continue disparaît."),
   ("La vulnérabilité au lobbying",
    "Parce qu’elle désigne explicitement des contraintes sectorielles, la "
    "règle concentre l’effort d’influence : son niveau et son calendrier "
    "deviennent l’objet d’une négociation politique."),
   ("Le contournement",
    "Lorsque la règle s’applique sur un périmètre limité, les agents "
    "réorganisent leurs flux pour en sortir : la mesure produit un effet sur "
    "l’indicateur réglementé sans effet sur le phénomène réel."),
   ("L’encadrement des prix et la perte sèche",
    "Un prix plafond ou plancher empêche le prix de s’ajuster librement : les "
    "quantités échangées diminuent, une perte sèche apparaît et l’allocation "
    "devient sous-optimale.")],
  [{'a': "La réglementation garantit un résultat, là où les instruments de "
         "prix ne garantissent qu’une incitation.",
    'cond': "La garantie suppose un contrôle effectif et des sanctions "
            "crédibles, sans lesquels la norme reste un affichage.",
    'lim': "Même contrôlée, elle peut être neutralisée par une réorganisation "
           "des flux, ce que le cours appelle le risque de contournement."},
   {'a': "Elle est indispensable lorsque le comportement visé doit être "
         "éliminé et non simplement réduit à un optimum.",
    'cond': "L’argument vaut pour les pratiques jugées inacceptables en "
            "elles-mêmes, pour lesquelles un prix reviendrait à autoriser "
            "contre paiement.",
    'lim': "Étendue au-delà, elle supprime tout arbitrage coût-avantage et "
           "impose des coûts de mise en conformité très inégaux selon les "
           "agents."},
   {'a': "Elle est le seul instrument adapté aux asymétries d’information, qui "
         "appellent une révélation et non une tarification.",
    'cond': "Le remède suppose que l’information exigée soit vérifiable et que "
            "la fausse déclaration soit sanctionnable.",
    'lim': "Il reste exposé à la capture : le cours rappelle que l’État peut "
           "produire des réglementations capturées par des intérêts privés."},
   {'a': "Elle permet d’encadrer les prix lorsque le marché seul produirait "
         "des résultats jugés inacceptables.",
    'cond': "L’encadrement suppose d’en accepter le coût, puisque toute "
            "entrave à l’ajustement du prix réduit les quantités échangées.",
    'lim': "Le cours relève que ces interventions provoquent soit une "
           "surproduction soit une pénurie, et encouragent parfois des "
           "comportements illégaux."}],
  [{'t': "Les instruments de prix sont supérieurs, car ils obtiennent le même "
         "résultat au moindre coût collectif.",
    'qui': "La logique pigouvienne, que le cours oppose à l’action par les "
           "règles.",
    'rep': "L’argument est juste en efficacité, et le cours admet que la "
           "réglementation n’est pas toujours efficace économiquement ; mais "
           "elle garantit un niveau que le prix ne garantit pas."},
   {'t': "La règle est contournable, donc inefficace dès lors qu’elle est "
         "appliquée à petite échelle.",
    'qui': "Le constat que le cours tire de la taxe sur les colis aériens.",
    'rep': "L’objection ne condamne pas l’instrument mais impose de choisir le "
           "bon niveau de gouvernance : une règle isolée est inefficace si les "
           "acteurs disposent d’arbitrages spatiaux et logistiques."},
   {'t': "Les prix administrés, plafonds comme planchers, créent finalement "
         "plus de problèmes qu’ils n’en résolvent.",
    'qui': "L’analyse des prix plafond et plancher que le cours développe.",
    'rep': "Le coût est réel — réduction des quantités échangées, perte sèche, "
           "allocation sous-optimale — mais le cours note qu’un prix plancher "
           "peut être efficace en situation de monopsone, où c’est "
           "l’acheteur qui est price maker."},
   {'t': "La réglementation finit par être capturée par les intérêts privés "
         "qu’elle était censée encadrer.",
    'qui': "L’école des choix publics, qui dénonce des réglementations "
           "capturées par des intérêts privés.",
    'rep': "L’objection est sérieuse et rejoint la sensibilité au lobbying que "
           "le cours relève ; elle impose de comparer deux imperfections "
           "plutôt que de supposer un régulateur neutre."}],
  [{'n': "Arthur Pigou",
    'i': "Mieux vaut corriger les prix que prescrire les comportements.",
    'p': "Le cours oppose son action par les prix à l’action par les règles et "
         "en tire la comparaison décisive : la taxe est incitative, flexible "
         "et efficace économiquement, là où la norme produit un effet de seuil "
         "et manque de flexibilité."},
   {'n': "Garrett Hardin",
    'i': "Un bien commun non régulé est surexploité, ce qui justifie de "
         "limiter l’accès à la ressource.",
    'p': "Le cours lui rattache explicitement les instruments réglementaires "
         "appliqués aux communs : quotas de pêche, limitation de l’accès aux "
         "ressources et protection contre la surexploitation."},
   {'n': "James Buchanan",
    'i': "L’État n’incarne pas automatiquement l’intérêt général : il est "
         "une somme d’intérêts individuels.",
    'p': "Son école des choix publics fournit la critique la plus structurée "
         "de la réglementation : l’État peut agir pour des raisons "
         "électoralistes, favoriser des groupes organisés, créer des "
         "politiques inefficaces et produire des réglementations capturées par "
         "des intérêts privés."},
   {'n': "Richard Musgrave",
    'i': "Certains biens sont tutélaires, pris en charge par l’État et mis à "
         "disposition quasi gratuitement.",
    'p': "Le cours mentionne sa notion à propos des cas où l’État décide de "
         "produire au lieu de subventionner ou de taxer : la réglementation "
         "n’est alors plus un encadrement du marché mais sa substitution par "
         "l’offre publique."}],
  [{'f': "Le cours énumère trois grandes familles de solutions : l’action par "
         "les règles, l’action par les prix avec Pigou, l’action par les "
         "quantités avec Coase.",
    'p': "Le classement situe la réglementation comme l’une des trois voies "
         "possibles, ce qui empêche d’en faire l’intervention publique par "
         "défaut."},
   {'f': "Les limites de la réglementation sont qu’elle est peu incitative, "
         "sensible au lobbying, peu flexible, contournable et pas toujours "
         "efficace économiquement.",
    'p': "Les cinq limites couvrent l’incitation, le processus politique, "
         "l’adaptabilité, l’application et l’efficience : elles fournissent "
         "cinq angles distincts de discussion."},
   {'f': "Le prix plancher est un prix minimum qui s’impose au marché, dont "
         "l’exemple typique est le SMIC.",
    'p': "L’exemple relie la microéconomie des défaillances au marché du "
         "travail et permet de discuter l’encadrement des prix sur un cas "
         "concret."},
   {'f': "Toute intervention de l’État qui empêche le prix de s’ajuster "
         "librement peut réduire les quantités échangées, créer une perte "
         "sèche et rendre l’allocation sous-optimale.",
    'p': "L’énoncé donne le coût théorique des prix administrés et permet de "
         "le mettre en balance avec l’objectif social poursuivi."}],
  [{'q': "Sujet du type « La réglementation est-elle le bon instrument de "
         "l’intervention publique ? »",
    'f': "Elle garantit un résultat mais au prix de cinq défauts que le cours "
         "énumère : elle est peu incitative, puisqu’on respecte la norme mais "
         "sans faire mieux ; elle est sensible au lobbying ; elle est peu "
         "flexible ; elle présente un risque de contournement ; elle n’est pas "
         "toujours efficace économiquement. L’action par les prix est à "
         "l’inverse incitative, flexible et efficace économiquement, mais "
         "suppose de mesurer le coût externe et se heurte à une faible "
         "acceptabilité politique.",
    'r': "Le raisonnement oppose une garantie de résultat à une efficacité de "
         "coût, ce qui permet de conclure selon la nature du dommage plutôt "
         "que par préférence doctrinale.",
    'ex': "L’interdiction des sacs plastiques, où l’objectif est "
          "l’élimination d’un usage et non sa réduction optimale."},
   {'q': "Sujet du type « Faut-il encadrer les prix ? »",
    'f': "Le cours rappelle d’abord le coût théorique : toute intervention "
         "empêchant le prix de s’ajuster librement peut réduire les quantités "
         "échangées, créer une perte sèche et rendre l’allocation "
         "sous-optimale, ces interventions provoquant soit une surproduction "
         "soit une pénurie. Mais il introduit une exception importante : un "
         "prix plancher peut être efficace en situation de monopsone, où c’est "
         "l’acheteur qui devient price maker.",
    'r': "Le raisonnement montre que le jugement dépend de la structure du "
         "marché sous-jacent : ce qui est une distorsion en concurrence "
         "devient une correction face à un acheteur en position de force.",
    'ex': "Le SMIC, prix plancher qui s’impose au marché du travail et "
          "protège les salariés les moins qualifiés."}],
  voisins=['n6-taxation', 'n6-externalites', 'n6-defaillances-etat',
           'n4-reglementation-env'])


d('n6-taxation', 6, "Taxation et subventions",
  "Corriger les prix pour qu’ils reflètent le coût ou le bénéfice social",
  "La taxation et les subventions constituent l’action par les prix, associée "
  "à Arthur Pigou : il s’agit de corriger les prix pour qu’ils reflètent le "
  "vrai coût ou le vrai bénéfice pour la société. À une externalité négative "
  "répond une taxe pigouvienne selon le principe pollueur-payeur ; à une "
  "externalité positive répond une subvention destinée à rémunérer le bénéfice "
  "collectif créé.",
  "L’action par les prix est l’instrument le plus satisfaisant "
  "économiquement, et son analyse doit être menée dans les deux sens. Du côté "
  "de la taxe : faire payer à l’entreprise le coût qu’elle impose à la société "
  "a pour effet d’augmenter le coût marginal privé, de le rendre égal au coût "
  "social, de faire monter le prix et baisser la quantité, donc de revenir à "
  "l’optimum collectif. Du côté de la subvention : rémunérer le bénéfice "
  "collectif créé abaisse le coût, fait baisser le prix et augmenter la "
  "quantité jusqu’à la production socialement optimale. Le bilan que le cours "
  "en dresse est contrasté et doit être repris intégralement. Trois "
  "avantages : l’instrument est incitatif, flexible et efficace "
  "économiquement, parce qu’il laisse chaque agent choisir comment réduire au "
  "lieu de lui imposer un comportement. Trois limites : la difficulté de "
  "mesurer précisément le coût externe, une acceptabilité politique faible, et "
  "un effet inflationniste possible. Deux prolongements complètent le "
  "dossier. Le premier concerne l’efficacité des subventions : le cours "
  "analyse l’effet d’aubaine, qui apparaît lorsqu’un agent bénéficie d’une "
  "aide publique alors qu’il aurait adopté le même comportement en son "
  "absence ; l’aide ne change pas la décision, elle réduit simplement le coût, "
  "de sorte que la subvention ne crée pas d’effet supplémentaire mais "
  "constitue un transfert financier, avec un coût budgétaire élevé sans effet "
  "additionnel équivalent. Le second concerne l’alternative à la "
  "taxation : il arrive que l’État décide de produire au lieu de subventionner "
  "ou de taxer, ce que Musgrave analyse par la notion de bien tutélaire, bien "
  "institutionnellement pris en charge par l’État et mis à disposition de la "
  "population quasi gratuitement, financé par l’impôt. Reste enfin la critique "
  "la plus radicale, celle de l’école des choix publics : l’État qui taxe et "
  "subventionne est lui-même soumis à des défaillances.",
  [("L’internalisation du coût externe",
    "La taxe relève le coût marginal privé jusqu’au niveau du coût social : "
    "l’entreprise intègre alors dans son calcul le dommage qu’elle cause, sans "
    "que l’activité soit interdite."),
   ("L’ajustement du prix et de la quantité",
    "Le coût de production augmentant, le prix monte et la quantité diminue "
    "jusqu’au niveau socialement optimal : la correction opère par le marché "
    "et non contre lui."),
   ("Le mécanisme symétrique de la subvention",
    "Pour une externalité positive, la subvention abaisse le coût, fait "
    "baisser le prix et augmenter la quantité : le raisonnement est "
    "exactement inverse et appelle le même critère d’évaluation."),
   ("La liberté laissée à l’agent",
    "Contrairement à une norme, le prix n’impose pas comment réduire : chaque "
    "agent compare le montant du prélèvement au coût de sa propre adaptation, "
    "de sorte que l’effort se concentre là où il est le moins coûteux."),
   ("Le risque d’effet d’aubaine",
    "Une aide versée à un agent qui aurait agi de même sans elle ne modifie "
    "aucune décision : elle réduit un coût privé sans produire d’effet "
    "additionnel, et constitue alors un pur transfert.")],
  [{'a': "La taxation est incitative, flexible et efficace économiquement, "
         "puisqu’elle laisse chaque agent choisir ses moyens d’adaptation.",
    'cond': "L’efficacité suppose que des solutions alternatives existent et "
            "que le taux soit suffisamment élevé pour peser sur les "
            "décisions.",
    'lim': "Pour des usages sans substitut à court terme, la taxe pèse sur le "
           "pouvoir d’achat sans modifier les comportements."},
   {'a': "Elle fournit des recettes publiques, à la différence de la "
         "réglementation qui n’en produit aucune.",
    'cond': "L’affectation des recettes est une décision distincte, dont "
            "dépend largement l’acceptabilité de la mesure.",
    'lim': "Une compensation proportionnelle à la consommation taxée annule "
           "une partie de l’incitation qu’elle devait rendre acceptable."},
   {'a': "La subvention permet de faire produire des activités à bénéfice "
         "collectif que le marché sous-produit.",
    'cond': "L’aide n’est justifiée que si l’action financée n’aurait pas eu "
            "lieu sans elle, critère d’additionnalité.",
    'lim': "Le cours décrit précisément le cas contraire, l’effet d’aubaine, "
           "où certaines entreprises auraient embauché des apprentis même sans "
           "prime, la subvention devenant un transfert sans création d’emploi."},
   {'a': "L’instrument peut être étendu au-delà des frontières, comme le "
         "montre l’ajustement carbone.",
    'cond': "L’extension suppose de pouvoir mesurer avec précision le contenu "
            "taxable incorporé dans les biens importés.",
    'lim': "Le cours signale que certains contestent la qualification de taxe "
           "pour le mécanisme d’ajustement, qui n’est pas fixe et varie avec "
           "le prix du quota."}],
  [{'t': "On ne sait pas mesurer précisément le coût externe, donc on ne sait "
         "pas calibrer correctement la taxe.",
    'qui': "La première limite que le cours relève pour l’action par les prix.",
    'rep': "L’objection explique le recours aux marchés de quotas, où l’État "
           "fixe une quantité et laisse le marché déterminer le prix, ce qui "
           "évite d’avoir à estimer le dommage."},
   {'t': "La subvention peut ne rien changer au comportement de l’agent et "
         "constituer un simple transfert financier.",
    'qui': "L’analyse de l’effet d’aubaine que le cours développe à propos des "
           "aides à l’apprentissage.",
    'rep': "L’objection impose un critère d’additionnalité et donc une "
           "évaluation : une aide n’est justifiée que si l’action financée "
           "n’aurait pas eu lieu sans elle."},
   {'t': "Les effets pervers conduisent les agents à contourner la mesure, ce "
         "qui déplace le problème au lieu de l’éradiquer.",
    'qui': "La critique du contournement que le cours formule à propos des "
           "instruments fiscaux.",
    'rep': "Le cours donne l’exemple du déplacement d’échelle : en fuyant "
           "l’Europe on résout le problème au niveau européen mais on le "
           "déplace au niveau mondial."},
   {'t': "L’État qui taxe et subventionne est lui-même soumis à des "
         "défaillances qui peuvent aggraver le marché.",
    'qui': "L’école des choix publics, qui répond à Pigou que l’État est "
           "imparfait et peut aggraver le marché.",
    'rep': "L’objection est de poids mais symétrique : elle impose de comparer "
           "deux imperfections, et ne rétablit pas l’efficacité d’un marché "
           "dont les prix ignorent le coût social."}],
  [{'n': "Arthur Pigou",
    'i': "Il faut corriger les prix pour qu’ils reflètent le vrai coût ou le "
         "vrai bénéfice pour la société.",
    'p': "Le cours situe sa proposition dans les années 1920 et en tire le "
         "principe pollueur-payeur : la taxe augmente le coût marginal privé, "
         "le coût devient social, le prix monte, la quantité baisse, et l’on "
         "retrouve l’optimum collectif."},
   {'n': "Arthur Pigou",
    'i': "L’externalité positive appelle une subvention, symétrique de la taxe "
         "sur l’externalité négative.",
    'p': "C’est un second apport, souvent oublié : la subvention rémunère le "
         "bénéfice collectif créé, ce qui abaisse le coût, fait baisser le "
         "prix et augmenter la quantité jusqu’à la production socialement "
         "optimale."},
   {'n': "Richard Musgrave",
    'i': "Certains biens sont institutionnellement pris en charge par l’État.",
    'p': "Le cours introduit sa notion de bien tutélaire à propos des cas où "
         "l’État décide de produire au lieu de subventionner ou de taxer : le "
         "bien est mis à disposition de la population quasi gratuitement et "
         "financé par l’impôt."},
   {'n': "James Buchanan",
    'i': "Même quand l’État veut corriger une défaillance du marché, il peut "
         "agir pour des raisons électoralistes.",
    'p': "Son école des choix publics fournit la critique centrale de "
         "l’instrument fiscal : l’État peut favoriser des groupes organisés, "
         "créer des politiques inefficaces et produire des effets pervers, de "
         "sorte que l’intervention n’est ni neutre ni nécessairement efficace."}],
  [{'f': "Le cours attribue à l’action par les prix trois avantages — "
         "incitative, flexible, efficace économiquement — et trois limites : "
         "difficulté de mesurer le coût externe, acceptabilité politique "
         "faible, effet inflationniste possible.",
    'p': "Le bilan équilibré évite de présenter la taxe pigouvienne comme la "
         "solution évidente et fournit la matière d’une discussion complète."},
   {'f': "L’effet d’aubaine apparaît lorsqu’un agent bénéficie d’une aide "
         "publique alors qu’il aurait adopté le même comportement en son "
         "absence.",
    'p': "La définition fournit le critère d’évaluation des subventions : "
         "l’additionnalité, c’est-à-dire l’effet propre de l’aide sur la "
         "décision."},
   {'f': "Le cours illustre l’effet d’aubaine par l’apprentissage : certaines "
         "entreprises auraient embauché des apprentis même sans prime, de "
         "sorte que la subvention ne crée pas d’emploi supplémentaire mais "
         "constitue un transfert financier.",
    'p': "L’exemple montre qu’une politique peut être coûteuse "
         "budgétairement et sans effet additionnel équivalent, ce qui appelle "
         "un meilleur ciblage plutôt qu’un abandon."},
   {'f': "Il arrive que l’État décide de produire au lieu de subventionner ou "
         "de taxer, ce que Musgrave analyse par la notion de bien tutélaire.",
    'p': "Le fait complète la panoplie : au-delà du prix, de la quantité et de "
         "la règle, l’offre publique directe constitue un quatrième mode "
         "d’intervention."}],
  [{'q': "Sujet du type « Faut-il taxer ou réglementer ? »",
    'f': "Le cours tranche en faveur de l’efficacité tout en reconnaissant ses "
         "limites. L’action par les prix est incitative, flexible et efficace "
         "économiquement, parce qu’elle laisse chaque agent choisir comment "
         "s’adapter ; la réglementation est au contraire peu incitative, "
         "puisqu’on respecte la norme sans faire mieux, peu flexible et "
         "contournable. Mais la taxe suppose de mesurer précisément le coût "
         "externe, se heurte à une acceptabilité politique faible et peut "
         "avoir un effet inflationniste.",
    'r': "Le raisonnement oppose deux séries de propriétés plutôt que deux "
         "doctrines, ce qui permet de choisir l’instrument selon la "
         "mesurabilité du dommage et l’existence de solutions alternatives.",
    'ex': "Le principe pollueur-payeur, qui fait payer à l’entreprise le coût "
          "qu’elle impose à la société sans lui interdire de produire."},
   {'q': "Sujet du type « Les aides publiques sont-elles efficaces ? »",
    'f': "Le critère décisif est l’additionnalité, et le cours le formule par "
         "l’effet d’aubaine : il y a effet d’aubaine lorsqu’un agent bénéficie "
         "d’une aide publique alors qu’il aurait adopté le même comportement "
         "en son absence. L’aide ne change alors pas la décision, elle réduit "
         "simplement le coût, de sorte que la subvention ne crée pas d’effet "
         "supplémentaire mais constitue un transfert financier, avec un coût "
         "budgétaire élevé sans effet additionnel équivalent.",
    'r': "Le raisonnement substitue au critère de volume un critère d’effet "
         "propre, ce qui déplace la discussion du montant vers le ciblage et "
         "l’évaluation.",
    'ex': "Les primes à l’apprentissage, dont certaines bénéficient à des "
          "entreprises qui auraient embauché de toute façon."}],
  voisins=['n6-externalites', 'n6-reglementation', 'n6-defaillances-etat',
           'n4-fiscalite-eco'])
